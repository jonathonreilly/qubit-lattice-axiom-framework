---
claim_id: sharp_actual_rotor_cube_energy_tail_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Conditional supplied rotor cube: exact exceptional phase set and two-sided order tau^(-5/2) for the
  three actual zero-field first-birth high-energy curves; no finite-spin growing-time or unscaled microscopic conclusion.'
upstream_dependencies:
- actual_birth_rotor_energy_has_an_algebraic_lower_bound_bounded_theorem_note_2026-09-24
- minimal_axioms
- rotor_cube_fast_energy_strong_decay_without_uniform_decay_bounded_theorem_note_2026-09-24
runner: scripts/sharp_actual_rotor_cube_energy_tail_2026_09_24.py
---

# A sharp power bound for the actual rotor cube birth-energy tail

**Type:** bounded_theorem

**Status:** conditional mathematical result; unaudited.

This is a conditional theorem for the supplied compensated cube's fast rotor
generator and actual zero-field first-birth inputs. It adds a global upper
bound to the existing lower bound and classifies the exceptional phases exactly.
It does not select the microscopic Hamiltonian, formation law or a physical bath.

## Model, physical space and statement

Use A=(0,3,5,6), B=(1,2,4,7), with A-to-B edges ordered

    01,02,04,31,32,37,51,54,57,62,64,67.

Hard-core site charges q=0,+1,-1 and integer fields obey div E=q-1_A.
An outward charge-s hop moves s from occupied A to empty B and shifts its
field by -s; the adjoint moves inward and shifts by +s. Rotor shifts have unit
amplitude. Let F be the sum of outward hops, W the number of empty A sites,
and Pi_1 the W=1 projection in the N=6, total-charge-four sector. The full
fast Hermitian generator and the original birth loss are

    G=Pi_1(FF^*-F^*F)Pi_1,       Gamma_1=2 P_bright,
    L=-i delta G-kappa P_bright, delta,kappa>0 fixed.

Bright charge words have adjacent A/B vacancies; dark words have opposite
vacancies. Their dimensions are 72 and 24. Resolved and coherent original
marks have this same loss, while retaining their different actual outputs.
The birth instrument is not replaced by a field-only law or an energy filter.

Take tree indices (1,2,3,4,6,9,11) and chord indices (0,5,7,8,10). The chord
fields are the five integer Gauss coordinates. The inherited exact Fourier
representation of the complete physical space is L2(T5;C96), with normalized
Haar measure. An outward hop on chord j has phase z_j^(-s), z_j=exp(i theta_j).
The dark/bright matrix of G(theta) is

    G(theta) = [ 0       Q(theta)^* ] ,
               [ Q(theta) B(theta)  ]

where B=B^*, Q is 72 by 24, and the zero dark block is an identity of Laurent
polynomials. Both Q and B have uniform norm at most M=288: ||F||<=12 gives
||G||<=288. This deliberately loose finite bound suffices.

For each original first mark i (resolved plus, resolved minus, coherent), let
r_i=R_i/sqrt(b_i) be its actual high component from the inherited canonical
zero-field preparation and define

    f_i(tau)=||exp(tau L) r_i||^2.

These are the same curves obtained after taking the supplied microscopic
compact-fast-time joint limit. Their initial values are 2,1,3/2. Each r_i
has finite physical word support, so its Fourier vector is a bounded Laurent
polynomial. No phase eigenstate is substituted for this normalizable input.

**Theorem.** For every fixed delta,kappa>0 and each of the three inputs there
are constants 0<c_i<=C_i<infinity such that, for every tau>=0,

    c_i (1+tau)^(-5/2) <= f_i(tau) <= C_i (1+tau)^(-5/2).             (1)

This is a two-sided order bound. It does not assert convergence of
tau^(5/2) f_i(tau) to an asymptotic constant or give optimal constants.
The exceptional phases where Q loses rank are exactly the following, in the
stated chord coordinates; the bit string denotes theta/pi modulo 2:

| Bits | Rank of Q | Dark kernel dimension |
| --- | ---: | ---: |
| 00000 | 23 | 1 |
| 00011 | 23 | 1 |
| 01101 | 22 | 2 |
| 01110 | 23 | 1 |
| 10100 | 23 | 1 |
| 10111 | 22 | 2 |
| 11001 | 20 | 4 |
| 11010 | 22 | 2 |

## Exact Laurent identities give a global singular-value bound

Construct Q directly by pairing an inward/outward path through W=0 with sign
+1, and an outward/inward path through W=2 with sign -1. Enumerate six occupied
vertices, choose the single negative charge among them, retain W=1, and split
the charge words by adjacent versus opposite vacancies. This fixes both charge
orders and all monomials without sampling the torus. It also reconstructs the
identically vanishing dark-dark block.

The finite certificate consists of 120 rational Laurent row identities,

    p_(j,a)(z) Q(z) = (z_j-z_j^-1) e_a^T,
    j=1,...,5,  a=1,...,24.                                      (2)

Each p_(j,a) is a row of length 72. Its Laurent multipliers have total absolute
degree at most three. The primary runner constructs and verifies every
coefficient of (2) exactly over Q. Modular elimination and rational recovery
are only a way to discover candidates; no finite-field rank is used as the
certificate. Even an incorrect modular discovery would be rejected by the
subsequent rational coefficient comparison.

For reproducibility, the discovery matrix contains each of the 72 primitive
rows multiplied by each integer exponent n with sum |n_j|<=3. The 231 shifts
are ordered by (sum |n_j|,n). A row combination records its shifted-row index
and a rational numerator/denominator. The complete regenerated witness is
written to outputs/sharp_rotor_cube_energy_tail_20260924/RATIONAL_LAURENT_CERTIFICATES.json.
Its hash is recorded in the compact committed result and source-bound cache.
The witness is generated from the self-contained runner; it is not an external
runtime input or an assumed identity.

The sum of absolute Laurent coefficients in each p_(j,a) is at most 68891,
as checked exactly from these rational combinations. Stack the 24 rows for
each j into P_j. The elementary row norm and Frobenius bound give

    sum_j sup_T5 ||P_j(z)||^2 <= M_P=120*(68891)^2=569516385720.

For every dark vector v, (2) therefore implies

    4 sum_j sin(theta_j)^2 ||v||^2
      = sum_j ||P_j Q v||^2 <= M_P ||Qv||^2.

In particular,

    sigma_min(Q(theta))^2 >= (4/M_P) sum_j sin(theta_j)^2.           (3)

Every rank defect must consequently have z_j in {+1,-1} for all five j.
Exact rational elimination at all 32 sign phases gives the table above and
rank 24 at the remaining 24 points. This proves completeness of the table;
a numerical grid or an assumption that the known exceptions are exhaustive
does not enter the argument. The bound (3), rather than a fitted local Hessian,
is what the decay proof needs.

## Uniform dissipative-block estimate

The exact fiber equations, with d dark and b bright, are

    d'=-i delta Q^* b,
    b'=-i delta Q d-(kappa+i delta B)b.

Use the inner product linear in its second argument. Write
c=Im<b,Qd>. Direct differentiation gives

    c'=delta ||Qd||^2-kappa c
          +delta Re<b,BQd>-delta ||Q^*b||^2.

Choose

    A0=(kappa+delta M)^2/(2 delta)+delta M^2,
    alpha=min(1/M,kappa/A0)>0,
    E=||d||^2+||b||^2-alpha c.

The bound |c|<=M(||d||^2+||b||^2)/2 yields

    (||d||^2+||b||^2)/2 <= E <= 3(||d||^2+||b||^2)/2.

The original norm derivative is -2 kappa ||b||^2. Combining the displayed
cross derivative with Young's inequality gives

    E' <= -[2 kappa-alpha A0]||b||^2-alpha delta ||Qd||^2/2
       <= -kappa ||b||^2-alpha delta ||Qd||^2/2.

Let sigma=sigma_min(Q), so sigma<=M, and set
c0=min(kappa/M^2,alpha delta/2)>0. Then

    E' <= -c0 sigma^2 (||d||^2+||b||^2)
       <= -(2c0/3) sigma^2 E.

Thus the exact matrix exponential obeys the uniform bound

    ||exp(tau L(theta))||^2 <= 3 exp[-(2c0/3) sigma(theta)^2 tau].   (4)

The derivation includes singular Q. It does not require diagonalizability,
normality, an eigenvector condition-number bound or a phase-dependent prefactor.
The original matter coupling and birth loss remain in both block equations.

## Integrating physical inputs and matching the lower bound

Let A_i=ess sup_theta ||rhat_i(theta)||, which is finite for the actual
finite-support vectors. Combining (3)-(4) and Parseval gives

    f_i(tau) <= 3 A_i^2 integral_T5
        exp[-(8c0/(3M_P)) tau sum_j sin(theta_j)^2] dtheta.         (5)

On each circle, distance x to {0,pi} lies in [0,pi/2] and sin x>=2x/pi.
Splitting into those neighborhoods and bounding by Gaussian integrals yields
an upper bound C(1+tau)^(-1/2) for each one-dimensional factor. The normalized
five-dimensional integral factorizes. Equation (5) proves the upper part of
(1), for all tau>=0 after increasing its finite constant if necessary.

The inherited actual-input lower theorem proves the other half of (1) under
these identical fixed positive parameters. Its flat-phase dark kernel is
simple, its eigenvalue has vanishing first derivatives, and the squared
actual-input overlaps there are 1/12,1/12,1/6. It integrates a shrinking
positive-measure neighborhood of that phase, giving a positive multiple of
(1+tau)^(-5/2). The full physical input, not the measure-zero fiber alone,
is essential in both bounds.

## Scope, verification and remaining obligations

The proof's new global input is the rational Laurent identity family (2).
The primary runner reconstructs Q from primitive hops, regenerates and checks
all 120 identities, computes all 32 exact sign-phase ranks, and checks the
coefficient bound. An altered witness coefficient is rejected by a direct
Laurent residual check. An exact two-state example detects reversal of the
modified-energy cross-term sign. The analytic inequalities above, rather
than a numerical large-time fit, supply the infinite-time conclusion.

The upper estimate applies to fixed inputs with bounded Fourier amplitude;
it is not a common decay rate over all normalizable inputs. It also does not
justify a growing-time microscopic approximation. Finite spin, the coupled
limit at fixed laboratory time, unscaled microscopic moments, moving high-flux
preparations, another electric completion or graph, physical reservoir
accounting and native selection of the supplied dynamics remain separate
questions. The compact-fast-time limit is taken before the large-tau analysis
in this theorem.

Run:

```bash
python3 scripts/sharp_actual_rotor_cube_energy_tail_2026_09_24.py
```

## Imports and status

- [Strong rotor decay and the complete physical Fourier space](ROTOR_CUBE_FAST_ENERGY_STRONG_DECAY_WITHOUT_UNIFORM_DECAY_BOUNDED_THEOREM_NOTE_2026-09-24.md) supplies the exact charge decomposition, original generator, Gauss coordinates and actual finite-word inputs.
- [Actual-input algebraic lower bound](ACTUAL_BIRTH_ROTOR_ENERGY_HAS_AN_ALGEBRAIC_LOWER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-24.md) supplies the positive lower half of (1), with the same preparation and parameters.

These are conditional mathematical imports. Their presence on main and any
source comparison do not confer retained audit status. Independent scientific
reconstruction and released-source comparisons are recorded in the review
packet. No axiom, audit verdict or physical completion claim is adopted here.

## Machine-status block

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: sharp_actual_rotor_cube_energy_tail_bounded_theorem_note_2026-09-24
target_blocker_text: "Strong decay and an actual-input lower bound left the global upper rate and exceptional phase set unresolved."
source_of_blocker_text: frontier_question
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Control the finite-spin dynamics on growing fast-time intervals before inferring ordinary microscopic energy bounds."
conditional_surface_status: "Supplied lambda=0 rotor cube, original marks, actual zero-field inputs and fixed positive parameters."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A two-sided order bound and finite exceptional set follow from exact Laurent identities and analytic dissipative estimates under declared model hypotheses."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Landing-review boundary and No-Go Discipline Gate

N1: the specified rotor cube, fixed positive rates and three fixed actual inputs. N2: other graphs, inputs and limiting regimes remain open. N3: the compensated quantum model and birth instrument are supplied, not axiom-derived. N4: both linked parent results retain their domains. N5: exact finite Laurent certificates supply the global singular-value bound; the displayed dissipative estimate and integration supply the infinite-time upper bound. No finite-time fit proves it. N6: no asymptotic constant or microscopic growing-time approximation is established. N7: the bounded Fourier amplitude of the chosen inputs is essential; the operator norm still does not decay. N8: the compact-fast-time limit precedes the rotor long-time limit.

- [Repository premise boundary](MINIMAL_AXIOMS_2026-06-29.md): does not select this dynamical model.

Author reports and execution history are provenance only. The original packet remains recoverable at the frozen PR #9049 head. No audit verdict or retained grade is applied.
