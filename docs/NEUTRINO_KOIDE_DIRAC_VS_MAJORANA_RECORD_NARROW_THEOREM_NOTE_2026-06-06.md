# Neutrinos and Koide: Q_ν=2/3 Iff Dirac (Direct Record); Majorana/Seesaw Breaks It — and the Data Confirms Q_ν<2/3

**Date:** 2026-06-06
**Claim type:** bounded_theorem (recordable-lens prediction + data comparator)
**Status:** review-loop source proposal. Adds no axiom, no fitted input, no audit
verdict. Oscillation splittings appear **only as a comparator**, never as a
derivation input.
**Primary runner:**
[`scripts/frontier_neutrino_koide_dirac_vs_majorana_record_2026_06_06.py`](../scripts/frontier_neutrino_koide_dirac_vs_majorana_record_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_neutrino_koide_dirac_vs_majorana_record_2026_06_06.txt`](../logs/runner-cache/frontier_neutrino_koide_dirac_vs_majorana_record_2026_06_06.txt)

---

## Role

Third application of the recordable-outcome lens to the mass sectors, completing
the fermion triptych:

| sector | record status | Koide |
|---|---|---|
| charged leptons | colorless, recorded free → **pole masses** | **Q=2/3** (#2910/#2917/#2923) |
| quarks | **confined**, no free record, no pole mass | no clean Koide (#2937) |
| **neutrinos** | colorless (**not** confined) → recordable | **this note** |

Neutrinos are colorless, so the confinement exclusion of #2937 does **not** apply
— they *can* be recorded as free states. The question is whether their record is
a **directly-recorded Dirac √mass** (like the charged leptons) or a **composite**.

## The lens prediction

```text
   Q_ν = 2/3   <=>   neutrinos are DIRAC with a directly-recorded √mass
                     (the same single-summand C₃ record as the charged leptons).
```

If neutrinos are **Majorana / seesaw**, the light mass is the composite
`m_ν = m_D M_R^{-1} m_D^T` (diagonally `m_ν = m_D²/M_R`): the light mass is **not**
a directly-recorded Dirac √mass, and the super-heavy Majorana scale `M_R` is
decoupled / unrecorded. A nonlinear composite does **not** preserve the Koide
constraint, so `Q_ν ≠ 2/3` generically.

## Demonstration (runner SCORECARD 14/14 PASS)

**(i) Seesaw breaks Koide.** Starting from a Dirac set whose √masses satisfy Koide
(`Q=2/3`), the seesaw light masses `m_D²/M_R` give `Q_ν ≠ 2/3` for **every** `M_R`
structure tested:

| `M_R` | `Q_ν` |
|---|---|
| degenerate (1,1,1) | 0.894 |
| hierarchical (1,10,100) | 0.730 |
| inverse (100,10,1) | 0.964 |
| generic (3,1,7) | 0.765 |

**(ii) The data already shows it.** With the measured oscillation splittings
`Δm²₂₁ = 7.42×10⁻⁵ eV²`, `Δm²₃₁ = 2.51×10⁻³ eV²` (comparator), and the
cosmological bound `Σm_ν < 0.12 eV`, the neutrino Koide ratio lies **strictly
below 2/3 for both hierarchies**:

```text
   Normal hierarchy:   Q_ν ∈ [0.34, 0.586]   (max at m₁ = 0)
   Inverted hierarchy: Q_ν ∈ [0.36, 0.50]
```

So neutrinos do **not** obey the charged-lepton Koide (`Q=2/3`). This is
**consistent with** the lens's Majorana/seesaw expectation and **inconsistent
with** the simplest "neutrinos are Dirac with the charged-lepton C₃ structure →
`Q=2/3`" hypothesis.

## Sharpened: the bound `Q_ν < 2/3` is guaranteed and robust

The data statement above is not merely a scan — it is a **guaranteed, robust
bound** (runner Block 4b):

1. **Monotonicity ⟹ the maximum is at `m_lightest = 0`.** `Q_ν(NH)` decreases
   monotonically in the lightest mass (verified over the full range), so its
   supremum over **all** absolute scales is attained at `m_lightest = 0`:
   `Q_ν^max = (√Δm²₂₁ + √Δm²₃₁)/(Δm²₂₁^{1/4} + Δm²₃₁^{1/4})²`. The bound therefore
   holds for **every** absolute scale, not just the sampled range.
2. **3σ-robust.** Maximizing the hierarchy over the global-fit 3σ boxes
   (`Δm²₂₁ ∈ [6.8, 8.0]×10⁻⁵`, `Δm²₃₁ ∈ [2.40, 2.60]×10⁻³ eV²`) gives
   `Q_ν^max(NH) = 0.591` and `Q_ν^max(IH) = 0.500` — both still well below
   `2/3 = 0.667`. The charged-lepton Koide is excluded for neutrinos at a robust
   margin.
3. **The Koide deficit as a discriminant.** Define
   `Δ_K := 2/3 − Q_ν^max ≳ 0.076` (3σ). This nonzero, robust deficit *is* the
   quantitative Dirac/Majorana discriminant: a directly-recorded Dirac neutrino
   sharing the charged-lepton structure would have `Δ_K = 0` (`Q_ν = 2/3`); the
   composite Majorana/seesaw mass forces `Δ_K > 0`, and the measured splittings
   already require `Δ_K ≳ 0.08`.

So the charged-lepton Koide is not approximately, but **robustly (≳0.08 in Q,
3σ)** forbidden for neutrinos — independent of the unknown absolute mass scale.

## The falsifiable distinction

- **Charged leptons:** `Q = 2/3` (recorded Dirac √mass).
- **Neutrinos:** `Q < 2/3` (composite / not the charged-lepton record).

`Q_ν = 2/3` would require neutrinos to be Dirac *and* share the charged-lepton C₃
record structure — **disfavored** by the current data. **Neutrinoless
double-beta decay** (tests Majorana) and **absolute-mass** measurements (KATRIN,
cosmology) sharpen the test directly.

## Honest scope

- Qualitative lens prediction + data comparator — **not** a neutrino-mass
  derivation.
- "Dirac ⟹ Q=2/3" assumes the neutrino Dirac sector shares the charged-lepton C₃
  record structure; the data showing `Q_ν < 2/3` means neutrinos do **not** share
  it — consistent with Majorana/seesaw **or** a different Dirac structure.
- Oscillation `Δm²` and `Σm_ν` are **comparators only**, never derivation inputs.
- No axiom added.

## Reprove-and-cite ledger

- **Reproven here** (runner): `Q=2/3` for the charged-lepton-like Dirac √mass; the
  seesaw `m_D²/M_R` breaking `Q_ν ≠ 2/3` for all tested `M_R`; the data ranges
  `Q_ν ∈ [0.34, 0.586]` (NH), `[0.36, 0.50]` (IH) under `Σm_ν < 0.12 eV`.
- **Cited**: the directly-recorded single-summand structure (#2910/#2917/#2923);
  the confinement exclusion for quarks (#2937); the Record axiom realized-outcome
  premise (`MINIMAL_AXIOMS_2026-06-05`); the seesaw mechanism and the oscillation
  `Δm²` / `Σm_ν` bounds (comparators).

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. It does not promote any note or change any
audited claim scope.

- [KOIDE_HOLDS_IFF_RECORDED_FREE_POLE_MASS_CONFINEMENT_NARROW_THEOREM_NOTE_2026-06-06.md](KOIDE_HOLDS_IFF_RECORDED_FREE_POLE_MASS_CONFINEMENT_NARROW_THEOREM_NOTE_2026-06-06.md)
- [KOIDE_R_HALF_RECORD_NATIVE_READOUT_DOUBLET_COUNTED_ONCE_NARROW_THEOREM_NOTE_2026-06-06.md](KOIDE_R_HALF_RECORD_NATIVE_READOUT_DOUBLET_COUNTED_ONCE_NARROW_THEOREM_NOTE_2026-06-06.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
