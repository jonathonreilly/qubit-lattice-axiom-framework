"""F2 (lane RF, campaign C4): one-loop speed split for lattice QED on Z^3 with CONTINUOUS time.

Matter: naive (= 4 x staggered) fermions on Z^3, continuous Euclidean time, non-compact U(1) links,
Kogut-Susskind-type covariant hopping  psi-bar gamma_i (U psi(x+i) - U^dag psi(x-i))/2, A_0 enters only via d_tau.
Photon: S_A = int dtau sum [ 1/2 (d_tau A_i - grad_i A_0)^2 + 1/2 F_ij^2 ], Feynman gauge D = delta/(k0^2 + khat^2 + lam^2).

Quantities (all per e^2; k0/q0 integrals done in closed form, 3D BZ by midpoint rule on L^3):
  fermion:  Gamma(p) = i g0 p0 (1+a0) + i g_j sin p_j (1+a1) + ...,  dc_f = a1 - a0
      a0 = - int d3k/(2pi)^3 (1 - sum_j cos^2(k_j/2)) / (2 w (E+w)^2)        [E^2 = sum sin^2 k + m^2, w^2 = khat^2 + lam^2]
      a1 = -(1/2)<A_x^2> - d/dp_x int d3k/(2pi)^3 sin(p_x-k_x)(2cos^2(p_x-k_x/2) - C)/(2 E_q w (E_q+w)),
           C = 1 + sum_j cos^2(p_j - k_j/2),  <A_x^2> = int d3k/(2pi)^3 1/(2w)
  photon (per naive fermion = 8 Dirac doublers; staggered = 1/4 of this = 2 tastes):
      a_E = (1/2) int cos^2 q_x (E^2 - s_x^2)/E^5                          (from Pi_xx(k0,0) = a_E k0^2)
      a_B = lim Pi_yy(0, k xhat)/khat_x^2,  Pi_yy^bub = -4 int cos^2 q_y (E E' + Y)/(2 E E'(E+E')),
            Y = s_x s_x' - s_y^2 + s_z^2 + m^2,  Pi^tad_yy = 2 int s_y^2/E
      dc_gamma = (a_B - a_E)/2
  Delta_QED = (dc_f - dc_gamma) / (1/16pi^2)   [i.e. in units of e^2/16pi^2]

Checks printed: Ward identity Pi_xx(0,0) = 0; continuum log coefficients (a_E: N/(6pi^2) ln(1/m) per Dirac doublers).
Usage: python f2_qed_speeds.py
"""
import numpy as np, sys, time

def grid(L):
    k = (np.arange(L) + 0.5) * 2 * np.pi / L - np.pi
    KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
    return KX, KY, KZ

def fermion_coeffs(L, m, lam, h=1e-4):
    KX, KY, KZ = grid(L)
    khat2 = 4 * (np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2)
    w = np.sqrt(khat2 + lam ** 2)
    E = np.sqrt(np.sin(KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2 + m ** 2)
    C0 = np.cos(KX / 2) ** 2 + np.cos(KY / 2) ** 2 + np.cos(KZ / 2) ** 2
    a0 = -np.mean((1 - C0) / (2 * w * (E + w) ** 2))
    A2 = np.mean(1 / (2 * w))
    def I(px):
        Eq = np.sqrt(np.sin(px - KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2 + m ** 2)
        C = 1 + np.cos(px - KX / 2) ** 2 + np.cos(KY / 2) ** 2 + np.cos(KZ / 2) ** 2
        F = np.sin(px - KX) * (2 * np.cos(px - KX / 2) ** 2 - C) / (2 * Eq * w * (Eq + w))
        return np.mean(F)
    dI = (I(h) - I(-h)) / (2 * h)
    a1_sun = -dI
    a1_tad = -0.5 * A2
    a1 = a1_tad + a1_sun
    return dict(a0=a0, a1=a1, a1_tad=a1_tad, a1_sun=a1_sun, A2=A2, dcf=a1 - a0)

def photon_coeffs(L, m, kxs=(0.02, 0.04)):
    QX, QY, QZ = grid(L)
    sx, sy, sz = np.sin(QX), np.sin(QY), np.sin(QZ)
    E2 = sx ** 2 + sy ** 2 + sz ** 2 + m ** 2
    E = np.sqrt(E2)
    aE = 0.5 * np.mean(np.cos(QX) ** 2 * (E2 - sx ** 2) / E ** 5)
    # Ward identity at k=0: bubble + tadpole for Pi_xx(0,0)
    wi = -2 * np.mean(np.cos(QX) ** 2 * (E2 - sx ** 2) / E ** 3) + 2 * np.mean(sx ** 2 / E)
    tad_yy = 2 * np.mean(sy ** 2 / E)
    vals = []
    for kx in kxs:
        sxp = np.sin(QX + kx)
        Ep = np.sqrt(sxp ** 2 + sy ** 2 + sz ** 2 + m ** 2)
        Y = sx * sxp - sy ** 2 + sz ** 2 + m ** 2
        bub = -4 * np.mean(np.cos(QY) ** 2 * (E * Ep + Y) / (2 * E * Ep * (E + Ep)))
        Pi = bub + tad_yy
        vals.append(Pi / (4 * np.sin(kx / 2) ** 2))
    # Richardson in kx^2 (kxs = h, 2h)
    aB = (4 * vals[0] - vals[1]) / 3
    return dict(aE=aE, aB=aB, wi=wi, aB_raw=vals, dcg=(aB - aE) / 2)

if __name__ == "__main__":
    t0 = time.time()
    u = 16 * np.pi ** 2
    print("== check: closed-form k0 integral  int u^2/((u^2+a^2)(u^2+b^2)^2) du = pi/(2b(a+b)^2)")
    from scipy.integrate import quad
    for a, b in [(0.3, 1.1), (2.0, 0.5)]:
        num = quad(lambda x: x * x / ((x * x + a * a) * (x * x + b * b) ** 2), -np.inf, np.inf)[0]
        print(f"   a={a} b={b}: numeric {num:.10f}  closed {np.pi/(2*b*(a+b)**2):.10f}")
    print("\n== photon (per NAIVE fermion = 8 Dirac doublers); units: coefficient per e^2, then x16pi^2")
    for L in (64, 128, 192):
        for m in (0.2, 0.1, 0.05):
            r = photon_coeffs(L, m)
            print(f"L={L:4d} m={m:5.3f}  WI Pi_xx(0,0)={r['wi']:+.2e}  aE={r['aE']:.6f}  aB={r['aB']:.6f}  "
                  f"(aB-aE)={r['aB']-r['aE']:+.6f}  dc_gamma*16pi^2 = {u*r['dcg']:+.4f}   aE log-check: aE*16pi^2/(8*(8/3)) - ln(1/m) = {u*r['aE']/(8*8/3) - np.log(1/m):+.4f}", flush=True)
    print("\n== fermion self-energy (Feynman gauge, photon mass lam, fermion mass m); dc_f*16pi^2")
    for L in (64, 128, 192):
        for (m, lam) in [(0.05, 0.1), (0.02, 0.05), (0.01, 0.025)]:
            r = fermion_coeffs(L, m, lam)
            print(f"L={L:4d} m={m:5.3f} lam={lam:5.3f}  a0*16pi^2={u*r['a0']:+.4f}  a1*16pi^2={u*r['a1']:+.4f} "
                  f"[tadpole {u*r['a1_tad']:+.4f}, sunset {u*r['a1_sun']:+.4f}]  <A^2>={r['A2']:.5f}  dc_f*16pi^2={u*r['dcf']:+.4f}", flush=True)
    print(f"\nelapsed {time.time()-t0:.1f}s")
