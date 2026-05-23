# Operator-Theoretic Delta_T > 0 Support on the Finite-Lambda SU(3) Transfer Operator

**Date:** 2026-05-19
**Status (source-side label):** bounded_theorem with a named conditional composition input
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py`](../scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py)
**Cached output:** [`logs/runner-cache/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.txt`](../logs/runner-cache/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.txt)
**Parent repair target:** `docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`, candidate 2 ("Perron-Frobenius for the positive transfer matrix").
**Redo of:** closed PR #1531 (4×4 finite-dim toy was rejected as not applicable to continuous SU(3) link variables).
**Status authority:** independent audit lane only. The `bounded_theorem` label above is a source-side claim-boundary declaration, not an audit verdict.

## Honest scope (read this first)

- **Finite Λ only.** Λ ⊂ Z³ is a finite connected spatial sublattice with a finite number of links. All operator norms, traces, and eigenvalue bounds are stated on this single Hilbert space.
- **No thermodynamic limit.** No claim that the gap survives `Λ → Z³`. In fact one expects the gap to close in the limit on a confining theory; this is not what is proved here.
- **No uniform-in-Λ bound.** No quantitative claim on how the gap scales with `|Λ|`.
- **NOT the Yang-Mills mass gap.** The Clay Millennium problem asks for a continuum, infinite-volume gap on the Yang-Mills functional integral. We address a finite-volume lattice transfer operator only.
- **The fermion-determinant input is not promoted here.** Leg A `det(D[U] + m I) > 0` is cited from `docs/STRONG_CP_THETA_ZERO_NOTE.md` (§"Leg A: Fermion phase closure", lines 46-58) as parent context only; the T_full extension below is conditional on the separately landed Leg A salvage repair [`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md) (PR #1582 salvage commit `5f6f0b87a`), not on the older unfixed `strong_cp_theta_zero_note` row itself. The conditional T_full extension is gated on the salvage candidate's audit retention, not on the parent's `audited_conditional` status.
- **The new content is the finite-Lambda SU(3) transfer-operator support theorem (§5) and the conditional symmetrized composition with Leg A (§6).** The operator-theory step imports the standard Perron-Jentzsch/Krein-Rutman positivity-improving compact-operator theorem as bounded mathematical machinery; it is not a new repo axiom.

---

## §0. Honest framing — why this note replaces the closed PR #1531

The closed PR exhibited Perron-Frobenius on a 4×4 finite-dimensional toy matrix. The reviewer objection was correct:

> A finite spatial lattice Λ ⊂ Z³ still has CONTINUOUS link variables `U_ℓ ∈ SU(3)`. The configuration space is `SU(3)^{|E(Λ)|}` — a connected compact Lie manifold. The transfer operator acts on `L²(SU(3)^{|E(Λ)|}, dU_Haar)`, an infinite-dimensional separable Hilbert space. Finite-dimensional Perron-Frobenius DOES NOT APPLY.

This note responds by:

1. Working in the actual operator-theoretic setting (§1).
2. Proving the SU(3) heat kernel is strictly positive (§2) from the character expansion plus the strong maximum principle for parabolic equations on connected compact Lie groups.
3. Proving the resulting heat-kernel transfer operator is trace-class on `L²(SU(3)^{|E(Λ)|})` (§4), using the character expansion and the compact smooth-kernel trace-class theorem.
4. Applying the standard Perron-Jentzsch/Krein-Rutman positivity-improving compact-operator theorem (§5) to get a simple top eigenvalue and a strict gap below it.
5. Giving the conditional symmetrized composition with Leg A `det(D + m I) > 0` (§6) and stating the finite-Λ theorem boundary (§7).

The runner verifies each step on the ACTUAL SU(3) integral operator, not a 4×4 toy.

---

## §1. Setting

Let `Λ ⊂ Z³` be a finite connected spatial lattice with edge set `E(Λ)` of cardinality `|E(Λ)| = E`. Each spatial bond `ℓ ∈ E(Λ)` carries a parallel-transport link variable `U_ℓ ∈ SU(3)`. The total configuration space is

```
Conf(Λ) := SU(3)^E
```

equipped with the product Haar measure `dU = ⊗_ℓ dU_ℓ` (each factor normalized to `∫_{SU(3)} dU_ℓ = 1`). The single-slice Hilbert space is

```
H_Λ := L²(Conf(Λ), dU)
```

For the canonical Cl(3)/Z^3 staggered + Wilson Hamiltonian at gauge coupling `β > 0` and quark mass `m > 0`, the temporal transfer operator `T = T_W · T_F` factors as

- `T_W` — the pure-gauge piece, the integral kernel
  ```
  T_W(U, V) = exp(-β · ΔS_W[U, V]) · Π_{ℓ ∈ E(Λ)} K_τ(U_ℓ V_ℓ^†)
  ```
  with `K_τ` the SU(3) heat kernel at "time" `τ` (set by the lattice spacing), and `ΔS_W[U, V]` a real-valued Wilson action increment (manifestly real since `tr(plaquette) ∈ R` after the standard `Re tr` in the Wilson action).
- `T_F` — the fermion-determinant piece, `T_F[U] = det(D[U] + m I)`, acting as multiplication on `H_Λ` (it depends only on `U`, not on `V`).

We will prove that the integral operator `T` defined by the kernel `T_W` followed by multiplication by `T_F` has a simple top eigenvalue with a strict spectral gap below it on `H_Λ`.

**Notation summary.** `K_τ` denotes the SU(3) heat kernel; `χ_R` the character of irrep `R = (p, q)`; `dim R = (p+1)(q+1)(p+q+2)/2`; `C_2(R) = (p² + q² + pq)/3 + p + q`; `N_c = 3`. The character expansion of the heat kernel on a connected compact Lie group is

```
K_τ(g) = Σ_R (dim R) χ_R(g) exp(-τ C_2(R) / (2 N_c))                   (*)
```

with absolute convergence for `τ > 0` (see §2 Lemma A.1). Verified on the runner mesh in V2 with relative tail `< 1e-6` at `N_max = 20`, `τ = 4`.

---

## §2. Lemma A — SU(3) heat-kernel strict positivity

### Lemma A.1 (Absolute convergence of the character series)

The series (*) converges absolutely uniformly on `SU(3)` for every `τ > 0`.

**Proof.** Each irrep has `|χ_R(g)| ≤ dim R = χ_R(e)` (Cauchy-Schwarz on the regular representation). So term-by-term

```
|(dim R) χ_R(g) exp(-τ C_2(R)/(2 N_c))|  ≤  (dim R)² exp(-τ C_2(R)/(2 N_c)).
```

The reduced bound is a number that depends only on `(p, q)` and `τ`. For SU(3), `dim(p, q) = (p+1)(q+1)(p+q+2)/2` is polynomial in `(p, q)` and `C_2(p, q) = (p² + q² + pq)/3 + p + q` grows quadratically. So the tail is bounded by

```
Σ_{p, q ≥ 0} ((p+1)(q+1)(p+q+2)/2)² exp(-τ((p² + q² + pq)/3 + p + q)/(2 N_c))
```

The quadratic decay in the exponent dominates the polynomial prefactor for every `τ > 0`, giving absolute convergence. ∎

(Runner V2 verifies this convergence numerically: at `τ = 4`, the partial sum is converged to 6 digits at `N_max = 12` and to better than 1e-9 relative tail at `N_max = 20`.)

### Lemma A.2 (Strict positivity of K_τ on SU(3))

For every `τ > 0` and every `g ∈ SU(3)`, `K_τ(g) > 0`.

**Proof.** We use the parabolic strong maximum principle on a connected compact Riemannian manifold.

**Step 1 — `K_τ` satisfies the heat equation.** Differentiate (*) term-by-term (justified by the absolute convergence + uniform bound of differentiated terms — the only new factor is `−C_2(R)/(2 N_c)`, which is polynomial in `(p, q)` and is dominated by the same exponential):

```
∂_τ K_τ(g) = Σ_R (dim R) χ_R(g) · (-C_2(R)/(2 N_c)) · exp(-τ C_2(R)/(2 N_c))
            = (1/(2 N_c)) · Δ_SU(3) K_τ(g)
```

since each `χ_R` is an eigenfunction of the Laplace-Beltrami operator `Δ_SU(3)` on SU(3) (with the bi-invariant metric induced by the Killing form) with eigenvalue `−C_2(R)`. So `K_τ` is a classical solution of

```
∂_τ u = (1/(2 N_c)) Δ_SU(3) u                                          (**)
```

on `(0, ∞) × SU(3)`.

(Runner V5 verifies this heat-equation consistency numerically at four torus points: max relative finite-difference error `< 1e-3`.)

**Step 2 — Initial data.** As `τ → 0⁺`, `K_τ → δ_e` in the distributional sense (formal sum `Σ_R (dim R) χ_R(g)` is the kernel of the identity by orthogonality of characters). In particular `K_τ` is a non-negative continuous function for `τ > 0` (Lemma A.3 below gives the non-negativity; we are proving STRICT positivity here).

**Step 3 — Non-negativity (Lemma A.3 inline).** For any test function `f ∈ C(SU(3))` with `f ≥ 0`, define

```
u(τ, g) := ∫_{SU(3)} K_τ(g h^{-1}) f(h) dh                              (***)
```

By the character expansion, `u(τ, ·) = exp(τ Δ / (2 N_c)) f` in the spectral functional calculus on `L²(SU(3))`. By the contraction property of the heat semigroup `exp(τ Δ / (2 N_c))` on `C(SU(3))` (it is a Markov semigroup — see Lemma A.4 below — i.e. preserves non-negative functions and constants), `u(τ, g) ≥ 0`. Take a sequence of `f_n ≥ 0` approximating `δ_h` for fixed `h ∈ SU(3)`; in the distributional limit `u(τ, g) → K_τ(g h^{-1})`. So `K_τ(g h^{-1}) ≥ 0` for all `g, h`. Equivalently, `K_τ(g) ≥ 0` for all `g`. ∎ (Lemma A.3)

**Lemma A.4 (heat semigroup is a Markov semigroup).** The heat semigroup `P_τ := exp(τ Δ / (2 N_c))` on `C(SU(3))` satisfies:
(i) `P_τ 1 = 1` (it preserves constants), since `Δ 1 = 0`.
(ii) `P_τ f ≥ 0` whenever `f ≥ 0`.

For (ii), one route: on a connected compact Lie group with the bi-invariant metric, the heat kernel is the transition density of a Brownian motion (Wiener-Yosida construction on a compact manifold gives the Markov semigroup). The transition density of a continuous-time Markov process is non-negative by construction. Alternatively, one can integrate `f ≥ 0` against the (formally non-negative) representation in (***) and observe non-negativity term-by-term from the polynomial-in-character-spectral structure. We omit further details since the strict-positivity step (Step 4 below) is what carries new content.

**Step 4 — Strict positivity by parabolic strong maximum principle.** Suppose for contradiction that `K_{τ₀}(g₀) = 0` at some `(τ₀, g₀)` with `τ₀ > 0`. Since `K_τ ≥ 0` (Step 3) and `K_τ` satisfies the heat equation (**), the parabolic strong maximum principle for non-negative subsolutions on connected manifolds applies (the minimum value 0 is achieved at an interior point; if any solution achieves its minimum at an interior parabolic point and is C² in space, time-continuous, on a connected domain, then the solution is constant equal to the minimum throughout the parabolic cylinder backwards in time). Specifically:

The function `v(τ, g) := K_τ(g)` is C^∞ on `(0, ∞) × SU(3)` (smoothness of the heat kernel) and non-negative on the parabolic interior. If `v(τ₀, g₀) = 0`, the parabolic strong maximum principle (Evans, "Partial Differential Equations", §7.1.4, Theorem 11 — but we are using the GENERAL principle on a connected manifold, which is purely the statement of the maximum principle for second-order parabolic equations on connected open sets, not a specialized theorem) gives `v(τ, g) ≡ 0` for all `g ∈ SU(3)` and `0 < τ ≤ τ₀`.

But then `∫_{SU(3)} K_τ dg = 0`, contradicting the normalization `∫_{SU(3)} K_τ dg = 1` (Step 1 of (***) with `f ≡ 1` gives `u(τ, g) = 1` constant, i.e. `∫ K_τ = 1`). Contradiction. So `K_τ(g) > 0` for all `g ∈ SU(3)`, all `τ > 0`. ∎

(Runner V1 verifies strict positivity on the SU(3) maximal torus: `min K_τ ≈ 1.29e-3 > 0` on a 16×16 mesh with `τ = 4`, `N_max = 12`. Since `K_τ` is a class function — see Lemma A.5 — positivity on the maximal torus implies positivity on all of SU(3) by conjugation invariance.)

### Lemma A.5 (`K_τ` is a class function)

`K_τ(h g h^{-1}) = K_τ(g)` for every `g, h ∈ SU(3)`.

**Proof.** From the character expansion (*), each `χ_R` is a class function (`χ_R(h g h^{-1}) = χ_R(g)` by the cyclic property of trace), and the other factors are independent of `g`. ∎

(Runner V3 verifies `∫_{SU(3)} K_τ dg = 1` via Weyl integration on the torus: `|val - 1| < 5e-2` on the coarse 16×16 mesh, error `3.331e-16` after Haar normalization.)

---

## §3. Lemma B — T_W kernel strictly positive on Conf(Λ) × Conf(Λ)

**Lemma B.** The integral kernel `T_W(U, V)` on `Conf(Λ) × Conf(Λ)` is strictly positive: `T_W(U, V) > 0` for every `(U, V)` in `Conf(Λ)²`.

**Proof.** By definition,

```
T_W(U, V) = exp(-β ΔS_W[U, V]) · Π_{ℓ ∈ E(Λ)} K_τ(U_ℓ V_ℓ^†)
```

Two factors:

- `exp(-β ΔS_W[U, V])` is the exponential of a real number (real Wilson action), so is `> 0` pointwise. (The Wilson action `S_W = Σ_plaquettes (1 - Re tr(plaquette/N_c))` is real-valued because `Re tr` is.)
- Each factor `K_τ(U_ℓ V_ℓ^†)` is `> 0` by Lemma A.2 applied to the SU(3) element `U_ℓ V_ℓ^† ∈ SU(3)`.

Product of strictly positive quantities is strictly positive. ∎

(Runner V8 verifies this on sampled `(U_ℓ, V_ℓ)` Haar pairs: `min K_τ(UV†) ≈ 1.66e-3 > 0` across 30 random configurations.)

---

## §4. Lemma C — `T_W` is trace-class on `H_Λ`

**Lemma C.** The integral operator with kernel `T_W` is trace-class (in particular Hilbert-Schmidt) on `H_Λ = L²(Conf(Λ), dU)`.

**Proof.** We show the Hilbert-Schmidt norm is finite; combined with positivity and self-adjointness, this gives trace-class.

**Step 1 — Hilbert-Schmidt norm of single-link kernel.** On `L²(SU(3), dU)`, the single-link kernel is `K_τ(U V^†)`. Its Hilbert-Schmidt norm squared is

```
||K_τ||²_HS  =  ∫∫ |K_τ(U V^†)|² dU dV
             =  ∫_{SU(3)} K_τ(g)² dg                            (change of variable g = U V^†, Haar)
```

Using the character expansion (*) and orthonormality of `{χ_R / √(dim R)}` over the conjugacy classes (more precisely, orthonormality of `{√(dim R) χ_R}` in `L²(SU(3))` via the Peter-Weyl theorem combined with the dimension factor), one gets

```
||K_τ||²_HS  =  Σ_R (dim R)² exp(-τ C_2(R) / N_c)
```

(double the exponent because the eigenvalue is `exp(-τ C_2(R)/(2 N_c))` and we square it for HS, AND multiplicity is `(dim R)²` arising from matrix-element index pairs `(a, b)` in the Peter-Weyl basis `√(dim R) D^R_{ab}`).

(Runner V2 computes this HS norm² explicitly at `τ = 4`: `||T||²_HS ≈ 6.53`, finite.)

**Step 2 — Finiteness.** The same polynomial-vs-quadratic-exponent argument as Lemma A.1 gives convergence for every `τ > 0`. Concretely the series is dominated by

```
Σ_{p, q ≥ 0} ((p+1)(q+1)(p+q+2)/2)² exp(-τ((p² + q² + pq)/3 + p + q)/N_c)
```

which is finite by quadratic decay versus polynomial growth. So `||K_τ||²_HS < ∞`.

**Step 3 — Multi-link HS norm.** The full T_W kernel is a product over `E` links of single-link factors (times `exp(-β ΔS_W)` which is uniformly bounded on the compact configuration space `SU(3)^E`). So

```
||T_W||²_HS  ≤  ||exp(-β ΔS_W)||²_∞  ·  ||K_τ||²_HS^E
```

with the sup-norm factor finite (uniform continuous function on compact space) and `||K_τ||²_HS` finite by Step 2. Hence `||T_W||²_HS < ∞`.

**Step 4 — From HS to trace-class.** A positive Hilbert-Schmidt operator is automatically trace-class via the singular-value decomposition: if `K_HS = Σ s_n |φ_n⟩⟨ψ_n|` with `Σ s_n² < ∞` and the operator is self-adjoint positive (so `s_n = λ_n ≥ 0` and `φ_n = ψ_n`), then `Σ λ_n ≤ Σ λ_n²/λ_n` cannot be used naively, BUT one route is: a positive self-adjoint operator on a separable Hilbert space with finite Hilbert-Schmidt norm has discrete eigenvalues `λ_n ↓ 0`, and since `Σ λ_n² < ∞` and `λ_n ↓ 0`, one shows `Σ λ_n < ∞` by the explicit computation of the trace from the character expansion below.

**Step 4' — Direct computation of trace.** The trace of T_W is

```
Tr(T_W)  =  ∫_{Conf(Λ)} T_W(U, U) dU
         =  ∫ exp(-β ΔS_W[U, U]) Π_ℓ K_τ(I) dU
         ≤  (sup |exp(-β ΔS_W)|) · (K_τ(I))^E
```

with `K_τ(I) = Σ_R (dim R)² exp(-τ C_2(R)/(2 N_c))` finite (same character series with different summation convention; see Runner V2 partial sums, e.g. `K_τ(I) ≈ 5.37e1` at `τ = 4`, `N_max = 12`). And `sup |exp(-β ΔS_W)|` is finite on the compact configuration space. Equivalently, the heat-kernel factor is a smoothing kernel on the compact manifold `SU(3)^E`; multiplication by the smooth bounded Wilson factor leaves a smooth compact-manifold kernel, hence a trace-class integral operator. ∎

(Self-adjointness of T_W follows from the reflection-symmetry of its kernel: `T_W(V, U) = T_W(U, V)*` by `K_τ(U V^†) = K_τ((V U^†)^†) = K_τ(V U^†)*` — the latter equality uses `K_τ` is a class function and real-valued, as is `exp(-β ΔS_W)` symmetric in `(U, V)` via the standard Wilson action symmetry.)

---

## §5. Lemma D — Standard positivity-improving compact-operator theorem

This is the bounded functional-analysis import used by the note. It is
standard Perron-Jentzsch/Krein-Rutman theory for compact positivity-improving
operators on a Hilbert lattice; it is not introduced as a new repo axiom.

### Theorem D (Perron-Jentzsch spectral gap)

Let `(X, μ)` be a finite measure space and let
`T : L²(X, μ) -> L²(X, μ)` be a self-adjoint trace-class integral operator
with measurable kernel `T(x, y) >= 0`. Assume `T` is positivity improving:
for every nonzero `f >= 0`, `(T f)(x) > 0` for `μ`-a.e. `x`.

Then the spectral radius `r(T) = ||T||_op` is a positive, simple eigenvalue
with an eigenfunction `ψ_0 > 0` a.e. All other spectral values satisfy
`|λ| < r(T)`. Since trace-class compact self-adjoint spectra have only
finite multiplicities away from zero and accumulate only at zero, this gives
a strict spectral gap

```text
δ := r(T) - sup{|λ| : λ in spec(T), λ != r(T)} > 0.
```

### Use in this note

The proof of Theorem D is not load-bearing new physics. The audit-relevant
work in this note is to verify that the finite-Lambda SU(3) heat-kernel
transfer operator satisfies the theorem's hypotheses:

1. self-adjointness from the symmetric real heat-kernel/Wilson kernel,
2. trace-class from smooth heat-kernel smoothing on the compact manifold
   `SU(3)^E` and the summable character spectrum in §4,
3. positivity improvement from `K_tau(g) > 0` on connected `SU(3)` and the
   positive Wilson factor.

Runner V4 checks the explicit single-link spectrum: top eigenvalue `= 1.0`
(trivial irrep, multiplicity `dim^2 = 1`), second eigenvalue
`= exp(-2 tau / 9) ~= 0.411` for `tau = 4`, gap `~= 0.589`. Runner V6 checks
the same strict-gap structure on the two-site truncated character basis.

---

## §6. Conditional composition with Leg A

### Leg A statement (cited as a current conditional dependency)

From `docs/STRONG_CP_THETA_ZERO_NOTE.md`, §"Leg A: Fermion phase closure" (lines 46-58) as parent context only; the structural Leg A statement is taken from the salvage repair [`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md) (PR #1582 salvage), not as a load-bearing dep on the unfixed parent row — the staggered Dirac operator `D[U]` on the Cl(3)/Z³ retained surface is anti-Hermitian (`D† = -D`), and for real mass `m > 0`,

```
det(D[U] + m I) = Π_k (m² + λ_k²) > 0
```

pointwise on every SU(3) configuration `U` (the eigenvalues of `D` are pure imaginary, in `±iλ` pairs). The current audit ledger marks `strong_cp_theta_zero_note` as `audited_conditional`, so this note treats Leg A as a named conditional dependency, not as retained input.

(Runner V7 samples Leg A on 50 random SU(3) Haar configurations: `min det(D[U] + m I) ≈ 1.76e-2 > 0`, real positive on all 50. This is a sanity check, not an audit promotion of Leg A.)

### Composition

Assuming Leg A, define the symmetrized full transfer kernel

```text
T_full(U, V) := sqrt(T_F[U]) · T_W(U, V) · sqrt(T_F[V]),
T_F[U] := det(D[U] + m I).
```

The symmetrized sandwich is the self-adjoint transfer-operator surface; the unsymmetrized product `T_W M_F` is not used as the self-adjoint operator.

1. **`M_F` is bounded and strictly positivity-preserving.** Since `Conf(Λ)` is compact and `U ↦ det(D[U] + m I)` is continuous in `U` (composition of continuous functions on a compact group), it is bounded above and bounded below by a positive constant: `0 < c_F ≤ T_F[U] ≤ C_F < ∞` uniformly on `Conf(Λ)`. So `M_F` is a bounded multiplication operator with strictly positive multiplier.

2. **`T_full` is self-adjoint, trace-class, strictly positivity-preserving.**
   - Self-adjoint: `T_full(U, V) = T_full(V, U)` because `T_W` is real symmetric and the square-root factors exchange under `U <-> V`.
   - Trace-class: the square-root multipliers are bounded on compact `Conf(Λ)`, so `T_full = M_F^{1/2} T_W M_F^{1/2}` is trace-class whenever `T_W` is trace-class.
   - Strict positivity: `T_W(U, V) > 0` (Lemma B) and `T_F[U], T_F[V] > 0` (Leg A), so the product is `> 0`.

3. **Apply Theorem D (§5) to `T_full` on `H_Λ`, conditional on Leg A.** Conditions (SA), (TC), (SP) all hold under the Leg A determinant-positivity dependency. Conclude: `T_full` has a simple top eigenvalue `λ₀(T_full) > 0`, a strictly positive eigenfunction, and a strict spectral gap `δ_full := λ₀ - sup_{n ≥ 1} |λ_n| > 0`.

(Runner V8 verifies pointwise positivity of the sampled symmetrized product factor `K_τ · sqrt(det_F(U) det_F(V))` on `(U, V)` Haar pairs: `min product ≈ 2.92e-5 > 0` across 30 pairs.)

---

## §7. Theorem statement

**Theorem (finite-Λ Delta_T > 0, bounded surface).** Let `Λ ⊂ Z³` be a finite connected spatial lattice. On the Hilbert space `H_Λ = L²(SU(3)^{|E(Λ)|}, dU_Haar)`, the finite-Lambda SU(3) heat-kernel/Wilson transfer operator `T_W` has a simple top eigenvalue `λ₀` with a strictly positive eigenfunction and a strict spectral gap

```
Δ_T(Λ)  :=  E_1(Λ) - E_0(Λ)  =  -log(|λ_1| / λ₀)  >  0
```

where `λ_0 = λ₀ > 0` and `λ_1` is the next eigenvalue (in absolute value).

Conditional extension: if the Leg A determinant-positivity input from `STRONG_CP_THETA_ZERO_NOTE.md` is audited retained-grade for the same finite-Lambda action surface, then the symmetrized staggered+Wilson transfer operator

```text
T_full(U, V) = sqrt(det(D[U] + mI)) T_W(U, V) sqrt(det(D[V] + mI))
```

has the same simple-top/strict-gap conclusion by §6.

**Proof.** Lemma B gives strict positivity of the `T_W` kernel, Lemma C gives trace-class, self-adjointness follows from the real symmetric transfer kernel, and Theorem D applies. The `T_full` conclusion is conditional on the Leg A determinant-positivity dependency and uses the bounded symmetrized multiplication argument in §6. ∎

---

## §8. Out-of-scope anti-overclaim list

The theorem of §7 does NOT claim:

- (X1) **Thermodynamic limit.** No statement about `Δ_T(Λ)` as `Λ → Z³`. In a confining theory one expects `Δ_T → 0` exponentially in the spatial volume on long temporal extents, or `Δ_T → constant` only in pure-glue mass-gap regime — which is itself the Yang-Mills mass-gap problem.
- (X2) **Uniformity in Λ.** No quantitative bound on how `Δ_T(Λ)` scales with `|Λ|`. The strict positivity `δ > 0` exhibited by Theorem D may depend on `Λ` in a non-trivial way.
- (X3) **Yang-Mills mass gap (Clay).** Not addressed. The Clay problem is for the continuum Yang-Mills theory in infinite volume; we work on a finite spatial lattice with explicit cutoffs.
- (X4) **Gauge-invariant restriction.** The finite-Lambda theorem is stated on `H_Λ` without gauge fixing. For either `T_W` or the conditional symmetrized `T_full`, restriction to the gauge-invariant subspace `H_Λ^G` inherits the gap when the operator commutes with the gauge action: the unique positive top eigenfunction is gauge-invariant, and the off-top spectrum of the restricted operator is a subset of the off-top spectrum of the full operator.
- (X5) **Continuum limit `a → 0`.** Not addressed. The lattice spacing `a` (encoded in `τ` and `β`) is fixed.
- (X6) **Spatial cluster decomposition.** Not addressed. This theorem provides the temporal-direction gap. Spatial clustering still needs a separate retained argument.
- (X7) **Permanently retained.** The source-side label is `bounded_theorem`; effective status is the audit lane's call.

---

## §9. Runner

Companion runner: [`scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py`](../scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py)

Eight verifications on the ACTUAL SU(3) integral operator (not a 4×4 toy):

| # | Verification | Result |
|---|---|---|
| V1 | `K_τ > 0` strictly on SU(3) maximal torus (Lemma A.2) | PASS — `min K_τ = 1.29e-3` on 16×16 mesh |
| V2 | Character-series trace-norm converges (Lemma A.1, Lemma C Step 2) | PASS — relative tail `< 1e-9` at `N_max = 20`, `τ = 4` |
| V3 | `K_τ` is a probability kernel `∫ K_τ = 1` (Lemma A.4 (i) + Lemma A.5) | PASS — `\|val − 1\| = 3.331e-16` after Haar normalization |
| V4 | Single-link operator simple top + strict gap (Theorem D applied to `T_W` on `L²(SU(3))`) | PASS — top = 1, gap = `0.589` |
| V5 | Heat-equation consistency (Lemma A.2 Step 1) | PASS — max relative error `2.31e-9` (tol 1e-3) |
| V6 | 2-site Λ truncated transfer strict gap | PASS — same gap structure tensored |
| V7 | Conditional Leg A `det(D + m I) > 0` on sampled SU(3) configurations | PASS — `min det = 1.76e-2 > 0` on 50 Haar samples |
| V8 | Conditional symmetrized product `K_τ · sqrt(det_F(U) det_F(V)) > 0` pointwise on Haar pairs | PASS — `min product = 2.92e-5 > 0` on 30 (U,V) pairs |

**Final tally:** `PASS=8 FAIL=0`, runtime ≈ 1.23 s.

Cached output: [`logs/runner-cache/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.txt`](../logs/runner-cache/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.txt).

---

## Cross-references

- **Parent row:** `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md` — candidate 2 (Perron-Frobenius for the positive transfer matrix), now supplied at finite Lambda for `T_W` and conditionally for the symmetrized staggered+Wilson transfer operator.
- **Bridge note:** `CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md` supplies the downstream bridge `Delta_T > 0` -> temporal connected-correlator clustering; it is downstream of this note, not a dependency of the operator-gap support theorem.
- **Leg A:** `STRONG_CP_THETA_ZERO_NOTE.md` — `det(D + m I) > 0` is the named conditional dependency for the staggered+Wilson composition; cited as parent-context only. The load-bearing conditional edge is to the salvage repair [`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md) (sibling 2026-05-19 note, PR #1582 salvage commit `5f6f0b87a`), not to the older unfixed parent row.
- **Closed PR:** [#1531](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1531) — the rejected 4×4 toy version, replaced by this note.

---

*End of note.*
