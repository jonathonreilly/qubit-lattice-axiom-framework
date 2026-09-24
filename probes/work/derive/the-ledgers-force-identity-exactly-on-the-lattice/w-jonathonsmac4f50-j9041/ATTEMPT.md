# The ledger's force identity exactly on the lattice — attempt 2

Worker `w-jonathonsmac4f50-j9041`, model `claude-opus-5-5`. The notes used (blocks 62–72) were written by the campaign supervisor, who is from the same model family (Claude). A referee from another family should check every step.

No prior attempt was printed at claim time. Own prior art checked:
- block 66 (#8597), T1–T4 and its NOT-claimed list;
- block 64 T1 (#8595): curl-built energies have divergence-free field equations "for uniform rates";
- block 69 (#8601): the reach-three momentum `P_j`;
- block 72 (#8605): species under reach two and reach three;
- block 62 (#8592): the kinetic numbers.

## 1. Statement attempted

Conventions:
- `H = Σ σ_a S_a`, `H_w = φHφ`, `u = log w`, `χ = φψ`.
- Energy density: `e(y) = Re ψ†(y)(H_wψ)(y) = Re χ†(y)(Hχ)(y)` (block 55).
- Force density: `f_j(x)` as in block 66 T3.

**(a)** Find the exact lattice form of `f_j`. Decide whether it factorises as (energy) × (difference of `u`).

**(b)** Find the exact lattice identity of a per-tick ledger built from curls, `F = Σ_x w_x D_x(curls of B)`, under a relabelling that carries the rates along. Compare it with (a).

**(c)** Add a kinetic term for the strains.

**(d)** Repeat with `P_j = S_jC_j`.

**Result.**

*(a)*
- `f_j(x)` is exactly the average, over the two `j`-bonds at `x`, of (difference of `φ`) × (a bond cross-energy).
- It splits exactly into site energies times the exact differences `e^{Δu/2} − 1` and `1 − e^{−Δu/2}`, plus a remainder `R` that is bilinear in `(Δφ, Δχ)`.
- No identity `f_j(x) = Σ_y c_y e(y)` holds for every state. The reason is support: `f_j(x)` couples sites two steps apart, while every `e(y)` couples only neighbours.

*(b)*
- For every rate field, the lattice identity is `Σ_b E_b (dξ)_b = 0`.
- The carried rates change `F` by `Σ U δu` and never enter the identity. So this ledger owes no weight at any order.
- The walk's balance has `f ≈ e du` at leading order. The two disagree at the order of the fall.
- In the continuum, a curl-only density also fails block 66 T1 at second order. T1's weight term comes from terms that are not functions of the curls.

*(c)* The kinetic term adds only `d/dt` of the field's momentum. There is still no weight term.

*(d)* The same holds over 2-bonds, with reach three.

## 2. Steps

**A0 (CHECKED).** On a 7×3×3 torus with a generic rational clock field, block 66 T3(a), T3(b) and T3(c) hold exactly:
- (a) `i[φ, S_j] = −C_j[d_jφ]`;
- (b) `i[H_w, G_ξ] = φ(i[H,G_ξ])φ − (ΛHφ + φHΛ)`;
- (c) `Σ_x ξ_j(x) F_x = Λ_jHφ + φHΛ_j`, where `f_j(x) = ⟨ψ|F_x|ψ⟩`.

These re-check block 66's definitions with separate code.

**A1 (PROVED, CHECKED): exact bond form.**

*Formula.* Let `v(y) = φ(y+e_j) − φ(y)` and let `β(y) = Re[ψ†(y)(Hχ)(y+e_j) + ψ†(y+e_j)(Hχ)(y)]` be the bond cross-energy. Then
`f_j(x) = ½[v(x) β(x) + v(x−e_j) β(x−e_j)]`.

*Proof.* Expand `C_j[v]` in `Re[ψ†(x)(C_j[v]Hχ)(x) + (C_j[v]ψ)†(x)(Hχ)(x)]` and group the terms by bond. The check compares the two hermitian forms matrix element by matrix element.

**A2 (PROVED, CHECKED): exact split into weight and remainder.**

*Rewriting the cross-energy.*
- Write `ψ = χ/φ`.
- Use `χ(y) = χ(y+e) − Δχ` in the first term and `χ(y+e) = χ(y) + Δχ` in the second.
- This gives `β(y) = e(y+e)/φ(y) + e(y)/φ(y+e) + Re[Δχ(y)†((Hχ)(y)/φ(y+e) − (Hχ)(y+e)/φ(y))]`.

*Multiplying by `v`:* `v β = e(y+e)(e^{Δu/2} − 1) + e(y)(1 − e^{−Δu/2}) + R(y)`, with
`R(y) = Δφ(y) Re[Δχ(y)†((Hχ)(y)/φ(y+e) − (Hχ)(y+e)/φ(y))]`.

*Interpretation.*
- The first two terms are the weight: site energies times exact differences of `u`.
- At long wavelength their sum is `e Δu` to leading order.
- `R` is a product of three differences, so it is two orders below the weight.
- Block 66 states that for a plane wave the exact `f` carries a factor `cos k`. On that reading `R` is the `(cos k − 1)` part, of relative order `k²`. This is consistent with `R` being bilinear in differences, but it is not re-derived here.

**A3 (PROVED, CHECKED): no factorisation through site energies at any order.**

*The claim.* If `Δ_jφ(x) ≠ 0`, the form `F_x` has a non-zero block at the pair `(x, x+2e_j)`. On the check's field that block is `(13i/98) σ₁`.

*Why no identity is possible.*
- `H_w` hops one step, so the form of `e(y)`, which is the hermitian part of `P_y H_w`, is supported on nearest-neighbour pairs. This is checked at all 63 sites.
- A hermitian form determines its matrix, so `F_x` is not in the span of `{E_y}`, with any coefficients.
- Hence no identity `f_j(x) = Σ_y c_y(u) e(y)` holds for every state. The same holds for any nearest-neighbour bond energy built from matrix elements of `H_w`.

*Where the obstruction sits.*
- The weight part of A2 has no block at `(x, x+2e_j)`.
- `R` carries all of it. The check compares the block exactly.

*Conclusion.* The quantity that is pulled equals the quantity that sources the rates (`e`) only at long wavelength. On the lattice the pulled quantity is the bond cross-energy.

**B1 (PROVED, CHECKED): the lattice identity of a per-tick curl ledger.**

*The identity.*
- The curls `d_aB_b^j − d_bB_a^j` are unchanged by `B → B + dξ`, because lattice differences commute. This is block 64 T1.
- So any `F = Σ_x w_x D_x(curls)` satisfies `F(B + dξ) = F(B)` for every rate field. The weights are only multipliers.
- Therefore `Σ_b E_b(dξ)_b = 0` identically, with `E = ∂F/∂B`.

*The check.*
- A 3³ torus, all 243 strain variables.
- A non-uniform rational `w`.
- `D` has a random quadratic form in the nine curls, a divergence term `Σ_b V_b`, and a cross term.
- `F(B + dξ) − F(B) = 0` exactly, and `Σ E·dξ = 0` as a polynomial identity in `B`.

*Carrying the rates.* For any site rule `u → u + δ_ξu`, `F` changes by exactly `Σ_x (e^{δ_ξu_x} − 1) w_x D_x`, which to first order is `Σ U δ_ξu`.
- `F` is not invariant under the carried relabelling.
- The rates therefore enter no identity among the field equations.
- The right-hand side of the lattice identity is 0 at every order and in every rate field.

**B2 (PROVED): what the ledger requires of the content.**

*The equations at a solution.*
- Static strains' equation: `E = −𝒥`, with `𝒥 = ∂⟨H_w[B]⟩/∂B`.
- Rates' equation: `U = −e`.
- B1 with the strains' equation gives `Σ 𝒥·dξ = 0` for all `ξ`.
- Stationarity of the content, `⟨i[H_w[B], G_ξ]⟩ = 0`, then says that the total force density vanishes at every site.
- That total is the rates' force `f` (with `H → H[B]`) plus the strains' own force, defined as `⟨φψ|i[K[B], G_ξ]|φψ⟩` with `K[B]` block 63's coupling.

*Comparison.*
- Block 66 T2 (continuum) requires instead that the stress gradient equal the weight `e ∂u`. The walk meets that at leading order (T4) with no condition on the strains.
- The lattice curl ledger requires that the strains' force cancel `f` site by site.
- At zero strain this means `f = 0`. Block 66 W3 executed stationary states in a smooth rate field with `f` up to `5×10⁻³`, and no exact counterpart is claimed here.

*Conclusion.* At the order of the fall, the content's law and the lattice ledger's identity disagree. The ledger owes no weight.

**B3 (CHECKED): the continuum control, which locates the weight term.**

*The curl-only density.*
- Take the continuum density `w (−2∂_bV_b + q(T))`, where `T` is the linear curl of `B` and `q` a quadratic form. This is the curl-only analogue of the curvature member's terms.
- `∂_aE_j^a ≡ 0` for all `j`.
- Block 66 T1's combination `E_j^a∂_be^j_a − ∂_a(E_j^a e^j_b) + U∂_bu`, evaluated at polynomial fields `tB(x)` and `w = 1 + t(…)`, has no `t` term.
- Its `t²` coefficients at a rational point are `(−18029/6750, −4673/3375, −517/375)`. T1 fails at second order, which is the order of the fall.

*Validation of the code.* The same code gives zero residual, at all orders, for the volume density `w det e`, which is a scalar density.

*Conclusion.*
- The weight term in T1 needs the parts of block 64's densities that are not functions of the curls: `det e` and the nonlinear torsion vector.
- Weighted per tick, their total derivatives stop being harmless.
- These parts have no exact lattice form. Block 66 says "a relabelling makes a weighted hop of a rate, not a rate", and B1 is the ledger-side counterpart of that sentence.

**C (PROVED): kinetic terms.**

*The setting.*
- Take any kinetic term `K(Ḃ, w)` that depends on the strains only through `Ḃ`. This covers block 62's `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]`, and the same with per-site `1/w_x`.
- A static relabelling leaves `Ḃ` unchanged, so `K` is unchanged. Carrying the rates changes `K` by `Σ ∂K/∂u δu`, again outside any identity.

*The balance.*
- The strains' equations are `dΠ/dt = −E − 𝒥`, with `Π = ∂K/∂Ḃ`.
- Paired with `dξ`, and using B1: `Σ 𝒥·dξ = −d/dt Σ Π·dξ`.
- In words: the content's stress divergence is balanced by the rate of change of the field's momentum divergence.
- In statics this is B2 again. No weight term appears.

*Time-dependent relabellings* change `Ḃ` by `dξ̇`. They give no identity without a shift field, which no supplied clause contains.

**D (PROVED, CHECKED): reach three.**

*The operators.*
- `P_j = S_jC_j = (T_j² − T_j⁻²)/(4i)` (block 69).
- `i[φ, P_j] = −½ C2_j[d2_jφ]`, where `C2` is the symmetric two-step hop weighted by `d2φ(y) = φ(y+2e) − φ(y)`.

*The force density.*
- `fP_j(x) = ¼[d2φ(x) β₂(x) + d2φ(x−2e) β₂(x−2e)]`, where `β₂` is the cross-energy over the 2-bond.
- At leading order it is again `e ∂u`, because `v₂β₂ ≈ 2h u′ e`.
- The split of A2 carries over with `Δ → Δ₂`.
- `FP_x` has a non-zero block at `(x, x+3e_j)`, so there is no factorisation through site energies.

*The field side.* The reach-three coupling is also generated by a relabelling, `B → B + dξ`. B1 and B2 hold unchanged, and so does the disagreement at the order of the fall.

*Species.* Under reach three every species' weight has the sign of its energy (block 72), so nothing here depends on the species.

## 3. First failing step

None. The "fall owed by the ledger" route fails on the lattice at B1–B2, when the ledger is built from curls as the task defines it.

## 4. What would finish it

1. A lattice ledger whose identity contains a weight term. It needs non-curl terms, which are lattice counterparts of `w_x × (divergence of a non-curl quadratic)`, chosen so that `F` is invariant under a lattice relabelling that transports both `B` and `u`.
2. After that, which weight it owes. By A3, a ledger whose weight term is linear in the site energies `U = −e` can match `f` only at long wavelength, and the exact mismatch is `R` (A2). Matching exactly would need a ledger that sees bond cross-energies.
3. Whether a coupled static solution exists for the curl ledger, meaning whether the strains' force can cancel `f` site by site. This needs the coupled equations solved; nothing is claimed here.

ASSUMED: nothing beyond the named notes' definitions. Block 66 T1 is a theorem of that note, used only as the comparator: B3 checks the curl-only density against it and validates the code on `w det e`.
