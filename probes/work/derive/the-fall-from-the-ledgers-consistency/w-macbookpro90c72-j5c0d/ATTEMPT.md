# J:derive:the-fall-from-the-ledgers-consistency:a1 — no local momentum carries the fall with weight one; its weight is ∂p̄/∂k with zero zone mean

**Provenance.** Worker `w-macbookpro90c72-j5c0d`, model `claude-opus-5-5`, one session.
- The claim printed attempt `a2` (`w-jonathonsmac4f50-j5024`, same model). I read it after planning.
- `a2` covers the task's (a)–(c) on the lattice:
  - (a) block 66 T3's exact content law, and the first-order force `e·(centred du)·cos k_j` for `π_j`;
  - (b) the curl ledger `F = Σ w_x D_x` keeps "divergence-free" for every rate field and forbids the fall; no content-blind `(e, J)` ledger reproduces `cos k_j`;
  - (c) the fall is owed only at leading order in `k`.
- I take a different route that settles `a2`'s open item 4.2 (the two-step momentum's weight) in general: **which local momentum could carry block 54's fall with weight one?** None can.

**Definitions.**
- **The walk and its clock.** `H = Σ_a σ_a D_a`, with `D_a = (i/2)(T_a − T_a†)` and `(T_aψ)(x) = ψ(x − e_a)`, so the symbol is `sin k_a` (block 54). The clocked walk is `H_w = φHφ`, with `φ = √w` and `u = log w`.
- **The momenta.** `π_j` has symbol `sin k_j` (block 63). The two-step momentum `P_j = D_jC_j`, with `C_j = (T_j + T_j†)/2`, has symbol `sin k_j cos k_j` (blocks 69, 73).
- **The quasi-momentum.** In a uniform gradient block 54 has `H_w^n T_a = λ_a^n T_a H_w^n`. So the translation eigenvalue, i.e. the quasi-momentum `k`, falls with weight one: `dk/dt = −E∇u` in every state.

## 1. Statement

**Claim F1.** Let `P` be any finite-reach, translation-invariant operator with `[P, H] = 0`, with symbol `P(k)` (a 2×2 trigonometric polynomial). Define:
- `p̄(k) = ⟨χ(k)|P(k)|χ(k)⟩`, its value on the positive band, away from the eight zeros;
- a clock with a uniform gradient, `φ = 1 + ε g·x`, so that `u = 2ε g·x + O(ε²)`.

Then for a plane wave `ψ = χ(k)e^{ik·x}` with `Hψ = Eψ`, `E = |sin k| > 0`:

`d⟨P⟩/dt (per site) = −E·∇u·∇_k p̄(k)·|χ|² + O(ε²)`.

The weight of the fall along `j` is therefore `∂p̄/∂k_j`:
- `cos k_j` for `π_j`, in agreement with `a2`'s exact local result;
- `cos 2k_j` for `P_j`;
- `(4/3)cos k_j − (1/3)cos 2k_j = 1 − k_j⁴/6 + …` for the fourth-order stencil `(4/3)D_j − (1/6)D_{2j}`.

**Claim F2 (the no-go).** On every line of the zone that avoids the eight zeros, the weight `∂p̄/∂k_j` has mean zero over `k_j ∈ (−π, π]`.
- So no local momentum commuting with the walk falls with weight one at every wave vector. Along `j`, either it never falls or it rises for some `k`.
- The exact, weight-one fall of block 54 belongs to the quasi-momentum, which is not a local density.
- Any ledger whose consistency condition demands the force `e∇u` with a weight independent of the packet's wave vector can therefore agree with a local momentum balance only asymptotically in `k`. That covers block 66's continuum identity and any rate-transporting lattice ledger.

## 2. Steps

**Step 1 (PROVED; CHECKED O.XT, S.comm_*). The commutator with a linear clock.**
- `[X_l, T_n] = n_l T_n` exactly, since `(X T_n ψ)(x) = xψ(x − n)` and `(T_n X ψ)(x) = (x − n)ψ(x − n)`.
- So for `P = Σ_n P̂_n T_n`, `i[X_l, P] = Σ_n i n_l P̂_n T_n`. Its symbol is `Σ_n i n_l P̂_n e^{−ik·n} = −∂P/∂k_l`.
- Checked on integer matrices, and on the symbols of `D` and `DC`.

**Step 2 (PROVED). First order in `ε`.**
- `H_w = H + ε(φ₁H + Hφ₁) + ε²φ₁Hφ₁`, with `φ₁ = g·x`.
- Since `[H, P] = 0`: `d⟨P⟩/dt = ⟨i[H_w, P]⟩ = ε⟨i([φ₁, P]H + H[φ₁, P])⟩ + O(ε²)`.
- For `Hψ = Eψ`, this is `2εE⟨ψ|i[φ₁, P]|ψ⟩`.
- By Step 1 the per-site value is `−2εE g·⟨χ|∇_kP|χ⟩|χ|²`.

**Step 3 (PROVED; CHECKED B.commute, B.band). The band identity `⟨χ|∂_k P|χ⟩ = ∂_k p̄`.**
- Where `s(k) ≠ 0`, `P(k)` commutes with `σ·s(k)`. So it has `χ(k)` as an eigenvector with eigenvalue `p̄(k)`.
- Differentiating `⟨χ|P|χ⟩`, the terms `⟨∂χ|P|χ⟩ + ⟨χ|P|∂χ⟩ = p̄ ∂⟨χ|χ⟩` vanish.
- Checked exactly for `P = (cos k₁ + cos k₂ cos k₃) + (1 + cos(k₁ + k₂))σ·s` at the rational point `sin k = (3/5, 4/5, 0)`: `⟨χ|∂P/∂k₁|χ⟩ = ∂p̄/∂k₁ = −28/25`.
- With `u = 2εg·x`, Steps 2 and 3 give Claim F1.

**Step 4 (PROVED; CHECKED W.pi, W.P, W.P4, W.torus). The weights of the named momenta.**

| Momentum | Symbol | Weight `∂p̄/∂k_j` | At `k_j = 0, π/2, π, 3π/2` |
|---|---|---|---|
| `π_j` | `sin k_j` | `cos k_j` | `1, 0, −1, 0` |
| `P_j` | `sin k_j cos k_j` | `cos 2k_j` | `1, −1, 1, −1` |
| fourth-order stencil | `(4/3)sin k_j − (1/6)sin 2k_j` | `1 − k_j⁴/6 + …` | `−5/3` at `k_j = π` |

- `π_j`'s value `−1` at `k_j = π` is `a2`'s reflected species.
- `P_j`'s value `−1` at `k_j = π/2` means the two-step momentum rises at `π/2`; block 72 found the lattice factor `cos 2q`.
- Better stencils push the agreement near `k = 0` to higher order. They make the far zone worse.

**Step 5 (PROVED; CHECKED W.zero_mean). Zero mean.**
- Fix the transverse wave numbers so that the line misses the eight zeros; that is, not both of them in `{0, π}`. On such a line `s(k) ≠ 0`, the band is non-degenerate, and `p̄` is `C^∞` and `2π`-periodic in `k_j`. So `∫_{−π}^{π} ∂p̄/∂k_j dk_j = p̄(π) − p̄(−π) = 0`.
- Hence `∂p̄/∂k_j ≡ 1` is impossible. If the weight is not identically zero, it is negative somewhere on the line.
- Checked for a random trigonometric polynomial, and for the band-type non-smooth `|sin k|`, which covers the lines through the zeros.

**Step 6 (PROVED). The consequence for (c).**
- A ledger's consistency condition that demands the force density `e·(lattice difference of u)` has a weight independent of the packet's wave vector. The difference acts on `u`, not on `ψ`.
- This covers:
  - block 66's continuum identity;
  - any lattice ledger in which a relabelling carries the rates along (`a2`'s open item 4.1);
  - any `(e, J)` ledger (`a2` Step 4).
- By Steps 4–5, any local momentum's actual weight is `∂p̄/∂k_j`. The two agree only in the sense `∂p̄/∂k_j = 1 + O(k^{2n})` near `k = 0`, and they disagree somewhere on every line.
- So the fall is owed by the ledger's consistency **only asymptotically in the wave number**, whatever local momentum and ledger are chosen:
  - at order `k²` for `π_j`, with weight `cos k_j = 1 − k_j²/2`;
  - at order `k⁴` for the fourth-order stencil.
- The **placement** is `a2`'s: the energy density on the site, with the centred difference of `u` at that site.
- At the exact lattice level the fall is an independent statement about the non-local quasi-momentum (block 54), not a local balance.

**ASSUMED:** plane waves and a linear clock on the infinite lattice, as the standard first-order test. The per-site statement is exact at first order in `ε`; the `O(ε²)` terms grow with `|x|`.

## 3. The first failing step

The route "a local momentum balance owes block 54's fall exactly" fails at Step 5: every local momentum's weight has zero mean on the zone. `a2`'s lattice results (the curl ledger forbids the fall; no `(e, J)` ledger gives `cos k_j`) are instances of this general obstruction.

## 4. What would finish it

1. **A rate-transporting lattice ledger** (`a2` item 4.1). By Step 6 its identity can match a local momentum only asymptotically. What remains open is which lattice placement of the transport gives agreement to the highest order, and whether that selects a stencil.
2. **A non-local clause.** A ledger that sees the quasi-momentum itself would need one, which the Lattice axiom's nearest-neighbour rule does not supply.
3. **A referee from another model family**, especially for Steps 3 and 5 on lines through the zeros. Those lines are excluded from the zero-mean statement, which covers almost every line.

## 5. Running it

```
python3 probes/work/derive/the-fall-from-the-ledgers-consistency/w-macbookpro90c72-j5c0d/check.py
```

Requires `sympy`. The run takes under 1 s. All checks are exact: integer matrices, sympy symbols, and rational trigonometric points.
