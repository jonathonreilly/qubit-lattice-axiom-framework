# Independent PRE: ordinary microscopic mean after a cube first birth

Prepared without reading the coordinator's new argument, its checkpoint or proof,
or any earlier independent-check packet. Source identities are in
`SOURCE_PINS.json`; complete supplied-source snapshots are in `sources/`.
No publication, research, axiom, audit, prompt, or instruction file was edited.
This is a conditional scientific reconstruction, not formal audit status.

## Result and exact domain

I obtain a positive conditional result, stronger than the supplied scaled-mean
statement. It uses two additional analytic estimates proved below, and a local
jump cancellation not stated in the supplied fixed-time theorem.

Retain the supplied lambda=0 compensated cube, original resolved or coherent
marks, canonical zero-field first-mark preparation on edge 01, fixed positive
`delta,K,kappa`, and integer `S -> infinity` with

    epsilon^2 S(S+1) = delta/K.

Write `beta_i=B_i/sqrt(b_i)` for the three supplied first outputs. On the full
physical rotor N=6, W=0 space put

    h_rot = K D - (delta/2) Z^* Z,
    Gamma_B = sum_j B_j^* B_j,
    w_i(t) = exp[t(-i h_rot - kappa Gamma_B/2)] beta_i.

Here the exponential is the contraction semigroup defined by the self-adjoint
`h_rot` on `D(D)` and the bounded dissipative perturbation. The initial vector
has finite physical-word support. In fact all its polynomial electric moments
remain finite on every bounded physical-time interval, as proved below.

Then the independently reconstructed conclusion is

    sup_{t in [t0,T]} |Tr(H_epsilon,S rho_i(t))
                         - <w_i(t),h_rot w_i(t)>| -> 0

for every fixed `0<t0<=T<infinity`. The limiting mean is finite. The proof also
works with lower endpoint `epsilon` (for sufficiently small epsilon and fixed T).
It does not cover all lower endpoints allowed by the supplied scaled theorem.

The N=8 terminal sector has exactly zero microscopic and effective energy.
Thus this is the ordinary full-ensemble mean; `w_i` is not renormalized by its
survival norm. The result says nothing new about ordinary unscaled variance,
physical selection of the supplied model, a reservoir, or heat/work accounting.
The six-site cycle is not used and cannot form twice.

## Conditional inputs actually used

1. The supplied finite-spin Hamiltonian, canonical preparation, original marks,
   exact terminal-zero reduction, and uniform analytic spectral clusters.
2. On the cube, `C_S` is zero for W>0; its low block is `F^*F+D/C`,
   `C=S(S+1)`. The Hermitian low-band coefficient is

       h_H,0 = epsilon^2 D/C + epsilon^4 H4_S + O(epsilon^6),
       H4_S -> -(1/2) Z^*Z strongly,

   with uniform norm bounds.
3. Exact no-event cluster coordinates have, uniformly in S,

       h_eff,1 = I + epsilon^2 [G_1,S-i kappa Gamma_1,S/(2delta)]
                    + O(epsilon^4),
       h_eff,0 = epsilon^2 D/C
                    + epsilon^4[H4_S-i kappa Gamma_B,S/(2delta)]
                    + O(epsilon^6).

   The Hermitian and no-event spectral projectors differ by `O(epsilon^3)`.
   The actual normalized initial grade-one coordinate is
   `epsilon r_i+O(epsilon^3)`, `r_i=R_i/sqrt(b_i)`, and its low coordinate
   is `beta_i+O(epsilon^2)`.
4. The rotor high generator is the finite Laurent matrix

       L(theta) = -i delta [[0,Q(theta)^*],[Q(theta),B(theta)]]
                         - kappa P_bright.

   Its exact dark-dark block vanishes. The supplied sharp-tail argument gives

       ||exp(tau L(theta))|| <= sqrt(3) exp[-c tau a(theta)],
       a(theta)=sum_{j=1}^5 sin(theta_j)^2,

   for a fixed `c>0`, through the rational Laurent singular-value certificate.
   I use this inequality conditionally; I did not rerun the large Laurent
   certificate or inspect its independent checker. The actual `r_i` are finite
   Laurent polynomials. The exact list of eight rank-defect phases is more
   information than this proof needs; confinement to the 32 sign phases suffices.

These are mathematical imports, not retained or physically selected laws.
The new proof does not use trace-norm convergence against the unbounded H.

## 1. A weighted rotor-decay lemma

Let `u_i(tau)=exp(tau L)r_i`. Identify the physical W=1 space with
`ell^2(Z^5;C^96)` by the supplied Gauss coordinates. Let
`Lambda^2` multiply a word of chord field `n` by `1+|n|^2`. I claim

    ||u_i(tau)|| <= C_i (1+tau)^(-5/4),
    ||Lambda^2 u_i(tau)|| <= C_i (1+tau)^(-1/4).          (A)

The second estimate is the new bridge. A naive twice-differentiated global
bound would lose two powers of tau and would not suffice.

Here is a local spectral proof, including the degeneracies. At a sign phase
`theta_*`, any imaginary-axis eigenvector of L has bright component zero:
the real part of `<x,Lx>` is `-kappa ||P_bright x||^2`. For a vector `(d,0)`,
its dark component under L is zero. Therefore an imaginary-axis eigenvalue is
necessarily zero, and its kernel is

    K_* = {(d,0): Q(theta_*)d=0}.

Every vector in this kernel is also killed by `L(theta_*)^*`. Consequently
K_* reduces L and its zero eigenvalue is semisimple. The restriction to its
orthogonal complement has strictly negative spectral real parts. This proves
a positive local fast spectral gap without assuming simple eigenvalues or
normality of the fast block.

If the kernel is empty, the entire local matrix is exponentially stable.
Otherwise take its Riesz cluster around zero and an analytic, uniformly
invertible local intertwiner `V(theta)` with `V(theta_*)=I`. It block
diagonalizes L into a slow matrix `A_s(theta)` on fixed K_* and a fast matrix.
At the central phase,

    A_s(theta_*)=0,
    partial_j A_s(theta_*) = P_* (partial_j L)(theta_*) P_* = 0.

The last equality uses the identically zero dark-dark block and the constant
bright loss. The derivative of the similarity contributes a commutator with
L(theta_*), whose compression to K_* is zero. Thus, with
`x=theta-theta_*`,

    ||A_s(x)|| <= C |x|^2,
    ||partial A_s(x)|| <= C |x|,
    ||partial^2 A_s(x)|| <= C.

The imported global semigroup inequality, conjugated by bounded V, gives

    ||exp(tau A_s(x))|| <= C exp[-c' |x|^2 tau].

Duhamel differentiation now gives, uniformly in a fixed sufficiently small
neighborhood,

    ||partial exp(tau A_s)||
          <= C tau |x| exp[-c' |x|^2 tau],
    ||partial^2 exp(tau A_s)||
          <= C (tau+tau^2 |x|^2) exp[-c' |x|^2 tau].

A harmless decrease of c' can absorb fixed constants. Derivatives of V,
its inverse, the local projections, and the finite Laurent input are bounded.
The fast block and its first two derivatives are bounded by a polynomial in
tau times `exp(-eta tau)`: its spectrum stays in a strict left half-plane on
this compact local neighborhood, and a common Dunford contour gives a uniform
bound. Away from neighborhoods of the sign phases, the supplied bound has a
uniform positive a(theta). A finite smooth partition completes the estimate
on the torus.

The resulting pointwise order-two derivative bound is a fixed multiple of

    [1+tau|x|+tau+tau^2|x|^2] exp[-c'|x|^2 tau]

plus an exponentially decaying polynomial. In dimension five, Gaussian
integration of its square yields

    ||partial^alpha u_i(tau)||_L2
          <= C_i (1+tau)^(|alpha|/2-5/4),  |alpha|<=2.

For example the squared `tau` term gives
`tau^2 tau^(-5/2)=tau^(-1/2)`, and the squared
`tau^2|x|^2` term gives the same exponent. Parseval and equivalence of the
finite set of Sobolev order-two norms with `||Lambda^2 u||` prove (A).
The proof accommodates the supplied one-, two-, and four-dimensional kernels.

## 2. Finite-spin comparison on a genuinely growing fast-time interval

Extend finite-spin operators by zero outside the physical spin box. Physical
edge fields are fixed linear functions of the five chord fields and the
finite charge word; hence `1+sum_e E_e^2` and `1+|n|^2` are comparable up to
fixed constants.

For an allowed spin hop with `x=E(E-s)/C` in [0,1],

    |sqrt(1-x)-1| = x/(1+sqrt(1-x)) <= x.

The analogous birth estimate holds. If the source or destination is outside
the box, the missing rotor amplitude is bounded by a constant times
`C^(-1)(1+sum_e E_e^2)`, since then some edge has magnitude at least S.
At an exact spin boundary the actual zero amplitude is retained. Finite
products telescope, and finite shifts change this weight by only a fixed
factor. The actual high generators consequently obey the operator-domain
estimate

    ||(A_1,S-L)u|| <= C_0/C ||Lambda^2 u||,
    A_1,S=-i delta G_1,S-kappa Gamma_1,S/2,               (B)

for every order-two weighted vector. This bound includes box truncation;
it is not convergence on a fixed support alone.

Let U map W grades to Hermitian clusters, let P_r and E_r be respectively
Hermitian and exact no-event projectors, and put

    S_epsilon=sum_r E_r P_r=I+O(epsilon^3),
    C_epsilon=S_epsilon U.

In these exact no-event coordinates the fast grade-one scalar phase can be
removed. Its remaining generator is

    A_ex,1 = A_1,S + epsilon^2 R_epsilon,S,
    sup ||R_epsilon,S|| < infinity.

This is an operator-norm identity at every finite S, from the uniform analytic
even cluster expansion. Its semigroup has an all-time bound independent of S
and epsilon: it is a restriction of the exact contractive no-event semigroup,
conjugated by C_epsilon, and removal of the scalar phase has modulus one.
Use zero generator outside the spin box so that this bound remains valid on
the common rotor word space.

Duhamel, with the *exact* semigroup on the left and the rotor evolution on
the right, (A), (B), and `C^(-1)=(K/delta)epsilon^2`, therefore proves for
all tau>=0

    ||exp(tau A_ex,1)r_i - exp(tau L)r_i||
       <= C_i epsilon^2 integral_0^tau
                    [(1+s)^(-5/4)+(1+s)^(-1/4)] ds
       <= C_i epsilon^2 (1+tau)^(3/4).                  (C)

The norm of the rotor trajectory is integrable; the weighted norm is not,
and its explicit three-quarter power is essential. No compact-tau limit is
being evaluated at a moving tau.

Take `tau_*=epsilon^(-1)` and `t_*=epsilon^2 tau_*=epsilon`. Equation (C)
and (A) give

    ||exp(tau_* A_ex,1)r_i|| = O(epsilon^(5/4)).

The actual initial grade-one coordinate is `epsilon r_i+O(epsilon^3)`, so
its coordinate and physical exact-cluster norm at t_* are
`O(epsilon^(9/4))`. For every later physical time the exact E_1 component
has nonincreasing norm, because E_1 commutes with the full contraction.
Finally `||P_1-E_1||=O(epsilon^3)` and `||v(t)||<=1` give

    sup_{t>=epsilon} ||P_1 v(t)|| = O(epsilon^(9/4)),
    sup_{t>=epsilon} epsilon^(-4) ||P_1 v(t)||^2
                                              = O(epsilon^(1/2)). (D)

The same argument could use `tau_*=epsilon^(-alpha)` for
`4/5<alpha<4/3`; alpha=1 balances the two bounds. It does not supply a
uniform norm decay rate for arbitrary normalizable initial vectors.

## 3. The apparent order-one grade-two mean cancels

The supplied `O(epsilon^2)` initial grade-two norm, by itself, permits an
order-one ordinary microscopic mean. It cannot simply be dropped. The actual
local birth has a stronger property.

For the canonical all-cluster U, the minimal-order block raising a W grade
by m is `epsilon^m F^m/m!`. Its inverse/adjoint has minimal upward block
`(-epsilon)^m F^m/m!`. This follows directly from
`h U Pi_r=U Pi_r h_bar,r`: at minimal order in an upward displacement m,
only m outward hops occur, and the recurrence is `m U_m=F U_(m-1)`.
Diagonal compensation, the within-grade effective coefficients, and canonical
normalization first contribute at higher orders in that displaced block.
The analogous downward recurrence gives the adjoint sign.

Thus the order-three coefficient of the unnormalized rotated birth in W=2 is

    J3 = j F^3/6 - F j F^2/2 + F^2 j F/2
       = (1/6)(jF^3-3FjF^2+3F^2jF-F^3j)P.

The omitted `F^3jP` is zero. Write `F=F_a+F_other` for a mark centered at a.
The primitive local identities used in the supplied first-high-component
proof are `[F_other,j]=0`, `[F_other,F_a]=0`, and `F_a^2=0`, including the
shared-B hard-core zeros. Therefore `ad_F^3(j)=ad_(F_a)^3(j)=0`, and J3
vanishes on all P vectors. This is not a consequence of `[W,j]=-j` alone.

Uniform analytic remainders and the nonzero normalization
`||j U Omega||=epsilon sqrt(b_i)(1+O(epsilon^2))` now give

    ||P_2 phi_i|| = O(epsilon^3),

which already suffices. Parity improves this to O(epsilon^4), but no later
estimate needs the improvement. The generic projector comparison gives
`||E_2 phi_i||=O(epsilon^3)`; exact component contraction and comparison back
to P_2 give

    sup_{t>=0} epsilon^(-4)||P_2 v(t)||^2 = O(epsilon^2). (E)

An independent exact primitive-word implementation checks J3=0 for every
one of the 12 edges and its plus, minus, and coherent marks, preserving all
charge/field words. It also reconstructs the local first-high-component
identity and the norms (2,4), (2,2), (4,6). Its generic five-level lowering
counterexample has nonzero third commutator, confirming that the local
nilpotence hypothesis is consequential. See `primitive_word_check.py`,
`primitive_word_check.log`, and `primitive_word_results.json`.

## 4. Low-band field domains and uniform integrability

Let `a(t)=C_epsilon^(-1)v(t)` be exact no-event coordinates. Their low block
satisfies on the finite-spin P space

    a_0' = [-i K D -i delta H4_S-kappa Gamma_B,S/2
                          +epsilon^2 R0_epsilon,S] a_0, (F)

with a uniformly bounded remainder. For an ordinary mean, boundedness of R0
without a field-domain argument would be insufficient. The needed weighted
bound follows from the supplied local operator definitions as follows.

On each fixed charge sector use

    J_a = exp[a ell(n)],  ell(n)=sum_j |n_j|, a>0 fixed.

Every primitive hop or birth shifts n by a bounded amount. Its coefficient
is uniformly bounded. Conjugating each finite shift by J_a changes its norm
by at most a fixed factor; all diagonal field terms commute with J_a. Thus
T, C_S, Gamma and every fixed finite product have uniform J_a-conjugated
bounds on the spin boxes. Resolvent contours around W have Neumann expansions
with a uniform radius in this weighted operator norm too, after taking
sufficiently small epsilon depending on a. The canonical inverse square
roots and the exact no-event intertwiner have the same convergent-series
property. Consequently every finite Taylor coefficient and its remainder
used above, in particular R0 in (F), has a uniform J_a-conjugated bound.
This is a field-weight version of the analytic perturbation argument, not
an inference from its unweighted conclusion alone.

The normalized actual output is analytic after its nonzero leading epsilon
is divided out. The same weighted expansions, applied to the finite-word
Omega, give

    ||J_a a_0(0)|| <= C_a,
    a_0(0) -> beta_i.

In (F), KD commutes with J_a and generates a unitary diagonal group. The
remaining J_a-conjugated generator is bounded uniformly in epsilon and S.
Its interaction-picture Dyson series or Gronwall estimate proves

    sup_{0<=t<=T} ||J_a a_0(t)|| <= C_(a,T).             (G)

There is no need for D to confine every electric direction: J_a controls all
five chord directions. The same argument applies to w_i(t).

Extend (F) to the common P rotor space using the same KD outside the box and
zero-extended bounded corrections. The boxes reduce this dynamics. The
bounded corrections converge strongly to `-i delta H4_infinity-
(kappa/2)Gamma_B`; the remainders have norm O(epsilon^2). Uniform boundedness,
the common KD interaction picture, and its absolutely convergent Dyson
series therefore give

    sup_{0<=t<=T} ||a_0(t)-w_i(t)|| ->0.                 (H)

For fixed T the initial difference also tends to zero. Since
`0<=D<=C(1+|n|^2)`, (G) gives uniformly vanishing D tails outside `|n|<=R`.
For example the tail expectation is bounded by

    C_(a,T) sup_{|n|>R} (1+|n|^2) exp[-2a ell(n)],

which tends to zero with R. On the finite field cutoff, (H) gives convergence
of the D expectation. Hence

    sup_{0<=t<=T}|<a_0(t),D a_0(t)>-<w_i(t),D w_i(t)>| ->0. (I)

Strong convergence and uniform bounds for H4_S, plus compactness of the
continuous limiting orbit, give the corresponding uniform H4 expectation
limit. This proves the low mean limit in exact no-event coordinates with all
unbounded-operator domains accounted for.

## 5. Returning to Hermitian energy and the full ensemble

Set `b(t)=U^*v(t)`. Since `C_epsilon=S_epsilon U` and
`S_epsilon=I+O(epsilon^3)`,

    ||b_0(t)-a_0(t)|| = O(epsilon^3)

uniformly at all times by no-event contraction and the bounded similarities.
On the spin box `||D||<=C_1 S(S+1)=O(epsilon^(-2))`. The difference between
the two low D expectations is therefore O(epsilon); bounded H4 contributes
a smaller error. The actual Hermitian low Hamiltonian is

    delta epsilon^(-4) h_H,0 = K D+delta H4_S+O(epsilon^2).

Its mean thus converges uniformly on [0,T] to `<w_i,h_rot w_i>` by (I).
The high Hermitian h blocks have uniformly bounded norms. Their ordinary
energy contributions tend uniformly to zero on [epsilon,T] by (D) and (E).
Finally, terminal N=8 energy is exactly zero, so

    Tr(H rho_i(t)) = delta epsilon^(-4)<v(t),h v(t)>

is the full original ensemble mean. This completes the stated conditional
convergence. Nonpositivity of h_rot causes no issue; its negative part is
bounded by the bounded fourth-order term, and the proof uses absolute errors.

## Boundaries, failed shortcuts, and verification limits

- Substitution `tau=t/epsilon^2` into compact-time convergence is invalid.
  Here (C) is an independently proved quantitative growing-time comparison,
  used once at physical time epsilon; exact cluster contraction handles all
  later times.
- Strong density convergence against H, or merely strong `D/C -> 0`, proves
  no ordinary energy limit. (G)-(I) supply the missing uniform integrability.
- Ignoring the initial W=2 coordinate at its supplied O(epsilon^2) bound leaves
  a possible order-one mean. Section 3 proves the necessary local cancellation.
- Differentiating the global rotor bound without the quadratic slow-block
  structure yields only `||Lambda^2 u||=O(tau^(3/4))`; its integrated spin
  error `O(epsilon^2 tau^(7/4))` does not overlap the time scale needed to
  reduce the initial high component below order epsilon^2.
- No finite-spin spectral gap, uniform decay for arbitrary inputs, growing
  volume, moving high-flux input, changed electric completion, or zero-rate
  endpoint is asserted. Constants depend on fixed positive delta,K,kappa.
- The proof of (A) is analytic. The exact primitive-word program checks the
  different local cancellation, not the spectral lemma. Neither the 253
  assertions nor the source hashes certify the continuum argument.
- The sharp-tail Laurent certificate and earlier cluster coefficients remain
  conditional imports. I did not run the full microscopic finite-S numerical
  propagation or reproduce a finite-S quantitative simulation of (C).
- The ordinary variance is still outside this conclusion. Multiplying the
  new high-band norm bound by epsilon^(-8), instead of epsilon^(-4), does not
  yield a vanishing second moment.

The decisive point for POST scrutiny is the local spectral proof of (A) and
the weighted analytic-remainder justification in section 4. Both are spelled
out here so that a disagreement can identify an exact hypothesis or step.
