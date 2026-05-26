# AFT Closure Plan — 5-Cannon Synthesis

**Date:** 2026-05-26
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Type:** synthesis + concrete closure plan
**Status:** **path to retained closure well-mapped; one user-governance decision is the critical dependency.**

## Five-cannon findings

### Cannon 1 — Dependency tree

AFT has 4 admissions:
- **(i) ABJ-to-inconsistency on lattice** — BARE EXTERNAL, no internal note on `main`
- **(ii) RH singlet completion** via `NATIVE_GAUGE_CLOSURE_NOTE` — **RETAINED** (audited_clean, positive_theorem)
- **(iii) chirality grading** via `STAGGERED_DIRAC_KAWAMOTO_SMIT` — unaudited bounded_theorem, queue rank **#16**
- **(iv) single-clock codim-1** via `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1` — unaudited positive_theorem, queue rank **#26**

The single-clock subtree has ~10 unaudited nodes (RP, spectrum, cluster, microcausality, Lorentz). Already-retained nodes form a substantial backbone.

### Cannon 2 — PR 402 fully recoverable

PR 402's content (`AXIOM_FIRST_LATTICE_WESS_ZUMINO_FUJIKAWA_Z4_THEOREM_NOTE_2026-05-02.md` + runner, 1,199-line diff at commit `63d0d9c42`) is **fully recoverable** via `gh pr diff 402`. Closure reasons:
- **(a) Scope/runner mismatch:** note claimed broad WZ/Fujikawa/index/no-counterterm/continuum/nonabelian; runner only checked finite-lattice algebra
- **(b) Policy violation:** PR body and note carried "Expected verdict bracket" language

**Both defects are fixable.** A successor narrowed to W1 + W3 + integer-cocycle corollary, with matched runner, lands cleanly as `unaudited bounded_theorem`.

### Cannon 3 — Three doors

| Door | Effort | Outcome |
|---|---|---|
| **A** | Lowest | Submit AFT as-is → expected `bounded_theorem / audited_conditional` |
| **B** | Medium | Narrower successor to PR 402 → unblocks admission (i) internally |
| **C** | High | Positive_theorem upgrade → requires A+B+full subtree audit |

### Cannon 4 — Hostile review found additional weak links

Beyond admission (i):
- **F-G:** single-clock substrate `Λ = Z_τ × Z³` pre-bakes `d_τ = 1` (substrate-level circularity)
- **F-H:** `ν_R = 0` is SM convention, not retained primitive
- **F-I:** per-site γ_5 (Step 3, Lawson-Michelsohn) vs lattice ε(x) (Step 5, Kawamoto-Smit) silent swap
- **F-J:** even routed companions (iii, iv) are themselves unaudited

**Probability assessment (AFT submitted today):**
- Retains as "forces (3,1)" positive_theorem: **<5%**
- Retains as bounded_theorem: **~40%**
- Verdict `audited_conditional` (most likely): **~45%**
- Demote/retitle: **~10%**

### Cannon 5 — Recommended path

**Option 2':** narrow scope + explicit bare-external labeling for admission (i).

The framework already retains primitives that are standard external QFT (Lieb-Robinson, cluster decomposition, Stone-vN). "No imports" means **no disputed imports**, not **no standard QFT axioms**. ABJ (1969, Adler + Bell-Jackiw, textbook) is in the same class.

## The critical governance decision

> **Is ABJ (1969 textbook chiral anomaly) acceptable as `bare_external_standard_qft_axiom` — same tier as already-retained Lieb-Robinson, cluster decomposition, and Stone-von-Neumann?**

If **YES**: clean 6-step concrete closure path
If **NO**: write narrower successor to PR 402 (Door B), ~40% success probability per hostile review

## Concrete closure plan (assuming user says YES)

**Step 1 (this lane, immediate):** Author AFT v2 amended source note that:
- Classifies admission (i) as `bare_external_standard_qft_axiom`
- Retitles to address F-B + Cannon 4: "ABJ + Cl(3)/Z³ + Retained Primitives ⇒ Consistent (3,1)" (removes "Forces")
- Addresses F-G: explicit acknowledgment that single-clock substrate pre-bakes a temporal axis
- Addresses F-H: flag `ν_R = 0` as SM-convention choice
- Addresses F-I: explicit statement that Step 3 γ_5 is Lawson-Michelsohn dimensional parity, Step 5 is staggered ε(x)

**Step 2 (user governance):** One-line authorization confirming ABJ-as-bare-external.

**Step 3 (this lane):** Submit AFT v2 to audit lane via standard PR workflow.

**Step 4 (audit lane, separate timeline):**
- Process (iii) STAGGERED_DIRAC_KAWAMOTO_SMIT (queue #16)
- Process (iv) SINGLE_CLOCK_CODIM1 (queue #26)
- Process AFT v2 (after iii and iv clear)
- Expected verdict: `retained_bounded` (positive_theorem if all subtrees audit clean)

**Step 5 (this lane, after AFT retains):** Write inheritance sub-lemma:
- "Under retained A1+A2 + retained AFT v2 + cyclotomic algebra: the framework's natural angular unit on the C_N orbit IS the anomaly coefficient's ℝ/ℤ period."

**Step 6 (this lane, after inheritance retains):** Translation lemma becomes a direct consequence. Convention 𝒞_b is FORCED. δ_Brannen = (N-1)/N² rad for both sectors. Closes radian-bridge primitive P.

## Concrete closure plan (assuming user says NO)

**Step 1':** Write narrower successor to PR 402:
- Scope: W1 + W3 only
- Runner matched to load-bearing claims (εDε = -D, t-independence, integer-valuedness with explicit non-trivial U background)
- Strip all verdict-bracket language
- Honest residual: nonabelian cocycle classification open

**Steps 2'-6':** Same as YES path but with audit risk on the WZ-Fujikawa successor.

## Recommendation

**Recommend Option 2' (YES on ABJ classification).**

Rationale:
1. ABJ is in the same epistemic class as Lieb-Robinson — both uncontested QFT results the framework uses as background regardless.
2. PR 402 audit history suggests internalization is difficult.
3. The framework's import policy is no-disputed-imports; standard QFT axioms are not disputed.
4. The "anomaly inheritance" structural content (what the translation lemma needs) is robust to whether ABJ is internalized or external — what matters is anomaly coefficients live in ℝ/ℤ, which is mathematics independent of internalization.
