# Koide (Q=2/3) Holds Iff the Fermion is Recorded as a Free Durable State (a Pole Mass)

**Date:** 2026-06-06
**Claim type:** bounded_theorem (qualitative recordable-lens explanation + comparator)
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. PDG masses appear **only as a comparator** confirming
the prediction, never as a derivation input.
**Primary runner:**
[`scripts/frontier_koide_holds_iff_recorded_free_2026_06_06.py`](../scripts/frontier_koide_holds_iff_recorded_free_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_holds_iff_recorded_free_2026_06_06.txt`](../logs/runner-cache/frontier_koide_holds_iff_recorded_free_2026_06_06.txt)

---

## Role

Carries the recordable-outcome lens from the charged-lepton mass pattern to the
**quark/lepton contrast**: *why do the charged leptons satisfy Koide (Q=2/3, to
~10⁻⁵) while the quarks do not?* This is a long-standing puzzle; the lens supplies
a clean, physical answer that also **grounds the known pole-vs-running obstacle**.

## The frame

The recordable-lens results on the charged-lepton value
([KOIDE_R_HALF_RECORD_NATIVE_READOUT_...](KOIDE_R_HALF_RECORD_NATIVE_READOUT_DOUBLET_COUNTED_ONCE_NARROW_THEOREM_NOTE_2026-06-06.md) #2910,
[KOIDE_DELTA_SPLIT_IS_RECORDABLE_ARROW_...](KOIDE_DELTA_SPLIT_IS_RECORDABLE_ARROW_NARROW_THEOREM_NOTE_2026-06-06.md) #2917,
[KOIDE_2OVER9_RECORD_LOCAL_FIXED_POINT_READOUT_...](KOIDE_2OVER9_RECORD_LOCAL_FIXED_POINT_READOUT_NARROW_THEOREM_NOTE_2026-06-06.md) #2923)
all rest on one premise from the Record axiom
([MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)): the observable is
the **realized, durable** outcome. The realized, durable mass of a free fermion is
its **pole mass** — a scheme-independent recorded quantity. A running / Lagrangian
mass, by contrast, is a scheme-dependent **parameter**, not a recorded outcome.

## The prediction (qualitative, from the lens)

```text
   Koide (Q=2/3)  <=>  the fermion is RECORDED as a free durable state
                  <=>  it has a physical pole mass
                  <=>  it is colorless (not confined).
```

- **Charged leptons** are colorless and are recorded as free asymptotic states.
  Their **pole masses** are realized records, so the single-summand C₃ structure
  (#2910/#2917/#2923) applies and **Q_lepton = 2/3**.
- **Quarks** are **confined** by the framework's SU(3) gauge sector — the same
  confining SU(3) Wilson theory whose plaquette `⟨P⟩` at `β=6` the campaign
  computes. A quark is **never realized as a free durable record**; it has **no
  pole mass**. Its "mass" is a running / scheme-dependent Lagrangian parameter —
  **not a recorded outcome**. So the lens's single-summand `Q=2/3` does not apply,
  and any "apparent" quark Koide ratio is coordinate/scheme-dependent.

## Comparator + teeth (runner SCORECARD 16/16 PASS)

With `Q := (Σ m)/(Σ √m)²` and PDG masses (comparator only):

| sector | masses | `Q` | vs 2/3 |
|---|---|---|---|
| charged leptons | **pole** (e, μ, τ) | **0.666661** | `|Q-2/3| ≈ 6×10⁻⁶` (FIXED, scheme-independent) |
| up-type quarks | running (u, c, t) | 0.849 | off by 0.18 |
| down-type quarks | running (d, s, b) | 0.731 | off by 0.06 |

**Teeth:** `Q_lepton` (pole) is essentially fixed (perturbation spread `~2×10⁻⁴`),
while `Q_quark` **drifts with scheme/scale** (running the light quarks by a factor
0.8–1.3 moves `Q_down` over 0.71–0.75, spread `~0.05`) — confirming the quark
"masses" are scheme-dependent parameters, not fixed recorded outcomes, exactly as
the lens requires.

## What this is

A clean recordable-lens **explanation** of the lepton/quark Koide contrast:
Koide is a statement about **recorded (pole) masses**, which only colorless,
unconfined fermions have. This **grounds the known pole-vs-running obstacle to
quark Koide** (Koide 2018; Sumino; Rivero–Gsponer — comparator) in the recordable
lens + the framework's SU(3) confinement: confinement removes the free quark
record, hence the pole mass, hence the clean Koide relation.

## Honest scope

- **Qualitative** explanation of the contrast — **not** a quantitative derivation
  of quark masses (the lens *predicts the absence* of a clean quark Koide, which
  matches; it does not compute the quark spectrum).
- **Confinement** of the framework's SU(3) sector is cited (the gauge sector /
  `⟨P⟩` campaign); "confined ⟹ no pole mass" is standard QCD (cited).
- **Neutrinos** are a **separate case**: colorless, but their mass mechanism
  (Majorana / seesaw) and tiny/uncertain values are not addressed here; the lens
  does not by itself predict a clean neutrino Koide.
- No axiom added; **no PDG value is load-bearing** on the lens argument (the
  argument is the lens + confinement; the Q values are the comparator).

## Reprove-and-cite ledger

- **Reproven here** (runner): `Q_lepton(pole) = 2/3` to `~10⁻⁵` and its
  scheme-independence; `Q_up/Q_down ≠ 2/3` and their scheme/scale drift.
- **Cited**: the recordable single-summand structure (#2910/#2917/#2923); the
  Record axiom's realized-outcome premise (`MINIMAL_AXIOMS_2026-06-05`); the
  framework's SU(3) confinement (the gauge sector / `β=6` `⟨P⟩` campaign);
  "confined ⟹ no pole mass" (standard QCD); the pole-vs-running Koide obstacle
  (Koide 2018; Sumino; Rivero–Gsponer) as the literature comparator.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. It does not promote any note or change any
audited claim scope.

- [KOIDE_R_HALF_RECORD_NATIVE_READOUT_DOUBLET_COUNTED_ONCE_NARROW_THEOREM_NOTE_2026-06-06.md](KOIDE_R_HALF_RECORD_NATIVE_READOUT_DOUBLET_COUNTED_ONCE_NARROW_THEOREM_NOTE_2026-06-06.md)
- [KOIDE_2OVER9_RECORD_LOCAL_FIXED_POINT_READOUT_NARROW_THEOREM_NOTE_2026-06-06.md](KOIDE_2OVER9_RECORD_LOCAL_FIXED_POINT_READOUT_NARROW_THEOREM_NOTE_2026-06-06.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- [QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md](QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md)
