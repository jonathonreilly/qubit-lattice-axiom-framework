---
claim_id: staggered_dirac_berezin_signed_measure_probe_2026-06-05
claim_type_author_hint: meta
---

# Staggered-Dirac Berezin Signed-Measure Probe

**Date:** 2026-06-05
**Claim type:** meta (probe / route-disambiguation support; no new axiom, no closure, no verdict set)
**Runner:** `scripts/staggered_dirac_berezin_signed_measure_probe_2026_06_05.py` (SCORECARD PASS=31, FAIL=0)
**Cache:** `logs/runner-cache/staggered_dirac_berezin_signed_measure_probe_2026_06_05.txt`
**Status authority:** independent audit lane only. This note sets no `audit_status` /
`effective_status` and approves no primitive, import, or admission. It records a tested
disambiguation of three mechanisms that all travel under the name "det_C / signed".

## What was probed

The probe attacked the charged-lepton `r = 1/2` (Q = 2/3) selector through the
**finite-Grassmann / Berezin fermion-measure** angle on the open staggered-Dirac
realization gate (`staggered_dirac_realization_gate_note_2026-05-03`, open_gate). The
hypothesis under test:

> The Berezin integral gives a determinant. Complex/Dirac fermions → `det(D)` with
> *signed* (complex) eigenvalues → the signed (det_C / Brannen) readout → `r = 1/2`;
> real/Majorana fermions → Pfaffian/real → the unsigned readout → `r = 1`. So the
> `r = 1/2` selection might follow from the *Dirac (complex, signed) nature* of the
> charged-lepton fermion measure.

## Result — three axes, only one fixes `r`, and it is not the measure's determinant nature

The runner separates three things conflated in the hypothesis (each verified exactly):

| Axis | Distinction | Who decides it | Fixes `r`? |
|---|---|---|---|
| **1** | Berezin `det(H)` vs bosonic `(det H)^{-1/2}` | **forced** by Cl(3) faithful complex-irrep dim 2 (retained substep-1 D4) | **no** |
| **2** | signed `λ_k` vs singular `|λ_k|` readout | native operator class Hermitian `H = iD` → **signed side** (retained 2026-05-29) | **no** (presupposes `r = 1/2`) |
| **3** | doublet **counting**: complex 1-slot vs real 2-slot | the open `U(1)_b` / complex-counting import — **NOT** forced | **yes** |

**The load-bearing demonstration (Part 0–1, 5):** the Berezin partition is
`Z_F = ∫ dχ̄ dχ exp(−χ̄ H χ) = det(H)` (verified by direct permutation expansion of
the Berezin top form), and `det(H) = ∏_k λ_k` with the signed real eigenvalues. But the
signed Koide invariant `Q(S) = (3a² + 6|b|²)/(3a)² = (1 + 2r)/3` is a **nonconstant
function of `r`** (runner: `Q = 7/15, 2/3, 5/6, 1` at `r = 1/5, 1/2, 3/4, 1`). So the
determinant/Dirac/signed structure (axes 1+2) yields `Q = 2/3` **only when `r` is already
`1/2`**; it does not select `r`. The value of `r` is set by the coefficient ratio
`|b|/a`, i.e. by **how the measure counts the doublet amplitude** (axis 3), which is a
different question from whether the measure is a determinant.

**The Majorana/Pfaffian branch does not relabel `r` (Part 2):** the real-antisymmetric
(Majorana) single-field integral is the Pfaffian, with `Pf² = det ≥ 0` (sign-square,
democratic). But the C₃ Hermitian mass operator `H = aI + bC + b̄C²` is **not in the
Majorana class** — its diagonal is `a ≠ 0`, so it is not real-antisymmetric — and any
`3×3` real-antisymmetric operator is **singular** (odd dimension ⇒ `det = 0`,
`Pf = 0`), so a literal Majorana 3-generation mass operator cannot even carry three
nonzero masses. Hence "Dirac vs Majorana for the generation operator" is *not* a free
relabel of the same spectrum; it changes the operator class. The genuine det_R↔det_C
question (the fork note) is therefore **not** "Dirac vs Majorana operator" but the
doublet-counting of axis 3.

**Statistics is not the selector (Part 3):** reproducing the four-cell fork of
`koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04`, the Gaussian-vs-Berezin
(det-vs-Pfaffian) *statistics* row is **not** decisive — Majorana-Berezin (a Pfaffian)
lands `r = 1`, Dirac-Berezin (a det) lands `r = 1/2` — while the real-slot-vs-complex-slot
*polarization* column **is** decisive. So "det vs Pfaffian fixes `r`" is **false**;
polarization (complex-counting) does.

## Is the Dirac-nature (complex-counting) derived or imported?

**Imported, and precisely characterized (Part 4).** The natural mechanism that would
make the charged-lepton sector "Dirac/complex" and so activate complex-counting —
*carry electric charge* — **fails at the first arrow**:

- The framework's gauge U(1)s (em, hypercharge, fermion-number) are **generation-blind**:
  they act as scalars `e^{iχ} I` on the generation triplet and **commute with `C`**
  (verified), so `g H g† = H` leaves the doublet coordinate `b` untouched. They cannot
  orient the doublet complex structure. (Same finding as
  `flavor_both_readings_charge_selects_note_2026-05-30`, where the quark sector also
  *refutes* the naive "charged → det_C → 2/3" rule: up/down are charged Dirac fermions
  carrying the very U(1) invoked, yet sit at `Q = 0.849 / 0.731 ≠ 2/3`.)
- A doublet-rephasing `U(1)_b` is **incompatible with `C³ = I`**: a continuous
  `C → e^{iα} C` forces `(e^{iα}C)³ = e^{3iα} I = I`, i.e. `α ∈ {0, 2π/3, 4π/3}` — the
  discrete `C₃` only (verified). The continuous `U(1)_b` is not merely absent from the
  retained inventory; it is **incompatible** with the retained order-3 relation. This
  matches the hardened first-principles derivation
  `generation-doublet-measure-detC-vs-detR-2026-05-29` (verdict: UNDETERMINED; discrete
  default det_R → Q = 1).

So the complex-counting that fixes `r = 1/2` is **not** supplied by the staggered/Berezin
construction, nor by the Dirac (charged) nature via any framework gauge structure.

## Honest verdict: RELOCATES-TO-DIRAC-NATURE-IMPORT (sharpened to the doublet complex-counting / `U(1)_b`)

The chain "signed readout → `r = 1/2`" **does not hold** as the probe framed it: the
signed/determinant readout (axes 1+2) gives `Q = (1+2r)/3` for *every* `r` and is `2/3`
only once `r = 1/2` is supplied by axis 3. The `r = 1/2` selection lives **entirely** on
the doublet complex-counting axis, which is a genuine import — and the probe **sharpens**
the prior "Dirac-vs-Majorana sector property" framing: at dimension 3 the
Dirac-vs-Majorana *operator-class* distinction is not even the operative fork (Majorana
generation op is singular), and within the determinant class the operative selector is
the complex-vs-real *counting* of the doublet, equivalently a `U(1)_b` that breaks
`C³ = I`. The signed-readout class (axis 2) is real and native — it correctly places the
framework on the side compatible with `Q = 2/3` — but it is downstream of, not a
substitute for, the complex-counting that sets the value.

This is **not** SIGNED-MEASURE-DERIVES-R-HALF: the Dirac-nature that would do so is not
derived. The Berezin/Dirac measure being a determinant (axis 1, forced) and the native
readout being signed (axis 2, native) are both genuine and on the right side, but neither
fixes `r`.

## What this opens (next paths)

The probe does not close any route; it isolates the live one. The single sharp search it
points to (inheriting the falsification constraint of the charge-selection note) is a
**derived continuous horizontal/flavor `U(1)` that rephases the doublet `b → e^{iθ}b`
relative to the singlet `a` and is reconcilable with `C³ = I`** — e.g. acting on the
singlet⊕doublet idempotent decomposition rather than on `C` itself — which would supply
the complex-counting internally and would have to reproduce the *entire* sector ordering
(leptons `2/3` < down `0.73` < up `0.85`), not just the lepton point. Two further open
handles the determinant framing leaves untouched: (a) a record/persistence
distinguishable-label counting principle that prefers block-count over Hilbert
multiplicity (the `flavor_record_readout_form_not_weight_2026-06-02` residual); (b) the
separate-tensor-factor chirality route (Connes–Lott), which currently imports a non-native
L/R factor and does not force `r = 1/2`.

## What this does NOT claim

- Does **not** derive `r = 1/2` or `Q = 2/3`; does not predict `m_e, m_μ, m_τ`.
- Does **not** adopt the holomorphic polarization, a `U(1)_b`, or any complex-counting.
- Does **not** assert `Q = 2/3` is impossible to derive natively; promotion routes remain
  open.
- Does **not** consume any PDG value, fitted selector, literature comparator, or admitted
  unit convention as a proof input (`2/3`, `1`, and the quark Q-values are
  comparators/context only).
- Does **not** edit any generated ledger, queue, or publication-status file, and does not
  close, retire, or exhaust any search.

## Cited context (plain-text, non-load-bearing reader pointers)

- `koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`
  (retained) — axis 2: signed vs singular readout; `Q(S) = (1+2r)/3`, `2/3` at `r = 1/2`.
- `spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10` (retained_bounded)
  — axis 1: `Z_F = det(M)`; real-antisym `det = Pf² ≥ 0`.
- `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16`
  (retained_bounded) — Cl(3) dim-2 forces Grassmann/determinant over bosonic (D4).
- `koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04` (unaudited) — the four-cell
  polarization×statistics fork this note reproduces and sharpens.
- `flavor_both_readings_charge_selects_note_2026-05-30` — charge-selection fails;
  generation-blind gauge U(1)s; quark sector refutes the naive rule.
- `flavor_record_readout_form_not_weight_2026-06-02` (open_gate) — the dimension-count
  (1:2) vs sector-count (1:1) residual.
- `staggered_dirac_realization_gate_note_2026-05-03` (open_gate) — the gate parent; this
  probe is a downstream disambiguation, not an upstream dependency.
