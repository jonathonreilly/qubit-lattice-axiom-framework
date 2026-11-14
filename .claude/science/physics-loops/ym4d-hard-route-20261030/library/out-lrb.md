# The local real base of a polymer: a proof with explicit replacement estimates

Ethan and Levent,

This note completes your Proposition `4.4:prop-local-real-base` in the explicit form stated below.
Your heading at [CA-I 8110](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8110) says “Proof outstanding”.
We retain hypotheses (a)–(d), your assigned walk families, and the setting of Tadeusz Balaban's CMP 116 (2.14).
Clauses (4a)–(4b) use the written estimates (21)–(25) and (34) below in place of the unprinted lemmas.
No complete source text of those lemmas was available, so the match is to the described estimates and consumers, not word for word.
This qualification applies to the “verbatim” comparison at [CA-I 8316–8318](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8316-L8318) and the applications at [CA-I 8340–8347](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8340-L8347).

All account and outline citations refer to commit `31a47c543775`.
CA-I and CA-II denote Parts I and II of your complete account. SA denotes your outline `YM4_sketch_500.tex`.
The interpolation and Gaussian cluster integral are Balaban's CMP 116 constructions.
The walk setting follows Balaban's CMP 99b, as specified in your account at [CA-I 4875–4907](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L4875-L4907) and [CA-I 5120–5216](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L5120-L5216).
We use the quotations and formulas in your account for Balaban's papers; we did not inspect CMP 116 itself.

Your continuation already contains the symmetric-base comparison and the full-polydisc Neumann argument.
We retain those arguments and supply the crossing, product, Cauchy, and Gaussian estimates they require.
The additional hypotheses in that continuation are listed at [CA-I 8564–8575](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8564-L8575).
Your outline proves a finite-dimensional Gaussian comparison at [SA 13904–14089](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L13904-L14089).
Its covariance at [SA 14159–14218](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L14159-L14218) is the inverse of a compressed interpolated precision.
Here we interpolate your resolvent walk family itself, as required at [CA-I 8144–8169](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8144-L8169).
Your outline still identifies the actual gap and closeness estimates as obligations at [SA 14251–14270](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L14251-L14270).

## Setting and retained inputs

All matrices act on finite bond spaces, with a fixed real orthonormal basis in the Lie algebra.
Kernel absolute values are block operator norms. Transpose is bilinear transpose.
Write \(\operatorname{Re}_{\rm ent}\) for entrywise real part and \(\operatorname{sym}T=(T+T^{\mathsf T})/2\).
An accretivity inequality means \(\operatorname{Re}\langle v,Tv\rangle\ge c\|v\|^2\), with the Hermitian pairing.
We distinguish this from entrywise real parts in determinant formulas.
Distances between bonds are the \(\ell^1\) torus distances of your walk convention.
The notation \(b_-\) denotes the initial endpoint of a bond.

Use the geometry of [CA-I 8132–8169](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8132-L8169).
Let \(Z_0\in\mathbf D_k\), \(H=Z'_0\supset Z_0^{+M}\), and \(H\subset Z\subset\Omega_{k+1}\).
Here \(Z\) is a closed union of \(M_1\)-cubes; in your setting \(\mathcal S_0\), any such \(Z\) is admitted.
Let \(I=\mathbb B(Z_0)\), \(\chi=\chi_I\), and \(\chi^c=1-\chi\).
The inverse-root family lives on \(Y\), with \(\mathbb B(H)\subseteq Y\subseteq\mathbb B(T)\).
In \(\mathcal S_0\), \(Y=\mathbb B(T)\).
The parameter cubes have side \(LM\) and lie in \(Z\setminus\operatorname{int}H\).
Their parameters satisfy \(|\sigma(\Delta)|\le e^{\kappa_1}\).
A cube meets a footprint when its interior intersects that footprint.
Write \(\sigma_0\) for this parameter family.
For \(\sigma'\subseteq\sigma_0\), let
\[
W(\sigma')=\overline{Z\setminus\bigcup_{\Delta\in\sigma_0\setminus\sigma'}\Delta}.
\]
Use the prescribed family with \(W(\emptyset)=H\), as in your proposition.
All restricted sums below still omit footprints outside \(Z\).

Use your three assigned families
\[
\mathsf A,\qquad C=\mathsf R^{I}(0),\qquad \mathsf M=\mathsf M^Y.
\]
A walk footprint is the union of its step domains.
It is the closure of an open set, as required by your interpolation rule.
The length \(d(\varpi;b,b')\) is the least length of a tree containing \(b_-,b'_-\) and meeting every step domain.
Let \(m(\varpi)\) count the parameter cubes that meet this footprint.
Only readable walks enter:
\[
K(\sigma;\mathsf u)=\sum_{|\varpi|\subset Z}
K_\varpi(\mathsf u|_{|\varpi|})\prod_{\Delta\ {
m meeting}\ |\varpi|}\sigma(\Delta),
\qquad K^H(\mathsf u)=\sum_{|\varpi|\subset H}K_\varpi(\mathsf u|_{|\varpi|}).
\]
Thus \(K(0;\mathsf u)=K^H(\mathsf u)\).
This is Balaban's full-footprint interpolation, as read at [CA-I 5120–5216](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L5120-L5216).
Set
\[
C(\sigma;\mathsf u)=C(Z_0,\sigma;\mathsf u),\qquad
\Gamma(\sigma;\mathsf u)=\chi\mathsf A(\sigma;\mathsf u)\chi^c\mathsf M(\sigma;\mathsf u).
\]
Each factor receives its own interpolation multiplier.
In particular, the notation does not identify \(C(\sigma)\) with the inverse of an interpolated form.

Fix a real local base \((U|_Z,0)\).
Use your local polydiscs \(\mathbf P_{s,Z}\) from [CA-I 4608–4642](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L4608-L4642).
Their complex coordinates are \((A',\mathbf J)\), with \(\mathbf U=e^{i\xi A'}U\).
Balaban's CMP 109 (1.13) and the current part of (1.14) give their homogeneous radius bounds.
There is no extra complex plaquette constraint in these polydiscs.
Let \(\mathsf u\in\mathbf P_{\varsigma,Z}\), where \(0<\varsigma\le1+\beta\) and \(\rho\ge2\varsigma\).
No global extension of this datum is assumed.

**(a) Walk, cell, coercivity, and symmetry inputs.** Retain your hypothesis (a) at [CA-I 8111–8116](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8111-L8116) in full.
This includes the local half of W′, not just a bound for a globally summed operator.
The coefficients are analytic functions of their readable local data and have datum-independent absolute majorants.
Retain the cell-resolvent hypotheses, including local positivity, inclusion of analyticity polydiscs, and regularity.
Retain local coercivity and the symmetric-part lemma, through its polymer-base corollary.
Their relevant statements are [CA-I 5519–5578](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L5519-L5578), [CA-I 6219–6302](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L6219-L6302), [CA-I 6959–6984](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L6959-L6984), [CA-I 7162–7189](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7162-L7189), and [CA-I 7827–7988](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7827-L7988).
The full unprinted symmetry premise remains an input.

For clarity, the quantitative consequences used here are the absolute family bounds
\[
|||K|||_\theta\le B_K,\qquad
B_{\mathsf A}=\mathsf B,\quad B_C=8S/\gamma_*,\quad
B_{\mathsf M}=4S(2/\gamma_*)^{1/2},\quad \delta_{\mathsf A}\ge8\theta.
\]
They hold on \(\mathbf P_{\rho,Z}\), also for restricted readable families.
For \(\mathsf A\), the family bound holds at the stronger rate \(\delta_{\mathsf A}\).
For every admissible \(W\supset H\), the localized covariance is \(\mathsf T_W^{-1}\), with
\[
\operatorname{Re}\langle v,\mathsf T_Wv\rangle\ge(5\gamma_*/8)\|v\|^2,
\qquad \|\mathsf T_W\|\le\mathsf B.
\]
The symmetric-part input supplies the tail bounds (9), (10), and the two imaginary-kernel bounds in proof §4.
These are precisely the consequences of your polymer-base corollary used below.

Retain (k1), (k2), (k2′), and (k3), as at [CA-I 6095–6154](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L6095-L6154).
With the fixed profile \(h\) and \(c_h=\sup|h'|\), these say
\[
\begin{gathered}
r=r'+2\rho_w,\qquad \varepsilon(r')=\mathsf B e^{-\delta_{\mathsf A}r'/2},\qquad
\theta_0=\min\{\gamma_*/(4e\mathsf B r),\delta_{\mathsf A}/2\},\qquad \theta=\theta_K=\theta_0/4,\\
S=\sup_b\sum_{b'}e^{-(\theta_0/2)|b-b'|},\qquad
8S\varepsilon(r')\le\gamma_*,\\
\ell\in L^{\mathbb N},\qquad \ell\ge2r+4,\qquad
(2\mathsf B/\gamma_*)S e^{-\theta_0\ell/8}\le\tfrac12,\\
2^{d+1}c_h^2r^2\mathsf B\le\tfrac18\gamma_*\ell^2,\qquad M\ge48\ell.
\end{gathered}
\]
All step domains have sup-diameter at most \(4\ell\le M/12\).

**(b) Two parameter inequalities.** Retain exactly
\[
\theta LM\ge648\kappa_1,\qquad 243\kappa_1\le\theta M/64,
\qquad \bar\eta=e^{-\theta M/64}.
\]
Balaban's parameter order gives \(\kappa_1>0\), as read at [CA-I 1492–1496](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L1492-L1496).

**(c) Walk count.** Retain
\[
m(\varpi)\le81\left(\frac{2d(\varpi;b,b')}{LM}+1\right).
\]
The count concerns the parameter cubes of side \(LM\).
We use it as a hypothesis, exactly as in your proposition.

**(d) Three floors.** Let \(\beta=1/4\) be Balaban’s fixed schedule constant; only \(\beta\ge0\) is used here.
Retain your floors at [CA-I 7990–8108](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7990-L8108).
Set
\[
\begin{gathered}
0<\varepsilon_0^{P'}\le\min\{3,\mathsf B\},\qquad
\mathcal R_{\mathbf P}=\min\{\alpha_0'/\alpha_0,\alpha_1'/\alpha_1\},\qquad
\rho=\frac{\mathcal R_{\mathbf P}\gamma_0^X}{16\mathsf B},\\
\mathsf r_s=M/24-4\ell-3,\qquad
\mathsf r^*=\frac2\theta\log\frac{12\mathsf B}{\varepsilon_0^{P'}},\qquad
\eta_{\rm sym}=4\mathsf B e^{-\theta\mathsf r_s/2}.
\end{gathered}
\]
The floors are
\[
\bar\eta\le\varepsilon_0^{P'}/3,\qquad
\mathcal R_{\mathbf P}\ge
\frac{16\mathsf B(1+\beta)(1+3/\varepsilon_0^{P'})}{\gamma_0^X},\qquad
M\ge24(4\ell+3+\mathsf r^*).
\]
The threshold depends only on \((\mathsf B,\gamma_*,S,\theta,\delta_{\mathsf A})\).
We decrease it before choosing \(M\), as your definition permits.
The radius floor implies \(\varsigma/(\rho-\varsigma)\le\varepsilon_0^{P'}/3\) for every \(\varsigma\le1+\beta\).

**Balaban's CMP 116 (2.14) setting.** Retain the actual Mayer and contour representation, not an arbitrary potential.
Retain the potential form (1.42), the bounds (1.36), (1.43), and the fixed real cutoffs.
Their form in your account is [CA-II 3530–3537](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3530-L3537), [CA-II 3562–3567](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3562-L3567), and [CA-II 3598–3624](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3598-L3624).
Use the normalized unit auxiliary Gaussian:
\[
d\mu_0(X)=(2\pi)^{-n/2}e^{-|X|^2/2}\,dX.
\]
We retain this convention explicitly. Your account calls \(d\mu_0\) the measure of \(X\) in Balaban's CMP 116 (2.8) ([CA-I 7311](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7311)) and does not state its covariance. Your convergence test at [CA-I 8737](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8737) uses this normalization. We did not check it against CMP 116. If \(d\mu_0\) has instead a bounded covariance \(\Sigma\) fixed before \(M\), replace \(D_X\) by \(\Sigma^{1/2}D_X\Sigma^{1/2}\) in proof §7 and \(v\) by \(\|\Sigma\|v\); only early constants change.
For a possibly nonsymmetric localized matrix \(C\), use your normalized-density convention at [CA-I 7303–7364](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7303-L7364):
\[
H_C=\operatorname{sym}(C^{-1}),\qquad
d\mu_C(B)=(2\pi)^{-m/2}(\det H_C)^{1/2}e^{-B^{\mathsf T}H_CB/2}\,dB.
\]
The root continues from the positive real reference.
Retain the later ceilings on the potential parameter \(\alpha_4\) and tail parameter \(\gamma_2\).
In coarse-cube units these include their existing \((LM)^4\)-weighted ceilings.
We use Balaban's potential estimate as read at [CA-II 3710–3722](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3710-L3722); it is (36) below.

## Clauses proved

Define your local real base by
\[
T_0=\mathsf T_H(U|_H,0),\quad A_0=\operatorname{sym}\operatorname{Re}_{\rm ent}T_0,
\quad C_0^{\rm cv}=A_0^{-1},\quad
\Gamma_0=\Gamma(0;U,0),\quad G=\Gamma_0^{\mathbb R}=\operatorname{Re}_{\rm ent}\Gamma_0.
\]
Put \(\mathcal L(a)=\sup_b\sum_{b'}e^{-a|b-b'|}\) and \(\mathsf S=\mathcal L(\theta/4)\).
These lattice sums are uniform in the torus and fixed before \(M\).
The weighted Schur norm \(|K|_a\) is the maximum of its exponentially weighted row and column sums, as in (1).
For a restricted row class, both sums refer to the kernel with only those rows retained.

**(1) Base.** The operators \(A_0,C_0^{\rm cv}\) are real symmetric, and \(G\) is real. They obey
\[
\frac{5\gamma_*}{8}\le A_0\le\mathsf B,\qquad
\mathsf B^{-1}\le C_0^{\rm cv}\le\frac8{5\gamma_*},\qquad
|A_0(b,b')|\le\mathsf B e^{-\delta_{\mathsf A}|b-b'|},
\]
\[
|G(b,b')|\le|\Gamma_0(b,b')|\le
\mathsf B B_{\mathsf M}\mathsf S e^{-(\theta/2)|b-b'|}.
\]

**(2) Four displacement estimates.** These are your clauses at [CA-I 8212–8282](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8212-L8282), with the same constants.
Clause (2σ) holds on the full \(\mathbf P_{\rho,Z}\).
For \(K\in\{\mathsf A,C,\mathsf M\}\) and \(\operatorname{dist}_\infty(b_-,Z_0)\le M/4\),
\[
\begin{split}
\sum_{m(\varpi)\ge1}|K_\varpi(\mathsf u)(b,b')|e^{\kappa_1m(\varpi)}
&\le B_K\eta_1e^{-(3\theta/8)|b-b'|},\\
|[K(\sigma;\mathsf u)-K^H(\mathsf u)](b,b')|
&\le B_K\eta_1e^{-(3\theta/8)|b-b'|},\\
\eta_1=e^{81\kappa_1-\theta M/8}&\le e^{-23\theta M/192}\le\bar\eta.
\end{split}
\]
For \(C\), all rows and columns qualify, and
\[
|C(\sigma;\mathsf u)-\mathsf T_H(\mathsf u)^{-1}|_0
\le\frac{8S}{\gamma_*}e^{81\kappa_1-\theta M/4}
\le\frac{8S}{\gamma_*}e^{-47\theta M/192}.
\]
For (2U), put \(t_\rho=\varsigma/(\rho-\varsigma)\). Then
\[
|[K^H(\mathsf u)-K^H(U,0)](b,b')|\le B_K t_\rho e^{-\theta|b-b'|},\qquad
|K^H(\mathsf u)-K^H(U,0)|_0\le B_Kt_\rho.
\]
For \(K(\sigma;\mathsf u)-K(\sigma;U,0)\), replace \((B_K,\theta)\) by \((2B_Ke^{81\kappa_1},3\theta/8)\) at all rows.
At rows within sup-distance \(M/4\), replace it by \((2B_K,3\theta/8)\).
For (2s),
\[
\begin{gathered}
|T_0(b,b')-A_0(b,b')|\le4\mathsf B e^{-\delta_{\mathsf A}\max\{\mathsf r_s,|b-b'|\}}
\le\eta_{\rm sym}e^{-(\delta_{\mathsf A}/2)|b-b'|},\qquad |T_0-A_0|_0\le\eta_{\rm sym},\\
|[T_0^{-1}-C_0^{\rm cv}](b,b')|\le C_s\eta_{\rm sym}e^{-\theta_s|b-b'|}.
\end{gathered}
\]
The positive constants \(C_s,\theta_s\) depend only on \((\mathsf B,\gamma_*,S,\theta,\delta_{\mathsf A})\).
Proof §4 specifies them.
For (2Γ), at \(b\in I\),
\[
\begin{split}
|\operatorname{Im}\Gamma_0(b,b')|
&\le\mathsf B B_{\mathsf M}\mathsf S[4e^{-\theta\mathsf r_s/2}+e^{-\theta M/4}]
 e^{-(\theta/4)|b-b'|}\\
&\le B_{\mathsf M}\mathsf S(\eta_{\rm sym}+\mathsf B\bar\eta)e^{-(\theta/4)|b-b'|}.
\end{split}
\]

**(3) Coercivity on the full polydisc.** For \(\mathsf u\in\mathbf P_{\rho,Z}\) and \(|\sigma(\Delta)|\le e^{\kappa_1}\), \(C(\sigma;\mathsf u)\) is invertible and
\[
\operatorname{Re}\langle v,C(\sigma;\mathsf u)^{-1}v\rangle
\ge\tfrac12\gamma_*\|v\|^2\ge\tfrac38\gamma_*\|v\|^2.
\]
This uses (a) and (c) through (2σ), as well as (b), (k2), and (k3).
It uses none of the three floors in (d).

**(4) Applications.** Set \(\hat\varepsilon=\bar\eta+t_\rho+\eta_{\rm sym}\).
Each summand is at most \(\varepsilon_0^{P'}/3\).
For (4a), the kernel estimates and products of at most three assigned kernels hold in the two row classes.
The inverse, coupling, quadratic-form, and determinant estimates take the explicit form (19), (21)–(25) below.
Their smallness is \(C_P\hat\varepsilon\), with \(C_P\) depending only on the early constants above.
For (4b), the normalized Gaussian integral has the majorant (34).
Its real reference cancels exactly, and its auxiliary integral converges with a cost proportional to the local dimension only.
These replace the estimates described for Balaban's CMP 116 (2.16)–(2.17) and (2.23)–(2.26) in your continuation.
They retain the potential and tail inputs just stated.

For (4c), Balaban's actual functional \(f(\sigma)\), from CMP 116 (2.8)–(2.9), is analytic on a neighborhood of the closed parameter polydisc.
This holds at every admitted local \(\mathsf u\in\mathbf P_{\varsigma,Z}\) representing
\[
U^{\Sigma^1}_{k+1}(Z;(1+\beta)\alpha_0,(1+\beta)\alpha_1,\alpha_0),\qquad Z\in\mathbf D_k.
\]
For every \(Y'\in\mathbf D_k\) with \(Y'\subset Z\), restriction represents the same class on \(Y'\).
The potentials on \(Y'\subset Z_0\) therefore have their required arguments.
No extension to a global datum is needed.
The analyticity includes the Cauchy contours and implies the \(C^1\) hypothesis of your vertex formula.

## Explicit replacements for the unprinted lemmas

We number these displays (21)–(25) and (34) to make their proof counterparts easy to locate.
Let \(C=C(\sigma;\mathsf u)\), \(E'=C-C_0^{\rm cv}\), and \(a=\tfrac12\min\{\theta_s,\theta/32\}\).
Proof §6 establishes \(|E'|_a+|\Gamma-G|_a\le D_0\hat\varepsilon\).
Choose \(Q\ge1\) bounding \(|A_0|_a,|C_0^{\rm cv}|_a,|G|_a,D_0\).
Both \(D_0\) and \(Q\) depend only on the early data.
Shrink the early threshold so that \(QD_0\hat\varepsilon\le1/2\) and \(D_0\hat\varepsilon\le1\).
Then the inverse comparison and its quadratic remainder are
\[
\begin{split}
C^{-1}&=(I+A_0E')^{-1}A_0=A_0-A_0E'A_0+R_2,\\
|C^{-1}-A_0|_a&\le2Q^2D_0\hat\varepsilon,\qquad
|R_2|_a\le2Q^3D_0^2\hat\varepsilon^2.
\end{split}\tag{21}
\]
The base substitutions are
\[
C_0^{\rm cv}\ge\mathsf B^{-1}\ge\frac{5\gamma_*}{8\mathsf B^2},\qquad
1/\|C_0^{\rm cv}\|\ge5\gamma_*/8,\qquad
(C_0^{\rm cv})^{-1}=A_0,\quad
|A_0(b,b')|\le\mathsf B e^{-\delta_{\mathsf A}|b-b'|}.
\tag{22}
\]
The coupling error obeys \(|\operatorname{Re}_{\rm ent}\Gamma-G|_a\le D_0\hat\varepsilon\).
The quadratic prefactor satisfies
\[
\begin{split}
\Gamma^{\mathsf T}C\Gamma-G^{\mathsf T}C_0^{\rm cv}G
={}&(\Gamma-G)^{\mathsf T}C\Gamma
+G^{\mathsf T}(C-C_0^{\rm cv})\Gamma
+G^{\mathsf T}C_0^{\rm cv}(\Gamma-G),\\
|\Gamma^{\mathsf T}C\Gamma-G^{\mathsf T}C_0^{\rm cv}G|_a
&\le3(Q+1)^2D_0\hat\varepsilon.
\end{split}\tag{23}
\]
Thus it has exponential entrywise decay at rate \(a\), also as a form in real \(X\).
Put \(E_1=C^{-1}-A_0\) and \(E_2=\operatorname{Re}_{\rm ent}E_1\). Then
\[
\begin{split}
\det(C^{-1})&=\det A_0\,\det(I+C_0^{\rm cv}E_1),\\
\det(\operatorname{Re}_{\rm ent}C^{-1})&=\det A_0\,\det(I+C_0^{\rm cv}E_2).
\end{split}\tag{24}
\]
For every complex \(m\)-dimensional matrix \(N\) with \(\|N\|\le u\le1/2\),
\[
|\log\det(I+N)|\le m\sum_{j\ge1}\frac{u^j}{j}\le2mu.
\tag{25}
\]
The convergent logarithm fixes the branch.
After a further early threshold reduction, (24)–(25) bound the determinant quotients and their inverses by \(e^{C_P\hat\varepsilon m}\).
The same bounds hold with \(E_1,E_2\) replaced by their symmetric parts.
The latter are the determinants used by the actual normalized Gaussian density.

For the Gaussian estimate, let
\[
K=1+\mathsf B+\frac8{5\gamma_*}+\mathsf B B_{\mathsf M}\mathsf S^2,\qquad
\|C-C_0^{\rm cv}\|+\|\Gamma-G\|\le\delta=C_P\hat\varepsilon.
\]
Suppose \(F\) is Borel, \(|F(B)|\le F_*e^{\lambda|B|^2}\), and
\[
\delta\le(68K^6)^{-1},\qquad 0\le\lambda\le(16K^4)^{-1}.
\]
With \(m=\dim_{\mathbb R}B\), \(n=\dim_{\mathbb R}X\), and \(H_C=\operatorname{sym}C^{-1}\), we prove
\[
\begin{split}
&\int_{\mathbb R^n}\!d\mu_0(X)\int_{\mathbb R^m}\!
(2\pi)^{-m/2}|\det H_C|^{1/2}\\
&\quad\cdot\left|
 e^{-\frac12X^{\mathsf T}\Gamma^{\mathsf T}C\Gamma X
   -\frac12B^{\mathsf T}H_CB-B^{\mathsf T}\Gamma X}F(B)\right|\,dB
\le F_*e^{68K^6(\delta+\lambda)m}.
\end{split}\tag{34}
\]
There is no cost proportional to \(n\).
For Balaban's integrand, take \(\lambda=c_V\alpha_4+\gamma_2/2\) and \(F_*\) as in proof §7.
This keeps the failed-test factor in Balaban's CMP 116 (2.26).

**What this proof does not do.** It does not construct the primitive walk families; it uses your assigned families.
It does not establish their physical positivity, the full unprinted symmetry premise, or the CMP 116 potential bounds.
It proves the stated implication from the retained inputs.
It does not claim a literal verification of absent lemma texts, or completion of the full account.

## Proof

### 1. Norms, assigned families, and order of choice

Keep every hypothesis (a)–(d) and the setting of [CA-I 8110–8169](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8110-L8169).
In particular, keep the local half of (W′), the local cell-resolvent hypotheses,
and the hypotheses of the symmetric-base corollary.
Their conclusions are imported with those hypotheses; their upstream physical claims are not proved here.

Write \(H=Z'_0\), \(I=\mathbb B(Z_0)\), \(\chi=\chi_I\), and \(\theta=\theta_K=\theta_0/4\).
The parameter cubes are those outside \(\operatorname{int}H\).
Only these cubes contribute to \(m(\varpi)\). There are no parameter cubes inside \(\operatorname{int}H\).
This is the meaning of \(W(\emptyset)=H\) in [CA-I 8159](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8159) and of the parameter set at [CA-I 8141](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8141).
Coefficients with unread footprints are omitted before evaluation.
The parameter \(\kappa_1\) is positive in the stated Bałaban setting:
[CA-I 1492–1495](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L1492-L1495) fixes it above \(4L\kappa+1\).

For a matrix kernel use the weighted Schur norm
\[
 |K|_a=\max\left\{\sup_b\sum_{b'}|K(b,b')|e^{a|b-b'|},
 \sup_{b'}\sum_b|K(b,b')|e^{a|b-b'|}\right\}.
 \tag{1}
\]
For walk families replace the summand by its sum over \(\varpi\), weighted by
\(e^{a d(\varpi;b,b')}\). This is [CA-I 4875–4907](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L4875-L4907).
For kernels \(K,L\), the triangle inequality gives
\[
\sum_z|(KL)(b,z)|e^{a|b-z|}
\le\sum_y|K(b,y)|e^{a|b-y|}\sum_z|L(y,z)|e^{a|y-z|}.
\]
This proves the row bound \(|KL|_a\le|K|_a|L|_a\); reversing the summations proves the column bound.
For a vector \(v\), weighted Cauchy–Schwarz gives
\[
\sum_b\Bigl(\sum_{b'}|K(b,b')|\,|v(b')|\Bigr)^2
\le\Bigl(\sup_b\sum_{b'}|K(b,b')|\Bigr)
\Bigl(\sup_{b'}\sum_b|K(b,b')|\Bigr)\|v\|^2.
\]
Thus \(\|K\|\le|K|_0\le|K|_a\). These arguments also apply to rectangular kernels.

On \(\mathbf P_{\rho,Z}\), the three **assigned** families obey
\[
 |||K|||_\theta\le B_K,\qquad
 B_{\mathsf A}=\mathsf B,\quad B_C=8S/\gamma_*,
 \quad B_{\mathsf M}=4S(2/\gamma_*)^{1/2}.
 \tag{2}
\]
For \(\mathsf A\) the stronger rate is \(\delta_{\mathsf A}\ge8\theta\).
Every step domain has sup-diameter at most \(4\ell\le M/12\).
These are (W′), cell-resolvent (v), and [CA-I 7474–7491](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7474-L7491), [CA-I 7530–7540](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7530-L7540).
In particular, (2) is an absolute family bound, not merely a bound on a sum with cancellations.

Use your order, [CA-I 6095–6154](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L6095-L6154), [CA-I 7990–8050](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7990-L8050):

1. Fix \(\mathsf B,\delta_{\mathsf A},\gamma_*,\rho_w\) and the fixed profile.
   Choose \(r'\), hence \(r,\theta_0,\theta,S\), satisfying (k1).
2. Choose \(\ell\) under (k2), (k2′). All lattice sums and Gaussian comparison constants below
   depend only on these early data. In fact the comparison constants use only
   \((\mathsf B,\gamma_*,S,\theta,\delta_{\mathsf A})\).
3. Fix your positive smallness threshold \(\varepsilon_0^{P'}\), decreased as permitted by
   Definition 4.4:def-base-floors. It absorbs all comparison constants and is at most
   \(\min(3,\mathsf B)\).
4. For the already selected \(\kappa_1\), choose the allowed power \(M\) above (k3), (b),
   and the two \(M\)-floors in (d). Fix the required radius ratio
   \(\mathcal R_{\mathbf P}\) above its floor. Then choose the primed and unprimed radii
   below their ceilings, preserving this ratio.

No early constant is chosen from a later \(M\). The necessary floors exist because they
are finitely many lower bounds. The radius window opens by decreasing the unprimed radii,
as [CA-I 5822–5909](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L5822-L5909) specifies. The small potential and cutoff parameters of Balaban's
vertex integral retain their own later ceilings.

### 2. Weighted walks: clause (2σ)

Let \(d_\varpi=d(\varpi;b,b')\). If a walk meets a parameter cube, its footprint leaves \(H\).
By the meeting convention there is a parameter cube \(\Delta\) and a point \(x\in\operatorname{int}\Delta\cap|\varpi|\). Since \(\Delta\subset Z\setminus\operatorname{int}H\), we have \(x\notin\operatorname{int}H\).
Since \(H\supset Z_0^{+M}\), its sup-distance from \(Z_0\) is at least \(M\).
A tree defining \(d_\varpi\) meets the step domain containing \(x\).
Thus that tree comes within \(4\ell\) of \(x\).
If \(\operatorname{dist}_\infty(b_-,Z_0)\le M/4\), its length is at least
\[
 M-M/4-4\ell\ge 2M/3.
\]
For \(C\), every row belongs to \(I\), and the endpoint convention allows
\(\operatorname{dist}_\infty(b_-,Z_0)\le1\).
Here \(M\ge48\ell\) and \(\ell\ge2r+4>4\), so \(1\le M/4\).
In both cases the weaker bound
\[
 d_\varpi\ge M/3,\qquad d_\varpi\ge |b-b'|
 \tag{3}
\]
suffices. The same observation holds at columns of \(C\).

The assumed cube count and first inequality in (b) give
\[
 \kappa_1m(\varpi)\le81\kappa_1+
       \frac{162\kappa_1}{LM}d_\varpi
 \le81\kappa_1+\frac{\theta}{4}d_\varpi.
 \tag{4}
\]
For a contributing walk, split the remaining \(3\theta d_\varpi/4\) into two equal parts.
By (3),
\[
 e^{\kappa_1m(\varpi)-\theta d_\varpi}
 \le e^{81\kappa_1-\theta M/8}
       e^{-(3\theta/8)|b-b'|}.
 \tag{5}
\]
Multiply by \(|K_\varpi|e^{\theta d_\varpi}\), sum, and apply (2).
This proves the first bound of (2σ) with precisely
\(\eta_1=e^{81\kappa_1-\theta M/8}\).
The interpolation difference consists exactly of these walks.
The reference contribution of each is zero, so no factor two is needed.

For the Schur estimate on \(C\), spend all the remaining rate on (3).
Both the row and column sums are bounded by
\[
 |C(\sigma;\mathsf u)-\mathsf T_H(\mathsf u)^{-1}|_0
 \le \frac{8S}{\gamma_*}e^{81\kappa_1-\theta M/4}.
 \tag{6}
\]
Here the identification at \(\sigma=0\) is Corollary 4.4:cor-localised-covariance,
[CA-I 7162–7189](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7162-L7189), not an identity between interpolation and inversion away from vertices.

The second inequality in (b) is \(243\kappa_1\le\theta M/64\).
Consequently \(81\kappa_1\le\theta M/192\). Therefore
\[
 \eta_1\le e^{-23\theta M/192}\le e^{-\theta M/64}=\bar\eta,\qquad
 e^{81\kappa_1-\theta M/4}\le e^{-47\theta M/192}.
 \tag{7}
\]
These estimates hold at the full radius \(\rho\), as required.

For later use, (4) without the crossing condition gives the all-row bound
\(B_Ke^{81\kappa_1}\) at rate \(3\theta/4\).
On rows within \(M/4\), split into untagged and tagged walks.
Equations (2), (5) give the bound \(2B_K\) at rate \(3\theta/8\).
Both statements hold in Schur norm and entrywise. For the near-row statement,
the Schur norm means the kernel with those rows retained; its column sum is
also bounded by the restricted absolute family sum. For \(C\), retain all rows.

### 3. Field displacement: clause (2U)

Fix the real local \(U\) and write
\(\mathsf u=(e^{i\xi A'}U,\mathbf J)\in\mathbf P_{\varsigma,Z}\).
The radial path
\[
 z\longmapsto\mathsf u_z=(e^{iz\xi A'}U,z\mathbf J)
\]
lies in \(\mathbf P_{\rho,Z}\) for \(|z|<\rho/\varsigma\).
This follows directly from the bounds defining that polydisc;
no complex curvature constraint was added to it ([CA-I 4623–4636](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L4623-L4636)).
No extension of \(U\) outside \(Z\) occurs.

Suppose \(F(z)\) is any of the resulting matrix functions, bounded by \(D\)
on this disc in a specified Banach norm. On a circle of radius \(R<\rho/\varsigma\),
Cauchy's coefficient formula gives \(\|F_n\|\le D R^{-n}\).
Sum the positive-degree coefficients at \(z=1\), then let \(R\uparrow\rho/\varsigma\):
\[
 \|F(1)-F(0)\|\le D\sum_{n\ge1}(\varsigma/\rho)^n
      =D\,\frac{\varsigma}{\rho-\varsigma}.
 \tag{8}
\]
This also applies entrywise after multiplying by \(e^{\theta|b-b'|}\).
Use (2) for \(K^H\), and the last paragraph of proof §2 for \(K(\sigma)\).
It gives both bounds of (2U), including the stated replacements
\((2B_Ke^{81\kappa_1},3\theta/8)\) at all rows and
\((2B_K,3\theta/8)\) at controlled rows.
The factor two in the first replacement is harmless.
The Cauchy estimate is for a fixed real base and independent complex field/current coordinates.

### 4. The base and clauses (2s) and (2Γ)

We use your symmetric-base construction and its continuation at [CA-I 7827–7988](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7827-L7988) and [CA-I 8391–8562](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8391-L8562).
Set \(T_0=\mathsf T_H(U,0)\), \(A_0=\operatorname{sym}\operatorname{Re}T_0\),
\(C_0^{\rm cv}=A_0^{-1}\), and \(G=\operatorname{Re}\Gamma(0;U,0)\).

For real \(v\), local coercivity gives
\[
 v^{\mathsf T}A_0v=\operatorname{Re}(v^{\mathsf T}T_0v)
       \ge(5\gamma_*/8)|v|^2.
\]
Since \(A_0\) is real symmetric, the same lower bound holds for complex vectors.
The symmetric-base corollary supplies
\[
 A_0\le\mathsf B,\quad |A_0(b,b')|\le\mathsf B e^{-\delta_{\mathsf A}|b-b'|},
\quad
 |T_0-A_0|_0\le\eta_{\rm sym},
 \tag{9}
\]
and the stronger entry bound
\[
 |(T_0-A_0)(b,b')|\le4\mathsf B
 e^{-\delta_{\mathsf A}\max(\mathsf r_s,|b-b'|)}
 \le\eta_{\rm sym}e^{-\delta_{\mathsf A}|b-b'|/2}.
 \tag{10}
\]
Inverting the positive eigenvalues proves both covariance inequalities in (1).

Write \(\mathcal L(a)=\sup_b\sum_{b'}e^{-a|b-b'|}\).
These lattice sums are finite uniformly in the torus.
For example, lifting torus displacements to nearest representatives bounds the sum
by the corresponding sum on \(\mathbb Z^4\), times the finite bond multiplicity.
That sum factors into four convergent geometric sums.
The same argument bounds
\(S''=\sup_b\sum_{b'}|b-b'|e^{-\delta_{\mathsf A}|b-b'|/2}\).

Here is your Combes–Thomas comparison, with its constants retained.
Set
\[
 d_{\rm CT}=\min\{\delta_{\mathsf A}/2,\ 5\gamma_*/(16\mathsf B S'')\}.
\]
Conjugating \(A_0\) by \(e^{d_{\rm CT}|b-b'|}\), for a fixed column \(b'\),
changes it by a matrix of norm at most
\(\mathsf B d_{\rm CT}S''\le5\gamma_*/16\).
Indeed \(|e^t-1|\le |t|e^{|t|}\), and both Schur sums have this bound.
The conjugated matrix has inverse norm at most \(16/(5\gamma_*)\).
Thus
\[
 |A_0^{-1}(b,b')|\le\frac{16}{5\gamma_*}e^{-d_{\rm CT}|b-b'|}.
 \tag{11}
\]
Also \(|T_0^{-1}(b,b')|\le(8S/\gamma_*)e^{-\theta|b-b'|}\), by (2).
Apply
\[
 T_0^{-1}-A_0^{-1}=T_0^{-1}(A_0-T_0)A_0^{-1}.
\]
For \(a=\min(\theta,d_{\rm CT})\), convolution twice, halving the rate each time, gives
\[
 |(T_0^{-1}-C_0^{\rm cv})(b,b')|
 \le C_s\eta_{\rm sym}e^{-\theta_s|b-b'|},\quad
 \theta_s=a/4,\quad
 C_s=\frac{8S}{\gamma_*}\frac{16}{5\gamma_*}
       \mathcal L(a/2)\mathcal L(a/4).
 \tag{12}
\]
For clarity, the convolution inequality is
\(e^{-a u-a v}\le e^{-a|b-b'|/2}e^{-a u/2}\)
when \(u+v\ge|b-b'|\). This proves the remaining part of (2s).

In \(\Gamma_0\), keep the intermediate bond \(b_1\) in \(I^c\), as the definition requires.
The two factor bounds and convolution give
\[
 |\Gamma_0(b,b')|\le\mathsf B B_{\mathsf M}\mathsf S
        e^{-\theta|b-b'|/2},\qquad \mathsf S=\mathcal L(\theta/4).
 \tag{13}
\]
Taking real parts cannot increase an entry norm. This completes (1).

For (2Γ), call \(b_1\) near if
\(\operatorname{dist}_\infty(b_{1,-},Z_0)\le5M/6\).
At such bonds the symmetric-base corollary bounds
\[
 |\operatorname{Im}\mathsf M^H(b_1,b')|
 \le2B_{\mathsf M}e^{-\theta\max(\mathsf r_s,|b_1-b'|)}.
\]
At every \(b\in I\), its other bound gives
\[
 |\operatorname{Im}\mathsf A^H(b,b_1)|
 \le2\mathsf B e^{-\delta_{\mathsf A}\max(\mathsf r_s,|b-b_1|)}.
\]
At far \(b_1\), \(|b-b_1|\ge5M/6-1\ge M/2\).
Use \(\operatorname{Im}(XY)=(\operatorname{Im}X)(\operatorname{Re}Y)
+(\operatorname{Re}X)(\operatorname{Im}Y)\).
In the term containing \(\operatorname{Im}\mathsf A^H\), spend half the rate
on \(\mathsf r_s\) for all \(b_1\). Do the same in the term containing
\(\operatorname{Im}\mathsf M^H\) at near \(b_1\).
For the latter term at far \(b_1\), spend half of the first factor's rate on \(M/2\).
The remaining convolution, with rate halved once more, yields exactly
\[
 |\operatorname{Im}\Gamma_0(b,b')|
 \le\mathsf B B_{\mathsf M}\mathsf S
 [4e^{-\theta\mathsf r_s/2}+e^{-\theta M/4}]
 e^{-\theta|b-b'|/4}
 \le B_{\mathsf M}\mathsf S(\eta_{\rm sym}+\mathsf B\bar\eta)
 e^{-\theta|b-b'|/4}.
 \tag{14}
\]
Extending the restricted \(b_1\)-sums to all bonds only enlarges these nonnegative bounds.

### 5. Full-radius coercivity: clause (3)

This is [CA-I 8583–8631](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8583-L8631), now with its (2σ) input proved.
For \(\mathsf u\in\mathbf P_{\rho,Z}\), put \(T=\mathsf T_H(\mathsf u)\) and
\(E=C(\sigma;\mathsf u)-T^{-1}\).
The localised-covariance corollary gives
\(\operatorname{Re}\langle v,Tv\rangle\ge5\gamma_*|v|^2/8\) and \(\|T\|\le\mathsf B\).
Put \(t=\gamma_*/(4\mathsf B S)\le1/4\).
Here \(S\ge1\) from its diagonal summand, and the standing coercivity and norm bounds give \(\gamma_*\le\mathsf B\).
Condition (k2) says \(e^{-\theta_0\ell/8}\le t\).
Since \(M\ge48\ell\) and \(\theta=\theta_0/4\),
\[
 e^{-\theta M}\le t^{96}.
\]
Equations (6)–(7) then imply
\[
 \mathsf B\|E\|\le2t^{45/2}\le\tfrac12,\qquad
 \mathsf B^2\|E\|\le\frac{\gamma_*}{2S}t^{43/2}\le\frac{\gamma_*}{16}.
 \tag{15}
\]
The Neumann series for \(I+TE\) proves invertibility of \(C=T^{-1}(I+TE)\), and
\[
 \|C^{-1}-T\|\le
 \frac{\mathsf B^2\|E\|}{1-\mathsf B\|E\|}
 \le\gamma_*/8.
\]
Hence \(\operatorname{Re}\langle v,C^{-1}v\rangle\ge\gamma_*|v|^2/2\),
which is stronger than the printed \(3\gamma_*/8\).
This proof uses (a), (b), and (c), including (k2), (k3), and the local covariance bounds.
It does not use any floor from (d).

### 6. Products and the four perturbation estimates: clause (4a)

Here we supply the kernel and product estimates that [CA-I 8568–8572](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8568-L8572) lists as
additional inputs to its continued proof. We then follow its four steps at [CA-I 8646–8692](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8646-L8692).
Put \(t_\rho=\varsigma/(\rho-\varsigma)\).

**Products with a row near the polymer.**

Consider a product of \(p\le3\) of the assigned kernels, with any coordinate
projections between them. Retain every intermediate bond \(b_1,\ldots,b_{p-1}\)
and the separate walks \(\varpi_1,\ldots,\varpi_p\) in its expansion. Write
\[
 D=\sum_{j=1}^p d(\varpi_j;b_{j-1},b_j),\qquad
 N=\sum_{j=1}^p m(\varpi_j),\qquad B_\Pi=\prod_{j=1}^pB_{K_j}.
\]
The multiplicity in \(N\) is intentional: the interpolation is applied separately
to each factor. Applying (4) to each walk gives
\[
 \kappa_1N\le81p\kappa_1+\theta D/4.
 \tag{16}
\]
The absolute family sums with weight \(e^{\theta D}\) have both Schur sums at
most \(B_\Pi\). To see this directly, sum the last endpoint and last walk first
for the row sum, then work backwards through the factors. Each sum costs at
most its \(B_{K_j}\). For the column sum work forwards instead. A coordinate
projection only removes terms.

Suppose the initial row is within \(M/4\) of \(Z_0\) and \(N\ge1\).
Join the trees of the \(p\) walks at their common endpoints. The resulting
connected graph contains the initial endpoint and meets a step domain outside
\(H\), and its length is at most \(D\) (or arbitrarily close to it if an infimum
defines a walk length). The geometric argument of (3) gives \(D\ge M/3\).
Also \(D\ge|b_0-b_p|\). Thus
\[
 e^{\kappa_1N-\theta D}
 \le e^{81p\kappa_1-\theta M/8}e^{-(3\theta/8)|b_0-b_p|}
 \le\bar\eta\,e^{-(3\theta/8)|b_0-b_p|}.
 \tag{17}
\]
The last inequality uses \(81p\kappa_1\le243\kappa_1\le\theta M/64\);
in fact the first exponential is at most \(e^{-7\theta M/64}\).

The product at zero keeps exactly the terms with \(N=0\). Subtracting it
therefore leaves the terms estimated in (17), with no subtraction loss.
The difference has weighted Schur norm at rate \(3\theta/8\) at most
\(B_\Pi\bar\eta\), on the indicated rows. The zero product has norm at most
\(B_\Pi\) at rate \(\theta\). Since \(\bar\eta\le1\), their sum has norm at
most \(2B_\Pi\) at rate \(3\theta/8\). Without the row restriction, (16) gives
the bound \(B_\Pi e^{81p\kappa_1}\) at rate \(3\theta/4\).
These are the two required classes of product bounds.
Transposing the entire product gives the corresponding statement for a
column near \(Z_0\).

Apply the same radial Cauchy argument (8) to the product, rather than estimating
its factors one at a time at far intermediate rows. Its displacement in the
datum is bounded by \(2B_\Pi t_\rho\) in the controlled-row norm.
In particular, keeping \(\chi^c\) in the two-factor product defining \(\Gamma\),
\[
 |\Gamma(\sigma;\mathsf u)-\Gamma_0|_{3\theta/8}
 \le \mathsf B B_{\mathsf M}(\bar\eta+2t_\rho).
 \tag{18}
\]
The norm here is for the rectangular matrix whose rows belong to \(I\);
both of its Schur sums are controlled by the preceding proof.
This estimate is stronger than the rate \(\theta/32\) used at [CA-I 8678–8681](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8678-L8681).

**The covariance, inverse, coupling, and determinants.**

Choose once, before \(M\),
\[
 a=\tfrac12\min\{\theta_s,\theta/32\}>0.
\]
Equations (5), (8), (12), (14), (18), and finite lattice sums imply
\[
 |E'|_a+|\Gamma-G|_a\le D_0\hat\varepsilon,\qquad
 E'=C(\sigma;\mathsf u)-C_0^{\rm cv},\quad
 \hat\varepsilon=\bar\eta+t_\rho+\eta_{\rm sym}.
 \tag{19}
\]
Here \(D_0\) depends only on the early data displayed in the proposition.
For the first term use exactly the decomposition in [CA-I 8653–8654](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8653-L8654):
\[
 E'=[C(\sigma;\mathsf u)-\mathsf T_H(\mathsf u)^{-1}]
 +[\mathsf T_H(\mathsf u)^{-1}-T_0^{-1}]
 +[T_0^{-1}-A_0^{-1}].
 \tag{20}
\]
For the second term use
\(\Gamma-G=(\Gamma-\Gamma_0)+i\operatorname{Im}\Gamma_0\).
Every entrywise exponential used here has rate strictly larger than \(a\),
so the conversion to (19) costs only an early lattice sum.

Let \(Q\ge1\) bound \(|A_0|_a,|C_0^{\rm cv}|_a,|G|_a,D_0\);
(9), (11), and (13) supply such a \(Q\) uniformly in the regions and level.
If \(Q D_0\hat\varepsilon\le1/2\), the weighted Schur algebra gives
\[
 \begin{split}
 C^{-1}&=(I+A_0E')^{-1}A_0
       =A_0-A_0E'A_0+R_2,\\
 |C^{-1}-A_0|_a&\le2Q^2D_0\hat\varepsilon,\qquad
 |R_2|_a\le2Q^3D_0^2\hat\varepsilon^2 .
 \end{split}
\]
Indeed the terms of degree at least two are
\((A_0E')^2(I+A_0E')^{-1}A_0\).
This proves the inverse comparison and its Neumann remainder, part (i).
Its base inputs are precisely
\[
 C_0^{\rm cv}\ge\mathsf B^{-1}\ge5\gamma_*/(8\mathsf B^2),\qquad
 1/\|C_0^{\rm cv}\|\ge5\gamma_*/8,\qquad
 (C_0^{\rm cv})^{-1}=A_0,
\]
with the decay in (9); no further Combes–Thomas argument is needed.

For part (ii), taking entrywise real parts in (19) gives the bound for
\(R_3=\operatorname{Re}\Gamma-G\). For part (iii), telescope
\[
 \begin{split}
 \Gamma^{\mathsf T}C\Gamma-G^{\mathsf T}C_0^{\rm cv}G
 ={}&(\Gamma-G)^{\mathsf T}C\Gamma
   +G^{\mathsf T}(C-C_0^{\rm cv})\Gamma\\
   &+G^{\mathsf T}C_0^{\rm cv}(\Gamma-G).
 \end{split}
\]
Transposition preserves the norm (1), including for rectangular matrices.
After decreasing the threshold so that \(D_0\hat\varepsilon\le1\), all
unchanged factors have norm at most \(Q+1\). Thus (23) has norm
at most an early constant times \(\hat\varepsilon\), with exponential
entrywise decay at rate \(a\). This proves the asserted form estimate in real
\(X\), using the bilinear transpose required by the analytic prefactor.

For part (iv), set \(E_1=C^{-1}-A_0\), \(E_2=\operatorname{Re}E_1\),
where this real part is entrywise. Then
\[
 \det(C^{-1})=\det A_0\,\det(I+C_0^{\rm cv}E_1),\qquad
 \det(\operatorname{Re}_{\rm ent}C^{-1})
 =\det A_0\,\det(I+C_0^{\rm cv}E_2).
\]
If an \(m\)-dimensional matrix \(N\) has \(\|N\|\le u\le1/2\), the convergent
series for \(\log(I+N)\) proves
\[
 |\log\det(I+N)|\le m\sum_{j\ge1}u^j/j\le2mu.
\]
The determinant is nonzero throughout this ball, so this logarithm fixes
the branch. Equations (19), (21), and (25) give the determinant quotients
and their inverses a bound \(\exp(C\hat\varepsilon m)\).
The same proof applies with \(\operatorname{sym}E_1\) or
\(\operatorname{sym}\operatorname{Re}_{\rm ent}E_1\), since their norms do not
increase. These are the determinants of the actual Gaussian densities.

Thus all four estimates described in your continued proof hold with
one early constant \(C_P\hat\varepsilon\). Enlarge \(C_P\) to cover the
constants in (19)–(25), and shrink \(\varepsilon_0^{P'}\) to satisfy their
finitely many smallness inequalities. This is exactly the absorption
permitted at [CA-I 8015–8021](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8015-L8021); it happens before choosing \(M\).

### 7. The actual Gaussian integral: clause (4b)

We use the real integration argument at [CA-I 8694–8738](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8694-L8738), making its density
convention explicit. [CA-I 7313–7314](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7313-L7314) defines \(d\mu_C\) as the **normalized**
density proportional to \(\exp(-B^{\mathsf T}C^{-1}B/2)\).
Your account expressly allows a nonsymmetric localized matrix
([CA-I 7324–7364](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7324-L7364)). Therefore put
\[
 H_C=\operatorname{sym}(C^{-1}),\qquad C_s=\operatorname{sym}C.
\]
The density is
\((2\pi)^{-m/2}(\det H_C)^{1/2}
\exp(-B^{\mathsf T}H_CB/2)\).
The square root is continued from \(A_0\) using (25).
Normalization follows from the real positive Gaussian formula and
successive identity theorems in the symmetric matrix entries; this is the
argument in [SA 14023–14034](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L14023-L14034), applied to \(H_C\).
This convention matters: \(\det C^{-1}\) is not in general the normalizing
determinant when \(C\) is nonsymmetric. The algebraic estimates (24) hold
as written; the density estimates use their symmetrized versions.

For clarity we give the actual majorant, retaining the \(B\)-then-\(X\)
order of your account. Let
\[
 \mathcal J(F)=\int d\mu_0(X)\,
 e^{-\frac12X^{\mathsf T}\Gamma^{\mathsf T}C\Gamma X}
 \int d\mu_C(B)\,e^{-B^{\mathsf T}\Gamma X}F(B).
 \tag{26}
\]
This is [CA-I 7306–7314](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7306-L7314) and, at scalar parameter \(s=1\),
[CA-II 3606–3618](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3606-L3618). Take \(d\mu_0(X)=(2\pi)^{-n/2}e^{-|X|^2/2}dX\), the normalized unit Gaussian retained in the Setting. Let \(m\) be the real coordinate dimension on \(I\), and
\(n\) the dimension of \(X\). The following proof is uniform in both.

Choose the early number
\[
 K=1+\mathsf B+\frac8{5\gamma_*}
       +\mathsf B B_{\mathsf M}\mathsf S^2.
\]
It bounds \(\|A_0\|,\|C_0^{\rm cv}\|,\|G\|\), and \(A_0\ge K^{-1}\).
By (19), after an early enlargement of \(C_P\),
\[
 \|C-C_0^{\rm cv}\|+\|\Gamma-G\|\le\delta:=C_P\hat\varepsilon.
 \tag{27}
\]
Assume first that \(|F(B)|\le F_*e^{\lambda|B|^2}\), with \(\lambda\ge0\).
We will use only \(\delta\le1/(2K)\), and two explicit smaller bounds below.
The inverse identity gives
\[
 \|C^{-1}-A_0\|\le2K^2\delta,\qquad
 \|C\|,\|\Gamma\|,\|\operatorname{Re}_{\rm ent}\Gamma\|\le2K.
\]
Write
\[
 R=\operatorname{Re}_{\rm ent}H_C,\quad
 J=\operatorname{Re}_{\rm ent}\Gamma,\quad
 P=\operatorname{Re}_{\rm ent}(\Gamma^{\mathsf T}C_s\Gamma),\quad
 D_B=R-2\lambda I.
\]
These quadratic forms are real symmetric. Put
\(h=2K^2\delta+2\lambda\). If \(Kh\le1/2\), then
\[
 D_B\ge(2K)^{-1},\qquad
 \|D_B^{-1}-C_0^{\rm cv}\|\le2K^2h
       =4K^4\delta+4K^2\lambda .
 \tag{28}
\]
Taking absolute values in (26), then performing the real \(B\)-integral,
gives the bound
\[
 F_*\frac{|\det H_C|^{1/2}}{\det D_B^{1/2}}
 \int d\mu_0(X)\exp\!\left(\tfrac12X^{\mathsf T}D_X X\right),
 \qquad
 D_X=J^{\mathsf T}D_B^{-1}J-P .
 \tag{29}
\]
No contour is moved across a cutoff.

At \(\delta=\lambda=0\), \(J=G\), \(D_B=A_0\), and
\(P=G^{\mathsf T}C_0^{\rm cv}G\). Consequently \(D_X=0\).
Equivalently,
\[
 \int d\mu_{C_0^{\rm cv}}(B)e^{-B^{\mathsf T}GX}
   =e^{\frac12X^{\mathsf T}G^{\mathsf T}C_0^{\rm cv}GX},
 \tag{30}
\]
which cancels the reference prefactor exactly. This is the zeroth-order
cancellation in Balaban’s CMP 116 (2.24) and [CA-I 8700–8706](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8700-L8706).

Here is the small remainder in (29), with no reality assumption on the
true matrices. Expanding the two factors of \(J\), using
\(\|J-G\|\le\delta\), and then (28), gives
\[
 \|J^{\mathsf T}D_B^{-1}J-G^{\mathsf T}C_0^{\rm cv}G\|
 \le 10K^6\delta+4K^4\lambda .
\]
For example, the first two terms of this expansion cost
\(\delta(2K)(2K)+K(2K)\delta=6K^2\delta\), and the last costs
\(K^2(4K^4\delta+4K^2\lambda)\).
The three terms of (23), now in operator norm and with real parts,
give
\[
 \|P-G^{\mathsf T}C_0^{\rm cv}G\|\le7K^2\delta.
\]
It follows that
\[
 \|D_X\|\le v:=17K^6\delta+4K^4\lambda.
 \tag{31}
\]
If \(v\le1/2\), the remaining integral converges absolutely and equals
\(\det(I-D_X)^{-1/2}\).

These estimates give the required volume cost as well.
Over the real coordinates, \(J^{\mathsf T}D_B^{-1}J\) has rank at most
\(m\). If \(\Gamma=X_1+iX_2\) and \(C_s=C_1+iC_2\), then \(P\) factors
through the \(2m\) rows of \(\binom{X_1}{X_2}\), with middle matrix
\(\left(\begin{smallmatrix}C_1&-C_2\\-C_2&-C_1\end{smallmatrix}\right)\).
Hence \(\operatorname{rank}D_X\le3m\).
The real spectral theorem and
\(-\log(1-v)\le2v\) imply
\[
 \det(I-D_X)^{-1/2}\le e^{3mv}.
 \tag{32}
\]
Furthermore
\[
 \|C_0^{\rm cv}(H_C-A_0)\|\le2K^3\delta=:a_1,\qquad
 \|C_0^{\rm cv}(D_B-A_0)\|\le Kh=:a_2.
\]
All eigenvalues of either relative perturbation have modulus at most its
norm. Thus, for \(a_2\le1/2\),
\[
 \frac{|\det H_C|^{1/2}}{\det D_B^{1/2}}
 \le(1+a_1)^{m/2}(1-a_2)^{-m/2}
 \le e^{m(3K^3\delta+2K\lambda)}.
 \tag{33}
\]
Combining (29), (31)–(33) gives the explicit sufficient estimate
\[
 \int\!\!\int|\text{integrand of (26)}|
 \le F_*\,e^{68K^6(\delta+\lambda)m}.
\]
It has no cost proportional to the auxiliary dimension \(n\).
The inequalities used are elementary real Gaussian integration, finite
matrix algebra, and convergent series, not numerical checks.

The input \(F\) is the one in your account, not a new test integrand chosen
to replace it. [CA-II 3562–3567](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3562-L3567) and [CA-II 3600–3624](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3600-L3624) write its terms as
\[
 (-1)^{|P_{\rm fail}|}\chi_{Y_0}\chi^c_{P_{\rm fail}}\,
 \exp\!\left[\sum_{Y\in D}\tau(Y)V(Y,B)\right].
 \tag{35}
\]
Here \(D\) is the finite family of potentials in a Mayer term.
The factors \(\chi_{Y_0}\) and \(\chi^c_{P_{\rm fail}}\) impose the retained and failed cutoff tests.
The failed tests concern distinct bond blocks; \(T\) is their threshold.
The remaining cutoff factors have absolute value at most one.
The finite sums and the \(\tau\)-contours belong to Balaban's prior Mayer expansion.
In the stated setting of Bałaban (2.14), the potentials have the form and
bounds (1.42), (1.43), (1.36). We retain these inputs, exactly as [CA-II 3530–3537](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3530-L3537) does; they are not conclusions about arbitrary potentials from
(a)–(d). Their already-established bound is
\[
 \sum_{Y\in D}|\tau(Y)|\,|V(Y,B)|
 \le c_V\alpha_4|B|^2+c_V\alpha_4 M^{-4}|Y_0|.
 \tag{36}
\]
This is Balaban’s potential bound as read at [CA-II 3710–3722](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3710-L3722); \(c_V\) is an early constant.
Each failed test forces \(|B(b)|\ge T\). Pointwise, their product is at most
\[
 \exp(-\gamma_2T^2|P_{\rm fail}|/2)
 \exp\!\left(\frac{\gamma_2}{2}\sum_{b\in P_{\rm fail}}|B(b)|^2\right).
 \tag{37}
\]
Thus (34) applies with
\[
 F_*=\exp(c_V\alpha_4M^{-4}|Y_0|-\gamma_2T^2|P_{\rm fail}|/2),
 \qquad \lambda=c_V\alpha_4+\gamma_2/2.
\]
It preserves the failed-test factor of Bałaban (2.26).
Together with the determinant bounds, this proves the Gaussian estimates
described for Balaban’s CMP 116 (2.16)–(2.17) and (2.23)–(2.26), in the explicit form (21)–(25) and (34), with
\(\alpha_5=O(\hat\varepsilon)+O(\alpha_4)+\gamma_2\), as at
[CA-I 8695–8718](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8695-L8718). Fine-coordinate dimensions convert to your
volume convention with the fixed bond/color multiplicity, or one factor
of \((LM)^4\) per \(LM\)-cube. The later cluster-expansion ceilings on
\((LM)^4\alpha_4,(LM)^4\gamma_2\) are retained; no resummation claim is
inferred merely from convergence of (26).

For instance the explicit early bounds
\[
 \delta\le(68K^6)^{-1},\qquad \lambda\le(16K^4)^{-1}
 \tag{38}
\]
imply \(Kh<1/2\) and \(v\le1/2\).
Choose \(\varepsilon_0^{P'}\le(68K^6C_P)^{-1}\), along with the
earlier bounds of proof §6. Choose the later free parameters \(\alpha_4,\gamma_2\)
below the bound on \(\lambda\) and their existing ceilings.
This respects your order. The first two floors give
\(\bar\eta,t_\rho\le\varepsilon_0^{P'}/3\); the last gives
\(\eta_{\rm sym}\le\varepsilon_0^{P'}/3\), since
\[
 4\mathsf B e^{-\theta\mathsf r^*/2}
 =4\mathsf B\,\frac{\varepsilon_0^{P'}}{12\mathsf B}
 =\varepsilon_0^{P'}/3.
\]
Thus (38) is delivered by the original floors after your expressly allowed
early threshold reduction. This proves (4b).

### 8. Local admission and analyticity: clause (4c)

The potentials in (35) already depend on the local datum on \(Y\subset Z_0\).
The exterior \(\sigma\)-interpolation acts on the three Gaussian operators;
it does not substitute a new \(\sigma\)-dependent background into these
potentials. This is explicit in [CA-II 3600–3617](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L3600-L3617). The fixed real cutoffs are
kept throughout. Where a potential is only defined for \(|B|<T\) on its
support, evaluate it on that support of the cutoff and set the integrand
to zero outside it. This makes a Borel integrand, with (36) as its
majorant, without requiring analyticity of a sharp cutoff.

Use the equal-level case of Theorem 4.8:thm-restriction-units,
[CA-I 33276–33397](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L33276-L33397). A representative on \(Z\) has a fixed decomposition
\(\mathbf U=U'U\). Restrict both factors and the current to \(Y'\subset Z\).
Every plaquette, bond and cube tested there is also tested in \(Z\);
the same gauge on each tested cube supplies its gauge bound.
At equal levels there is no change in lattice units or any radius.
For the hereditary clause, a label \((p,W)\) of
\(\mathfrak T_{k+1}(Y')\) satisfies
\(W\subset Y'\subset Z\), so belongs to \(\mathfrak T_{k+1}(Z)\).
It asks for the same restriction, rule and constant
\(a_0L^{-(k+1-p)}\). All these conditions are therefore inherited,
including the strict inequalities. This proves
\[
 \mathsf u|_{Y'}\in
 U^{\Sigma^1}_{k+1}
 (Y';(1+\beta)\alpha_0,(1+\beta)\alpha_1,\alpha_0)
 \tag{39}
\]
in the sense of representatives used in the proposition.
Restriction also commutes with the gauge action, so the assertion holds
on the specified classes of orbits. Neither simple connectivity nor an
extension to the full torus is involved.
For \(Y'\subset Z_0\), (39) is exactly the admission needed in (35).

On the finite lattice the set of parameter cubes is finite.
Each assigned walk coefficient is analytic in the readable datum and
each walk multiplier is a square-free monomial in the \(\sigma\)'s.
Absolute convergence from (4) permits grouping the walks by their set
of parameter cubes. There are finitely many such sets. Consequently
each \(K(\sigma;\mathsf u)\), for fixed \(\mathsf u\), is a polynomial
in \(\sigma\), with analytic local coefficients.
This also proves analyticity in a neighborhood of the closed polydisc,
not only termwise holomorphy in its interior.

Part (3) keeps \(C\) invertible there. The bounds in proof §§6–7 leave a strict
positive margin in both real integrations. The logarithmic determinant
branch for \(H_C\) is fixed by (25); the same estimates hold on a
neighborhood of the closed polydisc, by continuity and compactness.
For fixed admissible local data the integrand in (26), (35) is analytic
in \(\sigma\) on that neighborhood and has a uniform integrable
Gaussian majorant. To see the latter before integrating, complete the
real \(B\)-square in (29): \(D_B\ge(2K)^{-1}\),
\(I-D_X\ge I/2\), and
\(\|D_B^{-1}J\|\le4K^2\). The resulting triangular change of real
coordinates has bounded inverse, so the joint real quadratic form is
bounded below by a positive early multiple of \(|B|^2+|X|^2\).
Small enlargements of the parameter set retain half this margin.
Fubini and Morera now prove analyticity of each term.
The definition also contains finitely many compact \(t(Y)\)-integrals and \(\tau(Y)\)-contour integrals.
The bound (36) holds uniformly on those contours. Integration over them therefore preserves analyticity.
The resulting finite sum is your actual \(f(\sigma)\).

At a vertex, your interpolation lemma, proved at [CA-I 5154–5194](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L5154-L5194) from the footprint convention, gives \(K(1_{\sigma'};\mathsf u)=K^{W(\sigma')}(\mathsf u)\), with \(Z\) as the ambient set.
The integral just constructed therefore is the specified vertex
functional, including its original \(F\).
Its analyticity implies the \(C^1\) hypothesis on the real parameter
cube needed by Lemma 4.4:lem-vertex-formula.
All coefficients, potential arguments, and cutoffs have used only
\(\mathsf u|_Z\). This proves all of (4c).


## Uses in your account

The following list covers the identified direct consumers of the local real base.
It states which inputs this proof supplies; the consumers retain their other hypotheses.

| Your passage | Covered here |
|---|---|
| [CA-I 8761–8837](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8761-L8837), `4.4:rem-cluster-lemmas-base` | The real pair \((G,C_0^{\rm cv})\), symmetry of \(C_0^{\rm cv}\), smallness \(C_P\hat\varepsilon\), the actual local vertex functional, and equal-level admission. These supply the described local-base inputs to Balaban's CMP 116 cluster estimates. The unprinted “word for word” statements remain subject to the explicit replacements above. |
| [CA-I 9208–9353](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L9208-L9353), `4.4:rem-cluster-lemmas-local` | Clause (1), the four perturbation estimates in the written form (21)–(25), full-polydisc coercivity, and (4c). The product estimates use \((B',\delta')=(\max\{\mathsf B,8S/\gamma_*,4S(2/\gamma_*)^{1/2}\},\theta)\). These supply the named local inputs for Balaban's CMP 116 Lemma 3 and your analogue for CMP 119 §3. |
| [CA-I 9615–9791](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L9615-L9791), `4.4:cor-localised-independence`, especially [CA-I 9665–9668](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L9665-L9668) and [CA-I 9774–9777](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L9774-L9777) | The actual vertex functional is defined at the specified local hereditary representatives, including \(\mathbf P_{1+\beta,X}\), with the required restrictions. This supplies the local-base input for the second and third parts. It does not prove the separate agreement and assembly hypotheses. |

In the second passage, your references to “(R9)” have no matching clause in this proposition.
The product and positivity arguments above use (b), together with the retained (a), (c), (k2), and (k3).
This is the reading under which the estimates serve that passage.
The three floors in (d) comprise two floors on \(M\) and one on the radius ratio.
For the third passage, retain (f1) and (f4) for operators inside previously formed potentials, as at [CA-I 9762–9767](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L9762-L9767).
The exterior interpolation does not create a new background argument inside those potentials.
This list is not a claim about every transitive use in your account.

## Who wrote and checked this

Codex wrote the proof and this note. Claude (Opus 5.5) checked the proof and this note line by line, and its repairs are applied.
These are model readings of research text, not human review or an audit. They grant no scientific status.
Every proof step above is a written argument. No computer-assisted step discharges an obligation.
