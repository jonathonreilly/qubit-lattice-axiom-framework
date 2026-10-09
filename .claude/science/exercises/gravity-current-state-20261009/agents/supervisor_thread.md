# Supervisor's own thread (Claude Opus 5.5)

Written before any route agent reported, so the comparison stays fair: the skill's standing rule is that the supervisor runs its own thread on farmed-out work.

## The smallest object (CHECKED, exact; `scripts/S0_ir_cone_cutoff_identity.py`)

Take one massless field in a constant, volume-preserving metric g = exp(−tε), with ε symmetric traceless and tr ε² = 1. Its vacuum energy's second derivative in t at t = 0 is:

| Cutoff | Bosonic mode | Weyl sea |
|---|---|---|
| window fixed in **label** space, \|k\| < K₀ | **+K₀⁴/(120π²)** | **−K₀⁴/(60π²)** |
| window fixed in **proper** space | **0** | **0** |

- The value is the same for axis, face and generic shears.
- The Weyl value matches the W1 referee's independent number.
- Reading: in the IR-cone approximation, the transverse-traceless (TT) modulus is exactly the cutoff geometry. Nothing else enters.

## An observation to test: bosons and fermions enter with opposite sign

- **At the free IR-cone level,** the modulus is ∝ (n_B − 2 n_Weyl)·K₀⁴/(120π²), a supertrace. A boson–fermion-balanced content cancels the leading K₀⁴ term exactly. This is the TT twin of the SUSY cancellation of the quartic vacuum-energy divergence (suggested).
- **With mass splittings** the cancellation stops at subleading orders, K₀²·STr m² and STr m⁴·log (suggested). With modulus ~ STr m⁴ and m_g² ~ modulus/M_P², a TeV splitting gives m_g ~ TeV²/M_P ~ 1e-4 eV. That is far above the LIGO bound of about 1e-23 eV.
- So balance can remove the Planck-scale part but not reach the bound. This mirrors the cosmological constant: SUSY leaves about TeV⁴ against the observed meV⁴ (suggested, order of magnitude).
- **Beyond the IR cone,** lattice band structure enters: K3a″'s free part is O(0.1) per cell with signs that depend on the coupling. Whether a lattice supertrace cancels the *whole* free-level modulus is a cheap check, not run.

## My candidate routes (for comparison with the agents)

| # | Route | Premise challenged | First test |
|---|---|---|---|
| C1 | **A liquid vacuum.** A substrate whose neighbour structure rearranges has no static shear modulus, so the low-energy cutoff follows the geometry | L1 (fixed adjacency), S4 | In a model whose bonds can rewire (or whose defects proliferate), does the field theory living on it have zero static TT modulus? Compare crystal and melt |
| C2 | **A protected emergent graviton.** An exact lattice constraint forbids the TT mass, as Gauss's law protects the photon | S2, S5 | Is a rank-2 exact constraint compatible with a linear (ω ∝ q) TT mode? The 09-29 probes say exact slides give ω ~ q², so this is likely wounded |
| C3 | **One mechanism for two problems.** The trace part of the cutoff's vacuum response is the cosmological constant; the TT part is this modulus | S6, H2 | Does any known CC-relaxation mechanism also zero a **second** derivative, not just the first? Equilibrium self-tuning (Volovik) zeroes pressure (the tadpole), not a modulus (suggested) |
| C4 | **The price lemma.** For any local field theory regulated by a fixed label-space cutoff, the static TT modulus is generically nonzero and cancels only by supertrace balance or tuning | L1 | Generalize the IR-cone identity to the lattice band structure and to O(e²); state it as a lemma |

**Lean (a reading).** C1 and C4 together are the honest core. The stiffness face says a fixed crystal substrate makes the vacuum rigid against shear. Gravitational waves are massless, so the substrate must flow (C1), unless something cancels the modulus exactly, which in the known cases is supersymmetry, and that cancellation is broken in nature. This is a layman-simple candidate price: **"space is not a fixed crystal"**. Still to be weighed against the agents' independent routes.
