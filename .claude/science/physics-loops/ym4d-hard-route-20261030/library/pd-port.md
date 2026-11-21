# Analytic plate density in four dimensions (row 196)
Provenance: Codex (GPT-6; exact runtime variant and effort unavailable; queue requests max), checkout `4b2a9031b460a669beccf03452d10186c111a661`, Sussman–Alpoge commit `31a47c543775`. Research text; not an audit; grants no status.

## 1. Inputs and source

We take the Results of [ui-port.md](ui-port.md) and [cone-o6.md](cone-o6.md) as conditional inputs. UI has \(p=0\). O6 gives the joint spectral cone \(E\ge |q_j|\), \(j=1,2,3\). Their common setting includes normalized separated moments, local \(C^1\) continuity, and the OS Hilbert space. These inputs retain their stated dependencies.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The sources, at the commit above, are [YM3_I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM3/YM3_I.tex), Lemma IV-32-34, Propositions IV-32-38 and IV-34-17/30, and Corollary IV-34-42 (L75697–75825, L76220–76497); and the [YM4 outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), PD1–PD18 (L28537–28840). The compact parametrix below is the outline's construction. YM3_I uses holomorphic mean values instead. All deductions below are by hand.

Their [QED3](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/QED3/QED3.tex), L21665–21686, invokes RPM1 through an additional Gaussian \(L^2\) source bound. That bound is not among our inputs.

Write \(t=x_4\), \(\theta(t,\mathbf x)=(-t,\mathbf x)\), and \(\tau_xh(v)=h(v-x)\). Set
\[
 I(F;h;G)=\sigma(\theta\bar F\cdot(h)\cdot G),\qquad
 \|F\|_a=\|[\tau_{-ae_4}F]\|,\qquad
 \|h\|_\sharp=\max(\|h\|_\infty,c_M\|\nabla h\|_\infty).
\]
For \(0<\eta\le1\), UI bounds this form by
\(C_I\eta^{-p}\|h\|_\sharp\|F\|_{\eta/4}\|G\|_{\eta/4}\).
Here the outside entries lie above \(\eta/4\), and \(h\) lies in \(B(y,c_I\eta)\), with \(|y_4|\le\eta/8\). Constants below depend only on these input constants. They do not depend on outside field numbers.

## 2. Bounded insertions and analytic translation

Apply UI to \(\tau_{(\eta/4)e_4}A,\tau_{(\eta/4)e_4}B\), with \(h\) centered at zero. The resulting form kills null vectors and extends to the Hilbert completion. Its representing operator satisfies
\[
 \|B_{h,\eta}\|\le C\eta^{-p}\|h\|_\sharp,\qquad
 B_{h,\eta}[A]=[(\tau_{(\eta/4)e_4}h)\cdot\tau_{(\eta/2)e_4}A]. \tag{1}
\]
Pairing the displayed vector with every polynomial class proves the identity by one common time translation. Its supports are separated. Splitting real and imaginary parts permits complex \(h\), at a factor two.

Define
\[
 T(z)=\int e^{-z_4E+i\mathbf z\cdot\mathbf q}\,d\Pi(E,\mathbf q).
\]
O6 bounds its norm by one when \(\Re z_4\ge\sum_{j=1}^3|\Im z_j|\). On a region with positive margin \(\delta\), an order-\(m\) spectral derivative is bounded by
\(E^m e^{-\delta E}\le m!\delta^{-m}\).
The exponential series therefore converges uniformly on smaller neighborhoods. Its spectral integral is holomorphic in operator norm.

For \(\operatorname{supp}h\subset B(0,c_I\eta/2)\), put
\[
 M_{h,\eta}(z)=T(\eta e_4/8+z)B_{h,\eta/2}T(\eta e_4/8-z),\qquad
 \mathcal O_\eta=\{|\Re z_4|+\textstyle\sum_j|\Im z_j|<\eta/8\}.
\]
This is holomorphic with norm at most \(C\eta^{-p}\|h\|_\sharp\).
For real \(x\), \(|x_4|<\eta/8\), (1), spatial covariance and a common time translation give
\[
 I(F;\tau_xh;G)=\langle\Phi,M_{h,\eta}(x)\Psi\rangle,\qquad
 \Phi=[\tau_{-(\eta/4)e_4}F],\quad\Psi=[\tau_{-(\eta/4)e_4}G]. \tag{2}
\]
The time factors are \(e^{-(\eta/8+x_4)H}\) and \(e^{-(\eta/8-x_4)H}\); the spatial factors are \(U(\mathbf x)\) and \(U(-\mathbf x)\). Thus (2) uses only positive time shifts. Real spatial positions are unrestricted.

## 3. The scaled parametrix

In \(\mathbb R^4\), put \(G(x)=-|x|^2\log|x|/(64\pi^2)\), with \(G(0)=0\). This function is \(C^1\). Away from zero, radial differentiation gives
\[
 \Delta(|x|^2\log|x|)=8\log|x|+6,\qquad
 \Delta\log|x|=2|x|^{-2}.
\]
Integration by parts outside a radius-\(\varepsilon\) ball proves these distribution identities too. Their boundary errors are respectively \(O(\varepsilon^4|\log\varepsilon|)\) and \(O(\varepsilon^2)\). For \(|x|^{-2}\), the surviving flux is
\(-2|S^3|f(0)=-4\pi^2f(0)\); the other term tends to zero. Thus
\[
 \Delta|x|^{-2}=-4\pi^2\delta_0,\qquad \Delta^3G=\delta_0. \tag{3}
\]
Choose real \(\chi\in C_c^\infty(B_1)\), equal to one near zero. Set
\[
 n=\chi G,\quad s=\delta_0-\Delta^3n,\qquad
 n_r(x)=r^2n(x/r),\quad s_r(x)=r^{-4}s(x/r).
\]
Every remaining term in \(s\) differentiates \(\chi\) away from zero. Hence \(s\) is smooth and compactly supported. Scaling (3), including the delta's fourth power, gives
\[
 \Delta^3n_r=\delta_0-s_r,\qquad
 \|n_r\|_\sharp\le Cr,\quad \|s_r\|_\sharp\le Cr^{-5}\quad(0<r\le1). \tag{4}
\]
Both supports lie in \(B_r\). Explicitly,
\(n_r=-\chi(x/r)|x|^2\log(|x|/r)/(64\pi^2)\).
Keeping the ratio inside the logarithm removes the false \(|\log r|\) loss.
For smooth compact \(k\), convolution of (4) yields
\[
 k=(\Delta^3k)*n_r+k*s_r. \tag{5}
\]
Indeed, move derivatives onto the smooth factor under the integral. The distribution identity then gives (5), and both sides are continuous.

## 4. Density, plates and compatibility

Fix \(\epsilon=\min(c_I/8,1/1024)\), \(r=\epsilon\eta\), and define
\[
 V_\eta(z)=\Delta_z^3M_{n_r,\eta}(z)+M_{s_r,\eta}(z).
\]
On \(|\Re z_4|+\sum_j|\Im z_j|<\eta/32\), a polydisc of radius \(\eta/128\) lies in \(\mathcal O_\eta\). Cauchy's formula bounds each sixth derivative by \(6!(128/\eta)^6\) times the original bound. The sum of coefficients of \(\Delta^3\) is \(4^3\). Equations (2) and (4) give
\[
 \|V_\eta(z)\|\le C\eta^{-p}(\eta^{-6}r+r^{-5})
                  \le C\eta^{-(p+5)}. \tag{6}
\]
For \(k\in C_c^\infty(\{|t|<\eta/64\})\), apply the insertion form to (5). Convolution Riemann sums converge in \(C^1\), with a common compact support. Local \(C^1\) continuity and (2) therefore pass the form through each integral. Integration by parts moves six derivatives from \(k\) to \(M\), with positive sign and no boundary term. This proves
\[
 I(F;k;G)=\int k(x)\langle\Phi,V_\eta(x)\Psi\rangle\,dx,\qquad
 |I(F;k;G)|\le C\eta^{-(p+5)}\|k\|_1\|\Phi\|\|\Psi\|. \tag{7}
\]
All convolution supports remain between the outside supports. Mollification proves (7) for compact \(C^1\) tests. Their density in \(L^1\) defines the unique continuous extension on this strip. Different parametrices give the same continuous density: their difference integrates to zero against every smooth compact test. Holomorphic uniqueness then identifies their continuations.

Write \(x=(t,u,y)\), \(y\in\mathbb R^2\). For \(\varphi\in L^1(\mathbb R^2)\), define
\[
 V_{\varphi,\eta}(t,u)=\int\varphi(y)V_\eta(t,u,y)\,dy.
\]
The uniform bound (6) defines this operator integral. Locally uniform Taylor bounds allow termwise integration, proving norm holomorphy for \(|\Re t|+|\Im u|<\eta/32\). Equation (7) and Fubini give the required plate bound:
\[
 |I(F;\alpha\otimes\varphi;G)|
 \le C\eta^{-\wp}\|\alpha\|_1\|\varphi\|_1
                   \|F\|_{\eta/4}\|G\|_{\eta/4},\qquad
 \boxed{\wp=p+5=5}. \tag{8}
\]
Here \(\alpha\in L^1(\mathbb R^2)\) is supported in \(|t|<\eta/64\); its spatial extent is unrestricted.

For \(0<a\le1/4\), set \(B_{\varphi;a}=V_{\varphi,4a}(0,0)\). A plane approximate identity converges to this operator in norm, by continuity of \(V\). Translation of the smooth insertion form, followed by that limit, gives
\[
 B_{\varphi;b}=e^{-(b-a)H}B_{\varphi;a}e^{-(b-a)H}\quad(a<b\le1/4),
 \qquad \|B_{\varphi;a}\|\le Ca^{-5}\|\varphi\|_1. \tag{9}
\]
The same identity with a translated approximate identity gives
\[
 V_{\varphi,4a}(t,u)=T((a-a'+t)e_4+ue_1)
 B_{\varphi;a'}T((a-a'-t)e_4-ue_1) \tag{10}
\]
when \(0<a'<a\), \(|t|<a/16\), and \(a-a'>|t|\). Both factors are contractions for real arguments as stated. Smooth compact labels are dense in \(L^1\); (8) passes (9)–(10) to all such labels. These are the compatible point plates required by S9. No unsandwiched point operator was assumed.

## 5. Can the exponent be improved enough?

**Five is optimal for the uniform \(L^1\)-label bound deduced from UI and O6. Even fixed smooth labels cannot have a universal exponent below four.** The following counterexample concerns these analytic inputs, not the Wilson construction.

Define centered Gaussian separated moments by Wick pairings with
\[
 C(x)=\int_0^\infty\lambda^3\,d\lambda
       \int_0^\infty(4\pi s)^{-2}e^{-|x|^2/(4s)-\lambda s}\,ds
       =c|x|^{-10}\quad(x\ne0),\qquad c>0. \tag{11}
\]
Integrating \(\lambda\) gives \(6s^{-4}\); substituting \(v=|x|^2/(4s)\) proves the last equality. Only disjoint-test moments are used. Disjoint compact supports make every pairing finite and locally \(C^1\)-continuous. The mass-\(\lambda\) kernel has spatial Fourier transform \(e^{-|t|\omega}/(2\omega)\), \(\omega^2=|q|^2+\lambda\): its first derivative has jump \(-1\), so it is the decaying Green function. Changing \(\lambda=E^2-|q|^2\) yields the positive measure
\[
 d\nu(E,q)=(2\pi)^{-3}(E^2-|q|^2)^3
                1_{\{E>|q|\}}\,dE\,d^3q. \tag{12}
\]
The reflected covariance is the inner product of the Laplace–Fourier transforms in \(L^2(\nu)\). Expand each polynomial into internal Wick contractions and products of these vectors. Its reflection form equals the symmetric Fock inner product, term by term. This proves reflection positivity and the Hilbert realization. There \(H=d\Gamma(E)\), \(P_j=d\Gamma(q_j)\), and O6 follows by summing \(E\ge|q_j|\) over particles. Radiality of (11) gives the other mirror symmetries as well.

Here is UI, including its independence of field number. Put \(a=\eta/4\). For a test in UI's ball, set
\[
 f_\pm(E,q)=\int h(t,x)e^{-(a\pm t)E+iq\cdot x}\,dt\,d^3x.
\]
Take \(a(f)\) antilinear and \(a^\dagger(f)\) linear. For real \(h\), the centered slab operator is
\(a^\dagger(f_+)e^{-2aH}+e^{-2aH}a(f_-)\). Wick contraction with polynomial vectors verifies this formula: the creation term leaves the inserted field unpaired; the annihilation term contracts it with each right-hand field. The support condition gives
\[
 |f_\pm|\le C\eta^4\|h\|_\infty e^{-\eta E/16},\qquad
 \|f_\pm\|\le C\eta^{-1}\|h\|_\infty,\qquad
 \|E^{-1/2}f_\pm\|\le C\eta^{-1/2}\|h\|_\infty. \tag{13}
\]
To check the powers, integrate (12) in \(q=Ev\), giving \(CE^9dE\). Then use
\(\int_0^\infty E^k e^{-b\eta E}\,dE=k!(b\eta)^{-k-1}\), obtained by repeated integration by parts.
Sectorwise Cauchy–Schwarz gives
\(\|a(f)v\|\le\|E^{-1/2}f\|\|H^{1/2}v\|\).
The creation norm squared adds \(\|f\|^2\|v\|^2\). Since
\(\|H^{1/2}e^{-2aH}\|\le Ca^{-1/2}\), (13) bounds the slab operator by \(C\eta^{-1}\|h\|_\infty\).
Finally, vanishing outside the source ball gives
\(\|h\|_\infty\le2c_I\eta\|\nabla h\|_\infty\).
Thus this model satisfies precisely UI with \(p=0\), uniformly on the whole Hilbert space.

Choose real \(\varphi\in C_c^\infty(\mathbb R^2)\) with positive integral. For its point plate,
\[
 \|B_{\varphi;a}\Omega\|^2
   =\int e^{-2aE}|\widehat\varphi(q_2,q_3)|^2\,d\nu(E,q). \tag{14}
\]
The Fourier transform is bounded below near zero. Restrict (14) to
\(a^{-1}\le E\le2a^{-1}\), \(|q_1|\le(4a)^{-1}\), and a fixed small transverse ball. For small \(a\), the spectral weight is at least \(ca^{-6}\), while this region has volume \(ca^{-2}\). Therefore
\(\|B_{\varphi;a}\|\ge ca^{-4}\).
For \(\varphi_a(y)=a^{-2}\varphi(y/a)\), its \(L^1\) norm stays fixed. The transverse ball can now have radius \(c/a\). Its extra area gives
\[
 \|B_{\varphi_a;a}\|\ge ca^{-5},\qquad
 \|\varphi_a\|_1=\|\varphi\|_1. \tag{15}
\]
This rules out every smaller exponent in (8) with the same uniform label norm. Equation (14) also rules out the fixed-label improvement \(\wp<4\) required by the shortcut.

For completeness, the numerical threshold in [RPM1](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/RP%20O(d)%20trick%20(RP1)/RPM1.tex), L2438–2590, is strict. Grant its band, cut inequality and rotated-law positivity:
\[
 0\le M_n\le\wp n,\quad M_0=0,\quad
 2M_{a+b}\le M_{2a}+M_{2b},\quad M_{2a}\in8\mathbb Z.
\]
If \(\wp<4\), then \(M_2=0\). The differences \(M_{2a}-M_{2a-2}\) are nondecreasing multiples of eight. One positive difference forces eventual slope at least eight, contradicting \(M_{2a}\le2\wp a<8a\). Hence every even term vanishes; using \(b=0\) kills every term. At \(\wp=4\), and thus also at five, the sequence \(M_n=4n\) satisfies all these inequalities. This is an obstruction to that integer argument, not a noncovariant field example. **RPM1's elimination therefore does not replace TU and AC on the supplied inputs.**

## 6. Dimension and the first input

YM3_I has two spatial generators; here there are three. Its holomorphic tube therefore gains one absolute-value term. Its mean-value proof of IV-34-30 costs \(r^3r^{-7}=r^{-4}\). In four dimensions the four-variable weight costs \(r^4r^{-9}=r^{-5}\). For IV-34-17, a transverse label now needs two partition directions instead of one. Their cell count costs \(r^{-2}\), yielding \(r^2r^{-5}r^{-2}=r^{-5}\). Thus leaving the label smooth does not remove the extra power in that proof. The four-dimensional replacement (3)–(4) gives the same loss directly. Bounded forms, convolution, holomorphic uniqueness and the compatibility identities do not change.

**First failing input for conditional PD: none.** Local \(C^1\) continuity belongs to the supplied separated-moment setting; UI and an abstract cone alone would not define these forms. **First unavailable premise of the proposed shortcut: a plate exponent below four.** Equations (11)–(15) disprove its implication from the supplied analytic inputs. For unconditional T0, D1 remains unproved, beginning with C1/OH1 in the input notes; the cutoff sequence is also assumed. This port establishes neither.

## Result

**Given UI and O6 in their stated common setting, S8 follows:** the scaled parametrix (3)–(5), analytic density (6)–(7), and compatible \(L^1\) plates (8)–(10), with \(\wp=p+5=5\). The uniform \(L^1\)-label exponent cannot be lowered using these inputs alone. Even fixed labels cannot yield the strict \(\wp<4\) needed by RPM1. TU and AC remain on this route. Proved by Codex as a conditional research statement; not yet checked by the other model. Every step is by hand; no scientific status is granted.
