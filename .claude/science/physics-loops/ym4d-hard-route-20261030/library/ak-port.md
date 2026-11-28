# Analytic kernels in four dimensions (row 198)
Provenance: Codex (GPT-6; exact runtime variant and effort unavailable; queue requests max), checkout `13424f9e21239dda99dbf1cfee576bff311e438d`, Sussman–Alpoge commit `31a47c543775`. Research text; not an audit; grants no status.

## 1. Inputs and source

Take [PD](pd-port.md), equations (6)–(10), [O6](cone-o6.md), Result, and O2 from [s4-s6.md](s4-s6.md), Result, as conditional inputs. They share one separated-moment functional and its OS Hilbert space. O2 includes translations, coordinate reflections, quarter turns, symmetry, reality, and local continuity. No full rotation invariance is assumed.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Their sources are [the YM4 outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), AK, L29028–29774, and [YM3_I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), L75578–76680. Both have the source commit above. The constructions below port their argument by hand.

The cut proof continues through SA L29823; Y3's band and cut are IV-37-2/18, L76690–76856. Their [QED3](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/QED3/QED3.tex), L21656–21686, instead invokes RPM1 with Gaussian source domination. That extra input is not used here.

Fix the plane \((t,u)=(x_4,x_1)\). Its transverse label is \(\varphi\in L^1(\mathbb R^2)\). Use real labels first; extend by complex multilinearity. Write \(p=5\) for the plate exponent, not UI's exponent zero. PD supplies self-adjoint plates for real labels, with
\[
 \|B_{\varphi;a}\|\le Ca^{-p}\|\varphi\|_1,\qquad
 B_{\varphi;b}=e^{-(b-a)H}B_{\varphi;a}e^{-(b-a)H}\quad(0<a<b\le1/4).
 \tag{1}
\]
Self-adjointness follows by reflecting the smooth insertion form, then taking its plane approximate identity. Thus no unbounded point field is needed.

## 2. Tubes and products

Put \(e_0=(1,0)\), \(v_\pm=v^0\pm iv^1\), and
\[
 \mathbb V=\{\Re v_\pm>0\},\qquad
 r(v)=\min_\pm\Re v_\pm,\qquad v^*=(\bar v^0,-\bar v^1).
\]
O6 gives \(E_\pm=(E\pm q)/2\ge0\) in the joint spectral measure of \((H,P_1)\). Therefore
\[
 T(v)=\int e^{-v^0E+iv^1q}\,d\Pi
     =\int e^{-v_+E_--v_-E_+}\,d\Pi,
 \quad \|T(v)\|\le1,\quad T(v)^*=T(v^*),\quad T(v)\Omega=\Omega.
 \tag{2}
\]
These formulas hold on the closed tube. Multiplying integrands proves the semigroup law. Dominated convergence proves strong continuity. If \(\Re v_\pm\ge r>0\), the Taylor coefficient of degree \((j,k)\) has norm at most \(r^{-j-k}\). Indeed, \(x^je^{-x}/j!\le1\). Thus its power series converges in norm for \(|\Delta_\pm|<r\), proving holomorphy.
For real \(v^0\ge0\), reconstruction gives \(T(v)[F]=[\tau_vF]\), where \(\tau_vf(x)=f(x-v)\).

For \(v_i\in\mathbb V\), choose \(0<a\le1/4\) with \(2a<\min_i r(v_i)\). Define
\[
 K_n(v;\vec\varphi)=
 \langle\Omega,B_{\varphi_1;a}T(v_1-2ae_0)B_{\varphi_2;a}
       \cdots T(v_{n-1}-2ae_0)B_{\varphi_n;a}\Omega\rangle.
 \tag{3}
\]
For \(x_1,x_{i+1}-x_i\in\mathbb V\), also require \(a<r(x_1)\), and define
\[
 \Psi(\mathbf x;\vec\varphi)=T(x_1-ae_0)B_{\varphi_1;a}
       \prod_{i=1}^{n-1}\bigl[T(x_{i+1}-x_i-2ae_0)B_{\varphi_{i+1};a}\bigr]\Omega.
 \tag{4}
\]
Products run from left to right in increasing index. Replacing padding \(b\) by \(a<b\) in (1) leaves both expressions unchanged. Each internal translation becomes
\((b-a)e_0+(v-2be_0)+(b-a)e_0=v-2ae_0\).
The first translation in (4) becomes \(x_1-ae_0\); the final factor fixes \(\Omega\). This proves independence of padding. Locally fixed padding proves norm holomorphy of (4) and holomorphy of (3).

Set \(\delta(v)=\min(1,\min_i r(v_i))\). Choosing \(a=\delta(v)/4\) gives
\[
 |K_n(v;\vec\varphi)|\le\Bigl(\prod_i C_{\varphi_i}\Bigr)\delta(v)^{-pn},
 \qquad C_\varphi=4^p C\|\varphi\|_1. \tag{5}
\]
The vector bound uses the same formula with \(r(x_1)\) included in the minimum. Set \(K_0=1\), \(\Psi(\varnothing)=\Omega\), and \(K_1(\varphi)=\langle\Omega,B_{\varphi;a}\Omega\rangle\). Equation (1) makes \(K_1\) independent of \(a\). It is constant in position, and zero for the centered functional.

## 3. Removing smoothing

Initially take \(\varphi_i\in C_c^1(\mathbb R^2)\). For a nonnegative plane bump \(\beta_\epsilon\) of mass one, supported in \(B_\epsilon\), PD gives
\[
 B_a[\beta_\epsilon,\varphi]=\int\beta_\epsilon(y)V_{\varphi,4a}(y)\,dy,
 \quad
 \|B_a[\beta_\epsilon,\varphi]-B_{\varphi;a}\|
 \le\sup_{|y|\le\epsilon}\|V_{\varphi,4a}(y)-V_{\varphi,4a}(0)\|\longrightarrow0.
 \tag{6}
\]
Take \(\epsilon<a/16\). Pairing with polynomial classes and using PD's insertion formula identifies
\[
 B_a[\beta_\epsilon,\varphi][G]
 =[(\tau_{ae_0}(\beta_\epsilon\otimes\varphi))\cdot\tau_{2ae_0}G].
\]
Inserting these operators in (4), from right to left, puts their centers exactly at the real points \(x_i\). All supports remain separated. Equation (6) and the telescoping difference of finite products give norm convergence to (3)–(4). Convergence is uniform on compact tube subsets, since one padding works there and every translation is a contraction. Different entries may shrink at different rates.

For compact plane profiles \(\alpha_i\) with strictly ordered time supports, choose padding below half their smallest gap. Integrate the smoothed class identity against \(\prod_i\alpha_i(y_i)\). Its left side is the moment with profiles \(\alpha_i*\beta_{i,\epsilon}\). Riemann sums converge in \(C^1\), on fixed separated supports. Local continuity passes them through the moment. Convolution tends to \(\alpha_i\) in \(C^1\); (6) passes the right side to its limit. Hence
\[
 \sigma((\alpha_i\otimes\varphi_i)_i)
 =\int\prod_i\alpha_i(y_i)\,
       K_n(y_2-y_1,\ldots,y_n-y_{n-1};\vec\varphi)\,d\mathbf y.
 \tag{7}
\]
A common time translation handles profiles that start at negative time.
Only a norm limit of bounded operators entered the construction. This supplies the product limit that weak convergence alone would not give.

## 4. Gluing the frames

For \(\nu\in\{0,\pi/2,\pi,3\pi/2\}\) and a permutation \(\rho\), set
\[
 U_{\nu,\rho}=\{\mathbf z:R_{-\nu}(z_{\rho(i+1)}-z_{\rho(i)})\in\mathbb V\},
 \qquad
 K^{\nu,\rho}(\mathbf z)=K_n(R_{-\nu}\partial(\rho\mathbf z);\rho\vec\varphi).
 \tag{8}
\]
Here \(\partial\) takes consecutive differences. O2 and (7) identify this as the moment density in that frame. Any nonempty overlap is convex and contains the real part of each point. Small real discs there preserve both orders. Integrating either density against bumps in those discs gives the same moment. Shrinking the bumps proves equality on the real overlap. A holomorphic function zero on a real open ball has zero Taylor series there. Overlapping balls propagate this equality throughout the connected overlap.

Thus (8) gives one holomorphic \(\mathcal K_n\) on \(U_n=\bigcup U_{\nu,\rho}\). This union is connected: arbitrary strict time and spatial orders can be assigned independently, so every time chart meets every spatial chart. The other frames reverse those orders. Its real part is
\[
 \operatorname{Ord}_n=\{\mathbf y:\text{all times are distinct, or all spatial coordinates are distinct}\}.
\]
The density is real there, by (7). It has permutation symmetry, translation invariance, and quarter-turn invariance. The real identities and the same Taylor argument prove their complex versions.

## 5. The Gram kernel

For positive tube configurations \(\mathbf x,\mathbf y\), of lengths \(k,l\), put
\[
 J(\mathbf x,\mathbf y)=
 ((x_k-x_{k-1})^*,\ldots,(x_2-x_1)^*,x_1^*+y_1,
                         y_2-y_1,\ldots,y_l-y_{l-1}).
\]
Reverse the real left labels too. Use one padding small enough for both configurations. Taking the adjoint of (4) reverses its operators. Their middle translations add to \(x_1^*+y_1-2ae_0\). The remaining factors are exactly (3), so
\[
 K_{k+l}(J(\mathbf x,\mathbf y);\varphi_k,\ldots,\varphi_1,\vec\psi)
       =\langle\Psi(\mathbf x;\vec\varphi),\Psi(\mathbf y;\vec\psi)\rangle.
 \tag{9}
\]
With one empty configuration, remove the central difference and that side's list; with both empty, the value is one.
Complex left labels must also be conjugated.

Complex rotation satisfies \((R_zv)_\pm=e^{\pm iz}v_\pm\). Thus \(R_{is}\) preserves \(\mathbb V\) and the positive configuration domains. Also \((R_{is}v)^*=R_{is}v^*\). Replacing both configurations in (9) by their boosts proves
\[
 G_s(\mathsf x,\mathsf y):=K_{k+l}(R_{is}J(\mathbf x,\mathbf y))
       =\langle\Psi(R_{is}\mathsf x),\Psi(R_{is}\mathsf y)\rangle.
 \tag{10}
\]
For every finite family, its quadratic form is the squared norm of the corresponding vector sum. Hence \(G_s\) is positive for every real \(s\), including mixed lengths and the vacuum.

## 6. The finite band

A pencil has real consecutive differences \(v_i\) with \(|\arg(v_i^0+iv_i^1)|<\pi/8\). Put \(r_0=\min_i|v_i|>0\). For \(z=t+is\), choose a nearest quarter turn \(\nu\), so \(|t-\nu|\le\pi/4\). Then
\[
 \Re(R_{z-\nu}v_i)_\pm
 =|v_i|e^{\mp s}\cos(\arg(v_i^0+iv_i^1)+t-\nu)
 \ge r_0\cos(3\pi/8)e^{-|s|}.
\]
Thus \(a_{\mathbf y}(z)=\mathcal K_n(R_z\mathbf y)\) is defined for every complex \(z\). The glued charts make it entire and \(\pi/2\)-periodic. Equation (5) gives \(|a_{\mathbf y}(t+is)|\le A_{\mathbf y,\vec\varphi}e^{pn|s|}\). Define
\[
 c_m(\mathbf y)=\frac2\pi\int_0^{\pi/2}a_{\mathbf y}(t)e^{-4imt}\,dt.
\]
Move this integral to height \(s\). The vertical sides cancel by periodicity, and Cauchy's theorem gives
\[
 |c_m(\mathbf y)|\le A_{\mathbf y,\vec\varphi}e^{4ms+pn|s|}.
\]
Send \(s\to-\infty\) when \(4m>pn\), and \(s\to+\infty\) when \(4m<-pn\). These coefficients vanish. The entire periodic function descends under \(w=e^{4iz}\) to a holomorphic function on \(\mathbb C\setminus\{0\}\). Its Laurent coefficients are these \(c_m\). Therefore
\[
 a_{\mathbf y}(z)=\sum_{4|m|\le pn}c_m(\mathbf y)e^{4imz},
 \qquad \boxed{4|m|\le5n}. \tag{11}
\]

To define coefficients on every chart, put \(N=\lfloor pn/4\rfloor\) and
\[
 \mathcal L=\sum_i(-z_i^1\partial_{z_i^0}+z_i^0\partial_{z_i^1}),\quad
 P(X)=\prod_{j=-N}^N(X-4ij),\quad
 p_m(X)=\prod_{\substack{-N\le j\le N\\j\ne m}}\frac{X-4ij}{4im-4ij}.
\]
Equation (11) makes \(P(\mathcal L)\mathcal K_n\) zero on the real open set of pencils. Holomorphic uniqueness on connected \(U_n\) makes it zero everywhere. Define \(c_m=p_m(\mathcal L)\mathcal K_n\). Polynomial interpolation gives \(\sum_m p_m=1\), and \((X-4im)p_m(X)\) is a constant multiple of \(P(X)\). Consequently
\[
 \mathcal K_n=\sum_m c_m,\qquad \mathcal Lc_m=4imc_m,
 \qquad \mathcal K_n(R_{is}\mathbf z)=\sum_m e^{-4ms}c_m(\mathbf z).
 \tag{12}
\]
The last identity solves \(\partial_s c_m(R_{is}\mathbf z)=-4mc_m(R_{is}\mathbf z)\); boosts preserve every chart. Real rotations give the phase \(e^{4imt}\) while the path stays ordinary. Permutation symmetry passes through \(\mathcal L\). A common translation adds only total derivatives, which annihilate translation-invariant functions. Reality and \(\overline{p_m}=p_{-m}\) give \(c_{-m}=\bar c_m\) on real configurations.

## 7. Global coefficients and boost positivity

Consider distinct planar configurations with no perpendicular pair of nonzero difference vectors. They form a dense open set. Indeed, the product of the excluded squared distances and scalar products is a polynomial, nonzero at distinct collinear points. Its restriction to a segment ending at that configuration has finitely many zeros, proving density. Every rotation of such a configuration is ordinary: a time tie and a spatial tie would give perpendicular differences. The local phase law from (12) therefore holds along its whole rotation orbit.

For any distinct configuration \(\mathbf y\), choose an angle \(t\) giving distinct rotated times. Each pair forbids only finitely many angles modulo \(2\pi\). Locally define
\[
 \widetilde c_m(\mathbf y)=e^{-4imt}c_m(R_t\mathbf y).
 \tag{13}
\]
Two choices agree on the dense set just described, hence throughout their overlap by continuity. These definitions give real-analytic coefficients on all distinct planar configurations. They inherit translations, labelled permutations, conjugation, and the phase law for every real angle. They agree with \(c_m\) on ordinary configurations. This extends the coefficients; it does not yet identify moment densities on exceptional supports.

Set \(M(0)=M(1)=0\). For \(n\ge2\), let \(M(n)\) be the largest \(|m|\) occurring for any real labels, or zero if none occurs. Thus \(M(n)\le5n/4\). For arbitrary real positive-half-plane configurations of lengths \(k,l\), define
\[
 \widetilde G_s(\mathsf x,\mathsf y)
 =\sum_m e^{-4ms}\widetilde c_m^{(k+l)}
          (\theta\mathbf x,\mathbf y;\vec\varphi,\vec\psi),
 \qquad \theta(t,u)=(-t,u).
 \tag{14}
\]
Use \(\widetilde c_0^{(0)}=1\) and the constant \(K_1\) for length one. If each tuple has distinct times, sort them; (12) and (10) identify (14) with a Gram matrix. For any finite family with time ties, perturb its points inside the half-plane to remove the ties. Reflected combined configurations remain distinct. Continuity of each finite coefficient sum gives entrywise convergence. Each quadratic form is a limit of nonnegative numbers. Thus (14) is positive for every \(s\), with arbitrary lengths and time ties.

For fixed length \(k\), put \(t_k=\widetilde c_{-M(2k)}^{(2k)}\). Multiply its boosted Gram matrix by \(e^{-4M(2k)s}\) and send \(s\to+\infty\). All other coefficients vanish in this limit. Therefore \(t_k(\theta\mathsf x,\mathsf y)\) is a positive kernel. For a line \(\ell\) with chosen normal \(R_\nu e_0\), translating and rotating that side to \(t>0\) proves positivity of
\[
 e^{4iM(2k)\nu}t_k(\theta_\ell\mathsf x,\mathsf y).
\]
The phase follows from (13) and must be retained. Cauchy–Schwarz for this kernel gives
\[
 |t_k(\theta_\ell\mathsf x,\mathsf y)|^2
 \le |t_k(\theta_\ell\mathsf x,\mathsf x)|\,
       |t_k(\theta_\ell\mathsf y,\mathsf y)|. \tag{15}
\]

## 8. The cut inequality

For all \(k,l\ge0\),
\[
 \boxed{2M(k+l)\le M(2k)+M(2l).} \tag{16}
\]
If \(M(k+l)=0\), this follows from nonnegativity. Otherwise choose real labels and a pencil with \(c_{-M(k+l)}\ne0\). Such a pencil exists: conjugation gives the negative frequency, and a nonzero holomorphic coefficient cannot vanish on the real open pencil set.

For \(k,l>0\), translate a time strictly between its first \(k\) and last \(l\) points to zero. Reflect and reverse the first group to obtain a positive configuration \(\mathsf x\); call the second group \(\mathsf y\). Translation and permutation invariance preserve the chosen coefficient. Equations (10), (12), and Hilbert Cauchy–Schwarz give
\[
 |\widetilde G_s(\mathsf x,\mathsf y)|^2
 \le\widetilde G_s(\mathsf x,\mathsf x)\widetilde G_s(\mathsf y,\mathsf y).
\]
As \(s\to+\infty\), the left side divided by \(e^{8M(k+l)s}\) tends to the positive squared modulus of that coefficient. The right side is at most a finite constant times \(e^{4(M(2k)+M(2l))s}\). A larger left exponent would contradict the inequality. This proves (16).

For \(k=0\), translate the pencil into the positive half-plane and use \(\Omega\) as the first vector. Its diagonal Gram entry is one. The same comparison gives \(2M(l)\le M(2l)\). Interchanging the groups handles \(l=0\), and the fully empty case is equality.

## 9. Dimension and the first input

Smooth compact labels are dense in \(L^1(\mathbb R^2)\). Equations (1) and (5) make their products converge in norm on compact tube subsets. Cauchy's formula gives convergence of the finite derivatives used in (12). Thus all kernels, coefficient identities, and positive matrices extend to \(L^1\) labels. Equation (7) defines the corresponding continuous extension of ordered moments. A coefficient nonzero at an \(L^1\) label remains nonzero at some smooth approximation, so \(M(n)\) does not change.

In Y3, time is \(x_3\) and a plate label lies on \(\mathbb R\). Here time is \(x_4\) and the label lies on \(\mathbb R^2\). PD changes Y3's exponent \(p_{\mathrm I}+4\) to \(p_{\mathrm I}+5=5\). Each product therefore has growth \(e^{5n|s|}\). AK uses only \(H\ge|P_1|\), not the number of remaining generators. The tube, quarter turns, planar configuration spaces, Gram algebra, and cut argument are unchanged. O2 transports them to every coordinate plane.

**First failing input within the stated conditional premises: none.** For unconditional T0, rooted **D1** remains unavailable; its cited construction starts at **C1/OH1**. E1 must also provide the cutoff sequence. These are the upstream limits recorded in the input notes.

## Result

**Given PD, O2 and O6 in their common setting, S9 follows:** holomorphic product kernels, norm removal of smoothing, frame gluing, the Gram representation, the band \(4|m|\le5n\), boost positivity, and the cut inequality (16), including the empty tuple. The highest coefficient also satisfies (15). This leaves TU and AC on the route to O(4).

Proved by Codex as a conditional research statement; not yet checked by the other model. Every deduction is by hand. No audit or scientific status is granted.
