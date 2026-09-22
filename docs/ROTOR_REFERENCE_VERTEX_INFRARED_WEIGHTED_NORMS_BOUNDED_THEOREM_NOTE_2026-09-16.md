---
claim_id: rotor_reference_vertex_infrared_weighted_norms_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "Specified cubic Maxwell reference: exact low-frequency norm bounds, finite inverse-half-energy form and logarithmic bare inverse-energy norm with projector factor; local free-cube profile limit. Reference-domain statement only, not a physical no-go."
runner: scripts/rotor_reference_infrared_norm_check_2026_09_16.py
upstream_dependencies: ["rotor_global_gauss_dressing_coulomb_variational_compression_bounded_theorem_note_2026-09-16", "rotor_orthogonal_transverse_reference_current_vertex_bounded_theorem_note_2026-09-16"]
---

**Type:** bounded_theorem

# Infrared profile of the reference current vertex

**Status:** conditional-support under the explicitly supplied model/reference; independent retained-grade audit remains separate.

## 1. Exact reference symbol

For the unit-weight infinite cubic Maxwell reference, on k in [-pi,pi]^3, put

    d_i(k)=exp(i k_i)-1, omega(k)=sqrt(sum_i |d_i(k)|^2),
    P(k)=I-d(k)d(k)*/omega(k)^2,
    A(k)=omega(k)P(k).

The single zero Fourier point can be assigned arbitrarily for L2 statements. The transverse mode profile of an oriented link at the origin is

    v_i(k)=omega(k)^(-1/2)P(k)e_i.                    (1)

This is the bulk counterpart of K^(1/2)P e in orthogonal-reference theorem. Inner products use dk/(2pi)^3. The diagonal projector is

    ||P(k)e_i||^2=1-|d_i(k)|^2/omega(k)^2.

Its angular average near zero is 2/3, not one. This is a transverse two-polarization reference calculation.

## 2. Exact low-frequency integral and bounds

For 0<lambda<=1 use q_i=2sin(k_i/2). This is one-to-one on the Brillouin cube; omega=|q| and

    dk=J(q)dq, J(q)=product_i(1-q_i^2/4)^(-1/2).

The ball |q|<=lambda lies inside its image. Therefore

    ||1_(A<=lambda) v_i||^2
      =(2pi)^(-3) integral_0^lambda r dr
          integral_(S^2)(1-n_i^2)J(rn)dn.            (2)

The spectral projection in (2) is within the transverse space. It does not include the longitudinal zero eigenspace, on which v_i is zero.

For 0<=r<=1,

    1<=J(rn)<=(1-r^2/4)^(-3/2)<=1+r^2.

The last inequality follows by differentiating in r^2: the derivative is at most (3/8)(3/4)^(-5/2)<1. Since integral_(S^2)(1-n_i^2)dn=8pi/3, equation(2) gives the explicit bound

    lambda^2/(6pi^2)
      <=||1_(A<=lambda) v_i||^2
      <=lambda^2/(6pi^2)+lambda^4/(12pi^2).           (3)

Expanding the same smooth Jacobian uniformly gives

    J(rn)=1+r^2/8+O(r^4),
    ||1_(A<=lambda) v_i||^2
      =lambda^2/(6pi^2)+lambda^4/(96pi^2)+O(lambda^6).

The coefficients follow from the analytic integral, not a fit to the finite lattice sums.

## 3. Energy-weighted norms distinguish two obligations

For 0<sigma<lambda<=1 and p>=0, the same exact integral has radial factor r^(1-2p):

    ||1_(sigma<A<=lambda) A^(-p)v_i||^2
      =(2pi)^(-3) integral_sigma^lambda r^(1-2p)dr
          integral_(S^2)(1-n_i^2)J(rn)dn.            (4)

At p=1/2 the integral is finite down to sigma=0. Thus v_i is in the domain of A^(-1/2). At p=1,

    0 <= ||1_(sigma<A<=lambda) A^(-1)v_i||^2
           -(1/(3pi^2))log(lambda/sigma)
      <=(lambda^2-sigma^2)/(6pi^2).                  (5)

Consequently v_i is not in the domain of A^(-1). The coefficient 1/(3pi^2) is exact. Contributions away from k=0 are finite and cannot remove this positive logarithmic divergence.

The per-link leading vertex in orthogonal-reference theorem is (g/sqrt(2))eta v_i. At any fixed nonzero g and eta>0, its inverse-energy norm has coefficient g^2 eta^2/(6pi^2) multiplying log(1/sigma). Its energy-form norm remains finite. Multiplication by a matter-current matrix element that vanishes at low momentum could change this conclusion; no such matrix element has been supplied here.

## 4. Matching a local free-box form factor to the bulk reference

Center successively larger free cubes around a fixed link and embed their edge spaces in the infinite lattice. Their positive matrices C*C converge on finitely supported vectors, and are uniformly bounded by12. Continuous functional calculus therefore converges strongly. The function defining v_i is x^(-1/4) on x>0 and zero at x=0, so its singular endpoint needs an additional bound.

The tensor eigenfunction estimate used in Gauss-dressing theorem supplies that bound. For a fixed link, the spectral mass of K=(C*C)^(-1/2) on 0<sqrt(x)<=lambda is bounded above by the corresponding mass of H1^(-1/2) on that interval. The two operators commute with the Hodge decomposition and agree on S; the extra gradient contribution is nonnegative. Every tensor eigenfunction has squared value <=8/(L+1)^3 and sqrt(lambda_n)>=2|n|/(L+1). A shell sum up to |n|_infinity<=(L+1)lambda/2 bounds the mass by C lambda^2 uniformly in L; if this radius is below one the sum is empty. Indeed the bound is at most14 M(M+1)/(L+1)^2 with M=floor((L+1)lambda/2), which is <=7lambda^2 when M>=1.

A continuous cutoff removing 0<sqrt(x)<delta hence changes the local form factor in squared norm by at most C delta^2 uniformly. First let the box grow with delta fixed, then let delta decrease to zero. This proves convergence of the local finite-box profile to (1), and convergence of K_ee to its finite bulk value. In particular eta_e=exp(-g^2 K_ee/4) converges to a strictly positive constant at fixed g.

This statement concerns the chosen reference modes. It does not identify the actual interacting finite-volume vacuum or transport a gap theorem between boundary conventions.

## 5. What the calculation changes

The local current vertex is finite, but applying a bare free-photon energy inverse to it produces a logarithmic norm divergence. A uniform all-state perturbative elimination cannot be justified merely by the local vertex norm. Energy-form estimates, a coupled fermion/photon denominator, current cancellations, coherent dressing, or a multiscale construction are materially different remaining routes.

No route to the actual phase is ruled out here. In particular, the calculation does not prove that interactions stay strong at macroscopic scales or that the axioms need to change. It identifies the particular inverse estimate that fails and the current information that a successful replacement must supply. The physical-wall count is zero.

## 6. Checks and scope controls

The runner uses two distinct calculations: direct Cartesian sums of the lattice dispersion on periodic grids N=16,32,64,128,256, and spherical quadrature after the exact low-frequency coordinate change. The successive logarithmic slopes approach the analytically derived 1/(3pi^2). The low-frequency quadrature resolves the quadratic and quartic terms. These are numerical challenges of the formulas; the integrability and divergence conclusions follow from equations(3)-(5).

Finite grids exclude their exact zero mode, as required by the transverse reference convention. They are not samples of the compact interacting ground state. A divergence in this positive reference norm cannot be cancelled by a sign choice; a physical matrix element with an additional soft factor is a different object and remains open. The earlier campaign's bounded-time weak-coupling propagation theorem did not apply an inverse photon energy, so this calculation does not contradict it.

## Dependency and proposal record

Exact target: prove the stated infrared norms of the cubic reference vertex under the supplied finite-volume and reference assumptions of this note.

Specified cubic symbol -> exact q-coordinate integral -> angular factor and Jacobian bounds -> energy-weighted domains. The local free-cube matching additionally uses the explicit tensor spectral bound restated here. These are reference spectral statements; they require no actual interacting state theorem.

Strongest missing downstream lemma: An estimate on the actual coupled state or an effective interaction under infrared rescaling. This is an open physical bridge, not a lemma that the present result claims to have reduced to a smaller equivalent problem. Boundary conventions, zero modes, coupling ranges and finite-cutoff limitations are specified above and are not extended by this record.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Control the fixed-interaction, large-system physics of the supplied coupled model."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: "Author proposal under explicitly supplied model/reference assumptions; independent affected-source confirmation and audit required."
hypothetical_axiom_status: "none proposed"
admitted_observation_status: "none used"
claim_type_reason: "Bounded supplied-model mathematics; no derivation of the model from the framework axioms."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Check the written proof independently, then address the named actual-state bridge."
```

Canonical finite evidence sources: [rotor_reference_infrared_norm_check_2026_09_16.py](../scripts/rotor_reference_infrared_norm_check_2026_09_16.py). The author's finite checks challenge the written formulas; they do not establish a uniform theorem by sampling. The scientific imports are the explicitly supplied rotor/CAR or Gaussian/Wilson model and stated boundary conventions. No observed values, fitted selectors, new axioms or new approved primitives are imported. Mathematical tools and their use are specified in the proof.

Canonical source registration and current runner evidence support review; independent audit and the combined integrated-tree gate remain separate. No author audit verdict is asserted.

## Scope and negative-claim discipline

N1: energy-form bounds, a coupled fermion denominator, current soft factors, coherent dressing and multiscale state construction are distinct open physical routes. The coupled denominator is worked at first order in the resolvent-density note. These are not five completed attacks against a universal exclusion.

N2: compression versus off-space action and a specified inverse-domain failure are different reference diagnostics, not independent physical walls. Physical-wall count zero.

N3: no unique finite-volume sea, positive matter gap, volume-independent total error, invariant trial space or interchangeable limits is assumed.

N4: the linked model definitions and explicit mathematical imports are the actual premises; a chosen reference is not an interacting ground-state identification.

N5: finite element, site, mode and block challenges are printed by the named programs at their stated cutoffs and tolerances. Infinite-volume bounds, analytical domain statements and limit proofs are checked in the written mathematics, not executed by a finite grid. Source hashes and resource limits do not prove science.

N6: the successful coupled first coefficient remains positive progress, not a broad perturbative impossibility result.

N7: current conservation, particle-hole phase space and coherent or multiscale constructions can change the actual observable; none is excluded.

N8: earlier bounded-time weak-coupling results do not identify the fixed-g interacting state or use the same inverse operator. Historical author mutation results remain historical; no broad negative certificate or audit verdict is granted.


## Current dependencies and evidence

[Original recovery](work_history/review_loop/pr8161/README.md) and [exact manifest](work_history/review_loop/pr8161/original-manifest.json) preserve all original proofs, working notes, programs and outputs.

Actual linked mathematical context: [ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16](ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md), [ROTOR_ORTHOGONAL_TRANSVERSE_REFERENCE_CURRENT_VERTEX_BOUNDED_THEOREM_NOTE_2026-09-16](ROTOR_ORTHOGONAL_TRANSVERSE_REFERENCE_CURRENT_VERTEX_BOUNDED_THEOREM_NOTE_2026-09-16.md).

Canonical caches: [rotor_reference_infrared_norm_check_2026_09_16](../logs/runner-cache/rotor_reference_infrared_norm_check_2026_09_16.txt). These must match the current source/input bytes.
