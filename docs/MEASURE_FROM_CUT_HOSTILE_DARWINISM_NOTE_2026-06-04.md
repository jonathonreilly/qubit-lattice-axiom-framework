# Flavor — "measure-from-the-cut" is NOT a new forcing mechanism: it is the broken minimum-information argument repackaged (front 1, killed by quantum Darwinism) + a rename of the real-vs-complex / dimension slot (front 3). `r=1/2` stays a distinguished STABLE SETTING, not the record-FORCED measure.

**Date:** 2026-06-04
**Claim type:** meta
**Claim boundary:** a hostile soundness check on one proposed mechanism. It does **not** force
`r=1/2`, does **not** exclude `r=1/2`, approves no import, and sets no audit verdict. It verifies,
as concrete linear algebra on the `Z₃`-circulant 2-block carrier, that the "measure-from-the-cut"
argument does **not** force the block-counting measure (`r=1/2`) over the Born/dimension measure
(`r=1`). Consistent with the campaign's standing: `r=1/2` is the distinguished block-count /
2-sector-equipartition **setting** on the dial; the cut neither forces nor excludes it.
**Runner:** [`scripts/measure_from_cut_hostile_darwinism_2026_06_04.py`](../scripts/measure_from_cut_hostile_darwinism_2026_06_04.py) (SCORECARD PASS=27, FAIL=0).
**Cache:** [`logs/runner-cache/measure_from_cut_hostile_darwinism_2026_06_04.log`](../logs/runner-cache/measure_from_cut_hostile_darwinism_2026_06_04.log).

## The mechanism under attack

> "A record resolves only the **PARTITION** (which Wedderburn block: singlet `ℝ` ⊕ doublet `ℂ`),
> not the within-block **state** (within-block is reversible/quantum, unrecorded). So a classical
> record can only **BLOCK-COUNT** (→ `r=1/2`); the **BORN/DIMENSION** measure (→ `r=1`) requires
> within-block **state-counting** the record lacks. Hence `r=1/2` is the record-natural setting,
> `r=1` the within-block setting — two distinguished settings on the dial."

If sound, this would **close** the gate the campaign explicitly leaves open
([`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md),
[`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md)):
*the Born/dimension measure gives `r=1`; `r=1/2` is the separate equal-power-per-block input.* The
hostile question (per the user's frame — do not force `r=1/2`, do not save it) is strictly whether
that closure is **sound** or whether it **repackages the previously-broken minimum-information
argument** (broken by quantum Darwinism: objective classical records are **maximally redundant**, not
minimal).

## Calibration (the object is the real one)

`H = aI + bC + b̄C²` on `ℂ³`; real Wedderburn blocks `P₀` (singlet, rank 1) and `P₁` (doublet, rank 2);
`r=|b|²/a²`; exact `Q = 1/3 + (2/3)r` (retained). `r=1/2 → Q=2/3`; `r=1 → Q=1`. `H` is block-diagonal
in `{P₀,P₁}` for **every** `r`, so a pointer/einselection map is a literal no-op on `r` (CAL-1…6 PASS,
matching `FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY`). The dial's two named ends: Born/**dimension**
weights blocks `Tr P₀:Tr P₁ = 1:2 → r=1`; **block-count** (equal power per block) weights `1:1 → r=1/2`.

## Per-front verdict

### Front 1 — Darwinian redundancy: **REPACKAGED-BROKEN-ARGUMENT** (the mechanism fails here)
- **F1.1** Redundancy does **not** enlarge the resolvable operator algebra: `N` broadcast copies of the
  partition POVM `{P₀,P₁}` still generate the dim-2 (2-outcome) abelian algebra, for `N=1…100`.
- **F1.2** (decisive, sound half) Redundant partition-records **cannot** distinguish two orthogonal
  **within-doublet** states — both give `(p₀,p₁)=(0,1)` for any redundancy. The within-block **state**
  is genuinely unrecorded.
- **F1.3 / F1.4** (decisive kill) But the block **DIMENSION** (`rank P₁ = 2`) is a **structural**
  attribute of the projector, fixed from **one** copy (`Tr P₁ = 2`), copy-count-independent. The
  Born/dimension weighting (`1:2 → r=1`) is therefore **built from projector ranks the partition record
  already holds**. "Partition-only ⇒ must block-count" is **false**: the record that knows the partition
  also knows the block dimensions, hence can equally apply Born (`r=1`).
- **F1.5 / F1.6** (steelman granted, then killed) Grant the mechanism's strongest premise — a *single
  bare outcome label* `('singlet'/'doublet')` carries no rank (F1.5, conceded). **This is exactly where
  quantum Darwinism bites.** Objective records are maximally redundant; the Haar-averaged outcome
  **frequencies** over an unbiased probe ensemble reconstruct the Born weight `Tr P_k/d`, whose only
  state-independent content is the **dimension fraction**. F1.6 verifies numerically: the reconstructed
  doublet:singlet frequency ratio `= 2.01 ≈ 2 = Tr P₁:Tr P₀` — **the dimension, recovered from labels
  alone via redundancy.** So redundancy reconstructs precisely the dimension the steelman tried to
  withhold.

**This is the same wall that broke the minimum-information argument.** The minimum-info route died
because objective records are maximally redundant (Zurek), not minimal; the cut route dies for the
identical reason — what the redundant environment objectively holds (the partition **and**, via Born
frequencies, the block dimensions) is **enough to apply Born → `r=1`**. The cut does not privilege
block-counting.

### Front 2 — dimension-vs-state: the cut does NOT force block-counting
- **F2.1** (sound) The within-block **state** is unrecorded: a within-doublet rotation commutes with
  `{P₀,P₁}`; the record is blind to it. This half of the cut is correct.
- **F2.2** But the block **DIMENSION** (`rank=2`) is **invariant** under within-block unitaries — it is
  structural data **not** contained in the within-block state.
- **F2.3** (decisive) The Born measure is a function of **dimensions only** (`Tr P₀:Tr P₁`), which F2.2
  puts on the **record's side of the cut**. Resolving the within-block **state** (genuinely quantum,
  unrecorded) is **distinct from** knowing the block's **dimension** (a fixed structural number the
  record has). So dimension-counting (`r=1`) is available and the cut does **not** force block-counting.

### Front 3 — real-vs-complex slot: **RENAMES-THE-SLOT** (does not resolve it)
- **F3.1** The doublet is one `ℂ`-irrep: `dim_ℂ=1` (count once → `r=1/2`) **and** `dim_ℝ=2` (count
  dimension → `r=1`) — both true of the same block. This is the unforced real-vs-complex slot the prior
  Q1 panel found, and restriction-of-scalars makes `det_ℝ` equally canonical.
- **F3.2** (decisive) The cut's "doublet" **outcome is the same operator** whether the block is read as
  one `ℂ`-unit or two `ℝ`-dims — the cut carries **no scalar-field tag**, so it cannot resolve the slot.
- **F3.3** Restriction-of-scalars: the `ℂ`-doublet carries a **faithful real 2×2 rep** (rotation by
  `2π/3`), so `det_ℝ` (`r=1`) is well-defined on the same block. The cut does not escape the
  `det_ℝ/det_ℂ` slot it tries to adjudicate; it **renames** it in records language.

### Front 4 — overreach: the charged-lepton-only restriction is EXTERNAL / post-hoc
- **F4.1** Observed sectors do **not** all sit at `r=1/2` (charged leptons ≈ `1/2`; up-type, down-type
  ≠ `1/2`). A universal "classical mass record → `r=1/2`" is falsified.
- **F4.2** The **generation-block** structure `(1+2)` is identical for every fermion sector (same `C₃`
  triplet). The offered distinguisher (charged leptons are color singlets, quarks are confined color
  triplets) acts on a **different** factor (color), not on the generation partition that sets `r`; it
  does not change the generation block dimensions.
- **F4.3** (decisive) The "only charged leptons" restriction is therefore **external** to the cut
  mechanism — the cut is sector-blind on generations. The multi-lane escape is **post-hoc** with respect
  to the mechanism, not principled by it. (Sector selection may be principled by *other* physics, but it
  is **not** delivered by the cut argument, which would otherwise predict `r=1/2` universally.)

## The two crucial findings

1. **Sound or repackaged? → REPACKAGED-BROKEN-ARGUMENT.** The measure-from-the-cut argument is **not** a
   sound new forcing mechanism. Its load-bearing premise — "the record sees only the partition, never
   the within-block dimension" — is **false**: the block dimensions are single-copy structural facts
   (F1.3, F2.2) on the record's side of the cut, **and** redundant records reconstruct them from labels
   alone via Born frequencies (F1.6). That is the **identical** wall (Darwinian maximal redundancy) that
   decisively broke the prior minimum-information argument. Born/dimension (`r=1`) is **not excluded** by
   the cut.
2. **Resolves or renames the slot? → RENAMES-THE-SLOT.** The cut's "doublet" outcome is operator-agnostic
   between one-`ℂ`-unit (`r=1/2`) and two-`ℝ`-dims (`r=1`) (F3.2), and `det_ℝ` stays canonical via
   restriction-of-scalars (F3.3). The cut carries **no** scalar-field tag to pick `det_ℂ` over `det_ℝ`.
   It **renames** the real-vs-complex / dimension slot in records language; it does **not** resolve it.

## Net (frame-consistent)

`r=1/2` is **not** the record-**forced** measure. It remains a **distinguished, STABLE SETTING** — the
block-count / equal-power-per-block / 2-sector-equipartition point — and `r=1` the Born/dimension
setting. **Both** are reachable from the partition + dimension data on the record's side of the cut; the
cut **does not adjudicate** between them. This is exactly the unforced `det_ℂ`-vs-`det_ℝ` convention the
campaign already names as the open input (`AC_φλ`, value half) — now shown to be **untouched** by the
measure-from-the-cut proposal. We did not force `r=1/2` and did not exclude it.

**Honest verdict: REPACKAGED-BROKEN-ARGUMENT (front 1) + RENAMES-THE-SLOT (front 3).**

## What this does NOT claim
- It does **not** claim `r=1/2` is wrong, excluded, or unstable — `r=1/2` is reaffirmed as a distinguished stable setting on the dial.
- It does **not** claim the Born/dimension `r=1` reading is the physical one; it claims only that the cut leaves it reachable, so the cut does not force `r=1/2`.
- It does **not** close, reopen, or re-tier any audit row; it is a soundness diagnosis of one proposed mechanism.
- It does **not** approve any import (no Darwinism axiom, no measure axiom is adopted; quantum Darwinism is used only as the standard physics fact that breaks the "partition-only" premise, exactly as it broke the minimum-info premise).

## Provenance (verified 2026-06-04)
- All facts are concrete linear algebra on the `Z₃`-circulant 2-block carrier; nothing is hard-coded to a target `r`. The Darwinism reconstruction (F1.6) is a Haar-average over 2×10⁵ probe states. Runner 27/27 PASS.
- Consistent with — and sharpening — the campaign's standing that the Born/dimension measure gives `r=1` and `r=1/2` is the separate block-counting input:
  [`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md) (GAP B),
  [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md) (AC, value-half),
  [`KOIDE_FINITE_BETA_WEIGHT_IS_THE_PARTITION_BIT_NOTE_2026-06-02.md`](KOIDE_FINITE_BETA_WEIGHT_IS_THE_PARTITION_BIT_NOTE_2026-06-02.md) (same weight-ratio choice).
- Retained support for the underlying weight-freedom: [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md) (`retained_no_go` — singlet:doublet ratio free).
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
