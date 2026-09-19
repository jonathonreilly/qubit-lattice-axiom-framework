#!/usr/bin/env python3
"""J:note falsifier for SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03 (on main).

Falsifier implemented: "any fitted c_L is nonpositive or unresolved at the stated threshold" (seven reported standard errors), together
with "any Monte Carlo chain leaves its assigned sector", carried BEYOND the note's volumes L = 6, 8, 10, 12 to L = 14, 16, 20, with the
note's L = 8 and 12 recomputed as cross-checks.

Objects as defined by the parent (so that the numbers are comparable): links n(x, mu) in {0,1} on the L^3 torus, the three-of-six
Gauss constraint, the zero-flux background n(x, mu) = x_mu mod 2, the staggered field E = (-1)^(x+y+z) (n - 1/2) and its plane fluxes,
N_f = number of flippable (alternating) square plaquettes, the uniform RK measure within the initialized component, straight
noncontractible alternating flux lines. Independent machinery: a two-colour plaquette decomposition ((x_a + x_b) mod 2 per
orientation; the note's sampler uses four colours), flux lines placed on an evenly spread transverse lattice (the note walks
consecutive positions), a longer run at every volume (1000 thermal sweeps, 1000 samples two sweeps apart, 10 blocks), six signed-axis
chains per nonzero |Phi| and three zero-flux replicas, and an own weighted fit of the orbit means to a_L - c_L Phi^2 / L.
"""
from __future__ import annotations

import numpy as np

ORIENT = [(0, 1), (1, 2), (2, 0)]


def background(L):
    c = np.indices((L, L, L))
    occ = np.zeros((L, L, L, 3), dtype=np.uint8)
    for mu in range(3):
        occ[..., mu] = c[mu] % 2
    return occ


def degrees(occ):
    d = np.zeros(occ.shape[:3], dtype=np.int16)
    for mu in range(3):
        d += occ[..., mu]
        d += np.roll(occ[..., mu], 1, axis=mu)
    return d


def flux(occ):
    L = occ.shape[0]
    stag = (-1.0) ** np.indices((L, L, L)).sum(axis=0)
    E = stag[..., None] * (occ.astype(float) - 0.5)
    out = []
    for mu in range(3):
        sl = [slice(None)] * 3
        sl[mu] = 0
        out.append(int(round(float(E[tuple(sl) + (mu,)].sum()))))
    return tuple(out)


def flippable(occ, a, b):
    al = occ[..., a]
    bl = occ[..., b]
    ah = np.roll(al, -1, axis=b)      # a-link at r + b
    bh = np.roll(bl, -1, axis=a)      # b-link at r + a
    return (al == ah) & (bl == bh) & (al != bl)


def nf(occ):
    return int(sum(np.count_nonzero(flippable(occ, a, b)) for a, b in ORIENT))


def flip(occ, a, b, roots):
    r = roots.astype(np.uint8)
    occ[..., a] ^= r
    occ[..., a] ^= np.roll(r, 1, axis=b)
    occ[..., b] ^= r
    occ[..., b] ^= np.roll(r, 1, axis=a)


def insert_lines(L, axis, signed, offset):
    """straight noncontractible lines along `axis`; a line at transverse (s, t) changes the flux by (-1)^(s+t)."""
    occ = background(L)
    need, sign = abs(signed), (1 if signed > 0 else -1)
    tr = [i for i in range(3) if i != axis]
    cand = [(s, t) for s in range(L) for t in range(L) if (-1) ** (s + t) == sign]
    step = max(1, len(cand) // max(1, need))
    chosen = [cand[(offset + k * step) % len(cand)] for k in range(need)]
    assert len(set(chosen)) == need
    for s, t in chosen:
        sl = [slice(None)] * 3
        sl[tr[0]], sl[tr[1]] = s, t
        occ[tuple(sl) + (axis,)] ^= 1
    return occ


def chain(L, axis, signed, seed, therm=1000, samples=1000, stride=2, blocks=10):
    rng = np.random.default_rng(seed)
    occ = insert_lines(L, axis, signed, seed % 97)
    expect = tuple(signed if i == axis else 0 for i in range(3))
    start_ok = flux(occ) == expect and bool(np.all(degrees(occ) == 3))
    c = np.indices((L, L, L))
    colours = {(a, b): [((c[a] + c[b]) % 2) == k for k in (0, 1)] for a, b in ORIENT}

    def sweep():
        for oi in rng.permutation(3):
            a, b = ORIENT[oi]
            for k in rng.permutation(2):
                m = flippable(occ, a, b) & colours[(a, b)][k] & (rng.random((L, L, L)) < 0.5)
                flip(occ, a, b, m)

    for _ in range(therm):
        sweep()
    vals = []
    for _ in range(samples):
        for _ in range(stride):
            sweep()
        vals.append(nf(occ))
    v = np.array(vals, dtype=float)
    bm = v.reshape(blocks, -1).mean(axis=1)
    ok = start_ok and flux(occ) == expect and bool(np.all(degrees(occ) == 3))
    return bm, ok


def orbit(L, phi):
    specs = [(0, 0, rep) for rep in range(3)] if phi == 0 else [(ax, s * phi, 0) for ax in range(3) for s in (-1, 1)]
    blocks, ok, means = [], True, []
    for ax, sgn, rep in specs:
        seed = 7_000_000 + 1000 * L + 37 * phi + 11 * ax + (1 if sgn > 0 else 0) + 5 * rep
        bm, good = chain(L, ax, sgn, seed)
        blocks.extend(bm)
        means.append(bm.mean())
        ok &= good
    b = np.array(blocks)
    return b.mean(), b.std(ddof=1) / np.sqrt(len(b)), ok, float(np.ptp(means))


def fit(L, rows):
    x = np.array([p * p / L for p, _, _ in rows])
    y = np.array([m for _, m, _ in rows])
    e = np.array([s for _, _, s in rows])
    A = np.column_stack([np.ones_like(x), x])
    W = 1 / e ** 2
    cov = np.linalg.inv(A.T @ (W[:, None] * A))
    coef = cov @ (A.T @ (W * y))
    return -coef[1], float(np.sqrt(cov[1, 1]))


def main():
    note = {8: (1.884728, 0.151700), 12: (1.260166, 0.173252)}
    res, all_ok = {}, True
    for L in (8, 12, 14, 16, 20):
        rows = []
        for phi in range(L // 2 + 1):
            m, s, ok, spread = orbit(L, phi)
            rows.append((phi, m, s))
            all_ok &= ok
        c, ce = fit(L, rows)
        res[L] = (c, ce, rows)
        cmp = f"; note c = {note[L][0]:.4f} +- {note[L][1]:.4f} (difference {abs(c - note[L][0]) / np.hypot(ce, note[L][1]):.1f} combined sigma)" if L in note else ""
        print(f"L = {L}: orbit means " + ", ".join(f"{m:.2f}" for _, m, _ in rows) + f"; c_L = {c:.4f} +- {ce:.4f} ({c / ce:.1f} sigma){cmp}")
    beyond = {L: res[L] for L in (14, 16, 20)}
    fails = [L for L, (c, ce, _) in beyond.items() if not (c > 0 and c / ce > 7)]
    print(f"sector preservation (Gauss degrees 3 everywhere, assigned flux) in all chains: {all_ok}")
    if fails or not all_ok:
        print(f"HIT: beyond the note's volumes the fitted coefficient is nonpositive or not resolved at seven standard errors at L = {fails} "
              f"(or a chain left its sector: {not all_ok}); values " + ", ".join(f"L={L}: {res[L][0]:.3f} +- {res[L][1]:.3f}" for L in fails))
    print("SUMMARY: with an independent two-colour sampler and flux-line placement, " + "; ".join(
        f"c_{L} = {c:.3f} +- {ce:.3f} ({c / ce:.1f} sigma)" for L, (c, ce, _) in res.items())
        + f"; every chain kept its Gauss charges and flux ({all_ok}); beyond the note (L = 14, 16, 20) the falsifier "
        + ("does not fire" if not fails else f"fires at L = {fails}"))


if __name__ == "__main__":
    main()
