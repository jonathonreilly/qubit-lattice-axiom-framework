"""GUIDE run for FINISH row 894 (a run can refute or guide; it proves nothing).

Model: Wilson lattice gauge theory in 2+1 dimensions on a spatial torus of 1 x 1
sites: two links U1, U2 (closed loops), one space-like plaquette
x_P = (1/2) tr(U1 U2 U1^-1 U2^-1), one time-like plaquette per link and step.
Transfer operator on conjugation-invariant functions of (U1, U2):
T = K^(1/2) B K^(1/2), K = k (x) k, k(V) ~ exp(beta x(V)), B = exp(beta x_P).
Centre flips: U1 -> -U1, U2 -> -U2. Flux sector chi = (odd, even).
This is the smallest lattice with a toron valley (commuting pairs) and a wall
(trace-zero holonomy). Groups: SU(2) (character basis, truncated at jmax),
and the frozen subgroups 2T (24 elements) and Q_8 (exact, finite).

Criteria written before the run:
C0 basis orthonormal under the quadrature to 1e-9.
C1 beta -> 0: kappa -> 2 for SU(2) and 2T, 4 for Q_8; theta -> I_2/I_1 (SU(2)).
C2 Lemma R: W (1 - rho) <= 1 in every row (W = (kappa-1)/(kappa (1-theta^2))).
C3 (KE-ineq) lambda_bar (kappa - 1) <= kappa (1 - theta^2) in every row.
C4 SU(2) numbers stable between jmax and jmax - 1 (reported).
Outputs per beta: kappa, theta, rho, W, r_W = W (1 - rho), jump fraction J_1
(Corollary A2: 1 - J_1 = (3/4) lambda_bar (kappa-1)/(kappa (1-theta))).
"""
import sys, itertools
import numpy as np

def bessel_I(n, x, npts=4000):
    t = (np.arange(npts) + 0.5) * np.pi / npts
    return np.mean(np.exp(x * np.cos(t)) * np.cos(n * t))

# ---------------- SU(2) in the character basis ----------------
def su2_run(beta, jmax2, na=56, nc=40):
    # jmax2 = 2*jmax (integer). alpha grid on [0, pi], c = cos(gamma) on [-1, 1]
    xa, wa = np.polynomial.legendre.leggauss(na)
    al = (xa + 1) * np.pi / 2; wal = wa * np.pi / 2 * (2 / np.pi) * np.sin(al) ** 2
    xc, wc = np.polynomial.legendre.leggauss(nc); wcc = wc / 2
    # radial functions f_{jJ}
    F = {}
    for tj in range(0, jmax2 + 1):
        m = (np.arange(tj + 1) - tj / 2.0)           # m = -j..j
        V = np.vander(m, tj + 1, increasing=True)     # columns m^0..m^(2j)
        Q, _ = np.linalg.qr(V)                        # discrete Legendre polys
        for J in range(0, tj + 1):
            p = Q[:, J]
            if J % 2 == 0:
                f = (p[:, None] * np.cos(2 * m[:, None] * al[None, :])).sum(0)
            else:
                f = (p[:, None] * np.sin(2 * m[:, None] * al[None, :])).sum(0)
            nrm = np.sqrt((wal * f * f).sum())
            F[(tj, J)] = f / nrm
    Jmax = jmax2
    PJ = np.zeros((Jmax + 1, nc))
    for J in range(Jmax + 1):
        c = np.zeros(J + 1); c[J] = 1
        PJ[J] = np.polynomial.legendre.legval(xc, c) * np.sqrt(2 * J + 1)
    s1 = np.sin(al) ** 2
    Wgt = np.exp(beta * (1 - 2 * s1[:, None, None] * s1[None, :, None] * (1 - xc ** 2)[None, None, :]))
    # G[J,J',a1,a2]
    G = np.einsum('abc,c,Jc,Kc->JKab', Wgt, wcc, PJ, PJ, optimize=True)
    cj = np.clip(np.array([bessel_I(tj + 1, beta) / bessel_I(1, beta) for tj in range(jmax2 + 1)]), 0.0, None)
    out = {}
    for sec in [(0, 0), (1, 0)]:
        idx = [(t1, t2, J) for t1 in range(sec[0], jmax2 + 1, 2) for t2 in range(sec[1], jmax2 + 1, 2)
               for J in range(0, min(t1, t2) + 1)]
        D = len(idx)
        A1 = np.array([F[(t1, J)] for (t1, t2, J) in idx])      # D x na
        A2 = np.array([F[(t2, J)] for (t1, t2, J) in idx])
        Js = np.array([J for (_, _, J) in idx])
        B = np.zeros((D, D))
        for J in range(Jmax + 1):
            ia = np.where(Js == J)[0]
            if len(ia) == 0: continue
            for K in range(Jmax + 1):
                ib = np.where(Js == K)[0]
                if len(ib) == 0: continue
                X = A1[ia][:, None, :] * A1[ib][None, :, :] * wal[None, None, :]
                Y = A2[ia][:, None, :] * A2[ib][None, :, :] * wal[None, None, :]
                B[np.ix_(ia, ib)] = np.einsum('ija,ab,ijb->ij', X, G[J, K], Y, optimize=True)
        kd = np.sqrt(np.array([cj[t1] * cj[t2] for (t1, t2, J) in idx]))
        T = kd[:, None] * B * kd[None, :]
        T = (T + T.T) / 2
        ev, evec = np.linalg.eigh(T)
        out[sec] = (idx, ev[::-1], evec[:, ::-1], T, A1, A2, Js)
    # C0: orthonormality check in the even sector (use Wgt = 1)
    idx, ev0, U0, T0, A1, A2, Js = out[(0, 0)]
    # values on the 3D grid
    def on_grid(sec, vec):
        idx, _, _, _, A1, A2, Js = out[sec]
        val = np.einsum('d,da,db,dc->abc', vec, A1, A2, PJ[Js], optimize=True)
        return val
    w3 = wal[:, None, None] * wal[None, :, None] * wcc[None, None, :]
    lam0 = ev0[0]; Om = U0[:, 0]
    # undo K^(1/2): eigenvectors of T live in L^2(dU) directly (T acts on functions)
    Omg = on_grid((0, 0), Om)
    if Omg.sum() < 0: Omg = -Omg; Om = -Om
    idx1, ev1, U1, T1, _, _, _ = out[(1, 0)]
    Psi = U1[:, 0]; Psig = on_grid((1, 0), Psi)
    n0 = (w3 * Omg ** 2).sum(); n1 = (w3 * Psig ** 2).sum()
    theta = ev1[0] / lam0; rho = ev0[1] / lam0
    mask = Omg > 1e-7 * Omg.max()
    g = np.where(mask, Psig / np.where(mask, Omg, 1.0), 0.0)
    kappa = (w3 * g ** 4 * Omg ** 2).sum() / n0 / (n1 / n0) ** 2
    # fused vector g^2 Omega projected on the even basis
    fus = np.where(mask, Psig ** 2 / np.where(mask, Omg, 1.0), 0.0) / (n1 / n0) * 1.0
    idx, _, _, _, A1, A2, Js = out[(0, 0)]
    coef = np.einsum('abc,abc,da,db,dc->d', w3, fus, A1, A2, PJ[Js], optimize=True)
    g2Pg2 = coef @ T0 @ coef / lam0 / n0
    kap_proj = coef @ coef / n0
    minOm = Omg.min() / Omg.max()
    return dict(kappa=kappa, theta=theta, rho=rho, g2Pg2=g2Pg2, kap_proj=kap_proj,
                n0=n0, n1=n1, minOm=minOm, dim=(len(idx), len(idx1)))

# ---------------- finite subgroups of SU(2), exact ----------------
def qmul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return np.array([w1*w2 - x1*x2 - y1*y2 - z1*z2, w1*x2 + x1*w2 + y1*z2 - z1*y2,
                     w1*y2 - x1*z2 + y1*w2 + z1*x2, w1*z2 + x1*y2 - y1*x2 + z1*w2])
def group(name):
    els = []
    for s in (1, -1):
        for k in range(4):
            v = np.zeros(4); v[k] = s; els.append(v)
    if name == '2T':
        for sg in itertools.product((1, -1), repeat=4):
            els.append(np.array(sg) / 2.0)
    return np.array(els)
def finite_run(beta, name):
    E = group(name); n = len(E)
    def find(v): return int(np.argmin(((E - v) ** 2).sum(1)))
    mul = np.array([[find(qmul(E[a], E[b])) for b in range(n)] for a in range(n)])
    inv = np.array([find(E[a] * np.array([1, -1, -1, -1])) for a in range(n)])
    x = E[:, 0]                                   # (1/2) tr
    k1 = np.exp(beta * x[mul[inv][:, :]])         # k(a^-1 a')
    Kop = np.einsum('ac,bd->abcd', k1, k1).reshape(n * n, n * n)
    comm = np.array([[mul[mul[a, b], mul[inv[a], inv[b]]] for b in range(n)] for a in range(n)])
    Bd = np.exp(beta * x[comm]).reshape(n * n)
    # gauge projection (simultaneous conjugation)
    Pi = np.zeros((n * n, n * n))
    for h in range(n):
        ca = mul[mul[h], :][:, inv[h]]            # ca[a] = h a h^-1
        ca = np.array([mul[mul[h, a], inv[h]] for a in range(n)])
        tgt = (ca[:, None] * n + ca[None, :]).reshape(n * n)
        Pi[tgt, np.arange(n * n)] += 1.0 / n
    ek, vk = np.linalg.eigh((Kop + Kop.T) / 2); ek = np.clip(ek, 0, None)
    Kh = (vk * np.sqrt(ek)) @ vk.T
    T = Pi @ Kh @ (Bd[:, None] * Kh) @ Pi; T = (T + T.T) / 2
    # centre flips on link 1 and link 2
    m1 = find(np.array([-1.0, 0, 0, 0]))
    f1 = (mul[m1][:, None] * n + np.arange(n)[None, :]).reshape(n * n)
    f2 = (np.arange(n)[:, None] * n + mul[m1][None, :]).reshape(n * n)
    C1 = np.zeros((n * n, n * n)); C1[f1, np.arange(n * n)] = 1
    C2 = np.zeros((n * n, n * n)); C2[f2, np.arange(n * n)] = 1
    def top(s1, s2, k=2):
        Pr = Pi @ (np.eye(n * n) + s1 * C1) @ (np.eye(n * n) + s2 * C2) / 4
        ev, evec = np.linalg.eigh(Pr @ T @ Pr)
        return ev[::-1][:k], evec[:, ::-1][:, :k]
    e0, v0 = top(1, 1); e1, v1 = top(-1, 1)
    Om = v0[:, 0] * np.sign(v0[:, 0].sum()); Psi = v1[:, 0]
    lam0 = e0[0]; theta = e1[0] / lam0; rho = e0[1] / lam0
    g = Psi / Om
    kappa = (g ** 4 * Om ** 2).sum()
    fus = g ** 2 * Om
    g2Pg2 = fus @ T @ fus / lam0
    return dict(kappa=kappa, theta=theta, rho=rho, g2Pg2=g2Pg2, kap_proj=kappa, minOm=Om.min() / Om.max())

def derived(r):
    k, th, rho = r['kappa'], r['theta'], r['rho']
    W = (k - 1) / (k * (1 - th ** 2)) if k > 1 + 1e-13 else 0.0
    lamb = (k - r['g2Pg2']) / (k - 1) if k > 1 + 1e-9 else float('nan')
    J1 = 1 - 0.75 * lamb * (k - 1) / (k * (1 - th)) if k > 1 + 1e-9 else 1.0
    return W, W * (1 - rho), lamb, J1

if __name__ == '__main__':
    betas = [0.25, 1.0, 1.5, 2.0, 2.3, 2.6, 3.0, 4.0, 5.0, 6.0, 8.0]
    jm = int(sys.argv[1]) if len(sys.argv) > 1 else 14       # 2*jmax
    print('SU(2), 2*jmax = %d and %d' % (jm, jm - 2))
    print(' beta   kappa    (jmax-1)   theta      rho       W       r_W    lam_bar    J_1   KE-ok  kap_proj  minOm')
    for b in betas:
        r = su2_run(b, jm); r2 = su2_run(b, jm - 2)
        W, rW, lamb, J1 = derived(r)
        ke = lamb * (r['kappa'] - 1) <= r['kappa'] * (1 - r['theta'] ** 2) + 1e-9
        print('%5.2f  %8.5f  %8.5f  %9.6f  %9.6f  %7.3f  %6.4f  %7.4f  %6.4f  %s  %8.5f  %.1e' % (
            b, r['kappa'], r2['kappa'], r['theta'], r['rho'], W, rW, lamb, J1, ke, r['kap_proj'], r['minOm']))
    for name in ['2T', 'Q8']:
        print(name)
        print(' beta   kappa      theta        rho         W        r_W     lam_bar    J_1')
        for b in betas:
            r = finite_run(b, name if name == '2T' else 'Q8')
            W, rW, lamb, J1 = derived(r)
            print('%5.2f  %9.6f  %10.7f  %10.7f  %8.4f  %8.5f  %7.4f  %7.4f' % (
                b, r['kappa'], r['theta'], r['rho'], W, rW, lamb, J1))
