# Hostile review of LIB1

Review date: 2026-10-29. User-assigned independent Codex reviewer in a fresh
context, with no authorship of the submitted unit. This is one review pass,
not an audit or a claim of cross-family confirmation. The review follows
`briefs_lib1/REVIEW_BRIEF_LIB1.md`; only this report is written.

**HOLD for one reproducible checker defect, B1 below.** The stated finite-graph
lemma, including its counting and conditional norm clauses, survives the
mathematical review. The submitted full-norm mutation control does not test
the full-norm computation: substituting the active norm passes every predicate
and still reports that substitution as rejected. This is an evidence defect,
not a counterexample to the written theorem. The missing unrestricted-history
and sea-integration estimates are already disclosed residue, not new findings.

Frozen candidate HEAD is `4f04b662f4d72d7ef269f6d9693ae9ff6424acf9`;
freshly fetched `origin/main` is `ca2bc7ddf64790da96cd43d42017d000fbfe4808`.
The applicable repository procedures match that main revision. Planning was
read without checkout and supplies no mathematical authority. The specific
review brief overrides general integration, fix, and landing procedures.

| Reviewed artifact | SHA-256 |
|---|---|
| `LIB1.md`, 40,718 bytes, lines 1–721 | `cc1252b360b00e0463452febefba22313a1329cfee17515f012d3f4aa9bc8c76` |
| `LIB1_LOG.md`, lines 1–172 | `b31bbbc52780fddf1779cb95d5a6f7e2405b5981d01dc1870e52bf564cfd7bc7` |
| `checks/lib1_check.py`, lines 1–299 | `63256a04b6d2fc46dad13ee26ae0b0c592e93ac7d271157076ef32d23650fdbc` |
| `checks/lib1_criteria.md`, lines 1–49 | `2401a70f2e9b87af8a876eb4a5274b7467bf5769f7f1d30bddbcd4b1356d1f68` |

All `checks/lib1_*` artifacts were inspected. Both recorded result copies
match; stderr is empty. All 25 source-manifest entries and all recorded
artifact hashes match the files reviewed. The ten quoted consumer/producer
passages match their source text with whitespace normalization only.

**1. Provenance — PASS. Fix: none.**

`LIB1.md:1–147` is the original 8,489-byte prefix, with SHA-256
`1f7367c972e1ad49e81cfccdab1bec07b2259a44616fc45bab28e89174941c3d`.
It contains the target selection, candidate comparisons, statements, proposed
specialization, scope test, and success criteria. It contains no proof or
result from the new finite checks. The first-result heading begins at line
149. The prior-work assessments at lines 20–36 are selection reasons, not
post-test results for LIB1.

The receipt at `LIB1_LOG.md:5–26` is corroborated by the original tool events,
not accepted solely on the author's assertion. In
`/Users/jonBridger/.codex/sessions/2026/10/29/rollout-2026-10-29T15-24-26-01a1891e-e51d-7bf1-bb4c-73157fc88441.jsonl`:

- Line 137 records the first `Add File: .../LIB1.md` at
  `19:30:50.605Z`. Decoding its patch reconstructs exactly the current
  8,489-byte prefix and its hash.
- Line 140 records the stat/hash command and receipt at
  `19:30:50.707400Z`, before the later additions to LIB1 at transcript lines
  200 and 218 (`19:39:41.835Z` and `19:43:51.551Z`).
- Line 173 creates the current check criteria at `19:34:24.972Z`; line 181
  creates the current checker at `19:36:00.445Z`. The first recorded check
  starts at `19:36:00.548330Z`.

Only tool-operation provenance was used from that transcript; the proof was
reviewed from the submitted source. The prefix, criteria-first ordering, and
reported initial stat are substantiated. Source reading and exploratory
reasoning before the first edit are expressly disclosed at `LIB1.md:3–6`.

**2. Target choice — PASS at the stated library scope. Fix: none.**

| Author-brief criterion | Verdict and source evidence |
|---|---|
| (a) Current soft route, preferably both routes | PASS. `SOFTHARD.md:5,29,349–351` keeps Decision 4 and identifies the resummation ingredient as shared. `SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md:27–37,111–120` supplies the actual fixed soft-kernel/source convention. LIB1 does not take an infinite-stiffness limit or replace the measure. Its hard-route usefulness remains ARGUED at `LIB1.md:580–585`. |
| (b) Named open consumer | PASS for narrowing. `HANDOFF.md:417–428` explicitly leaves holes/reference bookkeeping and the normalized source-local return open. `CODEX_REVIEW_ASSEMBLY.md:229,231` leaves coupled reconstruction and source norm/radius matching open. `STEP55.md:583–584` leaves the boundary-polymer integration and failed returns open. LIB1 supplies a reindexing/locality/norm sublemma and does not claim to complete these consumers. |
| (c) Complete open proof strategy | PASS. Dimock III, Appendix B, p.35, (238)–(245), gives the regrouping strategy; Dimock II, Appendix E, pp.88–91, supplies the disconnected-set and punctured-family counting strategy. LIB1 rebuilds the needed graph count instead of importing E.3. The different metric and constants are explicit. |
| (d) Not already proved in this folder | PASS for the required bounded search. I independently searched the folder and read the closest hits. None states arbitrary nested inactive-component saturation with these active/full norm comparisons. This is not an absence claim about every branch or all literature. |

The independent folder search included:

```sh
rg -n -i 'resumm|inactive region|punctured.distance|boundary.polymer|enlarg.{0,60}(holes|regions)|saturat.{0,60}(region|component)' --glob '*.md' --glob '!LIB1*' --glob '!checks/lib1_*' .
```

The relevant prior arguments are `SF.md:423–438,758–780,1242–1289`
(bounded collars, connectors, and collar regrouping),
`RECOVERY_CLUSTER_ASTRA.md:92–111,231–305` (full rooted norms and a connected
logarithm), and `SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md:622–650` (fixed-boundary
cancellation). The latter still retains the boundary variables and unproved
integration. These overlap the method but do not duplicate the new theorem.
The corrected assembly order at `CODEX_REVIEW_ASSEMBLY.md:215–235` was checked
against `ASSEMBLY55.md:551–609` and `APPROACH_REGISTRY.md:20–23,54–58`;
historical status summaries were not treated as proofs.

The source PDFs actually inspected were `checks/sh_dimock_III.pdf` (p.1 and
p.35), `checks/sh_dimock_II.pdf` (p.1 and pp.88–91), and
`/Users/jonBridger/ym4d-lanes/arxiv/review_residual_full_colour_literature_dimock_multiscale.pdf`
(p.1 for the candidate-comparison scope). The two saved equation-page renders
were visually checked. The official records confirm Dimock's scalar d=3
scope for [Part III](https://arxiv.org/abs/1304.0705v1) and
[Part II](https://arxiv.org/abs/1212.5562v2), and the abelian d=3 scope of
[Multiscale block averaging for QED](https://arxiv.org/abs/1712.10029v3).
No scalar or abelian estimate is used as a four-dimensional SU(N) theorem.
The other PDFs in ARXIV_DIR were hash-checked as manifest entries; they are
not proof inputs to LIB1 and no reading of their arguments is claimed.

**3. Proof — PASS as an explicitly quantified implication. Fix: none.**

I checked the complete argument, rather than inferring validity from its
finite tests. Its dependency chain is geometry → counting → decay, with a
separate direct norm estimate; it is not circular.

| Statement and lines | Independent reconstruction and disposition |
|---|---|
| Domain, `LIB1.md:45–79,164–214` | The face graph has degree at most 8, including periodic identifications. The tree length uses ambient graph edges, not zero-cost holes or SF's continuum touching length. Supports carry every original source/field argument. Masks and F are fixed combinatorial parameters when data vary. PASS. |
| Part A, `216–273` | Every added inactive component meets or is adjacent to the connected X; distinct inactive components cannot be adjacent. Their union is connected and saturated, and adds no vertex of Λ. Therefore `Y∩Λ=X∩Λ⊆X∩Ω`. Any ambient tree covering the latter covers the former. Fibres partition precisely the supports meeting Λ. The complementary sum stays in the exponent. Finite sums preserve original-variable locality and source holomorphy. PASS. |
| Counting, `275–331` | A minimum tree has n+1 vertices, so `card(S)≤n+1`. The deterministic traversal plus marked vertices recovers S. Every included hole has an edge to S, giving at most `8 card(S)` candidate components and `2^(8 card(S))` choices. Thus the displayed `512·32768^n` majorant and its geometric sum are valid uniformly in hole sizes and graph volume. PASS. |
| Part B, `333–355` | Every input in a nonempty fibre contains every vertex of `Y∩Λ`; choose one common root. Split the input exponent into rates a and `κ_B−a`, use monotonicity only on the latter, and apply the rooted count to the former. This proves the stated constant and decay loss without a factor `card(Y∩Λ)`. Empty fibres cause no exception. PASS. |
| Active norm, `357–375` | At a retained root, membership and active support size pull back exactly to X. Triangle inequality followed by `card(X∩Λ)≤card(X∩Ω)≤card(X)` proves contraction for `μ≥0`. No new entropy factor is needed. This is not a full-norm contraction. PASS. |
| Conditional full norm, `377–412` | At most `8 card(X)` inactive components can enlarge X, so `card(Y)≤(1+8M)card(X)`. For an inactive root in H, any preimage X must meet the closed neighbourhood of H, containing at most `9M` vertices. Sum over those possible input roots. This gives exactly the stronger rate and the factor `9M`; retaining the separate inactive family costs the stated additional 1. PASS, conditional on the explicit M hypothesis. |
| Source differences/derivatives, `414–438` | The map is fixed and linear; subtraction commutes with it and costs at most two in the supremum. Cauchy's integral formula on inner polydiscs gives the multi-index factorial and radius gap shown in L16. Derivatives outside Y vanish. No analyticity in a hard-selected coarse field is inferred. PASS. |
| H24 specialization, `440–526` | This is expressly an implication from a supplied H24 bound. Setting Ω=Γ admits the producer's face-connected supports. The original coefficient labels, real-field supremum, and fixed K remain the same. L20 reproduces H21's dependence on the stronger input rate; L21 does not silently retain the old smallness budget. H25 is preserved only if supplied. PASS at this conditional scope. |
| Scope example, `528–557` | The punctured four-dimensional torus is connected by the explicit path construction. Saturating the single supported source activity gives support Γ. The full norm is `b exp(μ card(Γ))` and the active norm remains `b exp(μ)`. This tests the chosen support label; it does not refute alternative returns or assert that this activity is an actual Yang–Mills coefficient. PASS. |

As a second counting derivation, encode a rooted ordered minimum tree by a
balanced-parenthesis word of length 2n (at most `4^n` possibilities) and the
chosen neighbour for each of its n forward edges (at most `8^n`). Mark S in
its n+1 vertices and choose the adjacent holes. This independently bounds
the count by

```text
4^n · 8^n · 2^(n+1) · 2^(8(n+1)) = 512 · 16384^n
                                      ≤ 512 · 32768^n.
```

Thus the author's deliberately loose constant is not inferred from small
samples. At `a=16 log 2`, the author's series has ratio 1/2 and equals 1024.
Singleton and empty active sets, no holes, disconnected active sets, μ=0,
and fixed masks all fit the stated clauses. The full norm conversion does
not extend to arbitrary hole sizes at a fixed rate. There is no load-bearing
`[m]` assertion or specialized literature theorem left hidden in these proofs.

**4. Statement match — PASS for the advertised implications and narrowing;
the complete consumers remain OPEN. Fix: none at that scope.**

The only claimed quantitative application takes the following source bound
literally from `SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md:592–593`, reproduced
at `LIB1.md:450–453`:

```text
sup_x sum_(X contains x) exp(mu|X|)
     sup_(real U,V; D_(rho,lambda)(u)) |V_X^F| <= d_q.
```

The source domain at producer lines 438–442 and LIB1 lines 455–459 is the
same `D_(rho,lambda)(u)={epsilon: |epsilon_p|<=rho+lambda/u}`. The locality
and fixed-kernel quotations at LIB1 lines 461–466 match producer lines
576–581 and 456–459. The producer's admissible source/coupling conditions
are part of supplying H24; LIB1 does not prove H24 for arbitrary parameters.
Its conditional use does not promote the candidate producer to an
independently established theorem.

| Consumer row in `LIB1.md:565–572` | Exact matching boundary |
|---|---|
| SOFTHARD R10, line 567 | The quoted reindexing/decay task is met on the explicitly defined graph distance. The stronger claim that this is the same distance as a different continuum or punctured-domain consumer is not made. |
| HANDOFF step 2, line 568 | Holes and the inactive reference term are retained algebraically. Reference integration, failure prices, and the returned denominator remain OPEN, as the row says. |
| HANDOFF step 4, line 569 | Fixed-mask source locality and its domain are preserved. The complete normalized all-coarse-field, all-level N1 representation and N2 are not supplied. |
| Assembly item 11, line 570 | This is one reconstruction ingredient, not a flow estimate or completed coupled induction. |
| Assembly item 13, line 571 | L18 has the active norm. L21 has a full norm only with uniform bounded holes, the stronger H24 rate, and its increased budget. An unrestricted full-norm consumer cannot consume L18 as H24. This mismatch is explicitly left OPEN at lines 498–515 and 708–716. |
| STEP55 reference comparison, line 572 | All cone/sea arguments survive the regrouping. Nothing performs the missing COL-compatible integration. |

These rows contain real, open requests; they do not claim to discharge their
entire contracts. The distinction is essential to accepting the theorem's
scope. `LIB1.md:151–162,199–206,352–355,519–526,706–717` already preserves it.
No additional physical premise, reconstruction theorem, or continuum mass
gap follows from this review.

**5. Checks — original replay PASS; mutation coverage HOLD (B1).**

The original runner and documentation validator were rerun successfully.
To obey the one-file write restriction, the two final `Path.write_text`
calls were intercepted in memory, with any unexpected write rejected. The
runner source, mathematical predicates, resource guards, and validator
inputs were otherwise unchanged. No saved author receipt was overwritten.
Python ran with `-B`, `nice -n 10`, and all five recorded thread variables
equal to 1; the observed process niceness was 20. No pool was used.

The original replay started at `2026-10-29T19:52:19.865534+00:00`, exited 0,
and reproduced every recorded predicate count: 2,187 coefficient identities,
36,873 small-graph support instances, 576 entropy comparisons, 8,972 decay
comparisons, 2,187 active-norm comparisons, 2,184 bounded-hole comparisons,
and 6,288 native four-dimensional support instances. Its 15 internal
resource samples showed maximum RSS 22,855,680 bytes, minimum free memory
62%, maximum load average 2.18505859375, and elapsed time 0.468111166 seconds.
The validator again checked all 25 source bindings, ten literal quotations,
the prefix, and unchanged recorded outputs.

I also ran independent set-based reachability and exhaustive edge-subset
tree minimization, with signed rational coefficients, on every connected
labelled simple graph with 1–4 vertices: 44 graphs, 3,198 nested-region
pairs, 17,981 support checks, 3,198 norm comparisons, and 3,191 entropy
slices. All assertions passed. This reused only the author's resource
monitor, not its graph, saturation, tree-length, grouping, or norm routines.
It additionally checked the connected complement and exact single-activity
norms on `(Z/3Z)^4`: input full norm 2, output active norm 2, output full
norm `2^81 = 2417851639229258349412352`. Seven resource samples showed
maximum RSS 23,199,744 bytes, free memory 62%, maximum load 2.20556640625,
and elapsed time 0.350318917 seconds. These are finite diagnostics; the
general claims rest on the proof above.

**B1 — the active/full substitution survives the claimed control.**
Locations: `checks/lib1_criteria.md:40–45`,
`checks/lib1_check.py:199–203,245–267`, and the reported mutation coverage at
`LIB1.md:647–649` / `LIB1_LOG.md:142–146`.

I compiled four modified copies of the checker only in memory, retained all
resource gates, and invoked their `main()` functions:

| Mutation | Observed result |
|---|---|
| At line 188, replace `recombined = dict(inactive)` by `recombined = {}` | Rejected by `polynomial_identity_with_inactive_remainder`. |
| At line 186, replace the monomial key x by `x & lam` | Rejected by `polynomial_identity_with_inactive_remainder`. |
| At line 98, fill only intersected components (`if x & h`) | Rejected by `two_closure_algorithms`. |
| At line 202, replace `norm(grouped, out_labels, allv, allv, 1)` by `norm(grouped, out_labels, lam, lam, 1)` | **Survived every predicate, including all 2,184 purported full-norm comparisons; still reported `identify_active_and_full_norms: rejected by exact witness`.** |

The final mutant took 0.423582583 seconds; its 15 resource samples had
maximum RSS 22,528,000 bytes, free memory 62%, and maximum load
2.1650390625. The three rejected mutants each stopped in under 0.005 seconds.
All four used the same niceness/thread settings and no on-disk edits.

The defect has a precise cause. The inequality at line 203 becomes easier
after replacing its left side by the smaller active norm. The purported
control at line 259 compares two separate powers of two and never calls the
output-norm computation. The `norm_witness` numbers at lines 264–267 are
literal values, not assertions against that computation. Consequently the
control still says “rejected” while the tested output uses exactly the
forbidden norm. The constant comparison itself is true; it does not provide
the implementation-discrimination required by criteria lines 40–45.

This minimal reproducer preserves the submitted file and its resource checks
and demonstrates the surviving mutation without writing any artifact:

```sh
nice -n 10 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 -B - <<'PY'
from pathlib import Path
p = Path('checks/lib1_check.py').resolve()
s = p.read_text()
old = 'output_full = norm(grouped, out_labels, allv, allv, 1)'
new = 'output_full = norm(grouped, out_labels, lam, lam, 1)'
assert s.count(old) == 1
ns = {'__file__': str(p), '__name__': 'lib1_review_mutant'}
exec(compile(s.replace(old, new), str(p) + '::active-for-full', 'exec'), ns)
ns['main']()
print('SURVIVED', ns['REPORT']['mutations'])
PY
```

**Binding fix.** B1 is the single blocking finding. Connect the exact norm
witness to the same full-output computation used by the inequality check,
and assert its result against an independently derived full-support value.
For the existing four-cycle singleton example, the computed input full,
output full, and output active norms must be 2, 16, and 2. The active-for-full
substitution must then fail at the full-norm assertion. If root selection is
factored separately, include overlapping output supports whose largest
rooted sum occurs at an inactive vertex, so omission of inactive roots is
also detected. Run the corrected baseline and the actual mutant under the
existing resource gates, preserve their distinct outcomes, and update the
check/log claims to describe what was tested. Do not rewrite the immutable
PRE-STATED prefix or change the theorem to conceal the failed control.

No mathematical rewrite is requested. A different honest disposition would
explicitly withdraw the implementation-mutation coverage claim and identify
the unmet optional criterion; the current positive coverage claim cannot
stand unchanged. The original reviewer should confirm whichever narrow
repair is submitted before the unit receives LAND.

No source fix, commit, push, PR, audit operation, or consumer edit was made.
The branch's tracked diff remains empty. The author artifacts and the
2,196 pre-existing files inventoried in the working folder were unchanged
through the review; this report is the only deliverable. Repository-wide
integration validation was not run because the brief authorizes this scoped
review, not integration. The mathematical disposition is PROVEN at the
stated implication scope, with the named producer and analytic residues
retained. The submitted evidence package awaits B1's correction.

VERDICT: HOLD
