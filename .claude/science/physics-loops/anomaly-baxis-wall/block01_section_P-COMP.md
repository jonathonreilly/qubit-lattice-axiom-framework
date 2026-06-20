# Block01 Section — EDGE P-COMP (RH singlet completion)

**Campaign:** anomaly_forces_time ABJ premise-bridge wall consolidation
**Keystone:** `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` (fanout 1105)
**Edge:** P-COMP = existence of the opposite-chirality SU(2)-singlet RH completion template `{u_R, d_R, e_R, n_R}` (incl. the **neutral** singlet `n_R`) consumed by step **(B3)**.
**Branch:** `physics-loop/anomaly-abj-bridge-block01-20260620`
**Runner:** `scripts/frontier_abj_pcomp_block01_template_existence_2026_06_20.py` → `logs/runner-cache/frontier_abj_pcomp_block01_template_existence_2026_06_20.txt` — **TOTAL: PASS=49 FAIL=0**
**Date:** 2026-06-20

---

## 1. Scope and absorbed prior work (do NOT rebuild)

Absorbed via GROUNDING_MAP (re-derived in-tree, not cited blind):

- `abj-pcomp-singlet-classification` branch — `ABJ_P_COMP_SCALE_FREE_SINGLET_COMPLETION_CLASSIFICATION_NOTE_2026-06-18` + runner **PASS=49**: on `Q_L:(2,3)_a, L_L:(2,1)_{-3a}`, GIVEN the template `{u_R,d_R,e_R,n_R}`, anomaly cancellation FORCES `{x,y,z,n}={4a,-2a,-6a,0}` (unique up to `x↔y` triplet swap). I **independently re-derived** this in PART A (checks A1–A7) rather than copying it.
- `abj-hypercharge-completion-boundary` branch — B1/B2/B3 negative lemmas (free-`n_R` family, vectorlike pairs, global rescaling). Re-derived in PART B.

Confirmed the arithmetic split is settled and convention-independent. My block01 mandate is the THREE fresh routes on the **physical existence** residual, plus the bankability assessment.

---

## 2. Arithmetic core — re-derived in-tree (PART A, PASS)

Under the chirality-signed ABJ trace convention (RH singlets subtract from LH traces), with `n=0` imposed:

- `Tr[SU(3)^2 Y]=0` ⇒ `x+y=2a` (A1)
- cubic with `n=0` ⇒ `xy=-8a^2`, so `x,y` are roots of `(t-4a)(t+2a)` (A2)
- linear/grav with `n=0` ⇒ `z=-6a` (A3)
- `Tr[SU(3)^3]`: `2-1-1=0` needs **exactly two** RH color-triplet slots (A5)

Forced template `{4a,-2a,-6a,0}` verified at `a∈{1/3, 2/5, 7/4, -1/2}` (A6); `a=1/3` reproduces the keystone (B3) witness `(4/3,-2/3,-2,0)` exactly (A7, matches keystone note lines 35/104).

---

## 3. Non-vacuity witnesses — the walls are load-bearing (PART B, PASS)

- **B-CE (the load-bearing counterexample):** `(0,2a,-2a,-4a)` cancels **all** the same anomalies (`Tr[Y]`, `Tr[SU(3)^2 Y]`, `Tr[Y^3]`) yet is **non-neutral** (`n=-4a≠0`). ⇒ `n=0` is load-bearing; SM uniqueness fails without it.
- **B1:** the free-`n_R` family `{4a+t, -2a-t, -6a-t, t}` is anomaly-free for **every** `t` ⇒ neutrality `n=0` is a SELECTION, not an anomaly consequence.
- **B2:** vectorlike pairs `(w,-w)` preserve all anomaly zeros ⇒ matter content is **not** anomaly-unique; mirror/vectorlike exclusion is a separate premise.
- **B3:** anomalies are homogeneous in `Y` ⇒ global rescaling preserves zeros; absolute scale is convention (only ratios invariant).

---

## 4. The three FRESH routes (the block01 mandate)

### Route 1 — derive template existence from Record/Cl(3) native matter structure — **WALLED** (PART C)

In-tree recomputation of `CL3_SM_EMBEDDING_THEOREM` (unaudited): the Cl(3) staggered taste carrier `V=(C^2)^{⊗3}` (dim 8) splits into **only** the LH 6+2 surface `{+1/3 ×6, -1 ×2}` (C-R1.1, eigenvalues recomputed numerically). The carrier is a **single chirality** — no opposite-chirality SU(2)-singlet slot appears as a native consequence; the RH completion must be **adjoined**, not derived.

Decisive supplier note: `CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05` (meta) — **Record is a CONSUMER of chirality, not a source**. "Record dynamics can consume realized chiral labels but cannot produce the carrier grading relation." Post-record information cannot supply the opposite-chirality grading; that requires a separate carrier/CAR/Dirac bridge that A_min (Lattice+Quantum+Record) does not provide.

⇒ Route 1 residual relocates to **MINIMAL_AXIOMS withholding** of the second-chirality matter sector / particle content / species. No new axiom permitted ⇒ not derivable here.

### Route 2 — minimal-axioms NO-GO for template existence, steelman-then-attack — **STEELMAN-DEFEAT, not hard impossibility** (PART D)

**Steelman:** "A_min could FORCE the template because (i) the LH surface is native, (ii) anomaly cancellation is a consistency requirement of any gauge theory, (iii) the unique anomaly-free completion IS the SM template — so existence follows from consistency."

**Attack (all three legs recomputed):**
- D-R2.1: a **vectorlike/mirror** completion is anomaly-free with NO chiral RH singlet template ⇒ consistency does not force a chiral template at all.
- D-R2.2: the **non-neutral** chiral model `(0,2a,-2a,-4a)` is also anomaly-free ⇒ the specific template+neutral-singlet is not uniquely consistency-forced.
- D-R2.3: the **two-triplet slot count** (needed for `SU(3)^3` by `2-1-1=0`) is a template INPUT — the carrier supplies zero RH triplets; one triplet leaves residual `1≠0`.

**Verdict:** the standing wall ("template existence not derivable from A_min") is a genuine **conditional no-go** in the form of a steelman-defeat — anomaly-consistency provably **admits** vectorlike + non-neutral alternatives — but it is **NOT a hard impossibility proof**. There is no positive supplier and no closed impossibility theorem: this is a **NEW hard wall** in the no-go sense (see §7).

### Route 3 — derive `n=0` from a framework charge-neutrality / Record-trace condition — **WALLED** (PART E)

- E-R3.1: **Record-trace / total-hypercharge neutrality** (`Σ Y=0`) is exactly the grav anomaly already imposed ⇒ reduces to the B1 family, `n=t` free. Does NOT pin `n`.
- E-R3.2: **RH-singlet-block neutrality** (`Σ_RH Y=0`) DOES algebraically force `n=0` — but:
- E-R3.3: applying the **realized-state-primitive counterfactual test**, RH-block-neutrality **FAILS** on the anomaly-equivalent model `(0,2a,-2a,-4a)` (block sum `=-4a≠0`). A condition that fails over the law-admissible anomaly-equivalent family is an extra selection input, i.e. **registered data, not a derivation** (counterfactual clause of the realized-state primitive).
- E-R3.4: any neutrality strong enough to pin `n` is itself non-derived (fails the counterfactual test); and per Route 1, Record cannot force the signed-vs-absolute readout on the singlet's `Y`.

⇒ `n=0` stays an **ADMITTED branch convention** — exactly matching the retained `ONE_GENERATION_ANOMALY_SINGLET_COMPLETION` note's `NEUTRAL_BRANCH` (named, not derived).

---

## 5. Bankability of the arithmetic core (PART F) — **YES, deps-all-retained**

Ledger facts recomputed from `docs/audit/data/audit_ledger.json` (read-only, parsed with python):

| claim_id | effective_status | chain_closes |
|---|---|---|
| `one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10` | **retained_bounded** | **True** |
| `lh_traceless_eigenvalue_ratio_narrow_theorem_note_2026-05-10` | **retained_bounded** | **True** |
| `cl3_color_automorphism_theorem` | **retained_bounded** | **True** |
| `cl3_complexification_split_narrow_theorem_note_2026-05-10` | **retained** | **True** |
| `one_generation_matter_closure_note` | unaudited | — |
| `rh_completion_color_anti_fundamental_narrow_theorem_note_2026-05-17` | unaudited | — |
| `su3_anomaly_forced_3bar_completion_theorem_note_2026-05-02` | unaudited | — |
| `su3_dabc_symmetric_theorem_note_2026-05-02` | **audited_failed** | False |

**F1/F2:** The P-COMP arithmetic core (`given template + P-HY ⇒ anomalies force {4a,-2a,-6a,0}`) routes through a **deps-all-retained** set (`chain_closes=True`), NOT through the unaudited keystone. In fact the retained `one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10` **already banks** the `n_color=3` RH-Y closed form `(4/3,-2/3,-2,0)` as a conditional `bounded_theorem`; the new scale-free classification (PASS=49) generalizes it parametrically in `a`. This is the **SM_ANOMALY_CLOSURE precedent shape** — bankable as a conditional bounded theorem.

**F3:** Bankable **only with named premises** — conditional on `{template existence (P-COMP), P-HY identification, n=0 branch}` as EXPLICIT admissions (mirror how `SM_ANOMALY_CLOSURE` keeps P/C1-C3 named). Do not silently import the physical identifications as load-bearing.

**F4/F5:** Crucially, the **existence-side suppliers are ALL unaudited** (`one_generation_matter_closure`, `rh_completion_color_anti`, `su3_anomaly_forced_3bar`) and the closest representation-mapping support (`su3_dabc_symmetric`) is **audited_failed**. So **only the arithmetic (RH-Y solving) is bankable**; the **template/existence wall cannot be banked**. P-COMP also remains **circular-on-parent** (the SM witness used by (B3) is the conditional output, not an independent matter-existence supplier); banking the arithmetic core does not resolve the circularity.

---

## 6. Independent confirmation of the documented wall (RH_COMPLETION note)

`RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL_NARROW_THEOREM_NOTE_2026-05-17` (unaudited) states the wall in its own words (lines 257–277, 313): the **existence-side residual** — that RH colored Weyl fermions exist in the framework's matter content at all — is the open gap, NOT closed by any retained theorem, and "SU(3) cancellation alone does not force the SM `3̄ + 3̄` completion" (vectorlike `3+3̄`, adjoint `8` are anomaly-balanced alternatives — same family as my D-R2.1/B2). This corroborates that the P-COMP wall is **physical existence/minimality**, not arithmetic.

---

## 7. Verdict and exercise-skill recommendation

**P-COMP = `arithmetic_closable_identification_walled` + circular-on-parent.** The arithmetic core is bankable deps-all-retained (SM_ANOMALY_CLOSURE shape; one supplier already retained_bounded). All three fresh routes WALL on the **same** A_min withholding of the opposite-chirality matter sector.

This **is a genuinely new hard wall**: template existence has **no positive supplier**, **no closed impossibility theorem**, and the standing wall was previously asserted only via axiom-withholding. Route 2 sharpened it to a steelman-defeat (a conditional no-go) but not a hard impossibility. Per the exercise lessons (do not just declare a no_go), **the repo exercise skill should be run on the P-COMP template-existence wall** before any unified no_go ships — N1 needs ≥5 attacked routes + N7 steelman on the IDENTIFICATION wall; this block adds three fresh genuine attempts plus the N7 steelman, but a positive Record/Cl(3) matter-sector supplier (if one is constructible) would change the verdict and must be honestly hunted first.

**What to carry into the unified note (block02):**
1. Bank the arithmetic core as a conditional bounded theorem with named premises (Decision A), citing the already-retained `one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10`.
2. Wall = physical existence/minimality of the opposite-chirality SU(2)-singlet template + neutral singlet, relocated to MINIMAL_AXIOMS withholding; root supplier-side fact: `CHIRALITY_RECORD_TYPING_INTERFACE` (Record is a consumer, not a chirality source).
3. Non-vacuity: B1/B2/B3 + the `(0,2a,-2a,-4a)` counterexample (n=0 load-bearing).
4. `n=0` is an admitted convention; the counterfactual test rules out deriving it from any neutrality condition.
5. Keep the circular-on-parent flag explicit.
