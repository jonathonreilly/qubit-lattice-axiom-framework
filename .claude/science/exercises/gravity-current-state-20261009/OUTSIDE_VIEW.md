# Step 5: outside view

The agent was Claude Opus 5.5 (same family) with live web access. "V" means the agent fetched the source; "M" means it is cited from memory and unverified. The agent's full return is summarized here, and its scripts are in `scripts/LIT_*`.

## The headline (reading, supported by sources)

**The wall is a known case, not new physics.** Coupling a metric to a medium whose points carry fixed spatial labels (a "solid", with Goldstone fields φ^i) gives Lorentz-violating massive gravity. The graviton's TT mass m₂ comes from the medium's shear stiffness.
- **Rubakov; Rubakov–Tinyakov** (hep-th/0407104; arXiv:0802.4379, V). The TT mass is m_G = m₂ (eqs. 74–75). A Goldstone medium φ^i = Λ²x^i gives m ~ Λ²/M_P (eq. 91).
- **Dubovsky** (hep-th/0409124, V). Classifies the masses. Healthy regions need tuning unless a residual diffeomorphism subgroup enforces them.

The framework's Z³ labels are exactly the φ^i. K3a″'s and W1's TT modulus is m₂².

**Three known ways to keep the graviton massless:**
1. exact gauge redundancy, as in GR;
2. no spatial labels at all: the ghost condensate, or a Hořava-type foliation that keeps spatial diffeomorphisms;
3. labels with a **continuous, volume-preserving relabelling symmetry**, i.e. a fluid.

The fixed Z³ grid has only a finite label symmetry (Z³ ⋊ O_h), so the stiffness is generic and expected from power counting. It is not an accident of the K3a″ and W1 models.

## Checks run by the agent and reproduced by the supervisor

**The medium's TT mass** (`scripts/LIT_tt_mass_medium.py`, output beside it).
- **The setup:** L = √g F(Y^{ij}) with Y = g^{ij}, at a zero-stress background under a static TT perturbation.
- **A generic isotropic solid** gives a TT mass coefficient (F₁ + 4F₂)(a² + b²) ≠ 0.
- **A fluid**, F = F(det Y), gives exactly 0.
- **So:** volume-preserving relabelling symmetry protects m₂ = 0, and a finite symmetry does not (CHECKED, sympy).

**The size.**
- **The estimate:** m_g ≈ √μ·a⁻²/M_P with μ ≈ 9e-4 per cell (K3a″'s O(e²) value). At a = l_P that is m_g ≈ 4e26 eV, about 1.5e49 times the GWTC-3 bound.
- **No way out by coarsening:** staying under the bound needs a⁻¹ ≲ 3 keV, which collider and Lorentz-violation data exclude. The scale primitive P2 cannot rescue it (CHECKED arithmetic; reading on exclusion).
- **Tuning (S6)** means m² tuned to about 1e-98 of its natural size.

## Key sources (abridged)

| Source | What it shows | Maps to the repo? | Citation |
|---|---|---|---|
| Rubakov–Tinyakov; Dubovsky | A Lorentz-violating mass taxonomy; the solid medium gives m₂ ≠ 0; the ghost condensate keeps the graviton massless | **Directly: this wall is an instance** | arXiv:0802.4379; hep-th/0409124 (V) |
| Collins–Perez–Sudarsky–Urrutia–Vucetich; Polchinski | A Planck-scale preferred frame gives percent-level Lorentz violation unless tuned; supersymmetry is the exception | Yes. **The graviton twin is worse**: m₂²h² is a *relevant* operator (dimension 2), so no IR attractor helps (suggested) | PRL 93, 191301; arXiv:1106.6346 (V) |
| Weinberg–Witten; Weinberg soft-graviton theorem | No massless spin-2 with a covariant conserved T^μν. Masslessness plus Lorentz invariance forces universality | For an emergent graviton: with IR Lorentz invariance it must be a gauge mode, not a matter composite | PLB 96 (1980) 59 (V via Carlip); PR 135 B1049 (M) |
| Carlip, "Challenges for emergent gravity" | A lattice needs "infinitely many neighbours" for Lorentz invariance | Restates the wall's faces | arXiv:1207.2504 (V) |
| Arkani-Hamed–Schwartz | A gravitational dimension discretized with nearest-neighbour links gives massive gravitons and low strong coupling | A close analogue of L1 | hep-th/0302110 (V) |
| Bahr–Dittrich; Roček–Williams; Hamber | Perfect actions restore gauge symmetry but are non-local. Flat linearized Regge has exact zero modes (matches W2). Regge needs a tuned G_c | The W option | arXiv:0907.4323 (V) |
| Wetterich | A position-blind lattice action gives continuum diffeomorphism invariance, with the metric as a collective field | The escape already logged; no gauge fields shown | arXiv:1110.1539 (V) |
| Volovik; Klinkhamer–Volovik q-theory | Equilibrium gives a **first**-derivative condition (the tadpole cancels), with compressibility ≥ 0. Shear is not treated | **Answers ledger row S6: it cancels the tadpole only, never a modulus** | arXiv:0711.3170; arXiv:1812.07046 (V) |
| Kleinert; Kleinert–Zaanen | A world crystal whose dislocations condense becomes a "world nematic", with gravity from curvature sources | The liquid-like-vacuum escape. In the framework a dislocation is a change of adjacency, which is L1 | gr-qc/0307033 (V) |
| Pretko–Radzihovsky; Pretko | Elasticity–fracton duality. The crystal's gapless modes are helicity-1 phonons. Fracton "gravitons" exist but are non-Lorentzian | Phonons give the stiffness's speed, not a TT mass | PRL 120, 195301 (V) |
| Hořava; Blas–Pujolàs–Sibiryakov | Foliation-preserving diffeomorphisms keep the tensor massless, with an extra scalar and strong coupling | **The protecting symmetry, spatial diffeomorphisms, is exactly what fixed Z³ breaks** | JHEP 0910:029 (V) |
| Bombelli–Henson–Sorkin; CDT | A Poisson sprinkling picks no frame, but a finite-valency graph attached to one cannot be Lorentz invariant. CDT sums over adjacency | Z³ with nearest neighbours has finite valency, so Lorentz violation is unavoidable; the shear modulus is its graviton face | gr-qc/0605006 (V) |
| Gu–Wen; Xu; Barceló–Liberati–Visser; Sindoni | Qubit gravitons with k³ or k² dispersion. Analog gravity gives kinematics only | Covered 09-29; background | arXiv:0907.1203 etc. |

## Mathematical lenses

| Lens | Object that changes | Invariant or theorem type | First artifact |
|---|---|---|---|
| Invariant theory on lattice-shape space SL(3,Z)\SL(3,R)/SO(3) | The vacuum energy E(Y) under uniform strain | A "protected zero" holds iff E is constant on shape space. Any periodic lattice sum is non-constant (suggested) | The E and T₂ Hessians of an Epstein zeta at Z³ |
| Goldstone / Stückelberg EFT | The internal symmetry G of F(Y) | m₂ = 0 for every F at zero stress iff G ⊇ SL(3): checked in one direction, plus a generic counterexample | Extend to an O_h-only F |
| Graph automorphisms | The rule's covariance group | Aut(Z³) = Z³ ⋊ B₃ is finite, so no continuous relabelling exists (standard) | A one-line lemma |
| Power counting / RG | Operator dimension | m₂²h² is relevant, so it scales like Λ⁴/M_P². No IR attractor (suggested) | — |
| Point processes | Poisson–Delaunay sites | A Poisson process under a volume-preserving map is the same process in law, so the ensemble-averaged E is shape-blind | **A free scalar on a 3D Poisson–Delaunay graph: frozen adjacency (a glass, expect ≠ 0) versus adjacency re-triangulated from the deformed points (expect 0)** |

## Reframes

| Reframe | What moves | First test |
|---|---|---|
| Pre-record vs recorded | Geometry held only in the admissibility odds is still covariant only under Z³ ⋊ O_h, so it responds to strain like a solid (suggested) | The uniform-strain Hessian of a nearest-neighbour odds family |
| Dynamics vs kinematics | Analog models give a kinematic metric for free; the wall is the TT mass, which is pure dynamics | none new |
| Fixed vs dynamical substrate | Every known protection is label-blind. **The requirement is not just "dynamical adjacency" but adjacency recomputed from the geometry, which makes the vacuum a fluid** | the Poisson–Delaunay toy |
| Local vs collective | A collective medium mode is Stückelberg, so m₂ is generic. A gauge mode needs an exact rank-2 Gauss constraint, which hits the 09-29 finite-slot no-gos | Find the lattice generator of any candidate's TT redundancy |
| Obstruction vs missing input | The wall is a **missing symmetry** (SL(3) relabelling or spatial diffeomorphisms), not a new obstruction | — |
