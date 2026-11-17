"""GUIDE for row 1085: the two ends of the kinetic time on the box with one transverse plaquette, n = 2, beta_T = 0.
t = infinity (beta_L = 0): D = P_0, gap from P_0 M P_0 (tplaq.py).
t = 0 (beta_L = infinity, the face): at beta_T = 0 the face operator is a tensor product over the four sheets, restricted to
G-invariants. A sheet (two SU(2) elements, n = 2) splits by (left spin p, right spin q); G-invariance at a site forces
q of one sheet = p of the next. Face eigenvalues = products mu_(p1 p2) mu_(p2 p3) mu_(p3 p4) mu_(p4 p1).
mu_(pp): block j3 = p of the basis |j1 j2 j3> of row 1081 (K = a_j1 a_j2, X12 with squared 6j).
mu_(01): basis |j>, j1 = j2 = j >= 1/2, tridiagonal, entries (1/2) sqrt(d_j d_j') |{j j 1; j' j' 1/2}| (signs do not change the spectrum).
Same normalisation as tplaq.py: each side plaquette weight divided by c_0 = 2 I_1(beta)/beta.
Usage: python3 endpoint.py JMAX2 A D"""
import sys, math, numpy as np
from scipy.special import ive
import tplaq
from tplaq import sixj, ok

def sector_pp(p, J2, bM):   # doubled p
    B = [(a, b) for a in range(J2+1) for b in range(J2+1) if ok(a, b, p)]
    idx = {s: i for i, s in enumerate(B)}
    X = np.zeros((len(B), len(B)))
    for (a, b), i in idx.items():
        for da in (-1, 1):
            for db in (-1, 1):
                t = (a+da, b+db)
                if t in idx:
                    X[idx[t], i] = 0.5 * math.sqrt((a+1)*(a+da+1)*(b+1)*(b+db+1)) * sixj(a, b, p, b+db, a+da, 1)**2
    return B, X

def sector_01(J2, bM):
    B = [(a, a) for a in range(1, J2+1)]
    X = np.zeros((len(B), len(B)))
    for i, (a, _) in enumerate(B):
        if i+1 < len(B):
            ap = a + 1
            v = 0.5 * math.sqrt((a+1)*(ap+1)) * abs(sixj(a, a, 2, ap, ap, 1))
            X[i, i+1] = X[i+1, i] = v
    return B, X

def tops(B, X, bM, k=2):
    w, U = np.linalg.eigh(X)
    E2 = (U * np.exp(bM * (w - 1.0))) @ U.T / (2.0 * ive(1, bM) / bM)   # exp(bM x)/c_0, with ive scaling
    u = tplaq.uvec(bM, 400)
    kk = np.array([math.sqrt(u[a] * u[b]) for (a, b) in B])
    ev = np.linalg.eigvalsh(kk[:, None] * E2 * kk[None, :])
    return ev[::-1][:k]

if __name__ == '__main__':
    J2, A, D = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    S = tplaq.setup(A, D)
    sec = {('pp', p): sector_pp(p, J2, None) for p in (0, 1, 2)}
    sec['01'] = sector_01(J2, None)
    print(f"# 2Jmax {J2} (sheet sectors), A {A} D {D} (ker N block)")
    print("bM  mu00 gap_singlet  m_face[(0,1),(1,0)] m_face[all 1/2] m_face[all 1]  m(t=0)=min   m_odd(t=0)  m(t=inf)  m(inf)-m(0)   lam0(inf)<=mu00^4  lamodd(inf)<=mu_hh^4")
    for bM in (0.5, 1.0, 2.0, 2.4, 3.0, 4.0, 6.0, 8.0, 8.5, 9.0, 10.0, 11.0, 12.0, 14.0, 16.0, 20.0, 24.0):
        m00 = tops(*sec[('pp', 0)], bM); mhh = tops(*sec[('pp', 1)], bM); m11 = tops(*sec[('pp', 2)], bM); m01 = tops(*sec['01'], bM)
        g_s = math.log(m00[0] / m00[1]); g_01 = 2 * math.log(m00[0] / m01[0]); g_h = 4 * math.log(m00[0] / mhh[0]); g_1 = 4 * math.log(m00[0] / m11[0])
        m0 = min(g_s, g_01, g_h, g_1)
        o = tplaq.run(S, 2, bM, 0.0)
        minf = math.log(o['lam'][0] / o['lam'][1])
        print(f"{bM:5.1f} {m00[0]:.8f} {g_s:.6f}  {g_01:.6f} {g_h:.6f} {g_1:.6f}  {m0:.6f}  {g_h:.6f}  {minf:.6f}  {minf-m0:+.6f}   {o['lam'][0]:.8f}<={m00[0]**4:.8f}  {o['lam'][1]:.8f}<={mhh[0]**4:.8f}", flush=True)
