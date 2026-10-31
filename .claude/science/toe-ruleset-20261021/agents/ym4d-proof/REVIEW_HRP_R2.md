# Independent hostile review of HRP, round 2 — 29 October 2026

**Item 6: RESOLVED. Item 7: RESOLVED.** The recorded execution supplies the previously missing evidence, with both failed control criteria preserved as failures. The replacement consumer statements match their sources and retain the required qualifications. Items 1–5 stand as previously confirmed, including item 1's provenance qualification; this review does not claim to have repeated those proof reviews or grant banking/audit status.

This is a fresh review context, separate from authorship of HRP.md and REVIEW_HRP.md. I inspected the entire frozen Python runner and launcher, criteria, all six specified rerun records, all 30 saved Gram records, summary and geometry records, the complete replacement §9, and the relevant consumer statements and qualifications. I did **not** execute or import the runner, invoke its launcher, acquire its numeric lock, or bypass its priority guard. Read-only hashing, text comparison and stored-record consistency checks are inspection, not regeneration of the scientific computations. Only REVIEW_HRP_R2.md was written; no commit was made.

## Source identity and preservation

Local HEAD: `93a9d1a141849dfac1d8f1a585a17e43211ef271`. This review concerns the supplied local packet, not a refreshed remote source. The repository-local reviewer procedure and focused review contract were used within the owner's inspection-only scope.

| Source | SHA-256 inspected |
|---|---|
| HRP.md | `f1f991dea8062bfc7176a68cc639beacd848d4fb9cdd0bd4917198e39dac51b5` |
| REVIEW_HRP.md | `b02e4fad071318c6558699469eae78397986f325fde7c26848cfd45acea42fd6` |
| ASSEMBLY55.md | `253ea55619c7fd09d278add27b840c989a2a35160eb22a0385ea700f01fac9c7` |
| PANEL_P1.md | `feba5a1f2c0fc2c6ebc3373a5edfc3aec2ff0bb242550f4112b00e4d5a74a645` |
| CODEX_REVIEW_P4.md | `12d59c044e86af2fe66806332aed9a2e98181409e075151a983c4b4eeb7d1b34` |
| OSLEAF55.md | `7ba9423f52e7da40f5bf2a44dd4fb49d477405bb70cf5b41de3c0482bf2e0df0` |

HEAD's HRP.md has exactly the prior review's hash, `d85027730ac0c7d4c6102ede801be3f4f8cd3b89a34910675280cde15a5f11b7`. Current HRP before §9 is byte-identical to that version after removing only the added rerun pointer at line 739. The original §9 is also preserved exactly after removing its new Markdown quote markers. No previously reviewed mathematical argument changed.

The 38-file rerun evidence bundle comprises the 30 Gram files named by hrp_summary.json, hrp_sphere_geometry.json, hrp_summary.json, and the six records specified in this review request. Its manifest digest is `295c52386bc17a7e598c0bddac19db05a5fa0c344d31a4ca2c4a1fa26b07db84`: SHA-256 of the concatenation, in lexicographic relative-path order, of each file's lowercase SHA-256, two spaces, its `checks/...` path, and newline. Source/evidence identities were checked again before disposition; no concurrent change was found.

## Item 6 — executed exact-check evidence: RESOLVED

**Frozen source match.** Each recorded hash in checks/hrp_lead_rerun_hashes.txt matches the current file and the corresponding hash in REVIEW_HRP.md:15–17:

| File | Matching SHA-256 |
|---|---|
| checks/hrp_exact.py | `e951fb782c09534aac8a7c178b5963b731274fff83de6c34a5b7afe52415e2b6` |
| checks/hrp_run.sh | `893d362daf45eeb30c78a6cb1b658a4572d696b62f05ebad9813c7c72a86ba98` |
| checks/hrp_criteria.md | `3e00f5ec5bbc32522636004aa72628c45884fe3762573c047e1105593ea82173` |

The START record also contains the matching script and criteria hashes. No amended criterion or altered runner is being substituted.

**Execution receipts.** checks/hrp_preflight.txt records load 2.66 and free memory 46%, including the second memory check. The frozen launcher preserves the lock, single-thread environment and nice invocation; the runner asserts priority ≥10, the environment, the lock and the criteria hash before printing START (hrp_exact.py:518–528). The complete output reaches its summary/resource lines, stderr is empty, and hrp_time.txt records `numeric_exit=2 cleanup_exit=0`, with real time 1.41 s. The runner records 1.3683314999798313 s and peak RSS 25,903,104 bytes, within its limits. Its return at lines 560–561 makes exit 2 the disclosed-control-failure outcome. These receipts are consistent with the frozen execution path, not the earlier priority assertion failure. I did not witness or independently authenticate the lead's external process; the finding is based on the supplied, internally consistent records and unchanged source.

**Printed results versus source and saved evidence.** All 30 stdout Gram rows match the saved records and summary in order, name, dimension, normalization, PSD flag and Hermiticity flag. The matrices have the stated dimensions and symmetry; indicator-basis entries sum to their positive normalization. All 25 positive cases contain complete nonnegative rational Schur-pivot lists with consistent rank counts. Both saved Hermitian-part matrices are exactly `(M + M^T)/(2Z)`, with the doubled denominator, not a misnormalized substitute.

The source schedules exactly 25 positive outputs: 18 group/reflection/basic-sheet-zero cases, two direct Z2 cases, two fully coupled Z2 cases, and three prism cases (hrp_exact.py:531–549). Basis dimensions match the source: class pairs/triples, 32 tree-gauged slice indicators, and prism class indicators. Further checks against the actual construction are:

- At zero coupling the four transfer steps give normalization `|G|^12`: 4096, 531441 and 68719476736, as printed.
- Each saved direct Z2 matrix and its normalization are exactly 16 times their transfer counterparts, the four removed spatial tree-link factors. Thus the normalized matrices agree entry by entry.
- Each saved decoupled-sheet matrix equals its corresponding 2D matrix, as the source's cancellation requires. These are not fully coupled Z3/Q8 checks.
- The Q8 split-word count is `8^6 = 262144`. Geometry stdout matches its JSON for both radii, including crossing counts `(32,8,16)` and `(296,56,112)` for every coordinate reflection.
- Prism records use five free edges, giving 32, 243 and 32768 assignments; their six inherited coupling indices are `[5,6,6,5,6,6]`. Their declared scope remains the local six-face model, not the entire K_a partition sum.

The prior review already confirmed the exact arithmetic design. This inspection connects that frozen design to the now-present records; it does not claim a second exhaustive computation of every Gram sum or Schur recurrence.

**Controls checked against source, saved matrices and REVIEW_HRP's hand algebra (lines 110–116).** Put `K=[[34,16],[16,34]]` and `D=diag(34,16,16,34)`.

| Control | Independent algebra and recorded outcome | Original criterion |
|---|---|---|
| Negative crossing β | The saved numerator is `D(K_- ⊗ K)D`, with `K_-=[[16,34],[34,16]]`, and normalization 6145024. For `v=D^-1(1,1,-1,-1)`, `v^T M v=-3600`. The saved negative Schur pivot is −489600 after two positive pivots. Source and stdout therefore correctly detect a negative eigenvalue. | Satisfied |
| Asymmetric coupling | The saved numerator is `D(K ⊗ K)D_+`, `D_+=diag(130,40,40,130)`, with normalization 21774880. Entries 739840 and 1131520 in transposed positions prove non-Hermiticity. Diagonal similarity gives the positive definite matrix `sqrt(DD_+)(K ⊗ K)sqrt(DD_+)`, so the raw eigenvalues are positive, just as R1 derived. The saved Hermitian part is positive definite. | **FAILED**: no negative raw eigenvalue |
| Asymmetric cell | The saved normalized matrix is `diag(1,0,0,0)+(3/5)E_(3,2)` in one-based indices, with numerator entries 40 and 24 and denominator 40. Its raw spectrum is `1,0,0,0`; its Hermitian-part spectrum is `1,3/10,-3/10,0`. The saved Hermitian numerator has the negative minor −576, denominator 80, and `F=a-b` gives −3/5. These agree exactly with R1. | **FAILED**: the negative eigenvalue belongs to the Hermitian part |

The asymmetric-coupling Hermitian-part result also admits a separate small algebraic check: its numerator splits into positive scalar blocks 7,956,000 and 1,152,000, and the symmetric block `[[12482080,3742720],[3742720,1807360]]`. The latter has positive diagonal and determinant 8,551,659,110,400, proving positivity without reusing the Schur algorithm. R1's raw-spectrum conclusion alone would not establish this additional fact.

Both failures are explicitly identified in hrp_out.txt:40–43, the two-entry failure list in hrp_summary.json, and hrp_lead_rerun.md:19–23. The criteria at lines 25–31 require exactly this distinction. Neither non-Hermiticity nor a negative eigenvalue of a Hermitian part is relabelled as success of the raw-spectrum criterion. The asymmetric cell remains an intentionally malformed control, not a counterexample to K_a. Thus the binding execution-and-inspection fix is satisfied despite the two honestly reported criterion failures.

## Item 7 — exact consumer statements and qualifications: RESOLVED

I compared all ten quoted units in the [RHRP-7 fix] directly with the four consumer files. Every unit is an exact substring after removing Markdown quote prefixes; the additional ASSEMBLY55 N1F comparison needs only its original line wrapping joined. No words, punctuation, symbols or qualifications were normalized away.

| HRP.md location | Exact source matched |
|---|---|
| 751, first sentence | ASSEMBLY55.md:172–173, N3/N1F |
| 751, both sentences | PANEL_P1.md:57, including “Localization/renormalization errors are controlled in the same moment topology.” |
| 757 | ASSEMBLY55.md:173, “RP for great spheres through the base point S” |
| 763 | CODEX_REVIEW_P4.md:246, the two complete hypothesis sentences preceding its optional example |
| 765 | CODEX_REVIEW_P4.md:260, item 4's complete RP implication |
| 767 | CODEX_REVIEW_P4.md:263, the complete bounded/unbounded and moment/uniform-integrability qualification |
| 774–775 | OSLEAF55.md:312 and 318, H_RP-sep and CLOSURE-sep(d) |
| 785–790 | OSLEAF55.md:353–358, the complete U-sep, K-inv and RP-pole assumptions, including their OPEN/all-order qualifiers |

The surrounding text also preserves the binding scope. HRP:753 retains one common sequence, eventual exactness only for the stated zero-source local maps, and H_reg/(EXT)/ALG as supplied hypotheses. The N1S qualification at HRP:759 is byte-identical to REVIEW_HRP:130: four finite coordinate reflections, fixed-R continuum passage on the cap, separately supplied SO(4)_S state invariance, and radius-uniform convergence/continuity plus translations for the flat affine-plane conclusion. It does not claim the O(5)-invariant sphere states assumed by the quoted P4 consumer have been constructed.

For OSLEAF55, HRP:777–797 retains the common-sequence convergence and continuous extension needed by CLOSURE-sep(d), explicitly conditions affine-plane transport on H_Euc-sep, and retains fixed-R extraction and the restricted cap domain. This agrees with OSLEAF55:308–332, 349–369 and errata E2/E8 at 767–769 and 791–793. Ordinary polynomial moments and the restricted OS domain remain distinct; the latter is not silently substituted for literal N1F/N1S. The words “banked finite-cutoff RP” are accurately quoted consumer text and expressly confer no banking or retained status in this revision.

No remaining fix to item 6 or item 7 is required. H_reg/(EXT), algebra acceptance, state invariance, trajectory/diagonal construction, H_int, reconstruction, physical existence and a mass gap remain outside this disposition. Under the requested meaning of LAND, items 1–5 stand and both outstanding HOLD items are resolved.

VERDICT: LAND
