---
claim_id: admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_bounded_theorem_note_2026-08-23
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_RANK_TWO_SCALAR_TRANSPORT_COUNTEREXAMPLE_BOUNDED_THEOREM_NOTE_2026-08-23.md
claim_type: bounded_theorem
claim_scope: "on the committed Block-170 reflection-pairing form F_T(s_t) = Herm(Sel_S^T r_T Q_T(s_t) Sel_S), with Q_T = m Hq_T + Kq_T, at the two retained finite antiperiodic cover extents 8x4 and 12x4, fixed slice c = 1, region pin on the two links incident to c, sigma = s_x = 3/5 and m = 1, selecting ambient rows S = (4,5,6,7,8,9,10,11), and reading compression in the standard isometric sense X^dag F_T X. THE VERDICT: the literal Block-176 successor thesis that positive transport-sensitive scalar readouts occur exactly at rank one, with every rank >= 2 compression blind or indefinite, is FALSE on both committed fixtures. The exact rank-two isometry X = [x_0,x_2], x_0 = (4e_0+3e_4)/5 and x_2 = (4e_2+3e_6)/5, gives X^dag X = I_2 and X^dag F_T(s_t) X = (114/125 + 171 s_t/250) I_2 at both extents. It is positive definite for s_t > -4/3 and transport-sensitive with derivative 171/250; between s_t = 1/8 and 1/2 it changes by 513/2000. This is a finite-fixture exact counterexample and a route-pruning result. It does NOT select a physical readout, derive the Born rule, prove completeness of the affine effect class, exclude determinant/exterior-power or other non-affine non-convex categories, establish an infinite-volume statement, retire an axiom or obligation, justify an axiom amendment, or move a TOE percentage."
depends_on:
  - admissibility_dirac_kahler_conditional_symmetric_power_theorem_note_2026-08-23
runner: scripts/admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_2026_08_23.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: admissibility_dirac_kahler_complex_structure_synthesis_bounded_theorem_note_2026-08-23
target_blocker_text: "PROVE OR REFUTE THE SCALAR-SECTOR THEOREM. Within the committed reflection-pairing structure, do positive AND transport-sensitive readouts exist EXACTLY at rank one -- the matrix-element level -- with every rank >= 2 compression blind-or-indefinite?"
source_of_blocker_text: next_trace_action
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Do not continue the literal rank-one-only compression thesis. If the readout route continues, first derive and state an exhaustive presentation-invariant operational readout category; determinant or exterior-power subclasses may be tested only as bounded supplied categories. Run the already specified holomorphic interference discriminator J(a) only if its transport carrier is controlled. At portfolio level, pivot the main science budget to the Wilson-Q discriminator rather than another rank-family scan."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-177 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the load-bearing result is an exact symbolic matrix identity reconstructed from the committed Block-170 fixture at both retained cover extents. The isometry, compressed form, determinant, positivity interval, derivative and two-point gap are exact SymPy expressions with no floating-point input. The theorem is bounded because only two finite extents, one carrier family, one selected eight-row support and the standard isometric-compression reading are tested. The generic convex-affine admixture lemma is exact linear algebra, but it does not establish that Nature's full physical readout category is affine, convex or exhausted by PSD effects."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Rank-two scalar transport counterexample — the literal rank-one-only successor dies

**Date:** 2026-08-23

**Runner:** `scripts/admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_2026_08_23.py`

**Independent checker:** `scripts/admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_independent_check_2026_08_23.py`

**Parent:** Block 176, the complex-structure synthesis

**Standing:** exact bounded counterexample; nothing registered or adopted.

## Result in one paragraph

Block 176 deliberately posed a kill test: if a positive, transport-sensitive
rank-two compression exists, report it and abandon the proposed rank-one-only
scalar theorem. It exists at both committed extents. With local basis
`e_0,...,e_7` in the parent's selected row order, define

\[
x_0={4e_0+3e_4\over5},\qquad
x_2={4e_2+3e_6\over5},\qquad X=[x_0,x_2].
\]

Then, exactly,

\[
X^\dagger X=I_2,
\qquad
X^\dagger F_T(s_t)X
=\left({114\over125}+{171\over250}s_t\right)I_2
\]

for both `8x4` and `12x4`. This is rank two, scalar, positive definite for
`s_t > -4/3`, and not transport-blind. At the two parent's retained transport
values,

\[
F_X(1/8)={399\over400}I_2,
\quad
F_X(1/2)={627\over500}I_2,
\quad
{1\over2}\operatorname{tr}[F_X(1/2)-F_X(1/8)]={513\over2000}.
\]

The derivative of the half-trace is `171/250`, and

\[
\det F_X(s_t)={3249\over62500}(3s_t+4)^2.
\]

Therefore the literal successor is refuted on its own committed fixtures. This
is useful route pruning, not TOE closure.

## Relation to parallel Block 177

The parallel Block 177 conditional symmetric-power theorem arrived while this
counterexample was being packaged. The two results are compatible and are now
stacked in that order. Block 177 proves that the **full** displayed one-particle
kernel is indefinite and that symmetric powers inherit an indefinite minor,
conditional on a named quasi-free grading premise. This block proves that the
same indefinite full form contains an exact two-dimensional **positive**
subspace whose isometric compression is transport-sensitive. An indefinite
Hermitian form can have positive subspaces, so neither calculation overturns
the other.

The combined cut is sharper than either alone: Block 177's conditional
sector-indefiniteness survives, while the older claim that **every** rank-two
compression must be blind or indefinite does not. Block 177 already withdraws
unconditional Born-readout uniqueness; this counterexample independently
prevents that stronger wording from returning through the compression route.

## Provenance and what was actually reconstructed

The runner imports the landed
`scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py` machinery.
Its `Bench` constructs

\[
F_T(s_t)=\operatorname{Herm}
\left(\mathrm{Sel}_S^\top r_T Q_T(s_t)\mathrm{Sel}_S\right),
\qquad Q_T=mH_{q,T}+K_{q,T},
\]

after the committed region pin and carrier substitution. In both extents the
selected ambient rows are exactly
`S = (4,5,6,7,8,9,10,11)`, so the displayed local basis has an unambiguous
meaning. The primary runner reconstructs the full `8x8` form before applying
`X`; it does not insert the `2x2` answer as its input.

There is a second consistency fact, and it is not promoted beyond its role.
Block 175's declared coarse effects already include native rank-two projectors,
for example `E_12 = diag(0,1,1,0)`, with a strictly positive trace reading on
its exact classical density. That does not by itself prove transport
sensitivity; it only shows that rank-two effects are not alien to the committed
effect vocabulary.

## The convex-affine obstruction

The explicit fixture is stronger than a generic warning, but the warning
explains why the failed thesis was structurally fragile. For an affine effect
readout

\[
R_E(g)=\operatorname{Tr}[E W(g)],
\]

let `D = W(g)-W(0)`. If a rank-one effect `P` is sensitive, then
`d = Tr(PD) != 0`. For any orthogonal positive effect `Q`,

\[
E_\epsilon=P+\epsilon Q,\qquad
\Delta R_{E_\epsilon}=d+\epsilon\operatorname{Tr}(QD).
\]

For positive `epsilon`, `E_epsilon` has rank at least two, and its response is
nonzero for all sufficiently small `epsilon` except at most one tuned value.
Dividing by `Tr(E_epsilon)` does not turn a nonzero numerator into zero. Thus a
convex PSD-effect class closed under small positive admixtures cannot make
transport sensitivity rank-one-only.

This lemma does **not** forbid non-affine or non-convex categories such as
determinants, exterior powers or a supplied extreme-effect-only domain.

## N1 — alternative-route enumeration

The negative conclusion is scoped to the literal successor and, generically,
to affine convex PSD effects. The following escape routes were examined:

1. **ATTEMPTED — pure or extreme effects only.** This avoids convex admixture,
   but selects rank one by restricting the domain; it does not classify all
   physical readouts.
2. **ATTEMPTED — equal-weight orthogonal projections only.** In dimension at
   least three, blindness of every rank-two projection forces the quadratic
   response to vanish, so some rank-two sensitivity follows from any rank-one
   sensitivity. A two-dimensional traceless exception remains live.
3. **ATTEMPTED — determinant or exterior-power readouts.** These genuinely
   evade affinity. They remain a bounded route only if the nonlinear category
   is independently derived, exhaustive and presentation-invariant.
4. **ATTEMPTED — a superselection rule forbidding support mixtures.** This can
   exclude `E_epsilon`, but the rule is then the missing physical premise.
5. **ATTEMPTED — rank modulo dilation or refinement.** This could repair
   presentation dependence, but no exhaustive naturality theorem is supplied.
6. **ATTEMPTED — nonlinear normalized contrast.** A contrast can be engineered
   to vanish at higher rank, but that supplies the selection functional.

These live alternatives are why no universal no-go is claimed.

## N2 — wall-independence audit

Four walls are kept distinct:

- `W_R`: derive the complete operational readout/effect domain, including its
  mixture, coarse-graining and presentation-equivalence rules;
- `W_T`: identify the imposed chart dial with a physical transport carrier;
- `W_A`: show that the committed sesquilinear action class is exhaustive;
- `W_J`: obtain a nonzero controlled holomorphic interference signature.

They are pairwise independent. Closing `W_R` neither identifies transport nor
completes the action nor makes `J` nonzero. Closing `W_T` does not choose a
readout or action. Closing `W_A` does not choose a readout or certify the dial.
A measured `J != 0` would not prove any class complete. Rank and dilation
questions are included in `W_R`, not counted as a fifth wall.

## N3 — hidden-wall scan

The exact counterexample assumes the parent's standard isometric compression
language and uses its supplied finite fixtures, reflection, support, action and
transport dial. It does not silently promote any of those to axioms or to facts
about Nature. The generic lemma separately assumes affinity in the effect,
convex PSD closure and a fixed transport difference or derivative. The physical
event-to-effect map, global positivity of the uncompressed form, rank under
auxiliary dilation, action completeness and physical meaning of the chart dial
remain unsupplied.

## N4 — residual matching

- The parent says explicitly that a sensitive rank-two PSD compression kills
  its candidate. The `X^dag F_T X` witness answers exactly that residual.
- The parent calls the holomorphic `J(a)` arm unrun. This result does not cite
  the counterexample as a substitute for `J`.
- The parent's sesquilinear-only limitation maps to `W_A`, not to an
  all-actions theorem.
- Block 175's union effects support only the statement that rank-two projectors
  already occur in the effect vocabulary; they are not used to prove this
  transport response.
- Effect-Gleason and probability-simplex work are cross-cycle analogies only;
  the load-bearing result here is direct exact matrix algebra.

## N5 — rhetoric audit and resolution level

- **per_element:** proved exactly for the displayed isometric compression and
  for the convex-affine admixture lemma; nonlinear categories remain open.
- **per_site:** reconstructed on the selected eight-row finite reflection form
  at the two committed extents; no full site-effect algebra is derived.
- **per_mode:** proved transport-sensitive with respect to the supplied `s_t`
  dial; the dial's physical carrier identification remains open.
- **per_block:** the literal Block-176 rank-one-only successor is falsified.
- **lattice_wide:** not established; two finite extents are not a limit.
- **whole TOE:** no obligation or axiom is retired and no percentage moves.

Safe wording is: **“The literal rank-one-only successor fails under standard
isometric compression on both committed fixtures, and it also cannot hold in
an affine convex PSD-effect class.”** Unsafe wording is: **“No scalar-sector
principle can select a Born readout.”**

## N6 — partial positive closure paths

The counterexample leaves several honest positive programs:

- derive a complete physical effect algebra, then apply the existing
  additivity/trace-form machinery;
- prove a determinant or exterior-power theorem on a derived non-convex
  category;
- derive squared amplitude from orthogonal-alternative additivity rather than
  assuming bilinearity;
- run the controlled holomorphic `J(a)` arm;
- identify the physical transport carrier;
- classify action/readout pairs including auxiliary and antilinear extensions.

No statement that a new axiom is required is justified by this block.

## N7 — hostile-reviewer steelman

A strong objection is that Block 176 may have intended “compression” to mean a
determinant or exterior-power scalar of an exact-rank invariant block, not the
standard isometric matrix compression used here. Convex mixtures would then be
inadmissible, and a two-dimensional traceless sector could make the unique
full-rank trace blind while rank-one matrix elements remain sensitive.
Reflection positivity and composition might privilege a determinant-line
pairing.

That steelman defeats a universal impossibility claim. It does not rescue the
literal text, which neither defines such a narrow category nor supplies a
reason to exclude this exact `X`. A repaired theorem would need to derive that
category, prove it exhaustive and invariant under equivalent presentations,
and then demonstrate a controlled nonzero physical signature.

## N8 — cross-cycle echo

Earlier readout cycles obtained trace form only after enlarging to a complete
effect/menu domain and imposing normalization and additivity. Those results
show the right theorem shape: a representation theorem can follow from a
supplied full effect algebra, but it does not derive which effects are physical,
the state, the action or the transport map. Likewise, phase invariance and
multiplicativity leave `|Z|^p`; selecting `p=2` needs an independent
orthogonal-alternative additivity or equivalent Hilbert-space premise. This
mechanism has been considered here. It supports an exhaustive effect-algebra
program, not the failed rank-one-only exclusion.

## Decision cut

Stop spending campaign time on the literal rank-one-only compression thesis.
The exact counterexample is the requested kill condition, not an invitation to
search for a friendlier fixture. A narrower determinant/exterior-power theorem
may proceed only after its category is physically derived and stated. The main
portfolio should now move to the Wilson-`Q` discriminator, while the readout
lane retains `W_R`, `W_T`, `W_A` and `W_J` as named independent walls.

**TOE:** zero axiom retirement; zero obligation retirement; zero TOE movement;
no TOE percentage moves; retained-positive end-to-end theory count remains
zero.
