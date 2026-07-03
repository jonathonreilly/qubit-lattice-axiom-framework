# AC_phi_lambda K-Odd Carrier Registered-Datum Test Against 2/9

**Date:** 2026-07-03
**Type:** no_go
**Claim type:** no_go (scoped obstruction for the three tested
projective-carrier constructions; the broader escape path remains open)
**Primary runner:** [`scripts/frontier_acphilambda_k_odd_carrier_datum_2026_07_03.py`](../scripts/frontier_acphilambda_k_odd_carrier_datum_2026_07_03.py) (`TOTAL: PASS=28 FAIL=0`)
**Outcome:** OBSTRUCTION
**Audit boundary:** The audit lane owns statuses. This note does not edit a registry, set a grade, register a primitive, change an axiom, or claim an `AC_phi_lambda` derivation.

## Dependencies

- [`RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12.md`](RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12.md)
  supplies the escape-condition target, the fixed-locus density, and the I4b
  / N7 guardrails used here.
- [`ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md`](ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md)
  supplies the projective lift and K-odd trace identity tested here.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  record-readout sentence used in the registrability screen.

## Question

The live A1 path from the R-eta algebraic note is:

> "Construct a registrable `C_3`-covariant holonomy or eta-invariant on the carrier whose registered datum is provably the fixed-locus density. That would derive A1 on the framework surface."

This note tests that path on the projective spin carrier using the landed lift

```text
U = (I - i (sigma_x + sigma_y + sigma_z)) / 2,
U^3 = -I.
```

The load-bearing trace identity from the projective carrier is:

> "Tr(O U^2) = -conjugate(Tr(O U))"

The target is the fixed-locus density

```text
L_3(1,2) = 1/9 + 1/9 = 2/9.
```

The test is whether a registered datum equals `2/9`. It is not a test of whether an angle can be named so that it resembles the desired value.

## Registrability Screen

The readout screen uses the axiom sentence:

> "Only records are readable. A readout value is determined by record content alone."

Each candidate is screened for:

- record-content dependence alone;
- `C_3` covariance;
- K-odd separation, using the requirement that "a separator must make `Tr(O R)` non-real."

A number match would not count as A1 unless the same candidate also passed this screen. No candidate below has a number match.

## Period Conventions

Two angle conventions are kept separate.

- **Period-1 convention:** a full turn has value `1`. The target comparison is exactly the rational full-turn fraction `2/9`.
- **Period-2pi convention:** a full turn has angle `2 pi`; a rational full-turn fraction `q` means angle `2 pi q`. Under this convention the target fraction `2/9` would mean angle `4 pi / 9`.

The bare-radian reading `2/9` radians would correspond to the full-turn fraction `1/(9 pi)`. That is not a rational period datum and would import A2. This note does not import A2.

## Candidate 1: Projective Holonomy Phase

The projective branch projectors have exact U-weights:

| source | phase fractions for `Tr(O U^k)`, `k=1,2,3` | `C_3` product fraction | result |
|---|---:|---:|---|
| `P_+` branch | `-1/6, -1/3, 1/2` | `0` | NO-MATCH |
| `P_-` branch | `1/6, 1/3, 1/2` | `0` | NO-MATCH |

The Pauli-axis separator orbit gives the K-odd non-real traces directly:

| source | phase fractions for `Tr(O U^k)`, `k=1,2,3` | covariant datum | result |
|---|---:|---:|---|
| `sigma_x -> sigma_y -> sigma_z` | `-1/4, -1/4, undefined` | full orbit undefined because `Tr(sigma_z U^3)=0`; nonzero part is `1/2` | NO-MATCH |

So the exact projective phase data are Z6 torsion fractions and a half-turn. They do not equal `2/9` in the period-1 convention. In the period-2pi convention they give angles such as `0` and `pi`, not `4 pi / 9`. No bare-radian comparison is used.

Registrability screen: the phase data are `C_3`-covariant, and the Pauli-axis components satisfy the K-odd separator test through non-real traces. The record-content-alone condition is not established by this carrier calculation. The candidate is still a NO-MATCH before registrability can matter.

## Candidate 2: Eta-Style Spectral Asymmetry

Let

```text
S = sigma_x + sigma_y + sigma_z,
B_k = S U^k.
```

Because `S` and `U` commute, the small-carrier eigenvalues are exact:

| `k` | eigenvalues of `B_k` | principal phase fractions | real-cut asymmetry |
|---:|---|---:|---:|
| `1` | `sqrt(3) exp(-i pi/3)`, `-sqrt(3) exp(i pi/3)` | `-1/6, -1/3` | `0` |
| `2` | `sqrt(3) exp(-2 i pi/3)`, `-sqrt(3) exp(2 i pi/3)` | `-1/3, -1/6` | `0` |
| `3` | `-sqrt(3)`, `sqrt(3)` | `1/2, 0` | `0` |

The eta-style ratio used here is

```text
(# Re(lambda) > 0 - # Re(lambda) < 0) / (# eigenvalues).
```

It is `0` in each `k` sector and `0` in aggregate. As a sensitivity check, the imaginary-cut signed count gives `-1, -1, 0`, also not `2/9`.

Registrability screen: the eigenvalue multiset is `C_3`-covariant, but the real-cut signed count cancels the K-odd separation and the record-content-alone condition is not established. The candidate is a NO-MATCH.

## Candidate 3: Fixed-Locus Weight Readout

The parent fixed-locus arithmetic is not just the total `2/9`; it decomposes as:

```text
j = 1: 1/9
j = 2: 1/9
total: 2/9
```

The tested carrier data do not reproduce those per-locus weights:

| candidate decomposition | weights | comparison |
|---|---:|---|
| branch phase magnitudes | `1/6, 1/3` | not `1/9, 1/9` |
| Pauli-axis phase magnitudes | `1/4, 1/4` | not `1/9, 1/9` |
| real-cut eta weights | `0, 0` | not `1/9, 1/9` |

There is also no total-only accidental match. This is the sharpest obstruction in the run: the projective carrier naturally supplies Z6 torsion fractions and signed-count ratios, while the fixed-locus density supplies Lefschetz denominator weights. The tested data do not map one structure to the other.

Registrability screen: a direct fixed-locus readout would be `C_3`-covariant, but it would read parent fixed-locus arithmetic rather than a datum generated by the projective carrier record. It also lacks K-odd non-real separation. The candidate is a NO-MATCH.

## Walls Dodged

I4b is respected by keeping the construction off the Hermitian-positive mass surface:

> "on the Hermitian-positive mass surface `a > 2B > 0`, every eigenvalue is positive, so `det H` is real positive and `arg det H = 0`. There is no holonomy or determinant phase on this surface that can source `2/9`."

On restriction back to that surface, the holonomy phase datum trivializes to `0`, and the centered eta datum trivializes to `0`. The nonzero data tested above live on the projective, non-Hermitian-positive U-twisted carrier.

N7 is respected by not importing the bridge:

> "it imports the density-to-radian bridge it was supposed to derive."

The runner compares rational full-turn fractions exactly. It does not convert the density `2/9` into a bare radian angle, and it does not identify `1/(9 pi)` with a rational period datum.

## Boundary

A2 is untouched. No unit/radian atom is used.

A1 is not derived. A derivation claim would require both an exact `2/9` match and a full registrability-screen pass by the same candidate. Neither condition occurs here.

The outcome is OBSTRUCTION: the tested projective holonomy and eta-style constructions do not produce the fixed-locus density, and they do not reproduce the stronger `1/9 + 1/9` fixed-locus decomposition. This leaves the escape path open as a target, but these constructions do not fill it.

## Verification

Run:

```text
python3 scripts/frontier_acphilambda_k_odd_carrier_datum_2026_07_03.py
```

Measured local close on 2026-07-03:

```text
TOTAL: PASS=28 FAIL=0
SUMMARY candidates: C1=NO-MATCH; C2=NO-MATCH; C3=NO-MATCH
SUMMARY period-matches: none under period-1 full-turn or period-2pi full-turn; A2 not imported
```
