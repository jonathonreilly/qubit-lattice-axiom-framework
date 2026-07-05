# Zero-Import Hydrogen: Lepton `1/256` Reciprocal-Readout Firewall

**Date:** 2026-07-04
**Type:** partial-narrowing firewall note
**Claim type:** meta / readout-boundary support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_reciprocal_readout_firewall.py`

## Scope

This note attacks residual A2 from
`ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md`:

```text
A2 | Reciprocal readout: prove 1/dim_C(M_2(C)^tensor4) is the
     charged-lepton scale suppression S_l.
```

The OS0 repair improves the geometry count:

```text
dim_C(M_2(C)^tensor4) = 4^4 = 256.
```

This note checks the next question: what readout turns that count into a
Yukawa suppression?

## Existing Normalization Anchor

The lepton-scale probe already separates the charged-lepton scale into

```text
y_scale = g_2 * (1/sqrt(2)) * S_l
S_l     = 1/256.
```

The `1/sqrt(2)` factor is not missing. It is the lepton block-dimension
normalization from the D17-prime scalar-singlet block:

```text
H_unit^lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R,
Z_lep^2 = N_c * N_iso = 1 * 2 = 2.
```

So A2 is not asking for the ordinary unit normalization of the lepton scalar
block. That part is already accounted for. A2 asks for an **additional**
suppression factor `S_l = 1/256`.

## Readout Ambiguity

Even if A1 were granted, a four-slot `M_2(C)` tensor count does not by itself
select the reciprocal-dimension readout:

| readout class | value from `N = 4^4 = 256` | hydrogen-lane effect |
|---|---:|---|
| unit-amplitude normalization over `N` modes | `1/sqrt(N) = 1/16` | overshoots `S_l` by `16x` |
| volume/density reciprocal | `1/N = 1/256` | matches the target `S_l` |
| D17-prime lepton block normalization | `1/sqrt(2)` | already present as the block anchor, not the missing suppression |
| empirical `m_W/256` readout | `1/256` by comparator | not zero-import |

The target is therefore sharper than "find `256`." It is:

```text
derive the physical readout rule that makes the four-slot count enter
as a density/volume reciprocal 1/N rather than an amplitude normalization
1/sqrt(N), and prove that this readout is the charged-lepton S_l.
```

The follow-up discriminator
`ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md`
narrows the A2 readout rule further. Since
`M_2(C)^tensor4 ~= M_16(C)`, projection/Born trace on a rank-one event gives
`1/16`, while algebra-basis coefficient density over the `16^2 = 256`
matrix-unit coordinates gives `1/256`. The latter matches `S_l`, but still
needs a charged-lepton source-measure theorem.

## Primitive Boundary

The primitive registry was checked. The relevant approved premise nodes do not
decide this readout:

| node | what it supplies | what it does not supply here |
|---|---|---|
| `minimal_axioms` | `Z^3`, one-site `M_2(C)`, admissibility, record additivity | weighting, normalization, probability, source/action bridge, physical observable bridge |
| `kinetic_isotropy_primitive` | OS0 `Z^3 x Z_tau`, `c_t = c_s` geometry | selector, readout bridge, normalization rule, mass ratio, empirical match |
| `scale_reference_primitive` | one dimensionful ruler | dimensionless physics or `S_l` |
| `realized_state_primitive` | pointwise realized-state evaluation | state content, weighting, normalization rule, or value |

This is why the OS0 repair is real progress but not a scale derivation.

The paired A1 tensor-lift firewall
`ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md`
checks the preceding carrier question. Even a direct `D17 x M_2(C)^tensor4`
unit normalization would give `(1/sqrt(2))*(1/16)`, so A2 remains the separate
readout theorem that must select a reciprocal/density factor.

The A3 precision firewall
`ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md`
checks the following precision question. A2 can at most select exact
`1/256`; it does not explain the repo comparator divisor `256.082435...`.

## Open PR Alignment

Open PRs were checked on 2026-07-04 for normalization/readout movement:

| PR | effect on A2 |
|---|---|
| `#4922` Born form via composite Gleason | Conditional on full projection-lattice frame-function hypotheses; not merged and not a charged-lepton `1/N` readout theorem. |
| `#4924` graded-constraint interface | Repairs the frame-function interface to a conditioning form; useful context for future projection/Born work, but not a retained Lane 6 matrix-unit source-density rule. |
| `#4927` record-comparability block02 | Fresh comparability/conditional chain-arrow context. Its boundary supplies no probability or weight, so it does not close A2. |
| `#4903` D4 kinetic pattern dichotomy | Gives a bounded per-direction algebra-dimension pattern on a kinetic surface; selector bit remains undecided and it does not identify `1/dim_C(M_2(C)^tensor4)` with `S_l`. |
| `#4902`, `#4905`, `#4906` Koide stack | Keep occupancy, slot, and phase-readout questions open; they do not supply the reciprocal readout here. |

## Lane Consequence

Route A now has this dependency split:

| wall | current best status |
|---|---|
| A0 geometry slots | improved: OS0 primitive supplies the four regulator slots |
| A1 tensor lift | open: prove the charged-lepton scalar block carries the four `M_2(C)` factors |
| A2 readout rule | narrowed: prove a coefficient/source-measure theorem selecting algebra-basis density `1/256`, not projection/Born trace `1/16` |
| A3 precision correction | open: account for `256.08` versus exact `256` |

The next positive target is not another integer count. It is a retained
readout theorem: a determinant, density, Schur, or operator-normalization
argument that picks `1/N` and identifies it with the charged-lepton scale
suppression.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "reciprocal readout is
impossible" is **not** shipped. The narrowed claim is: current retained and
primitive surfaces do not by themselves turn `dim_C(M_2(C)^tensor4)=256` into
the charged-lepton suppression `S_l`; a readout theorem remains required.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| volume reciprocal | Read the four-slot count as `1/N = 1/256`. | ATTEMPTED. It matches `S_l`, but the physical readout rule is the missing A2 premise. |
| unit-amplitude normalization | Normalize one equal-amplitude vector over `N=256` modes. | ATTEMPTED. Gives `1/sqrt(N)=1/16`, showing the count alone is ambiguous. |
| projection/Born trace | Read `M_2(C)^tensor4 ~= M_16(C)` as a rank-one projection event. | ATTEMPTED. Gives `1/16`, so a projection theorem alone does not deliver the target source density. |
| D17-prime scalar normalization | Use the charged-lepton block's unit singlet normalization. | RULED OUT AS COMPLETE SUPPRESSION ROUTE. It gives the existing `1/sqrt(2)` anchor, not the extra `1/256`. |
| determinant/log-volume route | Treat the four-slot tensor block as a determinant or density object. | OPEN. This is the right shape for `1/N`, but no retained charged-lepton determinant readout is supplied here. |
| Schur `/64` route | Use `g_2^2|_lattice/64 = 1/256`. | OPEN parallel route; it needs the charged-lepton Schur carrier and two-scale split from the Schur firewall. |
| realized-state route | Let the realized state pick the readout. | RULED OUT AS ZERO-IMPORT ROUTE: the realized-state primitive supplies evaluation only, no weighting or normalization rule. |
| empirical `m_W/256` route | Use the observed scale relation directly. | RULED OUT AS ZERO-IMPORT ROUTE: comparator/open gate, not derivation. |

### N2 - Wall-independence audit

| pair | closes automatically? | conclusion |
|---|---|---|
| A1 tensor lift <-> A2 readout rule | no in either direction | independent |
| A1 tensor lift <-> A3 precision correction | no in either direction | independent |
| A2 readout rule <-> A3 precision correction | no in either direction | independent |

Granting four carried tensor factors does not choose `1/N` over
`1/sqrt(N)`. Choosing `1/N` does not prove the charged-lepton scalar block
carries the factors. Exact `256` still does not explain `256.08`.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `normalization` | explicit A2 wall unless citing D17-prime's `1/sqrt(2)` block anchor. |
| `reciprocal` | explicit readout claim, not automatic from a count. |
| `determinant` / `density` | possible partial-closure path; not used as an established premise. |
| `primitive` / `registered` | registry checked; primitives are bounded to their declared content. |
| `empirical` | comparator role only, not proof input. |

No hidden readout rule is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md` | A0 geometry and A1-A3 residual split | yes |
| `LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md` | factorization into `g_2`, `1/sqrt(2)`, and `1/256` | yes |
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | lepton block `1/sqrt(2)` normalization | yes, as contrast |
| `M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md` | finite `4^4=256` count | partial: count only |
| `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | realized-state evaluation boundary | guard only |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md` | projection/Born trace versus matrix-unit coefficient density | yes |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md` | Schur `/64` route walls | parallel, not A2 closure |

No cited count is treated as a readout theorem.

### N5 - Rhetoric audit

The note avoids saying "`1/256` is not derivable." The tested claim is
narrower:

| resolution | tested? | outcome |
|---|---|---|
| finite count | yes | `N=256` is exact. |
| unit-amplitude normalization | yes | gives `1/16`, not `1/256`. |
| projection/Born trace on `M_16(C)` | yes | rank-one projection gives `1/16`, not matrix-unit density. |
| volume/density reciprocal | yes | gives the target `1/256`. |
| physical charged-lepton readout theorem | not closed | named A2. |
| all future determinant or Schur routes | not closed | left open. |

### N6 - Partial-closure path scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained determinant/log-volume theorem for the charged-lepton scalar block | A2 readout as `1/N` |
| retained density/readout bridge from OS0 tensor slots to `S_l` | A1 plus A2 |
| charged-lepton Schur carrier with derived `/64` and two-scale split | parallel Route B closure |
| precision correction theorem from exact `256` to `256.08` | A3 |

These are not new axioms if derived as ordinary theorem work or as
import-retirement audits. The artifact is therefore a firewall, not a no-go.

### N7 - Steelman

A hostile reviewer can argue that the word "scale suppression" already means a
density or volume factor, not an amplitude. In that reading, once OS0 supplies
four `M_2(C)` slots, the natural scalar-suppression object is exactly
`1/dim_C(M_2(C)^tensor4) = 1/256`; `1/sqrt(N)` belongs to state-vector
normalization, not a Yukawa coefficient. That is the strongest positive route.
The rebuttal is that this is precisely the missing A2 theorem: the repo needs
to show that the charged-lepton scalar coefficient uses the density/volume
readout, rather than asserting it from the word "suppression."

### N8 - Cross-cycle echo

This mirrors earlier Koide and normalization campaigns: exact finite counts
and native structures often exist before the physical readout rule is fixed.
The current lane should preserve that split. OS0 supplies the count's fourth
slot; D17 supplies the lepton block's ordinary unit normalization; neither
alone supplies the extra `1/256` readout.

**Gate result:** broad no-go fails; narrowed reciprocal-readout firewall
passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that reciprocal dimension is a Yukawa suppression.
- No derivation of the charged-lepton tensor lift.
- No derivation of a determinant, density, or volume readout theorem.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_reciprocal_readout_firewall.py
```

The verifier checks the readout arithmetic, the D17-prime normalization
boundary, the primitive-registry boundary, the no-go discipline section, and
the explicit non-claims.
