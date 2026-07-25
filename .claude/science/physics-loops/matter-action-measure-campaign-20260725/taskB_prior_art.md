# TASK B — prior-art and adjacent-lane sweep: common vs independent onsite frames

**Date:** 2026-07-25. **Swept against `origin/main`** (`git fetch` run first;
tip at sweep time `4097451e9a`). All `file:line` anchors below are line numbers
**in the `origin/main` blob**, read via `git show origin/main:<path>` — not the
local worktree, which diverges from `origin/main` by 1307 files.

**No repo file was modified.** This report file is the only write. No commit,
no push, no PR. No audit verdict is set or predicted anywhere below; every
status quoted is read from `docs/audit/data/ledger/` shards on `origin/main`.

---

## 0. Framework surfaces read (mandatory refresher — declared)

| surface | read | what I took from it |
|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | in full (194 lines) | Lattice `:35-42`, Qubit `:43-53`, Admissibility `:55-61`, Record `:63-72`, Qualification `:74-79`, no-dynamics `:103-118`, open gates `:156-173` |
| `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` | in full | 3 approved primitives: `scale_reference`, `kinetic_isotropy`, `realized_state`. **None** touches frames, transport, or cross-site identification |
| `docs/audit/data/axiom_premise_nodes.json` | in full | `canonical_ids` = 4 only. The `minimal_axioms` note text ends: still supplies no "…source/action bridge, physical observable bridge, state-selection rule, law-domain derivation, **law-level dependence on an unfixed choice**…" |
| `docs/COMMON_FRAME_PAIR_GENERATOR_…_NOTE_2026-07-25.md` (PR #5602 head, **not on `origin/main`**) | in full | H1–H4, R1–R4, L1–L3, N1–N8 |
| campaign `CAMPAIGN.md` | in full | Waves 0–2 |

**The two axiom sentences this question turns on, verbatim:**

- Lattice, `MINIMAL_AXIOMS_2026-06-29.md:41-42`:
  > "No site is privileged. Sites are distinguished by the supplied lattice structure alone."
- Qubit, `MINIMAL_AXIOMS_2026-06-29.md:47-53`:
  > "The full one-site possibility domain has algebraic presentation `M_2(C)`. … No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone."

Neither sentence names an action of anything on the one-site algebra, and
neither names a map between the algebras at two different sites. The Qubit
axiom is a statement about **one** site, quantified over sites.

---

## 1. HEADLINE — the question is ALREADY ANSWERED, twice, in the same direction, and PR #5602's L1 states the opposite polarity

### 1a. The answer, from a landed `docs/` bounded theorem

`docs/COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md:73-81`
— **live ledger `effective_status = unaudited`, `bounded_theorem`, crit=medium**:

> "the intrinsic exchange of labeled factors is the flip isomorphism `C^2_x tensor C^2_y -> C^2_y tensor C^2_x`. **Realizing it as an operator `S` ON `C^2_x tensor C^2_y` requires an identification of the two site domains. The Qubit axiom itself supplies that identification:** both domains carry the same supplied algebraic presentation (`M_2(C)`), and 'Possibilities are distinguished by the supplied algebraic structure alone.' Relative to this shared presentation, `S` is fixed with no spatial axis, midpoint rotation, orientation, or additional convention"

and, three paragraphs later, `:96-101`:

> "**Frame-relativity (load-bearing honesty):** an INDEPENDENT per-site presentation change (`g tensor 1`) does not commute with `S` and moves the split; the runner exhibits this. The split is canonical relative to the shared presentation, and **its stability group is the diagonal**. Comparing presentations across sites is exactly the transport question left to later blocks; nothing here supplies it."

and it is registered as an open residual, `:198`:

> "**R5 frame transport:** the T1 frame-relativity exhibit shows independent per-site presentation changes move the split; **a rule for comparing presentations across sites (transport) is not supplied by anything in this note — open.**"

**This is exactly Task B's question, named, exhibited with a runner, and
registered as residual R5, nineteen days before this campaign opened.** Its
verdict: the *shared presentation* is read as supplied by the Qubit axiom, the
*comparison of presentations across sites* is not supplied, and the stability
group of the exchange split is the diagonal (= common frame).

Its sequel `docs/COLOR_COMPOSITION_RULE_MATTER_BILINEAR_POLAR_TRANSPORT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md:112`
(**`effective_status = audited_conditional`** — the only audited row in this
whole cluster) explicitly declines to close it:

> "this proves a DIFFERENT conditional frame-transport lemma — for supplied `C^3` color carriers — **not the comparison of qubit-domain presentations across sites that R5 concerns**. The relation between the two is open; R5 is not addressed, not closed."

### 1b. The answer, from `work_history` (excluded from the pipeline)

`docs/work_history/repo/review_feedback/FOUNDATION_LICENSED_PHYSICAL_EQUIVALENCE_WEYL_PAIR_NOTE_2026-07-14.md:21-34`
— **no claim id, no ledger row, `**Authority:** none` at `:8`**:

> "The current foundation does **not** supply one universal physical-equivalence group. It supplies one exact spatial covariance group, `G_found = Z^3 semidirect O_cubic^+` … It also makes the presentation of a one-site `M_2(C)` algebra nonprivileged. **The narrow safe re-presentation is a common complex-linear star-automorphism — an inner `PU(2)` conjugation — applied to the complete rule, record content, and decoder. Neither statement licenses arbitrary site-dependent quantum frames**, reflections, antiunitary conjugations, boundary changes, or a quotient over experimental protocols."

with a dedicated section `### Common versus site-dependent frames` at `:198`,
whose core is `:204-216`:

> "An arbitrary family `U_x` is different. It changes neighbor comparisons by the relative frame `U_x^dagger U_y`. **A particular gauge/connection law may make those changes redundant, but the foundation does not supply that law.** The runner's two-site control shows the distinction exactly: common conjugation preserves the isotropic Pauli relation `sigma_x tensor sigma_x + sigma_y tensor sigma_y + sigma_z tensor sigma_z`, whereas conjugating only one endpoint changes it. **This is a counterexample to automatic local-frame gauge status**, not a claim that local gauge theories cannot be derived."

and it explicitly disclaims the converse at `:708`:

> "**Not claimed:** … that no local gauge/connection law can derive site-dependent frames"

### 1c. Why this matters: it INVERTS PR #5602's L1

PR #5602 L1 (note body, "L1 — common-frame covariance is a PREMISE that
CREATES the two-point menu") reads the common-frame choice as the *extra*
import:

> "Adopting the exchange class therefore imports a physical premise; it does not read one off a symmetry slogan."

Both prior-art answers put the extra import on the **other** side:

- the common `PU(2)` re-presentation is the **narrow safe** reading of "no
  possibility is privileged" (`WEYL_PAIR:29-31`);
- **independent** site-dependent frames are the reading that is *not licensed*
  and that would need a further supplied gauge/connection law
  (`WEYL_PAIR:32-34`, `:204-206`);
- the shared presentation is read as supplied by the Qubit axiom itself
  (`COLOR_ARENA:76-78`), with only the *transport* left open (`:198`).

The middle position — the one PR #5602 actually states in its own body at
`L1` and which the exploratory source states first — is
`docs/work_history/repo/review_feedback/QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:39-50`:

> "'No possibility is privileged' does not itself say whether local basis changes act together or independently. … Under **common-basis covariance**, the invariant algebra is the two-dimensional span of identity and SWAP … Under **independent onsite covariance**, the commutant is only the identity, so no nontrivial pair interaction survives without a connection, shared frame, link variable, or symmetry reduction. **The current Qubit prose supplies neither interpretation as a dynamical law.** Promoting the exchange result without choosing and defending the covariance meaning would hide a new physical premise in a symmetry slogan."

**So the corpus already carries three mutually inconsistent readings of the
same axiom sentence, none of them audited.** That inconsistency, not the
commutant, is the finding.

### 1d. The distinction that reconciles them, and which no surface states

`WEYL_PAIR:200-202` licenses a common `PU(2)` conjugation **"applied to the
complete rule, record content, and decoder"** — it "changes notation, not the
represented relations." A transformation applied to *everything* is a
relabeling and constrains `h` not at all. The commutant condition
`[h, u ⊗ u] = 0` is a **different, strictly stronger demand**: that the law be
the *same function* in every presentation while the rest is held fixed. No
surface in the corpus derives the second from the first. That gap is the live
physics, and PR #5602's own `N6(1)` names it:

> "(1) Test whether the common-frame reading is forced by, or merely compatible with, the Admissibility covariance sentence."

The Admissibility sentence itself has been adjudicated and gives **no** help:
`COLOR_ARENA:107-123` (T2) concludes Admissibility "claims cross-site
DEPENDENCE at axiom strength, **not a cross-site OBJECT**", with an explicit
typing disclaimer that the axiom does not type "conditions". The one surface
that words Admissibility as transport-like is a methodology file, not a physics
authority: `docs/ai_methodology/skills/review-loop/SKILL.md:126` — "Admissibility
is one fixed finite-neighborhood rule, **the same at every lattice translate**".
"The same at every translate" presupposes a translation action on the internal
domain; the Lattice axiom names translations on **sites** only
(`MINIMAL_AXIOMS_2026-06-29.md:37-38`). Flagged as an unexplored route, not a
result.

---

## 2. (a)+(b) FULL HIT TABLE — every hit, with `file:line` and LIVE ledger status

Statuses are `effective_status` read from `docs/audit/data/ledger/<xx>/<claim_id>.json`
on `origin/main`. "no ledger row" is stated where the shard does not exist.

### Tier 1 — directly on the question (frame comparability / common vs independent)

| # | file:line | what it establishes | live status |
|---|---|---|---|
| 1 | `docs/COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md:73-81, 96-101, 198` | SWAP on an edge **needs** an identification of the two site domains; reads the Qubit axiom's "same presentation" as supplying it; exhibits (runner) that `g ⊗ 1` moves the Sym/Anti split; stability group = the diagonal; registers **R5 frame transport: OPEN** | `bounded_theorem` / **unaudited** / crit=medium |
| 2 | `docs/work_history/…/FOUNDATION_LICENSED_PHYSICAL_EQUIVALENCE_WEYL_PAIR_NOTE_2026-07-14.md:21-34, 161-166, 198-216, 704-713` | Foundation licenses `Z^3 ⋊ O_cubic^+` and a **common** `PU(2)` re-presentation only; **does not license site-dependent frames**; two-site control on `XX+YY+ZZ`; foundation names **no homomorphism `O_cubic^+ → PU(2)_onsite`**; disclaims the converse no-go | **no claim id, no ledger row**; `**Authority:** none` (`:8`) |
| 3 | `docs/work_history/…/QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:14-35, 37-50, 52-68` | The three premises; commutant `span{I,SWAP}`; the covariance reading is load-bearing and the Qubit prose "supplies neither interpretation"; `±SWAP` singlet-1 / triplet-3 separator; autonomy is load-bearing | **no ledger row**; `Authority: none` (`:7`) |
| 4 | `docs/work_history/…/RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md:146-152, 171-174, 176-190` | Same commutant under "the same `U in SU(2)` acts on both sites"; "**The common-frame reading is itself physical.** Independent onsite frame covariance would leave only identity unless a shared connection, link, or relational program is supplied"; the `(α>0, βI)` quotient and its active-edge limit | **no ledger row**; `Authority: none` |
| 5 | `docs/work_history/…/EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md:520-527, 1128-1145` | Same dichotomy in one sentence; **and the group statement**: "With the full named net fixed, the **bare group is `PU(2)^n ⋊ S_n`**; a common onsite recoding additionally needs a **homogeneous content dictionary**" | **no ledger row**; `Authority: none` |
| 6 | `docs/work_history/…/EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md:722-728` | Three exact equivalence levels: fixed full named net has **bare group `PU(2)^n ⋊` site permutations**; selected pointer-record algebra has a larger normalizer; transported-net groupoid | **no ledger row**; `Authority: none` |
| 7 | `docs/work_history/…/NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md:628, 809-817` | The **Record**-side route to a common frame: "One content relabeling applies at every site … 'content alone' reading … **Reduces independent onsite frames to common `PU(2)`**", flagged risk "Common-rotation claim is too strong"; N1 route 6 "content-dictionary" and route 8 "fixed-rule" both **ATTEMPTED, not closed** | **no ledger row**; `Authority: none` |
| 8 | `docs/work_history/…/FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md:182-192` | Finite exact count of the fork: 2 sites × 2 possibilities gives 24 bijections, **8** fiber-preserving (independent per-site dictionaries), and "**if the same content dictionary must be used at both sites, only four remain**" — stated as a condition, not derived | **no ledger row**; `Authority: none` |
| 9 | `docs/work_history/…/APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md:127-133` | Consumer-side consequence: "**Independent onsite frame covariance would not transport that frame down the wire without an additional link or connection. The cross-site qubit frame remains an import.**" | **no ledger row**; `Authority: none` |
| 10 | `docs/work_history/…/SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md:150-177` | `h = a I + b SWAP` under "common qubit-frame covariance"; sign of `b` survives; the three-site `H_1 + η H_2` gap-ratio `2 → 1` counterexample (PR #5602's L2) | **no ledger row**; `Authority: none` |
| 11 | `docs/work_history/…/FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md:319` | `commutant(U tensor U) = span{I,SWAP}` | **no ledger row**; `Authority: none` |
| 12 | `docs/COLOR_COMPOSITION_RULE_MATTER_BILINEAR_POLAR_TRANSPORT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md:112` | Explicitly declines to answer R5: its polar transport is for *supplied `C^3` carriers*, "not the comparison of qubit-domain presentations across sites" | `bounded_theorem` / **audited_conditional** / crit=medium |

Prior-art runners already computing this algebra (they exist on `origin/main`):
`scripts/qubit_symmetry_exchange_law_reduction_probe_2026_07_14.py`,
`scripts/relational_qubit_disagreement_canonical_law_escalation_probe_2026_07_14.py`,
`scripts/single_invariant_action_steelman_attack_probe_2026_07_14.py`,
`scripts/full_law_inventory_adversarial_reduction_probe_2026_07_14.py`,
`scripts/foundation_licensed_physical_equivalence_weyl_pair_probe_2026_07_14.py`.
**Zero ledger shards anywhere mention any of these seven `work_history` stems**
(checked by `git grep -il <stem> -- docs/audit/data/ledger/**`, all returned 0).

### Tier 2 — cross-site frame treated as a trivialization/connection (the gauge lane)

| # | file:line | what it establishes | live status |
|---|---|---|---|
| 13 | `docs/FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md:17, 26-28, 83-100, 133-135, 154-159` | **The same question, one level up the carrier stack, answered in the opposite direction.** "the translation bridge's `U=I` reference is **not a canonical physical cross-site frame pinning**"; "Under independent local fibre bases it is rewritten as `g_x g_y^dag`"; "`G H[U=I] G^dag = H[g_x g_y^dag]`"; "The case `U=I` proves that the free translation bridge **chooses the flat trivialization**; it does not prove that the `I` matrix is a local-frame-invariant physical cross-site frame" | `bounded_theorem` / **unaudited** / crit=medium |
| 14 | `docs/MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md:14-37` | With that bridge, "frame-independent nearest-neighbour hopping **uniquely requires a compensating link transporter with the lattice connection law**" — i.e. the framework's canonical response to independent onsite frames is: **supply a connection** | `bounded_theorem` / **unaudited** / crit=high |
| 15 | `docs/LOCAL_FRAME_ORBIT_FLAT_SECTOR_EXACT_CONVERSE_HOLONOMY_FRAME_UNREACHABLE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-06-10.md:8, 31-46, 67` | local-frame orbit of the free Hamiltonian; "the kinematic absolute-frame redundancy"; uncompensated local frames tested | `bounded_theorem` / **unaudited** / crit=medium |
| 16 | `docs/ADM2_GLOBAL_SU3_SYMMETRY_REDUCES_ACTION_FORM_BI_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-08.md:25, 41, 65, 89` | The **ADM-1** gate is named exactly as "the static local-frame gate"; "a **global** rotation is invariant while a **local** one is not"; **ADM-1 not discharged** | `bounded_theorem` / unaudited (row read via cluster; see §4) |
| 17 | `docs/BLOCKING_ISOMETRY_REDUCES_TO_POINTER_FRAME_ADMISSION_NARROW_THEOREM_NOTE_2026-06-09.md:18`; `docs/COLOR_DEPOLARIZATION_ADM2_GATING_…_NOTE_2026-06-09.md:122`; `docs/COLOR_EINSELECTION_MATTER_UNITARY_PRIMITIVITY_…_NOTE_2026-06-09.md:133`; `docs/COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_…_NOTE_2026-06-08.md:93`; `docs/EDGE_TWO_SITE_FRAMING_SUPPLIES_NO_NATIVE_COLOR_ROUTE_…_NOTE_2026-06-08.md:13`; `docs/COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_…_NOTE_2026-06-09.md:140,179`; `docs/EMERGENT_GAUGE_HEAT_KERNEL_CLT_…_NOTE_2026-06-08.md:18`; `docs/ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_…_NOTE_2026-06-08.md:94` | **Eight** landed notes each recording that **ADM-1 (static local colour-frame redundancy) is UNDISCHARGED**. `ST1_ST2:94` states the failure mode precisely: "The force is not a single global adjoint **under independent local frames**" | all `unaudited` where a row exists; `st1_st2_…_2026-06-08` = `bounded_theorem`/**unaudited** |
| 18 | `docs/GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md:29, 118, 164` | The gauge lane's own gate map lists "the current-surface **local-fibre-frame redundancy and link-transporter law**" as `currently unaudited per ledger (kinematic bridge)` | — |

### Tier 3 — surfaces that CONSUME the common-frame reading (the inheritance map for (d))

| # | file:line | how it consumes it | live status |
|---|---|---|---|
| 19 | `docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:196-205, 239-253` | **The campaign's own load-bearing four-axiom countermodel.** `Phi_{x,y} = I - SWAP_{x,y}` is argued axiom-compatible because "Because `SWAP` commutes with **every common one-site frame change `U tensor U`**, the law privileges no one-site possibility or Pauli axis." **The no-privilege discharge is done by the common-frame reading.** Under the independent-onsite reading `SWAP` is not invariant and the discharge would have to be re-argued | `no_go` / **unaudited** / crit=medium |
| 20 | `docs/MINIMAL_RECORD_INSTRUMENT_DILATION_SCALAR_EXCHANGE_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md:4, 33, 159-175, 197-199` | Whole note is built on a "**common-frame-invariant `I-SWAP` branch**"; defines `scalar-exchange` as "invariant under a common one-site frame rotation `G tensor G`" | `bounded_theorem` / **unaudited** / crit=leaf |
| 21 | `docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md:31-47` | Class defined by `SWAP h SWAP = h` (needs the identification) + "Place **the same `h`** on every undirected edge" + "**Up to one uniform onsite basis** taking `N` to `Z`" | `bounded_theorem` / unaudited (cluster) |
| 22 | `.claude/science/physics-loops/staggered-dirac-a1a2-realization-closure-20260710/ROUTE_PORTFOLIO.md:30-38` | The Admissibility countermodel is engineered to be "fixed, neighbor dependent, translation/proper-cubic covariant, and **common-frame covariant**" — common-frame covariance treated as a *checkable constraint* | campaign file, no row |
| 23 | `docs/COLOR_ARENA_…_2026-07-06.md:151-188` (T3a/T3b) | The spatial-singlet obstruction is landed **conditional on** "an identification — qubit generators = spatial axes — that the four axioms do not make" (`:188`) — a second, independent instance of the same class of unsupplied identification | `bounded_theorem` / **unaudited** |

### Tier 4 — the framework's own matter realization runs on the OTHER horn

| # | file:line | what it establishes | live status |
|---|---|---|---|
| 24 | `docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md:72-82, 454` | Kawamoto–Smit absorbing frame is **explicitly site-dependent**: `T(x) = σ₁^{x₁}σ₂^{x₂}σ₃^{x₃}`, "unique up to `T(x) → g(x) T(x) V` (**site-local `U(1)` gauge × one global frame**)"; the whole forcing theorem is stated at "translation+cubic covariance **up to site-local frame**" | `bounded_theorem` / **unaudited** / **crit=critical** |
| 25 | `docs/MATTER_REALIZATION_ARENA_SPLIT_PRESERVATION_UNDER_AXIS_COUPLED_FRAMES_BOUNDED_THEOREM_NOTE_2026-07-06.md:29-39, 131-142, 144-191` | Computes the **relative frame** across an edge, `g_μ(x) := T(x+e_μ)T(x)^{-1} = η_μ(x) σ_μ` — i.e. the staggered lane's cross-site comparison is a **link transporter**, not a common frame. Its EDGE-DIAG condition (`[O,S]=0`) is exactly "the edge coupling is through the relative frame's **diagonal lift** `g_μ^{-1} ⊗ g_μ`". `σ_3 ⊗ I` (one-sided) is **out of class**. `KS-HOP-BRIDGE` left **open** | `bounded_theorem` / **unaudited** / crit=leaf |
| 26 | `docs/ACPHILAMBDA_K1_STAGGERED_K_BLINDNESS_REAL_LIFT_2026-07-02.md:20`; `docs/ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md:20`; `docs/ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md:32` | Three `AC_φλ` notes carry the same premise quote verbatim: covariance "**each up to site-local `U(1)` frame**" | all unaudited |

---

## 3. (c) IS IT ALREADY ANSWERED? — verdict

**Yes for the question as posed, No for the question that actually decides the
campaign.**

**Answered:** "Does the framework supply a canonical cross-site identification
of the qubit domains?" Two independent surfaces answer, and both answer
*supplied-but-narrow*:

1. `COLOR_ARENA:76-78` — the Qubit axiom's shared-`M_2(C)`-presentation
   sentence **is read as supplying** the identification; the *transport*
   (comparing presentations across sites) is **R5, open** (`:198`).
2. `WEYL_PAIR:29-34` — the licensed re-presentation is a **common** `PU(2)`
   conjugation of rule+records+decoder; **arbitrary site-dependent frames are
   not licensed** and would need a gauge/connection law the foundation does
   not supply (`:204-206`).

Neither is retained. Ledger: `COLOR_ARENA` = `bounded_theorem`/**unaudited**;
`WEYL_PAIR` = **no claim id, no ledger row, `Authority: none`**. Consistent
with the campaign's own governance finding, **no foreclosure and no forcing in
this area can be cited as retained authority** (the only `audited_conditional`
row in the cluster, `color_composition_rule_…_2026-07-06`, explicitly declines
the question at `:112`).

**Not answered, anywhere:** the step from *"a common `PU(2)` re-presentation of
the whole description is safe"* to *"the pair generator must commute with
`u ⊗ u`"*. The first is a relabeling of rule + records + decoder together
(`WEYL_PAIR:200-202`: "It changes notation, not the represented relations") and
constrains `h` by nothing. The second holds the rest fixed and is what produces
the two-point menu. **No surface in the corpus derives the second from the
first, or from the Admissibility covariance sentence, or from Record.** The two
attempted routes toward it are both recorded as ATTEMPTED-not-closed in
`NAMED_SITE_RECORD_…:809-817` (route 6 content-dictionary; route 8 fixed-rule),
and PR #5602 lists it as `N6(1)`.

**Therefore: the campaign should NOT spend a wave re-deriving the commutant
dichotomy (11 surfaces + 5 runners already have it, and PR #5602 registers it).
The one unclaimed target is the invariance-vs-covariance step above.**

**A second finding that bites the campaign's framing:** Task B's prompt states
that under independent onsite covariance "NO nontrivial pair law survives at
all — which would be a very sharp negative about the framework reach." The
corpus already shows that horn is **not** where the framework sits. Every
prior-art surface that reaches it says the same thing —
`QUBIT_SYMMETRY:44-46`, `RELATIONAL_QUBIT:171-173`, `APPEND_ONLY:130-133`,
`FIBER_FRAME:83-100`, `MATTER_GAUGE_MINIMAL_COUPLING:14-37` — that under
independent frames a nontrivial law survives **once a connection / link
variable is supplied**, and the framework's own staggered realization
(`MATTER_REALIZATION_ARENA_SPLIT:131-142`) **already supplies exactly such a
transporter**, `g_μ(x) = η_μ(x) σ_μ`. The independent-onsite horn is therefore
not "no law at all"; it is "a law with one more supplied object", which is the
same shape as the gauge lane. The sharp negative, if there is one, is not there.

---

## 4. (d) ADJACENT-LANE DEPENDENCY MAP — who inherits which horn

The framework runs **both horns simultaneously, in different lanes**, and no
surface reconciles them.

**Lane A — consumes the COMMON-frame reading (menu-side).** Each of these
inherits the unsupplied covariance step:

- `STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:200-205`
  — **the campaign's own four-axiom countermodel**. Its no-privilege discharge
  is *literally* "`SWAP` commutes with every common one-site frame change
  `U ⊗ U`". This is the sharpest inheritance: the landed no-go that this
  campaign leans on for "the axioms do not select a nonzero first-order kinetic
  law" is itself standing on the common-frame reading.
- `MINIMAL_RECORD_INSTRUMENT_DILATION_…_2026-07-11.md:4, 159-175`
- `ONSITE_CHARGE_CONSERVING_…_COMMON_HAMILTONIAN_…_2026-07-12.md:31-47`
- `COLOR_ARENA_…_2026-07-06.md:73-101` (T1 arena split; stability group = diagonal)
- `MATTER_REALIZATION_ARENA_SPLIT_…_2026-07-06.md:107-122` (T1 split preservation)
- campaign route file `ROUTE_PORTFOLIO.md:30-38`
- PR #5602 itself (H4)

**Lane B — runs on INDEPENDENT site frames plus a supplied transporter
(connection-side).** These are *not* compatible with a common frame; they need
the transport R5 leaves open:

- **Staggered/Kawamoto–Smit matter, the flagship matter lane.**
  `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_…_2026-06-10.md:78-82` (site-dependent
  `T(x)`, unique up to *site-local* `U(1)` × one global frame; **crit=critical**)
  and `MATTER_REALIZATION_ARENA_SPLIT_…:131-142` (relative frame
  `g_μ(x) = η_μ(x)σ_μ`).
- **The whole `AC_φλ` / K1 cluster**, whose premise quote is "each up to
  site-local `U(1)` frame" (three notes, `:20`/`:32`).
- **The gauge lane.** `FIBER_FRAME_LOCAL_REDUNDANCY_…_2026-06-09.md:83-100`
  ("`I → g_x g_y^dag`"; the flat reference is a *trivialization choice*) →
  `MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_…_2026-06-08.md:14-37`
  (independent local frames **force** a link transporter). The colour campaign
  carries this as the **undischarged ADM-1 gate** across eight notes (row 17).

**Lane C — K/CPT, generation carrier, record readout.**
- **K/CPT:** the frame dependence is *acknowledged and localized*, not hidden.
  `docs/PMNS_TM2_COLUMN_SITE_BASIS_KCPT_PREDICATE_BOUNDED_THEOREM_NOTE_2026-06-07.md:1,18,40,90`
  names the residual "the **site-basis** `K`/CPT real-structure" and states the
  column is "derived **modulo** the site-basis `K`-reality" predicate. The
  2026-07-19→25 KCPT units (`KCPT_*`) work on a fixed finite `D2`/`G_amb`
  surface, not on the qubit site net; I found no cross-site frame dependence
  there. **So K/CPT does not silently presuppose a common frame; it registers a
  site-basis predicate as its named residual.** (Matches the standing memory
  note that K-reality pinning = orbit-indexing + adaptive-equivariance + value
  face.)
- **Generation carrier:** `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:34`
  consumes `PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02` at the **one-site**
  scope only ("the one-qubit local operator algebra carries the Pauli `j=1/2`
  `su(2)` module; **no physical matter-spin identification is consumed**"). That
  row is `positive_theorem` / **unaudited** / **crit=critical**. One-site scope
  ⇒ no cross-site frame dependence. Clean.
- **Record readout:** this is where a *derivation* of the common frame might
  live, and it is **attempted but not closed**.
  `NAMED_SITE_RECORD_…:628` — "One content relabeling applies at every site …
  '**content alone**' reading … Reduces independent onsite frames to common
  `PU(2)`", with its own risk column reading "Common-rotation claim is too
  strong. Compute `Stab(I)` once `I` is specified." Route 6 and route 8 at
  `:809-817` are both ATTEMPTED-not-closed. This is the most promising
  unexplored route in the corpus and it is `Authority: none`.

**Net inheritance statement.** If the common-frame reading is later judged
supplied, then Lane A inherits one shared supplied premise — including the
non-forcing no-go the campaign is building on. If it is judged not supplied,
Lane A's arguments need re-running and Lane B is unaffected (it already pays a
connection). **Either way Lane B's transporter is the framework's *de facto*
answer, and R5 is the gate that has never been closed.**

---

## 5. Native exact rebuild of every algebraic fact I quote as load-bearing

Written to scratchpad only (not a repo runner, no repo file touched):
`/private/tmp/claude-502/…/scratchpad/taskB_check.py`. Exact `sympy`, no floats
as inputs; commutants obtained by **solving** the linear system on a fully
symbolic `4×4` matrix against the `su(2)` generators, not by asserting a basis.

```
PASS G0  SWAP = (II+XX+YY+ZZ)/2                                   [exact]
PASS G1  commutant(u(x)u) complex dim = 2                          (solved: 2 free params)
PASS G2  commutant(u(x)u) = span{I,SWAP}                           (both directions)
PASS G2n negative control: X(x)I is NOT in the commutant
PASS G3  commutant(u(x)v) complex dim = 1                          (solved: 1 free param)
PASS G3b that 1-dim space is C.I
PASS G3c a*I + b*SWAP is independent-onsite invariant iff b = 0
PASS G4  u = (I - iZ)/sqrt(2) is unitary with det 1                (exact SU(2) element)
PASS G4a common u(x)u preserves XX+YY+ZZ                           [WEYL_PAIR:207-214 control]
PASS G4b one-endpoint u(x)I moves XX+YY+ZZ                         [same control, breaking side]
PASS G5  sign(b) = +1 -> ground-sector dimension 1                 (singlet)
PASS G5  sign(b) = -1 -> ground-sector dimension 3                 (triplet)
TOTAL: PASS=12 FAIL=0
```

So the three facts I rely on rhetorically are true as stated: the diagonal
commutant is 2-dimensional and equals `span{I,SWAP}`; the independent-onsite
commutant is the scalars alone, and `aI + bSWAP` survives it only at `b = 0`;
and the `WEYL_PAIR` two-site control separates common from one-sided
conjugation exactly. **None of this is new** — that is the point of this report.

---

## 6. Sweep method (so the next wave can check coverage rather than repeat it)

Swept `origin/main` with `git grep -in` over `docs/**` (8563 files, incl.
`docs/work_history/**` = 479 files), `scripts/**` (5251), `.claude/**`,
`docs/audit/data/ledger/**`. Terms were **mathematical content**, not phrasing:

`commutant` · `Schur` / `Schur-Weyl` · `SWAP` / `-SWAP` / `span{I,SWAP}` ·
`U tensor U` / `U ⊗ U` / `u(x)u` / `diagonal action` / `diagonal SU(2)` ·
`exchange` · `frame` × {`common`, `shared`, `global`, `local`, `site-local`,
`per-site`, `onsite`, `independent`, `redundancy`, `transport`, `comparab`,
`pinning`, `trivializ`} · `cross-site` · `PU(2)` / `Aut(M_2` / `Skolem-Noether` ·
`canonical identification` / `site algebra` / `amalgamat` · `relative
orientation` / `pointer frame` · `content alone` · `both sites` / `same U` /
`one and the same` · `gauge` × `frame` · `Sym^2` / `Anti^2` / `singlet` /
`triplet` · `η`-family / three-site gap ratio · `R5` / `transport residual` /
`ADM-1`.

Grep-forms that would have **missed** the answer, recorded so they are not
re-used: `"I - SWAP"` (prior art writes `-SWAP`), `"common frame"` as a
two-word phrase (the decisive `WEYL_PAIR` section header is
`Common versus site-dependent frames`), and any search restricted to `docs/*.md`
(seven of the twelve Tier-1 hits are under `docs/work_history/repo/review_feedback/`
and none has a claim id or a ledger shard).

---

## 7. Bottom line for the campaign

1. **The question is already answered twice and the answers disagree with
   PR #5602's L1 polarity.** Common `PU(2)` re-presentation is the *narrow safe*
   licensed reading (`WEYL_PAIR:29-34`); the shared presentation is read as
   supplied by the Qubit axiom (`COLOR_ARENA:76-78`); **independent** site-dependent
   frames are the reading the foundation does *not* license and that needs a
   connection law (`WEYL_PAIR:204-206`).
2. **The residual is registered and open: `R5 frame transport`**
   (`COLOR_ARENA:198`), untouched by its own sequel (`COLOR_COMPOSITION_RULE:112`),
   and mirrored in the colour lane as the eight-times-undischarged **ADM-1**.
3. **Nothing here is retained.** `COLOR_ARENA` `unaudited`; `WEYL_PAIR` and the
   six other decisive `work_history` surfaces have **no claim id and no ledger
   row** and say `Authority: none`; zero ledger shards mention any of them.
4. **The genuinely unclaimed target** is the invariance-vs-covariance step —
   why the law must be *invariant* under `u ⊗ u` when the licensed freedom is a
   *simultaneous re-presentation of rule + records + decoder*. Two routes to it
   are recorded ATTEMPTED-not-closed (`NAMED_SITE_RECORD:809-817`, routes 6 and 8),
   the Record `content alone` route being the most promising, and PR #5602 lists
   it as `N6(1)`. That is one wave of work, and it is the only part of this
   question that is not already written down somewhere in the repo.
5. **Third prior-art near-miss avoided.** Wave 1 missed `work_history` 2026-07-14;
   Wave 2 found it but treated L1 as new open physics. L1's *own question* was
   answered in `docs/` on **2026-07-06**, nine days before those surfaces and
   nineteen days before this campaign opened.
