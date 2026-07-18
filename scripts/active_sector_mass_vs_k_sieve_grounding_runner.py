#!/usr/bin/env python3
"""Class-A verifier: the active-sector assignment (charged leptons / quarks corner-diagonal,
neutrino C3-structured) -- which gives large PMNS and small CKM -- is modeled by a
mass-vs-|K| DOMINANT-OPERATOR (energy-monitored) predictability sieve.

Setup. The hw=1 generation triplet carries two competing operators:
  - the MASS M, diagonal in the CORNER (position/BZ) basis: M = diag(m1,m2,m3);
  - the emergent C3 coupling K = |K|*(J - I), with an exact C3 singlet plus a degenerate
    orthogonal doublet (J = all-ones).
The pointer/active basis is the eigenbasis of the DOMINANT of {M, K} (the most-predictable,
energy-monitored basis). Whichever operator's scale dominates sets the recorded basis.

Sector grading by mass (with |K| the emergent C3 scale, fixed):
  - charged leptons / quarks: heavy, generation SPLIT >> |K| -> M dominates -> CORNER basis;
  - neutrino: tiny mass-split << |K| -> K dominates -> an eigenbasis containing a vector
    approaching the singlet W (the doublet basis remains non-unique in the exact K limit).

Verifies:
  (1) the dominant operator sets the pointer basis: small |K|/split -> corner (mass eigenbasis);
      large |K|/split -> an eigenbasis containing a vector approaching the singlet
      W=(1,1,1)/sqrt3 => a trimaximal column;
  (2) PMNS LARGE: charged=corner (U_e=I) vs neutrino=C3 (|K|-dominated) gives a trimaximal PMNS
      column (the recorded C3-singlet) and O(1) mixing;
  (3) CKM SMALL: the supplied mass-dominated quark matrices give a near-identity
      V_CKM = U_up^dag U_dn; exact identity requires the separate aligned-basis hypothesis;
  (4) the displayed diagonal mass matrix has 3 DISTINCT eigenvalues, the separately supplied
      real-symmetric C3 matrix a*I+b*(J-I) has its exact singlet/doublet spectrum, and the
      supplied C3 coupling has the exact W/orthogonal-plane eigenspaces. These finite comparisons
      imply no position-observable or carrier/readout exclusion;
  (5) the five supplied (mass-split)/|K| samples separate into a small-split side with a
      near-trimaximal column and a large-split corner-like side; no unique sharp threshold is proved.

Conditional: the residual is the energy-monitoring / dominant-operator pointer principle (the
einselection monitor identity, an open slot named in the records-flow separatrix note). This note
does not force the masses. No fitted mixing value is used as input, and no alternative carrier or
readout route is excluded.
"""

from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


J = np.ones((3, 3), dtype=complex)
Kop = J - np.eye(3)                                  # C3 coupling (J-I), DFT-diagonal
W = np.ones(3) / np.sqrt(3)                          # C3 singlet (democratic)


def pointer_basis(masses, Kmag):
    H = np.diag(masses).astype(complex) + Kmag * Kop
    _e, U = np.linalg.eigh(H)
    return U


def has_trimaximal_column(U, tol=2e-2):
    P = np.abs(U) ** 2
    return any(np.allclose(P[:, j], 1 / 3, atol=tol) for j in range(3))


def main() -> int:
    print("=" * 78)
    print("active-sector grounding: the mass-vs-|K| dominant-operator sieve  [class A]")
    print("=" * 78)

    # ---- (1) the dominant operator sets the (mass-graded) pointer basis ----
    print("\n-- (1) dominant operator sets the pointer basis (mass-graded) --")
    masses = np.array([1.0, 2.0, 3.0])               # generic nondegenerate corner masses
    split = masses.max() - masses.min()
    U_small = pointer_basis(masses, 0.01 * split)    # |K| << split -> corner
    U_large = pointer_basis(masses, 100.0 * split)   # |K| >> split -> C3
    check("|K| << mass-split: supplied eigenbasis is corner-like with no trimaximal column",
          not has_trimaximal_column(U_small))
    check("|K| >> mass-split: eigenbasis contains a near-singlet W => trimaximal column",
          has_trimaximal_column(U_large))

    # ---- (2) PMNS large: charged corner, neutrino C3 ----
    print("\n-- (2) PMNS LARGE: charged=corner (U_e=I), neutrino=C3 (|K|-dominated) --")
    U_e = np.eye(3, dtype=complex)
    U_nu = pointer_basis(np.array([1e-6, 2e-6, 3e-6]), 1.0)   # tiny mass, |K| dominates
    PMNS = U_e.conj().T @ U_nu
    P = np.abs(PMNS) ** 2
    trimax = [j for j in range(3) if np.allclose(P[:, j], 1 / 3, atol=2e-2)]
    check("PMNS has a trimaximal column (the supplied C3-singlet W) => O(1) lepton mixing",
          len(trimax) >= 1, detail=f"trimaximal column index = {trimax}")
    check("PMNS is genuinely large (some off-diagonal |U|^2 of order 1/3 or more)",
          np.max([P[i, j] for i in range(3) for j in range(3) if i != j]) > 0.25)

    # ---- (3) CKM small: both supplied quark examples are mass-dominated ----
    print("\n-- (3) CKM SMALL: both supplied quark examples are mass-dominated --")
    U_up = pointer_basis(np.array([1.0, 500.0, 1.7e5]), 1.0)   # |K|=1 << splits
    U_dn = pointer_basis(np.array([2.0, 90.0, 4.2e3]), 1.0)
    V_CKM = U_up.conj().T @ U_dn
    offmax = max(abs(V_CKM[i, j]) ** 2 for i in range(3) for j in range(3) if i != j)
    check("both mass-dominated examples => V_CKM = U_up^dag U_dn is near-identity (small mixing, "
          "no trimaximal column)", offmax < 1e-3 and not has_trimaximal_column(V_CKM),
          detail=f"max off-diagonal |V_CKM|^2 = {offmax:.2e}")
    check("the supplied mass-dominated comparison is numerically near the aligned identity matrix",
          np.allclose(np.abs(V_CKM) ** 2, np.eye(3), atol=1e-3))

    # ---- (4) exact spectra of the two displayed finite matrices ----
    print("\n-- (4) exact displayed mass and real-symmetric C3 spectra --")
    mass_eigs = np.sort(np.linalg.eigvalsh(np.diag(masses).astype(complex)).real)
    distinct = len(set(np.round(mass_eigs, 9))) == 3
    # A separately supplied real-symmetric C3 comparison matrix a*I+b*(J-I).
    a_c3, b_c3 = 0.7, 0.4
    c3_obs = a_c3 * np.eye(3) + b_c3 * Kop
    c3_eigs = np.sort(np.linalg.eigvalsh(c3_obs).real)
    check("the MASS operator has 3 DISTINCT eigenvalues => distinguishes all generations",
          distinct, detail=f"mass eigs = {list(mass_eigs)}")
    check("the displayed real-symmetric C3 matrix has exact spectrum (a-b,a-b,a+2b)",
          np.allclose(c3_eigs, [a_c3 - b_c3, a_c3 - b_c3, a_c3 + 2 * b_c3]),
          detail=f"C3-obs eigs = {[round(e,3) for e in c3_eigs]}")
    plane_probe = np.array([1.0, -1.0, 0.0]) / np.sqrt(2)
    check("the supplied C3 coupling has eigenvalue 2 on W and -1 on its orthogonal plane",
          np.allclose(Kop @ W, 2 * W)
          and np.allclose(Kop @ plane_probe, -plane_probe)
          and np.isclose(W @ plane_probe, 0.0))

    # ---- (5) finite sampled crossover in split/|K| ----
    print("\n-- (5) sampled crossover in (mass-split)/|K| --")
    Kmag = 1.0
    flips = []
    for s in (0.01, 0.1, 1.0, 10.0, 100.0):          # mass-split / |K|
        U = pointer_basis(np.array([0.0, s / 2, s]), Kmag)
        flips.append((s, has_trimaximal_column(U)))   # trimaximal => C3-dominated
    c3_side = [s for s, tm in flips if tm]
    corner_side = [s for s, tm in flips if not tm]
    check("the five supplied ratios separate into near-trimaximal small-split and corner-like large-split samples",
          max(c3_side) < min(corner_side),
          detail=f"near-trimaximal (split/|K|): {c3_side}; corner-like: {corner_side}")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("CHECK FAILURE: one or more finite matrix assertions were not satisfied.")
        return 1
    print("SUMMARY: under the supplied dominant-operator hypothesis, the mass-dominated quark examples are "
          "near the CORNER basis (small/near-identity CKM), while the supplied small-split neutrino "
          "example has a near-singlet trimaximal column (large mixing). Conditional on the energy-monitoring pointer "
          "principle (the open monitor slot); the displayed finite spectra imply no position-observable "
          "or carrier/readout exclusion; "
          "no fitted mixing value is used; no flavor mass value is forced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
