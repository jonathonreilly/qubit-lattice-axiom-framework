# Flavor Chirality Gate: Finite Algebra Scope Repair

**Date:** 2026-05-31
**Scope repair date:** 2026-06-04
**Claim type:** bounded_theorem
**Actual current surface status:** bounded-support
**Runner:** `scripts/flavor_chirality_gate_narrows_to_one_spin_statistics_import_2026_05_31.py` (SCORECARD 7/7).
**Audit repair target:** narrow the row to the algebraic P1/P2 checks and repair the P2c epsilon/Laplacian wording.

## Narrow Claim

This packet proves only the finite algebraic checks executed by the runner:

1. A single-site qubit creator is nilpotent, so the two-dimensional site does not by itself
   distinguish a qubit, a hard-core boson mode, and a one-mode fermion.
2. On two sites, the native qubit ladder product is ungraded: the two bare site ladders commute.
3. A Jordan-Wigner dressed pair anticommutes and spans the same ungraded operator algebra `M_4(C)` as
   the native qubit ladder generators.
4. The second Jordan-Wigner dressed ladder is not an operator local to the second native qubit factor:
   there is no `B` with `c_2 = I tensor B`. The anticommuting frame therefore changes the native
   tensor-support bookkeeping rather than being forced by the ungraded qubit tensor product.
5. For a supplied first-order Pauli/Clifford symbol `iD(k) = -sum_mu sigma_mu sin(k_mu)`, the runner
   checks `(iD(k))^2 = (sum_mu sin(k_mu)^2) I`.
6. For the supplied nearest-neighbor `Z^3` hopping matrix, the bipartite parity
   `epsilon=(-1)^(x+y+z)` anticommutes with hopping.
7. The second-order graph Laplacian `L = deg I - hop` is symmetric and A2-local, but it is not a
   chiral first-order operator: in the restricted finite check it neither anticommutes nor commutes
   with `epsilon`.

These checks support a bounded no-force statement: the native ungraded qubit tensor product does not
select the cross-site CAR/Jordan-Wigner frame, and the existence of an A2-local second-order
alternative prevents A2 alone from selecting the first-order chiral operator class.

## Out Of Scope

The following statements are not asserted by this note and remain separate bridge work:

- Dirac-Kahler equals Kogut-Susskind staggered fermions as the physical matter carrier.
- The `hw=1` locus and count-three generation reading.
- The carrier/generation identification for charged leptons.
- The Koide `Q=2/3` chiral structure.
- Spin-statistics or emergent Lorentz support for choosing a fermionic matter frame.
- Any claim that the full flavor sector follows from a single remaining import.

The earlier wording treated those downstream items as if they followed once the fermionic frame was
selected. The current packet does not supply the one-hop bridge derivations requested by the auditor,
so those statements are kept out of the load-bearing theorem.

## What The Runner Now Checks

The prior runner had an interpretive hard-coded `P1d=True`. The repaired runner replaces that with a
finite support test: `I tensor B` reconstruction succeeds for a native second-site ladder and fails
for the second Jordan-Wigner dressed ladder `Z tensor sigma_-`.

The prior P2c wording said the Laplacian was in an epsilon-commuting sector. For
`L = deg I - hop` with `{epsilon, hop}=0`, this is not literal. The repaired runner checks the honest
statement: the graph Laplacian is A2-local and symmetric, while both `[epsilon,L]` and
`{epsilon,L}` are nonzero in the finite packet. That is enough for the bounded conclusion because it
exhibits an A2-local non-chiral alternative to the supplied first-order operator.

## Audit Relevance

The auditor's conditional verdict was caused by an overbroad source claim: the algebraic checks were
real, but the note also asserted downstream flavor bridges that were not in the packet. This repair
chooses the auditor's narrowing path. It does not retag the audit ledger, does not propose an
effective status change, and does not add a new axiom.
