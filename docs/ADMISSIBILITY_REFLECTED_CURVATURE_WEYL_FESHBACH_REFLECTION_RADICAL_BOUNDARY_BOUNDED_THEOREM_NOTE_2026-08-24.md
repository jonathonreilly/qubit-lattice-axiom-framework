---
claim_id: admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "For the supplied twenty-two-edge reflected-curvature action at mu=1/1024, in the odd y/z-reflection six-edge plus one-Ward sector at spatial momentum (pi/2,0,0), the full seven-endpoint-plus-seven-finite stable descriptor graph defines a Hermitian two-layer Weyl form that agrees with independent finite-depth Feshbach elimination. Its physical edge covariance is positive semidefinite for the same unrefitted local TT covector. This is equal-boundary positivity, not OS positivity. For the declared geometric site/link cross-action kernels, no positive left completion can preserve that source, and their radicals are not shift invariant; constant and one-forward-layer action-covariant internal intertwiners reduce to scalar site/link translations. A canonical positive Krein metric exists on the three real TT modes, but changes the original source-adjoint response. Other boundary embeddings, time-extended/environmental completions, actions, momenta, Record instruments, Newtonian limits, refinement, gravity failure, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
parents:
  - admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_bounded_theorem_note_2026-08-24
upstream_dependencies:
  - minimal_axioms
  - admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_bounded_theorem_note_2026-08-24
  - admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24.py
---

# Reflected-Curvature Weyl/Feshbach And Reflection-Radical Boundary

**Type:** `bounded_theorem`

**Status:** bounded numerical/algebraic support; unaudited; no canonical axiom
is edited.

**WEYL_FESHBACH_VERDICT: POSITIVE_BOUNDARY_OBJECT.**

**DECLARED_REFLECTION_COMPLETION_VERDICT: BOUNDED_INFEASIBLE.**

**MINIMAL_TT_KREIN_ESCAPE: NONTERMINAL.**

**GRAVITY_VERDICT: OPEN.**

TOE accounting: **zero obligation retirement, zero percentage movement, and
no axiom is amended**.

## Result Up Front

The previous block proved that the exact periodic three-pole TT response has
no positive source-faithful self-adjoint realization, but it left the most
important escape open: the physical half-space boundary response could differ
from that periodic contour response. This note constructs that boundary
object from the supplied action rather than choosing roots by hand.

The 28-dimensional polynomial descriptor has a 14-dimensional stable
deflating space: seven structured zero-endpoint chains and seven finite roots
inside the unit disk. An explicit endpoint-plus-polynomial-nullvector basis
agrees with ordered QZ to maximum subspace angle `5.7e-11`. Its two-layer
boundary graph has condition number `1.6573` and defines a stable shift `F`
with spectral radius `0.3030760`.

Writing the temporal Laurent coefficients as `B_-2,...,B_2`, define

\[
 A=\begin{pmatrix}B_0&B_1\\B_{-1}&B_0\end{pmatrix},\qquad
 C=\begin{pmatrix}B_2&0\\B_1&B_2\end{pmatrix},\qquad
 D_-=\begin{pmatrix}B_{-2}&B_{-1}\\0&B_{-2}\end{pmatrix}.       \tag{1}
\]

The stable graph obeys

\[
 D_-+AF+CF^2=0,\qquad W=A+CF,\qquad D_-+WF=0.          \tag{2}
\]

The resulting Weyl/Dirichlet-to-Neumann form `W` is Hermitian to residual
`4.6e-15`. Independent open-depth Schur complements converge to it; at depth
32 the relative difference is below `1e-12`. `W` itself has inertia
`(2-,12+)`, because the seven-coordinate Ward border includes multiplier
directions. After restricting `W^-1` to the twelve physical edge boundary
coordinates, the covariance has inertia `(0-,11+,1 zero)`. The same unrefitted
local TT covector, embedded as `s=(g,0)` on the two boundary layers, gives the
positive boundary response

\[
 s^\dagger W^{-1}s=0.463199342344.                    \tag{3}
\]

This is genuine positive route progress: a coherent action-derived
equal-boundary covariance now exists. It is not yet OS reconstruction.
Time-separated reflected Grams, a positive self-adjoint quotient shift, and
an operational Record instrument/update law are not supplied by (3).

The natural site- and link-centered geometric crossing forms do not complete
the route. Their inertias are `(1-,1+,5 zero)` and `(4-,4+,6 zero)`. Their
canonical signs make positive semidefinite forms, but the fixed radicals leak
under the stable shift by approximately `0.733` and `0.895`. More strongly,
an exact source-preimage lemma excludes *every* positive left completion of
these raw crossings that fixes the TT source; no sign convention is assumed.

The three real source-visible TT modes do admit a unique spectral fundamental
symmetry and a positive Krein metric. That construction is similarity
covariant, so it must not be dismissed as coordinate-dependent sign fitting.
It nevertheless changes the source-adjoint response by
`4.34901455e-4` at moment zero, or deletes a source-visible mode under its
positive-sign restriction. It remains a mathematically real but physically
nonterminal escape.

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
weyl_feshbach_verdict: positive_boundary_object
declared_reflection_completion_verdict: bounded_infeasible
minimal_tt_krein_escape: nonterminal
gravity_verdict: open
next_trace_action: "derive a source-faithful unitary/environmental dilation of the explicit positive Stein contraction, or an action-selected time-extended boundary embedding, and require a local Record-facing source law rather than an abstract bath"
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs, Types, And Scope

The supplied object is the same quadratic twenty-two-edge reflected-curvature
action and odd Ward border as Block 182, at `mu=1/1024` and spatial momentum
`(pi/2,0,0)`. It is not the distinct nonlinear fifteen-edge action used in a
neighboring gravity/refinement lane. The five `7 x 7` Laurent coefficients,
geometric time reflection, and local TT-plus covector are recomputed from
repository inputs.

The TT covector is a conserved, Record-facing source/observable probe. It is
not called an operational Record readout: no instrument measuring the
curvature observable, registered clock, or update map is supplied. Equation
(3) therefore establishes equal-boundary response transport only.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are contextual. They do not
select a Hamiltonian, reflection completion, boundary condition, source
dictionary, or Record cadence. Nothing in this note is imported from a new
axiom.

All conclusions are bounded to one action, sector, momentum, source, and the
declared site/link planes. No Brillouin-zone, infrared, nonlinear-background,
continuum, or refinement theorem is inferred.

## Stable Graph And Weyl Certificate

Let

\[
 \mathcal B(z)=\sum_{r=-2}^{2}B_rz^r,\qquad
 P(z)=z^2\mathcal B(z).                               \tag{4}
\]

The endpoint basis is constructed without interpreting defective QZ zero
eigenvectors. With `P_j=B_{j-2}`, the lower Toeplitz matrix

\[
 T_3=\begin{pmatrix}
 P_0&0&0\\P_1&P_0&0\\P_2&P_1&P_0
 \end{pmatrix}                                       \tag{5}
\]

has nullity seven. For `(x_0,x_1,x_2)` in its kernel, the companion column is
`(x_2,x_1,x_0,0)`. Appending `(v,zv,z^2v,z^3v)` for all seven finite inside
roots produces the explicit stable space. It matches the independent ordered
QZ subspace and transfer at residuals `5.7e-11` and `4.3e-11`; the combined
deflating/graph residual is below `2e-15`.

The finite inside roots are three real modes and two complex-conjugate pairs:

```text
-2.45439070e-5
+2.91169025e-4
+2.661717269e-1
+9.334299387e-2 +/- 8.806793995e-2 i
+5.554475415e-2 +/- 5.4771417336e-1 i
```

Structurally, `F` has seven zero eigenvalues plus the squares of those seven
finite roots. Four shift eigenvalues are nonreal. This fact is carried into
the OS assessment rather than hidden by projecting to the three real TT
modes.

Open-depth block Toeplitz eliminations at depths 4, 8, 16, and 32 give
relative Weyl errors approximately

```text
7.95e-3, 6.20e-5, 4.89e-9, <1e-12.
```

Every finite-depth form has the same two negative border directions. The
physical edge covariance is Hermitian positive semidefinite, and its TT value
converges to (3). The periodic inside-root moment zero was
`0.581819121519`; the boundary value is deliberately different by
`-0.118619779175`. The covector was not refitted—the action-derived boundary
condition changed the response.

## Source-Faithful Positive-Completion Obstruction

Let `R` be the geometric reflection and

\[
 A_2=-RB_2,\qquad
 K_S=A_2,\qquad
 K_L=\begin{pmatrix}-RB_1&A_2\\A_2^\dagger&0\end{pmatrix}.       \tag{6}
\]

In the displayed odd basis, the source and outer crossing coefficient reduce
exactly to

\[
 g=\sqrt2e_1,\qquad
 A_2=i\mu\left[\sqrt2(E_{15}-E_{51})-\sqrt3(E_{16}-E_{61})\right]. \tag{7a}
\]

The explicit vector

\[
 y=-\frac{2i}{5\mu}e_5+\frac{i\sqrt6}{5\mu}e_6
\]

satisfies

\[
 A_2y=g,qquad g^\dagger y=0.                         \tag{7}
\]

The runner independently reconstructs this preimage with residual below
`2e-16`. Suppose a site left completion
`H=Theta K_S` were positive semidefinite and source faithful, `Theta g=g`.
Then

\[
 Hy=g,qquad y^\dagger Hy=y^\dagger g=0.              \tag{8}
\]

For a positive semidefinite Hermitian form, zero quadratic norm implies
`Hy=0`, contradicting `Hy=g!=0`. Thus no such source-fixing positive left
completion exists. For the link form, set `s=(g,0)` and `v=(0,y)`. Then
`K_Lv=s` and `s^\dagger v=0`, so the identical argument applies.

This obstruction does not assume that `Theta` is the matrix sign, invertible,
involutive, or action covariant. It is correspondingly stronger than failure
of one sign choice, but its object is narrow: the raw cross-action forms (6)
and fixed source. A different boundary embedding or transported source law is
not excluded.

An independent quotient obstruction points the same way. The canonical
matrix signs produce PSD forms with six- and five-dimensional radicals, but
those radicals are not invariant under the respective stable shifts. Any
invertible left completion has the same kernel, whereas self-adjointness
would make the kernel invariant. Hence these sign-completed raw crossings
cannot induce the required self-adjoint quotient evolution.

## Local Intertwiner Boundary

If `J` is another constant reflection intertwiner, the two identities
`J B_r J=B_-r` and `R B_r R=B_-r` imply that the relative map `C=RJ`
commutes with every `B_r`. The simultaneous commutant of all five constant
coefficient matrices is one-dimensional: only scalar multiples of the
identity commute with the full family. The singular-value separation exceeds
`1e15`.

The runner also solves the convolution commutator for a one-forward-layer
internal map

\[
 C(z)=C_0+zC_1,\qquad [C(z),\mathcal B(z)]=0.           \tag{9}
\]

The `294 x 98` system has nullity two, a smallest nonzero singular value
`0.728244829`, and nullspace angle below `3e-15` to
`span{I,zI}`. Requiring a real Hermitian reflection involution reduces these
scalar monomials to signs and translated site/link planes. Their balanced
cross inertias remain those in (6).

This is not arbitrary finite-range exhaustion. At wider support the
coefficient family admits additional algebraic elements, including the
Laurent operator itself, and their involution/source behavior has not been
classified. The live construction space is therefore time-extended,
environmental, or a changed boundary embedding—not an unqualified no-go for
local reflection.

## Canonical Krein Escape And Its Physical Wall

For the three real minimal TT modes, write

\[
 D=\operatorname{diag}(z_1,z_2,z_3),\qquad
 H=\operatorname{diag}(a_1,a_2,a_3),                  \tag{10}
\]

where the weights have signs `(+,-,+)`. Because the roots are simple, the
spectral fundamental symmetry

\[
 J=\operatorname{diag}(+1,-1,+1)=I-2P_-              \tag{11}
\]

is uniquely characterized by `[J,D]=0`, `J^2=I`, and `G=HJ>0`. Under any
minimal similarity `S`,

\[
 D'=SDS^{-1},\quad H'=S^{-\dagger}HS^{-1},\quad
 J'=SJS^{-1},\quad G'=S^{-\dagger}GS^{-1}.            \tag{12}
\]

The runner verifies this covariance and `G`-self-adjointness below `3e-16`.
Thus a claim that no canonical positive algebraic quotient exists would be
false.

The physical mismatch is exact. With the same source `b=(1,1,1)`, the original
moments contain `H`, while the positive Hilbert metric gives

\[
 \widetilde m_n=b^\dagger GD^nb
 =m_n-2a_2z_2^n.                                     \tag{13}
\]

At `n=0` the change is `4.34901455e-4`. Restricting to the positive-sign
subspace removes the source-visible middle mode and changes `m_0` by
`2.17450728e-4`. The original one-step and even-step `3 x 3` Hankel
determinants remain negative. The polynomial spectral sign filter also has
coefficient magnitude about `2.38e4`, a locality warning rather than a proof
of non-canonicity.

What is missing is a physical derivation that licenses (13): an
action-selected reflection or environment, a transported full Ward source,
a Hermitian TT observable/instrument, and a Record update law. Until then the
Krein construction is a live mathematical escape, not positive retained
gravity.

## Axiom Decision

No contradiction with Lattice, Qubit, Admissibility, or Record is found. The
minimal axioms deliberately leave dynamics and the Hamiltonian open. The
positive boundary covariance and the two bounded completion walls therefore
do not justify editing the axioms.

If all action-derived boundary/dilation families fail, governance may later
face a dynamics-selection question. This block does not establish that
universal antecedent. Adding a sign axiom now would merely encode the desired
answer to one hostile probe.

## No-Go Discipline Gate

The negative statement is only: **for the declared site/link cross-action
kernels at this action and momentum, no positive left completion fixes the
local TT source, and their sign-completion radicals do not support the stable
self-adjoint quotient; fixed and one-forward-layer action-covariant internal
maps reduce to those planes.** The Weyl covariance, canonical Krein escape,
wider-support/environmental completions, other embeddings, and gravity remain
open.

### N1 — Alternative route enumeration

| route | executed terminal test | disposition |
|---|---|---|
| explicit endpoint-plus-finite stable graph | derive all fourteen stable descriptor directions without trusting defective endpoint QZ vectors | `ATTEMPTED`; agrees with ordered QZ and gives conditioned graph |
| finite-depth Feshbach sequence | independently eliminate open interiors and converge to the infinite Weyl form | `ATTEMPTED`; converges and yields PSD physical edge covariance |
| geometric link crossing | test sign positivity, source preservation, radical invariance, and transfer adjointness | `ATTEMPTED`; source-preimage contradiction and radical leakage |
| geometric site crossing | repeat on the distinct site plane and seven finite-mode shift | `ATTEMPTED`; same two independent failures |
| constant and nearest-layer internal completion | solve coefficient commutant and degree-one convolution commutant | `ATTEMPTED`; only scalar site/link translations |
| canonical minimal-TT Krein completion | build the invariant spectral fundamental symmetry and transport it under similarity | `ATTEMPTED`; algebraically positive, but changes the source-adjoint response |

These routes use different primary objects: a polynomial deflating space,
finite Schur complements, two crossing forms, a coefficient-convolution
system, and a minimal scalar realization. They are not duplicate restatements.

### N2 — Wall-independence audit

The exact bounded source-preimage contradiction is independent of transfer
self-adjointness: it excludes source-fixing PSD left completion before a
shift is chosen. Radical noninvariance is independent of source fixing: it
excludes self-adjoint quotient evolution for invertible completions even if
the source condition is dropped. The scalar/one-layer commutant calculation
is a third wall limiting how the geometric reflection can be changed while
remaining action covariant and nearest-layer local.

None closes the time-extended/environmental embedding wall. Equal-boundary
Feshbach positivity also does not imply all-time OS positivity. These are
kept as separate obligations.

### N3 — Hidden-wall scan

The scope explicitly records: constrained edge covariance versus the
indefinite Ward border; equal-boundary positivity versus time-separated OS
Grams; explicit endpoint chains versus defective zero QZ coordinates; seven
finite stable modes including four nonreal shift eigenvalues; local TT
covector versus a full conserved Ward source and operational Record
instrument; constant/one-forward-layer locality versus arbitrary finite
range; one hostile momentum versus Brillouin-zone and Newtonian IR behavior;
and finite quadratic KKT data versus nonlinear background/refinement laws.

No “canonical” step is load bearing without an invariant characterization.
The Krein symmetry is characterized spectrally and then rejected only as a
source-faithful physical solution, not as algebraically arbitrary.

### N4 — Residual matching

| witness | witness residual | residual here | match/use |
|---|---|---|---|
| `scripts/admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24.py:147-281` | stable descriptor graph and Weyl equation | action-derived half-space boundary object | yes; primary construction |
| `scripts/admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24.py:282-319` | independent finite-depth Schur complements | asymptotic Weyl form and edge covariance | yes; implementation-disjoint cross-check |
| `scripts/admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24.py:606-718` | link/site source preimages, radical leakage, and adjoint residuals | declared reflection-completion wall | yes; primary same-packet evidence |
| `scripts/admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24.py:364-432` | constant and degree-one convolution commutants | nearest-layer action-covariant family | yes; finite linear exhaustion at stated support |
| `docs/ADMISSIBILITY_REFLECTED_CURVATURE_DESCRIPTOR_HALFSPACE_SOURCE_FAITHFUL_METRIC_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md:248-270` | positive non-self-adjoint Stein contraction for exact scalar response | next dilation route | partial; live construction, not negative support |
| `docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md:903-923` | a different carrier has a data-built positive reflection swap | hostile steelman against a broad no-go here | no match; retained as counter-route |

The positive result on the distinct Dirac--Kahler carrier is not counted as
evidence for this bounded negative.

### N5 — Rhetoric audit

No sentence says gravity is nonpositive, every reflection fails, locality is
impossible, or a new axiom is necessary. The exact execution resolutions are:

| resolution | executed? | statement |
|---|---|---|
| per-element | yes | the twenty-two-edge action enters through six odd edge coordinates, one Ward border coordinate, and the geometric reflection |
| per-site | bounded | one translation-invariant site plane and one link plane are tested; no inhomogeneous family |
| per-mode | bounded | all seven endpoint and seven finite stable descriptor modes are included at one spatial momentum; the scalar escape uses its three real TT-visible modes |
| per-block | yes | the 14-dimensional graph, infinite Weyl form, four Feshbach depths, two crossing Grams, and two commutant systems are executed |
| lattice-wide | no | no Brillouin-zone, Newtonian-IR, nonlinear-background, refinement, or all-lattice theorem is claimed |

The cached stdout prints these five substantive lines verbatim.

### N6 — Partial-closure path scan

| live path | current partial closure | terminal missing object |
|---|---|---|
| action-derived Weyl/Feshbach boundary | Hermitian infinite-depth form and PSD constrained edge covariance | all-time reflected Grams, quotient transfer, full source and Record instrument |
| canonical TT Krein metric | unique similarity-covariant positive metric | source-faithful action/Record derivation and momentum-local transport |
| positive Stein contraction from Block 182 | explicit source-faithful strict contraction | source-faithful unitary dilation with physical environment and Hermitian observable semantics |
| wider-support boundary intertwiner | coefficient algebra is nontrivial beyond nearest layer | involution, positivity, source preservation, locality, and refinement |
| changed action/Hessian | remains allowed by axioms | independently selected nonlinear action and source pencil, not retrospective tuning |

The positive Weyl result retires the local concern that no coherent
action-derived half-space object exists. It does not retire a TOE obligation.

### N7 — Steelman

**Hostile reviewer:** The declared raw crossings are the wrong objects. The
action itself has already produced a different boundary covariance through
Feshbach elimination, and the three-mode realization has a canonical positive
Krein metric. On another carrier, stable/unstable action data generated a
positive reflection intertwiner. A time-extended boundary embedding or
unitary environmental dilation may therefore select the positive form while
transporting the source. The source-preimage lemma cannot rule out a changed
embedding, and the degree-one commutant cannot rule out wider support.

This steelman is convincing against a broad reflection, positivity, or gravity
no-go, so none ships. It does not defeat the narrow statement about the two
declared raw crossing kernels and nearest-layer internal family.

### N8 — Cross-cycle echo

| earlier result | later disposition | application here |
|---|---|---|
| Block 118 non-Hermitian stable pairing | positively repaired in Block 119 by a data-built swap on a different carrier | forces the time-extended/action-data counter-route to remain live |
| Block 120 torus-wrap defect | half-space carrier survived while literal torus claim remained separate | warns against identifying periodic contour response with boundary response |
| Blocks 74/181 negative TT moments | sharpened by endpoint and source-faithful metric analysis in Block 182 | now separated from the positive Weyl equal-boundary object rather than repeated |
| Block 182 positive Stein contraction | survived the exact self-adjoint no-go | promoted to the next dilation campaign if wider boundary completion does not close first |

No successful repair is ignored, and no old wall is promoted past its original
carrier or resolution.

**N1--N8 status: PASS for the narrow declared-reflection and nearest-layer
completion infeasibility only.**

## Reproduction And Evidence Contract

Primary runner:

```bash
python3 scripts/admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24.py
```

Required mutations:

```bash
for mutation in reflection_input stable_graph_input feshbach_input link_reflection_input site_reflection_input commutant_input scalar_sign_input note_boundary; do
  TOE_MUTATION="$mutation" python3 scripts/admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24.py
done
```

Each mutation changes an action/reflection input, stable or Feshbach
coefficient, declared crossing, commutant family, scalar signature, or landing
boundary before its relevant calculation. Baseline must finish with
`TOTAL: PASS=8 FAIL=0`; every mutation must finish with exactly one failed
check. The canonical cache is generated only through the repository cache
envelope and remains non-authoritative until independent audit.

## Boundary And Next Action

This block changes route confidence but not the TOE score. The action now has
a validated positive equal-boundary object. Its obvious geometric site/link
reflections cannot preserve the source and become positive, and nearest-layer
internal repair is exhausted. Gravity remains open.

The next highest-leverage campaign is the explicit all-powers unitary dilation
of Block 182's positive source-faithful contraction, cross-checked against a
wider-support action-selected boundary embedding. A viable result must derive
the environment/reflection from action data, carry the full Ward source and a
Hermitian TT observable, state what constitutes a Record, and preserve
locality, Newtonian IR reachability, and exact refinement. An arbitrary bath
or post-hoc absolute-residue rule does not count.
