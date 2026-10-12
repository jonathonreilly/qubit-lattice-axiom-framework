# Lane RN, probe L1 (free matter): report

Worker: Claude Opus 5.5 (same family as the supervisor). Run 11:16Z to 11:45Z, 2026-10-10. No repository files were edited. Scripts and `.out` files are in this folder.

## Reading against the fixed line

**Not F-PASS.** Items 1, 2, 4 and 5 pass for the free scalar, both massive and massless. Item 3 (TT modes gapless with no counterterm) holds before matter loops enter. At the matter-loop order, O(κ), it is not established.

Under the fixed binary this counts as **F-FAIL, with item 3 named**. The failure means "not established", not "shown impossible". Item 1 is also incomplete, but not failed, for the staggered fermion and for Maxwell. This FAIL must go to a codex referee before it is recorded.

## Normalization and sign (fixed by first-class closure)

The general model is:

- H = H_N(J, g) + H_m + n·(S/κ_s + T00) + N_j·(−(J/κ_s)G_j + P_j) + c′·h_ij T_ij.
- S and G are the integer stencils of the 09-14 note.
- h_ij = δγ_ij, and q_ij = 2h_ij off the diagonal.

Closure at O(√κ) forces c′ = −κ_s/J. At the GR point (J = 2κ_s, g = 1/(2κ_s), κ_s = 16πG) this gives c′ = −½, so the coupling is **−½h_ij T_ij**.

The brief's "+½h T" is the same thing with upper-index (δγ^ij) conventions. With h = δγ_ij, the + sign would make light unbent and masses repel. The sign is load-bearing.

## 1. Exact local stresses

### Free scalar, any m ≥ 0: PROVED (hand summation by parts) and CHECKED

Placement: T00 at sites, P_j on edge (x, x+e_j), T_jj at sites, T_ij on the ij face. These are exactly the slots the 09-14 G-stencil uses. Write d_jφ(x) = φ(x+e_j) − φ(x).

- T00 = ½π² + ½m²φ² + ¼Σ_j[d_jφ(x)² + d_jφ(x−e_j)²]. Each link's energy is split half and half between its ends.
- P_j = ½(π_x + π_{x+e_j})·d_jφ(x).
- T_jj = ½π² − ½m²φ² + ½d_jφ(x)·d_jφ(x−e_j) − ¼Σ_{i≠j}[d_iφ(x)² + d_iφ(x−e_i)²].
- T_ij(face) = ¼[d_iφ(x) + d_iφ(x+e_j)]·[d_jφ(x) + d_jφ(x+e_i)]. This is **symmetric**: one object per face.

Results (`l1_scalar_stress.out`):

- Ṫ00 = div P and Ṗ_j = G[T]_j hold with residual ≤ 1.7e-13 on fields of scale 60, at m = 0, 0.7 and 2.3. The time derivatives are exact for quadratic forms (polarization identity).
- The **same P** is both the energy current and the momentum density.
- Each quantum carries momentum f_i = sin k_i, which equals ω·v_g.
- The continuum limit is ∂_iφ∂_jφ + δ_ij·L.
- Control: the canonical guess π·(forward difference) is not conserved (d/dt of its total is about 10³), so no stress exists for it.

Non-uniqueness:

- T_ij → T_ij + R(χ)_ij for any local symmetric χ. This term is identically conserved and amounts to a nonminimal R(h)·χ coupling.
- P → P + curl A. This keeps (E) but changes the antisymmetric part needed in (M).
- The placement of T00 matters (ARGUED): putting all of a link's energy on one end shifts D = Σx·T00 by a non-conserved term, so P_tot would not be conserved.

### Staggered fermion: partly CHECKED

`l1_closure_and_fermion.out`, L = 6, m = 0 and 0.45:

- With T00(x) = ½{Π_x, h} and P_j = ½{J_j, h} (J the link particle current), Ṫ00 = div P holds exactly (residual 0).
- [h, P_tot] = 0 exactly.
- The spectrum of P_tot,x is the multiset ½ sin 2k_x (to 1e-15).

A **symmetric T_ij was not constructed.**

- SUGGESTED: by the module criterion, a symmetric T exists if a local spin density exists. The candidate, in the spin–taste symbol, is −cos k_i cos k_j·(i/4)[Γ_i, Γ_j]. This lattice Belinfante term cancels v_iP_j − v_jP_i.
- Neither the candidate nor the criterion was verified numerically here.

### Yee Maxwell: necessary condition CHECKED

`l1_maxwell_energy_current.out`, L = 6. Use symmetric site placement of T00: each link's E² goes ½ to each end, and each plaquette's B² goes ¼ to each corner. Then:

- d²D/dt² = 0 on the Gauss surface, to 7e-16. Off the Gauss surface it is 0.5.
- So the total energy current is conserved modulo Gauss's law. This is necessary for P = energy current.
- A local P and a symmetric T were **not constructed**.
- K3a's exact radius-½ stress was built without imposing that P equals the energy current, so it does not settle this.

## 2. First-class constraint algebra at linear order

PROVED from stencil identities plus (E) and (M); CHECKED numerically.

The gravity-sector identities (09-14 stencils) hold:

- S(q̇) = −J·div G, residual 7e-15.
- G Sᵀ = 0 exactly (integer).
- {G, V_N} = 0 uses the note's identity R2 Gᵀ = 0, cited and not re-run.

With these, at O(√κ):

- d/dt(S/κ_s + T00) = div(Φ_j).
- d/dt(−(J/κ_s)G_j + P_j) = 0.
- The lapse and shift terms drop out by G Sᵀ = S Gᵀ = 0.
- Mutual brackets of the constraints vanish at this order.

At O(κ), the order where matter loops enter, I CHECKED whether the matter part of the constraint algebra closes by itself (`l1_closure_and_fermion.out`, `l1_T00T00_check.out`, `l1_closure_1d_modes.out`):

- **{T00[μ], T00[ν]} = Σ_{x,j}(μ_x ν_{x+e_j} − ν_x μ_{x+e_j})·P_j(x) holds exactly** (4e-16). The lattice H–H bracket closes.
- **{P[ξ], P[η]} does not close.** No c-number combination of the P_j(x) and T00(x) fits it: the relative residual is 1.00 at L = 5, 8 and 12, with random and smooth ξ, η. In a 1D mode-resolved check it agrees with P[[ξ, η]] on IR modes (defect 2% for |k| < 0.2, 10% for |k| < 0.5) but is O(1) at lattice scale.
- **{P[ξ], T00[ν]}** gives residual 0.64–0.72.

So matter alone does not supply an O(κ) first-class completion. Corrections to the constraints at O(κ) that depend on h or on E were **not searched**, so this is a diagnostic, not a no-go.

## 3. TT spectrum

**At O(√κ): PROVED.** The coupling adds no h² term and no extra modes. The TT sector is H_N's: ω² = Jg·q̂², linear and untuned in the sense of no mass term (q̂ = 2 sin(k/2)).

**At O(κ), one matter loop, linear coupling only: CHECKED, and nonzero.** I computed the static vacuum response d²E₀/dε² per site (`l1_scalar_observables.out` §6; converged from Nb = 48 to 96). The two channels are the E channel, h = ε·diag(1, −1, 0), and the T2 channel, h_xy = h_yx = ε.

| Mass | E channel | T2 channel |
|---|---|---|
| m = 0 | −0.003695 | −0.011782 |
| m = 0.5 | −0.003172 | −0.010574 |
| m = 1 | −0.002317 | −0.008228 |

Both channels are nonzero, and their ratio is about 0.3, so the response is cubic-anisotropic: μ_E and μ_T2 are both nonzero. The R2 referee's −0.0386 at m = 0.5 uses a different coupling, so the numbers are not directly comparable.

**Ward identity.**

- ARGUED (f-sum algebra): a constant strain is pure gauge, ξ_i = ½h_ij x_j. For free fields, identity (M) gives U = exp(−iΣξ·P) with U H_m U† = H_m − ½h·ΣT + O(h²). E₀(h) is therefore exactly h-independent iff the O(h²) term is U's seagull. Then Π_TT(0) = paramagnetic + seagull = 0 identically.
- SUGGESTED: the seagull is local and translation-invariant, because [P_tot, ΣT] = 0.
- **So "exactly zero by the Ward identity" holds only with that O(h²) completion.**
  - The linear first-class algebra does not contain it.
  - Without it, a c-number counterterm (two tunings) is needed.
  - Extending it to non-constant h as a first-class O(κ) theory is blocked by the {P, P} non-closure above.

**Difference from K3a″.**

- K3a″ fixed its O(h²) coupling geometrically: vielbein-stretched hops on a fixed grid, plus O(e²) QED.
- That completion is not the pseudo-momentum flow U(h), which moves modes along sin k·∂_k rather than k·∂_k.
- Its c₂ ≠ 0 measures the mismatch between the two completions, plus interacting terms where no exact P exists. The interacting part is L2's question.

## 4. Universality and 1/r

PROVED (linear algebra) and CHECKED.

- **Static solution** (`l1_scalar_observables.out` §1; L = 96; the dust source has T_ij = 0):
  - ψ = κ_s·T00/(4q̂²) and n = −2gκ_s·ψ.
  - At the GR point ψ + n = 0 exactly.
  - n follows the lattice Coulomb law. Differences n(r) − n(16) match −GM(1/r − 1/16) to 0.05% at r = 8 on an axis, and to about 1–2% at r = 4 and on the diagonal, which is the lattice and torus correction.
- **Active coupling:** only T00 enters.
- **Passive coupling:** a quantum at rest has δω/ω = 1.00000000·n for m = 0.2, 0.8 and 1.5, with the coefficient of ψ below 1e-6. The same G holds for different masses.
- **Caveat:** species with different hopping speeds c_A are still universal at rest, but each sees γ_A = c_A²/c_g².

## 5. Light bending

PROVED within the linear theory, and CHECKED.

- **The general result is γ = 1/(Jg) = (c_matter/c_graviton)².** At the GR normalization this gives **γ = 1 at leading order**. Checked: Jg = 0.9 and 1.1 give γ = 1.111 and 0.909.
- **γ = 1 is not supplied by the lattice.** It is the one-speed tuning c_g = c, which R2 already counted. Cassini's bound only asks for |c_g/c − 1| < 1.2e-5, much weaker than GW170817.
- **Exact frequency shift:** δω/ω = n − ψ·Σ sin²k_j/ω² (`l1_scalar_observables.out` §2). For a massless packet this gives (1 + γ_eff)·n.
- **Anisotropy:** γ_eff(k) = Σ sin²k_j / Σ 4 sin²(k_j/2) = 1 − Σk_j⁴/(4k²) + O(k⁴). That is −k²/4 along an axis, −k²/8 along a face diagonal and −k²/12 along a body diagonal (checked).
- **Fermion γ:** SUGGESTED to be 1 through Σ f_i v_i/ω → 1 at every node. It is not computed, because no symmetric T was built.

## Strong-word check

- "Exact" applies only to the identities listed with their residuals.
- "Proved" means a short algebraic derivation plus a probability-1 random-point check.
- "Closes" and "does not close" for the O(κ) algebra are diagnostics within the class of c-number structure functions over {P, T00}.
- No claim is made about h-dependent completions, interacting matter, or a compact qubit realization.

## Files

All in this folder:
- `l1_scalar_stress.py` / `.out`
- `l1_scalar_observables.py` / `.out`
- `l1_closure_and_fermion.py` / `.out`
- `l1_T00T00_check.py` / `.out`
- `l1_closure_1d_modes.py` / `.out`
- `l1_maxwell_energy_current.py` / `.out`
