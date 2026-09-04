# Item 1 — the b141/b142 stale-pin chain: repair plan

**ANALYSIS ONLY. No commits, no pushes, no file edits were made.**
Paths relative to
`/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/gravity-toe-lane-work-427b0b/`.

## A. The defect, confirmed

An unanchored `sed` rewrote `STALE_PARENT_COMMIT` alongside `PARENT_COMMIT`,
leaving the two identical in both landed runners:

| runner | line | constant | current value | verdict |
|---|---|---|---|---|
| `scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py` (b141) | 139 | `PARENT_COMMIT` | `23ad6d38be6a39d1f4d1821961318a60fc9e10b2` | **CORRECT** — b140's tip, matches `PARENT_REF = origin/physics-loop/toe-axiom-closure-block140-isospectral-similarity-20260819` |
| same | **142** | `STALE_PARENT_COMMIT` | `23ad6d38be6a39d1f4d1821961318a60fc9e10b2` | **WRONG — identical to the live pin** |
| `scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py` (b142) | 163 | `PARENT_COMMIT` | `2d92a7252bb85ed4090e0fc76032f674e51c6236` | **CORRECT** — b141's tip, matches `PARENT_REF = …block141-coboundary-healing-family-20260819` |
| same | **166** | `STALE_PARENT_COMMIT` | `2d92a7252bb85ed4090e0fc76032f674e51c6236` | **WRONG — identical to the live pin** |

**The comments the sed did not touch name the intended values verbatim.**
b141 l.140–141: *"Block 139's tip: a real ancestor that predates the Block 140
artifacts and is therefore the honest 'stale pin' control."*
b142 l.164–165: *"Block 140's tip: a real ancestor that predates the Block 141
artifacts…"*. So the correct values are recoverable from the files themselves.

**Why it defangs the mutation.** Both runners share this gate wiring
(b141 l.899–903, b142 l.1204–1208):

```python
parent_blobs_ok = (
    authority.parent_artifact_blobs
    if claims["parent_pin"] == "resolved"
    else authority.stale_parent_artifact_blobs
)
```

and the `stale_parent_authority` mutation sets `claims["parent_pin"] = "stale"`
(b141 l.855, b142 l.1163). `stale_parent_artifact_blobs` is built at b141
l.315–317 / b142 l.373–375 as
`commit_blob(STALE_PARENT_COMMIT, path) for path in PARENT_ARTIFACTS` and
required to be all-hashes **and** equal to the worktree blobs. With
`STALE_PARENT_COMMIT == PARENT_COMMIT` that tuple is *identical* to
`parent_artifact_blobs`, so it is **True**, gate A **passes under the
mutation**, and the negative control proves nothing. Both runners have carried
this since their landing commit — `git log --all` shows exactly **one** commit
per file (`2d92a7252b` for b141, `503cf8dabd` for b142), so there is no earlier
good revision to restore; the sed ran inside the landing commit itself.

**Blast radius, bounded.** Across all 28 admissibility runners that carry both
constants, exactly these two have `PARENT_COMMIT == STALE_PARENT_COMMIT`. The
26 others are clean, including the immediate downstream b143 (`STALE=2d92a7252b`),
b144 (`STALE=2d92a7252b`) and b147 (`STALE=6195b68e4f`). The defect is exactly
what PR #6859 disclosed and no wider.

## B. The correct genuinely-stale values, verified

### b141 → `ccfdb57a46d22d3a60c82db8d31df1414835dd0c`
Block 139's tip: `ccfdb57a46 physics: complete the ledger at the third size and
find the isospectral mechanism`.

`PARENT_ARTIFACTS` (b141 l.102–110) and their existence at that commit:

| artifact | at `ccfdb57a46` |
|---|---|
| `docs/ADMISSIBILITY_DIRAC_KAHLER_ISOSPECTRAL_SIMILARITY_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-19.md` | **MISSING** ✔ |
| `scripts/admissibility_dirac_kahler_isospectral_similarity_theorem_2026_08_19.py` | **MISSING** ✔ |
| `logs/runner-cache/admissibility_dirac_kahler_isospectral_similarity_theorem_2026_08_19.txt` | **MISSING** ✔ |
| `docs/…TWISTED_SCOUTING_RECORD…_2026-08-19.md` (b137) | exists |
| `scripts/…twisted_scouting_record_2026_08_19.py` (b137) | exists |
| `docs/…CONNECTION_RESIDUAL_THEOREM…_2026-08-17.md` (b134) | exists |
| `scripts/…connection_residual_theorem_2026_08_17.py` (b134) | exists |

Verified with `git cat-file -e ccfdb57a46:<path>`. Three of the seven resolve
to no blob → `all(is_hash(...))` is False → `stale_parent_artifact_blobs` is
**False** → gate A **fails** under `stale_parent_authority`. Teeth restored.
It is also a **real ancestor** (b139 → b140 → b141), so `is_ancestor` reasoning
elsewhere in the file is unaffected.

### b142 → `23ad6d38be6a39d1f4d1821961318a60fc9e10b2`
Block 140's tip: `23ad6d38be physics: exhibit the similarity and collapse the
count family-wide` — the same value that is (correctly) b141's `PARENT_COMMIT`.

`PARENT_ARTIFACTS` (b142 l.128–134):

| artifact | at `23ad6d38be` |
|---|---|
| `docs/ADMISSIBILITY_DIRAC_KAHLER_COBOUNDARY_HEALING_FAMILY_BOUNDED_THEOREM_NOTE_2026-08-19.md` | **MISSING** ✔ |
| `scripts/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.py` | **MISSING** ✔ |
| `logs/runner-cache/admissibility_dirac_kahler_coboundary_healing_family_2026_08_19.txt` | **MISSING** ✔ |
| `docs/…CONNECTION_RESIDUAL_THEOREM…_2026-08-17.md` (b134) | exists |
| `scripts/…connection_residual_theorem_2026_08_17.py` (b134) | exists |

Three of five missing → same conclusion. This is also the value b143 and b144
already use as *their* stale pin, so it is the lane's own convention.

## C. The blob cascade — and it is NOT a two-line change

Every runner's gate A also asserts
`commit_blob(PARENT_COMMIT, path) == worktree_blob(path)` over its own
`PARENT_ARTIFACTS`. **Editing a runner changes its blob**, so every descendant
that content-binds that runner fails gate A on re-run until its `PARENT_COMMIT`
is advanced — and advancing it edits *that* runner, propagating forward.

Transitive closure from the two seeds (computed over all 29 runners that
declare `PARENT_ARTIFACTS`):

| wave | runners that must be re-pinned |
|---|---|
| 1 | `annealed_pairing_migration` (b147), `massless_seam_verdict` (b144), `staggered_hermitian_pairing` (b143) |
| 2 | `general_migration_theorem` (b148), `seam_dichotomy` (b145) |
| 3 | `m_block_measurement_theory` (b146), `shear_gauge_classification` (b149), `unique_completion_price` (b154)\* |
| 4 | `bare_character` (b153)\*, `discriminator_verdict` (b155)\*, `joint_lane_flip_enumeration` (b150) |
| 5 | `floor_boundary_theorem` (b151), `residue_transversality_gate` (b156)\* |
| 6 | `cutting_strata_completion` (b157)\*, `quotient_gate` (b158)\*, `sign_layer_comparison` (b152)\* |
| 7–16 | `link_curvature_scout` (b159)\*, `exchange_condition_contract` (b160)\*, `validation_battery` (b161)\*, `mass_survival_stratum` (b162)\*, `site_reflection_channel` (b163)\*, `zero_shear_region` (b164)\*, `scaling_probe` (b165)\*, `interpretation_discriminators` (b166)\*, `null_model_corner_theorem` (b167)\*, `shim_zero_diagonal` (b168)\* |

**Total: 26 downstream runners, 16 waves — the whole lane from b141 to b168.**
The 17 marked `*` additionally carry **hardcoded** `PARENT_ARTIFACT_BLOBS`
literals (e.g. `link_curvature_scout` l.194–197, whose own comment says *"the
landing supervisor refreshes these two lines by anchored sed against the Block
158 branch tip"* — the same unanchored-sed surface that caused this defect in
the first place), so each of those needs its literal blob hashes recomputed as
well, not just a commit hash swapped.

The immediate answer to "which b142 pins must be refreshed after the b141 fix":
**`PARENT_COMMIT` at b142 l.163** (to the new b141-fix commit), and the b141
branch tip that `PARENT_REF` resolves to must be advanced to that same commit,
because b142 l.383–384 asserts
`git_output("rev-parse", PARENT_REF) == PARENT_COMMIT`.

## D. Two executable options for a follow-up pass

### Option A — the full mechanical re-pin (correct, expensive)
Sequential, one commit per wave, on a branch off `main`:

1. Branch: `physics-loop/hygiene-stale-pin-repin-b141-b142-<date>`.
2. **b141**: edit line 142 only →
   `STALE_PARENT_COMMIT = "ccfdb57a46d22d3a60c82db8d31df1414835dd0c"`.
   Use an **anchored** replacement (`^STALE_PARENT_COMMIT = `), which is the
   whole point. Re-run the b141 runner; confirm gate A now **fails** under
   `--mutation stale_parent_authority` and **passes** clean. Commit. Call it `X1`.
3. Advance `origin/physics-loop/toe-axiom-closure-block141-…` to `X1` (b142's
   `PARENT_REF` check reads the branch, not the commit).
4. **b142**: edit line 166 →
   `STALE_PARENT_COMMIT = "23ad6d38be6a39d1f4d1821961318a60fc9e10b2"`
   **and** line 163 `PARENT_COMMIT = "<X1>"`. Re-run; same two checks. Commit
   as `X2`; advance the block-142 branch to `X2`.
5. Repeat wave by wave for the 26 downstream runners: bump `PARENT_COMMIT` to
   the predecessor's new commit, recompute any hardcoded `PARENT_ARTIFACT_BLOBS`
   with `git rev-parse <commit>:<path>`, re-run, commit, advance the branch.
6. Final sweep: re-assert `PARENT_COMMIT != STALE_PARENT_COMMIT` in all 28
   runners, and add that assertion as a repo-level check so an unanchored sed
   cannot reintroduce it.

Cost: 28 commits, 28 runner re-runs, 17 blob-literal recomputations, and it
rewrites the recorded authority state of every landed block from 141 to 168.

### Option B — the audit-not-correction route (cheaper, matches lane discipline)
The lane's own standing practice for a landed defect is to **measure it in a
successor and leave the landed artifact untouched** — exactly what b166/b167/b168
did for the inertia-convention collision and what b165 did for b164's wrap
artifact (*"no landed note is edited; Block 164 is NOT corrected"*).

A single new audit runner would:
* quote both defective lines with their file/line,
* recompute `stale_parent_artifact_blobs` at the **correct** stale commits
  (`ccfdb57a46…` for b141, `23ad6d38be…` for b142) and show it is `False`,
  i.e. demonstrate that the mutation **would** have been caught,
* recompute it at the **as-landed** value and show it is `True`, i.e. measure
  the defanging,
* state that the two blocks' `stale_parent_authority` controls carry **no
  evidential weight** and that every other gate in b141/b142 is unaffected
  (the defect touches one mutation of fifteen in each runner, routed to gate A
  only),
* and land the `PARENT_COMMIT != STALE_PARENT_COMMIT` invariant as a
  lane-wide check so the class cannot recur.

Option B costs one runner and one commit, changes no landed blob, and leaves
the cascade untouched.

## E. Recommendation

Take **Option B**, and add the anchored-sed / non-identity invariant. Option A
is the only route that literally restores the two controls, but it re-pins 26
landed runners across 16 waves and 17 hardcoded blob literals to recover two
negative controls out of thirty — and the thing those controls guard (that a
stale parent pin is rejected) can be demonstrated conclusively in a successor
without touching a single landed blob. If the owner wants Option A anyway, the
correct values and the wave order above are exactly what it needs; nothing
further has to be discovered.
