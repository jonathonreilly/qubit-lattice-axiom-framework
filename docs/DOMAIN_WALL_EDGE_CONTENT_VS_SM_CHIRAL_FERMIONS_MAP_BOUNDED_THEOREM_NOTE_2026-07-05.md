# Domain-Wall Edge Content vs SM Chiral Fermions Map: Bounded Theorem

**Date:** 2026-07-05
**Type:** bounded_theorem
**Claim scope:** an exact finite-dimensional map and obstruction report. The
runner enumerates the landed domain-wall edge content, re-earns the existing
`C^8` chiral-cube `Y` surface, compares that surface to the one-generation
Standard Model left-handed chiral fermion multiset, and reports exact matches
and exact gaps. This is a map, not a derivation of the Standard Model chiral
sector.
**Status authority:** independent audit lane only. This note does not set,
predict, or request an audit status.
**Primary runner:** [`scripts/domain_wall_edge_content_vs_sm_chiral_map_2026_07_05.py`](../scripts/domain_wall_edge_content_vs_sm_chiral_map_2026_07_05.py)
**Runner cache:** [`logs/runner-cache/domain_wall_edge_content_vs_sm_chiral_map_2026_07_05.txt`](../logs/runner-cache/domain_wall_edge_content_vs_sm_chiral_map_2026_07_05.txt)

## Source Context

Current-main posture on 2026-07-07: the Tier-A admitted-input count is zero.
This note does not edit `tier_a_admissions.json`, owner-governed-premise
registries, effective-status surfaces, or either Tier-A retirement record.

The map depends on the landed domain-wall edge diagnostics and respects these
existing boundaries:

- [`DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md`](DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md)
  supplies the free-field domain-wall edge spinor diagnostic.
- [`RECORD_FORMATION_FRONT_IS_THE_DOMAIN_WALL_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md`](RECORD_FORMATION_FRONT_IS_THE_DOMAIN_WALL_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md)
  and
  [`DOMAIN_WALL_EDGE_ANOMALY_INFLOW_SPECTRAL_FLOW_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md`](DOMAIN_WALL_EDGE_ANOMALY_INFLOW_SPECTRAL_FLOW_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md)
  provide the adjacent edge/front and spectral-flow diagnostics used as
  context for the finite map.
- [`CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md)
  supplies the algebraic `Y = (1/3) P_symm - P_antisymm` spectrum on
  `C^8 = (C^2)^{tensor 3}` and explicitly defers the physical Standard Model
  identification bridge.
- [`NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md`](NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md)
  supplies the bounded `6+2` surface and excludes anomaly-complete
  `U(1)_Y`, electroweak matching, matter-completion labels, electric charge,
  and phenomenology.
- [`LEFT_HANDED_CHARGE_MATCHING_NOTE.md`](LEFT_HANDED_CHARGE_MATCHING_NOTE.md)
  makes the scale-free `1:(-3)` ratio load-bearing; the absolute
  normalization is convention-fixed, not derived.
- [`HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md`](HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md)
  prunes the direct `H_unit` scalar-singlet to full EWSB doublet route. This
  note cites that no-go only for that direct route.

## Edge Content

The domain-wall edge content, per wall, is one local Weyl species with a
two-component `Cl(3,0)` Pauli spinor:

```text
species per wall = 1
Cl(3,0) spinor dimension = 2
local edge dimension per wall = 2
```

The runner verifies the Pauli anticommutation relations exactly. It also
enumerates the proper cubic rotation group as the 24 orientation-preserving
signed-permutation rotations, with vector-representation trace distribution

```text
{-1: 9, 0: 8, 1: 6, 3: 1}.
```

The edge spinor is not an ordinary single-valued representation of the proper
cubic group; it is the spin double-cover/projective representation. The runner
checks this directly: four lifted `90 degree` turns give `-I` on the spinor
even though the vector rotation returns to identity.

## Re-Earned Y Surface

On the chiral cube `C^8 = (C^2)^{tensor 3}`, the runner reconstructs the
`b1 <-> b2` swap, the projectors

```text
P_symm = (I + P_swap) / 2,
P_antisymm = (I - P_swap) / 2,
Y = (1/3) P_symm - P_antisymm.
```

It verifies:

```text
rank(P_symm) = 6
rank(P_antisymm) = 2
spec(Y) = {+1/3 with multiplicity 6, -1 with multiplicity 2}
Tr(Y) = 0
ratio = 1:(-3)
```

The taste-cube `S_3` character decomposition is also recomputed:

```text
C^8 = 4 A1 + 2 E.
```

In the base/fiber bookkeeping used by the existing embedding script, this is
the `(3 sym + 1 antisym) x 2 fiber` split.

## SM Target

The comparison target is the one-generation Standard Model left-handed
chiral-fermion multiset in the conventional, non-doubled hypercharge
normalization:

| field | multiplicity | `Y` |
|---|---:|---:|
| `Q` | 6 | `+1/6` |
| `u^c` | 3 | `-2/3` |
| `d^c` | 3 | `+1/3` |
| `L` | 2 | `-1/2` |
| `e^c` | 1 | `+1` |

Total dimension:

```text
15
```

The runner verifies the standard exact anomaly sums:

```text
sum Y        = 0
sum Y^3      = 0
SU(2)^2-U(1) = 0
SU(3)^2-U(1) = 0
SU(3)^3      = 0
```

## Map Result

### Matches

The scale-free `6+2` / `1:(-3)` surface is exactly reproduced. After applying
the conventional factor `1/2` that converts the doubled-framework convention
`(+1/3, -1)` to the target convention, the surface becomes

```text
{+1/6 with multiplicity 6, -1/2 with multiplicity 2}.
```

That is exactly the Standard Model `Q_L + L_L` hypercharge multiset:

```text
Q_L : 6 at +1/6
L_L : 2 at -1/2
```

This is the precise positive match. It is only a left-handed doublet-surface
match, and it uses the existing convention bridge for the absolute factor.

### Gaps / Route No-Gos

The same exact computation names the gaps:

```text
scaled 6+2 surface dimension = 8
SM target dimension          = 15
missing charges              = {-2/3: 3, +1/3: 3, +1: 1}
```

Thus the `6+2` surface does not supply the `u^c`, `d^c`, and `e^c` singlet
content of the target `15`-plet.

The domain-wall edge spinor is also not directly the taste cube:

```text
edge spinor dimension = 2
taste cube dimension  = 8
```

Tensoring the edge spinor with the taste cube gives a `16`-dimensional carrier,
not the requested `15`-plet. That `16` may be relevant to a separate
right-handed-neutrino-inclusive completion discussion, but it is not the
target of this Step 4 map and is not claimed here.

The direct `H_unit -> EWSB doublet representation` route remains pruned. The
runner independently reproduces the representation obstruction:

```text
Hom_SU(2)(1,2) = 0.
```

This is cited only for that direct scalar-singlet-to-doublet route. It is not
a no-go against an already supplied weak-fiber doublet bookkeeping surface.

## Anomaly Cross-Check

For the identified `6+2` subcontent alone, in the target normalization, the
runner computes

```text
sum Y        = 0
sum Y^3      = -2/9
SU(2)^2-U(1) = 0
SU(3)^2-U(1) = 1/6
```

So the matched `Q_L + L_L` surface is not anomaly-complete by itself. The
nonzero `sum Y^3` and `SU(3)^2-U(1)` values are the precise obstruction. The
missing seven singlet states are exactly the SM anomaly-completing charges:

```text
u^c : 3 at -2/3
d^c : 3 at +1/3
e^c : 1 at +1
```

This is a bounded partial map with named residuals, not a full chiral-sector
derivation.

## No-Go Discipline Gate

Review-loop current-main check on 2026-07-07 used the fresh no-go discipline
skill body from `origin/main`. The gate below covers the route-specific
negative statements in this note; no universal Standard Model, electroweak, or
hypercharge no-go is shipped.

**N1 - Alternative route enumeration.**

1. Direct edge-spinor to taste-cube route. ATTEMPTED. It fails as a direct
   identification because the computed dimensions are `2` and `8`.
2. Edge-spinor tensor taste-cube route. ATTEMPTED. It gives `16` states, not
   the requested SM `15`-plet.
3. `6+2` Y-surface to full SM route. ATTEMPTED. It matches only `Q_L + L_L`;
   the exact missing multiset is `{-2/3:3, +1/3:3, +1:1}`.
4. Direct `H_unit` to EWSB doublet route. RULED OUT BY PRIOR and rechecked.
   The HUNIT no-go and this runner both give `Hom_SU(2)(1,2)=0`.
5. Anomaly-completion from the identified `6+2` subcontent alone. ATTEMPTED.
   It fails exactly because `sum Y^3 = -2/9` and `SU(3)^2-U(1)=1/6`.

**N2 - Wall-independence audit.**

Collapsed walls are: the spin-edge to taste-cube bridge, the missing singlet
completion, the absolute-normalization convention, and the direct HUNIT route.
The first does not close the second, because even a supplied taste cube gives
only the `6+2` surface. The second does not close the first, because singlet
anomaly completion does not identify the domain-wall edge spinor with `C^8`.
The normalization convention does not close either structural carrier wall.
The HUNIT wall is route-specific and does not imply the matter-content gaps.

**N3 - Hidden-wall scan.**

Potential hidden-wall phrases are made explicit: "bridge" is the edge/taste
and physical-SM identification bridge; "convention" is the factor `1/2`
normalization bridge; "background" is not load-bearing here. No hidden
admission is left implicit.

**N4 - Residual matching.**

The
[`HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md`](HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md)
is cited only against the residual it actually attacks:
`H_unit scalar singlet -> full EWSB doublet`. The
[`CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md)
is cited only for the physical Standard Model identification bridge gap it
explicitly names.
[`LEFT_HANDED_CHARGE_MATCHING_NOTE.md`](LEFT_HANDED_CHARGE_MATCHING_NOTE.md)
is cited only for the scale-free-ratio versus absolute-normalization boundary.

**N5 - Rhetoric audit.**

The negative claims are at narrow resolutions: dimension mismatch `2 != 8`,
dimension mismatch `16 != 15`, multiset mismatch `8 != 15`, nonzero anomaly
sums on the `6+2` subcontent, and `Hom_SU(2)(1,2)=0` for the HUNIT route. No
global "no SM", "no electroweak", or "no hypercharge" claim is made.

**N6 - Partial-closure path scan.**

Partial closure paths remain open: a separate retained edge-to-taste bridge
could close the carrier wall; the existing one-generation completion notes can
provide singlets conditionally; accepting the conventional normalization fixes
the absolute factor; and a supplied electroweak doublet surface remains usable
despite the HUNIT direct-route no-go.

**N7 - Steelman.**

A hostile reviewer could argue that once the `C^8` taste cube is supplied as an
independent internal degeneracy on the edge, the `6+2` surface already matches
the physical `Q_L + L_L` sector exactly in the conventional normalization.
This note agrees with that partial steelman. The remaining issue is not the
`6+2` arithmetic; it is the absent domain-wall edge-to-taste bridge and the
missing anomaly-completing singlet sector.

**N8 - Cross-cycle echo.**

The same bridge shapes are already named in adjacent notes: the
[`CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md`](CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md)
names the physical-identification bridge; the one-generation matter-closure
notes provide conditional singlet completion; and the
[`HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md`](HUNIT_TO_EWSB_DOUBLET_REPRESENTATION_NO_GO_NOTE_2026-06-15.md)
preserves the supplied-doublet route while pruning only the direct
scalar-singlet route. This map does not retire those walls; it records them
precisely.

**Gate status:** PASS for the narrowed partial map and named route no-gos.
No universal no-go is shipped.

## What Is Shown

- The domain-wall edge content is one two-component `Cl(3,0)` Weyl spinor per
  wall, with a projective/double-cover cubic spin action.
- The `C^8` chiral-cube `Y` surface is re-earned exactly as
  `{+1/3 x6, -1 x2}`, with scale-free ratio `1:(-3)`.
- After the conventional factor `1/2`, that `6+2` surface matches exactly the
  SM `Q_L + L_L` hypercharge multiset.
- The full SM `15`-plet is not supplied: the exact missing states are
  `u^c`, `d^c`, and `e^c`.
- The matched `6+2` subcontent is not anomaly-complete by itself.

## What Is Not Shown

- This does not derive the Standard Model chiral sector.
- The electroweak doublet representation is not obtained via the direct
  HUNIT route; the HUNIT no-go is respected.
- The absolute hypercharge normalization is a convention bridge, not derived.
- Anomaly-complete `U(1)_Y`, electric charge, and full matter completion are
  not claimed.
- The spin-edge to taste-cube bridge is a named gap, not a match.
- The dimensional interpretation of record-time remains open.
- No strong-CP or theta claim is made.
- No import, axiom, audit status, closure, exhaustion claim, only-route claim,
  or discharge claim is made.

## Validation

Run:

```bash
python3 scripts/domain_wall_edge_content_vs_sm_chiral_map_2026_07_05.py
```

Observed terminal summary:

```text
TOTAL: PASS=23 FAIL=0
```
