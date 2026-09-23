# The field energy and the disturbances under the exchange maps — attempt 2

Worker `w-jonathonsmac4f50-j40bc`, model `claude-opus-5-5`. Task `J:derive:the-field-energy-and-the-disturbances-under-the-exchange-maps:a2`.

**Provenance.** Blocks 62, 64 and 68 to 74 were written by the same model family (Claude Opus). They are open and unrefereed; I restate what I use. There were no prior attempts at claim time.

**Scope.** This works within the supplied clauses of blocks 54 to 75. Nothing is adopted. The parked decisions are untouched. No gravitational claim is made. Block 64's family is a continuum family at leading order in the wave vector. Part (a) is therefore stated in weak-field plane-wave symbols, as block 64 T2 to T4 are. The curls and every operator identity are exact on the lattice.

**Notation.**
- `d_j = (−1)^{n_j}`, `D = diag(d)`, `s_n = det D`.
- `B_a^j` is the strain on the bond from `x` along `a`, with component `j`.
- Block 70: under reach two, species `n` sees `B` as `B D`. Under reach three the strain is unchanged. The frame goes to `ρEρ`, with `ρ = s_n D`.

## 1. The exact statement attempted

**(a) The field energy under `B → B D` (reach two).**
- **The curls.** Every plaquette curl goes to `F^j_ab d_j`, exactly on the lattice. `T₁` is unchanged; `T₂`, `T₃`, `ε·T`, `det e` and the divergence term are not.
- **Species (000)** sees the curvature member.
- **Species (111)** sees the same quadratic member, `(c₁, c₂, c₃) = (1/4, 1/2, −1)` in `D*`'s normalisation. But the first-order divergence term, which multiplies the rates, has the opposite sign: `c₄ → −c₄`. Its member is not blind, and block 64 T4's exponent is `β = −1` for it. A ray's bending over a slow body's fall, `1 + β`, is therefore 0 for species (111).
- **The six species with `|n| = 1, 2`** see a density that is **not in the family at all**:
  - no `(c₁, c₂, c₃)` reproduces its quadratic part;
  - its rate coupling is not a multiple of species (000)'s;
  - on an isotropic stretch `λ` the rate coupling is `Σ_a d_a ∂_a²λ − (Σ_a d_a) Δλ`. For species (000) this is `−2Δλ`; for species (100) it is `−2∂_1²λ`, the second derivative along the reflected axis alone.
- So under reach two the species that source a common strain field disagree about the member. Only (000) sees the curvature member.

**(b) Block 62's disturbances.** The vertex of species `n` with a metric disturbance `h` is:
- **frame coupling:** `D h D`, i.e. `h_ij d_i d_j`. The shear components with `d_i ≠ d_j` flip. For a TT wave along `z`, species with `d₁d₂ = −1` see the × polarisation reversed.
- **reach two:** `(hD + Dh)/2`, i.e. `h_ij (d_i + d_j)/2`. Species do not couple to components with `d_i ≠ d_j` at all, and diagonal components carry the sign `d_i`.
- **reach three:** `h`, for every species.

Each coupling is a hermitian generator, so the ledger of walker plus field is kept in every exchange of energy. What differs between species is the sign, or the presence, of a vertex. Emission by species `m` and absorption by species `n` therefore carry the relative factor `(d_i d_j)^{(m)} (d_i d_j)^{(n)}` in the frame coupling, and vanish under reach two whenever either species has `d_i ≠ d_j`.

**(c) Reach three.** Every species sees the same strain and the same field energy `F[B]`, and sources it with `s_n K`: the same response, up to the sign of its energy (block 71). The energy density maps to `s_n e` in any rate field. With block 72's `fP_j → s_n fP_j`, block 66's identity holds for species `n` iff it holds for (000).

**The task's HIT condition (a disagreement under reach three) does not arise.**

## 2. Steps

### Step 1 — the curls (PROVED; CHECKED 1.1)
`F_ab^j = d_a B_b^j − d_b B_a^j` is linear in `B` and does not mix components. So `B → B D` gives `F^j_ab d_j`, for every species. Checked symbolically with lattice shifts.

### Step 2 — the family per species (PROVED; CHECKED 2.1–2.7)
- **The terms.** `T^j_ab → d_j T^j_ab`. Then:
  - `T₁ = Σ|T^j|²` is unchanged (2.1);
  - `T₂ = Σ T^j_kl T^l_kj` picks up `d_j d_l`;
  - `V_b = Σ_a T^a_ab` picks up `d_a` inside the sum;
  - `ε·T` picks up `d_j`.
- **Species (000)** (2.2): as a function of the species' own strain `B' = B D`, the member `D*[B'D]` is `c₁T₁ + c₂T₂ + c₃T₃` with `(1/4, 1/2, −1)`, and the rate coupling is unchanged.
- **Species (111)** (2.3): `D = −1`, so `d_j d_l = 1` and `V → −V`. The quadratic part is the same member. The first-order divergence `∂_b V^b`, which multiplies the rates (block 60: `a = −2c₄`), changes sign: `c₄ → −c₄`.
- **The exponent (2.6).** Block 64 T4 gives `β = c₄/(4c₁ + 2c₂ + 4c₃)`: 1 for the blind member `(−1/8, −1/4, 1/2, 1)`, and −1 for (111).
- **Mixed species (2.4).** Solve for coefficients monomial by monomial in the plane-wave amplitudes and the wave vector. For the six mixed species, the equations for `(c₁, c₂, c₃)` have no solution, and neither does the equation for a multiple of species (000)'s rate coupling.
- **The rate coupling on an isotropic stretch** `B' = λ·1` (2.5): it is `Σ_a d_a ∂_a²λ − (Σ_a d_a)Δλ`. That is `−2Δλ` for (000), `+2Δλ` for (111), and `−2∂_1²λ` for (100).
- **`ε·T`** is unchanged for (000) and reversed for (111). In the member `c₅ = 0`, so it has no effect (2.7).

### Step 3 — the TT disturbances (PROVED; CHECKED 3.1, 3.2)
- **Frame:** `E → ρEρ` gives `h → D h D`, since `ρ = s_n D` and `s_n² = 1`.
- **Reach two:** the metric species `n` sees is `(1 + BD)ᵀ(1 + BD) = 1 + BD + DBᵀ + O(B²)`. With a symmetric strain `B = h/2` this is `(hD + Dh)/2` (3.1).
- **Reach three:** `h`.
- **A TT wave along `z` (3.2).** Components `(a, b)` for `+` and ×:
  - frame: × is multiplied by `d₁d₂`;
  - reach two: × vanishes for `d₁ ≠ d₂`, and the `(0,0)` entry is `d₁ a`. So for `d₁ = d₂ = −1`, + is reversed; for `d₁ ≠ d₂`, + turns into a pure trace.
- **The books.** Each coupling is hermitian, so the ledger is kept. The species differ only in sign, or in the absence of a vertex.

### Step 4 — reach three is species-blind (PROVED; CHECKED exactly 4.1–4.5)
- **The strain (4.1, 4.2).** On a `4³` torus with an integer strain field, `V_n H₃[B] V_n† = s_n H₃[B]` for all eight species. `V_n H₂[B] V_n† = s_n H₂[B D]` reproduces block 70.
- **The response (4.3).** The reach-three response `K_a^j` maps to `s_n K` at every bond sampled.
- **In a rate field (4.4).** With an integer `φ`, the energy density maps to `s_n e` at every site: `V_n` is site-diagonal and commutes with `φ`.
- **The field equations.** The field energy `F[B]` is a function of `B` alone, and every species' source maps into the same source up to `s_n`. So the field equations for `B` are the same for every species. The sign `s_n` is block 71's sign for negative-energy twins, not a disagreement.
- **Block 66's identity.** It is `∂_a K^a_b = e ∂_b u` at leading order (block 72 for `fP`). It therefore holds for species `n` iff it holds for (000) (4.5).

## 3. Where the route stops

No claimed step fails. Part (a)'s disagreement is a statement at leading order in the wave vector, like block 64's family. The mixed species' densities are not placed on the lattice.

## 4. What would finish it

1. A lattice placement of block 64's contractions. This would turn Step 2 into lattice statements. Block 64 N1.3 says no placement is known to be exactly blind to coin rotations.
2. The reach-three member of block 64's family: its blindness conditions with `K` as the source, redone with block 69's two-step momentum.
3. An owner's decision between reach two, where the species disagree about the member, and reach three, where they agree (block 74's "reach three serves all eight").
