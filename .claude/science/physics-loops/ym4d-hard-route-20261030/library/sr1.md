# SR1 — All-state transfer, graded bounds and growth

Provenance: Codex (GPT-6 family; exact runtime variant and effort not exposed), 2026-11-05. Phase A, pass 2, at `1724d326aee3af902e55c00bd248cf6ef6099e03`. Distilled from the Codex notes [d2-d4.md](d2-d4.md) and [growth-qf3.md](growth-qf3.md), read whole with [bridge-check.md](../gates/bridge-check.md) and [cluster-check.md](../gates/cluster-check.md). Those notes were checked line by line by Claude Opus 5.5, first failing step none, as implications from their named inputs. This assembled part has not been refereed. Research text, not an audit; it grants no status. Every proof below is a hand argument.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. Their source revision is `31a47c543775`. The source concordance below records the bounded excerpts checked. The skeleton is [ym4-assembly.md](ym4-assembly.md), §§4–5, SR1; [assembly-status.md](assembly-status.md), SR1, records the remaining upstream dependence on UV1.

## Definitions and imports

**Lattice and fields.** Use $SU(2)$, normalized Haar measure, and the Wilson weight $e^{-\beta\sum_p a_p}$, where
\[
 a_p(U)=1-\tfrac12\operatorname{Re}\operatorname{Tr}U(\partial p)\in[0,2],
 \qquad \mathcal O_K(f)=\sum_p f(x(p))a_p.
 \tag{1}
\]
Here $U(\partial p)$ is the ordered boundary-link product, with $U(y,x)=U(x,y)^{-1}$. The index $p$ runs over unoriented plaquettes, with six plane types, and $x(p)$ is its barycentre. There is no $a_K^4$ in (1). Set $a=a_K=L^{-K}\le1$, $a_s=L^{-s}$, and $M=L^{m_0}$. A first-passage datum means a supplied datum of IN1: for its actual coefficient sequence $x_j$,
\[
 K=\min\{j:x_j\le g^{-2}+B_\sharp\},\qquad x_0=\beta.
\]
Existence of that sequence is upstream. The transfer only uses the resulting pair $(a,\beta)$.

**States and tests.** A periodic Wilson Gibbs state is a probability measure on the infinite bond configuration space. Conditional on bonds outside any finite bond set $\Lambda$, its inside law has density proportional to $\exp[-\beta\sum_{p:\partial p\cap\Lambda\ne\varnothing}a_p]$ against product Haar measure, with the exterior bonds fixed. This is the DLR condition. The state has a finite-index translation period. Write its class as $\mathcal G_{a,\beta}$. Both the evaluating state $\rho$ and the centering state $\nu$ belong to this class at the same datum. Put
\[
 t_f=\|f\|_\sharp=\max(\|f\|_\infty,c_M\|\nabla f\|_\infty),
 \qquad \Phi_K^\nu(f)=\mathcal O_K(f)-\nu(\mathcal O_K(f)),
 \tag{2}
\]
with fixed $c_M>0$. For Lipschitz source profiles, replace the gradient norm by the Lipschitz constant. Tests are real $C_c^1(\mathbb R^4)$. Each support has its own radius-$R$ ball, with arbitrary centre. Separation $d>0$ means distance between distinct supports, not between ball centres. Complex tests are treated by multilinear extension. Define
\[
 \kappa_n^\rho(Y_1,\ldots,Y_n)
 =\left.\partial_1\cdots\partial_n
       \log\rho(e^{\sum_i z_iY_i})\right|_{z=0}.
 \tag{3}
\]
The logarithm in (3) is only local at zero. At fixed cutoff all observables in (1) are bounded. The generating function is entire and equals one at zero.

**LG1.** We import finite-torus reflection positivity at coordinate *link* planes (S1d), and all-lattice-isometry invariance and reflection positivity of every periodic Wilson state (S1g). Reflection positivity means $\langle\overline{F\circ\theta}F\rangle\ge0$ for bounded functions of the appropriate half-space bonds. Finite-torus reflection invariance is included. S1e, the complex chessboard inequality, is proved in Lemma 2; it is not a further import.

**UV1, in the full D1 consumer form.** All the following hold uniformly over the supplied first-passage data and compatible cofinal tori $\ell=2L^m$, $m\ge m_0$. A fixed board of side $l=L^j\ge a$ tiles every sufficiently large such torus with even cell counts. Keep every scale $0\le s\le K$.

For every finite real Lipschitz torus family $f_i$, and $W=\sum_i z_if_i$ with $\sum_i|z_i|t_{f_i}<2r_{\rm src}$, require
\[
 \begin{split}
 |Z_{K,\ell}(W)|&\le
 \exp\{V_{K,\ell}+\operatorname{Re}[U_{K,\ell}(W)+
             \sum_{s,X}e_{K,\ell,s,X}(W)]+C_+\ell^4\},\\
 Z_{K,\ell}(0)&\ge e^{V_{K,\ell}-C_-\ell^4}.
 \end{split}                                                    \tag{4}
\]
Here $Z(W)/Z(0)=\langle e^{\mathcal O_K(W)}\rangle$, $V$ is real, and $r_{\rm src},A_{\rm src},C_\pm$ are fixed positive constants. The source radius $r_{\rm src}$ is distinct from IN1's logarithmic threshold exponent $r$.

The point term is $U(W)=\sum_pu_p(W(x(p)))$. Each $u_p$ is holomorphic and vanishes at zero. Its bounds on smaller discs are uniform in $p,\ell$ at fixed $K$, but may grow with $K$. Each domain energy is holomorphic, vanishes at zero, and obeys
\[
 |e_{s,X}(W)|\le A_{\rm src}e^{-\kappa m(X)},\qquad
 \operatorname{diam}X^+\le C_{\rm dep}a_s(m(X)+1).                \tag{5}
\]
It depends only on $W|_{X^+}$, independently of the list representing $W$. Domain sums converge normally on smaller source balls. In particular, they vanish when $W|_{X^+}=0$. The source class includes the global Lipschitz profiles formed by mirror copying, with conjugation on odd copies.

The *actual rooted geometry* is part of this import. Domains $X$ are indexed by nonempty finite unions of cubes of side $Ma_s$. Their size $m(X)$ is the least number of edges of a connected cubical edge tree meeting every cube of $X$. The region $X^+$ is contained in a fixed number of neighbouring cube layers. The rate $\kappa$ exceeds a valid rooted entropy rate $\kappa_D$, including every extra domain-type multiplicity. The weaker ST6 estimate is also available:
\[
 \sum_{X:X^+\cap B(R)\ne\varnothing,\ m(X)\ge t}e^{-\kappa m(X)}
 \le C(R+1)^4a_s^{-4}e^{-ct}.                                    \tag{6}
\]
Lemma 5 supplies its sharper small-ball version from the stated geometry.

**Outstanding — UV1.** Equations (4)–(6), their actual source-locality and indexing realization, and their uniformity remain imports. This part does not prove them. The skeleton's shorthand involving $\log Z$ is used here only through the raw upper bound and floor (4), as in the checked note. No logarithm on the whole source ball is assumed.

**Limit and test spaces.** A separated limit is a family
\[
 S_n(f_1,\ldots,f_n)=\lim_{j\to\infty}
       \rho_j\!\left(\prod_i\Phi_{K_j}^{\nu_j}(f_i)\right),
 \qquad K_j\to\infty,                                           \tag{7}
\]
on every separated compact tuple, with $a^{(j)}=L^{-K_j}$, $\rho_j,\nu_j\in\mathcal G_{a^{(j)},\beta_j}$, and common source constants. Its existence is not asserted here. Set $S_0(1)=1$. Multilinearity is required only when all supports occurring in the identity remain separated; (7) has this property. Write
\[
 \Delta_n=\bigcup_{i<j}\{x_i=x_j\},\qquad
 \mathcal S_{\ne,n}=\{\varphi\in\mathcal S(\mathbb R^{4n}):
          \partial^\alpha\varphi|_{\Delta_n}=0\text{ for every }\alpha\},
 \quad
 p_q(\varphi)=\max_{|\alpha|\le q}\sup_x
       (1+|x|^2)^{q/2}|\partial^\alpha\varphi(x)|.                 \tag{8}
\]
For $n=1$, $\Delta_1=\varnothing$. Degree-zero tests are scalars, with $p_q(c)=|c|$. The positive-time subspace $\mathcal S_{\ne,+,n}$ also has all jets zero wherever some $x_{i,4}\le0$. A separated tensor is $f_1\otimes\cdots\otimes f_n$ with smooth compact pairwise separated factors. Let $\theta(x_1,x_2,x_3,x_4)=(x_1,x_2,x_3,-x_4)$, acting on each slot. Compact RP means nonnegativity of
\[
 \sum_{m,n=0}^N S_{m+n}(\theta\overline{F_m}\otimes F_n)          \tag{9}
\]
for finite sequences of finite sums of compact positive-time separated tensors. Cross groups are separated by their time gaps. Lemma 10 proves the required cross-diagonal flatness for the extended form. Compact RP is a necessary input to RP transfer. For (7) it follows from LG1 and the moving-test argument given there.

## Order of constants

Keep [IN1, Constant order](in1.md#constant-order), including Amendment 1, unchanged. Its order for the imported packages is:

| Order | Choices retained from IN1 |
|---|---|
| 1 | Reserve, rarity loss, margins, Hölder and finite source/age requirements; power-count constants, then $r,p_0,p_1,q,\kappa_0$. |
| 2 | Geometric and hull constants; odd $L\ge27$, including $L>L_0^\natural$; flat and averaging constants, $c_0,c_2$, and the weak flow bounds. |
| 3 | Gauge/inverse ceilings; propagator, profile and walk rates; local $M_1,R_1,\rho$; seam and tower bounds and radii. |
| 4 | Early matrix and Gaussian bounds; geometric constants and $W_0$; $\kappa$, including its entropy floors and $\kappa\ge\kappa_0^\natural(L)$; then $\Theta,\lambda$. |
| 5 | $\bar\kappa,\kappa_1$, response parameters, preparation constants; then $M=L^{m_0}$ above its floors. |
| 6 | Post-$M$ chart/comparison constants and tilt; $A_1$ before $A_0$, $C_0$ before $C_1$; absolute radii, ceilings and radius ratios. |
| 7 | List and boundary budgets, certificate and entropy constants, volume costs, and the final reserve coefficient $c_1$, in IN1's internal order. |
| 8 | Remaining source, floor, flow-error and tube constants. In particular the full D1 constants $c_M,r_{\rm src},A_{\rm src},C_\pm$, dependence-layer bounds and any remaining counting constants are fixed before $X_0$. Their admissibility retains the earlier entropy floors. |
| 9 | $X_0$, then $\gamma=X_0^{-1/2}$, then the returned flow bounds $\varsigma,\lambda_\sharp,B_\sharp$. |
| 10 | $0<g\le\gamma$, compatible torus/grid data and $\beta\ge g^{-2}+B_\sharp$; the actual first-passage datum. |

The full inequalities and definitions in that IN1 table are retained as imported parameter conditions; this table does not assert their construction. In particular no later choice of $M$, test, or cutoff repairs an earlier entropy floor. Conditional on this ordered source package, fix once the partitions and cutoffs below. Lemma 5 then determines $Q_0,p$; set $k=\lceil p\rceil+5$. Lemmas 4 and 6 determine $C_B$ and $B(R)=C_B(R+1)^4$; the radius-one bound determines $b_0$, then Lemma 9 determines $C_{\rm E}$. These constants precede $n,R,d$, positions, and states. Auxiliary boards and partitions may depend on those test data. No choice feeds back into IN1. Unspecified $C,c>0$ depend only on the fixed source/geometric data and cutoffs, unless subscripts state otherwise.

## Theorem 1 (SR1)

Source: the SR1 statement in the skeleton, with the hypotheses and corrections in [d2-d4.md](d2-d4.md), [growth-qf3.md](growth-qf3.md), [bridge-check.md](../gates/bridge-check.md), §1, and [cluster-check.md](../gates/cluster-check.md), Part B.

Assume the full D1 form of UV1 above and LG1, with constants in the stated order. Let $\rho,\nu\in\mathcal G_{a_K,\beta}$ be at the same supplied first-passage datum. For the tests in (2), uniformly in cutoff, both states and support positions:

1. **SA-D4.** $|\nu(\mathcal O_K(f))-\rho(\mathcal O_K(f))|\le C_1(R)\|f\|_\sharp$, where $C_1(R)\le C(R+1)^4$. If both states are invariant under all plaquette isometries, $|\nu(a_p)-\rho(a_p)|\le Ca_K^4$.
2. **G4.** For $n\ge2$, $|\kappa_n^\rho(\mathcal O_K(f_1),\ldots,\mathcal O_K(f_n))|\le C_n(d;R)\prod_i\|f_i\|_\sharp$. The cell normalizers in Lemma 3 are holomorphic and common to all states at the datum.
3. **D2.** With $B(R)=C_B(R+1)^4$ and $k=\lceil p\rceil+5$,
   \[
   \left|\rho\prod_{i=1}^n\Phi_K^\nu(f_i)\right|
   \le B(R)^n(n!)^k\max\{1,d^{-5n}\}\prod_i\|f_i\|_\sharp.       \tag{10}
   \]
   For $n\ge2$, cumulants obey (10) with $B(R)$ replaced by $2B(R)$. For $n=1$, no separation is required and the maximum is replaced by one.
4. **H1.** Every existing limit (7) extends uniquely from smooth separated tensors to $\mathcal S_{\ne,n}$, with
   \[
   |S_n(\varphi)|\le C_{\rm E}^n(n!)^{k+32}
      \sup_{|\alpha|\le20n,x}(1+|x|^2)^{10n}|\partial^\alpha\varphi(x)|.
                                                                    \tag{11}
   \]
   Finite sums of separated tensors are dense in this space. The positive-time version has strictly positive-time factors. Compact RP transfers to finite sequences in $\mathcal S_{\ne,+,n}$. The same constants apply to any component *realized by limits of the all-state moments (7)*; no component realization is proved here.

*Proof.* Lemmas 2–4 prove clause 1 and the common-normalizer assertion. Lemmas 5–6 prove clauses 2–3. Lemmas 7–10 prove clause 4, including the compact-RP hypothesis and its verification for (7). No lemma constructs UV1 or a vanishing-spacing sequence. \(\square\)

## Lemma 2 (chessboard and arbitrary-state domination)

Source: [d2-d4.md](d2-d4.md), §2; [bridge-check.md](../gates/bridge-check.md), §1, including its S1d/S1e correction. SA ST1–ST4.

A cell function uses only bonds wholly inside its open cell. Copy it by coordinate face reflections, conjugating copies with odd reflection parity. For $N=(\ell/l)^4$, set
\[
 P_{l,\ell}(F)=\left\langle\prod_C F^{[C]}\right\rangle_\ell^{1/N}.
\]
Then
\[
 \left|\left\langle\prod_C F_C\right\rangle_\ell\right|
 \le\prod_C P_{l,\ell}(F_C),\quad
 P(F+G)\le P(F)+P(G),\quad P(zF)=|z|P(F),\quad
 P(\bar F)=P(F),\quad P(1)=1.                                  \tag{12}
\]
For finitely many nontrivial factors and every compatible sequence $\ell_j\to\infty$,
\[
 \left|\rho\left(\prod_C F_C\right)\right|
       \le\liminf_j\prod_C P_{l,\ell_j}(F_C).                   \tag{13}
\]

*Proof.* Split the disseminated product at opposite faces. It is $\Theta\Psi\,\Psi$, where $\Theta F=\overline{F\circ\theta}$ for the splitting reflection, so LG1 makes the integral nonnegative. In one coordinate there are $q$ slabs, $q$ even. Transport the profiles to a reference slab and retain their labels. Divide each occurrence of label $i$ by $(Z_i^{\rm dis}+\epsilon)^{1/q}$, where $Z_i^{\rm dis}\ge0$ is its disseminated expectation. There are finitely many fillings. Reflection Cauchy–Schwarz gives $T^2\le T_+T_-$ for the maximum absolute normalized value $T$. Both reflected fillings have nonnegative values at most $T$; hence they also maximize if $T>0$. The normalization factors multiply correctly because the two reflected fillings contain each original factor twice. Reflect a half beginning at a constant run. Until the run contains a half, its length doubles. Once it contains a half, reflection makes the filling constant. Every constant filling has value at most one. Let $\epsilon\downarrow0$, including zero disseminated integrals. Repeating in four commuting coordinate directions gives exponent $1/N$ per original cell and the first inequality in (12).

Expand the disseminated product of $F+G$ and apply that inequality term by term. The binomial sum proves the triangle inequality. Half the copies are conjugated, giving absolute homogeneity. Conjugation of the nonnegative integral gives $P(\bar F)=P(F)$. Thus $P(\operatorname{Re}(e^{-i\phi}F))\le P(F)$.

Fix $a,\beta,l$. For bounded real cell $H$, sum its $N$ mirror copies over a large cube. LG1 makes their mean $N\rho(H)$. Conditional Jensen and DLR bound this by the largest conditional logarithmic exponential moment. Replacing the exterior condition by periodic bonds changes at most $C(\ell/a)^3$ plaquettes. Each action changes by at most $2\beta$. Compare numerator and denominator, adding dummy Haar variables if needed; source factors remain unchanged. Division by $N$ gives
\[
 \rho(H)\le\log P_{l,\ell}(e^H)+C\beta l^4a^{-3}\ell^{-1}.       \tag{14}
\]
For real $G$, put $H=\log(1+tG)$, $0<t<(2\|G\|_\infty)^{-1}$. Use $H\ge tG-Ct^2\|G\|_\infty^2$ and $\log P(1+tG)\le tP(G)$. First send $\ell_j\to\infty$, then $t\downarrow0$. This proves the one-cell bound for $G$. Rotate a complex $F$ by the phase of $\rho(F)$ and use the real-part bound.

Enclose the occupied cells strictly inside a larger aligned cell of an allowed side. Its ratio to $l$ is a power of the odd integer $L$, so coarse reflections belong to the fine board's reflection group. Apply the one-cell bound to the product. On each large torus, disseminate the coarse cell, apply (12) on the fine board, and take the coarse root. Each occupied profile contributes $P_{l,\ell}(F_C)$; inactive cells contribute one. This proves (13). The volume limit in (14) precedes every cutoff limit. \(\square\)

## Lemma 3 (common holomorphic cell normalizers)

Source: [d2-d4.md](d2-d4.md), §3; [bridge-check.md](../gates/bridge-check.md), §1. SA ST7–ST9 and ST11.

For any finite test family there is a holomorphic $E$, with $E(0)=0$, common to every state at the datum, such that
\[
 h_\rho(z)=e^{-E(z)}\rho(e^{\sum_i z_i\mathcal O_K(f_i)}),
 \qquad h_\rho(0)=1,\quad |h_\rho(z)|\le Q_{n,R},
 \qquad \sum_i|z_i|t_{f_i}<r_{\rm src}.                          \tag{15}
\]
The finite $Q_{n,R}$ is uniform in cutoff and positions. The normalizer itself need not be cutoff bounded.

*Proof.* First place $m$ radius-$R$ support balls in one cell, with face margin $b>2$. Their source $w=\sum_i z_if_i$ disseminates as
\[
 W^{\rm ch}=\sum_i z_iH_i^++\sum_i\bar z_iH_i^- .
\]
The real even/odd profiles vanish near faces and have sharp norms at most $t_{f_i}$. Their combined source-list norm is at most $2\sum_i|z_i|t_{f_i}$. Thus (4) applies on the disc used in (15). All source plaquette bonds lie inside the open cells.

Retain every point term and domain term whose complete dependence region lies in one open cell. For each retained odd-cell term, conjugate its value; then sum over cells and divide by $N$. Denote the result by $E_{C,\ell}(z)$. An odd-cell term is $g(\bar z)$; its conjugate is holomorphic in $z$ and has the same real part. Source representation independence ensures that this term depends only on the source in that cell. Thus the retained real part is $N\operatorname{Re}E_{C,\ell}$ and $E_{C,\ell}(0)=0$.

A nonzero discarded term sees a support and has a dependence point outside that support's cell. Its diameter is at least the face margin. By (5), $m(X)\ge cb/a_s-C$. Apply (6) once per support copy. The normalized upper bound and floor in (4) give
\[
 \begin{split}
 P_{l,\ell}(e^{\mathcal O_K(w)})
   &\le e^{\operatorname{Re}E_{C,\ell}(z)+B_C},\\
 B_C&=(C_++C_-)l^4+
       CA_{\rm src}m(R+1)^4\sum_{s\ge0}a_s^{-4}e^{-c'b/a_s}.
 \end{split}                                                     \tag{16}
\]
The scale sum converges: $a_s^{-4}=L^{4s}$, while the exponential decays as $e^{-c'bL^s}$. No point term with nonzero source is discarded.

At fixed $K$, the point bounds and (6), summed over $s\le K$, bound $E_{C,\ell}$ locally uniformly in $\ell$. Cauchy's formula gives derivative bounds on smaller source balls. Equicontinuity, Arzelà–Ascoli, and a countable compact exhaustion give a locally uniform convergent subsequence. Cauchy's formula makes its limit $E_C$ holomorphic. For finitely many occupied cells choose one common subsequence. It depends on the torus normalizers, not on any Gibbs state.

For arbitrary support positions choose an allowed $l$ with $l\le C_Ln(R+b+1)$ and an offset giving every support ball margin $b$. In one coordinate the forbidden offsets number at most $n(2(R+b)/a+2)$. Choosing $l$ above a fixed multiple of $n(R+b+1)$ leaves a link-plane offset; rounding up to a power of $L$ costs at most $L$. There are at most $n$ occupied cells. Apply (13) along the common subsequence, then (16), with $E=\sum_C E_C$ and $Q_{n,R}=\exp(\sum_C B_C)$, enlarged to a uniform bound. Boundedness of each observable makes its exponential series locally uniformly convergent, proving the holomorphy in (15). \(\square\)

## Lemma 4 (one-point transfer)

Source: [d2-d4.md](d2-d4.md), §3, (8) and the plaquette argument; [bridge-check.md](../gates/bridge-check.md), §1, nonnegative-bump correction. SA ST14 and D4.

Clause 1 of Theorem 1 holds.

*Proof.* In (15) with one test, Cauchy's formula gives
\[
 |\rho(\mathcal O_K(f))-E_f'(0)|\le Q_{1,R}t_f/r_{\rm src}.
\]
Subtract the same estimate for $\nu$, with the same $E_f$. A fixed nonnegative compact smooth bump, positive on a unit cube, divided by the positive periodic sum of its integer translates gives a partition of unity. That denominator has a positive minimum and bounded derivatives. Only $C(R+1)^4$ pieces meet a radius-$R$ support; each product with $f$ has sharp norm at most $Ct_f$ and support of fixed radius. Applying the preceding estimate to those pieces gives $C_1(R)\le C(R+1)^4$.

If both states are invariant under all plaquette isometries, let $\Delta=\rho(a_p)-\nu(a_p)$, independent of $p$. Choose a fixed compact smooth $f\ge0$ everywhere, with $f\ge1$ on a unit cube. For sufficiently small $a$, coordinate interval counting gives at least $ca^{-4}$ plaquette centres in that cube. Hence
\[
 |\Delta|\,ca^{-4}\le |\Delta|\sum_p f(x(p))
   =|\rho(\mathcal O_K(f))-\nu(\mathcal O_K(f))|\le C.
\]
For the remaining $a\ge a_0>0$, use $|\Delta|\le2\le2a_0^{-4}a^4$. \(\square\)

## Lemma 5 (rooted counting and polynomial cell loss)

Source: [d2-d4.md](d2-d4.md), §4; [bridge-check.md](../gates/bridge-check.md), §1. SA GS1–GS4.

The rooted geometry gives, uniformly in scale and torus,
\[
 \begin{split}
 \sum_{X:X^+\cap B(u)\ne\varnothing,\ m(X)\ge t}e^{-\kappa m(X)}
      &\le C(1+u/a_s)^4e^{-ct},\\
 \sum_Xe^{-\kappa m(X)}&\le C\ell^4a_s^{-4}.
 \end{split}                                                     \tag{17}
\]
If $v$ has support in a radius-$\delta$ ball with face margin $\delta$ in a side-$\eta$ cell, where $16a\le\delta\le\eta\le1$, then
\[
 P_{\eta,\ell}(e^{z\mathcal O_K(v)})
  \le e^{\operatorname{Re}E_{v,\ell}(z)}
              Q_0(\eta/\delta)^p,\qquad |z|<r_{\rm src}/t_v,       \tag{18}
\]
for fixed $Q_0\ge1$, $p\ge0$. For every finite list of such pieces the limiting univariate normalizers can be chosen on a common, state-independent subsequence.

*Proof.* Root a minimizing edge tree at a corner of a specified cube $Q\subset X$. There are at most sixteen choices. Traversing each edge twice gives a walk of length $2m$, with at most $8^{2m}$ choices. Every cube meeting a grid edge contains a vertex. At most $16(m+1)$ cubes contain vertices of this walk. Choosing a subset therefore gives
\[
 \#\{X:Q\subset X,\ m(X)=m\}
   \le16\,8^{2m}2^{16(m+1)}.                                    \tag{19}
\]
This includes $m=0$ and finite cubical quotients. Thus $2\log8+16\log2$ is an admissible geometric entropy rate, with a fixed prefactor. Use the rate $\kappa_D$ in D1 after including extra types. The strict gap $\kappa-\kappa_D>0$ makes its weighted tail geometric.

If $X^+$ sees $B(u)$, one cube of $X$ is within $CMa_s$ of that ball. Coordinate interval counts give at most $C(1+u/a_s)^4$ possible roots. Sum (19) at those roots to get the first line of (17). Sum instead over all torus cubes to get the second.

Apply the normalizer construction in Lemma 3 at face margin $\delta$. A discarded nonzero domain has $m(X)\ge c\delta/a_s-C$. Its cost per cell is bounded in three ranges:
\[
 \begin{array}{c|c|c}
 \text{range}&\text{cost at one scale}&\text{total cost}\\ \hline
 a_s\ge\eta&CA_{\rm src}(\eta/a_s)^4&CA_{\rm src}\\
 \delta\le a_s<\eta&CA_{\rm src}
                  &CA_{\rm src}[1+\log(\eta/\delta)]\\
 a_s<\delta&CA_{\rm src}(1+\delta/a_s)^4e^{-c'\delta/a_s}
                  &CA_{\rm src}.
 \end{array}                                                     \tag{20}
\]
The first row uses the *global* count, divided by $(\ell/\eta)^4$. The second and third count once per support copy with the local count. The coarse sum is geometric. For the fine sum compare with $\sum_{j\ge0}(1+L^{j+1})^4e^{-c''L^j}$. It converges by hand: the binomial expansion gives $L^j\ge3^j\ge2j(j-1)$, so the exponent eventually dominates every linear function of $j$. Point terms stay inside cells, and the stability cost is $(C_++C_-)\eta^4\le C_++C_-$. Exponentiating a bound $C_a+C_b\log(\eta/\delta)$ proves (18), with $Q_0=e^{C_a}$, $p=C_b$. Fixed-cutoff normalizer compactness is exactly Lemma 3's argument. \(\square\)

## Lemma 6 (graded moments and cumulants)

Source: [d2-d4.md](d2-d4.md), §5; [bridge-check.md](../gates/bridge-check.md), §1. The logarithm partition identity is from that note's §3. SA GS5–GS13 and ST12.

Clause 3 of Theorem 1 holds. Its cumulant estimate also proves clause 2 with
$C_n(d;R)=[2B(R)]^n(n!)^k\max(1,d^{-5n})$.

*Proof.* Omit zero tests. For $n\ge2$, set $\bar d=\min(d,1)$ and choose a power of $L$ with
\[
 \bar d/(16L)<\eta\le\bar d/16,\qquad \delta=\eta/(64n).            \tag{21}
\]
First suppose $a\le\delta/16$. Scaling Lemma 4's smooth partition gives $f_i=\sum_qv_{i,q}$, with
\[
 \#\{q:v_{i,q}\ne0\}\le C(1+R/\delta)^4,\quad
 \operatorname{supp}v_{i,q}\subset B_{i,q}(\delta),\quad
 t_{v_{i,q}}\le C\delta^{-1}t_{f_i}.                              \tag{22}
\]
The count is a four-dimensional count of partition centres. The derivative loss follows from the product rule.

Select one piece from each test. Per coordinate, a ball excludes at most $4\delta/a+2$ link-plane offsets if its face margin is to be $\delta$. All balls together exclude at most
\[
 n(4\delta/a+2)\le(33/512)\eta/a<\eta/a.
\]
Thus an offset exists. Distinct original tests occupy distinct cells, since a side-$\eta$ cell has diameter $2\eta<d$. Write the selected pieces as $v_i$. Lemma 5 gives $r_i=r_{\rm src}/t_{v_i}$, normalizers $E_i$, and $Q_i\le Q_0(64n)^p\le Cn^p$.

For every active subset $A\subset\{1,\ldots,n\}$, apply (13) to its separate cell factors along a common normalizer subsequence:
\[
 \left|e^{-\sum_{i\in A}E_i(z_i)}
        \rho(e^{\sum_{i\in A}z_i\mathcal O_K(v_i)})\right|
 \le\prod_{i\in A}Q_i,\qquad |z_i|<r_i.                          \tag{23}
\]
This is a product polydisc. Each factor uses only its own source radius; no combined-source constraint is imposed. Inactive factors equal one. The same $E_i$ work for $\nu$.

Put $X_i=\mathcal O_K(v_i)-E_i'(0)$. Differentiate once in each active variable in (23). Product Cauchy, with radii tending to $r_i$, gives
\[
 |\rho\prod_{i\in A}X_i|\le\prod_{i\in A}Q_i/r_i,\qquad
 |\nu(\mathcal O_K(v_i))-E_i'(0)|\le Q_i/r_i.                     \tag{24}
\]
Only first derivatives of the univariate normalizers occur. Expanding the product centered at $\nu$ over active subsets gives $2^n\prod_iQ_i/r_i$. Sum over the piece choices in (22), using linearity of centering:
\[
 |\rho\prod_i\Phi_K^\nu(f_i)|
 \le[C(R+1)^4n^p\delta^{-5}]^n\prod_it_{f_i}
 \le[C'(R+1)^4]^n n^{(p+5)n}\bar d^{-5n}\prod_it_{f_i}.          \tag{25}
\]
Each piece choice may use its own board; the bounds do not depend on that choice.

If $a>\delta/16$, at most $C(1+R/a)^4$ plaquette centres meet a radius-$R$ ball. Thus
\[
 \|\Phi_K^\nu(f)\|_\infty\le C(R+1)^4a^{-4}t_f
                         \le C'(R+1)^4\delta^{-4}t_f.
\]
Its product is bounded by (25), since $\delta\le1$ and $n^p\ge1$. This handles prospective boards finer than the lattice.

The inequality $\log n!\ge\int_1^n\log x\,dx\ge n\log n-n$ gives
$n^{(p+5)n}\le e^{kn}(n!)^k$ for $k=\lceil p\rceil+5$. Absorb $e^k$ and Lemma 4's constant into $C_B$. This proves (10), including $n=1$.

Put $G(z)=\rho(e^{\sum_i z_iY_i})$. Expanding $\log(1+(G-1))$ at $G(0)=1$ gives the following identity, where $\pi$ runs over set partitions of $\{1,\ldots,n\}$:
\[
 \kappa_n^\rho(Y_1,\ldots,Y_n)
  =\sum_{\pi}(-1)^{|\pi|-1}(|\pi|-1)!
                     \prod_{D\in\pi}\rho\!\left(\prod_{i\in D}Y_i\right).
                                                                    \tag{26}
\]
Indeed, a squarefree coefficient of $(G-1)^m$ chooses $m$ ordered nonempty blocks; the logarithm coefficient $(-1)^{m-1}/m$ gives the stated weight. Constant shifts change only the linear part of the logarithm. For $n\ge2$, center at $\rho$ and apply (10) to each block. Since $\prod_D|D|!\le n!$,
\[
 \begin{split}
 \sum_\pi(|\pi|-1)!\prod_{D\in\pi}(|D|!)^k
 &\le(n!)^{k-1}\sum_{m=1}^n\frac{n!}{m}\binom{n-1}{m-1}\\
 &\le2^{n-1}(n!)^k.
 \end{split}                                                       \tag{27}
\]
To obtain the first-line sum, order the blocks and choose their positive sizes. There are $\binom{n-1}{m-1}$ compositions. For each composition, assigning labels and multiplying by the block factorials gives $n!$; divide by $m!$ and multiply by $(m-1)!$. The product of the separation losses is $\bar d^{-5n}$. This proves the cumulant bound with $2B(R)$ and no extra factorial. \(\square\)

## Lemma 7 (controlled cutoffs and tensor consistency)

Source: [growth-qf3.md](growth-qf3.md), §§1–2; [cluster-check.md](../gates/cluster-check.md), Part B. SA QF1 and QF5–QF7.

Every existing limit (7) has admissibly complex-multilinear forms with
\[
 |S_n(f_1,\ldots,f_n)|\le b_0^n(n!)^k
       \max(1,d^{-5n})\prod_i\|f_i\|_1,\qquad
 \|f\|_1=\max(\|f\|_\infty,\|\nabla f\|_\infty),                  \tag{28}
\]
on independently placed unit-radius supports; for $n=1$ omit separation. It defines a consistent functional on finite sums of separated tensors. There exist fixed cutoffs in $[0,1]$, with derivatives of order $q$ bounded by $C^q(q!)^2$ for $q\ge1$, having the properties used below.

*Proof.* Pass (10) to each tuple limit. Expand real and imaginary parts and use fixed norm equivalence, absorbing the factor $2^n$ into $b_0$. This uses the full moment bound directly; no second moment–cumulant conversion is needed.

Here is a cutoff construction and its derivative proof. Let $\mathfrak a(t)=e^{-1/t}$ for $t>0$, zero otherwise. On $|z-t|=t/2$,
$\operatorname{Re}(1/z)\ge2/(9t)$. Cauchy's formula gives
\[
 |\mathfrak a^{(q)}(t)|\le q!(2/t)^qe^{-2/(9t)}
                         \le C^{q+1}(q!)^2.                    \tag{29}
\]
The last inequality maximizes $t^{-q}e^{-c/t}$ and uses $(q/e)^q\le q!$. All derivatives tend to zero at the join. Put
$s(t)=\mathfrak a(t)/(\mathfrak a(t)+\mathfrak a(1-t))$, with values zero and one beyond $[0,1]$. The denominator $D$ is at least $d_0=e^{-2}$ there. For $H=1/D$, differentiating $DH=1$ gives
\[
 \frac{|H^{(q)}|}{(q!)^2}\le d_0^{-1}
    \sum_{r=1}^q
       \frac{|D^{(r)}|}{(r!)^2}
       \frac{|H^{(q-r)}|}{((q-r)!)^2}\binom qr^{-1}.              \tag{30}
\]
If $|D^{(r)}|/(r!)^2\le AB^r$, induction gives
$|H^{(q)}|/(q!)^2\le d_0^{-1}\Lambda^q$ with
$\Lambda=B(1+2A/d_0)$: the remaining geometric sum is at most $1/2$. Leibniz proves the same derivative bound for $s$.

Choose an even $\eta_0$, equal to one on $[-1,1]$, zero outside $[-2,2]$, using $s(2-|t|)$ in between. Set
\[
 \psi(t)=\eta_0(2t),\quad
 \chi_1(t)=\frac{\psi(t)}{\sum_{z\in\mathbb Z}\psi(t-z)},\quad
 \chi(u)=\prod_{\mu=1}^4\chi_1(u_\mu),\quad
 \chi^+(u)=\prod_{\mu=1}^4\eta_0(u_\mu),\quad \zeta=1-\chi^+.     \tag{31}
\]
The denominator is at least one and has at most three local terms. The preceding reciprocal argument applies. Thus $\sum_{z\in\mathbb Z^4}\chi(u-z)=1$, $\chi^+=1$ on $\operatorname{supp}\chi$, and $\zeta$ is zero for $|u|_\infty\le1$ and one for $|u|_\infty\ge2$. For $N$ factors at scale $h$, Leibniz gives
\[
 |\partial^\alpha F|\le(CN)^q(q!)^2h^{-q},\qquad q=|\alpha|.
                                                                    \tag{32}
\]
An absolute prefactor is allowed at $q=0$. The multinomial coefficients sum to $N^q$, and the product of the assigned order factorials is at most $q!$. Undifferentiated factors cost one. Pair differences introduce only signs; there is no $C^N$ loss.

For tensor consistency, take a finite relation and choose $d$ smaller than all its separations. Localize each slot by a finite partition on sets of diameter below $d/8$. If two slot sets have distance below $d/2$, every original tensor has a zero localized factor: two nonzero factors would put points of its original supports less than $d/2+d/4<d$ apart. Otherwise the slot spaces are separated, and admissible multilinearity factors through their algebraic tensor product. That tensor product embeds in functions. Indeed, on each finite-dimensional factor span, point evaluations span the dual; otherwise a nonzero function would vanish at every point. Choose evaluation bases in all slots to recover every tensor coefficient. A zero function therefore has zero value. Summing the localizations proves consistency. \(\square\)

## Lemma 8 (local Fourier extension)

Source: [growth-qf3.md](growth-qf3.md), §3; [cluster-check.md](../gates/cluster-check.md), Part B. SA QF8–QF9. The explicit box sizes also retain the clarification in [bridge-check.md](../gates/bridge-check.md), §2.

The form in Lemma 7 extends consistently to a functional $T$ on $C_c^\infty(\Delta_n^c)$. Let $0<h\le1/16$, $\epsilon=h/64$, and suppose the expanded cubes $Q_i^+=c_i+[-2\epsilon,2\epsilon]^4$ have pairwise distance at least $h/2$. For $u$ supported in $\prod_i(c_i+[-\epsilon,\epsilon]^4)$,
\[
 |T(u)|\le(Cb_0)^n(n!)^k h^{-6n}J_{8n,\epsilon}(u),\qquad
 J_{q,\epsilon}(u)=\max_{|\alpha|\le q}
                      \epsilon^{|\alpha|}\|\partial^\alpha u\|_\infty.
                                                                    \tag{33}
\]

*Proof.* Take the Fourier series of $u$ on the product of period-$8\epsilon$ cubes:
\[
 \widehat u(\mathbf v)=(8\epsilon)^{-4n}
   \int_{\prod_i(c_i+[-4\epsilon,4\epsilon]^4)}
    u(x)\exp\!\left[-\frac{i\pi}{4\epsilon}
                   \sum_i v_i\cdot(x_i-c_i)\right]dx .
\]
In $y_i=(x_i-c_i)/(4\epsilon)$, integrate by parts with
$\prod_i(1-\pi^{-2}\Delta_{y_i})^4$. The coefficient sum of this differential operator is at most $C^n$. Consequently
\[
 |\widehat u(\mathbf v)|\le C^nJ_{8n,\epsilon}(u)
                                \prod_i(1+|v_i|^2)^{-4}.        \tag{34}
\]
Multiply each Fourier exponential by $\chi^+((x_i-c_i)/\epsilon)$. It has $C^1$ norm at most $C\epsilon^{-1}(1+|v_i|)$ and support in $Q_i^+$, which fits inside a unit-radius ball. The one-slot series
$\sum_{v\in\mathbb Z^4}(1+|v|)(1+|v|^2)^{-4}$ converges: the shell $|v|_\infty=r\ge1$ has at most $Cr^3$ points and summand at most $Cr^{-7}$. Using (28), the series of tensor evaluations is absolutely convergent, and gives (33). Its losses are $h^{-5n}$ for separation and $h^{-n}$ for the tensor norms.

These localized Fourier series converge to $u$ with every derivative. Extra integration by parts gives absolute convergence for each differentiated series. To identify its sum, the period-two Fejér kernel
$F_N(t)=N^{-1}|\sum_{r=0}^{N-1}e^{i\pi rt}|^2$ has integral one on $[-1,1]$ with measure $dt/2$, and
$F_N(t)\le[N\sin^2(\pi\varepsilon/2)]^{-1}$ for $\varepsilon\le|t|\le1$. Its mass concentrates at zero. Products have the same property in each fixed dimension. Uniform continuity on the near region and the vanishing mass on its complement prove convergence of convolution to the function. The cutoffs equal one on the inner support and vanish before the next periodic copy, so the localized series equals $u$ everywhere.

For a tensor in the inner box, Fourier coefficients factor. The individual series converge in $C^1$. A telescoping multilinear difference and (28) show that $T$ agrees with $S_n$ on that tensor. In an overlap, cover a compact support by smaller product boxes whose expanded closures stay inside both original inner boxes. Their Fourier tensors have the same evaluations under both functionals. Convergence in every derivative and (33) pass this equality to the local test. A finite partition of unity and common refinement therefore glue the local functionals independently of the cover. Partitioning each slot of any larger separated tensor into small pieces proves agreement with all prescribed tensor values. \(\square\)

## Lemma 9 (quantitative diagonal-flat extension)

Source: [growth-qf3.md](growth-qf3.md), §4; [cluster-check.md](../gates/cluster-check.md), Part B. SA QF10–QF19.

There is a continuous extension $\Sigma_n$ to $\mathcal S_{\ne,n}$, agreeing on smooth separated tensors, with
$|\Sigma_n(\varphi)|\le C_{\rm E}^n(n!)^{k+32}p_{20n}(\varphi)$.

*Proof.* Put
\[
 h_j=2^{-j}/16,\quad \epsilon_j=h_j/64,\quad
 P_h(x)=\prod_{i<l}\zeta((x_i-x_l)/h),\quad
 D_0=P_{h_0},\quad D_j=P_{h_j}-P_{h_{j-1}}\ (j\ge1),
 \quad \chi_{j,z}(x)=\prod_i\chi(x_i/\epsilon_j-z_i).             \tag{35}
\]
Off the diagonals, $\sum_jD_j=1$. The fine layers and their derivatives are supported where
\[
 h_j\le\min_{i<l}|x_i-x_l|_\infty\le4h_j.                        \tag{36}
\]
For $n=1$, the empty product is one and all fine layers vanish. Retain a box when $\chi_{j,z}D_j$ is nonzero. At some point of it the pair distances exceed $h_j$. Thus its centres have sup-distance at least $h_j-2\epsilon_j$, and its expanded slot cubes have distance at least $h_j-6\epsilon_j>h_j/2$. Lemma 8 applies to $u_{j,z}=\chi_{j,z}D_j\varphi$.

There are at most $Cn^2$ pair and grid factors. A fine $D_j$ is a difference of two products, costing at most a factor two. For derivatives through order $8n$, (32) gives a scaled cost at most
\[
 (Cn^2)^{8n}((8n)!)^2\le C^n(n!)^{32}.                          \tag{37}
\]
Indeed $n^{16n}\le e^{16n}(n!)^{16}$, and
$(8n)!/(n!)^8\le8^{8n}$ because that multinomial coefficient counts only some words on eight letters. These account for sixteen factorial powers each.

At a point of a fine layer, replace one member of a closest pair by the other. The resulting $y$ is diagonal and $|x-y|\le8h_j\le1/2$. All jets vanish at $y$. For $|\alpha|\le8n$, Taylor's integral remainder with $m=10n+2$ gives
\[
 |\partial^\alpha\varphi(x)|
 \le \frac{(16h_j)^m}{m!}\,C^{20n}
          (1+|x|^2)^{-10n}p_{20n}(\varphi).                    \tag{38}
\]
Only four coordinates move, with total absolute displacement at most $16h_j$. Every segment point $w$ satisfies $1+|x|^2\le3(1+|w|^2)$. The derivative order is $8n+m=18n+2\le20n$. All these extra costs are exponential in $n$.

In $J_{8n,\epsilon_j}$, the scale factors cancel the inverse powers from cutoff derivatives. Leibniz costs at most $2^{8n}$; remaining positive powers of $h_j$ can be dropped. Equations (37)–(38) give
\[
 J_{8n,\epsilon_j}(u_{j,z})
 \le C^n(n!)^{32}h_j^{10n+2}p_{20n}(\varphi)
       \sup_{\operatorname{supp}\chi_{j,z}}(1+|x|^2)^{-10n}.     \tag{39}
\]
For $j=0$ omit $h_j^{10n+2}$ and use the ordinary Schwartz bound.

The position sum costs at most $C^nh_j^{-4n}$. In fact
\[
 (1+\textstyle\sum_i|x_i|^2)^{-10n}
       \le\prod_i(1+|x_i|^2)^{-10},\qquad
 \sum_{z\in\mathbb Z^4}(1+|\epsilon z|^2)^{-10}
       \le C\epsilon^{-4}\quad(0<\epsilon\le1).                \tag{40}
\]
For the second inequality, compare each centre weight with the integral over its side-$\epsilon$ cube. Weights have a fixed ratio there; the integral is finite since its exterior radial bound is $C\int_1^\infty r^{3-20}dr$. The same comparison controls the supremum on a partition box. Taking products proves the claimed sum, with no $n^2$ exponent in the constant.

Combine (33), (39) and (40):
\[
 \sum_z|T(u_{j,z})|
 \le C^n(n!)^{k+32}p_{20n}(\varphi)\,
             h_j^{10n+2-6n-4n}
 =C^n(n!)^{k+32}p_{20n}(\varphi)h_j^2\quad(j\ge1).             \tag{41}
\]
The coarse bound omits $h_j^2$; all fixed powers of $h_0$ enter $C^n$. The dyadic sum converges, so define
\[
 \Sigma_n(\varphi)=\sum_{j\ge0}\sum_zT(\chi_{j,z}D_j\varphi).
                                                                    \tag{42}
\]
Absolute convergence proves the asserted bound and continuity. On a compact set away from all diagonals only finitely many layers and boxes contribute, so their partition gives $T$. This proves tensor agreement. \(\square\)

## Lemma 10 (constrained density, uniqueness and RP)

Source: [growth-qf3.md](growth-qf3.md), §5; [cluster-check.md](../gates/cluster-check.md), Part B, retaining the compact-RP input. SA QF20–QF22. The final lattice-to-limit paragraph spells out the compact-RP bridge using LG1 and Lemma 6; it is the moving-test argument checked in [bridge-check.md](../gates/bridge-check.md), §2.

Finite sums of compact smooth separated tensors are dense in $\mathcal S_{\ne,n}$. Strictly positive-time ones are dense in $\mathcal S_{\ne,+,n}$. Consequently (42) is unique, and compact RP passes to the extended finite sequences.

*Proof.* Let $Q_R(x)=\prod_i\chi^+(x_i/R)$, $R\ge1$. For fixed $n,q$ and integer $A>0$, Leibniz and additional Schwartz decay give
\[
 p_q((1-Q_R)\varphi)\le C_{n,q,A}R^{-A}p_{q+A}(\varphi).         \tag{43}
\]
Every nonzero term has a slot outside the radius-$R$ plateau; cutoff derivatives cost $R^{-1}$. For the diagonal cutoff, a contributing term has some pair within $2h$ in sup norm. Taylor to that diagonal, with $q_{\rm add}$ extra derivatives, and (32) give
\[
 p_q((1-P_h)\varphi)\le C_{n,q,q_{\rm add}}h^{q_{\rm add}-q}
                                  p_{q+q_{\rm add}}(\varphi).  \tag{44}
\]
Choose $q_{\rm add}>q$. First apply (43), then (44) to the compact cutoff. This approximates $\varphi$ by smooth compact tests away from every diagonal. Cover each support by finitely many product boxes. The Fourier partial sums of Lemma 8 converge with every derivative and keep one compact support. They are finite sums of separated tensors. Choosing the cutoffs and partial sums successively for the first $1,2,\ldots$ seminorms gives one Schwartz-convergent sequence.

For positive time also use
\[
 B_h(x)=\prod_i s(x_{i,4}/h-1).                                 \tag{45}
\]
It is zero when a time is at most $h$ and one when all times are at least $2h$. Wherever $(1-P_hB_h)\varphi$ or a derivative can contribute, either a pair is close or some positive time is at most $2h$; at nonpositive time all jets already vanish. Taylor to the corresponding diagonal or zero-time plane proves (44) with $P_hB_h$. Thus $Q_RP_hB_h\varphi$ gives compact approximants away from the forbidden set. Choose their Fourier boxes with expanded closures strictly above zero. Their tensor factors retain strictly positive-time supports.

Uniqueness follows because two continuous extensions agreeing on separated tensors agree on this dense subspace. There is no extra growth loss at the time boundary: in (35) replace $P_h$ by $P_hB_h$. Each fine layer has all pair distances and times at least $h_j$, and one of them at most $4h_j$. There are still at most $Cn^2$ cutoff factors. Taylor moves at most four coordinates to the nearest forbidden set. Thus (37)–(41) apply with the same orders. Uniqueness identifies that construction with the restriction of $\Sigma_n$.

If $F$ is positive-time diagonal-flat, $\theta\bar F$ is negative-time diagonal-flat. The tensor $\theta\bar F\otimes G$ is flat on each cross diagonal: at a positive common time the negative factor vanishes, at a negative common time the positive factor vanishes, and at zero all boundary jets vanish. Internal diagonals are flat by hypothesis. Also
\[
 p_q(F\otimes G)\le p_q(F)p_q(G),                               \tag{46}
\]
since $1+|x|^2+|y|^2\le(1+|x|^2)(1+|y|^2)$. Approximate each component of a finite positive-time sequence by the tensors just constructed. Equations (11) and (46) make its finitely many quadratic terms converge. Compact RP therefore passes to their nonnegative limit.

For a limit (7), compact RP itself follows from LG1. Choose a lattice coordinate mirror at distance at most $a^{(j)}$ from time zero. All plaquettes used by a fixed finite compact positive-time sequence lie on its positive side for large $j$. The lattice quadratic form of the centered observables is nonnegative. Centering transforms covariantly because $\nu_j$ has the same reflection invariance. The reflected continuum tests differ from the tests reflected in that lattice plane by a translation of size at most $2a^{(j)}$. Their $C^1$ differences tend to zero. For the finite collection of tuples, enlarge support containers slightly so that one positive separation remains. Telescoping a product one slot at a time and applying (10) on those containers bounds the change by a fixed constant times the sum of the $C^1$ differences. Hence the reflected lattice evaluations tend to (9), which is nonnegative. This proves compact RP without constructing the sequence (7). \(\square\)

## Definitions supplied in this part

The definitions needed to make the checked notes into one statement are all explicit above:

1. The plaquette normalization, barycentres, microscopic and intermediate scales, supplied first-passage datum, Wilson DLR state class, admissible test geometry, sharp norm, two-state centered field and local-log cumulant.
2. The full D1 source ball and raw bounds, point terms, normally convergent domain sums, actual cube/tree indexing, dependence regions, rooted entropy gap and compatible cofinal tori; the source radius is distinguished from IN1's exponent.
3. The cell algebra, conjugated reflection copies, chessboard functional, common cell normalizers, active-subset product polydiscs and normalizer-centered variables.
4. The separated limit and its admissible multilinearity, degree-zero normalization, pair diagonals, diagonal-flat Schwartz space and seminorms, positive-time flat subspace, separated tensors, reflection action and finite-sequence RP form.
5. The flat exponential and step, partition and expanded cutoffs, local Fourier coefficients and scaled derivative seminorm, dyadic pair layers and product grid, extension sum, and the infinity and time-boundary cutoffs.

The auxiliary choices do not add physical hypotheses. The actual D1 estimates, LG1, and the existence of any limit used remain distinguished from those definitions.

## Source concordance

The [SA index README](sa-index/README.md), relevant and neighbouring rows in chunks 03, 04, 22 and 23, and [obligations.md](sa-index/obligations.md) were used before reading the source excerpts. The following ranges were checked against the pinned raw files; they are provenance, not imported conclusions:

| Text and checked lines | Content used and standing in that text |
|---|---|
| [YM4 outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), 4086–4194, 4541–4599 | D1 is an obligation; D2, D4, G4 and H1 point to conditional deductions. The rooted geometry, nonnegative bump, separation exponent $5n$ and diagonal-flat restriction agree with this part. |
| YM4, 2834–2942, 23621–23883 | Finite link-reflection input, chessboard argument, arbitrary-state domination, precise ST5–ST6 hypothesis and common cell normalizers. Conditional transfer proved in detail. |
| YM4, 23884–24335 | ST10–ST15 and GS1–GS13. State comparison and factorial bounds proved under full D1 and lattice symmetries. Lemma 6 uses the stronger graded cumulant bound for G4, so the separate weaker ST10–ST13 estimate is not repeated. |
| YM4, 24917–25391 | QF1–QF22: the detailed conditional Fourier/dyadic extension, density, time boundary and realized-component scope. This is the four-dimensional argument rebuilt in the checked note. |
| YM4, 24651–24717 | CC8–CC10: moving tests and rounded mirrors. Lemma 10 spells out the compact-RP passage for an already supplied sequence. |
| [Complete account II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex), 60348–60430, 60692–60749, 61205–61240, 62030–62090, 62293–62330, 63964–64050, 64570–64630 | The skeleton's broad Chapter 6 reference was checked at its definitions and relevant statement/proof excerpts. It concerns the finite-torus per-ball construction and uses a cited Balaban tree sum. No unverified proof or stronger all-state conclusion is imported from those excerpts; Lemmas 2–6 give the required hand proofs. |
| [YM3 I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), 74807–74900, 74941–75168 | IV-25-55, IV-26-17, IV-26-24 and IV-26-37 give the three-dimensional comparison cited by the checked note. Their $4n+1$ Fourier order and slot weight $(1+\lvert x\rvert^2)^{-2}$ are not imported into four dimensions. Lemmas 8–9 retain the checked replacements. |

The two requested initial raw files were fetched once to /tmp/sa_ym4.tex and /tmp/sa_ca_I.tex. The two additional files used above were fetched once to /tmp/sa_ca_II.tex and /tmp/sa_ym3_I.tex. No whole raw manuscript was read. SR1 uses no CA-I or CA-III result; no claim about the indexed CA-I items 4.12–4.19 is made. No computation supplies a proof step.

## Result

This part proves the conditional implication **full rooted UV1 + LG1 ⇒ SA-D4, G4 and D2**, with
$B(R)=C_B(R+1)^4$, $k=\lceil p\rceil+5$, and separation loss $\max(1,d^{-5n})$.
For every existing separated limit, it proves **H1**, constrained tensor density and RP transfer, with
$k_{\rm E}=20$, $\kappa_{\rm E}=k+32$, and degree-zero normalization one.

The scientific imports are precisely the full D1 consumer hypothesis of UV1 and the stated LG1 reflection/symmetry properties. IN1 supplies the order of the upstream constants and the meaning of a supplied datum, not a proved existence claim here. Clause H1 requires a limit (7); RP transfer requires compact RP, which Lemma 10 derives from LG1 for such a limit. Component bounds require realization by those all-state limits. UV1 remains **Outstanding**. Existence of the cutoff/limit sequence belongs upstream and to CL1; component realization belongs to PH1.

Corrections and consolidations made in distillation:

- Retained the gate's everywhere-nonnegative bump, both-state centering hypothesis, S1g dependence, and S1d link-plane input. S1e is derived, not separately assumed.
- Replaced the skeleton's compressed logarithm wording by the checked raw source upper bound and unsourced floor. Kept locality, representation independence, normal convergence, the doubled mirror-source radius, all scales and the full rooted entropy gap explicit.
- Preserved IN1's order and Amendment 1; distinguished its threshold exponent from the source radius. The cell exponent $p$ precedes $k$ and every test order.
- Made the existing-limit and compact-RP conditions explicit, and wrote the lattice-to-limit RP passage. Restricted component uniformity to realized component limits and uniqueness to the diagonal-flat domain.
- Kept the checked four-dimensional Fourier order, integrable slot weight, explicit inner/expanded/periodic box sizes, active-subset polydiscs, coarse-cutoff case and factorial accounting. Used the moment bound directly for growth and the graded cumulant bound for G4, removing duplicate weaker estimates.
- Removed the old C1/OH1 pointer as a purported first open obstruction. The gate already identifies that pointer as stale; this part leaves actual UV1 open without assigning a new upstream priority.

No unresolved internal proof step was found under these hypotheses. There is no assertion of contact terms, an extension to unrestricted Schwartz tests across diagonals, or Yang–Mills existence. This distilled part is **not yet refereed as a whole part**. The earlier checks apply to the named notes, not automatically to this assembly; no scientific or audit status is granted.
