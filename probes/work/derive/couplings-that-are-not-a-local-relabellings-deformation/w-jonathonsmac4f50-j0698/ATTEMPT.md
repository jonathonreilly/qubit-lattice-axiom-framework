# couplings-that-are-not-a-local-relabellings-deformation, attempt 2 of 2: every conserved coupling is a local relabelling's deformation, and no coupling of reach two shows the species one geometry

Worker `w-jonathonsmac4f50-j0698` (`claude-opus-5-5`), unit `J:derive:couplings-that-are-not-a-local-relabellings-deformation:a2`.

**Provenance.**
- Attempt a1 was not delivered: there are no files and no log. My plan is my own.
- Definitions come from:
  - block 54 (PR #8570): the walk `H = Σσ_aS_a`, with symbol `σ·s(k)`, `s_a = sin k_a`;
  - block 63 (#8593): relabellings `G_ξ = ½Σ{ξ_j, S_j}`, the symmetric bond hop `C_a[v]`, and T4;
  - block 64 (#8595): the bond strain, and curls;
  - block 69 (#8601): the reach-three coupling with `S_jC_j`;
  - block 72 (#8605);
  - block 73 (#8606): the ladder's closure within relabellings generated with a conserved momentum, whose N1.1 leaves other couplings open;
  - block 74 (#8607).
- All of these blocks are by the same model family as me and unrefereed.
- **Block 73 T2/T3 already hold (d)'s conclusion within relabellings.** They show that no scalar momentum of reach at most two gives one geometry except `½ sin 2k_j`, whose coupling has reach three.
- **New here:**
  - the closed form of the generator for any coupling;
  - the locality theorem (one standard step ASSUMED);
  - the character argument that extends (d) to every coupling of reach at most two, relabelling or not, conserved or not.
- Nothing is adopted. No gravitational claim is made.

## 1. What is claimed

> **(a)** Let `dH[B]` be hermitian, linear in a bond field, translation-covariant and of finite reach. For `B = dξ`, `ξ_j = e^{ip·x}`, write its symbol as `A(k, p)` (from `k` to `k + p`).
> 1. Its response is conserved on every stationary state iff `A` has no block between equal energies, that is, iff `N := H(k+p)A + AH(k)` vanishes wherever `|s(k+p)| = |s(k)|`.
> 2. Because the walk squares to a scalar, `H(k)² = |s(k)|²`, the deformation is then `i[H, G]` with the explicit
>
>    **`G = −i(H(k+p)A + AH(k))/Δ`,  `Δ = |s(k+p)|² − |s(k)|² = Σ_a sin p_a sin(2k_a + p_a)`**.
>
>    Off the degenerate set this `G` is unique.
> 3. `Δ` is irreducible and square-free over `Q(i)` (checked). Then, with one standard real-algebraic step (ASSUMED), `Δ` divides `N`. **So `G` is a trigonometric polynomial in `k` and `p` jointly: local, linear in `ξ`, and of reach one less than the coupling.**
> 4. Exact at a plane wave: the closed form returns `½{ξ_j, S_j}` for block 63's coupling and `½{ξ_j, S_jC_j}` for block 69's.
>
> **(b)** Hence on `Z³` no local conserved coupling needs a non-local generator. There is no smallest example to test against the four demands. The division by energy differences is always exact.
>
> **(c)** A coupling through the curls alone:
> - has `dH[dξ] = 0`, so its response is conserved identically and `G = 0`;
> - makes no lengths for a uniform strain, which has no curl;
> - leaves `dH[dξ]`, and with it block 72's requirement, unchanged when added to another coupling.
>
> **(d) Theorem.** Take any coupling whose symbol at uniform strain has reach at most two (L1 hop length ≤ 2). It may have any coin structure, may or may not be conserved, and may have a local generator or not. At first order in the strain, species `n` sees the metric `1 + D_n dM_n + (D_n dM_n)ᵀ`, where `dM_n` is the gradient of the symbol at its zero. For `c ≠ j` the entry `D_c ∂_j f(πn)` of every monomial of reach at most two is a non-trivial character of the eight species. Hence:
>
> **the mean over the eight species of the shear metric they see is exactly zero.**
>
> - No coupling of reach two shows all eight species one geometry for a shear.
> - A nonzero mean first appears at reach three, and only for `e^{i(2e_j ± e_c)·k}` (block 69's `cos k_c sin 2k_j`).
> - Independently, the energy reversal by `U_(111)` confines a reach-two coupling to nearest-neighbour hops.
>
> **So no reach-two coupling meets the ladder's demands, and the task's HIT condition is not met.**

## 2. The steps

1. **PROVED + CHECKED (A1).**
   - With `H' = H(k+p)`, `H = H(k)` and `H'² = |s'|²`, `H² = |s|²`: `H'(H'A + AH) − (H'A + AH)H = |s'|²A + H'AH − H'AH − A|s|² = ΔA`. So `G := −iN/Δ` gives `i(H'G − GH) = A` wherever `Δ ≠ 0`.
   - The solution is unique there: an intertwiner `H'K = KH` maps eigenvalues to equal eigenvalues, and there are none in common when `|s'| ≠ |s|`.
   - Checked symbolically for an arbitrary `2×2` matrix `A`.

2. **PROVED + CHECKED (A3): the conservation criterion.**
   - As block 63 T2(c) does for its relabelling, the response's divergence paired with `ξ` is `⟨ψ|dH[dξ]|ψ⟩`. It vanishes on every stationary state, including every superposition within one energy shell of `Z³`, iff the compressions of `dH[dξ]` to each eigenspace vanish (polarisation).
   - For plane waves this reads `P_α(k+p)AP_α(k) = 0` for equal energies. Since `P'_αNP_β = (λ'_α + λ_β)P'_αAP_β`, that is the same as `N = 0` on `{|s'| = |s|}` away from the zeros.
   - Checked exactly at degenerate pairs `(k, Rk)`, with `R` permuting the axes and `k` Pythagorean:
     - blocks 63 and 69 have zero blocks and `N = 0` there;
     - block 62's nearest-neighbour frame coupling has nonzero blocks. This matches block 63's statement that its response is not conserved.

3. **CHECKED (A2): the plane wave, exactly** (symbolic in `e^{ik}` and `e^{ip}`). For `M = S_1` and `M = S_1C_1`:
   - the coupling's symbol `Σσ_a C_a[d_aξ]·(M(k) + M(k+p))/2` equals `i(H'G − GH)`;
   - `N = iΔG` with `G = (M(k) + M(k+p))/2`.

4. **The locality theorem.**
   - **CHECKED (A4):** the numerator of `Δ`, cleared of denominators, is one irreducible factor of multiplicity one over `Q` and over `Q(i)`, and it changes sign on the real torus.
   - **ASSUMED (a standard real-algebraic step):** a polynomial that vanishes on the five-dimensional real zero set of an irreducible, square-free, sign-changing hypersurface is divisible by its defining polynomial.
   - Then `Δ | N`, and `G = −iN/Δ` is a Laurent polynomial in `(e^{ik}, e^{ip})`: local, linear in `ξ`, with `reach(G) ≤ reach(A) − 1` by degree.
   - *The special momenta.* At `p ∈ π{0,1}³` the polynomial `Δ` vanishes identically. There the diagonal blocks of `G` are free, and the conserved operators, block 70's species maps `V_n` for even `|n|`, are on-site.
     - Expanding `N` near such `p` together with the degeneracy condition shows `∇_pN ∥ sin 2k`, so `G` is continuous there as well (proved in outline; the algebraic step covers it).

5. **PROVED (C1).** `d_ad_bξ = d_bd_aξ`, so the curl of `dξ` vanishes. The rest of (c) follows by linearity, and from block 64 T1(c) (a curl coupling's response is identically divergence-free).

6. **PROVED + CHECKED (D1): the theorem.**
   - *The metric each species sees.* At uniform strain the symbol is `f₀(k) + Σ_cσ_cf_c(k)`. Near zero `n` the walk is `Σσ_cD_cδk_c`, so the cone is `Σσ_c[(D + dM_n)δk]_c`, with `dM_{n,cj} = ∂_jf_c(πn)`. Its metric is `(D + dM)ᵀ(D + dM) = 1 + D dM + (D dM)ᵀ + O(B²)`. A shift of the node or of the energy does not change it.
   - *The characters.* `∂_j e^{im·k}` at `πn` is `i m_j (−1)^{m·n}`. For `|m|₁ ≤ 2` and `m_j ≠ 0`, the character `(−1)^{m·n}` is `D_j`, `1` or `D_jD_b`. So `D_c∂_jf_c(πn)` with `c ≠ j` lies in `span{D_c, D_cD_j, D_j, D_cD_jD_{c'}}`, none of which is constant.
   - *The mean.* The shear entry's mean over the eight species is therefore zero. "One geometry" needs every species to see `(1 + B)ᵀ(1 + B)`, whose shear entries are nonzero for a symmetric shear. So it fails.
   - *Checked:* exact enumeration of all 62 monomials of L1 degree 1 to 3. All reach-≤2 means vanish; the nonzero ones at degree three are exactly `2e_j ± e_c`.
   - *And `U_(111)`:* the displacements of odd L1 length within reach two are exactly the six nearest neighbours.

## 3. Where this stops

- **(d) is a theorem at reach two with no assumption.** One geometry for all species needs reach three, whatever the coupling. This closes block 73's N1.1 for that demand.
- **(a)'s locality rests on the ASSUMED real-algebraic step.** The supporting checks are irreducibility over `Q(i)` (not over `C`) and the sign change.
  - A referee should check absolute irreducibility, or replace the step by a direct argument, for instance the torus conjugation symmetry of `Δ` together with the sign change.
- **(b):** no non-local example exists on `Z³`. On a single finite torus the conservation condition is weaker: only that torus's exact degeneracies count. Torus-specific couplings could then exist; they are not pursued.

## 4. What would finish it

1. Absolute irreducibility of `Δ`, or a direct proof of `Δ | N` from the conservation condition.
2. The same character argument for demand (4), block 72's requirement for every species, at reach three. It is already met by block 69's coupling.
3. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/couplings-that-are-not-a-local-relabellings-deformation/w-jonathonsmac4f50-j0698/check.py
```

- It has 6 lines, all exact (sympy; Gaussian rationals; integer characters).
- The one numeric evaluation is a 30-digit sign of `Δ` at two points.
- It runs in about 65 seconds; the factorisation over `Q(i)` takes most of that.
- **No HIT line.** The task's HIT condition, a reach-two coupling meeting all four demands, is refuted by (d).
