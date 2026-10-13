"""R19-13: Wilson-Dirac (r = 1) plane insertion with the best radius-R one-particle unitary on the slab.
Per transverse momentum q = (qy, qz) the 3D problem is a 4-component chain along x (same conventions as R19-10's
r1910_insert_product.py: h0(q) = beta(m + r(2 - cos qy - cos qz) + r) + alpha_y sin qy + alpha_z sin qz,
T = alpha_x/(2i) - (r/2) beta, h(k) = h0 + T e^{ik} + T^dag e^{-ik}).
Old GS = filled negative sea (G = P_-), new site enters with 2 particles in the negative eigenvectors of h0(q)
(any 2-particle start is equivalent once U acts on S_new).  dE = E_mid_new(U) - E_mid_old - e0(q),
e0(q) = int dk/2pi sum of negative eigenvalues.  U ranges over U(4n), n = 2R+1 (number conserving Gaussian
unitaries on the slab; the U(1)-invariant convex relaxation is attained by such states, see report).
Usage: python r1913_dirac.py m R1 R2 ...  -> r1913_dirac_m{m}_R{R}.out
"""
import sys, time, numpy as np
from scipy.linalg import expm, expm_frechet
from scipy.optimize import minimize

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2)); I2 = np.eye(2)
al = [np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]
be = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
r = 1.0
T = al[0] / (2j) - 0.5 * r * be
NK = 2 ** 15


def corr(h0, nmax):
    k = 2 * np.pi * (np.arange(NK) + 0.5) / NK
    hk = h0[None] + T[None] * np.exp(1j * k)[:, None, None] + T.conj().T[None] * np.exp(-1j * k)[:, None, None]
    w, V = np.linalg.eigh(hk)
    P = np.einsum('kai,kbi,ki->kab', V, V.conj(), (w < 0).astype(float))
    e0 = (w * (w < 0)).sum() / NK
    G = [np.einsum('k,kab->ab', np.exp(1j * k * n), P) / NK for n in range(nmax + 1)]
    return G, e0     # G[n] = <c_b^dag(x) c_a(x+n)> block for separation n  (G_{x+n, x})


def window(h0, R):
    n = 2 * R + 1; d = 4 * n
    G, e0 = corr(h0, 2 * R + 2)
    def Gab(a, b):   # <c_b^dag c_a>, a,b old positions
        return G[a - b] if a >= b else G[b - a].conj().T
    oldpos = list(range(1, R + 1)) + [None] + list(range(R + 1, 2 * R + 1))
    w, V = np.linalg.eigh(h0); Pn = V[:, w < 0] @ V[:, w < 0].conj().T
    G0 = np.zeros((d, d), complex)
    for i, pi_ in enumerate(oldpos):
        for j, pj in enumerate(oldpos):
            if pi_ is None and pj is None:
                G0[4*i:4*i+4, 4*j:4*j+4] = Pn
            elif pi_ is not None and pj is not None:
                G0[4*i:4*i+4, 4*j:4*j+4] = Gab(pi_, pj)
    A = np.zeros((d, d), complex)
    for i in range(n):
        A[4*i:4*i+4, 4*i:4*i+4] = h0
        if i + 1 < n:
            A[4*i:4*i+4, 4*(i+1):4*(i+1)+4] = T; A[4*(i+1):4*(i+1)+4, 4*i:4*i+4] = T.conj().T
    # cross terms: bond (bL, s_first): H_{bL,s1} = T ; bond (s_last, bR): H_{slast,bR} = T
    GSbL = np.zeros((d, 4), complex); GSbR = np.zeros((d, 4), complex)
    for i, pi_ in enumerate(oldpos):
        if pi_ is None:
            continue
        GSbL[4*i:4*i+4] = Gab(pi_, 0); GSbR[4*i:4*i+4] = Gab(pi_, 2 * R + 1)
    E1 = np.zeros((4, d)); E1[:, 0:4] = np.eye(4)
    En = np.zeros((4, d)); En[:, d-4:d] = np.eye(4)
    # E_cross = tr(T G_{s1,bL}) + c.c. + tr(T G_{bR,slast}) + c.c. ; G_{S,b} -> U G0_{S,b}
    C = GSbL @ T @ E1 + GSbR @ T.conj().T @ En      # E_cross = 2 Re tr(C U)
    # old mid energy
    if R == 0:
        Emid_old = 2 * np.real(np.trace(T @ Gab(1, 0)))
    else:
        m_ = 2 * R
        Emid_old = m_ * np.real(np.trace(h0 @ G[0])) + (m_ + 1) * 2 * np.real(np.trace(T @ Gab(1, 0)))
    return dict(d=d, G0=G0, A=A, C=C, Emid_old=Emid_old, e0=e0)


def energy(W, U):
    rho = U @ W['G0'] @ U.conj().T
    return np.real(np.trace(W['A'] @ rho)) + 2 * np.real(np.trace(W['C'] @ U))


def opt(W, U_init=None, maxouter=60):
    d = W['d']; A = W['A']; C = W['C']
    U_ref = np.eye(d, dtype=complex) if U_init is None else U_init.copy()
    best = None
    for outer in range(maxouter):
        rho0 = U_ref @ W['G0'] @ U_ref.conj().T; Cp = U_ref @ C
        def f(x):
            Z = (x[:d*d] + 1j * x[d*d:]).reshape(d, d)
            K = (Z + Z.conj().T) / 2
            X = 1j * K
            V = expm(X)
            E = np.real(np.trace(A @ V @ rho0 @ V.conj().T)) + 2 * np.real(np.trace(Cp @ V))
            Gv = 2 * (A @ V @ rho0 + Cp.conj().T)
            M = expm_frechet(X.conj().T, Gv, compute_expm=False)
            Y = 1j * M.conj().T
            Gz = (Y + Y.conj().T) / 2
            return E, np.concatenate([Gz.real.ravel(), Gz.imag.ravel()])
        res = minimize(f, np.zeros(2 * d * d), jac=True, method='L-BFGS-B',
                       options=dict(maxiter=400, ftol=1e-16, gtol=1e-11, maxcor=30))
        x = res.x; Z = (x[:d*d] + 1j * x[d*d:]).reshape(d, d)
        U_ref = expm(1j * (Z + Z.conj().T) / 2) @ U_ref
        E = res.fun
        if best is not None and abs(best - E) < 1e-13 * max(1, abs(E)) and np.abs(res.jac).max() < 1e-8:
            best = E; break
        best = E
    return best - W['Emid_old'] - W['e0'], U_ref


def gradcheck():
    h0 = be * (0.3 + 1.0) + al[1] * np.sin(0.4) + al[2] * np.sin(0.2)
    W = window(h0, 1); d = W['d']
    rng = np.random.default_rng(1)
    Z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)); U = expm(1j * (Z + Z.conj().T) / 2 * 0.1)
    dE, _ = opt(W, U, maxouter=1)
    return dE


if __name__ == '__main__':
    m = float(sys.argv[1]); Rs = list(map(int, sys.argv[2:]))
    # graded Gauss-Legendre grid on [0, pi]^2 (q -> -q symmetric integrand; qy <-> qz symmetric)
    import os
    NG = int(os.environ.get('NG', '8')); tag = '' if NG == 8 else '_ng%d' % NG
    tg, wg = np.polynomial.legendre.leggauss(NG)
    t = (tg + 1) / 2; wt = wg / 2
    p = 2.0
    q = np.pi * t ** p; wq = np.pi * p * t ** (p - 1) * wt / np.pi    # weights for (1/pi) int_0^pi dq
    for R in Rs:
        t0 = time.time()
        with open('r1913_dirac_m%g_R%d%s.out' % (m, R, tag), 'w') as fo:
            fo.write('# Wilson-Dirac m=%g R=%d ; columns: qy qz weight dE_upper(q) seconds ; final line = BZ average\n' % (m, R))
            tot = 0.0; Uprev = None
            for i in range(len(q)):
                for j in range(i + 1):
                    h0 = be * (m + r * (2 - np.cos(q[i]) - np.cos(q[j])) + r) + al[1] * np.sin(q[i]) + al[2] * np.sin(q[j])
                    W = window(h0, R); ts = time.time()
                    dE, U = opt(W, None)
                    wgt = wq[i] * wq[j] * (1 if i == j else 2)
                    tot += wgt * dE
                    fo.write('%.6f %.6f %.6e %.10e %.1f\n' % (q[i], q[j], wgt, dE, time.time() - ts)); fo.flush()
            fo.write('# BZ average dE(R=%d) = %.10e   (sum of weights check below)\n' % (R, tot))
            fo.write('# weight sum = %.12f\n' % (np.sum(np.outer(wq, wq))))
        print('m=%g R=%d done %.0f s, avg %.6e' % (m, R, time.time() - t0, tot), flush=True)
