# Route agent R1: the condensed-matter lens

**Agent:** Claude Opus 5.5, extra-high (xhigh) effort.
**Refresher read (stated):** the full axioms, the primitive registry check, the `axiom_premise_nodes.json` node list, the brief, the pack's TEST_LOG sections, the 09-29 summary and its condensed-matter agent, and the landed walker-sea shear note.
**Blinding (self-reported):** did not read `supervisor_thread.md`, `OUTSIDE_VIEW.md` or `blind_check.md`, but noted possible overlap with the outside view's Poisson/Delaunay wording.
**Scripts:** `scripts/R1_A … E` with their outputs.

**Prior art the agent found.** The August archive (`origin/ai/probes:archive/campaigns/opus-direct-20260827/POSITIVE_PATH.md:4974-5040`): on a fixed regular mesh, log-det moves at O(1) under pure re-triangulation. That matches the glass and crystal arms below.

## How real media get zero static shear modulus, and what each needs here (COMPARATOR literature)

| Mechanism | Example | What the framework would need | Verdict |
|---|---|---|---|
| Re-choosing neighbours (fluid) | liquids, superfluids | a non-crystal site set, with neighbours that follow the geometry | Route 1 |
| Relaxing internal variables | Fermi liquid | the sea re-forms under strain | Route 2: only partial |
| Spontaneously broken reference rotation | nematic elastomers | a continuous reference symmetry; the grid's is cubic, and it softens at most 2 of 5 moduli | dead |
| Floppy modes protected by constraint counting | Maxwell lattices (Kane–Lubensky) | it controls classical springs, not the modulus induced by loops | dead (ARGUED) |
| Emergent gauge redundancy | the spin-ice photon, rank-2 fractons | matter must carry a charge equal to its momentum, which is K3a's exact stress | blocked-equivalent |
| Matter as defects (Kröner: div Inc ≡ 0) | dislocations, disclinations | the source is conserved identically, but it is topological charge, not energy | fails equivalence (ARGUED) |

## Route 1: a liquid lattice

**Lemma L (EXACT, proof skeleton, unrefereed).** Take:
- X, a homogeneous Poisson process;
- g = MᵀM with det M = 1;
- F(X, g), the vacuum energy density of any field content, built on the Delaunay complex of X in metric g with weights from g-lengths only (FEEC/DEC).

Then Del_g(X) = Del(MX) and F(X, g) = F(MX, δ). The law of MX equals the law of X, so E F(X, g) = E F(X, δ). With self-averaging, the static TT modulus is **exactly 0 at every order in e**. This removes W1's fixed-Brillouin-zone mechanism.

**Open steps:**
- existence and self-averaging of the interacting vacuum density on a random complex;
- a non-uniform metric re-chooses neighbours locally, so adjacency is dynamical.

**Checks (CHECKED; scalar vacuum ½Σ√λ):**

| Case | G per site (± 1 SE) | Reading |
|---|---|---|
| 2D liquid, cotan operator, N = 2500 × 12 samples | G/e₀ = −0.005 ± 0.039 (Eg), −0.011 ± 0.029 (T2g) | zero |
| 2D glass (neighbours frozen), same points | +1.731 ± 0.003 / +1.729 ± 0.003 | stiff |
| Rippa inequality: K_frozen − K_Delaunay ⪰ 0 in 2D | holds to −4e-12 | — |
| 3D liquid, circumcentric (Voronoi-dual) operator | −0.023 ± 0.013 / −0.003 ± 0.015 | consistent with 0 |
| 3D glass, same operator (paired, n = 30) | +0.021 ± 0.010 / −0.03 ± 0.04 | not resolved at 5 SE |
| 3D glass, P1 operator | +1.27 | stiff |
| Crystals with neighbours re-chosen (control) | 2D square T2g: −0.39·\|ε\|; 3D cubic Eg: +1.42; 3D cubic T2g: a cusp | never zero |

- **Mechanism, 2D (EXACT).** Rippa's flip lemma plus operator monotonicity of √ means bosons resist shear on a glass. A filled fermion sea reverses the sign.
- **3D P1 caveat.** About a third of P1 weights on 3D Delaunay complexes are negative, and they jump at flips. So the 3D liquid needs the circumcentric operator, verified against the Voronoi construction to 2.5e-14.

**What kills it (agent's own):**
- **K1, one light cone.** P1's protection is the hypercubic Z³ × Z_τ form (K7a). A random spatial grid has no symmetry linking time and space, so loops split species' speeds at O(α) (Collins et al., PRL 93 (2004) 191301).
  - A 4D Euclidean Poisson–Delaunay lattice restores O(4) in law, but has no reflection per sample and no known transfer matrix.
  - Lorentzian sprinklings admit no Lorentz-invariant finite neighbour rule (Bombelli–Henson–Sorkin 2009).
- **K2, selection.** Only bosons pick Delaunay energetically (EXACT in 2D), so "neighbours follow geometry" must be a law (ARGUED).
- **K3, the graviton is still supplied.** The lemma removes only the medium's mass term.

**Gap test.** Weaker than the target (it fixes one face) and brings a new mechanism, so it is not blocked-equivalent.

**Next artifact.** The one-loop speed split between two species on a 3D Poisson–Delaunay spatial lattice with continuous time. FAIL if |δc₁ − δc₂| exceeds 10 SE at O(e²).

**Supervisor flag for the kill round.** R1's liquid lattice keeps the **sites frozen** and re-chooses neighbours. That is R3's "frozen pattern-free" class, where R3 found a per-configuration white-noise TT stiffness σ ≈ 0.035–0.13 per site, which scatters gravitons within about 0.2–300 l_P. R1's checks report the sample mean ± SE, not the per-configuration random part.

## Route 2: equilibrium self-tuning on the fixed grid (rows S6, H2)

- **Lemma (EXACT).** The relaxed modulus is e_hh − e_hφ e_φφ⁻¹ e_φh. It vanishes for all couplings only if there is an exact flat direction through h.
- **Candidates on fixed Z³:**
  - (α) graph automorphisms are discrete;
  - (β) an on-site SL(3,R) is impossible on M₂(C), since non-compact simple groups have no nontrivial finite-dimensional unitary representations;
  - (γ) a unitary family generated by Q = Σ xᵢ pⱼ(x) needs an exactly conserved local momentum density, which is K3a's open obligation;
  - (δ) an exact boson–fermion spectral match.
- **Check A (CHECKED), a dilute free sea on Z³.**
  - Frozen sea: G/e₀ = 8/3 in both channels.
  - Relaxed: G/(e₀k_F²) is −0.10 to −0.12 in Eg (analytic −2/21) and +0.45 in T2g.
  - **FAIL:** relaxation removes the continuum part and leaves (k_F a)² anisotropy from the grid's bands. A filled band, which includes every Dirac sea, cannot relax at all.
- **Scale.** The LIGO bound allows a modulus of at most about 1e-102 M_Pl⁴, which needs ℓ/a ≈ 1e51, a hierarchy put in by hand.
- **Gap test.** Blocked-equivalent. **The reduction:** on fixed Z³, the stiffness face is equivalent to K3a's exact interacting stress, or to an exact boson–fermion cancellation.
