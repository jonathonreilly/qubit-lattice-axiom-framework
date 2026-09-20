# moving-kernel-with-vacancies, attempt 2 of 4 — the lattice condition, proved, and where the proof stops

Worker `w-jonathonsmac4f50-j5c79` (`claude-opus-5`), unit `J-derive-moving-kernel-with-vacancies:a2`.

**Provenance.** Both prior attempts on this problem are **mine** — `a3`
(`w-jonathonsmac4f50-jb416`) and `a4` (`w-jonathonsmac4f50-jb1d8`), same model family, machine and
running worker, both finished within the hour. Nothing here is independent confirmation of either.
I re-run neither route. `a4`'s §4 item 1 was *prove the lattice condition for `μ(A) ∝ z^{|A|}Z_A`*;
this attempt proves it, and then locates where the proof fails — which turns out to be at the menu
the unit is actually about.

## 1. What is claimed

> **Theorem (two-valued menu).** For every finite graph, every `z > 0` and every `β ≥ 0`, the
> occupation marginal `μ(A) = z^{|A|}Z_A` of the law with vacancies satisfies the FKG lattice
> condition `μ(A∪B)μ(A∩B) ≥ μ(A)μ(B)`. Consequently (with FKG) `ρ₂ ≥ ρ²`, and `a3`'s half-filling
> floor is provably removable.
>
> The proof factors into three pieces, of which **only the third carries any physics**:
>
> 1. `|A∪B| + |A∩B| = |A| + |B|` — the site count is **modular**, so the fugacity is neutral.
> 2. `E(A∩B) = E(A) ∩ E(B)` **exactly**, and `E(A) ∪ E(B) ⊆ E(A∪B)`, sometimes strictly. Hence the
>    coupling vectors satisfy `J(A∩B) = J(A) ∧ J(B)` and `J(A∪B) ≥ J(A) ∨ J(B)`.
> 3. `log Z` is increasing and **supermodular** in the couplings:
>    `∂²log Z/∂J_e∂J_f = ⟨σ_eσ_f⟩ − ⟨σ_e⟩⟨σ_f⟩ ≥ 0`. **That is exactly Griffiths' second
>    inequality (GKS-II).**
>
> Then
> `log μ(A∪B) + log μ(A∩B) ≥ log Z(J(A)∨J(B)) + log Z(J(A)∧J(B)) + (modular terms) ≥ log μ(A) + log μ(B)`.
>
> **Where it stops.** GKS-II is a theorem for the Ising model — block 36's two-valued menu — and is
> **not available for vector spins**. For the `O(3)` sphere menu this unit is actually about, the
> second Griffiths inequality is not known and is believed false in general. Pieces 1 and 2 are
> pure set combinatorics and are menu-independent; monotonicity of `Z` in the couplings holds for
> any ferromagnetic menu. So:
>
> - **two-valued menu:** `ρ₂ ≥ ρ²` is a theorem (modulo GKS-II and FKG);
> - **sphere menu:** `ρ₂ ≥ ρ²` rests on `a4`'s numerics alone, and the single missing ingredient is
>   now named.

## 2. The steps

1. **PROVED + CHECKED (`P1`).** Modularity of the count and supermodularity of the edge set, over
   **all** ordered pairs of subsets of a ring of 6 (4096) and a `3×3` torus (262144): zero
   failures of any of the three. The union inclusion is strict in general — witness on a ring of
   4, where `E(A∪B)` has 4 edges against 2 in `E(A)∪E(B)`.
2. **PROVED + CHECKED (`P2`).** The lattice statements about `J`, checked over the same pairs.
3. **ASSUMED (`P3`) — GKS-II** for the ferromagnetic Ising model, stated precisely. **CHECKED** on
   every ordered pair of edges of a ring of 5, a ring of 6 and a `2×2` torus (the last included
   because its doubled bonds are the degenerate case a naive proof would mishandle): all
   covariances non-negative, all `⟨σ_e⟩ ≥ 0`.
4. **PROVED (`P4`).** The assembly above. **CHECKED** on a ring of 5 at `z = 3/2, w = 2` — an
   instance not in `a4`'s list — over all 1024 ordered pairs, zero failures.
5. **CHECKED (`P5`), and the result was not what I expected to have to report.** How far past Ising
   does the GKS-II step survive? For a `q`-state menu (weight `w` on agreement, 1 otherwise) with
   the centred edge variable `1[agree] − 1/q`, on a ring of 5: **all edge-pair covariances are
   non-negative at `q = 2, 3, 4, 6`.** So there is no small-`q` counterexample. The obstruction for
   the sphere is the absence of a proof in the continuum, not a failure visible at finite `q` —
   which makes the sphere case look *likely true and unproved* rather than doubtful.

## 3. Where this stops

- **GKS-II is assumed, not proved**, and it is the only step with content. The whole theorem is
  conditional on it, exactly as `a4` was conditional on FKG — this attempt converts one assumption
  (the lattice condition, checked) into another (GKS-II, a standard theorem), which is progress
  only in the sense that GKS-II is a known result and the lattice condition was not.
- **FKG is still assumed** on top, to get from log-supermodularity to `ρ₂ ≥ ρ²`.
- **The sphere menu — the unit's actual subject — is not covered.** Neither `a4` nor this attempt
  establishes `ρ₂ ≥ ρ²` for `O(3)`. §5's finite-`q` evidence is suggestive and nothing more; `q`
  states with a *uniform* agreement weight is not the same family as the sphere's `e^{βs·s'}`, so
  even the evidence is only analogous.
- **Finite graphs only**, and the checks are one- and two-dimensional. The proof does not use the
  graph, so this is a limitation of the checks, not of the statement.
- This is now the third attempt on this problem by the same worker in one session. `a3` derived the
  bound, `a4` removed its floor by computation, `a2` proves what `a4` computed. **A shared error
  anywhere in that chain would propagate through all three**, and no step has been seen by another
  model family.

## 4. What would finish it

1. A GKS-II analogue for the sphere menu, or a counterexample. That single statement is what stands
   between the two-valued theorem and the unit's own menu, and §5 suggests looking for the proof
   rather than the counterexample.
2. Failing that, a route to `ρ₂ ≥ ρ²` for `O(3)` that does not go through Griffiths — the
   random-cluster/loop representation of the `O(N)` models is the natural candidate and would also
   give the lattice condition directly.
3. Check the lattice condition on a three-dimensional torus. The proof makes it unnecessary for the
   two-valued menu, but for the sphere menu it is still the only evidence there is.
4. An outside-family referee on the whole `a3 → a4 → a2` chain, for the reason in §3.

## 5. Running it

```
python3 probes/work/derive/moving-kernel-with-vacancies/w-jonathonsmac4f50-j5c79/check.py
```

Standard library only; 14 checks, exact integer and rational arithmetic throughout. The exhaustive
pair sweeps over the `3×3` torus dominate the runtime; about a minute.
