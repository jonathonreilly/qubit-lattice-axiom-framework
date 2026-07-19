---
claim_id: microcausality_finite_range_plaquette_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional extension of the finite-dimensional tensor-product walk-expansion chain to a SUPPLIED carrier decomposition on Z^3. Each declared carrier is a nearest-neighbor bond or unit face and h_S belongs to the carrier algebra A_S; S need not be the operator's minimal support, and all contributions assigned to the same carrier are summed before J is taken. For disjoint observable supports (d >= 1), exact carrier-adjacency counts give D = 52, reach at most 2k, series start ceil(d/2), and the all-time finite-volume bound 2||A||||B||(n_X^S/52) sum_{k>=ceil(d/2)}(104J|t|)^k/k!, with nonsharp readout 208eJ. A finite Z_2 example checks only containment of electric and plaquette operators in declared bond/face carrier algebras. The axioms select no dynamics; no physical gauge-model, transfer-kernel, gauge-measure, continuous-link, infinite-dimensional, longer-range, d=0, or optimal-constant theorem is claimed."
upstream_dependencies:
  - minimal_axioms
  - microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18
  - microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py
---

# Microcausality: Finite-Range Plaquette-Class Walk-Expansion Lieb-Robinson Bound

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; supplied finite-range class (bonds and
unit faces, arbitrary finite site dimensions); the axioms supply no
dynamics; same conventions and declared ODE context as the siblings.
**Audit-status authority:** independent audit lane only. This note sets
no audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py`](../scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.txt`](../logs/runner-cache/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.txt)

## Purpose

This note extends the supplied-Hamiltonian walk-expansion chain of
[`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
from nearest-neighbor bond carriers to declared bond-or-unit-face
carriers on `Z^3`. The proof uses tensor-factor disjointness and the
intersection graph of those carriers. The new work is the exact local
carrier geometry, the diameter-two reach accounting, and finite-dimensional
examples that exercise both bond and face carrier algebras.

The gauge-shaped example below is deliberately only an algebraic class
illustration. It does not identify a physical transfer Hamiltonian, integrate
a gauge measure, control a transfer kernel, or extend the finite-dimensional
argument to continuous-group link Hilbert spaces. No such physical bridge is
an upstream dependency of this theorem.

## Hypotheses (all supplied, none derived)

A finite region `Λ ⊂ Z^3`; each site `x` carries a supplied Hilbert
space of **arbitrary finite dimension** `q_x ≥ 1`; a supplied carrier
family `𝒮 ⊆ {nearest-neighbor bonds} ∪ {unit faces}` over `Λ`; and a
supplied Hamiltonian `H = Σ_{S∈𝒮} h_S`. A label `S` is a declared
geometric carrier, not necessarily the minimal operator support:
`h_S = h_S^* ∈ 𝒜_S`, so identity padding on some factors of `S` is
permitted. This convention intentionally gives a conservative carrier-graph
majorant. All contributions assigned to one carrier are summed into the
single `h_S` before `J = max_S ||h_S||` is taken; no contribution is counted
twice under two carrier labels. At `𝒮 = ∅`, set `J = 0`, `H = 0`, and every
statement is trivial. The theorem is about Hamiltonians supplied with such a
decomposition; it does not assert that this carrier assignment is unique or
minimal. Observables `A`, `B` have disjoint minimal supports `X`, `Y`
(`d = d(X, Y) ≥ 1` as the standing scoping hypothesis; this is a
tensor-product class, so `[A, B] = 0` holds and the clean form is
claimed — no CAR grading is involved anywhere in this note).
Heisenberg convention and the declared finite-matrix ODE context of
the sibling chain, unchanged, including directed time with the
`H → −H` extension (the class is invariant with the same `J`, terms,
and walks). The axioms supply no dynamics (needled); everything is
bridge-conditional. No literature statement is load-bearing.

## Results

**Exact carrier-adjacency geometry (natively enumerated, box-stable).**
Two **distinct** carrier labels are adjacent iff their declared site sets
intersect. On `Z^3`,
enumerated at two box radii and stable:

- bonds incident to one site: `6`; faces containing one site: `12` —
  so `n_X^𝒮 := #{S ∈ 𝒮 : S ∩ X ≠ ∅} ≤ 18·|X|`;
- from a bond: `10` adjacent bonds, `20` adjacent faces (degree `30`);
- from a face: `20` adjacent bonds, `32` adjacent faces (degree `52`);
- per-step degree bound `D = 52`; carrier diameters: bond `1`, face
  `2`.

A mixed length-2 walk count from a single site is `804`, below the
product bound `18·52 = 936` (both gated) — the per-step bound is not
tight, and no tightness is claimed.

**Dilated reach lemma (exact, with a sharpness exhibit).** The declared
carrier of the `k`-th term of a walk lies within distance `2k` of `X`
(induction: each carrier shares a site with its predecessor and has
diameter at most `2`), and the value `2k` is exactly attained at
`k = 1, 2, 3` (enumerated). Hence a walk whose last term touches `Y`
needs `k ≥ ⌈d/2⌉`, and the series below starts there. The dilation is
real, not an artifact: one adjoint step through a face term moves
information distance `2` — gated: for the four-qubit face term
`X⊗X⊗X⊗X`, the single commutator `[H, Z_corner]` already fails to
commute with `Z` at the **opposite** corner (distance 2).

**Chain carry-over.** Every locality input of the sibling chain is
tensor-factor disjointness. Applied to the declared carrier algebras, the
same proved steps are: the
boundary reduction `[H, O] = [H_{∂ supp O}, O]`, the self-drop, the
per-term re-derivation with the reduced generator (self term dropped
before the Jacobi step), the base-term vanishing unless the last term
touches `Y`, and the initial `[A, B] = 0`. The algebra-independent
steps (Jacobi, conjugation, directed-time norm transport with the
`H → −H` extension, iterated integrals, factorial tail, μ-reweighting,
vanishing remainder) are cited to the sibling where they are natively
gated. The walk now lives on the carrier-adjacency graph: first term at
most `n_X^𝒮` choices, each later term at most `D = 52` choices, and
the coefficient identity `(2J)^k · n · 52^{k−1} = (n/52)(104J)^k` is
gated symbolically. Dimension-blindness is not just asserted: the
reduction and the below-cone/arrival instances are gated on a
**mixed-dimension** chain (site dimensions `2, 3, 2`), where nothing
in the chain refers to qubits.

**Theorem (finite-range all-time volume-uniform Lieb-Robinson
bound).** For the supplied class above with `d ≥ 1`, for all `t` and
every finite `Λ`:

> `||[τ_t(A), B]|| ≤ 2||A|| ||B|| (n_X^𝒮/52) Σ_{k≥⌈d/2⌉}
> (104J|t|)^k / k!`
> `≤ 2||A|| ||B|| (n_X^𝒮/52) · ((104J|t|)^{⌈d/2⌉}/⌈d/2⌉!) ·
> e^{104J|t|}`,

with constants depending only on `||A||`, `||B||`, `n_X^𝒮 ≤ 18|X|`,
`J`, `d` — not on `|Λ|` and not on the site dimensions. The
μ-reweighted exponential tail form carries over verbatim (the tail
factor is algebra-independent): `Σ_{k≥⌈d/2⌉} x^k/k! ≤
e^{−μ⌈d/2⌉ + xe^μ}` for every `μ > 0`, giving decay once
`⌈d/2⌉ > e·104J|t|`, i.e. a velocity-type readout `v ≤ 208eJ` in site
units — the factor `2` from the real face-jump dilation, the `104J`
from the crude degree bound. **Neither `104J` (the class activity
scale) nor `208eJ` is claimed sharp**; the bond-only siblings'
constants (`20J`, `20eJ`) remain the sharper statement on the smaller
class, and this note does not modify them.

**Finite-dimensional gauge-shaped carrier example (remark, gated at a `Z_2`
instance).** Assign each lattice-link Hilbert factor to one chosen endpoint
site. For a plaquette, declare the four geometric face sites as its carrier;
for an electric link term, declare the link's geometric bond as its carrier.
The corresponding operators belong to those carrier algebras after explicit
identity padding. These carriers need not be minimal: in the runner's endpoint
assignment the magnetic product has minimal composite-site support on three
face vertices, while the electric operator has minimal support on one endpoint.
The gates check both strict containments and the nonzero commutator; they do
not relabel either minimal support as a theorem output.

Consequently, a **supplied** finite-dimensional discrete-gauge- or
quantum-link-shaped Hamiltonian to which this declared-carrier decomposition
has been assigned is inside the algebraic class after same-carrier terms are
summed. This is representation-dependent, conservative coverage. It is not a
claim that every Kogut-Susskind Hamiltonian has finite-dimensional local
factors, nor a physical-model selection or transfer/measure theorem.

## No-Go Discipline Gate

**Status: PASS after corrected wall count.** This is a
`bounded_with_named_walls` check, not a claim that extensions are impossible.
The collapsed wall set is:

| Wall | Narrow boundary |
|---|---|
| `W_D` | The axioms do not select the supplied Hamiltonian or place a physical model in this carrier class. |
| `W_R` | The displayed constants use carriers of diameter at most `2`; longer-range carriers require new counting. |
| `W_∞` | The declared analysis context has finite-dimensional site algebras; infinite-dimensional link spaces are not covered. |
| `W_0` | The clean displayed form assumes disjoint observable supports, `d ≥ 1`. |
| `W_*` | `104J` and `208eJ` are valid majorants, not optimality results. |

These are scope boundaries and non-claims. They do not say that no separate
theorem can close any wall.

**N1 — alternative attack routes.** Seven distinct attacks on the bounded
claim and its wall count were attempted:

| Attack route | Marker | Evidence and disposition |
|---|---|---|
| Read each `S` as minimal operator support | ATTEMPTED | The `Z_2` construction refutes that reading: its electric and magnetic operators have one- and three-site minimal supports but lie in declared bond and face carrier algebras. The theorem now requires only `h_S ∈ 𝒜_S`, and the runner checks the strict containments. |
| Change carrier orientation or enlarge the enumeration box | ATTEMPTED | Gates G1-G3 enumerate every bond/face orientation at radii `4` and `5`; both give bond degree `30`, face degree `52`. Hand inclusion-exclusion independently gives the face count. |
| Reach farther than two lattice steps in one allowed carrier move | ATTEMPTED | Every allowed carrier has diameter at most `2`; the induction gives reach `2k`, and G6 exhaustively attains but does not exceed `2,4,6` for `k=1,2,3`. A diameter-three carrier would evade this proof and is therefore retained as `W_R`, not declared impossible. |
| Introduce unequal finite site dimensions and look for dimension factors | ATTEMPTED | M1-M4 use dimensions `2,3,2`, including a four-site face operator; the analytic norm/commutator steps use no dimension factor. This does not close `W_∞`. |
| Reverse time and test whether the directed estimate survives | ATTEMPTED | The cited all-time sibling proves `τ_{-t}^{H}=τ_t^{-H}`; the declared carrier class is invariant under `H→-H` with unchanged `J` and graph. |
| Split one carrier contribution into several same-carrier terms to evade `J` | ATTEMPTED | The definition sums all contributions assigned to a carrier before taking `J`, so the path count contains that carrier once and its summed norm is charged once. |
| Extend the clean prefactor to overlapping supports | ATTEMPTED | The cited all-time sibling gives the exact `d=0` counterexample showing that its small carrier-count prefactor need not dominate the initial commutator. This preserves `W_0` without asserting a generic no-go for other bounds. |

**N2 — wall-independence audit.** Closing any one wall does not automatically
close another; the ten pairwise checks leave the collapsed count at five.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---|---|---|
| `W_D/W_R` | no | no | yes |
| `W_D/W_∞` | no | no | yes |
| `W_D/W_0` | no | no | yes |
| `W_D/W_*` | no | no | yes |
| `W_R/W_∞` | no | no | yes |
| `W_R/W_0` | no | no | yes |
| `W_R/W_*` | no | no | yes |
| `W_∞/W_0` | no | no | yes |
| `W_∞/W_*` | no | no | yes |
| `W_0/W_*` | no | no | yes |

For example, a longer-range counting theorem would not select a physical
Hamiltonian or prove sharp constants; a functional-analytic extension would
not alter carrier diameter or the overlapping-support prefactor.

**N3 — hidden-wall phrase scan.** The mandated phrases and close variants
were searched and classified rather than treated as proof:

| Phrase or close variant | Classification |
|---|---|
| “supplied” / “declared finite-matrix ODE context” | Explicit conditions; `W_D` and `W_∞`, not consequences of the axioms. |
| “declared carrier” / “assigned” | Explicit representation convention. Carrier sets may strictly contain minimal support; this is a conservative majorant, not hidden physics. |
| “same proved steps” / “cited sibling” | Cited algebraic dependency for Duhamel, norm transport, and the factorial tail; all new geometry is rechecked here. |
| “volume-uniform” | For each finite `Λ`, the displayed constant omits `|Λ|`; a family statement still requires uniform `J` and local carrier bounds. |
| “gauge-shaped” | Non-load-bearing finite-dimensional class illustration only; no model identification or measure/transfer statement. |
| “sharpness exhibit” | Refers only to attaining carrier reach `2` in one step, not to optimality of `104J` or `208eJ`; `W_*` remains. |

The exact trigger search for “we assume,” “by construction,” “as is standard,”
“the framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical” found no additional
load-bearing condition.

**N4 — residual matching and dependency roles.** No physical-gauge source is
cited as a witness or dependency. The three actual
upstream edges have the following exact roles:

| Witness or dependency | Residual attacked there | Role or residual here | Match? |
|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md:105-118`](MINIMAL_AXIOMS_2026-06-29.md) | Admissibility supplies no Hamiltonian, transfer operator, or dynamics | `W_D`: prevents reading the supplied `H` as axiom-selected | yes |
| [`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md), hypotheses and G1-G7 | supplied bond-carrier Duhamel chain; clean-form `d=0` exclusion | positive chain dependency plus exact witness for `W_0` | yes |
| [`MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md), hypotheses and L1-T3 | supplied finite tensor algebra, commutator support, and norm machinery | representation-level positive dependency; not a negative witness | not applicable |
| Primary runner Z1-Z3 | exact declared-carrier containment in one finite `Z_2` representation | same finite representation only | yes |

No mismatched witness is used to inflate closure support.

**N5 — rhetoric at each resolution.** Broad negative readings are narrowed in
the following resolution audit:

| Phrase | Per element/site | Per mode/block | Finite lattice or class | Untested broader resolution |
|---|---|---|---|---|
| “the axioms supply no dynamics” | Does not deny that a site Hamiltonian may be supplied externally | Does not deny a mode or block generator | Only the foundation's premise inventory is classified | No impossibility of dynamics is claimed at any physical resolution. |
| carriers “need not be minimal” | Exact one-link operator has one-site minimal support | Exact plaquette product occupies three composite sites | The class permits, but does not require, strict padding for any term | No claim that every gauge representation uses this assignment. |
| constants are “not sharp” | No per-carrier optimum is tested | No per-mode or per-block optimum is tested | No class-wide or lattice-wide optimum is tested | The phrase disclaims optimality; it does not assert that improvement is impossible. |
| “volume-uniform” | Local incidence bounds are sitewise | Carrier degrees are orientation-complete | Each finite-volume formula has no `|Λ|`; family reuse needs uniform `J` | No thermodynamic-limit existence theorem is claimed. |
| “not a physical gauge bridge” | Z1-Z3 test only operator containment | No transfer block or gauge mode is constructed | No physical model family or measure is identified | The absence is an artifact-scope statement, not a no-go against future bridges. |

**N6 — primitive, convention, reframe, and partial-closure scan.** The
primitive registry, premise history, controlled vocabulary, and active review
queue were inspected. No new axiom is requested.

| Path | Status | What it closes, and what it does not |
|---|---|---|
| [`docs/audit/data/axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json) and [`premise_decision_history.json`](audit/data/premise_decision_history.json) | approved premise registry/history | `minimal_axioms` supports the foundation boundary; the approved scale, kinetic-isotropy, and realized-state primitives supply no Hamiltonian or carrier decomposition, so they do not close `W_D`. |
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | approved premise node | Classifies dynamics as downstream supplied/derived content; it does not provide this theorem's `H`. |
| This note's declared-carrier definition | explicit convention repair | Reframes the earlier minimal-support ambiguity as honest identity-padded carrier bookkeeping. It closes that semantic defect without new physics and does not identify a physical model. |
| The two cited microcausality siblings | tracked bounded-theorem dependencies; no audit verdict imported | Supply the algebraic walk/norm machinery for finite tensor classes; they do not close `W_D`, `W_R`, `W_∞`, or `W_*`. |
| `docs/repo/CONTROLLED_VOCABULARY.md` | tracked governance authority; non-load-bearing scan target | Supplies existing `bounded_theorem` and scope vocabulary; no labeling-only convention there expands the mathematics. |
| `docs/repo/ACTIVE_REVIEW_QUEUE.md`, conformal-causal source-packet row | live review queue; not a premise or citation-graph dependency | Preserves the need to distinguish one-particle/full-Fock carriers and quasilocal LR composition. It reinforces, rather than closes, `W_D`; no in-flight result is used here. |

**N7 — hostile steelman.** A hostile reviewer can correctly argue that the
endpoint assignment is representation-dependent padding: the `Z_2` gate proves
only that two chosen operators belong to larger bond/face algebras, not that
their minimal supports have those shapes, not that every finite-dimensional
gauge Hamiltonian admits the same useful decomposition, and not that a
continuous-group or transfer Hamiltonian lies in this class. That argument
defeats the earlier “direct support” wording and any universal physical-gauge
reading. It does not defeat the carrier theorem, whose hypotheses now say
exactly `h_S∈𝒜_S` for a supplied decomposition and whose constants intentionally
use the larger carriers. The remark is therefore retained only at that narrow,
representation-dependent algebraic level.

**N8 — cross-cycle echo.** A repo-wide documentation search and a walk of the
physics-loop `NO_GO_LEDGER.md` files found these directly similar walls:

| Earlier wall | Later disposition or mechanism | Application here |
|---|---|---|
| Exact reconstructed `H` was treated as strictly finite range in earlier microcausality work | The [all-time sibling's N8](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md) records a quasilocal reframe | A weighted-carrier theorem could narrow `W_R`; it is not silently imported into this finite-range result. |
| Generic all-time interaction-path counting was treated as absent on early local certificates | Direct Duhamel/interaction-graph proofs retired that generic-mechanism wall | This theorem reuses the proved mechanism and claims novelty only for its explicit bond/face specialization. |
| Exponential LR tails were at risk of being read as exact causal relations | [Conformal-causal no-go ledger, lines 18-28](../.claude/science/physics-loops/conformal-causal-source-repair-block01-20260716/NO_GO_LEDGER.md) preserves that distinction | `208eJ` is only a nonsharp LR readout; no exact causality or physical light speed is claimed. |
| The clean small-prefactor form was at risk of extension to `d=0` | The all-time sibling supplied an exact overlapping-support counterexample | `W_0` is kept explicit; no broader no-go for alternative overlap bounds is inferred. |
| A representation convention was at risk of being mistaken for geometric support | The present repair separates declared carrier from minimal support and checks strict padding | The same convention-reframe mechanism is applied, not dismissed as requiring a new axiom. |

The ledger scan also found the explicit broader non-claim “No quasilocal
Hamiltonian can have a finite LR envelope”; this note likewise makes no such
foreclosure. No retired wall mechanism was omitted from the five-wall count.

## Non-Claims

- Does **not** identify the supplied `H` with a physical gauge or transfer
  Hamiltonian, and does **not** derive a gauge measure, transfer kernel, or
  gauge-field correlation statement.
- Does **not** cover continuous-group infinite-dimensional link Hilbert
  spaces; every site algebra in the declared ODE context is finite-dimensional.
- Does **not** claim `104J` or `208eJ` is sharp, and does **not**
  modify the bond-only siblings' sharper constants on their class.
- Does **not** cover terms of diameter greater than `2`.
- Does **not** cover `d = 0` (inherited clean-form exclusion; the
  sibling's counterexample applies verbatim to this tensor class).
- Does **not** involve CAR grading (tensor class only; the fermionic
  sibling stands separately).
- Does **not** claim novelty or priority over generic interaction-graph
  Lieb-Robinson theorems.
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains
  required.

## Verification

Primary runner:
[`scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py`](../scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py)
— exact throughout. Gate kinds, honestly distinguished: **exhaustive
finite gates** (the carrier-adjacency degrees for **every** bond and face
orientation at two box radii; the reach values at `k = 1, 2, 3`; the
mixed length-2 walk count — finite enumerations over the stated
ranges, with cubic symmetry thereby checked rather than assumed),
**exact representation gates** (the mixed-dimension chain reduction
and cone instances, including a four-site mixed-dimension face term
with its own one-step opposite-corner arrival; the face-jump
sharpness exhibit; the `Z_2` declared-carrier containment instance), and **symbolic
identity gates** (the coefficient assembly; the `⌈d/2⌉` arithmetic in
symbolic even/odd cases with the boundary failure exhibited; the tail
mechanism via binomial domination, supported by an exact partial-sum
instance — the infinite-tail statement itself is the sibling's, cited
where natively gated). The `N`-group gates are **presence needles**:
they pin quoted sentences and structure, and are not correctness
oracles for the quoted content. The enumeration code is written
natively for this runner; no campaign process file, worker transcript, or
future-block packet is executed or cited. The gate
sequence is enforced against an ordered label manifest (drift fails
the run). The runner prints one `PASS`/`FAIL` line per gate and a
final total; the cached transcript is committed at the path in the
header at landing time.
