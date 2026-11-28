# Repo search

**Plan (sketched).** Check the prior-work record, the cited repository hits, and ownership. Identify the unproved finite-form estimate in row 1489. Read the indexed source ranges for its inputs. Seek an exact rational upper certificate or a polynomial lower witness using the three-cube arms. Record the derivation and checks here, followed by the two next rows and their decision criteria.

**Checked provenance.** FINISH 1493, research by Codex at `626a56d91`. The target-specific prior file is absent. The lead's November 8 survey covered main and PRs 10114, 10133, 10134 and 10141. I checked PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149 (one chosen spatial loop in a transfer kernel) and main's `research/mass-gap/library/gap-form-exercise.md` 139–145 (twisted mass interpolation). Neither evaluates a Gram norm on observed sums. A phrase search outside this lane on main and the five available PR refs, including 10144, returned no match. The open registry has no matching owner. Row 1484 checks an auxiliary pivot environment. Rows 1485 and 1489 give the actual open-star law, the three comparisons, the three-cube arm formula and the existing cutoff. Row 1491 checks row 1489 and explicitly leaves this decision open. These results are prior work. [Lead search](prior/repo-search-2026-11-08.md) · [Wilson star](gap-k2-wilson-interface-astra62.md) · [Arm numerator and cutoff](gap-k2-interface-decide-astra62.md) · [Cross-provider check](gap-k2-pin-interface-check-opus.md)

**Checked literature scope.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of the text, derive the one-bond character multipliers and their ratios in GL3–GL4. Their connected-log theorem assumes the Kotecký–Preiss criterion. Their CA-I item 4.19 uses a previous-level representation and a terminal ceiling for Bałaban's small-coupling hypothesis. The external sources were located through the outline chunk and obligation index and the CA-I index. These inputs do not supply the order-one Gram norms here. The lattice RG background is due to Bałaban. [Outline, 2197–2239](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2197-L2239) · [Outline, 1310–1326](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1310-L1326) · [CA-I, 56439–56448](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L56439-L56448) · [CA-I, 56530–56539](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L56530-L56539)


## Decision at \(\beta=23/10\)

**Open.** For the Wilson star the bounds obtained here are
\[
 \frac{529}{2048}+3\,2^{-823}+2^{-2024}
       < R=3p+3m+o_1
       <7-\frac{1499}{300}\,2^{-511}-2^{-294}.
\]
Here \(p,m,o_1\) denote respectively the outgoing perpendicular, mixed perpendicular and opposite maximal correlations. Neither decision threshold has been reached. The 312 plaquette weights and the zero-transverse-corner pivots are those of 1485.

**Proved progress.** Bounds (5) and (12) remove a collar of width \(1/162\) and the large-trace region \(|T|\ge91/8\), together costing less than \(14/1024\) in the full row. The perpendicular conditional densities have five square-integrable derivatives, the opposite ones have nine, and (7) gives the corresponding degree errors. The marginal density on the retained core is at least \(2^{-2050}\), giving an explicit weighted finite compression. The spin-two quadratic Gram block has row strictly below one, and the high angular sectors in (11) have row at most \(3/2048\). Trace probes alone give infinite rank in each perpendicular form. On an opposite face they have rank at most 18157 against arbitrary probes on the other. The mixed form reduces to one shared class angle with finite private-edge labels. For the entire opposite form an explicit finite polynomial image contains its range exactly. The interior scalar and lower angular multiplicity norms still require an upper certificate or a violating trial. All results are author research and grant no status.

## What the adaptive density estimate can certify

**Proved.** Even an optimal choice of the reciprocal-density polynomial in 1489 (2) cannot give a small tensor-degree space with the stated constant. Write \(k=\ell(K)\) for the uniform mass of the support inside the ten-dimensional cube. If (2) is at most \(e\), Hölder's inequality and \(\int_Kp_i\,d\ell=1\) give
\[
 k\le \|b\|_\infty+k^{3/4}e/\sqrt C,\qquad
 (J+1)e\ge C^{3/2}\big(k-k^{3/4}e/\sqrt C\big).
 \tag{1}
\]
The cube of coordinate radius \(1/8\) lies in \(K\). Indeed \(\|M\|_*\le\sqrt3\|M\|_F\le3\sqrt3/8\), and \(1+3\sqrt3<8\). Thus \(k\ge2^{-30}\). With the \(C\ge2^{228}\) of 1489, already \(e\le1\) forces \(\|b\|_\infty>2^{-31}\) and \(J+1>2^{311}\). This applies to every choice of \(b,u,N\) in (2)–(3). The obstruction occurs before the Gram integrations. It concerns the displayed sufficient error bound.

**Proved.** There is a geometric limitation even if the density bound \(C\) is sharpened. Necessarily \(C\ge1/k\). The entire matrix lies in the nine-dimensional Euclidean unit ball of radius \(1-|s|\). Consequently
\[
 k\le \frac{\operatorname{vol}(B_9)}{10\,2^9}
       =\frac{32\pi^4}{945\cdot10\cdot2^9}<\frac1{256}.
\]
Here \(\operatorname{vol}(B_9)=32\pi^4/945\) follows by the disk-slicing recurrence \(V_d=2\pi V_{d-2}/d,\ V_1=2\). The last inequality already follows from \(\pi<4\). From (1),
\((J+1)e\ge k^{-1/2}(1-e k^{1/4})\) for \(0<e\le1\). At least one of the fourteen side errors in a passing sum is at most \((122/125)/14<1/14\). On that side \(J+1>220\) even with an optimal common \(C\). A dense tensor basis would already need more than \(220^{10}-1\) centred coordinates. This identifies why a useful change of space must also change the error argument or the matrix representation.

## A finite block for all functions of a single quadratic evaluation

**Proved.** Work at \(P=P_{23/10}\) of 1348 (13). For a bounded real function \(\phi\) on \([-12,12]\), take the spectral probe
\[
 F_\phi(Q)=\int_{S^3}\phi(v^tQv/\beta)\,dv .
 \tag{2}
\]
There is one fixed space of at most \(13\cdot481\) conditional fields that contains \(N_{F_\phi}(A)/N_1(A)\) for *every* \(\phi\), including polynomials of arbitrarily high degree. This holds in the full 312-plaquette star. The inward convention adds the rooted gauge average of 1485 (5). The proof gives the separated fields before this projection.

In 1489's three-cube arm integral write \(w(B)=W(B)(C^PW)(B)\). Each link of a three-cube is on two squares, so \(W\) has degree at most 20 in that link. The convolution kernel has degree ten there, so \(C^PW\) has degree at most ten. For fixed \(v,A\) change variables on each edge by \(B_e=v^{-1}A_e U_e v\). Product Haar is preserved, and the argument in (2) becomes \(\sum_e q(U_e)\). The full numerator weight \(w(B)\prod_eP(q(A_e^{-1}B_e))\) has degree at most 40 in each \(U_e\). Given \(x_e=q(U_e)\), its imaginary vector is uniform on the two-sphere of radius \(\sqrt{1-x_e^2}\). Odd monomials vanish and even angular moments are rational, for example by Gaussian radial separation in three coordinates. Integrating the directions and \(v\) gives a polynomial in the twelve scalars, of degree at most 40 in each. Its coefficients are rational polynomials of the fixed \(A\). Expand it in products of the Chebyshev polynomials \(U_j(x)\) of the second kind. Thus each field numerator is a sum of fixed coefficient fields times \(\int \phi\,d\nu_{\boldsymbol j}\), where
\[
 \nu_{\boldsymbol j}
   = (U_{j_1}\sigma)*\cdots*(U_{j_{12}}\sigma),\quad
 0\le j_e\le40,\qquad
 d\sigma(x)=\tfrac2\pi\sqrt{1-x^2}\,dx .
 \tag{3}
\]

**Proved.** These signed measures have a rational linear span of dimension at most \(13\cdot481\). For \(t>0\) the Laplace transform of \(U_j\sigma\) is \(2(j+1)I_{j+1}(t)/t\). This is the character integral in GL3 with the Wilson scalar normalization removed. The recurrence \(I_{j+1}=I_{j-1}-2jI_j/t\) expresses \(I_{j+1}\) in \(I_0,I_1\) with polynomials in \(1/t\) of degree at most \(j\), by induction starting with \(I_1,I_0\). Multiplying twelve transforms embeds their span into the span of
\[
 t^{-12-h}I_0(t)^r I_1(t)^{12-r},\qquad 0\le r\le12,\qquad 0\le h\le480 .
\]
A rational linear dependence of the coefficient vectors gives a dependence of the measures. Indeed a vanishing Laplace transform on \(t>0\) has all moments zero by analyticity at zero, and polynomials are dense on the compact support. Selecting independent rational coefficient columns therefore bounds the rank without assuming these displayed functions are independent. Division of all central fields by the same positive \(N_1\) preserves the rank bound. The other seven arm factors remain in the central Gram integral. Exact moments of a polynomial \(\phi\) in (3) use one-dimensional Haar moments only. The bound controls the conditional-field range of this family. Its marginal Gram form still uses the product of two averaged probes.

**Proved, a degree bound for the entire range in (2).** Moments through degree **5826** distinguish every signed measure in the span (3). Thus every conditional field of a bounded \(\phi\) in (2) is also the field of a polynomial in the scalar argument of degree at most 5826. Real coefficients suffice for arbitrary probes, and a rational vector of consistent moments has a rational solution. This concerns equality of the cross numerators. The minimal marginal variance representing a field is a separate question.

Here are details of the zero-order bound that makes the cutoff explicit. Multiply a linear combination of the Laplace transforms in (3) by \(t^{492}\). It becomes \(y=p(t)f(t)\), where \(p\) is a row of 13 polynomials of degree at most 480 and \(f_r(t)=I_0(t)^r I_1(t)^{12-r}\), \(0\le r\le12\). Write \(D=t\,d/dt\). The identities \(I_0'=I_1,\ I_1'=I_0-I_1/t\) follow termwise from the series. Thus \(Df=(tA+B)f\) for a constant matrix \(A\) and diagonal \(B_{rr}=-(12-r)\). Form rows \(p_0=p,\ p_{i+1}=Dp_i+p_i(tA+B)\). Their degrees are at most \(480+i\) and \(p_if=D^iy\). The first \(m\) independent rows, consecutive starting with \(p_0\), span all the rows over the rational functions because the derivative rule preserves their span as soon as a dependence occurs. The zero row is immediate. Otherwise \(1\le m\le13\), and a nonzero \(m\)-column minor \(w(t)\) of these rows has degree at most \(480m+m(m-1)/2\le6318\).

For the local argument let the coefficient field be \(\mathbb R\) (or \(\mathbb Q\) for rational combinations). In the Laurent-series span of the rows take the submodule \(E\) of vectors with power-series entries. Factoring the lowest power of \(t\) from each nonzero series shows that the power-series ring is a principal ideal domain. Elimination therefore gives a power-series basis of \(E\). Clearing powers of \(t\) gives the rank. Its reduction \(E/tE\) injects into the constant row space, since an element vanishing at zero can be divided by \(t\) within \(E\). The derivative rule preserves \(E\) and acts on its reduction by right multiplication by \(B\). For a basis \(e_j\) of \(E\), the vector \(z_j=e_j f\) therefore satisfies \(Dz=C(t)z\) with power-series matrix \(C\) whose constant term has only nonpositive eigenvalues. If \(z\) vanishes at zero but is nonzero as a series, its first nonzero coefficient at order \(k>0\) is an eigenvector of \(C(0)\) with eigenvalue \(k\), impossible. On the other hand, Cramer's rule on the selected columns expresses every \(w e_j\) as a power-series combination of the first \(m\) rows. If \(y\) vanishes to order greater than 6318, so do all \(D^iy\), hence every \(z_j\) vanishes at zero. This proves \(y=0\). Vanishing of the first 5827 moments gives precisely this order after multiplication by \(t^{492}\). Duality in a finite-dimensional space now proves the assertion about polynomial fields. It needs neither a test of thousands of determinants nor any independence assertion for the Bessel products.

As one application, the functional on (3) sending \(\nu_{\bf j}\) to \(\prod_e(j_e+1)\) is consistent because it is the limit of testing against \(e^{tx}/[\int e^{tu}d\sigma(u)]^{12}\) as \(t\to+\infty\), since each tilted coordinate concentrates at one. Its data are rational. A rational polynomial of degree at most 5826 thus realizes this endpoint functional exactly in the arm numerator. It substitutes \(B_e=v^{-1}A_e v\) in the polynomial weight before the \(v\)-average. No assertion about the variance of that interpolating probe is needed for the identity.

**Proved limitation.** This family by itself misses even the spectral polynomial \(s^2\), where \((s,M)\) are the observed coordinates of 1489. Its directions before averaging are proportional to \((1,R)\) with \(R\in SO(3)\). Every ridge function in these directions is annihilated distributionally in the interior by \(L=\sum_{ij}\partial_{M_{ij}}^2-3\partial_s^2\), since \(\sum R_{ij}^2=3\). This identity survives the rotation average, finite sums and constants, whereas \(L s^2=-6\). On a small interior ball where the actual marginal density is bounded below, convergence in the marginal \(L^2\) implies distributional convergence. Such a ball exists by 1489's positive submersion density, or by continuity of its nonzero probability density. The conclusion also holds for the closure of bounded ridge probes by approximation. Thus one cannot declare the missing spectral sector negligible on the strength of this finite rank.


## The shared square has infinitely many transmitting modes

**Proved for the actual polynomial and Wilson weights.** Put \(T=\operatorname{tr}Q/(4\beta)=\sum_e q(A_e)q(B_e)\) in transported outward variables. Let \(U\) be the central holonomy of the square fixed by the perpendicular reflection and \(\delta=\arccos|q(U)|\in[0,\pi/2]\). Conditional on \(\delta\), the essential upper endpoint of \(T\) is
\[
                    u(\delta)=8+4\cos(\delta/4).                 \tag{4}
\]
For a shared oriented edge set \(\alpha_e=\arccos|q(A_e)|\). Quaternion geodesic distance on the unit three-sphere is bi-invariant. Taking the smaller distance to the two central signs gives the quotient metric, hence \(\delta\le\sum_{\square}\alpha_e\), also for edges traversed backwards. Concavity and monotonicity of cosine on \([0,\pi/2]\) give \(\sum_{\square}|q(A_e)|\le4\cos(\delta/4)\). The eight private terms are at most one each. To reach the endpoint choose the four oriented square edges equal to a fourth root of the representative of \(U\) nearer the identity, with inversions and one central sign as necessary. Take the eight other \(A_e\) scalar, and every \(B_e\) a scalar with the sign of \(q(A_e)\). There is no further constraint on these links. Under product Haar, three square links and their oriented product can be used as independent Haar coordinates, by solving for the fourth. Thus every relative open neighbourhood of this configuration in a fixed-product fibre has positive conditional mass. Both star weights are continuous and strictly positive, as is the integrated weight of unmarked links. Conditioning on the class angle gives (4) almost everywhere, and every interior interval of \(\delta\) has positive mass. In particular the support boundary survives the tilt from all eight arms.

**Proved.** Both perpendicular reflection forms have infinite rank on the closure of polynomials in the *scalar trace alone*. Take arbitrarily many \(u(\pi/2)<t_1<\cdots<t_n<12\), let \(f_j={\bf1}_{T>t_j}\), and write \(d_j=u^{-1}(t_j)\), in decreasing order. The functions \(h_j(\delta)=\mathbb E[f_j\mid\delta]\) vanish for \(\delta>d_j\) and are positive for \(\delta<d_j\), up to null sets. They and the constant are linearly independent, by restricting successively to the intervals cut out by the \(d_j\). Centring preserves rank \(n\). For either perpendicular form, its self-pairing on a centred spectral probe \(f\) dominates \(\|\mathbb E[f\mid\delta]\|_2^2\). Indeed use Cauchy–Schwarz for the positive reflection form against any real centred fixed-plane function of \(\delta\). The shared-site gauge average defining the mixed form preserves this pairing, since the angle is gauge invariant. Take the fixed-plane function to be \(\mathbb E[f\mid\delta]\). The Gram form on the \(n\) centred probes above is therefore positive definite. Continuous ramps approximate these threshold indicators in marginal \(L^2\) (there are no trace atoms by 1489's one-face density, also valid under a bounded change of weight). Rational polynomials approximate the ramps uniformly. For each fixed \(n\), positivity of the smallest eigenvalue persists under sufficiently accurate approximation. This proves the infinite-rank assertion on rational polynomial trials as well, in the sense of arbitrarily large nonsingular finite Gram minors. It gives no uniform lower bound on their eigenvalues. The disjoint-array finite rank of 1489 for the opposite pair is consistent with this result.

**Consequence (proved).** The finite conditional range (2)–(3) cannot span the transmitting fields even after restricting to spectral probes. A tail estimate is essential for an upper certificate on the perpendicular forms. Formula (4) identifies a one-dimensional source of that tail on the shared square.


## An explicit mixed-pair polynomial trial

**Proved.** Both the Wilson and \(P\) forms have \(m>2^{-823}\) at \(\beta=23/10\). The same rational polynomial of the observed trace works in both laws. This gives a quantitative witness in the shared-square sector of (4).

Let \(B=\{|q(U)|\le1/8\}\), and let \(E\) require the twelve \(A_e\) and twelve transported \(B_e\) on one outward face to lie within chord distance \(1/8\) of the identity. These are auxiliary events for the proof. On \(B\), \(T<8+4(15/16)=47/4\), since \(8x^4-8x^2+1\) at \(x=15/16\) exceeds \(1/8\) and \(\cos(4\theta)\) decreases for \(0\le\theta\le\pi/8\). On \(E\), \(T\ge12(127/128)^2>12-3/16\).

Here are lower probabilities under either actual star law. Write \(b_0=13\,2^{-20}\). Each single plaquette weight has minimum-to-maximum ratio greater than \(2^{-8}\). For \(P\) use \(P>1/13,\ \sup P\le e^\beta<12\), the last bound following from \(e^2<8,\ e^{3/10}\le10/7\). Wilson satisfies the same ratio. Free one edge on the central square, conditioning on all other original links. At most six weights involve it. Its Haar holonomy would be uniform, with scalar density at least \(1/4\) on \([-1/8,1/8]\), so \(\Pr(B)\ge 2^{-52}\).

Set the selected crossings to identities by transporting the neighbour as in 1485, and hold all links other than the 24 specified in \(E\) fixed. Under base product Haar their cap probability is at least \(2^{-360}\), using the chord-ball bound \(r^3/64\) of 1489. Exactly 72 weights can be affected. They comprise 18 central plaquettes (six in the face, twelve normal to it), 18 in the neighbour, twelve crossing the selected interface and 24 crossings on other arms (two per selected central edge). On \(E\) the twelve internal face traces and twelve selected cut traces are each at least \(7/8\), by the chord triangle inequality for products of at most four links. Each of these weights exceeds half its global maximum, since \(e^{\beta/8}(1+b_0)<2\) by \(e^{23/80}\le(1-23/80)^{-1}\). The other 48 cost at most a factor \(2^8\) each. Comparing the integral on \(E\) to the unrestricted integral at fixed remaining links gives \(\Pr(E)\ge 2^{-360-24-384}=2^{-768}\).

For \(a=(12-T)/24\) let \(G(a)=\sum_{k=0}^{896}\binom{98304}{k}a^k(1-a)^{98304-k}\), and take
\[
 f(T)=\sum_{j=512}^{1024}\binom{1024}{j}G(a)^j(1-G(a))^{1024-j}.
\]
These are polynomials over the rationals. Binomial probabilities give a short hand proof of their bounds. The mean of the first count is 768 at \(a=1/128\), and 1024 at \(a=1/96\). Its variance at either endpoint is at most 1024. Chebyshev's inequality at distance 128 and monotonicity of the count in its parameter give \(G\ge15/16\) on \(E\), \(G\le1/16\) on \(B\). For the second count the wrong tail is bounded by \(2^{1024}(1/16)^{512}=2^{-1024}\). Thus \(0\le f\le1\), \(\mu=\mathbb E f>2^{-769}\), and \(\mathbb E[f\mid B]\le2^{-1024}<\mu/2\). Reflection on the fixed plane and gauge invariance of \(B\) yield
\[
 \operatorname{Corr}(f_i,f_j)
 \ \ge\ \frac{\operatorname{Cov}(f,{\bf1}_B)^2}
                 {\operatorname{Var}(f)\operatorname{Var}({\bf1}_B)}
 \ >\ \Pr(B)\mu/4\ \ge\ 2^{-823}
\]
for a mixed perpendicular pair, using \(\operatorname{Var}(f)\le\mu\). The same bound holds for the positive perpendicular test. This trial is of degree \(98304\cdot1024\), given in factored form. Its lower bound comes from its actual Gram form and the fixed-plane test, without expanding the monomials. Together with 1489's Wilson positive-pair bound and 1485's opposite-pair bound this gives \(R>529/2048+3\,2^{-823}+2^{-2024}\).


## A uniform bound on the boundary part of all three forms

**Proved.** In the coordinates \((s,M)\) of 1489, put \(D_\partial=\{|s|+\|M\|_*\ge1-1/162\}\). For each distinct pair of faces, in both star laws,
\[
       \Pr(Y_i\in D_\partial\mid Y_j)<2^{-23}
       \quad\hbox{almost surely}.                                  \tag{5}
\]
This estimates a fixed collar of the actual support and applies to every observed probe there.

For each of the twelve private tangential links in the neighbour, at most four plaquettes contain it (two spatial, one reaching the other slice, one cut). At fixed remaining links its Wilson conditional density is proportional to \(e^{h\cdot b}\) with \(t=|h|\le4\beta\). Its maximum divided by its Haar mean is \(1/\mathbb E_{\rm Haar}e^{-t(1-q)}\). Since \(19/2\ge4\beta\),
\[
 e^{-t(1-q)}\ge ((1+q)/2)^{19},\qquad
 \mathbb E_{\rm Haar} ((1+q)/2)^{19}
      =\frac{\operatorname{Cat}_{20}}{4^{19}}.
\]
The equality follows from the beta integral with both parameters \(3/2\), or by multiplying \((2k+3)/(2k+6)\) for \(0\le k<19\). For \(P\) the one-link density maximum costs at most the additional factor \((1+b_0)^4\). The resulting bound is less than 42. Conditional expectation preserves the same domination if fewer of the other links are fixed. Exposing the twelve links one by one therefore dominates their joint conditional law by \(42^{12}\) times product Haar given *all* exterior links. This includes \(Y_j\). At fixed crossings the changes to transported variables preserve this bound. On an inward face one uses the free neighbour on the source side and transposes the orthogonal map below.

For unit quaternions let \(T_{\eta,O}=\operatorname{diag}(\eta,O)\), where \(\eta=\pm1,\ O\in O(3)\). The support function in (5) is \(\max_{\eta,O}\sum_e b_e\cdot T_{\eta,O}a_e/12\), by the singular value decomposition. For a maximizer on the collar, the root mean squared chord distance between \(b_e\) and \(T_{\eta,O}a_e\) is at most \(1/9\). Changing the quaternion parametrizing the proper rotation by chord at most \(r=1/144\) changes its operator norm by at most \(2r\), by the two terms in the difference of quaternion conjugations. Fix a representative in the improper component to obtain the same bound there. The root mean squared chord then stays at most \(1/9+2r=1/8\). The corresponding Haar set of rotations has mass at least \(r^3/64\). Thus the indicator of the collar is bounded by \(64 r^{-3}\) times the sum, over two signs and two components, of the rotation averages of the event \(\sum_e(1-b_e\cdot T_{\eta,O}a_e)\le 3/32\).

For a fixed such map and fixed other endpoints, under independent Haar private links the twelve summands have independent densities \((2/\pi)\sqrt{x(2-x)}\) on \([0,2]\). Majorize each density by \((2\sqrt2/\pi)\sqrt{x}\) and integrate over the simplex of sum at most \(L=3/32\). Iterating the beta integral gives \((2/\pi)^6 L^{18}/18!\), using \(\Gamma(3/2)=\sqrt{\pi}/2\). Since \(\pi>3\), the combined upper bound in (5) is
\[
       256\,144^3\,42^{12}(2/3)^6(3/32)^{18}/18! < 2^{-23}.
\]
Only the twelve-link density bound used the interaction. The common unmarked-arm weights were allowed throughout.

**Proved.** Let \(C_{ij}\) be the centred covariance operator on the full marginal \(L^2\) spaces, extended to kill constants. Let \(P_i^\circ\) multiply by the indicator of the complementary interior \(D_\partial^c\). For a unit probe supported in the collar, test against a centred unit probe on the other face. Cauchy–Schwarz in the joint law bounds the covariance by the square root of (5), by putting the collar indicator on the other probe in its squared moment. This gives
\[
 \|C_{ij}-P_i^\circ C_{ij}P_j^\circ\|<2/2048 .
\]
It counts both omitted sides. The interior norm uses the original marginal \(L^2\) norms and the original centring in \(C_{ij}\). In particular, an upper sum \(24/25\) for the three interior forms with multiplicities \(3,3,1\) would give \(R_P<24/25+14/2048<122/125\). This removes the boundary collar with a quantitative cost. The interior still has infinitely many modes.


## Five derivatives for the perpendicular conditional density

**Proved for \(P\).** Let \(k_z\) be the density against uniform \(\ell\) on \([-1,1]^{10}\) conditional on another observed face. Extend the density by zero outside that cube. Uniformly up to null sets, the perpendicular density has an \(H^5\) bound \(2^{490}\), and the opposite density has an \(H^9\) bound \(2^{720}\). Every marginal and pair-conditional density has sup norm at most \(2^{510}\). The estimates below use the Fourier Sobolev norm with weight \((1+|\xi|^2)^a\) in the squared norm of order \(a\), and the constant density rescaling for \(\ell\). They improve both the derivative order and the large polynomial-coefficient constant of 1489 (1).

Freeze all but the eight private quaternion pairs of 1489, or all twelve for disjoint opposite faces. Fixing the crossing frames converts the pairs to \((a,b)\) with Haar reference. Their normalized joint density \(w\) is a positive polynomial of degree at most 60 on each single sphere. It integrates to one for each choice of frozen links. At frequency \(\xi\) put \(L=\operatorname{diag}(\xi_0,\Xi)/12\), where \(\Xi\) is the \(3\times3\) frequency matrix. Let \(t_1,t_2\) be the two largest singular values of \(L\). Apart from a constant phase, the integrand is a product of \(\exp(i a^t Lb)\) over free pairs.

**Proved, one pair.** The Haar reproducing kernel for spherical polynomials of degree at most 60 is
\[
 D(b,b')=\sum_{j=0}^{60}(j+1)U_j(b\cdot b'),\qquad |D|<2^{18}.
\]
Indeed quaternion coordinates are linear combinations of fundamental matrix coefficients, so their products of degree at most 60 lie in the representations with twice spin \(j\le60\), by successive tensoring with the fundamental. Character orthogonality gives the displayed projector on these representations. Conversely the spin-\(j/2\) coefficients are polynomials of degree \(j\). The sup bound uses \(|U_j|\le j+1\).

Projection of the plane wave \(e^{i h\cdot b}\) in \(b\), at \(b'\), has absolute value at most \(2^{28}(1+|h|)^{-3/2}\). In fact its expansion is the sum through \(j=60\) of \(2(j+1)i^jJ_{j+1}(|h|)U_j(\widehat h\cdot b')/|h|\). This follows by continuing the one-dimensional character integral used in (3) to an imaginary argument (or by expanding the exponential). For \(t\ge1,\ n\le61\), the bound \(|J_n(t)|\le(n+6)t^{-1/2}\) follows by taking the \(n\)th Fourier coefficient of \(e^{it\cos\theta}\), whose Bessel series follows by multiplying the two exponential series on the unit circle. The intervals with \(|\sin\theta|<t^{-1/2}\) have total length at most \(2\pi t^{-1/2}\). On the rest integrate by parts with divisor \(-it\sin\theta\). The boundary contribution is at most \(4/\sqrt t\) before division by \(2\pi\). The total variation of \(1/\sin\theta\) on those arcs is at most \(4\sqrt t\), and differentiating the other exponential costs at most \(2\pi n/\sqrt t\) after division by \(t|\sin\theta|\). At \(t\le1\) integrate \(|D|\) directly.

Projection in \(a\) costs at most \(2^{18}\) times the Haar average of this bound at \(h=L^ta\). Two coordinates of a uniform three-sphere point have the uniform law on the unit disk, by polar coordinates in two orthogonal planes. In the left singular frame,
\[
 \int(1+|L^ta|)^{-3/2}\,da
 \le \frac{2^6}{(1+t_1)\sqrt{1+t_2}} .
\]
For \(t_1\ge1\) enclose the disk in the square, use \(\sqrt{x^2+y^2}\ge(|x|+|y|)/2\), then integrate \((1+t_1 x+t_2 y)^{-3/2}\) first in \(0\le x\le1\). The remaining integral of \((1+t_2y)^{-1/2}\) is \(2/(1+\sqrt{1+t_2})\). For \(t_1<1\) the bound exceeds one. Hence the doubly projected plane wave is bounded by \(2^{52}/[(1+t_1)\sqrt{1+t_2}]\). Applying the tensor product projector to the density \(w\) leaves it fixed. Move the projector to the plane waves, then integrate their product against the positive probability \(w\). This avoids expanding any plaquette polynomial in coordinates. With \(m=8\) or 12 the Fourier bound is
\[
        2^{52m}(1+t_1)^{-m}(1+t_2)^{-m/2}.                      \tag{6}
\]

**Proved, integration around rank-one directions.** In the ten Lebesgue variables of \(L\) the region \(t_1\le R,\ t_2\le u\) has volume at most \(2^{17}R^5u^5\) for \(0<u\le R\). If the scalar block is largest, the volume is at most \(2^{10}Ru^9\). Otherwise the scalar lies in \([-u,u]\) and every matrix column is within \(u\) of a common singular line. Pick a longest column \(c\). Each other column is within \(2u\) of the line of \(c\), by projecting first onto the singular line and bounding the angle error by \(u/|c|\) times its length. The zero matrix costs no volume. With three choices of \(c\), a cube of side \(2R\) for \(c\), and two cylinders of length \(2R\), radius \(2u\), the claimed bound follows. For \(u>R\) the right side also bounds the volume by using \(u=R\) first.

For \(R=2^j\ge1,\ t_1<2R\), integration of \((1+t_2)^{-a}\) costs at most \(2^{30}R^5\) for \(a\ge6\), and \(2^{31}R^6\) for \(a=4\). Use the preceding volume for \(t_2<1\), then for \(2^l\le t_2<2^{l+1}\), \(0\le l\le j+1\), multiply \(2^{17}(2R)^5\,2^{5(l+1)}\) by \(2^{-al}\) and sum. On \(R\le t_1<2R\), \(|\xi|\le48R\) and \(d\xi=12^{10}\,dL\). Squaring (6), the shell power for \(H^5\) with eight pairs is \(R^{-16+10+5}=R^{-1}\), and for \(H^9\) with twelve pairs it is \(R^{-24+18+5}=R^{-1}\). Explicitly the squared Lebesgue norms are bounded by \(2^{104m}2^{40+30+12a+2}\) at derivative order \(a=5,9\), using \((1+48^2R^2)^a\le2^{12a}R^{2a}\). This includes the unit ball, bounded directly by \(2^{17}\) in \(L\)-volume, and the dyadic sum \(\sum_{j\ge0}2^{-j}=2\). The change to the \(\ell\)-density and norm costs \(2^5\) after the square root. For Fourier inversion fix any extra pairs and keep eight free. The shell power is \(R^{-8+6}=R^{-2}\), so the absolute integral is at most \(2^{416+40+31+2}\), and conversion to \(\ell\)-density costs \(2^{10}\). These bounds give the stated constants, dropping inverse Fourier factors at most one. Averaging over the frozen links preserves every bound.

**Proved, new all-degree error test.** For a rational polynomial \(b\), use the same marginal orthogonality as in 1489 (2), through coordinatewise degree \(J+\deg_{\max}b\). If \(J\ge r\), where \(r=5\) on a perpendicular pair and \(r=9\) on an opposite pair, a unit omitted probe has pairing with every unit probe on the other side bounded by
\[
 E_r(J,b)=\sqrt{H_r}\,\|1-bp_i\|_{4,K}
           +\frac{2^{255}H_r\|b\|_{\infty,D}}{(J+2-r)^r},
 \qquad H_5=2^{490},\quad H_9=2^{720}.                         \tag{7}
\]
For the tensor Legendre tail, the squared norm of the \(r\)th derivative of a normalized one-dimensional Legendre mode \(n\ge r\), with weight \((1-x^2)^r\), is \((n+r)!/(n-r)!\). Indeed the operator \((-1)^r(d/dx)^r(1-x^2)^r(d/dx)^r\) is symmetric on polynomials by integration by parts, preserves degrees, and has this leading coefficient on \(x^n\). Orthogonality identifies its eigenpolynomials. Integration by parts and Bessel's inequality now give the energy bound on the sum of the omitted squared coefficients, because at least one index \(n\ge J+1\) pays \((J+2-r)^{2r}\). Smooth approximation allows \(H^r\) densities. Apply this to the conditional density integrated against the unit opposite probe, as in 1489. The other Cauchy–Schwarz term uses \(\|k_z\|_2\le H_r\). In (3) of 1489 the marginal Legendre tail \(C/(N+1)\) can likewise be replaced by \(H_9/(N-7)^9\) for \(N\ge9\), and its sup-density constant by \(2^{510}\). The moment integrals remain the three-cube integrals of 1489. Even (7) with these explicit worst-case constants has a large second term at small \(J\). It does not give a passing interior or full Gram norm.


## A non-scalar finite Gram block

**Proved.** Consider the spin-two part of the outward, private-rotation-invariant polynomials of total degree at most two. In unscaled coordinates \(M_0=\sum_e{\bf a}_e{\bf b}_e^t\), it consists of
\[
                 F_H=\langle H,M_0M_0^t\rangle,\qquad
 H=H^t,\quad \operatorname{tr}H=0,\quad \|H\|_F=1 .
\]
Here the normalization on \(H\) selects unit coefficient tensors. Right rotations average a product of two columns using  \(\int R_{ij}R_{kl}=\delta_{ik}\delta_{jl}/3\), and a single column averages to zero. This proves the assertion about the degree-two space. The full marginal is invariant under common conjugations, so \(F_H\) is centred. Its mixed and opposite forms against *any* probe are zero by the gauge projections of 1485. Common conjugation and the irreducibility of symmetric traceless tensors make the positive perpendicular form a scalar on this five-dimensional block. One may see irreducibility by diagonalizing a nonzero tensor, then using axis permutations and planar rotations to span the diagonal differences and symmetric off-diagonal matrices. The same argument gives the scalar variance form. We bound their ratio below one third.

Write \(F_D\) for the component of the lifted probe charged precisely at the subset \(D\) of the eight central vertices. These are the commuting gauge projections of 1485, acting here before conditional expectation onto the central box. For a positive perpendicular pair only \(D\) contained in the shared square can pair. Cauchy–Schwarz, reflection and cube symmetry give
\[
 3\,\operatorname{Cov}(F_{H,i},F_{H,j})\le
 V+\tfrac12\sum_{|D|=1}\|F_D\|_2^2
       -\sum_{\text{\(D\) varying in all three coordinates}}\|F_D\|_2^2,
 \qquad V=\operatorname{Var}F_H.                                  \tag{8}
\]
Indeed the empty component vanishes by spin two. Of the six face squares a singleton lies on three, a set varying in one coordinate lies on two at most, and a set varying in all three lies on none. These projections apply directly to the expectation of the product of the two three-cube arm numerators. Equivalently they can be applied before integrating the two independent arms. This retains all spectator weights.

**Proved, singleton term.** Keep a physical configuration fixed while averaging its central vertex gauges. Simultaneous inversion keeps \({\bf a}{\bf b}^t\) fixed, so orient every incident edge away from the chosen vertex. Write \(a b^{-1}=(c_e,v_e)\) at that vertex. Given its gauge, integration at a far endpoint makes \(b\) uniform and \(a=(c_e,v_e)b\) in the corresponding frame. The mean edge matrix is \((c_e I+[v_e]_\times)/4\), where the bracket denotes cross product. For two copies of the same edge the traceless mean of \({\bf a}{\bf a}^t |{\bf b}|^2\) is \(-\operatorname{tf}(v_ev_e^t)/12\), by the fourth moment of a uniform quaternion. Here \(\operatorname{tf}\) removes a scalar trace. For distinct incident edges the two far endpoint gauges are independent. A term with at most one occurrence incident to the vertex has spin at most one there (a pair of fundamental coefficients), hence its singleton projection at spin two vanishes. Combining the three incident edges gives the singleton tensor, up to rotation by the vertex gauge,
\[
    -\operatorname{tf}\left[
        \tfrac1{16}\Big(\sum_e v_e\Big)\Big(\sum_e v_e\Big)^t
                       +\tfrac1{48}\sum_e v_e v_e^t\right].
\]
Its norm is at most \(\sqrt{2/3}(9/16+3/48)\). Haar rotation gives squared pairing with \(H\) equal to one fifth its squared norm, by irreducibility and the trace of the orbit covariance. The eight singleton norms squared therefore sum to at most \(5/12\).

**Proved, four distinct charged sites.** Of the 66 unordered edge pairs on a three-cube, 24 meet at a vertex. Twelve of the 42 disjoint pairs are coplanar, the opposite edge pairs of the six squares. Each of the other 30 has four vertices varying in all three coordinates and is the only perfect matching of its four endpoints by cube edges, since two matchings would form a four-cycle and hence a square. The charge on all four sites therefore comes only from the two indicated edge matrices, both charged at both ends.

For one edge let the orthogonal quaternion map \(x\mapsto axb^{-1}\) have spatial block \(C_e\) (the last three rows and columns). Then \(\|C_e\|_F^2=2+c_e^2\), by orthogonality and top-left entry \(c_e\). Gauging the endpoints rotates the block independently to \(C=R_s C_e R_t^t\). The doubly charged part of \({\bf a}{\bf b}^t\) is \(S=(C+C^t-\operatorname{tr}C\,I)/4\). To verify it, project \(x\mapsto axb^{-1}\) on the sixteen Frobenius-orthogonal matrices \(x\mapsto e_i x\bar e_j\) of squared norm four, \(e_i\in\{1,i,j,k\}\). For imaginary basis elements their spatial blocks are \(e_ie_j^t+e_je_i^t-\delta_{ij}I\). Only the spatial block is charged at both ends. The covariance of its rotated entries is \(\|C_e\|_F^2\delta_{ik}\delta_{jl}/9\) for entries \(ij,kl\). Thus on symmetric test matrices the covariance of \(S\) has eigenvalues at least \(1/72\) on the scalar line and \(1/18\) on the five traceless directions.

For a disjoint pair the two such matrices \(S,S'\) use independent endpoint gauges. The relevant scalar is \(2\langle H,SS'\rangle\). The map \(T\mapsto(HT+TH)/2\) on symmetric matrices has squared Hilbert–Schmidt norm \(5/4\). This follows in an eigenbasis of \(H\), where the diagonal multipliers are \(\lambda_i\) and its off-diagonal multipliers are \((\lambda_i+\lambda_j)/2\). The squared norms from scalar to traceless and back are each \(1/3\), and the scalar-to-scalar part vanishes. The squared norm of the traceless block is \(7/12\). It follows that each of the 30 four-site charges contributes at least
\[
 4\left(\frac{2/3}{72\cdot18}+\frac{7/12}{18^2}\right)=\frac1{108}.
\]
The supports are distinct, so the loss in (8) is at least \(5/18\). These inequalities hold for each fixed configuration averaged over its gauges.

**Proved bound on this block.** Substitution gives \(3\operatorname{Cov}(F_{H,i},F_{H,j})\le V-5/72\). Also \(V\le(2/15)12^4\), since \(\|\operatorname{tf}(M_0M_0^t)\|_F^2\le(2/3)\|M_0\|_F^4\), \(\|M_0\|_F\le12\), and rotation averaging divides by five. Thus the *maximum* seven-exit row of the compressed degree-two spin-two block is at most
\[
                    1-\frac{75}{144\cdot12^4}<1.                 \tag{9}
\]
The derivation holds for \(P\) and for Wilson directly. Higher-degree copies of spin two can mix with this one. The scalar polynomials \(1,s,s^2\) and \(\operatorname{tr}(M_0M_0^t)\) form a separate block whose norm remains open.


## An upper bound on the whole row from the three-cube weights

**Proved.** For the two actual laws write \(B=\sup P/\inf P\) or \(B=e^{2\beta}\), respectively. In either case \(B<2^7\), since \(e<11/4,\ e^{3/10}\le10/7\), and \(B\le(1+b_0)e^{2\beta}\). For any positive gauge-invariant three-cube density \(w\), the convolution
\[
        L_w(A)=\int w(B')\prod_{e=1}^{12}P(q(A_e^{-1}B'_e))\,dB'
\]
has maximum-to-minimum ratio at most \(B^5\). Given two boundary fields, gauge-transform one to agree with the other on a spanning tree. This is possible by solving at the seven non-root vertices. Change the \(B'\) frames along with it. Only five factors can differ in the resulting comparison. If just \(k\) tangential links change, the ratio is also at most \(B^k\) by direct comparison. The argument with exponential weights is identical. It applies both to the outer-slice convolution of \(W\) and to the entire unmarked arm \(N_1\).

For a perpendicular pair retain the coupled single-edge weights \(P(q(A_e^{-1}B_e))\) on both marked arms. Remove the 23 central squares touching the union of the two marked central faces' edge sets. In the two marked numerators remove \(W(B')(C^PW)(B')\), of oscillation at most \(B^{6+5}\) per arm. In each of the six unmarked arms replace \(N_1\) by its minimum over the selected central links at fixed other links. Two of these faces meet four selected edges, and four meet seven. Their total cost in the exponent is at most \(2\cdot4+4\cdot5\). The reference thus obtained has density ratio oscillation at most \(B^{73}\) against the original law. Minimization preserves vertex-gauge invariance by a change of the minimizing variables. Under the reference the selected central edges are independent uniform Haar after the partners of each edge are integrated. Given those edges, the partners are independent with the normalized one-link convolution law. The private frame averages are unchanged.

For the positive pair, 1485's subset decomposition therefore gives the reference bound \(1/3\). For clarity, any lifted conditional field \(H(A)=\mathbb E[F\mid A]\) is symmetric in the twelve edges. Only centred independent-edge components supported within the four shared edges contribute. At order \(k\ge1\) this is at most \(\binom4k/\binom{12}k\le1/3\) of their squared norm.

**Proved, use of the crossing weights on the mixed pair.** Both probes can be taken spectral for the actual supremum. The corresponding reference statistic \(F(A,B')\) is invariant under swap of the two arrays, since the swap transposes the matrix block and inverts the argument of the quaternion quadratic. Denote the fourth-order independent-edge component of \(H\) by \(H_4\). It is even in each link, since simultaneous sign changes of one \(A_e,B'_e\) preserve the statistic and the paired density. The one-link convolution on mean-zero even functions has norm \(<1/5\). Indeed the Wilson multipliers are \(r_j=I_{j+1}/I_1\), with even \(j\ge2\). The recurrence and 1489's \(r_1>23/48\) give \(r_2=1-4r_1/\beta<1/6\), and GL4 bounds the successive ratios by one. The normalized \(P\)-kernel differs in Haar \(L^1\) by at most \(b_0\), from the pointwise weight comparison and its normalizer. Integration of translations bounds the difference in operator norm by the same number. By tensoring, \(|\mathbb E H_4(A)H_4(B')|\le5^{-4}\|H_4\|^2\). For a centred unit probe, exchange symmetry gives
\[
 2\|H_4\|^2=\mathbb E F[H_4(A)+H_4(B')]
       \le\sqrt{2(1+5^{-4})}\,\|H_4\|.
\]
The mixed gauge projections remove every proper subset of the shared square by the forest argument of 1485. The single square has at most \(\|H_4\|^2/\binom{12}4\) after projection. Cauchy–Schwarz between the two fields gives the mixed reference bound \((1+5^{-4})/990<1/900\).

For an opposite pair use a different reference. Keep the two marked arms intact and keep the six internal squares in each central slice. Remove the twelve central plaquettes between slices and the six spectator arm factors. The resulting opposite observations are independent. The ratio oscillation costs at most \(B^{12+6\cdot5}=B^{42}\).

**Proved bounds, including the actual marginal tilts.** Apply the two-sided variance comparison of 1485 separately to each of these references. For both Wilson and \(P\),
\[
 p\le1-\tfrac23 B^{-73},\qquad
 m\le1-\tfrac{899}{900}B^{-73},\qquad
 o_1\le1-B^{-42},\qquad
 R<7-\tfrac{1499}{300}\,2^{-511}-2^{-294}.                  \tag{10}
\]
The reference coefficients themselves cannot be used as the interacting coefficients. The ratio cost in (10) leaves the upper endpoint above one.


## Which variables still couple the three Gram forms

**Proved.** Let \(Z_{ij}(F,G)\) be the unnormalized cross moment. Its central integrand is \(W_C\prod_{k\ne i,j}N_1(A_k)\) times the two marked arm numerators of 1489, including the private frame averages. On a mixed or opposite pair one may fully vertex-average both marked numerators after aligning the faces as in 1485 (5)–(6). The denominator \(N_1\) of each conditional field is gauge invariant and cancels its copy in the central density. This cancellation is specific to the cross moment. The one-face moment for the marginal Gram uses \(N_{FF'}\). In all three forms subtract the product of the normalized first moments.

For opposite faces factor out the two single-slice weights \(W(A),W(B')\). Integrating the eight normal central links leaves a polynomial kernel on two disjoint twelve-link arrays. It is separately vertex-gauge invariant, since the frames at the two ends can be changed independently before integrating the normal links. Each tangential link occurs in one remaining central plaquette and in two spectator \(N_1\)'s. From the arm convolution, \(N_1\) has degree at most ten in each central link. Hence this separating kernel has edge degree at most **30**. Expand each side in the trivalent cube spin networks of 1348 (6)–(7). There is one coefficient index for each admissible choice \(0\le j_e\le30\), with the triangle and even-sum conditions at every vertex. The cross form acts only on the one-face functionals \(\int W(A)N_F(A)\psi_{\bf j}(A)\,dA\) in these degrees. It has no omitted tail in the separating variables. The bound on allowed labels alone is too large for a dense computation because taking every \(j_e\) even between 16 and 30 gives \(8^{12}\) admissible tuples before the coefficients are examined. This counts a containing space, without asserting that all these coefficients are nonzero.

For a perpendicular pair, extract on each marked face the five internal plaquette factors other than the common square. Keep the common plaquette once. The sixteen central edges private to one of the two faces again have degree at most 30 in the remaining weight, by the same incidence count. Integrate the twelve central links outside their union. Calling the four shared links \(t\), expand this remaining polynomial in the sixteen private edges only. This writes the cross moment as a finite sum of integrals over \(t\) of a polynomial coefficient times two arm functionals, one on each side. Each functional integrates its eight private central edges against a matrix-coefficient monomial with labels at most 30, its five internal weights and its marked numerator. For the fully averaged mixed integrand choose three shared edges as a gauge tree. Their oriented product with the fourth edge serves as the fourth Haar coordinate. Successive changes of the other incident links preserve product Haar and set the three tree edges to identity. Residual conjugation reduces the remaining holonomy to \(U=(x,\sqrt{1-x^2},0,0)\), \(x\sim\sigma\). These gauge changes are made before expanding the private coefficients. Thus there is only **one continuous shared class parameter** for the mixed form. For the positive form the shared site charges must be retained. The moving endpoint (4) explains why the mixed dependence on \(x\) cannot be exhausted by a fixed finite list of modes on arbitrary probes. It persists after deleting the collar in (5) by taking all the thresholds in \((u(\pi/2),12(1-1/162))\) and test on this interval of endpoint values. At each maximizing configuration used there \(M=0\), so a relative neighbourhood remains in the interior.

**Proved, a separate angular tail without the reciprocal density.** The aligned positive-pair operator commutes with simultaneous left \(SO(3)\) rotations of both matrices \(M\), by a common conjugation and the independent private right rotations. Its marginal is left invariant. On left spin \(\ell\ge1\) its operator norm is at most
\[
             \min\{1,\,2^{509}/[\ell(\ell+1)]^2\}.                \tag{11}
\]
To see this, extend \(k_z\) by zero as above and let \(P_\ell\) be the left angular projection with respect to rotations. On its range the positive rotation Laplacian has eigenvalue \(\ell(\ell+1)\). Indeed, on lifting the rotations to unit quaternions, a unit rotation generator has half the speed and the degree-\(2\ell\) spherical harmonics have eigenvalue \((2\ell)(2\ell+2)\) by the polar Laplacian. Each infinitesimal left matrix rotation is a sum of six terms \(M_{kl}\partial_{M_{ij}}\) with signs. Its fourth iterated products involve at most \(6^4\,4!\) signed terms of derivative order at most four, with coefficients bounded by one on the support. The square of the rotation Laplacian has nine such words. Hence the \(L^2(\ell)\) norm of that square applied to \(k_z\) is at most \(2^{19}H_5\). (Here \(L^2(\ell)\) denotes the uniform cube measure of 1489.) It follows that \(\int_K|P_\ell k_z|\,d\ell\le2^{509}/[\ell(\ell+1)]^2\). In the kernel against the true marginal the angular projection commutes with division by its rotation-invariant density, giving the preceding integral as its absolute row integral. Null sets can be discarded. Reflection symmetry gives the identical bound on column integrals. Cauchy–Schwarz with the absolute kernel and the two integral bounds gives (11). Distinct spins are orthogonal for the operator. Spins \(\ell\ge2^{130}\) are each below \(1/2048\), without summing that error over spins. The numerical cutoff supplied by this uniform estimate remains large.


## Removing the shared-square endpoint from the remaining test

**Proved.** The large-trace region producing the moving endpoint (4) can itself be removed at small operator cost. For \(T=\operatorname{tr}Q/(4\beta)\) and every other observation, in both laws,
\[
              \Pr(|T|\ge 12-5/8\mid Y_j)<2^{-22}.                \tag{12}
\]
On a perpendicular pair choose the four parallel edges of the first face joining the shared square to its opposite square. Their four far endpoints are outside the other face. Independent gauges at those vertices turn the four links into independent Haar quaternions while preserving \(Y_j\). On an opposite pair designate one square and the same four matching edges. They are independent Haar given \(Y_j\) there as well. The other four edges of the private square are private central links. Bound their one-link densities by \(72\) using the beta moment in (5) with exponent 28, since \(2(6\beta)\le28\) and \((1+b_0)^6/\mathbb E[((1+q)/2)^{28}]<72\). All twelve neighbour links have density bound 42. In a sequential exposure, use the four exact Haar links first, then the four bounded central links and finally the twelve bounded neighbour links. For the latter sixteen, the all-other-links bound persists under the coarser conditioning, since \(Y_j\) uses none of them. For the inward convention condition in addition on the independent crossing frames in 1485 (4), whose fixed left and right translations preserve all the Haar dominations. In these frames the trace is the same sum of products of scalars. Thus the twenty required links, given \(Y_j\), are dominated by \(72^4 42^{12}\) times product Haar.

For each link put \(x=1-|q|\) with Haar density at most \((4\sqrt2/\pi)\sqrt x\). On the large-trace event the sum of the twelve deficits \(1-|a_0 b_0|\) is at most \(c=5/8\). For each of the eight pairs with both links private write \(x=1-|a_0|,\ y=1-|b_0|\), and set \(v=(1-x)y\). The deficit is \(x+v\), with density majorant for these two coordinates proportional to \(\sqrt{xv}\,(1-x)^{-3/2}\). For the other four pairs the deficit is at least the neighbour's \(y\). The twenty nonnegative coordinates therefore have sum at most \(c\). The product of the eight Jacobian factors is at most \((1-c)^{-3/2}<5\) because \(\prod(1-x)\ge1-\sum x\). Extending the integral to the simplex as in (5) gives
\[
  \Pr(|T|\ge 12-c\mid Y_j)
    \le 72^4 42^{12}(8/\pi)^{10} (1-c)^{-3/2}c^{30}/30!
    <2^{-22}.
\]
The estimate bounds both signs at once.

**Proved consequence.** Use the core \(D_*=\{|s|+\|M\|_*<1-1/162,\ |T|<91/8\}\). By (5) and (12), its complement has conditional probability at most \(3\cdot2^{-23}<2^{-20}\). The two-sided covariance-operator argument after (5) bounds the total omitted contribution by \(14/1024\). Hence a \(24/25\) upper row on this core still passes. In particular the thresholds used to exhibit infinite rank in (4) all exceed this cutoff since \(8+4\cos(\pi/8)>91/8\). The lower-rank question inside \(D_*\) is separate. Multiplication by the core indicator is an analytic projection. Computing the restricted Gram norms requires integrating the indicator as well as the polynomial weights.

## A lower bound for the marginal density on the retained interior

**Proved.** In the whole region \(|s|+\|M\|_*\le1-1/162\), the one-face density against uniform cube measure satisfies \(p_i\ge 2^{-2050}\) almost everywhere, for both laws. This supplies a lower bound for every point in the core used after (12), including matrices with repeated or zero singular values.

First consider one pair of independent Haar quaternions. Write \(\alpha,\gamma\in[0,\pi]\) for their angles, \(c=\cos\alpha\cos\gamma\), \(r=\sin\alpha\sin\gamma\), \(x=r u\), and \(v\) for the second unit imaginary direction. The increment is \((c,xv^t)\). The independent angle density is \(4r^2/\pi^2\). For \(r>0,\ |c|+r<1\) choose
\[
 \alpha=\tfrac12(\arccos(c-r)+\arccos(c+r)),\qquad
 \gamma=\tfrac12(\arccos(c-r)-\arccos(c+r)).
\]
The absolute forward Jacobian is \(|\sin(\alpha+\gamma)\sin(\alpha-\gamma)|\le1\). With unit probability sphere measures, \(r^2\,dr\,du=dx/(4\pi)\). Thus a single-pair measure dominates \(\pi^{-3}\,dc\,dx\,dv\) throughout \(|c|+|x|<1\). This comparison recovers ten-dimensional Lebesgue measure from twelve random rank-one matrices.

Fix a target \((s,M)\) in the stated region and a singular value decomposition \(M=U\Lambda V^t\). Use three groups of four with means \(M_1=M+\eta UV^t,\ M_2=M_3=M-\eta UV^t/2\), where \(\eta=2^{-11}\). For each group choose a singular value decomposition \(U_g\Lambda_g V_g^t\), let \(r_g=\operatorname{tr}\Lambda_g\), and take the four sign vectors \((+++),(+--),(-+-),(--+)\) as in 1489. For sign vector \(\sigma\) use
\[
 c^0=s,\qquad x^0=\sqrt{r_g}\,U_g\sqrt{\Lambda_g}\,\sigma,\qquad
 v^0=V_g\sqrt{\Lambda_g}\,\sigma/\sqrt{r_g}.
\]
At \(r_g=0\) use zero \(x^0\) and arbitrary unit \(v^0\). These controls give the target exactly and each satisfies \(|s|+|x^0|\le1-1/162+3\eta\). In the first group every singular value is at least \(\eta\), and \(r_1\le1\). The matrix of its first three direction columns has smallest singular value at least \(\sqrt{\eta}>1/64\), since the three sign columns have Gram matrix with diagonal three and off-diagonal minus one.

Put \(h=2^{-24}\). Allow every \(v\) chord distance at most \(h\) from its chosen direction, which has sphere probability \(h^2/4\) apiece. Let eleven \(c\)'s vary within \(h\) of \(s\). On the nine edges other than the first three, vary each coordinate of \(x\) by at most \(h\). Solve linearly for the remaining scalar and the first three vectors to attain the target mean. The changed three-column matrix has smallest singular value above \(1/128\), by the Frobenius perturbation bound \(\sqrt3h\). Before correction the sum of the twelve outer products differs from \(12M\) by at most \(12h+9\sqrt3h<30h\) in Frobenius norm. Corrections to the first three vectors therefore have norm at most \(3840h\) each. The scalar correction is at most \(11h\). The slack exceeds \((3840+11)h\), so all the controls remain in the single-pair minorant. The inverse Jacobian of these ten solved coordinates is \(12^{10}/|\det[v_1,v_2,v_3]|^3\ge1\), by the unit column lengths. The resulting pushforward density against Lebesgue measure is bounded below by
\[
 \pi^{-36}(h^2/4)^{12}(2h)^{38}>2^{-1546}.
\]
Here 38 counts eleven scalar and 27 vector coordinates. This is a pointwise bound for the density formula obtained by the indicated linear changes and Fubini, irrespective of the choice of target-dependent integration boxes. Reflection or transposition for an inward face preserves the same bound. Restoring the conditional law of the 24 marked links costs at most \(B^{72}<2^{504}\) by the 72-plaquette count above. Multiplying by \(2^{10}\) to use the uniform cube measure can only improve the stated bound.

**Proved consequence for finite compression.** There is an explicit space that dispenses with the unknown polynomial \(b\) in (7). On \(D_*\) use the span of \({\bf1}_{D_*} L_\alpha/p_i\), with \(L_\alpha\) tensor Legendre polynomials of coordinatewise degree at most \(J\). On an omitted core probe \(F\) of unit marginal norm, orthogonality now gives \(\int_{D_*} F L_\alpha\,d\ell=0\), while \(\|F\|_{L^2(\ell)}\le2^{1025}\). Pair against a centred unit probe on the other face. Its conditional-density numerator has the same Legendre tail as in (7) by Cauchy–Schwarz over its marginal. The per-side errors for core compression are thus at most \(2^{1025}H_r/(J+2-r)^r\). The same bound applies with a core-projected opposite probe by centring that probe in the original marginal. If \(J-3\ge2^{306}\) for a perpendicular pair and \(J-7\ge2^{196}\) for the opposite pair, each error is at most \(2^{-14}\). A \(24/25\) row on those finite weighted spaces would pass even with both core cuts and both degree tails, since \(24/25+14/1024+14/16384<122/125\). The subspaces involve the true marginal density. Their Gram entries require the corresponding inverse-weight integration. The Gram norms on these weighted spaces remain open.

## A character tail on the fixed plane at arbitrary trace degree

**Proved.** Let \(f\) have unit marginal \(L^2\) norm. On an outward face allow arbitrary bounded functions of \(T\) multiplying polynomials of degree at most \(k\) in \(M\), and their linear combinations and \(L^2\) limits. At \(P\), with \(U\) the shared central square holonomy, put \(a_j=\mathbb E[f\,\chi_j(U)]\), where \(\chi_j=U_j(q)\) has dimension \(j+1\). Then
\[
 \left(\sum_{j\ge J}|a_j|^2\right)^{1/2}
    \le \sqrt{72}\,
       \min\left(1,\frac{61+k}{J+1}\right)^3 .                   \tag{13}
\]
This tail has no dependence on the trace degree. For trace probes \(j+1\ge1281\) already gives error below \(1/1024\) in the Haar coefficients. It controls the part on the shared square that uses its class alone.

To prove it, form the unnormalized-in-the-four-edges field \(g(A_\square)\) by integrating \(f\) times the full normalized density over the other raw links. In an outward transported frame the trace reads only the four scalar parts of these central links when the remaining variables are fixed. Their independent conjugations preserve these scalars. The density has degree at most 60 in each link, so \(g\) has conjugation spin at most \(60+k\) in each link. This assertion also holds by \(L^2\) continuity. The true four-link marginal density against product Haar is at most 72 by exposing three independent Haar tree links with vertex gauges, then using the conditional one-link bound of (12) on the fourth. Thus \(\|g\|_{L^2({\rm Haar}^4)}\le\sqrt{72}\|f\|_{L^2(\mu_i)}\) by conditional Jensen.

In the Peter–Weyl block of dimension \(d=j+1\) on one edge, conjugation acts on \(d\times d\) coefficient matrices with their Hilbert–Schmidt norm. Spins \(0,\ldots,j\) occur once, by the SU(2) character product rule. Their subspace through \(60+k\) has dimension \(h=\min(d,61+k)^2\). Choose a Hilbert–Schmidt orthonormal basis \(T_a\) there. Then \(\sum T_a^*T_a=(h/d)I\) by invariance, Schur's lemma and the trace. Project the normalized square character onto these subspaces on four consecutive edges, reversing orientations as needed, which is unitary. Its squared norm is
\[
 d^{-4}\sum_{a,b,c,e}|\operatorname{tr}(T_aT_bT_cT_e)|^2
       \ \le\ d^{-4}\sum_{a,b,c}\|T_aT_bT_c\|_{\rm HS}^2
       \ =\ h^3/d^6 .
\]
The prefactor follows from the four \(\sqrt d\) factors in normalized edge coefficients. The inequality is Bessel's inequality, with adjoints of basis matrices where required because the subspace is adjoint-stable. Projected cycles for distinct \(j\) remain orthogonal. Since \(g\) is in the conjugation cutoff, Bessel's inequality against these orthogonal projected cycles proves (13).

**Proved, conversion to the physical square marginal.** Its class density \(w(U)\) is a polynomial of degree at most 60 in \(q(U)\). Fix three tree links and solve for the fourth at fixed product. Its entries are then linear in \(U\), and the remaining integrations preserve polynomial degree and conjugation invariance. The one-link minimum-to-maximum ratio gives \(w\ge2^{-42}\). The class conditional field \(h_f=\mathbb E[f\mid q(U)]\) has \(w h_f=\sum_j a_j\chi_j\). Consequently dividing the truncated series by \(w\) gives error in \(L^2(w\,d\sigma)\) at most \(2^{21}\) times (13). For \(k=0\), retaining \(j+1<163968\) gives error below \(1/1024\), since \(163968=61\cdot21\cdot128\) and \(21^3>9\cdot1024\). Multiplication by \(w\) has bandwidth 60 in the character basis by the product rule. For any rational polynomial approximation \(q\) to \(a/w\), where \(a\) is a finite character sum, its inverse-weight quadratic form obeys the exact upper test
\[
 \langle a,w^{-1}a\rangle
 \le 2\langle a,q\rangle-\langle q,wq\rangle
              +2^{42}\|a-wq\|^2 .
\]
All three pairings on the right are Haar pairings. This follows by completing the square and permits a banded residual check without forming a dense inverse. The full mixed reflection form also contains the private-edge coefficient functionals described above. An upper bound for the class projection alone cannot certify the full mixed form.

**Proved extension to charged private coefficients in the mixed form.** For one marked numerator put \(U_i(A)=W_{i\setminus I}(A)N_1(A)\) and \(v_F(A)=W_{i\setminus I}(A)N_F(A)\), where \(W_{i\setminus I}\) is the product of the five extracted face weights. Use the Haar \(L^2\) norm on this twelve-link array. Before the full vertex gauge average, \(v_F\) on each shared edge has conjugation spin at most \(L=k+20\) because one extracted plaquette and one kernel factor have degree ten each and the trace dependence is class invariant on that link. Project the private edges to labels at most 30, as allowed by the separating kernel. After the vertex gauge average, the part with any shared edge label \(j\ge J>60\) then has norm at most
\[
 \eta_J\|v_F\|_2,\qquad
 \eta_J=\min\left(1,\frac{496^2(L+1)^2}{(J+1)(J+1-60)}\right). \tag{14}
\]
Indeed each vertex on the square has just one private edge. The total twice spin of its two shared ends must therefore be at most 30. In a fixed shared-edge block write \(Q\) for the tensor product of the four vertex projections to these allowed totals. Each vertex projector has rank at most \(\sum_{h=0}^{30}(h+1)=496\). Tracing over one end gives its rank divided by the dimension of the remaining end times the identity, by Schur. Choose an edge with label \(j\ge J\) and its opposite on the square. Nonempty vertex projections require adjacent labels to differ by at most 30, so the two edge dimensions \(d_1,d_3\) are at least \(J+1,J+1-60\). On those two edges the independent conjugation cutoffs have ranks at most \((L+1)^2\) each. Taking the partial trace over the intervening edges gives
\(\operatorname{tr}(Q P_L^{(1)}P_L^{(3)})\le496^4(L+1)^4/(d_1^2d_3^2)\).
This bounds the squared operator norm of the product of the projections. The actual invariant projection has range inside \(Q\), and the private-edge cutoff commutes with vertex gauges. Distinct shared-edge blocks are orthogonal, which proves (14).

For converting (14) into a Gram error, let \(K_0\) be the positive remaining central weight after extracting the two five-square factors and integrating the twelve outside central links. Write \(D_0=\sup K_0/\inf K_0\), \(D_U=\sup U_i/\inf U_i\), common to the two marked faces by symmetry. The unnormalized bilinear integral with weight \(K_0\) on the two private arrays and the common square is bounded by \(\sup K_0\) times the product of the flat face norms, by Cauchy–Schwarz. Conditional Jensen gives \(\|v_F\|_2^2\le Z\,D_U\|F\|_{\mu_i}^2/\inf K_0\). Indeed the marked-face marginal contains \(U_i(A)\) times the integral of \(K_0 U_j\), divided by \(Z\), and \(|N_F/N_1|^2\) is bounded by its conditional second moment. Dropping the shared tail on both sides therefore costs at most \(2 D_0 D_U\eta_J\) on centred unit probes. One can use \(D_U\le B^{10}\) and \(D_0\le B^{27}\). For the latter match two arrays on a spanning tree of the union of the faces, which has 20 edges and 12 vertices. Each of the nine remaining selected edges enters at most one unextracted central plaquette and at most two spectator kernels. Gauge-change the integrated links before comparing. These worst-case ratios give a large cutoff. The estimate covers the finite private spectator labels, whereas (13) gives the much smaller constants for the pure class component. Both estimates leave the dependence on transverse degree \(k\) explicit.

## The opposite form at unbounded trace degree

**Proved for \(P\).** If one opposite probe is an arbitrary function of the scalar trace \(T\), its cross numerators against *all* probes on the other face have rank at most **18157**. More generally allow arbitrary functions of \(T\) multiplying spectral polynomials of transverse degree at most \(k\) in \(M\). An upper bound for the rank on that side is
\[
  (18157+24k)\ \#\{(a,b,c)\in\mathbb N^3:2a+3b+4c\le k\}.
  \tag{15}
\]
There is no truncation of the separating edge spins or of the scalar probe. Here the spin-network count \(8^{12}\) above can be replaced by a one-variable moment bound for each transverse polynomial. The result uses disjoint opposite arrays. Equation (4) prohibits its \(k=0\) conclusion for the perpendicular forms.

For a fixed transverse polynomial \(H\) of degree at most \(k\) and any opposite probe \(G\), form the signed measure \(\nu_{H,G}(dt)=\mathbb E[H(M)G\,{\bf1}_{T\in dt}]\). One can integrate the rest of the star first because \(G\) uses none of the 24 marked tangential links. Fix crossing frames in doing so. The integrand on the marked links is a polynomial of degree at most 60 on each single quaternion before inserting \(H\). Translations of the transported links preserve that degree. Expand \(H\) using \(M=\sum{\bf a}_e{\bf b}_e^t/12\). Each term adds \(k_e\) to each of the two quaternion degree caps on edge \(e\), with \(\sum k_e\le k\). Separate the imaginary directions conditional on each scalar part as in (3). Their moments leave monomials in \(x_e=q(a_e),y_e=q(b_e)\), of degrees \(u_e,v_e\le60+k_e\). The measure is a linear combination of convolutions of the twelve pushforwards of \(x^{u}y^{v}d\sigma(x)d\sigma(y)\) by \(z=xy\). This reasoning applies first to bounded \(G\). For general square-integrable \(G\) use truncation in the true marginal and convergence in total variation, since \(H\) is bounded and the resulting measure space below is finite dimensional.

Set \(x=\cos\alpha,\ y=\cos\gamma\) on two uniform circles, inserting \(2\sin^2\alpha,\ 2\sin^2\gamma\) for the semicircle laws. Translation by \((\pi,\pi)\) kills unequal parities of \(u,v\). Otherwise the two finite trigonometric weights have modes \(l,m\) of the same parity with \(|l|\le u+2,\ |m|\le v+2\). The torus homomorphism \((\alpha,\gamma)\mapsto(\alpha+\gamma,\alpha-\gamma)\) pushes probability Haar to probability Haar. By the product-to-sum formula the Laplace transform of each term is a rational coefficient times
\[
 I_{|(l+m)/2|}(t/2)\ I_{|(l-m)/2|}(t/2).
\]
The two orders add to \(\max(|l|,|m|)\le62+k_e\). The two occurrences of \(I\) arise from independent circle integrals. Multiplying twelve such transforms and using the integer-order recurrence of (3) gives the span of
\[
 t^{-h}I_0(t/2)^r I_1(t/2)^{24-r},\qquad
 0\le h\le d=744+k,\quad 0\le r\le24 .
\]
This also gives rational scalar-moment coefficients term by term from the power series \(I_j(t/2)=\sum_{n\ge0}(t/4)^{2n+j}/[n!(n+j)!]\). Opposite inputs need not be rational for the real rank bound.

For clarity, multiply by \(t^d\) and repeat the local row argument following (3). The vector now has size 25, polynomial row degree at most \(d\), and Euler-system residue with diagonal \(-(24-r)\). A selected minor has degree at most \(25d+300\). Thus moments through \(24d+300=18156+24k\) distinguish every such signed measure. This bounds their dimension over the reals by \(18157+24k\). In fact a scalar function multiplying fixed \(H\) can be replaced by a polynomial in \(T\) through this degree with exactly the same opposite cross numerators, for bounded scalar probes or whenever the finitely many pairings exist. This statement preserves the cross pairings. The marginal variance can change.

A spectral polynomial restricted to diagonal \(M\) is invariant under permutations and even sign changes of its three signed singular values. The latter force the three monomial exponents to have equal parity. The even polynomials are symmetric polynomials in the three squares, and odd ones have a factor of \(\det M\) followed by such a polynomial. Their generators are therefore \(h_2=\operatorname{tr}(M^tM)\), \(h_3=\det M\), and \(h_4=\operatorname{tr}((M^tM)^2)\), since the third elementary symmetric polynomial in the squares is \(h_3^2\). Signed singular value decomposition extends this equality to every \(M\). This proves the monomial count in (15), also for the \(L^2\) closure of the indicated probes by continuity of the finite-rank map.

**Proved, retaining the true marginal Gram.** Write \(H_a\) for these transverse monomials and \(\mu_T\) for the trace marginal. The one-face measures \(M_{ab}(t)\mu_T(dt)=\mathbb E[H_aH_b\,{\bf1}_{T\in dt}]\) have the same transform description with degree \(2k\), by taking \(G=1\). For a centred fixed opposite \(G\) put \(n_a(t)=d\nu_{H_a,G}/d\mu_T\). The square of the dual norm of its cross functional on the one-face span is exactly
\[
              \int n(t)^t M(t)^\dagger n(t)\,d\mu_T(t).
\]
Indeed \(M(t)\) is the conditional Gram of the \(H_a\) given \(T=t\); conditional Cauchy–Schwarz puts \(n(t)\) in its range. Complete the square there and truncate the pointwise optimizing vector to bounded norm, then take the increasing limit. This step includes the full one-face weight \(N_{FF'}\). It leaves a matrix of one-variable densities of order equal to the transverse monomial count. In particular the marginal weight is scalar at \(k=0\). Neither the coefficients of the opposite coupling nor an upper bound on this integral for every opposite unit probe have been evaluated here.

**Proved, an exact observation space for the entire opposite form.** There is also a uniform, much larger moment cutoff for *arbitrary* one-face probes against an opposite face. Put
\[
 H=60,\quad D=33+4H,\quad m=\binom{20}{8},\quad
 b=12[4+2(4H+8D)],\qquad d_*=mb+4m(m-1).
\]
Write \(C\) for the centred opposite operator with the two congruent faces identified. Its entire range is the span of \(C L_\alpha\) for observed polynomials \(L_\alpha\) of total degree \(|\alpha|\le d_*\). On the orthogonal complement it is zero. Thus this choice of observation space gives zero opposite truncation error. The Gram on this space still includes the true marginal. Its size makes the smaller trace and transverse spaces of (15) preferable for explicit tests.

Here is a direction-uniform proof of the cutoff. For any direction in the ten observation coordinates, one Haar pair contributes \(a^t L b'\) for a real four-dimensional matrix \(L\) with the factor \(1/12\) included. Take its singular value decomposition, which preserves both Haar sphere laws, and write \(\lambda_l\) for the four singular values. As in (15), the weight is a sum of products of monomials on disjoint pairs, of degree at most \(H\) on each sphere. For a one-pair monomial \(a^\alpha(b')^\gamma\), expand the exponential in the four diagonal terms. A term can contribute only when the two exponents at each coordinate have equal parity \(\epsilon_l\in\{0,1\}\). Write the exponential indices as \(2k_l+\epsilon_l\), \(E=\sum_l\epsilon_l\), \(n=\sum_l k_l\), \(A=(|\alpha|+E)/2,\ B'=(|\gamma|+E)/2\). Spherical even moments in four coordinates are \(\prod_l(1/2)_{r_l}/(2)_{\sum r_l}\), by Gaussian polar integration. Using \((2k)!=4^k k!(1/2)_k\) and \((2k+1)!=4^k k!(3/2)_k\), the one-pair transform therefore has the form
\[
 {\rm const}\ t^E
 \sum_{n\ge0}\frac{w^n[z^n]\,S(z)P(z)^{-H-1/2}}
 {(n+A+1)!(n+B'+1)!},\qquad
 w=t^2/4,\quad P(z)=\prod_{l=1}^4(1-\lambda_l^2 z),\quad \deg S\le4H .
\]
Indeed on coordinate \(l\) the numerator series has base coefficients \((1/2+\epsilon_l)_{k_l}/k_l!\) multiplied by a polynomial in \(k_l\) of degree \((\alpha_l+\gamma_l)/2-\epsilon_l\). Applying that polynomial in \(z\,d/dz\) gives a numerator over \((1-\lambda_l^2z)^{(\alpha_l+\gamma_l)/2+1/2}\). Clearing the denominator to exponent \(H+1/2\) leaves numerator degree at most \(H\) per coordinate. This derivation also allows zero or coincident singular values.

Let \(h_n=[z^n]P(z)^{-H-1/2}\), \(F(w)=\sum_{n\ge0} h_n w^n/(n+D)!^2\) and \(D_w=w\,d/dw\). A monomial \(z^j\) of \(S\) contributes \(w^j\) times a polynomial of degree at most \(2D\) in \(D_w\) applied to \(F\). This follows by shifting \(n\) by \(j\) and taking the two factorial ratios, since \(A,B'\le32,\ j\le4H\). Writing \(P(z)=\sum p_jz^j\) and \(x^{\underline q}=\prod_{l=0}^{q-1}(x-l)\), the first-order identity \(P D_z(P^{-H-1/2})=-(H+1/2)(D_zP)P^{-H-1/2}\) gives
\[
 \sum_{j=0}^4 p_j w^j (D_w+(H+1/2)j)
       \big[(D_w+D)^{\underline{4-j}}\big]^2 F=0 .
\]
Equating the \(w^n\) coefficients amounts to dividing the recurrence for \(h_n\) by \((n+D-4)!^2\). This equation is monic of order nine and its residue roots are zero and \(-D,-D+1,-D+2,-D+3\). In the nine-component first-order Euler system for \(F,\ldots,D_w^8 F\), the coefficients have \(w\)-degree at most four. Each further derivative increases a polynomial row degree by at most four. Thus each single-pair transform is a row of \(t\)-degree at most \(4+2(4H+8D)\) in these same nine components. After twelve products its row has \(t\)-degree at most \(b\) in the \(m\) monomials of degree twelve in the components. Their Euler system in \(t\) has coefficient degree at most eight and residue eigenvalues that are sums of nonpositive numbers. The minor argument after (3) bounds the order of every nonzero row output by \(mb+4m(m-1)=d_*\), uniformly in \(L\).

Consequently, if any signed opposite numerator measure on the ten observation coordinates has all moments through \(d_*\) zero, every one of its directional Laplace transforms vanishes. Its compact support then makes that measure zero. For the range claim, if \(G\) is orthogonal to every \(C L_\alpha\) through the cutoff, the centred measure \(\mathbb E[(G-\mathbb EG){\bf1}_{Y_i\in dy}]\) has exactly these vanishing moments. Hence \(CG=0\). Self-adjointness follows from the opposite-face reflection, and the indicated polynomial image is finite dimensional and closed. This proves the claim without needing the eigenvalues of any moment matrix. On that span the norm is the largest absolute generalized eigenvalue of the forms \(\langle L_\alpha,C^3 L_{\alpha'}\rangle\) and \(\langle L_\alpha,C^2 L_{\alpha'}\rangle\) after quotienting their common marginal null directions. The composition uses the actual marginal conditional expectation at the intermediate face. The degree bound does not evaluate these forms.

## Verification and the pivot

**Proof scope.** The state space and arm law are those of 1485 and 1489. The support, field-rank, regularity, reflection and gauge arguments above are mathematical derivations. The eleven closed rational and integer statements below were checked by the Lean 4.36.0 kernel on this checkout. The single-threaded run used `nice -n 15`, `-j1 -M768` and `decide +kernel` with `import Std`. It exited successfully in 7.19 seconds with maximum resident size 653,623,296 bytes. The trusted base is the Lean kernel and the imported definitions. The declarations `fourierBudget`, `classCut` and `oppositeTrace` printed no axioms. Each of the other eight printed `propext`, `Classical.choice` and `Quot.sound`. The replay source below matches the file that produced those results. The analytic arguments are written proofs. The retained Gram norms are open.

```lean
import Std

namespace Interface1493

def beta : Rat := 23/10
def minorErr : Rat := 13 / (2:Rat)^20

def betaMoment : Nat → Rat
  | 0 => 1
  | k+1 => betaMoment k * (2*(k:Rat)+3) / (2*(k:Rat)+6)

def fac : Nat → Nat
  | 0 => 1
  | k+1 => (k+1) * fac k

theorem geometry :
    (32 * 4^4 / (945 * 10 * 2^9) : Rat) < 1/256 ∧
    (3:Nat)^2 * 3 < 7^2 ∧
    (16:Rat) * (1 - (1/14)*(1/4)) * 14 = 220 ∧
    13 * 481 = (6253 : Nat) ∧
    13*480 + 78 = (6318 : Nat) ∧ 6318 - 492 = (5826 : Nat) := by decide +kernel

theorem traceCaps :
    (8 * (15/16)^4 - 8 * (15/16)^2 + 1 : Rat) > 1/8 ∧
    (12*(127/128)^2 : Rat) > 12-3/16 ∧
    ((1 + minorErr) / (1 - beta/8) : Rat) < 2 ∧
    8 * (10/7 : Rat) < 12 ∧
    (13:Nat)*12 < 2^8 ∧
    (98304/128 : Rat) = 768 ∧ (98304/96 : Rat) = 1024 ∧
    (1024 / 128^2 : Rat) = 1/16 ∧
    (360 + 24 + 48*8 : Nat) = 768 ∧
    (52 + 769 + 2 : Nat) = 823 := by decide +kernel

theorem privateLink :
    2*4*beta ≤ 19 ∧
    betaMoment 19 = 6564120420 / (4:Rat)^19 ∧
    (1+minorErr)^4 < 42 * betaMoment 19 := by decide +kernel

theorem collar :
    (1/9 + 2/144 : Rat) = 1/8 ∧
    (12/2 * (1/8)^2 : Rat) = 3/32 ∧
    (256 * 144^3 * 42^12 * (2/3)^6 * (3/32)^18 : Rat) * 2^23
      < (fac 18 : Rat) ∧
    (24/25 + 14/2048 : Rat) < 122/125 := by decide +kernel

theorem fourierBudget :
    (61^3:Nat) < 2^18 ∧ (12^10:Nat) < 2^40 ∧
    (1 + 48^2 : Nat) < 2^12 ∧
    (104*8 + 40+30+12*5+2+10 : Nat) < 2*490 ∧
    (104*12 + 40+30+12*9+2+10 : Nat) < 2*720 ∧
    (416+40+31+2+10 : Nat) < 510 := by decide +kernel

#print axioms geometry
#print axioms traceCaps
#print axioms privateLink
#print axioms collar
#print axioms fourierBudget

theorem quadraticBlock :
    ((2/3) * (9/16 + 3/48)^2 * 8/5 : Rat) = 5/12 ∧
    (5/4 - 2/3 : Rat) = 7/12 ∧
    (4*((2/3)/(72*18) + (7/12)/(18^2)) : Rat) = 1/108 ∧
    (30/108 - (5/12)/2 : Rat) = 5/72 ∧
    ((5/72)/((2/15)*12^4) : Rat) = 75/(144*12^4) := by decide +kernel

theorem wholeRow :
    ((1+minorErr)*((11/4)^2 * (10/7))^2 : Rat) < 2^7 ∧
    (1/6 + minorErr : Rat) < 1/5 ∧
    ((1+1/5^4)/990 : Rat) < 1/900 ∧
    (23 + 2*(6+5) + 2*4 + 4*5 : Nat) = 73 ∧
    (12 + 6*5 : Nat) = 42 ∧
    ((3*(2/3) + 3*(899/900)) : Rat) = 1499/300 ∧
    (9*6^4*24 : Nat) < 2^19 ∧ 130*4 = 509 + 11 := by decide +kernel

#print axioms quadraticBlock
#print axioms wholeRow

theorem traceCut :
    2*6*beta ≤ 28 ∧
    (1+minorErr)^6 < 72 * betaMoment 28 ∧
    ((8/3)^3 : Rat) < 25 ∧
    (5 * 72^4 * 42^12 * (8/3)^10 * (5/8)^30 : Rat) * 2^22
      < (fac 30 : Rat) ∧
    (12 - 5/8 : Rat) = 91/8 ∧
    ((27/32)^2 : Rat) < 3/4 ∧
    (3 : Nat) < 2^3 ∧ (24/25+14/1024 : Rat) < 122/125 := by decide +kernel

#print axioms traceCut

theorem classCut : 61*21 = (1281 : Nat) ∧ 61*21*128 = (163968 : Nat) ∧
    72 < (9:Nat)^2 ∧ 9*1024 < (21:Nat)^3 := by decide +kernel

#print axioms classCut

theorem coreLower :
    (1/162 - 3/2^11 : Rat) > (3840+11)/2^24 ∧
    (1/64 - 2/2^24 : Rat) > 1/128 ∧
    2 * 36 + 50 * 12 + 23 * 38 = (1546 : Nat) ∧
    1546 + 7 * 72 = (2050 : Nat) ∧
    (1025 + 490 + 14 : Nat) ≤ 5 * 306 ∧
    (1025 + 720 + 14 : Nat) ≤ 9 * 196 ∧
    (24/25 + 14/1024 + 14/16384 : Rat) < 122/125 := by decide +kernel

theorem oppositeTrace :
    12 * 62 = (744 : Nat) ∧
    (24 * 25 : Nat) / 2 = 300 ∧
    24 * 744 + 300 + 1 = (18157 : Nat) ∧
    (31 * 32 : Nat) / 2 = 496 := by decide +kernel

#print axioms coreLower
#print axioms oppositeTrace

end Interface1493
```

**Proved implication from 1475 §5.** A local pass would supply a contraction on this isolated pure-Wilson star. The first join still has charged shared links and four-linear corner interactions. The eight twisted unnormalized masses at each of the two periods enter the neutral purity. A common volume pressure cancels there, and a per-mass log error \(\delta_0\) costs up to \(3\delta_0\) in log purity. A local refutation would rule out this particular seven-exit criterion. Neither consequence is triggered by the current bounds. [Pivot and pressure](gap-k2-pivot-environment-astra62.md)

## Next two rows and their decisive outcomes

1. **Sketched. Certify the interior forms.** Use (14) on the mixed pair, the finite trace and transverse measures in (15) on the opposite pair, and the low rotation blocks on the positive pair. Bound the actual marginal Gram for each functional, including \(N_{FF'}\). A multiplicity-weighted upper sum of \(24/25\) on \(D_*\), counting (5) and (12) on both sides, passes the local Wilson test. For a polynomial compression using (7), a certified total including both sides of at most \(122/125\) also passes. A rational polynomial trial row at least \(257/251\) refutes it. The arithmetic and rank statements here do not evaluate these interior norms.
2. **Sketched, conditional on a pass. Test the first join.** Carry the charged shared links, the corner tensors, and all sixteen twist/period masses. A join-stable contraction with a common bulk pressure and winding error within the \(1/100\) budget, or a strict decrement with quantified scalar error, advances the pivot. A charged boundary probe that violates that contraction refutes the proposed extension. A local refutation from the first row ends this criterion before a join. [End-class contract](gap-k2-end-class-fable.md)
