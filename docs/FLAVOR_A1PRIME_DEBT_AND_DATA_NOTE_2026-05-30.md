# Flavor A1prime Carrier-Measure Boundary

**Date:** 2026-05-30
**Scope repair date:** 2026-06-07
**Claim type:** bounded_theorem
**Actual current surface status:** bounded-support
**Runner:** `scripts/flavor_a1prime_debt_and_data_2026_05_30.py`
(`SCORECARD PASS=9 FAIL=0`).

## Scope

This packet is a bounded finite-algebra and comparator boundary. It does not
introduce, accept, or reject a revised Axiom 1. It does not prove a native
`r/Q` normalization law, a global det_C-versus-C3 incompatibility theorem, or
framework source certificates for the embedded mass and angle data.

The finite algebra asks a narrower question:

```text
Given the real group-element basis of R[Z3] and the supplied counting
convention, what support does J-I occupy?
```

The comparator section asks only whether the quoted sector-mass and angle
inputs stress a universal within-sector reading. Those inputs are external
comparators in this packet.

## Finite Algebra

Let `g` be the order-three cycle matrix and use the real group-element basis

```text
{e, g, g^2}
```

with normalized trace pairing `tau(A,B)=Tr(A^T B)/3`.

The runner verifies:

1. The Gram matrix of `{e,g,g^2}` under this pairing is the identity.
2. In that basis,

   ```text
   J - I = g + g^2
   ```

   has coefficient vector `(0,1,1)`, hence two nonzero real-basis
   components.
3. Under the supplied support-count convention, reading the two doublet
   components as two real slots gives the dimension/Plancherel-style count,
   while grouping them as one complex slot is an extra counting convention.
4. The fixed order-three carrier has only the cube-root phase orbit inside
   this finite `C^3=I` model. A continuous U(1) doublet phase is not present in
   this finite carrier model as checked.

This proves a boundary, not a global no-go: the packet does not rule out every
permissible complex representation of the order-three carrier, and it does not
derive the physical measure ranking.

## Comparator Stress Tests

The runner also recomputes the quoted comparator arithmetic:

- charged leptons land near the displayed `c^2=2` / `Q=2/3` value;
- up-sector and down-sector triples are above that value under the supplied
  inputs;
- the `(c,b,t)` cross-sector triple lands near the same value but is not a
  within-sector `C3` carrier;
- normal-ordering neutrino splittings stay below `Q=2/3` over the scanned
  lightest-mass interval;
- the listed CKM escape-angle inventory is `1.31-2.85` times the Cabibbo
  angle, not a closed sign/order mechanism.

These are class-D comparator checks inside this packet. They stress
universality, but they do not supply framework-internal source certificates for
the embedded masses, splittings, or angle inputs.

## Boundary

The supported statement is:

> On the supplied real `R[Z3]` tracial basis and support-count convention,
> `J-I` occupies two real group-element directions. A one-complex-slot reading
> of that doublet is extra structure relative to the finite order-three carrier
> model checked here. The quoted sector-data comparisons are external
> comparator stress tests, not framework-native derivations.

The open bridges are:

- a retained or accepted axiom text for any proposed `r/Q` normalization rule;
- a retained bridge proving when the complex doublet count is permissible or
  impermissible for the order-three carrier;
- retained source certificates for the embedded sector mass, splitting, and
  angle comparator inputs.

## Audit Relevance

This branch removes the stronger claims that the packet fully discharges or
falsifies a candidate axiom, proves an inherited framework default physical
value, or makes the charged-lepton `Q=2/3` fact a framework-native theorem.
It does not retag the audit ledger and does not add an axiom.
