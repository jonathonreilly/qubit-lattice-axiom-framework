# Finite-Λ Lieb-Robinson Bound; Cluster-Decomposition Route Support Only

**Date:** 2026-05-19; 2026-06-06 interaction-graph path-count repair; 2026-06-06 inclusive-branching repair; 2026-06-08 LR-only audit-scope repair.
**Status (source-side label):** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py`](../scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py)
**Cached output:** [`logs/runner-cache/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.txt`](../logs/runner-cache/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.txt)
**Parent repair target:** `docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md` (backticked — parent this note supports; not a load-bearing dep). This row now supplies only the finite-volume Lieb-Robinson half identified in the parent's `notes_for_re_audit_if_any`.
**Companion (Δ_T > 0 half):** `docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md` (sibling 2026-05-19 note, landed source-side via salvage commit `8369973af`; audit status remains audit-lane authority — backticked as sibling-evidence, not load-bearing dep).
**Status authority:** independent audit lane only. The `bounded_theorem` label above is a source-side claim-boundary declaration, not an audit verdict.

## §0. Honest framing

The parent row `axiom_first_cluster_decomposition_theorem_note_2026-04-29` is recorded `audited_conditional` with the explicit `notes_for_re_audit_if_any` instruction:

> "cheapest repair is a retained proof of Δ_T > 0 PLUS a retained spatial gap-plus-Lieb-Robinson or spatial transfer-matrix cluster-decomposition theorem for the canonical Cl(3)⊗Z³ Hamiltonian."

This note supplies a source-side **finite-Λ Lieb-Robinson theorem** only. The companion `Δ_T > 0` half is a separate source theorem note on the pure-Wilson surface via PR #1577 (salvage commit `8369973af`); the staggered+Wilson extension `T_full = T_W · T_F` remains conditional on the separately landed strong-CP/operator-basis surface, `docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md` (sibling 2026-05-19 note, Leg A composition for T_full only; backticked as sibling-only — the LR proof here is bosonic-side and structurally independent of the staggered+Wilson extension).

The proof in this note develops the Lieb-Robinson bound from **operator-theoretic primitives** — Duhamel iteration, locality of the local Hamiltonian, triangle inequality on nested commutators, path counting on the interaction graph, factorial control via Stirling. **It does not cite Lieb-Robinson 1972, Hastings 2004, or Nachtergaele-Sims as black-box proof inputs.** Those works are the *technique source* — the inline development here is elementary and self-contained.

The spatial cluster-decomposition portion records the standard finite-volume route from a Lieb-Robinson bound plus a spectral gap to exponential connected-correlator decay. It is **not** part of this row's load-bearing theorem after the 2026-06-08 repair. The cluster-decomposition inequality is route support only because the filter argument below is an explicit bounded sketch, not a fully audited Paley-Wiener/Hastings filter theorem.

### 2026-06-08 LR-only audit-scope repair

The latest audit accepted the finite-volume Lieb-Robinson derivation but kept
the row conditional because the source also carried a spatial clustering route
without a retained finite-volume filter/Hastings-Koma bridge and retained
`Δ_T > 0` input. This repair narrows the audited claim surface:

- **load-bearing theorem:** Lemma C, the finite-volume Lieb-Robinson bound
  derived from locality, Duhamel iteration, inclusive interaction-chain
  counting, and factorial tail control;
- **non-load-bearing route support:** the cluster-decomposition sketch in §5
  and the transfer-gap composition discussion in §6;
- **not claimed:** a finite-volume cluster-decomposition theorem, a
  thermodynamic-limit cluster theorem, a Yang-Mills mass gap, or a continuum
  OS/cluster result.

Independent audit still owns the parent cluster-decomposition row. This row
does not apply a ledger verdict.

### Honest scope (read this first)

- **Finite-Λ only.** Λ ⊂ Z³ is a finite connected spatial sublattice. All operator norms, commutator bounds, and correlation length statements are at fixed finite Λ. No thermodynamic-limit claim.
- **No uniform-in-Λ bound.** The constants `C`, `v_LR`, and `ξ_cluster` are bounded in terms of finite-Λ data; we do not claim they are bounded uniformly as `Λ → Z³`.
- **NOT the Yang-Mills mass gap.** The Clay Millennium problem requires a continuum, infinite-volume gap on the Yang-Mills functional integral. This note is finite-Λ lattice only.
- **No continuum-limit statement.** The lattice spacing `a` is fixed; we do not address `a → 0`.
- **Gauge-invariant Hilbert reduction.** We work in the full link-variable Hilbert space `H_Λ = L²(SU(3)^E, dU)`. Reduction to gauge-invariant subspaces is straightforward at the structural level used here (`T_W` and `[H, ·]` preserve the gauge-invariant subspace) but the full reduction theorem is outside this note's load-bearing scope.
- **Physical Cl(3) local algebra.** The physical Cl(3) local algebra enters only through finite-dimensional bounded site operators of explicit norm; it is treated structurally, not via any model-specific identity.

---

## §1. Setting

Let `Λ ⊂ Z³` be a finite connected spatial lattice. The canonical physical Cl(3) local algebra on the `Z^3` spatial substrate with Wilson+staggered Hamiltonian on the single-time-slice Hilbert space `H_Λ` is

```
H  =  Σ_{Z ⊆ Λ} h_Z                                                       (1.1)
```

where each `h_Z` is a self-adjoint bounded operator supported on a finite-diameter region `Z ⊆ Λ`. For the canonical physical Cl(3) local algebra on the `Z^3` spatial substrate with Wilson+staggered Hamiltonian:

- **Plaquette / Wilson terms** `h_P`: supported on the four sites of an
  elementary plaquette `P`; in the lattice `ell_1` metric used below,
  `diam_1(P) = 2a`.
- **Staggered fermion terms** `h_{x,x+μ̂}`: nearest-neighbor hops; `diam = a`.
- **On-site mass / Cl(3) terms** `h_x`: supported on `{x}`; `diam = 0`.

In all cases:

- **(H-range) Finite range.** Distances below use the lattice `ell_1`
  metric. Each `h_Z` has `diam_1(Z) <= R_0` for a finite `R_0 = 2a`
  (with `a = 1` in lattice units, so `R_0 = 2`): nearest-neighbor
  staggered hops have diameter `a`, on-site terms have diameter `0`, and
  elementary plaquette terms have `ell_1` diameter `2a`.
- **(H-norm) Uniform norm bound.** Each `h_Z` has operator norm `‖h_Z‖ ≤ J` for a constant `J` independent of `Z`, depending only on the canonical normalization of the Wilson coupling `β`, the staggered hopping coefficient, and the physical Cl(3) on-site operator norms.
- **(H-degree) Bounded local degree.** Each site `x ∈ Λ` is contained in at most `Z_max` distinct terms `h_Z`; for the canonical physical Cl(3) local algebra on the `Z^3` spatial substrate with Wilson+staggered Hamiltonian, `Z_max ≤ 12 + 6 + 1 = 19` (12 plaquettes per site on Z³, 6 nearest-neighbor hops, 1 on-site).

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

## §3. Lemma B — Interaction-graph chain count

The previous version counted arbitrary support-union growth sequences. That
count was not a valid bounded-degree path estimate: at step `k`, the union may
contain `O(k)` local terms, so a naive "choose anything touching the union"
bound does not give a fixed branching factor. The repaired proof uses the
standard interaction-graph chain count, which is the quantity needed for the
commutator between two separated supports.

Let `I_Lambda` be the finite set of local interaction supports `Z` with
`h_Z != 0`. Define the interaction graph `G_I` on `I_Lambda` by joining two
distinct vertices `Z, Z'` when `Z ∩ Z' != empty`. For the chain count below,
use the inclusive overlap degree

```text
D_I^+ := max_Z |{Z' in I_Lambda : Z' ∩ Z != empty}|.
```

The superscript `+` is load-bearing: repeated local terms are allowed in the
nested-commutator expansion, so `Z_{i+1} = Z_i` must be counted. The older
exclusive degree `max_Z |{Z' : Z' ∩ Z != empty, Z' != Z}|` is not used in the
LR constants.

For the finite-range Wilson+staggered+on-site surface, `D_I^+` is finite. A
coarse bound is `D_I^+ <= s_max Z_max`, where
`s_max := max_Z |Z| <= 4` for plaquettes/hops/on-site terms and
`Z_max <= 19` is the number of local terms touching a site. This coarse bound
counts `Z` itself and may overcount terms touching several sites of `Z`; it is
chosen only to make the finite-volume constant explicit.

For local supports `X,Y`, define an interaction chain of length `n` from `X`
to `Y` as a sequence `(Z_1,...,Z_n)` such that

- `Z_1 ∩ X != empty`,
- `Z_i ∩ Z_{i+1} != empty` for `1 <= i < n`,
- `Z_n ∩ Y != empty`.

Let `N_chain(n; X, Y)` be the number of such chains. Then

```text
N_chain(n; X, Y) <= N_X (D_I^+)^(n-1),     N_X := |{Z : Z ∩ X != empty}| <= Z_max |X|.  (B.1)
```

Also, if `R := dist_1(X,Y)` and every local term has `ell_1` diameter at most
`R_0`, no chain can reach from `X` to `Y` unless

```text
n >= r := ceil(R / R_0).                                                   (B.2)
```

**Proof.** There are at most `N_X` choices for `Z_1`. Once `Z_i` is fixed,
there are at most `D_I^+` overlap choices for `Z_{i+1}`, including the repeated
choice `Z_{i+1}=Z_i`. This proves (B.1) for the full nested-commutator
expansion rather than only for self-avoiding interaction paths.
For (B.2), a chain of `n` overlapping local terms can advance the `ell_1`
distance from `X` by at most `n R_0`: the first support intersects `X`, each
successive support overlaps the previous one, and each support has diameter at
most `R_0`. Hence reaching `Y` requires `R <= n R_0`. ∎

This chain count is deliberately coarser than optimized Lieb-Robinson
interaction-norm estimates, but it has the needed fixed branching factor and
is sufficient for the finite-volume LR support theorem.

---

## §4. Lemma C — Lieb-Robinson bound from primitives

**Lemma C.** Let `A`, `B` be local observables with `supp(A) subset X`,
`supp(B) subset Y`, and `R := dist_1(X,Y)`. Set

```text
r := ceil(R / R_0),          lambda := 2 J D_I^+ |t|.
```

Then for all `t in R`,

```text
||[A(t), B]|| <= 2 ||A|| ||B|| N_X sum_{n >= r} lambda^n / n!.             (C.1)
```

Consequently, for the useful regime `lambda <= r/2`,

```text
||[A(t), B]|| <= 4 ||A|| ||B|| N_X (e lambda / r)^r.                       (C.2)
```

Equivalently, after the usual coarse light-cone packaging, there are finite
constants

```text
v_LR := 2 e J D_I^+ R_0,          xi := R_0 / log 2,          C_0 := 4 Z_max,
```

such that in the strict spacelike region with the stated margin,

```text
||[A(t), B]|| <= C_0 |X| ||A|| ||B|| exp(-(R - v_LR |t|) / xi).            (C.3)
```

Outside that region the universal ceiling
`||[A(t),B]|| <= 2||A||||B||` is retained. Thus the theorem supplies the
finite-volume Lieb-Robinson light-cone structure with explicit finite
constants; no optimized uniform-in-volume constant is claimed.

**Proof.** Use the standard Duhamel commutator recursion, not the invalid
union-growth sequence count. Expanding iteratively and bracketing with `B`,
only interaction chains from `X` to `Y` can contribute: a nonzero contribution
must contain a sequence of local terms whose consecutive supports overlap,
starting at `X` and ending at `Y`. For each length-`n` chain the nested
commutator norm is bounded by `(2J)^n ||A||`, and the final commutator with
`B` contributes the factor `2||B||`. Lemma B gives at most
`N_X (D_I^+)^(n-1) <= N_X (D_I^+)^n` chains and no chain can contribute for
`n < r`. Therefore

```text
||[A(t), B]||
  <= 2 ||A|| ||B|| sum_{n >= r} |t|^n/n! (2J)^n N_X (D_I^+)^n
  =  2 ||A|| ||B|| N_X sum_{n >= r} lambda^n/n!,
```

which is (C.1).

For `lambda <= r/2`,

```text
sum_{n >= r} lambda^n/n!
  = lambda^r/r! sum_{k >= 0} lambda^k r!/(r+k)!
  <= lambda^r/r! sum_{k >= 0} (lambda/r)^k
  <= 2 lambda^r/r!
  <= 2 (e lambda/r)^r,
```

using `(r+k)!/r! >= r^k` and Stirling `r! >= (r/e)^r`. This proves (C.2).
If `R` is large compared with `v_LR |t|`, the last expression is bounded by
the exponential form (C.3) after using `N_X <= Z_max |X|`, setting
`C_0 = 4 Z_max`, and taking `xi = R_0/log 2`. ∎

---

## §5. Non-load-bearing route support — spatial clustering from Lemma C + Δ_T > 0

Let `Ω` be the unique ground state of `H` with a finite-volume gap `Δ > 0`
to the first excited state, and let `A`, `B` be local observables with
`supp(A) = X`, `supp(B) = Y`, and `R := dist(X, Y) > 0`. The standard
finite-volume clustering target is

```
| ⟨Ω | A B | Ω⟩  -  ⟨Ω | A | Ω⟩ ⟨Ω | B | Ω⟩ |
        ≤  C_cluster · |X| · ‖A‖ · ‖B‖ · exp(-R / ξ_cluster).             (D.1)
```

This section does **not** claim an independently retained proof of (D.1).
It records the bounded composition route that future science and the audit lane
may inspect. It is not part of the retained-eligible theorem surface of this
row:

1. Use `P_Ω := |Ω⟩⟨Ω|`, `Q := I - P_Ω`, and

   ```
   ⟨Ω | A B | Ω⟩  -  ⟨Ω | A | Ω⟩ ⟨Ω | B | Ω⟩
        =  ⟨Ω | A Q B | Ω⟩.                                                (D.2)
   ```

2. Insert a time-Fourier filter that suppresses ground/excited mixing on the
   scale `Δ`. A Gaussian-times-cosine kernel is a useful numerical/support
   model because its Fourier transform is exponentially small in the target
   window for large `t_0 · Δ`, but it does **not** vanish exactly on the gap
   interval. Therefore this note does not use that kernel as a completed
   projection theorem.

3. Combine the filter suppression with Lemma C's finite-volume
   Lieb-Robinson bound

   ```
   ‖[A(s), B]‖ ≤ C_0 |X| ‖A‖ ‖B‖ exp(-(R - v_LR |s|) / ξ).                (D.3)
   ```

4. A fully rigorous cluster theorem still needs a clean filter lemma with
   stated hypotheses and constants, or an explicit citation/import recorded as
   a dependency. With that lemma supplied, the expected correlation length has
   the finite-volume form

   ```
   ξ_cluster = O(max(ξ, v_LR / Δ)).                                        (D.4)
   ```

The landable theorem in this note is Lemma C. The cluster-decomposition
portion is route support only: not a finite-volume cluster theorem, not a
status promotion, and not a repo-wide axiom.

---

## §6. Composition with Δ_T > 0 and the parent's row

**Composition recipe.**

1. The Lieb-Robinson bound (Lemma C) is **structural**: it depends only on the local Hamiltonian structure (H-range)–(H-degree) and operator-theoretic primitives (P1)–(P5). It does **not** depend on any gap.

2. The spatial cluster-decomposition route requires a gap `Δ > 0` between the ground state `Ω` and the first excited state. This gap input is supplied source-side by the companion note via the temporal transfer-matrix gap `Δ_T > 0`:

   - For the pure-gauge Wilson surface `T_W`, the companion note's V6 and Theorem 5.1 argue `Δ_T > 0` via Perron-Jentzsch / Krein-Rutman on the trace-class positivity-improving compact operator. That note landed source-side in salvage commit `8369973af` (PR #1577 salvage).
   - The Hamiltonian-form gap `Δ` is related to `Δ_T` by `Δ = -log(λ_1 / λ_0)` where `λ_0, λ_1` are the top two transfer-matrix eigenvalues. Since `Δ_T > 0` is exactly the statement `λ_0 > λ_1 > 0` (with `λ_0` simple), this gives `Δ > 0` on the Hamiltonian side.

3. For the staggered+Wilson `T_full = T_W · T_F` extension, the gap is conditional on the separately reviewed strong-CP/operator-basis input, `docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md` (sibling 2026-05-19 note; backticked as sibling-only — Leg A composition is for T_full only, the LR proof here is bosonic-side). If the needed positivity input for `T_F = det(D[U] + m I) > 0` is retained by the independent audit lane, the same Perron-Jentzsch route can be inspected for the full physical Cl(3) local algebra on the `Z^3` spatial substrate.

4. **The Lieb-Robinson half (Lemma C) itself does NOT depend on `Δ_T > 0`.** It is proved unconditionally from primitives in §4.

**Conclusion on the parent row.** The source-side composition picture is:
- (i) `Δ_T > 0` half: source-side PR #1577 salvage (Wilson surface; staggered+Wilson conditional on the strong-CP/operator-basis input).
- (ii) Lieb-Robinson half: Lemma C here.
- (iii) Missing cluster half: a retained finite-volume filter/Hastings-Koma
  bridge plus retained gap input for the relevant surface.

This row therefore does **not** close the parent cluster-decomposition row by
itself. It supplies only the finite-volume LR ingredient and leaves the
filter/composition step as the next required theorem.

---

## §7. Theorem statement (finite-Λ physical Cl(3) / `Z^3` Wilson+staggered)

On a finite connected `Λ ⊂ Z³` with the canonical physical Cl(3) local algebra on the `Z^3` spatial substrate and Wilson+staggered Hamiltonian `H = Σ_Z h_Z` satisfying (H-range), (H-norm), and (H-degree):

**(LR) Lieb-Robinson bound.** For all local observables `A`, `B` with disjoint supports `X, Y` and `R := dist(X, Y) > 0`, for all `t ∈ R`:

```
‖[A(t), B]‖  ≤  C_0 · |X| · ‖A‖ ‖B‖ · exp(-(R - v_LR |t|) / ξ)             (LR)
```

with `v_LR = 2 e J D_I^+ R_0` and `ξ = R_0 / log 2`, where `J`, `D_I^+`, and
`R_0` are the constants of §1 + Lemma B.

**Proof:** §2 (Lemma A) + §3 (Lemma B) + §4 (Lemma C).

**(Route support only, not part of this theorem) Spatial cluster-decomposition route.** Assume `Δ > 0` (the Hamiltonian gap derived from `Δ_T > 0` of the companion note) and a rigorous finite-volume filter lemma with the hypotheses and constants named in §5. For the ground state `|Ω⟩` and all local observables `A`, `B` with `R := dist(supp A, supp B) > 0`, the expected target bound is:

```
| ⟨Ω | A B | Ω⟩  -  ⟨Ω | A | Ω⟩ ⟨Ω | B | Ω⟩ |
     ≤  C_cluster · |X| · ‖A‖ ‖B‖ · exp(-R / ξ_cluster)                    (CD)
```

with `ξ_cluster = O(max(ξ, v_LR / Δ))`.

**Disposition:** §5 records non-load-bearing route support. This note does not claim (CD), does not promote it to an independently retained theorem, and does not close the parent cluster-decomposition row.

---

## §8. Out-of-scope, and what this note does not claim

1. **Thermodynamic limit Λ → Z³.** The expected correlation length `ξ_cluster = O(max(ξ, v_LR / Δ))` may grow as `Λ` grows if the gap `Δ` shrinks. No uniform-in-Λ cluster bound is claimed.

2. **Yang-Mills mass gap (Clay).** The Clay Millennium problem requires a continuum, infinite-volume, gap on the Yang-Mills functional integral. This note is a finite-volume lattice statement. The gap input `Δ_T > 0` is also finite-Λ; promoting either to the continuum infinite-volume setting requires additional, separately audited theorems.

3. **Continuum limit `a → 0`.** Lattice spacing `a` is fixed (set `a = 1`). The classical-continuum limit is a separate program.

4. **Gauge-invariant Hilbert reduction.** We work on the full link-variable Hilbert space `L²(SU(3)^E, dU)`. The reduction to gauge-invariant subspaces is consistent with our setting (`T_W` and `[H, ·]` preserve gauge-invariance), but the full reduction theorem is not load-bearing here.

5. **Open boundary conditions vs. periodic.** The proofs work for either choice. The runner uses open boundary for the spin chain (V1–V5), reflecting the canonical lattice convention; the SU(3) verifications (V6–V8) use a 2-site Λ which is small enough that boundary structure is explicit.

6. **Constants are not optimized.** Both `v_LR` and any downstream route-support `ξ_cluster` have sharper forms in the literature (using `M(s)` reproducing-kernel constructions, weighted Lieb-Robinson, etc.). We use the loose path-counting bound because it is sufficient for the finite-volume LR theorem. The downstream cluster constants are not load-bearing here.

---

## §9. Runner

The companion runner [`scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py`](../scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py) exhibits the load-bearing LR claim and non-load-bearing cluster-route checks numerically on real small lattice systems:

- **V1–V4: Lieb-Robinson locality, nested-commutator norm, and commutator-spread checks on a 6-site spin-1/2 Heisenberg chain.** Real lattice, exact diagonalization, and explicitly bounded finite-system scope.
- **V5: finite-N cluster-support fit on the same chain.** This is qualitative support only because the open Heisenberg chain is not a thermodynamic-limit gapped cluster theorem.
- **V6–V7: Composition with PR #1577's SU(3) truncated character basis transfer matrix.** Verifies `Δ_T > 0` on the SU(3) transfer spectrum and exhibits the structural exponential sequence implied by the top two eigenvalues; V7 is not a direct connected-character-correlator measurement.
- **V8: Anti-overclaim verification.** Confirms finite-Λ-only scope by showing that the extracted correlation length is Λ-dependent.
- **V9: Inclusive branching guard.** Brute-forces repeated interaction chains on a minimal two-term graph and confirms that the exclusive-degree count fails while the inclusive `D_I^+` count holds; also checks a 1D bond graph against the inclusive bound.

All nine verifications use only NumPy/SciPy and complete in under one minute on a laptop. PASS/FAIL with hard assertion gates is reported.

---

## §10. Audit-pipeline crosswalk

- **Repair target:** this row's conditional audit status and the parent row `axiom_first_cluster_decomposition_theorem_note_2026-04-29` in [`docs/audit/data/audit_ledger.json`](audit/data/audit_ledger.json).
- **This PR's closure target:** finite-Λ Lieb-Robinson theorem only.
- **Still required for the parent cluster row:** retained Δ_T/gap input plus a retained finite-volume filter/Hastings-Koma bridge or spatial transfer-matrix cluster-decomposition theorem.
- **Effective-status determination:** belongs to the audit lane after independent review.
- **No edits to `docs/audit/data/*.json`** are made by this note.

---

## §11. Cross-references

- Parent row: `docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md` (backticked — parent this note supports; not a load-bearing dep on this proof's chain).
- Companion Δ_T > 0 note: `docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md` (sibling-evidence for the downstream route only; the LR bound proved here stands structurally without needing the companion's retained status).
- Mass-gap bridge (retained_bounded, route-support authority for the non-load-bearing gap-input discussion in §5/§6): [`docs/CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md)
- Strong-CP/operator-basis input (conditional for staggered+Wilson): `docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md` (sibling 2026-05-19 note; backticked as sibling-only — Leg A composition for T_full only, the LR proof is bosonic-side).

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md` (effective_status: unaudited — demoted to backtick per dep-hygiene rule; sibling 2026-05-19 note, composition source for §6 staggered+Wilson conditional extension, not load-bearing on the pure Lieb-Robinson proof of §4)
- `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md` (effective_status: unaudited — demoted to backtick per dep-hygiene rule; sibling 2026-05-19 note, named conditional input for §6 staggered+Wilson extension only)
