# P3: Port of the complete account's free-field algebra

Provenance: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, *theorem_0_complete_account_raw_II.tex*, source commit `31a47c543775`, CA-II 69457–70152; repository base `0f018e1a401b347cae137a1d3317e378834dc6ab`. Port by Codex, 2026-11-05. Research text only; no audit or retained status. Not yet checked by another model. Balaban is credited at the inputs attributed to him below.


## Reading contract, conventions, and current checkpoint

CA-I and CA-II mean `theorem_0_complete_account_raw_I.tex` and `theorem_0_complete_account_raw_II.tex` at `31a47c543775`; SA means `YM4_sketch_500.tex` at that revision. The three files were fetched once in this session from the pinned raw URLs into `/tmp/sa_ca_I.tex`, `/tmp/sa_ca_II.tex`, and `/tmp/sa_ym4.tex`. Line numbers refer to those files. Exact source statements are retained in LaTeX blocks, followed by complete written proofs on the source route. An unqualified heading followed by a proof means **source-declared proved in full**, by CA-I 27–46; this declaration is not an independent check, and an implication retains its antecedents.

Source SHA-256 identities (bookkeeping only):

| File | SHA-256 |
|---|---|
| `/tmp/sa_ym4.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `/tmp/sa_ca_I.tex` | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| `/tmp/sa_ca_II.tex` | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |

The required GOAL, FINISH, chain-ca §7.2 and ca-full README were read. The entry-point `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent in this pinned checkout. Outline navigation used the README, neighbouring rows of chunks 02 and 24 and the corresponding obligations: SA 1733–1794, 2020–2037, 26002–26036 and 26133–26154 locate the exact-cochain covariance, Gaussian-square calculation, background conditioning and minimiser bounds. These outline passages are navigation and attribution, not substitutes for the CA proofs. The port map identifies these as the free-field inputs to its TPI/FREE row. `p1-base.md` is already ported and is not redone here. Only this file is edited. No mathematical conclusion rests on a computation.

The common finite torus has side period \(2L^{m+K}\) in bare lattice units, with \(m\ge1\), \(K\ge0\), and the standing blocking factor \(L\ge3\) (Balaban's convention is odd \(L>11\)). These are `1.1:def-lattice`, CA-I 403–445, already recorded in P1. Thus every period is at least six. Choose one positive orientation \(\mu<\nu\) for each plaquette. Inner products sum over sites and over positive orientations; oriented evaluation on a reversed plaquette changes sign. Write \(n=N^2-1\), \(N\ge2\).

The difference and cochain definitions at CA-II 69498–69514 are
\[
\nabla^+_\mu f(z)=f(z+e_\mu)-f(z),\quad
\nabla^-_\mu f(z)=f(z)-f(z-e_\mu),\quad
\nabla_\mu^2=\nabla^+_\mu\nabla^-_\mu,\quad \Delta=\sum_\mu\nabla_\mu^2,
\]
\[
(d_0\varphi)_\alpha=\nabla^+_\alpha\varphi,\qquad
(d_1\xi)_{\mu\nu}=\nabla^+_\mu\xi_\nu-\nabla^+_\nu\xi_\mu,\qquad
\Delta_1=d_1^*d_1+d_0d_0^*.
\]
A superscript \(+\) on an operator denotes its Moore–Penrose inverse (inverse on its positive eigenspaces and zero on its kernel), not a forward difference. Convolution uses counting measure: \((G*v)(z)=\sum_{z'}G(z-z')v(z')\).

## 1. Gaussian squares

**Source:** `8.1:lem-gaussian-squares`, CA-II:69457–69467; proof 69469–69496. **Status:** source-declared proved in full, confirmed at its unqualified heading and following proof. **Inputs:** a finite centred joint Gaussian family, as stated; the fourth-moment pairing identity used in the source is proved in F1 below. No RG or analytic hypothesis is used.

**Exact source statement:**

```latex
\begin{lemma}[Covariance of two sums of Gaussian squares]\label{8.1:lem-gaussian-squares}
Let $I$ and $J$ be finite index sets, and let $(\xi_\alpha)_{\alpha\in I}$ and
$(\eta_\beta)_{\beta\in J}$ be real random variables such that the joint family
$(\xi_\alpha,\eta_\beta)_{\alpha\in I,\,\beta\in J}$ is Gaussian and centred. Write
$\mathbb{E}$ for the expectation and
$\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\,\mathbb{E}[Y]$. Then
\begin{equation}\label{8.1:eq-gaussian-squares-1}
\operatorname{Cov}\Bigl(\sum_{\alpha\in I}\xi_\alpha^2,\ \sum_{\beta\in J}\eta_\beta^2\Bigr)
=2\sum_{\alpha\in I}\sum_{\beta\in J}\bigl(\mathbb{E}[\xi_\alpha\eta_\beta]\bigr)^2\ \ge\ 0 .
\end{equation}
\end{lemma}

```

**Proof, following CA-II 69469–69496.** All moments exist. To make the one input explicit, let \(Z\) be a finite centred Gaussian vector with covariance \(\Sigma\), possibly singular.

**(filled) F1 — the fourth pairing formula.** In an orthonormal eigenbasis of \(\Sigma\), write \(Z=\Sigma^{1/2}U\), where the nonzero eigencoordinates of \(U\) are independent standard normals and zero eigenvalues contribute zero. Completing the square in each one-dimensional Gaussian integral gives
\(\mathbb E e^{t\cdot Z}=\exp(\tfrac12t^T\Sigma t)\). Differentiating four times at zero is legitimate: for \(t\) in a bounded set a polynomial times \(e^{t\cdot Z}\) is bounded by a constant times \(e^{\epsilon|U|^2}\) times a polynomial, integrable for \(\epsilon<1/2\), by completing a square once more. The degree-four term is \((t^T\Sigma t)^2/8\). Differentiating with four separately labelled variables, including when the random variables coincide, yields exactly
\[
\mathbb E[abcd]=\mathbb E[ab]\mathbb E[cd]+\mathbb E[ac]\mathbb E[bd]+\mathbb E[ad]\mathbb E[bc].
\]
This also covers degenerate Gaussians by the same representation.

Apply this with \(a=b=\xi_\alpha\), \(c=d=\eta_\beta\). The first pairing is the product of means of the squares; the other two are each \((\mathbb E\xi_\alpha\eta_\beta)^2\). Consequently
\[
\operatorname{Cov}(\xi_\alpha^2,\eta_\beta^2)=2(\mathbb E\xi_\alpha\eta_\beta)^2.
\]
Expanding the two finite sums in the definition of covariance and distributing expectation gives the double sum of these covariances. Its terms are real squares with coefficient two, so it is nonnegative. Empty index sets give zero on both sides. This proves the printed statement.

## 2. Free lattice curvature covariance

**Source:** `8.1:lem-free-curvature-covariance`, CA-II:69516–69540; proof 69542–69598. **Status:** source-declared proved in full. **Inputs:** the preceding cochain definitions, `1.1:def-lattice` (definition), and the standard Gaussian law on the finite Euclidean subspace \(\operatorname{im}d_1\). Its covariance is verified below; no continuum comparison or minimiser estimate is used.

**Exact source statement:**

```latex
\begin{lemma}[The free lattice curvature covariance]\label{8.1:lem-free-curvature-covariance}
Let $n=N^2-1$. Let $\gamma_{\mathrm{ex}}$ be the standard Gaussian law on the orthogonal sum of $n$ copies of $\operatorname{im}d_1\subset\mathbb{R}^{\Lambda^2(\mathbb{F})}$, one copy for each colour; this is the free lattice Maxwell curvature in lattice units. Then under $\gamma_{\mathrm{ex}}$ distinct colour components are uncorrelated, and each colour component has covariance
\begin{equation*}
P_{\mathrm{ex}}=d_1\Delta_1^{+}d_1^{*}.
\end{equation*}
Put $G=(-\Delta)^+\delta_0$. For $x,y\in\mathbb{F}$ and ordered pairs $\mu\neq\nu$, $\rho\neq\sigma$,
\begin{equation}\label{8.1:eq-free-curvature-covariance-a}
\begin{aligned}
P_{\mathrm{ex}}\bigl((x;\mu\nu),(y;\rho\sigma)\bigr)
 &=\sum_{\alpha\in\{\mu,\nu\}\cap\{\rho,\sigma\}}
 \bigl\langle (d_1^*\delta_{(x;\mu\nu)})_\alpha,\,
 G*(d_1^*\delta_{(y;\rho\sigma)})_\alpha\bigr\rangle,\\
P_{\mathrm{ex}}\bigl((x;\mu\nu),(y;\mu\nu)\bigr)
 &=-\bigl(\nabla^2_\mu+\nabla^2_\nu\bigr)G(x-y),\\
P_{\mathrm{ex}}\bigl((x;\mu\nu),(y;\mu\sigma)\bigr)
 &=-\nabla^+_\nu\nabla^-_\sigma G(x-y)\qquad(\sigma\notin\{\mu,\nu\}).
\end{aligned}
\end{equation}
In particular the entry vanishes when $\{\mu,\nu\}\cap\{\rho,\sigma\}=\emptyset$. In $d=4$ the diagonal entries are
\begin{equation*}
P_{\mathrm{ex}}(p,p)=\tfrac12-\tfrac12|\mathbb{F}|^{-1}\qquad\text{for every } p\in\Lambda^2(\mathbb{F});
\end{equation*}
that is, the diagonal value is $\tfrac12$ up to the volume correction $-\tfrac12|\mathbb{F}|^{-1}$.
Every entry of $P_{\mathrm{ex}}$ is a linear combination of at most sixteen values of $G$.
\end{lemma}
```

**Proof, following CA-II 69542–69598.** If \(v_j\) is an orthonormal basis of a Euclidean subspace \(V\), its standard Gaussian is \(\sum_j U_jv_j\) with independent standard normals. Thus its covariance on ambient vectors \(u,v\) is \(\sum_j\langle u,v_j\rangle\langle v_j,v\rangle=\langle u,\Pi_Vv\rangle\). Separate copies have zero cross-covariances. It remains to identify the projection onto \(\operatorname{im}d_1\).

Commutation of the finite translations gives \(d_1d_0=0\), hence \(d_0^*d_1^*=0\). On \(W=\operatorname{im}d_1^*\), therefore, \(\Delta_1=d_1^*d_1\), and this operator maps \(W\) into itself. If \(d_1^*d_1u=0\), its scalar product with \(u\) is \(\|d_1u\|^2=0\). But \(\ker d_1=W^\perp\): indeed \(u\perp\operatorname{im}d_1^*\) is equivalent to \(\langle d_1u,w\rangle=0\) for every \(w\). Thus its restriction to \(W\) is injective and, by finite dimension, bijective. In particular \(W\subset\operatorname{im}\Delta_1=(\ker\Delta_1)^\perp\). The unique solution in \(W\) of \(\Delta_1u=v\), \(v\in W\), is therefore \(\Delta_1^+v\).

Decompose \(\xi=\xi'+\xi''\) with \(\xi'\in W\), \(\xi''\in\ker d_1\). Then \(\Delta_1^+d_1^*d_1\xi=\xi'\) and
\(d_1\Delta_1^+d_1^*d_1\xi=d_1\xi\). On \((\operatorname{im}d_1)^\perp=\ker d_1^*\) the same operator is zero. This proves \(P_{\rm ex}=d_1\Delta_1^+d_1^*=\Pi_{\operatorname{im}d_1}\).

**(filled) F2 — adjoints and cancellation of mixed differences.** Reindexing a periodic sum by \(z\mapsto z-e_\mu\) gives
\[
\sum_z(f(z+e_\mu)-f(z))g(z)
=\sum_z f(z)(g(z-e_\mu)-g(z)),
\]
so \((\nabla^+_\mu)^*=-\nabla^-_\mu\). Hence
\[
d_0^*\xi=-\sum_\alpha\nabla^-_\alpha\xi_\alpha,\qquad
(d_1^*\omega)_\nu=-\sum_{\mu\ne\nu}\nabla^-_\mu\omega_{\mu\nu}.
\]
For the second formula, combine the two terms in \(\sum_{\mu<\nu}\omega_{\mu\nu}(\nabla^+_\mu\xi_\nu-\nabla^+_\nu\xi_\mu)\) using \(\omega_{\nu\mu}=-\omega_{\mu\nu}\), then use the first adjoint formula. In particular
\[
(d_1^*d_1\xi)_\nu=-\sum_{\mu\ne\nu}\nabla^-_\mu\nabla^+_\mu\xi_\nu
+\sum_{\mu\ne\nu}\nabla^-_\mu\nabla^+_\nu\xi_\mu,
\quad
(d_0d_0^*\xi)_\nu=-\sum_\mu\nabla^+_\nu\nabla^-_\mu\xi_\mu.
\]
For \(\mu\ne\nu\) the mixed terms cancel by commutation. The remaining \(\mu=\nu\) term completes the missing diagonal difference, giving \((\Delta_1\xi)_\nu=-\Delta\xi_\nu\).

The identity \(\langle f,-\Delta f\rangle=\sum_\mu\|\nabla^+_\mu f\|^2\) shows that its kernel consists precisely of constants, because nearest-neighbour steps connect all sites. The mean-zero inverse is therefore unique. With \(V=|\mathbb F|\), \(G=(-\Delta)^+\delta_0\) has mean zero and satisfies \((-\Delta)G=\delta_0-V^{-1}\). For mean-zero \(v\), \(G*v\) has mean zero (sum over its first variable), and
\[
(-\Delta)(G*v)=v-V^{-1}\sum_{z'}v(z')=v.
\]
Uniqueness gives \((-\Delta)^+v=G*v\), component by component for \(\Delta_1^+\).

The evaluation identity
\(\langle d_1^*\delta_{(x;\mu\nu)},\xi\rangle=\nabla^+_\mu\xi_\nu(x)-\nabla^+_\nu\xi_\mu(x)\)
gives its two components \(-\nabla^-_\mu\delta_x\) in direction \(\nu\) and \(+\nabla^-_\nu\delta_x\) in direction \(\mu\). Both have zero mean. Insert these in the projection formula; only directions in the intersection of the two plane-index sets remain. This proves the first line of `8.1:eq-free-curvature-covariance-a` and vanishing for disjoint planes.

**(filled) F3 — shift and sign in the Green pairing.** Since \(\nabla^-_b\delta_y=\delta_y-\delta_{y+e_b}\),
\[
G*\nabla^-_b\delta_y(z)=G(z-y)-G(z-y-e_b)=\nabla^-_bG(z-y).
\]
The adjoint of \(\nabla^-_a\) is \(-\nabla^+_a\), so
\[
\langle\nabla^-_a\delta_x,G*\nabla^-_b\delta_y\rangle
=-\nabla^+_a\nabla^-_bG(x-y).
\]
For identical planes the direction-\(\nu\) term has two minus signs and yields \(-\nabla^2_\mu G\); the direction-\(\mu\) term yields \(-\nabla^2_\nu G\). For planes \((\mu,\nu)\), \((\mu,\sigma)\) only direction \(\mu\) remains, with positive signs on both component differences, and yields \(-\nabla^+_\nu\nabla^-_\sigma G\). Reversed plane orientations multiply the corresponding evaluation vector by minus one, so the formulas cover ordered pairs exactly as stated.

Negation and coordinate permutations preserve both the equation for \(G\) and its zero mean on the equal-period torus. Uniqueness makes \(G\) invariant under these operations. Thus
\(\nabla^2_\mu G(0)=2(G(e_\mu)-G(0))\) is independent of \(\mu\), and
\[
-\nabla^2_\mu G(0)=\tfrac14(1-V^{-1}),\qquad
P_{\rm ex}(p,p)=\tfrac12(1-V^{-1}).
\]
Finally
\[
\nabla^+_a\nabla^-_bG(r)
=G(r+e_a)-G(r+e_a-e_b)-G(r)+G(r-e_b).
\]
There are at most two common directions and four values per term, hence at most eight values, which in particular proves the printed upper bound of sixteen without changing it. No correction is needed for this lemma.


## 3. Background definitions and Gaussian kernel positivity

**Inputs and status.** `8.1:def-background-kernel`, CA-II 69600–69640, defines the Gaussian background using Balaban CMP 95 (1.3), (1.5), (1.18), (1.19). The asserted realization as the actual massless lattice Gaussian, with a specified gauge/zero-mode convention and the indicated block map, and its identification with Balaban's linear variational minimiser, are retained as **H-BG**. They are not proved in full in that definition. The exact-cochain Gaussian of §2 is already defined without these identifications. Conditional expectation for finite jointly Gaussian vectors is established below, so no nonsingular block covariance is silently assumed.

In one colour, let \(\mathcal A\) be the centred Gaussian 1-cochain of H-BG, \(B=Q_{k_0}\mathcal A\), \(k_0=K-s\), \(A_B=\mathbb E[\mathcal A\mid B]\), and \(F_B=d_1A_B\). The block map is the same real linear map in each independent colour. With attachment point \(x_p=x\) for \(p=(x;\mu\nu)\), define, exactly as in `8.1:eq-background-kernel-1`–`3`,
\[
C^{\rm bg}_{K,s}(p,q)=\mathbb E F_B(p)F_B(q),\qquad
C^{\rm fl}(p,q)=\mathbb E\operatorname{Cov}(d_1\mathcal A(p),d_1\mathcal A(q)\mid B),
\]
\[
\mathcal K_{K,s}(f_1,f_2)=\sum_{p,q}f_1(x_p)f_2(x_q)C^{\rm bg}_{K,s}(p,q)^2,
\quad k(x,y)=\sum_{p:x_p=x}\sum_{q:x_q=y}C^{\rm bg}_{K,s}(p,q)^2,
\quad b_0=n/2.
\]
There are six plaquettes attached to each site. These are attachment points, not the barycentres used in some earlier notations; no change between the two evaluations is made. The free kernel `8.1:eq-background-kernel-5` (CA-II 69661–69667) is the same double sum with \(P_{\rm ex}\) in place of \(C^{\rm bg}\).

**(filled) F4 — Gaussian conditioning, including singular data.** Let \(S=\operatorname{Cov}(\mathcal A)\), \(D=QSQ^*\), and \(T=SQ^*D^+\). If \(v\in\ker D\), then \(0=v^TDv=\|S^{1/2}Q^*v\|^2\), so \(SQ^*v=0\). Thus \(SQ^*D^+D=SQ^*\). The Gaussian residual \(R=\mathcal A-TB\) has zero covariance with \(B\). Their joint Gaussian characteristic function is the exponential of minus one half their covariance quadratic form; zero cross-covariance factors this function into its two marginals, proving independence. Hence \(\mathbb E[R\mid B]=0\) and \(A_B=TB\). In particular \(F_B\) is a centred linear Gaussian image. Applied to independent colour copies with the same \(Q,S\), this proves both identical one-colour covariances and independence of different colours. This is a finite Gaussian argument, not a proof of H-BG's identification with the RG construction.

For completeness the decomposition `8.1:eq-background-kernel-4`, CA-II 69647–69659, follows on H-BG's further identification \(\operatorname{Cov}(d_1\mathcal A)=P_{\rm ex}\). Put \(Y=d_1\mathcal A\) and \(Z=Y-F_B\). Finite linearity gives \(\mathbb E[Y\mid B]=F_B\) and \(\mathbb E[Z\mid B]=0\), so both cross terms in \(\mathbb E[(F_B+Z)(F_B+Z)^T]\) vanish. The residual term is the expected conditional covariance, yielding \(P_{\rm ex}=C^{\rm bg}+C^{\rm fl}\). The later free/background comparison `8.1:eq-background-kernel-6` is not used or ported here.

**Source:** `8.1:lem-kernel-positivity`, CA-II:69682–69736; proof 69738–69837. **Status:** source-declared proved in full. **Inputs:** `8.1:lem-gaussian-squares` (§1), `8.1:lem-free-curvature-covariance` (§2), `1.1:def-lattice` (period condition), and `8.1:def-background-kernel` (H-BG for the background specialization only). Parts (b), (c), and (d) require no minimiser bounds.

**Exact source statement:**

```latex
\begin{lemma}[The Gaussian two-point covariance and positivity of the kernel]
\label{8.1:lem-kernel-positivity}
Let $n=N^2-1$. Write $F^a(p)$, $a=1,\dots,n$, for the colour components at the plaquette $p$ of
$\mathbb{F}$ of a curvature field $F$, and let $F=(F^a(p))_{a,p}$ be a centred, jointly Gaussian
family with
\begin{equation}\label{8.1:eq-kernel-positivity-1}
\mathbb{E}\bigl[F^a(p)F^b(q)\bigr]=\delta^{ab}\,C(p,q)
\end{equation}
for a real function $C$ on pairs of plaquettes. For a real function $f$ on the plaquettes of
$\mathbb{F}$ put
\begin{equation*}
X^{(2)}(f):=\tfrac12\sum_{a=1}^{n}\sum_{p}f(p)\bigl(F^a(p)\bigr)^2 .
\end{equation*}
For real functions $f_1,f_2$ on the plaquettes we write $\mathcal{K}^{\mathrm{ex}}(f_1,f_2)$ and
$\mathcal{K}_{K,s}(f_1,f_2)$ for the kernels of Definition~\ref{8.1:def-background-kernel} with
$f_i(x(p))$ replaced by $f_i(p)$; in particular
\begin{equation*}
\mathcal{K}^{\mathrm{ex}}(f_1,f_2)=\sum_{p}\sum_{q}f_1(p)f_2(q)\,P_{\mathrm{ex}}(p,q)^2 .
\end{equation*}
For test functions on the torus the two readings agree with $f_i(p):=f_i(x(p))$.
\begin{itemize}
\item[(a)] For all real $f_1,f_2$,
\begin{equation}\label{8.1:eq-kernel-positivity-a}
\operatorname{Cov}\bigl(X^{(2)}(f_1),X^{(2)}(f_2)\bigr)
=b_0\sum_{p}\sum_{q}f_1(p)f_2(q)\,C(p,q)^2,
\end{equation}
where
\begin{equation*}
b_0=\bigl(\tfrac12\bigr)^2\cdot 2\cdot n=\frac{N^2-1}{2}\neq0 .
\end{equation*}
In particular, the covariance equals $b_0\,\mathcal{K}^{\mathrm{ex}}(f_1,f_2)$ when $F$ is
distributed according to $\gamma_{\mathrm{ex}}$, so that $C=P_{\mathrm{ex}}$. It equals
$b_0\,\mathcal{K}_{K,s}(f_1,f_2)$ when $F=F_B$ is the background curvature, so that
$C=C^{\mathrm{bg}}_{K,s}$.
\item[(b)] For every real function $f$ on the plaquettes with $f\not\equiv0$,
\begin{equation}\label{8.1:eq-kernel-positivity-b}
\mathcal{K}^{\mathrm{ex}}(f,f)>0 .
\end{equation}
\item[(c)] If $f_1\ge0$ and $f_2\ge0$, every term of the double sums defining
$\mathcal{K}^{\mathrm{ex}}(f_1,f_2)$ and $\mathcal{K}_{K,s}(f_1,f_2)$ is non-negative.
\item[(d)] With $\delta_p$ the $2$-cochain equal to $1$ on $p$, to $-1$ on $p$ with reversed
orientation, and to $0$ on every other plaquette, $d^*$ the adjoint
of $d_1$, $\langle\cdot,\cdot\rangle$ the standard inner product of $1$-cochains on $\mathbb{F}$, and
$(-\Delta)^+$ the pseudo-inverse of the lattice Laplacian acting on each component of a
$1$-cochain,
\begin{equation}\label{8.1:eq-kernel-positivity-2}
b_0\,\mathcal{K}^{\mathrm{ex}}(f_1,f_2)=\frac{N^2-1}{2}\sum_{p}\sum_{q}f_1(p)f_2(q)
\bigl[\langle d^*\delta_p,(-\Delta)^+d^*\delta_q\rangle\bigr]^2 .
\end{equation}
Each bracket is a sum of at most two second differences of $G$. The right side therefore
involves only $f_1$, $f_2$ and finitely many values of the Green's function
$G=(-\Delta)^+\delta_0$ of Lemma~\ref{8.1:lem-free-curvature-covariance}, and no quantity of the
renormalisation-group construction.
\end{itemize}
\end{lemma}
```

**Proof, following CA-II 69738–69837.**

(a) Expanding finite sums and using §1 on each two-variable pair gives
\[
\begin{aligned}
\operatorname{Cov}(X^{(2)}(f_1),X^{(2)}(f_2))
&=\tfrac14\sum_{a,b,p,q}f_1(p)f_2(q)\operatorname{Cov}(F^a(p)^2,F^b(q)^2)\\
&=\tfrac14\sum_{a,b,p,q}f_1(p)f_2(q)\,2(\delta^{ab}C(p,q))^2\\
&=\tfrac n2\sum_{p,q}f_1(p)f_2(q)C(p,q)^2.
\end{aligned}
\]
Here \((\delta^{ab})^2=\delta^{ab}\) and its sum over \(a,b\) is \(n\). Since \(N\ge2\), \(b_0=n/2>0\). This calculation permits arbitrary signed real tests. The self-contractions contribute exactly the constant mean \(\mathbb E X^{(2)}(f)=\tfrac n2\sum_pf(p)C(p,p)\), removed by the definition of covariance. For \(\gamma_{\rm ex}\), §2 supplies \(C=P_{\rm ex}\) and independent colours. For \(F_B\), F4 supplies centred Gaussianity, independent identical colours, and \(C=C^{\rm bg}\). These give the two stated specializations.

(b) Taking equal tests and \(C=P_{\rm ex}\) in (a) first gives \(b_0\mathcal K^{\rm ex}(f,f)=\operatorname{Var}X^{(2)}(f)\ge0\). Suppose it is zero. On \(V=\operatorname{im}d_1\), put \(q_f(v)=\sum_pf(p)v(p)^2\). The variables \(q_f(F^a)/2\) are independent and have finite second moments. The variance of their sum is the sum of their nonnegative variances, so each is zero and \(q_f(F^1)=c\) almost surely for a constant \(c\).

In orthonormal coordinates the standard Gaussian on \(V\) has density \((2\pi)^{-\dim V/2}e^{-|v|^2/2}>0\). Every nonempty open ball has positive measure. If the continuous function \(q_f-c\) were nonzero at a point, it would remain bounded away from zero in a sufficiently small ball, contradicting its almost sure vanishing. Thus \(q_f=c\) everywhere, and evaluation at zero gives \(c=0\). Expanding the two squares in \(q_f(u+v)-q_f(u-v)\) gives
\[
\sum_pf(p)u(p)v(p)=\tfrac14(q_f(u+v)-q_f(u-v))=0\quad(u,v\in V).
\]

Fix \(\bar p=(x;\mu\nu)\) with \(\mu<\nu\). Let \(b=(x,\mu)\) and \(b'=(x+e_\nu,\mu)\) be its opposite positively oriented \(\mu\)-bonds. The coboundaries of their unit 1-cochains are zero except on incident plaquettes, where their values are \(\pm1\).

**(filled) F5 — unique common plaquette and its signs.** An incident plaquette to \(b\) in a plane containing \(\mu\) has corner \(x\) or \(x-e_\rho\), for \(\rho\ne\mu\). A common plaquette incident to \(b'\) must have the same plane, hence the same \(\rho\), and corner \(x+e_\nu\) or \(x+e_\nu-e_\rho\). Write these alternatives as \(x-ae_\rho=x+e_\nu-ce_\rho\), \(a,c\in\{0,1\}\). Each coordinate of their difference has absolute value at most two. Since the periods are at least six, equality modulo periods is equality in \(\mathbb Z^4\). It reduces to \(e_\nu=(c-a)e_\rho\), which forces \(\rho=\nu\), \(c=1\), \(a=0\). The only common plaquette is therefore \(\bar p\). Directly from \(d_1\),
\[
d_1\delta_b(\bar p)=1,\qquad d_1\delta_{b'}(\bar p)=-1.
\]
Substituting \(u=d_1\delta_b\), \(v=d_1\delta_{b'}\) into the polarized identity gives \(0=-f(\bar p)\). Since \(\bar p\) was arbitrary, \(f=0\), the desired contradiction. This proof establishes strict positivity only for the full free kernel, as printed; it does not assert strict positivity of the background kernel for arbitrary signed tests.

(c) For nonnegative \(f_1,f_2\), every summand \(f_1(p)f_2(q)C(p,q)^2\) is nonnegative, for either real covariance in question.

(d) From §2, each component of \(d_1^*\delta_p\) has mean zero and is zero unless its direction belongs to the plane of \(p\). On these components \(\Delta_1^+\) is convolution with \(G\), and is the componentwise \((-\Delta)^+\). Consequently
\[
P_{\rm ex}(p,q)=\sum_\alpha\langle(d_1^*\delta_p)_\alpha,G*(d_1^*\delta_q)_\alpha\rangle
=\langle d_1^*\delta_p,(-\Delta)^+d_1^*\delta_q\rangle.
\]
Squaring, summing with the test weights, and multiplying by \(n/2\) gives `8.1:eq-kernel-positivity-2`. There are at most two common directions, each contributing a signed second difference as in F3. Its four displayed Green values contain no RG data. This completes (d) and the lemma.

## 4. Tower input needed by the kernel bounds

**Source:** `8.1:lem-background-tower`, CA-II:69849–69872; proof 69874–69912. **Status:** source-declared proved in full as an implication. The finite conditional-expectation decomposition is proved here on the definitions; its identification with the actual unit-coupling Balaban tower remains **H-TOWER**, not a consequence of orthogonality. The source's last proof paragraph (69903–69912) appeals to the flat-step/free-field identification. The related `8.2:def-flat-quadratic-form`, CA-II 75437–75479, explicitly uses Balaban CMP 95 §1, (1.19), (1.23)–(1.24), and CMP 109 (0.21)–(0.22) as stated; CA-II 145581–145582 lists the identification as printed without proof. Credit Tadeusz Balaban for this identification and the tower of CMP 95 (1.16)–(1.19), used in CMP 109.

**Exact supporting source statement:**

```latex
\begin{lemma}[The background covariance as an orthogonal tower]\label{8.1:lem-background-tower}
Let $\mathcal{A}$, $B=Q_{k_0}\mathcal{A}$, $A_B$, $F_B=dA_B$,
$C^{\mathrm{bg}}=C^{\mathrm{bg}}_{K,s}$ and the Gaussian law with its expectation $\mathbb{E}_\gamma$
be as in Definition~\ref{8.1:def-background-kernel}, with $k_0=K-s$. Let $i_*\ge0$ be the index of
the last block step of Ba{\l}aban's tower above level $k_0$. For $0\le i\le i_*$ let $Q^{(i)}$ be the
$i$-fold composition of the linearised one-step block-averaging map $Q$ of
Definition~\ref{1.5:def-block-average}, with $Q^{(0)}$ the identity, and put
$\mathcal{G}_i:=\sigma(Q^{(i)}B)$, the $\sigma$-algebra generated by the $i$-fold blocked field; for
$i>i_*$ let $\mathcal{G}_i$ be the trivial $\sigma$-algebra. Put
\begin{equation}\label{8.1:eq-background-tower-1}
F_{B,i}:=\mathbb{E}_\gamma[F_B\,|\,\mathcal{G}_i]-\mathbb{E}_\gamma[F_B\,|\,\mathcal{G}_{i+1}],
\qquad
C^{\mathrm{step}}_i(p,q):=\mathbb{E}_\gamma[F_{B,i}(p)\,F_{B,i}(q)].
\end{equation}
Then the $F_{B,i}$ are orthogonal martingale differences along the decreasing sequence of
$\sigma$-algebras $(\mathcal{G}_i)_{i\ge0}$, only finitely many of them are non-zero, and
\begin{equation}\label{8.1:eq-background-tower-2}
C^{\mathrm{bg}}(p,q)=\sum_{i\ge0}C^{\mathrm{step}}_i(p,q)
\qquad\text{for all plaquettes } p,q.
\end{equation}
The right-hand side of \eqref{8.1:eq-background-tower-2} is Ba{\l}aban's tower of renormalisation
steps above level $k_0$ with all couplings set equal to one, in the form stated in
\cite[(1.16)--(1.19)]{B-CMP95} and used in \cite{B-CMP109}.
\end{lemma}
```

**Proof of the finite decomposition on the source route.** Use `8.1:def-background-kernel` and the linear iteration in `1.5:def-block-average` (definition) to form the \(\mathcal G_i\) in the statement. For \(i<i_*\), \(Q^{(i+1)}B=Q(Q^{(i)}B)\) gives \(\mathcal G_{i+1}\subset\mathcal G_i\); at and after the last index the next sigma algebra is trivial. Let \(M_i=\mathbb E[F_B\mid\mathcal G_i]\); \(M_0=F_B\) because \(F_B\) is a function of \(B\), as F4 supplies. It is a vector of square-integrable centred random variables, \(M_0=F_B\), and \(M_{i_*+1}=0\). Thus
\[
F_B=\sum_{i=0}^{i_*}(M_i-M_{i+1}),\qquad F_{B,i}=0\quad(i>i_*).
\]
For nested sigma algebras, the defining integral identity for conditional expectation gives \(\mathbb E[M_i\mid\mathcal G_{i+1}]=M_{i+1}\), by testing on each event of \(\mathcal G_{i+1}\). Hence \(\mathbb E[F_{B,i}\mid\mathcal G_{i+1}]=0\). If \(i<j\), then \(F_{B,j}\) is \(\mathcal G_j\)-measurable and therefore \(\mathcal G_{i+1}\)-measurable. Conditioning the product gives
\(\mathbb E[F_{B,i}(p)F_{B,j}(q)]=0\).

**(filled) F6 — integrability and both cross-index orders.** Conditional Jensen gives \(\mathbb E M_i(p)^2\le\mathbb E F_B(p)^2<\infty\); thus all the products just used are integrable by Cauchy–Schwarz. The conditional product identity follows first for bounded measurable factors and then by truncation and this \(L^2\) bound. If \(j<i\), exchange \((i,p)\) and \((j,q)\) in the already proved identity. Therefore expansion of the two finite telescoping sums leaves only terms \(i=j\), proving
\(C^{\rm bg}(p,q)=\sum_{i\ge0}C_i^{\rm step}(p,q)\).
The terminal difference at \(i_*\), including all remaining covariance, is retained; there is no discarded zero-mode or last-scale remainder. Under H-TOWER these particular covariances are Balaban's unit-coupling tower steps, which is the last sentence of the source statement. Its identification is explicitly conditional here.


## 5. Kernel bounds, with the displayed analytic hypotheses retained

**Source:** `8.1:lem-kernel-bounds`, CA-II:69925–70000; proof 70002–70152. **Status:** source-declared proved in full **from (h1)–(h3)**, confirmed at the heading and the explicit assumptions. The operational content of those assumptions is not proved in this port. The mass-upper-bound step in (e) needs the correction C1 below; the exact source statement is kept unchanged for comparison.

**Inputs by label and status.**

- `8.1:def-background-kernel`, CA-II 69600ff.: definition, with H-BG as in §3. `8.1:lem-background-tower`, CA-II 69849ff.: finite decomposition proved in §4; H-TOWER retains the identification with Balaban's steps.
- **H1-MIN / (h1)**, CA-II 69927–69929: the linear-minimiser estimates attributed to Balaban **CMP 102b, Theorem 1, (9)–(10)**, together with the operator theorem at free current. The latter is `4.14:thm-operator-theorem`, CA-I 46035–46156, whose heading declares a theorem and whose statement expressly assumes its prepared-nest conditions (A1), (A2), block-size floors and ceilings. It is not ported here; none of those admission conditions is discharged. The source proof at CA-II 70004–70016 says specifically that (h1) supplies **both bounds (a) for these covariances**, not merely an estimate for an unspecified linear map. We retain that operational implication, with the constants \(C_u,\delta_\square\), as part of H1-MIN. No derivation of (a) from an unported citation is claimed.
- **H2-FLUX / (h2)**, CA-II 69930–69938 and `8.1:eq-kernel-bounds-1`: existence, support, exact \(\ell^1\) normalization and flux identity for \(\varphi_P\), and \(\mathfrak g_{k_0}\ge c_d>0\), all assumed. There is no additional numbered flux theorem invoked in the displayed hypothesis; this local hypothesis is its precise label here.
- **H3-CONT / (h3)**, CA-II 69939–69955 and `8.1:eq-kernel-bounds-2`: the continuum tensor as displayed and, crucially, the quantitative **background** comparison \(\eta^{-8}k\ge\frac13\sum\langle FF\rangle^2\) beyond the stated depth and distance thresholds. This is assumed, not inferred from the algebra of the tensor. The source's `8.21:lem-continuum-kernel`, CA-II 145220–145222, explicitly says its statement and proof are not written out. We do not replace H3-CONT by that absent proof or by an outline result for the full free covariance.
- `8.1:eq-constants-ceiling-c`, CA-II 73250–73259: a choice of constants, including \(C_0^{\rm ker}(L)\) as a named kernel floor. Only that floor and \(k_W(L)\) from (h3) are used here; no correlation or running-normalisation conclusion is imported.
- `8.1:def-witness-class`, CA-II 68722–68795: definition and ensuing proved geometric assertions. The consumed assertions are rebuilt immediately below. Its parent `8.1:not-test-pairs-kernel`, CA-II 68376ff., fixes \(\vartheta\in(0,1]\), witness depth, and \(\rho=L^s\mathsf d\). The algebra below needs only the displayed class conditions; interpreting an arbitrary physical test pair as such a discrete witness pair remains subject to the source's mesh-admission condition (68788–68795), not an automatic consequence of its continuum mass.
- `8.1:lem-kernel-positivity` (c), proved in §3: nonnegative summands. Strict positivity from its (b) is not used for the background kernel.

**Witness definitions needed here.** In units of the level-\(k_0\) cells, the bare spacing is \(\eta=L^{-k_0}\), the support radius is \(\rho=L^s\mathsf d\), and
\[
\mathfrak n_K(f)=\eta^4\sum_{x\in\mathbb F}f(x).
\]
The subscript \(K\), omitted in the source, makes its cutoff dependence visible. The class \(\mathfrak F^+(\mathsf d,\vartheta)\) consists of nonzero nonnegative Lipschitz functions supported in a ball of radius \(\rho\) and satisfying
\[
\mathfrak n_K(f)\ge\vartheta\|f\|_\infty\rho^4,
\qquad \operatorname{Lip}_{k_0}f\le\|f\|_\infty/(\vartheta\rho).
\]
A witness pair has both members in this class and support distance between \(\rho\) and \(6\rho\). The correlation theorem mentioned in the definition is not used to prove this finite geometry.

**(filled) F7 — the precise mass bound and distance range from the witness definition.** The \(\eta\)-cubes centred at bare sites partition the torus up to their measure-zero boundaries. Each has volume \(\eta^4\), and its half-diagonal in four Euclidean dimensions is \(\eta\). The union of the cubes centred in a ball \(B(c,\rho)\) is contained in its \(\eta\)-neighbourhood, hence in \(B(c,\rho+\eta)\). A torus ball is the image of a Euclidean ball; projection can only reduce volume. The four-ball volume follows by slicing into two-dimensional discs: \(\int_0^r2\pi t\,\pi(r^2-t^2)\,dt=\pi^2r^4/2\). Therefore
\[
\mathfrak n_K(f)\le\tfrac{\pi^2}{2}(\rho+\eta)^4\|f\|_\infty
\le10\rho^4\|f\|_\infty\quad\text{if }\eta\le\rho/6.
\]
The numerical inequality is a hand inequality: \(\pi<22/7\) follows from
\[
0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx
=\int_0^1\left(x^6-4x^5+5x^4-4x^2+4-\frac4{1+x^2}\right)dx
=\frac{22}{7}-\pi.
\]
Thus \(\frac{\pi^2}{2}(7/6)^4<11858/1296<12960/1296=10\). This establishes exactly the source constant, without numerical evaluation.

For any support points \(x,y\), the lower bound \(\operatorname{dist}(x,y)\ge\rho\) is the pair definition. Compactness of the two supports gives points \(x',y'\) attaining their distance, at most \(6\rho\). Their respective support diameters are at most \(2\rho\). The triangle inequality gives \(\operatorname{dist}(x,y)\le2\rho+6\rho+2\rho=10\rho\). These are the only geometric facts from that definition used in (e).

**Exact source statement:**

```latex
\begin{lemma}[Upper and lower bounds and marginal scaling of the kernel]\label{8.1:lem-kernel-bounds}
Assume the following.
\begin{itemize}
\item[(h1)] The bounds on the kernel of the linear minimiser hold; they are used here as stated in
\cite[Theorem~1, (9)--(10)]{B-CMP102b}. The operator theorem at free current also holds.
\item[(h2)] The flux identity holds with its constant $C_d$. For every plaquette $P$ of the block lattice
of level $k_0$ there are weights $\varphi_P$ on the plaquettes of $\mathbb{F}$ such that
\begin{equation}\label{8.1:eq-kernel-bounds-1}
\sum_q \varphi_P(q)\,F_B(q)=(dB)(P),\qquad \|\varphi_P\|_1=\sum_q|\varphi_P(q)|=\eta^{-2}.
\end{equation}
Moreover $\varphi_P$ is supported on plaquettes $q$ with $|x_q-x_P|\le C_d$. Here $x_P$ is the point to
which $P$ is attached, and distances are measured in cells. The lower bound on the flux variance also
holds: the variance $\mathfrak{g}_{k_0}$ of $(dB)(P)$ satisfies $\mathfrak{g}_{k_0}\ge c_d$, with a
constant $c_d>0$.
\item[(h3)] The continuum kernel holds in the following form. Let $C_0^{\mathrm{ker}}(L)$ be the constant
of \eqref{8.1:eq-constants-ceiling-c}. For $x\ne0$ let the continuum curvature two-point function be
\begin{equation}\label{8.1:eq-kernel-bounds-2}
\begin{gathered}
\langle F_{\mu\nu}(x)F_{\rho\sigma}(0)\rangle
:=\frac{1}{\pi^2|x|^4}\bigl(I_{\mu\rho}I_{\nu\sigma}-I_{\mu\sigma}I_{\nu\rho}\bigr),\\
I_{\mu\nu}=\delta_{\mu\nu}-2\hat{x}_\mu\hat{x}_\nu,\quad \hat{x}=x/|x|.
\end{gathered}
\end{equation}
In this lemma and its proof only, $\hat{x}$ denotes the unit vector $x/|x|$. The premises of the
continuum kernel, in the form used here, are the bounds \eqref{8.1:eq-kernel-bounds-a} of item~(a) below
and the operator theorem at free current; its conclusion is that, for $K-s\ge k_W(L)$ and all points
$x,y$ with $|x-y|\ge C_0^{\mathrm{ker}}(L)$,
\begin{equation*}
\eta^{-8}\,k(x,y)\ge\frac13\sum_{\mu<\nu,\ \rho<\sigma}\langle F_{\mu\nu}(x-y)F_{\rho\sigma}(0)\rangle^2 .
\end{equation*}
\end{itemize}
Then the following hold.
\begin{itemize}
\item[(a)] There are constants $C_u$ and $\delta_{\square}>0$ such that, for all $i\ge0$ and all
plaquettes $p,q$ of $\mathbb{F}$,
\begin{equation}\label{8.1:eq-kernel-bounds-a}
\begin{gathered}
|C^{\mathrm{bg}}(p,q)|\le C_u\,\eta^4\,(1+|x_p-x_q|)^{-4},\\
|C^{\mathrm{step}}_i(p,q)|\le C_u\,\eta^4 L^{-4i}\,e^{-\delta_{\square}|x_p-x_q|L^{-i}}.
\end{gathered}
\end{equation}
\item[(b)] For every plaquette $P$ of the block lattice of level $k_0$,
\begin{equation*}
\max_{q\in\operatorname{supp}\varphi_P} C^{\mathrm{bg}}(q,q)\ge c_d\,\eta^4 .
\end{equation*}
\item[(c)] For every $f\in\mathfrak{F}^{+}(\mathsf{d},\vartheta)$ with $\rho\ge 2(C_d+2)/\vartheta$, and
at every $K$,
\begin{equation*}
\mathcal{K}_{K,s}(f,f)\ge \tfrac14\,\|f\|_\infty^2\,c_d^2\,\eta^8>0 .
\end{equation*}
\item[(d)] Put $c_*:=2/\pi^4$. For $K-s\ge k_W(L)$ and $|x-y|\ge C_0^{\mathrm{ker}}(L)$,
\begin{equation*}
k(x,y)\ge c_*\,\eta^8\,|x-y|^{-8}.
\end{equation*}
The continuum two-point function \eqref{8.1:eq-kernel-bounds-2} satisfies
\begin{equation}\label{8.1:eq-kernel-bounds-3}
\sum_{\mu<\nu,\ \rho<\sigma} \langle F_{\mu\nu}(x)F_{\rho\sigma}(0)\rangle^2=\frac{6}{\pi^4|x|^8}.
\end{equation}
Its components change sign, and $\langle F_{12}(x)F_{34}(0)\rangle=0$ for every $x\ne0$.
\item[(e)] Put $c_{\mathcal{K}}:=2\cdot10^{-8}/\pi^4$ and $C_{\mathcal{K}}:=36\,C_u^2$. Let
$(f_1,f_2)$ be a witness pair. The upper bounds below hold for every such pair. The lower bounds hold
when in addition $K-s\ge k_W(L)$ and $\rho\ge C_0^{\mathrm{ker}}(L)$; these are the conditions under
which (d) applies to the point pairs of a witness pair. The bounds are
\begin{equation}\label{8.1:eq-kernel-bounds-b}
\begin{gathered}
c_{\mathcal{K}}\,\rho^{-8}\,\mathfrak{n}(f_1)\,\mathfrak{n}(f_2)\le\mathcal{K}_{K,s}(f_1,f_2)
\le C_{\mathcal{K}}\,\rho^{-8}\,\mathfrak{n}(f_1)\,\mathfrak{n}(f_2),\\
c_{\mathcal{K}}\,\vartheta^2\,\|f_1\|_\infty\|f_2\|_\infty\le\mathcal{K}_{K,s}(f_1,f_2)
\le 100\,C_{\mathcal{K}}\,\|f_1\|_\infty\|f_2\|_\infty .
\end{gathered}
\end{equation}
\item[(f)] For fixed $s$ and every witness pair $(f_1,f_2)$, the bounds \eqref{8.1:eq-kernel-bounds-b}
hold with $\mathcal{K}_{K,s}(f_1,f_2)$ replaced by its lower limit and by its upper limit as
$K\to\infty$; the lower bounds there hold when $\rho\ge C_0^{\mathrm{ker}}(L)$.
\end{itemize}
\end{lemma}
```

**Proof, following CA-II 70002–70152.**

(a) By H-BG the map from \(B\) to \(F_B\) is the composite \(dH\) of the linear minimiser and coboundary. If \(S_B\) is the covariance of \(B\), finite expansion gives \(C^{\rm bg}=dH S_B H^*d^*\). Section 4 gives its orthogonal tower, and H-TOWER identifies the steps in the minimiser estimate. H1-MIN, in the operational form explicitly used by the source at 70011–70016, supplies
\[
|C^{\rm bg}(p,q)|\le C_u\eta^4(1+|x_p-x_q|)^{-4},\qquad
|C_i^{\rm step}(p,q)|\le C_u\eta^4L^{-4i}e^{-\delta_\square|x_p-x_q|L^{-i}}.
\]
The same \(C_u,\delta_\square\) and their stipulated uniformity are retained. This is an application of a named hypothesis, not a newly completed proof of the Balaban/operator estimates. No geometric-series argument is substituted for the source's route.

(b) The field \(F_B\) is centred by F4, as is the linear flux \((dB)(P)\). Square H2-FLUX's exact identity and take expectations, obtaining
\[
\mathfrak g_{k_0}=\sum_{q,q'}\varphi_P(q)\varphi_P(q')C^{\rm bg}(q,q').
\]
Write \(M_P=\max_{q\in\operatorname{supp}\varphi_P}C^{\rm bg}(q,q)\); the finite support is nonempty because its \(\ell^1\) norm is \(\eta^{-2}>0\). Cauchy–Schwarz gives
\( |\mathbb E F_B(q)F_B(q')|\le\sqrt{\mathbb EF_B(q)^2\mathbb EF_B(q')^2}\le M_P\)
on this support. **(filled) F11 — the covariance inequality, including zero variance.** That probabilistic inequality follows by expanding \(\mathbb E(U-tV)^2\ge0\) and minimizing in \(t\) when \(\mathbb EV^2>0\); if \(\mathbb EV^2=0\), then \(V=0\) almost surely and it holds as well. Taking absolute values term by term yields
\[
c_d\le\mathfrak g_{k_0}\le M_P\Bigl(\sum_q|\varphi_P(q)|\Bigr)^2=M_P\eta^{-4}.
\]
Multiply by \(\eta^4\) to obtain (b). No positivity of individual off-diagonal covariance entries is assumed.

(c) A Lipschitz function on the compact torus attains its maximum at some \(x_0\). Since \(f\ne0\) and \(f\ge0\), this maximum is positive, and the class Lipschitz bound gives
\[
f(x)\ge\|f\|_\infty-\frac{\|f\|_\infty}{\vartheta\rho}|x-x_0|
\ge\tfrac12\|f\|_\infty\quad (|x-x_0|\le\vartheta\rho/2).
\]
**(filled) F8 — finding a coarse attachment point.** Round each coordinate of a lift of \(x_0\) to the nearest coordinate of the unit-spaced coarse grid, allowing its fixed translate. The four coordinate errors are at most \(1/2\), so the Euclidean distance is at most \(\sqrt{4(1/2)^2}=1\). Projection to the torus does not increase it. Choose any positively oriented coarse plaquette \(P\) attached there. In particular \(|x_P-x_0|\le2\), the bound used in the source. Every \(q\in\operatorname{supp}\varphi_P\) has
\( |x_q-x_0|\le C_d+2\le\vartheta\rho/2\).
Part (b) supplies such a \(q\) with \(C^{\rm bg}(q,q)\ge c_d\eta^4\). Every summand in \(\mathcal K_{K,s}(f,f)\) is nonnegative, so retaining only the \((q,q)\) term gives
\[
\mathcal K_{K,s}(f,f)\ge f(x_q)^2 C^{\rm bg}(q,q)^2
\ge\tfrac14\|f\|_\infty^2c_d^2\eta^8>0.
\]
This is the printed finite-cutoff bound, with its factor \(\eta^8\); it is not a cutoff-independent floor.

(d) Put \(u=x/|x|\), \(I_{\mu\nu}=\delta_{\mu\nu}-2u_\mu u_\nu\), and
\(T_{\mu\nu\rho\sigma}=I_{\mu\rho}I_{\nu\sigma}-I_{\mu\sigma}I_{\nu\rho}\).
The matrix \(I\) is symmetric and
\[
(I^2)_{\mu\nu}=\delta_{\mu\nu}-4u_\mu u_\nu+4u_\mu\Bigl(\sum_\alpha u_\alpha^2\Bigr)u_\nu=\delta_{\mu\nu}.
\]
It follows that \(\sum_{\mu,\rho}I_{\mu\rho}^2=\operatorname{Tr}I^2=4\).

**(filled) F9 — contraction and ordered-index multiplicity.** In the expansion of \(\sum T^2\), the two square terms each sum to \((\sum_{\mu,\rho}I_{\mu\rho}^2)^2=16\). The mixed term before its coefficient \(-2\) is
\[
\sum_{\mu,\nu,\rho,\sigma}I_{\mu\rho}I_{\nu\sigma}I_{\mu\sigma}I_{\nu\rho}
=\sum_{\rho,\sigma}\Bigl(\sum_\mu I_{\mu\rho}I_{\mu\sigma}\Bigr)
\Bigl(\sum_\nu I_{\nu\sigma}I_{\nu\rho}\Bigr)
=\sum_{\rho,\sigma}\delta_{\rho\sigma}^2=4.
\]
This is the source's \(\operatorname{Tr}I^4\) contraction with all indices written out. Therefore the unrestricted sum is \(16+16-8=24\). Terms with equal indices in either pair vanish; every term with \(\mu<\nu,\rho<\sigma\) has four ordered versions, whose signs disappear on squaring. The restricted sum is \(24/4=6\), proving
\[
\sum_{\mu<\nu,\rho<\sigma}\langle F_{\mu\nu}(x)F_{\rho\sigma}(0)\rangle^2
=6/(\pi^4|x|^8).
\]
This calculation proves the norm identity for H3-CONT's displayed tensor, not its lattice approximation.

For the disjoint planes,
\(I_{13}I_{24}-I_{14}I_{23}=4u_1u_3u_2u_4-4u_1u_4u_2u_3=0\).
For an example of sign change,
\[
\pi^2|x|^4\langle F_{12}(x)F_{12}(0)\rangle
=(1-2u_1^2)(1-2u_2^2)-4u_1^2u_2^2=1-2u_1^2-2u_2^2.
\]
It is \(+1\) for \(u=e_3\) and \(-1\) for \(u=e_1\). Thus components can change sign although the summed square is positive; the assertion does not mean that the identically zero disjoint-plane component changes sign.

If \(K-s\ge k_W(L)\) and \(|x-y|\ge C_0^{\rm ker}(L)\), (a) and the retained free-current operator hypothesis permit H3-CONT's comparison. Multiplying that comparison by \(\eta^8\) and inserting the norm identity gives
\[
k(x,y)\ge\eta^8\frac13\frac6{\pi^4|x-y|^8}
=\frac2{\pi^4}\eta^8|x-y|^{-8}=c_*\eta^8|x-y|^{-8}.
\]
This retains both the factor \(1/3\) in the hypothesis and \(c_*=2/\pi^4\) in the conclusion.

(e) Regroup the finite plaquette sum by attachment points:
\[
\mathcal K_{K,s}(f_1,f_2)=\sum_{x,y}f_1(x)f_2(y)k(x,y).
\]
Only support points contribute, and F7 gives \(\rho\le|x-y|\le10\rho\). By (a), each of the \(6\cdot6=36\) squared covariance entries in \(k(x,y)\) is at most \(C_u^2\eta^8\rho^{-8}\). Thus
\[
\mathcal K_{K,s}(f_1,f_2)\le36C_u^2\eta^8\rho^{-8}
\Bigl(\sum_xf_1(x)\Bigr)\Bigl(\sum_yf_2(y)\Bigr)
=C_{\mathcal K}\rho^{-8}\mathfrak n_K(f_1)\mathfrak n_K(f_2).
\]
This upper bound needs no use of H3-CONT and no mesh-to-radius condition. The identity on the right uses exactly \(\eta^8=\eta^4\eta^4\), not an unrecorded integration normalization.

Under the additional depth and distance conditions of (d), every contributing pair satisfies its hypotheses. Since the exponent is negative, \(|x-y|\le10\rho\) implies \(|x-y|^{-8}\ge(10\rho)^{-8}\). Therefore
\[
\mathcal K_{K,s}(f_1,f_2)\ge c_*10^{-8}\eta^8\rho^{-8}
\Bigl(\sum_xf_1(x)\Bigr)\Bigl(\sum_yf_2(y)\Bigr)
=c_{\mathcal K}\rho^{-8}\mathfrak n_K(f_1)\mathfrak n_K(f_2),
\]
with exactly \(c_{\mathcal K}=2\cdot10^{-8}/\pi^4\).
The class lower mass bounds give
\(\rho^{-8}\mathfrak n_K(f_1)\mathfrak n_K(f_2)\ge\vartheta^2\|f_1\|_\infty\|f_2\|_\infty\),
so the second-line lower bound follows with no additional mesh condition.

**(correction) C1 — restore the omitted condition on the mass upper bound.** At CA-II 70138–70142 the proof says the witness definition gives \(\mathfrak n(f)\le10\rho^4\|f\|_\infty\) without qualification. The cited definition at 68762–68763 asserts it **only when \(\eta\le\rho/6\)**, and its proof at 68808–68818 uses that condition explicitly. The gap is real: with \(\rho=\eta/2\) a tent function on one bare site is a valid class member and pair with mass \(16\rho^4>10\rho^4\), and the printed route then gives only \(256C_{\mathcal K}\). It costs nothing downstream: the witness admission items (g) and (h) already force \(\eta\le\rho/6\). Thus this citation as an unconditional step is incorrect. The smallest repair on this route is to require \(\eta\le\rho/6\) for the **second-line upper bound in (e)** (or explicitly supply the two mass upper bounds). Under that condition, F7 gives
\[
\rho^{-8}\mathfrak n_K(f_1)\mathfrak n_K(f_2)
\le100\|f_1\|_\infty\|f_2\|_\infty,
\]
which proves the printed upper constant \(100C_{\mathcal K}\). Neither first-line mass bound nor the second-line lower bound is changed. This is a correction to the displayed implication's proof scope; it is not a claim of a counterexample to the unqualified upper estimate by a different argument. A later application may already impose enough room to ensure this condition, but that must be stated at that application. No such stronger room hypothesis is silently inserted into this lemma. All source constants and the source proof route are preserved.

With this correction, the second-line estimates have no explicit \(\rho\) or \(\mathsf d\) factor: the two masses contribute \(\rho^4\) each, cancelling \(\rho^{-8}\). This is the claimed marginal scaling, conditional on the recorded assumptions.

(f) Fix \(s\), the physical torus, the two Lipschitz functions, \(\mathsf d>0\), and their witness-pair membership for all sufficiently large \(K\). Then \(\rho=L^s\mathsf d\) is fixed and \(\eta=L^{s-K}\to0\). The inequality \(K-s\ge k_W(L)\) and the correction condition \(\eta\le\rho/6\) both hold eventually. For a direct proof of the latter convergence, \(L\ge3\) gives \(L^j\ge j+1\) by induction, so given any \(\epsilon>0\) one can choose an integer \(j>1/\epsilon\), and \(L^{-j}<\epsilon\). Thus no assertion about a computed cutoff is needed.

**(filled) F10 — liminf/limsup and the cutoff-dependent masses.** For fixed tests the first line's masses are not literally constant in \(K\). Their limiting values in cell units are
\[
\mathfrak n_\infty(f)=\int_{\mathbb T_m\text{ in cell units}} f(u)\,du
=L^{4s}\int_{\mathbb T_m\text{ in physical units}}f(u)\,du.
\]
On each \(\eta\)-cube centred at a bare site \(x\), \(|f(u)-f(x)|\le\operatorname{Lip}_{k_0}f\,\eta\). Integrating and summing the partition of the fixed torus gives
\[
|\mathfrak n_K(f)-\mathfrak n_\infty(f)|
\le\operatorname{Lip}_{k_0}f\,\eta\,\operatorname{vol}(\mathbb T_m\text{ in cell units})\longrightarrow0.
\]
Hence, writing \(A_K=\mathcal K_{K,s}(f_1,f_2)\), the precise first-line limiting statement is
\[
c_{\mathcal K}\rho^{-8}\mathfrak n_\infty(f_1)\mathfrak n_\infty(f_2)
\le\liminf_K A_K\le\limsup_K A_K
\le C_{\mathcal K}\rho^{-8}\mathfrak n_\infty(f_1)\mathfrak n_\infty(f_2),
\]
where the lower inequality still requires \(\rho\ge C_0^{\rm ker}(L)\). To justify passage, if \(a_K\le A_K\le b_K\) eventually and \(a_K\to a\), \(b_K\to b\), then for every \(\epsilon>0\) an entire sufficiently late tail lies in \([a-\epsilon,b+\epsilon]\); take its infimum and supremum, then let \(\epsilon\downarrow0\). The second-line bounds have fixed right and left sides already, so the same argument applies directly to both lower and upper limits, with the source constants and the same lower-bound threshold. No existence or uniqueness of a full kernel limit follows. This fills the suppressed limiting-mass interpretation of (f); it does not hold the discrete \(\mathfrak n_K\) artificially fixed.

## Result

This is a **port of the source proofs and conditional implications**, with one correction to a missing premise, not an audit or a proof of T0.

**Statements ported:** `8.1:lem-gaussian-squares`; `8.1:lem-free-curvature-covariance`; `8.1:lem-kernel-positivity` (a)–(d); and `8.1:lem-kernel-bounds` (a)–(f), retaining (h1)–(h3) and with C1 on the finite-cutoff sup-norm upper bound. The necessary supporting `8.1:lem-background-tower` decomposition is also ported, with its RG identification conditional. The exact four requested source statements are reproduced with their original labels and constants. Source-declared “proved in full” is distinguished from verification in this repository throughout.

**Every filled step:** F1, the fourth Gaussian pairing identity including degeneracy; F2, periodic summation by parts and full mixed-index cancellation in \(\Delta_1\); F3, the convolution index shift, signs and four Green values; F4, linear Gaussian conditioning with singular covariance and independent colour copies, together with the total-covariance decomposition; F5, uniqueness of the common plaquette of opposite bonds and its signs; F6, integrability, both cross-index orders and the terminal tower difference; F7, the exact witness mass threshold, hand bound for its constant and the \([\rho,10\rho]\) distance interval; F8, the coarse-grid nearest-site argument; F9, the continuum tensor's complete index contraction and factor four; F10, eventual thresholds, limiting masses and rigorous liminf/limsup passage; F11, the covariance Cauchy–Schwarz inequality including its zero-variance case. The intervening finite sum, nonnegativity and covariance expansions are written explicitly in their source order.

**Correction:** C1 restores \(\eta\le\rho/6\), the hypothesis actually attached to the cited witness mass bound, for (e)'s sup-norm upper estimate. The other bounds retain their printed hypotheses. The condition is automatic eventually in the fixed-\(s\) limit; no constant changes. No other correction to the requested algebraic statements was found in this reading.

**Named hypotheses still carried:** H-BG, the specified free potential/block/minimiser realization and its free-curvature identification; H-TOWER, its identification with Balaban's unit-coupling tower; H1-MIN, the cited linear-minimiser estimates and the free-current operator theorem on its admitted geometry and parameter domain, including their stated consequences (a) for the actual covariance kernels; H2-FLUX, the exact flux weights, localization, normalization and variance floor; H3-CONT, the quantitative continuum/background comparison with its depth and distance floors. C1 and the witness membership/shape assumptions are explicit restrictions, not analytic results proved here. In particular the tensor norm \(6/\pi^4\) does not discharge H3-CONT, and finite Gaussian conditioning does not discharge H-BG or H-TOWER.

**Recovery checkpoint:** the requested port is complete with these named antecedents and C1. The remaining proof obligations are the actual Balaban/minimiser/operator and continuum identifications just listed, and an independent reading of this port. The unqualified finite-cutoff sup-norm upper conclusion outside C1's domain has not been established by the printed route. Running normalisation, CA-II 70501–70584, was not ported; it remains downstream of the correlation theorem. P1 was not redone. No unrelated route was attempted, no numerical or computer-assisted proof was used, and no scientific status was granted.

Credit for the statements and proof routes belongs to **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, and to **Tadeusz Balaban** for the published inputs explicitly attributed above. This port was written by Codex and **is not yet checked by another model**.

## Change log (check, 2026-11-05)

Ported by Codex. Checked line by line by a fresh Claude session ([p3-free-gate](../../gates/p3-free-gate.md)): first failing step none; the five statement blocks are byte-identical to the source; F1–F11 hold; C1 is correct and needed. Applied by the lead (Claude): C1's line citations corrected and its counterexample and downstream cost recorded; the tower lemma cites F4 for \(M_0=F_B\).

Status: **checked port.** lem-gaussian-squares, lem-free-curvature-covariance, lem-kernel-positivity faithful; lem-background-tower faithful under H-TOWER; lem-kernel-bounds with repair C1, (a) assumed through H1-MIN, (d) and the (e) lower bounds on H3-CONT.

