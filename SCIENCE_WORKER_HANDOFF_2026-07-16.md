# Science Worker Handoff — 2026-07-16

**Audience:** an independent high-capability science worker (Fable-tier with backing
bandwidth) starting fresh on this repo. This document is self-contained: it names the
targets, the context, the constraints, and the delivery mechanics. It lives only on
this handoff branch; it is not repo science and must not be cited by any note.

**Provenance:** produced from a 32-agent full-repo audit run 2026-07-16 (science
deep-reads by domain with adversarial verification of headline claims). The owner has
directed science effort to the targets below. Repo mechanics (front-door repair,
audit-lane retargeting, CI) are being handled in a separate lane — do not work on
those here.

---

## Ground rules (non-negotiable)

1. **Foundation:** the four named axioms in `docs/MINIMAL_AXIOMS_2026-06-29.md`
   (Lattice, Qubit, Admissibility, Record) plus exactly three approved primitives
   registered in `docs/audit/data/axiom_premise_nodes.json`. **No new axioms, no new
   primitives, no new repo-wide vocabulary.** The three open derivation obligations
   carry zero premise weight.
2. **Every math fact is re-proven from primitives by a paired runner script**
   (exact/sympy where possible) with a cached transcript in `logs/runner-cache/`.
   Literature is comparator, never input.
3. **Claim discipline:** notes use canonical claim types (`positive_theorem`,
   `bounded_theorem`, `no_go`, `open_gate`, `decoration`, `meta`). Status prose never
   contains bare `retained`/`promoted` (use `proposed_retained`, `support`, `bounded`,
   `open`). Never prefill audit verdicts. Load-bearing dependencies must be markdown
   links (backticked filenames seed **zero** citation-graph edges). The independent
   audit lane alone sets status.
4. **Negative claims** walk the N1–N8 no-go discipline battery
   (`docs/ai_methodology/skills/no-go-discipline/SKILL.md`) before being called no-gos.
5. **Landing gate (new, owner-ratified direction):** do not accumulate more than ~5
   unlanded blocks in any campaign. Produce → land (via `/review-loop`) → let the
   audit queue see it → then extend. No 40-block stacked towers.
6. **PRs:** one coherent block per PR, branch off current `origin/main`, science
   files only (never `docs/audit/data/` payloads, never generated status surfaces —
   the pipeline validation step is run-and-strip). Follow
   `docs/repo/CONTROLLED_VOCABULARY.md` naming.
7. **Compute safety:** never run full-Brillouin-zone 4D numpy quadratures in
   parallel agents (OOM-crashes this machine). Heavy 4D work runs inline,
   single-process, N≤32.

---

## Target 1 — the Koide grain gate (highest value)

**The single load-bearing question:** does the physical charged-lepton matter
action/measure count the K/CPT orbit **once** (orbit grain → r=1/2 → Q=2/3) or
**per-sector** (sector grain → r=1)? This is the
`ac_orbit_occupancy_statistical_grain_derivation_obligation`
(`docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`).

**State of the art (all July 2026, read these first):**
- `docs/KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_FORCED_VALUE_UNFIXED_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`
  — dial shape forced by C3 + K/CPT antiunitary; the r-value split is NOT forced.
- `docs/ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md`
  — IF orbit grain AND IF strict-sharpening record dynamics THEN r=1/2 is
  rule-class-universal. Read its L1–L3 and N2/N3 sections: those are the two
  undischarged imports you are attacking.
- `docs/KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md`
  — K-ENS weights-face; proves K-closure alone does NOT foreclose doublet
  resolution (a K-even observable W resolves it), so orbit-indexing must come from
  the matter action/measure, not from K-reality alone.

**The two attack surfaces (in priority order):**

**(1a) The grain itself.** Find what, in the framework's own supplied surfaces
(staggered/Dirac corner structure, record-readout additivity, the admissibility
availability rule), forces orbit-counting vs sector-counting in the occupancy
measure — or prove a sharp no-go that nothing on the current supplied surface can
force it (which would make r=1/2 permanently a registered realized-state datum and
close the lane honestly). Either outcome is decisive progress. A useful sharpening:
the K-ENS note already shows the decision cannot come from K-closure of the
observable algebra; enumerate the remaining candidate deciders (action reality
class, measure pushforward under the K/CPT quotient, record-formation locking rule)
and test each exactly on the smallest faithful model.

**(1b) The sharpening import.** The rule-universality theorem assumes record
formation is a majority-sharpening update (its N2 shows non-sharpening dynamics
selects nothing). Either derive strict sharpening from the Record axiom's
permanence/one-record-per-site structure (the current "permanence ⇒ stationarity"
step is a declared reading, not a theorem), or produce the counterexample class and
demote the assumption to a named open input.

**Do NOT re-walk (memorialized refuted paths):**
- det_C "Dyson reality class" reframe — refuted, closed.
- Multiplicative/det-character bridge — structurally foreclosed (C₃ regular rep +
  Schur; not Lindemann).
- Corner fermion-determinant extremum selection of r=1/2 — no-go
  (`docs/CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`).
- Max-record-entropy — sector-blind, cannot derive the dial.
- "chiral → r=1/2" — do not cite; chirality moves only the determinant phase.

**Note:** δ=2/9 is a SEPARATE obligation (R-eta h-class/h-unit readout). Do not
bundle it. If grain work opens a clean line on it, write it as its own block.

---

## Target 2 — cross-sector front-speed alignment (v_fermion = v_gauge)

**Why:** this is the sharpest missing theorem in the emergent-Lorentz story. The
B4 discrete-tick symmetry protects single-species marginal isotropy but **cannot**
protect the relative speed of different sectors (it is a free B4 invariant), and
the framework's own decisive no-go
(`docs/GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md`) shows the
velocity anomalous dimension is 4–16 orders too small to relax anisotropy
radiatively. Without alignment, emergent Lorentz invariance fails at the
multi-sector level regardless of the kinetic-isotropy primitive.

**Read first:**
- `docs/VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md` (names the gap:
  power-divergent drag coefficient f0 does not factorize)
- `docs/VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md`
- `docs/EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`
- `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (scope: the primitive grants
  c_t=c_s structural kinetic-form isotropy ONLY — it is not a cross-sector theorem,
  and the review lane will reject any use of it as one)

**Deliverable shapes that would count as decisive:**
- a custodial mechanism: an exact lattice symmetry or Ward-type identity on the
  supplied gauge+staggered surface that ties the fermion and gauge front speeds
  (compute the object, do not check identities of an assumed form — repo lesson);
- OR a sharp no-go: on the named supplied surface, no local covariant structure
  forces alignment — with N1–N8 walked honestly. That would relocate emergent
  Lorentz to an explicit conditional and is publishable-honest.

**Trap to avoid:** any "unitary-conjugated observable that never reads the
perturbation" construction is a define-away (caught by supervisors before,
2026-06-13). The alignment claim must be read out of an observable that actually
feels the sector-velocity difference.

---

## Target 3 — one uniform RG step (continuum-limit program redirect)

**Context:** the record-faithful-dynamics campaign (47 blocks, now condensed into
PRs #5393–#5397 for review) established finite-volume RP, Dobrushin uniqueness +
OS gap in the heavy-mass/strong-coupling corner, and exactly ONE exact
block-decimation step (`physics-loop` block 24, in PR #5395). Blocks 25–48 tried
to control a second step and fragmented into per-horizon estimates at unphysical
parameters (m up to 1e96, β=0). **Do not extend that tail.**

**The real missing object (named in the campaign's own blocks 24/29 but never
delivered):** a one-step RG bound on a **closed effective-action/polymer space** —
i.e. a norm and an action space S such that the exact factor-two decimation maps
S→S with uniform-in-scale control, so the step can be iterated. Even a heavily
restricted version (free + small gauge coupling perturbation, fixed heavy mass) with
an honest bounded scope would be the first composable rung.

**Two prerequisite clarifications worth their own narrow notes:**
- **Z⁴ vs Z³+tick:** the campaign's OS "time" is a fourth lattice axis; the
  framework ontology is Z³ + emergent tick. A short bounded note pinning exactly
  what identification is being supplied (and that it is an import) would stop the
  campaign name from over-claiming — the audit found this is currently implicit.
- **Axiom→action bridge status:** a `meta`/`open_gate` note stating plainly that
  the Wilson-staggered SU(3) action is a supplied surface, with the (P-FUND-1TICK)
  per-plaquette work as the live route toward licensing it. Related: the
  per-plaquette one-tick-reachability chain is in open PRs (per-plaquette-license
  blocks 02–04, #5275/#5279/#5282) — if you pick this thread up, land those through
  review first; main currently has only stipulated-license support.

**Read first:** `docs/FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md`
(Section 7 G1–G6 gaps), the block-24 note in PR #5395
(`MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md`),
and the block-29 Grassmann polymer norm note in PR #5396.

---

## Target 4 (secondary) — g_bare residue-exhaustion identity

Only if Targets 1–3 stall. The Ward-forcing story for g_bare=1 is blocked by a
self-declared obstruction: a free residue multiplier R(g)=g² survives all cited
constraints
(`docs/G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md`, 2026-06-12/13
obstruction records). Either prove the H_unit tree matrix element exhausts the
complete same-projected 1PI Γ_S⁽⁴⁾ residue (killing the freedom), or write the
sharp no-go. Do not cite g_bare=1 as forced anywhere until this is resolved.

---

## Delivery mechanics

- Branch names: `physics-loop/<target-slug>-block01-YYYYMMDD` (increment blocks).
- Each block = one bounded note + one runner + one cached transcript. Note titles
  use explicit scientific noun phrases (no bare letter-number labels).
- Run `bash docs/audit/scripts/run_pipeline.sh` and
  `python3 docs/audit/scripts/audit_lint.py --strict` as validation before PR;
  strip generated audit outputs from the PR (pipeline is validate-and-strip).
- Open the PR, then run `/review-loop` on it (repo skill:
  `docs/ai_methodology/skills/review-loop/SKILL.md`). Respect the ≤5 unlanded
  blocks gate.
- If a result is negative, it ships as a properly N1–N8'd no-go or open_gate — a
  well-scoped no-go on Target 1a or 2 is a first-class deliverable here, not a
  failure.

Good hunting.
