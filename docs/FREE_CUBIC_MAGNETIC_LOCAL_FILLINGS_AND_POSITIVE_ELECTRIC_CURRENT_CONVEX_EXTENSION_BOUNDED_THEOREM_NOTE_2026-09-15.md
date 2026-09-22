---
claim_id: free_cubic_magnetic_local_fillings_and_positive_electric_current_convex_extension_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the supplied finite-clock Villain law on free four-dimensional cubic boxes, a boundary-compatible local integer filling extends the provisional carrier theorem to the actual magnetic Hodge kernel. Its locally marked source has uniform curvature bounds. At the stated sufficient smallness, summing magnetic defects gives an exact positive electric-current marginal with a uniformly convex real extension in the Coulomb current metric. The integer marginal retains both defects; no fixed-clock photon limit follows."
upstream_dependencies:
  - carrier_preserving_closed_integer_charge_gas_convexification_bounded_theorem_note_2026-09-15
  - finite_clock_exact_coupled_electric_magnetic_defect_representation_bounded_theorem_note_2026-09-15
runner: scripts/free_cubic_magnetic_local_fillings_and_positive_electric_current_convex_extension_2026_09_15.py
---

# Local magnetic fillings and the exact positive electric-current extension

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

For the supplied finite-clock Villain law on free four-dimensional cubic boxes, a boundary-compatible local integer filling extends the provisional carrier theorem to the actual magnetic Hodge kernel. Its locally marked source has uniform curvature bounds. At the stated sufficient smallness, summing magnetic defects gives an exact positive electric-current marginal with a uniformly convex real extension in the Coulomb current metric. The integer marginal retains both defects; no fixed-clock photon limit follows.

These proposed analytic results await independent review and formal audit.
No native law, primitive, axiom or physical parameter is selected or changed.

## Status and proof obligations

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Identify a controlled effective field and the exact coupled-defect law needed for a fixed-clock physical-score theorem."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the boundary/source bridge and then control the integer-current infrared limit, preserving the current lattice and physical-score observables."
conditional_surface_status: "The supplied finite-volume law, integer topology, boundary kernel and explicit smallness/source conditions in the proof."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Self-contained derivation with distinct exact-cochain, Gaussian, Fourier and finite-enumeration challenges, without a phase inference."
```

The two explicit mathematical premises are the linked carrier theorem and
exact coupled-defect identity, with their stated hypotheses and scope.
The new proof below supplies the boundary and local-source bridge.
The finite executable reads no repository helper or scientific input file.
The thermodynamic phase and physical-score limit remain separate
obligations; neither is inferred from the finite checks.


| Premise | Revision status and precise use |
|---|---|
| [Carrier theorem](CARRIER_PRESERVING_CLOSED_INTEGER_CHARGE_GAS_CONVEXIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Linked bounded theorem; rooted mass bound, explicit constants and finite-dimensional variance estimate |
| [Coupled-defect law](FINITE_CLOCK_EXACT_COUPLED_ELECTRIC_MAGNETIC_DEFECT_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-09-15.md) | Linked bounded theorem; exact integer-current/magnetic-coset identity and source normalization |
| Cubic boundary filling and actual Hodge kernel | Derived in section1 and matched in section2 here |
| Positive electric marginal and convex extension | Derived in sections3-4; the extension away from integer currents depends on the fixed filling convention |
| Fixed-order photon law and matter | Open; no Gaussian limit is inferred from convexity |

## 1. Free cubic cochains and a local integer filling

Take the cubical complex [0,L]^d with all its cells and free boundary.
Write d_p:C^p->C^(p+1), with standard counting inner products. For
1<=p<d the Hodge Laplacian

 H_p=d_(p-1)d_(p-1)^*+d_p^*d_p

is positive definite and bounded above by4d. This follows explicitly by
tensoring interval complexes: on each coordinate the0-form Laplacian is
the path-vertex Laplacian, with a constant kernel, while the1-form
Laplacian is D D^T on interval edges and is positive definite. In a
p-form tensor summand at least one coordinate is a1-form. Cross terms
cancel by the alternating signs, leaving the sum of the d one-coordinate
Laplacians. Their individual norms are at most4.

A connected closed integer p-form gamma, d_p gamma=0, has an integer
(p-1)-form n_gamma with d_(p-1)n_gamma=gamma, supported in a local cube
of side at most6||gamma||_1, and

 ||n_gamma||_infty<=d||gamma||_1.                       (1)

Here "local" allows a cube clipped by the physical boundary. The construction
is important, because free boundaries are not zero-extension boundaries.

Dualize gamma to a relative cubical(d-p)-cycle, with chains in the physical
boundary set to zero. The dual interval has interior vertices at primal
cell centers and endpoints on the physical boundary; endpoint half-cells
do not change integer incidence. Put S=||gamma||_1. A connected support
has coordinate diameter at most S-1 in cell bases, so its dual support
fits in a clipped cube of side at most S+2.

If this cube meets no physical boundary, contract its interval product
to a corner. The point projection annihilates cycles of positive degree
d-p. If it meets physical boundary faces but not an opposite pair, choose
one such face and contract in its normal direction onto that face. This
is a relative chain homotopy: other boundary faces are preserved, while
the chosen face is zero in the relative complex. Each input cell creates
at most one prism through a given output cell.

If enclosing the support requires opposite faces, choose the whole
physical cube. Because the domain is cubic, its side L is then at most
S+2. The relative interval complex has C0 generated by interior vertices
and C1 by all dual edges. Define h(v_x) as the path from the left boundary
to v_x. Then boundary h=I on C0, and P=I-h boundary on C1 sends only the
last edge to the whole interval chain, sending other edges to zero.
This is the integer projection onto the single relative1-homology generator.
All tensor differential and homotopy terms include the sign determined
by the sum of preceding coordinate degrees. Tensoring the identity
boundary h+h boundary=I-P gives a product chain
homotopy H=h_1+P_1h_2+...+P_1...P_(d-1)h_d. The product projection lives
only in total degree d and therefore vanishes on degree d-p<d. Thus the
relative cycle bounds. Each input contributes coefficient at most one to
any fixed output per coordinate term, even when an interval projection
extends its support. This proves the bound dS in(1).

Dualizing back enlarges base-cell boxes by a fixed number of lattice units.
The deliberately loose6S side bound and5S anchor radius from the carrier theorem
remain valid. A deterministic construction can be chosen once for each
charge and then made odd: n_(-gamma)=-n_gamma. This is not a claim for
arbitrarily anisotropic rectangles: a short boundary-crossing carrier can
then require a fill extending along a much longer direction. Cubic domains
are part of the theorem.

For a general closed q, decompose it into connected support components
under sharing a(p+1)cell and set

 n(q)=sum_components gamma n_gamma.

Local closure implies each component is closed. This integer filling is
component-additive, but it need not be a linear function of q.

## 2. The actual magnetic gas and a locally marked source

For d=4,p=3 put G_3=H_3^-1. The magnetic quotient of the actual free-box
U(1)/clock representation has q=d_2 k, and integer contractibility gives
all integer q with d_3q=0. On such q,

 <q,G_3q>=<q,(d_2d_2^*)^+q>=||P_perp k||^2.

This is the actual Hodge kernel in the coupled-defect theorem, not the componentwise
Dirichlet kernel in the carrier theorem. Its lower spectral bound G_3>=1/(4d) and
the local filling(1) are sufficient for the SAME Gaussian-split and
carrier proof with c=1/(8d). Its closure graph still has degree at most
Delta=2(d-p)(2p+1).

More generally define, on these free cubic cochains,

 Z_beta(f)=sum_{q integer,d_pq=0}
 exp[-2pi^2 beta<q,H_p^-1q>] exp[2pi i<n(q),f>],         (2)

where f is any real(p-1)-form. Use exactly the t,R_t,C0,C1,epsilon_t
constants of the carrier theorem. After the local Gaussian split, a polymer has
activity

 z_gamma(phi;f)=exp[-t||gamma||^2]
    exp[2pi i(<gamma,phi>+<n_gamma,f>)].

In fact every phase depends on phi,f only through d^*phi+f, since
<gamma,phi>=<n_gamma,d^*phi>. The source modulus is one and charge
reversal conjugates it. Therefore
the same convergent rooted expansion is real and exponentiates to a
strictly positive polymer sum for every real phi,f under the stated
smallness condition. This is a positive representation of(2), proved by
cluster convergence; no source-dependent positivity is assumed.

A marked cluster C couples through n_C=sum_i n_gamma_i, so a simultaneous
variation (h,g) of (phi,f) differentiates its phase by

 2pi i<n_C,d_(p-1)^*h+g>.

The carrier proof hence yields the JOINT Hessian estimate

 |D^2 V_t(phi;f)[(h,g),(h,g)]|
 <=epsilon_t||d_(p-1)^*h+g||^2.                       (3)

All source variables remain real. The Gaussian effective action in phi
is uniformly convex whenever beta epsilon_t<1, with lower metric
(beta^-1-epsilon_t)H_p. Its normalization equals Z_beta(f), up to the
same source-independent Gaussian constant.

Write F(f)=log[Z_beta(f)/Z_beta(0)]. The positive-source differentiation
identity and the finite-dimensional variance estimate from the carrier theorem give

 -epsilon_t||g||^2 <=D^2F(f)[g,g]
 <=epsilon_t/(1-beta epsilon_t)||g||^2.                (4)

To check the cross term carefully, (3) implies a bounded bilinear form
A of norm at most epsilon_t on the image of T(h,g)=d^*h+g: the Hessian
annihilates ker T and factors through T. Thus the phi-gradient of
D_fV[g] has H_p^-1 norm at most epsilon_t||g||, since
||H_p^-1/2 d_(p-1)||<=1. The variance term is bounded by
epsilon_t^2||g||^2/(beta^-1-epsilon_t). This proves(4), including its
nonnegative variance contribution.

Charge reversal gives F(0)=0, DF(0)=0. Since(2) is the characteristic
function of the component-filled integer field n(q), positivity and the
triangle inequality give

 -epsilon_t||f||^2/2 <=F(f)<=0,
 4pi^2 Var(<n(q),g>)<=epsilon_t||g||^2.                (5)

The function n(q) is nonlinear; its source is explicitly defined. No
arbitrary real-source invariance under changing integer fillings is claimed.

## 3. Matching an integer electric current

Let J be a conserved integer1-current on the same free cubic complex:
d_0^*J=0. Set G_1=H_1^-1 and f_J=d_1G_1J. Then

 ||f_J||^2=<J,G_1J>,
 d_1^*f_J=J.                                         (6)

The second identity uses absence of1-cohomology and conservation. If
k is any integer plaquette representative with d_2k=q, then k-n(q)
is an integer exact2-form d_1ell. Consequently

 exp[2pi i<k,f_J>]=exp[2pi i<n(q),f_J>],

because the phase difference is2pi i<ell,J>, an integer multiple of2pi i.
This endpoint identity holds for integer currents. For a real current the
same chosen component-fill source defines an extension, but need not equal
a different representative's source.

The continuous-angle Wilson numerator therefore factors exactly into
its Gaussian electric part and the locally marked magnetic characteristic:

 <exp[i<J,theta>]>_U(1)
 =exp[-<J,G_1J>/(2beta)] exp[F(f_J)].                  (7)

Under the proved smallness conditions,

 exp[-(beta^-1+epsilon_t)<J,G_1J>/2]
 <=<exp[i<J,theta>]>_U(1)
 <=exp[-<J,G_1J>/(2beta)].                             (8)

This is a finite-volume source bound for the matched actual magnetic law.
It is not a thin-loop continuum limit, charged-matter construction or a
full photon covariance theorem.

## 4. Exact positive electric marginal and a convex real extension

The coupled-defect theorem clock identity at zero external character sums over conserved
integer currents J=Na, where a ranges over the integer current lattice.
After summing all magnetic charges and removing a common source-independent
normalization, its positive weight is exactly

 w_N(a)=exp[-N^2<a,G_1a>/(2beta)+F(N d_1G_1a)].        (9)

Define the SAME expression for arbitrary real conserved a, using the
component-fill extension F already fixed in(2), and put H_e(a)=-log w_N(a).
Equations(4),(6) imply

 N^2(beta^-1-epsilon_t/(1-beta epsilon_t))<v,G_1v>
 <=D^2H_e(a)[v,v]
 <=N^2(beta^-1+epsilon_t)<v,G_1v>.                    (10)

Thus beta epsilon_t<1/2 gives a positive, uniformly convex real extension
in the Coulomb current metric:

 D^2H_e >=(N^2/beta)*(1-2beta epsilon_t)/(1-beta epsilon_t) G_1.

The restriction to the integer current lattice is the exact finite-clock
electric marginal, with both defect species integrated according to their
original law. Individual negative mixed summands have not been dropped.
The extension away from integer currents is a constructed mathematical
object depending on the chosen odd local fillings; its integer values
are invariant and physical. It is not a new microscopic degree of freedom.

The pointwise envelope follows immediately from(5):

 exp[-N^2(beta^-1+epsilon_t)<a,G_1a>/2]
 <=w_N(a)<=exp[-N^2<a,G_1a>/(2beta)].                  (11)

A pointwise weight or Hessian bound is not a small total-variation bound
in arbitrarily large volume, nor a Gaussian scaling theorem for the
integer-current gas. The remaining infrared argument must retain current
quantization and establish correlation asymptotics or an equivalent
physical reconstruction.

## 5. Finite verification design and scope

Check interval relative homotopies and their tensor products exactly,
including boundary-to-boundary cycles. Check the actual Hodge spectral
bound and energy/source equalities on finite3D/4D cubes. The coupled-defect theorem
three-cube data can verify(7),(9) directly, using an integer magnetic
section; a phase computed from another integer filling must agree at
integer currents but may disagree for real extensions.

The relative-chain controls also show why the domain restrictions matter.
A top-degree charge of unit mass in a long interval can require a fill
extending to a distant boundary. In a width-one rectangle, a relative
boundary-to-boundary1-cycle has fixed mass2 while its least filling grows
with the other side length. These exact controls do not contradict the
cubic,1<=p<d filling statement.

The pure kernel/character calculations do not certify the global cluster
theorem or every local filling support. Those assertions need the written
proof and independent review. The explicit beta=100,d=4 sufficient
constants from the carrier theorem continue to hold with the conservative identical
geometry constants. They do not identify a physical parameter or establish
a fixed-N=3 photon phase.

## 6. Finite evidence and negative-claim discipline

Four finite families check absolute, one-face-relative and full-relative
integer tensor homotopies; top-degree and anisotropic boundary controls;
actual three/four-cube Hodge spectra and source-energy identities; and
fifteen real-current Hessians for the exact one-mode magnetic quotient
of a single three-cube, compared with multiprecision finite differences.
That last finite quotient is a chain-rule control and does not execute the
uniform p<d filling theorem or a four-dimensional phase.

### N1 — Materially distinct attempted inferences

| Honesty | Inference attempted | Outcome |
|---|---|---|
| ATTEMPTED | Use an absolute contraction for every boundary carrier | The proof and exact tensor checks keep absolute, one-face-relative and full-relative homotopies distinct. |
| ATTEMPTED | Include top-degree charges under the same local support bound | Unit-mass top-degree interval charges require increasingly long fills;1<=p<d is retained. |
| ATTEMPTED | Replace cubic domains by arbitrary thin rectangles | A mass2 boundary-crossing carrier in a thin rectangle has an increasingly large least fill. |
| ATTEMPTED | Demand representative invariance for all real currents | Integer currents have phase ratio1; a half-current control has ratio-1. The real extension is explicitly constructed and convention-dependent. |
| ATTEMPTED | Differentiate the source normalization without its variance | The all-source bound retains the nonnegative variance term and the resulting denominator1-beta epsilon. |
| ATTEMPTED | Infer a photon limit from a convex extension of integer weights | The actual measure remains on the current lattice; its infrared correlations are an additional obligation. |

No route is ruled out by prior retained authority. These are distinct
assumption checks, not independent physical walls.

### N2 — Dependencies

This source composes two explicit provisional proofs. The boundary lemma
and source bridge are new obligations checked here; their use does not
retroactively give either premise independent retained status. Relations
to native formation, the N=3 penalty Hamiltonian and matter remain unknown.
The extension's metric convexity is not a theorem about current quantization.

### N3 — Hidden assumptions

Domains are free cubic boxes,1<=p<d, with the actual cubical Hodge kernel
and integer cohomology. Odd component fillings are fixed once. The source
extension for real currents is defined by those fillings; only integer
values have the original representative invariance. All smallness
conditions are explicit. The physical law has not acquired continuous
current variables or a new primitive.

### N4 — Residual matching

Relative homotopies test the same integer interval tensor construction.
Hodge matrices and source norms use the actual finite-cube incidence.
The exact three-cube scalar magnetic quotient checks a finite extension's
normalization and Hessian, not the universal cubic filling proof.
The positive marginal sums every magnetic charge and keeps the exact
electric current lattice; no negative mixed term is simply discarded.

### N5 — Resolution

The runner prints substantive per_element,per_site,per_mode,per_block and
lattice_wide evidence. The finite homotopies, rational source relations
and finite-difference Hessians are executed. General local fillings,
infinite cluster sums, all-box convexity and a physical infrared limit
are checked and not executed; the written proof carries the first three,
while the infrared limit remains open.

### N6 — Partial paths

The exact integer-current marginal and its controlled real extension
provide a specific next target. Its current lattice, source interaction
and physical-score correlations still require an infrared analysis.
A direct score argument remains possible. No axiom or primitive is
changed or declared inadequate by these bounds.

### N7 — Steelman

The main criticism is that a smooth convex extension is not the same as
a Gaussian scaling limit of an integer-current measure. This is correct,
even when the Hessian is close to its Coulomb quadratic form. Pointwise
weight bounds can accumulate volume-dependent normalization differences.
The construction supplies the exact integer marginal and a controlled
extension; it does not supply missing photon dispersion, charged matter
or a native probability law.

### N8 — Cross-cycle comparison

The carrier theorem's original Dirichlet kernel was narrower than the
actual magnetic law. This note explicitly proves the cubic-boundary and
Hodge-kernel bridge. The exact coupled-defect identity still has negative
individual mixed terms; complete magnetic summation gives the positive
marginal used here. Growing-coupling limits and fixed-law image-noise/Ward
distinctions retain their stated scope and are not promoted to phase proofs.

## 7. Personal review status

The derivation and all finite checks were performed personally without
subagents. Independent review and formal audit of all three linked sources
remain pending. The next step is the integer-current infrared theorem
and its match to physical-score observables.
