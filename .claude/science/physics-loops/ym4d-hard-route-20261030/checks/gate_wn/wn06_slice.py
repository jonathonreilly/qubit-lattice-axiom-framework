"""Criterion (written first): on a finite grid of momenta, colour isotropic, real covariance, search for a slice S(k) of dimension
d-1 (S(-k) = conj S(k)) on which the lattice cubic form vanishes. d = 2 is the control: the minimum must reach about 0 (axial). In d = 3 and 4
report the best relative residual over restarts. PASS for 'no slice seen' if the d = 3 minimum stays above 1e-2 of a random slice's value
while the d = 2 control is below 1e-8 of it. This is evidence on a grid, not a proof."""
import sys, time, itertools
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(9)


def setup(d, N):
    pts = [p for p in itertools.product(range(N), repeat=d) if any(p)]
    index = {p: i for i, p in enumerate(pts)}
    neg = np.array([index[tuple((-c) % N for c in p)] for p in pts])
    # independent representatives
    reps = [i for i, p in enumerate(pts) if i <= neg[i]]
    tri = []
    for p, q in itertools.product(pts, pts):
        r = tuple((-a - b) % N for a, b in zip(p, q))
        if r in index:
            tri.append((index[p], index[q], index[r]))
    tri = np.array(tri)
    # canonical wave numbers in (-pi, pi), keep k1+k2+k3 = 0 mod 2 pi: the half-angle phases in Lemma 3.6 need a choice: use k3 = -k1-k2 exactly
    k = np.array(pts, dtype=float) * 2 * np.pi / N
    k[k > np.pi] -= 2 * np.pi
    return pts, neg, reps, tri, k


def loss_factory(d, N):
    pts, neg, reps, tri, k = setup(d, N)
    k1 = k[tri[:, 0]]
    k2 = k[tri[:, 1]]
    k3 = -k1 - k2
    # note: k3 differs from k[tri[:,2]] by 2 pi multiples; tilde polarisations pick signs. Convert slices consistently with phase factors:
    # the tilde vector at k3' = k3 + 2 pi m differs by exp(i pi m_mu) componentwise.
    sign3 = np.cos((k3 - k[tri[:, 2]]) / 2)  # +1 or -1 componentwise
    D1, D2, D3 = np.cos(k1 / 2), np.cos(k2 / 2), np.cos(k3 / 2)
    Y12, Y23, Y31 = 2 * np.sin((k1 - k2) / 2), 2 * np.sin((k2 - k3) / 2), 2 * np.sin((k3 - k1) / 2)
    nrep = len(reps)
    m = d - 1
    repidx = {r: i for i, r in enumerate(reps)}
    selfconj = [r for r in reps if neg[r] == r]

    def build(z):
        z = z.reshape(nrep, d, m, 2)
        B = np.empty((len(pts), d, m), dtype=complex)
        for i, r in enumerate(reps):
            q, _ = np.linalg.qr(z[i, :, :, 0] + 1j * z[i, :, :, 1])
            B[r] = q
            B[neg[r]] = q.conj()
        return B

    def loss(z):
        B = build(z)
        B1, B2, B3 = B[tri[:, 0]], B[tri[:, 1]], B[tri[:, 2]] * sign3[:, :, None]
        X12 = np.einsum("tui,tu,tuj->tij", B1, D3, B2)
        y3 = np.einsum("tu,tul->tl", Y12, B3)
        X23 = np.einsum("tuj,tu,tul->tjl", B2, D1, B3)
        y1 = np.einsum("tu,tui->ti", Y23, B1)
        X31 = np.einsum("tul,tu,tui->tli", B3, D2, B1)
        y2 = np.einsum("tu,tuj->tj", Y31, B2)
        F = (np.einsum("tij,tl->tijl", X12, y3) + np.einsum("tjl,ti->tijl", X23, y1) + np.einsum("tli,tj->tijl", X31, y2))
        return float(np.sum(np.abs(F) ** 2)) / len(tri)

    return loss, nrep, m


def run(d, N, starts):
    loss, nrep, m = loss_factory(d, N)
    n = nrep * d * m * 2
    randv = np.mean([loss(rng.normal(size=n)) for _ in range(20)])
    print(f"d={d} N={N}: reps {nrep}, reals {n}, random slice loss {randv:.4e}", flush=True)
    best = np.inf
    for s in range(starts):
        t0 = time.time()
        r = minimize(loss, rng.normal(size=n), method="L-BFGS-B", options={"maxiter": 600, "maxfun": 200000, "ftol": 1e-14, "gtol": 1e-8})
        best = min(best, r.fun)
        print(f"   start {s}: loss {r.fun:.4e}, ratio to random {r.fun/randv:.3e}, iters {r.nit}, {time.time()-t0:.0f}s", flush=True)
    print(f"d={d} N={N}: best ratio {best/randv:.3e}", flush=True)


if __name__ == "__main__":
    run(2, 5, 4)
    run(3, 3, 4)
    run(3, 5, 1)
    run(4, 3, 1)
