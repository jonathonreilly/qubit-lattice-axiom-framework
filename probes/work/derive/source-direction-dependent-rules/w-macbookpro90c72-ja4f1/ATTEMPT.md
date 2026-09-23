# J:derive:source-direction-dependent-rules:a3: direction-dependent rules make content hedgehogs around records and lumps, but give no universal one-over-r attraction

**Provenance.**
- Worker `w-macbookpro90c72-ja4f1`, model `claude-opus-5-5`, one session. Unit a3; no prior attempt files exist on the branch.
- **Plan, formed before computing:**
  - (a) Burnside and exact orbit enumeration.
  - (b) Exact enumeration with symbolic `t`, validated on block 41's refuter number.
  - (c) The Goldstone coupling's derivative order decides the interaction's form.
  - (d) Exact enumeration of absence factors on lumps.
- **Setting.** Blocks 39–41 as the task restates them; block 01's reading (ii) as the task states it.
- **Related earlier units.** The same model did `moving-clumping-bounds` (#8728) and `odds-field` (#8723). Neither is used here.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**(a) Classification (PROVED; CHECKED D.a).**
- **Free values.** Under the 24 proper rotations acting on sites and contents together, the triples `(a, b, d)` of contents and bond direction fall into **12 orbits**. Each orbit is fixed by `(a·b, a·d, b·d, (a × b)·d)`, so a covariant nearest-neighbour pair weight on the six-axis menu has 12 free values.
- **Handedness.** The two orbits with `a, b, d` mutually orthogonal differ only by handedness: a chiral pair of values.
- **Symmetric weights.** Symmetry under exchange of the ends with `d → −d` leaves **9**.
- **The product subfamily** `h(a·d)h(−b·d)ω(a·b)` with `h(1) = t`, `h(0) = h(−1) = 1` is covariant, automatically symmetric and blind to handedness. It takes 6 distinct values: `pt, p, rt, r, qt², q`.
- **Burnside.** `(6³ + 9·2³)/24 = 12`. The identity fixes 216 triples; the nine face rotations fix `2³` each; the vertex and edge rotations fix none.

**(b) The content field in small occupied windows (CHECKED D.b, exact as functions of `t`, at `(p, q, r) = (3, 1, 2)`).**
- **Line of 3.** The end records carry `∓(t − 1)(3t² + 27t + 40)/(3t³ + 50t² + 179t + 200)` along the line, pointing at the middle record. At `t = 2` this is `53/391`, block 41's refuter's value `(−53/391, 0, 0)`.
- **Plaquette.** Every corner points at the centre.
- **2×3 window.** Every record leans towards the window's middle.
- **The isotropic rule.** Every field vanishes exactly at `t = 1`, block 41's rule.
- **So:** around a record, the neighbours' contents point at it, in proportion to `t − 1`.

**(c) An ordered medium (PROVED; CHECKED D.c exactly on `4³`; far form executed).**
- **The linear coupling.** Near an order along `+z`, the tilt `π` (the massless modes of a continuous-content medium) is transverse. A hedgehog rule (`h′(0) ≠ 0`) couples a record's occupancy linearly to the **in-plane divergence** of the tilt at the record: `−λ n (div_⊥ π)`.
- **The exact pair kernel.** Minimising `(K/2)Σ|∇π|²` against it gives `−(λ²/K)Σ_{c=x,y} D_c G D_cᵀ`, with backward differences `D_c` and the zero-mean lattice Green function `G`. On the `4³` torus, exactly:

  `Σ_{c=x,y} D_c G D_cᵀ = δ − 1/N + Δ_z G`.
- **The field of one record** is the gradient of `G`: a dipole-like tilt falling as `1/r²`.
- **The interaction of two records** is `−(λ²/K)Δ_z G(r)` off-site. Far away this is `−(λ²/K)(3cos²θ − 1)/(4πr³)`:
  - attractive along the order, repulsive across it;
  - zero angular mean;
  - executed on `32³`: `Δ_z G · 4πr³` tends to `+2` along and `−1` across.
- **A three-component tilt** (a full divergence) leaves only the contact term `δ − 1/N`.
- **The general reason (PROVED).** A scalar occupancy can couple linearly to the transverse Goldstone field only through a covariant scalar built from it: at lowest order its divergence, which carries one derivative. No derivative-free scalar is linear in a vector transverse to the order. With a massless propagator `∝ 1/k²`, the induced pair interaction has a symbol homogeneous of degree zero at small `k`. Its real-space form is a contact term plus a `1/r³` tail with zero angular mean. It is never `1/r`, which needs a symbol `∝ 1/k²`.
- **Conclusion.** **Direction-dependent rules cannot give a universal one-over-r attraction between masses.**

**(d) Block 01's reading (ii): absence factors (PROVED; CHECKED D.d, exact).**
- **Setup.** An empty neighbour in direction `d` contributes `φ(s, d) = a, b, c` for `s·d = 1, 0, −1`.
- **No action across a gap.** The absence factors belong to single records, so the weight still factorises across an empty site (block 41's refuter W7).
- **An isolated record** has no preference: each content meets `a`, `c` and `b⁴` once.
- **Lumps.** At `(p, q, r) = (3, 1, 2)`:
  - a dimer's ends, a plaquette's corners and the corners of a `2×2×2` lump lean **outward when `a > c`** and inward when `a < c`;
  - the cube's corners lean exactly along the body diagonals (`89734618/506936397` per component at `(a, b, c) = (3, 2, 1)`).
- **So** a closed lump carries a hedgehog of content, radial with zero vector sum. The preference comes from the surface, not from any action across the void.

## 2. Steps

**S1 (PROVED; CHECKED D.a).**
- The rotations are the 24 signed permutation matrices of determinant 1. Orbits are computed by canonical forms, and each is fixed by the four invariants (checked).
- **The handedness invariant.** `(a × b)·d = ±1` is preserved by proper rotations and exchanged by reflections, which are not in the group.
- **Exchange** sends the invariants `(a·b, a·d, b·d, χ)` to `(a·b, −b·d, −a·d, χ)`. This pairs orbits `{1,3}`, `{4,8}` and `{5,9}`, and fixes the rest: 9 classes.
- **The product family's values** depend only on `(a·b, a·d, b·d)`, so they are blind to `χ` and exchange-symmetric.

**S2 (CHECKED D.b).**
- The weight is `Π_bonds ω·t^{k}`, with `k` the number of bond ends whose content points along the bond. Integer coefficients are accumulated per power of `t`, and the fields are formed as exact rational functions.
- **Directions checked:**
  - the plaquette corners are parallel to the inward direction, with positive projection at `t = 2`;
  - on the 2×3 window the middle column has zero `x`-component, and the corners lean inward.
- **The isotropic limit.** Every field vanishes at `t = 1` (block 41's isotropy lemma).

**S3 (PROVED; CHECKED D.c).**
- **Stationarity.** `K(−Δ)π_c = λD_cᵀn`, so `π_c = (λ/K)G D_cᵀ n`, and `F_min = −(λ²/2K)Σ_c nᵀD_c G D_cᵀ n`.
- **The identity.** On the torus the difference operators and `G` are circulant and commute, and `Σ_{c=x,y,z} D_cD_cᵀ = −Δ`. So `Σ_{c=x,y} D_cGD_cᵀ = (1 − P₀) − D_zD_zᵀG = δ − 1/N + Δ_zG`.
- **CHECKED** entrywise with exact rationals on `4³` (`G` exact via `(−Δ + P₀)⁻¹ − P₀`).
- **The far form.** `Δ_zG ≈ ∂_z²(1/4πr) = (3cos²θ − 1)/(4πr³)`: executed as described.
- **The homogeneity argument.** The symbol of the kernel is `Σ_c |1 − e^{ik_c}|²/E(k)`, of degree zero at small `k`. Its inverse transform is a contact term plus a Calderón–Zygmund `1/r³` kernel with zero angular mean (ASSUMED, standard). In the lattice case it is exactly `δ − 1/N + Δ_zG`.

**S4 (CHECKED D.d).**
- **Enumeration.** Exact integer enumeration of all contents on each lump (up to `6⁸`). Site factors are the products of absence factors over each record's empty neighbours; bond factors are the isotropic `ω`.
- **Symmetry.** The cube's corner directions follow from its symmetry (each corner's stabiliser is a 3-fold rotation about its diagonal). Their signs and sizes are computed.

## 3. The first failing step

- **The massless modes in (c)** need a continuous content (the sphere reading). On the six-axis menu the ordered phase has no massless modes; the tilt is gapped and the interaction short-ranged.
- **The route "direction-dependent rules give 1/r"** fails at S3: every covariant linear coupling of occupancy to the tilt carries a derivative.

## 4. What would finish it

1. **A lump's halo** in a medium with direction-dependent rules: the long-range part of the content field around a hedgehog lump, which (c) makes dipolar in an ordered medium.
2. **Whether any rule couples occupancy to a massless scalar without a derivative.** That is the only route to `1/r`. By covariance it needs a scalar massless mode, which the content order does not supply.

## 5. Running it

```
python3 probes/work/derive/source-direction-dependent-rules/w-macbookpro90c72-ja4f1/check.py
```

The run takes about 8 s. It prints four exact checks and one floating-point note, then the SUMMARY and HIT lines.
