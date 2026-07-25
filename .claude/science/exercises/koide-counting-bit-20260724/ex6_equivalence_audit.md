# EX6 — Audit of the landed four-way "counting bit" equivalence

**Date:** 2026-07-24
**Sector:** SIX (audit the equivalence itself)
**Baseline:** `origin/main` @ `1652deb63b` (fetched at session start)
**Status of this file:** exercise working note. No audit verdict, no promotion,
no axiom or primitive proposed, no repo surface edited outside this file.

---

## 0. Framework refresher — surfaces actually read (from `origin/main`)

Read in full before any conclusion below:

- `docs/MINIMAL_AXIOMS_2026-06-29.md` — Lattice / Qubit / Admissibility / Record,
  the Qualification clause (`:77-79`), and the "Open Gates Outside The Axioms"
  list, which names the staggered-Dirac/finite-Grassmann realization and
  `AC_phi_lambda` (`:161`) and every formation/weight/normalization rule (`:164-167`)
  as outside axiom content.
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` — the four registered
  premise nodes and clause 5 ("do not grant more than the primitive source note
  declares": no weighting rule, normalization rule, or probability rule).
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` — units conversion only, zero
  dimensionless content.
- `docs/audit/data/axiom_premise_nodes.json` — `minimal_axioms`,
  `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive`; nothing else chain-satisfies.
- `docs/ai_methodology/skills/review-loop/SKILL.md` — the two supplied premise
  types, the Record guardrails, "no admission class exists".
- `docs/repo/CONTROLLED_VOCABULARY.md` policy noted; **I propose no new repo
  vocabulary.** Every name used below is either already in the repo or is
  explicitly marked as exercise-local shorthand.

**Exercise stance as instructed:** axioms and approved primitives are treated as
ASSUMPTIONS here, and landed repo content is treated as auditable. I do find
landed content misframed; that finding is stated with `file:line`.

**Artifact for everything below:**
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/ex6_horn_audit.py`
(exact sympy, built from scratch, imports no repo module, uses no literature
value as input). Output:
`.../scratchpad/ex6_horn_audit_output.txt` — **TOTAL: PASS=72 FAIL=0**.
Block labels `A…K` below refer to that runner.

---

## 1. The algebra, built natively (not by analogy)

### 1.1 The cone is derived, not assumed (Block A)

Carrier: the three generation patterns with the order-3 shift `C`, `C^3 = I`,
`C^T = C^2`. The `C_3`-equivariant Hermitian operator is the circulant
`Y = a I + b C + conj(b) C^2` (`A3`, `A4`), amplitudes `(a, b_R, b_I) ∈ R^3`.

The residual symmetry acting on the amplitude space is conjugation by
`D = diag(1, w, w^2)`, which sends `C -> w C` (`A5`, computed) and therefore acts
on `(a, b_R, b_I)` as `1 ⊕ Rot(120°)` (`A6`). Solving `R^T G R = G` over all
symmetric `G` gives a **unique** solution family (`A7`), and it is exactly

```
G = diag(g_00, g_22, g_22)      2 free parameters, block diagonal, no singlet–doublet mixing
```

(`A9`, printed by the runner). So the cone is `diag(g_0, g_1, g_1)` — derived, and
the projective coordinate `rho := g_0/g_1` is the only invariant.

### 1.2 The two distinguished points (Block B)

`||Y||_HS^2 = Tr(Y† Y) = 3a^2 + 6 b_R^2 + 6 b_I^2` (`B1`, exact), i.e. the
HS/coherent-state metric on `(a, Re b, Im b)` is `diag(3,6,6)` (`B2`) —
matching `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:16-19`.
So `rho_HS = 1/2` (`B3`) and `rho_flat = 1` (`B4`).

**Where the `1/2` comes from** (`B5`): `||I||^2 = ||C||^2 = ||C^2||^2 = 3`, and the
doublet amplitude `b` occupies **two** of the three group-algebra slots (`C` and
`C^2`). Hence `g_1/g_0 = 2 = dim_R` of the doublet isotype of `R[C_3]`.
**The HS metric already carries the doublet multiplicity 2 inside it.** Hold this;
it is load-bearing in §5.

### 1.3 The master identity (Block C)

Let `(m_s, m_d)` be the slot/multiplicity weights the occupancy law assigns to the
singlet and doublet sectors, and impose the equipartition law "equal form-energy
per slot", `g_0 a^2 / m_s = g_1 |b|^2 / m_d`. Solving (`C1`, sympy `solve`, not
asserted):

> **`r_K := |b|^2/a^2 = (g_0/g_1) · (m_d/m_s)`**, and independently
> **`Q = Tr(H^2)/(Tr H)^2 = 1/3 + (2/3) r_K`** exactly (`C2`).

Every horn below is evaluated against this one identity.

Degeneracy table (`C3`, `C4`, printed):

| cone point `rho` | slot ratio `m_d/m_s` | `r_K` | `Q` |
|---|---|---|---|
| 1/2 (HS) | 1 | **1/2** | **2/3** |
| 1/2 (HS) | 2 | 1 | 1 |
| 1 (flat) | 1 | 1 | 1 |
| 1 (flat) | 2 | 2 | 5/3 |
| 1/4 | 2 | **1/2** | **2/3** |

`(HS, count-twice)` and `(flat, count-once)` give the *same* physics. So the
exercise-statement identification "`r = g_0/g_1`, HS point ↔ 1/2, flat point ↔ 1"
is the **`m_d/m_s = 1` slice** of a two-factor problem, not the whole problem.
Only the product is observable.

### 1.4 The homogeneity lemma — the whole audit in one line (Block D)

`r_K` is invariant under `m -> κ m` (`D1`) and under `g -> λ g` (`D2`) separately,
and is moved by exactly the factor `2` under `m_d -> 2 m_d` (`D3`).

> **HOMOGENEITY LEMMA.** `r_K` depends only on the *ratio* `(g_0 m_d)/(g_1 m_s)`.
> **Any horn realized as a common scalar on both sector weights is r-neutral.
> Only a horn that changes the singlet:doublet ratio can move `r`.**

This is the criterion. It is exact, it is one line, and it decides all four horns
without any Berezin computation.

---

## 2. Horn-by-horn verdict

### Horn 1 — count the K/CPT orbit once vs twice (Block E) → **CONTROLS `r`**

Built explicitly: the three character projectors `P_k` are idempotent (`E1`), resolve
the identity (`E2`); entrywise conjugation `K` fixes `P_0` (`E3`) and swaps
`P_1 <-> P_2` (`E4`). Orbit structure on the channel menu is `(1, 2)` (`E5`).

- one slot per K-orbit → `m_d/m_s = 1` → `r_K = 1/2`, `Q = 2/3`
- one slot per channel atom → `m_d/m_s = 2` → `r_K = 1`, `Q = 1`   (`E6`)

It does **not** move the cone point `rho` (`E7`). Source of the horn:
`KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md:194-195`
("one occupancy slot per K-orbit versus one slot per channel atom").

### Horn 3 — 2-cell vs 3-cell quotient menu (Block F) → **CONTROLS `r`, and is literally Horn 1**

`e_1 = P_1 + P_2` is real (`F1`) and `P_1` alone is not (`F2`); ranks 1 and 2 (`F3`).
So `R[C_3]` has exactly 2 minimal central idempotents and `C[C_3]` has 3 (`F4`).

- uniform on 2 cells, `w = 1/2` → `r_K = 1/2` (`F5`)
- uniform on 3 cells, `w = 1/3` → `r_K = 1` (`F6`)

matching `KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:54`
and `ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_..._2026-07-16.md:16-18`.

**The map is identical to Horn 1's** (`F7`), and not by analogy: the 2-cell menu
*is* the set of K-orbits of the 3 channel atoms, and the 3-cell menu *is* the set
of channel atoms. Horn 3 is Horn 1 restated on the same set with the same counting
measure — one statement, two vocabularies.

### Horn 2 — `det_C` vs `|det_C|^2` (Block G) → **r-NEUTRAL**

On the entrywise-real coupling triple: `det W = a^3+b^3+c^3-3abc = L0 L1 L2` (`G1`),
`L0` real and `L2 = conj(L1)` (`G2`), `det W = L0·|L1|^2` (`G3`). Realification
identity `det_R R(K) = |det_C K|^2` re-proved on a generic symbolic 2×2 (`G4`).

Sector degree vectors `(deg_s, deg_d)`, computed with `sympy.Poly`:

| object | degree vector | ratio `deg_d/deg_s` | `r_K` |
|---|---|---|---|
| `det_C` | (1, 2) | 2 | 1 |
| `\|det_C\|^2` | (2, 4) | 2 | 1 |

(`G5`, `G6`, `G7`). Under the landed *orbit* bookkeeping the same conclusion holds:
`(1,1) -> (2,2)`, ratio 1 on both sides (`G8`).
**Squaring is a uniform doubling of both sector degrees; by the homogeneity lemma
it cannot move `r`.**

**Additional correction found here (`G9`).** The identity `det_R R(K) = |det_C K|^2`
requires the carrier to be the realification of a complex space, i.e. of *even*
real dimension. The generation carrier is real-3-dimensional — **odd** — so it is
not `R(K)` for any complex `K`. Its isotypic decomposition is `R ⊕ C`: the singlet
is real type and has no complex structure to realify. The honest realified
determinant of the actual carrier is `L0·|L1|^2`, degree `(1,2)` — **not** `(2,2)`.
Calling `|det_C|^2` "the realified realization" of *this* carrier realifies the
singlet as well, which the carrier does not permit.

### Horn 4 — 6 vs 12 Grassmann generators (Block H) → **r-NEUTRAL, and is literally Horn 2**

Berezin built from scratch (Grassmann multiplication with explicit inversion-count
signs; no library). Convention calibrated, sign *computed* not chosen: the integral
equals `+det M` for generic symbolic `M` at `n = 1, 2, 3` (`H1.1-H1.3`).

- 6 generators (one triple copy, kernel `W`): integral `= det W = L0·|L1|^2` (`H2`)
- 12 generators (triple copy ⊕ K-conjugate partner copy): integral `= det W · det W̄
  = det3^2` on the real locus (`H3`)

Degrees `(1,2) -> (2,4)` (`H4`), ratio 2 on both sides → **r-neutral** (`H5`), and
the map is **identical to Horn 2's** (`H6`) — necessarily so, because the 6-generator
Berezin integral *is* `det_C` and the 12-generator integral *is* its square. The
landed orbit bookkeeping `L0|L1|^2 -> L0^2|L1|^4 = (L0|L1|^2)^2` is reproduced (`H7`).

### Control — Pfaffian (Block I)

`Pf([[0,K],[-K^T,0]])^2 = det` of that block matrix (`I1`, Pfaffian implemented by
perfect matchings), so `Pf = ± det K`: a uniform **halving** of the degree vector.
By the same lemma the Pfaffian-vs-determinant fork is also **r-neutral** (`I3`).

### The pair that *does* flip `r` at determinant level (Block J)

| functional | degree vector | ratio | `r_K` |
|---|---|---|---|
| `L0 L1 L2` — determinant over channel atoms | (1, 2) | 2 | 1 |
| `L0 L1` — multiplicity-stripped / orbit-quotient functional | (1, 1) | 1 | **1/2** |

(`J1`, `J2`, `J3`). And `|det|^2` lands at ratio 2 — the **same side as `det`** (`J4`).

This is exactly the fork already landed at
`FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md:30-44`:
`log|det H| = log|λ_triv| + 2 log|λ_doublet|` (the `r=1` side) versus "the
multiplicity-stripped functional `log|λ_triv λ_doublet|`" — "That is a different
functional."

---

## 3. (a) Which horns actually control `r`?

| horn | landed name | acts on | verdict |
|---|---|---|---|
| 1 | K/CPT orbit once vs twice | `m_d/m_s : 1 → 2` | **CONTROLS `r`** (factor 2) |
| 3 | 2-cell vs 3-cell menu | `m_d/m_s : 1 → 2` | **CONTROLS `r`** — *identical map to horn 1* |
| 2 | `det_C` vs `\|det_C\|^2` | `(e_s,e_d) → (2e_s,2e_d)` | **r-NEUTRAL** |
| 4 | 6 vs 12 Grassmann generators | `(e_s,e_d) → (2e_s,2e_d)` | **r-NEUTRAL** — *identical map to horn 2* |

**The just-completed K1–K5 finding on horn 4 is CONFIRMED** (`K7`), and it is
confirmed as a corollary of the homogeneity lemma rather than as a coincidence of
the Berezin surface.

**It is also extended: horn 2 is neutral by exactly the same mechanism (`K8`),
and so is the Pfaffian/first-order-vs-second-order fork.**

---

## 4. (b) Is the landed four-way equivalence correct?

**PARTIALLY CORRECT, with the error concentrated in the summary/gate wording, not
in the careful theorem notes.**

### 4.1 It is a 2+2 split, not a 4-way equivalence

There are **two** statements, each written twice:

- **The multiplicity statement** (horns 1 ≡ 3): does the conjugate channel pair
  count as one cell or two? Moves `r` by exactly 2.
- **The power statement** (horns 2 ≡ 4, and Pf/det): a uniform rescaling of the
  degree vector. Moves `r` by exactly 0.

The two statements are **not** equivalent to each other. Calling them four horns of
one bit is a category error: it merges an inhomogeneity with a homogeneity.

### 4.2 The careful landed notes already say this — credit where due

I did **not** discover the neutrality. It is landed, twice, in the exact places the
work was done:

- `KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md:184`
  — the section is literally titled "**Power-ratio neutrality** and the underived
  graining binary (T4)"; and `:309` — "`|det3|^2` doubles both exponents and leaves
  their ratio unchanged, so it does not select a graining horn".
- `KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:177-183`
  — "**r-neutral doubling** … the singlet exponent and the doublet exponent double
  together, and every doublet-to-singlet power ratio is unchanged"; and `:111-115`
  — "**FLAG — declared reading, not an equivalence** … T3 makes no equivalence claim".
- `ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md:100-102`
  — "The construction is constant over every supplied registered-mass ratio `r`;
  `r` remains a free dial."
- `ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_..._2026-07-16.md:405-407` and `:420-424` —
  explicitly refuses to identify the 2-cell/3-cell menu arithmetic with the
  physical count-once/count-twice fork ("the missing binding theorem is not supplied").
- Earliest and sharpest of all, `FLAVOR_FIND_J_ROUND2_POWER_NOT_COUNT_2026-06-02.md:32-37`
  — the note's own title is "**Power Does Not Select the Count**": "This is an
  exponent statement, not a count of whether the generation doublet should be
  treated as two real modes or one complex mode."

**So the repo separated power from count on 2026-06-02 and then re-fused them in the
July gate wording.** That regression is the defect.

### 4.3 Where the strong (wrong) equivalence actually lives

1. **The obligation's closure criterion** —
   `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:21-24`:

   > "A closing theorem must derive the physical matter action and its measure, then
   > distinguish the count-once `det_C`/holomorphic realization from the count-twice
   > `|det_C|^2`/realified realization…"

   This is the **r-neutral** pair. A theorem that discharges this criterion exactly
   as written would establish **nothing** about `r`. Conversely, nothing needs to
   distinguish `det_C` from `|det_C|^2` in order to fix `r`. **The gate that governs
   the entire charged-lepton value lane is aimed at the wrong object.**

2. **The bundling** —
   `docs/ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:62-64`:
   "generator-channel / orbit / holomorphic count-once" **over** "dimension / sector /
   real count-twice". Of those six labels, `orbit` and `sector`/`dimension` are
   r-controlling; `generator-channel`, `holomorphic`, and determinant-power `real`
   are r-neutral. (The note's actual *theorem* — the axioms do not supply the binary
   — is a non-supply statement and survives untouched; only its target description is
   mis-drawn.) Same defect at `:139-140`, "Remaining Live Route 1": "derive whether
   the actual matter action implements **first-order/Pfaffian/count-once** or
   **second-order modulus/count-twice** statistics" — `Pf`, `det`, `|det|^2` are three
   uniform rescalings of one degree vector, so this research target cannot decide `r`.

3. **The label attached to the correct arithmetic** — three notes attach the name
   `det_C` to the (correct) equal-power-per-block reading:
   `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:67-68`,
   `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:159-165`,
   `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:35-40`.
   Their arithmetic is right; the name is wrong, because `det_C` over the channel
   atoms has ratio 2 (→ `r=1`). The object that gives `r=1/2` is the
   multiplicity-stripped functional of `FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT:38-42`.

---

## 5. (c) Blast radius — precisely

**GROUP A — machine-propagated gate defect (highest severity).**
The mis-aimed closure criterion is carried *verbatim* and is enforced as a source
gate by two runners, so the wrong sentence is being replicated by tooling:

- `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:21-24` (source)
- `docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md:399-402`
- `docs/ACPHILAMBDA_OCCUPANCY_GRAIN_SHARPENING_IMPORT_DECOMPOSITION_REFLECTION_ASYMMETRY_ORIENTATION_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-16.md:438-441`
- `docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md:382-385`
- `docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:470-473`
- `scripts/kcpt_coupling_triple_two_presentation_derivable_class_spectral_pairing_2026_07_16.py:562`
- `scripts/kcpt_coupling_triple_berezin_count_binary_measure_collapse_2026_07_17.py:615`

**Consequence, stated precisely:** the obligation `ac_orbit_occupancy_statistical_grain_derivation_obligation`
(registered in `docs/audit/data/derivation_obligations.json`, self-liquidation
condition "A retained kappa/counting-rule theorem deriving this exact grain removes
the obligation") is **satisfiable by a theorem that leaves `r` completely free**,
and is **not necessary** for a theorem that fixes `r`. The gate is neither necessary
nor sufficient for what it gates. Nothing landed becomes false; what breaks is the
*discharge condition*.

**GROUP B — label-only defects (no chain break).**
`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:67-68`,
`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:159-165`,
`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:35-40`,
`ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:62-64,:139-140`.
Their `r` arithmetic is exactly right (I re-derived all of it: `C1`, `E6`, `F5-F6`);
only the `det_C`/`det_R`/`Pfaffian` naming is mis-assigned. **No value, no theorem,
and no ledger row is falsified by this.** The chain of custody's own honest standing
(`:75-79`, "the charged-lepton value does not close until a separate `r=1/2` selector
is derived") is unaffected.

**GROUP C — theta lane, flagged concern (not proved here).**
`THETA_MASS_SIDE_COMPOSITION_CLOSE_ON_SHARED_OCCUPANCY_BRIDGE_BOUNDED_NOTE_2026-07-03.md:21`
consumes Leg 1 as "the charged-lepton matter action counts the `K`/CPT orbit once".
But what the theta side actually uses
(`STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md:26-27,:51`)
is that K/CPT orbit registration identifies `det M` with `conj(det M)` — an
identification **on the value set**, i.e. a modulus/phase-blindness statement, which
sits on the **r-neutral** side. The Koide side needs a **multiplicity on the sector
menu**, the r-controlling side. Same phrase, two different objects.
**Flagged, not proved:** I did not build the theta algebra in this sector. If it
holds, the "shared occupancy bridge" framing overstates the coupling, and
discharging the Koide-side horn would not supply the theta-side identification.
First check: whether `K`-orbit registration on the determinant *value* implies any
constraint on `m_d/m_s`. I expect not, by `D1`.

**GROUP D — unaffected, and the correct anchors for any repair.**
`FLAVOR_FIND_J_ROUND2_POWER_NOT_COUNT_2026-06-02.md:32-37`;
`FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md:30-44`;
`KCPT_..._SPECTRAL_PAIRING_..._2026-07-16.md:184,:309`;
`KCPT_..._BEREZIN_..._2026-07-17.md:111-115,:177-183,:526-528`;
`ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_..._2026-07-04.md:100-102`;
`ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_..._2026-07-16.md:405-407,:420-424`.
These already state the split correctly and should be cited by any repair.

**Not in the blast radius:** `koide_frobenius_isotype_split_uniqueness` (retained
no-go, "the Ad-invariant isotype-weight family has a free parameter") is *confirmed*
by this audit — it is the statement that `rho` is free, and my master identity shows
the slot ratio is a second, independent free factor. The 8-lens no-go
`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md:47`
("0 of 8 survived") is also confirmed and, in §6, explained.

---

## 6. (d) The FIFTH statement — the real controller of `r`

### 6.1 What it is

`r_K = (g_0/g_1) · (m_d/m_s)` is the **cross-ratio of two positive measures on the
two-element sector menu `S = {s, d}`**: `μ_form` (the point of the invariant-form
cone) and `μ_count` (the occupancy slot law). Neither is separately observable;
only their Radon–Nikodym derivative is.

> **FIFTH STATEMENT (exercise-local name only; I propose no repo vocabulary):**
> *Are `μ_form` and `μ_count` the same measure on the sector menu, or do they differ?*
> Equivalently: `dμ_count/dμ_form ∈ (R_{>0})^S` modulo overall scale.

**Concrete object:** the pair `(μ_form, μ_count)` on `S = {s, d}`, with
`μ_form ≡ (g_0, g_1)` from `diag(g_0, g_1, g_1)` and `μ_count ≡ (m_s, m_d)` from the
equipartition slot law.
**Invariant that acts on it:** the cross-ratio `R = (g_0 m_d)/(g_1 m_s)`. This is the
*only* function of the two that survives into `Q` (Block D).

### 6.2 Why it is not on the foreclosed list, and why it explains the failures

Every foreclosed lens — Frobenius–Schur / complex type / orientation /
CPT-antiunitary, the `AC_phi_lambda` multiplicative bridge, the δ-pattern leg,
chirality — is an **absolute invariant of a single object**. *No absolute invariant of
one object can produce the ratio of two independently supplied measures on it.*
That is a structural reason, not a hunch, and it retro-explains:

- why the FS indicator is constant `(+1, 0, 0)` across the whole cone (`K5`,
  recomputed here): FS is a property of the group representation, not of the form.
  FS `= 0` on the doublet channels is precisely the condition `dim_R End = 2 ≠ 1`
  (`K6`) — **FS creates the 1-vs-2 binary; it cannot resolve it**;
- why `0 of 8` selector lenses survived at
  `KOIDE_R_HALF_POLARIZATION_SELECTOR_..._2026-06-08.md:47`: all eight were
  absolute-invariant lenses.

The fifth statement is *relative*, so it is outside the class that has already failed.

### 6.3 The one-measure corollary — a candidate DECISIVE NO-GO

Suppose a single measure `μ` on `S` supplies both the invariant form
(`g_i ∝ μ_i`) and the slot law (`m_i ∝ μ_i`). Then (`K1`, symbolic)

> **`r_K = (μ_s/μ_d)·(μ_d/μ_s) = 1` identically — on the ENTIRE cone,
> for EVERY `μ`. Hence `Q = 1`.**

Both landed configurations are instances of this tie:
`(HS, count-twice)` realizes `μ = (1,2)` (`K2`); `(flat, count-once)` realizes
`μ = (1,1)` (`K3`). And `Q = 2/3` requires the two measures to differ **by exactly
`dim_R End_{C_3}(doublet) = dim_R(C) = 2`** (`K4`): the HS metric supplies `μ = (1,2)`
(it already counts the doublet twice — Block `B5`) while the occupancy law supplies
`μ' = (1,1)`.

Stated bluntly and honestly (the tie `g ∝ m` is an assumption, not a derivation):

> **Conditional statement.** If the framework's "energy" form and its occupancy count
> descend from one object, then `Q = 1` is FORCED and `Q = 2/3` is REFUTED, cone-wide.
> `Q = 2/3` requires the metric and the counting law to use *different* doublet
> multiplicities — the HS metric counting the doublet as 2 while the occupancy law
> counts it as 1.

This is the shape of a publishable negative, and it is decidable.

### 6.4 FIRST ARTIFACT (the specific thing to build first)

**Artifact 1 — the lemma (already built here, `PASS=72 FAIL=0`).**
`ex6_horn_audit.py` Blocks `A`–`D` + `K`: the derived cone, the master identity
`r_K = (g_0/g_1)(m_d/m_s)`, the homogeneity lemma, the one-measure corollary. This
lemma alone re-derives the "power-ratio neutrality" of
`KCPT_..._SPECTRAL_PAIRING_...:184,:309` and the "r-neutral doubling" of
`KCPT_..._BEREZIN_...:177-183` as two-line corollaries, and shows both are instances
of one fact rather than two computations.

**Artifact 2 — the decisive falsifier (next to build, ~1 runner).**
Named target: *does the framework chain supply ONE measure on `S` or TWO?*
Concrete test, entirely inside landed content:

1. Take the count-once presentation of the carrier seriously — the K-orbit quotient,
   i.e. `R[C_3] = R ⊕ C` with the doublet treated as **one** complex line rather than
   two real directions.
2. Compute the invariant form induced on the amplitude space **by that presentation**
   (not the `M_3(C)` HS trace, which is a count-twice object by `B5`).
3. Read off its cone point `rho`.

- If `rho = 1` (flat), then `r_K = rho · 1 = 1`: the count-once-consistent
  configuration gives `Q = 1` too, the one-measure corollary becomes unconditional on
  the landed surface, and **`Q = 2/3` is refuted as a consistent reading** — a decisive
  negative, and equally welcome per the exercise brief.
- If `rho ≠ 1`, the framework genuinely supplies two independent measures; `r` is then
  provably not derivable from either alone, and the open problem is sharply relocated
  from "pick a horn" to "derive the tie between the metric and the count".

Either branch is a result. Neither adopts a horn, fits a mass, imports a literature
value, or adds an axiom or primitive.

**Artifact 3 — the repair note (owner-gated, not proposed as a PR here).**
The obligation's closure criterion should target the r-controlling fork already
landed at `FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md:38-42` (multiplicity-
stripped `log|λ_triv λ_doublet|` vs `log|det H| = log|λ_triv| + 2 log|λ_doublet|`),
not the r-neutral `det_C`-vs-`|det_C|^2` pair. Because two runners hold the current
sentence as a verbatim SOURCE_GATE, this is a coordinated edit and belongs to the
audit/owner lane, not to this exercise.

---

## 7. Explicit non-claims

1. I do **not** claim the wall is solved. No horn is selected, `r` is not derived.
2. The one-measure corollary (`K1`) is **conditional** on the tie `g_i ∝ m_i`. That
   tie is an assumption stated as an assumption; Artifact 2 is precisely the test of it.
3. The theta-lane concern (§5 Group C) is **flagged, not proved** — I did not build
   the theta algebra.
4. I claim **no** priority for the r-neutrality of horns 2 and 4: both are already
   landed (`KCPT_..._SPECTRAL_PAIRING_...:309`, `KCPT_..._BEREZIN_...:177-183`), and
   the power/count separation is landed since `FLAVOR_FIND_J_ROUND2_POWER_NOT_COUNT_2026-06-02.md:32`.
   What is new here is the single homogeneity lemma that unifies them, the collision
   with the closure criterion, and the one-measure corollary.
5. No audit verdict is applied, no claim promoted, no axiom or primitive added, no
   repo vocabulary proposed, nothing committed or pushed, and no file outside this
   report was edited in the repository.
