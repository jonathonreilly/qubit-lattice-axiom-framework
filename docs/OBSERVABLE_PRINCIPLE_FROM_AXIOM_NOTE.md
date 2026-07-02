# Observable Principle Finite Readout-Boundary Note

**Date:** 2026-04-13 (initial); 2026-05-07 scope-narrowed to bounded
conditional exact-algebra statement per
`OBSERVABLE_PRINCIPLE_AUDIT_NOTE_2026-05-02` finding;
2026-05-09 runner-local checks of determinant evenness, finite-block
regularity, and baseline invariance are kept as candidate
consistency checks, without promoting any cited upstream row;
2026-05-25 headline narrowed to the **finite-algebra `log|det(D+J)|`
generator step on the runner block, conditional on the P1 additivity and
P2 phase-blind scalar-generator selection admissions**, per audit-lane
finding that unconditional baseline-to-observable closure is not supported.
2026-06-04 Record-axiom repair: P1 scalar record additivity is no longer a
Tier-A admission when the row uses only finite scalar record additivity; it is
part of the approved `minimal_axioms` node (current memo:
[MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)). 2026-06-06
positive-source-cone repair: on the finite real source sector this note
actually consumes, P2 phase-blindness is eliminated rather than admitted.
2026-06-10 boundary-declaration repair: the readout-identification bridge
premise is declared as the explicit Boundary, Theorem 1 is restated as a
five-input chain (T1-a..T1-e), and the runner residual-checks the Theorem-2
observable map; see Changelog. 2026-06-16 T1-d independence guardrail:
[`OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md`](OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md)
proves that Record additivity plus determinant block factorization does not
derive the determinant-only readout quotient or the source-blocks-to-records
clause, so T1-d remains an explicit Boundary rather than axiom-derived
content. 2026-06-18 context-bridge split:
[`OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md`](OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md)
proves that those two clauses close inside a supplied determinant-sector
readout context, while preserving the no-go that Record alone does not supply
that context. 2026-06-18 positive-diagonal readout classifier:
[`OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md`](OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md)
shows that, once finite positive diagonal source-block additivity is supplied,
every continuous direct-sum additive diagonal readout is a sum of one-site
terms, and determinant-only readout is exactly the quotient that removes all
non-logarithmic one-site invariants and any global dimension label. This
sharpens the T1-d residual; it does not derive T1-d from Record.
**Type:** bounded_theorem (finite-algebra `log|det(D+J)|` generator on
the runner block, using Record-backed finite scalar additivity, the
positive-source-cone P2 elimination on the consumed finite real source surface,
and **one declared bridge premise** — the readout-identification Boundary
below; finite-block regularity, the conventional `c = 1` representative of the
generator family, and zero-source baseline normalization are explicit
conventions/checks, not new axioms).
**Boundary (declared bridge premise, T1-d):** *the scalar record readout `W`
of the source-deformed block is a continuous function of the Berezin amplitude
`Z = det(D+J)` alone, defined on all of `R_{>0}` (the lemma's L3 continuity
hypothesis, not just the attainable block amplitudes), and independent
disjoint source blocks register as disjoint records.* The axiom memo
explicitly excludes source/action and physical-observable identification from
Record content, so this identification is a premise of this note, declared and
consumed as such — not a consequence of `minimal_axioms`. The 2026-06-16
T1-d independence no-go gives the exact obstruction: continuous direct-sum
additive finite source readouts such as `log det + epsilon Tr` obey Record-style
additivity and determinant multiplicativity while failing to be functions of
`det(D+J)` alone, and a source-disjoint assignment need not be record-disjoint
without an additional readout-context bridge.
The 2026-06-18 determinant-context quotient bridge records the positive half of
that boundary: if a determinant-sector readout context is independently
supplied, then the trace-sensitive countermodel is excluded by the quotient and
source-block labels are disjoint records by the supplied context's injective
assignment. That bridge still does not derive T1-d from Record or promote this
parent row. The 2026-06-18 positive-diagonal
classifier strengthens the obstruction into a full local classification:
on positive diagonal blocks, additivity gives `W_n(x_1,...,x_n)=sum_i phi(x_i)`;
determinant-only global readout is the special continuous case
`phi(x)=c log x` after erasing any dimension label. The remaining T1-d bridge is
therefore exactly a source-to-record disjointness bridge plus a determinant
quotient, not a hidden consequence of Record.
**Headline (post-2026-06-10 boundary declaration):** *On finite scalar record
readout surfaces, Record supplies P1 additivity over disjoint/independent
record collections. On the finite real staggered source sector consumed here,
`det(D+J)` is real-positive on the positive source cone and on the local
invertible derivative patch, so `log det`, `Re Log det`, and `log|det|`
coincide. Record additivity plus the declared readout-identification Boundary
(continuity of `W` in `Z = det(D+J)` on all of `R_{>0}`; disjoint blocks as
disjoint records) fixes the additive generator family
`{W_c = c log det : c in R}` on the consumed branch; with the conventional
`c = 1` representative and zero-source baseline, the runner-block generator is
`W = log|det(D+J)|`, and its exact local source-derivative algebra is the
in-scope theorem-grade content of this note.* Global/off-sector
phase-blindness, arbitrary observable identification, and baseline-to-observable
closure outside this finite real source sector are explicitly **out of scope**.
**Claim scope (post-2026-05-07 scope narrowing; further narrowed
2026-05-25; Record-repaired 2026-06-04; P2 source-cone-repaired
2026-06-06; boundary-declared 2026-06-10):** the load-bearing claim of this
note is the **finite exact-algebra statement** on the exact minimal hierarchy
block, using Record-backed P1 additivity, the phase-free positive/local source
surface, and the declared readout-identification Boundary:

> **Given** Record/P1 finite scalar additivity on disjoint independent
> record collections, the finite real staggered source block `D^T=-D`,
> real diagonal scalar sources in the positive source cone or local
> invertible derivative patch (so `det(D+J) in R_{>0}`), **and the declared
> readout-identification Boundary (`W` is a continuous function of
> `Z = det(D+J)` alone on all of `R_{>0}`; disjoint independent source
> blocks register as disjoint records)**, with the conventional `c = 1`
> representative and zero-source baseline fixed conventionally,
> the following exact lattice-algebra identities hold on the exact minimal
> hierarchy block: (1) the additive continuous scalar generator family is
> exactly `{W_c = c log det(D+J) : c in R}`, with `c = 1` the conventional
> representative `W = log|det(D+J)|`; (2) local scalar observables are exact
> source derivatives of `W`, with the derivative trace formulas
> residual-checked by the runner; (3) the closed-form Matsubara identity
> matches `W(j)` to the exact hierarchy curvature kernel (verified at two
> couplings, with the exact spectral multiset and pair-product determinant
> identity); (4) that kernel is Klein-four invariant and selects `L_t = 4`
> as the unique minimal resolved orbit on the APBC temporal circle, by an
> exact counting argument valid for all `L_t`, not by scan alone.

As of the 2026-05-07 scope narrowing, all four premises P1-P4 were
admitted selection premises with the role classifications recorded in
`OBSERVABLE_PRINCIPLE_AUDIT_NOTE_2026-05-02.md` §1. The exact-algebra
closure GIVEN those premises is the load-bearing content; that is what
the runner verifies.

As of the 2026-06-04 Record repair, the P1 part of that older premise set
is no longer a Tier-A admission when used only as finite scalar record
additivity: it is supplied by the approved Record axiom (current memo:
[MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)). As of the
2026-06-06 source-cone repair, the separate P2 admission is no longer
load-bearing on the in-scope consumed source surface: the positive-source-cone
bridge proves `det(D+J) in R_{>0}` on the relevant finite branch, so there is
no determinant phase for a scalar generator to retain or discard. As of the
2026-06-10 boundary declaration, the remaining bridge content — the
readout-identification step that turns Record's record additivity into
generator additivity in `Z = det(D+J)`, including the `R_{>0}` Cauchy domain —
is stated as the single declared Boundary premise (T1-d) rather than folded
silently into the axiom citation.
This note does not set or predict the audit row's status. The narrowed
Record/P1 plus positive-source-cone surface is for independent re-audit, and
this repair does **not** promote `CPT_EXACT_NOTE`, `AC_phi_lambda`, or any
upstream row.

The `v = 246.28 GeV` **numerical readout** in §"Consequence for v"
depends on the canonical hierarchy baseline
`M_Pl * alpha_LM^16 = 254.6432... GeV` and on the measurement
comparator `v_meas = 246.22 GeV`; both are out-of-scope of this note's
load-bearing claim and enter only as admitted-context comparators (see
"Out of scope" below).
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome; later status is generated by the audit
pipeline after independent review. The `bounded_theorem` label above is
a source-side claim-boundary declaration, not an audit verdict; the
prior independent review found the unconditional framing conditional only,
and this scope narrowing implements that repair path (see §"Prior conditional
scope" below).
**Script:** `scripts/frontier_hierarchy_observable_principle_from_axiom.py`

## Premise split

This note used to be the canonical source-side parent for the **P1** Tier-A
admission. That is stale after the owner-approved 2026-06-04 Record axiom.
The central registry now records that Record/P1 scalar additivity is retired
from Tier A and included in the approved `minimal_axioms` node; the older
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` parent is explicitly not promoted as
an axiom authority for anything beyond narrow finite scalar record additivity.

- **Record/P1 (Record-supplied premise in this row's narrow use):** scalar record
  functionals are additive over disjoint finite record collections:
  `I(R_1 sqcup R_2) = I(R_1) + I(R_2)`, with `I(empty)=0` after an explicit
  additive-baseline convention. Turning this record additivity into the
  generator additivity used by the proof,
  `W[J_1 ⊕ J_2] = W[J_1] + W[J_2]` on the runner's finite block-diagonal
  independent-subsystem surface, additionally consumes the declared
  readout-identification Boundary (T1-d): `W` is a continuous function of
  `Z = det(D+J)` alone on all of `R_{>0}`, and disjoint independent source
  blocks register as disjoint records. Record alone does not supply that
  identification (see "No laundering" below).
- **No status promotion from axioms:** Record premise support is
  chain-satisfying for this narrow dependency, but it is not `retained`,
  `retained_bounded`, or any other audit verdict. Consumers must not treat an
  axiom or primitive as a bounded-status source for this note or its
  descendants.
- **No laundering of the old parent:** Record supplies only finite scalar
  record additivity. It does not supply P2/modulus, log-det structure,
  source/action identification, measurement, Born weights, dynamics,
  normalization/scale, time arrow, or arbitrary observable identification.
- **Out-of-scope of this note's load-bearing theorem:** global/off-sector P2
  scalar-generator selection from independently accepted bridge theorems. The load-bearing
  theorem of this note is the finite-algebra `log|det(D+J)|` generator step
  on the runner block **on the real-positive consumed source surface**; it is
  not unconditional baseline-to-observable closure for arbitrary source sectors.
- **P2 on the consumed source sector (eliminated, not admitted):** the
  positive-source-cone bridge proves that the finite real staggered block with
  real diagonal scalar sources has `det(D+J) in R_{>0}` on the positive source
  cone and on the local invertible derivative patch. On that branch
  `log det = Re Log det = log|det|`, so phase-sensitive and phase-blind
  candidates coincide. No separate P2 premise is consumed by the in-scope
  source-response theorem.
- **Runner-local consistency checks:** determinant evenness, finite-block
  analyticity near zero source, and normalization shift-invariance are checked
  in §"Runner-local consistency checks for source regularity and normalization".
  They now support the positive-source-cone repair rather than serving as a
  substitute for a global P2 theorem.

This note does **not** extend the Tier-A portfolio. It consumes the new
Record axiom only for finite scalar additivity and leaves any global/off-sector
phase-blindness question outside the in-scope consumed source surface.

## Question

Can the last hierarchy gap be closed on the finite source surface by deriving
the scalar observable map from the finite Grassmann block, Record additivity,
and one explicitly declared readout-identification Boundary, instead of
importing the usual QFT language about effective actions and order parameters?

## Answer

On the finite real staggered source surface consumed by this note, Record/P1
finite scalar additivity, the declared readout-identification Boundary, and
the lemma's Cauchy-uniqueness fact select the `log|det(D+J)|` generator
without importing a separate P2 phase-blindness premise. The
positive-source-cone bridge proves that the relevant source branch has
`det(D+J) in R_{>0}`, so the possible distinction between `log det`,
`Re Log det`, and `log|det|` disappears on the in-scope branch. Exactly one
input of the chain is a declared bridge premise rather than a computed or
axiom-supplied fact: the Boundary (T1-d). Unconditional baseline-to-observable
closure outside this finite real source sector is **not** claimed by this
note and remains out of scope.

The key step is not another determinant fit. It is the additive structure of
the exact Grassmann Gaussian.

Given the source-deformed lattice Dirac operator

`D[J] = D + J`,

the exact fermionic partition amplitude is

`Z[J] = det(D[J])`.

That is forced by the finite Grassmann integral. No continuum QFT machinery is
needed.

## Theorem 1: the five-input chain selecting `W = log det(D+J)`

Theorem 1 is stated as an explicit five-input chain so that each input's
epistemic character (computed / lemma-recomputed / axiom premise / declared
bridge premise / lemma fact) is visible rather than folded into a single
axiom citation:

- **T1-a (computed: Berezin determinant + block factorization).** The finite
  Grassmann integral gives `Z[J] = det(D+J)`, and for two independent
  subsystems `D = D_1 ⊕ D_2`, `J = J_1 ⊕ J_2`, the partition amplitude
  factorizes exactly: `Z[J_1 ⊕ J_2] = Z_1[J_1] Z_2[J_2]`. (Runner Part 1.)
- **T1-b (lemma facts L1/L2, runner-recomputed: det positivity on the
  consumed branch).** On the in-scope source branch, the finite real
  staggered block has `D^T = -D` and real diagonal scalar sources, and facts
  L1/L2 of the det-positivity lemma give
  `Z[J] = det(D+J) in R_{>0}` on the positive source cone and on the local
  invertible derivative patch. The runner recomputes the L1 mechanism
  (`B = S^{-1/2} D S^{-1/2}` antisymmetric, `det(I+B) = prod(1+lambda_k^2)
  >= 1`) and the L2 Neumann hypothesis (`||D^{-1}J|| < 1` for every source
  magnitude this runner uses) on the actual runner blocks. (Runner Part 8.)
  Therefore there is no fermionic phase on the branch this note
  differentiates: `log Z[J] = Re Log Z[J] = log |Z[J]|`.
- **T1-c (axiom premise: Record finite scalar additivity).** For any finite
  pairwise-disjoint collection of records, the scalar readout `I` is finitely
  additive with `I(empty) = 0`
  ([MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md), Record).
- **T1-d (declared bridge premise — the Boundary).** The
  readout-identification bridge: the scalar record readout `W` of the
  source-deformed block is a continuous function of `Z = det(D+J)` alone,
  defined on all of `R_{>0}`, and independent disjoint source blocks register
  as disjoint records. This is exactly where Record's record additivity
  `I(R_1 ⊔ R_2) = I(R_1) + I(R_2)` becomes generator additivity
  `W[J_1 ⊕ J_2] = W[J_1] + W[J_2]`, and where the functional equation —
  justified pointwise only on the attainable block amplitudes — acquires its
  full `R_{>0} × R_{>0}` Cauchy domain (the L3 continuity hypothesis). The
  axiom memo explicitly excludes source/action and physical-observable
  identification from Record content, so this input is **not derivable** from
  `minimal_axioms`; it is declared and consumed as the single bridge premise
  of this note.
- **T1-e (lemma fact L3: Cauchy uniqueness on `R_{>0}`).** By L3 of the
  det-positivity lemma, with continuity on `R_{>0}` the solutions of the
  multiplicative-to-additive functional equation
  `W(r_1 r_2) = W(r_1) + W(r_2)` are exactly the one-parameter family
  `{W_c(r) = c log r : c in R}`; `c = 1` is the conventional representative.

**Conclusion (chain a→e).** Given T1-a..T1-e, the additive continuous scalar
generator family on the consumed branch is exactly
`{W_c[J] = c log det(D+J) : c in R}` (up to baseline convention), which on
this real-positive branch coincides with `{c log|det(D+J)|}`.
The theorem fixes this family, not an absolute physical scale. The `c = 0`
member is the null readout; the source-response and selector statements below
use the conventional nonzero representative `c = 1`.

A universal additive constant is not part of the exact Cauchy solution:
`W(r_1 r_2) = W(r_1) + W(r_2)` forces any constant term to vanish. The
zero-source subtraction used below is instead an explicit extensive baseline
convention applied to the selected generator,
`W[J] = c(log det(D+J) - log det D)`, so that `W[0]=0`.

After picking the conventional `c = 1` representative and subtracting the
zero-source baseline, the framework-native scalar generator is therefore

`W[J] = log |det(D+J)| - log |det D|`.

On the consumed finite source surface, this is not an imported QFT choice
and does not require a separate P2 premise. It is selected by:

1. exact Grassmann factorization (T1-a)
2. finite real-positive determinant branch, which eliminates the phase (T1-b)
3. finite scalar record additivity on independent disjoint subsystems (T1-c)
4. the declared readout-identification Boundary (T1-d)
5. Cauchy uniqueness on `R_{>0}` (T1-e)

## Theorem 2: local scalar observables are source derivatives of `W`

Once the scalar generator is fixed, local scalar observables are exactly the
coefficients in its local source expansion.

For a local scalar source

`J = sum_x j_x P_x`,

the exact derivatives are

`∂W/∂j_x = Re Tr[(D+J)^(-1) P_x]`

and

`∂^2 W / ∂j_x ∂j_y = - Re Tr[(D+J)^(-1) P_x (D+J)^(-1) P_y]`.

So the local scalar curvature is:

1. **bosonic**: it is even in the fermion source
2. **quadratic / bilinear**: it is second order in the inverse Dirac operator
3. **connected**: mixed derivatives vanish on independent blocks
4. **local**: it is generated by local projectors `P_x`

That is the observable-principle map on the real-positive finite source
surface. Given Record/P1, the real staggered block, the declared Boundary, and
the local invertible source patch, it comes from the exact lattice source
response.

These derivative trace formulas are the actual observable-principle map, so
they are not left citation-only: the runner residual-checks the first,
mixed-second, and same-site-second source-derivative formulas against central
finite differences of `W` on a **non-uniform** positive-cone source
(deterministic fixed seed), with residuals at the `~1e-11` / `~1e-9` level
(Runner Part 2).

## Theorem 3: the hierarchy kernel is exactly the bosonic curvature kernel

For the homogeneous scalar source `J = j I` on the exact `L_s = 2` APBC block,

`W(j) = log |det(D + j I)| - log |det D|`

matches the exact Matsubara formula:

`W(j) = 4 sum_omega log(1 + j^2 / [u_0^2 (3 + sin^2 omega)])`.

So the small-source curvature is

`W(j) = 4 j^2 sum_omega 1 / [u_0^2 (3 + sin^2 omega)] + O(j^4)`.

Dividing by the four-volume gives the exact hierarchy coefficient already
derived independently:

`A(L_t) = (1 / (2 L_t u_0^2)) sum_omega 1 / (3 + sin^2 omega)`.

The closed form is verified as an identity in the coupling, not a
single-point coincidence: the runner checks it at `u_0 = 0.9` **and**
`u_0 = 1.17`, together with the underlying exact spectral multiset
`spec(D) = {± i u_0 sqrt(3 + sin^2 omega)}` (multiplicity 4 per temporal
mode) and the pair-product determinant identity
`log|det(D + jI)| = 4 sum_omega log(j^2 + u_0^2 (3 + sin^2 omega))`
(Runner Part 3).

This is the crucial closure step:

> under Record/P1 plus the positive-source-cone P2 elimination, the hierarchy
> normalization surface is not an imported effective-action object anymore; it
> is the exact local scalar curvature of the additive real-positive source
> generator.

## Theorem 4: the selector follows for the nonzero representative

The curvature kernel depends only on

`sin^2 omega`,

so it is exactly invariant under the Klein-four action on APBC phases:

`z -> z, -z, z*, -z*`.

That is the same sign-and-conjugation closure derived earlier from the
bosonic-bilinear selector route. On the APBC temporal circle:

- `L_t = 2` gives only the unresolved sign pair
- `L_t = 4` gives the unique minimal resolved closed orbit
- `L_t > 4` splits immediately into multiple orbit sectors

**Exact counting argument (valid for all `L_t`, not scan-only).** The
Klein-four group `V = {z, -z, z*, -z*}` has order 4, so every `V`-orbit has
at most 4 elements. The APBC temporal circle for `L_t` carries exactly `L_t`
distinct phases `exp(i (2n+1) pi / L_t)`. Hence the number of orbits is at
least `ceil(L_t / 4)`, and a single-orbit kernel requires `L_t <= 4` for
**every** `L_t`. `L_t = 2` gives the single orbit `{± i}` of size 2 — the
unresolved sign pair; `L_t = 4` gives one resolved orbit of size 4; every
`L_t > 4` has `>= 2` orbits and splits. The runner verifies the group-order
bound and the counting inequality on the scanned range and records the
conclusion (Runner Part 4); the argument itself needs no scan cutoff.

So, for the conventional nonzero representative, the `L_t = 4` selector is
internal to the Record-plus-source response on the repaired finite real source
surface with the declared readout Boundary.

## Consequence for `v` (out-of-scope numerical readout — admitted-context only)

**This subsection is out of the in-scope claim of this note.** It is
included as a numerical readout comparator under the explicit
admitted-context labels below. The status of the underlying canonical
baseline `M_Pl * alpha_LM^16` is decided by the audit lane on its own
authority row, not here. In the runner, the hard-coded
`canonical_plaquette_surface` helper backing this comparator is imported
locally inside the out-of-scope Part 5 only; the load-bearing Parts 1-4 and
6-8 are import-free of it, and Part 5 contributes zero PASS gates.

The exact selector correction is

`C = (7/8)^(1/4) = 0.967168210134`.

Using the current hierarchy baseline (audit-pending external authority,
admitted-context to this note):

`M_Pl * alpha_LM^16 = 254.643210673818 GeV`,

this gives

`v = 246.282818290129 GeV`.

Compared with the measurement comparator (admitted-context comparator role
only — not a derivation input):

`v_meas = 246.22 GeV`,

the difference is:

- `delta v = +0.062818290129 GeV`
- relative error `= +0.025513%`

This relative-error readout is shown as a **comparator only**. It is
not consumed as a load-bearing input by any in-scope claim of this note.

## What this closes (under the repaired finite source scope)

This removes the hierarchy-specific effective-action import on the current
exact minimal block, using **Record/P1 plus the positive-source-cone P2
elimination** on the finite real source surface.

The scalar observable principle is no longer:

> borrow the continuum effective-action language and hope it matches.

It is now:

> the axiom gives an exact Grassmann partition amplitude;
> using Record/P1 finite scalar additivity, the declared
> readout-identification Boundary (T1-d), and the fact that the consumed
> source branch has `det(D+J) in R_{>0}`, with zero-source baseline
> normalization fixed conventionally, scalar bosonic observables are the local
> source-response coefficients of the selected additive amplitude generator.

That generator is `log|det(D+J)|`, and its exact local curvature is the
hierarchy normalization surface — under the conditional scope. Record/P1 is
supplied by Record only in its narrow finite scalar-additivity use; that
premise support is not an audit verdict. Global/off-sector P2 is not derived
here, but it is no longer load-bearing on the in-scope consumed source branch.

## Honest scope

Under the **repaired finite source scope** (Record/P1 additivity plus the
real-positive source branch; finite-block regularity and zero-source baseline
behavior checked on the selected candidate generator — see §"Runner-local
consistency checks for source regularity and normalization" below),
the hierarchy closure is as clean as the current framework can make it on
the in-scope finite-source observable map.

The remaining `0.03%` is no longer an open theorem gap in the
observable-principle algebra under that scope. It sits in the canonical
same-surface plaquette evaluation and its downstream normalization chain
rather than in the finite-source observable algebra itself.

The remaining status question is no longer a separate P2 admission on the
finite source surface. It is twofold: whether the reviewer/auditor accepts
the positive-source-cone bridge as removing the phase premise on the consumed
branch, and whether the single declared readout-identification Boundary
(T1-d) is acceptable as the note's one bridge premise — it is genuinely not
derivable from the axiom memo, which excludes source/action and
physical-observable identification from Record content. This non-derivability
is now sharpened by
[`OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md`](OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md):
Record-compatible additive source readouts need not be determinant-only, and
source-disjoint blocks need not register as disjoint records. The broader
`AC_phi_lambda`/Berezin determinant identification and off-sector
phase-blindness questions stay out of scope. The
older P1 question is closed only for the narrow finite scalar
record-additivity use by the Record axiom; it is not a license to import the
broader old observable-principle parent. This revision does not change audit
status; the audit lane must still independently decide the row verdict.

## Prior conditional scope (2026-05-07 scope narrowing)

The 2026-05-02 independent review of the earlier unconditional framing found
that the theorem needed either upstream derivations of the missing selection
premises or an explicit conditional scope:

> The runner verifies the algebra after the scalar-generator premises are
> chosen; it does not by itself derive why physical scalar observables must
> select that generator from the baseline axioms alone. Repair target:
> either add independent upstream derivations of the bridge premises, or
> narrow this row to a conditional theorem given those premises.

This note originally adopted the verdict's second named alternative
("narrow this row to a conditional theorem given those premises"). The
2026-06-06 repair now takes the stronger bridge route for the remaining
phase premise on the consumed finite source surface:

- The runner `frontier_hierarchy_observable_principle_from_axiom.py`
  verifies the exact-algebra closure for the selected candidate generator on
  the finite staggered source block.
- The det-positivity lemma
  [`REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md`](REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md)
  proves that this finite real source branch has `det(D+J) in R_{>0}` on
  the positive source cone and local derivative patch. (That lemma is the
  self-contained fact this note consumes; the fuller application is the plain
  reference `OBSERVABLE_PRINCIPLE_POSITIVE_SOURCE_CONE_P2_ELIMINATION_NARROW_THEOREM_NOTE_2026-06-06.md`,
  cited non-load-bearing to avoid a parent↔application audit-graph cycle.)
- Therefore the old P2 distinction between phase-blind and phase-sensitive
  scalar generators is vacuous on the branch this note consumes. Global P2
  outside that branch is not claimed.

**Current load-bearing statement (this note):**

> Given Record/P1 finite scalar additivity, a finite real staggered source
> block, real diagonal scalar sources on the positive source cone or
> local invertible derivative patch, and the declared readout-identification
> Boundary (T1-d), with zero-source baseline normalization
> fixed conventionally, the four exact-algebra identities (1-4) in the Claim
> Scope hold on the exact minimal hierarchy block.

**Out-of-scope for this note (cited only):**

> Global/off-sector phase-blindness. Numerical `v` readout. Hierarchy
> baseline `M_Pl * alpha_LM^16`. Measurement comparator `v_meas`.

Downstream rows that cite this note as authority must therefore cite it
in scoped form: *"…follows from `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE`
on the Record/P1 finite real-positive source surface…"*. Off-sector uses
that require arbitrary complex source phases must cite a separate global P2
authority or remain conditional.

Re-audit trigger (per `notes_for_re_audit_if_any` in the audit ledger):

> Re-audit if scalar additivity and CPT-even phase-blindness are
> accepted by upstream independent review, **or if the source is
> narrowed to a conditional exact-algebra statement**.

This note had already implemented the second branch. The 2026-06-04 repair
adds the new premise fact that scalar additivity, in this row's narrow finite
record sense, is now supplied by Record as an axiom premise. That premise
support is not a bounded-status source. The audit row may now be re-evaluated
against the Record/P1 plus positive-source-cone load-bearing statement above
rather than the unconditional 2026-04-13 framing, the stale P1-as-Tier-A
framing, or the older P2-conditional framing.

## Runner-local consistency checks for source regularity and normalization

### 2026-06-06 positive-source-cone bridge

The load-bearing P2 repair is the det-positivity lemma (the self-contained
`det(D+J) in R_{>0}` fact this note consumes):

- Lemma (load-bearing):
  [`REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md`](REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md)
  and its runner
  [`scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py`](../scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py).
- Application (plain reference, **not** a load-bearing dependency, to avoid a
  parent↔application audit-graph 2-cycle): the fuller positive-source-cone
  elimination is `OBSERVABLE_PRINCIPLE_POSITIVE_SOURCE_CONE_P2_ELIMINATION_NARROW_THEOREM_NOTE_2026-06-06.md`
  with runner `scripts/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.py`.

It proves and checks that for `D^T=-D` real antisymmetric and real diagonal
scalar sources, `det(D+J)` is real-positive on the positive source cone and
on a small local derivative patch around an invertible block. Thus
`log det`, `Re Log det`, and `log|det|` agree on the branch used by the
source-response formulas.

As of 2026-06-10 the consumed lemma facts are not citation-only: the runner's
Part 8 **recomputes** them on the actual runner blocks — L1 cone positivity
(`slogdet` sign `= +1` on non-uniform positive diagonal sources), the L1
mechanism (`B = S^{-1/2} D S^{-1/2}` real antisymmetric and
`det(I+B) = prod(1+lambda_k^2) >= 1`), the L2 Neumann hypothesis
(`||D^{-1}J|| < 1` for every source magnitude this runner uses), and L2 patch
positivity for signed sources inside the Neumann patch. The Cauchy-uniqueness
fact L3 remains cited from the lemma; its continuity-on-`R_{>0}` hypothesis is
part of the declared readout-identification Boundary (T1-d), matching the
lemma's L3 hypothesis exactly.

### Historical 2026-05-09 candidate checks

The 2026-05-07 conditional scope originally admitted four bridge premises
P1-P4. The 2026-06-04 Record axiom retires the P1 scalar-additivity part
only in this row's narrow finite record-additivity use. The 2026-05-09 runner checks
showed that the selected candidate
`W = log|det(D+J)| - log|det(D)|` has the expected source-evenness,
finite-block regularity near zero source, and baseline-shift invariance on
the registered staggered block. Per later audit feedback, those checks alone
did **not** derive the broader scalar-generator classification premise P2.
After the 2026-06-06 repair, they are kept as consistency checks for the
real-positive source branch rather than as a substitute for a global P2 theorem;
the runner verifies them as Part 7
(`test_candidate_consistency_checks`).

### Source-branch consistency check (source evenness of the selected candidate)

The staggered Cl(3) framework's lattice Dirac operator `D` on the exact
minimal hierarchy block is **real anti-Hermitian** in the registered
`CPT_EXACT_NOTE` construction (see "T operator: complex conjugation acts
trivially on H because all staggered phases and hoppings are real" and
`D + D^dagger = 0`). Real anti-Hermitian on a complex space is
equivalent to **real anti-symmetric** (`D^T = -D`) when `D` has zero
imaginary part. For any real-symmetric source `J = j I`:

- `(D + J)^T = D^T + J^T = -D + J = -(D - J)`;
- `det((D + J)^T) = det(D + J)` (transpose preserves determinant);
- `det(-(D - J)) = (-1)^n det(D - J)` where `n = dim(D)`.

On the runner's even-dim staggered blocks (`n = 16, 32`), `(-1)^n = 1`,
so `det(D + jI) = det(D - jI)` exactly. In particular
`|det(D + jI)| = |det(D - jI)|` is forced, giving `W(j) = W(-j)`
exactly. (For odd `n`, the equality becomes `det(D + jI) = -det(D - jI)`,
which still implies `|det(D + jI)| = |det(D - jI)|`, so `W` is even
regardless of dimension parity.)

This is a **structural candidate check** for the selected `log|det|`
generator, not a derivation of the full physical-principle premise that
all admissible scalar bosonic generators must be continuous functions of
`|Z|` alone. The runner's Part 7 verifies:

- `||Im(D)||_F = 0` and `D + D^dagger = 0` on the runner blocks
  (so `D` is real anti-Hermitian);
- `Re(spec(D)) = 0` (purely imaginary spectrum, the sharper algebraic
  consequence);
- `|det(D + jI)| = |det(D - jI)|` to machine precision for several
  values of `j` (so `W` is automatically even);
- the determinant equality `det(D + jI) = det(D - jI)` on the
  even-dim runner blocks (the unsigned form of the source-flip
  identity that underlies CPT-evenness; both sides are real on real
  `D`, so the conjugation form `det(D + jI) = conj(det(D - jI))`
  follows trivially from realness).

Therefore the selected candidate passes the expected source-evenness test on
the runner block. The 2026-06-06 bridge adds the stronger real-positive
determinant statement needed to remove P2 from the consumed source branch.

### P3 consistency check (finite-block regularity near zero source)

For finite-dimensional `D`, the map

`j -> det(D + jI) = sum_{k=0}^{n} c_k(D) j^k`

is a polynomial in `j` of degree `n = dim(D)`, with coefficients
`c_k(D)` fixed by the elementary symmetric functions of the eigenvalues
of `D`. Therefore:

- `j -> det(D + jI)` is real-analytic on all of `R`;
- `j -> log|det(D + jI)|` is real-analytic on every neighborhood of
  `j` where the polynomial is nonzero;
- in particular, on a neighborhood of `j = 0`, analyticity holds iff
  `det(D) != 0` (i.e., `D` is invertible);
- `D` is invertible on the runner block (verified by `sigma_min(D) > 0`),
  so `W(j) = log|det(D + jI)| - log|det D|` is real-analytic in a
  neighborhood of the origin and the multiplicative-to-additive
  functional equation has a real-analytic (hence continuous) `W`
  satisfying it. Cauchy's functional-equation uniqueness theorem
  then forces `W(r) = c log r`. The zero-source subtraction is a separate
  extensive baseline convention, not an additive constant in the Cauchy
  solution.

The runner's Part 7 verifies `D` is invertible on the staggered block and
that the small-`j` Taylor ratio `W(j) / j^2` converges to the exact
quadratic coefficient `A(L_t)`, consistent with analyticity of the
selected candidate in the checked neighborhood.

This check supports the finite-block candidate algebra. Together with the
positive-source-cone bridge, it supplies the finite local branch on which
the source derivatives are taken.

### P4 consistency check (canonical generator normalization and zero-source baseline)

The functional equation `W(r_1 r_2) = W(r_1) + W(r_2)` with continuous
`W: R_+ -> R` has solution `W(r) = c log r`; an additive constant would
violate exact additivity unless it is zero. The two conventions used here are
therefore not both parameters of the Cauchy solution: the overall scale `c`
selects a representative of the logarithmic generator family, and the
zero-source subtraction is an explicit extensive baseline convention applied
after selecting the generator:

- `c = 1` (canonical natural log, since `W` is consumed as a real
  scalar generator without dimensional rescaling on the runner block);
- zero-source baseline subtraction `- log|det D|`, enforcing `W(0) = 0` for
  the source coordinate `J=0`.

Both are conventional choices. A post-selection baseline shift does **not**
propagate to local source-derivative observables: any source-independent
shift `C` gives `W_alt = W + C` and `d/dj W_alt = d/dj W` exactly. This
does not make `+C` a solution of the multiplicative Cauchy equation; it only
records that source-derivative observables are insensitive to the chosen
zero-source reference. The runner's Part 7 verifies this additive-shift
invariance for the zero-source-baseline convention.

#### `c` is a scale convention, not a physical content choice

The overall scale `c` rescales the generator and (in unrestricted form)
its source-derivative observables, so a naive reading might treat
`c = 1` as a physically-loaded choice. The four in-scope identities
above are however **c-equivariant** in the precise sense that their
algebraic-structural content is invariant under `W -> c W` rescaling:

- **Theorem 1 (selected generator family).** Under Record/P1, the declared
  Boundary, and L3 on the real-positive source branch, the continuous
  additive solutions form exactly the one-parameter family
  `{W_c = c · log det(D+J) : c in R}` (the full Cauchy solution family,
  including the degenerate `c = 0` and negative-`c` members). Since
  `det(D+J)>0` on this branch, this is the same as
  `{W_c = c · log|det(D+J)| : c in R}`. The choice `c = 1`
  picks one representative of that family; any other `c`
  representative satisfies the same selection and the same Record/P1
  identities, modulo the same zero-source baseline convention and a global
  scale on source derivatives. Theorem 1
  in §"Claim scope" should therefore be read as fixing the
  generator family, not a single generator and not the absolute scale:
  "uniqueness" means uniqueness of the family, with `c = 1` conventional.

- **Theorem 2 (local source derivatives).** With `W_c`, local
  source-derivative observables carry a global `c` prefactor:
  `∂W_c/∂j_x = c · Re Tr[(D+J)^(-1) P_x]`, and similarly for the
  second derivative kernel. Ratios of local observables, locality /
  connectedness / boson-evenness of the kernel, and the index
  structure of the source-derivative operators are all `c`-
  independent. Only the absolute observable scale carries the `c`
  factor.

- **Theorem 3 (Matsubara closed-form identity).** The closed-form
  identity is `c`-equivariant: `W_c(j) = c · A(L_t) j^2 + O(j^4)`,
  with `A(L_t)` itself `c`-independent. Both sides scale together
  under `W -> c W`, so the identity holds for every `c` in
  the family with the same `A(L_t)`.

- **Theorem 4 (Klein-four invariance + `L_t = 4` selector).** For any
  nonzero representative, the
  Klein-four group acts on the source `J`, not on the generator
  scale. The orbit-resolution argument that selects `L_t = 4` as
  the minimal resolved APBC orbit is therefore manifestly
  independent of the nonzero value of `c`. The degenerate `c = 0`
  member is the null readout and carries no source-curvature kernel, so it is
  not the representative used for the selector claim.

In short, the in-scope identities (1)-(4) are statements about the
algebraic / index / orbit structure of `W_c`, all of which are
preserved under `c`-rescaling. The `c = 1` choice fixes only the
absolute scale of source-derivative observables, and that absolute
scale enters this note only through the §"Consequence for `v`"
comparator readout, which is already declared out-of-scope.

P4 is therefore a true normalization convention with respect to this
note's in-scope content: rescaling `c` leaves Theorems 1-4 invariant
as algebraic-structural statements. The physical generator scale
question — which `c` (if any) is preferred by retained framework
theorems, and whether absolute observable normalization is fixed
elsewhere in the framework — is out-of-scope for this row and is
recorded as an open question for the audit lane.

### What remains outside this row: global/off-sector P2

Record/P1 finite scalar additivity is now supplied by `minimal_axioms` when a
row uses only additivity over disjoint finite record collections. On the
finite real-positive source surface consumed here, the separate P2 premise is
removed by the positive-source-cone bridge. For arbitrary complex source
sectors where `arg det(D+J)` is nonzero, global phase-blindness remains outside
this row and must be supplied by a separate authority or left conditional by
the consuming row.

#### Record/P1 and global/off-sector P2 now have different premise character

- **Record/P1 finite scalar additivity** is supplied by Record only in the
  narrow sense stated in
  [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md). This axiom
  premise support is chain-satisfying for dependency closure, but it is not a
  `retained_bounded` audit status and does not promote downstream rows. The
  older P1 no-go portfolio remains useful history for why this was a genuine
  premise, but it is no longer a Tier-A admission for rows that need only
  finite scalar record additivity.

- **Global/off-sector P2** is **not** in the Tier-A registry and is not part of
  Record. This note does not admit it for the consumed source branch; it marks
  it out of scope. Downstream rows that load-bear on arbitrary complex source
  phase-blindness must keep that conditional citation explicit or cite another
  bridge.

This note closes only the P2 role on its finite real-positive source branch.
The audit lane is the authority on whether that repair is enough for this row.

#### Existing candidate retirement path for P2

A candidate derivation of the phase-positive side of P2 from a qubit-trace
generating functional is recorded in (backticked to avoid load-bearing the
parent on an `unaudited` row)
`OBSERVABLE_PRINCIPLE_P1_P2_FROM_QUBIT_TRACE_NOTE_2026-05-20.md`.
That note proposes that

```
W_qubit[J] := log Tr_A(e^{-(H + J)}) - log Tr_A(e^{-H})
```

automatically satisfies trace-tensor additivity on disjoint qubit regions and
the phase-positive side of P2 (because `Z[J]` is manifestly real-positive for
self-adjoint `H + J`). The additivity part is now superseded here by Record in
the finite scalar record sense. When that note is independently accepted,
transferring the phase-positive P2 retirement back to this note's
`W = log|det(D+J)|` formulation remains conditional on the admitted Grassmann /
Berezin bridge between the qubit-trace and Grassmann-determinant surfaces, per
the qubit-trace note's own scope.
This cross-reference is informational only and does **not** promote
either row.

### Updated load-bearing statement

> **Given Record/P1 finite scalar additivity, a finite real staggered source
> block, real diagonal scalar sources on the positive source cone or local
> invertible derivative patch, and the declared readout-identification
> Boundary (T1-d)**, with the conventional `c = 1` representative
> and zero-source baseline fixed conventionally, the four exact-algebra
> identities in §"Claim scope" hold on the exact minimal hierarchy block.

Downstream rows that cite this note may now do so as
*"…follows from `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE` on the Record/P1
finite real-positive source surface…"*.

This narrowing does **not** promote audit status. The conditional surface
is for independent re-audit, and the audit lane remains the only status
authority. The
`notes_for_re_audit_if_any` re-audit trigger named two alternatives:
derive the missing bridge theorem, or narrow the source to the conditional
surface. This source now supplies the missing finite-source bridge for the
branch it consumes. It does not derive scalar additivity beyond the narrow
Record axiom and does not derive global/off-sector phase-blindness.

## Out of scope (admitted-context to this note)

The following stronger or upstream-dependent statements are explicitly
**NOT** claimed by this note. They live in separate authority notes and
enter this note only as admitted-context:

- **Canonical hierarchy baseline.** `M_Pl * alpha_LM^16 = 254.6432... GeV`
  comes from the canonical-constants chain rooted in
  `PLAQUETTE_SELF_CONSISTENCY_NOTE.md` (and downstream normalization).
  This note does not derive that baseline; it consumes it as
  admitted-context for the §"Consequence for `v`" numerical readout only.
  Whether that baseline is independently ratified is decided by the audit
  lane on its own authority row.
- **Measurement comparator.** `v_meas = 246.22 GeV` is a PDG-style
  measurement comparator. It is **never** consumed as a derivation input
  by this note's in-scope claims; it appears only in the comparator
  role inside the out-of-scope §"Consequence for `v`" subsection.
- **Beyond-Record scalar additivity.** `W[J_1 ⊕ J_2] = W[J_1] + W[J_2]`
  is used here only as finite scalar record additivity over independent
  disjoint record collections, as supplied by Record. Any broader physical
  observable classification, arbitrary subsystem independence principle, or
  non-record scalar generator additivity remains outside this note.
- **Global/off-sector phase-blindness.** For arbitrary complex source sectors,
  the premise that the scalar bosonic generator depends on `|Z|` rather than
  the fermionic phase of `Z` is not a theorem of this note. It is unnecessary
  on the finite real-positive source branch because `arg det(D+J)=0` there.

In-scope content of this note is the finite real-source observable map:
Grassmann factorization -> positive determinant source branch -> declared
readout-identification Boundary -> additive generator family
`{c log det(D+J) : c in R}` with conventional representative
`W = log|det(D+J)|` -> local source-derivative formulas -> Matsubara
closed-form identity -> Klein-four invariance and `L_t = 4` selector (exact
counting). The physical numerical `v` readout depends on the admitted
upstreams named above and remains comparator-only here.

## Changelog

- **2026-04-13** — original note (unconditional baseline-to-observable framing).
- **2026-05-07 / 2026-05-25** — scope narrowed to the conditional
  exact-algebra statement per the 2026-05-02 conditional-repair finding;
  headline narrowed to the finite-algebra `log|det(D+J)|` generator step
  given the P1/P2 admissions.
- **2026-06-04 / 2026-06-06** — Record-axiom repair (P1 supplied by
  `minimal_axioms` in the narrow finite scalar record-additivity sense) and
  positive-source-cone repair (P2 eliminated on the consumed real source
  branch via the det-positivity lemma).
- **2026-06-10** — boundary-declaration repair (this revision):
  (a) the readout-identification bridge premise — previously consumed
  silently inside the Record citation — is declared as the single explicit
  Boundary (header and T1-d): `W` is a continuous function of
  `Z = det(D+J)` alone on all of `R_{>0}` (the L3 Cauchy-domain content
  included), and disjoint independent source blocks register as disjoint
  records; the axiom memo excludes this identification from Record content,
  so it is a premise, not a consequence;
  (b) Theorem 1 restated as the five-input chain T1-a..T1-e (computed
  Berezin factorization; runner-recomputed lemma facts L1/L2; Record
  additivity as axiom premise; the declared Boundary; lemma fact L3);
  (c) the uniqueness overclaim fixed: the selected object is the generator
  family `{c log det(D+J) : c in R}` with `c = 1` conventional (claim
  scope, headline, c-equivariance section);
  (d) stale axiom citations updated to the current memo
  `MINIMAL_AXIOMS_2026-06-05.md` (the ledger's `minimal_axioms` target);
  (e) runner upgrades: Theorem-2 derivative trace formulas residual-checked
  against central finite differences on a non-uniform positive-cone source
  (Part 2); Matsubara closed form, exact spectral multiset, and pair-product
  determinant identity verified at `u_0 = 0.9` and `1.17` (Part 3); the
  `L_t = 4` selector backed by the exact counting argument (Part 4); the
  consumed lemma facts L1/L2 recomputed on the runner blocks, including the
  `||D^{-1}J|| < 1` Neumann hypothesis for every source magnitude used
  (new Part 8); the hard-coded `canonical_plaquette_surface` helper now
  imported locally inside the out-of-scope Part 5 comparator only, which
  contributes zero PASS gates (comparator numbers unchanged:
  `v_pred = 246.282818290129 GeV`, `+0.025513%`).
  SCORECARD: 37 pass, 0 fail out of 37, deterministic (fixed seeds), ~0.1 s.
