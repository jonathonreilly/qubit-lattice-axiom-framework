# Charged-lepton Doublet Splitting (δ≠0) is a Recordable Outcome — the Arrow

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. It writes no audit verdict and supplies no direct
effective-status change.
**Primary runner:**
[`scripts/frontier_koide_delta_split_records_arrow_2026_06_06.py`](../scripts/frontier_koide_delta_split_records_arrow_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_delta_split_records_arrow_2026_06_06.txt`](../logs/runner-cache/frontier_koide_delta_split_records_arrow_2026_06_06.txt)

---

## Role

Companion to
[KOIDE_R_HALF_RECORD_NATIVE_READOUT_DOUBLET_COUNTED_ONCE_NARROW_THEOREM_NOTE_2026-06-06.md](KOIDE_R_HALF_RECORD_NATIVE_READOUT_DOUBLET_COUNTED_ONCE_NARROW_THEOREM_NOTE_2026-06-06.md),
which showed the **count** `r = 1/2` (`Q = 2/3`) is the import-free record-native
readout (the doublet counted once). This note carries the same
**recordable-outcome** lens to the *other* residual of the charged-lepton mass
pattern: the within-doublet phase **δ** that splits the K/CPT doublet into two
distinct masses (μ ≠ τ), giving **three distinct charged leptons** rather than a
degenerate pair.

Framework logic: **probability (qubit) → record → durable state.** `δ ≠ 0` does
not need to be *selected*; it needs to be a **recordable** outcome — and it is
the recorded value of the **K-odd channel**, which is exactly an **arrow**.

## Setup (on-main, cited)

For the C₃ generation carrier `H = a I + b C + b̄ C²` (`b = |b| e^{iδ}`), with
`K`/CPT = complex conjugation, the operator splits into orthogonal channels
([KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31.md](KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31.md),
[FLAVOR_KREAL_INSTRUMENT_TWO_LETTER_PHASE_ORTHOGONAL_2026-06-02.md](FLAVOR_KREAL_INSTRUMENT_TWO_LETTER_PHASE_ORTHOGONAL_2026-06-02.md)):

```text
    H = a I + |b| cos δ · S  +  |b| sin δ · J
        S = C + C²      (K-EVEN record channel; S-pointer spectrum {-1,-1,+2}, two-outcome)
        J = i(C - C²)   (K-ODD phase channel; Hermitian, J ⟂ S, spectrum {0, ±√3})
```

The K-even record sees the doublet as **one degenerate letter** (the source of the
`r = 1/2` count). The K-odd channel `J` **resolves** the doublet.

## The result (runner SCORECARD 17/17 PASS)

1. **The splitting is exactly the K-odd channel.** The doublet split is
   `λ₁ − λ₂ = −2√3 |b| sin δ`, proportional to the `J`-coefficient `|b| sin δ`.
   At `δ = 0` the doublet is **degenerate** (only two distinct masses); `δ ≠ 0`
   resolves it into three.
2. **A nonzero K-odd record is an arrow.** `J` is Hermitian and **K-odd**
   (`conj(J) = −J`), i.e. **T-odd** under the CPT conjugation. In any K-even /
   T-symmetric (no-arrow) record state `ρ_even = a₀ I + s₀ S`, the K-odd channel
   has **zero** record: `Tr(ρ_even J) = 0` (verified). So a **nonzero recorded
   ⟨J⟩** (`δ ≠ 0`) **requires T-symmetry breaking — a recorded time orientation,
   i.e. an arrow.**
3. **The arrow is recorded.** Record formation is irreversible / time-oriented
   ([ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)).
   Hence `δ ≠ 0` — the three-distinct-mass splitting — is a **recordable outcome**
   (the arrow being recorded), **not** a separate Koide admission.
4. **Consistency with the count.** `Q = 1/3 + (2/3) r` is **independent of δ**
   (`dQ/dδ = 0`, verified). So recording the K-odd arrow (`δ ≠ 0`) produces the
   three distinct masses **without disturbing** the record-native count
   `r = 1/2` (`Q = 2/3`). The two pieces compose cleanly:

   > **three distinct charged-lepton masses = (count `r = 1/2`, record-native) +
   > (splitting `δ ≠ 0`, the arrow).**

## Reframe of the FLAVOR_KREAL no-go (teeth)

`FLAVOR_KREAL_INSTRUMENT_TWO_LETTER_PHASE_ORTHOGONAL` is a no-go: the baseline
does **not** derive a "K-real instrument" that forces the readout onto the K-even
alphabet (`δ = 0`). Under the recordable lens that is the **wrong target**: we do
**not** need to force K-reality. The K-odd channel `J` is **recordable**, and a
nonzero record of it **is** the arrow — already a recorded structure. **Teeth:**
*without* the arrow (K-even-only record) `δ = 0`, the doublet is degenerate, and
there are only **two** distinct charged-lepton masses (μ = τ) — contradicting
observation. The arrow is **required** for three distinct charged leptons; it is
not an optional selector.

## Honest residual (named, not closed)

- **The value `δ = 2/9` is a separate residual.** Recording the arrow gives
  `δ ≠ 0` (an orientation), not the specific magnitude `2/9` (the topological /
  radian-period quantity, tracked elsewhere). This note fixes the **existence**
  of the splitting, not its value.
- **The arrow is a universal-floor admission.** `δ ≠ 0` collapses into the arrow
  (the past hypothesis / low-entropy boundary), which **all** of physics admits —
  it is **not** a framework-specific Koide input. This is a reduction of
  framework-specific content into the universal arrow, not a closure of the arrow.
- **The carrier is supplied** (the hw=1 C₃ corner / three generations; the
  recurring chirality gate), as in the on-main cluster.

## Net for the charged-lepton mass pattern

With the companion `r = 1/2` note, the qualitative charged-lepton structure is
now recordable-outcome native: the **count** `Q = 2/3` is the record-native
readout (doublet counted once), and the **existence of three distinct masses**
(`δ ≠ 0`) is the arrow being recorded. What remains is the **quantitative value**
`δ = 2/9`, the universal arrow itself, and the supplied carrier — not a
framework-specific "Koide selector."

## Reprove-and-cite ledger

- **Reproven here** (exact sympy): the `H = aI + |b|cosδ·S + |b|sinδ·J`
  decomposition (entry-wise); `S` K-even, `J` K-odd + Hermitian + `J ⟂ S`; the
  split `−2√3|b|sinδ` (degenerate at `δ=0`); `S` spectrum `{-1,-1,2}`, `J`
  spectrum `{0,±√3}`; `Tr(ρ_even J) = 0`; `dQ/dδ = 0`.
- **Cited** (reused): the S/J channel decomposition and the two-outcome S-pointer
  (`koide_pointer_record_degeneracy_d3`, `flavor_kreal_instrument_two_letter_phase_orthogonal`);
  `Q = 1/3+(2/3)r` (`koide_circulant_value_derivation`); the recorded arrow
  (`arrow_from_record_formation_past_hypothesis_residual`); the count `r=1/2`
  (`koide_r_half_record_native_readout`, companion).

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. It does not promote this note or change any
audited claim scope.

- [KOIDE_R_HALF_RECORD_NATIVE_READOUT_DOUBLET_COUNTED_ONCE_NARROW_THEOREM_NOTE_2026-06-06.md](KOIDE_R_HALF_RECORD_NATIVE_READOUT_DOUBLET_COUNTED_ONCE_NARROW_THEOREM_NOTE_2026-06-06.md)
- [KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31.md](KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31.md)
- [FLAVOR_KREAL_INSTRUMENT_TWO_LETTER_PHASE_ORTHOGONAL_2026-06-02.md](FLAVOR_KREAL_INSTRUMENT_TWO_LETTER_PHASE_ORTHOGONAL_2026-06-02.md)
- [ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)
- [KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md](KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md)
