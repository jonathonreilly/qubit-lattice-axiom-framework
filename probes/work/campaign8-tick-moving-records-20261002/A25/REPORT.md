# A25 report: can the spin-2 ("shape") field be ticked in real space with nearest-neighbour moves that respect the grid's turns?

**Scratch directory:** `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A25/`

| File | Content |
|---|---|
| `stag2.py` | Shared builder for the real-space operators: staggered, central and one-sided layouts; Bloch symbols; rotation maps |
| `check_hp.py` → `out_hp_L6.txt`, `out_hp_L4.txt` | Staggered (h,π) tick, parts P1–P9 |
| `check_cp.py` → `out_cp_L4.txt`, `out_cp_L3.txt` | Curl-split (C,π) tick on the Z³ parity-role lattice, parts Q1–Q5 |
| `check_colloc.py` → `out_colloc.txt` | Unstaggered alternatives, parts U1–U7 |
| `limits.py`, `check_limits.py` → `out_limits.txt` | Limiting gauge spans at the zone corners; generator-family search |
| `check_search.py` → `out_search.txt` | Wilson-term r-scan. Its own span measure is superseded by `limits.py` |
| `inspect_opt.py` | Diagnostic of one search optimum |
| `time_out_*.txt` | Run statistics |

**Grades**
- **EXACT**: a proof, or an exact matrix identity. With τ = 1/2 every entry is dyadic, so "0.0" is exactly zero in floating point.
- **CHECKED**: a numeric check with the tolerance stated.
- **ARGUED**: reasoning without proof.
- **COMPARATOR**: literature quoted from memory, unverified, never adopted.

**Scope.** Everything here is a supplied linear toy, a classical real field. Nothing is framework content. Repo reading was read-only: `git show origin/main:` at e485eab6b0. There were no edits and no git operations.

---

## 1. Question

**Decisive test 3 (A23).** Is there a real-space version of A23's spin-2 leapfrog tick in which:
- **(a)** every layer is nearest-neighbour, or of minimal reach;
- **(b)** each layer is covariant under the 24 proper rotations about vertices, with role relabelling allowed (and if so, in what precise sense);
- **(c)** the linearized momentum and Hamiltonian constraints are preserved to round-off, layer by layer;
- **(d)** A23's dispersion is reproduced: two tensor polarizations at z = 1, no doublers, no extra modes?

Also: does an **unstaggered** form exist that is exactly covariant, doubler-free and exactly gauge-invariant?

## 2. Answer

**Conditional yes for the staggered construction (EXACT/CHECKED), at the price of a role pattern. For the standard gauge symmetry, no unstaggered form exists (EXACT). Lattice-modified gauge symmetries are open.**

**The construction (a "Yee for spin-2").**
- h_ii, π_ii sit at vertex roles; h_ij, π_ij at face roles.
- In the curl-split form, C = curl h sits at edge and cube roles.

**How it meets (a)–(d).**
- **(a)** Every layer is a shear. On Z³ parity roles, the curl-split layers are strictly face-nearest-neighbour.
- **(c)** Every layer preserves the momentum and Hamiltonian constraint rows by exact matrix identities.
- **(d)** Its real-space Bloch symbol equals A23's to 1.3e-15. That gives exactly 2 tensor polarizations at z = 1, no spatial or time doubler, and no extra propagating mode.
- **(b)** Each layer commutes exactly with all 48 cubic transformations about every site, in this sense: components are relabelled by the tensor rule, and the role pattern is carried along (𝒪 L_s 𝒪⁻¹ = L_s′).

**What the grid does not fix.** Which of the **8 role translates** the state uses. This is a conserved state label, the same 8 as the repo's U(1) role compiler. It is not a law-level schedule, as A16 found for matter.

**Unstaggered forms.**
- With symmetric differences, the theory is **exactly 8 decoupled copies of the staggered one, one per role translate**: 7 doublers.
- For any collocated, covariant gauge symmetry of the standard (symmetrized-gradient) form, every gauge-invariant potential vanishes at the zone corner (π,π,π). That is a doubler.
- Patches (a Wilson-type term, one-sided differences) lose exact gauge invariance. They also turn unstable or lose covariance.
- Lattice-modified gauge generators are not excluded by representation theory. Lemma C (S14) forces them to vanish on the zone edges, and no tested member passed. Open.

## 3. Derivation

### 3.0 Named conditionals

- **F1–F5 as in A23.** In particular F1: field possibilities are never locked, and F4 gives GR's kinetic weights.
- **New, F6 (role pattern).** The shared possibilities carry period-2 role labels: one of 8 translates, never changed by the dynamics. This is a choice not fixed by the supplied structure, so per Qualification it stays a named conditional.

### 3.1 Staggered real-space operators (task 1)

| Step | Content | Grade |
|---|---|---|
| S1 Layout | See the layout list below. | EXACT |
| S2 Operators | See the operator list below. | EXACT |
| S3 Lattice identities | See the identity list below. | EXACT; CHECKED 0.0 at L = 4, 6 |
| S4 Symbol | The real-space Bloch blocks equal A23's symbols: V_EH(s) to 1.3e-15, DeWitt M to 4.4e-16, the whole tick to 6.7e-16, over all 216 momenta of L = 6. A23's symbol-level D15 is therefore realized exactly in real space. | CHECKED |

**S1 Layout.**
- Vertex spacing is 1.
- h_ii, π_ii sit at vertices x; h_ij, π_ij (i<j) at face centres x+(e_i+e_j)/2.
- The gauge vector ξ_i, and the momentum-constraint row it generates, sit at edge centres x+e_i/2.
- The Hamiltonian row (lapse) sits at vertices.
- C = curl h: C_ll at cube centres; C_lj and C_jl at the edge centre x+e_m/2, where m is the third axis.
- **"π dual"** means π_ij lives on the dual cell of h_ij's element, which has the same centre, so the kinetic layer is on-site. The field that lives on the dual positions (edges, cubes) is C, which plays B's role in Yee.
- Every derivative is one half-step difference. The builder asserts that every term of every operator lands on a single role.
- In the half-shift Fourier convention every difference has symbol i·s_k with s_k = 2 sin(k_k/2). So every continuum identity holds exactly with k → s.

**S2 Operators.**
- Gauge generator: (Dξ)_ii = 2∂_iξ_i, (Dξ)_ij = ∂_iξ_j + ∂_jξ_i.
- Curl: C_lj = ε_lki ∂_k h_ij.
- Potential: V = ¼ Σ C:Cᵀ = ¼ Σ_cubes Σ_l C_ll² + ½ Σ_edges Σ_{l<j} C_lj C_jl.
  - By summation by parts this equals ¼ h:inc(h) = ½ h:G_lin(h), the linearized Einstein–Hilbert potential.
- Kinetic term: H_kin = π:π − ½(tr π)², i.e. ḣ_ij = 2π_ij − δ_ij tr π. These are A23's weights (−½, 1, 1).
- Momentum row: Dᵀp = −2 ∂_jπ_ij.
- Hamiltonian row: R(h) = ∂_i∂_jh_ij − ∂² tr h.

**S3 Lattice identities.**
- 𝒱D = 0: exact gauge invariance.
- RD = 0.
- R𝓜 = −Div·Dᵀ: the Hamiltonian row propagates into the divergence of the momentum row.
- div₁C·Curl = 0 and trC·Curl = 0 (Bianchi).
- R = R_C·Curl, with R_C = −ε_ikl ∂_k C_il.
- Dᵀ(½ CurlᵀJ) = −½ CurlVᵀ div₁C.

### 3.2 Two tick forms (tasks 1–2)

| Step | Content | Grade |
|---|---|---|
| S5 (h,π) tick | See the bullets below. | EXACT; CHECKED |
| S6 Curl-split tick | See the bullets below. | EXACT; CHECKED |
| S7 Placing the field on Z³ sites | See the bullets below. | CHECKED |
| S8 Dispersion | See the bullets below. | CHECKED |

**S5, (h,π) tick: K(τ/2)·P(τ)·K(τ/2).**
- K: h += a𝓜π. This is on-site: it mixes the 3 diagonal components at a vertex.
- P: π −= b𝒱h. This is a second difference: Euclidean reach 1, with 10 inputs for vertex rows and 15 for face rows.
- Constraints:
  - P leaves Dᵀπ unchanged, because 𝒱D = 0.
  - K changes Rh by −a·Div(Dᵀπ), which is zero on the momentum-constraint surface.
- On a constraint-surface trajectory (200 ticks × 3 layers), both rows stay at 1.1e-13 / 8.5e-14 relative.
  - h drifts only along pure-gauge directions.
  - The gauge-invariant force 𝒱h stays O(1).
- U(−τ) = U(τ)⁻¹ exactly. Time reversal π → −π follows from the palindromic schedule.
- The local form E_τ = ½h𝒱h + ½π(𝓜 − τ²/4·𝓜𝒱𝓜)π is conserved exactly. It is positive on the tensor sector iff τ < 1/√3. It is indefinite on the conformal direction, which the constraints remove, as in GR.

**S6, curl-split ("Yee for spin-2") tick: C(τ/2)·π(τ)·C(τ/2).**
- C += a·Curl𝓜π, then π −= b·½CurlᵀJC.
- It intertwines exactly with S5: C(t) = Curl h(t), CHECKED to 2.5e-12.
- Constraints:
  - The C-rows (div₁C, trC) are preserved by every layer.
  - The momentum row is preserved iff div₁C = 0.
  - The Hamiltonian row written on C is preserved iff the momentum row vanishes.
- Spectrum: 15 eigenvalues per k, namely 11 unit ones plus 2 tensor pairs. CHECKED with power traces to 2.2e-13.

**S7, placing the field on Z³ sites.**
- **S2 parity roles** (the U(1) role compiler's encoding): role r(y) = (y+s) mod 2.
  - Weight 0: vertex (π_ii). Weight 2: face (π_ij). Weight 1: edge (C_lj, C_jl). Weight 3: cube (C_ll).
- **Curl-split on S2.** Every layer depends only on the site and its face-neighbours (Manhattan 1).
  - C outputs and π_ii outputs depend on 4 opposite-role neighbours; π_ij outputs on 6.
  - The C-layer updates exactly one checkerboard colour and the π-layer the other.
  - The composed tick has reach 3, as in the U(1) Yee template.
- **(h,π) form on S2:** the P-layer has Manhattan reach 2.
- **S1 "ownership" storage** (each site stores its vertex plus its three "up" faces): the P-layer has Chebyshev reach 1, Manhattan 2.

**S8, dispersion.**
- Tensor phases satisfy cos θ = 1 − τ²ŝ²/2 to 5.4e-16.
- There are exactly 4 non-unit eigenvalues (2 polarizations) at each of the 215 momenta k ≠ 0 at L = 6.
- θ/(τ|k|) = 0.99999999 at |k| = 1e-3: z = 1, speed 1.
- The smallest phase at k ≠ 0 is 2 asin(τ|s|_min/2) = 0.5054 > 0. Since ŝ = 0 only at k = 0, there is no doubler.
- Maximum phase: 2π/3 at τ = ½, and 0.9099π at τ√3 = 0.99 (tensor-block |eig| = 1.000000000000). At τ√3 = 1.01 the tick is unstable (|eig| 1.3266).

On minimal reach (ARGUED): the h-layer is on-site, and a nontrivial tick cannot be. An exactly gauge-invariant potential is built from the curl and pairs only co-located curl components. Its force stencil is two half-step differences, the smallest possible for a second-order operator.

### 3.3 Covariance and what is privileged (task 3)

**S9, precise sense of covariance** (EXACT by construction; CHECKED to 0.0):

1. **Geometric frame.** Let 𝒪_R move each component to its rotated position and relabel it by the tensor rule: ij → P(i)P(j) with sign σ_iσ_j, with C as a pseudo-tensor under reflections.
   - About a vertex or a cube centre, for all 48 signed permutations, 𝒪_R commutes exactly with each layer and with D and R.
   - About a face or edge centre, only 16 of 48 (8 of 24 proper) map the geometry onto itself; those commute too. The rest map the staggered geometry onto a half-shifted copy.
2. **Z³ sites with role labels in the site content.** For every site c (all 8 role classes) and all 48 transformations, 𝒪 L_s 𝒪⁻¹ = L_s′ exactly, with s′ = (R(s−c)+c) mod 2. Unit translations send L_s to L_{s+e}, and all 8 translates are reached.
   - The pattern s itself is kept by all 48 transformations about vertex- and cube-role sites.
   - It is kept by 16 (8 proper) about face- and edge-role sites.
   - It is kept by the translations in 2Z³.
3. **Not covariant: on-site relabelling with fixed storage (S1).** Only 3 of 24 proper rotations commute: the identity and the two 120° turns about the (1,1,1) diagonal. That storage privileges an octant.

**S10, what is privileged** (EXACT that the label is conserved; ARGUED for the comparison):
- The law sees roles only through labels. The only thing the lattice leaves unfixed is which parity class carries the vertex role: 1 of 8 translates (F6).
- The dynamics never changes roles, so the pattern is a conserved, superselected state label.

**Comparison with A16 (matter, A10's round).**

| | Matter (A10/A16) | Field (this report) |
|---|---|---|
| Where the privilege sits | In the law's schedule | In the state: 1 of 8 role translates |
| Site-centred quarter turns | Match only the reversed round | Map the schedule to itself exactly (no reversed round, no restart) |
| Odd translations | Match no restart | Map L_s to L_{s+e} exactly |
| Visible in records? | Yes once records interact (TV 0.04–0.39) | Only through records formed by matter that couples to role-dependent field components (ARGUED) |

- The field's schedule C/2–π–C/2 is palindromic and defined by roles.
- Under F1, field possibilities are never locked, so the pattern never enters records directly.
- Both structures are the same 2×2×2 = 8 blocks. Whether matter's sublattices and the field's roles could be one shared choice is open.

**S11, the taste identity** (EXACT; CHECKED |𝒱_c − ¼Σ_s E_s𝒱E_sᵀ| = 0.0):
- The collocated symmetric-difference theory on Z³ (side 2L) is exactly the direct sum, over the 8 role translates, of the staggered theory, with V/4, D/2 and the same 𝓜.
- Its potential vanishes identically at exactly the 8 zone corners. Near each corner there is a full second massless graviton (4 phases with θ/(τ|q|) = 1).
- So "no role privilege" with symmetric differences means all 8 patterns at once: 8 gravitons.
- COMPARATOR: the Kawamoto–Smit spin diagonalization of staggered fermions; this is the bosonic tensor analogue.

**Relation to A21's Theorem N** (ARGUED): the construction lies outside Theorem N's premises, because the payload exceeds one qubit and the role labels are part of the site content. It realizes A21 C22's escapes 2 (supplied pattern) and 3 (more than one qubit per site). There is no contradiction.

### 3.4 Unstaggered alternatives (task 4)

| Step | Content | Grade |
|---|---|---|
| S12 Theorem A | See the statement below. | EXACT |
| S13 Representation theory at the corners | See the bullets below. | EXACT (characters) |
| S14 Lemma C | See the statement below. | EXACT |
| S15 Necessary condition | See the statement below. | EXACT, assuming a bounded kinetic term |
| S16 Modified generators | See the bullets below. | CHECKED for this family only; OPEN in general |
| S17 Patches | See the bullets below. | CHECKED |

**S12, Theorem A.** Suppose h and ξ are collocated, and δh = gξᵀ + ξgᵀ for any local g(k) that is covariant under the 12 tetrahedral rotations about a site. Then g(π,π,π) = 0. And every exactly gauge-invariant local potential has V(π,π,π) = 0 on all six directions, so there are zero-frequency non-gauge modes at the corner: a doubler.

Proof:
- (π,π,π) is fixed by every rotation, so g there is an invariant vector, hence 0.
- The set of limit directions of g/|g| is invariant under the rotations and spans C³, because the vector representation T1 is irreducible.
- Continuity gives V(K)(nξᵀ + ξnᵀ) = 0 for every such n. Linearity extends this to all n.
- Those matrices span all symmetric tensors, so V(K) = 0.

The same proof shows that **every** collocated, covariant, gauge-invariant photon (δA = gλ) has a doubler at (π,π,π).

**S13, representation theory at the corners.**
- **Collocated, at (π,π,π):** ξ transforms as T1 and h as A1 + E + T2. There is no common irrep, so **every** O-covariant collocated generator vanishes there, not only the symmetrized ones.
- **Collocated, at the (π,0,0) and (π,π,0) corners:** with reflections (O_h), the generator also vanishes there (Hom = 0). Under O alone, Hom = 1: a parity-odd "crossed" map (ξ₂→h₁₃, ξ₃→h₁₂).
- **Staggered (the half-step offsets twist the corner action):** h becomes 2(A1+E) and ξ becomes A1+E. Hom = 4, so the gauge orbit stays non-degenerate (s = (2,2,2)).
- Staggering moves the components to different lattice positions, and that changes how the grid's turns act at the corner. COMPARATOR: band representations in topological quantum chemistry.

**S14, Lemma C.** In an O-covariant collocated theory, suppose the generator acts nontrivially on (ξ₁,ξ₂) anywhere on the zone edge (π,π,t). Then V(π,π,π) vanishes on all of T2, and the h₁₂-type tensor mode is gapless at (π,π,π).

Proof:
- On the edge, the 90° turn forces D(ξ₁,ξ₂) to lie in span(h₁₃,h₂₃).
- Hence V annihilates h₁₃ and h₂₃ along the whole edge, and by continuity at the corner.
- At the corner, the kernel of V is O-invariant and contains a T2 vector, so it contains all of T2, including h₁₂.
- Along the edge, h₁₂ lies outside both the gauge orbit and the Hamiltonian row.

So a doubler-free collocated theory needs a generator that vanishes on the transverse components along all three zone edges.

**S15, necessary condition.** At a degenerate momentum K, define S_K as the span of all limiting gauge directions. If dim S_K ≥ 5, a physical, constraint-satisfying direction has zero potential at K.

**S16, modified generators.**
- 7 named covariant members, plus a 250-sample + Nelder–Mead search over a 9-parameter family.
- None meets dim S_K ≤ 4 at all three corner classes.
- Robust patterns of dim S_K at [(π,0,0), (π,π,0), (π,π,π)]:

| Member | dim S_K |
|---|---|
| central | [6,6,6] |
| own-direction smearing c₂_j | [6,5,3] |
| double smearing c₂_j c₂_m | [5,5,3] |
| chiral | [5,5,6] |
| smear + chiral | [4,5,6] |
| smear2 + smeared chiral | [3,6,3] |
| smear2 + smeared diagonal | [3,5,6] |
| best search optimum | [4,3,6] |

- Among the 126 covariant range-2 potentials, each tested generator admits exactly one gauge-invariant form. Its common kernel is ≥ 5 at some corner.
- Not excluded by representation theory. Topology gives no obstruction (ARGUED): the gauge-orbit bundle around k = 0 has w₂ = 0.

**S17, patches.**
- **Covariant Wilson-type term**, order k⁴:
  - Gauge invariance breaks: |(V+W)D| = 4.25 at r = ¼.
  - All 12 directions become dynamical, against 4 for the gauge-invariant tick.
  - It is unstable: max|eig| = 1.41, 2.13 and 4.79 at r = 0.01, 0.05 and 0.25; the traceless-only version gives 3.73.
  - The momentum row reaches 7.6e11 in 20 ticks.
- **One-sided differences:** gauge invariance breaks (|V_f D_f| = 1.0), and only 6 of 24 rotations survive (the body-diagonal group).

## 4. Checks

**How every run was made:** numpy/scipy, `nice -n 10`, all four thread caps at 1, perl alarm at 58 s. Machine load was about 2.4–4.

| Script | Run | Key numbers | Tolerance |
|---|---|---|---|
| `check_hp.py 6` (and `4`) | 0.79 s, 84 MB | P1 identities 0.0; P2 Bloch vs A23 1.3e-15 / 4.4e-16 / 6.7e-16; P3 4 non-unit eigenvalues at every k ≠ 0, power traces 9.7e-13, min phase 0.5054; P4 rows 1e-13 relative; P5 48/48 vertex and cube, 16/48 face and edge, exact; P6 reach table; P7 E_τ and inverse exact; P8 z = 1 (0.99999999), plane wave 3.5e-13; P9 CFL at 0.99 and 1.01 | exact zeros; 1e-9 for phase counts |
| `check_cp.py 4` (and `3`) | 1.04 s, 68 MB | Q1 all identities 0.0; Q2 traces 2.2e-13, 4 non-unit eigenvalues per k; Q3 C = Curl h to 2.5e-12; Q4 Manhattan 1, Chebyshev 1, composed reach 3, two checkerboard colours; Q5 all 48 transformations × 8 site classes exact, pattern kept 48/48 (vertex, cube) and 16/48 (face, edge) | exact zeros |
| `check_colloc.py` | 1.54 s, 191 MB | U1 central differences exact, 8 zero-potential corners; U2 taste identity 0.0; U3 Wilson numbers; U4 one-sided and S1 storage; U5 Hom dimensions; U6 dim S_K; U7 1 gauge-invariant form per generator | exact zeros; SVD 1e-8–1e-9 |
| `check_limits.py` | 12.5 s, 75 MB | dim S_K for the 7 named members, stable at ε = 1e-3 and 1e-4; search | union threshold 0.05 (absolute) |
| `check_search.py` | 13.2 s, 75 MB | Wilson r-scan: 1.41 / 2.13 / 4.79 | — |

**First-run errors, fixed.**
1. My first corner-span count normalized by the largest singular value while stacking many random directions. That diluted limit directions that appear only along special approaches (axes, planes), and it undercounted. Example: double smearing at (π,π,0) read 3; the true value is 5. I replaced it with an absolute threshold on stacked orthonormal bases (`limits.py`); all dims above use it.
2. A parametrization 1 + a(F − 1) lost F < 1e-16 in floating point. I rewrote it as (1 − a) + aF.
3. The search objective at finite ε can be gamed by near-cancellations. One "optimum" scores 0 at ε = 1e-3 but reads [4,3,6] at ε = 1e-4, so the search is weak evidence only.
4. My first momentum-row identity guessed the wrong factor; the exact relation is −½ (Q1).
5. One search variant hit the 58 s alarm without output. It was cut down and then superseded.

**Not run (suggested next):** a search with exact structural parameters and symbolic Taylor expansion at the corners and zone edges (see §6).

## 5. Real-physics match

**At linear order, under F1–F6, the lattice tick gives:**
- exactly two tensor polarizations at z = 1;
- exact constraints;
- no doubler and no extra mode.

These are the requirements A23 matched to the comparators: GW polarization tests, GW170817 speed, γ = 1 and dragging via F2–F4.

**Lattice artifacts.** Dispersion and anisotropy enter at order (ka)², from ŝ² = k² − Σk_j⁴/12 + …, plus the τ² terms. With a at the Planck length, at 100 Hz: (2πf·a/c)² ≈ 5e-86 (EXACT arithmetic; scale identification ARGUED). Far below GW170817's ~1e-15.

**Falsifiers.**
- GW anisotropy or birefringence at accessible frequencies would demand a ≫ ℓ_P.
- Extra light graviton species would rule out the symmetric-difference unstaggered form, which predicts 8 tastes (ARGUED; COMPARATOR: light-species counting).
- Lattice-scale (period-2) effects of the role pattern on matter would be the visible trace of F6. They are invisible at long wavelength (ARGUED).

**Not determined here:** β, and the nonlinear lattice gauge algebra. On a fixed lattice, diffeomorphisms do not close beyond linear order (COMPARATOR: Regge calculus has only approximate vertex-displacement symmetry).

## 6. Open edges and next steps

1. **Payload (A23 (g), unchanged).**
   - A linear field needs unbounded local content: in the curl-split form, 3, 1, 2 or 3 reals per role.
   - It also needs a role label of 8 values, as in the U(1) compiler.
   - Compiling this into one qubit per site is open.
2. **Matter coupling with roles (A23 test 4).**
   - Does the coupling make the role pattern visible in records?
   - Can matter's 8 sublattices (A10/A16) and the field's 8 role translates be one shared choice instead of two?
3. **Lattice-modified collocated generators.** Open, with a sharpened target:
   - The generator must vanish identically on the transverse components along the zone edges (Lemma C, EXACT).
   - A further edge-line case analysis (ARGUED) leaves one shape: a T2-type limiting gauge structure on the edges, with traceless-diagonal tensor modes near (π,π,π).
   - Next: build that shape by hand, or by a symbolic, structure-exact search; then solve for V at range 2–3.
   - A band-representation proof attempt is the other route.
4. **Nonlinear order, β, and the closure of lattice diffeomorphisms** (A23 test 5).
5. **Quantum version** (oscillators per site) and its interplay with formation under F1/F5.

**What this asks the owner to decide (axioms' register):**
- Whether the shared possibilities may carry a fixed, never-changing pattern of jobs (1 of 8 layouts) as a named choice.
- Whether each place may hold more than one site's worth of settings.

## 7. Plain-language summary

The shape field can be moved forward tick by tick using only next-door steps, each step treating every turn of the grid exactly alike and keeping the field's bookkeeping exact at every step. The price is that the places of the grid must take fixed jobs in a repeating 2×2×2 pattern: some places hold the field's stretch parts, some its shear parts, and some the in-between parts that pass the change along. Nothing in the grid says which of the 8 possible layouts of this pattern is the real one; the rule treats all 8 alike, but any one world must have one, and it never changes. If every place is instead given the same job, the field comes out as 8 separate copies of itself, eight kinds of ripple where there should be one; this is proved for the usual way of keeping the bookkeeping, and patching it by hand breaks the bookkeeping and lets ripples grow without limit. Whether some unusual bookkeeping avoids both costs is still open, and each place would also have to hold more settings than one site's possibilities allow.