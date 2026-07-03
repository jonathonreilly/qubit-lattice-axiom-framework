# Koide r-Polarization Gate Sharpening: the Record K/CPT-Orbit Quotient Is the Complex-Slot Quotient

**Date:** 2026-06-09
**Claim type:** open_gate
**Type:** open_gate sharpening + two narrow computed results (dichotomy completeness; orbit-quotient entailment)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_r_polarization_orbit_quotient_2026_06_09.py`](../scripts/frontier_koide_r_polarization_orbit_quotient_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_r_polarization_orbit_quotient_2026_06_09.txt`](../logs/runner-cache/frontier_koide_r_polarization_orbit_quotient_2026_06_09.txt)
(SCORECARD: PASS=23, FAIL=0)

> **Not claimed:** a derivation of `r = 1/2`, a polarization-selector closure, or
> any mass prediction. The landed fork's open gate stays open. **Claimed:** the
> gate is *sharpened* on three computed fronts — the polarization dichotomy is
> proven **complete**; the 2026-06-05 Record refinement's orbit quotient is
> exhibited as **identical to the complex-slot quotient** (the fork note's named
> positive route), entailing conjugation-invariance of the doublet record readout
> and excluding phase-resolved record readouts; and the residual selector is pinned to
> **exactly one** existing atom (the modulus/(M) degree question), unifying the
> Koide-r gate with it.

---

## Role and non-re-walk discipline

The landed fork note
([`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md))
records the runner-verified four-cell mechanism on the generation algebra
`R[Z₃] = R ⊕ C`: the Koide fork `r ∈ {1, 1/2}` (`Q = (1+2r)/3 ∈ {1, 2/3}`) is
decided by the **polarization** (real: doublet = 2 real slots → `r = 1`;
holomorphic: 1 complex slot → `r = 1/2`), not by statistics. It names two open
positive routes: *derive a native polarization selector*, or *show the readout
functional factors through the doublet complex-slot quotient*.

This note attacks the second route with an ingredient that **postdates every
prior Koide attempt**: the 2026-06-05 Record-axiom refinement, which reads the
realized outcome as the **K/CPT orbit of the realized central sector**. Refuted
routes are not re-walked: no "chiral → r=1/2" (#2624), no Dyson/Pfaffian reading
of `det_C` (#3138 — the landed table is **cross-checked cell-by-cell as a hard
runner gate**), no "charge forecloses r=1/2". The honest dynamical tension is
stated, not hidden: the supplied CW/fluctuation-modulus route favors the *real*
cell (`r = 1`), and neither readout is selected by this note.

## Result 1 (computed): the polarization dichotomy is complete

On the doublet block, the `Z₃`-commutant is exactly `span{1, J}` (computed
symbolically), and the complex structures it contains are exactly `{+J, -J}`
(the solutions of `(x + yJ)² = -1` are `x=0, y=±1`; computed). The canonical
conjugation `K` exchanges `+J ↔ -J` (computed: `K(e₁) = e₂`), so the two
holomorphic cells are **one K-orbit**; a quaternionic polarization is
dimensionally impossible (`dim_R = 2 < 4`). Hence the fork
`{real, holomorphic}` is **exhaustive**: `r ∈ {1, 1/2}` and `Q ∈ {1, 2/3}` are
the only cells — a genuine dichotomy, not two options among many. This upgrades
the fork from "four tested cells" to a **classification**.

## Result 2 (computed, narrow): the orbit quotient *is* the complex-slot quotient

With the canonical conjugation on `R[Z₃]` (`K(e₁) = e₂`, computed), the
central-sector orbit partition under the 2026-06-05 Record wording is

```text
    { e₀ }   and   { e₁ , e₂ }
```

— which **coincides** with the `R`-block / `C`-block partition of
`R[Z₃] = R ⊕ C`. The orbit quotient is therefore *literally* the doublet
complex-slot quotient named by the fork note. Two precise consequences:

- **Entailment (new):** any record-readout is a function on orbits, so it cannot
  distinguish `e₁` from `e₂`: **phase-resolved record readouts are excluded**,
  and conjugation-invariance `I(b) = I(\bar b)` of the doublet record readout is
  **entailed** by orbit granularity. (Narrow scope: this is
  conjugation-invariance of the *sector* readout, **not** full P2/modulus; the
  earlier "P2 not Record-derivable" result concerned full modulus and is
  untouched.)
- **Honest boundary (computed):** orbit granularity does **not** select the slot
  *degree* — both `|b|` (degree 1, the holomorphic-magnitude reading) and
  `|b|²` (degree 2, the real reading) factor through the orbit quotient. The
  residual selector is therefore **exactly** the existing modulus/(M) degree
  atom.

## Net: the gate, before and after

```text
before:  polarization gate = an unstructured binary {real, holomorphic},
         separate from the P2/modulus question; phase-resolved record readouts
         not excluded; completeness untested.

after:   (i)   the binary is PROVEN complete (r in {1, 1/2} exhaustive);
         (ii)  the readout provably factors through the orbit quotient
               = the complex-slot quotient (fork note's route 2, exhibited);
         (iii) phase-resolved record readouts EXCLUDED (entailed by Record-orbit);
         (iv)  the residual is ONE atom: the slot-degree/(M)-modulus choice —
               the Koide-r gate and the P2/(M) question are UNIFIED.
```

The comparator (labeled, never an input): the empirical charged-lepton Koide
ratio is `Q_PDG = 0.666661`, on the holomorphic cell to `6×10⁻⁶`, while the real
cell `Q = 1` is excluded empirically by ~50%.

## Named next target (sharp, new)

Does orbit granularity constrain the orbit-space **measure class** (the
one-complex-slot weight `π/g` vs the two-real-slot weight `2π/g` — the landed
measure fork re-exhibited in the runner)? That is now the *precise* remaining
question behind Koide-`r`, and it is a candidate for the independence method:
either the measure class is derivable from the Record-orbit structure, or two
consistent models exist and the slot degree is an irreducible structural premise
of the kinetic-isotropy category — owner-decision territory either way.

## What this note does NOT claim

- **Not** a derivation of `r = 1/2`; **not** a selector closure; **not** a mass
  prediction; the gate remains open (sharpened).
- **Not** full P2/modulus from Record (only doublet conjugation-invariance, a
  strictly weaker narrow entailment).
- **No** PDG/fitted input in any derivation step (PDG `Q` appears as a labeled
  comparator only); **no** new axiom, primitive, vocabulary, or class tag.
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): the central idempotents and the canonical `J`; the
  Koide lever `Q = (1+2r)/3`, `r = |b|²/a²` (300 random draws); holomorphic
  Berezin = `det`, Majorana Berezin = Pfaffian, `Pf² = det_R`; the four-cell
  fork **cross-checked verbatim against the landed table**; the `Z₃`-commutant
  and the `{±J}` classification; `K(e₁) = e₂` and the orbit partition; the
  orbit-quotient = block-partition identification; the entailment and the
  honest degree boundary; the measure-weight fork `2π/g` vs `π/g`; the PDG
  comparator arithmetic.
- **Cited:** the landed fork note (mechanism + table);
  `KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`
  (the `Q`-lever); `MINIMAL_AXIOMS_2026-06-05.md` (the K/CPT-orbit Record
  wording); the refuted-route corpus (#2624, #2688, #3138) as non-re-walk
  boundaries; `KOIDE_DELTA_RADIAN_PERIOD_PHYSICAL_NOT_VACUOUS_NARROW_THEOREM_NOTE_2026-06-04.md`
  (the phase admission, context).

## Dependencies

- [KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  — the landed four-cell mechanism this note sharpens; its table is a hard
  cross-check gate in the runner.
- [KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
  — the upstream `Q = (1+2r)/3` lever (re-derived in the runner).
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
  — the Record axiom's K/CPT-orbit outcome wording (the new ingredient; this
  note consumes the wording, adds nothing to it).

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
