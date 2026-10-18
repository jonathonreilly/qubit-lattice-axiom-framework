**R4 report: can the lattice's own numbers give the three generations their large fixed mass ratios?**

**Short answer.** No. The lattice's spectra and group numbers stay small, at most 16 to 1. Once they are exponentiated they can fit the observed masses within ×3, but they fit random fake spectra just as often, so such a fit is no evidence. The only exact pattern in the data that beats chance is the lepton Koide–Brannen relation, and the framework supplies neither of its two numbers.

**Refresher, read before any conclusion.** I read `docs/MINIMAL_AXIOMS_2026-06-29.md` and `PRIMITIVE_REGISTRY_CHECK.md` in full, read `SCALE_REFERENCE_PRIMITIVE_NOTE.md`, and read `derivation_obligations.json` in full. That file has no hierarchy entry; its three entries are about charged-lepton (Koide and η) readouts and the θ readout. I also read the WALL and the HIER-2 SUMMARY and H2 reports.

**Prior art on main, checked with git grep.** None of the following is presented as new:
- the Wilson corner staircase, masses linear in Hamming weight (`WILSON_BZ_CORNER_HAMMING_STAIRCASE_*`);
- the circulant eigenvalue mechanism (`YT_GENERATION_HIERARCHY_PRIMITIVE_ANALYSIS` §0);
- the Koide cone and the Brannen δ gate, including the finding that every retained period is a rational multiple of π (`KOIDE_A1_O13_CHEEGER_SIMONS_RZ_NO_GO`, `KOIDE_DELTA_RADIAN_PERIOD_*`);
- the α_s(v) mass-ratio formulas (`QUARK_MASS_RATIOS_TASTE_STAIRCASE_*`);
- HIER-2's sector blindness and its free-integer control (400 of 400 random spectra fit).

The grep found no area-law (worldsheet) Yukawa texture, no chance estimate for Koide, and no count of how densely a formula family covers random targets.

## Results

Everything ran pre-registered in `PREREG.md`, with random spectra drawn log-uniform in two ways (N1: all 9 masses random; N2: heaviest in each sector fixed). Peak memory was 355 MB, and nothing is left running.

- **T0. Lattice spectra alone fall short (checked).** I took the energies at high-symmetry momenta of the naive, Wilson, Laplacian and walker operators in 3D and 4D. The largest ratio of two nonzero values is 16; the cubic-group integers reach at most 48. Within one sector the data need 1.0e3 (down quarks) to 1.25e5 (up quarks). So an exponential map is unavoidable.

- **T1a. Exponential ladders, mass = scale × base^exponent (checked).** The library had 15 exponent triples (hop counts and squares) and 14 lattice-fixed bases (α_s(v), α_LM, ⟨P⟩, 1/16, e^−π and others), so 210 combinations.
  - A single pre-registered base-and-triple pair, shared by all sectors, would count as evidence: random spectra pass it only 0.1–0.6% of the time.
  - None of the 210 passes. The best is α_s(v) with exponents (4, 2), off by ×3.8 at M_Z and ×3.1 on the low-scale set.
  - Any freedom per sector raises the random pass rate to 72–98%.

- **Which sectors can share a pattern (checked; sharpens HIER-2 R2).** Even with a free scale per sector, the first-generation ratio m₁/m₃ differs by ×123 between up and down quarks, and ×35 between up quarks and leptons; ×3 allows ×9. Down quarks and leptons differ only ×3.5, so they can share a pattern. The least sector input the data force is one split: up quarks against the rest.

- **Post-hoc, weak (suggested).** Using one shared ladder for down and lepton and scaling the up-quark exponents by 2 or by 3/2 passes at ×2.6 and ×2.0. Random spectra do at least as well 0.6–8% of the time, and the winning bases look arbitrary (⟨P⟩ with exponents (12, 5), or 1/8).

- **T1b. Area-law texture, Y_ij = exp(−σ·A).** A is the lattice area of the triangle joining the left-handed site eᵢ, the Higgs site and the right-handed site. There are 3,312 distinct placements per sector and one tension σ for all sectors (checked).
  - At σ = 2.5, all nine masses fit within ×1.16 and the CKM moduli within ×1.12 (|V| = 0.210, 0.037, 0.0034). On its face this meets the wall's target.
  - But it also fits 100% of 2,000 random spectra, and 59 of 60 random spectra paired with random CKM values. **My pre-registered prediction that masses plus CKM would fail was wrong.** The fit passes and carries no evidence.

- **T1c/d. Symmetric placements fail.**
  - Placements symmetric under the 3-fold cube rotation always give a degenerate mass pair (proved: a real circulant has |λ₁| = |λ₂|). They miss by ×57–71.
  - If up and down share a swap symmetry, the CKM matrix has exact zeros (proved: the odd swap state is a shared singular vector).
  - If up and down have different swap axes, the mixing comes out of order one: |V_us| = 0.71, CKM off by ×16 (checked).

- **T2. Koide control (checked; the lepton values are comparators).**
  - With pole masses, |Q − 2/3| = 6.2e-6 and |δ − 2/9| = 7.4e-6. Both are within one standard deviation of the τ-mass error (6.8e-6 and 8.3e-6).
  - The chance that a random triple sits this close to one of 30 simple fractions for Q is 6.0e-4. For one of 63 simple values of δ (plain fractions or fractions of π) it is 8.4e-4. Allowing for any of the three sectors, the combined chance is about 1.5e-6.
  - δ/π = 0.070738 is not a fraction with denominator ≤ 12 at this precision.
  - Quarks: Q_u is 0.85–0.89 and Q_d is 0.73–0.74. The same fraction family fits them within ×1.05–1.45, but it fits 96% of random triples within ×3 and 64% within ×1.1.

- **T3. How densely main's formula family covers random numbers (checked).** Formulas c·α_s(v)^p, with p a fraction of denominator ≤ 6 and small prefactors, give 816 distinct values. They land within 1.3% of 93% of random targets and within 3.3% of 99%. Even a 42-value subset lands within 3.3% of 27%. So agreements at the 1–3% level, such as m_d/m_s = α_s/2, are not evidence unless the formula was fixed before the comparison.

## Route W: area-law (worldsheet) Yukawas on Z³

- **Object.** Y^f_ij = exp(−σ·A_L1(eᵢ, hᶠ, rᶠⱼ)), where A_L1 is the plaquette lower bound for a surface spanning the triangle, and σ is one tension for all sectors. This is the lattice version of intersecting-geometry Yukawas.
- **What it would fix.** All six within-sector ratios and the three CKM moduli from one σ, provided the placements hᶠ and rᶠ were fixed. The axioms do not place Higgs or right-handed fields. Every symmetric placement rule I tested is excluded.
- **Strongest objection.** With generic placements it fits random data 98–100% of the time. Also, the axioms give no plaquette weight or gauge field, so σ itself is supplied.
- **Kill condition.** A placement rule derived from the axioms that leaves ≤ 10 placements per sector, pre-registered, must pass the observed masses while random spectra pass ≤ 5%. Otherwise the route is dead as evidence.
- **Cheapest next test.** Rerun `t1b` restricted to whatever placements a proposed rule allows; it takes minutes.

## Route K: twisted circulant on the 3-fold triplet (mapped on main)

- **Object.** √m_k = μ(1 + r·cos(δ + 2πk/3)). For leptons, r = √2 and δ = 2/9 rad.
- **What it would fix.** Both within-sector ratios. Neither number is supplied: r = √2 is main's open BAE gate, and δ in radians is the open δ gate. A lattice flux or holonomy would give δ as a fraction of π, which T2 excludes for denominators ≤ 12 at the 1e-5 level.
- **Strongest objection.** The form fits any positive triple, so its only content is how exactly the two values hold. Only the leptons are measured precisely enough to test that. It holds for pole masses (Q = 0.6679 at M_Z), so a short-distance lattice mechanism would have to explain a long-distance relation.
- **Kill condition.** A τ-mass measurement that moves Q off 2/3 by more than 3σ. For quarks no test is possible at current precision.
- **Value.** It is the only regularity with chance below 1e-5 after trials, so it is the gate worth the effort.

## Extra numbers the data force (checked, not proved)

- One split between up quarks and down-plus-leptons.
- Either a placement rule, or the base and exponent triple, with no choice left per sector.
- For leptons, r and δ, or equivalently two ratios.

**Recommendation for the wall.** A claimed pass at ×3 should come with the random-spectrum pass rate under the same search, required to be ≤ 5%. T1b meets the wall's target with no evidence at all.

**Provenance.** All work is same-family and unrefereed. Masses and CKM values were recalled, not fetched. I edited nothing outside my folder.

Everything is in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/masswall/R4/`:
- `PREREG.md`
- `scripts/`: `t0_spectral.py`, `t1a_ladders.py`, `t1b_area_texture.py`, `t1c_symmetric_placements.py`, `t1d_misaligned_z2.py`, `t1e_posthoc_upsplit.py` (post-hoc), `t2_koide.py`, `t3_grammar.py`
- outputs: `t0.out` … `t3.out`