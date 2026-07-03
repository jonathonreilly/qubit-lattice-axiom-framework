# Flavor Value Campaign Finite Channel Boundary

**Date:** 2026-05-31
**Scope repair date:** 2026-06-07
**Claim type:** bounded_theorem
**Actual current surface status:** bounded-support
**Runner:** `scripts/flavor_four_channel_reframe_validated_2026_05_31.py`
(`SCORECARD PASS=5 FAIL=0`).

## Scope

This packet is a finite coordinate-algebra boundary for the supplied `C3`
circulant form

```text
H = a I + b C + conjugate(b) C^2.
```

It does not derive this operator from the axiom baseline, does not derive the
physical gauge/Yukawa/CP/anomaly channel identifications, and does not derive
the topological `eta=2/9` datum. It also does not provide a complete account of
charged-lepton flavor.

The old campaign-capstone language is superseded. The safe claim is narrower:
within the supplied circulant coordinate model, scale, ratio, and phase are
independent coordinates, while the displayed `Q` values depend on the chosen
readout convention.

## Finite Algebra

Write `b=|b| exp(i delta)` and use the three real coordinates

```text
(a, |b|, delta).
```

The runner verifies:

1. The Jacobian of

   ```text
   (mean eigenvalue, dispersion Q, delta)
   ```

   with respect to `(a, |b|, delta)` is nonzero at the tested generic point.
   This is a finite local-coordinate independence check.

2. A supplied generation-blind scalar `G=gI` has zero coefficient on the
   `C/C^2` doublet direction. This proves a singlet/doublet algebra fact for
   that supplied scalar operator, not a physical gauge-sector theorem.

3. The dispersion readout `Q` is independent of `delta` in the supplied model.
   This separates the ratio coordinate from the phase coordinate at the level
   of the displayed formula.

4. The specific numerical floors are readout-convention dependent:

   ```text
   Q_dispersion(r=0)=1/3,      Q_Brannen(r=0)=1.
   ```

   Therefore the coordinate decomposition is separate from any physical
   choice of readout convention.

## Boundary

The branch supports this statement:

> The supplied `C3` circulant model has three finite real coordinates
> `(a, |b|, delta)` whose displayed readouts are locally independent in the
> runner. The singlet/doublet split and the `delta`-blindness of dispersion
> `Q` are finite algebraic facts. Physical channel interpretation, `eta=2/9`,
> and charged-lepton value selection remain outside this packet.

The open bridges are:

- axiom-to-`H` construction for the physical charged-lepton carrier;
- retained lane/channel bridge from the finite coordinates to gauge, Yukawa,
  CP, anomaly, or flavor observables;
- retained derivation of the `eta=2/9` topological datum in this restricted
  packet;
- retained or accepted readout-convention selection.

## Audit Relevance

This repair removes the capstone overclaim that the campaign has a complete
framework-native charged-lepton flavor account. It preserves the finite
coordinate facts that the runner actually checks. It does not retag the audit
ledger and does not add an axiom.
