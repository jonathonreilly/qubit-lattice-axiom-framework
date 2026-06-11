# B-W Bridge Reduction: The OS0 Identification Consumes Only The IR Slope

**Date:** 2026-06-10
**Claim type:** bounded_theorem (computes the computable half of the named
B-W bridge exactly and sharpens the remainder to one named IR-restricted
premise; the full Wick-pair version is refuted for strict ticks)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/bw_bridge_reduction_os0_ir_slope_2026_06_10.py`](../scripts/bw_bridge_reduction_os0_ir_slope_2026_06_10.py)
(SCORECARD: PASS=20, FAIL=0; cached:
[`logs/runner-cache/bw_bridge_reduction_os0_ir_slope_2026_06_10.txt`](../logs/runner-cache/bw_bridge_reduction_os0_ir_slope_2026_06_10.txt))

---

## What this closes (relative to block01 and the dichotomy cycle)

Block01
([`KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md))
and the site-license dichotomy cycle
([`STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md`](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md))
deliver `|v| = 1` for the realized dispersive tick and leave the translation
of that real-time cone slope into the OS0 Euclidean ratio `c_t/c_s` as the
**named bridge B-W** — "the standard first-order Wick identification", not
computed there.

This note splits B-W into a computable half and a premise half, computes the
computable half **exactly**, and shows the premise half is **forced** to be
IR-restricted (the naive full version is false for strict ticks). After this
note the bridge's content is:

```text
  B-W  =  (T1)-(T2) exact computation   +   (W-IR) one named premise.
```

## The theorem (exact, both carrier orders)

**(T1) The inverse map.** For the spatially `O_h`-invariant Euclidean lattice
kinetic forms (massless point),

```text
  second-order carrier:  c_t (2 sinh(E/2))^2 = c_s (2 sin(p/2))^2
                         =>  E(p) = 2 asinh( sqrt(c_s/c_t) sin(p/2) ),
                             cone slope v = sqrt(c_s/c_t)  EXACTLY,
                             xi := c_t/c_s = 1/v^2;
  first-order carrier:   c_t sinh(E) = c_s sin(p)
                         =>  cone slope v = c_s/c_t  EXACTLY,
                             xi = 1/v.
```

Both inverse maps are injective on `v > 0`, so `v = 1  <=>  xi = 1` in both
carrier orders, and the two reads agree at — and only at — the isotropic
point (runner Parts A, B, F3). The two-coefficient freedom of the spatial
no-go is reproduced, not erased: nothing in the form itself forces `xi`
(Part A4).

**(T2) UV-insensitivity.** The quadratic-order OS0 extraction consumes
**only** the cone slope: bands with the same slope and different UV shapes
(`arcsinh(sin p)`, the exactly-linear saturating dichotomy band, a deformed
sine) give the same `xi`; slope-`1/2` bands give `xi = 4` (second-order read)
regardless of UV shape (runner Part D). This is what makes an IR-restricted
bridge premise *sufficient*.

**(T3) The Wick mapping at a supplied pair.** At a **supplied** `(T, tau)`
(positive transfer, blocked-time normalization), the generator is unique and
the Wick pair `U = e^{-i tau H}`, `T = e^{-tau H}` shares its dispersion:
quasi-energy phase `= -tau E` exactly (runner Part C). The Stone uniqueness
is used scope-compliantly: it is transfer-relative AND tau-relative — the
runner reproduces the tau-relativity (`(T, 2 tau)` reconstructs `H/2`) so the
supplied status of `tau` stays visible.

**(T4) The full pairing is refuted for strict ticks; W-IR is forced.** The
exponential tick of the transfer's `H` leaks beyond radius 1 at every nonzero
step, while a strict radius-1 tick has distance-2 amplitude exactly 0 (runner
Part E, reproducing block01 Part C and exhibiting the strict contrapositive).
So "the realized strict tick **is** `e^{-i tau H}` of the transfer's `H`" is
**false**, and the surviving minimal identification is:

```text
  (W-IR)  at the cone point, the realized tick's quasi-energy band and the
          supplied RP transfer's reconstructed dispersion agree to first
          order in momentum.
```

By (T2), W-IR is exactly strong enough; by (T4), nothing stronger is
available on the strict-tick surface. Under W-IR, the chain's `|v| = 1`
gives `xi = 1` — the kinetic-isotropy primitive's content — at quadratic
order, exactly (runner Part F).

## Where W-IR sits

W-IR is the dispersion-level shadow of the one-spectrum question: the
scope-boundary note
([`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md))
records that excluding an independent second clock/spectrum requires a
separate premise (its checklist item N5). W-IR asserts single-spectrum
agreement at one point (the cone point) to one order (first) — strictly
narrower than both "the first-order Wick identification" and a framework-wide
no-second-clock claim. Its derivation from the record/readout surface is the
next open row of this chain, not claimed here.

## Chain state after this note

```text
  {C-reading + N-reading}  =>  tick unitarity (P2)     [separate spectrum-reflection cycle; not consumed here]
  + P1 site-license reading                            [block01 / dichotomy]
  + dispersiveness (reduced P4)                        [dichotomy]
  =>  |v| = 1 exactly                                  [dichotomy]
  + (W-IR) cone-point agreement, supplied tau          [THIS NOTE: the bridge residual]
  =>  xi = c_t/c_s = 1 at quadratic order, exactly     [THIS NOTE: T1-T2]
```

For the larger kinetic-isotropy primitive retirement campaign, this note
replaces the old bare "unitarity + Wick bridge" residual with W-IR on the
B-W side. Any spectrum-reflection/P2 readings and the P1/periodicity scope of
the dichotomy cycle remain separate rows with their own grades.

## Premise ledger, with provenance (each graded honestly)

- **(W-IR)** — named premise, **not derived**. Grounding target: the
  one-spectrum question (scope-boundary N5 slot). The runner proves its
  *sufficiency* (T2) and its *minimality direction* (T4: stronger pairings
  are refuted), not its truth.
- **supplied `tau`** — the blocked-time normalization convention from
  [`AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md);
  consumed as a convention input, with the tau-relativity guard kept visible
  (runner Part C3).
- **Stone uniqueness at supplied `(T, tau)`** — the retained narrow theorem
  ([`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)),
  used inside its scope per the scope-boundary note.
- **carrier forms** — the two `O_h`-invariant kinetic forms are the
  anisotropy gate's invariant space
  ([`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md));
  the two-coefficient freedom is reproduced (Part A4), so no isotropy is
  smuggled in through the form.

## Hostile/contrast witnesses

| claim stressed | witness | outcome |
|---|---|---|
| nothing forces `xi` in the form | `xi in {4, 1, 1/4}` sweep | slope tracks `1/sqrt(xi)`; freedom is real (A4) |
| extraction is slope-only | slope-1 bands, three UV shapes | same `xi = 1`; slope-1/2 bands give `xi = 4` (D1, D2) |
| full Wick pairing | exponential-tick leakage vs strict-tick zero | full pairing refuted; W-IR forced (E1, E2) |
| `tau` erasure | `(T, 2 tau) -> H/2` | tau-relativity reproduced, supplied status visible (C3) |

## What this does not do

- It does not derive W-IR; it names it, proves its sufficiency, and shows the
  stronger pairings are unavailable.
- It does not derive the blocked-time `tau` or any absolute scale (the scale
  reference is untouched; no dimensionful content is used).
- It does not produce a framework-wide no-second-clock theorem (the
  scope-boundary note's discipline is followed, not bypassed).
- It does not promote the chain upstream of it: the conditionality of
  block01 and the dichotomy cycle is inherited, and any
  spectrum-reflection/P2 cycle remains separate unless landed and audited on
  its own.
- Radiative/interacting orders remain the velocity-RG row; this is the free
  single-particle quadratic-order statement.
- It does not add an axiom or primitive, and it does not set audit status.

## Falsifiers

- A band family where the quadratic OS0 extraction depends on UV shape at
  fixed cone slope (would refute T2).
- An exact solution of either carrier relation whose cone slope differs from
  the stated inverse map (would refute T1).
- A strict radius-1 tick equal to the exponential of a NN transfer generator
  (would refute T4 and re-open the full Wick pairing).
- A retained derivation that the realized tick's cone-point dispersion
  *differs* from the RP-reconstructed one (would falsify W-IR and with it
  this route to the primitive's content — the route, not the primitive).

## Dependencies

- [KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — block01: names B-W and the leakage point; landed but unaudited, so
  conditionality is inherited.
- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — supplies `|v| = 1` for the dispersive licensed tick; landed but
  unaudited, so conditionality is inherited.
- [SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
  — the scope discipline for every uniqueness statement used here.
- [SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
  — the (T, tau)-relative generator uniqueness.
- [AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md](AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — the supplied blocked-time normalization convention.
- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
  — the two-coefficient invariant space whose freedom Part A4 reproduces.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the target primitive of the retirement chain.
- [KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md)
  — the independence surface this chain walks through (its own N7 door).

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
