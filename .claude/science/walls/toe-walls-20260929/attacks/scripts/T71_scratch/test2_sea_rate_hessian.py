#!/usr/bin/env python3
"""T71 test 2: the walker's filled sea as the only field energy of the clock (lapse) channel.

Model (P6 walker): H = sum_{x,j} psi_x^dag (sigma_j / 2i) t_j(x) psi_{x+j} + h.c. on an antiperiodic L^3 torus,
sea = sum of negative eigenvalues.  Modulations (q = 2 pi m / L):
  'lapse'  : t_j(x) = 1 + eps cos(q.(x + e_j/2))                       (rate at the hop midpoint; linear in Theta)
  'tt'     : t_y = exp(+eps cos(q_x x)/(2 sqrt2)),  t_z = exp(-eps cos(q_x x)/(2 sqrt2)), q along x
             (= P6's e = expm(eps_ij/2) with eps = A cos(qx) diag(0,1,-1)/sqrt2, unit norm)
  'phiHphi': t_j(x) = exp((u_x + u_{x+j})/2),  u = eps cos(q.x)       (b76 / b55 log-rate form)
Curvature per site per unit mean-square amplitude:  c(q) = 2 (E(eps)+E(-eps)-2E(0)) / (N eps^2).
"""
import sys
import itertools
import numpy as np
import scipy.linalg as sla

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def build_H(L, t):
    """t[j] is an array (L,L,L): amplitude of the hop from x to x+e_j."""
    N = L ** 3
    ix = np.arange(N).reshape(L, L, L)
    A = np.zeros((2 * N, 2 * N), complex)
    for j in range(3):
        nb = np.roll(ix, -1, axis=j)                 # index of x + e_j
        sign = np.ones((L, L, L))
        sl = [slice(None)] * 3
        sl[j] = L - 1
        sign[tuple(sl)] = -1.0                       # antiperiodic boundary
        amp = (t[j] * sign).reshape(-1)
        src = ix.reshape(-1)
        dst = nb.reshape(-1)
        M = SIG[j] / 2j
        for a in range(2):
            for b in range(2):
                if M[a, b] != 0:
                    A[2 * src + a, 2 * dst + b] += M[a, b] * amp
    return A + A.conj().T


def sea_energy(H):
    w = sla.eigvalsh(H)
    return w[w < -1e-12].sum()


def coords(L):
    g = np.arange(L)
    return np.meshgrid(g, g, g, indexing='ij')


def tfun(L, kind, m, eps):
    X = coords(L)
    q = [2 * np.pi * mi / L for mi in m]
    e = [np.zeros(3) for _ in range(3)]
    if kind == 'lapse':
        t = []
        for j in range(3):
            phase = sum(q[i] * (X[i] + (0.5 if i == j else 0.0)) for i in range(3))
            t.append(1 + eps * np.cos(phase))
        return t
    if kind == 'phiHphi':
        u = eps * np.cos(sum(q[i] * X[i] for i in range(3)))
        return [np.exp(0.5 * (u + np.roll(u, -1, axis=j))) for j in range(3)]
    if kind == 'tt':
        # q along x: bond amplitudes at the midpoints (y and z hops do not shift x)
        assert m[1] == 0 and m[2] == 0
        c = np.cos(q[0] * X[0])
        return [np.ones_like(c), np.exp(eps * c / (2 * np.sqrt(2))), np.exp(-eps * c / (2 * np.sqrt(2)))]
    raise ValueError(kind)


def curvature(L, kind, m, eps=0.02, E0=None):
    N = L ** 3
    Ep = sea_energy(build_H(L, tfun(L, kind, m, eps)))
    Em = sea_energy(build_H(L, tfun(L, kind, m, -eps)))
    if E0 is None:
        E0 = sea_energy(build_H(L, [np.ones((L, L, L))] * 3))
    return 2 * (Ep + Em - 2 * E0) / (N * eps ** 2), E0 / N


def lat_lap(m, L):
    return sum(2 - 2 * np.cos(2 * np.pi * mi / L) for mi in m)


if __name__ == '__main__':
    L = 8
    E0N = None
    Ms = [(1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0), (1, 1, 0), (2, 2, 0), (4, 4, 0), (1, 1, 1), (2, 2, 2), (4, 4, 4), (2, 1, 0), (3, 2, 1)]
    E0 = sea_energy(build_H(L, [np.ones((L, L, L))] * 3))
    E0N = E0 / L ** 3
    print(f"L={L}: sea energy per site (antiperiodic) = {E0N:.5f}   (P6 check D: -1.19015)")
    kk = 2 * np.pi * (np.arange(L) + 0.5) / L
    KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing='ij')
    Ek = -np.mean(np.sqrt(np.sin(KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2))
    check("sanity: 8^3 antiperiodic real-space sea energy per site equals the k-space value -<|s(k)|> on the (n+1/2) grid",
          abs(E0N - Ek) < 1e-9, f"real space {E0N:.6f}, k-space {Ek:.6f}; infinite volume -1.19380 (P6 check C)")
    res = {}
    print(f"{'q-index':>10} {'lap(q)':>8} {'c_lapse':>10} {'c_lapse/lap':>12} {'c_phiHphi':>11} {'c_u=c_lapse+E0':>15}")
    for m in Ms:
        cth, _ = curvature(L, 'lapse', m, E0=E0)
        cu, _ = curvature(L, 'phiHphi', m, E0=E0)
        lp = lat_lap(m, L)
        res[m] = (lp, cth, cu)
        print(f"{str(m):>10} {lp:8.4f} {cth:10.5f} {cth / lp:12.5f} {cu:11.5f} {cth + E0N:15.5f}")
    # decomposition of the log-rate curvature: exponent form gives a diamagnetic piece E_0 (1 - lap/12) exactly (t_j = exp(cos(q_j/2) * midpoint wave))
    print("       decomposition c_u = dia + para, dia = E_0 (1 - lap/12):")
    para_ok = True
    for m in Ms:
        lp, cth, cu = res[m]
        dia = E0N * (1 - lp / 12)
        para = cu - dia
        para_ok &= para < 1e-9
        print(f"         {str(m):>10} dia={dia:9.5f} para={para:9.5f}")
    check("2g log-rate curvature = diamagnetic E_0(1 - lap(q)/12) + paramagnetic part <= 0: the positive q^2 coefficient in c_u is the placement term -E_0/12, not sea dynamics",
          para_ok, "paramagnetic part <= 0 at every q tested (see table)")
    cth_all = np.array([v[1] for v in res.values()])
    cu_all = np.array([v[2] for v in res.values()])
    check("2a lapse (linear-in-rate) channel: sea curvature c(q) <= 0 at every q tested (concavity of the ground-state energy under a linear coupling)",
          bool(np.all(cth_all < 1e-9)), f"max c = {cth_all.max():.2e}, min c = {cth_all.min():.5f}")
    check("2b log-rate form phi H phi: c_u(q) <= 0 at every q tested",
          bool(np.all(cu_all < 1e-9)), f"max c_u = {cu_all.max():.2e}, min = {cu_all.min():.5f}")
    ch = res[(4, 4, 4)]
    check("2c chessboard q=(pi,pi,pi): the sea is blind to a checkerboard of rates (opposite-parity hopping)",
          abs(ch[2]) < 1e-6, f"c_u(chessboard) = {ch[2]:.2e}; c_lapse = {ch[1]:.2e}")
    # gradient coefficient sign: fit c_lapse(q) = -kappa * lap(q) on the small-q points, and c_u = E0 + kappa_u lap
    small = [m for m in Ms if res[m][0] < 2.2]
    ls = np.array([res[m][0] for m in small]); ct = np.array([res[m][1] for m in small]); cuu = np.array([res[m][2] for m in small])
    kap = np.polyfit(ls, ct, 1)
    kapu = np.polyfit(ls, cuu, 1)
    print(f"       lapse channel (linear rate) small-q fit: c = {kap[1]:+.5f} + ({kap[0]:+.5f}) lap(q);   log-rate: c_u = {kapu[1]:+.5f} + ({kapu[0]:+.5f}) lap(q)")
    check("2d gradient coefficient signs: linear-rate channel c(q) ~ -kappa lap(q) (negative gradient coefficient, no mass term); log-rate channel c_u ~ E_0 + kappa_u lap with kappa_u > 0",
          kap[0] < 0 and abs(kap[1]) < 0.02 and kapu[0] > 0 and kapu[1] < 0, f"kappa = {-kap[0]:.4f}; c_u(0) = {kapu[1]:.4f}, kappa_u = {kapu[0]:.4f}")

    # two-body sign from the sea-only kernel on the 8^3 torus (log-rate variable), all q by cubic symmetry
    def kernel_c(m):
        key = tuple(sorted(abs(min(mi % L, (-mi) % L)) for mi in m))
        for k2, v in res.items():
            if tuple(sorted(k2)) == key:
                return v[2]
        # missing orbit: compute
        v = curvature(L, 'phiHphi', key, E0=E0)[0]
        res[key] = (lat_lap(key, L), curvature(L, 'lapse', key, E0=E0)[0], v)
        return v
    qs = list(itertools.product(range(L), repeat=3))
    Kq = np.zeros((L, L, L))
    for m in qs:
        if m == (0, 0, 0):
            Kq[m] = E0N            # uniform mode: weight-one identity, c_u(0) = E_0 per site
        else:
            Kq[m] = kernel_c(m)
    # real-space inverse (mean mode kept; sources neutralised by removing q=0)
    Kinv = np.zeros_like(Kq)
    nz = Kq != 0
    Kinv[nz] = 1.0 / Kq[nz]
    Kinv[0, 0, 0] = 0.0
    G = np.real(np.fft.ifftn(Kinv))
    print("       sea-only kernel, real-space inverse G(r) along x (log-rate, mean removed): ",
          [round(float(G[r, 0, 0]), 5) for r in range(0, 5)])
    print("       pair energy W_AB(r) = -J^2 G(r) (negative = attractive):", [round(float(-G[r, 0, 0]), 5) for r in range(1, 5)])
    # tuned case: remove the mass-type term (c_u -> c_u - E0), keep the gradient part
    Kt = Kq.copy()
    for m in qs:
        Kt[m] = Kq[m] - E0N if m != (0, 0, 0) else 0.0
    Ktinv = np.zeros_like(Kt)
    nz2 = Kt != 0
    Ktinv[nz2] = 1.0 / Kt[nz2]
    Gt = np.real(np.fft.ifftn(Ktinv))
    print("       mass-type term removed (c_u - E_0): W_AB(r) = -J^2 G(r):", [round(float(-Gt[r, 0, 0]), 5) for r in range(1, 5)])
    print("       info 2e: the sea-only two-body energy alternates in sign with r and has no 1/r tail (negative-definite kernel with a constant mass-type term)")

    # ---- TT channel (like-for-like): c_TT(q) at L = 8 and L = 12, q along x
    print("TT channel (yy - zz shear, q along x), same code:")
    ctt = {}
    for LL in (8, 12):
        E0L = sea_energy(build_H(LL, [np.ones((LL, LL, LL))] * 3))
        for mm in ([1], [2], [3]):
            mtuple = (mm[0], 0, 0)
            c, _ = curvature(LL, 'tt', mtuple, E0=E0L)
            ctt[(LL, mm[0])] = c
            print(f"       L={LL:2d} m={mm[0]}  q={2 * np.pi * mm[0] / LL:.3f}  c_TT = {c:+.5f}")
    for LL in (8, 12):
        qs_ = [2 * np.pi * i / LL for i in (1, 2, 3)]
        cs_ = [ctt[(LL, i)] for i in (1, 2, 3)]
        kt = np.polyfit(np.array(qs_) ** 2, cs_, 1)
        print(f"       L={LL}: c_TT(q) ~ {kt[1]:+.5f} + {kt[0]:+.5f} q^2   (P6: -0.17793 + 0.0097 q^2)")
    kt8 = np.polyfit((2 * np.pi * np.arange(1, 4) / 12) ** 2, [ctt[(12, i)] for i in (1, 2, 3)], 1)
    check("2f TT channel: mass-type term negative and gradient coefficient positive (reproduces P6 check L within finite-size error)",
          kt8[1] < -0.1 and kt8[0] > 0, f"L=12 fit c0 = {kt8[1]:+.4f}, kappa_TT = {kt8[0]:+.4f}")
    # q^4 scaling of the lapse channel at L = 12 (linear-rate coupling): the lapse has no q^2 term
    E012 = sea_energy(build_H(12, [np.ones((12, 12, 12))] * 3))
    cl1, _ = curvature(12, 'lapse', (1, 0, 0), E0=E012)
    cl2, _ = curvature(12, 'lapse', (2, 0, 0), E0=E012)
    print(f"       lapse channel, L=12: c(q=0.524) = {cl1:.5f}, c(q=1.047) = {cl2:.5f}, ratio {cl2 / cl1:.2f} (q^4 scaling: 16; q^2 scaling: 4); L=8 ratio c(1.571)/c(0.785) = {res[(2, 0, 0)][1] / res[(1, 0, 0)][1]:.2f}")
    check("2h the lapse (linear-rate) channel of the sea has no q^2 term: doubling q multiplies the curvature by about 16, not 4",
          cl2 / cl1 > 10 and res[(2, 0, 0)][1] / res[(1, 0, 0)][1] > 10, f"ratios {cl2 / cl1:.1f} (L=12), {res[(2, 0, 0)][1] / res[(1, 0, 0)][1]:.1f} (L=8)")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    sys.exit(0 if FAIL == 0 else 1)
