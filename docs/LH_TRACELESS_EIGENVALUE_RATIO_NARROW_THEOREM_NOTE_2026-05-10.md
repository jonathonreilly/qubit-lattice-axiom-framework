# Left-Handed Traceless U(1) Eigenvalue Projective-Ratio Narrow Theorem

**Date:** 2026-05-10; clean-core boundary revised 2026-07-18
**Type:** positive_theorem
**Claim scope:** for a positive integer `n_color` and a nonzero real pair
`(a,b)` satisfying `2 n_color a + 2 b = 0`, both entries are nonzero,
`b = -n_color a`, and the projective class is
`[a:b] = [1:-n_color]`. The theorem fixes a ratio, not an absolute scale.

**Status authority:** independent audit lane. This source note does not set or
predict an audit outcome.

**Runner:**
[`scripts/audit_companion_lh_traceless_eigenvalue_ratio_exact_2026_05_10.py`](../scripts/audit_companion_lh_traceless_eigenvalue_ratio_exact_2026_05_10.py)

## Clean theorem

Let

```text
n_color in Z,  n_color > 0,
a,b in R,
2 n_color a + 2 b = 0,
(a,b) != (0,0).
```

Then

```text
a != 0,
b != 0,
b = -n_color a,
[a:b] = [1:-n_color].
```

Here `[x:y]` denotes a real projective point: two nonzero pairs represent the
same point when one is a nonzero scalar multiple of the other. Equivalently,

```text
(a,b) = lambda (1,-n_color)  for the nonzero scalar lambda = a.
```

After nonzeroness has been established, the affine ratio form is also valid:

```text
a/b = -1/n_color.
```

This projective implication is the conclusion formerly labelled `(R1)`.

## Proof without premature division

Divide the trace equation by the nonzero scalar `2`:

```text
n_color a + b = 0,
```

so `b = -n_color a`.

If `a = 0`, that equality gives `b = 0`, contrary to the nonzero-pair
hypothesis. Thus `a != 0`. Since `n_color > 0`, `n_color != 0`; therefore
`b = -n_color a != 0` as well. Setting `lambda = a` now gives

```text
(a,b) = lambda (1,-n_color),  lambda != 0,
```

which is precisely `[a:b] = [1:-n_color]`. Division by `b` is justified only
after this step and yields `a/b = -1/n_color`. ∎

## Domain checks

- `n_color = 1` gives the nonzero solution line
  `(a,b) = lambda(1,-1)`.
- Every positive integer `n_color` has the nonzero solution line
  `(a,b) = lambda(1,-n_color)` with unrestricted nonzero real scale and sign
  `lambda`.
- Removing the nonzero-pair hypothesis admits `(0,0)`, for which no
  projective point or affine ratio is defined.
- At `n_color = 0`, the equation gives `b = 0`; a pair such as `(1,0)` is
  nonzero, so the theorem's conclusion that both entries are nonzero does not
  extend to that domain.
- The projective algebra itself extends to every nonzero real value of the
  parameter, including negative and noninteger values. Those values are
  outside the stated count domain. Integer parity and rational-denominator
  statements do not extend to an arbitrary noninteger parameter.

## 2026-07-18 convention boundary: former `(R2)`-`(R4)`

The following is exact algebra after two additional conventions are supplied.
It is recorded as non-load-bearing support and is not part of the clean theorem
above.

```text
(C_norm)  b = -1,
(C_Q)     Q = T_3 + Y/2, with Y = a on the left-handed quark doublet
          and T_3 = +1/2 or -1/2 for its two labelled components.
```

Under `(C_norm)`, the projective relation gives

```text
a = 1/n_color.
```

Under both `(C_norm)` and `(C_Q)`, the conventional charge arithmetic is

```text
Q(u_L) = (n_color + 1)/(2 n_color),
Q(d_L) = (1 - n_color)/(2 n_color).
```

For positive integer `n_color`, the two fractions have the same reduced
denominator because

```text
gcd(n_color + 1, 2 n_color) = gcd(n_color + 1, 2),
gcd(1 - n_color, 2 n_color) = gcd(1 - n_color, 2).
```

Consequently, on this explicitly convention-supplied surface,

```text
d_red(n_color) = n_color    when n_color is odd,
d_red(n_color) = 2 n_color  when n_color is even.
```

At `n_color = 3` this support arithmetic returns
`a = 1/3`, `Q(u_L) = 2/3`, `Q(d_L) = -1/3`, and `d_red = 3`. These values do
not follow from the clean theorem without `(C_norm)` and `(C_Q)`.

The two conventions are independent. Supplying `b = -1` does not choose a
charge functional; for example `Q = T_3 + Y` gives different charges.
Supplying `Q = T_3 + Y/2` does not select the scale; replacing
`(a,b)` by `lambda(a,b)` changes the charge readout whenever
`lambda != 1`.

## Exact authority boundary

The clean theorem derives the projective relation from its stated homogeneous
hypotheses. It does not derive or select:

- the physical carrier or the left-handed state inventory represented by the
  trace equation;
- `n_color = 3`;
- an absolute U(1) scale or the normalization `b = -1`;
- a hypercharge interpretation of `a` and `b`;
- the charge functional `Q = T_3 + Y/2`;
- labels such as quark, lepton, up, or down for the two eigenspaces;
- physical electric charges or a physical charge-denominator selection;
- right-handed singlet content, anomaly cancellation, dynamics, empirical
  values, or a Standard Model species map.

The coefficients `2 n_color` and `2` in the trace equation are hypotheses of
this theorem. The theorem makes no inference from them to a carrier or species
inventory.

## Direct-consumer dispositions (2026-07-18)

- `ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md`
  continues to cite this note for `b = -n_color a`. Its normalization,
  charge-shift, singlet inventory, and branch labels are explicit local
  conditions rather than conclusions inherited from this theorem.
- `SU2_WEAK_BETA_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md` treats
  `N_W = (N_color + 1) N_gen` as a supplied field-inventory condition. It does
  not cite this projective theorem as a count authority.
- `QCD_BETA_3_PURE_GAUGE_VS_FULL_SM_NARROW_THEOREM_NOTE_2026-06-02.md` treats
  `N_quark = 6` as the supplied full-Standard-Model flavor inventory. It does
  not cite this projective theorem as authority for `N_pair = 2` or species
  identification.

## Current-cycle N1-N8 boundary evidence

This checklist stress-tests the boundary statements; it does not issue an
audit verdict.

### N1 — distinct attack routes

| route | test | disposition |
|---|---|---|
| zero pair | remove `(a,b) != (0,0)` | `(0,0)` satisfies the equation and has no projective ratio; the hypothesis is load-bearing |
| zero parameter | set `n_color = 0` | `(1,0)` satisfies the equation and has `b = 0`; positivity/nonzeroness of the count is load-bearing for the two-nonzero conclusion |
| negative parameter | set `n_color = -2` | the projective algebra still holds; this is an algebraic extension outside the count domain |
| noninteger parameter | set `n_color = 1/2` or `sqrt(2)` | the projective algebra still holds for a nonzero parameter, while parity/denominator language no longer has the stated domain |
| alternate scale | use `lambda = 2` and `lambda = -3` | both pairs satisfy the trace equation; neither selects `b = -1` in general |
| alternate charge functional | replace `Q = T_3 + Y/2` by `Q = T_3 + Y` | the projective theorem remains true and the charge formulas change |

All six routes are exercised by the runner's hostile mode.

### N2 — independence of the two convention conditions

| pair | close first only | close second only | independent? |
|---|---|---|---|
| `(C_norm)`, `(C_Q)` | `b = -1` with `Q = T_3 + Y` changes the charges | `Q = T_3 + Y/2` with scale `lambda = 2` changes the charges | yes |

The denominator support needs the charge fractions produced after both
conditions are supplied; the wall set is not inflated by downstream
consequences.

### N3 — hidden-condition scan

The proof uses the displayed positive-integer, real-pair, trace-equation, and
nonzero-pair hypotheses. The support appendix marks normalization and charge
readout as supplied conventions. No carrier, species, empirical, dynamics, or
registry premise is hidden inside construction or standardness shorthand. The
runner performs a source-text hygiene scan separately from its
theorem evidence.

### N4 — residual matching

| residual | exact location after repair | scope match |
|---|---|---|
| absolute normalization `b = -1` | `(C_norm)` support condition | exact |
| charge readout `Q = T_3 + Y/2` | `(C_Q)` support condition | exact |
| physical carrier/state inventory | exact authority boundary | excluded from the theorem rather than declared resolved |

The GCD identities match the convention-supplied rational fractions; they do
not match a framework derivation of those fractions.

### N5 — rhetoric and resolution

The positive conclusion is per eigenvalue pair and projective class. No
per-site, per-mode, per-block, lattice-wide, carrier, or physical-species
conclusion is inferred. Countermodels at alternate scale and alternate charge
functional test the two nearby overbroad readings directly.

### N6 — partial-closure path

Supplying `(C_norm)` and `(C_Q)` closes the displayed charge and GCD arithmetic
as conditional support. Reclassifying those choices as conventions does not
turn them into chain-satisfying premises and does not require or propose a new
axiom or primitive.

### N7 — strongest objections

The strongest objection to the projective proof is the zero solution: a
homogeneous equation always contains it, so any ratio proof that divides first
is invalid. The explicit nonzero-pair hypothesis and the no-division proof
answer that objection. The strongest objection to the former charge scope is
the free common scale together with freedom to choose a charge functional;
the alternate-scale and alternate-functional countermodels show why those
claims remain outside the theorem.

### N8 — cross-route echo

The rearrangement proof, an independent exact nullspace computation, and
finite exhaustive integer checks agree on `[1:-n_color]` for the stated
domain. Independent two-way Bézout combinations plus the two exhaustive
residue classes modulo `2` prove the conditional GCD reduction for every
positive integer. The zero-pair route echoes the 2026-06-19 scope repair; the
independent scale and charge-functional routes address the distinct
2026-07-18 convention boundary.

## Cited dependencies

None. This theorem is a self-contained implication in elementary linear and
projective algebra. Plain-text reader pointers elsewhere in the note do not
seed dependency edges.

## Validation

Run all evidence modes:

```bash
python3 scripts/audit_companion_lh_traceless_eigenvalue_ratio_exact_2026_05_10.py --mode normal
python3 scripts/audit_companion_lh_traceless_eigenvalue_ratio_exact_2026_05_10.py --mode independent
python3 scripts/audit_companion_lh_traceless_eigenvalue_ratio_exact_2026_05_10.py --mode hostile
python3 scripts/audit_companion_lh_traceless_eigenvalue_ratio_exact_2026_05_10.py --mode all
```

The output reports theorem evidence, convention-supplied support arithmetic,
boundary/countermodel evidence, and hygiene evidence as separate counts. A
literal note string, cache header, or ledger status is not counted as theorem
evidence.

## Repair history

- **2026-06-19:** added the explicit nonzero-pair hypothesis and zero-solution
  guard.
- **2026-07-18:** restricted the clean claim to the homogeneous/projective
  implication, moved normalization/charge/denominator arithmetic to the dated
  convention boundary, and narrowed all three graph-direct consumers.
