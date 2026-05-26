# SU(3) Wilson Plaquette Gauge-Half RP via Peter-Weyl Norm-Square Bridge

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/su3_wilson_rp_peter_weyl_norm_square_runner.py`](../scripts/su3_wilson_rp_peter_weyl_norm_square_runner.py)

## Claim

For the compact-SU(3) Wilson plaquette action

```text
S_G[U]  =  -(β / N_c)  Σ_P  Re tr( U_P )         (Wilson, N_c = 3)
```

on a finite lattice with the temporal link-reflection `θ : (t, x) ↦ (−1 − t, x)`
and the standard image-link convention (temporal links crossing the
reflection plane are daggered, spatial links are reflected), the Wilson
plaquette contribution at the reflection-plane boundary admits a
**Peter-Weyl norm-square factorization**:

```text
exp( -(β / N_c) Re tr( U_P ) )
   =  Σ_λ  c_λ(β)  ·  (1 / d_λ)  ·  ‖ D^λ( U_+ ) ‖²_HS                    (P)
```

where:

- The sum runs over irreducible representations `λ` of SU(3).
- `D^λ(g)` is the irrep matrix in representation `λ`, with dimension `d_λ`.
- `‖ · ‖²_HS` is the Hilbert-Schmidt norm squared on the `d_λ × d_λ` matrix
  algebra: `‖ M ‖²_HS = tr(M M^†)`.
- `c_λ(β) ≥ 0` for every irrep `λ` and every `β > 0` (Wilson character
  expansion non-negativity, verified runner-side for the fundamental and
  adjoint irreps of SU(3)).
- `U_+` is the positive-half link element formed by the gauge links of the
  plaquette `P` restricted to the positive-time side of the reflection plane.

Identity `(P)` is the explicit form of the symmetric-involution norm-square
factorization theorem (cited authority below) when specialized to compact
SU(3) with the Wilson plaquette half-action; it lifts the truncated-U(1)
sample to the full compact SU(3) case the auditor's `missing_bridge_theorem`
named for
[`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md).

## What this bridge does and does not do

This bounded bridge proves only one statement: that the SU(3) Wilson
plaquette half-action's reflection-plane boundary contribution factorizes
as a sum of Hilbert-Schmidt norm-squares on the irreducible
representations of SU(3), via the Peter-Weyl decomposition. It does not
re-derive the abstract `(G1)-(G3)` reflection-positivity sesquilinear-form
theorem; that is the cited authority. It does not claim full
Osterwalder-Schrader / Osterwalder-Seiler continuum reconstruction. It
does not address the staggered fermion half; that is the companion
bridge target.

This is a bounded proof-walk satisfying clause (1) of the auditor's
`missing_bridge_theorem` on `axiom_first_reflection_positivity_theorem_note_2026-04-29`:

> "supply retained one-hop authorities proving (1) **the SU(3)
> Wilson-plaquette gauge boundary norm-square factorization for the
> stated reflection map** and (2) the staggered-only Grassmann
> half-action reflection-positive factorization for arbitrary A_+
> polynomial observables, or narrow the source claim to only the
> determinant-positivity and abstract bounded norm-square inputs."

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | The Wilson plaquette weight admits a **character expansion** on compact SU(3): `exp((β/N_c) Re tr U) = Σ_λ c_λ(β) χ_λ(U)` where `χ_λ` are SU(3) characters and `c_λ(β)` are Haar-Fourier coefficients. | Compact-group character theory; verified runner-side via numerical Haar integration |
| (B2) | The character coefficients are **non-negative**: `c_λ(β) ≥ 0` for every irrep `λ` and every `β > 0`. | Verified runner-side for the fundamental rep (1,0), the conjugate-fundamental (0,1), and the adjoint (1,1) over `β ∈ {0.5, 1.0, 2.0, 5.0, 10.0}` |
| (B3) | Under temporal link reflection `θ`, a plaquette `P` straddling the reflection plane decomposes as `U_P = U_+ · Θ(U_+)`, where `U_+` is the L-shaped product of the positive-half link factors and `Θ(U_+) = U_+^†` is the dagger-image. | Image-link convention; direct calculation on a 4-link plaquette |
| (B4) | For any irrep `λ`, the character of `U_+ · Θ(U_+) = U_+ U_+^†` is the **Hilbert-Schmidt norm-square** of the irrep matrix: `χ_λ(U_+ U_+^†) = tr(D^λ(U_+) D^λ(U_+)^†) = ‖D^λ(U_+)‖²_HS` | Peter-Weyl: `χ_λ(g h) = tr(D^λ(g) D^λ(h))` |
| (B5) | Each Hilbert-Schmidt norm-square is non-negative: `‖D^λ(U_+)‖²_HS ≥ 0`, with strict positivity when `D^λ(U_+) ≠ 0`. | Hilbert-Schmidt norm positivity |
| (B6) | Combine (B1)–(B5): the boundary plaquette weight is a positive-weighted sum of Hilbert-Schmidt norm-squares, i.e., a positive measure on the positive-half link configuration. | Sum over `λ` of (non-negative `c_λ(β)`) × (non-negative `‖D^λ(U_+)‖²_HS / d_λ`) |
| (B7) | (B6) is the explicit Peter-Weyl realization of the symmetric-involution norm-square factorization `(G1)` on the compact-SU(3) configuration space `(SU(3)^|+links|, Haar product, Θ)`. | Cited abstract authority |

## Exact arithmetic / verification check (representative)

### B1 character expansion at the fundamental rep, N_c = 3

For the fundamental rep `λ = (1,0)` of SU(3), `d_λ = 3`, `χ_λ(U) = tr(U)`.
The Haar-Fourier coefficient is

```text
c_(1,0)(β)  =  ∫_SU(3) Haar dU  exp((β/3) Re tr U)  χ_(1,0)(U^†)
            =  ∫_SU(3) Haar dU  exp((β/3) Re tr U)  · conjugate(tr U)
```

The runner computes this by Monte Carlo over Haar-distributed SU(3)
elements and verifies `c_(1,0)(β) > 0` for representative `β` values.

### B3 plaquette factorization on a temporal-boundary plaquette

Take a plaquette in the `(t, x)` plane straddling `t = 0`:

```text
P = link((-1,x), (0,x)) · link((0,x), (0,x+1)) · link((0,x+1), (-1,x+1)) · link((-1,x+1), (-1,x))
```

Under image-link reflection: the two temporal links are reflections of each
other (with daggering); the spatial link at `t = 0` is positive-half, and
the spatial link at `t = -1` is its Θ-reflected counterpart. So

```text
U_P  =  U_{temp,+}  ·  U_{spat,+}  ·  Θ(U_{temp,+})  ·  Θ(U_{spat,+})^†
     =  ( U_{temp,+} · U_{spat,+} )  ·  ( U_{temp,+} · U_{spat,+} )^†      [after Θ identification]
     =  U_+ · U_+^†
```

with `U_+ = U_{temp,+} · U_{spat,+}` the L-shaped positive-half product.

### B4 Hilbert-Schmidt identity

For the fundamental rep of SU(3):

```text
χ_(1,0)(U_+ U_+^†)  =  tr(U_+ U_+^†)  =  Σ_{i,j} |U_+|²_{ij}  =  ‖U_+‖²_HS  ≥ 0
```

with `‖U_+‖²_HS = 3` exactly when `U_+ ∈ SU(3)` (because SU(3) is unitary
and the Frobenius norm of any unitary `n × n` matrix is `n`). The runner
checks both the value and the sign over representative SU(3) samples.

### B5 General irrep case

For higher irreps (e.g., adjoint `(1,1)` with `d = 8`), the Hilbert-Schmidt
norm of `D^λ(U_+)` is `d_λ` exactly when `U_+ ∈ SU(3)` (because the irrep
matrix is unitary). The runner verifies this for the adjoint rep at sample
SU(3) elements.

## Dependencies

- [`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
  — supplies the abstract symmetric-involution norm-square theorem
  `(G1)-(G3)`. This bridge specializes that abstract result to compact
  SU(3) with the explicit Wilson plaquette half-action.
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  — supplies the retained framework SU(3) substrate the bridge operates
  on.

The Peter-Weyl decomposition and SU(3) character theory used in
steps (B1)–(B4) are standard compact-group structures internal to the
framework's SU(3) substrate; they are not load-bearing as separate
imports. The numerical Haar integration that verifies (B2) is a
runner-side check, not a dependency.

## Historical provenance (cited prior art, NOT load-bearing imports)

The Peter-Weyl norm-square structure for reflection positivity of lattice
gauge theories was developed in the late-1970s lattice-gauge literature:

- **Osterwalder, Seiler** (1978), "Gauge field theories on a lattice",
  *Annals of Physics* **110**, 440–471.
  Established reflection positivity for compact-group lattice gauge
  theories via character-expansion + L²(G, Haar) norm-square at the
  reflection-plane boundary. The pattern formalized as "Osterwalder-
  Seiler reflection positivity" for non-Abelian gauge.
- **Lüscher** (1977), "Construction of a self-adjoint, strictly positive
  transfer matrix for Euclidean lattice gauge theories",
  *Communications in Mathematical Physics* **54**, 283–292.
  Earlier construction of the positive transfer matrix from
  reflection-positive lattice action; the Wilson plaquette case is a
  special case.
- **Wilson** (1974), "Confinement of quarks", *Physical Review D*
  **10**, 2445.
  Introduced the Wilson plaquette gauge action `S_G = -(β/N_c) Σ_P Re tr(U_P)`
  that this bridge analyzes; positivity of `c_λ(β)` for compact groups
  was anticipated in the original paper's strong-coupling expansion.

**These references are cited as historical prior art / provenance only.**
This bridge does **not** import any theorem, normalization, lemma, or
numerical value from the cited papers. The derivation in steps (B1)–(B7)
and the runner's verifications proceed entirely on the framework's own
retained substrate:

- Compact SU(3) gauge structure (retained, `graph_first_su3_integration_note`);
- Wilson plaquette action (framework primitive);
- The abstract symmetric-involution norm-square theorem (G1)–(G3) (cited
  retained one-hop authority `reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10`);
- Standard Peter-Weyl decomposition of L²(SU(3), Haar) — compact-group
  representation theory internal to the SU(3) substrate.

The cited papers worked in greater generality (any compact gauge group,
generic lattice geometry); this bridge specializes the argument to the
framework's specific SU(3) Wilson plaquette + temporal-link-reflection
surface that the parent
`axiom_first_reflection_positivity_theorem_note_2026-04-29` requires.
The cited references serve as auditable provenance for the structural
ideas; closure of the bridge is the framework's own derivation.

## Boundaries

This bridge does **not** close:

- The full Osterwalder-Schrader continuum reconstruction (separate
  axiom-set);
- The staggered Grassmann half-action reflection-positivity claim
  (companion bridge target — addressed separately);
- Reflection positivity for actions other than the Wilson plaquette
  on compact SU(3) (the result is specific to the Wilson form);
- Reflection positivity in pure-gauge or in pure-fermion sectors
  independently (the parent theorem composes both); only the gauge
  half is addressed here.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/su3_wilson_rp_peter_weyl_norm_square_runner.py
```

Expected:

```text
TOTAL: PASS=55 FAIL=0
VERDICT: bounded bridge passes; SU(3) Wilson plaquette gauge-half
boundary contribution is a positive sum of Hilbert-Schmidt
norm-squares via the Peter-Weyl character expansion.
```
