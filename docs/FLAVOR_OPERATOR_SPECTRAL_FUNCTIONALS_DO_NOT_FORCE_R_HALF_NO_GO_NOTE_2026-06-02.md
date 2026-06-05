# Flavor Operator-Spectral Functionals Do Not Force r=1/2 No-Go

**Date:** 2026-06-02
**Claim type:** no_go
**Runner:** `scripts/flavor_operator_spectral_functionals_do_not_force_r_half_no_go_2026_06_02.py`

This note tests a narrow variational route for the generation weight parameter
`r = |b|^2/a^2`: do ordinary operator-spectral or Hilbert-Schmidt functionals
force the `r=1/2` point that gives `Q=2/3`? They do not. In the tested
`C_3`-circulant family, choice-free spectral functionals land at `r=0` or
`r=1`. The functionals that land at `r=1/2` first fold the two complex-conjugate
off-identity modes into one real doublet channel.

The framework baseline is
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md). Lattice and
Quantum supply the finite carrier and matrix algebra used in the runner. Record
does not supply the generation weight or the block-fold choice.

## Result

For the symmetric `C_3`-circulant form

```text
H = a I + b (J - I),
```

the runner verifies

```text
Q = Tr(H^2) / (Tr H)^2 = 1/3 + (2/3) r.
```

The target `r=1/2` is exactly the equal-Hilbert-Schmidt-energy point for the two
channels `I` and `J-I`:

```text
3 a^2 = 6 b^2.
```

That is a useful characterization, not a choice-free derivation. The runner then
tests spectral entropy, von Neumann entropy of `H^2/Tr(H^2)`, thermal entropy,
relative entropy to `I/3`, purity, the canonical Hilbert-Schmidt metric on the
`C_3` commutant, and transfer-positivity. None forces `r=1/2`.

The canonical Hilbert-Schmidt metric on `span{I,C,C^2}` weights the three modes
equally. That is the dimension-mode read and points to `r=1`, not `r=1/2`. To
reach `r=1/2`, the functional must first use the two-sector fold
`{C,C^2} -> C+C^2` and then impose a two-channel balance. That fold is the
block-count choice, not an output of the choice-free spectral functionals.

## Scope

This is not evidence against `Q=2/3`. It says only that `r=1/2` is not forced by
the tested operator-spectral/HS variational route. A chiral-sector theorem,
non-tracial reference state, finite-gap dynamics, or owner-approved block-count
admission can still select `r=1/2`.

## No-Go Discipline Gate

This gate applies only to the route above: deriving `r=1/2` from
choice-free operator-spectral or Hilbert-Schmidt variational functionals.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Spectral entropy | Maximize entropy of the three eigenvalue weights. | Peaks at the degenerate endpoint, not `r=1/2`. |
| Von Neumann entropy of `H^2/Tr(H^2)` | Use the induced spectral state. | Same endpoint behavior. |
| Thermal entropy | Use `exp(-H)/Z` as the state. | Does not select `r=1/2`. |
| Relative entropy to `I/3` | Minimize distance to the uniform three-mode state. | Selects the three-mode uniform endpoint. |
| Purity | Minimize `Tr rho^2`. | Again selects the three-mode uniform endpoint. |
| Canonical HS metric | Use the forced metric on `span{I,C,C^2}`. | Weights the three modes equally and gives `r=1`. |
| Transfer positivity | Use `exp(-tH)` positivity. | It is an inequality on the family and pins no interior point. |
| Two-sector entropy/imbalance | Fold `{C,C^2}` into one block and extremize. | Lands at `r=1/2`, but only after inserting the block fold. |

### N2 - Wall Independence

The collapsed wall is the two-sector block-fold choice. Spectral entropy,
purity, relative entropy, HS metric, and positivity are probes of the same
question: whether the block fold appears without being inserted. It does not.

### N3 - Hidden-Wall Scan

"Canonical HS" means the Hilbert-Schmidt form on the three commutant modes.
"Two-sector" means the separate fold that treats the doublet as one real block.
No chiral sector, reference-state dynamics, or Record weight is hidden inside the
operator-spectral route.

### N4 - Residual Matching

The residual is the block-fold / weight convention. It is not the algebraic
existence of the `r=1/2` equal-energy point and not the Koide line itself.

### N5 - Rhetoric Audit

"Does not force" is scoped to these variational functionals. The note does not
say `r=1/2` is unnatural, impossible, or unavailable as a chiral-sector value.

### N6 - Partial-Closure Path Scan

A chiral-sector theorem, a dynamical beta function with an `r=1/2` attractor, a
non-tracial reference derivation, or a block-count admission could still close
the value route.

### N7 - Steelman

A hostile reviewer can argue that the two-sector entropy is the natural
functional because the real doublet is one physical block. That is a coherent
block-count principle. It is also the extra fold this note isolates; it is not
produced by the choice-free three-mode spectral functionals.

### N8 - Cross-Cycle Echo

Other flavor notes separate available block-count characterizations from forced
value selection. This note adds the operator-spectral sweep: the `r=1/2`
characterization is real, but the functionals that produce it require the
block-fold input.

**Gate result:** pass for the operator-spectral variational route only.

## Validation

The runner checks finite symbolic and numerical facts:

- `Q = 1/3 + (2/3)r`;
- `r=1/2` equals the two-channel HS equipartition condition;
- ordinary spectral entropy, von Neumann entropy, relative entropy, and purity do
  not select `r=1/2`;
- the canonical HS metric on `span{I,C,C^2}` is three-mode isotropic;
- two-sector entropy and imbalance select `r=1/2` only after the block fold;
- the tested positive-transfer condition pins no interior point.
