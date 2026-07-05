# Tick Unitarity From Spectrum-Reflection Conjugacy: The Realized-Tick Unitarity Premise Reduces To Discrete-Symmetry Transport Plus The Channel Envelope

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope note:** exact unitarity characterization for the realized one-tick
update; retires the legacy bare unitary-tick reading (P2) of the
kinetic-isotropy chain into two narrower named readings.
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/tick_unitarity_from_spectrum_reflection_conjugacy_2026_06_10.py`](../scripts/tick_unitarity_from_spectrum_reflection_conjugacy_2026_06_10.py)
(SCORECARD: PASS=28, FAIL=0; cached:
[`logs/runner-cache/tick_unitarity_from_spectrum_reflection_conjugacy_2026_06_10.txt`](../logs/runner-cache/tick_unitarity_from_spectrum_reflection_conjugacy_2026_06_10.txt))

---

## What this closes (relative to block01 and the dichotomy cycle)

In the kinetic-isotropy retirement chain, block01
(`KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md`)
named **(P2) "unitarity of the realized one-tick update"** as a bare
conditional reading, and the site-license dichotomy cycle
(`STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md`)
discharged P3 and reduced P4 while still **assuming** the unitary tick in its
setting. P2 is the surviving dynamical premise of the chain.

These two references name the surrounding retirement chain and downstream
consumers; they are not load-bearing authorities for the finite-dimensional
characterization proved here. They are recorded as plain filenames so the
source graph keeps the audit direction honest.

This note replaces the bare unitarity postulate with an **exact
characterization**: inside the physical-envelope class (invertible
contractions), unitarity is *equivalent* to carrying a spectrum-reflection
conjugacy — and the retained CPT-note identity table already supplies two such
conjugacies on the staggered Hamiltonian sector, both of which transport to
the exponential tick exactly. The bare reading "the tick is unitary" is
thereby retired into two narrower named readings:

- **(C-reading)** the realized tick carries a tick-level transport of either
  retained spectrum-reflection identity (unitary sublattice `eps H eps = -H`,
  or the antiunitary commuting CPT representative `[Theta, H] = 0`) — the same
  epistemic slot as block01's P3 reading (an H-level retained identity read on
  the tick), now doing P2's work;
- **(N-reading)** the realized tick is norm-nonincreasing on its carrier (the
  channel envelope: physical maps do not increase norm).

The `omega <-> -omega` quasi-energy pairing (block01's P3) follows as a
corollary of the unitary-S version — coherent with the dichotomy cycle having
discharged its separate use.

## The theorem (finite-dimensional, exact)

**Setting:** `T` an invertible linear map on a finite-dimensional Hilbert
space with `||T|| <= 1` (operator norm; the contraction/channel envelope).
Call `Theta` a *spectrum-reflection conjugacy* for `T` if `Theta` is isometric
or anti-isometric and

```text
    Theta T Theta^{-1} = T^{-1}.
```

**Theorem (characterization).**

```text
    a spectrum-reflection conjugacy exists for T   <=>   T is unitary.
```

**Forward.** Isometric and anti-isometric conjugations preserve the operator
norm (conjugation preserves singular values), so the relation forces
`||T^{-1}|| = ||T|| <= 1`. Then for every `x`,
`||x|| = ||T^{-1} T x|| <= ||T x|| <= ||x||`, so `T` is an isometry; a
finite-dimensional isometry is unitary.

**Converse.** For unitary `T = W D W^dag` with unimodular `D`, the antiunitary
`Theta = W o K o W^{-1}` (complex conjugation in the spectral frame) satisfies
`Theta T Theta^{-1} = W conj(D) W^{-1} = T^{-1}`, and is an involution.

Both directions, the load-bearing norm identities, and the corollary are
verified exactly by the runner (Parts A-C, E).

**Corollary (the former P3).** If the conjugacy is implemented by a unitary
`S` (the sublattice case), `S T S^{-1} = T^{-1}` pairs the quasi-energy
spectrum `omega <-> -omega` exactly (runner Part E6).

## The framework read

The retained scope of [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md) (post-2026-05-19
narrowing: the `Theta_H`-odd Hamiltonian-sector identities) supplies, on the
staggered carrier:

- the **C-type unitary** sublattice parity `eps(x)` with `eps H eps = -H`;
- the **CPT-type antiunitary** commuting representative with `[Theta, H] = 0`.

At exponential-tick level both give `Theta U Theta^{-1} = U^{-1}` exactly
(runner Parts E1-E4, massless hopping carrier, `L = 8, 12`; the identity
`Theta e^{-iH} Theta^{-1} = e^{+iH}` uses only anticommutation-or-antiunitarity
with `H`). Reading either identity on the **realized strict tick**, plus the
channel envelope, the theorem forces tick unitarity — and the dichotomy
cycle's flat-or-saturating conclusion then applies to it with its "unitary"
hypothesis discharged into the two readings above.

The chain state after this note:

```text
  {C-reading + N-reading}  =>  tick unitarity (P2)      [this note, exact]
  + P1 site-license reading                              [block01 / dichotomy]
  + dispersiveness (reduced P4)                          [dichotomy]
  =>  |v| = 1 exactly                                    [dichotomy]
  + B-W bridge (OS0 identification)                      [named open]
  =>  c_t = c_s                                          [the primitive's content]
```

## Premise ledger, with provenance (each graded honestly)

- **(C-reading) tick-level transport** — the H-level identities are retained
  (CPT note, narrowed scope). Their transport to the realized strict tick is a
  **named reading**, not derived here: the exponential ticks used as instances
  are not strict radius-1 (runner Part G1 reproduces block01 Part C's leakage),
  so the realized strict tick is a distinct object on which the same symmetry
  is read. This is the identical epistemic move block01 made for P3, now
  carrying P2's load instead.
- **(N-reading) channel envelope** — `||T|| <= 1` on the carrier is the
  physical-map envelope (quantum-channel restrictions are contractions). Named
  reading; its grounding in the framework's pointer-level CPTP surface is
  adjacent landed science but is **not** consumed or derived here.
- **Invertibility** — part of the relation's meaning (a singular tick cannot
  satisfy it). Decohering open-sector ticks are thereby **outside the
  hypothesis class**, which is consistency with the einselection program, not
  a conflict: unitarity is located exactly where the spectrum-reflection
  identities hold (the matter carrier), and nowhere broader (runner Part D/W3).

## Hostile witnesses (wall-independence)

| dropped hypothesis | witness | outcome |
|---|---|---|
| conjugacy | scalar winding family `r e^{ik}` (block01 Part E2's tunable class) | contraction, winding 1, relation a-priori unsatisfiable (`\|\|T^{-1}\|\| = 1/r > 1`), not unitary |
| contraction | `diag(2, 1/2)` with swap conjugacy | relation **holds**, not unitary — the envelope is load-bearing |
| invertibility | dephasing tick (Kraus `{P_0, P_1}`) | singular; relation unsatisfiable; open-sector ticks evade the theorem by design |

## Coherence with the irreducibility support

The kinetic-isotropy independence surface
([`KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md))
exhibits a **bosonic positive-transfer** witness family with tunable
`xi = c_t/c_s`. That family is exactly the relation-**violating** sector:
`T = e^{-E}` has `||T^{-1}|| > 1` strictly whenever `E != 0` (runner Part F).
The support note's non-fixation result and this note's unitarity forcing are
therefore disjoint-sector statements: the tunable family lives on the
Euclidean (positive-transfer) side, the forcing lives on the real-time
(spectrum-reflection) side. This note walks further through the support
note's own N7 steelman door; it does not contradict the support.

## What this does not do

- It does not derive the tick-level transport of the H-level identities (the
  C-reading) or the channel envelope (the N-reading); both are named readings
  with stated parentage.
- It does not supply locality: the theorem uses no locality input at all
  (runner Part G2); P1 remains the dichotomy cycle's separate license reading.
- It does not compute the B-W bridge: the OS0 `c_t/c_s` consequence of
  `|v| = 1` remains the named open identification.
- It does not assert framework-wide unitarity: open-sector (decohering) ticks
  are outside the hypothesis class by construction.
- Mass-sector scope: the framework instances are the massless hopping carrier
  (the dispersive/massless point is where the kinetic-form normalization
  lives, per the dichotomy cycle); the massive carrier's tick is the
  dichotomy note's named periodicity open, inherited unchanged.
- It does not add an axiom or primitive, and it does not set audit status.

## Falsifiers

- An invertible contraction satisfying the relation that is not unitary
  (would refute the forward direction).
- A unitary admitting no spectrum-reflection conjugacy (would refute the
  converse).
- A retained-surface derivation that the realized strict tick **fails** the
  tick-level transport of both retained identities (would empty the C-reading
  on the realized carrier and re-open bare P2).
- A physical realized tick on the matter carrier that increases norm (would
  empty the N-reading).

## Dependencies

- [CPT_EXACT_NOTE.md](CPT_EXACT_NOTE.md) — the retained `Theta_H`-odd
  Hamiltonian-sector identities (C-type `eps H eps = -H`; CPT-type
  `[Theta, H] = 0`); retained scope per its 2026-05-19 narrowing.
- `KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  — context source: it names P2, and its Part C/E2 witnesses are restated
  here as hostile witnesses. This is not an upstream theorem premise for the
  characterization.
- `STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  — downstream consumer: its "unitary tick" hypothesis is what this note
  grounds if this note later passes independent audit.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the target primitive of the retirement chain.
- [KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md)
  — the independence surface; Part F verifies the disjoint-sector coherence.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
