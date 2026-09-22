# a-bond-placed-stress-for-the-walk, attempt 3 of 3: momentum is conserved on the bonds, but a metric member's condition fails by the bond torque

Worker `w-jonathonsmac4f50-j1518` (`claude-opus-5-5`), unit `J-derive-a-bond-placed-stress-for-the-walk:a3`.

**Provenance.**
- No attempt of this problem had been delivered: attempts a1 and a2 left nothing on `ai/probes`.
- I read block 62 (PR #8592) on its branch, and the axioms memo in full (`docs/MINIMAL_AXIOMS_2026-06-29.md`, on `main`).
- I planned (a) before reading anything further, deriving the current from `[S_j, H] = 0`.
- Then I read blocks 63, 64 and 65 (PRs #8593, #8595, #8596). They are later blocks of the same campaign: same model family as me, unrefereed, and not named in the task.
  - Block 63 T1 has the same current as my derivation, term for term.
  - Block 63 T2/T4 and block 64 T1 give the coupling `H[B]` and its response.
  - Block 64 T5 has the site-wise bond torque, and block 65 the coin-rotation law.
- This attempt re-checks those pieces with its own exact machinery. It is not a referee of them: same family.
- It adds:
  - (b)'s theorem that `H[B]²` is not a metric;
  - (c)'s rewrite and decision, with a closed form and a no-go for re-weighting;
  - (d)'s pairing form of the obstruction, and the exact statement that a coin-rotation law cannot absorb it.

## 1. What is claimed

**Setting.**
- The walk is block 54's, identity frame: `H = Σ_a σ_a S_a`, with `S_a = (T_a − T_a†)/(2i)`, `(T_aψ)(x) = ψ(x + e_a)` and `i ψ̇ = Hψ`.
- The momentum density is `π_j(x) = Re ψ†(x)(S_jψ)(x)`.
- `d_a f(x) = f(x+e_a) − f(x)`, and `back_a f(x) = f(x) − f(x−e_a)`.
- `C_a[v]` is the symmetric hop along `a` weighted by a bond function `v`:
  `(C_a[v]f)(x) = ½[v(x) f(x+e_a) + v(x−e_a) f(x−e_a)]`.
- A **bond strain** `B_a^j(x)` sits on the bond `x → x+e_a`.
- The **bond torque** is `τ_aj(x) = J_a^j(x) − J_j^a(x)`.

> **(a) Conservation (exact, every state, every torus).**
> `∂_t π_j(x) + Σ_a back_a J_a^j(x) = 0`, where
> `J_a^j(x → x+e_a) = ½ Re[ψ†(x+e_a) σ_a (S_jψ)(x) + (S_jψ)†(x+e_a) σ_a ψ(x)]`.
> `J_a^j(x)` depends on `ψ(x + e_a ± e_j)`, which are second neighbours.
>
> **(b) The coupling whose response is `J`.**
> - `H[B] = H + Σ_{a,j} σ_a ½{C_a[B_a^j], S_j}` is hermitian, and `∂⟨H[B]⟩/∂B_a^j(x) = J_a^j(x)` exactly.
> - It reaches second neighbours (block 63 T4).
> - For a uniform strain, `H[B](k) = Σ_a σ_a V_a` with `V_a = s_a + c_a(Bs)_a` (`s = sin k`, `c = cos k`), and
>   `H[B]² = |V|²`.
> - The reflection `k_a → π − k_a` keeps `s` and flips `c_a`, and it changes `|V|²` by exactly `4 s_a c_a (Bs)_a`.
> - **So `H[B]²` is a function of `sin k` alone — a metric form `g^{ij} s_i s_j`, block 62 T1 — only for `B = 0`.** The bond
>   placement buys exact conservation with block 62's exact metric; the metric form survives only at long wavelength, where
>   `c → 1`.
>
> **(c) The member placed to match, and the decision.**
> - *Rewrite.* Put displacements `ξ` on sites and the symmetric strain at each site from its three forward bonds:
>   `h_ij(x) = −(B_i^j(x) + B_j^i(x))`.
>   - A relabelling moves `h` by forward differences, `δh_ij = −(d_iξ_j + d_jξ_i)`.
>   - Translate `h_ij` by `(e_i + e_j)/2` and `ξ_j` by `e_j/2`. This turns the relabelling into block 62's `i(p_iη_j + p_jη_i)`.
>   - So the member is **block 62's own `R_1`, `R_2` of the translated `h`**. The symbols `p_j = 2 sin(k_j/2)` are unchanged, and
>     relabelling invariance is exact.
> - *Decision.* In the symmetric gauge at each site (`B_i^j = B_j^i = −h_ij/2`), T5's condition reads
>   `Σ_a back_a J_(aj) = 0`. By (a), on stationary states this equals `½ Σ_a back_a J_j^a = −½ Σ_a back_a τ_aj`.
> - **It is not met.** The state `ψ = e^{iπx₁/2}(1,1) + e^{iπx₂/2}(1,i)` on the 4³ torus has `Hψ = ψ` exactly. Its current is
>   conserved at every site, but its transposed divergence `Σ_a back_a J_j^a` takes the values `±2`.
> - *Every pair of plane waves.* Take `ψ = χe^{ik·x} + χ'e^{ik'·x}` with `q = k − k'` and `k̄ = (k+k')/2`. Then
>   `J_a^j = const + Re[(s_j + s'_j) A_a M_a e^{iq·x}]`, where `A_a = (e^{ik_a} + e^{−ik'_a})/2` and `M_a = χ'†σ_aχ`. At equal
>   energy the transposed divergence is
>   `Re[2i e^{iq·x} A_j M_j Σ_a sin q_a sin k̄_a (cos(q_a/2) − cos k̄_a − i sin(q_a/2))]`.
>   This is third order in the wave numbers, with leading term `Re[e^{iq·x} A_j M_j Σ_a q_a² k̄_a]`: the order of block 62's site
>   defect.
> - *No re-weighting helps.* At `q = (0, 3π/2, π/2)` on the 4³ torus, energy 1, the pairs of the shell force every
>   translation-invariant weight on the transposed current to vanish.
>
> **(d) What obstructs, and what absorbs it.**
> - For a member of `h` alone, with any realisation `B = Rh` (`ΛR = 1`, `Λ` the symmetric part), the condition on stationary
>   states is `⟨J, (1 − RΛ) Dξ⟩ = 0` for every `ξ`. That is the pairing of `J` with the **rotational part of every relabelling
>   strain**; in the site gauge it is the bond-torque pairing.
> - A member of the **full nine-component strain** that relabellings leave unchanged (for instance, any function of the
>   plaquette curls, block 64) has the condition `⟨J, Dξ⟩ = 0`. That is exactly (a). Its three rotations are field variables,
>   sourced by `τ`.
> - A **law for the rotation of the coin axes** (block 65's) cannot absorb it. Its response is `½ d(ψ†σψ)/dt` for every state,
>   zero on stationary states, while the torque pairing is not zero.
> - **The axioms memo has neither object.** It supplies `Z³` with adjacency, translations and proper cubic rotations, and
>   `M_2(C)` at each site. It supplies no frame, bond strain, rotation field, transport of the qubit between sites, or dynamics.

## 2. The steps

1. **PROVED + CHECKED (A1): conservation.**
   - Put `φ = S_jψ`. Since `[S_j, H] = 0`, `φ̇ = −iHφ`, so `∂_tπ_j = Im[ψ†(Hφ) − (Hψ)†φ](x)`.
   - Use `(Hφ)(x) = Σ_a σ_a(φ(x+e_a) − φ(x−e_a))/(2i)`, `Im(z/(2i)) = −½Re z` and `Im(z/(−2i)) = ½Re z`. Then
     `∂_tπ_j(x) = −½Σ_a Re[ψ†(x)σ_aφ(x+e_a) + ψ†(x+e_a)σ_aφ(x)] + ½Σ_a Re[ψ†(x)σ_aφ(x−e_a) + ψ†(x−e_a)σ_aφ(x)]`.
   - That is `−Σ_a back_a J_a^j`, with `J` written as above, after conjugating one term inside `Re`.
   - Checked exactly at all 60 sites of a 3×4×5 torus, for a random Gaussian-integer state (not stationary), `j = 1, 2, 3`.
     The dependence on `ψ(x + e₁ + e₂)` is checked too.
2. **PROVED + CHECKED (B1): the response.**
   - `C_a[v]` (real `v`), `S_j` and `σ_a` are hermitian, and `σ_a` commutes with the lattice operators, so each term of `H[B]`
     is hermitian.
   - `⟨ψ|σ_a ½{C_a[v], S_j}|ψ⟩ = Re⟨ψ|σ_a C_a[v] S_jψ⟩`. Re-indexing the backward hop gives `Σ_x v(x) J_a^j(x)`.
   - Checked exactly at all 64 sites × 9 index pairs of the 4³ torus, plus hermiticity for random bond fields.
3. **PROVED + CHECKED (B2): uniform strains.**
   - A uniform `C_a[B]` has symbol `B cos k_a`, so `H[B](k) = Σ σ_a V_a`. Checked against the operator on all 64 plane waves of
     the 4³ torus, both coins, for a rational `B` with eight non-zero entries.
   - `(Σ σ_aV_a)² = |V|²` by anticommutation.
   - Under `k_a → π − k_a`, only `V_a` changes (only it contains `c_a`), and
     `|V|² − |V'|² = 4 s_a c_a (Bs)_a` (symbolic, general `B`).
   - If `B ≠ 0`, take a non-zero row `a` and a `k` with `s_a c_a ≠ 0` and `(Bs)_a ≠ 0`. Then `|V|²` takes two values at one
     `s`, so it is not `g^{ij}s_is_j`.
4. **PROVED + CHECKED (C1): the rewrite.**
   - `D_i = e^{ik_i} − 1 = i e^{ik_i/2} p_i`, so `e^{−i(k_i+k_j)/2}(D_iξ_j + D_jξ_i) = i(p_iη_j + p_jη_i)` with
     `η_j = e^{−ik_j/2}ξ_j`. This is checked symbolically.
   - Block 62's `R_1` and `R_2` are unchanged by `h → h + p_iξ_j + p_jξ_i`. This is checked as a polynomial identity (the
     transcription of `R_2` is tested by it).
   - So `R(Φh)`, with `Φ` the translation phases, is exactly invariant under the corner relabelling.
   - Real space: `R_1' = Σ_ij back_i back_j h_ij − Σ_m Δ_m Σ_i h_ii(x − e_i)` vanishes at all 60 sites of a 5×4×3 torus for a
     random integer relabelling.
5. **PROVED (C2, the reduction).**
   - In the site gauge, `∂⟨H⟩/∂h_aj(x) = −J_(aj)(x)` for `a < j`, and `−½J_a^a(x)` on the diagonal.
   - T5 (Fredholm alternative for block 62's symmetric static matrix) asks the sources to be orthogonal to every relabelling
     `δh = −(d_aξ_j + d_jξ_a)`: `Σ_x Σ_{a,j} J_(aj) d_aξ_j = 0` for all `ξ`.
   - Summation by parts turns this into `Σ_a back_a J_(aj) = 0`.
   - With (a), `J_(aj) = J_a^j − ½τ_aj` gives `Σ_a back_a J_(aj) = −½Σ_a back_a τ_aj = ½Σ_a back_a J_j^a`.
6. **CHECKED (C2, C3): the witness.**
   - `Hψ = ψ` exactly. `Σ_a back_a J_a^j = 0` at all 64 sites. `Σ_a back_a J_j^a ∈ {−2, 0, 2}`, not all zero.
   - For five random integer `ξ`: `Σ J_a^j d_aξ_j = 0`, the symmetric pairing equals minus the torque pairing
     `½Σ τ_aj d_aξ_j`, and it is not zero.
7. **PROVED + CHECKED (C4): plane waves.**
   - Expand `J` for `χe^{ikx} + χ'e^{ik'x}`. The cross terms give `Re[(s_j + s'_j) A_a M_a e^{iq·x}]`, with
     `2A_a = e^{ik_a} + e^{−ik'_a}`.
   - The transposed divergence multiplies by `1 − e^{−iq_a}`, and
     `Σ_a (1 − e^{−iq_a})(s_a + s'_a) = 2i Σ_a e^{−iq_a/2} sin q_a sin k̄_a`.
   - Use `s_a + s'_a = 2 sin k̄_a cos(q_a/2)`, `|s|² − |s'|² = Σ sin q_a sin 2k̄_a = 0` and `2 sin k̄ cos k̄ = sin 2k̄`. These give
     the stated form (sympy identities).
   - Checked on the witness pair at every site for all nine `(a, j)`, and for the divergence.
8. **CHECKED (C5): no re-weighting.**
   - Let an operator `P` act on the transposed current, with symbol `π_a(q)`. For a superposition of stationary plane waves, the
     `q`-component of `Σ_a back_a P J_j^a` is `Σ_{pairs} c_k c̄_{k'} A_jM_j Σ_a β_a(s_a+s'_a)`, with
     `β_a = (1 − e^{−iq_a})π_a(q)`.
   - Since `2q ≢ 0`, distinct pairs carry independent coefficients, so each pair with `A_jM_j ≠ 0` gives
     `Σ_a β_a(s_a + s'_a) = 0`.
   - At `q = (0, 3π/2, π/2)`, `j = 1`, energy 1 on the 4³ torus, these rows have rank 2 on the two components with `q_a ≠ 0`. So
     `π₂(q) = π₃(q) = 0`.
9. **PROVED + CHECKED (D1, and the pairing form).**
   - With `ΛR = 1`, the member's null directions are `ΛDξ`, and the walk's source is `R^T J`. So the condition is
     `⟨J, RΛDξ⟩ = 0`, which by (a) is `⟨J, (1 − RΛ)Dξ⟩ = 0`. `1 − RΛ` projects onto the rotations `ker Λ` along `range R`.
   - For a member `G(B)` of all nine components with `G(B + Dξ) = G(B)`, the condition is `⟨J, Dξ⟩ = 0`, which (a) gives.
   - Plaquette curls of `Dξ` vanish identically: checked on a 5×4×3 torus.
10. **CHECKED (D2): the coin-rotation law.**
    - For block 65's `H[θ] = H + ½Σ_j{(θ × e_j)·σ, S_j} + ½Σ_a C_a[d_aθ_a]`, `∂⟨H[θ]⟩/∂θ_c(x) = ½ d(ψ†σ_cψ)(x)/dt`. Checked
      exactly for a random state at all 192 site–axis pairs.
    - It is therefore zero on the witness, whose torque is not.
    - So a member depending on `h` and a coin rotation still has the condition `Σ J_(aj) d_aξ_j = 0`, which fails.
11. **ASSUMED.** Nothing beyond the declared objects. Block 62's member, blocks 63–65's couplings and block 54's walk are
    supplied clauses, not adopted. The Fredholm alternative for a finite symmetric matrix is standard linear algebra.

## 3. Where this stops

- **The first failing step of (c)** is "the symmetric part is then divergence-free".
  - For the full current, the bond placement gives an exact law.
  - For the symmetric part, which is what a metric member sees, it gives an exact failure: the bond torque's divergence.
  - The failure is at every wavelength (C4). It is not a placement artefact that a re-weighting could remove (C5).
- **Not shown: that every realisation `R` fails.**
  - On a finite torus, a `q`-by-`q` choice of `range R` containing every relabelling strain `D(q)ξ` would satisfy the condition,
    and such a choice is not local.
  - A local one would need `range R(0) ⊇ span{q̂ ⊗ ξ} = all nine directions`, against rank 6. But that argument also needs the
    stationary currents' `q`-parts to span the whole six-dimensional complement of `D(q)C³` for small `q`. That is not proved
    here. They lie in `U ⊗ C³`, with `U` the two-dimensional annihilator of `(1 − e^{−iq_a})_a`.
- Identity frame and uniform rates only, and first order in the strain. The walk's momentum is `S_j`; with the reach-two
  momentum `½ sin 2k_j` (blocks 69, 73) the current changes, and this is not examined.
- Whether a member of the full strain has acceptable dynamics for its rotational modes is not examined. Nor is it examined
  whether the three rotations propagate, and at what speed.

## 4. What would finish it

1. The spanning statement above, which would turn "no local realisation of the symmetric six removes the torque" into a
   theorem. Alternatively, a local realisation that does, which would reverse the decision.
2. The travelling modes of a relabelling-invariant member of the full nine-component strain, with the torque as the source of
   its rotations. This is the lattice form of a frame with torsion: teleparallel members that see the rotations, or
   Einstein–Cartan, as comparators.
3. The owner's call on which object, if any, the framework should carry. None is in the axioms memo.
4. A referee from another model family, especially for C1 (the translation equivalence) and C5 (the per-pair reduction).

## 5. Running it

```
python3 probes/work/derive/a-bond-placed-stress-for-the-walk/w-jonathonsmac4f50-j1518/check.py
```

- It has 10 exact checks, using `fractions`, a small Gaussian-rational class and `sympy`. There are no floats.
- It runs in about 20 seconds.
