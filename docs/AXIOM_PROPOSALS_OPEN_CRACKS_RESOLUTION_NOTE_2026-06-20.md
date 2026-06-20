# Axiom-Update Proposals — Open No-New-Axiom Cracks RESOLUTION (block02, 2026-06-20)

**Date:** 2026-06-20
**Type:** meta / governance proposal (FOR the owner's governance decision — adopts nothing)
**Lane / branch:** `axiom-update-proposals`,
`physics-loop/axiom-update-proposals-block02-20260620`.
**Status authority:** the independent audit lane / owner is the **sole** status
authority. This note sets **no** audit verdict, promotes **no** axiom, edits
**no** axiom registry. It records the honest resolution of the two candidate
no-new-axiom cracks (SK-1, SK-2) that the block01 consolidated note flagged with
an explicit ACTION ("attempt the derivation BEFORE proposing"). Both were
attempted in block02; both **wall**. This is the additive, dated correction.

```yaml
proposal_allowed: false   # owner governance decision required; this note REQUESTS nothing new, it RESOLVES two flags
adopts_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
hypothetical_axiom_status: "not invoked — both SK-1 and SK-2 WALL (no axiom proposed here; the corresponding block01 candidate proposals are CONFIRMED needed, not adopted)"
bare_retained_allowed: false
```

> **Posture (owner-authorized "don't believe the no-gos").** A genuine crack here
> is a **NEW DERIVATION** — it would retire the need for a proposed axiom and is
> strictly higher value than any proposal. Each open crack got a fresh, harder
> skeptical re-attack than the prior block, with a real runner. Honest either way:
> where the primitive note **explicitly disavows** the content the crack needs,
> reading the granted content as the disavowed content would **mis-cite a
> primitive** (registry rule 5, forbidden), so the wall **stands** and the
> proposal is **confirmed needed**. We say so plainly.

---

## 0. Scope and what this resolves

SCOPE = `A_min` (Lattice + Quantum + Record) + the four owner-approved primitives
ONLY (`axiom_premise_nodes.json`: `minimal_axioms`, `scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`). A CRACK = derive the
target from these **WITHOUT** any new axiom/primitive.

Block01 (`docs/AXIOM_UPDATE_PROPOSALS_CONSOLIDATED_2026-06-20.md` §3) listed five
no-new-axiom cracks found en route. Three (N4-LABEL, SK-3, SK-4) **landed** as
genuine no-axiom derivations and already shrank the wall set. **Two were left as
CANDIDATE cracks with an explicit ACTION**, never carried out:

- **SK-1** — derive B-AXIS **N2b** (the absolute blocked time-step `2 a_tau`, the
  Stone-generator clock unit) from `scale_reference × kinetic_isotropy`.
- **SK-2** — close P-ABJ **route (c)** by showing the emergent matter EVALUATION
  complex is forced imbalanced/curved (`χ ≠ 0`) by `A_min`-native geometry.

Block02 carried out both ACTIONs with dedicated runners. **Result: both WALL.**
The two block01 candidate proposals they would have retired (C1's N2b clause;
C3's P-ABJ clause) are therefore **CONFIRMED needed** — not adopted, confirmed as
genuine residuals for the owner's decision.

---

## 1. SK-1 — B-AXIS N2b clock unit `2 a_tau` — **WALL STANDS**

### 1.1 Target and prior wall

The Stone generator of the 2-step blocked staggered transfer
(`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28`) is

```text
    H_hat = - log( T_hat^2 ) / ( 2 a_tau ),     T_hat^2 = T_odd . T_even.
```

**N2b is the absolute value of the denominator `2 a_tau`** (the dimensionful
tick / clock unit). The live wall `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06`
(§"`T` alone does not fix the clock unit", runner W2) proves a fixed positive
transfer `T` fixes only the **product** `tau·H`, never `tau` alone (the same `T`
reconstructs for `tau = 1, 2, 0.7` with `H ∝ 1/tau`). So `T` by itself cannot pin
`2 a_tau`; N2b is a genuine open clock-unit datum. The prior block's
spacing-ratio route `R-KINFORM-N2b` (tried the identity `c_t/c_s = a_tau/a_s`)
walled because the kinetic-isotropy note disavows the spacing ratio.

### 1.2 The SK-1 push (harder than the prior block)

SK-1 does **not** use a spacing-ratio identity. It tests whether
`kinetic_isotropy`'s **"one tick is one edge in FORM"** + `scale_reference`'s
absolute edge length `a` **JOINTLY** pin `2 a_tau` by treating the time edge as
the **SAME edge object** as the space edge — forcing `a_tau = a` directly, with no
separate spacing ratio invoked. The runner constructs the OS0 kinetic form
`Q(p) = c_t ω² + c_s k²` from the staggered action with explicit, **independent**
edges `a_tau, a_s`, and tests exactly which object `c_t = c_s` constrains.

### 1.3 What the runner proves

`scripts/sk1_baxis_n2b_kinform_scale_join_2026_06_20.py` — **TOTAL: PASS=28
FAIL=0** (sympy exact + numpy; deterministic, no RNG in any load-bearing leg;
clean under `python3 -W error`; no empirical import; re-run 2026-06-20, exit 0,
reproduces). Six blocks:

- **(A)** Restoring one `1/a` per lattice difference, the dimensionful inverse
  propagator small-momentum-expands to `Q = c_t ω² + c_s k² + …` with `c_t = 1`,
  `c_s = 1`. **Decisive (A4):** the form ratio `c_t/c_s = 1` is a **dimensionless
  pure number with `a_tau, a_s` ABSORBED into the physical `ω, k`**
  (`free_symbols = []`).
- **(B)** `c_t/c_s = 1` holds at a **continuum** of `a_tau ∈ {1/3, 1, 7/2, 10}`
  (B1, B2): kinetic-isotropy is a **single point true for EVERY `a_tau`**, so it
  cannot select one. The form ratio (constant `1`) and the spacing ratio
  `a_tau/a_s` (varies) are provably **different functions** (B4).
- **(C)** "One tick is one edge in FORM" = range-1 adjacency; its **topology is
  identical** for `a_tau = a_s` and `a_tau = 10 a_s` (C4, explicit NN adjacency
  matrices) — only the metric weight differs. So the "same FORM object" reading is
  satisfied for **every** `a_tau` and does **not** force `a_tau = a_s` (C5). The
  join supplies `{absolute anchor a^{-1}}` and `{form ratio c_t/c_s = 1}` but
  **NOT** the spacing ratio `a_tau/a_s` (C6).
- **(D)** Dissect `2 a_tau`: the factor **2** is the staggered **2-step block
  count** — single-step transfer non-positive (D1, `min|Im eig| = 0.375` over the
  BZ), so the positive object is `T_hat² = T_odd·T_even` over two temporal edges,
  eigenvalues `exp(±2E)`, `E = arcsinh√(m²+sin²p)` exactly (D2, residual `5e-15`).
  Functional-calculus-correct restatement of N2 (log on the positive spectrum):
  `T` fixes only `2 a_tau · H_hat`, never `a_tau`.

### 1.4 Primitive-disavowal check (registry rule 5 — no mis-citation)

> **`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09`.** GRANTS: "`c_t = c_s` … One
> tick is one edge in **form**, not only in spacing"; "this primitive fixes only
> the one **dimensionless** graining ratio." DISAVOWS the SK-1 object exactly:
> "It carries **no dimensionless dynamical content**"; "the **absolute** scale
> belongs to the single approved scale-reference primitive"; "any **spacing**
> ratio or reachability claim lives in its **own derivation row**"; "It does not
> supply the absolute scale (`scale_reference_primitive`) or the **spacing ratio
> (derived from the no-diagonal clause)**; it supplies only the
> kinetic-**form** isotropy."

> **`SCALE_REFERENCE_PRIMITIVE_NOTE`.** GRANTS one dimensionful anchor
> `a^{-1} = M_Pl`. DISAVOWS: "It carries **zero dimensionless content**"; "does
> not assert `a/l_P = 1` as a derived theorem."

The note phrase **"not only in spacing"** deliberately **splits** the granted
FORM claim from the **reserved** SPACING claim, and names a **different supplier**
(the no-diagonal clause) for the spacing ratio. The two notes do not fuse them.

**The only path from these two primitives to `a_tau/a_s = 1` is to read
`kinetic_isotropy`'s granted FORM ratio (`c_t/c_s`, constant `1`) AS the disavowed
metric SPACING ratio (`a_tau/a_s`, varying).** B4 proves these are different
functions; doing so would **mis-cite the primitive** — exactly the laundering the
axiom-premise purity guard (`check_axiom_premise_clean.py`) and the no-laundering
discipline of `docs/audit/AXIOM_MINIMALITY_POLICY.md` §6 forbid (a primitive
chain-satisfies **only for what it grants**). The attempt does **not** mis-cite;
it identifies precisely **why** the wall stands.

### 1.5 Verdict and partial no-axiom progress

**SK-1 does NOT crack N2b. The wall STANDS; the candidate is needed.** The
absolute clock unit `2 a_tau` still needs either a separate **spacing-row
derivation** (the no-diagonal clause the kinetic-isotropy note names as the
spacing supplier — an untested no-axiom lead, flagged for a follow-up block) or a
primitive.

**Partial no-axiom progress (banked):** `2 a_tau = (2) × (a_tau)` where the factor
`2` is the structural 2-step staggered block count (D1–D2, derivable with no
axiom). So N2b's only **axiom-bearing** residual is the single metric time-edge
`a_tau` (equivalently the dimensionless `a_tau/a_s`), **not** the whole `2 a_tau`.
The optimistic block01 SK-1 flag ("`2 a_tau` may be derivable … likely removes
N2b") is **downgraded**: the factor 2 is structural, but `a_tau` walls.

---

## 2. SK-2 — P-ABJ route (c), imbalanced/curved EVALUATION complex — **WALL STANDS**

### 2.1 Target, the exact door, and the path the prior block omitted

`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30` proves the staggered
`ε`-index `A_t[U] = Tr(ε exp(-t D[U]^† D[U])) = 0` for every U(1) background on any
finite **even periodic** torus with **equal** sublattices (`N_+ = N_-`, `B`
square). Its named escape (route (c), fanout ~1105): an **imbalanced or curved
complex with `χ ≠ 0`**. The curvature-free door is a sublattice imbalance
`N_+ ≠ N_-` making `B` rectangular. The runner's **Part A** establishes the exact
criterion: `N_+ = N_-` **iff at least one extent is EVEN**; **ALL-ODD** extents
give `|N_+ − N_-| = 1` exactly — the unique curvature-free door.

The prior block (block05 chi-native-curvature ray) probed only **CLOSED**
complexes and found every `A_min`-native closed complex is flat-cubic `χ = 0`
(time circle / twisted gluings leave `χ = 0`; disclination breaks the
translation-invariant Lattice ⇒ ADMITTED curvature; holonomy off the sea is
state-dependent REGISTERED DATA). **It did not test the OPEN / boundaried /
matter-occupied EVALUATION complex** — the push-harder target here.

### 2.2 What the runner proves

`scripts/frontier_abj_pabj_evaluation_complex_imbalance_2026_06_20.py` — **TOTAL:
PASS=75 FAIL=0** (exact finite linear algebra in numpy; no MC; no empirical
import; re-run 2026-06-20, exit 0, reproduces).

- **(B) The closed/translation-invariant imbalance is disqualified.** The only way
  an imbalance could be closed and translation-invariant is an **all-odd PERIODIC
  torus** — but an odd extent is an **odd cycle, non-bipartite**, so the parity
  grading `ε` is not single-valued under the wrap and `{ε, D} = 0` **BREAKS**
  (`max|εDε + D| = 1.0`); `{ε, D} = 0` holds **iff ALL extents even**. A
  curvature-free imbalance is **unreachable on any closed surface**.
- **(C) The OPEN all-odd box is a live `χ ≠ 0` surface.** On an OPEN
  (Dirichlet/free-edge) all-odd box, `{ε, D} = 0` holds, `B` is rectangular, and
  the signed heat trace `A_t = N_+ − N_- = +1` (t-independent, spread `3e-15`,
  equals the analytic graded zero-mode index, **gauge-robust** under random U(1)).
  Here the square-block proof genuinely fails and route (c) **WOULD** close.
- **(D) The decisive nativity gate — the imbalance is NOT `A_min`-native.**
  - **D1** The index **FLIPS** with the boundary condition: even-periodic torus
    `A_t = 0`; even-open box `A_t = 0`; all-odd-open box `A_t = +1`. A_min's
    Lattice axiom is infinite `Z^3` with **no** boundary condition, so
    open-vs-periodic is a **regulator** choice. A number that flips `0 → ±1`
    across A_min-admissible regulators is not A_min-forced.
  - **D2** Even among OPEN boxes, the imbalance is an **extent-parity** choice:
    open `4³` → 0, open `3³` → +1, open `4×3×3` → 0, open `5×3×3` → +1. A_min
    supplies **no finite extent**.
  - **D3** The realized-state occupied region's imbalance is **REGISTERED DATA**:
    on a balanced `4³` box, two equal-`N=8` occupied regions give imbalance 0 vs
    +4 — a value that changes under another law-admissible state (the
    `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11` counterfactual clause).

### 2.3 Primitive-disavowal check (registry rule 5 — no mis-citation)

> **Lattice axiom (`MINIMAL_AXIOMS_2026-06-05`).** GRANTS `Z^3` adjacency.
> DISAVOWS "boundary condition … continuum or infrared limit" and supplies no
> finite extent. So open-vs-periodic and extent-parity (the only curvature-free
> imbalance levers) are **not A_min-granted**; citing A_min for an open all-odd
> box would be mis-citation.

> **`realized_state` primitive.** GRANTS pointwise evaluation at the supplied
> state. DISAVOWS any "value that would differ had another law-admissible state
> been realized" — the occupied-region imbalance (D3) is exactly such a value.

> **`scale_reference`** (units-only, "zero dimensionless content … no selector")
> and **`kinetic_isotropy`** (OS0 form `c_t = c_s` only, "no selector", "not a new
> dynamics") GRANT no topological/cardinality content ⇒ cannot supply `χ ≠ 0`.

No primitive is mis-cited; the open evaluation complex's nonzero index rests on a
regulator/occupancy input none of the four primitives provide.

### 2.4 Verdict

**SK-2 does NOT crack route (c). The wall STANDS; the candidate is needed.** Every
`A_min`-native front yielding `χ ≠ 0` is one of: (i) an OPEN all-odd box — a
regulator choice (D1/D2); (ii) curvature/disclination — already ADMITTED by the
prior block; (iii) a realized-state occupied region — REGISTERED DATA (D3). The
one closed/translation-invariant imbalance (all-odd periodic torus) is not a valid
`ε`-index surface (non-bipartite, Part B). The P-ABJ wall stands on all of routes
(a)/(b)/(c); the full ABJ fanout (~1105) remains attributed to Cluster 3
(gauge-content / particle-content). The wall is re-localized and **sharpened** onto
the boundary-condition / finite-region / occupancy selection — precisely the
gauge-/particle-content gate the minimal-axioms memo lists as open.

---

## 3. Net resolution of the two open cracks

| Crack | Target | Re-attack (harder than prior block) | Runner | Outcome |
|---|---|---|---|---|
| **SK-1** | B-AXIS N2b clock unit `2 a_tau` | "same FORM edge object" join of `scale_reference × kinetic_isotropy` (not the spacing-ratio identity) | `PASS=28 FAIL=0` | ⛔ **WALL STANDS** — FORM ratio `c_t/c_s = 1` is a single point true for every `a_tau`; the spacing ratio is reserved to its own row; reading FORM as SPACING mis-cites a primitive. Factor 2 is no-axiom structural; `a_tau` is the residual. |
| **SK-2** | P-ABJ route (c) `χ ≠ 0` evaluation complex | the OPEN/boundaried all-odd EVALUATION complex (the path the prior block omitted) | `PASS=75 FAIL=0` | ⛔ **WALL STANDS** — the only curvature-free `χ ≠ 0` surface (open all-odd box, `A_t = +1`) is a regulator/occupancy choice; index flips `0 → ±1` across A_min-admissible BCs; closed all-odd torus non-bipartite. |

**Neither crack lands. No axiom is retired by block02.** The corresponding
block01 candidate proposals are CONFIRMED needed (not adopted):

- **C1 (RP-DYN)** — its N2b clause is **confirmed needed** for the absolute clock
  unit. Narrowing (banked, no axiom): the factor `2` in `2 a_tau` is structural;
  the axiom-bearing residual is the single metric edge `a_tau`. C1 deliberately
  proposes only the **dynamics-side existence** of a step, never the dimensionful
  value `2 a_tau`; SK-1's wall confirms the C1/N2b division of labor (the dynamics
  tick and the metric clock unit are separate residuals). The weakest sufficient
  home for `a_tau` is a no-axiom spacing-row derivation from the no-diagonal
  clause OR, failing that, a single time-edge spacing primitive (one dimensionless
  `a_tau/a_s`), strictly weaker than C1 and disjoint from the FORM content
  `kinetic_isotropy` already supplies.
- **C3 (PIN-GAUGE-CONTENT)** — its P-ABJ clause is **confirmed needed**. SK-2 does
  **not** shrink Cluster 3; the full ABJ fanout (~1105) remains attributed to C3.
  The recommended owner sequence (C1 then C2, defer C3) is unaffected; C3 remains
  required for the ABJ chain.

The block01 minimality clauses are **vindicated**: the consolidated note's own
"does NOT grant the dimensionful tick value `2 a_tau`" (C1) and the P-ABJ
sibling's HEAVY-strength residual (C3) both hold.

---

## 4. Status discipline / policy

- `hypothetical_axiom_status` is **not invoked**: this note reports two **walls**
  (no axiom proposed, no candidate adopted) plus one partial no-axiom structural
  result (the factor 2 in `2 a_tau`).
- No bare `retained` / `promoted`; no audit verdict set; nothing written to
  `docs/audit/data/` (read-only this lane); no `axiom_premise_nodes.json` edit; no
  git ops (orchestrator owns git).
- The independent audit lane / owner is the **sole** status authority. Adoption of
  C1 / C3, if any, routes through `docs/audit/AXIOM_MINIMALITY_POLICY.md` §6.

## 5. Component artifacts

- SK-1 section: `.claude/science/physics-loops/axiom-update-proposals/block02_section_SK1.md`
- SK-2 section: `.claude/science/physics-loops/axiom-update-proposals/block02_section_SK2.md`
- SK-1 runner: `scripts/sk1_baxis_n2b_kinform_scale_join_2026_06_20.py`
  (cache `logs/runner-cache/sk1_baxis_n2b_kinform_scale_join_2026_06_20.txt`)
- SK-2 runner: `scripts/frontier_abj_pabj_evaluation_complex_imbalance_2026_06_20.py`
  (cache `logs/runner-cache/frontier_abj_pabj_evaluation_complex_imbalance_2026_06_20.txt`)
- Consolidated proposal set (additively updated, dated BLOCK02 section):
  `docs/AXIOM_UPDATE_PROPOSALS_CONSOLIDATED_2026-06-20.md`
- Certificate: `.claude/science/physics-loops/axiom-update-proposals/CLAIM_STATUS_CERTIFICATE_block02.md`
