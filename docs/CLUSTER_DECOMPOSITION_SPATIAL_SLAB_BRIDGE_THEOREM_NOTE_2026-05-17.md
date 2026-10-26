# Spatial-Slab Cluster-Decomposition Bridge on physical Cl(3) over Z^3

**Date:** 2026-05-17; 2026-06-06 finite-Lambda pure-Wilson H1/H2
authority wiring; 2026-06-06 compact trace-class scope and adjoint repair.
**Status:** source-note proposal; final claim type, audit verdict, and
effective status are set only by the independent audit lane.
**Type:** bounded_theorem
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The algebraic implication from H1+H2 to the stated finite-block bounds closes by spectral decomposition, Cauchy-Schwarz, and trace-distance control. The packet does not derive H1 or H2, so no unconditional spatial clustering claim closes."*

with repair: *"missing_bridge_theorem: add retained one-hop authorities constructing the positive Hermitian spatial slab transfer operator for the canonical Hamiltonian and proving Δ_x>0, then re-audit any unconditional promotion."*.

The 2026-05-28 repair took the **split path**:

- **Load-bearing (in scope):** The finite-dimensional spectral decomposition + Cauchy-Schwarz + trace-distance argument that, given hypotheses H1 (existence of positive Hermitian slab transfer operator `T_x`) and H2 (spatial gap `Δ_x > 0`), derives the exponential spatial clustering bounds (S.1)-(S.2) exactly. This chain is runner-verified and closes on its own conditional terms.
- **NON-load-bearing (split off / admitted on the full canonical surface):**
  The construction of a positive Hermitian spatial slab transfer operator
  `T_x` from the canonical physical Cl(3) over Z^3 Hamiltonian (H1) and the
  derivation of `Δ_x > 0` for that operator (H2); both require retained
  authority such as spatial OS reflection positivity or direct slab-positivity
  from the canonical action.

## 2026-10-23 correction to the historical H1/H2 wiring

The earlier 2026-06-06 physical pure-Wilson composition is withdrawn. The
axis-permutation companion [`CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md`](CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md) proves unitary relabeling of a supplied
smooth, strictly positive, real symmetric kernel, including its boundary data.
It does not identify that kernel with the physical Wilson transfer operator.
Its strict modulus gap is a property of the constructed operator. Pointwise
kernel positivity does not imply positive semidefiniteness: the matrix
[[1, 2], [2, 1]] has eigenvalues 3 and -1. Thus this result supplies neither
physical H1 nor physical H2 for the bridge below, even at finite Lambda.

The conditional spectral proof and no-gap counterexample below are unchanged.
An application requires the positive Hermitian operator and gap hypotheses,
physical partition-function and observable identification, and, on an infinite
Hilbert space, the stated trace-class conditions. Finite Lambda does not make
L^2(SU(3)^E) finite-dimensional. Full prior source is recoverable at commit
8c9957e651a04ae4e156e6cdacc608ffc93dc876; this correction changes no audit verdict.

**Loop:** `axiom-first-foundations`
**Cycle:** block-28 narrow closure follow-up to the 2026-05-09 temporal bridge
**Runner:** `scripts/cluster_decomposition_spatial_slab_bridge_check.py`
**Log:** `outputs/cluster_decomposition_spatial_slab_bridge_check_2026-05-17.txt`

## Why this note exists

The audit verdict on
`axiom_first_cluster_decomposition_theorem_note_2026-04-29` (recorded in
the audit ledger as a prior review/audit rationale) requests two repair targets:

> Repair target: derive Δ_T > 0 on the canonical Cl(3) ⊗ Z^3 staggered +
> Wilson Hamiltonian **and add a retained spatial cluster-decomposition
> theorem with constants**. Claim boundary until fixed: retain only
> L1/L3/L4 and conditional temporal gap-to-clustering support, not
> unconditional L2 spatial clustering.

The 2026-05-09 mass-gap bridge note
`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`
addresses the **temporal** part of repair target (b): it proves a
closed-form finite-block conditional bridge from `Δ_T > 0` to temporal
ground-state and finite-β connected-correlator decay (its theorem (B),
exhibits B.6–B.9).

This note is the **strict spatial-direction mirror** of that temporal
bridge. It proves, on the same finite-block surface, the closed-form
conditional spatial bridge:

> **(S)** Conditional on (i) existence of a positive Hermitian slab
> transfer operator `T_x` along one lattice direction `x ∈ {1, 2, 3}` of
> Z^3 perpendicular to a slab decomposition of Λ, and (ii) a spatial
> transfer-matrix spectral gap `Δ_x := -log(λ_1(T_x) / λ_max(T_x)) > 0`,
> the finite-block spatial connected correlator
>     | ⟨A_p · T̃_x^d · B_q⟩_0 - ⟨A_p⟩_0 ⟨B_q⟩_0 |
>         ≤ ‖A_p‖ ‖B_q‖ · exp(-d · Δ_x)
> holds for any operators `A_p, B_q` localized in slabs separated by `d`
> slab-units along direction `x`, with the analogous finite-temperature
> bound (S.8) holding for `0 < β < ∞`.

This addresses repair target (b) at the *same* authority level the
temporal bridge addresses the temporal side: it is a closed-form
finite-block conditional theorem, with the gap input made explicit. At the
general bridge level, the existence of `T_x` and `Δ_x > 0` are named
hypotheses. The supplied-kernel companion does not discharge these physical
hypotheses, including on the finite-Lambda pure-Wilson surface.

**What this note does NOT do.** It does not derive `Δ_x > 0` from
the full canonical framework baseline; it does not construct `T_x` from the
full canonical Hamiltonian (both physical identifications remain open,
including the proposed finite-Lambda pure-Wilson application); it does not derive `Δ_T > 0` (that remains the
second-named open derivation target across both spatial and temporal bridges).
The parent
`axiom_first_cluster_decomposition_theorem_note_2026-04-29` row's
unconditional L2 spatial claim therefore remains conditional pending
those derivations.

## Scope

This is a **bounded narrow theorem** in the spirit of the 2026-05-09
temporal bridge note. It mirrors that note's argument structure exactly:

- finite-dim spectral decomposition of a positive Hermitian operator
- Cauchy-Schwarz on the off-diagonal sum
- trace-distance control from a finite-temperature state to the
  ground-state projector

with the only change being the role of the operator: `T` (temporal
transfer matrix in the time direction) is replaced by `T_x` (slab
transfer matrix in a chosen lattice direction `x`), and the ground
state is the unique top eigenvector of `T_x` rather than of `T`.

## Framework Objects In Use

Same as the parent
`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`:

- **Physical Cl(3) local algebra** — finite-dimensional per-site algebra;
  Hermitian elements have finite operator norm.
- **Z^3 spatial substrate** — cubic lattice, supports slab decomposition
  perpendicular to any one of the three axis directions
  `x ∈ {1, 2, 3}`; the slab `Σ_n(x) := {p ∈ Λ : p_x = n}` is a
  two-dimensional sublattice of Z^2 type).
- **Finite-range Hermitian Hamiltonian setup** — `H = Σ_X h_X` with
  each `h_X` of diameter ≤ `R_int`. For the slab construction to be
  well-defined we use the standard slab partition `H = H_intra(x) +
  H_inter(x)` where `H_intra(x)` collects all terms with support
  entirely inside a single slab and `H_inter(x)` collects the cross-
  slab "link" terms.
- **Canonical normalization surface** — the existing `g_bare = 1`
  convention, used only to fix the operator norm of each `h_X` to an
  `O(1)` bound.

Only structural finite-dim properties are used. No infinite-volume
limit. No continuum limit.

## Inputs and support artifacts

- **Slab transfer matrix existence (hypothesis H1).** Existence of a
  positive Hermitian `T_x : H_slab(x) → H_slab(x)` on a finite-dim slab
  Hilbert space `H_slab(x)`, with `M_x := λ_max(T_x) > 0`, satisfying
  the standard slab construction `Z(Λ) = Tr(T_x^{L_x})` for the
  partition function on a block of length `L_x` along direction `x`.
  This is the spatial analogue of the reflection-positivity-derived
  temporal transfer matrix used by the 2026-05-09 bridge.
  **Canonical full-Hamiltonian status:** open input on the framework baseline;
  see `## Open hypotheses` below.
  **Supplied-kernel boundary:** the linked axis-permutation companion
  transports an assumed kernel. It does not establish this physical H1 or
  its partition-function identity.

- **Spatial transfer-matrix gap (hypothesis H2).** `Δ_x > 0`, where
  `Δ_x := -log(λ_1(T_x) / M_x)` and `λ_1(T_x)` is the second-largest
  eigenvalue (counted with multiplicity beneath the top). Equivalent to
  non-degeneracy of the top eigenvector of `T_x`. **Canonical
  full-Hamiltonian status:** open input on the framework baseline.
  **Supplied-kernel boundary:** the companion gives a modulus gap for its
  constructed operator. Physical transfer identification and positive
  semidefiniteness needed for this H2 application remain separate premises.

- **Parent LR bound (L1).** From the parent
  `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`. Cited
  as context for the parent row only; not load-bearing in the proof of
  (S) below. The proof of (S) is direct finite-dim spectral theory and
  does not import the LR series.

## Statement of the spatial-slab bridge (formal version)

Fix one lattice direction `x ∈ {1, 2, 3}` of Z^3 and let `Λ = {1, …, L_1}
× {1, …, L_2} × {1, …, L_3}` be a finite cubic block.

Let `H_slab(x)` be a finite-dim Hilbert space and let `T_x` be a positive
Hermitian operator on `H_slab(x)` (hypothesis H1). Let `M_x := λ_max(T_x)`
and `λ_1 := λ_2(T_x)` (second largest eigenvalue beneath the top, counted
with multiplicity). Define the spatial transfer-matrix gap

```text
    Δ_x  :=  -log(λ_1 / M_x)                                                  (S.5)
```

so that hypothesis H2 (`Δ_x > 0`) is equivalent to non-degeneracy of the
top eigenvector of `T_x`. Let `|0_x⟩ ∈ H_slab(x)` be the unique unit-norm
top eigenvector of `T_x`.

For operators `A_p` localized in slab `Σ_n` and `B_q` localized in slab
`Σ_{n + d}` (separation `d ≥ 1` along direction `x`), define
`T̃_x := T_x / M_x`. The slab-localized operators are bounded operators
on `H_slab(x)` (after their localization in slab `n` is folded through
the slab-projection conventions standard in lattice OS reconstruction).

**(S) Spatial-slab bridge theorem.** *Conditional on H1 and H2, for any
bounded operators `A_p, B_q` on `H_slab(x)`*:

**(S.1) Ground-state spatial clustering.** For any integer `d ≥ 1`,

```text
    ⟨0_x|  A_p · T̃_x^d · B_q  |0_x⟩  -  ⟨0_x|A_p|0_x⟩ ⟨0_x|B_q|0_x⟩
                                                                       (S.6)
        =     Σ_{k ≥ 1}  (λ_k / M_x)^d  · ⟨0_x|A_p|k⟩ ⟨k|B_q|0_x⟩
```

where `{|k⟩}_{k ≥ 0}` is an orthonormal eigenbasis of `T̃_x` with
eigenvalues `1 = (λ_0/M_x) > (λ_1/M_x) ≥ (λ_2/M_x) ≥ … ≥ 0`. Hence

```text
    | ⟨A_p · T̃_x^d · B_q⟩_0 - ⟨A_p⟩_0 ⟨B_q⟩_0 |   ≤   ‖A_p‖ · ‖B_q‖ · exp(-d · Δ_x).   (S.7)
```

**(S.2) Finite-temperature spatial bound.** Let `H̃_x := -(1/a_x) log T̃_x`
be the slab-Hamiltonian with spectrum `0 = E_0 < E_1 ≤ E_2 ≤ …` where
`E_k = -(1/a_x) log(λ_k / M_x)`. For any `0 < β < ∞`, the slab thermal
state `ρ_{β,x} := Z_{β,x}^{-1} exp(-β H̃_x)` satisfies

```text
    | ⟨A_p · T̃_x^d · B_q⟩_β - ⟨A_p⟩_β ⟨B_q⟩_β |
                                                                        (S.8)
        ≤   ‖A_p‖ · ‖B_q‖ · ( exp(-d · Δ_x)  +  6 q_{β,x} )
```

where `q_{β,x} := Tr(P_⟂ exp(-β H̃_x)) / Tr(exp(-β H̃_x))` is the
slab-excited-state population. Equivalently, with
`m_x := Δ_x / a_x` the slab gap and `D := dim H_slab(x)`,

```text
    q_{β,x}  ≤  (D - 1) exp(-β m_x) / (1 + (D - 1) exp(-β m_x)).         (S.9)
```

At zero temperature (`β → ∞`), `q_{β,x} → 0` and (S.8) reduces to (S.7).

**Compact trace-class extension.** The same ground-state proof also holds
when `H_slab(x)` is a separable Hilbert space, `T_x` is positive self-adjoint
trace-class, and the top eigenvalue is simple with `lambda_1 < M_x`. The
spectral theorem gives an orthonormal eigenbasis for the compact positive
operator and the off-ground sums below converge by Cauchy-Schwarz. Thus
(S.7) holds for bounded `A_p,B_q` on that compact trace-class surface.

The finite-temperature trace-distance form (S.8) holds on the compact surface
whenever the thermal operator `exp(-beta Htilde_x)` is trace-class and the
excited population `q_{beta,x}` in (S.16) is finite. The finite-dimensional
counting estimate (S.9) is not asserted on the compact surface.

**Conditional application boundary.** No physical pure-Wilson corollary is
established by the supplied-kernel companion. Applying this bridge requires
H1 and H2 for the intended physical operator. The compact extension additionally
requires its stated positivity and trace-class hypotheses; a strictly positive
kernel alone does not supply operator positive semidefiniteness or a
Hamiltonian logarithm.

**Not proved here.**

1. **Existence of `T_x` on the canonical Hamiltonian (H1).** Constructing
   a positive Hermitian slab transfer operator from the canonical
   physical Cl(3) over Z^3 staggered + Wilson Hamiltonian (e.g. via the standard
   slab-decomposition lemma of lattice statistical mechanics) is left as
   an open construction. The temporal analogue, via reflection
   positivity, is supplied by
   `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`.
   A spatial analogue requires either (a) a spatial reflection-positivity
   theorem along the chosen direction `x` (the standard OS construction
   restricted to a spatial axis), or (b) a direct slab-positivity
   argument (the columnar transfer-matrix construction of lattice
   statistical mechanics applied to the canonical action).

2. **Spatial gap `Δ_x > 0` (H2).** Equivalent in difficulty to deriving
   `Δ_T > 0` for the canonical Hamiltonian. Listed as an explicit open
   derivation target.

3. **Conversion between slab-localized and site-localized operators.**
   The (S) theorem speaks of operators "localized in a slab." Bridging
   to the parent note's site-localized operators `A_x, B_y` requires the
   standard slab-projection identification; this is a notational pass-
   through, not a new derivation, but it is listed for completeness.

## Proof of (S)

The proof mirrors the 2026-05-09 temporal bridge note's proof of (B)
exactly, replacing the temporal transfer matrix `T` by the slab transfer
matrix `T_x`.

### Step 1 — Spectral decomposition of T̃_x

`T̃_x := T_x / M_x` is positive Hermitian on the finite-dim slab Hilbert
space `H_slab(x)`. By H2, its spectrum satisfies
`1 = (λ_0/M_x) > (λ_1/M_x) ≥ … ≥ 0` with strict inequality at the top.
By the finite-dim spectral theorem,

```text
    T̃_x   =   Σ_{k ≥ 0}  (λ_k / M_x) · |k⟩⟨k|                                  (S.11)
```

with `|k⟩` an orthonormal eigenbasis of `T̃_x`. The power:

```text
    T̃_x^d   =   Σ_{k ≥ 0}  (λ_k / M_x)^d · |k⟩⟨k|.                              (S.12)
```

### Step 2 — Ground-state spatial clustering (proves S.1)

For any bounded operators `A_p, B_q` on `H_slab(x)` and any `d ≥ 1`,

```text
    ⟨0_x|  A_p · T̃_x^d · B_q  |0_x⟩
       =  Σ_{k ≥ 0}  (λ_k / M_x)^d · ⟨0_x|A_p|k⟩ · ⟨k|B_q|0_x⟩
                                                                     (S.13)
       =  ⟨0_x|A_p|0_x⟩⟨0_x|B_q|0_x⟩  +  Σ_{k ≥ 1}  (λ_k/M_x)^d · ⟨0_x|A_p|k⟩⟨k|B_q|0_x⟩.
```

This is (S.6). For the bound (S.7):

```text
    | ⟨A_p · T̃_x^d · B_q⟩_0 - ⟨A_p⟩_0 ⟨B_q⟩_0 |
        =  | Σ_{k ≥ 1}  (λ_k/M_x)^d · ⟨0_x|A_p|k⟩⟨k|B_q|0_x⟩ |
        ≤  (λ_1/M_x)^d · Σ_{k ≥ 1} |⟨0_x|A_p|k⟩| · |⟨k|B_q|0_x⟩|       ((λ_k/M_x)^d ≤ (λ_1/M_x)^d)
        ≤  (λ_1/M_x)^d · ( Σ_{k ≥ 1} |⟨0_x|A_p|k⟩|² )^{1/2}
                       · ( Σ_{k ≥ 1} |⟨k|B_q|0_x⟩|² )^{1/2}            (Cauchy-Schwarz)
        ≤  (λ_1/M_x)^d · ‖A_p^†|0_x⟩‖ · ‖B_q|0_x⟩‖
        ≤  (λ_1/M_x)^d · ‖A_p‖ · ‖B_q‖
        =  exp(-d · Δ_x) · ‖A_p‖ · ‖B_q‖.                                    (S.14)
```

The penultimate line uses
`Σ_{k ≥ 1}|⟨0_x|A_p|k⟩|² = ‖P_⟂ A_p^†|0_x⟩‖² ≤ ‖A_p^†|0_x⟩‖²` and
`Σ_{k ≥ 1}|⟨k|B_q|0_x⟩|² = ‖P_⟂ B_q|0_x⟩‖² ≤ ‖B_q|0_x⟩‖²`.
The last line uses `(λ_1/M_x)^d = exp(-d · log(M_x/λ_1)) = exp(-d · Δ_x)`,
which is (S.7). ∎

### Step 2b — Compact trace-class extension

If `T_x` is positive self-adjoint trace-class on a separable Hilbert space,
then `Ttilde_x` is compact and has a countable orthonormal eigenbasis for the
closure of its range, with eigenvalues decreasing to zero. A simple top
eigenvalue and `lambda_1 < M_x` give the same gap `Delta_x`.

For bounded `A_p,B_q`, the expansion (S.13) and the Cauchy-Schwarz estimate
above remain valid with infinite sums: the coefficient sequences are the
square-summable coordinates of `P_perp A_p^dagger|0_x>` and
`P_perp B_q|0_x>`. Therefore (S.7) holds on the compact trace-class surface.
For finite temperature, the same trace-distance proof applies if
`exp(-beta Htilde_x)` is trace-class; this condition is explicit and is not
replaced by a finite-dimensional `D` count.

### Step 3 — Finite-temperature spatial bound (proves S.2)

Write `H̃_x := -(1/a_x) log T̃_x`, the slab-Hamiltonian with spectrum
`0 = E_0 < E_1 ≤ E_2 ≤ …` where `E_k = -(1/a_x) log(λ_k/M_x)`. The
thermal state at slab-inverse-temperature `β` is

```text
    ρ_{β,x}  :=  Z_{β,x}^{-1} · exp(-β H̃_x),     Z_{β,x} = Σ_k exp(-β E_k).    (S.15)
```

Let `P_0 := |0_x⟩⟨0_x|` and `P_⟂ := I - P_0`. Define

```text
    q_{β,x} := Tr(P_⟂ exp(-β H̃_x)) / Tr(exp(-β H̃_x)).                       (S.16)
```

Then `ρ_{β,x} = (1 - q_{β,x}) P_0 + q_{β,x} σ_⟂` for a density matrix
`σ_⟂` supported on the excited subspace, so
`‖ρ_{β,x} - P_0‖_1 = 2 q_{β,x}`. For `X_d := A_p T̃_x^d B_q`,
`‖X_d‖ ≤ ‖A_p‖ ‖B_q‖`, hence

```text
    |Tr(ρ_{β,x} X_d) - ⟨0_x|X_d|0_x⟩|  ≤  2 q_{β,x} ‖A_p‖ ‖B_q‖.            (S.17)
```

Similarly,

```text
    |Tr(ρ_{β,x} A_p) Tr(ρ_{β,x} B_q) - ⟨A_p⟩_0 ⟨B_q⟩_0|  ≤  4 q_{β,x} ‖A_p‖ ‖B_q‖.   (S.18)
```

Combining (S.17), (S.18), and the ground-state bound (S.7):

```text
    | ⟨A_p · T̃_x^d · B_q⟩_β - ⟨A_p⟩_β ⟨B_q⟩_β |
       ≤   ‖A_p‖ ‖B_q‖ · ( exp(-d · Δ_x) + 6 q_{β,x} ).                       (S.19)
```

This is (S.8). The slab finite-block estimate
`q_{β,x} ≤ (D - 1) exp(-β m_x) / (1 + (D - 1) exp(-β m_x))` where
`D := dim H_slab(x)` and `m_x := Δ_x / a_x` follows from
`E_k ≥ m_x` for `k ≥ 1` and the Boltzmann distribution. ∎

## Closed-form identity content + counter-example

Step 1 (S.11)–(S.12) is the finite-dim spectral theorem; Step 2's (S.13)
is an exact identity; Step 2's (S.14) bound is Cauchy-Schwarz; Step 3's
(S.17)–(S.19) bound is trace-distance control plus the (S.7) ground-state
bound. The full chain is closed-form finite-dim spectral theory.

The gap input `Δ_x > 0` is genuinely required: with `Δ_x = 0` (degenerate
top eigenvector) the prefactor `(λ_1 / M_x)^d = 1` for all `d` and no
spatial decay is obtained. The runner exhibits this no-gap counter-example
in exhibit `E6` (mirror of the temporal bridge's `E4`).

## Where the gap input enters and what closes it

`Δ_x > 0` enters in three places, exactly as `Δ_T > 0` enters in the
temporal bridge:

1. Strict inequality `(λ_1 / M_x) < 1` — used in (S.14) to obtain
   exponential decay rather than `O(1)` bounds.
2. `m_x := Δ_x / a_x > 0` — used to make the slab-thermal excited-state
   population `q_{β,x}` vanish as `β → ∞`.
3. `E_k ≥ E_1 > 0` for `k ≥ 1` — automatic on finite-dim spectrum
   ordering, but `E_1 > 0` follows from `Δ_x > 0`.

The identity content of (S) is closed-form finite-block spectral theory.
The gap input `Δ_x > 0`, like its temporal cousin `Δ_T > 0`, is the open
derivation target on the physical Cl(3) local algebra over the Z^3
spatial substrate for the canonical Hamiltonian.

## Hypothesis set used

This bounded narrow theorem uses:

- the framework objects named above (only via the parent note's setup;
  no new premise is introduced here);
- the standard slab decomposition `Λ = ⊔ Σ_n(x)` of a finite cubic block;
- **named open inputs:**
  - **H1.** Existence of a positive Hermitian slab transfer operator
    `T_x : H_slab(x) → H_slab(x)`.
  - **H2.** Spatial transfer-matrix gap `Δ_x > 0` for the slab transfer
    operator.

H1 and H2 remain explicit physical inputs, including for the proposed
finite-Lambda pure-Wilson application. The companion [`CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md`](CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md)
provides conditional kernel relabeling, not physical transfer identification.
The conditional theorem (S) follows from H1 + H2 by the spectral argument above.

Standard finite-dim spectral theorem (resolution of identity for positive
Hermitian on finite-dim Hilbert space) is the only "standard mathematical"
input — the same authority level used by the 2026-05-09 temporal bridge
note.

## Honest status

**Closed-form finite-block spatial bridge.** (S.1)–(S.2) are proved on
the finite-block slab transfer-matrix surface, conditional on H1
(existence of `T_x`) and H2 (`Δ_x > 0`). The proof is spectral
decomposition + Cauchy-Schwarz + trace-distance estimate; no
Hastings-Koma constants, no LR series, no continuum limit.

**The bridge does not derive H1 or H2.** Both are explicitly named
open inputs that mirror, on the spatial side, the open input
`Δ_T > 0` of the temporal bridge. This note **explicitly tags** both
H1 and H2 as the spatial open derivation targets; H2 is at the same
difficulty level as the temporal gap, while H1 (slab transfer-matrix
existence) requires either spatial OS reflection positivity along the
chosen axis or a direct columnar-transfer-matrix construction on the
canonical action.

**Supplied-kernel composition boundary.** The axis-permutation companion
preserves a constructed operator's spectrum under unitary relabeling. Physical
Wilson transfer identification and positive semidefiniteness are not derived.
The bridge remains conditional; its finite-dimensional bounds and compact
extension retain exactly their stated hypotheses.

**What this rules out.**

- No unconditional canonical or finite-Lambda pure-Wilson spatial clustering
  follows from these supplied-kernel diagnostics.
- H1 and H2 imply the stated finite-dimensional bounds; the compact extension
  requires its explicit operator and thermal trace-class hypotheses.
- The parent physical L2 claim still requires the missing physical inputs.

**Repair targets for full closure (still open).**

1. **First-principles construction of `T_x` on the canonical
   Hamiltonian.** Two routes: (i) spatial OS reflection positivity along
   the chosen lattice axis (rotate the standard OS construction by 90°);
   (ii) direct columnar slab-positivity argument from the physical Cl(3)
   over Z^3
   staggered + Wilson Boltzmann weight.
2. **First-principles derivation of `Δ_x > 0`.** Same difficulty class
   as `Δ_T > 0`; candidates are strong-coupling expansion convergence,
   slab Perron-Frobenius, or a structural confinement theorem.
3. **First-principles derivation of `Δ_T > 0`** (still the second-named
   open input, see the 2026-05-09 temporal bridge note).

## Relationship to the parent and temporal bridge

The parent
`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`
holds L1, L3, L4 closed-form, and L2 conditional on (a) the temporal
bridge (closed-form, open input `Δ_T > 0`) and (b) a spatial cluster
theorem with constants.

With this note, (b) is satisfied in the same conditional form as (a) on the
finite-dimensional bridge surface: the chain "H1 and H2 imply spatial
clustering" is closed-form, mirroring "`Delta_T > 0` implies temporal
clustering." The 2026-06-02 companion does not discharge H1 or H2 for a
physical pure-Wilson operator. Physical transfer identification, positivity,
partition-function and observable correspondence remain open, as do any
thermodynamic or continuum claims. The conditional bridge is available once
its premises are independently established.

## Citations

- framework baseline: [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- parent cluster-decomposition note (context for the prior repair request;
  not a load-bearing dependency of this bounded theorem):
  `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`
- 2026-05-09 temporal bridge (context for the spatial mirror; the proof
  here is direct finite-dimensional spectral theory):
  `CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`
- conditional supplied-kernel relabeling companion:
  [`CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md`](CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md)
- reflection-positivity support note (defines temporal `T`):
  `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`
- spectrum-condition support note (defines `H̃ ≥ 0`):
  `AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`
- Lieb-Robinson microcausality (downstream consumer of L1):
  `AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`

## Audit dependency note

This note is a bounded theorem with three surfaces:

- General bridge surface: conditional on explicit H1 and H2.
- Finite-dimensional surface: H1 and H2 imply both the ground-state and
  finite-temperature bounds, including the finite `D` estimate.
- Compact conditional surface: the stated positive self-adjoint trace-class
  operator and gap imply the ground-state bound; finite temperature requires
  the explicit thermal trace-class condition. The kernel companion does not
  establish the physical identification or operator positivity premises.

It does **not** promote the parent row's audit status. The supplied-kernel
companion is a conditional mathematical dependency, not an authority supplying
physical H1/H2. The physical pure-Wilson and full staggered+Wilson applications
remain open. No generated citation graph or audit status is changed here.
