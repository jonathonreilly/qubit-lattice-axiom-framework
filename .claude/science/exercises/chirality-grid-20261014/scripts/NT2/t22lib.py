"""NT-2: pure-gauge hard-plaquette crossing kernel on a 3D lattice whose spatial slice is a 2x2 periodic torus (T22).

Links of the slice (sites (i, j), i, j in {0, 1}):
  a[j, 0]: (0,j)->(1,j),  a[j, 1]: (1,j)->(0,j)      (x-links of row j)
  b[i, 0]: (i,0)->(i,1),  b[i, 1]: (i,1)->(i,0)      (y-links of column i)
Config array layout (8,): [a00, a01, a10, a11, b00, b01, b10, b11] with a[j,i] -> index 2j+i, b[i,k] -> 4+2i+k.

Kernel K(u, v) = (2pi)^-3 int_{T^3} prod_l 1(|wrap(w_l + dg_l)| < delta), w = u - v (normalised Haar on gauge).
Closed form (PREREG 2(c)): (2pi)^-3 (B_a0*B_a1*B_b0*B_b1)(sigma).
"""
import numpy as np

TWO_PI = 2 * np.pi


def wrap(x):
    return (np.asarray(x) + np.pi) % TWO_PI - np.pi


def invariants(L):
    """L: (..., 8) link angles -> dict of X0, X1, Y0, Y1, phi00, phi10, phi01, phi11 (wrapped)."""
    a00, a01, a10, a11, b00, b01, b10, b11 = [L[..., k] for k in range(8)]
    out = dict(X0=wrap(a00 + a01), X1=wrap(a10 + a11), Y0=wrap(b00 + b01), Y1=wrap(b10 + b11),
               p00=wrap(a00 + b10 - a10 - b00), p10=wrap(a01 + b00 - a11 - b10),
               p01=wrap(a10 + b11 - a00 - b01), p11=wrap(a11 + b01 - a01 - b11))
    return out


def build_links(p00, p10, p01, X0, Y0, rng=None, gauge=True):
    """Links with given plaquettes (p11 = -(p00+p10+p01)) and Wilson lines X0, Y0; random gauge if rng given."""
    p00, p10, p01, X0, Y0 = np.broadcast_arrays(*[np.asarray(z, float) for z in (p00, p10, p01, X0, Y0)])
    L = np.zeros(p00.shape + (8,))
    L[..., 0] = X0                       # a00
    L[..., 1] = 0.0                      # a01 (tree)
    L[..., 2] = p01 + X0                 # a10
    L[..., 3] = -p00 - p01 - p10         # a11
    L[..., 4] = Y0                       # b00
    L[..., 5] = 0.0                      # b01 (tree)
    L[..., 6] = p00 + p01 + Y0           # b10
    L[..., 7] = 0.0                      # b11 (tree)
    if gauge and rng is not None:
        g = rng.uniform(-np.pi, np.pi, size=p00.shape + (2, 2))  # g[..., i, j] at site (i, j)
        for j in range(2):
            d = g[..., 1, j] - g[..., 0, j]
            L[..., 2 * j + 0] += d
            L[..., 2 * j + 1] -= d
        for i in range(2):
            d = g[..., i, 1] - g[..., i, 0]
            L[..., 4 + 2 * i + 0] += d
            L[..., 4 + 2 * i + 1] -= d
    return wrap(L)


def box4(sig, a):
    """(B_a1*B_a2*B_a3*B_a4)(sig), B_a = indicator of [-a/2, a/2]; a: (..., 4). Signed truncated powers."""
    sig = np.asarray(sig, float)
    out = np.zeros(np.broadcast(sig, a[..., 0]).shape)
    for e0 in (1, -1):
        for e1 in (1, -1):
            for e2 in (1, -1):
                for e3 in (1, -1):
                    s = sig + 0.5 * (e0 * a[..., 0] + e1 * a[..., 1] + e2 * a[..., 2] + e3 * a[..., 3])
                    out = out + (e0 * e1 * e2 * e3) * np.where(s > 0, s, 0.0) ** 3 / 6.0
    return out


def kernel_closed_inv(Iu, Iv, delta):
    """Closed form from invariants dicts (arrays broadcastable)."""
    a = np.stack([np.maximum(2 * delta - np.abs(wrap(Iu[k] - Iv[k])), 0.0) for k in ('X0', 'X1', 'Y0', 'Y1')], axis=-1)
    d00 = wrap(Iu['p00'] - Iv['p00']); d10 = wrap(Iu['p10'] - Iv['p10']); d01 = wrap(Iu['p01'] - Iv['p01'])
    # general branch (equals (d10 + d01)/2 for admissible pairs): sigma = -d00 + (wrap(d00+d10) + wrap(d00+d01))/2
    sig = wrap(-d00 + 0.5 * (wrap(d00 + d10) + wrap(d00 + d01)))
    val = box4(sig, a) / TWO_PI ** 3
    return np.where(np.all(a > 0, axis=-1), val, 0.0)


def kernel_matrix_closed(L, delta):
    I = invariants(L)
    Iu = {k: v[:, None] for k, v in I.items()}
    Iv = {k: v[None, :] for k, v in I.items()}
    return kernel_closed_inv(Iu, Iv, delta)


# ---------------- independent builder: explicit links -> arcs -> exact tau integral -----------------
def _arc_inter(c1, c2, h):
    """Intersection of arcs (c1-h, c1+h) and (c2-h, c2+h) on the circle (h < pi/2): (center, halflength) or None."""
    d = float(wrap(c2 - c1))
    if abs(d) >= 2 * h:
        return None
    return (float(wrap(c1 + d / 2)), h - abs(d) / 2)


def _overlap_len(A, B, tau):
    """|A cap (B - tau)| for arcs A=(cA,hA), B=(cB,hB), vectorised in tau."""
    cA, hA = A
    cB, hB = B
    d = np.abs(wrap(cB - tau - cA))
    return np.clip(hA + hB - d, 0.0, 2 * min(hA, hB))


def kernel_indep(u, v, delta, ng=4):
    """K(u, v) from explicit link angles, by a different route: arcs from links, then int dtau ovA(tau) ovB(tau)
    with all breakpoints located and Gauss-Legendre (exact for the piecewise-quadratic integrand)."""
    w = wrap(np.asarray(u) - np.asarray(v))
    # row j: a[j,0] + Delta_j in I and a[j,1] - Delta_j in I  -> arcs (-a0 +- delta) and (a1 +- delta)
    A = [_arc_inter(-w[2 * j], w[2 * j + 1], delta) for j in range(2)]
    B = [_arc_inter(-w[4 + 2 * i], w[4 + 2 * i + 1], delta) for i in range(2)]
    if any(z is None for z in A + B):
        return 0.0
    # tau = Gamma1 - Gamma0 = Delta1 - Delta0 ; ovA(tau) = |A0 cap (A1 - tau)|, ovB(tau) = |B0 cap (B1 - tau)|
    bps = []
    for (P, Qa) in ((A[0], A[1]), (B[0], B[1])):
        base = Qa[0] - P[0]
        for off in (0.0, Qa[1] + P[1], -(Qa[1] + P[1]), Qa[1] - P[1], P[1] - Qa[1]):
            bps.append(float(wrap(base - off)))
    bps = np.unique(np.concatenate([np.array(bps), [-np.pi, np.pi]]))
    bps = bps[(bps >= -np.pi) & (bps <= np.pi)]
    x, wts = np.polynomial.legendre.leggauss(ng)
    tot = 0.0
    for lo, hi in zip(bps[:-1], bps[1:]):
        if hi - lo < 1e-15:
            continue
        t = 0.5 * (hi - lo) * x + 0.5 * (hi + lo)
        f = _overlap_len(A[0], A[1], t) * _overlap_len(B[0], B[1], t)
        tot += 0.5 * (hi - lo) * np.dot(wts, f)
    return tot / TWO_PI ** 3


def kernel_matrix_indep(L, delta):
    k = L.shape[0]
    K = np.zeros((k, k))
    for i in range(k):
        for j in range(i, k):
            K[i, j] = K[j, i] = kernel_indep(L[i], L[j], delta)
    return K


def kernel_mc(u, v, delta, n, rng):
    """Brute-force Monte Carlo over the 4 site gauge angles (validates the whole reduction)."""
    w = wrap(np.asarray(u) - np.asarray(v))
    g = rng.uniform(-np.pi, np.pi, size=(n, 2, 2))
    ok = np.ones(n, bool)
    for j in range(2):
        d = g[:, 1, j] - g[:, 0, j]
        ok &= np.abs(wrap(w[2 * j] + d)) < delta
        ok &= np.abs(wrap(w[2 * j + 1] - d)) < delta
    for i in range(2):
        d = g[:, i, 1] - g[:, i, 0]
        ok &= np.abs(wrap(w[4 + 2 * i] + d)) < delta
        ok &= np.abs(wrap(w[4 + 2 * i + 1] - d)) < delta
    p = ok.mean()
    return p, np.sqrt(p * (1 - p) / n)


def sample_plaq(n, m, rng):
    """n plaquette triples (p00, p10, p01) with all four |p| <= m (p11 = -sum)."""
    out = []
    while len(out) < n:
        p = rng.uniform(-m, m, size=(4 * n, 3))
        p11 = -p.sum(1)
        out.extend(p[np.abs(p11) <= m])
    return np.array(out[:n])


def nmin(K):
    """lambda_min of the unit-diagonal normalised matrix (inertia-preserving), plus raw min/max."""
    d = np.sqrt(np.clip(np.diag(K), 1e-300, None))
    Kn = K / d[:, None] / d[None, :]
    ev = np.linalg.eigvalsh(Kn)
    evr = np.linalg.eigvalsh(K)
    return ev[0], evr[0], evr[-1]
