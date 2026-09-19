# corrigendum-PR8178: derivation attempt 1 of 2

Worker `w-jonathonsmac4f50-j9532` (claude-opus-5), unit `J-derive-corrigendum-PR8178-a1`.

**Sources**
- **Block 34:** PR #8178 at head `e6ffae5b460b` (note, runner, runner cache, `GOAL_block34.md`, `RESULTS_block34.md`).
- **Block 35:** PR #8180 at `7c844adf7555` (note, runner, control specs).
- **The search:** the notes and runners of every campaign PR for blocks 12–35 (#8146–#8158, #8168, #8170–#8180), fetched at their heads.
- **The defect report** is the task's: a probe found it and a worker of another model family confirmed it.
- No other attempt on this problem existed when I claimed it.

## 1. Statements

**(a) The corrected T1.1 (PROVED; CHECKED `C1`, `C2`)**
- Setting: on the `L × L` torus, `(Pθ)_x = (θ_x + θ_{x−e₁} + θ_{x−e₂})/3` and `θ̂_k = L^{−1} Σ_x e^{−ik·x} θ_x` with `k = 2πn/L`.
- Then `(Pθ)^_k = φ_c(k) θ̂_k`, where `φ_c(k) = (1 + e^{−ik₁} + e^{−ik₂})/3`. This is the complex conjugate of the stated `φ`.
- The stated form `(Pθ)^_k = φ(k) θ̂_k`, with `φ = (1 + e^{ik₁} + e^{ik₂})/3`, holds exactly on the modes with `sin k₁ + sin k₂ = 0`:
  - `n₁ + n₂ ≡ 0 (mod L)`, or
  - `L` even and `n₂ − n₁ ≡ L/2 (mod L)`.
- Hence it holds for every field only when `L ≤ 2`. For example, `L = 3` has 3 of 9 modes right and `L = 10` has 20 of 100.
- An equally minimal repair is to keep `φ` and change the transform to `e^{+ik·x}`. The note's other formulas are unchanged either way.

**(b) Verdicts on every later statement that uses T1.1**

| where | statement | verdict |
|---|---|---|
| block 34 | T1.2: `1 − |φ|² = (4/9)[…]` | unaffected: `|φ| = |φ_c|` (`C3`) |
| block 34 | T1.3: `θ̂_k(t+1) = φθ̂_k(t) + ξ̂_k`, the variances `σ²(1 − u^t)/(1 − u)`, the zero mode, `v_t` | the recursion holds with `φ_c`; every stated variance uses `u` only and is unaffected (`C3`) |
| block 34 | T2: tiny tori | unaffected: the recursion `Σ_{t+1} = PΣPᵀ + I` against the `u`-mode sum, which is phase-blind (`C3` re-runs it on `L = 3`) |
| block 34 | T3: `τ_L`, the rate, the bracket of `V_L`, `S_L` | unaffected (`u` only) |
| block 35 | declared objects: multiplier `φ` "(block 34)" | needs its own repair: the mode multiplier is `φ_c`, and `φ = φ̄_c` is the symbol of the kernel in block 35's convention |
| block 35 | T1: `Cov(θ̂_k(t), θ̂_k(t+s)) = φ^s Var θ̂_k(t)` and `C_s(k) = σ²φ^s/(1 − u)` | the statement holds on the corrected reading: in the convention of block 35's control, `Cov(X, Y) = E[X Ȳ]`, it is exact (`C4`: `E[θ̂(t) conj θ̂(t+s)] = φ^s Var` at every nonzero mode of `L = 3, 4`). Its proof line `θ̂_k(t+s) = φ^s θ̂_k(t) + noise` needs `φ̄ = φ_c` |
| block 35 | T1, operator form `C_s = σ²(I − PP*)^{−1}P*^s` | unaffected (convention-free) |
| block 35 | T2: `1 − u = kᵀMk + O(k⁴)`, the order-six symmetry | unaffected (`u` only) |
| block 35 | T3: `|φ|^s ≤ e^{−2|k|²s/(9π²)}` | unaffected (modulus) |
| block 35 | T3: the drift `φ = 1 + i(k₁ + k₂)/3 + O(k²)` | holds for `φ` as the kernel symbol, which is what the note and the `D1` code state. The runner docstring (line 13) and comment (line 232) state `1 − i(k₁ + k₂)/3`, which is `φ_c`'s expansion (`C5`). Needs its own one-line repair |
| block 35 | executed comparison `C_s(k)` against `φ^s` | consistent: the control accumulates `E[f(k, t−s) conj f(k, t)]` with numpy's `e^{−ik·x}` FFT, and that equals `φ^s S₀` |
| block 13 (#8147) | the difference walk's characteristic function `|φ(k)|²`, `φ = (1 + e^{ik₁} + e^{ik₂})/3`, giving `P_n = (2π)^{−2}∫|φ|^{2n}` | unaffected: only `|φ|²` enters |
| block 26 (#8170) | `φ(θ) = (1 + e^{−iθ₁} + e^{−iθ₂})/3` for steps `(0,0), (−1,0), (0,−1)`, `p_k(y) = (2π)^{−2}∫φ^k e^{−iθ·y}` | unaffected, and already in the corrected form: block 34's T1.1 disagreed with its parent |
| blocks 19–23, 29 (#8153–#8157, #8173) | static-law transforms `ŝ(k) = N^{−1/2}Σ e^{ik·x}s_x` | unrelated object (real symmetric operators), unaffected |
| block 22 (#8156) | `φ(k) = (1/3)Σcos k_j` | real, unrelated |
| blocks 31–33 (#8175–#8177) | "T1.1" | different theorems (tree lemmas), unrelated |
| #8179 and the other campaign PRs | — | no use of the multiplier or of block 34's T1.1 |

Outside the task's scope: the library docstring `probes/lib/formation_levelplane.py` writes the backward stencil's `φ` with `e^{+ik}` and uses numpy's FFT. Its estimator uses only `|φ|²`.

**(c) The exact lines that must change (`C6` verifies the quoted strings at the pinned heads)**

Block 34 (#8178):
- The note:
  - line 4 (claim scope): `multiplier phi(k) = (1 + e^{i k_1} + e^{i k_2})/3` → `(1 + e^{-i k_1} + e^{-i k_2})/3`;
  - line 85: `P acts as multiplication by φ(k) = (1 + e^{ik₁} + e^{ik₂})/3` → `(1 + e^{−ik₁} + e^{−ik₂})/3`;
  - line 104 (T1.1): the same formula. The proof's "each shift multiplies `θ̂_k` by `e^{−ik·e}`; the conjugate convention gives the stated `φ`" → "each shift `θ ↦ θ_{·−e}` multiplies `θ̂_k` by `e^{−ik·e}`, so `φ(k) = (1 + e^{−ik₁} + e^{−ik₂})/3`".
- The runner:
  - line 5 (docstring): the same formula;
  - line 199: `sp.exp(sp.I * k1)`, `sp.exp(sp.I * k2)` → `sp.exp(-sp.I * k1)`, `sp.exp(-sp.I * k2)`. B1's verdict is unchanged, because it checks `|φ|²`;
  - line 206: B1's text, the same formula;
  - suggested: a check of the diagonalization itself (`C1`'s construction), since every current check is blind to the phase.
- The runner cache, line 18: B1's text, regenerated.
- `GOAL_block34.md` line 6 and `RESULTS_block34.md` line 6: the same formula.

Block 35 (#8180):
- The note:
  - line 86: multiplier `φ_c(k) = (1 + e^{−ik₁} + e^{−ik₂})/3` (block 34, corrected), and `φ := φ̄_c` is the symbol of `C_s`;
  - line 87: make the convention explicit, `C_s(k) := E[θ̂_k(t) \overline{θ̂_k(t+s)}]`;
  - line 106 (T1 proof): `θ̂_k(t+s) = φ̄^s θ̂_k(t) + (noise)`, so the stated covariance is `φ^s Var`.
- The runner:
  - line 13 (docstring): `phi(k) = 1 - i(k1 + k2)/3` → `1 + i(k1 + k2)/3`, to agree with line 234's code, D1's text and the note's line 116;
  - line 232 (comment): likewise.

## 2. Steps

**S1 (PROVED; CHECKED `C1`). The multiplier.**
- `Σ_x e^{−ik·x} θ_{x−e} = Σ_y e^{−ik·(y+e)} θ_y = e^{−ik·e} L θ̂_k`, so `(Pθ)^_k = (1 + e^{−ik₁} + e^{−ik₂})θ̂_k/3`.
- `C1` builds `F` and `P` on `L = 2, 3, 4, 5` in `Q(ζ_L)`, testing zero modulo the cyclotomic polynomial, and verifies `(FP)_{k,y} = φ_c(k)F_{k,y}` at every mode and site.
- With the stated `φ`, `C1` finds 54, 160 and 500 failing (mode, site) pairs on `L = 3, 4, 5`, and none on `L = 2`.

**S2 (PROVED; CHECKED `C2`). The domain.**
- `φ − φ_c = (2i/3)(sin k₁ + sin k₂) = (4i/3) sin((k₁+k₂)/2) cos((k₁−k₂)/2)`. This vanishes iff `k₁ + k₂ ∈ 2πZ` or `k₁ − k₂ ∈ π + 2πZ`.
- On the torus this is `n₁ + n₂ ≡ 0`, or `n₂ − n₁ ≡ L/2` for even `L`. `C2` checks it exactly for `L = 2..10`.
- A field supported on one failing mode shows that the stated identity fails for every `L ≥ 3`.

**S3 (PROVED; CHECKED `C3`). Block 34's other statements use `u = |φ|² = φφ̄`,** which is invariant under conjugation. The mode recursion is linear, so the variance recursion `V(t+1) = uV(t) + σ²` is phase-blind.

**S4 (PROVED; CHECKED `C4`). Block 35's covariance.**
- From the recursion with `φ_c`: `E[θ̂(t) \overline{θ̂(t+s)}] = \overline{φ_c}^s Var = φ^s Var`, and `E[\overline{θ̂(t)} θ̂(t+s)] = φ_c^s Var`.
- `C4` verifies both exactly from the covariance matrices on `L = 3, 4`.
- Block 35's control uses the first convention, so its formulas and its executed comparison are consistent. Only the proof line and the name "multiplier" are wrong.

**S5 (CHECKED `C5`). The drift signs.**

**S6 (search).**
- `C6` pins the quoted lines.
- The search `git grep` covered every note, runner and `RESULTS_block*.md` touched by the 25 campaign PRs. The patterns were `e^{±ik`, `exp(sp.I`, `exp(1j`, `φ(k)`, `phi(k)`, `block 34`, `#8178` and `T1.1`.
- Every hit is classified in (b).

## 3. Where the route stops

It does not stop: (a)–(c) are complete within the search above.

## 4. What would finish it

The supervisor applies the line changes in (c) and adds a phase-sensitive check, such as `C1`'s diagonalization, to block 34's runner.
