# Minimal Framework Axioms — PROPOSED REVISION (Lattice, Quantum, Record-valuation)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-21
**Type:** meta / PROPOSED REVISION (governance draft).
**Status:** **PROPOSED REVISION — NOT ADOPTED.** `hypothetical_axiom_status: proposed`;
`proposal_allowed=false`. This memo is a **draft for the owner's governance
decision plus independent audit-lane review**; it is not the current public
framework axiom memo and does not set any audit status.

**Status authority:** The **owner** plus the **independent audit lane** are the
**sole authority** to adopt any wording below. Nothing here sets, predicts, or
estimates an audit verdict, and nothing here promotes any downstream theory
surface. Audit status remains set only by the independent audit lane.

**Supersedes-references (supersedes-on-approval-only):** This memo
**supersedes-references** `docs/MINIMAL_AXIOMS_2026-06-05.md` (the canonical
current memo) **only if and when the owner adopts it**. Until then, the
2026-06-05 memo remains canonical and authoritative; this memo **does not replace
it**, and the 2026-06-05 memo is **left untouched**. The 2026-06-05 memo remains
the source for the prior welded-Record wording being revised here.

**Provenance.** Drives from the clean first-principles panel
(`docs/INCUMBENT_AXIOMS_PRIMITIVES_CLEAN_FIRST_PRINCIPLES_PANEL_2026-06-20.md`,
10/10 `needs_revision`), the OLD->NEW language drafted and adversarially
re-checked in `docs/FOUNDATION_REVISION_PROPOSAL_2026-06-20.md` (four lenses, all
`revision_sound_with_notes`), and the independent Codex / gpt-5.5 cross-check
(`.claude/science/physics-loops/foundation-revision-proposal/CODEX_CROSSCHECK_RAW_2026-06-21.md`).
Codex independently confirmed the two load-bearing findings (A3 split, P2
re-tier) and added two items folded in below: (i) a **missing global
composition / state-space** clause (Codex's #1 change — folded into Quantum and
flagged as gate **G-COMPOSE**); (ii) P1 should arguably be **reclassified from a
primitive to a unit convention / calibration datum** — presented as an explicit
**OPEN OWNER CHOICE** (the Claude clean panel passed P1; Codex flagged it).

---

## Proposal status (read first)

- This memo **does not** edit `docs/MINIMAL_AXIOMS_2026-06-05.md` (canonical) or
  `docs/audit/data/axiom_premise_nodes.json` / `docs/audit/data/tier_a_admissions.json`
  (audit-lane authority). Editing any of those surfaces **is** adoption; the
  registry-of-record changes are emitted instead as an applyable git patch
  (`.claude/science/physics-loops/foundation-revision-proposal/registry_changeset.patch`)
  plus a human-readable diff in the changeset README.
- Everything below is `hypothetical_axiom_status: proposed`. Adopt nothing
  without explicit owner approval recorded in
  `docs/audit/AXIOM_MINIMALITY_POLICY.md` and the machine registry, and without
  independent audit-lane review.
- **One item (P2) is a decision REVERSAL,** not housekeeping: it un-adopts the
  logged 2026-06-09 owner approval of `kinetic_isotropy_primitive`. See the
  changeset README.

## Purpose

This note states the framework's minimal premises in revised form. They are
named rather than treated as bare letter codes:

1. **Lattice** (axiom; A1 annotated)
2. **Quantum** (axiom; A2 amended, with the composition/state-space clause folded
   in per Codex)
3. **Record (valuation)** (axiom; A3a — the additivity valuation that stays an
   axiom)

plus, **outside the axioms**:

- **Realized-outcome identification** (A3b — conditional / derived, NOT an axiom);
- the **scale-reference** datum P1 (primitive, with an open keep-vs-convention
  owner choice) and the **realized-state** primitive P3;
- the **kinetic-form anisotropy condition** P2, **removed** from the axiom-premise
  registry and registered as a Tier-A admitted input (or open derived target);
- the required **open gates** G-DYN / G-SECT / G-TIME / G-ARROW / G-COMPOSE.

Legacy `A1`/`A2`/`A3` numbering is historical; new repo surfaces should use the
axiom names above unless quoting an older document.

---

## The Framework Axioms (proposed)

### Lattice (A1; annotated — passes, no demotion)

The site set is `Z^3` with the standard translation action and nearest-neighbor
cubic adjacency. Finite-range locality means finite support or finite
graph-distance range with respect to this lattice when a local expression is
specified.

This axiom supplies exactly three things and nothing more: (i) the discrete site
set `Z^3` with its translation action; (ii) the **combinatorial point-group
symmetry** of that adjacency — the cubic group `O_h` on the site stencil,
equivalently the hyperoctahedral group `B_3` (the discrete permutation-and-sign
symmetry of the three axes), which is the discrete residue of, **not** a
substitute for, continuous rotational isotropy; and (iii) the **combinatorial
`L1` graph metric** induced by edge adjacency. The three coordinate directions
are interchangeable **as graph axes** (a discrete `B_3` statement); this is
*not* continuous spatial isotropy and is *not* an emergent-Lorentz statement.

This axiom does **not** supply: a dynamics, a boundary condition, a dimensionful
metric scale, a lattice spacing, a continuum or infrared limit, a causal cone, a
probabilistic-independence rule, a physical unit conversion, **continuous
rotational isotropy**, or any **emergent-symmetry** result.

The `L1` graph metric supplied here is `O_h`-invariant but **not**
`SO(3)`-invariant: its unit ball is the `L1` diamond, not a round ball, so it is
**anisotropic at the continuum level** and supplies **no** rotation-invariant
distance. No row may cite this axiom for a rotational-distance claim.

**Supplied-vs-derived discipline (corrected 2026-06-22).** Continuous spatial
isotropy `a_x = a_y = a_z` (in the metric, not the graph, sense), a
relativistic/Lorentz statement, and a kinetic-form ratio are **not supplied by**
this axiom — A1 supplies only the discrete `O_h`/`B_3` symmetry and the `L1`
graph metric. They may, however, be **derived** as theorems that take A1 as one
premise **together with an explicitly named** dynamics, limit, or RG argument
(see the kinetic-form condition P2 and the required dynamics/time gates below).
What is barred is treating continuous isotropy/Lorentz as a property **read off
A1 alone** (an axiom-grade chain-satisfy / free pass); using A1 as a premise in a
derivation that *proves* emergent isotropy is correct and encouraged. A row that
currently *asserts* the lattice axiom *supplies* isotropy must be reworded to
"…**derived** from A1 (discrete `O_h`/`B_3`) + [named dynamics/limit]".

> **Reviewer context (Layer-2 migration accounting, not a panel finding).** An
> exact triage of all 58 rows that co-locate the lattice axiom with an
> isotropy/rotation/Lorentz claim found **zero** rows that free-ride on A1 (Class
> A = 0): the framework already derives isotropy from named dynamics premises
> (~14 derivations), treats it as the separate `kinetic_isotropy` primitive or a
> Wilson-action label (~20 incidental), or is explicitly anisotropy-aware (~24
> no-go/anisotropy notes that *support* this annotation). So this annotation
> requires **no citation reframes**. The only downstream cost is the **236-row
> hash-guard re-audit** (rows with `minimal_axioms` as a direct dep), which is the
> mechanical consequence of editing the canonical memo *at all* (shared by
> A1/A2/A3, a re-audit not a content change) — **the audit lane / owner decides
> whether and when to run it.** Full list:
> `docs/A1_LATTICE_REVISION_IMPACT_MANIFEST_2026-06-21.md`.

### Quantum (A2; amended — keep `M_2(C)` at axiom grade; add the composition / state-space clause)

At each site `x`, the primitive physical local degree of freedom is one qubit;
equivalently, the primitive one-site operator algebra is the complex matrix
algebra `A_x ~= M_2(C)`, taken over the **complex scalar field `C`** (the unit
`i` is the complex unit of `M_2(C)`).

**Global composition / state space (folded-in clause; per Codex's #1 change).**
The framework composes sites by **tensor product**: for any finite region
`R \subset Z^3`, the region algebra is the finite tensor product
`A_R = (x)_{x in R} A_x ~= M_2(C)^{(x)|R|} ~= M_{2^{|R|}}(C)`, with the standard
inclusions `A_R \hookrightarrow A_{R'}` for `R \subset R'` (an operator embedded
on `R'\setminus R` as the identity). The **global one-site-carrier algebra** is
the infinite **quasi-local `C*`-algebra**
`A = closure( \bigcup_{R finite} A_R )` — the UHF / hyperfinite inductive limit
of the `M_{2^{|R|}}(C)` net (a `C*`-completion of the algebraic inductive limit).
A **state** of the framework is a normalized positive linear functional on `A`
(equivalently, a compatible family of finite-region density operators); the
state space is the set of such states. This clause **only** names the
composition law and the state-space carrier; it is **not** a dynamics, a
preferred state, a measure, a probability rule, a superselection structure, or a
center-producing map (`A` so composed is a **factor**: it has trivial center —
see G-SECT and A3b below).

This axiom supplies **only**: the one-site algebraic carrier `M_2(C)` and its
complex scalar field; and the finite-tensor composition law together with the
quasi-local `C*`-algebra `A` and its state space. It does **not** supply: a
dynamics; a composition theorem beyond the named tensor placement; a
distinguished set of generators or a preferred basis; a chirality / pseudoscalar
element; a real form, conjugation, or antiunitary structure; a measurement
instrument; a Born rule; a species identification; a gauge group; particle
content; a preferred or distinguished state; a nontrivial center / superselection
sectors; or a physical observable bridge.

**Labelled downstream identification (NOT part of the axiom).** `M_2(C)` is
isomorphic, as a complex algebra, to the complexified Clifford algebra
`Cl(3,0) (x) C`; under a *chosen* real form one may read the carrier as the real
algebra `Cl(3,0)`. That real-Clifford reading additionally distinguishes an
`so(3) ~ su(2)` bivector generator set, a pseudoscalar/chirality element, and a
real-structure conjugation. **None of that extra structure is supplied by this
axiom.** Any row that uses Clifford generators, chirality, a real form, or an
antiunitary built from them must cite that identification explicitly as a
separate, labelled step and own the choices it makes (canonical landing:
`docs/A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md` and the per-site `Cl(3)`
uniqueness note), not draw them from this axiom.

### Record (valuation) (A3a; the part of A3 that STAYS an axiom)

A **record** is a registered outcome, drawn from a collection of registered
events closed under **finite disjoint union** and equipped with a distinguished
empty record `0` (an orthocomplemented poset / generalized Boolean ring of
disjoint records — **not** a full Boolean algebra; complementation/negation is
deliberately **not** required, as finite additivity over disjoint collections
does not need it). The framework posits a **scalar readout** `I` on records that
is **finitely additive over finite pairwise-disjoint collections**:

```text
    I(r_1 \/ ... \/ r_n) = I(r_1) + ... + I(r_n)   for pairwise-disjoint r_k,
    I(0) = 0.
```

This axiom supplies **only** the finite-additivity valuation structure of the
scalar readout. It does **not** supply: a readout context; a sector
decomposition (central or otherwise); a conjugation or antiunitary; a
sector-generation rule; weighting; normalization; probability; a
measurement/decoherence dynamics; a time metric or arrow of time; an
irreversibility ("durability") claim; within-sector data; or an occupancy rule.
In particular, **what counts as "the realized outcome"** — the map from physical
configurations to records — is **not** fixed by this axiom; it is the subject of
the separate conditional identification (A3b) and depends on the required
dynamics/time gates below.

> **What changed from the 2026-06-05 Record axiom.** The incumbent Record welded
> this clean valuation to a "`K`/CPT orbit of the realized central sector"
> selector that (i) disclaims-while-uses a decomposition and a conjugation,
> (ii) posits central sectors on a **factor** (`M_2(C)` and its tensor
> product/inductive limit have trivial center — no nontrivial sectors exist),
> (iii) imports "CPT" (a *theorem* of Lorentz-invariant local QFT, not a
> primitive), and (iv) smuggles an arrow via "durable = fixed once registered."
> The valuation above is kept as the axiom; the selector is relocated to the
> conditional A3b; "durable" is removed and its arrow content relocated to
> G-ARROW. The carrier was weakened from a full Boolean algebra to the minimum
> finite-additivity needs (disjoint-union-closed, with `0`).

---

## Outside the axioms

### Realized-outcome identification (A3b; conditional / derived — NOT an axiom)

**Tier:** derived-result / conditional identification (depends on the
center-producing gate G-SECT, the dynamics/time gates, and a supplied realized
configuration).

**Hypotheses (each must be supplied, none is posited here):**

1. a **center-producing coarse-graining / superselection ingredient** `E` that
   sends the factor algebra of the foundation to an algebra with a **nontrivial
   center** `Z`, yielding a family of **central sectors** `{s_1, ..., s_m}`.
   (`M_2(C)`, all its finite lattice tensor powers, and their UHF/hyperfinite
   inductive limit `A` are **factors with trivial center**, so without such a
   supplied `E` there are **no** nontrivial sectors — this hypothesis is
   load-bearing.) **`E` is not produced by reflection-positive dynamics alone:**
   a factor's reflection-positive time evolution stays a factor evolution, so `E`
   requires dynamics **plus** an additional coarse-graining / thermodynamic or
   large-`N` limit / gauge-constraint / environment-induced-superselection
   ingredient. That sector-producing ingredient is the sub-gate **G-SECT**,
   distinct from the bare dynamics gate G-DYN. **The finiteness and the count `m`
   of `{s_1, ..., s_m}` are themselves part of this supplied hypothesis**, not
   free corollaries of `K` or of the dynamics; any downstream generation/sector
   *count* inherits `m` as a carried dependency.
2. the existence of a **neutral antiunitary involution** `K` on the carrier (an
   antilinear `*`-map with `K^2 = +/- 1`) whose existence is *posited as a
   hypothesis*, **not** identified with CPT and **not** carrying any
   theorem-strength corollary. **`K` must NOT be silently drawn from the
   real-structure conjugation that A2 explicitly withdrew:** any `K` built from
   Clifford generators / a real form must cite A2's labelled downstream
   identification and own that choice. Physical identifications of `K` (e.g. with
   a CPT-like or charge/parity-like operator) are separate, labelled, and audited
   downstream. The **sign** `K^2 = +1` (real/orthogonal) vs `K^2 = -1`
   (quaternionic/Kramers) is left open here; the resulting **orbit-size /
   fixed-sector structure** (orbit size 1 or 2; whether fixed sectors exist) is a
   **downstream-audited consequence of the sign**, not fixed by this
   identification.
2′. (**K–E compatibility**) `K` **normalizes** the center `Z` produced by `E` and
   therefore **descends to a well-defined involution on the sector set**
   `{s_1, ..., s_m}` (so that `K . s_*` is again a sector). Posited at the
   `K`-on-the-carrier level alone, this descent is **not** automatic; it is an
   explicit hypothesis the orbit construction uses.
3. a **realized configuration** supplied by the physical history (the
   realized-state slot, P3).

**Conditional conclusion.** Given (1)-(2′)-(3), the **realized outcome** is the
`K`-orbit of the realized central sector `s_* in {s_1, ..., s_m}`:
`outcome = { s_*, K . s_* }` (well-defined as a subset of the sector set by
hypothesis 2′). The scalar readout `I` of A3a is then evaluated on the records so
identified.

**Status.** This identification is a **conditional/derived result**, not a
premise. It is *false as stated at the bare-foundation level* (no center exists
there); it becomes meaningful only once the supplied maps `E`, `K`, and the
realized configuration exist. It supplies none of `E`, `K`, the sector count,
weighting, normalization, probability, or within-sector data. Downstream
`K`/CPT-orbit consumers (e.g.
`docs/P2_KCPT_ORBIT_TEMPORAL_FACTOR_NO_GO_2026-06-06.md`) must re-cite A3b
(conditional) and carry `E`/`K`/realized-config/`m` as dependencies.

### P1 scale-reference (primitive — OPEN OWNER CHOICE: keep-as-primitive vs reclassify-as-convention)

**Tier:** primitive (retained) **OR** unit convention / calibration datum —
**this is an explicit OPEN OWNER CHOICE.** The Claude clean first-principles
panel passed P1 cleanly and unanimously (primitive grade). The independent Codex
cross-check flagged P1 as "mostly yes, but better as a convention": a dimensionful
anchor alone has no invariant content, and identifying `a^{-1}` with `M_Planck`
would import an empirical Planck identification (plus `G, hbar, c` conventions).
Both framings are presented; the owner selects.

**Framing K (keep-as-primitive — Claude clean-panel result; optional hygiene):**

> The framework takes exactly one dimensionful reference: a single inverse length
> / mass scale `a^{-1} = M_0` that converts the framework's lattice-natural units
> to physical units. `M_0` is an **abstract anchor**; the *identification*
> `M_0 = M_Pl` (equivalently `a = l_Planck`) is **not** part of this primitive —
> it is a separate open gravity self-consistency gate and is recorded there, not
> here. This is a units conversion, not a physics axiom. It carries zero
> dimensionless content: no mass ratio, coupling, mixing angle, phase, selector,
> readout bridge, or empirical fit is supplied by it, and it does **not** assert
> `a / l_Planck = 1` as a derived theorem.

**Framing C (reclassify-as-convention — Codex result):**

> `a^{-1}` is recorded as a **unit convention / calibration datum**, not as a
> physical-structure primitive: a dimensionful anchor with **no invariant
> dimensionless content** carries no physical structure on its own. Should
> `a^{-1}` ever become an *observable scale bridge* (e.g. via a load-bearing
> `= M_Planck` identification consuming `G, hbar, c`), it is reclassified at that
> point as an admitted empirical input, not a light primitive. Under this framing
> P1 leaves the approved-primitive class and is recorded as a convention
> alongside `Y0`/`g0` (survey-completeness conventions; not status-bounding
> dependencies).

**Owner decision required.** Framing K leaves the approved-primitive count
unchanged at this slot; Framing C drops P1 from the primitive class. Both agree
the `= M_Pl` number must not be load-bearing. The registry changeset (below) does
**not** move P1 under either framing — the keep-vs-convention call is left open
for the owner; only P2's removal is encoded in the patch.

### P2 kinetic-form anisotropy condition (DEMOTED: primitive → admitted input — DECISION REVERSAL)

**Tier change:** from **approved primitive** → **Tier-A admitted input** (primary
route), with an explicit **alternative** of a **derived IR-fixed-point target**.
Either way `c_t = c_s` leaves the axiom-premise registry.

**THIS IS A DECISION REVERSAL.** `AXIOM_MINIMALITY_POLICY.md` §6 (entry
2026-06-09) and `axiom_premise_nodes.json` both record an explicit **owner
approval** of `kinetic_isotropy_primitive` *as a primitive*, on the ground that
`c_t = c_s` is "dimensionless **structural** ... of the same category as cubic
adjacency ... **not** dimensionless **dynamical** content." This proposal asserts
the **opposite**. Adopting it **reverses** that 2026-06-09 owner approval and
amends the registry; it cannot land without the owner reversing the approval and
the audit lane re-auditing.

**Primary route — ADMITTED INPUT (Tier-A; not a primitive):**

> On the regulated theory with an emergent time direction (supplied by gate
> **G-TIME**, with **G-DYN** upstream) — taken in the Euclidean /
> Osterwalder-Schrader branch where `c_t` and `c_s` are defined (`xi_R = 1` is
> the bridge condition between branches) — the **renormalized** space-time
> kinetic-form anisotropy is tuned to isotropy,
> `xi_R = c_t / c_s = 1` (renormalized, not bare).
>
> Why admitted, not primitive: (i) `c_t = c_s` is the emergent-Lorentz output;
> positing the answer as a free datum is circular. (ii) On a lattice
> `xi_R != xi_bare` (related by interaction-dependent **Karsch coefficients**),
> so fixing `xi_R = 1` is a **dimensionless dynamical tuning condition** — exactly
> the content a primitive may not carry. (iii) It presupposes an emergent time
> direction, supplied by G-TIME, not by this statement.
>
> **Carried residual (B4-theorem-consistent).** `xi_R = 1` is a tuning condition
> to reach the hypercubic-symmetric (`B4`) surface; on that surface the marginal
> anisotropy is symmetry-protected (one-loop `Sigma_t = Sigma_s` by exact axis
> relabeling; leading Lorentz violation pushed to a Planck-suppressed
> dimension-6 operator — cf.
> `docs/EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`).
> So the residual is (a) the one-time tuning-to-surface and (b) the dimension-6 /
> non-`B4` naturalness question — **not** generic marginal radiative instability.
>
> **Explicitly dropped:** "free structural datum" and "analogue of cubic
> adjacency" are withdrawn (cubic adjacency is kinematic and
> interaction-independent; `xi_R = 1` is a renormalized dynamical condition).

**Alternative route — DERIVED TARGET (if the owner prefers):**

> `xi_R = c_t/c_s -> 1` as an **infrared fixed-point** property of the emergent
> dynamics: isotropy of the matter light cone is a *consequence* to be derived
> (emergent Lorentz invariance in the IR), not an input. Until a retained
> derivation closes it, it is an **open derived target** carrying the same
> tuning-to-surface / dimension-6 residual; rows that need `xi_R = 1` cite it as
> an open dependency, not as an axiom or primitive.

The two routes carry different audit semantics (admitted-input dependents
chain-satisfy at `retained_bounded`; derived-target dependents stay open), so the
owner must select one. The registry changeset encodes the **admitted-input**
route as registry-of-record.

### P3 realized-state (primitive — retained; disambiguated)

**Tier:** primitive (retained).

> The laws do not pick the state; the world does, among the states the laws
> permit. This primitive posits **one** datum: a single law-admissible **realized
> state** is supplied by the physical history (a one-world / actualization
> commitment — an initial/boundary-condition input that the state-blind laws
> cannot themselves supply). Derivations may **evaluate at the realized state,
> pointwise**.
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
> **Sense disambiguation (cross-link).** "Realized **state**" here is the supplied
> physical configuration of hypothesis (3) of the realized-outcome
> identification (A3b). It is **distinct** from the "realized **outcome**" of
> A3b, which is the *recorded event* (`K`-orbit of the realized central sector).
> The two uses of "realized" are not interchangeable.
>
> **Stronger input held out.** The **past hypothesis** (a specialness /
> atypicality claim about the realized history) is a strictly stronger input of
> exactly the class this primitive's guard forbids; it is **not** housed here and
> remains the named residual of
> `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`
> (routed to gate G-ARROW).

---

## Open Gates (required; flagged, NOT axioms or primitives)

The foundation (axioms Lattice, Quantum, Record-valuation; primitives P1, P3)
supplies **no** dynamics, **no** time, **no** nontrivial center, and (without the
G-COMPOSE clause now folded into Quantum) historically did not state global
composition. The following are **required open gates**, on which several
downstream statements are explicitly conditional; they are **flagged here so they
are never silently presupposed**, and they are **not** promoted to axioms or
primitives. (Per `AXIOM_MINIMALITY_POLICY.md` §1/§4, when a lane needs an extra
axiom, do not add it — flag a gate and land a boundary note. No dynamics axiom is
added.)

- **(G-COMPOSE) Global composition / state space** *(per Codex's #1 change).* The
  finite-region **tensor composition** law and the infinite **quasi-local
  `C*`-algebra** `A` (UHF/hyperfinite inductive limit of the `M_{2^{|R|}}(C)`
  net) and its **state space**. This was **never explicitly stated** in the
  incumbent foundation (Codex's #1 finding). It is now folded into the **Quantum
  axiom** as the composition/state-space clause **and** flagged here as a gate so
  that any further global-state-space structure (a distinguished GNS
  representation, a thermodynamic limit prescription, a global state) is named
  rather than presupposed. The bare composition clause in Quantum supplies the
  factor algebra `A` only; it supplies **no** preferred state, no center, no
  dynamics. Current status: composition clause **proposed adopted into Quantum**;
  any structure beyond the bare factor `A` + its state space remains open.
- **(G-DYN) Dynamics / time-evolution.** A law of evolution (action, transfer
  matrix, or Hamiltonian) with **reflection positivity (RP)**. RP gives a
  positive transfer matrix and hence a self-adjoint transfer generator and a
  Euclidean semigroup `T^n` (`T = exp(-a H)`, `H` bounded below). It does **not**
  by itself hand you a continuous real-time unitary group `U(t) = exp(-i t H)`:
  that requires a further reconstruction / analytic-continuation
  (Wick-rotation / OS-reconstruction) step, itself an open dependency.
  RP-dynamics is **time-symmetric** (the unitary evolution carries **no** arrow;
  the arrow is quarantined in G-ARROW). Current status: conditional/derived
  cluster (RP transfer-matrix and single-clock notes), **not** an axiom.
- **(G-SECT) Center-producing coarse-graining / superselection.** The map `E`
  that produces a **nontrivial center** (the finite central-sector family
  `{s_1, ..., s_m}` and its count `m`) required by A3b (hypothesis 1). **NOT
  supplied by G-DYN alone:** reflection-positive evolution of a **factor** stays
  a factor evolution, so a nontrivial center additionally needs a coarse-graining
  / thermodynamic or large-`N` limit / gauge constraint /
  environment-induced-superselection ingredient. Named **separately** from G-DYN
  precisely so "dynamics supplies `E`" cannot stand unqualified. Current status:
  open (no nontrivial center exists at the bare-foundation level), **not** an
  axiom.
- **(G-TIME) Emergent time axis.** A distinguished evolution direction ("time"),
  emergent from G-DYN (e.g. the single-clock codimension-1 evolution). This is
  the time direction presupposed by the kinetic-form condition
  `xi_R = c_t/c_s` (P2). **Currently UNDISCHARGED:** an emergent single time axis
  (codimension-1, one clock) is itself a nontrivial selection the gate **names
  but does not establish** — the repo's own single-clock note states "**the axis
  is a premise, not a derivation**." Not to be read as already-supplied. Current
  status: emergent / axis-conditional and undischarged, **not** an axiom.
- **(G-ARROW) Arrow / irreversibility.** The "durability" of records — the
  time-asymmetric claim that a registered outcome does not change — is a statement
  about an **arrow of time**, not part of the Record valuation (A3a). The arrow
  lives in the **initial condition** (past hypothesis), not in the time-symmetric
  dynamics of G-DYN. Held here as a required gate; remains the residual of the
  past-hypothesis / arrow note
  (`docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`).
  **Not** an axiom and **not** supplied by P3.

Any row that uses an evolution law, an emergent time direction, a
superselection/coarse-graining (center-producing) map, record durability, or
global-state-space structure beyond the bare factor `A` must cite the relevant
gate (G-DYN / G-SECT / G-TIME / G-ARROW / G-COMPOSE) as an explicit open
dependency.

---

## Other open gates and admissions outside the axioms (unchanged from canonical)

The axioms do not close, import, or rename the framework's downstream open gates.
The following remain outside axiom content:

- the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;
- the strong-CP theta admission;
- P2/modulus/phase-blindness and any log-det readout theorem;
- arrow, measurement, decoherence, record-production dynamics, and physical
  persistence dynamics (see G-ARROW / G-DYN);
- source/action and physical-observable identification;
- `g_bare = 1` convention handling;
- the scale-reference datum (P1) and the separate gravity self-consistency
  question that the framework's natural unit equals the Planck length.

---

## Audit-pipeline treatment (proposed)

The machine-readable source of the axiom set is the `minimal_axioms` entry in
`docs/audit/data/axiom_premise_nodes.json` (left untouched here; proposed changes
emitted as a patch). On adoption: the `minimal_axioms` source content changes
(A1 annotation; A2 amendment incl. the composition/state-space clause; A3 split
into A3a axiom + A3b conditional), invalidating prior direct `minimal_axioms`
audits via the axiom-premise hash guard (all direct dependents re-audited by the
independent lane). `kinetic_isotropy_primitive` is **removed** from
`canonical_ids`/`nodes` and **moved** to `tier_a_admissions.json` as a
renormalized-anisotropy admitted derivation target (primary route).

Axioms and approved primitives are not Tier-A admitted derivation targets.
Depending on an axiom or an approved primitive must not be treated as a source of
bounded status. Bounded status belongs to non-axiom Tier-A admissions recorded in
`docs/audit/data/tier_a_admissions.json` — which, after adoption, includes the
demoted `kinetic_isotropy_primitive` (admitted-input route).

---

## Historical context

The April–May sequence separated the one-qubit local algebra and the `Z^3`
lattice from downstream realization gates previously written too axiomatically.
The 2026-06-04 memo added scalar finite Record additivity; the 2026-06-05 memo
welded a `K`/CPT-orbit realized-outcome selector onto that valuation. The
2026-06-20 clean first-principles panel returned 10/10 `needs_revision`; the
independent Codex cross-check returned `unsound as a complete foundation` (one
notch harsher) and independently confirmed the A3-split and P2-retier while
adding the missing global composition / state-space requirement and the P1
keep-vs-convention question. This proposed memo encodes those revisions while
preserving the byte-for-byte operative content that passed (the Lattice core, the
`M_2(C)` carrier core, and finite Record additivity).

---

*End of PROPOSED REVISION. Adopt nothing from this file without explicit owner
approval recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md` and the machine
registry, and without independent audit-lane review. `hypothetical_axiom_status:
proposed`; `proposal_allowed=false`. Supersedes-references
`docs/MINIMAL_AXIOMS_2026-06-05.md` on approval only; the canonical 2026-06-05
memo and the `docs/audit/data/` registry JSON were NOT edited.*
