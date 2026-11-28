# Repo search

**GUIDE.** Row 1163, pinned at `b61681c80`. The target-specific prior file is absent. The lead’s November 8 search inventories thirteen earlier problems and the gap supplement identifies the relevant neighboring projects. I checked main at `8b11ae2bb9` (the finite-clock Villain covariance note, lines 1–24), PR 10114 at `f76f6c649c` (MASS_GAP_LOCAL_BLOCK_ASTRA, lines 1–11), PR 10133 at `89faef229f` (APPROACH_REGISTRY, lines 226–228), PR 10134 at `1e70c7211a` (hard-route goal, lines 1–14) and PR 10141 at `a2f6a430e2` (fp1, lines 302–315). The first uses a finite cyclic group and a Villain action. The soft route gives a fixed-spacing Wilson estimate at \(0<\beta\le1/32\) and identifies the physical crossover as open. The older hard-route goal concerns existence, and fp1 controls a constrained classical field in one blocking step. The registry’s W points to the reconstruction tree. I found no other owner of this continuation. [Lead search](prior/repo-search-2026-11-08.md) · [Gap supplement](prior/gap-crux-prior-ym.md) · [Registry](open-registry.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the positive projected Wilson transfer and the periodic trace identity in outline lines 2313–2336 (chunk 02, GL8). Outline lines 31871–31882 (chunk 29) distinguish decay from a spectral gap. CA-I lines 2704–2712 leave the gap open. The index of CA-I §§4.12–4.19 concerns the ultraviolet induction. Tadeusz Bałaban supplies the upstream RG method. Sourav Chatterjee’s weak-coupling free-energy method enters the earlier rows. I use no numerical result from any of these sources. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2313-L2336) · [Complete account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712)

## The target and the two alternatives

**GUIDE.** The starting plan was to check prior ownership, recover the quantifiers of (W), and test the preceding reductions against the actual Wilson transfer. Every conditional PROVED statement below concerns the displayed implication. Row 1163 is research text without scientific or audit status.

**OPEN.** On the assigned trajectory \(a_j\to0,\beta_j\), at physical side \(L\) on the allowed dyadic grid put \(n=L/a_j\). Let \(U=F_0/\|F_0\|\) denote the periodic Wilson transfer on the whole physical slice. One form of (W) asks for \(\limsup_j(\operatorname{Tr}U^{n/2}-1)<1/1650\) at one fixed side, allowing dyadic enlargement for equivalence. Row 720 gives the equivalent excess-free-energy and spectral-gap criterion. Passing from this seed to a continuum mass gap requires the lane’s separate continuum hypotheses. [Row 720, §3.1](gap-phys-seed.md) · [Council brief](gap-council-brief.md) · [Gap part](../parts/gap.md)

**GUIDE.** Row 1161 is an unchecked input at the pinned commit. Its one-cube argument uses multiplicity from fractional spatial momentum, positivity of crossed electric Fourier coefficients on rectangular tori, and their time slopes at the symmetric torus. With \(4\mid n\) and a periodic electric-neutral trace at most \(3/2\) by time \(\lfloor n/512\rfloor\), it yields either a periodic seed or an all-magnetic neutral seed. Both give a Pfaffian seed. Its fixed-coupling exclusion test is sublinear elementary-twist cost along an unbounded sequence. Its lower count on microscopic neutral levels leaves the thermal upper bound at physical time open. I keep these inputs conditional on their hand arguments and pursue estimates after and before branch selection. [Row 1161, (9), (13), (19), (26)](gap-solve9-astra62.md) · [Council synthesis](gap-council-synthesis.md)

**GUIDE.** The direct test of (W) is (23), a signed sum over the two ordinary periodic partition functions' zeros. The unconditional count (31) explains why their locations and signs matter. Under the separate cylinder hypotheses, (26) gives spectral weight in physical energy and momentum bands, and (27) counts the levels visible at short times. The last section records the obstruction at the physical seed time.

## What a neutral seed forces in the ordinary periodic free energy

**PROVED, given the seed propagation of Theorem S-w.** At one fixed bare coupling put \(Z=Z_0\) and \(V=|Q|\). Use the three crossing-symmetric partition functions
\[
 W_P=Z,\qquad W_M=\tfrac18\sum_B Z_B,\qquad
 W_K=\tfrac18\sum_B(-1)^{\mathrm{Pf}(B)}Z_B .
\]
In any time frame each includes the periodic neutral trace. Their other seven terms are positive electric-sector traces. In that frame each of the eight terms in \(W_P\) is bounded by the periodic neutral trace, since temporal-twist integrals are positive. Also \(Z_B\le Z\) by deleting temporal seams in successively chosen frames. Consequently
\[
 Z/8\le W_K\le W_M\le8Z .
 \tag{1}
\]
The inequality \(W_K\le W_M\) follows either term by term in the twist sum or in the electric Fourier decomposition. In particular all three bulk log pressures \(f=\lim_{b\to\infty} b^{-4}\log W(b^4)\) coincide. All three have the same top transfer eigenvalue \(\lambda_b\) on the periodic spatial box \(b^3\). These transfer and crossing facts are from the lane’s proof for the three sector sets. [Theorem S-w and Lemma W](gap-flux-exercise.md) · [Twisted transfer](gap-transfer-twisted.md)

**PROVED.** Suppose a periodic or all-magnetic neutral seed \(s<1/5041\) is given on spatial side \(n_0=2N\), time \(N\). Put \(q=5041s<1\). For \(b\ge n_0\) with \(2^k n_0\le b<2^{k+1}n_0\), set \(v=q^{2^k}/71\). On \(b^4\) put \(D(b)=\log Z(b^4)-fb^4\) and \(\Phi_2(b)=16\log Z(b^4)-\log Z((2b)^4)\). With absolute constants, as \(v\downarrow0\),
\[
\begin{array}{c|cc}
 \text{seed at }n_0 & D(b)&\Phi_2(b)\\ \hline
 P & O(v)& O(v)\\
 M & \log8+O(v)&15\log8+O(v).
\end{array} \tag{2}
\]
Thus even the second alternative has bounded ordinary excess. Its excess at large sizes can be measured without inserting a twist or computing a transfer eigenvalue. The constant \(\log8\) for a frozen finite group appears in the earlier rigidity work. Here it follows for the actual Wilson torus under the second seed, with a uniform exponential error. [Earlier constant for the frozen theory](gap-uv-rigidity-max.md) · [Earlier excess propagation, Lemma Z3](gap-phys-seed.md)

**PROVED.** For whichever partition function has the seed, S-w gives \(S(b;b^3)\le v\), also at the shorter time \(2^{k-1}n_0\). Its excess \(D_w(b)\) is \(O(v)\). Here are details on the shape dependence of this step. Write \(d=2^k n_0,\ a=d/2\). At time \(a\) the log trace in units of the vacuum on \(d^3\) is at most \(v\). Lemma E' in the proof of S bounds the cost of replacing a side \(d\) by \(x\in[d,4d]\), at fixed \(a\), by a multiplier \(x/(d-a)\le8\) on that log trace. Apply it in three spatial directions. At the intermediate shapes used to double \(b^4\) one side at a time, all spatial sides are in \([d,4d]\). At the new time \(b\ge a\) the log trace is at most \(512v\). Each doubling in time cancels the vacuum exactly and gives \(0\le2\log W(b,B)-\log W(2b,B)\le 2\cdot512v\). Their coefficients \(8,4,2,1\) give a bound \(15360v\) on the doubling defect. Telescoping the bulk limit gives \(D_w(b)=\sum_{h\ge0}16^{-h-1}\Phi_{2,w}(2^h b)\), between zero and \(1024v\), since the later \(v\)'s decrease. This proof uses the positive sector transfer for the chosen seed. [Lemmas E and E', Theorem S](gap-crux-restate.md)

**PROVED.** In branch \(M\) write \(W_M/\lambda_b^b=1+S_M\) on the cube, \(0\le S_M\le v\). For every \(B\ne0\), there is a coordinate frame in which at least one nonzero component of \(B\) is purely spatial. In this frame \(Z_B/\lambda_b^b\) is at most the sum of the eight weights in that static class. Each is at most its neutral weight, which is included in \(S_M\). The frame change preserves \(\lambda_b\) on this cube. Hence
\[
 0\le\sum_{B\ne0}Z_B/\lambda_b^b\le 504v,\qquad
 Z/W_M=8-\sum_{B\ne0}Z_B/W_M .
\]
For \(504v\le4\), \( |\log(Z/W_M)-\log 8|\le126v\), by integrating \(1/x\) on \([4,8]\). Combining with the previous paragraph proves the second line for \(D\), and \(\Phi_2(b)=16D(b)-D(2b)\) gives its defect. In branch \(P\) the previous paragraph applies directly. The conclusions for \(s=0\) follow by using any positive upper bound on \(s\) and decreasing it to zero.

**PROVED (branch selection without a twisted observable).** Assume the physical Pfaffian seed with a strict uniform margin at one admissible size. Equivalently one can assume the one-cube neutral test of row 1161. By propagation and that row’s finite-aspect theorem, after a fixed dyadic enlargement there is at every sufficiently fine cutoff a \(P\) or \(M\) seed with a common strict bound \(q<1\). In the Pfaffian formulation the enlargement follows by propagating \(K\), bounding the neutral sum by the propagated \(K\)-sum, and enlarging the spatial cube at a fixed shorter time as in row 1161 after (10). For fixed \(j\), (2) then forces the alternative throughout its tail of lattice sizes. In particular (W) holds if and only if
\[
 \liminf_{L\to\infty,\ L\ {\rm dyadic}}\,
       \limsup_{j\to\infty}\Phi_{2,j}(L/a_j)<15\log8 .                 \tag{3}
\]
One can replace \(\Phi_2,15\log8\) by \(D,\log8\). If there are infinitely many \(M\) cutoffs, their estimates on the enlarged physical cubes have the same error tending to zero as \(L\to\infty\). The cutoff upper limit therefore tends to the displayed nonzero plateau. Otherwise the periodic seeds eventually give (W) and the upper limit tends to zero. The order of the limits and the upper limit over cutoffs matter. Also (BDD-\(\Delta\)) follows in either case. On the Pfaffian route, the outstanding part of row 720 is selection of the periodic spectrum. Condition (3) requires information on the actual periodic Wilson free energies.

## A magnetic branch requires an area-order number of distinct complex singularities

**PROVED (Wilson contact at the origin).** On an even \(b^4\) torus, \(b\ge4\), take an elementary twist in the \(12\)-plane. Write \(R_b(z)=Z_{12}(z)/Z_0(z)\) at complex isotropic bare coupling \(z\). Both integrals are entire and equal one at zero. Then
\[
 R_b(z)=1+O_b(z^{b^2}),\qquad H_b=R_b'/R_b=O_b(z^{b^2-1}).
 \tag{4}
\]
Use weights \(e^{z w_p}\), \(w_p=\operatorname{tr}U_p/2\), since the common constant cancels. A Taylor monomial has an odd plaquette set \(S\) consisting of plaquettes of odd multiplicity. If an edge is incident to an odd number of faces of \(S\), Haar invariance under changing the sign of that link kills the integral. Hence only mod-two cycles contribute. The twist changes a coefficient only if this cycle intersects the stack \(x_1=x_2=0\) oddly. The parity is the same for each of the \(b^2\) stacks at fixed \(x_1,x_2\). Indeed adjacent stacks differ by the coboundary of the intervening plane of links, which pairs to zero with a cycle. The disjoint stacks each require a face of \(S\). Every changed monomial therefore has total degree at least \(b^2\). This proves (4). The winding-sheet expansion and the Schwarz method are prior work. Row 1147 counts singularities along a spatial-coupling interpolation for a thermal ratio. Here the input is isotropic contact of order \(b^2\) for the vortex, and the conclusion counts a positive multiple of \(b^2\) distinct points even in an arbitrarily thin fixed neighborhood. [Strong-coupling winding terms](gap-seed-sc.md) · [Earlier Schwarz argument](gap-unit-check-opus.md) · [Row 1147, §8](gap-solve3-astra62.md)

**PROVED.** Fix a finite coupling \(B>0\) admitting an all-magnetic neutral seed at some lattice size. For each \(w>0\), let \(M_b(B,w)\) count the distinct points with nonzero order of the meromorphic function \(R_b\) in \(\{z:\operatorname{dist}(z,[0,B])\le w\}\). Cancel all common multiplicities first and count a point only once, irrespective of the remaining multiplicity or its sign. There are \(c(B,w)>0\) and \(b_0(B,w)\) such that
\[
                  M_b(B,w)\ \ge\ c(B,w)b^2
           \qquad(4\mid b,\ b\ge b_0(B,w)).                              \tag{5}
\]
The constants can depend on the witnessing seed. In fact the same conclusion holds if on some fixed nonempty closed interval \(I\subset(0,B]\) the modulus of the real log ratio is bounded below by a fixed positive number for all sufficiently large allowed \(b\). A single point lower bound need not give the interval argument below.

**PROVED (removing the poles).** It suffices to use \(0<w\le\min(1,B)\). Let \(P(z)=\prod_\zeta((z-\zeta)/D)\), with one factor \((z-\zeta)/D\) per counted point and \(D=4(1+B+w)\). Then \(|P|\le1\) in the tube. The function \(PH_b\) is analytic inside it, because logarithmic derivatives have only simple poles. On the closed tube of radius \(w/2\),
\[
                   |P H_b|\le C_{B,w} b^4 .                              \tag{6}
\]
For completeness, center a disk at real \(x\in[0,B]\). Each of \(V(q)=Z(x+q)/Z(x)\), for the two real positive integrals, has \(V(0)=1,\ |V(q)|\le\exp(12 b^4 |q|)\), by the bounded real action. There are \(O(b^4w)\) zeros, with multiplicity, in \(|q|\le w\). To see this, factor zeros in a disk of radius between \(2w\) and \(3w\) with zero-free boundary and take the circular mean of the logarithm of the modulus. A zero \(a\) adds \(\log(r/|a|)\) to the mean over its value at zero, by the power series for \(\log(1-z)\) on smaller radii and continuity of the integral. The zero-free factor has harmonic logarithmic modulus. Each zero inside \(w\) therefore costs at least \(\log2\) of the available \(36b^4 w\).

**PROVED.** Choose \(3w/4<r<w\) avoiding both zero sets on its circle. Divide \(V\) by \(r(q-a)/(r^2-\bar a q)\) per interior zero to get \(g\). These factors have modulus one on the boundary, so \(12b^4 r-\log|g|\) is nonnegative harmonic and its circular mean is at most \(12b^4 r\), since \(|g(0)|\ge1\). On \(|q|\le w/2\), differentiating the disk Poisson kernel \((r^2-|q|^2)/|re^{i\theta}-q|^2\) bounds its gradient by an absolute constant divided by \(r\). The Cauchy–Riemann equations give \(|g'/g|\le C b^4\). Each reflected denominator adds a term bounded by \(3/r\). Subtract the two logarithmic derivatives. The remaining terms have the form \(m_\zeta/(x+q-\zeta)\) with total absolute residue \(O(b^4w)\). Equal residues at a common zero cancel. Multiplication by \(P\) cancels each remaining denominator, at cost at most \(1/D\). This proves (6), including at the removable points.

**PROVED (transport with the zeros kept).** Put \(d=b^2-1,\ r_0=w/8\). Schwarz's elementary disk estimate gives \(|PH_b(z)|\le C b^4(2|z|/w)^d\) for \(|z|\le w/2\), by (4), (6) and the maximum principle applied after division by \(z^d\). On the tube of radius \(w/16\) about \([0,B]\) this gives
\[
                      |PH_b|\le C b^4 e^{-c_0 d}                         \tag{7}
\]
with \(c_0>0\) depending only on \(B,w\). Start with the disk of radius \(w/8\) at zero. Enlarge it to \(w/4\) inside the disk of radius \(w/2\). The log maximum at the intermediate radius is bounded by the average of the inner and outer log maxima, by applying the maximum principle on the annulus with a harmonic affine function of \(\log|z-x|\). Move the center at most \(w/16\) and repeat with the uniform outer bound (6). At most \(2+16B/w\) enlargements suffice. This only multiplies the initial negative exponent by a fixed positive factor.

**PROVED (avoiding the logarithmic loss per pole).** Shrink \(I=[\alpha,\gamma]\subset(0,B]\) if necessary so \(\gamma>\alpha>0\). Pick a fixed angular interval \(|\theta|\le\theta_0\) with \(0<\theta_0<\pi/8\) and \(B\theta_0<w/32\). There exist an angle \(\theta\) there and a radius \(r\in I\) such that, writing \(M=M_b(B,w)\),
\[
 \prod_\zeta|\sin(\theta-\arg\zeta)|\ge e^{-C_1 M},
 \qquad \prod_\zeta |r-|\zeta||/D\ge e^{-C_2 M}.
 \tag{8}
\]
There is no zero or pole at zero. For the angle, average the negative log of the product. The integral of \(-\log|\sin t|\) over a period is finite by the linear lower bound on the sine near a zero, so the average is at most a fixed constant per point. For \(r\), the integral of \(\log(D/|r-|\zeta||)\) on \(I\) is bounded uniformly in \(\zeta\), since \(-\log|u|\) is integrable at zero and all lengths are bounded. These two choices avoid every counted point on the path that follows.

**PROVED.** Travel from zero along angle \(\theta\) to \(re^{i\theta}\), then on its circle to \(r\). The path stays in (7). At radius \(s\) on the ray, the distance to each \(\zeta\) is at least \(s|\sin(\theta-\arg\zeta)|\), by projection perpendicular to the line through \(\zeta\) and zero. Thus \(|P|\ge(s/D)^M e^{-C_1 M}\). For \(s\le r_0\), retain the \(s^d\) disk estimate before (7). If \(M\le d\), the resulting upper bound on \(|H_b|\) is largest at \(s=r_0\), at most \(C b^4\,4^{-d}(D/r_0)^M e^{C_1 M}\). For \(s\ge r_0\) use (7) and that same lower bound on \(|P|\) evaluated at \(r_0\). On the circular arc (8) gives \(|P|\ge e^{-C_2 M}\). Hence if \(M\le c_*d\) with \(c_*=c_*(B,w,I)>0\) sufficiently small, the entire path has \(|H_b|\le C b^4 e^{-c_3d}\). Integrating along its bounded length gives \(|\log R_b(r)|\le C' b^4 e^{-c_3d}\), where the real logarithm at \(r\) equals the real part of the path integral. The real part is independent of winding around a zero.

**PROVED.** For an \(M\) seed at \(B\), continuity at that one finite witness size gives an interval \(I\) ending at \(B\) with a common strict seed margin. Row 1161 (14), or S-w with the elementary twist rotated to a static sector, gives \(R_b(x)\le C e^{-c b}\) uniformly for \(x\in I\). This contradicts the bound at the selected \(r\) for all sufficiently large \(b\). The stated version with a fixed nonzero lower bound on \(|\log R_b|\) has the same contradiction. This proves (5).

**PROVED (a weaker complex hypothesis suffices to select the seed).** Given the physical neutral input of row 1161, it suffices that for each sufficiently fine \(j\) there be some fixed \(w_j>0\) with \(\liminf_{4\mid b\to\infty} M_b(\beta_j,w_j)/b^2=0\). Apply (5) at the fixed coupling \(\beta_j\), prior to any cutoff limit. It excludes \(M\) there and leaves the physical periodic seed. This criterion permits arbitrarily many common zeros and an unbounded subarea number of uncanceled points arbitrarily close to the real axis. No uniform width in \(j\) is required. It gives a sufficient condition only. The unconditional zero count from the bounded action is of volume order, \(O_{B,w}(b^4)\), for either integral on this compact region. Whether enough zeros cancel for this criterion is open.

## How many fundamental links can carry a slow electric state?

**PROVED (an unconditional Wilson bound).** On a periodic spatial cube \(n^3\), choose a spatial direction \(i\) and, in every plane \(x_i=l\), an arbitrary deterministic subset \(A_l\) of the \(n^2\) forward \(i\)-links. The one-slice observation \(\mathcal O\) contains all the raw adjoint links, all fundamental links in the other two directions, and the fundamental \(i\)-links in the \(A_l\). Let \(h\) be a unit, gauge-invariant eigenfunction in the vacuum Markov space with normalized eigenvalue \(b_h>0\) and electric character odd in direction \(i\). At any finite \(\beta\ge0\),
\[
 b_h\|\mathbb E_\pi(h\mid\mathcal O)\|_2
 \ \le\ \prod_{l=0}^{n-1}\tanh\!\left[\beta(2|A_l|+|\partial A_l|)\right]
 \ \le\ \exp\!\left[-2n\exp\!\left(-12\beta\,\frac{\sum_l|A_l|}{n}\right)\right].
 \tag{9}
\]
Here \(\partial A_l\) counts transverse nearest-neighbor edges with exactly one endpoint in \(A_l\). This permits arbitrary nonlinear use of every observed link and of all transverse fundamental loops. Row 1157 (9) assumed oddness under specified *individual* link flips. Here the only symmetry hypothesis on the state is its physical plane character. Row 1161 (24) treats a different observation, the complete family of straight winding holonomies. [Earlier individual-flip estimate](gap-solve8-astra62.md) · [Earlier winding test](gap-solve9-astra62.md)

**PROVED.** Use a stationary vacuum pair \(X_0,X_1\). In pairing \(h(X_1)\) with any \(\mathcal O\)-measurable function \(f(X_0)\), project \(f\) first to the same physical character and average over spatial vertex gauges. These are contractions preserving the observation space and the pairing. Thus \(f\) is odd under the full cut in every plane \(l\), as the cuts differ by vertex gauges. On the observed data, flipping just the selected links \(A_l\) has exactly the same effect as the full cut. If one \(A_l\) is empty the pairing vanishes. Otherwise average over the group generated by these \(n\) disjoint partial flips on slice zero of a finite periodic cylinder. Condition on the orbit under this group, retaining every other link including \(X_1\). Haar measure assigns equal reference weight to the orbit signs \(\epsilon_l=\pm1\). Affected spatial plaquettes are precisely the transverse boundary plaquettes of the cuts. The two neighboring time layers supply \(2|A_l|\) affected temporal plaquettes. No affected plaquette reads two distinct \(l\)'s. The conditional law therefore has weight proportional to \(\prod_l e^{\epsilon_l J_l}\), with \(|J_l|\le\beta(2|A_l|+|\partial A_l|)\). On this orbit \(f\) is its reference value times \(\prod_l\epsilon_l\). The modulus of its conditional mean is at most \(|f|\prod_l\tanh[\beta(2|A_l|+|\partial A_l|)]\), and \(|f|\) is orbit invariant. Cauchy–Schwarz, followed by the fixed-box long-cylinder limit, bounds \(|\mathbb E f(X_0)\overline{h(X_1)}|\) by the product in (9) times \(\|f\|_2\|h\|_2\). First take bounded tests and then use \(L^2\) density; positive normalized transfer powers converge in trace norm to the simple vacuum projection. The eigenfunction equation gives the left side of (9) on maximizing over the tests. Finally \(\log\tanh x\le-2e^{-2x}\) for \(x>0\), \(|\partial A_l|\le4|A_l|\), and Jensen's inequality gives the last bound.

**PROVED.** At fixed \(\beta>0\), even with the full adjoint field on the slice and *all* transverse fundamental links, a family with \(\sum_l |A_l|\le(1-\epsilon)n\log n/(12\beta)\) has projection norm at most \(b_h^{-1}e^{-2n^\epsilon}\) for each such state. Thus the approximately conserved charges required by the magnetic alternative cannot be read with fixed nonzero \(L^2\) overlap by those observations. At fixed physical \(L\) with \(\beta\) of order \(\log n\), (9) retains its explicit size dependence. The fixed-\(\beta\) logarithmic-width conclusion uses the separate order of limits allowed by row 1161 (13).

**PROVED (one-step estimate on the whole charged space).** For the complete slice an improved form avoids the second temporal face per link. On a rectangular spatial box of sides \(n_i\), set \(A_i=\prod_{j\ne i}n_j\). For each static twist \(m\), with \(\lambda_m=\|F_m\|\), and each electric character \(q\), the one-step operator obeys
\[
 \|F_m|_q\|/\lambda_m \ \le\
      \prod_{i:q_i=1}\tanh(\beta A_i)^{\,n_i}.                           \tag{10}
\]
Use the one-step integral between gauge-invariant vectors. Fix \(y\) and the integrated temporal vertex gauges, and average the input \(x\) over independent full-plane flips in the specified directions. The magnetic multiplier is invariant. Each temporal plaquette of orientation \(0i\) belongs to exactly one plane, with a total exponent \(J_{i,l}\) satisfying \(|J_{i,l}|\le\beta A_i\). The unsigned integral averages its exponentials to \(\cosh J_{i,l}\). The charged integrand replaces each such factor by \(\sinh J_{i,l}\) because the input changes sign under every corresponding plane flip. The absolute bilinear form is at most the product in (10) times the unsigned form of \(|f|,|g|\). These are physical vectors, so the latter is at most \(\lambda_m\|f\|\|g\|\). This proves (10) on the whole sector. The earlier thin-section argument already identified the scale \(-\log\tanh(\beta A_i)\). [Thin-section area bound, N3](gap-skeleton-max.md)

**OPEN.** On a full cube, the exponent obtained from (10) for one charged direction is of order \(n e^{-2\beta n^2}\) at fixed \(\beta>0\), whereas the target needs a bound at physical time proportional to \(n\). Indeed the scalar cap in (10) tends to one even after raising it to \(\lfloor rn\rfloor\) for fixed \(r>0\). At the identity endpoint and identity temporal gauges the temporal sums saturate \(J_{i,l}=\beta A_i\). Thus no improvement of the power of \(n\) in that worst-case action cap follows by estimating each factor uniformly over those fields. A proof using the actual distribution of the coupled fields remains possible.

## A complete finite family for the neutral trace of the actual transfer

**PROVED (compression with relative error uniform in the slab length).** Write \(p=3n^3\) for the number of spatial links, \(D\) for the positive spatial magnetic half weight, and \(F=D P_{\rm gauge} C D\) on slice Haar space, with the usual common electric scalar suppressed. Each electric link of \(C\) has kernel \(k(w)=e^{\beta(w-1)}\), \(w=\operatorname{tr}(xy^{-1})/2\). Let \(F_+=P_+ F\) denote the periodic electric-neutral transfer, extended by zero outside its sector, and \(\lambda=\|F_+\|=\|F\|>0\). Given \(0<\eta<1/4\), take an integer \(d\) with
\[
              d+1\ge 4e\beta,\qquad 2^{-(d+1)}\le \eta/p .              \tag{11}
\]
Let \(\mathcal V_{d,+}\) be \(D\) times the gauge-invariant, electric-neutral polynomials of degree at most \(d\) on **each** quaternion link separately. Let \(\Pi\) be its Haar orthogonal projection. For every integer \(k\ge1\), put \(A=\Pi F_+^k\Pi|_{\mathcal V_{d,+}}\). Then
\[
 (1-2\eta^2)\frac{\operatorname{Tr} F_+^{2k}}{\lambda^{2k}}
 \ \le\ \frac{\operatorname{Tr} A^2}{\|A\|^2}
 \ \le\ (1-\eta^2)^{-2}\frac{\operatorname{Tr} F_+^{2k}}{\lambda^{2k}} .
 \tag{12}
\]
The span and its Gram matrix are specified before any vacuum or spectral calculation. This gives a completeness estimate for the actual Wilson open-slab moments. The comparison kernels keeping a finite family of neutral correlations fixed in row 1161 lack this estimate. No finite matrix has to be evaluated by a machine in the implication.

**PROVED.** Replace \(k\) on each link by
\[
 k_d(w)=e^{-2\beta}\sum_{r=0}^d [\beta(1+w)]^r/r! .
\]
At \(s=\beta(1+w)\le2\beta\), the relative omitted part \(e^{-s}\sum_{r>d}s^r/r!\) is a Poisson upper tail bounded by \((es/(d+1))^{d+1}\le2^{-(d+1)}\). For \(s>0\), multiply the summands by \(e^{t(r-d-1)}\ge1\), sum the entire exponential series and take \(t=\log((d+1)/s)\). The zero case follows directly. All individual kernels are nonnegative pointwise and positive semidefinite. Indeed \(w=x\cdot y\) in unit quaternion coordinates and \((1+x\cdot y)^r\) is a Gram kernel of tensor powers of \((1,x)\). Apply the two positive averages \(P_{\rm gauge},P_+\) and the unchanged \(D\) factors to the product kernel to obtain \(F_{d,+}\). The averages commute with the homogeneous product convolutions and preserve the polynomial degree on each link. Thus \(\operatorname{ran} F_{d,+}\subset\mathcal V_{d,+}\) and, pointwise in both endpoints,
\[
                   0\le F_+-F_{d,+}\le\eta F_+ .
\]
Here the inequalities are between integral kernels. They follow from \((1-\eta/p)^p\ge1-\eta\) before the positive averages. In particular \(\|F_+-F_{d,+}\|\le\eta\lambda\) by pairing absolute values of test functions with the positive kernel \(F_+\).

**PROVED.** Write \(Q=1-\Pi,\ B=F_+^k\). Then \(QB=Q(F_+-F_{d,+})F_+^{k-1}\). Before applying \(Q\), the latter product has kernel bounded pointwise in absolute value by \(\eta B(x,y)\), also for \(k=1\). Integrating its square gives \(\|QB\|_{\rm HS}\le\eta\|B\|_{\rm HS}\). By the orthogonal two-block decomposition and self-adjointness, \(\|B\|_{\rm HS}^2-\|\Pi B\Pi\|_{\rm HS}^2\le2\|QB\|_{\rm HS}^2\). For the unit vacuum \(\psi\), the one-step operator bound gives \(\|Q\psi\|\le\eta\). Test \(B\) against \(\Pi\psi/\|\Pi\psi\|\). Its overlap squared with \(\psi\) is \(\|\Pi\psi\|^2\ge1-\eta^2\), and \(B\) is positive in operator order. Thus \((1-\eta^2)\lambda^k\le\|A\|\le\lambda^k\). These two estimates give (12). The proof also gives \(\|Q\,{\bf1}_{[r,1]}(F_+/\lambda)\|\le\eta/r\) for every \(r>0\), by inverting \(F_+/\lambda\) only on that spectral subspace.

**PROVED (what would suffice at one size).** Use an independent spanning family \(f_i=Dp_i\) of \(\mathcal V_{d,+}\). Its matrices \(G_{ij}=\langle f_i,f_j\rangle,\ T_{ij}=\langle f_i,F_+^k f_j\rangle\) use a single-slice integral and an open Wilson slab. The eigenvalues of \(G^{-1/2}TG^{-1/2}\) are precisely those of \(A\), by orthonormalization. At \(2k=2\lfloor n/1024\rfloor\), an upper bound on the squared Hilbert–Schmidt norm of this matrix divided by its squared top eigenvalue of at most \((3/2)(1-2\eta^2)\) gives the neutral input of row 1161. This period is no later than \(\lfloor n/512\rfloor\). With \(\eta\to0\) polynomially in \(n^{-1}\) and \(\beta=O(\log n)\), degree \(d=O(\log n)\) suffices. The slab width and the number of probes may grow. This differs from assuming the answer for an unspecified dense family of tests. Combining (12) with (3) or the fixed-coupling condition following (5) supplies a conditional route to (W).

**PROVED (limitations of this reduction).** Any scalar polynomial approximating the *unprojected* one-link exponential within a fixed relative factor \(C\ge1\) everywhere needs degree at least \((\beta-2\log C)/\log(3+\sqrt8)\). Rescale to approximate \(e^{\beta x}\) on \([-1,1]\). It is bounded by \(C\) on \([-1,0]\), and its value at \(1\) is at least \(e^\beta/C\). For any polynomial \(h\) of degree \(d\), the polynomial \(u^d h((u+u^{-1})/2)\) has modulus at most \(\|h\|_{[-1,1]}\) in the unit disk by the maximum principle. Taking \(u=(3+\sqrt8)^{-1}\) gives \(|h(3)|\le(3+\sqrt8)^d\|h\|_{[-1,1]}\). Apply this to \(h(y)=p((y-1)/2)\). Thus when \(\beta\) is comparable to \(\log n\), the order of the degree in (11) is necessary for a pointwise polynomial comparison of this kind.

**PROVED.** For \(d\ge1\), the neutral span in (12) already has dimension at least \(2^{c n^3}\) at large \(n\). Take a stride-four family of \(M\ge c n^3\) spatial plaquettes on disjoint links. The \(2^M\) products of their normalized traces are neutral and orthogonal in raw product Haar measure: one unused plaquette trace has zero mean in every off-diagonal pairing. They have positive squared norms. Multiplication by the strictly positive \(D\) preserves linear independence. In particular an estimate that bounds every subleading singular value of \(A/\|A\|\) by \(e^{-c' n}\) and simply multiplies its square by the span dimension does not prove the needed trace bound. The linear-algebra obstruction is exact: in dimension \(m\), \(v v^*+\delta(I-v v^*)\), with \(v=m^{-1/2}(1,\ldots,1)\), is positive, has positive entries for \(0<\delta<1\), and has squared Hilbert–Schmidt norm \(1+(m-1)\delta^2\). The missing Wilson estimate is on the *sum* in (12) or its distribution over representations.

## A moving neutral state at bounded physical energy

**PROVED, conditional on the cylinder witness of row 865.** Fix its reference coupling and all the depth, source, free-kernel comparison and rectangular volume-transfer hypotheses of (SD-cyl-CA). Take a fixed admissible periodic spatial cube of physical side \(L\) that is an integer multiple of its reference side and contains the two test balls used below. Write \(a=a_j,\ n=L/a\). There are \(E_*<\infty\), \(J<\infty\) independent of \(j\) such that at every sufficiently fine cutoff the periodic **neutral** transfer has an eigenstate with
\[
 -a^{-1}\log\lambda_{\rm norm}\le E_*,
 \qquad \text{spatial momentum } 2\pi k/L,\quad 0<\|k\|_\infty\le J .
 \tag{13}
\]
The integer \(k\) can vary with cutoff. Row 865 gave one neutral state without specifying momentum. Here excluding zero momentum matters because powers of the phase of a moving state give many orthogonal trial states. No dispersion relation or particle interpretation is assumed. The source normalizations and the two-sided bound on positive tents are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Cylinder port, §§4–5](gap-sdcyl-ca-astra.md) · [Check of the port](gap-sdcyl-ca-check-opus.md) · [CA-I, lines 2727–2797](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2727-L2797)

**PROVED (two fixed scales and a bound on momentum).** First choose an admitted fixed physical scale \(D_0\le1/40\), small compared with \(L\), and later an admitted \(d\ll D_0\). Use the row 865 tent \(f=(d/4-|x-x_0|)_+\), a lattice time-reflection center, and its two time separations \(t_1=\lceil 3d/(2a)\rceil,\ t_2=2t_1\). Subtracting the common slab width \(w\) gives \(u_i=t_i-w\). Its centered slab vector \(v\) is spatial-centre neutral, and its time covariance at these separations is \(G_i=\langle v,U^{u_i}v\rangle\), by the cylinder transfer identity (use the physical Haar space here). Spatial translations act on \(v\) as they do on the tent. Average the tent over translations by \([-m,m]^3\) in lattice units with \(m=\lfloor d/(100a)\rfloor\). Denote the corresponding contraction on vectors by \(H\), and \(G=\langle Hv,U^{u_2}Hv\rangle\). Every pair in this last average consists of two of the original tents at time separation \(t_2\), with a spatial displacement of at most \(2\sqrt3\,d/100\). Each is still in the witness class at scale \(d\), with support separation in \([d,6d]\) and a common containing ball of radius \(5d\). They use exactly the same running coefficient. Thus for constants \(c,C>0\) independent of \(d,a,L\) at the fixed source parameters,
\[
 G\ge c\,d^2\bigl(g^{-2}+B^\sharp(s(d)+1)\bigr)^{-2},\qquad
             G_1,\ G_2\le C G .                                          \tag{14}
\]
This is a lower bound on a positive spectral weight and two *ratios* at one scale. It does not compare running coefficients at different scales.

**PROVED.** In the joint eigenbasis of \(U\) and the three commuting unit translations, at most \(G/16\) of \(G\) is at physical energies exceeding \(E_*=C_1/d\), by (14), time damping from \(u_1\) to \(u_2\), and \(a(u_2-u_1)\ge3d/2\). Choose \(C_1\) so that \(Ce^{-3C_1/2}\le1/16\). The spatial averaging multiplier in coordinate \(i\) has absolute value at most
\[
 \min\{1,[(2m+1)|\sin(\pi k_i/n)|]^{-1}\}.
\]
This follows by summing a finite geometric progression. Use signed representatives \(|k_i|\le n/2\), so \(|\sin(\pi k_i/n)|\ge2|k_i|/n\). By \(G_2\le C G\), at most \(G/16\) is at \(\|k\|_\infty>J\) on choosing \(J=\lceil C_2 L/d\rceil\) with \(C_2\) large enough. If (13) were absent, the weight outside \(k=0\) would be at most \(G/8\). It follows that the real connected covariance of the two averaged tents at separation \(t_2\) is at least \(3G/4\) for **every** relative spatial lattice translation: zero momentum contributes with sign \(+1\), and each other phase has real part at least \(-1\).

**PROVED (why the zero-momentum possibility is excluded).** Place two broad tents of radius \(D_0/4\), with spatial centers \(2D_0+O(a)\) apart and temporal centers \(t_2 a\) apart. In the interior spatial ball of radius \(D_0/8\) at each center place \(M\ge c_1(D_0/d)^3\) averaged little tents at the corresponding time. A spatial grid of spacing between \(d\) and \(2d\) on an inscribed cube suffices for all fine cutoffs. Their spatial supports at each end are disjoint, their spacetime supports lie inside their broad tent's support, and the sums \(F,H'\) at each end have height at most \(d/4\) and Lipschitz constant at most one (a sum of these disjoint nonnegative tents equals their maximum). Under the preceding zero-momentum consequence, bilinearity gives \(S^{\rm cyl}_2(F,H')\ge 3M^2G/4\).

**PROVED.** There is also a bound \(|S^{\rm cyl}_2(F,H')|\le C_{D_0}\) independent of \(d,j\). Call the broad tents \(B_1,B_2\). Expand the covariance by writing \(F=(B_1+F)-B_1,\ H'=(B_2+H')-B_2\). Each of the four pairs is in the row 865 class at scale \(D_0\). Adding the small tents keeps the support, increases height by at most \(d/4\), and gives Lipschitz constant at most two. A broad tent satisfies \((\int B_i)/(\|B_i\|_\infty D_0^4)=\pi^2/2560>1/300\). There is a strict margin for adding the smaller height. The separation lies strictly between \(D_0\) and \(6D_0\), and a ball of radius \(5D_0\) contains the pair. Apply the witness upper bound to each of the four positive pairs, at this one fixed scale. This argument uses neither positivity of arbitrary mixed covariances nor a bound for signed infinitesimal tests outside the witness class.

**PROVED.** By the source definition \(s(d)=\min\{s:C_W(s)L_{\rm block}^{-s}\le d\}\), where \(C_W(s)\) grows at most polylogarithmically in \(g^{-2}+B^\sharp(s+1)\). For large \(s\), \(C_W(s)\le L_{\rm block}^{s/2}\), so \(s(d)=O(1+\log(1/d))\). The lower bound \(3M^2G/4\) is consequently at least a constant times \(D_0^6 d^{-4}/(1+\log(1/d))^2\). Choose the admitted \(d\) small enough that this exceeds \(C_{D_0}\), before removing the cutoff, using the eventual depth admission in row 865. Then choose the cutoff sufficiently fine for both fixed scales. The contradiction proves (13). For all sufficiently large compatible physical sides the same two test scales and \(E_*\) work, while \(J\) is proportional to \(L/d\).

## Many neutral levels in physical energy units

**PROVED, with the same upstream hypotheses as (13).** At that fixed physical side, for all sufficiently fine cutoffs and each positive integer \(\ell\) with
\[
             \ell<n/J,\qquad \ell^2 a E_*\le\tfrac12 ,
\]
there is a neutral level of physical energy at most \(2\ell^2 E_*\) and momentum \(\ell k\) modulo the spatial reciprocal lattice. The levels so obtained lie in different momentum subspaces. More directly, if \(s_+(u)=\operatorname{Tr}_+ U^u-1\), then for every integer \(u\ge1\)
\[
 s_+(u)\ \ge\ \tfrac12 \min\!\left\{\lceil n/J\rceil-1,\
                           \left\lfloor(2 E_* a u)^{-1/2}\right\rfloor\right\}.
 \tag{15}
\]
In particular \(s_+(u_j)\to\infty\) at **every** \(a_j u_j\to0\) on this fixed physical cube. Row 1161 (19) is unconditional at \(\beta\ge1\) and excludes \(u=o(\log n)\). Equation (15) excludes the entire subphysical-time regime given the named ultraviolet cylinder hypotheses; the time \(\lfloor n/512\rfloor\) of its physical seed is proportional to \(n\).

**PROVED.** In the vacuum Markov space choose the complex unit eigenfunction \(z\) of (13) with translation character \(k\). For \(\ell\ge1\), \(w_\ell=|z|e^{i\ell\arg z}\), set to zero where \(z=0\), has norm one, is neutral and has character \(\ell k\). One coordinate of \(k\) is nonzero of absolute value at most \(J\), hence has order at least \(n/J\). These nonzero characters are distinct in the stated range. The phase map is \(\ell\)-Lipschitz: in polar coordinates use the squared-distance formula and \(|\sin(\ell t)|\le\ell|\sin t|\). For a stationary pair \(u\) steps apart its Dirichlet form is therefore at most \(\ell^2(1-e^{-u a E_*})\le\ell^2uaE_*\), using that the actual starting eigenvalue is at least \(e^{-aE_*}\). At one step the Rayleigh quotient is at least \(1-\ell^2aE_*\); \(-\log(1-x)\le2x\) for \(0\le x\le1/2\) gives the level assertion in its own momentum space by compactness. At \(u\) steps sum the quotients at least \(1/2\) on the indicated orthonormal states to obtain (15). The phase-map method is from rows 1157 and 1161. The bounded nonzero physical momentum in (13) is what allows its use in the periodic neutral, rather than magnetically twisted, transfer. [Earlier phase comparison](gap-solve8-astra62.md) · [Earlier fractional-momentum harmonics, (16)](gap-solve9-astra62.md)

## Counting neutral states with spatially translated sources

**PROVED, given (SD-cyl-CA) with its running-coupling bounds.** In the same fixed physical cube as (13), there are \(d_*>0\) and \(c,C>0\) such that for every \(0<d\le d_*\), at all sufficiently fine admitted cutoffs,
\[
 \#\{\,i\ne0:\ i\text{ periodic electric-neutral},\
                   E_i^{\rm physical}\le C/d\,\}\ \ge\ c\,d^{-3}.        \tag{16}
\]
The constants may depend on the fixed reference scale and source parameters. The same estimate holds simultaneously when the cutoff is fine enough for the tents at \(d\) and the admissible range of larger scales used below. In particular for a physical time \(\tau>0\) sufficiently small, taking \(d=\tau\) and the cutoff limit first gives a neutral excited heat trace at time \(\lfloor\tau/a\rfloor\) of at least \(c e^{-C}\tau^{-3}\) in lower limit. Equation (16) counts actual transfer levels with multiplicity. Its input is a two-point *cylinder* estimate with its original open suppliers. No infinite-volume spectrum or guessed dispersion is used.

**PROVED (bounds used from the witness).** Fix an admitted upper test scale \(D_{\max}\le1/40\) small enough that the depth assumptions hold throughout the subsequent tail of depths, with room for the two broad tents in the spatial box. Put \(l(x)=1+\log(1/x)\) in these physical units. For all \(x\le D_{\max}\), \(s(x)\) is between positive constant multiples of \(l(x)\) after adjusting constants. The upper bound was proved after (14); the lower bound follows from \(C_W(s)\ge1\). CA-I lines 2784–2789 give bounds proportional to \((g^{-2}+B^\sharp(s+1))^{-2}\) below and \((g^{-2}+\lambda_\sharp s-c_5)^{-2}\) above. The cylinder port keeps the same reference coefficient and the same factor-\(1/2\) relative margin. Thus a pair of positive tents with heights of order \(x\) in the admitted class has covariance between \(c x^2/l(x)^2\) and \(C x^2/l(x)^2\). The upper bound also applies to the padded pairs of height \(O(x)\) used below. Constants are uniform in \(x,j\) after the reference data are fixed. [Source depth and bounds](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2727-L2789) · [Cylinder transfer](gap-sdcyl-ca-astra.md)

**PROVED (the translation Gram matrix).** Use the original unsmoothed small tent at scale \(d\), the centered neutral slab vector \(v\), and \(u_1,u_2\) from (13). Set \(h=a\lceil d/a\rceil\in[d,2d]\) for \(a\le d\). In a fixed spatial cube of side, for instance, \(D_{\max}/20\), take its grid of centers of spacing \(h\), with \(N\ge c_{D_{\max}} d^{-3}\) centers. For \(z\in\mathbb Z^3\) write
\[
 K(z)=\langle v,U^{u_2}T_{h z}v\rangle,\qquad G=K(0).
\]
Here \(T_{h z}\) is translation by the indicated physical lattice vector. The \(N\)-by-\(N\) matrix \(K(j-i)\) is positive semidefinite and real, by the reflected slab representation. In particular \(|K(z)|\le G\) for all \(z\), and \(G\asymp d^2/l(d)^2\). We will bound the sum of its squared entries by \(C N G^2\). Absolute bounds applied separately to all off-diagonal entries would give an extra factor \(N\).

**PROVED (signed sums on two separated boxes).** For \(R\le\|z_0\|_\infty\le3R\), \(R\) a sufficiently large integer, take \(m=\lfloor R/512\rfloor\), \(I=[-m,m]^3\cap\mathbb Z^3,\ J'=z_0+([-2m,2m]^3\cap\mathbb Z^3)\). Set \(x=h|z_0|/2\) with Euclidean length here. We use these boxes only for differences of the fixed spatial cube and its immediate grid coverings, so \(x\le D_{\max}\), decreasing that cube by a fixed factor if needed. Use small tents in \(I\) at the first time and in \(J'\) at the second time. Then
\[
 \sup_{|s_i|,|t_j|\le1,\ \mathrm{real}}
 \left|\sum_{i\in I,j\in J'}s_i t_j K(j-i)\right|
              \le C x^2/l(x)^2 .                                         \tag{17}
\]
Indeed at each end split the signed sum of little tents into its positive and negative coefficient sums. Each sum is nonnegative, has height at most \(d/4\), Lipschitz constant at most one, and its support fits inside the support of a broad tent of radius \(x/4\) centered there. The last assertion follows from \(2\sqrt3 mh+d/4<x/4\) for the stated scale separation. Add and subtract the appropriate broad tents as in the proof of (13). The padded pairs at scale \(x\) have the required mass, slope, common ball and distance: the spatial centers are \(2x\) apart and their time centers differ by at most \(4d\). Take the absolute constant lower floor on \(R\) large enough for the strict mass margin there. The resulting fixed number of upper bounds gives (17). Translating all centers together does not change its left side.

**PROVED (how the signed sum pays for the number of offsets).** Give the columns independent fair signs \(t_j\), and choose \(s_i\) to be the sign of their row sum. For any real numbers \(c_j\), \(Y=\sum c_j t_j\) has second moment \(\sum c_j^2\) and fourth moment at most \(3(\sum c_j^2)^2\), by pairing indices. Hölder's inequality gives \(\mathbb E|Y|\ge(\sum c_j^2)^{1/2}/\sqrt3\). Every row \(i\in I\) sees all the offsets in \(z_0+I\), because \(i+z_0+I\subset J'\). Thus (17) gives
\[
 \sum_{z\in z_0+I}|K(z)|^2
       \le \frac{3C^2 x^4}{|I|^2 l(x)^4}
       \le \frac{C' d^4}{R^2 l(x)^4}.                                   \tag{18}
\]
The averaging is an exact inequality for finite sign sums. It requires no enumeration.

**PROVED.** Cover the integer shell \(R\le\|z\|_\infty<2R\) by a bounded number of these offset boxes. For example partition into cubes of side \(m\) and choose a point of the shell in each nonempty piece as \(z_0\); its translate of \(I\) contains that piece. The number is bounded by \((4R/m+3)^3\), an absolute constant above the fixed floor. Sum (18) over dyadic \(R\) from that floor to the diameter in grid units. For \(R\le d^{-1/2}\), \(x\le C R d\) gives \(l(x)\ge c\,l(d)\) for sufficiently small \(d\), and \(\sum R^{-2}\) is bounded. The larger shells pay at most \(C d\) in the sum over \(R^{-2}\), and \(d\,l(d)^4\) is bounded. The finite set of small offsets costs at most a constant times \(G^2\) by Cauchy–Schwarz. Consequently
\[
         \sum_{\text{offsets of the chosen grid}} |K(z)|^2
                            \le C d^4/l(d)^4\le C' G^2.                  \tag{19}
\]
Using translation invariance to get the same offsets in every row of (17) is essential to this power of \(d\).

**PROVED (rank in the physical energy window).** Form the Gram matrix \(K_{\rm lo}\) of the translated vectors \(U^{u_2/2}T_{hi}v\) after orthogonal projection to physical energy \(\le C_1/d\), using spectral powers if \(u_2\) is odd. These vectors are neutral and orthogonal to the vacuum. Their squared norms before projection are \(G\). As in (14), the earlier-time diagonal \(\langle v,U^{u_1}v\rangle\le C G\), so for sufficiently large fixed \(C_1\) every projected diagonal is at least \(G/2\). Also \(0\le K_{\rm lo}\le K_{\rm grid}\) as positive matrices, and (19) gives \(\operatorname{Tr}K_{\rm lo}^2\le\operatorname{Tr}K_{\rm grid}^2\le C' N G^2\). The first inequality follows by taking the trace of the product of the positive matrices \(K_{\rm grid}-K_{\rm lo}\) and \(K_{\rm grid}+K_{\rm lo}\). Cauchy–Schwarz on eigenvalues now gives
\[
 \operatorname{rank}K_{\rm lo}
      \ge (\operatorname{Tr}K_{\rm lo})^2/\operatorname{Tr}K_{\rm lo}^2
      \ge N/(4C').
\]
The rank is bounded above by the dimension of the actual neutral excited spectral space in that energy window. This proves (16).


**PROVED (distinct physical momenta).** In fact there are \(c',c_1,c_2,C>0\) such that at least \(c'd^{-3}\) *distinct* translation characters \(k\in(\mathbb Z/n)^3\), represented in the centered cube, satisfy
\[
 \frac{c_1}{d}\ \le\ \frac{2\pi}{L}\|k\|_\infty\ \le\ \frac{c_2}{d},
 \qquad \min\operatorname{spec}(H_{+,k})\le C/d,\quad
 H=-a^{-1}\log U.                                                        \tag{20}
\]
Replace each little tent in (17) by the spatial average from (14). The enlarged supports have radius at most \((1/4+\sqrt3/100)d\), hence are disjoint for centers \(h\) apart. Their positive sums still have slope at most one: along a segment joining different supports, each function vanishes at its first boundary, and their nonnegativity bounds the absolute difference by the larger value. They still fit inside the broad tents, and their diagonal \(G\) is comparable to the raw diagonal by (14). Thus (17)–(19) apply, with changed constants. The averaging multiplier and the earlier-time diagonal bound in (14)–(15) show that projecting simultaneously to \(E\le C/d\) and \((2\pi/L)\|k\|_\infty\le c_2/d\) retains at least \(G/2\) on the diagonal. The rank bound is again \(c d^{-3}\). This whole projection commutes with translations. In each character space all translates of the projected vector are scalar multiples of a single vector, including when that character has internal multiplicity. Consequently the rank counts at most one per character. Finally the lattice cube with \((2\pi/L)\|k\|_\infty<c_1/d\) contains at most \((1+Lc_1/(\pi d))^3\) characters. Choose \(c_1>0\) small compared with the fixed rank coefficient, then decrease \(d_*\). Subtraction proves (20).

## What the complex singularities can distinguish

**PROVED (a limitation of the converse to (5)).** Exact real positivity, a paired positive action, agreement of the first \(b^2-1\) moments, and even an area-order count of *distinct* uncanceled zeros and poles in every fixed tube are consistent with both possible real behaviors of an elementary twist. Fix \(x_*>0\), put \(A=b^2,\ K=e^{b x_*},\ p=(1+K)^{-1}\), and choose \(0<\lambda\le1\). Define
\[
 c(z)=1-p+p\cosh(bz),\qquad s(z)=\lambda p\sinh(bz),\qquad
 Z_\pm(z)=e^{-Abz}\bigl(c(z)^A\pm s(z)^A\bigr).                         \tag{21}
\]
These are Laplace transforms of probability laws on \([0,2Ab]\). Take uniform signs \(S_i\) conditioned on \(\prod S_i=\pm1\), independent Bernoulli variables \(H_i\) with mean \(p\), and independent signs \(D_i\) with mean \(\lambda\). The action is \(\sum_{i=1}^A b(1-S_iH_iD_i)\). In the product of single-site expectations the parity conditioning keeps the constant and the all-site sign monomials, giving (21). Flipping one \(S_i\) couples the actions within \(2b\). Their contact at zero is exactly order \(A\); on real \(B>0\) their ratio \(R=Z_-/Z_+\) lies strictly between zero and one.

**PROVED.** If \(\lambda=1\) and \(B>x_*\), then \(1-s(B)/c(B)=(K+e^{-bB})/(K+\cosh(bB))\asymp e^{-b(B-x_*)}\). Writing \(t=s/c\) gives \(1-t^A\asymp A(1-t)\) at fixed \(B\) and large \(b\). Thus \(-\log R(B)=(B-x_*)b-2\log b+O(1)\). If \(0<\lambda<1\), then \(0<t(B)<\lambda\), so \(0<1-R(B)\le2\lambda^A\) at *every* positive real \(B\). Nevertheless for this latter choice the tube of any fixed width about \([0,B]\), \(B>x_*\), contains at least \(2A\) distinct zeros or poles of \(R\) for large \(b\). For each of the \(2A\) roots \(\omega^{2A}=1\), solve \(s/c=\omega\) in \(y=e^{bz}\):
\[
       (\lambda-\omega)y^2-2\omega K y-(\lambda+\omega)=0 .
\]
For fixed \(0<\lambda<1\), the absolute value of the sum of the roots is comparable with \(K\), their product bounded uniformly, and one root has modulus comparable with \(K\), uniformly in \(\omega\). Its principal logarithm divided by \(b\) has real part \(x_*+O(1/b)\) and imaginary part at most \(\pi/b\) in modulus. The denominator \(c\) cannot vanish at that solution: a common zero would have \(y=\pm1\), where \(K+\cosh(bz)\ne0\). Distinct \(\omega\)'s give distinct points. At each point exactly one of \(c^A+s^A,\ c^A-s^A\) vanishes. This proves the count for the real behavior approaching one, as well as the contrasting real behavior for the other parameter. These examples test deductions from the specified action bounds, moment cancellations and zero counts. Their actions are explicit parity models. Wilson locality and the spatial dependence of its plaquettes remain possible sources of extra information.

## A direct physical-size criterion from the ordinary partition zeros

**PROVED (finite sum with an analytic error bound).** Return to two *ordinary periodic* Wilson integrals on \(n^3\), at time lengths \(T=n/2\) and \(2T\), with the same complex isotropic bare coupling. Denote them by \(Z_T,Z_{2T}\) and put \(J(B)=2\log Z_T(B)-\log Z_{2T}(B)\) for real \(B\ge0\). For \(B>0,\ r>2B\) whose circle misses the zeros, and \(1\le m\le4T-1\), define
\[
 \nu(\zeta)=2\,\mathrm{ord}_\zeta Z_T-\mathrm{ord}_\zeta Z_{2T},\qquad
 \Psi_{m,B}(\zeta)=\log|1-B/\zeta|+
                 \operatorname{Re}\sum_{k=1}^m\frac{(B/\zeta)^k}{k}.
\]
On every such torus with \(n\ge4\),
\[
 \left|J(B)-\sum_{|\zeta|<r}\nu(\zeta)\Psi_{m,B}(\zeta)\right|
       \le C n^4 B\,\frac{(2B/r)^m}{1-2B/r}.                             \tag{22}
\]
The sum is over distinct points with their signed multiplicities. It uses no transfer eigenvalue, restored-face interpolation, common zero-free neighborhood up to \(B\), or neutral-seed hypothesis. The earlier work establishes the thermal ratio, its contact at zero and obstructions to zero-free continuation. Equation (22) retains the contributions of the singularities, including their signs and positions. [Thermal interpolation](gap-solve2-astra62.md) · [Lemma ORD and its application](gap-unit-check-opus.md) · [Local logarithmic derivative estimate](gap-solve3-astra62.md)

**PROVED.** Write \(H=2Z_T'/Z_T-Z_{2T}'/Z_{2T}\) and \(G=H-\sum_{|\zeta|<r}\nu(\zeta)/(z-\zeta)\). Both Wilson integrals equal one at zero and are transforms of actions of absolute value at most \(12n^4\). The disk factorization used in (6), now centered at zero on radius \(r\), gives \(|G|\le Cn^4\) on \(|z|\le r/2\). Indeed Jensen on a larger circle between \(2r,3r\) counts at most \(Cn^4r\) zeros with multiplicity, and the reflected denominator in each Blaschke factor costs at most \(2/r\). The derivative of the residual zero-free logarithm is bounded by \(Cn^4\) there by the same Poisson kernel argument. The contact result for the periodic transfer gives \(H=O_n(z^{4T-1})\): the nonvacuum transfer starts at fourth order by Gauss's law and spatial girth, hence its \(T\)-th power starts at order \(4T\); the common Perron contribution cancels in \(J\). This is precisely the local statement of Lemma ORD. Thus the Taylor polynomial of \(G\) through degree \(m-1\) is the negative of that of the displayed pole sum. Cauchy's inequality bounds the Taylor remainder of \(G\) on \([0,B]\) by \(Cn^4(2B/r)^m/(1-2B/r)\). Integrate, using \(J(0)=0\). Each pole contributes the real part of its primitive with its first \(m\) Taylor terms removed, namely \(\Psi_{m,B}\). Real positivity ensures no zero on the integration path. This proves (22).

**PROVED (quantifiers on the assigned trajectory).** Let \(r_s=1/12800\), the common strong-coupling zero-free radius of the two ordinary boxes, from the checked rectangle port. Fix any \(p>0\), set \(Q=2+B/r_s\), take any \(r\) between \(4(1+B)Q\) and \(8(1+B)Q\) avoiding zeros, and set
\[
    m=\left\lceil\frac{\log(n^{4+p}(1+B))}{\log Q}\right\rceil.
\]
For \(B=\beta_j=O_L(\log n)\) on the assigned trajectory, this \(m\) is admissible for all sufficiently fine cutoffs. The error in (22) is \(O(n^{-p})\) and the disk contains at most \(C n^4(1+B)^2\) zeros with multiplicity, counting both integrals. All constants here may absorb \(r_s^{-1}\). Define \(\mathcal S_j(L)=\sum_{|\zeta|<r}\nu(\zeta)\Psi_{m,\beta_j}(\zeta)\) with these choices. Then (W), allowing its usual dyadic enlargement, is equivalent to
\[
 \text{for some fixed permitted }L,\qquad
       \limsup_j\mathcal S_j(L)<\log(1+1/1650).                           \tag{23}
\]
Indeed for \(X_t=\operatorname{Tr}U^t\) one has \(X_T\le e^{J}=X_T^2/X_{2T}\le X_T^2\), since \(1\le X_{2T}\le X_T\). Thus (23) implies the periodic seed directly. Conversely a physical periodic seed implies arbitrarily small \(X_T-1\) after fixed dyadic enlargements by the two-stage line of Theorem SH followed by Theorem S, as in row 720, giving (23). No large-volume limit at fixed \(B\) is interchanged with the physical cutoff limit. [Strong-coupling rectangle bound (P)](gap-seed-sc.md) · [Two-stage physical propagation](gap-phys-seed.md)

**PROVED (stability under matching nearby zeros).** There is also a test at fixed tolerance \(\epsilon>0\). Use the preceding \(Q,r\) and instead set \(m=\lceil\log(n^4(1+B)/\epsilon)/\log Q\rceil\), with \(0<\epsilon<1\). In the sum in (22), match any units of positive multiplicity with units of negative multiplicity, and put \(d_{\rm sum}=\sum_{\rm matched}|\zeta-\xi|\). The change in \(\mathcal S\) from dropping all matched pairs is at most
\[
              C\, n^4(1+B)^2\, d_{\rm sum}/\epsilon .                    \tag{24}
\]
The additional analytic error is at most \(C\epsilon\). To prove (24), every zero obeys \(|\zeta|\ge r_s\) by the strong-coupling bound. Also \(|\operatorname{Im}\zeta|\ge c n^{-4}\): under the real tilt at \(\operatorname{Re}\zeta\), all phases of the bounded action lie in an arc of width less than \(\pi/2\) when \(|\operatorname{Im}\zeta|<c n^{-4}\), so their mean is nonzero. The difference of two log-distance terms to either \(0\) or \(B\) is bounded by the separation divided by the smaller endpoint distance. The difference of their \(k\)-th reciprocal powers is at most \(k r_s^{-k-1}|\zeta-\xi|\), by factoring the power difference. Hence the Lipschitz bound for the whole weight is \(C n^4+r_s^{-1}\sum_{k=1}^m(B/r_s)^k\le C n^4+C Q^m\). For the last inequality sum the geometric bound using \(Q\ge2\). The ceiling gives \(Q^m\le Q n^4(1+B)/\epsilon\), which proves (24). In particular it suffices to bound the signed *residual* sum plus (24) plus \(C\epsilon\) strictly below the threshold at one physical size. This permits genuinely distinct nearby zeros; exact shared zeros are unnecessary. Neither Jensen's separate counts nor the higher-order contact bounds this signed residual at \(B=\beta_j\).

## Where the cylinder witness puts its spectral weight

**PROVED, conditional on (SD-cyl-CA).** Let \(\mu_d\) be the joint positive energy and spatial momentum measure of \(U^{u_2/2}Hv\) in (14), so \(\mu_d(\mathrm{all})=G\asymp d^2/l(d)^2\). Use \(p=2\pi k/L\) for physical momentum, with distances periodic in the Fourier lattice if necessary. For \(A_0d\le x\le D_{\max}\), \(A_0\) a fixed sufficiently large number, the following two upper bounds hold at sufficiently fine cutoffs:
\[
 \begin{split}
  \mu_d(E\le 1/x)/G
       &\le C(d/x)^3\,l(d)^2/l(x)^2,\\
  \sup_{p_0}\mu_d(E\le 1/x,\ \|p-p_0\|_\infty\le1/x)/G
       &\le C(d/x)^6\,l(d)^2/l(x)^2.                                   \tag{25}
 \end{split}
\]
These bounds concern the specified source in the actual Wilson transfer. The supremum includes momentum bins far from zero.

**PROVED (reflection of an array of sources).** In a four-dimensional cube of side \(x/50\) about a lattice time \(-x+O(a)\), place coordinate grids of small averaged tents at spacing \(h=a\lceil d/a\rceil\) in space and time. There are \(M_s\ge c(x/d)^3\) spatial positions \(y_i\) and \(M_t\ge c x/d\) time positions. Reflect the array in time zero. For any complex coefficients \(|c_{ir}|\le1\), the reflected connected covariance of the linear combination and its conjugate is at most \(C x^2/l(x)^2\). Indeed split into positive and negative real and imaginary coefficients and pad by the two broad tents of radius \(x/4\), exactly as in (17). Distinct small supports are disjoint even after the spatial averaging. They fit inside the respective broad tent supports. The broad centers are \(2x+O(a)\) apart in time, the separation margins are strict, and their mass condition persists for \(d/x\) sufficiently small. The two-root cylinder covariance is bilinear in the original bare sources at this common cutoff; the coefficient in the witness comparison is taken at \(x\) for the padded pairs.

**PROVED.** Write the positive time distances of the early centers from the reflection plane as \(b_r a=x+O(x/50+a)\), independent of \(i\). The entry pairing \((i,r)\) with the reflection of \((j,s)\) is the integral against \(\mu_d\) of
\(\exp[-E a(b_r+b_s-t_2)]\exp[ip\cdot(y_j-y_i)]\). This follows by the slab formula, since the vacuum centering and the slab width \(w\) are common to every translate and \(u_2=t_2-w\). The whole quadratic form is the integral of
\[
  \left|\sum_{i,r}c_{ir}
              e^{-Ea(b_r-t_2/2)} e^{ip\cdot y_i}\right|^2 .
\]
For \(E\le1/x\), the time factors are between a fixed positive constant and one. Set \(c_{ir}=\epsilon_i\) independent fair signs on the spatial sites, the *same sign at every time on each site*. Averaging removes the cross terms in space and keeps all \(M_t^2\) time terms, giving at least \(cM_s M_t^2\,\mu_d(E\le1/x)\). For the second bound instead take \(c_{ir}=e^{-ip_0\cdot y_i}\). On the stated momentum bin, after one common phase rotation the real parts of all spatial factors are bounded below by a positive constant, since the spatial array has side \(x/50\). The contribution is at least \(cM_s^2 M_t^2\) times the mass in this bin. Divide the common upper bound by these two quantities and by \(G\). This proves the powers three and six in (25).

**PROVED (many states in both energy and momentum bands).** There are fixed positive constants such that for each small fixed \(d\), at least \(c_N d^{-3}\) distinct \(k\)'s in \(c_p/d\le\|2\pi k/L\|_\infty\le C_p/d\) have
\[
 c_w\,d^3 G\ \le\
 \mu_d\bigl(c_E/d\le E\le C_E/d,\,p=2\pi k/L\bigr)
 \ \le\ C_w\,d^3G .                                                         \tag{26}
\]
In particular *each* of these sectors contains an actual neutral excited transfer level in the displayed energy band. To see this, first fix \(K\ge A_0\) large, and take \(x=Kd\). For all sufficiently small \(d\), \(l(d)/l(Kd)\le2\), so (25) puts at most \(G/16\) at \(E\le1/(Kd)\) by increasing \(K\). The early-time energy and spatial smoothing bounds following (14) discard at most \(G/16\) each at the high ends. Set \(w_k\) to be the remaining mass in sector \(k\), divided by \(G\). On the same \(N\) grid centers as in (19), the Gram matrix of these projections divided by \(G\) is \(\sum_k w_k e_k e_k^*\), with \((e_k)_i=e^{2\pi i k\cdot y_i/L}\). Its squared Hilbert–Schmidt norm is at least \(N^2\sum_k w_k^2\), since the cross terms are \(w_kw_{k'}|\langle e_k,e_{k'}\rangle|^2\). It is at most \(C N\) by (19) and positive Gram domination. Thus \(\sum w_k^2\le C/N\). By Cauchy–Schwarz, the very small momentum cube \(\|p\|_\infty<c_1/d\) has total weight at most \(1/8\) if \(c_1\) is small enough. There are at most \(C_L N\) remaining momentum labels. Those of weight below \(\eta/N\) have total at most \(C_L\eta\); those above \(A/N\) have total at most \(C/A\). Choose \(\eta\) small and \(A\) large. A fixed positive mass remains on weights between these two cutoffs, so at least \(cN\) labels qualify. Here \(N\asymp d^{-3}\). This proves (26) with the energy and momentum intervals just chosen.

**PROVED (survival in subsequential two-point limits).** For each fixed \(d\) the damped measures just used have uniformly bounded mass and an exponential large-energy tail \(C G e^{-c d E}\) by (14). Spatial averaging gives a tail \(C G (L/(d M))^2\) for integer momentum indices of norm larger than \(M\), from the same Dirichlet kernel bound and the raw diagonal in (14). Consequently, along a common subsequence for any countable sequence \(d\downarrow0\), they have finite positive weak limits on \([0,\infty)\times\mathbb Z^3\). For example extract convergence of the distribution functions on rational energy thresholds for each fixed momentum and then use the two tail bounds. For each \(d\) there are finitely many eligible momentum lists. Extract again so a list of at least \(c d^{-3}\) qualifying labels is fixed. Each corresponding closed energy interval retains at least \(c d^5/l(d)^2\) of measure by (26) and the closed-set inequality for weak convergence. For fixed additional physical time and spatial translation, the Laplace–Fourier transforms converge along this subsequence, by the two tail bounds and rounding translations to the lattice. This is a conclusion about limits of these particular cylinder correlations. It supplies neither a continuum Hilbert space for all fields nor an upper bound on its full thermal trace.

## Testing an upper bound from source moments

**PROVED (an obstruction on the same \(SU(2)\) slice).** Even the complete set of *normalized multitime* correlations of per-link polynomials of any prescribed degree \(d_0<\infty\) can agree exactly for two positive local-in-time gauge transfers on the same \(SU(2)\) links while their periodic neutral heat traces differ by an arbitrarily large factor. Here the discarded property is the particular Wilson one-link time kernel used in (11). This refines, for these probes, the council's earlier spectator-factor test. [Council comparison models](gap-council-brief.md) · [Earlier tensor obstruction](gap-solve4-astra62.md)

**PROVED.** Work with independent Haar links on one slice and choose \(M\ge c n^3\) elementary spatial plaquettes on disjoint links, for instance on a stride-four grid. For each chosen plaquette set
\[
 h_p(X)=\operatorname{sign}\cos(K\theta(U_p)),\qquad
 \tfrac12\operatorname{tr}g=\cos\theta(g),\quad 0\le\theta\le\pi ,
\]
with integer \(K>d_0+2\). The convention at the isolated zeros is immaterial. For a polynomial \(P(X)\) of degree at most \(d_0\) on each link and every nonempty subset \(A\) of selected plaquettes, \(\int P\prod_{p\in A} h_p=0\). Condition on all links except one of a chosen \(p\in A\), and change that link to its plaquette holonomy. This is a Haar-preserving affine orthogonal substitution on the real quaternion coordinates, including possible inversion. Its residual polynomial has degree at most \(d_0\). Central averaging produces a polynomial of degree at most \(d_0\) in \(\cos\theta\): odd spatial-coordinate moments vanish, and at even degree the spherical average gives powers of \(1-\cos^2\theta\). The Haar factor \(\sin^2\theta\) increases the cosine degree by at most two. The even \(2\pi\)-periodic function \(\operatorname{sign}\cos(K\theta)\) has no Fourier modes of absolute frequency below \(K\), including the zero mode, by its period and its sign change on shifting by \(\pi/K\). This proves the claimed orthogonality by integrating over \([0,\pi]\).

**PROVED.** For \(0<\rho<1\) take the transfer kernel
\[
        P_\rho(X,Y)=\prod_{p}(1+\rho h_p(X)h_p(Y)).
\]
It is strictly positive, real, symmetric, Markov and gauge invariant at each end. All its factors involve a single spatial plaquette on each of two consecutive slices. Its nonzero eigenvalues are \(\rho^{|A|}\) on the orthonormal products \(h_A=\prod_{p\in A}h_p\), including the constant at \(A=\varnothing\). Every state here is center-neutral, since all plaquettes are contractible. Multiplication by any allowed slice polynomial, compressed to these products, is the scalar \(\int P\) times the identity: use \(h_A h_B=h_{A\triangle B}\) and the preceding orthogonality. Consequently every normalized periodic correlation with one allowed polynomial at each of arbitrarily many distinct times is exactly the product of the one-slice Haar averages, for every positive integer separation. This is also its value for the rank-one Haar transfer \(P_0\). The cylinder vacuum correlations agree as well. In contrast their normalized neutral heat traces at time \(u\) are \((1+\rho^u)^M\) and one. Taking \(\rho=e^{-a^2}\) makes the trace grow exponentially in \(M\) at fixed physical time as \(a\to0\). The construction allows \(d_0\) to grow with the cutoff by increasing \(K\). It uses a selected spatial grid and a different temporal action; it is a counterexample to recovering the trace from those observations and the listed positivity and locality properties alone. Equation (12) escapes it through relative approximation of the actual Wilson kernel. That estimate still requires control of the spectrum of the retained moment matrix.

## The shortest cylinder times covered by the count

**PROVED, with the explicit cutoff admission of (SD-cyl-CA).** Write \(a=L_{\rm block}^{-K}\) and retain its fixed coupling and geometry. For a sufficiently large fixed \(C_{\rm mesh}\) put
\[
  q_K=\max\{C_{\rm mesh},\, L_{\rm block}^{\,k_W} C_W(K-k_W)\}.
\]
For all large \(K\) and every integer \(u\ge1\) such that \(d=\max(au,aq_K)\le d_*\), the actual periodic neutral trace satisfies
\[
     \operatorname{Tr}U_+^u-1
                  \ \ge\ c\,\big[a\max(u,q_K)\big]^{-3}.                 \tag{27}
\]
Here \(d_*>0\) is decreased if necessary. Indeed \(C_W(K-k_W)L_{\rm block}^{-(K-k_W)}\le d\), so the definition of the first admissible witness depth gives \(s(x)\le K-k_W\) at every \(d\le x\le D_{\max}\). Choose \(D_{\max}\) in the tail satisfying all three depth inequalities of row 865. The mesh constant pays \(32/\vartheta^2\) and all fixed rounding and Fourier-grid margins used for (16); the source comparison constants are uniform. This makes precisely the family of larger-scale tests in that proof admissible at this cutoff. Use its \(c d^{-3}\) excited energies \(\le C/d\), each contributing at least \(e^{-C}\) at time \(u\). The polylogarithmic growth of \(C_W(K-k_W)\) in \(g^{-2}+B^\sharp(K+1)\) implies \(a q_K\to0\). Thus the divergence at every subphysical time in (15) has the three-dimensional lower power once \(u\ge q_K\), and (27) also supplies a quantitative floor when \(u<q_K\). This concerns small physical times. The physical seed time of row 1161 need not be in that range.

## Testing cancellation at the physical cutoff

**PROVED, conditional on the cylinder witness where stated.** Fix a compatible \(L\) and any one admitted small \(d\). By (16) and \(J(\beta_j)\ge\log X_T\), one has, on every sufficiently fine cutoff,
\[
 J(\beta_j)\ \ge\ \delta_L,\qquad
 \delta_L=\min\!\left\{1,\log\!\left(1+c d^{-3}e^{-CL/(2d)}\right)\right\}>0 .
\]
Thus (23) has a strictly positive signed sum in lower limit on this cube. It need only become small on sufficiently large *physical* cubes. More quantitatively, for any complete pairing of the positive and negative multiplicities in the disk of (24),
\[
     \liminf_j n^4(1+\beta_j)^2 d_{\rm sum}\ \ge\ c'\delta_L^2 .          \tag{28}
\]
Use the fixed tolerance \(\epsilon=\delta_L/(4\max\{C,1\})\), where \(C\) bounds the analytic error divided by \(\epsilon\). With no residual points, (22)–(24) must supply at least \(3\delta_L/4\) through the matching cost. The same proof applies to pairings on any subsequence admitting them. If multiplicity counts differ, one must keep residual points or match across a different circle. This obstruction is to a bound with vanishing total error at fixed \(L\); (28) leaves the strict physical inequality in (23) undecided.

**PROVED (the scalar data allow a nonzero periodic contribution).** There is also a local, isotropic positive comparison for (22)–(24). The finite-group factor is the council's existing frozen \(\mathbb Z_2\) comparison. Its contribution to this particular signed sum at the physical bare couplings can be seen without a phase assumption. On the same four-torus put independent uniform signs on links and assign action \(J_0\) to each negative plaquette, zero to a positive one. Call its normalized partition function \(Y_t(z)\) on \(n^3\times t\). With \(V=n^3 t\),
\[
       1\le \frac{Y_t(B)}{2^{3-3V}}
             \le (1+e^{-J_0 B})^{6V},\qquad B\ge0.                        \tag{29}
\]
Every admissible plaquette pattern has the same number of link preimages, as it is a fiber of the mod-two coboundary. In the flat fiber one freely chooses the \(V-1\) vertex gauge signs relative to one vertex and four commuting winding signs. Tree transport with four periods recovers all flat connections from these data. Dividing its \(2^{V+3}\) configurations by \(2^{4V}\) gives (29) upon summing all subsets for the upper bound. On the first-passage trajectory at fixed reference coupling, the two drift bounds (RF25) give \(\beta_j\asymp\log n\). Choose a fixed \(J_0\) with \(J_0\beta_j\ge5\log n\) eventually. For \(t=T,2T\), (29) yields
\[
           2\log Y_T(\beta_j)-\log Y_{2T}(\beta_j)
                         =\log 8+O(n^{-1}).                               \tag{30}
\]
Taking the product with Wilson leaves every normalized correlation of its original fields exactly unchanged and adds (30) to \(J\). The action remains local and reflection positive in all frames; the extra degrees of freedom are a finite gauge group. [Council test and finite-coupling Peierls comparison](gap-council-brief.md) · [Flat-sector count](gap-uv-rigidity-max.md) · [Use of both first-passage drift bounds](gap-solve3-astra62.md)

**PROVED.** This example also has the precise analytic inputs of (22) and (24), with its own fixed strong-coupling radius. In the one-frame transfer the nontrivial \(\mathbb Z_2\) character on an electric link has ratio \(\tanh(J_0 z/2)\) to the trivial character. The gauge projection permits nonempty link sets only when every vertex has even degree, so on a spatial torus of side \(n\ge4\) they start at degree four. The same finite-dimensional rank-one perturbation argument as in Lemma ORD gives contact \(4T\) for the thermal log ratio. For a uniform zero-free disk, factor out the nonvanishing one-plaquette constant near zero. Expanding the product of \(1+v U_p\), \(v=\tanh(J_0z/2)\), leaves just edge-closed plaquette subsets, with weight \(v^{|S|}\). Their components for adjacency by a common link are individually closed. On any permitted plaquette set \(\Lambda\), remove a plaquette \(p\). The resulting sum changes by the sum over closed connected \(C\ni p\) of \(v^{|C|}\) times the partition sum on \(\Lambda\) minus \(C\) and its neighbors. With maximum adjacency degree \(\Delta\), at most \(\max(2,\Delta)^{2m}\) connected sets of size \(m\) contain \(p\), by traversing a spanning tree. Induct on \(|\Lambda|\) that every ratio upon adding one plaquette lies within \(1/2\) of one. Each smaller partition sum in the change divided by the sum on \(\Lambda\setminus\{p\}\) costs at most \(2^{(\Delta+1)m}\) by the induction hypothesis. The resulting geometric series is less than \(1/2\) for a fixed sufficiently small \(|v|\). The empty set initializes the induction. Thus the disk radius is independent of \(n,t\), and the action obeys the same volume-order exponential-type bound. Applying (22) to \(Y\) gives a signed sum tending to \(\log 8\); additivity gives the stated obstruction for a product. For the actual pure \(SU(2)\) integrals the sign and size of the residual sum are a separate question.

## Unconditional Fisher zeros from the first winding coefficient

**PROVED (an obstruction in the actual pure Wilson integrals).** Let \(N_{\rm v}(b,R)\) count the distinct zeros and poles of the elementary vortex ratio (4) in the disk \(|z|\le R\), after cancellation. Let \(N_{\rm t}(n,R)\) count them for the ordinary thermal ratio in (22). There is an absolute \(r_*>0\) independent of the boxes such that, for every fixed \(R>4\),
\[
 \liminf_{4\mid b\to\infty}\frac{N_{\rm v}(b,R)}{b^2}
 \ \ge\ \frac{\log(R/4)}{\log(2R/r_*)},\qquad
 \liminf_{2\mid n\to\infty}\frac{N_{\rm t}(n,R)}{4T}
 \ \ge\ \frac{\log(R/4)}{\log(2R/r_*)},\quad T=n/2.                     \tag{31}
\]
These lower counts require neither a magnetic seed nor a cylinder witness. Thus even on the strongly coupled periodic side there are area-order vortex singularities in a sufficiently wide disk. The location near a *real segment* in (5), or signed data such as (22), matters. A zero-free continuation on such a disk is unconditionally impossible for the thermal ratio itself.

**PROVED (the vortex coefficient).** At the minimum degree \(A=b^2\) in (4), a contributing monomial must contain exactly one positively oriented \(12\)-face over each \((x_1,x_2)\), with no other plaquette and no repetition. Closure at the edges forces the transverse coordinates of neighboring chosen faces to agree. Hence the support is one flat \(12\)-torus, and there are \(b^2\) choices. On each torus the Haar integral of the product of the normalized traces is \(4^{-A}\). Orient all faces coherently: each shared link occurs once in the fundamental representation and once in its conjugate. Integration identifies the two endpoint color indices with factor \(1/2\) per edge by the fundamental Haar orthogonality identity. There are \(2A\) edges, one free index per vertex with \(A\) vertices, and a normalization \(1/2\) per face. Their product is \(2^{-2A}2^A2^{-A}\). The twist changes the sign once. Dividing by the untwisted integral, whose constant term is one, gives
\[
       \log R_b(z)=-2b^2 (z/4)^{b^2}+O_b(z^{b^2+1}).                    \tag{32}
\]
Here the diagrams contributing to this coefficient have been integrated explicitly; no conjectural sign of a general surface weight is used.

**PROVED (a thermal coefficient).** On the spatial \(n^3\) torus use the \(3n^3\) elementary fundamental plaquette traces, orthogonal in Haar measure together with the constant at \(n\ge 6\). Each is an eigenvector of the electric convolution normalized to preserve the constant, with eigenvalue \(\rho_{1/2}(z)^4\), where \(\rho_{1/2}(z)=I_2(z)/I_1(z)=z/4+O(z^3)\). They are gauge invariant. At real \(z>0\), test the true transfer on \(D^{-1}\) times this span including the vacuum constant of the *electric* transfer. The minimum Rayleigh quotient is at least \(\|D^{-1}\|^{-2}\rho_{1/2}^4\), and the true top eigenvalue in this normalization is at most one. At fixed \(n\), \(\|D^{-1}\|\to1\) as \(z\downarrow0\) for the action \(1-w\). The min–max principle thus gives \(3n^3\) *excited* normalized eigenvalues at least \((1+o_n(1))(z/4)^4\). Using \(J\ge\log X_T\) and its analytic contact \(4T\) proves
\[
                [z^{4T}]\,J(z)\ \ge\ 3n^3\,4^{-4T}.                     \tag{33}
\]
The coefficient concerns fixed \(n\) first. The resulting lower bound is explicit in \(n\). The tube graphs and sharp leading coefficient for the related cube-doubling defect are prior results. [Strong-coupling winding expansion](gap-seed-sc.md) · [Electric character and contact](gap-unit-check-opus.md)

**PROVED (counting distinct places).** Both twisted and untwisted integrals have a common fixed zero-free disk at zero. One direct proof uses \(e^{z\sigma_p w_p}=1+g_p\), with \(\sigma_p=\pm1\) and \(|g_p|\le e^{|z|}-1\). Distinct connected components of any selected plaquette set, under shared-link adjacency, integrate independently under Haar. The induction after (30) applies verbatim with connected-component activity \(\mathbb E\prod_{p\in C}g_p\) of modulus at most \((e^{|z|}-1)^{|C|}\); allow every connected set instead of just closed ones. This gives the claimed \(r_*>0\), decreased below one. The common action constant is entire and nonvanishing. This is the usual strong-coupling argument with a uniform bound for the two signs.

**PROVED.** Write \(H\) for the log derivative of either ratio and \(D_0\) for its contact order, \(b^2\) or \(4T\). With \(V_0=b^4\) or \(n^4\), (32) or (33) gives \(|[z^{D_0-1}]H|\ge c V_0 4^{-D_0}\), with all lower coefficients zero. Form \(P=\prod_{|\zeta|\le R}((z-\zeta)/(2R))\), one factor per distinct uncanceled point. Then \(|P|\le1\) on the disk and \(|P(0)|\ge(r_* /(2R))^{N}\). For any fixed \(0<\alpha<1\), \(|PH|\le C_{\alpha,R} V_0\) on \(|z|\le\alpha R\): use the disk argument of (6) on a boundary radius between \((1+\alpha)R/2\) and \(R\), with no zero on the boundary. All pole denominators inside are removed by one factor of \(P\) each. The analytic part is bounded by the volume from the Poisson kernel, and Jensen bounds the sum of absolute multiplicities by \(C_R V_0\). Cauchy's inequality for the coefficient of \(z^{D_0-1}\) now gives
\[
       N\log(2R/r_*)\ \ge\ D_0\log(\alpha R/4)-O_{\alpha,R}(1).
\]
Take the size lower limit first and then \(\alpha\uparrow1\). This proves (31). In particular the degree of contact and the separate volume-order growth estimates alone cannot turn these disks into a subarea-count criterion for selecting the physical branch.

## What the spectral counts decide about (W)

**PROVED (both possible infrared behaviors fit the band count).** Consider the continuous spatial three-torus of side \(L\) with uniform measure. Let \(Q_t\) be the convolution with eigenvalues \(e^{-2\pi t\|k\|_1/L}\) on its Fourier characters. This is a positive Markov kernel: the one-dimensional Fourier series with coefficients \(r^{|k|}\), \(r=e^{-2\pi t/L}\), sums to \((1-r^2)/(1-2r\cos\theta+r^2)\), and the three factors multiply. With \(\Pi\) projection on constants, \(P_t=e^{-m t}Q_t+(1-e^{-m t})\Pi\) is a positive self-adjoint Markov semigroup for every \(m\ge0\). The nonzero momenta have energies \(m+2\pi\|k\|_1/L\). Both \(m=0\) and fixed \(m>0\) give \(c_L d^{-3}\) distinct momentum and energy labels in annuli of order \(1/d\). One can put total squared norm \(d^2/l(d)^2\) equally on a fixed inner subannulus, giving the weights of (26) and zero mass below \(1/x\) for \(x\ge A_0d\). At time \(L/2\) the excited trace is exactly
\[
       e^{-mL/2}\left[\left(\frac{1+e^{-\pi}}{1-e^{-\pi}}\right)^3-1\right].
\]
For \(m>0\) it eventually meets the periodic seed. For \(m=0\) it exceeds \(6e^{-\pi}>1/1650\) on every box. This compares the information in the spectral bands themselves, without an additional invisible factor. The semigroups are not claimed to arise from the Wilson action.

**OPEN (remaining Wilson estimates).** On the neutral-trace route the missing positive estimate is an upper bound on the squared eigenvalue sum in (12) at one fixed physical size. Its degree and rank obstructions and the exact moment comparison above explain why local cylinder control, even with the weight distribution in (25)–(27), does not yield that sum. After a neutral seed, the alternative (2) needs exclusion of the \(\log8\) value: (9)–(10) bound particular charged readings but their uniform full-cube estimate tends to one. On the complex route (5) requires zeros near a real interval, whereas (21), (31)–(33) show exactly what a wide-disk count or moment contact misses. The direct alternative (23) bypasses both the neutral input and branch selection; its unresolved quantity is the signed Wilson sum at one physical endpoint. Equations (28)–(30) identify a fixed-size obstruction to complete matching and a local comparison which contributes \(\log8\) to that sum. I have no estimate on the pure Wilson divisor or the full retained spectrum that supplies the strict inequality. These arguments leave (W) and the Jaffe–Witten mass gap open.


RESULT — Row 1163. PROVED by hand, unchecked: (W) is equivalent after allowed enlargement to the signed ordinary Wilson partition-zero test (23), with the finite error bound (22) and matching estimate (24). The first winding coefficients force area-order vortex and linear-order thermal singularities in every fixed disk of radius greater than four. Given the open cylinder suppliers, at least \(c d^{-3}\) distinct neutral momenta carry positive weight in energy and momentum bands of order \(1/d\), with the short-time floor (27). Given the preceding neutral seed, the ordinary excess selects between \(0\) and \(\log8\). OPEN: the strict physical upper bound in (23), hence (W) and the Jaffe–Witten mass gap.
