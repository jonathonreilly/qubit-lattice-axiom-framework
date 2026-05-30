# No γ_5 Chirality Operator in the Supplied Cl(3) Pauli M_2(C) Rep

**Date:** 2026-05-02
**Type:** no_go
**Claim scope:** in the supplied complex Pauli representation
`rho: Cl(3) -> M_2(C)`, `gamma_i -> sigma_i`, the Cl(3) volume element
`omega = gamma_1 gamma_2 gamma_3` acts as the central scalar `i I_2`.
Therefore there is **no element of `M_2(C)` that
anticommutes with all three Cl(3) generators σ_i**, and in particular no
γ_5 candidate satisfying γ_5² = +I_2 with {γ_5, σ_i} = 0. Per-site chirality
operators do not exist inside this supplied Pauli carrier. This narrowed note
does not identify the physical framework carrier `H_x` with that supplied
representation.
**Status:** independent audit required.
**Runner:** `scripts/no_per_site_chirality_check.py`
**Log:** `outputs/no_per_site_chirality_check_2026-05-02.txt`

## Framework-carrier bridge not claimed

The earlier source wording cited
`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md` for a
framework-level identification of `H_x ~= C^2`. Independent audit correctly
held that bridge conditional. This narrowed note does **not** consume that
bridge as load-bearing authority. It proves only the supplied-Pauli
`M_2(C)` algebraic no-go.

## Admitted-context inputs

- **Standard Clifford-algebra volume-element identity.** In Cl(p, q) with
  n = p + q, the volume element ω = e_1 e_2 ... e_n satisfies
  ω · e_μ = (-1)^(n-1) e_μ · ω. For n = 3 (odd), ω commutes with every
  generator. Standard reference: Lawson–Michelsohn, *Spin Geometry*, Ch. I.
- **Pauli matrices are a C-linear basis for M_2(C).** Standard fact: any
  2x2 complex matrix decomposes uniquely as a·I + b·σ_1 + c·σ_2 + d·σ_3.

Both are pure mathematical facts; no admitted physics conventions.

## Statement

Fix the supplied complex Pauli representation of `Cl(3)` on `C^2`, with
generators acting as Pauli matrices `gamma_i -> sigma_i`. Define the Cl(3)
volume element

```text
    ω  :=  γ_1 γ_2 γ_3.                                                     (1)
```

Then:

**(N1) ω is central in Pauli rep.** ω = i·I_2; in particular [ω, σ_i] = 0
for every i.

**(N2) ω² = -I_2.** Direct computation (i·I)² = -I.

**(N3) No γ_5 candidate exists.** There is no element γ_5 ∈ M_2(C) such
that
- γ_5² = +I_2 (involution), and
- {γ_5, σ_i} = 0 for every i (anticommutes with all Cl(3) generators).

Equivalently, the only M ∈ M_2(C) satisfying {M, σ_i} = 0 for all i is
M = 0 (which fails the involution condition).

**(N4) Even/odd subalgebras coincide on Pauli rep.** The Z_2-graded
subalgebras Cl(3)_even = span{I, σ_iσ_j} and Cl(3)_odd = span{σ_i, ω}
each span the full M_2(C) when projected to Pauli rep. There is no
internal Z_2 grading, hence no chirality projector P_± = (1 ± γ_5)/2.

## Proof

### Step 1 — Supplied Pauli representation

We assume only the supplied representation `gamma_i -> sigma_i` inside
`M_2(C)`. No framework-level physical carrier identification is used.

### Step 2 — Volume element computation (N1, N2)

Direct multiplication in the Pauli basis:

```text
    ω  =  σ_1 σ_2 σ_3
       =  σ_1 · (σ_2 σ_3)
       =  σ_1 · (i σ_1)
       =  i · σ_1²
       =  i · I_2.                                                          (2)
```

Hence ω = i·I_2 is a scalar (proportional to identity), so it commutes
with every σ_i — establishing (N1). Squaring: ω² = (i·I)² = -I_2 —
establishing (N2).

### Step 3 — No M anticommutes with all σ_i (N3)

Suppose M ∈ M_2(C) satisfies {M, σ_i} = 0 for all i. Decompose M in the
Pauli basis:

```text
    M  =  a·I  +  b₁·σ_1  +  b₂·σ_2  +  b₃·σ_3                            (3)
```

with a, b_k ∈ C. Computing the anticommutator with σ_j and using
{σ_j, σ_k} = 2 δ_{jk} I:

```text
    {M, σ_j}  =  2a · σ_j  +  Σ_k b_k · {σ_k, σ_j}
              =  2a · σ_j  +  2 b_j · I_2.                                  (4)
```

For this to vanish, we need both 2a = 0 (coefficient of σ_j) and
2 b_j = 0 (coefficient of I_2). Since this must hold for all j ∈ {1,2,3},
we get a = b_1 = b_2 = b_3 = 0, i.e. M = 0.

The zero matrix has 0² = 0 ≠ I_2, so it fails the involution condition
γ_5² = +I_2. Therefore no γ_5 candidate exists — establishing (N3).

### Step 4 — Even/odd subalgebra collapse (N4)

In Pauli rep:
- Even subalgebra basis (degree 0 + degree 2): {I, σ_1σ_2 = i σ_3,
  σ_2σ_3 = i σ_1, σ_3σ_1 = i σ_2}, which as a C-span equals
  span{I, σ_1, σ_2, σ_3} = M_2(C).
- Odd subalgebra basis (degree 1 + degree 3): {σ_1, σ_2, σ_3,
  σ_1σ_2σ_3 = i I}, which also as a C-span equals M_2(C).

Both subalgebras span all of M_2(C) when extended to C-coefficients.
The Z_2 grading, real and nontrivial in Cl(3) over R, becomes invisible
in the complex Pauli rep — the rep "doesn't see" the chirality split.
Hence there is no projector P_± = (1 ± γ_5)/2 internal to the supplied
Pauli `M_2(C)` carrier — establishing (N4). ∎

## Hypothesis set used

- Supplied complex Pauli representation `gamma_i -> sigma_i` inside `M_2(C)`.
- Standard Clifford volume-element identity (mathematical, admitted-context).
- Pauli matrices span M_2(C) (mathematical, admitted-context).

No fitted parameters. No observed values. No physics conventions admitted
beyond the supplied Pauli representation.

## Corollaries

C1. **No Pauli-carrier chirality projector.** A "left/right" projection cannot
be defined by an operator internal to the supplied `M_2(C)` Pauli carrier that
anticommutes with all three `sigma_i`.

## Out of scope

This note does not derive a temporal direction, 3+1 signature, Standard Model
left/right gauge assignments, a physical chirality mechanism, or the
framework-level identification `H_x ~= C^2`. It only proves the supplied
`M_2(C)` no-go above. Any claim that a larger Clifford algebra supplies
physical γ_5 structure belongs to a separate theorem and runner.

## Honest status

No-go theorem inside the supplied complex Pauli `M_2(C)` representation,
derived by elementary matrix algebra in the Pauli basis. The volume element
identity is standard Clifford theory; the no-γ_5 conclusion follows by
exhausting the Pauli basis decomposition. The framework-H_x carrier bridge is
out of scope.

```yaml
claim_type_author_hint: no_go
claim_scope: "Supplied Cl(3) Pauli M_2(C) representation: volume element omega = i I; no gamma5/chirality operator exists inside M_2(C)."
upstream_dependencies: []
admitted_context_inputs:
  - Clifford volume-element commutation identity (Lawson–Michelsohn)
  - Pauli matrices span M_2(C) (basic linear algebra)
  - supplied Pauli representation gamma_i -> sigma_i
```
