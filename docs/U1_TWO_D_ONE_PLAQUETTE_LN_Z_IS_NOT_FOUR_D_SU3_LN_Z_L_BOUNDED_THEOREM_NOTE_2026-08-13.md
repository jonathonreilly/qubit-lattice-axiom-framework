---
claim_id: u1_two_d_one_plaquette_ln_z_is_not_four_d_su3_ln_z_l_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Remainder-controlled rational enclosures of I_0(β) at β=1,2,3 are the partition function of 2D U(1) one-plaquette (and of a tree-gauge-fixed 2D disk factor); they are not 4D SU(3) ln Z_L, because N_p(L=2)=96≠1 and the June 10 wrapping count 72 is unused."
upstream_dependencies:
  - minimal_axioms
  - plaquette_value_derivation_program_specification_and_bracket_reduction_narrow_theorem_note_2026-06-10
runner: scripts/u1_two_d_one_plaquette_ln_z_is_not_four_d_su3_ln_z_l_2026_08_13.py
---

# Certified 2D U(1) One-Plaquette I_0 Is Not 4D SU(3) ln Z_L

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** remainder-controlled `I_0` at three couplings for 2D U(1)
one-plaquette, and the type split versus 4D SU(3) `ln Z_L`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/u1_two_d_one_plaquette_ln_z_is_not_four_d_su3_ln_z_l_2026_08_13.py`](../scripts/u1_two_d_one_plaquette_ln_z_is_not_four_d_su3_ln_z_l_2026_08_13.py)

## Result Up Front

The June 10 program note
[`PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`](PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md)
names the remaining interface for admission B1 as

> a certified enclosure of ln Z_L at three couplings

for one explicit `(L, δ)` of 4D SU(3) Wilson. The fuller June 10 sentence
is to produce certified enclosures of `ln Z_L` at the three couplings
`{6-delta, 6, 6+delta}`. That interface is not executed here.

This note constructs a simpler executable object: the 2D U(1)
one-plaquette partition function, equivalently one tree-gauge-fixed 2D
disk factor,

```text
Z_1(beta) = int_{U(1)} exp(beta cos theta) dtheta/(2 pi) = I_0(beta),
I_0(beta) = sum_{k >= 0} beta^{2k} / (4^k (k!)^2).
```

Certified rational enclosures of `I_0` at `beta in {1, 2, 3}` **are** the
partition function of this finite U(1) model. Because `ln` is increasing
on the positive reals, those enclosures are equivalent information to a
`ln Z_1` table; the comparison stays at the `I_0` level, so no floating
logarithm is claimed. Even a perfect `ln I_0` table is `ln Z` of this
U(1) model only.

The same table is **not** 4D SU(3) `ln Z_L`. On the periodic 4D torus,
`N_p = 6 L^4`, so `N_p(L=2) = 96 ≠ 1`. The June 10 wrapping count
`6 L^2 (2L-1)` equals `72` at `L=2` and is never an input of `I_0`.
Substituting `ln I_0` for `f_L` or for `ln Z_L` is not the June 10
bracket.

The axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is an
upstream dependency. No axiom sentence is edited, and no axiom sentence
is used as a hypothesis that would identify `I_0` with 4D `Z_L`.

This note does not derive 0.5934. It does not retire B1. It does not claim I_0 is Z_L of 4D SU(3).

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Remainder-controlled I_0 enclosures are Z of 2D U(1) one-plaquette; N_p(L=2)=96≠1 so they are not 4D SU(3) ln Z_L."
trace_class: upstream_support
target_claim_id: certified_three_point_ln_z_l
target_blocker_text: "produce certified ln Z_L enclosures at three couplings, or a mass-gap rate"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "2D U(1) I_0 is an executable certified table for that model only. The June 10 4D SU(3) interface remains open. Do not import 0.5934. Do not adopt axiom text."
hypothetical_axiom_status: "no edit"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Normalized Haar measure on `U(1)` is `d theta / (2 pi)`. The one-plaquette
weight used here is `exp(beta cos theta)`. The partition function is
`Z_1(beta) = I_0(beta)` as above.

Partial sums and term ratios are the exact rationals

```text
t_k(beta) = beta^{2k} / (4^k (k!)^2),
S_N(beta) = sum_{k=0}^{N} t_k(beta),
t_{k+1}/t_k = beta^2 / (4 (k+1)^2).
```

The first three terms, recomputed from the Haar moments of even powers of
`cos theta`, are

```text
t_0 = 1,
t_1(beta) = beta^2 / 4,
t_2(beta) = beta^4 / 64.
```

In particular `S_2(1) = 1 + 1/4 + 1/64 = 81/64`.

Whenever `q := beta^2 / (4 (N+2)^2) < 1`, the tail admits the geometric
majorant

```text
0 <= I_0(beta) - S_N(beta) <= R_N(beta) := t_{N+1}(beta) / (1 - q).
```

At the three couplings `beta in {1, 2, 3}` the truncation `N = 8` already
gives `q in {1/400, 1/100, 9/400}`, all strictly less than `1`. The same
`q < 1` test holds at `beta in {5, 6, 7}` for this `N`; those optional
points remain U(1) calculus and are not 4D SU(3) couplings.

On the periodic 4D hypercubic torus the June 10 counts are

```text
N_p(L) = 6 L^4,     N_ell(L) = 4 L^4,
wrap(L) = 6 L^2 (2L - 1).
```

At `L = 2` these are `96` plaquettes, `64` links, and `72` wrapping
plaquettes. U(1) one-plaquette has `N_p = 1` and group `U(1)`, not
`SU(3)`.

A tree-gauge-fixed 2D disk with `m` plaquettes factorizes as
`Z_disk(beta) = I_0(beta)^m`. The `m = 2` product is `I_0(beta)^2`.

The runner identity gates call `i0_partial(beta, N)` and
`plaquette_count_4d(L)`. Series coefficients are the terms `t_k` only.

## Exact Target And Obligation Graph

**Exact target.** Certify `Z_1 = I_0` with an explicit remainder, produce
a three-point rational table at `beta in {1, 2, 3}`, and record that the
table is not 4D SU(3) `ln Z_L`.

| Obligation | Role | Disposition |
|---|---|---|
| pin the June 10 three-point `ln Z_L` interface | premise | quoted from the June 10 note |
| pin `N_p = 6 L^4` and wrap `6 L^2 (2L-1)` | premise | quoted from the June 10 note |
| identify `Z_1 = I_0` and recompute `t_0, t_1, t_2` | Theorem 1 | Haar moments |
| produce `S_N <= I_0 <= S_N + R_N` at three couplings | Theorem 2 | remainder-controlled series |
| split `I_0` from 4D `ln Z_L` | Theorem 3 | `96 ≠ 1` and unused wrap `72` |
| show the disk product is still U(1) 2D | Theorem 4 | `I_0^2` and `2 ≠ 96` |
| record scoped negatives, including B1 | Theorem 5 | no retirement, no 4D claim |
| produce 4D SU(3) `ln Z_L` at three couplings | June 10 interface | open |
| retire B1, or derive the June 10 named numeral | non-claim | not executed |

## Theorem 1 — Executable U(1) Identity

**Claim.** `Z_1(beta) = I_0(beta)` as a normalized Haar integral. The
series and the remainder bound above are exact. The first three terms are
`t_0 = 1`, `t_1 = beta^2/4`, and `t_2 = beta^4/64`.

**Proof.** Expand the exponential and integrate term by term against
normalized Haar measure:

```text
Z_1(beta) = sum_{n >= 0} (beta^n / n!) int_0^{2 pi} cos^n theta d theta / (2 pi).
```

Odd `n` vanish. For `n = 2k` the binomial identity
`cos theta = (e^{i theta} + e^{-i theta})/2` isolates the constant term
`C(2k, k) / 4^k`, so

```text
int cos^{2k} theta d theta / (2 pi) = (2k)! / (4^k (k!)^2).
```

The corresponding series term is

```text
(beta^{2k} / (2k)!) * (2k)! / (4^k (k!)^2) = t_k(beta).
```

Thus `Z_1 = I_0`. The cases `k = 0, 1, 2` are

```text
k = 0:  1,
k = 1:  (beta^2 / 2) * (1/2) = beta^2 / 4,
k = 2:  (beta^4 / 24) * (3/8) = beta^4 / 64,
```

using `int cos^2 = 1/2` and `int cos^4 = 3/8`. In particular
`S_2(1) = 81/64`.

All terms are nonnegative. The consecutive ratio is
`t_{k+1}/t_k = beta^2 / (4 (k+1)^2)`. For every `k >= N+1` one has
`k+1 >= N+2`, hence `t_{k+1}/t_k <= q` with
`q = beta^2 / (4 (N+2)^2)`. If `q < 1` the tail is at most the geometric
series `t_{N+1} (1 + q + q^2 + ...) = t_{N+1}/(1-q)`. This is `R_N`.

## Theorem 2 — Certified Three-Point Table (This Model Only)

**Claim.** At `beta in {1, 2, 3}` and truncation `N >= 8`, the exact
rationals `S_N(beta)` and `R_N(beta)` satisfy

```text
S_N(beta) <= I_0(beta) <= S_N(beta) + R_N(beta).
```

The table is `Z_1` of this U(1) model only. Even a perfect `ln I_0`
enclosure would still be `ln Z` of this model only.

**Proof.** Theorem 1 gives the enclosure law once `q < 1`. At `N = 8`,

```text
q(1) = 1/400,   q(2) = 1/100,   q(3) = 9/400.
```

The paired runner recomputes the displayed partial sums and remainders
from `t_k` and the geometric majorant. None of those rationals is
constructed from a 4D Wilson integral, and none is constructed from the
numeral the June 10 interface names. The `N = 8` values are

| `beta` | `S_8(beta)` | `R_8(beta)` | `S_8 + R_8` |
|---|---|---|---|
| `1` | `44963077292459/35514010828800` | `1/34433319479279616` | `4359485085044947363/3443331947927961600` |
| `2` | `1235309099/541900800` | `1/130365075456` | `29717830994743/13036507545600` |
| `3` | `6419871123697/1315333734400` | `59049/5142954901504` | `2510169615270427/514295490150400` |

Because `ln` is increasing on `(0, infty)`, the same bounds would pass to
`ln S_N <= ln I_0 <= ln(S_N + R_N)`. Those logarithms are not rational,
so the certified table stays at the `I_0` level.

The same remainder law at `N = 8` has `q < 1` for `beta in {5, 6, 7}`
(`q = 1/16`, `9/100`, `49/400`). Those optional enclosures are still
`I_0` of U(1), not `Z_L` of 4D SU(3).

## Theorem 3 — Type Split Versus June 10

**Claim.** `N_p(L=2) = 96 ≠ 1`. The June 10 wrapping count
`6 L^2 (2L-1)` equals `72` at `L=2` and is never used by `I_0`.
Substituting `ln I_0` for `f_L` is not the June 10 bracket.

**Proof.** June 10 defines the 4D Wilson torus by `4 L^4` links and
`N_p = 6 L^4` plaquettes, and the per-plaquette free energy
`f_L(beta) = (1/(6 L^4)) ln Z_L(beta)`. At `L = 2` this is `96`
plaquettes. The U(1) object of Theorems 1 and 2 has one plaquette.
The equality `96 = 1` is false, so `I_0` cannot be `Z_L` and
`ln I_0` cannot be `ln Z_L`.

Lemma L2 of June 10 counts torus plaquettes that use at least one
wrapping link as `6 L^2 (2L-1)`. At `L = 2` that count is `72`. The
series `I_0 = sum t_k` is a function of `beta` and of the factorials in
`t_k`. It has no wrapping argument. The identity gates call
`i0_partial(beta, N)` and `plaquette_count_4d(L)`; replacing
`plaquette_count_4d(2)` by `1` fails the identity `6 * 16 = 96`.

The June 10 bracket also requires three 4D couplings of the form
`{6-delta, 6, 6+delta}` and the surface rate `|f_L - f| <= 6 beta / L`.
The present table uses `{1, 2, 3}` and never forms `f_L`. Group, dimension,
volume, wrapping, and coupling list all differ. The substitution of
`ln I_0` for `f_L` is therefore not the June 10 bracket.

A predicate that the `I_0` enclosure **is** 4D SU(3) `ln Z_L` must fail
at `L = 2` because `N_p = 96 ≠ 1`.

## Theorem 4 — Disk Product Is Still U(1) 2D

**Claim.** The tree-gauge-fixed 2D disk with two plaquettes has
`Z_disk(beta) = I_0(beta)^2`. That product is executable and is still not 4D SU(3) `Z_L`.

**Proof.** On a 2D disk, a spanning tree of links may be gauge-fixed to
the identity. Each remaining link is a unique plaquette holonomy. The
Haar measure factorizes over those holonomies, so
`Z_disk = I_0^m` for `m` plaquettes. At `m = 2` this is `I_0^2`.

Theorem 2 supplies `S <= I_0 <= S + R` with `S > 0` and `R >= 0`, hence

```text
S^2 <= I_0^2 <= (S + R)^2.
```

The right-hand side is an exact rational. The product still has two
U(1) plaquettes, not `96` SU(3) plaquettes, and still ignores the
wrapping count `72`. Therefore `I_0^2` is not `Z_L`.

## Theorem 5 — Scoped Negatives

**Claim.** This note does not retire B1, does not derive 0.5934, does not claim 4D `<P>*`, and does not perform Monte Carlo. The numeral the June 10 interface names is not an input to `I_0`. Series coefficients are the terms `t_k` only.

**Proof.** Theorems 1--4 certify a U(1) object and split it from the
June 10 4D object. Admission B1 is the 4D thermodynamic-limit plaquette
mean named by June 10, not `I_0` and not `I_0^2`. No certified 4D
`ln Z_L` enclosure is produced, and no mass-gap rate is produced, so
the June 10 retirement interface is unused. B1 is therefore not retired.

The series `I_0 = sum t_k` has coefficients
`t_k = beta^{2k}/(4^k (k!)^2)`. Feeding the June 10 named numeral, as
the rational `5934/10000`, into that series as a coefficient is
rejected: it equals none of the terms `t_k` at `beta in {1, 2, 3}`.
The numeral is not a target of the `I_0` table.

No 4D configuration is sampled, so there is no Monte Carlo. No axiom
sentence is added or edited.

## Boundary And Non-Claims

The note does not:

- produce a certified 4D SU(3) `ln Z_L` enclosure at any coupling;
- retire B1, or derive 0.5934;
- claim 4D `<P>*`, or evaluate the June 10 bracket at any `(L, delta)`;
- perform Monte Carlo, or import a sample as a remainder;
- substitute the SU(3) single-link integral `J` for `I_0` and call that
  `Z_L`;
- supply a 4D mass-gap rate that would replace `6 beta / L`;
- edit an axiom, or argue that an axiom update is necessary.

The scope is the executable U(1) table and the type split `96 ≠ 1`.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| June 10 three-point `ln Z_L` interface | premise | quoted; not executed |
| June 10 counts `N_p = 6 L^4` and wrap `6 L^2 (2L-1)` | premise | quoted; recomputed at `L=2` |
| axiom memo | upstream dependency | linked; no edit |
| Haar identity `Z_1 = I_0` and `t_0, t_1, t_2` | Theorem 1 | computed here |
| remainder-controlled three-point table | Theorem 2 | computed here |
| type split `96 ≠ 1`, unused wrap `72` | Theorem 3 | computed here |
| disk product `I_0^2` | Theorem 4 | computed here |
| 4D SU(3) `ln Z_L` and B1 retirement | residual | live, not derived |

The exact advance is a finite U(1) enclosure table together with a
volume/group type split. Independent audit remains required before any
effective status may change.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | June 10 names the remaining interface as a certified enclosure of ln Z_L at three couplings. This note supplies an executable certified table for 2D U(1) one-plaquette and records that the table is not that 4D object. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for U(1) 2D one-plaquette `I_0` as a certified `ln Z` versus SU(3) 4D `ln Z_L`. Hits: the action-family character note uses `I_n/I_0` as Wilson character ratios; the staggered-sign note uses `I_1/I_0` as a first moment; Picard–Fuchs and Bars notes use SU(N) Bessel determinants; the fixed-lattice existence note tests U(1) one-plaquette positivity, not a remainder-controlled `I_0` table; June 10 uses an SU(3) one-plaquette proxy to validate bracket algebra, not as a claim that `I_0` is `ln Z_L`. No landed type-split theorem identifying certified `I_0` with 2D U(1) `ln Z` and refusing 4D SU(3) `ln Z_L` appears on that commit. |
| V3 | Independently checkable? | Textbook `I_0` is the generating function of `exp(beta cos theta)` and does not name B1, `0.5934`, or 4D SU(3) `Z_L`. The runner recomputes Haar moments, `t_k`, and the geometric tail in exact rationals. |
| V4 | More than a restatement? | Yes. The witnesses `t_0=1`, `t_1=beta^2/4`, `t_2=beta^4/64`, `S_2(1)=81/64`, `N_p(L=2)=96`, and wrap `72` are not restatements of the June 10 interface sentence. |
| V5 | One-step relabel? | No. June 10's one-plaquette proxy is an SU(3) test of bracket algebra. A certified U(1) `I_0` table is not a corollary of that proxy, and it is not a 4D `ln Z_L` enclosure. |

## No-Go Discipline Gate (Theorems 3 and 5 only)

The negative claim is restricted to this: the certified `I_0` table is
not 4D SU(3) `ln Z_L`, and the present construction does not retire B1.
The gate does not ship a global non-existence theorem against a later
4D enclosure, and it does not ship a 4D mass-gap rate.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| substitute `I_0` for `Z_L` | identify the Theorem 2 table with June 10 `ln Z_L` | Theorem 3: `N_p(L=2)=96 ≠ 1`; wrap `72` unused | **ATTEMPTED** |
| SU(3) one-plaquette `J` | replace `I_0` by the June 10 single-link integral `J` and call that `Z_L` | `J` is an SU(3) Haar integral, not `I_0`; even a certified `J` table still has one plaquette, not `96` | **ATTEMPTED** |
| Monte Carlo | sample 4D SU(3) and treat the sample as `ln Z_L` | not performed; `I_0` is an exact series with a factorial majorant, not a sample | **ATTEMPTED** |
| mass-gap rate | use `I_0` to replace the June 10 surface rate `6 beta / L` | `I_0` supplies no 4D gap and no exponential finite-volume rate | **ATTEMPTED** |
| axiom edit naming `I_0` as `Z_L` | add a sentence identifying the U(1) table with 4D Wilson | not required by Haar calculus; see N6 | **ATTEMPTED** |
| import `0.5934` | feed `5934/10000` into `I_0` as a series coefficient | rejected: coefficients are `t_k` only | **ATTEMPTED** |

### N2 — wall independence

Theorem 3 closes only the identification of `I_0` with 4D `Z_L`.
Theorem 5 closes only the listed non-claims. Neither closes the June 10
three-point interface, a later certified 4D enclosure, or a mass-gap
rate. Those walls remain independent. An executable U(1) table does not
by itself retire B1.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| Haar measure on `U(1)` and weight `exp(beta cos theta)` | declared U(1) objects |
| series `t_k`, truncation `N >= 8`, and `q < 1` | explicit remainder hypotheses |
| three couplings `{1, 2, 3}` | explicit table |
| optional `{5, 6, 7}` | same U(1) calculus; not 4D SU(3) |
| `N_p = 6 L^4` and wrap `6 L^2 (2L-1)` | June 10 counts, evaluated at `L=2` |
| disk product `I_0^2` | explicit `m=2` factorization |
| 4D mass-gap rate | open; not assumed |
| axiom edit identifying `I_0` with `Z_L` | live governance path; not required |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`](PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md) | three-point `ln Z_L` interface; `N_p = 6 L^4`; wrap `6 L^2 (2L-1)` | quoted; 4D enclosure remains open |
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice / Qubit / Admissibility / Record | linked as upstream only; no edit |

No unmerged note is used as a parent. The counts `96` and `72` are
recomputed here.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | remainder-controlled terms `t_k` at `beta in {1, 2, 3}` | no 4D Wilson character expansion |
| per site | U(1) one-plaquette versus the `L=2` counts `96` and `72` | no 4D site configuration is sampled |
| per mode | the `I_0` power series, not a transfer-matrix mode | no 4D spectral gap |
| per block | Haar identity, three-point table, type split, disk product | no B1 retirement and no 4D `ln Z_L` |
| lattice-wide | checked and not executed | no lattice-wide 4D SU(3) enclosure |

The residual is a type split. It is not lattice-wide.

### N6 — live partial-closure paths

1. A later certified enclosure of 4D SU(3) `ln Z_L` at three couplings
   for one explicit `(L, delta)`, which is the June 10 interface.
2. A proven 4D mass-gap rate with explicit constants, replacing
   `6 beta / L` and collapsing the June 10 cost budget.
3. A later SU(3) calculation that does not pass through `I_0` at all.
4. An owner-approved typed axiom addition. Haar uniqueness of `I_0` on
   U(1) does not require that addition, and it would not turn `I_0`
   into 4D `Z_L`.

The quoted June 10 sentences already name the 4D interface. They do not
identify `I_0` with `Z_L`. No axiom sentence is required by Theorems 3
or 5.

### N7 — hostile steelman

> A partition function is a partition function. `I_0` is `Z`, so
> `ln I_0` is `ln Z_L`, and the June 10 three-point interface is
> thereby executed.

**Answer.** June 10's `Z_L` is the 4D SU(3) Wilson torus integral with
`N_p = 6 L^4` plaquettes. `I_0` is the U(1) one-plaquette Haar integral.
Theorem 3 is the witness: `96 ≠ 1`, and the wrapping count `72` is
unused. Theorem 2 already states that even a perfect `ln I_0` table is
`ln Z` of this U(1) model only.

### N8 — cross-cycle echo

June 10 already used an exactly solvable one-plaquette/2D surface as a
proxy to validate bracket algebra. That proxy is the SU(3) single-link
integral `J`, and June 10 does not identify it with 4D `Z_L`. The
present U(1) `I_0` table is a different proxy. It does not reverse the
June 10 non-derivation of the named numeral, and it does not execute
the 4D interface.

**Gate disposition.** PASS for the executable U(1) table and for the
scoped type split `96 ≠ 1`. FAIL / DO NOT SHIP for “B1 is retired,”
“`I_0` is 4D SU(3) `ln Z_L`,” or “an axiom edit is required.”

## Primary Runner

[`scripts/u1_two_d_one_plaquette_ln_z_is_not_four_d_su3_ln_z_l_2026_08_13.py`](../scripts/u1_two_d_one_plaquette_ln_z_is_not_four_d_su3_ln_z_l_2026_08_13.py)
recomputes Haar moments, `t_0, t_1, t_2`, `S_2(1)=81/64`, the
`N = 8` enclosures at `beta in {1, 2, 3}`, the counts `N_p(L=2)=96`
and wrap `72`, the disk square, and the coefficient rejection in exact
rational arithmetic. Identity gates call `i0_partial(beta, N)` and
`plaquette_count_4d(L)`. A predicate that the `I_0` enclosure is 4D
SU(3) `ln Z_L` must fail. Replacing `plaquette_count_4d(2)` by `1`
must fail `6*16=96`. Feeding `5934/10000` into `I_0` as a coefficient
must be rejected. No cache is written.

```bash
python3 scripts/u1_two_d_one_plaquette_ln_z_is_not_four_d_su3_ln_z_l_2026_08_13.py
```

Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
