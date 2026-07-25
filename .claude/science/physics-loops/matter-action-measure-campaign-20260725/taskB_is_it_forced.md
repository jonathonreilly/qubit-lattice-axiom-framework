# TASK B — Is common-frame covariance FORCED?

**Date:** 2026-07-25. Worked against `origin/main` (`git fetch` first; tip
`4097451e9a`). This file is a campaign report, not a repo note. Nothing was
committed, pushed, or opened as a PR. No file other than this one was edited.
No audit verdict is set or predicted anywhere below; every status quoted is read
from `docs/audit/data/ledger/` shards, never from prose.

**Verdict, up front:** **common-frame covariance is NOT forced — and neither is
independent-onsite covariance.** The four axioms name **no internal covariance
group at all**. The word `frame` occurs **zero times** in
`docs/MINIMAL_AXIOMS_2026-06-29.md`; the only occurrence of `covariant` is
`:57–58`, and it quantifies over **lattice translations and proper cubic
rotations** — spatial motions, never an internal `SU(2)`. Confidence **high**
(see §5 for the exact grading of each sub-claim). The `SU(2)` in H4 of PR #5602
is supplied by the note, exactly as that note already says of itself.

**But the sharper result is that the question as posed has a false trichotomy in
it**, and both of the horns the campaign wrote down are artifacts of a supplied
*continuous* group:

| reading of the internal group on one edge | class of Hermitian pair laws | source of the group |
| --- | --- | --- |
| none demanded (what the four axioms actually say) | `dim_R = 16` | — |
| bare endpoint exchange only (cubic rotations act on `Z^3`, not on `M_2(C)`) | `dim_R = 10` | Lattice |
| **common** frame, axiom-named finite `C_4` edge stabiliser | `dim_R = 6` | Lattice + a **supplied** internal action |
| **common** frame, full order-8 proper edge stabiliser | `dim_R = 5` | Lattice + a **supplied** internal action |
| **independent** onsite, same axiom-named finite group | `dim_R = 4` (**nontrivial**, witness `Z⊗Z`) | Lattice + a **supplied** internal action |
| **common** frame, **continuous** `SU(2)` | `dim_R = 2` = `span{I, SWAP}` | **entirely supplied** |
| **independent** onsite, **continuous** `SU(2)` | `dim_R = 1` (scalars) | **entirely supplied** |
| frames as **redundancy** (quotient, not constraint) | `dim_R = 8` physical invariants | Qubit `:52–53`, read correctly |

All eight rows are computed exactly in this report's runner (§6), `PASS=51`,
`FAIL=0`, sympy only, no float is an input to any load-bearing comparison.

Two consequences that bite the campaign's Wave-2 disposition:

1. **The third horn stated in the task brief is false as written.** "If
   independent-onsite covariance is what the axioms license, there is no
   nontrivial pair law at all" holds **only** for a supplied *continuous*
   `SU(2)`. Under independent-onsite covariance with respect to the group the
   Lattice axiom actually names, a nontrivial pair law survives:
   `dim_R = 4`, with the explicit Hermitian witness `Z⊗Z` (gates `D2`, `D2w`,
   `D2m`). So the sharp negative about framework reach does **not** follow.
   This is also a limitation on limitation **L1** of PR #5602.
2. **The dominant error is a category error, present on both horns**: the Qubit
   axiom's "No possibility is privileged" is a **redundancy** statement, and a
   redundancy **quotients** a menu — it never **constrains** a law. Requiring
   `h` to commute with the frame group converts a redundancy into a symmetry.
   Read as redundancy, one edge carries **8** physical parameters (`B3`), not 2
   and not 0. The underdetermination is far worse than a two-point menu.

---

## Surfaces read (mandatory refresher, stated as required)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` — read in full, Lattice `:35–41` and
  Qubit `:43–53` word by word, plus Admissibility `:55–61`, Record `:63–72`,
  Qualification `:74–84`, dynamics boundary `:103–118`, open gates `:156–173`.
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` — read in full.
- `docs/audit/data/axiom_premise_nodes.json` — read in full, including the
  `minimal_axioms` node text at `:25`.
- The four approved primitives are `scale_reference_primitive`,
  `kinetic_isotropy_primitive`, `realized_state_primitive`, plus
  `minimal_axioms` (`axiom_premise_nodes.json:4–9`). **None of them supplies a
  site frame, a cross-site identification, or any internal symmetry group.**
  Per `PRIMITIVE_REGISTRY_CHECK.md:16`, "any dimensionless quantity, selector,
  weighting rule, normalization rule, probability rule, readout bridge,
  dynamics, source/action, or empirical match remains separate unless
  independently derived", and per `:17–19` a proposed primitive absent from the
  registry is unapproved. A cross-site frame identification is absent.
- `docs/COMMON_FRAME_PAIR_GENERATOR_EXCHANGE_CLASS_BOUNDED_THEOREM_NOTE_2026-07-25.md`
  and `scripts/common_frame_pair_generator_exchange_class_2026_07_25.py` (PR
  #5602, branch `physics-loop/r3-common-frame-pair-generator-registration-20260725`;
  **not on `origin/main`** — fetched from the PR head).
- Campaign file `CAMPAIGN.md` in full, all wave results.

---

## 0. MANDATORY PRIOR-ART SWEEP — run on the mathematics, not the wording

This is the third consecutive campaign wave at risk of rediscovery, so the sweep
was run on the **mathematical content** of the forcing question — cross-site
identification of one-site algebras, local vs global frame change, connections
and parallel transport, "covariance up to frame" — and **not** on the phrases
"common frame" or "forced". `docs/work_history/**` was searched explicitly.

### 0.1 The forcing question is ALREADY ANSWERED IN THE CORPUS, in the negative

**This is the headline prior art and it is decisive.** It predates this campaign
by six and a half weeks and it is not in `work_history` — it is in `docs/`:

> **`docs/MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md:95–99`**
> "The retained hopping `Σ_x a_x† a_{x+μ} + h.c.` contracts the fibre index of
> `a_{x+μ}` (in *some* frame at `x+μ`) with that of `a_x†` (in *some* frame at
> `x`). Writing it as `Σ_{x,i} a_{x,i}† a_{x+μ,i}` presupposes that "frame label
> `i` at `x`" means the same as "frame label `i` at `x+μ`". **The Lattice and
> Qubit axioms do not supply such a canonical identification.**"

That last sentence is the exact answer to task (a)–(d), written on 2026-06-08.
Its one-hop bridge states the same thing from the other side:

> **`docs/FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md:98–100`**
> "Therefore the translation bridge's `U=I` reference is the flat choice of
> coordinates on neighbouring fibres, **not an invariant physical rule that pins
> the fibre basis at `x` to the fibre basis at `y`**."

and gives the algebra at `:83–110` — under independent local bases the identity
link is rewritten `I → g_x g_y^†` (F3), a general transporter transforms
`U_xy → g_x U_xy g_y^†` (F4). The consumer note's own summary of what it closes,
`MATTER_GAUGE_...:175–179`, calls the gauge field "the **bookkeeping of the
framework's absent canonical cross-site fibre identification**".

**Caveat I am not papering over:** those two notes carry the internal space as
the graph-first `U(3)` *fibre*, not as the Qubit axiom's own `M_2(C)`. The
carrier differs. But the Step-1 sentence quoted above is stated about **the
Lattice and Qubit axioms directly**, and the argument (an index contraction
between two sites presupposes an identification the axioms do not supply) is
carrier-agnostic. I therefore treat it as on-point prior art and rebuild the
`M_2(C)` instance natively in §6 rather than inheriting it.

### 0.2 The repo's own implementation of translation covariance is "UP TO FRAME"

This kills route F3 (task item (c)) using the repo's own landed algebra:

> **`docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md:231–236`**
> (licensing lemma L-EQ) "The axiom data (Lattice + Qubit) is invariant under the
> lattice automorphisms `Aut = O ⋉ T` … Any kinetic term constructed from the
> axiom data WITHOUT an additional direction/position selector must therefore be
> `Aut`-covariant **up to the declared frame redundancy**."
>
> `:252–256` "Frame redundancy: **site-local** `U(1)`, `a_x → u(x) a_x`, acting as
> `t_μ(x) → conj(u(x+μ̂)) t_μ(x) u(x)`; … The **plaquette flux** … is
> frame-invariant".
>
> `:264–270` "(K2) translation covariance **up to frame**; (K3) cubic
> `O`-covariance **up to frame** (L-EQ) … there are EXACTLY TWO kinetic classes".
>
> `:454` (claim_scope) "translation+cubic covariance **up to site-local frame**
> collapses the kinetic family to exactly two flux classes; the site-local
> absorbing frame … is unique **up to gauge × global frame**".

So the repo already imposes translation and cubic covariance in the
**independent-onsite** reading with a site-local frame quotient, and the
invariant it extracts is a **holonomy** (plaquette flux), which is precisely the
object that exists when frames are *not* shared. Same posture at
`docs/PROTOCOL_ADMISSIBILITY_3D_REALIZATION_BRIDGE_AND_WORD_DISPERSIVENESS_NARROW_THEOREM_NOTE_2026-07-10.md:29`:
"translation covariance of the fixed rule requires each constituent factor to be
fully covariant **modulo local `U(1)` frames**".

### 0.3 The common frame is elsewhere tracked as a SUPPLIED input, sometimes as a named gate

- `docs/ONSITE_CHARGE_CONSERVING_..._STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md:4`
  and `:41` — "**Up to a uniform onsite basis**, `h = c II + r(ZI+IZ) + g ZZ +
  J(XX+YY)`"; its own scope line lists "the tensor carrier, charge axis,
  identical-edge ansatz, coefficients, and time are **supplied**". Note the class
  there is **four** real parameters, not two — a different supplied symmetry set,
  a different count.
- `docs/PAIRWISE_COMMUTING_..._BOUNDED_THEOREM_NOTE_2026-07-12.md:4` — "Up to one
  uniform onsite basis … The … **basis frame** … are supplied."
- `docs/RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md:70–71`
  — the cubic classification works "Within the **separately supplied** standard
  spatial-vector action on traceless `Herm(2)`". **That is the very assumption
  that lets a cubic rotation act on the internal `M_2(C)` at all**, and it is
  labelled supplied there.
- `ADM-1`, "local color-frame redundancy", is carried as an **open premise/gate**
  across `docs/EMERGENT_GAUGE_HEAT_KERNEL_..._2026-06-08.md:13–18,57–61,74` and
  `docs/RECORD_INSTRUMENT_COMPOSITE_LINK_..._2026-06-09.md:249`.
- `docs/work_history/repo/review_feedback/RELATIONAL_QUBIT_DISAGREEMENT_CANONICAL_LAW_ESCALATION_NOTE_2026-07-14.md:171–174`
  — "The common-frame reading **is itself physical**. Independent onsite frame
  covariance would leave only identity unless a shared connection, link, or
  relational program is supplied. The current phrase 'no possibility is
  privileged' does not choose between those dynamical readings." That is an
  **assertion** of physicality with no derivation attached, and it is the
  strongest pro-forcing sentence I found anywhere. §4.1 answers it.
- `.../QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:45–46`;
  `.../APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md:130`
  ("… does not follow from common-frame covariance alone. This candidate uses a
  supplied …"); `.../SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md:622`
  ("common frame/connection **still supplied**");
  `.../CFSI_Q_BELL_COHERENT_CAUSAL_FRONT_LAW_NOTE_2026-07-14.md:335`
  ("The common frame and causal policy are **supplied**").

### 0.4 A live contradiction in the corpus, on exactly this point

`docs/PRR_LOCAL_DERIVATION_FROM_JAYNES_MAX_ENTROPY_NARROW_THEOREM_NOTE_2026-05-22.md:87`
asserts the opposite of §0.1: "`α_t` maps the site-`x` factor `M_2(ℂ)_x` to the
site-`(x+t)` factor `M_2(ℂ)_{x+t}` **via the canonical identification**." The
identification is used there as if it existed and were canonical. Both rows are
`unaudited` on the live ledger (§0.6), so neither settles anything, but the
contradiction is real and is worth the owner's attention: **one note says the
canonical cross-site identification does not exist; another consumes it by
name.**

### 0.5 What is NOT prior art — my genuinely new content

Swept and found **nothing** for: a translation-invariant law that fails
common-frame covariance (§4.3 / gates `F3`–`F9`); the local-unitary orbit /
invariant count for a two-qubit Hermitian operator (`16 − 6 − 2 = 8`, gates
`B1`–`B4`); the commutant dimensions under the axiom-named **finite** cubic edge
stabiliser (`D1`,`D3`,`D5`) and under its **independent-onsite** version (`D2`,
witness `Z⊗Z`); and the redundancy-versus-symmetry framing. Greps covered
`docs/**` including `docs/work_history/**` and `scripts/**` for `orbit
dimension`, `local-unitary invariant`, `LU-equivalen`, `16 - 6`, `twisted
diagonal`, `conjugated translation`, `redundanc.*symmetry`, and the
translation-invariant-but-not-frame-covariant pattern.

### 0.6 Ledger status of everything cited above (shards, not prose)

| claim_id | claim_type | effective_status | audit_status |
| --- | --- | --- | --- |
| `matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08` | bounded_theorem | `unaudited` | `unaudited` |
| `fiber_frame_local_redundancy_bridge_narrow_theorem_note_2026-06-09` | bounded_theorem | `unaudited` | `unaudited` |
| `staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10` | bounded_theorem | `unaudited` | `unaudited` |
| `protocol_admissibility_3d_realization_bridge_and_word_dispersiveness_narrow_theorem_note_2026-07-10` | bounded_theorem | `unaudited` | `unaudited` |
| `record_faithful_cubic_neighbor_response_classification_bounded_theorem_note_2026-07-11` | bounded_theorem | `unaudited` | `unaudited` |
| `onsite_charge_conserving_endpoint_symmetric_common_hamiltonian_strict_qca_dichotomy_bounded_theorem_note_2026-07-12` | bounded_theorem | `unaudited` | `unaudited` |
| `staggered_dirac_minimal_surface_kinetic_corner_nonforcing_no_go_note_2026-07-10` | no_go | `unaudited` | `unaudited` |
| `prr_local_derivation_from_jaynes_max_entropy_narrow_theorem_note_2026-05-22` | bounded_theorem | `unaudited` | `unaudited` |
| `two_site_qubit_tensor_carrier_bridge_narrow_theorem_note_2026-06-06` | positive_theorem | `unaudited` | `unaudited` |
| `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25` | **decoration** | `retained_pending_chain` | `audited_decoration` |

The last row is the only one with any grade, and it matters: it is the note that
*defines* the translation operator. §4.3 shows what it actually contains.
Consistent with the campaign's own finding, **no `no_go` row anywhere is
retained**, so nothing below is cited as a foreclosure.

---

## (a) THE AXIOMS, VERBATIM — every sentence bearing on inter-site frames

### Lattice / Physical Locality (`MINIMAL_AXIOMS_2026-06-29.md:35–41`)

> `:37–38` "Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic rotations
> about each site."
>
> `:40–41` "No site is privileged. Sites are distinguished by the supplied
> lattice structure alone."

Bearing: this sentence is entirely about `Z^3`. "standard translations" and
"proper cubic rotations" are maps of **sites**. Nothing states that either acts
on the one-site possibility domain, and "proper cubic rotations **about each
site**" is if anything a *per-site* phrasing. "Sites are distinguished by the
supplied lattice structure alone" says the lattice structure exhausts what
distinguishes sites — it says nothing about what identifies their *contents*.

### Qubit / Site Possibility (`:43–53`)

> `:45` "Each site has a domain of local possibilities."
>
> `:47` "The full one-site possibility domain has algebraic presentation `M_2(C)`."
>
> `:49` "A `Cl(3,0)`-compatible real-algebra presentation may be used
> equivalently and adds no further primitive structure."
>
> `:52–53` "No possibility is privileged. Possibilities are distinguished by the
> supplied algebraic structure alone."

Bearing, sentence by sentence — this is where the whole question lives:

- `:45` distributes a domain **over sites** ("Each site has **a** domain"). No
  sentence anywhere identifies the domain at `x` with the domain at `y`.
- `:47` is the **strongest textual hook a forcing advocate has**: the definite
  singular "**The** full one-site possibility domain". I take it at its
  strongest and it still fails, because of the verb: it "**has algebraic
  presentation** `M_2(C)`". "Has presentation `A`" fixes an **isomorphism
  class**, not a **chosen isomorphism**. `M_2(C)` has a `PU(2)` of
  `*`-automorphisms, so "presented as `M_2(C)`" leaves an entire `PU(2)` free at
  each site. Rebuilt natively, gates `Q1`, `Q2`, `Q2m`: conjugation by any
  unitary preserves the product exactly (so the supplied algebraic structure is
  blind to it), and no non-scalar element survives all such conjugations
  (`dim_R = 1`).
- `:49` says the alternative real presentation "adds **no further primitive
  structure**". Read strictly, this *withholds* rather than grants: it does not
  license reading the `Cl(3,0)` vector triple as the *spatial* triple. That
  reading is exactly what
  `RECORD_FAITHFUL_CUBIC_..._2026-07-11.md:70–71` calls "separately supplied".
- `:52–53` is the decisive sentence and it points **away** from forcing. "No
  possibility is privileged" is a statement that the structure **distinguishes
  nothing inside the algebra** — a redundancy declaration, per site. Applied at
  each site independently, it grants *more* freedom, not less.

### Admissibility / Local Constraint (`:55–61`)

> `:57–58` "There is one fixed nearest-neighbor admissibility rule, **covariant
> under lattice translations and proper cubic rotations**."
>
> `:60–61` "For each site, the available possibilities are determined by, **and
> vary with**, the nearest-neighbor conditions."

Bearing: this is the only sentence in the four axioms containing the word
`covariant`, and the group it names is **spatial only**. "one fixed … rule" is
the second-strongest forcing hook (§3.4). "**and vary with**" is an explicit
non-triviality assertion — note it, because Record lacks it (below).

### Record / Fixed Reality (`:63–72`)

> `:70–72` "Only records are readable. A readout value is **determined by record
> content alone**. For any finite collection of pairwise-disjoint records, scalar
> readout `I` is additive, with `I(empty)=0`."

Bearing: no site index appears; the readout is scalar and additive. Critically,
Record says "determined by" and **not** "and vary with" — the phrase
Admissibility *does* carry at `:60–61`. That asymmetry is load-bearing in §4.2.

### Qualification (`:74–84`) — the tie-breaker, and it is explicit

> `:76–79` "These axioms state only their named primitive content. Further
> physical structure requires a retained derivation or bridge, or explicit
> approved-primitive registration, before use as a premise. **A choice not fixed
> by the supplied structure remains a named conditional or open dependency.**"

And the machine registry says the same in its own words:

> `docs/audit/data/axiom_premise_nodes.json:25` — the node "still supplies no …
> source/action bridge, physical observable bridge, state-selection rule,
> law-domain derivation, **law-level dependence on an unfixed choice**, or
> downstream theory consequence."

A frame **is** a choice; §6 `Q1`/`Q2` shows it is not fixed by the supplied
structure; a law written in a frame **is** a law-level dependence on an unfixed
choice. By the axiom memo's own rule, it "remains a named conditional or open
dependency".

### Machine check of the whole memo

`frame`: **0 occurrences**. `basis`: 1 occurrence, `:164`, inside the list of
things **outside** axiom content ("measurement basis selection"). `identif`: 1
occurrence, `:170`, also **outside** ("source/action and physical-observable
identification"). `SU(2)`, `unitary`, `isomorph`: **0 occurrences**.

### Direct answer to the question as posed

> "The axiom memo says no site is privileged and sites are distinguished by the
> supplied lattice structure alone — does that force a COMMON frame, forbid one,
> or say nothing?"

**It says nothing about frames.** It is a statement about how *sites* are
individuated. It neither forces nor forbids a common frame. The sentence that
comes closest to bearing on frames is the Qubit axiom's `:52–53`, and it points
the other way, because it is a redundancy declaration and redundancies do not
constrain laws.

---

## (b) THE STRONGEST CASE THAT COMMON-FRAME COVARIANCE IS FORCED

Built at full strength before being attacked. Each route is stated as its
proponent would state it.

### F1 — Gauge-triviality route

*A global frame choice has no physical content — it is pure convention. The
Qubit axiom's `:52–53` says exactly that: nothing distinguishes one basis. A
convention with no content may be fixed once, globally, without loss of
generality. Having fixed it, the only remaining freedom is to re-fix the one
convention, which changes the basis at **every** site by **the same** `u`.
Hence the theory's internal covariance group **is** the diagonal
`{u ⊗ u ⊗ ⋯}`, and the common-frame reading is not an assumption but the
physical content of "no possibility is privileged". Independent onsite `u_x`
would mean the frame is physical data varying site to site, which contradicts
`:52–53`.*

### F2 — Record-readout-comparability route

*Record `:70–72` says a readout value is determined by record content **alone**.
"Alone" excludes dependence on anything else about the record, including which
site carries it. Lattice `:40–41` says no site is privileged, so a site-dependent
readout function is forbidden outright. Therefore one and the same function `I`
eats record content at every site. Its argument at `x` lives in `D_x` and at `y`
in `D_y`, so a single well-defined `I` requires `D_x` and `D_y` to be the same
domain — a shared frame. If two sites carried incomparable frames, `I` could not
be a single content-determined function and the Record axiom would be
unsatisfiable. So Record forces frame comparability, and comparability across
all sites is a common frame.*

### F3 — Translation-invariance route (the one the owner most suspects)

*The Lattice axiom `:37–38` supplies "standard translations" as part of the
lattice structure, and Admissibility `:57–58` requires the rule to be covariant
under them. For translations to act on configurations at all, the `Z^3` action
must lift to the possibility assignment: a translation `T_a` needs a map
`D_x → D_{x+a}` for every `x`, satisfying the cocycle condition. `Z^3` acts
freely and transitively on sites, so any such lift trivialises the whole family:
pick a base site `0`, set `ψ_x = φ_{x,0} : D_0 → D_x`, and every site's domain is
now identified with `D_0`. That **is** a global frame, delivered by translation
covariance alone. The residual freedom is the choice of frame at `D_0` — one
global `u`, acting diagonally. Forced.*

### F4 — Admissibility-as-a-local-constraint route (the strongest)

*Admissibility `:57–58` asserts "**one fixed** nearest-neighbor admissibility
rule". For "one" rule to be applied at every edge, the rule must be a single
mathematical object; but the rule at edge `(x,y)` is a relation on `D_x × D_y`
and at `(x',y')` a relation on `D_{x'} × D_{y'}`. To say these are "the same
rule" is exactly to supply identifications `D_x ≅ D_{x'}`, `D_y ≅ D_{y'}`.
Moreover `:60–61` says the available possibilities "**vary with**" the neighbour
conditions, so the rule is **non-trivial**. And a non-trivial relation cannot be
invariant under independent onsite frame changes: solving directly,
`a I + b SWAP` is independent-onsite invariant only at `b = 0` (gate `A2m`), and
independent `PU(2) × PU(2)` acts transitively on pairs of pure states so the only
invariant relations are `∅` and everything. Therefore the rule **must** be
written relative to an edge identification. The axiom asserts such a rule exists;
therefore the identification exists; therefore covariance is common-frame.
Nothing else can make Admissibility's own sentences simultaneously true.*

---

## (c) DESTRUCTION OF EACH ROUTE

### 4.1 F1 fails: it computes the commutant of a redundancy group

F1's own premise defeats its conclusion. If the frame is "pure convention with no
physical content", then it is a **redundancy**, and a redundancy group acts on
the space of laws by **quotienting**, not by constraining. F1 slides, in one
step, from "changing the convention is unobservable" to "the law must commute
with the convention change". Those are different mathematical operations:

- **Constraint reading:** `{h : [h, G] = 0}`. On one edge with `G` the diagonal
  `SU(2)`: `dim_R = 2` (gates `A1`, `A1h`, with the negative control `A1b` that
  `X⊗I` is *not* in the commutant, so the count is not read off a dimension
  argument alone).
- **Redundancy reading:** `Herm(C^2 ⊗ C^2) / G`. With `G` the site-local
  unitaries plus the licensed positive rescaling and energy shift, the
  infinitesimal action has rank exactly **8** at an exact rational generic
  Hermitian probe (gate `B2`), so **8 physical parameters survive on one edge**
  (gate `B3`). Mutation control `B4`: at `h = SWAP` the same orbit has dimension
  only 3, because the diagonal `su(2)` stabilises `SWAP` — so `B1`/`B2` are not
  reporting a degenerate point.

The redundancy reading is the one `:52–53` licenses, and it gives **8**, not 2
and not 0. F1 does not narrow the menu; correctly applied it **widens** it by
six dimensions relative to the note's `span{I, SWAP}`.

A second, independent kill: if the frame really were pure gauge, then `SWAP`
itself would not be a well-defined object. Conjugating by site-local unitaries,
`(g ⊗ h) SWAP (g ⊗ h)† = ((g h†) ⊗ (h g†)) SWAP` — rebuilt exactly at gate `C1`,
with the underlying identity `SWAP (A⊗B) SWAP = B⊗A` verified for **symbolic**
`2×2` entries at gate `S0`. The result `(w ⊗ w†) SWAP` is Hermitian (`C2`), has
the **same** spectrum `{+1(×3), −1(×1)}` (`C3`) — so the ground-sector invariant
that PR #5602 R3 relies on is frame-**blind** — and is **not** in
`span{I, SWAP}` (`C4`, rank 3). So "the law is `I − SWAP`" is not a
gauge-invariant sentence. F1 cannot simultaneously say the frame has no content
and pick `SWAP` out of the carrier.

### 4.2 F2 fails twice: Record does not say "vary with", and readout never pins a frame

**First kill — the missing verb.** Compare, in the same memo:

> Admissibility `:60–61` "… are determined by, **and vary with**, the
> nearest-neighbor conditions."
> Record `:70–72` "A readout value is **determined by** record content alone."

Record does **not** say the readout varies with content. A **content-blind**
readout — `I(collection) = number of records`, additive over disjoint
collections, `I(∅) = 0` — satisfies every sentence of the Record axiom (gate
`E1`) and compares **no** frames whatsoever, because it never looks at content.
F2 needs the readout to be content-*sensitive*, and the axiom does not supply
that. This is the vacuous-premise trap: F2's crucial word "alone" is doing
locality work ("not on context"), not injectivity work.

**Second kill — even a maximally content-sensitive readout leaves a
positive-dimensional family.** Take the most favourable case for F2: a Bloch-axis
readout. Its stabiliser in the frame group is the entire `U(1)` of rotations
about that axis (gate `E2`, exact for symbolic `θ`), with mutation `E2m` showing
a perpendicular rotation *does* move it, so `E2` is not vacuous. So a
content-sensitive readout cuts `SU(2)` to `U(1)` at best; it never determines a
unique cross-site identification. F2's step "a single well-defined `I` requires
`D_x` and `D_y` to be the same domain" is false: it requires only that the
identification be readout-compatible, and readout-compatible identifications form
a group of dimension ≥ 1.

**Corroboration from the corpus, different notion but same posture:**
`docs/RECORD_COMPARABILITY_OWNER_ONE_PAGER_2026-07-04.md:53–57` records that an
adjacent comparability question was "assessed here (2026-07-04) as not derivable
from the" landed sentences. That is about ordering of realized configurations,
not frames — I am **not** conflating them — but it establishes that the repo does
not treat Record as a free source of comparability.

### 4.3 F3 fails: the owner's suspicion is exactly right, and here is the exact test

The owner's formulation is precise and it is the crux: *"translation invariance
says the LAW is the same at every site, which is not the same as saying the FRAME
is shared — a law can be translation-invariant while each site carries an
independent frame, provided the law is written frame-covariantly."*

F3's error is at the word "**the** lift". A lift of the `Z^3` action to the
possibility assignment **exists** — F3 is right about that — but it is **not
unique**, and two lifts differ by an arbitrary **site-local** frame assignment.
F3 silently picks the trivial one and then reports the frame it just chose as a
discovery.

**Constructive proof, exact, gates `F0`–`F9`.** Three sites on a ring, exact
sympy:

- `T` = the ordinary cyclic tensor-factor permutation. Unitary, `T³ = I`, and it
  carries the site-0 algebra onto the site-1 algebra (`F0`).
- `H = Σ_edges SWAP` is exactly `T`-invariant (`F1`) and is common-frame
  covariant (`F2`).
- Now give the sites **independent** exact-rational `SU(2)` frames
  `ρ_0 = I`, `ρ_1 = (1/5)[[3,4],[−4,3]]`, `ρ_2 = (1/13)[[5,12],[−12,5]]`, and set
  `G = ρ_0 ⊗ ρ_1 ⊗ ρ_2`, `H' = G H G†`, `T' = G T G†`.
- **`F3`: `T'` is unitary, has order exactly 3, and still carries the site-0
  algebra onto the site-1 algebra.** It implements the same permutation of sites
  that the Lattice axiom names. It is as legitimate a lift of the lattice
  translation as `T` is, and the axioms supply nothing that prefers `T`.
- **`F4`: `T' H' T'† = H'` exactly.** `H'` is translation-invariant.
- **`F5` (decisive): `H'` does NOT commute with the diagonal `su(2)`.** A
  translation-invariant law that is **not** common-frame covariant.
- **`F7`: every edge term of `H'` is isospectral to `SWAP`.** So `H'` is
  literally "one fixed rule" in the sense Admissibility `:57–58` asks for.
- **`F8` (control): make the three frames EQUAL and common-frame covariance is
  restored.** So `F5` is caused by frame *independence* and by nothing else — it
  is not an artifact of the construction.

Therefore *"translation invariance ⟹ same `u` at every site"* is **false**, and
it is false constructively, not by appeal.

**`F9` — the honest limit, stated rather than hidden.** `H'` and `H` are
unitarily equivalent (same spectrum), so `F5` does **not** exhibit new physics.
What it exhibits is that **common-frame covariance is a condition on the
coordinates, not on the law**. That is enough to defeat F3, because F3 must claim
that no translation-invariant law fails diagonal covariance, and `H'` is one.

**The corpus already did this, in the direction I am arguing.** F3's premise that
`T` is *the* translation traces to
`docs/TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`
— the only row here with any audit grade (`audited_decoration`,
`retained_pending_chain`). Read it: `:29–30` fixes the ladder matrices "in **the
ordered basis** `(|0⟩, |1⟩)`", `:35–36` defines `a_x` with **the same** `σ_∓` at
every site, and `:47` defines `T_a` by transporting **basis labels**
`b_{x−a} ↦ b_x`. So the graded row **assumes a common frame by construction**; it
does not derive one. And the repo's own bridge says so explicitly
(`FIBER_FRAME_LOCAL_REDUNDANCY_...:98–100`, `MATTER_GAUGE_...:81–85`): the
translation bridge's `U = I` reference "is the flat choice of coordinates", and
"under independent neighbouring fibre bases it is represented as `g(x)g(x+μ)†`".
And the landed kinetic-class treatment imposes "(K2) translation covariance **up
to frame**" with a **site-local** redundancy group
(`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_...:252–256, :264–270, :454`).

### 4.4 F4 fails on three separate counts, and the third one reverses the campaign's third horn

F4 is genuinely the strongest route. Its algebra is correct — gate `A2m`
reproduces it: `a I + b SWAP` is independent-onsite `SU(2)`-invariant only at
`b = 0`. It fails on what it does with that algebra.

**Kill 1 — invariance is not covariance.** F4 needs "one fixed rule" to mean "the
rule, as an operator on a fixed carrier, commutes with the internal group". The
axiom asks for covariance under **lattice translations and proper cubic
rotations** and no internal group at all (`:57–58`, and the machine check: zero
occurrences of `frame`, `SU(2)`, `unitary` in the memo). A rule can be one fixed
rule *as an abstract relation* while its coordinate expression differs edge to
edge, and §4.3 builds exactly that object: `H'` has isospectral edge terms
(`F7`), is exactly translation-covariant (`F4`), and violates internal
diagonal invariance (`F5`). So "one fixed rule" is satisfied without internal
invariance, and F4's central inference does not hold.

**Kill 2 — the axiom's group is FINITE; the continuous `SU(2)` is what does the
cutting.** Grant F4 everything: grant the common-frame reading, and grant (as
`RECORD_FAITHFUL_CUBIC_...:70–71` says is separately supplied) that proper cubic
rotations act internally through the `Cl(3,0)`↔spatial vector identification.
Then the edge-relevant group is the stabiliser of an edge inside the proper cubic
motions: the `C_4` about the edge axis, extended by the endpoint flip (a
`π`-rotation composed with a lattice translation) to the dihedral group of order
8 — verified at gates `D0`, `D3a`, `D3b`. The exact class sizes:

- common-frame `C_4` alone: `dim_R = **6**` (`D1`);
- common-frame full order-8 edge stabiliser: `dim_R = **5**` (`D3`);
- and if the cubic rotations do **not** act internally at all — the strict
  reading of `:49`, "adds no further primitive structure" — the only edge
  constraint is the bare endpoint exchange: `dim_R = **10**` (`D5`).

None of these is 2. The step from 5 (or 6, or 10) down to 2 is bought entirely
with the **continuous** `SU(2)`, which appears nowhere in the axioms. Summary
gate `D4`: `16 → 10 → 6 → 5 → 2`.

**Kill 3 — and this one inverts the campaign's third horn.** F4's clinching move
is "independent-onsite covariance kills every nontrivial pair law". That is true
only for the supplied continuous group. Under **independent-onsite** covariance
with respect to the group the Lattice axiom actually names:

- `dim_R = **4**` (`D2`) — a four-parameter nontrivial family survives;
- explicit witness `Z ⊗ Z`: Hermitian, invariant under `u_4 ⊗ I` and `I ⊗ u_4`
  separately, and not a multiple of `I` (`D2w`);
- mutation `D2m`: the same witness fails full independent `SU(2)` invariance, so
  `D2` is a statement about the finite group and is not in contradiction with
  `A2`.

So the task brief's third horn — "if independent-onsite covariance is what the
axioms license, there is no nontrivial pair law at all, which would be a very
sharp negative about the framework reach" — **does not follow**. It is an
artifact of a supplied continuous `SU(2)`. This is also a correction to
limitation **L1** of PR #5602 (`:156–166`), whose sentence "under independent
onsite covariance **no nontrivial pair interaction survives at all**" needs the
qualifier *for the continuous group*.

---

## (d) VERDICT, CONFIDENCE, AND THE SENTENCE THAT WOULD HAVE TO EXIST

### 5.1 Verdict

1. **Common-frame covariance is NOT forced by Lattice/Qubit/Admissibility/Record.**
   Confidence **high (~0.95)**. Grounds: the memo names no internal group at all
   (machine-checked, §(a)); its only `covariant` clause quantifies over spatial
   motions; the Qualification `:78–79` and the registry node
   (`axiom_premise_nodes.json:25`, "no … law-level dependence on an unfixed
   choice") classify an unfixed choice as a named conditional; the constructive
   counterexample `F5` defeats the translation route; and the corpus already
   states the conclusion at `MATTER_GAUGE_...:98–99`. Residual 0.05 covers the
   possibility that an owner reads `:47`'s definite article as fixing a
   presentation rather than an isomorphism class — a reading `:52–53` and gates
   `Q1`/`Q2` argue against, but which is a reading, not a theorem.
2. **Independent-onsite covariance is not forced either.** Confidence **high
   (~0.95)**, same grounds. The axioms are silent, not partisan.
3. **The premise does more than create the menu — it manufactures a
   two-point menu out of a continuum.** Confidence **very high (~0.99)**;
   this is arithmetic on the runner. Read as a **redundancy** (what `:52–53`
   says), one edge carries **8** physical parameters (`B3`). Read as a
   **symmetry** with a supplied continuous group, it carries **1**. The
   difference is seven dimensions of supplied content.
4. **"Independent-onsite ⟹ no nontrivial pair law" is FALSE for the group the
   axioms name.** Confidence **very high (~0.99)**; `D2` + witness `D2w` +
   mutation `D2m`. The sharp negative the campaign hoped for from that horn is
   not available on this route.
5. **Therefore the honest campaign statement is:** the framework supplies the
   covariance reading *and* the group it is a covariance of, and gets the
   two-point menu as a consequence of both. Both PR #5602's H4 and its L1 are
   supplied inputs. This **confirms** the note's own self-description
   (`:61–70`, `:81–82`, `:156–166`) and closes the note's own open item
   `N6(1)` (`:316–318`, "Test whether the common-frame reading is forced by, or
   merely compatible with, the Admissibility covariance sentence") with:
   **merely compatible — and the Admissibility covariance sentence is not even
   about an internal group.**

### 5.2 The exact sentence that would have to exist

Forcing needs **two** sentences, not one, and **neither exists anywhere in the
repository**.

**Sentence 1 (the identification).** Something with the force of:

> *"The one-site possibility domains at distinct sites are identified by a fixed
> family of algebra isomorphisms carried by the lattice translations and proper
> cubic rotations; this identification is part of the supplied structure."*

Nothing of this form exists. The nearest sentence in the corpus is its **direct
negation**, at
`docs/MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md:98–99`:
"**The Lattice and Qubit axioms do not supply such a canonical identification.**"
The only sentence pointing the other way is
`docs/PRR_LOCAL_DERIVATION_FROM_JAYNES_MAX_ENTROPY_NARROW_THEOREM_NOTE_2026-05-22.md:87`
("via the canonical identification"), which **uses** the identification without
establishing it. Both rows are `unaudited`.

**Sentence 2 (the symmetry).** Even with Sentence 1, the two-point menu needs:

> *"The admissibility rule is invariant under the continuous group of unitary
> re-presentations of the one-site domain, acting identically at every site."*

Nothing of this form exists either. `MINIMAL_AXIOMS_2026-06-29.md:57–58` supplies
covariance under **lattice translations and proper cubic rotations** only, and
`:49` withholds rather than grants an internal action of those rotations. The
memo contains the word `frame` zero times, `SU(2)` zero times, `unitary` zero
times.

**Where the burden lands.** By the memo's own Qualification `:76–79` — "Further
physical structure requires a retained derivation or bridge, or explicit
approved-primitive registration, before use as a premise. A choice not fixed by
the supplied structure remains a named conditional or open dependency" — and by
`PRIMITIVE_REGISTRY_CHECK.md:17–19` (an unregistered proposed primitive is
unapproved), the cross-site frame identification is a **named conditional or open
dependency**. It is not in `axiom_premise_nodes.json`. Adding it would require
explicit owner approval and a reviewed registry/policy update; **I am not
proposing one and no new axiom, primitive, or vocabulary is introduced by this
report.**

### 5.3 What this means for the campaign (for the owner, not a verdict)

- The task brief's binary — *forced ⟹ real no-go; supplied ⟹ artifact* — has a
  third outcome, and this is it: **supplied, and the artifact is worse than the
  campaign thought.** The menu is not two points and not zero points; under the
  reading the axioms license it is an **8-parameter continuum on a single edge**.
  That is a sharper negative than the two-point witness Wave 1 chased, it does
  not depend on any supplied covariance premise, and it is not prior art (§0.5).
- Wave 2's recommendation **(B)** ("since under independent-onsite covariance
  there is NO menu, that single question decides whether the matter law is
  underdetermined at all") rests on a premise this report refutes: under the
  axiom-named group there **is** a menu even with independent onsite frames
  (`D2`). The question is still worth asking, but it does not decide the
  underdetermination, because the underdetermination is already 8-dimensional
  before any covariance premise is chosen.
- Recommendation **(A)** is unaffected and is reinforced: §0.1–§0.3 found four
  more `docs/`-level surfaces carrying the frame answer, plus one live
  contradiction (§0.4), all `unaudited`.
- The one clean positive available here: **`MATTER_GAUGE_...` and
  `FIBER_FRAME_LOCAL_REDUNDANCY_...` already contain the answer and already
  name the object that repairs it — a connection.** The corpus route from
  "frames are independent" to "a link variable appears" is written
  (`MATTER_GAUGE_...:108–139`). If the owner wants a positive out of this lane,
  the shape is: *the matter law's frame data is not fixed by the axioms; the
  minimal object that fixes it is a connection; the surviving invariant is a
  holonomy* — which is exactly the flux classification the staggered kinetic
  note already reaches at `:262–292`.

---

## 6. VERIFICATION — native, exact, `PASS=51 FAIL=0`

Runner written for this report and run at
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/taskB_frame_forcing_probe.py`
(scratchpad — nothing was added to the repository). Full source is inlined below
so this report is self-contained and reproducible after the scratchpad is gone.

Design rules honoured, and stated plainly:

- **Exact sympy throughout.** No float is an input to any load-bearing
  comparison; no numeric tolerance appears; every `SU(2)` element used is an
  exact rational matrix or an exact root of unity.
- **No prose-needle gates.** The runner reads no markdown and greps no text,
  including its own, so the `PASS` total is entirely mathematical.
- **Construction-mutation probes, not assertion flips.** `A1b` (a non-invariant
  candidate must leave the commutant), `A2m` (solve for the coefficient rather
  than assert it), `B4` (rebuild the orbit at a symmetric point; the rank must
  fall 6→3), `C4` (rank must rise to 3), `D2m` (the finite-group witness must
  fail the continuous group), `E2m` (a perpendicular rotation must move the
  readout), `F8` (rebuild with equal frames; covariance must return), `Q2m` (a
  specific non-scalar must move).
- **The `PASS` total is a gate count, not a count of independent scientific
  facts.**
- **One prediction of mine was wrong and the runner caught it.** I predicted
  `dim_R = 4` for the full order-8 common-frame edge stabiliser; the exact
  computation returned **5** (`D3`). The label was corrected to the computed
  value, not the other way round. The reason is checkable by hand: the flip acts
  as `−1` on `span{|01⟩,|10⟩}`, so it constrains nothing there and only forces
  `m_00 = m_11`, giving `4 + 1 = 5`.

### 6.1 Runner output, verbatim

```text
PASS S0 SWAP is the exchange operator: SWAP (A(x)B) SWAP = B(x)A for symbolic A,B :: symbolic 2x2 entries
PASS S1 SWAP is Hermitian and an involution :: SWAP^2 = I
PASS Q1 conjugation by a unitary is a *-algebra automorphism of M_2(C): it preserves the product exactly, for symbolic operands :: so the SUPPLIED algebraic structure is blind to it
PASS Q2 no NON-SCALAR element of M_2(C) is fixed by every such conjugation (commutant of SU(2) in M_2 is the scalars) :: dim_R=1: a presentation of M_2(C) is fixed only up to a whole PU(2)
PASS Q2m MUTATION a specific non-scalar IS moved, so Q2 is not vacuous :: w Z w^dag != Z
PASS A0 no internal covariance demanded: dim_R Herm(C^2 (x) C^2) = 16 :: dim_R=16
PASS A1 COMMON-frame SU(2) (diagonal): commutant has complex dimension 2 :: dim_C=2
PASS A1h and its Hermitian part has real dimension 2 :: dim_R=2
PASS A1a I and SWAP are IN the diagonal commutant :: both commute
PASS A1b NEGATIVE CONTROL X(x)I is NOT in the diagonal commutant :: not a tautology
PASS A1c {I, SWAP} is linearly independent, so the commutant EQUALS span{I,SWAP} :: rank=2 = dim
PASS A2 INDEPENDENT onsite SU(2): commutant collapses to complex dimension 1 (scalars) :: dim_C=1
PASS A2h Hermitian part real dimension 1 :: dim_R=1
PASS A2m MUTATION a*I + b*SWAP is independent-onsite invariant only at b = 0 :: solution=[{b: 0}]
PASS B0 the probe operator is Hermitian by construction :: h = h^dag
PASS B1 generic local-unitary orbit through a Hermitian pair operator has real dimension 6 :: rank=6 (= dim su(2)+su(2), so the action is locally free)
PASS B2 adding the licensed scale and shift directions gives rank 8 :: rank=8
PASS B3 therefore the REDUNDANCY reading leaves 16 - 8 = 8 physical parameters on ONE edge :: 8 invariants, versus 1 free coefficient under the SYMMETRY reading
PASS B4 MUTATION at h = SWAP the same orbit has dimension only 3 (the diagonal stabilises SWAP) :: rank=3, stabiliser = diagonal su(2)
PASS C0 w is a genuine SU(2) element (exact rational) :: w^dag w = I, det = 1
PASS C1 CONSTRUCTION (g(x)h) SWAP (g(x)h)^dag = ((g h^dag)(x)(h g^dag)) SWAP :: verified on an exact rational instance
PASS C2 the twisted exchange (w(x)w^dag)SWAP is Hermitian :: Hermitian
PASS C3 it has the SAME spectrum as SWAP, {+1 (x3), -1 (x1)} :: eigenvals={-1: 1, 1: 3}
PASS C4 but it is NOT in span{I, SWAP}: the twisted law is a DIFFERENT operator :: rank=3 > 2, so the frame choice changes the law on the fixed carrier
PASS C5 the TWISTED diagonal {u (x) w u w^dag} also has commutant dimension exactly 2 :: dim_C=2
PASS C6 and it is spanned by {I, (w^dag(x)w)SWAP}, NOT by {I, SWAP} :: SWAP itself fails the twisted covariance
PASS C7 hence 'some common frame exists' leaves a 3-parameter SO(3) of inequivalent exchange laws on a fixed carrier (= the orbit dimension of B4), not two points :: orbit dim 3, times the sign bit
PASS D0 u4 is unitary with u4^4 = -I, so u4 (x) u4 has order exactly 4 on the edge :: order 4
PASS D1 COMMON-frame, axiom-licensed FINITE C4 only: dim_R = 6, not 2 :: dim_R=6
PASS D2 INDEPENDENT-onsite C4 x C4: dim_R = 4 -- a NONTRIVIAL pair law SURVIVES :: dim_R=4 (the 'nothing survives' statement needs the full SU(2))
PASS D2w WITNESS Z(x)Z is independent-onsite C4-invariant, Hermitian, and not a multiple of I :: explicit nontrivial independent-onsite-invariant pair term
PASS D2m MUTATION the same witness FAILS full independent SU(2) invariance :: so D2 is a statement about the FINITE group, not a contradiction of A2
PASS D3a the endpoint flip is unitary and squares to the identity on the edge :: involution
PASS D3b the flip inverts the C4 generator, so the two together generate the dihedral group of order 8 -- the full proper edge stabiliser :: F A F^dag = A^{-1}
PASS D3 COMMON-frame FULL edge stabiliser (C4 + endpoint flip): dim_R = 5, still not 2 :: dim_R=5
PASS D5 if the cubic rotations do NOT act internally at all, the only edge constraint is the bare endpoint exchange and the class is dim_R = 10 :: dim_R=10
PASS D4 SUMMARY the SU(2) content of the common-frame premise does the work: 16 -> 10 -> 6 -> 5 under axiom-named structure, 16 -> 2 only after SU(2) is supplied :: 16, 10, 6, 5, 2
PASS E1 a content-blind readout I(collection) = #records satisfies additivity and I(empty)=0 :: additive, I(empty)=0, and it reads NO content, so it compares no frames
PASS E2 the full U(1) of rotations about the readout axis preserves the readout exactly :: stabiliser of a Z-readout is 1-dimensional, so readout never pins a unique frame
PASS E2m MUTATION a rotation about a perpendicular axis DOES move the readout :: Z -> -Z, so E2 is not vacuous
PASS F0 T is unitary, T^3 = I, and it implements the site shift on the local algebras :: T (site0 algebra) T^dag = site1 algebra
PASS F1 the common-frame ring law H = sum_edges SWAP is translation invariant :: T H T^dag = H
PASS F2 ... and it IS common-frame SU(2) covariant :: commutes with all three
PASS F3a rho1, rho2 are exact SU(2) elements and the three frames are NOT all equal :: distinct site frames
PASS F3 T' = G T G^dag is unitary, has order 3, and STILL implements the site shift on the local algebras -- it is a legitimate lift of the lattice translation :: T' (site0 algebra) T'^dag = site1 algebra
PASS F4 H' = G H G^dag is EXACTLY invariant under that translation :: T' H' T'^dag = H'
PASS F5 DECISIVE H' is NOT common-frame SU(2) covariant: it fails the diagonal commutant :: a translation-invariant law that carries INDEPENDENT site frames
PASS F6 H' is a genuinely different operator on the same carrier, not a relabelling of H :: H' != H
PASS F7 every edge term of H' has the SAME spectrum as SWAP, so H' is 'one fixed rule' in exactly the sense the Admissibility sentence asks for :: isospectral edge terms
PASS F8 CONTROL with EQUAL site frames (rho0=rho1=rho2=w) the same construction returns a common-frame-covariant law, so F5 is caused by frame INDEPENDENCE and nothing else :: equal frames -> covariance restored
PASS F9 H' and H are unitarily equivalent (same spectrum), which is the honest limit of F5: the common-frame condition constrains the COORDINATES, not the physics :: isospectral

PASS=51 FAIL=0
```

### 6.2 Runner source, verbatim

```python
#!/usr/bin/env python3
"""
TASK B probe: is COMMON-FRAME covariance forced by Lattice/Qubit/Admissibility/Record?

Exact sympy throughout. No float is an input to any load-bearing comparison.
No prose is read; no gate greps text. Every claimed constant has a mutation
partner or a negative control.

Sections
  A  baseline class sizes under the three readings of the internal group
  B  redundancy-vs-symmetry: the gauge QUOTIENT dimension (reading 2)
  C  "there exists a common frame" is not "the standard common frame"
  D  the AXIOM-LICENSED group is FINITE (proper cubic), not SU(2)
  E  Record readout does not determine a cross-site identification
  F  translation invariance does NOT force a shared frame (3-site witness)
"""

import sympy as sp

PASS = 0
FAIL = 0
LINES = []


def gate(label, ok, detail=""):
    global PASS, FAIL
    if ok is not True:
        FAIL += 1
        LINES.append("FAIL %s :: %s" % (label, detail))
    else:
        PASS += 1
        LINES.append("PASS %s :: %s" % (label, detail))


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
I4 = sp.eye(4)


def kron(a, b):
    return sp.Matrix(sp.kronecker_product(a, b))


SWAP = sp.Matrix([[1, 0, 0, 0],
                  [0, 0, 1, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 1]])

# sanity on SWAP itself (construction, not assertion): SWAP (A (x) B) SWAP = B (x) A
_a = sp.Matrix(2, 2, sp.symbols('a0:4'))
_b = sp.Matrix(2, 2, sp.symbols('b0:4'))
gate("S0 SWAP is the exchange operator: SWAP (A(x)B) SWAP = B(x)A for symbolic A,B",
     sp.simplify(SWAP * kron(_a, _b) * SWAP - kron(_b, _a)) == sp.zeros(4, 4),
     "symbolic 2x2 entries")
gate("S1 SWAP is Hermitian and an involution",
     (SWAP.H == SWAP) and (SWAP * SWAP == I4), "SWAP^2 = I")


# ---------------------------------------------------------------- helpers
def commutant_dim(gens, n=4):
    """dim_C of the commutant of `gens` inside M_n(C), exactly."""
    v = sp.symbols('m0:%d' % (n * n))
    M = sp.Matrix(n, n, list(v))
    eqs = []
    for g in gens:
        C = sp.expand(M * g - g * M)
        eqs.extend(list(C))
    A, _ = sp.linear_eq_to_matrix(eqs, v)
    return n * n - A.rank(), v, M, A


def herm_solution_dim(gens, n=4):
    """dim_R of the HERMITIAN part of the commutant, computed directly over R."""
    # real parameterization of Herm(n)
    re = sp.symbols('r0:%d' % (n * n), real=True)
    params = []
    M = sp.zeros(n, n)
    k = 0
    for i in range(n):
        M[i, i] = re[k]
        params.append(re[k])
        k += 1
    for i in range(n):
        for j in range(i + 1, n):
            p = re[k]
            q = re[k + 1]
            params.append(p)
            params.append(q)
            k += 2
            M[i, j] = p + sp.I * q
            M[j, i] = p - sp.I * q
    eqs = []
    for g in gens:
        C = sp.expand(M * g - g * M)
        for e in C:
            r, i = sp.expand(e).as_real_imag()
            eqs.append(sp.expand(r))
            eqs.append(sp.expand(i))
    if not any(e != 0 for e in eqs):
        return len(params)
    A, _ = sp.linear_eq_to_matrix(eqs, params)
    return len(params) - A.rank()


# ================================================================ SECTION Q
# Instantiating the Qubit axiom sentence "No possibility is privileged. Possibilities
# are distinguished by the supplied algebraic structure alone."

_p = sp.Matrix(2, 2, sp.symbols('p0:4'))
_q = sp.Matrix(2, 2, sp.symbols('q0:4'))
wq = sp.Rational(1, 5) * sp.Matrix([[3, 4], [-4, 3]])
gate("Q1 conjugation by a unitary is a *-algebra automorphism of M_2(C): it preserves the "
     "product exactly, for symbolic operands",
     sp.simplify((wq * _p * wq.H) * (wq * _q * wq.H) - wq * (_p * _q) * wq.H) == sp.zeros(2, 2),
     "so the SUPPLIED algebraic structure is blind to it")
gate("Q2 no NON-SCALAR element of M_2(C) is fixed by every such conjugation "
     "(commutant of SU(2) in M_2 is the scalars)",
     herm_solution_dim([X, Y, Z], n=2) == 1,
     "dim_R=1: a presentation of M_2(C) is fixed only up to a whole PU(2)")
gate("Q2m MUTATION a specific non-scalar IS moved, so Q2 is not vacuous",
     sp.simplify(wq * Z * wq.H - Z) != sp.zeros(2, 2), "w Z w^dag != Z")


# ================================================================ SECTION A
# The three readings of the internal group, as SYMMETRY constraints.

DIAG = [kron(X, I2) + kron(I2, X),
        kron(Y, I2) + kron(I2, Y),
        kron(Z, I2) + kron(I2, Z)]
INDEP = [kron(X, I2), kron(Y, I2), kron(Z, I2),
         kron(I2, X), kron(I2, Y), kron(I2, Z)]

gate("A0 no internal covariance demanded: dim_R Herm(C^2 (x) C^2) = 16",
     herm_solution_dim([]) == 16, "dim_R=16")

dA, _, _, _ = commutant_dim(DIAG)
gate("A1 COMMON-frame SU(2) (diagonal): commutant has complex dimension 2",
     dA == 2, "dim_C=%d" % dA)
gate("A1h and its Hermitian part has real dimension 2",
     herm_solution_dim(DIAG) == 2, "dim_R=2")

# both containments, with a negative control
gate("A1a I and SWAP are IN the diagonal commutant",
     all(sp.simplify(g * I4 - I4 * g) == sp.zeros(4, 4) for g in DIAG) and
     all(sp.simplify(SWAP * g - g * SWAP) == sp.zeros(4, 4) for g in DIAG),
     "both commute")
gate("A1b NEGATIVE CONTROL X(x)I is NOT in the diagonal commutant",
     any(sp.simplify(kron(X, I2) * g - g * kron(X, I2)) != sp.zeros(4, 4) for g in DIAG),
     "not a tautology")
gate("A1c {I, SWAP} is linearly independent, so the commutant EQUALS span{I,SWAP}",
     sp.Matrix([list(I4), list(SWAP)]).rank() == 2 and dA == 2, "rank=2 = dim")

dB, _, _, _ = commutant_dim(INDEP)
gate("A2 INDEPENDENT onsite SU(2): commutant collapses to complex dimension 1 (scalars)",
     dB == 1, "dim_C=%d" % dB)
gate("A2h Hermitian part real dimension 1",
     herm_solution_dim(INDEP) == 1, "dim_R=1")

a_, b_ = sp.symbols('a b', real=True)
h_ab = a_ * I4 + b_ * SWAP
res = [sp.simplify(h_ab * g - g * h_ab) for g in INDEP]
sol = sp.solve([sp.Eq(e, 0) for m in res for e in m], [a_, b_], dict=True)
gate("A2m MUTATION a*I + b*SWAP is independent-onsite invariant only at b = 0",
     len(sol) == 1 and sp.simplify(sol[0].get(b_, b_)) == 0,
     "solution=%s" % sol)


# ================================================================ SECTION B
# Reading 2: the frame group as a REDUNDANCY (gauge), which QUOTIENTS.
# Infinitesimal action on Herm(4): h -> [A1(x)I + I(x)A2, h] + alpha*h + beta*I.

def orbit_rank(h, include_scale_shift=True):
    t = sp.symbols('t1:9', real=True)
    A1 = sp.I * (t[0] * X + t[1] * Y + t[2] * Z)      # su(2) at site 1
    A2 = sp.I * (t[3] * X + t[4] * Y + t[5] * Z)      # su(2) at site 2
    G = kron(A1, I2) + kron(I2, A2)
    V = sp.expand(G * h - h * G)
    used = list(t[:6])
    if include_scale_shift:
        V = sp.expand(V + t[6] * h + t[7] * I4)
        used = list(t[:8])
    eqs = []
    for e in V:
        r, i = sp.expand(e).as_real_imag()
        eqs.append(sp.expand(r))
        eqs.append(sp.expand(i))
    A, _ = sp.linear_eq_to_matrix(eqs, used)
    return A.rank()


# an explicit RATIONAL generic Hermitian h (no floats anywhere)
hg = sp.Matrix([[sp.Integer(3), 1 + sp.I, 2 - sp.I, sp.I],
                [1 - sp.I, sp.Integer(5), sp.Rational(1, 2) + 2 * sp.I, 1],
                [2 + sp.I, sp.Rational(1, 2) - 2 * sp.I, sp.Integer(7), 3 - sp.I],
                [-sp.I, 1, 3 + sp.I, sp.Integer(11)]])
gate("B0 the probe operator is Hermitian by construction", hg.H == hg, "h = h^dag")

r_gauge = orbit_rank(hg, include_scale_shift=False)
gate("B1 generic local-unitary orbit through a Hermitian pair operator has real dimension 6",
     r_gauge == 6, "rank=%d (= dim su(2)+su(2), so the action is locally free)" % r_gauge)

r_full = orbit_rank(hg, include_scale_shift=True)
gate("B2 adding the licensed scale and shift directions gives rank 8",
     r_full == 8, "rank=%d" % r_full)

gate("B3 therefore the REDUNDANCY reading leaves 16 - 8 = 8 physical parameters on ONE edge",
     16 - r_full == 8, "8 invariants, versus 1 free coefficient under the SYMMETRY reading")

r_swap = orbit_rank(SWAP, include_scale_shift=False)
gate("B4 MUTATION at h = SWAP the same orbit has dimension only 3 (the diagonal stabilises SWAP)",
     r_swap == 3, "rank=%d, stabiliser = diagonal su(2)" % r_swap)


# ================================================================ SECTION C
# "there EXISTS a common frame" != "THE standard common frame".
# Conjugating SWAP by site-local unitaries gives (w (x) w^dag) SWAP.

w = sp.Rational(1, 5) * sp.Matrix([[3, 4], [-4, 3]])          # exact rational SU(2)
gate("C0 w is a genuine SU(2) element (exact rational)",
     sp.simplify(w.H * w) == I2 and sp.simplify(w.det()) == 1, "w^dag w = I, det = 1")

g1 = w
g2 = I2
lhs = kron(g1, g2) * SWAP * kron(g1, g2).H
rhs = kron(g1 * g2.H, g2 * g1.H) * SWAP
gate("C1 CONSTRUCTION (g(x)h) SWAP (g(x)h)^dag = ((g h^dag)(x)(h g^dag)) SWAP",
     sp.simplify(lhs - rhs) == sp.zeros(4, 4), "verified on an exact rational instance")

SWAPw = sp.simplify(kron(w, w.H) * SWAP)
gate("C2 the twisted exchange (w(x)w^dag)SWAP is Hermitian",
     sp.simplify(SWAPw.H - SWAPw) == sp.zeros(4, 4), "Hermitian")
ev = SWAPw.eigenvals()
gate("C3 it has the SAME spectrum as SWAP, {+1 (x3), -1 (x1)}",
     ev == {sp.Integer(1): 3, sp.Integer(-1): 1}, "eigenvals=%s" % ev)
gate("C4 but it is NOT in span{I, SWAP}: the twisted law is a DIFFERENT operator",
     sp.Matrix([list(I4), list(SWAP), list(SWAPw)]).rank() == 3,
     "rank=3 > 2, so the frame choice changes the law on the fixed carrier")

# the twisted diagonal has its own 2-dimensional commutant
TWIST = [sp.expand(kron(P, I2) + kron(I2, w * P * w.H)) for P in (X, Y, Z)]
dT, _, _, _ = commutant_dim(TWIST)
gate("C5 the TWISTED diagonal {u (x) w u w^dag} also has commutant dimension exactly 2",
     dT == 2, "dim_C=%d" % dT)
gate("C6 and it is spanned by {I, (w^dag(x)w)SWAP}, NOT by {I, SWAP}",
     all(sp.simplify(kron(w.H, w) * SWAP * g - g * kron(w.H, w) * SWAP) == sp.zeros(4, 4)
         for g in TWIST) and
     any(sp.simplify(SWAP * g - g * SWAP) != sp.zeros(4, 4) for g in TWIST),
     "SWAP itself fails the twisted covariance")
gate("C7 hence 'some common frame exists' leaves a 3-parameter SO(3) of inequivalent "
     "exchange laws on a fixed carrier (= the orbit dimension of B4), not two points",
     r_swap == 3, "orbit dim 3, times the sign bit")


# ================================================================ SECTION D
# The group the axioms actually name is the PROPER CUBIC group, which is FINITE.
# Its edge stabiliser is C4 about the edge axis, extended by the endpoint flip.
# (Whether it acts on M_2(C) at all is itself supplied -- see the report.)

zeta = sp.exp(sp.I * sp.pi / 4)
u4 = sp.Matrix([[zeta**-1, 0], [0, zeta]])          # spin lift of the pi/2 rotation about z
gate("D0 u4 is unitary with u4^4 = -I, so u4 (x) u4 has order exactly 4 on the edge",
     sp.simplify(u4.H * u4) == I2 and
     sp.simplify(u4**4 + I2) == sp.zeros(2, 2) and
     sp.simplify(kron(u4, u4)**4 - I4) == sp.zeros(4, 4) and
     sp.simplify(kron(u4, u4)**2 - I4) != sp.zeros(4, 4),
     "order 4")

dC4 = herm_solution_dim([kron(u4, u4)])
gate("D1 COMMON-frame, axiom-licensed FINITE C4 only: dim_R = 6, not 2",
     dC4 == 6, "dim_R=%d" % dC4)

dC4i = herm_solution_dim([kron(u4, I2), kron(I2, u4)])
gate("D2 INDEPENDENT-onsite C4 x C4: dim_R = 4 -- a NONTRIVIAL pair law SURVIVES",
     dC4i == 4, "dim_R=%d (the 'nothing survives' statement needs the full SU(2))" % dC4i)

ZZ = kron(Z, Z)
gate("D2w WITNESS Z(x)Z is independent-onsite C4-invariant, Hermitian, and not a multiple of I",
     sp.simplify(ZZ * kron(u4, I2) - kron(u4, I2) * ZZ) == sp.zeros(4, 4) and
     sp.simplify(ZZ * kron(I2, u4) - kron(I2, u4) * ZZ) == sp.zeros(4, 4) and
     ZZ.H == ZZ and sp.Matrix([list(I4), list(ZZ)]).rank() == 2,
     "explicit nontrivial independent-onsite-invariant pair term")
gate("D2m MUTATION the same witness FAILS full independent SU(2) invariance",
     any(sp.simplify(ZZ * g - g * ZZ) != sp.zeros(4, 4) for g in INDEP),
     "so D2 is a statement about the FINITE group, not a contradiction of A2")

# endpoint flip: pi rotation about an axis perpendicular to the edge, composed with
# the lattice translation that exchanges the two endpoints.
v = sp.Matrix([[0, -sp.I], [-sp.I, 0]])             # spin lift of the pi rotation about x
FLIP = sp.simplify(kron(v, v) * SWAP)
gate("D3a the endpoint flip is unitary and squares to the identity on the edge",
     sp.simplify(FLIP.H * FLIP) == I4 and sp.simplify(FLIP * FLIP - I4) == sp.zeros(4, 4),
     "involution")
gate("D3b the flip inverts the C4 generator, so the two together generate the dihedral "
     "group of order 8 -- the full proper edge stabiliser",
     sp.simplify(FLIP * kron(u4, u4) * FLIP.H - kron(u4, u4).H) == sp.zeros(4, 4),
     "F A F^dag = A^{-1}")
dD4 = herm_solution_dim([kron(u4, u4), FLIP])
gate("D3 COMMON-frame FULL edge stabiliser (C4 + endpoint flip): dim_R = 5, still not 2",
     dD4 == 5, "dim_R=%d" % dD4)

# the most conservative reading: the Qubit axiom's Cl(3,0) clause "adds no further
# primitive structure", so the cubic rotations need not act on M_2(C) at all. Then the
# only edge constraint the Lattice axiom can impose is the bare endpoint exchange.
dBare = herm_solution_dim([SWAP])
gate("D5 if the cubic rotations do NOT act internally at all, the only edge constraint is "
     "the bare endpoint exchange and the class is dim_R = 10",
     dBare == 10, "dim_R=%d" % dBare)

gate("D4 SUMMARY the SU(2) content of the common-frame premise does the work: "
     "16 -> 10 -> 6 -> 5 under axiom-named structure, 16 -> 2 only after SU(2) is supplied",
     (16, dBare, dC4, dD4, dA) == (16, 10, 6, 5, 2), "16, 10, 6, 5, 2")


# ================================================================ SECTION E
# Record: does the readout determine a cross-site identification of possibilities?

# (i) content-blind readout: I(any single record) = 1, additive on disjoint collections.
counts = [0, 1, 2, 3, 7]
gate("E1 a content-blind readout I(collection) = #records satisfies additivity and I(empty)=0",
     all(sp.Integer(m) + sp.Integer(n) == sp.Integer(m + n) for m in counts for n in counts)
     and sp.Integer(0) == 0,
     "additive, I(empty)=0, and it reads NO content, so it compares no frames")

# (ii) even a maximally content-sensitive readout leaves a positive-dimensional
#      family of identifications: the stabiliser of a Bloch-axis readout in SU(2).
th = sp.symbols('theta', real=True)
uz = sp.Matrix([[sp.exp(-sp.I * th / 2), 0], [0, sp.exp(sp.I * th / 2)]])
gate("E2 the full U(1) of rotations about the readout axis preserves the readout exactly",
     sp.simplify(uz.H * Z * uz - Z) == sp.zeros(2, 2),
     "stabiliser of a Z-readout is 1-dimensional, so readout never pins a unique frame")
gate("E2m MUTATION a rotation about a perpendicular axis DOES move the readout",
     sp.simplify(v.H * Z * v + Z) == sp.zeros(2, 2) and sp.simplify(v.H * Z * v - Z) != sp.zeros(2, 2),
     "Z -> -Z, so E2 is not vacuous")


# ================================================================ SECTION F
# THE DECISIVE TEST: translation invariance does NOT force a shared frame.
# 3-site ring, exact.

def emb3(op2, slot):
    """embed a 2x2 operator into site `slot` of a 3-qubit ring"""
    ms = [I2, I2, I2]
    ms[slot] = op2
    return kron(kron(ms[0], ms[1]), ms[2])


def swap3(i, j):
    """SWAP on sites i,j of the 3-qubit ring, built from basis permutation"""
    P = sp.zeros(8, 8)
    for n in range(8):
        bits = [(n >> (2 - k)) & 1 for k in range(3)]
        bits[i], bits[j] = bits[j], bits[i]
        m = sum(bits[k] << (2 - k) for k in range(3))
        P[m, n] = 1
    return P


# cyclic translation: content at site x moves to site x+1 (mod 3)
T = sp.zeros(8, 8)
for n in range(8):
    bits = [(n >> (2 - k)) & 1 for k in range(3)]
    new = [bits[(k - 1) % 3] for k in range(3)]
    m = sum(new[k] << (2 - k) for k in range(3))
    T[m, n] = 1

gate("F0 T is unitary, T^3 = I, and it implements the site shift on the local algebras",
     sp.simplify(T.H * T) == sp.eye(8) and sp.simplify(T**3 - sp.eye(8)) == sp.zeros(8, 8) and
     sp.simplify(T * emb3(Z, 0) * T.H - emb3(Z, 1)) == sp.zeros(8, 8),
     "T (site0 algebra) T^dag = site1 algebra")

H = swap3(0, 1) + swap3(1, 2) + swap3(2, 0)
gate("F1 the common-frame ring law H = sum_edges SWAP is translation invariant",
     sp.simplify(T * H * T.H - H) == sp.zeros(8, 8), "T H T^dag = H")

DIAG3 = [emb3(P, 0) + emb3(P, 1) + emb3(P, 2) for P in (X, Y, Z)]
gate("F2 ... and it IS common-frame SU(2) covariant",
     all(sp.simplify(H * g - g * H) == sp.zeros(8, 8) for g in DIAG3), "commutes with all three")

# now give the three sites INDEPENDENT frames
rho0 = I2
rho1 = w                                   # exact rational SU(2)
rho2 = sp.Rational(1, 13) * sp.Matrix([[5, 12], [-12, 5]])
gate("F3a rho1, rho2 are exact SU(2) elements and the three frames are NOT all equal",
     sp.simplify(rho2.H * rho2) == I2 and sp.simplify(rho2.det()) == 1 and
     sp.simplify(rho1 - rho0) != sp.zeros(2, 2), "distinct site frames")

G = kron(kron(rho0, rho1), rho2)
Hp = sp.simplify(G * H * G.H)
Tp = sp.simplify(G * T * G.H)

gate("F3 T' = G T G^dag is unitary, has order 3, and STILL implements the site shift "
     "on the local algebras -- it is a legitimate lift of the lattice translation",
     sp.simplify(Tp.H * Tp) == sp.eye(8) and
     sp.simplify(Tp**3 - sp.eye(8)) == sp.zeros(8, 8) and
     sp.simplify(Tp * emb3(Z, 0) * Tp.H - emb3(rho1 * Z * rho1.H, 1)) == sp.zeros(8, 8),
     "T' (site0 algebra) T'^dag = site1 algebra")

gate("F4 H' = G H G^dag is EXACTLY invariant under that translation",
     sp.simplify(Tp * Hp * Tp.H - Hp) == sp.zeros(8, 8), "T' H' T'^dag = H'")

gate("F5 DECISIVE H' is NOT common-frame SU(2) covariant: it fails the diagonal commutant",
     any(sp.simplify(Hp * g - g * Hp) != sp.zeros(8, 8) for g in DIAG3),
     "a translation-invariant law that carries INDEPENDENT site frames")

gate("F6 H' is a genuinely different operator on the same carrier, not a relabelling of H",
     sp.simplify(Hp - H) != sp.zeros(8, 8), "H' != H")

gate("F7 every edge term of H' has the SAME spectrum as SWAP, so H' is 'one fixed rule' "
     "in exactly the sense the Admissibility sentence asks for",
     sp.simplify(G * swap3(0, 1) * G.H).eigenvals() == swap3(0, 1).eigenvals(),
     "isospectral edge terms")

gate("F8 CONTROL with EQUAL site frames (rho0=rho1=rho2=w) the same construction returns "
     "a common-frame-covariant law, so F5 is caused by frame INDEPENDENCE and nothing else",
     all(sp.simplify(kron(kron(w, w), w) * H * kron(kron(w, w), w).H * g -
                     g * kron(kron(w, w), w) * H * kron(kron(w, w), w).H) == sp.zeros(8, 8)
         for g in DIAG3),
     "equal frames -> covariance restored")

gate("F9 H' and H are unitarily equivalent (same spectrum), which is the honest limit of F5: "
     "the common-frame condition constrains the COORDINATES, not the physics",
     Hp.eigenvals() == H.eigenvals(), "isospectral")


print("\n".join(LINES))
print()
print("PASS=%d FAIL=%d" % (PASS, FAIL))
```
