# Zero-Import Hydrogen: Lepton `1/256` Tensor-Lift Firewall

**Date:** 2026-07-04
**Type:** partial-narrowing firewall note
**Claim type:** meta / tensor-lift boundary support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_tensor_lift_firewall.py`

## Scope

This note attacks residual A1 from
`ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md`:

```text
A1 | Tensor lift: prove the charged-lepton scalar block carries one
     M_2(C) factor per OS0 regulator slot.
```

The OS0 repair supplies the four-slot regulator geometry:

```text
Z^3 x Z_tau,  dim_C(M_2(C)^tensor4) = 4^4 = 256.
```

This note checks the next question: does that four-slot algebra actually lift
onto the charged-lepton scalar source, rather than staying a regulator
bookkeeping count?

## Existing Lepton Block Anchor

The D17-prime lepton scalar-singlet note supplies a different and already-used
normalization:

```text
H_unit^lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R
Z_lep^2 = N_c * N_iso = 1 * 2 = 2.
```

That is the ordinary unit normalization of the charged-lepton scalar block.
It accounts for the `1/sqrt(2)` factor in the lepton-scale frontier formula:

```text
y_scale = g_2 * (1/sqrt(2)) * S_l
S_l     = 1/256.
```

Therefore A1 cannot be closed by reusing D17-prime alone. D17 gives the scalar
singlet and its two-component weak-isospin normalization; A1 needs an
additional theorem attaching the OS0 `M_2(C)^tensor4` carrier to the same
charged-lepton scalar coefficient.

## Ordinary Tensoring Is Not Enough

A tempting shortcut is:

```text
D17 lepton block count      = 2
OS0 M_2(C)^tensor4 count    = 256
direct tensor product count = 2 * 256 = 512.
```

But ordinary unit-amplitude normalization over the direct product gives

```text
1/sqrt(512) = (1/sqrt(2)) * (1/16),
```

while the hydrogen lane needs

```text
(1/sqrt(2)) * (1/256).
```

The shortcut overshoots the needed suppressed coefficient by a factor of `16`.
So even a literal `D17 x M_2(C)^tensor4` tensor product would not by itself
produce the target lepton-scale factor unless a separate density,
determinant, volume, Schur, or operator-normalization theorem selects the
reciprocal count `1/N` instead of unit-amplitude `1/sqrt(N)`.

That is why A1 and A2 remain separate:

| residual | content |
|---|---|
| A1 tensor lift | attach the four OS0 `M_2(C)` factors to the charged-lepton scalar source |
| A2 readout rule | prove those factors contribute as `1/N = 1/256`, not `1/sqrt(N) = 1/16` |

## Tensor-Lift Theorem Shape

A future positive theorem has to prove all of the following without consuming
the empirical `m_W/256` comparator:

| item | required content |
|---|---|
| T1 carrier attachment | the charged-lepton scalar source actually carries one `M_2(C)` factor for each OS0 regulator slot |
| T2 sector specificity | the lift is a charged-lepton scalar suppression, not a universal regulator factor or a neutrino/top/quark coefficient |
| T3 D17 compatibility | the D17 `1/sqrt(2)` unit normalization remains the block anchor and is not double-counted |
| T4 readout compatibility | the lift leaves room for the A2 density/determinant/Schur readout that supplies `1/256` |

Current retained and primitive surfaces do not yet supply this theorem. The
minimal axioms supply the one-site `M_2(C)` possibility domain; the
kinetic-isotropy primitive supplies the OS0 regulator geometry; D17-prime
supplies the charged-lepton scalar singlet. None of those sources alone says
that the lepton scalar coefficient is tensor-enriched over the four OS0 slots.

The follow-up support note
`ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md`
settles the finite carrier arithmetic under a sharper conditional: if the
charged-lepton scalar source is a full OS0-cell linear source over the four
local qubit-slot algebras, then the carrier is `M_2(C)^tensor4` with `256`
matrix-unit coordinates. It does not derive that full-cell source locality or
the charged-lepton sector attachment.

The follow-up support note
`ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md`
settles the finite D17-compatibility arithmetic under another conditional: if
the full-cell carrier is supplied as a scalar source multiplier on the stated
D17 charged-lepton block, the D17 `1/sqrt(2)` normalization separates from the
`256` source weights. It does not derive the physical source attachment or the
A2 source-density readout.

## Open PR Alignment

Open PRs were checked on 2026-07-04 for tensor-lift movement:

| PR | effect on A1 |
|---|---|
| `#4925` presentation-gauge axis-sign flips | New orientation/gauge-section context for admissibility. It does not attach OS0 `M_2(C)` factors to the charged-lepton scalar source. |
| `#4922` Born form via composite Gleason | Conditional frame-function/Born bridge; useful normalization context, but not a charged-lepton tensor-lift theorem. |
| `#4924` graded-constraint interface | Repaired conditioning-form interface; may support later readout work, but does not prove A1. |
| `#4903` D4 kinetic pattern dichotomy | Relevant because it studies per-direction algebra-dimension patterns, but it is unmerged, selector-undecided, and not a lepton scalar source lift. |
| `#4902`, `#4906` Koide occupancy/phase stack | Keep readout/registrability questions open; they do not provide a charged-lepton `M_2(C)^tensor4` carrier theorem. |

## Lane Consequence

Route A has now been narrowed twice:

```text
A0 geometry slots: repaired by kinetic_isotropy_primitive.
A1 tensor lift: narrowed; full-cell source locality would give the carrier.
A2 reciprocal readout: still open; ordinary normalization gives 1/16.
A3 precision correction: still open; exact 256 is not 256.08.
```

The A3 precision firewall
`ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md`
quantifies this last residual: exact `256` would still need a downstream
correction `C_A3 = 0.999678091...`, or a direct derivation of the noninteger
divisor `256.082435...`.

The next positive attempt should be a theorem of the following kind:

```text
charged-lepton scalar source
  -> four OS0 M_2(C) carrier factors
  -> independent density/determinant/Schur readout
  -> S_l = 1/256
```

Without the first arrow, `4^4 = 256` remains a regulator-side count. Without
the second arrow, even a tensor lift gives the wrong normalization class.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the tensor-lift route is
impossible" is **not** shipped. The narrowed claim is: current retained and
primitive surfaces do not by themselves lift `M_2(C)^tensor4` onto the
charged-lepton scalar coefficient; an A1 carrier theorem remains required.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| D17 scalar alone | Use the existing charged-lepton scalar-singlet theorem. | ATTEMPTED. It gives `1/sqrt(2)`, not four `M_2(C)` factors. |
| OS0 slot tensor | Use `Z^3 x Z_tau` to count four regulator slots. | PARTIAL POSITIVE. It supplies the geometry count `4^4 = 256`, not the lepton carrier attachment. |
| direct `D17 x M_2(C)^tensor4` unit normalization | Tensor the D17 block with the four-slot count and unit-normalize all components. | ATTEMPTED. It gives `(1/sqrt(2))*(1/16)`, not `(1/sqrt(2))*(1/256)`. |
| determinant/density lift | Attach the four-slot carrier and read it by determinant or volume density. | OPEN. This is the right shape, but the carrier theorem and A2 readout theorem are not supplied here. |
| D4 per-direction pattern | Use the open D4 kinetic-pattern PR as a source for per-direction algebra dimension. | OPEN/UNMERGED. It is selector-undecided and not a charged-lepton scalar source theorem. |
| Schur `/64` route | Avoid tensor lift by deriving a charged-lepton Schur carrier. | OPEN parallel route; handled by the Schur two-scale firewall. |
| empirical `m_W/256` route | Use the observed relation directly. | RULED OUT AS ZERO-IMPORT ROUTE: comparator/open gate, not derivation. |

### N2 - Wall-independence audit

| pair | closes automatically? | conclusion |
|---|---|---|
| T1 carrier attachment <-> T2 sector specificity | no in either direction | independent |
| T1 carrier attachment <-> T3 D17 compatibility | no in either direction | independent |
| T1 carrier attachment <-> T4 readout compatibility | no in either direction | independent |
| T2 sector specificity <-> T3 D17 compatibility | no in either direction | independent |
| T2 sector specificity <-> T4 readout compatibility | no in either direction | independent |
| T3 D17 compatibility <-> T4 readout compatibility | no in either direction | independent |

Proving that four factors attach does not prove that they attach only to the
charged-lepton scalar. Proving sector specificity does not prove the ordinary
D17 normalization is preserved. Proving the tensor lift does not choose the
reciprocal readout.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `tensor` / `lift` | explicit T1 carrier-attachment wall. |
| `charged-lepton` | explicit T2 sector-specificity wall. |
| `normalization` | D17 anchor if `1/sqrt(2)`; explicit T3/T4 wall otherwise. |
| `density` / `determinant` / `Schur` | partial-closure path, not established premise. |
| `primitive` / `registered` | registry checked; approved primitives are bounded to their declared content. |
| `empirical` | comparator role only, not proof input. |

No hidden tensor-lift or readout rule is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md` | A0 geometry slots and A1-A3 residual split | yes |
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | charged-lepton scalar singlet and `1/sqrt(2)` normalization | yes as block anchor, no as tensor lift |
| `M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md` | finite `4^4 = 256` count with explicit `d=4` parameter | partial: count only |
| `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | OS0 `Z^3 x Z_tau` geometry | yes for slots only |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md` | A2 readout ambiguity | parallel guard, not A1 closure |
| `LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md` | structural base/exponent/precision status | yes for target, not carrier theorem |

No cited surface is counted as proving the charged-lepton tensor lift.

### N5 - Rhetoric audit

The note avoids saying "the tensor lift cannot be derived." The tested claim
is narrower:

| resolution | tested? | outcome |
|---|---|---|
| finite OS0 count | yes | `N=256` is exact. |
| D17 scalar block | yes | unit normalization is `1/sqrt(2)`. |
| direct ordinary tensor normalization | yes | gives `1/(16 sqrt(2))`, not target. |
| physical charged-lepton carrier theorem | not closed | named T1/T2. |
| all future determinant, density, Schur, or operator routes | not closed | left open. |

### N6 - Partial-closure path scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained source/action theorem attaching OS0 slots to the charged-lepton scalar coefficient | T1 carrier attachment |
| sector-specific scalar theorem distinguishing charged leptons from top/quark/neutrino blocks | T2 sector specificity |
| determinant/log-volume theorem preserving D17 normalization while adding `1/N` | T3 plus T4 |
| charged-lepton Schur carrier theorem with two-scale split | parallel Route B closure |
| future use of merged D4 kinetic-pattern work plus a lepton scalar bridge | possible support for T1, not current closure |

These are import-retirement paths, not new axioms. The artifact is therefore a
firewall, not a no-go.

### N7 - Steelman

A hostile reviewer can argue that the route is nearly closed: the Qubit axiom
supplies `M_2(C)` at each site, kinetic isotropy supplies four OS0 slots, and
D17 supplies the local charged-lepton scalar source. If a scalar source is a
local object evaluated over the OS0 regulator block, then the natural carrier
is exactly `M_2(C)^tensor4`, and the desired `1/256` is its density. That is
the strongest positive route. The rebuttal is that each italicized step is
precisely what must be proved: local scalar source to OS0 tensor carrier,
charged-lepton sector specificity, and density rather than amplitude readout.

### N8 - Cross-cycle echo

This mirrors earlier Koide and Yukawa campaigns: finite counts, scalar
singlets, or candidate carriers often landed before the physical source/readout
bridge. D17 supplies the scalar singlet; OS0 supplies the four slots; the
current lane must not fuse them without the missing carrier theorem.

**Gate result:** broad no-go fails; narrowed tensor-lift firewall passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar block carries
  `M_2(C)^tensor4`.
- No derivation that ordinary tensor-product normalization is the lepton
  suppression.
- No derivation of a determinant, density, volume, Schur, or
  operator-normalization readout theorem.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_tensor_lift_firewall.py
```

The verifier checks the D17 normalization boundary, the OS0 finite count, the
direct tensor-product normalization mismatch, open-PR alignment, the no-go
discipline section, and the explicit non-claims.
