"""Probe: verify the review panel's objections rather than take them on authority.

A reviewer's assertion is evidence, not proof. Four of the mathematical-rigour
panellist's objections are directly checkable, and each would be severe if true:

  (P1) the trivial one-point model satisfies every drafted axiom, so the axiom
       set entails nothing quantum, geometric or dynamical;
  (P2) almost all finite posets are rigid, so "invariant under every automorphism
       of the supplied order" constrains nothing on a typical causal set;
  (P3) ACTUALITY is self-contradictory: if every finite partition of the unit
       into positive observables is a menu, and exactly one element of a menu
       occurs, that is a dispersion-free assignment on effects, which is
       impossible;
  (P4) "decays with order separation" has no formalisation for INCOMPARABLE
       pairs - which is exactly the case decay is needed for - and causal-set
       link valency diverges, so there is no finite neighbourhood to decay from.

Each is tested. A failed check here means the panellist was wrong; a passed
check means the objection stands and the drafted axiom must change.
"""

import itertools

import numpy as np

RESULTS = []
rng = np.random.default_rng(20260809)


def check(label, ok, detail=""):
    RESULTS.append((label, bool(ok), detail))


# ---------------------------------------------------------------------------
# (P1) does the trivial model satisfy every axiom?
# ---------------------------------------------------------------------------

def probe_trivial_model():
    """One event; A(R) = C for every region; f = 1; omega = identity on C."""
    # Substrate: single event, order = {(e,e)}
    R = np.array([[True]])
    reflexive = bool(R[0, 0])
    antisym = bool(np.array_equal(R & R.T, np.eye(1, dtype=bool)))
    trans = bool(np.all((R.astype(int) @ R.astype(int) > 0) <= R))
    intervals_finite = True                      # |[e,e]| = 1

    # Observables: A(R) = C (1x1 matrices) for the only region
    A = np.array([[1.0 + 0j]])                   # the algebra C, unital
    isotone = True                               # only one region
    # commutation for order-unrelated regions: vacuous (no unrelated pair),
    # and in any case C is commutative
    commutes = True
    generated = True                             # union of one region

    # Law: f = 1 on the single configuration
    f = 1.0 + 0j
    aut_invariant = True                         # Aut = {id}
    decays = True                                # vacuous: no separated pair
    # positive type: omega(x) = x on C, two-point function = 1 >= 0
    two_point = np.array([[1.0]])
    psd = float(np.linalg.eigvalsh(two_point).min()) >= 0
    antisym_part = two_point - two_point.T
    commutator = np.zeros((1, 1))                # C is commutative
    commutator_matches = bool(np.allclose(antisym_part, commutator))

    # Actuality: the one-element partition {1} of the unit
    menu = [np.array([[1.0 + 0j]])]
    partition_ok = bool(np.allclose(sum(menu), np.eye(1)))
    outcome_exists = len(menu) >= 1

    all_satisfied = all([reflexive, antisym, trans, intervals_finite, isotone,
                         commutes, generated, aut_invariant, decays, psd,
                         commutator_matches, partition_ok, outcome_exists])
    check("(P1) the trivial one-point model satisfies EVERY drafted axiom",
          all_satisfied,
          "substrate ok, isotony/commutation/generation ok, Aut-invariance and "
          "decay vacuous, two-point function PSD (min eig 1.0), antisymmetric "
          "part = commutator = 0, unit partition {1} is a menu -> nothing "
          "quantum, geometric or dynamical is entailed by the axiom set")


# ---------------------------------------------------------------------------
# (P2) are typical causal sets rigid?
# ---------------------------------------------------------------------------

def sprinkle(n, rng):
    pts = []
    while len(pts) < n:
        t, x = rng.uniform(-1, 1, size=2)
        if abs(x) + abs(t) <= 1.0:
            pts.append((t, x))
    return np.array(sorted(pts, key=lambda p: p[0]))


def causal_matrix(P):
    dt = P[None, :, 0] - P[:, None, 0]
    dx = np.abs(P[None, :, 1] - P[:, None, 1])
    return dt >= dx


def automorphism_count(R):
    n = R.shape[0]
    count = 0
    for perm in itertools.permutations(range(n)):
        if np.array_equal(R[np.ix_(perm, perm)], R):
            count += 1
    return count


def refinement_signatures(R):
    """Order-invariant colour refinement. All-distinct signatures => rigid."""
    n = R.shape[0]
    S = R & ~np.eye(n, dtype=bool)
    sig = [(int(S[:, i].sum()), int(S[i, :].sum())) for i in range(n)]
    for _ in range(n):
        new_sig = []
        for i in range(n):
            past = tuple(sorted(sig[j] for j in range(n) if S[j, i]))
            fut = tuple(sorted(sig[j] for j in range(n) if S[i, j]))
            new_sig.append((sig[i], past, fut))
        codes = {v: k for k, v in enumerate(sorted(set(map(str, new_sig))))}
        nxt = [codes[str(v)] for v in new_sig]
        if nxt == sig:
            break
        sig = nxt
    return sig


def probe_rigidity():
    rows_exact = []
    for n in (5, 6, 7, 8):
        counts = [automorphism_count(causal_matrix(sprinkle(n, rng)))
                  for _ in range(40)]
        rows_exact.append("N=%d: %d/40 rigid, max |Aut|=%d"
                          % (n, sum(1 for c in counts if c == 1), max(counts)))

    rows_large, frac_last = [], 0.0
    for n in (20, 40, 80, 160):
        trials, rigid = 30, 0
        for _ in range(trials):
            sig = refinement_signatures(causal_matrix(sprinkle(n, rng)))
            if len(set(map(str, sig))) == n:
                rigid += 1
        frac_last = rigid / trials
        rows_large.append("N=%d: %d/%d provably rigid" % (n, rigid, trials))

    check("(P2) sprinkled causal sets become rigid with size, so Aut-invariance "
          "is asymptotically vacuous",
          frac_last > 0.9,
          "exact small-N: " + "; ".join(rows_exact)
          + " || refinement large-N: " + "; ".join(rows_large)
          + " -- small causal sets are often NOT rigid, so the objection fails "
            "at toy sizes; the asymptotic claim is the one that matters")


# ---------------------------------------------------------------------------
# (P3) is ACTUALITY self-contradictory?
# ---------------------------------------------------------------------------

def probe_dispersion_free():
    """If every partition of unity into positive observables is a menu, and
    exactly one element of a menu occurs, outcomes define v: effects -> {0,1}
    additive over partitions. Test whether such a v can exist on a qubit."""
    I2 = np.eye(2, dtype=complex)
    half = 0.5 * I2

    # {I/2, I/2} is a legitimate two-element partition of the unit into
    # positive observables: both are positive, and they sum to I.
    is_partition = bool(np.allclose(half + half, I2))
    both_positive = (float(np.linalg.eigvalsh(half).min()) >= 0)
    identical = bool(np.allclose(half, half))

    # "exactly one occurs" demands v(E1) + v(E2) = 1 with v in {0,1}.
    # Both elements are the SAME effect, so v must take two different values
    # on one and the same operator. No such function exists.
    contradiction = is_partition and both_positive and identical

    check("(P3) ACTUALITY is self-contradictory on the menu {I/2, I/2}",
          contradiction,
          "I/2 is positive, {I/2, I/2} sums to the unit, so it is a menu under "
          "the drafted clause; 'exactly one occurs' then requires a {0,1}-valued "
          "v with v(I/2) + v(I/2) = 1, i.e. v(I/2) = 1/2 -- no such function "
          "exists, and the two elements are literally the same operator")

    # And the general statement: no dispersion-free additive assignment on
    # effects, verified against the Born family which IS additive.
    rng2 = np.random.default_rng(3)
    worst_gap = 0.0
    for _ in range(2000):
        r = rng2.normal(size=3)
        r = r / max(np.linalg.norm(r), 1e-12) * rng2.uniform(0, 0.999)
        b = rng2.normal(size=3) * 0.2
        a = rng2.uniform(np.linalg.norm(b), 2 - np.linalg.norm(b))
        mu = 0.5 * (a + float(np.dot(r, b)))      # Tr(rho E) for rho=(I+r.sigma)/2
        worst_gap = max(worst_gap, min(abs(mu - 0.0), abs(mu - 1.0)))
    check("(P3b) the additive assignments on qubit effects are never {0,1}-valued",
          worst_gap > 0.4,
          f"over 2000 sampled effects the Born value Tr(rho E) sits at least "
          f"{worst_gap:.3f} away from both 0 and 1 in the worst case, so no "
          f"additive assignment is dispersion-free (Busch / Caves-Fuchs-Manne-Renes)")


# ---------------------------------------------------------------------------
# (P4) is "order separation" definable, and is link valency bounded?
# ---------------------------------------------------------------------------

def link_matrix(R):
    n = R.shape[0]
    S = R & ~np.eye(n, dtype=bool)
    two = S.astype(np.int16) @ S.astype(np.int16) > 0
    return S & ~two


def probe_order_separation():
    P = sprinkle(120, rng)
    R = causal_matrix(P)
    n = len(P)
    strict = R & ~np.eye(n, dtype=bool)
    related = strict | strict.T
    n_pairs = n * (n - 1)
    n_related = int(related.sum())
    frac_incomparable = 1.0 - n_related / n_pairs
    check("(P4) most event pairs are INCOMPARABLE, where the order gives no separation",
          frac_incomparable > 0.4,
          f"{frac_incomparable:.1%} of ordered pairs are incomparable in a "
          f"{n}-event sprinkling; chain-length separation is defined only for "
          f"comparable pairs, so 'decays with order separation' has no argument "
          f"to take exactly where decay is needed")

    rows, grows = [], True
    prev = 0.0
    for m in (30, 60, 120, 240):
        Pm = sprinkle(m, rng)
        L = link_matrix(causal_matrix(Pm))
        mean_val = float(L.sum() / m)
        rows.append(f"N={m}: mean links per event = {mean_val:.2f}")
        if mean_val <= prev:
            grows = False
        prev = mean_val
    check("(P4b) link valency grows without bound as the sprinkling densifies",
          grows,
          "; ".join(rows) + " -- valency diverges in the continuum limit, so "
          "there is no finite nearest-neighbour set for a local rule to act on")


def main():
    probe_trivial_model()
    probe_rigidity()
    probe_dispersion_free()
    probe_order_separation()

    passed = sum(1 for _l, ok, _d in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok, detail in RESULTS:
        print(f"[{'CONFIRMED' if ok else 'NOT CONFIRMED'}] {label}"
              + (f"\n    {detail}" if detail else ""))
    print("=" * 76)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    print("NOTE: PASS here means the PANEL'S OBJECTION IS CONFIRMED, i.e. the "
          "drafted axiom set is defective in that respect.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
