# The zero-field floor sharpened, attempt 1: a floor linear in M², exact at β = 0

Worker `w-macbookpro9927a-ja8d2` (`claude-opus-5-5`), unit `J-derive-the-zero-field-floor-sharpened-a1`.

**Provenance.**
- **What I read.** Block 92 on its PR branch (head `3e26092f3c`), for T1–T3 and the corrigendum on the clause. Blocks 90 and 91 enter only through block 92's statements of them: the bilayer, the sum rule `M² ≥ 1 − β_L/β`, and the response `R̂ = βu`.
- **My plan, formed before reading the prior attempt.** Keep block 92's Bogoliubov inequality, but put a weight inside its Cauchy–Schwarz step. The extra term of the second integration by parts can then be computed exactly.
- **The prior attempt.** a2 (`w-jonathonsmac4f50-je12b`, same model family, no HIT, unrefereed):
  - reached `4(M²/3)²` with `F = (m × A)₂`;
  - reduced the linear bound to an unproved correlation inequality (C);
  - noted that "weighting the measure by `|m|²` breaks the integration by parts".
- **What is a2's and what is mine.** This attempt uses a2's `F = (m × A)₂` (credited). The weighted step and its exact cross term are mine. They make both `F` choices linear in `M²`, with no correlation inequality.
- **Related prior work of mine.** An earlier session on this machine did `the-small-k-limit-of-the-held-source-response` a2 (#8837), the field version of block 91's Bogoliubov step. It is not used here.
- Blocks 19, 20 and 90–92 are the same model family. A referee from another family is owed.

## 1. What is attempted

**Setting (block 92, block 90's bilayer).**
- The model is the sphere ferromagnet `∏_edges e^{β s_u·s_v}` on two copies of `(Z/L)^d`, with nearest-neighbour bonds and one rung per site, at zero field. `V = 2N` vertices, `N = L^d`.
- `c_u = e^{ik·x_u}`, and `L_u` rotates `s_u` about `e₂` (`L s = e₂ × s = (s³, 0, −s¹)`). `D = Σ_u c_u L_u` and `D̄ = Σ_u c̄_u L_u`.
- `A = Σ_u c̄_u s_u` (a complex 3-vector), `m = V⁻¹Σ_u s_u`, `M² = ⟨|m|²⟩`, and `u(k) = V⁻¹⟨|A₁|²⟩`.
- `E(k) = Σ_j(2 − 2cos k_j)`, and `H = Σ_edges s_u·s_v`.
- The clause behind the bilayer carries block 92's corrigendum. Nothing is adopted.

**Theorem 1.** For every finite `L`, every `β ≥ 0`, every `k ≠ 0` and any rung coupling:

  `u(k) ≥ (4/9) M² / (βE(k) + 4/(3V))`.

- It is linear in `M²`. It is an **equality at `β = 0`** for every `V`.
- With block 92's own `F`, the same route gives `u(k) ≥ (M²/3)/(βE(k) + 1/V)`.
- Block 92's floor is `(M²/3)²/(βE + 2/(3V))`.

**Corollary 2 (3+1).** With `R̂ = βu` (block 91 via block 92) and `M² ≥ 1 − β_L/β` (block 90), in every finite volume and for `β > β_L`:

  `(4/9)(1 − β_L/β)/(E(k) + 4/(3βV)) ≤ R̂(k) ≤ 1/E(k)`.

- In the limit, `E(k)R̂(k) ≥ (4/9)(1 − β₀/β)`. At `β = 1, 2, 3, 6` that is `0.182, 0.313, 0.357, 0.401`.
- Block 92 had `0.019, 0.055, 0.072, 0.090`, with limit `1/9`. This floor's limit is `4/9`. Block 91 measures about `0.95`.

**Corollary 3 (planes).**
- In 2+1, `M² ≤ (3/2)(π²β + 1/6)/H_{L/2−1}`. With block 92's staggered term, `⟨|m₀|²⟩ ≤ M² + 3/(20βN)`.
- Block 92 had `M⁴ ≤ (6π²β + 1/2)/H`. The bound now decays like `1/log L`, not `1/√(log L)`. It falls below 1 from `L = 124` at `β = 0.3`.

## 2. The steps

1. **PROVED: integration by parts.**
   - Each `L_u` is a divergence-free vector field on its sphere, so `∫ L_uψ dσ = 0`. For `D` with complex coefficients, `∫ D(G e^{βH}) dσ = 0` gives

     `⟨DG⟩ = −β⟨G·DH⟩`   for every smooth `G`.   (IP)

   - Since `H` is real, `D̄H = conj(DH)`.

2. **PROVED + CHECKED (S1): the derivation identities.** From `Ls = (s³, 0, −s¹)` and `|c_u| = 1`:
   - `DA₁ = Vm₃`, `DA₃ = −Vm₁`, `DA₂ = 0`;
   - `Dm₃ = −Ā₁/V`, `Dm₁ = Ā₃/V`, `Dm₂ = 0`.
   - Hence, for `F := (m × A)₂ = A₁m₃ − A₃m₁`:
     - `DF = V(m₁² + m₃²) − (|A₁|² + |A₃|²)/V`;
     - for `w := |m|²`, `D̄w = −2F/V`.
   - Also `DH = Σ_edges (c_u − c_v)(e₂ × s_u)·s_v`, and

     `D̄DH = −Σ_edges |c_u − c_v|² (s_u⊥·s_v⊥)`,

     where `⊥` means the components orthogonal to `e₂`. The rungs join equal phases and drop out.
   - All of these are checked as polynomial identities on a symbolic six-vertex bilayer with unit rational phases.

3. **PROVED + CHECKED (R1): rotation averages.**
   - At zero field the joint law of `(m, A)` is invariant under global rotations. So `E[YY†]` is a rotation-invariant hermitian form for any covariant `Y`, and by Schur's lemma it equals `(E|Y|²/3)·I`.
   - Hence `⟨m₁²⟩ = ⟨m₃²⟩ = M²/3` and `⟨|A_i|²⟩ = Vu` for each `i`.
   - It also gives `E|(n × A)₂|² = E|n × A|²/3`, with `n = m/|m|`.
   - Checked: the average over the 24 cube rotations of `(Ry)(Ry)†` is `(|y|²/3)I` for symbolic complex `y`.

4. **PROVED: the weighted Cauchy–Schwarz inequality.**
   - By (IP), `⟨DF⟩ = −β⟨F·DH⟩`. Split `F·DH = (F/|m|)(|m|DH)` (the set `m = 0` is null, and `|F|/|m| ≤ |A|` is bounded). Then

     `|⟨DF⟩|² ≤ β² ⟨|F|²/w⟩ ⟨w|DH|²⟩`.   (CS)

   - **First factor.** `|F|²/w = |(n × A)₂|²`, so `⟨|F|²/w⟩ = E|n × A|²/3 ≤ E|A|²/3 = Vu`. This uses `|n × A|² = |A|² − |n·A|²` (S1) and step 3.
   - **Second factor, by (IP) with `G = w·DH` and `D̄`:**

     `⟨w|DH|²⟩ = −β⁻¹⟨D̄(w DH)⟩ = −β⁻¹⟨(D̄w)DH⟩ + β⁻¹⟨w(−D̄DH)⟩`.

   - **The cross term is exact.** By step 2, `(D̄w)DH = −(2/V)F·DH`. By (IP), `⟨F·DH⟩ = −β⁻¹⟨DF⟩`. So `⟨(D̄w)DH⟩ = (2/(βV))⟨DF⟩`.

     This is the step a2 found blocked. Nothing needs to be conditioned on `|m|`: the derivative of the weight is again the derivative of `F`.
   - **The remaining term.** By step 2, `−D̄DH ≤ Σ_edges|c_u − c_v|² = VE(k)` pointwise. So `⟨w(−D̄DH)⟩ ≤ VE⟨w⟩ = VE·M²`.
   - **Together.** `⟨w|DH|²⟩ ≤ β⁻¹VEM² − (2/(β²V))⟨DF⟩`.
   - This upper bound is automatically `≥ 0`, because the left side is. So the product of the two factor bounds is legitimate.

5. **PROVED + CHECKED (A1): the algebra.**
   - Put `a = M²/3` and `X = ⟨DF⟩`. By steps 2 and 3, `X = 2(Va − u)`.
   - Then (CS) gives `X² ≤ β²(Vu)(β⁻¹VE·3a − 2X/(β²V)) = 3βV²Eau − 2uX`.
   - Since `X² + 2uX = X(X + 2u) = 4Va(Va − u)`, this is `4Va(Va − u) ≤ 3βV²Eau`.
   - For `a > 0` (the claim is trivial at `a = 0`) it is `u(3βVE + 4) ≥ 4Va`, that is `u ≥ (4/9)M²/(βE + 4/(3V))`.
   - **Block 92's `F`.** With `F = A₁m₃` and `w = m₃²`, the same steps give `D̄w = −2F/V`, `⟨|F|²/w⟩ = ⟨|A₁|²⟩ = Vu`, `⟨w⟩ = a` and `X = Va − u`. The result is `u² + βV²Eau − V²a² ≥ 0`, whose positive root exceeds `a/(βE + 1/V)` because `√(b² + 4) ≤ b + 2`.
   - Checked symbolically.

6. **PROVED + CHECKED (Z1): equality at `β = 0`.**
   - The spins are independent and uniform: `⟨s^i_u s^j_v⟩ = δ_uv δ_ij/3`.
   - So `u = V⁻¹Σ_u|c_u|²/3 = 1/3` and `M² = 1/V`, and the floor is `(4/9)(1/V)/(4/(3V)) = 1/3`.
   - So the ratio of the two constants, `(4/9)/(4/3) = 1/3`, cannot be raised by any bound of this shape. Block 92's floor at `β = 0` is `1/(6V)`.

7. **PROVED + CHECKED (P1): the corollaries.**
   - **3+1.** Corollary 2 follows from Theorem 1, `R̂ = βu`, and the floor increasing in `M²`.
   - **Planes, the shell count.**
     - `Σ_{k≠0}|k|⁻² ≥ (N/π²)H_{L/2−1}`: the shell `max|n_i| = r` has `8r` points with `|n|² ≤ 2r²`, and `k = 2πn/L`. It is checked exactly for even `L = 4..24`.
     - `E ≤ |k|²`, and `4/(3V) = 2/(3L²) ≤ |k|²/(6π²)` because `|k| ≥ 2π/L`.
   - **Planes, the bound.** The sum rule `Σ_k u(k) ≤ V/3` (block 92) against Theorem 1 gives `(4/9)M²(N/π²)H/(β + 1/(6π²)) ≤ 2N/3`, that is `M² ≤ (3/2)(π²β + 1/6)/H_{L/2−1}`.
   - The algebra is checked symbolically, and the threshold `L` is computed with `π² < 98697/10000` and exact harmonic numbers.

8. **CHECKED, executed, floating point (M1): not a proof.** A heat-bath Monte Carlo on block 90's bilayer, 500 sweeps:
   - `d = 3`, `L = 4`, `β = 1`: `u = 0.347`, `M² = 0.63`. New floor `0.139`, block 92's `0.022`.
   - `d = 2`, `L = 8`, `β = 1`: `u = 1.29`, `M² = 0.32`. New floor `0.235`, block 92's `0.019`.

9. **ASSUMED.**
   - Block 90's bilayer and sum rule `M² ≥ 1 − β_L/β`.
   - Block 91's identity `R̂ = βu`, used only in Corollary 2.
   - Block 92's sum rule `Σ_k u(k) ≤ V/3` and staggered term, used only in Corollary 3.
   - `β₀ = 0.5905` as block 90 states it.
   - Theorem 1 itself uses none of these. It holds on any finite graph for the zero-field `O(3)` ferromagnet, with unit phases `c_u` and `E` replaced by `V⁻¹Σ_edges|c_u − c_v|²`.

## 3. Where it stops

- **(a) is met.** The bound is linear in `M²` and unconditional, at zero field and in every finite volume.
- **(b) is partly met.**
  - The coefficient in front of `βE` is `4/9`.
  - At `β = 0` the bound is an equality, so the ratio `c/d` of a floor `cM²/(βE + d/V)` is best possible at `1/3`.
  - Whether `c = 4/9` is best is not shown. The loss is located in step 4's pointwise stiffness bound `s⊥·s⊥ ≤ 1`.
    - In an ordered, spin-wave regime the weighted average of `s⊥·s⊥` is near `2/3`, not 1. That would give `c` near `2/3`.
    - A Goldstone heuristic gives `u ≈ (2/3)M²/(βρE)`, with stiffness `ρ ≤ 1`.
    - These are heuristics, not claims.

## 4. What would finish it

1. **A weighted stiffness bound.** Something like `⟨|m|²(−D̄DH)⟩ ≤ VE(⟨|m|²(1 − n₂²)⟩ + small)`, which would raise `4/9` toward `2/3`. Alternatively, a matching example showing `4/9` is best.
2. **A referee from another model family,** line by line: especially step 4's cross term and the sign conventions in (IP).
3. **The same weighted route for other members of blocks 19–20's family.** For example, the static law's window (block 19), where block 20's argument originated.

## 5. Running it

```
python3 probes/work/derive/the-zero-field-floor-sharpened/w-macbookpro9927a-ja8d2/check.py
```

- Seven checks. S, R, A, Z and P are exact (`sympy`, `fractions`); M is a floating control.
- It runs in about 5 seconds.
