# R-eta Conversion-Factor Carrier-Class Elimination -- Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane. This source note does not set or predict an audit outcome and does not edit audit-owned registry, ledger, queue, or publication-status surfaces.
**Primary runner:** `scripts/frontier_reta_conversion_carrier_class_elimination_2026_06_12.py`

**No-promotion statement:** this note does not promote, demote, or set the audit status of any dependency. The independent audit lane owns status.

## Boundary

This note addresses a single bounded question: within the retained registrable carrier classes on the supplied charged-lepton circulant surface, does any retained class supply a dimensionless multiplicative conversion factor `c != 1` for the rival family `delta = c * L` against the direct R-eta reading `c = 1`?

The answer is bounded to the retained surface. The note does not derive R-eta; the identification that the registered angle equals the fixed-locus density remains the named proposed premise. Future readout contexts remain open, including contexts with carriers not retained here. The occupancy dial is untouched. No comparator is consumed. The value `2/9` appears as the cited retained fixed-locus arithmetic, not as a new comparator input.

The retained registrable carrier classes considered here are:

- **R1 -- multiplicative determinant characters.** The `K`-invariance identity forces `k = 0`, so the class carries no angle datum.
- **R2 -- modulus, log-modulus, and symmetric-function data.** The supplied circulant's elementary symmetric data have delta-dependence through `e_3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta)`. The coefficient `3` is derived from the `C_3` orbit size and the `k -> -k` relabel, not chosen.
- **R3 -- periodic `q*pi` sources.** The retained radian-bridge audit rules out this periodic-source bin for the rational density route while carrying `2/9` as an arithmetic witness outside that bin.
- **R4 -- determinant-sign pi mechanism.** The standard `exp(i pi eta)` packaging rides the determinant-phase class, and R1 reduces that phase class to `k = 0`.

Bounded conclusion: on this retained registrable carrier surface, every listed class either carries no angle datum, carries the derived `cos(3 delta)` symmetric datum with no primitive multiplicative coefficient, or is ruled out by the retained periodic-source audit. Within this surface, the direct `c = 1` reading is the retained-carrier-compatible member of the rival family. R-eta itself remains the proposed identification that the registered angle equals `L_3(1,2) = 2/9`; this note eliminates the retained-carrier supply of a separate conversion factor.

## The supplied class

The carrier surface is stipulated in-note as the charged-lepton Hermitian circulant

```text
H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T,
```

with real `a`, positive `B`, real `delta`, and `C` the cyclic 3-shift. The theorem below concerns what the retained registrable classes can carry on this supplied surface; it does not derive the physical carrier identification.

## Theorem

**R1 check tag -- determinant characters.** A multiplicative determinant character has phase part `chi_k(z) = exp(i k arg z)`. `K`/CPT conjugation sends `arg z` to `-arg z`, so invariance requires

```text
exp(i k phi) = exp(-i k phi) for all phi.
```

Equivalently `sin(k phi) = 0` for all `phi`, whose linear coefficient at `phi = 0` is `k`; hence `k = 0`. The runner also breaks sample nonzero indices. Thus this class carries no angle datum.

**R2a check tag -- symmetric data.** For the supplied `H(delta)`, the elementary symmetric data are

```text
e_1 = 3a
e_2 = 3a^2 - 3B^2
e_3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta).
```

So the angle-sensitive retained symmetric datum has the form `F(cos(3 delta))`. The `3` is derived by the cyclic orbit and conjugate relabel, as the determinant combines the three cyclic phase factors.

**R2b/R2c check tags -- inversion on the fundamental domain.** On `delta in [0, pi/3]`, `cos(3 delta)` is strictly monotone in the open interval because its derivative is `-3 sin(3 delta) < 0`. Therefore the symmetric datum recovers the magnitude:

```text
|delta| = arccos((e_3 - a^3 + 3 a B^2) / (2 B^3)) / 3.
```

The inversion gives the angle magnitude supplied by the carrier; it does not supply an independent multiplier.

**R2d check tag -- no generic symmetric-data carrier for `cos(3 c delta)`.** At fixed `(a, B) = (1, 1/4)`, values with equal `e_3` have equal `cos(3 delta)`. The runner samples equal-symmetric-data pairs and shows that a non-integer rival, tested with `c = pi`, changes `cos(3 c delta)` across such pairs. Therefore `cos(3 pi delta)` is not a function of the retained symmetric data and cannot be supplied by this class.

The runner also records the integer guard requested by this theorem: `c = 2` is a Chebyshev composite, `cos(6 delta) = 2 cos(3 delta)^2 - 1`. That composite is a post-readout function of the already-carried `cos(3 delta)` and does not add a primitive carrier coefficient. The carrier coefficient remains the derived `3`.

**R3 check tag -- periodic sources.** The radian-bridge audit's retained bin is the periodic phase-source bin: it says such phases have the `q*pi` form, while a nonzero pure rational such as `2/9` is not supplied as a literal radian by a retained periodic phase source. This citation is scope-honest: it rules out the periodic bin and leaves the rational-density route as the separate R-eta readout premise.

**R4 check tag -- determinant-sign pi packaging.** The standard `exp(i pi eta)` form uses the determinant-sign phase carrier. By R1, the determinant-phase character has `k = 0` on the retained registrable surface, so this class supplies no retained pi carrier for a conversion factor.

**Conclusion assembly.** The runner assembles the conclusion from computed booleans: R1 and R4 carry no angle datum, R2 carries the derived `cos(3 delta)` datum and recovers `|delta|`, and R3 is outside the retained periodic-source bin for the rational density. The retained carrier surface supplies the direct reading and no primitive `c != 1` conversion carrier.

## What This Strengthens

The `KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md` E8.3 import accounting moves from "no currently retained pi-source" to this carrier-class statement for the retained registrable surface. The `THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md` determinant-phase diagnostic is reproven here at the class level by the `k = 0` identity.

Both companion notes are context, not dependencies. This note is a source-side bounded theorem claim.

## Does Not

- Does not derive R-eta.
- Does not assert that future readout contexts cannot supply other carriers.
- Does not touch the occupancy dial.
- Does not consume a mass comparator.
- Does not turn the proposed R-eta identification into a retained axiom.
- Does not edit any audit-owned status surface.

## Dependencies

- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
  -- the registrable readout class and the R1/R2 constraint surface.
- [`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
  -- the periodic-source foreclosure used for R3; its bin is periodic `q*pi` sources, and its witness inventory keeps `2/9` outside that bin.
- [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  -- the retained fixed-locus density `L_3(1,2) = 2/9` used by the rival family.
