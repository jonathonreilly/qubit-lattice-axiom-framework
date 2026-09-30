"""T46 P1: RG-covariant discriminator for the 5/6 bridge.  See PREREGISTRATION.md."""
import numpy as np
from fractions import Fraction
from qcdrun import QCD

rng = np.random.default_rng(46)
V_ATLAS = 0.103303816122/np.sqrt(6)            # atlas |V_cb|
R_PRED = V_ATLAS**(6/5)
print(f"V_cb atlas = {V_ATLAS:.8f}   R_pred = V^(6/5) = {R_PRED:.8f}")

# central inputs (recalled PDG-style; same central values as repo comparators)
MS2, MB = 0.0934, 4.180
q = QCD()
print("alpha_s: MZ %.4f  m_b %.4f  2GeV %.4f  m_t %.4f" %
      (q.asMZ, q.alpha_s(4.18), q.alpha_s(2.0), q.alpha_s(163.0)))
print("repo comparators: alpha_s(2 GeV)=0.2965  alpha_s(m_b)=0.2265  (July note) ;  0.3026 / 0.2211 (Apr note)")

# --- Check A: R(mu) constant?
print("\nCheck A: R(mu) = m_s(mu)/m_b(mu) with m_s(2GeV)=0.0934, m_b(m_b)=4.18")
mus = [2.0, 3.0, 4.18, 5.0, 10., 30., 91.19, 163., 1000.]
Rs = []
for mu in mus:
    ms = q.mass(MS2, 2.0, mu); mb = q.mass(MB, 4.18, mu)
    Rs.append(ms/mb)
    print(f" mu={mu:8.2f}  m_s={ms*1e3:8.3f} MeV  m_b={mb:7.4f} GeV  R={ms/mb:.6f}")
Rs = np.array(Rs)
print(" spread over mu>=m_b (nf=5 region):  (max-min)/mean = %.4f%%" %
      (100*(Rs[2:].max()-Rs[2:].min())/Rs[2:].mean()))
R_common = q.mass(MS2, 2.0, 4.18)/MB
print(f" R_common (mu=m_b) = {R_common:.6f}   repo: 81.0/4180 = {81.0/4180:.6f}")
T = MS2/q.mass(MS2, 2.0, 4.18)
print(f" transport m_s(2)/m_s(m_b) = {T:.5f}   (July note 1.13799 / 1.14747; April 1.1530 from PDG)")

# --- Check B: Monte Carlo
N = 20000
d = []
for _ in range(N):
    ms2 = rng.normal(0.0934, 0.0008)
    mb = rng.normal(4.180, 0.025)
    asz = rng.normal(0.1180, 0.0009)
    mc = rng.normal(1.27, 0.02)
    qq = QCD(asMZ=asz, mc=mc, mb=mb)
    R = qq.mass(ms2, 2.0, mb)/mb
    d.append((R, ms2/mb))
d = np.array(d)
Rc, Rs_ = d[:, 0], d[:, 1]
print(f"\nCheck B: R_common = {Rc.mean():.6f} +- {Rc.std():.6f}  ({100*Rc.std()/Rc.mean():.2f}%)")
print(f"         R_threshold-local (93.4/4180) = {Rs_.mean():.6f} +- {Rs_.std():.6f}")
Dc = R_PRED/Rc - 1
Dl = R_PRED/Rs_ - 1
print(f" Delta(common)  = R_pred/R_common - 1  = {100*Dc.mean():+.2f}% +- {100*Dc.std():.2f}%  -> {Dc.mean()/Dc.std():.1f} sigma")
print(f" Delta(local)   = R_pred/R_local  - 1  = {100*Dl.mean():+.2f}% +- {100*Dl.std():.2f}%  -> {Dl.mean()/Dl.std():.1f} sigma")

# implied exponent on the common surface for the atlas V_cb, and for data V_cb
print("\nImplied exponent p = ln V / ln R on the RG-covariant common surface:")
for label, V in (("atlas 0.042174", V_ATLAS), ("inclusive-like 0.0422", 0.0422),
                 ("PDG-avg-like 0.0408", 0.0408), ("exclusive-like 0.0391", 0.0391)):
    p = np.log(V)/np.log(Rc)
    print(f" V_cb={label:24s}  p = {p.mean():.4f} +- {p.std():.4f}   (5/6 = {5/6:.4f}; gap {(p.mean()-5/6)/p.std():+.1f} sigma from R only)")

# --- Check D: prefactor
c = V_ATLAS/Rc**(5/6)
print(f"\nCheck D: prefactor needed for exponent 5/6 on common surface: c = V/R^(5/6) = {c.mean():.4f} +- {c.std():.4f}")
print(f"         2^(1/6) = {2**(1/6):.4f}   9/8 = 1.125   (numerology not claimed)")
c_loc = V_ATLAS/Rs_**(5/6)
print(f"         same on the threshold-local surface: c = {c_loc.mean():.4f} +- {c_loc.std():.4f}")

# --- Check C: look-elsewhere
print("\nCheck C: look-elsewhere")
nine = {'C_F-T_F':5/6, '6/7':6/7, '8/9':8/9, '3/4':3/4, '5/8':5/8, 'T_F':1/2, '1':1.0, 'C_F':4/3, 'C_A-C_F':5/3}
R_loc = Rs_.mean(); R_com = Rc.mean()
# exponent implied by each surface for the atlas V
p_loc = np.log(V_ATLAS)/np.log(R_loc); p_com = np.log(V_ATLAS)/np.log(R_com)
print(f" p_local = {p_loc:.4f}   p_common = {p_com:.4f}")
def dev(p, R): return V_ATLAS**(1/p)/R - 1
for k, p in nine.items():
    print(f"  {k:8s} p={p:.4f}: dev(local) {100*dev(p,R_loc):+8.2f}%   dev(common) {100*dev(p,R_com):+8.2f}%")
# how likely is a hit within 0.2% at random?  window in p:
# d ln R_pred / dp = -ln V / p^2 ; 0.2% in R -> dp
dp = 0.002/(-np.log(V_ATLAS)/(5/6)**2)
print(f" a 0.2% window in R is a window of +-{dp:.4f} in p, i.e. width {2*dp:.4f}")
span = 5/3 - 0.5
p_hit_9 = 9*2*dp/span
print(f" chance that one of 9 uniformly scattered exponents on [0.5,1.667] falls in a given 0.2% window: {100*p_hit_9:.1f}%")
print(" ... with 3 candidate surfaces (local 2GeV/m_b, common m_b, common 2GeV): ~%.0f%%" % (100*(1-(1-p_hit_9)**3)))
# Farey: rationals a/b, b<=6 and b<=9 in [0.5, 1.7]
def farey(bmax, lo=0.5, hi=1.7):
    s = set()
    for b in range(1, bmax+1):
        for a in range(1, int(hi*b)+1):
            f = Fraction(a, b)
            if lo <= f <= hi: s.add(f)
    return sorted(s)
for bmax in (6, 9):
    F = farey(bmax)
    print(f" rationals with denominator <= {bmax}: {len(F)} in [0.5,1.7]; mean spacing {np.mean(np.diff([float(x) for x in F])):.3f}")
# probability that ANY rational with b<=6 lies within the 1-sigma exponent window of a given surface
sig_p = np.std(np.log(V_ATLAS)/np.log(Rc))
F6 = [float(x) for x in farey(6)]
print(f" exponent sigma from mass errors on common surface: {sig_p:.4f}")
# Monte Carlo on random 'true exponent' positions: fraction with some b<=6 rational within 1 sigma
u = rng.uniform(0.5, 1.7, 200000)
arr = np.array(F6)
idx = np.searchsorted(arr, u)
lo_ = arr[np.clip(idx-1, 0, len(arr)-1)]; hi_ = arr[np.clip(idx, 0, len(arr)-1)]
nearest = np.minimum(np.abs(u-lo_), np.abs(u-hi_))
print(f" P(some rational with denominator<=6 within +-1 sigma of a random exponent) = {100*np.mean(nearest<sig_p):.0f}%")
print(f" P(... within 0.2%-in-R window, +-{dp:.4f}) = {100*np.mean(nearest<dp):.0f}%")
# what rationals with b<=6 lie within 2 sigma of p_common?
near = [(x, abs(x-p_com)/sig_p) for x in F6 if abs(x-p_com) < 3*sig_p]
print(" rationals (b<=6) within 3 sigma of p_common:", [(str(Fraction(x).limit_denominator(6)), round(s, 1)) for x, s in near])
