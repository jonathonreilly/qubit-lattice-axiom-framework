# J:derive:a-lattice-ledger-that-transports-the-rates:a1: no rate-transporting lattice ledger owes the walk's fall, at any reach; two species with identical densities fall opposite ways

**Provenance.**
- Worker `w-macbookpro90c72-j7770`, model `claude-opus-5-5`, one session. Unit a1 (attempt 1 of 3); no prior attempts on the branch.
- **Plan, formed before reading the setting:**
  - parametrise every content-independent transport of the rates;
  - write the identity that invariance gives;
  - substitute the static field equations;
  - compare the force the ledger then owes with the clocked walk's exact force on plane waves.
- **Setting.**
  - Block 66 (PR #8597), read on its branch: T1–T4, the carried rate `Λ_ξ`, the force density `f_j`.
  - Harvest issue #8644: at first order, `f_j = e cos k_j (centred d_j u)`, and a strain-only relabelling forbids the fall.
  - Blocks 62, 63 and 69 for the strain couplings.
- **Overlap, disclosed.** The same model did `the-fall-from-the-ledgers-consistency:a1` (#8702), on local momenta. It is not a premise here.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**(a) The relabelling (stated exactly).**
- Strains: `B_a^j → B_a^j + d_aξ_j`, as in #8644.
- Rates: carried by a lattice transport. The choice made here is the centred one, `δu_x = −Σ_j ξ_j(x)(u(x + e_j) − u(x − e_j))/2`; that is, `δw_x = −w_x Σ_j ξ_j(x) (centred d_j u)(x)` at first order.
- For a ledger invariant under this at first order, invariance gives the identity

  `Σ_a back_a ∂F/∂B_a^j(x) = −(∂F/∂u_x)(centred d_j u)(x)`,

  which is the form the task asks for, with the centred gradient of #8644.
- More generally, any content-independent transport `T` of any reach gives `Σ_a back_a ∂F/∂B_a^j = −Σ_y (∂F/∂u_y) K_j(y, x)[u]`, with `K` built from `T` alone.

**(b) Theorem (PROVED; CHECKED F1–F4).** No lattice ledger `F[w, B]`, of any reach (not only ≤ 2), whose relabelling moves the strains by `dξ` and the rates by a content-independent transport owes the clocked walk's fall. Scope: contents coupled to the strains through block 62's frame coupling or blocks 63 and 69's reach-two and reach-three couplings.
1. **The owed force is blind to the species.** Substitute the static field equations into the ledger's identity:
   - `∂F/∂u = −(𝔢 − μ)`, from block 55;
   - `∂F/∂B = −(content's strain response)`, from block 66.

   Then the force the ledger requires of a static content, at first order in the rate gradient, is a content-independent bilinear function of `(𝔢, strain response)` and `∇u`.
2. **The walk's force is not.** At first order the clocked walk's force density is exactly `f_j = 𝔢 cos k_j (centred d_j u)`: block 66's definition, re-derived here and CHECKED F1.
3. **Two plane waves separate them (CHECKED F2).** The energy-one plane waves `k = (π/2, 0, 0)` and `(π/2, π, 0)`, related by the site sign `(−1)^{x₂}` (the species map reflecting axis 2), have:
   - equal energy density at every site;
   - equal site response `Θ = s sᵀ/E`;
   - equal, identically zero, reach-two and reach-three strain responses;
   - but exactly opposite `f₂`.

   The owed force is the same for both and the actual forces differ, so the ledger cannot be consistent with both as static contents.
4. **The finite linear system on plane waves (CHECKED F3).** The ansatz is `f_j = [α𝔢 + Σβ Θ + Σβ' R] g_j`, over all 48 energy-one plane waves of `4³`. Its rank is 3 for the coefficients against 4 augmented, for `j = 1, 2, 3`, so it has no solution. Plane-wave densities are uniform, so the reach of the ansatz does not matter.

**(c) Does not arise.** No such ledger exists.
- Restricted to one family of species (contents near one zero `k = πn`), a transport with gradient `cos(πn_j) (centred d_j u)` would match at leading order.
- But `cos(πn_j) = (−1)^{n_j}`. So a species-blind ledger serves the four species with `n_j = 0` or the four reflected along `j`, never both (F4).
- Block 66 T4's leading-order agreement is the `n_j = 0` species' only. The question whether `β = 1` survives is not reached.

## 2. Steps

**S1: the identity (PROVED).**
1. Invariance at first order means `Σ_{a,j,x} (∂F/∂B_a^j)(x) (d_aξ_j)(x) + Σ_x (∂F/∂u_x) δu_x[ξ] = 0` for all `ξ`.
2. Sum by parts in the first term, which gives `−Σ ξ_j back_a ∂F/∂B_a^j`. The second term is linear in `ξ` with content-independent coefficients.
3. `ξ` is arbitrary, which gives the identity.
- If the transport or the strain relabelling depends on the fields, extra terms `∂F/∂B · (field-dependent)` appear. They are still content-independent in form.

**S2: the owed force (PROVED).**
- **The static equations.** Stationarity of `⟨H_w⟩ + F` gives:
  - in `u`: `𝔢 + ∂F/∂u = μ` (block 55);
  - in `B`: `(strain response) + ∂F/∂B = 0` (block 66).
- **The walk's balance.** For stationary content the walk's exact momentum balance (block 66 T3(d)) sets `back · J[φψ] = −f`. At first order the strain response is `∓` the bond current.
- **Result.** Inserted into S1, the static system is consistent only if `f` equals the content-independent expression S1 produces from `(𝔢, response)`. At first order in `∇u` those densities are the zeroth-order ones.

**S3: the walk's first-order force (PROVED; CHECKED F1).**
1. Take `φ = 1 + εv`. Then `f_j = ε · 2E Re[ψ†C_j[d_jv]ψ] + O(ε²)` for a plane wave `ψ = χe^{ik·x}` of energy `E`.
2. `Re[ψ†C_j[w]ψ](x) = ½|χ|² cos k_j (w(x) + w(x − e_j))`.
3. With `w = d_jv` this gives `f_j = 𝔢 cos k_j (centred d_j u)`, where `𝔢 = E|χ|²` and `u = 2εv + O(ε²)`.
- CHECKED as 9216 exact equalities: 48 states × 3 directions × 64 sites, Gaussian rationals, with the first order extracted exactly from two values of `ε` (`f` is quadratic in `ε`).

**S4: the pair (PROVED; CHECKED F2).**
1. The site sign `(−1)^{x₂}` shifts `k₂` by `π`. With `s₂ = sin k₂ = 0` it leaves `s(k)`, `E` and `χ` unchanged.
2. The strain responses of the walk's couplings are built from `χ†σ_aχ = (s_a/E)|χ|²` together with:
   - `sin k_j`, for the frame coupling;
   - `cos k_a sin k_j`, for the reach-two coupling;
   - `cos k_a sin(2k_j)/2`, for the reach-three coupling.

   Any factor `cos k₂` there is multiplied by `s₂ = 0`.
3. So the two states have identical densities, while `f₂ ∝ cos k₂ = ±1`.

**S5: the system (CHECKED F3).** Exact ranks come from sympy on exact rational rows. The reach-three response vanishes on all these states, since `sin(2k_j) = 0` for `k_j ∈ πZ/2`, so it adds zero columns.

## 3. The first failing step

- **The route fails at S2 versus S3.** The ledger's owed force is blind to the species, while the walk's force carries `cos k_j = (−1)^{n_j}` near the zeros.
- **This is a no-go for the whole class** of rate-transporting ledgers, at every reach.
- **Scope:** contents coupled to the strains through the walk's own couplings (frame, reach two, reach three). A strain coupling through a coin-scalar hop along `j`, whose response carries `cos k_j`, is outside this scope and would be a new supplied coupling.

## 4. What would finish it

1. **A coupling whose strain response distinguishes the species along `j`**, for instance through the coin-scalar hop of block 77's `a`-term, with a ledger identity built on it. That is the one door this no-go leaves open.
2. **Species-resolved ledgers**, one per sense along each axis. Whether such a structure is supplied or forbidden by the axioms' "no possibility is privileged" is not examined.
3. **A referee from another model family.**

## 5. Running it

```
python3 probes/work/derive/a-lattice-ledger-that-transports-the-rates/w-macbookpro90c72-j7770/check.py
```

The run takes about 14 s and uses exact Gaussian rationals throughout, plus sympy for the ranks. It prints F1–F4, then the SUMMARY and HIT lines.

Standard mathematics used, none as authority:
- summation by parts;
- exact rank of rational matrices;
- Noether's second theorem, named for comparison only.
