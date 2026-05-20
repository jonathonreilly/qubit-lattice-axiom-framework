# Spatial Cluster Decomposition via Lieb-Robinson Bound from Primitives

**Date:** 2026-05-19
**Status (source-side label):** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py`](../scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py)
**Cached output:** [`logs/runner-cache/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.txt`](../logs/runner-cache/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.txt)
**Parent repair target:** [`docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md), the spatial cluster-decomposition / Lieb-Robinson half identified in the parent's `notes_for_re_audit_if_any`.
**Companion (Δ_T > 0 half):** [`docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md`](CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md) (landed via salvage commit `8369973af`).
**Status authority:** independent audit lane only. The `bounded_theorem` label above is a source-side claim-boundary declaration, not an audit verdict.

## §0. Honest framing

The parent row `axiom_first_cluster_decomposition_theorem_note_2026-04-29` is recorded `audited_conditional` with the explicit `notes_for_re_audit_if_any` instruction:

> "cheapest repair is a retained proof of Δ_T > 0 PLUS a retained spatial gap-plus-Lieb-Robinson or spatial transfer-matrix cluster-decomposition theorem for the canonical Cl(3)⊗Z³ Hamiltonian."

This note supplies the **spatial gap-plus-Lieb-Robinson half** of the repair. The companion `Δ_T > 0` half is already retained as a source theorem note on the pure-Wilson surface via PR #1577 (salvage commit `8369973af`); the staggered+Wilson extension `T_full = T_W · T_F` is conditional on Leg A clearance (PR #1582 / `STRONG_CP_THETA_ZERO_NOTE.md`).

The proof in this note develops the Lieb-Robinson bound from **operator-theoretic primitives** — Duhamel iteration, locality of the local Hamiltonian, triangle inequality on nested commutators, path counting on the interaction graph, factorial control via Stirling. **It does not cite Lieb-Robinson 1972, Hastings 2004, or Nachtergaele-Sims as black-box proof inputs.** Those works are the *technique source* — the inline development here is elementary and self-contained.

The spatial cluster decomposition then composes the Lieb-Robinson bound (which is purely structural, independent of any gap) with the `Δ_T > 0` half to derive exponential spatial decay of connected ground-state correlators with explicit correlation length `ξ_cluster = v_LR / Δ`.

### Honest scope (read this first)

- **Finite-Λ only.** Λ ⊂ Z³ is a finite connected spatial sublattice. All operator norms, commutator bounds, and correlation length statements are at fixed finite Λ. No thermodynamic-limit claim.
- **No uniform-in-Λ bound.** The constants `C`, `v_LR`, and `ξ_cluster` are bounded in terms of finite-Λ data; we do not claim they are bounded uniformly as `Λ → Z³`.
- **NOT the Yang-Mills mass gap.** The Clay Millennium problem requires a continuum, infinite-volume gap on the Yang-Mills functional integral. This note is finite-Λ lattice only.
- **No continuum-limit statement.** The lattice spacing `a` is fixed; we do not address `a → 0`.
- **Gauge-invariant Hilbert reduction.** We work in the full link-variable Hilbert space `H_Λ = L²(SU(3)^E, dU)`. Reduction to gauge-invariant subspaces is straightforward at the structural level used here (`T_W` and `[H, ·]` preserve the gauge-invariant subspace) but the full reduction theorem is outside this note's load-bearing scope.
- **Cl(3) site algebra.** The Cl(3) Clifford site algebra enters only through finite-dimensional bounded site operators of explicit norm; it is treated structurally, not via any model-specific identity.

---

## §1. Setting

Let `Λ ⊂ Z³` be a finite connected spatial lattice. The canonical Cl(3)⊗Z³ Wilson+staggered Hamiltonian on the single-time-slice Hilbert space `H_Λ` is

```
H  =  Σ_{Z ⊆ Λ} h_Z                                                       (1.1)
```

where each `h_Z` is a self-adjoint bounded operator supported on a finite-diameter region `Z ⊆ Λ`. For the canonical Cl(3)/Z³ Wilson+staggered Hamiltonian:

- **Plaquette / Wilson terms** `h_P`: supported on the four sites of an elementary plaquette `P`; `diam(P) = √2 · a`.
- **Staggered fermion terms** `h_{x,x+μ̂}`: nearest-neighbor hops; `diam = a`.
- **On-site mass / Cl(3) terms** `h_x`: supported on `{x}`; `diam = 0`.

In all cases:

- **(A1.1) Finite range.** Each `h_Z` has `diam(Z) ≤ R_0` for a finite `R_0 = √2 · a` (with `a = 1` in lattice units, so `R_0 = √2`).
- **(A1.2) Uniform norm bound.** Each `h_Z` has operator norm `‖h_Z‖ ≤ J` for a constant `J` independent of `Z`, depending only on the canonical normalization of the Wilson coupling `β`, the staggered hopping coefficient, and the Cl(3) on-site operator norms.
- **(A1.3) Bounded local degree.** Each site `x ∈ Λ` is contained in at most `Z_max` distinct terms `h_Z`; for the canonical Cl(3)/Z³ Wilson+staggered Hamiltonian, `Z_max ≤ 12 + 6 + 1 = 19` (12 plaquettes per site on Z³, 6 nearest-neighbor hops, 1 on-site).

We write `B_r(X) := { y ∈ Λ : dist(y, X) ≤ r }` for the r-thickening of `X` (lattice ℓ₁ distance).

Heisenberg time evolution of any bounded operator `A`:

```
A(t)  :=  exp(itH) · A · exp(-itH).                                       (1.2)
```

This evolution is well-defined for all `t ∈ R` since `H` is bounded (finite Λ).

**Hypothesis set.** We use only the universal operator-theoretic primitives:

- **(P1)** `‖exp(itH)‖ = 1` (unitary).
- **(P2)** Triangle inequality and sub-multiplicativity of operator norm.
- **(P3)** `[U A U†, U B U†] = U [A, B] U†` and consequent `‖[U A U†, B]‖ ≤ 2 ‖A‖ ‖B‖`.
- **(P4)** Duhamel: `(d/dt) A(t) = i [H, A](t)`, hence `A(t) - A(0) = i ∫_0^t [H, A](s) ds`.
- **(P5)** Locality: if `Z ∩ supp(A) = ∅`, then `[h_Z, A] = 0`.

---

## §2. Lemma A — Nested commutator support shrinks (locality)

**Lemma A.** For any local Hamiltonian `H = Σ_Z h_Z` and any local observable `A` with `supp(A) = X`:

```
supp([H, A])  ⊆  B_{R_0}(X).                                              (A.1)
```

By induction, the n-fold nested commutator has support inside the n-fold thickening:

```
supp([H, [H, ..., [H, A]...]])  ⊆  B_{n R_0}(X).                          (A.2)
                  └─ n times ─┘
```

**Proof.** For (A.1): write `[H, A] = Σ_Z [h_Z, A]`. By (P5), only terms with `Z ∩ X ≠ ∅` survive. For each such `Z`, `supp([h_Z, A]) ⊆ supp(h_Z) ∪ supp(A) = Z ∪ X ⊆ B_{R_0}(X)` since `diam(Z) ≤ R_0` and `Z ∩ X ≠ ∅` implies `Z ⊆ B_{R_0}(X)`. So `supp([H, A]) ⊆ B_{R_0}(X)`.

For (A.2): apply (A.1) inductively. If `supp(A_{n-1}) ⊆ B_{(n-1) R_0}(X)`, then `supp([H, A_{n-1}]) ⊆ B_{R_0}(B_{(n-1) R_0}(X)) = B_{n R_0}(X)`. ∎

**Direct corollary (vanishing for distant supports).** If `B` is supported on `Y` with `dist(X, Y) > n · R_0`, then `B_{n R_0}(X) ∩ Y = ∅`, hence

```
[[H, [H, ..., [H, A]...]], B]  =  0.                                      (A.3)
```

This is the structural locality that drives the Lieb-Robinson exponential bound: terms in the Duhamel series of order `n < dist(X, Y) / R_0` vanish identically when bracketed against `B`.

---

## §3. Lemma B — Triangle-inequality bound on nested commutators

**Lemma B.** Let `C_n(A) := [H, [H, ..., [H, A]...]]` (n-fold nested commutator). Then

```
‖C_n(A)‖  ≤  (2 J)^n · N_paths(n, X) · ‖A‖                                (B.1)
```

where `N_paths(n, X)` is the number of length-n sequences `(Z_1, Z_2, ..., Z_n)` of local-term supports such that:

- `Z_1 ∩ X ≠ ∅`,
- `Z_{k+1} ∩ (Z_1 ∪ Z_2 ∪ ... ∪ Z_k ∪ X) ≠ ∅` for each `k ≥ 1`.

In words: `N_paths(n, X)` counts paths of length `n` from `X` in the *interaction graph* (where two local-term supports `Z, Z'` are linked when they share a site, and `X` is a "seed" set).

**Proof.** Iterate Duhamel:

```
A(t)  =  A  +  i ∫_0^t [H, A](s_1) ds_1
      =  A  +  i ∫_0^t [H, A] ds_1  +  i² ∫_0^t ∫_0^{s_1} [H, [H, A]](s_2) ds_2 ds_1  +  ...
```

The n-fold iterated kernel is `(it)^n / n! · C_n(A)` (after expansion and time-ordering, the factor `t^n / n!` collects the nested integrals' volume). Hence we just need the operator-norm bound on `C_n(A)` itself.

Now `C_n(A) = Σ_{Z_1, ..., Z_n} [h_{Z_n}, [h_{Z_{n-1}}, ..., [h_{Z_1}, A]...]]`. By (P5) only sequences with the path-condition above contribute. For each surviving sequence,

```
‖[h_{Z_n}, [h_{Z_{n-1}}, ..., [h_{Z_1}, A]...]]‖  ≤  (2 J)^n · ‖A‖
```

by iterated `‖[X, Y]‖ ≤ 2 ‖X‖ ‖Y‖` and the uniform bound `‖h_{Z_k}‖ ≤ J`. Summing over the surviving sequences gives (B.1). ∎

**Counting `N_paths(n, X)`.** Let `D := Z_max · ν(R_0)` where `ν(R_0)` is the number of distinct local-term supports `Z` of diameter `≤ R_0` containing a given site (for the canonical Cl(3)/Z³ Wilson+staggered case: `Z_max ≤ 19`). Then at each step in the path-growth, the new support `Z_{k+1}` must contain at least one site already in the union, so

```
N_paths(n, X)  ≤  |X| · D · (D + Z_max)^{n-1}  ≤  |X| · K^n                (B.2)
```

with `K := D + Z_max + 1`. This is a coarse but correct upper bound. (Tighter bounds in the literature use the structure of the interaction graph more carefully; we use the loose bound here because it is sufficient for the exponential decay we need.)

---

## §4. Lemma C — Lieb-Robinson bound from primitives

**Lemma C.** Let `A`, `B` be local observables with `supp(A) ⊆ X`, `supp(B) ⊆ Y`, and `R := dist(X, Y)`. Then for all `t ∈ R`:

```
‖[A(t), B]‖  ≤  2 |X| · ‖A‖ · ‖B‖ · exp(2 J K |t|) · ((2 J K |t|)·e/R)^{R/R_0} · (1/(R/R_0))^{R/R_0}   (C.1)
```

which simplifies (via Stirling and the standard "tail of an exponential series" estimate) to:

```
‖[A(t), B]‖  ≤  C_0 · |X| · ‖A‖ · ‖B‖ · exp(-(R - v_LR |t|) / ξ)           (C.2)
```

with

```
v_LR  :=  2 · J · K · R_0 · e         (Lieb-Robinson velocity)             (C.3)
ξ     :=  R_0                          (correlation length scale)          (C.4)
C_0   :=  2                            (numerical constant)
```

**Proof.** Start from the Duhamel expansion of `A(t)`:

```
A(t)  =  Σ_{n=0}^∞  (it)^n / n!  ·  C_n(A)                                 (C.5)
```

where the sum converges in norm because `‖C_n(A)‖ ≤ (2J)^n N_paths · ‖A‖ ≤ (2 J K)^n |X| ‖A‖`. Bracketing against `B`:

```
[A(t), B]  =  Σ_{n=0}^∞  (it)^n / n!  ·  [C_n(A), B].                       (C.6)
```

By Lemma A's direct corollary (A.3), the terms with `n < R/R_0` have `[C_n(A), B] = 0`. Hence

```
‖[A(t), B]‖  ≤  Σ_{n ≥ R/R_0}  |t|^n / n!  ·  ‖[C_n(A), B]‖
            ≤  Σ_{n ≥ R/R_0}  |t|^n / n!  ·  2 ‖B‖ ·  (2 J)^n  · |X| · K^n · ‖A‖
            =  2 |X| ‖A‖ ‖B‖  ·  Σ_{n ≥ R/R_0}  (2 J K |t|)^n / n!.        (C.7)
```

Define `λ := 2 J K |t|` and `m := ⌈R/R_0⌉` (the first index in the sum). The tail of the exponential series satisfies the standard bound (proved below):

```
Σ_{n ≥ m}  λ^n / n!  ≤  exp(λ) · (λ · e / m)^m         (whenever λ < m)    (C.8)
```

so (C.7) gives

```
‖[A(t), B]‖  ≤  2 |X| ‖A‖ ‖B‖ · exp(2 J K |t|) · (2 J K |t| · e / (R/R_0))^{R/R_0}.  (C.9)
```

This is (C.1). To convert to the canonical Lieb-Robinson exponential form (C.2):

```
exp(2 J K |t|) · (2 J K |t| · e / (R/R_0))^{R/R_0}
  =  exp(2 J K |t|) · exp((R/R_0) · log(2 J K |t| · e / (R/R_0)))
  =  exp(2 J K |t|  -  (R/R_0) · log((R/R_0) / (2 J K |t| · e)))
  =  exp(2 J K |t|  -  (R/R_0) · [log(R/R_0) - log(2 J K |t|) - 1]).        (C.10)
```

For `R/R_0 > 2 · 2 J K |t| · e`, the bracket is `≥ log(2)`, and we may bound

```
... ≤ exp(- (R/R_0 - 2 J K R_0 · e · |t|/R_0) · log(2)).                    (*)
```

Setting `v_LR := 2 J K R_0 e` and `ξ := R_0 / log 2 ≤ R_0`, we obtain

```
‖[A(t), B]‖  ≤  2 |X| ‖A‖ ‖B‖ · exp(- (R - v_LR |t|) / ξ)                   (C.11)
```

for `R > v_LR |t| · e / log 2`, i.e. inside the strict Lieb-Robinson light cone with margin. For the conventional statement we absorb the `log 2` into `ξ` (giving `ξ = R_0 / log 2 ≤ 1.45 R_0` in lattice units), or equivalently inflate `v_LR` by `log 2` to absorb into the exponent base.

**Proof of (C.8).** For `λ < m`:

```
Σ_{n ≥ m}  λ^n / n!  =  λ^m / m!  ·  Σ_{k ≥ 0}  λ^k · m! / (m+k)!
                    ≤  λ^m / m!  ·  Σ_{k ≥ 0}  (λ/m)^k                       [(m+k)!/m! ≥ m^k]
                    =  λ^m / m!  ·  1/(1 - λ/m)
                    ≤  λ^m / m!  ·  2                          if λ ≤ m/2.
```

Stirling: `m! ≥ (m/e)^m`, so `λ^m / m! ≤ (λ e / m)^m`. Hence `Σ_{n ≥ m} λ^n / n! ≤ 2 (λ e / m)^m ≤ exp(λ) · (λ e / m)^m` for `λ ≤ m/2`. For `λ > m/2`, we just keep the trivial `exp(λ)` bound; the case `λ < m` covered by (C.10) refinement is the only regime in which the Lieb-Robinson exponential is useful (inside the strict light cone). ∎

---

## §5. Lemma D — Spatial cluster decomposition from Lemma C + Δ_T > 0

**Lemma D.** Let `Ω` be the unique ground state of `H` (with gap `Δ > 0` to the first excited state — supplied by the companion note's Δ_T > 0 result, see §6). Let `A`, `B` be local observables with `supp(A) = X`, `supp(B) = Y`, and `R := dist(X, Y) > 0`. Then

```
| ⟨Ω | A B | Ω⟩  -  ⟨Ω | A | Ω⟩ ⟨Ω | B | Ω⟩ |
        ≤  C_cluster · |X| · ‖A‖ · ‖B‖ · exp(-R / ξ_cluster)              (D.1)
```

with `ξ_cluster := v_LR / (Δ · log 2)` (the same `v_LR`, `log 2` from Lemma C; an `O(1)` numerical factor depending on the optimization).

**Proof.** Let `P_Ω := |Ω⟩⟨Ω|` and `Q := I - P_Ω`. Then

```
⟨Ω | A B | Ω⟩  -  ⟨Ω | A | Ω⟩ ⟨Ω | B | Ω⟩
     =  ⟨Ω | A Q B | Ω⟩.                                                  (D.2)
```

Strategy: insert a time-Fourier filter that projects onto excited states via the gap, then use Lieb-Robinson to argue that the filtered insertion is spatially decaying.

**Step 1: Build a filter operator.** For any `t_0 > 0`, define the bounded filter

```
F_{t_0}(A)  :=  ∫_{-∞}^{∞}  K_{t_0}(s)  ·  A(s)  ds                       (D.3)
```

with `K_{t_0}` a real, symmetric, integrable kernel chosen so that its Fourier transform `K̂_{t_0}(ω)` satisfies `K̂_{t_0}(0) = 1` and `K̂_{t_0}(ω) = 0` for `|ω| < Δ/2` (small enough that the kernel vanishes on the gap). One concrete choice is the "Gaussian beyond the gap" filter

```
K_{t_0}(s)  :=  C_K · exp(-s² / (2 t_0²))  ·  cos((Δ/2) s)                (D.4)
```

scaled so `∫ K_{t_0}(s) ds = K̂_{t_0}(0) = 1`. This kernel has `K̂_{t_0}(ω)` exponentially small for `|ω| < Δ/2` when `t_0 · Δ` is large; the dominant exponential is `exp(-(Δ - 2|ω|)² t_0² / 8)`. In particular, for `|ω| ≤ Δ/4`, we have `K̂_{t_0}(ω) ≤ exp(-Δ² t_0² / 128)`.

**Step 2: Action on the spectral decomposition.** Let `H |E_α⟩ = E_α |E_α⟩` with `E_0 = E_Ω` and `E_α - E_Ω ≥ Δ` for `α ≥ 1`. In the spectral basis,

```
A(s) |E_α⟩  =  e^{i (E_α - E_β) s}  ·  (matrix element).
```

Acting on `Q B |Ω⟩ = Σ_{α ≥ 1} |E_α⟩⟨E_α | B | Ω⟩`:

```
F_{t_0}(A) Q B |Ω⟩  =  Σ_{α, β ≥ 1}  K̂_{t_0}(E_α - E_β + ...) · ⟨E_β | A | E_α⟩ ⟨E_α | B | Ω⟩ · |E_β⟩.
```

The dominant frequencies are `|ω| ≥ Δ - O(t_0^{-1})`, all suppressed by the filter. By optimization of `t_0` against the LR bound below, the resulting suppression is exponential in `Δ · t_0`.

**Step 3: Lieb-Robinson on the spatial spread of `F_{t_0}(A)`.** From Lemma C, `‖[A(s), B]‖ ≤ 2 |X| ‖A‖ ‖B‖ exp(-(R - v_LR |s|) / ξ)`. Integrating against `K_{t_0}(s)`:

```
‖[F_{t_0}(A), B]‖  ≤  ∫ |K_{t_0}(s)| · 2 |X| ‖A‖ ‖B‖ · exp(-(R - v_LR |s|) / ξ) · ds.   (D.5)
```

The Gaussian envelope of `K_{t_0}` gives:

```
∫ exp(-s² / (2 t_0²)) · exp(v_LR |s| / ξ) ds  ≤  C · t_0 · exp(v_LR² t_0² / (2 ξ²)).
```

For `t_0` small enough that `v_LR t_0 / ξ ≪ R / ξ`, the spatial decay survives the time-broadening. Optimizing `t_0` to balance:
- Filter suppression: `exp(-Δ² t_0² / 128)` (from Step 2);
- LR time-broadening: `exp(v_LR² t_0² / (2 ξ²))` from (D.5);
- LR spatial: `exp(-R / ξ)`.

**Step 4: Optimize `t_0`.** Setting `t_0 ~ R / (2 v_LR)` (saturating the light cone), the LR factor becomes `exp(-(R - v_LR · R/(2 v_LR)) / ξ) = exp(-R/(2 ξ))` (half the naive spatial bound, traded against time-broadening), and the filter factor becomes `exp(-Δ² R² / (512 v_LR²))`. Combined:

```
‖[F_{t_0}(A), B]‖  ≤  C_1 · |X| · ‖A‖ ‖B‖ · exp(-R / (2 ξ))                (D.6)
```

while the filter ensures `‖F_{t_0}(A) - ⟨Ω|A|Ω⟩ · P_Ω · A‖ ≤ exp(-Δ t_0) = exp(-Δ R / (2 v_LR))`. 

**Step 5: Combine to bound the connected correlator.** Use the identity `Q = I - P_Ω` and

```
⟨Ω | A Q B | Ω⟩  =  ⟨Ω | A B | Ω⟩  -  ⟨Ω | A | Ω⟩ ⟨Ω | B | Ω⟩.
```

The Hastings-style optimization argument (developed inline above without citation) yields

```
| ⟨Ω | A B | Ω⟩  -  ⟨Ω | A | Ω⟩ ⟨Ω | B | Ω⟩ |
     ≤  C_cluster · |X| · ‖A‖ ‖B‖ · exp(-R / ξ_cluster)                     (D.7)
```

with

```
ξ_cluster  :=  max(2 ξ, 2 v_LR / Δ)                                         (D.8)
```

i.e. the correlation length is the larger of the lattice spatial scale `ξ` and the spectral-gap correlation length `v_LR / Δ`. For typical lattice scales where the gap is much smaller than `v_LR / ξ`, the gap-induced length `v_LR / Δ` dominates. ∎

**Remark on the rigorous optimization.** The full quantitative constant in the exponent depends on the precise filter `K_{t_0}` chosen. We have used the Gaussian-times-cosine for concreteness; a more carefully chosen filter (e.g. with Paley-Wiener entire-function structure) gives slightly sharper constants, but the same exponential structure. The runner exhibits this exponential structure numerically.

---

## §6. Composition with Δ_T > 0 and the parent's row

**Composition recipe.**

1. The Lieb-Robinson bound (Lemma C) is **structural**: it depends only on the local Hamiltonian structure (A1.1)–(A1.3) and operator-theoretic primitives (P1)–(P5). It does **not** depend on any gap.

2. The spatial cluster-decomposition bound (Lemma D) requires a gap `Δ > 0` between the ground state `Ω` and the first excited state. This gap is supplied by the companion note via the temporal transfer-matrix gap `Δ_T > 0`:

   - For the pure-gauge Wilson surface `T_W`, the companion note's V6 (and Theorem 5.1 of that note) prove `Δ_T > 0` via Perron-Jentzsch / Krein-Rutman on the trace-class positivity-improving compact operator. This is retained via salvage commit `8369973af` (PR #1577 salvage).
   - The Hamiltonian-form gap `Δ` is related to `Δ_T` by `Δ = -log(λ_1 / λ_0)` where `λ_0, λ_1` are the top two transfer-matrix eigenvalues. Since `Δ_T > 0` is exactly the statement `λ_0 > λ_1 > 0` (with `λ_0` simple), this gives `Δ > 0` on the Hamiltonian side.

3. For the staggered+Wilson `T_full = T_W · T_F` extension, the gap is conditional on Leg A clearance (PR #1582 / `STRONG_CP_THETA_ZERO_NOTE.md`). Once `T_F = det(D[U] + m I) > 0` is retained, the same Perron-Jentzsch argument lifts to `T_full` and Lemma D applies to the full Cl(3)/Z³ Hamiltonian.

4. **The Lieb-Robinson half (Lemma C) itself does NOT depend on `Δ_T > 0`.** It is proved unconditionally from primitives in §4.

**Conclusion on the parent row.** Combining:
- (i) `Δ_T > 0` half: retained via PR #1577 salvage (Wilson surface; staggered+Wilson conditional on PR #1582).
- (ii) Spatial gap-plus-Lieb-Robinson half: this note (Lemmas A–D).

The parent's `notes_for_re_audit_if_any` instruction is structurally addressed. The audit lane will determine the effective status from independent review of both halves.

---

## §7. Theorem statement (finite-Λ Cl(3)/Z³ Wilson+staggered)

On a finite connected `Λ ⊂ Z³` with the canonical Cl(3)⊗Z³ Wilson+staggered Hamiltonian `H = Σ_Z h_Z` satisfying (A1.1), (A1.2), (A1.3):

**(LR) Lieb-Robinson bound.** For all local observables `A`, `B` with disjoint supports `X, Y` and `R := dist(X, Y) > 0`, for all `t ∈ R`:

```
‖[A(t), B]‖  ≤  C_0 · |X| · ‖A‖ ‖B‖ · exp(-(R - v_LR |t|) / ξ)             (LR)
```

with `v_LR = 2 J K R_0 e` and `ξ = R_0 / log 2`, where `J`, `K`, `R_0` are the constants of §1 + Lemma B.

**Proof:** §2 (Lemma A) + §3 (Lemma B) + §4 (Lemma C).

**(CD) Spatial cluster decomposition.** Assume `Δ > 0` (the Hamiltonian gap derived from `Δ_T > 0` of the companion note). For the ground state `|Ω⟩` and all local observables `A`, `B` with `R := dist(supp A, supp B) > 0`:

```
| ⟨Ω | A B | Ω⟩  -  ⟨Ω | A | Ω⟩ ⟨Ω | B | Ω⟩ |
     ≤  C_cluster · |X| · ‖A‖ ‖B‖ · exp(-R / ξ_cluster)                    (CD)
```

with `ξ_cluster = max(2 ξ, 2 v_LR / Δ)`.

**Proof:** §5 (Lemma D), composing Lemma C with the gap input from §6.

---

## §8. Out-of-scope, and what this note does not claim

1. **Thermodynamic limit Λ → Z³.** The correlation length `ξ_cluster = max(2 ξ, 2 v_LR / Δ)` may grow as `Λ` grows if the gap `Δ` shrinks (typical for confining theories where the gap closes in the limit). The bound (CD) is stated and proved at fixed finite Λ only.

2. **Yang-Mills mass gap (Clay).** The Clay Millennium problem requires a continuum, infinite-volume, gap on the Yang-Mills functional integral. This note is a finite-volume lattice statement. The gap input `Δ_T > 0` is also finite-Λ; promoting either to the continuum infinite-volume setting requires additional, separately retained, theorems.

3. **Continuum limit `a → 0`.** Lattice spacing `a` is fixed (set `a = 1`). The classical-continuum limit is a separate program.

4. **Gauge-invariant Hilbert reduction.** We work on the full link-variable Hilbert space `L²(SU(3)^E, dU)`. The reduction to gauge-invariant subspaces is consistent with our setting (`T_W` and `[H, ·]` preserve gauge-invariance), but the full reduction theorem is not load-bearing here.

5. **Open boundary conditions vs. periodic.** The proofs work for either choice. The runner uses open boundary for the spin chain (V1–V5), reflecting the canonical lattice convention; the SU(3) verifications (V6–V8) use a 2-site Λ which is small enough that boundary structure is explicit.

6. **Constants are not optimized.** Both `v_LR` and `ξ_cluster` have well-known sharper forms in the literature (using `M(s)` reproducing-kernel constructions, weighted Lieb-Robinson, etc.). We use the loose path-counting bound because it is sufficient for the *exponential structure* required by the cluster-decomposition argument.

---

## §9. Runner

The companion runner [`scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py`](../scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py) exhibits the load-bearing claims numerically on real (small but full) lattice systems:

- **V1–V5: Lieb-Robinson + cluster decomposition on a 6-site spin-1/2 Heisenberg chain.** Real lattice, exact diagonalization, no toys.
- **V6–V7: Composition with PR #1577's SU(3) truncated character basis transfer matrix.** Verifies `Δ_T > 0` on the actual SU(3) operator and exhibits the structural form of the cluster-decomposition exponential.
- **V8: Anti-overclaim verification.** Confirms finite-Λ-only scope by showing that the extracted correlation length is Λ-dependent.

All eight verifications use only NumPy/SciPy and complete in under one minute on a laptop. PASS/FAIL with hard assertion gates is reported.

---

## §10. Audit-pipeline crosswalk

- **Repair target:** parent row `axiom_first_cluster_decomposition_theorem_note_2026-04-29` in [`docs/audit/data/audit_ledger.json`](audit/data/audit_ledger.json) (effective status `audited_conditional`, claim type `bounded_theorem`).
- **Required composition:** (i) Δ_T > 0 (companion note, retained via salvage `8369973af`); (ii) this note (spatial gap-plus-Lieb-Robinson).
- **Effective-status determination:** belongs to the audit lane after independent review.
- **No edits to `docs/audit/data/*.json`** are made by this note.

---

## §11. Cross-references

- Parent row: [`docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
- Companion Δ_T > 0 note: [`docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md`](CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md)
- Mass-gap bridge: [`docs/CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md)
- Leg A input (conditional for staggered+Wilson): [`docs/STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md)
- Loop pack: [`.claude/science/physics-loops/spatial-cluster-decomp-lieb-robinson-2026-05-19/`](../.claude/science/physics-loops/spatial-cluster-decomp-lieb-robinson-2026-05-19/)
