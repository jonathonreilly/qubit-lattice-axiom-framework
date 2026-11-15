# PRE-STATED — REC-LIB

## Statements fixed before derivation

1. **Domain.** For each n, let Δ_n be the union of pair-coincidence planes,
   E_n the Schwartz functions flat to all orders on Δ_n, and E_{+,n} the
   Schwartz functions vanishing outside 0<t_1<...<t_n. Tests have finitely
   many components and finitely many insertion degrees. Set S_0=1. Reflection
   reverses Euclidean time and the order of insertions; conjugation is
   antilinear. The scalar hypotheses are exactly OSLEAF55 D1–D7 and
   E0′, E1, E2, E3, (Re), with simultaneous permutation of field labels.

2. **L-DOM.** Reflected positive-half products belong to E_{n+m}; compact
   tests away from coincidences, and compact strictly ordered tests,
   respectively are dense in E_n and E_{+,n}. Ordered data plus Euclidean
   covariance and permutation symmetry determine the restricted hierarchy.

3. **L-HILB.** Reflection positivity constructs a Hilbert space, a unit
   vector Ω, a strongly continuous self-adjoint contraction semigroup P_t,
   its generator H≥0, and spatial Euclidean unitaries commuting with P_t.
   For an m-insertion test the translation estimate has weight 1+m t².

4. **L-INS.** The separated insertion operators of REC(d) descend to the
   quotient, have densely defined adjoints and are closable. They reproduce
   ordered Euclidean vacuum products. They are not asserted to be sharp
   time-zero fields or Minkowski fields at this stage.

5. **L-TIME.** Semigroup matrix elements are holomorphic for Re z>0 without
   E0′. Extension of this assertion to every multitime Schwinger kernel
   requires a separately proved domain and analytic-continuation argument.

6. **L-CONT.** Under E0′, E1–E3 and (Re), all n-point kernels continue to
   the appropriate forward tubes with polynomial growth and inverse-power
   boundary-distance bounds sufficient for tempered boundary values. The
   argument must identify where the order sn is used across arbitrarily
   high insertion degrees; fixed-n temperedness alone is not this statement.

7. **L-BV.** A holomorphic tube kernel with suitable global polynomial and
   inverse-distance bounds has a tempered distributional boundary value.
   The exact topology, cone, uniformity and distribution order belong to the
   statement of the proved version.

8. **L-BOOST/SPEC.** Continuing time-space rotations yields a continuous
   unitary representation of the connected Poincaré group on the same
   Hilbert space. Together with nonnegative H, Lorentz covariance gives
   joint translation spectrum in the closed future cone. Individual
   spatial momentum components are not required to be nonnegative.

9. **L-LOCAL.** E3 gives local commutativity of the reconstructed fields.
   Any analytic gluing or edge-of-the-wedge step used in that implication
   must have a full library proof or be listed as an open lemma.

10. **L-GNS.** A tempered, positive, Hermitian Wightman hierarchy with
    Poincaré covariance, spectral support and local commutativity gives
    operator-valued distributions on a common invariant dense domain,
    a cyclic vacuum, and the specified representation. A separate
    identification matches its Hilbert space and time generator to L-HILB.

11. **L-LABEL.** Finite scalar labels are carried through all proved
    constructions with explicit norm factors. Tensor fields additionally
    require a specified real Euclidean representation, reflection matrix,
    and its Lorentz continuation; scalar covariance is not a tensor law.

12. **L-GROW.** For Z=1 and a genuinely uniform unconditional separated
    moment estimate with exponent b_0=p+2, the short-distance/Taylor route
    yields E0′ with s=11 and β=p+3. Conditional higher cumulants alone do
    not supply the singleton or all-order averaging hypotheses of that route.

13. **REC-LIB target.** The hypotheses in statement 1 imply a local tempered
    Wightman theory for finitely many real scalar fields, without a claim
    of unique vacuum unless a separate uniqueness condition is supplied.
    Its Wightman functions analytically continue the restricted S_n, and
    its time generator agrees with H. A tensor version has precisely the
    extra representation hypotheses in statement 11. An unproved lemma in
    this chain leaves this target CONDITIONAL, not PROVEN.

14. **L-GAP.** Once the common-Hilbert-space identification and Lorentz
    covariance hold, a positive gap of H on the full Ω-perpendicular
    subspace gives a Wightman invariant-mass gap. A bound restricted to a
    proper observable subspace gives only that sector's statement. Dense
    reflected-correlation decay with one common rate is a sufficient
    spectral criterion; no such Yang–Mills decay estimate is postulated as
    an established result here.

15. **Completion contract.** The final artifact contains a statement,
    proof or exact unproved obligation, and status for each library lemma;
    its last material is Statement match, Consumers, Open residue, and
    Binding fixes to OSLEAF55. No source repair outside the permitted paths
    and no scientific status promotion is part of this author assignment.

---

# Results — author proof library, 2026-10-29

**R-CONT status: PROVEN in [REC_CONT.md](REC_CONT.md), with independent
source review in [checks/reccont2_review.md](checks/reccont2_review.md).**
That proof now supplies L-CONT from E0′–E3, (Re), S_0=1 for the stated
finite Cartesian tensor class. This file's downstream conditional theorem
is unchanged. No external consumer or physical-existence status is updated.

PROVEN means proved here from the hypotheses printed with the lemma.
ARGUED means a proposed mechanism whose missing step is identified. OPEN
means no proof of the stated implication is supplied. These are author
statuses, not independent-review or audit verdicts. The ordinary mathematical
background is Schwartz/distribution calculus, the Hilbert-space spectral
theorem (including joint spectral measures of commuting translations),
Bochner integration, and Cauchy's formula/identity theorem. Specialized OS
reconstruction, tube-completion, edge-of-the-wedge and Lie-algebra integration
theorems are not imported. The spectral theorem already used in REC(b) is
not itself being re-proved from axioms of functional analysis.

## 1. Exact objects and conventions

Write E_n=^0𝒮(R^{4n}), Ω_n^+={0<t_1<...<t_n},
E_{+,n}={F∈𝒮:F=0 off Ω_n^+}, and D_n=C_c^∞(R^{4n}∖Δ_n).
For m real scalar fields use components F^{a_1...a_n}, 1≤a_j≤m,
with the **sum norm**

    ||F||_k,1 = Σ_(a_1,...,a_n) max_(|γ|≤k)
                  sup_x (1+|x|²)^(k/2)|∂^γ F^{a_1...a_n}(x)|.

For one component this is exactly D1, not an equivalent norm with an
uncontrolled n-dependent constant. A componentwise E0′ estimate is
equivalent to the same estimate on this sum norm by the triangle
inequality and by testing one component. Relative to the maximum component
norm it costs at most m^n. All permutations reverse/permutate labels together
with positions. For scalar labels Θ acts only on positions. Let

    F*(x_1,...,x_n) = overline{F(x_n,...,x_1)},
    B(F,G) = Σ_(n,r) S_(n+r)(ΘF_n* ⊗ G_r).

All sequences are finite, S_0=1, and scalar E1 is exactly the full E(4)
action D4. E3 includes (Re) as explicitly printed in §1.3. No clustering,
unique-vacuum assumption, full ordinary Euclidean moment algebra or
nontriviality assumption is inserted. The phrase “Wightman axioms” below
means their possibly degenerate-vacuum version until uniqueness is supplied.

In Minkowski variables use metric diag(1,−1,−1,−1), future cone
V_+={y:y^0>|y⃗|}, and Wick embedding

    j(τ,x⃗)=(iτ,x⃗).

The ordering convention is z_(r+1)−z_r∈R^4+iV_+. It corresponds to
W_n=⟨Ω,φ(x_1)...φ(x_n)Ω⟩ and U(a)=exp(iHa^0−iP⃗·a⃗).
An overall reversal of Wightman ordering changes both signs, not the result.

## 2. L-DOM — flat spaces, density and determination

**Status: PROVEN. Statement.** Reflected ordered products are admitted flat
tests. Their seminorm is bounded by the product of the respective seminorms.
D_n is dense in E_n and C_c^∞(Ω_n^+) is dense in E_{+,n}. Two E0-continuous,
Euclidean-covariant, symmetric hierarchies agreeing on compact tests with
distinct times agree on E_n. A tempered contact distribution supported on
Δ_n vanishes on E_n. None of these statements asserts E_n dense in all 𝒮.

**Proof.** A smooth function zero on the complement of Ω_n^+ has every
derivative zero there: first differentiate in its interior and then use
continuity at its boundary. ΘF_n* is flat outside t_1<...<t_n<0; G_r is
flat outside 0<t'_1<...<t'_r. An internal collision is in the corresponding
zero region. A cross collision either places a factor in its zero region
or has both times zero, where both factors are flat. Leibniz's rule therefore
makes every derivative of their tensor product zero on Δ_(n+r).
Furthermore

    1+|x|²+|y|² ≤ (1+|x|²)(1+|y|²),
    ||ΘF*⊗G||_k,1 ≤ ||F||_k,1 ||G||_k,1.                 (2.1)

To prove density, first multiply by a smooth cutoff χ(x/R), equal to one
on |x|≤R and zero outside |x|≤2R. The product converges in each Schwartz
seminorm, because the derivatives of the cutoff cost nonpositive powers of
R while one additional Schwartz weight supplies R^−1 on the discarded tail.
For the resulting compact flat test multiply by

    Π_(i<j) ψ(|x_i−x_j|²/ε²),

where ψ=0 up to 1 and ψ=1 from 2 onward. A derivative of order k of this
cutoff is O_(n,k)(ε^−k). On the support of the cutoff error, a nearest coincidence
plane is at distance at most ε. Taylor's formula from the orthogonal
projection onto that plane, using the vanishing of all jets there, bounds
each derivative of the test by C_(n,k,M) ε^M times a higher Schwartz
seminorm. Choosing M>k makes the product error tend to zero. For the ordered
cone use ψ(t_1/ε)Π_i ψ((t_(i+1)−t_i)/ε); flatness on the bounding
hyperplanes gives the same proof. Finite component sums cause no change.

For determination take a compact set K disjoint from Δ_n. At each point
of K there is a unit vector e not orthogonal to any of its finitely many
nonzero pair differences: a finite union of proper great spheres cannot
cover S³ (each has zero surface measure, as a coordinate graph in charts).
The same e works on a neighborhood. A finite subcover and smooth partition
of unity split a test on K into pieces. Rotate each piece so e becomes the
time axis; all times are distinct on its support. E1, the asserted equality
there, and E3 for reordering imply equality on the original piece. Sum and
use density. Finally if T is a tempered distribution supported on Δ_n,
T annihilates each compact off-diagonal approximant; continuity gives
T(F)=0 on E_n. ∎

The qualification matters: δ(x_1−x_2) is a nonzero continuous functional
on full 𝒮 and zero on E_2. Thus this lemma does not construct a unique
extension of S_n to unrestricted Euclidean tests. What is reconstructed
below, under the additional analytic input, is a Minkowski distribution
on full 𝒮; it is not an arbitrary Hahn–Banach extension of Euclidean S_n.

## 3. L-HILB — quotient, semigroup and spatial motions

**Status: PROVEN. Statement.** E0, time/spatial Euclidean covariance, E2
and S_0=1 give precisely REC(a)–(c) on the stated ordered algebra, for any
finite scalar label set. The translation estimate for r insertions is

    ||T_u G_r||_k,1 ≤ 2^(k/2)(1+r u²)^(k/2)||G_r||_k,1.   (3.1)

**Proof.** Lemma L-DOM makes B well defined. Positivity of B(F+λG,F+λG)
for λ=1,i and then arbitrary complex λ gives Hermiticity and
|B(F,G)|²≤B(F,F)B(G,G): if B(G,G)>0 minimize the quadratic in λ;
if B(G,G)=0 its linear term must vanish. Hence the null space N is a
linear space orthogonal to all tests. Complete A_+/N; its dense image is
denoted D_+, and Ω=[1] has norm one.

On r arguments the displacement vector has length √r|u|. For x=y+(ue_0)^r,

    1+|x|² ≤ 2(1+r u²)(1+|y|²),

which proves (3.1), including r=0 with the harmless factor 2^(k/2).
Time-translation invariance gives

    B(F,T_tG)=B(T_(t/2)F,T_(t/2)G)=B(T_tF,G).             (3.2)

For a finite sequence F, E0, (2.1), and (3.1) give constants C_F,M_F
with |B(F,T_uF)|≤C_F(1+u)^M_F for u≥0. Constants can depend on every
insertion degree present; no n-uniform bound is needed in this step.
Put a(t)=B(T_tF,T_tF)^(1/2). Cauchy–Schwarz and (3.2) give
a(t)²≤a(0)a(2t). If a(0)=0 this immediately implies a(t)=0. Otherwise

    a(t) ≤ a(0)^(1−2^−j) a(2^j t)^(2^−j).

The polynomial upper bound on a(2^j t) has logarithm O_F,t(j), so the
last factor has limsup at most one. Thus a(t)≤a(0). T_t descends to a
contraction P_t. Equation (3.2) proves self-adjointness and
⟨[F],P_t[F]⟩=||[T_(t/2)F]||²≥0. Tensor translation gives the semigroup law.
Continuity of translations in Schwartz topology and E0 show

    ||(P_t−1)[F]||²=B(F,F)−2 Re B(F,T_tF)+B(F,T_(2t)F)→0.

The contraction bound extends this convergence to every Hilbert vector.
If P_1v=0, positivity and P_1=P_(1/2)² imply P_(1/2)v=0; iteration and
strong continuity give v=0. The spectral logarithm H=−log P_1 is therefore
a densely defined self-adjoint operator ≥0. Positive square roots give
P_q=exp(−qH) for nonnegative dyadic q, and continuity gives this for every
t≥0. P_tΩ=Ω implies HΩ=0.

A spatial motion commutes with reflection, preserves the ordered cone,
and preserves B by E1. It consequently gives a unitary with the inverse
motion as inverse; composition is exact on D_+. Its action is strongly
continuous because the action on Schwartz tests is continuous. To see the
latter directly, a coordinate derivative of order k after a four-dimensional
rotation has at most 4^k terms of coefficient modulus ≤1, and a common
translation b changes the weight by at most
2^(k/2)(1+n|b|²)^(k/2). The mean value theorem gives convergence in every
seminorm using one further derivative and weight. Spatial unitaries commute
with P_t on D_+, hence everywhere, and fix Ω. ∎

No inference that P_j≥0 is made. Positivity is an assertion about energy H.
Neither uniqueness of Ω nor a nonzero excited sector follows here.

## 4. L-INS — the separated insertion, including its adjoint

**Status: PROVEN. Statement.** Let τ>0 and h_a∈𝒮(R^4), supported in
0<t<τ/2 in the “zero off” sense. On D_+ set

    A_τ(h)[F]=[h⊗′T_τF].

It is well defined, maps D_+ into D_+, is closable, and its ordered vacuum
products give the nested tensor formula of REC(d).

**Proof.** Supports are strictly ordered, and flatness handles their
boundaries. Translate the entire pairing B(G,h⊗′T_τF) by −τ/2. If

    h^♯_a(t,x⃗)=overline{h_a(τ/2−t,x⃗)},
    K_G=h^♯⊗′T_(τ/2)G,

the reflected bra, the h insertion, and the translated ket give exactly

    B(G,h⊗′T_τF)=B(K_G,T_(τ/2)F)
                =⟨P_(τ/2)[K_G],[F]⟩.                  (4.1)

For F null this vanishes for every G; choosing G=h⊗′T_τF proves its
image null. For each fixed G the last expression is bounded in [F], so
[G] lies in the adjoint domain. If G has two representatives their
right-hand vectors agree: their difference pairs to zero with dense D_+
by the left side of (4.1). The adjoint therefore has dense domain; explicitly,
if v_j→0 and A_τ(h)v_j→w, pairing with every vector in that adjoint domain
gives w=0, which is the closability criterion. Finally apply the insertions
successively to Ω and use ⟨Ω,[F_n]⟩=S_n(F_n). ∎

These operators have a positive support gap and include an explicit shift.
Taking τ→0, defining a sharp time-zero field, or substituting them into an
arbitrary product at complex times would require another argument.

## 5. L-TIME — what semigroup analyticity actually establishes

**Status: PROVEN (single cut and bounded chains). Statement.** For v,w∈H,
z↦⟨v,exp(−zH)w⟩ is holomorphic on Re z>0, continuous at Re z=0 in
the strong-operator sense, and bounded there by ||v||||w||. If bounded
operators B_1,...,B_r are inserted between semigroups, the corresponding
matrix element is jointly holomorphic when every Re z_j>0. E0′ is unused.

**Proof.** Spectral integration gives exp(−zH); its norm is ≤1. On
Re z≥δ>0,

    ||H^k exp(−zH)|| ≤ sup_(λ≥0) λ^k e^(−δλ)
                    ≤ k! δ^−k,

where the last inequality follows from e^(δλ)≥(δλ)^k/k!. Taylor series
therefore converge in operator norm on |h|<δ, proving holomorphy. Dominated
convergence in each vector's spectral measure proves strong boundary
continuity. For finitely many bounded B_j the product of these locally
norm-convergent series converges absolutely, proving joint holomorphy and
the bound ||v||||w||Π||B_j||. For a Euclidean cut, (3.2) identifies
B(F,T_tG) with such a single matrix element for real t>0; uniqueness of
one-variable continuation fixes that cut. ∎

**Unproved extension of this statement.** The A_τ(h) of L-INS are generally
unbounded. Their closability does not imply that exp(−zH) maps into the
domains of their products. Nor does separate continuation at fixed real
values of other time gaps prove holomorphy on their entire product
half-plane. The all-gap assertion in approach step 2 is part of L-CONT
below, not a consequence silently appended to this lemma.

## 6. L-CONT — the exact analytic input

**Status: PROVEN from E0′–E3, (Re), S_0=1; see REC_CONT.md.** For each n and
ordered label word a, there are holomorphic functions 𝒲_n^a on

    𝒯_n={z∈C^(4n): Im(z_(j+1)−z_j)∈V_+, 1≤j<n},

with 𝒲_0=1. Their restrictions to the Wick slice j(x_1),...,j(x_n)
agree as distributions with S_n^a on compact tests with t_1<...<t_n.
For n=1 the function is constant. The functions are invariant under common
complex translations and have, for some finite C_n,A_n,B_n independent of
z and of the label word, the bound

    |𝒲_n^a(x+iy)| ≤ C_n(1+|x|+|y|)^B_n (1+d_n(y)^−1)^A_n,
    d_n(y)=min_(j<n){(y_(j+1)−y_j)^0−|(y_(j+1)−y_j)⃗|}.   (6.1)

The common-translation condition also follows from the matching and E1
by differentiating and analytic uniqueness. It is written here to remove
any ambiguity about center-of-mass variables. For n=1 set d_1=1.
Constants may depend on n; the theorem below does not require a claimed
linear bound on the output exponents. The input E0′, however, has one s,
α,β for every n, exactly as in §1.3.

**What has and has not been derived.** L-TIME supplies a single-cut
continuation. Norm estimates for a state with r insertions involve a
2r-point distribution. Repeating continuation across more cuts therefore
uses unbounded insertion degrees even for a fixed target n. The budgets
available from E0′ are

    order(S_r)/r ≤ s,
    log(max(1,α(r!)^β))/r ≤ log(max(1,α))/r + β log r.    (6.2)

The inequalities in (6.2) follow directly from r!≤r^r. They are the
uniform derivative and constant budgets that an iteration must propagate.
E0 with arbitrary N_r,C_r supplies neither budget. In particular, the
corrected factor (1+r u²) in (3.1) cannot be discarded inside such an
iteration merely because it was harmless for a fixed finite test sequence.

**Attempted route and remaining proof.** Continue single cuts, extend
Hilbert-valued states from continued positive kernels, and enlarge the
domains of the time differences; then combine Euclidean rotations to obtain
𝒯_n. A successful implementation must define the domains at every stage,
prove that their union reaches every compact subset of the target tube,
prove consistency on overlaps, and propagate estimates with finite final
A_n,B_n,C_n. It must also control spatial derivatives/weights and removal
of test smearing. An arbitrary real-analytic tempered distribution need
not satisfy a pointwise polynomial bound, so distributional E0′ alone
cannot be substituted for that estimate without the positivity argument.
No domain-exhaustion or quantitative propagation proof is supplied here.

The route is **ARGUED**, not a new theorem. L-KERNEL below proves one of its
ingredients once a holomorphic kernel already exists; it does not produce
the missing kernel or its domain. An OS II theorem citation would supply
precisely the load-bearing step the assignment asks to rebuild, and is not
used to mark this lemma PROVEN. The local-semigroup alternative [m] would
instead require invariant domains, essential self-adjointness and group
integration; none of those requirements is discharged by renaming the route.

## 7. L-BV — a boundary-value theorem with a full proof

**Status: PROVEN. Statement.** Let C⊂R^d be a nonempty open convex cone
and f holomorphic on R^d+iC. Suppose, for finite A,B,K≥0,

    |f(x+iy)|≤K(1+|x|+|y|)^B
                   (1+dist(y,∂C)^−1)^A.                (7.1)

Then f(·+iy) has a unique limit T in 𝒮′ as y→0 within C, with no
nontangential restriction. T is bounded by a finite Schwartz seminorm.
Indeed for a sufficiently large fixed N and |y|≤1,

    |T_y(φ)|≤K'|φ|_N,
    |T_y(φ)−T(φ)|≤K''|y||φ|_(N+1),                     (7.2)

where T_y(φ)=∫f(x+iy)φ(x)dx. A holomorphic function satisfying (7.1)
and having zero boundary distribution is identically zero. The same result
holds componentwise for a finite family.

**Proof.** Choose e∈C and c>0 with B(e,c)⊂C. Cone convexity gives
B(y+te,tc)⊂C for y∈C,t>0. Hence dist(y+te,∂C)≥ct.
For |y|≤1 and 0<t≤1, (7.1) is bounded by
K_e t^−A(1+|x|)^B. Integration against a Schwartz test is legitimate.
Holomorphy and integration by parts give, for h(t)=T_(y+te)(φ),

    h^(j)(t)=(-i)^j T_(y+te)((e·∇)^jφ).                 (7.3)

For justification, first integrate over a large ball with a smooth cutoff;
Cauchy's estimates on a smaller tube give polynomial growth of each
derivative on compact t-intervals, so the boundary terms vanish as the
cutoff radius grows. The integral of (1+|x|)^B times a derivative of φ
is bounded by a finite Schwartz seminorm. Fix an integer ℓ>A and, for
example, an integer N≥ceil(B)+d+ℓ+2. Then (7.3) is bounded by
C_j t^−A|φ|_N for j≤ℓ. Taylor's formula backwards from t=1 gives

    h(0)=Σ_(j=0)^(ℓ−1) (-1)^j h^(j)(1)/j!
          + (-1)^ℓ/(ℓ−1)! ∫_0^1 t^(ℓ−1)h^(ℓ)(t)dt.    (7.4)

For each fixed interior y, h is smooth at zero. The integral in (7.4)
has the uniform majorant C t^(ℓ−1−A)|φ|_N, whose integral is finite.
This proves the first bound of (7.2), uniformly even for y approaching
the sides of the cone. Apply that bound to ∂_jφ. Since
∂_(y_j)T_y(φ)=−iT_y(∂_jφ), integration along the segment from y to y′
(which lies in C) gives

    |T_y(φ)−T_y′(φ)|≤C|y−y′||φ|_(N+1).

Consequently all approaches to zero have the same limit, with the stated
seminorm and rate. This establishes a tempered distribution, not merely
pointwise convergence on a chosen family of tests.

For uniqueness take the ordinary Fourier transform in x. The
Cauchy–Riemann equations give ∂_(y_j) T̂_y=−p_j T̂_y as distributions
in p. Restrict to compactly supported smooth momentum tests, so all
exponential multipliers below are legitimate. Along the ray ry_0 the
distribution exp(r p·y_0)T̂_(ry_0) has derivative zero. Its limit at
r=0 is T̂. If T=0, this proves T̂_(y_0)=0 on every compact momentum
test; hence T_(y_0)=0. A continuous function defining the zero distribution
is zero, and y_0 was arbitrary. ∎

For (6.1) use C={y:successive differences lie in V_+}. The linear
difference map is surjective onto its relative coordinates; Euclidean
distance to its boundary is comparable, by constants depending on n, to
d_n(y). Common-translation lineality causes no problem in the proof.
Thus L-BV applies in all 4n real coordinates. The n=1 constant case is
immediate. This lemma removes the need to import a boundary-value theorem;
it does not establish its hypothesis (6.1).

## 8. L-BOOST — rotations to Lorentz covariance, without group integration

**Status: PROVEN as an implication from L-CONT and E1 (scalar labels).**
Every 𝒲_n and its boundary W_n are covariant under the connected real
Lorentz group and translations.

**Proof.** Ordered real Euclidean configurations form a nonempty totally
real open slice of 𝒯_n under j. “Totally real” is literal here: each
time coordinate lies on iR and each spatial coordinate on R, giving
4n independent real coordinates. A holomorphic function zero on an open
piece of this slice is zero nearby by its Taylor expansion in those
coordinates, and then on the connected tube by analytic continuation.

The matched Schwinger distribution is a smooth function on that slice.
Euclidean rotations sufficiently close to the identity preserve strict
time ordering on a small neighborhood of any one configuration. E1
therefore gives its rotation differential equations there. For a rotation
in the 0j-plane, conjugation by j turns the rotation generator into
−i times the boost vector field

    L_j=Σ_r (z_r^j ∂_(z_r^0)+z_r^0 ∂_(z_r^j)).

Thus L_j𝒲_n=0 on the slice, hence on 𝒯_n. Spatial rotation and common
translation differential equations follow the same way. For a real boost
B_j(u), the entire path B_j(u)z remains in 𝒯_n because V_+ is invariant;
d𝒲_n(B_j(u)z)/du=0. Integration proves real-boost invariance.
Spatial rotations and boosts generate the connected Lorentz group:
send a future unit vector to e_0 by a boost, leaving a spatial rotation
as the stabilizer. Translations are already part of E1 and L-CONT.
Taking boundary distributions by L-BV transfers these identities to W_n;
linear changes of variables act continuously on Schwartz space and send
admissible imaginary directions to admissible ones. ∎

This proves distributional covariance without assuming self-adjoint boost
generators. The unitary representation will be obtained from the positive
Wightman functional in L-GNS, rather than by integrating unbounded
Euclidean generators on an unproved common domain.

## 9. L-LOCAL — explicit analytic gluing at a spacelike pair

**Status: PROVEN as an implication from L-CONT, E1 and E3, for scalar
labels. Statement.** On (x_(k+1)−x_k)²<0 the boundary distributions satisfy

    W_n^(...ab...)(...,x_k,x_(k+1),...)
       =W_n^(...ba...)(...,x_(k+1),x_k,...).              (9.1)

This is the particular analytic-gluing assertion used here. No general
edge-of-the-wedge theorem is assumed.

**Proof.** First fix a real equal-time pair with difference (0,r,0,0),
r>0; real translations and spatial rotations allow this normalization.
Give all spectator variables complex values whose successive imaginary
differences are strictly future timelike, except that the fixed pair has
zero imaginary difference. Spectators before the pair have imaginary
parts strictly before zero, and those after it strictly after zero. The
spectator domain D is open and convex. For any point of D choose θ>0
small enough that the complex boost B_1(iθ) leaves all other imaginary
differences inside V_+. Its effect on the pair difference is

    B_1(iθ)(0,r,0,0)=(i r sin θ,r cos θ,0,0),

so the full configuration enters 𝒯_n. Define its extension at the
unboosted configuration by 𝒲_n(B_1(iθ)z). It is independent of sufficiently
small positive θ: along that interval its derivative is iL_1𝒲_n=0
by L-BOOST. Choosing a fixed θ on each small spectator neighborhood
therefore defines consistent holomorphic germs on all of D.

These germs really extend the original function on its tube side.
For a pair gap (iδ,r,0,0), δ>0, its imaginary time after B_1(is) is
δ cos s+r sin s>0 for 0≤s≤θ<π/2, and its imaginary spatial part is
zero. The other gaps stay strictly future for small θ. Thus the whole
path from s=0 to θ lies in the tube and the boost differential equation
identifies the germ with the original value there. At each fixed δ>0
the strict inequalities persist on an open neighborhood. Analytic
uniqueness extends this agreement over the connected intersection of
a sufficiently small polydisc with the original convex tube. The same
argument, with the opposite sign, applies to the permuted tube.

For the permuted pair use B_1(−iθ); its reversed difference also acquires
a future imaginary part. This defines the corresponding permuted germs
on the same D. On the Euclidean spectator slice, with negative ordered
times before the pair and positive ordered times after it, both boosts
are Euclidean rotations under j. The original distribution is smooth
near the equal-time separated pair: rotate slightly into a strictly
ordered chart, where L-CONT is smooth, and pull back by E1. E1 and E3
then identify the two germs with that same value of S_n. They agree on
an open totally real spectator slice, hence throughout connected D.
For n=2 there are no spectators; the same Euclidean rotation and E3
give the equality directly.

For any real spacelike pair a real Lorentz transformation makes its
difference equal-time: choose the boost velocity v=Δx^0/|Δx⃗| along
Δx⃗, with |v|<1. It preserves all future spectator imaginary differences.
L-BOOST transports the equality just proved. Locally a fixed complex
boost works on a whole neighborhood of this real pair, so the extensions
are holomorphic germs also in the pair coordinates. The conclusions are
therefore locally uniform on compact real sets with spacelike pair.

It remains to justify the boundary, rather than just equality of germs.
Let φ be a compactly supported smooth test inside the spacelike-pair
region. For ε>0 place the spectator imaginary times at strictly ordered
multiples of ε, with the pair both at zero. Separate the pair by ±δ/2
in imaginary time, 0<δ<ε, choosing the sign for the original or the
permuted tube. At fixed ε, each compact support admits a common small
complex-boost neighborhood (or a finite cover and partition of unity).
Holomorphy there shows that the integrals against φ tend, as δ↓0, to
the integrals of the two germs. Those integrals are equal.

For the original tube, (7.2) bounds the difference between its integral
at these imaginary times and W_n(φ) by C ε|φ|_(N+1), uniformly in
δ<ε. The permuted tube has the same bound with its own finite constant
and seminorm order. Let δ↓0 first and then ε↓0. The common germ
integrals therefore give equality of the two boundary distributions
against φ. Compact tests exhaust the open spacelike-pair region,
proving (9.1). This argument uses the uniform, all-approach estimate in
L-BV; radial boundary limits alone would not justify the two limits. ∎

## 10. L-KERNEL — continuation of vectors from a positive kernel

**Status: PROVEN. Statement.** Let D_j be connected complex domains and
E_j⊂D_j open pieces of totally real affine slices of real dimension
dim_C D_j (maximal totally real slices). Suppose K_(ij)(z,w)
is antiholomorphic in z and holomorphic in w on D_i×D_j. Suppose vectors
v_j(t) in a Hilbert space H for t∈E_j have

    ⟨v_i(s),v_j(t)⟩=K_(ij)(s,t),

and their span is dense. Then these vectors have unique single-valued
holomorphic continuations v_j(z) to D_j, with the same kernel on all
D_i×D_j. On a polydisc centered at a continued point, with radii r_ν
and |K_(jj)|≤M on its product with itself, their Taylor coefficients obey

    ||c_α||≤sqrt(M) Π_ν r_ν^−α_ν.                       (10.1)

**Proof.** Change complex linear coordinates to make an initial real
slice ordinary R^d. Difference quotients of v(t) exist in H to every
order. For the first derivative, the squared norm of the difference of
two difference quotients is a double finite difference of K. Express
each finite difference by the integral of the corresponding derivative
over its real segment. Continuity of ∂_s∂_tK makes this norm tend to
zero. Induction with higher finite differences gives all derivatives
and their inner products as the corresponding mixed derivatives of K.
This also proves continuity of each derivative. Cauchy's formula on a
product polydisc gives

    ||(∂^α v)(a)/α!||²
       = (∂_(bar z)^α ∂_w^α K)(a,a)/(α!)²
       ≤ M Π_ν r_ν^−2α_ν.

For |z_ν−a_ν|<r_ν the norm sum of the vector Taylor series is bounded
by sqrt(M)Π_ν(1−|z_ν−a_ν|/r_ν)^−1. It converges locally uniformly,
so it defines a holomorphic vector. Expanding both sides of its inner
products gives K; comparison with the original v on the real slice
shows agreement there. In particular the continuation has the same
inner products with every original vector.

The same argument works at any point where v has already been continued:
the derivative identity with K holds locally, and Cauchy's estimate uses
the entire larger polydisc where K exists, not only the smaller domain
where v was previously known. Along a compact path in D_j, choose a
positive uniform radius of product polydiscs contained in D_j×D_j.
Finitely many overlapping Taylor extensions then reach its endpoint.
At every step the pairings with all original vectors continue the
globally defined functions K_(ij)(s,z), by the identity theorem. Two
paths therefore give vectors with identical pairings against a dense
set, hence the same vector. Applying analytic uniqueness in both variables
proves the kernel identity for all continued pairs, including different
j. This proves existence, uniqueness and (10.1). ∎

The statement has a strong, explicit hypothesis: the mixed kernels already
exist on the full product domains. It cannot be applied to an unexplained
“continued norm” on just the diagonal, nor used to infer L-CONT.

## 11. L-POS — positive boundary hierarchy on the original OS Hilbert space

**Status: PROVEN as an implication from L-CONT and E2. Statement.** The
W_n obtained in L-BV are positive in the full Minkowski Schwartz polynomial
algebra. There are vectors V(F)∈H_OS, for every finite Schwartz sequence F,
such that

    ⟨V(F),V(G)⟩=Σ_(n,r) W_(n+r)(F_n*⊗G_r),             (11.1)

and their span is dense in H_OS. The vacuum is the same Ω.

**Proof.** First construct point vectors at real ordered positive
Euclidean configurations. Approximate each such labeled configuration
by normalized smooth mollifiers with compact support in the ordered
cone, regarded as OS test vectors. Their inner products converge to

    K_(n,r)(z,w)=𝒲_(n+r)(bar z_n,...,bar z_1,w_1,...,w_r),
    z_l=j(x_l), w_l=j(y_l),                              (11.2)

because L-CONT is smooth there and matches S. The squared norm of a
difference of two mollifier vectors therefore tends to zero. This gives
actual point vectors with kernel (11.2), independent of the mollifiers.
Integrating them against a compact ordered test recovers its OS class:
Riemann sums converge in norm by continuity of the kernel on the compact
product support, and their pairings with all compact tests agree with B.
L-DOM and continuity of B make their span dense in H_OS.

Take

    D_n^V={z: Im z_1∈V_+,
                Im(z_(j+1)−z_j)∈V_+ for j<n}.

These are convex domains. For z∈D_n^V,w∈D_r^V the entire argument of
(11.2) belongs to 𝒯_(n+r): its middle gap has imaginary part
Im z_1+Im w_1∈V_+. The kernels are therefore defined on the full product
domains required by L-KERNEL. Apply that lemma, including n=0 and all
finite label words. This gives holomorphic OS vectors v_n(z) with
norm²=K_(n,n)(z,z), without introducing a second Hilbert space.

For ε>0 and a Schwartz test F_n, set

    V_ε(F_n)=Σ_a ∫ F_n^a(x) v_n^a(x_1+iεe_0,...,
                                             x_n+inεe_0) dx.

The square-root bound from (6.1) on K_(n,n) has polynomial real-coordinate
growth and finite inverse powers of ε, so this Bochner integral exists.
Its pairing with V_δ(G_r) is the integral of 𝒲_(n+r) with negative
ordered bra regulators and positive ordered ket regulators, against
F_n*⊗G_r. L-BV makes the limit, as ε,δ↓0 independently, equal to
W_(n+r)(F_n*⊗G_r). Applying this fact to the four terms in
||V_ε(F)−V_δ(F)||² proves that V_ε(F) is Cauchy. Its limit V(F)
satisfies (11.1); positivity and Hermiticity follow from that identity.

For density suppose ψ is orthogonal to every V(F). For each word set
g_n(z)=⟨ψ,v_n(z)⟩. Its norm bound from K_(n,n) has the form (7.1)
on D_n^V: the relevant distances are those of Im z_1 and the successive
imaginary differences to the future-cone boundary. Its boundary
distribution is zero, because integration at the regulators just used
converges to ⟨ψ,V(F_n)⟩=0. Boundary uniqueness in L-BV gives g_n=0.
In particular ψ is orthogonal to all original Euclidean point vectors,
whose span is dense. Hence ψ=0. For n=0, V(1)=Ω throughout. ∎

This is the positivity step that analytic continuation alone must not
silently replace. It also proves density of the Minkowski states in the
OS space, rather than only an isometric inclusion into a larger space.

## 12. L-GNS — fields, domains, covariance and cyclicity

**Status: PROVEN. Statement.** A normalized tempered Hermitian positive
hierarchy W with covariance and the adjacent spacelike symmetry (9.1)
defines local Hermitian scalar operator-valued distributions on a common
invariant dense domain and a continuous unitary Poincaré representation.
For the hierarchy of L-POS this representation acts on H_OS. The spectrum
condition is established in the next lemma, using its identified H.

**Proof.** Let B=⊕_(n≥0)𝒮(R^{4n})⊗C^(m^n), with finite sequences,
the everywhere-defined concatenation product, and conjugate reversal *.
Give it inner product W(F*G), quotient its null space, and complete.
The null space is a left ideal. Indeed for null F and any A,X∈B,

    ⟨X,AF⟩=⟨A*X,F⟩=0

by Cauchy–Schwarz; choose X=AF. Thus left multiplication is well defined
on the quotient D. For a one-point test f in component a define
φ_a(f)[F]=[f_a⊗F]. Its adjoint contains φ_a(bar f) on D by the same
inner-product identity, so it is closable and Hermitian for real f.
D is invariant under every such field. For fixed F, the squared norm
of φ_a(f)F is a finite sum of pairings of tempered distributions with
products of f,bar f and fixed Schwartz tests. It is a continuous quadratic
form in f. Hence f↦φ_a(f)F is continuous in Hilbert norm, which is the
operator-valued-distribution assertion on the common domain; matrix
elements are tempered as well.

Simple tensors of one-point Schwartz functions are dense in every
Schwartz space of n variables. One direct proof first cuts off at infinity,
extends the resulting smooth compact function periodically in a larger
box, and uses its Fourier series. Integration by parts gives frequency
coefficients decreasing faster than any power; multiply each Fourier
factor by a one-point cutoff equal to one on the inner box. The series
then converges with every derivative on a fixed compact set. Letting
the original cutoff grow proves the Schwartz assertion. Continuity of
the above quadratic form makes these approximations converge in the
quotient norm. Consequently products of fields on Ω=[1] are dense.

Translations and connected Lorentz transformations act on each test by
pullback. Covariance of W makes these actions isometric, with inverse
given by the inverse group element. They therefore give an exact unitary
representation, fixing Ω. Continuity of pullback in Schwartz topology
and continuity of W show strong continuity on D, hence on the completion.
Its covariance on fields follows by conjugating left multiplication.

For tests f,g with mutually spacelike supports, (9.1) applied in every
matrix element W(X*([f_a,g_b])F) gives zero. To justify noncompact tests,
first cut all factors off compactly and then use Schwartz convergence;
the spacelike support condition is preserved. Thus the commutator vector
is orthogonal to D and is zero. This proves locality as operators on D.

Finally (11.1) maps [F] isometrically to V(F). L-POS proves its range
dense, so it extends to a unitary onto H_OS. All the fields and group
operators may be transported by this unitary. ∎

## 13. L-ID/SPEC — the time generator and the joint spectrum

**Status: PROVEN as an implication from L-CONT and the lemmas above.**
The Wightman time generator is the H of L-HILB, on the same Hilbert
space, and the joint spectrum of (H,P⃗) lies in the closed future cone.

**Proof of identification.** On the original Euclidean point vectors,
P_t v_n(z)=v_n(z_1+it e_0,...,z_n+it e_0) for t≥0, by the definition
of T_t and the mollifier limit. Both sides are holomorphic in z on
D_n^V, so L-KERNEL's density/identity argument continues this equality
there. For fixed z both sides are also holomorphic as functions of w
in Re w>0 when t is replaced by w: the left side by L-TIME and the
right side because Im(z_l+iw e_0)=Im z_l+Re w e_0 stays admissible.
Equality on positive real w implies equality throughout that half-plane.
Set w=t−ia and let t↓0. Strong continuity gives

    exp(iaH)v_n(z)=v_n(z_1+a e_0,...,z_n+a e_0).          (13.1)

Integrating and passing to boundary vectors identifies the GNS time
translation with exp(iaH) on a dense set, hence on all H_OS. Its
self-adjoint generator is exactly H (equality of unitary groups fixes
the generator and its domain). The same argument for spatial motions
identifies their GNS and OS actions.

**Proof of spectral condition.** The commuting translation unitaries have
a joint spectral measure E on R^4. Positivity of H puts its support in
p^0≥0. Poincaré covariance transforms E by Lorentz transformations, so
its support is Lorentz invariant. If a support point p had p^0≥0 but
|p⃗|>p^0, choose a boost along p⃗ with speed v satisfying
p^0/|p⃗|<v<1. The boosted energy γ(p^0−v|p⃗|) is negative, contradicting
the support's invariance. Thus p^0≥|p⃗| on the support. Equivalently,
one may apply the nonnegative-energy condition in every boosted frame;
there is no assumption of positive spatial momentum components. ∎

## 14. L-GAP — the precise mass-gap consumer

**Status: PROVEN (conditional corollary). Statement.** Under L-ID/SPEC,
suppose ker H=CΩ and spec(H|Ω^⊥)⊂[m_*,∞), m_*>0. Then the excited
joint spectrum satisfies p²≥m_*², p^0≥0. Conversely a future-cone joint
spectrum with invariant mass at least m_* on Ω^⊥ gives that Hamiltonian
gap. A common exponential bound on a dense family of centered reflected
correlations is sufficient for the Hamiltonian premise. A nonzero excited
space must be supplied if a finite nonvacuous threshold is asserted.

**Proof.** Ω^⊥ is invariant under the Poincaré unitaries, since they fix
Ω. Its joint spectral support is Lorentz invariant and every point has
energy ≥m_*. A future timelike point can be boosted to rest, of energy
sqrt(p²), so sqrt(p²)≥m_*. A nonzero future lightlike point can be boosted
to arbitrarily small positive energy and is excluded. The origin is
excluded on Ω^⊥ by the Hamiltonian gap. The reverse implication is the
inequality p^0≥sqrt(p²) on the future cone.

For the correlation criterion let v_F=[F]−⟨Ω,[F]⟩Ω and assume their
linear span dense in Ω^⊥. From L-HILB its exact reflected expression is

    ⟨v_F,e^(−tH)v_F⟩=B(F,T_tF)−|S(F)|².                (14.1)

If it is ≤A_F e^(−m_*t) for t≥t_F, spectral positivity gives, for
0≤b<m_*,

    e^(−bt)||E_H([0,b])v_F||² ≤ A_F e^(−m_*t).

Let t→∞, then use boundedness of the projection and density, and finally
take a countable sequence b↑m_*. This proves the gap and excludes any
extra zero eigenvector. If Ω^⊥≠0, its spectral projections on finite
intervals increase strongly to the identity, so some finite interval
carries excited spectrum; the positive spectral infimum is finite.
All cutoff/volume passages needed to obtain (14.1) and its decay are
separate premises, not justified by the spectral argument. ∎

Here the full OS test quotient has dense centered classes automatically.
A smaller family of e-only or two-point tests need not have dense span
in the intended full Yang–Mills Hilbert space. A gap of a restriction
therefore proves only that sector's gap unless equality/density of the
sector is established. This is exactly the limitation in MASS_GAP_TARGET.

## 15. L-LABEL — several fields and the tensor dictionary

**Status: PROVEN for the stated finite-dimensional bookkeeping; the
analytic producer remains L-CONT.** For m scalar labels the preceding
proofs apply to all mixed words, with no diagonal-only positivity
assumption. In particular E2 must allow simultaneous sums over different
degrees and different label words; separate RP for each single species
would not be the hypothesis used in L-POS.

**Proof for scalars and constants.** Label reversal is an isometry in the
sum norm; tensor norms multiply, so (2.1) holds with constant one.
Componentwise bounds with the same C_n give the bound C_n||F||_k,1.
There are m^n words, so replacing the sum norm by a maximum component
norm costs exactly the upper bound m^n. This factor satisfies
m^n≤e^m n!, hence can be absorbed into α→αe^m, β→β+1 if that norm
conversion is actually required. With the sum norm and uniform
componentwise inputs it is not required and β remains unchanged.
All finite sums commute with differentiation, limits and integrals used
above. L-KERNEL is applied to the disjoint union of labeled configuration
domains, so its mixed kernels retain every cross-species pairing. E3
permutes the labels as well as the points, giving locality for every
pair a,b. This proves the scalar claim. ∎

**Explicit tensor extension.** The following is a sufficient, fully
specified class, rather than a claim about an unspecified representation.
Take finitely many real bosonic Cartesian tensor fields, with total
component space a direct sum of (R^4)^(⊗r), 0≤r≤r_max. In the Cartesian
basis set

    D_E(R)=⊕_r R^(⊗r),       J=D_E(θ),
    B=diag(i,1,1,1),         C=⊕_r B^(⊗r).

The Euclidean tests transform by D_E(R), Θ includes J on every slot,
and (Re) is ordinary real-component conjugation. Replace the matching
clause of L-CONT by

    𝒲_n(jx_1,...,jx_n)=C^(⊗n) S_n(x_1,...,x_n).          (15.1)

Its analytic and quantitative clauses are proved in REC_CONT.md for this
Cartesian tensor class. Given those clauses, all downstream conclusions
hold for these tensor fields.

**Proof of the tensor implication.** Entrywise J²=1, |C_aa|=1 and
bar C J=C. For a vector Lorentz transformation Λ,
R=B^−1ΛB obeys R^TR=1, since B^TB=−diag(1,−1,−1,−1).
The tensor polynomial representation extends to these complex matrices,
and

    D_M(Λ)=C D_E(B^−1ΛB) C^−1=⊕_r Λ^(⊗r).             (15.2)

This is real for real Λ and is a representation. Thus differentiating
Euclidean covariance in (15.1) yields precisely tensor Lorentz covariance.
L-BOOST's integration is the same linear differential equation with its
finite matrix generator. In L-LOCAL replace each continued scalar value
by D_M(B_1(±iθ))^(−⊗n)𝒲_n(B_1(±iθ)z); its derivative is zero by that
equation. Permutation of slots intertwines the corresponding matrices,
so the Euclidean-slice and boundary arguments are unchanged.

For positivity multiply an Euclidean point vector with component word a
by q_a=Π_l C_(a_l a_l). Its reflected kernel has the bra factor
bar q_a Π_l J_(a_l a_l)=q_a. Thus the kernel of these phased OS vectors
is exactly the kernel built from (15.1), with C on both bra and ket
indices. This proves the initial hypothesis of L-KERNEL in the original
positive Hilbert space. Since the phases are invertible, density is
unchanged. In L-HILB, spatial matrices commute with J; in L-INS the
formula is h^♯=J bar h(τ/2−t,x⃗). Both proofs therefore still apply.
L-GNS uses the test action D_M(Λ^−1)^T F(Λ^−1x); this reduces to the
printed D_E(R) action for real Euclidean rotations. Wightman Hermiticity
follows from the positive kernel, including its vacuum component.

[R-fix 2026-10-29 REC-1] **Corrected tensor bounds (binding review item 1).**
The original paragraph is preserved below as a superseded quotation.
Its arbitrary-direction boost bound and norm-one-generator justification
are false; the corrected statement and proof follow the quotation.

> Quantitatively, ||J||_1=||C||_1=||C^−1||_1=1 in this basis.
> For an orthogonal four-dimensional R, ||R||_1≤2, so
> ||D_E(R)||_1≤2^r_max; on n slots the bound is 2^(r_max n).
> A boost of rapidity u has ||D_M||_1≤exp(r_max|u|), hence costs at most
> exp(r_max n|u|). This bound also holds for complex u: the vector boost
> generator has induced ℓ¹ norm one, and its exponential power series
> is bounded by exp(|u|). Spacetime chain-rule factors are
> still those of L-HILB. Component aggregation costs at most m^n as above.
> These are explicit finite factors and introduce no unbounded label sum. ∎

In the same fixed Cartesian basis,
||J||_1=||C||_1=||C^−1||_1=1. For a real R∈O(4), columnwise
Cauchy–Schwarz gives ||R||_1≤2, hence ||D_E(R)||_1≤2^r_max
and ||D_E(R)^(⊗n)||_1≤2^(r_max n).

For **every real v∈R³ with ||v||_2=1 and every u∈C** (including real
rapidity), define Λ(v,u)=exp(uK(v)), where

    K(v) = [[0, v^T], [v, 0]],
    ||K(v)||_1 = max(||v||_1, |v_1|, |v_2|, |v_3|)
               = ||v||_1 ≤ sqrt(3).

The time-column sum is ||v||_1; the other column sums are |v_j|.
For the induced norm on the complexified Cartesian ℓ¹ space, the
exponential series and submultiplicativity therefore give

    ||Λ(v,u)||_1 ≤ Σ_(k≥0) |u|^k ||K(v)||_1^k/k!
                = exp(||v||_1 |u|).

Induced ℓ¹ norms multiply under tensor products and take the maximum
under a block diagonal direct sum. Thus (15.2), for every n≥0 and every
nonnegative integer r_max bounding the tensor ranks, gives

    ||D_M(Λ(v,u))||_1 ≤ exp(r_max ||v||_1 |u|)
                     ≤ exp(sqrt(3) r_max |u|),
    ||D_M(Λ(v,u))^(⊗n)||_1 ≤ exp(r_max n ||v||_1 |u|)
                           ≤ exp(sqrt(3) r_max n |u|).   (15.3)

The n=0 or r_max=0 case has norm one. For a coordinate-axis direction
v=±e_j, ||v||_1=1, so the original exponent remains valid in precisely
that restricted class, for real and complex u. It fails in general:
for v=(3/5,4/5,0), u=log 2, the time column is
(5/4,9/20,3/5,0), whose ℓ¹ norm is 23/10>2=exp(|u|).
This exact rank-one counterexample explains the correction.

The coordinate-axis matrices B_1(±iθ) and their inverses in L-LOCAL
retain the factor exp(r_max n|θ|). Any arbitrary-direction tensor
boost estimate instead uses (15.3). Spacetime chain-rule factors
remain those of L-HILB, and component aggregation still costs at most
m^n. All these are finite factors; no unbounded label sum or new
physical premise is introduced. ∎

For symmetric/antisymmetric tensors one may retain the redundant full
Cartesian components and impose their linear identities; the above
formula remains a valid sufficient formulation. For an arbitrary abstract
real O(4) representation in OSLEAF55's larger-family paragraph, a
compatible complexification, real Minkowski form, reflection matrix and
Wick conversion must instead be specified and checked. That generic
representation bridge is **OPEN here**. No fermionic or spinor extension
is asserted. The scalar target has no such extra representation premise.

## 16. L-GROW — what really gives s=11 and β=p+3

**Status: PROVEN as the following quantified implication.** Consider
centered lattice fields with Z=1, |ê_a(x)|≤C_X a^−4 for 0<a≤1, and
suppose the **unconditional** moments satisfy, for a fixed c_*>0, n≥2,
all volumes and all configurations with δ=min_(i<j)|x_i−x_j|≥c_*a,

    |E Π_i ê_a(x_i)|≤A_0^n(n!)^b_0 Π_i wbar(δ_i),
    δ_i=min_(j≠i)|x_i−x_j|,
    wbar(r)=min(r,1)^−4 [log(2+1/min(r,1))]^q,  q≥0.     (16.1)

Assume b_0≥0. Constants are independent of a, volume, placements and n.
Then on every compact admissible flat test

    |S_n^a(F)|≤C^n(n!)^b_0 |F|_(10n+1),                (16.2)

with a single C. Any common infinite-volume/cutoff limit continuous on
flat tests satisfies E0′ with s=11, β=b_0+1 and α=e^C (enlarged for
n=0,1 if needed). In particular b_0=p+2 gives β=p+3.

**Proof.** The lattice weight sum has an a-uniform bound

    a^4 Σ_(x∈aZ^4)(1+|x|²)^−5/2 ≤ Z_*<∞.

For the cube of side a centered at x, |y−x|≤a≤1 implies
1+|y|²≤3(1+|x|²). Compare its integral with the summand; one may take
Z_*=3^(5/2)∫_(R^4)(1+|y|²)^−5/2dy. Products give Z_*^n.
Also (1+Σ_i|x_i|²)^−5n/2≤Π_i(1+|x_i|²)^−5/2.

First treat c_*a≤1. If δ≥1, (16.1) and |F|_(5n) bound the sum by
(A_0(log 3)^q Z_*)^n(n!)^b_0|F|_(5n). If c_*a≤δ<1,
the finite number C_q=sup_(0<r≤1) r[log(2+1/r)]^q gives
Π_i wbar(δ_i)≤C_q^n δ^−5n.
Choose a closest pair and project onto its coincidence plane by replacing
the two points by their midpoint. The displacement h has Euclidean
length δ/√2 and only eight nonzero coordinates, hence ||h||_1≤2δ.
Along its normal segment to x, 1+|x|²≤2(1+|z|²) when δ<1.
Taylor's formula with all lower jets zero gives for any integer M≥1

    |F(x)|≤(2δ)^M/M! · 2^(5n/2)|F|_(M+5n)
                                      Π_i(1+|x_i|²)^−5/2. (16.3)

Take M=5n. Even discarding 1/(5n)! leaves only a constant to the n-th
power. The δ powers cancel, proving that region's contribution bounded
by C^n(n!)^b_0 |F|_(10n).

For 0<δ<c_*a use the crude field bound and M=4n+1 in (16.3).
Provided c_*a≤1, the factor a^−4n δ^(4n+1) is at most
c_*^(4n+1)a. Its sum is at most a C^n|F|_(9n+1); constants depending
only on c_* are absorbed into C^n for n≥1. Configurations with δ=0
contribute zero by flatness. For the remaining range c_*a>1, a is
bounded below by 1/c_* and the crude bound plus |F|_(5n) suffices.
All estimates are uniform on admissible supports; restricting a sum
to a finite volume only decreases its upper envelope. This proves
(16.2). Centering gives S_1=0. Density from L-DOM passes the limit
bound to E_n. Finally 10n+1≤11n and C^n≤e^C n! by the nth term
of the exponential series. ∎

**The cumulant qualifier.** Here is exactly the combinatorics, separately
from its missing probabilistic hypotheses. Let p≥0 and suppose total
cumulance is applicable and, for each partition π of n labels with r blocks, its
outer joint cumulant of conditional block cumulants is bounded by

    A^n r! Π_(B∈π)(|B|!)^p Π_i wbar(δ_i).              (16.4)

This is an additional all-order hypothesis, including singleton blocks.
Since Π_B |B|!≤n!, and

    Σ_π |π|! ≤ 2^(n−1)n!,

the unconditional nth cumulant is bounded by (2A)^n(n!)^(p+1) times
the same weights. To prove the count, order the blocks; for each
composition n=k_1+...+k_r their number is n!/(k_1!...k_r!)≤n!, and
there are 2^(n−1) compositions. Passing from cumulants to moments sums
over at most n! partitions (encode a partition by the permutation formed
by its blocks written as cycles with their entries increasing). Block
factorials multiply to at most n!, and the capped weight for a subset is
bounded by the corresponding full-configuration weight. Singleton bounds
must be included explicitly; the capped weight is at least one. Thus
b_0=p+2 is sufficient. This proves the stated combinatorial implication,
not (16.4) for the actual source transport.

SRC-κ's higher conditional cumulants alone do not state (16.4): conditional
means and uniform all-order moments of the outer products remain needed,
as CODEX_REVIEW_SRCCD §7 identifies. Nor does a same-test schematic bound
C_0^n(n!)^p p(f)^n automatically supply a multilinear separated-distribution
bound on E_n; f^⊗n is generally not even in that partial test algebra.
The fixed-seminorm-order slogan therefore cannot replace (16.1) or the
separately proved shrinking-support extension route.

For a crude bound |ê_a|≤C_X a^−q_X instead, use the integer majorant
Q=ceil(q_X), M=Qn+1 in the near region. A safe s is
max(11,Q+6). The value s=11 here is deliberately restricted to Z=1,
q_X=4, exactly as the reviewed correction requires. For finitely many
components with uniform (16.1), the sum norm keeps the same s,β.

## 17. L-VAC — no hidden uniqueness premise

**Status: PROVEN (scope witness). Statement.** E0′–E3 and (Re), even
with S_0=1, do not imply a one-dimensional translation-invariant space.

**Proof.** Let q take values 0 and 1 with probabilities 1/2 each and set
S_n(F)=E(q^n)∫F, n≥1. For finite ordered F its RP form is

    (1/2)|F_0|²+(1/2)|F_0+Σ_(n≥1)∫F_n|²≥0.

The distributions are real, Euclidean invariant and symmetric. The
integral estimate used in L-GROW gives |S_n(F)|≤C^n|F|_(5n), hence
E0′ with s=5, β=1, α=e^C. The two displayed coordinates can be
chosen independently using a constant component and a one-point test
of nonzero integral, so the OS Hilbert space is C². All translations
act as the identity and H=0. The unit vector Ω corresponds to the
constant function one on {0,1}; it is cyclic for multiplication by q,
but its orthogonal complement contains another invariant vector. ∎

This is a counterexample to adding uniqueness to the hypotheses, not to
OS reconstruction and not to Yang–Mills existence. MASS_GAP_TARGET's
unique vacuum must follow from its dense-family decay premise or another
proved uniqueness condition.

## 18. REC-LIB — the assembled theorem and its exact verdict

**PROVEN conditional theorem.** Let S_0=1 and a finite real scalar
hierarchy on the exact E_n spaces satisfy E0, E1, E2, E3 and (Re).
**If L-CONT's matching holomorphic functions and bound (6.1) are supplied,**
then L-BV, L-BOOST, L-LOCAL, L-POS, L-GNS and L-ID/SPEC construct a local
tempered Wightman theory on the Hilbert space of L-HILB. Its vacuum is
cyclic and invariant, its joint spectrum is in the closed future cone,
and its self-adjoint time generator is precisely the OS H. Its Wightman
functions continue the restricted S_n. The functions and the cyclic theory
are unique up to the unitary identification preserving the fields and Ω.
This last uniqueness is uniqueness of reconstruction, not uniqueness of
the invariant vector.

**Proof.** The cited lemmas supply every listed conclusion with their
explicit common domains and identifications. Two matching analytic
functions agree on an open totally real Euclidean slice and therefore
on the connected tube, so their boundary distributions agree. The
map between their polynomial quotient vectors preserving each test
has identical inner products and dense range; it extends uniquely to
the required unitary. L-DOM determines the hierarchy on all E_n from
the ordered data, including configurations with equal times but distinct
positions. No contact extension has been used. The tensor-power version
uses exactly (15.1) and the tensor RP/covariance rules in L-LABEL. ∎

[R-fix 2026-10-29 REC-1] **Downstream tensor scope (binding review item 1).**
The tensor-power extension above uses the corrected fixed-basis bounds
(15.3): exp(r_max n ||v||_1 |u|), or the direction-independent
exp(sqrt(3) r_max n |u|), for real unit v and real or complex u.
The coordinate-axis continuation in L-LOCAL keeps its original exponent.
The phase, reflection and real-rotation bounds were rechecked in §15.
This repairs the tensor constant only; the scalar conditional theorem
and the analytic producer L-CONT retain their stated scope; its current
R-CONT status is recorded below.

**R-CONT target: PROVEN in REC_CONT.md.** Its pass-2 proof derives the
analytic seed and quantitative exhaustion from E0′,E1,E2,E3,(Re),S_0=1,
including the stated finite Cartesian tensor class. The independent review
resolves both binding obligations. This updates the status of the analytic
input to the preceding conditional theorem; external N9/REC(e) consumer
text and source-side follow-through remain outside this status-only edit.

## 19. Literature, author verification and scope discipline

Osterwalder and Schrader receive credit for the theorem and its method.
The public OS I/II URLs returned iframe/service HTML in this session;
their proof text was not retrieved. No challenge was bypassed. The
accessible research paper by [Kravchuk, Qiao and Rychkov, §9.2](https://arxiv.org/html/2104.02090v2#S9.SS2)
was used to locate the continuation/growth distinction, not as proof of
L-CONT. Its discussion also points out the use of unbounded insertion
degrees. [Adamo, Moriwaki and Tanimoto, §2.5](https://arxiv.org/html/2407.18222v2#S2.SS5)
was consulted for the flat-space/ordered-cone formulation. Their
two-dimensional construction is not a four-dimensional reconstruction
input. Glaser and the Klein–Landau/Fröhlich route are orientation [m]
only; no result of theirs is used to discharge a lemma here. The proofs
printed above are this author's arguments and require independent review.

No numerical experiment could certify L-CONT. The optional algebra checks
were not launched: the machine had fewer than 50% free memory at the
resource preflight recorded in REC_LIB_LOG.md. No checks/rec_* runner or
result is claimed. Author verification consists of the proofs, dependency
and hypothesis match, and readback of the two allowed deliverables;
it is not an independent proof check.

### No-Go Discipline Gate — original REC-LIB pass

The following route record describes the original pass, when R-CONT was
open. Its current status is PROVEN as recorded below; no no-go conclusion
or other residue status is changed by that update.

- **N1, actual routes.** The single-cut/continued-kernel route was attempted;
  its all-degree quantitative domain enlargement is unproved. The direct
  complex-rotation route was developed downstream of an existing tube,
  with full proofs above. The symmetric-local-semigroup alternative is
  only named [m] and is untested. No five-family search occurred and no
  packet PASS is claimed. In particular the result is a partial rebuild,
  not exhaustion of available proofs.
- **N2, dependency collapse.** L-CONT's domain and quantitative-bound
  clauses are one joint residual here. The bound presupposes a function
  on the domain; the domain assertion alone does not include that bound.
  No separate independent-obstruction count is asserted. Boundary values,
  Lorentz covariance, locality, positivity and identification follow from
  the joint residual by the proved lemmas. The generic tensor dictionary
  is a separate specification issue; its relation to alternative analytic
  proofs is not asserted independent.
- **N3, hidden hypotheses.** The explicit background functional analysis
  is stated before §1. L-KERNEL requires full product-domain kernels;
  L-LOCAL requires (6.1); L-GROW requires unconditional, all-scale and
  all-order estimates. None is inferred from the word “standard”.
- **N4, residual match.** OSLEAF REC(e) and ASSEMBLY N9 concern precisely
  the missing reconstruction implication. CODEX_REVIEW_OSLEAF F6 concerns
  only the finite-sequence translation bound and does not refute L-CONT.
  CODEX_REVIEW_SRCCD §7 concerns the upstream producer of (16.1)/(16.4),
  not the mathematical implication from already supplied E0′.
- **N5, resolution.** The only new impossibility-shaped statement is the
  explicit two-state L-VAC example, which concerns uniqueness without
  clustering. No per-site, lattice-wide, Yang–Mills or physical no-go is
  inferred. Optional finite numerical checks were not executed.
- **N6, partial closure.** A proof of L-CONT would retire the analytic
  import; it would add mathematics, not a physical axiom. No primitive
  registry change or permission is needed for that mathematical work.
- **N7, steelman.** The original OS continuation strategy is a concrete
  way to finish: establish the iterative domains, Hilbert-vector
  extensions, spatial estimates and quantitative exhaustion using (6.2).
  This file has proved several downstream tools but has not defeated
  that strategy. Its incompleteness is not evidence the strategy fails.
- **N8, prior echoes.** The specified local source search found the same
  missing reconstruction in OSLEAF, ASSEMBLY and SRCCD reviews. The
  prior source-access failure did not establish a mathematical obstruction.
  No broad historical no-go search or historical automation was run.

The methodological packet is **not submitted as a no-go PASS**. Its
five-route and committed-packet requirements are not represented as met;
the author brief expressly forbids commits and extra ledger artifacts.
This limits procedural promotion and makes no claim against the theorem.

## Statement match

| OSLEAF55 line / exact requirement | REC-LIB hypothesis or construction | Match and remaining qualification |
|---|---|---|
| D1, line 149: max derivative order k and weight (1+|x|²)^(k/2) | §1, same scalar seminorm | Exact; finite-label sum norm is explicit, with max-norm cost m^n |
| D2, lines 150–154: all jets zero on Δ_n | E_n and L-DOM | Exact; not full Euclidean Schwartz space |
| D2/D5: zero off 0<t_1<...<t_n, finite sequences including n=0 | E_{+,n}, A_+, D_+ | Exact; compact interior density proved |
| D3, lines 155–156: θ, reversal/conjugation *, common T_s | §§1,3–4 | Exact for scalars; labels reverse simultaneously |
| D4, line 157: scalar full E(4) pullback | E1 in §§1,3,8 | Exact; connected Poincaré group is the reconstructed unitary group |
| D6, lines 161–164: partial products only | L-DOM and L-INS | Exact in Euclidean space; full Minkowski products appear only after L-POS |
| D7, line 165: S_0=1 | §§1,3 | Explicit; the abbreviated approach target needs this convention |
| E0′, line 205: one s∈N and α,β≥0, all n≥1 and F∈E_n | §1 and §6; REC_CONT.md | Exact input; R-CONT is proved by the reviewed continuation proof |
| E1, line 207: Euclidean covariance for every g∈E(4) | §1; L-BOOST | Exact scalar hypothesis, including the time reflection |
| E2, line 208: Σ_(n,r) S_(n+r)(ΘF_n*⊗F_r)≥0 on A_+ | B and L-HILB/L-POS | Exact; mixed-label sums required for several fields |
| E3, line 209: permutation symmetry | L-DOM/L-LOCAL | Exact; permutation acts on field labels too |
| (Re), line 209: S_n(bar F)=overline{S_n(F)} | §1 | Explicitly retained; not omitted from the abbreviated E0′–E3 list |
| E4/clustering, lines 210–211: not assumed | L-VAC and §18 | No unique vacuum asserted without an additional proved condition |
| REC(a)–(c), lines 216–221 | L-HILB | PROVEN; F6 insertion-number repair included |
| REC(d), lines 222–226 | L-INS | PROVEN with support gap; no sharp time-zero field claim |
| REC(e), lines 227–232 | §18 conditional theorem | L-CONT is supplied by REC_CONT.md; external REC(e) source follow-through remains outside this edit |
| Larger-family paragraph, lines 513–517 | L-LABEL | Finite scalar/tensor-power analytic producer supplied by REC_CONT.md; arbitrary D still requires its separate dictionary and proof |

## Consumers

[R-fix 2026-10-29 REC-4] **Growth and mass-gap reuse conditions retained
(binding review item 4); producer residues R-SRC and R-MG remain OPEN.**
The s=11, β=p+3 assertion requires Z=1 and the uniform unconditional
input (16.1) with b_0=p+2. If that exponent is obtained by the cumulant
route, the all-order outer-cumulant and conditional-singleton inputs
stated in §16, including (16.4), must actually be supplied; literal
SRC-κ conditional estimates alone do not supply them.

MG0 requires the same complete hierarchy and the identified full
Hamiltonian H_Wightman=H_OS. MG1–MG4 require actual dense-family decay
with a uniform positive physical rate, common limits, and a nonzero
excited sector, with the vacuum/density qualifications in L-GAP and
MASS_GAP_TARGET. No such producer or physical identification is added
here. R-SRC and R-MG in the Open residue table name these unfinished
obligations; the conditional reconstruction does not discharge them.

| Consumer | What this file supplies | What it does not discharge |
|---|---|---|
| OSLEAF55 REC(a)–(d) | Full re-derivation with correct m-insertion translation weight and adjoint formula | No sharp-time field or unconditional Minkowski field follows from these parts alone |
| OSLEAF55 REC(e) | Full downstream reconstruction given L-CONT, with boundary-value and local-gluing proofs; R-CONT now proved in REC_CONT.md | External REC(e) consumer source follow-through remains required |
| OSLEAF55 L3/GROW and reviewed s=11,β=p+3 | Quantified Z=1 unconditional growth implication in L-GROW | Singleton, all-order averaging, separated bounds and actual continuum hierarchy |
| ASSEMBLY55 N9 (REC) | Reviewed R-CONT proof in REC_CONT.md and the explicit downstream theorem | External N9 consumer status is unchanged by this R-CONT-only edit |
| ASSEMBLY55 §9 item 18 (EXT and REC) | Exact restricted-domain reconstruction interface; R-CONT supplied by REC_CONT.md | EXT's actual RG estimates and external consumer follow-through remain necessary |
| MASS_GAP_TARGET MG0 / Hamiltonian | Conditional equality H_Wightman=H_OS on the full reconstructed space | No unconditional complete Yang–Mills hierarchy or physical identification |
| MASS_GAP_TARGET MG1–MG4 | Reflected-correlation identity, dense-family spectral implication, invariant-mass equivalence | No decay producer, uniform physical rate, cutoff passage or nonzero excited state |
| HANDOFF full-proof bar | Honest dependency/status separation | No complete existence theorem, mass-gap proof or independent certification |

## Open residue

[R-fix 2026-10-29 REC-2, pass 2] **R-CONT: PROVEN for the stated finite
Cartesian tensor class.** [REC_CONT.md](REC_CONT.md) derives continuous
ordered kernels from E0′, removes smearing, constructs SEED with explicit
constants fixed by s,alpha,beta,r_max, and proves logarithmic entrance
depth for the continuation domains. Its factorial estimate therefore gives
the polynomial time bound; the spatial and boundary construction proves
exactly §6's L-CONT conclusion, with tensor matching (15.1).
The fresh [independent review](checks/reccont2_review.md) resolves both
binding obligations and ends VERDICT: LAND. This is same-family/fresh-context
source review, not an audit grade. Provenance and checks are recorded in
[REC_CONT_LOG.md](REC_CONT_LOG.md). No other residue or external consumer
status is promoted by this update.

| ID | Exact missing item | Scope / reopening evidence |
|---|---|---|
| R-CONT | Functions, matching and bound (6.1) from E0′–E3,(Re),S_0=1, with all spatial variables and mixed words | PROVEN in REC_CONT.md §§3–11; both binding obligations RESOLVED by checks/reccont2_review.md |
| R-TENSOR | For a representation beyond the explicit tensor-power class, provide and verify D_E,J,C,D_M and their reality/covariance relations; prove its version of R-CONT | No classification or “verbatim adaptation” is banked; tensor-power downstream implication only is proved |
| [R-fix 2026-10-29 REC-3] R-CONSUMERS | Apply binding review item 3 in the external OSLEAF55/ASSEMBLY55 consumers; retain insertion count, separated REC(d), imported/open REC(e)/N9, S_0, (Re), absent E4, proper-orthochronous scope and explicit tensor dictionaries | OPEN source-side follow-through: this task edits only REC_LIB.md and its log; the local qualifications below are retained, not a claim that those consumer files were repaired |
| R-SRC | Produce the uniform unconditional input of L-GROW, including conditional singletons and all-order averaging if that route is used | External to the abstract reconstruction theorem; the actual Yang–Mills E0′ producer remains open |
| R-MG | Establish dense-family exponential decay with one positive physical rate, common limits, unique vacuum and a nonzero excited sector in the intended complete field family | External physical estimates; L-GAP is only an implication |
| R-REVIEW | Independently check the new boundary, kernel, gluing and identification proofs | Author readback is not independent confirmation; no audit status is assigned |

## Binding fixes to OSLEAF55

[R-fix 2026-10-29 REC-3] **Consumer requirements retained; source repairs
remain OPEN (binding review item 3, residue R-CONSUMERS).** The existing
numbered instructions below remain binding. In particular, OSLEAF55's
translation estimate must retain the insertion count in
(1+m u²)^(k/2); REC(d) remains a separated Euclidean insertion construction.
REC(e) and ASSEMBLY55 N9 remain imported/open. Every restatement retains
S_0=1, (Re), the absence of an assumed E4/unique vacuum, and the proper
orthochronous Poincaré scope. General tensors require explicit reflection
and Wick dictionaries; the arbitrary-representation bridge remains
R-TENSOR, OPEN. These restrictions are preserved in this library.
OSLEAF55 and ASSEMBLY55 are outside the permitted edits and have not
been repaired here; recording their obligations does not complete them.

1. In REC(b)'s Peetre estimate replace `(1+u²)^(k/2)` by
   `(1+m u²)^(k/2)` for a test with m insertions. Keep the dependence
   during any continuation iteration involving unbounded degrees.
2. Retain S_0=1 and (Re) explicitly whenever REC is restated. State that
   E4/unique vacuum is absent; use L-VAC to prevent an accidental
   uniqueness claim under the name “all Wightman axioms”.
3. Keep REC(d) scoped to separated Euclidean insertion operators with
   the stated support gap. The term “time-zero structure” must not be
   read as existence of sharp time-zero operator-valued distributions.
4. Do not replace REC(e)'s imported/conditional status by PROVEN on the
   strength of this file. Its new library interface is R-CONT; the
   single-cut semigroup lemma does not prove the all-gap continuation.
5. Replace any momentum-component positivity argument by positive H
   plus Lorentz covariance (L-ID/SPEC). Components of P⃗ may have either sign.
6. Keep the s=11,β=p+3 route conditional on Z=1, unconditional (16.1),
   and the actual all-order/singleton premises needed for b_0=p+2. For
   general q_X use the stated larger s, or prove a better bound.
7. For finite families specify the sum norm, simultaneous label
   permutation, and mixed RP form. For tensors specify J and Wick
   conversion; use §15's explicit tensor class or prove the missing
   representation bridge. An arbitrary O(4) representation is not
   covered merely by multiplying estimates by m^n.
8. Any mass-gap claim must use the identified full H and a dense
   centered physical observable family. A gap on a proper e-sector
   cannot be promoted to the complete Yang–Mills spectrum without a
   proved sector/density identification. These fixes are recorded here;
   OSLEAF55 itself has not been edited.
9. Specify the proper orthochronous Poincaré group for the continuous
   unitary output. Extensions to disconnected transformations need their
   own unitary/antiunitary conventions; a unitary time reversal is not
   part of the positive-energy assertion proved here.
