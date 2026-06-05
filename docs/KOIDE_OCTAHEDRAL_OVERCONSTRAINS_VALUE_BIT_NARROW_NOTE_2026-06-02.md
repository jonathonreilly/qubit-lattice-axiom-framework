# Octahedral Equivariance Over-Constrains the Koide Value-Bit Carrier

**Date:** 2026-06-02
**Claim type:** no_go
**Review provenance:** source theorem candidate; post-landing audit decides the
ledger grade. This note introduces no axiom, primitive, Tier-A admission, or
charged-lepton Koide derivation.
**Primary runner:** `scripts/frontier_koide_octahedral_overconstrains_value_bit.py`
(SCORECARD PASS=28)

## Claim

On the three-dimensional generation-axis carrier `R^3`, full octahedral
equivariance (`O_h`, signed permutations of the three axes) is too strong to
derive the `C_3` Koide value bit. It over-constrains the carrier:

- `C_3`-invariant symmetric forms on `R^3` have two dimensions, preserving the
  trivial/doublet weight freedom;
- `O_h`-invariant symmetric forms on `R^3` collapse to the one-dimensional round
  metric;
- the democratic direction `(1,1,1)` is not `O_h`-invariant, so `O_h` erases the
  trivial/doublet split on which the value bit is defined;
- any `O_h`-equivariant generation mass operator on `R^3` is scalar, hence
  degenerate;
- any `O_h`-equivariant operator anticommuting with the chiral grading is zero.

Therefore the full lattice point group does not pin `r = 1/2` or derive
`Q = 2/3`; it removes the nondegenerate carrier. The remaining positive route is
a `C_3`-level selection principle or another split-preserving structure, not
full `O_h` equivariance on the generation-axis carrier.

## Computation

The runner verifies:

1. `|O_h| = 48`, `|C_3| = 3`, and `C_3` is a subgroup of `O_h`.
2. The invariant symmetric-form space has dimension `2` for `C_3` and `1` for
   `O_h`; the unique `O_h` form is the round metric.
3. The democratic projector averages under `O_h` to `(1/3) I`, so the
   `C_3` trivial/doublet split is not preserved.
4. Round scalar rescaling does not select the spectrum split `A^2:D^2`; the
   example spectra with ratios `1:0`, `1:1`, and `1:2` give `Q = 1/3`, `2/3`,
   and `1` respectively.
5. The `O_h` commutant on `R^3` is one-dimensional, so an equivariant mass
   operator is scalar and degenerate.
6. `O_h`-equivariance also forces a chiral anticommuting operator to zero, while
   a non-circulant anticommuting witness exists outside the `O_h`-equivariant
   class.
7. On `Herm(3)`, the two Frobenius forms `Tr(XY)` and `tr(X)tr(Y)` remain
   `O_h`-invariant, so this note's collapse is specific to the `R^3`
   generation-axis carrier.
8. The largest `O_h` subgroup fixing `(1,1,1)` has order `6` and still leaves a
   two-dimensional weight freedom.

## No-Go Discipline Gate

**Gate result:** PASS for the scoped `O_h`-equivariance no-go only.

### N1 - Alternative Route Enumeration

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Metric route | Use `O_h` to collapse the `C_3` weight metric and select the value bit. | `O_h` collapses the metric to round, but a round metric does not select the spectrum split `A^2:D^2`. | ATTEMPTED |
| Block route | Use `O_h` to refine the `C_3` trivial/doublet split. | `O_h` erases the democratic direction; the split is no longer invariant. | ATTEMPTED |
| Mass-operator route | Demand an `O_h`-equivariant mass operator. | The commutant is scalar, so the spectrum is degenerate. | ATTEMPTED |
| Chiral route | Combine `O_h` equivariance with a nonzero anticommuting chiral operator. | The only `O_h`-equivariant anticommuting operator is zero. | ATTEMPTED |
| Intermediate subgroup route | Enlarge from `C_3` partway toward `O_h` to both preserve and pin the bit. | The split-preserving subgroup still leaves two-dimensional freedom; enlargements that add the needed sign flips erase the split. | ATTEMPTED |
| Hermitian-form route | Move the bit to `Herm(3)` rather than the axis carrier. | On `Herm(3)`, the Frobenius family remains two-dimensional, so the ratio is not pinned. | ATTEMPTED |
| `C_3` internal selector | Derive the value bit from a split-preserving `C_3` principle. | Out of scope and left open. | OUT OF SCOPE |

### N2 - Wall-Independence Audit

The collapsed wall set has one wall: full `O_h` over-constrains the
generation-axis carrier. Pairwise independence is therefore vacuous after
collapse. The metric, block, mass-operator, chiral, and intermediate-subgroup
routes are separate tests of this one wall, not separate admissions.

### N3 - Hidden-Wall Scan

Phrase scan result: no load-bearing step uses "we assume", "by construction",
"as is standard", "the framework provides", "bridge context", "naturally",
"obviously", or "canonical" as proof support. The note does not assume `O_h` is
the physical generation symmetry. It tests the candidate hypothesis and reports
that it over-constrains. `Q = 2/3` and `r = 1/2` are check targets only; the
computation uses finite group actions, linear algebra, and explicit
invariant-space dimensions.

### N4 - Residual Matching

| context row | residual it names | residual attacked here | match? |
|---|---|---|---|
| `koide_q23_oh_covariance_nogo_note_2026-04-22` | Full octahedral covariance is not available for the charged-lepton chart. | This note gives the structural reason on the `R^3` carrier: equivariant spectra are scalar. | yes |
| `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | The `C_3` scalar/doublet weight ratio is not forced by the Frobenius constraints. | This note tests whether enlarging to `O_h` forces it; it does not. | yes |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | The `C_3` chiral operator route has a scoped obstruction. | This note checks the stronger `O_h` version and finds only the zero operator. | yes |

### N5 - Rhetoric Audit

"Over-constrains" means full `O_h` removes the split or forces degeneracy; it
does not mean all possible value-bit derivations are closed. "Does not derive"
is scoped to `O_h` equivariance on the generation-axis carrier.

### N6 - Partial-Closure Path Scan

Open paths remain: a `C_3`-internal selection principle, a split-preserving
subgroup plus additional positivity/reality input, or a non-group-theoretic
functional on the circulant surface. None is called a new axiom here.

### N7 - Steelman

The strongest objection is that the lattice's own point group should be the
most natural source of a value selection. The computation grants that `O_h` is
strictly stronger than `C_3`; the problem is that this strength destroys the
carrier structure needed for a nondegenerate spectrum. Stronger symmetry is not
automatically more informative when it collapses the representation content.

### N8 - Cross-Cycle Echo

The common failure mode is to infer a value from a larger symmetry without
checking whether the target carrier survives that symmetry. This note explicitly
separates the metric, block, spectrum, operator, and subgroup readings, and
keeps the `C_3`-internal route open. The result does not say the value bit needs
new foundational input; it says this larger-symmetry mechanism is not the route.

## Cited Context

Context rows, not status claims:

- `koide_frobenius_isotype_split_uniqueness_note_2026-04-21`
- `koide_q23_oh_covariance_nogo_note_2026-04-22`
- `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16`
- `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`
- `koide_q23_block_weight_frontier_bounded_note_2026-05-29`
- `koide_generation_id_cl3_grade1_bridge_narrow_theorem_note_2026-06-02`

## Command

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_octahedral_overconstrains_value_bit.py
```

Expected output: `SCORECARD: PASS=28 FAIL=0`.
