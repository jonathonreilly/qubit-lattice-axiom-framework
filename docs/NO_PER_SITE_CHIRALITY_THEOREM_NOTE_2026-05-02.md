# No γ_5 Chirality Operator in the One-Qubit Operator Algebra

**Date:** 2026-05-02
**Type:** no_go
**Claim scope:** in the Axiom 1 one-qubit operator algebra
`A_x ≅ M_2(C)`, choose any Pauli generating triple for the local
`Cl(3,0)` presentation. The Cl(3) volume element
`omega = gamma_1 gamma_2 gamma_3` acts as the central scalar `i I_2`.
Therefore there is **no element of `M_2(C)` that anticommutes with all
three Pauli generators σ_i**, and in particular no γ_5 candidate satisfying
`γ_5^2 = I_2` with `{γ_5, σ_i} = 0`. Per-site chirality projectors do not
exist inside the single-site one-qubit operator algebra.
**Status:** independent audit required.
**Runner:** `scripts/no_per_site_chirality_check.py`
**Log:** `outputs/no_per_site_chirality_check_2026-05-02.txt`

## Authority Boundary

[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) supplies
Axiom 1: a qubit at every lattice site, equivalently the primitive local
operator algebra `A_x ≅ M_2(C)`. The
[`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
supplies the two simple-module classes of the complexification and the
fixed-sign uniqueness of the selected Pauli quotient. The proof below is only
a single-site matrix no-go; it does not derive a temporal direction, a
spacetime Clifford algebra, Standard Model left/right assignments, or a
physical chirality mechanism.

## Admitted-Context Inputs

- **Pauli basis for `M_2(C)`.** Every `2 x 2` complex matrix decomposes
  uniquely as `a I + b_1 σ_1 + b_2 σ_2 + b_3 σ_3`.
- **Direct volume-element computation.** In the Pauli realization,
  `σ_1 σ_2 σ_3 = i I`.

Both are finite-dimensional matrix computations carried out below. A
standard odd-dimensional Clifford-volume statement gives parallel
mathematical context, but it is not imported as a load-bearing theorem.
The 2026-05-29 repair removes the previous load-bearing appeal to the
older per-site uniqueness row, because that theorem is now correctly
scoped away from the Axiom 1 local-algebra statement used here.

## Statement

Fix a Pauli presentation of the single-site one-qubit operator algebra
`A_x ≅ M_2(C)`, with generators acting as Pauli matrices
`gamma_i -> sigma_i`. Define the Cl(3) volume element

```text
    ω := σ_1 σ_2 σ_3.                                                       (1)
```

Then:

**(N1) Volume element is scalar.** `ω = i I`; hence `[ω, σ_i] = 0`.

**(N2) No universal anticommuting element.** The only
`M ∈ M_2(C)` satisfying `{M, σ_i} = 0` for all `i = 1,2,3` is `M = 0`.

**(N3) No γ_5 candidate.** There is no `γ_5 ∈ M_2(C)` satisfying
`γ_5^2 = I` and `{γ_5, σ_i} = 0` for all `i`.

**(N4) No intrinsic one-site chirality projector.** Since no such
`γ_5` exists, no projector pair `(1 ± γ_5)/2` exists internally to the
single-site Axiom 1 qubit algebra.

## Proof

### Step 1 — Axiom 1 One-Qubit Algebra

By Axiom 1, each site carries the one-qubit operator algebra
`A_x ≅ M_2(C)`. Choosing a Pauli generating triple is a presentation of
that algebra, not an added physical premise.

### Step 2 - Volume Element (N1)

Using the Pauli multiplication rules,

```text
    ω = σ_1 σ_2 σ_3
      = σ_1 (i σ_1)
      = i σ_1^2
      = i I.                                                               (2)
```

Thus `ω` is a scalar and commutes with each `σ_i`.

### Step 3 - Exhaust the Pauli Basis (N2)

Let `M ∈ M_2(C)` and write it in the Pauli basis:

```text
    M = a I + b_1 σ_1 + b_2 σ_2 + b_3 σ_3.                                 (3)
```

For a fixed `j`,

```text
    {M, σ_j} = 2a σ_j + Σ_k b_k {σ_k, σ_j}
             = 2a σ_j + 2 b_j I.                                           (4)
```

If `{M, σ_j} = 0`, the linearly independent coefficients of `σ_j` and
`I` force `a = 0` and `b_j = 0`. Requiring this for all
`j = 1,2,3` gives

```text
    a = b_1 = b_2 = b_3 = 0,
```

so `M = 0`. Therefore zero is the only matrix in `M_2(C)` that
anticommutes with all three Pauli generators.

### Step 4 - Exclude γ_5 (N3, N4)

Both subalgebras span all of M_2(C) when extended to C-coefficients.
The Z_2 grading, real and nontrivial in Cl(3) over R, becomes invisible
in the complex Pauli rep — the rep "doesn't see" the chirality split.
Hence there is no projector `P_± = (1 ± γ_5)/2` internal to the single-site
one-qubit operator algebra — establishing (N4). ∎

## Hypothesis Set Used

- `minimal_axioms_2026-05-20`: Axiom 1 supplies the one-qubit operator
  algebra `A_x ≅ M_2(C)`.
- `cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10`:
  two-class complexified classification and fixed-sign Pauli uniqueness.
- Standard Clifford volume-element identity (mathematical, admitted-context).
- Pauli matrices span M_2(C) (mathematical, admitted-context).

No fitted parameters. No observed values. No physical chirality convention
is admitted.

## Corollaries

C1. **No Pauli-carrier chirality projector.** A "left/right" projection cannot
be defined by an operator internal to the one-site `M_2(C)` Pauli carrier that
anticommutes with all three `sigma_i`.

C2. **Larger chirality mechanisms remain separate.** Any physical
chirality construction must use additional structure beyond this one-site
`M_2(C)` no-go, such as a larger Clifford algebra, temporal/signature
data, multi-site structure, or independent gauge representation data.

This note does not derive a temporal direction, a 3+1 spacetime Clifford
algebra, Standard Model left/right assignments, or a physical chirality
mechanism. It only proves the single-site `M_2(C)` no-go above.

No-go theorem inside the single-site one-qubit operator algebra,
derived by elementary matrix algebra in the Pauli basis. The volume element
identity is standard Clifford theory; the no-γ_5 conclusion follows by
exhausting the Pauli basis decomposition.

## No-Go Discipline Gate

- **N1 alternative routes:** direct Pauli volume-element computation
  (`ATTEMPTED`); full Pauli-basis anticommutator exhaustion (`ATTEMPTED`);
  adding a fourth Clifford generator / temporal direction (`RULED OUT OF
  SCOPE`, separate larger-algebra route); multi-site or block chirality
  (`RULED OUT OF SCOPE`, not a single-site operator); gauge-representation
  left/right assignments (`RULED OUT OF SCOPE`, requires independent gauge
  structure).
- **N2 wall independence:** there is one wall only: no nonzero
  `M ∈ M_2(C)` anticommutes with all three Pauli generators. The larger
  routes are scoped alternatives, not additional walls.
- **N3 hidden-wall scan:** the note uses only Axiom 1 local algebra,
  fixed-sign Pauli-irrep uniqueness, and finite-dimensional Pauli arithmetic;
  temporal, gauge, and multi-site mechanisms are explicitly outside scope.
- **N4 residual matching:** the residual attacked is exactly "single-site
  γ_5 inside `M_2(C)`"; no claim is made against larger spacetime Clifford
  or gauge chirality mechanisms.
- **N5 rhetoric audit:** all negative wording is at the single-site /
  one-qubit operator-algebra resolution. Broader physical chirality language
  is excluded.
- **N6 partial-closure path scan:** a larger Clifford algebra or temporal
  direction could supply chirality, but that is a different theorem, not a
  counterexample to this single-site no-go.
- **N7 steelman:** a reviewer could build γ_5 after adding temporal or
  multi-site structure. That does not break the claim because this note
  rules out only an operator internal to one `M_2(C)` site.
- **N8 cross-cycle echo:** prior chirality lanes already separate
  single-site Cl(3) algebra from spacetime/gauge chirality. This note keeps
  that separation and does not close the larger lane.

Status: `PASS` for the narrowed single-site no-go.

```yaml
claim_type_author_hint: no_go
claim_scope: "One-qubit operator algebra M_2(C): volume element omega = i I; no gamma5/chirality operator exists inside one site."
upstream_dependencies:
  - minimal_axioms_2026-05-20
  - cl3_pauli_irrep_uniqueness_narrow_theorem_note_2026-05-10
admitted_context_inputs:
  - Clifford volume-element commutation identity (Lawson–Michelsohn)
  - Pauli matrices span M_2(C) (basic linear algebra)
```
