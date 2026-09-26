# A Gram-kernel invariant controls the first density correction

2026-09-21. Primary extension of the checked symmetric-stirring coefficient
theorem in draft PR8561. Independent review pending. This calculation sets
the context wave drive to zero; it is a controlled comparison of formation
kernels, not a coefficient for the driven transverse process.

## 1. General finite feature menu

Let there be n occupied labels a and vacancy0. Assign real vectors t_a,
with t_0=0, |t_a|<=1, an antipodal label permutation a->-a, and
t_(-a)=-t_a. Set

    M=sum_a t_a t_a^T,        G_ab=t_a dot t_b,
    W_ab=1+j G_ab,            |j|<1.                     (1)

Duplicate or non-unit occupied features do not affect the argument. A
nonzero M is needed for strict positivity below. Each bond on the cubic
torus swaps its whole states at rate kappa N on macroscopic time, with
kappa>0. A vacant site forms each label a at rate beta times the product
of its six nearest-neighbor weights; beta>0. Initially the law is iid with
vacancy v0 in (0,1) and each label having probability (1-v0)/n. All model
parameters are fixed as N grows, and N>=4 keeps the neighbor sites distinct.

At j=0 the exact growing product has

    v(t)=v0 exp(-n beta t),       rho(t)=1-v(t).           (2)

All Taylor coefficients below are coefficients of powers of j at fixed
finite N, without factorials. No fixed-nonzero-j remainder is asserted.

## 2. Matrix-valued first pair response and its vacancy projection

For distinct x,y write Q_N(y-x,t)=[j] E_j[t(eta_x)t(eta_y)^T]. At a birth
at x, differentiating its marked vector drift yields

    beta 1_(eta_x=0) M sum_(z~x)t(eta_z).

In the unperturbed product only z=y contributes to the pair source.
Its one-endpoint value is beta v rho M^2/n; the other endpoint is its
transpose, the same matrix. Symmetric stirring acts only on positions.
Thus

    Q_N(r,t)=M^2 C_N(r,t),
    partial_t C_N=2 kappa N Delta_ref C_N
                   +(2 beta rho v/n) b,
    C_N(r,0)=0,       b(r)=1_(r nearest0).                (3)

Delta_ref is the unit-rate Laplacian on the torus with the origin and
incident edges removed. Reversing two marked endpoints has no effect on
the even spatial response and the symmetric matrix M^2.

For a third distinct site z, the corresponding vacancy-weighted response
is exactly

    [j] E_j[1_(eta_z=0)t(eta_x)t(eta_y)^T]
         =v(t) M^2 C_N(y-x,t).                           (4)

The proof is the same marked-position intertwining as in PR8561, with a
matrix coefficient. The three-mark stirring chain projects to the two
vector-mark chain; swapping a vector mark and vacancy mark exchanges
positions rather than blocking a jump. Uniform births kill the vacancy
mark at rate n beta and have zero vector mean. In the first source, a
term with the neighbor at the vacancy mark vanishes because 1_vac t=0;
the other nonzero source acquires precisely v(t). The source from a
derivative of the vacancy's death rate vanishes pointwise since sum_a t_a=0.
Both finite linear systems have zero initial data, so uniqueness proves
(4), not a finite-j factorization assumption.

## 3. Cubic density coefficient

The total birth intensity has no odd powers of j by antipodal symmetry.
Its quadratic term is

    [j^2] R_j n_x = beta 1_(eta_x=0)
          sum_(unordered distinct y,z~x) t(eta_y)^T M t(eta_z).  (5)

There is no first-order term even before taking expectations. In the
unperturbed product each two-neighbor term in (5) has zero expectation.
Consequently the first two density coefficients vanish. If

    E_j n_x(t)=rho(t)+j^3 m3_N(t)+O_N(j^4),

then (4) gives the exact finite-volume coefficient equation

    m3_N'=-n beta m3_N
         +beta v(t) Tr(M^3) sum_(unordered y,z~0) C_N(z-y,t),
    m3_N(0)=0.                                           (6)

For M!=0 and t>0, positivity of the reflected heat semigroup gives
m3_N(t)>0. This is a coefficient statement, not an all-j monotonicity law.
No closure of unretained higher moments has been assumed.

## 4. Three-dimensional limit and the two new kernels

Use the already checked punctured-torus heat bound from PR8561; the graph,
rate normalization, positive smooth scalar source and limiting argument
are unchanged. For the unit-rate infinite-lattice Green function G_latt
with -Delta G_latt=delta0,

    N C_N(r,t) -> (6 beta rho(t)v(t)/(n kappa)) G_latt(r).

Let A_star=3G_latt(2e_1)+12G_latt(e_1+e_2)=15G_latt(0)-3>0.
The uniform integrated heat bound permits dominated convergence in (6),
yielding

    N m3_N(t) -> [6 beta^2 Tr(M^3) A_star/(n kappa)]
       integral_0^t exp[-n beta(t-s)] rho(s)v(s)^2 ds.      (7)

The geometry supplies A_star; the label kernel supplies Tr(M^3)/n. The
old six-axis comparison has n=6,M=2I_3 and Tr(M^3)/n=4, recovering the
previous coefficient24 beta^2 A_star/kappa.

For the original fourteen-label local-curl law, t_a=(e_a,b_a/2), so
n=14, M=2I_6 and Tr(M^3)/n=24/7. For the Born-compatible deformation,
t_A=e and t_B=b/sqrt(3), so M=(14/3)I_3 and Tr(M^3)/n=196/9.
With the same beta,kappa,v0 their trajectory (2) and scalar equation (3)
are identical. Therefore even at fixed finite N,

    m3_N(Born kernel) / m3_N(original kernel) =343/54.    (8)

This ratio compares the stated normalization of the same j; it is not an
invariant comparison under an arbitrary redefinition of interaction strength.
It gives a concrete correlation effect of the constructive kernel change.

The N^(3/2) density-field centering has a third Taylor coefficient growing
as sqrt(N) times the positive right-hand side of (7). A mean-field-centered
fluctuation theorem therefore needs a separate centering/remainder analysis.
This does not prove a failure at fixed j, give a uniform weak-coupling
regime, or transfer the coefficient to a nonzero context wave drive.

The mathematical supplier for the only asymptotic step is the full heat
bound and limit proof in the frozen PR8561 source at
4ae52ade2299b4dfaff388971f423aa8f6ddf64a; its note SHA-256 is
b10c0ad5fb9e0802b9fb7a5c206d5d9e1970b2c2573a5d792ab29b2758aea0dc.
The extension above checks how the finite-alphabet matrix factors change;
it does not assert a new independent proof of that unchanged geometric bound.
