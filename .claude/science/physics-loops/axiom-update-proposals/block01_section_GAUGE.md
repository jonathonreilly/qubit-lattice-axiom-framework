# block01 — Section: GAUGE-CONTENT / PARTICLE-CONTENT cluster (P-HY, P-COMP)

**Lane:** axiom-update-proposals, branch
`physics-loop/axiom-update-proposals-block01-20260620`.
**Cluster:** Cluster 3 of `WALL_TO_GATE_MAP.md` — gauge group / particle content
/ species gate (the gauge/content half).
**Posture:** OWNER-authorized to propose axiom updates. This section maps the
consequences of an **UNADOPTED** candidate primitive; it adopts nothing and sets
no audit verdict.

**`hypothetical_axiom_status` (throughout):** *"conditional on accepted new
axiom; not retained on the actual current surface."*

**Deliverables**
- Proposal note: `docs/AXIOM_UPDATE_PROPOSAL_GAUGE_CONTENT_2026-06-20.md`
- Runner: `scripts/axiom_update_proposal_gauge_content_2026_06_20.py`
- Runner cache: `logs/runner-cache/axiom_update_proposal_gauge_content_2026_06_20.txt`
  — **TOTAL: PASS=21 FAIL=0**

---

## Walls in this cluster

Both are gauge/particle-content premises of `ANOMALY_FORCES_TIME_THEOREM.md`,
living in the `MINIMAL_AXIOMS_2026-06-05.md` open gate "gauge group / particle
content / species" (Quantum's text excludes these explicitly):

| Wall | Statement | Source that declines to supply it |
|---|---|---|
| **P-HY** | the traceless `Y_like` `u(1)` direction is a **gauged** `U(1)` | `NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23` (eigenvalue surface only; "not anomaly-complete `U(1)_Y`") |
| **P-COMP** | the completion is the **opposite-chirality** SU(2)-singlet RH template (existence) | `ANOMALY_FORCES_TIME_THEOREM` P-COMP row (SM branch is a computed existence witness only) |

Fanout (`load_bearing_summary.json`): `anomaly_forces_time_theorem td=1049`;
native-gauge cone `native_gauge_closure_note td=1361`. Highest of the three
clusters.

---

## Skeptical no-new-axiom re-attack (FIRST) — both walls hold

**P-HY.** The four published gauging-selection discriminators
(`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08`) are
reproduced fresh in the runner (`[A1]`) and each is blind/one-sided/circular:
maximality (irreducible ⇒ commutant `C·I` for both the dim-12 algebra and a full
`u(6)` set), `d_{abc}` (one-sided filter: `su2 d=0`, `su3 d≠0`), chirality
grading (`[ε, T_color]=0`), reality bilinear (separates complex color from a real
vector but selects no gauged `U(1)`). The gate note asserts **no** N1–N8 no-go,
so this is an **open gate** — but no natural no-axiom route forces "is-gauged."
**Does not crack.**

**P-COMP.** Two vector-like traps defeat any native completion (the block02
"naive CPT-mirror → vectorlike" + "Hamming-odd native-RH killed" lessons),
reproduced in the runner (`[A2]`, `[A3]`):
- naive CPT mirror cancels all six anomalies but the spectrum **equals its CPT
  conjugate** → vector-like, chirally inert (no second chirality class);
- native taste-cube complementation `c(b)=1-b` maps `L_k → L_{3-k}` and its
  single-bond `γ₅` admits a trivial `γ₅=±I` (vector-like) survivor admissible on
  `{Lattice,Quantum,Record}` (`ε` is a **free selector** until `{D,γ₅}=0` is
  imposed — `STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR…_2026-06-06`).
The wall is real: the LH content **alone is anomalous** (`Tr[Y³]=-16/9`,
`Tr[SU3²Y]=+1/3`, `SU3³=+2`, runner `[A4]`), so a completion is required — but no
*chiral* completion is forced. **Does not crack.**

---

## Candidate primitive (minimal)

> **PIN-GAUGE-CONTENT (UNADOPTED).** (i) the canonical traceless `u(1)`
> direction `Y_like` supplied by graph_first **is gauged**; (ii) the matter
> carrier is completed by an **opposite-chirality (RH) SU(2)-singlet template**
> — chirality **stipulated** (the chiral completion, not the vector-like CPT
> mirror), `Y_{νR}=0`.

**The chirality stipulation is load-bearing (block02 caveat).** Falsification leg
**F3**: the naive CPT-mirror completion cancels all six anomalies but is chirally
**inert** (vector-like) → no `d_t`-odd lower bound. A primitive asserting only
"a completion exists" would be satisfied by the inert mirror. So the primitive
must say **opposite-chirality** — exactly the precision block02 demands.

**Minimality.** Grants only the *gauged predicate* (i) and the *chirality-class
predicate* (ii); both land in the gate the memo declares outside axiom content
(not a §1 reword). Does **not** grant the RH hypercharge *values* (forced by the
SHIFT relation, banked exactly), the branch convention (named discrete
convention, F2), `n_color=3`, generation count, the non-abelian content
(retained), P-ABJ/P-REC, or any coupling/mass/mixing. Weakest sufficient: the
arithmetic and non-abelian algebra are already on the surface; only these two
predicates are missing. **Splittable** into P-HY-gauging / P-COMP-chirality.

**Consistent with retained no-gos** (a new axiom must add, not contradict): no
collision with `NO_PER_SITE_CHIRALITY` (chirality on the taste-reconstructed
factor, not per-site), `ABJ_EPSILON_INDEX_SQUARE_BLOCK` (content, not the index
route), `REGISTRATION_REINSTATES_CHIRALITY` (chirality via gauge-content
primitive, not via Record — which is *why* a separate primitive is the vehicle),
or `FLAVOR_ABSOLUTE_HANDEDNESS_IS_GAUGE` (matter-content `Z₂` ≠ generation-sector
`Z₂`).

---

## Conditional discharge (runner HALF B) — all `hypothetical_axiom_status`

- **B1**: chiral RH template `(4/3,-2/3,-2,0)` cancels all six conditions exactly.
- **B2**: full content is genuinely chiral (spectrum ≠ CPT conjugate; ≠ inert
  mirror) ⇒ second chirality class exists.
- **B3**: SHIFT closed form parametric in `n_color`; `n_color=3` ⇒ SM branch
  (existence witness); `Y_{uR}+Y_{dR}=2a` for all `nc`.
- **B4**: with `Y_like` gauged (i), the nonzero LH traces are GAUGE anomalies ⇒
  cancellation is a consistency demand (P-ABJ bites) ⇒ with the retained EVEN
  Clifford theorem and the genuine second chirality class, `d_s+d_t` even ⇒
  (`d_s=3`) **`d_t` odd ≥ 1** (lower-bound half of the (3,1) chain). Cap
  `d_t≤1` supplied separately by B-AXIS / Cluster 1 ⇒ `d_t=1`, signature (3,1).

Conditional derivation the runner verifies, end to end:
```text
(i) Y_like gauged => LH gauge anomalies (Tr[Y^3]=-16/9, Tr[SU3^2 Y]=1/3, SU3^3=2)
    are inconsistencies => completion MANDATORY.
(ii) opposite-chirality RH template => CHIRAL (not vector-like mirror) =>
     2nd chirality class; banked SHIFT closed form cancels all six exactly =>
     [EVEN Clifford theorem] d_s+d_t even => (d_s=3) d_t ODD >= 1.
intersect single-clock cap d_t<=1 => d_t=1, signature (3,1).
```

**Falsification:** F1 wrong `Y_{νR}` fails; F2 `e_R↔ν_R` only other consistent
branch (convention, not axiom); F3 vector-like mirror inert (chirality must be
stipulated).

---

## Status discipline / policy

- `hypothetical_axiom_status: conditional on accepted new axiom; not retained.`
- No bare `retained`/`promoted`; no audit verdict; nothing added to
  `axiom_premise_nodes.json`.
- Conforms to `AXIOM_MINIMALITY_POLICY.md` §1/§4/§6: recorded as an **unmade
  science-level decision** awaiting owner approval. The proposal is FOR the
  owner's governance decision.

---

## Skeptical re-attack outcome (one line)

Both the is-gauged predicate (P-HY) and the chiral RH-template existence
(P-COMP) survive a genuine no-new-axiom re-attack: the four gauging
discriminators are blind, and every native completion is vector-like (block02's
CPT-mirror/Hamming-odd traps), so neither cracks — the minimal PIN-GAUGE-CONTENT
primitive (gauged `Y_like` + stipulated opposite-chirality RH template) is the
weakest sufficient addition, and conditional on it the full banked ABJ arithmetic
discharges and the (3,1) lower bound follows.
