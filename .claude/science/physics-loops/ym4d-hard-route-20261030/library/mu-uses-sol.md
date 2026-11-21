# Uses of the constrained-minimiser lemma

The label `4.13:lem-minimizer-unique` occurs only at `/tmp/sa_ca_I.tex:45163`; there are no label references to it in the three files. Its content is (a) uniqueness of the constrained minimiser in Balaban's Lemma 4 and (b) locality sufficient to use CMP 109 (3.38) on an arbitrary subdomain. At `sa_ca_I.tex:45199–45201` the author explicitly says that both parts enter the statement on the one-power hereditary class through that arbitrary-subdomain reading.

The tables below distinguish identifiable uses of this content from related statements whose dependence on this particular lemma cannot be established. An occurrence of “Balaban's Lemma 4” alone is insufficient: many such citations use its bounds or analyticity, rather than the uniqueness/locality completion. The complex, graded-tower and global versions below can also require additional hypotheses; listing them does not assert that Lemma 4.13 alone proves them. The source marks Lemma 4.13 **proof outstanding**.

Locations below are absolute source line numbers; filenames abbreviate `/tmp/sa_ca_*.tex`. Multiple anchors in a row identify separate uses within the same statement.

## Uses of the nesting/locality content

| File:line | Statement label | What is used and why |
|---|---|---|
| `sa_ca_I.tex:31072`, `31101–31122` | `4.7:prf-lemma-four-gaps` | Uses (3.38), described as the conjugation lemma for window minimisers, first to obtain condition (iv) from (iii), then at every tower label `(p,Z)` to obtain the one-power curvature/current bounds. |
| `sa_ca_I.tex:32420–32424` | `4.7:prop-coupling-increment` | Explicitly lists the nesting lemma for (3.38), with factorisation `U=1`, among the inputs supporting membership in the induction's regularity class. |
| `sa_ca_I.tex:33610–33623`, `33654–33694`, `33765`, `33790–33794` | `4.8:prf-near-case-labels` (also identifies the input as the first antecedent of `4.8:prop-near-case`) | Assumes and applies sub-tower conjugation on arbitrary `Z`, checks uniqueness of sub-problems, and uses the resulting curvature/current identities to establish the tower clause and half-radius membership; uniqueness also identifies the identity-data minimiser with `1`. |
| `sa_ca_I.tex:34254–34257` | `4.8:prop-class-reproduction` | Its hypotheses explicitly include the hypotheses of the near-case proposition and the statements from which it is derived; this carries the nesting/uniqueness input into the reproduction of the one-power class. |
| `sa_ca_I.tex:121191–121197`, `121435–121467` | `4.26:prf-near-pair-chain` | Assumes a bound on the (3.38) conjugator at every triple and uses the nesting identity there to turn direct entries `1,3` into composite entries `2,4` without rerunning the chain at the lower level. |
| `sa_ca_I.tex:123125–123134` | `4.26:prop-near-pair-graded` | Uses (3.38) at each own triple to carry the direct bounds to composite entries `2,4`, conditional on the full-datum conjugator bound. |
| `sa_ca_I.tex:128569–128576`, `128733–128737` | `4.26:prf-nested-criticality` | Hypothesis (III) supplies uniqueness modulo gauge and identification of the localised minimiser with the restricted background off the boundary layer; clause (d) invokes it. |
| `sa_ca_I.tex:144931–144933` | `4.28:prop-near-pair-box` | Uses (3.38) to treat composite entries `2,4` at the triples of a near pair meeting lifted points. |
| `sa_ca_I.tex:147454–147466` | `4.29:lem-localisation-exact` | Assumes restriction of minimisers and uniqueness of the local minimal orbits to identify both endpoint configurations with local minimisers of their own induced data, modulo gauge. |
| `sa_ca_I.tex:148801–148809`, `148872–148880` | `4.29:prop-window-minimiser` | Assumes criticality transfer/uniqueness and the restriction identity, then uses the latter to obtain the window representation (d1) needed by the cube analysis. |
| `sa_ca_I.tex:151282–151289`, `151386–151392`, `151406`, `151429–151438` | `4.29:rem-transfer-inputs` | Assumes the local reproduction identity; applies it at zero perturbation, at the other endpoint, and on the window to identify the minimisers entering the transferred small-field analysis. |
| `sa_ca_I.tex:151610–151611`, `151631–151632`, `151661–151662`, `151688` | `4.29:cor-cubewise-analysis` | Explicitly retains the subdomain restriction lemma as an input and uses it to identify the cube minimiser and justify entering CMP 109 (3.18) at good cubes. |
| `sa_ca_I.tex:154187–154190`, `154203–154206` | `4.31:def-complex-background` | Chooses the local datum radius to satisfy the nesting hypotheses and specifies uniqueness of the normalised small complex minimiser; this is a complex/local version, with its own construction hypotheses. |
| `sa_ca_I.tex:154339–154420` | `4.31:def-window-counting-nesting` | Imports the nesting lemma as identities (N1)–(N3), displayed in `4.31:eq-window-counting-nesting-c`, for local fields, global-to-local comparison, and arbitrary global domains; explicitly identifies (N1)'s published counterpart as CMP 109 (3.38). |
| `sa_ca_I.tex:154697–154700` | `4.31:prop-fixed-depth-convergence` | Explicitly assumes the nesting identities (N1)–(N3) among its convergence/analyticity inputs. |
| `sa_ca_I.tex:155251–155252`, `155394–155430` | `4.31:lem-background-membership` | Assumes and applies global nesting to compare every local minimiser and its current with `W`, thereby deriving condition (iv) from the direct bounds uniformly in the local depth. |
| `sa_ca_I.tex:155466–155467`, `155509–155511` | `4.31:rem-non-minimiser-data` | Uses nesting as the successful route to condition (iv), explaining why comparison with `W` itself avoids the failure of the datum-only linear estimate. |
| `sa_ca_I.tex:155868–155869`, `156007–156018`, `156047–156057` | `4.31:prf-marginal-minimiser-path` | Assumes (N1)/(N2); (N1) proves condition (iv) along the complex minimiser path, and (N2) identifies its endpoint functional value with that of the original background. |
| `sa_ca_I.tex:156154–156156`, `156210–156214` | `4.31:rem-marginal-uniformity` | Uses the depth-uniform gauge bound in the nesting identities to show that the marginal estimate's constants are cutoff independent. |
| `sa_ca_II.tex:4115–4117`, `4151–4154` | `5.2:rem-own-box` | Uses the box restriction/minimiser-of-own-data representation to extend the local representation to a domain's own box with two layers of margin. |
| `sa_ca_II.tex:4220–4227` | `5.2:rem-chain-configurations` | Applies the own-box representation to preparatory backgrounds and `Phi(b)` to obtain regularity clauses (c1)–(c3) along the chains. |
| `sa_ca_II.tex:13872` | `5.2:lem-animal-resummation` (explanatory mechanism following its estimates) | Uses the assertion that the window restricted to a small box is that box's minimiser to apply the local CMP 109 estimates at the box's actual maximum weight. |
| `sa_ca_II.tex:35641–35655`, `35706–35714` | `5.5:lem-weight`, proof labelled `5.5:prf-box-regularity` | Uses locality plus uniqueness to identify the window restricted to `Q` with its own-data minimiser; repeats the argument for part (a4), expressly identifying the result as (3.38). |
| `sa_ca_II.tex:44066–44078` | `5.5:thm-membership-remainder` | Uses “a minimiser is the box minimiser of its own data” to identify the constructed interpolation configuration with the one in the interpolation formula. |
| `sa_ca_II.tex:96010–96029`, `96119–96138` | `8.5:lem-background-regularity` | Explicitly assumes the box nesting statement and uses it to identify a critical background and its current with the box minimiser/current of their own determining data, including the graded rim. |
| `sa_ca_II.tex:96177–96185` | `8.5:lem-vacuum-subtraction` | Uses that nesting conclusion to rewrite the functional on the background as a functional of a box minimiser, enabling the vacuum-subtraction estimate. |
| `sa_ca_II.tex:96290–96291`, `96381–96391` | `8.5:lem-core-estimate` | Assumes nesting and uses it to identify the box extension of the restricted background with the original background/current, so that the Cauchy-estimate endpoint equals the desired core value. |
| `sa_ca_II.tex:99782–99788` | `8.5:lem-minimiser-regular` | Invokes the restriction lemma for minimisers to identify the global minimiser on `X` with the box minimiser of its level-j averages. |
| `sa_ca_II.tex:101228–101232` | `8.5:lem-branch-comparison` | Uses regularity clause (c1)'s own-data box representation for both backgrounds before comparing their comb-gauge data and remainder readings. |
| `sa_ca_III.tex:2994–3016` | `9.1:lem-hull-exactness` | Invokes re-minimisation of minimisers, displayed as `9.1:eq-hull-exactness-5`, to equate hull reads with restrictions at bracket endpoints and preserve bracket values. |
| `sa_ca_III.tex:5926` | `9.1:prop-dilation-failure` | Uses complex nesting to identify a seed's restriction with the solution reconstructed from its own averages, reducing the issue to the restriction map. |
| `sa_ca_III.tex:6245–6265`, `6345–6358` | `9.1:lem-slice-displacement` | Uses chart nesting to identify a seed's restriction with its local slice; then identifies composite members `E2(p), E4(p)` and condition-(iv) pairs with the original `E1,E3` members. |
| `sa_ca_III.tex:88580–88593`, `88620–88630` | `10.3:lem-real-values-unchanged` | Explicitly assumes the box restriction and box-minimiser identities and uses them to identify the extension reading with the real chain configuration, including boxes astride the boundary. |

## Related uses: attribution to Lemma 4.13 is not established

These are worth reporting in a content search, but they should **not** be represented as confirmed citations of Lemma 4.13. Refinement criticality alone is weaker than its uniqueness/locality assertion, and some passages give a separate argument from CMP 102b.

| File:line | Statement label | Related content used |
|---|---|---|
| `sa_ca_I.tex:34738–34743` | No separately labelled statement; discussion following `4.8:lem-layerwise-bound` | Says the orbit-form membership theorem uses tower locality for every admissible determining set and CMP 102b Theorem 1; explicitly limits that tower-locality statement to real configurations. |
| `sa_ca_I.tex:41830–41833` | `4.11:lem-idempotence` | Uses the unique minimal orbit at fixed admissible data to obtain equal-index idempotence; cites CMP 102b directly. |
| `sa_ca_II.tex:9400–9407` | `5.2:lem-almost-invariance` | Establishes finer-constraint re-minimisation by feasible-set inclusion and uniqueness of the critical orbit from CMP 102b, then defines the minimal action function. |
| `sa_ca_II.tex:40007–40009` | `5.5:thm-own-level-membership` | Uses refinement criticality at the field's own averages to identify the base as critical for the local determining set. |
| `sa_ca_II.tex:52110–52111`, `52162` | `5.7:prop-critical-layer-closeness` | Assumes/applies the own-average refinement statement for critical configurations, rather than explicitly using uniqueness or (3.38). |
| `sa_ca_II.tex:75359–75376` | `8.2:lem-curvature-contraction` | Uses nesting of whole-lattice minimal orbits and uniqueness to identify a composition of one-step backgrounds with a single multi-step minimiser; its stated sources are CMP 109 (0.21), (2.3), not (3.38). |
| `sa_ca_III.tex:9297–9299`, `9355–9357` | `9.1:lem-link-bound` | Uses the complex criticality clause of a nesting lemma to transfer criticality to the second determining set and retain holomorphy. |
| `sa_ca_III.tex:11230–11232` | `9.1:lem-split-rotation` | Uses complex nesting under refinement to make the base critical on the refined determining set with its own readings as data. |
| `sa_ca_III.tex:18908–18914` | Unlabelled lemma “Criticality of the chart centre and the root, and the tables on the core” | Uses the second clause of nesting for critical configurations to transfer criticality of the centre and complex root to three refinements; its displayed conclusions have labels `9.1:eq-seed-criticality-1` onward. |
| `sa_ca_III.tex:36969–36998` | `9.3:lem-refinement` | Proves identification of the minimiser for refined own-average data using criticality and CMP 102b's unique critical orbit; this is a separate explicit argument. |

## Mentions and exclusions

- `sa_ca_I.tex:45199–45201`, under `4.13:lem-minimizer-unique`: the explicit dependency explanation connecting the lemma to the one-power hereditary-class statement. This is explanatory text, not a second application inside the lemma's proof.
- `sa_ca_I.tex:166621` and `sa_ca_III.tex:111211`: proof-status inventories naming uniqueness/locality; neither is a new proof or hypothesis use.
- `sa_ca_I.tex:29235–29238`, `4.7:not-step-constants`: defines the gauge map from (3.38). `sa_ca_I.tex:130188–130190`, unlabelled remark “Independence of the action convention”: identifies the element acting in (3.38). These use notation/content of the displayed identity but are not applications of the minimiser theorem.
- `sa_ca_I.tex:10607`, under `4.4:lem-twist-stability`: refers to the gauge-constant floor for membership of pairs of (3.38); it does not itself invoke the uniqueness/locality argument.
- The restriction theorem for the one-power class is not automatically another use: its proof at `sa_ca_I.tex:33365–33385` passes the already-imposed tower inequalities by inclusion of label sets. Likewise, references to the one-power class elsewhere are not all new uses of Lemma 4.13.
- Generic references to CMP 109 Lemma 4's analytic maps, smallness conditions, representation bounds, or input spaces have not been counted as uniqueness/locality uses. CMP 99b (3.38) is a different equation. Geometric nesting of regions, gauge projections, arrests, and cubes is also different.

## Confidence and search method

**High confidence** that there is only one occurrence of the literal lemma label and that the explicit CMP 109 (3.38)/named nesting uses above have been found. **Moderate confidence** that the semantic list is complete: the files repeatedly rename premises and use stronger complex/graded versions, so the text does not establish that every similarly described lemma is literally Lemma 4.13. In particular, the related-use table preserves that uncertainty instead of silently asserting a dependency. This is a source-use inventory, not verification that the outstanding lemma or the stronger extensions are proved.

I searched only the three permitted TeX files, using `rg` first and then small `sed` ranges around candidates. Searches covered:

- `4.13:lem-minimizer-unique`, `lem-minimizer`, `uniqueness and locality`, both `minimizer` and `minimiser` spellings;
- `Balaban`/the TeX `Ba{\\l}aban` form, `Lemma~4`, `B-CMP109`, `3.38`, and surrounding equation citations;
- `nesting identity`, `nesting lemma`, `nesting statement`, `nesting property`, `sub-tower conjugation`, `conjugation lemma for window minimisers`;
- `constrained minimiser in a local box`, `restriction of minimisers`, `restriction lemma`, `local reproduction`, `tower-locality`, `box-minimiser identity`, `re-minimisation of minimisers`;
- combinations of `minimi[sz]`, `unique`, `critical`, `locality`, `restriction`, `restricted`, `own data`, `own determining data`, and `own averages`;
- downstream identifiers `4.31:eq-window-counting-nesting-c`, `(N1)`–`(N3)`, `I9`, `8.5:eq-background-regularity-c`, and `5.2:eq-own-box-a`;
- statement beginnings and `\\label{...}` matches to locate the containing statements, with local context checks.

No source or repository file was edited. Only this requested report was written.
