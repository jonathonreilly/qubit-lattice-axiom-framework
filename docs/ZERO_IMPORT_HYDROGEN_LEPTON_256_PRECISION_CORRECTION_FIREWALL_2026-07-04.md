# Zero-Import Hydrogen: Lepton `1/256` Precision-Correction Firewall

**Date:** 2026-07-04
**Type:** partial-narrowing firewall note
**Claim type:** meta / precision-boundary support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_precision_correction_firewall.py`

## Scope

This note attacks residual A3 from the zero-import hydrogen lepton-scale route:

```text
A3 | Precision correction: account for the empirical divisor 256.08 versus
     exact 256.
```

The A0-A2 route notes have already separated the integer target from the
carrier and readout gates:

```text
dim_C(M_2(C)^tensor4) = 4^4 = 256
S_l target             = 1/256
```

This note checks the precision residual: if a future theorem derives exact
`256`, what still has to explain the repo's empirical open-gate target?

## Comparator Arithmetic

Using the same repo constants as
`LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md`:

```text
a_lepton^2      = 313.8411267023086 MeV
m_W / 256       = 313.9421875000000 MeV
empirical N     = m_W / a_lepton^2 = 256.08243522600384
relative offset = N/256 - 1 = 0.0003220126015774927
                = +0.03220126015774927 percent
```

The multiplicative correction needed after an exact-`256` theorem is therefore

```text
C_A3 = 256 / N = 0.9996780910571587
1 - C_A3 = 0.0003219089428413424.
```

Equivalently, exact `256` would put the `m_W/256` scale high by
`0.10106079769138887 MeV` relative to `a_lepton^2`. In the `m_W` direction,
the exact-`256` value would correspond to

```text
m_W(exact 256) = 256 * a_lepton^2 = 80343.328435791 MeV,
```

which is `25.87156420899555 MeV` below the repo comparator `m_W = 80369.2 MeV`,
or about `1.945` times the quoted `m_W` uncertainty used by the structural
probe. The repo's current precision statement is therefore not "exact 256";
it is "a sharp empirical target near 256.08, with 256 as a low-look-elsewhere
integer nearby."

## Candidate Correction Classes

The needed correction is small but not zero:

```text
epsilon_A3 = 0.0003220126.
```

Useful scale comparisons:

| candidate scale | value | A3 consequence |
|---|---:|---|
| required `epsilon_A3` | `0.0003220126` | target |
| `alpha(0) / pi` | `0.0023228195` | about `7.2x` too large |
| `alpha(0) / (8 pi)` | `0.0002903524` | numerically nearby but denominator choice is unproved |
| `g_2(v)^2 / (16 pi^2)` | `0.0026988213` | about `8.4x` too large |
| `g_2(v)^2 / (64 pi^2)` | `0.0006747053` | about `2.1x` too large |
| `y_tau^2 / (16 pi^2)` | `0.0000006596` | about `488x` too small |
| `m_e / m_mu` | `0.0048363317` | about `15x` too large |
| `m_mu / m_tau` | `0.0594635343` | about `185x` too large |

These comparisons are not derivations. They only locate the correction scale:
ordinary one-loop electroweak factors are generally too large, the `8 pi`
subdivision is close but unmotivated, and simple charged-lepton mass ratios
are not the right size.

## What A3 Must Prove

A retained A3 closure has two possible shapes:

| route | theorem shape |
|---|---|
| correction-on-exact-256 | derive exact `S_l = 1/256`, then derive a downstream multiplicative correction `C_A3 = 0.999678091...` for the lepton-scale comparator |
| direct-noninteger divisor | derive the physical divisor `N = 256.082435...` directly, with exact `256` appearing only as the nearest structural integer |

Either route must keep the zero-import boundary: no PDG `m_W`, no observed
charged-lepton masses, and no fitted `a_lepton` may be used as proof inputs.

## Relation To A1 And A2

A3 is independent of the two preceding residuals:

| residual | current state |
|---|---|
| A1 tensor lift | `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` pins the missing carrier theorem |
| A2 reciprocal readout | `ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md` pins the missing `1/N` readout theorem |
| A3 precision correction | this note pins the remaining `256.08` versus exact `256` theorem |

Closing A1 and A2 would make exact `1/256` meaningful as a lepton-scale
suppression, but it would not by itself explain why the empirical open-gate
divisor is `256.082435...`. Conversely, an A3 correction formula would not
prove the charged-lepton carrier or readout.

## Open PR Alignment

Open PRs were checked on 2026-07-04 for precision-correction movement:

| PR | effect on A3 |
|---|---|
| `#4926` Tier-A elimination block01 no-go hygiene | New record-formation/Tier-A hygiene context. It does not supply a lepton-scale precision correction or retire `AC_phi_lambda`/`theta`. |
| `#4925` presentation-gauge axis-sign flips | Orientation/gauge-section context; no lepton-scale divisor correction. |
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | Conditional normalization context; no numerical A3 correction. |
| `#4903` D4 kinetic pattern dichotomy | Potential support for future tensor-lift structure, but no `256.0824` correction theorem. |
| `#4902`, `#4905`, `#4906` Koide stack | Readout/phase/occupancy surfaces remain open; no scale precision closure. |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the precision correction
cannot be derived" is **not** shipped. The narrowed claim is: current retained,
primitive, and open-PR surfaces do not by themselves explain the difference
between exact `256` and the empirical open-gate divisor `256.082435...`; a
precision theorem remains required.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| exact-256 route | Treat `1/256` as exact and ignore the offset. | ATTEMPTED. The repo comparator prefers `N=256.082435...`; exact `256` is about `1.945 sigma_mW` away. |
| multiplicative correction | Derive `C_A3 = 256/N = 0.999678091...` after exact `256`. | OPEN. This is a valid route shape, but no retained correction theorem is supplied here. |
| direct noninteger divisor | Derive `N=256.082435...` directly. | OPEN. This would close A3, but it must avoid fitting observed masses or `m_W`. |
| electroweak loop-size route | Use a loop factor as the correction. | ATTEMPTED AS SCALE CHECK. Common loop factors are the wrong size or require unproved denominators. |
| running/threshold route | Let electroweak or lepton-threshold running supply the small offset. | OPEN. Plausible in shape, but no retained charged-lepton scale-running law is supplied here. |
| Koide phase or species-readout route | Move the offset into phase/species readout rather than scale. | OPEN parallel route; K1-K3 remain separate hydrogen blockers. |
| empirical `m_W/256` route | Use observed `m_W` and charged-lepton masses directly. | RULED OUT AS ZERO-IMPORT ROUTE: comparator/open gate, not a derivation. |

### N2 - Wall-independence audit

| pair | closes automatically? | conclusion |
|---|---|---|
| A1 tensor lift <-> A3 precision correction | no in either direction | independent |
| A2 readout rule <-> A3 precision correction | no in either direction | independent |
| Koide phase/species readout <-> A3 precision correction | no in either direction | independent |
| alpha-running threshold derivation <-> A3 precision correction | no in either direction | independent |

Exact carrier and readout theorems would not explain the noninteger divisor.
Likewise a precision correction formula would not prove the carrier, readout,
or electron branch.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `exact 256` | structural integer target only; precision offset remains explicit A3. |
| `empirical` / `comparator` | proof-input boundary; not used as a derivation. |
| `correction` / `running` / `threshold` | possible closure path; not established premise. |
| `primitive` / `registered` | registry checked; approved primitives supply no mass ratio, coupling correction, selector, readout bridge, or empirical match. |
| `m_W` / `a_lepton` | comparator quantities only in this note. |

No hidden precision-correction theorem is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md` | exact `256` versus `256.08` precision residual | yes |
| `LEPTON_MASS_SCALE_MW_OVER_256_EMPIRICAL_OPEN_GATE_NOTE_2026-05-26.md` | empirical `m_W/256` open gate | yes as target, not proof |
| `M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md` | exact finite `4^4 = 256` count | partial: integer only |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | A1 carrier theorem | guard only, not A3 |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md` | A2 readout theorem | guard only, not A3 |
| `axiom_premise_nodes.json` | primitive boundary | guard only |

No cited integer-count surface is counted as explaining the precision offset.

### N5 - Rhetoric audit

The note avoids saying "`256` is wrong" or "no correction exists." Tested
resolutions:

| resolution | tested? | outcome |
|---|---|---|
| exact integer count | yes | `4^4 = 256` is exact. |
| empirical open-gate divisor | yes | `N = 256.082435...`. |
| required correction magnitude | yes | `C_A3 = 0.999678091...`. |
| simple loop/mass-ratio scale comparisons | yes | scale location only, no theorem. |
| all future running, threshold, determinant, or phase corrections | not closed | left open. |

### N6 - Partial-closure path scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained finite correction theorem multiplying exact `1/256` by `C_A3` | A3 correction-on-exact-256 |
| retained noninteger divisor theorem deriving `256.082435...` directly | A3 direct route |
| charged-lepton scale-running theorem with controlled threshold offset | A3 via running |
| Koide/readout theorem showing the apparent scale offset belongs to phase/species assignment | parallel K1-K3/A3 interface |

These are import-retirement paths, not new axioms. The artifact is therefore a
firewall, not a no-go.

### N7 - Steelman

A hostile reviewer can argue that a `0.032%` offset is exactly the size one
should expect after deriving a clean structural integer: exact `256` is the
bare lattice suppressor, while the repo comparator uses physical pole
quantities. Under that reading, the required `C_A3 = 0.999678...` is not a
defect but the first visible renormalization correction. That is the strongest
positive route. The rebuttal is scope: no retained charged-lepton scale-running
or threshold theorem in the current packet derives that correction, so the
offset must remain an explicit A3 target.

### N8 - Cross-cycle echo

This mirrors previous framework lanes where an exact structural integer landed
before the physical readout or pole-scale correction. The right discipline is
not to demote the integer as numerology and not to promote it as final
precision. It is to preserve the exact integer as a strong scaffold while
requiring a separate correction or direct noninteger-divisor theorem.

**Gate result:** broad no-go fails; narrowed precision-correction firewall
passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of `C_A3 = 0.999678091...`.
- No derivation of a direct `N = 256.082435...` theorem.
- No derivation of a lepton scale-running or threshold correction.
- No derivation of `m_W`, `a_lepton`, `m_e`, `alpha(0)`, or hydrogen
  spectroscopy.
- No use of observed charged-lepton masses or `m_W` as proof inputs.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_precision_correction_firewall.py
```

The verifier checks the precision arithmetic, required correction, candidate
scale comparisons, primitive boundary, open-PR alignment, the no-go discipline
section, and the explicit non-claims.
