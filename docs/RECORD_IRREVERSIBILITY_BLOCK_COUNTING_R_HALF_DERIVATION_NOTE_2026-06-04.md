---
claim_id: record_irreversibility_block_counting_r_half_derivation_note_2026-06-04
claim_type_author_hint: bounded_theorem
---

# Record IRREVERSIBILITY → Block-Counting → `r = 1/2`? The Superselection Crux Holds at the σ-Algebra Level but Does Not Force the Measure — Decisive Culminating Test

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the canonical
> source-of-truth doc.

**Date:** 2026-06-04
**Claim type:** bounded_theorem. This note reaches a clean, ruthlessly-honest result with a
single named residual. The proposed "irreversibility ⟹ frozen ⟹ superselection ⟹ center ⟹
block-count ⟹ `r = 1/2`" chain has a **true crux** — irreversible/frozen record information **is**
block-level, with **no finer-than-block frozen fact** (the superselection step **holds**, and an
explicit falsification attempt **fails**) — **but** "no finer frozen fact" fixes only the frozen
**σ-algebra** (the blocks), **not** the **measure** on it. Two block-level measures use **only** the
frozen center: the **counting** measure → `(1,1)` → `r = 1/2`, and the **tracial pushforward** → `(1/3,2/3)`
→ `r = 1`. Irreversibility does **not** select between them. **Verdict: RESTATEMENT, sharpened.** The
missing bit reduces to one named measure-theoretic choice (indifference over superselection **labels**
vs over **microstates**), which irreversibility does not supply.
**Status authority:** independent audit lane only. This note sets no audit status, promotes no row,
weakens no retained no-go, and edits no axiom. `r = 1/2` remains the Tier-A admitted input `AC_φλ`;
it is compared **structurally** only (no PDG value consumed).
**Primary runner:**
[`scripts/record_irreversibility_block_counting_r_half_derivation.py`](../scripts/record_irreversibility_block_counting_r_half_derivation.py)
(SUMMARY: PASS=49 FAIL=0).
**Cached log:**
[`logs/runner-cache/record_irreversibility_block_counting_r_half_derivation.txt`](../logs/runner-cache/record_irreversibility_block_counting_r_half_derivation.txt)

---

## §0 The exact gap, and what is decisively different about this attack

The charged-lepton Brannen modulus `r = |b|²/a² = 1/2` (equivalently Koide `Q = 2/3` via the retained
biconditional [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md))
is the single Tier-A admitted input `AC_φλ` on the value chain
([`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)). Its
residual is sharply located: the **equal-power-per-block** (det_C / block-count) measure selects
`r = 1/2`; the **Born/dimension** (det_R) measure selects `r = 1`.

**A long arc localized the gate to a single discrete bit.**

- **Three adjacency-geometry attacks** (single face-diagonal; all diagonals / L2; all-to-all + Planck)
  all failed: geometry gives a **law-DEPENDENT** amplitude ratio (the singlet/doublet power swings with
  the decay law), whereas the equal-power measure is **law-INVARIANT** — geometry is the wrong **kind**
  of object.
- The **record-binary attack** (sister branch
  [`RECORD_BINARY_EQUAL_POWER_MEASURE_R_HALF_TEST_NOTE_2026-06-04`](RECORD_BINARY_EQUAL_POWER_MEASURE_R_HALF_TEST_NOTE_2026-06-04.md);
  read first) got onto the right layer (discrete, law-invariant) and **reached `r = 1/2` exactly** — but
  its verdict was **RESTATEMENT**: it needed the added premise "record = central idempotent / block".
  Bare record **additivity** is **linear** (so `Tr` is additive too — Pattern-L), and the isotype
  measure is **quadratic**, so additivity does not select block over dimension. **The single missing
  bit: does the carrier individuate records by PRESENCE (block, → 1/2) or by DIMENSION (Born, → 1)?**

**The proposed unlock (the user's principle).** Records cannot unform once formed; time flows by record
formation. The candidate derivation of the missing bit:

1. A record that cannot unform is a **frozen, irreversible, classical** fact.
2. On a finite quantum operator algebra, the frozen/irreversible/classical facts are precisely the
   **superselection sectors = the center = the central idempotents = the Wedderburn blocks**. Within a
   simple block `M_n` all states are reversibly connected by unitaries, so **no** frozen distinction
   finer than the block exists; only **across** blocks (the center) is there an irreversible
   distinction.
3. Therefore an irreversible record is necessarily a **block-fact**, never a within-block (dimension)
   fact.
4. Record-counting by irreversible formation counts **blocks**, each once, independent of block
   dimension → **block-counting** → equal-power → `r = 1/2` → `Q = 2/3`.

**This is the right layer, and Step 2/3 is genuinely true.** What this test establishes — by computing
the centers explicitly and by **attempting and failing** to construct a finer frozen record — is that
the superselection crux **holds**: irreversible/frozen record information **is** block-level. But it
also establishes, decisively, that this is **not enough**: "no finer frozen fact" fixes the frozen
**σ-algebra** (the block partition), **not** the **measure** on it — and the block-vs-dimension choice
is a choice of **measure**, not of σ-algebra. So the unlock **sharpens** but does not **close** the bit.

## §1 Part A — THE CRUX: irreversible/frozen record information is block-level (and no finer)

**Step 3 holds. The superselection argument delivers exactly what it claims — and no more.**

### §1.1 Within a simple block there is no nontrivial frozen fact (center is trivial)

The runner computes the center of a full simple matrix block directly (build the algebra by product
closure; solve `[X, a] = 0` for all algebra elements `a`):

- `center(M₂(ℂ)) = ℂ·I` (center-dim **1**, algebra-dim 4) — runner A2a.
- `center(M₃(ℂ)) = ℂ·I` (center-dim **1**, algebra-dim 9) — runner A2b.

So **within a simple matrix block there is no nontrivial frozen/superselected observable**: all pure
states lie on one unitary orbit, reversibly connected. This is the einselection/pointer-theory fact
that the maximal set of mutually-frozen classical facts is the **center** of the algebra.

### §1.2 The center of `ℝ[Z₃] = ℝ ⊕ ℂ` is the block labels

The two minimal **real** central idempotents are the singlet projector `E₀` (rank 1) and the doublet
projector `E₁` (rank 2), with `E₀E₁ = 0`, `E₀² = E₀`, `E₁² = E₁` (runner A3a). Over `ℂ` there are three
rank-1 Fourier projectors; the conjugate pair fuses into the **real** rank-2 doublet — the frozen,
time-reversal-real block (runner A3b). So the **frozen/classical σ-algebra = the center = span{E₀, E₁} =
the block labels.**

### §1.3 Falsification attempt — a finer-than-block frozen record — FAILS

A within-doublet ray-distinction would be a frozen fact **finer** than the block. The runner tests
whether a rank-1 projector `P_ray` inside the doublet can be such a fact:

- `‖[P_ray, C]‖ = 1.2247 > 0`: a doublet-ray projector is **not central** (runner A4a).
- The doublet's own internal unitary `U = exp(iθ·i(C−C²))` **moves** the ray:
  `‖U P_ray U† − P_ray‖ = 1.3244 > 0` (runner A4b) — the two doublet directions are **reversibly
  connected**, hence not classical/irreversible.
- By contrast the **block** projectors `E₀, E₁` are **invariant** under that internal unitary
  (frozen/central) — runner A4c.

**The falsification fails: no finer-than-block frozen record exists.** This is the strongest part of the
unlock, and it is **true**: I tried hard to build a within-block frozen fact and the algebra forbids it.

### §1.4 The decisive refinement — "no finer frozen fact" fixes the σ-algebra, NOT the measure

Here is where the chain's Step 4 over-reaches. "No finer frozen fact" forces the **σ-algebra of frozen
facts to be the blocks**. It does **not** force the **measure** on that σ-algebra. There are (at least)
**two** block-level measures, **both** functions of the (frozen) center, **neither** requiring any finer
frozen fact:

| measure | construction (uses only the frozen center) | weights | `r` | `Q` |
|---|---|---|---|---|
| **counting** | each minimal central idempotent weight 1 | `(1,1)` | **1/2** | **2/3** |
| **tracial pushforward** | block weighted by `Tr(E_k · I/3)` = occupation prior | `(1/3,2/3)` | **1** | **1** |

Both are computed end-to-end (runner A6a/A6b) and give **different** `r` (runner A6c). Crucially, the
**dimension/Born weight is the tracial STATE `I/3` pushed through the (frozen) blocks** — it uses **no
within-block frozen fact**. So superselection does **not** exclude it. **The crux delivers the partition;
it does not deliver the weight.**

This matches, and makes precise, the two prior near-misses on `origin/main`:
[`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02`](FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md)
(objectivity fixes the **basis**, not the **weight**) and
[`KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31`](KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31.md)
(the `S = C + C²` pointer fixes the two-atom **σ-algebra**, not the **measure**).

## §2 Part B — block-count → `r = 1/2`; dimension-count → `r = 1`; structural law-invariance

Given the block-count partition, the isotype weights on `ℝ[Z₃] = ℝ ⊕ ℂ` follow from the block-total
Frobenius split `E₊ = ‖aI‖² = 3a²` (identity-orbit), `E_⊥ = ‖bC + b̄C²‖² = 6|b|²` (shift-orbit):

- **BLOCK-count `(1,1)`** equalizes the block energies `3a² = 6|b|²` ⟹ `r = 1/2`, and the explicit
  Brannen circulant at `r = 1/2` (`a=1, b=1/√2`) has **equal** block energies and spectrum `Q = 2/3`
  (runner B2/B2b).
- **DIMENSION-count `(1,2)`** gives `E_⊥ = 2E₊` ⟹ `r = 1`, and the explicit circulant at `r = 1`
  (`a=b=1`) has `E_⊥ = 2E₊` and spectrum `Q = 1` (runner B3/B3b).

**Structural law-invariance (the discriminator that killed geometry).** A measure is law-invariant iff
its doublet/singlet weight ratio is independent of any continuous parameter. **Both** block-level counts
are discrete, so **both** are law-invariant (ratio spread `= 0`; runner B4a/B4b), while a distance
weighting **is** law-dependent (spread `0.882`; positive control B4c). So block-count via the frozen
center **clears** the wall the geometry attacks hit — **necessary**, but **not sufficient**: law-invariance
does **not** pick `(1,1)` over `(1,2)` (runner B4d).

## §3 Part C — FORCED vs RESTATEMENT, and axiom-native vs posit (the discipline crux)

**Is the chain a genuine derivation, or does it smuggle "record = block"?** The honest answer is that
the chain delivers the **partition** (Part A) but **smuggles the measure**. Specifically:

- **NOT FORCED.** Equal-power is forced only if the frozen structure **excludes** the dimension weight.
  It does not: the dimension/Born weight is the **tracial pushforward** through the frozen blocks (§1.4),
  needs **no** finer-than-block fact, and — decisively — is itself **irreversibly realizable**. The
  runner simulates a monotone, irreversible record-formation process where block-`k` records accrue at
  rate `∝ Tr(E_k · I/3)`: the **token** count converges to `(1/3, 2/3) → r ≈ 1` (Born), while the
  **type** count is `(1,1) → r = 1/2` (runner C2a/C2b). **Both processes are monotone and irreversible**
  ("records can't unform"). So irreversibility constrains the **sign** of `dN/dt`, **not** the per-block
  **weight** (runner C2c). It does not select counting over the tracial frequency.

- **The steelman, and why it still fails to force.** The strongest pro-unlock argument: "a frozen fact
  is a **proposition** (counted once), and weighting by dimension over-counts reversibly-connected
  microstates that are **not** distinct facts." But the **canonical retained state** on the qubit-`Z³`
  algebra is the **unique tracial state `I/3`**
  ([`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md),
  the uniqueness half), and it weights each **minimal projection** equally `= 1/3` — i.e. **per
  dimension** — so a block gets weight `=` its dimension `=` Born (runner C3a). Therefore:

  > **block-count `(1,1)` = indifference over superselection LABELS; Born `(1,2)` = indifference over
  > MICROSTATES (the tracial pushforward).** Irreversibility makes the **labels** classical, but it does
  > **not** tell you to be indifferent over **labels** rather than over **microstates** (runner C3b).

  **This is the single unsupplied bit, now named precisely.** The unlock **sharpens** the gate from a
  vague "block vs dimension" to a sharp, classifiable measure-theoretic choice — but it does not close
  it.

- **The `(α,β)` cone is unweakened.** Irreversibility is (at most) a measure-**selection** principle; it
  does not collapse the positive-definite cone `{α > 0, α + 3β > 0}` of the retained no-go
  [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  to `β = 0` (runner C5 retains 9 PD points including `β ≠ 0`).

- **Axiom-native or posit? POSIT.** The Record axiom
  ([`MINIMAL_AXIOMS_2026-06-04`](MINIMAL_AXIOMS_2026-06-04.md), Record) supplies **only** additive scalar
  record readout `I(R₁ ⊔ R₂) = I(R₁) + I(R₂)`, `I(∅) = 0`. Its own scope sentence states it does **not**
  supply "a rule for record production, persistence, measurement/decoherence, … time arrow." **So
  irreversibility ("records can't unform" + "time flows by record formation") is NOT in the Record
  axiom — it is an added dynamical principle, a posit** (runner C6b). And `AC_φλ` is explicitly listed as
  an open gate **outside** axiom content (runner C6c). Hence even the part that **is** delivered (the
  block partition) rests on a **posited** dynamical principle, not on bare-axiom content.

**Why RESTATEMENT and not FORCED-MODULO-IRREVERSIBILITY-POSIT.** A FORCED-MODULO-POSIT verdict would
require that **granting** irreversibility **entails** block-counting. It does not: the tracial-pushforward
(Born) record process is **equally** irreversible and monotone (Part C / runner C2a). The step from
"irreversible" to "count labels, not microstates" is **exactly** the missing bit and is **not** entailed
by irreversibility — so the block-individuation is **smuggled** via the type-vs-token choice. That is the
defining signature of **RESTATEMENT** (the conclusion is reachable only by independently choosing the
thing to be shown), now localized one level deeper than the sister test: not at "record = block"
(σ-algebra), but at "count blocks by **presence**, not by **occupied dimension**" (measure).

## §4 Part D — time-arrow → chirality `C₃`-breaking (corroboration; honest negative)

"Time flows by record formation" makes the monotone-growing record-set the **arrow of time**. Does this
**directional** structure supply the `C₃`-orbit-splitting the chirality gate needs (which pure
`C₃`-symmetric structure cannot)? `Γ_χ = (2/3)J − I` is itself a **circulant** (lies in `⟨I, C, C²⟩`), so
the retained chirality no-go
[`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
(`comm(C) ∩ anticomm(Γ_χ) = {0}`) applies. The runner tests two arrow structures:

- **The formation-arrow operator** `A = i(C − C²)` (the T-odd, formation-order-asymmetric Hermitian
  generator) is **still circulant** (commutes with `C`), so it does **not** anticommute with `Γ_χ`
  (`‖{A, Γ_χ}‖ = 4.899 ≠ 0`; runner D2a/D2b). The arrow **lives in** the circulant algebra and cannot
  leave it.
- **A formation-order ranking** `diag(3,2,1)` (which **breaks** `C₃`, leaving the circulant algebra) is
  **site-diagonal** — the **same wrong-basis problem** as the record-binary on-site `Z₂`: it does **not**
  anticommute with the circulant `Γ_χ` (runner D3b), and it induces a **non-circulant** `H`, so the
  Brannen `Q = 1/3 + (2/3)r` structure the Koide value requires **breaks** (runner D3c).

**Honest negative: the time-arrow does NOT reach `Q = 2/3` chirality.** The no-go is robust to the
arrow (runner D4). The formation-order `C₃`-breaking is in the wrong (site-diagonal) basis, exactly as
the record-binary `Z₂` was; the directional structure does not supply the correctly-structured grading.

## §5 Part E — hostile / category-mismatch closeout

- **Law-invariance closeout (re-confirmed).** Block-count via the frozen center is discrete and
  law-invariant — it clears the wall the geometry attacks hit (runner E1).
- **The deepest hostile check — is "3 generations = 1 singlet + 1 doublet" free?** Yes, in the sense
  that the real-irreducible decomposition `ℝ[Z₃] = ℝ ⊕ ℂ` is the **standard unique** real decomposition,
  and the count `3 = dim(regular rep) = 1 + 2` is the **retained** 3-generation structure
  ([`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)), not an
  extra input here (runner E2a). **But the COUNTING-vs-DIMENSION tension is structural:** the same `C₃`
  that yields the count 3 **forces `H` circulant** (`[H, C] = 0`), and the **dimension/Born** weight
  `(1,2)` is what tracks that dimension; block-count `(1,1)` is the alternative that does **not** track
  the dimension that produced the count (runner E2b). Irreversibility does not resolve this tension.
- **Category mismatch — the root of the whole difficulty.** Irreversibility forces a **set-level,
  Boolean** object (the frozen σ-algebra = the blocks). The Koide weight is a **quadratic form on
  operators** (the block energies `B(A,A) = α Tr(AB) + β tr(A)tr(B)`). A set-level "no finer frozen fact"
  cannot, by itself, fix an operator-level quadratic-form normalization; the **label-vs-microstate
  indifference** bit is exactly the bridge between the two levels, and it is unsupplied (runner E3).

## §6 Honest verdict — RESTATEMENT (sharpened to a single named measure bit)

Of the four possible outcomes the result is **RESTATEMENT**, but a **materially sharper** one than the
sister test:

- **NOT CRUX-FAILS.** The superselection crux **holds**: irreversible/frozen record information **is**
  block-level, with **no finer-than-block frozen fact** (center of `M_n` trivial; within-doublet ray not
  central and reversibly moved). The explicit falsification attempt **failed**. This is a genuine,
  verified positive: a within-block frozen record is **impossible**, so dimension-counting cannot be
  realized by a **finer frozen fact**.
- **NOT FORCED-AND-AXIOM-NATIVE, NOT FORCED-MODULO-IRREVERSIBILITY-POSIT.** "No finer frozen fact" fixes
  the frozen **σ-algebra**, not the **measure**. The dimension/Born weight is the **tracial pushforward**
  through the same frozen blocks — it needs no finer fact and is **itself irreversibly realizable**
  (monotone token accumulation). So irreversibility does **not** force block-counting; granting it does
  **not** entail the conclusion.
- **RESTATEMENT (the verdict).** Block-count `(1,1) → r = 1/2` is reachable **only** by the added,
  independent choice "count records by **presence** (one token per superselection **label**), not by
  **occupied dimension** (the tracial/Born **microstate** weight)". That choice is the missing bit; it is
  **not** entailed by irreversibility. **The smuggled premise moved one level deeper** — from "record =
  block" (σ-algebra, sister test) to "block measured by label-count, not microstate-occupation"
  (measure, this test).

**The genuine sharpening this delivers (not a closing claim).** Three prior attacks (objectivity,
records-pointer, einselection) each reduced the gate to "fixes basis/σ-algebra, not weight." This test
**proves the σ-algebra half outright** (no finer frozen fact — a verified impossibility, not a
stipulation) and **names the weight half precisely**: it is **indifference over superselection LABELS
(block-count, → 1/2) vs over MICROSTATES (tracial pushforward, → 1)**. The next path this opens is
therefore sharply posed and independent of geometry, partition, and dynamics: **a principle that fixes
the record-counting NORMALIZATION (per-label vs per-microstate)** — a measure/indifference principle on
the frozen center, not an adjacency, a basis, or an arrow. If a future source result derives **that**
one normalization from the framework's record/measurement structure, the no-go closes on the block side;
this note neither supplies nor forecloses it.

## §7 What this note does NOT do

- Does **not** find irreversibility to force block-counting, and does **not** claim `r = 1/2` / `Q = 2/3`
  is derived. The verdict is RESTATEMENT; `r = 1/2` remains the Tier-A admitted input `AC_φλ`.
- Does **not** edit any axiom. [`MINIMAL_AXIOMS_2026-06-04`](MINIMAL_AXIOMS_2026-06-04.md) (Lattice /
  Quantum / Record) is untouched; the irreversibility / record-formation-arrow principle is an
  exploratory **posited** dynamical surface, **not** adopted as a primitive.
- Does **not** set audit status, promote any row, or weaken any retained no-go. The isotype-split no-go
  (`retained_no_go`) and the chirality no-go (`retained_bounded`) remain correct on their scope; this
  note's RESTATEMENT verdict is **consistent** with both, and Part D explicitly **corroborates** the
  chirality no-go (robust to the arrow).
- Does **not** import external comparators or PDG values. `√2`, `r = 1/2`, `Q = 2/3` are lattice/algebra
  structural data; the runner uses **no** measured mass.
- Does **not** claim the unlock is worthless: it **proves** the σ-algebra half (no finer frozen fact),
  which the prior objectivity/pointer/einselection notes left as a stipulation, and it **names** the
  residual measure bit precisely. It simply does not rise to a forcing — the label-vs-microstate
  normalization remains unsupplied.

## §8 Audit-lane handoff

- **Claim type:** bounded_theorem. Clean forced-or-not result; single named residual (the per-label vs
  per-microstate normalization bit), no value discharged. Honest tier matches the sister
  `retained_bounded` block-weight frontier
  ([`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md);
  [`KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29`](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md)).
- **No status to set.** This note proposes no promotion. `r = 1/2` remains Tier-A `AC_φλ`.
- **Runner:** PASS=49, FAIL=0; every PASS keyed to a substantive computed assertion (centers computed by
  product-closure + commutant nullspace; falsification attempt explicitly run and failed; the two
  block-level measures and the monotone-formation simulation both computed; no hard-coded `True`).
- **Dependency posture:** depends only on the framework baseline (Brannen circulant structure, the
  `hw = 1` orbit, `ℝ[Z₃] = ℝ ⊕ ℂ`), the Record axiom (for the additive-record target), and the retained
  unique-tracial-state characterization (for the Born/microstate pushforward). It **load-bears on none**
  of the cited retained rows and **weakens none**. It does not load-bear on
  `closure_c_staggered_dirac_gate` or any open-gate output.

## §9 Cross-references

- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) — the Record axiom (additivity) and its
  scope sentence excluding record-production, persistence, decoherence, and time arrow (the basis for the
  POSIT classification of irreversibility).
- [`RECORD_BINARY_EQUAL_POWER_MEASURE_R_HALF_TEST_NOTE_2026-06-04.md`](RECORD_BINARY_EQUAL_POWER_MEASURE_R_HALF_TEST_NOTE_2026-06-04.md)
  (sister branch `codex/record-binary-equal-power-r-half-2026-06-04`) — the RESTATEMENT predecessor and
  the precise "single bit" residual this test attacks one level deeper (σ-algebra → measure).
- [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
  — `retained_no_go`: the `(α,β)` PD cone; left unweakened (Part C / runner C5).
- [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
  — `r = 1/2 ⟺ Q = 2/3`.
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
  — `AC_φλ`; the equal-power-vs-dimension measure fork; the two named selectors (K-reality + block-count).
- [`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md`](FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md)
  — `no_go`: objectivity fixes the basis, not the weight; its N7 steelman ("counting by labels is a
  coherent possible additional principle") is exactly the bit this note names and shows irreversibility
  does not supply.
- [`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md)
  — einselection fixes the 2-sector partition (modulo K-reality) but the Born/thermalizing measure gives
  `r = 1`; the same partition-vs-measure split, in dynamics language.
- [`KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31.md`](KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31.md),
  [`KOIDE_RECORDS_POINTER_GROUNDS_BLOCK_CHANNEL_NOTE_2026-05-31.md`](KOIDE_RECORDS_POINTER_GROUNDS_BLOCK_CHANNEL_NOTE_2026-05-31.md),
  [`KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md`](KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md)
  — the pointer/records lane: the `S = C + C²` pointer fixes the two-atom σ-algebra; the measure on the
  atoms (count vs rank/Born) is the residual; `(1,1)` + objectivity-maximization is a **conditional**
  route, both inputs named.
- [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md)
  — the unique tracial state `I/3` on the qubit-`Z³` algebra (the per-microstate / Born pushforward used
  in Part C).
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  — the chirality no-go `comm(C) ∩ anticomm(Γ_χ) = {0}`; Part D corroborates it (robust to the
  formation-order arrow).
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md),
  [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
  — the "time from records/evolution" lane for the time-arrow framing of Part D.
- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) — the
  retained 3-generation structure (`ℝ[Z₃] = ℝ ⊕ ℂ`, count 3) cross-checked in Part E.
