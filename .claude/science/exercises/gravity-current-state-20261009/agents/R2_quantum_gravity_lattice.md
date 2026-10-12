# Route agent R2: the discrete and lattice quantum-gravity lens

**Agent:** Claude Opus 5.5, extra-high (xhigh) effort.
**Refresher read (stated):** the full brief, the full axioms, the primitive registry check, `axiom_premise_nodes.json`, the pack's `TEST_LOG.md`, and the 09-29 SUMMARY and quantum-gravity lens.
**Scripts:** `scripts/R2_c1 … c4` with their outputs. None of this is refereed.

**Independence, self-reported.** The agent did not open `OUTSIDE_VIEW.md` or `agents/`. It did see the commit title "fluid/label-blind substrates protect m2=0" in a git-status snapshot. So Route 1's *headline* is not independent of the supervisor's view; its lemma, numbers and trade-off are its own.

## Route 1: site sets whose statistics cannot tell shapes apart

**Lemma A (EXACT, proof sketch).** Suppose:
- the site set is a stationary, ergodic point process whose **law is invariant under SL(3)**;
- matter is any local rule, interacting ones included, built only from the sites and proper distances.

Then the vacuum energy density depends on g only through det g, so the TT stiffness is 0 to all orders.

*Proof.* E(g;P) = E(1;AP), with A = g^½, and AP has the same law as P. Open steps: existence of the interacting thermodynamic limit, and the S2 mass definition.

**Count of TT constants (EXACT).** Under O_h, 6 = A1g ⊕ Eg ⊕ T2g:
- a cubic crystal has 2 TT constants;
- an isotropic glass has 1;
- an SL(3)-invariant law has 0.

**Check C2 (CHECKED).** A free massive scalar, with Gaussian weights computed from g, σ = 0.5 spacing, N up to 1728:

| Site set | TT stiffness Eg | TT stiffness T2g |
|---|---|---|
| Z³, with all weights recomputed from g | +0.2218 | −0.0492 |
| RSA glass | +0.0376 ± 0.0003 | +0.0381 ± 0.0005 |
| **Poisson** (sites never move) | **+0.0015 ± 0.0010** | **0.0000 ± 0.0005** |

The Poisson result is consistent with 0 at N = 512, 1000 and 1728.

- **Ledger correction.** L1 and H1 name the wrong premise. The load-bearing one is "**the law of the site set is not SL(3)-invariant**". Dynamical adjacency is neither necessary (Poisson passes with frozen sites) nor sufficient (a glass fails).
- **What you would have to believe.** That a 3+1 ensemble of this class has an extended phase with a spin-2 pole and one light cone for interacting matter. The literature (COMPARATOR):
  - Euclidean 4D DT has a first-order transition;
  - CDT has a second-order transition but a foliated time, so no symmetry ties the time and space directions;
  - causal sets are Lorentz-invariant in law (Bombelli–Henson–Sorkin, MPLA 24 (2009) 2579), but their links are non-local and they have no Hamiltonian.
- **Price.** It drops the Lattice axiom's site set: a Poisson sprinkling needs continuous positions, and DT/CDT sum over adjacency.
- **Gap test.** Stronger than the target, since the continuum limit of a sum over geometries is unsolved. It brings a new protecting mechanism (a symmetry of the law), so it is not blocked-equivalent.

## Route 2: Wetterich position-blind actions on fixed Z³ (a kill)

- **Lemma B1 (EXACT).** Position blindness for a constant vielbein forces L(E) = det E · L(1), so every position-blind counterterm is constant at fixed det E.
- **Lemma B2 (EXACT, Cauchy–Schwarz).** For any fixed set of label momenta, d²|Bs|/dt² = (2|Ys|²|s|² − (s·Ys)²)/|s|³ > 0, and d² log|Bs|²/dt² ≥ 0. So the Dirac-sea energy and the Euclidean −log det **both fall along every shear**.
- **Check C3 (CHECKED).** Per site, per two-component:
  - 3D Dirac sea: −0.1779 (Eg) and −0.1467 (T2g);
  - 4D log det: −0.2066 and −0.1467;
  - a strain-following control: 0, to about 1e-13.
- **Reading.** The isotropic composite-vielbein vacuum is a saddle in the TT directions, and no position-blind counterterm can stop it.
- **Effect.** This closes the open escape in the pack's TEST_LOG at mean-field level. It contradicts at zero momentum the abstract's claim that the effective action inherits the invariance (arXiv:1110.1539).
- **One opening it leaves.** A boson sea has the opposite sign, which is the field-content-cancellation route, not position-blindness.

## Route 3: smooth kernels in proper distance on fixed Z³

**Check C1 (CHECKED, massive scalar; L = 64 and 96 agree).**
- Nearest-neighbour coupling: about +0.18 / +0.19.
- **Gaussian kernel in proper distance: about 0.35·exp(−π²σ²)** (fitted slope 9.87). Values are −1.8e-5, −7.0e-8 and −7.8e-11 at σ = 1, 1.25 and 1.5.
- Rational, reflection-positive kernel: 6.4e-3, 8.4e-4, 9.1e-5 and 7.7e-6 at σ = 1, 2, 4, 8, about σ^−3.5.

**Mechanism (ARGUED, Poisson summation).** The first non-covariant piece is the overlap of neighbouring images at the zone face, about e^(−π²σ²).

**Check C4 (CHECKED).** A Gaussian kernel in Euclidean time violates reflection positivity: the Hankel min/max ratio is −1.7e-4, −7.8e-3 and −1.1e-2 at σ = 1, 2, 3.

**The trade (ARGUED):**

| Regulator | Stiffness suppressed | One cone protected | Reflection positive |
|---|---|---|---|
| Entire kernel, 4D | yes | yes | **no** (C4) |
| Rational kernel, 4D | power law only | yes | yes |
| Entire kernel in space, Hamiltonian time | yes | **no** (Collins et al.) | yes |
| Nearest-neighbour hypercubic (K7a) | **no**, O(1) | yes | yes |

- **First artifact (hours).** The one-loop speed split between two species with a smooth spatial kernel and continuous time.
  - **PASS:** the split → 0 as σ grows.
  - **FAIL:** a σ-independent O(g²/16π²) split.
  - The agent predicts FAIL.
- **Gap test.** If it fails, the route is blocked-equivalent (the naturalness clause restated as a regulator property).

## The cheaper question that may replace the wall (reading): a regulator trilemma

Is there a reflection-positive regulator that gets both:
- (a) a single light cone protected by a symmetry linking time and space;
- (b) zero TT stiffness, from SL(3)-invariance in law?

C1, C3 and C4 check three corners, and Collins is the fourth (COMPARATOR). A fixed Z⁴ gets positivity and the cone. CDT-type foliated ensembles are the only candidate the agent knows for all three, and their light cone is untested.
