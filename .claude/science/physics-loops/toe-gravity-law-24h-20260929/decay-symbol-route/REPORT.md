# Decaying kernels, the mixed TT identity, and controlled escapes

This is a new conditional discovery calculation, not an independent review of the preceding finite-support result and not a formal PASS. The extension has a real boundary: **absolute first moments justify the affine test, but do not by themselves imply the contradiction.** One also needs the TT kinetic symbol to be invertible on a dense set. The finite-Laurent implication from nonzero determinant to dense invertibility does not hold for general smooth symbols.

Under that additional kinetic condition the trace obstruction extends to the stated decaying kernels. Exponential decay plus nondegenerate continuum normalization is sufficient. In contrast, a smooth kinetic bump with an open region of zero kinetic symbol satisfies the two reduced uniform/affine equations exactly, with summable first moments and nondegenerate kinetic normalization at zero momentum. This is an explicit escape from the reduced argument, not a completed mixed constraint algebra.

There is also a rigorous full-zone residual bound for uniformly invertible kinetic symbols, accompanied by controlled low-momentum examples. Standard improved stencils already provide the latter approximation mechanism; no novelty is claimed for them. A discontinuous logarithm/SLAC symbol changes the domain assumptions and has a seam defect on compactly supported fields; discarding that defect would be incorrect.

## Exact source comparison and inherited scope

I read the actual landed `docs/SOFT_SPIN2_COLLISION_INVARIANTS_COMMON_CONES_AND_LATTICE_WARD_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md` at main `e75578f7136401d4bd750131671aed9212c06291`, with sections 6–9 read separately in full after a combined output was truncated. The source already proves the bounded analytic finite-band open-patch obstruction and constructs the higher-range central derivative family, including its moment identities and uniform remainder estimates. Its actual soft-collision current is `d_R d_R'`, while the reduced mixed identity here tests `d_R'`. The present use of the same stencil is an application to a different residual, not a new approximation family. Its caveats about approximate infrared identities, nonanalytic couplings, changed source content, and actual interacting phases are preserved. I did not rerun its historical runner or independently review its full collision/pole/aether theorem chain.

The earlier campaign matrix calculation supplies the setting being extended: six canonical tensor pairs, the fixed linear `C1,G1`, regular field-degree jets, proper cubic covariance, the two-dimensional axial TT block, and an exact off-shell mixed bracket. This calculation does not derive any of those structures from the framework axioms, and it does not assert a theorem about general finite-`M2` dynamics or phases.

The axial canonical coordinates are `q=((h_yy−h_zz)/2,h_yz)` and `p=(P_yy−P_zz,P_yz)`. Proper `C4` around the axial direction acts as `−I` on this two-component block and has no `−1` eigenvector in its scalar/vector complement. Both TT components must be retained. Constant and affine smearings in the axial direction preserve this isolation. Transverse zero modes are normalized canonically on a periodic transverse cylinder; the common transverse area cancels.

## A sufficient kernel and Poisson-domain contract

Assume finitely many component/monomial types at each field degree under discussion. After translating the density center, each degree-`m` term, `m≥2`, is a finite sum of expressions of the form

\[
H[s;\phi]=\sum_{x\in\mathbb Z}\sum_{a_1,\ldots,a_m}
K(a_1,\ldots,a_m)s_x
\phi^{i_1}_{x+a_1}\cdots\phi^{i_m}_{x+a_m}.
\]

Require the **complete relative-offset kernel** to obey

\[
\|K\|_{1,1}:=\sum_a(1+\sum_j|a_j|)\|K(a)\|<\infty.
\tag{1}
\]

For structures with several smearing slots, include every relative smearing and field offset in the same weight. Thus (1) applies to `G2,T2,T3,G3`, including all allowed cubic-momentum terms, and to `U0,W1` and any other retained same-order regular mixing kernels. A moment bound only for the already-projected `D` is insufficient to justify discarding the other brackets. The fixed linear seeds remain the specified finite-difference operators.

In three dimensions use the corresponding weight on all vector offsets. Absolute summability is preserved by transverse periodization, axial projection, and the finite kernel compositions used in the bracket. The weight is submultiplicative up to the elementary inequality `1+|a+b|≤(1+|a|)(1+|b|)`. Thus an off-shell polynomial identity tested against compact fields/smearings descends to a finite transverse cylinder: its symmetrized coefficient identities can be periodized with absolutely convergent sums. This is preferable to silently treating a transversely uniform infinite-volume field as compact. This descent is a necessary-sector test, not a sufficient three-dimensional construction.

Take finite-support field configurations as a common test core. Functionals with bounded or at-most-affine smearings have absolutely convergent values there. Their first functional derivatives for `m≥2` are in `ℓ¹`. To see the relevant bound, differentiate one field factor and anchor any remaining factor at a site `y` in the finite field support `S`. If `|s_x|≤C_s(1+|x|)`, then

`|s_x|≤C_s(1+max_(y∈S)|y|+|a_j|)`

for the anchored factor. Summing the derivative's output site is equivalent to summing the density center. It follows that

\[
\|\nabla H[s;\phi]\|_{\ell^1}
\le C(m,S,\|\phi\|_\infty,C_s)\|K\|_{1,1}.
\tag{2}
\]

This argument uses a remaining field factor and is why the fixed linear seeds are handled separately. Pairing two such gradients is absolutely convergent, since `ℓ¹⊂ℓ∞`; pairing them with a bounded seed gradient also converges. The canonical Poisson contractions are therefore well-defined on the stated core. No claim is made that compact support is preserved by the nonlocal Hamiltonian flows, or that (1) alone constructs a global Banach Poisson manifold and time evolution. Any claimed off-shell realization on a larger domain must in particular satisfy these necessary core identities.

## Compact plateaux justify the two tests

Choose a fixed smooth compact cutoff `χ`, equal to one near the origin. Put

`X_R(x)=χ(x/R)`, `N_R(x)=x χ(x/R)`.

For the uniform test use `N_R(x)=χ(x/R)`. These converge pointwise to constant shift and affine/uniform lapse, with `|X_R|≤C` and `|N_R(x)|≤C(1+|x|)` uniformly in `R`. The same anchoring estimate as (2), followed by dominated convergence over the coefficient and site sums, gives **ℓ¹ convergence** of every degree-at-least-two functional gradient to its constant/affine counterpart. There is no second-moment requirement in this estimate: the affine smearing costs one relative-offset moment, and no additional position-weighted gradient norm is taken.

The finite-difference gradient of `G1[X_R]` is uniformly `O(R⁻¹)`. The second-difference gradient of `C1[N_R]` is also uniformly `O(R⁻¹)` for the affine cutoff: derivatives of `xχ(x/R)` give `2χ'/R+xχ''/R²`, and `|x|=O(R)` on their support. For the uniform cutoff it is `O(R⁻²)`. Combining these bounds with (2) makes

`{G1[X_R],T3[N_R]}→0` and `{G3[X_R],C1[N_R]}→0`.

This includes cubic-momentum `G3`; it is a tail estimate, not a claim that its nonlocal derivative has finite support. The brackets of `G2` and `T2` converge by the ℓ¹ gradient convergence and boundedness. The coefficients of `U0` give, by the same dominated convergence,

\[
U_0(1,1)=\mu_0,\qquad U_0(1,x)=\mu_0x+\mu_1,
\quad \mu_1=\sum_{a,b}b\,u_{ab}.
\]

Its cutoff values are uniformly at most affine, so insertion into `T2` is legitimate. On the axial TT sector the linear momentum-constraint density is identically zero, including after transverse periodic summation. Consequently `G1[W1]` evaluates to zero for any well-defined retained `W1`; its field dependence is not ignored. The corresponding regular scalar-mixing terms that contain the vanishing linear scalar constraint also vanish at this field configuration/degree. Additional constraint species or different linear seeds are separate hypotheses, not covered by this statement.

Thus (1), together with the explicit seed/projection assumptions, is sufficient to obtain the same uniform and affine TT equations from compactly supported smearings. No affine function on a periodic torus and no uncontrolled boundary limit is used.

## Symbols and the exact extension

Write the two-component reduced forms

\[
G_2[1]=p^T Dq,\quad T_2[1]=\tfrac12p^TFp,
\quad T_2[x]=\tfrac12p^TBp,\quad B=XF+A.
\]

Here `X` multiplies by the axial integer coordinate. With `(S f)_x=f_(x+1)`, the symbol convention is `S↔e^{ik}`. Condition (1) gives `D,F∈ℓ¹_1`, hence periodic `C¹` matrix symbols. The affine offset `A` has an `ℓ¹` kernel and is continuous; its first moment is not automatically finite and is not needed. Every lapse-linear density has this form: inserting affine lapse contributes the coordinate of an anchored field plus one offset. For real kernels, write `M^sharp(k)=M(k)†`. Reality of the quadratic form gives

\[
F^\sharp=F,\quad A-A^\sharp=-i\partial_k F,
\quad [D,X]\ \longleftrightarrow\ -i\partial_kD.
\tag{3}
\]

In particular `A` need not be self-adjoint. The sign in (3) follows directly from `[S^r,X]=rS^r`; `z∂_z=−i∂_k` for `z=e^{ik}`.

Canonical differentiation with `{q,p}=1` yields the necessary identities

\[
DF+FD^\sharp=\mu_0F,
\qquad DB+BD^\sharp=\mu_0B+\mu_1F.
\tag{4}
\]

On the open set where `F` is invertible, subtracting `X` times the first identity from the second and eliminating `D^sharp` gives

\[
-iD'+[D,AF^{-1}]=\mu_1I_2,
\qquad -i(\operatorname{tr}D)'=2\mu_1.
\tag{5}
\]

No commutation, simultaneous diagonalization, reflection symmetry, or scalar TT reduction is assumed. Only the finite matrix trace is taken, not an infinite operator trace.

**Exact decay extension.** If the invertibility set of `F(k)` is dense on the momentum circle, the second identity in (5) extends to the whole circle by continuity of `D'`. Integrating one period gives `0=4πμ1`, impossible for `μ1≠0`. Invertibility almost everywhere is a sufficient stronger condition. Uniform positivity is another sufficient condition. The result uses the full exact off-shell mixed identity through (4), not an approximate infrared identity.

**Exponential corollary.** If the complete kinetic density has an exponentially weighted absolute kernel sum, `F(k)` extends analytically to a strip around the real circle. If `det F(0)≠0`, its determinant cannot vanish identically; its real-circle zeros are isolated and its invertibility set is dense. Therefore exponential kinetic decay, nondegenerate continuum normalization, and first-moment decay of the remaining kernels suffice for the contradiction. Requiring exponential decay of every kernel is sufficient but stronger than necessary. Analyticity is used here to recover dense invertibility, not to justify the compact cutoff limit.

For merely smooth kernels, `det F(0)≠0` proves invertibility only on a neighborhood of zero. Replacing that statement by dense invertibility would be an error.

## A constructive summable-kernel escape from the reduced argument

Choose real, even, periodic `C∞` functions `f,χ` with `f≥0`, `f(0)=1`, `supp f⊂(−κ,κ)`, and `χ=1` on a neighborhood of this support, with `χ=0` near the endpoints `±π`. Set `d(k)=kχ(k)`, an odd smooth periodic function, and

\[
D=i d(k)I_2,\qquad F=f(k)I_2,
\qquad A=-\tfrac{i}{2}f'(k)I_2.
\tag{6}
\]

All Fourier coefficients decay faster than every inverse power, so all fixed absolute moments are finite. The symbol `F` has the required nondegenerate value at zero, but vanishes on an open ultraviolet region. Since `d'=1` wherever `f` is nonzero, (3) and both equations (4) hold with `μ0=0,μ1=1`:

`DF+FD^sharp=0`, and the centered affine expression is `d'F=F`.

These are realizable reduced quadratic forms, not just incompatible formal symbols. Use the lapse density

`T2[N]=(1/4)p^T(NF+FN)p`

and `G2[X]=Σ_x X_x p_x^T(Dq)_x`. For affine lapse the first form gives exactly `B=XF−iF'/2`. Their density kernels inherit the stated moment bounds. This constructs the two reduced equations only; arbitrary lapse/shift closure, the full three-dimensional proper-cubic completion, other brackets and a physical phase remain unproved.

An additional explicit piecewise-polynomial version is checked in `check_decay_route.py`: `f=(1−4k²)^4` for `|k|<1/2` and zero outside, while `d=k` for `|k|≤1/2`, `d=k[1−10t³+15t⁴−6t⁵]` for `1/2<k<1`, `t=2k−1`, zero for `k≥1`, and odd for negative `k`. Periodic extension is `C²` for `d` and `C³` for `f`. Their piecewise third derivatives are integrable, so three integrations by parts give Fourier coefficients `O(|r|⁻³)` or better and hence finite first absolute moments. This less smooth example already suffices to disprove the overbroad implication from (1) and `F(0)>0` to the trace contradiction.

If a uniformly invertible example is desired, replace `f` by `f_ε=(f+ε)/(1+ε)`, `ε>0`, keeping `d`. It has `F_ε(0)=I` and positive minimum eigenvalue `ε/(1+ε)`. The uniform equation remains exact, while the affine residual is

\[
R_A=\frac{\varepsilon}{1+\varepsilon}(d'-1)I_2.
\tag{7}
\]

It becomes arbitrarily small in absolute full-zone norm as `ε→0`, despite a fixed zero-momentum kinetic normalization. Its relative residual does not become small. Thus no positive absolute lower bound depending only on `F(0)` can be inferred; control of the ultraviolet minimum singular value matters.

## Full-zone residual bound, including noncommuting matrices

For arbitrary symbols of the stated regularity define

\[
R_0=DF+FD^\sharp-\mu_0F,
\]

\[
R_A=(-iD')F+DA+AD^\sharp-\mu_0A-\mu_1F.
\]

The actual affine matrix defect is `X R0+R_A`. Thus `R_A` is the **centered** affine defect; when the uniform equation is exact it is the full affine defect. At invertible `F`, exact matrix algebra, with no commutativity assumption, gives

\[
Q:=(R_A-AF^{-1}R_0)F^{-1}
=-iD'+[D,AF^{-1}]-\mu_1 I_2.
\tag{8}
\]

Use normalized measure `dk/(2π)` on the full Brillouin circle and the matrix operator norm. Periodicity implies

\[
\int\operatorname{tr}Q\,\frac{dk}{2\pi}=-2\mu_1.
\]

Since `|tr M|≤2||M||op`, every normalized `L^p`, `1≤p≤∞`, obeys

\[
\|Q\|_{L^p(\mathrm{op})}\ge |\mu_1|.
\tag{9}
\]

This relative statement is also valid for almost-everywhere invertible `F` if (8) defines a measurable residual, interpreting an infinite norm as an immediate bound; its trace has the displayed integrable extension. For a dense invertibility set with a positive-measure singular complement, the exact contradiction above still holds, but this a.e. norm formulation should not be silently applied on the missing set.

For a uniformly invertible continuous `F`, put `κ_F=sup||F⁻¹||op` and `a_A=sup||A||op`. Equation (8) gives the useful absolute inequality

\[
\kappa_F\|R_A\|_{L^p}+a_A\kappa_F^2\|R_0\|_{L^p}
\ge |\mu_1|.
\tag{10}
\]

In particular, with the uniform equation exact,

\[
\|R_A\|_{L^p}\ge |\mu_1|\inf_k\sigma_{\min}(F(k)).
\tag{11}
\]

For positive `F`, one may instead use the self-adjoint relative energy matrix `F⁻¹/² R_A F⁻¹/²`; its trace equals that in (8) when `R0=0`, so it has the same lower bound (9). Norm statements use the declared canonical TT coordinates and lapse normalization; no observational error estimate is being asserted.

There is an explicit infrared/ultraviolet tradeoff. If a low-momentum region has normalized measure `θ<1` and `||Q||op≤ε` there, then the conditional mean norm on its complement, and therefore every conditional `L^p` norm there, is at least

\[
\frac{|\mu_1|-\theta\varepsilon}{1-\theta}
\tag{12}
\]

whenever the numerator is positive. This follows by splitting the averaged trace and applying the same trace inequality; no diagonalization is involved. Exact or accurate low-momentum behavior is allowed, at the cost of a residual elsewhere.

## Controlled infrared constructions and existing stencil prior art

For any allowed `F,A`, take the scalar-matrix generator

`D=(μ0/2)I+i μ1 d_R(k)I`.

It commutes with all matrix symbols, even when `F` and `A` do not commute with each other. The uniform equation is exact, and

`R_A=μ1(d_R'−1)F`, `Q=μ1(d_R'−1)I`.

Use the already-landed central stencil

\[
d_R(k)=\sum_{r=1}^R a_r\sin(rk),\qquad
a_r=\frac{2(-1)^{r+1}}r\frac{(R!)^2}{(R-r)!(R+r)!}.
\]

Its cancelled moments give the rigorous remainder, with `M_R=Σ|a_r|r^(2R+1)`,

\[
|d_R'(k)-1|\le \frac{M_R|k|^{2R}}{(2R)!}.
\tag{13}
\]

The leading coefficient is `−(R!)² k^(2R)/(2R)!`, so the defect is not identically zero at any finite range. With physical lattice spacing `a`, generator symbol `i μ1 d_R(ap)/a`, and position `X=an`, the same estimate is `O((aΛ)^(2R))` on `|p|≤Λ`. It is fully compatible with (9): the full Brillouin zone grows as `a⁻¹`, while the controlled physical momentum window remains fixed.

Using a smooth periodic `d(k)=k` on a prescribed interior interval, as in (6), instead gives an **exact reduced-pair identity on that interval** even with `F=I` everywhere. The residual is confined to its complement. Such `C∞` symbols can have rapidly decaying nonanalytic kernels; an analytic periodic `d` cannot equal `k` on an open interval and remain periodic. Neither construction supplies full nonlinear closure, interactions preserving a chosen band restriction, or a gravitational phase.

## Logarithm/SLAC: the seam and domain cannot be omitted

Consider `D(k)=ik I₂` on `−π<k<π`, periodically continued, `F=I₂`, `A=0`. Its real-space coefficients are

`D_r=(-1)^(r+1) I₂/r` for `r≠0`, `D_0=0`.

This defines a bounded skew-adjoint `ℓ²` Fourier multiplier, but its kernel is not absolutely summable and its first absolute moment diverges. Distributionally,

\[
-iD'=I_2-2\pi\delta_\pi I_2.
\]

The formal derivative equal to one away from the seam therefore does not solve the full-circle equation. On finitely supported real two-component `p`, direct kernel summation gives the exact quadratic-form defect

\[
\{p^TDq,\tfrac12p^TXp\}-\tfrac12p^Tp
=-\tfrac12\left\|\sum_x(-1)^x p_x\right\|^2.
\tag{14}
\]

Indeed the commutator coefficient is `rD_r=−(−1)^r` for `r≠0`, with zero at `r=0`; as a form this is `I−vv^T`, `v_x=(−1)^x`. Formula (14) is checked on four exact rational profiles, including a single-site profile with defect `−1/2` and a profile with zero alternating sum and zero defect. The commutator is not a bounded operator on the whole `ℓ²` space; Fourier point evaluation at the seam is not an `ℓ²`-continuous functional. The form on compact profiles is still well-defined.

On the different test domain of Schwartz fields whose smooth Fourier transforms are supported away from the seam, multiplication by position and this multiplier preserve the support, and the seam term vanishes. The two reduced equations then hold there. This is a verified restricted-domain escape, not a solution on all compact fields. Nonlinear products can enlarge Fourier support, so completion of the full constraint algebra on that domain is an additional obligation. Other nonsummable nonlocal kernels also require their own domain analysis; (14) does not exclude them all.

## Evidence, resource use and claim boundary

`check_decay_route.py` performs exact generic noncommuting `2×2` elimination, verifies the smoothness and reduced equations of the explicit first-moment counterexample, checks the six stencil ranges `R=1,…,6`, and evaluates the SLAC compact-field defect directly from its real-space kernel. All assertions succeeded in 0.600 seconds. The run was priced as a few symbolic `2×2` expressions and finite rational sums, comfortably below one minute and 200 MB; no heavy job or unmanaged worker was launched. Threads were capped at one. Deadline and stop-sentinel checks were active.

The quantified proofs above supply the infinite-family conclusions; finite symbolic controls do not establish them by themselves. No author runner or external theorem output was imported. `SOURCE_BINDINGS.json`, `results.json`, `results.txt`, and `MANIFEST.json` bind the actual coverage and evidence.

The supported new statement is the decay extension under a complete first-moment kernel/domain contract **and dense TT kinetic invertibility**, with the exponential-decay corollary and residual estimates. The rapidly decaying kinetic-bump example and the restricted-domain logarithm example are successful escapes from overbroad versions of that statement. Full mixed-algebra completion and actual lattice phases remain open. No universal summable-kernel, native-qubit, or emergent-gravity impossibility follows.
