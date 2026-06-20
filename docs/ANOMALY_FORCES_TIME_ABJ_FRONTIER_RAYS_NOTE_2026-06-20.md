# ANOMALY_FORCES_TIME ABJ — Block 05 Frontier Rays (Two Live Supply-Side Rays: P-REC Supply / P-ABJ χ≠0)

> **Key terms used in this doc** are indexed A–Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the canonical
> source-of-truth doc.

**Date:** 2026-06-20
**Type:** frontier_discovery + negative_route_pruning
**Claim type:** no_go (two sharper walls; one registered-data classification)
**Branch:** physics-loop/anomaly-abj-bridge-block05-20260620
**Keystone under attack:**
`anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
(ledger=**unaudited**; fanout 1105) — kept **CONTEXT-ONLY**.
**Parent:** `anomaly_forces_time_theorem` (ledger=**unaudited**) — kept
**CONTEXT-ONLY**.

**Status:** frontier source note awaiting independent audit handling. Status
authority is the **independent audit lane only**; this note asserts no audit
verdict and claims no "retained"/"promoted"/"bare retained" standing. Both rays
are honest frontier negatives (sharper walls + a precise registered-data
classification) reported with non-bare Type:/Claim type: above — not a bare Status
line. **NO crack of the keystone on either ray.**

```yaml
Type: frontier_discovery + negative_route_pruning
Claim type: no_go
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
independent_audit_lane_sole_authority: true
no_new_axiom_or_primitive: true
keystone_decoupled: true
empirical_inputs: none
```

---

## 0. What this block attacked and why

Block 03 closed the anomaly_forces_time ABJ bridge consolidation as a HYBRID: three
deps-all-retained keystone-decoupled bounded cores, four named physical-identification
walls, and ONE partial unlock — the **block02 P-REC consumer reframe** (the keystone
consumer edge B4→B5/EVEN→B6 needs only γ₅-existence, supplied by the taste-singlet
`Γ₅^spin`, invariant over the full `M₄(C)` taste family, no single-taste admission).

The owner Decision-F packet
(`ANOMALY_FORCES_TIME_ABJ_OWNER_DECISION_PACKET_2026-06-20.md`) and the unified note
(`ANOMALY_FORCES_TIME_ABJ_PREMISE_OBSTRUCTION_UNIFIED_NOTE_2026-06-20.md`) left **two
live supply-side rays** — the only places a genuine crack of the 1105 cone could still
come from at A_min scope:

1. **RAY S1 — P-REC SUPPLY side.** The block02 reframe discharged the *consumer*; it
   left the *supplier* (the single-taste / irreducible-Dirac-factor selector) walled as
   registered data on the complex carrier. The highest-value remaining crack candidate:
   could the selector be **DERIVED** (not admitted) once the carrier is reduced to the
   real Majorana form `Cl(3,1)=M₄(R)` and Record's antilinear `J` (K/CPT) is imposed?
2. **RAY P-ABJ χ≠0 — A_min-native curvature.** The open internal route
   (grounding_map `routes_still_to_attempt[3]`, GW-not-necessary re-target): does **any**
   A_min-native mechanism give `χ≠0` / `Q≠0` **without** admitting external curved
   geometry?

A genuine crack of either is a **bigger unlock than the consumer reframe** and is said so
loudly below. Neither cracked. The honest deliverable is **two sharper walls** plus a
decisive **registered-data** classification of the most tempting internal candidate.
Posture: `trace_class = frontier_discovery / negative_route_pruning`. **No wall is sold
as a closure.**

Scope held throughout: A_min = Lattice + Quantum + Record + the four approved primitives
(`minimal_axioms`, `realized_state_primitive`, `kinetic_isotropy`, `scale_reference`). No
new axiom or primitive; functional-calculus-correct algebra ({α}″ as the true commutant,
taste-singlet KD grading — never `span{I,G}`); a realized-state-DEPENDENT result is
REGISTERED DATA, not a derivation (invariance over the law-admissible family is the test);
no empirical/PDG/fitted inputs; `docs/audit/data/` parsed READ-ONLY; no git operations.

---

## RAY S1 — P-REC SUPPLY-SIDE single-taste selector under the real Majorana reduction

**Section of record:**
`.claude/science/physics-loops/anomaly-baxis-wall/block05_section_S1.md`
**Runner:** `scripts/frontier_abj_prec_supply_side_majorana_J_real_selector_2026_06_20.py`
— **TOTAL: PASS=40 FAIL=0** (deterministic across re-runs).
**Cache:** `logs/runner-cache/frontier_abj_prec_supply_side_majorana_J_real_selector_2026_06_20.txt`

### S1.1 — What was tested

Whether imposing the antilinear `J` (Record K/CPT conjugation, built from the CPT-EXACT
relation `ε D ε = −D` with `D` real anti-Hermitian) on the `M₄(C)` taste commutant of the
blocked staggered 2⁴ carrier **FORCES exactly one** `J`-real rank-4 projector onto a Dirac
factor (⇒ single-taste DERIVED, a supply-side crack of the 1105 P-REC edge), or **>1 / 0**
(⇒ wall stands). Computed in-tree: `dim_R` of the `J`-real taste commutant; the count of
`J`-real rank-4 single-taste projectors; the real-form classification (`M₄(R)` vs `M₂(H)`)
via Artin–Wedderburn + minimal-real-idempotent-rank; and the registered-data invariance
over the admissible `J = U_J K` family.

### S1.2 — Method (recomputed in-tree; absorbed runners by path+PASS)

Real numpy runner. Recomputed citation-free: blocked staggered `αμ` on the 2⁴ hypercube
(Cl₄, `{αμ,αν}=2δ I`); the taste-singlet `Γ₅^spin = α₀α₁α₂α₃` (`(Γ₅^spin)²=+I`,
`{Γ₅^spin,αμ}=0`, commutes with the full `M₄(C)` taste commutant, `dim_C=16`); the CPT-EXACT
relation `ε D ε = −D` with `ε` = sublattice parity; the `αμ` are REAL in the lattice basis
(staggered ±1 phases) so bare `K` is the spin Majorana real structure (`J₀=K`, `J₀²=+I`).
Decisive computation: impose `J`-reality, count `J`-real rank-4 projectors; compute the
eigenvalue-multiplicity pattern of generic K-real symmetric taste elements; Artin–Wedderburn
over R with minimal-idempotent-rank tiebreaker; registered-data guard sampling `J = U_J K`.
**Independent cross-check (separate method):** `min ‖conj(P)−P‖` over 12000 candidate rank-4
commutant projectors = **0.277 > 0**. Absorbed by path+PASS (re-confirmed, not rebuilt):
`frontier_abj_prec_r4_taste_reconstruction` (PASS=43), `frontier_abj_prec_consumer_reframe`
(PASS=35), `frontier_abj_prec_spin_taste_clifford_core_bank` (PASS=40).

### S1.3 — Result (decisive)

- `dim_R` of the `J`-real (K-real) taste commutant = **16** (reality halves `M₄(C)`'s
  `dim_R 32` to a full real form).
- **Number of `J`-real rank-4 single-taste projectors = ZERO** (counts `[0,0,…]`). Not
  exactly 1 (no crack), and not ≥2 (the block01 complex-carrier picture). **None.**
- Minimal real idempotent rank = **8**, not 4; every generic K-real symmetric taste element
  has eigenvalue multiplicities **`[8,8]` (Kramers doubling)**.
- Real form: **`M₂(H)` (quaternionic).** Both `M₄(R)` (4·4·1) and `M₂(H)` (2·2·4) fit the
  `dim_R=16` arithmetic; the minimal-real-idempotent-rank (8, not 4) breaks the tie to
  `M₂(H)`, where rank-4 Dirac idempotents are FORBIDDEN. (This is the retained `CL3_TO_CL31`
  `M₄(R)` vs `M₂(H)` contrast made concrete on the taste factor; both complexify to `M₄(C)`.)

### S1.4 — Registered-data check (DECISIVE and load-bearing)

A crack requires exactly ONE `J`-real rank-4 projector for **every** admissible `J` (the
law-admissible family `J = U_J K`, `U_J` unitary in the taste commutant — Record supplies
the SLOT, never `U_J`). Result: the count is **0** for the canonical `K` and **never 1**
across the sampled `J` family (distinct counts = `[0]`). The derivation leg fails over the
whole family. The guard is recorded explicitly: any unique projector (none appeared) would
be `J`-choice / state-dependent ⇒ REGISTERED DATA per `realized_state_primitive`'s
counterfactual clause, not a derivation. The finding is therefore a **law-admissible-family-
invariant NEGATIVE** (a derivation of non-derivability), not a realized-state datum.

### S1.5 — Disposition: SHARPER NO-GO (no crack)

The wall STANDS and is SHARPER. The K-real form of the `M₄(C)` taste commutant is the
quaternionic `M₂(H)`, which has ZERO rank-4 single-taste idempotents. Block01/02 had the
selector merely AMBIGUOUS (≥2 rank-4 projectors on the complex carrier = registered data);
the real Majorana reduction DELETES the rank-4 single-taste object entirely (it is
intrinsically complex). The wall locus moves from "an unforced choice among several" to
"**no rank-4 single-taste object exists in the real form at all**."

**What it unlocks on the 1105 cone:** NO crack — does NOT unlock the keystone. As a sharper
wall it PRUNES the highest-value remaining P-REC supply route (real-reduction-forces-single-
taste) with a runner-verified structural reason, and **REINFORCES the block02 consumer
reframe**: the taste-singlet `Γ₅^spin` is K-fixed and `J`-invariant — the ONLY chirality
object that survives the real reduction — so the consumer's reliance on it is the only
viable route. Redirects any future supply attempt away from rank-4 Dirac-factor selection
(structurally impossible in the real form) toward the quaternionic-structure question itself.

---

## RAY P-ABJ χ≠0 — A_min-native curvature (internal route)

**Section of record:**
`.claude/science/physics-loops/anomaly-baxis-wall/block05_section_CHI.md`
**Runner:** `scripts/frontier_abj_chi_native_curvature_routes_2026_06_20.py`
— **TOTAL: PASS=23 FAIL=0** (deterministic across re-runs).
**Cache:** `logs/runner-cache/frontier_abj_chi_native_curvature_routes_2026_06_20.txt`

### CHI.1 — What was tested

Three genuinely-new fronts the prior runners did not build, on top of the block02 PR-D
anchor (taste-singlet Kähler–Dirac index = Euler char `χ`, +2 on S², product cubical tori
all `χ=0`):
- **(A) Z_τ-extended complex / nontrivial cycles** — does the kinetic-isotropy emergent
  time circle or a twisted time-gluing (Klein bottle, reachable by re-identifying
  cubic-adjacency boundary edges) change `χ`?
- **(B) realized-state INDUCED HOLONOMY** (`INDUCED_HOLONOMY_..._2026-06-10`, curvature
  `C = 1 − |tr Hol|/3`) — does an off-sea matter state carry a framework-internal `χ≠0` /
  nonzero topological charge `Q` the flat vacuum lacks, and is it law-invariant or
  registered data?
- **(C) lattice DISCLINATIONS / angular deficits** reachable from the cubic adjacency
  (square-celled cube surface) — `χ≠0` native or admitted?

### CHI.2 — Method (in-tree CW machinery; absorbed runners by path+PASS)

Real numpy/scipy runner. In-tree CW-complex machinery (integer boundary maps; combinatorial
Hodge Laplacian `L_k=∂ᵀ∂+∂∂ᵀ`; Betti = `dim ker`; graded KD kernel index =
`Σ(−1)^k b_k = Σ(−1)^k f_k = χ`), recomputed citation-free (`χ=+2` on S² rebuilt as a live
anchor). Prong A: faithful product cubical tori (`L≥3`) and square-celled Klein bottles,
f-vectors compared. Prong B: recomputed the induced-holonomy two-pole dichotomy
(sea `C=0`, off-sea `C≈0.73`), then probed (i) topological charge via det-phase winding
around genuinely-closed state-space loops (integer-spectrum generators, `U(2π)=I` verified),
(ii) the realized_state counterfactual (vary state over the law-admissible family, check `C`
invariance), (iii) continuity/quantization of `C`. Prong C: built the cube-surface
disclination (`χ=+2`, KD=+2), verified combinatorial Gauss–Bonnet `Σ_v(1−faces/4)=χ`
in-tree, and enumerated 16 faithful flat-cubic tori (all `χ=0`, all vertex links=4).
Absorbed (not rebuilt): `frontier_abj_pabj_kd_index_chi_tracking` (PASS=45),
`frontier_abj_internal_chi_nonzero_index_escape` (PASS=34),
`frontier_induced_holonomy_..._2026_06_10` (PASS=12), `anomaly_abj_obstruction_unified`.

### CHI.3 — Result (three prongs)

- **(A) Z_τ / twisted gluing CANNOT move χ.** Torus and Klein bottle on the same `4×4` block
  have identical f-vectors `[16,32,16]` ⇒ identical `χ=0`. Because `χ = Σ(−1)^k f_k` is a
  **gluing-invariant cell count**, twisting/gluing the time circle changes
  orientability/homology but never the Euler characteristic.
- **(B) Induced holonomy: state-dependent LOCAL curvature, no native charge.** `C_sea=0`
  exactly, off-sea mean `C≈0.73`. A single realized state carries winding **0**; a nonzero
  winding appears ONLY around a non-contractible loop through OTHER states and varies
  erratically with the chosen loop (`{rank 1,2,4,5}` → windings `{1,−1,−1,0}`), so it is
  realized-PATH / choice data, not a state invariant. `C` is a **local** connection
  invariant (continuous under perturbation; no quantized jumps) — the wrong KIND of object
  for `χ`.
- **(C) Square-celled disclination exists but is ADMITTED curvature.** The cube surface
  (8 vertices, 12 edges, 6 **square** faces; every vertex link = 3 squares = an angular
  deficit) has `χ=8−12+6=2`, KD=+2, verified by in-tree Gauss–Bonnet `8·(1−3/4)=2`. But a
  vertex with ≠4 face-links breaks the **translation-invariant** flat-cubic Lattice axiom —
  it is exactly the admitted angular deficit. All 16 faithful flat-cubic tori (edge lengths
  3..6): every one has `χ=0` and every vertex link = 4 (zero deficit).

### CHI.4 — Registered-data check (DECISIVE and explicit)

Induced-holonomy curvature `C` is **NOT invariant** over the law-admissible realized-state
family (`C=0` on the sea, `C≈0.73` off it, spread ≈0.93). A_min admits BOTH flat and curved
states; the value is fixed by WHICH state is realized, not by the law ⇒ **REGISTERED DATA**
(`realized_state_primitive` counterfactual clause), not a derivation. Any induced topological
winding `Q` is even weaker — realized-PATH / choice data. By contrast the law-admissible
INVARIANTS (gluing-invariance of `χ` across the torus/Klein family; the 16-tori faithful
flat-cubic enumeration) are derivations and they say `χ=0`. So the only positive `χ≠0`
objects (cube surface, S²) are admitted curved geometry, and the only state-induced positive
object (`C`) is registered data — neither is an A_min derivation.

### CHI.5 — Disposition: SHARPER NO-GO (no crack)

No A_min-native `χ≠0` crack ⇒ no internal-route unlock of the 1105 cone. Real, sharper
deliverable: (1) re-localizes the P-ABJ internal-route wall from PR-D's "flat-cubic Lattice
axiom" to the sharper, fuller **"flat-cubic + TRANSLATION-INVARIANT Lattice axiom"** — a
single named geometric admission now also fencing the Z_τ/twisted-gluing route (`χ` is a
gluing-invariant cell count) and the square-celled disclination route (cube surface is
`χ=+2` but breaks translation invariance); (2) definitively classifies the most tempting
internal candidate (induced-holonomy derived curvature) as realized-state registered data
with NO native topological charge — closing that steelman precisely; (3) re-witnesses
non-vacuity `χ=+2` in a SQUARE cell type (cube surface) in addition to PR-D's triangulated
S². The external B2 (Adler–Bell–Jackiw anomaly-to-inconsistency implication) is a separate,
categorically-external admission, untouched.

---

## 1. Final dispositions

| Ray | Edge | What was tested | Runner | PASS/FAIL | Registered-data check | Disposition |
|---|---|---|---|---|---|---|
| S1 | P-REC supply | Does real `Cl(3,1)=M₄(R)` + Record `J` force exactly one rank-4 single-taste projector? | `frontier_abj_prec_supply_side_majorana_J_real_selector_2026_06_20.py` | PASS=40 FAIL=0 | DECISIVE; count 0 for canonical K, never 1 over `J=U_J K` family ⇒ family-invariant NEGATIVE | **sharper_no_go (no crack)**; selector deleted (M₂(H), 0 rank-4 idempotents) |
| P-ABJ χ≠0 | P-ABJ internal | Any A_min-native `χ≠0`/`Q≠0` without admitting curved geometry? | `frontier_abj_chi_native_curvature_routes_2026_06_20.py` | PASS=23 FAIL=0 | DECISIVE; induced `C` not law-invariant (spread ≈0.93) ⇒ registered data; `Q` is path-choice data | **sharper_no_go (no crack) + registered-data**; wall sharpened to flat-cubic + translation-invariant |

**No crack of the keystone on either ray.** No ray genuinely cracked; therefore no
supply-side unlock to flag for an owner-packet addendum on a crack basis. The honest
deliverables are two sharper walls plus the registered-data classification of induced
holonomy — real frontier `negative_route_pruning`, not a closure, and not sold as one.

## 2. What any crack would have unlocked (counterfactual, for the record)

- **A genuine S1 crack** (single-taste DERIVED from the real reduction + Record `J`) would
  have been a **SUPPLY-SIDE unlock of the 1105 cone P-REC edge — strictly bigger than the
  block02 consumer reframe**, supplying the selector the consumer reframe only rendered
  moot. It is NOT found: the count is 0, never 1, across the whole admissible `J` family.
- **A genuine P-ABJ χ≠0 crack** (an A_min-native `χ≠0`/`Q≠0` background) would have unlocked
  the internal route of the P-ABJ/P1 edge, removing the need to admit external curved
  geometry. It is NOT found: `χ` is unreachable inside the translation-invariant flat-cubic
  family, induced curvature is registered data with no native charge, and the only positive
  `χ≠0` objects are admitted curvature.

## 3. Exercise-skill warrant on the new walls

- **S1 (P-REC supply / M₂(H) deletion):** exercise-skill run **NOT warranted** as a fresh
  hard wall. This ray IS the exercise-grade attack on the highest-value supply route
  (`abj-walls-break` SUMMARY ranks S1 rank-4); it was steelmanned (N2), tested
  decisive-failure-first (N3), and defeated with a runner-verified structural reason
  (quaternionic real form). N1≥5 routes + N7 met. No residual sub-wall is left unworked.
- **P-ABJ χ≠0 (translation-invariant flat-cubic):** exercise-skill run **NOT warranted** as
  a fresh hard wall. The three named internal fronts (Z_τ/twisted gluing; induced holonomy;
  disclination) are each closed with an in-tree structural reason; the wall is a single named
  geometric admission. The remaining open object — the external B2 ABJ implication — is
  categorically external by policy, not an A_min-native wall an exercise run would attack.

## 4. Discipline / firewall attestation

- **Four primitives loaded;** functional-calculus-correct algebra ({α}″ as the true
  commutant; taste-singlet KD grading; real form classified by Artin–Wedderburn +
  minimal-idempotent-rank — never `span{I,G}`).
- **Realized-state guard load-bearing on both rays:** S1's decisive negative leg is "no
  admissible `J` derives a unique rank-4 projector"; P-ABJ's induced curvature is classified
  registered data because it is not law-admissible-invariant. Counterfactual clause applied,
  not waved.
- **Absorb-not-rebuild:** in-tree runners cited by path + PASS
  (`frontier_abj_prec_r4_taste_reconstruction` 43, `frontier_abj_prec_consumer_reframe` 35,
  `frontier_abj_prec_spin_taste_clifford_core_bank` 40, `frontier_abj_pabj_kd_index_chi_tracking`
  45, `frontier_abj_internal_chi_nonzero_index_escape` 34,
  `frontier_induced_holonomy_..._2026_06_10` 12, `anomaly_abj_obstruction_unified_2026_06_20`),
  not rebuilt; their residual-0 facts recomputed in the two block05 runners.
- **Retained authorities recomputed in-tree (CONTEXT-ONLY, not cited blind):** `CL3_TO_CL31`
  (M₄(R) vs M₂(H), both → M₄(C)); `CPT_EXACT_REAL_ANTI_HERMITIAN_D` (`εDε=−D`);
  `LORENTZ_BOOST_FREE_STAGGERED`; `ABJ_RESIDUAL_GW_NOT_NECESSARY` (re-target only).
- **No new axiom or primitive. No empirical/PDG/fitted inputs.** Keystone + parent kept
  CONTEXT-ONLY (no load-bearing edge); both confirmed unaudited.
- **No protected surface touched:** no edit to `docs/audit/**`, AUDIT_LEDGER/QUEUE,
  MISSING_DERIVATION_PROMPTS, `docs/publication/**`; `docs/audit/data/` parsed READ-ONLY; no
  row/effective status set. No `git checkout/commit/push/fetch` (orchestrator owns git). The
  **independent audit lane is the sole status authority** before any effective-retained
  movement.

## 5. Load-bearing residuals (the discipline working, both runners)

- **S1:** the 5 initial runner FAILs (against a pre-written block01-style "≥2 rank-4"
  hypothesis) were load-bearing residuals that surfaced the STRONGER true finding (**0**
  rank-4, not ≥2) and were corrected — the runner-exposes-load-bearing-residuals pattern.
- **P-ABJ:** the runner caught FOUR real residuals mid-cycle — two cubical-torus
  degeneracies at edge length 2 (faithful only for `L≥3`; documented as check A1a), a
  spurious det-phase winding `Q≈4.77` from a non-closing random Hermitian loop generator
  (fixed with an integer-spectrum generator, `U(2π)=I` verified), and a tautological `≥0.0`
  check at B4 (replaced by a genuine continuity probe). Fixing the winding probe surfaced the
  sharper finding that the induced winding is realized-path / choice data — stronger than the
  initial "winding 0" claim. None hidden.

---
*Block05 frontier rays of the anomaly_forces_time ABJ bridge attack. Two live supply-side
rays (S1 P-REC supply; P-ABJ χ≠0 internal) attacked decisive-failure-first. NO crack of the
keystone on either: S1 puts the taste spectator into the quaternionic `M₂(H)` with ZERO
rank-4 single-taste idempotents (selector intrinsically complex, deleted by the real
reduction — a sharper wall than block01/02, consumer reframe untouched and reinforced);
P-ABJ finds no A_min-native `χ≠0` (Z_τ/twisted gluing leave `χ=0` as a gluing-invariant cell
count, induced holonomy is realized-state registered data with no native charge, the only
positive `χ≠0` objects are admitted translation-invariance-breaking curvature). Two honest
sharper walls + a registered-data classification; no closure asserted; no new axiom/primitive;
keystone/parent CONTEXT-ONLY; independent audit lane sole authority.*
