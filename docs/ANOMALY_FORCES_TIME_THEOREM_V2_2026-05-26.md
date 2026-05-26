# Consistent (3,1) Signature From ABJ + Cl(3)/Z³ + Retained Primitives (AFT v2)

**Date:** 2026-05-26
**Type:** `bounded_theorem` proposal — citation/scope refinement of the
predecessor `ANOMALY_FORCES_TIME_THEOREM.md` (2026-04-24).
**Lane:** source-only. This note is a successor amendment; it does
**not** edit, retire, or re-classify the v1 row in any audit index.
The v1 row stays where it is; this v2 row enters as a new
`unaudited bounded_theorem` and is judged independently.
**Status authority:** independent audit lane only. This note does not
set, predict, estimate, or bracket any audit verdict. No
"expected-verdict" language appears anywhere in this file by design.
**Primary runner:** `scripts/frontier_anomaly_forces_time.py`
(unchanged from v1; the algebraic content of the chain is unchanged).
**Predecessor note:** [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)
(v1, 2026-04-24, currently `bounded_theorem`, audit-pending).
**Hostile-audit input addressed:**
[`ANOMALY_FORCES_TIME_NOTE_2026-05-16.md`](ANOMALY_FORCES_TIME_NOTE_2026-05-16.md)
(F-A, F-B, F-C) plus the lane-internal Cannon-4 fan-out findings
F-G (substrate circularity), F-H (`ν_R = 0` SM convention), and F-I
(per-site γ₅ vs. lattice ε(x)).
**Companion (PR 1 in this two-PR sequence):**
[`AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md).
Internal Z⁴ lattice re-proof of the Adler-Bell-Jackiw chain
(W1, W3, C-int); itself `unaudited`. This v2 imports the internal
proof as a citation; the import remains *pending* until PR 1 audits.

## What this amendment changes (summary)

This v2 is a **scope/citation refinement**, not a structural change to
the proof. The five algebraic steps (Step 1 anomaly traces, Step 2
right-handed completion, Step 3 chirality requires even total
dimension, Step 4 single-clock excludes `d_τ > 1`, Step 5 conclusion)
are identical to v1. What changes:

1. **Retitle (F-B).** The v1 title "Anomaly Cancellation Forces 3+1
   Spacetime" overclaims. ABJ + chirality forces only
   `d_total = d_s + d_t even`. The selection of `d_τ = 1` comes from
   the single-clock codimension-1 evolution theorem (admission (iv)
   in v1), not from ABJ. The v2 title drops "Forces" and reads as a
   *consistency* statement: given ABJ + Cl(3)/Z³ + retained
   primitives, signature (3,1) is the unique consistent outcome — but
   the title no longer asserts that ABJ alone *derives* time.

2. **Admission (i) closure path (F-A).** v1 carried admission (i)
   (ABJ-to-inconsistency on the lattice) as a **bare external
   admission** to Adler 1969 and Bell-Jackiw 1969 after PR 402 closed
   without merge. v2 replaces this bare-external import with a
   citation to the internal narrow lattice re-proof in PR 1
   (`AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26`).
   That note is itself `unaudited`, so the v2 import is classified
   as **"internal proof pending audit"** on the date of this note.
   When PR 1's narrow theorem audits, this classification flips to
   **"retained internal proof"** *without any structural change to
   v2*. Until that audit lands, v2 is honestly a **conditional bridge**
   on the success of PR 1.

3. **Step 4 substrate-circularity acknowledged (F-G).** The
   single-clock codimension-1 evolution theorem
   (`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`)
   constructs its argument on the substrate `Z_τ × Z³`, which
   *pre-bakes* a temporal direction. v2 makes this circularity
   explicit: AFT v2's content is *conditional* — "given chirality
   forces `d_s + d_t` even and `d_τ > 0`, the single-clock substrate
   forces `d_τ = 1`". It is **not** a derivation of temporal
   emergence ex nihilo. The v2 title and the proof's Step 4 are
   revised so that this conditional structure is visible upfront.

4. **`ν_R = 0` SM convention flagged (F-H).** v1 Step 2 imposes
   `ν_R = 0` (no right-handed neutrino) to select the Standard Model
   branch from the two-branch anomaly-cancellation solution. v2
   flags this explicitly as an **SM-convention input**: the
   *structural* content of AFT (anomaly cancellation forces chirality
   forces `d_s + d_t` even) is robust to this convention. The
   *specific SM matter content* (the `y_1, y_2, y_3, y_4` hypercharge
   tuple) uses `ν_R = 0` as a labelling convention. If the framework
   later includes a right-handed neutrino, only the matter labelling
   shifts; the time-dimension conclusion does not.

5. **Per-site γ₅ vs. lattice ε(x) book-keeping (F-I).** Two
   structurally distinct chirality objects appear in the chain and
   were not clearly separated in v1:
   - **Step 3** invokes Lawson-Michelsohn (Cl(p,q) volume element):
     a per-site Clifford-algebra argument forcing `d_s + d_t` even.
   - **Step 5 / admission (iii)** invokes the staggered sublattice
     parity `ε(x)` (now `(-1)^{x_1+x_2+x_3+x_4}` on Z⁴ from PR 1, or
     `(-1)^{x_1+x_2+x_3}` on Z³ in the v1 chain) for the lattice
     ABJ anomaly evaluation.

   These are **different objects**: Step 3's γ₅ is a per-fiber
   Clifford element whose existence is an algebra parity question;
   Step 5's ε(x) is a site-coordinate scalar whose anticommutation
   with the staggered Dirac comes from Kogut-Susskind hop phases. v2
   adds a dedicated **"Chirality object book-keeping"** section to
   keep these straight; v1 conflated them under a single γ₅ symbol.

6. **All verdict-bracket language stripped.** v1 contained no such
   language; v2 also contains none. This is recorded as a positive
   non-change for audit-prep completeness.

## Chirality object book-keeping (F-I, new section)

The chain uses **two distinct** chirality-grading objects that must
not be conflated:

| Object | Role | Lives on | Theorem invoked | Anticommutation |
|---|---|---|---|---|
| `γ₅` (Clifford volume element) | parity argument: even total dimension required for a γ₅ that anticommutes with all γ_μ | per-site Cl(p,q) fiber | Lawson-Michelsohn (Spin Geometry, Ch. I) | `{γ₅, γ_μ} = 0` iff `p + q` even |
| `ε(x)` (staggered sublattice parity) | lattice ABJ anomaly trace evaluation: anticommutes with staggered Dirac D | site-index Z^d (d = 3 in v1, d = 4 in PR 1) | Kogut-Susskind / Karsten-Smit / PR 1 W1+W3 | `{ε, D_staggered} = 0` from hop phases |

These are orthogonal: the volume-element γ₅ acts inside the per-site
Hilbert fiber `C²` and is constrained by Cl(p,q) parity; the
staggered ε(x) acts on the site-index direction `ℓ²(Λ)` and is
constrained by the staggered Dirac hop structure. The retained
no-go [`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`](NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md)
forbids a per-site γ₅ *inside the C² fiber* of Cl(3); it does **not**
forbid the staggered ε(x) *on the site index*, and PR 1 verifies
`ε D ε = -D` at machine precision on Z⁴ free and gauged. The two
objects coexist without contradiction. The v1 text used the symbol
`γ₅` for both roles in places; v2 keeps them separate by symbol and
section.

Step 3 (Cl(p,q) parity → `d_s + d_t` even) uses the volume-element
chirality. Step 5 / the lattice ABJ trace evaluation uses the
staggered ε(x). Both are load-bearing in their respective steps;
neither substitutes for the other.

## Citation chain on current `main` (under v2)

Step-by-step admissions, with v2 routing:

| Admission | v1 routing | v2 routing |
|---|---|---|
| (i) ABJ anomaly-to-inconsistency on the lattice | bare external (Adler 1969 [1], Bell-Jackiw 1969 [2]); PR 402 closed without merge | **internal proof pending audit**: `AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26` (PR 1, this two-PR sequence). Bare-external Adler/Bell-Jackiw demoted to **sidecar context**, not load-bearing import. |
| (ii) opposite-chirality SU(2)-singlet completion | `NATIVE_GAUGE_CLOSURE_NOTE.md` (audit-pending aggregator) | unchanged |
| (iii) chirality grading for ABJ trace evaluation | `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07` Step 4 (post-F-C correction 2026-05-17) | unchanged routing; the v2 book-keeping section clarifies that this object (ε(x)) is **distinct** from the Step 3 Lawson-Michelsohn γ₅ |
| (iv) single-clock codimension-1 evolution | `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03` (proposed_retained, audit-pending; PR 418 merged 2026-05-03) | unchanged routing; **F-G substrate circularity** acknowledged: this theorem starts from `Z_τ × Z³` and hence is the inheritance source of `d_τ ≥ 1`, not its derivation |

Retained primitives invoked elsewhere in the chain — Lieb-Robinson
velocity bound, cluster decomposition, reflection positivity,
microcausality — are imported as retained and require no re-proof.

## Sidecar external citations (context, not load-bearing)

With PR 1 internalizing the ABJ chain, the following are demoted from
"load-bearing external admissions" to **sidecar context**:

- Adler 1969 (Phys. Rev. 177, 2426) — original U(1) axial anomaly.
- Bell-Jackiw 1969 (Nuovo Cim. A 60, 47) — independent derivation.
- Fujikawa 1979/80 (PRL 42, 1195; PRD 21, 2848) — path-integral
  Jacobian formulation that PR 1 re-derives on Z⁴.
- Wess-Zumino 1971 (Phys. Lett. B 37, 95) — consistency condition.
- Atiyah-Singer 1968 / Atiyah-Patodi-Singer 1975 — index theory
  context for the integer-valued PR 1 lattice index.
- Lawson-Michelsohn, *Spin Geometry* (1989), Ch. I — Cl(p,q) volume
  element parity; still load-bearing for Step 3, but as a standard
  algebra reference, not as a quantum-field-theory admission.
- Craig-Weinstein 2009 / Tegmark 1997 — classical-PDE
  ultrahyperbolic obstruction; cross-reference for Step 4 only,
  not load-bearing.

## Theorem statement (v2 form)

Let Cl(3) act per-site on `Z³` with the gauge content
`su(2) + su(3) + u(1)` and left-handed matter `(2,3)_{+1/3} + (2,1)_{-1}`
(per `NATIVE_GAUGE_CLOSURE_NOTE.md`). Assume:

- (i) the internal lattice ABJ chain
  (`AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26`,
  W1+W3+C-int): nontrivial integer-cocycle implies no local
  counterterm can restore gauge invariance, hence the chiral gauge
  theory is inconsistent on backgrounds where the index is non-zero;
- (ii) the opposite-chirality SU(2)-singlet completion via
  `NATIVE_GAUGE_CLOSURE_NOTE` and the `ν_R = 0` SM convention
  (flagged: structural conclusions are robust to this convention);
- (iii) the staggered sublattice parity `ε(x)` with
  `{ε, D_staggered} = 0` per
  `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07`;
- (iv) single-clock codimension-1 evolution on `Z_τ × Z³` per
  `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`.

Then signature `(3,1)` is the unique consistent outcome:

1. Step 1-2 (ABJ + cancellation) force a chirality grading on the
   matter spectrum.
2. Step 3 (Lawson-Michelsohn) forces `d_s + d_t` even, hence `d_t`
   odd given `d_s = 3`.
3. Step 4 (single-clock on `Z_τ × Z³`) forces `d_τ = 1` *within its
   substrate* — this is inheritance, not derivation; the conditional
   nature is explicit per F-G.
4. Combining: `d_t ∈ {odd positives}` ∩ `{1}` = `{1}`.

The structural content is **"ABJ + chirality + single-clock real-time
evolution + Cl(3)/Z³ are consistent with signature (3,1) and no other
signature"**, not "ABJ alone derives time".

## Load-bearing class and promotion path

- **On current `main` (2026-05-26):** `bounded_theorem` (B-class
  conditional bridge). The bridge is conditional on PR 1's internal
  ABJ proof auditing. Until then, admission (i) is "internal proof
  pending audit" — strictly stronger than v1's bare-external import,
  but still not retained.
- **After PR 1 audits to retained:** admission (i) becomes a
  citation to a retained internal proof; v2's classification shifts
  from "internal proof pending audit" to "retained internal proof"
  *without* any change to v2's text or proof. v2 itself would then
  become eligible for its own audit and potential promotion.
- **Promotion authority:** independent audit lane only. This source
  note does not assign, predict, or propose any retained or
  positive_theorem status.

## Honest acknowledgment: what v2 adds vs. v1

v2 is a **scope/citation refinement**, not a structural change:

- **Unchanged:** the five-step algebraic chain (anomaly arithmetic,
  cancellation algebra, Clifford parity, single-clock exclusion,
  combinatorial conclusion). The primary runner is unchanged.
- **Changed:**
  - Admission (i) import classification (bare-external → internal
    proof pending audit).
  - Title (drops "Forces" overclaim per F-B).
  - Explicit acknowledgment of F-G substrate inheritance at Step 4.
  - Explicit `ν_R = 0` convention flag (F-H).
  - Dedicated chirality book-keeping section (F-I).

v2 is therefore a **conditional bridge** until PR 1 audits. It is
strictly more honest than v1: bare-external ABJ is replaced by a
named internal proof, and the F-B / F-G / F-H / F-I overclaims and
elisions are surfaced rather than buried. The structural promise of
the chain is the same; the import bookkeeping is cleaner.

## Audit-lane handoff

```yaml
proposed_claim_type: bounded_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  v2 of the anomaly-and-time bridge. Re-cites admission (i) to the
  internal narrow lattice WZ-Fujikawa proof
  (AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26,
  PR 1 in this two-PR sequence), which is itself unaudited. v2 is
  therefore a conditional bridge until PR 1 audits. Hostile-audit
  findings F-A, F-B, F-C (from ANOMALY_FORCES_TIME_NOTE_2026-05-16),
  plus the Cannon-4 fan-out findings F-G, F-H, F-I, are addressed
  in the text. The source author does NOT propose retained or
  positive_theorem promotion. Independent audit lane decides verdict.
admission_routing_status:
  - admission_id: i
    description: ABJ anomaly-to-inconsistency on the lattice
    routing_state: internal proof pending audit
    routed_to: docs/AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md
    sidecar_external: [Adler 1969, Bell-Jackiw 1969, Fujikawa 1979/80, Wess-Zumino 1971]
    classification_change_on_pr1_audit: |
      if PR 1 audits to retained, this admission becomes
      "retained internal proof" with no change to v2 text
  - admission_id: ii
    routing_state: unchanged from v1
    routed_to: docs/NATIVE_GAUGE_CLOSURE_NOTE.md
  - admission_id: iii
    routing_state: unchanged from v1 (post-F-C correction)
    routed_to: docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md
    book_keeping_clarification_added_in_v2: |
      Step 3 (Cl volume element γ₅) and Step 5 (staggered ε(x)) are
      now flagged as DISTINCT chirality objects; see new
      "Chirality object book-keeping" section
  - admission_id: iv
    routing_state: unchanged from v1
    routed_to: docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md
    f_g_acknowledgment_added_in_v2: |
      this admission's substrate (Z_τ × Z³) pre-bakes a temporal
      direction; v2 acknowledges Step 4 is inheritance, not
      derivation of time emergence ex nihilo
hostile_audit_findings_addressed:
  - id: F-A
    source: ANOMALY_FORCES_TIME_NOTE_2026-05-16
    v2_response: |
      bare-external ABJ admission replaced by citation to PR 1
      internal proof; conditional on PR 1 auditing
  - id: F-B
    source: ANOMALY_FORCES_TIME_NOTE_2026-05-16
    v2_response: |
      retitled from "Forces 3+1 Spacetime" to "Consistent (3,1)
      Signature From ABJ + Cl(3)/Z³ + Retained Primitives"
  - id: F-C
    source: ANOMALY_FORCES_TIME_NOTE_2026-05-16
    v2_response: |
      v1 already corrected the routing 2026-05-17 (PR #1262);
      v2 inherits the corrected routing
  - id: F-G
    source: lane-internal Cannon-4 fan-out
    v2_response: |
      Step 4 substrate-circularity acknowledged explicitly; AFT v2
      framed as conditional structural result, not ex-nihilo time
      derivation
  - id: F-H
    source: lane-internal Cannon-4 fan-out
    v2_response: |
      nu_R = 0 flagged as SM-convention input; structural
      conclusions robust to this choice
  - id: F-I
    source: lane-internal Cannon-4 fan-out
    v2_response: |
      dedicated "Chirality object book-keeping" section separates
      Step 3 (per-site Cl volume element) from Step 5 (lattice
      sublattice parity ε(x)); these are distinct objects
proposed_claim_scope: |
  Given the internal lattice ABJ chain (PR 1, pending audit) +
  Cl(3)/Z³ gauge content + retained single-clock evolution
  + retained Lieb-Robinson / cluster decomposition / RP positivity
  / microcausality, signature (3,1) is the unique consistent
  outcome. This is a conditional bridge: classification of
  admission (i) flips from "internal proof pending audit" to
  "retained internal proof" automatically when PR 1 audits.
proposed_load_bearing_step_class: B (bounded conditional bridge)
status_authority: independent audit lane only
companion_pr_status:
  - PR 1 (this two-PR sequence): lattice WZ-Fujikawa narrow theorem;
    unaudited on date of v2
  - PR 2 (this note): AFT v2 amendment; unaudited
v1_status_under_v2: |
  v1 (ANOMALY_FORCES_TIME_THEOREM.md, 2026-04-24) is NOT edited,
  retired, or re-classified by this v2. v1 remains an
  independent bounded_theorem row; v2 enters as a separate row.
  The audit lane decides each row's verdict independently.
```

## References

(Sidecar context only; not load-bearing imports under v2. The
load-bearing ABJ chain is now PR 1.)

[1] S. L. Adler, "Axial-vector vertex in spinor electrodynamics,"
    Phys. Rev. 177, 2426 (1969).

[2] J. S. Bell and R. Jackiw, "A PCAC puzzle: π⁰ → γγ in the σ
    model," Nuovo Cim. A 60, 47 (1969).

[3] J. Wess and B. Zumino, "Consequences of anomalous Ward
    identities," Phys. Lett. B 37, 95 (1971).

[4] K. Fujikawa, "Path integral measure for gauge invariant
    theories," Phys. Rev. Lett. 42, 1195 (1979); Phys. Rev. D 21,
    2848 (1980).

[5] M. F. Atiyah and I. M. Singer, "The Index of Elliptic
    Operators," Ann. Math. 87, 484 (1968); M. F. Atiyah,
    V. K. Patodi and I. M. Singer, "Spectral asymmetry and
    Riemannian geometry," Math. Proc. Camb. Phil. Soc. (1975).

[6] H. B. Lawson and M.-L. Michelsohn, *Spin Geometry*,
    Princeton University Press (1989), Ch. I.

[7] W. Craig and S. Weinstein, "On determinism and well-posedness
    in multiple time dimensions," Proc. Roy. Soc. A 465, 3023
    (2009). arXiv:0812.0210.

[8] M. Tegmark, "On the dimensionality of spacetime," Class. Quant.
    Grav. 14, L69 (1997). arXiv:gr-qc/9702052.
