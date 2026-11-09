## Repo search

The lead's `repo-search-2026-11-08.md` is a retroactive search report for
FINISH row 531, not row 629. Its searches cover `origin/main` and PRs #10114,
#10133, #10134 and #10141, but its targets are PI, GW, M3, TPI, GEOH and
other November 8 items; it records no COV or `i3-cert` hit. I read that
search report and the local `library/i3-cert.md` sections 4 and 5.4 as row
629 directs. The local note identifies COV as the unproved test-to-footprint
assignment (section 5.4, especially lines 367–418). The open-registry entry
at line 1006 confirms COV is open and splits the follow-up: row 628 handles
footprints in X; row 629 reads structures outside X; after this reading the
lead is to write the outside-X proof item. Row 630 owns a later check of
`i3-cert.md`, not this reading. This exact scope means the nearby ownership
does not cover the requested outside-X read. The lead's row-531 digest does
not name a row-629-specific prior result. This checkout is pinned at the
requested commit; I did not check out other branches into it.

lead: OpenAI/Codex (gpt-6.1-sol)/high, reading lane
lease_until: 2026-11-09 23:59 UTC

# COV reading: assignment outside X

Reading report for FINISH row 629, at repository commit
`9a566ab6d8e409a4c62d9696bd2d87b4830ac3cd`. This is research text, not an
audit and grants no status. The report records what Sussman and Alpoge's Y
text says; it does not prove or assess those statements. Credit for the
account and outline: Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text.

## 1. Definitions and usage

The terms below are indexed from the requested COV passages and their
operation/sequence introduction. “Used without definition” means that the
quoted Y passage uses the phrase but does not define it there; it is not a
claim that no related construction occurs elsewhere in the book.

| Term | Y text | Status |
|---|---|---|
| departure | “For each test place in a stopped component use its least-level departure” (65425–65426). | USED WITHOUT DEFINITION; the sentence invokes rather than defines departure. |
| least-level departure | Same sentence, 65425–65426. | USED WITHOUT DEFINITION; no ordering rule for “least-level” is stated there. |
| standing departure | “A standing departure below the current waiting window keeps its earlier determining reads and averaging completions” (65467–65469). | USED WITHOUT DEFINITION; its retention rule is stated, but not what makes a departure standing. |
| stopped component | “For each test place in a stopped component…” (65425). | USED WITHOUT DEFINITION in the assignment passage. |
| untouched component | “If the component is untouched…” (65426). | USED WITHOUT DEFINITION in the assignment passage. |
| island | “A healed component leaves the label; an island passes the earlier tests and fails the last” (1176–1177). | DEFINED by the stated outcome distinction (healed / island / drop-out). |
| drop-out | “A drop-out fails after (n\leq\mathsf N_t) stages and keeps those stages” (1177–1178); later, a failure of one of tests (1)–(3) makes that component drop out and remain live (63876 onward). | DEFINED by the operation's outcome and retained stages. |
| restored core | “At a restored core the bound comes from the retained reference cutoff and the surrounding ordinary tests” (65431–65433). | USED WITHOUT DEFINITION in the assignment passage. |
| waiting window | “An operation can use its waiting window only when (t_\flat=t-\mathsf N_t\geq0). Before then it is not eligible” (1182–1183). | DEFINED BY REFERENCE to the stage count (\mathsf N_t); this gives eligibility and lower endpoint, not a separate geometric definition. |
| inset of the stage test region | “If … the full footprint misses the inset of its stage test region, the ordinary density test supplies the bound” (65426–65428). | USED WITHOUT DEFINITION in the assignment passage. |
| action top | “The same ordinary test is used at untouched higher levels and on the unchanged action top” (65429–65430). The action sequence is the (\boldsymbol\nu=0) choice in (1176–1202), governing sums and coupling profiles. | DEFINED BY REFERENCE to `eq:rg-objects-R21` (the action sequence); the local phrase “action top” is not separately defined. |
| determining sequence / action sequence | “The choice (\boldsymbol\nu=n) is the determining sequence; it governs backgrounds. The choice (\boldsymbol\nu=0) is the action sequence; it governs the sums and the coupling profiles” (1199–1202), following the piecewise region definition in `eq:rg-objects-R21`. | DEFINED, with the region formulas in `eq:rg-objects-R21`. |
| prepared face (seam) | Y refers to “the crossing plaquettes of the prepared interface” and says they “require the comparison below” (63876); it later names “a prepared face” and locates it relative to (Z''_q) (77609–77620). | USED WITHOUT DEFINITION as a named boundary in these passages; the text supplies locations and separation rules, not a definition of the term. |
| collar departure | “On a collar departure include the approximate test on the collar links” (76663–76665); the earlier rule calls it a “sharp collar split” after (n) integrations (65436–65445). | USED WITHOUT DEFINITION; the split and its tests are described, but the phrase itself is not defined. |

The operation's three outcomes are specified at 1176–1178. The history
structure and its phase are further defined at 1204 onward, but those do not
add definitions for “stopped component,” “untouched component,” “least-level
departure,” or “collar departure.”

The Sussman–Alpoge outline separately defines its three fates and its two
region sequences at SA 17415–17440 (indexed in `sa-index/chunk-16.md`); those
outline definitions are not transferred into Y here.

## 2. Moves carried by a history

Y describes operations and test timing across 63836–63876, 65459–65474,
76654–76689 and 77741–77763. The list records only the integrations, rows,
tests and removals that those passages name.

| Move | Integrated or drawn variables | Determining rows changed / preserved | Tests and delta factors inserted or retained | Tests removed, and when |
|---|---|---|---|---|
| Ordinary stage | The stored variables in the outer shell of (Z_{j+1}\cap X) are integrated “one value after another” (63836–63842); the stages proceed for (j=k_\flat,\ldots,k-1). | The staged shells carry fields (V_j) and form (V'') on prepared determining set \(\mathbf B''\) (63838–63847). The later global account says levels below (j) retain rows, while level (j) can lose rows and new rows are imposed outside the old region (65536–65560). | Before each stage: localized regularity test \(\chi_i^{(n+1)}\), collar gauge, approximate closeness \(\chi'_j\) at (2\delta'_j\), and completed step-(j+1) fluctuation tests (77741–77748). The stage condition on the shell and its threshold ladder are given at 63864–63876. | Earlier indicators are removed only if they equal one on the complete chart used for removal (77751–77757). The sharp collar split follows removal (77761–77763). |
| Removal of a stage test | No field draw is assigned to removal itself. | It uses the retained averaging deltas and the top/core density tests, plus lower and higher one-step tests still in the term (77744–77747); the promoted coarse row remains fixed by its averaging constraint (65450–65455). | The new positive stage test and the approximate collar test on old collar variables are the suppliers after removal and before integration (65459–65465). Any still-active indicator remains part of the real collar integral (77757–77761). | “Remove an old indicator only when it equals one on the complete chart used for its removal” (77751–77755); timing is after the new stage/collar guards and before the sharp split/integration (77741–77763). |
| Integration / main step | Integrate (V_k) over the prepared box \(\Lambda^{\rm pr}\); prior level-by-level integrations resolve the bare chain of Haar variables and averaging deltas (63847–63859). | The bare chain is resolved top-down; (V_k) becomes a free Haar integral over the box, with averaging constraints used in the elimination (63850–63862). | Carried factors displayed include \(\chi_k\), \(\chi_{k,\Lambda}\), core tests \(\chi\), shell tests \(\chi''_k\), action \(A''_k\), and \(\delta_{\rm ax}\) in the normalized reference law (63859–63876). | The passage says the core operation containing failed tests is “at no point unfolded” (63868–63872). It does not give a general list of other test removals beyond the stage-removal rule above. |
| Late Haar refresh | A fresh Haar field is used for outgoing rows; the old determining datum is retained in the inner slot (65470–65474; 76677–76681). | The refresh leaves the old determining datum and its test values in that inner slot; outgoing rows use the fresh field (65470–65474; 76677–76681). | Existing inner-slot test values remain there (65470–65474). | No inner test is removed by the refresh in these assignment passages. |
| Restoration by reference law | A reference-law draw changes the datum itself; the prepared operation uses (V'_k) in the reference-law numerator and denominator and restores block variables through normalized reference laws (1174; 63862–63868; 76677–76689). | The restored datum has new tests as suppliers; the restored-box links are compared with the reference (65472–65474; 76681–76689). | Retained reference cutoff plus surrounding ordinary tests bound a restored core (65431–65433); at an island the reference uses bounds from the passed extendibility test and surrounding density cubes (76681–76689). | Y does not give a separate exact removal time for the replaced datum's tests in these assignment passages. It says that tests of the restored datum provide the new bound where restoration replaces the field (65472–65474). |
| Drop-out | A component that fails one of tests (1)–(3) drops out, remains live, and its failed occurrence counts as a creation; it keeps its completed stages (63874–63876; 1176–1178). | The determining sequence uses \(\boldsymbol\nu=n\), the action sequence \(\boldsymbol\nu=0\); outside affected levels the label regions are retained (1193–1202). The stopped component uses its recorded departure place (76661–76665). | The failed sharp indicator remains a separate factor; the positive \(\chi_i^{(n+1)}\) and collar test at (2\delta'_j) are listed at the sharp split (65436–65448; 77741–77763). | The failed sharp indicator is not described as removed; it is “carried as a separate factor” (65444–65446). Other old indicators follow the complete-chart rule at 77751–77757. |
| Healing of a component | The quiet operation first integrates stored fields in \(\mathsf N_t\) stages, then extension, inner-box integration in axial gauge, reference restoration, exponent localization and a last test (1176–1178). | A healed component leaves the label (1176–1177); old marks disappear when swallowed by a healed component or island (1202–1204). | Earlier tests pass and the last test determines healing versus island (1176–1178). For a quiet containing component, the old top test enlarged by four cells covers the outer six cells (76681–76689). | No standalone removal time is given for healing in these passages; the label/mark removal is at the healed outcome (1176–1177; 1202–1204). |
| Core operation | The core \(C_{k_\flat}=X\cap Z_{k_\flat}\) is integrated by \(\mathbf T_{k_\flat}(C_{k_\flat})\), with core variables appearing in the displayed integral (63842–63847, 63858–63867). | It is kept as an operation containing the failed tests; Y says it is not unfolded (63868–63872). | Core plaquette tests \(\chi\) and averaging deltas remain under the core operation (63858–63867; 77744–77747). The level-(k_\flat) last-shell test is stated at 63868–63872. | No test-removal moment is assigned to the core operation; the text emphasizes that it stays intact (63868–63872). |

## 3. Assignment table in Y

“Moment” here means the timing Y itself states: before the first stage,
while a test is carried, after removal/before integration, or at a later
datum-changing move. The table is descriptive, not an inference that a
single test covers all mixed footprints.

| Test place | Structure, level, footprint position | Supplier named by Y and threshold | Carried between moments (as Y states) |
|---|---|---|---|
| Untouched ordinary datum | Outside a stopped component, including untouched components; ordinary place at its original density cube | Original ordinary density test; ordinary defect order \(\varepsilon_q\) (65426–65430; 76654–76672). | Before the first stage use the untouched datum; ordinary test at unchanged places (65459–65462; 76654–76660). |
| Untouched higher level / action top | Higher levels untouched, or unchanged action-top region | Same ordinary density test at original cube (65429–65430; 77813–77818). | Original density test remains the supplier for untouched action-top reads (77813–77818). |
| Stopped component, shell interior | Test place in stopped component, at its least-level departure; full footprint in the inset/tested shell | Last positive stage test at that departure (65425–65433); for stopped-component assignments Y also says use the last applicable stage guard when full union of corner blocks lies in its tested inset (76661–76669). | Use the test carried at the relevant moment; positive stage guard supplies while carried (65459–65463). |
| Stopped component, footprint exits inset | Full footprint misses the stage-test inset or extends outside the tested inset | Original density cube/test on the complete exterior read (65426–65428; 76664–76669). | Ordinary test is used at the current carrying datum before marginalizing; the complete exterior read is retained (76654–76669). |
| Remade shell | Shell at level (q), footprint in the shell | Stage witness with bound factor \(C_L L_\flat^{2(q-k_0-1)_+}\) (76669–76672); earlier general stage ladder describes the same (L_\flat^2) overlap loss (63864–63876). | Latest applicable positive stage guard at the recorded departure; Y says to use the tests carried at that moment (65431–65434; 65459–65469). |
| Sharp collar departure | Operation at level (i), after (n) collar integrations, (j'=i_\flat+n); level-(j') footprint in the positive-test inset and a corner in collar | Retained \(\chi_i^{(n+1)}\) plus approximate collar bound on old collar variables at (2\delta'_{j'}); failed sharp indicator is separate (65436–65448). Collar loss factor is (c_f L_\flat^{2(q-k_0)_+}\) (76669–76672). | After removal and before integration, use the new positive stage test plus approximate collar test; sharp split occurs after removal (65459–65465; 77741–77763). |
| Promoted level / direct exterior collar | Level (j') promoted row; direct exterior collar links and completed bonds | Promoted coarse row fixed by averaging constraint; direct exterior retained links have no endpoint in next old member; completed bonds use both full blocks outside it (65449–65457). | At promoted level the constraint is retained; original strip tests remain suppliers for old-wall fluctuation reads (65454–65458). |
| Restored core | Core after reference-law replacement; surrounding ordinary region | Retained reference cutoff and surrounding ordinary tests (65431–65433); restored-box comparison with reference gives (C(M)\varepsilon_i) (76681–76689). | New restored-datum tests supply the bound where the field is replaced (65472–65474; 76681–76689). |
| Prepared sequence inside X | Level (q<i), place in (Z''_i\subset O_i), complete footprint is four order-(q) blocks, inside spatial inset | The passage says the full footprint is in (Z''_i); top tests in the original top action region keep halos (78299–78315). For a lower footprint meeting an earlier shell seam, the literal shell test covers only bare plaquettes wholly contained in that shell; the comparison test at the last prepared seam supplies a different plaquette set (78316–78320). | Keep prepared variables before marginalizing; on the admitted incoming fibre carry the bound as support on the prepared datum, before old averaging deltas are integrated (78320–78331). |

The global/local paragraph at Y 65019–65067 gives the joined comparison and
incoming-support bounds: collar read-set comparison is \(C\varepsilon_\star
e^{-cM\check R_m}=o(\delta'_j)\), and prospective guards use promoted datum
bounds \(C e_q\) “before their delta functions are integrated.” Those are
stated for the collar read set and prospective joined datum there; they are
not worded as the labelled all-entrances theorem asked about in section 6.

## 4. Literal clause and footprint qualifications

These are the file's nearby statements that distinguish literal test
plaquettes from complete averaging/test footprints or name a comparison
supplier. They are grouped by the affected interface.

| Y lines | What literal coverage does not give / what differs | Remedy named in Y |
|---|---|---|
| 64063–64065, 64081–64086 | A test-cube box can meet the old wall; the joined comparison reads a stated footprint and “does not require the discarded sharp bound at the artificial bare rim of X.” | Use the ordinary coarse density test and retained rows; the joined comparison on the complete stated footprint supplies the bound (64075–64086). |
| 64096–64101 | Density cubes cover plaquettes near the old seam; in the other case new plaquette averaging blocks lie in the preceding level-(j) member and outside old \(\Omega_m\). | Use the density test on the first case, or the exact one-step average of the old determining rows on the other (64096–64101). |
| 64151–64164 | A pivot crossing the old \(\Omega_m\) seam is absent from the finer determining set under the no-inward convention; crossing rows have an outside block in the collar. | Use the approximate collar test, the retained average, real response and node factors, before the sharper split (64151–64164). |
| 64214–64230 | The earlier guard's support is confined to (X\cap\Omega_m^c); the artificial bare rim occurs only in the final guard. | Keep complete footprints in the comparison region and use the preceding-guard seam comparison (64214–64230; label `hi:preceding-guard-support`). |
| 64465–64474 | The literal final continuation and inset continuation differ by omitted indicators; they are not the same set of clauses. | Split the difference sectors with \(\kappa_\times\) and its complement, preserving each branch's kernel and stage count; comparing the rule itself requires comparing kernels on those sectors. |
| 64583–64595 | A bound only on support of the literal prospective guard gives neither the complete-chart condition nor acceptance of the reference ball needed for an inset rule. | Put the preceding curvature guard in fixed-domain form and prove it accepts the reference ball; use the real collar path for remaining inset-positive evaluations (64583–64595). |
| 65042–65045 | Old groups of tests at the original \(\Omega_q\) seam need their full four-layer test-cube enlargements. | Use the preceding wall comparison and those enlarged carriers (65042–65045). |
| 75832–75836 | A row crossing the new prepared face belongs to a seam; its middle fine bond may itself cross into \(\Omega''_{j+1}\). | Assign the pivot to the actual integration/reconstruction and read lower inputs through the preceding operation (75824–75841). |
| 77557–77590 | A complete test footprint can meet both sides of a prepared face even though the bare guard uses plaquettes contained in individual shells; sharper earlier-shell thresholds need a bound on the full footprint (78384–78386). | Use the coarse datum at the preceding averaging fibre; use full original density-test halo before removal at the original wall, or the preceding exterior guard on the full carrier, then carry its bound through the exact average (77557–77589). |
| 77609–77656 | At a compressed prepared seam, complete footprints meet \(\partial Z''_q\); a remaining footprint may meet an original wall. | Use the deep/exterior preceding guard on the full footprint and retained averages; at an original face use that face's density test before removal (77609–77656). |
| 77810–77828 | For a datum plaquette, its full footprint may leave the stage-test region, exceed (j+1), or belong to untouched top; these are outside the literal stage clauses. | Use its smallest-level drop-out's recorded place and full endpoint-block footprint, then the original action-cube density test, or the core tests; within coverage use \(\chi_i^{(n+1)}\) and collar \(\chi'_j\) (77810–77828). |
| 78299–78320 | A lower footprint may meet an earlier shell seam. Literal shell bound covers only bare plaquettes wholly contained in that shell; last prepared seam comparison supplies “a different set of plaquettes.” | Use the real endpoint comparison, retain prepared variables before marginalizing, and carry the incoming-fibre bound as a support condition (78316–78331). |
| 78384–78386 | A sharper earlier-shell seam test must bound the complete footprint. | Supply the bound on that full footprint (78384–78386). |

## 5. Symbols

**\(\psi_l\).** Its only occurrences are Y 65477 and 65478. The first
says “The witnesses on the complete footprints give
\(2\psi_l\varepsilon_l\) for the datum defect.” The next says
“\(\psi_l\) is \(O(1)\) for an ordinary witness or a restored core and is
bounded by \(C(\log\theta_l)^r\) on the remade shells.” Y gives these
casewise bounds, but no separate definition of \(\psi_l\) in these lines.

**\(L_\flat\).** The occurrences relevant to its role are:

- Y 1234–1235: a radius lift is (L_\flat^{2e_\sigma(x)}), with fixed
  (L_\flat\geq1).
- Y 63864–63876: (L_\flat) is an integer, (2\leq L_\flat< L/2),
  chosen with (L), requiring (L\geq5); each overlap gives a factor
  (L_\flat^2), and the shell factor is
  (L_\flat^{2(i-k_\sharp-1)_+}).
- Y 64259: the exterior threshold ratio contains
  (max{L_\flat^2,3})/L^2. Y 64311, 64383 and 77627 define/use the shell
  factor (F_j=L_\flat^{2(j-k_0-1)_+}); Y 64354–64359 compares the reserve
  using (L_\flat/L)^2.
- Y 64414 has zero exterior power in the uncompressed range; 64751 uses
  (max{3,L_\flat^2}); 64768 states (L_\flat<L/2). Y 71291–71293 again uses
  (L_\flat<L/2) for the adjacent-shell threshold comparison.
- Y 65481: the remade-shell logarithmic bound is said to use
  (L_\flat^2<L).
- Y 68349, 68550, 68609–68614, 68625, 69884, 71400, 76669–76670,
  77627, 77639 and 78097 use powers or comparisons involving
  (L_\flat). At 68614 Y chooses a fixed geometric floor with
  ((8\log L_\flat+1)/\varrho_0\le\kappa/2); at 77639 it uses
  (L_\flat<L) in the compressed-seam estimate.

Thus (L_\flat^2<L) is **not** stated as an independent standing condition
in the construction passage: its standing choice (L_\flat<L/2) already
implies it for (L\ge5). Among conditions on (L_\flat), the explicit strict
square inequality occurs only at Y 65481. Y 77639 uses the weaker
(L_\flat<L) in a separate compressed-seam estimate.

## 6. Global statement and uses

Yes, as an **anchored prose subsection**, not as a numbered theorem:
`hi:prepared-real-endpoint` begins at Y 65409. Its assignment at Y 65417–65485
addresses each test place of the current carrying datum at the relevant
moment, says the witnesses give the datum defect, and concludes “each test
gives a bound C e_l directly” (65475–65485); it then fixes an entering point
on the retained tests. The anchor therefore labels the per-test,
entrance-based assertion in the form asked. Y 65536–65560 separately gives
the levelwise calculation for the fixed prospective global orbit. At Y
65019–65067 the collar read set has a joined comparison, prospective guards
use promoted datum bounds on entering support, and each joined-datum
holonomy is related to a global tested holonomy, a lifted-collar identity,
or a tested top holonomy. At Y 134198–134216 the endpoint estimate is applied
to a prospective datum and Y says to take the profile “from the actual
retained tests at each entrance” when carrying estimates through stages.

| Item | Y lines | Status |
|---|---:|---|
| Departure / least-level departure / standing departure | 65425–65426, 65467–65469 | USED WITHOUT DEFINITION |
| Stopped component / untouched component | 65425–65428 | USED WITHOUT DEFINITION |
| Island / drop-out | 1176–1178, 63874–63876 | DEFINED by outcome rules |
| Restored core | 65431–65433 | USED WITHOUT DEFINITION |
| Waiting window | 1182–1183, 1193–1202 | DEFINED BY REFERENCE (`eq:rg-objects-R21`) |
| Inset of stage-test region | 65426–65428, 76664–76669 | USED WITHOUT DEFINITION |
| Action top | 65429–65430, 1199–1202 | DEFINED BY REFERENCE (`eq:rg-objects-R21`); “action top” itself remains descriptive |
| Determining sequence / action sequence | 1193–1202 (`eq:rg-objects-R21`) | DEFINED |
| Prepared face / seam | 63876, 77609–77620, 78316–78320 | USED WITHOUT DEFINITION |
| Collar departure | 65436–65448, 76661–76672 | USED WITHOUT DEFINITION |
| \(\psi_l\) | 65477–65478 | STATED with casewise bounds; no definition found |
| (L_\flat^2<L) | 63864–63876, 65481 | STATED as a derived comparison in the COV estimate; not an independent standing condition |
| Anchored per-test estimate at an entering point | `hi:prepared-real-endpoint`, 65409; assignment and bound 65417–65485 | STATED in prose under the anchor, not a numbered theorem |
| Fixed-prospective global levelwise estimate | 65536–65560 | PROVED IN Y (Y gives the calculation) |
| Uses / transport of the entering-point estimate | 65019–65067, 134198–134216 | STATED |
| Ordinary stage and stage-test removal | 63836–63876, 77741–77763 | STATED |
| Main integration / free Haar integral | 63847–63872 | STATED |
| Late Haar refresh | 65470–65474, 76677–76681 | STATED |
| Restoration by reference law | 1174, 63862–63872, 65472–65474, 76681–76689 | STATED |
| Drop-out and healing outcomes | 1176–1178, 63874–63876, 1202–1204 | STATED |
| Core operation and last-shell test | 63858–63872 | STATED |
| Test-to-place assignment cases in section 3 | 65425–65474, 76654–76689, 77810–77828, 78299–78331 | STATED in prose under `hi:prepared-real-endpoint`; no numbered COV statement |
| Literal footprint and seam qualifications in section 4 | 64063–64595, 65042–65045, 75824–75841, 77557–77656, 77810–77828, 78316–78386 | STATED |
