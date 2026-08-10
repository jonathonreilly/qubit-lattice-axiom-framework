# Goal

Run a 24-hour first-principles campaign against the highest-value unoccupied
TOE residuals. Block 1 attacks an explicit open mathematical question in the
landed Born-form program. It may identify a candidate axiom delta, but it must
not edit or enlarge the canonical axiom set.

## Exact target contract

**Target statement.** At one `M_2(C)` site let

`S = {c P(n) : 0 <= c <= 1, |n|=1} union {c I : 0 <= c <= 1}`.

A menu is a finite family of nonzero elements of `S` summing to `I`. Let
`w:S->[0,1]` be a function of the effect alone with `w(0)=0` and `w(I)=1`.
Assume `sum_j w(E_j)=1` for every scaled-projector menu containing at most
three outcomes. Decide, without a regularity premise, whether there must be a
unique density matrix `rho` such that

`w(E)=Tr(rho E)` for every `E in S`.

**Quantifiers/domain.** Every qubit Bloch direction, every coefficient in the
closed unit interval, every binary menu, and every ternary nonzero menu are in
scope. Menus may repeat an effect or a ray. The target is mathematical and
conditional; no physical eligibility is inferred.

**Allowed premises.** Finite-dimensional matrix algebra, positivity and the
range of `w`, Pauli/Bloch identities, and only the grading/menu hypotheses
written above.

**Forbidden weakenings.** Do not assume continuity, measurability,
differentiability, ray homogeneity, arbitrary finite additivity, four-outcome
same-ray splits, full-effect functionality, mixed-projective closure, a
literature theorem, or the Born formula itself.

**Required edge cases.** Coins; projective binary menus; equal-weight
projector pairs plus a coin; collinear ternary rank-one menus; nondegenerate
weighted trines; repeated outcomes; coefficient limits near zero and one; and
the distinction between exactly three outcomes and at most three outcomes.

**Completion witness.** Either a self-contained proof of the trace form with
an acyclic obligation graph, or one explicit non-trace `w` with exact range
and normalization proofs for every binary and ternary menu.

**What does not count.** Finite sampling, a floating-point LP alone, an ansatz
search that finds no rogue, a proof with an unproved regularity step, an
exactly-three-only counterexample, or a result using menus of arity four.

## Current Block 1 Disposition

The one-ancilla compression proves an exact bounded theorem after openly
applying the standard dimension-three frame-function theorem. That is a valid
direct answer to the landed frontier question at the repository's existing
named-theorem granularity, but it does not satisfy this campaign contract's
stronger self-contained witness because a literature theorem is load-bearing.
The remaining native obligation is a no-regularity representation lemma for
the special qutrit frame functions induced by top-block compression. The
bounded theorem may ship with that import exposed; the exact campaign target
must remain `advances`, not `closes`.

## Trace target

The landed source states:

> "prove ternary scaled-projector sufficiency or find a rogue"

Resolving the at-most-three surface closes that exact mathematical blocker and
sets the outcome-count threshold within one. It does not by itself derive Born
probabilities from the four axioms, because effect grading and physical menu
eligibility remain open.

## Campaign percentage rule

The checkpoint-zero TOE percentages in `STATE.yaml` remain fixed until an
obligation is actually retired. Mathematical threshold closure can increase
repo-science completeness in the Born lane. Physical-bridge or autonomous
closure percentages move only if the corresponding registration or selector
premises are also derived; naming candidate axiom text earns no closure.
