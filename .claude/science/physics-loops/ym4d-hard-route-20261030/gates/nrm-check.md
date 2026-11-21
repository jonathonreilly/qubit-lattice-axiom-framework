# NRM: bare-partition-function normalization check

Codex, high-effort mathematical check, 2026-11-05; checkout `534b15cc841d36b1ee4918f6753aa94e45d42115`. Research text, not an audit; grants no status. Only this report is edited. Source retrieval and text searches are navigation, not computer-assisted proof.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. `SA` means their outline `YM4_sketch_500.tex`; `I`, `II`, `III` mean their complete-account parts, all at `31a47c543775`. Citations below are **source-file line numbers**, not rendered page numbers. The outline and CA-I were fetched once to `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`; the existing `/tmp/sa_ca_II.tex` and `/tmp/sa_ca_III.tex` supply the other cited excerpts. The `library/sa-index/` README, object rows with neighbours, obligations, and complete-account index guide the bounded readings.

## Statements being checked

- **ADVANCE:** the bare Wilson axial-gauge upper bound, proved below by hand.
- **WRONG in the bare normalization:** the simultaneous application of CA-I 4.33's lower member and mass preservation to Definition 1.1, with the stated uniform small-field/background inputs. The conditional implication inside 4.33 is not the error; its vacuum-energy hypothesis is imported with a different initial constant.
- **CORRECT-NO-ADVANCE:** a vacuum-normalized lower bound has no such contradiction. The account does explicitly use this other normalization elsewhere. Accordingly the referee's assertion that Chapter 4 contains no such constant (`lsc-gate.md:20–23`) needs correction; its diagnosis of `lsc.md:214,342–353` in the bare normalization survives.

## 1. The normalization is specified, not implicit

Definition 1.1 sets `rho_0 = exp[-g_0^{-2} A]` (I:477–481), and distinguishes the probability measure obtained by dividing by its integral (I:482–487). Definition 1.5 explicitly starts the recursion from **that** density (I:924–933). Its large-field replacement uses normalized reference laws and preserves the integral (I:907–922). Thus one cannot interpret `rho_k` in 4.33 as a probability density or silently multiply its initial value by a constant.

The never-large term in 4.33 is

\[
\tau_\varnothing=\chi_k\exp\{-x_k A(U_k)+\mathbf E_k(U_k)+\mathbf R_k(U_k)-E_k[\varnothing]\}\,dV_k
\tag{1}
\]

(I:157011–157018). Here `N_k` counts **scale-k** cells (I:157000–157009), not bare cells. Hypothesis (h2) bounds the two field-dependent terms by `C_E N_k` independently of coupling (I:157033–157037). Hypothesis (h4)(a) asserts

\[
-E_k[\varnothing]=\mathfrak l_k-\mathfrak r_k,
\qquad \mathfrak l_k\ge0,\qquad
|\mathfrak r_k|\le C_{\mathfrak r}N_k
\tag{2}
\]

(I:157039–157041). The lower member discards the positive logarithmic part and gives `rho_k dV_k >= chi_k exp[-x_k A(U_k)-E_- N_k] dV_k`, with `E_- = C_E+C_r` independent of `g_k,k,K,m,g_0` (I:157084–157089; proof I:157114–157129). Clause (i-c) equates its integral with that of `rho_0` (I:157110). These are precisely the ingredients used as (9) in `lsc.md:135–163` and then at `214,342–353`.

There is a different constant elsewhere: I:159153–159160 defines

\[
E=\sum_{j=0}^{K-1}E^{(j)}(T,T),\qquad
E_k[\mathcal S]=E-\sum_{j=0}^{k-1}E^{(j)}(\Omega_{j+1},\Lambda_{j+1}).
\tag{3}
\]

Consequently the never-large energy is the **remaining** sum from `j=k` to `K-1`, not the negative accumulated sum from `j=0` to `k-1`; this is explicit in I:159321–159327. In particular `E_0=E` and `E_K[emptyset]=0`. This is the vacuum-normalized convention. Its compatibility and the precise failed substitution into (2) are proved below.

## 2. What the claimed lower member would imply

Fix the group **SU(2)**. Write `k=K'`, let `N` now denote the side of the last lattice, and put `V=N^4=N_k`. The bare side is `T=L^k N`, so its volume is `T^4=L^{4k}V`; this follows from the scale spacings in I:434–444. Set `x=x_k` and `eta=L^{-k}`. The extra inputs needed to integrate the lower member are explicit: I:154052–154058 bounds the fine background curvature by `B_3 w eta^2` for coarse plaquette curvature below `w<=a_1`, and I:155039–155095 gives `chi_k=1` when also `B_3 w<=epsilon(x)`. If using the alternative datum convention at I:155092–155095, absorb its fixed `C_Q` into `B_3` throughout. Here `epsilon(x)=A_0 x^{-1/2}(log x)^{p_0}` (I:153602–153613), with `p_0>=5r>=10` (I:1349–1352). These are retained hypotheses of this implication, not new proofs of the background construction. The three statements named in the question **alone**, without a nonempty small-field region and an action bound there, would not give a useful floor.

For `x>=e` and the nonnegative threshold exponent, choose once

\[
a=\min\{1/2,a_1/8,A_0/(8B_3),1/(8B_3)\}>0,
\qquad s=a x^{-1/2},
\qquad \mathcal B_s=\{V_b:\|V_b-1\|_{\rm op}<s\text{ on every bond}\}.
\tag{4}
\]

Telescoping a product of four unitaries, and using `||W^{-1}-1||=||W-1||`, gives coarse plaquette curvature `<4s`. Our choices give `4s<=a_1/2` and `4B_3s<=epsilon(x)/2`. Thus all the stated tests pass and fine plaquette curvature is `<4B_3s eta^2` on this set. For SU(2), the eigenvalues `e^{±i theta}` give exactly

\[
1-\operatorname{Re}\operatorname{tr}W
=1-\cos\theta=\tfrac12\|W-1\|_{\rm op}^2.
\]

There are `6V eta^{-4}` fine plaquettes. Therefore

\[
xA(U_k(V))\le48B_3^2a^2V\le\tfrac34V.
\tag{5}
\]

For completeness, normalized Haar measure is normalized volume on the unit quaternion sphere: multiplication is orthogonal and preserves this probability measure. In polar coordinates its density is `(2 pi^2)^{-1} sin^2(theta) dtheta dOmega`. For `0<s<=1`, the interval `0<theta<s` is inside the operator ball because `2 sin(theta/2)<=theta`. Concavity of sine gives `sin(theta)>=2theta/pi` on this interval. Integrating over the sphere of directions gives

\[
\operatorname{Haar}(\|W-1\|<s)
\ge\frac2\pi\int_0^s\frac{4\theta^2}{\pi^2}\,d\theta
=c_Hs^3,\qquad c_H=\frac8{3\pi^3}.
\tag{6}
\]

This reproduces the outline's argument (SA:23504–23513), including its probability normalization. The last lattice has `4V` independent positive bonds. The putative lower member, positivity, (5), and (6) consequently imply

\[
\begin{aligned}
\int\rho_k\,dV_k
&\ge e^{-(E_-+3/4)V}(c_Ha^3x^{-3/2})^{4V}\\
&=\exp[-(C_0+6\log x)V],\\
C_0&=E_-+3/4+4\log(c_H^{-1})+12\log(a^{-1}).
\end{aligned}
\tag{7}
\]

`C_0` is independent of `k,K,g_0,x` and volume. On a last-coupling window `x<=x^*(g)<infinity`, this is the asserted floor with `C(g)=C_0+6 log x^*(g)`. It is uniform in cutoff and volume at fixed reference `g`, **not bounded as `g` tends to zero**. In the literal Chapter 1 convention, (i-c) makes the left side exactly `Z_bare`. The same derivation, with a window-dependent radius, verifies the arithmetic of `lsc.md:294–353`; its problem is the input normalization.

## 3. Full axial-gauge upper bound, without a determinant approximation

Take a periodic four-dimensional cubic lattice of side integer `T>=3` with the action and Haar convention of I:450–468. This includes the admissible bare lattices used below. Write sites as `(y,t)`, where `y` has three coordinates modulo `T` and `0<=t<T`. For each fixed `y`, keep the temporal edges from `t=0` through `t=T-2` as a tree; leave the closing edge unrestricted. Define vertex matrices recursively by

\[
h(y,0)=1,\qquad h(y,t+1)=h(y,t)U_4(y,t).
\]

Under the gauge transformation `U'(v,w)=h(v)U(v,w)h(w)^{-1}`, every tree temporal edge becomes `1`. The last edge becomes its unrestricted temporal holonomy `P(y)`. This change costs **no gauge-volume factor**: change the temporal variables successively to `h(y,1),...,h(y,T-1),P(y)`. At each stage it is left or right multiplication by an already fixed group element, preserving probability Haar measure. Conditional on these temporal variables, transform every spatial bond to `W_i(y,t)=h(y,t)U_i(y,t)h(y+e_i,t)^{-1}`; this also preserves its independent Haar measure. The action is gauge invariant, since its plaquette products are conjugated and their traces unchanged. Integrating the unused `h` variables therefore contributes exactly one. This is an explicit finite change of variables, not an assumed Faddeev–Popov formula.

For each `i=1,2,3`, each `y`, and `t=0,...,T-2`, the transformed `(i,4)` plaquette product is

\[
W_i(y,t)W_i(y,t+1)^{-1}.
\]

All Wilson plaquette actions are nonnegative (I:456–460). Dropping every spatial plaquette and every temporal plaquette crossing the closing slice increases the integrand. The retained integrand is independent of every `P(y)`, whose Haar integrals are one. Consequently

\[
Z_{\rm bare}(x_0,T)
\le\prod_{i=1}^3\prod_y
\int\prod_{t=0}^{T-1}dW_t\,
\prod_{t=0}^{T-2}e^{-x_0[1-\operatorname{Re}\operatorname{tr}(W_tW_{t+1}^{-1})]}.
\tag{8}
\]

Define

\[
c(x)=\int_{SU(2)}e^{-x(1-\operatorname{Re}\operatorname{tr}W)}\,dW.
\]

Integrate `W_0` first in each chain: it occurs in exactly one retained factor, whose integral is `c(x_0)` for every `W_1`, by Haar invariance. Repeat for `W_1,...,W_{T-2}`. The remaining integral over `W_{T-1}` is one. There are exactly `3T^3` such disjoint chains. Thus

\[
Z_{\rm bare}(x_0,T)\le c(x_0)^{3(T-1)T^3}.
\tag{9}
\]

The quaternion polar formula used above gives

\[
c(x)=\frac2\pi\int_0^\pi e^{-x(1-\cos\theta)}\sin^2\theta\,d\theta.
\]

On `[0,pi]`, concavity of sine on `[0,pi/2]` gives `1-cos(theta)=2sin^2(theta/2)>=2theta^2/pi^2`, and `sin^2(theta)<=theta^2`. Extending the nonnegative integral to infinity gives

\[
c(x)\le\frac2\pi\int_0^\infty\theta^2e^{-2x\theta^2/\pi^2}\,d\theta
=C_Hx^{-3/2},\qquad C_H=\frac{\pi^{5/2}}{2^{5/2}}>1.
\tag{10}
\]

The integral evaluation is elementary: the square of `integral_R exp(-u^2) du` is the planar integral `2pi integral_0^infinity r exp(-r^2) dr=pi`; integration by parts then gives `integral_0^infinity u^2 exp(-u^2) du=sqrt(pi)/4`, followed by the indicated linear substitution. No numerical estimate enters.

Combining (9) and (10), and substituting `T=L^{K'}N`, proves exactly

\[
\boxed{\log Z_{\rm bare}
\le-\frac92(1-T^{-1})L^{4K'}N^4\log x_0
+3(1-T^{-1})L^{4K'}N^4\log C_H.}
\tag{11}
\]

In particular the `O(L^{4K'}N^4)` in the question has an absolute, explicitly displayed constant. Closing temporal holonomies have not been gauged away, and none of the retained plaquettes shares a variable between distinct chains.

## 4. The contradiction, with the quantifiers and flow defect retained

The referee writes `x_0>x_k`. Strict stepwise monotonicity is unnecessary and is not what the account assumes. The actual flow bound is `lambda_sharp k-c_5<=x_0-x_k` (I:2536–2541; I:56342–56358); hence `x_k<=x_0+c_5`. The correlation version has the same conclusion with `c_5=2c_2` (II:2875–2884). Thus for `x_0>=1`, (7), if identified with the bare integral, would imply

\[
\log Z_{\rm bare}\ge-[C_1+6\log x_0]V,
\qquad C_1=C_0+6\log(1+c_5).
\tag{12}
\]

For every `k>=1`, `T>=2`, so (11) implies

\[
\log Z_{\rm bare}\le
-L^{4k}\bigl[(9/4)\log x_0-3\log C_H\bigr]V.
\tag{13}
\]

Fix the construction constants and integer `L>=2`. The number `D=(9/4)L^4-6` is positive (already `L^4>=16`). Choose `x_0` so large that

\[
\log x_0>
\max\left\{1,\frac43\log C_H,
\frac{C_1+3L^4\log C_H}{D}\right\}.
\tag{14}
\]

The bracket in (13) is positive, so its magnitude is at least its value at `k=1`; the last inequality in (14) makes that magnitude strictly greater than `C_1+6 log x_0`. Equations (12) and (13) contradict one another. This holds uniformly for **every admissible `K'>=1`** once the couplings are sufficiently small. It does not require an asymptotic estimate for `m_J(g)` or a numerical choice of `L`.

There is also the weaker but useful fixed-reference-coupling version: if `x_k` remains in a fixed window and `K'` tends to infinity, (7) would give a fixed exponent per last-lattice site while (11) tends to minus infinity per last-lattice site. The account's first-passage statement makes `K` tend to infinity as `g_0` tends to zero (I:56442–56448), so a run stopped a fixed number of levels before first passage has exactly this problem. A merely arbitrary finite `C(g)`, without its growth being controlled, would not by itself prove a contradiction for **one** step as `g` varies; (7) and (14) supply that missing control.

## 5. The failing hypothesis and the normalization actually used elsewhere

**The precise failure is the application of (h4)(a) to the bare density.** This is not an error in the inequality derived *from* (h4)(a) at I:157117–157129. The energy in its vacuum theorem has been initialized with `E`, whereas the density it is applied to has been initialized with zero. The Chapter 4 representation itself reiterates its dependence on Chapter 1's bare density (I:60940–60958), so this cannot be resolved by treating Definition 1.5 as irrelevant notation.

Here is the algebra and its sign. Denote the one-step number `E^{(j)}(T,T)` by `e_j`, and distinguish the initial constant `E_vac=sum_{j<K} e_j` from the level-dependent energy. The explicitly displayed convention (3) gives

\[
E_k^{\rm vac}[\varnothing]
=E_{\rm vac}-\sum_{j<k}e_j=\sum_{j=k}^{K-1}e_j.
\tag{15}
\]

For SU(2), I:159412–159426 gives

\[
e_j=-\frac92(L^4-1)N_{j+1}\log x_j+r_j,
\qquad |r_j|\le D_0N_{j+1},
\tag{16}
\]

where `D_0=(L^4-1)c_G^sharp+K_*(E_0+1)` uses the fixed constants of that statement, and its `E_0` is a local-polymer bound, not our initial energy. To check the logarithmic coefficient directly, the one-step normalization in I:159093–159111 contains `D log g_j` per starred bond and subtracts `(L^4-1) log z_j` per next-level site. The bond count is `4(L^4-1)N_{j+1}` (I:159264–159267); `D=3`, and `log z_j=D log g_j+zeta_j` with bounded `zeta_j` (I:159370–159384). Thus the surviving coefficient is `(4-1)D log g_j = -(9/2) log x_j`. The stated bounds on the remaining terms give (16). This is algebra on their stated one-step inputs, not a fresh proof of the full RG representation.

The sum in (15) has a nonpositive logarithmic part and a remainder bounded on the **current** volume: `sum_{j>=k}N_{j+1}<=N_k/(L^4-1)`. This is exactly the calculation in I:159429–159443 and the conclusion at I:159321–159336. Therefore `-E_k^vac=l_k-r_k` has `l_k>=0`, as (h4)(a) requires. At `k=0`, however, its energy is `E_vac`, not zero.

Multiplying every density and every history by the same positive number does not change a normalized measure. Write this change explicitly:

\[
\widehat\rho_0=e^{-E_{\rm vac}}e^{-x_0A},\qquad
\widehat\rho_k=e^{-E_{\rm vac}}\rho_k^{\rm bare},\qquad
\widehat Z=e^{-E_{\rm vac}}Z_{\rm bare}.
\tag{17}
\]

The exact integral steps preserve this same scalar: the block push-forward is linear, the decomposition sums to one, and the replacement of a term is its mass times a probability law (I:157204–157222). In the exponent of a given never-large term, (17) means

\[
E_k^{\rm bare}=E_k^{\rm vac}-E_{\rm vac}
=-\sum_{j<k}e_j,
\qquad
-E_k^{\rm bare}=E_{\rm vac}+\mathfrak l_k-\mathfrak r_k.
\tag{18}
\]

**The missing summand in (h4)(a) in the bare convention is `E_vac`.** Already at `k=1`, (16) gives

\[
E_1^{\rm bare}\ge
\bigl[\tfrac92(L^4-1)\log x_0-D_0\bigr]N_1.
\tag{19}
\]

For `log x_0>(D_0+C_r)/[(9/2)(L^4-1)]`, this contradicts the consequence `E_1^bare<=C_r N_1` of (h4)(a). This identifies the failure rather than merely guessing which member of a collection of hypotheses breaks. More cautiously, without trusting any one-step input, (1), positivity, (h2), and the ball argument force

\[
E_k^{\rm bare}\ge -\log Z_{\rm bare}
-\bigl[C_E+3/4+4\log c_H^{-1}+12\log a^{-1}+6\log x_k\bigr]N_k.
\tag{20}
\]

Indeed the never-large term alone has mass at least the exponential of minus the right-hand bracket times `N_k`, times `exp(-E_k^bare)`, and is at most `Z_bare`. Substitution of (11) in (20) forces the same failure of `E_k^bare<=C_r N_k` at small coupling. Thus, if the other declared representation and real-field inputs are retained, (h4)(a) cannot apply to the bare energy; this check does not certify those other inputs.

The corrected form of the lower member in the bare convention is

\[
\rho_k^{\rm bare}\,dV_k
\ge e^{E_{\rm vac}}\chi_k e^{-x_kA(U_k)-E_-N_k}\,dV_k,
\qquad
Z_{\rm bare}\ge e^{E_{\rm vac}-(C_0+6\log x_k)N_k}.
\tag{21}
\]

Equivalently, the originally printed lower member and floor concern `hat rho_k` and `hat Z`. These corrected statements follow by the same conditional proof; no new construction is proved here. The negative fine-volume term (16) is now present, so (11) does not refute them.

There are **explicit** places where the authors use precisely this convention:

1. **CA-I vacuum energies:** I:159153–159160 and I:159321–159327 are (15), with the total constant already included at level zero. The associated density-constants corollary repeats the lower member (I:159530–159537), using the sign argument at I:159571–159585. This is correct accounting for (17), incompatible with silently keeping I:479 unchanged.
2. **CA-II sourced density:** II:730–739 expressly permits `rho_0^w=exp[-A(x_0-w,U)-E]`, with `E` independent of fields and sources. Choosing `E=E_vac` supplies (17); taking arbitrary `E`, or zero, does not justify the same claimed constants. Its source subtraction has zero value at zero source (II:59703–59706), so it cannot itself supply the missing unsourced constant.
3. **CA-II volume transfer is decisive:** II:140880–140888 defines `Z_m` with **no** constant. II:140916–140926 then defines `tilde Z_m=e^{-E_m-mathcal E_m}Z_m`, with `E_m=sum_{j<K}E_vac^(j)`, and explicitly writes the normalized bare density `exp[-x_0A-E_m]`. In fact II:140922–140923 calls this the density of Definition 1.5, whereas I:929 points to the different formula I:479. These two passages disagree literally. The volume-transfer proof keeps the factor correctly: `Z_m(0)>=exp[E_m-C_low(2L^m)^4]` (II:141703–141708), followed by the vacuum-density difference (II:141709–141723). It does **not** claim the false bare floor.
4. **The outline also keeps it:** SA:23405–23415 defines `tilde Z=e^{-E-mathcal E}Z`; OH5 retains `e^E` in the positive-label lower bound (SA:23489–23498); OH6 proves the floor for `e^{-E}Z(0)`, not for `Z(0)` (SA:23515–23527). Its accumulated vacuum recursion is SA:31906–31925 and its explicit leading-energy hypothesis has the same negative logarithmic sign (SA:22292–22302). The index classifies OH5 as assumed and OH6 as conditional; the source itself retains the background obligation (SA:23499–23502,23536–23539). This check does not promote those assumptions into proofs.

This corrects the referee's overstatement at `lsc-gate.md:20–23,83`: the account **does** have the required alternative normalization. Its existence does not make the literal Chapter 1/4.33 combination consistent; it shows the specific repair, and why the contradiction is not a refutation of vacuum-normalized ultraviolet stability.

## 6. Uses of the bound: which normalization each must carry

I searched all three complete-account files for `4.33`, `lem-stability-exponent`, and `4.31`, then followed the lower-bound-bearing references (`standing-inputs-d`, `window-counting-nesting-d`, the main theorem's (i-b), and `C_low`). References to equations numbered 4.31 or 4.33 **in Balaban's CMP109 paper** are different objects. The following groups include the definitions, proofs and repeated uses of the bound; unrelated chart/analyticity references in 4.31 are not new stability uses.

| Place and source lines | Use and consequence of this check |
|---|---|
| **Theorem 0 and 4.33.** I:2574–2582; induction cross-references I:3573–3587,61109–61116,61208–61210; lower statement/proof I:157084–157129; upper statement/proof I:157090–157107,157131–157202; common-integral proof and transport to earlier levels I:157204–157240; downstream-use list I:157251–157259; gauge-fixing reference I:157510–157523. | The lower member is false for the Chapter 1 densities with the other stated real-field inputs. Its conditional algebra is valid for the vacuum-normalized density. Equality of integrals holds in either convention **within that convention**; the proof never multiplies by a new vacuum factor. The bare upper bound alone is not refuted (indeed `Z_bare<=1`). The induction's assertion that the vacuum hypothesis is supplied needs the normalization correction. |
| **4.31(d) and the never-large energy.** I:154022–154050,154430–154439,154667–154700. | Here `E_-(x)` is only required to be locally bounded, not constant in `x` as in 4.33. Nevertheless the fixed-last-window argument proves that its bare floor cannot be cutoff-uniform. The asserted bound on `abs(E_emptyset)` uses the residual vacuum energy, not the bare accumulated one. |
| **4.31 fixed-depth limits.** D2/D2+ at I:154728–154746, D5 at I:154807–154819; the lower floor is constructed at I:156531–156547,156611–156656; D5 and its never-large prefactor at I:156782–156834. | In the literal bare convention, `Z_K` tends to zero by (11), so the asserted `Z_K>=z_*>0` and positive unnormalized limit are false. The conditional proof works with `hat Z_K` and `hat rho_{K,s}`. Probability measures `rho/Z` are invariant under this correction; the unnormalized limit density and its prefactor are not. The coupling/holomorphic statements do not acquire a separate counterexample from this calculation. |
| **4.36 repetition at SU(N), including N=2.** I:159153–159160,159298–159327,159530–159563,159571–159603. | This is the explicit `E_vac` convention. Its lower-density formula has the same content as 4.33 but must refer to `hat rho`, or carry `e^{E_vac}` on the bare side. No contradiction with its negative one-step vacuum numbers. |
| **Correlation floor, last-scale uniformity and per-ball bounds.** II:730–739,2933–2950; floor is hypothesis 8 at II:59677 and used at II:59815–59833; (S),(F) at II:60732–60741; chessboard division II:62549–62585; last-scale input II:63179–63226,63393–63410,63510–63565,63907–63935; per-ball division/constants II:64166–64183,64260–64282. | These use the sourced density with its free **unsourced** constant `E`. Set it consistently to the vacuum constant. Neither `mathcal E(0)=0` nor matching the bare lattices identifies this integral with Chapter 1's unshifted integral. This is exactly the fault in `lsc.md:214,346`: in a corrected port the equality is `tilde Z(0)=hat Z=e^{-E_vac}Z_bare`. The remaining upper-history hypotheses are still required. The mathematical ratio and offset arguments are not refuted. |
| **Earlier global-history applications.** II:104292–104301,104364–104376; II:105982–106003; II:107650–107665,107832–107850,107947–107953,108069–108078. | The floor controls a global denominator for history probabilities/first moments; it is not a local conditional floor. Numerator and denominator must both use (17). Then their common vacuum multiplier cancels. These passages do not independently prove a bare floor. |
| **8.8 stability-exponent lemma and every direct reference to it.** Statement II:109859–109907; lower proof II:109918–109975; logarithmic aggregation II:109976–110014; ceilings II:110016–110045; base-case inputs and division II:110118–110131,110214–110228; flat-reserve use II:110258–110265,110288–110337,110355–110367; live-cell inputs II:110445–110499. | Its hypothesis (a) is explicitly the integrated lower member. The ball/Haar/action calculation is the same as §2, with radius `g_k`; at sufficiently small coupling also `4g_k<=a_1`, or use the fixed smaller radius (4). The proof is valid as an implication, but its `Z=integral rho_k` and `C_low` cannot mean the bare mass. The claimed logarithmic bound on `B=E_+^lin+C_low` can be retained only with the upper majorants and lower floor in the **same** vacuum convention. The ceiling and rarity consequences remain conditional on those corrected inputs. |
| **8.12 and 8.18 global quotient, probability conversion and witness inputs.** II:125874–125920,126261–126269,126313–126343,143040–143050,143410–143454,143819–143898,144437–144458. | These repeat the same division at one last lattice, and use it in the age/rarity route. Reading their effective density through Chapter 1 identifies `Z>=exp(-C_low #Lambda)` with the false bare floor; these displays do not themselves add a vacuum factor. Using all history masses and `Z` in the vacuum-normalized convention leaves the probability inequality unchanged, subject to its other named assumptions. Choosing the same lattice without also choosing the same normalization is insufficient. |
| **Volume transfer, where the factor is already retained.** II:140880–140933,141551–141565,141686–141723,141849–141851; III:72665–72686,72722–72764,72851–72879,72992–72999,73922–73937. | These passages use `Z_m(0)>=exp(E_m-C_low N_m^4)` explicitly, or a ratio where the same `E_m` cancels. Across different tori the vacuum-density difference is retained as an additional input. The axial bound refutes **none of these normalized formulations**. Their attribution to the incompatible Definition 1.5 needs correction; their vacuum-density comparison still has its own hypotheses. |
| **Inherited constants and final dependency summaries.** I:2606–2607,3336–3338; II:65222–65234,68126–68165; III:60586–60598,71449–71458,71667–71678,73461–73468,73532–73539,75693–75710,110813–110818,110950–110964. | These propagate the already formed quotient constant, floor or volume-transfer input; they supply no independent normalization repair. They remain conditional on a common normalized stability input. This check alone is neither a proof nor a counterexample to their normalized correlation conclusions. |

To make the cancellation precise, suppose at a fixed last volume `V` that the **corrected** estimates are

\[
|e^{-\mathcal E(w)}\widehat Z(w)|\le e^{AV},
\qquad \widehat Z(0)\ge e^{-BV}.
\]

Then the bare estimates have exponents `A_bare=A+E_vac/V` and `B_bare=B-E_vac/V`, so `A_bare+B_bare=A+B` and

\[
\left|e^{-\mathcal E(w)}\frac{Z_{\rm bare}(w)}{Z_{\rm bare}(0)}\right|
=\left|e^{-\mathcal E(w)}\frac{\widehat Z(w)}{\widehat Z(0)}\right|
\le e^{(A+B)V}.
\tag{22}
\]

This proves the normalization invariance of the downstream division, **not** the missing upper-history estimates. In particular, combining the bare upper bound `Z_bare<=1` with a normalized lower bound is invalid. Replacing the bare density everywhere by (17), or carrying the factor in (21) on both sides of each estimate, is the concrete repair. It is the convention already explicit in the outline and in CA-II's volume transfer. It is not an additional physical axiom, and it leaves normalized observables unchanged.

## Verdict

**(A), for the literal CA-I statement.** Definition 1.1 (I:477–481), Definition 1.5 (I:924–933), 4.33 (i-b)(1) and (i-c) (I:157084–157110), together with the account's stated small-field/background inputs, imply the false bare floor (7). The exact axial-gauge bound is (11); (14) gives a hand-proved contradiction for every admitted `K'>=1` at sufficiently small coupling. The erroneous hypothesis application is **(h4)(a)**: it uses a remaining vacuum-energy sum initialized by `E_vac`, while the stated bare recursion is initialized with zero. Equations (18)–(21) display the missing term and the corrected bound.

**The referee's stronger claim about all normalizations is wrong.** The account explicitly uses `exp[-x_0A-E_vac]` elsewhere (especially II:140916–140926), and its outline's floor is explicitly for `e^{-E}Z` (SA:23515–23527). In that convention the lower-bound argument is consistent; the correctly normalized volume-transfer uses already retain the requisite factor. Thus the finding is an actual incompatibility in the stated definitions and their application, not a refutation of the conditional normalized bounds or of all downstream conclusions. Uses through 4.31, 8.8 and LSC must carry this correction and their other hypotheses; no scientific status is granted.

**Checked line by line by Codex.** First failing step in the literal CA application: the substitution of the vacuum-normalized energy into (h4)(a), I:157039–157041, for the Chapter 1 bare density. First failing step in the checked LSC application: `library/lsc.md:214`, used at `346`, equating the vacuum-normalized zero-source integral with that unshifted Chapter 4 integral. The hand derivations (4)–(22) have no computer-assisted step.
