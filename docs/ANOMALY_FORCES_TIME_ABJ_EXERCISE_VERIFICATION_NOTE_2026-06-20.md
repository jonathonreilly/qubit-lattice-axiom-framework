# ANOMALY_FORCES_TIME ABJ — Exercise-Surfaced Route Verification + Honest Reassessment (Block 02)

**Type:** exercise_route_verification + honest_reassessment (one partial reframe-crack; two decisive no-go KILLs)
**Date:** 2026-06-20
**Branch:** physics-loop/anomaly-abj-bridge-block02-20260620
**Keystone under audit:** `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` (ledger=unaudited; fanout 1105)
**Parent:** `anomaly_forces_time_theorem` (ledger=unaudited)

```yaml
Type: exercise_route_verification + honest_reassessment
Status: ONE partial reframe-crack (P-REC unnecessary for the 1105 consumer, no admission); TWO decisive finite KILLs (P-COMP existence, P-ABJ internal route) that SHARPEN their walls; no native-bankable new derivation; no new axiom/primitive
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
independent_audit_lane_sole_authority: true
```

## 0. What this note is, and the honest headline

Block 01 (`docs/ANOMALY_FORCES_TIME_ABJ_FRESH_ATTEMPTS_STRETCH_NOTE_2026-06-20.md`)
banked three scale-free arithmetic cores (deps-all-retained) and flagged three
genuinely new hard walls for an exercise-skill run (P-COMP existence, P-REC
single-taste selector, P-ABJ internal-route N7 steelman). The `abj-walls-break`
exercise surfaced a route portfolio; block 02 took the three highest-value routes
to **decisive finite runners**. This note records the **verified** outcome of each,
the **final per-wall disposition** after exercise + verification, and what each
crack/reframe **unlocks** on the 1105 cone.

**Honest headline — cracks vs walls (do not soften):**

- **P-REC — PARTIAL CRACK (reframe).** Route PR-A is a **partial unlock**: the
  1105 consumer (keystone B4 → B5/EVEN → B6 chirality+even-dimension edge) consumes
  only γ₅-EXISTENCE (parity-of-n, irreducible-representation-independent), and the
  consumed quantity is taste-dial invariant — so the single-taste / irreducible
  selector P-REC was admitting is a **within-sector dial, not load-bearing**. The
  taste-singlet `Γ₅^spin` discharges the edge with **no new axiom, no new primitive,
  no single-taste admission**. The SELECTOR wall is **not cracked as a supplier
  statement** — it is rendered UNNECESSARY for the consumer.
- **P-COMP — NO CRACK (decisive KILL).** Route PR-B's "likely crack" (the
  complementary Hamming-odd sector is a native RH template supplier) is **dead**.
  A finite computation of the complementary chirality block proves the only
  candidate native supplier is the SU(2)_weak fiber-flip image of the LH content
  (vectorlike), not the chiral opposite-chirality SU(2)-singlet 3̄ template. The
  wall **STANDS, now SHARPENED** from axiom-withholding/steelman-defeat to a
  computed no-go → **register-as-premise**.
- **P-ABJ — NO CRACK (sharper no-go).** Route PR-D builds the campaign's first
  `χ≠0` object: the taste-singlet Kähler–Dirac index DOES track χ and IS nonzero
  (+2) on a curved closed S², but every A_min-native closed complex is a flat
  cubical torus (χ=0). The `χ≠0` geometry is **admitted, not native**. The wall is
  **re-localized** onto A_min's flat-cubic Lattice axiom → **walled**.

> **CORRECTION recorded for the audit lane (rigorous honesty):** any disposition
> shorthand reading "P-COMP: native-bankable-CRACK" is **contradicted by the
> verified runner**. PR-B is `wall_stands`, `cracked=no` — a decisive KILL of the
> candidate crack. The correct P-COMP disposition is **decisive-no-go /
> register-as-premise**. The ONLY crack in this block is the P-REC partial reframe.

Source discipline: every load-bearing fact below was recomputed in-tree by a
numpy runner with explicit residuals and a `TOTAL: PASS=.. FAIL=..` line. Beyond
the three per-route runners, an **independent synthesis verification runner**
re-derives the route-killing / reframe-load-bearing facts from scratch (not by
importing the route runners). The keystone and parent are unaudited and are kept
CONTEXT-ONLY; no load-bearing fact routes through them blind.

## 1. The three verified routes (runner + PASS/FAIL)

| Route | Edge / wall | Outcome | Crack? | Runner | PASS/FAIL |
|---|---|---|---|---|---|
| **PR-A** | P-REC consumer reframe (B4/B5/EVEN single-taste/irreducible selector) | reframes_unnecessary | **partial** | `scripts/frontier_abj_prec_consumer_reframe_2026_06_20.py` | **PASS=35 FAIL=0** |
| **PR-B** | P-COMP existence/minimality of opposite-chirality SU(2)-singlet RH template (+ S4 Record/CPT) | wall_stands (decisive KILL) | **no** | `scripts/frontier_abj_pcomp_hamming_odd_sector_2026_06_20.py` | **PASS=31 FAIL=0** |
| **PR-D** | P-ABJ internal route (KD index vs χ on a family of complexes) | sharper_no_go | **no** | `scripts/frontier_abj_pabj_kd_index_chi_tracking_2026_06_20.py` | **PASS=45 FAIL=0** |
| **SYNTH** | independent recomputation of all three route-killing / reframe facts | confirms all three | n/a | `scripts/frontier_abj_block02_synthesis_verification_2026_06_20.py` | **PASS=29 FAIL=0** |

All three route runners were **re-run** for this note and reproduce their totals
exactly (31/0, 35/0, 45/0). The synthesis runner caught and fixed three real
residual bugs mid-cycle (two floating-point list-equality comparisons and a
reducible-vs-irreducible Clifford-rep error in the nullity table) before reaching
PASS=29 FAIL=0 — the load-bearing-residual pattern, working as intended.

## 2. PR-A — P-REC reframes to UNNECESSARY for the 1105 consumer (PARTIAL CRACK)

**Section:** `.claude/science/physics-loops/anomaly-baxis-wall/block02_section_PR-A-PREC.md`

**What was tested.** Does the keystone (B4/B5) + parent (EVEN parity law phrased
"in irreducible representations" + the P-REC declaration "on the irreducible Dirac
factor") genuinely CONSUME a single-taste / de-tasted **irreducible** γ₅, or only
the **EXISTENCE** of a taste-singlet γ₅ (γ₅²=+I ∧ ∀μ {γ₅,γμ}=0)? And is the
consumed quantity taste-dial-invariant across the `M₄(C)` taste commutant?

**Decisive-FAILURE probe (run BEFORE the crack claim).** Recomputed the
anticommutant-nullity `dim{X : ∀μ {X,γμ}=0}` on the **irreducible** Cl_n rep AND
**reducible** multiplicity-m carriers (γμ⊗I_m, m∈{1,2,4}) for n=2..6, searching for
ANY case where reducibility flips the γ₅ existence verdict (γ₅ on odd n, or no γ₅
on even n). **Independently re-confirmed in the synthesis runner** (A1/A2):

| n | irrep nullity | m=2 | m=4 | verdict (γ₅ exists ⟺ nullity>0) |
|---|---|---|---|---|
| 2 (even) | 1 | 4 | 16 | YES on all |
| 3 (odd)  | 0 | 0 | 0  | NO on all |
| 4 (even) | 1 | 4 | 16 | YES on all |
| 5 (odd)  | 0 | 0 | 0  | NO on all |
| 6 (even) | 1 | 4 | 16 | YES on all |

Reducibility scales the nullity (by m²) but **never flips** the nonzero-vs-zero
verdict — **no flip found** (non-vacuous: a flip would have FAILED the route). The
EVEN parity law's load-bearing content is **parity-of-n only**, and it is
irrep-INDEPENDENT. "In irreducible representations" is the parent runner's
computational convenience (the minimal faithful matrix realization), not a consumed
requirement.

**The witness + dial-invariance.** The block01 taste-singlet `Γ₅^spin = α₀α₁α₂α₃`
on the blocked free staggered 2⁴ carrier satisfies `Γ₅^spin² = +I`,
`{Γ₅^spin, αμ} = 0` (residual 0.0), and commutes with the full `M₄(C)` taste
commutant (residual 1.1e-15) — an explicit witness for the existence predicate on
the **full 4-tasted (reducible) carrier**, with NO taste selected. Varying the
single-taste projector across 12 random `M₄(C)` sectors: γ₅-existence holds on
every dial (residual 3.9e-15), and the per-sector anomaly trace is identical across
all 4 degenerate replicas (spread 6.4e-16). Both consumed quantities are
taste-dial INVARIANT.

**Grep-backed consumer audit.** Read-only grep of keystone + parent for
`irreducible | single-taste | de-tast`: ZERO occurrences in the keystone; every
parent occurrence is either the P-REC premise itself (the claim being reframed) or
the EVEN parenthetical (computational convenience).

**Disposition: P-REC = reframable-UNNECESSARY for the 1105 consumer (PARTIAL CRACK).**
The B4→B5/EVEN→B6 chirality+even-dimension edge is discharged from A_min + the
taste-singlet core, holding invariantly over the entire `M₄(C)` law-admissible taste
family — so it is a **derivation of UNNECESSITY, not realized-state-dependent
registered data**, with no single-taste admission. The block01 SELECTOR wall is
**not cracked as a supplier statement** — it is rendered moot for the consumer.

**Scope fence (honest, load-bearing).** This unlock is the B4/B5/B6
chirality+even-dim edge ONLY. It does NOT touch P-ABJ (B2 external), P-COMP (B3 RH
existence), or P-HY (the "is-gauged" predicate). The d_t=1 pin still needs
SC/(B-AXIS). The independent audit lane is the sole authority to accept this
consumer reading.

**Authorities (recomputed in-tree / CONTEXT-ONLY).** Reused (not rebuilt): block01
P-REC core `frontier_abj_prec_r4_taste_reconstruction_2026_06_20.py`.
`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10` (retained
positive_theorem) — anticommutant-nullity law recomputed on irrep AND reducible
carriers, never imported as a bare A_min derivation.
`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02` (retained_no_go) — root M₂(C) wall.

## 3. PR-B — P-COMP existence is NOT native: decisive KILL (NO CRACK)

**Section:** `.claude/science/physics-loops/anomaly-baxis-wall/block02_section_PR-B-PCOMP.md`

**What was tested (the "likely crack").** Block01's P-COMP runner inspected only the
Hamming-EVEN L-sector of `Λ(C³)=(C²)^⊗3` (dim 8). PR-B's hypothesis: the
complementary Hamming-ODD sector `{|001>,|010>,|100>,|111>}` is the `4_-` chirality
block of `8 = 4_+ ⊕ 4_-`, and its gauge quantum numbers MATCH the RH template
`{u_R,d_R,e_R,n_R}` — which would make P-COMP existence **native** (deps-all-retained
bankable) and break circular-on-parent. PLUS S4: does Record K/CPT conjugation on
the LH 6+2 surface give an SU(2)-singlet chiral image with a J-fixed neutral n=0
ray?

**Decisive-FAILURE test (run BEFORE any crack claim).** If the odd-sector color rep
is the same `3` (not `3̄`), or the odd sector is an SU(2)-doublet (not singlet), or
the J/CPT image is vectorlike, the route is killed. **All failure conditions fired**
(independently re-confirmed in the synthesis runner, B0–B14):

| object | RH template (keystone B3) | Hamming-ODD sector |
|---|---|---|
| chirality (ω ±i block?) | OPPOSITE (RH) | **NOT a chirality block** (ω=Γ₁Γ₂Γ₃ flips Hamming parity; the +i eigenspace is 50/50 even/odd) |
| SU(2)_weak rep | **singlet** (T(F)=0) | **fiber DOUBLET-half** (Casimir=3/4, T₃=±1/2) |
| color rep | **3̄** (A=−1) | carrier color = **3** (A=+1) |
| Y spectrum (a=1/3) | `{4/3,−2/3,−2,0}` | `{+1/3 ×3, −1}` (parity-blind; SAME as even LH) |
| relation to even sector | independent, adjoined | **SU(2)_weak fiber-flip image** (vectorlike) |
| neutral n=0 ray | present (`n_R`) | **absent** (Y has no zero eigenvalue) |

The four route-killing facts, each a PASS confirming the failure-to-match:
(#0) `ω=Γ₁Γ₂Γ₃` is the anti-diagonal bit-complement that FLIPS Hamming parity, so
the Hamming-odd sector is NOT the `4_-` chirality block the route assumed;
(#1) carrier color rep is the fundamental `3` (A=+1), not `3̄` (A=−1);
(#2) Y is parity-blind (`[Y, P_parity]=0`) so the odd sector carries the SAME
`{+1/3 ×3, −1}` as the even LH surface, not `{4/3,−2/3,−2,0}`;
(#3) the odd sector is an SU(2)_weak fiber doublet-half (Casimir=3/4, T₃=±1/2),
reached from the even sector by the SU(2) group element σ₁ on the fiber bit.
S4 (J=CPT) gives a **vectorlike CPT-mirror** (doublet, Y→−Y giving `{−1/3,+1}`,
no native n=0 ray — Y has no zero eigenvalue).

**Disposition: P-COMP = decisive-no-go / register-as-premise (NO CRACK).** The 8-dim
carrier is ONE SU(2)-vectorlike LH generation; it supplies NO independent
opposite-chirality SU(2)-singlet 3̄ RH block. Block01's "RH completion must be
adjoined" is now **PROVEN by direct computation of the complementary block** rather
than asserted from inspecting only the even sector. The opposite-chirality
SU(2)-singlet 3̄ completion (incl. neutral `n_R`) must still be adjoined, and A_min +
the four approved primitives withhold that second-chirality matter sector.

**Bankability (load-bearing honesty).** Only the block01 **arithmetic core**
(given template + n=0 ⇒ `{4a,−2a,−6a,0}`) stays bankable deps-all-retained. The
existence side stays **non-bankable**: suppliers `rh_completion_color_anti_fundamental`
and `su3_anomaly_forced_3bar` are unaudited; `su3_dabc_symmetric` is **audited_failed**;
**circular-on-parent persists**. The keystone P-COMP edge stays a named admitted premise.

**Authorities (recomputed in-tree).** `cl3_color_automorphism_theorem`
(retained_bounded, chain_closes=True), `cl3_complexification_split_narrow_theorem_note_2026-05-10`
(retained, chain_closes=True). Wall corroboration:
`CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05` (Record is a consumer of chirality,
not a source — now made quantitative by S4).

## 4. PR-D — P-ABJ internal route: KD index tracks χ but χ≠0 is admitted (SHARPER NO-GO)

**Section:** `.claude/science/physics-loops/anomaly-baxis-wall/block02_section_PR-D-PABJ.md`

**What was tested.** The internal-route open ray (re-targeted by
`ABJ_RESIDUAL_GW_NOT_NECESSARY`): exhibit a framework-internal `χ≠0`/`Q≠0`
background carrying a nonzero taste-singlet index. Block01's square-block no-go is
tight on the hypercubic 1-skeleton GRAPH (ε-index=0). PR-D tests the OFF-graph ray:
the taste-singlet Kähler–Dirac index on the FULL cochain complex (0-cells ⊕ 1-cells
⊕ 2-cells ⊕ …, graded by `(−1)^k`) over a family from a flat torus (χ=0) to a curved
closed χ≠0 complex (tetra-boundary S², χ=2). Does the index track χ
(Catterall–Butt: KD index = χ)?

**Decisive-failure honesty guard (run BEFORE any crack claim).** Is any χ≠0 complex
A_min-native or admitted? Independently re-confirmed in the synthesis runner
(D1–D7):
- **KD index = χ verified in-tree** (NOT imported blind): combinatorial Hodge
  Laplacians on the tetra-boundary S² give Betti `(1,0,1)`, χ = Σ(−1)^k b_k = +2,
  matching the f-vector `(4,6,4)`. The KD graded-kernel index = +2 — **the first
  χ≠0 of the campaign**.
- **Every A_min-native closed complex is a flat cubical torus.** Enumerated 28
  cubical tori (dim 2..4, edge lengths in {2,3}): **all χ=0**, by the product law
  `χ(S¹)^n = 0`. The full cubical cochain complex on `Z³×Z_τ` (the A_min substrate
  WITH the kinetic-isotropy emergent time edge) has χ=0 at every size and in every
  dimension — adding plaquettes/cubes to block01's 1-skeleton graph does NOT create χ.
- **The χ≠0 carrier (S²) is NOT a cubical torus** — read off its OWN f-vector with
  zero gauge field (categorically distinct from block01 R-C's injected gauge
  topological charge Q). The χ≠0 geometry is **ADMITTED, not native**.

**Disposition: P-ABJ internal route = sharper-no-go / walled (NO CRACK).** The KD/χ
index IS the right object and IS a genuine non-vacuous escape MECHANISM (nonzero
off-substrate), but the geometry that carries it lies outside A_min's flat-cubic
Lattice axiom. The wall is **re-localized** from block01's diffuse GRAPH framing
(`χ≠0 ⇔ all-odd ⇔ grading destroyed`) to a **single named geometric admission — the
flat-cubic Lattice axiom**. The external P-ABJ implication (B2, Adler–Bell–Jackiw
anomaly-to-inconsistency) is untouched and remains a categorically external admission.

**Authorities (recomputed in-tree / CONTEXT-ONLY).**
`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30` (retained_no_go; A_t=0
reproduced on (4,2,2,2)/(4,4,4,4)). `ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28`
(retained_bounded; the re-target ray). Catterall–Butt / Becher–Joos–Rabin
literature kept CONTEXT-ONLY — the KD-index=χ identity is recomputed in-tree, never
presented as an A_min derivation.

## 5. Final per-wall disposition (after exercise + verification)

| Wall | Block-01 status | Block-02 verified disposition | Crack? | Unlocks on the 1105 cone |
|---|---|---|---|---|
| **P-REC** | single-taste SELECTOR wall (new hard wall) | **reframable-UNNECESSARY** for the B4/B5/B6 consumer; selector is a within-sector dial | **partial** | **PARTIAL UNLOCK:** B4→B5/EVEN→B6 chirality+even-dim edge discharged from A_min + taste-singlet core, no admission. Does NOT touch P-ABJ/P-COMP/P-HY; d_t=1 still needs SC. |
| **P-COMP** | template existence WALLED, circular-on-parent (new hard wall) | **decisive-no-go → register-as-premise**; complementary block is vectorlike, not RH | **no** | **No new movement.** Wall SHARPENED to a computed no-go on the complementary chirality block. Existence non-bankable; arithmetic core bankable; circular-on-parent persists. |
| **P-ABJ** | internal route SHARPER-walled; external admission (new hard wall / N7 steelman) | **sharper-no-go → walled**; χ≠0 is admitted curved geometry, not native | **no** | **No audit movement.** Wall re-localized onto the flat-cubic Lattice axiom; N7 steelman discharged (χ≠0 witness exists off-substrate, not A_min-native). External B2 unchanged. |
| **P-HY** | "is-gauged" predicate (wall shrank; block01) | unchanged (not re-attacked in block02) | no | unchanged from block01: arithmetic core bankable; only the "is-gauged" predicate walled. |

**Net for the keystone bridge:** ONE consumer edge (P-REC / B4-B5-B6) is reframed
out of the load-bearing set without an admission (partial unlock). The other three
walls (P-COMP existence, P-ABJ internal+external, P-HY is-gauged) STAND, two of them
now sharper. **No new native-bankable derivation; no new axiom/primitive.** The
keystone remains an unaudited bounded note whose remaining identification premises
(P-COMP existence, P-ABJ external, P-HY is-gauged) stay named admitted premises.

## 6. Firewall / forbidden-surface attestation

New artifacts only: this note, the synthesis verification runner
`scripts/frontier_abj_block02_synthesis_verification_2026_06_20.py` and its cache
`logs/runner-cache/frontier_abj_block02_synthesis_verification_2026_06_20.txt`, the
three per-route sections + runners + caches (already on this branch), and the
branch-local `CLAIM_STATUS_CERTIFICATE_block02.md` + `NO_GO_LEDGER.md` append.
**No file under `docs/audit/`, `docs/publication/`, AUDIT_LEDGER/QUEUE,
MISSING_DERIVATION_PROMPTS was edited.** `docs/audit/data/` was parsed READ-ONLY
(python) for effective_status/chain_closes. No row/effective status set; no audit
verdict asserted. **The independent audit lane is the sole authority** before any
effective-retained movement.

---
*Block 02 of the anomaly_forces_time ABJ bridge attack. Block 03 plan: consolidated
hybrid obstruction note incorporating these verified results + bank the three
block01 arithmetic cores as standalone deps-all-retained bounded theorems. See
CLAIM_STATUS_CERTIFICATE_block02.md and the appended NO_GO_LEDGER.md.*
