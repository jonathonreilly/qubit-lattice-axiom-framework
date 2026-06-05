# Flavor K-Real Instrument Two-Letter Phase Orthogonal

**Date:** 2026-06-02
**Claim type:** open_gate.
**Runner:** `scripts/flavor_kreal_instrument_two_letter_phase_orthogonal_2026_06_02.py`.

This source note records a conditional localization. It does not derive a
measurement instrument from the three baseline axioms and does not promote a
Koide value claim.

## Result

For the generation operator

```text
H = a I + Re(b) S + Im(b) J,
S = C + C^2,
J = i(C - C^2),
```

the runner verifies:

- `S` is K-even, Hermitian, and has spectrum `{2,-1,-1}`;
- `J` is K-odd, Hermitian, and has spectrum `{-sqrt(3),0,sqrt(3)}`;
- `[S,J]=0`;
- `H = aI + bC + conjugate(b) C^2` equals the `S/J` decomposition.

A K-real, conjugation-even instrument cannot record the K-odd `J` direction
without adding structure beyond that instrument. Under that specified
instrument, the record alphabet is the K-even two-sector split: singlet plus
doublet. The Brannen phase then lives in the orthogonal K-odd channel and does
not itself choose the two-sector measure.

## Consequence

This localizes the charged-lepton value residual. The alphabet/phase split
does not select between:

- dimensional pushforward from `I/3`: `(1/3, 2/3) -> r=1`;
- block-count over the two recorded sectors: `(1/2, 1/2) -> r=1/2`.

The remaining question is the measure/reference choice on the two-sector
record partition. This note does not force `r=1/2`.

## Boundaries

- Record additivity does not supply the K-real instrument.
- The K-real instrument does not supply a measure over the two recorded
  sectors.
- The K-odd phase can shape the three mass values while remaining orthogonal
  to the K-even record alphabet.

## Provenance

The runner verifies the spectra, K-parities, commutator, decomposition, entropy
gap `S_vN - H_Shannon = (2/3) log 2`, and the two weight maps directly.
