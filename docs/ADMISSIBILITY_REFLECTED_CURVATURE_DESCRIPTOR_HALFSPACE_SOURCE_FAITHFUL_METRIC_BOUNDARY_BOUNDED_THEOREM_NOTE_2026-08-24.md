---
claim_id: admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "For the supplied twenty-two-edge reflected-curvature action at mu=1/1024, in the odd y/z-reflection six-edge plus one-Ward border at spatial momentum (pi/2,0,0), the declared structural-zero threshold gives a regular degree-four 7-by-7 polynomial descriptor with seven zero, fourteen finite-nonzero, and seven infinite generalized eigenvalues. Deflating the endpoint chains leaves a minimal three-mode stable scalar TT response. Every Hermitian metric that makes that response self-adjoint and preserves the same TT source/readout is uniquely indefinite for both one-step and even-step transfer; direct inverse-border moments independently have negative Stieltjes/Hankel eigenvalues. This is a bounded numerical/algebraic infeasibility result for the exact supplied action, momentum, contour response, and source/readout only. A different action-derived physical half-space response, source/Record map, action, other momentum, continuum theorem, gravity failure, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
parents:
  - admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_bounded_theorem_note_2026-08-23
  - admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_bounded_theorem_note_2026-08-14
upstream_dependencies:
  - minimal_axioms
  - admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_bounded_theorem_note_2026-08-23
  - admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24.py
---

# Reflected-Curvature Descriptor Half-Space Source-Faithful Metric Boundary

**Type:** `bounded_theorem`

**Status:** bounded numerical/algebraic support; unaudited; no canonical axiom
is edited.

**EXACT OS/SELF-ADJOINT RESPONSE VERDICT: BOUNDED_INFEASIBLE.**

**PHYSICAL_BOUNDARY_RESPONSE: OPEN.**

**GRAVITY_VERDICT: OPEN.**

TOE accounting: **zero obligation retirement, zero percentage movement, and
no axiom is amended**. The advance is a sharp route decision: removing the
descriptor endpoint chains does not turn the same TT response positive.

## Result Up Front

The previous odd-sector calculation found fourteen finite nonzero Laurent
roots and three stable roots that couple to one local TT-plus row. It left a
high-value escape open: perhaps zero and infinite descriptor chains were being
mistaken for dynamical states, and a correct half-space reduction would expose
a positive finite transfer.

This note executes that escape. For the supplied action and one declared
momentum, the endpoint chains can be separated cleanly. They account for seven
zero and seven infinite generalized eigenvalues. The fourteen finite modes
remain, and the exact scalar TT response on its stable source-visible part has
the minimal realization

\[
 A_s=\operatorname{diag}(z_1,z_2,z_3),\qquad
 b=(1,1,1)^T,\qquad c=(w_1,w_2,w_3)^T,                 \tag{1}
\]

with

| mode | `z_i` | `w_i` |
|---|---:|---:|
| alternating | `-2.4543907e-5` | `+1.5176104e-4` |
| negative-weight | `+2.9116903e-4` | `-2.1745073e-4` |
| dominant TT | `+2.66171727e-1` | `+5.81884812e-1` |

Both controllability and observability have rank three. Thus the middle pole
is not a source-dark constraint mode, and the negative root is not an
unreachable auxiliary mode.

For a source-faithful OS/self-adjoint Hilbert realization of the same response,
a positive Hermitian metric `H` must obey

\[
 A_s^\dagger H=H A_s,\qquad H b=c.                    \tag{2}
\]

The three roots are real and distinct, so the first equation forces `H` to be
diagonal. The second then forces

\[
 H=\operatorname{diag}(w_1,w_2,w_3).                 \tag{3}
\]

Its inertia is one negative and two positive. For a positive one-step
transfer, `H A_s` would also have to be positive semidefinite; it instead has
two negative directions. Repeating (2) with `A_s^2` again fixes (3), and
`H A_s^2` retains one negative direction. Therefore neither one-step nor
even-step evolution has a positive H-self-adjoint metric while preserving this
exact scalar source/readout response.

This is stronger than another negative raw Hankel sample and much narrower
than a gravity verdict. It identifies the minimum change required: a physical
completion must derive a different boundary response or source/readout map,
change the action, or abandon the self-adjoint/OS-transfer interpretation.
Merely deleting the hostile pole after seeing its sign is not source-faithful.

## Trace And Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_bounded_theorem_note_2026-08-23
target_blocker_text: "the originally promised terminal route verdict is blocked until a physical reduction/section (or an inner product inducing one) and directed state/source/observable refinement law are supplied"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
exact_response_verdict: bounded_infeasible
physical_boundary_response: open
gravity_verdict: open
next_trace_action: "derive and test an action-built reflection intertwiner/Weyl boundary map that is allowed to change the periodic scalar response, while transporting the TT source and Record readout explicitly"
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs, Types, And Scope

The supplied object is the quadratic twenty-two-edge reflected action

\[
 Q_\mu(q)=Q_{\rm union}(q)+\mu D(-q)^T D(q),
 \qquad \mu=1/1024,                                    \tag{4}
\]

not the distinct nonlinear fifteen-edge action studied in the neighboring
gravity/refinement lane. The calculation uses the odd sector of the `y/z`
swap, one odd Ward column, spatial momentum `(pi/2,0,0)`, the local TT-plus
row, and the inside-unit-disk contour used to reconstruct the periodic
covariance. These are explicit finite-probe inputs, not observational fits.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are contextual. They state
that Admissibility does not choose a Hamiltonian or transfer operator. They do
not supply this action, contour, boundary metric, source dictionary, or Record
clock. The approved scale-reference, kinetic-isotropy, and realized-state
primitives are not load-bearing inputs. The result neither requests nor
licenses a new axiom.

The numerical statements use the coefficient-zero threshold declared in the
runner. Fourier leakage is approximately `4e-17` relative, whereas the
smallest retained structural coefficient is separated by many orders of
magnitude. The root/sign conclusions are therefore reported as bounded
numerical evidence. Equations (2)--(3) are exact finite-dimensional algebra
conditional on those resolved distinct roots and weights.

## Polynomial Descriptor And Endpoint Staircase

Let the reconstructed 7-by-7 odd Ward border be

\[
 \mathcal B(z)=\sum_{r=-2}^{2}B_r z^r,
 \qquad P(z)=z^2\mathcal B(z)=\sum_{j=0}^{4}P_jz^j.     \tag{5}
\]

The runner uses the strong first companion pencil

\[
 \mathsf A=
 \begin{pmatrix}
 0&I&0&0\\0&0&I&0\\0&0&0&I\\-P_0&-P_1&-P_2&-P_3
 \end{pmatrix},\qquad
 \mathsf E=
 \begin{pmatrix}
 I&0&0&0\\0&I&0&0\\0&0&I&0\\0&0&0&P_4
 \end{pmatrix}.                                      \tag{6}
\]

For a finite `z`, the first three block rows of
`mathsf A x=z mathsf E x` give
`x_j=z^j x_0`; the last gives `P(z)x_0=0`. Thus finite generalized
eigenvalues coincide with polynomial roots, without inverting either singular
endpoint coefficient.

At the declared threshold,

- `rank(P_0)=rank(P_4)=2` and `rank(mathsf A)=rank(mathsf E)=23`;
- `det P(z)` has support from degree 7 through degree 21;
- homogeneous QZ gives `(zero, finite nonzero, infinite)=(7,14,7)`;
- the lower block-Toeplitz kernel dimensions at orders one, two, and three are
  `(5,6,7)` at both zero and infinity.

Because the determinant multiplicity is seven and the kernel increments are
`5,1,1`, the endpoint partial multiplicities are

\[
 (3,1,1,1,1)                                           \tag{7}
\]

at both ends. The first three staircase gaps exceed `1e7`. Clearing the
Laurent denominators therefore creates structured endpoint chains, but their
deflation leaves all fourteen finite nonzero modes.

The scalar response removes the endpoint ambiguity independently. Writing

\[
 F(z)=g^T\mathcal B(z)^{-1}g
     ={g^T\operatorname{adj}(\mathcal B(z))g\over\det\mathcal B(z)},
\]

the numerator has Laurent support `-6,...,+6`, whereas the denominator has
support `-7,...,+7`. Consequently `F(z)=O(z)` at zero and `F(z)=O(z^{-1})`
at infinity. Neither endpoint chain is a pole of the scalar TT response.

## Finite Spectrum, Source Visibility, And Minimality

The companion finite spectrum is matched by a global assignment to the
fourteen Laurent determinant roots (seven inside plus reciprocal partners).
The maximum scaled mismatch is below the runner gate. Ward rank is four and
the full action rank is eighteen at all four declared temporal controls.

Let the stable scalar moments be

\[
 m_n=c^T A_s^n b=\sum_{i=1}^{3}w_i z_i^n.              \tag{8}
\]

For distinct roots, the controllability determinant is a Vandermonde product.
It is nonzero. Observability is the same Vandermonde multiplied by the three
nonzero weights, so it too has rank three. Any realization of this rational
response has minimal dimension at least three; a pole can be removed only if
its source or readout coupling vanishes. Neither happens here.

The four other stable determinant roots are one-sided TT-dark or carry a
nonvanishing border multiplier in the supplied computation. They do not enter
(8), and their exclusion is not what creates the negative weight.

## Positive-Metric Feasibility

For real symmetric `H`, equations (2) form a six-unknown linear system. The
runner solves the full system rather than inserting (3). Its coefficient rank
is six, both equation residuals are below `1e-12`, and its eigenvalues reproduce
the three weights. Hence the negative eigenvalue is a finite infeasibility
certificate for `H>0`.

The one-step transfer additionally fails positivity because

\[
 \operatorname{diag}(H A_s)=(w_1z_1,w_2z_2,w_3z_3)
\]

has two negative entries. Blocking to two steps removes the sign of `z_1` but
not the sign of `w_2`; the unique source-faithful even-step metric remains
indefinite and `H A_s^2` has one negative entry.

A nonminimal positive self-adjoint, source-adjoint dilation cannot preserve
the same scalar response either. Any such Hilbert realization would make
every finite scalar moment Gram matrix positive semidefinite. Direct 8,192-point inverse-border
quadrature reconstructs the first nine residue moments at relative error well
below `1e-6`, while the base, shifted one-step, and even-step Hankel tests each
have a negative minimum eigenvalue. This uses the covariance itself, not the
companion eigenvectors, and is therefore an implementation-disjoint check.

### A positive contractive escape

Self-adjointness is load-bearing. Positivity and stability alone are possible.
Let `u=(1,1,1)^T`, `Pi=I-uu^T/3`, and define without fitting

\[
 H_c=\frac{cu^T+uc^T}{3}
     -\frac{u^T c}{9}uu^T+\Pi.                         \tag{9}
\]

Then `H_c u=c` identically. On the computed response, `H_c` is positive
definite with minimum eigenvalue `0.1094414`, and so is the Stein difference

\[
 H_c-A_s^T H_c A_s>0.                                  \tag{10}
\]

whose minimum eigenvalue is `0.1021778`. Thus the same scalar response has a
positive-metric strict contraction. But `||H_c A_s-A_s^T H_c||=0.1085594`,
so this is not an OS/self-adjoint transfer and
does not evade (2)--(3). This constructive counterexample prevents the bounded
result from being misstated as “no positive metric exists.” It also opens a
separate Lorentzian/open-system question: whether a source-faithful unitary
dilation can be physically derived without sacrificing the Hermitian TT
observable interpretation.

## What Changed Scientifically

The constraint-artifact hypothesis is resolved at this probe. Seven zero and
seven infinite roots are endpoint chains, but the source-visible negative
weight belongs to the finite minimal response. Constraint deflation alone is
not the repair.

The remaining constructive seam is now more precise:

1. derive a reflection intertwiner or Weyl/Feshbach boundary map from the
   supplied action's stable/unstable data;
2. transport the full conserved source and TT/Record readout through it;
3. allow the resulting physical half-space response to differ from the
   periodic inside-root response;
4. test positivity, locality, the infrared/Newtonian limit, and exact
   refinement before calling it a gravity law.

A data-built reflection intertwiner repaired a superficially similar
non-Hermitian half-space problem for a different Dirac--Kahler carrier. That
is a live construction pattern, not evidence that it succeeds here. It is the
next highest-leverage campaign because it is the only current route that can
change the boundary pairing without changing the microscopic action by hand.

## Axiom Decision

No contradiction with Lattice, Qubit, Admissibility, or Record is found. The
minimal axioms deliberately do not choose dynamics. This computation therefore
does not justify adding a sign-selection or desired-root axiom.

If the program's intended claim is that the four axioms uniquely derive a
gravity evolution law, the open issue is indeed axiom-level: an independently
motivated dynamics/boundary-selection principle would eventually be needed
unless the law is derived from existing content. But a principle chosen only
to delete this action's negative pole would overfit the failed candidate. The
right immediate move is the action-derived boundary-intertwiner test above;
only after constructive families are compared should owner governance decide
whether a minimal dynamics axiom is scientifically warranted.

## No-Go Discipline Gate

The bounded negative statement is only: **no positive one-step or even-step
H-self-adjoint realization preserves the exact three-pole TT response (8)
while making the fixed readout the H-adjoint of the fixed source at the
declared action and momentum.** It is not a claim about non-self-adjoint
contractions, every boundary response, action, observable, momentum, or
gravity.

### N1 — Alternative route enumeration

| normalized route | attempt and terminal obligation | disposition and evidence | honesty |
|---|---|---|---|
| descriptor/Kronecker deflation | remove zero and infinite chains before judging the finite boundary phase space | endpoint ranks, determinant valuation/degree, homogeneous QZ, and the Toeplitz staircase leave fourteen finite modes and the same three-pole response; primary runner `descriptor-endpoint-chain-separation` | `ATTEMPTED` |
| minimal Hermitian metric | solve self-adjointness and source/readout adjointness on the finite stable realization | the full six-unknown system is unique and has inertia `(1-,2+)`; primary runner `source-faithful-os-self-adjoint-metric-infeasibility` | `ATTEMPTED` |
| positive self-adjoint nonminimal dilation / moment measure | realize the same scalar moments in a larger positive self-adjoint, source-adjoint Hilbert space | the direct covariance has a negative finite Hankel eigenvalue, which no such dilation can reproduce; primary runner `direct-moment-and-even-step-gram-crosscheck` | `ATTEMPTED` |
| exact two-step blocking | replace `A_s` by `A_s^2` while transporting the same source/readout | the unique even-step metric still contains the negative weight and the direct even-step Hankel minimum is negative; the same two primary checks execute both obligations | `ATTEMPTED` |
| source-dark pole removal | test whether the hostile pole is unreachable or unobservable and may be quotiented | controllability and observability both have rank three and every response weight is nonzero; primary runner `source-visible-minimal-stable-response` | `ATTEMPTED` |

These are distinct in primary object and invariant: a polynomial descriptor,
a metric linear system, a scalar moment cone, a blocked transfer, and a
reachability/observability quotient. Five routes are executed; the gate does
not count different agents or restatements as additional routes.

### N2 — Wall-independence audit

The bounded algebra has no hidden admission beyond its explicit fixed object.
For eventual physical gravity, three live escape/selection obligations remain;
they are not presented as proof that the bounded theorem is conditional.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| physical boundary response / physical source-Record map | no | no | yes |
| physical boundary response / action selection | no | no | yes |
| physical source-Record map / action selection | no | no | yes |

The collapsed physical wall set therefore remains those three typed
obligations. Exact refinement is downstream of a positive selected response,
not counted as an independent cause of this finite infeasibility.

### N3 — Hidden-wall scan

The note was scanned for the prescribed phrases. “Supplied action” names the
explicit Block-74 numerical input. “Standard finite-dimensional algebra” is
non-load-bearing shorthand because equations (2), (3), and (6) are written
out and executed. “Primitive registry” is governance context and no primitive
is used numerically. No occurrence of “naturally,” “obviously,” “standard
QFT,” or an unsupported “canonical/registered” step carries the proof. The
inside-unit-disk contour, structural-zero threshold, source/readout, action,
and momentum are explicit scope conditions rather than hidden admissions.

### N4 — Residual matching

| cited witness | witness residual | residual here | match? / use |
|---|---|---|---|
| `docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md:200-266` | necessary one- and two-step Hankel positivity for the supplied covariance | positive self-adjoint realization of the same scalar response | yes; independently re-executed, not used alone |
| `docs/ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_TT_SPECTRAL_WEIGHT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md:108-138` | finite Laurent roots and TT residue signs | numerical input to the descriptor/minimal response | partial; input only, not a no-go witness |
| `docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md:711-742` | a different carrier admits a positive data-built reflection completion | this gravity response's exact metric | no; retained only as a live counter-route |
| `scripts/admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24.py:257-456` | endpoint separation, minimal realization, and metric equations for this object | exact residual claimed here | yes; primary same-packet evidence |
| `scripts/admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24.py:459-693` | direct covariance moment/Gram reconstruction | positive self-adjoint-dilation and even-step residual | yes; disjoint implementation path |

The nonmatching Dirac--Kahler result is not counted as support for the negative
claim.

### N5 — Rhetoric audit

No phrase of the form “gravity is not positive,” “positivity is not a
per-mode fact,” or another resolution-wide negative appears. The exact
resolution ledger is:

| resolution | executed? | statement |
|---|---|---|
| per-element | yes | twenty-two action coordinates, four Ward columns, six odd edge coordinates, and one odd border coordinate enter the reconstruction |
| per-site | no | only one translation-invariant reflected unit cell is represented; no inhomogeneous site family is tested |
| per-mode | yes, bounded | all zero/finite/infinite modes of the declared odd polynomial at one spatial momentum are classified |
| per-block | yes | the 28-dimensional companion, three-mode response, two metric systems, and finite moment Grams are executed |
| lattice-wide | no | no full Brillouin zone, nonlinear background, continuum limit, or all-lattice claim is made |

The primary cached stdout lands the required substantive five-line N5
execution certificate.

### N6 — Partial-closure path scan

`docs/MINIMAL_AXIOMS_2026-06-29.md:108-130` makes dynamics selection explicitly
downstream. The current premise registry contains the minimal axioms plus the
approved scale-reference, kinetic-isotropy, and realized-state primitives;
none supplies a boundary response or makes this result conditional. No phrase
equivalent to “no retained primitive supplies this” or “new axiom required”
is asserted.

The principal non-axiom partial closure is the data-built reflection
intertwiner pattern in
`docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md:711-742`.
Its status is bounded/unaudited and its carrier differs, but it identifies an
explicit import-retirement target: derive the boundary pairing from stable
action data rather than postulate a sign choice. A convention rename cannot
turn a negative Gram eigenvalue positive, so no labeling-only closure is being
misclassified as new physics.

### N7 — Steelman

**Hostile reviewer:** The calculation has proved too much about the wrong
response. A periodic inverse-covariance contour need not equal the physical
half-space OS boundary response of a singular higher-step constrained action.
On a different carrier, the action's stable data and their reality images
generated a reflection-real swap intertwiner and a positive quotient
(`docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md:711-742`).
The actionable counter-route is therefore to construct the palindromic
descriptor's boundary concomitant, solve for an involutive reflection
intertwiner on its stable/unstable deflating subspaces, and transport the Ward
source and TT readout through that map. Until that terminal positivity and
source-transport obligation is run, this result cannot be physicalized.

That steelman is convincing against a broad boundary/gravity no-go, so none
ships. The explicit positive Stein metric (9) also refutes any broader
“no-positive-metric” wording. Neither defeats the narrow exact-response OS
theorem: the intertwiner may change the pairing/response, and (9) drops
self-adjointness.

### N8 — Cross-cycle echo

The prescribed repository phrase search and all physics-loop no-go ledgers
were scanned. The relevant echoes are:

| earlier wall | later disposition | retirement mechanism | application here |
|---|---|---|---|
| Block 118 non-Hermitian stable-split pairing | positively repaired in Block 119 on its displayed carrier | action-data-built swap intertwiner on stable factors and reality images | directly motivates the next campaign; not yet constructed for this gravity pencil |
| Block 120 torus wrap defect | half-space result preserved while the literal torus remained separate | change of carrier/boundary contribution rather than rhetoric | warns that the periodic response must not be called the physical boundary response |
| Block 74 negative Hankel forms | mechanistically sharpened, not retired, by Block 181 and this block | residues, endpoint deflation, and exact-response metric solve | the constraint-artifact escape is now closed only at the declared probe |
| historical “new axiom” walls | some were narrowed by convention or primitive ratification | reframe/import-retirement audit | not applicable to a computed negative eigenvalue; no axiom wall is claimed |

No previously successful repair mechanism is ignored. The strongest one—the
stable-data reflection intertwiner—is promoted to the next exact action.

**N1--N8 status: `PASS` for the narrow exact-response infeasibility only.**

## Reproduction And Evidence Contract

Primary runner:

```bash
python3 scripts/admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24.py
```

Required mutations:

```bash
for mutation in ward_input endpoint_input finite_spectrum_input source_dark_input positive_readout_input direct_source_input note_boundary; do
  TOE_MUTATION="$mutation" python3 scripts/admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24.py
done
```

Each mutation changes an upstream action/gauge coefficient, descriptor
coefficient, finite polynomial, source/readout map, direct covariance source,
or landing-note boundary before the relevant calculation. Each must produce
exactly one failed check. Postcomputed Boolean replacement is not accepted.

The runner must finish with `TOTAL: PASS=7 FAIL=0`, stay under 6,000 stdout
characters, and print the five-resolution N5 certificate. The canonical cache
is generated only by the repository cache envelope and remains non-authoritative
until independent audit.

## Boundary And Next Action

This result is **not gravity failure**. It does not test another action,
another spatial momentum, a nonlinear background, a full source/Record law,
or a derived physical boundary response. It does not move a TOE percentage.

The next highest-leverage campaign is the action-derived reflection
intertwiner/Weyl boundary construction on this descriptor. A positive result
must provide the boundary form, reflection map, transported source/readout,
Gram inertia, locality controls, and refinement behavior. A negative result
must again pass N1--N8 and may not be promoted across actions or momenta.
