# Focused source check of the two-plaquette supervisor note

This is a focused mathematical/source check, not a landing review, audit,
retained-status decision, or authorization to publish. The same-family checker
first froze its independent Haar derivation, then read the supervisor note.
The primary implementation was not inspected. No numerical job was needed for
this review, and the three prior checker deliverables remain unchanged.

## Frozen source and coverage

The complete note reviewed was:

`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/docs/SU2_FIVE_STATE_TWO_PLAQUETTE_GAUGE_SECTOR_BOUNDED_THEOREM_NOTE_2026-11-07.md`

SHA-256:
`1ee7df33654b213d5134772f230902ad8e7ed936f626e19ccb4d8f5702a01db2`.
Line references below identify this source only.

The complete current axiom memo and premise registry were read in the
checker's `f5af11cd0102cfd0b51aef0911f600130bf5beb1` worktree:

| Source | SHA-256 |
|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | `93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753` |
| `docs/audit/data/axiom_premise_nodes.json` | `615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37` |

The independently frozen comparison sources are:

| Artifact | SHA-256 |
|---|---|
| `CHECKER.md` | `9dae7c28e6b840c7e7076001a1d5315686c876c15c06385c071d0159b43abc94` |
| `scripts/gb1_cf_two_plaquette_haar_check_2026_11_07.py` | `daa78235e9f850c486eba543cde39df04240ec6095f3db1998931874e80dfa66` |
| `logs/runner-cache/gb1_cf_two_plaquette_haar_check_2026_11_07.txt` | `1a586787d60fdfa75f45256ca5ef6056c3e6ea3a6c06c600f51dd185a094eb2b` |

## Findings

No blocking mathematical error was found in the sector dimension, Haar
coefficients, operator matrices, covariance convention, commutator, update
formulas, or either encoding. The following convention, provenance, and code
scope clarifications are requested; none changes the finite-patch theorem.

1. **State the dual-space identification in the singlet argument (lines
   82-87).** The unique two-end invariant is an antisymmetric tensor when both
   endpoint spaces are written as the defining doublet. With the natural
   oriented-link labeling, a mixed incoming/outgoing pair instead lies in
   `V tensor V*` and its invariant is the delta contraction. For example,
   `|up,up>+|down,down>` is invariant under `h tensor conjugate(h)`, whereas
   the antisymmetric vector generally is not. SU(2) self-duality identifies
   these descriptions, so the count is correct. Add "after identifying each
   dual doublet with the defining doublet via the SU(2) invariant epsilon
   tensor," or simply say "the unique two-doublet singlet." This makes the
   orientation/sign convention explicit and avoids suggesting that the same
   literal antisymmetric components apply to every oriented vertex.

2. **Define or remove the `s=1` provenance label (final provenance section).**
   No parameter `s` or representation family indexed by `s` is defined in this
   note. Section 4 of Chandrasekharan and Wiese's
   [Quantum Link Models: A Discrete Approach to Gauge Theories](https://arxiv.org/pdf/hep-lat/9609042)
   constructs the SO(5) embedding, exhibits the four-dimensional spinor
   representation, and permits other SO(5) representations. The five-state
   vector choice is compatible with that context, but the note should call
   it the five-dimensional SO(5) vector representation, or explicitly define
   its `s` convention and relation to this representation. The link
   normalization `P_mu=1/2(...)` remains the note's explicit convention;
   the citation should not silently stand in for that normalization.

3. **Explicitly restrict the 21-qubit equivalence to the initialized code
   (lines 200-205).** The existing code-projector language supports the correct
   reading, but a direct sentence would prevent a stronger interpretation.
   The three unused words per link transform trivially, so the enlarged
   qubit Hilbert space contains additional gauge singlets outside that code.
   Gauge invariance alone does not pick out the original four-dimensional
   physical sector.

## Mathematical checks

**Haar construction and gauge covariance.** The supplied five functions are
orthonormal, with `integral x_mu x_nu=delta_mu,nu/4`. Odd cubic moments vanish,
so compressed multiplication by each `x_mu` has precisely the stated `1/2`
empty/occupied entries and no occupied/occupied entries. For the declared
pullback, direct substitution gives
`T^dagger M_g T = M_(h_y g h_x^-1)`. The retained space is stable under
both actions, so compression preserves this identity. The note's
`T^dagger U T=h_y U h_x^-1` convention and `F_n ... F_1` traversal order
are consistent. Both displayed loop words cancel internal vertex factors.
No unitarity of the operator-valued U is used or required.

**Sector and coefficients.** All six zero-external-charge Gauss constraints
are included. Every vertex has degree at most three, so only zero or two
occupied ends survive, with one intertwiner. The four binary cycle patterns
are therefore the complete sector. The Wilson-trace basis, signs, and norms
are identical to the frozen independent basis; no rephasing is needed.
The shared-link integral is `+1/2` times the outer trace. Consequently the
magnetic entries are exactly 2 and +1, the electric diagonal is
`(0,3,3,9/2)`, and the commutator and its action on L have exactly the
displayed signs. The empty-flux reference is not identified with a physical
vacuum.

**Spatial exchange.** The geometric operation can be made explicit as
reflection in `x=1`, swapping A/C and D/F while fixing B/E. On oriented links
it sends `AB <-> BC^-1`, `DE <-> EF^-1`, `AD <-> CF`, with BE fixed.
The inverse-link operator on the five-state Haar basis fixes 0 and 4 and
changes the signs of 1,2,3; it implements `U -> U^dagger`. Combining those
inversions with the link permutation gives an involution on the full link
space. It exchanges the two magnetic operators and fixes E. Its restriction
is the note's S. Hence both gauge and exchange invariance of the joint
magnetic/electric product hold on the original full link space as well as
on the four-state sector. This is one patch symmetry, not a test of full
proper cubic covariance.

**Ordered and Strang products.** Their second- and third-order exchange
differences, including the factor `-i/8` and the empty-reference coefficient
`3i(L-R)/4`, match the independent exact Taylor computation. The text correctly
does not infer failure at every angle or a no-go for all schedules.

**Joint gate.** The additional identity `H^3=10H`, absent from the original
checker deliverable, was checked analytically here. Put

```
p = (L+R)/sqrt(2),       m = (L-R)/sqrt(2),
b = (2 empty+O)/sqrt(5), d = (empty-2 O)/sqrt(5).
```

Then `H p=sqrt(10)b`, `H b=sqrt(10)p`, and `H m=H d=0`.
Thus the spectrum is `sqrt(10),-sqrt(10),0,0`, proving the cubic identity
and the displayed sine/cosine exponential for every real angle. The note
correctly restricts that closed formula to the four-state sector. Because
S commutes separately with H and E, no commutativity of H with E is needed
for the product `exp(-i theta H) exp(-i tau E)` to preserve exchange.

**Logical encoding.** With the specified bit order, `X_1(2-n_2)` flips
`00 <-> 10` with coefficient 2 and `01 <-> 11` with coefficient 1.
`(2-n_1)X_2` gives the right-square transitions. The electric polynomial
takes values `0,3,3,9/2` on `00,10,01,11`. Hence all three formulas are
exact; no hidden rescaling or logical-bit permutation is needed.

**Full-link encoding.** Let V be the isometry from five link states to the
chosen three-qubit words and P=VV^dagger. Extending an operator as
`V O V^dagger`, and a gauge action as `V T V^dagger+(I-P)`, gives precisely
the stated zero/trivial extensions. The extended link operators commute with
P, and every loop Hamiltonian commutes with each link code projector, so
the seven-link code is invariant under their exponentials. The direct
21-qubit count is sufficient. Neither this algebraic embedding nor the
two-logical-qubit compression specifies a homogeneous site allocation,
nearest-neighbor circuit, or compatible overlap/gluing rule.

## Premise and scope disposition

The current axioms supply the cubic spatial structure, one-site `M_2(C)`
possibility algebra, the fixed nearest-neighbor probability-distribution
clause, and permanent records with their stated readout restrictions. The
registry does not independently supply this SU(2) group, representation,
boundary sector, interaction, update schedule, state, clock, or readout bridge.
The note treats those finite-model choices as explicit conditions and does
not promote them into axiom consequences. Its use of qubit blocks changes no
one-site algebra but also establishes no native physical implementation.

Remaining scope limits are the homogeneous spatial code/observable assignment,
translation/proper-cubic covariance, compatible overlapping updates at fixed
register size and locality, the admissibility/record law, state selection,
and Euclidean/continuum identification. No physical vacuum, gauge boson,
confinement, or mass-gap result is established. The reviewed exact source
supports the conditional finite-patch statement, with the requested source
clarifications above; it does not close the broader GB1-CF target. This report
applies to the exact note hash stated above, not to an unexamined amendment.

This check does not reproduce the primary runner, inspect its cache, validate
its source hashes, or execute formal landing/audit tooling. Its scientific
comparison uses the pre-exposure Haar derivation; the present source check is
a continuation of that same model/context, with the resulting correlated-bias
limitations, and not a new independently staffed review.

## Follow-up: requested amendments, 2026-11-07

The amended supervisor note has SHA-256
`268835ffc74a72e29890f1291a65611caa9c0af5a9efa66da330eab12e814305`.
The baseline remains the complete review above of note hash
`1ee7df33654b213d5134772f230902ad8e7ed936f626e19ccb4d8f5702a01db2`;
the review file before this appended follow-up had SHA-256
`13117ba2fe18ba5d4da7ab7ac9162c67755cd6d79890eb7a6b475926226ebffc`.
Only the requested convention, initialized-code, provenance, and
evidence/metadata amendments were checked in this follow-up. The preceding
complete mathematical review is reused; there was no rederivation, numeric
job, primary implementation access, audit, or formal landing verdict.

All three requested clarifications are resolved at this source hash:

1. The singlet paragraph now explicitly identifies dual doublets with the
   defining doublet using epsilon and separately names the delta contraction
   for a naturally labeled mixed incoming/outgoing pair. This removes the
   orientation ambiguity without changing the singlet multiplicity or any
   Wilson-trace phase convention.
2. The full-link encoding now restricts equivalence to the initialized code
   subspace and states that the unused words add singlets, so gauge invariance
   alone does not enforce initialization. This is the correct boundary for
   the zero/trivial extensions and preserves the 21-qubit sufficiency claim.
3. The undefined `s=1` literature label is removed. The provenance paragraph
   now credits the finite quantum-link approach and SO(5) embedding, while
   making the five-dimensional vector choice and P normalization explicit
   choices of this note. It no longer relies on an undefined representation
   parameter for the attribution.

The added metadata preserves the conditional finite-patch scope: it names
the supplied representation, graph, all-vertex zero-charge sector, and
operators; marks the result as upstream support for the still-open GB1-CF
extension; and explicitly requires audit before effective retained status,
with bare retained language disallowed. The body retains the author-proposal
status and pending independent landing review/audit. The added machinery
paragraph distinguishes mathematical tools from supplied model choices.
The evidence discussion also correctly separates the same-family, separately
derived original check from the later comparison and from landing/audit
authority. Its explicit existence-witness language does not turn the ordering
counterexamples into a no-go for other updates.

The implementation-level claims about the primary's later checker import,
its cache-input closure, and the handoff's receipts were not inspected or
reproduced here: primary implementation access was outside this assignment.
Those remain the supervisor's recorded provenance assertions, not newly
verified facts supplied by this follow-up. No cache or audit-schema validation
is implied by checking the metadata's scientific scope.

No unresolved issue was found in these amendments. The remaining substantive
limits from the complete review are unchanged: homogeneous spatial encoding,
full translation/proper-cubic covariance, compatible local overlap updates,
admissibility/record dynamics, state selection, and continuum identification.
The earlier three checker artifacts retain their recorded frozen hashes.
