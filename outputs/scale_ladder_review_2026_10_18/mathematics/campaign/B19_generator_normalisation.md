> Live supporting mathematical source with scope corrections. Historical run tables and numerical values below are submitted evidence, not a fresh capture or independent validation. The cross-rung primary does not execute these campaign producers. Exact displayed algebra retains its stated hypotheses. Terminal exclusions beyond the explicitly active constructive results remain deferred scientific proposals; their full arguments are preserved here for inspection and are not adopted by historical verdict labels.

# B19 findings: is the relabelling-generator normalisation, and hence the common cone, derived?



Runners, all printing PASS/FAIL and a TOTAL:
- `b19_continuum.py`: exact sympy jet calculus in 3D. PASS=19 FAIL=0.
- `b19_continuum_g2.py`: exact. PASS=3 FAIL=0.
- `b19_lattice.py 3 4`: exact rational elimination plus a numpy scaling study. PASS=12 FAIL=0.

Two first-run bugs are kept as `*_BUG.log`:
- C10a forgot that μ is rescaled.
- S4's magnitude threshold was guessed a priori and was wrong. It was replaced by a convergence-order criterion after the values had been seen (disclosed).

Conventions: δ_ξF = {F, G[ξ]}, and [ξ,η] = ξ·∂η − η·∂ξ.

## Continuum

**1. {G,G} closure, verified exactly.**
- **Scalar.** {G_m[ξ],G_m[η]} = +G_m[[ξ,η]], with π a weight-1 density (C1a).
- **Gravity.** With G_g = ∫P L_ξ(δ+h), {G_g,G_g} = G_g[[ξ,η]] to all orders (C2a).
- **Maxwell, Lie form.** G_L = ∫E L_ξA closes exactly (C3a).
- **Maxwell, covariant form.** G_c = ∫E^i ξ^k F_ki = G_L + Gauss[ξ·A], and {G_c,G_c} = G_c[[ξ,η]] − Gauss[ξ^iη^jF_ij] (C3b).
- **Cross brackets** vanish (C4a).

**2. What {G,G} fixes.**
- λG_s closes only for λ ∈ {0, ν} (C1b, C3c). For matter this bites at the matter fields' leading (quadratic) order, not at a nonlinear order.
- Write gravity as λ1 G1 + λ2 G2. Then {G,G} forces λ2 = ν but leaves λ1 free at every order (C2b). The ratio λ1/λ2 is the background scale r in g = rδ + h.
- Total: λ_m = λ_A = λ2 = ν, with λ1 free (C4b).
- **So {G,G} never fixes matter against the linear gauge shift δh = 2λ1∂ξ.** The B16 check's "λ_g = 1" is supplied by identifying h = g − δ.

**3. {C,C} at O(ε)** (C5): v_s² = λ_s K1/(4αλ1) for each species.

**4. {G,C} at O(matter²)** (C6):
- s1 = −λ_s, and the coupling strength is a_s = λ_s/λ1 times the metric stress.
- One constraint has one lapse rule, so λ_A = λ_m. This holds at B14's order with no {G,G} input, which excludes "double G_A → 2κ".

**5. Gravity's own {G,C} at h-linear order** (C7, C12, C13):
- **Same order as before.** In B14's counting (h, P ~ ε; φ, π ~ ε^½) this bracket is O(ε), the same order as items 3 and 4. B14 and B16 did not compute it.
- **It needs a quadratic generator G2.** Over a general 12-term covariant ansatz there is no solution with G2 = 0.
- **The lapse rule is unique:** s1 = −λ1·K2/K1 and s2 = 0, where K2 multiplies [√gR]^(2).
- **G2 itself is fixed only partly:** up to 3 directions W with R1(W) ≡ 0. Two of them are the field-dependent reparametrisations G1[h·ξ] and G1[tr h ξ].

**6. Block 62's R_2 is exactly [√gR]^(2) of g = δ + h** (C11). So K1 = K2 = K in the 09-24/block-101 member.

**7. Graviton speed.** The TT graviton has speed² K2/(4α) (C8).

**8. The chain** (C9): items 3–5 give v_s² = K2/(4α), the same for every species and equal to the graviton cone. All λ's cancel. With block 62, v² = K/(4α) = κ.

**9. Canonical rescalings** (C10):
- φ → φ/√r, π → √r π leaves G_m invariant. It cannot move λ_m.
- h → ρh, P → P/ρ maps λ1 → λ1/ρ, K1 → ρK1, K2 → ρ²K2, α → ρ²α and a_s → ρ a_s.
- Every derived relation, and the cone, is invariant. The invariant form of B14's "c = κ" is v_s² = a_s K1/(4α).
- **λ_s is a symplectic invariant**, because the structure constant of a represented Lie algebra survives any canonical map. Rescaling a sector's symplectic form is not canonical, and in the given bracket it is just λ_s ≠ 1, which item 4 excludes.

## Lattice

**Exact (L = 3, 4; random integer ξ, η; positive controls pass).**
- {G_m,G_m} ∉ span{G_m[ζ]} for any ζ. The certificate is [D_ξ,D_η]'s range-2 entries (ξ_bη_{b+e} − η_bξ_{b+e})/4.
- B16's G_A fails even mod Gauss, with any multiplier, and G_L fails too.
- Uniform translations commute.
- **The lattice relabellings do not close among themselves.**

**Smooth fields, against the natural second-order commutator ζ_lat.**
- Scalar defect ~ a^2.10, i.e. O(a²).
- One-sided G_A ~ a^0.95 and G_L ~ a^0.97, i.e. O(a).
- On rough φ the defect stays O(1).
- The effective structure constants β_s → 1:

  | | β at L = 48 | β − 1 slope |
  |---|---|---|
  | β_m | 0.9825 | −1.99 |
  | β_A | 0.9698 | −1.72 (possibly pre-asymptotic) |

- So λ_A/λ_m is pinned to 1 only asymptotically (1.013 at L = 48), never exactly.

**Gravity on the lattice.** The lattice G_g is linear, hence abelian, and 09-24 defines no lattice G2. So no lattice bracket fixes λ1. The lattice h-linear {G,C} is not computed and is open.

## Derived vs supplied (continuum, order ε)

| | Status |
|---|---|
| Matter–matter cone equality, and λ_A = λ_m | **Derived** at B14's order: {G,C} with one lapse rule, or {G,G} at the matter fields' leading order |
| Matter cone = graviton cone = K2/(4α), and = κ when K1 = K2 | **Derived** at the same order once gravity's h-linear {G,C} is included |

The second row rests on:
- block 62's Fierz–Pauli R2 with the same K (a supplied model clause, verified in C11);
- admitting a quadratic relabelling G2, which is required for gravity's own closure at that order;
- one constraint C.

**Conditional within B14/B16's computed brackets:** the value κ needs the supplied ratio λ_s/λ1 = 1. The B16 check's {G,G} argument cannot supply it, because λ1 is free.

**On the lattice:** nothing is fixed exactly. The relabellings are not a Lie algebra, with defects of O(a²) for the scalar and O(a) for the one-sided Maxwell generator. The normalisation is selected only in the continuum limit, and the lattice gravity G2 is missing.

## Caveats

- Flat background, polynomial order ε.
- The matter coupling is taken as metric stress plus a trace term, not re-derived. B14 and B16 derived it.
- Continuum results come from sympy solves over the stated ansätze.
- The lattice scaling uses one set of smooth test fields, and its slopes are fits.
- Exact lattice certificates cover only L = 3, 4 with two configurations each.
- The fermion G_f was not tested.
- Higher brackets ({G,G} with G2's free R1-null directions, and degree-2 {C,C}) are not checked.

## Prior art

- Teitelboim 1973; Hojman–Kuchař–Teitelboim 1976: the representation of the deformation algebra forces δg = L_ξg and GR.
- Kuchař 1974–76; Isham–Kuchař 1985.
- Barbour–Foster–Ó Murchadha 2002 and Anderson–Barbour 2002 ("relativity without relativity"): a universal light cone from consistent propagation of the Hamiltonian constraint with matter. This is the closest known result to item 8.
- Fierz–Pauli 1939; Deser 1970.
- Lattice breaking of diffeomorphisms: Renteln–Smolin, Gambini–Pullin, Bahr–Dittrich 2009.

**New and narrow here:**
- λ1 is free under {G,G} to all orders;
- the single-lapse-rule argument at order ε;
- the explicit order-ε fixing via gravity's h-linear {G,C} with the generic G2 ansatz;
- the lattice non-closure certificates and their orders.
