"""Lane RG probe G2: shared library.

On-shell 2<->2 sampler with the exact collision measure
    dmu = d^dk1 d^dk2 d^dk3 delta(E - w1 - w2) delta(w1 + w2 - w3 - w4),  k4 = k1 + k2 - k3 (mod 2pi)
implemented by line roots: k2 and k3 are sampled as (t, y_perp) with y_perp uniform and
ALL roots in t on the closed line t in (-pi, pi] found (grid of NG points + vectorised
bisection), each weighted by 1/|d/dt|.  This avoids the 'missed branch' pitfall of single
random-ray sampling (RN L2 referee) except for tangential roots between grid points.

Umklapp label: with every k in the principal zone (-pi, pi], D = k1 + k2 - k3 - k4 in 2pi Z^d;
umklapp iff D != 0.  D is exactly the sawtooth-momentum defect of the collision.
"""
import numpy as np

TWO_PI = 2 * np.pi


def wrap(a):
    return (a + np.pi) % TWO_PI - np.pi


def make_disp(kind, m=1.0):
    if kind == 'KG':
        return lambda k: np.sqrt(m ** 2 + np.sum(4 * np.sin(k / 2) ** 2, axis=-1))
    if kind == 'TB':
        return lambda k: -2 * np.sum(np.cos(k), axis=-1)
    raise ValueError(kind)


def _line_roots(G, n, NG=256, iters=55):
    """G(t) -> array (n, NG) or (n,) for t of shape (n, NG)/(n,).  Returns list of (row, t, |G'|)."""
    tg = np.linspace(-np.pi, np.pi, NG + 1)  # closed line, last == first point (periodic)
    T = np.broadcast_to(tg[None, :], (n, NG + 1))
    g = G(T)
    sgn = np.sign(g)
    br = np.nonzero(sgn[:, :-1] * sgn[:, 1:] < 0)
    rows, cols = br
    a = tg[cols].copy(); b = tg[cols + 1].copy()
    ga = g[rows, cols]
    for _ in range(iters):
        mid = 0.5 * (a + b)
        gm = G_rows(G, rows, mid)
        left = np.sign(gm) == np.sign(ga)
        a = np.where(left, mid, a); ga = np.where(left, gm, ga)
        b = np.where(left, b, mid)
    t = 0.5 * (a + b)
    h = 1e-6
    der = (G_rows(G, rows, t + h) - G_rows(G, rows, t - h)) / (2 * h)
    return rows, t, np.abs(der)


def G_rows(G, rows, t):
    # evaluate G for a subset of rows at scalar-per-row t
    return G(t[:, None], rows=rows)[:, 0]


def sample_shell(eps, d, E, N, rng, NG=256):
    """Configurations on the pair-energy shell E with exact collision measure weights.
    Returns k1,k2,k3,k4 (n,d) and weight w (n,)."""
    k1 = rng.uniform(-np.pi, np.pi, (N, d))
    y2 = rng.uniform(-np.pi, np.pi, (N, d - 1))
    e1 = eps(k1)

    def G2(t, rows=None):
        r = slice(None) if rows is None else rows
        kk = np.concatenate([t[..., None], np.broadcast_to(y2[r][:, None, :], t.shape + (d - 1,))], axis=-1)
        return eps(kk) - (E - e1[r])[:, None]
    rows, t, der = _line_roots(G2, N, NG)
    ok = der > 1e-9
    rows, t, der = rows[ok], t[ok], der[ok]
    k1 = k1[rows]; k2 = np.concatenate([t[:, None], y2[rows]], axis=1)
    w = 1.0 / der
    return _outgoing(eps, d, k1, k2, w, rng, NG)


def sample_free(eps, d, N, rng, NG=256):
    """k1, k2 uniform (vacuum / infinite-temperature weighting of the pair)."""
    k1 = rng.uniform(-np.pi, np.pi, (N, d)); k2 = rng.uniform(-np.pi, np.pi, (N, d))
    return _outgoing(eps, d, k1, k2, np.ones(N), rng, NG)


def _outgoing(eps, d, k1, k2, w_in, rng, NG):
    n = len(k1)
    K = k1 + k2
    E = eps(k1) + eps(k2)
    y3 = rng.uniform(-np.pi, np.pi, (n, d - 1))

    def G3(t, rows=None):
        r = slice(None) if rows is None else rows
        k3 = np.concatenate([t[..., None], np.broadcast_to(y3[r][:, None, :], t.shape + (d - 1,))], axis=-1)
        k4 = K[r][:, None, :] - k3
        return eps(k3) + eps(k4) - E[r][:, None]
    rows, t, der = _line_roots(G3, n, NG)
    ok = der > 1e-9
    rows, t, der = rows[ok], t[ok], der[ok]
    k3 = np.concatenate([t[:, None], y3[rows]], axis=1)
    a1, a2, a3 = wrap(k1[rows]), wrap(k2[rows]), wrap(k3)
    a4 = wrap(K[rows] - k3)
    w = w_in[rows] / der
    # drop exactly-trivial (forward / exchange-forward) roots
    triv = (np.linalg.norm(wrap(a3 - a1), axis=1) < 1e-7) | (np.linalg.norm(wrap(a3 - a2), axis=1) < 1e-7)
    keep = ~triv
    return a1[keep], a2[keep], a3[keep], a4[keep], w[keep]


def defect(k1, k2, k3, k4):
    D = k1 + k2 - k3 - k4
    return D  # in 2 pi Z^d up to roundoff


def umklapp(k1, k2, k3, k4):
    return np.any(np.abs(np.round(defect(k1, k2, k3, k4) / TWO_PI)) > 0, axis=1)


def Omega2(q):
    """massless lattice boson: Omega(q)^2 = sum 4 sin^2(q/2)"""
    return np.sum(4 * np.sin(q / 2) ** 2, axis=-1)
