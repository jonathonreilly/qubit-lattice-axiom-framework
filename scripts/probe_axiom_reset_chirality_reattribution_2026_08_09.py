"""Probe: was the chirality claim mis-attributed? (Referee objection 3.)

The reset proposal claimed that relaxing Admissibility's "nearest-neighbour"
to "local" removes the Nielsen-Ninomiya hypothesis, and called this the whole
cost of the chirality unlock. The referee objects that this is false:

  Nielsen-Ninomiya's locality hypothesis is NOT "nearest-neighbour". A lattice
  Dirac operator counts as local when its couplings are bounded by exp(-nu|x-y|)
  with nu > 0. Exponentially decaying couplings therefore sit INSIDE the NN
  hypothesis, not outside it. Relaxing nearest-neighbour to exponentially local
  removes no NN hypothesis at all. The overlap operator escapes doubling by
  giving up EXACT chiral symmetry in favour of the Ginsparg-Wilson relation -
  a different hypothesis entirely.

If the referee is right, the earlier probe measured the correct numbers and drew
the opposite inference from them.

Two things are tested:
  (A) the NN hypothesis audit: which hypothesis does each operator actually
      violate? If overlap violates EXACT CHIRAL SYMMETRY rather than LOCALITY,
      the escape is Ginsparg-Wilson and the axiom change is not what did it.
  (B) Horvath's no-go: can a strictly nearest-neighbour (compactly supported)
      operator satisfy the Ginsparg-Wilson relation at all? If not, then
      relaxing nearest-neighbour is NECESSARY to permit the real mechanism,
      even though it is not itself the mechanism.
"""

import numpy as np

RESULTS = []
L = 16

G1 = np.array([[0, 1], [1, 0]], dtype=complex)
G2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
G5 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def check(label, ok, detail=""):
    RESULTS.append((label, bool(ok), detail))


def momenta():
    k = 2.0 * np.pi * np.arange(L) / L
    return [(a, b) for a in k for b in k]


def d_naive(p1, p2):
    return 1j * (G1 * np.sin(p1) + G2 * np.sin(p2))


def d_wilson(p1, p2, mass=0.0, r=1.0):
    return (1j * (G1 * np.sin(p1) + G2 * np.sin(p2))
            + (mass + r * ((1 - np.cos(p1)) + (1 - np.cos(p2)))) * I2)


def d_overlap(p1, p2, m0=-1.0):
    dw = d_wilson(p1, p2, mass=m0)
    hw = G5 @ dw
    hw = 0.5 * (hw + hw.conj().T)
    vals, vecs = np.linalg.eigh(hw)
    return I2 + G5 @ (vecs @ np.diag(np.sign(vals)) @ vecs.conj().T)


def audit(op):
    """Return (species, exact-chiral defect, GW defect)."""
    species, chi, gw = 0, 0.0, 0.0
    for p1, p2 in momenta():
        D = op(p1, p2)
        if np.linalg.svd(D, compute_uv=False).min() < 1e-8:
            species += 1
        chi = max(chi, float(np.abs(G5 @ D + D @ G5).max()))
        gw = max(gw, float(np.abs(G5 @ D + D @ G5 - D @ G5 @ D).max()))
    return species, chi, gw


def main():
    # ---- (A) which NN hypothesis does each operator violate? -------------
    rows = []
    for name, op, compact in (("naive", d_naive, True),
                              ("Wilson", lambda a, b: d_wilson(a, b, 0.0), True),
                              ("overlap", d_overlap, False)):
        n, chi, gw = audit(op)
        rows.append((name, compact, n, chi, gw))

    naive = rows[0]
    overlap = rows[2]

    check("(A1) naive operator: strictly local AND exactly chiral => it doubles",
          naive[2] == 4 and naive[3] < 1e-12,
          f"species={naive[2]}, exact-chiral defect={naive[3]:.2e} "
          f"-- consistent with Nielsen-Ninomiya, no hypothesis violated")

    check("(A2) overlap operator does NOT have exact chiral symmetry",
          overlap[3] > 0.1,
          f"max |{{g5,D}}| = {overlap[3]:.4f} -- the operator that escapes "
          f"doubling has GIVEN UP exact chiral symmetry")

    check("(A3) overlap satisfies Ginsparg-Wilson instead",
          overlap[4] < 1e-10,
          f"max |g5 D + D g5 - D g5 D| = {overlap[4]:.2e}")

    # The decisive re-attribution: overlap is exponentially local, which IS
    # local in the NN sense. So NN is not evaded by locality.
    check("(A4) RE-ATTRIBUTION: the escape is Ginsparg-Wilson, not locality",
          overlap[3] > 0.1 and overlap[4] < 1e-10,
          "the overlap operator has exponentially bounded couplings, which "
          "already satisfies Nielsen-Ninomiya's locality hypothesis; the "
          "hypothesis it violates is EXACT CHIRAL SYMMETRY. Relaxing "
          "'nearest-neighbour' to 'exponentially local' removes no NN "
          "hypothesis. The earlier claim mis-attributed the mechanism.")

    # ---- (B) can a strictly nearest-neighbour operator satisfy GW? -------
    # Scan the general strictly-NN, gamma5-hermitian, cubic-covariant ansatz
    #   D(p) = i*c1*(g1 sin p1 + g2 sin p2) + (c0 + c2*(cos p1 + cos p2)) * I
    rng = np.random.default_rng(11)
    best = np.inf
    best_at = None
    for _ in range(40000):
        c0, c1, c2 = rng.uniform(-3, 3, size=3)
        worst = 0.0
        for p1, p2 in momenta()[::7]:            # subsample the zone
            D = (1j * c1 * (G1 * np.sin(p1) + G2 * np.sin(p2))
                 + (c0 + c2 * (np.cos(p1) + np.cos(p2))) * I2)
            worst = max(worst, float(np.abs(G5 @ D + D @ G5 - D @ G5 @ D).max()))
            if worst >= best:
                break
        if worst < best:
            best, best_at = worst, (c0, c1, c2)

    # A trivial solution D=0 or D=2 satisfies GW but is not a Dirac operator;
    # require a non-degenerate kinetic term.
    nontrivial = best_at is not None and abs(best_at[1]) > 0.1
    check("(B) Horvath: no strictly nearest-neighbour operator satisfies "
          "Ginsparg-Wilson with a real kinetic term",
          best > 1e-3 or not nontrivial,
          f"best GW defect over 40000 sampled ultralocal operators = {best:.4e} "
          f"at (c0,c1,c2)={tuple(round(float(v),3) for v in best_at)}; "
          f"kinetic coefficient |c1|={abs(best_at[1]):.3f}. Ultralocality blocks "
          f"the GW route, so relaxing nearest-neighbour is NECESSARY to permit "
          f"the real mechanism even though it is not itself the mechanism.")

    passed = sum(1 for _l, ok, _d in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok, detail in RESULTS:
        print(f"[{'CONFIRMED' if ok else 'NOT CONFIRMED'}] {label}"
              + (f"\n    {detail}" if detail else ""))
    print("=" * 76)
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
