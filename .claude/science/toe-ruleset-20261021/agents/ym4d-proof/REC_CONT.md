# REC-CONT — quantitative continuation work, 2026-10-29

**Target status: OPEN. This is a partial proof, not the requested completed
E0′ ⇒ L-CONT theorem.** The new results below are a bounded tube-extension
lemma, a local positive-kernel lifting lemma, a conditional finite-stage
continuation with an explicit factorial majorant, and a conditional passage
from polynomially bounded time continuation to the full forward tube.
Production of the analytic seed from E0′ and quantitative exhaustion remain
unproved. In particular, the auxiliary constants `D,K,gamma,t` below have
**not** been derived from OSLEAF55's `alpha,beta,s`.

PROVEN denotes an author proof of precisely the printed statement, including
its hypotheses. ARGUED denotes an unfinished route. OPEN denotes a missing
implication. These words confer no independent-review or audit status.
The fresh review and its source identities are recorded in
[REC_CONT_LOG.md](REC_CONT_LOG.md).

## 1. Exact target and inputs

The following is the exact statement from [REC_LIB.md §6](REC_LIB.md),
including its status and its qualification on output exponents:

> **Status: OPEN from E0′–E3. Statement to be proved.** For each n and
> ordered label word a, there are holomorphic functions 𝒲_n^a on
>
>     𝒯_n={z∈C^(4n): Im(z_(j+1)−z_j)∈V_+, 1≤j<n},
>
> with 𝒲_0=1. Their restrictions to the Wick slice j(x_1),...,j(x_n)
> agree as distributions with S_n^a on compact tests with t_1<...<t_n.
> For n=1 the function is constant. The functions are invariant under common
> complex translations and have, for some finite C_n,A_n,B_n independent of
> z and of the label word, the bound
>
>     |𝒲_n^a(x+iy)| ≤ C_n(1+|x|+|y|)^B_n (1+d_n(y)^−1)^A_n,
>     d_n(y)=min_(j<n){(y_(j+1)−y_j)^0−|(y_(j+1)−y_j)⃗|}.   (6.1)
>
> The common-translation condition also follows from the matching and E1
> by differentiating and analytic uniqueness. It is written here to remove
> any ambiguity about center-of-mass variables. For n=1 set d_1=1.
> Constants may depend on n; the theorem below does not require a claimed
> linear bound on the output exponents. The input E0′, however, has one s,
> α,β for every n, exactly as in §1.3.

For tensors its matching clause is replaced, exactly as in REC-LIB (15.1), by

    𝒲_n(jx_1,...,jx_n)=C^(⊗n) S_n(x_1,...,x_n).             (1.1)

Here `j(t,r)=(it,r)`. There are finitely many real bosonic Cartesian tensor
fields, of ranks at most `r_max`, in a direct sum of full tensor powers of
R^4. Put `B=diag(i,1,1,1)`, `C=⊕ B^⊗r`, and
`J=⊕ diag(-1,1,1,1)^⊗r`. Reflection includes J, and mixed-word reflection
positivity is required. Abstract unspecified representations and spinors
are outside this target. Scalars are the rank-zero case.

The E0′ input, on precisely `E_n=^0𝒮(R^(4n))`, is

    |S_n(F)| ≤ alpha (n!)^beta ||F||_(sn),1,   n≥1,           (1.2)
    ||F||_(k),1 = Σ_a max_(|γ|≤k)
                    sup_X (1+|X|²)^(k/2)|∂^γ F^a(X)|.

For one component this is OSLEAF55 D1 and §1.3 verbatim in mathematical
content. `s∈N`, `alpha,beta≥0` are a single triple for the entire hierarchy.
The flat space consists of Schwartz tests whose every jet vanishes on every
pair-coincidence plane. It is not the full Schwartz space. E1, E2, E3,
ordinary component reality, and S_0=1 are retained. E4 is not assumed.

The mathematical background is Hilbert-space spectral theory, distribution
and Fourier calculus, elementary integration, and Cauchy's formula and the
identity theorem. No OS reconstruction, tube theorem, edge-of-the-wedge
theorem, or spectral inversion theorem is imported. In particular, the
bounded tube lemma used below is proved here.

## 2. RC-CUT — the actual starting estimate

**PROVEN.** Let r,q≥1, `F∈E_(+,r)`, `G∈E_(+,q)`, and let H be the
nonnegative OS Hamiltonian. Then, for Re z≥δ>0 and integer h≥0,

    |∂_z^h ⟨[F],e^(-zH)[G]⟩|
      ≤ h! δ^(-h) alpha ((2r)!(2q)!)^(beta/2)
                       ||F||_(2sr),1 ||G||_(2sq),1.         (2.1)

The zeroth-derivative bound holds for Re z≥0. If one vector is Ω, replace
its norm bound by 1. For an r-insertion common time translation,

    ||T_u F||_(k),1
      ≤ 2^(k/2)(1+r u²)^(k/2)||F||_(k),1.                  (2.2)

**Proof.** The reflected product is flat: its two blocks have negative and
positive strictly ordered times, respectively, and flatness at the bounding
planes handles their boundaries. J and word reversal are isometries of
the component sum norm. From
`1+|X|²+|Y|²≤(1+|X|²)(1+|Y|²)` one gets

    ||[F]||²=S_(2r)(ΘF*⊗F)
          ≤alpha ((2r)!)^beta ||F||_(2sr),1².              (2.3)

For completeness, positive time translation is a contraction, rather than
merely a formal operation on equivalence classes. If
`a(u)=B(T_uF,T_uF)^(1/2)`, reflection and Cauchy–Schwarz give
`a(u)²≤a(0)a(2u)`. The E0′ estimate and (2.2) bound a(u) by a polynomial
for this finite vector. Iterating the inequality and taking 2^(-j)-th
powers yields `a(u)≤a(0)`. Null vectors descend. Reflection makes the
resulting contraction self-adjoint; translation continuity makes the
semigroup strongly continuous. Its spectral generator is H≥0.

Spectral integration gives
`||H^h e^(-zH)||≤sup_(λ≥0) λ^h e^(-δλ)≤h!δ^(-h)`.
Taylor expansion on smaller right half-planes proves holomorphy, and
Cauchy–Schwarz with (2.3) gives (2.1). Finally a common displacement in
R^(4r) has length √r|u|. The inequality
`1+|X+(ue_0)^r|²≤2(1+r u²)(1+|X|²)` proves (2.2). ∎

This proves a cut with smeared vectors. It does not put an unbounded field
insertion into a complex-time product. The first step recalled in the
author brief is stronger than the actual L-TIME statement in REC-LIB §5.

**PROVEN edge cases.** If alpha=0, all S_n with n≥1 vanish, so
`𝒲_0=1`, `𝒲_n=0` solve the whole target. For n=1, translation invariance
on E_1=𝒮 implies `S_1(F)=c∫F`, componentwise, so the target function is
constant (C times c for tensors). To see the distribution assertion,
translation invariance implies all first derivatives vanish. A compact
test with zero integral is a sum of first derivatives of compact tests,
by successive one-dimensional integration after subtracting products of
fixed integral-one bumps. The distribution therefore depends only on the
integral; density extends the conclusion to Schwartz tests. E0′ bounds
`|c|≤alpha||χ||_s` for any integral-one Schwartz χ.

## 3. RC-POINT — what removing a mollifier requires

**PROVEN estimate, not an unsmearing theorem.** Fix an integral-one
`ρ_r∈C_c^∞(R^(4r))` supported in the unit ball and write
`D_(r,k)=max_(|γ|≤k)||∂^γρ_r||_∞`. For an ordered positive configuration X
and ε≤1 small enough that the ε-ball about X is strictly ordered, set
`F_(X,ε)(Y)=ε^(-4r)ρ_r((Y-X)/ε)` in a single component. Then

    ||[F_(X,ε)]||
      ≤sqrt(alpha) ((2r)!)^(beta/2) D_(r,2sr)
        ε^(-(4+2s)r) [1+(|X|+ε)²]^(sr).                 (3.1)

**Proof.** A derivative of order k costs ε^(-4r-k); on its support
`|Y|≤|X|+ε`. Insert the resulting seminorm bound in (2.3). ∎

The divergent upper bound (3.1) supplies no Cauchy estimate as ε↓0. It
does not prove that the point vectors fail to exist. In particular,
substituting delta functions into (2.1) is not a valid proof of a
pointwise seed or of its all-order constants.

**PROVEN conditional point-vector lemma.** If, instead, the reflected
two-block kernel of the distributions is a jointly continuous function on
a neighborhood of two positive ordered configurations, their mollified
OS vectors have limits in the Hilbert space. Their inner products are the
values of that kernel. If the kernel is analytic in the time variables,
the resulting vectors have the corresponding real-time derivatives.

**Proof.** The squared norm of the difference of two mollified vectors is
the sum of four smeared kernel values with coefficients `1,1,-1,-1`.
Continuity makes the limit zero. The same computation fixes all mixed
inner products and independence of mollifier. For a derivative, use finite
differences of the vectors; their mixed inner products are finite
differences of the kernel. Existence and convergence of the corresponding
mixed derivatives make these vectors Cauchy. Repeating proves every finite
derivative. No delta function is treated as a flat Schwartz test. ∎

## 4. RC-TUBE — bounded tube convexification, rebuilt

**PROVEN.** Let U be a bounded connected open subset of R^d, and let f be
holomorphic on `T_U=R^d+iU`, with `|f|≤M`. There is a unique holomorphic
extension to `T_conv(U)`, still bounded by M. This is the bounded version
of the tube principle associated with Bochner. It is sufficient for the
normalized finite-stage functions below; no unbounded version is used.

**Proof of existence.** Choose ε>0 and put
`g(z)=f(z)exp(-εΣ z_j²)`. If `|y|≤R_U` on U, its horizontal slices obey

    ||g(·+iy)||_2 ≤ L_ε,
    L_ε=M exp(εR_U²)(π/(2ε))^(d/4).                     (4.1)

Use the unitary Fourier transform in the real coordinates. The
Cauchy–Riemann equations imply, first against compact momentum tests,

    ĝ_y(p)=exp(-p·(y-y_0)) ĝ_(y_0)(p).                   (4.2)

Indeed the derivative of `exp(p·y)ĝ_y` is zero. Local differentiation is
justified by Cauchy estimates on smaller tubes and the Gaussian bound;
connectedness then gives (4.2) along polygonal paths in U. The compact-test
identities agree with the L² functions wherever these are defined.

For `y=Σ λ_i y_i`, `y_i∈U`, `λ_i≥0`, `Σλ_i=1`, Hölder's inequality gives

    ∫|ĝ_(y_0)(p)|² exp(-2p·(y-y_0))dp
      ≤ Π_i ||g(·+iy_i)||_2^(2λ_i) ≤ L_ε².             (4.3)

Each y in the convex hull has such a finite representation. On a small
closed box `y+[-r,r]^d⊂conv(U)`, sum (4.3) over its 2^d vertices to get

    ∫|ĝ_(y_0)|² exp(-2p·(y-y_0)) exp(2r||p||_1)dp
       ≤ 2^d L_ε².                                    (4.4)

Fourier inversion is consequently absolutely convergent at y, with bound
`(2π)^(-d/2) 2^(d/2)r^(-d/2)L_ε`; the same estimate on smaller boxes
permits all complex derivatives. It defines a holomorphic extension G of
g, since Fourier inversion agrees on the original tube. Then
`F(z)=G(z)exp(εΣz_j²)` extends f. Convexity gives connectedness and the
identity theorem gives uniqueness, including independence of ε.

**Proof of the bound.** For every complex c with |c|>M, the function
`1/(f-c)` is bounded and holomorphic on T_U. Apply the existence argument
to it, obtaining H on the convex tube. The identity `(F-c)H=1` holds
on the initial tube, hence everywhere. Thus F takes none of the values
with modulus greater than M, proving `|F|≤M`. ∎

If P is nonvanishing and holomorphic on the entire convex tube and
`|f|≤A|P|^v`, with integer v≥0, apply the lemma to `f/P^v` and multiply
back. The majorant P must actually be supplied; a pointwise weight with
absolute values cannot simply be called holomorphic.

## 5. RC-LIFT — Hilbert vectors from a local analytic kernel

**PROVEN conditional lemma.** Suppose real-parameter Hilbert vectors
v(u), `u∈R^k`, have a kernel that extends antiholomorphically in its first
argument and holomorphically in its second. At a real center c suppose
this kernel is bounded by M on the product of two complex polydiscs with
radii `R_1,...,R_k`. Then v extends to that polydisc, with coefficients

    ||∂^γv(c)/γ!|| ≤sqrt(M) Π_i R_i^(-γ_i).              (5.1)

For `|z_i-c_i|≤q_i R_i`, `0≤q_i<1`, its series is absolutely convergent
and its norm is at most `sqrt(M)Π_i(1-q_i)^(-1)`.

**Proof.** Difference quotients, as in RC-POINT, give the derivative
vectors and their Gram matrix by differentiating the two kernel slots.
Cauchy's formula bounds the `(γ,γ)` coefficient by
`MΠR_i^(-2γ_i)`. Taking its nonnegative square root proves (5.1).
The product of geometric series proves absolute convergence. Polarization
and absolutely convergent double series identify the continued inner
products with the continued kernel. ∎

For later use let an angular domain be open, convex, and invariant under
independent sign changes of its coordinates. If it contains a point a,
it contains the box `|b_i|≤|a_i|`: write b as a convex combination of
the sign changes of a. Openness allows slightly larger radii. Therefore
a reflected diagonal angular point supplies the real-centered product
polydiscs needed in RC-LIFT, in logarithmic coordinates. Such polydiscs
patch uniquely: intersections of polydiscs centered on the real locus,
when nonempty, contain a real open product set. Scalar pairings and the
identity theorem identify the vectors on the intersection. This argument
uses local product neighborhoods, not an inference from mere positivity
of a number called a continued norm.

## 6. RC-STAGE — a precisely conditional domain construction

**PROVEN conditional construction.** The seed hypothesis in this section
is an additional analytic input, presently OPEN from (1.2).

Use n fields and k=n-1 relative gaps. Let `a=π/2`. For n≥2 define

    U_(n,0)=(-a/(2k),a/(2k))^k,
    V_(r,N)={θ∈R^(r-1): (-reverse θ,0,θ)∈U_(2r,N)},
    U_(n,N+1)=conv[U_(n,N) ∪ ⋃_(j=1)^(n-1)
                 {(-reverse V_(j,N))×(-a,a)×V_(n-j,N)}]. (6.1)

`V_(1,N)` is the single point of R^0. All domains here are nonempty,
open in their stated dimensions, convex, invariant under independent
coordinate sign changes and reversal, and contained in `(-a,a)^k`.
These properties follow inductively from the formulas. They are nested:
the explicit old-domain term ensures this. The construction has genuine
open initial domains; RC-TUBE is not applied to a union of real axes.

For positive real baselines `b=(b_1,...,b_k)`, real spatial differences
`ξ=(ξ_1,...,ξ_k)`, and `w_j=exp(u_j)`, put

    δ_b=min b_j,
    L=1+Σb_j+δ_b^(-1)+Σ|ξ_j|,
    P(w;L)=(sqrt(L)+Σ sqrt(w_j))².                      (6.2)

The square roots have positive real part on Re w_j>0. In this domain P
has no zero, and

    (sqrt(L)+Σsqrt(|w_j|))²/2 ≤ |P(w;L)|
                                  ≤(sqrt(L)+Σsqrt(|w_j|))²,
    L+Σ|w_j| ≤2|P(w;L)| ≤2n(L+Σ|w_j|).                 (6.3)

For the first inequality each square root has real part at least its
modulus divided by √2. The last upper bound is Cauchy–Schwarz on n terms.

**Seed hypothesis SEED.** There are fixed `D,K≥1`, `gamma≥0`, integer
`t≥0`, and compatible functions F_n for every mixed word, every b, and
every real ξ, holomorphic for `Im u∈U_(n,0)` in
`ζ=b+exp(u)`, continuous locally in ξ, matching the phase-converted
restricted Schwinger distributions, and satisfying

    |F_n(b+w,ξ)| ≤ D K^n(n!)^gamma |P(w;L)|^(tn).        (6.4)

Compatibility includes different baselines on their overlaps. The
real Euclidean reflected kernels are those of the original mixed OS
form. This last clause is an identification, not ordinary same-half
Euclidean positivity. SEED does not follow here from “tempered and real
analytic”; both its analyticity and its quantitative estimate are missing.

Under SEED, F_n extends to all the domains

    𝒞_(n,N)(b)={ζ=b+exp(u): Im u∈U_(n,N)},              (6.5)

and has, uniformly in words, baselines, and real ξ, the bound

    |F_n(b+w,ξ)|≤A_(n,N)|P(w;L)|^(tn),
    A_(n,0)=D K^n(n!)^gamma,
    A_(n,N+1)=max{A_(n,N),
               16^(tn) max_(1≤j<n) sqrt(A_(2j,N)A_(2(n-j),N))}.
                                                               (6.6)

**Proof.** On real positive gaps, continuity of the seed reflected
kernels and RP produce the point vectors by RC-POINT. Their analyticity
and their extensions with internal angular parameters in V_(r,N) follow
from RC-LIFT: the reflected kernel is F_(2r) with internal gaps
`reverse(bar ζ), central positive gap, ζ`. Real-centered logarithmic
polydiscs lie inside U_(2r,N) by its unconditional convexity.

For cut j, put the nearest-time insertion of each point vector at distance
`b_j/4` from the reflection plane. Choose each block's spatial positions
to reproduce its original internal differences, and place their adjacent
endpoints apart by the original spatial gap ξ_j. Independent spatial
translations of the blocks accomplish this without changing their norms;
in each individual reflected norm the central spatial gap is zero.
Insert the bounded operator
`exp(-(b_j/2+w_j)H)` between them. Its norm is at most one. The resulting
matrix element is jointly holomorphic on the j-th cut domain in (6.1);
the reflected left vector is evaluated antiholomorphically so that the
whole expression is holomorphic in the original left gaps. It agrees
with the real ordered Schwinger kernel by translation and the cut identity.

In each squared norm the internal gaps are duplicated and the central
gap is `b_j/2`. Represent that central gap as a new baseline `b_j/4` plus
the positive variable `w'_central=b_j/4`. All other baselines are copied
from the pertinent block. Spatial internal gaps are copied with possible
sign changes, and the central spatial gap is zero. Common translations
drop out. Thus

    L'≤4L,
    Σsqrt(|w'_i|)≤2Σsqrt(|w_i|)+sqrt(b_j)/2,
    |P(w';L')|≤(5/2)²(sqrt(L)+Σsqrt(|w_i|))²
              ≤(25/2)|P(w;L)|≤16|P(w;L)|.              (6.7)

Cauchy–Schwarz now gives the cut bound in (6.6). The power is
`(2jt)/2+(2(n-j)t)/2=nt`; it does not double. This is the precise place
where a *linear seed exponent* is used.

The cut functions and the old function agree on overlaps. Their angular
intersections are convex and contain zero; on the positive real slice
they all have the prescribed value. The identity theorem applies in
logarithmic variables. Divide the glued function by P^(tn). It is
bounded by the right side of (6.6) on the connected union of angular
domains. RC-TUBE extends it, with the same bound, to their convex hull.
Multiplying back proves the induction.

Continuity in ξ follows locally by the same constructions: initial Gram
kernels give continuous vectors; locally uniform Cauchy estimates give
continuous sums; Gaussian Fourier inversion in RC-TUBE is locally
dominated. Different baselines patch as well. In an intersection, replace
`ζ` by `Re ζ+iλ Im ζ`, `0≤λ≤1`. Each angle of `ζ-b` decreases in modulus,
so unconditional convexity keeps this path in both domains. Their common
real part is the connected positive orthant `Re ζ>max(b,b')`. Hence the
intersection is connected and contains a real open set, where both
constructions have the original value. Analytic uniqueness identifies
them on the whole intersection. The same argument permits comparison of
different finite stages. ∎

For tensors, phase each real point vector by the product of its component
entries of C. The identity `bar C J=C` gives precisely the kernel of
(1.1). Since every phase and every reflection entry has modulus one,
(2.3), (5.1), (6.6), and (6.7) retain their constants. No label count is
summed in these bounds; with the sum norm, finite mixed words share the
same estimates. A maximum-component test norm would introduce the separate
factor `m^n`, where m is the total number of components.

## 7. RC-FACTORIAL — solving the finite-stage constant recurrence

**PROVEN under SEED.** A majorant for (6.6), for n≥2 and N≥0, is

    A_(n,N) ≤ D K^n 16^(tnN) [((2^N n)!)]^(gamma/2^N)
            ≤ D K^n n^(gamma n) (16^t 2^gamma)^(nN).    (7.1)

**Proof.** The claim at N=0 is equality. At a cut, the two factorial
arguments are `2^(N+1)j` and `2^(N+1)(n-j)`. Their factorial product is
at most `(2^(N+1)n)!`, since the corresponding binomial coefficient is
an integer at least one. The square root changes the exponent from
`gamma/2^N` to `gamma/2^(N+1)`. The powers of D and K remain D and K^n;
the powers of 16 add to `tn(N+1)`. The old-domain term also fits this
majorant, using `((2m)!)^(1/2)≥m!`. Finally use `r!≤r^r`. ∎

For raw E0′ the analogous elementary budget is, explicitly,

    [max(1,alpha) ((2^N n)!)^beta]^(1/2^N)
      ≤max(1,alpha)^(1/2^N) n^(beta n)2^(beta nN),
    s(2^N n)/2^N=sn.                                  (7.2)

Equation (7.2) is arithmetic, not an analytic-continuation proof. To use
(7.1) for the actual hierarchy requires the missing conversion from
`(s,alpha,beta)` to the constants in SEED. No choice `t=s`, `gamma=beta`,
or an unproved “harmless” mollifier constant is made here.

## 8. RC-EXHAUST — the unproved geometric/quantitative step

**OPEN.** It remains to prove, for the actual construction or a justified
replacement, that the time domains cover every point with Re ζ_j>0,
with an entrance-depth/bound estimate sufficient for a polynomial bound.
Even a proof of qualitative exhaustion alone would not control (7.1).

Here is one explicit sufficient estimate, not an established one. For
`δ=min Re ζ_j`, set `b_j=Re ζ_j/2`, `w_j=ζ_j-b_j`, and

    R=1+Σ|ζ_j|+Σ|ξ_j|+δ^(-1).

If there are finite nonnegative c_0(n),c_1(n) and the angular point
`arg w` belongs to U_(n,N) for some

    N≤c_0(n)+c_1(n)log(R/δ),                            (8.1)

then (6.3) and (7.1), with `Q=16^t2^gamma`, imply

    |F_n(ζ,ξ)|≤D K^n n^(gamma n)(3n)^(tn) Q^(nc_0(n))
                          R^[tn+2nc_1(n)log Q].         (8.2)

Indeed `L+Σ|w_j|≤3R`, `|P|≤3nR`, and `R/δ≤R²`.
The estimate (8.1), or another sufficient propagation argument, is not
proved. It is a proposed sufficient condition; there is no assertion that
the original OS construction must have this depth bound.

A tempting simplification is to retain only a common cube radius at every
degree. It loses information about reflected angular configurations,
whose central coordinate is zero. For cube radii r_(n,N), averaging the
cut boxes gives the valid new lower radius

    min_(1≤i<n) [a + Σ_(j<i) r_(2(n-j),N)
                         + Σ_(j>i) r_(2j,N)]/(n-1).     (8.3)

The minimum cannot silently be replaced by its endpoint term. For n=4
and seed radii `r_(m,0)=a/[2(m-1)]`, the endpoint term is `19a/45`,
whereas the middle term is `2a/5`. These exact fractions follow by
substitution in (8.3). This is a check on that simplification, not a
counterexample to reconstruction or to the full domains (6.1).

The finite domains, kernel lift, and factorial budget therefore do not
yet establish either a common continuation on the entire time half-plane
or its global bound. A successful proof must resolve both the seed and
this quantitative step.

## 9. RC-SPACE — a conditional route from complex times to the full tube

**PROVEN conditional lemma.** Let k=n-1≥1. Suppose the missing time
continuation has been supplied as functions `F_n(ζ,ξ)`, holomorphic in
all Re ζ_j>0, continuous in real spatial gaps, matching the phase-converted
Schwinger functions, and obeying, for fixed finite C,p,

    |F_n(τ-it,ξ)|≤C(1+|(t,ξ)|+|τ|)^p
                         (1+(min τ_j)^(-1))^p.          (9.1)

Assume the original Euclidean covariance with the stated tensor dictionary.
Then it determines a tempered distribution W in all 4k relative real
coordinates, a Fourier transform supported in `(closed V_+)^k`, and a
holomorphic continuation to the full forward tube. In particular spatial
complexification need not be obtained by a further unproved envelope
theorem. The constants C,p in this lemma are **supplied**, not established
from (1.2).

### 9.1 Boundary values in time, with the spatial variables retained

Write `d=4k`, `q=ceil(p)`, `ell=q+1`, `M=2q+d+3`, and

    I_d=∫_(R^d)(1+|x|)^(-d-1)dx
       =2π^(d/2)/(d Γ(d/2)),
    C_* = C (2+sqrt(k))^q 2^q 2^(M/2) I_d,
    C_W = C_* [Σ_(j=0)^(ell-1) k^j/j! + k^ell/(ell-1)!]. (9.2)

For a test φ∈𝒮(R^d), let T_τ(φ) be integration of the function in
(9.1) against φ. It is well defined. If |τ|≤1 and 0<s≤1, then
`min(τ_j+s)≥s` and `|τ+s(1,...,1)|≤1+sqrt(k)`. Therefore, for
`h(s)=T_(τ+s1)(φ)`, holomorphy and integration by parts give

    h^(j)(s)=(-i)^j T_(τ+s1)((Σ_(a=1)^k ∂_(t_a))^j φ),
    |h^(j)(s)|≤C_* k^j s^(-q)||φ||_M,   0≤j≤ell.       (9.3)

The integration by parts is justified first with a compact cutoff and
then by the polynomial bound and local Cauchy estimates. The factor
`2^(M/2)I_d` bounds the integral of the real-coordinate weight against
the Schwartz decay; M exceeds both every derivative order used and
`q+d+1`.

Taylor's formula backward from 1 is

    h(0)=Σ_(j=0)^(ell-1) (-1)^j h^(j)(1)/j!
        +(-1)^ell/(ell-1)!∫_0^1 s^(ell-1)h^(ell)(s)ds.

Since `ell-1-q=0`, (9.3) proves `|T_τ(φ)|≤C_W||φ||_M`, uniformly as
τ approaches any face of the positive orthant. Applying this bound to
the time derivatives of φ and integrating along the segment between
τ and τ' gives

    |T_τ(φ)-T_τ'(φ)|≤sqrt(k) C_W |τ-τ'| ||φ||_(M+1).

Thus W=lim_(τ→0)T_τ exists in 𝒮′, independently of approach, and has
seminorm bound C_W||φ||_M. All spatial coordinates were integrated in
these estimates; they were not discarded as fixed parameters.

### 9.2 Energy support and Lorentz covariance before spatial continuation

Take the unitary Fourier transform, with Minkowski pairing
`Σ(E_j t_j-p⃗_j·ξ_j)`, and write μ=Ŵ. The Cauchy–Riemann equations,
tested first on compact momentum supports, give

    T̂_τ=exp(-Στ_j E_j)μ.                               (9.4)

The equality follows by differentiating the exponentially compensated
distribution and taking the just-proved limit. Fix a momentum test ψ
supported where `E_j≤-ε<0`, and fix all other imaginary times positive.
Send τ_j to infinity. Equation (9.1) bounds T̂_τ by a fixed Schwartz
seminorm times a polynomial in τ_j. In the compensated pairing, every
derivative of `exp(τ_j E_j)ψ` decays exponentially times a polynomial.
Consequently that pairing vanishes. Varying ψ proves

    supp μ ⊂ {E_j≥0 for all j}.                         (9.5)

Euclidean covariance supplies its infinitesimal rotation identities on
real positive time gaps, as distribution identities in ξ. After Wick
conversion these are the boost identities. More explicitly, conjugation
by B sends a Euclidean time–space rotation generator to -i times the
corresponding Minkowski boost generator; on tensor slots the matrix
generator is conjugated by C in the same way. Test the identities in ξ.
Each side is holomorphic in ζ, including its distribution derivatives
and polynomial coordinate factors. Equality for positive real ζ extends
through the connected product half-plane by repeated one-variable
identity theorems. Taking the time boundary gives the boost identities
for W in all real coordinates.

These identities integrate without an unbounded-operator integration
theorem: along a real boost Λ(u), differentiate
`D_M(Λ(u))^(-⊗n) W(Λ(u)·)` as a distribution. Pullback of Schwartz tests
by a finite invertible linear map is differentiable, and the derivative
is the just-established zero Lie derivative. Hence this expression is
constant in u. Spatial rotations give the analogous statement. The
tensor matrix is invertible, so the support of μ is invariant under
common proper orthochronous Lorentz transformations.

If a momentum in this support had a component outside closed V_+,
(9.5) says that component has nonnegative energy but is spacelike.
A real boost along its spatial momentum would make its energy negative.
Support invariance would contradict (9.5). Thus

    supp μ ⊂ K=(closed V_+)^k.                          (9.6)

This reasoning does not assume positive spatial momentum components.

### 9.3 Fourier–Laplace construction and an explicit global tube bound

For clarity a usable seminorm bound for μ can be obtained directly.
Set `L_μ=M+d+1` and

    C_F=(2π)^(-d/2)(d+1)^M 2^M(M+1)^M 2^(L_μ/2) I_d,
    C_μ=C_W C_F.

Then `|μ(ψ)|≤C_μ||ψ||_(L_μ)`. To verify the Fourier constant, expand
`p^a∂_p^b φ̂` as the Fourier transform of
`∂_x^a(x^b φ)`, with |a|,|b|≤M. Leibniz coefficients sum to at most
2^M; differentiated monomial coefficients are at most (M+1)^M; expansion
of `(1+Σ|p_j|)^M` has coefficient sum (d+1)^M. The remaining integral
is bounded by `2^(L_μ/2)I_d||φ||_(L_μ)`. This proves the displayed bound.

Choose a fixed nonnegative smooth bump ρ on the unit ball of R^d with
integral one, and set

    χ=1_(K+B(0,2))*ρ,
    A_L=max(1,max_(|γ|≤L)||∂^γρ||_1).

Then χ=1 where dist(p,K)<1, χ=0 where dist(p,K)>3, and
`||∂^γχ||_∞≤A_L` for |γ|≤L. For η∈(V_+)^k put
`δ=min_j(η_j^0-|η⃗_j|)>0`, `ε=(1+|η|)^(-1)`, and
`χ_η(p)=χ(p/ε)`. Since K is a cone, this cutoff equals one near K.
For p in its support choose q∈K with |p-q|≤3ε. Then

    Σ η_j·p_j ≥ (δ/sqrt(2))|p|-6.                      (9.7)

Here `η_j·q_j≥δ q_j^0≥δ|q_j|/sqrt(2)`, and the error from p-q is at
most `3ε(|η|+δ/sqrt(2))≤6`. Thus

    𝒲_n(z)=(2π)^(-d/2) μ(χ_η(p)exp(iΣp_j·z_j)),
    z=x+iη,                                            (9.8)

is defined by a Schwartz test, and is independent of the chosen cutoff
equal to one near the support. To check holomorphy, fix a smaller
neighborhood of any η and use one fixed cutoff there. Exponential decay
on that neighborhood allows every complex derivative in the Schwartz
topology. Differences between cutoffs are annihilated by μ.

For `L=L_μ`, Leibniz's rule, (9.7), and

    sup_(r≥0)(1+r)^L exp(-δr/sqrt(2))
       ≤L!(1+sqrt(2)/δ)^L

give the fully explicit relative-coordinate bound

    |𝒲_n(x+iη)|≤C_tube(1+|x|+|η|)^L(1+δ^(-1))^L,
    C_tube=(2π)^(-d/2) C_μ A_L exp(6)
                                      2^L L!(1+sqrt(2))^L. (9.9)

The Leibniz derivative factor is bounded by
`A_L(ε^(-1)+|z|)^L≤A_L[2(1+|x|+|η|)]^L`.
This checks the polynomial dependence also for large |η|; a fixed-width
cone cutoff would instead have introduced an unwanted exponential in |η|.

At purely temporal η, (9.4) identifies (9.8) with the original time
continuation as distributions, hence as continuous functions. Its
Euclidean matching is therefore preserved. For arbitrary η→0 in the
product cone, use a fixed χ and multiply a Schwartz test by
`χ exp(-Ση_j·p_j)`. These products converge to χ times the test in
Schwartz topology: on supp χ the exponential and its derivatives are
uniformly bounded for |η|≤1; split a compact set from a Schwartz tail.
Since μ(χψ)=μ(ψ), the boundary is W, without a nontangential restriction.

Finally compose with the relative-coordinate map
`z↦(z_2-z_1,...,z_n-z_(n-1))`, whose Euclidean operator norm is at most
2. It gives common complex translation invariance and (6.1), with
`A_n=B_n=L`, and full-coordinate constant `2^L C_tube`. This proves
the conditional lemma. ∎

## 10. Tensor and finite-family accounting

**PROVEN bookkeeping, conditional on the analytic producer.** All actual
E0′ cut estimates use the input triple `(s,alpha,beta)` unchanged in the
sum norm. Every continuation estimate above is uniform in the finitely
many component words when SEED is. The phase identity used in RC-STAGE is
entrywise: if an index has h temporal slots, its C entry is i^h and its
J entry is (-1)^h, so `overline(i^h)(-1)^h=i^h`.

For a real Lorentz matrix Λ, `B^(-1)ΛB` preserves the complex Euclidean
quadratic form because `B^TB=-diag(1,-1,-1,-1)`. Thus

    C D_E(B^(-1)ΛB) C^(-1)=⊕ Λ^⊗r.

This verifies the covariance dictionary used in §9, without an arbitrary
representation claim. In the fixed Cartesian sum norm, a real rotation
costs at most `2^(r_max n)`. A unit-direction boost with complex rapidity
u costs at most

    exp(r_max n ||v||_1 |u|)≤exp(sqrt(3) r_max n |u|).

Indeed the vector generator `[[0,v^T],[v,0]]` has induced ℓ¹ norm
`||v||_1`, and the exponential series and tensor products give the bounds.
No incorrect direction-independent exponent 1 is used. These finite
matrix estimates do not produce the missing SEED functions or their
constants.

## 11. Statement match

| Exact input or target clause | Result here | Status for the requested implication |
|---|---|---|
| OSLEAF55 D1, weight and total derivative order | (1.2), (2.2), (3.1); no norm replacement with an unnamed n-dependent factor | Matched |
| Flat `^0𝒮` tests, partial products, S_0=1 | §§1–3; mollifiers stay strictly ordered; point vectors require a continuous kernel | Matched; no unrestricted Euclidean moment algebra assumed |
| One s,alpha,beta for every degree | (2.1), (2.3), (3.1), (7.2) | Explicit actual input; conversion to SEED remains OPEN |
| Mixed several-field RP and tensor reflection | §§1–3,6,10 | Matched with the exact Cartesian dictionary |
| Existence on the full forward tube for every word | Conditional finite stages §6; conditional full spatial tube §9 | OPEN from E0′ |
| Overlap compatibility | §6, including different baselines | PROVEN conditional on SEED, for constructed finite domains |
| Exhaustion of all time gaps | §8 | OPEN; no unproved domain theorem is cited as a solution |
| Holomorphy-envelope input | §4 | Bounded tube convexification rebuilt; no general envelope claim |
| Polynomial bound (6.1) | (6.6),(7.1) at finite stages; (8.2) conditional on (8.1); (9.9) conditional on (9.1) | OPEN from E0′ |
| Tempered boundary in every real variable | §9.1 and §9.3 | PROVEN given the time bound, with explicit seminorm constants |
| Common complex translation; n=0,1 | §§2,9.3 | Constant cases proved; general case conditional on producer |
| Wick matching (15.1) | §§1,6,9,10 | Preserved by every proved conditional step |
| No unique-vacuum or physical-existence assertion | No E4 or source/decay estimates introduced | Preserved |

## 12. Literature and scope

Credit for the reconstruction problem and continuation strategy belongs
to Osterwalder and Schrader; credit for the analyticity investigations
also belongs to Glaser. [OS II](https://doi.org/10.1007/BF01608978) and
[Glaser's paper](https://doi.org/10.1007/BF01645941) are attribution, not
load-bearing inputs. The accessible discussion in
[Kravchuk–Qiao–Rychkov §9.2](https://arxiv.org/html/2104.02090v2#S9.SS2)
helped locate the distinctions between analytic continuation, all-order
estimates, and spatial control. The estimates and proofs above must stand
on their printed arguments.

[Zinoviev's alternative](https://arxiv.org/html/hep-th/9408009v1) formulates
an additional weak spectral condition. This file neither assumes that
condition nor proves it from E0′. Balaban and Dimock are credited for the
broader constructive Yang–Mills program; no estimate from their work is
an input here. No claim of novelty for the established library mechanisms
is made. No numerical checks were run.

## Open residue

**R-CONT remains OPEN, already for one scalar.** This file does not fulfill
the author brief's request for a completed proof of E0′ ⇒ L-CONT.

| ID | Exact unfinished obligation | What would resolve it |
|---|---|---|
| RC-SEED | Produce the analytic functions and bound (6.4) from the actual flat-distribution E0′/RP/covariance hypotheses, with explicit `t,D,K,gamma` determined by `s,alpha,beta` and the finite tensor data | A proof of joint Euclidean/time analyticity and quantitative removal of smearing; (3.1) alone does not do this |
| RC-EXHAUST | Prove quantitative coverage of the time half-plane by (6.1), or replace it with a fully proved scheme giving a global polynomial bound | A valid domain exhaustion and estimate argument; (8.1) is one sufficient, unproved option |
| RC-TARGET | Supply (9.1) from those two missing steps, for all n and mixed words | Then §9 supplies the complex spatial variables and the exact L-CONT bound; presently this antecedent is missing |

These are dependent obligations in one reconstruction argument, not
independent physical obstructions or a no-go result. No finite-stage
lemma, successful mechanical check, review verdict on a conditional lemma,
or paper-access success closes them. REC-LIB remains conditional and
OSLEAF55 REC(e)/ASSEMBLY55 N9 are not promoted.
