# Foundation Revision PROPOSAL (Lattice / Quantum / Record + primitives)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-20 (panel date); finalized 2026-06-21.
**Type:** meta / governance proposal.
**Status:** `hypothetical_axiom_status` — **PROPOSAL ONLY**. `proposal_allowed=false`.

## Proposal status (read first)

This file is a **proposal for the owner's governance decision**, not an adoption.

- It does **not** edit `docs/MINIMAL_AXIOMS_2026-06-05.md` (the canonical axiom
  memo) or `docs/audit/data/axiom_premise_nodes.json` (the machine registry).
  Editing either of those surfaces **is** adoption; both were left untouched and
  the working tree shows no diff against them.
- The **owner** plus the **independent audit lane** are the **sole authority** to
  adopt any wording below. Nothing here sets, predicts, or estimates an audit
  verdict, and nothing here promotes any downstream theory surface.
- Everything below is `hypothetical_axiom_status`. Adopt nothing without explicit
  owner approval recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md` and the
  machine registry, and without independent audit-lane review.
- **One item (P2) is a decision REVERSAL,** not housekeeping: it un-adopts the
  logged 2026-06-09 owner approval of `kinetic_isotropy_primitive`. See §5.

**Drives from:** the clean first-principles panel
(`docs/INCUMBENT_AXIOMS_PRIMITIVES_CLEAN_FIRST_PRINCIPLES_PANEL_2026-06-20.md`,
10/10 `needs_revision`) and the verbatim incumbent statements judged there.
**Re-checked by** four adversarial lenses (operator-algebras; lattice-gauge;
GR/arrow + axiomatic-QFT; philosopher-of-physics), all returning
`revision_sound_with_notes`; their demanded fixes are applied below and itemized
in §12.
**Current wordings corrected against:** `docs/MINIMAL_AXIOMS_2026-06-05.md`
(Lattice/Quantum/Record), `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` (P1),
`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (P2),
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (P3).
**Full working draft:**
`.claude/science/physics-loops/foundation-revision-proposal/DRAFT_revised_language.md`.

---

## 0. Drafting principles (stated, then used everywhere below)

1. **Non-circularity of an axiom.** An axiom must not *use* structure it
   disclaims supplying. Every object a statement consumes (decomposition,
   conjugation, sector label, metric) must be supplied — by the same statement,
   another posit, or a flagged open gate — never disclaimed-while-used.
2. **Single-datum purity of a primitive.** A primitive is one narrow datum
   carrying **no** dynamical, selector, renormalized, or empirical content, and
   is **not** a consequence of the other posits.
3. **Theorems are not premises.** A statement that is a *theorem* of a richer
   structure (paradigmatically CPT, a theorem of Lorentz-invariant local QFT)
   must not be posited as a premise. Name the **bare object** (here: an
   antiunitary `K`) and posit only its **existence**.
4. **No smuggling.** Any irreversibility/arrow, emergent time axis, evolution
   law, central decomposition, or conjugation that is *used* must be **explicitly
   posited or flagged as a required open gate**.
5. **Weakest sufficient change.** Prefer the minimal edit. Keep what passed: the
   Lattice core, the `M_2(C)` carrier core, P1 in full, and finite Record
   additivity.

These are restated as general policy criteria in §9.

---

## 1. A1 LATTICE — PASSES; ANNOTATE (no demotion)

**Tier:** axiom (unchanged).
**Objection resolved (panel A1):** A1 passes but is silently over-cited
downstream as the isotropy source. Nearest-neighbor cubic adjacency supplies the
cubic `O_h` / hyperoctahedral `B_3` point group **and** an `L1` graph metric —
**not** continuous rotational isotropy and **not** "no metric". Downstream rows
must not cite A1 for continuous spatial isotropy `a_x=a_y=a_z`, a Lorentz
statement, or a kinetic-form ratio.

**OLD** (`docs/MINIMAL_AXIOMS_2026-06-05.md`, "Lattice"):

> The site set is `Z^3` with standard translation action and nearest-neighbor
> cubic adjacency. Finite-range locality means finite support or finite
> graph-distance range with respect to this lattice when a local expression is
> specified.
>
> This axiom supplies the discrete site set and local adjacency notion. It does
> not supply a dynamics, boundary condition, metric scale, lattice spacing,
> continuum or infrared limit, causal cone, probabilistic independence rule, or
> physical unit conversion.

**NEW (paste-ready):**

> ### Lattice
>
> The site set is `Z^3` with the standard translation action and
> nearest-neighbor cubic adjacency. Finite-range locality means finite support
> or finite graph-distance range with respect to this lattice when a local
> expression is specified.
>
> This axiom supplies exactly three things and nothing more: (i) the discrete
> site set `Z^3` with its translation action; (ii) the **combinatorial
> point-group symmetry** of that adjacency — the cubic group `O_h` on the site
> stencil, equivalently the hyperoctahedral group `B_3` (the discrete
> permutation-and-sign symmetry of the three axes), which is the discrete
> residue of, **not** a substitute for, continuous rotational isotropy; and
> (iii) the **combinatorial `L1` graph metric** induced by edge adjacency. The
> three coordinate directions are interchangeable **as graph axes** (a discrete
> `B_3` statement); this is *not* continuous spatial isotropy and is *not* an
> emergent-Lorentz statement.
>
> This axiom does **not** supply: a dynamics, a boundary condition, a
> dimensionful metric scale, a lattice spacing, a continuum or infrared limit,
> a causal cone, a probabilistic-independence rule, a physical unit conversion,
> **continuous rotational isotropy**, or any **emergent-symmetry** result.
>
> The `L1` graph metric supplied here is `O_h`-invariant but **not**
> `SO(3)`-invariant: its unit ball is the `L1` diamond, not a round ball, so it
> is **anisotropic at the continuum level** and supplies **no** rotation-invariant
> distance. No row may cite this axiom for a rotational-distance claim.
>
> **Downstream-citation guard.** No downstream row may cite this axiom as the
> source of continuous spatial isotropy `a_x = a_y = a_z` (in the metric, not
> the graph, sense), of a relativistic/Lorentz statement, or of a kinetic-form
> ratio. Those are separate posits or derivations (see the kinetic-form
> condition, §5, and the required dynamics/time gate, §8).

**Why this is the weakest change.** Operative content (`Z^3`, translations,
cubic adjacency, finite-range locality) is byte-for-byte preserved. The only
additions name the two structures the adjacency *does* hand you (`O_h`/`B_3`;
`L1` graph metric, with its `O_h`-not-`SO(3)` anisotropy made explicit) and add
a citation guard. Pure annotation; uses nothing it disclaims (principle 1, 5).

---

## 2. A2 QUANTUM — PASSES; AMEND (keep `M_2(C)` at axiom grade)

**Tier:** axiom (unchanged) for the `M_2(C)` carrier; **relocate** the `Cl(3,0)`
real-algebra reading to a labelled downstream identification.
**Objection resolved (panel A2):** keep `M_2(C)`, but "`= Cl(3,0)` in its
real-algebra reading" is not inert: the **real** Clifford reading silently
supplies an `so(3)~su(2)` bivector generator set, a pseudoscalar/chirality
element, and a real-form/conjugation that A3 later reuses. Also the scalar field
(`R` vs `C`) must be declared so "`i`" is owned.

**OLD** (`docs/MINIMAL_AXIOMS_2026-06-05.md`, "Quantum"):

> At each site `x`, the primitive physical local degree of freedom is one qubit;
> equivalently, the primitive one-site operator algebra is
> `A_x ~= M_2(C)`, equivalently `Cl(3,0)` in its real-algebra reading.
>
> This axiom supplies the one-site algebraic carrier. It does not supply a
> dynamics, composition theorem beyond the named lattice placement, measurement
> instrument, Born rule, species identification, gauge group, particle content,
> or physical observable bridge.

**NEW (paste-ready):**

> ### Quantum
>
> At each site `x`, the primitive physical local degree of freedom is one
> qubit; equivalently, the primitive one-site operator algebra is the complex
> matrix algebra `A_x ~= M_2(C)`, taken over the **complex scalar field `C`**
> (the unit `i` is the complex unit of `M_2(C)`).
>
> This axiom supplies **only** the one-site algebraic carrier `M_2(C)` and its
> complex scalar field. It does **not** supply: a dynamics; a composition
> theorem beyond the named lattice placement; a distinguished set of generators
> or a preferred basis; a chirality / pseudoscalar element; a real form,
> conjugation, or antiunitary structure; a measurement instrument; a Born rule;
> a species identification; a gauge group; particle content; or a physical
> observable bridge.
>
> **Labelled downstream identification (NOT part of the axiom).** `M_2(C)` is
> isomorphic, as a complex algebra, to the complexified Clifford algebra
> `Cl(3,0) (x) C`; under a *chosen* real form one may read the carrier as the
> real algebra `Cl(3,0)`. That real-Clifford reading additionally distinguishes
> an `so(3) ~ su(2)` bivector generator set, a pseudoscalar/chirality element,
> and a real-structure conjugation. **None of that extra structure is supplied
> by this axiom.** Any row that uses Clifford generators, chirality, a real
> form, or an antiunitary built from them must cite that identification
> explicitly as a separate, labelled step and own the choices it makes
> (canonical landing: `docs/A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md` and the
> per-site Cl(3) uniqueness note), not draw them from this axiom.

**Why this is the weakest change.** The `M_2(C)` carrier (what passed) is
preserved and sharpened: the scalar field is declared `C`, closing the "`i`"
ambiguity, while the antilinear/real structure is explicitly listed as **not**
supplied (so declaring `C` does not covertly bless `K`). The single substantive
move demotes the `Cl(3,0)` clause to a labelled downstream identification and
enumerates the three structures (generators, chirality, conjugation) the real
reading would otherwise smuggle. Removes the silent supplier A3 reused
(principle 1); makes "`i`" owned (principle 4).

---

## 3. A3 RECORD — FAILS (10/10 mis-tiered); SPLIT into A3a (axiom) + A3b (conditional)

The load-bearing repair. The incumbent Record welds a clean finite-additivity
valuation (legitimate, axiom-class) to a "K/CPT orbit of the realized central
sector" **selector** that fails four ways. We split it.

**OLD** (`docs/MINIMAL_AXIOMS_2026-06-05.md`, "Record"):

> A record is the durable registration of the realized outcome.
>
> Given a readout context with a finite central-sector decomposition and a fixed
> `K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized
> central sector. For any finite pairwise-disjoint collection of records, the
> scalar readout `I` is finitely additive, with `I(empty)=0`.
>
> Durable means fixed once registered: the recorded outcome does not change. A
> record supplies no readout context, decomposition, `K`/CPT structure,
> sector-generation rule, weighting, normalization, probability,
> measurement/decoherence dynamics, time metric, within-sector data, or
> occupancy rule.

**Objections resolved (panel A3, 10/10 fail):**
- **(i) Disclaim-while-use.** The selector *uses* a finite central-sector
  decomposition and a fixed conjugation in the sentence that disclaims them.
- **(ii) No nontrivial center exists yet.** `M_2(C)` is a **factor** (trivial
  center); its lattice tensor product (and the UHF/hyperfinite inductive limit)
  is a factor too. There are **no** nontrivial central sectors absent an
  unsupplied gauge/coarse-graining/superselection map.
- **(iii) CPT illegitimately imported.** "CPT" is a **theorem** of
  Lorentz-invariant local QFT, not a primitive (and this repo treats CPT as a
  separate `bounded_theorem` stretch). The bare object must be a neutral
  antiunitary `K` with stated existence only.
- **(iv) Smuggled arrow.** "durable = fixed once registered" smuggles
  irreversibility / an arrow of time into the foundation.

### 3a. A3a RECORD-VALUATION — the part that STAYS an axiom

**Tier:** axiom.

**NEW (paste-ready):**

> ### Record (valuation)
>
> A **record** is a registered outcome, drawn from a collection of registered
> events closed under **finite disjoint union** and equipped with a distinguished
> empty record `0` (an orthocomplemented poset / generalized Boolean ring of
> disjoint records — **not** a full Boolean algebra; complementation/negation is
> deliberately **not** required, as finite additivity over disjoint collections
> does not need it). The framework posits a **scalar readout** `I` on records
> that is **finitely additive over finite pairwise-disjoint collections**:
>
> ```text
>     I(r_1 \/ ... \/ r_n) = I(r_1) + ... + I(r_n)   for pairwise-disjoint r_k,
>     I(0) = 0.
> ```
>
> This axiom supplies **only** the finite-additivity valuation structure of the
> scalar readout. It does **not** supply: a readout context; a sector
> decomposition (central or otherwise); a conjugation or antiunitary; a
> sector-generation rule; weighting; normalization; probability; a
> measurement/decoherence dynamics; a time metric or arrow of time; an
> irreversibility ("durability") claim; within-sector data; or an occupancy
> rule. In particular, **what counts as "the realized outcome"** — the map from
> physical configurations to records — is **not** fixed by this axiom; it is the
> subject of the separate conditional identification (§3b) and depends on the
> required dynamics/time gate (§8).

**Notes.** The clean, durability-free, decomposition-free, conjugation-free
valuation. Genuinely axiom-class (uses nothing it disclaims). "durable" is
**removed**; its irreversibility content relocates to G-ARROW (§8). The
"realized outcome" map is **deferred** to §3b, not disclaimed-while-used. Per
re-check, the carrier was weakened from a full Boolean algebra to the minimum
finite-additivity needs (disjoint-union-closed, with `0`).

### 3b. A3b REALIZED-OUTCOME IDENTIFICATION — derived/conditional, NOT an axiom

**Tier:** derived-result / conditional identification (depends on the
center-producing gate G-SECT, the dynamics/time gate §8, and a supplied realized
configuration).

**NEW (paste-ready):**

> ### Realized-outcome identification (conditional; not an axiom)
>
> **Hypotheses (each must be supplied, none is posited here):**
> 1. a **center-producing coarse-graining / superselection ingredient** `E` that
>    sends the factor algebra of the foundation to an algebra with a **nontrivial
>    center** `Z`, yielding a family of **central sectors** `{s_1, ..., s_m}`
>    (`M_2(C)`, all its finite lattice tensor powers, and their UHF/hyperfinite
>    inductive limit are **factors with trivial center**, so without such a
>    supplied `E` there are **no** nontrivial sectors — this hypothesis is
>    load-bearing). **`E` is not produced by reflection-positive dynamics alone:**
>    a factor's reflection-positive time evolution stays a factor evolution, so
>    `E` requires dynamics **plus** an additional coarse-graining / thermodynamic
>    or large-`N` limit / gauge-constraint / environment-induced-superselection
>    ingredient. That sector-producing ingredient is the sub-gate **G-SECT**
>    (§8), distinct from the bare dynamics gate G-DYN. **The finiteness and the
>    count `m` of `{s_1, ..., s_m}` are themselves part of this supplied
>    hypothesis**, not free corollaries of `K` or of the dynamics; any downstream
>    generation/sector *count* inherits `m` as a carried dependency.
> 2. the existence of a **neutral antiunitary involution** `K` on the carrier
>    (an antilinear `*`-map with `K^2 = +/- 1`) whose existence is *posited as a
>    hypothesis*, **not** identified with CPT and **not** carrying any
>    theorem-strength corollary. **`K` must NOT be silently drawn from the
>    real-structure conjugation that A2 (§2) explicitly withdrew:** any `K` built
>    from Clifford generators / a real form must cite A2's labelled downstream
>    identification and own that choice. Physical identifications of `K` (e.g.
>    with a CPT-like or charge/parity-like operator) are separate, labelled, and
>    audited downstream. The **sign** `K^2 = +1` (real/orthogonal) vs `K^2 = -1`
>    (quaternionic/Kramers) is left open here; the resulting **orbit-size /
>    fixed-sector structure** (orbit size 1 or 2; whether fixed sectors exist) is
>    a **downstream-audited consequence of the sign**, not fixed by this
>    identification.
> 2′. (**K–E compatibility**) `K` **normalizes** the center `Z` produced by `E`
>    and therefore **descends to a well-defined involution on the sector set**
>    `{s_1, ..., s_m}` (so that `K . s_*` is again a sector). Posited at the
>    `K`-on-the-carrier level alone, this descent is **not** automatic; it is an
>    explicit hypothesis the orbit construction uses.
> 3. a **realized configuration** supplied by the physical history (the
>    realized-state slot, §7).
>
> **Conditional conclusion.** Given (1)-(2′)-(3), the **realized outcome** is the
> `K`-orbit of the realized central sector `s_* in {s_1, ..., s_m}`:
> `outcome = { s_*, K . s_* }` (well-defined as a subset of the sector set by
> hypothesis 2′). The scalar readout `I` of §3a is then evaluated on the records
> so identified.
>
> **Status.** This identification is a **conditional/derived result**, not a
> premise. It is *false as stated at the bare-foundation level* (no center
> exists there); it becomes meaningful only once the supplied maps `E`, `K`, and
> the realized configuration exist. It supplies none of `E`, `K`, the sector
> count, weighting, normalization, probability, or within-sector data.

**Notes.** The heart of the split. Everything illegitimate as an axiom is
**retained as a clearly conditional identification with hypotheses exposed**: the
missing center has a named supplier (the center-producing map `E`, via G-SECT —
explicitly **not** RP-dynamics alone); "CPT" → a bare antiunitary `K`, existence
only (principle 3); the selector no longer disclaims-while-uses (principle 1).
Per re-check, three additional hypotheses were exposed: K–E compatibility
(2′, else `{s_*, K.s_*}` is ill-defined), the sector finiteness/count `m` as
supplied (not a free corollary), and an explicit bar on silently reusing A2's
withdrawn conjugation for `K`. Downstream K/CPT-orbit consumers (e.g.
`docs/P2_KCPT_ORBIT_TEMPORAL_FACTOR_NO_GO_2026-06-06.md`) must re-cite A3b
(conditional) and carry `E`/`K`/realized-config as dependencies.

---

## 4. P1 SCALE-REFERENCE — PASSES CLEANLY (unanimous); KEEP, optional hygiene

**Tier:** primitive (unchanged).
**Objection resolved (panel P1):** none required — P1 passes cleanly and
unanimously. Optional hygiene only: name the anchor abstractly so the
`= M_Pl` identification (a gravity self-consistency `a = l_P`) is a separate open
gate, not part of the primitive.

**OLD** (`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`):

> The framework takes exactly one dimensionful reference: a scale that converts
> the framework's lattice-natural units to physical units. The chosen reference
> is the Planck mass scale, `a^{-1} = M_Pl`.
>
> This is a units conversion, not a physics axiom. It carries zero dimensionless
> content [...].

**NEW (paste-ready, OPTIONAL):**

> The framework takes exactly one dimensionful reference: a single inverse
> length / mass scale `a^{-1} = M_0` that converts the framework's
> lattice-natural units to physical units. `M_0` is an **abstract anchor**; the
> *identification* `M_0 = M_Pl` (equivalently `a = l_Planck`) is **not** part of
> this primitive — it is a separate open gravity self-consistency gate and is
> recorded there, not here.
>
> This is a units conversion, not a physics axiom. It carries zero dimensionless
> content: no mass ratio, coupling, mixing angle, phase, selector, readout
> bridge, or empirical fit is supplied by it, and it does **not** assert
> `a / l_Planck = 1` as a derived theorem.

**Notes.** Strictly optional. The existing note already disclaims `a/l_P = 1`;
this only makes the abstract/identified split explicit at declaration. If the
owner prefers continuity, the current wording is acceptable as-is — hygiene, not
a defect repair. Re-check note: confirm no downstream row cites `a^{-1} = M_Pl`
as a load-bearing *number*; the rename is inert only if the equality was never
load-bearing (consistent with the note's existing `a/l_P ≠ 1` disclaimer).

---

## 5. P2 KINETIC-ISOTROPY — FAILS (10/10 mis-tiered); RE-TIER (demote from primitive)

**Tier change:** from **approved primitive** → **admitted input** (Tier-A
admission), with an explicit **alternative** of a **derived IR-fixed-point
target**. Either way `c_t = c_s` leaves the axiom-premise registry.

**THIS IS A DECISION REVERSAL.** `AXIOM_MINIMALITY_POLICY.md` §6 (entry
2026-06-09) and `axiom_premise_nodes.json` both record an explicit **owner
approval** of `kinetic_isotropy_primitive` *as a primitive*, on the ground that
`c_t = c_s` is "a dimensionless **structural** ... of the same category as cubic
adjacency ... **not** dimensionless **dynamical** content." This proposal asserts
the **opposite**. Adopting it **reverses** that 2026-06-09 owner approval and
amends the registry; it cannot land without the owner reversing the approval and
the audit lane re-auditing. Presented here as a proposed reversal for owner
decision, not as housekeeping (`proposal_allowed=false`).

**OLD** (`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`):

> The framework takes one structural graining fact: the emergent evolution tick
> is grained on the same footing as the spatial lattice edge. Concretely, the
> matter kinetic normalization is space-time isotropic, `c_t = c_s` [...]. This
> is a structural statement about the regulator geometry, the time-direction
> analogue of the `LATTICE` axiom's spatial **cubic adjacency** `a_x = a_y =
> a_z`. It carries no dimensionless dynamical content [...].

**Objections resolved (panel P2, 10/10 fail):**
- **(a)** `c_t = c_s` is the emergent-Lorentz **answer** (isotropic light cone),
  asserted as a free datum (the repo's own note calls it "itself the
  emergent-Lorentz output"; the magnitude chain lives in the Euclidean branch,
  `docs/P2_EUCLIDEAN_VS_LORENTZIAN_FORK_2026-06-05.md`). A primitive may not be a
  derivation answer (principle 2).
- **(b)** On a lattice it is a **renormalized** tuning condition:
  `xi_R != xi_bare`, related by interaction-dependent **Karsch coefficients** —
  i.e. dimensionless **dynamical** content, not kinematic graining.
- **(c)** It presupposes an emergent **time direction** nothing supplies
  (routed to G-TIME, §8).

**NEW (paste-ready) — primary route: ADMITTED INPUT (proposed registry-of-record):**

> ### Kinetic-form anisotropy condition (admitted input — Tier-A; not a primitive)
>
> **Admitted condition.** On the regulated theory with an emergent time
> direction (the emergent time axis is supplied by gate **G-TIME**, with **G-DYN**
> as its upstream supplier; §8) — taken in the Euclidean / Osterwalder-Schrader
> branch where `c_t` and `c_s` are defined (the Euclidean tick vs Lorentzian
> time, cf. `docs/P2_EUCLIDEAN_VS_LORENTZIAN_FORK_2026-06-05.md`; `xi_R = 1` is
> the bridge condition between the branches) — the **renormalized** space-time
> kinetic-form anisotropy is tuned to isotropy,
>
> ```text
>     xi_R = c_t / c_s = 1   (renormalized, not bare).
> ```
>
> **Why this is an admitted input, not a primitive.** (i) `c_t = c_s` is the
> emergent-Lorentz output (an isotropic matter light cone); positing the answer
> as a free datum is circular, so it is **not** primitive-class. (ii) On a
> lattice the bare and renormalized anisotropies differ
> (`xi_R != xi_bare`, related by interaction-dependent Karsch coefficients), so
> fixing `xi_R = 1` is a **dimensionless dynamical tuning condition**, i.e.
> exactly the dynamical content a primitive may not carry. (iii) It presupposes
> an emergent time direction, supplied by gate G-TIME (§8), not by this
> statement. It is therefore registered as a **Tier-A admitted input** (in
> `docs/audit/data/tier_a_admissions.json`), **not** as an axiom-premise
> primitive: dependents chain-satisfy only at `retained_bounded` until the
> condition is retired by a retained derivation.
>
> **Carried residual (stated to match the repo's own B4 theorem).** `xi_R = 1`
> is a **tuning condition to reach the hypercubic-symmetric (`B4`) surface**: the
> bare anisotropy must be set so the renormalized value lands at `1`. On that
> surface the marginal anisotropy is **symmetry-protected** — the repo's own
> `EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`
> shows one-loop `Sigma_t = Sigma_s` by exact axis relabeling, so the leading
> Lorentz violation is pushed to a Planck-suppressed **dimension-6** operator.
> Hence the carried residual is **(a)** the one-time tuning-to-the-surface, and
> **(b)** the dimension-6 / non-`B4`-symmetric naturalness question — **not**
> a claim of generic marginal radiative instability.
>
> **Explicitly dropped claims.** The phrases "free structural datum" and
> "analogue of cubic adjacency" are **withdrawn**: cubic adjacency is kinematic
> and interaction-independent (axiom A1), whereas `xi_R = 1` is a renormalized
> dynamical condition. The two are **not** the same category.

**NEW (paste-ready) — ALTERNATIVE route: DERIVED TARGET (if the owner prefers):**

> ### Emergent kinetic isotropy (derived IR-fixed-point target; open)
>
> **Target.** `xi_R = c_t/c_s -> 1` as an **infrared fixed-point** property of
> the emergent dynamics (supplied by §8): isotropy of the matter light cone is
> a *consequence* to be derived (emergent Lorentz invariance in the IR), not an
> input. Until a retained derivation closes it, the IR isotropy of the matter
> kinetic form is an **open derived target** carrying the same tuning-to-surface
> / dimension-6 residual; rows that need `xi_R = 1` cite this target as an open
> dependency, not as an axiom or primitive.

**Notes.** `c_t = c_s` **leaves the axiom-premise registry** on either route; the
approved-primitive count drops by one. The **admitted-input** route is proposed
as registry-of-record because it keeps the magnitude/Lorentz chains usable
(`retained_bounded` rather than fully open); the **derived-target** route is
cleaner physics but leaves dependents open. The two routes carry different audit
semantics, so the owner must select one. Both (i) state `xi_R` is renormalized,
(ii) carry the corrected B4-consistent residual, (iii) drop "free datum /
cubic-adjacency analogue", (iv) route emergent-time through G-TIME.

---

## 6. Where spatial isotropy and the kinetic form now live (bookkeeping; no new posit)

After §1 and §5: spatial axis-interchange is a **discrete `B_3` graph fact**
(axiom A1, kinematic); the **continuous** spatial isotropy `a_x=a_y=a_z` and the
**space-time** kinetic-form isotropy `xi_R=1` are **not** axioms — the former is
an emergent/derived statement, the latter the admitted/derived condition of §5.
No row may conflate the three. Adds no premise.

---

## 7. P3 REALIZED-STATE — DISAMBIGUATE (consolidate the guard; own the commitment)

**Tier:** primitive (retained).
**Objection resolved (panel P3):** judged **bare**, P3 drew a 0-pass/10-concern
reading. Fix: make the statement **self-sufficient on a bare reading**.
*Diagnosis correction (per re-check):* the counterfactual-test guard is **not**
absent from the canonical note — it already lives in its `## The Primitive`
("no quoting a number that would differ ...") and `## What This Declares`
blocks. So the accurate framing is **"consolidate and make explicit"**, not
"fold in a missing guard." The genuinely **new** content is (a) the explicit
**one-world / actualization** (initial/boundary-condition) commitment, and (b)
the **cross-link to A3a/A3b** disambiguating the two senses of "realized" —
neither stated outright before.

**OLD** (`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`, "The Primitive"):

> The laws do not pick the state; the world does, among the states the laws
> permit.
>
> Derivations may evaluate at the realized state, pointwise.
>
> Nothing more is supplied: no averaging over alternatives, no typical or
> generic claim, and no quoting a number that would differ had another
> law-admissible state been realized.
>
> The past hypothesis is a separate, stronger input.

**NEW (paste-ready):**

> ### Realized-state (primitive)
>
> The laws do not pick the state; the world does, among the states the laws
> permit. This primitive posits **one** datum: a single law-admissible
> **realized state** is supplied by the physical history (a one-world /
> actualization commitment — an initial/boundary-condition input that the
> state-blind laws cannot themselves supply). Derivations may **evaluate at the
> realized state, pointwise**.
>
> **Counterfactual-test guard (part of the primitive, not external prose).** A
> quoted number is a derivation output **only if** it is invariant over the
> entire law-admissible family of realized states. **Any quantity that would
> differ had another law-admissible state been realized is registered data, not
> derivation output.** Equivalently: no averaging over alternatives; "typical"
> and "generic" are **banned** as specialization predicates; no preferred or
> default state (the maximal-symmetry state is never "the natural input").
>
> **What it does not supply.** No state, state-selection rule, measure,
> weighting, probability rule, typicality/genericity claim, preferred or default
> state, normalization rule, or state-contingent value.
>
> **Sense disambiguation (cross-link).** "Realized **state**" here is the
> supplied physical configuration of hypothesis (3) of the realized-outcome
> identification (§3b). It is **distinct** from the "realized **outcome**" of
> §3b, which is the *recorded event* (`K`-orbit of the realized central sector).
> The two uses of "realized" are not interchangeable.
>
> **Stronger input held out.** The **past hypothesis** (a specialness /
> atypicality claim about the realized history) is a strictly stronger input of
> exactly the class this primitive's guard forbids; it is **not** housed here and
> remains the named residual of
> `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`
> (routed to gate G-ARROW, §8).

**Notes.** Content unchanged; the guard is **consolidated** into one
self-contained block (it already existed in the canonical note), and the two
genuinely new pieces are made explicit. *Boundary-vocabulary watch:* P3 names the
realized state an "initial/boundary-condition input" while the **past
hypothesis** (also boundary-condition language) is held **out** — the distinction
is the single supplied datum (allowed) vs a specialness/atypicality *claim* about
it (forbidden here → G-ARROW). Shared vocabulary is intentional but the two are
not the same input. P3 stays a primitive: so guarded it carries no contingent
content (principle 2).

---

## 8. SYSTEM gap — DYNAMICS + EMERGENT TIME: a REQUIRED OPEN GATE (not a new axiom)

**Tier:** **open-gate** (explicitly flagged required gate), **not** an axiom and
**not** a primitive.
**The gap (panel SYSTEM, under-completeness):** a dynamics / time-evolution
(transfer matrix / Hamiltonian / action with reflection positivity) **and** an
emergent time axis are *presupposed* by P2 (`c_t`) and by A3b (the
center-producing map; the arrow behind "durable") but posited **nowhere**.

**Decision: FLAG it as a required open gate, do NOT add a dynamics axiom.**
1. **Minimality / policy.** A dynamics axiom is far heavier than the gap requires
   and would import selector/dynamical content. The foundation already lists
   "arrow, measurement, decoherence, record-production dynamics" and
   "source/action" as **open gates outside the axioms**
   (`MINIMAL_AXIOMS_2026-06-05.md`). The binding `AXIOM_MINIMALITY_POLICY.md`
   §1/§4 mandates: when a lane needs an extra axiom, **do not add it** — record a
   flagged decision and land a boundary note. Adding a dynamics axiom would
   **contradict** the policy.
2. **Already a downstream conditional cluster.** The repo *derives* evolution
   from supplied transfer data: the reflection-positivity 2-step transfer matrix
   feeds the single-clock generator and `U(t)=exp(-itH)`; the single-clock note
   itself states "**the axis is a premise, not a derivation**"; Gate B dynamics
   is an explicit `open_gate`.
3. **Anti-smuggling (principle 4).** Flagging stops the silent presupposition;
   P2 (§5) and A3b (§3b) now name the gate as an explicit dependency, and the
   arrow removed from Record (§3a) lands here, owned.

**PROPOSED gate flag (paste-ready) — add to the "Open Gates" section, NOT to the axiom list:**

> ### Required open gate: dynamics + emergent time axis (flagged, not an axiom)
>
> The foundation (axioms A1, A2, A3a; primitives P1, P3) supplies **no**
> dynamics and **no** time. The following are **required open gates**, on which
> several downstream statements are explicitly conditional; they are **flagged
> here so they are never silently presupposed**, and they are **not** promoted to
> axioms or primitives:
>
> - **(G-DYN) Dynamics / time-evolution.** A law of evolution — an action, a
>   transfer matrix, or a Hamiltonian — with **reflection positivity (RP)**. RP
>   gives a **positive transfer matrix** and hence a **self-adjoint transfer
>   generator** and a Euclidean **semigroup** `T^n` (`T = exp(-a H)`, `H` bounded
>   below). It does **not** by itself hand you a continuous real-time unitary
>   group `U(t) = exp(-i t H)`: that requires the further
>   reconstruction / analytic-continuation (Wick-rotation / OS-reconstruction)
>   step, which is **itself an open dependency**, not automatic. RP-dynamics is
>   **time-symmetric** (the unitary evolution carries **no** arrow; the arrow is
>   quarantined in G-ARROW). Current status: conditional/derived cluster
>   (reflection-positivity transfer-matrix and single-clock evolution notes),
>   **not** an axiom.
> - **(G-SECT) Center-producing coarse-graining / superselection.** The map `E`
>   that produces a **nontrivial center** (the finite central-sector family
>   `{s_1, ..., s_m}` and its count `m`) required by the realized-outcome
>   identification (§3b, hypothesis 1). **This is NOT supplied by G-DYN alone:**
>   reflection-positive evolution of a **factor** stays a factor evolution, so a
>   nontrivial center additionally needs a coarse-graining / thermodynamic or
>   large-`N` limit / gauge constraint / environment-induced-superselection
>   ingredient. G-SECT is named **separately** from G-DYN precisely so that
>   "dynamics supplies `E`" cannot stand unqualified. Current status: open
>   (no nontrivial center exists at the bare-foundation level), **not** an axiom.
> - **(G-TIME) Emergent time axis.** A distinguished evolution direction
>   ("time"), emergent from (G-DYN) (e.g. the single-clock codimension-1
>   evolution). This is the time direction presupposed by the kinetic-form
>   condition `xi_R = c_t/c_s` (§5). **It is currently UNDISCHARGED:** an emergent
>   **single** time axis (codimension-1, one clock) is itself a nontrivial
>   selection that the gate **names but does not establish** — the repo's own
>   single-clock note states "**the axis is a premise, not a derivation**." The
>   gate must not be read as already-supplied. Current status: emergent /
>   axis-conditional and undischarged, **not** an axiom.
> - **(G-ARROW) Arrow / irreversibility.** The "durability" of records — the
>   time-asymmetric claim that a registered outcome does not change — is a
>   statement about an **arrow of time**, not part of the Record valuation
>   (§3a). The arrow lives in the **initial condition** (past hypothesis), not in
>   the time-symmetric dynamics of G-DYN. It is held here as a required gate and
>   remains the residual of the past-hypothesis / arrow note
>   (`docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`).
>   It is **not** an axiom and is **not** supplied by P3.
>
> Any row that uses an evolution law, an emergent time direction, a
> superselection/coarse-graining (center-producing) map, or record durability
> must cite the relevant gate (G-DYN / G-SECT / G-TIME / G-ARROW) as an explicit
> open dependency.

**Notes.** Flag, do not axiomatize. Four sub-gates (dynamics G-DYN,
center-producing coarse-graining G-SECT, time axis G-TIME, arrow G-ARROW) absorb
exactly the smuggled content — `c_t` (via G-TIME), the center-producing map `E`
(via G-SECT, split from G-DYN because RP keeps a factor a factor), and Record's
"durable" (via G-ARROW). Per re-check: G-DYN no longer over-claims a continuous
real-time `U(t)` from bare RP, G-SECT is separated from G-DYN, G-TIME is flagged
undischarged, and G-ARROW correctly locates the arrow in the initial condition.

---

## 9. First-principles criteria the minimality policy should encode

A premise surface is admissible iff every member satisfies the criterion for its
tier:

1. **Axiom non-circularity (no disclaim-while-use).** An axiom may not consume
   structure it disclaims supplying. Every object a statement *uses*
   (decomposition, conjugation, metric, sector label, basis, generator set,
   ordering) must trace to a supplier inside the premise surface or a flagged
   gate. *Test:* list every object used; each must have a supplier.
2. **Primitive single-datum purity.** A primitive is **one** narrow datum
   carrying no dynamical/selector/renormalized/empirical content, and is not a
   consequence of the other posits. *Test:* (a) derivable from the rest ⇒ derived,
   not primitive; (b) requires renormalized (not bare) values ⇒ admitted
   dynamical input; (c) fixes a mass ratio/coupling/angle/phase/count ⇒
   empirical/selector content.
3. **Kinematic vs dynamical classification.** Kinematic / interaction-independent
   structure (lattice geometry, point group, graph metric, algebraic carrier) is
   axiom/primitive-admissible; dynamical / interaction-dependent structure
   (anything that runs under renormalization, any emergent-symmetry output, any
   IR fixed-point property) is **never** a primitive — it is an admitted input
   (Tier-A, bounding) or a derived target. *Test:* does it run/renormalize/emerge
   in the IR?
4. **Theorems are not premises.** A statement that is a theorem of a richer,
   not-yet-established structure may not be posited as a premise. Posit only the
   **bare object** (an antiunitary involution `K`, not "CPT"; a positive transfer
   operator, not a relativistic spectrum-condition theorem) and only its
   **existence**, no theorem-strength corollaries. *Test:* is the named object
   provable elsewhere as a theorem? If yes, replace with bare-object + existence
   hypothesis.
5. **Explicit accounting of arrow / time / dynamics / decomposition / conjugation
   (no smuggling).** Any irreversibility/arrow, emergent time axis, evolution
   law, central/superselection decomposition, or conjugation used anywhere
   downstream must be **either** a stated posit **or** an explicitly flagged
   required open gate. *Test:* grep the downstream corpus for uses of
   time/evolution/durability/sectors/conjugation; each must trace to a posit or a
   flagged gate.
6. **Factor/center honesty.** Do not posit a sector decomposition,
   superselection, or central orbit on an algebra that is a **factor** (trivial
   center, e.g. `M_2(C)` and its lattice tensor product). Such structure requires
   an explicitly supplied center-producing map. *Test:* is the algebra a factor?
   If yes, any sector talk needs a named supplier.
7. **Weakest sufficient change / minimality of premises.** Prefer the weakest
   admissible repair: prefer a flagged open gate to a new axiom; prefer demotion
   (axiom→primitive→admitted input→derived target) to addition; prefer
   annotation to rewording. Adding a premise is the **last** resort. *Test:*
   enumerate demotion/flag/annotate options before any addition.
8. **Self-sufficiency of a stated premise (bare-reading test).** A premise must
   carry its own load-bearing guards inside its statement. *Test:* judge the
   statement alone, no source note — does it still pass?
9. **Tier provenance and downstream-citation discipline.** Each premise is tagged
   with its tier (axiom / primitive / admitted-input / derived-target /
   open-gate); downstream rows must cite the **correct** tier. An axiom may not be
   cited for content it does not supply (e.g. A1 for continuous isotropy).
   *Test:* for each citation, does the cited premise supply the cited content at
   the claimed tier?

---

## 10. Adoption consequences (if the owner + audit lane adopt)

> These are the downstream status changes that **would** follow adoption. This
> proposal adopts nothing; the audit lane sets all effective statuses.

1. **Registry change (`axiom_premise_nodes.json`).** `kinetic_isotropy_primitive`
   is **removed** from `canonical_ids`/`nodes` and **moved** to
   `tier_a_admissions.json` as a renormalized-anisotropy admission (primary
   route) — **or** recorded as an open derived target (alternative). The
   approved-primitive count drops **3 → 2** (P1, P3 remain). `minimal_axioms`
   source content changes (A1 annotation; A2 amendment; A3 split into A3a axiom +
   A3b conditional).
2. **P2-dependent rows re-tier.** Every row whose only otherwise-clean dependency
   was the kinetic-isotropy primitive (emergent-Poincaré/kinetic-isotropy
   theorem cluster, staggered-Dirac kinetic-class rows, graviton-isotropy rows)
   **loses** its chain-satisfy pass → `retained_bounded` (admitted-input route)
   or open (derived-target route), pending re-audit.
3. **A3b consumers re-audited.** Rows that cited "Record" for the **K/CPT-orbit
   selector** (generation-sector-count usage; determinant/character
   phase-erasure rows leaning on the K/CPT orbit — cf
   `docs/P2_KCPT_ORBIT_TEMPORAL_FACTOR_NO_GO_2026-06-06.md`,
   `docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`)
   must re-cite **A3b (conditional)** and carry `E` (center-producing map, via
   G-SECT), `K` (antiunitary existence), the K–E compatibility hypothesis, the
   sector count `m`, and the realized configuration as explicit dependencies.
   Rows using only finite **additivity** keep citing A3a (axiom) and are
   **unaffected**.
4. **New required-gate dependencies.** Rows using an evolution law, an emergent
   time direction, a center-producing superselection/coarse-graining map, or
   record durability now carry explicit **G-DYN / G-SECT / G-TIME / G-ARROW**
   open-gate dependencies. RP/single-clock notes supply G-DYN/G-TIME
   conditionally; `E` (G-SECT) needs an *additional* coarse-graining/limit/gauge
   ingredient beyond RP; the past-hypothesis/arrow note supplies G-ARROW.
5. **A2 Clifford-reading consumers re-audited.** Rows using Clifford
   generators/chirality/real-form conjugation drawn from "the Cl(3,0) reading of
   A2" must re-cite the labelled downstream identification and own those choices.
   `M_2(C)`-only rows unaffected.
6. **A1 isotropy-citation sweep.** Any row citing A1 as the source of
   **continuous** spatial isotropy or a Lorentz statement must be corrected; A1
   supplies only `B_3`/`O_h` + the (`O_h`-not-`SO(3)`) `L1` graph metric.
7. **Hash-guard re-audit (mechanical).** Editing `MINIMAL_AXIOMS` content
   invalidates prior direct `minimal_axioms` audits via the axiom-premise hash
   guard; all direct dependents re-audited by the independent lane.
8. **Policy update (`AXIOM_MINIMALITY_POLICY.md`).** §6 records removal of
   `kinetic_isotropy_primitive` from primitive class (this **reverses** the
   logged 2026-06-09 owner approval — a science-level owner decision, not
   housekeeping) and adopts the §9 first-principles criteria as the admissibility
   test for future premise proposals. **No new axiom is added** (the dynamics gap
   is a flagged gate).
8a. **Tier-honesty re-audit obligation (adoption-time).** The P2-dependent rows
   that previously chain-satisfied *for free* via `kinetic_isotropy_primitive`
   must be **actively re-audited** to `retained_bounded` (admitted-input route)
   or open (derived-target route); they must **not** be left silently at their
   old axiom-grade status. The registry move is honest only if the downstream
   ledger is refreshed in the same adoption.
9. **Net premise-count effect.** Axioms still 3 by name, but Record is now A3a
   axiom + A3b conditional; primitives **3 → 2**; **+4 explicit open gates**
   (G-DYN/G-SECT/G-TIME/G-ARROW) that **replace silent presuppositions**, so
   honest premise content **decreases** while becoming auditable.

---

## 11. Summary table

| Item | Verdict | Tier change | Core move |
|---|---|---|---|
| A1 Lattice | passes | axiom (unchanged) | annotate: name `O_h`/`B_3` + (`O_h`-not-`SO(3)`) `L1` metric; isotropy citation guard |
| A2 Quantum | passes | axiom (unchanged) | keep `M_2(C)`; declare scalar field `C`; relocate `Cl(3,0)` reading to labelled downstream id |
| A3 Record | **fails 10/10** | **split** | A3a = finite-additivity valuation, axiom (drop "durable", weaken carrier to disjoint-union-closed); A3b = realized-outcome id (conditional), `K` not CPT, center via supplied `E`/G-SECT, K–E compatibility + sector count exposed |
| P1 scale-reference | passes cleanly | primitive (unchanged) | optional: abstract anchor `M_0`, move `=M_Pl` to gravity gate |
| P2 kinetic-isotropy | **fails 10/10** | **demote: primitive → admitted input** (or derived target) — **DECISION REVERSAL** | `xi_R=1` renormalized dynamical condition; carry B4-consistent tuning/dim-6 residual; drop "free datum / cubic-adjacency analogue" |
| P3 realized-state | concern when bare | primitive (retained) | consolidate counterfactual guard; own one-world commitment; cross-link to A3 |
| SYSTEM (dynamics+time) | under-complete | **new open gate (not axiom)** | G-DYN / G-SECT / G-TIME / G-ARROW required-gate flags; no dynamics axiom |

---

## 12. Re-check fixes applied (traceability)

All four adversarial re-checks returned `revision_sound_with_notes`. Fixes
applied to the wording above:

- **A1:** added the `O_h`-not-`SO(3)` `L1`-metric anisotropy clause (no
  rotational-distance claim may cite A1). [lattice-gauge re-check]
- **A3a:** weakened the carrier from a full **Boolean algebra** to a
  disjoint-union-closed / orthocomplemented poset with `0` (full complementation
  is more than finite additivity needs). [philosopher re-check]
- **A3b:** added hypothesis **2′ (K–E compatibility)** so `{s_*, K.s_*}` is
  well-defined; flagged **sector finiteness/count `m` as supplied** (not a free
  corollary); **barred silent reuse of A2's withdrawn conjugation** for `K`;
  flagged the **`K^2=±1` sign** as a downstream-audited orbit-size consequence.
  [operator-algebras + GR/arrow re-checks]
- **P2:** corrected "tuned point, not protected" to the **B4-theorem-consistent**
  residual (one-loop `Sigma_t=Sigma_s` on the surface; tuning-to-surface +
  dim-6, not generic instability); specified the **Euclidean/OS branch** for
  `c_t`/`c_s`; tightened the gate citation to **G-TIME** (G-DYN upstream); named
  the **registry-of-record route** (admitted-input primary); surfaced the
  **decision reversal** of the 2026-06-09 owner approval. [lattice-gauge + GR/arrow]
- **P3:** corrected the diagnosis to **"consolidate and make explicit"** (the
  guard already lived in the canonical "The Primitive" block); added the
  boundary-vocabulary watch (single datum vs specialness claim → G-ARROW).
  [philosopher re-check]
- **§8 gate:** G-DYN no longer over-claims continuous real-time `U(t)` from bare
  RP (RP ⇒ self-adjoint transfer generator + Euclidean semigroup; real-time
  `U(t)` is a further reconstruction step); **split out G-SECT** as the sole home
  of the center-producing map `E` (RP-dynamics alone keeps a factor a factor);
  flagged **G-TIME undischarged** (single axis is a premise, not a derivation);
  G-ARROW locates the arrow in the initial condition. [all four re-checks]
- **Adoption consequences:** added the **tier-honesty re-audit obligation** (8a)
  and threaded G-SECT through the gate-dependency and registry entries.
  [philosopher re-check]

---

*End of proposal. Adopt nothing from this file without explicit owner approval
recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md` and the machine registry, and
without independent audit-lane review. `hypothetical_axiom_status`;
`proposal_allowed=false`. The canonical `docs/MINIMAL_AXIOMS_2026-06-05.md` memo
and `docs/audit/data/axiom_premise_nodes.json` registry were NOT edited.*
