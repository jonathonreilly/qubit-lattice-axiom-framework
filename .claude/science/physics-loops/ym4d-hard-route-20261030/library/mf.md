# M-freeness of the random-walk constants

Provenance: Codex, 2026-11-05, checkout `c04b80758f0ed2cac26749baca173a0dd8a50c4a`. Research text, not an audit; grants no status. New work is not yet checked by another model. No computer-assisted proof steps.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`. Tadeusz Balaban for the random-walk construction used there. CA-I/II/III and SA below refer to the pinned raw TeX line numbers.

## 1. Exact target and source map

The target is CA-I 2239–2251, `2.4:prop-m-freeness`, repeated at CA-II 59574–59586. Its local data are those at the decomposition of the density, on the one cell family. Its quantifier includes every \(M\) above its floors. It asserts

\[
 |G_W(x,y)|\le B_W e^{-\delta_W|x-y|},
\]

and the exponential bound for the companion random-walk kernel at rate \(\mu_0\). All three constants must be the Stage-5 global constants. An unspecified positive rate chosen after \(M\) does not suffice.

**Their standing.** CA-II 59588 says the proof is incomplete. Lines 59594–59605 give the global bounds and the local \((B_W,\delta_W)\) bound. Lines 59607–59609 leave precisely the companion bound at local data open. This note accepts the already supplied first bound as a port. It neither reproves nor audits the operator theorem.

**What “companion” identifies.** The proposition gives this kernel no symbol or formula. The explicit nearby use of \(\mu_0\) is the conditioned covariance and its root: CA-II 8521–8539 and Lemma `5.2:lem-covariance-root`, 10104–10186. The root lemma covers \(\sigma=1\) only. Its last paragraph expressly sends the decoupled family back to the assigned random-walk expansion. Thus a proof for an arbitrary inverse root is insufficient. Below, “assigned family” always means the book's family at that density decomposition, with its original terms and reading sets. It does not mean a newly chosen decomposition with the same sum.

**Every labelled occurrence read.** The two proposition labels occur at CA-I 1203, 1514, 1528, 1533, 1546, 2067, 2239, 2342, 2408; CA-II 10493, 59568, 59574, 59590; CA-III 110855–110856, 111071, 111410. Their containing passages have these roles:

| Passage | Use |
|---|---|
| CA-I 1201–1204 | Consistency of the main theorem's choices. |
| CA-I 1500–1551, 2058–2084 | Kernel constants precede widths, then \(r',\ell\), then \(M\). |
| CA-I 2257–2269 | Explains why \(M\)-dependent decay could make the three floors unusable. |
| CA-I 2325–2345, 2403–2409 | Hypothesis (A2) of `2.4:prop-order-consistent`; this is its sole application in that proof. |
| CA-II 10489–10506 | Complex and non-true pairs use kernel bounds; true-pair positivity is not substituted there. |
| CA-II 59540–59618 | Old terms beside a new region and the repeated proposition with its marked gap. |
| CA-III 110846–110860, 111066–111079 | Assembly depends on the constant-order implication. These summaries call M-freeness an implication; they do not fill the marked step. |
| CA-III 111410–111412 | The open-statement list retains the incomplete standing. |

The three relevant Stage-6 floors are

\[
 \mu_0M\ge2\kappa_1,\qquad \delta_WM\ge2\kappa_1,\qquad
 \delta_WM/4\ge32\kappa_1+2\log(LM)+C(d,L).                 \tag{1}
\]

The order is \(L\), \(\kappa\), \(\kappa_1\), \(M_1\) and its stated companions, kernel constants, \(\Theta_1,\varpi_T\), \(r',\ell\), \(M\), radii, then coupling ceilings. See CA-I 1468–1580 and 2058–2073. Choosing a smaller rate after any width or \(M\) has read it is not an exact proof of the proposition.

## 2. Comparison with the frozen texts

The comparison was made before the new attacks. None of these four texts proves the proposition as stated.

| Clause of the target | `hm.md`, Lemma 1 and Theorem 5 | `pw.md` | `hma.md` | `in1.md` |
|---|---|---|---|---|
| Conditional fluctuation operator of this account | Precision is PR-lay (7), with explicit R/W/AV imports; physical identification retains G-ID. | Operators are the specified \(H,H_1,\mathfrak G\), not the conditional covariance root. | Precision (3) uses the relative Y gauge form. | Lemma 1 starts from an abstract accretive matrix. |
| Only local data on the account's one cell family | Lemma 1 constructs terms on \(\mathcal R_{\rm loc}\); Theorem 5 uses \(\mathcal W(Y)\), including Rep and local gaps. The account's class has not been identified with these classes. | Uses admitted regular pairs and its fixed cut-downs; the Result retains P82 and admission hypotheses. | Theorem 2 covers R4 by adopting assignment D4. It retains whole-domain admission and formation matching. | Lemma 2 begins with a global matrix; its heredity paragraph explains why path tags do not remove exterior dependence. |
| The assigned companion expansion | Theorem 5 defines grouped polynomial-resolvent labels, then integrates them. It is a particular root family. Equality of its complete sum with a root does not identify local subseries. | Section 8 insists on its own full-hull composition; independently tagged factors differ. | D4 explicitly adopts the hm grouping with Y coefficients. Theorem 2 is conditional on that adoption. | The path-tagged root is a different construction. |
| Same Stage-5 rate \(\mu_0\) | Rates are \(\mu_W,\theta\), chosen from its own R/W constants. No equality or lower bound relative to CA's \(\mu_0\) is proved. | Rate \(\tau\) and \(C_{\rm PW}\) precede \(\kappa\), uniformly in larger \(M_1\); no identification with CA's \(\mu_0\). | Rate is \(d=\theta/4\), with the same identification issue. | Lemma 1 proves a rate from its input gap and weighted norm. It does not supply those inputs for the assigned local family. |
| Account's order and all larger \(M\) | Constants precede \(\kappa,\bar\kappa,M\) in IN1's order. This is an early-constant version, not the CA identification. | Same distinction; \(M\)-independence itself is explicit. | Early constants, followed by stated \(M\) floors and radius ceilings. | Its constant table is conditional on all imported packages and differs from CA's table. |

Sources read: hm §§1–4 and Result; pw §§1, 7–9 and Result; hma §§1–2 and Result; in1 constant table, Lemmas 1–2 and their scope paragraph. Hma's gauge change cannot silently be imposed on the account's stored family. These are useful versions, not counterexamples to CA.

## 3. What the account already supplies

The indexed outline passages are SA 10111–10139, 10307–10352 and 14101–14169. They describe regular pairs, walk families and the local inverse-root method. In particular, the separately decoupled root is not the inverse root of the decoupled precision.

The complete account supplies more. `4.4:lem-cell-resolvent` (CA-I 6219–6309), its local proof (6827–6957), and `4.4:lem-cell-coercivity` (6646–6809) construct local terms on \(\mathbf P_{\rho,W'}\). The form hypothesis (5517–5561) includes datum-independent, absolute walk majorants on each full footprint. The local proof bounds families before summation; it does not require a global extension of the whole datum. Corollary `4.4:cor-covariance-local-pieces` (12428–12481) identifies cube pieces for that construction.

These results are ported inputs, with their printed hypotheses. They are not unconditional statements about every later density decomposition. In particular, cell coercivity uses the base setting \(\mathcal S_0\) with trivial traces (CA-I 6681–6687). The general free-current theorem has another limitation: its local-ball clause fixes a **global** real background \(U\in\mathcal U_{\mathbb R}\) (46111–46121; proof at 46800–46950). Arbitrary integration-bond subsets in that theorem do not remove this hypothesis.

There is also a rate issue even on the first construction. Its printed rate is

\[
 \theta=\tfrac14\min\{\gamma_*/(4e\mathsf B(r'+2\rho_w)),\,
                          \delta_{\mathsf A}/2\}.              \tag{2}
\]

See CA-I 6097–6113. This is independent of \(M\), but reads \(r'\). The table fixes \(\mu_0\) before \(r'\). The next section removes this particular loss for the **same cell-resolvent construction**, without claiming the missing family identification.

## 4. A rate fixed before the near–far cutoff

**Lemma 1 (earlier rate for the CA cell family).** Retain the actual form
walks, cells, matrices, word order and footprints of
`4.4:lem-cell-resolvent`. Assume its local hypotheses, in particular the
datum-independent majorants in (W′) and the conclusion of
`4.4:lem-cell-coercivity` on every readable cell. Abbreviate
\(\delta=\delta_{\mathsf A}\), \(\gamma=\gamma_*\), and put

\[
 \nu=\min\left\{\frac\delta2,\frac{e\gamma\delta}{16\mathsf B}\right\},
 \qquad \lambda=\frac\nu4,\qquad a=\frac\gamma2,
 \qquad
 S_\nu=d(1+4/\nu)^d.                                   \tag{3}
\]

The bond-lattice estimate used in CA-I 6112 gives
\(\sup_b\sum_{b'}e^{-\nu|b-b'|/2}\le S_\nu\), uniformly in the
torus; in particular \(S_\nu\ge1\). Choose the same auxiliary parameters
under their printed floors and, if necessary, the additional floors

\[
 8S_\nu\mathsf B e^{-\delta r'/2}\le\gamma,
 \qquad \ell\ge2(r'+2\rho_w)+4,
 \qquad \frac{2\mathsf B S_\nu}{\gamma}e^{-\nu\ell/8}\le\frac12 .       \tag{4}
\]

These are successive lower bounds on \(r'\) and \(\ell\), not conditions on
\(M\); retain \(M\ge48\ell\) and the other printed floors. Then the **same
labelled families** satisfy

\[
 \left|\!\left|\!\left|\mathsf R^{Y,W'}(x)\right|\!\right|\!\right|_\lambda
       \le\frac{4S_\nu}{x+a},\qquad
 \left|\!\left|\!\left|\mathsf M^{Y,W'}\right|\!\right|\!\right|_\lambda
       \le\frac{4S_\nu}{\sqrt a},\qquad x\ge0.                 \tag{5}
\]

The constants in (3) and (5) read only the form constants and the gap, before
\(r',\ell,M\). The assertions are uniform over local data in the stated
class, arbitrary permitted \(Y,W'\), and all larger \(M\). They also hold
after deleting any set of complete word labels. No assertion that a deleted
sum is an inverse is needed.

**Proof.** This changes the estimate in the third step of the CA proof;
it does not construct another expansion. The remaining steps are ported
with the new estimate. Details of their inequalities are included to track
the order and absolute majorants.

Write \(a_\omega(b,b')\) for the datum-independent entry majorants of (W′).
The endpoint-weighted row and column sums of their sum are at most
\(\mathsf B\) at rate \(\delta\), since
\(d(\omega;b,b')\ge |b-b'|\). Taking a subfamily or a bond compression
decreases these nonnegative sums. In particular every readable near-cell
matrix \(T_X\), with \(X\subset q^*\), has that same Schur majorant and
\(\operatorname{Re}T_X\ge7\gamma/8\).

Fix a bond \(b_0\). On this finite cell let \(D\) be multiplication by
\(e^{\nu f(b)}\), where \(f(b)=|b-b_0|\). The distance is the same unit-lattice
distance as in the CA cell proof; it is 1-Lipschitz. With
\(F=DT_XD^{-1}-T_X\),

\[
 |F(b,b')|
 \le \nu |b-b'|e^{\nu|b-b'|}|T_X(b,b')|.
\]

For \(t\ge0\), \(t e^{-(\delta-\nu)t}\le [e(\delta-\nu)]^{-1}\).
Apply this to each row and each column, before Schur's test. It gives

\[
 \|F\|\le\frac{\nu\mathsf B}{e(\delta-\nu)}
       \le\frac{2\nu\mathsf B}{e\delta}\le\frac\gamma8.       \tag{6}
\]

Consequently
\(\operatorname{Re}(x+T_X+F)\ge x+3\gamma/4\).
Cauchy–Schwarz implies invertibility on the finite cell and inverse norm
at most \((x+3\gamma/4)^{-1}\le(x+a)^{-1}\). Conjugate back, taking
\(b_0=b'\) for the entry \((b,b')\), to obtain

\[
 |(x+T_X)^{-1}(b,b')|
       \le(x+a)^{-1}e^{-\nu|b-b'|}.                       \tag{7}
\]

This is the exponential-moment argument of `in1.md`, Lemma 1, applied to
the book's matrices. It uses neither finite range \(r\) in (6) nor the
norm of a globally extended datum. The finite range is still used for
locality and for the next boundary-distance estimate.

Keep the book's

\[
 P_q=\chi_{c_q^*}(x+T_q)^{-1}\kappa_q,\qquad
 B_q=\chi_{Y\setminus c_q^*}\mathsf A_{\rm loc}
                  \chi_{c_q^*}(x+T_q)^{-1}\kappa_q.       \tag{8}
\]

For local data only cells with \(q^\sharp\subset W'\) are used. Hence
\(\sum_q\kappa_q(b')\le1\). Summing (7) against these weights, first by
rows and then by columns, gives

\[
 |||P|||_\lambda\le S_\nu/(x+a).                        \tag{9}
\]

In an entry of \(B_q\), write \(b''\in c_q^*\) for the intermediate
bond. The geometry in CA-I 6487–6499 gives
\(|b''-b'|\ge\ell/2\). The triangle inequality and \(\lambda=\nu/4\)
therefore give

\[
 e^{\lambda|b-b'|}e^{-\nu|b''-b'|}
 \le e^{\lambda|b-b''|}e^{-\nu|b''-b'|/2}e^{-\nu\ell/8}.    \tag{10}
\]

The row sum of \(\mathsf A_{\rm loc}\), weighted at \(\lambda\), is at
most \(\mathsf B\); the remaining sum over \(b'\) is at most \(S_\nu\).
For the column estimate sum first over \(b\), then \(b''\), and finally
over \(q\) with weight \(\kappa_q(b')\). Both estimates give

\[
 |||B|||_\lambda\le
       \frac{\mathsf B S_\nu}{x+a}e^{-\nu\ell/8}
       \le\frac12.                                      \tag{11}
\]

The single-cell walk weight is bounded by the endpoint weight in (9)–(11),
exactly as in CA-I 6466–6470. Where the near matrix in (8) is evaluated on
different local cells, use \(\sum_\omega a_\omega(b,b'')\), not the value
of a putative common global matrix. This is why the datum-independent
clause of (W′) matters.

The walk-family product inequality of CA-I 4906–4949 now gives, for the
**family of words**, not an asserted local inverse,

\[
 |||\mathsf N|||_\lambda
 :=\left|\!\left|\!\left|
   \big(P_{q_0}(-B_{q_1})\cdots(-B_{q_n})\big)_{n,q_0,\ldots,q_n}
   \right|\!\right|\!\right|_\lambda
 \le\frac{2S_\nu}{x+a}.                                  \tag{12}
\]

The far-walk family \(E\) has norm at most
\(\varepsilon=\mathsf B e^{-\delta r'/2}\) at any rate at most
\(\delta/2\). Indeed \(d(\omega)>r'\) removes the factor
\(e^{\delta r'/2}\) from its (W′) majorant. Expand precisely the words
\(\mathsf N(-E\mathsf N)^m\) prescribed in CA-I 6257–6263. By (4),

\[
 |||E\mathsf N|||_\lambda
       \le\varepsilon\frac{4S_\nu}{\gamma}\le\frac12,
 \qquad
 |||\mathsf R^{Y,W'}(x)|||_\lambda
       \le\frac{2S_\nu}{x+a}\sum_{m\ge0}2^{-m}
       =\frac{4S_\nu}{x+a}.                               \tag{13}
\]

All quantities summed here are nonnegative majorants. No factor counting
the number of cells, no volume factor, and no inverse identity for a local
subseries enters.

Finally integrate each already assigned word, as in the book:

\[
 \mathsf M_\varpi=\pi^{-1}\int_0^\infty
              x^{-1/2}\mathsf R_\varpi(x)\,dx.
\]

Tonelli applied to the majorants and the elementary substitution
\(x=at^2\) give

\[
 \pi^{-1}\int_0^\infty\frac{x^{-1/2}}{x+a}\,dx=a^{-1/2}.
\]

This proves (5). Holomorphy follows from the cell inverse and normal
convergence, uniformly on compact subsets, with the same integrable
majorant. Restricting whole word labels decreases the bounds. This proves
the lemma. \(\square\)

**What this fixes in the order.** With the form inputs supplied at Stage 5,
one may fix \(\lambda,S_\nu,4S_\nu/\sqrt a\) there, then choose \(r'\),
then \(\ell\), then \(M\). The exponential in \(r'\) beats the polynomial
growth of the book's original \(S\), so its printed (k1) and (4) can both
be met; the remaining conditions on \(\ell\) are lower bounds. Thus no
later quantity is fed back into a rate. If one is still making the common
global/local choice, the smaller of a valid global rate and \(\lambda\)
can be chosen **at Stage 5**, with all subsequent widths and floors then
read at that choice. This observation does not establish the proposition
at an already selected \(\mu_0\). For that reading one must prove the
local estimate at that very rate; \(\lambda>0\) alone is insufficient.

The proof also does not identify \(\mathsf M^{Y,W'}\) with the Chapter-5
companion on its entire local-data class. That is a separate question
about the existing construction, addressed by the attacks below.

## 5. Three attacks on the remaining passage

These are attacks on the local passage, not attempts to reconstruct
Balaban's global random-walk theorem. The global theorem is an input, as
in CA-II 59594–59601. The following arguments explain exactly what can
and cannot be transported from it.

### Attack 1: complete primitive patches independently

A simultaneous global extension of a datum on a large, possibly
multiply connected union would be more than a random-walk estimate needs.
One can try to complete only the data read by each primitive factor.
Here is the precise conditional transport argument.

Suppose an assigned word is
\(F_{\alpha_1}(u)\cdots F_{\alpha_n}(u)\). Suppose each primitive
\(F_\alpha(u)\) has a completion \(\widehat u_\alpha\) into the global
class, agreeing on its **whole** reading set, including the current and
the geometric data. Suppose also that the global proof supplies
datum-independent entry envelopes \(f_\alpha\) for these primitives.
Locality gives
\(F_\alpha(u)=F_\alpha(\widehat u_\alpha)\), up to its prescribed unitary
gauge transports. Its entries are consequently bounded by
\(f_\alpha\). Entrywise matrix multiplication gives

\[
 |(F_{\alpha_1}\cdots F_{\alpha_n})(b,b')|
 \le\sum_{b_1,\ldots,b_{n-1}}
    \prod_{j=1}^n f_{\alpha_j}(b_{j-1},b_j),
 \quad b_0=b,\ b_n=b'.                                  \tag{14}
\]

The same global numerical summation of words then applies, without one
common completion. Gauge covariance is used to return each matrix to the
original frame before multiplication; it is not a license to multiply
matrices in unrelated gauges. For endpoint entry norms these transports
are isometries. Thus this route would preserve the original constants
and the assigned labels, not merely give some new positive rate.

I tried the actual cutoffs in the two available CA local constructions.
In the base cell of §4.4 the gauge and cutoff construction is already
proved: one real gauge on \(q^\sharp\), cutoff of the real potential and
the independent complex/current data, then extension by zero. Port
CA-I 6686–6809. It gives the inputs of Lemma 1 on that class. Extending
the whole union is unnecessary.

For the general free-current theorem, however, its local-ball proof uses

\[
 (e^{i\eta\chi A'}U,\chi J),\qquad
 \chi=\max\{0,1-(2L/M)\tau(\{\cdot\},[\nu])\}.
\]

The cutoff is applied to the perturbation and current while retaining a
**global** \(U\). The product rule bounds the perturbation norm by
\((1+2L/M)r/2<r\) when \(M>2L\). This estimate, including its seam collar,
is in CA-I 46800–46885 and 46887–46919. It does not define \(U\) where a real local
datum is absent. Cutting off the real potential as well would require a
single admissible real gauge on the primitive's complete reading hull,
and would have to preserve (u1), (reg), and (reg)\(^{\sharp}\) on the
resulting layered background. The gauges asserted separately on the
sets in CA-I 45439–45481 do not, by themselves, supply that extension.
In particular the proof for trivial traces in §4.4 cannot be applied to
every traced primitive merely by renaming its hull.

The seam lemma does not supply this missing construction. It asserts
weights for its own operator list and its reread data class, and keeps
the application-domain inclusion as a separate input: CA-I
53550–53631. No use is made here of its promised proof or of a wider
domain than it states.

**Outcome of attack 1.** Formula (14) proves that independent primitive
completions would suffice whenever the global argument has the requisite
absolute envelopes. The actual general-density real completions, with
unchanged primitive matrices and constants, have not been constructed.
The failure is at the real-background admission on a full reading hull,
not at the summation over walks or at the topology of the entire union.
Nor may a bound on the already summed global kernel be substituted for
the primitive envelopes in (14).

### Attack 2: infer the companion directly from the local operator

The first try was to use the already ported local kernel bound for
\(G_W\), take an intrinsic local matrix, and apply the spectral integral
or the accretive-matrix estimate of `in1.md`, Lemma 1. Two distinct
obstructions can be checked by hand.

First, localization and functional calculus do not commute. For

\[
 A=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
 P=(1\ \ 0),
\]

one has

\[
 PA^{-1}P^*=\frac23\ne\frac12=(PAP^*)^{-1},\qquad
 PA^{-1/2}P^*=\frac{1+1/\sqrt3}{2}
       \ne\frac1{\sqrt2}=(PAP^*)^{-1/2}.                 \tag{15}
\]

The inverse follows by multiplying the two-by-two matrices; the root
follows from the eigenvectors \((1,1)\) and \((1,-1)\), of eigenvalues
1 and 3. This is not an example of the account's walk localization. It
shows why an identity between that localization and an intrinsic
compressed inverse root must be proved, rather than inferred from
agreement of complete operators. CA-I 6937–6957 expressly distinguishes
the summable local family from a local inverse; the latter requires the
separate collar/coercivity result.

Second, even exponential decay and positivity of a covariance do not
alone give a fixed exponential rate for its square root. On
\(\ell^2(\mathbb Z)\) consider

\[
 C_\epsilon=\epsilon^2 I+2I-S-S^*,\qquad 0<\epsilon\le1,
\]

where \(S\) is the unit shift. This is positive, and its entries are
bounded at any fixed exponential rate with a constant independent of
\(\epsilon\): only distances zero and one occur. Its positive root
has Fourier symbol

\[
 f_\epsilon(t)=\sqrt{\epsilon^2+2-2\cos t}.
\]

Suppose its convolution coefficients obeyed
\(|\widehat f_\epsilon(n)|\le C e^{-\mu|n|}\) for fixed \(C,\mu>0\)
uniformly in \(\epsilon\). Since
\(0\le f_\epsilon(t)\le\sqrt5\), dominated convergence in the Fourier
coefficient integral gives the same estimate for the coefficients of
\(f_0(t)=2|\sin(t/2)|\). But
\(\sum_n |n|C e^{-\mu|n|}<\infty\). Its Fourier series would therefore
be continuously differentiable, and equal \(f_0\); the latter has unequal
one-sided derivatives at zero. This contradiction proves the assertion.
Equivalently one may first take periodic cycles and pass to their
Riemann-sum Fourier coefficients; uniform volume bounds would imply
the same contradiction.

This example does **not** satisfy all of the account's fluctuation-form
hypotheses: \(C_\epsilon^{-1}\) has no uniform upper bound as
\(\epsilon\downarrow0\). It refutes only the attempted inference from
the known covariance-kernel bound. It is not a counterexample to
Proposition 2.4.

**Outcome of attack 2.** A genuine local form with a sector gap and a
weighted norm would give its own inverse root by hand. The first
ported kernel bound supplies neither the missing identification (15)
nor all of those form hypotheses for the assigned local companion.
CA-II 10104–10186 establishes the spectral argument only at the
specified true global pair and \(\sigma=\mathbb1\); its final paragraph
does not extend that argument to the independently assigned family.

### Attack 3: keep the words and improve their majorants

This is Lemma 1. It succeeds beyond a direct reuse of the frozen texts:
it re-estimates the **book's** cell words, bounds an arbitrary readable
subfamily using datum-independent sums, and fixes a rate before \(r'\).
The critical estimate is (6), which replaces the finite-range loss
\(e\theta_0 r\mathsf B\) by
\(\nu\mathsf B/[e(\delta-\nu)]\). Thus the near–far split is no longer a
source of backward rate dependence.

The remaining application cannot be supplied by equality of untagged
global kernels. To see the exact algebraic issue, introduce a formal
variable \(z_\Delta\) for every density cell. Each assigned word carries
its actual cell monomial. Retention of words in a region is implemented
by setting the appropriate outside variables to zero. At the simplest
scalar level the families

\[
 1,\qquad (1+h)-h z_\Delta                            \tag{16}
\]

agree at \(z_\Delta=1\), for every \(h\), and disagree at
\(z_\Delta=0\). Hence untagged equality of two absolutely convergent
expansions is insufficient even when both sides are analytic and
volume-free. This example concerns an inference, not the book's actual
coefficients. The same issue is why `pw.md` insists on its full-hull
composition, and why adopting D4 in `hma.md` is a substantive assumption.

There is a partial assignment in the complete account: CA-I 8146–8163
explicitly uses the cell-resolvent families for its local-real-base
proposition. That is useful and is retained. But that proposition is
itself headed “Proof outstanding” (8110), and assumes its own local
coercivity and data-class hypotheses. It does not assert that every
local background of Chapter 5, including the old terms beside a new
region, has this realization with the fixed Stage-5 rate. The general
operator theorem's resolvent sheet at CA-I 46088–46095 and its
local-ball clause at 46111–46121 also do not make that assertion: the
latter retains the globally given real background.

**Outcome of attack 3.** The estimates (5) are proved for the local
cell family with its printed hypotheses. What remains is continuation
of the **assigned spectral-parameter family** to the actual density
data, at the same preassigned rate, with its labels retained. Replacing
it by the family of Lemma 1 without proving that continuation would
change the object. Lowering an already read \(\mu_0\) afterward would
change the constants. Neither is done here.

## Round 1 result (retained)

**Open lemma**

**Local resolvent lift of the assigned companion, at the fixed Stage-5
rate.** Fix an instance of the density decomposition in
`2.4:prop-m-freeness`, its existing family of cells and its existing
random-walk assignment. Let \(W\) be any union of those cells on which
that instance calls for local data, and let \(u\) be any datum admitted
there by that instance. Keep its nest, free bonds, currents, traces,
reading hulls, radius ceilings and \(M\) floors. In particular \(M\)
ranges over **all** values above those floors and \(\mu_0\) is the
already fixed Stage-5 rate. Any decoupling parameters occurring at that
instance retain their stated ranges; they are not silently set to one.

The companion in that instance is the local reading of the same
spectral-integral family as at its global regular backgrounds: there is
a locally normally convergent family
\(\bigl(R^{\rm CA}_\alpha(x;u)\bigr)_\alpha\), \(x\ge0\), obtained by
evaluating and retaining the **existing global resolvent words**, with
their original coefficients and full reading sets, such that

\[
 \begin{split}
 R_W^{\rm CA}(x;u)&=\sum_{\alpha\ {m retained\ in}\ W}
                         R^{\rm CA}_\alpha(x;u),\\
 K_{{\rm comp},W}(u)&=\frac1\pi\int_0^\infty
                         x^{-1/2}R_W^{\rm CA}(x;u)\,dx .       \tag{17}
 \end{split}
\]

Here the equality is an equality of the assigned families: attach one
formal variable to each density cell and keep each word's original
monomial, including any multiplicity prescribed by that assignment.
The equality must persist coefficientwise in those variables. In
particular, retaining a word is decided from its original full reading
set. Agreement only at all variables equal to one is not the assertion.
The label correspondence identifying the companion of Proposition 2.4
with (17) is part of this lemma; the proposition's unnamed companion
must not simply be replaced by an arbitrary square root.

There are \(a_*>0,C_*<\infty\), chosen at Stage 5 from the already fixed
global operator constants, such that this local reading is defined and
holomorphic on the whole stated local-data domain and obeys

\[
 \boxed{\displaystyle
  \bigl|R_W^{\rm CA}(x;u)(b,b')\bigr|
       \le\frac{C_*}{x+a_*}\,e^{-\mu_0\rho(b,b')}
       \quad (x\ge0).}                                    \tag{18}
\]

The same \(a_*,C_*\) work for global data, all admitted local data, all
retained regions, levels, nests, volumes and larger \(M\). They are
chosen before the widths and before \(r',\ell,M\). No new ceiling on
\(M\), no new background class, and no later reduction of \(\mu_0\) is
allowed. Only the existing geometric and radius hypotheses of the
density instance may be used.

This is one sufficient, stronger lemma, not a claim that (18) is
necessary for the desired companion bound. Its extra content is the
uniform spectral parameter and the continuation of the fixed labels.
It is more specific than asking for a decay estimate for some locally
constructed covariance. The global resolvent formula to be continued
is present in CA-I 4844–4873 and 6243–6282; the general free-current
resolvent sheet is CA-I 46088–46095. None of those passages is being
asserted here to have proved this continuation to the Chapter-5 local
data.

**Why this one lemma would finish the requested proposition.** By (18)
the integral in (17) is absolutely convergent entrywise, and the
elementary integral already evaluated in Lemma 1 gives

\[
 |K_{{\rm comp},W}(u)(b,b')|
 \le\frac{C_*}{\sqrt{a_*}}e^{-\mu_0\rho(b,b')}.             \tag{19}
\]

Thus its decay rate is the same preselected \(\mu_0\); its amplitude
can be fixed at the same Stage 5 for global and local data. The
\((B_W,\delta_W)\) part is already the ported conclusion at
CA-II 59602–59605. Neither bound now reads \(M\), so all three floors
(1) have exactly the required direction. No inverse identity at a
non-true pair has been inserted. This is a hand proof of the implication
from the lemma to the proposition, not a proof of the lemma.

What is proved in this round is Lemma 1 for the book's local cell family,
the independent-completion implication (14), and the obstructions to
the two invalid shortcuts (15)–(16) and the covariance-only inference.
The three attacks fail, respectively, at admission of real primitive
patch completions, at the missing local functional-calculus identity
and form hypotheses, and at continuation of the original tagged family
at the fixed rate to the actual density data. No counterexample to
Proposition 2.4 has been obtained. The local resolvent lift (17)–(18)
remains open.

## 6. Second round: sources and the point of attack

Provenance: Codex, 2026-11-05, same pinned checkout. This round preserves
Sections 1–5 and their result. It starts from (17)–(18), not from a new
choice of Gaussian carriers. The new arguments below are not yet checked
by another model. They grant no status.

The target is the M-freeness row of `port-map.md`, Table 3 and plan 4.2.
A proof would remove its marked step from the constant-order argument.
Failure leaves that argument conditional. The account's operator theorem
and its proved lemmas are ported with their hypotheses, not re-derived.

I read `mf.md` whole, then rechecked the comparison against hm Lemma 1
and Theorem 5, pw Sections 1, 8–9 and Result, hma D4 and Theorem 2, and
in1's constant table and Lemmas 1–2. The five rows of Section 2 still
apply. In particular, hma D4 **adopts** its carrier assignment. It does
not identify the account's assignment. No frozen text already proves
the requested proposition.

The outline and CA-I were fetched once in this round from the requested
revision. The existing CA-II and CA-III files were reused. Before source
reads I used `sa-index/README.md`, `obligations.md`, chunks 10 and 12's
neighbouring walk and root rows, `ca-full/README.md` and its statement
rows, and the neighbouring rows in `ca-4.12-4.19` chunks 3–5 and 8. The
direct source checks include every
labelled use listed in Section 1, CA-II 8922–8999 and 10104–10186, and
the additional ranges below. The §4.14 index's initial “sketched” entries
refer forward to the proofs in its later chunks; they are not new gaps.

| Source | Input retained, and exact scope |
|---|---|
| CA-I 45312–45328, 45439–45490, 45750–45824 | The free-current constants, the three real gauge conditions, their ceilings and their order. |
| CA-I 46035–46129 | The free-current operator theorem. Clause (D) supplies shifted resolvent sheets. Clause (H) still requires a globally supplied real base. |
| CA-I 47435–47533 | The second-cover positivity comparison uses a cutoff perturbation of the flat base, on one box. |
| CA-I 47693–47892 | The unit-frame proof defines \(m_1=\gamma_0/4\), a rate \(\mu_1\), and \(\delta_0=\mu_1/4\); it compares each local partial form with the flat one, then inverts globally. |
| CA-I 48012–48052 | The \(n\)-step resolvent estimate carries \((1+2x/m_1)^{-(n+1)}\). Its labels and reading sets survive the spectral parameter. The local-ball argument retains its global real base. |
| CA-I 6139–6146, 6243–6264, 6827–6860, 6937–6957 | The actual endpoint weights, cell words and rule for retaining local words. Local sums are not asserted to be inverses. |
| CA-I 52620–52647 | The perturbation norm uses the covariant difference in the real base; real gauge transformations preserve this norm when they also transform that base. |
| CA-II 8521–8539, 10104–10186, 10424–10434, 10465–10474 | \(\mu_0\) is the Combes–Thomas rate read by the root and transfer estimates. It is not identified there with \(\delta_0\). |

The earlier literature record is `lit-balaban.md`, Section 3. The targeted
paper read was Balaban, *Propagators for lattice gauge theories in a
background field*, CMP **99** (1985), pp. 413 and 432: the walk factors
read enlarged local domains, and Theorem 3.15 gives the covariance's
M-independent global bound. The available text is
`~/ym4d-papers/cmp99b.txt`. I did not use its OCR formulas for arithmetic.
The account's statements of these inputs are the port used here.

All source constructions and their notation remain credited to Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors of their text,
and to Tadeusz Balaban. The three attacks below are new to this note.

## 7. Attack 4: integrate the original step factors exactly

The previous result asks for a uniform resolvent estimate. The global
proof contains more structure than a generic resolvent bound. Write

\[
 a=m_1/2,\qquad q(x)=\frac{a}{a+x},\qquad
 \widehat R_\nu(x;u)=q(x)^{-(n(\nu)+1)}R^{\rm CA}_\nu(x;u),
                                                               \tag{20}
\]

where \(n(\nu)\) is the step count before any regrouping. This definition
does not assert that \(\widehat R_\nu\) is independent of \(x\).
The factor in CA-I 48012–48017 is a factor in the word estimates.
Identifying the remaining matrix with its value at \(x=0\) would be an
extra, generally false assertion.

**Lemma 2 (integration keeps the assigned labels and rate).** Suppose the
*existing* locally evaluated words admit nonnegative bounds

\[
 \|\widehat R_\nu(x;u)(b,b')\|\le A_\nu(u;b,b')\quad(x\ge0),
                                                               \tag{21}
\]

where each \(A_\nu\) is independent of \(x\). Keep the prescribed tag
\(s_\nu\), including all its multiplicities. If

\[
 \sum_{\nu\text{ retained}} |s_\nu|\,c_{n(\nu)}A_\nu(u;b,b')
       \le H\,e^{-\mu_0\rho(b,b')},\qquad
 c_n=\frac{\binom{2n}{n}}{4^n},                              \tag{22}
\]

then the termwise spectral integral has bound

\[
 \left\|\sum_{\nu\text{ retained}}s_\nu\,
    \frac1\pi\int_0^\infty x^{-1/2}R^{\rm CA}_\nu(x;u)\,dx\right\|
       \le \sqrt a\,H\,e^{-\mu_0\rho(b,b')}.                \tag{23}
\]

Thus integration costs neither a smaller rate nor a later constant.
The assertion applies on each compact parameter set on which (21)–(22)
hold uniformly. With local normal convergence of those majorants, it
also preserves holomorphy. It does not establish (21) or (22).

**Proof.** Substitute \(x=at^2\), then \(t=\tan\theta\). This gives

\[
 \frac1\pi\int_0^\infty x^{-1/2}q(x)^{n+1}\,dx
 =\frac{2\sqrt a}{\pi}\int_0^{\pi/2}\cos^{2n}\theta\,d\theta
 =\sqrt a\,c_n.                                             \tag{24}
\]

For completeness, let \(J_n\) be the last integral without its prefactor.
Its initial value is \(J_0=\pi/2\). For \(n\ge1\), integration of the
derivative of \(\sin\theta\cos^{2n-1}\theta\) gives
\(J_n=(2n-1)(J_{n-1}-J_n)\). Both boundary terms vanish.
Therefore \(J_n/J_{n-1}=(2n-1)/(2n)\), which proves (24).
Take norms before integration and use (21). Tonelli for the nonnegative
majorants, followed by (22), gives (23). No regrouping of labels occurs.
Compact uniform domination and Morera's theorem give the holomorphic
version. \(\square\)

I tried to obtain (21)–(22) from the already ported local covariance
bound, namely the first half of Proposition 2.4. That attempt fails even
before any gauge issue. Bounds on the sum at \(x=0\) do not bound the
normalized words. The following two scalar words exhibit the failure:

\[
 R_1(x)=h(1+x)^{-1},\qquad R_2(x)=-h(1+x)^{-2}.             \tag{25}
\]

Their sum at zero is zero for every \(h>0\). Their spectral integrals
sum to \(h(1-c_1)=h/2\), by (24) with \(a=1\).
They can carry the same reading set, so separating regions does not
separate this cancellation. They are not asserted to be CA words.
They refute only the inference from the zero-parameter summed bound.

Nor does (24) fix a missing exponential margin. One has

\[
 \frac1{n+1}\le c_n\le1.                                  \tag{26}
\]

The upper bound follows from the recurrence. For the lower bound, start
with \(c_0=1\) and use
\((2n+1)/(2n+2)\ge(n+1)/(n+2)\). Thus the integration factor cannot
turn a critical geometric word sum into a convergent sum, or supply a
positive exponential rate that was absent from its majorant.

**Exact failure of attack 4.** The spectral integration and the original
tags are now accounted for. What is missing is the local bound on the
normalized original words. The available global sheet bound has rate
\(\delta_0\). The account's root estimate has rate \(\mu_0\).
Neither the local covariance bound nor (24) proves a comparison between
those rates. Choosing their minimum during the original Stage-5 choice
would be a possible common convention; it is not a proof at an already
read \(\mu_0\). This attack does not change that choice.

## 8. Attack 5: complete into the complex fibre at the flat base

Attack 1 sought a completion in the **real** regularity class. There is
another possibility. A small real potential can be treated as a complex
perturbation of the global flat base. The account itself uses this move
in its positivity proof. Its one-box application extends to the following
local data. This is a port of that comparison, with only the local-domain
passage supplied here.

**Lemma 3 (one real local partial form).** Fix the global geometric
record, floors and ceilings of `4.14:thm-operator-theorem`. Let
\(\mathsf b\) be one of its unit boxes, \(\ell=M/(12d)\), and put
\(S=\mathsf b^{+\ell}\). Let \(Q\subset\Omega_k\) be the containing
\(M\)-cube of CA-I 47745–47753, with
\(S^{+\ell}\subset Q\). Suppose a real configuration is given on
\(Q\), with a witnessing gauge

\[
 U^g=e^{i\eta A},\qquad |A|,|\nabla A|<a_Q,\qquad
 a_Q\le\frac{a_1^{\oplus}\gamma_0}{24\gamma_1}.             \tag{27}
\]

No real configuration outside \(Q\) is assumed. Set the independent
current to zero. Retain precisely the form words with field reading
sets \([\omega]\subset S\), and retain their original geometric
reading lists. Then the account's partial form

\[
 \mathsf Q^{\mathsf b}_{\rm loc}(U,0)
 =1''\sum_{[\omega]\subset S}\mathsf Q_\omega(U,0)1''       \tag{28}
\]

has a well-defined continuation from global data. It uses the original
words, not new labels. It is independent of the witnessing gauge and
cutoff used to define it. On the range of \(1''\) it is real symmetric,
and

\[
 \frac{3\gamma_0}{4}I\le\mathsf Q^{\mathsf b}_{\rm loc}(U,0),
 \qquad \|\mathsf Q^{\mathsf b}_{\rm loc}(U,0)\|\le\gamma_1. \tag{29}
\]

The constants are exactly those of that comparison. This statement is
restricted to data having the full containing cube \(Q\). It does not
assert that every Chapter-5 retained word has such a cube in its data.

**Proof of the local-domain passage.** Take the account's cutoff
\(\chi=1\) on \(S\), zero off \(S^{+\ell}\), with slope at most
\(1/\ell\). Extend \(\chi A\) by zero. The product-rule calculation
in CA-I 47789–47798 uses only (27) on \(Q\). Hence

\[
 u_z=(e^{iz\eta\chi A},0)\in\mathcal U(1),\qquad
 |z|<r_{\rm reg}:=\frac{a_1^{\oplus}}{2a_Q},               \tag{30}
\]

where the real base of this global complex fibre is \(\mathbf1\).
In particular \(u_1\) is admitted in \(\mathcal U(1)\), whether or
not its real configuration belongs to \(\mathcal U_{\mathbb R}\).
This distinction is the reason the construction works here.

Extend the site gauge \(g\) arbitrarily off \(Q\). Define each term in
(28) by evaluating its original global term at \(u_1\), then conjugating
back by this gauge. Such a global real gauge transformation takes the
flat-base fibre to a fibre about a global pure gauge. That base belongs
to \(\mathcal U_{\mathbb R}\), by its gauge invariance (CA-I
45523–45555). Admission in the complex fibre is preserved too: the
gradient in its norm is \(\nabla_U\), not an ordinary difference in a
fixed frame (CA-I 52626–52634). Under a real gauge transformation, the
field, current and covariant difference are conjugated at their
respective indices. In the difference, the gauge matrices at the
transported index cancel against those of the transformed link. Their
norms are therefore unchanged, as are the scalar scale weights. The
transformed global datum agrees with \((U,0)\) on \(S\).

Two such choices give admitted global complex data agreeing on the
field reading set of every retained word. The geometric record is held
fixed. The ported reading and gauge-covariance properties (Sh2), (Sh4)
therefore give the same term in the original frame. This also proves
agreement with every admitted global datum whose restriction is the
given local datum. No simultaneous real extension is used.

The global absolute sheet majorant at \(u_z\) bounds the partial sum
by \(\gamma_1\). On a finite-dimensional bond space, the account's
Schwarz comparison, applied to its scalar matrix elements, gives

\[
 \|\mathsf Q^{\mathsf b}(u_1)-\mathsf Q^{\mathsf b}(u_0)\|
 \le\frac{2\gamma_1}{r_{\rm reg}}
 =\frac{4a_Q\gamma_1}{a_1^{\oplus}}\le\frac{\gamma_0}{6}.
                                                               \tag{31}
\]

Here \(r_{\rm reg}\ge12\gamma_1/\gamma_0\ge12\), so evaluation
at one is inside the disc. At the flat base, the already proved tail
estimate of CA-I 47777–47787 gives
\(\mathsf Q^{\mathsf b}(u_0)\ge\gamma_0-\gamma_0/12\).
The partial family is real symmetric at the real point \(u_1\), as
in CA-I 47836–47842. Subtracting (31) gives
\(\gamma_0-\gamma_0/12-\gamma_0/6=3\gamma_0/4\).
Real gauge conjugation is unitary. This proves both bounds in (29).
Every term kept its original reading set throughout. \(\square\)

I then tried to feed (29) into the general sheet-inversion proof. The
attempt has a precise boundary. The account obtains its complex sector
bound by applying Schwarz on the full fibre about each real global
\(U\in\mathcal U_{\mathbb R}\), then compressing that global form
(CA-I 47850–47883). Lemma 3 supplies a real **partial form** and a path
from the flat base. It does not supply that full complex fibre.

For a local pair \(\mathbf U=e^{i\eta A'}U\), the direct replacement
would require a global admitted pair agreeing on the word's whole
reading set with

\[
 e^{i\eta\operatorname{Ad}(g)A'}e^{i\eta A},\qquad
 \operatorname{Ad}(g)J.                                    \tag{32}
\]

The perturbation about the flat base in (32) is a logarithm of a
product. It is not \(A+\operatorname{Ad}(g)A'\). One must control
that logarithm, its weighted difference bounds, all the supplied
radius ceilings, and its entire complex parameter range. The local-ball
lemma, CA-I 46800–46828 and 46920–46950, instead cuts off \(A',J\)
while retaining a globally given real \(U\). It proves no admission
statement for (32) about a new base. Applying it here would assume the
passage being sought.

There is also a second cover inside the form's original words. Its
inverse factors use the localisations of
\(\widetilde T=\widetilde{QG_0Q^T}\), not the unit-box matrix (28).
CA-I 47435–47533 compares them along a different flat-base path using
(reg)\(^{\sharp}\), the layered norms and their own ceilings. Field
readings use \(\widehat\square\); geometric readings use
\(\square^{\mathsf r}\) (CA-I 46321–46333, 46372–46409).
Replacing both with a smaller unit cube would change the word.
I did not obtain the joint bound for (32) on those original reading
sets at the printed radii. No failure of that bound is asserted.

**Exact failure of attack 5.** The need for a real global completion is
removed for the zero-current partial form (28). The attempted extension
to the assigned normalized resolvent words stops at the complex
recentring (32) with all its original field and geometric readings.
The proof of (29) cannot be substituted for that statement. Even if
recentring were supplied, the fixed-rate comparison identified in
attack 4 would still have to be carried through. These are requirements
of the single prescribed-word lemma stated in the final Result.

## 9. Attack 6: reconstruct the spectral family from all wall values

The local covariance estimate holds at arbitrary allowed subfamilies.
This suggests using **all** zero–one wall values, rather than only the
value with all parameters one. If every wall value determined a local
positive covariance, perhaps its functional calculus would determine
the missing companion, with the original assignment recovered by
inclusion–exclusion.

The first algebraic part works. On a finite set \(\mathcal C\) of
density cells, group an absolutely convergent family by its full cell
footprint \(S\subset\mathcal C\). Write its grouped coefficient as
\(F_S\). Deleting words outside \(V\subset\mathcal C\) gives

\[
 F[V]=\sum_{S\subset V}F_S,
 \qquad
 F_S=\sum_{V\subset S}(-1)^{|S|-|V|}F[V].                  \tag{33}
\]

To verify the second identity, insert the first. The coefficient of
\(F_T\), for \(T\subset S\), is
\(\sum_{T\subset V\subset S}(-1)^{|S|-|V|}\). This is one
when \(T=S\); otherwise the terms cancel in pairs, according to whether
one fixed cell of \(S\setminus T\) belongs to \(V\). This is a finite
identity, with no enumeration used as evidence.

However, (33) recovers only the **sum** of words sharing a footprint.
It recovers neither their step counts nor their spectral dependence.
In particular, the two terms in (25), with a common footprint, are
invisible in every \(F[V]\) at \(x=0\), but not after integration.
Even coefficient bounds obtained directly from (33) cost up to
\(2^{|S|}\); a bound on each wall sum does not supply the required
absolute word majorant at the unchanged rate.

I next tried the stronger input that each wall value was itself a
resolvent, so that its value at zero would determine the other values.
For the account's actual retention rule this input is false in general.
The following example uses its **own cell-word formulas**, rather than
replacing walk deletion by ordinary coordinate compression as in (15).

Take the scalar specialisation of those formulas with form
\(\mathsf A=aI\), \(a>0\), and only diagonal near-form entries.
There are no far entries. Keep the cells and the endpoint weights of
CA-I 6139–6146:

\[
 \kappa_q(b)=\tfrac12\bigl(1_{b_-\in q}+1_{b_+\in q}\bigr).
                                                               \tag{34}
\]

Choose a bond \(b\) crossing the face between two cells \(q,q'\).
Retain the complete words whose readable cell hull is \(q^\sharp\),
and delete the others. This can also be realised by a local reading
region: take a sufficiently fine \(M_1\)-grid outer approximation to
\(q^\sharp\), with excess width smaller than the cell spacing
\(\ell\). Choose \(\ell\) large relative to \(M_1\), as permitted
by its upward choice. The region then contains \(q^\sharp\) and no
other full cell hull. Work on a torus large enough to avoid wrapping.

Take \(Y=\{b\}\). The full family gives the scalar resolvent
\((x+a)^{-1}\). In the retained family, the formulas (8) give
\(T_q=a\), \(B_q=0\), and
\(P_q(x)=\kappa_q(b)/(x+a)\). All longer words vanish. Thus

\[
 R_W(x)=\frac1{2(x+a)},\qquad
 K_W=\frac1\pi\int_0^\infty x^{-1/2}R_W(x)\,dx
     =\frac1{2\sqrt a}.                                    \tag{35}
\]

For \(x\ne y\),

\[
 \begin{aligned}
 R_W(x)-R_W(y)&=\frac{y-x}{2(x+a)(y+a)},\\
 (y-x)R_W(x)R_W(y)&=\frac{y-x}{4(x+a)(y+a)}.
 \end{aligned}                                             \tag{36}
\]

So this retained family fails the resolvent identity. Moreover,
\(K_W^2=1/(4a)\ne R_W(0)=1/(2a)\), although \(R_W(0)>0\).
Taking the positive square root of the wall covariance changes the
assigned companion even in this example.

The defect is the missing partition of the identity. For all cells,
\(\sum_q\kappa_q=I\). For retained cells one has only
\(\sum_{q\text{ retained}}\kappa_q\le I\), with the value
\(1/2\) at the chosen bond. This is exactly the distinction recorded
in the account's local-family proof, CA-I 6937–6957. The example refutes
the proposed reconstruction rule. It is **not** a counterexample to
Proposition 2.4: both kernels in (35) have uniform bounds, and the scalar
form is not asserted to be the Yang–Mills fluctuation form.

Finally, analytic uniqueness alone does not repair the reconstruction.
Even after a coefficient's continuation is uniquely identified, a bound
on one domain need not persist on a larger domain. For example, for
\(0<r<1\), the entire functions

\[
 f_n(z)=e^{-\mu n}(z/r)^n
                                                               \tag{37}
\]

obey \(|f_n(z)|\le e^{-\mu n}\) on \(|z|\le r\), while
\(|f_n(1)|=e^{-(\mu+\log r)n}\). With \(r=e^{-\mu/2}\) this
loses half the rate. There are no poles or branch changes. This only
tests the inference from holomorphic continuation; it makes no claim
about CA's coefficients.

**Exact failure of attack 6.** All Boolean covariance values determine
grouped zero-parameter coefficients, but not the original spectral
words. The attempt to fill that missing information by local functional
calculus fails at (36). The attempt to fill the bound by analytic
uniqueness fails at (37). Thus neither reconstruction supplies the
normalized local word estimate left by attacks 4 and 5.

## Round 2 result (retained)

**Open lemma**

**Prescribed-word continuation at the fixed Stage-5 rate.** Fix a
density-decomposition instance of `2.4:prop-m-freeness`, its original
cells, geometry, free bonds, current variables, traces and local-data
class. Let \(M\) range over every value above its existing floors.
Keep the fixed global constants \((B_W,\delta_W)\), \(\mu_0\), and
the amplitude \(B_{\rm comp}\) of the global companion bound.
Where the companion is the root in CA-II 10120, that amplitude is
\(2\gamma_0^{-1/2}\), with the \(\gamma_0\) of that statement.
If its amplitude has not been named, name it from the global bound
**at Stage 5**, before any width reads it.

The following assertion remains to be proved. On the entire local-data
class of this instance, the **original** resolvent words
\(R^{\rm CA}_\nu(x;u)\) have compatible holomorphic local evaluations.
They keep their coefficients, step counts, complete field and geometric
reading sets, and their assigned parameter monomials \(s_\nu\).
Their termwise spectral integrals are the instance's assigned companion
words. This last assertion must identify the companion in the account;
it is not permission to define a replacement companion.

Let \(m_1\) be the already fixed constant in the global word estimate
CA-I 48012–48017, and set \(a=m_1/2\). There are nonnegative envelopes
\(A_\nu(b,b')\), independent of the local datum and of \(x\), such
that

\[
 \boxed{\begin{gathered}
 \sup_{x\ge0}
  (1+x/a)^{n(\nu)+1}
   \|R^{\rm CA}_\nu(x;u)(b,b')\|\le A_\nu(b,b'),\\[2mm]
 \sum_{\nu\text{ retained in }W}|s_\nu|\,
       \frac{\binom{2n(\nu)}{n(\nu)}}{4^{n(\nu)}}A_\nu(b,b')
 \le\frac{B_{\rm comp}}{\sqrt a}\,
             e^{-\mu_0\rho(b,b')}.
 \end{gathered}}                                           \tag{38}
\]

The bounds hold for all admitted local data and all parameter values
covered by that instance's bound. They hold also globally. They are
locally normally summable on the stated analytic domains. The envelopes
may carry the original geometric indices; the bound on their sum has
no dependence on \(M\), depth, volume, local region or datum. If words
are grouped in the density, (38) is read on their original constituent
words before integration. No new grouping or change of tags is allowed.

All constants on the right are fixed at Stage 5. The later choices
remain widths, then \(r',\ell\), then \(M\), then the account's radii
and coupling ceilings. In particular, (38) adds no upper bound on
\(M\), no smaller local-data class, and no reduction of \(\mu_0\)
after a width has read it. The comparison between the available sheet
rate and this fixed rate is part of (38), not an assumed identification.

This is **one sufficient lemma**, not an equivalence or a necessary
condition for Proposition 2.4. Compared with the first round's route,
it retains the explicit step factors and asks only for their integrated,
\(c_n\)-weighted summability. No claim is made that the printed global
Combes–Thomas bound already supplies these absolute word bounds at
\(\mu_0\).

**Implication to the requested statement.** Apply Lemma 2 with
\(H=B_{\rm comp}/\sqrt a\). The assigned local companion then obeys

\[
 \|K_{{\rm comp},W}(u)(b,b')\|
       \le B_{\rm comp}e^{-\mu_0\rho(b,b')}.               \tag{39}
\]

The other kernel estimate is the ported conclusion at CA-II
59602–59605. Both now use their unchanged global constants at local
data for all larger \(M\). Consequently the three floors (1), and the
widths that precede them, read precisely their original constants.
This proves the implication from (38) to Proposition 2.4 by hand.

The three new attacks end at the same quantitative task. Attack 4
proves exact spectral integration but cannot recover normalized word
bounds from a summed covariance estimate. Attack 5 proves (29) on one
real local cube; it does not supply complex recentring on the full
original readings at the printed radii. Attack 6 proves that all wall
values and analytic uniqueness do not reconstruct the required
spectral bounds. Sections 1–5, Lemma 2 and Lemma 3 are retained.
No counterexample to Proposition 2.4 has been obtained. The proposition,
and the prescribed-word lemma (38), remain open.

## 10. Third round: what the new inputs change

Provenance: Codex, 2026-11-05, checkout
`a5586b6f781f442f407f53e5b21ef17cbea5428c`. Research text, not an audit;
no status granted. Sections 1–9 and both earlier results are preserved.
The new arguments below have not been checked by another model.

Credit remains with Ethan Sussman and Levent Alpoge, with Claude and
Codex as authors of their text, and Tadeusz Balaban for the underlying
construction. The source revision remains `31a47c543775`.

I read this note whole before continuing (38). The outline and CA-I
were fetched once; the existing CA-II and CA-III were reused. All four
hashes match the pinned hashes in `mu.md`. Source identities, a copy
of the previous note, bounded source excerpts and the recovery checkpoint
are in `/tmp/mf-round3-a5586b6f7/`. The general workflow and repository
skills named by AGENTS.md are absent from this checkout. GOAL, the
specified FINISH sections, `port-map.md` Tables 1–3 and plan, and the
source indexes govern this bounded task.

The index searches preceded the source reads: outline chunks 10 and 12,
their neighbouring walk/root rows and obligations; the CA full index;
and the 4.12–4.19 index's background, operator and local-ball rows.
I rechecked the statement and every labelled occurrence listed in §1.
CA-II 59588 still declares the proof incomplete; 59607–59609 is still
the companion-kernel step. The assembly's implication language does
not supply a proof of it. No new counterexample to that proposition
is asserted below.

### Clause-by-clause comparison before the new attacks

The original comparison in §2 survives inspection of the current
hm Lemma 1 and Theorem 5, pw §§1, 8–9 and Result, hma D2–D4 and
Theorem 2, and in1's constant table and Lemmas 1–2. In particular,
hm groups polynomial entries **before** assigning labels. Hma adopts
that grouping for its Y form. Pw tags a composed operator's full hull
once. None identifies these assignments with the prescribed CA words.
The independent-current and constant-order differences remain.

The additional inputs are now available as proved or checked texts,
with their stated premises. Their scopes give the following comparison.

| Clause needed by (38) | New input | What it supplies; what it does not supply |
|---|---|---|
| The actual background branch | `mu.md`, Result and §§4–8 | The CA minimizer and its arbitrary-subdomain nesting in the specified Lemma-4 windows. It does not parametrize arbitrary independent-current pairs by physical pairs. |
| Cube gauges at the printed radius | `oc.md`, §§4–5 and Result | The own-constant gauge clause for the stated small/true-background pairs and its one-step transport. Its thin-cube argument uses an ambient minimal background; it is not an extension theorem for a field known only on an arbitrary union. |
| Stability under a twist | `ui.md`, §2 and Result | The two physical readouts, curvature and \(J_n(M^{\boldsymbol\cdot}V)\), obey the uniform increment bound. The separately supplied current remains a different coordinate. |
| The original local spectral families | `lrb.md`, §§3–5, 10 and Result | CA §4.4's three assigned families on their local polydiscs, retaining (W′), cell coercivity, symmetry and the stated setting. This is substantially more than a replacement Gaussian. It does not identify every Chapter-5 instance with that setting. |
| The fixed Stage-5 rate | `lrb.md`, §3; `port/p4-operator.md`, A9 | Lrb supplies its absolute rate \(\theta\), and A9 supplies the global sheet rate \(\delta_0\). Neither gives a comparison with the already fixed \(\mu_0\), in the same bond metric and for the same words. |
| The full local-data domain | P4 A9(H), its input table and check log | The local-ball theorem still starts from a globally given real \(U\). P4 also retains the unprinted original-hull format and assembly assertions as named hypotheses. Checking the port did not remove those hypotheses. |
| Finite local coordinates and response | `piv.md`, §§3–6; `pw.md` | A unique finite-read pivot graph in PIV's averaging convention, and PW's specified independent-current response bounds. Neither changes the CA word assignment or fixes the missing rate comparison. |

The decisive source lines for this comparison are CA-I 5517–5578
((W′), including datum-independent local majorants), 6095–6113
(\(\theta\)), 6219–6309 (the local cell family), 8110–8169
(the exact lrb setting and assignment), 45162–45234 (the two §4.13
statements), 45439–45521 (the three gauge conditions and independent
data radii), and 46073–46129 (A9's bounds and global-real-base clause).
CA-I 16104–16150 identifies UI's readouts. CA-II 8521–8539 and
10104–10186 fix the distinct role of \(\mu_0\). In particular,
the \(\gamma_0\) in that root lemma is not silently identified with
the similarly named constant in A9.

The following attacks do not repeat primitive completion, a new root
construction, or Boolean reconstruction. They test whether the new
physical charts determine the missing germ; whether a quantitative
perturbation can retain a fixed rate; and whether endpoint summation
can replace a strict contraction at that rate.

## 11. Attack 7: use the physical-current graph as the continuation set

Mu now identifies the minimizer branch and its restrictions. OC supplies
the corresponding real cube gauges. UI controls the branch's physical
current under a twist. It is tempting to pull the companion back to
that branch, prove the required estimate there, and extend it in the
independent current. This is a different route from constructing
global completions of individual patches.

The first part is legitimate within its scope. At an admitted true
pair with \(\sigma=\mathbb1\), port CA-II 10104–10186: the root
has the bound at its fixed \(\mu_0\). Mu can identify the physical
branch on its admitted windows. PIV can identify its own constrained
graph when its averaging conventions and domains are the ones in use.
Neither statement identifies a prescribed decoupled word outside that
physical setting.

The proposed identity-theorem passage has a sharper obstruction than
loss of a bound under analytic continuation. It does not determine
the ambient analytic function at all.

**Lemma 4 (the physical graph misses transverse current data).**
Let \(z\) be local field coordinates and let \(j(z)\) be their
holomorphic physical current. Suppose there is at least one independent
current coordinate \(w_1\). For any holomorphic matrix function
\(H(z,w)\),

\[
 F(z,w)=w_1\bigl(w_1-j_1(z)\bigr)H(z,w)                  \tag{40}
\]

vanishes both on the physical graph \(w=j(z)\) and on the
zero-current slice \(w=0\). All derivatives of its pullback along
either slice vanish. Nevertheless \(F\) need not vanish on any
ambient independent-current neighbourhood.

**Proof.** The pullbacks are identically zero by the two displayed
factors; differentiation of a zero function proves the derivative
assertion. In an open current ball, choose \(w_1\) different from
zero and from \(j_1(z)\). Taking \(H\) to be a nonzero constant
matrix then gives a nonzero value. This also covers \(j_1\equiv0\),
when the factor is \(w_1^2\). \(\square\)

Thus even all physical response derivatives and all zero-current
values do not identify the independent-current words. This is not
the failure in (37): there, the continuation was already identified.
Here the proposed initial set is not a uniqueness set.

Nor does a uniform weaker-rate envelope repair that defect. For a
scalar flat chart with \(j(0)=0\), take one labelled entry at
distance \(N\ge1\), from \(0\) to \(Ne_1\), and set

\[
 F_N(z,w)=\frac{e^{-\mu_0N}
             +w_1(w_1-j_1(z))e^{-\vartheta N}}{(N+1)^2},
 \qquad 0<\vartheta<\mu_0.                              \tag{41}
\]

On a small fixed chart the functions have a uniform absolute family
bound at rate \(\vartheta\): the remaining series is bounded by
\(\sum_{N\ge1}(N+1)^{-2}\). On both slices they have the stronger
rate. At \(z=0\) and any fixed small real \(w_1\ne0\), their
ratio to \(e^{-\mu_0N}\) is unbounded. Even multiplying by the
spectral integration factor \(c_N\ge1/(N+1)\) leaves an
exponential divided by a cubic polynomial. It still diverges.
These are tests of the proposed inference, not CA coefficients or
a counterexample to the global free-current theorem.

**Exact failure.** Mu, OC and UI settle branch and gauge matters in
their stated settings; they do not supply transverse derivatives of
the prescribed independent-current resolvent words. PIV solves an
averaging constraint and does not impose \(\mathbf J=J(\mathbf U)\)
on the free-current domain. P4 supplies that domain about a global
real base, but its clause (H) does not remove the base. The new
physical results therefore cannot identify the local germ in (38)
by this route. The missing information concerns transverse current
directions. Minimizer uniqueness does not determine it.

## 12. Attack 8: continue with an explicit budget at the fixed rate

Lrb supplies local holomorphy and an absolute family bound, including
independent currents, in its own setting. I tried to use its larger
polydisc to continue a stronger reference estimate without changing
\(\mu_0\). This uses its actual assigned family, not the identity
theorem from attack 7 or a new inverse-root prescription.

First consider the direct displacement argument. Write \(\rho_f\)
for the large field radius, to distinguish it from bond distance,
and put \(t=\varsigma/(\rho_f-\varsigma)\). Lrb §5's Cauchy
argument preserves the exponent of the available family norm. In
any common metric in which that norm has rate \(\vartheta\), it
gives a bound of the form

\[
 |K(u)-K(u_0)|(b,b')\le Dt e^{-\vartheta\rho(b,b')}.       \tag{42}
\]

It also holds for the absolute difference family when Cauchy's
formula is applied to its coefficients and summed: the boundary
integral of their nonnegative sum is at most the uniform family
bound. The locally normally convergent family justifies that exchange.
This adds no new estimate for data outside lrb's hypotheses.

If \(\vartheta<\mu_0\), no fixed positive \(t\), however small,
makes the right side bounded by a fixed multiple of
\(e^{-\mu_0\rho(b,b')}\) at all distances and volumes. The ratio
is \(Dt e^{(\mu_0-\vartheta)\rho(b,b')}\). The coupling ceiling
cannot depend on the diameter of the torus. Nor do the printed
floors force lrb's rate above \(\mu_0\):

\[
 \theta\le\frac{\gamma_*}{16e\mathsf B(r'+2\rho_w)}
       \longrightarrow0\quad(r'\longrightarrow\infty).   \tag{43}
\]

The near–far conditions allow sufficiently large \(r'\), followed
by sufficiently large \(\ell,M\). Equation (43) concerns the
**printed estimate**, not the actual decay of the kernels. Lemma 1
improves that estimate to an earlier rate, but still supplies no
comparison with the fixed \(\mu_0\).

I then tried to retain a reserve in the individual word bounds instead
of using the additive difference (42). This gives the following
quantitative criterion. It uses the original step count in (38).

**Lemma 5 (a sufficient perturbation budget for the original words).**
Keep \(a=m_1/2\), \(q_a(x)=a/(a+x)\), and every original label
and monomial. Suppose the local words are already defined holomorphically.
Suppose there are datum- and \(x\)-independent numbers
\(a_\nu(b,b')\ge0\) such that

\[
 q_a(x)^{-n(\nu)-1}\|R^{\rm CA}_\nu(x;u)(b,b')\|
       \le(1+\eta)^{n(\nu)+1}a_\nu(b,b'),\qquad \eta\ge0. \tag{44}
\]

For every allowed parameter value suppose also that

\[
 \sum_{n(\nu)=n}|s_\nu|a_\nu(b,b')\le(PT^n)(b,b'),
 \qquad |P|_{\mu_0}\le p,\quad |T|_{\mu_0}\le q<1,       \tag{45}
\]

where \(P,T\) are nonnegative kernels and \(|\cdot|_{\mu_0}\)
is the two-sided Schur norm in the account's bond distance. All
parameter costs are included in (45). These majorants do not change
any word, grouping, reading set or monomial. If

\[
 q_\eta:=(1+\eta)q<1,\qquad
 \sqrt a\,\frac{p(1+\eta)}{\sqrt{1-q_\eta}}
                  \le B_{\rm comp},                     \tag{46}
\]

then the two inequalities in (38) hold, with
\(A_\nu=(1+\eta)^{n(\nu)+1}a_\nu\).
The identification of the integrated words with the assigned companion
is still required. For uniform conclusions, the premises and constants
in (44)–(46) must hold uniformly over the same instances as (38).

**Proof.** Schur norms multiply by the triangle inequality for
\(\rho\); hence \(|PT^n|_{\mu_0}\le pq^n\). In particular,

\[
 \sum_\nu |s_\nu|c_{n(\nu)}A_\nu(b,b')
 \le p(1+\eta)e^{-\mu_0\rho(b,b')}
              \sum_{n\ge0}c_n q_\eta^n
 =\frac{p(1+\eta)}{\sqrt{1-q_\eta}}
              e^{-\mu_0\rho(b,b')}.                     \tag{47}
\]

Here the last equality can be checked without a summation algorithm.
The recurrence in Lemma 2 is
\((n+1)c_{n+1}=(n+\tfrac12)c_n\).
For \(f(z)=\sum c_nz^n\), absolute convergence on \(|z|<1\)
allows differentiation and gives \((1-z)f'(z)=f(z)/2\),
\(f(0)=1\). Differentiating \((1-z)^{1/2}f(z)\) shows it
is constant one. Thus \(f(z)=(1-z)^{-1/2}\).
Equation (46) proves the second inequality of (38), and (44) proves
the first. The geometric majorant at \(q_\eta<1\) gives local
normal convergence. Deleting complete labels only decreases it.
Lemma 2 then integrates the words without changing their tags.
\(\square\)

This criterion has a useful order of choice. If
\(\sqrt a\,p/\sqrt{1-q}<B_{\rm comp}\) at Stage 5, continuity
leaves a positive allowance for \(\eta\). A later field or current
ceiling can meet that allowance without altering any earlier constant.
If the budget is saturated, this argument gives no positive allowance;
one must prove unchanged envelopes, or find actual slack in the same
global bound. The square-root denominator in (46) is better than
the geometric denominator obtained by discarding the \(c_n\)'s.

There is an elementary way to obtain the factor in (44) **if** the
necessary primitive estimates are known. For a prescribed product
of \(n+1\) factors, let their reference envelopes be \(h_i\),
and bound each displacement by \(\eta h_i\) in the same
compatible matrix norm. Each factor is bounded by
\((1+\eta)h_i\); multiply these bounds and sum the prescribed
intermediate indices. This proves (44). If an original step has
several factors, its whole product must first be estimated with its
original reading set. No equality of the new envelopes with a bound
on the already summed operator follows.

**Exact failure.** Lrb supplies (42) on its local class and an
absolute moment at \(\theta\). P4 supplies the normalized global
step factor (CA-I 48012–48017) and its sheet estimate at
\(\delta_0\). Neither supplies (44)–(45) at the fixed
\(\mu_0\), with the original current-dependent factors, on every
Chapter-5 local datum. In particular, their statements give neither
\(q<1\) in that weighted majorant norm nor the amplitude margin
in (46). PW proves such estimates for its specified response family;
HM obtains a contraction by grouping its own polynomial entries.
Importing either grouping would change the prescribed object.
Thus small late radii alone do not close the gap. Lemma 5 states
exactly the additional quantitative information this attempt would use.

## 13. Attack 9: replace strict contraction by endpoint smoothing

The preceding attack asks for a strict weighted contraction. A different
possibility is to estimate each endpoint at the critical rate, using
four-dimensional diffusion in the step count. This was not used in
the earlier spectral integration argument: a critical scalar geometric
sum may diverge while its endpoint kernels decay with the number of steps.

**Lemma 6 (endpoint summation at the critical rate).** Suppose the
original normalized word envelopes exist as in (38), and for every
\(n\ge0\) their endpoint sum satisfies the following bound with
one Stage-5 constant \(D\), uniform in the instances of (38):

\[
 E_n(b,b'):=\sum_{n(\nu)=n}|s_\nu|A_\nu(b,b')
 \le D(n+1)^{-2}e^{-\mu_0\rho(b,b')}.                    \tag{48}
\]

Then their integrated sum is bounded by
\((5D\sqrt a/3)e^{-\mu_0\rho(b,b')}\). In particular,
\(5D\sqrt a/3\le B_{\rm comp}\) implies (38)'s summed bound.

**Proof.** The recurrence for \(c_n\) gives
\(c_n\le(n+1)^{-1/2}\). Indeed induction reduces its next step
to
\((2n+1)^2(n+2)\le4(n+1)^3\); the difference is \(3n+2\).
Consequently

\[
 \sum_{n\ge0}c_nE_n(b,b')
 \le D e^{-\mu_0\rho(b,b')}
       \sum_{n\ge0}(n+1)^{-5/2}
 \le\frac53D e^{-\mu_0\rho(b,b')}.                      \tag{49}
\]

The last inequality follows by bounding the tail after its first
term by \(\int_1^\infty t^{-5/2}dt=2/3\). Apply Lemma 2.
Uniform versions of (48) on compact analytic sets also give normal
convergence there. \(\square\)

This is a real alternative to a geometric word bound, not merely a
renaming of it. To test the mechanism, consider the lazy walk on
\(\mathbb Z^4\) with transition

\[
 (Pf)(v)=\tfrac12f(v)+\tfrac1{16}
       \sum_{i=1}^4[f(v+e_i)+f(v-e_i)] .                 \tag{50}
\]

Its Fourier multiplier is
\(p(t)=\tfrac12+\tfrac18\sum_i\cos t_i\in[0,1]\).
Concavity of sine on \([0,\pi/2]\) gives
\(1-\cos t\ge2t^2/\pi^2\) for \(|t|\le\pi\).
Therefore
\(p(t)^n\le\exp[-n|t|^2/(4\pi^2)]\).
The coefficients of the Laurent polynomial \(p^n\) are the transition
entries of \(P^n\). Integrating against a character selects each
coefficient. Taking absolute values and extending the resulting
Gaussian integral to \(\mathbb R^4\) gives
\(P^n(v,v')\le\pi^2n^{-2}\) for \(n\ge1\).
Here \(\int_{\mathbb R}e^{-ct^2}dt=\sqrt{\pi/c}\), as follows
by squaring the integral and using polar coordinates.
The bound at \(n=0\) is one. Thus the required power of the
step count is available in this infinite-volume comparison model.
This is only a test for a prospective **tilted** majorant; (50)
is not identified with the CA walk or its exponential tilt.

The target also includes finite periodic volumes. On a periodic
four-dimensional lattice with \(V\) sites, the same walk has
nonnegative Fourier eigenvalues and a constant eigenvector of
eigenvalue one. Fourier inversion at a diagonal entry gives

\[
 P^n(v,v)=V^{-1}\sum_{t}p(t)^n\ge V^{-1},\qquad
 \sum_{n\ge0}c_nP^n(v,v)
       \ge V^{-1}\sum_{n\ge0}\frac1{n+1}=\infty .         \tag{51}
\]

Hence infinite-volume transience cannot replace a uniform contraction
without controlling the finite-volume stationary mode. If the
comparison walk is killed by \(1-\epsilon\), its constant mode
alone contributes \(1/(V\sqrt\epsilon)\), by (47).
A qualitative positive killing rate is insufficient for uniform bounds.
This does not say that a weighted Schur norm equal to one always
causes divergence; it identifies the mode that this proposed
comparison argument must rule out.

I also tried to obtain that exclusion directly from the now available
positive local base. Positivity controls the signed matrix. It need
not control the absolute path majorant. The distinction is already
visible in three dimensions of coordinate space. Let

\[
 A=\begin{pmatrix}1&3/4&3/4\\3/4&1&3/4\\3/4&3/4&1\end{pmatrix},
 \qquad b=5/2,\qquad T=I-A/b .                           \tag{52}
\]

On constant vectors \(A\) has eigenvalue \(5/2\); on their
orthogonal complement it has eigenvalue \(1/4\). Thus \(A>0\)
and \(\|T\|=9/10<1\). Its convergent resolvent series is

\[
 (x+A)^{-1}=(x+b)^{-1}\sum_{n\ge0}
                 [b/(x+b)]^nT^n .                       \tag{53}
\]

Expanding each matrix power into coordinate paths and taking absolute
values replaces \(T\) by a matrix \(P_*\) with diagonal \(3/5\)
and off-diagonal \(3/10\). Its constant and orthogonal eigenvalues
are \(6/5\) and \(3/10\), respectively. Hence

\[
 (P_*^n)_{11}=\tfrac13(6/5)^n+\tfrac23(3/10)^n,
 \qquad \sum_{n\ge0}c_n(P_*^n)_{11}=\infty.              \tag{54}
\]

The lower bound (26) proves the divergence by hand. In contrast,
integrating (53) as grouped matrix powers converges. This is why
preserving the account's grouping matters. The example refutes an
inference from a spectral gap to a summable unsigned path majorant;
it is not a CA fluctuation form or a counterexample to Proposition 2.4.

**Exact failure.** No imported statement provides (48) for the
original words at \(\mu_0\). A Markov or heat-kernel interpretation
of their positive majorants has not been established. Even in the
comparison model, transience alone fails the periodic-volume clause
at (51). Lrb's positive base, P4's sector bound and HM's gaps cannot
supply this missing assertion just by taking absolute values, as
(52)–(54) show. A proof would need a uniform estimate for the actual
grouped words, including the finite-volume mode and the prescribed
parameter charges. Lemma 6 provides a sufficient endpoint criterion;
none of those additional properties is assumed to hold for CA.

## 14. Current checkpoint and limits

The newly proved statements are Lemma 4's obstruction to determining
the free-current germ from its physical slices, Lemma 5's fixed-rate
perturbation criterion, and Lemma 6's endpoint summation criterion.
Equations (51) and (54) give explicit failures of two proposed
majorant inferences. These are hand arguments. They are not new
properties of the CA family unless their displayed premises are met.
This round closes no CA obligation.

The new frozen inputs were used at their stated scopes. No open
premise in the operator port, lrb, mu, oc, ui, PIV or PW was promoted
to a theorem. In particular, there is no remaining proposal to
reprove mu's uniqueness, oc's cube gauge, or lrb's Gaussian comparison.
Those would not supply the missing transverse word estimates.

Recovery decision: the next round should inspect the **original
grouped step factors at free current**, on their complete local
reading sets. It must either obtain a common \(\mu_0\)-weighted
majorant with an explicit budget such as (44)–(46), or prove an
endpoint estimate such as (48) while controlling finite periodic
volumes. These are sufficient tests of the one lemma below, not new
requirements imposed on Proposition 2.4. A direct proof of the
proposition may avoid them. No failure example here refutes that
proposition or its prescribed-word lemma.

Only `library/mf.md` is changed. No prompt, ledger, audit file,
platform instruction or scientific status is changed. Tools were
used for source retrieval, bounded reading, hashes and editing;
no computation discharges a mathematical step. The new work remains
unreviewed research text.

## Result

**Open lemma**

**Prescribed-word continuation at the fixed Stage-5 rate.** For every
density-decomposition instance of CA `2.4:prop-m-freeness`, retain its
original cells, geometry, free bonds, traces, independent currents,
local-data domain, parameter range and word assignment. Let \(M\)
range over all values above its existing floors. Keep the global
Stage-5 constants \((B_W,\delta_W),\mu_0,B_{\rm comp}\) and the
global word constant \(a=m_1/2\) from CA-I 48012–48017.

The open assertion is that every prescribed resolvent word
\(R^{\rm CA}_\nu(x;u)\), \(x\ge0\), has a compatible holomorphic
evaluation on the whole stated local-data domain. It must retain
its coefficients, step count \(n(\nu)\), full field and geometric
reading sets, and original parameter monomial \(s_\nu\). Its
termwise spectral integral must be the account's assigned companion
word. This is an identification requirement, not a definition of
a new companion. There must be datum- and \(x\)-independent
envelopes \(A_\nu(b,b')\) such that

\[
 \sup_{x\ge0}(1+x/a)^{n(\nu)+1}
       \|R^{\rm CA}_\nu(x;u)(b,b')\|\le A_\nu(b,b'),
 \qquad
 \sum_{\nu\ {\rm retained\ in}\ W}|s_\nu|c_{n(\nu)}A_\nu(b,b')
 \le\frac{B_{\rm comp}}{\sqrt a}e^{-\mu_0\rho(b,b')},
 \qquad c_n=4^{-n}\binom{2n}{n}.                         \tag{55}
\]

The same bounds must hold globally and locally, normally on compact
analytic sets, for all admitted parameter values, depths, nests,
volumes and larger \(M\). They keep the original groups and their
constituent resolvent words as specified in (38). They add no upper
bound on \(M\), no restriction of the local-data class and no
later change of \(\mu_0\) or \(B_{\rm comp}\). Constants precede
the widths, \(r',\ell,M\), and the later radii and coupling ceilings.
When the companion is CA-II 10120's root, retain that statement's
amplitude \(B_{\rm comp}=2\gamma_0^{-1/2}\), with its own
\(\gamma_0\). No comparison with A9's similarly named constants
is presumed.

This is the same sufficient, stronger lemma as (38). Its implication
to the requested proposition is still a hand proof: Lemma 2 integrates
(55) to give
\(|K_{{\rm comp},W}(u)(b,b')|\le B_{\rm comp}e^{-\mu_0\rho(b,b')}\).
The first kernel bound is the ported CA-II 59602–59605 conclusion.
Both bounds then use their original global constants, so the Stage-5
widths and the three Stage-6 floors read them in their original order.

Three new attacks were made. Attack 7 fails because the physical
and zero-current slices do not determine transverse current data,
even with all their tangent derivatives. Attack 8 gives the exact
budget (46), but the imported bounds do not supply its original-word
majorants at the fixed rate; smaller radii alone cannot repair a lost
exponent. Attack 9 gives the endpoint criterion (48), but diffusion
does not remove the finite-volume stationary mode, and form positivity
does not bound the unsigned word majorant. These are specific failures
of the attempted deductions, not proofs that the needed estimates
are false for CA.

All earlier proved material is retained. Neither a complete proof
nor a counterexample to Proposition 2.4 was obtained in this round.
