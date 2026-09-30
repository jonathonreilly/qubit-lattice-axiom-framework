#!/usr/bin/env python3
"""T55 test: scan strength, m/alpha_X degeneracy, and the T1 effective-potential ladder.
Reads (never writes) the repo checkout for the canonical constants."""
import sys, math, itertools
import numpy as np
sys.path.insert(0, "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts")
from canonical_plaquette_surface import (CANONICAL_ALPHA_BARE as A_BARE, CANONICAL_ALPHA_LM as A_LM,
                                         CANONICAL_ALPHA_S_V as A_SV, CANONICAL_U0 as U0)
PI = math.pi
M_PL = 1.2209e19
V = M_PL * (7/8)**0.25 * A_LM**16
G_STAR, X_F, R, ETA_OBS, BBN, KT = 106.75, 25.0, (31/9)*1.59, 6.12e-10, 3.65e7, 1.07e9
def C_of(a): return KT*X_F/(math.sqrt(G_STAR)*M_PL*PI*a*a*R*BBN)
def m_target(a): return math.sqrt(ETA_OBS/C_of(a))
M_T = m_target(A_LM); LAM = M_T/A_LM
print(f"v = {V:.4f} GeV ; m_target(alpha_LM) = {M_T:.2f} GeV = {M_T/V:.3f} v ; 16 v = {16*V:.2f} ; dev = {16*V/M_T-1:+.4f}")
print(f"Lambda* = m/alpha_X = {LAM:.1f} GeV = {LAM/V:.2f} v   (m_target is linear in alpha_X: check {m_target(0.03)/0.03:.1f}, {m_target(0.12)/0.12:.1f})")

# ---------------- families ----------------
BLOCKS = [("alpha_LM",A_LM),("u_0",U0),("pi",PI),("2",2.0),("3",3.0),("N_c",3.0),("N_sites",16.0),
          ("hw_dark",3.0),("R_base",31/9),("alpha_s(v)",A_SV),("dim_adj",8.0)]
def fam(powers):
    out=[]
    for n,x in BLOCKS:
        for p in powers: out.append((f"{n}^{p}",x**p))
    return out
F22 = fam([1,-1]); F44 = fam([2,1,-1,-2])
print(f"F22: {len(F22)} entries, {len({round(v,9) for _,v in F22})} distinct values; F44: {len(F44)} entries, {len({round(v,9) for _,v in F44})} distinct")

def window_coverage(vals, tol, lo, hi):
    """fraction of ln-uniform targets t in [lo,hi] with some value within relative tol of t."""
    xs = np.exp(np.linspace(math.log(lo), math.log(hi), 200001))
    hit = np.zeros_like(xs, bool)
    for v in vals: hit |= (np.abs(v/xs-1) < tol)
    return hit.mean()

tm = M_T/V   # 15.68 in units of v
lo, hi = tm/math.sqrt(10), tm*math.sqrt(10)
vals22 = [v for _,v in F22]; vals44 = [v for _,v in F44]
print("\n== A1: base rate for a hit in a random target window (factor-10 window centred on 15.68 v) ==")
for name, vals in (("F22",vals22),("F44",vals44)):
    for tol in (0.05,0.108):
        print(f"  {name} tol {tol:.3f}: P(some multiplier within tol of a random target) = {window_coverage(vals,tol,lo,hi):.3f}")
print("  window sensitivity (F22, tol 5%): "+"; ".join(f"[{tm/w:.2f},{tm*w:.1f}] v: {window_coverage(vals22,0.05,tm/w,tm*w):.3f}" for w in (2,3.16,10,30)))
print("  family's own span [1/16, 16] v (target at the top edge): "+f"{window_coverage(vals22,0.05,1/16,16.0):.3f} ; [1, 100] v: {window_coverage(vals22,0.05,1.0,100.0):.3f}")
# actual hits at the target
for name, fm in (("F22",F22),("F44",F44)):
    for tol in (0.05,0.108):
        hits=[(n,v,v/tm-1) for n,v in fm if abs(v/tm-1)<tol]
        print(f"  {name} hits at 15.68 v, tol {tol:.3f}: "+"; ".join(f"{n}={v:.3f} ({d:+.3f})" for n,v,d in hits))

# ---------------- A2: pair scan ----------------
g2 = [0.65939, 0.6711, 0.68283]
A_FILE = [("1/(4pi)",A_BARE),("alpha_LM",A_LM),("alpha_s(v)",A_SV)] + \
         [(f"alpha_2(g={g})",g*g/(4*PI)) for g in g2] + [("1/(16pi)",1/(16*PI)),("0.048 cosmo-note",0.048)]
print("\n== A2: pairs (m_i = F * v, alpha_j) with m_i/alpha_j within tol of Lambda* ==")
print("  couplings:", ", ".join(f"{n}={a:.5f}" for n,a in A_FILE))
def pairs(fm, tol):
    out=[]
    for (n,mult) in fm:
        for (an,a) in A_FILE:
            dev = (mult*V/a)/LAM - 1
            if abs(dev)<tol: out.append((n,mult,an,a,dev))
    return out
for name, fm in (("F22",F22),("F44",F44)):
    for tol in (0.05,0.108):
        P = pairs(fm,tol)
        # distinct by (rounded mult, rounded alpha)
        distinct = {(round(m,6),round(a,6)) for _,m,_,a,_ in P}
        print(f"  {name} tol {tol:.3f}: {len(P)} labelled pairs, {len(distinct)} distinct (m,alpha)")
        for n,m,an,a,dev in P: print(f"      {n:14s} ({m:8.4f} v) x {an:18s} ({a:.5f})  dev {dev:+.3f}")
# the Wilson-bare 6 v (Origin B first factor) with each coupling
print("  Wilson-bare 6 v (2 r hw_dark v, A0) against each coupling on file:")
for an,a in A_FILE:
    dev = (6*V/a)/LAM-1
    print(f"      6 v x {an:18s} dev {dev:+.3f}")
print(f"      alpha_X needed for exactly 6 v: {A_LM*6*V/M_T:.5f}  -> g_2 = {math.sqrt(4*PI*A_LM*6*V/M_T):.5f} (repo interval [0.65939, 0.68283])")
print(f"      eta_pred(6 v, alpha_LM) = {ETA_OBS*(6*V/M_T)**2:.3e}  (obs 6.12e-10)")

# pair-family random-target coverage: shift Lambda* log-uniformly over the factor-10 window
lam_lo, lam_hi = LAM/math.sqrt(10), LAM*math.sqrt(10)
pair_vals = sorted({m*V/a for _,m in F44 for _,a in A_FILE})
xs = np.exp(np.linspace(math.log(lam_lo), math.log(lam_hi), 200001))
for tol in (0.05,0.108):
    hit=np.zeros_like(xs,bool)
    for pv in pair_vals: hit |= (np.abs(pv/xs-1)<tol)
    print(f"  F44 x A_file, tol {tol:.3f}: P(random Lambda has >=1 pair within tol) = {hit.mean():.3f} ({len(pair_vals)} distinct ratios)")
# with alpha_LM only, F44, for comparison
pv1 = sorted({m*V/A_LM for _,m in F44})
for tol in (0.05,0.108):
    hit=np.zeros_like(xs,bool)
    for pv in pv1: hit |= (np.abs(pv/xs-1)<tol)
    print(f"  F44 x alpha_LM only, tol {tol:.3f}: coverage = {hit.mean():.3f}")

# ---------------- A3: the response of the scan to alpha_X ----------------
print("\n== A3: what the same F22 scan returns if alpha_X is not alpha_LM ==")
for an,a in A_FILE + [("0.03",0.03),("0.05",0.05),("0.10",0.10)]:
    t = m_target(a)/V
    best = min(F22+[("6 (Wilson bare)",6.0)], key=lambda nv: abs(nv[1]/t-1))
    inF22 = min(F22, key=lambda nv: abs(nv[1]/t-1))
    print(f"  alpha_X = {a:.5f} ({an:18s}) target {t:7.3f} v ; best F22: {inF22[0]:11s} dev {inF22[1]/t-1:+.3f}"
          f"{'  <-- within 5%' if abs(inF22[1]/t-1)<0.05 else ''}")
# fraction of log-uniform alpha_X in [0.03,0.12] with an F22 hit within 5 %
print(f"  fraction of ln-uniform alpha_X in [0.03,0.12] with an F22 hit <5%: {window_coverage(vals22,0.05,m_target(0.03)/V,m_target(0.12)/V):.3f}; F44: {window_coverage(vals44,0.05,m_target(0.03)/V,m_target(0.12)/V):.3f}")

# ---------------- A4: rationals near the 'bridge factor' ----------------
need = tm/6
rats = sorted({(p,q) for q in range(1,7) for p in range(1,25) if math.gcd(p,q)==1 and abs(p/q/need-1)<0.05})
print(f"\n== A4: factor needed to lift 6 v to the target = {need:.4f}; reduced p/q (p<=24,q<=6) within 5%: "
      + ", ".join(f"{p}/{q}={p/q:.3f}" for p,q in rats) + f"  (8/3 = {8/3:.3f}, dev {8/3/need-1:+.3f})")

# ---------------- B: T1 effective-potential ladder ----------------
print("\n== B: T1 operator on the 2^4 block, curvature ladder ==")
sites = list(itertools.product([0,1],repeat=4)); idx={s:i for i,s in enumerate(sites)}
def Dmat(u0):
    D=np.zeros((16,16))
    for s in sites:
        for mu in range(4):
            eta = (-1)**sum(s[:mu])
            t=list(s); t[mu]^=1; t=tuple(t)
            # forward hop from s_mu=0 to 1: +; from 1 to 0 wraps antiperiodically: -
            sgn = 1.0 if s[mu]==0 else -1.0
            D[idx[s],idx[t]] += u0*eta*sgn
    return D
D = Dmat(U0)
print(f"  D^2 + 4 u0^2 I: max abs = {np.abs(D@D+4*U0**2*np.eye(16)).max():.2e}  (antisymmetric: {np.abs(D+D.T).max():.1e})")
def Vfun(m): return -np.log(np.linalg.det(D+m*np.eye(16)))/2 if False else -np.log(abs(np.linalg.det(D+m*np.eye(16))))
h=1e-3
Vpp = (Vfun(h)-2*Vfun(0)+Vfun(-h))/h**2
print(f"  V(m) = -ln det(D+m): finite-difference V''(0) = {Vpp:.5f} ; T1 analytic -N/(4 u0^2) = {-16/(4*U0**2):.5f}")
kappa = 1/(4*U0**2)
print(f"  per-channel kappa = 1/(4 u0^2) = {kappa:.5f} ; u0 = {U0:.6f}")
lad = {"D1 per-channel  m=v/(2u0)":math.sqrt(kappa),
       "incoherent N kappa  sqrt(N)/(2u0)":math.sqrt(16*kappa),
       "coherent N^2 kappa  N/(2u0)":math.sqrt(256*kappa),
       "coherent N^3 kappa":math.sqrt(4096*kappa)}
for k,x in lad.items(): print(f"  {k:38s}: {x:7.3f} v   dev vs 15.68 v: {x/tm-1:+.3f}")
print(f"  (u0 -> 1: per-channel 0.5, sqrt(N)/2 = 2, N/2 = 8, N^1.5/2 = 32 v)")
print(f"  N_sites v with u0 removed = 16 v needs |V''| coefficient c = {4*U0**2*256:.1f} in m^2 = c*kappa*v^2 -> c/N^2 = {4*U0**2:.4f}, i.e. a factor 2u0 = {2*U0:.4f} absent from the Higgs analogue")
print(f"  Higgs-parallel dark mass N v/(2 u0) = {16*V/(2*U0):.1f} GeV ; eta_pred = {ETA_OBS*(16*V/(2*U0)/M_T)**2:.3e} (dev {(16/(2*U0)*V/M_T)**2-1:+.2f} in eta relative to eta_obs)")

# ---------------- C: cross-section ----------------
sv = PI/LAM**2   # GeV^-2
print(f"\n== C: <sigma v> = pi/Lambda*^2 = {sv:.4e} GeV^-2 = {sv*1.1673e-17:.3e} cm^3/s  (thermal ~2e-26)")
# information content: eta band vs Planck
print(f"  bypass eta band [5.25e-10, 8.11e-10] width ratio {8.11/5.25:.2f}; Planck eta 6.12e-10 +- ~1% -> m resolution +-0.5%; 16v is {abs(16*V/M_T-1)*100:.2f}% off = {abs(16*V/M_T-1)/0.005:.1f} sigma at 0.5%")

# ---------------- A5: sensitivity of the pair-family base rate to the coupling list ----------------
print("\n== A5: coverage of random Lambda targets (factor-10 window, tol 5%) for smaller coupling lists, F44 masses ==")
lists = {
 "canonical surface only {1/4pi, alpha_LM, alpha_s(v)}": [A_BARE, A_LM, A_SV],
 "+ alpha_2 (one point, g=0.6711)": [A_BARE, A_LM, A_SV, 0.6711**2/(4*PI)],
 "+ 0.048 (cosmo note)": [A_BARE, A_LM, A_SV, 0.6711**2/(4*PI), 0.048],
 "full A_FILE (8, incl. 1/16pi and 3 alpha_2 points)": [a for _,a in A_FILE],
}
xs = np.exp(np.linspace(math.log(LAM/math.sqrt(10)), math.log(LAM*math.sqrt(10)), 200001))
for name, al in lists.items():
    pv = sorted({m*V/a for _,m in F44 for a in al})
    hit=np.zeros_like(xs,bool)
    for x in pv: hit |= (np.abs(x/xs-1)<0.05)
    P = [(n,m,a) for n,m in F44 for a in al if abs(m*V/a/LAM-1)<0.05]
    print(f"  {name:55s}: coverage {hit.mean():.3f}; pairs within 5% at the real target: {len({(round(m,6),round(a,6)) for _,m,a in P})}")
