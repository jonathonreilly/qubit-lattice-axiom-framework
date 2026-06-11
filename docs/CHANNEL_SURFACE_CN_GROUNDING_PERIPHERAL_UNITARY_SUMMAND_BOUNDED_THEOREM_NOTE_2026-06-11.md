# C And N Ground On The Channel Surface: The Peripheral Unitary Summand

**Date:** 2026-06-11
**Claim type:** bounded_theorem (derives the spectrum-reflection cycle's two
named readings — the channel envelope and the conjugacy transport — on the
channel surface itself; the residual is three named items, each strictly
narrower)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/channel_surface_cn_grounding_peripheral_summand_2026_06_11.py`](../scripts/channel_surface_cn_grounding_peripheral_summand_2026_06_11.py)
(SCORECARD: PASS=12, FAIL=0; cached:
[`logs/runner-cache/channel_surface_cn_grounding_peripheral_summand_2026_06_11.txt`](../logs/runner-cache/channel_surface_cn_grounding_peripheral_summand_2026_06_11.txt))

---

## What this narrows (relative to the spectrum-reflection cycle)

The landed spectrum-reflection cycle
([`TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md`](TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md))
retired the kinetic-isotropy chain's bare unitarity premise into two named
readings:

- **(N)** the realized tick is norm-nonincreasing on its carrier fiber;
- **(C)** the realized tick carries a tick-level transport of a retained
  spectrum-reflection identity.

This note grounds the channel-theoretic part of both readings on the channel
surface. **N becomes a theorem** on the doubly stochastic class, with each
hypothesis witnessed as load-bearing. **C becomes automatic on the peripheral
unitary summand** — the asymptotically undamped part of the tick — eliminating
the transport premise there. On this channel-surface slice, the residual is
three named items: the CPTP-class reading, sea-stationarity, and band
persistence. Consumer-specific finite-window covariance and record-production
premises remain with the downstream notes that use them.

## The theorems (finite-dimensional, exact)

**(T1, N derived.)** A unital trace-preserving CP fiber tick is a
**Hilbert-Schmidt contraction**:

```text
  ||Phi(a)||_2^2 = tr(Phi(a)^dag Phi(a))
                <= tr(Phi(a^dag a))        [operator Schwarz: unitality]
                 = tr(a^dag a) = ||a||_2^2 [trace preservation].
```

Verified: the Schwarz gap is PSD on 30 random unital CP Stinespring maps;
mixed-unitary (doubly stochastic) superoperators have HS-norm `<= 1` with
the chain checked stepwise (runner Parts A, B). **Both hypotheses are
load-bearing** (runner Part C): amplitude damping (TP, not unital) has
HS-norm `1.107 > 1`; a unital CP non-TP Stinespring witness has HS-norm
`1.018 > 1`.

On the carrier fiber, unitality is exactly **sea-state stationarity** (the
`K`-real maximally mixed state is stationary) — the same sea reading the
chain's spectral cycles already consume. So:

```text
  N  reduces to  { CPTP class  +  sea-stationarity }.
```

**(T2, peripheral structure.)** A finite-dimensional contraction splits as
`T = U_per (+) T_cnu`: each unimodular eigenvalue's eigenvector is a joint
`T^dag` eigenvector (the contraction equality case — the same mechanism as
the spectrum-reflection cycle's forward direction), the peripheral
eigenspaces reduce `T` orthogonally to a **unitary summand**, and the
completely-non-unitary remainder has spectral radius `< 1` (runner Part D).

**(T3, C derived on the summand.)** The peripheral summand carries the
**canonical** spectrum-reflection conjugacy — complex conjugation in its
spectral frame, the spectrum-reflection cycle's converse:
`Theta U_per Theta^{-1} = U_per^{-1}` exactly (runner Part E). On the
summand, C needs **no transport premise at all**.

**(T4, asymptotic consumer reduction.)** Tick-separation covariance data is
(peripheral oscillation) + (cnu transient); the cnu contribution decays
geometrically in finite dimension, and the runner measures the
`rho_cnu^{n_0}` suppression in a diagonal witness (Part F1). The chain's
spectral consumers factor through the peripheral summand when they are read
at large separation or in the faithful asymptotic window. This does **not**
discharge any consumer's separate finite-window covariance or record-production
premise. A fully cnu tick has nothing persistent for the chain to read
(Part F2): band persistence is exactly "the peripheral summand is nonempty".

**(T5, the residual.)**

```text
  before:  (N) channel envelope        -- named reading
           (C) conjugacy transport     -- named reading
  after:   { CPTP-class reading }      -- the pointer-transport surface's class
           { sea-stationarity }        -- fiber unitality; the standing sea reading
           { band persistence }        -- the carrier band is peripheral:
                                          the sharpened form of the dichotomy
                                          chain's reduced-P4 "dispersiveness"
```

Every item listed here is strictly narrower than what it replaces, and none is
a statement about a specific operator identity anymore. This list is the
channel-surface residual; downstream finite-period covariance, record
production, and other consumer-local gates are not changed by this note.

## Composition with the transcription cycle

The stack-transcription model's channel (`sigma_x`-dephasing x rotation) is
doubly stochastic — its Bloch transfer has HS-norm exactly 1 — and its
registered sector `M(eps)` is a strict contraction for `eps > 0` (empty
peripheral part: the band is slightly damped), becoming peripheral exactly
at `eps = 0` (runner Part G). The transcription cycle's faithful limit **is**
the peripheral restoration of this note's summand. The two cycles compose
without tension: registration dresses the peripheral band into the
`M(eps)` covariance; weak registration undresses it.

## Hostile witnesses (wall-independence)

| dropped hypothesis | witness | outcome |
|---|---|---|
| unitality | amplitude damping (TP) | HS-norm `1.107 > 1`: N fails (C1) |
| trace preservation | unital Stinespring non-TP | HS-norm `1.018 > 1`: N fails (C2) |
| band persistence | fully cnu tick | covariance dies geometrically; no band to read (F2) |

## What this does not do

- It does not derive that the realized tick is in the CPTP class: that is
  the record-dominated pointer-transport surface's reading
  ([`RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09.md`](RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  is the adjacent landed class surface), inherited as a named residual.
- It does not derive sea-state stationarity; it identifies it with fiber
  unitality, locating it as the same standing sea reading the chain's other
  cycles consume.
- It does not derive band persistence: that the carrier's band is
  peripheral (undamped) is the sharpened persistence residual — the
  successor of the dichotomy chain's reduced-P4, now with an exact
  structural meaning (nonempty peripheral summand).
- It does not replace the retained H-level identities: the CPT-note surface
  remains the physical source of the spectrum-reflection structure; this
  note shows the chain's consumers no longer need its tick-level transport
  as a separate premise.
- It does not add an axiom or primitive, and it does not set audit status.

## Falsifiers

- A unital trace-preserving CP map with HS-norm `> 1` (would refute T1).
- A contraction with a unimodular eigenvalue whose eigenvector fails the
  joint-`T^dag` property (would refute T2).
- A peripheral summand admitting no spectrum-reflection conjugacy (would
  refute T3 and the spectrum-reflection cycle's converse).
- Large-separation covariance data carrying non-peripheral content beyond
  the geometric bound (would refute T4).

## Dependencies

- [TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md](TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — names C and N; supplies the converse construction (T3) and the
  equality-case mechanism (T2); landed but unaudited, conditionality
  inherited.
- [RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09.md](RECORD_DOMINATED_POINTER_SECTOR_TRANSPORT_GENERATOR_VACUOUS_LINK_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — the adjacent landed pointer-transport surface whose channel class the
  CPTP reading cites; landed but unaudited, conditionality inherited.
- The stack-transcription cycle (`STACK_SPECTRAL_TRANSCRIPTION_WEAK_REGISTRATION_FAITHFUL_LIMIT`,
  in flight as PR #3547 at time of writing; cited by name, not linked, until
  it lands) — the cycle Part G composes with; the composition claim is
  conditional on it.
- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — the reduced-P4 residual that band persistence sharpens; landed but
  unaudited, conditionality inherited.
- [CPT_EXACT_NOTE.md](CPT_EXACT_NOTE.md) — the retained H-level
  spectrum-reflection source (context for what the transport premise was).
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  and
  [KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md)
  — the retirement chain's target and independence surface.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
