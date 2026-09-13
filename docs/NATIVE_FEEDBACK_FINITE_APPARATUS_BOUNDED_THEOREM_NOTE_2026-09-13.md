---
claim_id: native_feedback_finite_apparatus_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "Supplied native occupation-feedback generator on a fixed finite legal one-head domain: finite positive battery and unitary collision approximation with its actual non-scalar loss, original free Hamiltonian, retained-battery error and explicit resource bounds."
upstream_dependencies:
  - native_edge_record_occupation_feedback_shared_battery_bounded_theorem_note_2026-09-07
  - native_edge_record_ambient_generator_erasure_bounded_theorem_note_2026-09-07
  - native_edge_record_local_quench_finite_ladder_bounded_theorem_note_2026-09-07
  - native_edge_record_finite_collision_apparatus_bounded_theorem_note_2026-09-07
runner: scripts/native_feedback_finite_apparatus_2026_09_13.py
---

# A finite battery and collision apparatus for native occupation feedback

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

Actual current-surface status is conditional-support. This is an author
proposal; independent source review and formal audit remain pending.

The [occupation-feedback generator](NATIVE_EDGE_RECORD_OCCUPATION_FEEDBACK_SHARED_BATTERY_BOUNDED_THEOREM_NOTE_2026-09-07.md)
has a state-dependent loss operator. The existing
[finite-battery theorem](NATIVE_EDGE_RECORD_LOCAL_QUENCH_FINITE_LADDER_BOUNDED_THEOREM_NOTE_2026-09-07.md)
explicitly excluded this feedback extension, while its
[collision companion](NATIVE_EDGE_RECORD_FINITE_COLLISION_APPARATUS_BOUNDED_THEOREM_NOTE_2026-09-07.md)
treated the complete instrument. Here the capped loss is compared directly,
and their finite-apparatus construction is extended to the feedback law.

~~~yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "State-weighted dissipator comparison and finite battery/collision construction, with small native algebra and unitary checks."
trace_class: upstream_support
target_claim_id: native_edge_record_occupation_feedback_shared_battery_bounded_theorem_note_2026-09-07
target_blocker_text: "Localize the energy-dressed operator with controlled retained-battery error and explicit physical resource costs."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Independently review this finite-apparatus extension, then test a specified physical control and formation interface."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## The theorem and its input domain

For the supplied finite native occupation-feedback model with maximum
virtual degree d, rate gamma and Lambda=d gamma, rounding the whole ambient
energy to mesh delta and using n fresh unitary collisions approximates the
original continuous-battery channel through modeled time T with error

\[
\delta\left[\frac2w+T+4\Lambda T\sqrt{\pi^2/w^2+T^2}\right]
+\frac{(6\Lambda^2+2\delta\Lambda)T^2}{n},
\qquad n\in\mathbb N,\quad n\ge\max\{1,4\Lambda T\}.        \tag{1}
\]

The norm is the trace-norm channel error maximized over legal matter inputs
and arbitrary reference entanglement, with the specified independent sine
battery attached. The output retains native matter, fuel, head, physical
Record sectors and the battery. Collision ancillas are traced in this
comparison. They may be kept physically without recoupling; their storage
is included in the inventory below. Equation(1) compares neither their
joint output state nor an unrestricted class of battery inputs.

Keep the original free matter Hamiltonian. Every finite collision and free
step conserves the rounded total-energy distribution exactly. For the
symmetric aligned sine preparation, the original modeled total-energy
mean changes by at most delta relative to the original input.

On the inherited cube, delta=1/1280, w=T=1, Lambda=3 and n=2161 suffice:
124160 positive battery levels,49 storage qubits and6 fresh ancillary
qubits per collision give13015 qubits in total, with error strictly below
15/256<0.06. This is a resource bound, not a simulation of that apparatus.

The domain is one fixed legal initial head/fuel/old-Record sector, including
arbitrary admissible matter/reference input; classical mixtures of such
sectors sharing the stated safe-energy enclosure are also allowed. All
physical outcomes and dark mass are included. The battery is
\(\beta(E)=\sqrt{2/w}\sin(\pi(E-b)/w)\) on[b,b+w], zero elsewhere.
The cap[0,C] has C=M delta and contains the exact invariant safe support.
For the energy-mean statement its cells and packet reflection are aligned.
The finite-time statement includes T=0; n is a positive integer throughout.
The native supplied parameters
have gamma>0 and w,delta>0; vanishing rate is the free-evolution boundary.

## Supplied model and proof dependencies

The [ambient construction](NATIVE_EDGE_RECORD_AMBIENT_GENERATOR_ERASURE_BOUNDED_THEOREM_NOTE_2026-09-07.md)
provides the physical edge-qubit algebra, legal code, fuel and one-head
guards, whole hopping operators and the common Hamiltonian

\[
A=\sum_e q_e(h_e+\Delta I),\qquad
B_{vw,z}=d_w^\dagger d_v f_e Q_{e,z}J_{vw}q_e,
\quad J_{vw}=T_e n_v(1-n_w).
\]

Here \(Q_{e,z}=(I+zZ_e)/2\) acts after the hop. On the one-head domain,
\(\sum_z B_{vw,z}^\dagger B_{vw,z}=E_{vw}n_v(1-n_w)\), with
\(E_{vw}=n_v^{head}q_e\). This is the actual feedback effect.

The ambient note supplies energy lifting and sign-summed legal-code
invariance. The feedback note supplies the same exact safe-energy domain
and non-scalar GKSL law. The finite-ladder parent supplies the sine/cell
embedding; its key estimates are rederived below. The collision parent's
star unitary and remainder estimate are also reproduced. These dependencies
are supplied-model conditional sources, not newly selected physical axioms.

The new lemma is the capped state-weighted loss comparison. Subsequent
steps preserve its exact-source domain, then add cell preparation and
collision errors. Native roles and preparation, hopping/rate/fuel values,
the energy apparatus, pulse controls and modeled clock remain supplied.
Spatial synthesis, continued fuel/blank renewal and a framework-admissible
physical occurrence rule are separate construction targets.

## A comparison lemma retaining the non-scalar loss

Let L and K be the exact and changed jump columns on a common invariant
system domain, with norms at most ell. A column includes its output label
space; recycling traces that label. Put D=K-L and S=sqrt(rho), Tr rho=1.
Suppose the two separate state-weighted estimates hold:

\[
\|DS\|_2\le e,\qquad \|D^\dagger LS\|_2\le\ell e.       \tag{2}
\]

The recycling difference is D rho K^dagger+L rho D^dagger, with trace
norm at most2ell e by Hilbert-Schmidt Cauchy-Schwarz. Regroup the loss as

\[
K^\dagger K-L^\dagger L=K^\dagger D+D^\dagger L.
\]

Its product with S has Hilbert-Schmidt norm at most2ell e by(2).
Multiplying by S^dagger bounds each loss product with rho by2ell e in
trace norm. The two half-anticommutators together have that same bound.
Therefore the full dissipator difference on rho is at most4ell e.
The proof includes arbitrary reference factors.

Both premises in(2) are necessary for this argument. A measured forward
error is not substituted for the common bound. The exact native check below
exhibits squared uncapped forward error21/25, capped forward error41/50,
and squared adjoint error1.

## Rounding and capping along the exact safe evolution

Let A_delta be the spectral rounding of the whole A with a fixed tie rule.
Then ||A-A_delta||<=delta/2 and[A,A_delta]=0. In Fourier battery coordinate
tau, a lifted sign column is exp(-i tau A) B exp(i tau A). Both spectral
exponentials give the full-column estimates

\[
\|L(\tau)-L_\delta(\tau)\|\le\sqrt\Lambda\delta|\tau|,
\qquad \|L(\tau)\|,\|L_\delta(\tau)\|\le\sqrt\Lambda.    \tag{3}
\]

Signs are stacked before bounding, and at most d edges are eligible in
each one-head source block. Compress each rounded jump by the cap P and
use its actual summed loss. No eligibility completion is added.

Let Q be the exact total-energy spectral projector containing the initial
input support. The enclosure gives PQ=Q. Every exact jump and its adjoint
preserves Q. Thus on an exact source state, S=QS,

\[
(K-L)S=P(L_\delta-L)S,\qquad
(K-L)^\dagger LS=P(L_\delta-L)^\dagger LS.             \tag{4}
\]

The exact unconditional Fourier marginal translates by modeled time s:
all jump multipliers commute with scalar functions of tau, while the free
battery generator translates them. Its second moment is consequently
pi^2/w^2+s^2, including developed system-battery correlations. Equations
(3)–(4) imply both premises(2) with

\[
\ell=\sqrt\Lambda,\qquad
e(s)=\sqrt\Lambda\delta\sqrt{\pi^2/w^2+s^2}.
\]

For the adjoint estimate, bound the pointwise product of the difference
column adjoint and the exact column by Lambda delta|tau|, then integrate
against that same exact marginal. This explicitly supplies the second
premise. No Fourier property of the approximate capped process is used.

Duhamel applies the generator difference to the exact safe state and
propagates it by the changed CPTP semigroup. Its error through T is at most
4Lambda delta T sqrt(pi^2/w^2+T^2). The bounded dissipators share the same
free generator; the statement follows in its interaction picture.

Whole spectral rounding preserves fuel/head blocks, N and old Record
guards. In each target block the consumed hopping is absent, so its
spectral projectors commute with the newly measured Z_e. The ambient
sign-summed argument therefore preserves source code in the loss as well
as in each forward branch. Cap compression acts on the battery only.

## Finite cells and energy accounting

Embed the M positive ladder levels(j+1/2)delta as normalized constants on
[j delta,(j+1)delta). Rounded jumps shift cells by integers. The cap and
the actual sign-summed loss preserve the cell subspace, as do their
no-jump exponentials. Replacing only free battery energy by cell centers
costs at most delta T in trace norm. Original free matter A is retained.

Cellwise Poincare and ||beta'||=pi/w give
||(I-P_delta)beta||<=delta/w. Replacing beta by its normalized cell
projection costs at most2delta/w for the pure input density. This input
replacement follows the exact-safe comparison, so it needs no safety
assertion for the projected source. This proves the first term of(1).
Unused battery encodings have an inert trace-preserving extension.

Define F=A+E_delta and K_energy=A_delta+E_delta. Every rounded jump
commutes with K_energy, and[F,K_energy]=0. Therefore the finite generator
preserves every bounded function of K_energy. Since
||F-K_energy||<=delta/2, two endpoints bound the original mean change by
delta. The initial continuous and cell means agree for the aligned
symmetric sine, and every embedded cell state has its cell-center energy
mean. A differently aligned preparation must include its actual mean
replacement error; exact unrounded energy-distribution conservation is
not part of this theorem.

## Finite unitary collisions

For finite jumps J_a set R=sum J_a^dagger J_a<=Lambda I. On a fresh
ancilla with zero-energy labels |0>,|a>, put

\[
B=\sum_a J_a\otimes|a\rangle\langle0|,\quad
V=B+B^\dagger,\quad U_h=\exp(-i\sqrt h V).
\]

With the ancilla prepared in |0>, the reduced Kraus operators are
cos(sqrt(hR)) and -i sqrt(h)J_a sinc(sqrt(hR)), with sinc(0)=1.
The actual dark subspaces are kept. Since ||V||^2=||R||<=Lambda,
ancilla parity eliminates odd powers ofsqrt(h). The fourth-order remainder
is at most(2sqrt(hLambda))^4 cosh(2sqrt(hLambda))/24. The dissipative
semigroup remainder is at most2h^2 Lambda^2 exp(2hLambda). Their sum is
less than6h^2 Lambda^2 for hLambda<=1/4.

Every collision commutes with K_energy tensor I. With X=-i ad_F and
D_energy=F-K_energy, the K_energy part commutes with the dissipator and
||[X,Diss]||_diamond<=4delta Lambda. Positive-time Duhamel bounds the
free/dissipative splitting error by2delta Lambda h^2. Telescoping n CPTP
steps with h=T/n proves the second term of(1). Each step is collision
followed by the original free evolution. Ancillas are never recoupled.

A pulse of modeled duration h has interaction norm at most
sqrt(Lambda/h). At prescribed bounded physical strength, the duration
must be changed accordingly. The inventory supplies fresh pure ancillas
and controls over a finite horizon; it is not an indefinitely reused bath.

## Explicit cube certificate

Use the parent's cube A between0 and24, gamma=hopping bound=Delta=1,
d=3, sine[48,49], cap[0,97], T=1. Exact total energy remains in[48,73],
and the battery stays in[24,73]. Set delta=1/1280. Since
sqrt(pi^2+1)<10/3, the finite-battery coefficient is less than
3+12(10/3)=43. The finite-battery error is below43/1280.

There are97*1280=124160 positive cells, fitting17 qubits. The inherited
native12 edge qubits,12 fuel qubits and8 head qubits give49 storage
qubits with that battery. Feedback uses no refusal flag. At most24
oriented edges with two physical signs give48 nonvacuum collision labels;
vacuum plus these fits6 qubits. The collision coefficient is
6Lambda^2+2delta Lambda=34563/640. For n=2161 its error is below1/40,
and n>=4Lambda T. Thus

\[
43/1280+1/40=15/256<0.06,\qquad49+6(2161)=13015.
\]

The original mean-energy bound is1/1280. These counts price the stated
storage and fresh labels. Physical spatial routing, preparation, clocks
and gate synthesis are not included in that count.

## Author checks and review record

The [primary runner](../scripts/native_feedback_finite_apparatus_2026_09_13.py)
directly imports its two helpers, so both are in its execution closure.
The [cap helper](../scripts/native_feedback_cap_check_2026_09_13.py) constructs
an exact native two-edge path and a padded discrete energy ladder. The
[collision helper](../scripts/native_feedback_collision_check_2026_09_13.py)
constructs a square from physical Pauli bit actions and checks a cycle-code
input and a separate old-Record input. Its deleted hopping is sqrt2/3;
original free evolution does not commute with the rounded jump.

The cap fixture is an algebraic discriminator, not a sine-packet or
spatial-radius approximation. The square has96 system/battery dimensions
and a288-dimensional explicit unitary. Its small state-specific errors
are compared against a separately built GKSL generator. They are not
measured diamond norms. The two legal square inputs share the same
selected-dimer dynamics; they are not independent proofs.

This proposal extends the existing complete-law result to feedback. The
earlier campaign derivation used a valid looser6ell e dissipator bound;
regrouping the loss above gives4ell e and reduces the sufficient fresh
collision count from5401 to2161 at the new stated error allocation.
Original work and failed fixtures are preserved at campaign commit
`a30bf0ecc57551d3bf5724ffa82819c3c4a8f9a1`. No native transport or
formation-selection conclusion follows from the resource improvement.

The focused [author review record](../.claude/science/physics-loops/native-feedback-finite-apparatus-20260913/REVIEW_HISTORY.md)
records the final source/check state. Seven actual scratch mutations were
rejected: removed cap, reversed energy shifts, reversed loss sign, an
overly small dissipator constant, removed occupation filter, replaced free
Hamiltonian and an identity loss substituted for feedback. Exact mutations
and failures are in the
[mutation results](../.claude/science/physics-loops/native-feedback-finite-apparatus-20260913/mutations/RESULTS.json).
These are author checks, not independent review. The
[scope stress test](../.claude/science/physics-loops/native-feedback-finite-apparatus-20260913/NO_GO_DISCIPLINE_CHECKLIST.md)
keeps this positive construction distinct from an impossibility claim.
