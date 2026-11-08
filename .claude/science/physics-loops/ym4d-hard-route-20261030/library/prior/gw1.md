# GW1: prior-work and consumer digest

Codex (gpt-6.1-sol), checkout `ee461c11b4febca76887cab1ae236182b29392e6`, FINISH row 463.
Research reading and collation. No new proof, independent proof check, audit, or status grant.
Credit Tadeusz Balaban for the operators and method. Credit Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their account, for the account's constructions and arguments.
Paths below are relative to `ym4d-hard-route-20261030/`. I, II, III denote the three complete-account files.
SA denotes `YM4_sketch_500.tex`. All source references are physical line numbers.

**Decision:** do not launch an all-primitive Laplacian proof lane. The account excludes that
bound for $G_\pi^J,G_1^J$, and GW already proves the graph source-inverse estimates.
The residual useful port is the $G_1^J,q_{1,J},H_1^J$ **first-order/coarse-kernel** word family.
The stronger general-layer graph/current problems already belong to LAYER-THM; its proposed
field-slot graph extension has a checked obstruction. Details and exact consumers follow.

## Recovery point and scope

`library/prior/gw1-prior.md` is absent. `open-registry.md:440` assigns GW1 to `gw1`.
The true-current precision walk lane B99-W belongs to `b99-w` (`open-registry.md:25,125,143`);
the prescribed-assignment transfer belongs to CO/`ol`. This digest does not attack either.
The workflow file named by AGENTS.md is absent in this checkout. No editable prompt file changes.
Only this digest is written. No proof lane, fetch, audit, status edit, commit, or outward post is started.

The source directory `/Users/jonreilly/ym4d-lead/sa/` is a snapshot, not a Git checkout.
SHA-256 matches the recorded identities of revision `31a47c543775`:

| File | SHA-256 |
|---|---|
| SA | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| II | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| III | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

Navigation began with `sa-index/README.md`, chunk-10's neighbouring operator/walk rows,
chunk-11's current-expansion rows, and `obligations.md:523–550,627–640`.
Bounded SA passages read: 10139–10161, 10307–10342, 11687–11715.
Search inventories are under `/tmp/gw1-digest-ee461c11b/`; they are retrieval evidence only.
No computation discharges a mathematical claim. Balaban attribution below is to quotations
and citations in the permitted account/repository sources, not a fresh reading of his papers.

## 1. Definitions and the precise requested norms

**The target's name is too strong if it means a Laplacian bound for every primitive.**
I 13760–13764 expressly says: “The Laplacian member is not asserted for” $G_\pi^J$.
I 13783–13784 transfers those same assertions to $G_1^J$.
I 19614–19616 repeats “not the bound involving the Laplacian”, retaining it for $G_0,H_0$.
SA 10307 and 11714–11715 also exclude that member. I 5817–5819 quotes Balaban:
“It does not hold for $G$, $G_1$”. A new proof lane must preserve that exclusion.
Graph endpoint means the component covariant Laplacian in GW, not the Wilson Hessian.

Write $B_0=P_0G_0$ in the following table only; this is an operator, not the account's bound constant.

| Object | Definition in I; short exact source phrase/formula | Published source identified there |
|---|---|---|
| Bare $G_0,q_0,H_0,P_0,B_0$ | 13579–13589,13624–13627,13640–13646: $G_0=\Delta_a^{-1}$, $q_0=(QG_0Q^*)^{-1}$, $H_0=G_0Q^*q_0\ell^{-1}$, $P_0=I-G_0Q^*q_0Q$ | CMP 99b Theorems 3.3–3.4, (3.42)–(3.47); CMP 102b (129),(131), p.300; inverse walks before CMP 99b (3.132) |
| $\Lambda,\Pi$ | 13629–13637,13720–13725: “$\Lambda:=G'RD_U^*$”, $\Pi=I-D_U\Lambda$ | CMP 99b (3.42),(3.49), gauge-variation construction (3.116)–(3.120) |
| $\Theta'_J$ and local current insertions | 13688–13725: $\Theta'_J=\mathfrak k_J\Lambda+\Lambda^T\mathfrak j_J+\Lambda^T\mathfrak m_J\Lambda$ | CMP 99b (3.116),(3.120); polarization/decomposition printed at I 13811–13833 |
| $G_\pi^J,q_J,H^J$ | 13727–13731, `4.5:eq-free-current-operators-a`: $\sum_{n\ge0}G_0(\Theta'_JG_0)^n$, $(QG_\pi^JQ^*)^{-1}$, $G_\pi^JQ^*q_J\ell^{-1}$ | CMP 99b (3.130),(3.132),(3.133); identification at own current, I 15546–15553 |
| $\Theta_J,\widetilde G^J$ | 13733–13735: $\langle A,\Theta_JA\rangle=2\langle H^JC^{(2)}(\ell A),J\rangle$; $(I-B_0\Theta_J)^{-1}B_0$ | CMP 99b (3.134)–(3.137); CMP 102b (143),(180), related CMP 116 (1.4) |
| $G_1^J,q_{1,J},H_1^J$ | 13737–13739: $G_1^J=\sum G_0((\Theta'_J+\Pi^T\Theta_J\Pi)G_0)^n$; $q_{1,J}:=(QG_1^JQ^*)^{-1}$; $H_1^J=G_1^JQ^*q_{1,J}\ell^{-1}$ | CMP 99b (3.128),(3.129),(3.135),(3.138); I 27524–27527 supplies this dictionary explicitly |
| $D^J,\mathfrak L^J$ | 13994–14000: fixed point $X=C(\ell A'-\ell H^JX)$; $\mathfrak L^J(A')=A'-H^JD^J(A')$ | CMP 102b Proposition 3, (48),(50)–(58),(63)–(73) |
| $\mathfrak R^J,(I+\mathfrak R^J)^{-1},\mathfrak D^J$ | 14005–14015: $\mathfrak R^J=C'(\ell\mathfrak L^JA')\ell H^J$; $\mathfrak D^J=(I+\mathfrak R^J)^{-1}C'(\ell\mathfrak L^JA')\ell$ | CMP 102b (63)–(73); I 14055–14069 differentiates the fixed-point identity |
| $\mathbb V'^J$ | 14156–14192, `4.5:def-higher-order-functional`: gradient of $V^{J,\mathrm{disp}}+W^J$; seven terms, including both extra free-current terms | CMP 102b (77),(80),(87),(90)–(96); printed differentiation I 14198–14262 |
| $\mathcal A_0^J,A_G,X_G,\mathcal H^J$ | 14376–14401, `4.5:def-response-chart`: fixed point $B_0[\Theta_J(\mathcal A+H_0B)-\mathbb V'^J(\mathcal A+H_0B)]$; $A_G=\mathcal A_0^J+H_0B$, $X_G=D^J(A_G)$, $\mathcal H^J=A_G-H^JX_G$ | CMP 102b (143),(179),(180); CMP 116 (1.2),(1.4),(1.18), with the different splitting explained I 14425–14438 |
| $\Lambda^J,\mathfrak J$ | 14402–14419: $\Lambda^J=P_0^T\Xi+Q^*(q_0-a)\widetilde B-Q^*\mathsf kX_G-\Lambda^T\mathfrak j_J(H^JX_G)$; $\mathfrak J=\Lambda^J-\Delta'\mathcal H^J+F(U,\mathcal H^J)$ | $\mathsf k=(q_J-a)\ell^{-1}$ at 14137–14140; CMP 109 (3.11), p.272 for $F$; CMP 109 (3.6)–(3.9),(3.13)–(3.14) for its chart consumers |

The duplicate $H^J$ in the task distinguishes the linear map $H^J$ from the nonlinear chart
$\mathcal H^J$. They must not be identified with the general field/block-data layer map.
I 14384–14393 has block datum only and expressly removes the old $-GJ$ source (14425–14430).
`layer-find.md:72–78` records this difference from the assumed general layer theorem.

At switches, I 15278–15314 expands primitives **at one**, then tags each concatenated word,
including every side branch, once per distinct visited cube. It then forms composites
from those tagged primitives. “These series are not re-summed at $s$” (15286).
Thus $q_J(s)$ is not defined by inverting $QG_\pi^J(s)Q^*$.
The local averaging operators and composite identity terms retain their prescribed convention.

## 2. Coverage already present in this repository

The important comparison is with the whole GW proof, not its three-line theorem alone.

| File and exact locus | Existing result; recorded check and limitation |
|---|---|
| `walks-gw.md:36–105` | Three graph estimates T2, absolute tagged endpoint sums T3, common PI constants. All statements conditional on its explicit PI class, full reads, geometry and small radii. |
| `walks-gw.md:629–768` (§6) | Absolute first-order/Hölder word estimates for the scalar/vector divergence branches, $\Lambda$ and reversed chains; then $G_0\Theta'_J$, $G_\pi^J,q_J,H^J$ and physical transposes. At 733–747 it explicitly constructs their Neumann word series. This work is already done; it is not a new GW1 target. It says “No graph bound for $G_\pi^J$ is used” (633). |
| `walks-gw.md:769–963` (§7) | Local averaging/transpose bounds, induced $H^{J,T}J$, $\Theta_J$, nonlinear $D^J$ branch and seven-term $V'^J$ majorants. Uses supplied-frame averaging results, not an unconditional global-frame theorem. |
| `walks-gw.md:964–1013` (§8) | More than T2: $\widetilde G^J(s):F_p\to E_p^\Delta$ itself has absolute majorants, 981–985, with the graph readout on the leftmost bare word. T2's second/third lines are corollaries. Do not re-prove this under GW1. |
| `gates/walks-gw-check.md:210–239,287–296,345–359` | Claude checked §§6 and 8, ADVANCE. Overall REVISE, no BLOCK: insertion-carrier tree weights and complex-background Wilson vertex needed repairs. FINISH row 454 records them applied at `b133dfe5f`; current GW has them. The old header's “No independent check” is stale provenance, not the latest check record. |
| `print-inverse-r2.md:221–367,820–1029,1101–1153` | Theorem PI: literal corner rows, compressed whole-action Hessian, $G_0,q_0$ inverse/energy walks with complete footprints and compatible local reads, under (S1-loc),(S2),(S2+). Its use table expressly excludes corrected $G_1$ at III 36352–36370 (1135). Energy words alone do not give pointwise/Hölder graph norms. `gates/pi-r2-gate.md` records local-scope ADVANCE with repairs, applied in PI §13. |
| `layer-pkg.md:93–136,423–633,875–977,1139–1232` | Fixed seven-term equation, unswitched graph reduction, switched-current problem and U01–U34 inventory. Generation text; its missing GW input is supplied later by GW. It does not certify actual layer-source matching or admission. Superseded as the consolidated statement by the part below. |
| `layer-thm-part.md:706–950,975–1031,1329–1567,1651` | Consolidates PI/GW first-order primitives, graph contraction and four-entry estimates into one conditional layer theorem. Frozen **as an implication** after Claude's `gates/layer-part-ref.md` and repairs. All actual-domain, source, current-assignment M3, matching and clause-(e) premises remain. This is not a proof of the unnamed account layer theorem on every use. |
| `b99.md:1651–1934,2481–2565` | B15 real projected/current-corrected $G,H,G_1,H_1$ and induced-current/energy decay; B16 actual constrained gap U on original/appended nests with boundary qualifications. U is already proved on its stated class. B17 inverse/root construction is conditional on a local analytic precision family and accretivity. Not independent-current enlarged-switch graph supply. |
| `b99-w.md:173–285,796–876`; `gates/b99w-gate.md:169–194` | Lemma 3.3 identifies $G,G_1,H,H_1,q_1$ as blocks of an unfolded system. Repaired Lemma W is a checked conditional **true-current** precision-family result. Its header and older registry descriptions are stale; the gate and repair log are later evidence. The gate explicitly blocks inference to the full independent-current conditioned/root/switch package. This work belongs to B99-W and must not be duplicated. |
| `lrb.md:5–10,800–859`; `gates/lrb-gate.md:1–7` | Port of I 8110–8373's local-real-base implication for assigned walk families, continued account proofs and Gaussian vertex integral. Checked by Claude, first failing step none. It retains the upstream walk hypotheses; it proves neither corrected primitive walks nor their physical positivity input. |
| `port/p4-operator.md:1–20,23–71` | Conditional port of I 19578–19743, with source distinctions. Explicitly “not yet checked by another model”; imports the operator lemma and K10. A port is not another supplier proof. |
| `lit-balaban.md:127–147` | Second-hand published-source map, explicitly “unchecked”. Distinguishes propagator theorems, omitted inverse walks and omitted nonlinear-response derivative calculations. |

Other relevant hits have different scopes:

| File | Relevant content and boundary |
|---|---|
| `prior/print-inverse.md:11–40`, `prior/b99-w.md:11–95` | Earlier digests already separate bare inverse, real corrected precision, independent-current families and prescribed assignments. Retrieval records, not proof checks. Their old open-W description predates the repaired W result. |
| `flat-port.md` §§4,8–12; `b98p5.md` §§2.1–2.5; `b98p5-r3.md` §§3–4 | GW's existing flat source-space/walk and local analytic averaging suppliers. The supplied-frame port is checked in `gates/b98p5-port-check.md`; its full carrier/admission claim stays conditional. Do not rebuild the flat parametrix or averaging port. |
| `h-walk.md:120–179,285–393`, `h-walk-fix.md` | Checked unfolded/tree-walk construction for the **outline's** straightened-row system, including $G_1,H_1,q_1$, in energy norms. At 393 it expressly does not claim the pointwise/derivative/Hölder upgrade. Different operators and assignment from literal PI. |
| `pw.md:810–1050,1173–1207`; `gates/pw-gate.md` | Checked PW implication for the specified outline/DR family: weighted supremum bounds for $H,H_1,\mathfrak G$ with independent current and enlarged switches. Not a literal-PI, component-Laplacian, common-assignment theorem. |
| `dr.md:7–55,592–610`; `dec-field.md:225–245,350–371`; `a3-clauses.md:238` | DR's first real-reference lift estimate; older differentiated-current obstruction and conditional response implications. The old “PW open” text is superseded for PW's specified family. The warning remains: no bounded $J$ derivative, no silent transfer between row/gauge systems. |
| `a3-balaban.md:14–41,151–176,189–215` | Published-theorem map and algebraic/conditional energy ports; explicitly excludes the $G,G_1$ Laplacian estimate. It is not independent-current K10 supply. |
| `layer-thm.md`, `layer-r2.md:335–450,795–846`, `layer-r3.md:34–100` | Earlier layer generations: unswitched reduction, the checked S5/field-slot graph incompatibility, and the zero-switch M3 test. `gates/layer-thm-gate.md:29–49` checks the incompatibility; do not repeat that attack. Use the consolidated part for the repaired four-entry theorem. |
| `hma.md:279–409`; `gates/hma-gate.md` | Checked conditional Hessian/current identities for the relative Y3 gauge family; PH1 assumes the matching $G_1$ and row inverse. Not their walk construction on PI's literal-row class. |
| `cm-claude.md:187–221`, `cv-claude.md:94–125,164–173`, `ol.md` | Conditional companion/continuation, reality and Gaussian-assignment work. Reality, a spectral gap, or equality of the sum at one does not identify independent switched words. CM/CO remain separate owned tasks. |
| `out-gw.md`, `out-gw-issue.md:15`; `gates/out-gw-check.md` | Exposition of GW and its limits, not new supplier results. “graph bounds for $G_\pi^J$ or $G_1^J$ are not supplied” is an exclusion, not evidence that a consumer requests them. |

The library/gate symbol search also found older drafts, index/registry rows, generic variables
named $G_1$ or $q_j$, and downstream conditional applications. These are not extra proofs of
the literal current-corrected word family. In particular, all six named files requested in
the task retain the distinctions in the tables above; none proves a missing blanket graph bound.

## 3. Consumers: what is actually used

Coverage codes below distinguish **T2**, GW's three displayed graph lines, from **GW-full**,
the already written argument in §§6–8. “Conditional” always retains the actual domain,
normalization, local frame, footprint and assignment matching. It does not certify an account use.
Uses of an entire operator list are recorded as such; a list assumption is not evidence that
each listed primitive is separately used in the chart equation.

### 3.1 Direct primitive, chart and kernel consumers

| Source use, with a short quote | Operator and bound used | Does existing GW supply it? |
|---|---|---|
| I 4136–4144, `4.3:thm-small-field-step`: “Assume the operator bounds at free current” | Entire free-current package in the cited one-step theorem | T2 alone no. GW-full partly; $G_1,q_{1,J},H_1$ family and actual-class matching remain. This is a direct route into the small-field induction. |
| I 5580–5587,5666–5708,5712–5730, `4.4:def-one-family-hypothesis`, (f4),(C1),(C2): “on the same terms with the same $\kappa_\omega$” | $G_\pi,G_1,\widetilde G,G',P$ and $H,H_1,H_0$: value/gradient/Hölder norms; coarse inverses: kernel bounds; absolute restricted/switched sums, local reads | T2 alone no. GW-full supplies its own first-order/current-source pieces; not the whole one-family/covariance/setting assertion, nor the remaining $G_1$ branch. I 5705–5708 expressly excludes any Laplacian from (f4). |
| I 5872–5881 | Same families on local and extended complex polydiscs | Domain requirement; GW applies only after inclusion in its PI class. |
| I 8878–8885,8928–8941,9360–9374,9415–9424,9462–9481 | Expansion-rule properties, uniform agreement and interior sufficiency: termwise local index/value/support agreement and convergence for every list member | Not consequences of T2. PI/GW compatible footprints give a partial supplier; full prescribed-family and covariance matching remain. LRB does not erase them. |
| I 13807–13809,13824–13874 (J1): “no Hölder norm of $J$” | $\Lambda,D_U\Lambda,RG',RG'D_U^*$ and $G_0\Theta'_J$ in weighted first-order/Hölder norms | T2 alone no; GW-full §6 supplies the derivative allocation and absolute words. |
| I 13878–13920 (J2–J4): “its Neumann series converges” | $G_\pi^J$ first-order/Hölder and differentiated-source bounds; $q_J\in\mathcal K_{-2}$; $H^J\in\mathcal K_{-1}$ and transpose | T2 alone no; GW-full §6 already constructs these. No new graph bound is read here. |
| I 13924–13942 (J5–J6): “$|H^{J,T}J|_{(-4)}$” | Induced current, local $\Theta_J:E\to F$ smallness, $\widetilde G^J:F\to E$ | GW-full §§7–8 supplies these, with the stronger $F\to E^\Delta$ source inverse. |
| I 13944–13955 (J7): “arguments of (J1)--(J4) apply verbatim” | $G_1^J,q_{1,J},H_1^J$ versions of those first-order/Hölder/coarse-kernel bounds | **Not written as a literal-PI common-word result in GW.** Account gives the reduction; real B99 results and other-row PW do not cover its full independent-current switched scope. |
| I 13957–13977 (J8): “the side branches included” | Absolute analytic local words for all primitives, including both coarse inverses | GW-full covers its actual constructed branches. The $G_1,q_1,H_1$ extension and full one-family identification remain. |
| I 14033–14053;14055–14090 | $H^J$ decay/right inverse, $(I+\mathfrak R^J)^{-1}$, $\mathfrak D^J$ and transpose/second marked leg, to solve $D^J$ | GW-full §7 constructs inner small-branch/marked-leg majorants. The identity $\ell QH^J=1$ is used at one, not inferred at switches. |
| I 14295–14371, `4.5:lem-gradient-bound`: “the first five terms”; “sixth and seventh terms” | $q_J,H^J,\Lambda,D^J,\mathfrak D^J$ and transposes give $|\mathbb V'^J(A')|_{-3}=O(N(A')^2)$ | GW-full §7, seven-term majorant P16–P17. T2's third line supplies the graph readout only after composition with $G$. |
| I 14559–14618,14640–14659 (K1): “the operator $\Theta_J$” | $H_0$, bare constrained inverse, current insertion and $V'$ estimates for contraction/holomorphy of $\mathcal A_0^J$ | GW-full supplies these analytic norm ingredients on its class. Chart existence is already a printed conditional argument, not a new primitive graph problem. |
| I 14735–14800 (K3): “We bound the terms in turn” | $H^JX_G$ first-order; $q_J$ via $\mathsf k$; $\Lambda^T$; $P_0^T,q_0$; local $\Delta',F$; hence $\mathcal H^J,\Lambda^J,\mathfrak J$ size | GW-full supplies the norm products on admitted data. No $\Delta G_\pi^J$, $\Delta H^J$ or $\Delta G_1^J$ is requested. Current locality at switches has the separate M3 issue below. |
| I 14822–14865,14916–14985 (K4,K8): “Every other operator ... lies in some class $\mathcal K_a$ or is local” | Weighted $V''$, $(I+\widetilde G^JV'')^{-1}$, first variations of $D^J,\mathcal H^J,\Lambda^J,\mathfrak J$, exponential value/gradient/Hölder/current kernels | GW-full §§6–8 supplies the input majorants; the account already prints the weighted Neumann/Cauchy argument. T2 alone does not state the separate coefficient/current kernel bounds. |
| I 15278–15339,15417–15438 (K10): “Each primitive operator”; “bounds ... and their locality” | Listed primitive norms at $s$, $B_0e^{16\kappa_1}$; composite norms $Ce^{c\kappa_1}$; K1,K3–K5,K8 and zero-switch separation | T2 alone no. GW-full covers much more, including $G_\pi^J,q_J,H^J,\Lambda,D^J,V'^J,\widetilde G^J$. The $G_1$ branch is residual. The current's diagonal/locality convention is **not** supplied by any extra graph norm. |
| I 15546–15634,15770–15853 (K6): “on the diagonal” | Identification with Balaban's own-current chart; $\Lambda^J=\Delta\mathcal H^J$ and physical current increment, then first variation | Uses physical algebra at one, not a missing independent-current Laplacian estimate. GW does not extend these identities to arbitrary switches. |
| I 18136–18149 (axial frame): “For the $s$-localised chart we use” K10 | $\mathcal H^J(s)$ size/covariance with $e^{c\kappa_1}$ and footprint outside frame support | Conditional GW-full chart ingredients; frame/actual support admission separate. |
| I 19609–19620,19745–19753 (O): “not the bound involving the Laplacian” | All free-current operator bounds/walks and CMP 116 (1.11) | Residual $G_1,q_1,H_1$ first-order/coarse-inverse family; not an all-primitive graph theorem. |
| I 19638–19700,19705–19733 (F,N): “same statements ... localised in the decoupling parameters” | Chart/variation/current kernels in far terms; near chart size, locality, first derivatives; CMP 109 (3.9),(3.14)–(3.17),(3.21),(3.22),(3.31),(3.32), CMP 116 (1.21) | Conditional on GW-full plus the already printed chart proofs and frame inputs. Does not require the excluded Laplacian members. |
| I 26872–26875,26996–27002,27560–27584,28051–28072 | Formal tower expansions and local cancellation: replace global $G,H,H_1,q_J,q_1,\Lambda$ by words; “used only ... before any operator is expanded” | Local-assignment/absolute-family requirement, not a graph endpoint. Full tower recipe and same labels are separate from GW's existential compatible assignment. |
| I 47253–47295,47557–47584, `4.14:prf-form-walk-expansion` | Current insertions and branching produce $G_\pi,T_\pi^{-1},G_1,T_1^{-1}$ and the fluctuation precision sheet | T2 alone no. Account already gives conditional assembly using imported elementary sheets. GW does not identify the whole precision sheet; B99-W/CO own the matching subproblems. |
| I 56939–56953,58189–58206,58415–58430,58649–58670,58747–58762,58853–58865,58932–58945,60877–60894 | Torus independence/localized terms: one-family locality, restricted convergence, termwise reflections, and free-current bounds. I 58669: “used only ... at $U=1$” for the explicit Balaban walk substitutions there | Existing flat/PI/GW branches contribute. Full termwise covariance, common scheme and prescribed-assignment compatibility are extra; no missing curved primitive graph estimate is introduced at these sites. |
| I 92125–92138,92293–92304,142533–142543 | Field datum $j=\widetilde G_0(s)\mathsf J$, including $\|\widetilde G_0(s)\mathsf J\|_p^\Delta\le K_\sharp\|\mathsf J\|_p$ | Bare source inverse, not $G_\pi^J$ or $G_1^J$. GW's bare construction can supply its graph bound on matched domains; field-source matching remains FD/FM. |
| I 94468–94528,94571–94586 | Graph bound on linearized **nonlinear** response $T^{\mathsf L}$; physical identification with $H_1$, distinguished from $T^\sharp=H^J$ | T2 already gives $T^{\mathsf L}=(I+G\Theta_J)H_0$ through P19. `layer-thm-part.md:1010–1031` explicitly avoids a graph norm on $H^J$. Physical identification is an additional premise. |
| I 103670–103699 | Decoupled collar form built from $q_1-a-2H_1D^{(2)}[\cdot,J]$; holomorphic decaying collar kernel assumed | Not supplied by T2. Requires $G_1$ coarse-inverse/induced-current family and its precision/assignment matching, not $\Delta G_1$. |
| II 10018–10102, `5.2:cor-kernel-decay` | $|q_1(c,c')|\le C\ell_c^{-2}\ell_{c'}^{-d}e^{-\delta_1d(c,c')}$ yields fluctuation-form kernel decay; “For the first term we apply hypothesis (ii)” | **Beyond GW T2 and GW's explicit $G_1$ coverage.** Real true-current B99 B15/B16 already supplies part of this route; preserve its class. PI's bare $q_0$ is insufficient. |
| II 10589–10601 | Positivity of the $J=0$ slice inverse $\widetilde G_0$ by CMP 99b Theorem 3.11 | A positivity input, not a missing GW graph bound. |
| II 10607–10610 | Response containment: CMP 116 (1.17)–(1.22), CMP 109 (3.14)–(3.17), CMP 102b (190) | Conditional response/current estimates; extra containment is not discharged by GW. |
| II 54464–54528,54624–54661, `5.8:prop-local-decay` | $H_0,C_Q,\Theta,(I+\mathfrak R)^{-1},\mathfrak D$ in local weighted kernels at rate $8\delta_1$ | These are **bare** definitions, not the free-current $H^J,q_J$. PI/GW and the local nonlinear argument contribute, with matched data. No new corrected-primitive graph demand. II 60313–60316 lists these inputs for clause (v), separately from clause (iii). |
| II 73925–73935 | $H_1$ and nonlinear $\widetilde D$ occur in the displayed fluctuation interaction | A formation formula, not a separate bound on a primitive; reads the already assumed family/analyticity. No new graph readout. |
| III 22086–22118,22162–22181 | Natural-vertex hypothesis: $G_1,H_1,q_1$ outside $\mathfrak O$, strengthened kernels, CMP 102b (189)–(190); by-pass through CMP 109 (3.9) | Not supplied by T2. Important notation caution: this paragraph defines $G_1=(\Delta_a-\Delta^{(2)})^{-1}$ in CMP 102b's splitting. Do not equate it with the literal free-current primitive merely by its name. Natural-vertex/zone and physical-domain inputs remain separate. |
| III 35459–35460,35536 | Slice stability uses $\mathfrak G=G_1\mathfrak P^*$ | Different slice composite; needs its native inverse estimates. Not a direct demand for $\Delta G_1$; not identified by GW T2. |
| III 36153–36157,36238–36251 | Stationarity first jet pairs $H_1B$ and $D_UH_1B$ against forcing; exponential value/gradient bound (3.133) | Beyond T2; $H_1$ first-order decay required. Real B99 contribution/conditional account proof already exists; complex full-class version needs matching. |
| III 36347–36373 | Second jet uses $q_1-a$, complex-class kernel decay via CMP 99b Theorems 3.4,3.12, (3.132) | Beyond T2; residual $q_1$ family/complex first-order extension, not a Laplacian estimate. |
| III 36733–36742 | Two-depth difference of $q_1$ reduced to second-jet bounds and a segment estimate | A **comparison** estimate. Single-background GW bounds, even extended to $G_1$, do not supply it. Account prints this reduction. |
| III 37375–37429, `9.3:eq-propagator-stationarity-1` | Fine-junction two-cutoff comparison for $G',G,G_1,\mathfrak G$, with small $L^{-\theta'\min j}$ and exponential distance | **Proof outstanding** (37398). The Route names localized $\log Z$, decoupled covariance/$\Gamma_k$, and CMP 122b (1.54)–(1.55). A bounded walk family is not this cross-cutoff comparison. Do not open it as GW1. |

No other explicit `4.5:lem-free-current-operators`, K10, $q_J$, $G_\pi^J$, $G_1^J$ or
their displayed $J$-superscript chart references occur in II/III. Later uses are through the
aliases/packages above and the general-layer invocations below. Generic $G_1,G_2$ observables,
Hamiltonians, Hermitian parts, open sets and anisotropic Gaussian $G_\pi$ in III 108540ff
are different objects and were excluded from the inventory.

### 3.2 General-layer consumers, including stronger literal demands

These are the already catalogued U01–U34 (`layer-find.md:26–61`,
`layer-thm-part.md:1590–1649`). They are **not** thirty-four independent demands for
a graph estimate on $G_\pi^J$ or $G_1^J$. They consume an assumed general layer package.
Source snippets at the cited invocations were read to separate norm uses from mere existence.
In the table, **V** means size/first-order weighted response; **A** means graph size of $A'$;
**M** means reduced-current/$P_1,m_H$ and locality; **L** means general-domain/assignment matching.
GW supplies the analytic V/A ingredients on admitted matched data. M/L are separate premises.
**HΔ** means the source literally requests a graph norm of the nonlinear layer itself;
the repaired part does not assert that member.

| Use; source invocation and short phrase | Actual read; GW comparison |
|---|---|
| U01 — I 72395–72415,72500–72524, “layer theorem, clauses (a)--(f)” | Component localization, exponential profile, general field/block datum; V/A/M/L. T2 alone does not identify this package. |
| U02 — I 73132–73139, “localisation lemma for decoupled operators” | Four successive admitted links and field datum $\widetilde G_0(s)J_3$; V/A/M/L, full reached domains. |
| U03 — I 73560–73567,73629–73633, “jointly holomorphic” | Holomorphic chain on four independent switch discs; L. No new primitive graph bound is used. |
| U04 — I 89970–89975, “clauses (a), (b), (f)” | Source-presentation layer bound/locality/rider; V/A/M/L. |
| U05 — I 94196,94234,94244–94260,94284–94287, “admissible choice” | Uniform bidisc radii and small-solution constants; L and admitted operator bounds. |
| U06 — I 94308–94311,94402–94419, “vanishes at ... zero” | Existence/zero datum at two calls; no new decay or graph norm. |
| U07 — I 94476–94480,94525–94542, “difference quotient” | Graph norm of $T^{\mathsf L}=D_bh(0)$, obtained in the source from HΔ. GW T2/P19 gives this derivative bound directly, without the stronger nonlinear HΔ assumption. Physical $H_1$ identification remains PH. |
| U08 — I 94835–94842, “main ones are clauses (a) and (b)” | Existence/size at both localized sets, plus source and side clauses; V/A/M/L; not an automatic K10-to-general-layer extension. |
| U09 — I 94965–94973, “clause (b), with the norm at the kernel” | Actual bidisc output and current admission. Corrected four-entry version uses V/A/M/L; do not claim literal HΔ from the part. |
| U10 — I 95691–95699, “By the uniqueness” | Real solution and derivative; structural, not a new walk bound. |
| U11 — I 95758–95769, “Clause (c) ... Clause (d)” | Physical-current identification and gauge transport, not extra primitive graph regularity. |
| U12 — I 95877–95883, “$H''$ is covariant” | Covariance/choice of linearization; L/PH, not a new graph demand. |
| U13 — I 99788–99792,99884–99888, “floors ... localised small solution” | Uniform constant order and one ceiling; common GW choices can contribute after admission. |
| U14 — I 111514–111549, “furnished by the layer theorem” | Cut layer and current partner; graph $A'$, first-order $h$, M/L. The actual four/five-entry norms are printed at 111405,111534–111549. |
| U15 — I 112198–112212, “$N_y\le N_y^\Delta$” | First-order $HX=A'-h$ from furnished entries. Already covered conditionally; no new GW1 graph estimate. |
| U16 — I 112589–112610, “five weighted norms” | Literally includes HΔ at 112595, plus A/M. At 112603–112604 the text says the four entries are what is contained/used; part §3.4 proves those four, not all five literal norms. |
| U17 — I 114803,114841,114873, “Bound (b) of the layer-map theorem” | Weighted sizes of two healing layers and partner currents; V/A/M/L. |
| U18 — I 115389–115400, “four-entry size” | Weighted four entries at (T), cut-layer tail at (L); GW graph $A'$ is enough for the graph slot, conditional on M/L. |
| U19 — I 116567–116570,116638–116660, “each of $N_y^\Delta(\mathbb H)$” | Literal HΔ and A on the stage domain, plus local current slot. The part deliberately proves a weaker first-order $h$ entry; no universal HΔ conclusion follows. |
| U20 — I 125785–125790, “Lipschitz constant” | Stage response constant in near-pair estimates; V and L, not another primitive endpoint norm. |
| U21 — I 131642–131646,131680–131692, “layer and the source increment” | Literal HΔ profile at the T-step, current bound and physical identification. The repaired four-entry interpretation requires actual consumer matching, not a new $G_1$ graph estimate. |
| U22 — I 131725–131732, “same constants” | Localized $B_Z$ continuation/holomorphy and inherited size; L and input admission. |
| U23 — I 136759–136770, “component without data” | Off-$Y'$ zero component/restriction; L/M and support, not primitive graph regularity. |
| U24 — I 137582–137590, “decay profile proportional to” | Exponential localized response size and small shift; V/L. |
| U25 — I 137985–137994, “coincides with its input off $Y'$” | Locality of the change of variables; L/M, not a graph bound. |
| U26 — I 138657–138664,142533–142543, “in the units of $\mathfrak B^t$” | Completion-layer increments and field-source graph bound; A/M/L plus actual $G''$ source matching FD/FM. |
| U27 — II 13895–13904,13940–13959, “layer bound and the product estimate” | $N_y(h)$, $N_y^\Delta(A')$, cut current and decay; V/A/M/L. Source here already uses first-order $h$. |
| U28 — II 15398–15404, “fixed data of the response layers” | Inherited A-slot/companion/continuation inputs; not a new norm assertion. |
| U29 — II 20803–20809, “exactly one member non-local in $\chi$” | Bracket's reduced current formula and locality, specifically M. Graph primitive estimates do not define it. |
| U30 — II 23169–23175,23993–23999, “current of the dilated layer” | Carrier derivatives through $\chi h$ and its current; V/A/M/L, bump domains. |
| U31 — II 51823–51828,52044–52059, “third member furnished” | Response at nonlinear averaged datum, sizes/weights; V/L and both frame admissions. |
| U32 — II 52163–52179, “Both sides ... holomorphic” | Two exactly paired physical critical layers, equality continued in $(\beta,b)$; PH/L, not equality at independent-current switches. |
| U33 — II 52390–52404,52465–52473, “regularity at this weight” | Rippled-parent weighted response plus **relative** comparison across bases. GW bounds each admitted frame, not their difference. RC is separate and the source marks linear closeness “proof outstanding”. |
| U34 — III 49219–49226,49280–49286,49459–49464,49491–49497 | Relaxed earlier-frame admission and boundary-crossing localization; L/M. Neither PI nor GW certifies that literal relaxed class. |

The literal nonlinear HΔ citations extend beyond that invocation inventory:

| Source | Actual use and available prior work |
|---|---|
| I 117573–117577 | Uses HΔ to bound $N_y(\chi h)$. Only first-order $N_y(h)$ is read in the ensuing inequality, so the weaker part suffices for this particular calculation. |
| I 136304–136321;137272–137291;140158–140179;140825–140844;141784–141795;142191–142205 | Reuses T-step/stage HΔ profiles for raw-point displacement, majorant/admission and collar/current bounds. These are inherited layer hypotheses. Small positive decay is expressly distinguished from vanishing at raw points (140826–140836). No primitive $G_\pi^J$/$G_1^J$ Laplacian bound is derived. Actual weakening must be checked at the named displacement/containment consumer. |
| I 147739–147746,147849–147853 | Physical Landau response $\mathcal H'$ has $e=0,1,2$ derivative decay at observation points, imported as hypothesis (dec), CMP 102b (190), then used for $P_1\mathcal H'$. Physical chart, not arbitrary independent-current K10. GW T2 alone does not supply this second-derivative assertion. |
| II 55095–55160,55213–55217 | `5.8:lem-critical-size` **already prints a conditional proof** of $N_y^\Delta(X)$ under weighted calculus, critical-point existence/analyticity and the specific field identity (55119–55126). It then calls $X$ the response $\mathbb H$. This is a possible matched supplier, not a universal consequence of K10 or a reason to re-prove a new graph theorem. |
| II 57533–57547,57554–57567,57659–57666 | One-cutoff sizes use that critical-size lemma for HΔ of $\mathbb H^w$ and $\mathbf H_j$; the datum estimate at 57663 uses only the value member. Their critical-point/field-identity hypotheses remain. |
| III 38074–38117,38135–38142 | `9.5:def-box-response` requires increments with $\ell^3|\Delta_Uh|$ and uses them in presentations. Its response is a small critical point of an **external response lemma** with multiplier $H_U^\dagger J$. A matching theorem is required before treating this as the K10 chart or S5 layer. It is not proof of that identification. |

**A completed negative finding must not be re-attacked.** `layer-r2.md:436–446,795–846`
proves the incompatibility of a common positive analytic datum radius for the proposed
general-field (S5) realization with its extra HΔ correction bound (B4). It already fails
at flat $W=1$, switches one, weight one, fixed physical volume; mesh uniformity is the loss.
`gates/layer-thm-gate.md:29–49` records Claude's line-by-line check, first failing step none.
At 49 the checker explicitly says this **does not refute the block-only chart**; it uses
the field slot. Thus neither a universal HΔ assertion nor its block-only refutation may be
claimed here. The consolidated part states “There is no graph-norm conclusion for $h$”
(`layer-thm-part.md:378`) and labels its U table “weaker corrected norms” (1590–1593).
That declared repair must remain visible when comparing it with the account's stronger wording.

### 3.3 Uses beyond GW, separated by the actual missing requirement

1. **A residual first-order/coarse-inverse family:** I 13944–13977 (J7–J8), I 15322–15324
   and 19609–19620, the one-family consumers, I 103670–103699, II 10018–10102,
   III 36245–36251 and 36359–36373. They require $G_1^J,q_{1,J},H_1^J$, their local words,
   weighted value/gradient/Hölder/transpose estimates and scale-correct coarse kernels.
   GW §§6–8 does not explicitly finish this branch on its common literal-PI class.
   B99 already covers the real true-current subcase; do not duplicate it.
2. **Literal nonlinear HΔ / second-derivative assertions:** the HΔ rows above and physical
   observation-point (190). They are not consequences of T2, and the general S5 version has
   an existing checked obstruction. First determine the actual equation/domain and which weaker
   entries the consumer accepts. This is LAYER-THM/matching work, not a new $G_1$ graph theorem.
3. **Switched current and exact locality:** K10's current separation, U01/U14/U16/U19/U21/
   U27/U29/U30 and the other rider uses require M. More decay does not fix an unassigned
   local diagonal. The M3 obstruction is already recorded and checked.
4. **Assignment, covariance, admission and comparisons:** (f1)–(f4)/uniform agreement/LRB,
   the collar form, U33 and III 37375–37429 retain distinct requirements. They are not supplied
   by the three T2 inequalities or by adding more endpoint derivatives.

**No T0 use was found demanding $\Delta G_\pi^J$ or $\Delta G_1^J$ at arbitrary independent
current.** The account excludes them. There **are** T0-route uses beyond GW's three lines,
including the coarse $G_1$ inverse and general-layer/current packages. “No further graph
bound on these two primitives” must not be rewritten as “no remaining T0 consumers”.

## 4. What the account proves, assumes, or marks incomplete

The source's conventions, I 27–56, distinguish printed proofs of implications from cited
inputs. An unmarked heading is not an unconditional closure of its hypotheses.

| Locus | What is actually on the page |
|---|---|
| I 13143–13173 | $q_0$ bounds and walks: “without proof” and “cited as printed”. The quoted sentence mentions **both** $(QGQ^*)^{-1}$ and $(QG_1Q^*)^{-1}$. It is not a printed inverse-walk proof. |
| I 13674–13677 | Bare propagator bounds quoted by statement: “their proofs are Bałaban's and are not reproduced”. |
| I 13681–13978 | `lem-free-current-operators` has a printed conditional proof J1–J8, with explicit bounded-current derivative allocation and Neumann series. J7 is the short reduction at 13944–13955; J8 cites local propagator constructions and concatenates their words. **Do not describe this as absent proof work.** Its bare inverse-walk and analytic averaging hypotheses stay separate. |
| I 13981–14090 | Nonlinear correction proof ports CMP 102b Proposition 3 and derives the marked derivative identities. It assumes the analytic/uniform CMP 98 Proposition 5 extension. |
| I 14198–14371 | Seven-term differentiation and quadratic gradient proof are printed, with the extra free-current terms treated separately. |
| I 14455–14494 | Representation identity proved **at the unswitched operators** by inverse/constraint identities. This is algebra, not a norm-only consequence. |
| I 14544–14663,14730–14800,14869–14985 | Conditional chart contraction, linear size, weighted Hessian/first-response kernel proofs. These are reusable account arguments, not fresh open derivations. |
| I 15342–15462 | K10 has a printed concatenated-walk/spare-exponential argument; it assumes inverse walks. At 15430–15438 it claims the earlier chart proofs need only bounds and locality. M3 limits what can be inferred about the current's switched diagonal/locality. |
| I 166593–166598; III 111327–111333 | Two separate missing published inputs: inverse constrained-covariance walks, and “walk expansions of the further operators ... after Theorem 3.9”; both “printed without proof; cited as printed”. They must not be merged into an assertion that no current-correction proof exists anywhere. |
| I 47253–47599 | Conditional form-sheet assembly is printed, but imports elementary sheets and prepared-data hypotheses. It is not a fresh derivation of all their published propagator inputs. |
| II 10009–10102 | Kernel decay of fluctuation form is proved **assuming** the corrected coarse-inverse kernel bound. This is an actual consumer, not that bound's proof. |
| II 55095–55217 | Conditional critical-size argument exists for its own critical point/field identity. Reuse it if the actual response is matched; do not silently identify different maps. |
| III 35577–35625 | CMP 102b (189)–(190) quoted as “printed without proof”; quotation: “We do not perform these calculations here”. The free-current chapter prints its own restricted replacement, while this later physical statement still imports the published form. |
| II 52398–52404; III 37398–37429 | Rippled-parent linear closeness and fine-junction propagator stationarity are marked “proof outstanding”. These are comparison problems, not just absolute decay. |

I 20132–20149 is particularly decisive: the operator theorem does **not** assert free-current
$\Delta_U\mathcal H^J$, $D^*D\mathcal H^J$, their variations/localized pieces, or equality of
individual switched pieces with Balaban's pieces. The last distinction is explicit even though
the sums coincide at one and on the diagonal.

## 5. Published route available to port

This is the account/repository's report of the papers. Their full proofs were not available
for fresh inspection under this task's source restriction.

* **CMP 99b:** Theorems 3.1,3.3,3.4 supply bare/local complex estimates, (3.42)–(3.47),
  (3.49). Theorems 3.7,3.9,3.10 give the local walk constructions cited at I 13957–13965.
  Theorem 3.12 and (3.130)–(3.138) give the successive current-correction route, with
  (3.132) coarse inverse and (3.133) lift estimates. Their Laplacian exclusion is explicit.
  The inverse-family sentence preceding (3.132) omits the proof by analogy; so do the further
  walks recorded after Theorem 3.9. A published **route** exists, but the account itself
  identifies an omitted proof. Calling the entire missing word-family result a published
  proof would overstate this evidence.
* **CMP 102b:** Proposition 3, (50)–(58),(63)–(73), constructs the nonlinear correction
  from a decaying bounded linearizer; (129),(131),(143),(179),(180) organize the background
  equations. Proposition 9 supplies the analytic physical chart. The additional derivative
  estimates (189)–(190) are explicitly not calculated there. The account's free-current
  J/K arguments and GW already rebuild relevant restricted parts.
* **CMP 109:** Independent-current regular pairs are the domain framework; (1.10)–(1.19)
  and (3.6)–(3.17),(3.21),(3.22),(3.31),(3.32) are the chart/activity consumers.
  (2.3)–(2.11) use the corrected coarse inverse/lift in the Gaussian step. (3.11), p.272,
  is the local current remainder. These citations do not license differentiating a merely
  bounded independent $J$, imposing an own-current identity off that graph, or assuming
  every relaxed continuation lies in the published domain.
* **CMP 116:** (1.2),(1.4) give the response splitting; (1.6)–(1.7) give walks/tags/spare
  exponentials; (1.11) gives operator growth $e^{16\kappa_1}$; (1.15),(1.18) support
  contraction with operator bounds; (1.17)–(1.22) are response/localization uses.
  Its operators-as-data principle does not retain inverse/constraint identities at arbitrary switches.

The ready-to-use port is **CA J7 on top of GW §6**, followed by its coarse compression and
reversed-chain estimates. It is not a reason to reconstruct Balaban's entire propagator theory,
redo PI, redo GW's $\widetilde G^J$ graph proof, or redo the B99 true-current gap.

## 6. Verdict and the smallest defensible next task

**(a) Critical path.** There is a residual relevant to T0's chosen account route, but **GW1
as an all-primitive graph-endpoint theorem is not the right statement**. The independent-current
$G_1^J,q_{1,J},H_1^J$ first-order/coarse-kernel walk branch would finish that portion of
J7–J8, K10(1), and `4.5:thm-operator-bounds` (O). It would provide inputs to
`4.4:def-one-family-hypothesis`, the decoupled collar form and `5.2:cor-kernel-decay`.
It would not by itself finish their assignment, covariance, physical matching, positivity,
or local-data-domain hypotheses. LRB remains an implication from those hypotheses.

For the **graph part of the general layer's corrected four entries**, GW T2 already gives
the required $A'$ estimates and the zero-datum $T^{\mathsf L}$ estimate. No additional
$G_\pi^J$ or $G_1^J$ Laplacian theorem was found on the T0 path. The literal stronger HΔ
wording, its map identification and the current rider belong to the already owned
LAYER-THM problem. Its S5/field-slot HΔ extension has a checked obstruction. **Stop a
proof lane aimed at that extension; do not give it a new GW1 name.**

**(b) Minimal statement if a residual port is commissioned.** On exactly the admitted PI
class and the GW common constant order, extend the **existing** absolute first-order
word algebra to $G_1^J$, $q_{1,J}$ and $H_1^J$. Require:

* the J2 value/gradient/Hölder and differentiated-source members, with the positive Hölder
  exponent gap retained; no Laplacian member for $G_1^J$;
* $q_{1,J}\in\mathcal K_{-2}$ with density bound
  $C\ell_c^{-2}\ell_{c'}^{-4}e^{-\delta d(c,c')}$ and physical column majorants;
  $H_1^J\in\mathcal K_{-1}$ with the J4 first-order/Hölder readouts and physical transpose;
* analytic words defined on complete local reads, absolutely summable endpoint/branch
  majorants with spare tree decay, restrictions equal on common footprints, and zero-switch
  component separation for **these primitives**;
* expansion at one followed by the account's primitive union tags, $Ce^{16\kappa_1}$
  primitive bounds on $|s|\le e^{\kappa_1}$ above the GW cube floor, with the current
  ceiling fixed before $\kappa_1$. Identification is for this precise assignment.

Do not re-prove $G_\pi^J,q_J,H^J,\Lambda,D^J,V'^J$ or $\widetilde G^J$ merely to enlarge
the displayed theorem. Their pertinent majorants already appear in GW. State the new result
as a port of CA J7 and an extension/corollary of GW's word algebra, not a frontier derivation
of a result the account never treated. Reuse B99's true-current subcase; full true-current
precision work and prescribed-sheet transfer remain with B99-W and CO/`ol`.

**(c) Safe route and the switch restriction.** At one put
$K_J=\Theta'_J+\Pi^T\Theta_J\Pi$. CA I 13944–13955 supplies the decomposition
\[
 \Pi^T\Theta_J\Pi A=f'-D_U\varphi',\qquad
 f'=\Theta_J\Pi A,\qquad \varphi'=RG'D_U^*f'.
\]
Use GW's scalar divergence and vector Hölder-source words, and their reversed chains,
to bound $G_0K_J$ by $C|J|_{-3}$ in the needed absolute algebra. Then port the series
\[
 G_1^J=(I-G_0K_J)^{-1}G_0,\qquad
 q_{1,J}=\bigl(I+q_0Q(G_1^J-G_0)Q^*\bigr)^{-1}q_0,
 \qquad H_1^J=G_1^JQ^*q_{1,J}\ell^{-1}.
\]
These are **unswitched** identities used to generate words. Expand every current-induced
weight, scalar branch and coarse correction before tagging. Apply GW's footprint-tree
count and spare exponentials to each complete primitive concatenation. Products of
tagged primitives retain product tags. Neither resolvent inversion of the tagged sums
nor a representation identity may be silently substituted after switching.

In particular, M3 is not a smallness failure. `layer-thm-part.md:1440–1461` and
`gates/layer-part-ref.md:187–274` describe the all-zero-switch flat test: the untagged
mass term leaves $-Q^Ta\ell^{-1}b$ while a zero-component current would vanish.
The representation proof at I 14455–14494 used exact inverse/constraint identities.
I 15450–15451 leaves its scope too wide. Safe use is at one; away from one one must
define and match the reduced current's localized diagonal ($P_1(s),m_H(s)$) separately.
No stronger absolute endpoint estimate repairs this algebraic/assignment problem.

**(d) First hard step.** For the narrowed port, write the **termwise**, row-and-column,
scale-correct bound on $G_0\Pi^T\Theta_J\Pi$ with every scalar branch and identity
footprint included. The account's summed “apply verbatim” sentence is not yet a written
literal-PI common-word estimate. The work must allocate the derivative onto adjacent
inverses without differentiating $J$, keep the exponent gap, and absorb carrier/tree costs
before fixing the current ceiling. The subsequent Neumann/compression route is already
specified in J3/J7 and GW §6. This is the first unfilled port step, not a claim that it is
an unresolved theorem of the literature.

For an **end-to-end layer result**, the next hard decision is instead the actual map/current
assignment and full-domain admission, including M3 and the relation to the separately
printed critical-point construction. That problem is already owned by LAYER-THM. Extra
$G_1$ bounds alone do not unblock its last two current entries, U33's relative comparison,
or the account's unrestricted general-layer assumptions.

Verification limit: this is a bounded-source digest, not a line-by-line independent check of
the cited proofs or a claim of T0 closure. Searches cover the explicit target symbols,
legacy $G,G_1,H,H_1$ names, package references and traced layer aliases; the U inventory
is reused from the existing source map and checked at the listed invocation snippets.
No claim is made to have read the entire account or every downstream theorem wholesale.
The recorded mathematical obstruction is a prior checked result with its original scope.

Digest by Codex (gpt-6.1-sol).
