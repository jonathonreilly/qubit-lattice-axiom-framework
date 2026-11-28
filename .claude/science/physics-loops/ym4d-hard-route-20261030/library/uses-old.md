# Uses of the five old inputs in CA I–III

Sources: `/tmp/sa_ca_I.tex`, `/tmp/sa_ca_II.tex`, `/tmp/sa_ca_III.tex`, corresponding to the supplied raw-account revision `31a47c543775`. Locations below use **I**, **II**, **III** for those exact filenames. Searches covered all three files; inspection was by bounded excerpts. No proofs were attempted.

A **clear use** includes a result explicitly assumed as a hypothesis, an application in a proof, or an unmistakable reuse of its displayed estimate. Repeated applications within one labelled statement are grouped, with separate locators where their roles differ. A restatement, proposed route, negative comparison, or status inventory is identified separately. This is a map of textual dependencies, not an endorsement of any inference. It does not expand every dependency transitively through all downstream theorems. Labels beginning `prf-` can themselves label lemmas/propositions, rather than merely proof paragraphs. Unlabelled material is identified as such instead of borrowing the last preceding theorem's label.

## 1. `4.5:lem-uniform-increment`

Source: **I:16019–16150**, displays `4.5:eq-uniform-increment-a,b`. The distinctive content is the depth-independent constant `C_IV`, the increment `½ C_IV α₂ λ²` for both tower quantities on `X^{~2}`, all `n≤j`, and the threshold `α₂≤min(α₁/8,α₀/C_IV)`. The same statement also supplies the potential, plaquette, unchanged-unitary-factor and tower clauses. Its own proof and its continued proof blocks are not external applications.

### Clear uses

| Location | Using statement | Content used |
|---|---|---|
| I:10534,10552–10553,10626 | `4.4:lem-twist-stability` | Uses the uniform-increment constant in floor (s3′), `C₀>2 C_IV C_H(1+β₀)‖C‖C₁A₁`, to place the layered twist below both radius thresholds. |
| I:11889–11916 | `4.4:prf-interior-sources` | Hypothesis (P) explicitly instantiates the lemma at every `(p,Z)∈T_j(X)`, cube letter `M/L`, gauge letter `LB`, radii `L^{-(j-p)}(α₀,j,α₁,j,α₂)`; concludes the hereditary tower clause for the twisted configuration. |
| I:12037–12057 | `4.4:prf-interior-sources` | Verifies `α₂<min(α₁,j/8,α₀,j/C_IV)` and carries the rescaled floors `δ₀M≥32L`, `2LR₁M₁≤M` and the lemma's ceilings. |
| I:17926–17939 | `4.5:prf-base-change` | Uses the plaquette expansion from the lemma's proof for real twists `U_{A''}` on the twist polydisc: curvature `<(α₀‴+C₁₄α₁‴)ξ²`. The text calls this item (ii), although the plaquette conclusion is labelled (iii)₁ in the statement. |
| I:19455,19466,19480,19525 | `4.5:rem-constants-order` | Imports the lemma's floors/ceilings and `α₂≤α₀/C_IV` into the common order of constants for the operator theorem. |
| I:19781–19794 | `4.5:thm-operator-bounds` | Proof of (F1): applies the lemma with `A=A(t_□)`, amplitude `≤⅔α₂`, to a half-radius base; obtains (i), (ii), the first curvature member and uniform (iv) at `(α₀,α₁)`, making the old effective-action term analytic. |
| I:19825–19836 | `4.5:thm-operator-bounds` | Proof of (F6): reuses the same application for two further far terms; only admissibility, collar `≤M/2`, and the tower clause are read from the tower; window towers are included wherever their (iv) is established. |
| I:19915,19943–19950,19985,20001,20053,20091,20118 | `4.5:rem-size-conditions` | Carries the lemma's ceilings, floors and `C_IV` radius ratio into the consolidated size conditions; discusses their validity after substitution of the cube letter and the gauge used for `Q`. |
| I:29421–29432,29460 | `4.7:not-shift-fields` | Fixes shift radius using `α₂≤min(α₁/8,α₀/C_IV,…)`; explicitly identifies the class lemma behind `C_IV` and uses it for membership of the perturbed pair. |
| I:29533–29535 | `4.7:not-true-pairs` | Defines `c_T=min(c_T° ,1/8,1/C_IV)`, importing the same perturbation-to-curvature radius ratio. |
| I:29621,29631,29654,29671–29682 | `4.7:not-working-radii` | Chooses `c_α≤1/(3C_IV)` and verifies `α₂,i≤min(α₁,i/8,α₀,i/C_IV)` for running radii. |
| I:33839–33869 | `4.8:prop-far-case` | Explicit hypothesis is the “increment lemma” with its tower-uniform clause; assumes precisely its ceilings and the `M/L` floors before asserting preservation of the class. |
| I:33939–33950,33988–34004 | `4.8:prop-far-case` | In the proof, reads the lemma at each hereditary label with cube `M/L`, `LB`, and radii multiplied by `μ=L^{-(j-p)}`; uses constants independent of the label/depth. |
| I:34037–34054 | `4.8:prop-far-case` | Applies the tower increment `½C_IV(μα₂)λ′²` on the label's cut and uses `α₂≤α₀/C_IV`; explains that the target is the one-power radius, not the stronger two-power radius. |
| I:34252–34255,34328–34344,34391–34392 | `4.8:prop-class-reproduction` | Assumes the far-case proposition and its underlying inputs; membership (d) uses its half-radius base, and the proof uses the same `C_IV` threshold uniformly as radii shrink. |
| I:34436–34458,34504–34506,34530–34533 | `4.8:lem-top-layer-bound` | Uses the two uniform-increment thresholds to bound `H_w` at a top-layer consumer; the `C₀` floor pays the `1/C_IV` requirement, yielding a permitted strict perturbation radius. |
| I:34546,34576–34606 | `4.8:lem-layerwise-bound` | For a straddling producer, uses both the tower increment and clause (ii); requires additive margins `F_jα₀,j+½C_IVα₂≤α₀,j` and `F_jα₁,j+4α₂≤α₁,j` at every receiving label. |
| I:34660–34681,34685–34686 | `4.8:lem-layerwise-bound` | Proof (b),(c): chooses `α₂^far=min(α₁,j/8,α₀,j/C_IV)`; reads ceilings at source radii `μF_jα₀,j, μF_jα₁,j`; cancels common `μ` and `λ′²` factors in the additive inequalities. |
| I:34782,34797–34818 | `4.8:rem-lower-bounds` | Converts those `C_IV` radius requirements into lower bounds on `C₀,C₁′` and lists the increment lemma's amplitude ceilings. |
| I:32419–32424 | `4.7:prop-coupling-increment` | Explicitly assumes the class-membership propositions and their input “lemma on admissible towers accompanying the operator bounds … at scale M/L”; this is a mediated use of the tower-uniform increment input, not a new estimate. |

### Mentions, overlap and exclusions

- **I:15949–15954**, `4.5:rem-condition-iv`: discusses an alternative use on a potential of size `α₁′`, costing `½C_IVα₁′λ²`; explicitly says that route is not used. **I:16002–16016**, same remark, explains the two powers and previews the displayed bound.
- **I:16234–16258**, `4.5:lem-uniform-increment`, and **I:16269,16373,16462,16564,16781,16849,16927,16939–16961**, `4.5:prf-increment-geometry`, `4.5:prf-increment-kernel`, `4.5:prf-increment-recentring`, `4.5:prf-increment-conclusion`: internal uses of the lemma's own increment/ceilings while assembling its proof; not external dependencies.
- “Increment lemma” at **I:85827ff**, **I:111797ff**, **I:127403ff** refers to other local increment lemmas (profiles, stage layers or bump shells), not this depth-free twist lemma. No direct counterpart using this label, `C_IV`, or the uniform-increment name was found in II or III.

## 2. `4.13:lem-own-constant`

Source: **I:45203–45236**. The label occurs only at its declaration. The requested **content** nevertheless occurs elsewhere: the small and real-background pairs obey the widened cube condition at their own printed curvature constant, with one constant reproduced by a step. Earlier occurrences below are content overlap, not claims that an earlier proof cites the later lemma.

### Clear content uses and restatements

| Location | Using statement | Content used |
|---|---|---|
| I:35388–35415,35426–35439 | `4.9:rem-reproduction-meaning` | Defines reproduction to include seeds (unit/small/real-background pairs) at `α₀′`, and the same `B₁₂` for transport and seeds; the widened cubes have side `≤S=c₁₂LM` in level units. This formulates the content as a requirement. |
| I:36102–36104,36190 | `4.9:prop-gauge-transport` | At locus `⟨5c⟩`, `U_k|_X` is not inherited from a source membership; its clause (i) at `α₀′` is exactly the seed requirement. |
| I:36806–36838 | `4.9:cor-printed-pairs` | Explicit restatement of the own-curvature conclusion: bound `c₁₂LMB₁₂α₀′` on every cube of side `≤c₁₂LM`; small/unit pairs use `U=1`; real pairs use `α₀′=ε₀`, or `L^{-(k-j)}ε₀` at lower level. It explicitly claims reproduction at `k+1`. |
| I:36830–36838,36902–36905 | `4.9:cor-printed-pairs` | Says this supplies the seed hypothesis of one-step closure and the gauge hypothesis for minimal configurations to belong to every `U_j^{Σ¹}(X;α₀,α₁)`, with `2B₃ε₀≤α₀`. The text calls these hypotheses (f) and (i); the receiving statements' numbering is not consistently reproduced, so these are textual recipient descriptions, not invented label references. |
| I:36872–36900 | `4.9:cor-printed-pairs` | Uses the real-background gauge bound and `B₁₂≥2B₃` to express it at the pair's own constant, transports it to lower levels with one `μ`, then reapplies the same assertion at the next step. |
| I:38000–38004,38039–38059,38083 | `4.9:lem-thin-cube-gradient` | Uses the seed/own-curvature clause through `4.9:prop-real-backgrounds` and `4.9:cor-printed-pairs` to conclude clause (ii) of one-step reproduction; same constants for all levels and widened cubes. |
| I:34077–34096 | `4.8:prop-small-pairs` | Assumes (i), including the widened gauge clause, at the source constants `(α₀′,α₁′,γ₀)` before claiming class membership; the final sentence covers sufficiently small minimal backgrounds. This uses the own-constant gauge content as a hypothesis rather than citing `4.13`. |
| I:56425–56427,56465–56467 | `4.19:prop-clause-zero` | Hypothesis (a′) assumes the widened `(1.12)` condition on smaller cubes and its reproduction by the step; the proof includes (a′) among the joint induction inputs. It does not separately spell out the small/real seeds here. |

### Ambiguous/general mentions

- **I:30206–30218**, `4.7:not-class-restrictions`, and **I:32417–32424**, `4.7:prop-coupling-increment`: require the widened gauge condition for the whole inductive class. They are broader than the two seed kinds and do not identify `4.13:lem-own-constant`; count as shared gauge-content requirements, not direct uses of that lemma alone.
- **I:45229–45236**, `4.13:lem-own-constant`: proposed route, not a completed application; requires both the own-constant assertion and reproduction.
- **I:166622–166623**, unlabelled Chapter 4 dependency/status list; **III:111213–111214**, unlabelled outstanding-proof inventory: name the cube gauge condition for small and real-background pairs, marked proof outstanding. No proof or hypothesis application there.
- **I:53270**, `4.16` discussion, says “Bałaban's own constant” for a different cube-regularity input; **II:58892**, `5.9:rem-shifted-chart`, concerns dilating curvature in another argument. Neither phrase alone establishes a use of this lemma. Small-pair rotation invariance at **III:79880,79894** is also a different assertion.

## 3. `4.14:prop-prepared-data-admissible`, including every `pp. 178–179` citation

Source: **I:45557–45596**, display `4.14:eq-prepared-data-admissible-a`. Distinguish **A1** (nested, compatible unions of level-j M-cubes, separation `dist∞(Ω_j^c,Ω_{j+1})≥Mℓ_j`, Dirichlet hull) from **A2** (`Ω_t⊂Ω_k`, clearance `≥6M`, union of level-k LM-cubes). The proposition's concluding assertion for the prepared nest `Ω″` is **A1**. Applications that assume A1 and A2 together are listed as such; they do not show that the printed concluding sentence proves A2.

### Clear uses

| Location | Using statement | Content used |
|---|---|---|
| I:45628–45634 | Unlabelled discussion after the proposition | Uses the produced-nest admissibility lemma to supply the same conditions with stronger interlevel separation `LM`, in place of `M`. |
| I:46045–46046 | `4.14:thm-operator-theorem` | Standing hypothesis: A1 and A2 for the old nest and the new region `Ω_t`, for the free-current operator theorem. |
| I:46244–46260 | `4.14:lem-reading-hulls` | A1 interlevel clearance plus `M≥13L²M₁♯` gives `dist∞≥13Ls_{i+1}`; A1/A2 support the reading-hull construction. Includes page citation at 46247. |
| I:46478–46481 | Unlabelled remark “No reading hull in the unit frame” | Uses A2 to put `widehat□⊂Ω_k`; includes the page citation. There is no independent statement label. |
| I:46841–46850 | `4.14:lem-local-balls` | A1 makes a full layer crossing cost weighted length `≥M`, greater than the ball/path cut `M/(2L)`; cites the proposition and pages. |
| I:47253–47260 | `4.14:prf-form-walk-expansion` | Assumes A1/A2 as operator-theorem hypotheses for the form's walk expansion/base bound; page citation at 47258. |
| I:47616–47623 | `4.14:prf-form-walk-expansion` | Uses A1/A2 as the first condition of the coercivity proposition for the base-point lower bound; page citation at 47619. |
| I:47637–47648 | `4.14:prf-form-walk-expansion` | Explains A1 use in CMP96 geometry at `(M/(LM₁),M₁)` and `(M/(LM₁♯),M₁♯)`, summation with `M/L`, and property (Sc), at most two adjacent layers; A1/A2 also enter step (vii) and coercivity at `Λ=Ω_t^(k)`. |
| I:47745–47751 | `4.14:prf-positivity-inversion` | A2's `6M` clearance puts the enlarged unit boxes inside `Ω_k`, supplying property (b4); cites the proposition/pages. |
| I:47869–47875 | `4.14:prf-positivity-inversion` | Uses A2 again, as in Step 1, for unit-box properties (b1)–(b4) in sheet inversion. |
| I:47998–48001 | `4.14:prf-block-identities` | A2 supplies alignment of the level-k M-cubes within `3M` of a core, needed for the core/resolvent statement. |
| I:48042–48050 | `4.14:prf-block-identities` | A1 gives layer-crossing cost and levelwise alignment; applies local balls at radii `ε₁` for C/resolvent and `1` for J, with cut `M/(2L)`. |
| I:48132–48138 | `4.14:prf-block-identities` | Concludes operator clauses (A)–(K), covariance, dependence and Schur complements conditional on prepared-data admissibility at every history nest. |
| I:48337–48344,48373 | `4.14:lem-hull-cube` | Assumes A1 for the hatted nest; uses nesting, compatible partitions and separation to fit a second-cover hull into one cube, under `M≥13L²M₁♯`. |
| I:48520–48525 | `4.14:lem-gauge-family` | Uses admissibility of every assignment of stage states to get A1 for the stage nest before selecting the hull cube and its printed gauge family. |
| I:48764–48770,48843–48847,48862 | `4.14:rem-tiling-later-steps` | Uses A1 for the global componentwise nest and for every assignment of component states; the hull case analysis reads at most one component. |
| I:52560–52566 | `4.16:def-cube-class` (subsequent explanatory argument) | A1 makes `Ω₁` a closed union of level-1 M-cubes, hence `X₁⊂Ω₁`; compatible partitions are then used for the cube class. |
| I:52676–52679 | `4.16:prop-lowest-level-regularity` | Explicit A1 hypothesis for the decreasing nest, shells and pointwise weight. |
| I:52806–52813 | `4.16:prop-lowest-level-regularity` | Uses A1 to tile each `X_j` by level-j M-cubes and then `s_j=M₁♯ℓ_j` cubes; handles level 0 using LM-cubes. |
| I:53059–53066 | `4.16:prf-boundary-factors` | A1's positive separations imply `X_n∩Ω_j=∅` for `n≤j−2`, giving boundary weight factors. |
| I:53111–53118 | `4.16:prf-boundary-factors` | A1 puts faces of `Ω₁` on the `LMη` grid, used to locate fine sites/bonds relative to boundaries. |
| I:97621–97630 | `4.23:def-copies-reading` | Explicitly uses prepared-data admissibility in defining the subtracted copies: whole group for far `y∈Z`, only its tail for far `y∈Z^c`; cites pages. |
| I:143833–143835 | `4.28:lem-cutting-strata` | Page citation supplies monotonic increase of `Z″_i` and `Z″_h=Z_h`, used to combine the thin strata. |
| I:143888–143895 | `4.28:lem-cutting-strata` | Page citations supply the definition of `N₀` and the equality between an `MR_{κ₀+1}` cube at scale `κ₀+1` and an M-cube at scale `κ`; derives `N₀≥3` and the layer width. |
| I:143913–143920 | `4.28:lem-cutting-strata` | Page citation supplies that `Γ″_m` is one layer of scale-(m+1) M-cubes; its width is `L^{m+1−κ₀}≥L²` in `π_{κ₀}` sides. |
| II:14830–14843 | `5.2:prf-arrested-regions` | Page citation supplies compatible M-cube tilings: every coarser cube meeting `B_n` contains a `π_{j_n+1}` cube in it, producing the injective cube count. |
| II:17129–17132 | `5.2:lem-current-label-anchors` | Page citation says preparation remakes `Ω″_j,Z″_j` only inside its own component, leaving unprimed `Λ_j` unchanged; used to preserve current-label anchoring. |
| III:21301–21309 | `9.1:not-integer-floors` | Reads the first three CMP122a geometric floor conditions through prepared-data admissibility; page citation at 21304. |
| III:53327–53335 | `9.8:lem-exponent-localisation` | Uses the admissibility point count `#Y≤M⁴ C_d(d(Y)+1)`, then absorbs it in `e^{δκ^c d(Y)}`; page citation. |

### Restatements, inventories and ambiguous mentions

| Location | Context | Treatment |
|---|---|---|
| I:45558–45559,45598–45618 | `4.14:prop-prepared-data-admissible` and its unlabelled source discussion | Declaration and quoted source for prepared A1, including both page citations (45558,45599), not external applications. |
| I:166579,166647 | Unlabelled Chapter 4 input/status inventories | Both page citations list prepared-data admissibility as an input; no new use or bound is derived there. |
| II:145579–145580 | Input inventory associated with `8.21:cor-consequences-torus` | Lists prepared-data admissibility and its page citation among dependencies. |
| III:75801 | Unlabelled Chapter 9 dependency inventory | Lists the page citation, marked printed without proof. The nearest preceding labelled remark is not its consuming theorem. |
| III:111073–111079,111104–111106 | Unlabelled Chapter 11 synthesis | Names admissibility as an input shared by main clauses (0),(i); page citation at 111074. This is a reported dependency. |
| III:111311–111312 | Unlabelled Chapter 13 status list | Page citation in the outstanding-input inventory. |

All literal `178…179` page matches found in the three files are represented above, including ones about the preparation's other geometric content rather than the precise A1 conclusion. Generic uses of an “admissible nest” need not invoke the prepared-nest theorem: where the text merely fixes an arbitrary admissible datum, I have not inferred that theorem as its supplier.

## 4. `4.2:lem-unmarked`

Source: **I:4031–4069**, display `4.2:eq-unmarked-1`: `|β_l^A−β_l^0|≤C_rem ε₁^I` and `|β_l^A|≤C_β`, with the stated parameter independence. Its own proof at **I:4076–4133**, including the reference at **4127**, is not an external application.

### Clear uses

| Location | Using statement | Content used |
|---|---|---|
| I:3601–3605 | `4.1:thm-clause-zero` (following explanation) | Identifies the unmarked increment bound, together with the one-loop result and large-field bound, as an input to the coupling-flow conclusion. |
| I:4017–4028 | Unlabelled application paragraph immediately after `4.2:lem-one-loop` | Chooses `ε₁^I≤c₀/(2C_rem)`; assumes the unmarked lemma through `l≤n`, sums `|β_l^A−β_l^0|≤C_rem ε₁^I`, and transfers the Gaussian cumulative lower bound to the unmarked increments. This is not part of a newly labelled theorem. |
| I:56345–56354,56370–56378,56386–56390 | `4.19:lem-flow-bounds` | Supplies its per-step hypotheses at `l=k+1`: error `≤c₀/2` via the `C_rem` ceiling and absolute bound `C_β`; with the marked bound gives `B♯=C_β+barς` and the two-sided flow estimate. |
| I:56428–56430,56465–56478 | `4.19:prop-clause-zero` | Hypothesis (b) explicitly assumes the lemma, jointly with prior-level effective-density representation; its proof uses those bounds through `4.19:lem-flow-bounds` to control all increments up to n. |
| I:163165 | `4.36:rem-order-of-choice` | Imports exactly the ceiling `ε₁^I≤c₀(N)/(2C_rem)` with the SU(N) constants; records that it is imposed among the auxiliary small-field conditions. |

### Clear reuse of the resulting flow constant (mediated, not fresh applications)

The following locations use the derived envelope `B♯≤C_β+1`, its parameter order, or its frozen value. They are useful content matches, but the immediate supplier is the flow result/definition, not a new invocation of the unmarked lemma.

| Location | Using statement | Content used |
|---|---|---|
| I:144,162 | `0.2:not-glossary` | Records `bar B=C_β+1` and the parameter letter. |
| I:644–652 | `1.2:def-flow-constants` | Defines the flow constant `C_β` and envelope `B♯≤bar B=C_β+1`, to be fixed in Chapter 4. |
| I:1148 | `2.2:not-hypotheses` | Includes `C_β` in the auxiliary parameter tuple. |
| I:1631–1634,1659–1661,1687 | `2.3:not-stages-last` | Places `C_β` after M and before γ; freezes the flow triple and uses `(C_β+1)γ²≤1`. |
| I:2124–2125,2137,2145,2153–2157 | `2.4:lem-no-cycle` | Uses that same order and frozen triple to avoid a circular γ choice. |
| I:2648 | `3.1:thm-main` | Uses `C_β` as the previously fixed flow constant. |
| I:31794,31818,31823,31938 | `4.7:def-smallness-conditions` | Evaluates flow-dependent smallness ceilings with `bar B=C_β+1`. |
| I:56481 | `4.19:prop-clause-zero` | Reuses `barς≤1`, hence `B♯≤C_β+1`, in the coupling conclusion. |
| I:92964–92966,93336 | `4.22:def-coupling-ceilings` | Freezes ceilings at `C_β+1` and uses monotonicity to pass to actual `B♯`. |
| I:157195–157202 | `4.33:thm-stability` | Uses the flow envelope to bound the coefficient in the energy/stability estimate. |
| I:158112–158122,158315 | `4.36:not-flow-thresholds` | Uses `B♯=C_β+barς≤C_β+1` and the frozen envelope in first passage/transport thresholds. |
| I:163095,163143,163169 | `4.36:rem-order-of-choice` | Discusses the frozen `C_β+1` upper flow constant and why it is not compared with a power of L. |
| I:163307–163310,163423 | `4.36:not-sun-conventions` | Enlarges the envelope to `max(C_β+1,c₅)` for the SU(N) convention. |

### Ambiguous mentions and exclusions

- **I:166617**, unlabelled Chapter 4 status inventory, and **III:111368–111369**, unlabelled Chapter 13 list: explicitly list the lemma as stated/proof incomplete; no new application.
- **I:156347,156392,156478–156482**, `4.31:prf-tube-analyticity`: assumes `|β_j(g_{j−1})|≤C_β` for the **complete** increment via `4.31:eq-standing-inputs-a` and uses it in the complex energy bound. The notation matches, but this is not literally the lemma's unmarked-only bound; attribution to this lemma alone would be unwarranted.
- **I:113154–113155,113297**, `4.25:lem-pile-bound`, and **I:115596–115599,115804**, `4.25:thm-frozen-collar-weight`, use a separately defined pile constant also called `C_β`. The latter expressly distinguishes it from the flow constant. Not uses.
- The many `C_β` occurrences in II/III for extraction-functional norms, running shifts and typed coefficients trace to `5.2:lem-extraction-cost` or a locally named constant. They do not by notation alone invoke this lemma. No additional direct use of `4.2:lem-unmarked` or its displayed equation was found in II.

## 5. CMP 102: Theorem 1, Proposition 9, and (189)–(190)

The three named presentations are **I:35144–35199**, `4.9:thm-minimal-orbit`; **II:85845–85895**, `8.4:thm-minimiser-analyticity`, including `8.4:eq-minimiser-analyticity-a`; and **III:35577–35626**, `9.3:prop-second-variation`. They are declarations/source identifications, not external applications. Other presentations of the same inputs are included below because their formulas are subsequently used without repeating the original labels.

Notation in this section: **T1** = existence, uniqueness of the critical orbit in the stipulated regularity class, and minimiser regularity/cube estimates; **P9** = analytic continuation in the relative block datum about a real regular base and its Landau/axial representation; **189** = localised higher-order-functional Hessian bound with an `ε₃` factor; **190** = exponentially decaying data-response kernels, including the appropriate derivative members when the text invokes them. In particular T1's cube estimate requires `M′≤R₁M₁a₁/ε₁`; P9 is on its own small-data neighbourhood, usually (172). These are distinct inputs. References to other equations of CMP 102 are not automatically uses of these four results.

### Clear uses in I

| Location | Using statement | Content used |
|---|---|---|
| I:1031–1035 | `1.5:def-domains` | Defines the tower minimiser/current functions used in regularity condition (iv) by the CMP102 variational problem on the maximal tower. This is a definition-level use of the minimiser content. |
| I:1340;1510,1559;1670 | `2.3:not-stages-first`, `2.3:not-stages-middle`, `2.3:not-stages-last` | Imports `B₃(d,L)`, P9's `B₅` and T1's `a₁`, and the cube-size ceiling `M≤R₁M₁a₁/ε^run` into the parameter order. |
| I:2063,2094 | `2.4:lem-no-cycle` | Reuses those constants and the decreasing cube ceiling while checking the order of parameter choices. |
| I:3136 | `3.1:thm-main` (dependency explanation) | Names T1 as an input to the main-theorem implications, with the stated `q≥21p₀+1` restriction. |
| I:3791 | `4.2:def-increment` | Uses the linear response of the CMP102 minimiser at the identity to define the free-boundary response entering the polarisation/extraction coefficient. |
| I:10163–10202 | `4.4:not-response-bound` | Takes P9/(190) at real minimiser bases with complex data in (172); all five members are included. Integrating and summing gives rate `δ₀/16`; free independent-current extensions are separately supplied by the operator theorem. |
| I:10516,10521–10522 | `4.4:lem-twist-stability` | Hypotheses include all five (190) members on (172); imports T1/P9 plaquette constant `B₃` for real minimisers. |
| I:10725–10738 | `4.4:lem-twist-stability` | T1 gives the real base `U₀=U_{p,X}(M·U)` from (7); P9/(190) is read along the complex data-twist segment in (172). |
| I:10747–10780 | `4.4:lem-twist-stability` | Uses the real-base curvature `≤2B₃α₀,n` and integrates the first two (190) members from `H_p(0)=0` to bound the nonlinear current-remainder increment. |
| I:12793,12812,12892–12894 | `4.5:not-geometry-conventions` | Chooses fixed `barε₁≤a₁`, uses `B₃a₁≤a₀`, and T1 uniqueness in `B₃ε₁≤ε₀≤a₀`; separates this fixed parameter from the actual data curvature. |
| I:13128–13134 | `4.5:not-reading-conventions` | Fixes the P9/(172) margin `sup|B|≤½C₁barε₁`, respecting both the group-valued and logarithmic readings of the small-data domain. |
| I:14847–14865 | `4.5:prf-chart-variation-decay` | Uses the first three (190) estimates as the pattern/content for free-current chart bounds (K8), with layer factors `ℓ_j^{-1}`, `ℓ_j^{-2}`, `ℓ_j^{-2−β}` and data measure `ℓ_{j′}^d`; the current kernel substitutes for the last two members. This is an explicitly identified analogue, not direct applicability of P9 to an independent current. |
| I:15125,15137–15150;15432 | `4.5:prf-chart-constants`; `4.5:prf-chart-walk-localisation` | Reuses (K8)'s weighted Hessian/response-decay content in the chart's uniform constants and in the localised operator expansion. The local proof of the analogue is separately identified. |
| I:15707–15735 | `4.5:prf-diagonal-exactness` | T1 (9) supplies `(3.35)` regularity for the real base on cubes of side `12 mathfrak M L^jη`; checks `6 mathfrak M≤R₁ mathfrak M a₁/barε₁`, then identifies the regular real minimiser. |
| I:15964–15966 | `4.5:rem-condition-iv` | Uses T1 regularity for the small fixed class cubes rather than an M-sized cube, so the local regularity conclusion does not impose an M cap there. |
| I:16026,16044–16066 | `4.5:lem-uniform-increment` | Assumes the P9 data neighbourhood (172) with logarithmic margin `sup|B|≤½C₁barε₁`, and requires the entire segment `tB` to remain in it; supplies the analytic-response domain of its increment argument. |
| I:16375–16382 | `4.5:prf-increment-geometry` | Applies T1/P9 for arbitrary admissible truncated towers; admissibility, not a special tower name, is the tower input. |
| I:16492–16532 | `4.5:prf-increment-kernel` | T1 gives `U₀=U_n(V₀)` and its unique critical orbit: data curvature `≤C₇α₀≤barε₁≤a₁`; chooses `ε₀=B₃barε₁≤a₀`. |
| I:16565–16579,16595,16667 | `4.5:prf-increment-kernel` | Places `V_t=e^{iB_t}V₀` in the P9 polydisc with the stated margin, uses analyticity and the Landau-to-axial representation, and uses the response derivative kernel along that data segment. |
| I:16772–16801 | `4.5:prf-increment-recentring` | P9 analyticity near the real base and its Landau representation allow recentering under the small complex gauge change; uses identity continuation on a common neighbourhood in (172). |
| I:17555,17592–17594,17617,17769–17771 | `4.5:lem-literal-frame` | Assumes derivative bounds for H at base 1; P9 supplies two analytic charts (base 1 and base `M·U`), and T1 uniqueness identifies the base-1 minimiser as 1. `|B_V|≤½C₁barε₁` is inside (172). |
| I:17882–17905 | `4.5:prf-base-change` | T1 gives the chart's real base at `ε₁=barε₁`; P9 provides holomorphy of the two chart functions on the twist polydisc. |
| I:17940–17964,17976–18000 | `4.5:prf-base-change` | At real points uses T1 uniqueness with `ε₀=B₃barε₁≤a₀` and P9 agreement with the real minimiser, then extends the equality between charts holomorphically. |
| I:18492,18499,18633,18671,18690 | `4.5:lem-fine-axial-frame` | P9 at base 1 supplies H and its analytic frame map; compares this chart with the chart at `M·U` on the fine twist polydisc; assumes the window-H bound. |
| I:18783–18793 | `4.5:lem-fine-axial-frame` | Explicit source-input list includes P9's analytic chart/agreement and normalised axial-gauge description for the frame construction. |
| I:19023,19069,19079–19089,19126 | `4.5:prf-lattice-stokes` | P9 makes the base-1 chart holomorphic on (172); T1 identifies the real minimiser under the curvature/cube thresholds; identity continuation gives the fine-frame identity and analytic map. |
| I:19327–19337 | `4.5:lem-window-minimiser` | Uses T1's unique critical orbit after checking the restriction is critical and lies in (6), at `ε₀=O(1)B₃²ε₁^[15]≤a₀`; identifies the global restriction with the window minimiser. |
| I:19806 | `4.5:thm-operator-bounds` | (F2) uses the derivative-decay content of (K8), display `4.5:eq-chart-variation-decay-b`, for localised chart variations and current, at rate `c_*δ₀`; this is mediated through the free-current chart result. |
| I:19876,20110–20123 | `4.5:rem-size-conditions` | Explicitly tracks T1's cube cap `M′≤R₁ mathfrak M a₁/ε₁`; applies it to the small regularity cubes, not to cube side M in the uniform-increment proof; at base 1 the cap is vacuous. |
| I:29558–29565 | `4.7:not-true-pairs` | Uses P9 through CMP109 (1.17) to obtain the fine plaquette bound `2B₃α₀′ξ²` and the corresponding current estimate, with no domain-size factor. |
| I:29274–29277 | `4.7:not-step-constants` | Imports the constant of P9's (172) data radius into the second radius ceiling, distinguishing it from the other constants called C₁. |
| I:29325–29333 | `4.7:not-shift-fields` | Uses the base-1 P9 neighbourhood `sup|B|≤½C₁^(172)barε₁` for off-window data, while explicitly distinguishing it from the stronger Mα₀-proportional datum bound. |
| I:30883–30911 | `4.7:prf-lemma-four-gaps` | Uses P9's sup-Lipschitz H/gradient bounds, localised by (190), for `D=τQ_j(L^{-1}ηH_{k+1})`; pays the bound `B₃²O(1)Mα₀<½α₁`. |
| I:32244–32252 | `4.7:prop-beta-extraction` | Hypothesis (A3) is P9/(190) at real background 1, including derivative and second-order-operator members; used to bound the extraction functional. |
| I:32532,32606–32619,32703–32706 | `4.8:not-regularity-spaces` | Uses P9 via CMP109 (1.17): layered averaged-data curvature `<2α₀′(L^pξ)²` gives the minimiser curvature/current `2B₃α₀′` bounds on `tilde X^{-2}`. Its complex-data applicability is explicitly taken as printed. |
| I:32897,32964 | `4.8:def-tower-rules` | T1 defines the axial depth-n minimiser for each admissible tower rule; uses dependence on tower and datum to establish that the maps read only `U|_Z`. |
| I:33245,33269 | `4.8:lem-class-properties` | P9 continuity/analyticity of the finitely many tower functions makes strict tower inequalities relatively open. |
| I:33620,33679–33682,33792 | `4.8:prf-near-case-labels` | Uses T1 uniqueness for the inner sub-problems, P9 continuation at complex D, and uniqueness to identify the identity-data axial minimiser as 1; establishes both halves of the near tower clause. |
| I:34064,34149–34159 | `4.8:prop-small-pairs` | Uses T1/P9/CMP109 (1.17) under both tower rules at every `(p,Z)`, cube letter `M/L`; bounds are `2B₃ μα₀′ ξ_p²` and `2B₃ μα₀′(L^nξ_p)²`. Requires `2B₃α₀′≤α₀`. |
| I:34718,34738 | `4.8:lem-layerwise-bound` (following membership discussion) | Names T1 and admissible-tower locality as inputs of the orbit-form re-minimisation theorem used for the straddling producer; the complex locality alternative is separately said to be unproved. |
| I:36231–36252 | `4.9:rem-twist-complex-factor` | Uses the T1 constraint-space/regularity description when explaining that twisting the complex factor preserves the unitary cube gauge; the data and configuration clauses remain distinct. |
| I:36508,36649–36680 | `4.9:prop-real-backgrounds` | Directly cites `4.9:thm-minimal-orbit`: applies it at `ε₁=2ε₀`, with its enlarged-cube class and size ceiling, to supply ambient cube gauges; then treats lower levels. |
| I:36914–36932 | `4.9:rem-seed-remarks` | Reuses T1's `B₃` and decreasing cube ceiling; explains the scope of the real-background gauge claim and why a single fixed smallness parameter does not cover arbitrarily large cube sizes. |
| I:37332–37334 | `4.9:prop-ambient-condition` | T1 uniqueness identifies the local minimal orbit with `U_R|_{X″}` after checking (6),(7); the following hypothesis supplies the gauge comparison. |
| I:37907,37956,38043–38045 | `4.9:lem-thin-cube-gradient` | Assumes T1 (8)–(9) for trivial nests and uses it in the real-background seed clause; general nests instead use CMP99a Proposition 6. |
| I:38511–38529 | `4.10:def-minimiser-continuation` | T1 gives real regular minimisers, `ε₁≤barε`, and unique critical orbit under `B₃ε₁≤ε₀≤a₀`. |
| I:38535–38583,38604–38632 | `4.10:def-minimiser-continuation` | P9 supplies holomorphic logarithmic charts on the strict (172) domain, single-valued continuation, real-data agreement, and covariance/gauge extension; packages them as `4.10:eq-minimiser-continuation-a` (P9.1–P9.4). |
| I:38645,38667 | `4.10:def-tower-quantities` | Defines complex tower quantities by the P9 continuation wherever the averaged datum belongs to its chart domain. |
| I:39094–39098 | `4.10:prop-continuation-open` | Uses P9.1's open strict data domain and local logarithmic charts to obtain openness of the continuation domain. |
| I:39176–39177 | `4.10:thm-existence-set` | Assumes P9.1/P9.2 to prove openness/holomorphy of the tower existence set. |
| I:39285 | `4.10:cor-representative-analyticity` | Explicit P9 input `4.10:eq-minimiser-continuation-a` supplies analyticity of a chosen representative. |
| I:39465–39476 | `4.10:rem-representative-assumptions` | Uses the meaning of existence in the P9 continuation domain S(T) to explain the presupposition behind the tower clause, for both the complex representative and its real factor. The additional real-data conclusion at 39480–39485 is expressly unused in that section. |
| I:39499–39500 | `4.10:cor-orbit-extension` | Uses P9 continuation and (181) to extend orbit statements to the gauge-saturated domain. |
| I:39571–39637 | `4.10:rem-single-valuedness` | Uses P9's unique analytic solution and gauge covariance to identify overlapping chart representations; explicitly discusses the domain clause `|B(c)|<π`. |
| I:39941–39943 | `4.10:prop-tower-clause-open` | Assumes the first two P9 clauses via the display alone to obtain openness of the strict tower inequalities. |
| I:40109–40112,40159 | `4.10:cor-class-openness` | Uses that same P9 display and the preceding proposition to conclude relative/class openness. |
| I:40219–40223 | `4.10:rem-radius-ceilings` | Uses T1/§G's data threshold only in the definition of admitted real data, and distinguishes it from the class radii `a₀,a₁,γ₀`. |
| I:40422–40428 | `4.11:def-tower-rules` | Uses T1 at real data to define the unique axial minimiser for a determining set, and P9 for complex data. |
| I:41518–41536,41601,41624 | `4.11:prop-natural-witness` | Assumes T1 existence/uniqueness and P9 analytic Landau response; applies T1 to real data `D_T^{t,Z}(U)` satisfying (7), then P9 to the factored twist in its `b_H` polydisc. |
| I:41831 | `4.11:lem-idempotence` | Uses T1's constrained-minimiser uniqueness to identify the minimiser reconstructed from its own averages. |
| I:41942 | `4.11:rem-no-composition` | Uses uniqueness of the minimal orbit to discuss what can be identified from matching constraint data; does not infer a general composition rule. |
| I:42094–42097 | `4.11:thm-clause-reproduction` | Explicitly assumes the T1/P9 inputs supplying the factored data twist and analytic response in the natural-witness construction. |
| I:42209–42225,42347 | `4.11:prop-one-layer-clause` | Assumes T1 in its CMP109 form: `ε₁=2α′(L^tξ)²≤a₁`, then curvature `<2B₃α′ξ²` and current `<2B₃α′(L^tξ)²` on regularity cubes. |
| I:42361–42363,42397–42413 | `4.11:prop-perturbative-clause` | Assumes P9 analyticity radius `b_H` and layered (190) response bounds; applies them to the real minimiser base and the complex factored datum to control the perturbative tower correction. |
| I:43122–43152 | `4.12:def-constrained-minimisers` | Repackages T1 at the determining set's local block scale: existence/regularity and unique critical orbit; display `4.12:eq-constrained-minimisers-b`. |
| I:43158–43190 | `4.12:def-constrained-minimisers` | Repackages P9/(190) at base 1 for real data in a block-sum norm: `sup|b|<b_H`, response field/gradient/second-order bounds; display `4.12:eq-constrained-minimisers-c`. |
| I:43380 | `4.12:def-consumer-radii` | Uses existence under display (b) to define the reblocked minimiser/consumer quantity. |
| I:43564 | `4.12:def-coupling-thresholds` | Imports `b_H,B_H,c_d,δ` from the P9/(190) response display to set the coupling ceilings. |
| I:44001,44050–44053 | `4.12:lem-minimiser-covariance` | Uses T1 regularity and uniqueness via display (b) to identify the gauge-transformed constrained minimiser. |
| I:44168,44248–44255 | `4.12:prop-reblocking-inside` | T1 gives `U_E(p,X″)` at `ε₁=2 tildeα₀,k ℓ_p²`, after checking the datum bound; uses its curvature/current bounds. |
| I:44543–44561,44636–44643,44704 | `4.12:prf-below-slot-level` | Uses T1 at `ε₁′=5c_Q a_max` and P9/(190) at base 1 for `sup|b|<b_H`; at a site of consumer level `n<p`, converts response/gradient/`D*D` bounds into local plaquette/current bounds. |
| I:58943 | `4.38:prf-polarisation-limit` | Uses T1 uniqueness of the regular minimal orbit to obtain rotation covariance of the minimiser; differentiates at V=1 and passes to the infinite-volume tensor. |
| I:60661 | `4.38:rem-locality-induction` | Explicitly assumes existence, uniqueness among regular configurations, near-identity analyticity and linearisation bounds of the minimiser when defining the unpointed coefficient/exhaustion limit. The prose cites T1 for this combined input; analyticity is P9 content. |
| I:88523–88526 | `4.22:rem-gauge-representatives` | P9 identifies axial and Landau representatives of the same orbit and the normalised map between them, clarifying the background representative. |
| I:88639,88655,88781–88784,88865–88869 | `4.22:lem-axialising-map` | Assumes P9 for the orbit identification and P9/(190) for exponential decay of the layer's profile; applies this at real data/full layer and then to the analytic map. |
| I:120941–120943,121133–121136 | `4.26:prop-near-pairs-outside` | Uses the P9/CMP109 H-bound constant `B₃(d,L)` in the near-pair radius condition; keeps its L-dependence explicit in the `C₁/C₀` floor. |
| I:125387–125391 | `4.26:not-arrest-conventions` | T1 bounds the designated current/curvature entries by fixed `(d,L)` multiples of the frozen-level `ε_ℓ`. |
| I:128914–128925 | `4.26:prf-plaquette-current-entries` | Uses T1 with CMP109 (1.16) at every admissible structure/index to control the normalised current entry by `ε_ℓ`. |
| I:147456–147475 | `4.29:lem-localisation-exact` | Hypotheses include T1 minimisers/unique critical orbits for the local determining set and P9 applicability within the sup-neighbourhood of `W₀=M′U⁰`. |
| I:147514–147542,147571 | `4.29:lem-localisation-exact` | P9 represents the two endpoint minimisers relative to `U⁰`; T1 uniqueness identifies restricted endpoints, and the factored/interpolated datum remains in the P9 neighbourhood. |
| I:147710,147725,147738–147743 | `4.29:lem-collar-staircase` | Hypothesis (dec) is the summed (190) bound in local units, `e=0,1,2` including `D*D,Δ`; P9 data must be in its polydisc, and evaluation points have determining-set level j. |
| I:147816,147848–147852,147915 | `4.29:lem-collar-staircase` | Applies P9 to `B′,W₀,U⁰|_{Λ_j^~}` and (190) at evaluation level j, with factors `ℓ_j^{-1−e}`; Landau gauge lets the same estimates control `P₁H′`. |
| I:148819,148828–148832,148894–148902 | `4.29:prop-window-minimiser` | Hypothesis (4) assumes unique critical orbit at radius `a₀`; the proof applies it to the truncated determining set with witness size `ε₁′=2L²B₃ε₁^g`, after checking regularity of `U_{k+1}` at size `B₃ε₁^g`. This is a content use without the B-CMP102b token. |
| I:148973–148985 | `4.29:def-path-length-decay` | Hypothesis (I1) uses the layered response-decay content, weighting H by `ℓ_a`, its gradient by `ℓ_a²`, at `a=min(n(y),k)`; fixes the response decay exponent. |
| I:149837–149843,149961–149966 | `4.29:lem-scale-thresholds` | Uses P9 polydisc and derivative decay for directions supported outside `E⁺`, `E=tilde□²,tilde□³`, with `e≤2`; uses analyticity of H to obtain clause (τ4). |
| I:150100,150119–150124,150180,150282 | `4.29:lem-interpolated-field-bounds` | Assumes P9 for `B(t)=Q′(ηtH_k)`, `|t|≤1`, and the kernel form of (190); applies it at the local evaluation level to bound interpolated fields and derivatives. |
| I:150413–150416 | `4.29:prop-near-field-scope` | Hypothesis is precisely the directional-derivative kernel form of `4.29:eq-collar-staircase-a`, with `C_ker,c_Q`; uses the (190) content without repeating its citation. |
| I:151264,151323–151328,151402,151420 | `4.29:rem-transfer-inputs` | Identifies H_j as P9's H′ for `B′,W₀,U⁰`; applies (190) at the evaluation element's level. For the window's own set this holds only on `□_j`, explicitly not all `□₀`. |
| I:151767,151773,151917–151918,151938 | `4.29:rem-constants-order` | Imports P9/(190) decay/polydisc constants; distinguishes the response's data-size `ε₂` from a fixed absolute radius and orders the thresholds accordingly. |
| I:154052–154066,154134–154140 | `4.31:def-standing-inputs` | Assumption (e) is T1 (7)–(10) for full-torus nests: regularity `B₃ε₁`, cube gauges for `M′≤R₁M₁a₁/ε₁`; uses uniqueness for translated partitions. |
| I:154690–154693 | `4.31:prop-fixed-depth-convergence` | Hypothesis (I5) requires T1's cube regularity on every aligned local-background window `□₀`. |
| I:155046–155079,155092 | `4.31:lem-window-characteristic` | Uses T1 regularity at size w, with `w≤a₁`, `B₃w≤ε_k`, to make `χ_k=1` on `V_s(w)` (in particular `w_s+16r_s`). |
| I:155104 | `4.31:lem-charts-gluing` | Uses the real-background T1 display at `ε₁=w_s` to glue the local charts. |
| I:155248,155278,155321,155339 | `4.31:lem-background-membership` | Uses T1 real cube regularity and its allowed half-side `M″`, together with nesting, to verify background membership under changes of units. |
| I:155647–155657,155690–155691 | `4.31:prf-marginal-cube-gauge` | Uses T1 (9) at `j=k`, `ε₁=w_s`, and the (S1) cube conditions; combines the gauge bound with `32M′h_s≤1` to control the complex marginal. |
| I:155866,155956–155989,156040–156067 | `4.31:prf-marginal-minimiser-path` | Uses the local analytic-minimiser content (W1),(W2): H is holomorphic for `sup|D|<β_W`, represents the real orbit and vanishes at zero. Takes `|τ|<R′_X`, so `sup|τD|<β_W`, to obtain a holomorphic minimiser/current path. The immediate source is the stronger local complex-background construction, rather than a fresh P9 citation. |
| I:157470–157481,157521 | `4.35:prop-gauge-fixing` | Hypothesis (B) is T1 existence, regularity, uniqueness and cube gauges; applies the cube-size condition in the gauge-fixing construction. |
| I:158215–158216,158232–158252 | `4.36:not-flow-thresholds` | Imports T1 smallness constants and P9's (172) constant for the local minimiser/action and the one-link admissibility threshold (t8). |
| I:160157–160174,160187–160201,160288–160303 | `4.36:def-unit-directions` | P9 gives analytic one-link continuation with `B=ζT′`, `|V′−1|<C₁^(102)ε₁`; defines the permitted radius `r₀`, real agreement and Lie-algebra-valued response. |
| I:160601,160617–160638,160734–160738 | `4.36:lem-broken-paths` | Uses T1 minimisers and P9 continuation for broken one-link paths, with `a₁′`, the (172) constant and radius `r₀` fixed by (t8). |
| I:160800–160825,160840 | `4.36:lem-broken-paths` | Uses T1 plaquette regularity and the first (190) response bound along the one-link path; checks the small relative datum stays in (172). |
| I:160924–160969,161262 | `4.36:rem-normalisation-inputs` | Uses P9 for the one-link complexification and (190) to measure the resulting response with the specified input/output conventions; separates regular-base curvature from the variation. |
| I:161303,161324–161330,161465,161672 | `4.36:lem-one-link-curvature` | Uses P9's continued H_ζ and (190) to control the plaquette variation, respecting representative/gauge changes and the one-link radius. |
| I:161723–161724,161789–161843 | `4.36:rem-curvature-readings` | Explicitly combines (190) for the response with T1 (8) for base curvature and (172) for the window; identifies which member carries `x_k`. |
| I:161964–161975 | `4.36:rem-frozen-background` | Uses (190) with the specified input/output normalisation and T1 (8) for the frozen real-background curvature. |
| I:163160,163174 | `4.36:rem-order-of-choice` | Uses T1's `B₃(d,L)` in the ratio-of-radii floor and discusses the SU(N) reading of its dependence. |
| I:163377,163438 | `4.36:not-sun-conventions` | Imports the P9 (172) constant and T1 smallness constant into the SU(N) threshold notation. |
| I:163795–163834,163932 | `4.36:not-probing-direction` | Uses the (172) relative-data radius and (190) response to the unit direction `ζT′` at bond b₁; keeps the frozen-base and data variation distinct. |

### Clear uses in II

| Location | Using statement | Content used |
|---|---|---|
| II:2165–2168 | `5.1:def-admitted-inputs` | T1 supplies regularity of the term's own minimiser for the coercivity/positivity input, under `M₁α₀,k≤a_X(d,L)`. |
| II:3996–3998,4044 | `5.2:prop-box-comb-gauge` | Uses P9's `B₃` in the comb bound `2(α₂+B₃O(1)Mα₀)` and P9 at base 1 in nested-box containment/admissibility. |
| II:4149–4150 | `5.2:rem-own-box` | Attributes the quoted own-box bounds to P9 through CMP109's argument. |
| II:4608,4662–4668 | `5.2:lem-extraction-cost` | P9/(190), including the derivative and second-order members, bounds the free response `‖h_x‖≤B₃e^{−δ₀dist(x,X)}`; Cauchy radius is `r_j` (absolute part `r_○`), yielding the extraction constant. |
| II:9004 | `5.2:lem-random-walk-bounds` | Uses T1 (9)–(10) regularity of the minimal configurations as the background input to the walk estimates. |
| II:9407–9411 | `5.2:lem-almost-invariance` | T1 unique critical orbit identifies `U=U_B(M_BU)` when more constraints are imposed, allowing the effective minimum action to be expanded at its own data. |
| II:10231–10237,10322–10323,10344,10365–10369,10434 | `5.2:cor-true-pair-positivity` | T1 gives regularity `α₀(γ)=O(1)B₃L²(1+β₀)sup ε_i`; verifies the cube-size/smallness conditions on the characteristic-function support for coercivity at true pairs. |
| II:10608–10610 | `5.2:lem-response-containment` | Hypothesis (c) is the layered response-shift estimate resting on P9/(190), taken by statement, for layers `n≤k`. |
| II:13717 | `5.2:lem-animal-resummation` | Chooses `c_h` as half the least of the published smallness constants, including T1/P9, so resummed inputs remain admissible. |
| II:17530–17533,17551–17553 | `5.2:def-plain-interior-units` | Identifies the core read with the minimiser at its level-j datum and uses P9 at `V₀=1` to justify the box-minimiser reading. |
| II:34841 | `5.5:def-weight-constants` | Imports T1/P9 smallness constants into `c_h` and the common ceiling on `A_w(γ)`. |
| II:35582–35587 | `5.5:lem-weight` | Uses T1's constraint-fixing gauge orbit: gauge maps are 1 at block base points, making the gauge factor local to each block; the identity persists analytically. |
| II:35633,35647–35652 | `5.5:prf-box-regularity` | Uses T1 uniqueness for the minimiser of Q; smallness is bounded by `2.8 A_w(γ)` and paid by `K_loc A_w(γ)≤c_h`. |
| II:35669–35675,35705–35706 | `5.5:prf-box-regularity` | P9 at identity gives `U_p(Q,e^{iB})=(e^{iηH(B)})^u` and the regularity estimates in the box's own level-p units. |
| II:43034,43096,43124–43143 | `5.5:def-remainder-constants` | Uses T1/P9 `B₃` and radii `a₀,a₁`; requires actual data size `ε₁′≤2B₃ε₁^top`, and uses `B₃a₁≤a₀` to place the remainder chart in the uniqueness class. |
| II:43653,43675–43680 | `5.5:prf-box-field-charts` | P9 makes Y(B) analytic on O; T1 identifies the restriction as the critical orbit of its own `B_j(r_v)` datum Φ(B), with smallness from the remainder constants. |
| II:44016–44021 | `5.5:thm-membership-remainder` | P9 analyticity of `(U,J)(B_j^*,V)` allows the two stored-remainder data presentations to be compared on their chart domain. |
| II:44402–44405,44415–44420 | `5.5:cor-thin-layers` | T1 identifies the local critical orbit with base-point-normalised gauge; P9 regauges the small datum `e^{iB_u⁰}` into `e^{iξH}` under the `α₃,j` bound. |
| II:50317–50320 | `5.7:prop-response-zeroth-order` | P9 holomorphy of both response maps on `D(a_Λ)` makes the paired maps holomorphic into E. |
| II:50809–50812 | `5.7:not-canonical-loops` | Uses P9 analyticity about real `V₀₀` on a ball containing both B₀,B₁, under the two-machine response hypothesis. |
| II:50918–50923 | `5.7:lem-native-loop-closeness` | T1 (9) bounds curvature on both lattices by `Cεℓ_i^{-2}` and its Hölder quotient by `Cεℓ_i^{-2−β}`. |
| II:52177–52181 | `5.7:prop-critical-layer-closeness` | P9 supplies holomorphy on the right side of the layer identity; equality at real points extends to the complex ball. |
| II:58995 | `5.9:def-variation-hypotheses` | Uses T1 (with covariance (181)) as a stated input of the absolute chart/low-order variation setting. |
| II:59247–59250 | `5.9:thm-low-order-variation` | Uses uniqueness/flatness of the critical orbit at flat data, citing P9/(181), to normalise the flat value. |
| II:69929,70014–70016 | `8.1:lem-kernel-bounds` | Hypothesis (h1) invokes T1 (9)–(10) for the linear-minimiser kernel; uses it with the free-current theorem for background covariance and tower-step decay. |
| II:71256–71261 | `8.1:rem-extraction-errors` | Applies T1 at the top scale for the displayed order-η² observable bound, with constant proportional to `B₃²a₁²`. |
| II:75244–75252,75356 | `8.2:lem-curvature-contraction` | Hypothesis (I) uses a stated consequence of T1 (8)–(10) for every level/window and every torus exponent, with `B₃` independent of depth/volume; uses it in the contraction estimate. |
| II:85642,85655–85657 | `8.4:not-step-zones` | Defines the minimiser for the step and the regularity condition on zones, including the interface convention of (7); this is the T1 applicability setting. |
| II:85786,85794–85796 | `8.4:not-box-variation` | Imports (190)'s H/distance and constants `a₀,a₁,B₃,B₅,δ₀,c_*` for the box response. |
| II:85913–85956 | `8.4:def-response-hypotheses` | Explicitly reads `8.4:thm-minimiser-analyticity` with fixed-gauge base, single-bond differentiation, base-covariant gradient, and pointwise validity throughout (172), containing `sup|B|<a₉`; constants are geometry/depth independent. |
| II:85974–85987 | `8.4:def-response-hypotheses` | Hypothesis (c1) transfers T1/P9/(190) to the step's determining set `B_j` when `(7^flat)(barε)` holds, `barε≤a₁`; deep fixed zone-zero plaquettes do not enter the unknown minimiser. This transfer is assumed. |
| II:86161 | `8.4:def-far-member-hypotheses` | Uses lower-zone T1 (9)–(10) regularity as the comparison for the datum restrictions. |
| II:86291–86300 | `8.4:not-decay-weight` | Uses (190)'s multiscale distance and its assumed comparison with either `dist_j` or scaled path distance to define the response weight. |
| II:86786–86807 | `8.4:lem-far-member` | Hypotheses explicitly assume `8.4:thm-minimiser-analyticity`, the T1/P9 transfer, and the distance comparison; uses `x∈Δ(y_x)` and localised data bonds. |
| II:86835,86866 | `8.4:lem-far-member` | Requires the varied data to stay in `sup|B|<a₉⊂(172)` and identifies the gradient member of (190) with the base-covariant derivative. |
| II:86904–86912 | `8.4:lem-far-member` | Applies T1/P9 to base data `(B_j,V^base)` to obtain a unique real axial base and its analytic response. |
| II:86983–87002 | `8.4:lem-far-member` | Writes the top-zone-only variation as `V′V^base`, `supp V′⊂S(I)⊂Γ_j`, `sup|B|<a₉`; uses P9 to compose H(B(y)) holomorphically on the source tube T. |
| II:87015–87022 | `8.4:lem-far-member` | Uses real-data agreement/Landau-gauge representation with a base independent of B to relate the varied real minimiser to `exp(iηH)U₀`. |
| II:87078–87094,87156 | `8.4:prf-far-member-proof` | Uses both members of `8.4:eq-minimiser-analyticity-a` at every point of the analyticity domain, data level j, observation level n; obtains size/decay with factors `L^{-n}`, `L^{-2n}` and rate from `δ₀/8`. |
| II:88384–88389,88428–88435 | `8.4:rem-own-scale-smallness` | Reuses the theorem's whole-determining-set base regularity and relative-variation smallness; explains that the large-field application requires the assumed transfer `(7^flat)`, not smallness of the observed plaquette alone. |
| II:95939–95969 | `8.5:def-critical-backgrounds` | Defines `R(S;ε′)` using restrictions of T1 minimisers, `0<ε′≤a₁`, with admissible nests and the stated (7) hypothesis; sets the allowed special-cube size M_Q. |
| II:96003–96034,96061–96122 | `8.5:lem-background-regularity` | Uses T1 (2),(8),(9) at top level n and `ε₁=ε′` to obtain regularity `B₃ε′`, box-data regularity and the cube gauge on size `2M_Q` when its enlarged cube lies in `C♯`. |
| II:96156–96159,96224–96234 | `8.5:lem-vacuum-subtraction` | Assumes analytic dependence of the box minimiser/current on `|B′|<α₃,j`; uses it on `|σ|<Σ=α₃,j/sup|B^ax|` for the vacuum-subtraction Schwarz estimate. This is P9 analytic-minimiser content mediated through the correlation theorem; the additional membership in `U_j^flat(X)` is part of that stated hypothesis, not supplied by P9 alone. |
| II:97407–97412 | `8.5:lem-insertion-sup` | T1 gives `U_B′(V′)∈U_n(B₃ε′)` over `C_i♯⊂Ω_n′`, supplying the background regularity in the insertion supremum. |
| II:97568–97571 | `8.5:thm-averaged-extraction` | Explicit hypothesis (b) is T1 regularity, used with the listed CMP109/116/119 input estimates. |
| II:99758,99774–99778,99804–99806 | `8.5:lem-minimiser-regular` | Uses T1 (9)–(10), linear in `ε′≤a₁`, to supply conditions (c1)–(c3), including the comb Hölder remainder with coefficient `B₄Mc_d`. |
| II:101126–101128 | `8.5:lem-branch-comparison` | Hypothesis (1) is the localisation-of-minimisers input tracing to P9/(190), used in the paired branch comparison. |
| II:106924–106931 | `8.6:prop-exponential-moment` | Hypothesis (i) is the T1 block-field bound in terms of coarse plaquette size `m≤α_B`, with constants `α_B,C_B`. |
| II:109951–109966 | `8.8:lem-stability-exponent` | Uses T1 by description: “Theorem 1 of the reference numbered 16” in CMP119. Coarse plaquettes `<4g_k`, with `4B₃≤p₀(g_k)`, give fine-minimiser plaquettes `<4B₃g_kη²`, then `g_k^{-2}A(U_k(V))≤C_dB₃²N_k`. |
| II:117626 | `8.10:prop-window-lower-bound` | Explicitly includes T1 variational regularity in its list of source inputs. This is conditional use, not a derivation of the window claim from T1 alone. |
| II:119733–119739 | `8.11:not-units-cap-amplitude` | Uses the tail of (190) to compare the interpolated field with the exterior's own field away from H; curvature is `σε` up to that tail. |
| II:138407–138410 | `8.17:not-top-step-notation` | Defines the background action using the T1 minimiser, continuous on the crude-regular class and its specified bondwise `α_P` neighbourhood. |
| II:139604–139608 | `8.17:lem-crude-short-move` | Uses that minimal-background action for crude-regular `x′` with `sup_b d(x′_b,z_b)≤α_P`, `z∈cl S²_all(e)`. |
| II:139967–139974 | `8.17:prop-short-move-construction` | Hypothesis (i) takes the second-order window bound from P9 analyticity in a relative variable about an arbitrary regular background, with fixed second-derivative constant K₂. |

### Clear uses in III

| Location | Using statement | Content used |
|---|---|---|
| III:1065 | `9.1:not-constant-order` | Uses T1's explicit dependence `a₀,a₁,B₃` on d,L only in the order of constants. |
| III:2194,2345,2389–2390 | `9.1:lem-glued-minimisers` | Assumes T1/P9; uses regularity (9)–(10), criticality and membership in (6) to identify the healed configuration with the minimal orbit. |
| III:2919,2939 | `9.1:prop-hull-step` (following hull-read definitions) | Defines `(U_j,J_j)(X⁺,v)` by T1/P9 and requires v within coupling-independent radius r_c of a real regular datum; the read slice must lie in `D_v[0]`. |
| III:2999,3025–3030 | `9.1:lem-hull-exactness` | Uses the unique real critical orbit and P9 analytic box minimiser on the radius-r_c ball to obtain exact/analytic hull reads. |
| III:6362 | `9.1:lem-slice-displacement` | T1 uniqueness identifies `U_e|_{X⁺}` with the chart point `V(B[U_e])` after refinement of the constraints. |
| III:7265–7269 | `9.1:cor-tolerance-rooms` | Uses P9 response to logarithmic increments `B=(1/i)log V′`, together with the free-current theorem, to bound slice displacement by `|1−s|D`. |
| III:18821 | `9.1:def-seed-criticality` | Uses the T1 variational problem with sub-averages over the seed's own `Ω(R)` as the meaning of seed criticality. |
| III:19103–19106 | `9.1:rem-cellwise-increments` | Uses uniqueness of the critical orbit at given data to make the Landau representative independent of the data-orbit representative. |
| III:19435 | `9.1:lem-core-gauge` | Uses the T1 constraint equation: the local minimiser's averages on the cells of `□^~` return the supplied datum V. |
| III:19882–19884 | `9.1:cor-seed-rotation` | Uses T1 unique critical orbit and identity continuation to identify the rotated seed's complex chart representative. |
| III:22139,22178 | `9.1:def-natural-vertex` | First natural-vertex bound rests on (190) at vertices; the explicit standing-input list includes both (189) and (190) at vertices. |
| III:31748 | `9.2:not-parameters-couplings` | Imports T1's B₃ into the running-radius constants. |
| III:34767–34840 | `9.3:not-minimiser-bounds` | Applies T1 (9),(10) at the two cutoffs `T_η,T_η′`; obtains membership in `U_k(Ω,B₃ε)` and `U_{k+1}(Ω′,B₃ε)`, potentials/gradients and Hölder regularity with B₄(β). |
| III:35173–35176 | `9.3:lem-gauge-fixing` | Hypothesis takes `U₀∈U_k(Ω,α₀)`, the T1 regularity class, in addition to CMP99b (3.35); gauge-fixing applies relative to that base. |
| III:35740–35749 | `9.3:thm-stationarity-minimisers` | Directly applies `9.3:prop-second-variation`/189: test form supported in `tildeΔ(y′)`, potential in (77), observation in `Δ(y)`, to control the local Hessian of V. |
| III:35794–35796 | `9.3:thm-stationarity-minimisers` | Distinguishes the full-torus case: (98) replaces (189) when all `Ω_j=T_η`; the rest of the argument is reused. Thus the full-torus variant is not an additional use of (189). |
| III:35913–35916 | `9.3:cor-stationarity-level-data` | T1 gives `U_B∈U_k(Ω,B₃ε)` and curvature `≤Cεℓ^{-2}`, used in the perturbative curvature/action comparison. |
| III:36002–36007 | `9.3:not-perfect-action` | P9 at real `V₀` regular with `ε=a_A/2`, with `C₁ε₁≥r_c`, makes `V↦U_B(V)` analytic on `D(r_c)`. |
| III:36252–36256 | `9.3:thm-stationarity-jets` | Directly uses `9.3:prop-second-variation` (integrated Hessian content) for `|V′(A_W′)|_{−3−θ}≤Cε₂‖A_W′‖_θ`, then the stationarity estimate for `A_W′`. |
| III:36300–36314 | `9.3:thm-stationarity-jets` | P9 provides the induced variation of the minimiser; the first (190) member, explicitly through `9.3:prop-second-variation`, bounds it on a level-j′ block with decay rate `δ₀/8`; pairs it with the current in the action derivative. |
| III:36721–36728 | `9.3:thm-stationarity-covariance` | Calls the input “second-variation bound” and cites the proposition/(190) for `|∂_c V^(k)(c₁)|≤Ce^{−δ|c−c₁|}`; Cauchy at tube radius r supplies second derivatives. The wording/citation mix is retained, not silently corrected to (189). |
| III:36974–36990 | `9.3:lem-refinement` | Uses T1 regularity under a refined/shrunk sequence and applies T1 to refined data at size `2B₃ε`; uniqueness identifies the refined constrained minimal orbit. |
| III:37006–37015,37026–37030 | `9.3:lem-response-decay` | P9 on `D(r_c)` about regular data of size `a_A/2` gives analytic `H(tB)`, with `sup|B|<r_c`, and `H(0)=0`. |
| III:37042–37048 | `9.3:lem-response-decay` | Uses the first two (190) members uniformly along `tB`, supported in S; integrates to get field/gradient decay with `ℓ^{-1}`, `ℓ^{-2}` and rate `δ₀/8`. |
| III:37147–37152 | `9.3:prf-local-backgrounds` | Uses that P9/(190) response content through `9.3:lem-response-decay` on the refined determining set, for `V²=e^{iB}V¹`. |
| III:37324–37330 | `9.3:rem-large-field-regions` | Reuses the same response-decay lemma at the refined determining set for `sup|B|<r_c`, `supp B⊂S`, to compare backgrounds beside large-field regions. |

### Ambiguous mentions, proposed routes, negative uses and inventories

These are not silently counted as applications of the four printed results.

| Location | Statement/context | What the text does |
|---|---|---|
| I:10065–10072 | `4.4:def-group-factor-bounds` | Rejects the route via P9/CMP109 giving `2B₃α₀′`: it cannot supply the desired post-step bound without an unassumed `4B₃≤L²`. |
| I:15931–15951 | `4.5:rem-condition-iv` | Quotes the P9-derived (1.17) bounds, then lists three routes to (iv) that the book does not use; contrasts curvature and potential data sizes. |
| I:16701–16703 | `4.5:prf-increment-kernel` | Explicitly says P9's extended-configuration bound (19)–(21), `ε₂=B₅barε₁`, is **not used here**. |
| I:20141–20142 | `4.5:rem-not-asserted` | Lists fourth/fifth (190) members at independent free current and off-diagonal (21) among claims not asserted. |
| I:34928,35007–35018 | `4.8:rem-literal-inclusions` | Uses the P9-derived constant in an analysis of a possible literal inclusion: closure would require `4B₃(1+β)≤L^{2g}`; the remark expressly says these observations are not used in the named class proofs. |
| I:45179–45190 | `4.13:lem-minimizer-unique` | Proposed route from T1, proof outstanding: still must show all admitted fields meet its hypotheses, every minimiser lies in its uniqueness class, and orbit uniqueness gives uniqueness of the required representative. |
| I:44893,44936–44963 | `4.12:rem-refined-minimiser` | Discusses an unused refined-minimiser identity. It uses the T1/P9 response displays to explain why a different local estimate suffices and why the alternative sharp-data route does not close. |
| I:131690–131692 | `4.27:lem-t-step-layer` | Identifies the real layer with P9's H, but explicitly says P9 is **not applied**: its CMP99b (3.35)–(3.38) hypotheses are not supplied. Bounds come from the separately assumed background-field layer theorem. |
| I:155507–155512 | `4.31:rem-non-minimiser-data` | Discusses a possible derivation of (iv) from P9 with datum entering only through β_n; the actual membership proof uses nesting instead. |
| I:154200–154230,154275–154291 | `4.31:def-complex-background` | Local (W1),(W2) share P9's analytic-minimiser/real-agreement content on `sup|D|<β_W`, but add normalised uniqueness and local bounds from the complex-background construction. The proof uses that uniqueness to obtain constant-conjugation covariance. The explicit CMP102 citation here is (181), so attributing the entire strengthened local assertion to P9 would be ambiguous. |
| I:164436,164531 | `4.36:prf-regular-absorption` | Mentions real points/complex-ball comparison “as in CMP102”; no particular T1/P9/(189)/(190) clause is identified at those tokens, so these are only possible analytic-method analogies. |
| II:54241–54243 | `5.8:rem-kernel-rates` | Explicitly says the lower-rate (190) H-derivative is absent from the kernel chain and is used neither there nor in the smeared-datum majorant. |
| II:54659–54660 | `5.8:prop-local-decay` | Explicitly excludes the (190) operator from the family `mathfrak L`; the invoked kernels are instead from (71),(73). |
| II:114770 | `8.10:def-window-structure` (route discussion) | Says regularity of the local minimiser should come from T1 and that B_W still has to be extracted; a stated route, not a verified application giving that constant. |
| I:166573,166633 | Unlabelled Chapter 4 dependency inventories | Lists T1/P9 among inputs; these are inventories, not uses in `4.36:lem-monotone-substitution`, the last preceding labelled statement. |
| II:60248–60253,60315 | `5.13:prop-sun-correlation` | Inventory of source results used in extending the correlation theorem to SU(N), including T1, P9 and (190); other CMP102 equations in the list are different inputs. |
| II:145545–145547 | Dependency inventory associated with `8.21:cor-consequences-torus` | Lists T1 (6)–(10), P9/(190), (172),(182); gives source/dependency attribution rather than a new kernel estimate. |
| III:75776–75781 | Unlabelled Chapter 9 input inventory | Lists T1, P9, and (189)–(190), alongside Propositions 3,5,6; not a use in the last preceding labelled remark. |
| III:110946 | Unlabelled Chapter 11 synthesis | Reports T1 regularity as an input of the variational analysis under the stated restrictions. |
| III:111362 | Unlabelled Chapter 13 inventory | Lists the passage between (189) and (190) as an outstanding/incomplete input. |

### Citation/content boundaries checked

The full `B-CMP102b` concordance also contains references solely to: geometry (1)–(7), block/gauge conventions, the averaging correction and kernels (39)–(73), force/Hessian formulas (74)–(111), propagator construction (120)–(143), axial-gauge construction §F/(145)–(163), variational identities (170)–(181), and standalone Propositions 3,5,6. Those are not by themselves uses of T1, P9 or (189)–(190). Where one of those passages also invokes the target content, its consuming statement is included above. In particular gauge covariance (181) alone has not been relabelled as P9 analyticity.

## Search terms and confidence in completeness

Each family was searched across all three source files, then the relevant matches were read in small surrounding ranges. A streaming label index was used to locate the enclosing statement; multiline titles and unlabelled status lists were checked separately. Equation searches followed the restatements of the requested results, rather than stopping at the original labels.

| Item | Search terms used | Confidence |
|---|---|---|
| (1) Uniform increment | `4.5:lem-uniform-increment`; `4.5:eq-uniform-increment-a,b`; `uniform.increment`; `increment lemma`; `depth.free`; `C_{IV}`; tower quantities/increments; the radius pair `α₁/8, α₀/C_IV`; later far-case and layerwise-bound passages. | **High** for explicit/name/formula uses. **Medium-high** for all descriptive uses: the distinctive constant and radius pattern are strong anchors, but later generic “increment lemma” occurrences require discrimination from unrelated lemmas. No independent direct match in II/III was found. |
| (2) Own curvature constant | `4.13:lem-own-constant`; `own.curvature`; `own printed`; `small pairs`; `real-background pairs`; `cube gauge`; widened gauge/form; reproduction of the gauge condition; `4.9:cor-printed-pairs`; `4.9:rem-reproduction-meaning`; seed requirement. | **High** for literal/name matches and the explicit duplicated content. **Medium-high** for attribution: the corollary earlier in I supplies the same content independently, while the later lemma remains labelled proof outstanding. A general widened-class hypothesis is not necessarily a citation of that later lemma. |
| (3) Prepared admissibility/pages | `4.14:prop-prepared-data-admissible`; `4.14:eq-prepared-data-admissible-a`; `prepared.large.field`; `admissibility of the prepared`; `178.{0,15}179`; A1/A2; `6M`; layer clearance `Mℓ_j`; compatible M-cube partitions; stage/produced nests; hull and local-ball uses. | **High** for every page citation and explicit proposition/equation use. **Medium-high** for unlabelled geometric-content uses. Generic hypotheses fixing an arbitrary admissible nest are not evidence that the prepared-nest assertion is being applied. |
| (4) Unmarked increment | `4.2:lem-unmarked`; `4.2:eq-unmarked-1`; `unmarked part`; unmarked/increment/bound combinations; `C_{\\mathrm{rem}}`; `C_\\beta`; `β^A`, `β^0`; the ceiling `ε₁^I≤c₀/(2C_rem)`; flow-bound and clause-zero passages. | **High** for actual lemma/bound applications and their parameter ceiling. **Medium-high** for mediated constant reuse: C_β has several explicitly different meanings, so the complete-increment and extraction-functional occurrences are not all assigned to this lemma. |
| (5) CMP102 results | Full `B-CMP102b` concordance; all three local labels; `Theorem~1`, `Proposition~9`, `Prop.~9`; `(189)`, `(190)`; `minimal.orbit theorem`; `unique critical orbit`; minimiser/minimizer theorem; analytic continuation/analyticity of constrained or box minimisers; second-variation/derivative/response decay; numbered-reference descriptions including “Theorem 1 … reference numbered 16”; equations `8.4:eq-minimiser-analyticity-a`, `4.10:eq-minimiser-continuation-a`, `4.12:eq-constrained-minimisers-b,c`, `4.29:eq-collar-staircase-a`, `4.31:eq-standing-inputs-e`, `4.5:eq-chart-variation-decay-b`; local (W1),(W2) analytic-minimiser passages. | **High** for the explicit citations, local-label references and identified restatement displays. **Medium** for absolute completeness of all description-only content uses: these are pervasive through independently stated free-current/local-chart inputs, and an unqualified H or minimiser reference does not uniquely identify a printed CMP102 result. The tables include clear mediated uses and isolate uncertain attribution; they do not claim a mechanically certified exhaustive semantic dependency graph. |
