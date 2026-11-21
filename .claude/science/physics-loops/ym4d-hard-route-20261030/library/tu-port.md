# Two-point rotation invariance in four dimensions (row 199)
Provenance: OpenAI Codex (GPT-6; effort not exposed); checkout `f10a6da8b29f470dcb00ab34e9c3f78d9a29daa6`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; no status granted.

## 1. Claim, sources and premises

The target is S10: every nonconstant two-point harmonic vanishes, including the critical frequency.
We assume AK from [ak-port.md](ak-port.md), coordinate and diagonal reflection positivity O5, and TU10 (S16).
All premises concern the same separated limiting correlations.
TU10 supplies a uniform bound tending to zero on its prescribed short-distance shape class.
It remains a named premise; [tu10.md](tu10.md), Section 4, does not prove its interacting inputs.
The [s4-s6.md](s4-s6.md) Result supplies the common limiting and Hilbert-space setting conditionally.

Sources: [SA outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), TU, lines 29922–30499, especially 30071–30470; [YM3_I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), lines 75872–76220.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text.
Both sources are pinned to `31a47c543775`.
The deductions below are by hand.

## 2. The axis measure

Write \(y=(t,x)=(x_4,x_1)\), \(z=(x_2,x_3)\), and \(\theta(t,x)=(-t,x)\).
Let \(R_\alpha\) rotate the \(y\)-plane counterclockwise.
Use the connected \(S_2\) of TU10 throughout.
In AK, replace \(B_{\varphi;a}\Omega\) by \(\zeta_{\varphi,a}=(1-P_\Omega)B_{\varphi;a}\Omega\).
The vacuum projection commutes with translations. Thus AK's semigroup identities survive this subtraction.
Centered reflection positivity follows by subtracting the vacuum component in each reflection Hilbert space.

For real \(\varphi,\psi\in C_c^1(\mathbb R^2)\), AK gives
\[
 S_2(\alpha\otimes\varphi,\beta\otimes\psi)
 =\iint\alpha(y)\beta(y')G_{\varphi,\psi}(y'-y)\,dy\,dy',
 \qquad
 G_{\varphi,\psi}(t,x)
 =\langle\zeta_{\varphi,a},e^{-(t-2a)H+ixP_1}\zeta_{\psi,a}\rangle
 \quad(t>2a).                                      \tag{1}
\]
The first formula holds for disjoint planar supports.
Indeed, partition them into pieces of diameter below one quarter of their separation.
Each pair is ordered along one signed coordinate. Sum AK's ordered formula over those pairs.
Every distinct planar pair lies in an AK chart, so \(G\) is continuous away from zero.
Shrinking planar test bumps transfers translations, reality, symmetry, coordinate reflections and quarter turns to \(G\).

Fix a real label and write \(G=G_{\varphi,\varphi}\).
Let \(\Pi\) be the joint spectral measure of \((H,P_1)\), and set
\[
 d\mu=e^{2aE}\,d\langle\zeta_{\varphi,a},\Pi(E,q)\zeta_{\varphi,a}\rangle,
 \qquad \mathcal C=\{E\ge|q|\}.
\]
AK gives \(\zeta_{\varphi,b}=e^{-(b-a)H}\zeta_{\varphi,a}\), so \(\mu\) is independent of \(a\).
It is positive and supported on \(\mathcal C\), since AK includes O6.
For \(t>0\), choose \(a<t/2\) in (1). Then
\[
 G(t,x)=\int_{\mathcal C}e^{-tE+ixq}\,d\mu,
 \quad \Gamma(t):=G(t,0)<\infty,
 \quad |G(y)|\le\Gamma(|y|/\sqrt2).                 \tag{2}
\]
The last bound uses a quarter turn with positive time at least \(|y|/\sqrt2\).

For a planar profile \(\alpha\) supported at positive time, reflection positivity gives
\[
 \|[\alpha\otimes\varphi]\|^2
 =\int\left|\int\alpha(t,x)e^{-tE+ixq}\,dt\,dx\right|^2d\mu.
                                                               \tag{3}
\]
Fubini is valid: if \(t\ge\delta>0\) on the support, the absolute integral is at most
\(\|\alpha\|_1^2\Gamma(2\delta)\).
This seminorm obeys the triangle inequality by positivity and Cauchy–Schwarz.

## 3. TU10 gives the strict endpoint bound

Here TU10 means \(0\le S_2(f,h)\le u(d)\|f\|_\infty\|h\|_\infty\) for \(0<d\le d_0\).
The function \(u\) is finite, nonnegative, and tends to zero at zero.
Its class uses \(\vartheta_*=1/12000\), or a smaller parameter.
Each test is nonzero and nonnegative, supported in a radius-\(d\) ball.
The support distance lies in \([d,6d]\); each test satisfies
\(\int f\ge\vartheta_*\|f\|_\infty d^4\) and
\(\operatorname{Lip}f\le\|f\|_\infty/(\vartheta_*d)\).
We verify this class before applying TU10.

Use the following fixed \(C^1\) functions.
Let \(a=1\) on \([9/4,11/4]\), zero outside \([17/8,23/8]\).
On each intervening interval use the rescaled cubic \(3s^2-2s^3\), increasing or decreasing.
Thus \(0\le a\le1\), \(\int a=5/8\), and \(\|a'\|_\infty\le12\).
Put
\[
 b(s)=
 \begin{cases}1-3s^2+2|s|^3,&|s|\le1,\\0,&|s|>1.\end{cases}
\]
Direct integration and differentiation give \(\int b=1\), \(0\le b\le1\), and \(\|b'\|_\infty\le3/2\).
For \(0\le s\le1\), \(b(s)+b(1-s)=1\), so \(\sum_{j\in\mathbb Z}b(s-j)=1\).
Let \(\rho=1\) on \([-1,1]\), with cubic ramps to zero at \(\pm3/2\).
Then \(\int\rho=5/2\) and \(\|\rho'\|_\infty\le3\).
Set \(\psi(z)=b(z_1)b(z_2)\) and \(\widetilde\psi(z)=\rho(z_1)\rho(z_2)\).
Their gradient bounds are \(3,6\), respectively; \(\psi\le\widetilde\psi\) and \(\int\widetilde\psi=25/4\).

For \(\varphi\ne0\), fix \(R\ge1\) with \(\operatorname{supp}\varphi\subset B(0,R)\).
Take \(0<h\le\min(1,2d_0/5)\), and put
\[
 \alpha_h(t,x)=a(t/h)b(4x/h),\quad
 A=\|\varphi\|_\infty+h\|\nabla\varphi\|_\infty,\quad
 f_i^-=\alpha_h\otimes(2A\widetilde\psi_i),\quad
 f_i^+=\alpha_h\otimes(2A\widetilde\psi_i+\psi_i\varphi),
 \quad \psi_i(z)=\psi(z/h-i).                         \tag{4}
\]
Define \(\widetilde\psi_i\) in the same way.
Keep only indices with \(\psi_i\varphi\ne0\).
Their number \(N\) is at most \((2R/h+3)^2\le25R^2h^{-2}\).
The partition identity gives \(\alpha_h\otimes\varphi=\sum_i(f_i^+-f_i^-)\).
Each transverse factor lies between \(A\widetilde\psi_i\) and \(3A\widetilde\psi_i\).
Consequently \(A\le\|f_i^\pm\|_\infty\le3A\).

Take \(d=5h/2\). Each support lies within that radius of \((5h/2,0,hi)\):
the squared coordinate half-widths sum to at most \(5h^2<d^2\).
Its distance from its time reflection lies between \(4h\) and \(6h\).
Moreover,
\[
 \int f_i^\pm\ge {125\over128}Ah^4
       \ge {1\over120}\|f_i^\pm\|_\infty d^4,\qquad
 \operatorname{Lip}f_i^\pm
 \le[3(12+6)+12+3+1]A/h
 =70A/h
 \le{\|f_i^\pm\|_\infty\over\vartheta_*d}.             \tag{5}
\]
The integral is the product \((5/8)(1/4)(25/4)Ah^4\).
The derivative bound uses the product rule and \(h\|\nabla\varphi\|_\infty\le A\).
Reflected tests have the same bounds. Thus \((\theta f_i^\pm,f_i^\pm)\) belongs to TU10's class.
Its bound and the Hilbert triangle inequality yield
\[
 \|[\alpha_h\otimes\varphi]\|^2
 \le(6NA)^2u(5h/2).                                  \tag{6}
\]

Now restrict (3) to \(E\le h^{-1}\).
The cone gives \(|q|\le h^{-1}\). On \(|x|\le h/4\), \(\cos(xq)\ge1/2\).
Evenness of \(b\) therefore gives a spatial transform at least \(h/8\).
The time transform is at least \((h/2)e^{-3}\).
Writing \(m_\mu(L)=\mu\{E\le L\}\), we obtain
\[
 {e^{-6}\over256}h^4 m_\mu(h^{-1})
 \le\|[\alpha_h\otimes\varphi]\|^2,\qquad
 m_\mu(L)\le C_\varphi L^8u(5/(2L))=o(L^8),          \tag{7}
\]
for large \(L\), with
\(C_\varphi=256e^6[150R^2(\|\varphi\|_\infty+\|\nabla\varphi\|_\infty)]^2\).
No lower bound on a Fourier transform at large momentum is used.

Tonelli gives \(\Gamma(t)=t\int_0^\infty e^{-tL}m_\mu(L)\,dL\).
Given \(\epsilon>0\), choose \(L_\epsilon>0\) with \(m_\mu(L)\le\epsilon L^8\) above it.
Local finiteness follows from \(m_\mu(L)\le e^L\Gamma(1)\).
Hence
\[
 t^8\Gamma(t)
 \le t^9L_\epsilon m_\mu(L_\epsilon)+8!\epsilon
 \quad\Longrightarrow\quad
 \boxed{t^8\Gamma(t)\longrightarrow0}.               \tag{8}
\]
The factorial comes from eight integrations by parts in \(\int_0^\infty e^{-v}v^8\,dv\).
The zero label is immediate.

## 4. The critical frequency vanishes

AK's two-point band is \(4|m|\le10\).
Thus, for \(r>0\), its entire angular continuation has the form
\[
 g_r(z)=G(R_z(r,0))=\sum_{m=-2}^{2}a_m(r)e^{4imz}.
                                                               \tag{9}
\]
The notation \(G(R_z(r,0))\) means this continuation when \(z\) is complex.
For imaginary angles, (2) and the cone give
\[
 0\le g_r(is)
 =\int e^{-r(E\cosh s+q\sinh s)}d\mu
 \le\Gamma(re^{-|s|})=o(e^{8|s|}).                  \tag{10}
\]
Divide (9) at \(z=is\) by \(e^{8s}\) and let \(s\to+\infty\).
This gives \(a_{-2}(r)=0\).
Divide instead by \(e^{-8s}\) as \(s\to-\infty\), giving \(a_2(r)=0\).
These are the critical frequencies \(\pm8\); a mere \(O(t^{-8})\) bound would not remove them.
Reality and the coordinate reflection \(x\mapsto-x\) give
\[
 g_r(z)=c_0(r)+2c_1(r)\cos4z,\qquad c_0(r),c_1(r)\in\mathbb R.
                                                               \tag{11}
\]

## 5. The diagonal measure

Put \(D(t,x)=G(R_{\pi/4}(t,x))\), \(t>0\).
O5 makes the point-vector form
\[
 \langle e_{t,x},e_{u,v}\rangle_D=D(t+u,v-x)         \tag{12}
\]
positive: approximate each rotated point by a planar smooth bump, tensor with \(\varphi\), and apply diagonal RP.
Every reflected pair stays separated. Formula (1) and continuity pass positivity to the point limit.
Complete the quotient by null vectors.

On finite sums define \(T_s e_{t,x}=e_{t+s,x}\) and \(U_b e_{t,x}=e_{t,x+b}\).
The \(U_b\) preserve (12), while the \(T_s\) are symmetric and commute with them.
For \(v=\sum c_i e_{t_i,x_i}\), (2) bounds every time orbit by
\[
 \|T_sv\|\le
 \Gamma(\sqrt2\min_i t_i)^{1/2}\sum_i|c_i|=:B_v,\qquad
 \|T_sv\|^2=\langle v,T_{2s}v\rangle_D
       \le\|v\|\,\|T_{2s}v\|.
\]
The last inequality preserves null vectors.
Iteration gives \(\|T_sv\|\le\|v\|^{1-2^{-k}}B_v^{2^{-k}}\); hence \(T_s\) is a contraction.
It is positive since \(T_s=T_{s/2}^2\).
Continuity of \(D\) gives strong continuity of both families on point vectors, then on the completion.
Also \(T_1v=0\) implies \(T_{1/2^k}v=0\) for every \(k\), hence \(v=0\).
Set \(H_D=-\log T_1\ge0\).
Uniqueness of positive roots gives \(T_s=e^{-sH_D}\), first for rational \(s\), then for all \(s\).
The unitary-group spectral theorem defines \(P_D\) by \(U_b=e^{ibP_D}\).
Commutation with \(T_1\) makes their spectral resolutions commute.

Let \(\Pi_D\) be their joint spectral measure and set
\[
 d\nu=e^{2aE}\,d\langle e_{a,0},\Pi_D(E,q)e_{a,0}\rangle.
\]
The relation \(e_{b,0}=T_{b-a}e_{a,0}\) makes \(\nu\) independent of \(a\).
It is positive on \([0,\infty)\times\mathbb R\).
Choosing \(a<t/2\) in (12) gives
\[
 D(t,x)=\int e^{-tE+ixq}d\nu,\qquad
 \int e^{-tE}d\nu=D(t,0)<\infty.                    \tag{13}
\]
No cone support for \(\nu\) has been assumed.

## 6. The fourth frequency vanishes

We need uniqueness of the transforms in (13).
For two measures with finite Laplace weights, equality for real \(t>0,x\) extends to \(t=a+i\tau\).
Indeed, exponential domination gives holomorphy on \(\Re t>0\); apply the identity theorem for each \(x\).
These values are the Fourier transforms of the finite measures weighted by \(e^{-aE}\).
Their difference is zero: convolution with a Gaussian is zero by its Fourier integral and Fubini.
Letting the Gaussian width tend to zero against compact continuous tests proves equality of the weighted measures.
Remove the strictly positive weight. This also proves uniqueness for positive linear combinations.

Define
\[
 L_s(E,q)=(E\cosh s+q\sinh s,\ E\sinh s+q\cosh s),
 \qquad \mu_s=(L_s)_*\mu,\qquad C=\cosh4>1.
\]
The map preserves \(\mathcal C\), satisfies \(L_sL_t=L_{s+t}\), and has energy \(E_s\ge e^{-|s|}E\).
Thus \(\mu_s\) has every finite Laplace weight.
Direct multiplication gives
\[
 F_s(t,x):=\int e^{-tE+ixq}d\mu_s
 =G(R_{is}(t,x))=g_r(\theta+is),
 \quad (t,x)=R_\theta(r,0),\quad t>0.               \tag{14}
\]
Here the complex kernel is its AK tube continuation.
Indeed \(R_{is}(t,x)=(t\cosh s-ix\sinh s,\ x\cosh s+it\sinh s)\);
its spectral multiplier is \(e^{-tE_s+ixq_s}\).

Each of the three terms in (11) satisfies
\[
 (C-1)g_r(\theta+\pi/4)+g_r(\theta+i)+g_r(\theta-i)
 =(C+1)g_r(\theta).
\]
For the constant term the coefficients sum to \(C+1\).
For \(e^{\pm4i\theta}\) they sum to \(-(C-1)+2C=C+1\).
Equations (2), (13), (14) and transform uniqueness therefore give
\[
 (C-1)\nu+\mu_1+\mu_{-1}=(C+1)\mu,\qquad
 0\le\nu\le{C+1\over C-1}\mu.                       \tag{15}
\]
This proves the diagonal cone support.

Integrate (15) against \(w_s(E,q)=e^{-r(E\cosh s+q\sinh s)}\).
Domination in (15) makes it integrable for \(\nu\); the group law handles \(\mu_{\pm1}\).
Using (11) gives two inequalities:
\[
 F_s(r,0)=c_0(r)+2c_1(r)\cosh4s\ge0,\qquad
 \int w_s\,d\nu=c_0(r)-2c_1(r)\cosh4s\ge0.           \tag{16}
\]
Divide by \(\cosh4s\) and let \(s\to+\infty\).
The first inequality gives \(c_1(r)\ge0\); the second gives \(c_1(r)\le0\).
Thus \(G_{\varphi,\varphi}\) is radial.

Symmetry and a planar half turn give
\(G_{\varphi,\psi}(y)=G_{\psi,\varphi}(-y)=G_{\psi,\varphi}(y)\).
Therefore
\[
 G_{\varphi,\psi}
 ={1\over4}(G_{\varphi+\psi,\varphi+\psi}-G_{\varphi-\psi,\varphi-\psi})
\]
is radial too. Complex labels follow by bilinearity.
AK's \(L^1\) continuity extends the conclusion from smooth compact labels to every AK label.
Formula (1) gives rotation invariance of two plates with disjoint planar supports.
Hypercubic symmetry gives the same result in each coordinate plane.

## 7. Dimension and the first input

In four dimensions, the transverse label has two coordinates.
The cell count is \(O(h^{-2})\); its squared triangle bound costs \(h^{-4}\).
The two planar integrations in (3) cost another \(h^{-4}\) when solving for spectral mass.
Thus the exponent is eight. AK's plate exponent also changes to five, leaving \(m=0,\pm1,\pm2\) initially.

**The first unavailable input in a literal Y3 port is its strict growth exponent \(4+a_\Gamma<8\)** (Y3 L76141).
A bounded \(u\) gives only the endpoint estimate here.
TU10's \(u(d)\to0\) supplies (8), which removes the critical \(m=\pm2\).
The positive-measure identity (15) then ports the fourth-frequency argument without a dimension change.

**No input fails within the named conditional premises AK, O5 and TU10.**
For an unconditional conclusion, TU10 remains an unproved premise.
Row 168 stops first at identifying the exact transported source law with the localized exponent of Proposition 7.3.
That step needs C4 and B4; the later reference estimates and transfer also remain open.
AK's upstream D1 and cutoff-sequence premises remain conditional as recorded in its Result.

## Result

**AK + O5 + TU10 imply S10 in four dimensions: every nonconstant two-point harmonic vanishes, including frequency eight.**
In AK notation, \(M(2)=0\).
The proof uses only hand estimates, Hilbert positivity and spectral identities.
It grants no status and does not prove TU10, AC, all-order O(4), or T0.
Proved here by Codex as a conditional research statement; not yet checked by the other model.
