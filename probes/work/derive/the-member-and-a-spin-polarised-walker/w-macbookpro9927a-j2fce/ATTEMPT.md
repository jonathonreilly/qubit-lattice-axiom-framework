# the-member-and-a-spin-polarised-walker: attempt a1

Worker `w-macbookpro9927a-j2fce` (claude-opus-5-5). The claim printed no prior attempts, and I formed my plan before reading any. Every clause is supplied and nothing is adopted.

## Sources

- **Blocks 136 and 138** are open hand-off PRs #9196 and #9200. Both are read on their branches, at `d7e6aacc` and `133b1d2c`. `check.py` pins both notes by SHA256 (`Q1`) and quotes the statements used (`Q2`, `Q3`).
- **The walk and its densities** are block 54's walk, block 69's two-step momentum `P_j = S_jC_j`, and block 120's average `φ_jᵀ = ½(1 + T_j)Π_{l≠j}C_l`. Block 120 is open; it is used as blocks 136 and 138 place it.
- **Densities, with their placements:**
  - `e`, `π_j`, `P″_j = φ_jᵀπ_j`;
  - `K_a^j` and `Θ_ij = φ_jᵀK_i^j`, with `Θ_ij` at `x + (e_i + e_j)/2`;
  - `Q_j`, `P^B = (P″ + Q)/2`;
  - the face spin `S_l(x)` at `x + (e_j + e_k)/2`, and `S̃ = C₁C₂C₃S`.

  All are exactly as in block 138's premises. `C2` confirms that my implementation reproduces block 138 T1 exactly.
- **Provenance.** Blocks 136 and 138 are the supervisor's own derivations (Claude), not refereed by another model family. This attempt is by the same family.

## 1. The statement attempted

**(c) The spin's own balance law.** For every state of the walk on `ℤ³` and each `l`:

```
dS̃_l(x)/dt + D(x) − D(x − e_l) = −Σ_ij ε_lij (Θ_ij(x) − Θ_ji(x)),
```

where:
- `D₀(x) = ¼ Σ_{four body diagonals (p, p′) of the cube [x, x + (1,1,1)]} Re ψ†(p)ψ(p′)` is placed at the cube centre `x + (1,1,1)/2`;
- `D = C₁C₂C₃D₀` is averaged over the eight body diagonals.

So:
- **The spin current is isotropic.** `J^S_il = δ_il D` is the lattice counterpart of a two-component wave's spin current `δ_il ψ†ψ`.
- **The torque is exactly the antisymmetric part of block 120's two-step stress**, which sits on the same face as `S̃_l`.
- **Consistency with block 138.** Taking the curl gives block 138's T3.

**(a) and (b) A spin-polarised walker at rest.** Take `ψ = fχ`, with `f` real (for example the indicator of a box) and `χ` a fixed spinor.
- **Nothing but the shift is sourced.** Exactly, `e ≡ 0`, `π ≡ 0` and every current `K ≡ 0`. Hence `P″ ≡ 0` and `Θ ≡ 0`: at this instant the walker sources neither the clock nor the lengths.
- **The shift is sourced by the spin's curl.** `P^B = ¼∇̄ × S̃` exactly. This is block 138 T1 with `P″ = 0`, and it is nonzero near the box's surface.
- **The source is momentarily static.** `dπ/dt = 0`. By (c) the spin moves only by a gradient, `dS̃/dt = −∇̄D` with zero torque, so `d(∇̄ × S̃)/dt = 0`.
- **The member's static transverse shift** solves `4α(−Δ̄)N = w̄P^B`. That is block 136 T4's transverse shift constraint at `ċ = 0`, read on the lattice. It is exactly
  ```
  N = ∇̄ × (−Δ̄)⁻¹ M,   M = w̄ S̃/(16α)   (= w̄ S̃/(4K) at α = K/4),
  ```
  the lattice vector potential of a magnetisation `M`. Here `S̃` is the spin `σ` (not `σ/2`).
- **Properties of `N`.** `N` is divergence-free, so the longitudinal constraint is `P^B_∥ = 0` and the clock is not driven.
- **The dipole moment.** The total `Σ_x S̃ = b(b−1)² n` for a `b³` box, with `n = χ†σχ`. At distances large compared with the box, `N` is the field of a dipole of moment `(w̄/(16α))·b(b−1)² n`; this is a continuum comparator, named only.
- **The transverse strain.** In the static gauge the transverse strain is constant, and can be taken as 0. Under a relabelling in time with `ξ = −tN`, the shift is removed and the transverse strain instead grows at the symmetrised gradient of `N` (block 136 T4(d)).

**Exact witnesses.**
- (c): random Gaussian-rational states on the `5³` torus (all 375 site–direction pairs, two states) and the `6³` torus, with all three terms nonzero.
- (a), (b): `ψ = 1_{3³ box}·(3/5, 4i/5)`, so `n = (0, 24/25, −7/25)`, on the `6³` torus, with an exact inverse Laplacian.

## 2. Steps

**S1 (PROVED; CHECKED C3). The beat of the face spin.**
- **Setup.** Take two eigen-waves with `(σ·s)u = lu` and `(σ·s′)u′ = l′u′`, where `s = sin k`. Put `q = k − k′` and `k̄ = (k + k′)/2`.
- **The beat.** The face spin's beat is `u′†σ_lu · cos k̄_a cos k̄_b · e^{iq·c}`, where `c` is the face centre and `a, b` are the two directions other than `l`.

  Both diagonals give `e^{iq·c} e^{±ik̄_a}cos k̄_b`, as block 138 states. The `C` averages add `Π_m cos q_m`.
- **Its rate.** `d/dt` supplies `i(l′ − l)`.

**S2 (PROVED; CHECKED C3). The coin identity.**
- **The identity.** `(l′ − l)u′†σ_lu = u′†[(σ·s′)σ_l − σ_l(σ·s)]u = (s′_l − s_l)u′†u + iε_mln(s_m + s′_m)u′†σ_nu`.
- **The first term.** `s_l − s′_l = 2cos k̄_l sin(q_l/2)`. With `cos k̄_a cos k̄_b` it makes `Π_n cos k̄_n`, which is the beat of `D₀`: the mean of the four body-diagonal cosines equals the product of the three cosines. The factor `2i sin(q_l/2)` is `∇̄_l` acting between the cube centres `c ± e_l/2`. So the first term is `−∇̄_lD`.
- **The second term.** Use `(s_a + s′_a)cos k̄_a = sin 2k̄_a cos(q_a/2)`. The torque term becomes
  `[sin 2k̄_a cos(q_a/2)cos k̄_b u′†σ_bu − sin 2k̄_b cos(q_b/2)cos k̄_a u′†σ_au] Π cos q`.
- **Matching the stress.** Block 120's `Θ_ij` has the beat `½ sin 2k̄_j cos(q_j/2) cos k̄_i Π cos q · u′†σ_iu` on the face. That is `K_i^j`'s beat `½ sin 2k̄_j cos q_j cos k̄_i u′†σ_iu`, averaged by `φ_jᵀ`. So the second term is exactly `2(Θ_ba − Θ_ab) = −Σ_ij ε_lij(Θ_ij − Θ_ji)` for cyclic `(l, a, b)`.

  This gives the law (c). By bilinearity it holds for every state on `ℤ³`.

**S3 (CHECKED C1). Exact random-state checks.**
- The `5³` torus: two states, every site and direction.
- The `6³` torus: every seventh site.
- The residual is 0, and the rate, the torque and the difference of `D` are all nonzero.
- On the `4³` torus the two-step momentum vanishes identically (`sin 2k = 0`), so that torus cannot test the torque. It is not used.

**S4 (PROVED; CHECKED C2). The curl gives block 138 T3.**
- `ε_jkl∇̄_k∇̄_lD = 0`, since differences commute.
- `−ε_jklε_lmn∇̄_kA_mn = 2Σ_k∇̄_kA_kj` for antisymmetric `A`.
- Hence `½ d/dt(∇̄ × S̃)_j = Σ_k∇̄_k(Θ_kj − Θ_jk)`, which is T3.

**S5 (PROVED; CHECKED A1). At rest, only the spin's curl survives.** For `ψ = fχ` with `f` real, each of `e`, `π_j` and `K_a^j` is the real part of `i` times a real number:
- `S_j` maps real `f` to imaginary values, and `C_j` keeps real values real;
- `χ†σ_aχ` and `χ†χ` are real.

So all three vanish, and with them `P″` and `Θ`. `Q` survives, since `χ†σ_jσ_aχ = δ_ja + iε_jab n_b`.

**S6 (CHECKED A2, A3).** `P^B = Q/2 = ¼∇̄ × S̃` at every bond. It is nonzero only on part of the bonds. The total face spin is `12n = b(b−1)²n` at `b = 3`.

**S7 (PROVED; CHECKED A4, A5). The static shift.**
- **The inverse Laplacian.** On the `6³` torus `−Δ̄` has the 13 eigenvalues `0, …, 12`. On zero-mean fields, `(−Δ̄)⁻¹` is the degree-12 polynomial `q(−Δ̄)`, with `q(λ) = 1/λ` for `λ = 1, …, 12` and `q(0) = 0`. This is exact over `ℚ`.
- **The shift.** `N = (w̄/(4α))(−Δ̄)⁻¹P^B` satisfies `4α(−Δ̄)N = w̄P^B` exactly. It equals `∇̄ × (−Δ̄)⁻¹(w̄S̃/(16α))` at every bond; `∇̄` and `Δ̄` commute. It is nonzero and has zero lattice divergence.
- **ASSUMED (declared reading).** Block 136 T4 states the transverse shift constraint for one wave vector, `4αp(pN_x − ċ_x)/w̄ = P_x`, with each difference's factor absorbed. On the lattice I read `p²` as the symbol of `−Δ̄` on bond fields, and take `ċ = 0` for the static response.

**S8 (CHECKED B1). The source is momentarily static.**
- `dπ_j/dt = 0` at every site.
- `dS̃_l/dt = −(D(x) − D(x − e_l))` at every face (torque 0), and it is nonzero.
- The curl of `dS̃/dt` is 0.

So `dP^B/dt = 0` at the instant: `P″` does not move, and `Q − P″` is the spin's curl. The first-order static response is consistent at that instant.

## 3. First failing step

None for (c), for (b) at the instant of rest, or for (a)'s exact source and static shift. Open:
- **The lattice reading of the member's static equation (S7).** Block 136 states T4 in Fourier form for a single wave vector. A lattice statement of the member's full static equations is not in the notes.
- **Time dependence.** The walker at rest does not stay at rest. Its stress and energy develop at order `t`, and the static response then no longer suffices.
- **The strain.** In the static gauge the strain is gauge, so no gauge-invariant transverse strain beyond `N`'s symmetrised gradient is computed.

## 4. What would finish it

- A lattice form of block 136's member, so that S7 is a theorem rather than a reading.
- The time-dependent response to the spreading walker, sourced by `Θ^sym` from order `t`.
- The law (c) together with block 136 T2 gives a total angular-momentum balance, orbital plus spin, with no torque. Stating it on the faces is the natural next identity.
