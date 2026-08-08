---
claim_id: record_minimum_information_interlock_r_half_derivation_note_2026-06-04
claim_type_author_hint: bounded_theorem
---

# Record IRREVERSIBILITY + MINIMUM-INFORMATION Interlock → Brannen `r = 1/2` (Koide `Q = 2/3`): the Two Principles TOGETHER Force the Equal-Power Measure — FORCED-MODULO-TWO-POSITS

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the canonical
> source-of-truth doc.

**Date:** 2026-06-04
**Claim type:** bounded_theorem. This note reaches a clean, ruthlessly-honest **forcing** result with a
single, sharply-classified residual: the **two named physical principles** —
**IRREVERSIBILITY** ("records can't unform") and **MINIMUM-INFORMATION** ("a record stores the least
information consistent with being faithful") — **TOGETHER force** the Brannen modulus `r = 1/2`
(Koide `Q = 2/3`). The mechanism: irreversibility fixes the **recordable σ-algebra** to the **2 frozen
sector labels** (proven on the sister branch — used, not re-derived); minimum-information, applied to
that content, lands **unambiguously** on the **type/block-count** weight `(1,1) → r = 1/2`. The decisive
test computes **six** independent "minimum-information" readings (Shannon, MDL, Landauer, Jeffreys,
Kolmogorov, sufficient-statistic), **each restricted to the 2 sectors**; **all six converge on type**.
The **single** token/dimension reading (`(1,2) → r = 1`) is the **microstate pushforward** of the
maximally-mixed state `I/3`, and it is **excluded on two independent grounds**: (i) microstate content
is non-frozen → **non-recordable** (irreversibility), and (ii) the token distribution `(1/3, 2/3)` has
**strictly less** Shannon entropy on the 2-label space than uniform → it is **not minimum-information on
the recordable content**. **Verdict: FORCED-MODULO-TWO-POSITS.** Both principles are **posits** (the
Record axiom's scope excludes arrow/persistence and any store-the-least optimization), so the result is
a clean **closure-modulo-two-named-physical-principles**, not bare-axiom-native. This **materially
advances** the sister irreversibility result (which was RESTATEMENT): irreversibility alone left the
type/token bit open; **adding** minimum-information **closes** it.
**Status authority:** independent audit lane only. This note sets no audit status, promotes no row,
weakens no retained no-go, and edits no axiom. `r = 1/2` remains the Tier-A admitted input `AC_φλ`; it is
compared **structurally** only (no PDG value consumed).
**Primary runner:**
[`scripts/record_minimum_information_interlock_r_half_derivation.py`](../scripts/record_minimum_information_interlock_r_half_derivation.py)
(SUMMARY: PASS=50 FAIL=0).
**Cached log:**
[`logs/runner-cache/record_minimum_information_interlock_r_half_derivation.txt`](../logs/runner-cache/record_minimum_information_interlock_r_half_derivation.txt)

---

## §0 The exact gap, and what the two-principle interlock fills

The charged-lepton Brannen modulus `r = |b|²/a² = 1/2` (equivalently Koide `Q = 2/3` via the retained
biconditional [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md))
is the single Tier-A admitted input `AC_φλ` on the value chain
([`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)). Its
residual is sharply located: the **equal-power-per-block** (det_C / block-count) measure selects
`r = 1/2`; the **Born/dimension** (det_R) measure selects `r = 1`.

**A long arc localized the gate to a single discrete bit, then split that bit.**

- **Three adjacency-geometry attacks** (single face-diagonal; all diagonals / L2; all-to-all + Planck)
  all failed: geometry gives a **law-DEPENDENT** amplitude ratio, whereas the equal-power measure is
  **law-INVARIANT** — geometry is the wrong **kind** of object.
- The **record-binary attack** (sister branch
  [`RECORD_BINARY_EQUAL_POWER_MEASURE_R_HALF_TEST_NOTE_2026-06-04`](RECORD_BINARY_EQUAL_POWER_MEASURE_R_HALF_TEST_NOTE_2026-06-04.md))
  reached the right (measure) layer but was **RESTATEMENT**: bare record **additivity** is **linear**
  (so `Tr` satisfies it too), and the isotype measure is **quadratic** — additivity cannot select block
  over dimension.
- The **irreversibility attack** (sister branch
  [`RECORD_IRREVERSIBILITY_BLOCK_COUNTING_R_HALF_DERIVATION_NOTE_2026-06-04`](RECORD_IRREVERSIBILITY_BLOCK_COUNTING_R_HALF_DERIVATION_NOTE_2026-06-04.md))
  **PROVED the first half**: a frozen/irreversible record is necessarily a **superselection/block** fact
  (center of `M_n` is scalars → **no finer-than-block frozen fact**; an explicit falsification attempt
  **fails**). This fixes the recordable **σ-algebra** = the Wedderburn blocks. **But** it does **not**
  fix the **measure** on blocks. Two block-level measures remain, **both monotone**:

  | measure | construction (uses only the frozen center) | isotype weight `(w_singlet, w_doublet)` | `r` | `Q` |
  |---|---|---|---|---|
  | **TYPE-count** | each block once | `(1, 1)` | **1/2** | **2/3** |
  | **TOKEN-count** | tracial pushforward `Tr(E_k · I/3) = d_k/3` | `(1, 2)` (∝ `(1/3, 2/3)`) | **1** | **1** |

  The single remaining bit: **when a block forms a record, does it contribute 1 unit (type) or
  dimension-many units (token)?** Irreversibility leaves it **open** — the sister branch's exact
  RESTATEMENT verdict was that the residual is *indifference over superselection **LABELS** (block-count,
  → 1/2) vs over **MICROSTATES** (tracial pushforward, → 1)*, and that irreversibility supplies neither.

**The proposed interlock (the user's two principles).** This is exactly the bit a second principle can
fill:

1. **IRREVERSIBILITY** restricts faithful recordable content to the **frozen sector labels** —
   within-block microstates are reversibly connected (not frozen), so a record cannot faithfully store
   them. (Proven on the irreversibility branch; **used here**.)
2. **MINIMUM-INFORMATION**: a record stores the **least** information consistent with being a faithful
   record. Given (1), the faithful content is the sector label; the minimal register of "this sector is
   present" is **1 unit**, NOT dimension-many units. Storing dimension-many units **exceeds** the
   minimum.
3. Therefore each block contributes exactly **1 unit** → **TYPE-count** → `(1,1)` → equal-power →
   `r = 1/2` → `Q = 2/3`.

The interlock is the point: **irreversibility kills the microstate/von-Neumann reading** (not frozen →
not recordable), and **minimum-information kills the tracial/dimension weighting** (more than minimal).
**Neither principle alone forces `r = 1/2`** (the irreversibility branch showed irreversibility alone
leaves the type/token bit open; minimum-information applied to microstates would give token). The claim
is that the **PAIR** forces it — and the decisive test below confirms it.

## §1 Part A — the interlock setup (irreversibility restricts recordable content to sectors)

The sister irreversibility branch is **used, not re-derived**. The runner confirms (Part A) the two
facts this note **builds on**:

- The two sectors are exactly the **real-Wedderburn blocks** of `ℝ[Z₃] = ℝ ⊕ ℂ`: the singlet projector
  `E₀` (rank 1) and the doublet projector `E₁` (rank 2), orthogonal idempotents with dimensions `(1,2)`
  (runner A1a/A1b).
- **No finer-than-block frozen fact exists.** The center of a simple matrix block is trivial:
  `center(M₂(ℂ)) = ℂ·I` and the center within a full `M₃(ℂ)` is scalars (runner A2a/A2b). The explicit
  **falsification** is reproduced: a within-doublet **ray** projector (a real direction inside
  `range(E₁)`) is **not central** (`‖[P_ray, C]‖ = 1.2247 > 0`, runner A3a), and the doublet's own
  internal unitary `U = exp(iθ·i(C − C²))` **moves** it (`‖U P_ray U† − P_ray‖ = 1.3244 > 0`, runner
  A3b), while the **block** projectors `E₀, E₁` are **invariant** under that unitary (frozen/central,
  runner A3c).

**The decisive consequence.** Irreversibility fixes the recordable σ-algebra to be the **2 sector
labels** `{E₀, E₁}`. Microstate (within-block) information is **reversibly connected** → **not frozen**
→ **not faithfully recordable**. So the **von-Neumann/microstate reading is excluded by COMPUTATION**
(runner A3), **not by fiat**: there is no frozen microstate fact for a record to be noncommittal about.
**Minimum-information now operates on the 2-sector label content only.**

## §2 Part B — THE DECISIVE TEST: do sector-restricted minimum-information readings converge on type?

Each candidate "minimum-information" reading is **restricted to the 2 sectors** {singlet (dim 1),
doublet (dim 2)} and yields an isotype weight pair `(w_singlet, w_doublet)`. Via the block-total
Frobenius split `E₊ = ‖aI‖² = 3a²` (identity orbit), `E_⊥ = ‖bC + b̄C²‖² = 6|b|²` (shift orbit),
equalizing the **weighted** block energies gives **`r = w_doublet / (2 w_singlet)`**: TYPE `(1,1) → 1/2`,
TOKEN `(1,2) → 1` (the retained MRU weight-class dictionary `κ = 2μ/ν`).

### §2.1 The convergence table (runner Part B)

| reading | construction (restricted to the 2 sector LABELS) | `(w_s, w_d)` | kind | `r` | `Q` |
|---|---|---|---|---|---|
| **M1 Shannon** | max-entropy / uniform code over the 2 labels | `(1, 1)` | **TYPE** | **1/2** | **2/3** |
| **M2 MDL** | shortest prefix code to register which sector formed (1 bit each, dim-independent) | `(1, 1)` | **TYPE** | **1/2** | **2/3** |
| **M3 Landauer** | erasure cost of the sector-label register (`kT ln 2` per label, dim-independent) | `(1, 1)` | **TYPE** | **1/2** | **2/3** |
| **M4 Jeffreys** | reference prior over the 2-sector multinomial = `Beta(1/2, 1/2)`, label-symmetric | `(1, 1)` | **TYPE** | **1/2** | **2/3** |
| **M5 Kolmogorov** | minimal program to output "sector k" (label length, dim-independent) | `(1, 1)` | **TYPE** | **1/2** | **2/3** |
| **M6 sufficient-statistic** | minimal sufficient statistic for the frozen sector = the label index | `(1, 1)` | **TYPE** | **1/2** | **2/3** |
| **T0 token foil** | microstate pushforward `Tr(E_k · I/3) = d_k/3` (the maximally-mixed `I/3` marginal) | `(1, 2)` | **TOKEN** | **1** | **1** |

**The six sector-restricted minimum-information readings all give TYPE** `(1,1) → r = 1/2` (spread `= 0`;
runner B-CONV1/B-CONV2/B-CONV3). The destination is the explicit Brannen circulant at `r = 1/2`
(`a = 1, b = 1/√2`): equal block energies and spectrum `Q = 2/3` (runner B-DST1/B-DST2).

### §2.2 Why the danger candidates (M3 Landauer, M4 Jeffreys) land on type

These are the two readings most likely to sneak in dimension-weighting; the runner computes both
explicitly and **honestly**:

- **M3 Landauer.** The record **is the label**. Erasing the **label register** costs `kT ln 2` per
  **label** bit, **independent** of the sector's Hilbert dimension: resetting the "doublet-present" flag
  resets a 1-bit flag, not a `dim`-many register (runner B-M3a). The **dimension-erasure** reading
  (cost `∝ ln(d)` per block) does **not** rescue Born — it is **DEGENERATE**, not token: the singlet
  cost is `ln(1) = 0`, giving the pathological weight `(0, ln 2)` → `r = ∞`, **not** the Born token
  `(1,2) → r = 1` (runner B-M3b/B-M3c). So no Landauer reading gives token.
- **M4 Jeffreys.** The Jeffreys (reference) prior of the **2-outcome multinomial** (the 2 sector labels)
  is `Beta(1/2, 1/2)` — **symmetric** in the two labels (`α = β = 1/2`, mean `(1/2, 1/2)`), introducing
  **no** dimension dependence (runner B-M4a). The classical 2-outcome Fisher volume `1/√(p(1−p))` is
  **label-exchange symmetric** (runner B-BR4). The dimension-weighting Jeffreys is the **quantum (Bures)**
  prior over the `d`-dimensional **microstate** block — which is **excluded** by irreversibility
  (microstates non-recordable; the relevant Jeffreys, once restricted to the classical 2-label simplex,
  is the symmetric `Beta(1/2,1/2)`) (runner B-M4b).

### §2.3 The single token reading is doubly excluded

The **only** reading giving token `(1,2) → r = 1` is **T0**, the **microstate pushforward**: the
maximally-mixed quantum state `ρ = I/3` pushed to the sectors gives `p_k = Tr(E_k · I/3) = d_k/3 =
(1/3, 2/3)` (runner B-T0a). This is **excluded on two independent grounds**:

1. **Non-recordable (irreversibility).** `T0` puts the indifference prior over **microstates**, but
   microstates are non-frozen → non-recordable (Part A). It is **not** a sector-restricted reading at
   all; it lives on the excluded microstate space.
2. **Not minimum-information on the labels (minimum-information).** The token distribution `(1/3, 2/3)`
   has **strictly less** Shannon entropy on the 2-label space than uniform: `H(1/3, 2/3) = 0.918 bit <
   H(1/2, 1/2) = 1 bit` (runner B-T0b). It is therefore **more committed** — it is **not** the
   minimum-information distribution **on the recordable (label) content**. It is minimum-information on a
   **different** (microstate) space.

### §2.3a The strongest counterargument: "minimum information" has two readings — both give type

The hardest objection to the forcing is that "minimum information" is **itself ambiguous**, even on the
sector labels:

- **(R-maxent) minimum-information-CONTENT** = the max-entropy (Jaynes least-committed) distribution on
  the recordable label space → **uniform** `(1/2, 1/2)` → **TYPE**.
- **(R-faithful) minimum-EXCESS-over-source** = "store no more than the source provides" → reproduce the
  source's marginal on the labels.

The objection is that **(R-faithful)** gives token: the source marginal is `(1/3, 2/3)`. But this holds
**only if** the source is the microstate state `I/3` — a **non-recordable** microstate object (Part A).
If the source's **recordable** content is the **label alone** (which irreversibility establishes), there
is **no** microstate distribution to push forward: the faithful record of "which sector formed" is just
the **label occurrence**, 1 unit each → **TYPE** (runner B-T0c). So **both** readings, once microstates
are excluded by irreversibility, give **TYPE** (runner B-T0d). The `(1/3, 2/3)` answer of (R-faithful)
requires **reintroducing** the excluded microstate prior `I/3`. **This is the crux of the interlock:** it
is precisely irreversibility's restriction (microstates non-recordable) that collapses **both** readings
of minimum-information onto type. Absent irreversibility, (R-faithful) could match the `I/3` marginal and
give token — which is why **neither principle alone** forces `r = 1/2`.

### §2.4 Adversarial break attempts (try HARD to make a sector-restricted reading give token)

Six prior attacks precede this; a falsely-claimed closure is worse than an honest divergence. The runner
runs five explicit break attempts; **all confirm convergence-on-type**:

- **B-BR1 (Rényi/Tsallis).** For **every** order `q ∈ {1/2, 1, 2, 5, ∞}` (the Aczel-Daroczy family the
  framework already cites in
  [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md)),
  the max-entropy distribution on an **unconstrained** 2-label set is **uniform** → type, never token.
- **B-BR2 / B-BR2b (constrained max-ent).** To reach token `(1/3, 2/3)` by max-ent on labels, you must
  **impose** a constraint encoding dimension (`f_doublet − f_singlet = ln 2`). That constraint **is** the
  dimension/microstate input — it is **not** label-intrinsic; with **no** label-intrinsic constraint,
  max-ent is uniform → type.
- **B-BR3 (the steelman "doublet = 2 things").** The number of **frozen, recordable propositions** is
  `#blocks = 2`, **not** `sum-of-dims = 3`. The steelman counts the **non-recordable** doublet
  microstates; min-info records **1 proposition per block**.
- **B-BR4 (Fisher volume).** The classical 2-outcome Fisher volume is label-exchange symmetric → type;
  only the **quantum/dimension** volume breaks the symmetry (the excluded microstate route).
- **B-BR5 (distinctness).** The six readings are **six distinct constructions** (distinct construction
  signatures) that **converge** on type — per "no coincidences in frontier physics", multi-measure
  convergence is **structural**, not a relabel of one computation written six times.

**Decisive output: CONVERGE-ON-TYPE.** Among sector-restricted minimum-information readings, the answer
is **unique**: type → `r = 1/2`. The token reading is not sector-restricted and is not minimal on the
labels.

## §3 Part C — FORCED vs RESTATEMENT, and the two-principle status

### §3.1 The forcing is genuine (not a smuggle of "minimum = per-label")

The honest question: does minimum-information genuinely **force** type, or does it **smuggle** "count by
label" the way the record-binary attack smuggled "record = block"? It is a **genuine forcing**, for a
precise reason the runner computes:

- **Minimum-information is a STORAGE-MINIMIZATION criterion.** Among **faithful** sector-records, the
  per-**label** register has total size `2` (1 unit per label), while the per-**dimension** register has
  size `1 + 2 = 3`. Since `2 < 3`, minimum-information **selects** per-label = TYPE; the dimension-many
  register is **faithful-but-not-minimal** → excluded (runner C1a/C1b).
- **This is a strictly-new ordering that neither prior input supplies.** Additivity is **linear** — both
  `Tr` (token) and label-count (type) are additive over disjoint blocks (Pattern-L), so additivity does
  **not** order them (runner C2a). Irreversibility constrains only the **sign** of `dN/dt` — the sister
  branch showed the tracial-pushforward (token) record process is **equally** monotone/irreversible — so
  irreversibility does **not** order them (runner C2b). Minimum-information **adds** the ordering "smaller
  faithful register wins," which does **real work**: it is the missing bit (runner C2c).
- **It does not relocate the bit.** A relocation would mean the answer depends on "minimum of **which**
  measure." The Part-B convergence is precisely the refutation: among **sector-restricted** readings the
  answer is **unique** (all type), and the single token reading is excluded on **two** independent grounds
  (non-recordable AND non-minimal-on-labels; runner C3a/C3b). So once irreversibility restricts the
  content, minimum-information **lands**, it does not relocate.

**Why this is FORCED-MODULO-POSITS and not RESTATEMENT (contrast with the sister branch).** The sister
irreversibility test was RESTATEMENT because granting irreversibility did **not** entail block-counting —
the token process was equally irreversible. **Adding** minimum-information changes this: granting **both**
principles, the token reading is **excluded** (it is faithful-but-not-minimal **and** lives on the
non-recordable microstate space), so the conclusion (type) is **entailed**, not independently chosen. The
"smuggled premise" of the sister test ("count by presence, not occupied dimension") is **exactly** what
minimum-information **supplies** (presence-counting is the strictly-smaller faithful register). The bit is
therefore **derived from the second principle**, not assumed.

### §3.2 Principle status: BOTH posits (natural, but beyond bare axiom)

| principle | axiom-native? | status | basis |
|---|---|---|---|
| **IRREVERSIBILITY** ("records can't unform"; time flows by record formation) | **NO** | **POSIT** | the Record axiom scope **excludes** record production, persistence, decoherence, and **time arrow** ([`MINIMAL_AXIOMS_2026-06-04`](MINIMAL_AXIOMS_2026-06-04.md)); runner C4a |
| **MINIMUM-INFORMATION** ("store the least faithful record") | **NO** | **POSIT** | an **optimization** beyond additive readout `I(R₁ ⊔ R₂) = I(R₁) + I(R₂)`; it is MDL/parsimony/Landauer-efficiency, not in the axiom; runner C4b |

Neither posit is exotic: irreversibility ≈ records-are-frozen (the einselection/pointer fact);
minimum-information ≈ MDL / parsimony / Landauer thermodynamic efficiency — **both are standard
physical/inferential principles** (runner C4c). But both are **beyond the bare Record axiom**, so the
honest verdict is **FORCED-MODULO-TWO-POSITS** — a clean closure-modulo-two-named-physical-principles,
**not** axiom-native.

### §3.3 The `(α,β)` cone retained no-go is UNWEAKENED

Minimum-information is a measure-**selection** principle: it **selects** the Frobenius point `β = 0`
(equal isotype weight, type) as the **minimal-register** point. It does **not** collapse the
positive-definite cone `{α > 0, α + 3β > 0}` of
[`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
(`retained_no_go`) as an algebraic identity — the runner retains **7** PD points with `β ≠ 0` (runner
C5a/C5b). The no-go correctly states the **linear-algebra premises** do not force `β = 0`; this note
adds a **selection principle** (minimum-information) that **picks** `β = 0` as a point, which is exactly
the "independent authority that fixes the scalar/traceless isotype-weight ratio to 1" the no-go's
Boundary section calls for — supplied here as a **posited** principle, not as a strengthening of the
linear-algebra premises. The two are **consistent**.

## §4 Part D — law-invariance + category-mismatch closeout

- **Law-invariance (clears the wall the geometry attacks hit).** The sector-restricted minimum-information
  weights are **discrete** → **law-invariant**: sweeping a decay-law parameter, the type weight ratio
  `(1,1)` is **constant** (spread `0`), while a distance weighting **sweeps** (spread `0.645`, positive
  control) (runner D1a/D1b/D1c). So this attack lives on the **right kind of object** — unlike adjacency
  geometry.
- **Category-mismatch — does the pair CLOSE the bit or RELOCATE it?** **Closes.** Irreversibility delivers
  a **set-level, Boolean** object (the 2-label σ-algebra). Minimum-information delivers the **measure** on
  that set **uniquely** (Part-B convergence). The bridge between the set level and the operator-quadratic
  weight is exactly the **label-vs-microstate indifference** bit, and minimum-information **supplies** it
  ("minimal faithful register = per-label") (runner D2a/D2b/D2c). Had the sector-restricted readings
  **diverged**, the bit would relocate to "minimum-of-which-measure"; they **converge**, so it is
  **closed** (modulo the two posits).

## §5 Part E — bonus: do the two principles touch the other gates? (honest negative)

- **Chirality gate.** `Γ_χ = (2/3)J − I` is itself a **circulant** (commutes with `C`), so the retained
  chirality no-go
  [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  (`comm(C) ∩ anticomm(Γ_χ) = {0}`) applies (runner E1a). Minimum-information supplies a per-sector
  **weight operator** (`w₀E₀ + w₁E₁`), which is **circulant** (commutes with `C`) → it supplies **no
  C₃-orbit-splitting** (runner E1b). **The chirality gate does NOT move** — minimum-information fixes a
  **normalization**, not a chiral grading.
- **Color / sector-structure gate.** The sector **count** (1 singlet + 1 doublet) is the **retained**
  `ℝ[Z₃] = ℝ ⊕ ℂ` structure
  ([`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)), not
  something minimum-information sets; it weights a **given** decomposition (runner E2a). **No movement.**

**Honest negative:** minimum-information bears **only** on the `r = 1/2` measure bit; the chirality and
color/sector-structure gates stay exactly where the prior tests left them.

## §6 Honest verdict — FORCED-MODULO-TWO-POSITS

Of the possible outcomes the result is **FORCED-MODULO-TWO-POSITS** — the strongest honest outcome short
of bare-axiom-native, and a **material advance** over the sister branch's RESTATEMENT:

- **NOT DIVERGE/AMBIGUOUS.** The six sector-restricted minimum-information readings (M1 Shannon, M2 MDL,
  M3 Landauer, M4 Jeffreys, M5 Kolmogorov, M6 sufficient-statistic) **converge** on type `(1,1) → r = 1/2`
  (spread `0`). The danger candidates (Landauer, Jeffreys) land on type; the dimension-Landauer reading is
  **degenerate** (not token), and the dimension-Jeffreys is the **excluded** quantum/microstate prior. No
  sector-restricted reading gives token.
- **NOT RESTATEMENT.** Granting **both** principles **entails** type: the token reading is excluded on two
  independent grounds (non-recordable **and** non-minimal-on-labels), so the conclusion is **not**
  independently chosen. Minimum-information **supplies** exactly the "count by presence, not occupied
  dimension" bit the sister branch found unsupplied.
- **NOT FORCED-AND-AXIOM-NATIVE.** Both principles are **posits** — the Record axiom's scope excludes
  arrow/persistence (irreversibility) **and** any store-the-least optimization (minimum-information).

**The combined claim.** **IRREVERSIBILITY** (fixes the recordable σ-algebra = the 2 sector labels) **+
MINIMUM-INFORMATION** (minimal faithful register = 1 unit per label) **TOGETHER FORCE** `r = 1/2`
(`Q = 2/3`). **Neither alone suffices.** `AC_φλ` for the charged-lepton sector **reduces to these two
named physical principles** — a clean closure-modulo-two-posits. This is the culmination of the seven-attack
arc: geometry (wrong kind of object) → record-binary (RESTATEMENT, needs "record = block") → irreversibility
(proves the σ-algebra, RESTATEMENT on the measure) → **irreversibility + minimum-information (forces the
measure, modulo two posits).**

**The genuine residual (named precisely).** The result is **modulo two posits**. To make it axiom-native,
a future source result would have to **derive** either (a) irreversibility / the record-formation arrow,
or (b) the minimum-information / parsimony principle, from the framework's record/measurement structure
(the Record axiom + dynamics). This note neither supplies nor forecloses that. It does **prove** that
**given** the two principles, the type measure (`r = 1/2`) is **forced** — the bit is no longer open
**modulo** the principles.

## §7 What this note does NOT do

- Does **not** claim `r = 1/2` / `Q = 2/3` is derived from the bare Lattice/Quantum/Record axioms with no
  added principle. The forcing is **modulo two named posits** (irreversibility + minimum-information).
  `r = 1/2` remains the Tier-A admitted input `AC_φλ`.
- Does **not** edit any axiom. [`MINIMAL_AXIOMS_2026-06-04`](MINIMAL_AXIOMS_2026-06-04.md) (Lattice /
  Quantum / Record) is untouched; irreversibility and minimum-information are exploratory **posited**
  principles, **not** adopted as primitives.
- Does **not** set audit status, promote any row, or weaken any retained no-go. The isotype-split no-go
  (`retained_no_go`) is left **unweakened** (selected at a point, not algebraically collapsed; §3.3); the
  chirality no-go (`retained_bounded`) is **corroborated** (Part E: minimum-information supplies no
  orbit-splitting).
- Does **not** re-derive the sister irreversibility result. The superselection / no-finer-than-block
  σ-algebra result is **used** (Part A confirms the two facts built on), not re-proven.
- Does **not** import external comparators or PDG values. `√2`, `r = 1/2`, `Q = 2/3`, and the weights
  `(1,1)` / `(1,2)` are lattice/algebra structural data; the runner uses **no** measured mass.

## §8 Audit-lane handoff

- **Claim type:** bounded_theorem. Clean **forced-or-not** result; the forcing **holds** (CONVERGE-ON-TYPE),
  the residual is the **two posits** (named, classified), no value discharged. Honest tier matches the
  sister `retained_bounded` block-weight frontier
  ([`KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29`](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md);
  [`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md)).
- **No status to set.** This note proposes no promotion. `r = 1/2` remains Tier-A `AC_φλ`.
- **Runner:** PASS=50, FAIL=0; every PASS keyed to a substantive computed assertion (centers by
  product-closure + commutant nullspace; the within-doublet ray falsification explicitly run; the six
  sector-restricted readings each computed; the token foil's entropy deficit computed; five adversarial
  break attempts run; no hard-coded `True`).
- **Dependency posture:** depends only on the framework baseline (Brannen circulant structure, the
  `hw = 1` orbit, `ℝ[Z₃] = ℝ ⊕ ℂ`), the Record axiom (for the additive-record target), the sister
  irreversibility result (for the σ-algebra restriction), and the retained unique-tracial-state
  characterization (for the Born/microstate foil). It **load-bears on none** of the cited retained rows
  and **weakens none**. It does not load-bear on `closure_c_staggered_dirac_gate` or any open-gate output.

## §9 Cross-references

- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) — the Record axiom (additivity) and its
  scope sentence excluding record-production, persistence, decoherence, and **time arrow** (basis for the
  POSIT classification of **both** principles).
- [`RECORD_IRREVERSIBILITY_BLOCK_COUNTING_R_HALF_DERIVATION_NOTE_2026-06-04.md`](RECORD_IRREVERSIBILITY_BLOCK_COUNTING_R_HALF_DERIVATION_NOTE_2026-06-04.md)
  (sister branch `codex/record-irreversibility-block-counting-r-half-2026-06-04`) — the **proven**
  σ-algebra = blocks result (no finer frozen fact) that this note **uses as the restriction**, and the
  precise type-vs-token residual this note **fills**.
- [`RECORD_BINARY_EQUAL_POWER_MEASURE_R_HALF_TEST_NOTE_2026-06-04.md`](RECORD_BINARY_EQUAL_POWER_MEASURE_R_HALF_TEST_NOTE_2026-06-04.md)
  (sister branch `codex/record-binary-equal-power-r-half-2026-06-04`) — the RESTATEMENT predecessor
  ("record = block" needed); the "individuate by PRESENCE vs DIMENSION" bit minimum-information now
  supplies.
- [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  — `retained_no_go`: the `(α,β)` PD cone; left **unweakened** (Part C / runner C5); its Boundary's
  call for "an independent authority that fixes the isotype-weight ratio to 1" is answered here by a
  **posited** selection principle (minimum-information).
- [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
  — `r = 1/2 ⟺ Q = 2/3` (the retained biconditional); the `κ = 2μ/ν` weight dictionary.
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
  — `AC_φλ`; the equal-power-vs-dimension measure fork; the two named selectors (K-reality + block-count)
  — block-count is exactly what this note's minimum-information supplies.
- [`OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md`](OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md)
  — the Shannon-Khinchin-Aczel-Daroczy classification (the Rényi/Tsallis family of break attempt B-BR1).
- [`KOIDE_V_BAE_MAXENTROPY_THERMAL_NOTE_2026-05-08_probeV_bae_maxent.md`](KOIDE_V_BAE_MAXENTROPY_THERMAL_NOTE_2026-05-08_probeV_bae_maxent.md)
  — the prior MaxEntropy probe: max-ent on the **Born density** (a microstate/operator-config measure)
  decouples from `(a,b)`; consistent with this note's finding that the **microstate** reading is the
  token side, while the **sector-label** reading is type.
- [`KOIDE_FISHER_RAO_SPHERICAL_REORGANIZATION_NOTE_2026-06-01.md`](KOIDE_FISHER_RAO_SPHERICAL_REORGANIZATION_NOTE_2026-06-01.md)
  — the Fisher-Rao reorganization (the classical-Fisher / Jeffreys symmetry used in M4 / B-BR4).
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md)
  — the unique tracial state `I/3` (the microstate / Born pushforward = the token foil T0).
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  — the chirality no-go; Part E **corroborates** it (minimum-information supplies no orbit-splitting).
- [`KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md`](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md),
  [`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md)
  — the `retained_bounded` block-weight frontier this note's honest tier matches.
- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) — the
  retained 3-generation structure (`ℝ[Z₃] = ℝ ⊕ ℂ`, count 3) cross-checked in Part E.
