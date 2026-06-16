# Koide kappa Block-Total Frobenius Measure Theorem

**Date:** 2026-04-19
**Lane:** Charged-lepton Koide / MRU
**Claim type:** bounded_theorem
**Status:** bounded support theorem on the finite block-total
Frobenius algebra. The block-total Frobenius-squared functional
`E_I := || pi_I(H) ||_F^2` on `Herm_circ(d)` assigns one scalar slot per
real isotype independent of block real dimension. At `d = 3` this gives
the 1:1 algebraic weights named by the MRU weight-class obstruction
theorem; `d = 3` is the unique dimension where the real-irrep
multiplicity pattern is `(1 trivial + 1 doublet)`.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Measure choice boundary (post-audit).** This note does not derive the
scalar-lane `SO(2)` quotient or prove that the block-total law is the
canonical physical scalar measure. Those are the remaining bridge tasks
for turning this bounded support into an unbounded closure route. The
result proved here is narrower: if the scalar lane is carried by the
block-total Frobenius slots `(E_+, E_perp)`, then the equal-weight
extremum gives `kappa = 2`, and the finite `d = 3` multiplicity scan is
framework-native.

**Primary runner:** [`scripts/frontier_koide_kappa_block_total_frobenius_measure_theorem.py`](../scripts/frontier_koide_kappa_block_total_frobenius_measure_theorem.py)

---

## 0. Executive summary

The MRU weight-class obstruction theorem classified block-log-volume
laws by weights `(mu, nu)` on the two real isotypes of `Herm_circ(3)`
and identified the missing object as a **1:1 real-isotype measure** on
the non-trivial doublet block.

This note exhibits the candidate measure explicitly:

> **Theorem (block-total Frobenius measure).** The functional
> `E_I(H) := || pi_I(H) ||_F^2` on `Herm_circ(d)` (with pi_I the
> canonical isotypic projector on the matrix algebra) assigns one
> scalar per real-isotype block. At `d = 3` it produces
> `E_+ = 3 a^2` and `E_perp = 6 |b|^2`, giving the block-total
> log-law
> 
> ```
> S_block(H) = log E_+ + log E_perp
> ```
> 
> whose equal-weight extremum at fixed `E_+ + E_perp` is exactly
> `E_+ = E_perp`, equivalently `a^2 = 2 |b|^2`, equivalently
> `kappa = 2`, whenever this block-total law is supplied as the scalar
> carrier.

**d = 3 uniqueness.** Frobenius reciprocity counts the real-irrep
multiplicities inside `Herm_circ(d)` for every `d`:

| d | real-irrep multiplicities (trivial, doublets, sign) |
|---|---|
| 2 | (1, (), 1) — trivial + sign (no doublet) |
| **3** | **(1, (1,), 0) — 1 trivial + 1 doublet, no sign** |
| 4 | (1, (1,), 1) — trivial + doublet + sign |
| 5 | (1, (1, 1), 0) — trivial + 2 doublets |
| 6 | (1, (1, 1), 1) — trivial + 2 doublets + sign |

`d = 3` is the unique dimension at which `Herm_circ(d)` decomposes into
exactly one trivial irrep and one doublet irrep, each with multiplicity
one. This makes `mult(rho, Herm_circ(3)) = (1, 1)` the
Frobenius-reciprocity-native candidate at `d = 3`, matching the target
`1:1` weights of the MRU obstruction theorem.

**Boundary positioning.** This theorem is a source-side repair of the
block-total branch, not a claim that the operator-side `kappa = 2` gate
is closed by independent routes. It separates the algebraic support
from the still-open canonical-measure bridge:

1. **Bridge route.** Operator-side `kappa = 2` may be inherited from
   spectrum-side Koide `Q = 2/3` through the cyclic-compression
   dictionary, subject to that bridge note's audit status.
2. **Block-total Frobenius branch (this theorem).** Operator-side
   `kappa = 2` is the equal-weight extremum of `log E_+ + log E_perp`
   under a stipulated block-total 1:1 scalar carrier, with `d = 3`
   uniqueness proved internally here.

The branch remains distinct from the `log|det|` law, which lands at
`kappa = 1` on the unreduced determinant carrier.

---

## 1. Setup

### 1.1 Isotypic decomposition of `Herm_circ(3)`

Every Hermitian circulant decomposes canonically as

```text
H = pi_+(H) + pi_perp(H),   pi_+(H) = (tr H / 3) I,   pi_perp(H) = H - pi_+(H).
```

On the explicit parametrization `H = a I + b C + bbar C^2`:

```text
pi_+(H) = a I,
pi_perp(H) = b C + bbar C^2.
```

The two pieces live in orthogonal real-isotype subspaces of
`Herm_circ(3)`:

- `image(pi_+) = { alpha I : alpha in R }` — real dim 1 (trivial
  irrep).
- `image(pi_perp) = { b C + bbar C^2 : b in C }` — real dim 2 (real
  doublet irrep).

Frobenius orthogonality `<pi_+(H), pi_perp(H)>_F = 0` is a direct
consequence of orthogonality of the real cyclic basis
`{I, C + C^2, i(C - C^2)}`.

### 1.2 Block-total functionals

Define

```text
E_+(H)    := || pi_+(H) ||_F^2     = 3 a^2,
E_perp(H) := || pi_perp(H) ||_F^2  = 6 |b|^2.
```

Each `E_I` assigns one scalar slot per real isotype regardless of the
block's real dimension. This is multiplicity weighting: each real
isotype contributes multiplicity 1 to the inner-product counting,
rather than per-real-dim weighting (which gives 1 to the trivial and
2 to the doublet). This defines the candidate scalar carrier; it does
not by itself prove that the carrier is canonical for the physical
scalar lane.

### 1.3 Weight-class classification and MRU

The MRU weight-class obstruction theorem classified laws of the form

```text
S_{mu, nu}(H) = mu log E_+ + nu log E_perp
```

showing the extremum at fixed `E_+ + E_perp` is `kappa = 2 mu / nu`.
MRU's target `kappa = 2` is the equal-weight leaf `(mu, nu) = (1, 1)`.
The det-carrier `log|det|` law on the unreduced `3 x 3` circulant gives
`(mu, nu) = (1, 2)` because rank `P_+` = 1 and rank `P_perp` = 2 in
the pointwise-vector-projector picture, landing at `kappa = 1`.

---

## 2. Theorem

**Theorem (block-total Frobenius measure).** On `Herm_circ(3)`:

1. `E_+(H) = 3 a^2` and `E_perp(H) = 6 |b|^2` for every
   `H = a I + b C + bbar C^2`.
2. The equal-weight log-law `S_MRU(H) = log E_+(H) + log E_perp(H)`
   under the constraint `E_+(H) + E_perp(H) = const` is extremized at
   `E_+ = E_perp`, i.e. at `a^2 = 2 |b|^2`, i.e. at `kappa := a^2 / |b|^2
   = 2`.
3. When the block-total scalar carrier is stipulated, the weights
   `(1, 1)` in `S_MRU` are Frobenius reciprocity's multiplicity count
   `mult(rho, Herm_circ(3))` over the two real isotypes (trivial,
   doublet).

**d = 3 uniqueness.**

4. The real-irrep multiplicity count inside `Herm_circ(d)` equals
   `(1 trivial + 1 doublet)` if and only if `d = 3`. At `d = 2`, there
   is no non-trivial doublet. At `d = 4`, a sign irrep joins. At `d >= 5`,
   multiple doublets appear. The multiplicity-weighted 1:1 candidate
   therefore matches MRU at `d = 3` only.

**Proof sketch.**

*Item 1.* By direct Frobenius evaluation on the orthogonal cyclic basis
`{I, C + C^2, i(C - C^2)}` with norms `(sqrt(3), sqrt(6), sqrt(6))`.
The runner verifies this symbolically (T4, T5).

*Item 2.* Let `x = E_+` and `y = E_perp`. Maximize `log x + log y`
subject to `x + y = S`. Lagrange: `1/x = 1/y`, so `x = y`. Substituting
into item 1: `3 a^2 = 6 |b|^2`, i.e. `kappa = 2`.

*Item 3.* The isotypic decomposition `Herm_circ(3) = R I + (R C + R C^2)`
has one real dim in the trivial isotype (`a`) and two real dims in the
doublet isotype (`Re b`, `Im b`). Frobenius reciprocity counts each
real isotype once by multiplicity (not by real dim). The runner enumerates
the counts for d = 2..6 (T7, T8).

*Item 4.* A Hermitian circulant `H` on `C^d` is specified by
`a_0 in R`, `b_k in C` for `1 <= k < d/2`, and (if d even)
`b_{d/2} in R`. These correspond respectively to the trivial, doublet,
and sign real irreps. Hence `(trivial, doublets, sign)` multiplicities
are

```text
(1, floor((d - 1) / 2), 1 if d is even else 0).
```

This equals `(1, 1, 0)` iff `floor((d - 1) / 2) = 1` and `d` is odd,
i.e. `d = 3`.

QED.

---

## 3. Implication for the Koide closure stack

The MRU weight-class obstruction theorem identified the missing object
as a 1:1 real-isotype measure. This theorem exhibits a concrete
framework-native candidate, the block-total Frobenius-squared
functional, with `d = 3` uniqueness, and identifies the weight count as
Frobenius-reciprocity multiplicity.

This does not prove that the block-total candidate is the canonical
physical scalar-lane measure. It instead gives the next audit a clean
separation:

| Route | Mechanism | Residue |
|---|---|---|
| Bridge | Cyclic-compression Fourier dictionary, exact identity `a_0^2 - 2|z|^2 = 3(a^2 - 2|b|^2)` | inherited from the bridge note's audit status |
| Block-total Frobenius | Multiplicity-weighted log-law extremum at `E_+ = E_perp` | missing scalar-lane canonical-measure / `SO(2)` quotient bridge |

The operator-side framing is therefore no longer underspecified at the
finite algebra level, but the physical closure still depends on a
separate bridge theorem.

---

## 4. Residue (single-named)

The block-total Frobenius candidate realizes the target weights `(1, 1)`
from Frobenius reciprocity. The remaining choice is between two natural
log-laws on `Herm_circ(3)`:

1. **Block-total log-law** `log E_+ + log E_perp`, weights `(1, 1)`,
   extremum at `kappa = 2`. This is MRU's target and is algebraically
   realized here.
2. **Det log-law** `log|det(alpha P_+ + beta P_perp)|` on the unreduced
   3x3 circulant, weights `(1, 2)`, extremum at `kappa = 1`. This is
   the det-carrier `log|det|` law flagged as the obstruction.

Both are natural functionals on `Herm_circ(3)`. The single-named
residue is: which is the canonical extremal principle for the physical
scalar lane? The block-total route prefers multiplicity weighting (one
scalar per real isotype); the det route prefers rank/dimensional
weighting.

This is not treated as a minor convention here. It is the missing bridge
for promoting the block-total branch from bounded algebraic support to
unbounded physical closure.

---

## 5. Falsification checks

1. **Block-total formula.** The runner verifies `E_+ = 3 a^2` and
   `E_perp = 6 |b|^2` both symbolically (T4, T5) and on a synthetic
   numeric instance (T9a, T9b) from direct Frobenius evaluation. A sign
   error or incorrect projection would break these.

2. **Non-load-bearing PDG comparator.** The runner prints the PDG
   charged-lepton ratio `E_+ / E_perp` as a diagnostic only; it is not a
   PASS gate and is not used to derive the operator-side law.

3. **d = 3 uniqueness.** The runner enumerates the multiplicity pattern
   at `d = 2..6` (T8). Any `d != 3` fails the "1 trivial + 1 doublet"
   pattern, confirming the uniqueness claim.

4. **Law separation.** Block-total extremum `kappa = 2` differs from
   det-carrier extremum `kappa = 1` by exactly 1 (T10), so the two laws
   are not interchangeable without an additional scalar-lane bridge.

---

## 6. Runner — expected output

```
TOTAL: PASS=16 FAIL=0
```

The runner exercises:

- `T1, T2` canonical isotype projectors on `Herm_circ(3)` (symbolic),
- `T3` real-dim image counts `(1, 2)`,
- `T4, T5` exact block-total formulae `E_+ = 3 a^2`, `E_perp = 6 |b|^2`,
- `T6` MRU equivalence with `kappa = 2`,
- `T7, T8` Frobenius-reciprocity multiplicity pattern and `d = 3`
  uniqueness at d=2..6,
- `T9a-c` synthetic numerical realization plus non-load-bearing PDG
  diagnostic,
- `T10` separation of block-total law (kappa=2) vs det carrier law
  (kappa=1).

No hard-coded True; all PASSes keyed to substantive computations.
The PDG line is printed as a comparator and does not increment PASS.

---

## 7. Cross-references

- `docs/KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`
  — the obstruction theorem this note partially repairs by exhibiting
  the block-total candidate while leaving the canonical-measure bridge open.
- `docs/KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md`
  — MRU as a d = 3 theorem.
- `docs/KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`
  — companion bridge theorem for the spectrum/operator route.
- `docs/KOIDE_CYCLIC_PROJECTOR_BLOCK_DEMOCRACY_NOTE_2026-04-18.md`
  — block democracy equivalent to MRU via block-total energies.
- `docs/KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`
  — operator-space lift of `sigma = 1/2`.

---

## 8. Honest limits

- This theorem does not close the spectrum-side Koide `Q = 2/3` itself
  or import any spectrum-side closure claim into this branch.
- This theorem shows the operator-side 1:1 block-total measure is a
  framework-native candidate functional, but it does not derive the
  scalar-lane `SO(2)` quotient or prove canonical physical measure
  status. The choice between block-total log-law and det log-law remains
  a real structural residue.
- The theorem is stated at `d = 3`; the all-`d` multiplicity formula is
  given in the proof sketch and the runner scans d = 2..6 as regression
  coverage.
- Numerical verification uses synthetic values for PASS gates. PDG
  charged-lepton masses are printed only as a comparator, not used to
  derive or verify the operator-side law.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [koide_moment_ratio_uniformity_theorem_note_2026-04-19](KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md)
- [koide_mru_weight_class_obstruction_theorem_note_2026-04-19](KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md)
