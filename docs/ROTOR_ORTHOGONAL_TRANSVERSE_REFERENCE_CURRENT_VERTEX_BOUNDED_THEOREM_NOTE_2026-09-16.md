---
claim_id: rotor_orthogonal_transverse_reference_current_vertex_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "Supplied small-coupling Gauss Gaussian reference: exactly centered orthogonal sector, normalized shifted overlap and charge/volume-uniform per-link current vertex with an extensive total bound; no stable physical photon claim."
runner: scripts/rotor_transverse_reference_vertex_check_2026_09_16.py
upstream_dependencies: ["rotor_global_gauss_dressing_coulomb_variational_compression_bounded_theorem_note_2026-09-16"]
---

**Type:** bounded_theorem

# An orthogonal transverse sector and its current vertex

**Status:** conditional-support under the explicitly supplied model/reference; independent retained-grade audit remains separate.

The new result identifies the leading hopping matrix element from the charge-dependent trial vacuum into a normalized, exactly orthogonal transverse excitation sector. Its compact correction is uniform in box size and charge configuration. It does not identify that sector with stable physical photons.

## 1. Exact first centered sector

Use Gauss-dressing theorem notation, and let S_C be the complexification of S. The Gaussian electric state in charge sector Q has n=E-e_Q and mean m_Q. For f in S_C define the complex-linear map

    W_Q f = sqrt(2)g [(K^(1/2)f).(n-m_Q)] psi_Q.

The dot product in the wave function is bilinear, so the resulting Hilbert inner product is conjugate-linear in the first f. By centering, W_Q f is exactly orthogonal to psi_Q. Its Gram matrix is

    G_Q=W_Q*W_Q
       =I_S+(1/(2g^2))A^(1/2)F''(a_Q)A^(1/2).        (1)

This follows from the exact covariance in Gauss-dressing theorem, not from a continuum approximation. With

    rho=sqrt(12)epsilon/(2g^2),

we have ||G_Q-I||<=rho. In the stated g<=0.1 range, rho<1/2. Thus W_Q G_Q^(-1/2) is an isometry from S_C into the gauge charge sector. Define the whole-matter map

    V_1(f tensor |b>)=|b> tensor W_(Q(b))G_(Q(b))^(-1/2) f.

It is an isometry, and V_1*V_g=0 exactly. Matter basis orthogonality handles different b even when their charges coincide. This is a centered polynomial sector of a chosen reference, not a conserved photon-number subspace of the full Hamiltonian.

## 2. Exact normalized link vertex

Consider a positive link shift U(e), from charge Q to Q+De, and put a=a_Q, t_e=P e. The new integer representative may be E0+e, so its affine coordinate is a+t_e. All formulas are invariant under changing that representative by Lambda.

The electric overlap weight in equation(10) of Gauss-dressing theorem has midpoint variable y=n+t_e/2 distributed with the Gaussian weight on Lambda+a+t_e/2. In the final sector n'=n+t_e=y+t_e/2. Therefore the exact vector obtained by projecting U(e)psi_Q onto the normalized final centered sector is

    b_Q(e)=sqrt(2)g I_Q(e) G_(Q+De)^(-1/2) K^(1/2)
             [m(a+t_e/2)+t_e/2-m(a+t_e)],             (2)
    m(b)=-A grad F(b)/(2g^2).

The final mean must be subtracted. Dropping either affine mean before establishing a difference bound is incorrect; the individual means are not bounded in volume by their Euclidean norm.

By the uniform Hessian estimate,

    ||K^(1/2)[m(a+t_e/2)-m(a+t_e)]||
       <=sqrt(||A||)epsilon ||t_e||/(4g^2).           (3)

The cancellation in (3) is why the volume-independent bound survives. It uses K^(1/2)A=A^(1/2), ||t_e||<=1, and a difference of gradients separated by t_e/2.

Let v_e=K^(1/2)P e, so ||v_e||^2=K_ee<=14. Cauchy-Schwarz gives 0<I_Q(e)<=1, and Gauss-dressing theorem gives |I_Q(e)-eta_e|<=epsilon/4. Spectral calculus on [1-rho,1+rho] gives

    ||G_Q^(-1/2)||<=sqrt(2),
    ||G_Q^(-1/2)-I||<=2rho.

Insert these in (2)-(3) to obtain

    ||b_Q(e)-(g/sqrt(2))eta_e v_e||
      <=[sqrt(sqrt(12))/2+sqrt(7)sqrt(12)+sqrt(7)/4]
           epsilon/g
      <12 epsilon/g.                                (4)

The same argument applies to -e, with the leading vector negated. This is a per-link bound for every allowed source charge Q and every box size, at fixed sufficiently small g. It includes the Gram normalization and affine charge dependence.

## 3. The hopping current and the extensive bound

Write the free oriented matter hop as

    h_(e,s)=c_(x,s)^dagger T_(e,s)c_(y,s), s=+1,-1.

Only the hopping part of the full Hamiltonian is considered in this section. Its exact matrix from V_g to V_1 satisfies

    V_1* H_hop V_g
      =(g/sqrt(2)) sum_(e,s) s eta_e v_e tensor
                        [h_(e,s)-h_(e,s)^dagger] + R_10,
    ||R_10|| <=144 t_* V epsilon/g.                  (5)

Each error is a vector-valued diagonal charge function of norm <=12epsilon/g followed by the corresponding free hop, whose norm is <=t_*. Adding both orientations and species and E_edges<=3V gives the displayed conservative bound. A per-link estimate is not silently substituted for the norm of an extensive sum.

With the Hermitian current convention

    J_e=-i sum_s s[h_(e,s)-h_(e,s)^dagger],

which equals minus the derivative of the unscaled hopping Hamiltonian with respect to the link angle at zero, the leading expression is

    i(g/sqrt(2)) sum_e eta_e v_e tensor J_e.

The factor i belongs to the convention in which the reference excitation is a real centered electric-coordinate polynomial. Its sign is fixed by the charge-raising shift in (2); changing an excitation's overall phase changes this display and no physical prediction.

H_on has zero matrix between V_g and V_1 because it preserves every local charge and the two gauge sectors are orthogonal. Equation(5) does not include the electric and magnetic Hamiltonian's matrix into V_1 or any higher excitation sector. Those are separate matrix elements, not assumed absent in the compact model.

## 4. Scientific consequence and limit

The same globally Gauss-constrained reference that yields the Coulomb variational matrix has a nonzero transverse current vertex of order g. Its local norm remains finite as the box grows. Thus an exponentially small compact correction in the vacuum compression does not mean that the coupling to transverse excitations is exponentially small. The actual charged-ring calculation in Gauss-dressing theorem already exhibits this distinction directly.

The mode profile v_e involves A^(-1/2). A dynamical elimination also needs energy denominators and actual matter-current correlations; none follows from the local finiteness of v_e. This result supplies a controlled reference vertex for that next calculation. It proves neither physical photon stability nor a vanishing effective interaction at long distances.

## 5. Historical verification

The separate rank-five cube implementation constructs the electric sums and centered polynomial wave functions directly, then compares their Gram matrix, orthogonality, orthonormalization and charged-hop projection to dual-theta derivatives. It uses g=0.8,1.2,1.6 to expose charge-dependent corrections in finite identities. These values are outside the conservative uniform theorem range and are not used to validate an all-volume small-coupling bound by sampling.

Observed Gram and vertex discrepancies are near floating arithmetic precision; omitting the affine means gives a visible error, about0.108 in the last case. The comparison retains its actual finite cutoffs. It is an author calculation, not an independent mathematical review or a computation of an infinite-volume phase.

## Dependency and proposal record

Exact target: prove the stated orthogonal transverse reference sector and current vertex under the supplied finite-volume and reference assumptions of this note.

Gauss-dressing theorem exact covariance and uniform affine Hessian (provisional dependency) -> centered Gram matrix -> inverse square-root normalization -> exact shifted overlap -> uniform mean-difference bound -> current vertex. The last five steps are derived here.

Strongest missing downstream lemma: Control of all interacting excitation sectors and physical current correlations, beyond a chosen reference matrix element. This is an open physical bridge, not a lemma that the present result claims to have reduced to a smaller equivalent problem. Boundary conventions, zero modes, coupling ranges and finite-cutoff limitations are specified above and are not extended by this record.

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

Canonical finite evidence sources: [rotor_transverse_reference_vertex_check_2026_09_16.py](../scripts/rotor_transverse_reference_vertex_check_2026_09_16.py), [rotor_gauss_affine_theta_check_2026_09_16.py](../scripts/rotor_gauss_affine_theta_check_2026_09_16.py). The author's finite checks challenge the written formulas; they do not establish a uniform theorem by sampling. The scientific imports are the explicitly supplied rotor/CAR or Gaussian/Wilson model and stated boundary conventions. No observed values, fitted selectors, new axioms or new approved primitives are imported. Mathematical tools and their use are specified in the proof.

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

Actual linked mathematical context: [ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16](ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md).

Canonical caches: [rotor_transverse_reference_vertex_check_2026_09_16](../logs/runner-cache/rotor_transverse_reference_vertex_check_2026_09_16.txt). These must match the current source/input bytes.
