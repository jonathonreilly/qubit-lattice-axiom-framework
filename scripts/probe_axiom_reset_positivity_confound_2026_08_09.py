"""Probe: is the positivity failure about IRREGULARITY, or about the INTERFACE?

The earlier probes reported "order-reversal positivity holds on a regular causal
order and fails on a sprinkled one", and that finding drove the headline
conclusion that the reset cannot have both Lorentz invariance and a Hilbert
space. But the two cases were built differently:

  - the regular test used a causal set CONTAINING a t = 0 layer, with the
    positive half taken to be t > 0, so the interface sits between the halves;
  - the sprinkled test used a mirrored construction with NO t = 0 layer, so the
    two halves are linked directly across the reflection surface.

Regularity and interface presence were therefore varied together. This probe
separates them with a 2x2: {regular, sprinkled} x {interface, no interface},
one construction, one action, one test.

If the interface is the live variable, the earlier headline conclusion is wrong
and must be withdrawn.
"""

import numpy as np

RESULTS = []
rng = np.random.default_rng(20260809)


def check(label, ok, detail=""):
    RESULTS.append((label, bool(ok), detail))


def causal_from_points(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dx = np.abs(P[None, :, 1] - P[:, None, 1])
    return dt >= dx


def build(fut, interface_x):
    """future half + time mirror + optional t=0 interface layer.

    theta swaps future with past and fixes the interface pointwise.
    """
    past = np.column_stack([-fut[:, 0], fut[:, 1]])
    k = len(fut)
    if interface_x is None or len(interface_x) == 0:
        P = np.vstack([fut, past])
        theta = np.concatenate([np.arange(k, 2 * k), np.arange(0, k)])
    else:
        iface = np.column_stack([np.zeros(len(interface_x)), interface_x])
        P = np.vstack([fut, past, iface])
        theta = np.concatenate([np.arange(k, 2 * k), np.arange(0, k),
                                np.arange(2 * k, 2 * k + len(iface))])
    return P, causal_from_points(P), theta, np.arange(k)


def link_action(R, lam=0.2):
    n = R.shape[0]
    S = R & ~np.eye(n, dtype=bool)
    two = S.astype(np.int16) @ S.astype(np.int16) > 0
    A = (S & ~two).astype(float)
    Asym = A + A.T
    deg = max(Asym.sum(axis=1).max(), 1.0)
    return np.eye(n) - (lam / deg) * Asym


def bd_action(R, m2):
    """2D Benincasa-Dowker d'Alembertian, symmetrised, plus a mass term."""
    n = R.shape[0]
    S = R & ~np.eye(n, dtype=bool)
    between = S.astype(np.int32) @ S.astype(np.int32)
    L1 = S & (between == 0)
    L2 = S & (between == 1)
    L3 = S & (between == 2)
    B = -np.eye(n) + 2.0 * (L1.T.astype(float) - 2.0 * L2.T.astype(float)
                            + L3.T.astype(float))
    return -0.5 * (B + B.T) + m2 * np.eye(n)


def positivity(K, theta, future):
    if not np.allclose(K[np.ix_(theta, theta)], K, atol=1e-9):
        return None, "theta not a symmetry of the action"
    if np.linalg.eigvalsh(0.5 * (K + K.T)).min() <= 1e-9:
        return None, "action not positive-definite"
    G = np.linalg.inv(K)
    M = G[np.ix_(theta[future], future)]
    nrm = float(np.linalg.norm(M))
    if nrm < 1e-12:
        return None, "degenerate zero Gram matrix"
    ev = np.linalg.eigvalsh(0.5 * (M + M.T))
    return (float(ev.min()), nrm), ""


def regular_future(Lt=4, Lx=5):
    return np.array([(float(t), float(x))
                     for t in range(1, Lt + 1) for x in range(-Lx, Lx + 1)])


def sprinkled_future(n, rng, tmin=0.05):
    pts = []
    while len(pts) < n:
        t, x = rng.uniform(0, 1), rng.uniform(-1, 1)
        if abs(x) + t <= 1.0 and t > tmin:
            pts.append((t, x))
    return np.array(pts)


def run_cell(label, make_fut, make_iface, n_trials, action=None):
    viols, notes = [], set()
    for _ in range(n_trials):
        fut = make_fut()
        P, R, theta, future = build(fut, make_iface())
        if not np.array_equal(R[np.ix_(theta, theta)], R.T):
            notes.add("theta failed to reverse the order")
            continue
        K = link_action(R) if action is None else action(R)
        out, why = positivity(K, theta, future)
        if out is None:
            notes.add(why)
            continue
        viols.append(-out[0] / out[1])
    if not viols:
        return None, f"{label}: no usable trial ({'; '.join(sorted(notes))})"
    worst = max(viols)
    ok = worst <= 1e-8
    return ok, (f"{label}: worst -min_eig/||M||_F = {worst:.4f} over "
                f"{len(viols)} trials" + (f" [{'; '.join(sorted(notes))}]" if notes else ""))


def main():
    Lx = 5
    iface_reg = np.array([float(x) for x in range(-Lx, Lx + 1)])

    cells = {}
    cells["regular + interface"] = run_cell(
        "regular + interface", lambda: regular_future(4, Lx), lambda: iface_reg, 1)
    cells["regular, no interface"] = run_cell(
        "regular, no interface", lambda: regular_future(4, Lx), lambda: None, 1)
    cells["sprinkled + interface"] = run_cell(
        "sprinkled + interface", lambda: sprinkled_future(14, rng),
        lambda: np.sort(rng.uniform(-1, 1, size=11)), 10)
    cells["sprinkled, no interface"] = run_cell(
        "sprinkled, no interface", lambda: sprinkled_future(14, rng),
        lambda: None, 10)

    for name, (ok, detail) in cells.items():
        check(f"positivity holds: {name}", bool(ok), detail)

    # Complete the matrix with the Benincasa-Dowker action, which the previous
    # probe tested only without an interface. Sweep the mass until the kernel
    # is usable, so a failure is not merely "action not positive-definite".
    for m2 in (4.0, 16.0, 64.0, 256.0):
        act = lambda R, _m=m2: bd_action(R, _m)
        bd_reg = run_cell(f"BD m^2={m2} regular + interface",
                          lambda: regular_future(4, Lx), lambda: iface_reg, 1, act)
        bd_spr = run_cell(f"BD m^2={m2} sprinkled + interface",
                          lambda: sprinkled_future(14, rng),
                          lambda: np.sort(rng.uniform(-1, 1, size=11)), 6, act)
        if bd_reg[0] is not None and bd_spr[0] is not None:
            check(f"BD action, regular + interface (m^2={m2})", bool(bd_reg[0]), bd_reg[1])
            check(f"BD action, sprinkled + interface (m^2={m2})", bool(bd_spr[0]), bd_spr[1])
            break
    else:
        check("BD action: no usable kernel at any tested mass", False,
              "swept m^2 in {4, 16, 64, 256}")

    # The one passing cell is regular + interface. Does positivity survive a
    # NEIGHBOURHOOD of regularity? Lorentz invariance needs full Poisson
    # randomness, so if positivity breaks at infinitesimal jitter the
    # obstruction is sharp. Interface points stay at t=0 so theta stays exact.
    base = regular_future(4, Lx)
    rows, first_break = [], None
    for eps in (0.0, 0.001, 0.005, 0.02, 0.05, 0.15, 0.40):
        worst = 0.0
        for _ in range(1 if eps == 0.0 else 6):
            fut = base + rng.uniform(-eps, eps, size=base.shape)
            P, R, theta, future = build(fut, iface_reg)
            if not np.array_equal(R[np.ix_(theta, theta)], R.T):
                continue
            out, _why = positivity(link_action(R), theta, future)
            if out is not None:
                worst = max(worst, -out[0] / out[1])
        rows.append(f"jitter={eps}: worst {worst:.4f}")
        if first_break is None and worst > 1e-8:
            first_break = eps
    check("positivity survives a neighbourhood of regularity (interface present)",
          first_break is None or first_break > 0.02,
          "; ".join(rows) + (f"; breaks at jitter={first_break}"
                             if first_break is not None else "; never breaks"))

    reg_i = cells["regular + interface"][0]
    reg_n = cells["regular, no interface"][0]
    spr_i = cells["sprinkled + interface"][0]
    spr_n = cells["sprinkled, no interface"][0]

    interface_is_the_variable = (reg_i and spr_i) and not (reg_n or spr_n)
    regularity_is_the_variable = (reg_i and reg_n) and not (spr_i or spr_n)

    check("DIAGNOSIS: the live variable is the INTERFACE, not regularity",
          bool(interface_is_the_variable),
          f"regular+interface={reg_i}, sprinkled+interface={spr_i}, "
          f"regular-no-interface={reg_n}, sprinkled-no-interface={spr_n}")
    check("DIAGNOSIS: the live variable is REGULARITY, not the interface",
          bool(regularity_is_the_variable),
          "this is the reading the earlier probe reported; it is contradicted "
          "if the row above passes")

    passed = sum(1 for _l, ok, _d in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok, detail in RESULTS:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" ({detail})" if detail else ""))
    print("=" * 76)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
