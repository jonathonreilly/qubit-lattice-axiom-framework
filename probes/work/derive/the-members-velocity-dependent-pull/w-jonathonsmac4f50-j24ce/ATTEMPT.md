# The member's velocity-dependent pull and the weight of pull-bound pairs — attempt a2

Worker `w-jonathonsmac4f50-j24ce`, model `claude-opus-5-5`.

**Provenance.**
- Block 144 (PR #9230, open), which this attempt checks, is the supervisor's own derivation, the same model family (Claude). It is not refereed by another family.
- No prior attempt was printed at claim time.
- This attempt checks block 144 by other routes. The referee should be of another family.

**Sources.**
- Block 101 as landed on main (`docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_..._2026-09-23.md`):
  - `R1 = p² tr h − p·h·p`;
  - `R2 = −(p²/4) tr(h²) + (hp)·(hp)/2 − (p·h·p) tr h/2 + p² (tr h)²/4`;
  - `L = [α tr(ḣ²) + β (tr ḣ)²]/w̄ + K w̄ (u R1 + R2) − e u`.
- At `β = −α` and `w̄ = 1`, this is block 144's position-space Lagrangian term by term: `R1 = ∂_i∂_j h_ij − ∇² tr h`, and the four terms of `R2` correspond one to one.
- The shift `N` (in `Ḣ_ij = ∂_t h_ij − ∂_iN_j − ∂_jN_i`) and the couplings `+N·P + ½Θ·h` are block 136's, as block 144 restates them. They are ASSUMED as stated there.
- Blocks 136 and 115 are closed; block 144 is read on its branch.

## 1. Statement attempted

The task's (a), (b) and (c): the member's two-body pull to order `v²`, the weight of a pull-bound pair, and the case without the shift. Each is checked against block 144's T2–T5 by routes of my own:
- **M** — the member's plane-wave equations, derived here by Euler–Lagrange from the Lagrangian and solved directly;
- **X** — the two-body Lagrangian from that exchange;
- **W** — a direct bound-state computation of the weight;
- **G** — a Poisson-bracket boost generator.

## 2. Steps

1. **CHECKED (M1) — T2, with the shift.**
   - The Euler–Lagrange equations of the Lagrangian are derived by sympy for all ten fields `(u, N, h)`, with dependence on `(t, x)` only. The wave vector along one axis is block 144's own choice, by rotation invariance.
   - At plane waves `e^{i(px − ωt)}` and `α = K/4`, a source that keeps the books (`ωe = pP_x`, `ωP_j = pΘ_xj`) gives a solvable linear system. Its solution has free (relabelling) parameters.
   - The pairing `−e′u + N·P′ + ½Θ′·h` does not depend on them. It equals `(1/(2K))[T′·T − ½T′T]/(p² − ω²)` exactly, with signature `(−, +, +, +)`.
   - Checked at three random rational `(ω, p, Θ, Θ′)`.
2. **CHECKED (M2) — T2 and T5, without the shift.** With `N ≡ 0` and no `N·P` term, a solution exists and the pairing is the same.
3. **CHECKED (M3) — T2(c).** At `α = K/3`, a moving source with `e ≠ 0` has no solution, with or without the shift.
4. **PROVED and CHECKED (X1–X3) — T3.** For slow compact bodies, `T_a = m_aγ_a(1, v_a, v_a⊗v_a)` (block 144's premise).
   - **Instantaneous part.** `T₁·T₂ − ½T₁T₂ = m₁m₂[½ + ¾(v₁² + v₂²) − 2v₁·v₂]` to order `v²` (X1).
   - **Retardation.** Expanding `1/(p² − ω²) = 1/p² + ω²/p⁴ + …`, the `ω²` between the two bodies becomes `(p·v₁)(p·v₂)`. With `FT[p_ip_j/p⁴] = ∂_i∂_j r/(8π) = (δ_ij − n_in_j)/(8πr)` (X2), this gives `(m₁m₂/2)[v₁·v₂ − (n·v₁)(n·v₂)]/(8πr)`.
     - `FT[1/p²] = 1/(4πr)` is ASSUMED, as block 144 names it.
     - `FT[1/p⁴] = −r/(8π)` is checked for consistency through `∇²(−r/(8π)) = −1/(4πr)`.
   - **Result.** `L_int = (m₁m₂/(16πKr))[1 + (3/2)(v₁² + v₂²) − (7/2)v₁·v₂ − ½(n·v₁)(n·v₂)]`: `a = 3/2`, `b = −7/2`, `c = −½` (X3). This is block 144 T3.
5. **PROVED and CHECKED (W1–W5) — T4, by a direct bound-state computation.**
   - **The Hamiltonian.** Take `H = Σ_a √(m_a² + p_a²) − (k/r)[1 + a(p₁²/m₁² + p₂²/m₂²) + b p₁·p₂/(m₁m₂) + c(n·p₁)(n·p₂)/(m₁m₂)]`, expanded to `p⁴`. It is the first-order Legendre transform of the pull, ASSUMED as a standard import.
   - **The `P²` coefficient.** With `p_{1,2} = μ_{1,2}P ± q`, the `P²` coefficient along `ê` is
     `1/(2M) − (T + 2T_P)/(2M²) + ((2a + b)U + cU_P)/M²`, exactly (W1),
     with `T = q²/(2μ)`, `T_P = (ê·q)²/(2μ)`, `U = −k/r` and `U_P = −k(n·ê)²/r`.
   - **Terms linear in `P`.** The leading kinetic term has no `P·q` term (W2). The other terms linear in `P` are of order `kv` or `v³`. Their first-order averages vanish in a bound state, and their second-order contributions are beyond first order in the binding.
   - **The directional virial.** For a stationary state, `d/dt⟨x_P q_P⟩ = 0` gives `2⟨T_P⟩ = ⟨x_P ∂_P V⟩ = −⟨U_P⟩` for `V = −k/r` (W4).
   - **The weight.** With `E₀ = M + ⟨T⟩ + ⟨U⟩`, the result to first order in the binding is `W = E₀ ∂²E/∂P² = 1 + [(1 + 2(2a + b))⟨U⟩ + (1 + 2c)⟨U_P⟩]/M` (W3). This is block 144 T4.
   - **When `W = 1` along every axis.** As the orbit turns, `⟨U_P⟩/⟨U⟩` ranges over an interval, so `W = 1` along every axis and for every bound state iff `2a + b = −½` and `c = −½`.
     - The member's `(3/2, −7/2, −½)` satisfies both.
     - The clock alone, `(0, 0, 0)`, gives `W = 1 + (⟨U⟩ + ⟨U_P⟩)/M < 1` (W5).
6. **CHECKED (G1) — why exactly those pulls.**
   - Take a centre of energy `G = Σ(m_a + p_a²/(2m_a))x_a − (k/r)(σ₁x₁ + σ₂x₂)`. The condition `{G, H} = P` at first order in `k` and in the momenta is imposed at 24 configurations and solved.
   - The unique solution family is `c = −½`, `a = −b/2 − 1/4` (that is, `2a + b = −½`), with `σ₁ = σ₂ = ½`.
   - So the pulls that give weight one along every axis are exactly those that admit a first-order boost generator of this centre-of-energy form. This confirms block 144's statement that they are "the pulls that a long-wave change of velocity leaves unchanged". The `⇒` direction is shown within the stated ansatz for `G`.
   - For comparison, the vector (Darwin) values `(0, −½, −½)` and scalar-exchange values `(−½, ½, −½)` are also in the family.

## 3. Where the route fails or stops

- Nothing in (a) or (b) fails. Block 144's T2, T3 and T4 are confirmed by the independent routes above.
- **(c) is only partly checked.** "Without the shift the pull is unchanged" is confirmed (M2). The claim that relabelling-drifting lengths act on moving content as `−ξ·P` is **not** checked here.
- **Premises that are supplied or assumed, not re-derived:**
  - the shift coupling (block 136 as restated by block 144);
  - the point form of slow compact bodies;
  - the first-order Legendre transform;
  - the two Fourier transforms `FT[1/p²]` and `FT[1/p⁴]`.
- Block 144's T1, the match to the comparator's lapse-and-shift quadratic action, is not re-checked.

## 4. What would finish it

- Check T5's drifting-lengths claim: the conserved residual of the momentum constraint, and its action on content as a fixed vector potential.
- Show that the boost-generator condition holds with a general centre-of-energy ansatz, not only the one used.
- Check block 144's T1 against the landed blocks 62 and 101 at second order.
