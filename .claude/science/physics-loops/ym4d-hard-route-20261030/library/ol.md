# One-loop coefficient and finite part: CA-I Lemma 4.2

Provenance: Codex, research text at checkout 6a792352b901b4da73e40cbc393023af5c19d427, 2026-11-05; not an audit and grants no status. Sources: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, complete account and outline at 31a47c543775; Tadeusz Bałaban, CMP 109 and the account's quotation of CMP 116. All proof steps must be written and checkable by hand.

## 1. Target and source comparison

The target is the Gaussian lemma `4.2:lem-one-loop`, CA-I 3901–4029. It supplies hypothesis (b) of `4.19:prop-clause-zero`. It is not the bound on the non-Gaussian increment. This note ports the account's route: compose the constrained Gaussians, preserve their quadratic coefficient under background substitution, and compare with massive Wilson and ghost determinants.

The following is the exact lemma at CA-I 3901–3926. Its preceding definitions, CA-I 3764–3900, are retained below.

```latex
\begin{lemma}[{the one-loop coefficient and the finite part of the one-loop law;
\cite[(1.22), Theorem~3]{B-CMP109}, \cite[(2.41)]{B-CMP116}}]
\label{4.2:lem-one-loop}
With $F_{l-1}$, $\beta^0_l$ and $c_0$ as above, the following hold.
\begin{itemize}
\item[(a)] Let $l\ge1$. The localised family of the functional $B\mapsto F_{l-1}(U_l(e^{iB}))$
satisfies hypotheses (A) and (B) of the existence lemma for the coefficient of
Definition~\ref{4.2:def-increment} with $j=l$, read for
this family alone. In hypothesis (A) the terms of the family are analytic on polydiscs $P_a(X)$
and bounded there by $E^\natural e^{-\kappa d_l(X)}$; the bound $E^\natural$ and the decay rate
$\kappa$ depend only on $L$, $N$ and $\mathfrak{p}$. The analyticity radius $a=a_l>0$ depends in
addition on $l$, through the scale
factor of the potentials; in the norms of \cite[(1.13)]{B-CMP109} the radius is free of $l$. Only
$a_l>0$ is used.
\item[(b)] There is a constant $c_2\ge0$, depending only on $L$ and $N$, such that for every
$k\ge0$
\begin{equation}\label{4.2:eq-one-loop-2}
\Bigl|\sum_{l=1}^{k}\beta^0_l-k\,c_0\Bigr|\le c_2 .
\end{equation}
Consequently, for all $0\le i<n$, with $c_0$ as in \eqref{4.2:eq-one-loop-1},
\begin{equation}\label{4.2:eq-one-loop-3}
\sum_{l=i+1}^{n}\beta^0_l\ \ge\ (n-i)\,c_0-2c_2 .
\end{equation}
The bound \eqref{4.2:eq-one-loop-3} has the same form for every $N\ge2$.
\end{itemize}
\end{lemma}
```

Here `tr` is the normalized fundamental trace, `Tr = N tr`, and `tr(t_a t_b)=δ_ab`. Set
\[
F_{l-1}=\log Z^{(l-1)}-\log Z^{(l-1)}(1),\qquad
\beta_l^0=b[F_{l-1}\circ U_l],\qquad
b[F]=\sum_{u\in\mathbb Z^4}u_\mu u_\nu\Pi^F_{\mu\nu}(u)\quad(\mu\ne\nu).
\]
The last formula is CA-I 3826–3828 and CMP 109 (1.22), p. 264. The tensor is the whole-lattice Hessian formed with the free-boundary response, not a finite-torus coefficient. CA-I 3847–3865 makes this limit explicit. The Gaussian includes the constraint and gauge Jacobians of Balaban's step.

**Source status.** CA-I 3928–3945 cites the lemma and its two determinant comparisons by statement. It has an “Outline of (b)” at 3946, not a proof with a marked (*). CA-I 56361–56368, 56428–56430 and 56463–56467 nevertheless describe it as incomplete at a step. This is a source discrepancy. Neither description supplies the missing estimates. CMP 109 Theorem 3, p. 264, propagates the inductive assumptions. Its Theorem 2, pp. 259–260, defers the perturbative coupling calculation to another paper. CA-I 4201–4211 also records that distinction. CMP 116 is not local; only the account's quotations are used here.

All literal occurrences of `4.2:lem-one-loop` in the three pinned CA files were located. They are in CA-I only: 3603, 3876, 3903, 56363, 56428 and 56466. The passages read are 3580–3615, 3764–4030 and 56342–56495. The first introduces the joint induction; the second defines and states the coefficient; the last uses the interval lower bound. The later one-loop implication also consumes the absolute interval bound: CA-II 5.14, ported in `port/p6-correlation.md`, lines 4019–4033 and 4160–4188. That use must not be weakened to a lower bound.

| Closest text | Comparison with the target |
|---|---|
| `port/p3-free.md`, §§1–2 | Proves Gaussian-square contractions and the free curvature covariance. It has no background-dependent determinant or finite-part estimate. |
| `port/p5-induction.md`, A12 and P5-H-loop, lines 419–496 | Carries this very lemma as a cited/open input and records the status discrepancy. |
| `port/p6-correlation.md`, B4b and B-ONELOOP, lines 4019–4033, 4119–4300, 4412 | Deduces the running law conditional on the finite-part estimate. Its summation does not compute that input. |
| `sfol-draft.md`, §§3.3–3.7 | Gives a conditional bridge from a companion normalizer to the bulk Gaussian. It retains G-ID, TI, D7 and analytic-domain inputs. Its check of Theorem V says that the main uniform estimates were read, not re-derived. |
| `b-value.md`, Theorem V and §§3–6 | Claims the SU(2) bulk bound for the outline's R3 contour construction. It leaves localization/identification with RF8 separate. It is not yet a proof of (a) and (b) for the CA family. The uniform determinant estimate is examined below. |

The account chooses `c_0,c_2,c_5=2c_2` at Stage 2, after `L,N` and before `κ,κ_1,M_1,M` (CA-I 1416–1427). The localization constants in (a) may depend on the auxiliary tuple; the finite-part constant in (b) may not. Shrinking the final coupling ceiling cannot repair a depth-dependent finite-part estimate.

The required outline index was used first: README; chunks 04, 07, 19 and 20 with neighbouring rows; obligations at 3986–4004; CA index and ca-4.12-4.19 chunk 11. The source passages include SA 3986–4004, 20304–20390 and 21064–21462. The outline explicitly leaves the mixed energy estimates and matching of lattice numerators to be checked. Its stronger summable-increment demand is not part of this CA lemma.

## 2. The reference determinant: the finite calculation

This section computes the reference in CA-I 3967–3986. It does **not** identify it with the constrained normalizer. The bulk comparison is in §3; the remaining transfer is the question in §4. The magnetic-product route comes from Sussman and Alpoge, SA 21378–21452, and `b-value.md` §6. The calculation below fills in its resolvent algebra and treats every $N\ge2$.

Use the unit bare lattice and write $z=\eta^2\in(0,1]$. Put
\[
 \psi(q)=\sum_{\mu=1}^4(2-2\cos q_\mu),\qquad
 A=\psi+z,\qquad I_m(z)=\int_{[-\pi,\pi]^4}A^{-m}\frac{dq}{(2\pi)^4}.
\]
Choose $t=\sqrt{N/2}\operatorname{diag}(1,-1,0,\ldots,0)$. Then $t=t^*$, $\operatorname{tr}t=0$, and $\operatorname{tr}t^2=1$. Use a constant Abelian curvature $ft$ in the 12-plane. A fixed positive mass is kept during differentiation and the volume limit. Denote by $\widetilde\beta_N(z)$ the second $f$-derivative per unit volume of
\[
 -\tfrac12\log\det(K_f+z)+\log\det(\Delta_f+z),                 \tag{2.1}
\]
where $K_f$ is the Wilson Hessian in background Feynman gauge and $\Delta_f=D_f^*D_f$. Subtract the value at $f=0$.

### 2.1 Normalization and colour factors

The matrix units give the following completeness identity for a basis with $\operatorname{tr}(t_at_b)=\delta_{ab}$:
\[
 \sum_a(t_a)_{ij}(t_a)_{kl}=N\delta_{il}\delta_{jk}-\delta_{ij}\delta_{kl}.
\]
Indeed, the orthogonal projection onto traceless matrices for the unnormalized trace is $X\mapsto X-N^{-1}\operatorname{Tr}(X)1$; the basis here has squared norm $N$. Consequently
\[
 \sum_at_aXt_a=N\operatorname{Tr}(X)1-X,\qquad
 \sum_at_a^2=(N^2-1)1,
\]
\[
 \sum_a[t_a,[t_a,X]]
 =2(N^2-1)X-2\{N\operatorname{Tr}(X)1-X\}
 =2N^2X
\]
for traceless $X$. Thus $C_{\mathfrak g}=2N^2$.

Diagonalize $t$, with real eigenvalues $t_i$. The real two-plane spanned by the Hermitian and anti-Hermitian parts of $E_{ij}$, $i<j$, has charges $\pm\lambda_{ij}$, where $\lambda_{ij}=t_i-t_j$. All Cartan directions are neutral, and
\[
 \sum_{i<j}\lambda_{ij}^2
 =N\sum_it_i^2-\Big(\sum_it_i\Big)^2=N^2=C_{\mathfrak g}/2.     \tag{2.2}
\]
For $N=2$, $t=\operatorname{diag}(1,-1)$, so the only pair has charges $\pm2$. No trace-normalization factor is omitted.

### 2.2 What the Wilson stencil contributes

Here is a finite expansion that fixes which terms can be singular. For one oriented plaquette transport the four oriented link variations to its first corner; call them $Z_1,\ldots,Z_4$. An oppositely oriented link contributes the negative of its transported variation. With $P=e^{ift}$,
\[
 U_p(\epsilon)=e^{i\epsilon Z_1}e^{i\epsilon Z_2}
              e^{i\epsilon Z_3}e^{i\epsilon Z_4}P.
\]
Twice differentiating $1-\operatorname{Re}\operatorname{tr}U_p$ gives
\[
 \operatorname{tr}\{\cos(ft)Y^2+i\sin(ft)C\},\qquad Y=Z_1+Z_2+Z_3+Z_4,       \tag{2.3}
\]
\[
 C=[Z_1,Z_2]+[Z_1,Z_3]+[Z_1,Z_4]
   +[Z_2,Z_3]+[Z_2,Z_4]+[Z_3,Z_4].
\]
This follows by grouping the four diagonal terms and the six ordered cross terms into $Y^2+C$. Write $Z_i=Z_{i0}+fZ_{i1}+f^2Z_{i2}+O(f^3)$, $Y_r=\sum_iZ_{ir}$, and $C_r=\sum_{i<j}\sum_{a+b=r}[Z_{ia},Z_{jb}]$. The three coefficients of (2.3) are exactly
\[
\begin{array}{ll}
f^0:&\operatorname{tr}Y_0^2,\\
f^1:&\operatorname{tr}(Y_0Y_1+Y_1Y_0)+i\operatorname{tr}(tC_0),\\
f^2:&\operatorname{tr}(Y_1^2+Y_0Y_2+Y_2Y_0)
       -\tfrac12\operatorname{tr}(t^2Y_0^2)+i\operatorname{tr}(tC_1).
\end{array}                                                        \tag{2.4}
\]
All transports here have bounded length and bounded signed area on the unit plaquette. Adding the gauge form $D_fD_f^*$ uses only two endpoint differences. Thus, after removing straight endpoint transport, every coefficient is a finite trigonometric matrix, with bounded momentum derivatives. At zero flux the curl form plus the gauge form is $\psi I_4$. In each nonzero charge sector one can therefore write
\[
 K_\varphi(q)=\psi(q)I_4+\varphi S(q)+\varphi^2T(q)+O(\varphi^3),\qquad
 \varphi=\lambda f.                                             \tag{2.5}
\]
The $T$-term is retained below. Its particular bounded numerator cannot change the logarithm. There are finitely many colour sectors; constants here may depend on $N$. A zero-charge sector is treated directly in $f$, without division by $\lambda$.

The spin numerator at $q=0$ is fixed by an exact identity. The constant Abelian configuration is stationary: the two plaquettes adjacent to a bond have opposite orientations and equal sine. Gauge invariance therefore gives
\[
 K_fD_f=D_f\Delta_f.
\]
In midpoint coordinates the transport-removed gradient is $d_\mu(q)=2i\sin(q_\mu/2)$, with no explicit flux coefficient. With the magnetic product defined below, its first-order identity is
\[
 S(q)d(q)=i\{\psi,d\}(q).
\]
Since $d(q)=iq+O(|q|^3)$, its linear part reads
\[
 S(0)(iq)=(2q_2,-2q_1,0,0)^T,
\quad
 S(0)=\begin{pmatrix}0&-2i&0&0\\2i&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}.
\]
All four columns are determined by this identity. Squaring gives diagonal entries $4,4,0,0$; hence
\[
 \operatorname{Tr}_4S(q)^2=8+O(|q|).                            \tag{2.6}
\]
Here $\operatorname{Tr}_4$ is the trace over vector directions, not the colour trace.

The neutral sector is not discarded. Its odd term is zero, since the commutator trace against $t$ vanishes on the centralizer of $t$. Its even Wilson term in (2.4) is bounded. For SU(2) it is explicitly $-f^2d_{12}^*d_{12}/2$. Its contribution to (2.1)'s second derivative is
\[
 \tfrac12\int\frac{\widehat q_1^2+\widehat q_2^2}{\psi(q)+z}\frac{dq}{(2\pi)^4},
 \qquad \widehat q_\mu=2\sin(q_\mu/2),
\]
and is bounded. This corrects the neutral-colour sentence at SA 21388, as already observed in `b-value.md`; it is not a counterexample to the target lemma.

### 2.3 Every singular numerator in the magnetic expansion

For two transport-removed kernels the product has the triangle phase. Expanding that phase through degree two gives
\[
 a\star b=ab-\frac{i\varphi}{2}(a_1b_2-a_2b_1)
 -\frac{\varphi^2}{8}(a_{11}b_{22}-2a_{12}b_{12}+a_{22}b_{11})+O(\varphi^3).  \tag{2.7}
\]
For example, apply this to Fourier monomials $e^{ir\cdot q},e^{is\cdot q}$: the extra phase is the signed area $\varphi(r_1s_2-r_2s_1)/2$. Linearity gives (2.7); absolutely summable displacement moments justify its use for massive inverse kernels. Momentum integration of a traced first bracket is zero by two integrations by parts; the trace integral is cyclic.

Solve the right inverse equation for $K_\varphi+z+s$, $s\ge0$. Put $a=A+s$. Degree zero and one give
\[
 R_0=a^{-1}I,\qquad R_1=-S/a^2.
\]
The degree-two equation is
\[
 R_2a+R_1S+R_0T
 -\tfrac i2\bigl(\{R_1,a\}+\{R_0,S\}\bigr)
 -\tfrac18\{\!\{R_0,a\}\!\}=0.
\]
The first-bracket terms cancel exactly:
\[
 \{-S/a^2,a\}=-\{S,a\}/a^2,\qquad
 \{a^{-1},S\}=-\{a,S\}/a^2.
\]
The remaining scalar derivatives are
\[
 \psi_i=2\sin q_i,\quad \psi_{ii}=2\cos q_i,\quad \psi_{12}=0,
\]
\[
 P=8\cos q_1\cos q_2,\qquad
 \widetilde P=8(\sin^2q_1\cos q_2+\sin^2q_2\cos q_1),
\]
so
\[
 R_2=\frac{S^2}{a^3}-\frac{T}{a^2}
      -\frac{P I}{8a^3}+\frac{\widetilde P I}{4a^4}.             \tag{2.8}
\]
The resolvent formula for the logarithm integrates $-R_2$ over $s\ge0$. The integrals of $a^{-2},a^{-3},a^{-4}$ are $A^{-1},(2A^2)^{-1},(3A^3)^{-1}$. Thus the coefficient of $\varphi^2$ in the vector logarithm is
\[
 v(z)=\int\left\{\frac{\operatorname{Tr}_4T}{A}
 -\frac{\operatorname{Tr}_4S^2}{2A^2}
 +4\left(\frac{P}{16A^2}-\frac{\widetilde P}{12A^3}\right)\right\}\frac{dq}{(2\pi)^4}. \tag{2.9}
\]
The scalar logarithm has $S=T=0$ and vector multiplicity one. Its coefficient is $u(z)$. There are no other terms of degree two.

Integrate the two periodic total derivatives
\[
 \partial_1\frac{\sin q_1\cos q_2}{A^2},\qquad
 \partial_2\frac{\sin q_2\cos q_1}{A^2}.
\]
Each integral is zero. They give, respectively,
\[
 \int\frac{\sin^2q_1\cos q_2}{A^3}
 =\tfrac14\int\frac{\cos q_1\cos q_2}{A^2},\quad
 \int\frac{\sin^2q_2\cos q_1}{A^3}
 =\tfrac14\int\frac{\cos q_1\cos q_2}{A^2}.
\]
Therefore the scalar orbital term and vector term are
\[
 u=\left(\tfrac12-\tfrac23\cdot\tfrac12\right)
       \int\frac{\cos q_1\cos q_2}{A^2}\frac{dq}{(2\pi)^4}
   =\tfrac16I_2+r_u,
\]
\[
 v=4u-4I_2+r_v=-\tfrac{10}{3}I_2+4r_u+r_v,                 \tag{2.10}
\]
where, without dropping any term,
\[
 r_u=\tfrac16\int\frac{\cos q_1\cos q_2-1}{A^2}\frac{dq}{(2\pi)^4},\quad
 r_v=\int\left\{\frac{\operatorname{Tr}_4T}{A}
 -\frac{\operatorname{Tr}_4S^2-8}{2A^2}\right\}\frac{dq}{(2\pi)^4}.             \tag{2.11}
\]

A real charged pair contributes $2\lambda^2 f^2u$ to the ghost logarithm and $2\lambda^2 f^2v$ to the vector logarithm. Equation (2.1) and two $f$-derivatives therefore give $2\lambda^2(2u-v)$. Summing (2.2), the full answer is
\[
 \widetilde\beta_N(z)=C_{\mathfrak g}\,\frac{11}{3}I_2(z)+r_N(z).            \tag{2.12}
\]
In detail the coefficients of $I_2$ are

| Contribution to the second $f$-derivative | Coefficient |
|---|---:|
| Vector spin, from $-\operatorname{Tr}_4S^2/(2A^2)$ and $-1/2\log\det$ | $4C_{\mathfrak g}$ |
| Four vector orbital directions | $-\tfrac23 C_{\mathfrak g}$ |
| Ghost determinant | $+\tfrac13 C_{\mathfrak g}$ |
| Sum | $\tfrac{11}{3}C_{\mathfrak g}$ |

The remainder is the sum over charged sectors of their terms (2.11), with the same determinant and charge factors, plus the neutral terms from (2.4). This is a finite sum, not an omitted diagram class.

### 2.4 Finite remainder and mass derivatives

For $|q_i|\le\pi$, $4q_i^2/\pi^2\le4\sin^2(q_i/2)\le q_i^2$. Thus
\[
 c|q|^2+z\le A\le |q|^2+z,\qquad c=4/\pi^2.
\]
The absolute numerators in (2.11) are bounded by $C_N|q|^2$, $C_N$ and $C_N|q|$, respectively. The needed radial integrals are bounded by constant multiples of
\[
 \int_0^{2\pi}\frac{r^5}{(cr^2+z)^2}dr,\quad
 \int_0^{2\pi}\frac{r^3}{cr^2+z}dr,\quad
 \int_0^{2\pi}\frac{r^4}{(cr^2+z)^2}dr.
\]
Replacing the denominators by $cr^2$ or $c^2r^4$ bounds them by integrals of $r$, $r$, and $1$. All are finite, uniformly in $z>0$. For every mass-independent numerator $h$,
\[
 z\partial_z(hA^{-m})=-m(z/A)hA^{-m},\quad
 z^2\partial_z^2(hA^{-m})=m(m+1)(z/A)^2hA^{-m}.
\]
Since $z/A\le1$, the same bounds apply to both scaled derivatives. Hence
\[
 |r_N(z)|+|zr_N'(z)|+|z^2r_N''(z)|\le C_N.                  \tag{2.13}
\]

Choose a fixed ball $0<|q|<\delta<1$. Taylor's formula gives $|\psi(q)-|q|^2|\le C|q|^4$. The difference of the two squared resolvents is at most
\[
 C|q|^4(c|q|^2+z)^{-3}.
\]
Its radial integral is bounded by $C\int_0^\delta r\,dr$. Outside the ball $A$ has a positive lower bound independent of $z$. The remaining radial integral is exactly
\[
 \frac{1}{8\pi^2}\int_0^\delta\frac{r^3}{(r^2+z)^2}dr
 =\frac1{16\pi^2}\left\{\log\frac{\delta^2+z}{z}
             +\frac z{\delta^2+z}-1\right\}.
\]
It follows that
\[
 I_2(z)=\frac1{16\pi^2}\log(1/z)+O(1).
\]
Also $I_2'=-2I_3$, $I_2''=6I_4$. Substitution $r=\sqrt{z/c}\,t$ in the radial bounds gives $I_3\le C/z$, $I_4\le C/z^2$: the remaining integrals are
\[
 \int_0^\infty\frac{t^3}{(1+t^2)^3}\,dt=\frac14,\qquad
 \int_0^\infty\frac{t^3}{(1+t^2)^4}\,dt=\frac1{12}.
\]
Both evaluations follow by $u=t^2$ and integrating the two powers in $u=(1+u)-1$. Therefore
\[
 \left|\widetilde\beta_N(z)-\frac{11C_{\mathfrak g}}{48\pi^2}\log(1/z)\right|
 +|z\widetilde\beta_N'(z)|+|z^2\widetilde\beta_N''(z)|\le C_N.              \tag{2.14}
\]
At $z=\eta^2$ the separate gluon and ghost coefficients per $\log(1/\eta)$ are
\[
 \frac{(10/3)C_{\mathfrak g}\,2}{16\pi^2}
   =\frac{5C_{\mathfrak g}}{12\pi^2},\qquad
 \frac{(1/3)C_{\mathfrak g}\,2}{16\pi^2}
   =\frac{C_{\mathfrak g}}{24\pi^2}.
\]
Their sum is the account's $11C_{\mathfrak g}/(24\pi^2)$.

**Limits used here.** At fixed $z>0$, finite Dirichlet compressions are positive for sufficiently small real flux: the covariant curl/gauge principal form is positive, and the spin perturbation is bounded by $C_N|f|$. Choose $|f|<c_Nz$ before differentiating. Conjugation by $e^{h\cdot x}$ changes a finite-range unit-lattice operator by at most $C_N|h|$. For $|h|<c_Nz$, its resolvent is inverted by a Neumann series after conjugation. Its kernel therefore decays exponentially. Flux derivatives insert at most polynomial factors in relative positions. Centre the gauge at the trace point; those polynomials are summable against this decay. Boundary contributions occupy a boundary layer with summable distance tails, so divided by volume they vanish. This proves existence of the differentiated trace density and justifies (2.7)–(2.9), first at fixed $z$, then as $z\downarrow0$. No uniform positive-flux disc as $z\downarrow0$ is asserted. No zero eigenvalue was silently deleted.

For an exponentially summable, gauge-invariant Hessian, this magnetic derivative is its coefficient $b$. Indeed the zero and first moments vanish by gauge invariance and reflections. For the affine potential $B_2(x)=fx_1t$, rewriting the quadratic form in differences gives density
\[
 -\frac{f^2}{4}\sum_u u_1^2\Pi_{22}(u)=\frac{b f^2}{2}.
\]
The last equality is the transverse quadratic Taylor identity
$\widehat\Pi_{22}(p)=b p_1^2+\cdots$. Exponential moments justify the polynomial substitution. Thus (2.14) proves the *reference* bound with $C_{\mathrm{det}}(N)$; it does not yet prove the first comparison bound at CA-I 3975.

## 3. The bulk finite part, and precisely what it would supply

This is the bulk version of `b-value.md` Theorem V, written in the account's normalization. Its construction uses the actual near-identity mean of CMP 109 (0.10)–(0.12), which is also the outline's R3. The off-small-field extension of the average is irrelevant to its jets at the identity. The coefficient is taken after the volume limit at each fixed $k$. This section does not construct the account's local families.

### 3.1 Gaussian composition and the coefficient

For a real symmetric matrix $T$, a surjection $A:\mathbb R^n\to\mathbb R^m$, and $T>0$ on $\ker A$, define
\[
 G(T,A)=\int e^{-\langle a,Ta\rangle/2}\delta(Aa)\,da.
\]
Choose orthonormal coordinates $a=(u,v)$ with $u\in\ker A$, $Av=A_1v$. Direct integration gives
\[
 G(T,A)=(2\pi)^{(n-m)/2}\det(T_{uu})^{-1/2}|\det A_1|^{-1}.
\]
Eliminating the $u$-block in the saddle matrix gives
\[
 \left|\det\begin{pmatrix}T&A^*\\A&0\end{pmatrix}\right|
 =\det T_{uu}\,(\det A_1)^2.                                \tag{3.1}
\]
This keeps the coarea factor. Gaussian integration in two successive kernel/complement splittings is the same integral. With the constrained Lagrangian Hessian used at each stationary point, it proves
\[
 \Psi_k=\Phi_k+\Psi_{k-1}\circ p_k,\qquad \Phi_l=F_{l-1}\circ U_l,
 \quad\Psi_0=0.                                              \tag{3.2}
\]
For a constraint $M(a)=Aa+C^{(2)}(a)+O(a^3)$, this Hessian includes $-\langle\mu,D^2M\rangle$. It cannot be replaced by the restriction of the unconstrained action Hessian. Equation (3.2) is the finite-dimensional identity used at SA 21072–21078 and CA-I 3948–3957. `prefactor-loc.md` §§2–4 proves the fixed-depth inverse and the response identities for this same near-identity mean.

For clarity, the coefficient preservation argument needs only fixed-depth estimates. Linearizing (0.12) gives the plain straight-path average plus a coarse gradient. The plain average sends a constant one-form to $L$ times that form and an affine form's curl to $L^2$ times its curl. The stationary response therefore sends affine curls to $L^{-2}$ times their value, up to a fine gradient. This follows by inserting that affine field into the flat saddle equation: its curl is constant, its current is zero, and its contour-gauge representative is obtained by solving site differences from the coarsest nodes down. The fixed-depth saddle inverse gives uniqueness.

Let $\Pi$ have exponential moments and annihilate gradients. In midpoint coordinates its quadratic symbol is $b(|p|^2I-pp^*)$. For a response through one block, the zero alias contributes two factors $L^{-1}$ and $L^4$ fine sites. Hence it contributes $L^2\widehat\Pi(p/L)$. Every nonzero alias of the constant response is a gradient. Affine-curl reproduction makes its curl $O(|p|^2)$, so, modulo a gradient, that alias is $O(|p|^2)$. Both gradient legs vanish against $\Pi$, and its contribution is $O(|p|^4)$. There are finitely many aliases at this fixed step. Thus
\[
 b[H\circ p_k]=b[H],\qquad B_k:=b[\Psi_k]=\sum_{l=1}^k b[\Phi_l].          \tag{3.3}
\]
No depth-uniform estimate is inferred from this identity. This is the route of `prefactor-loc.md` Theorem S and Corollary T, and CA-I 3958–3965.

### 3.2 A massive comparison on constant-curvature jets

Set $\eta=L^{-k}$ and use level-$k$ length units. The fine plaquette flux is $f\eta^2t$. Symmetric contour means of this Abelian field are its straight integrals: pairing coordinate orders cancels their signed areas. The remaining area in (0.12) is linear in the displacement from the block centre and averages to zero. Thus blocking reproduces constant curvature. The Wilson current and the constraint multiplier vanish. The physical branch has these jets: at fixed $k$, their polynomially growing gauge representative solves the differentiated saddle equations, whose inverse decays exponentially. This also explains why no constant-flux periodic configuration is assumed.

Write $D=D_f$, $\Delta=D^*D$, and $K=\Delta^{\rm W}+DD^*$. One may straighten the linear constraint by a coarse gauge displacement:
\[
 Q=Q^{\rm orig}+D_c\Phi,\qquad QD=D_cR.
\]
Here $\Phi$ is the block mean of the infinitesimal contour transports, and $R$ is the corresponding transported site mean. This follows by differentiating a gauge transformation along each contour: its two endpoint terms are the node value and the transported endpoint value. The intermediate terms cancel. At zero curvature, $Q$ is the plain straight-segment mean. Iteration gives
\[
 (R\lambda)(y)=\eta^4\sum_{x\in B^k(y)}T_{yx}\lambda(x),\qquad RR^*=1.    \tag{3.4}
\]
The second identity uses disjoint blocks and $T_{yx}T_{yx}^*=1$, with the volume-weighted adjoint. For complex jets use the analytic bilinear transpose, not a conjugate-analytic adjoint.

The finite Gaussian gauge change retains its determinant. Introduce a coarse site displacement $\nu$ and the constraint $Q^{\rm orig}a-D_c\nu=0$. The shear $\nu'=\nu+\Phi a$ has determinant one. The residual gauge parameter lies in $\ker R$. Using $PD^*a$, $P=1-R^*R$, as its gauge condition gives the Faddeev–Popov determinant $\det(\Delta|_{\ker R})$. This is a change of coordinates on a finite Gaussian integral, not a deletion of longitudinal modes. In the original contour gauge the gauge coordinates are triangular by level; their Gaussian normalization is independent of the datum. Equation (3.1) now yields the four determinant terms
\[
 \Psi_k=-\tfrac12\tau\log\Xi-\tfrac12\tau\log(Q\Xi^{-1}Q^*)
             +\tau\log M+\tau\log(RM^{-1}R^*),              \tag{3.5}
\]
\[
 \Xi=K+E,\quad E=Q^*Q-DR^*RD^*,\qquad M=\Delta+R^*R.
\]
Here and below $\tau$ is the trace density per coarse cell, and every term is vacuum-subtracted. To obtain (3.5), add $Q^*Q$ to the upper-left saddle block by a constraint-row operation, then take its Schur complement. Do the same with $R$ for the site saddle. Equation (3.4) fixes its coarea determinant. This is the stationary-field specialization of the source's saddle route; there are no current terms on this field.

The following bounds concern these homogeneous magnetic jets only. They do not concern independent currents on the hereditary domains of part (a).

**Averages.** At a scale $s_i=L^{i-k}$, all contours for a one-step row lie in a double block of diameter $C_Ls_i$. In a gauge centred there, their transport-removed coefficients are analytic in $fs_i^2$. The derivative of the defining group-mean equation with respect to its mean is minus the number of contours at the identity; dividing by that number gives an invertible derivative. The analytic implicit-function argument therefore has a fixed one-step disc, depending on $(L,N)$.

At $f=0$, physical one-form normalization gives weight $L^{-5}$ to each block-site/segment-link pair. There are $L^5$ such pairs in a row and $L$ occurrences of each fine link. With the cell-volume ratio $L^4$, the row and weighted column sums are both one. Analyticity bounds their deviations by $C_{L,N}|f|s_i^2$. On iteration, the product of these bounds is at most
\[
 \prod_i(1+C_{L,N}|f|s_i^2)
 \le\exp\{C_{L,N}|f|/(1-L^{-2})\}.
\]
Removing endpoint transports in a product also gives triangle phases. Their areas are at most $C_L(\sum_i s_i)^2$, bounded because $\sum_i s_i\le(1-L^{-1})^{-1}$. Momentum derivatives multiply coefficients by these bounded physical displacements. Cauchy's formula on a smaller flux disc and the row/column bound give
\[
 \|\partial_p^\alpha\partial_f^jQ\|+
 \|\partial_p^\alpha\partial_f^jR\|\le C_{L,N,\alpha,j},\quad j\le2.       \tag{3.6}
\]
This is a statement about transport-removed jets. It does not assert a bounded operator in a nonzero complex magnetic field on the infinite lattice.

**The flat gap.** On a Bloch fibre, put $q=p+2\pi n$, $p\in[-\pi,\pi]^4$, retaining only aliases in the fine Brillouin zone. The actual zero-flux means have symbols
\[
 a_\eta(t)=\frac{\eta\sin(t/2)}{\sin(\eta t/2)},\quad
 R(q)=\prod_\nu a_\eta(q_\nu),\quad
 Q_{\mu\mu}(q)=a_\eta(q_\mu)\prod_\nu a_\eta(q_\nu).           \tag{3.7}
\]
Each formula follows by summing a centred finite geometric series; the segment sum supplies the extra directional factor. Products over consecutive scales telescope to (3.7). For the zero alias every ratio is at least $2/\pi$ in modulus. Nonzero aliases have $|q|\ge\pi$. Since $Q,R$ are contractions, solving for the zero alias and estimating the remaining aliases by their gradient energy gives
\[
 \|a\|\le C(\|\partial a\|+\|Qa\|),\qquad
 \Delta+R^*R\asymp\Delta+1.                                  \tag{3.8}
\]
One must also check the divergence removed in $\Xi$. For $p\ne0$, write
\[
 a=t+D\Delta^{-1}(v+R^*g),\quad D^*t=0,\quad
 v=PD^*a,\quad g=RD^*a,\quad m=R\Delta^{-1}R^*.
\]
The zero alias and (3.4) give $m\asymp |p|^{-2}$ and
$R\Delta^{-2}R^*\le C|p|^{-4}$. Hence
$\|m^{-1}R\Delta^{-1}\|\le C$. Applying $Q$ and using $QD=D_cR$ yields
\[
 |g|\le C\{|p|\|Qa\|+|p|\|Qt\|+\|v\|\}
 \le C(\|Qa\|+\|da\|+\|v\|).
\]
For the last inequality, $|p|\|t\|\le C\|dt\|=C\|da\|$. At $p=0$, $R$ kills all nonzero aliases and the divergence has no zero-alias component, so $g=0$. Using
$\|\partial a\|^2=\|da\|^2+\|D^*a\|^2$ and (3.8) proves
\[
 cW^2\le\Xi_0\le CW^2,\qquad W=(K_0+1)^{1/2},                \tag{3.9}
\]
with constants depending only on $(L,N)$.

**Mixed bounds.** Interpolate $H_s=K+1+s(E-1)$, $0\le s\le1$. At zero flux (3.9) holds throughout by convexity. A momentum derivative of the fine gradient
$2i\eta^{-1}\sin(\eta q_\mu/2)$ is bounded; the undifferentiated gradient is bounded after multiplication by $W^{-1}$. The transport-removed first and second flux coefficients of the Wilson stencil are $O(1)$ and $O(\eta^2)$: each flux differentiation brings a plaquette area $\eta^2$, and the precision has factor $\eta^{-2}$. Applying (3.6) to each of the four factors in $DR^*RD^*$, and to the two factors in $Q^*Q$, therefore proves
\[
 \|W^{-1}(\partial_p^\alpha\partial_f^jH_s)_0W^{-1}\|
 \le C_{L,N,\alpha,j}\quad(j\le2).                           \tag{3.10}
\]
Magnetic products add at most four momentum derivatives at flux degree two. Differentiate the inverse equation using (2.7). Each term has outer factors $W^{-1}$ and middle factors bounded by (3.9)–(3.10). Thus every needed inverse jet is $W^{-1}BW^{-1}$ with $\|B\|\le C$. The same proof applies to the site interpolation. The two coarse covariances in (3.5) have upper bounds from (3.6)–(3.9). For their lower bounds, lift a coarse vector through its invertible zero-alias symbol in (3.7); that lift has bounded energy. Cauchy–Schwarz in the precision inner product bounds its inverse energy from below. Their logarithmic jets are consequently bounded in fixed dimension.

**Trace remainder.** Set $G=(K+1)^{-1}$, $B=E-1$. Twice applying the resolvent identity and integrating in $s$ gives the exact finite-matrix formula
\[
 \tau\log\Xi=\tau\log(K+1)+\tau(GB)-\tfrac12\tau(GBGB)
       +\int_0^1s^2\tau(GBGBH_s^{-1}B)\,ds.                 \tag{3.11}
\]
Every occurrence of $E$, including its finitely many jets, factors through a fixed number of coarse bond or site components. After moving the energy weights cyclically, (3.6)–(3.10) give a bounded trace of bounded rank. These terms are uniformly bounded.

The terms with no $E$ in the last integral have three inverse factors. For their jets,
\[
 \|W^{-1}BW^{-1}\|_{\mathfrak S^3}
 \le\|B\|\Big(\sum_n(1+c|p+2\pi n|^2)^{-3}\Big)^{1/3}\le C.             \tag{3.12}
\]
The last sum is bounded independently of the number of aliases: its shell of radius $m$ has at most $C(m+1)^3$ points, and the tail is bounded by $C\sum m^{-3}$. Hölder's trace inequality bounds a product of three such factors. The finitely many magnetic-product terms have the same bounds. Thus, through second flux order,
\[
 \tau\log\Xi=\tau\log(K+1)-\tau G-\tfrac12\tau G^2+O_{f^2}(1).
\]
The site determinant has the same expansion. The coarse determinants in (3.5) contribute $O_{f^2}(1)$. Rescaling to bare units cancels the cell-volume factor $\eta^{-4}$ with the squared flux factor $\eta^4$. Therefore
\[
 B_k=\widetilde\beta_N(\eta^2)
       -\eta^2\widetilde\beta_N'(\eta^2)
       +\tfrac12\eta^4\widetilde\beta_N''(\eta^2)+e_k,
 \qquad |e_k|\le C_E(L,N).                                  \tag{3.13}
\]
These are derivatives of the genuine finite-volume Gaussians, followed by the fixed-depth volume limit. At fixed depth their inverse kernels decay; centred gauge differentiation introduces only polynomial moments. The same inverse recursion then identifies their limits with the magnetic jets above. Neither (3.12) nor (3.13) is a numerical estimate.

Define the finite constants
\[
 C_R(N)=\sup_{0<z\le1}\left|\widetilde\beta_N(z)
            -\frac{11C_{\mathfrak g}}{48\pi^2}\log(1/z)\right|,
 \qquad
 C_M(N)=\sup_{0<z\le1}\left(z|\widetilde\beta_N'(z)|
                       +\tfrac12z^2|\widetilde\beta_N''(z)|\right).
\]
Their finiteness is (2.14). Combining it with (3.13) gives the bulk bound
\[
 |B_k-kc_0|\le C_E(L,N)+C_R(N)+C_M(N)=:c_2^{\rm bulk}(L,N).                \tag{3.14}
\]
Choose the flux disc first, then the constants in (3.6)–(3.12), then $C_E,C_R,C_M$. They read only $(L,N)$, so (3.14) has the required Stage-2 order. Also
\[
 |B_k-B_k^{\rm ref}|\le C_E+C_M,
\]
which is the account's first comparison with $C_{\rm cmp}=2(C_E+C_M)$, for this **bulk** construction. Take $B_0=0$ separately; enlarging $c_2^{\rm bulk}$ if necessary covers $k=0$.

### 3.3 Transfer to the account, conditional on localization

Suppose the account's actual Gaussian family has its asserted analytic bound, common lifts, total identity and reflection covariance. At a fixed $l$, Cauchy's formula bounds its pointed Hessian by
\[
 C_l e^{-\kappa d_l(X)}e^{-\delta_0(\operatorname{dist}(x,X)+\operatorname{dist}(y,X))}.
\]
The constant may depend on $l$; this transfer uses no uniformity in $l$. Summing half the domain decay pays the domain entropy. Its other half bounds distances from $x,y$ to the base point. This is precisely the argument of CA-I 58853–58904, with
$\delta'=\frac14\min\{\delta_0,\kappa/M\}$. A wrapping domain has $d_l(X)>\varsigma/(4M)-2$, so its sum tends to zero. On each fixed non-wrapping domain the local forms agree and the response converges. Dominated convergence then identifies the local-family Hessian with the bulk Hessian; the exponential majorant also permits its second moment. This is the fixed-depth transfer of `sfol-draft.md` Lemma 3.5, on the account's domain geometry.

It follows, **under those family hypotheses**, that
\[
 \beta_l^0=b[\Phi_l]=B_l-B_{l-1}.
\]
Equation (3.14) then proves (b), with $c_2=c_2^{\rm bulk}$, and subtraction gives the stronger consumer bound
\[
 \left|\sum_{l=i+1}^n\beta_l^0-(n-i)c_0\right|\le2c_2.       \tag{3.15}
\]
The lower inequality used in clause (0) follows. No sign of an individual increment follows. All bare couplings disappear before (3.1); the total Gaussian coefficients therefore read neither $g_0,\ldots,g_{l-1}$, $K$, nor the torus. Localization parameters may affect the representation but not its coefficient once the transfer is proved.

## 4. Three new attacks on the remaining local realization

Part (a) is stronger than analyticity of each finite Gaussian. Its family has prescribed local ingredients, exact common lifts, and a depth-free domain in the norms of CMP 109 (1.13). The bulk calculation in §3 cannot be relabelled as a proof of those facts. The source's unnamed “existence lemma” with hypotheses (A),(B) is not printed under those names elsewhere in the pinned CA files. The explicit nearby supplier is `4.38:prf-polarisation-limit`, CA-I 58732–58989, whose analytic-family bounds are **hypotheses**. Its proof was read above; it proves the transfer once those bounds are supplied.

The local CMP 99b Theorem 3.10 (pp. 415–416) and Theorem 3.12 (p. 423) were also checked. The latter extends walk bounds under its stated background hypotheses, (3.35)–(3.36); it does not verify those hypotheses for every independent-current family used here. The damaged estimate in the local OCR is not used as a proved bound. The three attacks below concern the actual local Gaussian family, not the already ported flow arithmetic. Each keeps the unsuccessful construction explicit.

### Attack 1: localize the global logarithm before taking the volume limit

Let $A_0$ be the flat precision and $\delta A$ its variation. On a fixed finite torus, when $\|A_0^{-1/2}\delta A A_0^{-1/2}\|<1$, the exact normalized logarithm is
\[
 \log\det(A_0+\delta A)-\log\det A_0
 =\sum_{r\ge1}\frac{(-1)^{r+1}}r
        \operatorname{Tr}(A_0^{-1}\delta A)^r.                \tag{4.1}
\]
Expanding the trace into bond indices gives local-looking cyclic terms. At every fixed depth, the flat inverse has exponential decay; hence (4.1) can be differentiated and grouped absolutely on a sufficiently small ball. The gauge and coarea logarithms can be expanded in the same way. This directly supplies a fixed-depth analytic total.

It does **not** give the required exact common lifts if a term is labelled only by the sites of its $\delta A$ insertions. Here is an exact hand check. On the one-dimensional lattice let
\[
 A=(2+a)I-S-S^*,\quad a>0,\quad
 r=\frac{2+a-\sqrt{a(a+4)}}2\in(0,1).
\]
The recurrence $r+r^{-1}=2+a$ and the equation at zero give
\[
 A^{-1}_\infty(n)=\frac{r^{|n|}}{\sqrt{a(a+4)}}.
\]
Periodizing on a torus of length $T$ gives
\[
 A_T^{-1}(0,0)=\frac1{\sqrt{a(a+4)}}\left(1+2\sum_{m\ge1}r^{mT}\right)
 =\frac{1+r^T}{(1-r^T)\sqrt{a(a+4)}}>A_\infty^{-1}(0,0).      \tag{4.2}
\]
The coefficient of a perturbation at the single site zero therefore depends on $T$, although the labelled support does not wrap. Exponential smallness of the difference does not turn it into equality. This is a counterexample to this **localization shortcut**, not to the Yang–Mills lemma.

**Why this attack failed.** Global resolvents carry unlabelled winding paths. To satisfy (B), their entire footprints must be assigned to the domain before taking traces. Equations (3.14) and (4.1) do not perform that assignment. They prove no exact non-wrapping agreement for the account's family.

### Attack 2: replace every global inverse by a local Dirichlet one

The outline proposes a local Möbius construction at SA 20317–20336. With the actual local precision $A_Y$, its free-bond part has
\[
 f_b(Y)=\operatorname{tr}(\log A_Y)(b,b),\qquad
 e(X;b)=\sum_{Y\subset X,\ b\text{ admitted in }Y}(-1)^{|X|-|Y|}f_b(Y).     \tag{4.3}
\]
For a finite set of cells this is an exact inclusion–exclusion identity. Expanding $f_b(Y)$ by (4.1), now with a genuinely local flat inverse, prevents the winding error in (4.2). The pivot determinant must be included separately. This construction is promising because each ingredient then depends on a finite domain only.

The local matrix cannot be chosen by convenience. Compression and inversion do not commute. For
\[
 A(t)=\begin{pmatrix}1&t\\t&1\end{pmatrix},\qquad |t|<1,
\]
compression to the first coordinate gives
\[
 \chi A(t)\chi=1,\qquad
 (\chi A(t)^{-1}\chi)^{-1}=1-t^2.                            \tag{4.4}
\]
The two log determinants have second derivatives $0$ and $-2$ at zero. Thus substituting the first matrix for the second changes exactly the jet under study. A flat bulk gap does not justify that substitution. In the account the local fluctuation form is built from its constrained covariance and the stated Dirichlet-cube walk rule. It is not an arbitrary compression of the Feynman operator in §3.

For this route the needed analytic estimate is of the form
\[
 \sup_{l,Y,P\in P_{a_l}(Y)}
 \big\|A_{l,Y}(0)^{-1/2}\big(A_{l,Y}(P)-A_{l,Y}(0)\big)
                  A_{l,Y}(0)^{-1/2}\big\|\le\theta<1,         \tag{4.5}
\]
with the corresponding weighted walk estimate, using the **actual** local form and the scale-normalized radius. If (4.5) holds, the $r$-th logarithmic term is bounded by its local trace multiplicity times $\theta^r/r$; the geometric sum is finite. But controlling this multiplicity and the domain sum in (4.3), uniformly in $l$, needs the actual local scale factors. The $k$-independent bounds in §3 apply to the bulk constant-curvature jets and do not establish (4.5) on the independent-current polydisc.

**Why this attack failed.** The exact local matrix and its complex-domain gap must be estimated before inclusion–exclusion. The computation (4.4) rules out the attempted replacement by a simpler compressed matrix. Fixed-depth positivity only gives an $l$-dependent neighbourhood; it does not give the scale-normalized uniform radius and amplitude in part (a).

### Attack 3: construct the intrinsic walks first, then differentiate their logarithm

Start instead with a cover by Dirichlet cubes and a parametrix $G_{\rm loc}$ for the actual constrained precision $A$. Write
\[
 AG_{\rm loc}=1-\mathcal R,\qquad
 A^{-1}=G_{\rm loc}\sum_{n\ge0}\mathcal R^n.                  \tag{4.6}
\]
Each product in (4.6) is labelled by every cube it visits. This repairs the winding defect of Attack 1. At a shared non-wrapping footprint the factors are the same Dirichlet matrices on both tori. Integrating
\[
 \frac d{dt}\log\det A(t)=\operatorname{Tr}\{A(t)^{-1}A'(t)\}              \tag{4.7}
\]
then produces a local logarithm with the correct matrix, avoiding (4.4). If a weighted row norm satisfies
\[
 \sup_\Delta\sum_{\Delta'}
 e^{\kappa d(\Delta,\Delta')}\|\mathcal R_{\Delta\Delta'}(P)\|
 \le\theta<1                                                   \tag{4.8}
\]
on a fixed scale-normalized polydisc, multiplication gives $\theta^n$. The sum in (4.6) is then bounded by $(1-\theta)^{-1}$. The logarithm integral and the domain entropy can be paid from a strict margin in (4.8). Reflection covariance follows if the cube rule and all its attachments transform together. This shows exactly how a proof on the account's route would close (a).

I tested whether the flux-jet estimates (3.6)–(3.10) imply (4.8). They do not cover its variables. The account's local precision depends on an independent current and on the curvature of the averaging constraint, before substituting the physical minimizer. The second variation contains
\[
 S''[a,a]-\langle\mu,D^2\mathcal M[a,a]\rangle,
\]
and a gauge change at nonzero current adds the corresponding current pairing. Both vanish on the constant-curvature stationary family used in §3. A bound proved only on that family has no information about derivatives in these independent directions. The hereditary domains also require the local minimizers on each smaller determining region, not just the flat global response. CA-I 3932–3941 names the walk input; CA-I 58738–58757 and 58853–58869 explicitly keep the local-family bounds and covariance assumptions.

There is no abstract way to infer the missing domain from a flat gap. The scalar analytic family $H_l(t)=1-L^lt$ has $H_l(0)=1$ and the same flat inverse for all $l$, but has a zero at $L^{-l}$. This is not the Yang–Mills precision. It proves that a depth-free flat bound, even exact, cannot replace an estimate of its actual complex perturbation. Likewise, bounded inverse norms on a one-parameter flux curve do not bound a derivative in an independent current direction.

**Why this attack failed.** To prove (4.8) one must control the actual local current/constraint factors on the polydiscs of part (a), with their scale factors, before differentiating or summing walks. Neither Gaussian composition, the bulk magnetic estimate, nor the quoted CMP 116 remainder bound provides that estimate. CMP 116 (2.41), as quoted at CA-I 4053–4056 and 4177–4179, bounds the non-Gaussian remainder with an $\varepsilon_1^{\rm I}$ factor; it is not a derivation of (4.8). This is the unresolved construction step, not lack of access to CMP 116.

## 5. Recovery checkpoint and verification limits

Only `library/ol.md` was changed. The target's wording, source status and consumer strength remain unchanged. No audit, ledger, prompt, branch, remote or retained status was modified.

Source identities: checkout `6a792352b901b4da73e40cbc393023af5c19d427`; Sussman–Alpoge revision `31a47c543775`. SHA-256 of the reused pinned outline is `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`; CA-I is `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`. The exact `/tmp/sa_*.tex` paths were already present and match the pinned identities recorded by the ports; they were not downloaded twice. Additional source hashes: CA-II `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f`; CA-III `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d`; local CMP 109 OCR `489fdb9d6f113fd8f98c552203ba65c841e5d137cc5b31ea5b14ff96b09a7d48`. The source reads were bounded excerpts. Shell/Python use was limited to source navigation, copying, hashing and text checks. No mathematical assertion was discharged by a run.

The bulk calculation and its conditional transfer are research arguments by Codex, not yet independently checked. The reference coefficient, the finite mass remainder, the fixed-depth Gaussian algebra, and the three failed localization routes are written above. Their conclusions do not establish the local realization lemma below. The next useful action is to estimate the actual Dirichlet-cube precision and its current/constraint jets in (4.5)–(4.8); repeating the radial integral or the first-passage arithmetic would not close it.

## Result

**Open lemma**

**Local realization of the zero-coupling Gaussian family (OL-loc).** Fix $N\ge2$, an admissible odd $L$, and the auxiliary parameters in the account's order. For every $l\ge1$, apply the account's intrinsic Dirichlet-cube walk and pivot rule to the genuine zero-coupling Gaussian normalizer $F_{l-1}$ of Balaban's step. The resulting family $N^{(l)}(X;(U,J),z)$, including its gauge and constraint Jacobians, has the following properties with constants chosen once:

1. Its total on every admitted torus, evaluated at the physical pair $(U_l,J_l)(e^{iB})$, is exactly $F_{l-1}(U_l(e^{iB}))$. Its first derivative at the trivial pair vanishes. Its physical total has the required translation and reflection covariance.
2. There are $E^\natural,\kappa>0$, depending only on $L,N,\mathfrak p$, and polydisc radii $a_l>0$, such that
   \[
   \sup_{P\in P_{a_l}(X)}|N^{(l)}(X;P,z)|
        \le E^\natural e^{-\kappa d_l(X)}.
   \]
   The radius is independent of $l$ when expressed in the potential/current norms specified by CMP 109 (1.13) and the account; the conversion to unscaled coordinates may depend on $l$. The bound is uniform in the torus and the domain.
3. Each non-wrapping term, including its holomorphic continuation, equals the term on its common infinite-lattice lift. The decay margin suffices for the domain sum and the second response moment used in CA-I 3808–3828.

This is the analytic-localization step of part (a), made explicit at the level of the actual Gaussian integral. It remains open after the three attacks in §4. The proved bulk route would give part (b), with $c_0=11N^2\log L/(12\pi^2)$ and $c_2=c_2(L,N)$, once OL-loc supplies the transfer in §3.3. The exact lemma as stated and used by the account is therefore **not proved here**. No counterexample to it is claimed. This is proof work on an open cited step, not an audit or a grant of status.
