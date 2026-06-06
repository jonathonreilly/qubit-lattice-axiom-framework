# The Magnitude of the Interaction Asymmetry `delta` Reduces to the Massless-Gravity Scale; the Form is Corner-Protected and the Flavor Pattern is Robust — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (the magnitude reduction + form/pattern robustness; the magnitude itself open)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/delta_magnitude_massless_gravity_scale_runner.py`](../scripts/delta_magnitude_massless_gravity_scale_runner.py)
**Cached output:** [`logs/runner-cache/delta_magnitude_massless_gravity_scale_runner.txt`](../logs/runner-cache/delta_magnitude_massless_gravity_scale_runner.txt)

## Audit context

The interaction asymmetry `delta` (the two-excitation mutual energy that sources the emergent
`C3` coupling `|K|`) has its **form** fixed (`J − I`, corner-protected) and its **sign** fixed
(`< 0`, attractive). Its **magnitude** was reduced to the mediator's IR scale. This note traces
that scale: the framework's gravity is **massless** (retained
[`NEWTON_LAW_DERIVED_NOTE`](NEWTON_LAW_DERIVED_NOTE.md), `retained_bounded`: an inverse-square
`1/r` law), so the mediator's `mu^2` is an **IR regulator**, not a physical mass, and the
magnitude of `delta` reduces to the **single open gravity-scale derivation** named by the
[`SCALE_REFERENCE_PRIMITIVE_NOTE`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (the framework takes exactly
one dimensionful ruler and "whether the framework's natural unit equals the Planck length remains
a separate open gravity derivation").

Mediator: retained
[`STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11`](STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md)
(`retained_bounded`). Pattern sieve: retained
[`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md)
(`bounded_theorem`).

## Safe statement

With `delta_ij = ( Vq(0) − Vq(k_i − k_j) ) / N`, `Vq(q) = −G/(eps(q)+mu^2)`,
`eps(k_i − k_j) = 8` for every generation corner pair:

1. **The magnitude is the massless-gravity IR scale.** As `mu^2 → 0` (the framework's massless
   `1/r` gravity), the `q = 0` **monopole** `|Vq(0)| = G/mu^2` is IR-divergent — it *is* the
   gravitational IR scale — while the corner (Fock) part `|Vq(Δk)| = G/(8+mu^2) → G/8` is
   `mu^2`-**independent** (the IR-safe piece). So `|delta|` is set by the gravity mediator's IR
   scale `(G, mu^2)`, not a localization distance. By the scale-reference primitive (one ruler,
   zero dimensionless content), the physical magnitude is exactly what the framework leaves to
   the **open gravity-scale derivation** — `delta`'s magnitude is **not an independent flavor
   parameter**; it is unified with the gravity scale.

2. **The `J − I` form is corner-protected and IR-robust.** `eps(Δk) = 8` for all three generation
   pairs at *every* `mu^2`, so the exact `C3` (`J − I`) form holds independently of the magnitude.

3. **The emergent coupling is K-real.** The second-order `|K|` is a **real** coefficient on
   `J − I = C + C^2`, i.e. it lies in the einselection sieve's K-real cone `span_R{I, C + C^2}`
   — so it is **2-sector-partition-compatible** (the sieve's K-real predicate selects the
   singlet ⊕ doublet partition over the 3-mode `r=0` partition). Shown for the **real single-hop
   model**; whether the full complex staggered-Dirac hopping preserves K-reality is the open
   K-reality predicate. This does **not** deliver the value `r=1/2` (no overreach).

4. **The flavor pattern is robust to the magnitude.** The predictability sieve selects the pointer
   basis as the eigenbasis of the **dominant** of `{coupling |K|, sector mass M}`. The selection
   flips on the `|K|`-vs-`M` **ordering**, so for any `|K|` across a wide window the lightest
   (neutrino) sector is `|K|`-dominated (→ `C3`, large mixing) and the heavier sectors are
   mass-dominated (→ corner, small mixing). The pattern is robust to the magnitude **and** the
   sign of `|K|` (the sieve uses `|K|`, not `sign(K)`).

So the magnitude of `delta`/`|K|` is the framework's massless-gravity scale (open by design),
the `C3` (`J − I`) form is corner-protected, the coupling is K-real, and the flavor pattern is
robust to the magnitude.

## The genuine open piece (the route this opens)

The magnitude is the **open gravity-scale derivation** — the framework's single open dimensionful
self-consistency (`a/l_P`), not a flavor parameter. So the route this opens is the gravity-scale
self-consistency, shared with the gravity sector, *not* a new flavor input. The K-reality of the
**full** staggered-Dirac (complex-hopping) coupling is the other named-open predicate (the sieve's
K-reality question); the real single-hop model satisfies it here.

## Boundary (honest)

- **Magnitude reduction, not a value.** The magnitude is traced to the open gravity scale; it is
  not pinned.
- **Symbol collision (important).** The einselection sieve's "`δ=0`" denotes the **Brannen phase**
  `arg(b)` (time-reversal-reality), a *different* object from this note's energy-asymmetry
  `delta`. They are not conflated; only the K-real **cone** (`span_R{I, C+C^2}`) is shared.
- **K-reality shown for the real single-hop model.** The complex staggered-Dirac hopping is the
  open K-reality predicate; this note does not settle it, and forces no value `r`/`Q`.
- **Robustness uses the retained sieve logic** (pointer = dominant of `{|K|, mass}`); the window's
  precise width is a separate quantitative surface.

## Forbidden imports check

No new axiom/import. Massless gravity (`NEWTON_LAW_DERIVED`), the two-body mediator
(`STAGGERED_SELF_CONSISTENT_TWO_BODY`), the corner generations, the einselection cone
(`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY`), and the scale-reference primitive are all
**retained/declared**. The IR structure, the cone membership, and the ordering logic are exact
arithmetic. The magnitude is named open (the gravity-scale derivation), not asserted.

## Runner check breakdown

Class A: (1) the monopole `G/mu^2` diverges as `mu^2 → 0` while the corner-Fock `G/(8+mu^2) → G/8`
is `mu^2`-independent; (2) `eps(Δk) = 8` for all three pairs (form corner-protected); (3) `J − I =
C + C^2` and the emergent `|K|` is real (K-real cone) for either sign of `delta`; (4) the
`|K|`-vs-mass ordering flips the pointer basis across a wide window. Expected
`runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content shows that for the framework's massless (`1/r`) gravity the magnitude of
`delta` is carried by the IR-divergent `q=0` monopole (the gravitational IR scale), with the
corner-Fock `G/8` as the `mu^2`-independent IR-safe remainder; that the `J − I` form is
corner-protected at every `mu^2`; that the emergent `|K|` is K-real (in the sieve's
`span_R{I, C+C^2}` cone, hence 2-sector-partition-compatible) for the real single-hop model; and
that the predictability sieve's pointer selection flips on the `|K|`-vs-mass ordering, making the
flavor pattern robust to the magnitude and sign. The magnitude reduces to the open gravity-scale
derivation rather than an independent flavor parameter. The note forces no value `r`/`Q` and flags
the Brannen-`δ` symbol collision and the complex-hopping K-reality caveat. Effective status
remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/delta_magnitude_massless_gravity_scale_runner.py
```
