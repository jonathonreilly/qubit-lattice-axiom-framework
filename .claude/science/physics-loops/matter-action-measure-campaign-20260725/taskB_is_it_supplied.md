# TASK B — Is common-frame covariance SUPPLIED?

**Date:** 2026-07-25. Worked against `origin/main` (fetched; tip
`4097451e9a`). No commit, no push, no PR. This report file is the only file
edited in the repo; the runner lives in the session scratchpad. **No audit
verdict is set or predicted anywhere below.**

**Mandatory framework surfaces read:**
`docs/MINIMAL_AXIOMS_2026-06-29.md` (all four axioms, the Qualification, the
"Relation To Dynamics" section, and the Open-Gates list);
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`;
`docs/audit/data/axiom_premise_nodes.json` (four canonical ids:
`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive` — none of them supplies a frame, a transport, a
dynamics, or a source/action).

**Runner (mine, exact sympy, no float is an input to any load-bearing
comparison):**
`/private/tmp/claude-502/.../scratchpad/taskB_covariance_group_commutants.py`
— **PASS=54 FAIL=0**. Every commutant is obtained by *solving* the
commutation system natively; every claimed containment is checked in both
directions; every claimed constant carries a construction-mutation partner.

---

## BOTTOM LINE

The question as posed ("forced, or supplied?") has a **false dichotomy** in
it, and the true answer is sharper than either horn.

"Common-frame covariance" is a **conjunction of two independent things**, and
they have opposite statuses:

| component | content | status |
|---|---|---|
| **(H4a) correlation** | the two endpoint frames are locked to each other by *some* fixed comparison — the covariance group on an edge is a **twisted diagonal** `{(u, v u v†)}`, not the independent product | **FORCED**, conditional on one axiom reading (below) — and forced by **Admissibility**, not by Qubit |
| **(H4b) flatness** | the twist is trivial (`v = I`) uniformly, i.e. the comparison has **no holonomy** | **SUPPLIED**. Nothing in the axioms or the registry selects it. Already named as a choice on main since 2026-06-08/09 |

And the payoff, which inverts Wave 2's limitation L1:

> **The two-point menu does NOT depend on the supplied part.** The commutant
> of a twisted diagonal has complex dimension **exactly 2** for *every* twist
> (gate `C3b`), and the separating invariant — ground-sector degeneracy 1 vs
> 3 — is **conjugation-invariant**, so it is identical for every `v` (gates
> `C3f`). Dropping flatness does not dissolve the menu; it **enlarges** it, by
> adding a link field. The underdetermination is real and is understated by
> the two-point framing, not manufactured by it.

What creates the menu is not a frame convention. It is the **Admissibility
axiom's content-sensitivity** — the "vary with the nearest-neighbor
conditions" clause. That clause is a cross-site comparison, and it is
axiom content.

---

## (a) THE STRONGEST CASE THAT IT IS SUPPLIED — and how far back it goes

### The case, stated at full strength

Nothing in the axioms names a map between the one-site algebras at two
different sites.

- Lattice (`MINIMAL_AXIOMS_2026-06-29.md:37-41`) supplies sites, adjacency,
  translations, proper cubic rotations, and: *"No site is privileged. Sites
  are distinguished by the supplied lattice structure alone."* Nothing about
  internal frames.
- Qubit (`:45-53`) supplies *"The full one-site possibility domain has
  algebraic presentation `M_2(C)`"* and *"No possibility is privileged.
  Possibilities are distinguished by the supplied algebraic structure
  alone."* This is a statement about **one** site. `Aut(M_2(C)) = PU(2)`, so
  the identification `A_x ≅ A_y` is a `PU(2)`-torsor with no distinguished
  point.
- The Qualification (`:76-79`) then bites: *"Further physical structure
  requires a retained derivation or bridge, or explicit approved-primitive
  registration... A choice not fixed by the supplied structure remains a
  named conditional or open dependency."*
- And `:170` puts *"source/action and physical-observable identification"*
  outside axiom content, while `:105-110` says Admissibility *"is not a
  dynamics axiom"* and *"does not choose a Hamiltonian or transfer
  operator."*

So on the face of it: the frame comparison is exactly "a choice not fixed by
the supplied structure."

### Where it first enters the corpus, traced back

It enters **as a definition wearing a theorem's clothes**, and it predates
the four-axiom reset.

1. **2026-04-10 — imported, pre-axiom.**
   `docs/STAGGERED_FERMION_CARD_2026-04-10.md:5-7` and
   `docs/GRAPH_DIRAC_REQUIREMENTS_2026-04-10.md:23-24,65` already run a
   Kogut–Susskind staggered operator with *"a nearest-neighbor hopping
   operator"* and *"oriented hopping"*. Writing `χ̄_{x+μ̂} χ_x` at all
   presupposes that the internal index at `x` and at `x+μ̂` are the same
   index. This is wholesale external architecture; there is no axiom in
   sight (the earliest axiom path aliased in `axiom_premise_nodes.json` is
   `MINIMAL_AXIOMS_2026-05-20.md`). So the frame identification is older
   than the axioms it is now supposed to follow from.

2. **2026-05-25 — the definitional moment. This is the true origin.**
   `docs/TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md:43-47`
   defines the translation operator:

   > ```text
   >     T_a · ( ⊗_{x ∈ Λ}  |b_x⟩_x )  :=  ⊗_{x ∈ Λ}  |b_{x - a}⟩_x.        (2)
   > ```

   Note the `:=`. The label `b` ranges over **one** two-element label set
   that is shared by every site by fiat. **That shared label set is the
   common frame.** It is not derived, not declared as a premise, and not
   flagged: it is smuggled in by the notation of a definition.
   Ledger: `retained_pending_chain`.

3. **2026-05-02 — the identity that makes it look derived.**
   `docs/TRANSLATION_COVARIANCE_LOCAL_OP_THEOREM_NOTE_2026-05-02.md:5-9`
   states as a `positive_theorem`:

   > *"every single-site matrix operator `M_x` in the local `M_2(C)` factor
   > translates by tensor-factor relabeling, `T_a M_x T_a^dag = M_{x+a}`."*

   This identity **is** the common frame: the *same matrix* `M` at `x`
   becomes the *same matrix* `M` at `x+a`. It is a true theorem — about the
   trivialization chosen in step 2. Ledger: `unaudited`.
   Same date, `docs/HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md:10`
   ships `H_{xy} = a_x^† a_y + a_y^† a_x` as *"translation-covariant"* on
   that surface. Ledger: `unaudited`.

4. **2026-06-08/09 — the corpus catches it, in the colour sector.**
   `docs/FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md:83,99-101`:

   > **"(F3) The flat `U=I` link is a trivialization choice."** … *"the
   > translation bridge's `U=I` reference is the flat choice of coordinates
   > on neighbouring fibres, not an invariant physical rule that pins the
   > fibre basis at `x` to the fibre basis at `y`."*

   and `:78-80`: *"The only fibre operator invariant under conjugation by all
   local `U(3)` frame changes is a scalar multiple of `I_3`."*
   `docs/MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md:33-35`:
   *"the translation bridge's `U=I` reference is the flat cross-site
   trivialization rather than an invariant physical fibre pinning. With that
   bridge, frame-independent nearest-neighbour hopping uniquely requires a
   compensating link transporter with the lattice connection law."*
   Both `unaudited`.

5. **2026-07-02 — the axiom-level admission.**
   `docs/INFORMATIVE_FRACTION_COVARIANT_RULE_QUANTIZATION_OCCUPANCY_RESIDUAL_THEOREM_NOTE_2026-07-02.md:183`:
   *"The axiom fixes the covariance class of the rule, quoted above, not the
   selected rule."* And `:189` declines to settle whether *"No possibility is
   privileged"* constrains the rule at all, computing **both** variants.
   Corroborated by a ledger row:
   `docs/audit/data/ledger/re/record_local_finite_atom_availability_narrow_theorem_note_2026-06-17.json:610`
   — *"the fixed admissibility rule's content is unspecified, no possibility
   or basis is privileged."*

6. **2026-07-06 — the corpus argues the FORCED side.**
   `docs/COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md:75-79`:
   *"Realizing it as an operator `S` ON `C^2_x tensor C^2_y` requires an
   identification of the two site domains. **The Qubit axiom itself supplies
   that identification**: both domains carry the same supplied algebraic
   presentation (`M_2(C)`)…"* — but the same note then retracts most of it at
   `:96-101`: *"an INDEPENDENT per-site presentation change (`g tensor 1`)
   does not commute with `S` and moves the split… its stability group is the
   diagonal. **Comparing presentations across sites is exactly the transport
   question left to later blocks; nothing here supplies it.**"* `unaudited`.

7. **2026-07-14 — named as a premise, with no authority.**
   `docs/work_history/repo/review_feedback/QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:39,42-50`
   (`Authority: none`, no claim id, no ledger row): *"'No possibility is
   privileged' does not itself say whether local basis changes act together
   or independently"*; *"Promoting the exchange result without choosing and
   defending the covariance meaning would hide a new physical premise in a
   symmetry slogan."*

8. **2026-07-25 — registered as (H4)** in PR #5602
   (`docs/COMMON_FRAME_PAIR_GENERATOR_EXCHANGE_CLASS_BOUNDED_THEOREM_NOTE_2026-07-25.md:81-82,156-166`).
   Not on `origin/main`; no ledger row exists for it.

**Verdict on (a):** derived — no. Declared — only from 2026-07-14 onward,
and only on `Authority: none` surfaces until PR #5602. **Silently used —
yes, from 2026-05-25, by a `:=` in the definition of `T_a`.** It is older
than the axiom set that is now asked to justify it.

---

## (b) THE DECISIVE TECHNICAL QUESTION — what the framework actually licenses

### The commutant table (all exact, all solved natively)

Complex dimension of `{M ∈ M_4(C) : [M, g] = 0 ∀ g}` on one qubit edge:

| covariance group on the edge | dim | the algebra | gate |
|---|---|---|---|
| **diagonal `SU(2)`** (`u ⊗ u`) | **2** | `span{I, SWAP}` | `C1a`,`C1b` |
| **independent** `SU(2) × SU(2)` (`u₁ ⊗ u₂`) | **1** | scalars only; `SWAP ∉` | `C2a`,`C2b`,`C2c` |
| **twisted diagonal** `{(u, v u v†)}` | **2** | `span{I, SWAP_v}`, `SWAP_v = (I⊗v)SWAP(I⊗v†)` | `C3b`,`C3c` |
| **diagonal `2O`** (framework's own proper cubic rotations, lifted) | **2** | still exactly `span{I, SWAP}` | `C5a`,`C5b` |
| **independent `2O × 2O`** | **1** | scalars only | `C5c` |
| diagonal `U(1)` (a rule naming an axis) | 6 | — | `C6a` |
| independent `U(1) × U(1)` (both endpoints record-locked) | 4 | — | `C6b` |
| one site only, `SU(2) × {1}` | 4 | — | `C6c` |
| trivial group | 16 | full Hermitian pair space | `C6d` |

Three facts in that table are load-bearing and, to my sweep, **new**:

- **The menu does not need continuous `SU(2)`.** The Lattice axiom's own
  *proper cubic rotations*, lifted to the spinor as the binary octahedral
  group `2O ⊂ SU(2)` (48 elements, all built exactly from unit quaternions
  and verified unitary with `det = 1`, `C4a`–`C4c`), give commutant dimension
  **2**, and the **same** `span{I, SWAP}` (`C5a`,`C5b`). Reason: `O` is one
  of the three finite subgroups of `SO(3)` acting irreducibly on `R^3`, so
  the triplet stays irreducible. Shrinking to the framework-native finite
  group does **not** widen the menu.
- **Independence kills the pair law even at the finite group** (`C5c`,
  dim 1). The collapse is not an artifact of demanding full `SU(2)`.
- **`SWAP` restricted to the one-excitation sector *is* the hopping bilinear**
  `a_x^† a_y + a_y^† a_x` (`H1a`, exact). So this is not an analogy to the
  matter lane — it is the *same operator*. The twisted exchange reduces to the
  **link-dressed** hop (`H1b`).

### The classification theorem — which subgroup can it be?

Rebuilt from primitives, not cited:

- **`su(2)` is simple.** `ad_X` has rank 2 for `X ≠ 0`, and
  `span{X} + im(ad_X)` has rank 3, so every nonzero ideal is everything
  (`P1b`–`P1e`, with `ad_0` as the mutation control).
- **`Aut(su(2)) = SO(3) = Inn(su(2))`.** The Killing form is
  `K(X,Y) = −2⟨X,Y⟩` (rebuilt from `ad`, `P2b`), so an automorphism is
  orthogonal; the cofactor identity `(Gu) × (Gv) = cof(G)(u × v)` is verified
  as a **symbolic polynomial identity in all nine entries** (`P2a`), and it
  forces `det = +1` — a proper rotation is an automorphism (`P2c`), a
  reflection is not (`P2d`).
- **Consequence (Goursat).** A subgroup of `PU(2) × PU(2)` whose projections
  are both onto is either the whole product or the graph of an automorphism,
  i.e. a **twisted diagonal**. Cross-checked constructively: adjoining a
  single element outside the diagonal generates the whole 6-dimensional
  algebra (`C7a`), so **nothing sits strictly between** (`C7b`).
- **Transitivity.** `PU(2)` is transitive on the ray space; every proper
  closed subgroup is not — `U(1)_z` fixes the two poles (`C8a`), a finite
  group has a finite orbit in an infinite ray space (`C8b`, orbit size 6).

So once *"No possibility is privileged"* is read as forbidding the covariance
group from distinguishing rays, **only two commutant dimensions are
reachable: 2 (twisted diagonal) or 1 (independent).** There is no third
option and no continuum of options. Everything in the table with dimension
4, 6 or 16 requires the covariance group to privilege possibilities.

### Which framework object selects between 2 and 1? — **Admissibility, and only Admissibility**

Not Qubit. Not Lattice. Not Record. Not any registered primitive.

**Lemma (value-blindness under independent covariance).** Let the edge rule
assign `Avail(x | c) ⊆ Ω` given the neighbour condition `c`. If the rule is
equivariant under *independent* onsite relabelings, then setting the
neighbour's relabeling to the identity forces `Avail(x|c)` to be invariant
under the whole internal group; if that group is transitive on `Ω`, then
`Avail(x|c) ∈ {∅, Ω}`; and setting the site's relabeling to the identity
forces `Avail` to depend only on the *orbit* of `c`.

Verified by **exhaustive enumeration** on the framework's own two-value
domain with the value flip:

- `V2a`: of all rules, the independent-covariant ones number 2 — and **zero**
  of them narrow to a proper nonempty available set.
- `V2b`: every available set is `∅` or the whole domain (sizes seen: `[0, 2]`).
- `V2c`: **zero** independent-covariant rules vary at all.
- `V2d` (mutation): under **diagonal** covariance, proper nonempty narrowing
  *is* available — so the contrast is real, not an artifact of the model.
- `V1c`: the relational rule `Avail(c) = {c}` ("agree with the neighbour") is
  diagonal-covariant, narrows properly, and satisfies vary-with;
  `V1d` (mutation): it is **not** independent-covariant.
- `V3a` (mutation): with an **intransitive** internal group the lemma fails —
  so its load-bearing hypothesis is exactly transitivity, and that is exactly
  what "no possibility is privileged" is being asked to supply.
- `V4a`–`V4c`: adding "unrecorded" as a fixed extra symbol (the realistic
  six-neighbour setting) softens the kill to precisely its honest form —
  independent-covariant rules remain **content-blind** (`V4b`) but may still
  depend on **which** neighbours are recorded (`V4c`).

**The corpus's own Admissibility witnesses are content-sensitive, and
therefore are not independent-covariant.**
`docs/DYNAMICS_CONTENT_SORT_ORDERING_DERIVED_ACCUMULATION_IRREDUCIBLE_BOUNDED_NOTE_2026-07-03.md:127`
exhibits the vary-with clause as *"two sites with different neighbor
conditions carrying `{+1}` versus `{+1,-1}`"* — a **proper nonempty**
available set — and `:166` as *"a site just outside the saturated window is
**pinned to `{+1}`** by the recorded interior."* Gate `V1b` shows that exact
witness is not independent-onsite covariant.

### The exact gating

> **DICHOTOMY (exact, given (P1)).** Let the covariance group on an edge be
> the stabilizer of the supplied Admissibility rule.
>
> - **(P1)** *"No possibility is privileged"* forbids the covariance group's
>   projection to either factor from distinguishing rays ⇒ each projection is
>   all of `PU(2)`.
> - **(P2)** the Admissibility rule is **content-sensitive**: for some
>   neighbour condition the available set is a proper nonempty subset.
>
> Then **(P1) ∧ (P2) ⇒ the covariance group is a twisted diagonal and the
> Hermitian pair-generator menu has complex dimension exactly 2.**
> **(P1) ∧ ¬(P2) ⇒ independent covariance is available and the menu has
> dimension 1 — no nontrivial pair law.**
> **¬(P1) ⇒ dimension ≥ 4; the menu is strictly larger, never smaller.**

**(P1) and (P2) are axiom READINGS, not free physical premises**, and neither
is settled:

- (P1) is exactly the fork that
  `INFORMATIVE_FRACTION_...2026-07-02.md:100-102,189` flags and **refuses to
  adjudicate**, computing both variants. Meanwhile
  `EMPTY_STATE_BOOTSTRAP_...2026-07-04.md:144-146` uses the *opposite*,
  stronger reading — *"Rule covariance under proper cubic rotations then
  gives `g . A0 = A0` for every proper `g` **acting on contents**"* — which
  places the diagonal cubic group inside the covariance group outright and,
  by `C5a`, lands on dimension 2 immediately. **Both notes are `unaudited`.
  This is an unreconciled corpus fork on the load-bearing premise.**
- (P2) is the natural reading of *"the available possibilities are determined
  by, and vary with, the nearest-neighbor conditions"* (`:60-61`) and of the
  section title *"Admissibility / Local Constraint"*, and it is what both
  registered Admissibility exhibits actually do. But the literal sentence is
  also satisfied by the degenerate all-or-nothing behaviour, so (P2) is a
  reading, not a quotation.

### And what is left over after the theorem: the twist

`C3d` is the sharpest gate in the run: **the untwisted `SWAP` is not in the
twisted commutant.** "Dimension 2" does *not* pin the law — it pins the law
*given the twist*. On a lattice the twists `{v_e}` form a link field whose
**plaquette holonomy is gauge-invariant**:

- `T1a` (constructive, `3^3` window, 54 links): a pure-gauge link field
  `v_e = g_x g_y†` is trivialized to the identity exactly — a common frame
  **exists** and is constructive.
- `T1b`/`T1c`: after trivialization the residual freedom is exactly the
  **global constant**, which acts **diagonally** on every edge — a constant
  frame change preserves the identity links, a site-dependent one destroys
  them.
- `T1d` (mutation): a link field with **nontrivial holonomy admits no common
  frame at all**.

So *"common-frame covariance"* = *"the twist is flat."* That is (H4b), and it
is supplied. `H1c` rebuilds the passive-frame law natively in the qubit
sector — `G H[U=I] G† = H[g_x g_y†]` with `g_x g_y† ≠ I` — which is the
`FIBER_FRAME_...2026-06-09.md:83-101` (F3)/(F4) statement transplanted from
`U(3)` to `PU(2)`.

---

## (c) IF IT IS SUPPLIED — the honest blast radius

Only the **flatness** half (H4b) is supplied, so the blast radius is the
flatness premise, not the whole menu.

**Direct consumers of the `T_a M_x T_a† = M_{x+a}` / `U = I` trivialization.**
Measured on `origin/main`: **27 markdown surfaces** cite the 2026-05-25
tensor-product translation bridge or the 2026-05-02 hopping bilinear. Their
ledger statuses: **20 `unaudited`, 2 `meta`, 1 `audited_conditional`,
1 `retained_pending_chain` (the bridge itself), 3 with no ledger row.
Zero `retained`, zero `retained_bounded`.** They include the whole spine of
the matter lane:

`translation_covariance_local_op_theorem_note_2026-05-02`,
`translation_abelian_composition_theorem_note_2026-05-02`,
`momentum_charge_commute_theorem_note_2026-05-02`,
`hopping_bilinear_hermiticity_theorem_note_2026-05-02`,
`two_site_qubit_tensor_carrier_bridge_narrow_theorem_note_2026-06-06`,
`staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10`,
`staggered_kernel_satisfies_z_point_cone_certificate_narrow_theorem_note_2026-06-11`,
`axiom_first_fermionic_stefan_boltzmann_narrow_theorem_note_2026-05-26`,
`local_tomography_from_qubit_complex_structure_narrow_theorem_note_2026-06-03`,
`matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08`,
`fiber_frame_local_redundancy_bridge_narrow_theorem_note_2026-06-09`,
the three 2026-06-10 `p_flux_*` no-gos,
`p_flux_selection_via_fsb_k_and_z_certificate_conditional_theorem_note_2026-06-11`,
`gl_f_identification_bridge_decomposition_narrow_theorem_note_2026-06-11`,
`generated_finite_composition_minimality_theorem_2026-07-13`.
Also on the same surface but citing it indirectly:
`microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09`,
`transfer_matrix_log_quasilocality_narrow_theorem_note_2026-06-10`,
`gauged_log_transfer_quasilocality_combes_thomas_narrow_theorem_note_2026-06-13`,
`staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` — all
`unaudited`.

**Stated precisely, the inherited premise is not "a frame was chosen" but:**

> Every landed matter-sector surface that writes a **flat** cross-site kernel
> is a statement about the **zero-holonomy sector** of the qubit frame bundle.
> The framework's own colour lane already proved that independent local frames
> **force a connection**
> (`MATTER_GAUGE_MINIMAL_COUPLING_...2026-06-08.md:33-35`). The qubit matter
> sector as currently written has silently set that connection to pure gauge.

**Blast radius, sized:**

- **The two-point menu itself: NOT affected.** `C3b` + `C3f`: the dimension
  is 2 and the ground-degeneracy separator is 1-vs-3 for every twist. The
  underdetermination survives.
- **Any claim of the form "the cross-site kernel is `X`" (staggered phases,
  Kawamoto–Smit class, `Z`-point cone certificates, the `p_flux` family,
  quasilocality/Lieb–Robinson ranges, the RP kernels):** these are claims about
  `SWAP_v` with `v ≡ I`. They are correct **on the flat sector** and carry an
  unregistered flatness premise. This does not refute any of them; it names a
  premise they do not currently name.
- **Retained exposure: essentially none.** No row in the direct consumer list
  is `retained` or `retained_bounded`. The single `retained` neighbour,
  `graph_first_su3_integration_note`, is the colour-fibre surface and is
  *upstream* of, not downstream of, the flatness choice.
- **The `AC_φλ` / charged-lepton gate is not additionally damaged by this.**
  The two-point menu was never landed anywhere: PR #5602 is open, is not on
  `origin/main`, and **has no ledger row**. Literally zero landed results
  stand on the two-point menu today.

---

## (d) THE THIRD POSSIBILITY — independent covariance, no pair law at all

I take it seriously and it survives partially. Here are both readings,
honestly.

**Reading A — it is a reductio (the framework must intend common frames).**
If the axioms licensed independent onsite covariance, then by `C2a`/`C5c` the
Hermitian pair-generator space is the scalars, so there is no nearest-neighbour
matter law of *any* kind — no hopping, no exchange, no staggered kinetic term,
no Dirac operator. But the framework's Admissibility axiom is titled *"Local
Constraint"* and its own registered exhibits pin a neighbour's availability to
a **proper nonempty subset** determined by neighbour **content**
(`DYNAMICS_CONTENT_SORT_...2026-07-03.md:127,166`). Gate `V1b` shows that
witness is not independent-covariant. So independent covariance is not merely
awkward — it **contradicts the corpus's own worked instantiation of the
vary-with clause**. On this reading, Admissibility *is* the cross-site frame:
a content-sensitive nearest-neighbour rule is, by definition, a comparison of
the two sites' internal structure, and its stabilizer is the covariance group.
The framework never needed to supply a frame separately; it supplied one in
the Admissibility axiom and then forgot it had.

**Reading B — it is a genuine finding about reach.** Gates `V4a`–`V4c` are the
honest limit of the kill. With "unrecorded" present, an independent-covariant
rule can still depend on **which** neighbours are recorded, just never on
**what** they recorded. Such a rule satisfies the literal sentence *"the
available possibilities are determined by, and vary with, the nearest-neighbor
conditions"* — `Avail` is `∅` for some occupancy patterns and everything for
others, so it does vary. Under that reading the axioms license independent
covariance, and the matter sector is **empty**: dimension 1, no pair law. That
would be a very sharp negative about reach, and nothing in the axiom text
literally excludes it.

**Which does the evidence support? Reading A, but conditionally and with the
condition named.** Grounds, in order of weight:

1. **Both registered Admissibility exhibits are content-sensitive.** The
   framework's only two worked instantiations of the axiom
   (`DYNAMICS_CONTENT_SORT_...:127,166`) both narrow to a proper nonempty set
   by neighbour **value**, which Reading B forbids.
2. **Reading B guts the axiom it is reading.** Under B, Admissibility becomes
   a pure record-occupancy predicate: it can forbid a site from recording, but
   can never say *what* it may record. That drains "Local **Constraint**" of
   its constraint and makes the *"determined by"* half of `:60-61` vacuous.
3. **Reading B is self-defeating for the campaign's own target.** It does not
   merely remove the two-point menu; it removes the matter sector entirely,
   and with it every landed result in the list in (c). A reading that
   invalidates the whole corpus in one stroke is a reading to be stated and
   gated, not adopted.
4. **Counterweight, honestly recorded:** the axiom does **not** type
   "conditions". `COLOR_ARENA_...2026-07-06.md:119-122` says so explicitly —
   *"the axiom does not type 'conditions.' Whether a neighbor's condition is
   its record content, its possibility state, or other rule data is not fixed
   by the quoted sentence."* That untyped word is the entire remaining hole,
   and Reading B lives in it.

So: **not a reductio, and not a finding about reach either — it is a
well-posed fork that turns on a single untyped word in the Admissibility
axiom.** Typing "conditions" as record **content** closes it and forces the
menu; typing it as record **occupancy** closes it the other way and empties
the matter sector. The framework has never typed it.

---

## (e) VERDICT

**SPLIT VERDICT.**

1. **Common-frame covariance is not one premise. It is two, with opposite
   statuses.** The **correlation** (twisted-diagonal covariance group on an
   edge) is **FORCED** by Admissibility's content-sensitivity, conditional on
   (P1) and (P2), both of which are axiom readings rather than imported
   physics. The **flatness** (trivial twist, `U = I`) is **SUPPLIED**, has
   been named as a choice on main since 2026-06-08/09, and entered the corpus
   silently on 2026-05-25 in the `:=` defining `T_a`.

2. **Wave 2's limitation L1 is half wrong.** It is true that under independent
   covariance no pair law survives (`C2a`, and even `C5c`). It is **false**
   that the premise creates the menu: the menu is created by
   content-sensitivity of the Admissibility rule, and it **survives the
   supplied half untouched** — dimension 2 for every twist (`C3b`),
   ground-degeneracy separator 1-vs-3 for every twist (`C3f`).

3. **Dropping the supplied premise makes the framework MORE underdetermined,
   not less.** `C3d` + `T1d`: without flatness the law is `a I + b SWAP_{v_e}`
   with a link field carrying gauge-invariant plaquette holonomy. The
   two-point menu is a **lower bound** on the matter-law underdetermination,
   obtained by supplying away a connection.

4. **The genuine open gate is one untyped word.** Admissibility's
   "conditions" is untyped (`COLOR_ARENA_...2026-07-06.md:119-122`). Typed as
   record **content** ⇒ menu of exactly 2. Typed as record **occupancy** ⇒ no
   pair law at all. Nothing else can happen: gates `C7a`/`C7b`/`C8a`/`C8b`
   close off every intermediate dimension once (P1) holds.

**Confidence.**

- **High (≈0.93)** — the algebra: every commutant dimension in the table, the
  twist-invariance of the ground-degeneracy separator, the `2O` result, the
  `SWAP` = hopping identification, and the value-blindness lemma. All exact,
  all mutation-gated, PASS=54 FAIL=0. Failure mode would be a modelling error
  in the finite Admissibility model, not in the operator algebra.
- **High (≈0.90)** — that flatness is supplied and was smuggled in by the
  2026-05-25 definition. Two independent landed surfaces say so in the colour
  sector, and the `:=` is verbatim.
- **Medium-high (≈0.78)** — that the correlation half is forced. This rests on
  (P1)+(P2), and the corpus contains an explicit, unreconciled, both-`unaudited`
  fork on (P1) (`INFORMATIVE_FRACTION_...:189` refusing to adjudicate vs
  `EMPTY_STATE_BOOTSTRAP_...:144-146` acting on contents). If (P1) is read
  weakly the menu grows past 2 rather than shrinking, which would still
  contradict L1, but by a different route.
- **Medium (≈0.65)** — that Reading A over Reading B is the framework's
  intent. Grounded in both registered exhibits and in the axiom's own section
  title, but the untyped "conditions" is a real hole and the owner, not a
  worker, should type it.

---

## MANDATORY PRIOR-ART SWEEP — run on mathematical content, not wording

Swept `docs/`, `docs/work_history/**`, `scripts/`, and
`docs/audit/data/ledger/` shards for the **mathematics**, using multiple
independent spellings for each object (`commutant`, `Schur-Weyl`, `SWAP` /
`-SWAP` / `S`, `U ⊗ U` / `g tensor g` / `common basis` / `shared
presentation`, `independent onsite` / `g tensor 1` / `local frame` / `per-site
basis`, `trivialization` / `cocycle` / `coboundary` / `holonomy`, `Goursat` /
`twisted diagonal` / `graph of an automorphism`, `value-blind` / `available
set invariant`, `binary octahedral` / `2O`).

**Prior art FOUND — and it is substantial. I am not claiming these:**

- The diagonal-vs-independent commutant contrast (2 vs 1) and the
  common-vs-independent covariance fork:
  `QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:39-50`
  (work_history, `Authority: none`), and PR #5602's L1.
- The diagonal as the stability group of the exchange split, and the explicit
  statement that cross-site comparison is not supplied:
  `COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md:96-101`.
- "`U = I` is a trivialization choice, not a physical pinning", and
  `g_x U g_y†` as the passive-frame law:
  `FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md:83-105`
  (in `U(3)`).
- Independent local frames force a connection:
  `MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md:33-35,110-123`
  (in `U(3)`).
- "The axiom fixes the covariance class of the rule, not the selected rule",
  and the unsettled no-privilege reading:
  `INFORMATIVE_FRACTION_..._2026-07-02.md:19,183,189`.
- The rule's content is unspecified:
  `docs/audit/data/ledger/re/record_local_finite_atom_availability_narrow_theorem_note_2026-06-17.json:610`.
- Cubic covariance acting **on contents**:
  `EMPTY_STATE_BOOTSTRAP_..._2026-07-04.md:144-146`.

**No prior art found for (my new content):**

1. The **dichotomy theorem** — that (P1) closes the reachable commutant
   dimensions to exactly `{2, 1}` with nothing between, via `su(2)`
   simplicity + `Aut(su(2)) = SO(3)` + ray-transitivity.
2. The **value-blindness lemma** — that independent onsite covariance forces
   `Avail ∈ {∅, Ω}` and content-blindness, exhaustively enumerated, with the
   intransitivity mutation isolating the load-bearing hypothesis.
3. The **`2O` result** — that the framework's own finite proper cubic group,
   acting diagonally, already gives commutant dimension 2 and the same
   `span{I, SWAP}`.
4. The **twist-invariance of the separator** — dimension 2 and ground
   degeneracy 1-vs-3 for **every** twist, hence the menu survives supplying
   flatness.
5. The **split of (H4)** into a forced correlation half and a supplied
   flatness half, and the resulting inversion of L1.

**Anchor discipline.** All thirteen files cited above were checked with
`git diff --quiet origin/main -- <file>` and are **byte-identical to
`origin/main`**, so every `file:line` anchor resolves against `origin/main`.
The ledger was read from `git archive origin/main docs/audit/data/ledger`,
**not** from the local worktree — the worktree's ledger diverges from
`origin/main` by 1111 shard files and would have given wrong counts. (First
pass of this report used worktree counts; they are corrected below and every
individual row status was re-verified against `origin/main` and is unchanged.)

**Governance note (not a verdict).** Measured on `origin/main`: 3872 ledger
shards; `unaudited: 2712`, `meta: 356`, `retained_bounded: 336`,
`audited_conditional: 221`, `retained: 110`, `audited_failed: 56`.
Of **439** `no_go` rows, **438 are `unaudited` and 1 is
`audited_conditional`** — **zero retained `no_go` rows corpus-wide**, so no
foreclosure anywhere in this lane can be cited as retained authority. Every
single surface load-bearing for the question in this task —
`fiber_frame_local_redundancy_bridge` (2026-06-09),
`matter_gauge_minimal_coupling_...` (2026-06-08),
`color_arena_bonded_pair_...` (2026-07-06),
`informative_fraction_...` (2026-07-02),
`dynamics_content_sort_...` (2026-07-03),
`empty_state_bootstrap_...` (2026-07-04) — is **`unaudited`**, and the two
that fork on (P1) contradict each other while both being `unaudited`. No prose
status label was trusted anywhere in this report; every status above was read
from `docs/audit/data/ledger/` shards.
