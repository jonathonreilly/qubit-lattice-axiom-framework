"""Probe: does the Benincasa-Dowker action rescue order-reversal positivity?

Follow-up to probe_axiom_reset_order_reversal_positivity_2026_08_09.py, which
found that no non-degenerate member of a two-parameter order-local quadratic
family satisfies positivity on sprinkled causal sets. That probe named three
ways the negative could still be wrong:

  (E1) the causal-set literature's natural action - the Benincasa-Dowker
       discrete d'Alembertian - lies outside the scanned family;
  (E2) the systems were small, so the violation could be a finite-size effect;
  (E3) the mirrored-sprinkling construction could itself be atypical.

(E3) is attacked by interpolation: jitter a regular causal set continuously
toward a sprinkled one and locate where positivity breaks. If it breaks at any
nonzero irregularity, the obstruction is about irregularity itself rather than
about one construction.

Everything is measured. Nothing is assumed to pass.
"""

import numpy as np

RESULTS = []
rng = np.random.default_rng(20260809)


def check(label, ok, detail=""):
    RESULTS.append((label, bool(ok), detail))


def min_eig_hermitian(M):
    M = 0.5 * (M + M.T)
    return float(np.linalg.eigvalsh(M).min())


def causal_from_points(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dx = np.abs(P[None, :, 1] - P[:, None, 1])
    return dt >= dx


def mirrored(fut):
    """Future-half points + their time mirror; theta is order-reversing."""
    past = np.column_stack([-fut[:, 0], fut[:, 1]])
    P = np.vstack([fut, past])
    k = len(fut)
    theta = np.concatenate([np.arange(k, 2 * k), np.arange(0, k)])
    return P, causal_from_points(P), theta, np.arange(k)


def sprinkled_future(n, rng, tmin=0.05):
    pts = []
    while len(pts) < n:
        t, x = rng.uniform(0, 1), rng.uniform(-1, 1)
        if abs(x) + t <= 1.0 and t > tmin:
            pts.append((t, x))
    return np.array(pts)


def bd_operator(R):
    """2D Benincasa-Dowker discrete d'Alembertian from the order alone.

    B phi(x) = -phi(x) + 2( sum_{L1} phi - 2 sum_{L2} phi + sum_{L3} phi ),
    where L_k(x) are the ancestors of x with k-1 elements strictly between.
    Overall normalisation is irrelevant to positivity and is dropped.
    """
    n = R.shape[0]
    S = R & ~np.eye(n, dtype=bool)
    between = S.astype(np.int32) @ S.astype(np.int32)      # |{z : y < z < x}|
    L1 = S & (between == 0)
    L2 = S & (between == 1)
    L3 = S & (between == 2)
    return -np.eye(n) + 2.0 * (L1.T.astype(float)
                               - 2.0 * L2.T.astype(float)
                               + L3.T.astype(float))


def positivity_from_kernel(K, theta, future, tol=1e-9):
    """Return (min eigenvalue, ||M||_F) or None if K is unusable."""
    if not np.allclose(K[np.ix_(theta, theta)], K, atol=1e-9):
        return None                                  # theta not a symmetry
    if np.linalg.eigvalsh(0.5 * (K + K.T)).min() <= tol:
        return None                                  # action not positive-definite
    G = np.linalg.inv(K)
    M = G[np.ix_(theta[future], future)]
    nrm = float(np.linalg.norm(M))
    if nrm < 1e-12:
        return None                                  # degenerate zero Gram matrix
    return min_eig_hermitian(M), nrm


# ---------------------------------------------------------------------------
# (E1) the Benincasa-Dowker action
# ---------------------------------------------------------------------------

def probe_bd_action(n_future=14, n_sets=10):
    masses = [0.5, 1.0, 2.0, 4.0, 8.0]
    rows, any_pass = [], False
    sym_fail = 0
    for m2 in masses:
        vals, mags, skipped = [], [], 0
        for _ in range(n_sets):
            P, R, theta, future = mirrored(sprinkled_future(n_future, rng))
            B = bd_operator(R)
            Bsym = 0.5 * (B + B.T)
            K = -Bsym + m2 * np.eye(len(P))
            out = positivity_from_kernel(K, theta, future)
            if out is None:
                skipped += 1
                continue
            vals.append(out[0])
            mags.append(out[1])
        if not vals:
            sym_fail += 1
            rows.append(f"m^2={m2}: no usable kernel ({skipped} skipped)")
            continue
        n_pos = sum(1 for v in vals if v > -1e-10)
        if n_pos == len(vals):
            any_pass = True
        rows.append(f"m^2={m2}: {n_pos}/{len(vals)} positive, "
                    f"worst min eig {min(vals):.3e}, mean ||M||_F {np.mean(mags):.3e}"
                    + (f", {skipped} skipped" if skipped else ""))

    check("(E1) Benincasa-Dowker action restores order-reversal positivity",
          any_pass,
          "; ".join(rows))


def probe_bd_on_regular(Lt=5, Lx=6):
    """Does BD at least behave like the order-local family on a REGULAR order?"""
    fut = np.array([(float(t), float(x))
                    for t in range(1, Lt + 1) for x in range(-Lx, Lx + 1)])
    P, R, theta, future = mirrored(fut)
    B = bd_operator(R)
    Bsym = 0.5 * (B + B.T)
    rows, all_pos = [], True
    for m2 in (1.0, 4.0, 16.0):
        out = positivity_from_kernel(-Bsym + m2 * np.eye(len(P)), theta, future)
        if out is None:
            rows.append(f"m^2={m2}: unusable kernel")
            all_pos = False
            continue
        rows.append(f"m^2={m2}: min eig {out[0]:.3e}, ||M||_F {out[1]:.3e}")
        if out[0] <= -1e-10:
            all_pos = False
    check("(E1b) Benincasa-Dowker action is positive on a REGULAR causal order",
          all_pos, f"{len(P)} events; " + "; ".join(rows))


# ---------------------------------------------------------------------------
# (E2) is the violation a finite-size effect?
# ---------------------------------------------------------------------------

def probe_finite_size(sizes=(6, 9, 12, 16, 20, 25), n_sets=8, lam=0.2):
    rows, ratios = [], []
    for n_future in sizes:
        norm_viol = []
        for _ in range(n_sets):
            P, R, theta, future = mirrored(sprinkled_future(n_future, rng))
            S = R & ~np.eye(len(P), dtype=bool)
            two = S.astype(np.int16) @ S.astype(np.int16) > 0
            A = (S & ~two).astype(float)
            Asym = A + A.T
            deg = max(Asym.sum(axis=1).max(), 1.0)
            out = positivity_from_kernel(np.eye(len(P)) - (lam / deg) * Asym,
                                         theta, future)
            if out is None:
                continue
            norm_viol.append(-out[0] / out[1])       # violation relative to scale
        mean_v = float(np.mean(norm_viol))
        ratios.append(mean_v)
        rows.append(f"N={2*n_future}: mean -min_eig/||M||_F = {mean_v:.4f}")

    trend = float(np.polyfit(np.log([2 * s for s in sizes]), np.log(ratios), 1)[0])
    shrinking = trend < -0.5 and ratios[-1] < 0.25 * ratios[0]
    check("(E2) the positivity violation is a finite-size effect that vanishes",
          shrinking,
          "; ".join(rows) + f"; log-log slope vs N = {trend:+.3f} "
          f"(a strongly negative slope would mean it washes out)")


# ---------------------------------------------------------------------------
# (E3) interpolate regular -> sprinkled
# ---------------------------------------------------------------------------

def probe_regularity_interpolation(Lt=4, Lx=5, n_sets=8, lam=0.2):
    base = np.array([(float(t), float(x))
                     for t in range(1, Lt + 1) for x in range(-Lx, Lx + 1)])
    rows, first_break = [], None
    for eps in (0.0, 0.02, 0.05, 0.10, 0.20, 0.35, 0.50):
        vals = []
        trials = 1 if eps == 0.0 else n_sets
        for _ in range(trials):
            fut = base + rng.uniform(-eps, eps, size=base.shape)
            P, R, theta, future = mirrored(fut)
            S = R & ~np.eye(len(P), dtype=bool)
            two = S.astype(np.int16) @ S.astype(np.int16) > 0
            A = (S & ~two).astype(float)
            Asym = A + A.T
            deg = max(Asym.sum(axis=1).max(), 1.0)
            out = positivity_from_kernel(np.eye(len(P)) - (lam / deg) * Asym,
                                         theta, future)
            if out is not None:
                vals.append(-out[0] / out[1])
        worst = max(vals) if vals else float("nan")
        rows.append(f"jitter={eps}: worst -min_eig/||M||_F = {worst:.4f}")
        if first_break is None and worst > 1e-6:
            first_break = eps

    check("(E3) positivity survives some nonzero irregularity",
          first_break is None or first_break > 0.10,
          "; ".join(rows) +
          (f"; first violation at jitter = {first_break}" if first_break is not None
           else "; no violation observed"))


def main():
    probe_bd_action()
    probe_bd_on_regular()
    probe_finite_size()
    probe_regularity_interpolation()

    passed = sum(1 for _l, ok, _d in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok, detail in RESULTS:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" ({detail})" if detail else ""))
    print("=" * 76)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
