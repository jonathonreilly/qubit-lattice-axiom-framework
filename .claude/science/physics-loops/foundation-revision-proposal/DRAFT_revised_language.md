# DRAFT — Corrected Foundation Language (PROPOSAL, not adopted)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-21
**Type:** meta / governance proposal
**Status:** `hypothetical_axiom_status` — PROPOSAL ONLY. `proposal_allowed=false`.
This draft does **not** edit `docs/MINIMAL_AXIOMS_2026-06-05.md` or
`docs/audit/data/axiom_premise_nodes.json`. Those are the canonical/registry
surfaces; editing them is adoption. The **owner** plus the **independent audit
lane** are the sole authority to adopt any wording below. Nothing here sets,
predicts, or estimates an audit verdict.
**Drives from:** the clean first-principles panel
(`docs/INCUMBENT_AXIOMS_PRIMITIVES_CLEAN_FIRST_PRINCIPLES_PANEL_2026-06-20.md`,
10/10 `needs_revision`) and the verbatim incumbent statements judged there
(recovered from `.claude/tmp/incumbent-panel-clean-wf.js`).
**Current wordings corrected against:** `docs/MINIMAL_AXIOMS_2026-06-05.md`
(Lattice/Quantum/Record), `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` (P1),
`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (P2),
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (P3).

---

## 0. Drafting principles applied (stated, then used everywhere below)

1. **Non-circularity of an axiom.** An axiom must not *use* structure it
   disclaims supplying. If a statement consumes a decomposition, a conjugation,
   a sector label, or a metric, that object must be supplied — by the same
   statement, by another posit, or by an explicitly flagged open gate — never
   disclaimed-while-used.
2. **Single-datum purity of a primitive.** A primitive is one narrow accepted
   datum that carries **no** dynamical, selector, renormalized, or empirical
   content, and is **not** a consequence of the other posits. A renormalized
   tuning condition, an emergent symmetry result, or a fit is not primitive-class.
3. **Theorems are not premises.** A statement that is a *theorem* of a richer
   structure (paradigmatically CPT, which is a theorem of Lorentz-invariant
   local QFT) must not be posited as a premise. Name the **bare object** the
   theorem would otherwise hand you (here: an antiunitary `K`) and posit only
   its **existence** as a hypothesis, with no theorem-strength corollaries.
4. **No smuggling of arrow / time / dynamics / decomposition / conjugation.**
   Any irreversibility, arrow of time, emergent time axis, evolution law,
   central decomposition, or conjugation that is *used* anywhere downstream
   must be **explicitly posited or explicitly flagged as a required open gate**.
   Silent presupposition is disallowed.
5. **Weakest sufficient change.** Prefer the minimal edit that resolves the
   objection. Keep what passed intact: the A1 Lattice core, the A2 `M_2(C)`
   carrier core, P1 in full, and finite Record additivity.

The five principles are restated as general policy criteria in §9.

---

## 1. A1 LATTICE — PASSES; ANNOTATE (no demotion)

**Tier:** axiom (unchanged).

**Current wording** (`docs/MINIMAL_AXIOMS_2026-06-05.md`, "Lattice"):

> The site set is `Z^3` with standard translation action and nearest-neighbor
> cubic adjacency. Finite-range locality means finite support or finite
> graph-distance range with respect to this lattice when a local expression is
> specified.
>
> This axiom supplies the discrete site set and local adjacency notion. It does
> not supply a dynamics, boundary condition, metric scale, lattice spacing,
> continuum or infrared limit, causal cone, probabilistic independence rule, or
> physical unit conversion.

**Objection it resolves (panel A1):** A1 *passes* but is silently over-claimed
downstream. "Nearest-neighbor cubic adjacency" supplies (i) the cubic point
group `O_h` / hyperoctahedral `B_3` symmetry of the site set, and (ii) an
`L1`/graph (combinatorial) distance. It does **not** supply continuous
rotational isotropy and it is **not** "no metric". Downstream rows must not
cite A1 as the source of spatial isotropy `a_x = a_y = a_z` in the *continuous*
sense, nor as a no-metric statement.

**PROPOSED corrected wording (paste-ready):**

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
> condition, §6, and the required dynamics/time gate, §8).

**Notes.** This is a pure annotation: the operative content (`Z^3`,
translations, cubic adjacency, finite-range locality) is byte-for-byte
preserved. The only additions are (a) naming the two structures the adjacency
*does* hand you (`O_h`/`B_3` point group; `L1` graph metric) so they are owned
rather than latent, and (b) an explicit citation guard so the isotropy
over-claim the panel flagged cannot recur. No object is used that is not
supplied. Resolves the A1 finding with the weakest possible change (principle 5).

---

## 2. A2 QUANTUM — PASSES; AMEND (keep `M_2(C)` at axiom grade)

**Tier:** axiom (unchanged) for the `M_2(C)` carrier; **relocate** the
`Cl(3,0)` reading to a labelled downstream identification.

**Current wording** (`docs/MINIMAL_AXIOMS_2026-06-05.md`, "Quantum"):

> At each site `x`, the primitive physical local degree of freedom is one qubit;
> equivalently, the primitive one-site operator algebra is
> `A_x ~= M_2(C)`, equivalently `Cl(3,0)` in its real-algebra reading.
>
> This axiom supplies the one-site algebraic carrier. It does not supply a
> dynamics, composition theorem beyond the named lattice placement, measurement
> instrument, Born rule, species identification, gauge group, particle content,
> or physical observable bridge.

**Objection it resolves (panel A2):** Keep `M_2(C)` at axiom grade. But
"`= Cl(3,0)` in its real-algebra reading" is **not** an inert "equivalently".
`M_2(C)` and `Cl(3,0)` are isomorphic as *complex* algebras, but the **real
Clifford reading** silently supplies extra structure that A3 later *reuses*:
(a) a distinguished `so(3) ~ su(2)` **bivector generator** set (a choice of
rotation generators), (b) a **pseudoscalar / chirality** element (the volume
element `e1 e2 e3`), and (c) a **real form / conjugation** that fixes the
antiunitary structure A3 reuses. An axiom that says "carrier only" must not be
the silent supplier of generators, chirality, and a conjugation. Also: the
scalar field of the algebra (is "`i`" the complex unit of `M_2(C)`, or the
pseudoscalar of the real `Cl(3,0)`?) must be **declared** so that "`i`" is
owned, not ambiguous.

**PROPOSED corrected wording (paste-ready):**

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

**Notes.** The `M_2(C)` carrier — everything that passed — is preserved and in
fact *sharpened* (the scalar field is now declared, closing the "`i`" ambiguity).
The single substantive move is to **demote** the `Cl(3,0)` clause from an inert
axiom-grade "equivalently" to a clearly labelled downstream identification, and
to enumerate exactly the three structures (generators, chirality, conjugation)
that the real reading would otherwise smuggle in. This directly removes the
silent supplier that A3 was reusing (principle 1) and makes "`i`" owned
(principle 4). Weakest change: the carrier and its axiom status are untouched.

---

## 3. A3 RECORD — FAILS (10/10 mis-tiered); SPLIT into A3a (axiom) + A3b (derived/conditional)

This is the load-bearing repair. The incumbent Record welds together a clean
finite-additivity valuation (legitimate, axiom-class) and a "K/CPT orbit of the
realized central sector" **selector** that fails four independent ways. We
split it.

**Current wording** (`docs/MINIMAL_AXIOMS_2026-06-05.md`, "Record"):

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

**Objections it resolves (panel A3, 10/10 fail):**
- **(i) Disclaim-while-use contradiction.** The selector clause *uses* a finite
  central-sector decomposition and a fixed conjugation in the very sentence
  that disclaims supplying them. An axiom cannot consume what it disclaims
  (principle 1).
- **(ii) No nontrivial center exists yet.** `M_2(C)` is a **factor** (trivial
  center `= C.1`); a tensor product of factors over `Z^3` is a factor. So there
  are **no nontrivial central sectors** to take an orbit of without an
  unsupplied **gauge / coarse-graining / superselection map** that produces a
  center. The selector presupposes structure the foundation does not have.
- **(iii) CPT illegitimately imported.** "CPT" is a **theorem** of
  Lorentz-invariant local QFT, not a primitive; importing it as a premise is
  exactly principle 3's prohibition — and circular, since this very repo treats
  CPT as a separate `bounded_theorem` stretch
  (`docs/AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`). The bare object
  must be a **neutral antiunitary `K`** with stated existence, never "CPT".
- **(iv) Smuggled arrow of time.** "durable = fixed once registered: the
  recorded outcome does not change" smuggles **irreversibility / an arrow of
  time** into the foundation. Time-asymmetry by fiat is not axiom-legitimate
  (principle 4); it must be relocated to the flagged dynamics/arrow gate.

### 3a. A3a RECORD-VALUATION — the part that stays an axiom

**Tier:** axiom.

**PROPOSED corrected wording (paste-ready):**

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

**Notes.** This is the clean, durable-free, decomposition-free, conjugation-free
valuation: a finitely additive scalar on a Boolean algebra of events with
`I(0)=0`. It is genuinely axiom-class (it uses nothing it disclaims), it is what
the whole panel agreed was legitimate, and it is what downstream additive-readout
rows actually consume. The word "durable" is **removed** (its irreversibility
content moves to §8). The "realized outcome" map is explicitly **deferred**, not
disclaimed-while-used.

### 3b. A3b REALIZED-OUTCOME IDENTIFICATION — derived/conditional, NOT an axiom

**Tier:** derived-result / conditional identification (depends on the dynamics
+ time gate §8 and on a supplied coarse-graining that produces a center).

**PROPOSED corrected wording (paste-ready):**

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

**Notes.** This is the heart of the fix. Everything the panel called
illegitimate when posited as an axiom is **retained as a clearly conditional
identification** with its hypotheses *exposed*: the missing center now has a
named supplier (the center-producing map `E`, supplied by the **G-SECT** sub-gate
of §8 — explicitly **not** by reflection-positive dynamics alone, which keeps a
factor a factor); "CPT" is replaced by a **bare antiunitary `K` with posited
existence only**
(principle 3); and the selector no longer disclaims-while-using (principle 1) —
it openly *requires* `E`, `K`, and a realized configuration. Downstream rows
that previously cited "Record" for the K/CPT-orbit selector (e.g. the
generation-sector-count usage referenced in
`docs/P2_KCPT_ORBIT_TEMPORAL_FACTOR_NO_GO_2026-06-06.md`) must be **re-audited**
to cite A3b (conditional) rather than an axiom, and to carry the `E`/`K`
hypotheses as explicit dependencies.

---

## 4. P1 SCALE-REFERENCE — PASSES CLEANLY (unanimous); KEEP, optional hygiene

**Tier:** primitive (unchanged).

**Current wording** (`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`, "What This
Declares"):

> The framework takes exactly one dimensionful reference: a scale that converts
> the framework's lattice-natural units to physical units. The chosen reference
> is the Planck mass scale, `a^{-1} = M_Pl`.
>
> This is a units conversion, not a physics axiom. It carries zero dimensionless
> content [...].

**Objection it resolves (panel P1):** none required — P1 passes cleanly and
unanimously. The *optional* hygiene is: the identification of the abstract
anchor with `M_Pl` quietly leans on a gravity self-consistency (`a = l_P`) that
is a **separate open gate**. Naming the anchor abstractly keeps the primitive
strictly units-only.

**PROPOSED corrected wording (paste-ready, OPTIONAL):**

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

**Notes.** Strictly optional. The only change is to name the anchor abstractly
(`M_0`) and move the `= M_Pl` identification to a referenced open gravity gate,
so the primitive is provably free of even the *appearance* of dimensionless /
self-consistency content. The existing note already disclaims `a/l_P = 1`; this
just makes the abstract/identified split explicit at the point of declaration.
If the owner prefers continuity, the current wording is acceptable as-is — this
is hygiene, not a defect repair.

---

## 5. P2 KINETIC-ISOTROPY — FAILS (10/10 mis-tiered); RE-TIER (demote from primitive)

**Tier change:** from **approved primitive** to **admitted input** (Tier-A
admission, a renormalized-anisotropy *condition*), with an explicit alternative
of recording it as a **derived IR-fixed-point target**. Either way it leaves
the axiom-premise registry.

**Current wording** (`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`, "What
This Declares"):

> The framework takes one structural graining fact: the emergent evolution tick
> is grained on the same footing as the spatial lattice edge. Concretely, the
> matter kinetic normalization is space-time isotropic, `c_t = c_s` [...]. This
> is a structural statement about the regulator geometry, the time-direction
> analogue of the `LATTICE` axiom's spatial **cubic adjacency** `a_x = a_y =
> a_z`. It carries no dimensionless dynamical content [...].

**Objections it resolves (panel P2, 10/10 fail):**
- **(a) It is the emergent-Lorentz ANSWER, asserted as a free datum.** `c_t = c_s`
  is precisely the emergent-Lorentz output (isotropic light cone). The repo's
  own notes say so: `c_t = c_s` is "itself the emergent-Lorentz output"
  (`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`), and the magnitude chain
  lives in the Euclidean branch where this isotropy is a *choice*
  (`docs/P2_EUCLIDEAN_VS_LORENTZIAN_FORK_2026-06-05.md`). A primitive must not
  be the answer to a derivation (principle 2).
- **(b) On a lattice it is a RENORMALIZED tuning condition, i.e. dynamical
  content.** The bare anisotropy and the renormalized anisotropy differ:
  `xi_R != xi_bare`, related by interaction-dependent **Karsch coefficients**.
  Setting the *renormalized* `c_t = c_s` (`xi_R = 1`) is a dimensionless
  **dynamical** tuning, not a structural graining fact — exactly the
  lattice-gauge-theorist objection. This is *not* the analogue of cubic
  adjacency (which is kinematic and interaction-independent).
- **(c) It presupposes an emergent TIME direction nothing supplies.** "`c_t`"
  requires an emergent time axis; the foundation posits none. This dependence is
  routed specifically to gate **G-TIME** (emergent time axis), with G-DYN
  upstream (see §8).

**PROPOSED corrected wording (paste-ready) — primary route: ADMITTED INPUT:**

> ### Kinetic-form anisotropy condition (admitted input — Tier-A; not a
> primitive)
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
> an emergent time direction, which is supplied by the dynamics/time gate (§8),
> not by this statement. It is therefore registered as a **Tier-A admitted
> input** (in `docs/audit/data/tier_a_admissions.json`), **not** as an
> axiom-premise primitive: dependents chain-satisfy only at `retained_bounded`
> until the condition is retired by a retained derivation.
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
> a claim of generic marginal radiative instability. (The earlier "tuned point,
> not a protected one" phrasing overstated the residual against this theorem and
> is corrected here.)
>
> **Explicitly dropped claims.** The phrases "free structural datum" and
> "analogue of cubic adjacency" are **withdrawn**: cubic adjacency is kinematic
> and interaction-independent (axiom A1), whereas `xi_R = 1` is a renormalized
> dynamical condition. The two are **not** the same category.

**PROPOSED corrected wording (paste-ready) — ALTERNATIVE route: DERIVED
TARGET.** If the owner prefers, record instead:

> ### Emergent kinetic isotropy (derived IR-fixed-point target; open)
>
> **Target.** `xi_R = c_t/c_s -> 1` as an **infrared fixed-point** property of
> the emergent dynamics (supplied by §8): isotropy of the matter light cone is
> a *consequence* to be derived (emergent Lorentz invariance in the IR), not an
> input. Until a retained derivation closes it, the IR isotropy of the matter
> kinetic form is an **open derived target** carrying the same marginal-Lorentz-
> violation / radiative-stability residual; rows that need `xi_R = 1` cite this
> target as an open dependency, not as an axiom or primitive.

**Notes.** The substantive verdict is identical on both routes: `c_t = c_s`
**leaves the axiom-premise registry** (`axiom_premise_nodes.json`). The primary
route (admitted input) is the weakest move that resolves the objection while
keeping the framework's magnitude chain usable (it can still *cite* the
admission, bounded). The alternative (derived target) is cleaner physics but
owes a derivation now. Both versions (i) state `xi_R` is **renormalized**, (ii)
carry the radiative-stability residual, (iii) drop "free structural datum /
analogue of cubic adjacency", and (iv) route the emergent-time dependence
through §8. This is the single largest premise-count reduction in the proposal:
the approved-primitive count drops by one.

**Registry-of-record route (proposed primary).** The **admitted-input** route is
proposed as the registry-of-record because it keeps the magnitude/Lorentz chains
*usable* (they chain-satisfy at `retained_bounded` rather than going fully open).
The **derived-target** route is the cleaner physics but leaves those dependents
*open* until a derivation lands; the two routes carry **different audit
semantics**, so the owner must select one — both are offered here, primary route
flagged, final selection is the owner's.

**This is a DECISION REVERSAL, not housekeeping (must be surfaced).** The current
registry and `AXIOM_MINIMALITY_POLICY.md` §6 (entry **2026-06-09**) record an
explicit **owner approval** of `kinetic_isotropy_primitive` *as a primitive*, on
the stated ground that `c_t = c_s` is "a dimensionless **structural** ... of the
same category as cubic adjacency ... **not** dimensionless **dynamical**
content." This proposal asserts the **opposite** (it **is** renormalized
dynamical content; the cubic-adjacency analogy is **withdrawn**). The re-tier is
therefore an **un-adoption of a logged owner approval** and a registry/policy
edit — it cannot land without the owner **reversing** the 2026-06-09 approval and
the independent audit lane re-auditing. It is presented here as a proposed
reversal for owner decision, **not** as neutral housekeeping (`proposal_allowed=false`).

---

## 6. (Derived from §1 + §5) Where spatial isotropy and the kinetic form now live

For clarity (not a new posit): after §1 and §5, spatial axis-interchange is a
**discrete `B_3` graph fact** (axiom A1, kinematic), the **continuous** spatial
isotropy `a_x=a_y=a_z` and the **space-time** kinetic-form isotropy `xi_R=1` are
**not** axioms — the former is an emergent/derived statement and the latter is
the admitted/derived condition of §5. No row may conflate the three. This
paragraph is bookkeeping; it adds no premise.

---

## 7. P3 REALIZED-STATE — DISAMBIGUATE (fold in the guard; own the commitment)

**Tier:** primitive (retained), with the counterfactual-test guard folded **into**
the primitive statement and the single-world / actualization commitment owned.

**Current wording** (`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`, "The
Primitive"):

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

**Objection it resolves (panel P3):** when judged **bare** (statement only, no
source-note context), P3 drew a 0-pass / 10-concern reading. The genuine fix is
to make the statement **self-sufficient on a bare reading** by consolidating its
guards and adding the two pieces that were **not** previously stated outright.
*Diagnosis correction (per adversarial re-check):* the
**counterfactual-test guard** ("a quoted number that would differ under another
law-admissible state is registered data") is **not** absent from the canonical
note — it already appears in its `## The Primitive` block (the "no quoting a
number that would differ ..." clause) and in `## What This Declares`. So the
accurate framing is **"consolidate and make explicit"**, not "fold in a missing
guard." The genuinely new content this revision adds is **(a)** the explicit
**one-world / actualization (initial/boundary-condition) commitment**, and
**(b)** the **cross-link to A3a/A3b** disambiguating the two senses of "realized"
("realized state" = the supplied physical configuration; "realized outcome" = the
recorded event identified in §3b) — neither of which was stated outright before.

**PROPOSED corrected wording (paste-ready):**

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
> `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`.

**Notes.** The change is conservative: the primitive's *content* is unchanged.
The counterfactual-test guard is **consolidated into one self-contained block**
(it already lived in the canonical note's `## The Primitive` / `## What This
Declares` sections — see diagnosis correction above — so this is consolidation,
not repair of an absent guard), and the two genuinely new pieces are made
explicit: the **one-world / actualization** commitment (stated outright rather
than implied) and the explicit **cross-link to §3a/§3b** disambiguating the two
"realized" senses. *Boundary-vocabulary watch:* P3 names the realized state an
"initial/boundary-condition input" while the **past hypothesis** (also a
boundary-condition claim) is held **out**; the distinction is the single
supplied datum (allowed) vs a *specialness/atypicality claim* about that datum
(forbidden here → routed to G-ARROW, §8). The shared vocabulary is intentional
but the two are not the same input; the past-hypothesis hold-out is preserved.
P3 stays a primitive because, so guarded, it carries no contingent content
(principle 2) and is a genuine laws-vs-initial-conditions floor.

---

## 8. SYSTEM gap — DYNAMICS + EMERGENT-TIME AXIS: a REQUIRED OPEN GATE (not a new axiom)

**Tier:** **open-gate** (explicitly flagged required gate), **not** an axiom and
**not** a primitive.

**The gap (panel SYSTEM, under-completeness):** a **dynamics / time-evolution**
(transfer matrix / Hamiltonian / action with reflection positivity) **and** an
**emergent time axis** are *presupposed* by P2 (`c_t`) and by A3b (the
coarse-graining that yields sectors, and the irreversibility behind "durable")
but are **posited nowhere**. They must be made explicit — either as a stated
posit or as an explicitly flagged required open gate — never silently
presupposed.

**My judgment: flag it as a REQUIRED OPEN GATE, do not add a dynamics axiom.**
Reasons:
1. **Minimality / weakest change (principle 5).** A dynamics axiom (an action,
   a Hamiltonian, a transfer matrix) is *much* heavier than the gap requires and
   would import selector/dynamical content the framework deliberately keeps out
   of its axioms. The existing foundation already lists "arrow, measurement,
   decoherence, record-production dynamics, and physical persistence dynamics"
   and "source/action" as **open gates outside the axioms**
   (`MINIMAL_AXIOMS_2026-06-05.md`, "Open Gates And Admissions Outside The
   Axioms"). The governance rule (`docs/audit/AXIOM_MINIMALITY_POLICY.md` §1, §4)
   is explicit: when a lane needs an extra axiom, **do not add the axiom** —
   record it as a flagged decision and land a boundary note. Adding a dynamics
   axiom would violate that rule.
2. **It is already a downstream `bounded_theorem`/open-gate cluster, not a
   premise.** The repo *derives* its evolution from supplied transfer data: the
   reflection-positivity 2-step transfer matrix `T̂²`
   (`docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`) feeds
   the single-clock generator `H := -(1/(2 a_tau)) log(T̂²/M_T)` and
   `U(t)=exp(-itH)`
   (`docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`),
   which itself states "**the axis is a premise, not a derivation**". And Gate B
   dynamics is an explicit `open_gate` (`docs/GATE_B_DYNAMICS_NOTE.md`). So the
   honest status of "dynamics + time axis" is a **required open gate that
   downstream theorems are conditional on**, not an axiom.
3. **Anti-smuggling (principle 4).** The point is precisely to stop the silent
   presupposition. A flagged gate satisfies that: P2 (§5) and A3b (§3b) now name
   it as an explicit dependency, and the irreversibility/arrow content removed
   from Record (§3a) lands here, owned.

**PROPOSED gate flag (paste-ready) — add to the foundation's "Open Gates"
section, NOT to the axiom list:**

> ### Required open gate: dynamics + emergent time axis (flagged, not an axiom)
>
> The foundation (axioms A1, A2, A3a; primitives P1, P3) supplies **no**
> dynamics and **no** time. The following are therefore **required open gates**,
> on which several downstream statements are explicitly conditional; they are
> **flagged here so they are never silently presupposed**, and they are **not**
> promoted to axioms or primitives:
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
>   (§3a). It is held here as a required gate and remains the residual of the
>   past-hypothesis / arrow note
>   (`docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`).
>   It is **not** an axiom and is **not** supplied by P3.
>
> Any row that uses an evolution law, an emergent time direction, a
> superselection/coarse-graining (center-producing) map, or record durability
> must cite the relevant gate (G-DYN / G-SECT / G-TIME / G-ARROW) as an explicit
> open dependency.

**Notes.** This is the decisive call the prompt asks for: **flag, do not
axiomatize.** Four sub-gates (dynamics G-DYN, center-producing coarse-graining
G-SECT, time axis G-TIME, arrow G-ARROW) absorb exactly the content that was
being smuggled — by P2 (`c_t`, via G-TIME), by A3b (the center-producing map `E`,
via G-SECT — split out from G-DYN because RP-dynamics keeps a factor a factor),
and by Record's "durable" (the arrow, via G-ARROW). It coheres with the framework's
existing open-gate list and with the binding minimality policy's "do not add the
axiom" rule. Adding a dynamics axiom is *unwarranted* (principle 5) and would
*contradict* the policy; a flagged required gate is the correct, weakest,
non-smuggling resolution.

---

## 9. First-principles criteria the minimality policy should encode

Stated from physics, generally (not by citing the current policy). A premise
surface is admissible iff every member satisfies the criterion for its tier:

1. **Axiom non-circularity (no disclaim-while-use).** An axiom may not consume
   structure it disclaims supplying. If a statement's content references a
   decomposition, conjugation, metric, sector label, basis, generator set, or
   ordering, that object must be supplied — by this axiom, by another posit, or
   by an explicitly flagged open gate. *Test:* list every mathematical object the
   statement *uses*; each must have a supplier inside the premise surface or a
   flagged gate.

2. **Primitive single-datum purity.** A primitive is **one** narrow accepted
   datum carrying **no** dynamical, selector, renormalized, or empirical content.
   It must not be a *consequence* of the other posits (else it is a derived
   result), and it must not be a *tuning condition* (a renormalized value differs
   from its bare value via interaction-dependent coefficients ⇒ dynamical ⇒ not
   primitive). *Test:* (a) can it be derived from the rest? If yes, it is
   derived, not primitive. (b) Does setting it require renormalized (not bare)
   values? If yes, it is an admitted dynamical input, not a primitive. (c) Does
   it fix a mass ratio / coupling / angle / phase / count? If yes, it is
   empirical/selector content, not primitive.

3. **Kinematic vs dynamical classification.** Distinguish **kinematic /
   interaction-independent** structure (lattice geometry, point group, graph
   metric, algebraic carrier — admissible at axiom or primitive grade) from
   **dynamical / interaction-dependent** structure (anything whose value flows
   under renormalization, any emergent-symmetry output, any IR fixed-point
   property). Dynamical content is **never** a primitive; it is an admitted input
   (Tier-A, bounding) or a derived target. *Test:* does the quantity run / get
   renormalized / emerge in the IR? If yes, it is dynamical.

4. **Theorems are not premises.** A statement that is a theorem of a richer,
   not-yet-established structure may not be posited as a premise. Posit only the
   **bare object** the theorem would hand you (e.g. an antiunitary involution
   `K`, not "CPT"; a positive transfer operator, not "the Hamiltonian is
   bounded below as a relativistic spectrum-condition theorem"), and only its
   **existence**, with no theorem-strength corollaries. *Test:* is the named
   object provable elsewhere as a theorem (in this repo or in standard QFT)? If
   yes, replace the name with the bare object + existence hypothesis.

5. **Explicit accounting of arrow / time / dynamics / decomposition /
   conjugation (no smuggling).** Any irreversibility or arrow of time, emergent
   time axis, evolution law, central/superselection decomposition, or conjugation
   that is *used anywhere downstream* must be **either** a stated posit **or** an
   explicitly flagged required open gate. Silent presupposition is inadmissible.
   *Test:* grep the downstream corpus for uses of time, evolution, durability,
   sectors, conjugation; each must trace to a posit or a flagged gate.

6. **Factor/center honesty.** Do not posit a "sector decomposition",
   "superselection", or "central orbit" on an algebra that is a **factor**
   (trivial center). Such structure requires an explicitly supplied
   center-producing map (gauge / coarse-graining / superselection). *Test:* is
   the algebra a factor? If yes, any sector talk needs a named supplier.

7. **Weakest sufficient change / minimality of premises.** When a gap appears,
   prefer the *weakest* admissible repair: prefer a flagged open gate to a new
   axiom; prefer demotion (axiom→primitive→admitted input→derived target) to
   addition; prefer annotation to rewording. Adding a premise (axiom or
   primitive) is the **last** resort, allowed only when no derivation, flagged
   gate, identification, or bounded composition suffices. *Test:* enumerate
   demotion/flag/annotate options before any addition.

8. **Self-sufficiency of a stated premise (bare-reading test).** A premise must
   carry its own load-bearing guards **inside** its statement. If its good
   standing depends on a guard living only in surrounding prose (as P3's
   counterfactual test did), the guard belongs in the statement. *Test:* judge
   the statement alone, with no source note — does it still pass?

9. **Tier provenance and downstream-citation discipline.** Each premise is
   tagged with its tier (axiom / primitive / admitted-input / derived-target /
   open-gate), and downstream rows must cite the **correct** tier. An axiom may
   not be cited for content it explicitly does not supply (e.g. A1 for
   continuous isotropy). *Test:* for each downstream citation, does the cited
   premise actually supply the cited content at the claimed tier?

---

## 10. Adoption consequences (if the owner + audit lane adopt)

> These are the downstream status changes that **would** follow adoption. This
> draft adopts nothing; the audit lane sets all effective statuses.

1. **Registry change (`axiom_premise_nodes.json`).** `kinetic_isotropy_primitive`
   is **removed** from `canonical_ids`/`nodes` and **moved** to
   `tier_a_admissions.json` as a renormalized-anisotropy admission (primary
   route) — **or** recorded as an open derived target (alternative route). The
   approved-primitive count drops from 3 to 2 (P1 scale-reference, P3
   realized-state). `minimal_axioms` source content changes (A1 annotation, A2
   amendment, A3 split into A3a axiom + A3b conditional).

2. **P2-dependent rows are re-tiered `retained_bounded`.** Every row whose only
   otherwise-clean dependency was the kinetic-isotropy primitive (e.g. the
   emergent-Poincaré / kinetic-isotropy theorem cluster, the staggered-Dirac
   kinetic-class rows, the graviton-isotropy rows) **loses** its chain-satisfy
   pass and becomes `retained_bounded` (bounded by the new admitted input) or
   open (if the derived-target route is taken), until a retained derivation
   retires the condition. These rows must be re-audited.

3. **A3b consumers must be re-audited.** Rows that cited "Record" for the
   **K/CPT-orbit selector** (the generation-sector-count usage; the
   determinant/character phase-erasure rows that lean on the K/CPT orbit; see
   `docs/P2_KCPT_ORBIT_TEMPORAL_FACTOR_NO_GO_2026-06-06.md`,
   `docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`)
   must re-cite **A3b (conditional)** and carry the `E` (center-producing map),
   `K` (antiunitary existence), and realized-configuration hypotheses as
   explicit dependencies. Rows that only used **finite additivity** keep citing
   A3a (axiom) and are **unaffected**.

4. **New required-gate dependencies appear.** Rows using an evolution law, an
   emergent time direction, a center-producing superselection/coarse-graining
   map, or record durability now carry explicit
   **G-DYN / G-SECT / G-TIME / G-ARROW** open-gate dependencies. The
   reflection-positivity and single-clock notes become the conditional suppliers
   of G-DYN/G-TIME; the center-producing map `E` (G-SECT) needs an *additional*
   coarse-graining/limit/gauge ingredient beyond RP-dynamics; the
   past-hypothesis/arrow note remains the supplier of G-ARROW.

5. **A2 Clifford-reading consumers re-audited.** Rows that used Clifford
   generators, chirality/pseudoscalar, or a real-form conjugation drawn from "the
   Cl(3,0) reading of A2" must now cite the **labelled downstream identification**
   (the qubit-interpretation / Cl(3) uniqueness notes) and own those choices.
   Rows using only `M_2(C)` are unaffected.

6. **A1 isotropy-citation sweep.** Any row citing A1/Lattice as the source of
   **continuous** spatial isotropy or a Lorentz/relativistic statement must be
   corrected to cite the appropriate emergent/derived source; A1 supplies only
   `B_3`/`O_h` and the `L1` graph metric.

7. **Hash-guard re-audit (mechanical).** Editing `MINIMAL_AXIOMS` content
   invalidates prior direct `minimal_axioms` audits via the axiom-premise hash
   guard (as the 2026-06-05 refinement already did); all direct
   `minimal_axioms` dependents must be re-audited by the independent lane.

8. **Policy update (`AXIOM_MINIMALITY_POLICY.md`).** Section 6 records the
   removal of `kinetic_isotropy_primitive` from primitive class and the addition
   of the §9 first-principles criteria as the admissibility test for future
   premise proposals. No new axiom is added (the dynamics gap is a flagged gate,
   per §8). **This explicitly reverses the logged 2026-06-09 owner approval** of
   `kinetic_isotropy_primitive` as a primitive; the reversal is a science-level
   owner decision, recorded as such, not a housekeeping edit.

8a. **Tier-honesty re-audit obligation (adoption-time).** The P2-dependent rows
   that previously chain-satisfied *for free* via `kinetic_isotropy_primitive`
   must be **actively re-audited to `retained_bounded`** (admitted-input route)
   or **open** (derived-target route) — they must **not** be left silently at
   their old axiom-grade status. The registry move is honest only if the
   downstream ledger is refreshed in the same adoption.

9. **Net premise-count effect.** Axioms: still 3 by name, but Record is now
   honestly **A3a axiom + A3b conditional** (one of the three "axioms" is
   demoted in half). Primitives: **3 → 2**. New explicit open gates: **+3**
   (G-DYN, G-TIME, G-ARROW) — but these *replace silent presuppositions*, so the
   honest premise content **decreases**, not increases, while becoming auditable.

---

## 11. Summary table

| Item | Verdict | Tier change | Core move |
|---|---|---|---|
| A1 Lattice | passes | axiom (unchanged) | annotate: name `O_h`/`B_3` + `L1` metric; isotropy citation guard |
| A2 Quantum | passes | axiom (unchanged) | keep `M_2(C)`; declare scalar field `C`; relocate `Cl(3,0)` reading to labelled downstream id |
| A3 Record | **fails 10/10** | **split** | A3a = finite-additivity valuation (axiom); A3b = realized-outcome id (conditional/derived), `K` not CPT, center via supplied map, drop "durable" |
| P1 scale-reference | passes cleanly | primitive (unchanged) | optional: abstract anchor `M_0`, move `=M_Pl` to gravity gate |
| P2 kinetic-isotropy | **fails 10/10** | **demote: primitive → admitted input** (or derived target) | `xi_R=1` renormalized dynamical condition; carry LV/radiative residual; drop "free datum / cubic-adjacency analogue" |
| P3 realized-state | concern when bare | primitive (retained) | fold counterfactual guard into statement; own one-world commitment; cross-link to A3 |
| SYSTEM (dynamics+time) | under-complete | **new open gate (not axiom)** | G-DYN / G-SECT / G-TIME / G-ARROW required-gate flags; no dynamics axiom |

---

*End of proposal. Adopt nothing from this file without explicit owner approval
recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md` and the machine registry,
and without independent audit-lane review. `proposal_allowed=false`.*
