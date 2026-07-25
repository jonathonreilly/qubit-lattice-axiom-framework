# Route Portfolio and Prior-Art Sweep Record

Workflow step 2 of the physics-loop skill (the prior-art sweep) landed on
`main` mid-campaign as PR #5611 at `ab6e6bd8d9`. This campaign began under the
prior version. The sweeps below were performed for every cycle; the searched
commit, commands, hits, and classifications are recorded here as the landed
step now requires. Cycles 697 and 698 were swept before their PRs were opened
but their command records were reconstructed here after #5611 landed; cycle 699
was swept in the landed format from the start.

## Cycle 699 — content pair-kernel channel census

**Searched commit:** `ab6e6bd8d96fb5b7f1fe6712a7bb426c8df1c1e1`
(refreshed with `git fetch origin main:refs/remotes/origin/main` immediately
before the sweep; `git rev-parse origin/main`).

Target statement searched for: *the number of nearest-neighbour two-body
couplings between qubit contents that lattice covariance permits, and an
explicit basis for them.*

| # | command | hits | classification |
|---|---|---|---|
| S1 | `git grep -n -iE "(two.body.*(coupling\|census\|count)\|(coupling\|census).*two.body)" origin/main -- 'docs/*.md'` | `INTERACTION_ASYMMETRY_DELTA_OCCUPATION_CURVATURE_TWO_BODY_STRUCTURE_THEOREM_NOTE_2026-06-06.md` | **nonmatching.** Defines `delta` as carried by a connected two-body coupling in a dynamics/occupation-curvature setting and proves `delta = 0` iff no two-body coupling. It does not count covariance-permitted kernels and has no lattice-covariance classification. |
| S2 | `git grep -n -iE "spin.spin\|dzyaloshinskii\|antisymmetric exchange\|pseudo.dipolar" origin/main -- 'docs/*.md'` | one incidental hit in an A3 review note listing unrelated literature terms | **context-only.** |
| S3 | `git grep -n -iE "burnside\|character average\|molien\|invariant dimension" origin/main -- 'docs/*.md'` | `ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md`, `ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_..._2026-07-03.md`, `BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28.md`, `BRANNEN_DELTA_SPECTRAL_ASYMMETRY_...` | **method-only for three** (Burnside/Molien used as standard machinery on unrelated objects: `C_3` invariant dimensions, irrep dimension sums). The admissibility note is **adjacent** — see below. |
| S4 | `git grep -n -iE "(proper rotation\|det.*\+1).*(chiral\|antisymmetric)\|chiral.*proper rotation" origin/main -- 'docs/*.md'` | chirality/proper-rotation discussion in the 2026-07-14 review-feedback family and `KOIDE_X_BAE_PAULI_ANTISYMMETRIZATION_...` | **nonmatching.** These concern whether proper rotations identify mirror hands for law/domain placement, not invariance of a two-body coupling form. |
| S5 | `git ls-tree -r --name-only origin/main -- docs/ \| grep -iE "PAIR_KERNEL\|COUPLING_CENSUS\|TWO_BODY.*KERNEL\|CHANNEL_CENSUS"` | none | absence of a titled result. |
| S6 | `git grep -n -iE "pair kernel\|two.body kernel\|coupling census" origin/main -- docs/audit/data/derivation_obligations.json 'docs/audit/data/ledger/*/*.json'` | `post_record_persistent_record_production_bridge_prototype_2026-06-06`, `read_reset_cadence_interference_channel_bounded_theorem_note_2026-07-17` | **nonmatching.** Both use "pair kernel" for unrelated objects (record-production target fibers; squared-modulus read/reset kernels). |
| S7 | `git grep -n -iE "(kernel.*octahedral\|octahedral.*kernel\|covarian.*coupling count\|coupling count.*covarian)" origin/main -- 'docs/*.md'` | one hyperoctahedral remark in `KCPT_D2_COMMUTANT_...2026-07-25.md` | **context-only.** |
| S8 | `git grep -n -iE "six (face\|axis) direction.*(invariant\|coupling)\|(invariant\|coupling).*six (face\|axis) direction" origin/main -- 'docs/*.md'` | none | absence. |

### The adjacent hit, read in full

`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`
(bounded_theorem) asks the *same question shape* — when does proper cubic
covariance extend to full cubic covariance on the six nearest-neighbour
directions, and what is the minimal chiral channel — and uses Burnside orbit
counts as cross-checks.

It is not the same result. Its object is the **admissibility rule**, modelled
as colorings of the six directions by a `k`-letter condition alphabet, with
improper elements acting **complex-antilinearly** on rule values, re-earned
from the `Cl(3,0)` presentation. Cycle 699's object is a **two-body readout
kernel**, a trilinear form on (six displacements) x C x C with
`C = span_R{I, sigma_1, sigma_2, sigma_3}`, and its counterfactual uses the
standard **axial** action. Its answer is a condition-value threshold
(`k = 3`, one chiral pair); cycle 699's answer is a coupling census
(96 -> 6 -> 5) with an exhibited basis.

**Disposition:** cited in the cycle 699 note, with the difference in object and
in improper-action convention stated, and with explicit deference to that note
as the owner of the framework's principled improper-action question.

**Target state:** not already proven, not already refuted. Proceed.

## Cycle 697 — REJECTED AS SUBMITTED, abstract core salvaged and landed

Recorded for completeness. Review-loop rejected PR #5620 as submitted and
landed only the abstract kernel classification, as
`PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md`
(`a89337f0bd`). The rejected parts were the position-blindness and
"dimensionless" claims and the admissibility step of the duplication argument.
The sweep below is kept as the record of what was searched.

### Original sweep

Swept before the PR at `origin/main` `1f4e053d87`/`cf8e85dc1c`. Searches, all
over `docs/*.md`, on the statement rather than the lane:

- `"only (local|nearest.neighbou?r).{0,40}(operator|kernel|law)"`,
  `"laplacian is (the only|uniquely|forced)"`, `"forced.{0,20}laplacian"` —
  **no hits**, so no landed derivation of the law's form from covariance.
- `"octahedral orbit|cubic rotation orbit|orbit.invariant kernel"` — one hit in
  a review-feedback tournament note; context-only.
- `"position.blind|site.blind|content.only readout"` — hits are the readout
  bridge family and cycle 693; read and classified as nonmatching (none states
  position-blindness of Record readouts).
- `"stencil|two.parameter (family|operator)|span\{?I, ?(Delta|Laplacian)"` —
  the significant hit is
  `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`,
  which **imports** the graph-Laplacian Green's-function identification as
  accepted-premise packet P1. **Adjacent, and cited in the value gate**: it is
  the surface cycle 697 narrows, not a prior derivation of it.

**Target state:** not already proven. Proceed. Later, the review seat on
PR #5620 independently surfaced
`CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md`; it was read
and classified as the standard-math analogue (Reynolds projector for the `D_4`
stabilizer of a *selected* forward direction) and is now cited in cycle 698.

## Cycle 698 — pair kernel as the minimal position-carrying extension

Swept before the PR. Searches over `docs/*.md`:

- `"two.body readout|pair kernel|k.body|cluster expansion|many.body readout"` —
  hits across the Wilson/staggered and beta6 families; all read as
  nonmatching (polymer/cluster expansions in a lattice-gauge context, not
  readout classification).
- `"additivity (forbids|excludes|rules out)|no (two.body|pair|joint) (term|dependence)"` —
  one hit,
  `BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`;
  read and classified **nonmatching** (effect-partition gradings and the Born
  trace form, not record-collection additivity).
- `"irreducibly two.body|two.body mediator"` — the `DELTA_SIGN` /
  `INTERACTION_ASYMMETRY` family; nonmatching as in S1 above.
- `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md`
  read in full: an `open_gate` admission candidate proposing a Grassmann source
  action with `W` additivity on independent blocks. **Adjacent in spirit,
  nonmatching in object** — it proposes adopting an action; cycle 698
  classifies what covariance permits without adopting one.

**Target state:** not already proven. Proceed.

## Ranked routes still open

See `OPPORTUNITY_QUEUE.md`. The named successors after 699 are the
site-anchored readout derivation, the reference-normalization selection, and
T4a's `L^-1 = G_0`, in that order of leverage.
