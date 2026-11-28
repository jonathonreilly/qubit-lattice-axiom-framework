# One-field Hilbert insertion in four dimensions (row 171)
Provenance: Codex (GPT-6; runtime variant and effort unavailable; queue requests max), checkout `cfa884a833e244a4c452a13bc5546dc10e33354d`, Sussman–Alpoge commit `31a47c543775`. Research text; not an audit; grants no status.

## 1. Premises and claim

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. We port [YM3_I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), Propositions IV-55-9, IV-55-19 and IV-56-17 (lines 79104–79201 and 79374–79443). The [YM4 outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), UI1–UI10 (lines 28229–28521), supplies the four-dimensional rooted-count route. All deductions below are by hand.

The named premises are **full D1**, **S1g** from [am1-port.md](am1-port.md), Result, and **S6**, the Hilbert bridge. D1 includes the actual rooted indexing, source locality, representation independence, the entropy gap, upper stability and the unsourced floor. Constants are uniform in cutoff and compatible tori. S1g gives lattice translations and both site and bond reflections for every periodic Wilson DLR state. We assume S6's Hilbert realization on its translation-invariant separated-moment domain, with contraction semigroup \(e^{-tH}\).

We use the setting of [d2-d4.md](d2-d4.md), Results and equations (4)–(14); the needed estimates are derived below. Put \(a=L^{-K}\), \(a_s=L^{-s}\), with odd \(L\ge3\), fixed \(M=L^{m_0}\), and tori \(\ell=2L^m\), \(m\ge m_0\). Write \(\mathcal O_a(f)=\sum_p f(x(p))a_p\), where \(a_p=1-\tfrac12\operatorname{ReTr}U_p\). Set
\[
 X_a(f)=\mathcal O_a(f)-\nu\mathcal O_a(f),\qquad
 t_f=\|f\|_\sharp=\max(\|f\|_\infty,c_M\|\nabla f\|_\infty).
\]
Fix any sequence of pairs \((\rho_j,\nu_j)\) of periodic states at \(a_j=L^{-K_j}\to0\), whose centered separated moments converge to \(\sigma\). Existence of that sequence is not asserted here. Field polynomials are finite complex sums of products with separated entries in each product.

We will prove, for \(0<\eta\le1\), real \(k\in C_c^1\),
\[
 \begin{gathered}
 \operatorname{supp}k\subset B(y,\eta/(40L)),\qquad |y_4|\le\eta/8,\\
 \left|\sigma(\theta\overline F\cdot(k)\cdot G)\right|
 \le C\|k\|_\sharp\|F\|_{\eta/4}\|G\|_{\eta/4},\qquad
 \|F\|_b:=\|[\tau_{-be_4}F]\|_\sigma . \tag{1}
 \end{gathered}
\]
Every entry of \(F,G\) lies strictly above \(\eta/4\). The constant is independent of their degrees and coefficients. Thus rank 17 holds with \(p=0\). It implies the \(p=4\) form at SA line 28489 for the fixed admissible radius constant \(c_I=1/(40L)<1/64\). This is the small-ball insertion statement, not a bound for arbitrary supports.

## 2. The chessboard estimates used in the port

A cell function uses bonds wholly inside its open cell. Let \(D^{[C]}\) be its reflected copy, conjugated for odd reflection parity. Define
\[
 p_{l,\ell}(D)=\left\langle\prod_C D^{[C]}\right\rangle_\ell^{1/N},
 \qquad N=(\ell/l)^4. \tag{2}
\]
Here is the finite reflection positivity needed for this definition. Split every bond crossing either cut as \(U=VW^{-1}\), with independent Haar variables. Haar invariance preserves its original integral. Each crossing plaquette becomes \(\tfrac12\operatorname{ReTr}(AB^*)=q(A)\cdot q(B)\), where the two paths use opposite halves and \(q\in\mathbb R^4\) is the SU(2) quaternion coordinate. Expand
\[
 e^{\beta q(A)\cdot q(B)}
 =\sum_{n\ge0}\frac{\beta^n}{n!}
   \sum_{i_1,\ldots,i_n=1}^4
       \prod_rq_{i_r}(A)\prod_rq_{i_r}(B).
\]
The expansion converges absolutely. The remaining action and Haar factors split into reflected halves. Integrating \(\Theta\Phi\,\Phi\) therefore gives a sum of nonnegative coefficients times squared absolute integrals. This proves finite Wilson reflection positivity for \(\beta\ge0\). In particular, the root in (2) is nonnegative.

For completeness, reflection Cauchy–Schwarz gives the finite chessboard inequality as follows. In one coordinate, transport the finitely many slab profiles to one reference slab. There are an even number \(q\) of slabs. Normalize profile \(j\) by \((Z_j+\epsilon)^{1/q}\), where \(Z_j\) is its fully reflected integral. Maximize the absolute integral over all fillings with these normalized profiles. Reflecting either half preserves a positive maximum, since its square is bounded by the product of two values at most that maximum. Choose a maximizing filling with a longest constant run. A run of length at most \(q/2\) can end at the reflection plane and then doubles. A longer run contains a whole half, whose reflection makes the filling constant. Thus a constant filling maximizes. Its value is at most one. Let \(\epsilon\downarrow0\), then apply this inequality successively in four coordinates. Coordinate reflections commute, giving
\[
 \left|\left\langle\prod_C D_C\right\rangle_\ell\right|
 \le\prod_Cp_{l,\ell}(D_C). \tag{3}
\]
Expansion of the reflected product of \(D+E\), followed by (3), proves the triangle inequality for \(p\). Also
\(p(zD)=|z|p(D)\), \(p(\bar D)=p(D)\), \(p(1)=1\), and \(p(D)\le\|D\|_\infty\).

We also need (3) in any periodic state \(\rho\). For real bounded cell \(H\), sum its \(N\) copies in a cube of side \(\ell\). S1g makes their mean \(N\rho(H)\). Conditional Jensen and the DLR equation compare this sum with the torus exponential integral. The boundary cost is at most \(72\beta(\ell/a)^3\). Indeed, for each of six plaquette orientations, with \(n=\ell/a\), the common interior has \(n^2(n-1)^2\) plaquettes. The DLR and torus actions have respectively \(n^4+2n^3\) and \(n^4\) terms. Comparing numerator and denominator, using \(0\le a_p\le2\), gives that cost. Consequently
\[
 \rho(H)\le\log p_{l,\ell}(e^H)+72\beta l^4a^{-3}\ell^{-1}. \tag{4}
\]
For real \(V\), use \(H=\log(1+tV)\), \(|tV|\le1/2\). The inequalities \(\log(1+x)\ge x-x^2\) and \(p(1+tV)\le1+tp(V)\) apply. First send \(\ell\to\infty\) along any compatible sequence, then \(t\downarrow0\). This gives \(\rho(V)\le\liminf p(V)\). Apply it to \(\operatorname{Re}(e^{-i\phi}D)\), choosing \(\phi=\arg\rho(D)\), to obtain the absolute one-cell bound.

An aligned coarsening of ratio \(d=L^r\) has \(d^4\) fine cells. Its fine indices are
\(z+dj+\{-(d-1)/2,\ldots,(d-1)/2\}^4\).
Coarse reflections preserve fine walls and reflection parity. Apply (3) to the disseminated coarse product and take its coarse-cell root. This proves
\[
 p^{\rm coarse}_{dl,\ell}\!\left(\prod_{C\subset C'}D_C\right)
 \le\prod_{C\subset C'}p_{l,\ell}(D_C).
\]
Enclose any finite collection of cells in one such coarse cell and apply the absolute one-cell bound. We obtain
\[
 \left|\rho\!\left(\prod_C D_C\right)\right|
 \le\liminf_{\ell\to\infty}\prod_Cp_{l,\ell}(D_C). \tag{5}
\]
This proves the required domination and refinement estimates from the lattice model and S1g.

## 3. IV-55-9: multiple reflections with an insertion

Let the time faces of \(C\) be \(c,c+l\). On bounded local functions above \(c\), put
\[
 \langle B,A\rangle_c=\rho(\overline{\theta_cB}A),\quad
 T_DA=D\tau_{le_4}A,\quad D^\sharp=\overline{\theta_{c+l/2}D}.
\]
S1g and \(\theta_c\theta_{c+l/2}=\tau_{-le_4}\) give
\(\langle B,T_DA\rangle_c=\langle T_{D^\sharp}B,A\rangle_c\).
Indeed, expanding the right side gives the translate by \(-le_4\) of the left integrand. This is an identity on functions, before taking a Hilbert quotient.

Write \(K_D=T_{D^\sharp}T_D\) and \(s_n=\langle A,K_D^nA\rangle_c\). Moving these formal adjoints gives
\[
 s_{2r}=\|K_D^rA\|_c^2,\qquad
 s_{2r+1}=\|T_DK_D^rA\|_c^2,\qquad
 s_n^2\le s_{n-1}s_{n+1}. \tag{6}
\]
For odd \(n\), use Cauchy–Schwarz on \(K_D^rA,K_D^{r+1}A\). For even \(n\ge2\), use \(T_DK_D^{r-1}A,T_DK_D^rA\). If \(s_0=0\), the case \(n=1\) gives \(s_1=0\). Otherwise, either \(s_1=0\), or all ratios \(s_{n+1}/s_n\) increase. Hence
\[
 s_1^n\le s_0^{n-1}s_n. \tag{7}
\]
The expanded integrand for \(s_n\) has endpoints \(\overline{\theta_cA}\), \(\tau_{2nle_4}A\), and a column of \(2n\) factors. They alternate between \(\tau_{rle_4}D^\sharp\) for even \(r\) and \(\tau_{rle_4}D\) for odd \(r\). These are successive conjugated mirror copies. Each has fine seminorm \(p_{l,\ell}(D)\); midpoint reflection also preserves that seminorm.

Choose an odd \(d=L^r\) large enough to enclose \(A\) in the coarse cell immediately above \(c\). Keep its spatial center aligned with \(C\). For \(n\in d\mathbb N\), the reflected endpoint lies in the coarse cell below \(c\). The other endpoint lies in the coarse cell above \(c+2nl\). All column factors lie in the intervening coarse cells. Thus neither endpoint shares a coarse cell with a column factor. Apply (5), refine the middle cells, and use \(p(A)\le\|A\|_\infty\) only in the endpoint cells. With \(q_D=\liminf_\ell p_{l,\ell}(D)\), this gives
\[
 0\le s_n\le\|A\|_\infty^2q_D^{2n}. \tag{8}
\]
The volume limit comes first, for each fixed \(n\). Combine (7)–(8), take \(n\)-th roots, and let \(n\to\infty\) through multiples of \(d\). If \(q_D=0\), any such \(n\ge2\) already gives \(s_1=0\). Thus \(\|T_DA\|_c\le q_D\|A\|_c\). Cauchy–Schwarz with \(B\) gives
\[
 \boxed{\left|\rho(\overline{\theta_cB}D\tau_{le_4}A)\right|
       \le q_D\|B\|_c\|A\|_c.} \tag{9}
\]
Null vectors stay null. The endpoint supremum norm disappears in the root limit. Consequently the constant has no dependence on either polynomial degree. No estimate of \(p(AD)\) by \(\|A\|_\infty p(D)\) was used.

## 4. D1 gives a uniform middle-cell normalizer

Let real \(h\) be supported in the middle cube \(\|x-y_*\|_\infty\le l/4\), with \(l\le1\). First take \(a\le l/64\). D1 gives
\[
 \frac{|Z_\ell(W)|}{Z_\ell(0)}
 \le \exp\left\{\operatorname{Re}\left(U_\ell(W)+\sum_{s,X}e_{s,X}(W)\right)
                  +C_0\ell^4\right\},\qquad
 |e_{s,X}(W)|\le A e^{-\kappa m(X)}. \tag{10}
\]
The source terms vanish at zero. The point terms in \(U\) are holomorphic. Choose \(r>0\) so D1 admits source norm below \(2r\). Reflected periodization of \(zh\) has norm at most \(2|z|t_h\), so \(|z|t_h<r\) suffices, for every torus.

Here is the rooted count used in (10). At scale \(s\), \(X\) is a union of cubes of side \(Ma_s\). For a fixed cube \(Q\subset X\), a minimal meeting tree has \(m=m(X)\) edges. Choose a corner of \(Q\) on that tree in at most 16 ways. Traverse each edge twice, with eight choices per step. Every cube of \(X\) contains a tree vertex. Selecting these cubes among at most \(16(m+1)\) candidates gives
\[
 \#\{X:Q\subset X,\ m(X)=m\}
 \le16\,8^{2m}2^{16(m+1)}\le C e^{\kappa_Dm}. \tag{11}
\]
For this indexing, \(\kappa_D=2\log8+16\log2\) is a valid rate. Use D1's strict gap above the rooted bound, including any domain-type multiplicities. Summing the resulting geometric tail, and counting possible root cubes coordinate by coordinate, gives
\[
 \begin{aligned}
 \sum_{X:X^+\cap B(u)\ne\varnothing,\ m(X)\ge t}e^{-\kappa m(X)}
   &\le C(1+u/a_s)^4e^{-\gamma t},\\
 \sum_Xe^{-\kappa m(X)}&\le C\ell^4a_s^{-4},\qquad \gamma>0.
 \end{aligned} \tag{12}
\]
Indeed, fixed-layer dependence places a root within \(CMa_s\) of the ball. There are at most \(C(1+u/a_s)^4\) such cubes. Globally there are \((\ell/(Ma_s))^4\) cubes. The same traversal count holds on the torus quotient.

Retain all point terms and each domain term whose entire dependence region lies in one cell. Conjugate retained odd-cell values and divide their sum by \(N=(\ell/l)^4\). Call this holomorphic function \(E_{h,\ell}(z)\). For an odd cell, \(\overline{g(\bar z)}\) is holomorphic and has the required real part. Locality and representation independence justify this operation. Also \(E_{h,\ell}(0)=0\).

A discarded nonzero term sees a source copy and reaches a cell face. The margin \(l/4\) and tree diameter bound imply \(m(X)\ge c l/a_s-C\). For \(a_s\ge l\), use the **global** bound in (12), divided by \(N\). For \(a_s<l\), count once per source copy using the local bound. The respective costs per cell and scale are
\[
 C_1(l/a_s)^4,\qquad C_2(1+l/a_s)^4e^{-\gamma' l/a_s},\quad \gamma'>0. \tag{13}
\]
Because \(l\) and \(a_s\) are powers of \(L\), their sums are bounded by
\[
 B_0=C_0+\frac{C_1}{1-L^{-4}}
       +\frac{16C_2\,6!}{(\gamma')^6(1-L^{-2})}.
\]
For the last term, use \((1+L^j)^4\le16L^{4j}\) and
\(e^{\gamma'L^j}\ge(\gamma'L^j)^6/6!\). Thus all actual scales are included. Upper stability and the floor contribute only \(C_0l^4\le C_0\). Equation (10) now gives
\[
 p_{l,\ell}\!\left(e^{z\mathcal O_a(h)-E_{h,\ell}(z)}\right)
 \le Q_0:=e^{B_0},\qquad |z|t_h<r. \tag{14}
\]

At fixed cutoff, these normalizers are locally bounded uniformly in \(\ell\). Point terms have D1's fixed-cutoff bound; the domain bound follows from the finite sum over \(s\le K\) in (12). Cauchy bounds each Taylor coefficient uniformly on smaller discs. Select convergent coefficients successively along one subsequence. The same Cauchy bounds make the Taylor tails uniformly geometric on every still smaller disc. This proves locally uniform convergence to a holomorphic \(E_h\), with \(E_h(0)=0\). The subsequence depends only on torus data, not on \(\rho\) or \(\nu\). Homogeneity of \(p\) and (14) give
\[
 \limsup_\ell p_{l,\ell}\!\left(e^{z\mathcal O_a(h)-E_h(z)}\right)\le Q_0. \tag{15}
\]
The limit here uses that subsequence.

The other mesh ratios cause no loss. If \(3\le l/a<64\), contributing plaquettes remain inside the cell and
\(\|\mathcal O_a(h)\|_\infty\le12\,64^4\|h\|_\infty\), by counting their six orientations and using \(a_p\le2\). Take \(E_h=0\) and enlarge \(Q_0\) to at least \(e^{12r64^4}\). If \(l/a=1\), the middle cube contains no plaquette center, so the observable vanishes. These exhaust the allowed ratios. All constants were chosen from D1 and the fixed geometry, before choosing \(h,l,a\) or the states.

## 5. IV-55-19: one derivative and arbitrary centering

More generally, suppose real cell test \(h\) has one holomorphic normalizer \(E(0)=0\), radius \(\varrho/t_h\), and bound \(q_{D_z}\le Q\), where \(D_z=e^{z\mathcal O_a(h)-E(z)}\). The case \(h=0\) is immediate. Otherwise (9) bounds
\(\Phi(z)=\rho(\overline{\theta_cB}D_z\tau_{le_4}A)\)
by \(Q\|B\|_c\|A\|_c\). At fixed cutoff, the exponential series converges uniformly on compact parameter sets. Thus \(\Phi\) is holomorphic. Cauchy's formula, with radii increasing to \(\varrho/t_h\), bounds its derivative at zero by \(Qt_h\|B\|_c\|A\|_c/\varrho\).

Use the same normalizer with \(A=B=1\) in state \(\nu\). This gives
\(|\nu\mathcal O_a(h)-E'(0)|\le Qt_h/\varrho\).
The case \(D=1\) of (9) bounds the scalar correction. Subtraction proves
\[
 \left|\rho(\overline{\theta_cB}X_a(h)\tau_{le_4}A)\right|
 \le\frac{2Q}{\varrho}t_h\|B\|_c\|A\|_c. \tag{16}
\]
For a middle-cell test, (15) supplies \(Q=Q_0\), \(\varrho=r\). Hence \(C=2Q_0/r\) is uniform. No bound on the possibly divergent number \(E'(0)\) is required: it cancels between the two states.

## 6. IV-56-17: a fixed-gap continuum passage

Take the data of (1). Choose \(l=L^{-i}\) and \(y_*\), independently of the cutoff index, with
\[
 \frac{\eta}{5L}<l\le\frac\eta5,\qquad
 y_*\in L^{-i-2}\mathbb Z^4,\qquad
 \|y-y_*\|_\infty\le\frac{l}{2L^2},\qquad c=y_{*,4}-l/2.
\]
Rounding each coordinate gives \(y_*\). Since \(L\ge3\),
\[
 \operatorname{supp}k\subset\{\|x-y_*\|_\infty<l/4\},\qquad
 |y_{*,4}|+l/2\le\eta\left(\frac18+\frac1{10L^2}+\frac1{10}\right)
 \le\frac{17\eta}{72}<\frac\eta4. \tag{17}
\]
For the first inclusion, the radius is less than
\(l(1/8+1/(2L^2))\le13l/72<l/4\).
Put \(B=\tau_{2ce_4}F\), \(A=\tau_{-le_4}G\). Both lie strictly above \(c\), and
\(\theta_cB=\theta F\), \(\tau_{le_4}A=G\).

When \(K_j\ge i+2\), the center \(y_*\) is a lattice site. The odd integer \(l/a_j\) makes \(c\) a bond mirror. The translations \(2ce_4\) and \(-le_4\) are lattice translations. For sufficiently large \(j\), every participating plaquette stays in its required half-space or cell: its time coordinate extends by at most \(a_j/2\) from its center. S1g makes the centering law covariant under these exact lattice operations. Apply (16) to the corresponding centered lattice polynomials.

Every insertion tuple and norm tuple is fixed independently of \(j\) and has positive separation. The assumed convergence therefore passes (16) to \(\sigma\), including zero limiting norms. In S6's translation-invariant Hilbert realization, the two norm factors are
\[
 \begin{aligned}
 \|B\|_{\sigma,c}
   &=\|e^{-(c+\eta/4)H}[\tau_{-(\eta/4)e_4}F]\|_\sigma,\\
 \|A\|_{\sigma,c}
   &=\|e^{-(\eta/4-c-l)H}[\tau_{-(\eta/4)e_4}G]\|_\sigma.
 \end{aligned} \tag{18}
\]
Both times are positive by (17). S6's contraction bound proves (1). No moving test or half-lattice translation invariance was used in taking the cutoff limit. After downshifting the two outside polynomials, (1) is a bounded sesquilinear form. It kills null vectors, extends to the Hilbert completion, and represents an operator of norm at most \(C\|k\|_\sharp\). Complex \(k\) follows by splitting real and imaginary parts, with constant \(2C\).

## 7. Exactly what changes in dimension four

The changes occur in (2)–(5) and (10)–(13). Boards have \((\ell/l)^4\) cells; coarsening has \(d^4\) cells. Boundary comparison has six plaquette orientations and order \((\ell/a)^3\), giving (4). Root counting has eight walk directions and sixteen incident cubes. Local and global counts have fourth powers. Stability per cell costs \(C_0l^4\); the coarse-scale series is \(\sum L^{-4j}\). These counts preserve a constant middle-cell normalizer. The fourth coordinate replaces the third as time; rounding in (17) uses four coordinates. The adjoint identities, root limit, Cauchy estimates, centering cancellation and contraction argument do not change. No plate partition is needed for this small-ball form, so no dimension-dependent loss in \(\eta\) enters.

## Result

**Conditional on full rooted D1, S1g and S6, the three requested ports give rank 17 with \(c_I=1/(40L)\), \(p=0\), and \(C_I=2Q_0/r\).** Equation (1) is uniform in cutoff sequences, states, support positions and surrounding polynomial degrees and coefficients. It implies the requested \(C\eta^{-p}\|k\|_\sharp\) bound, including SA's weaker choice \(p=4\) for \(\eta\le1\).

D1, S1g and S6 remain named premises. In particular, ST6 without rooted counting does not supply (13). This proves no existence, plate-density or rotation theorem. Proved by Codex as a research implication; not yet checked by the other model. No scientific status is granted.
