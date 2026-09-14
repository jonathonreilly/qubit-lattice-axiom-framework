---
claim_id: principal_flux_positive_gaussian_transfer_and_extensive_hamiltonian_limit_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "A periodized Gaussian restricted to the finite principal-flux graph gives a strictly positive gauge-compatible transfer for the explicitly supplied three-state penalty Hamiltonian. A local Poisson-history comparison bounds its one-step error proportionally to spatial volume and identifies its finite-volume Hamiltonian limit and first local logarithmic correction. The principal-Wilson temporal kernel has the same limit but has an exact negative physical quadratic form on a specified three-square strip at finite step. No thermodynamic phase, native law selection or axiom update is inferred."
upstream_dependencies: []
runner: scripts/principal_flux_positive_gaussian_transfer_and_hamiltonian_limit_2026_09_14.py
---

# Principal-flux positive Gaussian transfer and extensive Hamiltonian limit

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

The specified three-state monopole-penalty Hamiltonian admits a positive
finite-step transfer with an explicit local spacetime weight. Positivity
follows by restricting a periodized Gaussian kernel to the nonlinear graph
of principal plaquette fluxes. A Poisson-history comparison shows that the
transfer approaches the intended Hamiltonian with an error proportional to
the number of spatial links. It preserves the fixed electric diagonal and
all original-link multiplicities.

The principal-Wilson temporal prescription has the same infinitesimal law,
but need not be a positive operator at finite step. An exact physical
three-square counterexample is given below. The positive completion changes
that finite-step prescription by at most `6 E q^4` for `q<=1/8`.

These are author-derived statements about a supplied model. Independent
review is pending. An actual-state Coulomb phase and selection of this law
from the framework axioms remain open.

## Status and target

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "Construct an everywhere-positive finite-step principal-flux transfer for the supplied penalty Hamiltonian and control its time-limit error with explicit spatial-volume dependence."
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Establish an actual-state estimate uniform in the anisotropic and thermodynamic limits; retain native law selection as a separate physical obligation."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit Gaussian positivity, finite-dimensional operator limits, local Poisson bounds and an exact rational counterexample for a fully specified model."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The Hamiltonian was specified in the campaign derivation at commit
`652ea36706f7df14f153f2d40ee900662fe73706`, then studied in the proposed
local-probability/projected-harmonic source of PR8123 at
`9a84632e8b9e4f82969d7b4e22827d0037c51df5`. Those are provenance, not
imported theorem or audit authority. All objects and arguments needed here
are defined below. This Hamiltonian is distinct from the unpenalized
clock-plus-matter model in the 2026-09-03 finite-clock bridge and PR8106.

| Supplied object or mathematical input | Role | Boundary |
|---|---|---|
| Finite cubic geometry, link qutrits and gauge group | Complete microscopic carrier for this theorem | Native geometry and payload compilation are not derived |
| Positive `t`, nonnegative finite `mu,K,lambda` | Define hopping and spatial penalties | No physical coupling is selected or fitted |
| Gaussian Fourier transform, finite group projection, Poisson processes and matrix functional calculus | Proof machinery with hypotheses checked below | No external phase theorem is assumed |
| Principal-Wilson action and its anisotropic scaling | Explicit comparison law | Isotropic numerical phase evidence supplies no uniform time-limit theorem |

The proof obligations form the following acyclic chain; none of its proved
steps uses the open phase question as a premise.

| Obligation | Disposition | Consumer |
|---|---|---|
| Positive Gaussian and nonlinear finite graph restriction | Proved in section 2 | Strict transfer positivity |
| Gauge commutation, orbit restriction and seam projection | Proved in sections 1 and 3 | Physical transfer and spacetime identification |
| Principal-image tail | Proved in section 4 | Same infinitesimal Hamiltonian |
| Disjoint-history factorization and repeated-event control | Proved in section 5 | Extensive operator error |
| Contraction products and logarithm estimate | Proved in sections 5–6 | Fixed-volume semigroup and generator limit |
| Local first logarithmic coefficient | Proved in section 6 | Explicit leading correction |
| Exact physical negative form | Proved in section 7 | Scope of principal one-step positivity |
| Uniform actual-state phase and native law selection | Open; not used above | Further physical conclusions |

## 1. Hamiltonian and gauge conventions

Let `G:C^0->C^1`, `F:C^1->C^2`, and `D:C^2->C^3` be the oriented cubical
coboundaries of a finite three-dimensional rectangular box or cubic torus.
For tori take side lengths at least three; cells and original links are
counted with their actual identities. Write `E` for the number of links,
`P` for faces, and `C` for cubes. Thus `FG=0` and `DF=0` over the integers.
The strip counterexample uses an explicitly described planar cubical
subcomplex with free boundary instead.

The full coordinate Hilbert space has orthonormal states `a in (Z/3Z)^E`.
For any integer vector, `principal(x)=(x+1) mod 3-1` componentwise. Define

    b(a)=principal(Fa),           Q(a)=D b(a)/3.

Every `Q_c` is integral, with absolute value at most two. For an elementary
signed link lift `k=sigma e_l`, set

    a'=a+k mod 3,
    m(a',a;k)=[b(a')-b(a)-F k]/3,
    W_(l,sigma)|a>=exp[-mu ||m(a',a;sigma e_l)||^2]|a'>.

The mismatch is integral. Reversing the move changes its sign. Put

    A_l=W_(l,+)+W_(l,-),       A=sum_l A_l,
    H_E=t(2E I-A),
    V(a)=K sum_p[1-cos(2pi b_p(a)/3)]+lambda ||Q(a)||^2,
    H=H_E+V.                                                    (1)

Here `A_l` is dimensionless; the hopping rate is `t` times its matrix entry.
Each `A_l` is real symmetric with row sums at most two, so
`2I-A_l>=0`, `H_E>=0`, `V>=0`, and `||H_E||<=4tE`.
The diagonal in (1) is **2t per original link**, including all moves that
later coincide in physical flux coordinates. It is not the sum of the
penalized escape rates. At finite `mu`, every elementary rate is at least
`t exp(-4mu)`, so the full configuration graph is connected.

Spatial gauge transformations are the permutations `a->a+G phi mod 3`.
They leave `b` unchanged and commute with (1). Their group average `P_G`
is an orthogonal projection. The physical Hilbert space is `im P_G`.
Perron-Frobenius applied to `-H` after a scalar shift gives a unique positive
finite-volume ground vector; gauge invariance and uniqueness make it physical.
This says nothing about a uniform spectral gap.

For contractible boxes, exactness of the cellular complex over `Z3` gives
a physical basis of normalized gauge-orbit sums indexed by principal `b`
with `Db=0 mod 3`. Every orbit has the same size. On tori retain the global
holonomies and the realizability of `b`; do not replace the physical space
by arbitrary mod-three-closed fluxes.

## 2. An exact positive finite-step kernel

For `0<q<1`, set

    Theta(q)=sum_(j in Z) q^(j^2),
    K_per(q,mu)(a',a)=Theta(q)^(-E)
      sum_(k in Z^E: k=a'-a mod 3)
        q^(||k||^2) exp[-mu ||b(a')-b(a)-Fk||^2/9].              (2)

The series converges absolutely. Swapping endpoints and sending `k->-k`
shows symmetry. Every entry is strictly positive for finite `mu`. Each
integer `k` selects exactly one endpoint, so the sum of every row is at
most one. This row-sum statement alone would not prove operator positivity.

**Gaussian positivity proof.** Write `c=-log q>0`. When `mu>0`,

    f(x,y)=exp[-c||x||^2-(mu/9)||y-Fx||^2]

is a positive-definite Gaussian on `R^E x R^P`. Its quadratic form is
strictly positive under the invertible change `(x,y)->(x,y-Fx)`. Its Fourier
density is a positive constant times

    exp[-||p+F^T eta||^2/(4c)-9||eta||^2/(4mu)].

Periodize only the `x` variable by `3 Z^E`. Poisson summation restricts `p`
to `2pi n/3`, `n in Z^E`, while leaving the everywhere-positive continuous
`eta` density. Restrict this positive kernel on `(R/3Z)^E x R^P` to the
finite graph `a -> (a,b(a))`. The result is (2), up to its positive scalar.
The fact that this graph is nonlinear is harmless for a Gram restriction.

Strict positivity also follows from this representation. Given nonzero
coefficients `u_a`, at `eta=0` at least one finite clock character has
`sum_a u_a exp(2pi i n.a/3) != 0`. Continuity makes its squared modulus
nonzero on a positive-measure `eta` neighborhood, where the density is
positive. The associated quadratic form is therefore strictly positive.

At `mu=0`, the kernel factorizes over links. Its discrete Fourier eigenvalues
are proportional to

    sum_(j in Z) exp(-c j^2) exp(2pi i r j/3)
      =sqrt(pi/c) sum_(s in Z) exp[-pi^2(s+r/3)^2/c] >0.

Thus (2) is strictly positive also at `mu=0`. Together with symmetry and
the row-sum bound, this proves `0<K_per<=I` as operators.

Define, for `0<epsilon t<1`,

    D_epsilon=exp(-epsilon V/2),
    T_epsilon=D_epsilon K_per(epsilon t,mu) D_epsilon.          (3)

Then `0<T_epsilon<=I`. Its canonical finite-dimensional Hamiltonian
`H_epsilon=-epsilon^(-1)log T_epsilon` is well-defined and nonnegative.
The proof gives positivity of the transfer in the chosen time direction;
spatial reflection positivity or Euclidean isotropy of this anisotropic
measure is not inferred.

## 3. Physical projection and local spacetime representation

Simultaneous gauge transformations at the two endpoints preserve `b` and
the modular increment class in (2); changing representative integers simply
reindexes the lift sum. Hence `K_per` commutes with every gauge permutation,
as do `D_epsilon` and `T_epsilon`. The physical restriction is strictly
positive. The kernel need not be invariant under separate endpoint gauge
transformations before temporal gauge variables have been summed.

For periodic Euclidean time, the physical partition function is

    Tr(P_G T_epsilon^M),

with the temporal holonomy/gauge projection retained. The unprojected trace
on all link coordinates is a different finite-temperature quantity. For
free temporal boundaries, use physical boundary vectors. Gauge projection
and restriction cannot increase the operator-norm errors proved below.

Writing an integer lift `k_j` for each temporal interval, the history weight
in temporal gauge is a sum of local factors with action

    sum_j {[-log q]||k_j||^2+mu||m_j||^2+epsilon V(b_j)},
    m_j=[b_(j+1)-b_j-F k_j]/3,

with the clock congruences and the appropriate temporal seam projection.
Spatial half factors in (3) give the displayed potential on a periodic
history. This is an auxiliary summation representation of the supplied law.
It adds no native primitive or state-selection rule.

The integer defects obey an exact continuity equation:

    D m_j=Q_(j+1)-Q_j.                                        (4)

It follows directly from `DF=0`. Finite penalties allow defect histories;
they do not erase (4) or impose `Q=0` in every state.

## 4. Principal-Wilson comparison

For a three-state clock, every modular link difference has a unique lift
`k_l in {-1,0,1}`. Define the principal temporal kernel

    K_pr(q,mu)(a',a)=(1+2q)^(-E) q^(||k||^2)
                       exp[-mu||m(a',a;k)||^2].               (5)

This is the normalized anisotropic Wilson temporal weight with

    q=exp(-3 beta_t^W/2),
    beta_t^W=(2/3)log[1/(epsilon t)],
    beta_s^W=epsilon K,     mu_t=mu,     mu_s=epsilon lambda.   (6)

The spatial Wilson and cube factors then give (3) with `K_pr` replacing
`K_per`. In temporal gauge the mixed cube charge is exactly `m`, up to a
common orientation sign. Keeping `mu_s` fixed and nonzero as epsilon goes
to zero instead sends the Hamiltonian's spatial charge penalty to infinity;
that is a different limiting question.

Let `s=Theta(q)-1-2q`. At `q<=1/8`,

    s=2 sum_(j>=2) q^(j^2)
      <=2q^4/(1-q^5)<=3q^4.

Separate the lifts in (2) into `{-1,0,1}^E` and its complement. Exactly,

    K_per=alpha K_pr+R,
    alpha=[(1+2q)/Theta(q)]^E,
    ||R||<=1-alpha.

The remainder is symmetric and nonnegative entrywise. Both `K_pr` and
`K_per` have row sums at most one and norm at most one, although `K_pr`
may have negative eigenvalues. The triangle and union bounds give

    ||K_per-K_pr||<=2(1-alpha)
       <=2E s/Theta(q)<=6E q^4.                               (7)

Thus they have the same finite-volume infinitesimal Hamiltonian. Positivity
of their entries must not be substituted for positivity of either operator.

## 5. Local Poisson proof of the extensive error

Let `J` count unordered pairs of distinct original links sharing a plaquette.
A cubic link has at most twelve such neighbors, so `J<=6E`.
The interaction graph here concerns principal-face support, not arbitrary
pairs of links elsewhere in the box.

Give each signed original link an independent Poisson clock of rate `t`.
During `[0,epsilon]`, update the configuration in event order and multiply
the factor `exp(-mu||m_event||^2)` at every event. The Dyson series for
`tA-2tE I` shows that its weighted transition matrix is exactly
`exp(-epsilon H_E)`. Every history weight lies in `[0,1]`; the reference
Poisson process is independent of its initial configuration.

Condition this process on at most one event per original link. The condition
has probability

    alpha_P=[exp(-2q)(1+2q)]^E,    q=epsilon t.

Conditional on it, each link has no event with probability `1/(1+2q)` or
one event of each sign with probability `q/(1+2q)`. Its event time is uniform,
and distinct links remain independent. Denote the conditional weighted
matrix by `K_cond`. Reversal of the complete timed history reverses every
mismatch without changing its squared norm or reference probability.
Therefore `K_cond` is symmetric, nonnegative entrywise and has row sums
at most one. The unconditioned remainder has row sums at most `1-alpha_P`.
Since a Poisson variable of mean `2q` has probability at most `2q^2` of
being at least two,

    ||K_cond-exp(-epsilon H_E)||<=2(1-alpha_P)<=4E q^2.        (8)

The endpoint distribution of the conditional reference process is exactly
the unpenalized principal step. If no two active links share a plaquette,
their changed face supports are disjoint. Each elementary mismatch is
unaffected by the other events, and the squared norm of the total mismatch
is the sum of their squared norms. Thus the principal endpoint penalty in
(5) equals the product of the timed penalties, for every event ordering.

On the complementary histories, both weights are in `[0,1]`, so their
absolute difference is at most one. The probability of this event is bounded
by `J[2q/(1+2q)]^2`. This bounds the absolute row sums of
`K_pr-K_cond`, uniformly in the initial configuration. Symmetry gives the
same column bound and therefore

    ||K_pr-K_cond||<=4J q^2.                                  (9)

Combining (7)–(9),

    ||K_per-exp(-epsilon H_E)||
       <=4(E+J)q^2+6E q^4<=29E q^2,    q<=1/8.              (10)

This estimate is uniform in finite `mu>=0`. It does not count every spatially
separated pair of jumps as an error.

For positive matrices `B,C`, the contraction Lie-product bound is

    ||exp(-uB)exp(-uC)-exp[-u(B+C)]||
       <=(u^2/2)||[B,C]||.

One proof differentiates the interpolating product, represents its
commutator by one more integral, and bounds all exponential factors by one;
the triangular integration region has area `u^2/2`. Apply this bound first
to `V/2,H_E` and then to `V/2+H_E,V/2`. The resulting conservative estimate
for the symmetric product is `epsilon^2||[H_E,V]||/2`.

A link jump changes at most four faces and four cube charges. Since
`b_p^2` changes by at most one and `Q_c^2` by at most four,

    |V(a')-V(a)|<=6K+16lambda,
    ||[H_E,V]||<=2tE(6K+16lambda).                            (11)

The absolute-value commutator matrix is symmetric; its row bound proves
the norm inequality even though the commutator itself is antisymmetric.
Equations (10) and (11) give

    ||T_epsilon-exp(-epsilon H)||<=epsilon^2 C_ext,
    C_ext=29Et^2+||[H_E,V]||/2
         <=E[29t^2+t(6K+16lambda)].                          (12)

For `epsilon=tau/M`, telescoping `M` contractions yields

    ||T_epsilon^M-exp(-tau H)||<=tau epsilon C_ext.           (13)

The analogous principal-transfer bound adds `6E(epsilon t)^4` per step.
These are extensive finite-volume estimates. Their right sides still grow
with volume, so no thermodynamic state, ground-state limit or Coulomb-phase
interchange follows from (12) or (13).

## 6. Canonical logarithm and its first local correction

At fixed volume assume `q=epsilon t<=1/8`,
`epsilon||H||<=log 2` and `epsilon^2 C_ext<=1/4`.
The least eigenvalue of `exp(-epsilon H)` is at least `1/2`; (12) therefore
bounds that of `T_epsilon` below by `1/4`. For positive matrices bounded
below by `a I`, the resolvent integral for their logarithms gives
`||log X-log Y||<=||X-Y||/a`. Consequently

    ||H_epsilon-H||<=4 epsilon C_ext.                        (14)

At finite `mu`, finite-volume eigenvalues and the unique ground projection
therefore converge to those of (1). The constants and finite-volume gap
needed for that projection convergence need not survive volume growth.

The first correction can be written explicitly. Let `B_lr` be the sum of
the four signed simultaneous-lift operators on distinct links `l,r`, each
weighted by its total mismatch, and set `B=sum_(l<r)B_lr`. Expanding (2),

    log K_per=q(A-2E I)+q^2 C_K+O_box(q^3),
    C_K=B-A^2/2+2E I.                                       (15)

Here `log Theta(q)=2q-2q^2+O(q^3)`. For links sharing no face,
`B_lr=A_l A_r=A_r A_l`, by the disjoint-support argument above. Thus

    C_K=sum_l(2I-A_l^2/2)
       +sum_(l<r sharing a face)
           [B_lr-(A_l A_r+A_r A_l)/2].                       (16)

Each single-link term has norm at most four, and each pair term at most
eight. Hence `||C_K||<=4E+8J<=52E`. The symmetric potential sandwich has
no second-order commutator in its logarithm, giving

    H_epsilon=H-epsilon t^2 C_K+O_box(epsilon^2).             (17)

Only this coefficient is proved local here. An all-orders locality statement
for the finite-step logarithm is not used or asserted.

## 7. Exact physical counterexample for the principal kernel

Take three adjacent unit squares in a planar strip, with free spatial
boundary. There are ten links, eight vertices and three independent faces.
In face coordinates, the ten incidence columns can be oriented as

    e1, -e1+e2, -e2+e3, -e3, e1, -e1, e2, -e2, e3, -e3.

The flux map onto `(Z3)^3` is surjective, and its kernel is the gauge
subgroup. All gauge fibers have size `3^7`; normalized orbit sums therefore
give a 27-state physical flux basis. The principal reduced kernel is

    K_pr(b',b)=(1+2q)^(-10)
      sum_(k in {-1,0,1}^10: principal(b+Fk)=b')
        q^(||k||^2) r^(||[b'-b-Fk]/3||^2),   r=exp(-mu).       (18)

Order each `b_i` as `-1,0,1`. Define

    g=(1,-2,1),
    A0=[[0,1,-1],[-1,0,1],[1,-1,0]],
    w(b1,b2,b3)=g(b2) A0(b1,b3).

Its squared norm is 36. At `q=9/10`, `r=1/2`, exact arithmetic gives

    w^T K_pr w=-901886967/55267035185152<0.                    (19)

For a compact algebraic verification, the integer-curl distribution is the
Laurent generating function

    g_q(z1)^3 g_q(z2)^2 g_q(z3)^3
          g_q(z2/z1) g_q(z3/z2),
    g_q(z)=1+q(z+z^(-1)).

For each monomial exponent `s`, use `b'=principal(b+s)` in (18) and multiply
its coefficient by `w(b')w(b)r^(||[b'-b-s]/3||^2)`, then sum over `b`.
At `r=1/2` the resulting polynomial is `(q-1)P9(q)/64`, where

    P9(q)=13659q^9-7097q^8-56738q^7+126672q^6-124012q^5
           +54056q^4+9504q^3-24800q^2+12352q-2304.

Dividing by `(1+2q)^10` and substituting `9/10` proves (19).
At `r=1` the unnormalized form instead equals
`36(1-q)^9(1+2q)`, a check of the unpenalized sign and normalization.
The primary runner reproduces (19) both by all principal lifts and by ten
short integer Laurent convolutions. Floating-point eigenvalues only helped
find the displayed simple witness; they do not establish its sign.

This refutes positivity for **all** principal one-step kernels at arbitrary
positive parameters, even after physical gauge projection. Positive spatial
half factors preserve the negative direction by invertible congruence.
It does not refute the simulated periodic four-dimensional parameters, a
photon phase, or the Hamiltonian limit. A symmetric transfer has positive
square, so two-step reconstruction also remains possible. The positive
completion (2) is an explicit alternative with the same limit.

## 8. Literature and phase boundary

Giansiracusa, Lanners and Sulejmanpasic study a Wilson action with principal
cube-monopole suppression and give numerical photon-phase evidence for
three-state links. Equation (6) is an explicitly anisotropic version of their
N=3 action; their isotropic data do not control this path to continuous time.
[Primary source, arXiv:2505.00079v2](https://arxiv.org/abs/2505.00079v2).

Nguyen, Sulejmanpasic and Ünsal also discuss a modified Villain model with
independent integer plaquette fields and monopole suppression. Its constrained
duality is a useful different formulation. It must not be identified with a
principal-flux truncation without a further argument.
[Primary source, arXiv:2401.04800v2](https://arxiv.org/abs/2401.04800v2).
Neither paper is a proof input to (2)–(19).

For comparison, with the convention
`phi_beta(theta)=sum_n exp[-n^2/(2beta)]exp(i n theta)`, the unpenalized
sampled Villain temporal kernel agrees with (2) at `mu=0` when
`q=exp(-2pi^2 beta_t/9)`. Thus the fixed-three-state time limit uses
`beta_t=(9/(2pi^2))log[1/(epsilon t)]`. A continuous-U(1) rotor scaling
`beta_t` proportional to `1/epsilon` would instead freeze clock jumps
faster than epsilon. For a Villain spatial weight with K>0, the first-order
Wilson potential uses `exp[-1/(2beta_s)]=epsilon K/2`, so `beta_s` tends to zero.
An isotropic theorem requiring every coupling large does not automatically
cover this anisotropic family.

The terminal scientific obligation remains a bound on the actual state of
(1), uniform in volume and the relevant low-energy limit. The transfer
construction supplies a precise object on which to attempt that bound;
finite positivity and an extensive time approximation are insufficient.
No conclusion requiring an axiom update follows from the counterexample.

## Executable evidence and falsifiers

The primary runner uses NumPy and SciPy and has no mutable scientific input
files. Its nine reported families cover:

- twelve full-coordinate/physical square kernel comparisons, with controlled
  integer-lift tails, symmetry, row sums and finite positivity;
- theta tails, Poisson repeated-event bounds and both temporal scalings;
- the four-original-link multiplicity in the three-state reduced generator;
- independent cube incidence construction, physical realizability and (4);
- all cube link-pair cancellations, conditional Poisson weights and (16);
- one-step and fixed-time approximation at four steps, including the explicit
  omitted-lift tail and the first logarithmic coefficient;
- potential-jump and commutator bounds on every cube transition;
- row-normalization and mismatch-scale controls that change the target law;
- the exact physical strip quadratic form, all eleven coefficients of its
  displayed polynomial, a separate Laurent convolution, spatial congruence
  and positive two-step square.

The full-cube transfer calculation retains only integer lifts of squared
norm at most two. It bounds the omitted operator norm by

    1-Theta(q)^(-12)(1+24q+264q^2).

The cube one-step and fixed-time error comparisons include this tail.
Floating-point comparisons use tolerances; the analytic lift tail is not an
interval enclosure of floating-point roundoff. The numerical logarithmic
coefficient check concerns that truncation; its tail is order `q^3`, so it
does not change (15). Positivity of the full kernel comes from section 2,
not from the truncated cube eigenvalues.

The finite tests challenge load-bearing formulas; they do not prove the
arbitrary-volume bounds or a phase. The theorem would fail if the Gaussian
Fourier density or graph restriction were invalid, if the physical projection
changed the kernel claimed here, if disjoint jumps failed the factorization
used in (9), or if the exact polynomial in section 7 gave a different sign.
A row-normalized escape generator is outside the stated target and must not
be substituted for it.

Run:

    PYTHONPATH=scripts python3 scripts/principal_flux_positive_gaussian_transfer_and_hamiltonian_limit_2026_09_14.py

The expected final line is `TOTAL: PASS=9 FAIL=0`. A green runner is author
verification, not independent scientific review or effective retention.

## No-Go Discipline Gate

The negative claim is only (19): the entire family of principal one-step
kernels cannot be declared positive at arbitrary parameters. The displayed
finite physical witness proves that statement. No broader impossibility or
axiom-forcing conclusion is proposed.

### N1 — Alternative route enumeration

| Honesty | Distinct route and decisive object | Result and exact scope |
|---|---|---|
| **ATTEMPTED** | Gaussian feature representation: periodize the real joint increment/principal-flux Gaussian and restrict its Gram matrix. | Positive for the completed kernel (2), by section 2. It changes the finite-step image sum, so it does not establish positivity of (5); (7) identifies precisely what changes. |
| **ATTEMPTED** | Perron-Frobenius and positive history weights: try to turn entrywise positivity into a positive spectrum. | (18) has positive entries but (19) is negative. Perron-Frobenius controls its leading eigenvector, not every quadratic form. The exact witness, not a failed search, closes this inference. |
| **ATTEMPTED** | Gauss reduction: remove nonphysical negative modes before deciding whether the transfer is positive. | Gauge reduction is performed in (18); all normalized fibers and original-link multiplicities are retained. The 27-state physical witness survives, unlike a separate nonphysical one-square negative mode. |
| **ATTEMPTED** | Spacetime decimation: integrate every other time slice and reconstruct from the squared transfer. | Positive square is available by `K_pr^2=K_pr^* K_pr`; the runner checks it on the counterexample. This is a successful two-step construction and cannot repair a claim about the original one-step operator. |
| **ATTEMPTED** | Infinitesimal Poisson-history formulation: match the time-ordered generator instead of the finite-step spectrum. | Sections 5–6 prove the intended finite-volume Hamiltonian limit and its extensive error. This route succeeds for that different terminal statement; it leaves (19) intact at fixed step. |
| **ATTEMPTED** | Spatial potential congruence: add the positive half factors of the desired spatial action. | If `D>0`, the vector `D^(-1)w` has the same negative form under `D K_pr D`; the explicit congruence check implements this inertia argument. |

These are distinct mechanisms with explicit successful alternatives as well
as failed inferences. The new algebraic proofs and exact certificate are
their authority in this author proposal; no route is marked ruled out by a
prior retained result. The route count is a packet requirement, not evidence
of impossibility.

### N2 — Relations among remaining obligations

The counterexample is a closed finite statement, and the positive completion
is constructed. Two contextual obligations remain: `W_phase`, a uniform
actual-state phase estimate for (1), and `W_native`, derivation/selection of
the supplied law within the native framework. Whether a future proof of one
would also establish the other is unresolved in both directions. No mutual
independence, two-wall theorem or inflated wall count is claimed.

| Pair | Does the first close the second? | Does the second close the first? | Independence |
|---|---|---|---|
| `W_phase`, `W_native` | Unresolved | Unresolved | Not asserted |

Time-limit identification is discharged here and is not counted again as a separate
physical wall.

### N3 — Hidden-hypothesis scan

All geometry, boundaries, qutrit coordinates, principal representatives,
couplings, gauge projection and time scalings are explicit in sections 1–4.
The term "canonical" denotes the unique self-adjoint logarithm of a strictly
positive finite matrix; it imports no framework dynamics. The strip is a
free-boundary subcomplex, not a periodic four-dimensional simulation.
The extensive constants use bounded cubic incidence and finite penalties.
No Gaussian ground-state ansatz, Euclidean isotropy, Poincare symmetry,
phase robustness or selected vacuum is hidden in the operator proof.

### N4 — Exact residual matching

| Evidence | Residual established | Match to the negative statement |
|---|---|---|
| Equations (18)–(19), exact rational lift and convolution calculations | Failure of positive semidefiniteness for this finite physical principal one-step kernel | Exact match |
| Prior finite-box small-step continuity construction at `652ea367...` | Positivity sufficiently near the identity at each fixed volume | Different claim; compatible, not a negative witness |
| Published isotropic numerical photon evidence cited in section 8 | Empirical evidence for specified finite periodic classical models | Different claim; not used against or as proof of (19) |

No old phase failure or unrelated reflection-positivity result is used as
support for the exact counterexample.

### N5 — Resolution audit

Individual lift weights, local cube states, finite matrix modes and the
three-square physical block are executed. The arbitrary-volume positivity
and extensive approximation are proved analytically. Infinite-volume
actual-state phase estimates are not executed by the runner. Its cache
prints substantive `per_element`, `per_site`, `per_mode`, `per_block` and
`lattice_wide` lines with precisely those limits. Finite negative modes
are not presented as a phase or a lattice-wide spectral exclusion.

### N6 — Partial closure and primitive boundary

The completion (2), infinitesimal limit and two-step alternative already
resolve useful transfer questions without an axiom change. They modify or
interpret a supplied mathematical regulator, with differences explicit.
No claim that a retained primitive is absent, or that a new axiom is
required, is made. No axiom, primitive or dynamics-selection rule is edited.
A future native realization or actual-state estimate may close further
obligations without changing the present counterexample.

### N7 — Steelman

A reviewer should insist that a free three-square negative mode says little
about a periodic four-dimensional photon phase or the infinitesimal
Hamiltonian. The concrete alternatives are the positive Gaussian completion
of section 2, exact two-step positivity, and a parameter-restricted
principal-kernel theorem near the identity. All remain compatible with the
phase evidence cited in section 8. A uniform covariance or dressed-observable
bound for the same anisotropic state would materially advance the phase
question. None of these alternatives makes the particular quadratic form
(19) positive; they prevent enlarging its domain into a phase no-go.

### N8 — Cross-campaign comparison

The earlier principal-kernel derivation at `652ea367...` deliberately left
arbitrary-step positivity open and established fixed-box continuity only.
The present completion supplies arbitrary-step positivity for (2), while
(19) explains why that conclusion cannot simply be assigned to (5).
PR8123 distinguishes positive bare-defect probabilities from absence of a
dressed photon phase; that distinction is retained. PR8106 distinguishes
positive weights from stronger positivity properties in a different matter
model; no counterexample is transplanted from it. The familiar two-step
mechanism is explicitly kept as a successful escape from a one-step demand.
No prior failed phase search is counted as an axiom obstruction.

**Gate disposition:** the scoped counterexample and successful alternative
constructions are documented; broader phase and native-law conclusions
remain open. This author packet grants no independent review or audit status.


## Author review record

The complete argument and runner were personally reviewed, with a Gaussian
Fourier derivation, Poisson path comparison, independent flux reduction and
two exact arithmetic constructions for the negative witness. Eighteen
deliberate mathematical faults were detected, including normalization,
integer-image deletion, cube orientation, logarithmic signs, omitted local
interactions, time mismatch and the spatial-cosine coefficient. This is
author verification; no separate reviewer or audit verdict is represented.

The result adds a new source. Earlier small-step constructions retain their
qualified scope. A one-square negative mode outside the physical sector was
not used as a physical counterexample; the exact strip witness replaces that
insufficient test. Finite matrix checks include their lift tails, and the
full-volume theorem rests on the written proof. Independent source review,
combined current-main validation and any later formal audit remain pending.
