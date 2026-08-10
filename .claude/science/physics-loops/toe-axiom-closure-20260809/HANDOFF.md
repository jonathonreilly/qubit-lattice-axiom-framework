# Handoff

Block 1 has a candidate-complete bounded theorem at named-standard-theorem
granularity. The exact question was whether a menu-independent grading on
one-site scaled projectors, normalized on every binary and ternary nonzero
menu, must be a density-matrix trace grading.

The proof lets `Pi:C^3->C^2` be top-block projection and defines
`F(u)=w(|Pi u><Pi u|)` on unit vectors. Every orthonormal basis of `C^3`
compresses to a binary or ternary qubit menu, so `F` is a nonnegative
weight-one frame function. The standard dimension-three frame theorem gives a
qutrit density matrix, and the zero ancilla expectation deletes its ancilla
row and column.

This closes the landed frontier question at the repository's existing
named-theorem granularity. It does **not** meet `GOAL.md`'s deliberately
stronger self-contained completion witness: a native no-regularity proof of
the special compression-invariant frame lemma remains open and is not hidden.

The direct functional-equation route gives restricted perimeter-two
additivity; exact polynomial rank leaves only the three Born modes through
degree nine. The source note includes the sufficient candidate axiom wording
and a complete N1-N8 firewall: it does not claim that an axiom edit is
necessary.

Block 1 is open as PR #6063. Direct conformance, five mutation probes, cache refresh, citation-manifest
regeneration, strict lint, link invariants, and cold diff review are complete.
The full pipeline's only stop is current-main dependency-policy drift owned by
open PR #6061. Next exact action: pivot to the native frame lemma or the physical
distribution-to-effect-grade/menu-eligibility bridge. Do not duplicate PR
#6062's basis-menu CNOT witness. Do not edit canonical axiom files. Do not
invoke `review-loop`.

## Current axiom-interface block

The physical pivot now has an exact type result. A single whole-domain
probability measure `mu` cannot itself be a raw singleton grade on even the
disjoint `x` and `z` binary menus: each menu would have mass one, so their
union would have mass two. Normalized finite restriction is also not a
universal bridge. The current wording admits a full-support atomless Gaussian
family for which every finite menu has measure zero, and an exact atomic
shared-effect witness gives `25/142` in one ternary menu and `2/11` in another.

The sufficient axiom-facing interface is therefore typed as:

1. registered measurable outcome partitions that push the existing `mu` to a
   normalized conditional kernel for how a forming Record's locked realization
   is read;
2. descent to one grade of the same registered effect across menus;
3. the endpoint values `w(0)=0` and `w(I)=1`;
4. physical coverage of every binary and ternary resolution in the full
   scaled domain `S`.

Composed with the parent frame-lift theorem, these clauses derive a unique
local density matrix and trace grade. They are candidate wording only: no
canonical axiom was edited, and N1--N8 rejects any necessity or constructive-
route-exhaustion claim.

The primary runner is `PASS=20 FAIL=0`; eleven mutation probes fail exactly at
their targets; an independent SymPy calculation agrees. The source, cache,
harness row, and citation manifest are open as stacked PR #6065 at commit
`4b12a78d16`, with #6063 as a hard parent. The full
pipeline reproduces only the current-main dependency-policy epoch mismatch
owned by PR #6061; 1,044 tracked generated changes and 814 generated ledger
shards were removed after the run. Continue without `review-loop`.

Next campaign block: test a constructive derivation of the registered
measurable outcome partitions and same-effect descent from Record plus
Admissibility. If current structure underdetermines them, seek an exact paired-
model witness and report the residual axiom update; do not edit the canonical
axiom memo without owner authorization.
