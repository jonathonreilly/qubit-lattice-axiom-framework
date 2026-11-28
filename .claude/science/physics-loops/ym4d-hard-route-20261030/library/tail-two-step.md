State of attack

**Gap — test complete; verdict undecided at (42)–(43) below.** The frozen target is (GROUP), Lemma 4.7j, labelled stage (ii), and (BANACH) in `parts/hard-core--independent.md`, in the filtered copy identified by the user as commit `45a9f59f9`. No definition has been repaired. The shared-label Gaussian budgets can be made consistent under the stated inputs. The normalized mixed field/site coefficient of one old factor has not been bounded with the asserted contraction, and no coefficient violating that contraction has been exhibited. The exact coefficient is (35)–(37), with crude size (39); its source insertion is (44)–(46).

**Discharged — procedure.** Read `GOAL.md` and `FINISH-rules.md` first. Only this directory has been read. Only this report has been written. No numerical job, machine enumeration, subagent, git operation, or external lookup has been used. Only written mathematical checks are claimed below. Provenance: OpenAI Codex, GPT-6 family; this is a mathematical kill test, not an audit or a claim of independent model verification. The commit identifier is supplied by the user.

**Discharged — reading boundary.** Located the frozen norm (TAIL), the two-centre coordinate, (GROUP), Lemma 4.7j, both integration stages, (ONE), and (BANACH). Read the previous independent-side gate named in the task. The main file expressly assumes, rather than proves in §3.1a, the polynomial envelopes needed for its order of constants. No quoted numerical PASS in the draft is evidence in this report.

**Implication — coefficient bookkeeping.** Introduce formal activity markers `a,b` on two old factors with overlapping near-noise sets. Their coefficient `ab` belongs to one group; their coefficients `a` and `b` each have one old factor and must retain the smoothing contraction. Put one far field variable `w` and one idempotent site variable `h` (`h²=h`) in the coefficient algebra. The relevant mixed coefficient is `[a w^n h]`, including `n=0`; all integrations must use the same Gaussian density once.

**Unchecked — current bottleneck.** The scalar Gaussian budgets below are compatible. They do not prove the coefficient estimate for the normalized one-factor integral. The bottleneck is the mixed field/site coefficient of that integral after the marginal quadratic form is subtracted. No counterexample to that coefficient estimate has been established.

**Discharged — notation for the frozen test.** Write I for `parts/hard-core--independent.md`. Work on a finite torus, at two consecutive levels, indexed by `j=0,1`; these mean `k,k+1`, not a new RG definition. Each level has two integrations, over the local noise and over its spectator. Use `a,b` for activity markers, `w` for one Lie-algebra component of one far coarse link, `h` for one allowed far site, and `f` for a source marker. The site algebra is

\[
 H(w,h)=H_0(w)+h\{H_1(w)-H_0(w)\},\qquad h^2=h.
 \tag{1}
\]

Thus `[w^n h]H=[w^n](H_1-H_0)`, not a derivative through an interpolating region. Write `H_{n,0}=[w^n]H₀` and `H_{n,1}=[w^n](H₁−H₀)`. The coefficient norm is precisely the restriction of (TAIL):

\[
 \|H\|_{A,R}=
 \sum_{n\geq0}\rho_R(c)^n
 \left(e^{c_3\tau(A;\{c:n>0\})}|H_{n,0}|
 +e^{c_3\tau(A;\{c:n>0\},S)}|H_{n,1}|\right).
 \tag{2}
\]

Here `S` is the site, and the empty field support is used at `n=0`. Multiplying two series and using the union of their trees proves submultiplicativity: every coefficient of a product is a convolution, and `h²=h` only merges terms. This does not replace an all-site estimate by an estimate at the two real site states.

**Discharged — the actual two-centre integrand, before estimation.** For either site state, at fixed spectator `η=ξ′`, put

\[
 s_j=s_{J,j}+\sqrt2 R_j(G_{1,j}\eta_1+G_{2,j}\eta_2),\quad
 x_i=\begin{cases}x_i,&i\in K,\\ \xi_i+s_{j,i}(W,\eta),&i\notin K,\end{cases}
 \quad b_j={g_j\over\sqrt2}P_jx.
 \tag{3}
\]

`K` is the union of the near-noise sets of the chosen old factors. There is no G label and no bad cube in the tested activity. The exact near-label measure is

\[
 \prod_{i\in K}{\bf1}_{|x_i|\leq p_{2,j}}
 \phi_3(x_i-s_{j,i}(W,\eta))\,d^3x_i;
 \qquad
 \prod_{i\notin K}{\bf1}_{|\xi_i|\leq p_j}\phi_3(\xi_i)\,d^3\xi_i
 \tag{4}
\]

on the other local labels, together with the good spectator cuts and its product Gaussian. Here `φ₃(t)=(2π)^{-3/2}exp(-|t|²/2)`. The field inserted in the old factors is the actual chart `V_j(W,x)`, including its fibre correction; its origin is `V_j^#`, not `V_j^*`. The analytic weight is `A_j=exp Ψ_j`, where `Ψ_j` is the action remainder and the analytic, Jacobian and Faddeev–Popov terms of I:636–646,793,857. For a source it is `A_j exp I_j^f`, with `I_j^f` exactly as in I:1170–1175. Equations (3)–(4) are a substitution of the frozen definitions. They make no claim that the chart or its bounds have been reconstructed.

**Discharged — one shared label is integrated once.** Let `F_P,F_Q` denote the two selected old factors. For a fixed choice of all other local variables their contribution has the form

\[
 \int d\mu'(\eta)\int_{|x_i|\leq p_2}
 \phi_3(x_i-s_i(W,\eta))\,
 A(W,x,\eta)\,F_P(V(W,x))F_Q(V(W,x))\,d^3x_i,
 \tag{5}
\]

with the integrations of (4) on the remaining variables implicit. There is one Gaussian in (5), even when the label occurs in both factors. If `i∈NV(Z_P)∩NV(Z_Q)`, (GROUP) puts the two factors in a single group with `U=N₁(Z_P)∪N₁(Z_Q)`. At fixed real `x_i`, their near data are real by (LOCAL) and (R2); moving `x_i` through its entire cut changes their real base. If `i∈NV(Z_Q)\NV(Z_P)` but enters the analytic tail of P, the two factors need not be in one group. In that case Lemma 4.7j must localize P's reading of this very same variable. These two cases must not be conflated.

**Discharged — markers separate the linear coefficient.** Denote by `J_j^K(H)` the unnormalized integral (3)–(4), with integrand `A_j H`, and by `N_j=J_j^∅(1)` the good denominator. Expansion of the selected factors gives

\[
 \begin{split}
 Z_j(a,b)/N_j={}&1+a\,{J_j^{K_P}(e_P)\over N_j}
 +b\,{J_j^{K_Q}(e_Q)\over N_j}
 +ab\,{J_j^{K_P\cup K_Q}(e_Pe_Q)\over N_j}
 +O(a^2,b^2),\\
 [a]\log Z_j={}&{J_j^{K_P}(e_P)\over N_j},\\
 [ab]\log Z_j={}&{J_j^{K_P\cup K_Q}(e_Pe_Q)\over N_j}
 -{J_j^{K_P}(e_P)J_j^{K_Q}(e_Q)\over N_j^2}.
 \end{split}\tag{6}
\]

These identities follow by multiplying the marker series and the series `log(1+z)=z-z²/2+…`. The relevant coefficient of `exp(ae_P)-1` is `e_P`. In particular, the second old activity never multiplies `[a]log Z_j`. Normalizing `J_j^{K_P}` separately gives exactly the ratio in (ONE), not its omission:

\[
 {J_j^{K_P}(e_P)\over N_j}
 ={J_j^{K_P}(1)\over N_j}\,\Gamma_j^P,
 \qquad \Gamma_j^P={J_j^{K_P}(e_P)\over J_j^{K_P}(1)}.
 \tag{7}
\]

**Implication — real-base growth, retained in (5).** Assuming the input (TAIL) bound at the actual real base `V^t`, set `D_P^+=D(P)+2r_e` and `ω_P=exp[-κ(|P|-160)_+]`. Before taking any supremum the old C factor has the majorant

\[
 c_P(V^t)=2cc_j\,\omega_P\,[T_P(V^t)^2+T_P(V^t)^3],\quad
 T_P=\max\left\{{(D_P^+)^2\over g_j}
 \sup_z e^{-c_1d(z,P)/2}|F_z(V^t)|,\ t_{{\rm fl},P}\right\}.
 \tag{8}
\]

For SU(2), `|U−1|≤2` follows from the triangle inequality and `|U|=|1|=1` in operator norm. Thus, for small `g_j` so that the stated floor is below `2(D_P^+)²/g_j`,

\[
 c_P(V^t)\leq 24\,cc_j g_j^{-3}(D_P^+)^6\omega_P
 =:\widehat c_P.
 \tag{9}
\]

The constant 24 includes the factor 2 allowed in (TAIL): `T²+T³≤4D⁴/g²+8D⁶/g³≤12D⁶/g³` for `D=D_P^+≥1`, `g≤1`. It is uniform over the real range of the shared label and all real bases. Therefore the two-factor integrand in (5) is bounded by `ĉ_Pĉ_Q` times its remaining weight. This is a bound on their product at one base, not a product of separately integrated moments.

**Discharged — the diameter envelope in (9).** A connected n-cube support has diameter at most `ML n` (the deliberately loose frozen bound). Hence

\[
 (D_P^+)^6\leq(ML+2r_e)^6n^6,
 \qquad
 n^6e^{-\kappa(n-160)_+/2}
 \leq\left(160+{12\over\kappa}\right)^6.
 \tag{10}
\]

For the second inequality put `x=(n−160)_+`. The function `(160+x)exp(−κx/12)` attains its maximum either at zero or where `160+x=12/κ`; its maximum is at most `160+12/κ`, and take its sixth power. This proves the half-weight version of (CRUDE), without dropping a power of the diameter. If `r_e=O(log L)` and `M=O((log L)^5)` as stipulated, (10) is polynomial in L. The bound involves no region size, depth, or cap radius. This derivation does not prove the chart envelopes in §3.1a.

**Implication — moving the unsplit label all the way to p₂.** At a real good spectator, the stipulated centre bounds give

\[
 |s_i(0,\eta)|\leq p_2/32+p/2,
 \quad |x_i|\leq p_2,
 \quad |t_i|:=|x_i-s_i(0,\eta)|\leq2p_2
 \tag{11}
\]

when `p≤p₂/2`. The relevant far-noise threshold is exactly

\[
 A_P(c)={\min(\rho_e/g,\ c'e^{c_1d_k(l,U_P)})\over128C_{\rm row}}-1,
 \tag{12}
\]

with the minimum over links read by that cube. At the cap, the frozen choice `2p₂+1≤ρ_e/(128C_row g)` implies `|t_i|≤A_P(c)`; no large state occurs there. On a cube actually in `Lg_P`, the cap therefore cannot be the active obstruction, and

\[
 A_P(c)={c'\over128C_{\rm row}}e^{c_1d_k(l,U_P)}-1,
 \quad d_k(l,U_P)\geq LR_{\rm loc}.
 \tag{13}
\]

The unconditional lower bound by the uncapped exponential in I:886 is not literally true at capped cubes. Equations (12)–(13) give the valid restricted reading used here. For `a_P(c)≤1/4`, the Möbius factor is `4a_P(c)≤1`; above it the factor is 2 and must be integrated on `|t_i|>A_P(c)`. Moving the shared label up to `p₂` does not require a deterministic `log p` enlargement under this conditional bound. It does not establish the mixed-coefficient hypothesis in Lemma 4.7j(b).

**Implication — lower threshold.** If `(c′/(128C_row))exp(c₁LR_loc)≥2`, (13) gives `A_P(c)≥A_sharp`, where `A_sharp=(c′/(256C_row))exp(c₁LR_loc)`. This is the g-independent threshold used in (18).

**Discharged — a single Gaussian budget.** Put `σ_i=s_i(w,h)−s_i(0,0)`, and assume its coefficient norm is at most `a_i`. Expansion of the Gaussian exponential gives

\[
 \|\phi_3(t_i-\sigma_i)\|\leq
 \phi_3(t_i)\exp\left(a_i\sum_{\nu=1}^3|t_i^\nu|+{3a_i^2\over2}\right).
 \tag{14}
\]

Indeed the norm of `t_i·σ_i−σ_i·σ_i/2` is at most the displayed exponent, and the exponential series is bounded by the exponential of that norm. If the complete family exponent from (FAM) is `qU`, `q≤1/16`, where `U=Σ_i|t_i|²`, and all large-label attachment factors together cost at most `exp(U/12)`, then, using `a|t|≤|t|²/16+4a²` component by component, the *entire* exponent is at most

\[
 -\tfrac12 U+\tfrac1{16}U+\tfrac1{16}U+\tfrac1{12}U
 +\tfrac{27}{2}\sum_i a_i^2
 =-\tfrac7{24}U+\tfrac{27}{2}\sum_i a_i^2.
 \tag{15}
\]

Thus the product of the two old C majorants and every term charged here obeys the displayed integrand bound

\[
 \boxed{\quad
 \widehat c_P\widehat c_Q(2\pi)^{-N/2}
 \exp\left(CH_0|Y|+\tfrac{27}{2}\sum_i a_i^2-\tfrac7{24}U\right).
 \quad}\tag{16}
\]

`N` is the number of scalar Gaussian components being integrated. The integration domain may still be the ball cuts; enlarging it gives an upper bound. Formula (16) is an implication for the actual integrand if the specified coefficient and family hypotheses hold. It spends the shared Gaussian once. In particular it does not invoke (GOOD), since T is empty, or spend a second Gaussian for the second factor. Constants from integrating finitely many near variables have not been declared harmless for the linear term.

**Discharged — the logarithmic envelope used in (15).** With the notation of I:890, packing disjoint U's in a four-dimensional box of radius `d(v)+M` gives at most `(3+2d(v)/M)^4` possibilities: assign to each group one distinct M-cube in that box. Here

\[
 d(v)=\rho_P+c_1^{-1}\log(128C_{\rm row}(v+1)/c').
 \tag{17}
\]

Consequently the logarithm of their large-state attachment product is bounded by `B(1+log(v+1))⁵`, for a polynomial B in `1+ρ_P/M`, `1/c₁`, `1+κ′`, and `1+|log(128C_row/c′)|`. No region volume enters. For `z≥1`, the power-series term `e^{z/2}≥(z/2)^5/5!` gives `z⁵≤2⁵5!e^{z/2}`. Taking `z=1+log(v+1)` bounds this envelope by `B_*sqrt(v+1)`, with `B_*=2⁵5!sqrt(e)B`. For

\[
 v\geq V_*:=\max\{1,(12\sqrt2 B_*)^{2/3}\},
 \qquad B_*\sqrt{v+1}\leq v^2/12.
 \tag{18}
\]

This derives the claimed comparison with a Gaussian square. It also exposes its actual hypothesis: `A_sharp≥V_*`. That follows if the §3.1a constants and `1/c′` have polynomial envelopes in L and `R_loc=A_R log L` with sufficiently large fixed `A_R`; it has not been proved merely by saying that an exponential beats a logarithm. The threshold is independent of g, region, and RG depth under those envelopes.

**Implication — the spectator stage and its budget.** Use the radius actually specified in I:963,

\[
 \varrho_A(c')=\min\left\{{e^{\kappa_Gd_c(c',A)/2}\over C_9},
 {\rho_e\over C_{10}g}\right\}.
 \tag{19}
\]

For `c′` outside the touching layer, `d_c≥1`; when the exponential term is active, `κ_G≥8log C₉` gives `varrho_A(c′)≥C₉³ exp[κ_G(d_c−1)/2]`. The cap contributes no large good-spectator state if `p₄<ρ_e/(4C₁₀g)`. Thus the deterministic layer is independent of g. This implication concerns the radius, not the assertion that the whole integrand is a series at that radius.

**Discharged — the spectator polynomial envelope.** A large spectator of magnitude `v≥1` reaches at most distance `d_v=(2/κ_G)log(4C₉v)`. The frozen hull cost is at most `(4C₉v)^{1/4}`, since `κ′=κ_G/8`. For the sum over old supports, an animal count can be obtained without enumeration: encode a connected n-cube set containing a root by a depth-first traversal of a chosen spanning tree, of length `2(n−1)`, using at most 80 neighbour directions at each move. Hence there are at most `80^{2(n−1)}` such sets. For `r>2log80`, their total `exp(−rn)` weight is at most `exp(−r)/(1−80²exp(−r))`. Multiplying by the number of possible roots within distance `d_v`, at most `(3+2d_v)^4`, gives an envelope

\[
 B_1H_0\,(1+\log(4C_9v))^4(4C_9v)^{1/4}
 \leq B_2H_0\,(1+v)^{1/2}.
 \tag{20}
\]

For the last step use `z⁴≤4⁴4!e^{z/4}`, proved from one term of the exponential series. The constants B₁,B₂ are polynomial in C₉ and `1+κ_G^{-1}`, with the displayed geometric denominator; they are independent of volume, region, depth and radius. This proves the elementary envelope used by the spectator paragraph, conditional on its asserted assignment and summability of the activities.

**Discharged — Gaussian integration after (20).** Let `ε=B₂H₀`. For `v≥1`, `εsqrt(1+v)≤sqrt2 εsqrt v`. Write `y=sqrt v`. The maximum of `sqrt2 εy−(c₄/2)y⁴` occurs at `y=(sqrt2 ε/(2c₄))^{1/3}` and is at most `2 ε^{4/3}c₄^{-1/3}`. For `v≤1`, the expression is at most `sqrt2 ε`. Consequently the complete spectator exponent, with the original margin retained, is bounded by

\[
 -c_4v^2+\epsilon\sqrt{1+v}
 \leq-{c_4\over2}v^2+\sqrt2\epsilon
 +2\epsilon^{4/3}c_4^{-1/3}.
 \tag{21}
\]

There is no use of a second copy of the spectator Gaussian for each old factor. Equations (15) and (21) apply to independent local and spectator variables. They do not permit adding a further unbudgeted exponential from the normalized smoothing density.

**Implication — what the two supports become.** At the first level, (R2) gives rough set

\[
 R^{(1)}=\bigcup_{J=P,Q}
 \{\operatorname{image}N_1(Z_J)+B(R_P^+)\}.
 \tag{22}
\]

The group anchors are the bricks meeting the same enlargement of the *supports*. The local Möbius term on X has support containing its anchor and a connecting hull of X; the spectator Möbius term has the touching layer and a connecting hull of X′. Thus for these labelled terms a sufficient support is

\[
 Y^{(1)}=\operatorname{Hull}\bigl(L(A_P\cup A_Q\cup X)\cup X'\bigr).
 \tag{23}
\]

The one shared local label is either already in the anchor, or adds a path to its cube when (13) is used. The sets X and X′ depend on the term; (23) is not a deterministic enlargement by their maximum possible range. The proof that all terms with these labels have the coefficient bound at this support remains conditional on the coefficient substitutions of Lemma 4.7j and stage (ii).

**Implication — the second successive scale, given the claimed labelled output.** Apply (3)–(7) at level `j=1` to the labelled output functions of the first level, with fresh variables `x̃,ξ̃,η̃`, coupling `g₁`, and old factors `E_P,E_Q`. In particular its unnormalized coefficient linear in `E_P` is explicitly

\[
 J_1^{K_{E_P}}(E_P)(U)
 =\int d\mu'_1(\widetilde\eta)
 \int d\mu^{K_{E_P}}_{1,U,\widetilde\eta}(\widetilde x,\widetilde\xi)
 A_1(U,\widetilde x,\widetilde\eta)\,
 E_P\bigl(V_1(U,\widetilde x)\bigr).
 \tag{24}
\]

Substitute `E_P(W)=J_0^{K_P}(e_P)(W)/N₀(W)` from (6) before vacuum subtraction and marginal extraction. This writes the two successive scales as one nested integral with factor

\[
 {A_1(U,\widetilde x,\widetilde\eta)\over N_1(U)}
 {A_0(V_1(U,\widetilde x),x,\eta)\over N_0(V_1(U,\widetilde x))}
 e_P\bigl(V_0(V_1(U,\widetilde x),x)\bigr)
 \tag{25}
\]

and the two independent measures (4). When the first output is a sum of labelled functions, (24) is summed over its labels, each with its own `K_{E_P}`. Both denominators in (25) are retained. Marginal extraction moves a quadratic classical term into the coupling; its contribution at the next step must be retained separately. Formula (25) is the carried old-factor contribution before that bookkeeping, not a claim that the marginal contribution disappears.

**Discharged — marker algebra at the second scale.** In (24) replace `E_P` by the first numerator coefficient `A₀=J₀^{K_P}(e_P)/N₀`, and similarly obtain `B₀` and `C₀=J₀^{K_P∪K_Q}(e_Pe_Q)/N₀`. Write `𝒰₁^R H=J₁^{K_R}(H)/N₁`, including its label sum. The logarithmic coefficients at the second scale are

\[
 [a]\log Z_{01}=\mathcal U_1^{R_P^{(1)}}A_0,
 \qquad
 [ab]\log Z_{01}=\mathcal U_1^{R_P^{(1)}\cup R_Q^{(1)}}C_0
 -(\mathcal U_1^{R_P^{(1)}}A_0)(\mathcal U_1^{R_Q^{(1)}}B_0).
 \tag{26}
\]

This follows by the same expansion as (6), before regrouping the first-level exponential. In particular neither (GROUP) nor the second integration changes the activity degree of the linear term. Replacing its bound by `ĉ_Pĉ_Q`, or by a `tt^{3/2}` bound, is algebraically unavailable.

**Implication — near-set radii through two scales.** Use `r^(j)` for geometric thickness, distinct from the draft's collar `r₂(g)`. For each branch of (22) the stated rule gives `r^(1)≤r^(0)/L+R_P^+` and then

\[
 r^{(2)}\leq r^{(0)}/L^2+(1+L^{-1})R_P^+.
 \tag{27}
\]

Any fixed one-cell convention for `N₁` can be included in the constant already in `R_P^+`. The fixed point is `LR_P^+/(L−1)`. The claimed special support for the *resummed linear* term is the bricks meeting `image N_{r_e}(P)+B(R_P^+)` at each application of (ONE). Its geometric thickness is likewise independent of g if `r_e=O(log L)`; the assertion that resummation has the required norm on that support is precisely what still needs (BANACH). No path or touching layer from (23) may be charged to that linear term without proof.

**Implication — the Gaussian fluctuation moment relevant to one-factor growth.** Assume the uniform variance premise used in I:1004: every component of `D b̂/g` has variance at most `σ²`, with σ absolute. Let

\[
 S=\sup_z e^{-c_1d(z,P)/2}|(D\widehat b)_z|/g,
 \qquad T=(D_P^+)^2 S.
 \tag{28}
\]

A one-dimensional centred Gaussian X with variance at most σ² has `E exp(tX)≤exp(σ²t²/2)`, by completing the square; Markov with `t=u/σ²` gives `P(|X|>u)≤2exp(−u²/(2σ²))`. For three components use that one has magnitude greater than `u/√3`. The number of plaquettes in the distance-n shell of P is at most `C(D_P^++n+1)^4≤C(D_P^++1)^4(n+1)^4`, by enclosing it in a lattice box. A union bound, requiring no independence between plaquettes, yields

\[
 \Pr(S>u)\leq C(D_P^++1)^4
 \sum_{n\geq0}(n+1)^4
 \exp[-u^2e^{c_1n}/(6\sigma^2)].
 \tag{29}
\]

For `u≥max(1,σ)`, split the exponent in half and use `e^{c₁n}≥1+c₁n`; the sum is bounded by a constant depending only on c₁ and σ times `exp(−u²/(12σ²))`. The shell sum is finite because `(n+1)^4≤C exp(c₁n/24)` follows from the fourth term of the exponential series. Split the tail integral `E S^m=∫₀^∞m u^{m−1}P(S>u)du` at a constant times `sqrt(log(D_P^++2))`. Above this point set `u=u₀+v`, use `u²≥u₀²+v²`, and integrate a fixed polynomial against `exp(−v²/(12σ²))`. These integrals are finite: on `v≥1` a polynomial times the Gaussian is bounded by a constant times `exp(−v)`, again by the exponential series. For each fixed integer m this proves

\[
 \mathbb E T^m\leq C_m(D_P^+)^{2m}
 [1+\log(D_P^++2)]^{m/2}.
 \tag{30}
\]

For m=2,3 this gives the envelope

\[
 P_P=C(D_P^+)^6[1+\log(D_P^++2)]^{3/2}.
 \tag{31}
\]

It is uniform in torus radius, region and depth *if the stated uniform variance bound holds*. For the small polymers to which smoothing is applied, `D_P^+≤170M+2r_e`; (31) is then polynomial in M and `r_e`. For long polymers it depends on their diameter and must be absorbed as in (10). The comparison of the actual nonlinear curvature with `t_*+T`, and the same moment bound under the normalized coefficient-valued interacting density, are not discharged by (29)–(31).

**Discharged — an exact mixed coefficient of the actual integrand.** The following gives a specific term to check, rather than a proposed lemma list. Fix one of the two real site states, `r=0,1`. All other real integration variables, including the spectator, remain integrated. On the unsplit near labels expand the *actual* centre at the actual base as

\[
 s_i^r(w)=s_{i,0}^r+w\,a_i^r+w^2b_i^r+O(w^3),
 \qquad t_i^r=x_i-s_{i,0}^r,
 \tag{32}
\]

and expand the rest of the numerator integrand as

\[
 H^r(w)=A^r(w)\,e_P(V^r(w,x))
 =H_0^r+wH_1^r+w^2H_2^r+O(w^3).
 \tag{33}
\]

This includes the variation of the real-base old factor, its analytic tail, the kernels on A labels, and the full analytic weight. It does not hold the old C growth fixed at a fictitious flat base. From the exponential in (14), define

\[
 L_1^r=\sum_{i\in K_P}t_i^r\cdot a_i^r,
 \quad L_2^r=\sum_{i\in K_P}t_i^r\cdot b_i^r
 -\tfrac12\sum_{i\in K_P}a_i^r\cdot a_i^r,
 \quad D_2^r=L_2^r+\tfrac12(L_1^r)^2.
 \tag{34}
\]

The dot product in the Gaussian is bilinear; at the real base and a real w direction these coefficients are real. If `dν₀^r` denotes the base measure (4), including the spectator, then the first three numerator coefficients are exactly

\[
 J_{e,0}^r=\int H_0^r\,d\nu_0^r,\qquad
 J_{e,1}^r=\int(H_1^r+L_1^rH_0^r)\,d\nu_0^r,
 \qquad
 \boxed{J_{e,2}^r=\int(H_2^r+L_1^rH_1^r+D_2^rH_0^r)\,d\nu_0^r.}
 \tag{35}
\]

The domain in x is still `|x_i|≤p₂`. It was not shifted to a w-dependent cut. The same formulas with `e_P=1` give `N_0^r,N_1^r,N_2^r` for the denominator of `Γ^P`. Formal division, legitimate since `N_0^r>0` at a real base, gives

\[
 \boxed{\Gamma_2^r={J_{e,2}^r\over N_0^r}
 -{N_1^rJ_{e,1}^r\over(N_0^r)^2}
 +\left({(N_1^r)^2\over(N_0^r)^3}
 -{N_2^r\over(N_0^r)^2}\right)J_{e,0}^r.}
 \tag{36}
\]

The mixed coefficient being tested is `Γ₂¹−Γ₂⁰`. Thus it is a difference of the *whole* expressions (35)–(36), not a pointwise comparison of centres and not the difference of numerator integrands alone. In particular the shared-label piece

\[
 {1\over N_0^r}\int H_0^r\,
 \left\{t_i^r\cdot b_i^r+
 \tfrac12[(t_i^r\cdot a_i^r)^2-a_i^r\cdot a_i^r]\right\}d\nu_0^r
 \tag{37}
\]

is linear in the old activity. It is present even though T and Bad are empty. Cross terms with other labels occur in `(L₁^r)²`; omitting them would spend the joint density incorrectly. Equations (35)–(37), with the site difference, give the precise integrand term for this test.

**Discharged — the elementary size of the density polynomial.** Let `ρ=ρ_{R′}(c)`, `𝔞_r=ρ(Σ_i|a_i^r|²)^{1/2}`, and `𝔟_r=ρ²(Σ_i|b_i^r|²)^{1/2}`, at fixed spectator. Under the full product Gaussian in t,

\[
 \rho^2\int |D_2^r|\,d\mu(t)
 \leq\mathfrak b_r+\mathfrak a_r^2.
 \tag{38}
\]

Indeed `E|Σt_i·b_i|≤(Σ|b_i|²)^{1/2}` by Cauchy–Schwarz and Gaussian variance, while `E(L₁)²=Σ|a_i|²`; the two quadratic summands contribute at most that sum. The Gaussian variance identity follows by integrating `−t φ′(t)` and using `∫φ=1`; boundary terms vanish since a polynomial times `exp(−t²/2)` tends to zero. Restricted x cuts only lower the integral of this nonnegative bound. For a factor bounded by M at every real t, the right side of (38) is multiplied by M. Taking M=`ĉ_P` exhibits the uncontracted size available from (CRUDE):

\[
 24\,cc_j g_j^{-3}(D_P^+)^6\omega_P
 (\mathfrak b_r+\mathfrak a_r^2).
 \tag{39}
\]

This is not a lower bound or a counterexample. The full analytic weight and denominator still have to be treated in (36). Replacing the prefactor in (39) by `C cc_j ω_P P_P`, uniformly in the coefficient algebra after normalization, is the substantive moment step; (30) alone does not do it.

**Discharged — what the shift part of (DENS-Q) actually proves.** For a fixed positive precision matrix Q and a real Gaussian vector X of covariance `Q⁻¹`, let `y=Σ_m y_m z^m` be a shift series. Put `b_m=||y_m||_Q ρ^m`, `B=Σ_m b_m`; B=0 is the unchanged-density case. For real coefficient vectors, write `Z_m=〈X,Qy_m〉/||y_m||_Q`; every nonzero `Z_m` is standard normal. Convexity, with weights `b_m/B`, gives

\[
 \exp\Bigl(\sum_m b_m|Z_m|\Bigr)
 \leq\sum_m{b_m\over B}e^{B|Z_m|},
 \qquad E e^{B|Z|}\leq E(e^{BZ}+e^{-BZ})=2e^{B^2/2}.
 \tag{40}
\]

The quadratic part of the shift costs at most `exp(B²/2)`. Thus the integrated density norm is at most `2exp(B²)`. This uses one Gaussian and no factor per link. For complex coefficient vectors, split real and imaginary parts and use their Q norms; the same proof gives a bound with B replaced by their summed norms, at most `√2` times the summed complex Q norms. A limiting argument on increasing finite coefficient sets is justified by monotone convergence of these nonnegative majorants. What (40) does **not** prove is a bound for B for the actual inverse-coordinate map, for its Jacobian and analytic weight, or for the inverse normalizing series. Those are separate factors in (35)–(36).

**Gap — the exact inequality not derived.** Let `𝓜(w,h)=β(e_P)(F₀^*(w,h),F₀^*(w,h))` mean exactly the marginal term specified in (BANACH), without changing its prescription. Let

\[
 \mathcal R_{2,S}:=(\Gamma_2^1-\Gamma_2^0)-[w^2h]\mathcal M.
 \tag{41}
\]

A necessary one-link, one-site consequence of the claimed contraction is

\[
 \boxed{\quad
 \rho^2e^{c_3\tau(Y';\{c\},S)}|\mathcal R_{2,S}|
 \ \leq\ C\,cc_j\omega_P P_P
 \left(t_\#^3+t_\#^2(D_P^+/L)^a\right)
 +\mathcal B_j(P),\quad C\text{ absolute},
 \quad}\tag{42}
\]

where `t_#` and its floor are the frozen quantities of (BANACH), and `𝓑_j(P)` is its allowed born-error bound, namely the coefficient-sized bound with factors `C(L,M)(g_j^η+p_j exp(−c₃T_{j+1}/8))+exp(−p_j²/3)`. The corresponding inequality with a supremum over all field multi-indices and sums over all site sets is stronger. I have not derived (42), already for the single coefficient (41). I have also not obtained a lower bound violating it. Formula (36) specifies exactly what must be estimated or cancelled; (39) states the crude size, which does not establish the required contraction.

**Gap — where the frozen argument stops supplying an estimate for (42).** In (BANACH), steps (3)–(5), the assertions `N_Q≤Cc`, `J exp Ψ=1+small in the algebra`, and the claim that normalization at fixed `(v,ξ_d^⊥)` costs `1+small` are used together to obtain the following disc estimate. To specify the integrand without inserting an extra Gaussian, let `χ=(ξ_d^⊥,ξ_off d,η)`, let `Ξ_ζ(v,χ;w,h)` be the actual inverse-coordinate value of `ξ_d`, and let `J_ζ` be the exact Jacobian of this change of variables. Let `dν=dv dξ_d^⊥ dμ(ξ_off d)dμ′(η)`; it contains no Gaussian on `ξ_d`, since that Gaussian is written explicitly. Keep the new real-coordinate cuts `1_𝒞` of the smoothing proof, with their claimed replacement error charged to `𝓑_j(P)`. The unresolved estimate is

\[
 \sup_{|\zeta|\leq c/t_\#}
 \left\|{\int d\nu\,{\bf1}_{\mathcal C}J_\zeta e^{\Psi_\zeta}
 \phi_d(\Xi_\zeta(v,\chi;w,h))\,e_P(V_\zeta)
 \over N_{\rm good}^Z(W_\zeta)}\right\|_{Y'}
 \leq C\,cc_j\omega_P P_P.
 \tag{43}
\]

Here `φ_d` is the original normalized Gaussian on all local noise components in d. The norm on the left is the sum of absolute field and site coefficients of the integral. A proof by taking the norm inside that integral must sum those coefficients before integrating their majorant. This is the unproved estimate used by the draft to improve (39); (40) proves only a translation-density bound, conditional on the required form-norm bound for the actual shift series. Lemma 4.7f bounds a saddle and several kernels. It is not itself an estimate of the conditional inverse-coordinate density and its normalizing series in (43). The cluster library gives a norm bound when the integrated activities and product-norm hypotheses are supplied; it does not supply those hypotheses for this conditional density. In particular, applying it to the unconditioned good gas and then calling the conditional ratio `1+small` does not derive the coefficients in (36). This report leaves (43), and consequently (42), as gaps. It does not designate either as false, or rule out a proof of (42) using further cancellations instead.

**Discharged — a possible spurious objection excluded.** In the situation of the test a far site outside the fixed locality neighbourhood does not directly change the near rows of P or V^#. This follows from their frozen finite-range definitions. One must not manufacture a covariance defect by allowing those rows to read that site. The unresolved term (35) instead retains the actual centre, the far chart fields, the analytic weight, and the normalizing denominator. Its dependence on the site is not set to zero by that locality observation.

**Gap — polynomial uniformity needed at this point.** The elementary envelopes (10), (18), (20), (30) have been derived above, with their hypotheses stated. A finite-range row bound can also be proved from an operator bound: if a row has at most N entries, Cauchy–Schwarz gives `Σ|T_li|≤√N||T||₂→₂`; in four dimensions range `ρ_P` gives `N≤C(1+ρ_P)^4`, by counting a containing box. Thus a polynomial operator bound would give a polynomial row bound uniformly in region and depth. But the uniform operator and mixed-coefficient bounds for the actual conditional density in (43) have not been derived here. I:250 explicitly makes the polynomial bounds for `C_F,C_F′,C_row,R₀,D` inputs. Substituting the word “polynomial” for those bounds, or fixing L first and allowing an unspecified function of L, would not verify their role in (18), (19), or the absolute constant in (42). Consequently this report does not claim that the order of constants, uniformly in region, depth and radius, has been closed.

**Discharged — one source insertion, exactly.** Put `I=D_f I^f|_{f=0}` for a source direction allowed in §6; the chart, centres and cuts do not read f. If the old factor also depends on f, write `ė=D_f e_P^f|₀`. Differentiating the numerator and denominator in (7), at a fixed site state, gives

\[
 D_f\Gamma^P\big|_0=
 E^Z[\dot e+e_P I]-E^Z[e_P]E^Z[I].
 \tag{44}
\]

This identity follows directly from the quotient rule. At the unnormalized level (35) the source replaces `H(w)` by

\[
 H^I(w)=A(w)\,[\dot e(V(w))+e_P(V(w))I(w)].
 \tag{45}
\]

It leaves `L₁,L₂,D₂` unchanged. For example the actual inserted counterpart of (37) contains

\[
 {1\over N_0^r}\int A_0^r e_P(V_0^r) I_0^r
 \left\{t_i^r\cdot b_i^r+
 \tfrac12[(t_i^r\cdot a_i^r)^2-a_i^r\cdot a_i^r]\right\}d\nu_0^r,
 \tag{46}
\]

together with the numerator-tail terms of (35), and the derivatives of every normalizing term of (36). Take the difference between site states after forming this expression. There is still only one old activity. Gauge invariance does not erase (46) individually; any cancellation has to be established in the complete expression (44).

**Implication — no forced double spending from the source.** Per cube, the source bound in I:1173 has a quadratic charge `C(L)ρ_src g²U_c` and a linear charge `ℓ_c sqrt U_c`, where `ℓ_c=C(L)Λa_k g Φ_c^w`. If `C(L)ρ_src g²≤1/64`, then `ℓ_c sqrt U_c≤U_c/64+16ℓ_c²`. Sum over cubes, with `U=Σ_c U_c`. Adding both charges to (15) gives

\[
 -\tfrac7{24}U+\tfrac1{64}U+\tfrac1{64}U
 =-\tfrac{25}{96}U,
 \tag{47}
\]

plus the already displayed constants and `16Σ_cℓ_c²`. The two-factor source integrand is consequently bounded by (16) with `−7U/24` replaced by `−25U/96` and the source constants included. This is one total budget. For a first insertion rather than its exponential, the factor is polynomial in the same Gaussian variables; the tail argument proving (30) applies to any fixed higher moment as well. Neither fact proves the normalized mixed-coefficient estimate (43) with (45) inserted.

**Discharged — the insertion at the second successive scale.** Differentiate (25), including both normalizations. The result is the sum of an insertion at the first level and one at the second, plus the propagated old-factor insertion. In normalized operator notation `𝒯_j H=E_j^Z H`, each differentiated integration is

\[
 D_f(\mathcal T_jH)=\mathcal T_j(D_fH)
 +\mathcal T_j(H I_j)-\mathcal T_jH\,\mathcal T_jI_j.
 \tag{48}
\]

Apply (48) first with `H=e_P`, then with the full first output. Differentiate the ratios in (7) as well when using `𝒰` instead of `𝒯`. The marginal extraction and its source derivative are retained separately, as in (25). Thus (46) has a first-level and a second-level occurrence. The second old factor cannot pay for either linear occurrence. A proof of (43) with the insertion would be needed at both levels, with the same uniform constants; that proof has not been supplied by this test.

**Discharged — scope of this conclusion.** Read the requested goal and rules first, the named previous gate, the main file's frozen definitions and target proofs and their immediate passages on the source, tree/site norm and linear lift, and `library/ultralocal_cluster_expansion.md`. Source locators exposed other passages of the same permitted main file. Did not read the mapped attempt, other proof accounts, git history, external skills, or anything outside this directory. No numerical job was run. The reported algebra is written out above; imported lattice, saddle, chart and cluster estimates are expressly conditional or gaps. No actual SU(2) coefficient has been shown to exceed (42).

**Gap — final verdict: undecided at (42), specifically the normalized integrand estimate (43) needed for the mixed coefficient (35)–(37), and its one-source counterpart (44)–(46).** The two-old-factor Gaussian budget and the scalar large-label envelopes do not falsify the proposed repair under their stated inputs. They also do not discharge (BANACH). The one-factor term has no second small activity, and its displayed crude size (39) cannot be relabelled as the asserted contraction. No conclusion of survival or failure of the actual closure is justified by this test.
