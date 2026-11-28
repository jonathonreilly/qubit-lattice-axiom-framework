# PRINT-INVERSE, round 2: line-by-line check

Provenance: Codex (gpt-6-astra), checkout `7662d3a4b5f7680170b108c3ad11193c9fe697ea`, 2026-11-07. Research referee check, not an audit; no status is granted. No computer-assisted proof step.

Checked text: `library/print-inverse-r2.md`, SHA-256 `bdd3786c631211ef16332652bb77ca36dd9d1e690071425ec3881dacdba6a4a6`, lines 1–1153. Line references without a source name refer to this text. `library/prior/pi-r2-gate.md` is absent. Registry PRINT-INVERSE assigns this target to the print-inverse lane; FINISH 430 requests this check. B98-P5 is a different, separately owned obligation. The workflow file named by AGENTS.md is absent in this checkout.

The four source files match the full SHA-256 identities for `31a47c543775` in `library/prior/print-inverse.md:21–26`. The `sa` directory is a snapshot, not a Git checkout. The outline index, neighbouring rows and obligations were consulted before its bounded source passages. Its symmetric-row arguments are not a proof of the literal older-row target. The earlier gate's accepted flat and algebraic results are reused at their stated scope.

Credit: Tadeusz Balaban for the operators and walk construction; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account and outline; the authors of `flat-port.md`, `b109.md` and `pi-gate.md` for the supplied inputs and repairs. Only this report is edited. No editable prompt file changes.

## 1. Printed sources and the reading of section 2

**ADVANCE — the principal transcriptions (62–80, 89–147).** The page images confirm CMP 99b (3.132), (3.98)–(3.99), (3.93), (3.107)–(3.108), (3.13)–(3.19), and (3.35). In particular (3.132) contains spatial decay in `d(y,y')`, including within one layer. The distinction between the bare operator and the corrected operator in (3.130) is right. The first sentence of p.421 concerns the bare inverse; the subsequent renaming and (3.132) concern corrected operators.

CMP 98 pp.17, 19, 23–24, 27–29, 31 and 36 confirm the corner blocks, coarse contours, (42)–(43), (58)–(63), the iterated contour variable, (89)–(92), and (124)–(125). Section 1's relative-average formula has the right multiplication order. The four nonprincipal terms in (124) vanish at the flat background. The expression called (89) at line 116 is the operation defined in (89), applied in (90); this numbering shorthand changes no formula.

**Source-verification limit.** The supplied image collection has no `cmp96_p231.png` or `cmp95_p018.png`. Thus I cannot certify the literal CMP 96 (2.46) transcription or CMP 95 (1.6)–(1.7) against those page images. The block convention is independently visible in CMP 98 (2), and the coordinate-order contour is visible on CMP 98 p.24. SA:10113–10127 explicitly distinguishes its continuous-path metric from the lattice-contour metric. The proof below is checked for the metric expressly defined in section 2.5; no OCR display substitutes for an absent image.

**ADVANCE — the class distinction.** CMP 99b p.396 says the size number is at least 10, and restricts the outer region to big blocks within distance `RM` of `Omega_1`. Page 409 allows choosing 12. CA-I:12684–12724 instead states the broader separated tower class, including arbitrary localised outer domains. CA-I:12943–12973 imports the cube test and chooses 12. These passages support the distinction made in section 2; the remote finger is not a counterexample to Balaban's original class.

The internal-cube bond convention also has direct account support: CA-I:11016–11023 defines a lattice cube by consecutive sites and its bonds by **both** endpoints lying in it. This is distinct from the touching-bond convention expressly assigned to `Omega_j` at CA-I:12721–12722. The compressed whole-action Hessian, including protruding plaquettes, is expressly stated in SA:10287. CMP 99b pp.394–395 confirm the projection formula (3.25), the operator (3.26), its compression (3.27), and the gauge covariance (3.28)–(3.32). Thus the propositions concern the account's broadened tower/cube reading together with this compressed Hessian. They do not refute an alternative convention which tests crossing bonds or uses only internal plaquettes.

**REVISE — domains in the setting comparison (306–309).** A setting supplies `U` only on `Omega_0^+`, whereas its footprint can extend farther. Replace “every bond with both endpoints in W” by “every such bond in the common background domain”; alternatively give settings arbitrary full-torus background extensions. All coefficients compared in section 9 read the common domain inside the footprint, so the mathematical locality assertion survives either precise convention.

## 2. Lemmas 4.1–4.4: the literal complex rows

**ADVANCE — Lemma 4.1, all four parts (410–426).** The power-series estimates and the one- and two-variable Cauchy estimates have the stated constants. These are written analytic arguments, not numerical evidence.

**ADVANCE — Definition 4.2 and Lemma 4.2(i), (iii), (vi) (435–450, 452–454, 460, 462–472, 480–484).** The telescoping product is exactly CMP 98 (58). Formula (63) gives the displayed relative average, with the final factor `A(V_0)^{-1}` on the right. Under a gauge, each logarithm of a closed relative contour is conjugated at its starting point. This proves the stated relative covariance, including complex gauges near 1.

The margins suffice. The argument of the relative-average logarithm has distance less than `0.41` from 1. Conjugation costs at most `(11/10)^2`, and
`(41/100)(121/100) = 4961/10000 < 1/2`.
The absolute-loop and relative-contour logarithms have still larger margins. The bounds on the transformed links themselves need not be `r_1`: the logarithms used for covariance are of closed relative products. This distinction is essential and is respected by the proof. The decimal inequalities in (i) follow from the displayed exponential series bounds; no computed enclosure is needed.

**ADVANCE — Lemma 4.2(ii), (iv), (v) (451, 455–459, 473–489).** Both endpoint factors are present. Their first variations cancel the two internal axial paths, leaving `S`. The Cauchy estimate gives the entry error. A straight row has sum `L`; a fixed fine bond belongs to exactly `L` of the translated segments, giving column sum `L^{-3}`. The loose incidence bounds cover the other finite one-step derivatives.

**ADVANCE — Definition 4.3 and Lemma 4.4(i)–(iv) (493–582).** These are the literal CMP 98 relative maps at the successive absolute averaged backgrounds, as CMP 99b (3.13)–(3.19) requires. They are not the CMP 109 symmetric rows. The unitary gauge reduction, bootstrap, ordered products and site-contour telescoping all check.

In particular `sum_{m<j} s_m < 1/(L-1)` controls both the potential and the accumulated complex gauge. The induction strictly stays inside the one-step ball. The exact intermediate factor is `t_m^{-1}t_{m-1}=z_{m-1}^{-1}`; replacing it by independent gauge losses would be wrong, but the note does not do that. Row and column product estimates retain respectively `L^j` and `L^{-3j}` before the physical factor `L^{-j}`. The final column error is therefore `C_R eps (eta/l_j)^4`. The site products have the same summable scale factors and disjoint-block column count. There is no depth-dependent loss. The norm conversion from operator norm to the stated colour norm costs only a fixed `N`-dependent constant.

This closes round 1's actual-row identification obstruction. It does not close B98-P5's different averaging-derivative obligation.

## 3. Propositions 3.1, 3.2 and 3.3

**ADVANCE — Proposition 3.1 (359–365, 999–1018), with its stated thickness and interior qualifications.** Each of its four steps checks. The layer gaps give at most two adjacent heights, thickness supplies a containing aligned size-12 cube, and the next gap excludes `Omega_{i+2}`. The losses are at most `L` and `L^2`. Whole-torus `Omega_0` removes the outer-boundary qualification; it does not remove the thickness assumption on the tower.

**ADVANCE — Proposition 3.2 (369–376, 1020–1049), on its expressly fixed class.** The transverse segment argument excludes every tested cube with size number at least 10. It also excludes the plaquette endpoints used in the construction. Higher rows do not read the changed bond. The path `U_t(b_0)=exp(i pi t sigma_3)`, with all other positive links equal to 1 and reversed links their inverses, satisfies (S1), (S2) and (S2+) with twist zero.

The scalar Gram stays positive and its projection stays continuous. At the endpoint `t=1`, the six plaquette contributions total `-6 eta^{-2}||A||^2`; the divergence and mass contributions are at most `2 eta^{-2}||A||^2` and `eta^{-2}||A||^2`. The strict negative bound and the first eigenvalue crossing therefore give the asserted singular configuration. The endpoint configuration separately violates the asserted plaquette bound. These are exact hand checks of the displayed construction. No approximate value of the crossing parameter is used.

**REVISE — Proposition 3.3 must say `emptyset != Omega_0 != T_eta` (378–382, 1051).** As printed it includes the empty outer region, which has no boundary bond and no singular field matrix. Add nonemptiness to the statement and to each “any proper” summary.

**ADVANCE — its singularity construction for every nonempty proper outer region (1051–1059).** The finite periodic lattice is connected, so a crossing bond exists. The first gap makes it a level-0 row and excludes every higher-row carrier. No tested cube contains that bond. With `U_r=U_t` and twist zero, every tested cube sees the identity. The three asserted hypotheses hold, including (S2+).

At `t=1` all six full-action plaquettes through the bond have holonomy `-I`. For the field supported on that bond, the compressed divergence has only its interior endpoint. Its squared norm is exactly `eta^{-2}||A||^2`; the mass has the same value. Hence the displayed upper bound is `-4 eta^{-2}||A||^2`. The same positive-at-zero, continuous least-eigenvalue argument gives `U_{t_*}` with singular `Delta_a`. This proves failure of the inverse conclusion on that class. The final inference about failure of the small (S1-loc) hypothesis uses PI after its repairs below, not the negative endpoint alone.

**ADVANCE — removal of the old claim about Balaban's Theorem 3.3.** No such refutation remains. The note repeatedly preserves the outer-region and boundary-convention distinctions.

## 4. Flat transfer, operators, norms and constants

**REVISE — Lemma 4.5 (586–591).** The block-image identity is correct. The additional claim that the displayed translation maps every `T^(j)` onto itself is false. For example, take `L=3`, `k=j=1`, `eta=1/3`: the translation sends the coarse site 0 to `-1/3`, which is not in `T^(1)=Z`.

Here is the complete coordinate repair. Put `h_j=(L^j-1)eta/2`, with this displacement in all four coordinates. Translate fine sites and fine bonds by `-h_k`. **Separately relabel** a level-j site row, or both endpoints of a level-j field row, by

`y -> y+h_j-h_k = y-l_j (L^(k-j)-1)/2`.

This row relabelling, unlike the fine translation, does preserve the level-j row grid. The translated corner block is the centred block with that relabelled centre. Its straight paths translate to the straight paths of the relabelled row. The same statement holds for the block mean. Translate the regions as unions of blocks; layer membership and outward-row membership are preserved under these identifications. All fine pairings and row pairings are unchanged. The differential operators translate on the fine coordinates. Thus the flat mixed matrices are conjugate by these separate coordinate permutations. Their inverse bounds transfer. A single translation of both fine coordinates and all row labels was not the correct argument.

**ADVANCE — [F] with that repair (593–608).** This transfers the already supplied flat inverse to the actual corner rows. Alternatively, flat-port's formula (2.1) and its block proofs can be read directly on corner blocks. Its cutoff commutator proof uses oscillation across the double block, and applies with the row reference point at the corner as well. Choose the constants to cover that convention before making section 3.3's choices. No new flat coercivity proof is needed.

**ADVANCE — section 3.1 and Lemma 7.1's spaces and normalisations (216–247).** `K=mQ` maps into counting rows, and its transpose is `Q^T m^{-3}`. Thus `K^T K=Q^T m^{-2}Q`. The mass-independence assertion for the real site projection is correct on its invertibility domain. The five-block matrix has precisely the required scalar and vector Schur complements. It never installs a global propagator as a local coefficient.

**ADVANCE — section 3.2 (251–266).** The energy and second-order site norms, zero extensions, special `M_1:H_m^2 -> L^2` source space, and counting multiplier estimate (E) are consistent with flat-port. The norm of a field supported in the agreement region is the same after transplantation, including its difference stencils.

**ADVANCE — section 3.3 (270–295).** The order of choice is noncircular after [F] has the precise corner interpretation above. The stronger fourth-power bound on `theta` is available by choosing one fixed large power `M_t`. The comparison radii are chosen afterwards and may depend on that fixed size. The resulting constants depend on `N,L`, not depth, volume or the background. The later shell floors remain genuine additional conditions before a kernel-algebra use. No variable-`M_t` asymptotic is claimed.

**REVISE — harmless top-index convention.** Set `Omega_n=emptyset` for **every** `n>k`, not just `n=k+1`; the cube definition uses `Omega_{j+2}` also at `j=k`. Likewise use the centre of the run of lattice sites for `x_tau`, as the exterior displacement formula already does.

## 5. Lemmas 5.1–5.3 and every local-model step

**ADVANCE — Lemma 5.1(i)–(iii) (614–667).** The literal row estimates now supply its averaging blocks. The physical column factor in Lemma 4.4 gives the mass-norm bound with no fine-mesh loss. The two adjacent heights cost a fixed constant. Replace both factors when comparing a mass block. For the strong `A_s` block the site means and their transposes are bounded on the weighted `L^2` spaces, as well as in the displayed bilinear forms.

The first- and second-difference product rules need only `B` and its first difference. The neighboring-scale factors are absorbed in `C_C`. The Wilson Hessian expansion has the correct commutator sign and polarisation. Its raw plaquette remainder is `C|P-1| eta^2 |v||w|`, and the small-curvature estimate gives the required `C e eta^4 m^{-2}|v||w|`. This meets the earlier normalisation correction. Zero extension and the full plaquette read handle a Dirichlet edge. The real norm comparison then follows from the same first- and second-order difference bounds.

**ADVANCE — Tiles and Cutoffs (671–690).** Divisibility gives the tiling. The added exterior tiles cover every allowed bond's exterior initial point. The denominator is at least one on every active component. The gaps prohibit nonadjacent bump heights, giving the stated smooth cutoff bounds with fixed profile constants. Values on inactive coordinates can be assigned by extension; no division by a vanishing denominator is used on an active component.

**ADVANCE — Footprints and two levels; Models; Agreement; Diameter (692–737).** The larger floor in section 3.3 excludes three heights even from `F_tau^+`. The rounded and graded cut-down tower is admitted. Its read, including protruding plaquettes and outward-row double blocks, is contained in `N_tau`. The model agrees on the complete read closure of the cutoff, not merely on its support. The lattice staircase in the diameter proof is admissible for section 2.5's contour metric. Its scale cost is bounded by the displayed `24 L^2 M_t`.

**REVISE — the intermediate intersection-size claim in Overlap (745–747).** An intersection cannot be larger than its smaller cube. For unequal tile heights the stated lower bound can exceed that cube's side. Replace it by

`min{2 rhat min(l_tau,l_sigma), (rhat-r_N)(l_tau+l_sigma)}`.

This is a valid lower bound on each coordinate's intersection length. Both quantities are at least `M_t l_i`, where `l_i` is the smaller tile scale. Since `M_t>=L`, the needed intersection still contains a level-`i+1` grid point. The count `D_*=3(20L)^4` and the existence of a top in consecutive footprints are unchanged. The corrected count `15+14/L` is present; round 1's count error is repaired.

**ADVANCE — the exterior-centre case (674–679, 711–718, 751–784).** Its model is entirely bare by the first gap. The selected interior endpoint `z_tau` is within `(M_t-1)eta/2+eta` of the exterior centre. Its model read lies in `N(z_tau)` because `6M_t+2+M_t/2+1<=7M_t` for the declared `M_t`. The proof uses that interior endpoint's gauge. It never asks (S1-loc) at an exterior site.

**ADVANCE — Lemma 5.2 (751–766).** Gauge covariance of the twist, the first-difference product rule and the BCH bound give (5.4), with the bond-scale convention of section 3.1. The model scale never exceeds the actual extended scale. The outside plaquette bonds are covered by (S2+). This is an implication from supplied local gauges, not a boundary gluing argument.

**ADVANCE — Lemma 5.3 (768–784), using repaired [F].** Covariance is now proved for the literal rows. The flat perturbation is at most `1/(8B_F)`, giving inverse bound `(8/7)B_F`; the two norm conversions give `(9/8)^2(8/7)B_F=(81/56)B_F<3B_F`. The original coefficients define the inverse independently of the gauge chosen for its estimate. Nonvanishing determinant and coefficient holomorphy give the asserted holomorphy on the whole ball.

## 6. Assembly and Schur identification

**ADVANCE — Lemma 6.1 (793–805).** Agreement supplies the full commutator read and support. Its flat part costs `C_88/M_t`; its perturbative part costs at most the same amount. The norm conversion gives `2(9/8)^2<3`. The estimate holds for all four systems with their specified spaces.

**ADVANCE — Lemma 6.2 (807–829).** The sign in `M Par=I+Res` is right. The smooth-cutoff synthesis/transpose argument justifies localisation of dual sources. It does not use sharp characteristic multipliers on `H^2`. Bounded overlap gives `||Res||<=D_* theta<1/2`. The finite square matrix consequently has the asserted inverse.

**ADVANCE — Lemma 6.3(i)–(v) and its by-product qualification (831–850).** Expansion, ordered supports, norm products and rooted walk counts check. Each letter reads only its model, its cutoffs and their stated tower data. The by-products remain energy-norm statements; they do not supply the missing pointwise or Hölder vector bounds.

**ADVANCE — Lemma 7.1(i)–(iv) (854–873).** The null-vector test, scalar elimination and two subsequent Schur complements have the right signs and domains. The conversion gives exactly `q_0=-m^{-3}[M_5^{-1}]_{nu nu}m`.

**ADVANCE — PI(a), after the foregoing definitional repairs (875–891).** The local inverses give all four global inverses; the Schur chain gives the remaining inverse and projection formulas. Bilinear symmetry gives `q_0^T=q_0`. Holomorphy holds for fixed `U_r` on the full stated twist ball, including the (S2+) restriction. Real-point identification now uses the same finite CMP 98 formulas as CMP 99b; it no longer tries to identify two different curved averaging rules by analytic continuation. The bare/current-corrected distinction remains intact.

## 7. PI(b)–(e): bounds, spare factors and settings

**ADVANCE — density conversion, (SD), each-term estimate and summation (895–940).** The density is `-l_j^{-3}l_j'^{-3}(W_omega)_{nu nu}`. The intervening layer stretches in (SD) are disjoint. Their scale-distance estimate absorbs the scale ratio using at most `delta_q/3`. Splitting the norm majorant leaves at least `3 delta_q D_X(n+1)` for the exponential. The endpoint multiplicity and geometric series give exactly the stated `C_q`. The at-most-eight field rows at a base point give the displayed `K_{-2}` constant. There is no missing source-cell volume.

**ADVANCE — PI(d) (338–345, 923–929).** The stronger choice gives `D_* theta^{1/4}<=1/4`, so the fourth-power factor really is summable in both directions. The second fourth-power factor is spare. The two exponential reserves follow from the walk-diameter bound. Both defects in round 1's part (d) are removed: no unsupported fourth-power summation, and no claim of an `O(M_b^{-1})` variable-size majorant.

**ADVANCE — PI(e), with section 1's precise background-domain convention (942–988).** Each of its four steps checks. In the cutoff step, every contributing neighbouring tile is contained in the footprint: its centre is within `(L+1)M_t l_j` and its half-side is at most `L M_t l_j/2`. An exterior neighbour's additional one-bond membership test is still inside the remaining margin. Thus the two settings select identical contributing bumps and identical denominators. The models, reads and transplants are also fixed there. Symmetry of this argument gives the same restricted-walk index set in both directions.

This defeats the earlier `L=27` counterexample: the formerly invisible coarse bump is now in the required tower read. The larger footprint does not enlarge dependence on `U` at a fixed tower. Connected interiors follow from the corrected positive-overlap estimate above.

The support margin in PI(e) is valid for the **base-point coordinates** of the kernel, which are the coordinates used in (b)–(c). If support is instead taken to include each entire row bond, subtract its length from that margin; the margin required by the cited consumer remains ample. State that coordinate convention explicitly.

## 8. Section 11, use by use

“Repaired PI” means the theorem on its stated (S1-loc), (S2), (S2+) domain, with the coordinate and set conventions corrected above. It does not mean the account's unrestricted S1–S2 class. The following checks concern the particular inverse input, not proofs of the consumer theorems.

| Account passage / note line | Verdict |
|---|---|
| I:13143–13178 / 1077 | **ADVANCE** for the qualified supply; **BLOCK** an unconditional discharge of the remark. The two counterexamples apply on the documented broadened reading, with nonempty outer region in Proposition 3.3. The inverse bound is for bare `G_0`, and the walk bounds are the fixed-size bounds actually proved. |
| I:13589, 13624–13627 / 1078 | **ADVANCE.** Repaired PI supplies `q_0 in K_{-2}` and an actual local complex walk expansion. Impose all the shell floors, not just the scale-ratio floor. |
| I:13640–13665 / 1079 | **ADVANCE.** The stated constraint, projection, transpose and inverse identities use precisely PI(a)'s inverse algebra. |
| I:13675 / 1080 | **ADVANCE** for “Partly.” The missing pointwise/Hölder vector and lift bounds remain separate. |
| I:13683; 19583–19600 / 1081 | **ADVANCE.** This supplies only the specified inverse input on the stronger domain. The other hypotheses in those passages remain. |
| I:13766, 13899–13909, J3 / 1082 | **ADVANCE.** The `q_0` input has the right order. The kernel algebra spends decay and determines the current ceiling afterwards. |
| I:13787–13798, 13966–13979, J8 / 1083 | **ADVANCE** for the `q_0` piece. Its local terms, absolute majorant and reserves are available. This does not establish the other primitive families or their differentiated vector norms. |
| I:13915–13923, J4 / 1084 | **ADVANCE.** The inverse factor is supplied; the separate `H_0` bound remains a premise. |
| I:14377–14476 / 1085 | **ADVANCE.** The inverse insertions and representation algebra are supplied. Chart existence and its fixed-point bounds are explicitly left as inputs. |
| I:14655 / 1086 | **ADVANCE.** Holomorphy holds on the entire PI ball, subject to its exterior restriction. Consumer inclusion in that ball must be imposed by the radius choice. |
| I:14715–14774, K3 / 1087 | **ADVANCE.** The physical transpose column bound, order `-2` inverse bound and weighted shell sum supply the indicated order `-1` to order `-3` estimate. They do not prove the rest of K3. |
| I:14831 / 1088 | **ADVANCE.** The same inverse input is available with an allowed weight rate, after fixing the common rate and shell floors. This is a first variation. |
| I:15266–15490, K10 / 1089 | **ADVANCE** for the inverse contribution, with the full-footprint assignment and the stated later decoupling-size floor. Use rate at most `delta_q/17` for its anchored-tree reserves, and choose subsequent constants at that rate. See the geometric detail below. The other operators and nonlinear equations remain inputs. |
| I:15770–15796 / 1090 | **ADVANCE.** `P_0^T Delta_a=Delta_a-Q^T q_0 Q` follows. The real minimiser, chart uniqueness and continuation in the datum are separate premises. |
| I:19744–19750 / 1091 | **ADVANCE.** The row now correctly limits PI's contribution to the listed `q_0` inputs. It does not claim J2–J8 or K10 in full. |
| I:5293–5470, 5702–5712 and their C1 conclusion / 1092 | **REVISE.** Section 9 supplies same-grid setting locality, equality of restricted terms, and absolute convergence for `q_0`. It does not supply the full account one-family/C1 input, which also requires lattice covariance of the same assigned terms. See the explicit limitation below. |
| I:13323 / 1093 | **ADVANCE.** This is a dependency attribution. PI does not construct the near-bound frame. |
| II:54464–54635 / 1094 | **ADVANCE** for the bare `C_Q` bound under PI's hypotheses. For the displayed factor `exp(-8 delta_1 d)`, choose `8 delta_1<=delta_q` as well as the other common-rate restrictions. No other operator in the proposition is supplied. The page image confirms that the account's assertion of no within-layer spatial decay in (3.132) is a transcription/reading discrepancy. |
| II:60313 / 1095 | **ADVANCE** for the stated dependency distinction: the bare (3.132)-form input is available; (3.133) needs separate lift/vector bounds. |
| III:36352–36370 / 1096 | **ADVANCE** for “Not supplied.” This is the current-corrected `G_1` inverse and needs its perturbation argument and other premises. |
| I:166593–166594; III:111329 / 1097 | **REVISE** the proposed summary to include this report's repairs and its precise scope. **BLOCK** replacing those entries by an unconditional closed BP07 claim. These passages are status lists; this check grants no status. |

**K10's geometric detail.** A footprint of side smaller than the decoupling cube side meets at most `2^4` such cubes. Choose a representative in each intersection and join these representatives, the consecutive-footprint joining points and the end anchors. The usual count is at most `17(n+1)` links of bounded layer length. If a thin intersection has no top, choose a top inside the decoupling cube within `l_{i+1}` of it. It lies in `F_tau^+`. The same staircase argument extends to these endpoints: its bound is at most

`16 L(L+1) M_t + 8L^2 + 12L <= 24 L^2 M_t = D_X`

under `L>=3`, `M_t>=4L`. The larger staircase box still meets only the two heights by the stated gap floor. Thus the claimed `17 D_X(n+1)` tree bound survives this endpoint issue. The two spare factors have rate `delta_q/17`. A surviving zero-switch word has its full connected footprint in the retained union, so it cannot connect distinct components. Equality at switch value one follows from the original sum. This proves the inverse contribution without asserting K10 for the other operators.

**The C1 limitation is substantive (1092).** CA-I:5664–5669 requires termwise covariance under the specified translations, reflections and elements of `W_4`; CA-I:5725 includes that covariance in C1. PI(e) compares settings on one fixed grid and says nothing about those transformations. An allowed choice of its profile actually fails the stronger assertion.

Take `L=3`, `k=0`, `eta=1`, `Omega_0=T_eta`, and `U=1`, with a large admissible torus. Let `phi(s)=prod_mu f_mu(s_mu)`, where each smooth `f_mu` takes values in `[0,1]`, equals 1 on `[-1/2,1/2]`, and vanishes outside `[-1,1]`. Choose `f_1(-2/3)=1/2` and `f_2(-2/3)=1/4`. For the tile whose four centre coordinates are equal, take a direction-3 bond based at `x=x_tau+(M_t/3)e_1`. Let `r` interchange coordinates 1 and 2. It fixes the tile, its model cube and its footprint. The cutoff normalisation gives

`h_tau(x)^2=1/(1+1/4)=4/5`, whereas `h_tau(rx)^2=1/(1+1/16)=16/17`.

Here `Q=Q'=I`, `R=0`, and the local bare inverse satisfies `-[M_{5,tau}^{-1}]_{nu nu}=Delta_tau+I`. At either interior direction-3 bond its diagonal colour block is `7I`: six flat plaquettes and one mass. The one-letter `q_(tau)` therefore has diagonal blocks `7(4/5)I` and `7(16/17)I`. They differ although `r(tau)=tau` and the flat background is invariant. This is a hand-checkable failure of termwise `W_4` covariance for an assignment allowed by PI; it does not contradict PI(e).

Replace row 1092 by: “Supplied for the same-grid locality, support and convergence clauses of the `q_0` entry. Identification with the account's full one-family hypothesis, including termwise lattice covariance on its domains, remains an input.” One possible further construction would transport all grids, contours, profiles and model choices as part of the setting, then check the required operator transformation. That construction is not supplied here. This check does not open its separately governed proof work.

Also replace the causal wording at 1070–1071: Proposition 3.3 proves that S1–S2 do not give the required **boundary real-gauge control**. Its example has twist zero and already satisfies (S2+); it is not a counterexample to an implication concerning the exterior twist alone. Retain (S2+) as the explicit exterior-domain hypothesis that PI uses.

## 9. Each verdict of `pi-gate.md`

| Earlier verdict | Round-2 result |
|---|---|
| Section 1: bare versus corrected inverse | **Met.** The operator distinction and the “form of (3.132)” wording are correct; the principal printed displays were checked visually this time. CMP 95/96 image limits remain as recorded above. |
| Section 2: literal-row mismatch | **Met.** Definitions 4.2–4.3 and Lemmas 4.2–4.4 supply the actual one-contour comparison. |
| Section 3.1: Proposition 3.1 only on its interior scope | **Met.** Thickness and the interior qualification remain. |
| Section 3.2: invalid claim about Balaban's Theorem 3.3 | **Met.** Removed. |
| Section 3.2: specify the cube class and its size | **Met on the stated reading.** The images confirm the lower size 10 and the permitted choice 12; the account supplies the internal-cube bond convention. Preserve the distinction from the original outer-region restriction. |
| Section 3.3–3.6: fixed tile size and order of constants | **Met.** Changing `M_t` requires recomputing the later constants. |
| Section 4.2: plaquette power | **Met.** The raw remainder is now proportional to `eta^2`. |
| Section 4.3: overlap count | **Met.** The count is corrected. A different intersection-size overstatement needs the minimum formula in section 5 of this report. |
| Section 4.3: exterior-centre boundary tiles | **Met.** The interior endpoint gauge and (S2+) cover their reads. |
| Section 5: cutoff-dependent tower locality | **Met**, after making the background-domain comparison precise. The enlarged footprints determine all relevant bumps. |
| Section 6: Lie-algebra wording and final operator identification | **Met.** The twist wording and literal-row identification are now correct. |
| Section 7: fourth-power summation and variable-size claim | **Met.** Stronger smallness proves the split; the unsupported variable-size claim is gone. |
| Section 8: consumer qualifications | **Mostly met.** The vector, chart, current, shell-floor and fixed-size qualifications are retained. Row 1092 still needs the one-family/C1 limitation above; the summary must incorporate the small repairs identified in this check. |

**Section 3.7, the symmetric-row remark: ADVANCE as a separate variant.** Reuse of the earlier checked P15 comparison is legitimate with its read enlargement. “Verbatim” must mean the estimates and construction, with part (a)'s identification changed to the specified symmetric operator. It cannot identify those rows with the literal CMP 99b rows.

## 10. Disposition and final source checkpoint

**Theorem PI: REVISE, then ADVANCE at its expressly stated local scope.** Its existence, holomorphy, literal-row identification, density bound, absolute walk expansion, spare factors and same-grid setting locality are supported by the checked argument, using [F]. The written repairs above complete the coordinate transfer and intersection estimate and make the setting/support conventions precise. These are not new curvature, coercivity or averaging hypotheses. The note is therefore not correct line for line unchanged; in particular Lemma 4.5 contains a false grid assertion. No failure of the repaired inverse theorem under its local hypotheses was found.

The precise scope is: fixed `SU(N)` and odd `L>=3`; the corner-block, no-inward row convention; the compressed whole-action Wilson Hessian; separated towers with the stated floors and torus room; supplied (S1-loc) at every required interior anchor, plus (S2) and (S2+) on the full coefficient read. The tile size is fixed before the radii. Constants are uniform in depth, fine mesh, volume, tower and background, with dependence on fixed `N,L`. At real data the inverse is the bare CMP 99b operator under these conventions. At complex data it is its holomorphic extension on that same fixed ball. Setting compatibility is on the fixed grids specified in section 9.

This does **not** prove the S1–S2 remark on arbitrary separated towers, the corrected `G_1` inverse, the pointwise/Hölder vector bounds, a boundary gauge-gluing lemma, a tile-size-independent radius, or the account's full covariant one-family input. The two counterexamples concern the documented broadened reading; they do not refute Balaban's original Theorem 3.3.

**Propositions:** 3.1 is correct with thickness and interior qualification. Proposition 3.2 is correct on its stated size-at-least-10, remote-finger class. Proposition 3.3 is correct after adding `Omega_0 != emptyset`; as printed its empty-region case is false. The singular configurations are the precisely defined first crossings of the explicit real paths, justified by continuity and the hand-checked negative quadratic forms.

**Every earlier verdict met?** The main mathematical obstructions from round 1 are repaired, including the literal rows, exterior anchors, cutoff counterexample and summation split. The blanket claim “every verdict applied” still needs the consumer-table correction and the finite repairs in this report. There is no unconditional BP07 or publication-status conclusion.

Source identities were refreshed after writing: the checked note retains the hash at the start; `flat-port.md` retains SHA-256 `329371416b74e2c69d75229e83b33ab7717ccd8cc4b3726472d58f4d26b920cc`, the identity recorded by the earlier gate. SA, CA-I, CA-II and CA-III retain respectively the full hashes recorded in `library/prior/print-inverse.md:21–26`. Images inspected were CMP 99b pp.392, 393, 394, 395, 396, 409, 410, 413, 416, 421, 422 and CMP 98 pp.17, 18, 19, 23, 24, 26, 27, 28, 29, 31, 32, 36. The unavailable CMP 95/96 images are the only visual-source limitation identified above. Only `gates/pi-r2-gate.md` is changed; no source note, prompt, ledger, audit or public posting is changed.

Checked line by line by Codex (gpt-6-astra).
