# EXERCISE ONE — Assumptions ledger from the axioms up to the counting-bit blocker

**Date:** 2026-07-24. **Base:** `origin/main` @ `1652deb63b` (fetched).
**Scope:** exercise report only. No repo science surface edited, nothing committed,
no audit verdict asserted or predicted, no axiom or primitive proposed.

## Framework refresher — surfaces actually read before any conclusion

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (Lattice / Qubit / Admissibility / Record;
  Qualification; "Open Gates Outside The Axioms" list, which explicitly names
  `AC_phi_lambda`, weighting, normalization, probability, and formation rules as
  *outside* axiom content).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (three approved
  primitives; rule 5: no dimensionless quantity, selector, weighting rule,
  normalization rule, probability rule or readout bridge is granted).
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` (units conversion only, zero
  dimensionless content).
- `docs/audit/data/axiom_premise_nodes.json` (`canonical_ids` = `minimal_axioms`,
  `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive` — the complete supplied foundation).
- `docs/ai_methodology/skills/review-loop/SKILL.md` (axiom vs approved-primitive
  boundary; Record guardrails; no-go discipline gate; ledger-status discipline).
- `docs/repo/CONTROLLED_VOCABULARY.md` (checked; I propose **no new repo name** —
  see §6 note on `equal-sector locus`).

Per the exercise instruction, axioms and primitives are treated **as assumptions**
below, marked `AXIOM` / `PRIMITIVE` rather than as unquestionable.

**Verification.** Every algebraic claim marked **[gated]** was recomputed exactly
in sympy in this session (scratch runners; not repo files): **26 exact checks,
PASS=26 FAIL=0**. The load-bearing new computation (§7) was obtained by **two
independent implementations** — one applying the cone form to explicit matrix
products, one extracting group-algebra coordinates — which agree on the factored
residual `(2g_0 − g_1)·(…)`. The first run of the second implementation FAILED
against my own hand-analysis; the hand-analysis was wrong and the runner was
right (I had used componentwise multiplication in group-algebra coordinates,
where the product is a convolution). Recorded because it is exactly the failure
mode the repo's math-runner gate exists to catch.

---

## 0. The ledger in one line

Climbing from the axioms, the chain to `r` passes through **19 distinct
assumptions**. Only 4 are axioms/primitives, 5 are landed theorems with
retained-grade status, and **7 are conventions or unexamined habits**. Three of
those seven are load-bearing on the *value* of `r`, and one of them —
the choice of which weighting form on the C_3 cone is admissible — turns out
**not to be free at all** (§7).

---

## 1. Layer A — supplied foundation (treated as assumptions)

| # | Assumption | Where it enters | Class | What opens if it is wrong |
|---|---|---|---|---|
| A1 | Physical sites are `Z^3`, nearest-neighbour, proper cubic rotations about each site | `docs/MINIMAL_AXIOMS_2026-06-29.md:37-41` | AXIOM | The three-generation carrier is not "the three cube axes". The whole hw=1 taste-cube construction (§2) is downstream of cubic geometry; a different lattice gives a different generation count and no `C_3` at all. `d=3` is a Lattice primitive (memory: derivation experiment closed), so this row is *supplied*, not derived. |
| A2 | One-site domain is `M_2(C) ≅ Cl(3,0)`; no possibility privileged | `docs/MINIMAL_AXIOMS_2026-06-29.md:45-51` | AXIOM | The `C^8 = (C^2)^{⊗3}` taste cube of §2 evaporates. |
| A3 | Record: records form, lock one admissible possibility, permanent; **scalar readout `I` is additive over finite disjoint records, `I(∅)=0`** | `docs/MINIMAL_AXIOMS_2026-06-29.md:65-72` | AXIOM | This is the *only* axiom sentence with quantitative content anywhere in the chain. Additivity alone supplies **no weights on atoms** — every weight in §5–§6 is downstream of a separate bridge. If additivity were strengthened (e.g. to a *linear functional on the observable algebra*), §7's pin becomes axiom-grade instead of bridge-grade. |
| A4 | `realized_state_primitive`: pointwise evaluation at a supplied realized state; **no measure, no typicality, no weighting, no probability rule** | `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md:37-46` | PRIMITIVE | This primitive is the reason the counting bit cannot be discharged by "the realized state has weights `w`". A recorded `r` is data, not premise (`KOIDE_GENERATION_WEIGHT_DIAL_SHAPE...:196-203`). If the primitive were widened to grant a measure, the wall closes trivially and dishonestly. |

`scale_reference_primitive` and `kinetic_isotropy_primitive` are **not** in this
chain: `r` and `Q` are dimensionless and static. Confirmed against the registry —
neither is cited by any note in the chain.

---

## 2. Layer B — algebraic carrier

| # | Assumption | Where it enters | Class | What opens if it is wrong |
|---|---|---|---|---|
| B1 | The generation degree of freedom is the **hw=1 corner triple** `{e1,e2,e3}` of the taste cube `C^8=(C^2)^{⊗3}` | `docs/CL3_TASTE_GENERATION_THEOREM.md:58-70` | landed theorem, ledger `decoration` / `audited_decoration` / `retained_pending_chain` | The carrier is `decoration`-graded in the live ledger, i.e. it is *naming*, not load-bearing derivation. `RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md:38-47` says outright the carrier is **supplied**, not re-derived, and that the staggered-Dirac/chiral import selecting hw=1 is "carried elsewhere". If hw=1 is not the generation locus, nothing below survives. |
| B2 | Observables on the triple are all of `M_3(C)` (irreducible, no proper quotient) | chain-of-custody `docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:36` (L3) | landed theorems | If the observable algebra were smaller, the circulant commutant argument of §3 changes. |
| B3 | The three corner labels are the three **charged leptons of one charge sector** | *nowhere derived* — `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:11-12` ("Identifying `Q_H` with the physical charged-lepton Koide ratio is not supplied by this row") | **UNEXAMINED HABIT / open bridge** | This is the species bridge. It is open by the corpus's own statement, yet every "the observed value is 2/3" comparison uses it. If the three corners are not one charge sector, `Q` is not the Koide ratio and the counting bit is not a lepton question. |

---

## 3. Layer C — the acting group (`C_3` vs `S_3`) — **first load-bearing convention**

| # | Assumption | Where it enters | Class | What opens if it is wrong |
|---|---|---|---|---|
| C1 | "the **only** relabeling symmetry of the three hw=1 patterns is the order-3 cyclic shift `C`" | `docs/GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:36-38` and again `:102` | **FALSE AS WRITTEN** — contradicted by `CL3_TASTE_GENERATION_THEOREM.md:58-63` (the hw=1 sector carries the **`S_3`** permutation rep `A_1+E`) | Lattice (A1) supplies proper cubic rotations, whose action on the three axes is the full `S_3`, not `C_3`. The reduction `S_3 → C_3` is a **choice**, and this sentence hides it as a fact. |
| C2 | `S_3` is discarded because it forces spectrum multiplicities `{1,2}` — "two degenerate masses, **excluded for the charged leptons**" | `docs/KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md:42-46` | **EMPIRICAL SELECTOR wearing structural clothes** — **[gated]** `H = αI + β(J−I)` has eigenvalues `{α+2β (×1), α−β (×2)}` | The group is chosen by the observed non-degeneracy of the lepton spectrum. That is a fit input, disallowed by the exercise's own "what does not count" list, sitting *upstream* of the value question. If instead the group is fixed structurally (it is `S_3`), the mass operator is degenerate and the whole Koide construction is the wrong model of leptons. |
| C3 | The full cubic group `O_h` is rejected as over-constraining | `docs/KOIDE_OCTAHEDRAL_OVERCONSTRAINS_VALUE_BIT_NARROW_NOTE_2026-06-02.md:11-20` (ledger `no_go`/`unaudited`) | landed no-go, unaudited | Consistent with C2: the corpus *knows* larger groups kill the structure. This makes the `C_3` choice a Goldilocks selection: `C_3` is the unique subgroup between trivial and `S_3` that leaves exactly one free ratio. |
| C4 | **Group asymmetry**: the *mass operator* is required `C_3`-equivariant only, but the *weight rule* is required invariant under `C_3` **and** the antiunitary `K`/CPT | operator side `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:101-116`; weight side `KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_..._2026-07-11.md:88-110` (S2) | **UNEXAMINED HABIT — the strongest unstated premise in the chain** | **[gated]** The `S_3` transposition acts on the mass-operator coefficients as exactly `Θ = diag(1,1,−1)` (`b → conj(b)`) — i.e. the "`K`-reality"/CPT input imposed on the weight side **is literally the piece of `S_3` that was discarded on the operator side**. Nothing in the corpus states a principle for using different groups on the two sides. If the same group acts on both: `S_3` both sides ⇒ degenerate spectrum (excluded); `C_3` both sides ⇒ the doublet weights `p_1 ≠ p_2` are free and the weight rule has **two** free parameters, not one (`KOIDE_GENERATION_WEIGHT_DIAL_SHAPE...:150-151`, CHECK 05). **So the "single counting bit" framing is an artifact of the group mismatch, not a structural fact.** |

> **Ledger verdict on Layer C.** The one-bit shape of the blocker is manufactured
> by two conventions (C1/C2 pick `C_3`; C4 re-imports the discarded `S_3` element
> on the weight side only). This is the clearest place in the whole chain where a
> convention is doing the work of a derivation.

---

## 4. Layer D — the operator class

| # | Assumption | Where it enters | Class | What opens if it is wrong |
|---|---|---|---|---|
| D1 | Commutant of `⟨C⟩` = circulants ⇒ `H = aI + bC + conj(b)C²` | `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:101-116` | landed theorem (Schur, abelian) — sound | — |
| D2 | **Hermiticity** of `H` (hence `C²`-coefficient = conj of `C`-coefficient) | same, `:108-114` | convention/bridge | Non-Hermitian real circulants have a genuine complex-conjugate eigenvalue pair — the very structure that the `det_R` "fusion" route needed (`KOIDE_REAL_REP_BLOCK_COUNT_..._2026-05-30.md:68-77`). Hermiticity *removes* that pair, and the corpus uses that removal to kill a route. So Hermiticity is load-bearing on a no-go. |
| D3 | `a ∈ R` from the "`K`/CPT-real readout condition"; `arg b = δ` free | same, `:112-114` | **POSITED, not derived** — stated flatly in `docs/FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md:26-31` ("GAP A — K-reality is posited, not derived … it carries **no selective information** distinguishing r=1/2 from r=1") | Note the double role: `K`-reality is posited to pin `δ`, but is explicitly *not* a selector for `r`. Under C4 this is the discarded `S_3` element re-entering. If `S_3` were kept on the operator side, `δ=0` would be **free** — one posited input discharged — at the cost of degeneracy (C2). |
| D4 | `a ≠ 0` (equivalently `Tr H ≠ 0`) | `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:39` (L6) | domain restriction | `Q` is undefined at `Tr H = 0`; the "cone" of admissible `r` is punctured. Minor but must be named. |
| D5 | **Positive spectrum** (all `λ_k > 0` ⇒ `0 < r < 1`) | same, `:41` (L8) | convention + comparator | Without positivity `r` ranges over `(0,∞)` and `Q > 1` is allowed; the "two horns `1/2` and `1`" picture depends on the positivity window. The Brannen **signed-`√m`** freedom is explicitly identified with the same counting bit (`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_..._2026-06-05.md:74-75`). So positivity is not independent of the bit it is used to frame. |

---

## 5. Layer E — the weighting-form cone

| # | Assumption | Where it enters | Class | What opens if it is wrong |
|---|---|---|---|---|
| E1 | The admissible weighting forms are `diag(g_0, g_1, g_1)` — a 2-parameter cone with `g_0:g_1` free | `docs/KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md:55-57`; equivalently `docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md:25-61` (`B = α Tr(AB) + β tr(A)tr(B)`, PD iff `α>0, α+3β>0`) | landed no-go, ledger **`no_go` / `unaudited` / `unaudited`** | **STALE STATUS.** `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_..._2026-06-05.md:72,140,151,188` and `FLAVOR_EINSELECTION_..._2026-06-02.md:72` all call this row **`retained_no_go`**. The live ledger says `unaudited`. The single wall the whole reduction rests on has never been audited. (Independently flagged by the sibling campaign; I confirm it from `docs/audit/data/audit_ledger.json`.) |
| E2 | **Which group cuts the cone.** The runner hard-codes `R = diag(1, Rot(2π/3))` with the comment "`C_3` acts as singlet fixed, doublet rotated 2pi/3" | `scripts/frontier_koide_real_rep_block_count_permitted_not_forced_2026_05_30.py:57-59` | **MIS-NAMED GROUP** | **[gated]** On the mass-operator coefficient space the **generation shift acts trivially**: `Ad_C(H) = H` for every circulant, so shift-`C_3` invariance leaves the **full 6-parameter** symmetric-form space, not a 2-parameter cone. The 2π/3 rotation is realized by the **clock/dual `Z_3`**, conjugation by `D = diag(1,ω,ω²)` (`b → ω^{-1} b`) — a *different group*, not supplied anywhere as a framework symmetry. The `S_3` transposition alone leaves **4** parameters. The cone is correct only for the dual group. |
| E3 | The cone lives on the **mass-operator coefficient space** `(a, Re b, Im b)` | `KOIDE_REAL_REP_BLOCK_COUNT_..._2026-05-30.md:55` | convention | But `KOIDE_OCTAHEDRAL_..._2026-06-02.md:16-18` puts the *same* 2-parameter cone on the **generation carrier `R^3`**, where the shift genuinely acts by rotation. Two different spaces (one is an algebra, the other a module) carrying the same `C_3`-rep are used interchangeably. Only the algebra supports the pin of §7. **Naming which space the cone lives on is a prerequisite to any selector search.** |
| E4 | The **HS point** is `diag(3,6,6)` | `docs/FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:17` (ledger `bounded_theorem` / **`audited_clean`** / **`retained_bounded`**) | landed, retained-grade — the *only* retained-grade node in the whole cone layer | **[gated]** `diag(3,6,6)` is basis-dependent: the *same* HS form reads `diag(3,3,3)` in the frame `{I, B1/√2, B2/√2}` and `diag(1,1,1)` in the HS-orthonormal frame. So `g_0/g_1` is a property of the **(form, basis)** pair, not of the form. The basis-free content is `ρ := 2 g_0/g_1` = the blockwise Radon–Nikodym derivative of the weighting form against HS. `ρ = 1` for HS **in every frame**. |
| E5 | The **flat point** `diag(1,1,1)` is the other horn | *not landed* — introduced by the current campaign, `.claude/science/physics-loops/koide-mode-content-campaign-20260724/CAMPAIGN.md:120-124` | **NEW FRAMING, not corpus content** | **[gated]** Every landed `r = 1` result in the corpus is the HS form read *per dimension*, not the flat cone point: `FLAVOR_DOUBLET_METRIC..._2026-06-02.md:35-39`; `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:159-165`; `KOIDE_GENERATION_WEIGHT_DIAL_SHAPE..._2026-07-11.md:179-181`; `KOIDE_R_HALF_POLARIZATION_SELECTOR..._2026-06-08.md:53-55` ("Hessian `diag(12,12)`, rank 2 → two real modes → `(1,2) → r=1`" — that *is* the HS form read per dimension). **No landed result varies the cone point at all.** The two-horns-on-a-cone picture mislocates the `r=1` horn and therefore sweeps a family the corpus never uses. |

---

## 6. Layer F — the "equal-sector locus" and the `r` readout

| # | Assumption | Where it enters | Class | What opens if it is wrong |
|---|---|---|---|---|
| F1 | `r` is read off the **equal-sector locus** of the cone: `g_0 a² = g_1 |b|²` ⇒ `r = g_0/g_1` | campaign framing, `CAMPAIGN.md:120-122`; landed equivalent `FLAVOR_DOUBLET_METRIC..._2026-06-02.md:35-39` | **CONVENTION, and it is the counting bit itself** | **[gated]** With the `dim^s` balance `g_0 a² · 2^s = g_1 |b|²` one gets exactly `r = 2^s · (g_0/g_1) = 2^{s−1} ρ`. Writing "`r = g_0/g_1`" **silently fixes `s = 0`** (per-block). Writing the dial "`r(s)=2^{s−1}`" (`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:80-94`) **silently fixes `ρ = 1`** (HS). The corpus uses both parameterizations of the *same* one-dimensional freedom, and no note states the joint formula. Consequence: **a selector that fixes only the form, or only the counting exponent, fixes nothing.** |
| F2 | Sector "powers" are `p_s = a²`, `p_d = 2|b|²`, with `r = p_d/(2 p_s)` | `docs/C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md:36-37` | **`meta` note, "naming ratification"; ledger `meta`** | The explicit `2` in `r = p_d/(2p_s)` is the `s`-exponent in disguise, ratified as a *dictionary*. `:44-48` of the same note says it "does not supply a weighting, normalization … or any value of `r`". A dictionary that contains the disputed factor 2 is not weight-neutral. |
| F3 | "Equal-sector locus" as a name | campaign only | **would be new repo vocabulary** | Not in `docs/repo/CONTROLLED_VOCABULARY.md`. I propose **no** new name; the landed native phrases are *equal-channel-energy* (`KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED...:2-3 statement 1`) and *2-sector equipartition* (`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:42`, L9). |
| F4 | `Q = Tr(H²)/(Tr H)² = 1/3 + (2/3) r` | `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:39` (L6); `koide_circulant_q_two_thirds_algebraic...` ledger `audited_clean`/`retained` | landed theorem, sound | **[gated]** `Σλ = 3a`, `Σλ² = 3a² + 6|b|²`. This layer is not where the problem is. |

---

## 7. Layer G — **the finding: the cone is not free**

The exercise's stated wall is "`r` is a FREE parameter of the invariant-form
cone". That is true only if *every* PD `C_3`-invariant form is an admissible
weighting form. The corpus's own no-go tested exactly three conditions —
positive-definiteness, Ad-invariance, scalar/traceless orthogonality
(`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md:60-61`). It did
**not** test the one condition that a weighting form induced by a *readout* must
satisfy.

**Associativity / Frobenius condition.** A form generated by a linear readout
functional `φ` on the observable algebra, `⟨X,Y⟩ = φ(X†Y)`, is exactly a form
satisfying

```text
⟨u v, t⟩ = ⟨v, u† t⟩      for all u, v, t in the circulant algebra.
```

**[gated]** Imposing this on the general cone form `g_0 a² + g_1(b_re² + b_im²)`
over `V = Herm_circ(3)` with the actual matrix product gives the exact residual

```text
⟨uv,t⟩ − ⟨v,u†t⟩ = (2 g_0 − g_1) · ( a_t·(bu·bv) − a_v·(bu·bt) )
```

which vanishes identically **iff `g_1 = 2 g_0`**, i.e. iff the form is
proportional to the Hilbert–Schmidt/trace form. Solved symbolically:
`solve(...) = [{g_0: g_1/2}]`; residual `= 0` at `(3,6)`, `= −1` at `(1,1)` on an
explicit witness. Equivalently in the ambient framing: `⟨AB,C⟩ = ⟨B,A†C⟩` on
`M_3(C)` forces the Frobenius note's `β = 0` (also gated: `lhs=0, rhs=β`).
Equivalently again: in eigenvalue coordinates the clock-`Z_3` permutes
`(λ_0,λ_1,λ_2)` cyclically, so the associative invariant form is forced to the
**counting measure on the three eigenvalue slots**, `Σ_j λ_j λ'_j = Tr(HH')`.

**Consequences, stated conservatively.**

1. **The cone freedom collapses to a point.** `ρ = 1` is forced, not chosen. Every
   landed derivation already sits there (§5 E5), so this is a *repair*, not a
   contradiction — but it means the FS-constant-across-the-cone theorem foreclosed
   a family whose non-HS members are not admissible weighting forms in the first
   place, and it means `KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS`'s "future
   positive work must supply an independent authority that fixes the ratio to 1"
   (`:88-90`) has a candidate answer that was never tested.
2. **It does not close `r`.** With `ρ = 1` fixed, `r = 2^{s−1}` — exactly the
   landed dial. The residual is the **counting exponent `s`**, not a metric.
3. **It kills the campaign's Wave 2 as specified.** Wave 2 proposes to "derive
   `g_0/g_1` from the landed corner action's kinetic normalization" and to read
   `3:6 ⇒ r = 1/2`. Any kinetic normalization that is a readout-induced form
   **must** give `3:6`; that is now algebra, not dynamics. Reading `r = 1/2` off it
   requires per-block balance (`s = 0`), which is the open bit. **Wave 2 as
   specified would produce a convention-laundering false positive.** (I also
   checked the kill-check Wave 2 asks for: "action kinetic normalization" is *not*
   among the 8 tested lenses in `KOIDE_R_HALF_POLARIZATION_SELECTOR..._2026-06-08.md:44-48`
   — the 8 are `J_cs`, geometric quantization/Kähler polarization, MDL record,
   equivariant holomorphic index, KMS/modular, Grassmann/Pfaffian, CPT/antiunitary,
   canonical-quantization uniqueness.)

**Residual premise of the lead (named honestly).** The associativity condition is
the statement "the weighting form is generated by a *linear readout functional on
the observable algebra*". Record (A3) gives additivity over **disjoint records**,
not linearity over **algebra elements**. Wiring one to the other is a bridge and
must be derived or declared. That bridge — not the cone — is where this lead's
weight sits.

---

## 8. Layer H — the mass-ratio bridge (does it smuggle a normalization?)

| # | Assumption | Where it enters | Class | What opens if it is wrong |
|---|---|---|---|---|
| H1 | `m_k = λ_k²` (operator eigenvalues are **√mass**, Brannen parametrization) | `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:94` — "The physical statement `m_k = λ_k²` **additionally requires the unresolved P1/species/carrier bridge**"; `KOIDE_CIRCULANT_Q_TWO_THIRDS..._2026-05-10.md:164-166, 207-210` | **OPEN BRIDGE, explicitly** | This is a normalization smuggle only if used silently — the corpus is clean here and says so twice. But note the consequence: with `m_k = λ_k` instead, `Q_Koide = Σm/(Σ√m)²` is a *different* function of `(a,b)` and the entire `r`-analysis is void. The bridge is doing real work. |
| H2 | The **sign** of `√m` on the doublet | `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT..._2026-06-05.md:74-75` — "only the **count** (the `Q` readout / the sign of `sqrt(m)` on the doublet) differs" | **the counting bit again, in a third dress** | The signed-`√m` choice, the Dirac-vs-Majorana choice, the K-reality partition and the fermionic frame are asserted to be "one counting bit on different tensor factors" (`:83-85`). That four-way equivalence is asserted, not proved, and the sibling campaign has already found the 6-vs-12-generator horn is **`r`-neutral** in its landed realization (`CAMPAIGN.md:151-160`). **At least one leg of the asserted equivalence is broken; the others are unverified.** |
| H3 | `Q_H` is the **physical charged-lepton Koide ratio** | `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:11-12` (explicitly not supplied) | OPEN BRIDGE | Same as B3. |
| H4 | Absolute scale `S` of the lepton masses | `:94` (out of scope), `scale_reference_primitive` gives units only | OPEN | Not part of the `r` question; named for completeness so no one closes `r` and calls the sector closed. |

---

## 9. Convention-vs-derivation map (the deliverable of this exercise)

Places where **a convention is doing the work of a derivation**, ranked by how
much of the value question they carry:

1. **C4 — the group asymmetry** (`C_3` on the operator, `C_3 + K/CPT` on the
   weight). Makes the blocker one-dimensional. Without it there is either no
   hierarchy (`S_3`) or a two-parameter weight freedom (`C_3` both sides).
   *Unstated anywhere.*
2. **F1/F2 — the balance exponent `s`**, hidden inside "`r = g_0/g_1`" and inside
   the ratified dictionary factor `r = p_d/(2 p_s)`. This is the actual residual.
   *Named as a dial in one note, as a cone coordinate in another, never jointly.*
3. **E2 — the mis-named cutting group.** The cone is cut by the clock/dual `Z_3`,
   not by the supplied generation `C_3`. A selector search aimed at "`C_3`
   invariants" is aimed at a group that imposes nothing here.
4. **C2 — the empirical exclusion of `S_3`** by observed lepton non-degeneracy.
5. **E5 — the flat point as a horn.** Not corpus content; mislocates `r=1`.
6. **D5 — spectrum positivity**, entangled with the signed-`√m` half of the bit.
7. **E1 stale status** — the sole wall is cited four times as `retained_no_go`
   and is `unaudited` in `docs/audit/data/audit_ledger.json`.

Places where the corpus is **clean** and should not be re-attacked: `Q = 1/3 +
(2/3)r` (F4), the circulant commutant (D1), the two-sector *partition* (B2/§4),
the explicit open-ness of H1/H3.

---

## 10. First artifacts (concrete, in priority order)

**Artifact 1 — `readout_induced_form_pins_the_c3_cone` (lemma + runner).**
*Object:* the C_3-invariant symmetric-form cone on `Herm_circ(3)`.
*Tool acting on it:* the associativity/Frobenius condition `⟨uv,t⟩ = ⟨v,u†t⟩`
(equivalently: the form is `φ(X†Y)` for a linear readout functional `φ`).
*Content:* the residual is `(2g_0 − g_1)·(a_t (b_u·b_v) − a_v (b_u·b_t))`, so the
unique associative ray is the trace form, `ρ = 1`. Exact sympy, ~12 gates,
including the mutation gate (residual non-zero at `(1,1)`) and the ambient
`M_3(C)` restatement (`β = 0`). **Not** on the foreclosed list: it is not a
reality-type/FS invariant, not the multiplicative/`AC_phi_lambda` bridge, not the
δ-pattern leg, not a chirality argument. Its honest output is a *narrowing*: it
converts "cone free" into "counting exponent free", and it names a candidate
answer to the open obligation at
`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md:88-90`.

**Artifact 2 — `koide_r_convention_factorization_probe` (decisive falsifier).**
*Object:* the pair (weighting form `G`, balance exponent `s`).
*Tool:* the exact identity `r = 2^s (g_0/g_1) = 2^{s−1} ρ`, plus the doublet-frame
mutation `B_i → μ B_i`.
*Content:* re-express **every** landed `r`-value in the corpus in `(ρ, s)`
coordinates (I have already done this for 7 of them — all have `ρ = 1`), then
apply the mutation to each proposed selector. **Falsifier rule:** a proposal whose
answer for `r` changes under `μ`-rescaling is fixing a frame normalization, not
deriving `r`; a proposal that returns only `ρ` or only `s` is `r`-silent. This is
the test I would run against Wave 2 *before* Wave 2 runs.

**Artifact 3 — `generation_group_symmetry_budget` (the C4 audit).**
*Object:* the pair (operator-side group `G_op`, weight-side group `G_w`).
*Tool:* exact enumeration of `(G_op, G_w)` over subgroups of `S_3 × ⟨K⟩` with, for
each, (i) the mass-spectrum multiplicity pattern and (ii) the dimension of the
invariant weight family. *Content:* show that the "one free ratio" outcome occurs
**only** at `G_op = C_3`, `G_w = C_3 + K`, and that this pair is not derived
anywhere. Expected deliverable: either a principle that forces the asymmetry
(which would be genuine progress), or a narrow honest statement that the
counting-bit's *one-dimensionality* is itself an unforced choice — which is a
publishable sharpening of the blocker, and is exactly the sort of negative the
exercise says is welcome.

**Artifact 4 (repair, low science content, high hygiene value).** The four
`retained_no_go` citations of `koide_frobenius_isotype_split_uniqueness`
(`CHARGED_LEPTON_VALUE_REDUCES..._2026-06-05.md:72,140,151,188`) and the one in
`FLAVOR_EINSELECTION..._2026-06-02.md:72` are stale against the live ledger. Per
repo policy this is a source-side correction, not an audit action.

---

## 11. Honest boundary — what this exercise did NOT establish

- It did **not** derive `r`. Artifact 1 removes the cone freedom; the counting
  exponent `s` survives untouched, and `s` is the landed residual.
- It did **not** show the corpus is wrong about `r` being unforced. Every note
  read says so explicitly and correctly at its own scope.
- The associativity pin is **conditional** on the readout-functional bridge (§7,
  residual premise). I did not derive that bridge from Record.
- I did not re-verify B1 (the carrier) or H1 (the mass bridge) — both are
  `decoration`/open in the live ledger and both are upstream of everything here.
- I did not test whether `s` is pinnable. My reading of the corpus is that after
  Artifact 1 the bit reduces to a single sharply-stated question — *is the balanced
  object the mass operator's own trace-form decomposition (⇒ `r = 1/2`), or a
  density operator on the 3-dimensional carrier (⇒ `r = 1`)?* — i.e. **form
  equipartition vs state equipartition**. `FLAVOR_DOUBLET_METRIC..._2026-06-02`
  (form, retained_bounded) and `KOIDE_GENERATION_WEIGHT_DIAL_SHAPE..._2026-07-11`
  (state, S3 density-operator input) are the two landed representatives of exactly
  that split. That is where I would point Exercise Two, not at the cone.
