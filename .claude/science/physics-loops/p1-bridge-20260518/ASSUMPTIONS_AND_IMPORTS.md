# P1-Bridge Loop — Assumption & Import Ledger

## Framework axioms (A_min, per `MINIMAL_AXIOMS_2026-05-03.md`)

- **A1** — `Cl(3)` local algebra per site
- **A2** — `Z^3` spatial substrate
- **A3** — Hermitian Hamiltonian / finite Grassmann partition
- **A4** — Canonical normalization (`g_bare = 1`, `β = 6`, etc.)

The no-new-axiom rule applies: no extension to this axiom stack is
allowed under physics-loop work.

## P1 admitted premise (the target of this loop)

> **P1** (scalar additivity on independent subsystems).
> For two independent subsystems with `D = D_1 ⊕ D_2`, the
> physical scalar bosonic observable generator `W` satisfies
> `W[J_1 ⊕ J_2] = W[J_1] + W[J_2]`.

P1 is the **classification choice** that selects `W = c · log|Z|` from
the family `F_p[J] = |Z[J]|^p`. Without P1, the selection between
`p = 0` (`log`) and `p ≠ 0` (`(·)^p`) is ambiguous.

## P2/P3/P4 (runner-local consequences, not load-bearing for P1)

- **P2** — CPT-even phase blindness: runner-local consequence of
  `CPT_EXACT_NOTE` algebra (currently `audited_conditional`).
- **P3** — Continuity / minimal regularity: runner-local consequence
  of finite-block regularity (no additional admission needed
  on the exact minimal hierarchy block).
- **P4** — Normalization choice up to overall constant: runner-local
  consequence; the conventional choice is `c = 1`, which fixes
  the constant in `W = c log|Z|`.

## Retained framework primitives available

Per `docs/audit/data/audit_ledger.json` snapshot 2026-05-18:

| Primitive | Status | Constrains | Excludes `F_p` for `p ≠ 0`? |
|---|---|---|---|
| `cl3_color_automorphism_theorem` | retained_bounded | rep theory | No — orthogonal to scalar functional |
| `graph_first_su3_integration_note` | retained_bounded | gauge axis selection | No — orthogonal |
| `native_gauge_closure_note` | retained_bounded | gauge closure | No — orthogonal |
| `cpt_exact_note` | audited_conditional (now unaudited post-PR-#1526) | CPT-even (P2) on phase blindness | No — `F_p` is CPT-even for all `p` |
| `axiom_first_reflection_positivity_theorem_note_2026-04-29` | unaudited | measure positivity | No — `F_p > 0` for all `p` on real-D blocks |
| `anomaly_forces_time_theorem` | unaudited | gauge content + spacetime signature | No — orthogonal |
| `cluster_decomposition_mass_gap_bridge_theorem_note_2026-05-09` | retained_bounded | temporal clustering given `Δ_T > 0` | No — orthogonal to functional admissibility |

None of the retained primitives independently excludes `F_p` for
`p ≠ 0`. This is the load-bearing observation of the Route D no-go.

## The universal counterexample family

```
F_p[J] := r(J)^p,   r(J) := |Z[J]| > 0,   p ∈ R \ {0}
```

Properties of `F_p`:
- Continuous (composition of continuous functions): ✓
- CPT-even (depends only on `|Z|`): ✓
- Positive (`r > 0`): ✓
- Multiplicatively factorizing on independent subsystems:
  `F_p[J_A ⊕ J_B] = (r_A · r_B)^p = r_A^p · r_B^p = F_p[J_A] · F_p[J_B]`
- **Not additive** for `p ≠ 0`: `(r_A · r_B)^p ≠ r_A^p + r_B^p`
  generically.

`F_p` is therefore compatible with every retained framework primitive
in `A_RETAINED` AND with every standard mathematical scaffold in
`S_STD` enumerated below. Excluding `F_p` requires a NEW classification
mechanism not currently in the framework.

## Standard mathematical scaffolds (S_STD, per Route D)

- **S_OA** — operator-algebraic: Hilbert tensor product factorization,
  Grassmann determinant block factorization, type II_1 trace-state
  factorization, Reeh-Schlieder cyclicity, cluster decomposition.
- **S_IT** — information-theoretic: Shannon-Khinchin-Aczel-Daroczy
  classification, Cauchy logarithm functional equation.
- **S_FI** — framework-internal retained primitives: reflection
  positivity, anomaly-forces-time, CL3 color automorphism, gauge
  closure, generation algebra, scale-invariance, max-entropy
  obstruction.
- **S_CD** — cross-disciplinary categorical/topological/tropical:
  Atiyah-Singer index, K-theory / Euler characteristic, homology
  direct sum, Cramer rate function, tropical max-plus, geometric
  quantization, Legendre / free energy, synthetic differential
  geometry, Tarski first-order, Tao functional-equation classifier.

## Counterfactual pass

For each implicit framework choice, "what if this were different,
what direction does the alternative open?"

| Implicit choice | Alternative | Direction opened |
|---|---|---|
| Scalar observable generator = `log|Z|` | `log|Z|^p` | Already Route A/B/C/D obstruction |
| Local source response is local (only depends on data near `x`) | Source response carries global `|Z|^{p-1}` factor | This IS extensive ⇔ additive: equivalent to P1 (Pattern L circularity D5) |
| Physical scalar observables are extensive | Physical observables can be intensive (multiplicative) | Choice between extensive/intensive IS P1; just relabeling |
| `Cl(3)` ⊗ `Z^3` substrate | Different fibre algebra | Doesn't affect scalar functional admissibility |
| Lattice action structure | Continuum field theory | The continuum reduction inherits the same multiplicative `Z[J] = Z_A · Z_B` structure |

The counterfactual pass surfaces no orthogonal premise that escapes
Pattern L circularity. **All routes that try to select `log` over
`(·)^p` either invoke `log` explicitly (Pattern L = D5) or require
an additive-class hypothesis (Pattern A = D2, restating P1).**

## Honest assessment

The P1 derivation lane is structurally foreclosed against the four
standard scaffold families and the framework's current retained
primitives. The legitimate forward path is **Path (b)** of the Route
D no-go: accept P1 as a permanent classification admission.

Adopting Path (b) is the campaign-mode honest outcome here. It does
NOT downgrade the framework — it explicitly documents the
classification choice as a physical-principle premise and ships
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE` at its honest
`audited_conditional` status with P1 admitted indefinitely, with
rigorous structural backing via Route D.
