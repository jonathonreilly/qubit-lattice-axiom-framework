# WAVE 2 — steelman and stress-test of EX1 (the associativity/Frobenius pin)

**Date:** 2026-07-24. **Base:** `origin/main` @ `62826882ac` (fetched at start).
**Scope:** this report file only. No repo science surface created or edited,
nothing committed/pushed, no PR. No audit verdict set or predicted. No axiom, no
approved-primitive claim, no new repo vocabulary proposed.

**Verification.** Everything load-bearing below was rebuilt natively and exactly
(sympy, symbolic/`Rational` only — no float inputs, nothing cited as arithmetic).
Scratch runner (not a repo file):
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/wave2_defend_ex1_probe.py`,
log `…/wave2_defend_ex1_probe.log`. **SCORECARD PASS=72 FAIL=0**, including six
construction-mutation probes (A5 at three mutated cone points, A9 wrong-product,
B2d, B3c) per campaign rule 3. This section is written from the runner output,
not from intent (campaign rule 4). Gate labels below (`A3`, `B8b`, …) are runner
lines.

---

## 0. Framework refresher — surfaces actually read before concluding

- `docs/MINIMAL_AXIOMS_2026-06-29.md` **in full** — Lattice / Qubit /
  Admissibility / Record (`:65-72`), the Qualification (`:76-80`), the
  anti-laundering clause on `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE`
  (`:122-126`), and the "Open Gates Outside The Axioms" list (`:160-176`).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` — all six rules and
  the three approved primitives.
- `docs/audit/data/axiom_premise_nodes.json` — `canonical_ids` =
  `minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive` (complete supplied foundation).
- Source notes of the primitives I touch: `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`
  and `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (via the registry node
  text) — neither is in the `r` chain and neither is invoked as a premise here.
- Wall surfaces: `docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`,
  `docs/KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md` +
  its runner `scripts/frontier_koide_real_rep_block_count_permitted_not_forced_2026_05_30.py`,
  `docs/GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md`,
  `docs/KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_FORCED_VALUE_UNFIXED_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`,
  `docs/FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md`,
  `docs/KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`,
  `docs/FLAVOR_OPERATOR_SPECTRAL_FUNCTIONALS_DO_NOT_FORCE_R_HALF_NO_GO_NOTE_2026-06-02.md`,
  `docs/FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md`,
  `docs/RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md`,
  `docs/RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md`,
  `docs/C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`,
  `docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, `docs/ACTION_NORMALIZATION_NOTE.md`,
  `docs/KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`,
  `docs/FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md`,
  `docs/FLAVOR_FIND_J_CONSOLIDATION_KAPPA_IS_THE_INPUT_2026-06-02.md`,
  `docs/FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31.md`,
  `docs/FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md`.

No approved primitive is invoked as a premise anywhere below.

---

## 1. Verdict in one block

| Ex1 claim | Verdict |
|---|---|
| The residual is `(2g_0 − g_1)(a_t(b_u·b_v) − a_v(b_u·b_t))`, vanishing iff `2g_0 = g_1` | **CONFIRMED exactly** (`A3`, `A4b`). Ex1's algebra is right, including the sign structure. I found no arithmetic error anywhere in Ex1 §7. I can also **strengthen** it: no group is needed (§2.4, `B3a/B3b`). |
| The associativity/Frobenius condition is *required* because "any form induced by a linear readout functional must satisfy it" | **REFUTED as a framework consequence.** It is an **import** — a physical-observable/readout-identification bridge that `MINIMAL_AXIOMS_2026-06-29.md:170` lists as *outside* axiom content, and that the corpus's own parent note declares as a Boundary premise with a landed independence no-go. **Ex1 is demoted from theorem to conditional.** (§3) |
| Granting the bridge, `g_0/g_1 = 1/2` is FORCED, so with the mode-count fixed the ratio closes | **The pin is real but selects NEITHER horn.** Both landed horns sit on the trace ray. Worse for Koide: applied to the corpus's own landed invariant weight-rule dial, Ex1's admissibility test holds **exactly at `r = 1`** and **rejects the `r = 1/2` rule** (`B8b`, `B8c`). (§3.4) |
| The cone is cut by the clock/dual `Z_3`, not the generation `C_3`, which acts trivially on the coefficient space | **CONFIRMED** (`C1b`, `C1c`, `C2a`, `C2b`). Real correction to the landed framing. But it does **not** damage Ex1's own pin, which needs no group (§4). |
| `diag(1,1,1)` is a new framing, not corpus content; all seven landed `r = 1` results are the same HS form read per-dimension with `ρ = 1` | **PARTIALLY REFUTED.** `diag(1,1,1)` *is* corpus content — it is how the HS form reads in the corpus's own working frames (`D1b`, `D1c`). And at least three landed `r = 1` routes are not quadratic-form readings at all, so a pin on the form cannot touch them (§5). |
| `r = 2^s (g_0/g_1)` | **CONFIRMED** (`E1a`) and identical to Ex2's `r = (g_0/g_1)(w_1/w_0)` with `w_1/w_0 = 2^s`. The two sectors are stating **one** identity (§6, §7). |

**The one-sentence finding.** The Frobenius condition is a correct and slightly
under-stated piece of algebra about *forms*, imported rather than derived; it
pins the metric factor to the trace ray — and **both horns live on the trace
ray**, so it cannot close `r`; and when translated onto the corpus's own landed
weight-rule dial its admissibility test is *exactly* the condition `r = 1`.

---

## 2. (a) The residual, re-derived from scratch

### 2.1 What the objects are, stated precisely

The exercise brief asks exactly this, and it matters, so it is fixed once.

- **The space the form lives on.** `V = Herm_circ(3)`, the real 3-dimensional
  space of Hermitian circulant matrices
  `H = a·I + b·C + conj(b)·C²`, `a ∈ R`, `b = x + iy ∈ C`, with `C` the cyclic
  shift, `C³ = I`. Coordinates `(a, x, y) = (a, Re b, Im b)` — the group-algebra
  frame `{I, B_1 = C+C², B_2 = i(C−C²)}`. This is the surface the landed cone is
  stated on (`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md:53-57`,
  `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:16-19`).
- **The algebra `uv` refers to.** The ordinary **matrix product** of the two
  circulants — equivalently the `Z_3` group-algebra **convolution** of the
  coefficient vectors, *not* componentwise multiplication of `(a, x, y)`.
  Gate `A1b/A1c`: `Herm_circ(3)` is closed under this product and commutative;
  gate `A9` is the construction-mutation probe showing the componentwise product
  gives a *different* residual, so the gate is sensitive to using the true
  convolution. (Ex1 records making and catching exactly this error; I reproduce
  the correct product independently.)
- **What `u†` means.** Conjugate transpose. On `Herm_circ(3)` it is the
  **identity** (`A1d`), so on this space the condition
  `⟨uv, t⟩ = ⟨v, u†t⟩` reads `⟨uv, t⟩ = ⟨v, ut⟩` — the ordinary associativity
  (Frobenius) condition for a symmetric bilinear form on a commutative algebra.
  The dagger is not idle in general: gate `A8` verifies the sesquilinear version
  on *general* (non-Hermitian) circulants, where `u† ≠ u` and order reversal is
  what makes the trace form associative.
- **The form.** `⟨u, v⟩ = g_0 a_u a_v + g_1 (x_u x_v + y_u y_v)`, the polarization
  of the cone quadratic `g_0 a² + g_1|b|²`. Write `b_u·b_v := x_u x_v + y_u y_v`.

### 2.2 The product law (gate `A2`)

From the explicit symbolic `3×3` matrix product:

```text
(uv)_a = a_u a_v + 2 (b_u · b_v)
(uv)_b = a_u b_v + a_v b_u + conj(b_u b_v)
```

The `2(b_u·b_v)` term in the **identity** component is the whole story: it is the
`C·C²` and `C²·C` contribution. Dropping it (the natural slip) makes the residual
come out `−g_1(…)`, which would be non-vanishing on the entire positive-definite
cone and would have refuted Ex1 outright. It does not; the term is there.

### 2.3 The residual (gates `A3`, `A4`, `A5`)

```text
⟨uv, t⟩ − ⟨v, u†t⟩
  = 2 g_0 [ a_t (b_u·b_v) − a_v (b_u·b_t) ]
  +   g_1 [ a_v (b_u·b_t) − a_t (b_u·b_v) ]
  = (2 g_0 − g_1) · ( a_t (b_u·b_v) − a_v (b_u·b_t) ).
```

Exactly Ex1's expression (`A3`, sympy `simplify(residual − claimed) == 0`).

- The second factor is **not** identically zero: witness `u = v = B_1`-direction,
  `t = I` gives it the value `1` (`A4a`).
- Hence the residual vanishes identically **iff `g_0 = g_1/2`**; the symbolic
  solve returns `[{g_0: g_1/2}]` (`A4b`), reproducing Ex1's `solve` result.
- Point + mutation probes (`A5`): residual `= 0` at `(3,6)` and at `(1,2)` (the
  whole HS ray); residual `= 1` at the flat point `(1,1)`; `= −1` at the mutated
  point `(1,3)`; `= 1` at `(2,3)`. So the gate is not a tautology and the pin is
  not "any `g_1 > g_0`".
- Ambient restatement (`A7`): on `M_3(C)` with
  `B(A,B) = α Tr(A†B) + β tr(A)tr(B)` — the exact form of the landed no-go's cone
  (`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md:25-40`) — the
  `α`-part is identically associative and the `β`-part is not, with explicit
  witness residual `1`. So `β = 0` is forced. Ex1's ambient claim is confirmed.

### 2.4 A strengthening Ex1 missed (and it matters for §4)

Ex1 reaches `g_0/g_1 = 1/2` by intersecting associativity with the
`diag(g_0, g_1, g_1)` **cone**, whose cutting group Ex1 elsewhere argues is not a
supplied framework symmetry (its own §5 E2). That tension is removable. In
eigenvalue coordinates `λ_j = a + 2Re(b ω^j)` the map `H ↦ (λ_0,λ_1,λ_2)` is an
`R`-algebra isomorphism `Herm_circ(3) ≅ R³` with **pointwise** product (`B1b`),
and:

- the Frobenius family is **exactly** `⟨u,v⟩ = Σ_j c_j λ_j λ'_j` — a 3-parameter
  family inside the 6-parameter symmetric-form space, i.e. **a measure with three
  atoms on the eigenvalue slots** (`B2a`, `B2b`, `B2c`; mutation `B2d`);
- imposing **only** scalar/traceless orthogonality — `⟨I, X⟩ = 0` for traceless
  `X`, one of the three conditions the landed no-go already grants
  (`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md:6-9`: *"Positive-
  definiteness, Ad-invariance, and scalar/traceless isotype orthogonality do not
  force the Frobenius normalization `beta = 0`"*) —
  forces `c_0 = c_1 = c_2` and hence `G = c·diag(3,6,6)`, the HS ray
  (`B3a`, `B3b`; mutation `B3c` shows dropping orthogonality leaves the ratio
  unpinned, e.g. `c = (1,1,2)` is Frobenius with a nonzero singlet–doublet cross
  term).

**So: Frobenius + scalar/traceless orthogonality ⇒ HS, with no group at all.**
That is a cleaner and strictly stronger version of Ex1 §7, and it immunises the
pin against the E2 group-misnaming correction. Credit where due — but it also
makes the *next* section's translation exact, and that translation is what
kills the closure claim.

---

## 3. (b) THE DECISIVE QUESTION — is associativity required?

### 3.1 The claim decomposes into three separable steps

Ex1 justifies the condition with "any form induced by a linear readout functional
must satisfy it". That is true (and its converse holds: setting `φ(X) := ⟨1, X⟩`
recovers `⟨u,v⟩ = φ(u†v)`). But the justification silently bundles three
independent steps:

- **(B-i)** there is a **linear functional `φ` on the observable algebra** of the
  corner carrier;
- **(B-ii)** the weighting form is `⟨X,Y⟩ = φ(X†Y)` — i.e. the sector "energy" is
  the readout applied to the **algebra product of two mass operators**;
- **(B-iii)** the resulting form is **isotype-orthogonal** (equivalently
  clock-invariant), which is what actually pins `φ ∝ Tr`.

Only (B-i)+(B-ii) is "induced by a linear readout functional". (B-iii) is a
separate condition and, as §3.4 shows, it is the one carrying the whole result.

### 3.2 What the Record axiom actually gives — it is not (B-i)+(B-ii)

The Record axiom, quoted exactly
(`docs/MINIMAL_AXIOMS_2026-06-29.md:65-72`):

> Records form. When present, a record locks exactly one admissible local
> possibility. A site never carries more than one record; records are permanent.
> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

This is a **finitely additive set function on disjoint collections of records**.
Turning it into (B-i)+(B-ii) requires two things the axiom does not contain.

1. **An identification of algebra elements with record content.**
   `MINIMAL_AXIOMS_2026-06-29.md:170` lists *"source/action and physical-
   observable identification"* among the **Open Gates Outside The Axioms**, and
   `:76-80` says *"Further physical structure requires a retained derivation or
   bridge, or explicit approved-primitive registration, before use as a premise."*
   `PRIMITIVE_REGISTRY_CHECK.md` rule 5 withholds *"any … weighting rule,
   normalization rule, probability rule, readout bridge"*.
2. **Extension from disjoint additivity to algebra-linearity.** Records lock one
   possibility; there is no linear combination of records, no `−1·record`, and
   nothing that evaluates a *product* of two mass operators.

The corpus has already adjudicated exactly this move, twice, against Ex1's
reading:

- `MINIMAL_AXIOMS_2026-06-29.md:122-126`: *"`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`
  is not this axiom note and is not an approved axiom-premise node… That older
  parent must not be moved wholesale into `docs/audit/data/axiom_premise_nodes.json`."*
  That parent is precisely the note that packages "additive scalar observables"
  into a readout functional. There is a standing anti-laundering clause covering
  this exact step.
- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md:45-57` declares the readout
  identification as an explicit **Boundary premise (T1-d)**, saying in its own
  words that *"the axiom memo explicitly excludes source/action and physical-
  observable identification from Record content, so this identification is a
  premise of this note, declared and consumed as such — not a consequence of
  `minimal_axioms`"* (`:50-53`), backed by a landed independence no-go
  (`:22-26`) and an explicit countermodel: `log det + ε·Tr` *"obey[s]
  Record-style additivity"* while failing the intended functional form (`:53-57`).
- The landed **classifier** is the sharpest statement of what Record does give
  (`:63-69`): *"on positive diagonal blocks, additivity gives
  `W_n(x_1,…,x_n)=sum_i phi(x_i)`"* — a sum of one-site terms with `φ` an
  arbitrary continuous function; and the determinant-only readout is the case
  `φ(x) = c log x`. Record's readout, as landed, is a **weighted counting measure
  with free atom weights**, and its best-supported functional form is
  **logarithmic** — the opposite of linear-on-the-algebra.

Two further landed statements say the same thing directly on the Koide surface:

- `KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md:83-85`:
  *"The Record axiom itself supplies no weighting, normalization, or occupancy
  rule …, so it cannot force the holomorphic polarization either."*
- `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:172-176`: *"Finite additivity of
  the Record readout allows the singlet and doublet powers to be summed …, while
  the per-block (`s=0`) and per-mode (`s=1`) normalizations remain separate
  weighting conventions."*
- `FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md:96-106`, from the
  Record-side algebra note `RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05`:
  *"finite additivity leaves the normalized two-sector coordinate arbitrary: for
  any supplied `p in (0,1)`, choosing `d = p u/(1-p)` gives `d/(u+d)=p`. Thus
  Record permits both the generator-channel endpoint `r=1/2` (`rho=1`) and the
  dimension/per-mode endpoint `r=1` (`rho=2`), along with a continuum of other
  supplied readout ratios."* Reproduced natively at `F1a/F1b`.

**Answer to (b), part one: the associativity requirement is an IMPORT, not a
framework consequence.** Ex1's own §7 "residual premise" paragraph says as much;
this section upgrades that admission from a caveat to the load-bearing finding,
with the corpus's own adjudications quoted. Ex1 Artifact 1 is a **conditional
lemma**, not a theorem — and its condition is a named open gate, not a small one.

### 3.3 Granting the bridge in full: the family it leaves is the landed dial

Suppose we grant (B-i)+(B-ii) outright. The Frobenius family on `Herm_circ(3)` is
then exactly `⟨X,Y⟩ = Tr(ρ X†Y)` with `ρ` a positive circulant (§2.4, `B2c`).
Imposing the supplied `K`/CPT reality `Θ = diag(1,1,−1)` gives `c_1 = c_2`
(`B4a`), i.e.

```text
rho = diag(p_s, p_d/2, p_d/2)      (character basis).
```

That is *verbatim* the invariant family of the landed bounded theorem
`KOIDE_GENERATION_WEIGHT_DIAL_SHAPE_FORCED_VALUE_UNFIXED_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md:129-135`,
whose T1 proves the singlet-versus-doublet split is **not** forced by any
supplied automorphism (`:161-169`) and whose T2 exhibits both horns inside the
family (`:178-181`): `ρ = I/3` (dimension rule) → `r = 1`; `ρ = diag(1/2,1/4,1/4)`
(cell rule) → `r = 1/2`. Reproduced natively at `B6b/B6c/B6d`.

**So (B-i)+(B-ii) — the entire "linear readout functional" content — leaves `r`
free over `(0, ∞)`.** The closure comes only from (B-iii).

### 3.4 (B-iii) translated onto the landed dial: it selects `r = 1`

This is the decisive computation of this report.

On the landed dial `ρ = diag(p_s, p_d/2, p_d/2)`, the induced Frobenius form has
singlet–doublet cross term (`B8a`)

```text
G_01 = 2 ( p_s − p_d/2 ),
```

so Ex1's isotype-orthogonality condition holds **iff `p_d = 2 p_s`**, i.e. **iff
the dial coordinate `r = p_d/(2 p_s)` equals `1`** (`B8b`). And the landed
`r = 1/2` weight rule `ρ = diag(1/2, 1/4, 1/4)` is Frobenius but has
`G_01 = 1/2 ≠ 0`, so it is **rejected** by the orthogonality half of Ex1's own
test (`B8c`).

Read plainly: **Ex1's admissibility criterion, applied to the corpus's own landed
invariant weight-rule family, is exactly the condition `r = 1` — against Koide.**

*Honest caveat on the translation, stated because a reviewer will raise it.* The
landed `ρ` is a weight rule on **cells** (`w(P) = Tr(ρP)`), while Ex1's object is a
**metric** on the operator space. The translation is nonetheless forced by Ex1's
own equivalence, not by me: Ex1 asserts that the admissible weighting forms are
exactly those induced by a linear readout functional, and on `Herm_circ(3)` those
are exactly `{Tr(ρ X†Y)}` (`B2c`), so `ρ` **is** Ex1's admissible-form parameter
and the landed T1 classification is directly on point. Ex1's orthogonality
condition is then literally the condition `ρ ∝ I`. What the criterion does *not*
do is tell you how to read `r` off the object it admits: the metric route gives
`1/2`, the cell-weight route gives `1`, and the corpus's landed reading of `ρ ∝ I`
is the dimension rule, `r = 1`
(`KOIDE_GENERATION_WEIGHT_DIAL_SHAPE…_2026-07-11.md:178-179`). So the fully
careful statement is: **the criterion admits exactly one object, and that object
is read as `r = 1` by the corpus and as `r = 1/2` by Ex1 — the criterion does not
adjudicate between the readings, which is the counting bit itself.**

The reason is now visible and is the real content of the wall. The bridge selects
`φ ∝ Tr`. But `φ ∝ Tr` is the source of **both** horns, depending on what it is
applied to (`B5`):

| the same `φ = Tr`, applied to | reading | `r` |
|---|---|---|
| the quadratic content of `Y` per **cell**, balanced `E_s = E_d` (`3a² = 6\|b\|²`) | metric, per-cell | **1/2** |
| the quadratic content per **real mode**, balanced `E_s/1 = E_d/2` | metric, per-mode | **1** |
| the cell **projectors**, `w(P_s):w(P_d) = Tr P_s : Tr P_d = 1:2` | measure on cells | **1** |

`B5d` gates that the two metric readings differ by exactly the conjugation-orbit
size `2`. The corpus states the third row itself:
`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md:23-25` —
*"DIMENSION / Plancherel / trace `(1,2)` (weight by irrep dimension; this is what
the Hilbert-Schmidt trace gives, `Tr(P_singlet)=1`, `Tr(P_doublet)=2`) gives
`r=1`"* — and
`FLAVOR_OPERATOR_SPECTRAL_FUNCTIONALS_DO_NOT_FORCE_R_HALF_NO_GO_NOTE_2026-06-02.md:45-49,72`
— *"The canonical Hilbert-Schmidt metric on `span{I,C,C^2}` weights the three
modes equally. That is the dimension-mode read and points to `r=1`, not `r=1/2`…
That fold is the block-count choice, not an output of the choice-free spectral
functionals."*

### 3.5 The presentation test: "Frobenius" is not a predicate on `r`

Independent confirmation that the pin cannot be a statement about `r`. The two
horns admit two equivalent presentations:

- **P1 (landed):** one form `G = HS = diag(3,6,6)`, two counting rules
  `w = (1, 2^s)`.
- **P2 (campaign/Ex1):** one counting rule `w = (1,1)`, two cone points
  `G_eff(s) = diag(3, 6·2^{−s}, 6·2^{−s})`.

They give the same `r` for every `s` (that is the §6 identity). But the Frobenius
factor of the P2 presentation is `2·3 − 6·2^{−s} = 6(1 − 2^{−s})` (`B7b`), which
vanishes only at `s = 0`. At `s = 1` the *same physical `r = 1` horn* is Frobenius
in P1 (the form is HS) and non-Frobenius in P2 (the form is `diag(3,3,3)`, the
flat ray — `B7a`). **The associativity verdict is a function of the presentation,
not of the physical datum.** That is Ex2's redundancy, made concrete on Ex1's own
test.

### 3.6 Answer to (b), stated plainly

1. The framework readout does **not** induce a form on this algebra at all
   without a declared physical-observable bridge that `MINIMAL_AXIOMS:170`
   places outside axiom content and that the corpus's own parent note carries as
   a Boundary premise with a landed independence no-go. **The associativity
   requirement is an import.**
2. Even granted in full, the "linear readout functional" content (B-i)+(B-ii)
   leaves `r` free — it reproduces the landed 2026-07-11 dial.
3. The closure comes from (B-iii), isotype orthogonality, which is not a readout
   property; and on the landed dial (B-iii) is **exactly `r = 1`**.
4. `φ ∝ Tr` is common to both horns, so selecting it selects neither.

**Ex1 is demoted from theorem to conditional, and the conditional does not point
where Ex1 hoped.** This is a sharp negative and I am reporting it as the finding.

---

## 4. (c) Which group cuts the cone — Ex1 CONFIRMED, with a qualification

**Confirmed, exactly.**

- `Ad_C(H) = H` for every circulant, so the matrix of the generation shift on the
  coefficient space `(a, Re b, Im b)` is the `3×3` **identity** (`C1a`, `C1b`),
  and the invariance residual `R^T G R − G` vanishes for **every** symmetric `G`:
  generation-`C_3` invariance leaves the full **6-parameter** space, not a
  2-parameter cone (`C1c`).
- The `2π/3` rotation is realised by the **clock/dual `Z_3`**, conjugation by
  `D = diag(1, ω, ω²)`, whose matrix on `(a, Re b, Im b)` is exactly
  `diag(1, Rot(2π/3))` (`C2a`) — i.e. exactly the matrix the landed runner
  hard-codes at
  `scripts/frontier_koide_real_rep_block_count_permitted_not_forced_2026_05_30.py:57-59`
  under the comment *"`C_3` acts as singlet fixed, doublet rotated 2pi/3"*, and
  exactly the group the note names as `C_3` at
  `KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md:53-57`.
  It does cut the 2-parameter cone (`C2b`).
- The **supplied** cubic-rotation content lands differently: the `S_3`
  transposition acts on the coefficient space as `Θ = diag(1,1,−1)` (`C3a`) and
  leaves a **4-parameter** family (`C3b`), not the 2-parameter cone.

**Ex1's E2 is a correct and material correction to the landed framing.** Two
qualifications that Ex1 does not state and that a reviewer will:

1. **The cone shape is not wrong, the space is.** On the **carrier** `R³`, where
   the generation `C_3` genuinely acts by cyclic permutation, the invariant
   symmetric forms *are* a 2-parameter cone (`C4`). The landed lane uses the same
   cone symbol on the carrier (`KOIDE_OCTAHEDRAL…`) and on the operator
   coefficient space (`KOIDE_REAL_REP_BLOCK_COUNT…:53-57`); only the second is
   mis-attributed.
2. **The clock `Z_3` is not physically arbitrary.** It cyclically permutes the
   three **eigenvalue slots** (`C2c`) — i.e. it is the relabelling of the three
   mass eigenvalues (the three charged leptons), while the generation `C_3`
   permutes the corner/taste basis. So the corpus is tracking a real structure
   under a wrong name, not inventing one. What is true is the narrow claim: the
   framework-**supplied** symmetry (Lattice proper cubic rotations, `→ S_3 → Θ`)
   does not cut this cone.
3. **It does not damage Ex1's own pin**, because §2.4 shows the pin needs no group
   — Frobenius + scalar/traceless orthogonality suffices. Ex1 could have made its
   §7 immune to its own §5 E2; it did not.

---

## 5. (d) `diag(1,1,1)` and the "seven landed `r = 1` derivations"

Ex1's E5/Artifact-2 claim has two parts. They fare differently.

### 5.1 "`diag(1,1,1)` is NOT corpus content" — REFUTED as stated

`diag(1,1,1)` is precisely how the HS form reads in the frames the corpus works
in (`D1b`, `D1c`):

| frame | HS reads |
|---|---|
| `{I, B_1, B_2}` (group-algebra, unnormalised) | `diag(3,6,6)` (`D1a`) |
| `{I/√3, B_1/√6, B_2/√6}` (HS-orthonormal real) | `diag(1,1,1)` |
| `{I/√3, C/√3, C²/√3}` (HS-orthonormal group-algebra) | `diag(1,1,1)` |

The third frame is the one `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:126-129`
explicitly uses (*"read off the group-algebra coordinates of `Y` in the
Hilbert–Schmidt-orthonormal basis `{I/√3, C/√3, C^2/√3}`"*), and
`FLAVOR_OPERATOR_SPECTRAL_FUNCTIONALS…:45-46` states the `diag(1,1,1)` reading in
words (*"weights the three modes equally"*). So `diag(1,1,1)` is corpus content.

The **narrower** true claim — that the *flat point of the cone over
`(a, Re b, Im b)`* is not used by any landed note as a distinct form — survives,
but it is undercut by `B7a`: the landed `r = 1` horn, re-presented with a single
per-cell balance, **is** `3·diag(1,1,1)` on those coordinates. So the campaign's
"HS point vs flat point" framing is a legitimate re-presentation of the landed
horn, not a mislocation. Ex1's charge that the campaign "sweeps a family the
corpus never uses" does not stand; the family is the corpus's own dial in
different clothes.

### 5.2 "All seven are the same HS form read per-dimension with `ρ = 1`" — PARTIALLY REFUTED

I enumerated the landed `r = 1` statements rather than accepting a count of seven.
There are more than seven, and they are not all form-readings.

**Group A — genuinely the trace/HS content read per real dimension (Ex1 is right
about these):**

| # | file:line | mechanism |
|---|---|---|
| 1 | `docs/FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:35-36` | `diag(3,6,6)`, per-real-direction: `3a²=6(Re b)²=6(Im b)²` |
| 2 | `docs/GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:162-165` | `s=1` endpoint, weights `(1,2)` = real dimensions |
| 3 | `docs/KOIDE_R_HALF_POLARIZATION_SELECTOR…_2026-06-08.md:52-55` | `E_d = Tr(M†M)\|_doublet = 6\|b\|²`, Hessian `diag(12,12)`, rank 2 |
| 4 | `docs/FLAVOR_OPERATOR_SPECTRAL_FUNCTIONALS…_2026-06-02.md:45-46, 72` | canonical HS metric on `span{I,C,C²}` weights three modes equally |
| 5 | `docs/FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31.md:31` | equal power per real dimension, `3a² = 3\|b\|²` |
| 6 | `docs/FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md:77` | per-mode basis equipartition `a²=b²` |
| 7 | `docs/FLAVOR_FIND_J_CONSOLIDATION_KAPPA_IS_THE_INPUT_2026-06-02.md:35-37, 49` | Gaussian equipartition with `‖H‖² = 3a²+6\|b\|²` ⇒ `⟨a²⟩=⟨\|b\|²⟩` |
| 8 | `docs/FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md:15-16, 28` | dimensional/Born weighting `1:2` |
| 9 | `docs/KOIDE_GENERATION_WEIGHT_DIAL_SHAPE…_2026-07-11.md:178-179` | `ρ = I/3` (tracial **state**, not a metric) |
| 10 | `docs/FLAVOR_MAX_RECORD_ENTROPY…_2026-06-15.md:73-75` | max von Neumann entropy → `ρ = I/3`, block weights `(1/3,2/3)` |
| 11 | `docs/FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md:37-41` | Born measure `1:2` |

Rows 9–11 are **states**, not metrics; calling them "the HS form" requires
identifying the tracial state with the HS form, which is fair but is a
re-description, not an instance.

**Group B — landed `r = 1` results that are NOT quadratic-form readings, so a pin
on the form cannot touch them (Ex1 is wrong about these):**

| # | file:line | mechanism |
|---|---|---|
| 12 | `docs/KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md:51-54` | built determinant `det D = \|det M\|²`; index a signed mode-count in `{±1,±3}` |
| 13 | `docs/FLAVOR_NATIVE_ACTION_PREDICTS_Q1_2026-06-02.md:35-42` | five spectral-action cutoffs `S(b)=Σ f(λ²)` peak near `r=1` |
| 14 | `docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:132`; `docs/FLAVOR_RECORD_DYNAMICS_SHARPENS_ARROW_STABILIZER_FAILS_2026-06-02.md:16` | heat-kernel / records-arrow flow; thermalization |

**Group C — landed values outside `{1/2, 1}` entirely, which the two-horn framing
does not contain (gates `D3`, `F2`, `F2b`):**

- `r = 17/2 − 6√2 ≈ 0.0147` — eigenvalue/idempotent partition,
  `docs/FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md:76`
  (re-derived exactly from `(1+2t)² = 2(1−t)²`);
- `r = 3/2` — `α_s = 3, α_d = 1` weighting,
  `docs/FLAVOR_MAX_RECORD_ENTROPY…_2026-06-15.md:60`;
- `r = 2` — Ex2's flat-metric × dimension-weights cell, `E3`.

**Net for (d):** Ex1's `ρ = 1` census is right for the *majority* of landed
`r = 1` statements and wrong as a universal. Its stronger rhetorical use — "the
corpus never varies the cone point, so the pin is a free repair" — does not
survive Groups B and C.

### 5.3 A vocabulary collision Ex1 should not ship

Ex1 introduces `ρ := 2 g_0/g_1`. The corpus already uses `ρ` on this exact
surface with a different meaning:
`FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md:87, 92-94, 105` defines
`rho = doublet/singlet = 2r`, so corpus-`ρ = 1 ⇔ r = 1/2` and
corpus-`ρ = 2 ⇔ r = 1`, whereas Ex1-`ρ = 1 ⇔ the form is HS`. They disagree
off `r = 1/2` (`F1c`, `F1d`). Per the repo's no-new-vocabulary discipline this
symbol must not be reused; the landed native phrases are *equal-channel-energy*
and *2-sector equipartition*.

---

## 6. (e) The identity `r = 2^s (g_0/g_1)`, stated exactly

### 6.1 Definitions

- **Cells.** The canonical `C_3` generation readout context supplies exactly two
  cells (`C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md:19-28`):
  the **singlet cell** (unit direction `I`) and the **doublet cell** (the HS
  orthocomplement, `B = J − I`), with `‖I‖² = 3`, `‖B‖² = 6`, `⟨I,B⟩ = 0`.
  Real dimensions `(dim_R singlet, dim_R doublet) = (1, 2)`.
- **Weighting form.** `G` on `(a, Re b, Im b)`, cell-diagonal, with singlet weight
  `g_0` and doublet weight `g_1`; cell contents
  `E_0 = g_0 a²`, `E_1 = g_1 |b|²`.
- **Cell multiplicity vector.** `w = (w_0, w_1)`, `w_i > 0`. Define
  **`s := log_2(w_1/w_0)`**.
- **Balance.** `E_0/w_0 = E_1/w_1`.

### 6.2 The identity (gate `E1a`)

```text
g_0 a^2 · 2^s = g_1 |b|^2      ==>      r := |b|^2/a^2 = 2^s · (g_0/g_1).
```

At the trace/HS ray `g_0/g_1 = 1/2` this is `r(s) = 2^{s−1}` — *exactly* the
landed dial (`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:81`), with
`s = 0 ⇒ r = 1/2` and `s = 1 ⇒ r = 1` (`E1b`, `E1c`; note `:86-90`).
And `Q = 1/3 + (2/3) r`, `Q(1/2) = 2/3`, `Q(1) = 1` (`D2a`, `D2b`).

### 6.3 The two equipartition conventions, exactly

- **(EQ-CELL), `s = 0`, `w = (1,1)`.** Each `K`/CPT-orbit cell of the readout
  context is counted **once** — the block-count / `det_C` measure. `r = g_0/g_1`;
  at HS, `r = 1/2`.
- **(EQ-MODE), `s = 1`, `w = (1,2) = (dim_R singlet, dim_R doublet)`.** Each real
  carrier dimension is counted once — the Born / dimension / `det_R` /
  Plancherel measure, and the classical equipartition-per-quadratic-DOF reading
  (`FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31.md:76`).
  `r = 2 g_0/g_1`; at HS, `r = 1`.

### 6.4 Redundancy — only the product is physical

`(g_0/g_1, 2^s) → (t·g_0/g_1, t^{−1}·2^s)` leaves `r` invariant for every `t > 0`
(`E2`). This is Ex2's `Γ` in Ex1's coordinates: **Ex1's `r = 2^s (g_0/g_1)` and
Ex2's `r = (g_0/g_1)(w_1/w_0)` are the same identity**, with `w_1/w_0 = 2^s`. The
four metric × count cells give `r ∈ {1/2, 1, 1, 2}` (`E3`).

### 6.5 What would fix `s`

`s` is fixed exactly when the framework supplies a **cardinality** for each cell —
a finite set of atoms per cell whose count is `w_i` — as opposed to a form. Three
inequivalent candidates, all currently open, and one already known dead:

1. **Berezin/CAR generator count per cell** (6 vs 12 generators). Known
   `r`-neutral **as landed**: Wave 1 found it doubles singlet and doublet
   *together* (`CAMPAIGN.md:145-153`), so it does not move `s`.
2. **`w_i = I(cell)`, the physical record readout of each cell.** Blocked at the
   axiom: Record's finite additivity leaves the normalized two-sector coordinate
   arbitrary (`F1b`;
   `FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md:96-106`).
3. **First-order vs second-order matter action** — `det D` (count-once) vs
   `det D†D` (count-twice). This is the landed open sub-question
   (`KOIDE_R_HALF_POLARIZATION_SELECTOR…_2026-06-08.md:96-99`) and currently
   *leans `r = 1`* on the one built realization
   (`KOIDE_KAHLER_DIRAC_REALIZATION…_2026-06-08.md:51-54`).

**What cannot fix `s`:** any condition on the form alone, including Ex1's. `B7`
shows the Frobenius predicate is not even well-defined on `(r, s)` independently
of presentation. And `s` need not be an integer: the corpus itself lands
`r = 3/2` and `r = 17/2 − 6√2`, so "bit" presupposes the `w_i` are cardinalities
of finite sets — an undischarged premise (Ex2 §3 makes the same point; I confirm
it from landed content rather than from a `Z_N` sweep).

---

## 7. Adjudication of the stated EX1 / EX2 tension

**There is no real contradiction to adjudicate.** The brief frames it as
"Ex1 forces `r = 1/2`" vs "Ex1 fixes a gauge". Ex1's own report already concedes
the second: `ex1_assumptions_ledger.md:172-173` (*"It does not close `r`… The
residual is the counting exponent `s`, not a metric"*) and `:282-283` (*"It did
not derive `r`… the counting exponent `s` survives untouched"*). Ex1's identity
`r = 2^s(g_0/g_1)` **is** Ex2's `r = (g_0/g_1)(w_1/w_0)` (`E1a`, `E2`). Both
sectors locate the residual in the same factor.

What this wave adds, beyond confirming that:

1. Ex1's justification for the associativity condition **fails** as a framework
   consequence (§3.2), so Artifact 1 is a conditional lemma resting on a named
   open gate, not a theorem.
2. Ex1's condition, granted, does not merely fail to select `1/2` — on the
   corpus's own landed invariant weight-rule dial it is **exactly `r = 1`**
   (`B8b`, `B8c`). Ex1's route, completed honestly, tilts **against** Koide.
3. Ex2's "a selector must be a measure with atoms, not an invariant" is
   **strengthened, not contradicted**, by Ex1: `B2c` shows the Frobenius family
   *is* the set of measures with three atoms on the eigenvalue slots. Ex1's
   condition converts the metric freedom into the atom-weight freedom; it does
   not remove a freedom.
4. Ex2's `Γ`-freeness argument gains a concrete instance: `B7` exhibits a single
   physical horn whose Frobenius verdict flips between two equivalent
   presentations.
5. **Credit where due.** The direct answer to the exercise question — *does the
   Frobenius condition genuinely force `g_0/g_1 = 1/2`?* — is **yes, on the
   cone, and yes even without the cone once scalar/traceless orthogonality is
   granted** (`A4b`, `B3a`, `B3b`). That is a real, exact, previously untested
   condition, and it is a candidate discharge of the standing obligation at
   `KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md:89-90` (*"Future
   positive work must supply an independent authority that fixes the
   scalar/traceless isotype-weight ratio to `1`"*) — **as a conditional**, whose
   condition is the readout bridge of §3.2. What is refuted is only the step from
   there to `r`.

**Consequence for the campaign's Wave 2 as specified** ("derive `g_0/g_1` from the
corner action's kinetic normalization; is it `3:6` or `1:1`?"): I agree with Ex1
§7.3 that it would launder a convention, and I can sharpen the reason. Any
readout-induced kinetic normalization is Frobenius, hence on the trace ray, hence
`3:6` — algebra, not dynamics (`B3a/B3b`). Reading `r = 1/2` off `3:6`
additionally requires `s = 0`, which is the whole bit. **Wave 2 as specified would
produce a false positive.** The live target is `s`, i.e. §6.5 candidate 3.

---

## 8. Honest boundary — what this report did NOT establish

- I did **not** derive `r`, and I did not refute `r = 1/2` as a physical value.
  §3.4 shows Ex1's *criterion* selects `r = 1`; that is a statement about that
  criterion, not about the leptons.
- I did **not** show the associativity condition is *false* — only that it is
  imported rather than derived, and that granting it does not close `r`.
- I did **not** re-verify the upstream carrier (hw=1 corner triple), the species
  bridge, or the `m_k = λ_k²` mass bridge. All three are open/`decoration` in the
  corpus's own words (`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:11-12, 94`)
  and all sit upstream of everything here.
- I did **not** audit any status label and set no verdict. Two status frictions I
  observed and am reporting only as observations, both already flagged by Ex1 §5
  E1 and Ex2 §7 F-3: the source notes describe `koide_frobenius_isotype_split_uniqueness`
  as a retained no-go while the live ledger row is `unaudited`; and
  `KOIDE_REAL_REP_BLOCK_COUNT…_2026-05-30.md:27-30` calls it and
  `ACTION_NORMALIZATION_NOTE` "two retained no-go rows". Adjudicating those is the
  audit lane's, not mine.
- The `Herm_circ(3)` analysis is on the generation sector **as presented** (the
  `C_3` circulant carrier). A construction that changes the carrier — an
  off-circulant or genuinely first-order fermionic realization — is outside its
  scope, exactly as `KOIDE_R_HALF_POLARIZATION_SELECTOR…_2026-06-08.md:87-99`
  anticipates. That is where §6.5 candidate 3 lives.

---

## 9. Verification appendix

Scratch runner (not landed, exact sympy throughout, no float inputs):
`…/scratchpad/wave2_defend_ex1_probe.py`, log `…/wave2_defend_ex1_probe.log`.
**SCORECARD PASS=72 FAIL=0.**

- **Block A (19 gates)** — `Herm_circ(3)` closure/commutativity/dagger; the
  product law from the explicit `3×3` matrix product; the residual identity; the
  non-vanishing of the second factor; `solve → {g_0: g_1/2}`; five point/mutation
  probes on the cone; the ambient `M_3(C)` `β = 0` restatement with explicit
  witness; the sesquilinear check on general circulants; and the wrong-product
  mutation.
- **Block B (23 gates)** — eigenvalue coordinates and the pointwise algebra
  isomorphism; the Frobenius family as a 3-atom measure (with the 6-vs-3
  dimension mutation); Frobenius + scalar/traceless orthogonality ⇒ HS (with the
  drop-orthogonality mutation); Frobenius + `Θ` ⇒ the landed 2-parameter dial;
  the one-functional-two-readings table; the landed density-state horns; the
  `B8` translation of Ex1's test onto the landed dial; and the `B7`
  presentation-dependence test.
- **Block C (9 gates)** — `Ad_C` is the identity on the coefficient space and
  cuts nothing; `Ad_D` is the runner's `diag(1, Rot 2π/3)` and cuts the cone;
  the clock permutes eigenvalue slots; `Θ` leaves 4 parameters; the carrier `R³`
  cone.
- **Block D (7 gates)** — HS in three frames; the flat point is a different,
  non-Frobenius form; `Q = 1/3 + (2/3)r`; the landed third value `17/2 − 6√2`.
- **Block E (5 gates)** — the `r = 2^s(g_0/g_1)` identity, the landed
  `r(s) = 2^{s−1}` specialization, both endpoints, the redundancy, the four cells.
- **Block F (6 gates)** — the Record two-sector arbitrariness identity; the `ρ`
  symbol collision; the landed values outside `{1/2, 1}`.

Mutation probes (campaign rule 3): `A5`(×3 mutated cone points), `A9`
(componentwise instead of convolution product), `B2d` (6-dim symmetric space vs
3-dim Frobenius family; flat point symmetric but non-Frobenius), `B3c`
(orthogonality dropped ⇒ ratio unpinned), `B8c` (the `r = 1/2` rule fails the
test). No constancy claim above rests on an assertion probe alone.
