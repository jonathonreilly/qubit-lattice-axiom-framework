# One-loop coefficient and finite part: CA-I Lemma 4.2

Provenance: Codex, research text at checkout 6a792352b901b4da73e40cbc393023af5c19d427, 2026-11-05; not an audit and grants no status. Sources: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, complete account and outline at 31a47c543775; Tadeusz Bałaban, CMP 109 and the account's quotation of CMP 116. All proof steps must be written and checkable by hand.

Round 2 provenance: Codex, 2026-11-05, pinned checkout `5129d8d4e01a632c1293ab712f8a758dcc64e6f5`. The round-one arguments below are preserved. This continuation compares OL-loc with the frozen `lrb.md`, `piv.md`, and `mu.md`; it is research text, not an audit, and grants no status.

Round 3 provenance: Codex, 2026-11-05, pinned checkout `d073927c08564435973eb8d54558e0571798e10e`. This continuation tests OL-W0 against `p82.md`, `pw.md`, `rows.md`, `hm.md`, `piv.md`, and CA-II Lemma 5.2:lem-random-walk-bounds. It preserves both earlier rounds. This is research text, not an audit; it grants no status. The sources and credit in the Provenance line apply throughout.

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

## 5. Round-one recovery record (preserved)

Only `library/ol.md` was changed. The target's wording, source status and consumer strength remain unchanged. No audit, ledger, prompt, branch, remote or retained status was modified.

Source identities: checkout `6a792352b901b4da73e40cbc393023af5c19d427`; Sussman–Alpoge revision `31a47c543775`. SHA-256 of the reused pinned outline is `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`; CA-I is `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`. The exact `/tmp/sa_*.tex` paths were already present and match the pinned identities recorded by the ports; they were not downloaded twice. Additional source hashes: CA-II `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f`; CA-III `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d`; local CMP 109 OCR `489fdb9d6f113fd8f98c552203ba65c841e5d137cc5b31ea5b14ff96b09a7d48`. The source reads were bounded excerpts. Shell/Python use was limited to source navigation, copying, hashing and text checks. No mathematical assertion was discharged by a run.

The bulk calculation and its conditional transfer are research arguments by Codex, not yet independently checked. The reference coefficient, the finite mass remainder, the fixed-depth Gaussian algebra, and the three failed localization routes are written above. Their conclusions do not establish the local realization lemma below. The next useful action is to estimate the actual Dirichlet-cube precision and its current/constraint jets in (4.5)–(4.8); repeating the radial integral or the first-passage arithmetic would not close it.

## Round-one endpoint (preserved)

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

## 6. Round two: what the new inputs supply

The preceding endpoint is historical. Sections 1–4 and their calculations
are unchanged. The current endpoint and checkpoint are below.

The sources remain Sussman and Alpoge, with Claude and Codex as authors of
their text, and Bałaban. The new reading used the outline index first:
chunks 07–08 (pivot, coarea and flat precision), 12 (the actual Gaussian
matrices), 19–20 (Gaussian localization and one-loop comparison), their
neighbouring rows, and the matching obligations. CA's operator input is
indexed in ca-4.12-4.19 chunk 04. Source passages used below were then read
at the pinned revision. No other averaging operation is substituted.

The comparison is as follows.

| New text | What it supplies here | What remains an input of that text |
|---|---|---|
| [lrb](lrb.md), §§3–10 and frozen Result | The actual local real comparison base; weighted displacement estimates; local coercivity; the analytic normalized vertex integral on its closed interpolation polydisc. | The assigned form-walk hypothesis W′, including its local half, cell-resolvent hypotheses, symmetry input, and the CMP 116 (2.14) setting. It does not construct these inputs from the physical Gaussian. |
| [piv](piv.md), §§2–6 and frozen Result | The nonlinear graph, its derivative \(C_{\flat}\), finite reads, local pivot inverses and common branches on its admitted working domains. | Primitive averaging and admission. Its stated color constants are for SU(2); the matrix-norm argument below explains the fixed-SU(N) extension actually needed here. |
| [mu](mu.md), §§4–7 and frozen Result | The regular minimizer, its specified complex continuation and the sub-tower identity on its admitted domains. | The published chart and averaging inputs recorded there. Nesting is not finite-range dependence of the minimizer on its datum. It supplies no off-graph estimate at independent current. |

Thus lrb closes the *comparison-base* problem in round-one Attack 2,
conditional on its precise operator hypotheses. Its §§4–5 also provide
the interpolation estimates sought in Attack 3 **once the assigned
walk families obey W′**. Requiring another proof of lrb would add nothing.
The remaining task is to supply these operator hypotheses for the
particular Gaussian that defines \(F_{l-1}\), and to retain its scalar
normalizer.

This distinction is explicit in CA, not inferred from a title.
CA-I 5519–5577 defines W′ and assigns it eight clauses; its all-level,
datum-independent local majorants are assumptions at the entry to
4.4. CA-I 8110–8116 imports them into the local-real-base proposition.
CA-I 6219–6310 imports W′ and coercivity into the cell-resolvent lemma.
The operator theorem gives a route toward them, CA-I 47253–47635.
Its proof invokes elementary sheets, the singular-word lemma, inverse
and branching estimates, and form identification. The port
[p4-operator](port/p4-operator.md), A9, keeps these as P4-H-elementary,
P4-H-local, P4-H-singular, P4-H-sheet, P4-H-assembly and P4-H-form.
Their presence in a proved implication is not a hand proof of those
inputs.

For this lane the geometry is only the trivial nest
\(\mathcal S_0\), CA-I 4750–4769. No large-field seam or stage-admission
assertion is needed. In particular, the prepared-nest hypothesis is
vacuous here. Importing the entire general-nest frontier would enlarge
the problem unnecessarily.

The original comparison with p3, p5, p6 and sfol in §1 still stands.
In particular p6 uses the **absolute** interval error, not only its
lower half. The literal one-loop-label search was repeated across
CA-I/II/III: the six occurrences remain those listed in §1.
The statement, definition, route and uses at CA-I 3764–4030,
3580–3615 and 56342–56495 were reread. No source status is promoted.

## 7. Three further attacks

### Attack 4: recover the missing scalar from the normalized vertex

This attack starts with the newly proved lrb integral, rather than
with a global logarithm. It gives a useful exact separation.

Write \(T=C^{-1}\), \(H=\operatorname{sym}T\), and
\(C_s=\operatorname{sym}C\), with bilinear transposes. On lrb's
small comparison domain, set its remaining integrand to one:
\[
 f_0(C,\Gamma)=\int d\mu_0(X)\,
 e^{-X^{\mathsf T}\Gamma^{\mathsf T}C\Gamma X/2}
 \int d\mu_C(B)\,e^{-B^{\mathsf T}\Gamma X}.
 \tag{7.1}
\]
The inner measure has precision \(H\), not \(T\) when \(T\) is
nonsymmetric. Real Gaussian integration and continuation on the
nonvanishing branch give
\[
 \int d\mu_C(B)e^{-B^{\mathsf T}y}
       =e^{y^{\mathsf T}H^{-1}y/2},
 \qquad
 f_0(C,\Gamma)=
 \det\!\left[I-\Gamma^{\mathsf T}(H^{-1}-C_s)\Gamma\right]^{-1/2}.
 \tag{7.2}
\]
For the second equality first work where the real part of the
remaining precision is positive; lrb §9 supplies this neighborhood.
Both sides are analytic there and equal on its real positive slice,
which fixes the branch.

If \(C\) is symmetric, (7.2) is identically one for every such \(C\).
It therefore cannot determine \(-\tfrac12\log\det C^{-1}\).
For example \(C=tI\), \(t>0\), gives the same \(f_0=1\) for every \(t\),
while the unnormalized \(m\)-dimensional integral is
\((2\pi t)^{m/2}\).

The nonsymmetric case does not repair this loss. Write \(T=H+K\),
\(K^{\mathsf T}=-K\). Multiplication gives
\[
 C_s=(H-KH^{-1}K)^{-1}.
 \tag{7.3}
\]
Indeed
\((H+K)^{-1}H(H-K)^{-1}\) is both
\(\tfrac12[(H+K)^{-1}+(H-K)^{-1}]\) and the right side of (7.3).
If \(\|H^{-1}\|\le h\) and \(h\|K\|\le1/2\), the inverse identity yields
\[
 \|H^{-1}-C_s\|\le2h^3\|K\|^2.
 \tag{7.4}
\]
So (7.2) sees a small symmetry defect. It still omits the normalization
determinant. This agrees with CA-I 7313–7338 and lrb §§8–9.
There is no error in lrb's normalization.

**Retaining the scalar instead.** Let
\(q_V(a)\) be the actual logarithmic constraint of a step,
\(K_V=q'_V(0)\), \(J_c=K_V|_{p(c)}\), and let \(u\) denote its nonpivot
coordinates. Pivot isolation gives
\[
 a=C_{\flat}u+h_Vv,\qquad K_Va=v,\qquad
 \det\frac{\partial a}{\partial(u,v)}
       =\prod_c\det J_c^{-1}.
 \tag{7.5}
\]
This is a block triangular determinant: the free block is the identity
and the pivot block is diagonal in the coarse bonds \(c\).
On the real branch its determinant is positive. The endpoint adjoint
changes of frame have determinant one: SU(N) is connected and their
real orthogonal determinants equal one at the identity.

Let \(A_k(P)\) be the actual reduced precision at
\(P=(\mathbf U,\mathbf J)\), including the soft gauge and the multiplier
correction. In CA-I 4806–4849 it is \(C^*\Delta^{(k)}C\);
in the free-bond notation of CA-I 45297–45326 it is \(\mathsf Q\).
At a physical stationary pair, integrating the real delta constraint
and then the free Gaussian gives
\[
 Z^{(k)}(P)=c_{k,T}
       \prod_c\det J_c(V)^{-1}\,\det A_k(P)^{-1/2},
 \qquad V=\mathcal M^k\mathbf U .
 \tag{7.6}
\]
Here \(c_{k,T}\) is independent of the background.

To check that last assertion, the Haar densities at fluctuation zero
are their constant values. The nonlinear straightening has derivative
the identity there. Both facts follow directly by differentiating the
graph at zero, as in SA 8308–8360. The gauge normalization is also
constant: with the block-root gauge fixed, each internal transport
transforms as \(V(y,x)g(x)^{-1}\). Haar substitution in the integral
over each \(g(x)\) removes \(V(y,x)\). The gauge factor therefore
contributes the same scalar at every background. Its quadratic form,
however, remains in \(A_k\). This is precisely the order of
linearization, scaling and pivot elimination in CMP 109 §2,
(2.4)–(2.11), pp. 266–268. There is no extra, omitted determinant
of \(C_{\flat}^{\mathsf T}C_{\flat}\): (7.5) already uses the original
Lebesgue coordinates and the original delta function.

The quadratic matrix must be the constrained Lagrangian Hessian.
If \(M(a)=v\), \(S'(a_*)=DM(a_*)^{\mathsf T}\lambda\), and
\(a(t)\) stays on the fiber, then
\[
 (S\circ a)''(0)=
 a'(0)^{\mathsf T}\!
       \left(S''(a_*)-\sum_i\lambda_i M_i''(a_*)\right)a'(0).
 \tag{7.7}
\]
This follows by twice differentiating \(M(a(t))=v\), then substituting
the stationary equation into \(S'(a_*)a''(0)\).
The physical branch supplied by mu permits this identification.
It does not set the multiplier term to zero away from the flat pair.

Vacuum subtraction in (7.6) gives the exact finite-dimensional identity
\[
 F_k(P)=
 -\tfrac12\operatorname{Tr}\{\log A_k(P)-\log A_k(P_\circ)\}
 -\sum_c\log\det\{J_c(V)J_c(1)^{-1}\}.
 \tag{7.8}
\]
First this holds at real stationary data. Both sides have the same
local analytic continuation from the positive flat Gaussian.
The right side also defines the independent-current extension wherever
its matrices and coherent logarithms exist. Formula (7.8) does not
assert a uniform complex domain.

**The pivot term is controlled on the admitted reference ball.**
The finite matrix-norm estimates of piv Lemmas 1–2 do not use three
colors. For fixed SU(N), use the operator norm on traceless matrices.
The exponential, logarithm and implicit-mean estimates are unchanged.
The pivot coefficient at the identity is
\(L^{-3}I_{\mathfrak g}\): exactly \(L\) of the \(L^4\) straight
segments contain the pivot, and no internal contour does.
Thus the same choices
\[
 a=(2^{16}L)^{-1},\quad K_2=16a^{-2},\quad
 v_*=\min\{a/8,(4L^3K_2)^{-1}\}
 \tag{7.9}
\]
give, for \(V=e^{iv}\) in a local unitary frame and
\(\|v\|_\infty<v_*\),
\[
 E_c:=L^3J_c(V)-I,\qquad \|E_c\|<1/4.
\]
Equivalently \(J_c=L^{-3}\pi_c\) in CA-I 46981–46988;
the factor \(L^{-3}\) must not be lost. With \(h_N=N^2-1\),
\[
 p_c(V):=-\log\det\{J_c(V)J_c(1)^{-1}\}
 =-\sum_{n\ge1}\frac{(-1)^{n+1}}n\operatorname{Tr}_{\mathfrak g}E_c^n,
 \qquad |p_c|\le h_N/3.
 \tag{7.10}
\]
The estimate uses
\(\sum_{n\ge1}4^{-n}/n\le\sum_{n\ge1}4^{-n}=1/3\).
It fixes the analytic logarithm without an absolute value of a complex
determinant. The reads are the actual double block and its composed
averaging carriers. Their equality on common lifts is exact.
Admission of \(V\) to this ball retains the hypotheses of piv §6,
or the account's unit-lattice lemma, CA-I 46992–47061.
It is not concluded from pivot invertibility alone.

**Outcome of Attack 4.** The scalar integral and pivot factor have
been identified, and the pivot logarithm has a local analytic bound.
Recovering them by setting the normalized lrb integrand to one fails
by (7.2). Even after the correct recovery (7.8), lrb supplies no
unconditional bound for the walk expansion of \(A_k\): it assumes it.
This attack therefore stops at the actual precision's local walk bound,
not at Gaussian normalization.

### Attack 5: perturb the actual flat fiber using piv and mu

The flat lower bound need not remain a separate unexplained input on
the trivial nest. The outline proves the needed argument at
SA 8467–8731. We port it here; it is not a new derivation of a result
missing from their text.

Let \(P^{[k]}\) be the derivative of the actual \(k\)-fold plain
average at the identity. Differentiating CMP 109 (0.10)–(0.12)
gives a straight-segment average plus a coarse gradient of internal
contour sums. Iteration preserves this description. With \(n=L^k\),
\[
 (d_nP^{[k]}w)_{\mu\nu}(y)
 =n^{-4}\sum_{x\in B_n(y)}\sum_{r,s=0}^{n-1}
                  (dw)_{\mu\nu}(x+re_\mu+se_\nu).
 \tag{7.11}
\]
The four boundary segments telescope; internal edges cancel.
The positive plaquette weights in (7.11) have row sum \(n^2\).
Their column sum is \(n^{-2}\): for each pair \((r,s)\), exactly
one centered block contains the corresponding starting point.
Weighted Cauchy therefore gives
\[
 \|d_nP^{[k]}w\|_2^2\le n^2n^{-2}\|dw\|_2^2=\|dw\|_2^2 .
 \tag{7.12}
\]
This is where dimension four matters. It is valid on finite tori,
with multiplicities retained, for every color component.

The flat constrained classical Hessian is
\[
 E_k(a)=\min_{P^{[k]}w=a}\|dw\|_2^2\ge\|da\|_2^2
 \tag{7.13}
\]
in the current lattice's own units. The affine set is nonempty:
put each coarse value on all fine bonds crossing its face and zero
on internal bonds. This is a right inverse at every scale.
A finite-dimensional affine subspace has a nearest image under \(d\),
so the minimum exists. Flat stationarity identifies this quadratic
minimum with the background Hessian; the first variation vanishes,
so no second derivative of the lift contributes. Equation (7.7)'s
multiplier correction also vanishes at this pair.

Let \(G\) be the arithmetic internal-contour gauge derivative and
\(C_0=C_{\flat}(1)\). The actual precision thus obeys
\[
 \langle u,A_k(P_\circ)u\rangle
 =E_k(C_0u)+\|GC_0u\|_2^2
 \ge\|dC_0u\|_2^2+\|GC_0u\|_2^2 .
 \tag{7.14}
\]
This uses the actual soft contour gauge; it does not replace it by a
divergence projector.

For completeness, the fixed-cell step making the lower bound uniform
is the one in SA 8620–8723. In a side-\(L\) cell the free space has
\(4L^4-4\) scalar coordinates. At Bloch parameter \(p\), the pivot
block is \(L^{-3}I_4\), independently of \(p\). Thus \(C_0(p)\)
is a continuous Laurent-polynomial matrix, is the identity on its
free coordinates, and has range \(\ker P_L(p)\).
If \(a=C_0(p)u\), \(d_pa=0\), and \(Ga=0\), plaquette swaps make
every internal contour sum independent of its path. Their average
being zero forces all internal bonds to vanish. A plaquette crossing
a block face then equates its two crossing bonds. Connectivity of
the transverse face grid makes their values one common value on
that face. The plain constraint equals that value and forces it to
zero. Hence \(a=u=0\), including at \(p=0\).

The continuous finite matrix
\[
 C_0(p)^*(d_p^*d_p+G^*G)C_0(p)
\]
therefore has a strictly positive minimum Rayleigh quotient \(c_L\)
on the compact Bloch torus. Otherwise a convergent sequence of
parameters and unit vectors would give a unit null vector.
The finite Fourier transform and (7.14) prove
\[
 A_k(P_\circ)\ge c_L I
 \tag{7.15}
\]
uniformly in \(k\) and volume. There are \(N^2-1\) identical color
copies. The same inequality holds for a genuine Dirichlet compression
of this flat matrix, by extending a vector by zero. It does **not**
identify that compression with a partial walk sum at a local datum.
The latter distinction remains the one in round-one (4.4).

Now try to continue (7.15) using only the new analytic charts.
Mu §4.1 gives a bounded holomorphic map on a depth-independent ball
in its weighted value norm. Cauchy's formula gives bounds for its
derivatives in that norm on a smaller ball. Piv gives fixed-range
bounds for \(C_{\flat}\) and its derivatives on admitted references.
These facts control coordinate changes. They do not yet bound the
weighted walks of the Hessian in (7.14) at a complex independent pair.

The exact missing derivatives can be displayed. In CA-I
47565–47573, put
\[
 H_k=P_\Lambda T_1^{-1}P_\Lambda-a+\mathcal J[\mathfrak j]+\mathsf G,
 \qquad A_k=C_{\flat}^{\mathsf T}H_kC_{\flat},
 \qquad T_1=QG_1Q^{\mathsf T}.
 \tag{7.16}
\]
Here \(P_\Lambda\) and \(a\) are fixed by the geometry; the current,
averaging letters and inverses retain their specified dependence.
A variation of the datum gives exactly
\[
 \begin{split}
 \dot A_k={}&\dot C_{\flat}^{\mathsf T}H_kC_{\flat}
       +C_{\flat}^{\mathsf T}\dot H_kC_{\flat}
       +C_{\flat}^{\mathsf T}H_k\dot C_{\flat},\\
 \dot H_k={}&-P_\Lambda T_1^{-1}\dot T_1T_1^{-1}P_\Lambda
                  +\dot{\mathcal J[\mathfrak j]}+\dot{\mathsf G},\\
 \dot T_1={}&\dot QG_1Q^{\mathsf T}
       +Q\dot G_1Q^{\mathsf T}+QG_1\dot Q^{\mathsf T},\\
 \dot G_1={}&-G_1(\dot G_0^{-1}+\dot W_1)G_1 .
 \end{split}                                                     \tag{7.17}
\]
The last line is used wherever the actual inverse exists, or first
at the flat point. It is obtained by differentiating its defining
inverse equation. These identities exhibit the derivative of each
factor; they do not estimate it.

In particular the chart bounds do not estimate the independent-current
terms in \(\dot W_1\) and \(\dot{\mathcal J[\mathfrak j]}\), nor the
local walk majorants of \(T_1^{-1}\). Mu does not vary that independent
current. Its nesting identity permits restriction of an already
admitted background, not removal of those variations from (7.17).

There is also a spatial loss even if one could prove an operator-norm
perturbation bound. To check the inference, take a torus of \(V=T^4\)
sites, let \(\mathbf1\) be its constant vector, and set
\[
 P_T=V^{-1}\mathbf1\mathbf1^{\mathsf T},\qquad
 A_T(t)=I+tP_T,\qquad |t|<1/4.
 \tag{7.18}
\]
Here \(P_T^2=P_T\), \(\|P_T\|_{2\to2}=\|P_T\|_{\infty\to\infty}=1\).
Thus \(A_T\) has a uniform analytic ball and
\(\operatorname{Re}A_T\ge3I/4\). The minimizer of its real quadratic
form is identically zero, with a trivial pivot chart.
Nevertheless, for fixed real \(t>0\), one distant off-diagonal entry
in a weighted row gives
\[
 \sup_x\sum_y |(A_T(t)-I)(x,y)|e^{b|x-y|}
       \ge t\,T^{-4}e^{bT/2}\longrightarrow\infty
       \quad(b>0).
 \tag{7.19}
\]
Taking even \(T\) makes the distance \(T/2\) exact.
This is a counterexample only to deducing exponential locality from
analytic and spectral bounds. It is not the actual local Yang–Mills
action and does not refute the target.

**Outcome of Attack 5.** The flat spectral lower bound is supplied
by a port of the outline's proof. The analytic-chart attack reaches
(7.17) but gives no depth-uniform local walk bound for its inverse
and current factors. Equation (7.19) shows why an operator-norm
Neumann argument alone would not finish it. The local equations,
rather than the chart's value bound, must supply the missing estimate.

### Attack 6: expand the actual Schur words, keeping their junctions

This attempt uses the actual word assembly in CA-I 47294–47635.
It is not a new choice of precision. The constrained inverse is
formed first; two current-dependent inverse series and two branching
operations then enter (7.16). On the trivial nest the geometric
separation conditions are void. The ultraviolet scales inside the
letters remain.

For one branch write \(G_\pi=(G_0^{-1}+W_\pi)^{-1}\). At finite depth,
whenever its Neumann series converges,
\[
 G_\pi=G_0-G_0W_\pi G_0
       +G_0W_\pi G_0W_\pi G_0-\cdots .
 \tag{7.20}
\]
The second branch has the same inverse identity with \(W_1\).
Expanding \(T_\pi^{-1}\) or \(T_1^{-1}\) adds the corresponding
coarse inverse and its local Dirichlet expansions. Every product
must retain its entire reading hull. The form finally produced is
(7.16), with its sign \(-a\), soft-gauge term and current vertex
unchanged.

The crude attempt is to estimate each factor by its absolute kernel
sum, then use multiplication of Schur norms. The account singles out
\[
 \mathfrak b=(DG')(D^*G_0D)(G'D^*)
 \tag{7.21}
\]
before doing this. Its prescribed treatment uses orders \((1,0,1)\)
and smooth junctions, CA-I 47389–47394. The reason this cannot simply
be omitted can be computed by hand.

The continuum local model for the middle differentiated Green kernel
in four dimensions is
\[
 g(x)=\frac1{4\pi^2|x|^2},\qquad
 \partial_\mu\partial_\nu g(x)
 =\frac1{4\pi^2}\left(
       -\frac{2\delta_{\mu\nu}}{|x|^4}
       +\frac{8x_\mu x_\nu}{|x|^6}\right),\quad x\ne0 .
 \tag{7.22}
\]
Two differentiations of \(r^{-2}\) give the two displayed terms.
For \(\mu\ne\nu\), its absolute radial integral over
\(\eta<|x|<1\) is
\[
 c_{\mu\nu}\int_\eta^1\frac{dr}{r}
       =c_{\mu\nu}\log(1/\eta),\qquad
 c_{\mu\nu}=\frac2{\pi^2}\int_{S^3}|\omega_\mu\omega_\nu|\,d\omega>0 .
 \tag{7.23}
\]
Positivity follows already on a small open patch where both coordinates
are nonzero. No numerical evaluation of this constant is needed.
At \(\eta=L^{-k}\), (7.23) grows as \(k\log L\).

The cancellation discarded by absolute values is equally explicit:
\[
 \int_{S^3}\omega_\mu\omega_\nu\,d\omega
       =\tfrac14\delta_{\mu\nu}|S^3|,
\]
by reflections, permutation symmetry and \(\sum_\mu\omega_\mu^2=1\).
Consequently (7.22) has zero mean on every sphere.
If a junction factor \(f\) is Hölder with exponent
\(0<\alpha\le1\), subtract \(f(x)\) before estimating its convolution.
The constant part cancels on each full annulus. The remaining local
integral is bounded by
\[
 C[f]_\alpha\int_\eta^1 r^{\alpha-1}\,dr
       \le C[f]_\alpha/\alpha .
 \tag{7.24}
\]
Boundary cutoffs add their own differences; their Hölder norms must be
included. This calculation identifies a possible repair of the crude
estimate, not a divergence of the true composite (7.21).

To apply that repair to the lattice word, one needs the corresponding
discrete cancellation and junction estimates **with the actual
Dirichlet boundaries, averaging rows, local background/current
variables and all reading hulls**. The elementary-sheet inputs
at CA-I 47294–47324 name precisely the CMP 99b (3.43), (3.44)
Hölder estimates. The singular-word step then imports its own
smooth-junction lemma. Local CMP 99b pp. 427–428 also explains that
expanding the current correction creates a third branch through \(H\);
it is not a product of two kernels with the third branch suppressed.

The attempted absolute-kernel estimate can now be stated precisely.
Replacing the order-zero letter by the envelope
\(C(|x-y|+\eta)^{-4}\) on distances at most one gives a Schur
upper bound \(C'(1+\log(1/\eta))\). Indeed, the innermost ball
has bounded integral and the remaining radial integral is
\(C'\int_\eta^1dr/r\). Combining this envelope with the finite
pivot bounds would impose a sufficient small-current condition of
the form \(C''(1+k\log L)\|\mathbf J\|<1\).
This estimate supplies no fixed scale-normalized radius.
It is an estimate for that envelope, not a lower bound on the
actual discrete word or a necessary condition for its convergence.
In particular, (7.23) alone does not prove that a logarithmic loss
survives in the lattice composite.

Keeping the cancellation leads instead to (7.24). Its missing input
is a uniform local estimate for the true junction factors, including
the dependence of \(H,H_1,T_\pi^{-1},T_1^{-1}\) on free current.
Piv estimates only the finite unit-lattice letters at the ends.
Mu's physical minimizer value bound does not give this estimate.
Lrb begins after these letters have already been assembled into a
family satisfying W′. Using lrb's walk bound to estimate (7.21)
would therefore be circular.

**Outcome of Attack 6.** The actual inverse/branching route has been
followed to its singular junction. The crude order-zero envelope
loses a logarithm; cancellation repairs that model loss, but its
required local lattice Hölder estimates have not been supplied for
the full actual family. The missing bound is
formulated as one precise sufficient lemma below. This is a failed
attempt, not a no-go statement.

**The depth-zero case does not need this estimate.** At \(k=0\)
the classical action is the Wilson action itself. Its quadratic
form is the sum of the four-link plaquette Hessians (2.3), the
soft contour-gauge square, and the constraint-multiplier term
\(-2\langle hC^{(2)}(B),\mathbf J\rangle\), followed by the two
factors \(C_{\flat}\). These are the direct step definitions in
CMP 109 §2 and CA-I 46972–46989. There is no fine-scale inverse
in this formula. Each factor reads a fixed finite number of
unit-lattice blocks. Piv's joint holomorphic bound, on a smaller
ball, bounds its first and second derivatives by Cauchy's formula;
the Wilson factors are finite products of exponentials. The current
vertex is linear in \(\mathbf J\).

Expand just this finite sum and its finite products. Assign to each
term its full connected block read. There are at most \(n_L\)
terms through any fixed bond, each with at most \(m_L\) other
bond indices and read diameter at most \(R_L\); these finite
numbers depend on the stencil and \(L\), not on the torus.
If \(C_{L,N}\) bounds each coefficient on the fixed smaller
potential/current ball, both weighted sums are at most
\(n_Lm_LC_{L,N}e^{\delta R_L}\), for any fixed \(\delta>0\).
The same coefficients and bounds are defined from local data alone.
This proves the required depth-zero version by a finite analytic
estimate. The unresolved quantifier in OL-W0 is \(k\ge1\).

## 8. What the remaining precision lemma would close

This section gives the reduction, with the hypothesis kept visible.
Assume the lemma OL-W0 stated in the Result, and combine it with
the depth-zero bound just proved by taking the larger majorant
constant and the smaller rates and radii. It asks for the actual
precision's local walk majorants near the flat pair, uniformly in
depth. It asks for no one-loop value and no estimate of a determinant.

### 8.1 From the precision family to local resolvents

Write its bound as \(B\), its rate as \(\delta\), and its scaled
analytic radius as \(r_*\). On a radial subdisc of relative radius
\(s<1\), Cauchy's formula, applied to each local coefficient, gives
\[
\max\!\left\{
\sup_b\sum_{\omega,b'}
 |(A_{k,\omega}(P)-A_{k,\omega}(P_\circ))(b,b')|
 e^{\delta d(\omega;b,b')},\quad
\sup_{b'}\sum_{\omega,b}
 |(A_{k,\omega}(P)-A_{k,\omega}(P_\circ))(b,b')|
 e^{\delta d(\omega;b,b')}
\right\}
\le B\frac{s}{1-s}
 \tag{8.1}
\]
in both row and column sums. The right side follows by summing the
positive-degree Taylor coefficients against their **datum-independent**
majorants. More explicitly, write \(A'=sA'_0\),
\(\mathbf J=s\mathbf J_0\), and expand the one-variable function
\(t\mapsto A_{k,\omega}(e^{it\xi A'_0},t\mathbf J_0)\).
Each coefficient of a kernel entry is bounded by its majorant
\(a_{k,\omega}(b,b')\); summing \(\sum_{n\ge1}s^n\) proves
(8.1), with no count of coordinate monomials. A bound on the sum
of the matrices alone would not justify this step. Choose
\(s>0\) so \(Bs/(1-s)\le c_L/8\).

For the account's near/far split choose \(r'\) with
\(Be^{-\delta r'}\le c_L/8\), as well as the account's
condition (k1).
The flat full form has gap \(c_L\) by (7.15). Its near part thus has
gap at least \(7c_L/8\). A local cell matrix is the compression of
that near part; its read lies in the enlarged cell. Equation (8.1)
on that read changes its norm by at most \(c_L/8\).
Consequently every such local cell matrix has real part at least
\(3c_L/4\). This compares locally defined matrices with the flat
matrix directly. It does not extend the nonzero local datum to a
torus.

The same estimates give global coercivity. They verify the
near-flat positivity, inclusion and regularity requirements of the
local cell-resolvent construction; one may use
\(\gamma_*=c_L/2\), so the cell bound is stronger than its
required \(7\gamma_*/8\). Apply the account's proved
4.4:lem-cell-resolvent, CA-I 6219–6310, with its local form and its
(k1),(k2) choices. In its notation this supplies, for every
\(\lambda\ge0\),
\[
 R_k^Y(\lambda)=\sum_\varpi R_{k,\varpi}^Y(\lambda),\qquad
 |||R_k^Y(\lambda)|||_\theta\le\frac{4S}{\lambda+c},
 \quad c=\gamma_*/2>0 .
 \tag{8.2}
\]
The constants are fixed before \(M\), uniformly in \(k,Y\) and volume.
Every term is analytic on its own read and uses the actual Dirichlet
cell matrices. Equal reads give equal terms on a common lift.
The local proof at CA-I 6827–6963 uses just these cell inequalities,
the datum-independent Schur majorants and the near/far geometry.
It sums families of kernels on the local region; it does not assume
that their partial sum is an inverse on that region.

This application ports the existing cell-parametrix proof. It does
not assert that an inverse of an interpolated precision equals an
interpolated inverse. On broader regular backgrounds lrb retains
its full upstream positivity hypotheses; (8.1) is only the
near-flat specialization needed for the coefficient lemma.

### 8.2 The actual determinant family, with an absolute bound

The account already localizes the scalar determinant at CA-I
9707–9757, ported in p4-operator A3-F2–F3. Use that rule, not the
normalized vertex (7.1). With the positive number \(c\) of (8.2),
\[
 -\tfrac12\log\det A_k^Y(P)
 =\mathrm{const}
 -\tfrac12\int_0^\infty
 \frac{\operatorname{Tr}[(A_k^Y(P)-cI)R_k^Y(\lambda;P)]}
      {\lambda+c}\,d\lambda .
 \tag{8.3}
\]
The scalar identity follows by integrating the difference of two
resolvents. At finite matrices it follows on each Jordan block by
differentiating that scalar identity. All eigenvalues of an accretive
matrix lie in the right half-plane, so the logarithm is the branch
continued from positive matrices. This is the source's proof route.

For a diagonal entry \((b,b)\), expand the product in (8.3).
Retain every intermediate bond and every walk footprint.
The \(X\)-term collects
\(\operatorname{tr}_{\mathfrak g}(A_{k,\omega}R_{k,\varpi}^Y)(b,b)\)
when the account's hull of their combined footprints is \(X\).
The \(-cR\) term is collected by its own footprint. Subtract the
identically collected term at \(P_\circ\). This is a formula for
the actual local scalar term, not a determinant of a replacement
local covariance.

The weighted row and column sums multiply: the union of trees
meeting at the intermediate bond has length at most the sum of their
lengths. Equation (8.2) therefore bounds the absolute integral before
any grouping by
\[
 \int_0^\infty
 \frac{4S(B+c)}{(\lambda+c)^2}\,d\lambda
       =\frac{4S(B+c)}c .
\]
The trace costs \(h_N=N^2-1\). The factor \(1/2\) and the two
vacuum-subtracted evaluations cancel in the upper bound. Hence at
each fixed root bond
\[
 D_{\log}:=\frac{4h_NS(B+c)}c
 \tag{8.4}
\]
bounds the full absolute, length-weighted determinant family.
There is no factor equal to the volume or the number of free bonds:
the estimate is for a *rooted diagonal entry*. This is the quantitative
addition to the existing p4 absolute-interchange argument.

For clarity, the passage from this walk weight to a polymer weight
requires the full dependence footprints. Let \(D\) be the total
tree length of a contributing product in step-\(k\) units.
Its steps have uniformly bounded diameter; choose \(M\) so this
diameter is at most \(LM/4\). The connected cube hull, with its
fixed finite collars, meets at most
\[
 C_h\left(1+\frac{D}{LM}\right)
 \tag{8.5}
\]
cubes of side \(LM\), for a geometric constant \(C_h\).
Here the hull is the cubical localization hull of the walk rule,
not the full rectangular box surrounding a long thin walk.
The convention is SA 5586–5596: the union of cubes containing the
set, with the fixed collars required for its complete read.

One elementary bound proving (8.5) is obtained by traversing a finite
tree in both directions, a path of length at most \(2D\).
Mark this path at arclength intervals \(LM\).
Every point of a step domain is within \(LM+LM/4\) of a mark.
Each such neighborhood meets at most \(5^4\) grid cubes.
A fixed number of collar layers only multiplies this count by a
fixed finite number. Thus \(C_h\) may be chosen as twice that number
times \(5^4\). Infima defining tree lengths are handled by first
using a tree within \(\epsilon\) of the infimum and letting
\(\epsilon\downarrow0\). No enumeration is used.

Joining centers of neighboring cubes by paths through their common
faces or corners gives
\[
 d_{k+1}(X)\le4C_h\left(1+\frac{D}{LM}\right).
 \tag{8.6}
\]
The factor four is the dimension; the joining paths remain in the
connected union of cubes. This is consistent with CA-I 3725–3761's
tree-length convention. If an intermediate choice of hull adds
fixed collars, use its correspondingly enlarged \(C_h\).

After \(\theta,C_h\) and the required \(\kappa\) have been fixed,
choose \(M\) with \(4\kappa C_h/(LM)\le\theta/2\).
Equations (8.4)–(8.6) then give, before pointing,
\[
 |d_b(X;P)|\le
 D_{\log}e^{4\kappa C_h}e^{-\kappa d_{k+1}(X)}.
 \tag{8.7}
\]
Half the walk decay remains for spatial moments. The prescribed
midpoint tents have finite support and finite overlap in rescaled
units. Let \(C_{\rm pt}\) be their overlap bound, including the
finite bond multiplicity. It depends only on the fixed template and
the auxiliary parameters. Pointing costs at most \(C_{\rm pt}\).
This is precisely the midpoint rule at SA 5917–5925.
The pivot terms (7.10), whose full reads have bounded size, obey
the same form of bound after increasing the constant.

The majorants in OL-W0 and (8.2) are valid for locally given data.
Consequently all rearrangements above are locally absolutely
convergent and holomorphic, without choosing an extension.
On a non-wrapping common lift every factor, intermediate index and
integration weight is identical. The terms agree exactly there.
A suppressed winding walk cannot hide in a coefficient.

On a finite torus, summing all roots and hulls in (8.3) returns the
determinant in (7.8); adding the pivot terms returns the genuine
Gaussian normalizer. The correct scalar branch is retained.
Individual localized matrices need not be symmetric. No
\(\det(\operatorname{sym}C^{-1})\) is substituted into (8.3);
that symmetrization belongs to lrb's normalized real integral.

### 8.3 Physical substitution, moments and constants

Every scalar term just constructed is invariant under simultaneous
constant color conjugation. Its first derivative at the flat pair
therefore vanishes. Indeed, fixing any one bond or current slot gives
an invariant linear functional on the traceless matrices. Such a
functional kills every commutator. Off-diagonal matrix units are
commutators with diagonal matrices, and traceless diagonals are
linear combinations of \([E_{ij},E_{ji}]\); hence that functional
is zero. This argument applies separately to each slot.

The physical total has the account's lattice translation and
reflection covariance. Transform the actual finite Gaussian and
its constraint together. The symmetry permutes the bond variables,
transports the specified contours, and changes the axial
representative by a gauge transformation when necessary.
Gauge normalization is the constant checked before (7.7);
(7.5) retains the constraint Jacobian. Thus its scalar integral,
and then its normalized logarithm, are unchanged. This uses the
account's symmetry-respecting average and attachments, not a new
symmetrization of the localized matrices.

For each fixed \(l\), take a smaller positive physical \(B\)-radius
whose background/current image lies in the local polydiscs above.
The chart admission and nesting are precisely the relevant
conclusions of mu, with their stated input ceilings; the free
response is the one used in §3.3. Conversion to raw coordinates can
shrink this radius with \(l\). The precursor pair radius is fixed
in the potential/current norms, as requested in Lemma 4.2(a).
No assertion about arbitrary large-field or unadmitted representatives
is made.

Choose the polymer decay with a strict margin above the domain
entropy constant in CA-I 3742–3747. Cauchy's estimate on a smaller
pair ball, the surviving walk decay, and the fixed-depth response
bound give the summable Hessian majorant used in §3.3.
In particular the second spatial moment is finite: a polynomial
of degree two times an exponential is summable on \(\mathbb Z^4\).
Port the convergence argument of CA-I 58732–58989 in its
Gaussian-only specialization. Its analytic inputs are the local
majorants just obtained, the common-lift equality and the fixed-depth
free response used in §3.3. These give a bound
\(C_l e^{-\delta_l(|x-z|+|y-z|)}\) for the pointed Hessian.
Summation over \(z\), with any second moment in \(x-y\), is
absolutely convergent: one may reserve half of the exponential
for the polynomial moment and sum the other half. Non-wrapping
terms agree on a common lift, and the wrapping tail tends to zero.
Dominated convergence therefore identifies the Hessian of the
finite-volume total with the sum of companion Hessians. Covariance
of that total, proved above at physical data, passes to this limit.
This step needs no assertion that an individual bond-rooted
logarithm is covariant under a change of pivot coordinates.
It is the same conditional transfer as §3.3, with its
analytic-family supplier reduced to OL-W0; the broader non-Gaussian
covariance hypotheses of the source theorem are not asserted here.

The order of constants is unchanged. The bulk calculation fixes
\(c_0\) and \(c_2^{\rm bulk}(L,N)\) at Stage 2, CA-I 1416–1427.
The local majorants, cell radius and decay are chosen before the
later \(M\)-floors; \(M\) then absorbs the interpolation, hull and
entropy costs. Finally the allowed potential/current radii are
decreased, with their ratio floors retained.
The localization amplitude may depend on \(\mathfrak p\);
\(c_2^{\rm bulk}\) does not.

Under OL-W0, (7.8), (8.7) and this transfer therefore prove
OL-loc on the near-flat polydiscs needed by Lemma 4.2, and §§2–3 give
\[
 \left|\sum_{l=1}^k\beta_l^0-kc_0\right|
 \le c_2^{\rm bulk}(L,N),\qquad
 \left|\sum_{l=i+1}^n\beta_l^0-(n-i)c_0\right|
 \le2c_2^{\rm bulk}(L,N).
 \tag{8.8}
\]
These remain implications. Neither lrb, piv nor mu supplies OL-W0.

## 9. Current recovery checkpoint and limits

This is the current checkpoint; §5 records round one only.
The target remains the exact lemma copied in §1, including the
absolute finite-part bound and the order of constants.

| Item | Present conclusion |
|---|---|
| Round-one §§2–3 | Preserved: hand reference calculation, bulk finite-part argument and conditional transfer. They remain research arguments, without a new independent review in this round. |
| lrb comparison | Its normalized local vertex and comparison-base conclusions are usable with their stated hypotheses. W′ is an input, not a consequence of that proposition. |
| Attack 4 | Equations (7.2)–(7.4) prove why the normalized vertex loses the scalar. Equations (7.5)–(7.10) retain the genuine determinant and control the pivot logarithm on its admitted ball. The missing estimate is for the actual precision. |
| Attack 5 | The outline's flat-fiber argument gives (7.15), uniformly in depth and volume. Charts and minimizer values do not bound the independent-current derivatives and spatial walks in (7.17). The explicit example (7.18) refutes that inference alone. |
| Attack 6 | The true assembly reaches the order-zero singular junction (7.21). The crude envelope gives a depth-dependent sufficient radius. The hand cancellation (7.24) identifies what a uniform lattice junction estimate must preserve; that estimate is still missing. The finite-stencil case \(k=0\) is covered. |
| Reduction | §8 derives the required near-flat local Gaussian family from OL-W0, with exact scalar normalization, common-lift agreement and the account's constant order. This is an implication, not a proof of OL-W0. |

The next decision is whether the published differentiated-kernel and
Hölder estimates, with their actual boundary and current hypotheses,
give datum-independent local majorants for the full word (7.21)
and its two current branches. Start at CA-I 47294–47584 and local
CMP 99b Theorem 3.12 and pp. 427–428. A proof must carry the full
reading domains through the Schur inverses and both branching
operations. A global norm estimate, a normalization convention,
or a numerical check would not decide OL-W0.

The source revision is still Sussman–Alpoge 31a47c543775, credited
to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text. The finite-dimensional Gaussian step is Bałaban's.
The current checkout is 5129d8d4e01a632c1293ab712f8a758dcc64e6f5.
The outline and CA-I were each fetched once in this round; their
SHA-256 values are the ones recorded in §5. CA-II and CA-III were
searched for the exact target label at their existing pinned copies.
Source quotations and uses were checked against bounded source
ranges; the full large source files were never read into context.

Frozen local input identities (SHA-256):

    lrb.md  23b7d710a2dff388ac1adbededa2177a0a0bf02f97d12523ca9f9fb35552969d
    piv.md  9e5483ca902652af890da208e3cc9f8479c42b0bd88450d827b2637ace383763
    mu.md   2f3643c41fa8655a01ae8a6f7afa16c45f459bf41512c585acbeae63504a323b

The original round-one file has SHA-256
73111c1ec99a4784d9d3564cf037df04e1e561339474b3e16cebd7052ef1df7b;
a recovery copy is at /tmp/ol-round2-5129d8d4e/ol-round1.md.
The text-integrity record is
/tmp/ol-round2-5129d8d4e/verification.json.
Only library/ol.md is edited. Source downloads, navigation,
hashing and textual integrity checks are bookkeeping. No run,
enumeration, numerical integration or computer enclosure is used
to discharge a mathematical assertion. The new arguments have
not received an independent referee check. No audit, claim status,
planning record or editable prompt is changed.

## Round-two endpoint (preserved)

**Open lemma**

**OL-W0: intrinsic analytic walk bound for the actual free-current
precision near the flat pair, at positive depth.** Fix \(d=4\),
\(N\ge2\), and the account's admissible odd \(L\). Fix the operator
frame parameters at their prescribed early stages, before the
localization cube size \(M\). There exist positive
\(r_A,r_J,\delta,B,\rho_w\), depending only on these fixed parameters
and \(L,N\), with the following property, uniformly for every
\(k\ge1\) and every admitted torus at the trivial nest
\(\mathcal S_0\).

Use the actual free-current quadratic form of CA-I 4737–4849,
in its free-bond notation (7.16):
\[
 A_k(P)=C_{\flat}(P)^{\mathsf T}
 \bigl(P_\Lambda T_1(P)^{-1}P_\Lambda-a
       +\mathcal J[\mathfrak j](P)+\mathsf G(P)\bigr)
 C_{\flat}(P),\qquad T_1(P)=Q(P)G_1(P)Q(P)^{\mathsf T}.
 \tag{OL-W0.1}
\]
All averages, currents, pivot coefficients, intermediate inverses
and contour attachments in this formula have the account's
definitions. In particular \(\mathbf J\) is an independent variable,
and the constraint-current Hessian is retained.

For a local reading domain \(D\), let \(\mathcal P_*(D)\) be the
flat-base polydisc of locally given pairs
\[
 P=(e^{i\xi A'},\mathbf J),\qquad
 \max\{|A'|,|\nabla^\xi A'|\}<r_A,\qquad
 |\mathbf J|<r_J
 \tag{OL-W0.2}
\]
on all bonds and difference stencils read in \(D\). The fields are
complex and Lie-algebra valued; \(\xi\), the current normalization
and changes of units are those of CMP 109 (1.13)–(1.14) and
CA-I 4610–4703. No additional plaquette condition or global
extension is part of this local polydisc. Equivalently the two
radii are fixed in those scale-normalized norms, not in raw
unscaled bond coordinates.

The account's actual word expansion and Dirichlet-cube rules,
CA-I 47294–47584, give coefficients \(A_{k,\omega}\) with these
properties:

1. **Identification and complete reads.** On global data in
   \(\mathcal P_*\),
   \(A_k=\sum_\omega A_{k,\omega}\), including both current
   branches and the \(C_{\flat}\) factors of (OL-W0.1).
   Each coefficient is defined and holomorphic from data on its
   complete read \([\omega]\) alone. Every step domain includes
   what that step actually reads, has diameter at most \(\rho_w\)
   in step-\(k\) units, and consecutive domains intersect.
   Intermediate averaging carriers and boundary data are included;
   they may not be suppressed from the footprint.

2. **One local majorant bound.** There are nonnegative numbers
   \(a_{k,\omega}(b,b')\), independent of the datum, such that
   \[
   \sup_{P\in\mathcal P_*([\omega])}
       |A_{k,\omega}(b,b';P)|\le a_{k,\omega}(b,b'),
   \]
   \[
   \max\!\left\{
   \sup_b\sum_{\omega,b'}a_{k,\omega}(b,b')
          e^{\delta d(\omega;b,b')},\quad
   \sup_{b'}\sum_{\omega,b}a_{k,\omega}(b,b')
          e^{\delta d(\omega;b,b')}
   \right\}\le B .
   \tag{OL-W0.3}
   \]
   Here \(d(\omega;b,b')\) is exactly CA-I 4875–4907's
   shortest-tree length: the tree contains the two initial bond
   points and meets every complete step domain. The norm of a
   kernel entry is the operator norm on the complex color space.
   This is a bound for the absolute family, before summing it
   into a matrix. It must hold when only local data are supplied.

3. **Intrinsic rule.** Equal complete reads in two geometries,
   including a non-wrapping common lift, produce equal coefficients
   and the same majorant assignment. Restrictions and the
   prescribed color/frame transformations act on the coefficients
   as they do on the actual defining operators. The constants in
   (OL-W0.2)–(OL-W0.3) are independent of \(k\), volume,
   localization domain, \(M\) and coupling. Subsequent decreases
   of the allowed potential/current radii preserve the bound and
   can respect the account's primed/unprimed ratio floors.

This is the near-flat, trivial-nest portion of W′ with its local
quantifier and scalar-independent operator content made explicit.
It is one sufficient operator lemma, not a claimed necessary
condition for the one-loop law. The depth-zero case, the flat
spectral lower bound and the pivot logarithm are established above.
The three new attacks fail for the distinct reasons recorded in
§7: normalization erases the scalar; charts and a spectral gap do
not supply spatial/current control; and absolute estimates at the
singular junction discard the cancellation needed for a uniform
local radius.

If OL-W0 is proved, §8 supplies OL-loc and the preserved calculation
gives the account's full one-loop statement, with
\(c_0=11N^2\log L/(12\pi^2)\) and \(c_2=c_2(L,N)\).
OL-W0 has not been proved here. No counterexample to Lemma
4.2:lem-one-loop is claimed, and that lemma remains open in this
research text.

## 10. Round three: what the frozen estimates actually supply

The statement of Lemma 4.2, its Route, and its uses are unchanged.
The comparison below concerns the operator obligation at the end of
round two. “At the flat pair” means a **complex neighbourhood** of
that pair, with an independent current; a bound only at \(A'=J=0\)
would not suffice. This round keeps OL-W0's requirement that the
family be the account's successive word/sheet family, CA-I
47294–47584. Existence of another good expansion is distinguished
from that requirement.

### 10.1 Comparison with the requested sources

| Source, checked passage | What it supplies here | What cannot be inferred |
|---|---|---|
| [p82.md](p82.md), I1–I5, Lemmas 1–6 and Theorem P | Matching flat/local inverse estimates, actual iterated averaging rows, smooth-cutoff parametrix and real layered propagator bounds, uniform in mesh and depth. | The real theorem alone does not give an independent-current complex neighbourhood. Retain its stated flat/model inputs. |
| [pw.md](pw.md) §§2–5.1 | Exact local splitting of the eight-variable system; absolute second jets of the actual averaging map; complex inverses on cut-downs with an arbitrary coefficient current; existence of the defining scalar and row Gram inverses. | A saddle inverse cannot simply be called an unconstrained inverse: §3 and §5.1 supply the separate coercivity and Schur checks. |
| PW §§6–7, (6.10)–(6.13), (7.1)–(7.7) | Bounds for individual coefficients of the specified unfolded parametrix, including the multiplier branches, before switches. The count retains \(C^{n+\sum m_i}\) and \(M_1^{-N/3}\). | The final inequality [PW], by itself, bounds a sum. Its coefficient proof is what is needed here. |
| [rows.md](rows.md) §§2–3 and §5, (5), (8)–(9), (22)–(27) | Absolute rows and columns, the full sixteen-insertion plaquette Hessian, and physical-to-counting multiplier conversion. | The raw-row transpose cannot replace the physical transpose without the row-length factors. |
| [hm.md](hm.md) Lemma 1 | Under W, two-sided datum-independent majorants for the unfolded precision on complete local reads, including the boxes read by the zero-length multiplier. | W is an explicit premise. The later integrated resolvent consumes the precision bound. HM's absolute soft-gauge Hessian needs the local replacement in §11.3. |
| [piv.md](piv.md) §§1–5 | Actual one-step mean, pivot inverse, graph derivative and complete finite reads. | One-step analyticity alone is not a depth-uniform bound; the iteration uses P82 Lemma 1 and PW §4. |
| CA-II 8922–8990, 5.2:lem-random-walk-bounds | The attributed precision, conditioned inverse and root bounds, with domain and exponential-gauge identifications. | CA-II 8941–8946 expressly takes three CMP 116 inputs by statement. This is not a new proof of their complex local-data, absolute-family version. |

The closest ports do not already prove the target. P3-free retains
H-BG, H-TOWER and H1-MIN in its free-covariance algebra. P5-induction's
clause-(0) table retains A12(b). P6-correlation, B4b, assumes the
one-loop lemma. Sfol-draft §§3.3–3.7 checks the bulk coefficient and
telescoping normalization for \(N=2\), conditional on its localized
moment, identification and other stated inputs. None supplies the
missing absolute bound for the account's assigned family. The
general-\(N\) calculation in §§2–3 above is preserved.

The two walk prescriptions are concretely different. CA-I
47294–47324 expands \(G',G_0,T'\) and differentiated letters;
47389–47394 treats a singular word; 47396–47531 inverts a coarse
Gram operator with a second cover; 47533–47584 performs two
branching operations and assembles the precision. H-walk §1
expressly uses another construction: unfold the Schur factors into
a finite-range system and expand its local inverse. PW §7 specifies
those coefficients. Bałaban CMP 99b, pp. 413–416, (3.98)–(3.108),
uses the successive construction, including local comparisons and
cancellations before iterating its small remainder.

P4-operator retains P4-H-elementary, P4-H-singular and P4-H-sheet
as named inputs at these exact use loci; it is not another proof of
them. Likewise CA-II's cited walk statement does not resolve the
status discrepancy between CA-I 3930 and 56361–56365, A12(b) at
56428–56430, and its proof at 56466.

### 10.2 The quantifier to be transferred

For a local family \(K=(K_\omega)\), put
\[
 \|K\|_{\mathrm{abs},\delta}
 =\max\left\{\sup_b\sum_{\omega,b'},\sup_{b'}\sum_{\omega,b}\right\}
 e^{\delta d(\omega;b,b')}
 \sup_{P\in\mathcal P_*([\omega])}|K_\omega(b,b';P)|.
 \tag{10.1}
\]
The local supremum precedes the sums. A bound on the globally
summed matrix is weaker. OL-W0 asks for (10.1) for the account's
construction. The next three attacks address this quantifier,
rather than repeat round two's normalization, spectral-gap and
absolute-kernel attacks.

## 11. New attack 7: unfold the actual precision on local flat data

This proves a **version** of OL-W0 for the repaired unfolded
family, retaining P82's frozen flat/model inputs. It does not
identify its coefficients with CA-I 47294–47584.

### 11.1 Local admission and order of constants

Put \(\eta=L^{-k}\) in level-\(k\) units. Expand the four plaquette
exponentials at the flat real reference. The linear terms give
\(\eta^2\) times the discrete curl. For \(\eta r_A<1/16\) the
remainder is bounded by \(C\eta^2r_A^2\). Therefore
\[
 \eta^{-2}|\partial(e^{i\eta A'})-1|
       \le C(r_A+r_A^2).                                  \tag{11.1}
\]
Only the forward differences already in \(\mathcal P_*\), including
boundary stencils in the complete read, were used. All longer
local scales are at most \(L\), so the complex curvature clause
has ceiling \(CL^2(r_A+r_A^2)\). The real curvature and gauge
clauses hold with gauge \(1\). The other clauses are bounded by
\(L^2r_A\) and \(L^3r_J\). Small early, depth-independent radii
therefore admit every local datum to PW's regular-pair class.
No extra plaquette assumption or global extension was introduced.

P82 Lemma 1 and PW §4 control the actual iterated means and
incremental site factors. For a level-\(j\) row their induction is
\[
 u_m\le C_Lr_A L^{m-j},\qquad
 \sum_{m<j}u_m\le C_Lr_A/(1-L^{-1}),\qquad
 \prod_{m<j}(1+C_Lu_m)
       \le\exp\!\left(C_L\sum_{m<j}u_m\right).              \tag{11.2}
\]
Decrease \(r_A\) once to make the last bound at most two. Thus
PIV applies to \(V=\mathcal M^k(e^{i\eta A'})\); no fixed
\(1+C_Lr_A\) factor is multiplied once per depth. PW (4.1)–(4.6)
supplies the absolute second jets of the intervening rows.

Keep P82's flat/model input order: choose the local parametrix
size \(M_P\), the complex and arbitrary-current ceilings of PW
Proposition 5, the cut-down size/gap floors, then \(M_1,R_1\).
Decrease the independent-current ceiling once for the multiplier
bounds below. These choices precede \(\kappa,M\). Choose
\(r_A,r_J\) below the resulting early ceilings. A later proportional
decrease of primed/unprimed radii preserves their ratio floors and
changes none of the early constants.

P82 and PW use three colour coordinates. In this near-flat
application the flat inverses are scalar colour copies. Perturbation
bounds use matrix multiplication, \(\|[X,Y]\|\le2\|X\|\|Y\|\),
and finite-dimensional norm conversions. The argument consequently
works with \(N^2-1\) copies and \(N\)-dependent constants. No
non-flat SU(2) stabilizer argument is imported to SU(\(N\)).
Below, \(C_L\) inherited from these proofs may depend on this
fixed \(N\) and the early frame parameters.

### 11.2 Schur factors and both multiplier currents

Use h-walk's actual first matrix \(\mathbb K_0\), with independent
current \(J\) and coefficient current zero, and its second matrix
\(\mathbb K_1[j_0]\). Check the current convention at the
quadratic-form level. Put \(\lambda=G'RD^{\mathsf T}A\) and
\(\lambda^+(b)=\operatorname{Ad}(\mathbf U(b))\lambda(b_+)\).
CA-I 45417–45425, 46489–46504 and 46670–46690 give
\(\mathfrak S\lambda=\lambda+\lambda^+\),
\(\lambda^+-\lambda=\eta D\lambda\), and
\(\langle X,M_JY\rangle=\langle i[X,Y],J\rangle\).
Thus its half-symmetrized first correction has quadratic form
\[
\begin{split}
 W_\pi(A)
 &=\langle i[A,\lambda+\lambda^+]
          +\tfrac i2[\lambda+\lambda^+,D\lambda],J\rangle\\
 &=-\langle i[\lambda,A]-i[A,\lambda^+]
                         -i[\lambda,D\lambda],J\rangle .
\end{split}                                                    \tag{11.3a}
\]
The second equality uses
\([\lambda^+-\lambda,D\lambda]=\eta[D\lambda,D\lambda]=0\).
This is precisely minus h-walk's \(c_J\). For the constraint
correction, the quadratic form in CMP 99b (3.128), which CA
uses for its sequence operators, is
\(-2\langle H C^{(2)}(A-D\lambda),J\rangle\).
Since \(C^{(2)}=q''/2\), this is
\(-\langle A-D\lambda,E_{H^{\mathsf T}J}(A-D\lambda)\rangle\),
with PW's positive second-derivative notation \(E\).
This comparison uses the signed quadratic forms, rather than
identifying letters named \(\Delta^{(2)}\) across conventions.
The first identity is linear in \(J\). The second is an identity
for every linear map \(H\), applied pointwise to \(H(P)\);
it does not assert that \(H(P)^{\mathsf T}J\) is linear in the
independent datum \(J\). Neither identity requires a physical
current.

PW Proposition 5 and §5.1 establish the
scalar, massive-field and row Gram inverses separately. The
elimination of h-walk Lemma U, in the physical row pairing, gives
\[
 [\mathbb K_0^{-1}]_{A\nu}=H,\qquad
 [\mathbb K_1[H^{\mathsf T}J]^{-1}]_{A\nu}=H_1,\qquad
 [\mathbb K_1[H^{\mathsf T}J]^{-1}]_{\nu\nu}
             =-(QG_1Q^{\mathsf T})^{-1}.                  \tag{11.3}
\]
These are independent-current identities. The second system uses
\(j_0=H^{\mathsf T}J\); the final one-step vertex uses
\(j=H_1^{\mathsf T}J\).

For a first-system walk \(\beta\), PW (7.2) is
\[
 m_c^3|j_{0,\beta}(c)|
 \le C_Lr_J(C_L/M_1)^{|\beta|}e^{-\tau t_\beta(c)/4}.
 \tag{11.4}
\]
The physical transpose contributes \(m_c^{-4}\), the unnormalized
row source has dual norm \(m_c\), and the current norm contributes
\(m_c^3\): their product is one. Rows §5 gives the counting
multiplier and both-sided estimates. The zero-length sum
\(j_0^{(0)}\) is therefore a small analytic local coefficient for
the second matrix; positive-length terms are its branching vertices.

PW (4.5) bounds such a vertex for every coefficient current in the
ball. PW §7 proves the exact Neumann expansion and, for a trunk
with \(n\) steps, \(v\le n\) vertices and \(m_i\ge1\) branch lengths,
\[
 p=n-v+\sum_i m_i,\qquad q=n+\sum_i(m_i+1),\qquad
 3p-q=2(n-v)+2\sum_i(m_i-1)\ge0.                           \tag{11.5}
\]
Keep \(C_L^{n+\sum_i m_i}\). The bound is
\(C_L(C_LM_1^{-1/3})^q e^{-\tau t/4}\), with at most
\(C_0C_1^q\) terms per root. Apply the same transpose calculation
to the second system's \(A\nu\) output to obtain the summable
family for \(j=H_1^{\mathsf T}J\). This final branch is retained.

### 11.3 The exact one-step factors, including the gauge term

CA-I 46952–47080 uses the relative contour logarithm
\[
 \Phi_g(V,B;y,x)=\frac1i\log\!\left[
 (e^{iB}V)\langle y,x\rangle V\langle y,x\rangle^{-1}\right],
 \qquad g_VB=(\Phi_g)_1(B),\qquad
 \langle B,\mathsf G_VB\rangle=\|g_VB\|^2,                \tag{11.6}
\]
bilinearly continued in the last expression. Off the flat pair
this need not be the Hessian of the absolute soft-gauge functional
in pr-lay/HM. Use (11.6) itself as the local term.

PIV's analytic mean and inverse-contour bounds on a fixed smaller
ball give \(\|g_V\|\le C_{L,N}\). Indeed, the one-variable Cauchy
formula along each direction bounds its first coefficient by \(C/a\)
on a raw ball of radius \(a\); only \(C_{L,N}\) coarse inputs and
contour sites occur per block. Summing these finitely many
coefficients bounds both row and column sums of
\(g_V^{\mathsf T}g_V\). Its fine-data read is the complete iterated
averaging neighbourhood of those inputs, controlled by (11.2).
It gives a depth-independent length-zero majorant. We replace HM's
gauge term, without assuming equality of the two Hessians.

The pivot derivative is the actual \(C_\flat\). In raw derivative
coordinates \(J_c=L^{-3}\pi_c\), so its right inverse is
\(J_c^{-1}=L^3\pi_c^{-1}\), CA's \(h\). The quadratic coefficient
of the next-step constraint is \(C^{(2)}=q''/2\). Hence
\[
 \langle B,\mathcal J[f]B\rangle
 =-2\langle h\,C^{(2)}(B),f\rangle
 =-\langle h\,q''[B,B],f\rangle.                          \tag{11.7}
\]
This is the negative ambient constraint-current Hessian of pr-lay,
with the physical transpose. No factor two is missing. PIV bounds
\(C_\flat,h,q''\) and their full reads. Thus (11.3)–(11.7),
with the active projections in OL-W0.1, identify the sum with the
actual precision. No on-shell equation is substituted for \(J\).

### 11.4 Absolute summation and complete reads for this version

Apply the proof of HM Lemma 1 with its W supplied by PW
Proposition 5, PW (4.5), PW §7's coefficient estimates and Rows'
absolute rows/columns. Replace its local gauge term by (11.6).
The three precision families are the local
\(C_\flat^{\mathsf T}(\mathsf G-a)C_\flat\), the negative
\(\nu\nu\) block of (11.3), and the final-current vertex (11.7).
They have datum-independent majorants. After spending some decay
on intermediate pillars, the label sum at a fixed endpoint is
\[
 C_{L,N}\sum_{q\ge0}(C_{L,N}M_1^{-1/3})^q<\infty.          \tag{11.8}
\]
An early floor makes this converge. The transposed proof gives
the other half of (10.1). This uses coefficient bounds, not the
norm of a resummed inverse or HM's later root construction.

At a local evaluation include all cut-down boxes, especially the
boxes read by \(j_0^{(0)}\), and the averaging, normalized-cutoff,
pivot and contour reads. A zero-length current box meets its row
and is within \(O_L(M_1)\) of its parent cell. On the trivial nest,
fixed grids and these complete data determine the finite matrices
and cutoffs. Equal reads in a non-wrapping common lift give equal
coefficients. This is fixed-region locality, not h-walk's rejected
claim about traces of different nested regions. No extension of a
local datum is used.

Enlarge each parent domain to include these reads. Consecutive
domains still meet and have diameter at most an early
\(\rho_u=O_L(M_1)\). Enlarging a domain decreases the shortest
length needed to meet it. The root's fixed pivot/row offset from
the endpoint costs only an \(L,N\)-dependent factor, not
\(e^{cM_1}\) per step. This converts HM's tree weight to CA-I
4875–4907's weight. Transpose partners can use the same enlarged
hull and half of each coefficient. The unfolded version thus has
the local, early-constant and absolute-majorant properties of
OL-W0 on the admitted tori.

**Outcome of attack 7.** The frozen proofs supply the needed
complex current estimate for an unfolded expansion of the actual
matrix, with (11.6) as its local gauge term. What this attack does
not prove is the absolute transfer to CA's successive sheet
assignment. A different good expansion cannot silently be
substituted for the family specified in OL-W0.

## 12. New attack 8: a label-preserving Schur resummation

The natural next attempt is to eliminate the auxiliary variables
**inside the local walk expansion**, retaining every label. This
would relate the unfolded proof to CA's successive construction.

For an ordinary block matrix, with the indicated inverses existing,
\[
 \mathbb K=\begin{pmatrix}E&B\\ C&D\end{pmatrix},
 \qquad
 [\mathbb K^{-1}]_{11}=(E-BD^{-1}C)^{-1}.                  \tag{12.1}
\]
Multiplication verifies (12.1): solve \(Cx+Dy=g\) for
\(y=D^{-1}(g-Cx)\), substitute into \(Ex+By=f\), and obtain
\((E-BD^{-1}C)x=f-BD^{-1}g\).
Section 11 supplies the required inverses in this application.
Thus eliminating after **summing** the unfolded walks recovers
the actual successive Schur operators. This part of the attack
works, also at independent complex currents.

Here is the quantitative criterion needed to eliminate before
absolute summation. Suppose a refinement of the unfolded family
has terms \(u_\zeta\), with the same bound as §11, and the CA
coefficient has an exact local identity
\[
 A^{\rm CA}_\omega(b,b';P)
       =\sum_\zeta c_{\omega\zeta}(b,b';P)u_\zeta(b,b';P).
                                                               \tag{12.2}
\]
Every summand must be readable from \([\omega]\).
If numbers \(C_{\omega\zeta}\) dominate
\(|c_{\omega\zeta}|\) on those local balls and
\[
 \sup_{\zeta,b,b'}\sum_\omega C_{\omega\zeta}
   e^{\delta d_{\rm CA}(\omega;b,b')
      -\delta_u d_u(\zeta;b,b')}\le C_* ,                 \tag{12.3}
\]
then the triangle inequality, followed by interchange of
nonnegative sums, gives
\(\|A^{\rm CA}\|_{\mathrm{abs},\delta}
 \le C_*\|u\|_{\mathrm{abs},\delta_u}\).
This proves a sufficient transfer criterion. It also specifies
the full-read and multiplicity costs that a purported regrouping
must pay.

Equation (12.1) does not prove (12.2)–(12.3). To see exactly where
the tempting formal argument fails, mark each local transition by
an independent variable \(z_\alpha\). The unfolded expansion then
has monomials recording its local-system transitions. CA instead
marks the elementary scalar/field sheets, local comparison
remainders, the second-cover inversion, and the two current
branches. The identity (12.1) at all \(z_\alpha=1\) is not an
identity of these two marked functions.

In particular the primitive cancellation
\[
 R=I-X(X^{\mathsf T}X)^{-1}X^{\mathsf T}
\]
at real data is changed, when its three factors receive independent
marks, into \(I-z_1z_2z_3P\), where
\(P=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}\).
Choosing \(z_1z_2z_3=-1\) changes it by \(2P\), even at the flat
pair. This is an order-one change, not the small field perturbation
admitted by PW Proposition 5. The exact local congruence cannot
therefore be invoked for arbitrary marks merely by taking
\(r_A,r_J\) smaller. This observation does not assert that all
marked systems are singular; it identifies the missing hypothesis
in that proposed proof.

Nor is there an abstract absolute-sum theorem behind (12.1).
For \(0<t<1\),
\[
 1=\sum_{n\ge0}t^n-\sum_{n\ge1}t^n,\qquad
 \sum_{n\ge0}|t^n|+\sum_{n\ge1}|-t^n|
       =\frac{1+t}{1-t}.                                 \tag{12.4}
\]
The first family consisting just of \(1\) has absolute norm one.
The second has the same sum and an arbitrarily large absolute
norm. Taking \(t_k=1-L^{-k}\) makes the latter
\(2L^k-1\). These are constant analytic functions of the field,
so field holomorphy does not repair the implication. This is a
test of a proposed inference, not a counterexample to CA's family
or to the one-loop lemma.

The source's successive construction does perform cancellations
before assigning some of its labels. In CMP 99b pp. 414–415,
(3.105) expands a comparison involving \(DPD^*\).
Its principal local term is moved through cutoff factors until
it cancels the corresponding \(DP_\square D^*\) term.
The discarded differences become separate remainder labels.
Thus neither treating every factor as an independent mark nor
retaining only their cancelled total gives its assigned family.
A legitimate transfer has to estimate these remainder labels,
with their reading hulls, before invoking (12.3).

**Outcome of attack 8.** Exact Schur resummation establishes
identity of the summed operators. The attempted label transfer
fails at (12.3): no uniform positive redistribution estimate for
the actual local-comparison labels has been proved. No claim that
such an estimate is false is made.

## 13. New attack 9: keep cancellation at the singular junction

This attack uses the mixed energy/regularity estimates of PW
directly on the account's difficult word, rather than splitting
its kernel into absolute values as in round two. The word at
CA-I 47389–47394 is
\[
 \mathfrak b=(DG')(D^{\mathsf T}G_0D)(G'D^{\mathsf T}).
                                                               \tag{13.1}
\]
Work first at \(J=0\) on a fixed admitted cut-down, in its physical
pairings. Let \(E\) be the field energy space and \(A_s=G'^{-1}\).
PW §5.1 supplies the uniform scalar coercivity/inverse estimates;
its row-multiplier-deleted system supplies \(G_0:E^*\to E\).
Since
\[
 |\langle Du,A\rangle|=|\langle u,D^{\mathsf T}A\rangle|
           \le C\|u\|_2\|A\|_E ,
\]
\(D:L^2\to E^*\) and \(D^{\mathsf T}:E\to L^2\) are bounded.
The scalar estimates and their transposes likewise give
\(DG':L^2\to L^2\) and \(G'D^{\mathsf T}:L^2\to L^2\).
Consequently
\[
 \|D^{\mathsf T}G_0D\|_{2\to2}\le C_L,\qquad
 \|\mathfrak b\|_{2\to2}\le C_L.                           \tag{13.2}
\]
On varying local scales these are the same inequalities in the
scaled energy spaces; at the trivial nest the largest scale is
one. Finite-dimensional transpose duality also proves them at
the admitted complex perturbations. There is no sum of
\(|x|^{-4}\) kernels and no logarithmic loss in (13.2).

Smooth junctions have an exact algebraic advantage. For a smooth
cutoff \(\chi\),
\[
 [G',\chi]=-G'[A_s,\chi]G',\qquad
 [G_0,\chi]=-G_0[T_0,\chi]G_0,\quad T_0=G_0^{-1},
                                                               \tag{13.3}
\]
and
\[
 [D^{\mathsf T}G_0D,\chi]
 =D^{\mathsf T}G_0[D,\chi]
  +D^{\mathsf T}[G_0,\chi]D
  +[D^{\mathsf T},\chi]G_0D.                              \tag{13.4}
\]
Each identity follows by multiplying out the two sides. For the
local unfolded matrix, PW (6.10)–(6.13) proves the corresponding
\(C_L/M_1\) commutator estimate with two controlled cutoff
differences: the divergence source and
\(p=h'+D^{\mathsf T}A/2\) keep the apparently third-order term
from demanding another derivative of the background. This is
substantially more information than the gap argument of round
two. It bounds the resummed junction and the unfolded local
remainder without discarding its cancellation.

The obstruction is exposed by the middle term of (13.4).
The successive scheme does not localize \(T_0\) as one finite-range
matrix: it contains \(DRD^{\mathsf T}\), and \(R\) contains the
site inverse and its Gram inverse. At this point its construction
inserts their assigned sheet expansions and local comparison
differences. Its singular-word statement asks for orders
\((1,0,1)\) and smooth junctions **for those terms**. Neither
(13.2) nor the identity (13.3) bounds the sum of the norms of those
separately labelled differences.

One can make a finer attempted use of PW: apply its local
\(W^{2,8}\) estimate to each elementary kernel and use Morrey's
inequality at the junction. Its source normalization shows why
this is not yet the required bound. For the fine point source
representing a unit mass in the physical pairing,
\[
 f_\eta(x)=\eta^{-4}{\bf1}_{x=x_0},\qquad
 \|f_\eta\|_{L^8(\eta^4{\rm count})}
       =(\eta^4\eta^{-32})^{1/8}=\eta^{-7/2}.              \tag{13.5}
\]
PW's represented-source estimate applied this way has this
factor. The row source used in (11.4) has uniformly bounded
scaled norm; the fine delta does not. Extracting individual
elementary kernels therefore needs their scale-dependent
singular estimates and the cancellation at the smooth junction,
before the internal fine coordinates are summed. PW's coarse
row bound cannot simply be used with a unit right-hand side at
each such coordinate. Equation (13.5) is not a lower bound on the
true kernel and does not disprove a uniform result.

For comparison, on a common space where \(S_X,S_Y\) are two
local inverses, the exact identity
\[
 S_X-S_Y=S_X(K_Y-K_X)S_Y                                  \tag{13.6}
\]
does turn a distant change of coefficients into a small
resummed comparison, using supported-source decay. With
Dirichlet domains, this identity must be applied after the
extension/restriction maps and boundary commutators have been
specified. CA/Bałaban's successive construction resolves the
right side into particular letters and repeats this operation
inside the Gram inversion. To use (13.6) here would require
an absolute bound for that resolution, with all its boundary
and current reads. Replacing the right side by a single bounded
label would construct a new family, as in §11, rather than prove
the bound for the specified one.

**Outcome of attack 9.** The singular word is bounded in the
correct energy spaces, and the smooth-cutoff calculation avoids
round two's spurious logarithmic loss. The attempt still stops at
a specific coefficient-level step: estimating the absolute family
produced when the local comparisons in (13.3)–(13.6) are expanded
into the account's successive sheets. An operator estimate for
the resummed comparison does not supply that estimate. This is
the same remaining obligation as §12, approached through the
actual singular junction rather than formal Schur elimination.

## 14. Current checkpoint, source identities and limits

This checkpoint supersedes §9 as the recovery point. The earlier
arguments and endpoints are preserved as historical rounds.

The new proved implication is §11: the frozen flat/model inputs,
PW's complex coefficient proof, Rows and PIV give an intrinsic
absolute expansion of the **actual** free-current precision,
with its relative contour gauge and both current branches,
uniform in depth on an early local flat ball. Its assignment is
the repaired unfolded one. It supplies more than a real flat
propagator bound or an estimate of the summed matrix.

The remaining obligation is OL-W0 for the account's successive
assignment. Attack 7 reaches the correct matrix with different
labels. Attack 8 verifies the exact Schur identity but does not
control the absolute redistribution of labels. Attack 9 bounds
the singular word without the old logarithmic loss but does not
bound the prescribed, separately expanded comparison terms.
Equations (12.3) and (13.3)–(13.6) locate the next calculation.
These are three attacks on one obligation, not three new axioms
or three independent verifications.

The family qualification matters. CA-I 4869 onward defines a
walk system by its sum; there is freedom to construct walk
systems. That definition alone does not identify the activities
of two systems after footprint restrictions, local inversion and
localization of the logarithm. The Route at CA-I 3932–3945 and
the construction being ported use their chosen local terms.
This note has not proved that replacing them by §11's terms
preserves that assigned family. OL-W0 remains a sufficient route
chosen in round two; no necessity claim or no-go conclusion about
other legitimate localizations is made.

No further bulk coefficient calculation is indicated by this
round. The coefficient remains
\(c_0=11N^2\log L/(12\pi^2)\); the unresolved step is the
analytic/local realization needed to apply the preserved
calculation to the assigned Gaussian family. If OL-W0 is supplied,
§8 gives OL-loc and the transfer to §§2–3. Its determinant and
comparison constants are still chosen at the early stage and
the finite part is \(c_2(L,N)\), not a number allowed to grow
with \(k\) or the late localization size.

**Source record.** Checkout:
\( \texttt{d073927c08564435973eb8d54558e0571798e10e}\).
The outline and complete-account files are the pinned revision
31a47c543775. Navigation used the index README, neighbouring
rows in outline chunks 04, 07, 10 and 11, obligations.md, and
the CA 4.12–4.19 index, particularly the elementary-sheet and
assembly rows in its chunk 04 and the one-loop/A12 rows in its
chunk 11. Bounded source passages used in this round include:

- SA 3986–4004, 10129–10185, 10533–10562, 11510–11541:
  obligation, independent-current conventions, unfolded route,
  branches and actual averaging.
- CA-I 3585–3610, 3764–4030, 4610–4907, 45236–45440,
  46489–46508, 46538–46562, 46658–46715, 46952–47080,
  47275–47645, 56342–56375 and 56419–56495: target and uses,
  local data, actual precision, unit maps and successive assembly.
- CA-II 8922–8990 and 27042–27082: cited walk input and the
  one-loop law that assumes this lemma.
- Local CMP 99b pp. 413–416, 419–423 and 427–428, with Theorem 3.15;
  CMP 109 (1.22) and Theorem 3. The CMP 116 statements are
  used only in the form quoted by the account; its paper is
  not present in the permitted local paper folder.

The complete list of literal occurrences of the one-loop label
in the three CA files is CA-I 3603, 3876, 3903, 56363, 56428
and 56466. Each occurrence and its relevant surrounding use was
checked. The large files were not read whole. Credit remains
with Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text, and Tadeusz Bałaban for the cited
propagator and RG construction.

The pre-round recovery copy is
/tmp/ol-round3-d073927c0/ol-before.md. Source hashes and text
integrity checks are recorded in
/tmp/ol-round3-d073927c0/verification.json.
Only library/ol.md is edited; no prompt, planning or audit file
is changed. Downloading, navigation, hashing and text checks are
bookkeeping. No numerical experiment, enumeration or
computer-assisted estimate discharges any assertion here.
The new arguments have not received an independent referee check.

## Result

**Open lemma**

**OL-W0 for the account's successive sheet assignment.** Fix
\(d=4\), \(N\ge2\), an admitted odd \(L\), and the early
operator-frame parameters in the account's order, before
\(\kappa,M\). There exist \(r_A,r_J,\delta,B,\rho_w>0\),
depending only on these early choices and \(L,N\), such that,
uniformly for \(k\ge1\) and all admitted tori at the trivial
nest, the account's successive word/Dirichlet-sheet construction
CA-I 47294–47584 for
\[
 A_k(P)=C_\flat(P)^{\mathsf T}
 \left(P_\Lambda[Q(P)G_1(P)Q(P)^{\mathsf T}]^{-1}P_\Lambda
       -a+\mathcal J[H_1(P)^{\mathsf T}J](P)
       +\mathsf G(P)\right)C_\flat(P)
\]
has locally defined holomorphic coefficients
\(A^{\rm CA}_{k,\omega}\), with the following absolute bound:
\[
 \sup_{k,\mathbb T}
 \max\!\left\{
  \sup_b\sum_{\omega,b'},\ \sup_{b'}\sum_{\omega,b}
 \right\}
 e^{\delta d(\omega;b,b')}
 \sup_{\substack{P=(e^{i\eta A'},J)\ {\rm on}\ [\omega]\\
                 |A'|,|\nabla^\eta A'|<r_A,\ |J|<r_J}}
 |A^{\rm CA}_{k,\omega}(b,b';P)|\ \le B .                 \tag{OL-W0-CA}
\]
The potential/current units are CA-I 4610–4703's scale-normalized
units. Every complete read includes the averaging carriers,
local inverse boundary stencils, both multiplier branches and
pivot/relative-contour factors. Step domains have diameter
at most \(\rho_w\), consecutive domains meet, and
\(d(\omega;b,b')\) is CA-I 4875–4907's shortest-tree length.
Equal complete reads in non-wrapping common lifts give equal
coefficients. On global data their sum is exactly \(A_k(P)\).
The local supremum does not assume a global extension or an
additional plaquette hypothesis. The constants are independent
of \(k\), torus volume, \(M\) and coupling; subsequent permitted
radius decreases preserve the bound.

The bound is proved in §11 for the repaired unfolded assignment,
under its frozen flat/model inputs. Its transfer to the specified
CA assignment remains unproved after the three new attacks.
There is no counterexample to the one-loop lemma here. The
account's full one-loop statement, and hence T0, is not claimed
proved by this note.
