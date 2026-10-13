"""R19-9 (b): the corner cost on the photon TT rows, converged (semi-analytic), plus a grid validation at resolved r.

The exact kernel's spatial PAIR block is N_glued = N_VW + chiC (N_C - N_VW), chiC = phi(|k1|/r) phi(|k2|/r) (lib199).
In U_r the photon is continuum (sigma = k, c = 1) and N_C - N_VW = q^2 N' + O(q^4) with N' = -dN_VW/d(q^2) at q = 0
(stencils P(s_l), u(s_l) depend on s = q only). At q = 0 nothing changes (so d/d(omega^2) part unchanged). Hence, per vector,
   dXi_e(r) = -(1/(2 pi)^3) Int d^3k phi(|k|/r)^2 2 tr(P N_C P N'^T)/(2|k|) = -(r^4 I_phi/(2 pi)^3) Int dOmega F_e(khat),
   tr(P N_C P N'^T) = |k|^2 F_e(khat),  I_phi = Int_0^1 x^3 phi(x)^2 dx.
Exactly r^4 (proved from homogeneity). F_e is a polynomial of degree <= 8 in khat; Gauss-Legendre x trapezoid is exact.
Grid validation: R18-13's exact-shift Richardson (vwface.xi_geo) with the glued pair amplitude, at r = 0.4, 0.8."""
import sys, time, numpy as np
import lib199 as L
sys.path.insert(0, L.os.path.join(L.HERE, 'arch18_13'))
import vwface as V
from scipy.integrate import quad
t0 = time.time()

def Nmat(ME, MB, s1, s2):
    w1 = np.linalg.norm(s1); w2 = np.linalg.norm(s2); rw = np.sqrt(w1*w2)
    X1 = V.crossmat(s1); X2 = V.crossmat(s2)
    return 0.5*(rw*ME + X1.T @ MB @ X2/rw)

def dvertex(e, n, a, wd, wo):
    """-(d/dq^2) vertex(e, 1, 1, P(q n), ud(q n), uo(q n)) at q = 0, exact: the vertex is a cubic polynomial in
    (P - 1, u - 1), which are -(lam/2) q^2 n_l^2, -(w/2) q^2 n_l^2 + O(q^4); 4-point difference is exact for cubics."""
    lam = 0.25 + 2*a; one = np.ones(3)
    def f(eps):
        return L.vertex(e, one, one, one - eps*lam/2*n**2, one - eps*wd/2*n**2, one - eps*wo/2*n**2)
    h = 0.1
    out = []
    for c in range(2):
        d1 = f(h)[c] - f(-h)[c]; d2 = f(2*h)[c] - f(-2*h)[c]
        out.append(-(8*d1 - d2)/(12*h))
    return out

def angular(e, n, a, wd, wo, nt=40, nph=80):
    one = np.ones(3)
    MEc, MBc = L.vertex(e, one, one, one, one, one)
    MEp, MBp = dvertex(e, n, a, wd, wo)
    x, wx = np.polynomial.legendre.leggauss(nt); ph = np.arange(nph)*2*np.pi/nph
    tot = 0.0
    for ct, wt in zip(x, wx):
        st = np.sqrt(1 - ct*ct)
        for p in ph:
            kh = np.array([st*np.cos(p), st*np.sin(p), ct])
            Nc = Nmat(MEc, MBc, kh, -kh); Np = Nmat(MEp, MBp, kh, -kh)
            P = np.eye(3) - np.outer(kh, kh)
            tot += wt*(2*np.pi/nph)*np.trace(P @ Nc @ P @ Np.T)
    return tot

Iphi = quad(lambda x: x**3*L.phi(x)**2, 0, 1, epsabs=1e-15, epsrel=1e-13, limit=200)[0]
print(f'I_phi = {Iphi:.15f}  (phi = 1 - sstep(2x - 1); sharp-ball value would be 1/4)')
ROWS = ('T2g', 'Eg', 'xz', 'face1', 'face2', 'body')
def corner_coeffs(a, wd, wo):
    C = {}
    for row in ROWS:
        n = np.array(V.DIRS[row], float); n /= np.linalg.norm(n)
        C[row] = -Iphi*angular(V.POL[row], n, a, wd, wo)/(2*np.pi)**3
    return C
if __name__ == '__main__':
    a, wd, wo = L.A_R, L.WD_R, L.WO_R
    C = corner_coeffs(a, wd, wo)
    print(f'per-vector corner shift dXi_e = C_e r^4 at root (a, wd, wo) = ({a}, {wd}, {wo}):')
    for row in ROWS: print(f'   C_{row:5s} = {C[row]:+.12e}')
    print(f'   O_h relation on the shift: body - (8 face1 + 4 face2 - 3 Eg)/9 = {C["body"] - (8*C["face1"] + 4*C["face2"] - 3*C["Eg"])/9:+.2e} ; C4 xz - T2g = {C["xz"] - C["T2g"]:+.2e}')
    # linearity in (lam, wd, wo): decompose
    C0 = corner_coeffs(-0.125, 0.0, 0.0)
    print('   at the continuum point (lam = 0, w = 0) all C_e =', ' '.join(f'{C0[r_]:+.1e}' for r_ in ROWS))
    for (lab, args) in (('d/da', (a + 1e-3, wd, wo)), ('d/dwd', (a, wd + 1e-3, wo)), ('d/dwo', (a, wd, wo + 1e-3))):
        C1 = corner_coeffs(*args)
        print(f'   {lab}: ' + ' '.join(f'{r_} {(C1[r_] - C[r_])/1e-3:+.6e}' for r_ in ROWS))
    for r in (0.05, 0.1, 0.2):
        print(f'   r = {r}: per vector ' + ' '.join(f'{r_} {C[r_]*r**4:+.3e}' for r_ in ROWS) + f' | x12 vectors: T2g {12*C["T2g"]*r**4:+.3e} Eg {12*C["Eg"]*r**4:+.3e} face1 {12*C["face1"]*r**4:+.3e} face2 {12*C["face2"]*r**4:+.3e}')
    np.save('corner_coeffs.npy', np.array([C[r_] for r_ in ROWS]))
    print(f'time {time.time()-t0:.1f} s', flush=True)
    # ---- grid validation (exact-shift Richardson, R18-13 machinery, glued amplitude) ----
    if len(sys.argv) > 1:
        N = int(sys.argv[1]); rs = [float(v) for v in sys.argv[2].split(',')]
        law = V.photonGw(L.BG, np.pi - L.BG)
        def pair_W_glue(shift, e, r):
            k = V.kgrid(N); s = law.sig(k); c = law.c(k)
            j = np.arange(N); j2 = [(shift[d] - j - 1) % N for d in range(3)]
            Y, Z = np.meshgrid(j, j, indexing='ij')
            Wv = np.empty((N, N, N)); Wg = np.empty((N, N, N)); Ea = np.empty((N, N, N))
            one = np.ones((N, N, 3))
            for ix in range(N):
                X_ = np.full_like(Y, ix); I1 = [X_, Y, Z]; I2 = [j2[0][X_], j2[1][Y], j2[2][Z]]
                s1 = np.stack([s[I] for I in I1], -1); s2 = np.stack([s[I] for I in I2], -1)
                c1 = np.stack([c[I] for I in I1], -1); c2 = np.stack([c[I] for I in I2], -1)
                k1 = np.stack([k[I] for I in I1], -1); k2 = np.stack([k[I] for I in I2], -1)
                ssum = k1 + k2
                w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2)
                X1 = V.crossmat(s1); X2 = V.crossmat(s2)
                P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
                P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
                ME, MB = V.vertex_geo(e, c1, c2, ssum, a, wd, wo)
                Nv = 0.5*(rw[..., None, None]*ME + np.einsum('...ji,...jk,...kl->...il', X1, MB, X2)/rw[..., None, None])
                MEc, MBc = V.vertex_geo(e, one, one, 0*ssum, 0.0, 0.0, 0.0)     # P(0) = 1, u(0) = 1: continuum kernel
                Nc = 0.5*(rw[..., None, None]*MEc + np.einsum('...ji,...jk,...kl->...il', X1, MBc, X2)/rw[..., None, None])
                chi = (L.phi(np.linalg.norm(k1, axis=-1)/r)*L.phi(np.linalg.norm(k2, axis=-1)/r))[..., None, None]
                Ng = Nv + chi*(Nc - Nv)
                Wv[ix] = np.einsum('...ij,...jk,...kl,...il->...', P1, Nv, P2, Nv)
                Wg[ix] = np.einsum('...ij,...jk,...kl,...il->...', P1, Ng, P2, Ng)
                Ea[ix] = w1 + w2
            return Wv, Wg, Ea
        for r in rs:
            line = f'GRID N={N} r={r}:'
            for row in ('T2g', 'Eg', 'face1', 'face2'):
                e = V.POL[row]; d = np.array(V.DIRS[row]); shifts = (1, 2)
                W0v, W0g, E0 = pair_W_glue((0, 0, 0), e, r)
                Xi = []
                for W0 in (W0v, W0g):
                    pass
                Dd = {n_: pair_W_glue(tuple(n_*d), e, r) for n_ in shifts}
                q1 = 2*np.pi*shifts[0]*np.sqrt(float(d @ d))/N; rr = shifts[1]/shifts[0]
                vals = []
                for t in (0, 1):
                    W0 = (W0v, W0g)[t]; beta = -np.mean(W0/E0**3); Pi0 = -np.mean(W0/E0)
                    Dn = {n_: -np.mean(Dd[n_][t]/Dd[n_][2]) - Pi0 for n_ in shifts}
                    alpha = (rr**4*Dn[shifts[0]] - Dn[shifts[1]])/((rr**4 - rr**2)*q1**2)
                    vals.append(alpha + beta)
                line += f' | {row}: grid dXi {vals[1]-vals[0]:+.4e} vs C r^4 {C[row]*r**4:+.4e} (Xi_VW {vals[0]:+.6e})'
            print(line, flush=True)
        print(f'time {time.time()-t0:.0f} s')
