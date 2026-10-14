"""TW-2 cross-checks with the DIRECT 8x8 staggered one-loop self-energy (nf1_sigma8.py's evaluator, copied; full-BZ midpoint grid N^3).
 (i)  folding consistency P_m H(k) P_m = H(k + pi m) of the taste-split law H8 = sum s Gamma_j + m Gamma_eps + sigma cos k1 cos k2 M_110;
 (ii) Sigma(P = 0) of the split law at t = 0 and under SF strain (Eg, tet), decomposed in the 64-element spin x taste basis of the dictionary:
      only beta x 1 and beta x (n3.tau) may appear (claim: P, T, C of each 4x4 block); compared with the two-block reduction (f3_lib.dm_gen
      on the SAME grid);
 (iii) the body-diagonal splitting  sigma (O_12 + O_23 + O_31)/sqrt 3  (taste vector along (n1 + n2 + n3)/sqrt 3; not block-reducible):
      its taste-split mass coefficient and its linear response to the trigonal T2g-type strain is NOT computed (F1's photon is singular for
      T2g); here only E_g strains (Eg, tet), where C3[111] forbids a linear term (check);
 (iv) the hw = 1 alternative (main's generation lane, Wilson/K0 splitting): H = h_stag + lam M_W, M_W(k)[n,n] = sum_mu (1 - cos(k_mu + pi n_mu));
      Sigma(P = 0) restricted to the hw = 1 corner span {100, 010, 001}: its one-loop shift and its linear E_g strain splitting (FB1 flow).
argv: N"""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
from f1_lib import Phot, flowG1, CPH, rk4
from f3_lib import dm_gen
from sublum import SymS
t00 = time.time()
N = int(sys.argv[1]) if len(sys.argv) > 1 else 24
BF = 0.909103708
A = SymS(BF); G = Phot(CPH)
G4 = np.load(os.path.join(HERE, 'nf1_gammas.npy')); Ud = np.load(os.path.join(HERE, 'nf1_dict.npy'))
Gam, Geps = G4[:3], G4[3]
MO = np.load(os.path.join(HERE, 'tw2_mass_ops.npy'))          # M_110 (taste n3), M_011 (n1), M_101 (n2)
M110, M011, M101 = MO
bits = [((i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)]
idx = lambda n: n[0] + 2*n[1] + 4*n[2]
def P(m):
    Pm = np.zeros((8, 8))
    for n in bits:
        Pm[idx(n), idx(tuple((a + b) % 2 for a, b in zip(n, m)))] = 1.0
    return Pm
Y = [np.diag([(-1.0)**n[mu] for n in bits]) for mu in range(3)]
STRAINS = {'Eg': (1.0, -1.0, 0.0), 'tet': tuple(v/np.sqrt(3) for v in (-1.0, -1.0, 2.0))}


def phi1(k, th):
    if th == 0.0:
        return np.array(k, float)
    return rk4(lambda y: (0.5*th*A.s(y[0])*A.ds(y[0]),), (np.array(k, float),), 6)[0]


def make_H(t, h, m=0.0, sig=0.0, body=False, lam=0.0):
    """8x8 H at unfolded momentum (FB1 taste-blind separable flow applied to every symbol: H_t(k) = H(Phi_t k))."""
    def Hf(kx, ky, kz):
        kx, ky, kz = np.broadcast_arrays(np.asarray(kx, float), np.asarray(ky, float), np.asarray(kz, float))
        f = [phi1(kk, t*hj) for kk, hj in zip((kx, ky, kz), h)]
        H = sum(np.multiply.outer(A.s(f[j]), Gam[j]) for j in range(3)) + m*np.multiply.outer(np.ones_like(kx), Geps)
        c = [np.cos(fj) for fj in f]
        if sig != 0.0:
            if body:
                H = H + (sig/np.sqrt(3))*(np.multiply.outer(c[0]*c[1], M110) + np.multiply.outer(c[1]*c[2], M011)
                                          + np.multiply.outer(c[0]*c[2], M101))
            else:
                H = H + sig*np.multiply.outer(c[0]*c[1], M110)
        if lam != 0.0:
            H = H + lam*sum(np.multiply.outer(np.ones_like(kx), np.eye(8)) - np.multiply.outer(c[mu], Y[mu]) for mu in range(3))
        return H
    return Hf


def sigma8(Hf, dx, dy, dz, x):
    """nf1_sigma8.py:65-93 (copied): Sigma(P = 0), Feynman gauge, Psym, A_0 exchange, critical m = 0; Hf(kx, ky, kz) -> (..., 8, 8)."""
    n = len(x); w = 1.0/n
    z = 0*x
    H0 = Hf(0.0, 0.0, 0.0)
    Hx, Hy, Hz = Hf(x, z, z), Hf(z, x, z), Hf(z, z, x)
    Hxm, Hym, Hzm = Hf(-x, z, z), Hf(z, -x, z), Hf(z, z, -x)
    T = [(Hx + Hxm - 2*H0)/(2*dx[:, None, None]**2), (Hy + Hym - 2*H0)/(2*dy[:, None, None]**2), (Hz + Hzm - 2*H0)/(2*dz[:, None, None]**2)]
    Hxy = Hf(x[:, None], x[None, :], 0*x[:, None])
    tot = np.zeros((8, 8), complex)
    for iz in range(n):
        zz = x[iz]
        Hq = Hf(x[:, None], x[None, :], zz + 0*x[:, None])
        Hxz = Hf(x, z, zz + z)[:, None]; Hyz = Hf(z, x, zz + z)[None, :]
        Hz1 = Hf(0.0, 0.0, zz)
        Cx = Hx[:, None]; Cy = Hy[None, :]
        dX = dx[:, None, None, None]; dY = dy[None, :, None, None]; dZ = dz[iz]
        Vx = (2*(Cx - H0) + (Hxy - Cy) + (Hxz - Hz1) + 2*(Hq - Hyz))/6/dX
        Vy = (2*(Cy - H0) + (Hxy - Cx) + (Hyz - Hz1) + 2*(Hq - Hxz))/6/dY
        Vz = (2*(Hz1 - H0) + (Hxz - Cx) + (Hyz - Cy) + 2*(Hq - Hxy))/6/dZ
        Om = np.sqrt(dx[:, None]**2 + dy[None, :]**2 + dz[iz]**2)
        E, U = np.linalg.eigh(Hq)
        X = U @ ((np.sign(E)/(2*Om[..., None]*(np.abs(E) + Om[..., None])))[..., None]*U.conj().swapaxes(-1, -2))
        val = X - sum(V @ X @ V for V in (Vx, Vy, Vz))
        tad = (T[0][:, None] + T[1][None, :] + T[2][iz])/(2*Om[..., None, None])
        tot += (val + tad).sum(axis=(0, 1))*w**3
    return tot


x = -np.pi + (np.arange(N) + 0.5)*2*np.pi/N; wv = np.full(N, 1.0/N)
def phot(t, h):
    return tuple(G.d(flowG1(G, np.abs(x), hj, t, 6)) if (t != 0 and hj != 0) else G.d(x) for hj in h)


# spin x taste basis in the dictionary frame
import itertools
sys.path.insert(0, HERE)
from f3_dirac import alpha, beta
gens = [alpha[0], alpha[1], alpha[2], beta]; gn = ['a1', 'a2', 'a3', 'b']
CL = []
for r in range(5):
    for sub in itertools.combinations(range(4), r):
        Xc = np.eye(4, dtype=complex)
        for s_ in sub:
            Xc = Xc @ gens[s_]
        CL.append(('.'.join(gn[s_] for s_ in sub) or '1', Xc))
tau = [np.eye(2), np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1.]).astype(complex)]
n3 = np.array([np.trace(np.kron(beta, tau[a]).conj().T @ (Ud @ M110 @ Ud.conj().T)).real/8 for a in (1, 2, 3)])
n3t = sum(n3[a]*tau[a + 1] for a in range(3))
def decomp(S, top=4):
    X = Ud @ S @ Ud.conj().T
    co = []
    for cn, C in CL:
        for tn, T in (('1', tau[0]), ('n3.t', n3t), ('t1', tau[1]), ('t2', tau[2]), ('t3', tau[3])):
            co.append(('%s(x)%s' % (cn, tn), np.trace(np.kron(C, T).conj().T @ X)/8))
    mb1 = [c for nm, c in co if nm == 'b(x)1'][0].real; mbn = [c for nm, c in co if nm == 'b(x)n3.t'][0].real
    rest = X - mb1*np.kron(beta, tau[0]) - mbn*np.kron(beta, n3t)
    return mb1, mbn, np.abs(rest).max()


print('TW-2 direct 8x8 checks, full-BZ midpoint N = %d (%d points); per e^2' % (N, N**3), flush=True)
rng = np.random.default_rng(1)
Hs = make_H(0.13, STRAINS['tet'], m=0.02, sig=0.03)
err = 0
for _ in range(5):
    k = rng.uniform(-np.pi, np.pi, 3)
    for m_ in bits:
        err = max(err, np.abs(P(m_) @ Hs(*k) @ P(m_) - Hs(*(k + np.pi*np.array(m_)))).max())
print('(i) folding P_m H(k) P_m = H(k + pi m), split law with tet strain t = 0.13: max err %.1e' % err)
print('(ii) split law (face-diagonal sigma O_12), m = 0, sigma = 0.01:  8x8 beta x 1 / beta x n3.tau coefficients vs two-block dm_gen')
for sn in ('Eg', 'tet'):
    for t in (0.0, 0.1, -0.1):
        if sn == 'Eg' and t < 0:
            continue
        h = STRAINS[sn]
        S = sigma8(make_H(t, h, 0.0, 0.01), *phot(t, h), x)
        mb1, mbn, rest = decomp(S)
        # two-block reduction on the same grid (taste-blind flow)
        def cMb(tau_):
            def cM(kx, ky, kz):
                kx, ky, kz = np.broadcast_arrays(np.asarray(kx, float), np.asarray(ky, float), np.asarray(kz, float))
                f = [phi1(kk, t*hj) for kk, hj in zip((kx, ky, kz), h)]
                return A.s(f[0]), A.s(f[1]), A.s(f[2]), tau_*0.01*np.cos(f[0])*np.cos(f[1])
            return cM
        dp = dm_gen(cMb(+1), *phot(t, h), x, wv); dmn = dm_gen(cMb(-1), *phot(t, h), x, wv)
        print('   %-3s t=%+.2f: beta x 1 %+.3e ; beta x n3.tau %+.12e ; two-block (S+ - S-)/2 %+.12e ; (S+ + S-)/2 %+.1e ; max other %.1e'
              % (sn, t, mb1, mbn, (dp - dmn)/2, (dp + dmn)/2, rest), flush=True)
print('(iii) body-diagonal splitting sigma (O_12 + O_23 + O_31)/sqrt3, m = 0, sigma = 0.01: taste-split coefficient and E_g linear terms')
for sn in ('Eg', 'tet'):
    vals = {}
    for t in (0.0, 0.1, -0.1):
        h = STRAINS[sn]
        S = sigma8(make_H(t, h, 0.0, 0.01, body=True), *phot(t, h), x)
        X = Ud @ S @ Ud.conj().T
        nb = sum(np.trace(np.kron(beta, tau[a + 1]).conj().T @ X).real/8*tau[a + 1] for a in range(3))
        # taste vector of the body splitting
        vb = np.array([np.trace(np.kron(beta, tau[a + 1]).conj().T @ X).real/8 for a in range(3)])
        b1 = np.trace(np.kron(beta, tau[0]).conj().T @ X).real/8
        rest = np.abs(X - b1*np.kron(beta, tau[0]) - np.kron(beta, nb)).max()
        vals[t] = vb
        print('   %-3s t=%+.2f: |beta x vec.tau| %+.10e (vec %s) ; beta x 1 %+.1e ; max other %.1e' % (sn, t, np.linalg.norm(vb), np.round(vb/np.linalg.norm(vb), 6), b1, rest), flush=True)
    print('   %-3s odd part |v(+0.1) - v(-0.1)| = %.2e' % (sn, np.linalg.norm(vals[0.1] - vals[-0.1])))
print('(iv) hw = 1 alternative: H = h_stag + lam M_W (FB1 flow), photon as above; corner-level tree energies 2 lam hw')
hw1 = [idx((1, 0, 0)), idx((0, 1, 0)), idx((0, 0, 1))]
DW = np.diag([2.0*sum(n) for n in bits])
Xw = Ud @ DW @ Ud.conj().T
terms = []
for cn, C in CL:
    for tn, T in (('1', tau[0]), ('t1', tau[1]), ('t2', tau[2]), ('t3', tau[3])):
        cf = np.trace(np.kron(C, T).conj().T @ Xw)/8
        if abs(cf) > 1e-9:
            terms.append('%s(x)%s %+.3f%+.3fi' % (cn, tn, cf.real, cf.imag))
print('   M_W(k=0) = diag(2 hw) in the spin x taste dictionary: %s' % '; '.join(terms))
print('   [M_W(0), beta x 1] = %.1e ; [M_W(0), alpha_j x 1] = %s' % (np.abs(DW @ Geps - Geps @ DW).max(), ['%.1e' % np.abs(DW @ Gam[j] - Gam[j] @ DW).max() for j in range(3)]))
for lam in (0.1,):
    for t in (0.0, 0.05, -0.05):
        h = STRAINS['Eg']
        Hf = make_H(t, h, lam=lam)
        H0 = Hf(0.0, 0.0, 0.0)
        S = sigma8(Hf, *phot(t, h), x)
        B = S[np.ix_(hw1, hw1)]
        print('   lam=%.2f Eg t=%+.2f: tree diag(H(0)) on hw=1 %s ; one-loop hw=1 block diag %s ; offdiag max %.1e ; eig %s ; Sigma(000) %+.4e ; ||Sigma - its hw-diagonal|| %.1e'
              % (lam, t, np.round(np.real(np.diag(H0))[hw1], 6), np.round(np.real(np.diag(B)), 7), np.abs(B - np.diag(np.diag(B))).max(),
                 np.round(np.linalg.eigvalsh(B), 7), S[0, 0].real, np.abs(S - np.diag(np.diag(S))).max()), flush=True)
print('time %.0f s' % (time.time() - t00))
