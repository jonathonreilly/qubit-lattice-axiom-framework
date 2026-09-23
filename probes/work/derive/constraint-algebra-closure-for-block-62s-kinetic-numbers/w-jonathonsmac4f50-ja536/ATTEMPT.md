# constraint-algebra-closure-for-block-62s-kinetic-numbers, attempt a2: at linear order the lattice algebra closes exactly iff β = −α

**Provenance.** Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-jonathonsmac4f50-ja536`, task
`J:derive:constraint-algebra-closure-for-block-62s-kinetic-numbers:a2`. There were no prior attempts at claim time. Block 62
(and the fork probe) were supervisor-run in the same model family, so this is not independent of them.

**What I read.** Block 62's note on its branch (the claim scope's member, the kinetic family and T4), block 63's
relabelling (`G_ξ` for the walker), block 64's claim scope, and the fork probe's gravitation lens (§5: "DeWitt's `β = −α`
and `K = 4α` … on the lattice closure may fail at `O(p²)`"). I did not read the notes of blocks 76–78 in full, and they are
not used.

## 1. What is claimed

**Setting** (block 62, supplied and not adopted; one clause added here):
- **Placement.** The strains are staggered: `h_jj` on sites, `h_ij` (`i < j`) on the faces spanned by `e_i` and `e_j`, and
  relabellings `ξ_j` on the bonds along `j`.
- **Member.** `R₁ = −(p_ip_jh_ij − p²h)` is linear in `h`. `R₂` (Fierz–Pauli) is quadratic.
- **Kinetic term.** `(1/w̄)[αḣ_ijḣ_ij + βḣ²]`. Its Legendre transform is
  `(1/4α)[Σ_j P_jj² − c(Σ_j P_jj)²] + Σ_{i<j} P_ij²/(8α)`, with `c = β/(α + 3β)`. This is the task's
  `(1/4α)(π·π − (β/(α+3β))π²)` with `π_ij = P_ij/2` off the diagonal.
- **Constraints.** `C[N]` is the per-tick energy with the clocks replaced by a lapse `N`.
- **Clause supplied here.** The unit's `w_x` lives on sites, so it leaves open how a face term is timed. I take it to be
  timed by the **mean of its four corner clocks**.
- **Generator.** The field's relabelling generator is `G[ξ] = Σ P·δ_ξh`, with `δ_ξh_ij = ∂_iξ_j + ∂_jξ_i`. It generates block
  62's relabelling of the strains. Block 63's `G_ξ` is the walker's; the two are joined in (b).

**(a) and (c): exact closure at linear order.**
- **The bracket.** The part of `{C[N], C[M]}` linear in the fields comes only from `{K R₁[N], kin[M]} − (N ↔ M)`.
- **Closure.** With `β = −α`, i.e. `c = 1/2`, it equals `G[ξ]` exactly on the lattice, with the bond field
  **`ξ_j(x → x + e_j) = (K/4α)(N_{x+e_j}M_x − N_xM_{x+e_j})`**, the lattice form of `(K/4α)(M∇N − N∇M)`.
  - This is checked in exact rationals on the `4³` torus.
  - It holds as a symbolic identity at every pair of wave vectors, so there is **no `O(p²)` obstruction** at this order.
  - The fork probe's expectation that "on the lattice closure may fail at `O(p²)`" does not hold for this placement.
- **β = −α is necessary.** The bracket is `b(1/2) + (1 − 2c)b₁`. `b₁` is isotropic on the diagonal and zero on the faces,
  and it is **not** in the span of the relabelling generators (exact rank: `189 → 190`). So closure holds iff `c = 1/2`,
  i.e. `β = −α`.
- **The clock placement matters.**
  - Timing a face term by one corner's clock breaks closure (either corner: rank `189 → 190`).
  - The mean of either pair of opposite corners gives exactly the same bracket as the four-corner mean. The general rule:
    any face timing whose symbol is real, i.e. symmetric under inversion through the face centre, of the form
    `cos(k_i/2)cos(k_j/2) + λ sin(k_i/2)sin(k_j/2)`, closes. The `λ` term cancels when the bracket is antisymmetrized.

**(b): `K/(4α)` is the structure constant.**
- The structure constant of the closed algebra is `K/(4α)`. That is block 62 T4's speed squared of the two travelling
  disturbances.
- Suppose the walker's energy density `e_x/2` is added, and its own bracket closes onto its relabelling generator with its
  speed squared, which is 1 (block 54's limiting speed). This is **ASSUMED**, not computed here.
- Then one relabelling field serves both only if **`K = 4α`**, the same cone for field and walker. That is the comparator's
  value, reached in the framework's variables.

**HIT** (the unit's criterion: "HIT if closure holds exactly on the lattice for some (α, β, K)"). At linear order it holds
exactly on the lattice for `β = −α` and every `α`, `K`, provided face terms are timed inversion-symmetrically.

## 2. Steps

1. **ASSUMED — the setting, and the one clause added.** Block 62's placement, member and kinetic family are supplied. Timing
   face terms by the four-corner mean is my addition, and step 5 examines it.

2. **PROVED / CHECKED (A4, then A1) — the bracket and the identity.**
   - Take plane-wave lapses `N = e^{ik·x}` and `M = e^{ik'·x}`, and let `q = k + k'`. Summation by parts gives
     `δR₁[N]/δh_jj = (p_k² − P_j(k)²)e^{ik·x}` and `δR₁[N]/δh_ij = −2P_i(k)P_j(k)e^{ik·f}`. The face lapse contributes
     `γ_ij(k') = cos(k'_i/2)cos(k'_j/2)`.
   - **Diagonal coefficients.** The antisymmetrized bracket has `(1/2α)[(1 − 2c)(p_k² − p_{k'}²) − (P_j(k)² − P_j(k')²)]`.
   - **Face coefficients.** It has `−(1/2α)[P_iP_j(k)γ_ij(k') − P_iP_j(k')γ_ij(k)]`.
   - **At `c = 1/2`.** The diagonal is `4 sin(q_j/2) sin((k'_j − k_j)/2)/(2α)`. That is `2·(iP_j(q))ξ̃_j` for
     `iξ̃_j = sin((k'_j − k_j)/2)/(2α)`.
   - **The face identity.** `sin(k'_i/2)sin(k'_j/2)cos(k_i/2)cos(k_j/2) − (k ↔ k') = [sin(q_i/2)sin((k'_j − k_j)/2) + sin(q_j/2)sin((k'_i − k_i)/2)]/2`.
     It makes the face part exactly `i(P_i(q)ξ̃_j + P_j(q)ξ̃_i)`, with the same `ξ̃`. (sympy)
   - **Real space.** `N_{x+e_j}M_x − N_xM_{x+e_j}` has the symbol `−2i sin((k'_j − k_j)/2)` on the bond. That gives A1's `ξ`.
   - A1 verifies the result in real space on the `4³` torus with three random integer lapse pairs and rational `α`, `K`.

3. **PROVED / CHECKED (A2) — β = −α is necessary.** `b(c)` is affine in `c`. The `(1 − 2c)` part is `(p_k² − p_{k'}²)` on
   each diagonal momentum and zero on the faces. An exact rank computation over `Q` shows it is outside the span of the
   relabelling generators.

4. **ASSUMED (B1) — the walker's structure constant.** The field's structure constant `K/(4α)` equals block 62's speed
   squared (sympy). The walker's is taken to be 1, and the lattice form of its bracket is not computed. Block 63 T4 says the
   walker's relabellings reach second neighbours, so its lattice structure need not match the field's bond placement.

5. **CHECKED (A3) — the placement.** Exact rank tests: one corner (near or far) fails, and either pair of opposite corners
   closes and equals the four-corner bracket. A4 proves the general rule symbolically, with the `λ sin sin` term.

## 3. Where the route stops

- **Only linear order is settled.** The quadratic part of the bracket, `{kin[N], K R₂[M]} − (N ↔ M)`, would have to match
  the quadratic part of the momentum constraint and the strain-dependent structure function. That needs the cubic terms of
  the energy, which are not supplied. The algebra at second order is therefore **not decided** here.
- **The walker's side (b) is ASSUMED.** The lattice bracket of the walk's energy density is not computed, and block 63
  suggests it will not share the field's exact bond structure.
- **The face timing is a clause I added.** Inversion-symmetric timings work; one-corner timings do not.

## 4. What would finish it

1. **The walker's lattice bracket.** Compute `[½{N, H}, ½{M, H}]` for `H = Σσ_aS_a` and see whether it closes onto block 63's
   `G_ξ`, and with what bond structure. That decides whether field and walker can share one exact lattice relabelling.
2. **The cubic terms.** Supply a cubic member (for example the next order of block 64's `√g R` expansion) and redo the bracket
   at quadratic order.
3. **Register the face-timing clause, or derive it.** The inversion symmetry is plausibly forced by covariance under the
   lattice's point group at the face.

## 5. Running it

```
python3 probes/work/derive/constraint-algebra-closure-for-block-62s-kinetic-numbers/w-jonathonsmac4f50-ja536/check.py
```

It needs `sympy`. It runs 5 checks (A1–A4, B1) in exact arithmetic in about 20 seconds.
