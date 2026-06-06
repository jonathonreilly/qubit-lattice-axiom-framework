# The 2/9 Charged-Lepton Asymmetry is the Local Fixed-Point Density a Record Reads

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. It writes no audit verdict and supplies no direct
effective-status change.
**Primary runner:**
[`scripts/frontier_koide_2over9_record_local_readout_2026_06_06.py`](../scripts/frontier_koide_2over9_record_local_readout_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_2over9_record_local_readout_2026_06_06.txt`](../logs/runner-cache/frontier_koide_2over9_record_local_readout_2026_06_06.txt)

---

## Role

Supplies the **"one named open bridge"** of
[FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md](FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md)
and
[FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md](FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md)
(both retained_bounded): the **physical single-summand readout**.

Those notes establish, on the supplied finite staggered / Kawamoto-Smit C₃
surface at the framework-forced `d = 3`:

- the Atiyah-Bott **local** fixed-point Lefschetz density is `L₃(1,2) = 2/9` (the
  faithful transverse C₃ doublet; the degenerate alternative gives
  `L₃(1,1) = 1/9`);
- the **global** readouts **vanish** (the staggered chirality `γ₅` anticommutes
  with `D`, so the signed eta sum and the equivariant eta trace are zero, and
  `Tr(γ₅ U) = 0`);
- the open bridge is, verbatim: the charged-lepton asymmetry observable is the
  *"single fixed-point local Lefschetz density `2/9`, **not** the vanishing global
  eta/equivariant invariant **and not** the extensive sum over all fixed sites."*

So the **same** operator admits **three** candidate readouts:

```text
    (a) single fixed-point LOCAL density   = 2/9        <- matches the data
    (b) global equivariant / eta invariant = 0          (vanishes by symmetry)
    (c) extensive sum over all fixed sites = 3·(2/9) = 2/3
```

## The result (runner SCORECARD 20/20 PASS)

**The recordable-outcome lens selects (a).** The Record axiom
([MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)) states: *"the
realized outcome is the K/CPT orbit of the **realized** central sector ...
durable ... A record supplies no ... within-sector data."* A record is therefore
a **single, local, realized, durable** imprint at one fixed sector. That is
exactly the single-summand local density **(a) = 2/9**. It is:

- **not (b)**, the global equivariant invariant — a symmetric average over *all*
  sectors, which no single realized record is (and which vanishes by the C₃
  symmetry the record breaks by realizing one sector);
- **not (c)**, the extensive all-sites sum — which records *every* site at once,
  not a single realized outcome.

So **the "physical single-summand readout" the bridge requires is precisely what a
record is.** With `2/9` already forced as the local density (cited, retained),
the recordable lens makes it the **recorded** charged-lepton asymmetry — closing
the single named open bridge.

Reproven in the runner: the cyclotomic norm `(1-ω)(1-ω²) = 3`; the Atiyah-Bott
density `L₃(a,b) = (1/3)Σ_{j=1,2} 1/[(1-ω^{ja})(1-ω^{jb})]` giving
`L₃(1,2) = 2/9` and `L₃(1,1) = 1/9`; the forced trace-free weight `(1,2)`
(`a₁+a₂ ≡ 0 mod 3`); the global signed-eta vanishing via `γ₅`-anticommutation
(`±λ` pairing). **Teeth:** reading the global invariant gives `0` (no asymmetry —
contradicts three distinct masses); reading the extensive sum gives `2/3 ≠ 2/9`
(over-counts); only the single local realized record yields `2/9`.

## Why this is the right move (and not the radian route)

Recall the radian Brannen phase `δ = 2/9` is π-transcendentally **unreachable** by
any dynamical periodic phase (those are all `q·π`; `2/9` radians is not):
that is the retained_no_go radian bridge. **This note does not use the radian
phase at all.** It reads the **dimensionless** `2/9` directly as the local
Lefschetz density — a pure rational, no radian, no π-transcendence obstruction.
The recordable readout bypasses the radian route entirely. **The two `2/9`s must
not be conflated** (the framework states this explicitly): this is the
dimensionless density, not the radian phase.

## Honest residual (named, not closed)

- **The carrier / `d=3` / KS operator surface is supplied** (cited retained: the
  three-generation observable theorem; the local-density operator certificate).
- **Scale and spectrum normalization are separate channel inputs.** The
  asymmetry is the genuinely-derivable channel; the overall mass scale and the
  relative normalization are carried separately (not derived here).
- This is a **finite-surface** readout (the KS certificate's scope); no
  thermodynamic-limit or continuum theorem is claimed.

## Reprove-and-cite ledger

- **Reproven here** (exact sympy + finite numerics): `(1-ω)(1-ω²)=3`; the
  Atiyah-Bott `L₃(1,2)=2/9`, `L₃(1,1)=1/9`; the trace-free weight selection; the
  `γ₅`-anticommutation `±λ` pairing → signed eta `= 0`; the three readout values
  `(2/9, 0, 2/3)`.
- **Cited** (reused, not re-derived): the forced local density `2/9` and the
  global-vanishing operator certificate
  (`flavor_asymmetry_2over9_forced_weight`,
  `flavor_operator_realization_local_density`); the forced `d=3` /
  three-generation carrier; the Record axiom (`MINIMAL_AXIOMS_2026-06-05`); the
  radian-bridge no-go separation (`koide_a1_radian_bridge_irreducibility`).

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. It does not promote this note or change any
audited claim scope.

- [FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md](FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md)
- [FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md](FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- [KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
