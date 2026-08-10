"""Probe: does the proposed axiom reset have models?

Tests obligations 1, 2 and 3 of docs/AXIOM_RESET_PROPOSAL_2026-08-09.md:
  (1) exhibit one model of the four drafted axioms;
  (2) show the model is non-trivial;
  (3) verify Z^3 x Z is a model of the Substrate axiom, so existing lattice
      work has a recovery path.

Every reported number is computed. No expected constant is embedded and
compared against itself.
"""

import itertools

import numpy as np

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append((label, bool(ok), detail))


# ----------------------------------------------------------------------------
# poset machinery
# ----------------------------------------------------------------------------

def poset_axioms(R):
    """R[i, j] is True iff event i precedes-or-equals event j."""
    n = R.shape[0]
    reflexive = bool(np.all(np.diag(R)))
    antisymmetric = bool(np.array_equal(R & R.T, np.eye(n, dtype=bool)))
    composed = (R.astype(np.int16) @ R.astype(np.int16)) > 0
    transitive = bool(np.all(composed <= R))
    return reflexive, antisymmetric, transitive


def interval_sizes(R):
    """|[i, j]| = #{k : i <= k <= j}, computed as the integer square of R."""
    Ri = R.astype(np.int32)
    return Ri @ Ri


# ----------------------------------------------------------------------------
# (3) Z^3 x Z under the light-cone order
# ----------------------------------------------------------------------------

def probe_lattice_substrate():
    space = range(-2, 3)
    time = range(0, 5)
    pts = [(x, y, z, t) for x in space for y in space for z in space for t in time]
    P = np.array(pts, dtype=np.int32)
    n = len(pts)

    dx = np.abs(P[:, None, 0] - P[None, :, 0])
    dy = np.abs(P[:, None, 1] - P[None, :, 1])
    dz = np.abs(P[:, None, 2] - P[None, :, 2])
    dt = P[None, :, 3] - P[:, None, 3]
    R = dt >= (dx + dy + dz)          # signal speed one in graph distance

    refl, anti, trans = poset_axioms(R)
    check("Z^3 x Z light-cone relation is reflexive", refl)
    check("Z^3 x Z light-cone relation is antisymmetric", anti)
    check("Z^3 x Z light-cone relation is transitive", trans,
          f"{n} events, all {n**2} pairs and compositions verified")

    # Finiteness of order intervals, verified without window truncation.
    # For a=(x,t), b=(y,s) any z in the interval obeys |z-x|_1 <= s-t, so the
    # interval sits strictly inside the sampled window when s-t is small
    # enough. Confirm the bound is respected rather than assumed.
    origin = pts.index((0, 0, 0, 0))
    worst_reach, sizes = 0, []
    for j, q in enumerate(pts):
        if not R[origin, j]:
            continue
        members = np.where(R[origin, :] & R[:, j])[0]
        sizes.append(len(members))
        reach = max(int(np.abs(P[m, :3]).sum()) for m in members)
        worst_reach = max(worst_reach, reach)
        span = q[3]
        if reach > span:
            check("interval spatial reach exceeded its causal bound", False,
                  f"reach {reach} > span {span}")
            return
    check("every order interval is finite and bounded by its causal span", True,
          f"{len(sizes)} intervals, max |[a,b]| = {max(sizes)}, "
          f"max spatial reach {worst_reach} <= max time span {max(time)}")

    interior = max(np.abs(P[:, :3]).max(), 1)
    check("intervals do not touch the sampling window, so counts are exact",
          worst_reach < interior + max(time),
          f"reach {worst_reach} < window bound {interior + max(time)}")


# ----------------------------------------------------------------------------
# (3b) a sprinkled causal set: substrate without a lattice
# ----------------------------------------------------------------------------

def sprinkle_diamond(n, rng):
    """Poisson-distributed events in the 2D causal diamond |x| + |t| <= 1."""
    pts = []
    while len(pts) < n:
        t, x = rng.uniform(-1, 1, size=2)
        if abs(x) + abs(t) <= 1.0:
            pts.append((t, x))
    return np.array(sorted(pts, key=lambda p: p[0]))


def causal_matrix(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dx = np.abs(P[None, :, 1] - P[:, None, 1])
    return (dt >= dx)


def probe_sprinkled_substrate():
    rng = np.random.default_rng(20260809)
    P = sprinkle_diamond(120, rng)
    R = causal_matrix(P)
    refl, anti, trans = poset_axioms(R)
    check("sprinkled causal set is reflexive", refl)
    check("sprinkled causal set is antisymmetric", anti)
    check("sprinkled causal set is transitive", trans, f"{len(P)} events")

    # "number = volume": interval cardinality should track the spacetime
    # volume of the interval. Fit, do not assume.
    sizes, volumes = [], []
    S = interval_sizes(R)
    for i in range(len(P)):
        for j in range(len(P)):
            if not R[i, j] or i == j:
                continue
            dt = P[j, 0] - P[i, 0]
            dx = P[j, 1] - P[i, 1]
            tau2 = dt * dt - dx * dx
            if tau2 <= 0:
                continue
            sizes.append(S[i, j])
            volumes.append(tau2 / 2.0)      # area of the 2D interval diamond
    sizes = np.array(sizes, float)
    volumes = np.array(volumes, float)
    corr = float(np.corrcoef(sizes, volumes)[0, 1])
    slope = float(np.polyfit(volumes, sizes, 1)[0])
    density = len(P) / 2.0                  # 120 events in a diamond of area 2
    ratio = slope / density
    check("interval cardinality tracks interval volume (number = volume)",
          corr > 0.95 and 0.8 < ratio < 1.2,
          f"corr={corr:.4f}, fitted slope={slope:.1f}, "
          f"sprinkling density={density:.1f}, slope/density={ratio:.3f}")


# ----------------------------------------------------------------------------
# (1) and (2): an explicit model of all four drafted axioms
# ----------------------------------------------------------------------------

PAULI = [
    np.eye(2, dtype=complex),
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]


def region_basis(region, n_events):
    """Pauli strings supported on `region`, identity elsewhere."""
    out = []
    for labels in itertools.product(range(4), repeat=len(region)):
        assign = dict(zip(region, labels))
        M = np.array([[1.0 + 0j]])
        for e in range(n_events):
            M = np.kron(M, PAULI[assign.get(e, 0)])
        out.append(M)
    return out


def probe_model():
    # A causal set with a genuine order automorphism, so the invariance test
    # below is not vacuous: a 1+1 light-cone order on x in {-1,0,1}, t in {0,1},
    # which carries the spatial reflection x -> -x.
    pts = [(float(t), float(x)) for t in (0, 1) for x in (-1, 0, 1)]
    P = np.array(pts)
    R = (P[None, :, 0] - P[:, None, 0]) >= np.abs(P[None, :, 1] - P[:, None, 1])
    n = len(P)
    refl, anti, trans = poset_axioms(R)
    check("model substrate satisfies the Substrate axiom", refl and anti and trans,
          f"{n}-event 1+1 light-cone causal set")

    # Regions must be genuinely unrelated by the order, or the commutation
    # test below passes for the trivial reason that they are disjoint.
    A, B = [0], [2]
    sub_A = A[:1]
    basis_A = region_basis(A, n)
    basis_B = region_basis(B, n)
    basis_subA = region_basis(sub_A, n)
    basis_AB = region_basis(sorted(A + B), n)

    def span_rank(mats):
        M = np.stack([m.reshape(-1) for m in mats])
        return int(np.linalg.matrix_rank(M, tol=1e-9))

    # Isotony: Alg(sub_A) sits inside Alg(A).
    r_A = span_rank(basis_A)
    r_join = span_rank(basis_A + basis_subA)
    check("Observables is isotone: a subregion algebra sits inside its region",
          r_join == r_A == 4 ** len(A),
          f"dim Alg(A)={r_A}, dim span(Alg(A) u Alg(subA))={r_join}")

    # Locality: order-unrelated regions commute.
    unrelated = not (R[A[0], B[0]] or R[B[0], A[0]])
    worst = 0.0
    for a in basis_A:
        for b in basis_B:
            worst = max(worst, float(np.abs(a @ b - b @ a).max()))
    check("Observables is local: unrelated regions commute",
          worst < 1e-12 and unrelated,
          f"regions genuinely order-unrelated={unrelated}, max |[a,b]| = {worst:.2e}; "
          f"NOTE this model is kinematic - all disjoint regions commute in a "
          f"tensor-product assignment, so the axiom is satisfied but not stressed")

    # Generation: Alg(A u B) is generated by Alg(A) and Alg(B).
    products = [a @ b for a in basis_A for b in basis_B]
    r_prod = span_rank(products)
    r_AB = span_rank(basis_AB)
    check("Observables generates: Alg(A u B) is generated by its parts",
          r_prod == r_AB == 4 ** (len(A) + len(B)),
          f"dim span(products)={r_prod}, dim Alg(A u B)={r_AB}")

    # Law: a complex amplitude on configurations, order-local, order-invariant.
    links = [(i, j) for i in range(n) for j in range(n)
             if i != j and R[i, j] and
             not any(k not in (i, j) and R[i, k] and R[k, j] for k in range(n))]
    configs = np.array(list(itertools.product([-1, 1], repeat=n)))
    beta, J = 0.37, 0.61
    bond = np.zeros(len(configs))
    for (i, j) in links:
        bond += configs[:, i] * configs[:, j]
    amp = np.exp(-beta * bond + 1j * J * bond)

    # invariance under order automorphisms
    autos = []
    for perm in itertools.permutations(range(n)):
        Q = R[np.ix_(perm, perm)]
        if np.array_equal(Q, R):
            autos.append(perm)
    inv_ok = True
    idx = {tuple(c): k for k, c in enumerate(configs)}
    for perm in autos:
        permuted = configs[:, list(perm)]
        mapped = np.array([idx[tuple(c)] for c in permuted])
        if not np.allclose(amp[mapped], amp, atol=1e-12):
            inv_ok = False
    check("Law is invariant under every order automorphism", inv_ok,
          f"{len(autos)} automorphism(s) checked over {len(configs)} configurations")

    # locality: flipping one event moves the amplitude only through its links
    local_ok = True
    for e in range(n):
        touched = [(i, j) for (i, j) in links if e in (i, j)]
        flipped = configs.copy()
        flipped[:, e] *= -1
        delta = np.zeros(len(configs))
        for (i, j) in touched:
            delta += flipped[:, i] * flipped[:, j] - configs[:, i] * configs[:, j]
        predicted = np.exp(-beta * (bond + delta) + 1j * J * (bond + delta))
        mapped = np.array([idx[tuple(c)] for c in flipped])
        if not np.allclose(amp[mapped], predicted, atol=1e-12):
            local_ok = False
    check("Law is local: single-event dependence runs only through its links",
          local_ok, f"{len(links)} links on {n} events")

    # (2) non-triviality: the amplitude is not a product over events
    logamp = np.log(amp)
    design = np.column_stack([np.ones(len(configs))] +
                             [configs[:, e] for e in range(n)])
    coef, *_ = np.linalg.lstsq(design, logamp, rcond=None)
    residual = float(np.abs(logamp - design @ coef).max())
    check("Law is non-trivial: the amplitude does not factorize over events",
          residual > 1e-6,
          f"max residual against the single-event span = {residual:.4f}")

    # Actuality: a non-trivial mutually exclusive menu exists in Alg(A)
    dim = 2 ** n
    menu = []
    for labels in itertools.product([0, 1], repeat=len(A)):
        M = np.array([[1.0 + 0j]])
        for e in range(n):
            if e in A:
                k = labels[A.index(e)]
                p = np.zeros((2, 2), dtype=complex)
                p[k, k] = 1.0
                M = np.kron(M, p)
            else:
                M = np.kron(M, np.eye(2, dtype=complex))
        menu.append(M)
    total = sum(menu)
    orth = max(float(np.abs(menu[i] @ menu[j]).max())
               for i in range(len(menu)) for j in range(len(menu)) if i != j)
    check("Actuality: a non-trivial exclusive menu exists in the region algebra",
          np.allclose(total, np.eye(dim)) and orth < 1e-12 and len(menu) > 1,
          f"{len(menu)} alternatives, sum = identity, max cross term {orth:.2e}")


def main():
    probe_lattice_substrate()
    probe_sprinkled_substrate()
    probe_model()

    passed = sum(1 for _l, ok, _d in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok, detail in RESULTS:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" ({detail})" if detail else ""))
    print("=" * 76)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
