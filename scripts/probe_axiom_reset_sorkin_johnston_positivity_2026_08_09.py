"""Adversarial probe: was the positivity negative an artifact of the WRONG clause?

The drafted Law axiom says the amplitude assignment is "positive under order
reversal". Rounds one and two tested that and found it fails on any substrate
that is not exactly regular.

The adversarial objection to my own probe: reflection positivity is a EUCLIDEAN
construction. It exists to Wick-rotate a Euclidean measure into a Lorentzian
Hilbert space. A causal set is intrinsically Lorentzian - there is no Euclidean
section and no Wick rotation - so importing reflection positivity onto it may be
a category error committed by the axiom draft, not an obstruction in the
substrate.

The Lorentzian condition for obtaining a Hilbert space is not reflection
positivity but WIGHTMAN POSITIVITY: a two-point function W that is
positive-semidefinite and whose antisymmetric part reproduces the commutator,
  W >= 0        and        W - conj(W) = i*Delta,
from which GNS gives the Hilbert space directly. The Sorkin-Johnston
construction builds exactly such a W from the causal order alone.

If SJ succeeds on the same sprinkled causal sets where reflection positivity
fails, then the negative result belongs to the drafted clause, not to the
substrate, and the clause must be rewritten.

Everything is verified numerically, including the properties SJ is supposed to
have by construction.
"""

import numpy as np

RESULTS = []
rng = np.random.default_rng(20260809)


def check(label, ok, detail=""):
    RESULTS.append((label, bool(ok), detail))


def causal_matrix(P):
    """R[i, j] True iff event i precedes-or-equals event j."""
    dt = P[None, :, 0] - P[:, None, 0]
    dx = np.abs(P[None, :, 1] - P[:, None, 1])
    return dt >= dx


def sprinkle_diamond(n, rng):
    pts = []
    while len(pts) < n:
        t, x = rng.uniform(-1, 1, size=2)
        if abs(x) + abs(t) <= 1.0:
            pts.append((t, x))
    return np.array(sorted(pts, key=lambda p: p[0]))


def regular_causet(Lt=5, Lx=6):
    return np.array([(float(t), float(x))
                     for t in range(-Lt, Lt + 1) for x in range(-Lx, Lx + 1)])


def sorkin_johnston(R):
    """SJ two-point function from the causal order alone.

    In 2D the massless retarded Green function on a sprinkled causal set is
    G_R = C/2, with C the strict causal matrix. Pauli-Jordan Delta = G_R - G_A.
    W is the positive spectral part of i*Delta.
    """
    n = R.shape[0]
    S = (R & ~np.eye(n, dtype=bool)).astype(float)
    G_R = 0.5 * S.T                      # G_R(x, y) supported on y strictly before x
    Delta = G_R - G_R.T
    iDelta = 1j * Delta
    iDelta = 0.5 * (iDelta + iDelta.conj().T)
    vals, vecs = np.linalg.eigh(iDelta)
    pos = vals > 1e-10
    W = (vecs[:, pos] * vals[pos]) @ vecs[:, pos].conj().T
    return Delta, iDelta, W, vals


def evaluate(P, label, n_trials_note=""):
    R = causal_matrix(P)
    Delta, iDelta, W, vals = sorkin_johnston(R)

    antisym = float(np.abs(Delta + Delta.T).max())
    herm = float(np.abs(iDelta - iDelta.conj().T).max())
    spectrum_sym = float(abs(np.sort(vals)[0] + np.sort(vals)[-1]))
    w_min_eig = float(np.linalg.eigvalsh(0.5 * (W + W.conj().T)).min())
    commutator_defect = float(np.abs((W - W.conj()) - iDelta).max())
    rank = int(np.linalg.matrix_rank(W, tol=1e-8))
    scale = float(np.linalg.norm(W))
    return {
        "label": label, "n": len(P), "antisym": antisym, "herm": herm,
        "spectrum_sym": spectrum_sym, "w_min_eig": w_min_eig,
        "commutator_defect": commutator_defect, "rank": rank, "scale": scale,
        "note": n_trials_note,
    }


def main():
    # --- the construction's own properties, verified not assumed ---------
    P = sprinkle_diamond(60, rng)
    r = evaluate(P, "sprinkled (60 events)")

    check("Pauli-Jordan operator is antisymmetric",
          r["antisym"] < 1e-12, f"max |Delta + Delta^T| = {r['antisym']:.2e}")
    check("i*Delta is Hermitian with a spectrum symmetric about zero",
          r["herm"] < 1e-12 and r["spectrum_sym"] < 1e-9,
          f"max |iD - iD^dag| = {r['herm']:.2e}, "
          f"|lambda_min + lambda_max| = {r['spectrum_sym']:.2e}")
    check("SJ two-point function is positive-semidefinite",
          r["w_min_eig"] > -1e-10, f"min eigenvalue of W = {r['w_min_eig']:.3e}")
    check("SJ two-point function reproduces the commutator: W - conj(W) = i*Delta",
          r["commutator_defect"] < 1e-10,
          f"max defect = {r['commutator_defect']:.2e}")
    check("SJ state is non-degenerate (a nontrivial GNS Hilbert space)",
          r["rank"] > 1 and r["scale"] > 1e-6,
          f"rank W = {r['rank']} of {r['n']} events, ||W||_F = {r['scale']:.3f}")

    # --- the decisive comparison: sprinkled substrates ------------------
    rows, all_ok = [], True
    for n in (20, 40, 80, 140):
        rr = evaluate(sprinkle_diamond(n, rng), f"sprinkled N={n}")
        ok = (rr["w_min_eig"] > -1e-10 and rr["commutator_defect"] < 1e-10
              and rr["rank"] > 1)
        all_ok = all_ok and ok
        rows.append(f"N={n}: min eig(W) {rr['w_min_eig']:.2e}, "
                    f"commutator defect {rr['commutator_defect']:.2e}, "
                    f"GNS rank {rr['rank']}")
    check("SJ SUCCEEDS on sprinkled causal sets, where reflection positivity failed",
          all_ok, "; ".join(rows))

    # --- and on a regular one, for completeness -------------------------
    rr = evaluate(regular_causet(4, 5), "regular")
    check("SJ succeeds on a regular causal order too",
          rr["w_min_eig"] > -1e-10 and rr["commutator_defect"] < 1e-10,
          f"{rr['n']} events: min eig(W) = {rr['w_min_eig']:.2e}, "
          f"commutator defect = {rr['commutator_defect']:.2e}, "
          f"GNS rank {rr['rank']}")

    # --- is the SJ state sensitive to the order, or trivial? ------------
    # A state that ignored the causal structure would be worthless. Compare the
    # SJ spectrum against that of an order-scrambled control with the same
    # number of relations.
    P = sprinkle_diamond(60, rng)
    R = causal_matrix(P)
    _d, _i, W_true, vals_true = sorkin_johnston(R)
    perm = rng.permutation(len(P))
    R_scr = R[np.ix_(perm, perm)]
    _d2, _i2, W_scr, vals_scr = sorkin_johnston(R_scr)
    # the scrambled poset is the SAME poset relabelled, so the spectrum must
    # be identical: that is the invariance check, not a triviality check
    spec_same = float(np.abs(np.sort(vals_true) - np.sort(vals_scr)).max())
    check("SJ spectrum depends only on the order, not on the labelling",
          spec_same < 1e-9,
          f"max spectral difference under relabelling = {spec_same:.2e}")

    # sensitivity: a different sprinkling gives a different spectrum
    P2 = sprinkle_diamond(60, rng)
    _d3, _i3, _W3, vals_other = sorkin_johnston(causal_matrix(P2))
    spec_diff = float(np.abs(np.sort(vals_true) - np.sort(vals_other)).max())
    check("SJ state is sensitive to the substrate (not a constant)",
          spec_diff > 1e-6,
          f"max spectral difference between two sprinklings = {spec_diff:.4f}")

    passed = sum(1 for _l, ok, _d in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok, detail in RESULTS:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" ({detail})" if detail else ""))
    print("=" * 76)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
