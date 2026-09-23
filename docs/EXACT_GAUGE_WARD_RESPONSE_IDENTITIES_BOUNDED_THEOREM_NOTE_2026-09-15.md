---
claim_id: exact_gauge_ward_response_identities_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/response_identity_check_2026_09_15.py
upstream_dependencies: ["docs/EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13.md"]
claim_scope: "Bounded conditional exact Ward response and conditional phase test; supplied hypotheses and limit order retained in full proofs."
---

# Exact Ward response and conditional phase test

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope and actual premises

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13](EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13.md).

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK24_EXACT_RESPONSE_IDENTITIES_AND_PHASE_TEST

Original source identity: `BLOCK24_EXACT_RESPONSE_IDENTITIES_AND_PHASE_TEST.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Exact response identities and the remaining charged-phase test

Personal derivation, 2026-09-16 UTC. PROVISIONAL; no independent audit.
These are finite-volume identities for the same integer-rotor Hamiltonian.
They specify what a positive-coupling phase argument must still control.
They do not establish that phase or amend the framework axioms.

#### 1. Hamiltonian and physical operators

On a fixed periodic cubic box use exact div E=Q and

    H= (g^2/(2a)) sum_l e_l E_l^2
      + (1/(ag^2)) sum_p b_p(1-cos theta_p)
      + (1/a) sum_l (T_l+T_l^*) + H_on,
    T_l=sum_(q=+1,-1) c_(x,q)^* t_(l,q) U_l^q c_(y,q).          (1)

The onsite term is gauge invariant and commutes with electric numbers and
link angles. All e_l,b_p are fixed positive real numbers and the CAR matrices
are finite. The paired Wilson choice is one specialization, not needed for
the identities. C maps link angles to oriented plaquette angles. On a finite
torus the electric part is elliptic on the gauge quotient and the remaining
matrix-valued potential is smooth and bounded. Ground vectors are smooth
and have the electric domain regularity used below. Gauss reduction makes
this statement on the actual physical Hilbert space.

For real test arrays v on links and w on plaquettes put

    F_E(v)=g sum_l v_l E_l,
    F_B(w)=g^-1 sum_p w_p sin(theta_p).                           (2)

Both are physical. No gauge-fixed vector potential is a local observable.
For a normalized exact ground vector Omega of energy E0 and a Hermitian F,
let P0 be the full ground projection and let dmu_F be the positive excitation
spectral measure of (1-P0)F Omega. This removes all elastic ground-space
weight, including transitions between degenerate ground vectors. Its total
mass is the INELASTIC variance; for a unique ground it is the usual variance.
Smoothness just noted makes its first energy moment finite for (2), and

    M1(F)=integral_0^infinity nu dmu_F(nu)
         =(1/2)<[F,[H,F]]>.                                    (3)

The proof is the spectral theorem applied to <F(H-E0)F>, followed by
H Omega=E0 Omega. Zero-energy degeneracy does not affect the identity.

#### 2. Electric f-sum: an explicit charged contribution remains

Using [E_l,U_l^q]=q U_l^q and the curl incidence signs gives exactly

    [F_E(v),[H,F_E(v)]]
      =(1/a) sum_p b_p (Cv)_p^2 cos(theta_p)
       +(g^2/a) sum_l v_l^2 D_l,
    D_l=-(T_l+T_l^*).                                          (4)

The charge square is one for both species, so their contributions ADD.
Opposite charge does not cancel this response. D_l need not be positive
as an operator; the full expectation in (3) is nonnegative. In particular

    0<=M1(F_E(v))
       <=(1/(2a))||W_B^(1/2) C v||^2
          +(g^2/a) sum_l v_l^2 ||T_l||.                         (5)

This is a finite-volume bound independent of any ground-state gap. For
normalized transverse real sine/cosine modes in a homogeneous box, the
first term is O(|s(k)|^2) and the second is O(g^2). The constants are local
hopping norms, not a norm of the extensive Hamiltonian. The estimate
therefore retains a nonzero fixed-g floor as k->0. Dropping the charged
term would manufacture a stronger infrared conclusion.

In the pure-gauge model T_l=0, (5) has only its curl term. Even then an
upper f-sum bound alone does not prove a photon: one needs a sufficiently
large low-momentum static variance or another spectral lower estimate.
In the charged model high-frequency matter weight can contribute to the
same total first moment, so isolating a photon may require a controlled
frequency filter and an estimate of the remaining current response.

#### 3. Magnetic f-sum: compact nonlinearities remain

F_B commutes with the magnetic and matter terms because it is a function
of link angles. The electric kinetic form gives

    [F_B(w),[H,F_B(w)]]
       =(1/a) sum_l e_l [C^*(w cos theta)]_l^2.                  (6)

All factors on the right commute, and the formula is exact at arbitrary g.
It is NOT generally equal to ||W_E^(1/2)C^*w||^2/a. At fixed positive g,
cos(theta_p) is an operator depending on p. A spatially slowly varying
w does not make w cos(theta) slowly varying.

For any epsilon>0 write z_p=w_p(cos(theta_p)-1). The elementary norm square
inequality and (1-cos theta)^2<=2(1-cos theta) imply the explicit upper bound

    2a M1(F_B(w))
       <=(1+epsilon)||W_E^(1/2)C^*w||^2
        +2(1+epsilon^-1)||W_E^(1/2)C^*||^2
                                sum_p w_p^2 <1-cos theta_p>.   (7)

This retains the compact fluctuation term. Its disappearance in Block22
was established in the order g->0 before volume; (7) supplies no uniform
control as momentum tends to zero at fixed positive g. Replacing sin theta
by a globally unwrapped angle is not a domain-preserving shortcut: the
branch discontinuity is outside this smooth commutator calculation.

#### 4. A flat external charge twist is exactly screened by a dynamical link shift

Let v be any real closed link one-form, Cv=0, including a harmonic constant
direction on a periodic cube. Apply an EXTERNAL charge twist only to matter:
replace U_l^q by exp(iq epsilon v_l)U_l^q in (1). Electric and magnetic
terms are kept fixed. Since electric numbers commute with Gauss law,

    U_epsilon=exp(i epsilon sum_l v_l E_l)

is a physical unitary. It translates link angles, leaves the electric energy
unchanged, and leaves every magnetic plaquette unchanged because Cv=0.
Consequently

    H(epsilon)=U_epsilon H(0) U_epsilon^*,
    spec H(epsilon)=spec H(0)                                  (8)

for ALL real epsilon and all g>0 in the untruncated rotor model. No small
coupling approximation, unique ground state, thermodynamic limit or
large-gauge identification is required. Arbitrary angle translations are
unitary even though electric numbers are integers.

Define J=H'(0), D=H''(0). With the reduced inverse R0=(H-E0)^-1 on the
orthogonal complement of the entire ground subspace, (8) gives

    <D>=2<J R0 J>,       D=(1/a)sum_l v_l^2 D_l.                 (9)

The finite-box positive excitation gap above the ground subspace makes R0
bounded. The identity also holds for a vector in a degenerate ground space:
J=i[E(v),H] has no matrix elements inside that space, and the second-order
effective operator there is zero by the explicit unitary equivalence.
Alternatively insert J between excited states and use
J_n0=-i(E_n-E0)E(v)_n0 to reduce (9) to (3)--(4) with Cv=0.

This is the exact cancellation of the static diamagnetic and paramagnetic
responses for this probe. It does not say the matter dynamics is absent.
An external SAME-sign flavor twist on both opposite-charge species is a
different probe and is not absorbed by this common gauge translation.

In particular Block20's e_L(phi) is the free matter energy at a FIXED
internal flat gauge holonomy phi. Its curvature and Block21's quantized slow
levels are real properties of the stated reduction. They are not the
curvature of the full dynamical model's energy under the external twist
in (8). With that probe the holonomy wavefunction can translate, and the
entire energy spectrum stays unchanged. No contradiction is involved.

#### 5. A decisive diagnostic: static screening is compatible with a massive mode

Consider the explicitly separate quadratic transverse comparator at one
nonzero real wave number k, with canonical [A,P]=i,

    H_eps=(g^2/2)P^2+(k^2/(2g^2))A^2
                         +(rho/2)(A+eps)^2,    rho>0.           (10)

It is the transverse mode of a gauge-invariant London/Stueckelberg model
whose full spatial energy contains rho|A+externalA-grad theta|^2/2.
That extra matter law is supplied here ONLY as a response discriminator;
it is not identified with the paired Wilson model or added to the axioms.

Completing the square in (10) gives

    omega(k)=sqrt(k^2+g^2 rho),
    d^2 E0(eps)/d eps^2|0 = rho k^2/(k^2+g^2 rho).               (11)

The static response tends to zero quadratically at k=0 even though the
physical transverse frequency has the strictly positive limit g sqrt(rho).
At k=0 the source is removed by A translation. Thus flat-twist screening
and a small static twist stiffness are not by themselves photon witnesses.
This example only falsifies that proposed diagnostic; it neither proves
nor disproves Higgs behavior in the actual rotor/Wilson model.

For a Hermitian probe F, a useful genuinely spectral implication is instead

    mu_F([0,lambda]) >= mu_F([0,infinity))-M1(F)/lambda,          (12)

by Markov's inequality for the positive spectral measure. To infer a
nonvanishing fraction of inelastic weight on an energy scale O(|k|), one must control
BOTH its inelastic variance and the first moment at matching scales, or prove a
stronger infrared resolvent estimate. It does not follow from the Ward
identity (9). Even (12) by itself gives weight, not an isolated pole or a
sharp dispersion.

#### 6. Next derivation contract

For the SAME paired Wilson/compact rotor model at some fixed g>0, target a
volume-uniform estimate on a specified physical transverse spectral measure
or Euclidean magnetic correlator. Keep the matter-current contribution and
compact-field fluctuations present in (4),(6). State whether the output
is gapless spectral weight, an isolated pole, a static force, or only an
upper response bound. These are different completion witnesses.

A credible first step is an exact current/Ward decomposition with an
infrared bound on its remainder, after a stated frequency/scale split.
A lower spectral estimate at momenta approaching zero must use the same
state whose regulator limit is controlled in Block16. An estimate at
g(L)->0, external twist screening, or a finite-volume gap fit does not
close the fixed-positive-coupling target. The matched free cone in Block23
is a starting comparator; possible pairing, compact defects and coefficient
renormalization remain part of this obligation.

The finite checker uses a literal Fourier/CAR charged ring for (4),(6),(9)
and checks (11) by independent oscillator displacement algebra. The ring
is a commutator/domain fixture, not evidence of a three-dimensional phase.

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK24_ROUTE_AND_NO_GO_REVIEW

Original source identity: `BLOCK24_ROUTE_AND_NO_GO_REVIEW.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Personal review: which response could certify a photon

2026-09-16 UTC. Same author, not independent review.

The target is a useful contract for the still-open fixed-positive-coupling
charged phase. The output is an exact set of identities plus a discriminator
for an insufficient measurement. It does not claim a failure of that phase.

1. **Alternatives.** Magnetic spectral weight, a physical transverse pole,
   static charged force and neutral-current response are distinct routes.
   The identities do not declare one of them impossible.
2. **Wall independence.** The O(g^2) term in the electric f-sum is an actual
   charged hopping contribution. Its presence in an upper bound is not a
   lower spectral gap. The compact correction in the magnetic f-sum is
   also not itself evidence of confinement.
3. **Hidden assumptions.** The analysis uses untruncated rotors, finite
   periodic volume, fixed positive stiffness and bounded smooth CAR
   hopping. Domain regularity follows from finite-dimensional ellipticity
   after exact Gauss reduction. The finite check explicitly excludes hard
   cutoff boundary rows when testing a smooth angle identity.
4. **Residual matching.** The external charge twist changes opposite-charge
   hoppings with opposite phases and allows gauge flux to respond. Block20
   fixes internal holonomy while computing the matter potential. These
   experiments are not interchangeable. Same-sign flavor twists remain
   outside the claimed absorption identity.
5. **Rhetoric.** Ward identities and oscillator completion are familiar
   mathematics. The useful delta is their exact normalization and application
   to this campaign's proposed phase diagnostics, not a new general theorem
   of gauge theory.
6. **Partial closure.** The exact finite-volume f-sums and flat-source
   cancellation are available to a future phase proof. No low-frequency
   lower bound, interacting pole, regulator-uniform spectral convergence
   or axiom selection follows yet.
7. **Steelman.** A frequency-filtered transverse correlator might isolate
   a photon despite the total f-sum's charged contribution. The explicit
   massive London comparator rejects only static screening as a sufficient
   witness, not that frequency-filtered route in the actual Wilson model.
8. **Cross-cycle check.** Block8 already distinguished absorbable charge
   twists from a same-sign response in another finite model. The current
   rotor result is not counted as a second confirmation of its transport
   claim. The new phase contract composes only with the stated rotor model.

Author review found a precision issue before finalizing the note: an ordinary
connected variance can retain zero-energy transitions inside a degenerate
ground space. The final spectral measure uses (1-P0)F Omega with P0 the FULL
ground projection. Its first moment is unchanged, but its total mass is the
inelastic variance. For H=diag(0,0,2) and F coupling only the first two basis
vectors, ordinary variance is1, first moment0 and inelastic variance0; calling
that a photon would be false. The exact preflight prose is preserved as
review/BLOCK24_PREFLIGHT_SOURCE.md. This is a scope clarification; no failed
numeric result or tolerance was edited away.

The literal 540-dimensional charged-ring implementation verifies1416 actual
CAR/Gauss transitions. Electric and interior magnetic double commutators
agree with the derived formulas to below1.9e-14. The magnetic hard-boundary
discrepancy is24.14 and is deliberately retained: a compressed shift is not
a unitary rotor shift there. Flat external twists match their physical
unitary conjugation to below1.5e-14. Diamagnetic and paramagnetic responses
are .31981617573350 and .31981617573351; the f-sum difference is below7e-16.
The separate massive oscillator has frequency .521536 at k=0 with zero
static source curvature. No initial checker failed.

These finite checks challenge signs, charge addition, domains and probe
definitions. They do not establish a phase or independently audit the proof.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: response_identity_check_2026_09_15](../scripts/response_identity_check_2026_09_15.py); [current cache](../logs/runner-cache/response_identity_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
