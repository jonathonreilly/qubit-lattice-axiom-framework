# /framework-refresher — Orient Before Physics Work

Run this orientation before any derivation, hypothesis, experiment design,
analysis, review prep, or science write-up in this repo. Do not work from
memory of the framework: the axiom set, the primitive registry, and claim
statuses all change; only current repo surfaces are authoritative.

## Required Reads (in order)

1. The current minimal-axioms memo. Resolve it through
   `docs/audit/data/axiom_premise_nodes.json` → `minimal_axioms.current_path`
   (currently `docs/MINIMAL_AXIOMS_2026-06-29.md`) so a re-dated memo cannot
   leave you on a stale axiom set.
2. `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, then the
   registry `docs/audit/data/axiom_premise_nodes.json` and each approved
   primitive's source note.
3. `docs/audit/data/tier_a_admissions.json` — the only accepted non-axiom
   premises; they bound otherwise-retained rows until retired.
4. `docs/repo/CONTROLLED_VOCABULARY.md` — status taxonomy, claim-strength
   labels, science naming rules, filename taxonomy. Skim the sections
   relevant to the task.
5. `docs/audit/README.md` — the propose/ratify split: what authors may
   write versus what only the independent audit lane may write.
6. For the specific lane: the relevant notes and runners, plus
   `docs/repo/LANE_REGISTRY.yaml` and `docs/repo/ACTIVE_REVIEW_QUEUE.md`.

## The Four Axioms (use the names, not letter codes)

- **Lattice** — physical sites are the points of the cubic lattice `Z^3`,
  with nearest-neighbor adjacency, standard translations, and proper cubic
  rotations.
- **Qubit** — each site has a domain of local possibilities; the full one-site
  possibility domain has algebraic presentation `M_2(ℂ)`, with `Cl(3,0)` as
  equivalent real-algebra notation only.
- **Admissibility** — one fixed nearest-neighbor admissibility rule, covariant
  under lattice translations and proper cubic rotations; for each site, the
  available possibilities are determined by, and vary with, the
  nearest-neighbor conditions.
- **Record** — a record locks exactly one available local possibility; only
  records are readable, and scalar readout is finitely additive over finite
  pairwise-disjoint record collections.

The minimal-axioms memo states explicitly what the axiom baseline does NOT
supply (dynamics, Born rule, readout context, species identification, gauge
group, time metric, unit conversion, ...). Treat those exclusion lists as
binding: anything on them enters only through a named derivation lane with
retained status, an approved primitive, or an explicit Tier-A admission.

## Standing Discipline

- **No new axioms, no new primitives, no new imports** without explicit user
  approval. A route whose closure requires one is infeasible as stated. The
  legitimate import-bearing shape is: explicit named import with a narrow
  role → bounded result → import-retirement audit queued.
- **The ledger is authoritative.** Before citing or building on any result
  as retained-grade, check its `effective_status` in
  `docs/audit/data/audit_ledger.json` on `origin/main` (retained-grade =
  `retained`, `retained_bounded`, `retained_no_go`). In-file `Status:`
  headers and session memory go stale. Use `/ledger`.
- **Author-side status vocabulary only.** Never write bare `retained` /
  `promoted` in Status lines; use `proposed_retained` / `proposed_promoted` /
  `support` / `bounded` / `open`. `audit_status` and `effective_status` are
  set only by the independent audit lane on `main`.
- **Comparator rule.** Established physics (QM/QFT/GR results, PDG values,
  literature) may name a target or serve as a disclosed comparator; it must
  never be a step in a derivation.
- **Negative claims need the gate.** Run `/no-go-gate` (N1–N8) before
  shipping any no-go, stretch-attempt-negative, or walls-naming bounded
  claim. Do not re-open a prior no-go route without naming a new premise.
- **Landing shape.** Science lands as one source note (`docs/`) + one runner
  (`scripts/`) + one cached output (`logs/runner-cache/`) per coherent claim,
  on a dedicated science branch off `origin/main`, via PR, with
  `/review-loop` as the pre-landing gate. Never push science to `main`.
  `.claude/science/` holds branch-local working state only — the citation
  graph scans `docs/` exclusively.
- **Do not audit.** The independent audit lane is operated separately from
  authoring sessions (see `docs/audit/FRESH_LOOK_REQUIREMENTS.md`). Never run
  the audit loop, write audit verdicts, or edit generated audit surfaces.
- **Isolated worktrees.** When other sessions may be active, do science work
  in a dedicated git worktree, not the shared checkout.

## Output

Confirm in one short block: current axiom memo path read, approved primitives
list, any Tier-A admissions relevant to the task, and the lane surfaces read.
Then proceed to the actual task.
