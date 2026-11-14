# Support envelope — queue row 88
Provenance: OpenAI Codex, GPT-6 family (exact backend model and actual effort not exposed; row 88 requests max); current resumption at `d120883ea20edcbd9ac7a1e676a2ef8bfccb4237`, preserving Sections 1–13 from the earlier runs at `bb7f39d69e3410da4e450f04e2331f031cc6f2a1` and `259167dd570555bbce1b3e8ad219b5787a40f3e0`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, grants no status.

**Outcome: REFUTED for the literal target covering every actual joined datum, including artificial level-zero bonds in the old floor.** Sections 20–22 give the configuration: an exactly flat incoming history reaches the main operation; its stated reference law draws a nonzero coarse plaquette; a cube localization in the final island decision copies that plaquette onto a level-zero determining plaquette in the old floor. Its holonomy stays fixed while \(R_0^2\varepsilon_0\) tends to zero. The argument concerns the operation on its declared real domain; it does not construct the background maps themselves. It does not refute an envelope restricted to surviving physical determining bonds. Section 23 gives the distinction and a direct admission repair. Sections 1–13 are retained; Section 19 is a superseded checkpoint.

## 1. Question and source boundary

This attacks Package C rank 1, the support hypothesis (D-F) used by conditional floor screening, and hence the heavy-wall reversal test in `route-decisions.md` §4.3. The question concerns the **actual joined datum** read by each stage of the operation R, including reconstructed level-zero pivots, substituted seam bonds and previously lifted collars. A proof would supply that support hypothesis; an admitted counterexample would require changing the formation or operation rules before using screening.

Credit for the [outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), its tests, histories, region construction and background conventions belongs to **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**. Below, “SA n–m” means lines n–m of their `YM4_sketch_500.tex` at the commit above, fetched once to `/tmp/sa_ym4.tex`. The starting correction is `gates/floor-screen-gate.md` §2; `library/floor-screen.md` §§1–4 supplies the intended consumer. The existing large-field literature record is reused. Only bounded excerpts are read. No numerical or computer-assisted inference is a proof step.

## 2. What must be checked before claiming a counterexample

A coarse plaquette equal to 1 together with an independently assigned fine-side factor equal to −1 does not suffice: the fine-side factor may be fixed by a surviving averaging constraint. Likewise a rough bare bond outside the determining set says nothing about (D-F). An example must identify its determining plaquette, the recorded test outcomes, the reconstruction constraints and the stage of R at which the actual datum is read. Conversely, regularity of an independently imposed evaluation fibre is not a proof of regularity on the original support.

## 3. The original seam: an exact obstruction to the proposed example

SA 9607–9625 defines regularity by mixed **plaquette products**, not by the distance of an individual bond from 1. A large individual bond can be pure gauge. The inward bonds are omitted at every level; the extra pinch tests for the alternative convention are not part of this problem.

For an ordinary step, SA 17528–17532 explicitly stores the field on the complement of the next region **together with its averaging constraint**. SA 17341 and 17526 reconstruct any pivot used by the retained tests by solving that same constraint. Thus, for an unmodified seam at level l, its fine-side coarse bonds b satisfy

\[
\mathcal M(V_{l-1})(b)=V_l(b).                         \tag{3.1}
\]

Here the V on the left is the reconstructed physical field. After the strip substitution it is the expression on SA 17523, not the new free coordinate W′ alone. Pulling an equation back by a change of coordinates preserves the equation. On an exterior row it is retained by the delta function; on an eliminated row it holds by the definition of the reconstructed pivot. These are the two cases, not an independent assignment of that pivot.

Write an oriented mixed test as H₁H₂H₃H₄, using inverses when a plaquette edge has opposite orientation. Substitute (3.1) on each fine-side edge. Each of its four factors is now exactly the corresponding factor of the full coarse plaquette of V_l, in the same order and frame. Consequently

\[
\partial\mathbf V(\tau)=\partial V_l(p).              \tag{3.2}
\]

This proves the seam identification for the ordinary stored step. If the coarse factors are all 1, no fine-side factor can independently be −1. It does **not** prove that the coarse plaquette was tested, or that (3.1) survives a main-step deletion followed by a reference-law draw. Those are different questions. SA 17416–17422 removes the old determining layers inside healed components and islands, so their old stored variables cannot simply be combined with the newly drawn coarse field as if both remained in the same determining set.

For later use, the elementary comparison valid for four unitary factors is

\[
\|U_1U_2U_3U_4-W_1W_2W_3W_4\|
 \le\sum_{a=1}^4\|U_a-W_a\|.                         \tag{3.3}
\]

Indeed, insert the four intermediate products which successively replace U₁, U₂, U₃, U₄ by W₁, W₂, W₃, W₄, subtract consecutive products and use invariance of the operator norm under unitary multiplication. Also \(\|U^{-1}-W^{-1}\|=\|U-W\|\). Thus bounds by h on **all four reconstructed bonds** and by u on the reference plaquette imply u+4h. A nonpivot estimate alone is insufficient for this last application.

## 4. A distant pivot cannot hide behind small nonpivot tests

The following finite statement is proved here, including the nonanalytic branches of the averaging map. It addresses an actual possible loophole in SA 17341; it does not assume that all solutions of an averaging constraint belong to its local chart.

**Pivot lemma.** Fix odd L. There are positive constants κ_L, h_L, C_L with the following property. Let W be a real field on the double block of a coarse bond c, with all its plaquettes within κ_L of 1. Let V agree with W to within h ≤ h_L on every nonpivot bond read by that row. Suppose

\[
\mathcal M(V)(c)=\mathcal M(W)(c).                    \tag{4.1}
\]

Then its middle crossing pivot satisfies
\(\|V(b_0(c))-W(b_0(c))\|\le C_Lh\).
The assertion concerns the full map of SA 7065–7073, including its two Borel fallback rules. There is only one coarse pivot in the row's support (SA 8167–8175).

**Proof, first the global exclusion near the flat field.** Give SU(2) its bi-invariant angular distance d, so
\[
d(e^{i\theta n\cdot\sigma},1)=|\theta|\quad(0\le|\theta|\le\pi),
\qquad \tfrac2\pi d(G,1)\le\|G-1\|\le d(G,1).
\]
The triangle inequality follows by viewing SU(2) as the unit three-sphere with its great-circle distance; left and right multiplication are orthogonal maps of that sphere. Consequently a product of N factors each within angular distance a of 1 has distance at most Na.

Temporarily suppose that every nonpivot is within angular distance a of 1 and that \(d(\mathcal M(V)(c),1)\le b\). Put P = V(b₀(c)) and w = L⁻³. Internal contour paths never use P. They have length at most 2L, hence their transports have angular distance at most 2La from 1. Their implicit mean also has distance at most C_La: in logarithms its equation is
\(Z=\overline X+O((\max|X|+|Z|)^2)\); the convergent exponential and logarithm series make this a contraction on \(|Z|\le2\max|X|\) once a is small. This argument works uniformly over the at most 24 paths.

Exactly L of the L⁴ straight segments used in the row contain P: their three transverse coordinates are zero, and their longitudinal starting coordinate is arbitrary. Write E = K_La, increasing the finite constant K_L to cover every path length and every contour mean just described. In either exponential-logarithm rule for the row, a fraction w of the closed transports is within E of 1; every other closed transport is within E of P⁻¹. Also \(d(V[c],P)\le La\). The second rule averages over internal paths as well, but does not change the fraction w. In the first rule the closed transports use their contour means; the same estimates apply.

Write the row as \(e^Z V[c]\), with Z the arithmetic mean of the intrinsic logarithms of these closed transports. The intrinsic logarithm of an SU(2) element other than −1 has norm at most π. Therefore
\[
|Z|\le(1-w)\pi+wE,
\qquad
d(P,1)\le(1-w)\pi+wE+La+b.                           \tag{4.2}
\]
Choose a and b so that \(wE+La+b\le\pi w/4\) and \(E\le\pi w/4\). Equation (4.2) puts P at angular distance at least 3πw/4 from −1. Each off-pivot closed transport is consequently at distance at least πw/2 from −1. On this fixed compact subset the intrinsic logarithm has a finite Lipschitz constant D_L. This follows directly from
\(\log(\cos\theta+i\sin\theta\,n\cdot\sigma)=i\theta n\cdot\sigma\): its removable singularity at θ=0 has bounded derivatives, and θ stays below π by a fixed amount. Thus
\[
|Z+(1-w)\log P|\le \max\{1,D_L\}E.
\]
For anti-Hermitian X,Y, integrating the derivative of \(e^{(1-t)X}e^{tY}\) gives \(\|e^X-e^Y\|\le\|X-Y\|\). It follows that
\[
\|e^{w\log P}-1\|\le b+La+\max\{1,D_L\}E.
\]
The angular comparison above, applied to w log P, proves
\[
d(P,1)\le C_L(a+b).                                 \tag{4.3}
\]
There is no omitted singular case: in the third rule the average is V[c] itself, so triangle inequality gives \(d(P,1)\le La+b\) directly. Thus (4.3) holds for every branch. In particular, all nonpivots equal to 1 and average equal to 1 force P=1. A distant solution cannot be added to the small solution.

**Proof, a regular reference and the relative estimate.** Choose a coordinate tree in the rectangular double block and put W in its tree gauge. Any remaining bond is a loop made from that bond and the two tree paths. Move the coordinate paths into one another by interchanging adjacent coordinate steps; each interchange contributes a conjugated elementary plaquette. The box has side at most 2L in each direction, so fewer than C L² interchanges suffice. Telescoping unitary products gives \(\|W(b)-1\|\le C L²\kappa_L\) on every bond. Apply this same gauge to V. Bond differences and (4.1) are unchanged in norm, and the coarse averages transform at the same endpoints. All nonpivot V's and the target \(\mathcal M(W)(c)\) are therefore within C_L(κ_L+h) of 1. Equation (4.3) puts the pivot there too. Choose κ_L and h_L small enough that **both full rows** lie in a fixed analytic coordinate ball.

For completeness, the needed local inverse estimate has no assumed inverse theorem. Write X for the Hermitian pivot logarithm and Y for the list of nonpivot logarithms. Let F(X,Y) be the Hermitian logarithm of the row average. The contour contraction just used, and the convergent matrix series, make F continuously differentiable on a fixed ball. At zero its pivot derivative is w times the identity: each of the L straight segments containing the pivot contributes L⁻⁴, and the two internal-contour terms contain no pivot. This also rederives SA (QC16). Shrink the ball until
\[
\|D_XF-wI\|\le w/4,
\qquad \|D_YF\|_{\ell^\infty\to\mathrm{op}}\le K'_L.
\]
These choices exist by continuity on the closure of a smaller finite-dimensional ball. Use (4.1), integrate the derivative on the straight coordinate segment from (X₀,Y₀) to (X,Y), and separate its pivot part:
\[
w\|X-X_0\|\le(w/4)\|X-X_0\|+K'_L\|Y-Y_0\|_\infty.
\]
The logarithm is Lipschitz on the chosen ball, so \(\|Y-Y_0\|_\infty\le C_Lh\). Absorb the first term and use the exponential inequality once more. This proves the lemma. Every constant was chosen after L and before h; no enumeration or numerical evaluation enters. ∎

**Level-zero consequence, with its precise coverage hypothesis.** Suppose a plaquette p lies in a passed level-one test cube, its comparison field W has \(\|\partial W(p)-1\|\le u\), and the approximate test compares every nonpivot read by the four pivot rows meeting p with this **same W**, to within 2δ₀. Require (4.1) on those rows, including rows with reconstructed pivots, and require W to be κ_L-regular there. Then the lemma and (3.3) give
\[
\|\partial V_0(p)-1\|\le u+8\max\{1,C_L\}\delta_0.   \tag{4.4}
\]
If \(u\le C\varepsilon_1\), this is C′ε₀. Indeed \(|\theta_0-\theta_1|\le\bar B\); for sufficiently large θ₀ the ratio θ₁/θ₀ lies between 1/2 and 2, and their logarithms have a fixed bounded ratio, giving ε₁ ≤ Cε₀ directly from SA 6029–6033. Also δ₀=(A₁/A₀)ε₀. The sharper u ≤ Cε₁/L² of the gate is more than this crude envelope needs. This closes the pivot algebra; it does not supply the stated coverage hypothesis.

**Persistence at level zero, before artificial localization.** Under the literal region updates of SA 17416–17429, no later operation creates a new physical Γ₀ bond. An eligible operation has bottom at least 1 (SA 17575). A partial stage changes only Ω_l with l greater than that bottom, hence neither Ω₀ nor Ω₁. Healing and island formation replace both Ω₀ and Ω₁ by their union with X. A new Γ₀ bond has both endpoints outside Ω₁∪X and lies in Ω₀∪X, so it was already in Γ₀. The regions are aligned unions of cells, so a bare bond with both endpoints outside X cannot cross through a cell of X. Ordinary later steps leave the two old members alone. This proves the inclusion at each move and hence by induction through the history.

On those surviving bonds, a later move either carries the old bare field, changes coordinates for it, or acts by a simultaneous gauge transformation. The first preserves the value, the second preserves its physical value, and the third conjugates a plaquette holonomy. The core is not unfolded by the stages (SA 17598); a main move which removes it from the determining set cannot furnish a new Γ₀ test there. Thus a bound proved on the original physical Γ₀ plaquettes persists. This sharply locates the remaining level-zero issue: the initial read coverage in (4.4), and genuinely **new artificial collar bonds**, not an arbitrary late reassignment of an old bare bond. This argument does not identify the latter artificial bonds with old physical Γ₀ bonds.

## 5. The averaging estimate needed after a passed plaquette test

Here is a hand derivation of the real converse estimate used in `floor-screen.md`, rather than treating SA 9667 as a discharge. All the plaquettes in the averaging rows' full underlying blocks must satisfy the input bound.

**One step.** For fixed L there are a_L,K_L>0 such that a real field with plaquettes of norm at most a≤a_L on those blocks satisfies
\[
\|\partial\mathcal M(W)(p)-1\|\le L^2a+K_La^2.       \tag{5.1}
\]
To prove it, put W in coordinate-tree gauge on the rectangle containing the four blocks under p. The interchange argument of §4 makes every bond logarithm A bounded by C_La. The matrix power series and the contour contraction then give the following first-order expression for the row logarithm:
\[
(QA)_\mu(y)=\sigma(y)+L^{-4}\sum_{z\in B(0)}
 \sum_{r=0}^{L-1}A_\mu(y+z+r e_\mu)-\sigma(y+Le_\mu),
\]
where σ is the arithmetic average of internal contour sums. The remainder is at most C_La²: the map is analytic on a fixed finite-dimensional ball and its second derivative is bounded on a smaller closed ball, so Taylor's integral remainder gives this bound. The same observation applies to the logarithm of the plaquette product. In its oriented sum the four σ terms cancel. The remaining expression is exactly
\[
L^{-4}\sum_{z\in B(0)}\sum_{r,s=0}^{L-1}
 (dA)_{\mu\nu}(y+z+r e_\mu+s e_\nu).                \tag{5.2}
\]
Indeed the sum in r,s telescopes first in each direction to the four length-L side sums. There are L² terms for each z and all weights in (5.2) are nonnegative. The elementary plaquette expansion gives
\(\|dA\|\le a+C_La^2\): its logarithm differs from dA by a quadratic remainder, while \(\|\log G\|\le\|G-1\|+C\|G-1\|^2\) near 1. Hence the plaquette logarithm of the average is bounded by L²a+C_La². Since it is anti-Hermitian, its exponential differs from 1 by at most its norm. This proves (5.1), including its leading coefficient L². All constants are fixed finite-dimensional bounds, not evaluated by computation.

**Iteration without a constant raised to the depth.** Suppose the bare bound is εL⁻²ʲ on all underlying blocks. Let a_n bound the curvature after n averages. Induction using (5.1) gives
\[
a_n\le\varepsilon L^{2(n-j)}
 \exp\!\left((K_L/L^2)\sum_{r<n}a_r\right).
\]
Assuming the asserted estimate a_r≤2εL^{2(r−j)} at previous indices, the sum is at most 2ε/(L²−1). Choose ε so that
\[
\exp\!\left(2K_L\varepsilon/[L^2(L^2-1)]\right)\le2,
\qquad 2\varepsilon/L^2\le a_L.
\]
The first condition closes the induction, and the second permits every one-step application before n=j. Thus
\[
a_n\le2\varepsilon L^{2(n-j)}\quad(0\le n\le j).     \tag{5.3}
\]
This proves the depth-independent bound for a uniform layer. For a seam at level j, suppose its full bare support lies in layers of index at least j−1, on which the reference field obeys the same radius ε. Its bare curvature is then at most εL⁻²⁽ʲ⁻¹⁾. Apply (5.3) with ε replaced by L²ε to obtain 2L²ε for the full j-th average. With the exact identities (3.1), this is the bound for the mixed test. No inward-bond variant is used. The usual gap larger than 3L in level-(j−1) units suffices for the support inclusion: the four centered coarse blocks lie within three level-j spacings of the seam, as in the repair of Lemma G in the starting gate.

The outstanding question here is therefore coverage by a passed test with the requisite full support, not the real averaging inequality itself.

## 6. What a collar lift preserves, and which level it reads

The lift in SA 9776–9783 is exact duplication, not smoothing: internal bonds are 1 and crossing bonds carry the corresponding coarse value. Its elementary plaquette is either 1 or a coarse plaquette, up to orientation and basepoint conjugation. To verify this, project the four corners to their coarse blocks. If neither coordinate crosses a block boundary the four factors are 1. If only one crosses, the two crossing factors are inverse to each other. If both cross, the four projected corners are those of a coarse plaquette and the product is its ordered holonomy. Nested centered blocks ensure that every lower-scale block lies in one source-scale block, so the same argument works at every finer lattice.

On a double block entirely inside the lifting collar, internal contour paths stay in a single source block. Each straight transport crossing a source face is the same coarse bond, independently of its transverse position. Thus each closed logarithm in that averaging row is zero and the average is again the lift. This proves the identities needed for a **pure lifting collar**, including its seam substitution factors. It does not establish that an old/new join falls entirely in such a collar; that is the geometric condition in SA 9783.

In particular a lifted test whose source has level j inherits the source bound C R_j²ε_j. One cannot replace j by its new geometric level q<j without another argument. For example, take a coarse field equal to 1 except for a bond with value exp(itσ₃), 0<t<π/4. A lifted fine plaquette crossing the two relevant coarse faces has exactly the holonomy exp(±itσ₃), at every lower scale at which those faces are resolved. It has no extra factor L⁻²⁽ʲ⁻q⁾. This is an exact datum-level example, **not an admitted history counterexample**.

Nor does the frame comparison run in the needed reverse direction. For a decreasing linear frame θ_i=T+b(j−i), with an admissible slope b>0 and fixed T, R_j²ε_j is fixed whereas
\[
R_0^2\varepsilon_0\le L^2 A_0(T+bj)^{-1/2}
 [\log(T+bj)]^{2r+\mathfrak p_0}\longrightarrow0.
\]
The limit follows by putting s=log(T+bj) and bounding a fixed power of s against e^{s/2} by its power series. The rounding and consecutive-drop conditions hold for sufficiently large T, since a bounded one-step change cannot cross two adjacent power-L thresholds of (log θ)^r. Thus source and geometric levels must be distinguished in any collar part of the support proof. The example shows the failure of a proposed inference, not that this source datum occurs at the problematic location of a history.

**The source-level variant suffices for the screening consumer.** This smaller implication can be closed. Replace the per-geometric-level bound for a floor test by
\[
\|\partial\mathbf V(\tau)-1\|\le C_*R_{b(\tau)}^2
 \varepsilon_{b(\tau)},\qquad b(\tau)\le m,           \tag{6.1}
\]
where b(τ) is an identified source level. Under the frame inequalities, for every b≤m and sufficiently large θ_m,
\[
R_b^2\varepsilon_b\le4L^2R_m^2\varepsilon_m.          \tag{6.2}
\]
Here is the complete scalar comparison. Set s=2r+𝔭₀ and f(x)=x⁻¹ᐟ²(log x)^s. Since \(f'/f=(s/\log x-1/2)/x\), f decreases above exp(2s). The frame gives θ_b≥θ_m−c₅. Rounding gives R_b≤L(log θ_b)^r, hence
\[
R_b^2\varepsilon_b\le L^2 A_0f(\theta_m-c_5)
 \le2L^2 A_0f(\theta_m)
\]
when θ_m≥2c₅: the square-root ratio is at most √2 and the logarithm ratio is at most one. Also min_{i≤m}θ_i≥θ_m−c₅. Choose θ_m so large that
\((\log(\theta_m-c_5)/\log\theta_m)^{2r}\ge1/2\), which is possible because the ratio tends to 1. Then R_m²ε_m≥A₀f(θ_m)/2, proving (6.2). This is the frame form of Lemma T in the starting gate.

Consequently (6.1) gives exactly the common floor amplitude 4L²C_*R_m²ε_m used in Theorem R of `floor-screen.md`. Its geometric distance estimate still uses the actual test support; no change of metric or of the floor is made. Every subsequent maximum and exponential-tail estimate in that conditional theorem uses only this common amplitude. Thus a source-level envelope supplies the same **conditional screening implication**. It does not prove (6.1) on histories, nor justify using an artificial collar's source level as its geometric distance level. If the strict per-level wording fails only because of collar relabeling, this is the smaller interface change to try before changing the averaging map or the operation.

## 7. The history step that remains unclosed

Three assertions still need a proof about the actual construction. None is supplied by defining the evaluation fibre to be regular.

1. **Complete read coverage.** For each determining test τ, identify a passed local test whose controlled plaquettes contain the full blocks needed in §5, or, at level zero, whose comparisons and constraints give all the hypotheses of (4.4). The width of the omitted older-region margin is not fixed by SA 17317. SA 6055–6077 explicitly makes the actual neighborhoods and enlargements formation data. The eight-cell, four-cell and two-cell expressions do not alone give the required inclusions. In particular a passed test somewhere near p is not the same as the passed test using the reference W in its pivot equations.
2. **Every stage and reference-law draw.** The original seam equations are written in §3. SA 17650–17654 also retains bare averaging integrals after a drop-out, which rules out declaring all its finer variables independent. Nevertheless, a proof must list the actual read rows after each completed stage, and after the main integration deletes constraints and draws a new coarse field. SA 17585–17630 describes the stage radii and SA 17656 the box minimum estimate. These descriptions are not a read-row induction. The estimate for the new reference field also requires the small exterior-data conclusion of Proposition 2.4; existence of a regular orbit at its fixed radius alone is weaker than the ε_k bound needed here.
3. **Previously formed collars.** On a pure collar §6 gives the exact identities. For an actual join one still has to show which old bonds remain, where its transition lies, and which source level pays for every test. For the floor consumer, one possible resolution is that all problematic new low-level collar tests miss the floor. That must be shown for the actual sequence after older operations as well as for the outer collar of the current component. Relabeling a source-level bound by its geometric level is invalid.

I also attacked two apparent shortcuts to a counterexample. Choosing an omitted margin wider than eight cells does not by itself make a bad coarse field admissible: earlier passed tests and the surviving delta constraints can still control it. Similarly, a freely specified nonzero collar plaquette is not an admissible history until a source field with that value, all earlier test outcomes, and its position in the new determining set have been exhibited. Neither shortcut establishes REFUTED. A single bond equal to −1 without a nontrivial test holonomy establishes nothing gauge invariant.

There is an exact reason not to infer the missing assertions from SA 17709, 17831 or 18149. SA 17709 asserts them on supports. SA 17831 and 18149 impose regularity on a different set, the evaluation fibre. SA 18194–18205 invokes the support estimate to show inclusion of later reads in that fibre. Reversing this implication would assume the inclusion being proved. Likewise the later typed-presentation definition says that formation and step closure are additional inputs (SA 6439–6447); it does not construct these missing neighborhoods.

## 8. A precise sufficient completion, not a verified property of SA

The algebra above gives the following conditional support theorem. It records exactly what a completion of the formation data must prove, and prevents an unspecified margin or an abstract regular evaluation fibre from serving as that proof.

For every test of every actual joined datum, supply a finite certificate ending in one of these sources:

* a passed plaquette test with its complete averaging footprint, to which §5 applies;
* a passed level-zero comparison with all four pivot rows, their averaging equations and the reference plaquette, to which §4 applies;
* a newly drawn or prepared field with a proved plaquette bound C₀R_b²ε_b at its birth level b, on the whole footprint, including its boundary.

Each intermediate arrow in a certificate must be an **exact identity of holonomies**, up to inversion or unitary conjugation: a surviving constraint as in (3.2), or the lift identity in §6. A coordinate change is read through its physical inverse expression. If a constraint is integrated out, its certificate is not carried forward unless the new determining set has removed the row or a new valid source replaces it. The certificate is acyclic and retains its terminal birth level b. Finally require, for a test whose claimed envelope uses level l,
\[
R_b^2\varepsilon_b\le K R_l^2\varepsilon_l,           \tag{8.1}
\]
with one K independent of the history, checked directly from the terminal source rather than multiplied along successive arrows.

**Conditional theorem, proved.** If all actual tests have these certificates, and the constants in their three kinds of source bounds are fixed, (D-F) holds with a fixed constant. Indeed §§4–5 bound each terminal source by C₁R_b²ε_b, enlarging C₁ once over the finitely many source types and using R_b≥1. Follow the certificate backwards. Inversion and unitary conjugation preserve distance from 1, and each other arrow is equality, so there is no multiplication of constants with the number of stages or collars. Apply (8.1) once at the terminal source. The result is C₁K R_l²ε_l for the actual mixed test. This proof covers every test, hence in particular all floor tests. ∎

To make this a definition-level repair, the places to change are the formation data at **SA 6055–6077**, the region/admission rule at **SA 17317–17323**, and admission of each new determining sequence in **SA 17575–17630**. They would have to exclude uncovered reads (including untested bands) and retain the source level of a lift. If a certificate fails, its component cannot proceed to the background call which uses it; the complementary branch must remain in the history. This is a proposed completion, **not shown to agree with the existing kernels**. In particular its extra failures have no proved rarity payment outside the old floor, and it has not repaired Package C as a whole. No claim is made that this change is necessary or minimal for the original outline: that would require the admitted counterexample which has not been constructed.

## 9. State at the budget boundary

The independent fine-side −1 assignment is excluded on the original seam by its retained constraint. The distant-pivot version is excluded by the global pivot lemma, including the Borel branches. The real converse averaging estimate is rebuilt, and exact lifts are tracked without inventing a scale gain. The source-level variant (6.1) is sufficient for the existing conditional floor-screening argument. These close specific algebraic substeps, not row 88.

The next decisive task is the read-by-read admission induction in §7: first supply the initial level-zero coverage, then identify the source of each actual joined test after a stage, a draw and an older collar. A counterexample must violate that induction while satisfying the actual recorded tests and constraints; the datum-only example in §6 does not do so. Until that task is closed, retain (D-F) as an input to screening and retain the heavy-wall reversal test. No change to the route decision or scientific status is warranted by this report.

## 10. Resumption: the admission boundary

The resumed task is still Package C rank 1 and its heavy-wall reversal test. A successful induction supplies (D-F); an admitted failure requires changing the rule that admits the offending read. The outline is again fetched once at the specified commit. Its constructions are credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. The following sections separate literal recorded admission rules from assertions of regularity made later in their outline. Neither the latter assertions nor a regular evaluation fibre is used as a premise for the support theorem.

### 10.1 The initial strip: the old-region margin is not the issue here

At the first step the old live region is empty. Put \(D=\Omega _1^c\). In the cell adjacency graph, write \(N_r E\) for the union of cells at graph distance at most \(r\) from \(E\). SA 17317–17323 gives
\[
D=N_2(Q'_1)\cup N_4(P'_1),\qquad
\Omega _0=N_1(\Omega _1).
\]
Here and below boundary sites are assigned using the fixed half-open convention; estimates involving physical distances allow one lattice spacing at either end. A cell \(C\) in \(\Omega _0\cap D\) has a neighbor \(C'\) in \(\Omega _1\). Since \(C'\notin N_2(Q'_1)\cup N_4(P'_1)\), triangle inequality in the adjacency graph gives
\[
\operatorname{dist}(C,Q'_1)\ge2,\qquad
\operatorname{dist}(C,P'_1)\ge4.                 \tag{10.1}
\]
For a cell in \(\Omega _1\), the stronger bounds are 3 and 5. Thus the original level-zero determining strip contains no failed approximate-test cube and no failed plaquette-test cube; there is a full cell of clearance to the former and three to the latter. A plaquette crossing two cells loses at most one bare spacing in the physical clearance, not a cell. This closes the cell-level exclusion at the initial strip. It does not use an unspecified margin of an older region.

For clarity about its limit, (10.1) is not yet the coverage hypothesis of (4.4). For a plaquette \(p\), let \(E(p)\) be its four bonds together with the complete double blocks of the averaging rows whose pivots occur among those bonds. A double block has side at most \(2L\) in bare units; consequently \(E(p)\) lies within \(4L\) of \(p\). A passed approximate test comparing **all of** \(E(p)\) with one \(U_{1,\square}\), and a passed curvature test for that same field on \(p\), finish the proof by (4.4). The ratio of the step cell size to the test cube size provides ample room: the cell side is \(MR_1L\), whereas SA 17334 makes the test side of order \(M_2R_1L\), with \(L^2M_2\le M\). But the actual enlargement and which plaquettes the curvature indicator examines must still be specified. “The reference is regular at its fixed defining radius” supplies the chart hypothesis of the pivot lemma; it does **not** supply the shrinking bound \(u=O(\varepsilon _1)\) in (4.4).

This distinction matters at a boundary of two test cubes. Choosing a passing approximate test whose doubled cube contains \(E(p)\) is insufficient if the curvature test of that reference is only known on a different central cube. The same reference and its tested plaquette set, rather than only the names of neighboring passing tests, are the remaining initial-level read. SA 6055–6077 assigns precisely these neighborhoods to formation data, without specifying them in the cited rules. This observation is not a counterexample.

### 10.2 What actually survives a draw

The later measure description makes the changed bond set explicit. At SA 22749 it is
\[
\mathfrak b_X=\{b\text{ of level }k:
                 b\text{ has an endpoint in }\Lambda^{\rm pr}\}.
                                                        \tag{10.2}
\]
It includes boundary-crossing bonds, and every endpoint lies in \(X\). An exterior datum cannot be joined to a newly drawn interior by keeping an old equality on a row in \(\mathfrak b_X\) merely because that equality held before deletion. For a healed component or an island, SA 17416–17420 removes the lower determining layers throughout \(X\). Thus such a row has no old fine-side determining factor left there. At the next ordinary step, the new coarse field is defined to be the average of the new fine field (SA 22748), which supplies the new seam equality. For a drop-out, SA 17654 instead retains the bare averaging integrals of the completed stages. The two cases cannot be combined into a freely chosen old fine factor and a freely chosen new coarse factor on one retained seam.

There is also a useful exact estimate for an actual draw. Suppose its centre \(V_\Lambda\) has plaquettes bounded by \(u\) on every plaquette meeting \(\mathfrak b_X\), and the reference-law cut-off bounds \(\|\log(V_kV_\Lambda^{-1})(b)\|\) by \(h=M_0\varepsilon_k\) on **every changed bond**. Extend the quotient by 1 on unchanged bonds. The inequality \(\|e^{iA}-1\|\le\|A\|\) and (3.3) give, including plaquettes crossing the box boundary,
\[
\|\partial V_k(p)-1\|\le u+4M_0\varepsilon_k.       \tag{10.3}
\]
The tree gauge does not alter this estimate: it compares fields in the same gauge and the plaquette norm is gauge invariant. In particular a bound \(u\le C_0R_k^2\varepsilon_k\) is sufficient; the stronger \(u=O(\varepsilon_k)\) is not needed for (D-F). Proposition 2.4 would supply such a bound from an exterior estimate of that size, but its small-data conclusion is an analytic input, not an admission rule or a consequence of the fixed radius \(a_\Lambda\).

The boundary scope of the cut-off in SA 17604 must follow (10.2). Interpreting “bonds of the box” as only bonds with **both** endpoints inside would not prove (10.3); an unbounded changed crossing bond is then an immediate obstruction. That alternative reading is not asserted to be the intended kernel, and no counterexample is claimed from this terminology alone. The original source explicitly changes the incident bonds in (10.2).

## 11. The stage thresholds do fit the proposed envelope

The threshold factors in SA 17624 can be bounded without multiplying a loss at each of the \(R_k\) stages. This closes a scalar part of the admission question; it does not determine which plaquettes those tests read. All constants in this section are chosen from the fixed frame constants, \(L,r,\mathfrak p_0\), before the coupling ceiling. SA 19410 specifies that these tests use the frame \(\theta\); no equality of \(\theta\) and the action weights \(x\) is assumed here.

Write \(b=k-R_k\ge1\) and \(T=\theta_k\). For \(b\le i\le k\), the frame inequalities give
\[
T-c_5\le\theta_i\le T+\bar B R_k,
\qquad R_k\le L(\log T)^r.                         \tag{11.1}
\]
Indeed the running minimum defining \(R_k\) is at most \(T\). Choose \(T\) large enough that \(c_5+\bar B L(\log T)^r\le T/2\) and \(\log(T/2)\ge\frac12\log T\). The first choice exists because \((\log T)^r/T\to0\): with \(s=\log T\) and integer \(n>r\), use \(e^{s/2}\ge(s/2)^n/n!\). Thus all \(\theta_i\) are in \([T/2,3T/2]\), and direct substitution in \(\varepsilon_i=A_0\theta_i^{-1/2}(\log\theta_i)^{\mathfrak p_0}\) gives one constant \(K\) with
\[
K^{-1}\varepsilon_k\le\varepsilon_i\le K\varepsilon_k.
                                                        \tag{11.2}
\]
For example \(K=2^{\mathfrak p_0+1}\) suffices after making the logarithms comparable by a factor two.

There is also at most one rounding step between the radii in this window:
\[
R_k\le R_i\le LR_k.                                \tag{11.3}
\]
The lower bound is monotonicity of the running minimum. For the upper bound, its value at \(i\) is at most \(\theta_i\le T+\bar B L(\log T)^r\), and its value at \(k\) is at least \(T-c_5\). Increase \(T\) so that
\[
\left[\frac{\log(T+\bar B L(\log T)^r)}
                 {\log(T-c_5)}\right]^r<L.
\]
The ratio tends to 1 by (11.1). The unrounded radius at \(i\) is then less than \(LR_k\); since \(LR_k\) itself is a power of \(L\), upward rounding proves (11.3).

Put \(j_0=k_\sharp+1\), the last index with \(L^{k-j_0}=R_{j_0}\) in SA 17624. It exists within \([b,k]\). In fact \(F(i)=L^iR_i\) takes power-of-\(L\) values and each increment either preserves it or multiplies it by \(L\), because \(R_i/R_{i+1}\in\{1,L\}\). For \(R_k\ge3\), (11.3) gives
\[
F(b)\le L^{k-R_k}LR_k\le L^k,
\qquad F(k)\ge L^k.
\]
It therefore cannot jump over \(L^k\). The elementary inequality \(LR\le L^R\) for integers \(R\ge3\), \(L\ge2\), follows from \(R\le2^{R-1}\), proved by induction. This justifies the preceding comparison without a computation.

On shell \(i\), the overlap multiplier obeys
\[
L_\flat^{2(i-j_0)_+}
 \le L^{2(k-j_0)}=R_{j_0}^{2}
 \le L^2R_k^2\le L^2R_i^2.                        \tag{11.4}
\]
Hence the stated shell threshold is at most \(L^2R_i^2\varepsilon_i\eta_i^2\). The factors \(1-\beta_{\rm s}(1-2^{-a})\) are at most 1 and need no accumulation estimate for this direction of implication.

In the remaining tested region at stage \(j\), the threshold is at most \(3L_\flat^{2e}\varepsilon_j\eta_j^2\). On a layer \(l\le j\), the displayed cases in SA 17624 give \(e\le j-l\): above \(j_0\) this is \((j-l-1)_+\), below it the value \(j-j_0\) is no larger, and before overlaps it is zero. Since \(\eta_j=L^{-(j-l)}\eta_l\),
\[
3L_\flat^{2e}\varepsilon_j\eta_j^2
 \le3\varepsilon_j\eta_l^2
 \le3K^2\varepsilon_l\eta_l^2                     \tag{11.5}
\]
when \(b\le l\le j\). The last inequality uses (11.2) twice. Layers below \(b\) belong to the unprepared old core; (11.5) makes no assertion about a new test there.

Equations (11.4)–(11.5) show that the actual numerical thresholds are not a depth obstruction. For a determining plaquette whose **whole averaging footprint** is controlled by one of these passed curvature tests, Section 5 converts these bare curvature bounds into the datum bound, with fixed one-step factors at a seam. Neither (11.4) nor (11.5) asserts that every new row has such a footprint. In particular they cannot be applied to an untested part of the old core or to the artificial outside collar.

## 12. The current outer collar misses the floor; an old read is different

Here the explicit free-evolution geometry supplies an inclusion which cannot be read from separation alone. Let \(X\) be a class component of an operation at level \(k\), and let \(s_k=MR_k\xi_k\). SA 17575–17583 gives, with the same concentric hull \(H_k\),
\[
X=H_k^{[10]},\qquad \Omega_k^c\cap X=H_k^{[8]}.
                                                        \tag{12.1}
\]
Consequently the inside of \(\partial X\) is separated from \(\Omega_k^c\cap X\) by two level-\(k\) cells. Only this inside clearance is needed to exclude the floor, since the floor is a subset of \(X\).

Suppose the actual outer localization collar has width at most \(c_{\rm col}M\xi_k\), on either side of \(\partial X\); this includes the one-\(M\)-cube enlargement specified in SA 17357. The fixed number \(c_{\rm col}\) must be supplied by the localization rule. Enlarge this collar by \(3\xi_k\) to include the source plaquettes and their blocks in any lift test. Choose the coupling ceiling so that
\[
c_{\rm col}M+3<MR_k.                              \tag{12.2}
\]
The intersection of this enlarged collar with \(X\) then lies in the **original** \(\Omega_k\), by the two inside cells just proved. Nesting gives \(\Omega_k\subset\Omega_b\). The floor is contained in \(\Omega_b^c\cap X\); the portion of the footprint outside \(X\) cannot meet it either. Thus neither these collar tests nor their full source footprints meet the floor. This applies at every stage of this operation, since its outer component \(X\) is unchanged and the old core is not unfolded. This is an exclusion from the floor, not a proof of admission of the entire exterior collar in the presence of other components.

It follows that the bare-level plaquette obtained by copying a nonzero level-\(k\) curvature into this particular outer collar, as in Section 6, cannot furnish a counterexample to the floor hypothesis. It still shows why a claim about **all** joined tests at their new geometric levels is stronger than the floor hypothesis. No scale gain is introduced by (12.2).

This argument cannot be applied to an older localized read retained in a mark. An old component of level \(s<b\) can lie well inside the current floor. Its own outer collar was separated from its own floor, not from the later floor. The fact that the physical determining sequence does not explicitly store artificial lift bonds is insufficient: a retained test is a function, and evaluating that function can form its old local background and its collar again. To settle that case one must track the actual source field of the retained function, and either obtain the geometric-level bound or prove that only the source-level version of Section 6 is consumed. The disjoint waiting windows constrain operation levels; they do not change the elementary lift identity.

The attempted counterexample at this point is therefore quite specific: retain an old local read with a nonzero coarse source plaquette, put its artificial fine collar inside a later floor, and make the bare threshold much smaller by extending the initial history. What is missing is an explicit family of admitted histories realizing that source with a fixed positive size while all earlier tests and the later read remain supported. Continuity of a finite-depth background at the flat field does not suffice: its continuity neighborhood may depend on the depth being sent to infinity. Invoking the uniform background and locality assertions without their proofs would only turn this attempted counterexample into another conditional argument. No such invocation is made here.

## 13. Resumed stopping point

**STOPPED at budget, not PROVED or REFUTED.** The first unresolved read is still at the initial strip: identify the actual passing indicator whose reference field and tested plaquettes meet (4.4) on each complete pivot footprint. Equation (10.1) supplies clearance from failures, not that identification. For positive-level reads, the corresponding missing datum is the exact omitted older-region margin and the placement of each complete averaging footprint relative to it and to the stage tests.

The later parts now have sharper limits. The stage multipliers themselves are controlled by (11.4)–(11.5), so repeating a constant once per stage is unnecessary. A new draw needs the bound on its centre on all incident plaquettes; (10.3) then handles the entire changed bond set. The current outer lift cannot meet its own floor under (12.2). None of these facts supplies the old localized reads in a retained mark. In particular, the ordinary surviving seam equations and the reconstruction lemma cannot be applied to a newly formed artificial collar merely by reusing its geometric level.

The attempted independent seam assignment, distant pivot, uncut boundary-bond reading, current outer-collar wall and old-collar depth argument have not produced an admitted violating history. The first two are excluded as in Sections 3–4; the boundary-bond reading does not specify the actual draw; the current collar misses the floor; and the old-collar attempt lacks the uniform supported family described at the end of Section 12. This is a failed search, not an impossibility theorem.

No necessary or minimal change to the original definitions has therefore been established. The explicit certificate completion of Section 8 and the source-level consumer of Section 6 remain proved **conditional** implications, with their admission hypotheses unverified for the actual kernels. The added statements in this resumption do not close row 88, remove the heavy-wall reversal test or establish the support hypothesis of floor screening. The route decision and scientific status are unchanged.

## 14. Third run: what the long account actually specifies

The target remains the admission induction in Section 7, not a new screening estimate. Sources for this continuation are the [long account, raw I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex) and [raw II](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex), credited to **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**, and Tadeusz Bałaban, CMP **119** (1988), 243–285, Sections 2–3, and CMP **109** (1987), 249–301, Section 3. The source files were fetched once to the prescribed scratch paths; the papers are read in place. These are definition lookups, not imported proofs.

There is a material correction to the proposed starting premise. Raw I 28697–28700, item (sigma6), identifies the region-data margin with Balaban CMP 99, not with a newly specified Chapter 8 formation rule. It calls the margin a one-sided lower bound and explicitly says that satisfaction of it is unresolved and that it is not imposed. The preceding item (sigma4), raw I 28675–28691, likewise distinguishes the quantitative nest gap of CMP 96 from the weaker qualitative boundary separation used there. Thus (sigma6) cannot be inserted into Section 7 as a proved upper bound on the omitted testing margin. These are also different notions: a lower bound on a nest gap does not upper-bound the band on which no indicator is evaluated.

Chapter 8's local-run definition (raw II 102572–102622) fixes nested level cells and their images. Its label definition (102959–103025) fixes live and healed labels, seeds, inheritance under merging, and nesting until healing resets a region. The age definition (111791–111845) distinguishes territory age from seed age. Those definitions do not by themselves specify the plaquettes of a localized passing indicator. In particular, positive probability or an age estimate for a label cannot supply the pointwise test coverage required in (4.4).

### 14.1 The relevant omitted band is specified elsewhere

Balaban CMP 119, pp. 264–266, (3.2)–(3.5), supplies the ordinary-step rule: enclose the old live region in level-\(t\) cells, omit the plaquette decomposition on its four-layer enlargement, insert gauge fixing outside its five-layer enlargement, and perform the approximate fluctuation decomposition outside its six-layer enlargement. The exclusions due to failed new plaquette tests are respectively one and two layers for gauge fixing and approximate testing. The final new region excludes eight old-region layers, four failed-plaquette layers and two failed-approximate layers. These numbers concern the **current cell grid**, after enclosing the old region in those cells.

This lookup is also present in raw II 10283–10310: the eight layers are decomposed as \(4+1+1+2\). Chapter 8, raw II 79848–79886, explicitly takes its ordinary step from CMP 119 (3.1)–(3.5), including the approximate-test set \((\square^{\sim2})^{(k)*}\). This is the concrete ordinary-step convention used below. It is not a consequence of (sigma6). If the outline's independent formation data depart from this convention, the conclusion below requires the corresponding read-set inclusions to be stated anew.

The reference in the two indicators is the **same** localized background. CMP 119 (1.2), (1.4), (1.8) and (2.16)–(2.17) specify its tower on the fourfold enlarged test cube, its curvature test on the once-enlarged cube, and the nonpivot comparison on the twice-enlarged cube. Formula (3.4) takes the appropriate average of that background at later steps. Its top determining member contains the once-enlarged test cube and its adjacent unit blocks: the tower removes at most two \(M_1\)-layers from the fourfold enlargement, whereas the test cube has side of order \(M_2R_t\), with \(M_2=L^2M_1\). This is an elementary containment, with more than one full test-cube layer to spare. No estimate on an untested localized background is being substituted for a passed indicator.

CMP 109, Section 3, (3.18)–(3.27), constructs padded cubes and uses exact averages on their interior; its later analytic extensions have hypotheses on their fields. These are localization devices for action terms, not an extra passing indicator on an arbitrary large-field history. They do not enlarge the ordinary testing zone just identified.

## 15. Initial strip and ordinary original seams with those read sets

**Initial-strip statement (proved for the concrete rule in 14.1).** Every actual level-zero determining plaquette at the first step satisfies
\[
 \|\partial V_0(p)-1\|
 \le \varepsilon_1L^{-2}
       +8\max\{1,C_L\}\delta_0
 \le C'_L\varepsilon_0.                         \tag{15.1}
\]
All constants are fixed before the frame ceiling. Pivot bonds here are reconstructed physical bonds, not independently chosen coordinates.

**Proof.** Let \(s_1\) be the side of a level-one cell and \(a_1\) the side of a test cube in bare units. The compatible partitions give test cubes contained in cells. The scale choices give \(a_1\ll s_1\), and, by lowering the ceiling once, \(a_1>8L\). Choose a corner of \(p\), an incident cell \(C\subset\Omega_0\), and an incident test cube \(D\subset C\); use their closures if the corner is on a partition face. Every bond of \(p\), and every double block used by a pivot row of \(p\), lies within \(4L\) of that corner. Hence this entire footprint lies in \(D^{\sim}\), and therefore also in \(D^{\sim2}\).

The containing cell belongs to \(\Omega_0=N_1\Omega_1\). The clearance proof (10.1) puts it outside the failed-approximate hull and at least four cell steps from the failed-plaquette hull. Consequently the approximate test at \(D\) was performed: the excluded new-plaquette band has only two layers, and there is no older live region. It passed, since otherwise \(D\) would belong to \(Q_1\) and its cell to \(Q'_1\). The plaquette test at \(D\) was performed and passed for the same reason using \(P_1\). If the chosen cell is already in \(\Omega_1\), the clearances are larger. Half-open boundary assignments do not change these cell exclusions or the strict footprint inclusion.

Set \(W=U_{1,D}(V_1)\) in the representative used by the approximate test. The first passing indicator bounds \(\|\partial W-1\|\) by \(\varepsilon_1L^{-2}\) throughout \(D^{\sim}\); the second bounds every required nonpivot difference by \(2\delta_0\) throughout \(D^{\sim2}\). All pivot rows lie in the top determining part of this tower, by 14.1. Thus their reference averages equal \(V_1(c)\). The original delta constraints, or their pivot solutions, give precisely the same values for \(\mathcal M(V_0)(c)\). The hypotheses of the pivot lemma hold on each of these double blocks, once \(\varepsilon_1L^{-2}\le\kappa_L\) and \(2\delta_0\le h_L\). These are fixed ceilings, not assumptions about depth. Apply that lemma to each pivot and telescope the four plaquette factors as in (3.3). This proves the first inequality of (15.1). The adjacent-level frame comparison in Section 4 and \(\delta_0=(A_1/A_0)\varepsilon_0\) prove the second. ∎

This identifies the previously missing indicator: it is \(\chi_1(D)\), on \(D^{\sim}\), paired with \(\chi'_0(D)\), on \(D^{\sim2}\), with reference \(U_{1,D}\). It is not a curvature test of a neighboring cube with a different reference. The persistence argument in Section 4 then preserves (15.1) on original physical level-zero plaquettes which remain determining bonds.

**Positive-level ordinary read (proved for the same rule, before a preparation changes that read).** Let a mixed determining test have level \(t\ge1\), and first consider its birth in an ordinary step. It has an endpoint in \(\Omega_t\). Choose an incident cell contained in \(\Omega_t\) and an incident test cube \(D\) in that cell, again using closures at partition faces. The complete four-row averaging footprint lies within \(3\xi_t\) of the endpoint, hence in \(D^{\sim}\), after the same fixed ceiling makes the test side larger than \(8\xi_t\). The chosen cell lies outside the eight-layer enclosure of the older live region and the four-layer enclosure of \(P'_t\). Thus \(\chi_t(D)\) was performed outside the four-layer omitted band and passed. Its single reference \(U_{t,D}\) has the bound \(\varepsilon_tL^{-2t}\) on this full footprint, and its top constraints give \(\mathcal M^tU_{t,D}=V_t\) on the four coarse rows. The hand averaging estimate (5.3) bounds their plaquette product by \(2\varepsilon_t\). On a substituted fine-side row, the retained equation (3.1) replaces its factor by this same \(V_t\) factor. Hence the mixed product has the same bound. Using \(CL^2\varepsilon_t\) instead also covers the one-layer footprint convention of Section 5.

This argument carries unchanged through restrictions which preserve the old rows and their equations. It does not carry an eliminated constraint through a reference-law draw. Nor does it identify a new artificial level-zero lift with an old physical level-zero bond. Those are the remaining operations, not another missing ordinary testing margin.

## 16. A late creation can be realized with exactly flat curvature

The counterexample search must not assume that a large-field component requires a rough plaquette. Here is an exact way to generate the quiet component needed for that search. It realizes the geometry, but has no violating holonomy.

Choose a terminal level \(k\), put \(a=k-R_k\ge2\) and \(b=a-1\), and use the linear frame of Section 6. Choose a site \(z\) of level \(b\) strictly inside a level-\(a\) block, away from its pivot crossings. Place it far from the boundary of one level-\(a\) cell; the test-cube side is much smaller than the cell side. At level \(b\), let the gauge function \(u_b\) equal \(G\) at \(z\) and 1 elsewhere, where
\[
 G=\exp(i\vartheta\sigma_3),\qquad
 \vartheta=2\arcsin(3\delta_b/2),\qquad
 \|G-1\|=3\delta_b<\varepsilon_b.                 \tag{16.1}
\]
Here \(\delta_b<1/3\) and \(3A_1<A_0\); the latter is within the prescribed small-ratio choice. For \(i<b\), extend \(u_b\) to level \(i\) by taking its value at the containing level-\(b\) block centre. For \(i\ge a\), put \(u_i=1\). Set
\[
 V_i(x,y)=u_i(x)u_i(y)^{-1}.                     \tag{16.2}
\]
All plaquette products are exactly 1. Gauge covariance of the averaging map, applied to the identity field, gives \(\mathcal M(V_i)=V_{i+1}\) at every step. In particular the nontrivial gauge at \(z\) is invisible at level \(a\), since \(z\) is not a level-\(a\) top.

For \(i\le b\), the gauge on the finer lattice is constant inside every level-\(i\) block. Thus the flat representative of the local reference in block axial gauge agrees with \(V_{i-1}\). The plaquette and approximate tests pass, the fluctuation is zero, and the collar and rim tests pass. This uses only the source's flat-background convention (SA 9791: over the identity the background orbit is the orbit of absolute minima), transported by the prescribed nodal gauge. That orbit can be checked directly here: zero Wilson action forces every plaquette to be 1; on a box, path transport gives a gauge of the identity, and on the torus the coarse constraints fix the fundamental-cycle holonomies to 1. The prescribed determining transports fix that gauge at the nodes, leaving precisely the residual gauge freedom. No small-nonzero-background estimate is used.

At step \(a\), the reference of every new approximate test is the identity. All affected nonpivot bonds have deviation \(3\delta_b\), so the approximate tests whose twice-enlarged cubes contain such a bond fail strictly; all other approximate tests pass. The plaquette tests still pass. The failed cubes fit in one level-\(a\) cell by the placement of \(z\) and \(a_a\ll s_a\). Gauge-fixing cut-offs pass because of (16.1); their exponential factors are positive. The component thus created is a boxed enlargement of one cell. The fluctuation field on its outer strip is zero, so this step creates no additional collar or rim failure.

At all subsequent ordinary steps through \(k\), the fields at the newly tested levels are exactly 1. No new failure or merger occurs. The component follows the free evolution \(\Phi_i\). Its size in cells stays bounded: at a step without a radius drop, enclosing a box in the next grid divides its side by \(L\), up to two boundary cells, and the margin adds twenty cells. A radius drop replaces that division by no division; by (11.3) there is at most one such drop in this waiting window. Hence one fixed cell-side bound suffices throughout. The torus is chosen larger than these boxes and all their read neighborhoods. There is no earlier operation on this component: for \(i<k\), monotonicity gives \(i-R_i<k-R_k=a\), so its creation is still inside that earlier waiting window. At \(k\) it satisfies size, quiet and quarantine.

Thus arbitrarily late class components are compatible with the recorded indicators and exact averaging equations. All passing indicators have a strict margin; the failed approximate indicator also has a strict margin. The nontrivial gauge is retained in the old core, not hidden in an untested determining plaquette. Choosing the later shell variables at their flat values gives no new curvature. This construction supplies the late creation and wait; it supplies **no nonzero source plaquette for a collar**. Calling it a counterexample would confuse a large gauge-dependent fluctuation with a large datum holonomy.

## 17. The prepared-shell geometry and the limit of its tests

The long account gives more precise prepared regions in raw I 51707–51728 and 53737–53835 (Definition 4.18, prepared sequence). Write \(h=k-R_k\), and let \(j_0\) be the first scale of the compressed outer shells, the index called \(k_\sharp+1\) in Section 11. Below that index its rule is
\[
 Z''_j=(\Omega_j^{\sim5})^c\cap X\quad(h<j<j_0);
                                                        \tag{17.1}
\]
above it, the nested \(Z''_j\) are separated by a layer of \(M\)-cubes at the later scale. The original core \(Z_h\cap X\) is contained in all of them. These are the concrete prepared regions of the cited Balaban construction; neither the symbols \(Z''\) nor the word “prepared” alone supplies (17.1).

**A new physical row's footprint misses the old core.** At a scale governed by (17.1), quiet evolution gives \(\Omega_j^c\cap X=H_j^{[8]}\), where \(H_j\) contains \(Z_{j-1}\cap X\). Enlarging its complement by five cell layers leaves the box \(H_j^{[3]}\), with boundary assignments harmless if one keeps only two layers of clearance. Thus the boundary of \(Z''_j\) is separated from \(Z_h\cap X\) by at least two level-\(j\) cells. In the compressed part, the one-\(M\)-cube separation from \(Z''_{j-1}\) gives at least \(M\xi_j\) of clearance from the old core. At the crossover, the nested-box construction has the same gap. In either case a complete averaging footprint of radius at most \(3\xi_j\) cannot reach the core when \(M>4\).

A newly added physical row of level \(j\) is outside \(Z''_j\), so the same conclusion holds for its footprint. It also stays inside \(X\): a changed row was in an original \(\Omega_j^c\subset\Omega_k^c\), and \(\Omega_k^c\cap X=H_k^{[8]}\) has the two-cell outer clearance to \(X=H_k^{[10]}\). The footprint therefore lies in
\[
                     X\setminus Z_h\subset\Omega_h.       \tag{17.2}
\]
This is a geometric conclusion for new physical rows. It does not concern artificial low-level rows introduced at the outer boundary of a localization.

At a passed stage, the current shell indicator explicitly tests the stage background in this newly prepared region, with the shell and remaining-region thresholds of SA 17624. Where the entire averaging footprint belongs to that tested region, (11.4)–(11.5) and Section 5 give \(C_LR_j^2\varepsilon_j\) for the new row's plaquette test. The seam substitution is exact: on a full fine-side row made of determining bonds, \(V_{j-1}=\mathcal M^{j-1}\widehat U\); the semigroup identity gives \(\mathcal M(V_{j-1})=\mathcal M^j\widehat U\), the same field as on the coarse side. This does not use an averaging constraint which the main integration has already deleted.

There is an important boundary to that argument. The long account itself separates the present preparation from cells inherited from a previous arrested operation: raw I 68257–68378, Remark 4.21, says that the displayed regularity bounds do not cover the latter cells and uses an additional inherited-datum hypothesis instead. In particular, the present shell indicator is not a newly passed indicator on every old marked read. Applying it there would repeat the unproved induction in different notation. A frozen physical datum can retain its old bound by identity; an old *function* which constructs its localization again needs the source of that new read identified.

The draw is another distinct case. Passing the extension test supplies a continuation of curvature less than \(2\varepsilon_k\). The centre \(V_\Lambda\), however, minimizes the effective function \(A(U_{k,X}(V_k))\), not the sum of coarse plaquette actions of that continuation. Consequently the elementary estimate “energy of the minimum is at most the energy of the exhibited continuation” does **not** bound its coarse plaquettes without a comparison for this effective function. The fixed radius \(a_\Lambda\) only gives a fixed-radius bound. Proposition 2.4's uniform conclusion \(C(M)\varepsilon_k\) supplies the needed shrinking bound, but its contraction argument has not been rebuilt here. Once that conclusion is proved, (10.3) handles every changed and crossing bond with no further loss depending on depth.

The finite number of coarse box bonds does not remove this issue: the effective function contains a background on a tower of varying depth. A finite-dimensional inverse theorem at each depth does not supply a common derivative bound or a common neighborhood. The positivity route in raw I 156946–156977 is explicitly marked as outstanding and refers this definedness and continuation step to CMP 122; it is not a further proof of the input.

## 18. The remaining collar counterexample: exact geometric and quantitative requirements

There is no geometric protection of an old outer collar from a later floor. To see this without a schematic picture, suppose an operation at level \(s\) leaves a drop-out on a box \(X_s\). Let \(H\) be its hull in level-\(s+1\) cells. A collar of width at most \(c_{\rm col}M\xi_s\), including its source footprint, lies within \(H^{[1]}\) once \(c_{\rm col}M+3<MR_{s+1}L\). A quiet next step has
\[
                 \Omega_{s+1}^c\cap X_{s+1}=H^{[8]}.
\]
Every cell of \(H^{[1]}\) is then separated from the complement of \(H^{[8]}\) by more than one cell. It belongs to the floor with bottom \(s+1\). At a later class operation whose bottom is \(s+1\), nesting puts this old collar inside the current component as well. Thus the current-collar exclusion of Section 12 cannot be recycled for that old read. This calculation concerns a retained localized function; it does not assert that artificial bonds became stored physical bonds.

The bottom index can be arranged without a rounding assumption: choose \(T\) in the interior of one radius plateau, with \(R(T\pm2\beta R)=R\), and let the frame continue linearly. Such choices exist for large powers \(R\) because the plateau endpoints are \(\exp((R/L)^{1/r})\) and \(\exp(R^{1/r})\), whose separation eventually exceeds \(4\beta R\). Then the next eligible quiet operation is at \(m=s+R+1\), with bottom \(s+1\); quarantine includes no earlier operation in its window. This proves feasibility of the index arithmetic, not the unconstructed nonzero field history.

What is still needed is a **supported nonzero** source on such an old read. For the linear frame ending with \(\theta_s=T\), let \(h_s=\|\partial V_s(p_s)-1\|\) be that source holonomy. The exact lift would violate the geometric-level-zero envelope uniformly if
\[
 \frac{h_s}{R_0^2\varepsilon_0}\longrightarrow\infty,
 \qquad
 R_0^2\varepsilon_0
 \le L^2A_0(T+\beta s)^{-1/2}
       [\log(T+\beta s)]^{2r+\mathfrak p_0}.       \tag{18.1}
\]
Here \(\beta>0\) is the fixed slope of the frame, not a bare inverse coupling. A fixed positive \(h_s\) is sufficient but unnecessary: a lower bound \(h_s\ge c s^{-\alpha}\), \(\alpha<1/2\), also suffices. This follows by dividing the right-hand side of (18.1) into that lower bound and using that a positive power dominates a fixed power of a logarithm. It is a hand limit, not a numerical test.

Section 16 supplies arbitrarily late quiet components with \(h_s=0\). Openness at each fixed depth could at most provide a radius \(r_s>0\) for perturbing that history. It supplies no lower bound on \(r_s/(R_0^2\varepsilon_0)\). In particular, assigning a nonzero coarse bond first and appealing to continuity afterwards still does not verify (18.1), the earlier localized plaquette indicators, or the recorded fate retaining the old function. The uniform support estimate needed for this perturbation is not established by the long account's age definitions or by its inherited-datum hypothesis. This is the exact unresolved step of this counterexample, not an asserted obstruction to constructing one.

If such a history is constructed, the smallest **candidate** change for the floor consumer remains (6.1): retain the source level of an artificial lift instead of imposing its bound at the new geometric level. For the old collar above the source is \(s\), below the later bottom \(s+1\), so (6.2) gives the common floor amplitude used by screening. This change is sufficient for that conditional consumer; without the supported example, its necessity or minimality for the outline is not proved.

## 19. Third-run checkpoint before the reference-law construction

**Intermediate checkpoint, superseded by Sections 20–23.** At this point neither a full proof nor a refutation had been obtained. The initial-strip read is no longer missing for the concrete ordinary-step rule of Section 14.1: (15.1) identifies its two passing indicators and reconstructs its pivots. The omitted ordinary plaquette band is four current-cell layers, not an unknown margin inferred from (sigma6). The same rule supplies ordinary positive-level seam coverage. The outline's formation data must actually select those read sets, or verify their replacements; a claim about every unspecified completion does not follow.

The full read-by-read induction still requires two substantive verifications. First, the reference-law centre must satisfy the uniform shrinking estimate on every incident plaquette; the extension test, fixed mild radius and finite coarse box alone do not prove it. Second, each inherited localized read must be traced at its own actual arguments, including the collar it constructs again. The current stage's passing curvature test does not control the whole old marked region. Imposing the desired bound in an evaluation fibre does not establish it on the original support.

The counterexample route has a concrete remaining task rather than a free seam assignment: add a nonzero collar source satisfying (18.1) to a recorded supported history, retain its localized read, and check its indicators. Section 16 proves the late-creation geometry at zero source; Section 18 proves that an old collar can fall in a later floor. Neither supplies that nonzero supported perturbation. No necessary definition change, unconditional support envelope, or screening result has been obtained. The existing conditional source-level repair remains available, without a claim of minimality.

Only this note was edited. Source extraction and whitespace checks are not mathematical evidence; no computation was used to discharge a step, and no audit or status change was made.

## 20. A different source: the reference law, not a perturbation of the old history

The preceding checkpoint overlooks a useful distinction. A uniform neighborhood of a nonzero *old* physical field is not needed to put a nonzero field in the *new* box. The main step replaces the box density by its mass times the displayed reference law (SA 17602–17608). At a flat exterior its centre is exactly 1. On its declared domain, that law is strictly positive at every tree-gauged box field strictly inside its cutoff. The mass can depend on the depth and be arbitrarily small without shrinking this support.

Here and below, a kernel's **declared domain** means the actual variable space in its definition: the real background maps and total Borel indicators are formation data (SA 6049–6063), and the reference law is the law in (2b)(4). This does not use a quantitative theorem about their response. In particular, the argument below applies to any realization of those maps on that domain with the specified constraints and group-valued outputs. It is not a construction of the background maps themselves. Rejecting their existence on that domain rejects the specified operation before the support question; it is not a smaller support produced by an additional indicator in the displayed reference law.

**Positive box support at flat exterior.** Use the exactly flat creation and quiet history of Section 16, through its first eligible operation at level \(s\), with bottom \(a=s-R_s\). The gauge disturbance lies in the old core. Every preparatory shell has field 1 in the gauge of its reference. Each sharper fluctuation is zero, each stage curvature is zero, the regular-extension test passes using 1, and the last-shell test passes using 1. The multi-scale variable \(B\) in the main integration can be zero. The failed creation test remains under the core integral, where its complementary indicator is 1; it is not imposed on \(B\).

The centre of the reference law is 1 in its tree gauge. Indeed, at exterior 1 the value 1 gives Wilson action zero; the Wilson action is nonnegative. A minimum of value zero has every plaquette equal to 1. On the box it is a pure gauge, and the tree including its one external bond fixes that gauge. This identifies the centre without Proposition 2.4's uniform shrinking estimate.

For each fixed finite \(s\), the incoming main-step mass is positive. At the flat history all passing inequalities are strict and the failed approximate inequality is strict in the other direction. In local coordinates the averaging constraints have full rank: their distinct pivots have nonzero diagonal derivatives, as in Section 4. After fixing the residual gauge, the flat constrained Hessian has no null direction: zero curl gives a gradient on a box, the fixed coarse data remove torus cycle directions, and the gauge slice removes the remaining gradients. The finite-dimensional inverse therefore gives a neighborhood of this history on its constraint surface. One may obtain it by writing the critical-point equation as a contraction after multiplying by that inverse; its radius may depend on \(s\). On a smaller neighborhood the recorded indicators are unchanged, the gauge weights and Wilson weights are positive, and all finite Gaussian elimination factors are positive. The integral of such a neighborhood is positive. Only positivity is used, not a lower bound uniform in \(s\).

Let \(e\) be a non-tree level-\(s\) bond strictly inside the draw box \(\Lambda^{\rm pr}\). Set
\[
 V_s(e)=\exp(i t\sigma_3),\qquad V_s=1\text{ on every other independent bond},
 \qquad 0<t<M_0\varepsilon_s.                 \tag{20.1}
\]
The inverse orientation has the inverse value. This obeys the tree delta and the cutoff. For any group-valued field furnished by the specified background map, its Wilson action on the finite lattice is finite. The reference-law numerator is thus positive, as is its normalizing integral. The latter is finite because the Wilson plaquette function is bounded and the integration domain is compact. Consequently (20.1), and a relatively open neighborhood of it in the tree slice, belong to the support of the new box measure. No bound on a derivative of a background map, and no lower bound on the old mass, enters this assertion.

This is also a point of the support of the full measure, not just an arbitrary version of a conditional measure at a null exterior. For each fixed \(s\), the strict incoming inequalities persist on a neighborhood of the flat exterior by the same finite-dimensional argument. The flat box centre is continuous on some such neighborhood: its gauge-fixed Hessian is the positive Schur complement of the finite flat constrained quadratic form, so multiplying its critical equation by that inverse again gives a local contraction. Its radius may depend on \(s\). The strict cutoff in (20.1) therefore persists after a sufficiently small exterior change. On this open exterior set the incoming masses are positive and the new-law density is positive on a relatively open box set. Every neighborhood of the displayed point consequently has positive mass. This uses no continuity estimate at the nonzero draw, since positivity of its finite real exponential is enough.

If the intended construction has a *further* restriction on this law, such as a depth-dependent domain excluding (20.1), it must be supplied as a changed formation rule. It is absent from the cutoff written in (2b)(4). This is the precise distinction from the unsuccessful continuity argument of Section 18.

## 21. A localization collar can cross the old floor during the final decision

The collar excluded from the floor by Section 12 is the outer collar of the **component** \(X\). The final healing/island decision also uses the ordinary cube tests \(\chi_s(D)\). SA 17831 identifies this explicitly as the test of a step, not a sharper stage test; SA 17648–17654 retains its complement \(\chi_s^c\) in an island. A cube test uses the tower on \(D^{\sim4}\), with the lifted datum of CMP 119 (1.2)–(1.3), (2.13), and SA 9783. Its boundary can pass through the core even while the whole localization domain lies well inside \(X\). The component's two-cell outside clearance says nothing against this.

Here is a placement with coordinates. Work in bare units, write \(\xi=L^s\), and let the side of a level-\(s\) test cube be \(q\xi\), where \(q\) is its fixed power-\(L\) multiple of \(R_s\). Choose the test cube with centre \((-4q\xi,0,0,0)\). The positive first-coordinate face of its fourfold enlargement \(W=D^{\sim4}\) is
\[
                         x_1=d:=q\xi/2.
\]
All lattice lengths are odd, so \(d-1/2\) and \((\xi\pm1)/2\) are integers. Consider the bare plaquette \(p\) in the \(2,3\) plane whose four corners are
\[
 \bigl(d-\tfrac12,\ (\xi\pm1)/2,\ (\xi\pm1)/2,\ 0\bigr).
                                                        \tag{21.1}
\]
It lies inside \(W\), one half bare spacing from its face. Erosion to the tower's next member has positive width greater than one bare spacing. Hence all four edges of \(p\) are level-zero determining bonds of this tower, and are new lift bonds. They are not inward bonds. Both block-face crossings are tangential to the outer face; a plaquette with only one crossing would instead have holonomy 1, which is why two tangential directions are used.

Its four level-\(s\) block centres are the vertices of the coarse plaquette \(P\) in the same \(2,3\) plane, with first coordinate \((q-1)\xi/2\), second and third coordinates in \(\{0,\xi\}\), and fourth coordinate 0. The exact lift calculation of Section 6 gives
\[
              \partial\mathbf V_W(p)=\partial V_s(P).
                                                        \tag{21.2}
\]
This is an equality of ordered group products, not an estimate on a background.

Place the creation of Section 16 in a bottom-level cell \(J_a\) incident to \(p\). Choose its gauge site deep in that cell; the approximate-test failure cubes then have hull \(J_a\). The plaquette-test failure set is empty. Thus \(\Omega_a^c=J_a^{[2]}\), and every cell meeting \(p\) is in \(J_a\) or an immediately adjacent cell. None touches \(\Omega_a\): the second added layer separates it from that set. All four corners of \(p\) are therefore in the old floor of this operation. This placement is compatible with the partitions. Choose the radius plateau of Section 22 large enough that \(L^R/(MR)\) is an odd integer. Both the level-\(s\) block side and its test-cube side are then odd multiples of the bottom cell side \(MRL^{s-R}\). Their faces are consequently faces of the finer cell partition; using the cells incident to those faces deals with all boundary assignments. The creation site need not be at the face.

The prepared main box contains the old core with a layer of level-\(s\) \(M\)-cubes to spare (the last enlargement in raw I, Definition 4.18, used in Section 17). The vertices and edges of \(P\) lie within two level-\(s\) spacings of \(p\). They thus lie strictly in \(\Lambda^{\rm pr}\), since \(M>4\). Pick a non-tree edge \(e\) of \(P\), which exists because a tree contains no cycle, and use precisely (20.1) on this edge. Up to inversion according to orientation,
\[
      \partial V_s(P)=\exp(i t\sigma_3),\qquad
      \|\partial\mathbf V_W(p)-1\|=2\sin(t/2).
                                                        \tag{21.3}
\]

The cube \(D\) is among the tests of the final decision. Raw I 51737–51753 specifies that decision on \(X^{\sim-6}\). Since \(X=H_s^{[10]}\), this leaves \(H_s^{[4]}\). The coordinate span from \(p\) to the opposite face of \(W\) is \(9q\xi\). In the outline \(q\le MR_s/L^2\), so this is less than one cell side for \(L\ge5\); even the extra fixed factor \(L\) in CMP 119 makes it less than two cell sides. As \(p\) belongs to the old core in \(H_s\), the whole \(W\), and in particular \(D\), lie inside \(H_s^{[4]}\). This also puts \(W\) inside \(X\), as required for the test to be local to the component. No parameter in this placement depends on the growing depth except lattice spacings and the location of the seed.

The floor here is the old floor fixed when the operation starts. The read occurs in the final decision after its main integration, not in the earlier shell tests. The old physical fine variables have then been removed from the box. The four bonds in (21.1) are **artificial determining bonds of this actual localized read**. They are not asserted to be surviving physical \(\Gamma_0\) bonds of the new label. This distinction is essential to the literal joined-datum target of this item.

## 22. The admitted configuration and failure of the uniform constant

Fix all geometric constants first. Take the permitted reference cutoff constant \(M_0>8\), and choose a sufficiently large \(T\) in a radius plateau with
\[
 R(T)=R(T+\beta(R+1))=R,\qquad L^R/(MR)\in 2\mathbb N+1.
                                                        \tag{22.1}
\]
Here \(\beta\) is an allowed positive frame slope, as in Section 6, and is not the bare inverse coupling. Such plateaux exist: their lengths eventually exceed any fixed multiple of \(R\), as shown in Section 18. The divisibility follows by choosing the power \(R=L^n\) with \(R\ge n+\log_L M\). Increase \(T\) to meet the fixed small-coupling ceilings below. For every integer \(s>R+2\), use the legal linear frame
\[
 \theta_i=T+\beta(s-i)\quad(0\le i\le s),\qquad
 a=s-R,\qquad b=a-1.
                                                        \tag{22.2}
\]
Choose a torus sufficiently large to contain the component and all the displayed read neighborhoods without wrapping.

The field and the recorded choices are now specified as follows.

1. Before the operation, use (16.1)–(16.2), with the gauge site in the cell \(J_a\) fixed in Section 21. The only creation is the approximate-fluctuation failure at level \(a\). All curvature tests pass; its failed approximate tests have value zero and their retained complements have value one. The subsequent steps are quiet, and the first eligible operation is at \(s\).
2. In that operation take the flat shell variables and \(B=0\) of Section 20. All sharper stage, extension, and last-shell tests pass strictly. The old failed creation remains confined to the core. This produces a strictly positive incoming mass at flat exterior, separately for every finite \(s\).
3. In the reference-law draw choose the non-tree edge of \(P\) and (20.1), now with
   \[
                    t=8\varepsilon(T).
   \tag{22.3}
   \]
   Every tree value is 1 and the logarithmic cutoff is strict. The exterior is still 1. Section 20 proves membership in the support of the new measure.
4. Record the final **island** outcome. To check it, let \(E\) be a test cube containing a corner of \(P\). Its once-enlarged cube contains the complete four-row averaging footprint, and its tower's top includes those rows, exactly as in Section 15. If \(\chi_s(E)=1\), the hand averaging estimate gives
   \(\|\partial V_s(P)-1\|\le2\varepsilon_s\).
   Instead, for \(4\varepsilon(T)<\pi/2\),
   \[
     \|\partial V_s(P)-1\|
       =2\sin(4\varepsilon(T))
       \ge \frac{16}{\pi}\varepsilon(T)>2\varepsilon_s.
   \tag{22.4}
   \]
   Thus \(\chi_s(E)=0\) and the retained island indicator
   \(1-\prod_{E\subset X^{\sim-6}}\chi_s(E)\) equals 1.
   The earlier extension, tree and cutoff factors retained by that island
   also equal 1. No new condition compares the drawn field to the integrated-out old shell variables.

The word *admitted* here does not mean that every elementary indicator is 1: a large-field history necessarily contains recorded failures. It means that every retained indicator **factor**, including the complementary factors selected by the history, is 1, all delta constraints are satisfied, and the non-indicator factors give positive weight. The four checks above give precisely that. Individual values of other cube indicators in the last product need not be guessed: one specified zero makes its complementary factor exactly 1. The formation rule retains that product's complement as a single island factor, not a demand that its other factors pass.

The cube \(D\) is a factor of this decision, and its joined datum is the datum specified for that factor. If one implements the product by sequential tests with early termination, take \(D\) first: no rule in the formation data specifies a contrary order, and this order changes neither the product nor the resulting measure. Thus the example can make this an actual read before any failure of the final decision is known, rather than an unused factor after early termination. Whatever value this first indicator takes, the failed test \(E\) proves the recorded island outcome. The level-zero test \(p\) of that read is in the old floor, and (21.3) gives the fixed positive value
\[
                    h=2\sin(4\varepsilon(T)).
                                                        \tag{22.5}
\]
All its data lie in the usual *fixed* mild-data domain: the single coarse bond gives coarse plaquettes of size \(h\) or zero, and every lifted or mixed plaquette is the corresponding coarse plaquette by Section 6. In particular \(h\) can be made smaller than every fixed real chart radius by choosing \(T\). The defect is the proposed **running level-zero envelope**, not a distant branch of the averaging map or a datum outside a fixed small-field chart.

On the other hand,
\[
 R_0^2\varepsilon_0
 \le L^2 A_0(T+\beta s)^{-1/2}
              [\log(T+\beta s)]^{2r+\mathfrak p_0}
 \longrightarrow0.                                  \tag{22.6}
\]
For a hand verification of the limit, put \(v=\log(T+\beta s)\), choose an integer
\(n>2r+\mathfrak p_0\), and use
\(e^{v/4}\ge(v/4)^n/n!\).
The right side of (22.6) is bounded by a constant times
\(e^{-v/4}v^{2r+\mathfrak p_0-n}\), which tends to zero.
For every proposed constant \(C\), therefore, an \(s\) in this explicit family satisfies
\[
                  \|\partial\mathbf V_W(p)-1\|
                     >C R_0^2\varepsilon_0.
                                                        \tag{22.7}
\]
This refutes the literal **every-joined-read** version of (D-F). There is no limiting configuration or computed value in the argument: each violating \(s\) gives a finite torus, a finite history, the stated recorded outcomes and a supported tree-gauged draw. The old incoming mass need not stay bounded below. The source is created by the reference law after the old averaging constraints have been integrated out, so none of Sections 3–4's surviving-constraint obstructions excludes it. No later quiet-history perturbation is required.

## 23. Exact scope and the definition to change

The contradiction uses three stated rules together: the box reference law has a cutoff of order \(\varepsilon_s\) independent of the total depth (SA 17602–17608); the final decision uses the ordinary localized cube tests (SA 17831; raw I 51737–51753); and their new lower-level datum is the exact unsmoothed lift (SA 9783, CMP 119 (1.3)). These cannot additionally satisfy a running envelope indexed by the **new geometric level of every artificial bond**. A lower bound on the region margin, or another pass through the physical pivot proof, changes none of them.

This is not a refutation of the narrower sentence about the stored physical fields \(V_l|_{\Gamma_l}\) in SA 17709–17715. The artificial bond in (21.1) is not such a surviving physical bond. Nor does this example say that the original pre-main shell datum fails its envelope. It refutes the broader joined-datum target explicitly asked for here, at an identified internal read of the operation. Omitting the final decision from that target would be a restriction of its quantifier, not a repair of the counterexample.

The smallest change to the **bound's indexing** is to give every artificial lift test its source level \(j\) and use \(CR_j^2\varepsilon_j\), keeping its actual geometric support and distance unchanged. This is the owner-level variant of Section 6. For the present example \(j=s\), not 0. It accommodates (22.5) directly. During an operation of level \(m\), all such source levels are at most \(m\); the scalar estimate of Section 6 bounds their common amplitude by \(C'L^2R_m^2\varepsilon_m\). If the floor is indexed by \(a=m-R_m\), the frame bound \(\theta_a-\theta_m\le\bar B R_m=o(\theta_m)\) also compares this with \(C''R_a^2\varepsilon_a\). Thus the change preserves the *conditional common-amplitude screening implication*. It does not establish the unproved source bounds at all other reads, and it does not restore the literal geometrically indexed (D-F).

If that literal statement must be retained, the smallest direct **admission change** is an additional binary gate immediately before *each actual background read*, including those in the final decision. Form its joined datum first and set
\[
 I_{\rm join}(\mathbf V)=
 \prod_{\tau\in\mathcal T(\mathbf B)}
 \mathbf1\!\left\{\|\partial\mathbf V(\tau)-1\|
                 \le C R_{\ell(\tau)}^2\varepsilon_{\ell(\tau)}\right\},
                                                        \tag{23.1}
\]
where \(\mathcal T(\mathbf B)\) is the finite set of that joined datum's mixed plaquette tests, and \(\ell(\tau)\) is their actual geometric level. Only the \(I_{\rm join}=1\) branch may make the background call. The complementary branch must retain its data and stop that attempted call as a new failure outcome. The products in (23.1) use already specified bonds, pivots and averages and are Borel; the gate requires no background to evaluate. The identity \(1=I_{\rm join}+(1-I_{\rm join})\) supplies both branches. On every branch that proceeds to a read, each factor is 1, which proves the literal (D-F) for those reads without an induction hypothesis. Applied to the configuration above, the gate rejects the call on \(D\) once (22.7) holds.

This changes the formation/admission definition at SA 6049–6074, and in particular its use after the reference-law draw. The existing law has no such factor. Merely imposing it on an evaluation fibre, or asserting it after the call, does not repair the support. The cost of its new failure outcomes, and compatibility with the claimed large-field mass estimates, are **not proved** by this repair. No claim of a repaired Yang–Mills construction, completed screening package, audit verdict or scientific status follows.
