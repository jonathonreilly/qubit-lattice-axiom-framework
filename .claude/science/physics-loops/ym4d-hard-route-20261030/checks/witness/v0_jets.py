#!/usr/bin/env python3
"""W1: a combination of T with zero quartic jet has zero cubic jet.

Criteria: CRITERIA.md, W1. Jets from Text 0 of parts/witness.md:
  psi_Gamma = Phi + Q + O(A^3), Q = -(1/2) sum_{s<t} e_s e_t A_s x A_t,
  T = (1/4) psi_1 . (psi_2 x psi_3) + O(psi^5),
so t_3 = (1/4) Phi_1 . Phi_2 x Phi_3 and
   t_4 = (1/4)(Q_1 . Phi_2 x Phi_3 + Phi_1 . Q_2 x Phi_3 + Phi_1 . Phi_2 x Q_3).
"""
import itertools, json, os, resource, sys
import numpy as np

LIM = 2 * 1024**3


def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        rss *= 1024
    if rss > LIM:
        sys.exit("rss limit")


def bonds_of(dims):
    idx = {}
    for x in itertools.product(*[range(n) for n in dims]):
        for mu in range(len(dims)):
            idx[(x, mu)] = len(idx)
    return idx


def step(x, mu, dims, sgn):
    y = list(x)
    y[mu] = (y[mu] + sgn) % dims[mu]
    return tuple(y)


def path(moves, o, dims, idx):
    """moves: list of signed axis labels, +1..+d, -1..-d. Returns [(bond,sign)]."""
    x = o
    out = []
    for m in moves:
        mu = abs(m) - 1
        if m > 0:
            out.append((idx[(x, mu)], 1))
            x = step(x, mu, dims, 1)
        else:
            y = step(x, mu, dims, -1)
            out.append((idx[(y, mu)], -1))
            x = y
    return out, x


def lassos(dims, idx, o):
    """Plaquette lassos and rectangles based at o, with axis-ordered tails."""
    d = len(dims)
    out = []
    origins = list(itertools.product(range(2), repeat=d))
    for t in origins:
        tail = []
        for mu in range(d):
            tail += [mu + 1] * t[mu]
        for mu in range(d):
            for nu in range(mu + 1, d):
                for (a, b) in [(1, 1), (2, 1), (1, 2)]:
                    loop = [mu + 1] * a + [nu + 1] * b + [-(mu + 1)] * a + [-(nu + 1)] * b
                    moves = tail + loop + [-m for m in reversed(tail)]
                    p, end = path(moves, o, dims, idx)
                    assert end == o
                    # remove immediate backtracks
                    q = []
                    for (bd, s) in p:
                        if q and q[-1][0] == bd and q[-1][1] == -s:
                            q.pop()
                        else:
                            q.append((bd, s))
                    out.append(q)
    return out


def su2(v):
    """exp(i v.sigma/2), v shape (...,3)."""
    th = np.linalg.norm(v, axis=-1)
    c = np.cos(th / 2)
    with np.errstate(invalid="ignore", divide="ignore"):
        s = np.where(th > 1e-14, np.sin(th / 2) / th, 0.5)
    x, y, z = v[..., 0], v[..., 1], v[..., 2]
    out = np.zeros(v.shape[:-1] + (2, 2), dtype=complex)
    out[..., 0, 0] = c + 1j * s * z
    out[..., 1, 1] = c - 1j * s * z
    out[..., 0, 1] = 1j * s * x + s * y
    out[..., 1, 0] = 1j * s * x - s * y
    return out


def holonomy(p, A):
    W = np.eye(2, dtype=complex)
    for (b, s) in p:
        U = su2(A[b])
        W = W @ (U if s > 0 else U.conj().T)
    return W


def T_exact(p1, p2, p3, A):
    W1, W2, W3 = holonomy(p1, A), holonomy(p2, A), holonomy(p3, A)
    return (0.5 * np.trace(W1 @ W2 @ W3) - 0.5 * np.trace(W1 @ W3 @ W2)).real


def phi_q(p, A):
    """Phi and Q for one path on a batch of fields A: (nsample, nb, 3)."""
    bs = np.array([b for b, _ in p])
    es = np.array([s for _, s in p], dtype=float)
    a = A[:, bs, :] * es[None, :, None]
    Phi = a.sum(axis=1)
    # Q = -(1/2) sum_{s<t} a_s x a_t; running sum
    run = np.cumsum(a, axis=1)
    prev = np.concatenate([np.zeros_like(a[:, :1, :]), run[:, :-1, :]], axis=1)
    Q = -0.5 * np.cross(prev, a).sum(axis=1)
    return Phi, Q


def main():
    out = {}
    for name, dims, nl in [("d3", (4, 4, 4), 60), ("d4", (4, 4, 4, 4), 54)]:
        rng = np.random.default_rng(20261101)
        idx = bonds_of(dims)
        o = tuple(0 for _ in dims)
        loops = lassos(dims, idx, o)
        rng.shuffle(loops)
        # keep distinct currents
        loops = loops[:nl]
        nb = len(idx)
        triples = list(itertools.combinations(range(len(loops)), 3))
        if len(triples) > 3000:
            sel = rng.choice(len(triples), 3000, replace=False)
            triples = [triples[i] for i in sel]
        ns = len(triples) + 400
        A = rng.normal(size=(ns, nb, 3))
        PQ = [phi_q(p, A) for p in loops]
        guard()
        t3 = np.empty((ns, len(triples)))
        t4 = np.empty((ns, len(triples)))
        for k, (i, j, l) in enumerate(triples):
            Pi, Qi = PQ[i]
            Pj, Qj = PQ[j]
            Pl, Ql = PQ[l]
            cr = np.cross(Pj, Pl)
            t3[:, k] = 0.25 * (Pi * cr).sum(1)
            t4[:, k] = 0.25 * ((Qi * cr).sum(1) + (Pi * np.cross(Qj, Pl)).sum(1) + (Pi * np.cross(Pj, Ql)).sum(1))
        guard()
        # jet check against the exact product at small amplitude
        errs = []
        for trial in range(6):
            i, j, l = triples[trial]
            eps = np.array([0.04, 0.02, 0.01])
            a0 = rng.normal(size=(nb, 3))
            vals = np.array([T_exact(loops[i], loops[j], loops[l], e * a0) for e in eps])
            P1, Q1 = phi_q(loops[i], a0[None])
            P2, Q2 = phi_q(loops[j], a0[None])
            P3, Q3 = phi_q(loops[l], a0[None])
            cr = np.cross(P2, P3)
            c3 = 0.25 * (P1 * cr).sum()
            c4 = 0.25 * ((Q1 * cr).sum() + (P1 * np.cross(Q2, P3)).sum() + (P1 * np.cross(P2, Q3)).sum())
            # fit e^3 c3 + e^4 c4 + e^5 c5 + e^6 c6 at three points: use c3 known, solve c4
            r = (vals[2] / eps[2] ** 3 - c3) / eps[2]
            errs.append(abs(r - c4) / max(abs(c4), 1e-12))
        s3 = np.linalg.svd(t3, compute_uv=False)
        U4, s4, Vt4 = np.linalg.svd(t4, full_matrices=True)
        tol = s4[0] * 1e-11
        rank4 = int((s4 > tol).sum())
        rank3 = int((s3 > s3[0] * 1e-11).sum())
        null = Vt4[rank4:].T
        if null.shape[1]:
            img = t3 @ null
            ratio = float(np.linalg.norm(img, 2) / s3[0])
        else:
            ratio = 0.0
        out[name] = dict(
            nb=nb,
            nloops=len(loops),
            ntriples=len(triples),
            nsamples=ns,
            rank_t3=rank3,
            rank_t4=rank4,
            null_dim=int(null.shape[1]),
            t3_on_null_over_top=ratio,
            jet_check_rel=[float(e) for e in errs],
        )
        print(name, out[name], flush=True)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "v0_jets.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
