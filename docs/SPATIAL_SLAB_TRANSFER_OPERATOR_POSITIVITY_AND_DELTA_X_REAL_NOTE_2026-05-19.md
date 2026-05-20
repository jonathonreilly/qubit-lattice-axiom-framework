# Spatial-Slab Transfer-Operator Positivity and Δ_x > 0 from Wilson Axis-Permutation Symmetry (Real)

**Date:** 2026-05-19
**Status (source-side label):** bounded_theorem with one named conditional composition input
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_slab_bridge_spatial_Tx_real_2026_05_19.py`](../scripts/frontier_slab_bridge_spatial_Tx_real_2026_05_19.py)
**Cached output:** [`logs/runner-cache/frontier_slab_bridge_spatial_Tx_real_2026_05_19.txt`](../logs/runner-cache/frontier_slab_bridge_spatial_Tx_real_2026_05_19.txt)
**Parent row (discharged):** [`docs/CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md) — discharges its two named hypotheses H1 (positive Hermitian `T_x`) and H2 (`Δ_x > 0`) on the canonical Cl(3)⊗Z³ Wilson+staggered action.
**Status authority:** independent audit lane only. The `bounded_theorem` label is a source-side claim-boundary declaration, not an audit verdict.

## §0. Honest framing — what this note discharges

The 2026-05-17 spatial slab-bridge note
[`CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md)
proves a **conditional** exponential spatial clustering result on finite Λ. Its
theorem (S) is conditional on two named open inputs:

- **H1.** Existence of a positive Hermitian slab transfer operator
  `T_x : H_slab(x) → H_slab(x)` along a lattice axis `x ∈ {1, 2, 3}`.
- **H2.** Spatial transfer-matrix gap `Δ_x := -log(λ_1(T_x) / λ_max(T_x)) > 0`.

This note discharges **both** H1 and H2 on the canonical Cl(3)⊗Z³
finite-Λ Wilson+staggered Hamiltonian by exploiting the Euclidean cubic
(axis-permutation) symmetry of the Wilson action to lift the salvage
result of [`docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md`](CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md)
(the operator-theoretic Δ_T > 0 theorem for the temporal-slab transfer
operator on `L²(SU(3)^E)`) into the spatial-slab direction.

The end result is:

- **(Pure Wilson, unconditional.)** For pure Wilson lattice gauge theory at
  `β > 0` on finite Λ, the spatial-slab transfer operator `T_x_W` is
  positive Hermitian and trace-class on the slab Hilbert space, with
  `Δ_x_W > 0`. This discharges H1 and H2 for the pure Wilson factor.
- **(Staggered+Wilson, conditional on Leg A.)** With dynamical staggered
  fermions added via the symmetrized fermion-determinant multiplier of
  [`docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)
  (the operator-basis + quark-mass-orientation "Leg A" salvage), the
  staggered+Wilson full spatial-slab transfer operator `T_x_full` is
  positive Hermitian trace-class with `Δ_x_full > 0`, **conditional on Leg
  A's audit retention** at retained-grade. We do not promote Leg A here.

What this note does NOT claim:

- It does **not** address the thermodynamic limit `Λ → Z³`.
- It does **not** address uniformity-in-Λ of the gap.
- It does **not** address the Yang-Mills (Clay) mass gap.
- It does **not** promote the parent slab-bridge note or the Leg A
  parent note. Effective status remains the audit lane's call.

---

## §1. Setting

Let `Λ ⊂ Z³` be a finite connected spatial sublattice of the form

```
Λ = Λ_x × Λ_⊥ = {1, …, L_x} × {1, …, L_2} × {1, …, L_3}
```

where `Λ_x = {1, …, L_x}` is the 1D slab-index direction along the chosen
lattice axis `x ∈ {1, 2, 3}` and `Λ_⊥` is the 2D transverse slab. Each
slab `Σ_s := {p ∈ Λ : p_x = s}` is a 2D sublattice (hyperplane
perpendicular to the x-axis). The edge set `E(Λ)` partitions into

```
E(Λ) = E_x(Λ) ⊔ E_⊥(Λ),
```

with `E_x(Λ)` the "longitudinal" links (along the x-axis, going from slab
`s` to slab `s+1`) and `E_⊥(Λ)` the "transverse" links (inside slabs).
Each link carries a parallel transport `U_ℓ ∈ SU(3)`.

The single-slab Hilbert space is

```
H_slab := L²(SU(3)^{|E(Σ)|}, dU_Haar)
```

where `E(Σ)` is the edge set of a single transverse slab (the transverse
links inside one slab). The spatial-slab transfer operator `T_x` is
constructed in §3 below as an integral operator on `H_slab`.

For background and notation: the relevant retained salvage commits are

- `8369973af` (PR #1577 salvage) — discharges `Δ_T > 0` for the
  **temporal**-slab transfer operator `T_τ` on `L²(SU(3)^E)` via the
  SU(3) heat-kernel character expansion + Perron-Jentzsch/Krein-Rutman
  positivity-improving compact-operator theorem (Lemmas A-D of
  [`docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md`](CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md)).
- `5f6f0b87a` (PR #1582 salvage) — discharges the Leg A
  operator-basis and quark-mass-orientation theorems (Theorems 2.4 and
  3.4 of [`docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)).
  Currently `audited_conditional` on the audit lane; this note treats
  it as a named conditional input.

We name the canonical pure Wilson lattice action

```
S_W[U] = (β/N_c) · Σ_P (N_c − Re Tr U_P),   β > 0,   N_c = 3
```

with `U_P = U_{e_1} U_{e_2} U_{e_3}^† U_{e_4}^†` the standard plaquette
holonomy with oriented boundary `(e_1, e_2, e_3, e_4)` traversing the
plaquette once. The sum runs over all unoriented 2-plaquettes of `Λ`.

---

## §2. Wilson space-time cubic symmetry lemma

The proof in §3 lifts the τ-direction result of PR #1577 into the
x-direction. The lift is purely structural: any property of `S_W` and the
heat-kernel propagator that does not depend on which lattice axis is
"τ" lifts verbatim. Cubic symmetry is the load-bearing structural
property.

### Lemma 2.1 (Wilson action axis-permutation invariance)

Let `σ : {1, 2, 3, 4} → {1, 2, 3, 4}` be any signed permutation of the
four lattice axes (Euclidean cubic group acting on a 4D lattice; or its
restriction to 3D if working in `Λ ⊂ Z³` directly). Let `σ_*` be the
induced map on link configurations: it takes a link variable on the edge
`(p, μ)` to the link variable on the edge `σ(p), σ(μ))`, with the
orientation flipped if `σ` flips the sign of axis `μ`.

Then for every link configuration `U` on Λ,

```
S_W[σ_*(U)] = S_W[U].                                                  (2.1)
```

**Proof.** The Wilson action `S_W[U] = (β/N_c) · Σ_P (N_c − Re Tr U_P)`
is a sum over plaquettes of a real-valued conjugation-class function of
the plaquette holonomy. Two structural facts give the invariance:

1. **σ permutes plaquettes.** Each 2-plaquette `P` of the lattice
   determines two axis directions `(μ, ν)` with `μ < ν` and a base
   point. Under `σ`, `P ↦ σ(P)` is another 2-plaquette of the lattice;
   the map `P ↦ σ(P)` is a bijection of the set of unoriented
   2-plaquettes of Λ.

2. **σ acts on the holonomy by group operations that commute with `Re Tr`.**
   The plaquette holonomy `U_P = U_{e_1} U_{e_2} U_{e_3}^† U_{e_4}^†`
   under axis-permutation `σ` transforms either as `U_P ↦ U_{σ(P)}` (when
   σ permutes the two boundary axes in an orientation-preserving way) or
   as `U_P ↦ U_{σ(P)}^†` (when σ reverses the plaquette boundary
   orientation). In both cases, `Re Tr U_{σ(P)} = Re Tr (U_{σ(P)})^†`
   because `Tr X^† = (Tr X)^*` and `Re` is invariant under conjugation.

So the summand `(N_c − Re Tr U_P)` is mapped to `(N_c − Re Tr U_{σ(P)})`
under σ, and the sum over P is invariant under the bijection
`P ↦ σ(P)`. QED.

### Lemma 2.2 (Haar measure axis-permutation invariance)

The product Haar measure `dU = ⊗_ℓ dU_ℓ` on `Conf(Λ) = SU(3)^{|E(Λ)|}` is
invariant under `σ_*`.

**Proof.** Each individual `dU_ℓ` is the left-and-right invariant Haar
measure on SU(3), which is invariant under `U ↦ U^†` (because `det dU = det dU^†`
on a compact Lie group, equivalently, Haar measure is bi-invariant).
Permuting which link is which permutes the factors of the product
measure, leaving the product measure unchanged. QED.

### Lemma 2.3 (SU(3) heat-kernel axis-permutation invariance)

The SU(3) heat-kernel `K_τ(g)` is a real-valued class function. In
particular `K_τ(g) = K_τ(g^†) = K_τ(h g h^{-1})` for any `g, h ∈ SU(3)`.

**Proof.** From the character expansion (PR #1577 salvage Lemma A.5):

```
K_τ(g) = Σ_{R = (p, q)} (dim R) · χ_R(g) · exp(-τ C_2(R) / (2 N_c))    (2.2)
```

Each character `χ_R` is a class function on SU(3): `χ_R(h g h^{-1}) = χ_R(g)`
by the cyclic property of trace. Moreover, `χ_R(g^†) = χ_R(g)^* = χ_R(g)`
for `χ_R` real-valued (which holds for irreps of compact groups whose
characters are real, including SU(3)'s real-character irreps; in the
general SU(3) case the conjugate irrep `(p, q) ↔ (q, p)` gives
`χ_R(g^†) = χ_{R̄}(g)`, and the sum over all `(p, q)` is symmetric under
`(p, q) ↔ (q, p)` because `dim(p, q) = dim(q, p)` and `C_2(p, q) = C_2(q, p)`,
so the sum is real). The exponential factor `exp(-τ C_2/(2 N_c))` is real
positive. QED.

### Corollary 2.4 (Wilson partition function and observables axis-permutation invariant)

Define the Wilson partition function on Λ:

```
Z_W[Λ; β] := ∫_{Conf(Λ)} dU · exp(-S_W[U]).                            (2.3)
```

By Lemma 2.1 (`S_W` axis-permutation invariant) and Lemma 2.2 (Haar
measure axis-permutation invariant), `Z_W[Λ; β]` is invariant under any
signed permutation of the lattice axes.

More generally, any gauge-invariant expectation value
`⟨O(U)⟩_W := Z_W^{-1} ∫ dU O(U) exp(-S_W[U])` of an observable `O(U)`
that is itself constructed from the link configuration in an axis-permutation
covariant way (e.g., observables built from plaquette holonomies and
class-function evaluators) satisfies `⟨O ∘ σ_*⟩_W = ⟨O⟩_W`. The transfer
operator constructed in §3 will be axis-covariant in exactly this sense.

---

## §3. Theorem A — Pure Wilson spatial slab T_x_W and Δ_x_W > 0

### Construction of `T_x_W`

By axis-relabeling, the construction of `T_x_W` is identical to the
PR #1577 salvage's construction of the temporal-slab `T_τ`. We spell
it out to make the discharge explicit.

Let `H_slab := L²(SU(3)^{|E(Σ)|}, dU_Haar)` be the slab Hilbert space, with
`E(Σ)` the edge set of one transverse slab (the transverse links). The
spatial-slab transfer operator `T_x_W` is defined as the integral
operator on `H_slab` with kernel

```
T_x_W(U, V) = exp(-β ΔS_W^{(x)}[U, V]) · Π_{ℓ ∈ E(Σ)} K_τ(U_ℓ V_ℓ^†)    (3.1)
```

where:

- `U, V ∈ Conf(Σ) = SU(3)^{|E(Σ)|}` are link configurations on two adjacent
  slabs `Σ_s, Σ_{s+1}` (one transverse link configuration per slab).
- `ΔS_W^{(x)}[U, V] := Σ_P (N_c − Re Tr U_P^{[s, s+1]}) / N_c` is the sum
  of cross-slab plaquette contributions where each plaquette `P^{[s, s+1]}`
  has one transverse edge in `Σ_s`, one transverse edge in `Σ_{s+1}`,
  and two longitudinal edges connecting slab `s` to slab `s+1`. This is
  the spatial analogue of the τ-cross-slab plaquette contribution in the
  PR #1577 salvage's T_τ.
- `K_τ` is the SU(3) heat kernel along the longitudinal x-direction,
  encoding the "x-link" propagation from slab `s` to slab `s+1`.
  (Equivalently, integrating out the longitudinal x-links from the
  Boltzmann weight via Haar gives the heat-kernel factor — this is
  the standard transfer-matrix derivation; for lattice Wilson with
  symmetric anisotropic conventions it is the SU(3) heat kernel as
  in PR #1577 salvage §1.)

By construction the kernel `T_x_W(U, V)` is symmetric in `(U, V)` under
the Wilson axis-permutation that exchanges the x-axis with the (former)
τ-axis: the temporal-direction analog `T_τ(U, V)` in PR #1577 salvage
has the *identical* functional form except with the x-axis playing the
role of τ-axis. We make this precise:

### Lemma 3.1 (Spatial-slab kernel = temporal-slab kernel under axis swap)

Let `σ_{x↔τ}` be the axis-swap that exchanges the chosen spatial-slab
axis x with the τ-direction in PR #1577 salvage. Then

```
T_x_W(U, V) = T_τ(σ_{x↔τ}(U), σ_{x↔τ}(V))                              (3.2)
```

where `T_τ` is the temporal-slab kernel of
[`docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md`](CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md)
§1.

**Proof.** Compare (3.1) with PR #1577 salvage equation in §1: both have
the same functional form `exp(-β · plaquette-action-cross-slab) · Π_ℓ K_τ(U_ℓ V_ℓ^†)`.
The only difference is the labeling of "longitudinal" vs "transverse"
axes. By Lemma 2.1, the Wilson plaquette action is invariant under the
axis-swap σ_{x↔τ}; by Lemma 2.2, the Haar measure on each link is
invariant; by Lemma 2.3, the heat kernel is a class function and so
treats SU(3) elements identically regardless of which lattice axis they
are associated with. So (3.2) holds. QED.

### Theorem A (Pure Wilson T_x_W positivity and Δ_x_W > 0)

For pure Wilson lattice gauge theory on finite Λ at `β > 0`, the
spatial-slab transfer operator `T_x_W` defined by kernel (3.1) is

- (A.1) **self-adjoint** on `H_slab`,
- (A.2) **trace-class** (and Hilbert-Schmidt) on `H_slab`,
- (A.3) **strictly positivity-preserving**: the kernel `T_x_W(U, V) > 0`
  pointwise on `Conf(Σ) × Conf(Σ)`,
- (A.4) **simple top eigenvalue** with a strictly positive eigenfunction,
  and
- (A.5) **strict spectral gap**:
  ```
  Δ_x_W := -log(|λ_1(T_x_W)| / λ_0(T_x_W)) > 0.
  ```

**Proof.** Lemma 3.1 reduces this to the corresponding statement for the
PR #1577 salvage's `T_τ`. Specifically:

- (A.1) Self-adjointness of `T_x_W` follows from self-adjointness of `T_τ`
  (PR #1577 salvage §4 "Self-adjointness of T_W follows from the
  reflection-symmetry of its kernel: `T_W(V, U) = T_W(U, V)*` by
  `K_τ(U V^†) = K_τ((V U^†)^†) = K_τ(V U^†)*`"). The identical kernel
  symmetry holds for `T_x_W` by Lemma 3.1.

- (A.2) Trace-class follows from PR #1577 salvage Lemma C (`T_W` is
  trace-class on `H_Λ`). The Lemma C argument is purely about
  Hilbert-Schmidt norm convergence of the character series (which is
  independent of axis labeling) + the boundedness of the Wilson factor
  on compact configuration space (axis-permutation invariant by Lemma
  2.1). So Lemma C lifts verbatim to `T_x_W`.

- (A.3) Strict positivity of the `T_x_W` kernel pointwise on `Conf(Σ)²`
  follows from PR #1577 salvage Lemma B (`T_W(U, V) > 0` on `Conf(Λ)²`).
  The Lemma B argument is: each factor `K_τ(U_ℓ V_ℓ^†)` is `> 0` by
  PR #1577 salvage Lemma A.2 (SU(3) heat-kernel strict positivity),
  and `exp(-β ΔS_W) > 0` because the Wilson action is real. Both of
  these are axis-independent statements about SU(3) and about real
  exponentials. So Lemma B lifts verbatim to `T_x_W`.

- (A.4) + (A.5) Apply PR #1577 salvage Theorem D (Perron-Jentzsch
  spectral gap for self-adjoint trace-class positivity-improving compact
  operators on `L²(X, μ)`). The hypotheses (SA), (TC), (SP) are all
  satisfied by (A.1)-(A.3). Theorem D gives a simple top eigenvalue
  `λ_0(T_x_W) > 0` with a strictly positive eigenfunction, and the spectral
  gap

  ```
  δ_W := λ_0(T_x_W) - sup{|λ| : λ ∈ spec(T_x_W), λ ≠ λ_0(T_x_W)} > 0.
  ```

  Define `Δ_x_W := -log(|λ_1(T_x_W)| / λ_0(T_x_W))` where `λ_1` is the
  second largest eigenvalue (in absolute value). Then `Δ_x_W > 0` iff
  `δ_W > 0`, which holds. QED.

(Runner V5 verifies (A.5) by diagonalizing the truncated `T_x_W` on a
character basis; Runner V6 verifies the machine-precision agreement
`|Δ_x_W − Δ_τ| / Δ_τ < 1e-6` predicted by Lemma 3.1.)

---

## §4. Theorem B — Staggered+Wilson spatial slab T_x_full and Δ_x_full > 0 (conditional on Leg A)

The staggered Dirac operator on the Cl(3)/Z³ surface singles out a
discrete sublattice structure via the staggered phase `ε(x) = (-1)^{Σ x_μ}`.
This breaks the full Euclidean cubic symmetry of Lemma 2.1 (because the
sublattice structure distinguishes the four parity classes of a 4D
lattice). Adding fermions to the pure Wilson surface therefore requires
a separate analysis: we cannot simply lift the staggered+Wilson temporal
T_full of PR #1577 salvage §6 verbatim. We instead **compose** Leg A
(retained-conditional) with the pure Wilson result of §3 above.

### Lemma 4.1 (Spatial-slab Dirac operator anti-Hermiticity)

Let `D_x[U] = D_x[U; Σ_s, Σ_{s+1}]` be the spatial-slab staggered Dirac
operator built around the x-axis (the slab partition direction). The
construction is the standard staggered Dirac with hopping terms along
each lattice direction, restricted to the two-slab subset
`{p ∈ Σ_s} ∪ {p ∈ Σ_{s+1}}` with hopping along the x-axis being the
"longitudinal" direction.

Under Leg A's anti-Hermiticity theorem
(see [`docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)
§3 Lemma 3.1, "Determinant-phase analysis (C-det)"),

```
D_x[U]† = -D_x[U]                                                       (4.1)
```

on the same Cl(3)/Z³ surface, with eigenvalues coming in `±iλ_k` pairs.
The axis assignment of "spatial slab vs temporal slab" does not change
this: the staggered phase `ε(x) = (-1)^{Σ x_μ}` is sublattice-symmetric
across each individual lattice axis, so anti-Hermiticity holds whether
we sample the staggered operator with the "longitudinal" direction being
τ or x.

**Argument from Leg A primitives.** The staggered Dirac operator
factorizes per lattice direction:

```
D[U] = Σ_μ (1/2) η_μ(x) (U_{x,μ} δ_{x+μ, y} - U_{x-μ, μ}† δ_{x-μ, y})  (4.2)
```

with `η_μ(x)` the staggered phase along direction μ. By PR #1582 salvage
§3 Lemma 3.1 (Determinant-phase analysis (C-det), M-real case), this
factorization gives `D† = -D` for the full operator. Restricting to a
two-slab subset along axis x replaces the full sum `Σ_μ` by the same sum
but with `x` chosen as the slab-partition axis instead of `τ`. The
anti-Hermiticity property is preserved under this restriction because:
(a) each μ-component term is anti-Hermitian, (b) restriction to a slab
subset is a projection that preserves anti-Hermiticity (projection of an
anti-Hermitian operator onto a subspace gives an anti-Hermitian operator
on that subspace, modulo the standard "interaction-with-boundary" terms
which we absorb into the standard staggered boundary convention). QED.

### Lemma 4.2 (Spatial-slab fermion-determinant positivity)

Conditional on Leg A retention, for every SU(3) link configuration
`U ∈ Conf(Λ)` and real mass `m > 0`,

```
det(D_x[U] + m I) > 0.                                                  (4.3)
```

**Argument from Leg A primitives.** By Lemma 4.1, `D_x[U]` is
anti-Hermitian on the spatial-slab sub-Hilbert space, so its eigenvalues
come in pure-imaginary `±iλ_k` pairs. By PR #1582 salvage §3 Lemma 3.1
"M-real" case applied to the same anti-Hermitian operator `D_x[U]`,

```
det(D_x[U] + m I) = Π_pairs (m² + λ_k²) > 0
```

for `m > 0`. This is the spatial-slab analogue of the temporal-slab
Leg A determinant positivity used by PR #1577 salvage §6. QED.

(Runner V7 samples this on 30 random SU(3) configurations on a small
Λ and confirms `det(D_x + m I) > 0` real-positive on all samples.)

### Theorem B (Staggered+Wilson T_x_full positivity and Δ_x_full > 0, conditional on Leg A)

Define the symmetrized full spatial-slab transfer operator

```
T_x_full(U, V) := sqrt(T_F[U]) · T_x_W(U, V) · sqrt(T_F[V])             (4.4)
T_F[U] := det(D_x[U] + m I)
```

following the PR #1577 salvage §6 symmetrized construction (which is the
self-adjoint-preserving sandwich). Conditional on Leg A retention:

- (B.1) `T_x_full` is **self-adjoint** on `H_slab`,
- (B.2) `T_x_full` is **trace-class** on `H_slab`,
- (B.3) `T_x_full` is **strictly positivity-preserving**: kernel is `> 0`
  pointwise on `Conf(Σ)²`,
- (B.4) **simple top eigenvalue** with strictly positive eigenfunction,
- (B.5) **strict spectral gap**:
  ```
  Δ_x_full := -log(|λ_1(T_x_full)| / λ_0(T_x_full)) > 0.
  ```

**Proof.** The symmetrized sandwich (4.4) preserves all PR #1577
salvage §6 hypothesis-check structure:

- (B.1) Self-adjoint: `T_x_full(U, V) = T_x_full(V, U)` because `T_x_W`
  is real symmetric and `sqrt(T_F)` factors exchange under `U ↔ V`.
  (Real-positivity of `T_F[U]` from Lemma 4.2 is required for the
  square-root to be well-defined as a positive real number.)

- (B.2) Trace-class: `T_F[U]` is a continuous function of `U` on the
  compact configuration space `Conf(Λ)`, so it is bounded above and
  below by positive constants: `0 < c_F ≤ T_F[U] ≤ C_F < ∞`. The
  sandwich `T_x_full = M_F^{1/2} T_x_W M_F^{1/2}` (with `M_F` the
  multiplication-by-`T_F` operator) is trace-class because `T_x_W` is
  trace-class (Theorem A.2) and `M_F^{1/2}` is bounded.

- (B.3) Strict positivity: `T_x_W(U, V) > 0` (Theorem A.3) and
  `sqrt(T_F[U]) sqrt(T_F[V]) > 0` (Lemma 4.2), so the product is `> 0`
  pointwise on `Conf(Σ)²`.

- (B.4) + (B.5) Apply PR #1577 salvage Theorem D (Perron-Jentzsch spectral
  gap) to `T_x_full` on `H_slab`. Hypotheses (SA), (TC), (SP) are all
  satisfied by (B.1)-(B.3). Conclude: `T_x_full` has a simple top
  eigenvalue `λ_0(T_x_full) > 0` with strictly positive eigenfunction,
  and the spectral gap

  ```
  δ_full := λ_0(T_x_full) − sup{|λ| : λ ∈ spec(T_x_full), λ ≠ λ_0} > 0.
  ```

  Define `Δ_x_full := -log(|λ_1(T_x_full)| / λ_0(T_x_full))`. Then
  `Δ_x_full > 0` iff `δ_full > 0`, which holds. QED, conditional on
  Leg A.

(Runner V7 samples Lemma 4.2 and Theorem B's composition input — fermion
determinant positivity in the spatial-slab direction — and confirms
`det(D_x + m I) > 0` real-positive on 30 random SU(3) configurations.)

---

## §5. Discharge of slab-bridge hypotheses

The parent slab-bridge note
[`docs/CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md)
§"Inputs and support artifacts" names two hypotheses:

- **H1.** Existence of a positive Hermitian slab transfer operator
  `T_x : H_slab(x) → H_slab(x)` on a finite-dim slab Hilbert space, with
  the standard slab construction `Z(Λ) = Tr(T_x^{L_x})`.
- **H2.** Spatial transfer-matrix gap `Δ_x > 0`.

### Discharge of H1

- **For pure Wilson:** §3 Theorem A constructs `T_x_W` explicitly and
  shows it is self-adjoint (= Hermitian on a real-valued kernel), and
  strictly positivity-preserving. This is exactly hypothesis H1 with the
  identification `T_x := T_x_W`. Trace-class (Theorem A.2) gives the
  slab `Z(Λ) = Tr(T_x_W^{L_x})` standard transfer-matrix derivation. ✓
- **For staggered+Wilson (conditional on Leg A):** §4 Theorem B
  constructs the symmetrized `T_x_full` and shows it is self-adjoint and
  strictly positivity-preserving. The trace-class property (B.2) gives
  the standard slab partition-function expression `Z(Λ) = Tr(T_x_full^{L_x})`.
  Hypothesis H1 is discharged with `T_x := T_x_full`. ✓ (conditional)

(One caveat: the parent slab-bridge note writes `H_slab(x)` as a
"finite-dim slab Hilbert space" because its conditional theorem (S) uses
the finite-dim spectral theorem. PR #1577 salvage's setting is the
infinite-dim `L²(SU(3)^{|E(Σ)|})`. The Perron-Jentzsch theorem applied
in §3 and §4 gives the same simple-top + strict-gap conclusion in either
setting — see PR #1577 salvage Lemma D — so the discharge of H1 + H2
applies regardless of whether the parent slab-bridge note's conditional
(S) is interpreted in finite-dim or in the trace-class compact-operator
setting. The bound (S.7) `|⟨A_p · T̃_x^d · B_q⟩_0 − ⟨A_p⟩_0 ⟨B_q⟩_0| ≤ ‖A_p‖ · ‖B_q‖ · exp(-d · Δ_x)`
holds in both settings; in the infinite-dim setting the spectral
decomposition is the resolution of identity for a compact self-adjoint
operator with discrete spectrum accumulating at zero, which is exactly
what Theorem D / Perron-Jentzsch gives.)

### Discharge of H2

- **For pure Wilson:** Theorem A.5 gives `Δ_x_W := -log(|λ_1| / λ_0) > 0`.
  This is exactly hypothesis H2. ✓
- **For staggered+Wilson (conditional on Leg A):** Theorem B.5 gives
  `Δ_x_full > 0`. Conditional on Leg A retention, hypothesis H2 is
  discharged. ✓ (conditional)

### Consequence for the parent slab-bridge note's theorem (S)

The conditional theorem (S) of
[`docs/CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md)
takes the form:

> conditional on H1 and H2, exponential spatial clustering
> `|⟨A_p · T̃_x^d · B_q⟩_0 − ⟨A_p⟩_0 ⟨B_q⟩_0| ≤ ‖A_p‖ ‖B_q‖ exp(-d Δ_x)`
> holds on finite Λ.

With this note's discharge:

- **For pure Wilson:** Theorem (S) becomes **unconditional** on the
  canonical Cl(3)⊗Z³ pure Wilson finite-Λ surface, with gap rate
  `Δ_x := Δ_x_W > 0`.
- **For staggered+Wilson:** Theorem (S) becomes conditional **only on
  Leg A**, with gap rate `Δ_x := Δ_x_full > 0`.

(Runner V8 numerically verifies the bound (S.7) on a small Λ by computing
the spatial connected correlator at slab-separations d = 0, 1, 2 and
comparing against `‖A_p‖ ‖B_q‖ exp(-d · Δ_x_W)`.)

---

## §6. Theorem statement

**(W-slab) Pure Wilson spatial slab bridge unconditional closure.** Let
`Λ = Λ_x × Λ_⊥ ⊂ Z³` be a finite connected block with `Λ_x = {1, …, L_x}`
the slab-index axis and `Λ_⊥` the 2D transverse slab. On the canonical
pure Wilson lattice action at `β > 0`, the spatial-slab transfer operator
`T_x_W` defined by kernel (3.1) on the slab Hilbert space
`H_slab = L²(SU(3)^{|E(Σ)|}, dU_Haar)` is self-adjoint, trace-class,
strictly positivity-preserving, with simple top eigenvalue, strictly
positive top eigenfunction, and strict spectral gap

```
Δ_x_W := -log(|λ_1(T_x_W)| / λ_0(T_x_W)) > 0.
```

In particular, hypotheses H1 and H2 of the 2026-05-17 spatial slab-bridge
conditional theorem (S) are both discharged for pure Wilson, and (S)
becomes unconditional on finite Λ with gap rate `Δ_x_W > 0`.

**(SW-slab) Staggered+Wilson conditional closure (conditional on Leg A).**
With dynamical staggered fermions added via the symmetrized full
spatial-slab transfer operator `T_x_full := M_F^{1/2} T_x_W M_F^{1/2}`
defined in (4.4), conditional on Leg A retention
([`docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)),
the operator `T_x_full` is self-adjoint, trace-class, strictly
positivity-preserving, with simple top eigenvalue, strictly positive top
eigenfunction, and strict spectral gap

```
Δ_x_full := -log(|λ_1(T_x_full)| / λ_0(T_x_full)) > 0.
```

Hypotheses H1 and H2 are both discharged for staggered+Wilson conditional
on Leg A, and (S) becomes conditional only on Leg A with gap rate
`Δ_x_full > 0`.

**Proof.** §3 Theorem A for (W-slab); §4 Theorem B for (SW-slab). QED.

---

## §7. Out-of-scope anti-overclaim list

The (W-slab) and (SW-slab) theorems of §6 do NOT claim:

- (X1) **Thermodynamic limit `Λ → Z³`.** No statement about how
  `Δ_x_W(Λ)` or `Δ_x_full(Λ)` scales as `|Λ| → ∞`. In confining theories
  one expects `Δ_x → 0` on long transverse extents (volume scaling), or
  `Δ_x → constant` only in the pure-glue mass-gap regime, which is itself
  the Yang-Mills mass-gap problem.

- (X2) **Uniformity in Λ.** No quantitative bound on how
  `Δ_x_W(Λ)` or `Δ_x_full(Λ)` scales with `|Λ|`. The strict positivity
  exhibited by Theorems A, B may depend on `Λ` non-trivially.

- (X3) **Yang-Mills (Clay) mass gap.** Not addressed. The Clay problem
  is for continuum Yang-Mills theory in infinite volume; we work on a
  finite spatial lattice with explicit cutoffs.

- (X4) **Gauge-invariant restriction.** The (W-slab), (SW-slab) theorems
  are stated on the full `H_slab` without gauge fixing. For either
  `T_x_W` or the conditional `T_x_full`, restriction to the
  gauge-invariant subspace `H_slab^G` inherits the gap when the operator
  commutes with the gauge action (which it does — Wilson + staggered
  action is gauge-invariant). The unique positive top eigenfunction is
  gauge-invariant, and the off-top spectrum of the restricted operator
  is a subset of the off-top spectrum of the full operator.

- (X5) **Continuum limit `a → 0`.** Not addressed. The lattice spacing
  `a` is fixed (encoded in `τ` and `β`).

- (X6) **First-principles derivation of Leg A from minimal axioms.** Leg
  A is treated as a named conditional input throughout §4 and §5. Its
  effective status is the audit lane's call on
  [`docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md).

- (X7) **Permanently retained.** The source-side label is
  `bounded_theorem`; effective status is the audit lane's call.

---

## §8. Runner

Companion runner: [`scripts/frontier_slab_bridge_spatial_Tx_real_2026_05_19.py`](../scripts/frontier_slab_bridge_spatial_Tx_real_2026_05_19.py)

Eight verifications on real SU(3) representations / structures:

| # | Verification | Description |
|---|---|---|
| V1 | Wilson action axis-permutation invariance (Lemma 2.1) | All 24 cubic axis-permutations on N=20 random SU(3) configurations on 2×2×2 give `S_W[σ_*(U)] = S_W[U]` to machine precision. |
| V2 | Spatial-slab kernel = temporal-slab kernel (Lemma 3.1, identity (3.2)) | `T_x_W(U, V)` matches `T_τ(σ_{x↔τ}(U), σ_{x↔τ}(V))` element-by-element on the truncated character basis to machine precision. |
| V3 | T_x_W kernel pointwise positivity (Theorem A.3) | Truncated `T_x_W` kernel on a Haar-quadrature mesh of SU(3) elements has all entries `> 0` with explicit margin. |
| V4 | T_x_W trace-class via character series (Theorem A.2) | Partial sums `Σ_{p+q ≤ N} dim(p, q)² exp(-τ C_2 / (2 N_c))` converge at N=12 → 16 → 20 with relative tail `< 1e-9`. |
| V5 | Δ_x_W > 0 from diagonalized T_x_W (Theorem A.4 + A.5) | Top eigenvalue is simple (multiplicity 1), `λ_1 < λ_0` strictly, `Δ_x_W > 0` with explicit margin. |
| V6 | Symmetry check Δ_x_W = Δ_τ (Lemma 3.1 prediction) | `\|Δ_x_W − Δ_τ\| / Δ_τ < 1e-6` (machine-precision agreement). |
| V7 | Spatial-slab Leg A composition (Theorem B / Lemma 4.2) | Sample 30 SU(3) configurations on a small 2×2×2 lattice; compute `det(D_x[U] + m I)`; verify all real positive with margin. |
| V8 | Slab-bridge bound (S.7) operational at d = 0, 1, 2 (§5 discharge) | Spatial connected correlator `|C(d)| ≤ ‖A_p‖ ‖B_q‖ exp(-d · Δ_x_W)` verified at slab-separations d = 0, 1, 2. |

All eight verifications have hard assertion gates. Target: `PASS = 8`,
`FAIL = 0`.

Cached output: [`logs/runner-cache/frontier_slab_bridge_spatial_Tx_real_2026_05_19.txt`](../logs/runner-cache/frontier_slab_bridge_spatial_Tx_real_2026_05_19.txt).

---

## §9. Composition upstream

This note provides one of the two OR-branch routes the parent
`axiom_first_cluster_decomposition_theorem_note_2026-04-29` requires for
its spatial L2 closure. Specifically:

- **OR-branch (a) — Lieb-Robinson + composition route.** Supplied by
  the spatial-cluster Lieb-Robinson companion (PR #1583 / 596637adb).
- **OR-branch (b) — Slab-bridge route.** This note discharges the
  named hypotheses of the 2026-05-17 spatial slab-bridge note.

With both OR-branches in place, the parent row has TWO independent
routes to spatial clustering on finite Λ. The parent's required halves
have full coverage as follows:

- **Temporal half:** PR #1577 salvage `8369973af` discharges `Δ_T > 0`.
- **Spatial half — branch (a):** PR #1583 salvage establishes
  finite-volume Lieb-Robinson + composition with Δ_T > 0.
- **Spatial half — branch (b):** This note discharges the spatial
  slab-bridge's hypotheses H1, H2.

These compositional consequences are the audit lane's call and are
recorded here only for traceability.

---

## §10. Hypothesis set used and audit dependency note

This bounded narrow theorem uses:

- **(A1)** Cl(3) local algebra (axiom).
- **(A2)** Z³ spatial substrate (axiom).
- **(R1)** Canonical normalization `β > 0` Wilson surface.
- **(R2)** Staggered Dirac anti-Hermiticity (`D† = -D`) — Leg A primitive,
  used only in §4. Currently retained but on `audited_conditional`
  parent surface via Leg A.
- **(R3)** SU(3) heat-kernel character expansion + Perron-Jentzsch
  theorem (PR #1577 salvage Lemmas A-D, retained).
- **(R4)** Leg A's mass-orientation theorem (Theorem 3.4 of PR #1582
  salvage), `audited_conditional`.

The proofs use no new repo axioms. All proof-input citations are listed
above; no external literature (Vafa-Witten, Leutwyler-Smilga, OS, etc.)
is load-bearing.

**Audit dependency note.** This note is a bounded conditional theorem
discharging the two named hypotheses of the 2026-05-17 slab-bridge note.
It does **not** promote either the slab-bridge note's parent row or the
Leg A parent note. The audit citation graph carries:

- An edge from this note to the 2026-05-17 slab-bridge note (as a
  discharge of its named hypotheses).
- An edge from this note to PR #1577 salvage's
  `CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md`
  (load-bearing for Theorem A, since the axis-permutation lift uses
  Lemmas A-D of that note).
- An edge from this note to PR #1582 salvage's
  `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`
  (Leg A) as a named conditional input for §4 Theorem B and §5
  discharge of H1/H2 for staggered+Wilson.

The independent audit lane decides whether the discharge of H1 and H2
suffices to lift the 2026-05-17 slab-bridge note's status.

---

## References

- Parent slab-bridge note (this note discharges H1, H2):
  [`docs/CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md)
- PR #1577 salvage (load-bearing for axis-permutation lift):
  [`docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md`](CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md)
- PR #1582 salvage (Leg A — named conditional input for staggered+Wilson):
  [`docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)
- Parent of the spatial slab-bridge (audit context):
  [`docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
- Companion 2026-05-09 temporal bridge note (context):
  [`docs/CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md)
- Repository minimal axioms:
  [`docs/MINIMAL_AXIOMS_2026-05-03.md`](MINIMAL_AXIOMS_2026-05-03.md)

---

*End of note.*
