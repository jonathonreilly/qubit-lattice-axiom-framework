# Repo search

**GUIDE.** FINISH row 1262, checkout `ad8d21df2`. The November 8 search singled out the one-step plaquette witness. I checked its argument on PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14 and 106–149. It supplies a positive correlation at one lattice step. Its uniform contraction uses bare parameter at most $1/32$. Grok's PR 10133, `MASS_GAP_CROSSOVER_REDUCTION.md`, lines 77–86, leaves source transport and crossover clustering open. PR 10134's `mass-gap-interface.md`, I1–I5, requires a common continuum observable space. The single-scale minimizer on PR 10141, `research/ym4d/library/fp1.md`, lines 299–315, concerns the classical constrained form. On main `8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md`, lines 305–329, gives a conditional criterion involving the cube spectrum and a thermal state count. None of these passages supplies a physical weak-coupling gap. The row-specific prior file is absent at the pin.

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, explain the observable sector and the exclusion of low spectral support in outline lines 581–599 and 31860–31882. Their scalar block estimate is at lines 773–780. I followed index chunks 01 and 29 and the corresponding obligations to those passages. CA-I lines 2704–2712 and 3213–3222 delimit their reconstruction. Both texts are at `31a47c543775`.

**GUIDE.** The question I pursue is whether relaxation of the actual Wilson law *inside one finite box* gives a lower bound at the scale required by the previous run, and whether that finite-box input can be established for Wilson fields. Row 1254, equations (20), (33), (37) and (39), concerns global or source-specific relaxation on an entire fine torus. Its comparison between update sizes assumes an input on that torus. Row 1218 compares the thermal estimate of Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy with the cube dynamics of the first four authors and the criteria of Zeng Chunping. Row 1224 (`gap-mini-solve-q-fable.md`, Appendix G reading) records a local-to-global criterion of the six authors with an error of order the inverse patch side. I will look for a bound with error of order the *inverse square* of the side, then test the needed local variance directly. The registry's B99-U concerns a constrained classical form. I found no row owning this finite-box Wilson relaxation estimate. All proof labels below describe hand arguments in this research note and confer no status.

## A patch of the fine Wilson dynamics

**GUIDE.** Knabe's method compares the square of a sum of local projections with squares on finite patches. The inverse-square threshold for a Wilson heat bath was proposed in \(\S\)B7 of [the earlier skeleton](gap-skeleton-max.md). Gosset and Mozgunov's spin-chain result is discussed on main in \(\S\)2 of \(\texttt{gap-form-exercise.md}\). I use the estimate for overlapping Wilson updates from [row 1254](gap-solve29-astra62.md), (18)–(19). The extra input below is a variance inequality inside a patch. This gives an explicit inverse-square threshold for the four-dimensional patches, with ordinary unweighted update rates inside them.

**GUIDE.** Let \(\mu\) be the Wilson law with density proportional to \(\exp(\beta\sum_p \frac12\operatorname{tr}U_p)\) relative to product probability Haar, at finite \(\beta\ge0\), on an even \(N^4\) torus. One positive link per site per direction is stored. Let \(V_s(x)\) contain the links based in \(x+\{0,\ldots,s-1\}^4\), \(P_x\) be conditional expectation given its exterior, \(D_x=1-P_x\), and \(H_s=s^{-4}\sum_xD_x\). Choose \(s\ge2,\ R\ge1,\ t=R+s-1,\ 2t+4\le N\). The patch with origin \(z\) uses the small-cube origins \(I_z=z+\{0,\ldots,R-1\}^4\). Their union of updated links is \(V_t(z)\). Write \(Q_z=1-\mathbb E_\mu[\,\cdot\mid V_t(z)^c]\), and \(L_z=s^{-4}\sum_{x\in I_z}D_x\). All forms use \(L^2(\mu)\). In particular \(L_z\) only resamples the small cubes wholly inside the patch.

**PROVED.** Suppose that for every gauge-invariant \(f\) and every \(z\)
\[
          \gamma\|Q_z f\|_2^2\ \le\ \langle f,L_z f\rangle .             \tag{1}
\]
It suffices to have this inequality on almost every conditional Wilson box with its given exterior, on restrictions of invariant tests. Set \(\vartheta=\pi/(R+1)\),
\[
 b_R=\left(\frac{(\sum_{i=1}^{R}\sin i\vartheta)^2}
                  {R\sum_{i=1}^{R}\sin^2 i\vartheta}\right)^4,\qquad
 e_{s,R}=\tfrac43(2+1/s)^4s(s+1)(1-\cos\vartheta).
\]
On the gauge-invariant centered functions the global gap of \(H_s\) is at least
\[
                        b_R\gamma-e_{s,R}.                              \tag{2}
\]
In fact only the **sum** of (1) over the patch positions is needed. Neither a thermodynamic limit nor a comparison with a coarse action enters (2).

**PROVED.** Give the origins of one patch weights \(p(i)=\prod_{\nu=1}^4\sin((i_\nu+1)\vartheta)\) for \(0\le i_\nu<R\), zero elsewhere. Write \(A=\sum p,\ B=\sum p^2,\ W_z=s^{-4}\sum_x p(x-z)D_x\), and \(E=\langle f,H_s f\rangle\). By nested conditioning \(Q_zW_z=W_z\). By counting translations \(\sum_zW_z=AH_s\) and \(\sum_zL_z=R^4H_s\). Thus
\[
 A^2 E^2\le \left(\sum_z\|Q_zf\|^2\right)\sum_z\|W_zf\|^2
            \le {R^4 E\over\gamma}\sum_z\|W_zf\|^2                     \tag{3}
\]
when \(\gamma>0\).

**PROVED.** The weighted upper comparison in row 1254 admits the following constant. Put \(B_v=\sum_i p(i)p(i+v)\). For the zero-extended one-dimensional sine \(u\), summation by parts and \(u_{i-1}+u_{i+1}=2\cos\vartheta\,u_i\) at its interior sites give \(\|\tau_1u-u\|^2=2(1-\cos\vartheta)\|u\|^2\). By telescoping \(k\) translates the square at shift \(k\) is at most \(k^2\) times the square at shift one. The one-dimensional overlaps lie in \([0,\|u\|^2]\). Multiplying the four normalized overlaps and using \(1-\prod_i c_i\le\sum_i(1-c_i)\) yields
\[
  0\le1-B_v/B\le(1-\cos\vartheta)\sum_\nu v_\nu^2 .
\]
For \(\|v\|_\infty>s\) (periodic distance), the two cubes share no plaquette. Conditional on their joint exterior their two fillings are independent. Their projections commute, so \(\operatorname{Re}\langle D_x f,D_{x+v}f\rangle=\|D_xD_{x+v}f\|^2\ge0\). In comparing \(\sum_z\|W_zf\|^2\) with \(B\|H_sf\|^2\), only closer pairs can increase the former. For each such pair bound the absolute cross term by half the sum of the two squared norms. Summing \(\sum_{\|v\|_\infty\le s}\sum_\nu v_\nu^2=4(2s+1)^4s(s+1)/3\) gives
\[
             \sum_z\|W_z f\|^2
              \le B\bigl(\|H_s f\|^2+e_{s,R} E\bigr).                  \tag{4}
\]
The periodic size restriction puts every listed displacement in a single copy of \([-s,s]^4\).

**PROVED.** Equations (3)–(4) give \(H_s^2\ge(b_R\gamma-e_{s,R})H_s\) as forms on invariant functions. The projections preserve this space by gauge covariance of the conditional laws. If \(H_sf=0\), then \(f\) is measurable off every small cube. At this finite cutoff the Wilson and product Haar laws have bounded density ratios in both directions. In product Haar space the commuting integrations over the small cubes have product equal to integration over all links. Hence \(f\) is constant. The spectral theorem now gives (2). If its right side is nonpositive, positivity gives the claim directly.

**PROVED.** Uniformly in \(R\), \(b_R\ge1/16\). Indeed \(\sin(\pi x)\ge2\min(x,1-x)\) on the unit interval, so the mean of \(u\) is at least \(1/2\) by summing the two arithmetic progressions. Since \(u^2\le u\), the ratio inside \(b_R\) is at least that mean. For \(s\ge2\), \(e_{s,R}\le 40\pi^2(s/(R+1))^2\), using \(1-\cos v\le v^2/2\), \(2+1/s\le5/2\), and \(1+1/s\le3/2\). Thus it suffices, for instance, that \(\gamma\ge 1280\pi^2(s/(R+1))^2\) to retain at least \(\gamma/32\) globally. The explicit expression (2) often gives a smaller threshold. This is a sufficient inequality with room for a positive margin. The optimal coefficient is open.

## How much weight can a rough exterior carry?

**GUIDE.** A worst-exterior version of (1) asks for a variance bound even when a whole boundary face carries center flux at every plaquette. Section 7.6 of [row 1224](gap-mini-solve-q-fable.md) constructs such a boundary and proves that every classical minimizer in its specified rectangle breaks the residual global conjugation symmetry. Its finite-coupling conclusions about slow face rotation are heuristic. I retain its example and examine whether (2) can dispense with this class of boundary conditions. Small ordinary probability by itself would give no bound on an arbitrary normalized test concentrated on a rare event.

**PROVED.** Put \(q_p=(1-\tfrac12\operatorname{tr}U_p)/2\in[0,1]\). For a plaquette orientation \(\nu\) (an unordered pair of coordinate directions) and \(J=\{0,\ldots,s-2\}^4\), let
\[
                Y_y^\nu=|J|^{-1}\sum_{j\in J}q_{y+j,\nu}.
\]
There is an absolute \(C\) such that, for \(\beta\ge1\), **every** exterior to the side-\(s\) update satisfies
\[
      P_y Y_y^\nu\ \le\ m_s,\qquad
      m_s=\min\{1,C[s^{-1}+(1+\log\beta)/\beta]\}.                     \tag{5}
\]
This concerns four-dimensional box averages, with a single fixed orientation.

**PROVED.** Let \(S_y\) be the sum of \(2q_p\) over all plaquettes meeting the updated links. There are at most \(24s^4\) of them. Any with both updated and exterior links has an updated base point in the inner boundary layer of at most \(8s^3\) sites, so there are at most \(192s^3\) such plaquettes. This uses the fact that the base points of links in a plaquette have pairwise maximum distance at most one. Restrict every updated link to round distance \(\delta=\beta^{-1/2}\le1\) of the identity. For a fully internal plaquette the angle is at most \(4\delta\), by bi-invariance, and \(2q_p\le8\delta^2\). A crossing plaquette costs at most two, independently of the exterior. The Haar probability of the cap is at least \(c\delta^3\) for an absolute \(c>0\), by integrating the radial density \(2\sin^2 u/\pi\) and using \(\sin u\ge2u/\pi\) on \([0,1]\). Thus the box normalizer \(Z_y=\int e^{-\beta S_y}d{\rm Haar}\) obeys
\[
  -\log Z_y\le \beta(192s^4\delta^2+384s^3)
                     +4s^4\log(1/(c\delta^3)).
\]
The relative entropy of the conditional law against product Haar is \(-\beta P_y S_y-\log Z_y\ge0\), by convexity of \(u\log u\). Each face in \(Y_y^\nu\) is internal, and \((s-1)^4\ge s^4/16\). Division gives (5). No large-volume concentration statement is needed here.

**PROVED.** Fix a nonempty finite list of positively oriented plaquettes \(F\), at arbitrary offsets, such that \(F+z\) uses only links exterior to \(V_t(z)\). Declare the exterior at \(z\) bad if the mean of \(q_p\) on this list exceeds \(h>0\). Several such tests may be used, with the exterior bad if any test fails. Write \(k\) for their number, \(B_z\) for the bad event and \(G_z\) for its complement. With \(A,W_z,E\) as in (3), every \(f\) in the spectral subspace \(\mathbf1_{[0,1]}(H_s)L^2(\mu)\) satisfies
\[
 \frac1A\sum_z\langle {\bf1}_{B_z}f,W_z f\rangle
       \le \rho E,\qquad
 \rho={k\over h}\left[2(1+2s/R)^4m_s+2592(s/R)^4\right].               \tag{6}
\]
The size of each list, the torus side and the values of \(f\) have disappeared from the bound. The weight on the left is nonnegative, since the bad event is exterior to every cube used in \(W_z\).

**PROVED.** For one list use \({\bf1}_{B_z}\le (h|F|)^{-1}\sum_{(d,\nu)\in F}q_{z+d,\nu}\), and sum this bound for several lists. It remains to bound one translated plaquette in the weighted sum. Fix \(x\) and \(g=D_x f\). For each \(j\in J\) write \(y=z+d-j\), and set \(p^+(v)=\max_{j\in J}p(v-j)\). Averaging the change of variable over \(j\) gives
\[
 \sum_z p(x-z)\int q_{z+d,\nu}|g|^2d\mu
      \le\sum_y p^+(x-y+d)\int Y_y^\nu |g|^2d\mu .                    \tag{7}
\]
The weights on the right are at most one and sum to at most \(A(1+2s/R)^4\). Indeed the nonnegative one-dimensional sine weight has interval superlevel sets on the circle. Expanding each superlevel set by \(\{0,\ldots,s-2\}\) adds at most \(s\) sites. Integration in the level shows that the one-dimensional sum increases by at most \(s\), while its original sum is at least \(R/2\). The four-dimensional maximum factors by coordinates.

**PROVED.** Write \(g=P_y g+D_y g\) in (7). Since \(Y_y^\nu\le1\) and \(P_yY_y^\nu\le m_s\), its weighted squared norm is at most \(2m_s\|g\|^2+2\|D_y g\|^2\). For the latter terms one needs a sum of double residuals with no volume factor. For distant pairs the squared double residual is exactly the cross term in \(\|H_s f\|^2\). For the close pairs use \(\|D_yD_x f\|^2\le\|D_x f\|^2\) and the elementary absolute cross-term bound in (4). Consequently
\[
   \sum_{x,y}\|D_yD_x f\|^2
        \le s^8\|H_s f\|^2+2(2s+1)^4s^4 E .                            \tag{8}
\]
In (7), sum in \(x\) and divide by \(A s^4\). For the double residuals discard the weights using \(p^+\le1\). Use \(\|H_sf\|^2\le E\) on the indicated spectral subspace, \(A\ge R^4/16\), and \((2+1/s)^4<40\). This gives (6). The use of (8) makes (6) an estimate on the fraction of **Dirichlet energy** attributable to the discarded exteriors, including for functions concentrated on rare configurations.

**PROVED.** Suppose (1) is known only conditionally on \(G_z\), at every \(z\), for the restrictions of invariant functions. If \(\rho<1\), the gap on the centered invariant space obeys
\[
        v_s\ \ge\ \min\{1,\ b_R(1-\rho)^2\gamma-e_{s,R}\}.              \tag{9}
\]
Indeed \(\sum_z\langle{\bf1}_{G_z}f,W_z f\rangle\ge(1-\rho)AE\) on \(\mathbf1_{[0,1]}(H_s)\). On this good part replace the first factor \(f\) by \(Q_z f\), since \(G_z\) is exterior-measurable. Conditional (1) yields \(\sum_z\|{\bf1}_{G_z}Q_z f\|^2\le R^4 E/\gamma\) by summing the nonnegative small-cube energies. Cauchy–Schwarz followed by (4) proves (9) on this subspace. The complement already has spectrum in \([1,\infty)\). The finite-volume kernel was identified after (4).

**PROVED.** At \(\beta\to\infty\), one may take \(s\to\infty,\ R/s\to\infty\) and fixed \(k\), and let \(h\) decrease to zero slowly enough that \(\rho\to0\). For example, for \(\beta\) large, take \(s=\lceil\beta^2\rceil,\ R\ge\beta^4,\ h=\beta^{-1/3}\). Then (5)–(6) have this property. A face bearing the center flux of row 1224 has \(q_p=1\) on its specified tangential plaquettes and is excluded by that face test. The open local inequality in (9) concerns the actual Wilson filling of boxes whose listed face means are small. It still includes exteriors with isolated rough plaquettes and exteriors with large coherent holonomy.

## Boundary tests at the Wilson fluctuation scale

**PROVED, using the periodic marked-plaquette bound.** For even \(s\ge4\), (5) can be replaced by
\[
                         m_s=\min\{1,C(s^{-1}+\beta^{-1})\}.             \tag{10}
\]
The input is [row 1155, (9)](gap-solve7-astra62.md), with its hand proof by transfer positivity and Hölder's inequality, and its [reading of the coupling reduction](gap-solve7-check-opus.md). The transfer and insertion method credits Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. In a periodic \(s^4\) Wilson box the input is \(\mathbb E\exp(c\beta\sum_{p\in D} 2q_p)\le C_0^{|D|}\) for any deterministic plaquette set \(D\).

**PROVED.** Put periodic \(s^4\) links on the same \(4s^4\) variables as the conditional box. Every fully internal face agrees with its periodic counterpart. All other terms in either action touch a boundary layer, with at most \(C_1s^3\) terms altogether by the boundary count used for (5), and each term is in \([0,2]\). Thus the ratio of the two **normalized** densities is at most \(\exp(2C_2\beta s^3)\), uniformly in the prescribed exterior. Apply this comparison to the exponential moment on the \((s-1)^4\) internal plaquettes of orientation \(\nu\). Jensen gives \(2c\beta |J| P_yY_y^\nu\le 2C_2\beta s^3+|J|\log C_0\), which proves (10). In particular if \(s\ge\beta\) and \(k\) is fixed, the good tests in (9) may demand mean \(q_p\le K/\beta\) for fixed sufficiently large \(K\), provided \(\beta(s/R)^4\) is small. This is an upper test on the ordinary size of a fluctuation.

**PROVED.** There is a second exclusion that uses local conditional probabilities. Let \(B_z\) be the union of \(k'\) translated exterior events \(B_{z,i}\). For each \(i\) suppose the update on \(V_s(z+d_i)\) at a fixed offset \(d_i\) satisfies \(P_{z+d_i}{\bf1}_{B_{z,i}}\le u_i\) uniformly in its exterior. In (6) a valid energy fraction for this union is
\[
                    \rho'=2\sum_{i=1}^{k'}u_i+
                                         2592 k'(s/R)^4.                \tag{11}
\]
For one \(i\), apply \(\|{\bf1}_{B_{z,i}} g\|^2\le2u_i\|g\|^2+2\|D_{z+d_i}g\|^2\) with \(g=D_xf\). The first term gives \(2u_i E\) after the weighted translation sum. For the second discard \(p\le1\), change variables \(y=z+d_i\), and apply (8). The bound adds over \(i\), including when events overlap. It adds to (6) for the union with the upper action tests. No independence between patches is assumed.

**PROVED, using the local two-loop estimate of row 1141.** Fix a tangential three-dimensional cube of exterior vertices of side \(t\) beside a face of the patch, with all its internal tangential links exterior. For example take the plane with one coordinate \(z_\mu-1\) and the three other coordinates in the corresponding intervals of length \(t\). Assume \(R\ge 2s,\ s\) sufficiently large. For any integer \(6\le r\le s/32\), one may require the following boundary condition at the additional cost
\[
          \rho'\ \le\ C(R/r)^3 e^{-c r^3}+ C\,s/R                      \tag{12}
\]
per face in (9). On every accepted face, simultaneously for every adjoint site field \(v\) there,
\[
 \sum_{\text{face}} |v_x|^2 \ \le\
       C(r^2+1+\beta)\sum_{\substack{xy\ \mathrm{internal}\\
                                     \mathrm{tangential\ bond}}}
                  |v_x-\operatorname{Ad}(U_{xy})v_y|^2 .                \tag{13}
\]
The proof of the curvature pinning and the deterministic Poincaré inequality is due to [row 1141, (3)–(7)](gap-crux2-astra62.md). What is needed here is their conditional version in a translated update, together with (11) on the low spectral subspace.

**PROVED.** Partition each tangential side first into intervals of lengths between \(\lfloor s/4\rfloor\) and \(2\lfloor s/4\rfloor\), by merging a short last interval. Partition each resulting interval into intervals of lengths in \([r,2r]\) in the same way. Each first rectangle fits, with its internal links, in a translated side-\(s\) update. In each small rectangle take disjoint three-site cells carrying the two tangential plaquettes of row 1141, with at least \(|B|/6^3\) cells in a rectangle \(B\). At their common root, with holonomies \(g_1,g_2\), a cell is accepted when
\[
 \min_{|v|=1}\sum_{l=1}^2|v-\operatorname{Ad}(g_l)v|^2
                       \ge [8(1+6\beta)]^{-1}.
\]
The one-link conditional law is the tilt of uniform measure on the unit quaternions by the six Wilson staples. Row 1141, (3)–(4), gives acceptance probability at least \(1/2\) conditional on all links outside the cell. It allows arbitrary fixed exterior links, so it holds after fixing the exterior of the side-\(s\) update and exposing earlier disjoint cells. Iterating the conditional bound on \(3^{-\#\mathrm{accepted}}\), exactly as in its (7), bounds the probability that fewer than one quarter are accepted by \(e^{-c r^3}\). A first rectangle fails if any small rectangle in it fails. Its conditional failure probability is at most \(C(s/r)^3e^{-c r^3}\). There are at most \(C(R/s)^3\) first rectangles. Formula (11) now proves (12).

**PROVED.** On each accepted small rectangle the norm of \(v\) at each accepted root is controlled by \(C(1+\beta)\) times the sum of its eight bond differences squared, by telescoping around the two plaquettes. Their bonds are disjoint. The scalar Neumann Poincaré inequality controls the variance of \(|v|\) on this rectangle by \(Cr^2\) times its bond energy, since \(\big||v_x|-|v_y|\big|\le|v_x-\operatorname{Ad}(U_{xy})v_y|\). The positive density of accepted roots also controls its mean squared by a constant times that variance per site plus the sum of the squared values at the roots per site. These are the estimates following (7) of row 1141. Sum over the rectangles to obtain (13). Taking \(r=\lceil(D\log(2+R))^{1/3}\rceil\) for a sufficiently large absolute \(D\), with \(s\ge32r\), makes the first term in (12) tend to zero. In particular the estimate is compatible with \(\log R=O(\beta)\) and even \(s\) of order \(\beta^2\). On that sequence the factor on the right of (13) is \(O(\beta)\).

**ARGUED.** Equations (9)–(13) allow a local proof to keep exterior faces with small average action and a quantitative obstruction to a covariantly constant color axis on every face cell. Row 1224's coherent center-flux boundary is removed. The probability statements behind (13) alone would leave the possibility that slow eigenfunctions put almost all their updating energy on the exceptional faces. Equation (11) addresses that possibility. The operator in (13) still acts on site colors. The inequality needed in (9) acts on scalar functions of Wilson links in the interior.

## Resampling an interior while its boundary can move

**PROVED.** Let \(b\ge0\) be an integer with \(2(t+2b)+4\le N\). Enlarge \(I_z\) by a collar of width \(b\) on every side and write \(L_z^{\rm out}=s^{-4}\sum_{x\in I_z^{\rm out}}D_x\), with \(R'=R+2b\) origins per direction. Keep \(Q_z\) for the original inner \(V_t(z)\). Condition on all links outside the enlarged union \(V_{t+2b}(z-b{\bf1})\). On each accepted exterior \(\omega\), it now suffices that
\[
       \gamma\|Q_z f\|_{L^2(\mu_\omega)}^2
                           \le \langle f,L_z^{\rm out}f\rangle_{\mu_\omega}.
                                                                          \tag{14}
\]
Inside this conditional law \(Q_z\) conditions on **all** the links outside the inner \(V_t(z)\), including the random collar. The outer filling and its ordinary updated subcubes use exactly the Wilson conditional distributions, by the tower property. If \(G_z\) tests the outer exterior and (6), (11) give total energy loss \(\rho_*<1\), then
\[
         v_s\ge\min\{1,\ b_R(R/R')^4(1-\rho_*)^2\gamma-e_{s,R}\}.        \tag{15}
\]
Indeed (3) on the good events uses only the sum of the left sides of (14), and \(\sum_z L_z^{\rm out}=(R')^4 H_s\). The rest of (4) and (9) is unchanged because \(W_z\) has the original inner support. The exclusion bounds work for any offsets from that support. For (12), a bounded ratio \(R'/R\) keeps the number of outer face rectangles within a constant times \((R/s)^3\).

**PROVED.** A field reading supported entirely on the artificial outer face has \(Q_zf=0\) when \(b\ge2\). Such a reading alone cannot violate (14), however slowly it rotates in the conditional dynamics. A nearly conserved function that also depends on the inner fields can violate (14). Its energy has to be compared with its variance **after the collar is observed**. This distinction matters for the proposed face-order obstruction in row 1224.

**PROVED, using the periodic marked moment of row 1155.** One can also require small mean action in every mesoscopic four-dimensional box along an outer collar. Here is a version with explicit geometry. Take even \(s\) divisible by four, \(l=s/4\), and a tangential exterior face of side \(t'=t+2b\) with \(R'/R\) bounded. Cover that face by at most \(\lceil t'/l\rceil^3\) tangential boxes with \(l\) sites per direction, allowing the last ones to overlap. Extend each outward by \(l\) layers, choosing internal plaquettes wholly exterior to the enlarged patch. This uses only a fixed number of torus collars, and they can be embedded when \(N\ge 4(t'+s)\). On each resulting four-box test the mean of the \(q_p\) at the \((l-1)^4\) inner base points, in all six orientations separately. For \(l\ge\beta\) the conditional probability that any one of the six averages exceeds \(K/\beta\) is at most \(6e^{-c_1l^4}\) for an absolute fixed \(K\) large enough. Indeed the periodic comparison used for (10) bounds the logarithm of its moment at parameter \(2c\beta(l-1)^4\) by \(C_3\beta l^3+(l-1)^4\log C_0\). Markov's inequality gives the result by increasing \(K\). The comparison requires even \(l\ge4\), so take \(s\) divisible by eight. The bound is uniform given the exterior of the four-box. It persists given the exterior of a containing side-\(s\) update by nested conditioning. Applying (11) costs at most
\[
                 C(R/s)^3 e^{-c_1l^4}+ C\,s/R
\]
per face. This admits local upper tests throughout these collars even when the number of boxes grows exponentially in \(\beta\). The separate three-dimensional tests in (10) and (13) still serve a different purpose on the boundary layer itself.

**PROVED, conditional physical consequence.** Take a sequence of even periodic Wilson tori at \(a_j\downarrow0,\ a_j N_j\to\infty\), and \(a_jR_j\to L>0\). One concrete choice is even \(s_j\) divisible by eight of order \(\beta_j^2\), \(b_j=\lfloor R_j/2\rfloor\), \(s_j=o(R_j)\), with \(\beta_j\to\infty,\ \log R_j=O(\beta_j)\) and \(\beta_j(s_j/R_j)^4\to0\). Use (10) with \(h=K/\beta_j\) and (12) with the stated logarithmic \(r\). For any fixed collection of the indicated faces, a fixed sufficiently large \(K\) makes \(\rho_*\le1/2\) eventually, including the mesoscopic collar tests. In fact the contribution in (10) is \(O(k/K)\), and the other displayed losses tend to zero. In (15) one has \(R/R'\ge1/2\), \(b_R\ge1/16\). Hence it would suffice to prove
\[
  \gamma_j\ge C_* (s_j/R_j)^2
  \quad\hbox{in (14) on all accepted exteriors},\qquad
  C_*>1024\cdot40\pi^2.                                                 \tag{16}
\]
Then \(v_{s_j}\ge c(s_j/R_j)^2\ge c'(a_js_j)^2\) eventually for some \(c,c'>0\). The constants in (16) come from (15) and determine the numerical sufficient condition. Row 1254, (17), upgrades this to a common positive cube gap at bounded physical update size. On that row's matched diagonal one also needs the logarithms of the source suprema and support sizes to be \(o(a_jN_j)\), reflection-positive convergence of the padded connected forms, and a dense centered family in the full physical Hilbert space. Under these premises its (1)–(4), using the finite-torus propagation bound of Bhattacharjee, Bhattacharya, Lockwood and Romanov, give a strictly positive physical spectral threshold. Neither continuum existence nor that matching has been assumed in proving (5)–(15).

## A direct lower bound for the conditional Wilson variance

**PROVED.** On \(t=2^n(s/2)\), with \(s\) even, \(t\ge s\) and \(b\ge s\), the original conditional Wilson law satisfies (14) for *every* outer exterior with
\[
                       \gamma=2^{-8}\exp(-440\beta t^3).                \tag{17}
\]
This lower bound costs a three-dimensional interface. No term proportional to the four-volume occurs in its exponent.

**PROVED.** First fix the collar as well, so the only free links have bases in the inner cube of side \(t\). Bisect into rectangles by halving each coordinate once per round. At a cut of a rectangle with longest side \(\ell\), delete the plaquette terms that read free links of both children. The remaining law is a product between the two children at this fixed exterior. At most \(48\ell^3\) terms were deleted. Indeed a crossing plaquette has a link based in one of the two layers at the cut, and each site contributes at most \(4\cdot6\) incidences. The ratio of the supremum to the infimum of the true density relative to this product is at most \(e^{96\beta\ell^3}\), since each normalized trace has range two.

**PROVED.** If \(l\le d\mu/d\nu\le u\), both the variance and the integrated conditional variance given any fixed exterior sigma-field compare with factors \(l,u\), by minimizing squared error over constants or exterior functions. On a two-factor product the variance is bounded by the sum of the two update variances, by expanding in the commuting coordinate projections. Hence on the true law the sum of the two child update variances bounds the parent variance from below with factor \(l/u\). On each child repeat the argument with everything else fixed and then integrate over what was fixed. Along any path through the cuts the sum of the logarithmic losses is at most \(4\cdot96\beta t^3\sum_{j\ge0}2^{-3j}<440\beta t^3\). This proves a lower bound using the sum of update variances on the terminal tiles of side \(s/2\).

**PROVED.** Each terminal tile fits in at least \((s/2)^4\) distinct side-\(s\) updates with origins in \(I_z^{\rm out}\). Every such side-\(s\) update contains at most \(2^4\) entire tiles. After integrating out the collar, enlarging the tile can only increase its integrated conditional variance, by nested orthogonal projections. Averaging over its containing cubes and counting gives a factor at most \(2^8s^{-4}\) in front of the unnormalized sum of their variances. This proves (17), with the normalization in (14).

**PROVED.** The first bisection really has density oscillation at least \(\exp(c\beta t^3)\), including at any exterior accepted above. Take an even \(t\ge 8\), a central cut normal to direction one, and all free links equal to one. In the first layer of the right half change the direction-two links based at sites at least two steps from the tangential ends to \(-1\). Each changed link now gives a crossing \(12\)-plaquette of trace divided by two equal to \(-1\), against \(+1\) previously. At least \((t-4)^3\) such terms change. Any other affected crossing plaquette is interior and initially maximized its trace. The rest, including all terms seeing a prescribed exterior, keep their former values in the cut weight. Continuity and positivity of the density give the same lower bound on essential oscillation. This applies to the proof that compares the two densities by their extreme ratio. A sharper variance inequality can integrate the interface against its true measure.

**GUIDE.** For that integration a tempting replacement is to refill two independent halves and sew their tangential links in the best relative gauge. Row 1155, (20), already gives an obstruction for the actual Wilson slice. Against any fixed reference, the probability of squared gauge-optimized link distance below \(c\,t^3/(1+\beta)\) is exponentially small in \(t^3\). Its proof conditions on disjoint marked links, so the same argument applies on an internal face away from any prescribed exterior. Paying the positive electric mismatch across this one sharp cut still costs order \(t^3\) on typical independent fillings. This is the earlier obstruction to that method of sewing. It gives no lower bound of that size on the cost of a correlated refill using a collar.

**OPEN.** At \(R\) of order \(1/a\) and \(s\) of order \(\beta^2\), (17) falls below the scale in (16). The face bounds (10) and (13) make no estimate of the change of the *interior conditional law* between two correlated refills. In particular they do not improve (17) to an inverse-square lower bound.

## Testing the local input against a Wilson short-distance mode

**PROVED, using the earlier Wilson packet estimate.** Let \(\beta\to\infty\), \(\beta\le B\log N\) on even symmetric tori, \(R=\lfloor\beta^\delta\rfloor\), \(0<\delta<1/48\), and let \(s\) be even of order \(R^{1/2}\). Take \(0\le b\le R/2\). Use the upper face tests (6) with \(h=s^{-1/3}\) on a fixed number of faces and use the color tests (12) with \(r=\lceil(D\log(2+R))^{1/3}\rceil\). Then \(\rho_*\to0\). Indeed (5) divided by \(h\) and \((s/R)^4/h\) both tend to zero. The loss in (12) tends to zero as above. On this sequence (14) cannot hold on those good exteriors with
\[
                         \gamma_j/(s_j/R_j)^2\longrightarrow\infty .    \tag{18}
\]
This uses the actual Wilson law even though the local candidate can discard the flux boundary and the nearly reducible faces.

**PROVED.** [Row 1231, (35)](gap-solve26-astra62.md) uses the long-time power law of a bounded mesoscopic magnetic packet and the finite-speed argument of Bhattacharjee and coauthors. It gives \(v_u R/u\to0\) for \(u\le C R\) on these tori. Its [packet check](gap-solve26-check-opus.md) covers the global gap used here. The same-torus upward comparison of row 1254 gives \(v_s(R/s)^2\to0\) in this range. For clarity, if the ratio stayed bounded below, (37) of that row at \(u=R\) would give \(v_R\) bounded below, contradicting the packet at \(u=R\). But (15) and \(\rho_*\to0\) give a coefficient of \(\gamma\) bounded below by a positive number and a subtraction bounded by \(40\pi^2(s/R)^2\). If (18) held, (15) divided by \((s/R)^2\) would diverge, as \(R/s\to\infty\), which is impossible. In particular the obstruction to a large patch gap at these shrinking physical sizes cannot all be assigned to the discarded exteriors. The argument makes no assertion about the typical value of the conditional gap.

**PROVED.** For a refill that literally pays the full electric action of an interpolating collar, a thick collar still has a cost. Take two independent Wilson readings \(X,Y\) on a three-dimensional internal face of side \(d\), in boxes with arbitrary fixed exteriors and all marked plaquette links free. For any interpolation through \(w\ge1\) normal steps, allow arbitrary normal links and intermediate tangential links. Use temporal gauge along each normal line. Each final link then has the form \(g_xY_{xy}g_y^{-1}\), with the gauge \(g\) allowed to depend on the entire interpolation. For each tangential link the sum of the squares of its \(w\) successive chord displacements is at least its total squared chord displacement divided by \(w\). Each such square is twice a normal plaquette deficit. Therefore the electric Wilson action is at least \(\beta d_G(X,Y)^2/(2w)\). By row 1155's disjoint-plaquette argument recalled above, \(d_G^2\ge c d^3/(1+\beta)\) except with probability at most \(e^{-c'd^3}\) for sufficiently large \(d\). This bound for a box face uses a stride-four subgrid away from its ends, still containing at least \(c''d^3\) disjoint marked plaquettes. It is uniform after fixing the reference copy. In particular \(w=O(d)\), \(\beta\ge1\), still costs at least \(c'''d^2\) with that probability. A refill argument paying a **difference** of actions or integrating over the normalized collar could recover a cancellation that this absolute estimate cannot see.

## Comparing the two boundary connections

**PROVED.** Two exterior faces with corresponding three-dimensional coordinates can also be required to satisfy a joint estimate. Denote their tangential links by \(U_e,V_e\). Suppose the faces are separated far enough that a side-\(s\) update enclosing one first rectangle in the proof of (12) misses the other face. On a set of accepted exteriors having the same energy loss bound (12), every field of quaternions \(v_x\), of arbitrary length and direction, obeys
\[
  \sum_x |v_x|^2\ \le\ C(r^2+1+\beta)
       \sum_{xy}|v_x-U_{xy}v_y V_{xy}^{-1}|^2.                          \tag{19}
\]
Thus one can test the actual relative transport on two faces, including its scalar component. Site quaternions here form a real four-dimensional vector space.

**PROVED.** In the \(3^3\) cells used for (13), mark one plaquette per cell. With \(H_U,H_V\) the two corresponding plaquette holonomies and \(\alpha,\alpha'\in[0,\pi]\) their class angles, the minimum chord displacement of any unit \(v\) under \(v\mapsto H_UvH_V^{-1}\) is at least \(2|\alpha-\alpha'|/\pi\). Indeed the geodesic distance from \(H_U\) to \(vH_Vv^{-1}\) is at least the difference of their distances to the identity. The conditional class-angle density of a plaquette given all links except a selected link is at most \(C\sqrt{1+\beta}\), uniformly in the six staples. This is precisely the angle lemma in row 1155, (20). The reference angle is fixed when testing the selected link. Therefore the probability of \(|\alpha-\alpha'|\ge c/\sqrt{1+\beta}\) is at least \(1/2\) for some absolute \(c>0\), conditional on that link's exterior. The conditional cell count of (12) applies without an independence assumption between the faces. Around every accepted plaquette the four bond differences telescope, giving the pinned-root estimate \( |v_x|^2\le C(1+\beta)\sum_{e\in p}|\nabla_{U,V}v(e)|^2\). The scalar Neumann argument for \(|v|\) then proves (19). Equation (11) pays for the exceptional outer exteriors in the original four-dimensional estimate.

**GUIDE.** For the next test take two *adjacent* prescribed tangential slices. The normal links between them are unit quaternions \(q_x\) on a three-dimensional sheet. Bergfinn Durhuus and Jürg Fröhlich's layer representation gives the exact conditional Wilson energy \(\frac{\beta}{2}\sum_{xy}|q_x-U_{xy}q_yV_{xy}^{-1}|^2\). The two background fields enter separately. In row 1139, [the equal-face construction](gap-frameless-2d-astra.md) exhibits order for fixed curved pins, and [row 1177, (22)](gap-solve17-astra62.md) bounds a twisted three-dimensional sheet partition function in a fixed periodic background. Equal faces have the exact parallel field \(v=1\) in (19). Neither example tests whether a strictly positive lower bound for the **full** relative quadratic form, together with plaquette deficits of order \(1/\beta\), forces this sheet to relax. That is the question in the following construction.

## A slow conditional sheet with weak, unequal prescribed fields

**PROVED.** There are fixed constants \(K_0,c,C>0\) and examples with arbitrarily large \(\beta\) on a periodic \(d^4\) Wilson lattice, \(d=2m\), \(m\) dyadic, \(d\ge\sqrt\beta+4\), with the following properties. Only the time links at one fixed time and one fixed third spatial coordinate are free. They form a two-dimensional periodic sheet. Every plaquette made entirely of prescribed links has \(1-w_p\le K_0/\beta\). The two tangential connections are unequal. On their periodic faces each individual adjoint quadratic form and the full relative quaternion form in (19) are bounded below by \(c/\beta\) times the squared site norm. Nevertheless, for \(2\le s\le d/16\), the conditional side-\(s\) heat bath has a centered test made solely from elementary **plaquette traces**, with Rayleigh quotient
\[
                        \le C(d/s)^2 d^2 e^{-cd}.                        \tag{20}
\]
This statement holds for sufficiently large \(\beta\) and \(m\). It tests a proposed reduction of (14) to uniform mixing on further conditioned sheets. Its conditioning freezes interior links that (14) resamples.

**PROVED (the Wilson filling).** Use coordinates \(t,x,y,z\). Let \(t=z=0\) be the free sheet of time links. In a tangential \(xy\) template \(\{0,1,2\}^2\) use row 1139's two marked successive horizontal bonds along the upper side. On the first face \(U\) give those bonds the unit quaternions \(e^{\theta{\bf i}},e^{\theta{\bf j}}\), with all other bonds one. On the second face \(V\) use \(e^{(1-\eta)\theta{\bf i}},e^{\theta{\bf j}}\). Here \(0<\eta<1/2\) and \(K>0\) will be fixed in that order, and \(\theta=\sqrt{K/\beta}\le1/4\) eventually. Extend both templates by reflecting in their sides, inverting the link on edge reversal. Repeat at every \(z\), with all \(z\)-links one. Use \(U\) at time zero and \(V\) at every other time.

**PROVED.** All other time links are one except at time zero. At time zero prescribe the normal links in the planes \(z=-1,+1\) to be \(+1,-1\) respectively. Along the complementary arc of the periodic \(z\)-circle join the two prescribed spins by equal steps on a great semicircle, independent of \(x,y\). The two \(tz\)-plaquettes incident to a free spin contribute a constant, since their two traces divided by two sum to zero. The conditional density on the remaining \(q_x\), where \(x\) now ranges over the two-dimensional sheet, is exactly
\[
   Z^{-1}\exp\left[-{\beta\over2}
                 \sum_{xy}|q_x-U_{xy}q_y V_{xy}^{-1}|^2\right]\prod_xdq_x .
                                                                         \tag{21}
\]
A fully prescribed tangential plaquette is a product of at most four factors of angle at most \(\theta\). A fixed mixed plaquette in direction \(x\) or \(y\) has angle at most \(2\theta\), since the prescribed time spin is constant on that bond and conjugation preserves angle. A fully fixed \(tz\) plaquette has angle at most \(\pi/(d-2)\). These facts prove the claimed upper bound on every prescribed plaquette. The trace of the \(tz\)-plaquette against the \(+1\) neighbor reads \(\operatorname{Re}q_x\) exactly, with either loop orientation.

**PROVED (linear stiffness).** Within a template the unmarked identity edges connect all nine sites. Along a path in these edges, variation from a chosen root is at most \(C\sqrt{E_T}\), where \(E_T\) is the tile's half-sum of squared transported differences, with perimeter bonds given half weight. This follows by Cauchy–Schwarz on at most eight bonds. On the first marked bond the map on \(\mathbb H=\mathbb C_{\bf i}\oplus\mathbb C_{\bf i}{\bf j}\) rotates its two orthogonal planes by \(\eta\theta\) and \((2-\eta)\theta\). Hence its displacement of a quaternion is at least \(2\sin(\eta\theta/2)\) times that quaternion's length. Transporting the two ends to the root gives \(\sum_T|v|^2\le C(\eta\theta)^{-2}E_T\) for arbitrary quaternion fields. For either face's individual adjoint form the two marked bonds rotate about orthogonal axes. The sum of squared displacements of a common imaginary quaternion is at least \(4\sin^2((1-\eta)\theta)|v|^2\). The same connected paths prove the adjoint bound. Summation over the reflected tiles and, in three dimensions, over the \(z\)-slices, proves all the claimed stiffness estimates. Constants may depend on the chosen absolute \(\eta,K\).

**PROVED (energy of a bad tile).** Let a tile be bad if its nine unit spins do not all belong to the same chordal \(1/4\)-cap about \(+1\) or \(-1\). When \(\eta=0\), write a root spin \(a+u\) with \(u\) imaginary. The path bound and the two marked bonds give \(4\sin^2\theta\,|u|^2\le C E_T^0\). The distance from the root spin to the nearer sign is at most \(\sqrt{2}|u|\). Every spin in the tile is within \(C\sqrt{E_T^0}\) of the root. Thus a bad tile costs \(E_T^0\ge c_0\theta^2\) with an absolute \(c_0>0\), uniformly down to \(\theta=0\) through positive values. Replacing one of the marked rotations changes its action on unit vectors by at most \(\eta\theta\) in norm. The inequality \(|v+w|^2\ge |v|^2/2-|w|^2\) gives \(E_T^\eta\ge E_T^0/2-C_0\eta^2\theta^2\). Choose \(\eta\) sufficiently small to obtain a bad-tile cost \(c_0\theta^2/4\). The reflected tiles have the same cost.

**PROVED (the entropy at vanishing curvature).** Write \(M=m^2\) for the number of tiles and \(n=4M\) for the number of sites. For the event that every tile is bad, use half the exponent in (21) to pay the cost \(c_0 K M/8\). In the other half keep only a spanning tree of the sheet, dropping nonnegative energies. Successive Haar integration at its leaves gives exactly \(z(\beta/2)^{n-1}\), where \(z(b)=\int e^{-b(1-\operatorname{Re}q)}dq\le C b^{-3/2}\) for \(b\ge1\). Each edge acts by an orthogonal Haar isometry on \(S^3\). The bound on \(z\) follows by integrating \(\sin^2 u\le u^2\) with \(1-\cos u\ge 2u^2/\pi^2\). For a lower bound on \(Z\), require every spin to be within \(\beta^{-1/2}\) of \(+1\). This has Haar probability at least \((c\beta^{-3/2})^n\). On this set each bond displacement is at most \(2\beta^{-1/2}+\eta\theta\), since its rotation moves \(+1\) by at most \(\eta\theta\). There are \(2n\) bonds. Consequently
\[
 \Pr(\text{all tiles bad})^{1/M}
 \le \exp\!\left[-c_0 K/8+C_1+C_2\eta^2K+
                              {3\log\beta\over 2M}\right].              \tag{22}
\]
The tree retains the Haar volume of the spin fluctuations in the numerator. Dropping that volume would introduce a \(\log\beta\) cost at *each* site and would lose this scale. Decrease \(\eta>0\) once to have \(C_2\eta^2<c_0/16\), then fix \(K\) large enough that (22) is below \(p=2^{-40}\) for \(M\ge\log(2+\beta)\). Finally take \(\beta\) large enough for the bound on \(\theta\). The hypotheses on \(d\) imply the condition on \(M\) eventually.

**PROVED.** For any set \(S\) of tiles the probability that they are all bad is at most \(p^{|S|}\). Use the site-reflection chessboard argument of Fröhlich, Israel, Lieb and Simon, as given for this folded geometry in row 1139. Both prescribed faces reflect, also for \(\eta>0\). Given the spins on the two reflection lines, the two interiors factor and have reflected laws. For any mark pattern, Cauchy–Schwarz bounds its probability squared by the product of the probabilities of copying each half into the other. The two resulting cardinalities sum to twice the original one. Subtract \((|S|/M)\log\Pr(\text{all bad})\) from the log probability of \(S\). A maximizer with a positive value would have at least one mark. Either reflected copy must again maximize this difference. Doubling a contiguous marked interval in a row up to a full row, then doubling the full rows, produces the fully marked torus since \(m\) is dyadic. Its difference is zero, a contradiction. All mark events have positive probability by taking spins near an imaginary unit.

**PROVED (a plaquette reading insensitive to one local update).** On the even-coordinate vertices of the sheet declare a coarse edge open when its two spins belong to the same sign cap. Every open path has a single cap sign. Define \(F=+1\) or \(-1\) if that sign has both a horizontal and a vertical open cycle of mod-two winding \((1,0)\) and \((0,1)\), respectively, and \(F=0\) otherwise. Opposite signs cannot both qualify, because those two winding classes have odd intersection on the torus. Membership in a cap depends only on \(\operatorname{Re}q_x\), so \(F\) uses only the elementary plaquette traces identified after (21). In particular its extension to Wilson fields is invariant under gauge transformations and center flips. Under the conditional sheet law the separate symmetry \(q_x\mapsto -q_x\) at every site simultaneously centers \(F\).

**PROVED.** In a horizontal band of \(h=m/8\) coarse faces, periodic horizontally, the probability of no horizontal open cycle is \(O(m^2(4p)^{h-2})\). To see the alternative, start at the lower boundary in the dual graph and cross only closed primal edges. If the upper boundary is unreachable, the frontier of the reached faces separates the two boundary circles and consists of open primal edges. With the lower cap included, the frontier has even vertex degrees and odd total winding around the cylinder because a path from its lower cap to its upper cap crosses the frontier an odd number of times. Decomposing into simple cycles yields the required winding cycle. Otherwise erase loops from a dual crossing. It passes through at least \(h-1\) distinct faces, all bad because a crossed closed edge has endpoints outside the same-cap condition. Counting simple dual paths by their starting point and at most four continuations at each step bounds their probability by a geometric series with ratio \(4p\). The identical estimate holds after exchanging the coordinate directions.

**PROVED.** Take two such horizontal bands with starting rows separated by \(m/2\), and two vertical bands with the same separation. Except on an event of probability at most \(Cm^2e^{-c m}\), each band contains its winding open cycle. Horizontal and vertical cycles meet and have one common sign. A side-\(s\) update with \(s\le d/16\) misses at least one complete horizontal band and one complete vertical band. Those two cycles survive regardless of the new spins. Hence \(F\) stays fixed under every such update on the stated event, and \(\operatorname{Var}F\ge1-Cm^2e^{-cm}\). For a given update its conditional variance averaged in equilibrium equals half the mean square difference of the old and fresh readings. This costs at most twice the exceptional probability. In the full four-dimensional sum only \(s\) origins in each of \(t,z\) hit the sheet. The normalization leaves \(s^{-2}\) times \(d^2\) tangential updates. Division by the variance proves (20). In particular its quotient divided by \((s/d)^2\) tends to zero even for \(s\) of order \(\beta^2\) on \(d\) growing exponentially in \(\beta\).

**PROVED.** At each fixed \(\beta,d,s\) the obstruction extends to an open neighborhood of these prescribed links with an arbitrarily small loss in (20). The finite positive Wilson density varies uniformly continuously with the pins. The test uses the fixed plaquette-trace thresholds and a finite graph. Threshold ties have zero Haar probability, including in the two resampled configurations for a cube variance. This follows by exposing a free link in each measured plaquette. Dominated convergence gives continuity of the variance and update forms as the exterior changes. The strict linear coercivity and plaquette upper bounds also persist on shrinking these neighborhoods, allowing a factor two in their constants. This continuity asserts no uniform lower bound on the probabilities of those exterior neighborhoods.

## Letting neighboring planes move

**PROVED.** In the example (21) let the next plane \(z=1\) move as well. The old cap reading \(F\) then satisfies \(\mathbb E F^2\le C m^2 e^{-c\beta m}\) for sufficiently large \(\beta,m\). Here the other end spin at \(z=2\) differs from \(-1\) by at most \(\pi/(d-2)\). Thus the slow reading exhibited in (20) loses its variance when this one neighboring plane is released.

**PROVED.** With end spins \(1,-1\), the minimum vertical action *per column*, before its factor \(\beta\), for given first free spin \(q\), is
\[
 \min_{q'} (1-\operatorname{Re}q)+(1-q\cdot q')+
                        (1+\operatorname{Re}q')
       =3-\operatorname{Re}q-|q-1|
       =\tfrac32+\tfrac12(|q-1|-1)^2 .                                \tag{23}
\]
Changing the second end spin by distance \(\pi/(d-2)\) alters each column energy by at most that amount. For \(q\) in either \(1/4\)-cap, (23) exceeds \(3/2\) by at least \(9/32\). Mark a tile if any even corner spin of its first layer is in either cap. When all tiles are marked at least \(M/4\) distinct columns incur this excess. For a lower bound on \(Z\) use the two constant spins \(e^{\pi{\bf i}/3},e^{2\pi{\bf i}/3}\) on the two layers, within chord \(1/\beta\) at every site. Their vertical energy is \(3/2\) per column up to \(O(1/\beta+1/d)\), and their horizontal energy is \(O(\theta^2+\beta^{-2})\) per site. The Haar cost per site has log magnitude \(O(1+\log\beta)\). Thus the \(M\)th root of the all-marked probability is at most \(\exp[-c\beta+C(1+K+\log\beta)+C\beta/d]\), at most \(e^{-c'\beta}\) eventually. The same planar reflection argument bounds specified marked sets. A simple cap cycle winding once visits at least \(m\) distinct even vertices, each marking its own northeast tile. Counting walks gives the claimed bound on \(F^2\). This argument uses the normalized two-plane law.

**PROVED (any fixed thickness).** For every fixed \(w\ge2\) there are also weak, unequal pins for a sheet of \(w\) free planes such that a *different* center-neutral Wilson reading has the exponentially small conditional Rayleigh quotient (20), with constants allowed to depend on \(w\). The two individual adjoint forms and their relative quaternion form still have lower bounds \(c_w/\beta\), and every fully prescribed plaquette still has deficit at most \(C_w/\beta\). This first argument chooses its parameters separately for each \(w\).

**PROVED.** Put \(L=w+1\). At the same time cut prescribe the normal spins at \(z=0,L\) to be \(+1,-1\) and free those at \(1,\ldots,w\). Interpolate the pins around the complementary arc as before, with \(d\ge 2L+\sqrt\beta\). Repeat identical tangential backgrounds at all \(z\). For one column write \(q_0=1,\ q_L=-1\). The minimum of \(\frac12\sum_{k=0}^{L-1}|q_{k+1}-q_k|^2\) on the product of unit spheres is \(E_0=L(1-\cos(\pi/L))\). To see this, extend by \(q_{k+L}=-q_k\) to a \(2L\)-cycle. Its Fourier modes have odd index, so the smallest eigenvalue of the discrete Laplacian there is \(2(1-\cos(\pi/L))\), as follows by applying the Laplacian to the finite exponential basis. Equality holds exactly on the harmonics of indices \(1,2L-1\). Thus the minimizing columns have
\[
           q_k=\cos(k\pi/L)+v\sin(k\pi/L),\qquad
                          v\ \text{a unit imaginary quaternion}.        \tag{24}
\]
Indeed the endpoint fixes the cosine coefficient. Evaluating the unit-length conditions at \(k=1,L-1\), for \(L\ge3\), gives \(\operatorname{Re}v=0,\ |v|=1\). These columns realize the bound. This is a finite Fourier identity with a formula for every \(L\).

**PROVED.** First use only the marked bond with axis \({\bf i}\), with equal rotations \(e^{\theta{\bf i}}\) on its two faces, all other tangential links one. A tile is good if every one of its columns stays within chord \(1/8\) at every free height of the same one of the two profiles (24) with \(v=\pm{\bf i}\). Give each site's vertical excess above \(E_0\) its reciprocal tile multiplicity as weight, and share horizontal bond energies as before. For sufficiently small \(\theta>0\) every bad tile has excess at least \(a_w\theta^2,\ a_w>0\). Otherwise there are bad tiles with \(\theta\downarrow0\) and excess \(o(\theta^2)\). The unmarked connected bonds at each height make the columns agree there to \(o(\theta)\). The marked bond then gives \(\sin\theta\,|\operatorname{Im}q_k\times{\bf i}|=o(\theta)\) at each height of a representative column. The vertical excess tends to zero. Compactness of the finitely many unit spheres and (24) force a limiting common profile with \(v=\pm{\bf i}\), inconsistent with the closed bad set.

**PROVED.** Now add the second bond with equal rotations \(e^{\xi\theta{\bf j}}\) and change the first right-hand rotation to \(e^{(1-\eta)\theta{\bf i}}\). Take fixed \(\xi,\eta>0\) sufficiently small. The squared-norm comparison used for (21) lowers the previous excess bound to at worst \(a_w\theta^2/2-C_w(\xi^2+\eta^2)\theta^2\). The vertical excess is nonnegative and unchanged. All linear stiffness estimates hold as before, with the individual adjoint forms using the two nonzero axes and the relative form using \(\eta\theta\). For a lower partition bound restrict the spins to \(\beta^{-1/2}\)-balls about the \(+{\bf i}\) profile. The exact profile minimizes the smooth vertical energy on the product of unit spheres. Its first derivative in every tangent direction is zero. Bounded second derivatives on this fixed compact product and Taylor's formula along shortest great circles bound the vertical excess by \(C_w/\beta\) per column. The horizontal cost per site is at most \(C_w(\beta^{-1}+(\eta^2+\xi^2)\theta^2)\), since the unperturbed rotations fix the profile.

**PROVED.** Subtract the same constant \(nE_0\) from every energy, where \(n=d^2\). In the upper integral for all bad tiles use half the excess to pay their cost and discard the remaining nonnegative vertical excess. Keep a tangential spanning tree in each of the \(w\) layers. These trees integrate to \(z(\beta/2)^{w(n-1)}\). The lower cap integral retains \((c\beta^{-3/2})^{wn}\). With \(\theta=\sqrt{K/\beta}\), the log of the \(M\)th root of the all-bad probability is therefore bounded above by
\[
        -c_w K+C_w(1+(\eta^2+\xi^2)K)
                               +\tfrac{3w}{2M}\log\beta .
\]
Choose \(\eta,\xi\) sufficiently small first, then a fixed sufficiently large \(K\), then \(\beta,m\) large. This yields the same \(p=2^{-40}\) and the arbitrary-tile estimate by the planar site reflections. All these parameters may depend on the fixed thickness.

**PROVED.** Let \(k_*=\lfloor L/2\rfloor\). Read at every coarse vertex the \({\bf i}\)-component of the imaginary part of \((q_{k_*}+q_{L-k_*})/2\). Each good tile places all its corner readings above \(1/2\) or all below \(-1/2\), since \(\sin(k_*\pi/L)\ge\sqrt3/2\). The exact symmetry \(q_{k,x}\mapsto -q_{L-k,x}\) preserves the pins because reversal interchanges them and negation restores them. It preserves all bond energies and negates these readings. They have a contractible Wilson-loop realization. In the prescribed lower time face use an unmarked identity path in the adjacent template to base the first marked bond and return through identity edges. Reverse the resulting loop if needed to obtain holonomy \(e^{\theta{\bf i}}\). A \(tz\)-rectangle reaching a free \(q_k\) and returning via the fixed \(q_0=1\) gives its holonomy at a common root, since the two spatial \(z\)-paths are identity. Its trace and the trace after concatenating the marked loop give the required component by
\[
             \operatorname{Im}_{\bf i}q_k=
                \frac{\cos\theta\,w(q_k)-w(e^{\theta{\bf i}}q_k)}
                     {\sin\theta}.
\]
The deterministic base paths have bounded length for fixed \(w\). Taking coarse edges open when their two readings have the same strict threshold sign, the four-band proof of (20) applies. There are at most \(s(s+w-1)\) normal-coordinate origins of side-\(s\) updates meeting any free link. This multiplies the one-plane counting bound by at most \(1+w/s\), bounded for fixed \(w\). The conditional centered variance remains bounded below and the Rayleigh quotient is exponentially small in \(d\).

## A thickness growing with inverse coupling

**PROVED.** The ordered conditional example extends to a thickness \(w\) of order \(\sqrt\beta\), with a common constant in the weak-plaquette bound and with a completion in which **every** plaquette, including each previously free plaquette, has \(1-w_p\le C/\beta\). In this construction the conditional variance stays bounded below and the quotient of the loop reading above is at most
\[
               C(1+w/s)(d/s)^2d^2 e^{-c w d}.                           \tag{25}
\]
Here \(d=2m,\ m\) is dyadic, \(d\ge 2(w+1)+\sqrt\beta,\ 2\le s\le d/16\). The constants are independent of \(d,s,w,\beta\) along the specified sequence. The free region consists of one time-link layer whose other three dimensions grow.

**PROVED (column stability with constants).** Take \(L=w+1\ge8\) divisible by four, \(\alpha=\pi/L\), and \(b_k=\cos(k\alpha)+{\bf i}\sin(k\alpha)\). For an arbitrary column with the two specified endpoints, write \(y=q-b\) and \(\Delta u_k=u_{k+1}-u_k\). Its excess \(D_v\) above \(E_0\) is exactly
\[
       D_v=\tfrac12\sum_{k=0}^{L-1}|\Delta y_k|^2
                      -(1-\cos\alpha)\sum_{k=1}^{L-1}|y_k|^2 .          \tag{26}
\]
Indeed the cross term after summation by parts is \(2(1-\cos\alpha)\sum b_k\cdot y_k\), and \(2b_k\cdot y_k=-|y_k|^2\). Expand \(y\) in Dirichlet sines and remove its first mode, writing
\[
 q_k=\cos(k\alpha)+v\sin(k\alpha)+e_k,\qquad
 v=\frac2L\sum_{k=1}^{L-1}(q_k-\cos(k\alpha))\sin(k\alpha).
\]
The eigenvalues are \(2(1-\cos(j\alpha))\), \(1\le j\le L-1\). The first-to-second ratio is \(1/(4\cos^2(\alpha/2))\le1/3\). Hence \(\sum|\Delta e_k|^2\le3D_v\), and telescoping from \(e_0=0\) gives \(\max_k|e_k|\le\sqrt{3LD_v}=\epsilon\). For \(\epsilon\le1/2\), evaluating at \(L/2\) gives \(||v|-1|\le\epsilon\). At \(L/4\) one has \(\big||1+v|/\sqrt2-1\big|\le\epsilon\). Squaring and combining gives \(|\operatorname{Re}v|\le C\epsilon\).

**PROVED.** Use first just the one equal \({\bf i}\)-bond. Let \(D\) be the whole unperturbed tile excess, with the previous multiplicity weights. Suppose \(L\theta\le1,\ 0<\theta\le1/4\) and \(D<u w\theta^2\). Each column has \(D_v\le4D\), so \(\epsilon\le C\sqrt u\). Across an edge with transport \(T\) the first sine coefficient gives \(|v_x-Tv_y|\le C\sqrt{D/L}\), since \(T\) is a conjugation fixing the real part and the coefficient functional has norm \(\sqrt{2/L}\). Connect vertices to a root through the identity edges and use the marked bond once. At that root,
\[
  2\sin\theta\,|\operatorname{Im}v\times{\bf i}|
          =|v-e^{\theta{\bf i}}v e^{-\theta{\bf i}}|
          \le C\sqrt{D/L}.
\]
The perpendicular and real components are \(O(\sqrt u)\), and \(|v|\) is within \(O(\sqrt u)\) of one. Thus the root coefficient and all eight others are within \(C\sqrt u\) of the **same** one of \(\pm{\bf i}\). The residual \(e\) obeys the same bound. For a sufficiently small absolute \(u>0\) the tile is good. This proves a lower bound \(uw\theta^2\) on every bad tile, uniformly in \(L\theta\le1\).

**PROVED.** For the unequal pair and the second weak axis used after (24), the loss in this lower bound is controlled by \(D^\mathrm{pert}\ge D/2-Cw(\eta^2+\xi^2)\theta^2\). This follows edge by edge from the squared-norm inequality and the nonnegative vertical excess. Choose fixed \(\eta,\xi>0\) sufficiently small. On the lower partition event in which all \(q_k\) stay within \(\beta^{-1/2}\) of \(b_k\), (26) gives \(D_v\le Cw/\beta\) by dropping its negative term. The excess tangential cost is at most \(Cw(\beta^{-1}+(\eta^2+\xi^2)\theta^2)\) per column. With the same \(w\) spanning trees in the numerator, \(\theta^2=K/\beta\), and \(M=m^2\), it follows that
\[
 \frac1M\log\Pr(\text{all bad})
       \le -c K w+Cw+C(\eta^2+\xi^2)K w+\frac{3w}{2M}\log\beta .
\]
All constants here are absolute. Decrease \(\eta,\xi\) once further, then increase the fixed \(K\) so that, for \(M\ge\log(2+\beta)\), the right side is at most \(-c'Kw\), with \(c'K>40\log2\). Chessboard reflection gives the corresponding bound \(e^{-c'Kw|S|}\) on any specified marked set \(S\). Repeating the four-band argument with this value of \(p\) proves (25). The lower variance bound uses the symmetry after (24). Its loop reading is defined by actual traces also at these growing heights.

**PROVED.** Choose \(L=4\lfloor\sqrt{\beta/K}/4\rfloor\), which has \(L\theta\le1\) and \(L\asymp\sqrt{\beta/K}\) for large \(\beta\). Complete every column by \(b_k\). Its inner \(tz\) plaquettes cost exactly \(1-\cos(\pi/L)\le C K/\beta\). Its tangential mixed plaquettes cost at most \(C(\eta^2+\xi^2)K/\beta\). The complementary arc and all prescribed plaquettes obey the estimates after (21), with \(d-L\ge\sqrt\beta\). The individual and relative linear stiffness estimates from (21) use the same fixed positive angles in units of \(\theta\), uniformly in the thickness. In particular an everywhere weak-curvature common filling, together with these three stiffness tests on the prescribed connections, permits the slow conditional mode (25). The exterior in (14) has a different geometry and admits four-dimensional motion throughout the collar.

## How often can the Wilson field impose these end holonomies?

**PROVED.** Consider \(M_0\) deterministic contractible loops in the periodic Wilson law, each obtained by peeling at most \(J\) elementary faces from a disk. Put \(q_C=(1-\tfrac12\operatorname{tr}U_C)/2\). Peeling the faces expresses \(U_C\) as a product of conjugates of their holonomies or inverses. The chordal metric on unit quaternions is bi-invariant, so the triangle inequality followed by Cauchy–Schwarz gives
\[
                  q_C\le J\sum_{p\in S_C}q_p .                          \tag{27}
\]
In particular for disjoint plaquette fillings without repetitions, on an even torus, the marked moment in (10) gives
\[
 \Pr\left(M_0^{-1}\sum_C q_C>h\right)
       \le \exp\!\left[-2c\beta h M_0/J+JM_0\log C_0\right].           \tag{28}
\]
This conclusion concerns the unconditioned Wilson probability. In (25) there are \(d^2\) disjoint \(1\times L\) rectangles in direction \(tz\), with perimeter holonomy exactly \(-1\), irrespective of the free links. An open neighborhood of these pins imposes average \(q_C>1/2\). For \(L\le\sqrt{\beta/K}\) and fixed sufficiently large \(K\), (28) bounds the probability of this neighborhood by \(\exp(-c_1\beta d^2/L)\). This quantifies the cost of imposing coherent end holonomies under the full Wilson law, even in the presence of the everywhere weak completion after (26).

**PROVED.** Suppose a translated bank of contractible **perimeters** at \(z\) is readable on the exterior being tested in (9) or (15). The plaquettes used to fill the perimeters may meet its interior. Excluding \(\bar q_C>h\) costs a fraction of low spectral Dirichlet energy bounded by
\[
       \rho_{\rm loops}\le {J^2\over h}
          \left[2(1+2s/R)^4 m_s+2592(s/R)^4\right].                    \tag{29}
\]
Indeed use (27) and sum (7) over at most \(JM_0\) individual translated plaquettes, with coefficient \(J/(hM_0)\). Equations (7)–(8) apply to the integral of \(q_p|D_xf|^2\) at every offset. Only the **bad event** must be exterior-measurable to identify this integral upper bound with the desired loss. Multiplicity of interior plaquettes in the sum is harmless here. In particular on the sequence (16), a bank with \(J\le\sqrt{\beta/K}\), at any fixed threshold \(h>0\), costs \(O(1/(Kh))+o(1)\). Its cardinality can grow without limit. The argument removes corresponding coherent holonomies whenever the perimeters are exterior to the actual cubical resampling in (14). The fixed-sheet eigenfunction in (25) is not an eigenfunction established for that resampling.

**PROVED.** The same energy estimate allows an exterior test of the *existence of a common filling*. Fix \(k\) translated finite lists of plaquettes, allowed anywhere in or near the box. Accept an exterior if some one filling has mean \(q_p\le h\) on **every** list. The minimum over the compact filling space of the maximum of these continuous means is a continuous exterior function, by uniform continuity at finite cutoff. For an exterior which fails, the actual configuration violates at least one list, whatever its interior links. Its indicator is therefore bounded by the sum of the \(k\) actual means divided by \(h\). Applying (7)–(8) proves (6) for this certification cost. The construction after (26) passes even a pointwise weak-plaquette filling test at its stated constant. Equations (28)–(29) see the further alignment of the curvatures along rectangles.

## Keeping a prescribed sheet fixed during a four-dimensional update

**PROVED.** The finite-size criterion can omit the fluctuations on a prescribed sheet, including a sheet as thick as the one in (25). More precisely, at each \(z\) let \(S_z=z+S_0\) be a translated set of links. In two chosen normal coordinates their bases lie in a square of radius \(w_0\) in lattice maximum distance. There is no tangential size restriction. Put \(u=w_0+2s+2=o(R)\). In (14) reveal \(S_z\) along with the outer exterior, keep these links fixed, and replace \(Q_z\) by
\[
 Q_z^\circ=1-\mathbb E_\mu[\,\cdot\mid
                           U_{V_t(z)^c},U_{S_z}].
\]
On the right use only outer small cubes disjoint from \(S_z\), writing \(L_z^\circ\) for their usual sum. Suppose \(\gamma\|Q_z^\circ f\|^2\le\langle f,L_z^\circ f\rangle\) on every accepted conditional filling. Then, for \(u/R\) sufficiently small,
\[
 v_s\ \ge\ \min\left\{1,\
 b_R\bigl(1-Cu/R\bigr)(R/R')^4
       \bigl[1-(1+Cu/R)\rho_*\bigr]^2\gamma
  -\bigl[1+C/\log(R/u)\bigr]e_{s,R}\right\},                           \tag{30}
\]
provided \((1+Cu/R)\rho_*<1\). Here \(\rho_*\) is any sum of the earlier loss bounds for the tests used. One may use tests of the additionally revealed links whenever the pointwise estimates (7) or (11) for those tests hold. With no exclusions take \(\rho_*=0\). All constants in (30) are absolute for one such sheet.

**PROVED.** Modify the patch weights on **origins**. Take \(H=\lfloor\sqrt{uR}\rfloor\), \(r\) the normal lattice maximum distance from the translated square's center, and take \(\chi=0\) for \(r\le u\), \(\chi=1\) for \(r\ge H\), and \(\chi=\log(r/u)/\log(H/u)\) in between. Set \(p'=p\chi,\ A'=\sum p',\ B'=\sum (p')^2\). A positive weight then updates no link of \(S_z\). The loss in either sum is at most \(C R^2H^2\), by counting the two normal directions and using \(p\le1\). Since \(A,B\asymp R^4\), \(A'\ge(1-Cu/R)A\), \(B'\ge(1-Cu/R)B\). In the two-dimensional normal lattice,
\[
     \sum_{x}\sum_{\nu=1}^2 |\chi(x+e_\nu)-\chi(x)|^2
           \le C/\log(H/u).
\]
A layer at radius \(j\ge u\) has at most \(Cj\) crossing edges, each difference at most \(1/(j\log(H/u))\). Summing proves the inequality. A cutoff of this size fits in the periodic normal coordinates.

**PROVED.** For \(\|v\|_\infty\le s\), expand \(\tau_v p'-p'=(\tau_v\chi)(\tau_v p-p)+p(\tau_v\chi-\chi)\). By telescoping the two normal translations and summing over the \(R^2\) tangential origins in the support of \(p\), the second term has squared norm at most \(C R^2|v|^2/\log(H/u)\). On its support, the first term is bounded pointwise by \(C|v|/R\), since the zero-extended sine product has this translation bound, and the support has at most \(C R^2(H+s)^2\) origins. Its norm **on that support** is thus at most \(C|v|(H+s)\). Bounding the square of the first term everywhere by \(\|\tau_v p-p\|^2\) gives
\[
  \|\tau_vp'-p'\|^2\le 2 B(1-\cos\vartheta)|v|^2+
       C |v|^2\left\{\frac{R^2}{\log(H/u)}
                    +\frac{R(H+s)}{\sqrt{\log(H/u)}}\right\}.
\]
We have \(B=((R+1)/2)^4\), \(B(1-\cos\vartheta)\asymp R^2\), \(H/R\le\sqrt{u/R}\), and \(\log(H/u)\asymp\log(R/u)\). Dividing by \(2B'\) proves the squared-translation bound used in (4) with a relative loss at most \(C/\log(R/u)\). Thus the absolute loss in the inverse-square threshold is \(O((s/R)^2/\log(R/u))\).

**PROVED.** For \(W'_z\) given by \(p'\), nested conditioning gives \(Q_z^\circ W'_z=W'_z\), and \(\sum_z W'_z=A'H_s\). Its bad-exterior energy is \(\sum_{z,x}p'(x-z)\int {\bf1}_{B_z}|D_x f|^2\,d\mu/s^4\), since every retained cube leaves the revealed links fixed. Use \(p'\le p\) and the earlier pointwise bounds to control it by \(A\rho_*E\), hence by \(A'(1+Cu/R)\rho_* E\). The sum of the outer retained energies is at most \((R')^4 E\). Cauchy–Schwarz as in (3), followed by the preceding weighted-square estimate and \((A')^2/(R^4B')\ge(1-Cu/R)b_R\), now gives (30). Increasing the absolute \(C\) absorbs the different constants. These arguments extend to a fixed finite number of such sheets by multiplying the cutoffs, with constants then allowed to depend on their number. For that extension bound the sum of their squared normal differences by a fixed multiple of the individual sums and use the union of their supports for the cross term.

**PROVED.** In particular, at \(s\asymp\beta^2,\ R\asymp a^{-1},\ s=o(R)\), one can reveal an entire translated tube wide enough to contain all the Wilson loops that measure (25), including their reference loops and return paths. A function of those links has \(Q_z^\circ f=0\) for that patch and costs no conditional variance. For a fixed number of prescribed tubes with \(w_0+s=o(R)\), (30) retains the sufficient threshold (16) with any fixed strict margin there, if the energy fraction is at most \(1/2\) before the \(o(1)\) losses. A proof would still have to control integration over the four-dimensional region around the tubes. Freezing additional fields can affect its law.

## The same loop readings in the full Wilson law

**PROVED.** The single-plane reading in (20), evaluated as the very same function of elementary plaquette traces in the unconditioned periodic Wilson theory, satisfies
\[
      \Pr_\mu(F\ne +1)\le C d^2 e^{-c\beta d}.                          \tag{31}
\]
For a coarse vertex to be outside its positive cap, its elementary \(tz\)-plaquette must have \(q_p\ge 1/64\). These are distinct plaquettes for distinct coarse vertices. By the marked Wilson moment in (10) the probability for any \(j\) specified vertices to be outside is at most \((C_0e^{-c\beta/32})^j\). In a band consider edges open only when both vertices are in the positive cap. The cylinder argument following (22) gives a simple closed-edge dual crossing when there is no positive winding cycle. For each edge of a simple dual path choose one endpoint of the crossed primal edge that is outside the cap. There are at most two choices per edge, and a vertex can account for at most four different edges of the path. A path of \(n\) steps therefore requires at least \(n/4\) distinct high-action plaquettes, up to a fixed endpoint loss at the band boundary. Summing the resulting geometric bound over paths of length at least \(m/8-2\), then over the four bands, proves (31) for large \(\beta,m\). Consequently \(\operatorname{Var}_\mu F\le 4 C d^2 e^{-c\beta d}\).

**PROVED.** For the loop reading in (25) one can choose its reference loops so that, in the full periodic Wilson law,
\[
                   \Pr_\mu(F\ne0)\le C d^2 e^{-cK d}.                  \tag{32}
\]
Use the tile northeast of each coarse vertex. Inside that tile run a path of identity-template edges to the first marked bond, go around the elementary square touching that bond inside the tile, and return on the reversed base path. Orient the square as required by the reflection. On the prescribed field the holonomy is \(e^{\theta{\bf i}}\). On **every** field its holonomy \(A\) is a conjugate of the elementary plaquette or its inverse. Different coarse vertices use distinct such plaquettes. For any other unit holonomy \(B\),
\[
 |\cos\theta\,w(B)-w(AB)|\le 1-\cos\theta+|1-A|.
\]
Thus a corner reading of magnitude greater than \(1/2\), also after averaging the two heights, implies \(|1-A|\ge\tfrac12\sin\theta-(1-\cos\theta)\ge\theta/4\) for \(0<\theta\le1/4\). For \(j\) specified corners the moment (10) now gives probability at most \((C_0e^{-cK/32})^j\), since their elementary deficits \(2q_p=|1-A|^2/2\) must each exceed \(\theta^2/32\). A winding cycle contains a simple winding cycle, or a simple component of nonzero winding after decomposition, and hence at least \(m\) distinct marked vertices. Counting paths as above gives (32) after increasing the fixed \(K\). This is compatible with the choice of \(L\) after (26). It holds uniformly in the other loop heights.

**PROVED.** By ordinary Cauchy–Schwarz these centered observables have vanishing correlations against any family uniformly bounded in Wilson \(L^2\) when \(d\to\infty\) at the physical size of (16). This remains true with multipliers having logarithm \(o(\beta d)\) in (31) or \(o(d)\) in (32). In particular the two explicit conditional slow modes found here do not give a nonzero massless continuum source at these normalizations. Equations (31)–(32) concern these two specific readings. They give no bound on a normalized family whose variance is concentrated on other interior observables.

## Testing the remaining variance bound with cuts through the box

**PROVED.** In (30) the right side of the conditional inequality can also use the larger form
\[
       \widehat L_z=s^{-4}\sum_{x\in I_z^{\rm out}}
          \big(1-\mathbb E_\mu[\,\cdot\mid U_{V_s(x)^c},U_{S_z}]\big).  \tag{33}
\]
This resamples all free links in a small cube even if the cube meets the sheet. On a conditional filling these are the exact Wilson updates with its revealed links fixed. Each summand's integrated variance is at most \(\|D_x f\|^2\) by nested projections. Summing over \(z\) gives the same budget \((R')^4E\) used in (30), while \(W'_z\) still uses ordinary cubes that avoid the sheet. This version has no reduced update rate at a link immediately beside a pinned sheet.

**PROVED.** For (33) the unconditional finite-volume estimate (17) holds at every joint value of the pins and outer exterior, with the very same constant. At fixed collar and pins bisect the remaining free links by their base points. Deleting the terms that read both children always gives a product law and deletes at most the previous \(48\ell^3\) terms, including when a child is empty. Each terminal tile now updates just its free subset. Each of its former containing small cubes still contains that subset among its own free variables. The comparison by integrated conditional variances and the terminal counting therefore give \(2^{-8}e^{-440\beta t^3}\) once again. This argument applies to arbitrary prescribed pin sets and needs the original dyadic geometry of (17). The larger form in (33) makes this lower bound available also near irregular parts of a sheet.

**PROVED.** One might pin a whole grid of planes to separate the Wilson law into smaller components. There is a geometric cost in (4) for such a proposal. For instance pin all links with one normal coordinate of the base point in \(h\mathbb Z\) on a torus with \(h\mid N,\ s\le h\). Any origin weight \(p_0\) for small cubes that avoid the pins vanishes on an interval of \(s\) consecutive normal-coordinate layers every \(h\) steps. For any displacement \(v\) with \(s/2\le v_1\le s,\ \|v\|_\infty\le s\), a progression \(x,x+v,\ldots\) reaches a zero layer within \(J=\lceil2h/s\rceil+2\) steps. It cannot skip the zero interval since its normal step is at most \(s\). Telescoping up to the first zero, then summing over \(x\), gives \(\|p_0\|^2\le J^2\|\tau_vp_0-p_0\|^2\). There are at least \(c s^4\) such displacements. For any nonzero weight this implies
\[
  s^{-4}\sum_{\|v\|_\infty\le s}
    \frac{\|\tau_vp_0-p_0\|^2}{2\|p_0\|^2}\ \ge\ c(s/h)^2.            \tag{34}
\]
The left side is the error paid by the termwise close-pair comparison in (4). If \(h=o(R)\), this cost is larger in order than \((s/R)^2\). A single pinned codimension-two tube has the smaller cost proved in (30).

**PROVED.** With planes pinned in all four directions, plaquettes cannot couple distinct complementary open cells. Their bases in one plaquette differ by at most one in each coordinate, whereas distinct open cells are separated by a pinned layer. Conditional factorization over cells and its global wall comparison were proved for thinner tangential wall sets in [the earlier wall calculation](gap-solve24-astra62.md), (1)–(2). Here (33) allows a direct bound at fixed pin values on each inner box. With \(h\le s/2,\ b\ge s\) the conditional variance coefficient in (33) is at least \(((s-h+1)/s)^4\ge1/16\), uniformly in \(\beta\).

**PROVED.** To see the coefficient, fix the collar too and decompose \(f\) into its orthogonal product components over the remaining trimmed cells. Explicitly for a subset \(J\) the component uses \(1-P_i\) on cells \(i\in J\) and \(P_i\) on the others, where \(P_i\) averages just that cell. These projections commute. For a small cube its integrated update variance dominates the variance of resampling all the cells wholly contained in it. The latter counts the squared component for \(J\) once whenever it meets at least one cell of \(J\). Each nonempty \(J\) contains a cell fitting inside at least \((s-h+1)^4\) enlarged-patch updates. Sum over these updates and integrate the collar back out, which can only increase the update variances. This proves the asserted coefficient. In this dense-grid regime every side-\(s\) cube meets the pins. There are no uncut origins to use in (3). At larger spacings (34) quantifies the cost of this same geometric decoupling.

## The interior estimate still needed

**PROVED.** There is an equivalent integrated-correlation target for the local step. At a fixed accepted exterior and pins, use the positive conditional generator \(\mathcal L=\widehat L_z\) from (33) and \(Q=Q_z^\circ\). On the whole conditional \(L^2\) space, or any common reducing subspace, the least constant \(C_{\rm loc}\) in \(\|Qf\|^2\le C_{\rm loc}\langle f,\mathcal Lf\rangle\) satisfies
\[
 C_{\rm loc}=
  \sup_{\substack{g=Qg\\\|g\|=1}}
          \int_0^\infty \|e^{-u\mathcal L/2}g\|^2\,du .                \tag{35}
\]
Take the supremum to be zero if \(Q=0\) and allow infinity. Indeed \(\|Qf\|^2=\sup_{g=Qg,\|g\|=1}|\langle g,f\rangle|^2\). With denominator \(\langle f,(\mathcal L+\epsilon) f\rangle\), the supremum over \(f\) at fixed \(g\) is \(\langle g,(\mathcal L+\epsilon)^{-1}g\rangle\), by Cauchy–Schwarz with equality at the resolvent vector. Both suprema commute. Letting \(\epsilon\downarrow0\) and using the scalar Laplace integral on the spectrum gives (35). Here \(g=Qg\) means the reading has zero mean after the whole inner exterior and the pins are observed. Time \(u\) is Wilson heat-bath time in a finite conditional box.

**PROVED.** Thus even a summable power tail in this time would suffice with the right prefactor. For instance, for \(T>0,\ \delta>0\), suppose every unit \(g=Qg\) obeys \(\|e^{-2^jT\mathcal L/2}g\|^2\le A_0\,2^{-(1+\delta)j}\) for every \(j\ge0\). Monotonicity gives \(C_{\rm loc}\le T[1+A_0/(1-2^{-\delta})]\) by integrating over the dyadic intervals. On the accepted exteriors in (16) or (30) an upper bound strictly below \((R/s)^2/C_*\) would give the stated physical-scale stochastic estimate. A one-time bound of fixed size does not control this integral for a general positive generator. On a two-dimensional centered space take eigenvalues \(1,\varepsilon\), let \(Q\) project on \(g=(\sqrt{1-\eta^2},\eta)\), and fix \(0<\eta<1\). Its time-\(T\) squared norm is at most \(e^{-T}+\eta^2\), while its integral is \(1-\eta^2+\eta^2/\varepsilon\). It diverges as \(\varepsilon\downarrow0\). This example identifies what a finite-time smoothing argument would still have to control.

**OPEN.** For the actual four-dimensional Wilson conditional filling, (17) and (33) bound the integrated correlation by \(2^8e^{440\beta t^3}\) on the stated dyadic boxes. The physical argument needs it bounded by a small fixed multiple of \((R/s)^2\) on boxes with \(aR\) finite and positive. The marked plaquette estimates prove (28), (31) and (32), which control specific exterior events and readings. I have no estimate at that order for the supremum over all interior readings in (35). In particular the sine-weight comparison alone gives no positive uniform physical threshold.

**OPEN.** Even conditional on that stochastic estimate, the Jaffe–Witten problem requires construction of a nontrivial continuum theory on four-dimensional Euclidean space with the Yang–Mills observables and the required axioms. The continuum implication used at (16) depends on convergence, matching and density on the full physical space. The earlier row 1254 is a research comparison and is unchecked at this pin. No construction or independent check of the present note is supplied here.

RESULT — OPEN. The four-dimensional SU(2) Yang–Mills mass gap in the sense of Jaffe and Witten remains unproved. Equations (15), (30) and (35) give a sufficient conditional Wilson estimate at inverse-square scale. The finite-volume bound obtained for it is (17). The weak-curvature slow sheets in (20) and (25) lose their centered variance in the full law by (31)–(32). This research result grants no status.
