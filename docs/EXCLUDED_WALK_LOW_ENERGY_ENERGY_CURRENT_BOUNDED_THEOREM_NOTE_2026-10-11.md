---
claim_id: excluded_walk_low_energy_energy_current_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
claim_scope: "For the supplied three-dimensional antisymmetric Weyl pair with exact site exclusion and the compressed additive symmetric energy density, the central low-energy scattering current changes by O(E^4). Explicit finite-time bounds hold for projected free-band packets, and smooth coherent packets realize a nonzero fourth-order current change after controlled finite preparation."
upstream_dependencies:
  - admissibility_rule_under_one_record_per_site_a_collision_changes_the_records_two_step_momentum_only_at_third_order_in_their_offsets_from_the_cones_bounded_theorem_note_2026-09-26
runner: scripts/excluded_walk_low_energy_energy_current_2026_10_11.py
---

# Low-energy energy-current control in the supplied excluded walk

**Date:** 2026-10-11

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit has not occurred.

**Source baseline:** current main `a13caa4885f547c8d206265b031ba7649e539fd9`.

**Runner:** [finite algebra, shell and packet controls](../scripts/excluded_walk_low_energy_energy_current_2026_10_11.py).

**Evidence cache:** `logs/runner-cache/excluded_walk_low_energy_energy_current_2026_10_11.txt`.

For this supplied two-record walk, exact current conservation fails in general.
This note proves quantitative positive results in an explicit central low-energy
sector. It establishes the threshold resolvent and stationary scattering
hypotheses, derives the current of a specified local energy density, and controls
both finite-time band preparations and remote-time coherent scattering packets.
The fourth-order asymptotic current bound has a nonzero coherent-packet example;
reversing its relative phase reverses the current change. This is not a
state-independent sign of loss or a kinetic relaxation rate.

The walk, continuous clock, antisymmetric sector, exclusion rule, spatial
coordinates and selected energy placement are supplied mathematical premises.
They are not derived from the framework's minimal axioms. The explicit
finite-time band bound uses 0<lambda<=1/16. The sharper scattering estimate
uses a proved common E*>0 whose numerical value is not evaluated.

## 1. Contract, theorem organization and provenance

The [parent walk contract](ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_A_COLLISION_CHANGES_THE_RECORDS_TWO_STEP_MOMENTUM_ONLY_AT_THIRD_ORDER_IN_THEIR_OFFSETS_FROM_THE_CONES_BOUNDED_THEOREM_NOTE_2026-09-26.md)
fixes the symbol, normalized contact projection and free two-step current;
its SHA-256 is `e0536f80a25feb0b368c10a0016a9d09b07b5bd06827751c30029d2eb1d70065`.
The mathematics below supplies the previously conditional central regularity
and checks the stationary theorem's hypotheses. The [placement-current note](ADMISSIBILITY_RULE_NO_FINITE_RANGE_INTERACTION_KEEPS_TWO_EXCLUDED_RECORDS_TOTAL_ENERGY_CURRENT_ON_THE_PLANE_OR_IN_SPACE_BOUNDED_THEOREM_NOTE_2026-09-26.md)
distinguishes a free additive current from an interacting energy current;
its generic-total-momentum conclusions are not used as threshold estimates.
The canonical placement is calculated explicitly in (J1)-(J6).

Equations (1)-(23) concern the contact resolvent, scattering and compressed
free current; (J1)-(J12) identify and bound the canonical energy current;
(C1)-(C12) give a quantitative preparation/scattering comparison on the actual
excluded space. The final coherent-packet construction controls its incoming,
outgoing and current-form-factor regularity, with normalizable total momentum.

All measures below are stated explicitly. The full relative torus uses
dq/(2pi)^3; the normalized singlet already lies in the antisymmetric fiber.
No extra exchange factor or collision-event normalization is inserted.

## 2. All four channels and exceptional fibers

Use normalized measure `dq/(2π)^3` on the full relative torus, the normalized constant singlet `c`, `C=|c><c|`, and `P=I-C`. The fiber free generator is

`H0(K,q)=h(K/2+q)⊗I+I⊗h(K/2−q)`, `h(k)=sin(k)·σ`.

It preserves the antisymmetric pair space. The contact vector and its norm are taken in that space using the full-torus representation; there is no additional factor of two. Define

`a=sin(K/2+q)`, `b=sin(K/2−q)`, `A=|a|`, `B=|b|`,
`S=A+B`, `D=A−B`, `t=a·b/(AB)`.

Away from individual cone points, the energies `S,−S,D,−D` have contact weights `(1−t)/4,(1−t)/4,(1+t)/4,(1+t)/4`. This follows by expanding the two one-particle projectors and using the singlet identity `<σ_i⊗σ_j>=−δ_ij`. Summing all four fractions, with `R0(z)=(H0−z)^{-1}`, gives

\[
G(K,z)=\langle c,R_0(z)c\rangle
=\int\left\{\frac{z(1-t)}{2(S^2-z^2)}+
\frac{z(1+t)}{2(D^2-z^2)}\right\}dq
=\int\frac{z(|a+b|^2-z^2)}{(S^2-z^2)(D^2-z^2)}dq.                 \tag{1}
\]

The final denominator also equals `(A²+B²−z²)²−4A²B²`. Formula (1) is interpreted at cone points through the original matrix resolvent. The singlet projector gauge is not a premise there.

M6's dispersion inequality gives `|D|≤ε(K)`, where `ε(k)=|sin k|`. At any total corner `C0∈{0,π}³`, the condition

`K=C0+δκ`, `E=δe>0`, `|κ|≤θe`, `θ<1`

therefore closes all mixed and negative-negative channels at energy E. It does not remove the mixed channels' virtual contribution to G. Conversely, low total energy alone does not close them: at `K=(π/2,0,0)`, put `q=(asin(E/√2),0,0)` with small positive E. Then `A−B=E`, both A and B tend to `1/√2`, and the positive mixed contact weight is exactly `1/2`.

At an exact total corner let r be its number of π components and let `ε_C(q)` use cos in those r coordinates and sin in the other coordinates. Then `A=B=ε_C`, and the combined zero-energy mixed weight is

`f_C(q)=Σ_{j:C_j=π} cos²(q_j)/ε_C(q)²`.

Coordinate shifts and permutation symmetry imply `∫f_C=r/3` and `∫f_C F(ε_C²)=(r/3)∫F(ε²)`. Consequently the exact full expression is

\[
G(C_0,z)=-\frac{r}{3z}
 +\left(1-\frac r3\right)z\int\frac{dq}{4\epsilon(q)^2-z^2}.   \tag{2}
\]

Thus the contact spectral measure has a zero-energy atom of mass r/3. At `C0=(π,π,π)`, `H0c=0`, `G=−1/z`, and c is already a reducing zero eigenspace. Its removal leaves the complementary unitary unchanged. Positive-energy contact weights vanish at that exact fiber. A uniform strictly positive scattering loss over all total corners is therefore false. At K=0 there is no contact atom, but the pair two-step current itself vanishes identically, so a current claim restricted only to K=0 would be trivial.

## 3. Explicit central regular domain

For the remainder of the proof take

\[
0<E\le\tfrac18,\qquad |K|\le E/4.                              \tag{3}
\]

Put `k=K/2`, `h=|k|≤E/8`. Every positive-positive shell point has `ε(q+k),ε(q−k)≤E`. Each coordinate of q±k therefore lies within `asin E` of a π-multiple. Since their separation is `2k` and `|2k|≤E/4<π−2 asin E`, both use the same coordinatewise corner. Write `q=C0+x`, `r=|x|`, in that chart. For `u=x+k`, `v=x−k`,

`ε(u)≥√(1−E²)|u|`, `ε(v)≥√(1−E²)|v|`.

Indeed each coordinate has absolute value at most asin E and `sin y/y≥cos(asin E)`. Hence

`3E/8≤r≤E/[2√(1−E²)]<9E/16`.                       (4)

The lower bound follows from `E≤|u|+|v|≤2r+2h`. This proves full shell coverage in eight disjoint small corner charts and excludes other shell components.

For `n∈S²`, let `S_K(r,n)=ε(rn+k)+ε(rn−k)`. On `r∈[E/4,E]`, `R=|rn±k|≤9E/8<1/4`, and

\[
\left|\nabla\epsilon(y)-\frac y{|y|}\right|\le\frac56|y|^2.
                                                                    \tag{5}
\]

To prove (5), write `∇ε(y)=diag(cos y) sin(y)/|sin y|`. The cosine error is at most `|y|²/2`; normalization changes a nonzero vector by at most twice its relative error, and `|sin y−y|≤|y|³/6`. The second error is at most `|y|²/3`. Also

`n·(rn±k)/|rn±k|≥(r−h)/(r+h)≥1/3`.

Each radial derivative is therefore greater than `1/3−5/96>1/4`. Since `|∇ε|≤1`,

\[
\tfrac12\le\partial_r S_K\le2.                                  \tag{6}
\]

At r=E/4 the energy is at most 3E/4; at r=E it is at least `(3/4)(|En+k|+|En−k|)≥3E/2`. Thus every ray has exactly one root, and (4) shows that it is the full shell.

Let `s_±=sin(rn±k)`. The actual vectors in (1) are `a=s_+`, `b=−s_−`, up to the same corner signs. The contact weight is

`w=(1+s_+·s_−/(|s_+||s_−|))/4`.

The identity `s_+·s_−=ε(rn)²−ε(k)²`, together with `ε(rn)≥3r/4` and `h≤r/2`, gives positive dot product. Thus `1/4≤w≤1/2`. Coarea now has no hidden shell multiplicity:

\[
\rho(K,E)=\frac8{(2\pi)^3}\int_{S^2}
 \frac{w(rn)r^2}{\partial_rS_K(r,n)}d\Omega,
\qquad
\frac{E^2}{32\pi^2}\le\rho(K,E)\le\frac{4E^2}{\pi^2}.          \tag{7}
\]

The lower estimate uses only r≥E/4, w≥1/4 and the slope upper bound; the upper uses r≤E, w≤1/2 and the slope lower bound.

The real boundary value needs an estimate, not just (7). Keep K and E fixed and consider energy `u∈I=[7E/8,9E/8]`. The same ray interval `[E/4,E]` contains every root for every such u. Full coverage follows from the same coordinate argument with `u≤9E/8`. On this common interval `|rn±k|≥E/8`, so `ε(rn±k)≥3E/32`. Therefore

`|∂_r w|≤6/E`, `|∂_r²S_K|≤44/E`.

For the latter, `||Hess ε(y)||≤2/ε(y)` when `ε(y)≤1`; the two terms in the Hessian of a Euclidean norm composed with sin give this bound. If `F(u,n)=w r²/S'_K`, implicit differentiation gives

`F_u=(w_r r²+2rw)/(S'_K)²−w r² S''_K/(S'_K)³`,

hence `|F_u|≤28E+176E=204E`. Integrating the angular factor gives

\[
\sup_{u\in I}|\partial_u\rho(K,u)|\le816E/\pi^2.              \tag{8}
\]

The positive-band Cauchy integral over I has a finite boundary value: subtract `ρ(K,E)` and use (8). The constant part has zero real principal value because I is symmetric about E. Its real contribution is at most `204E²/π²`; its imaginary part is `πρ(K,E)≤4E²/π`. Every remaining spectral contribution is at least E/8 from E, and the entire contact measure has mass one, so its absolute value is at most 8/E. Thus

\[
\operatorname{Im}G(K,E+i0)=\pi\rho(K,E),\qquad
\frac{E^2}{32\pi}\le |G(K,E+i0)|\le\frac9E,
\quad |G(K,E+i0)^{-1}|\le\frac{32\pi}{E^2}.                   \tag{9}
\]

Here `8/E+(204/π²+4/π)E²≤9/E` on (3). This proves an explicit nonzero regular denominator without assuming a limiting-absorption theorem. Smooth local coarea density and repeated subtraction also give `G,ρ∈C^∞` on every compact subdomain with strict energy separation. The bound in (9) is deliberately coarse near zero.

## 4. Sharper uniform central threshold expansion

Let e belong to a fixed compact positive interval and `|κ|≤e/4`, with `K=δκ`, `E=δe`. Define

\[
I_0=\int\frac{dq}{4\epsilon(q)^2},\qquad
v_j(q)=\frac{\sin q_j\cos q_j}{\epsilon(q)},
\]

\[
\mathcal A(\kappa,e)=e\int
\frac{e^2-|\kappa\mathbin{\odot}\cos q|^2}
 {4\epsilon(q)^2[e^2-(\kappa\cdot v(q))^2]}dq.                \tag{10}
\]

The singularity of I0 at each of the eight cones is integrable in dimension three. In particular `I0≥1/12`. Since `|κ·v|²≤|κ⊙cos q|²≤|κ|²`,

\[
e(1-|\kappa|^2/e^2)I_0\le\mathcal A(\kappa,e)\le eI_0.     \tag{11}
\]

The claimed uniform expansion, including virtual mixed channels, is

\[
G(\delta\kappa,\delta e+i0)=\delta\mathcal A(\kappa,e)+O(\delta^2).
                                                                    \tag{12}
\]

Here is a direct control of the principal value in (12). At real energy inside the gap rewrite (1) as

`G/E = ∫ Wδ(q)/(S²−E²−i0) dq`,
`Wδ=(E²−|a+b|²)/(E²−D²)`.

The shorthand `−i0` has the same positive-energy pole convention as `(S²−(E+i0)²)^{-1}`. The mixed denominator is separated from zero. Moreover `D²≤|a+b|²≤|K|²`, so `1−|K|²/E²≤Wδ≤1`.

Choose disjoint fixed balls of radius r0 around the eight cones, and an inner radius Rδ with fixed R sufficiently large for the compact e,κ domain. Every on-shell root lies inside these inner balls by (4). On a cone annulus `Rδ≤r≤r0`, the elementary norm-composition derivative estimates are `|∂^j ε|≤C_j r^{1−j}`: differentiate the norm of sin, use `|sin q|≥c r`, and bounded derivatives of sin. Taylor expansion symmetrically about q then yields

`S=2ε+O(δ²/r)`, `D/δ=κ·v+O(δ²/r²)`,
`|a+b|²/δ²=|κ⊙cos q|²+O(δ²)`.

Consequently `S²−δ²e²≥c r²` for a sufficiently large fixed R, and the difference between the integrand of `G/δ` and the integrand in (10) is bounded by `C δ²/r⁴`. Integrating `r² dr` from Rδ to r0 gives O(δ). Away from all cone balls the bound is O(δ²).

It remains to justify the inner part, where expanding through the pole would be invalid. Set `q=C0+δp` in each inner ball. The matrix resolvent integrand is δ^{-1} times the resolvent of the smooth scaled matrix `δ^{-1}H0(δκ,C0+δp)` at e, and the volume contributes δ³. The ++ pole is simple, in an annulus bounded away from the individual cone points, with uniformly positive radial slope by (6). Coarea followed by symmetric density subtraction, exactly as in (8), bounds its principal-value integral uniformly in the scaled variables. Away from this shell the scaled matrix inverse is uniformly bounded; in particular the individual projector cone points have no resolvent singularity because their total energy is separated from e. A smooth energy cutoff equal to one near e makes the subtraction interval fixed and leaves bounded integrals outside it. Thus each inner contribution to G is O(δ²). The integral of the limiting integrand in (10) over the same inner balls is O(δ), hence its contribution after multiplication by δ is also O(δ²). These bounds prove (12).

This proof supplies a finite uniform remainder constant, not a numerically evaluated maximal threshold. With e=1, (11) and (12) imply that there exists E*>0, E*≤1/8, such that uniformly for `|K|≤E/4`, `0<E≤E*`,

\[
\operatorname{Re}G(K,E+i0)\ge\frac{15I_0}{32}E\ge\frac5{128}E.
                                                                    \tag{13}
\]

The following differentiated form will be needed for the prepared packets.
Fix a compact domain D with e_-<=e<=e_+, e_->0 and |kappa|<=e/4.
For each fixed multi-index alpha, there is a finite C_alpha such that

    sup_D |partial_(kappa,e)^alpha
       [G(delta kappa,delta e+i0)-delta A(kappa,e)]|
          <=C_alpha delta^2.                         (12a)

To justify derivatives at the boundary of D, enlarge it slightly to a compact
positive-energy domain with |kappa|/e strictly below 1/3. On the cone annuli,
each extra spatial derivative in the Taylor remainder is accompanied by a
delta factor, with delta/r<=1/R. The product and quotient rules therefore
preserve the majorant C_alpha delta^2/r^4 for the difference of the G/delta
integrand and the limiting integrand. Its integral is O_alpha(delta).

Inside q=C0+delta p, the scaled ++ shell is separated from the individual
cone points and has a uniformly positive radial slope. Choose an even smooth
energy cutoff chi, equal to one near the pole and of fixed small width relative
to e_-. The scaled coarea density J(u;kappa,delta) has uniformly bounded
fixed-order derivatives. The pole part is exactly

    integral chi(t)[J(e+t;kappa,delta)-J(e;kappa,delta)]/t dt
       +i pi J(e;kappa,delta).

The constant real principal value vanishes by evenness. Every fixed parameter
derivative of the numerator difference is O_alpha(|t|), using one further
bounded energy derivative of J. This supplies an integrable majorant without
differentiating an unsubtracted pole. Outside the cutoff the full scaled
matrix inverse is uniformly separated from its poles, including the individual
cone points; use the matrix inverse there, not singular eigenprojectors.
This controls the inner contribution and its derivatives by O_alpha(delta^2).
The limiting integrand's derivatives are bounded by C_alpha/r^2, so its omitted
inner contribution after multiplication by delta is also O_alpha(delta^2).
These estimates prove (12a).

The derivatives are in scaled (kappa,e), not unscaled (K,E). Translating j
unscaled derivatives costs delta^(-j); no uniform physical-energy C^r bound
at zero follows. No estimate uniform in derivative order, derivative in delta,
or explicit numerical maximal E* is asserted. Local positive-energy C^r
regularity already follows from Section 3. The coarea argument for (14) also
gives its fixed-order scaled-parameter differentiated remainder.

For completeness the leading spectral density is

\[
\rho(\delta\kappa,\delta e)
 =\frac{\delta^2(e^2-|\kappa|^2)}{4\pi^2}+O(\delta^4).         \tag{14}
\]

To see the coefficient without relying on angular sampling, use one cone's physical momentum p for particle 1 and κ−p for particle 2. On the limiting shell `|p|+|κ−p|=e`,

`w0=(e²−|κ|²)/(8|p||κ−p|)`.

The integral of `δ(e−|p|−|κ−p|)/(|p||κ−p|)` over R³ equals 2π. For κ≠0, use prolate coordinates `u=(r1+r2)/|κ|`, `v=(r1−r2)/|κ|`, azimuth φ: the Jacobian is `|κ|³(u²−v²)/8`, and `r1 r2=|κ|²(u²−v²)/4`. The delta factor removes |κ|; the remaining v and φ integrals give 2π. The κ=0 case is its direct spherical limit. Multiplying by eight cones and `(2π)^{-3}` proves the coefficient. On the compact timelike domain, individual momenta stay bounded away from zero on the scaled shell; `sin(δp)/δ` is smooth in δ², and the implicit radial root has a uniform slope. Thus the scaled coarea integral differs from its δ=0 value by O(δ²), proving the remainder in (14).

At K=0 an exact independent normalization formula is available for `0<E<2`:

\[
\rho(0,E)=\frac{E^2}{16\pi^3}\int_{S^2}
 \prod_{j=1}^3(1-E^2 n_j^2/4)^{-1/2}d\Omega.
                                                                    \tag{15}
\]

It follows from `u=sin q` in the eight cone charts. In particular it lies between `E²/(4π²)` and `E²/[4π²(1−E²/4)^{3/2}]`.

## 5. Actual stationary scattering and coherent current change

The compressed generator is realized on the original fiber by `Hext=P H0 P`, with zero on c. Put `b=H0c`. Since `<c,H0c>=0`,

\[
V=H_{\rm ext}-H_0=-|b\rangle\langle c|-|c\rangle\langle b|,
\qquad \|b\|^2=2\sum_j\cos^2(K_j/2)\le6.                     \tag{16}
\]

This is bounded self-adjoint of rank at most two. Its contact zero mode is not an incoming scattering state.

The external stationary theorem used here is Yafaev's Theorems 2.3/2.4, Eq. (2.8), pp.369–371. They give the stationary formula for `V=L* J L` under the stated compactness and trace-ideal hypotheses for the sandwiched resolvent; J need not have constant sign. Choose `Lf=(<c,f>,<b,f>,Qf)`, where Q is injective Hilbert–Schmidt, and `J=[[0,−1],[−1,0]]⊕0`. Then L is injective and Hilbert–Schmidt. Since H0 is bounded, both trace-ideal hypotheses of Theorem 2.4 hold with p=1. Its conclusion supplies Assumption 2.2 and Eq. (2.8). This checks the otherwise easily missed kernel condition. The resulting formula holds almost everywhere in energy. [Yafaev, *On the scattering matrix for perturbations of constant sign* (1992)](https://www.numdam.org/item/AIHPA_1992__57_4_361_0.pdf).

The active two-dimensional part can be evaluated independently of that theorem's proof. Set G=G(K,z). The free sandwiched resolvent, in the rows c,b, is

\[
B_0(z)=\begin{pmatrix}G&1+zG\\1+zG&z+z^2G\end{pmatrix},
\qquad \det(I+B_0J)=-zG,
\]

\[
J(I+B_0J)^{-1}
=\begin{pmatrix}G^{-1}+z&-1\\-1&z^{-1}\end{pmatrix}.          \tag{17}
\]

The auxiliary Q rows do not enter because J is zero there. At shell energy E>0, the spectral restrictions satisfy `Γ_E b=E Γ_E c`. Thus (17) restricts exactly to `|Γ_Ec><Γ_Ec|/G`. Equivalently the full resolvent is

`Rext=R0−R0 C R0/G−C/z`;

the extra T term is `(H0−z)C(H0−z)/z` and vanishes on shell. No convergence of scattering operators under an infinite-coupling limit has been assumed.

On the regular region (3), `||Γ_Ec||²=ρ(K,E)>0`. Let `v_E=Γ_Ec/√ρ`. The stationary scattering matrix therefore has the representative

\[
S_E=I+(s_E-1)|v_E\rangle\langle v_E|,
\qquad s_E=1-\frac{2\pi i\rho}{G}=\frac{\overline G}{G},
\qquad |s_E-1|=\frac{2\pi\rho}{|G|}.                         \tag{18}
\]

It acts as the identity on the orthogonal channel complement. The sign in (18) is tied to `(H0−z)^{-1}` and `S=W_+^*W_-`. Formula (9) prevents a denominator zero; smooth local density and G give a continuous representative in the regular energy interval. The physical scattering operator itself is defined up to energy-null sets, which suffices for every packet statement. The theorem is applied fiberwise; no assertion that the direct integral over K is trace class is made.

For any bounded real multiplication observable g on the shell, set `μ=<v_E,g v_E>` and `w=(g−μ)v_E`. Since w is orthogonal to v_E, expansion of (18) gives exactly

\[
S_E^*gS_E-g=(s_E-1)|w\rangle\langle v_E|
 +(\overline{s_E}-1)|v_E\rangle\langle w|,
\qquad
\|S_E^*gS_E-g\|=|s_E-1|\sqrt{\operatorname{Var}_{v_E}(g)}.    \tag{19}
\]

The diagonal term cancels by `|s_E|=1`; the nonzero two-dimensional block has eigenvalues `±|s_E−1|||w||`. This remains true when w=0.

For the supplied additive pair two-step current, `g_a(K,q)=sin K_a cos 2q_a`. On (3) the relative offset r is at most E, so its shell range has length at most `2|sin K_a|E²`. The elementary interval variance bound is `Var≤(range)²/4`; it follows from `(g−m)(M−g)≥0` and maximizing `(μ−m)(M−μ)`. From (7), (13), (18), (19), for `0<E≤E*`,

\[
\|S_E^*g_aS_E-g_a\|
 \le\frac{1024}{5\pi}|\sin K_a|E^3
 \le\frac{256}{5\pi}E^4.                                  \tag{20}
\]

Direct integration gives the corresponding expectation bound for arbitrary normalized coherent incoming packets supported in that region, without an angular incoherence or event-count assumption. This is an asymptotic incoming/outgoing observable bound for actual hard-core scattering. It differs from a conditional change per selected collision, and it does not provide a kinetic relaxation time. The constant and E* are conservative; E* is supplied by the proved remainder existence, not numerically certified here.

## 6. A separate explicit finite-time unitary result

This result uses the density upper estimate (7) and needs neither stationary scattering nor a principal-value estimate. Let `0<λ≤1/16`, let φ be a normalized free pair packet with spectral support `λ≤H0≤2λ`, and restrict its total-momentum support to `|K|≤λ/4`. Equivalently one may work at one fixed K. These energies have only ++ channels. By (7),

\[
\|C\mathbf1_{[\lambda,2\lambda]}(H_0)\|\le
\eta_\lambda:=\sqrt{\frac{28}{3\pi^2}}\lambda^{3/2}<1.        \tag{21}
\]

For a direct integral, C and P in this section mean the decomposable contact projections, and the same bound follows from the uniform fiber estimate. The contact mass is `∫_λ^{2λ}ρ(K,E)dE≤28λ³/(3π²)`. The spectral theorem and (16) then give, for every t,

`||V exp(−itH0)φ||≤(√6+2λ)ηλ`.

The second term is `||C H0 exp(−itH0)φ||≤2λ ηλ`. Duhamel and normalization of the actual allowed initial state `χ=Pφ/||Pφ||` therefore yield

\[
\|e^{-itH_{\rm ext}}\chi-e^{-itH_0}\phi\|
 \le d_t:=\eta_\lambda[\sqrt2+(\sqrt6+2\lambda)|t|].          \tag{22}
\]

Indeed if `β=||Cφ||`, then `||χ−φ||²=2(1−√(1−β²))≤2β²`. The compressed state stays in P. Its projection initially introduces components outside the original energy band; (22) already includes them and does not assume that the hard-core state remains spectrally band-limited.

A useful current bound follows by subtracting the K-dependent constant `sin K_a`. That multiplier commutes with both generators, so it contributes no drift. Write `O_a=g_a−sin K_a I` and `s_a=ess sup_{K in packet}|sin K_a|≤λ/4`. Globally `||O_a||≤2s_a`, whereas on the free band `||O_a exp(−itH0)φ||≤8s_a λ²` by the shell coverage. Expanding the expectation in the state difference gives

\[
\left|\langle\chi_t,g_a\chi_t\rangle-
             \langle\chi,g_a\chi\rangle\right|
\le16s_a\lambda^2(d_t+d_0)+2s_a(d_t^2+d_0^2),
\quad d_0=\sqrt2\eta_\lambda.                               \tag{23}
\]

On the allowed space these expectations are those of `P g_a P` under the actual compressed unitary. Formula (23) is O((1+T)² λ⁴) for fixed `|t|≤T`, with all displayed constants explicit. For `|t|≤T0 λ^{-1/2}`, it is O_{T0}(λ³) and the state error in (22) is O_{T0}(λ). This is a positive finite-time result for arbitrary packets in the stated free spectral band, after the explicit allowed-state preparation. It neither assumes that a collision took place nor estimates a macroscopic relaxation time.

The observable here is the compressed free two-step current. M3 permits placement-dependent finite-rank corrections to an interacting energy current. Those require their own matrix elements and are not silently included in (20) or (23). Nor is an unbounded position observable controlled by these norm estimates. The quantitative Cook bridge below addresses remote-time preparation and such corrections; it is not used to prove (21)–(23).


## 7. Canonical compressed density and its bounded current

For particle i=1,2 let h_i be the repo's one-body walk and X_(i,a) its
position operator. Use the additive symmetric local energy densities

    e_x^0=(1/2) sum_(i=1,2) {Pi_(i,x),h_i},
    e_x=P e_x^0 P,
    H_D=sum_x e_x=P H0 P, H0=h_1+h_2.

Here P removes coincident sites in the antisymmetric two-record space.
On finite-support states the energy first moment is

    D_a=P D0,a P,
    D0,a=(1/2)({X_(1,a),h_1}+{X_(2,a),h_2}).       (J1)

The free commutator is bounded:

    i[H0,D0,a]=g_a,
    g_a=sin(k_(1,a))cos(k_(1,a))
           +sin(k_(2,a))cos(k_(2,a))
        =sin K_a cos(2q_a).                        (J2)

This follows from (1/2){partial_a h_i,h_i}=sin k_(i,a)cos k_(i,a) I.
The cross-particle commutators vanish. We compute i[H_D,D_a] first on
the common finite-support core and then obtain its bounded extension.

Work in a local total-momentum chart K=k_1+k_2, q=(k_1-k_2)/2, with
smooth sections compactly supported in K. Torus q is periodic. Let c be
the constant normalized singlet, C=|c><c|, P=I-C in each fiber, and

    h=H0 c, h'_a=partial_(K_a) h,
    Hdiff=h_1-h_2, H0'=partial_(K_a)H0.

P is independent of K. Since X_(1,a)=i(partial_Ka+partial_qa/2) and
X_(2,a)=i(partial_Ka-partial_qa/2), direct symmetrization gives

    D0,a=i H0 partial_Ka+(i/2) Hdiff partial_qa+i H0'. (J3)

The equality partial_qa Hdiff=2H0' is essential to this expression.
Put Dq=(i/2)Hdiff partial_qa+iH0'. Integration by parts in q gives
Dq^*=(i/2)Hdiff partial_qa, so Dq^* c=0. Also Dq c=i h'_a.
Consequently the contact blocks are

    C D0,a P psi = i c <h,partial_Ka psi>,
    P D0,a C (c f) = i partial_Ka(h f).             (J4)

Here c is constant, <c,H0c>=0 and <c,h'_a>=0. These relations retain
the derivatives in K; discarding them would give the wrong current.

Expand the compressed commutator:

    i[PH0P,PD0,aP]
       =P g_a P-i P H0 C D0,a P+i P D0,a C H0 P.

Insert (J4). The terms h<h,partial_Ka psi> cancel. The remaining bounded
finite-rank correction is

    J_a=i[H_D,D_a]=P g_a P+F_a,
    F_a=-|h'_a><h|-|h><h'_a|.                     (J5)

Both h and h'_a lie in P. Thus (J5) is an operator identity for the bounded
extension of this canonical current, and not a postulated current choice.
It uses the specified compressed local densities in (J1).
The finite-support core calculation extends to the smooth compact-chart
sections used above by H1 approximation: D0,a maps H1 to L2 continuously,
and H0 and P preserve H1. These sections need not themselves have finite
spatial support. No self-adjointness claim for the unbounded dipole is
needed to identify its bounded commutator extension.

Pointwise singlet algebra gives

    h(q)=2 sum_j cos(K_j/2) sin q_j sigma_(1,j)c,
    h'_a(q)=-sin(K_a/2) sin q_a sigma_(1,a)c,
    ||h||^2=2 sum_j cos(K_j/2)^2<=6,
    ||h'_a||=|sin(K_a/2)|/sqrt(2),
    ||F_a||<=2sqrt(3)|sin(K_a/2)|.                 (J6)

In particular both g_a and F_a vanish at central total momentum K=0.
This is consistent with special zero-current sectors; no nonzero drift
for every state is asserted.

## 8. Band estimates retaining the canonical correction

Use the domain and density conclusion (21): 0<lambda<=1/16, free spectral support
[lambda,2lambda], total-momentum support |K|<=lambda/4, and

    eta=sqrt(28/(3pi^2)) lambda^(3/2),
    ||C 1_[lambda,2lambda](H0)||<=eta.              (J7)

The source's positive-positive shell coverage also gives relative distance
r<=E<=2lambda from one of eight corners and contact spin weight at least
1/4 on every shell in this band. Let Pi_band be that spectral projection.
Since h=H0c,

    ||Pi_band h||<=2lambda eta.                    (J8)

The normalized torus measure of the band support is at most 4eta^2:
its contact spectral mass is at least one quarter of that volume. On this
support |sin q_a|<=2lambda. Equation (J6) therefore implies

    ||Pi_band h'_a||<=4lambda |sin(K_a/2)| eta.      (J9)

No inequality for a general spin form factor is inferred from contact
mass alone; the lower contact weight and pointwise bound are both used.

For a normalized free-band vector phi_t=exp(-itH0)phi and
t_a=ess sup_K |sin(K_a/2)|, equations (J6)-(J9) give uniformly in time

    ||F_a phi_t||<=(sqrt(2)+4sqrt(6)) t_a lambda eta,
    |<phi_t,F_a phi_t>|<=16 t_a lambda^2 eta^2.     (J10)

These also hold for normalized direct-integral packets by the uniform
fiber inequalities and Cauchy-Schwarz. Put

    s_a=ess sup_K |sin K_a|<=lambda/4,
    t_a<=lambda/8,
    O_a=g_a-sin K_a I+F_a,
    B_a=8s_a lambda^2+(sqrt(2)+4sqrt(6))t_a lambda eta,
    C_a=2s_a+2sqrt(3)t_a.

The shell range estimate in Sections 2-6 yields ||O_a phi_t||<=B_a;
globally ||O_a||<=C_a. On P, O_a is J_a minus the conserved multiplier
sin K_a. The latter commutes with the full compressed generator, so
subtracting it does not change the current drift.

## 9. Finite-time canonical energy-current theorem

Prepare chi=P phi/||P phi|| and evolve chi_t=exp(-itH_D)chi. The direct Duhamel estimate (22) is

    ||chi_t-phi_t||<=d_t,
    d_t=eta[sqrt(2)+(sqrt(6)+2lambda)|t|],
    d_0=sqrt(2)eta.                                (J11)

This includes the non-band-limited part introduced by projection. At each
endpoint, expand the quadratic expectation in chi_t-phi_t. The error is
at most 2B_a d_t+C_a d_t^2. The free expectation of g_a-sin K_a is
constant. Equation (J10) bounds the difference of its two F_a expectations.
Therefore the actual canonical current satisfies

    |<chi_t,J_a chi_t>-<chi,J_a chi>|
       <=2B_a(d_t+d_0)+C_a(d_t^2+d_0^2)
                                      +32t_a lambda^2 eta^2. (J12)

For a fixed supplied T, the right side is O_T(lambda^4), uniformly over
|t|<=T and every normalized packet with the specified free-band support,
after the displayed exclusion preparation. For |t|<=T0 lambda^(-1/2),
it is O_(T0)(lambda^3); the state error is O_(T0)(lambda). These are
upper bounds with explicit finite constants, not positive loss rates or
many-body relaxation estimates. No smooth spectral profile is required
for (J7)-(J12); the supplied band restriction suffices.

## 10. Canonical asymptotic current

At fixed K, a finite-rank form factor has vanishing matrix elements along
every free absolutely continuous packet as |t| tends to infinity. Its
scalar complex spectral density is L1 by finite variation and absolute
continuity, so this follows from the Riemann-Lebesgue lemma. Thus the F_a
expectation vanishes in asymptotic free scattering packets. For normalizable
total-K packets, uniform boundedness of F_a and dominated convergence give
the same result by integrating the fiber statement. Wave-operator norm
convergence then gives the same canonical current asymptotes as the free
g_a scattering observable. This statement is qualitative; the following
Cook bridge retains quantitative spectral-derivative constants.


## 11. Exact finite-rank extension

Fix total momentum K in three dimensions. On the antisymmetric fiber use
normalized torus measure and

    H0(q)=sigma_1 dot sin(K/2+q)+sigma_2 dot sin(K/2-q).

Let c be the normalized constant singlet, C=|c><c|, P=I-C, and h=H0 c.
The singlet has zero one-spin expectation, so <c,H0c>=0. Set H=PH0P on
the full fiber. Its restriction to P is the physical excluded walk and its
restriction to C is a decoupled zero eigenstate. Direct expansion gives

    V=H-H0=-|h><c|-|c><h|,                          (C1)
    <c,h>=0,  ||h||^2=2 sum_a cos(K_a/2)^2 <=6.      (C2)

Indeed H0 c=[sigma_1 dot (a-b)]c, where a=sin(K/2+q),
b=sin(K/2-q). The Pauli identity gives norm squared |a-b|^2 pointwise,
and a-b=2 cos(K/2) sin q. Each normalized torus integral of sin^2 q_a
is 1/2. Thus H and H0 are bounded self-adjoint and V is self-adjoint
of rank at most two. The special all-pi fiber has h=0 and no perturbation.

Let P_ac(H0) be the absolutely continuous spectral projection. Kato's
trace-class theorem implies that

    Omega_+/-=s-lim_(t->+/-infinity) exp(itH) exp(-itH0) P_ac(H0)

exist and map the absolutely continuous space of H0 isometrically onto
that of H. Consequently S=Omega_+^* Omega_- is unitary on that initial
space and Omega_- = Omega_+ S there. The auxiliary zero eigenstate is
orthogonal to both wave-operator ranges. No absence-of-bound-states
assumption is needed.

The exact primary import is Theorem 1, p.260, of Tosio Kato, Perturbation
of Continuous Spectra by Trace Class Operators, Proceedings of the Japan
Academy 33 (1957), 260-264:
[primary paper](https://www.jstage.jst.go.jp/article/pjab1945/33/5/33_5_260/_pdf)
Its self-adjoint and trace-class hypotheses hold by (C1); its limits use
the same sign convention. The theorem and its five-page source were read.
The bounds below are direct calculations and are not attributed to that
paper's statement. This application is fiberwise: it does not claim that
the full translation-invariant two-body perturbation is trace class.

## 12. Quantitative Cook tails from contact spectral regularity

Let psi be a normalized vector in P_ac(H0). Define the complex scalar
spectral density b_psi by

    <c, dP_H0(E) psi> = b_psi(E) dE.

For an integer r>=2 assume b_psi and E b_psi belong to W^(r,1)(R).
Functions are extended over the whole real line; these hypotheses include
the vanishing boundary traces needed for integration by parts. A compactly
supported smooth density inside a regular energy interval suffices. Set

    A_r(psi)=|| d_E^r b_psi ||_1,
    D_r(psi)=||h|| A_r(psi)+|| d_E^r(E b_psi) ||_1.

Write a_psi(t)=<c,exp(-itH0)psi>. Fourier integration by parts yields

    |a_psi(t)| <= A_r(psi) |t|^-r,
    |a_psi'(t)| <= ||d_E^r(E b_psi)||_1 |t|^-r.      (C3)

The sign relation <h,exp(-itH0)psi>=i a_psi'(t) and (C1) give

    ||V exp(-itH0)psi||
       <= ||h|| |a_psi(t)|+|a_psi'(t)|
       <= D_r(psi) |t|^-r.                         (C4)

The derivative of exp(itH)exp(-itH0)psi is
i exp(itH)V exp(-itH0)psi. Integrating this identity from T to infinity,
or from minus infinity to -T, proves for T>0

    ||(Omega_+ - exp(iTH)exp(-iTH0))psi||
       <= D_r(psi)/[(r-1) T^(r-1)],
    ||(Omega_- - exp(-iTH)exp(iTH0))psi||
       <= D_r(psi)/[(r-1) T^(r-1)].                 (C5)

These tails use the full V, including both contact matrix elements. A
bound on contact occupation alone without its time derivative would not
establish (C4).

## 13. Prepared finite-time scattering experiment

Let phi=S psi and also require the same W^(r,1) hypotheses for b_phi.
At time -T start the excluded walk in

    eta_- = P exp(iTH0)psi / ||P exp(iTH0)psi||,

assuming |a_psi(-T)|<1. Its state at +T is eta_+=exp(-2iTH)eta_-.
For any normalized chi with contact amplitude a, direct calculation gives

    ||P chi/||P chi|| - chi||^2
       =2(1-sqrt(1-|a|^2)) <=2|a|^2.              (C6)

Apply (C5) first to psi at -T, use Omega_-psi=Omega_+phi, and then apply
(C5) to phi at +T. Unitary propagation and (C6) prove

    ||eta_+ - exp(-iTH0)phi|| <= R_T,
    R_T=[D_r(psi)+D_r(phi)]/[(r-1) T^(r-1)]
                              +sqrt(2) A_r(psi)/T^r. (C7)

This is a finite-time norm estimate for the actual compressed unitary.
It is conditional on explicit packet regularity, not on a collision
count, relaxation ansatz, presumed Fermi-golden-rule rate or initial
scattering-state preparation. The excluded preparation is displayed.

## 14. Current and bounded-observable consequences

Let g be a bounded self-adjoint operator commuting with H0. For the
specific observable J=P g P on the excluded space, free time evolution
keeps the expectation of g fixed. The inequality between expectations
of a bounded observable in two unit vectors is at most twice its norm
times their norm distance. Applying it at both endpoints yields

    |<eta_+,J eta_+>-<eta_-,J eta_->
                 -<psi,(S^* g S-g)psi>|
       <=2||g|| { [D_r(psi)+D_r(phi)]/[(r-1)T^(r-1)]
                                    +2sqrt(2)A_r(psi)/T^r }. (C8)

For the repo's free two-step current, g_a(q)=sin K_a cos(2q_a).
Equation (C8) applies to its explicit compression. Identifying it with
a chosen interacting placement current requires checking that placement;
a finite contact correction is not silently set to zero.

A version retaining such a correction is also elementary. Suppose a
bounded self-adjoint extension of the desired physical current is
J_ext=g+A M A^*, with columns f_j of A and a Hermitian finite matrix M.
For chi=psi or phi let

    <f_j,dP_H0(E)chi>=b_(j,chi)(E)dE,
    F_r(chi)=sum_j ||d_E^r b_(j,chi)||_1^2,

and require these scalar densities to be W^(r,1)(R). At time +/-T,
the free expectation of A M A^* is bounded in absolute value by
||M|| F_r(chi)/T^(2r). Repeating the endpoint comparison proves (C8)
with ||g|| on its right replaced by ||J_ext|| and the extra term

    ||M|| [F_r(psi)+F_r(phi)]/T^(2r).               (C9)

Here the left-hand side uses the compression P J_ext P on the excluded
space; a literal restriction gives the same result when J_ext preserves P. Finite support by itself does not assert these packet regularity
hypotheses or numerical constants; the form factors must be checked.

## 15. Rank-one scattering specialization

On the central regular domain proved above, the stationary
representation has contact density rho(E)>0, normalized
contact vector v_E, and

    S_E=I+(s(E)-1)|v_E><v_E|,
    s(E)=conj(G(E+i0))/G(E+i0), Im G=pi rho.        (C10)

For a real bounded shell multiplier g_E put
w_E=(g_E-<v_E,g_E v_E>)v_E, so <v_E,w_E>=0. Direct multiplication gives

    S_E^*g_E S_E-g_E
       =(s-1)|w_E><v_E|+(conj(s)-1)|v_E><w_E|,
    ||S_E^*g_E S_E-g_E||
       = |s-1| ||w_E|| = (2pi rho/|G|) sqrt(Var_(v_E)(g_E)). (C11)

The equality also holds when w_E=0. It concerns an operator difference,
and does not assert nonzero loss for every state or a sign of current
change. Direct integration bounds the packet expectation by the
essential supremum of (C11) on its energy support.

The contact density of the outgoing packet is b_phi(E)=s(E)b_psi(E).
Thus b_psi compactly supported in this interval and s of class C^r
there provide the needed outgoing contact regularity; its constants
come from the product rule and must be bounded before using a claimed
uniform low-energy scaling. The current-contact form factors in (C9)
have their own regularity obligations.

Equations (7), (13) give rho<=C_rho E^2 and |G|>=c_G E on
the stated central domain, and its entire positive shell has distance at most E
from the relative-momentum corners in {0,pi}^3. Thus g_a=sin K_a cos(2q_a) has shell range at most 2|sin K_a|E^2.
The variance of a real variable in an interval of length L is at most
L^2/4. Hence (C11) is at most

    (2pi C_rho/c_G) |sin K_a| E^3.                (C12)

For |K|<=E/4 and E<=E*, this is the O(E^4) asymptotic packet-current
bound (20). Equations (C7)-(C9) state the extra finite-time errors; their
packet constants remain explicit until the construction below bounds them.

## 16. Normalizable center-of-mass packets

The finite-time statements extend to a normalizable direct-integral packet
without claiming global trace-class scattering. Let the total-momentum
fibers vary measurably over a coordinate patch, with the packet zero outside
that patch. Use normalized total-momentum measure dK. Take a measurable
field psi_K in P_ac(H0(K)) with integral ||psi_K||^2 dK=1. Individual
psi_K need not be normalized. Define the linear density b_(K,psi) and the
homogeneous seminorms A_r(K,psi), D_r(K,psi) as above, and assume A_r and D_r
are in L2(dK). Require the analogous
D_r(K,phi) bound for phi_K=S_K psi_K.

The fiberwise wave operators form measurable fields: they are pointwise
strong limits of measurable bounded operator fields along integer times.
Fiberwise strong convergence and the bound 2||psi_K|| give convergence in
the direct-integral Hilbert space by dominated convergence. The resulting
Omega operators are isometries between the direct integrals of the fiber
absolutely continuous spaces, and satisfy Omega_-=Omega_+ S on that domain.
This does not identify their ranges with the full absolutely continuous
space of the global H: dispersing fiber-bound states need not belong to
that range.

Let P now denote the direct integral of the contact complements, and prepare

    Eta_- = P exp(iTH0)Psi / ||P exp(iTH0)Psi||

using one global normalization. The removed-contact norm is at most
||A_r(.,psi)||_(L2_K)/T^r. Integrate the squared pointwise Cook bound and
then take a square root. Equations (C7) and (C8) hold verbatim with

    A_r(psi) -> ||A_r(.,psi)||_(L2_K),
    D_r(psi) -> ||D_r(.,psi)||_(L2_K),
    D_r(phi) -> ||D_r(.,phi)||_(L2_K),

and the essential supremum of the fiber observable norms. The preparation
requires the actual removed-contact norm to be less than one; the displayed
upper bound gives a sufficient condition. There is no fiber-by-fiber
renormalization. The global projection does reweight total momentum: if
p=integral |a_(K,psi)(-T)|^2 dK, its new density is
(||psi_K||^2-|a_(K,psi)(-T)|^2)/(1-p). Its total-variation distance from
the original K density is at most p, since the original is the mixture
of the normalized surviving and removed-contact densities with weights
1-p and p. Here p<=||A_r(.,psi)||_(L2_K)^2/T^(2r). This preparation effect
is already included in (C6)-(C8); unchanged total-momentum weights are not
assumed.

For (C9), take measurable finite-rank form factors and replace F_r(chi) by
integral F_r(K,chi) dK and ||M|| by ess sup_K ||M_K||. Its proof is the
same integrated quadratic bound. Likewise the asymptotic packet-current
estimate is the essential supremum of (C11) over (K,E) on the actual packet
support. All corner/channel and regularity restrictions remain in force.


## Coherent finite-time witness

The construction gives normalized smooth incoming packets whose asymptotic
canonical energy-current change is

    Delta J_asym = -epsilon C lambda^4 + O(lambda^5), C>0,

and actual excluded initial states at time -T, T=lambda^(-3/2), whose current
change by +T is

    Delta J_finite = -epsilon C lambda^4 + O(lambda^(9/2)).       (P1)

Here epsilon=+1 or -1 is an explicitly chosen relative coherent phase.
Changing it reverses the leading sign. This is a signed two-body coherent
current change, not dissipation, a many-body relaxation rate, or a statement
that every incoming packet changes current.

## 17. Model, regular region and analytic inputs

Use normalized relative-momentum measure dq/(2pi)^3 and normalized total-
momentum measure dK/(2pi)^3 in a local K chart. In each antisymmetric fiber,

    H0(K,q)=sigma_1 dot sin(K/2+q)+sigma_2 dot sin(K/2-q).

Let c be the normalized constant singlet, C0=|c><c| and P=I-C0. The full-fiber
extension H=PH0P is zero on c; its restriction to P is the excluded walk. Put

    h=H0c, h'_a=partial_(K_a)h,
    H-H0=-|h><c|-|c><h|,
    ||h||<=sqrt(6),
    h'_a(q)=-sin(K_a/2) sin q_a sigma_(1,a)c.                (P2)

The canonical placement is e_x=P[(1/2)sum_i{Pi_(i,x),h_i}]P. Its energy
dipole has the bounded commutator extension

    J_a=P g_a P+F_a,   g_a(K,q)=sin K_a cos(2q_a),
    F_a=-|h'_a><h|-|h><h'_a|,
    ||F_a||<=2sqrt(3)|sin(K_a/2)|.                         (P3)

This is the specified canonical current, not a claim for all local-energy
placements. With J_ext=g_a+F_a, its operator on the excluded space is
P J_ext P. Thus their expectations agree on vectors in P; J_ext itself
need not preserve that subspace.

The central region 0<E<=1/8, |K|<=E/4 contains only the positive-positive
free channel. Its eight relative-momentum corner shells are q=C_j+r n,
C_j in {0,pi}^3, n in S^2. There is one radial root, with

    E/4<=r<=E,   1/2<=partial_r E_(++)<=2,
    1/4<=w_(++)=<c,Pi_(++)c><=1/2.                       (P4)

Let G(K,E+i0)=<c,(H0-E-i0)^(-1)c> and rho=Im(G)/pi. On each compact
scaled region with E=lambda e, K=lambda kappa, e>0, |kappa|<e/4, Sections 3-5 give

    rho(lambda kappa,lambda e)=lambda^2 r_lambda(kappa,e),
    r_lambda=r_0+O(lambda^2), r_0=(e^2-|kappa|^2)/(4pi^2),
    G(lambda kappa,lambda e+i0)/lambda=A(kappa,e)+O(lambda), (P5)

with the displayed remainder bounds after any fixed finite number of
derivatives in the scaled parameters. In particular they hold through order
seven on the compact set selected below. Here

    A=e integral [(e^2-|kappa odot cos q|^2)
          / (4 eps(q)^2 (e^2-(kappa dot v(q))^2))] dq/(2pi)^3,
    eps(q)=|sin q|, v_j(q)=sin q_j cos q_j/eps(q),
    I0=integral dq/[(2pi)^3 4 eps(q)^2],
    e(1-|kappa|^2/e^2) I0<=A<=e I0.                    (P6)

The measure-zero cone points do not affect these integrals; I0 is finite in
three dimensions. Equation (13) supplies an E_*>0 for which
Re G>=5E/128 on 0<E<=E_*, |K|<=E/4. E_* has not been numerically certified.

For the convention S=Omega_+^*Omega_- and resolvent (H0-z)^(-1), the regular
shell scattering operator is

    S_(K,E)=I+(s-1)|v><v|,
    v=Z_(K,E)c/sqrt(rho), s=conj(G)/G.                  (P7)

Z is the coarea spectral restriction described below. The representative
(P7) is smooth on a regular interval; equality almost everywhere in energy
suffices for the packet. The contact zero eigenstate of H is not included
in the incoming free absolutely continuous space.

## 18. A compact domain and smooth normalized shell vectors

Take a=1; permutation gives either other component. Fix

    kappa_0=(1/8,0,0), R=1/32,
    U={kappa: |kappa-kappa_0|<R}, I=(5/4,7/4).

On the closures,

    3/32<=kappa_1<=5/32, |kappa|<=5/32,
    D=e^2-|kappa|^2>=D_min=1575/1024,
    beta=D+kappa_1^2>=D_min.                            (P8)

Thus the domain lies strictly inside |kappa|<e/4. For lambda<=1/16 it also
satisfies |K|<=lambda/4 and lambda<E<2lambda. Decrease a positive lambda_0
as needed so E<=E_* and the variance bound below holds. Every statement
from now on is for 0<lambda<=lambda_0.

For clarity use a fixed shell Hilbert space: the eight copies of
L2(S^2,C^4,dOmega/(2pi)^3), restricted to the positive band and the exchange-
antisymmetric subspace. Write r=lambda R_lambda(kappa,e,n). The physical
coarea restriction in these coordinates is

    (Z_(K,E)F)(j,n)=[r/sqrt(partial_r E_(++))]
                                  Pi_(++)(K,C_j+r n)F(C_j+r n). (P9)

On this positive spectral interval it is an isometry after integration over dE. The exchange constraint is
inherited from the original full-q-torus antisymmetric space; no additional
factor of two or half-torus convention is introduced.

The implicit root R_lambda and the projectors are smooth in lambda^2,
kappa,e,n on this domain. At the limiting shell both one-particle momenta
have norm at least (e-|kappa|)/2>0; (P4) gives a uniform radial derivative.
The implicit-function theorem therefore applies uniformly. It follows that

    Zc=lambda z_(c,lambda),
    v_lambda=z_(c,lambda)/sqrt(r_lambda)                  (P10)

has uniformly bounded derivatives of each fixed order in the scaled
parameters. Positive contact weight avoids a spinor gauge choice: Pi_(++)c
is a globally defined nonzero section on each shell. Also v_lambda is a
unit vector in the antisymmetric shell space.

Remove the shell-constant part of g_1 and define a stable scaled multiplier

    gamma_lambda=(g_1-sin(lambda kappa_1))/lambda^3
       =-2 [sin(lambda kappa_1)/lambda]
                    [sin(lambda R_lambda n_1)/lambda]^2,
    m_lambda=<v_lambda,gamma_lambda v_lambda>,
    d_lambda^2=<(gamma_lambda-m_lambda)^2>_(v_lambda).      (P11)

These expressions extend smoothly to lambda=0 as functions of lambda^2.
Once d_lambda>0, set

    u_lambda=(gamma_lambda-m_lambda)v_lambda/d_lambda,
    chi_(lambda,epsilon)=(v_lambda+i epsilon u_lambda)/sqrt(2),
    chi_out=(s v_lambda+i epsilon u_lambda)/sqrt(2).        (P12)

Here epsilon is either +1 or -1. Both shell vectors have unit norm;
<v_lambda,u_lambda>=0. Multiplication by g_1 preserves exchange antisymmetry.
Equation (P7) gives exactly S chi=chi_out. The strictly positive variance
and the uniform smoothness of u are proved next, not assumed.

## 19. Exact limiting contact measure and angular variance

On one limiting continuum cone put p=kappa/2+y, so the second momentum is
kappa-p. The limiting shell and contact weight are

    |p|+|kappa-p|=e,
    w_0=D/[8|p||kappa-p|].                              (P13)

Let k=|kappa|>0. In prolate coordinates
u=(|p|+|kappa-p|)/k, v_p=(|p|-|kappa-p|)/k and azimuth phi, the volume
Jacobian is k^3(u^2-v_p^2)/8 and the product of the two radii is
k^2(u^2-v_p^2)/4. Multiplying by w_0 and delta(e-ku) leaves
D dv_p dphi/16. Consequently the normalized contact angular measure is
dv_p dphi/(4pi), with weight 1/8 at each of the eight cones. This also
rederives r_0=D/(4pi^2), including the torus normalization.

Under this probability measure,

    y=T n, n uniform on S^2,
    T^2=[D I+kappa kappa^T]/4.                           (P14)

Indeed y_parallel=e v_p/2 and
|y_perpendicular|=sqrt(D)sqrt(1-v_p^2)/2. Since the squared length of
row 1 of T is beta/4, the uniform-sphere moments give

    <y_1^2>=beta/12, <y_1^4>=beta^2/80,
    Var(y_1^2)=beta^2/180.                               (P15)

For example these follow from <n_1^2>=1/3, <n_1^4>=1/5 and rotational
invariance, or directly from the displayed v_p,phi measure. Since
gamma_0=-2 kappa_1 y_1^2, (P11) yields

    d_0=kappa_1 beta/(3sqrt(5))
        >=d_min:=D_min/(32sqrt(5))>0,
    d_lambda=d_0+O(lambda^2).                            (P16)

All finite-order scaled derivatives have the same smoothness just used in
(P9)-(P11). An explicit way to choose the remaining variance restriction
is to let C_V be the supremum of
|partial_(lambda^2) Var_(v_lambda)(gamma_lambda)| over the compact domain
0<=lambda<=1/16, closure(U) times closure(I). This constant is finite before
taking a variance square root. Choose additionally
lambda_0<=d_min/sqrt(2C_V), interpreting that restriction as absent if C_V=0.
Then d_lambda>=d_min/sqrt(2). Thus u_lambda and chi have uniform scaled
derivative bounds, including through order seven. This proves that the
normalization in (P12) is legitimate everywhere on the packet support.

## 20. Exact coherent sign and leading shell change

Write sigma_lambda=sqrt(Var_v(g_1))=lambda^3 d_lambda. The exact rank-one
calculation in the v,u basis gives

    S^*g_1 S-g_1
       =sigma_lambda[(s-1)|u><v|+(conj(s)-1)|v><u|],
    <chi_(lambda,epsilon),(S^*g_1 S-g_1)chi_(lambda,epsilon)>
       =epsilon sigma_lambda Im(s).                     (P17)

For this sign convention,

    Im(s)=-2 Re(G) Im(G)/|G|^2<0,
    Im(s)=-2pi lambda r_0/A+O(lambda^2).                  (P18)

Using (P5) and (P16), uniformly on the selected domain,

    epsilon sigma_lambda Im(s)
       =-epsilon lambda^4 c_*(kappa,e)+O(lambda^5),
    c_*(kappa,e)=kappa_1 beta D/[6pi sqrt(5) A(kappa,e)]>0. (P19)

This fixes both the sign and the normalization; using the opposite convention
for the resolvent or S without changing the sign here would be an error.

There is a simple explicit lower bound for the coefficient. Fold the q torus
to eight copies of [-pi/2,pi/2]^3 and use |sin x|>=2|x|/pi on that cube.
The cube lies in the ball of radius sqrt(3)pi/2, so

    I0 <= (1/pi^3)(pi^2/16) integral_(|x|<=sqrt(3)pi/2) |x|^-2 dx
       =sqrt(3)pi/8.

Equations (P6) and (P8) then imply

    c_*(kappa,e)>=c_min:=D_min^2/[14pi^2 sqrt(15)]>0.       (P20)

The pure contact vector v is an exact zero-change control: S only multiplies
it by a phase. Its nonzero scattering phase alone cannot produce the claimed
current expectation change. The interference with u in (P12) is essential.

## 21. One actual normalizable incoming packet

Choose the following real smooth bump envelopes, extended by zero:

    alpha(kappa)=N_K exp[-1/(1-|kappa-kappa_0|^2/R^2)] in U,
    f(e)=N_E exp[-1/(1-16(e-3/2)^2)] in I.

The positive normalizers are defined by

    integral |alpha|^2 d^3kappa/(2pi)^3=1,
    integral |f|^2 de=1.                                 (P21)

In the shell spectral representation with measure dK/(2pi)^3 dE, set

    Psi_(lambda,epsilon)(K,E)
       =lambda^-2 alpha(K/lambda) f(E/lambda)
                             chi_(lambda,epsilon)(K/lambda,E/lambda).
                                                               (P22)

The norm is exactly one: the squared amplitude contributes lambda^-4,
the K measure contributes lambda^3 and the E measure contributes lambda.
There is no normalization of individual K fibers; they have norm
lambda^(-3/2)|alpha(K/lambda)|. Formula (P9), inverted on its positive-band
range, constructs the corresponding free two-record vector. It is in the
free fiberwise absolutely continuous space, supported inside the eight
regular shell neighborhoods and in the selected K chart.

For each lambda>0 the incoming vector is smooth in momentum. The chart
Jacobian is nonsingular on its support, the projectors and u are smooth,
and the bump envelopes vanish with every derivative at their support
boundaries. Thus this is a smooth normalizable packet, not a delta function
in K or energy. Define Phi=S Psi by replacing chi with chi_out in (P22).

Finite-rank F_1 has vanishing free asymptotic expectation on these packets:
its scalar spectral densities are L1, and the Riemann-Lebesgue lemma applies
fiberwise. Dominated convergence integrates the statement over K; wave-
operator norm convergence transfers it to the actual scattering states.
Therefore the canonical current has the same asymptotic change as g_1.
Equations (P17)-(P22) give

    Delta J_asym=-epsilon lambda^4 C+O(lambda^5),
    C=integral |alpha(kappa)|^2 |f(e)|^2 c_*(kappa,e)
                                      d^3kappa/(2pi)^3 de >=c_min. (P23)

The coefficient is independent of lambda and epsilon. No assumption about
incoherent angular averaging has been made; the constructed state is coherent.

## 22. Scaled Cook and canonical form-factor seminorms

This section verifies the regularity needed for a finite-time witness,
including both canonical form factors. It does not infer their bounds merely
from the contact density. All inner products below are in the fixed shell
space of (P9), linear in the second argument.

Put r_lambda=rho/lambda^2 as above and define, for b=in,out,

    B_0^in=f sqrt(r_lambda)/sqrt(2),
    B_0^out=s B_0^in,
    B_1^b=e B_0^b.                                      (P24)

The contact scalar densities of the full packet at K=lambda kappa,E=lambda e
are exactly

    b_(c,b)=lambda^-1 alpha(kappa) B_0^b,
    b_(h,b)=alpha(kappa) B_1^b.                          (P25)

For example the first identity is the product of Zc=lambda sqrt(r_lambda)v
with the lambda^-2 packet amplitude and <v,chi>=1/sqrt(2). For the outgoing
packet this last inner product is s/sqrt(2). The second identity uses
Z h=E Z c, rather than an independent approximation.

For h'_1 the pointwise formula (P2) on q=C_j+lambda R_lambda n has two
small sine factors. Combining it with the coarea factor in (P9) proves

    Z h'_1=lambda^3 zeta'_lambda,
    zeta'_lambda uniformly smooth in the scaled parameters,
    B_2^in=f <zeta'_lambda,chi>,
    B_2^out=f <zeta'_lambda,chi_out>,
    b_(h'_1,b)=lambda alpha(kappa) B_2^b.                 (P26)

Here zeta' is notation for this scaled form factor, not another derivative.
The formula also retains the corner signs and projectors; a bound on |sin q_1|
alone would not prove the required derivative regularity.

For each integer 0<=r<=7 define explicit finite mixed-norm constants

    C_(j,r)^b(lambda)
       = [integral_U |alpha(kappa)|^2
             (integral_R |partial_e^r B_j^b(lambda,kappa,e)| de)^2
                                      d^3kappa/(2pi)^3]^(1/2),
    bar C_(j,r)^b=sup_(0<lambda<=lambda_0,epsilon=+/-1) C_(j,r)^b(lambda).
                                                               (P27)

All B_j are extended by zero in e. Their compact smooth envelope gives the
vanishing endpoint traces. Equations (P9)-(P16), (P24)-(P26) and the order-seven
part of (P5) prove finiteness. More explicitly, G/lambda has a uniform positive
real-part lower bound, and

    s=1-2pi i lambda r_lambda/(G/lambda),                 (P28)

so product/quotient differentiation bounds each of its first seven scaled
e derivatives. Uniform smallness of s-1 without these derivative estimates
would not suffice.

The constants in (P27) are specified functionals, not numerically evaluated
uniform bounds. If numerical upper bounds are desired, the following direct
product-rule bounds reduce them to finitely many compact suprema. Let

    M_j^in=sup |partial_e^j sqrt(r_lambda)|,
    M_j^out=sup |partial_e^j(s sqrt(r_lambda))|,
    Z_j=sup ||partial_e^j zeta'_lambda||,
    X_j^b=sup ||partial_e^j chi_b||,
    H_j^b=sum_(l=0)^j binom(j,l) Z_l X_(j-l)^b,

where each supremum is over the same compact domain and chi_in=chi. Then

    bar C_(0,r)^b <= (1/sqrt(2)) sum_(j=0)^r binom(r,j)
                                          ||f^(r-j)||_1 M_j^b,
    bar C_(1,r)^b <= (7/4) bar C_(0,r)^b+r bar C_(0,r-1)^b,
    bar C_(2,r)^b <= sum_(j=0)^r binom(r,j)||f^(r-j)||_1 H_j^b. (P29)

The middle formula is for r>=1, with the evident r=0 bound. These constants
are independent of lambda and epsilon. No uniform bound in derivative order
is asserted.

Let A_r(K,b)=||partial_E^r b_(c,b)||_(L1_E) and
D_r(K,b)=||h(K)|| A_r(K,b)+||partial_E^r b_(h,b)||_(L1_E), as in Section 12. A change of variables E=lambda e, K=lambda kappa proves

    ||A_r(.,b)||_(L2_K)=lambda^(3/2-r) C_(0,r)^b(lambda),
    ||D_r(.,b)||_(L2_K)
       <=lambda^(3/2-r)[sqrt(6) C_(0,r)^b(lambda)
                                      +lambda C_(1,r)^b(lambda)]. (P30)

For the canonical finite-rank correction choose columns (h,h'_1) and
M=[[0,-1],[-1,0]], so ||M||=1. Its integrated C9 seminorm is exactly

    F_r(b)=integral [||partial_E^r b_(h,b)||_1^2
                          +||partial_E^r b_(h'_1,b)||_1^2] dK/(2pi)^3
       =lambda^(5-2r) [C_(1,r)^b(lambda)]^2
                         +lambda^(7-2r) [C_(2,r)^b(lambda)]^2.  (P31)

The extra lambda^3 in this integral is the total-momentum volume factor.
Using normalized individual fibers without restoring that factor would
give incorrect global seminorm powers.

## 23. An actual finite-time nonzero canonical-current witness

Set r=7 and T=lambda^(-3/2). Define finite constants

    D_bar=sqrt(6)(bar C_(0,7)^in+bar C_(0,7)^out)
                        +lambda_0(bar C_(1,7)^in+bar C_(1,7)^out),
    J_0=(1+sqrt(3)) 5/32.

Prepare and evolve the actual excluded state by one global normalization:

    Eta_-=P exp(iT H0)Psi / ||P exp(iT H0)Psi||,
    Eta_+=exp(-2iT H)Eta_-.                              (P32)

Its removed probability obeys

    p=||C0 exp(iT H0)Psi||^2
       <=[bar C_(0,7)^in]^2 lambda^10.                   (P33)

Take lambda small enough that this is less than one. In particular, the
preparation changes total-momentum weights: the normalized new density is
(||Psi_K||^2-|<c,exp(iT H0(K))Psi_K>|^2)/(1-p). Its total-variation distance
from the original K density is at most p. Neither unchanged K weights nor
fiberwise renormalization is assumed in (P32).

The integrated incoming-plus-outgoing Cook tail is at most
(D_bar/6)lambda^(7/2), and the projection norm cost is at most
sqrt(2) bar C_(0,7)^in lambda^5. On this K support, (P3) gives

    ||J_ext|| <= J_0 lambda.                             (P34)

This norm bound is global in q, so it covers components outside the original
free energy band introduced by P. Applying the (C8)-(C9) endpoint comparison
with (P30)-(P34) yields the explicit estimate

    | <Eta_+,J_1 Eta_+>-<Eta_-,J_1 Eta_->-Delta J_asym |
       <= (J_0 D_bar/3) lambda^(9/2)
          +4sqrt(2) J_0 bar C_(0,7)^in lambda^6
          +([bar C_(1,7)^in]^2+[bar C_(1,7)^out]^2) lambda^12
          +([bar C_(2,7)^in]^2+[bar C_(2,7)^out]^2) lambda^14. (P35)

The last two terms explicitly control the canonical h,h'_1 correction at
the free endpoints. Its qualitative asymptotic disappearance alone would
not justify a finite-time leading coefficient.

Combining (P23) and (P35) proves (P1). More quantitatively, choose C_asym
so the uniform integrated remainder in (P23) is at most C_asym lambda^5.
Let C_tot be C_asym plus the four coefficients on the right of (P35).
For lambda<=1 they bound the combined error by C_tot lambda^(9/2).
It is enough to impose, in addition to the prior restrictions,

    [bar C_(0,7)^in]^2 lambda^10 <=1/2,
    sqrt(lambda) C_tot <= c_min/2.                       (P36)

Such a positive range exists because all constants are finite and c_min>0.
It gives the genuinely nonzero finite-time statement

    -epsilon [<Eta_+,J_1 Eta_+>-<Eta_-,J_1 Eta_->]
                      >= (c_min/2)lambda^4>0.            (P37)

For epsilon=+1 the current decreases; for epsilon=-1 it increases. The
experiment has duration 2lambda^(-3/2) in the supplied clock and concerns
this prepared two-record family. It establishes no irreversible trend.


## 24. Verification, failure controls and claim boundary

The [evidence record](../.claude/science/physics-loops/toe-excluded-walk-20261011/evidence/README.md)
preserves the original threshold, Cook and canonical drafts, source-bound
selective reviews, independently written controls, exact source identities,
and raw logs. The combined source and coherent extension received a separate
source-bound review of the coefficient, normalization, outgoing regularity and
finite-preparation estimates; no consequential defect remained after the stated
compression wording correction. None of these records is an applied
retained-status audit or a Lean certificate.

The primary runner performs exact Gaussian-rational inversions and finite
compression/stationary identities; exact Laurent convolution retains arbitrary
K-derivative jets in the canonical commutator; continuum angular moments and
coherent phases are checked algebraically. Its deterministic lattice-shell
quadrature is a finite numerical control, not an interval proof of the
principal value or uniform threshold expansion. Twelve actual altered primary
sources fail at their intended scientific assertions. The independent records
also preserve a symbolic all-vector resolvent identity, a separately derived
continuum coarea coefficient, explicit absolutely-continuous Fourier tails,
and finite-dimensional unitary comparisons with their stated limitations.

Two invalid shortcuts remain explicit. A pure contact-channel packet has zero
asymptotic current expectation change despite its nonzero scattering phase.
Six derivatives at T=lambda^(-3/2) only bound the finite-time current error at
the same order as the desired coefficient. The coherent interference and
seven-derivative, two-form-factor calculation above supply the required steps.
Global contact preparation changes K weights by at most its removed mass;
it does not keep them exactly fixed. A literal restriction of g+F is not used
when that extension fails to preserve P: the physical operator is P(g+F)P.

The conclusions concern the supplied central three-dimensional two-record
model and its specified canonical energy placement. Other total corners,
open mixed channels, two-dimensional thresholds, arbitrary placements,
many-body transport, physical rates and native-law selection are outside this
theorem. The two coherent signs prohibit interpreting the witness as a
universal tendency to lose current. The existence of a sufficiently small
range is proved through finite analytic constants; no maximal numerical E*
or lambda interval is certified.

Potential scoped Lean audit obligations include the finite Pauli/compression
identities, shell/coarea constants, and the parameter-dependent subtracted
Cauchy integral with its imported scattering interface. No Lean execution is
claimed. These new derivations are admissible research in the repository;
formal retained status remains a separate independent audit decision.
