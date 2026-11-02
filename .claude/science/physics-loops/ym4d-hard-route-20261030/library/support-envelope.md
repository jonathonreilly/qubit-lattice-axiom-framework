# Support envelope — queue row 88
Provenance: OpenAI Codex, GPT-6 family (exact backend and actual effort not exposed; row 88 requests max); checkout `bb7f39d69e3410da4e450f04e2331f031cc6f2a1`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, grants no status.

**Outcome: STOPPED at the session budget. The full support assertion (D-F) is neither proved nor refuted. No explicit admitted counterexample has been obtained.** The finite pivot and averaging arguments below are completed; the history-wide admission step is not.

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
