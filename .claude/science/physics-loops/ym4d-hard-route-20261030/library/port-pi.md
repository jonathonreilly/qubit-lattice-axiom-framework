# Port PI: Pointed irrelevance

Provenance: Codex (GPT-6), 2026-11-05; research-text port at repository commit `c04b80758f0ed2cac26749baca173a0dd8a50c4a`. Source: the complete Yang–Mills account of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at upstream revision `31a47c543775`. Tadeusz Balaban supplies the underlying background, gauge and renormalization constructions. Not an audit; no status is granted. No computer-assisted proof step or independent-provider check is claimed.

## 1. Scope and source convention

The target is `5.2:lem-pointed-irrelevance`, CA-II 4852–5030, with its scope remark at 5032–5041. This is the first port in [port-map](port-map.md) §4.1. The route is the account's expansion of Balaban's second proof in CMP 119, §3. It splits near levels, tails and a comb-gauge core, identifies the quadratic tensor, and subtracts the same member's action coefficient.

CA-I and CA-II refer to `theorem_0_complete_account_raw_I.tex` and `theorem_0_complete_account_raw_II.tex` at that upstream revision. SA refers to `YM4_sketch_500.tex`. Source lines below refer to these files, not rendered page numbers. `sa-index/ca-full/index.tsv` is a retrieval index; each used status is checked against the source. Definitions and equation labels have no row in its numbered-statement scan.

The account classifies this lemma as proved: its heading has no qualification and a proof follows. Its proof nevertheless uses cited Balaban inputs. The box proposition also explicitly admits its one-layer representation with enlargement index `1+n−j` as a hypothesis (CA-II 3975–3981, 4032–4056). This port retains that input. It does not claim to reprove the background theory or to establish the hypothesis for this repository's maps.

The two consumers are [cp12](cp12.md) §§5–6, especially D6–D8 and the Outstanding paragraphs, and [ci](ci.md) §4, equation (13), with [sfol-draft](sfol-draft.md) §§4 and 7. A per-point value estimate is different from their required switched localization and absolute carrier budget.

## 2. Inputs, with source status

“Proved in CA” reports the account's classification, not an independent check of all its antecedents. CA-I 27–75 distinguishes proofs, cited theorems, printed assertions and incomplete proofs.

| Input | CA label and source lines | Index status, checked at source; use |
|---|---|---|
| Local families, covariance, norm and coefficient convention | 5.1:def-analyticity-spaces, especially CA-II 1851–1894; 5.1:eq-analyticity-spaces-c | Definition, outside the numbered-statement index. Conditions (f1)–(f3) are hypotheses on a family. |
| Running radii and their ratio | 5.1:not-coupling-functions; 5.1:eq-coupling-functions-a and -3; CA-II 1944–2027 | Definition and following algebraic proof, no index row. The flow envelope is 5.1:eq-correlation-notation-d, CA-II 236–253. It is an input at the current induction prefix. |
| Polynomial radius growth | 4.4:lem-radii-ratio, CA-I 10224–10302 | PROVED, conditional on its slope bounds and coupling ceiling. The needed scalar calculation is written below. |
| Parameter floors | 5.1:thm-correlation-theorem, CA-II 2814–2857 | Scan: PROVED. Its source statement assumes admitted inputs and an outstanding window-data statement (2792–2812). Here only its constant order and decay floors are used, **not the correlation conclusion**. |
| Disc Taylor bounds | 5.2:lem-disc-bounds, CA-II 2974–3022 | PROVED. For an analytic function bounded by \(N\) on radius \(S\), the Taylor tail after degree two is at most \(Nu^3/(1-u)\), \(u=\lvert z\rvert/S<1\). With zero first derivative the vacuum difference is at most \(2Nu^2\). |
| Box representation, trivial-point containment and comb gauge | 5.2:prop-box-comb-gauge, CA-II 3926–4072; equations 5.2:eq-box-comb-gauge-a, -1, -2 | CITED: Balaban CMP 109 (3.18), (3.25), (3.26), (3.32), Lemma 4, pp. 276–277, (4.18), and CMP 119 (2.28), (3.68). The one-layer case at \(a=1+n-j\) is explicitly **assumed**, not printed there (4032–4055). |
| Admitted configuration inputs | 5.1:def-admitted-inputs, CA-II 2083–2121 | Definition, no index row. Its clause (a1) admits (c1)–(c3) with the stated rider; (a2) specifies the chain extensions. |
| Own-box representation | 5.2:rem-own-box, CA-II 4074–4155 | Remark, no index row. Its proof uses the preceding cited input and retains the one-layer qualification. |
| Marginal estimate and \(C_M\) | 5.2:lem-marginal-bound, CA-II 4729–4836 | PROVED, using the box proposition. Supplies the analytic path, zero linear term and \(S^{-1}\le C_MD_Xt^2\rho\). |
| Pointed/bulk coefficient identification and localization equivalence | 5.2:lem-coefficient-total, CA-II 4403–4471 | PROVED, using Balaban CMP 109 (1.20)–(1.22), (4.15), and CMP 119 (3.61)–(3.64). Equivalence is agreement up to a field-independent constant on **every** real regular torus. |
| Flat-response kernels and box-to-bulk/domain-tail comparison | CA-II 4969–4976, inside 5.2:lem-pointed-irrelevance; no separate statement label | Cited there from Balaban CMP 109 (4.35)–(4.36) and CMP 119 §3. These are analytic locality inputs, not consequences of a family supremum bound. |
| Zero linear term, colour tensor, Ward and hypercubic identities | CA-II 4781–4789, 4977–5001; equations 5.2:eq-pointed-irrelevance-3, -4 | Cited from Balaban CMP 109 (4.14), (4.15), (4.33), and CMP 119 (3.51)–(3.61). Their algebra and polynomial limits are expanded below. |
| Pointed action normalization and remainder | 5.2:eq-pointed-irrelevance-5, CA-II 5003–5011 | Cited from Balaban CMP 119 (3.66); no separate index row. It uses the actual background response and the same trace convention as extraction. |
| Rooted summability and geometry | CA-II 4871–4875, 4894–4905, 4911–4918 | Standing localization geometry, no separate label here: rooted exponential summability, diameter controlled by tree length, and \(d_j(X)\ge\nu-1\) for a domain leaving the core. |

This lists the inputs to PI, not a port of their entire dependency closure. In particular, the background proposition remains cited and its added one-layer case remains assumed. The extension to chain backgrounds has further hypotheses in 5.2:rem-chain-configurations, CA-II 4157–4331. Here (c1)–(c3) are used **when supplied**, without asserting them for every independently defined carrier.

The source's direct kernel citations have no numbered CA labels. They must not acquire fictitious index rows. Their Balaban passages were also read in the supplied text: CMP 109 (4.14)–(4.15), (4.33)–(4.36), and CMP 119 (3.49)–(3.72). The OCR supplies prose and equation navigation; garbled formulas are not quoted as verified transcriptions. The statements ported here are those printed in CA.

## 3. Statement with standing hypotheses exposed

Work in four dimensions with the account's fixed simple gauge group and invariant trace, in particular \(SU(2)\). Pairings are complex bilinear. Fix odd \(L\ge3\), then decay rates and block size \(M\), then radius constants, and finally the small-coupling ceiling. Constants may depend on these choices but not on age, depth, point or volume.

A pointed \(E\)-family \(F=\{F(X,\mathbf U,\mathbf J,y)\}\) at scale \(j\) has:

1. Local holomorphic terms on the specified \(U_j^c(X,a_j)\), with nonwrapping compatibility between tori and the infinite-lattice companion.
2. Complex gauge invariance (f2), and pointed-total covariance (f3) under unit translations, permutations and reflections. Invariance only after summing base points is weaker.
3. A whole-domain bound, including the companion,
   \[
   |F(X,\cdot,y)|\le\mathfrak n e^{-\kappa d_j(X)}.
   \tag{PI1}
   \]
4. Its own coefficient \(\beta[F]\), extracted with the actual response, and the same pointed action \(A(h_y,\cdot)\) for subtraction.

Coordinates are in level-\(j\) units. Domains are connected unions of the localization \(M\)-cubes; \(d_j(X)\) is their in-domain shortest-tree length, divided by \(M\). The point \(y\) is a unit-lattice site.
The tent is \(h_y(p)=\prod_{\ell=1}^4(1-|p_\ell-y_\ell|)_+\), evaluated at plaquette midpoints, and \(A(h_y,U)=\sum_p h_y(p)A_p(U)\).
Use the action normalization in which an affine curl has quadratic density \(\frac12\operatorname{tr}\mathcal F_{\ell\mu}^2\).
The coefficient is the mixed second moment defined explicitly in §4.6. These conventions agree with the source and with SA 5863–5925.

The pair \(a_j\) is permitted by the box proposition, not an arbitrary analytic radius. For the running choice,
\[
 a_j=\alpha_\cdot(g_j),\quad
 \rho=\rho_{n,j}=\frac{\alpha_\cdot(g_n)}{\alpha_\cdot(g_j)},\quad
 \rho^2=\frac{x_j}{x_n}
       \left(\frac{\log x_n}{\log x_j}\right)^{2q}.
 \tag{PI2}
\]
The common exponent \(q\) makes this ratio independent of the radius component.
For absolute-radius families the proof uses their actual containment radius and the permitted comparison
\(\mathfrak a_n/\alpha_{3,j}\le C\rho\). This comparison cannot be omitted.

Let \(n\ge j\), \(t=L^{j-n}\), \(\nu=1+n-j\), and let \(\mathfrak b\) be a scale-\(n\) admissible background near \(y\). Every evaluated term, including a tail term, must lie in its member domain. The core and its counterterm use one common background.

With \(\square\) the \(M\)-cube of \(y\), put
\[
 \square_0=\square^{\sim\nu+1},\qquad D=M(2\nu+3).
\]
Input (c1) represents the background on each \(X\subset\square^{\sim\nu}\), modulo gauge, by
\[
 \mathcal P_j^{\square_0}(e^{iB})
       =(U_j(\square_0,e^{iB}),J_j(\square_0,e^{iB})).
\]
Input (c2) places this pair analytically in the member domain for
\(\|B\|_\infty<\alpha_{3,j}=c_3a_j\). Input (c3) gives
\[
\begin{split}
 B_\mu^{\rm ax}(x)&=B_\mu^{\rm m}(x)+e_\mu(x),\\
 B_\mu^{\rm m}(x)&=\sum_{\ell<\mu}(x_\ell-y_\ell)\mathcal F_{\ell\mu}(y),\\
 |\mathcal F(y)|&\le\mathfrak a_nt^2,\\
 |B^{\rm ax}(x)|+|B^{\rm m}(x)|
     &\le C(1+|x-y|)\mathfrak a_nt^2,\\
 |e(x)|&\le C(1+|x-y|)^2\mathfrak a_nt^{2+\hat\alpha},
       \qquad 0<\hat\alpha<1 .
\end{split}
\tag{PI3}
\]
Here \(\mathfrak a_n=C_{\mathfrak a}\alpha_\cdot(g_n)\), and \(\mathcal F\) is curvature.
The admitted class includes the named Balaban backgrounds, specified interpolations and decouplings, preparatory/large-field chains, and stated complex-tube extensions (CA-II 3930–3954). This list does not identify a different construction's maps with them.

**Port PI (5.2:lem-pointed-irrelevance).** Under these inputs,
\[
\begin{split}
 \mathfrak i_y(\mathfrak b)
   &=\sum_{X\ni y}\{F(X,\mathfrak b,y)-F(X,1,y)\}
                          -\beta[F]A(h_y,\mathfrak b),\\
 |\mathfrak i_y(\mathfrak b)|
   &\le C_I\mathfrak n\,\nu^3\rho^2(1+\rho)t^{4+\hat\alpha}.
\end{split}
\tag{PI}
\]
The symbol \(1\) denotes the trivial pair. This is a value estimate after the complete pointed subtraction.

## 4. Proof along the account's route

### 4.1 Radius, summation and constants

The flow input is
\[
 \lambda(n-j)-2c_2\le x_j-x_n
              \le3\lambda(n-j)+2c_2,\qquad x_i\ge X_0 .
 \tag{PI4}
\]
Choose \(X_0\ge\max(e^{2q},2c_2,1)\), after \(q,c_2,\lambda\).
The derivative of \(x^{-1/2}(\log x)^q\) has the sign of \(q-\frac12\log x\), hence is nonpositive on this range.
If \(x_j\ge x_n\), then \(\rho\ge1\) and
\(\rho^2\le1+(3\lambda(\nu-1)+2c_2)/X_0\).
If \(x_j<x_n\), then \(\rho\le1\), while
\(\rho\ge\sqrt{x_j/x_n}\ge\sqrt{X_0/(X_0+2c_2)}\ge1/2\).
Thus
\[
 \tfrac12\le\rho,\qquad \rho^2\le C_\rho\nu,\qquad
 C_\rho=1+3\lambda+2c_2 .
 \tag{PI5}
\]
This makes CA-II 4880–4883 precise using the same scalar flow/radius calculation as 4.4:lem-radii-ratio.

Write \(C(s)=\sum_{X\ni y}e^{-s d_j(X)}\).
If the rooted domain count in \(m\le d_j(X)<m+1\) is at most \(C_de^{\kappa_Dm}\), then
\[
 C(s)\le C_d\sum_{m\ge0}e^{-(s-\kappa_D)m}<\infty
                  \quad(s>\kappa_D).
 \tag{PI6}
\]
Polynomial factors also sum: the ratio for \((m+1)^pe^{-am}\) is at most \(e^{-a/2}\) once \(m+1\ge2p/a\).
Here is a hand count. A tree of length \(q_XM\) has a traversal of length \(2q_XM\).
Cover this traversal by at most \(2q_X+2\) balls of radius \(M\). Each ball meets at most \(4^4\) grid cubes, so the number of cubes of \(X\) is at most \(4^4(2q_X+2)\).
The graph joining cubes that touch has degree at most \(3^4-1=80\). A deterministic spanning-tree traversal of a rooted \(v\)-cube set has \(2(v-1)\) steps, so there are at most \(80^{2(v-1)}\) codes of that length.
Summing these bounds up to the stated linear bound on \(v\) gives \(C_de^{\kappa_Dm}\) on \(m\le q_X<m+1\), for a fixed dimensional \(\kappa_D\). Multiple codes only increase this upper bound. No enumeration is used.

Take \(\kappa\ge10\log L\), with an entropy reserve such that \(C(\kappa/2)<\infty\).
Retain a positive reserve for the polynomial moments below. The account allows increasing these fixed floors and then \(M\).
For its effective boundary-decay rate \(\delta>0\), choose \(\delta M\ge5\log L\); the effective rate may be reduced from the raw response rate to pay moment sums. All these choices precede the coupling ceiling.

The comb box is permitted: \(2\nu+3\le5L^{\nu-1}\), by induction from \(\nu=1\) using \(2\nu+5\le3(2\nu+3)\le L(2\nu+3)\).
Thus \(D\le5M/t\), as (c3) requires, and \(D\le5M\nu\).

### 4.2 Near levels

Put \(u=C_MD\rho t^2\), \(C_M=2dC_{\mathfrak a}/c_3\), as in the marginal lemma.
Then
\[
 u\le A\nu^{3/2}L^{-2(\nu-1)},\qquad A=5C_MM\sqrt{C_\rho}.
\]
The ratio of consecutive sequence terms is at most \(2^{3/2}/L^2<1/3\).
Choose an integer \(\nu_*\) with \(A3^{-(\nu_*-1)}\le1/2\).
Then \(u>1/2\) implies \(\nu<\nu_*\), independently of depth.

On this finite age range, whole-domain membership gives a vacuum difference bounded by \(2C(\kappa)\mathfrak n\).
The coefficient moment estimate in §4.6 gives
\(|\beta[F]|\le C\mathfrak n\alpha_{3,j}^{-2}\).
For the action, use the same box path as in §4.3 on its fixed analytic radius \(r_A>0\).
Its first derivative is zero and its norm is fixed, as in the action input of §2.
Here \(D\le5M\nu_*\). Choose the final coupling ceiling so that \(CD\mathfrak a_n<r_A/2\) throughout this finite range; this is possible since \(g(\log g^{-2})^q\to0\).
Part (b) of the disc lemma then gives
\(|A(h_y,\mathfrak b)|\le C D^2\mathfrak a_n^2t^4\le C'\mathfrak a_n^2t^4\), with \(\nu_*\) absorbed into the fixed constant.
Hence \(|\mathfrak i_y|\le C\mathfrak n(1+\rho^2)\).
For \(\rho\ge1/2\), \((1+\rho^2)/[\rho^2(1+\rho)]\le5\).
Also \(t^{-(4+\hat\alpha)}\le L^{5\nu_*}\) on this range.
Enlarging \(C_I\) proves (PI). Actual young-age domain membership is essential.

### 4.3 Tail and analytic core

Now \(u\le1/2\). If \(X\not\subset\square^{\sim\nu}\), then \(d_j(X)\ge\nu-1\). Thus
\[
 \sum_{\rm tail}|F(X,\mathfrak b,y)-F(X,1,y)|
  \le2C(\kappa/2)\mathfrak n e^{-\kappa(\nu-1)/2}
  \le2C(\kappa/2)\mathfrak n t^5 .
 \tag{PI7}
\]
Only the member norm is used. A remote tail with no box comparison is not assigned a curvature factor.

On a core domain set
\[
 \varphi_X(z)=F(X,\mathcal P_j^{\square_0}(e^{izB^{\rm ax}}),y),
 \qquad S=\alpha_{3,j}/\|B^{\rm ax}\|_\infty .
\]
Use the constant path if \(B^{\rm ax}=0\). Otherwise (c2) gives analyticity on \(|z|<S\), with bound \(\mathfrak n e^{-\kappa d_j(X)}\).
Representation and gauge invariance give its values at zero and one.
The comb bound gives \(S^{-1}\le u\le1/2\).

Its first derivative at zero vanishes. It is a linear functional invariant under constant colour rotations. The adjoint representation of a simple Lie algebra has no nonzero invariant linear functional. For \(SU(2)\), colour half-turns change the sign of each individual component. This is the argument behind Balaban (4.14).

Cauchy's formula on radius \(r<S\), followed by \(r\uparrow S\), bounds the \(m\)-th Taylor coefficient by \(\mathfrak n e^{-\kappa d_j(X)}S^{-m}\).
Summing from \(m=3\) proves the disc lemma's bound and gives
\[
 |\varphi_X(1)-\varphi_X(0)-\tfrac12\varphi_X''(0)|
 \le2\mathfrak n e^{-\kappa d_j(X)}(C_MD\rho)^3t^6 .
 \tag{PI8}
\]

### 4.4 Replacing the comb field by its affine term

Let \(Q_X(B_1,B_2)\) be the composed second derivative at zero.
On the bidisc \(|z_i|<\alpha_{3,j}/(2\|B_i\|_\infty)\), the sum \(z_1B_1+z_2B_2\) is in the containment ball.
Two Cauchy formulas therefore give
\[
 |Q_X(B_1,B_2)|\le4\mathfrak n e^{-\kappa d_j(X)}
    \alpha_{3,j}^{-2}\|B_1\|_\infty\|B_2\|_\infty .
 \tag{PI9}
\]
Zero directions are immediate, and holomorphy makes \(Q_X\) symmetric.
The exact identity
\[
 Q_X(B^{\rm ax},B^{\rm ax})-Q_X(B^{\rm m},B^{\rm m})
       =Q_X(e,B^{\rm ax})+Q_X(B^{\rm m},e)
\]
retains both mixed terms and the error squared.
Using (PI3), the factors have bounds \(CD\mathfrak a_nt^2\) and \(CD^2\mathfrak a_nt^{2+\hat\alpha}\).
The cost is
\[
 C\mathfrak n e^{-\kappa d_j(X)}D^3\rho^2t^{4+\hat\alpha}.
 \tag{PI10}
\]

### 4.5 Box-to-bulk replacement and absolute moments

This is the cited-kernel step of CA-II 4969–4976. It is an input about Balaban's actual response, not a property of every analytic map.
Since the first derivative of the member vanishes, the second chain rule contains only two first background responses. There is no second-background-response term.
Balaban (4.35) gives this expression; the response decay and (4.36) control its change on replacing the box response by the bulk response.

Here are the summation details. Let \(h^\square,h\) denote the flat pair responses in the box and the bulk, in the norms of the cited bounds.
Their columns decay exponentially with the distance of the input bond to \(X\).
The difference \(h^\square-h\), restricted to \(X\), also decays with its distance to the boundary. The bounds include the current.
Two-variable Cauchy and those bounds give, with a reduced positive rate \(\delta\),
\[
 |K_{X,y}(b,b')|
 \le C\mathfrak n\alpha_{3,j}^{-2}e^{-\kappa d_j(X)}
  e^{-\delta\{\operatorname{dist}(b,X)+\operatorname{dist}(b',X)\}}.
 \tag{PI11}
\]
This is the quantitative form used here of the cited response input. The background kernel estimate itself is **cited**, not proved by Cauchy. Cauchy transfers it to a member's Hessian.

Since \(y\in X\) and \(\operatorname{diam}X\le C_{\rm diam}(d_j(X)+1)\), with \(C_{\rm diam}\) retaining its \(M\)-dependence,
\[
 |b-y|\le\operatorname{dist}(b,X)+C_{\rm diam}(d_j(X)+1).
\]
There are at most \(C(r+\operatorname{diam}X+1)^4\) bonds in a distance-\(r\) shell.
Summing (PI11) against any fixed polynomial in \(|b-y|,|b'-y|\) therefore costs only a polynomial in \(d_j(X)+1\).
The entropy reserve in (PI6) sums it.
In particular, the completed pointed Hessian has absolute spatial moments, and its second moment is at most
\[
 C\mathfrak n\alpha_{3,j}^{-2}.
 \tag{PI12}
\]
The same estimates justify restrictions and compatible nonwrapping lifts. They justify every rearrangement and polynomial test below.

The quadratic response difference is
\[
 D^2F_X[(h^\square-h)B^{\rm m},h^\square B^{\rm m}]
       +D^2F_X[hB^{\rm m},(h^\square-h)B^{\rm m}].
\]
Use the weighted column sums to evaluate the affine field. No unbounded field is put into a nonlinear domain.
Write \(q_X=d_j(X)\). A tree through \(y\)'s cube that reaches layer \(r\) has length at least \(M(r-1)\).
Thus the distance from \(X\) to the outer box is at least \(M(\nu-q_X)\), when this is positive, up to fixed margin conventions.
Near-boundary domains instead pay through their domain size. After reserving half the domain decay for entropy and moments, the decay factors satisfy
\[
 e^{-\kappa q_X/2}e^{-\delta M(\nu-q_X)_+}
 \le e^{-a\nu},\qquad
 a=\min\{\kappa/2,\delta M\}\ge5\log L.
 \tag{PI13}
\]
For \(q_X\le\nu\), the exponent is at least \(a[q_X+\nu-q_X]\); for \(q_X>\nu\), its first term suffices.
Fixed margin conventions only change constants or the effective rate chosen in §4.1.
The quadratic completion over omitted domains uses the same argument with the domain-tail factor.
Retaining any remaining polynomial as \((1+\nu)^p\), the total error is bounded by
\[
 C\mathfrak n\rho^2t^4(1+\nu)^p e^{-a\nu}
       \le C'\mathfrak n\rho^2t^{4+\hat\alpha}.
 \tag{PI14}
\]
Indeed \(a-\hat\alpha\log L>0\), and the polynomial/exponential estimate following (PI6) applies.
This expands the summation behind CA's exponential-error statement. It proves no identification of different response maps.

### 4.6 Tensor and coefficient

Let \(K_y\) be the completed Hessian. Constant gauge invariance makes the colour tensor scalar:
\[
 K_y^{ab;\mu\mu'}(x,x')
           =\delta_{ab}\Pi_{\mu\mu'}(x,x',y).
\]
For \(SU(2)\), colour half-turns kill off-diagonal entries; rotations interchanging axes equate the diagonal entries. The argument is complex linear and needs no positivity or reality. This is Balaban (4.33).

Differentiate local gauge invariance in a compactly supported gauge parameter \(\chi\), then in a field \(B\). Terms involving the first derivative vanish, leaving
\[
 K_y[d\chi,B]=0.
 \tag{PI15}
\]
Polynomial tests are justified as follows. Multiply a polynomial \(\chi\) by a cutoff equal to one on a radius-\(R\) box and zero outside twice that box.
Its discrete gradient has a polynomial majorant independent of \(R\).
The moments from (PI11)–(PI12) permit dominated convergence as \(R\to\infty\).
Cut off the second field too when needed. These are Hessian tests, not nonlinear substitutions.

Linear \(\chi\) gives separate zero row and column sums of \(\Pi\).
A quadratic \(\chi\) has a discrete gradient with arbitrary symmetric affine slope, plus a constant. Constants have already been annihilated.
Testing all symmetric slopes gives
\[
\begin{split}
 T_{\mu\mu',\ell\ell'}
   &:=
   \sum_{x,x'}\Pi_{\mu\mu'}(x,x',y)
                     (x_\ell-y_\ell)(x'_{\ell'}-y_{\ell'}),\\
 T_{\mu\mu',\ell\ell'}
   &=-T_{\ell\mu',\mu\ell'}
    =-T_{\mu\ell',\ell\mu'} .
\end{split}
\tag{PI16}
\]
This is the Ward step of CMP 119 (3.51)–(3.55). Pointed translation covariance makes \(T\) independent of \(y\).

Use bond midpoints under reflections. Replacing starts by midpoints adds constants to the coordinates in (PI16). Every correction vanishes by a row or column sum.
Thus the tensor has no affine offset from reversing an oriented bond.
Reflection in one axis changes a component by \((-1)^r\), with \(r\) the number of occurrences of that axis. Odd \(r\) forces zero.
Together with the two antisymmetries, this leaves two equal unordered pairs of indices. Permutations equate their coefficients, so
\[
 T_{\mu\mu',\ell\ell'}
     =b(\delta_{\mu\mu'}\delta_{\ell\ell'}
                      -\delta_{\mu\ell'}\delta_{\ell\mu'}).
 \tag{PI17}
\]
For \(\ell<\mu,\ell'<\mu'\), the crossed pairing is impossible. Therefore
\[
 \frac12\sum_{X\ni y}Q_X^{\rm bulk}(B^{\rm m},B^{\rm m})
       =\frac b2\sum_{\ell<\mu}
                       \operatorname{tr}\mathcal F_{\ell\mu}(y)^2.
 \tag{PI18}
\]

To identify \(b\), set \(y=0\) and
\(\pi_{\mu\mu'}(v)=\sum_x\Pi_{\mu\mu'}(x,x+v,0)\).
Translation covariance makes this the bulk polarization obtained by summing pointed sites.
Absolute moments justify the change of variables. Row and column sums kill the two pure-square terms, giving
\[
 \sum_v\pi_{\mu\mu'}(v)v_\ell v_{\ell'}
       =-T_{\mu\mu',\ell\ell'}-T_{\mu\mu',\ell'\ell}.
\]
For \(\mu\ne\mu'\), take \(\ell=\mu,\ell'=\mu'\). Equation (PI17) gives \(b\).
This is the mixed second moment of Balaban CMP 109 (1.22), with CA's trace convention. Thus \(b=\beta[F]\); (PI12) bounds it.
This fills the identification used by 5.2:lem-coefficient-total, with no extra colour multiplicity.

For the equivalence clause of that lemma, equivalent totals have equal finite-torus Hessians: their difference is constant.
Nonwrapping compatibility and exponential decay send the wrapping contribution to zero, including its polynomial moments.
Their limiting coefficients therefore coincide.
Agreement at one background, or an unspecified independent-current extension, is not this equivalence.

### 4.7 Pointed action and cancellation

The pointed action is exactly \(A(h_y,\cdot)\) in the subtraction.
Its coefficient is one in this normalization, as supplied by CA-II 5003–5009 / Balaban CMP 119 (3.66).
This includes normalization of the actual affine response. Gauge covariance alone would not prove it.

The unit tent factor can be checked by hand. At mesh \(\eta=1/N\), the unshifted and half-shifted one-dimensional sums are
\[
 N^{-1}\left[1+2\sum_{r=1}^{N-1}(1-r/N)\right]=1,\qquad
 2N^{-1}\sum_{r=0}^{N-1}(1-(r+1/2)/N)=1 .
\]
Their product gives \(\eta^4\sum_{p_{\ell\mu}}h_y(p)=1\).
On the normalized affine response, the quadratic plaquette term is
\(\frac12\eta^4\operatorname{tr}\mathcal F_{\ell\mu}^2\).
SA 13345–13391 also gives this calculation and retains the response normalization as a hypothesis.

Apply the same Taylor and comb replacement to the pointed action, whose radius, local support and analytic norm are fixed.
The quadratic replacement costs \(CD^3\mathfrak a_n^2t^{4+\hat\alpha}\); the cubic remainder costs \(CD^3\mathfrak a_n^3t^6\).
Since \(\mathfrak a_n\) has a fixed ceiling and \(t^{2-\hat\alpha}\le1\), the second is bounded by the first after changing the constant.
The boundary moments are handled as in §4.5.
Thus \(D\le5M\nu\) gives CA's action estimate
\[
 A(h_y,\mathfrak b)
  =\frac12\sum_{\ell<\mu}\operatorname{tr}\mathcal F_{\ell\mu}(y)^2
          +O(\nu^3\mathfrak a_n^2t^{4+\hat\alpha}).
 \tag{PI19}
\]
Multiply its remainder by
\(|\beta[F]|\le C\mathfrak n\alpha_{3,j}^{-2}\).
The result is at most \(C\mathfrak n\nu^3\rho^2t^{4+\hat\alpha}\).
The leading term cancels (PI18) exactly.

### 4.8 The five errors

The tail, cubic Taylor remainder, comb replacement, box/completion error and action remainder are bounded, respectively, by
\[
\begin{split}
 &C\mathfrak n t^5,\\
 &C\mathfrak n\nu^3\rho^3t^6,\\
 &C\mathfrak n\nu^3\rho^2t^{4+\hat\alpha},\\
 &C\mathfrak n\rho^2t^{4+\hat\alpha},\\
 &C\mathfrak n\nu^3\rho^2t^{4+\hat\alpha}.
\end{split}
\]
Core domain sums use (PI6).
Since \(\nu\ge1,\rho\ge1/2,0<t\le1,0<\hat\alpha<1\),
\[
 t^5\le t^{4+\hat\alpha}\le4\rho^2t^{4+\hat\alpha},
 \qquad
 \rho^3t^6\le\rho^2(1+\rho)t^{4+\hat\alpha}.
\]
Their sum proves (PI). Near levels were handled in §4.2.
This is a proof of the implication from §2's inputs, with their status unchanged.

CA-II 5032–5041 permits different frozen scalar-source members at different points. Each point uses its own whole covariant family's coefficient. Its core and counterterm still share a background; admissible tails can be bounded separately.
The remark sends groups cut by localization to a later lemma. It does not itself assert a carrier-norm estimate.

## 5. Check 1: frozen H-ct

**Answer: PI does not give frozen H-ct as stated.** It supplies pointed cancellation and an admissible-background value estimate of the kind used in cp12 §5. H-ct in §6 requires further formation and localization.

Put \(a=n-j=\nu-1\). PI bounds **one old base point** by
\[
 C\mathfrak n(1+a)^3\rho^2(1+\rho)L^{-(4+\hat\alpha)a}.
 \tag{PI20}
\]
A later unit window contains at most \(C(M)L^{4a}\) such points. After this count and (PI5), the bound is
\[
 C(M)\mathfrak n(1+a)^{9/2}L^{-\hat\alpha a}.
 \tag{PI21}
\]
The series converges because its consecutive-term ratio tends to \(L^{-\hat\alpha}<1\).
If \(\rho\) is bounded independently of age, the polynomial power can be \(3\).
The map's exponent \(4+\hat\alpha\) is therefore the **per-base** exponent. After counting bases it is \(\hat\alpha\), and radius growth also costs a polynomial.

cp12 Lemma 9 / (23) gives
\(C\mathsf g[\rho_j^2\sigma^{4+\alpha_{\rm H}}+\rho_j^3\sigma^6]\) under D6–D7.
With cp12's age \(m=k+1-j\) and CA's application \(n=k\), \(\nu=m\) and \(t=\sigma=L^{-(m-1)}\).
Both subtract the same member's affine quadratic coefficient and gain a positive age exponent.
They differ quantitatively: CA's box has diameter \(O(\nu)\) and contributes \(\nu^3\). cp12 uses a larger window with localized-response moment bounds.
PI does not prove cp12's sharper weight by relabelling.
At equal Hölder exponent, the ratio of (PI21) to CI's existing
\((1+a)^{3/2}L^{-\alpha_{\rm H}a}\) grows like \((1+a)^3\).
A new summable majorant, or a smaller exponent with its constants chosen in order, is possible. Neither is an automatic change to a frozen weight.

The exact H-ct target is
\[
 \sum_{Z\ {\rm connected}}F_Z(B)+{\rm const},\qquad
 F_Z=F_Z(B|_Z),\qquad |F_Z|\le R_sE_ke^{-\kappa|Z|}
\]
on \(\mathfrak B_k(2r_k^{\rm ct})\), with \(R_s=e^{\bar\kappa}\).

| Frozen requirement | Match and difference |
|---|---|
| D6: own coefficient and normalized pointed action | The same cancellation is proved in §4.6–4.7 on the CA response. The actual member, companion and response must still be identified with these objects. |
| D7: complex regularity and uniform member admission | PI uses (c1)–(c3) for admitted backgrounds. It does not prove them for the repository's switched maps or independent currents. |
| C1: doubled fluctuation ball, whole switch polydisc, rootwise budget \(E_k\) | PI can bound a pointed group when the entire parameterized image is admitted. It does not construct that image or rootwise budget. Its Taylor variable scales data, not the full switch array. |
| C2: locality on every activated subset, root component, support collar | Not asserted by PI. Locality of \(F(X)\) before composition does not establish this identity after composition. |
| C3: (24), with non-interior bases, profile/tent matching, drop-outs and aged terms | PI supplies at most the admitted regular interior contribution, with its own age weight. It does not identify or count the other terms. |
| Support relabelling/entropy in (25), Hessian bound (26), evaluation-centre coverage | These remain cp12 Theorem 10's separate steps and hypotheses. PI gives no connected-support filing or \(R_s\) factor. |

The Outstanding paragraphs at cp12 412, 457–462 and 552–566, and correction 6 at 667, therefore remain applicable. No H-ct Outstanding mark is removed.

## 6. Check 2: old families, OSF-loc and (13)

**Answer: the cited repository texts do not establish membership on their full domains. OSF-loc and transfer (13) are not replaced.** This is an unmet-hypothesis finding, not a counterexample to possible membership.

CI D1 (9–13) quantifies over every local fibre, with independent current, stored variables and complex parameters.
D2 (15–24) uses its particular switched presentation on
\(\mathbb S_{X_f}(\bar\kappa)\times\mathbb D_R\), with complete reads and component identities.

| PI hypothesis | Evidence for the old families | Conclusion |
|---|---|---|
| Holomorphic \(E\)-family and bound on the **CA** \(U_j^c(X,a_j)\) | CI carries norms on ST1-r4/R1 cores. sfol-draft Lemma 4.4 assumes [ER8u] and uniform flat-response decay to obtain its usable pair ball. | The norm has the form (PI1); the required comparison of the domains and maps is not supplied. |
| Pointed covariance (f3), preserving the total and coefficient | sfol-draft Theorem 4.3 proves cancellation after re-pointing, conditional on [TI] and its supporting inputs. | Conditional match at the flat datum, not verification for every actual member. |
| Gauge/response conventions and normalized action | sfol-draft §4.2 uses block-constant gauge invariance and the composite response. Remark 4.2 retains \(\mathfrak h_\infty\ell\), including its gradient. | A conditional composite coefficient identity; not a full CA pair-domain identification. |
| **Scale-\(n\) admissibility at every evaluation**, with (c1)–(c3), current and analytic room | sfol-draft 231–238 leaves D7 bullets 1–2 open at curved/layered data. Its §7 table retains window regularity and uniform membership; CI 271 retains them on switched balls. | **Decisive unmet application hypothesis.** The arbitrary CI pair and its switched image have not been shown to be the required CA box-background pair. |
| Uniform weighted localization | CI 259–271 asks for (13); sfol-draft §7 leaves the conversion from a per-window bound to the switched oscillation bound open. | Still required even after pointwise admissibility is established. |

The fourth row requires more than physical regularity or holomorphy. It requires the simultaneous analytic pair representation, including the current, at every switch and local fibre.
CA includes certain independent-current tube extensions; that does not prove inclusion of CI's independently defined tubes.

Equation (13) requires an **exact linear localization** of the own-subtracted total and
\[
 \sup_\Delta\sum_{f:X_f\ni\Delta}e^{\alpha|X_f|}
  \sup_{\mathbb S_{X_f}(\bar\kappa)\times\mathbb D_R}
 |\mathcal F_f(P;s,\zeta)-\mathcal F_f(P;s,0)|
 \le C_{\rm OSF}f_{n-j}\|G_j\|_{j,\kappa}.
 \tag{PI22}
\]
It must preserve the cancellation, complete seeds and component identities, pay weights and multiplicities, and reproduce the actual exponent at \(s=1\).

If both evaluations are admissible, PI gives an oscillation bound for the **complete pointed sum**, at most twice its uniform value bound.
It does not give the sum of moduli of localized pieces in (PI22). The available inequality is
\(|\sum_f a_f|\le\sum_f|a_f|\), in the opposite direction.
Thus membership alone cannot justify the map's proposed deletion of transfer (13). One also needs a bounded localization operator in the required weighted norm, or a matched CA localization theorem.

This is not a claim that CA lacks localization machinery. Its scope remark refers to the later cut-group lemma.
The map also names these statements, whose hypotheses were checked at source:

| Additional CA statement | Source/status | Relevant limitation |
|---|---|---|
| 4.7:prf-lemma-four-gaps | CA-I 30757–30803; PROVED | Uses its specified one-power hereditary source space, shift bounds and smallness conditions. |
| 4.7:prf-fundamental-share | CA-I 31304–31328; PROVED | Its shares and counterterm leftovers have the specified working radii and total-field inputs. |
| 4.7:prf-simple-share | CA-I 31437–31470; PROVED | Old-level restriction uses the displayed hereditary source and rescales the current by \(L^{-3(n+1)}\). |
| 4.7:prf-level-summation | CA-I 31677–31711; PROVED | Sums shares already supplied in that construction; it does not construct CI's presentations. |

Their source headings carry no incomplete/outstanding qualification and proofs follow. Their full proofs are not imported into PI.
They do not identify CI's domains or switched localization with their objects merely by naming them.

CI's vacuum-only defects/remainders and boundary/strip/kept budgets remain separate. PI relies on a regular family's own quadratic subtraction.
Likewise, sfol-draft §6.4's NFE/[BG-u] work concerns a larger, depth-independent near-flat domain and carried-family coefficient estimates. PI assumes its family and its admitted evaluations; it does not construct that extension.

## 7. Source and recovery record

Sources are fixed at upstream 31a47c543775:

- [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), SHA-256: 4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93.
- [CA-II](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex), SHA-256: 6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f.
- [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), SHA-256: d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f.

The outline index was consulted first: chunks 05, 06, 12 and 18, their neighbouring rows, and obligations.md.
Principal bounded source readings were SA 5863–5927, 6664–6743, 13345–13420, 13747–13763 and 19540–19671.
They establish comparison vocabulary; the port follows CA-II.

The complete PI statement/proof and each direct named input in §2 were read at source.
The map's additional share statements were read for their hypotheses, as §6 specifies; no full-proof check of those statements is claimed.
The source manifest and numbered working excerpts are in /tmp/port-pi-evidence/.
Downloaded files are /tmp/sa_ym4.tex, /tmp/sa_ca_I.tex and /tmp/sa_ca_II.tex.
Scripts only recorded identities and excerpts. All estimates above are written arguments.

**Current checkpoint.** PI is ported as an implication. Cited background/kernel inputs and the one-layer assumption retain their status.
The next application decision is whether to supply the CA-domain/map match and port its localization machinery, or keep the existing conditional CP12/CI interfaces.
Family membership and weighted transfer require proofs before either consumer can be replaced.

Only library/port-pi.md was edited. No frozen consumer, editable prompt, ledger, audit status or platform instruction was changed.

## Result

Ported CA-II 5.2:lem-pointed-irrelevance: statement, the same near-level/tail/comb-gauge/tensor proof, explicit analytic and summation steps, and the source status of each input.
Credit belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and Tadeusz Balaban for the underlying route and constructions.

**Status in their account:** PROVED, with a printed proof. This port is a research implication using cited inputs and the explicitly admitted one-layer box clause. It is not independently checked and grants no status.

**H-ct:** no, not as frozen in cp12 §§5–6. PI matches own-coefficient cancellation and supplies an admissible-background age bound. It does not supply actual C1–C3, arbitrary-subset component locality, support/entropy filing or consumer-domain coverage.

**Old families / OSF-loc / (13):** membership is not established on the full switched domains. The decisive unmet hypothesis is scale-\(n\) admissibility with (c1)–(c3), uniform core room and the actual current. Pointed covariance and core identification also retain their premises. Even after those hold, weighted localization is a further step. **OSF-loc and (13) remain in force; this port replaces neither.**
