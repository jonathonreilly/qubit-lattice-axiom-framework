---
claim_id: finite_clock_local_ground_probabilities_and_charge_projected_plaquette_harmonics_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "For the explicitly defined three-state link Hamiltonian on finite full rectangular cubic boxes, a local imaginary-time comparison gives a strictly positive lower bound, independent of total volume, for every fixed coordinate pattern in its ground state at fixed finite couplings. It yields an explicit cube-charge probability bound in local weak limits. Integer-charge projection gives a spin-one plaquette operator with first and second harmonics; fixed-box spectral and imaginary-time estimates identify the large spatial-penalty limit and the fixed-spatial-weight-per-time-step limit. The Hamiltonian and ground-state choice are supplied model assumptions."
upstream_dependencies: []
runner: scripts/finite_clock_local_probability_and_charge_projection_2026_09_14.py
---

# Finite-clock local ground probabilities and charge-projected plaquette harmonics

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

For a specified three-state clock Hamiltonian, finite local hopping and finite
penalties give a positive, volume-independent lower bound for the ground-state
probability of each fixed local coordinate pattern. Applied to a cube, this
gives an explicit lower bound on its integer-charge probability. Sending the
spatial charge penalty to infinity instead selects a spin-one plaquette
operator whose second harmonic has coefficient `t exp(-r mu)`, where `r` is
the number of faces at the original edge. These are results about the stated
Hamiltonian and its limits. The physical phase and a native realization remain
open research targets.

## Machine status and exact target

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "Keeping a nonzero spatial penalty coefficient fixed as delta->0 instead imposes an infinite penalty; the low-energy constrained dynamics then needs a separate derivation."
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Use the derived constrained generator in the phase analysis, and keep finite-penalty local probabilities explicit when relating bare and effective observables."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Direct finite-dimensional operator and probability derivations for a supplied local Hamiltonian, with explicit uniform local constants and fixed-box limit qualifications."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The exact target is to prove a uniform local-probability inequality for this
Hamiltonian and identify its charge-projected generator and fixed-box penalty
limits. The quoted blocker is provenance from the prior kinetic derivation at
commit `652ea36706f7df14f153f2d40ee900662fe73706`; all objects and proofs used
here are re-established below. Closing this limiting-operator question has the
stated narrow scope.

## Supplied objects and imports

The native baseline is recorded in `docs/MINIMAL_AXIOMS_2026-06-29.md` and
the approved primitive registry. The present link qutrits, Hamiltonian,
couplings, and choice to study a ground state are supplied model assumptions.
Their realization by the native nearest-neighbor Admissibility and Record
structure is an open bridge. The scale-reference, kinetic-isotropy and
realized-state primitives retain their stated roles; this note assigns them
no state-selection or phase content.

There are no observational inputs, fitted constants or imported field-theory
phase theorems. Finite-matrix variational arguments, convexity and elementary
cellular incidence are used with their relevant hypotheses displayed. The
runner reads no mutable repository scientific inputs and no integrity files.
It computes from its own declared finite models; its external numerical
dependencies are NumPy and SciPy.

## 1. Clock Hamiltonian and physical flux coordinates

Take a full rectangular three-dimensional cubic box. Let `G`, `F`, and `D`
be its vertex-to-edge, edge-to-face, and face-to-cube coboundaries, with
orientations induced by products of positively oriented intervals. Thus
`FG=0` and `DF=0`. On the full coordinate Hilbert space, each edge carries
`a_l in Z3`. Put

    b_p(a) = principal((Fa)_p) in {-1,0,1},
    Q_c(a) = (Db(a))_c/3,
    N(a) = sum_c Q_c(a)^2.

The Bianchi identity modulo three makes every `Q_c` an integer. Since a cube
has six faces, `|Q_c|<=2`. For a shift of edge `l` by `sigma=+1,-1`, define

    b' = principal(b + sigma F e_l),
    m = (b'-b-sigma F e_l)/3,
    r_(l,sigma)(a) = t exp(-mu sum_p m_p^2),
    A_l |a> = sum_sigma r_(l,sigma)(a) |a+sigma e_l>.

Assume `t>0`, `mu>=0`, and `K,lambda>=0`. At finite `mu`,

    h := t exp(-4mu) <= r_(l,sigma)(a) <= t.

Reversal changes `m` to `-m`, so `A_l` is real symmetric. Its row sums are
at most `2t`; therefore `||A_l||<=2t` and `2t I-A_l>=0`. Define

    A = sum_l (2t I-A_l) + V_K,
    V_K = K sum_p [1-cos(2pi b_p/3)] = (3K/2) sum_p b_p^2,
    H_lambda = A + lambda N.                                  (2)

Each displayed local summand is positive. The electric diagonal is the
constant `2t` per edge, as specified in (2).

At finite `mu`, all single-edge shifts have positive rates, so the full
configuration graph is connected. Perron-Frobenius gives a unique normalized
positive ground vector. Original gauge transformations `a -> a+Gphi` are
permutations commuting with (2). They fix this vector by positivity and
uniqueness, so its energy is also the physical ground energy.

For these contractible boxes, cellular exactness over `Z3` gives
`ker F=im G` and `im F=ker D`. Every gauge orbit has size `3^(|V|-1)`.
Normalized sums over the orbits give a physical flux basis indexed by
`b in {-1,0,1}^P` with `Db=0 mod 3`. The link shifts map normalized orbits
to normalized orbits with the stated rates; coincident flux actions of
different original edges contribute their full multiplicity. In this basis,
let `Pi` project onto `Db=0` as an integer equation.

Global holonomies and flux restrictions must be included when changing to
periodic or other topologies. The full-coordinate local-probability proof
below uses only its explicitly stated local hypotheses; the flux-basis
identification just given is for the specified boxes.

## 2. Local-probability comparison

**Lemma.** Let a finite product of three-state registers have a real
symmetric Hamiltonian with nonpositive off-diagonal entries and a normalized
nonnegative ground vector `Omega`, of energy `E`. For a register set `R` of
size `r`, suppose

    H = H_outside + H_touching,

where `H_outside` acts only off `R` and has an entrywise nonnegative
imaginary-time semigroup, `H_touching>=0`, and
`diag H_touching<=C`. Off the diagonal, require the entrywise inequality

    -H_touching >= h sum_(l in R)(X_l+X_l*),

where `h>0` and `X_l` is the cyclic coordinate shift. This requires the
touching term itself to supply both shifts uniformly in the other
coordinates, with nonnegative remaining hopping amplitudes. Positivity of
the full Hamiltonian's hopping alone would not establish this split-specific
condition.
Then, for every coordinate pattern `s` on `R` and every `tau>0`,

    Prob_Omega(a_R=s) >= exp(-2C tau)
       [(exp(2h tau)-exp(-h tau))/3]^(2r).                    (3)

**Proof.** Let `X_l` be the cyclic coordinate shift, and set

    L = -H_outside - C I + h sum_(l in R)(X_l+X_l*).

Entrywise, `L<=-H`. Both matrices have nonnegative off-diagonal entries.
Adding a common scalar to their diagonals makes them entrywise nonnegative;
their exponential power series then give

    exp(-tau H) >= exp(tau L)
       = exp(-C tau) exp(-tau H_outside) K_R,
    K_R = product_(l in R) exp[tau h(X_l+X_l*)].

Each one-register factor has diagonal
`[exp(2h tau)+2exp(-h tau)]/3` and off-diagonal

    k = [exp(2h tau)-exp(-h tau)]/3 > 0.

Thus every entry of `K_R` is at least `k^r`. Write `Omega_u` for the
coordinate blocks on the complement of `R`. The ground-vector identity and
entrywise positivity imply

    Omega_s >= exp[tau(E-C)] k^r
                 sum_u exp(-tau H_outside) Omega_u.

All vectors being summed are nonnegative. The squared norm of their sum is
at least the sum of their squared norms, hence

    ||Omega_s|| >= exp[tau(E-C)] k^r ||exp(-tau H_outside) Omega||.

Diagonalize `H_outside` and apply scalar convexity to its spectral weights:

    ||exp(-tau H_outside) Omega||
      = <exp(-2tau H_outside)>^(1/2)
      >= exp(-tau <H_outside>).

Finally `E-<H_outside>=<H_touching>>=0`. Squaring proves (3).
The proof permits noncommuting `H_outside` and `H_touching`. It concerns
diagonal probabilities, rather than the rank of a reduced density matrix.

If instead `H_touching>=-m I`, the same argument applies after moving a
scalar `m I` into that term and subtracting it from `H_outside`, with `C+m`
in (3). The associated change in the constant matters.

## 3. Uniform constants and cube-charge probabilities

For (2), put in `H_touching` every declared local term whose support meets
`R`, and put the other terms in `H_outside`. Positivity of the summands
establishes the lemma's energy hypothesis. If `n_e,n_p,n_c` count the
touching electric, face and cube terms, one can take

    C = 2t n_e + (3K/2)n_p + 4lambda n_c,
    h = t exp(-4mu).                                        (4)

An electric term is supported on the union of the faces incident on its
edge, with at most thirteen edges in that union. A given edge belongs to at
most four faces and four cubes. Consequently

    n_e<=13r, n_p<=4r, n_c<=4r,
    C<=r(26t+6K+16lambda).

For the twelve edges of a bulk cube, the sharper counts are

    n_e=60, n_p=30, n_c=19,
    C=120t+45K+76lambda.                                    (5)

There are six cube faces and twenty-four external faces attached to one
cube edge each. The electric supports reach the twelve cube edges,
twenty-four outward edges from cube vertices and twenty-four opposite edges
of the external faces. The touching cubes are the original cube, its six
face neighbors and twelve edge neighbors. The runner independently rebuilds
these counts from a 5x5x5 cellular complex.

An explicit charged coordinate pattern sets the x-directed edges anchored
at `(0,0,0)` and `(0,0,1)` to `-1` and `+1`, respectively, and the other
ten cube edges to zero. In the product-cell orientation its face flux is
`(-1,1,1,0,0,0)` and `Q_c=+1`. Thus (3) already lower-bounds the charge
probability by the probability of that pattern.

Summing over all charged patterns strengthens the result. The coefficient
of `z^(3q)` in `(z^-1+1+z)^6` counts the allowed cube fluxes of charge `q`.
For `q=(-2,-1,0,1,2)` these counts are `(1,50,141,50,1)`. Each has `3^7`
original coordinate representatives. There are therefore
`102*3^7=223074` charged twelve-edge patterns, and

    Prob_Omega(Q_c!=0) >= 223074 exp(-2C tau)
          [(exp(2h tau)-exp(-h tau))/3]^24.                  (6)

The same expression lower-bounds `<Q_c^2>`. At fixed finite couplings it is
strictly positive and independent of the total box size. Local weak limits
of the specified finite-volume ground states inherit (6), since the charge
projector is a fixed local observable. The result is a conservative lower
bound; its numerical magnitude may be very small.

For `C>2rh`, the logarithm of (3) is maximized at

    tau = log[(C+rh)/(C-2rh)]/(3h).

Direct differentiation proves this formula. Every positive `tau` is valid,
including when this optimizer formula is inapplicable. The bounds have
their stated fixed-coupling scope; their constants change in singular
penalty or vanishing-hopping limits.

## 4. Integer-charge projection and plaquette harmonics

For an original edge `l`, write `f=F e_l` and `r_l=|supp f|`. In a
single clock move each incident mismatch is either `0` or `-sigma f_p`.
The latter is the wrap from `b_p=sigma f_p` to its opposite endpoint.
Preserving integer charge is equivalent to `Dm=0`.

On a full rectangular 3D edge star, the cube equations equate the oriented
coefficients of successive incident faces. In the bulk these equations run
around a cycle; at a boundary they run along a connected path. Thus a
mismatch supported on this star with `Dm=0` has `m=k f`. For the binary
wrap choices, `k=0` or `k=-sigma`. The charge-preserving moves are exactly

    b' = b + sigma f,       rate t;
    b' = b - 2sigma f,      rate t exp(-r_l mu).              (7)

This statement applies to every preserved integer charge sector, including
the neutral one. The second move wraps every incident face together.

Identify `b_p` with a spin-one electric coordinate on the dual link. Define
normalized shifts

    S+|-1>=|0>, S+|0>=|1>, S+|1>=0, S-=(S+)*,
    B_l=product_p S_p^(f_p),

where the superscript denotes choosing `S+` or `S-`. These shifts equal
the usual spin-one raising/lowering matrices divided by `sqrt(2)`. On the
neutral physical sector,

    H_proj := Pi A Pi
      = 2t |E| Pi + (3K/2)sum_p E_p^2
        -t sum_l [B_l+B_l*+exp(-r_l mu)(B_l^2+(B_l*)^2)].     (8)

Here `E_p` is the diagonal electric operator. The star sizes are four in
the bulk, three at a flat boundary, and two at a corner edge. The second
harmonic in (8) is a first-order surviving clock transition. As `mu` tends
to infinity its coefficient tends to zero, giving the single-step
spin-one plaquette operator. Each double step also has its two allowed
single steps through the intermediate electric coordinate.

Connected edge stars and the stated flux-basis identification are hypotheses
of (8). Degenerate lower-dimensional complexes and different cell
identifications require their own incidence analysis.

## 5. Fixed-box spatial-penalty limits

Let `P=Pi`, `Rperp=I-P`, `e0=min spec(PAP on ran P)`, and
`v=||Rperp A P||`. Since `A>=0` and `N>=Rperp`, the variational principle
and the charged-block ground-vector equation give, for `lambda>e0`,

    e0-v^2/(lambda-e0) <= min spec(H_lambda) <= e0,
    ||Rperp Omega_lambda||^2 <= v^2/(lambda-e0)^2.            (9)

To see this, write a normalized ground vector as `x+y` with `x=P Omega`
and `y=Rperp Omega`. The charged block of `H_lambda` is at least `lambda`,
so

    y=-(Rperp H_lambda Rperp-e_lambda)^(-1) Rperp A P x.

The inverse norm is at most `1/(lambda-e_lambda)`. Substitution into the
neutral equation bounds the Schur correction and proves (9). An internal
neutral spectral gap is not a premise of this calculation.

A direct semigroup estimate holds for `lambda>0` and `T>0`:

    ||exp(-T H_lambda)-P exp(-T H_proj) P||
      <= exp(-lambda T)+2v/lambda+T v^2/lambda.               (10)

Variation of constants in the two blocks gives charged norm at most
`exp(-lambda T)||y(0)||+v/lambda ||psi||`. Inserting this in the neutral
equation gives error at most
`v/lambda ||y(0)||+T v^2/lambda ||psi||`. The positive diagonal block
generators and the full semigroup are contractions, completing (10).
The constants `e0` and `v` here are finite-box quantities.

## 6. A fixed spatial weight at each time step

For completeness define the finite-step clock kernel on full coordinates.
Let `eta_l=principal(a'_l-a_l)`, let `w_delta(0)=1` and
`w_delta(+1)=w_delta(-1)=delta t`, and set

    K_delta(a',a) = product_l w_delta(eta_l)
      * exp[-mu sum_p ((b_p(a')-b_p(a)-(F eta)_p)/3)^2].

It is symmetric and gauge invariant. The identity difference gives `I`;
differences on exactly one edge give `delta sum_l A_l`. All other entries
are nonnegative, and their row sums are at most

    (1+2delta t)^|E|-1-2|E|delta t = O_box(delta^2).

Thus `K_delta=I+delta sum_l A_l+O_box(delta^2)`, also after restriction to
the physical space. For a fixed `kappa>0`, put `M=exp(-kappa N)` and

    T_delta = exp(-2t|E|delta) M^(1/2) exp(-delta V_K/2)
                K_delta exp(-delta V_K/2) M^(1/2).

The row bound implies `||T_delta||<=1`, and

    T_delta=M-delta M^(1/2) A M^(1/2)+O_box(delta^2).

At fixed box and fixed `T>0`,

    T_delta^(floor(T/delta)) -> P exp(-T H_proj) P.          (11)

Here is a quantitative block argument. Write
`a=P T_delta P`, `b=P T_delta Rperp`, `c=Rperp T_delta Rperp`.
For sufficiently small `delta`, take constants `B,C2` and `q'<1` with

    ||a||<=1, ||b||<=delta B, ||c||<=q',
    ||a-exp(-delta H_proj)||<=delta^2 C2.

Such a `q'` exists because the limiting charged block has norm at most
`exp(-kappa)`. The two-block recurrence and contraction imply

    ||T_delta^n-P exp(-n delta H_proj)P||
      <= (q')^n + 2delta B/(1-q')
                 + n delta^2[B^2/(1-q')+C2].               (12)

One obtains (12) by summing the geometric series for the charged component
and then inserting that bound into the neutral recurrence. Telescoping
`a^n` against `exp(-n delta H_proj)` supplies the last term. The remaining
time-rounding error vanishes. This proof is at fixed box and positive time;
`B,C2` may grow with the box.

Equations (8) and (11) specify the constrained dynamics for a nonzero spatial
weight held fixed at each time step. An isotropic Euclidean model and this
anisotropic trajectory are separately specified models whose phase relation
is a further question.

## 7. Obligation graph and validation

| Obligation | Evidence here | Status within the stated theorem |
|---|---|---|
| Symmetric local generator and positive summands | Reverse move and row bound, section 1 | Proved |
| Physical ground-vector identification | Gauge permutations and Perron-Frobenius, section 1 | Proved for the specified finite boxes |
| Uniform local coordinate probability | Entrywise semigroup order, block norm and convexity, section 2 | Proved under the displayed local hypotheses |
| Cube charge and local constants | Original coordinate witness, combinatorics and section 3 | Proved; finite checks below |
| Charge-preserving local moves | Connected edge-star incidence, section 4 | Proved for the specified stars |
| Compressed Hamiltonian | Normalized spin-one shifts and (7) | Proved on the specified sector |
| Spatial-penalty limits | Schur, continuous block equations and discrete recurrence | Proved with the stated fixed-box qualifications |

The stated inequalities and operator identities have no open terminal lemma
inside their declared domain. Independent scientific review remains pending.
For the broader phase program, uniform sector-energy ordering at fixed
couplings and a Coulomb spectral estimate for the actual ground state remain
open. The derivation of this Hamiltonian and its observables from native
Admissibility and Record also remains open.

The primary runner performs seven finite check families. It builds incidence
from products of intervals; checks all binary wrap patterns on 144 stars;
compares clock compression and integer shifts coefficientwise in `exp(-mu)`
on physical spaces of dimensions 243 and 19,683; exercises the Schur and
block-product inequalities; tests (3) on a noncommuting four-qutrit model;
reconstructs the cube assignment and bulk counts; and checks local coordinate
probabilities using the exact gauge-orbit multiplicity.

The product example uses `M^(1/2) exp(-delta A) M^(1/2)` to test the block
lemma. The expansion and row bound for the full clock kernel in section 6
are analytic arguments. The runner's finite matrices are checks of the
proof, with their computed scope exposed in stdout.

The embedded challenges include the second-harmonic omission, a bulk exponent
used on boundary edges, unnormalized spin-one raising matrices, and a mixed
wrap with nonzero integer charge. Two further examples show the numerical
effect of changing assumptions while keeping the probability formula's
constant unchanged: a negatively normalized touching term, and an on-region
potential assigned to the outside Hamiltonian. Load-bearing source mutations
and final cache results are recorded in the Review record after execution.

Reproduce with:

```bash
python3 scripts/finite_clock_local_probability_and_charge_projection_2026_09_14.py
```

The canonical output is
[the paired runner cache](../logs/runner-cache/finite_clock_local_probability_and_charge_projection_2026_09_14.txt).

## Review record

Author mathematical and scope review only; independent review and audit are
pending. This source carries its own derivations and one self-contained
runner. Earlier unmerged source bytes are provenance, rather than runtime or
theorem inputs. The public claim is the positive local-probability inequality
and the explicit projected operators/limits. The phase program and possible
dressed observables remain open, with no axiom-update proposal made here.

Seven source mutations were executed against primary-runner SHA-256
`84dbae9ac1081dc61774a423545d45cde307fd8dfe214180727809d027054fca`.
Each terminated with a relevant assertion failure: replacing the alternating
cell orientation; omitting double hops; halving the limiting generator;
reversing the probability cost sign; shrinking electric supports to their
central edges; multiplying the gauge orbit by an extra factor of three; and
removing the potential from the misplaced-potential counterexample. These
are author checks of discrimination, not independent review. The canonical
cache binds the primary runner and its declared execution envelope.
