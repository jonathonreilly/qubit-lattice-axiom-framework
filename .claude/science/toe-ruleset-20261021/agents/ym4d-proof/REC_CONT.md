# REC-CONT — quantitative continuation work, 2026-10-29

**Target status: PROVEN, with fresh independent source review: LAND.**
The proof derives continuous ordered kernels from the flat-test E0′ bound,
constructs the analytic seed with explicit hierarchy-wide constants, proves
quantitative exhaustion of the time domains, and applies the spatial tube
and boundary construction. The input is E0′–E3, reality and S_0=1, with the
specified finite Cartesian tensor dictionary. No physical existence or
mass-gap claim is made. Independent review is recorded in the lane log.

PROVEN denotes an author proof of precisely the printed statement, including
its hypotheses. ARGUED denotes an unfinished route. OPEN denotes a missing
implication. These words confer no independent-review or audit status.
The fresh review and its source identities are recorded in
[REC_CONT_LOG.md](REC_CONT_LOG.md).

## 1. Exact target and inputs

The following is the exact statement from [REC_LIB.md §6](REC_LIB.md),
including its current status and its qualification on output exponents:

> **Status: PROVEN from E0′–E3, (Re), S_0=1; see REC_CONT.md.** For each n and
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

### 3.1 RC-REAL — removing smearing with finite distribution order

**PROVEN from the stated inputs.** On every strictly time-ordered real
chart the distributions S_n, n≥2, have jointly continuous kernels. For
`g_i=t_(i+1)-t_i>0`, `δ=min g_i`, and spatial gaps ξ_i, put

    R=1+Σg_i+Σ|ξ_i|,   L_0=R+δ^(-1).

Uniformly in n and component words, one has

    |S_n(X)|≤D_0 K_0^n(n!)^(gamma_0) L_0^(t_0 n),
    D_0=max(1,alpha),  gamma_0=beta+24s+100,
    t_0=12s+36.                                       (3.2)

Here are explicit, deliberately generous constants. Define

    b_s=2s+10,  c_s=4s+15,
    K_1=2^(r_max+beta+7s+4) 10^s c_s^(2s) 5^(s+3)
                                                exp(4s+3),
    K_0=K_1 2^(8s+39)(8c_s)^(c_s)(48b_s)^(b_s)
                            128^(2s+c_s) exp(9s+40).   (3.3)

No unspecified degree-dependent constant enters this statement.

**Finite-order cutoff.** For any integer M≥1 let u_M be the uniform
probability density on `[-1/(8M),1/(8M)]`, and let η be any fixed smooth
nonnegative probability density supported in `[-1/8,1/8]`. Set

    c_M=1_[-3/4,3/4] * u_M^(*M) * η.

Then c_M is smooth, takes values in [0,1], equals one on [-1/2,1/2],
and is supported in [-1,1]. For q≤M, differentiate q distinct uniform
factors. Each derivative has total variation 8M, so

    ||c_M^(q)||_∞≤(8M)^q.                              (3.4)

No derivatives of η occur in this bound. Only the finitely many orders
specified below are used; an all-order analytic cutoff is not assumed.

**Local chart and directions.** Translate the reference configuration
so X_1=0. Define

    δ_0=min(1,δ),  ell=δ_0/128,  d=4n,
    m=(2s+4)n+2,  h=m+d+1,  M=m+h,
    ε=δ_0/(4R).                                       (3.5)

Let Q be the closed coordinate cube about X of half-side ell. All its
compact smooth tests are flat at the coincidence planes. Use the unit
directions e_0 and
`e_a=(e_0+ε e_a^sp)/sqrt(1+ε²)`, a=1,2,3. Their projections of each
adjacent reference gap are at least δ_0/2: the numerator is at least
`δ_0-εR=3δ_0/4`, and ε≤1/4. Let v_(j,a) translate the last n-j
points in direction e_a, for j=0,...,n-1.

**The cut estimate as a distribution estimate.** For every smooth φ
supported in Q, every j≥1, and every integer q≥0,

    |(D_(v_(j,a))^q S_n)(φ)|
      ≤A_n q!(4/δ_0)^q R^(2sn)ell^(-2sn)||φ||_(C^m),
    A_n=alpha ((2n)!)^(beta/2)2^(r_max n+sn+d)
                     10^(sn)n^(sn)(8M)^(2sn)(d+1)^(m/2)
      ≤alpha K_1^n(n!)^(beta+4s+3).                    (3.6)

The C^m norm here is the maximum of all derivatives of total order at
most m, without a weight. To prove the estimate, use the product cutoff
`b(Y)=Π_(ν=1)^d c_M((Y_ν-X_ν)/(2ell))`. It equals one on Q and
is supported in the cube of half-side 2ell. With the unnormalized Fourier
transform in this paragraph,

    φ(Y)=b(Y)(2π)^(-d)∫φhat(p)exp(ip·Y)dp.             (3.7)

Every integrand factorizes across cut j. Rotate the two block tests so
e_a becomes the time axis. Original-coordinate cutoffs are rotated with
the tests; no product support is presumed after rotation. Each point's
support displacement has Euclidean norm at most 4ell. Place the
reflection plane at `a_*=e_a·X_j+δ_0/8` and take semigroup parameter
`τ=δ_0/4`. The left block, after translation by -a_*, reflection and
reversal, has positive ordered times; the right block, translated by
`-a_*-τ`, does also. Their nearest support times are at least
`3δ_0/32`. Internal projected gaps remain positive. RC-CUT therefore
applies at z=τ, with derivative cost q!(4/δ_0)^q.

Every transformed point has Euclidean norm at most 3R. For a block of
r points the weight in its 2sr seminorm is bounded by
`(10n)^(sr)R^(2sr)`. A row of an orthogonal four-dimensional matrix has
ℓ¹ norm at most 2. Thus the chain rule, (3.4) and Leibniz's rule give
the block estimate

    ||F_p||_(2sr),1≤2^(r_max r)(10n)^(sr)R^(2sr)
                      (8M/ell)^(2sr)(1+|p_block|)^(2sr). (3.8)

The tensor factor is the induced component sum norm of the rotation;
reflection and reversal cost one. The two block estimates multiply.
Their factorials are bounded by `((2n)!)^(beta/2)`. To integrate them,
use the integer m/2 and

    |φhat(p)|≤(1+|p|²)^(-m/2)
                    (2ell)^d(d+1)^(m/2)||φ||_(C^m),
    (1+|p|)^(2sn)≤2^(sn)(1+|p|²)^(sn),
    m/2-sn=d/2+1,
    ∫(1+|p|²)^(-d/2-1)dp=vol(B_d)≤2^d.                (3.9)

The first inequality follows by expanding (1-Δ)^(m/2); its absolute
coefficient sum is (d+1)^(m/2). Dropping `(2ell)^d≤1` and
`(2π)^(-d)≤1` gives the displayed A_n. Also
`M≤c_s n`, `d+1≤5n`, and
`sn+2sn+m/2=(4s+2)n+1≤(4s+3)n`. Apply
`((2n)!)^(beta/2)≤2^(beta n)(n!)^beta` and `n^n≤e^n n!` to
obtain the final inequality in (3.6) with exactly (3.3).

For real small cut displacement, (3.7) gives the translated distribution.
The integrable block bound and RC-CUT justify differentiating its
holomorphic integral. Its q-th derivative is the distribution derivative
in (3.6); no higher test seminorm depending on q is introduced. For j=0,
common-translation invariance makes every positive-order derivative of
S_n zero. The q=0 estimate uses any genuine cut, so (3.6) is valid for
all directions needed below.

**Continuous representative by Fourier inversion.** Set
`χ(Y)=Π_ν c_M((Y_ν-X_ν)/ell)` and `T=χS_n`. This is a compactly
supported distribution on full R^d, since multiplication by χ takes
every test into the strictly ordered flat space. It agrees with S_n
near X. The product rule for distributions, followed by (3.6), gives

    |(v_(j,a)·p)^h That(p)|,
    |That(p)| ≤ B_n R^(2sn)ell^(-(2sn+m+h))(1+|p|)^m,
    B_n=A_n 2^(m+h)(2n)^h(8M)^(m+h)h!.                (3.10)

Both quantities on the left have the same bound. Indeed `||v||_1≤2n`
and

    ||(D_v^(h-q)χ)exp(-ip·Y)||_(C^m)
      ≤2^m(1+|p|)^m(2n)^(h-q)(8M/ell)^(m+h-q).

Only derivatives through m+h=M occur. In the sum over q, use q!≤h!,
the binomial sum 2^h, and `(4/δ_0)ell=1/32` to get (3.10).
The undifferentiated estimate follows from q=0 and the same enlarged
constant. Compact support permits the Fourier pairings; equivalently
insert a test equal to one near that support.

These directions span every real coordinate with the quantitative bound

    max_(0≤j<n,0≤a≤3)|v_(j,a)·p|≥ε|p|/(12sqrt(n)).     (3.11)

For a proof let z_j=Σ_(i>j)p_i and let A be the maximum on the left.
Then `|z_j^0|≤A` and `|z_j^a|≤3A/ε`, hence `|z_j|≤6A/ε`.
With z_n=0, `p_i=z_(i-1)-z_i` proves (3.11). The common-translation
directions j=0 are essential here, including for χS_n.

Combining (3.10),(3.11), separately for |p|≤1 and |p|≥1, gives

    |That(p)|≤B_n R^(2sn)ell^(-(2sn+m+h))
             (24sqrt(n)/ε)^h(1+|p|)^(-d-1).            (3.12)

Its integral is finite, since
`∫(1+|p|)^(-d-1)dp=vol(B_d)≤2^d`. Fourier inversion represents
T by a continuous function. This proves a continuous local representative
of S_n, and the representatives agree on overlaps as distributions,
hence pointwise. This is a direct removal of distribution smearing.

**Complete hierarchy budget.** Inserting ell and ε in (3.12) and
bounding the inverse-Fourier prefactor by one gives

    |S_n(X)|≤A_n 2^(m+2h+d)(2n)^h(8M)^M h!
        48^h n^(h/2)128^(2sn+M)
        R^(2sn+h)δ_0^(-(2sn+m+2h)).                   (3.13)

Here `m≤(2s+5)n`, `h≤b_s n`, and `M≤c_s n` for n≥2.
Beyond A_n, all powers of n in (3.13) are bounded by
`n^((2b_s+c_s+b_s/2)n)=n^((9s+40)n)`; use `h!≤(b_s n)^(b_s n)`.
Their conversion by `n^n≤e^n n!`, and the remaining displayed
numerical factors, are bounded by `(K_0/K_1)^n(n!)^(9s+40)`
with (3.3). The resulting factorial exponent is β+13s+43, no larger
than gamma_0. Finally R≤L_0, δ_0^(-1)≤L_0, and

    4sn+m+3h=(12s+28)n+11≤(12s+36)n.

This proves (3.2). Every derivative order used is linear in n; every
power of n is O(n) with coefficient fixed by s. This is where E0′,
rather than unrelated fixed-degree distribution bounds, supplies the
hierarchy-wide factorial and linear-power budget. Translation invariance
holds pointwise after continuity, and multiplication by C^(⊗n) preserves
the component bounds. RC-POINT now gives actual point-vector limits for
all mixed reflected kernels, with their original distributional values. ∎

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

### 4.1 RC-CROSS — starting with one complex time at a time

**PROVEN.** Fix a>0. Suppose, for each j=1,...,k, a continuous function
f_j is defined on `R^k+i(-a,a)e_j`, is holomorphic in its j-th variable,
and satisfies `|f_j|≤M`. Suppose all these functions restrict to the same
continuous f_0 on R^k. Then they have a unique joint holomorphic extension
to

    {u∈C^k: Σ_j |Im u_j|<a},                            (4.5)

with the same bound M. No open transverse neighborhood of the axes is
assumed. This is a bounded cross version of the preceding Fourier proof.

**Proof.** Multiply each f_j by `exp(-εΣu_i²)`, ε>0, obtaining g_j.
For every axial y the horizontal slice is in L²(R^k), with the common
bound `M exp(εa²)(π/(2ε))^(k/4)`. On a compact substrip, the
one-variable Cauchy estimate and the Gaussian give differentiation of
these slices as distributions. Their Fourier transforms satisfy

    ĝ_(te_j)(p)=exp(-tp_j) ĝ_0(p),   |t|<a.              (4.6)

To justify the equality, test on compact momentum supports and solve
`∂_t ĝ=-p_j ĝ`; the common initial slice fixes the integration constant.
No derivative in a transverse complex variable is used here.

The convex hull of the axial intervals is the open l¹ ball in (4.5).
For any finite convex representation of a point in this ball, apply
Hölder exactly as in (4.3), with the common ĝ_0. This gives the same L²
bound for its exponentially weighted transform. Summing at the vertices
of a small box around the point gives (4.4), hence absolutely convergent
holomorphic Fourier inversion. At every axial slice that inverse equals
g_j almost everywhere by L² uniqueness, and everywhere by continuity.
Multiplication by `exp(εΣu_i²)` therefore extends all f_j. The identity
theorem on the common real slice proves uniqueness and independence of ε.
Finally apply this existence construction to every `1/(f_j-c)`, |c|>M.
Their extensions obey `(F-c)H=1` by uniqueness from the real slice.
As in RC-TUBE, F cannot take any value of modulus greater than M. ∎

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

**PROVEN construction from SEED.** The following domain argument is stated
with its analytic input explicit. Sections 3.1 and 6.1 derive that input
from (1.2), RP and Euclidean covariance, with constants (3.3),(6.9).

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
form. This clause specifies the identification with the original reflected
positive form. Section 6.1 proves all these clauses from the continuous
kernel estimate (3.2); no ordinary same-half positivity is assumed.

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

### 6.1 Producing SEED from a quantitative continuous real kernel

**PROVEN implication.** Suppose the ordered real distributions have
continuous kernels satisfying, uniformly in component words and n≥2,

    |S_n(X)|≤D_0 K_0^n(n!)^(gamma_0)
       [1+Σg_i+(min g_i)^(-1)+Σ|ξ_i|]^(t_0 n),          (6.8)

where g_i>0 are their real time gaps, D_0,K_0≥1, gamma_0≥0 and
t_0 is a nonnegative integer. Then SEED holds with

    D=D_0,  gamma=gamma_0,  t=t_0,
    K=K_0 2^(gamma_0)4^(t_0).                          (6.9)

This implication requires no prior joint analyticity of S_n. Its real-kernel
input is precisely (3.2), with the explicit constants (3.3). Thus (6.9)
derives every SEED constant from s,alpha,beta,r_max.

**Proof.** RC-POINT applies to every reflected real kernel, giving
continuous Hilbert point vectors and all mixed inner-product identities.
For fixed b,ξ and each j, allow only u_j to be complex with
`|Im u_j|<π/2`; all other u_i are real. Make the cut and the spatial
placements described in §6, now using only real point vectors. Insert
`exp(-(b_j/2+exp(u_j))H)`. This bounded operator makes the resulting
matrix element holomorphic in u_j and jointly continuous in every real
parameter. Its equality to the real S_n kernel follows by taking the
Hilbert limits in the smeared cut identity. For tensors use the same
phases as in §6. Thus every axial function has the same real restriction.

In either reflected norm kernel the internal real gaps are duplicated,
the central gap is b_j/2, and the central spatial difference is zero.
Its bracket in (6.8) is bounded by

    2[L+Σ_(i≠j) exp(u_i)]≤4|P(exp(u);L)|.              (6.10)

Taking the two norm square roots therefore gives power t_0 n and
constant

    D_0 K_0^n 4^(t_0 n)
        [(2j)!(2(n-j))!]^(gamma_0/2)
      ≤D_0[K_0 4^(t_0)2^(gamma_0)]^n(n!)^(gamma_0).

The inequality uses the binomial bounds
`(2j)!(2(n-j))!≤(2n)!≤4^n(n!)²`. Divide the axial functions by the
holomorphic nonzero P^(t_0 n). RC-CROSS supplies a bounded joint
extension to `Σ|Im u_i|<π/2`, which contains U_(n,0). Multiplication
by P^(t_0 n) gives precisely (6.4).

For completeness the extension is continuous in ξ: on a compact set of
ξ the axial functions have a common bound and are pointwise continuous.
Gaussian damping makes their slices L²-continuous by dominated
convergence. Apply the Hölder argument to differences of two parameter
values and then use the box-vertex Fourier-inversion bound on a smaller
angular set. This gives local uniform convergence of the extensions.
Different baselines agree by the connected-overlap argument in §6,
which uses their common real restriction. All reflected identities on
that restriction are the original OS identities. ∎

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

For the actual hierarchy the constants in (7.1) are now (3.2),(3.3),(6.9).
In particular t=12s+36 and gamma=beta+24s+100 include the finite-order
cutoff, Fourier factorization and unsmearing costs. The linear exponent
survives each cut because its two square-root contributions add to tn;
the enlarged-degree factorial contributes only the exponential in nN in
(7.1). Section 8 controls that N-dependence explicitly.

## 8. RC-EXHAUST — a quantitative sparse-coordinate proof

**PROVEN geometry and its consequence under the established SEED.** The exact
domains (6.1) exhaust every product time half-plane with logarithmic
entrance depth. The controlling parameter is the number of nonzero
angular coordinates, including in higher-degree reflected configurations.

Normalize a=1 temporarily and write `K_(d,N)=closure(U_(d,N)/a)`.
An open convex set G containing zero satisfies `λ closure(G)⊂G` for
0≤λ<1: a ball about zero and an approximation to a closure point give
this inclusion by convexity. Consequently a reflected vector in K gives
an internal vector in `closure(V/a)`, by radial shrinking and passage
to the limit. Closed cut boxes with central coordinate in [-1,1] thus
belong to the next K. Each K is also solid: coordinatewise reduction of
absolute values follows by averaging independent sign changes.

Set

    r_(0,N)=1,  r_(h,0)=0 (h≥1),
    r_(h,N+1)=(r_(h,N)+r_(h-1,N))/2.                   (8.3)

These radii lie in [0,1] and decrease with h. For every ambient degree
d≥2, K_(d,N) contains the cube of radius r_(h,N) on **any support of
at most 2h coordinates**, with zero in all other coordinates.

**Proof by simultaneous induction on N for every d,h.** At N=0 only
zero is required when h≥1; for h=0 the support is empty. At the next
stage, a support of size at most 2h-2 already has radius
`r_(h-1,N)≥r_(h,N+1)`. For size 2h-1 cut at its middle active
coordinate. Each reflected side has 2h-2 active coordinates, so both
sides have radius r_(h-1,N), while the central coordinate reaches 1
in the closure. Solidity gives the required smaller cube.

For size 2h let the active positions be p_1<...<p_(2h). Cut at p_h,
using radius r_(h-1,N) on the left and r_(h,N) on the right, with
central coordinate 1. The reflected supports have sizes 2h-2 and 2h.
Cut also at p_(h+1), interchanging the side radii. In the average of
these two points, every active coordinate other than the middle two
equals r_(h,N+1); the middle two equal `(1+r_(h,N))/2`, which is
at least that radius. Solidity finishes the induction. Positions of
inactive coordinates and the ambient reflected degrees never enter. ∎

Pascal's identity solves (8.3): with binomial coefficients zero for j>N,

    1-r_(h,N)=2^(-N) Σ_(j=0)^(h-1) binom(N,j)
             ≤2^(h-1)(3/4)^N.                          (8.4)

For the inequality use `1≤2^(h-1)2^(-j)` for j<h, enlarge the sum to
j=0,...,N, and apply the binomial theorem. Put
`h=ceil((n-1)/2)` and `ell_0=log(4/3)`. For 0<ε≤1 choose

    N_ε=ceil([h log 2+log(1/ε)]/ell_0).                (8.5)

Then the closure of U_(n,N_ε) contains the full cube of radius
`a(1-ε/2)`. Radial shrinking puts the cube of radius `a(1-ε)` in
the **open** U_(n,N_ε); ε=1 uses membership of zero. This proves
coverage with a rate, not merely coverage of closures.

Now let `δ=min Re ζ_j>0`, `b_j=Re ζ_j/2`, `w_j=ζ_j-b_j`, and

    R=1+Σ|ζ_j|+Σ|ξ_j|+δ^(-1).

Writing θ_j=arg w_j, one has
`sin(a-|θ_j|)=Re w_j/|w_j|≥δ/(2R)`. Since sin v≤v for v≥0,
`(a-|θ_j|)/a≥δ/(πR)`. Equation (8.5) with ε=δ/(πR) therefore
gives `arg w∈U_(n,N)` with

    N≤c_0(n)+c_1 log(R/δ),
    c_0(n)=1+[h log 2+log π]/ell_0,  c_1=1/ell_0.      (8.1)

These constants are finite and nonnegative. With `Q=16^t 2^gamma`,
the proved finite-stage estimates (6.3),(7.1) consequently give

    |F_n(ζ,ξ)|≤B_n R^(p_n),
    B_n=D K^n n^(gamma n)(3n)^(tn)Q^(n c_0(n)),
    p_n=tn+2n log Q/ell_0.                             (8.2)

Indeed `L+Σ|w_j|≤3R`, `|P|≤3nR`, and `R/δ≤R²`. For
ζ=τ-it, k=n-1, Euclidean norms give

    R≤sqrt(2k)(1+|(t,ξ)|+|τ|)(1+δ^(-1)).                (8.6)

Thus (9.1) holds with `p=p_n≥0`, `C=B_n(2k)^(p_n/2)`, under SEED.
Overlaps patch by §6. Each compact subset enters some finite stage
uniformly, so the union is jointly holomorphic and continuous in ξ.

There is no summation of the growing numbers A_(n,N). The factorial
budget (7.1), whose powers rely on the linear seed exponent, gives
`Q^(nN)`; the entrance rate converts that factor into a fixed polynomial
in R at each n. This is the explicit growth control required by this
route. The prefactor B_n may grow as `Q^O(n²)`; the exact L-CONT target
allows n-dependent constants and imposes no output factorial bound.

## 9. RC-SPACE — from complex times to the full tube

**PROVEN conditional lemma, applied with §8.** Let k=n-1≥1. Suppose the time
continuation is given as functions `F_n(ζ,ξ)`, holomorphic in
all Re ζ_j>0, continuous in real spatial gaps, matching the phase-converted
Schwinger functions, and obeying, for fixed finite C and p≥0,

    |F_n(τ-it,ξ)|≤C(1+|(t,ξ)|+|τ|)^p
                         (1+(min τ_j)^(-1))^p.          (9.1)

Assume the original Euclidean covariance with the stated tensor dictionary.
Then it determines a tempered distribution W in all 4k relative real
coordinates, a Fourier transform supported in `(closed V_+)^k`, and a
holomorphic continuation to the full forward tube. In particular spatial
complexification need not be obtained by a further unproved envelope
theorem. The hypotheses of this lemma are now supplied by §§3–8, with
`p=p_n` from (8.2) and `C=B_n(2k)^(p_n/2)` from (8.6).

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

**PROVEN bookkeeping, with the analytic producer in §§3–8.** All actual
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
No direction-independent exponent 1 is used. The real-rotation factor
already enters K_1 in (3.3); the seed construction keeps the component
sum norm and incurs no additional field-count factor.

## 11. Exact L-CONT conclusion and statement match

**PROVEN author theorem.** For every n≥2 set k=n-1 and take p_n and the
constant `C=B_n(2k)^(p_n/2)` from §8. Equations (3.2),(6.9) give the
actual seed, §8 gives (9.1), and §9 therefore applies to the original
hierarchy. With `q=ceil(p_n)`, `d=4k`, `M=2q+d+3` and
`L_mu=M+d+1`, its output constants can be chosen as

    A_n=B_n^(target)=L_mu,
    C_n=2^(L_mu) C_tube,

where C_tube is the explicit constant (9.9), with (9.2) and §9.3's
Fourier and fixed-bump constants. The B_n in (8.2) is a time-bound
prefactor, distinct from this target exponent. These constants are finite
and independent of the component word. They give exactly REC-LIB (6.1)
on every point of the full forward tube, including complex spatial gaps.

The functions are invariant under common complex translations, have the
tempered boundaries proved in §9, and match the original S_n on every
compact strictly ordered Euclidean test. Tensor matching is exactly
(1.1), not scalar invariance of individual tensor components. Section 2
gives 𝒲_0=1 and the constant n=1 function, with d_1=1; it also covers
alpha=0. No E4, unique vacuum, or physical-existence input has been added.

| Exact input or target clause | Proof | Disposition |
|---|---|---|
| E0′ on flat tests with one s,alpha,beta | (1.2), (3.5)–(3.13) | Used with the original weight and total derivative order |
| Point-kernel identification and removal of smearing | RC-REAL and RC-POINT | PROVEN for all ordered real charts and mixed reflected kernels |
| Hierarchy-wide seed constants | (3.2),(3.3),(6.9) | Explicit functions of the input triple and r_max |
| Joint time holomorphy, spatial continuity and overlap compatibility | RC-CROSS, §6.1, RC-STAGE | PROVEN for the actual kernels |
| Quantitative exhaustion | Sparse-coordinate induction (8.3)–(8.5), depth (8.1) | PROVEN with c_1=1/log(4/3) |
| Growth after continuation | (7.1),(8.2),(8.6) | PROVEN; no unjustified infinite-stage majorant is used |
| All complex spatial variables and exact bound (6.1) | §9.2–§9.3 and the constants above | PROVEN |
| Tempered boundary in every real variable | §9.1 and §9.3 | PROVEN, independently of approach inside the product cone |
| Common complex translation; n=0,1 | §§2,9.3 | PROVEN |
| Finite mixed Cartesian tensors and Wick matching (15.1) | (3.8), §§6,9,10 | PROVEN in the specified class |
| No general representation or spinor extension | §1 and §10 | Scope unchanged |

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

## Completion and remaining scope

The two analytic obligations in REVIEW_REC_CONT are discharged by the
printed author proofs: RC-SEED by §§3.1,4.1,6.1 and RC-EXHAUST by §8.
Their composition through §9 proves RC-TARGET with the exact clauses
checked in §11. The fresh hostile review in
[checks/reccont2_review.md](checks/reccont2_review.md) resolves both binding
obligations and ends VERDICT: LAND. It is same-family/fresh-context source
review; it confers no audit grade. Provenance is in REC_CONT_LOG.md.

REC_LIB's R-CONT status is updated following that review.
No source-side consumer, axiom, audit or ledger is edited. This abstract
reconstruction result does not supply an actual Yang–Mills hierarchy,
unconditional constructive estimates, a spectral gap, or an extension
beyond the stated finite Cartesian tensor class. OSLEAF55 and ASSEMBLY55
consumer texts are outside the permitted edit scope.
