"""Exact-Schur on-shell O(k^4) shifts for scalar(P1), Maxwell(Whitney), Regge spin-2 on the Kuhn complex, b=0.
alpha_i with omega^2 = k^2 (1 + alpha_i k^2): alpha_i = eig(E^T Seff(p) E) / (c k^4) at null p=(k n, i k)."""
import numpy as np, contextlib, io
import fem, disp
from regge_project import build, HC
g0 = np.eye(4)
Qregge, _ = build(g0)            # returns (Qh, Qedge); Qh = M^T Q M; need edge-level for Schur
_, Qedge_r = build(g0)

def regge_map(k):
    k = np.asarray(k, complex); import regge_project as RP, frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4
    Mm = np.zeros((15, 10), complex)
    for ci, v in enumerate(R4.DIRS15):
        vv = np.array(v, float); ell = np.linalg.norm(vv); z = (k @ vv)/2
        ph = 1.0 if abs(z) < 1e-13 else (np.exp(2j*z)-1)/(2j*z)
        for hj, (a, b) in enumerate(HC):
            Hm = np.zeros((4, 4)); Hm[a, b] += 1
            if a != b: Hm[b, a] += 1
            Mm[ci, hj] = ph*(vv @ Hm @ vv)/(2*ell)
    return Mm

def schur(Q, Mp, Mm, C):
    # bilinear: x(-p)^T Q x(p), x = M a + C b ; minimise over b
    A = Mm.T @ Q @ Mp; Bc = Mm.T @ Q @ C; Cb = C.T @ Q @ Mp; D = C.T @ Q @ C
    return A - Bc @ np.linalg.solve(D, Cb)

def complement(M0):
    u, s, vt = np.linalg.svd(M0.real)
    return u[:, M0.shape[1]:]

def null_p(n, k): return np.array([k*n[0], k*n[1], k*n[2], 1j*k])

def pol_maxwell(p):
    # two vectors e with e.p = 0, independent of p (bilinear dot), not along p
    n = p[:3].real/np.linalg.norm(p[:3].real)
    a = np.cross(n, [0.3, 0.5, 0.7]); a /= np.linalg.norm(a); b = np.cross(n, a)
    return np.array([[*a, 0], [*b, 0]]).T     # spatial transverse: e.p=0
def pol_tt(p):
    e = pol_maxwell(p); a, b = e[:, 0], e[:, 1]
    plus = np.outer(a, a) - np.outer(b, b); cross = np.outer(a, b) + np.outer(b, a)
    vec = lambda h: np.array([h[x, y] for (x, y) in HC])
    # metric variables: off-diag var = h_xy; bilinear form uses vars so normalise by EH value later
    return np.array([vec(plus), vec(cross)]).T

C15_m = complement(fem.line_map(np.zeros(4), g0))
C15_r = complement(regge_map(np.zeros(4)))
def alpha(field, n, k):
    p = null_p(n, k)
    if field == 'scalar':
        return [disp.scalar_hol(p).real/k**4]
    if field == 'maxwell':
        S = schur(disp.maxwell_hol(p), fem.line_map(p, g0), fem.line_map(-p, g0), C15_m)
        E = pol_maxwell(p); c = 1.0
    else:
        S = schur(Qedge_r(p), regge_map(p), regge_map(-p), C15_r)
        E = pol_tt(p)
        # normalisation: c * p'^2 * N where EH(eps,eps) for TT = p^2 * (eps.eps) with eps.eps in matrix sense
        N = np.array([[np.sum(np.array([[1,0],[0,1]])[i,j]) for j in range(2)] for i in range(2)])
        c = -0.25 * 2.0      # plus/cross: tr(h h) = 2 ; Regge Q2 = -1/4 EH
    m = E.T @ S @ E
    return list(np.sort(np.linalg.eigvals(m).real/(c*k**4)))

if __name__ == '__main__':
    dirs = {'axis': (1,0,0), 'face': (1,1,0), 'face-': (1,-1,0), 'body': (1,1,1), 'body-': (1,1,-1), 'gen': (3,1,2), 'gen-': (3,-1,2)}
    for name, n in dirs.items():
        n = np.array(n, float); n /= np.linalg.norm(n)
        law = -(1 + (n**4).sum())/12
        row = []
        for f in ('scalar', 'maxwell', 'regge'):
            a1 = np.array(alpha(f, n, 0.02)); a2 = np.array(alpha(f, n, 0.01))
            row.append((4*a2 - a1)/3)
        print(f"{name:6s} law {law:+.6f} | scalar {row[0][0]:+.6f} | maxwell {row[1][0]:+.6f} {row[1][1]:+.6f} | regge TT {row[2][0]:+.6f} {row[2][1]:+.6f}")
