"""T46 kill check K2: does the ~18.6% / 13 sigma common-scale miss survive STANDARD (fetched) inputs?
Sources fetched this session (copies in this folder):
  pdg_sum_quarks_2024.txt : PDG 2024 summary table  (m_s 93.5(8) MeV @2 GeV; m_c(m_c) 1.2730(46); m_b(m_b) 4.183(7))
  pdg_quarkmass_u_d_2024.txt : PDG 2024 quark-mass review, lattice-only m_s(2 GeV, N_L=4) = 92.74(54) MeV  (Eq. 60.5)
  pdg_qcd_2024.txt : alpha_s(M_Z) = 0.1180 +- 0.0009  (Eq. 9.25)
  flag2024.txt : FLAG 2024 (arXiv:2411.04268v3) Table 1 / Table 15:
       Nf=2+1+1: m_s=93.46(58) MeV, m_c/m_s=11.766(30), m_c(3 GeV)=0.989(10), m_b(m_b)=4.200(14) GeV
       Nf=2+1 : m_s=92.4(1.0), m_b(m_b)=4.171(20)
       m_b/m_c (3 GeV, Nf=4): FNAL/MILC/TUMQCD 18 = 4.578(5)(6)(0)(1) ; HPQCD 21 = 4.586(12)
Transport is the independent implementation k1_indep_transport.py (agrees with the attacker's qcdrun.py to 5 digits).
"""
import numpy as np
from k1_indep_transport import transport, alpha_low, run_x, mass_factor, mass_decouple_down

V_ATLAS = 0.103303816122/np.sqrt(6)
R_PRED = V_ATLAS**1.2

def R_common(ms2, mb, asMZ=0.1180, nf5_ratio=False):
    """R = m_s(m_b)/m_b(m_b) with the strange mass in the nf=4 theory (default) or nf=5 (nf5_ratio=True, a 0.1% effect)."""
    T, a2, ab = transport(asMZ=asMZ, mb=mb)
    R4 = ms2/T/mb
    if nf5_ratio:
        R4 = R4/mass_decouple_down(ab/np.pi, 0.0)
    return R4

rows = [
 ("A attacker (93.4, 4.180, as 0.1180)",          93.4e-3, 4.180, 0.1180),
 ("B PDG24 listing (93.5, 4.183)",                 93.5e-3, 4.183, 0.1180),
 ("C PDG24 lattice-only m_s (92.74, 4.183)",       92.74e-3, 4.183, 0.1180),
 ("D FLAG24 Nf=2+1+1 (93.46, 4.200)",              93.46e-3, 4.200, 0.1180),
 ("E FLAG24 Nf=2+1 (92.4, 4.171)",                 92.4e-3, 4.171, 0.1180),
 ("F FLAG24 2+1+1, as(MZ)=0.1184",                 93.46e-3, 4.200, 0.1184),
 ("G high-side stress: 93.5+0.8, 4.183-0.007, as 0.1171", 94.3e-3, 4.176, 0.1171),
 ("H low-side stress: 93.5-0.8, 4.183+0.007, as 0.1189", 92.7e-3, 4.190, 0.1189),
]
print(f"R_pred (atlas) = {R_PRED:.7f}")
print(f"{'input set':58s} {'R_common':>9s} {'1/R':>7s} {'miss(atlas)':>11s} {'p=lnV/lnR':>9s} {'c=V/R^(5/6)':>11s}")
for name, ms, mb, a in rows:
    R = R_common(ms, mb, a)
    print(f"{name:58s} {R:9.6f} {1/R:7.2f} {100*(R_PRED/R-1):+10.2f}% {np.log(V_ATLAS)/np.log(R):9.4f} {V_ATLAS/R**(5/6):11.4f}")

print("\nrunning-free lattice chain (FLAG 2024): R = 1/[(m_b/m_c)(m_c/m_s)], same scale (3 GeV, nf=4)")
for lab, bc, bc_err in (("FNAL/MILC/TUMQCD 18", 4.578, 0.008), ("HPQCD 21", 4.586, 0.012)):
    cs, cs_err = 11.766, 0.030
    inv = bc*cs; err = inv*np.hypot(bc_err/bc, cs_err/cs)
    R = 1/inv
    print(f"  {lab:22s} m_b/m_s = {inv:.2f} +- {err:.2f}  R = {R:.6f} (+-{100*err/inv:.2f}%)  miss(atlas) = {100*(R_PRED/R-1):+.1f}%  p = {np.log(V_ATLAS)/np.log(R):.4f}")

print("\nsame inputs (set B) against DATA V_cb instead of the atlas number:")
R = R_common(93.5e-3, 4.183)
for lab, V in (("exclusive B->D*lnu  ~0.0392", 0.0392), ("PDG-average-like  0.0410", 0.0410), ("inclusive         0.0422", 0.0422)):
    print(f"  V_cb={V:.4f} ({lab}):  R_needed=V^(6/5)={V**1.2:.6f}  miss {100*(V**1.2/R-1):+.1f}%   p={np.log(V)/np.log(R):.4f}   V needed for exact 5/6: {R**(5/6):.4f} ({100*(R**(5/6)/V-1):+.1f}%)")

# Monte Carlo of the R error with PDG-2024 errors (m_b symmetric 0.007) and with the attacker's inflated m_b error
rng = np.random.default_rng(7)
def mc(ms_c, ms_e, mb_c, mb_e, as_e, N=3000):
    Rs = []
    for _ in range(N):
        Rs.append(R_common(rng.normal(ms_c, ms_e), rng.normal(mb_c, mb_e), rng.normal(0.1180, as_e)))
    Rs = np.array(Rs); d = R_PRED/Rs-1
    return Rs.mean(), Rs.std()/Rs.mean(), d.mean(), d.std()
for lab, args in (("PDG24 listing errors (ms 0.8, mb 0.007, as 0.0009)", (93.5e-3, 0.8e-3, 4.183, 0.007, 0.0009)),
                  ("attacker-style errors (ms 0.8, mb 0.025)",         (93.4e-3, 0.8e-3, 4.180, 0.025, 0.0009)),
                  ("PDG24 lattice-only m_s (0.54)",                     (92.74e-3, 0.54e-3, 4.183, 0.007, 0.0009))):
    m, s, d, ds = mc(*args)
    print(f"MC {lab}: R={m:.6f} (+-{100*s:.2f}%)  miss={100*d:+.2f}% +- {100*ds:.2f}%  -> {d/ds:.1f} sigma")
