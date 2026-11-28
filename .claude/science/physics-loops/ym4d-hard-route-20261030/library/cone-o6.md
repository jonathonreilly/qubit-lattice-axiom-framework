# The spectral cube cone (row 195)
Provenance: Codex (GPT-6; exact runtime variant and effort unavailable; requested effort max), checkout `9cbf5ba58e3373146c1fe2f40a7e2e874e72ebfa`, Sussman–Alpoge commit `31a47c543775`. Research text; not an audit; grants no status.

## 1. Inputs and source

The target is O6: \(H\ge |P_j|\) for \(j=1,2,3\), on the OS Hilbert space of [s4-s6.md](s4-s6.md).
Its Result supplies O4 and O5, conditional on its cutoff sequence, S3 and S1g.
It also supplies translations, \(W_4\), and continuous moments on separated compact tuples.
No full rotation invariance is an input.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Sources are their [YM4 outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), L25736–25904,
and [YM3_I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), L75249–75578, at the pinned source commit.
We rebuild Y3 IV-28-17 and IV-28-21, which compare two continuum reflection forms directly.

## 2. The diagonal Hilbert space

Fix \(j\in\{1,2,3\}\). Put \(u=(e_4+e_j)/\sqrt2\), \(v=(e_4-e_j)/\sqrt2\).
Let \(\mathcal D_u\) span separated compact tuples in \(u\cdot x>0\), including the empty tuple.
Write \(\theta_u x=x-2(u\cdot x)u\).
O5 makes
\[
 q_u(F,G)=\sigma(\theta_u\bar F\cdot G)
\]
positive. Polarization gives Hermiticity; positivity of \(q_u(F+zG,F+zG)\) gives Cauchy–Schwarz.
Complete its quotient by null vectors to obtain \(\mathcal H_u\).

Here is the needed reconstruction, as in Y3 IV-27-22.
Set \(a_F(t)=\|\tau_{tu}F\|_{q_u}\).
The position-independent moment bounds from [s4-s6.md](s4-s6.md), (2), give \(a_F(t)\le C_F\) for \(t\ge0\).
Indeed, internal separations stay fixed, and opposite-side separations cannot decrease:
\[
 |y+ru-x|^2=|y-x|^2+2r\,u\cdot(y-x)+r^2\ge |y-x|^2
 \quad(u\cdot x<0<u\cdot y,\ r\ge0).
\]
Individual support radii and test norms stay fixed.
Translation invariance and Cauchy–Schwarz give
\[
 a_F(t)^2=q_u(F,\tau_{2tu}F)\le a_F(0)a_F(2t),\qquad
 a_F(t)\le a_F(0)^{1-2^{-m}}C_F^{2^{-m}}.
\]
The first inequality handles \(a_F(0)=0\); otherwise let \(m\to\infty\).
Thus normal translations preserve null vectors and extend as symmetric contractions \(T_t^u\).
Symmetry follows from \(\theta_u\tau_{tu}=\tau_{-tu}\theta_u\) and translation invariance.
The bounded symmetric extensions are self-adjoint.
Their semigroup law gives \(T_t^u=(T_{t/2}^u)^2\ge0\).
Tangential translations preserve \(q_u\), have inverse translations, and give commuting unitaries \(U^u(sv)\).

Continuity of the separated moments makes these maps strongly continuous on tuple classes:
\[
 \|(T_t^u-I)[F]\|^2=q_u(F,\tau_{2tu}F)-2\operatorname{Re}q_u(F,\tau_{tu}F)+q_u(F,F)\to0,
\]
and the unitary formula has the two terms \(2q_u(F,F)-2\operatorname{Re}q_u(F,\tau_{sv}F)\to0\).
Uniform operator bounds extend continuity to the completion.
If \(T_1^ua=0\), positivity gives \(T_{1/2}^ua=0\); iteration and continuity give \(a=0\).
Hence spectral calculus defines \(H_u=-\log T_1^u\ge0\).
Unique positive roots give \(T_t^u=e^{-tH_u}\) for dyadic \(t\), then for all \(t\ge0\).
Write \(U^u(sv)=e^{-isQ}\), choosing the negative of its momentum generator for \(Q\).
These use the same spectral calculus as O4, with no rotation covariance assumption.

## 3. The measure estimate

Let \(\mu\) be a finite positive measure on \([0,\infty)\times\mathbb R\), and set \(w=(E-iq)/\sqrt2\).
Suppose vectors \(a,b\) and self-adjoint operators \(A\ge0,B\) satisfy
\[
 \int e^{-sw-s'\bar w}\,d\mu=\langle a,e^{-sA}e^{-is'B}b\rangle
 \quad(s,s'\ge0). \tag{1}
\]
We prove \(\mu\{|q|>E\}=0\).
For \(c\in L^1(0,\infty)\), put \(p(z)=\int_0^\infty c(s)e^{-sz}\,ds\).
Integrate (1) against \(c(s)\overline{c(s')}\).
Fubini applies: the left kernel has modulus at most one, and both operators on the right have norm at most one.
Spectral calculus gives, with \(C=\|a\|\|b\|\) and \(p^\sharp(y)=\overline{p(-iy)}\),
\[
 \int|p(w)|^2\,d\mu
 =\langle a,p(A)p^\sharp(B)b\rangle
 \le C\sup_{x\ge0}|p(x)|\sup_{y\in\mathbb R}|p(iy)|. \tag{2}
\]
No commutation between \(A\) and \(B\) is used.

Take \(\alpha=\varepsilon+i\kappa\), \(\varepsilon,\eta>0\), \(\kappa\in\mathbb R\), and
\[
 c(s)=\frac{s^{\alpha-1}e^{-\eta s}}{\Gamma(\alpha)},\qquad
 p(z)=(z+\eta)^{-\alpha}. \tag{3}
\]
Here is a hand justification of the normalization and transform.
Define \(\Gamma(\alpha)=\int_0^\infty t^{\alpha-1}e^{-t}\,dt\).
Integration by parts in \(\int_0^1t^{\alpha-1}(1-t)^Ndt\), followed by \(t=s/N\), gives
\[
 \Gamma(\alpha)=\lim_{N\to\infty}
 \frac{N!N^\alpha}{\alpha(\alpha+1)\cdots(\alpha+N)}\ne0. \tag{4}
\]
Dominated convergence proves the limit, since \((1-s/N)^N\le e^{-s}\) on \(0\le s\le N\).
For nonvanishing, the product equals
\(\alpha^{-1}N^\alpha\prod_{k=1}^N(1+\alpha/k)^{-1}\).
A logarithm of this product converges to a finite number.
Indeed, \(\sum_{k=1}^Nk^{-1}-\log N\) is nonnegative and decreasing, by comparison with \(\int_N^{N+1}dt/t\).
For the logarithmic tail, use
\[
 \log(1+z)-z=-z^2\int_0^1\frac{t}{1+tz}\,dt,\qquad
 |\log(1+z)-z|\le |z|^2\quad(|z|\le\tfrac12).
\]
Taking \(z=\alpha/k\) gives an absolutely summable tail.
Thus its limit is a nonzero exponential.
Substitution proves (3) for positive real \(z+\eta\).
Both sides are holomorphic for \(\operatorname{Re}(z+\eta)>0\), so the identity theorem proves (3) there.
Holomorphy of the integral follows by differentiation under its exponentially integrable majorants.
Also \(c\in L^1\), since \(\varepsilon,\eta>0\).

Use the principal argument in (3). Its two suprema in (2) are bounded by
\(\eta^{-\varepsilon}\) and \(\eta^{-\varepsilon}e^{|\kappa|\pi/2}\).
Consequently
\[
 \int |w+\eta|^{-2\varepsilon}e^{2\kappa\arg(w+\eta)}\,d\mu
 \le C\eta^{-2\varepsilon}e^{|\kappa|\pi/2}.
\]
Fatou first as \(\varepsilon\downarrow0\), then as \(\eta\downarrow0\), gives
\[
 \int_{w\ne0}e^{2\kappa\arg w}\,d\mu\le Ce^{|\kappa|\pi/2}. \tag{5}
\]
For \(\delta>0\), the set \(\arg w\ge\pi/4+\delta\) has measure at most \(Ce^{-2\kappa\delta}\) for every \(\kappa>0\).
Let \(\kappa\to\infty\). Use \(\kappa\to-\infty\) for \(\arg w\le-\pi/4-\delta\).
Take the union over \(\delta=1/m\), \(m\ge1\).
Since \(\operatorname{Re}w\ge0\), these sets cover precisely \(|q|>E\), proving the estimate.

## 4. Comparing the two reflections

Let \(\theta=\theta_{e_4}\), \(r=\theta_u\theta\), and \(W_j=\{x:x_4>|x_j|\}\).
For \(F\) in the span of separated compact tuples in \(W_j\), both \(F\) and \(rF\) belong to \(\mathcal D_u\):
\[
 u\cdot x=(x_4+x_j)/\sqrt2>0,\qquad
 u\cdot rx=(x_4-x_j)/\sqrt2>0.
\]
Let \(\mathsf E\) be O4's joint spectral measure for \((H,P_1,P_2,P_3)\).
Push \(\langle[F],\mathsf E(\cdot)[F]\rangle\) forward by \((E,p)\mapsto(E,p_j)\), obtaining \(\mu_F\).
It is positive and finite, with total mass \(\|[F]\|^2\).
For \(s,s'\ge0\), one correlation has the two representations
\[
 \begin{aligned}
 \int e^{-sw-s'\bar w}\,d\mu_F
 &=\sigma\bigl(\theta\bar F\cdot\tau_{su+s'v}F\bigr)\\
 &=\bigl\langle[rF]_u,e^{-sH_u}e^{-is'Q}[F]_u\bigr\rangle_u,
 \qquad w=(E-ip_j)/\sqrt2. \tag{6}
 \end{aligned}
\]
The first equality uses
\(su+s'v=((s+s')e_4+(s-s')e_j)/\sqrt2\) and O4's translation formula.
The second uses \(\theta_ur=\theta\) and the defining form \(q_u\).
Every product is defined: the coordinate halves remain separated, and the right factor stays in \(u\cdot x>0\).
The map \(r\) only changes test arguments; no invariance under \(r\) is assumed.

Section 3 applied to (6) gives \(\mu_F\{E<|p_j|\}=0\).
Thus the joint spectral projection \(\Pi_j=\mathsf E\{E<|p_j|\}\) annihilates \([F]\), since
\(\|\Pi_j[F]\|^2=\mu_F\{E<|p_j|\}\).

Now let \(F\) be any finite positive-time tuple combination.
Compactness permits \(R\ge0\) such that every support of \(\tau_{Re_4}F\) lies in \(W_j\).
Hence \(\Pi_jT_R[F]=0\).
Joint spectral calculus gives \(\Pi_jT_R=T_R\Pi_j\), and \(T_R\) is injective because \(e^{-RE}>0\).
Therefore \(\Pi_j[F]=0\). These classes are dense, so \(\Pi_j=0\).
Doing this for the three indices proves
\[
 \mathsf E\{(E,p):E<\max_{1\le j\le3}|p_j|\}=0. \tag{7}
\]
Write \(\mu_\psi(B)=\langle\psi,\mathsf E(B)\psi\rangle\).
For \(\psi\in\operatorname{Dom}H^{1/2}\),
\[
 \psi\in\operatorname{Dom}|P_j|^{1/2},\qquad
 \||P_j|^{1/2}\psi\|^2
 =\int|p_j|\,d\mu_\psi\le\int E\,d\mu_\psi
 =\|H^{1/2}\psi\|^2. \tag{8}
\]
Integrating \(p_j^2\le E^2\) also gives
\(\operatorname{Dom}H\subset\operatorname{Dom}P_j\) and \(\|P_j\psi\|\le\|H\psi\|\).
The bridge in [s4-s6.md](s4-s6.md), Section 7, identifies this completion with the extended OS space.
It intertwines translations, so (7) and (8) hold there too.

## 5. Dimension and the first input

The comparison uses only the plane \((x_4,x_j)\); the other two coordinates stay fixed.
Y3 uses \(x_3\) as time, one spectator coordinate, and two spatial generators.
In four dimensions there are two spectator coordinates and three spatial generators.
The factor \(\sqrt2\), the wedge, and the measure estimate do not change.
The supplied moment constants may depend on dimension; this argument needs no new bound.

**First failing input within the stated premises: none.**
The position-independent separated-moment bound is used in Section 2; abstract operator positivity alone would not supply that step.
Here [s4-s6.md](s4-s6.md), (2) and Result, supplies it together with O4 and O5.
For unconditional T0, the first unproved source input remains **D1**, beginning with **C1/OH1** in its cited construction.
This is the boundary recorded in [d2-d4.md](d2-d4.md), Result, and [s4-s6.md](s4-s6.md), Section 8.
E1 must also supply the cutoff sequence. This proof does not establish those inputs.

## Result

**Given the Result of [s4-s6.md](s4-s6.md), O6 follows:**
\[
 H\ge |P_j|\quad(j=1,2,3)
\]
on its OS Hilbert space, in the joint spectral and quadratic-form senses of (7)–(8).
This supplies the cube cone read by S8 and S9.
The proof ports Sussman–Alpoge's Y3 IV-28-17/21, with the authorship credit stated above.
Proved by Codex as a research implication; not yet checked by the other model.
Every step is by hand. No audit or scientific status is granted.
