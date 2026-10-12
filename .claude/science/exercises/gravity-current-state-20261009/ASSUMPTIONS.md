# Step 2: the load-bearing assumptions; step 3: the first-principles reduction

**Shorthand.** "Pack" is `.claude/science/candidates/candidate-law-20261008/` on branch `claude/candidate-law-20261008`. Locations are given by file and section where a line number would be unstable, which is the case for files still being edited.

## Step 2: the ledger

| ID | Kind | Assumption, in plain words | Where the wall uses it | What if it is wrong? | Already tested? | Cheapest test | Changes an owner decision? |
|---|---|---|---|---|---|---|---|
| L1 | axiom (Lattice), read geometrically | The grid's neighbour structure is fixed, so the low-energy fields' momentum cutoff is fixed in label space | K3a″ and W1. The mechanism is in Pack `TEST_LOG.md`, W1 referee section (fixed window −1/(60π²) vs strain-following 0) | The TT modulus need not arise. A cutoff that follows the geometry gives 0 in the free IR cone | Only "cutoff follows strain" in the continuum control (about 1e-12). Never on a lattice whose adjacency can change | A toy whose neighbour structure rearranges ("liquid"): does its vacuum TT modulus vanish? | **Yes**: this is the Lattice axiom |
| L2 | axiom (Qubit) with the supplied finite-slot reading | Each site's possibilities are finite (M₂(C)) | The 09-29 partner and speed face (probes 10–21) | Continuous slots remove the partner face, but then L1's stiffness face bites (K3a″) | Yes (09-29; K3a″) | none new | Yes, but the stiffness face survives |
| L3 | axiom (Admissibility) plus supplied dynamics | The law is a local Hamiltonian or tick on fixed sites | everywhere | Non-local or non-Hamiltonian laws are untested | partly (A42; campaign 8) | — | maybe |
| L4 | axiom (Record) | Records are permanent and one per site | FR1 and FR3 (record-carried gravity) | Moving records: FR3 is running | FR1 refereed; FR3 running | FR3 | yes (decision 7 of campaign 8) |
| P1 | approved primitive (kinetic isotropy) | c_t = c_s, with a hypercubic regulator | K7a (one cone) | Without it, the photon and matter speeds are also unprotected | K7a | — | no |
| P2 | approved primitive (scale reference), with a = l_P **not derived** | The cutoff sits at the Planck scale | the size of the induced mass, m_g² ~ (TT modulus)·a⁻⁴/M_P² (reading) | A coarser cutoff gives a smaller mass. A cutoff near 1e-3 eV would put m_g near 1e-33 eV, but such a coarse grid is excluded by Lorentz tests (suggested) | no | an order-of-magnitude scan | no |
| S1 | supplied model | Matter is ordinary interacting lattice fields (staggered fermions plus U(1)) | K3a″, W1 | The free part can be designed away; interactions bring the modulus back | K3a″ (O(e²), several coupling rules) | — | no |
| S2 | supplied definition | Graviton mass = the zero-momentum TT Hessian of the vacuum energy, for an independent metric field | K3a″ and W1 interpretation; referee caveat: needs a stationary background and kinetic normalization | For an emergent graviton the modulus is "a diagnostic only" (referee); the true mass needs the collective field's 1PI inverse propagator | no | build any emergent-graviton toy and compute its 1PI TT mass | maybe |
| S3 | supplied method | Harmonic or perturbative level: linearized gravity, O(e²) | everywhere | Strongly correlated phases could differ (the 09-29 "most likely wrong") | no | — | maybe |
| S4 | supplied state | The vacuum is the weakly interacting Fock vacuum of lattice fields on a crystal-like substrate | K3a″, W1 | A vacuum with zero static shear modulus (liquid-like, defect-proliferated) could remove the stiffness | no | as L1 | yes, if it needs a dynamical substrate |
| S5 | reading | Gravity is a local wave pattern (a lattice graviton mode) | everywhere | Gravity as non-local, global or thermodynamic (Jacobson) | Jacobson-type is dead on the grid (16–18% anisotropy) | — | maybe |
| S6 | target choice | Naturalness: no tuned counterterm for m_g | the wall's FAIL lines (K3a″, W1) | Nature already tolerates the cosmological-constant tuning, the trace twin of this modulus. A single mechanism could tune both | no | check whether any known CC mechanism, such as equilibrium self-tuning, also kills a **second** derivative (modulus), not just the first (tadpole) | yes |
| S7 | supplied coupling | The metric enters through a fixed rule: minimal, vielbein, Whitney | K3a″, W1 | A rule that moves the embedding, cutoff and measure together is untested on a lattice (referee) | continuum only | as L1 | maybe |
| H1 | hidden | Translation invariance of the substrate (a crystal) | K3a″, W1 | A random or disordered substrate (a glass) is untested; a glass also has a static shear modulus (suggested) | no | — | no |
| H2 | hidden | One vacuum, with no relaxation dynamics for anisotropy | K3a″, W1 | A dynamical relaxation of the modulus ("self-tuning") is untested | no | — | maybe |

**Rows the wall survives without:** P1, H1 and S1 (any interacting matter does it). L2 is load-bearing only for the partner face.

**Load-bearing for the stiffness face:** L1, S4, S7 (the fixed substrate and cutoff), S2 (what counts as a mass), S6 (naturalness) and S3.

### Route clusters

| Route | Assumptions challenged | Why this might open the wall | Expected artifact | Risk | First test |
|---|---|---|---|---|---|
| C1 "liquid vacuum" | L1, S4, S7 | A medium that can rearrange has no static shear modulus, so the cutoff would follow the geometry | a toy with a rearranging substrate and its TT modulus | changes the Lattice axiom's reading; Lorentz and cutoff issues | static TT modulus of a crystal versus its melt, for a field theory living on it |
| C2 "protected emergent graviton" | S2, S5, L2 | An exact lattice constraint forbids a TT mass the way Gauss's law forbids a photon mass | a constraint algebra, and a 1PI TT mass computation | the 09-29 probes (exact slides give ω ~ q²; light-like TT gives ±1 partners) | does a rank-2 exact constraint forbid the TT mass and keep ω ∝ q? |
| C3 "one tuning for two problems" | S6, H2 | The CC tuning and the TT modulus could be the same vacuum-energy problem, solved together | an argument or toy relaxation mechanism | relaxation mechanisms usually handle tadpoles, not moduli | is there a known mechanism that zeroes a modulus? |
| C4 "the price" | L1 | Prove that the wall is equivalent to "fixed adjacency" | a lemma: fixed label-space cutoff ⇒ TT modulus ≠ 0 generically | a generic statement is hard to make exact | the free IR-cone identity, generalised |

## Step 3: first-principles reduction

1. **Make the requirement less wrong.**
   - The goal needs gravitational waves to be **massless enough**: m_g ≲ 1e-23 eV (GWTC-3), about 1e-51 M_P. It does not need an exact zero.
   - It needs universality to about 1e-15 and two TT polarizations at speed c.
   - "Natural" means no counterterm tuned below what the premises supply.
   - The naturalness demand is the contested part (S6). It is kept as the target, and its status is examined by route C3.
2. **Delete.**
   - The partner face (finite slots) is not needed to state the stiffness face, which also hits continuous slots.
   - Records are not needed: FR1 shows they do not supply the mediator.
   - Matter content beyond "interacting" is not needed: any interacting lattice field gives an O(e²) modulus.
3. **Shrink.**
   - The smallest object in which the wall bites is the **free IR cone** of one massless lattice field. A fixed label-space window gives a TT second derivative of −K₀⁴/(60π²); a window that follows the strain gives 0.
   - This needs neither interactions nor gravity. It is the cutoff's geometry alone.
   - With interactions the same thing survives at O(e²) (K3a″, W1).
4. **Split.** Two independent bits:
   - (a) the **cutoff geometry** problem, where the modulus comes from a regulator that does not move with the metric;
   - (b) the **mediator** problem: a massless spin-2 field with universal coupling must exist at all.
   
   (a) is a naturalness problem and (b) a construction problem. Finite slots fail (b) at the harmonic level, and continuous slots plus a fixed cutoff fail (a).
5. **Price it.** The exact missing input would be one of:
   - (a1) a regulator whose cutoff moves with the geometry, which on a lattice means adjacency or labels that move;
   - (a2) an exact symmetry forbidding the modulus, which on a fixed lattice is not available among the tested couplings;
   - (a3) a tuned counterterm.
6. **Speed up the loop.** The free IR-cone identity takes seconds to evaluate and is the smallest runner. Any proposed route can be screened on it first: does the route's regulator follow the strain?
