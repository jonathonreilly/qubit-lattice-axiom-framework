# Decision record — the admissibility-induced-law campaign, blocks 01–34 (2026-09-18)

A one-page statement of what the campaign has established about the fourth axiom's reading, written for the owner's integration and for the axiom decision. Everything below is a proposal; nothing is adopted or retained by this record. Blocks 01–07 are on `main` by the owner's own commits; blocks 08–34 are open hand-off PRs (`#8138`–`#8178`), each an exact runner with a mutation census, controls and a refuting pass. PR numbers are evidence addresses only.

## 1. The question and the answer

The axioms say "records form" and "only records are readable" with one covariant nearest-neighbour rule. Two readings were on the table: the **static** reading (the rule is the full conditional of one joint law on the lattice) and the **formation** reading (records are laid down one after another, each drawn from the rule given the records already present). The campaign's answer, exact and executed at every step:

1. **The readings are different laws.** On every finite window that contains a cycle the formation law is not the static law (block 01), the static law is not even a mixture of formation laws over orders (block 16, `#8150`: a one-record flip raises every order's weight), and on `Z³` the monotone formation law differs from every static Gibbs law (block 09, `#8139`).
2. **Every formation law is Gibbs, with the recorded-set graph as its Markov graph** (block 10, `#8141`); it is nearest-neighbour Markov iff no site records two neighbours; its potential carries irreducible `k`-body terms up to `k = 6`; the monotone `Z³` law has a three-body term (block 08, `#8138`) that vanishes at exactly six exceptional weight points and nowhere else (block 11, `#8142`).
3. **The formation reading does not fix one law by itself.** The order in which records form is a free datum: the monotone class gives one law (block 05), other orders give others, and no covariant *rate* law — value-blind or value-dependent — reproduces the static law on the plaquette (block 14, `#8148`); "joint" formation of a unit equals sequential formation iff no site of the unit records an inside neighbour with a second (block 15, `#8149`). **A clause is needed**: the campaign recorded three exact candidates — a formation-rate clause (block 14), a formation-unit clause (block 15), and an unrecorded-site clause (block 24, `#8158`: the free-window and integrated-exterior readings agree iff every unrecorded component is pendant). Each comes with the plaquette or a `2 × 2` window as its exact witness. None is adopted.
4. **The menu decides memory for the formation reading; the reading decides memory for the sphere menu.** With the six-axis (soldered) menu the formation law keeps a plane of identical records at strong preference (blocks 25, 30: proved; block 28: located). With the sphere (unsoldered) menu the formation law loses its plane at every coupling run (block 26, `#8170`, executed; the linear theory exact), while the sphere static law orders (blocks 19, 22). So on the sphere menu the two readings differ in whether memory exists at all.
5. **Where the gravity node's kernel lives.** The Green-function kernel of the gravity lane is the transverse channel of the *ordered unsoldered static law* (block 19, `#8153`; block 29, `#8173` measured its normalization at `0.9–1.0` of the infrared bound), absent in the discrete-menu and causal-Gaussian objects (blocks 13, 17) and absent on planes (blocks 20, 23). That channel exists only under the static reading with the sphere menu on `Z³` and at strong coupling.

## 2. Proved regions against located strengths (block 28's map)

| law | proved | located |
|---|---|---|
| six-axis static, orders on `Z²` and `Z³` | `p ≥ 216·max(q, r)` (block 17) | `p ∈ (3.6, 3.7)` at `(p, 1, 2)` |
| six-axis formation, keeps its plane | `p ≥ 4165` at `(p, 1, 2)` (block 30; 2085, 8330, 6247 on the other lines) | `p ∈ (10.5, 11)` |
| six-axis formation, unique with exponential decay | `3c < 1`, containing the silent triples (block 08) | — |
| sphere static, orders on `Z³` | `β > 76/100` (blocks 19, 22); unique for `β < √3/6` (block 21) | `β ∈ (0.66, 0.72)` |
| sphere formation | unique with exponential loss of memory for `β < 1/√3` (block 27); never keeps its plane (executed, block 26); torus memory time `3βL²/A(3β)` exact (block 34) | no ordered phase found |

The six-axis formation gap (`4165` against `11`) is understood: the tree route is floored at `p = 368` (block 32), its best case is `p ≥ 453` pending one local lemma (block 33), and anything below needs a count that is not a union bound. Further threshold work is a research program, not a block.

## 3. Recommendations (proposals to the owner)

- **Integration order.** Blocks 13–34 are independent PRs against `main` and can land in any order; blocks 08–12 are a stack (`#8138 → #8139 → #8141 → #8142 → #8146`) and land in that order. Each note restates what it uses from open PRs as declared objects, so no note depends on another's landing.
- **The axiom decision.** The reading question is decided by the theorems above: the formation reading is a different theory from the static one, and it needs one clause (rate or unit) to be a theory at all. The plaquette witnesses of blocks 14 and 15 are the smallest cases on which any candidate clause can be tested, and block 24's pendant condition is the natural statement for unrecorded sites. A clause is an axiom change and is the owner's.
- **What the campaign would not spend more on.** The six-axis threshold (capped route), and simulations of the sphere formation law beyond the torus result. **What is worth a proof if capacity returns:** the tight-sibling lemma (`p ≥ 453`), spin-wave theory for the sphere formation law with the measured `1/|m|²` factor as target, and the infinite-plane loss of memory.

## 4. Where everything is

Pack `.claude/science/physics-loops/admissibility-induced-law-20260906/`: `RESULTS_blockNN.md`, `CHECKER_blockNN_findings.md`, `CLAIM_STATUS_CERTIFICATE_blockNN.md`, `GOAL_blockNN.md` per block on its branch; the shared `HANDOFF.md`, `STATE.yaml`, `OPPORTUNITY_QUEUE.md`, `APPROACH_REGISTRY.md`, `NO_GO_LEDGER.md`, `TRACE_GATE.md` carry each block's appends on its branch. Runners under `scripts/`, notes under `docs/`, pinned stdout under `logs/runner-cache/`.
