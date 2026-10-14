---
title: "Conditional calibration stability for finite energy measurements"
claim_id: graph_calibration_bounded_theorem_note_2026-10-13
status: conditional-support
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
assembly_status: parent_bound_source_ready_for_root_review
canonical_parent_binding_complete: true
scientific_execution: none_in_publication_source_preparation
runner: scripts/graph_calibration_identity_2026_10_13.py
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: assumed common H and spectral instrument; uniform ideal graph bounds; bounded control and first-commutator calibration errors; regular ideal history law for application; fixed resources
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: conditional positive graph perturbation theorem with explicit common-model hypotheses and preserved analytic checks
next_trace_action: obtain separate root source-integration acceptance of the bound publication package
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies:
  - postmeasurement_energy_tail_bounded_theorem_note_2026-10-13
---

Claim type: bounded_theorem

The canonical parent is bound to its actual regular PR and exact published
source. Separate root acceptance of this publication package is still required
before installation or runtime. Source checks establish byte identities only.

<!-- BEGIN CANONICAL PARENT BINDING -->
The direct parent is [Finite-first-energy tails and ideal forward/inverse graph bounds](POSTMEASUREMENT_ENERGY_TAIL_BOUNDED_THEOREM_NOTE_2026-10-13.md),
The original PR9526 source was submitted at commit
`ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989`. This integration preserves its mathematical bodies; the current
967-line source has SHA-256
`157f32fd61074c911d09d13cad84e074de4cddd1493bce6d9784b45a5f05e7da`.

The parent supplies ideal full and half graph bounds for both evolution
directions in its supplied massive strict-gap smooth-slot setting, together
with fixed-protocol finite-first-energy tails. Its regular normal-state
weak-law corollary explicitly assumes the archived prepared-state theorem;
that law remains a supplied provisional scientific dependency here. The
canonical vacuum multi-time parent does not establish the normal-state law.
The abstract result below continues to state graph regularity and the ideal
regular history law as assumptions when applied outside that supplied setting.

One new claim node and one direct canonical edge are proposed. Historical
source aliases, the tail parent's ancestors and sibling PR9518 do not create
additional direct edges. Exact complete-core containment and premise-role
locations are recorded in PARENT_BINDINGS.json. The original J sentence is
read with the required linear/unitary J=Gamma C precision. The parent's
epsilon=o(h^2) comparison remains valid; this note proves the stated sharper
sufficient calibration scale under the uniform ideal graph hypotheses.
<!-- END CANONICAL PARENT BINDING -->

# Conditional calibration stability for finite energy measurements

This publication candidate packages a checked conditional perturbation theorem.
Uniform ideal energy-graph bounds improve the sufficient calibration scale
from the earlier \(\epsilon=o(h^2)\) to \(\epsilon=o(h)\) on a kinetic
window with integrated drive budget \(b_h=O(h^{-1})\). The more precise
condition is \(\epsilon b_h\to0\). The earlier sufficient bound remains
valid. Necessity for the fixed-slot continuum model is not established.

The mathematical result received ordinary conditional source acceptance on
2026-10-13. This publication preparation adds no independent mathematical review, retained
audit status, physical realization or empirical prediction. The complete
unchanged proofs and analytic checks follow this wrapper. Their historical
status sentences and notation remain visible; the current scope is fixed
by this wrapper and the archived final acceptance/review.

<!-- CURRENT-SCOPE: uniform_C_G_for_full_theorem -->
<!-- CURRENT-SCOPE: calibration_order_p_plus_one_separate_from_2n_plus_one -->
<!-- CURRENT-SCOPE: assumed_common_H_not_retained_status -->
<!-- CURRENT-SCOPE: ideal_regular_law_is_an_application_assumption -->
<!-- CURRENT-SCOPE: growing_C_G_single_propagator_only -->
<!-- CURRENT-SCOPE: abstract_controls_do_not_prove_continuum_necessity -->

## Conditional theorem

Let \(H\ge0\) be the exact common self-adjoint free energy on the identified
Hilbert space, \(G=1+H\), and \(S=G^{1/2}\). Let \(h>0\),
\(\epsilon\ge0\), and all error constants be nonnegative. The ideal and
actual interactions differ by the real drive \(f_h(t)\Delta V\), where
\(\Delta V\) is bounded self-adjoint and

\[
 b_h=\int_0^{T_h}|f_h(t)|\,dt<\infty,\qquad
 \|\Delta V\|\le d_0\epsilon,\qquad
 \|[H,\Delta V]\|\le d_1\epsilon.
\]

The ideal Hilbert-space interaction-picture unitary starts at identity.
Assume the ideal and perturbed Hilbert evolutions satisfy the bounded
interaction integral equations used in Appendix A. Actual graph-domain
invariance is proved by the construction, rather than included here as an
assumption.

The last commutator is a genuine bounded graph-domain extension. The
perturbation preserves \(D(H)\); equivalently, the bounded commutator-form
criterion supplies that invariance. The free observable, embedding and
spectral instrument are common by assumption. Their physical realization
and the two error bounds are not derived in this packet.

For every prefix time, assume genuine ideal forward and inverse graph maps
with one constant \(C_G\ge1\), uniform over the parameter family:

\[
 \|G Y_h(t)G^{-1}\|,\quad
 \|G Y_h(t)^*G^{-1}\|\le C_G.
\]

Assume the stated strong graph evolution regularity. In the bounded-control
source setting, strong graph continuity follows at each fixed parameter
from its bounded first commutator. A uniform time modulus or operator-norm
Bochner measurability is not required. Mere norm inequalities are not used
as a replacement for an existing graph-space evolution.

Put \(d_G=d_0+d_1\) and \(x_h=C_G^2d_G\epsilon b_h\). Then the actual
evolution and its inverse preserve the graph domain and satisfy

\[
 \|G Y_{{\rm act},h}^{(*)}(t)G^{-1}\|\le C_G e^{x_h},
 \qquad
 \delta_G\le C_G(e^{x_h}-1),
\]

where \(\delta_G\) bounds both forward and adjoint full-graph differences
uniformly in prefix time. With \(D\) either propagator difference,

\[
 \|D\|\le d_0\epsilon b_h,\qquad
 \delta_S:=\sup\|SDS^{-1}\|
 \le\sqrt{d_0\epsilon b_h\,C_G(e^{x_h}-1)}.
\]

These are consequences of a graph-space Dyson construction in the ideal
interaction frame. A separate inverse construction gives the adjoint graph
bound; it is not inferred by equating oppositely weighted adjoint norms.
Vectorwise integrals have an integrable norm majorant, and their ordered
series converges in graph-operator norm.

Thus \(\epsilon b_h\to0\) gives uniform full and half graph differences
of order \(\epsilon b_h\). If \(\epsilon b_h\) is merely bounded, actual
graph norms remain uniformly bounded, but ideal-law convergence does not
follow from that fact alone. The case of zero perturbation or zero drive
has exactly zero difference.

For fixed kinetic resources \(b_h\le C/h\), the sufficient requirement is
\(\epsilon=o(h)\). Write the calibration order as \(p\ge0\), fixed, with
\(\epsilon=O(a^{p+1})\). Then

\[
                         a=o\!\left(h^{1/(p+1)}\right)
\]

is sufficient. The symbol \(p\) denotes calibration order only. It is
distinct from the number \(2n+1\) of unitary factors in an \(n\)-record
measurement chain. No optimality is claimed for this physical calibration
scale.

## Fixed finite measurement chains and first energies

For fixed times and common Borel bins, put
\(P_j=Y_h(t_j)^*1_{B_j}(H)Y_h(t_j)\) and
\(Q_h=Y_h(t_f)P_n\cdots P_1\); use the same construction for the actual
evolution. Common spectral projections contract both graph spaces. If
\(L_A\ge1\) bounds every ideal and actual unitary factor on the graph of
\(A=G\) or \(S\), finite telescoping gives

\[
 \|A(Q_{{\rm act},h}-Q_h)A^{-1}\|
 \le(2n+1)L_A^{2n}\delta_A.
\]

The comparison allows arbitrary common Borel bins because these exact
projections are unchanged between the models. It does not remove boundary
regularity assumptions from an ideal weak-limit theorem. The number of
records and the resource constants remain fixed.

For a fixed normalized state with finite first energy,
\(M=\operatorname{Tr}(G\rho)<\infty\), let \(L_{\rm act},L_{\rm id}\)
bound the two history half-graph norms, and let \(d\) bound their difference.
The unnormalized final-energy means obey

\[
 |m_{{\rm act},h}-m_h|
 \le (L_{\rm act}+L_{\rm id})dM.
\]

This follows from the bounded factorization of
\(H^{1/2}Q_h\rho^{1/2}\). It requires neither a second initial energy
moment nor quasifreeness. For moving normalized states with
\(d_E=\|S(\rho_{\rm act}-\rho)S\|_1\to0\), the extra mean error is at
most \(L_{\rm act}^2d_E\). Bounded history comparisons require only ordinary
trace convergence; any fixed normal initial state is allowed for them.

Uniform full and half graph bounds also give uniform first-energy tails
for each fixed finite-energy state. For moving states, the precise assertion
is \(\lim_{R\to\infty}\limsup_{\rm joint}\) of the tail equal to zero.
A convergent sequence or a weighted-trace-compact family has a genuine
uniform tail modulus. Convergence at a missing limit point alone does not
give uniformity over every arbitrary punctured continuum neighborhood.

For a limiting-law application, assume the ideal finite-history weak law
at its regular bins or separately justified common zero-gap convention.
Together with the graph tail argument, the comparison transfers branch
masses and unnormalized first means. For a selected history whose limiting
probability is positive, conditional weak convergence and first-moment
convergence yield conditional \(W_1\) convergence on nonnegative energies.
Zero-probability normalization is not covered. Finite unions of recorded
histories sum positive branch measures, rather than chain amplitudes.

## Scope of the analytic controls

The two-level resonant calculation shows failure of a generic ideal-law
convergence guarantee at \(\epsilon=kh\) within the abstract assumptions.
It does not prove necessity for the nonzero fixed-slot continuum model.
The bounded-commutator measurability example shows why vectorwise graph
integrals are used; it is not a physical obstruction. The escaping-energy
rotation shows why the growing-\(C_G\) comment cannot replace uniform
graph bounds in the full protocol and tail theorem.

In particular, formulas involving growing \(C_G\) diagnose the
single-propagator difference only. Finite products carry additional graph
powers, and uniform tails need separately justified bounds. No theorem for
growing resources, growing record count, arbitrary energy-ball families,
unspecified instruments, massless or zero-frequency limits, or physical
continuum realization is exported here.

## Exact dependencies and publication boundary

| Claim or application | Premise and current status |
|---|---|
| Abstract graph stability | Exact common \(H\), graph regularity, uniform two-way ideal graph bounds and the two error bounds are explicit assumptions; the unchanged root V2 proves the implication. |
| Fixed finite deterministic instrument comparison | Requires the same spectral instrument and fixed record count; proved in the included argument. |
| Weak-law, mean and conditional \(W_1\) application | Assumes an established regular ideal finite-history weak law and finite first initial energy for unbounded conclusions; graph tails and transfer are supplied here. |
| Supplied model's ideal graph theorem | The exact published tail parent supplies U6/U9 and T11/T19 in its strict-gap fixed-resource model, with the required \(J=\Gamma C\) precision. No retained status is inferred. |
| Canonical tail application | Regular PR9526 supplies finite-first-energy tails and a conditional limiting-law upgrade. Its prepared normal-state weak law remains a supplied provisional assumption; the vacuum canonical parent does not establish it. |
| Physical realization and calibration | Remain assumptions; no realization family, detector model or empirical validation is supplied. |

The abstract implication is complete without a newly published tail parent.
The application is now bound to the exact published tail parent. Its prepared
normal-state weak-law premise remains conditional; no scientific hypothesis
is discharged solely by Git ancestry or source-identity checks.
A root-owned publication driver is proposed as reviewable source. It has not
been executed. This preparation creates no branch, PR or audit verdict.

## Preserved proofs, correction and exposure history

Appendices A--D contain exact immutable bodies: root V2/192 lines,
independent derivation/289, independent evidence/192, and separate analytic
review evidence/206. Extraction records bind every body to its original
hash. Full comparison/194 and separate review/108, plans, seals, read
receipts and final acceptance/review are archived with their source closures.

Root V1 incorrectly asserted that the \(TR\) derivative directly vanishes.
V2 uses its commutator equation and uniqueness. The exact V1, V2 and diff
remain archived. V1 was sealed before the independent preliminary route
message; V2 followed that message and preceded the complete independent
proof. The separate exposed reviewer did not read the independent target.
All used the same selected model family and shared graph premises.

Historical pending/status sentences in the appended sources are preserved
as history. The final review requires uniform \(C_G\), the calibration
notation used above, and reading historical “retained common-H” as assumed
common-H, not audit retention. These are wrapper precisions, not silent
changes to frozen bodies.

The root's read-only wrong-filename attempt and subsequent complete recovery
are preserved in its independent-read receipt. Source checks execute zero
mathematical predicates. They validate bytes, extraction boundaries and
declared archive identities, not the correctness of the theorem. The read
coverage record distinguishes full new wrapper/review reads from reused
unchanged proof coverage and metadata-only archive checks.

No editable prompt, physical axiom, audit status or original scientific
source is changed by this preparation. The accepted assembly received root
source acceptance at 21:56:52 UTC on 2026-10-13. The present publication
wrapper and programs require their own exact root acceptance. Actual parent
binding is complete; publication integration and retained audit remain open.

Review-loop integration: exact current main a3ccb945b1543e31361f1c6fefd2cc7ab7d31d5f plus this batch supplies the live parent sources. Immutable mathematical bodies and original archives are unchanged. Live parent hashes and core coordinates are refreshed, with original identities preserved. Historical acceptance and pending labels are provenance, not audit authority.


## Appendix A — Accepted root V2 proof

The following body is an unchanged historical source. The current wrapper
and archived final review govern export scope and current status.

<!-- BEGIN IMMUTABLE A sha256=0906b06197d7664b5b7ee9c7bfe6b453e2949135225ee647feaeb6f93b1eb5dd -->
# Conditional sharpening of actual energy transfer by graph interaction picture

Root original derivation. Status at seal: proposed conditional theorem, not yet
independently checked. Plan sealed16:16:39UTC after disclosed pre-plan reasoning.
No independent target findings have been received. No new physical axiom,
embedding, instrument, channel selection or actual continuum construction.

## G1. Precise abstract premises

Let H>=0 be self-adjoint on Hilbert space, G=1+H and S=G^(1/2).
Fix a finite kinetic horizon. The ideal interaction-picture unitary Y(t)
starts at identity and its inverse obeys, uniformly for every prefix time,

  ||G Y(t) G^-1||, ||G Y(t)* G^-1|| <= C_G.                 (1)

Here these are genuine bounded extensions on the graph space D(H), and Y(t)
and its inverse preserve that domain. Strong continuity on this graph space
holds for each fixed parameter, not necessarily with a uniform time modulus.
The accepted postmeasurement q2 argument supplies uniform constants (1) for
its ideal drive families; the separately checked threshold version supplies
it on that extension. This note is an abstract implication from (1).

Ideal and actual Hamiltonians have exactly common free H and differ by
lambda c(t) DeltaV, where c is real measurable, b=integral|lambda c(t)| finite,
DeltaV is bounded self-adjoint and maps D(H) into itself, and its commutator
has a bounded extension satisfying

  ||DeltaV||<=d0 epsilon, ||[H,DeltaV]||<=d1 epsilon.       (2)

The common H and domain/error hypotheses are assumptions. Set dG=d0+d1.
For x in D(H), G DeltaV x=DeltaV Gx+[H,DeltaV]x, hence
||G DeltaV G^-1||<=dG epsilon. Free conjugation preserves this bound.
The original bounded-control/commutator premises ensure graph strong
measurability: on D(H), G V_I(t)G^-1=V_I(t)+[H,V]_I(t)G^-1 is strongly
continuous before multiplication by measurable c. Each fixed-parameter graph
Dyson series for the ideal evolution is consequently well-defined. Thus the
strong graph continuity premise above is satisfied in the source setting.

## G2. Relative propagator and graph construction

Let Y_a be the actual Hilbert-space interaction-picture evolution and define
T=Y*Y_a. Differentiation in the bounded interaction-picture integral equations
(or their absolutely continuous strong derivatives a.e.) gives

  T'=-i lambda c(t) B(t) T,  B(t)=Y(t)* DeltaV_I(t) Y(t).  (3)

Every factor in B preserves D(H). Equation(1) yields

  ||G B(t) G^-1|| <= C_G^2 dG epsilon =: k_G.             (4)

B is strongly measurable on the graph space; its norm majorant multiplied
by |lambda c| is integrable. On the Banach/Hilbert graph space with norm
||Gx||, construct the ordered Dyson series. The nth term has norm at most
(k_G b)^n/n!. Hence it converges in operator norm after conjugating by G,
with strong Bochner integrals understood vectorwise (operator-norm
measurability is unnecessary). Its sum T_G satisfies the graph-space
integral equation and

  ||G T G^-1|| <= exp(k_G b),
  ||G(T-I)G^-1|| <= exp(k_G b)-1.                        (5)

To justify the notation T rather than assuming graph invariance: embed the
graph-space integral equation continuously into the original Hilbert space.
For each initial vector in D(H) its solution satisfies the Hilbert integral
equation, which has uniqueness for an integrable bounded generator. It equals
Y*Y_a on D(H). This identifies the bounded graph solution and proves actual
forward invariance. Solve the right equation R'=i lambda c R B, R(0)=I,
by the reverse ordered series. It has the same absolute bounds. The product
rule a.e. on each graph vector gives (RT)'=0. For K=TR it instead gives
K'=-i lambda c B K+i lambda c K B, K(0)=I. Uniqueness of this bounded
operator integral equation (the difference is bounded by an integrable
coefficient times its norm) implies K=I as well. Thus both products equal
identity, R=T^-1=T*, and R has the same graph bounds. This proves actual
inverse invariance, without assuming Y_a already has uniform graph bounds.

## G3. Uniform actual bounds and differences

Since Y_a=YT and Y_a*=T*Y*, (1) and (5) imply, with x=C_G^2 dG epsilon b,

  ||G Y_a^(*) G^-1|| <= C_G exp(x),
  ||G(Y_a^(*)-Y^(*))G^-1|| <= C_G (exp(x)-1).            (6)

Both signs are separate products, not an illicit equality of weighted
adjoint norms. Hilbert unitarity gives the usual Duhamel bound
||Y_a^(*)-Y^(*)||<=d0 epsilon b (or the trivial cap2).
Complex interpolation of the Hilbert scale D(G^theta), or its three-lines
proof for <u,G^z D G^-z v>, yields

  ||S D S^-1|| <= sqrt(||D|| ||G D G^-1||).              (7)

Use finite spectral cutoffs/dense analytic vectors for the three-lines proof
then bounded extension and closure. G>=1 makes inverse powers bounded;
this is an interpolation of linear operator norms, not operator monotonicity
applied to an ordered square. Applying (7) to each difference gives

  delta_S <= sqrt(d0 epsilon b C_G (exp(x)-1)).           (8)

Also actual and ideal half-graph norms are bounded by the square roots of
their full-graph norms, since their Hilbert norms are1. Thus epsilon b->0
suffices for convergence on both graph spaces. For b<=C/h this is epsilon=o(h),
strictly weaker than the earlier sufficient epsilon=o(h^2) estimate. If b=0
or d0=0, the exact difference is zero. Nothing here asserts this scaling is
necessary or optimal; cancellations may permit still weaker hypotheses.

The earlier unweighted commutator estimate epsilon(b+b^2) remains a valid
coarser bound. The relative graph difference G D G^-1 does not imply a
small unweighted [H,D]. There is no contradiction: uniform ideal graph
bounds use energy structure absent from that earlier coarse estimate.

## G4. Fixed measurement protocols

Let Pi_j=1_{B_j}(H) and P_j=Y(t_j)* Pi_j Y(t_j); actual P_a,j uses Y_a.
Each Pi_j commutes with G,S and is a contraction on both graph spaces.
For a fixed number n of bins, the history amplitude with final drive is
Q=Y(t_f)P_n...P_1, and Q_a is the identical construction using Y_a.
It is a product of N=2n+1 unitary factors and n projections. A telescoping
product bounds each graph difference by

  ||A(Q_a-Q)A^-1|| <= N L_A^(N-1) delta_A,               (9)

for A=G,S, where L_A>=1 bounds every ideal/actual unitary factor and delta_A
bounds their differences. Projections contribute factor1 and are common.
The bound is uniform over Borel bins and protocol times on the fixed horizon,
for this actual/ideal comparison only; n and the resource constants are fixed.
The ordinary norm analogue also holds, and all history amplitudes contract
on the original Hilbert space. No dense-monitoring limit is asserted.

## G5. Energy moments, tails and limiting laws

For a positive normalized finite-energy density rho define M=Tr(G rho).
Let L bound ideal and actual half-graph history amplitudes, and d the
half-graph difference in (9). Their unnormalized final energy moments are
m_Q=||H^(1/2)Q rho^(1/2)||_HS^2. H^(1/2) S^-1 is a contraction, so

  |m_Qa-m_Q| <= (L_a+L_i) d M.                          (10)

Indeed each Hilbert-Schmidt norm is at most L_(a/i) sqrt(M), and their
difference norm at most d sqrt(M); apply the difference of squared norms.
This argument needs only initial first energy, not a second moment.

For varying rho_a with d_E=||S(rho_a-rho)S||_1->0, an additional moment
error is at most L_a^2 d_E: the conjugated positive form
S^-1 Q_a* H Q_a S^-1 is bounded by L_a^2 in norm and pairs with the signed
weighted trace-class difference. Branch probabilities differ by the ordinary
product norm and ||rho_a-rho||_1. No unjustified continuity of square roots
in the weighted trace norm is used here.

For fixed rho, uniform full and half graph bounds reproduce the accepted
cutoff tail argument for all Q_a whenever epsilon b remains bounded. The
constants are uniform and the initial tail modulus is common; hence actual
branch final energies are uniformly integrable. For varying rho_a converging
in d_E, compare the positive tail form
S^-1 Q_a* H 1_{H>R} Q_a S^-1, whose norm is at most L_a^2. Thus the actual
initial-state replacement changes each tail by at most L_a^2 d_E uniformly
in R. This gives lim_R limsup_joint tail=0; it does not assert uniform tails
on every arbitrary punctured continuum parameter neighborhood. Weighted
compact initial families or a convergent sequence do give uniform tails.

Combine (10) and ordinary actual/ideal norm convergence with an already
proved ideal weak finite-history law. The actual branch mass and first
moment converge. For any selected history of limiting probability p>0,
normalization is valid eventually and its conditional final-energy law
converges weakly and in first moment, hence in W1 on [0,infinity). Zero-mass
histories retain only unnormalized conclusions. Uniform conditional claims
require a common positive probability floor and the relevant compact-family
initial controls. The ideal weak-limit regular-boundary premises remain
required; arbitrary bins in (9) do not erase them.

## G6. Source application, limits and decisive checks

Under the accepted fixed-resource ideal q2 hypotheses, every retained common-H
actual-cell error pair of order epsilon can use this abstract sharpening.
If epsilon=a^(N+1), the sufficient joint scale becomes
 a=o(h^(1/(N+1))) instead of the earlier a=o(h^(2/(N+1))).
This is conditional on both error norms (2) and the ideal graph theorem;
it neither builds a physical embedding nor applies to arbitrary energy-ball
initial families. The old published sufficient estimates are not false and
are not silently edited. The threshold protocol application remains dependent
on its complete accepted composition, not merely on the marginal law.

Checks: (i) finite-dimensional H=0 reduces(3)-(8) to standard bounded-generator
stability and gives zero energy moments; (ii) DeltaV commuting with H gives
d1=0, and the graph-generator estimate uses only ideal graph constants;
(iii) if ideal graph constants grow with h, the correct condition is
C_G^2 epsilon b->0 and C_G expm1(C_G^2 dG epsilon b)->0, not automatically
epsilon=o(h); (iv) an energy-ball family without common initial tails is
still excluded by the archived escaping-energy countercontrol; (v) (6)
requires the inverse ideal graph bound, so bounded forward action alone is
not substituted. These are analytic checks, no numerical/Lean executions.

Open at this seal: independent reconstruction and complete source-exposed
comparison; no regular PR, retained verdict or formal domain verification.
<!-- END IMMUTABLE A -->

## Appendix B — Independent derivation

The following body is an unchanged historical source. The current wrapper
and archived final review govern export scope and current status.

<!-- BEGIN IMMUTABLE B sha256=c2f208d2b05d43167f6beb18b2f30cedc01e3ff6b430ed8f39ed24ff57a2c5b3 -->
# Perturbation in a uniformly bounded ideal energy graph

## 1. Conditional result and exact scope

The supplied uniform forward and inverse ideal energy graph bounds improve
the sufficient calibration scale to epsilon=o(h). More precisely, the
small parameter is epsilon b_h, where b_h is the integrated absolute drive
budget. The proof below gives uniform full and half graph differences of
order epsilon b_h when epsilon b_h tends to zero. Merely bounded epsilon b_h
gives uniform actual graph bounds, but does not by itself give convergence
to the ideal histories.

This is an improvement of the weighted propagator comparison needed for
energy observations. It does not assert that the unweighted operator norm
of [H,Y_a-Y] improves from the earlier coarse commutator estimate.
The exact common H, common spectral instrument and the stated calibration
remain hypotheses; no physical cell construction or new empirical claim
is supplied.

For kinetic time T<=tau_star/h^2 and bounded amplitude, b_h<=C/h. Hence
epsilon=o(h) suffices for graph convergence, bounded finite history transfer,
and finite-energy branch means. Together with the established ideal weak
history and first-mean limits, it gives conditional final mean and W1 at
positive limiting success probability. No second initial energy moment is
required. Fixed arbitrary normal states still have bounded-history transfer.

A finite-dimensional resonant example in the evidence shows that
epsilon=O(h) does not guarantee ideal convergence under the abstract graph
and commutator assumptions. This tests the general perturbation theorem.
It is not a claimed sharpness theorem for the particular nonzero continuum
CAR control with fixed slots; that narrower optimality question is not
needed for the sufficient result proved here.

## 2. Premises and graph domains

Let H>=0 be the exact common self-adjoint free energy and G=1+H.
Write S=G^(1/2). Consider the ideal interaction-picture propagator Y_h(t,s)
and its endpoint Y_h(t)=Y_h(t,0), with real integrable drive f_h(t).
In the supplied application f_h(t)=lambda c_h(t), |lambda|=h, and

    b_h(t)=integral_0^t |f_h(u)|du <= A tau_star/h.              (1)

The ideal interaction is V_I(t)=exp(itH)V exp(-itH). The actual interaction
is V_I(t)+Delta V_I(t), with bounded self-adjoint Delta V and

    ||Delta V||<=d0 epsilon,
    ||[H,Delta V]||<=d1 epsilon.                               (2)

The commutator is a bounded graph-domain commutator; equivalently its form
on D(H) has a bounded extension. The latter condition implies
Delta V D(H) is contained in D(H) by the adjoint-domain criterion. Since
free rotations commute with G and S, (2) holds equally in interaction
picture for every t.

The established ideal input is, for q=1/2 and q=1,

    sup_(h,t) ||G^q Y_h(t) G^-q|| <= M_q,
    sup_(h,t) ||G^q Y_h(t)* G^-q|| <= M_q.                      (3)

These are actual domain-preserving bounded extensions. The supplied ideal
propagator is strongly continuous on the graph spaces. In this model that
property follows at every fixed h from the bounded interaction with bounded
first commutator, before using any uniform kinetic estimate. It can also be
included explicitly as the evolution regularity premise of the abstract
statement. Uniform graph bounds alone are not used as a substitute for
existence of a graph-space evolution.

The endpoint bounds imply the interval bound

    ||G^q Y_h(t,s) G^-q|| <= M_q^2,
    Y_h(t,s)=Y_h(t)Y_h(s)*.                                  (4)

Thus the proof does not assume an independent uniform interval theorem.
It uses both directions of (3); forward bounds alone would not control
the generator in the ideal interaction frame.

## 3. The small perturbation is bounded on the graph

On D(H), using ||G^-1||<=1,

    G Delta V G^-1 = Delta V+[H,Delta V]G^-1,
    ||G Delta V G^-1|| <= (d0+d1)epsilon.                     (5)

Set D_1=d0+d1 and D_(1/2)=sqrt(d0(d0+d1)). Interpolation between
the Hilbert norm and the full graph norm gives

    ||S Delta V S^-1|| <= D_(1/2) epsilon.                    (6)

One may replace D_(1/2) by the weaker D_1 without changing any rate. The
interpolation follows by applying the three-lines bound to G^z Delta V G^-z
on spectral-compact vectors, then taking graph cutoffs. Imaginary powers
of G are unitary. If d0=0 then Delta V=0 and (6) is exact with zero.

For q in {1/2,1}, define the ideal-frame perturbation

    B_h(t)=Y_h(t)* Delta V_I(t) Y_h(t).

It is bounded self-adjoint on the Hilbert space. By (2), (3), (5)--(6),

    ||G^q B_h(t) G^-q|| <= M_q^2 D_q epsilon
                         = kappa_q epsilon.                 (7)

Its graph action is strongly measurable and bounded. In particular, the
integrated graph generator has norm budget at most kappa_q epsilon b_h.
No factor b_h from a separately estimated ideal commutator is introduced.

## 4. Construct actual domain preservation rather than assuming it

Solve on the graph space X_q=D(G^q), with norm ||G^q psi||,

    R_h'(t)=-i f_h(t) B_h(t) R_h(t),   R_h(0)=I.              (8)

The generator is integrable in the strong graph sense and uniformly bounded
by (7). Its chronological Dyson series converges as bounded operators on
X_q, with nth term norm at most (kappa_q epsilon b_h(t))^n/n!.
Consequently

    ||G^q R_h(t) G^-q|| <= exp(kappa_q epsilon b_h(t)),
    ||G^q (R_h(t)-I) G^-q||
       <= exp(kappa_q epsilon b_h(t))-1.                      (9)

The same series on the Hilbert space has a unique solution. Since B_h(t)
is self-adjoint and f_h real, that solution is unitary. Compatibility on
the dense graph domain identifies the graph-space and Hilbert solutions.

Define Y_a,h(t)=Y_h(t)R_h(t). The product differentiation in Hilbert space
gives the actual bounded-interaction equation with generator
f_h(t)(V_I(t)+Delta V_I(t)). Uniqueness identifies it with the actual
propagator. Thus Y_a,h preserves X_q by construction; actual graph-domain
preservation was not assumed to justify its own estimate.

The inverse requires a separate argument. The backward, right-ordered
Dyson equation

    Q_h'(t)=i f_h(t) Q_h(t) B_h(t),   Q_h(0)=I

has the same graph series bounds. The product rule gives Q_h R_h=I.
Hilbert-space uniqueness and unitarity identify Q_h=R_h*, hence also
R_h Q_h=I; both identities restrict to the graph space. Therefore

    ||G^q (R_h(t)*-I) G^-q||
       <= exp(kappa_q epsilon b_h(t))-1.                      (10)

This is not obtained by taking the Hilbert adjoint of G^q R_h G^-q,
whose adjoint has the reversed weights. Right-ordered inverse construction
is what proves the needed domain and estimate.

## 5. Improved endpoint and interval comparisons

Since Y_a,h-Y_h=Y_h(R_h-I), and
Y_a,h*-Y_h*=(R_h*-I)Y_h*, (3), (9) and (10) give

    ||G^q (Y_a,h(t)-Y_h(t))G^-q||
      <= M_q [exp(kappa_q epsilon b_h(t))-1],
    ||G^q (Y_a,h(t)*-Y_h(t)*)G^-q||
      <= M_q [exp(kappa_q epsilon b_h(t))-1].                 (11)

Likewise the actual forward and inverse graph norms are at most
M_q exp(kappa_q epsilon b_h(t)). An interval [s,t] has the same relative
Dyson construction with budget b_h(t)-b_h(s) and outside ideal factors
Y_h(t),Y_h(s)*, giving the analogous difference with M_q^2 in place of M_q.

Thus epsilon b_h(tau_star/h^2)->0 gives uniform forward/inverse full and
half graph convergence. For the specified kinetic budget, epsilon=o(h)
is sufficient, with graph error O(epsilon/h). Bounded epsilon/h supplies
uniform actual graph norms through the exponential, even when the graph
difference need not vanish.

Unweighted Duhamel also gives

    sup_t ||Y_a,h(t)-Y_h(t)|| <= d0 epsilon b_h.               (12)

The same bound holds for adjoints. The earlier epsilon(b_h+b_h^2)
commutator estimate is consistent but weaker for this purpose. It estimates
ideal commutators separately in the unweighted operator norm; (7) instead
uses the already available ideal graph maps as a whole.

## 6. Fixed finite spectral histories

Let Q_j=1_(B_j)(H) be any fixed Borel spectral projections of the common H.
They contract both X_q. Let

    P_j=Y_h(t_j)* Q_j Y_h(t_j),
    P_a,j=Y_a,h(t_j)* Q_j Y_a,h(t_j).

Under epsilon b_h->0, (3) and (11) imply uniformly bounded graph norms of
these projections and vanishing graph norm differences, of order
epsilon b_h. For example, insert and subtract Y_h* Q_j Y_a,h and use
the two differences in (11). No commutativity of different P_j is needed.

For a fixed chain and final observation time define

    T_h=Y_h(t_f)P_n ... P_1,
    T_a,h=Y_a,h(t_f)P_a,n ... P_a,1.

Finite telescoping in the Banach algebra of bounded graph maps gives

    ||G^q (T_a,h-T_h)G^-q|| ->0,
    sup_h [||G^q T_a,h G^-q||+||G^q T_h G^-q||] <infinity.    (13)

The constants depend on the fixed n and ideal graph constants. The
unweighted versions follow from (12). Consequently all bounded history
probabilities and bounded final-energy tests transfer to the ideal ones
for any fixed normal initial density. Ordinary trace convergence of moving
initial densities is enough for that bounded comparison.

This actual-versus-ideal comparison works for any fixed common Borel bins.
Identifying a limiting classical history law still requires the regular
boundary or common zero-gap hypotheses of the established ideal theorem.
The comparison does not remove those hypotheses or prove new ideal limits.

## 7. Finite first energies transfer directly

For a fixed finite-energy rho, put A=S rho S, a positive trace-class
operator with Tr A=1+Tr H rho. For either history chain put

    F_h=H^(1/2) T_h S^-1,
    F_a,h=H^(1/2) T_a,h S^-1.

Since ||H^(1/2)S^-1||<=1, the q=1/2 part of (13) gives bounded F_h,F_a,h
and ||F_a,h-F_h||->0. Quadratic forms on D(S), followed by density, give

    Tr rho T_h* H T_h = Tr A F_h* F_h.                       (14)

Hence actual minus ideal unnormalized history-weighted final mean tends
to zero, bounded in absolute value by

    Tr A (||F_a,h||+||F_h||)||F_a,h-F_h||.                    (15)

This direct energy-form comparison needs only the first initial moment.
It does not infer an unbounded mean from the norm estimate (12).

For normalized moving rho_a with

    d_E(rho_a,rho)=||S(rho_a-rho)S||_1 ->0,                  (16)

the additional mean error is at most d_E(rho_a,rho)||F_a,h||^2. Thus (15)
still gives convergence to the ideal mean along the stated joint limit.
Together with bounded-law convergence and the ideal first-mean theorem,
this proves the same unnormalized actual means. At a history event of
positive limiting probability, division by its converging mass gives
conditional weak convergence and convergence of first moments, hence W1
on the nonnegative energy line. No zero-probability normalization follows.

One can alternatively obtain the required tails from the actual full and
half graph bounds and the established two-cutoff estimate. For moving
states, (16) gives precisely

    lim_(L->infinity) limsup_(joint limit) Tr rho_a G1_(H>L)=0.

A convergent sequence or weighted-trace-compact family has genuine uniform
tails. A blanket supremum over every point in a fixed punctured continuum
neighborhood is not implied. The direct form comparison above avoids any
need to strengthen this quantifier.

Finite unions of measured records sum their positive branch measures;
coherently summing chain operators would describe another instrument.
Measurement count and bins are fixed; no increasing-record or moving-bin
extension is inferred.

## 8. Source boundary, novelty of this check and disposition

The pre-target neutral plan was sealed at SHA256
5123f69db72250d6f31802c9cf5726ca5626e92d6575109d394a3241d01693ab.
Its disclosure includes prior exposure to root211's coarse commutator
estimate and my own earlier proof/comparison. New root perturbation plan,
probe and findings remained unread throughout this derivation and freeze.

Eight exact source bodies in SOURCE_INVENTORY.json were already fully read
and were reused only after unchanged hashes were verified. Root306 and
independent390, with the mandatory linear/unitary J precision, supply the
ideal graph premise; fresh702 supplies the threshold protocol interface.
The present proof begins from the explicit graph bounds (3), not an unstated
ancestor theorem. No new reading or certification of corrected859 or other
unread ancestors is claimed.

The new load-bearing calculation is (7)--(11), with actual domains and
inverse graphs constructed before use. Equations (13)--(16) supply the
measurement-chain consequence directly. The evidence file independently
checks the frame equation, factorial bound, inverse order, endpoint/interval
distinction, resonant critical scale, and finite-energy form comparison.

Within these explicit hypotheses, no residual step is left in the sufficient
epsilon=o(h) implication. Optimality for the specified nonzero continuum
CAR slot control remains unclaimed. Parent comparison and ordinary
acceptance are pending. This is not retained science or a formal audit.
No scientific runtime, CW/Git mutation, prompt/axiom change, subdelegation,
other-chat contact, source assembly or publication occurred. Original
frozen sources remain unchanged.
<!-- END IMMUTABLE B -->

## Appendix C — Independent analytic evidence

The following body is an unchanged historical source. The current wrapper
and archived final review govern export scope and current status.

<!-- BEGIN IMMUTABLE C sha256=5c59ba4d4f587d547283c21cbd5afb6466d98732df86b76ba7eb50630a89cf5b -->
# Analytic checks for ideal-frame energy graph perturbation

These checks are analytic, source-exposed to the inherited graph theorem,
and unexposed to the new root perturbation argument. No scientific runtime
is used. They test the new relative-frame construction and its consequences.

## E1. Frame equation and graph generator

The ideal equation is Y'=-i f V_I Y. For a proposed actual equation
Y_a'=-i f(V_I+Delta V_I)Y_a, put R=Y*Y_a. Differentiation yields

    R'=i f Y*V_I Y_a-i f Y*(V_I+Delta V_I)Y_a
      =-i f(Y* Delta V_I Y)R.

The ideal terms cancel exactly, before taking any norm. With G=1+H,

    G(Y* Delta V_I Y)G^-1
    =(GY*G^-1)(G Delta V_I G^-1)(GYG^-1).

Each product is legitimate on D(H) and has a bounded extension. Both
ideal directions are needed. Its norm is bounded by M_1^2(d0+d1)epsilon.
Estimating [H,Y] separately would unnecessarily restore a factor b.

For construction, the logic is reversed: define the graph-space solution
R first and then Y_a=YR. The Hilbert equation and uniqueness identify
Y_a as the actual propagator. This avoids assuming actual graph regularity
before proving it.

## E2. Time simplex and domain compatibility

The nth graph Dyson term is an integral over
0<t_n<...<t_1<t of n generator factors. Bounding each graph generator by
kappa epsilon |f(t_j)| gives

    (kappa epsilon)^n integral_simplex product_j |f(t_j)|dt_j
    = (kappa epsilon b(t))^n/n!.

The scalar product integrand is symmetric; the simplex occupies one of
n! orderings up to measure-zero equal-time sets. Summing n>=0 gives the
exponential bound and summing n>=1 gives the difference from I.
This estimate remains valid for sign-changing or merely integrable f.

Strong graph continuity of the ideal maps and bounded graph action of
Delta V make the relative generator strongly measurable on D(G^q).
Strong integrals and the norm bound suffice; operator-norm continuity is
not required. The series converges on both the graph space and Hilbert
space to compatible operators. The latter solution is unitary because
the Hilbert generator is self-adjoint times a real scalar.

The proof imports the supplied graph regularity of the ideal evolution,
which also follows here from bounded [H,V] at each fixed h. It does not
deduce graph continuity merely from a uniform collection of norm bounds.

## E3. Inverse order and intervals

The inverse is constructed by Q'=i f Q B, with multiplication on the
right. Its series has the reversed chronological order and the same
factorial norm estimate. Differentiating QR gives zero, so QR=I.
In Hilbert space, uniqueness and unitarity give Q=R*, hence also RQ=I.
This proves that the Hilbert adjoint preserves the graph domain.

Taking the adjoint of GRG^-1 would instead give G^-1 R* G. That is the
wrong graph weight and is not used. The actual adjoint difference is

    Y_a*-Y*=(R*-I)Y*,

so its bound has the same ideal prefactor as the forward difference.

For an interval [s,t], the relative propagator is R(t,s)=R(t)R(s)* and

    Y_a(t,s)=Y(t)R(t,s)Y(s)*,
    Y(t,s)=Y(t)Y(s)*.

Its Dyson generator is the same B(u), now integrated from s to t. Thus
only b(t)-b(s) enters the exponential; outside ideal factors contribute
M_q^2. Bounding R(t)-I and R(s)*-I separately would give a valid but
weaker estimate depending on the full endpoint budgets.

## E4. Calibration regimes and a resonant critical-scale test

The estimate is M_q[exp(kappa_q epsilon b)-1]. Therefore:

- epsilon b tends to zero: graph differences vanish, with order epsilon b.
- epsilon b stays bounded: actual graph norms stay bounded.
- epsilon b grows without bound: this estimate gives no uniform conclusion.

The third statement is a limitation of the estimate, not a proof of
divergence. If b=0, the difference is exactly zero. A smaller actual drive
budget permits a weaker calibration requirement than replacing b by C/h.

For a direct critical-scale control, take a two-level Hilbert space with
H=diag(0,omega), omega>0, ideal V=0 and Delta V=epsilon sigma_x.
The ideal graph maps are the identity. Also

    ||Delta V||=epsilon,
    ||[H,Delta V]||=omega epsilon.

Take the fixed drive f_h(t)=h cos(omega t) and T=tau/h^2. Write
sigma_+=|1><0|, sigma_-=|0><1| and g=h epsilon. The actual interaction
equation has generator g[A+B(t)], where

    A=sigma_x/2,
    B(t)=[exp(2i omega t)sigma_++exp(-2i omega t)sigma_-]/2.

The primitive F(t)=integral_0^t B(s)ds is uniformly bounded by a constant
depending only on omega. Let Z(t)=exp(-igAt). Variation of constants gives

    Y_a(t)-Z(t)=-ig integral_0^t Z(t-s)B(s)Y_a(s)ds.

Integrate B=F' by parts. The endpoint term is bounded by ||F||_infinity;
the derivative terms are bounded by
g t ||F||_infinity (||A||+sup||A+B||). Thus

    ||Y_a(t)-Z(t)|| <= C_omega(g+g^2 t).                     (E1)

If epsilon=k h with fixed k>0, then g=k h^2. At T=tau/h^2 the right side
of (E1) tends to zero, while

    Y_a(T) -> exp(-i k tau sigma_x/2).

For k tau not a multiple of 2pi this differs from ideal I. Starting in
the zero-energy state, the final mean tends to
omega sin^2(k tau/2), while the ideal mean is zero. Choosing k tau not a
multiple of 2pi makes this strictly positive.

This example obeys the abstract common-energy, bounded commutator and
uniform ideal graph hypotheses, with a fixed positive-frequency cosine
drive and bounded resources. It shows that epsilon=O(h) cannot guarantee
ideal graph or energy convergence for that abstract class. It does not
establish optimality for the specific continuum CAR slot control: that
model has additional structure not represented by this two-level example.

## E5. A commuting phase and the meaning of convergence

If Delta V=v I, then the relative perturbation is v I and
R(t)=exp(-i v integral_0^t f(s)ds)I. Its exact graph error equals the
scalar phase error. The absolute-budget bound remains valid, though drive
cancellations may make it very loose. Energy histories are identical even
when the scalar phase does not converge to one.

Thus graph convergence is a sufficient route to energy convergence, not
a necessary condition for every special perturbation. The claimed scaling
is sufficient for the entire stated class and does not prohibit stronger
conclusions under additional structure or cancellations.

## E6. Measurement chains and the first-energy form

For q=1/2 or 1, let ||A||_q=||G^q A G^-q|| on bounded graph maps.
It is submultiplicative. Every common spectral projection Q_j has
||Q_j||_q<=1. Subtracting
P_a,j=Y_a,j*Q_jY_a,j and P_j=Y_j*Q_jY_j yields two terms, each with one
propagator difference. Their graph norm is O(epsilon b) with bounded
constants. A length-n product then differs by a sum of n terms, each
containing exactly one difference and finitely many uniformly bounded
graph factors. Fixed n is used here.

Let A=S rho S and F=H^(1/2)TS^-1. For a vector psi in D(S),

    ||H^(1/2)T psi||^2=||F S psi||^2.

Summing a density decomposition, using nonnegative forms and monotone
finite partial sums, gives Tr rho T*H T=Tr A F*F. This establishes the
trace identity without assuming Tr rho H^2 is finite.

For actual and ideal chains,

    ||F_a*F_a-F*F|| <= (||F_a||+||F||)||F_a-F||.

The half-graph chain difference bounds ||F_a-F||, because
H^(1/2)S^-1 is a contraction. Multiplication by Tr A therefore controls
the entire mean error using the first initial energy only. For moving
states an additional weighted trace-norm error multiplies ||F_a||^2.

This direct comparison is stronger than trying to apply the unweighted
propagator estimate to the unbounded H. Full graph bounds remain useful
for the independent tail route and are also proved by the same Dyson
construction. Positive limiting event probability is still required to
normalize branch measures; finite unions sum positive branches.

## E7. What is and is not independently established here

The inherited ideal graph theorem and ideal protocol law are exposed exact
premises. The independent new work is the relative graph generator bound,
the graph-compatible construction of actual evolution and its inverse,
the epsilon b estimate and the direct finite-energy chain comparison.
The resonant calculation tests the scale in the abstract class analytically.

No new root perturbation source was read. No numerical or symbolic runtime,
scientific test program, CW/Git mutation, audit, prompt/axiom change,
subdelegation or source assembly was performed. Sharpness for the nonzero
continuum slot control remains outside the proved claim. Parent comparison
and ordinary acceptance are pending.
<!-- END IMMUTABLE C -->

## Appendix D — Separate review analytic evidence

The following body is an unchanged historical source. The current wrapper
and archived final review govern export scope and current status.

<!-- BEGIN IMMUTABLE D sha256=24cb231fcaa5ca8fffbba28d3bd40578d5c6a3ea06a4f0fa5f727e6c4a8c9020 -->
# Decisive analytic reconstruction of the relative-graph perturbation argument

This is a source-exposed calculation from exact rootV2/0906b061. It does not
use the separately deriving independent target. H>=0 is self-adjoint,
G=1+H, S=G^(1/2), g=lambda c is real and integrable, b=integral|g|.
All graph constants below are uniform over the parameter family unless
explicitly labeled otherwise. No proposed-science runtime was executed.

## E1. Closed-domain graph conjugation and measurability

Equip X=D(G) with norm ||x||_X=||Gx||. This is a complete Hilbert space,
and G:X->H is an isometric isomorphism with bounded inverse G^-1.
A domain-preserving bounded DeltaV with bounded commutator satisfies, on X,

 G DeltaV G^-1 = DeltaV + [H,DeltaV]G^-1,
 ||G DeltaV G^-1|| <= (d0+d1)epsilon.

Thus this is an actual bounded operator identity, not a formal commutator.
Let U0(t)=exp(-itH), C=G DeltaV G^-1. Free conjugation of the graph
operator is U0(t)* C U0(t), up to the harmless chosen free-picture sign.
It is strongly continuous, because U0 is strongly continuous and C bounded.
It need not be norm continuous or operator-norm Bochner measurable.

Write Y_G=G Y G^-1 and Y_inv,G=G Y* G^-1. These are genuine inverses
by the assumed two-way domain invariance. Strong graph continuity and the
uniform inverse bound give strong continuity of both; alternatively use
Y_G(t)^-1-Y_G(s)^-1=Y_G(t)^-1(Y_G(s)-Y_G(t))Y_G(s)^-1.
Consequently B_G=Y_inv,G C_I Y_G is strongly continuous, with
||B_G||<=C_G^2(d0+d1)epsilon=k_G. Multiplication by the measurable scalar
g gives strongly measurable vector functions with integrable norm majorant.
In particular, all required integrals exist as Bochner integrals of vectors
in X or H. This uses no separability or measurability in the operator norm.

Here is an independent discriminator for that distinction. On a fixed Hilbert
space with orthonormal pairs e_n,f_n, let H e_n=0 and H f_n=n f_n. Define
DeltaV e_n=f_n/n and DeltaV f_n=e_n/n. It is bounded self-adjoint,
[H,DeltaV] e_n=f_n, [H,DeltaV] f_n=-e_n, and it preserves D(H).
However C_I(t)e_n=((n+1)/n) exp(i n t)f_n, up to the sign convention.
For distinct t,s in (0,2pi),

 ||C_I(t)-C_I(s)|| >= sup_n |exp(i n(t-s))-1| >= sqrt(3).

For irrational (t-s)/(2pi) the supremum is2; for a rational angle of order
q>=2, the largest chord among its roots is at least sqrt(3). The range is
therefore an uncountable uniformly separated set in operator norm. Any
norm-separable subset intersects it in only countably many points, so the
map is not essentially norm-separably valued on a time interval and is not
an operator-norm Bochner measurable map. It remains strongly continuous.
This meets the bounded-commutator hypotheses and confirms that rootV2's
vectorwise integral qualification is necessary and sufficient for its method.
This example is a scoped measurability diagnostic, not a physical no-go.

## E2. Dyson construction and both inverse orders

On X, recursively integrate the strongly measurable bounded generator
-i g(t) B(t). The ordered n-simplex term defines a bounded operator with
norm at most (k_G b)^n/n!, by the vector norm inequality and scalar simplex
integration. The resulting series converges in operator norm, although
its individual integrals were only constructed vectorwise. Its sum T_X is
strongly absolutely continuous on each vector and solves the integral
equation. The estimates are

 ||T_X||<=exp(k_G b), ||T_X-I||<=exp(k_G b)-1.

The embedding X->H is continuous. For x in X, the same vector equation
holds in H, with bounded integrable generator -i g B. Hilbert-space
uniqueness identifies T_X x with T x=Y*Y_a x. This proves forward graph
invariance without assuming it for Y_a.

For inverse invariance, construct the two-parameter graph propagator U(t,s)
using oriented integrals. Uniqueness gives U(t,s)U(s,r)=U(t,r) on each
vector. Hence U(0,t)U(t,0)=U(t,0)U(0,t)=I. The reverse series for
R(t)=U(0,t) obeys R'=i g R B, and has the same exponential norm and
R-I bounds. This proves both inverse orders without any unproved
operator-norm derivative. The Hilbert identification then gives R=T*=T^-1
on X and proves inverse graph invariance.

RootV2's displayed repair is also correct: RT has zero derivative, whereas
K=TR solves K'=-i g B K+i g K B. The identity solves this equation. The
difference of any two bounded solutions satisfies a norm integral inequality
with coefficient2|g|k_G, so Gronwall yields uniqueness. The evolutions are
operator-norm continuous by their integrable norm bounds. In the present
setting B_G is strongly continuous before multiplication by g, so strong
product differentiation can be justified at scalar Lebesgue points of g.
The two-parameter construction above additionally avoids reliance on choosing
common null sets for arbitrary operator-valued differentiability assertions.
V1's statement that (TR)' directly vanishes was wrong; V2 repairs it.

## E3. Forward, adjoint and half-graph difference estimates

Y_a=YT and Y_a*=T*Y*. Set x=C_G^2(d0+d1)epsilon b. Independently for
the two products,

 ||G Y_a G^-1||, ||G Y_a* G^-1|| <= C_G exp(x),
 ||G(Y_a-Y)G^-1|| <= C_G(exp(x)-1),
 ||G(Y_a*-Y*)G^-1|| <= C_G(exp(x)-1).

The adjoint estimate uses the graph inverse T*, not an equality between
weighted adjoint norms. Hilbert Duhamel gives ||D||<=d0 epsilon b for
each difference D, optionally capped by2.

For interpolation, let P_L=1_[1,L](G). D_L=P_L D P_L has operator norm
at most M0=||D|| and full-graph norm at most M1=||G D G^-1||. On the
spectral subspace P_L H, log G is bounded. Three-lines applied to scalar
matrix elements of G^z D_L G^-z gives
||G^(1/2) D_L G^(-1/2)||<=sqrt(M0 M1). Let L increase to infinity;
density and closure yield the same bounded extension for D. No finite-rank
assumption on P_L and no operator-order squaring rule is needed.
This proves (7) and

 delta_S <= sqrt(d0 epsilon b C_G(exp(x)-1)).

Applying the same interpolation to the individual unitaries gives half-graph
norms <=sqrt(C_G exp(x)), and <=sqrt(C_G) for ideal factors. With fixed
C_G,d0,d1, both graph differences are O(epsilon b) as epsilon b->0.
The cases b=0 or DeltaV=0 are exactly zero differences. If d0=0, DeltaV=0
by (2), irrespective of a loose d1 bound. If [H,DeltaV]=0, d1=0 suffices,
but B=Y*DeltaV_I Y need not commute with H; retaining C_G^2 is correct.

## E4. Finite history products and positive first-energy forms

There are N=2n+1 unitary factors and n identical H-spectral projectors in
Q=Y_f(Y_n*Pi_n Y_n)...(Y_1*Pi_1 Y_1). On either graph space, each
projector has norm<=1. Replace the N unitary factors one at a time. The
sum of N differences has norm <=N L_A^(N-1)delta_A. This establishes
(9), its adjoint-factor ordering and uniformity over arbitrary Borel bins
for this comparison. It is not a weak-limit regular-boundary theorem.
Both Q and Q_a contract on H.

For fixed finite-energy rho, X=S rho^(1/2) is Hilbert–Schmidt with
||X||_HS^2=M=Tr(G rho). The bounded factorization
H^(1/2)Q rho^(1/2)=(H^(1/2)S^-1)(SQS^-1)X
justifies its domain and norm, including noncommuting, nonquasifree rho.
The corresponding difference has norm <=d sqrt(M). Difference of squared
Hilbert–Schmidt norms therefore gives (L_a+L_i)d M exactly as in (10).

For varying rho_a, define the bounded positive operator associated with
S^-1 Q_a* H Q_a S^-1; it equals F_a*F_a for
F_a=H^(1/2)Q_a S^-1 and has norm<=L_a^2. Pairing it with the signed
trace-class S(rho_a-rho)S gives error <=L_a^2 d_E. This is an equality
of forms extended by bounded operators; it requires no unjustified square
root continuity. The identical argument applies to H1_(H>R), uniformly in R.
Ordinary probabilities differ by at most2||Q_a-Q||+||rho_a-rho||_1, and
||rho_a-rho||_1<=d_E, since G^-1/2 is a contraction.

## E5. Explicit cutoff tail and conditional scalar limits

Suppose the history norms obey ||GQ_aG^-1||<=C and ||SQ_aS^-1||<=L,
uniformly. Put P_K=1_[0,K](H). Splitting rho^(1/2) at this initial
projection gives the quantitative bound

 ||H^(1/2)1_(H>R)Q_a rho^(1/2)||_HS
 <= C sqrt((1+K)M/R)
    +L sqrt(Tr(G1_(H>K)rho)).

Indeed on H>R, H<=H^2/R, while
||G P_K rho^(1/2)||_HS^2<= (1+K)Tr(G rho). The other term uses the
half-graph bound. Fix K, send R to infinity, then K to infinity. The last
trace vanishes because the initial first energy is finite. This proves the
genuine fixed-state uniform tail assertion without a second moment or
finite-rank cutoff. If epsilon b is merely bounded, (6) provides the uniform
actual graph constants needed here; convergence is not necessary for UI.

For d_E(rho_a,rho)->0, tail replacement is bounded by L^2 d_E uniformly
in R. Therefore the correct assertion is lim_R limsup_joint tail=0.
A d_E-compact family has finite nets and bounded first energy, yielding a
common tail modulus. A convergent sequence plus its limit is compact, so
it also has uniform tails under uniform history constants. An arbitrary
fixed punctured continuum parameter neighborhood is not made compact by
convergence at its missing limit point; no such uniformity is inferred.

If the ideal regular-protocol weak law is given, the bounded-observable
comparison above transfers it. Ideal and actual tail control gives convergence
of unnormalized first moments; (10) also transfers an existing ideal mean
limit directly. For branch masses tending to p>0, normalize eventually:
weak convergence and convergence of first moments on [0,infinity) imply
W1 convergence. The conditional mean is the limiting unnormalized mean
integral x dmu divided by p. At p=0 only the unnormalized conclusions are
retained. A uniform normalized statement requires a success-probability floor
and the stated initial-tail/ideal-limit controls. No regular-boundary premise
is lost by the stronger arbitrary-bin comparison bound.

With b<=C/h and fixed resource constants, epsilon=o(h) is sufficient. For
fixed calibration order p>=0 and epsilon=a^(p+1), this is a=o(h^(1/(p+1))).
For example, a=h^(3/(2(p+1))) satisfies the new condition and need not satisfy
the older a=o(h^(2/(p+1))). The older bound remains valid; neither is claimed optimal.

## E6. Scope precision for nonuniform ideal graph constants

Root G6(iii)'s C_G-dependent conditions control the single-propagator
full-graph difference C_G expm1(C_G^2 dG epsilon b). They must not be read
as a replacement for uniform C_G in all finite-chain, tail and mean results.
The product estimate contains additional L_A powers, and uniform tails need
uniform graph constants or separately checked substitutes.

A decisive example uses fixed H e_0=0, H e_n=n e_n on l2, fixed rho equal
to the e_0 pure state, and Y_n rotating span(e_0,e_n) by theta_n=1/sqrt(n).
Choose a strongly continuous prefix rotation and Y_a,n=Y_n, DeltaV=0.
Then ||G Y_n^(*)G^-1|| grows like sqrt(n), while both proposed perturbation
conditions in G6(iii) are zero. Nevertheless the final energy law is
cos^2(theta_n)delta_0+sin^2(theta_n)delta_n. It converges weakly to delta_0,
its mean n sin^2(theta_n)->1, and its first-energy tails are not uniformly
integrable. This is outside G1's uniform-C_G assumption and is not a
counterexample to the fixed-resource theorem. It proves that the phrase
“correct condition” in G6(iii) is only a single-propagator convergence
qualification; exporting it to G4–G5 requires additional hypotheses.
<!-- END IMMUTABLE D -->
