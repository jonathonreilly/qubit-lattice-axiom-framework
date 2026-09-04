"""kuhn.py -- Kuhn (Freudenthal) triangulated L^4 torus: P1 FEM Laplacian with lumped
mass, Regge action, and an EXACT Bloch reduction transverse to a plane wave along x_0.

Metric (lattice units, a = 1):
    g_{mu nu}(x) = delta_{mu nu} (1 + eps P_mu cos(kk x_0)),   kk = 2 pi n / L.
Edge squared lengths are the metric evaluated at the edge midpoint contracted with the
integer edge vector; everything downstream (volumes, stiffness, hinge areas, deficits)
is a function of squared edge lengths only.

--------------------------------------------------------------------------------
BLOCH DECOMPOSITION (derived here, validated against dense assembly in t1_dense.py)

The configuration depends on x_0 only, so the stiffness K and the lumped mass M are
invariant under translations in x_1, x_2, x_3.  Label a vertex (m, y), m = x_0 in Z_L,
y in Z_L^3.  Then

    K_{(m,y),(m',y')} = kappa_{m,m'}(y' - y),      M_{(m,y)} = mu_m .

Insert psi(m, y) = phi(m) e^{i q.y} / L^{3/2}:

    (K psi)(m,y) = sum_{m',y'} kappa_{m,m'}(y'-y) phi(m') e^{i q.y'} / L^{3/2}
                 = e^{i q.y} sum_{m'} [ sum_delta kappa_{m,m'}(delta) e^{i q.delta} ] phi(m')
                 = e^{i q.y} (K^q phi)(m) / L^{3/2} .

Every Kuhn simplex sits inside one unit cell, so delta_0 in {-1,0,+1} and
delta_{1,2,3} in {0,+-1}^3.  Hence K^q is an L x L PERIODIC TRIDIAGONAL hermitian
matrix, and the L^3 momenta q = (2 pi / L) Z_L^3 exhaust the whole spectrum of
B = M^{-1/2} K M^{-1/2}.  L^3 blocks of size L instead of one matrix of size L^4.

--------------------------------------------------------------------------------
IMPROVEMENT

Delta = M^{-1} K,  C = diag(tr g(x) / 4),  Delta_imp = Delta + Delta C Delta / 24,
i.e. the covariant Symanzik coefficient c = tr g / 96 (= 1/24 iff tr g = 4).
M and C are diagonal, hence commute, so conjugating by M^{1/2}:

    M^{1/2} (Delta C Delta) M^{-1/2} = M^{-1/2} K C M^{-1} K M^{-1/2} = B C B ,

so the symmetric operator actually diagonalised is B_imp = B + B C B / 24.
Delta is applied twice; Delta^2 is never formed.
"""
import itertools, math
import numpy as np
from collections import defaultdict

# ---------------------------------------------------------------- Kuhn combinatorics
PERMS = list(itertools.permutations(range(4)))


def _kuhn_offsets():
    out = np.zeros((24, 5, 4), dtype=np.int64)
    for i, pi in enumerate(PERMS):
        for j in range(1, 5):
            out[i, j] = out[i, j - 1]
            out[i, j, pi[j - 1]] += 1
    return out


W = _kuhn_offsets()                                   # (24,5,4)
TRIPLES = [(t, tuple(sorted(set(range(5)) - set(t))))
           for t in itertools.combinations(range(5), 3)]     # 10 hinges per simplex


def gdiag(t, eps, P, kk):
    """diag(g) at coordinate x_0 = t."""
    return 1.0 + eps * np.asarray(P, dtype=float) * np.cos(kk * t)


# ---------------------------------------------------------------- one simplex
def simplex(p0, wi, eps, P, kk):
    """Kuhn simplex of type wi based at x_0 = p0 (spatial base 0).
    Returns volume, 5x5 stiffness, and the 5x5 extended Gram matrix."""
    w = W[wi]
    l2 = np.zeros((5, 5))
    for a in range(5):
        for b in range(a + 1, 5):
            d = w[b] - w[a]
            tm = p0 + 0.5 * (w[a][0] + w[b][0])       # edge midpoint x_0
            v = float(np.sum(d * d * gdiag(tm, eps, P, kk)))
            l2[a, b] = l2[b, a] = v
    G = np.empty((4, 4))
    for a in range(1, 5):
        for b in range(1, 5):
            G[a - 1, b - 1] = 0.5 * (l2[0, a] + l2[0, b] - l2[a, b])
    V = math.sqrt(np.linalg.det(G)) / 24.0
    K4 = V * np.linalg.inv(G)
    K5 = np.zeros((5, 5))
    K5[1:, 1:] = K4
    K5[0, 1:] = -K4.sum(axis=0)
    K5[1:, 0] = -K4.sum(axis=1)
    K5[0, 0] = K4.sum()
    Gt = np.zeros((5, 5))
    Gt[1:, 1:] = G                                     # e_0 = 0 so row/col 0 vanish
    return V, K5, Gt


def hinge_area_angle(Gt, tri, rest):
    """Area of the 2-face `tri` and the interior dihedral angle of the simplex there.
    The angle is between the projections of the two opposite vertices onto the
    2-plane orthogonal to the hinge."""
    i, j, k = tri
    l, m = rest

    def ip(a, b, c, d):                                # <v_a - v_b, v_c - v_d>
        return Gt[a, c] - Gt[a, d] - Gt[b, c] + Gt[b, d]

    T = np.array([[ip(j, i, j, i), ip(j, i, k, i)],
                  [ip(k, i, j, i), ip(k, i, k, i)]])
    area = 0.5 * math.sqrt(max(np.linalg.det(T), 0.0))
    Ti = np.linalg.inv(T)
    cu = np.array([ip(j, i, l, i), ip(k, i, l, i)])
    cw = np.array([ip(j, i, m, i), ip(k, i, m, i)])
    uu = ip(l, i, l, i) - cu @ Ti @ cu                 # |P_perp (v_l - v_i)|^2
    ww = ip(m, i, m, i) - cw @ Ti @ cw
    uw = ip(l, i, m, i) - cu @ Ti @ cw
    return area, math.acos(min(1.0, max(-1.0, uw / math.sqrt(uu * ww))))


# ---------------------------------------------------------------- global assembly
def build(L, eps, P, kk, cpoint='vertex'):
    """Translation-reduced assembly.  Only simplices with spatial base 0 are
    enumerated; the rest follow by exact translation invariance in x_1,x_2,x_3."""
    stencil = defaultdict(float)      # (x0_src, d0,d1,d2,d3) -> K entry
    mass = np.zeros(L)
    vol = 0.0
    ang = defaultdict(float)
    area = {}
    for p0 in range(L):
        for wi in range(24):
            w = W[wi]
            V, K5, Gt = simplex(p0, wi, eps, P, kk)
            vol += V
            for a in range(5):
                sa = (p0 + w[a][0]) % L
                mass[sa] += V / 5.0
                for b in range(5):
                    d = w[b] - w[a]
                    stencil[(sa,) + tuple(int(x) for x in d)] += K5[a, b]
            for tri, rest in TRIPLES:
                A, th = hinge_area_angle(Gt, tri, rest)
                vs = sorted(tuple([int(p0 + w[a][0])] + [int(x) for x in w[a][1:]])
                            for a in tri)
                v0 = np.array(vs[0])
                key = (int(v0[0]) % L,
                       tuple(np.array(vs[1]) - v0), tuple(np.array(vs[2]) - v0))
                ang[key] += th
                area[key] = A
    S = sum(area[c] * (2.0 * math.pi - ang[c]) for c in ang)
    # improvement weight C(x) = tr g(x) / 4
    if cpoint == 'vertex':
        C = np.array([float(np.sum(gdiag(x0, eps, P, kk))) / 4.0 for x0 in range(L)])
    elif cpoint == 'edge':      # (1/8) sum over the 8 incident edges of l^2, same
        C = np.array([float(0.5 * (gdiag(x0 - 0.5, eps, P, kk)[0]
                                   + gdiag(x0 + 0.5, eps, P, kk)[0])
                            + np.sum(gdiag(x0, eps, P, kk)[1:])) / 4.0
                      for x0 in range(L)])
    else:
        raise ValueError(cpoint)
    return dict(stencil=dict(stencil), mass=mass, vol=vol * L ** 3, S=S * L ** 3,
                C=C, nhinge=len(ang))


# ---------------------------------------------------------------- Bloch spectrum
def _bands(L, stencil):
    """Collect the stencil into the three x_0-bands, keyed by transverse offset."""
    bd = [defaultdict(lambda: np.zeros(L)) for _ in range(3)]   # d0 = -1, 0, +1
    for (x0, d0, d1, d2, d3), v in stencil.items():
        bd[d0 + 1][(d1, d2, d3)][x0] += v
    return [{k: np.asarray(v) for k, v in b.items()} for b in bd]


def bloch_eigs(L, bands, mass, q, C=None, improve=True):
    """Eigenvalues of B (or B_imp) for a batch of transverse momenta q (n,3)."""
    q = np.asarray(q, dtype=float)
    n = q.shape[0]
    A = np.zeros((n, L), dtype=complex)     # d0 = 0
    Up = np.zeros((n, L), dtype=complex)    # d0 = +1
    Dn = np.zeros((n, L), dtype=complex)    # d0 = -1
    for tgt, bnd in ((Dn, bands[0]), (A, bands[1]), (Up, bands[2])):
        for dd, arr in bnd.items():
            tgt += np.exp(1j * (q @ np.array(dd, dtype=float)))[:, None] * arr[None, :]
    herm = float(np.max(np.abs(Dn - np.conj(np.roll(Up, 1, axis=1)))))
    r = 1.0 / np.sqrt(np.asarray(mass))
    idx = np.arange(L)
    H = np.zeros((n, L, L), dtype=complex)
    H[:, idx, idx] = A * (r * r)[None, :]
    H[:, idx, (idx + 1) % L] += Up * (r * np.roll(r, -1))[None, :]
    H[:, (idx + 1) % L, idx] += np.conj(Up) * (r * np.roll(r, -1))[None, :]
    if improve:
        cc = np.ones(L) if C is None else np.asarray(C, dtype=float)
        H = H + (H * cc[None, None, :]) @ H / 24.0      # B + B diag(C) B / 24
    return np.linalg.eigvalsh(H), herm


def all_momenta(L):
    return np.array(list(itertools.product(range(L), repeat=3)), dtype=float) * (2 * np.pi / L)


# ---------------------------------------------------------------- dense reference
def dense_eigs(L, eps, P, kk, C=None, improve=True):
    """Full L^4 x L^4 assembly with no translation-invariance assumption."""
    N = L ** 4
    def ix(v):
        return (((v[0] % L) * L + v[1] % L) * L + v[2] % L) * L + v[3] % L
    K = np.zeros((N, N))
    M = np.zeros(N)
    cache = {}
    for p in itertools.product(range(L), repeat=4):
        for wi in range(24):
            key = (p[0], wi)
            if key not in cache:
                cache[key] = simplex(p[0], wi, eps, P, kk)[:2]
            V, K5 = cache[key]
            vs = [ix(np.array(p) + W[wi][a]) for a in range(5)]
            for a in range(5):
                M[vs[a]] += V / 5.0
                for b in range(5):
                    K[vs[a], vs[b]] += K5[a, b]
    r = 1.0 / np.sqrt(M)
    H = K * r[:, None] * r[None, :]
    if improve:
        if C is None:
            cvec = np.ones(N)
        else:
            cvec = np.repeat(np.asarray(C, dtype=float), L ** 3)   # index = x0*L^3 + ...
        H = H + (H * cvec[None, :]) @ H / 24.0
    return np.sort(np.linalg.eigvalsh(H)), M


# ---------------------------------------------------------------- flat references
def flat_lattice_trace(L, svals, improve=True, c=1.0 / 24.0, f=None):
    """Exact heat trace of the (improved) lattice operator on a UNIFORM diagonal
    metric f: symbol D(k) = sum_mu 2(1-cos k_mu)/f_mu, improved D + c_f D^2 with
    c_f = (sum_mu f_mu)/96.  Returns (4 pi s)^2 * Tr / L^3 ... no: returns Tr."""
    f = np.ones(4) if f is None else np.asarray(f, dtype=float)
    d1 = 2.0 * (1.0 - np.cos(2 * np.pi * np.arange(L) / L))
    D = (d1[:, None, None, None] / f[0] + d1[None, :, None, None] / f[1]
         + d1[None, None, :, None] / f[2] + d1[None, None, None, :] / f[3])
    if improve:
        cf = float(np.sum(f)) / 96.0
        D = D + cf * D * D
    return np.array([float(np.exp(-s * D).sum()) for s in np.atleast_1d(svals)])


def flat_exact_trace(L, svals, f=None, wmax=6):
    """K_exact(s) = (4 pi s)^{-2} Vol sum_{w in Z^4} exp(-|w|_g^2 L^2/(4 s)) for the
    flat torus of period L with constant diagonal metric f (|w|_g^2 = sum f_mu w_mu^2)."""
    f = np.ones(4) if f is None else np.asarray(f, dtype=float)
    vol = L ** 4 * math.sqrt(float(np.prod(f)))
    ws = np.array(list(itertools.product(range(-wmax, wmax + 1), repeat=4)), dtype=float)
    w2 = (ws * ws) @ f
    out = []
    for s in np.atleast_1d(svals):
        out.append((4 * math.pi * s) ** -2 * vol * float(np.sum(np.exp(-w2 * L * L / (4 * s)))))
    return np.array(out)
