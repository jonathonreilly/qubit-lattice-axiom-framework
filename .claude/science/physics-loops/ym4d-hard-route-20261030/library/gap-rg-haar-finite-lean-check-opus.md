# Check 1437 of row 1435: finite Haar Lean file (Opus 5.5)

Checker: Claude Opus 5.5 (this session). No Lean run here. The lead re-runs Lean elsewhere.

## Plan

1. Read the report `library/gap-rg-haar-finite-lean-astra62.md` in full.
2. Read `lean/haar/RECEIPT.md` head and pointed parts; tally axioms by script.
3. Read rows 1425, 1432, 1433 sections cited.
4. Split `lean/haar/Haar.lean` by `-- replay` markers with a script; list headers; read all non-literal code.
5. Items 1-7 of the brief. Independent exact sphere-moment computation.
6. Verdict.

## Findings

(appended as the check proceeds)

### F0. Source identity and layout

- `Haar.lean` SHA-256 is `83522c06...585af581`. It matches the receipt.
- The file starts `import Init`. It splits into 429 modules at `-- replay` lines. `HBase` (2,774 lines) holds all core definitions, the recoupling window, the sphere fixture and the local table. The `AM*`, `HCt*` and `AMDB` modules are mostly packed literals.
- Scripts and module copies are in the scratch folder `check1437/` (split.py, heads.py, mods/, trunc/).

### F1. Recoupling (HBase 46-203, 593-822)

- `triangle`, `deltaSq` and `Vertex.racah` are the standard Racah formula for the tetrahedron with triangles (a,t,r),(b,s,r),(b,t,u),(a,s,u). The three y's are sums over the three opposite-edge pairs (a,b),(t,s),(r,u). Correct.
- `Vertex.angular` gives (C_s+C_t-C_r-C_u)/2. I derived this from J_a·J_b = (C_s-C_a-C_b-C_t)/2 - J_a·J_t - J_b·J_t. Correct.
- `Vertex.mark` inserts two complete bases (left z, right w) in X². It adds (X/2 - C_aC_b/3)·O. Divided by sqrt(D_r E_u) this is K = X²+X/2-C_aC_b/3. Correct.
- Second calculation: `embed` builds (x1y2-y1x2)^p times the highest monomials and applies k lowerings y∂x. `pathEntry` couples the outer spin first. `Vertex.inner` uses the invariant weights k!(n-k)!. `Vertex.fourX` is 4J_a·J_b with J+ = x∂y, J- = y∂x, Jz = (n-2i)/2. I checked each coefficient. `pathAgrees` compares sign and squared magnitude against `racah` (or `mark`, with 48K = 3(4X)²+6(4X)-a(a+2)b(b+2)). This path shares only `fac`, `binom`, `triangle`, `spins` and `deltaSq` with the Racah side. It is a genuinely different derivation of the overlap.
- The phase (a+2t+3b+r-u)/2 is therefore fixed by the polynomial convention, not asserted. `rejects_wrong_6j_phase` shows the check is not trivially true.
- Window: a,b ≤ 6, t,s,r,u ≤ 7, sum ≤ 22. K is tested only when a,b ≥ 2. The marked vertex has both caps ≥ 2 (root floor), so this covers it.

### F2. Enumeration primitives and the positive count (HBase 233-290, 1036-1168; HCountCore2; HCountM46; HCountDigits)

- The 32 distinct triangles are (a_j, m_{i,j-1}, m_ij) and (b_i, m_{i-1,j}, m_ij). `atVertex` puts each one at two vertices. This matches row 1425's statement.
- `columns`, `cuts`, `pool`, `usable`, `lowerCost` and `liveCaps` define the bounded generator. The signed vacuum transfer (V28), the positive count and the census records all call them.
- The positive count (`CountCap`, `countPolyRow`, `countCommon`) uses no recoupling weight, no packed local table, no orbit code and no target. Its packed `rows` must equal `moveCodes` recomputed in the kernel. Its caps must equal `liveCaps true 46`. So it is independent of the signed records. It is NOT independent of the generator definitions: it counts the same bounded set. A bug in `columns` or `usable` would hit both sides. That is why written argument (a) carries weight. See F6 for my independent count.
- No carry: `degree_counts` checks `total.upper < digitBase-1` in the kernel. `upper` adds ways·rootWays, which is the product's value at 1, and each recorded upper may only exceed the computed one. The step "digit sum < B, so each digit is the count" is a one-line written argument. It is correct. Truncation mod B^(d+1) applied to partial sums is also safe when no carry occurs.
- `HCountDigits` restates the digits 11, 62, ..., 1,899,868 for faces 20-46. They match the report table.

### F3. Marked census records (HArcCore, HOrder, AMDB, AMAC*, AMDBOK, AM*Header/P/Leaf/Join/End, HFinal)

- `verifyArc` decodes (a,b,p,q,root) from the slice signature. It checks all four triangles and the window at each of the slice's four vertices, the floors a_0,b ≥ 2 on the rooted slice, the cost, the key and the weight. The weight is recomputed as `scaledSlice` (times `capDim a` on the root slice). `AMDBOK.checked` is a `CheckedSlices`, so every one of the 56,991 slices passed `verifyArc`. The Span type forces all 891 chunks.
- `recordedTerm` requires the four retrieved signatures to equal (a, b_i, m_{i-1}, m_i) for the cuts w→x (rooted), x→y, y→z, z→w, and the four costs to sum to d. So every admitted record is a labelled assignment that satisfies all 32 triangle conditions twice, both floors and the exact degree. The inclusion half of written argument (b) IS kernel-checked.
- `scaledCell` reads only cells that satisfy `validLocal`. Those cells are exactly the `pathSlice` window entries that `local_table_and_symmetries` checks against `localWeight` (the rational Racah formula). So no unchecked table cell can enter a weight.
- Disjointness: `GridPage.ordered` gives strictly increasing grid codes in a page. `gridResult` demands canonical codes (code ≤ every image), nonempty cap lists and strictly increasing cap tuples. `disjointGridPages` (shells 20-42) or `OrderedPages` (44, 46) orders the pages. `OrderedPages.join` checks left < right at each boundary. All of this is in each shell's `Claim`, so it is kernel-checked.
- Each record contributes `size = |gridOrbit code|` to the count and multiplies its weight by `size`. The fibre argument (one fixed g per image gives a bijection of cap fibres) is correct, also with stabilisers. It is a written argument. Its inputs (`mixed_digit_actions`, `rooted_orbit_multiplicities`, `graph_incidence`, `local_table_and_symmetries`) are kernel-checked.
- Each `AMnn.Claim` states: ordering, `good`, count = CM46 digit at nn, count literal, bins length, target length, divisibility, number of target zero rows, and exact equality of the sorted computed scores with `declaredSorted target` on denominator 10080^16. `spin_histogram_complete` joins all 14 claims with the positive census, the sums 3,748,591 / 1,897 / 13, both vacuum calculations and the equality of the two vacuum target copies.
- Vacuum completeness has no independent count. V28 and OV28 both reach 30,034 and the same 96 rows. V28 uses the bounded generator; OV28 uses a proposed canonical-array list with regenerated cap intervals. Their agreement is a cross-check, not a completeness proof. The report does not claim more for the vacuum. See F6 for my count.

### F4. Independent count (my code, `check1437/bf.c`)

- I wrote a C depth-first enumerator from the definition only: 24 nonnegative labels, the 32 triangle conditions, floors a_0,b_0 ≥ r, degree = label sum. Its only pruning is two inequalities I derived myself: each mixed row sum ≥ max(max_j a_j, ⌈A/2⌉), each column sum ≥ max(max_i b_i, ⌈B/2⌉) (from a_j ≤ m_{i,j-1}+m_ij). It uses no `columns`, `cuts`, `usable` or reserve logic.
- Marked (r=2) counts at faces 20-46: 11, 62, 178, 466, 1329, 3522, 8733, 21080, 48152, 105962, 227239, 472658, 959331, 1899868; total 3,748,591. These equal the kernel digits exactly. Vacuum (r=0) through 28: 30,034. Run time 1.4 s.
- So written argument (a) holds numerically at every checked shell: the bounded generator with `usable` has the same size as the unrestricted triangle set. With the kernel-checked inclusion (F3) and disjointness, argument (b) is the pigeonhole step for an injective map into a finite set of equal size. It is correct.
- Row 1425 vertex labels (r=m_{i-1,j-1}, s=m_{i,j-1}, t=m_{i-1,j}, u=m_ij, a=a_j, b=b_i) match `atVertex`. Row 1425's O_ru phase (a+2t+3b+r-u)/2 with sqrt((r+1)(u+1)) and 6j {a t r; b s u} matches `racah`/`leftSq`/`rightSq`. The polynomial construction is the Condon-Shortley convention (positive top coefficient; J- = y∂x has positive matrix elements).
- K: row 1425 gives K = J_a·J_b(J_a·J_b+1/2) - C_aC_b/3, the same as X²+X/2-C_aC_b/3. `Vertex.mark` and the 48K polynomial both implement it.
- Unpruned runs (`bfnp.c`, no inequality at all, only sum ≤ D) agree through marked face 34 (total 35,381) and the full vacuum through 28 (30,034). So my pruning drops nothing in that range.

### F5. Sphere moments (HBase 338-587, 1611-2770; HNeg)

- Monomial formula: my `pizzetti.py` evaluates Δ^h x^α / (2^h h! · 4·6···(2h+2)) with its own polynomial Laplacian. It agrees with ∏(2k_i-1)!!/[2^h (h+1)!] on all 1,680 exponent tuples of total degree ≤ 12. Spot values: E[x_0²]=1/4, E[x_0⁴]=1/8, E[x_0²x_1²]=1/24.
- `traceRule` does not call `sphereMono`. It uses the pair recursion with divisor n_e+2 and the gluing weights 1, -2, 4 of `quaternion_trace_pairing`. `coordinate_pair_recurrence` ties the recursion to the formula for every exponent tuple of total ≤ 4; `sphere_coordinate_range` shows every bond occurs at most four times. `certifyTrace` forces each node's children to equal `traceRule` of its actual words, so the 872 certificate nodes cannot be invented.
- Insertion: I derived Re(HKH⁻¹K⁻¹) = 1-2|h×k|² and then Q(h)·Q(k) = [3Re(HKH⁻¹K⁻¹) + 1 - 4h_0² - 4k_0² + 4h_0²k_0²]/6. This is the five-term insertion with weights 3,1,-4,-4,4 on 6.
- Independent evaluation (`fixture.py`, `runfix.py`, `treecheck.py`): my own lattice (x(i,j), y(i,j), plaquettes, circuits), Q(h)·Q(k) computed directly from vector components (not from the commutator identity), exact link moments from the checked monomial formula, maximal-tree gauge fixing, sparse exact tensor contraction. My enumerator (`bfp.c`) produced the same eleven supports, in the report's order. Values per support: torus 5/77309411328; even 5/1320903770112 (×4); mixed -5/195689447424 (×4); odd 5/86973087744 (×2). Total 15655/169075682574336. A second maximal tree gives identical values. Sanity: E[Re(U_p)²]=1/4, E[Re(U_p)⁴]=1/8.
- So `haar_sphere_moment_fixture` states the right numbers. Its identification with the Haar integral is open in the report, but my different method reaches the same values.

### F6. Targets and vacuity

- My own parser (`cmptargets.py`, not the receipt's `compare.py`) compares all 17 `def target` blocks and `markedLeading` with the row-1432 `Ring.lean` (SHA-256 `46c69bc4...`, as in the receipt). Every block equals the Ring rows of its face degree as a multiset. Keys are unique and sorted by the base-25 key. The marked union is 1,897 rows with 13 zeros; the vacuum has 96 rows and no zero. The 13 zero keys match the report's table.
- This equality is a script check (theirs and mine). No theorem states it; the kernel compares with the copies in `Haar.lean`.
- The computed side never reads a target. Shell bins come from `recordedTerm` (V28: `cutProduct`, OV28/OM32: `mixedFibre`). Packed `ScoreBanks` totals are proposals that `sameTotals` checks against recomputation.
- No vacuous checker found. Every comparison is exact list equality with equal lengths, stated row counts and stated assignment counts. `Span` types force full index ranges. `Fr.same` rejects zero denominators. `orbitCover`, `sphereCovers` and `bagEq` check both directions. `cosetTest` returns true for non-subgroups, which is intended. The two `#guard_msgs` examples and the positive rejection theorems show the phase and orbit checks can fail.

### F7. Axioms and keywords

- Scan of the whole file: 0 `sorry`, `native_decide`, `implemented_by`, `ofReduceBool`, `axiom` declarations, `unsafe`, `opaque`, attributes, `instance`, `macro`, `elab`, `syntax`, `partial`, `#eval`. The one `extern` hit is the word "external" in a comment. Only four `set_option` kinds occur (maxRecDepth, maxHeartbeats, Elab.async, maxErrors). Only `import Init`.
- 1,712 theorems and 1,712 `#print axioms`. The receipt's verbatim output tallies 1,213 [propext, Classical.choice, Quot.sound], 430 [propext], 69 none = 1,712. No other axiom appears. The named theorems match the report (recoupling none; sphere fixture propext; census and word identities all three). I did not re-run Lean; these are the producer's outputs.

### F8. Statements against the report (item 1)

- Census: `spin_histogram_complete` states the positive census digits, all 14 shell claims, the totals 3,748,591 / 1,897 / 13, V28 cap coverage, count 30,034, 96 rows, OV28's claim, and equality of the two vacuum target copies. This matches the report.
- Recoupling: `marked_recoupling_trace` (window a,b ≤ 6, t,s,r,u ≤ 7, sum ≤ 22) and `recoupling_window_cardinality` (1,846 / 1,242). Matches.
- Sphere: `haar_sphere_moment_fixture`. Matches.
- Fixtures: `rejects_wrong_6j_phase`, `rejects_missing_orbit` and the two `#guard_msgs` examples. Matches.
- Report claims no theorem states: equality of the copies with Ring.lean (script); written arguments (a), (b), the fibre bijection and the no-carry step; "1,689 flagged tuples" inside the window (not checked by me, and not needed since `validLocal` gates every used cell); "56,991 distinct" (only the size is used). `OM32.orbit_histogram` is a separate theorem and is not joined into `spin_histogram_complete`; the report does not say it is.
- Wording: "independent positive transfer" is accurate for weights, orbits and targets, but the count shares `columns`, `cuts`, `usable` and `liveCaps` with V28. Argument (a) is therefore load-bearing. It is now confirmed by F4. Suggest one sentence saying so.
- The delivered file has not been compiled as one process (guard at 2 GiB). Only the 429-module replay passed, per the receipt. The lead's re-run decides this.

### F9. Repo hygiene (item 7)

- The file is 33.7 MB; gzip -9 gives 7.1 MB and xz -9 4.3 MB. Most of it is untrusted certificate data. The kernel re-checks all of it, so a regenerated file with the same SHA-256 is as good as the stored one.
- The generator is not in the lane; it lived in the producer's `/private/tmp` scratch folder. As committed, the 33.7 MB file is the only way to reproduce the proof.
- Recommendation: commit the generator (small) and the expected SHA-256 with the receipt. Keep the generated `Haar.lean` out of git history (Mini SSD archive or a release asset), or at most commit it compressed. If it must stay, keep it in one commit and never rewrite it, so history grows once.

## Verdict

HOLDS. The kernel-checked statements say what the report claims. Written argument (a) is confirmed by my independent count at every shell (marked 20-46, vacuum ≤ 28). Argument (b)'s inclusion and disjointness are kernel-checked, and its pigeonhole step is correct. The Racah sum, phase and K insertion match row 1425, and the polynomial check is a separate derivation. My separate tensor contraction reproduces all eleven sphere values and 15655/169075682574336. Non-blocking wording note: say that the positive count shares the bounded generator with the vacuum transfer.

Not checked: I did not run Lean, so every "kernel-checked" statement above assumes the lead's re-run passes. I did not check the packed literal data beyond what the code forces, nor the 1,689-tuple claim, nor the integral identifications and analytic plan (open by the report's own account). The receipt's axiom output and resource numbers are the producer's.

Scratch files: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/check1437/` (bf.c, bfnp.c, bfp.c, pizzetti.py, fixture.py, runfix.py, treecheck.py, cmptargets.py, fixture.log, supports20.txt, mods/, trunc/).
