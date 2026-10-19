<!-- Saved by supervisor from worker's final message (harness blocked REPORT.md write). -->
# T-F3 report: can one realised state keep C₃ for charged leptons and C₂[110]∘T(e₃) for neutrinos?

**Reading: F3-PRICE, at the KILL boundary.** This uses the reading of the PRICE tuning clause I pinned in `PREREG_NOTES.md` before any run: "a tuning of ε ≤ 1e-2" taken as the strongest tuning PRICE covers.
- **The price is a tuning.** Every coupling between the two sectors must sit at about 0.05 of its loop-natural size (about 3e-4 of its tree size). That holds for normal ordering with the pre-registered operator set. For inverted ordering, or with every G-allowed trilinear insertion at natural size, it must be about 0.01.
- **No single named structure removes the leakage.**
- **The literal KILL clause also holds.** At the pre-registered natural size (O(1) × 1/16π²), the median Δ is 0.057–0.23, which is above 0.01, and no framework symmetry forbids the operators. Under the other reading of the tuning clause the result would be F3-KILL.

Writing REPORT.md was refused, so this message is the whole report. The worker was one Opus 5.5, the same family as the derivation's author, and the work is unrefereed. Peak memory was 484 MB with one process at a time, and nothing of mine is left running.

**Refresher surfaces read:**
- MINIMAL_AXIOMS_2026-06-29.md (all) and PRIMITIVE_REGISTRY_CHECK.md (all).
- `axiom_premise_nodes.json`: four nodes (the axioms plus scale_reference, kinetic_isotropy, realized_state). None is an internal symmetry.
- The FP derivation (all), s1–s4 scripts and outputs, TESTS.md (T-LANDAU, T-F3), T3 REPORT and PREREG, the CLS-1 REPORT, WALL.md and SUMMARY.md.
- A grep of main for "vacuum alignment | driving field | sequester" found 0 files.

## Plain-words findings
1. **One state cannot hand each sector its own residual unless the sectors are kept apart by hand.**
   - The two residuals generate the full 24-element cubic group on the generations, which acts irreducibly (proved; `t4_group.out:4`).
   - If both mass matrices are generic G-covariant functions of one state, each inherits only the state's own symmetry. Asking for both residuals then forces degenerate masses (Schur).

2. **G supplies no separation between the sectors.**
   - Every irrep the neutrino mass sees (A1, E, 3M) is also seen by the charged-lepton mass (`t4_group.out:17`).
   - The charged-lepton order must contain the symmetric irrep 3M. Without it, m_τ − m_μ ≤ 2m_e (proved; `t4_group.out:23`), whereas the data need about 1635 times more.
   - So mixed mass insertions are allowed at tree level both ways: 6 + 4 complex couplings (`t4_count.out:1`).

3. **The joint vacuum is not even stationary.**
   - Within each sector, the C₃ point and the g_ν point are stationary for any potential of that sector alone. This is Michel's theorem, checked to 1e-16 (`t4_group.out:46`).
   - The joint point's stabilizer is only ±1 (`t4_group.out:45`). Of the 714 cross invariants up to quartic order, 710 push it off the symmetric directions. That includes all 298 quartics that survive shaping and all 56 combinations invariant under U(1)×U(1) (`t4_group.out:47-49`). The lowest is the quadratic m·p (`t4_group.out:50`).
   - **Both residuals are lost.** I ran natural random potentials whose separate minima sit on the F3 strata, then coupled them. In 4 of 4 pairs the joint stabilizer dropped to ±1. At λ = 1/16π², the symmetry-breaking fraction is 0.006 for leptons and 0.003 for neutrinos with no shaping, and 0.0013 and 0.0004 with U(1)×U(1) (`t4_vacA2.out:25,28`).
   - At λ = 1 with no shaping, the joint potential was unbounded below and the minimiser ran away.

4. **The neutrino residual is a tuned vacuum even on its own.**
   - Untuned random quartic potentials put the neutrino minimum on the needed Z₂ stratum 1 time in 300 (`t4_vacA.out:18`). In the A2 ensemble it was 1 in about 3400 (`t4_vacA2.out:22`).
   - The charged-lepton Z₃ stratum is common: 89 of 300.
   - Separately, the data-fitted F3 point is a saddle along symmetry-breaking directions for 52% (leptons) and 20% (neutrinos) of random sector potentials (`t4_vacB.out:3`).

5. **The leakage is dominated by the charged-lepton side.** The C₃ mass matrix's entries are all about m_τ/3. So a leak of relative size ε rotates e into μ by about ε·m_τ/m_μ ≈ 17ε (suggested). Leaking into M_l alone gives median Δ 0.052, against 0.028 into M_ν alone (`t4_leak_NO_min.out:8`).

6. **SM-like fermion loops with the measured Yukawas are harmless.** They give median Δ = 9e-6 (normal ordering) and 5e-4 (inverted) (`t4_leak_NO_min.out:7`, `t4_leak_IO_min.out:7`). The danger is the admissibility rule's unspecified values (MINIMAL_AXIOMS:181-184), not the measured couplings.

## Tasks
**1. Operators that couple φ_ℓ and φ_ν** (`t4_count.out`, `t4_group.out:31-41`):

| Class | Count |
|---|---|
| Linear mixed insertions | 6 into M_l, 4 into M_ν (3M' is excluded by Majorana symmetry) |
| Second-order insertions | 33 (φ_ℓφ_ℓ into M_ν), 35 (φ_νφ_ν into M_l) |
| Trilinear, surviving any shaping | 414 into M_l, 342 into M_ν |
| Potential cross invariants, degree ≤ 4 | 714 |
| Shared-doublet wavefunction leak | present in both directions |

The 714 potential invariants split by degree as (1,1) 4, (1,2) 32, (2,1) 52, (1,3) 164, (2,2) 298, (3,1) 164. The irreps and placement are the derivation's. The generation triplet sits at the three X points, and the lattice acts on it as the 48 signed permutations. Both residual elements were built from geometry (`t4_group.out:2-3`).

**2. Symmetry.**
- G is the only symmetry the axioms supply (MINIMAL_AXIOMS:57-58). K/CPT is downstream (MINIMAL_AXIOMS:169-171). T(1,1,1) acts trivially on every mass matrix (`t4_group.out:18`).
- Proved (elementary): terms built from neutral pairs are invariant under any unitary internal symmetry that commutes with G. These are |φ_ℓ|²|φ_ν|²-type contractions, φ_ℓ(φ_νφ_ν†) insertions, and the shared-doublet term P (a C₃-invariant Hermitian matrix).
- What fixing it would cost, all imports:
  - a shaping symmetry (Z_N with N ≥ 3, or Z₂×Z₂) removes only the linear and odd terms;
  - SUSY with U(1)_R driving fields adds two more structures;
  - sequestering needs an extra dimension. A version inside Z³ is blocked because the nearest-neighbour rule couples neighbours, so one lattice step gives no suppression (suggested).

**3. Vacuum alignment.** Covered by findings 3 and 4. Misalignment from cross quartics at λ = 1/16π² gives median Δ (`t4_vacB.out:8,12,16`):
- 0.018 with no shaping;
- 0.013 with Z₂×Z₂;
- 0.006 with U(1)×U(1).

**4. Leakage.** Couplings are O(1) times the loop factor, with random magnitude in [1/3, 3] and random phase; 1000 draws, normal ordering, m1 log-uniform in [1e-4, 1e-2] eV.

| Class | Median Δ | 16–84% | Median \|ΔU_μ1²\|, \|ΔU_τ1²\| | Source |
|---|---|---|---|---|
| Linear insertions | 0.039 | — | 0.036, 0.010 | `t4_leak_NO_min.out:2` |
| Trilinear, 8 sampled words | 0.039 | — | — | `:3` |
| Trilinear, all 414/342 | 0.22 | — | — | `t4_leak_NO_count.out:3` |
| Shared-doublet wavefunction | 0.0052 | — | 0.0035, 0.0030 | `t4_leak_NO_min.out:4` |
| **All combined (primary)** | **0.057** | 0.018–0.13 | 0.050, 0.014 | `:5` |
| All combined, every trilinear | 0.23 | — | — | `t4_leak_NO_count.out:5` |
| All at tree size | 0.55 | — | — | `t4_leak_NO_min.out:6` |

- For the primary set, P(Δ < 0.003) = 0.02, and the signed median shifts are +0.014 (μ) and +0.001 (τ).
- With m1 fixed at 1e-4 eV the result is the same (0.056). Inverted ordering is much worse: 0.195 overall, and 0.13 from the wavefunction term alone.
- **θ₁₃ fit.** I froze the leak operators, then re-solved the TM1 block angle θ by root-finding on [0.9, π/2] so that the perturbed sin²θ₁₃ = 0.0220. This worked in 81–100% of loop-size draws; draws with no root were kept and flagged. Since Δ = ||U_e1|² − 2/3|/c₁₃², the fit only matters at second order.

**5. Tuning.** t_req is the factor on loop-natural size that brings the median Δ to 0.003.

| Set | t_req (× loop size) | × tree size | Source |
|---|---|---|---|
| All combined (primary) | 0.051 | 3.3e-4 | `t4_leak_NO_min.out:11` |
| Plus vacuum misalignment | 0.045 | — | `t4_vacB.out:22` |
| Leading set plus misalignment | 0.059 | — | `t4_vacB.out:21` |
| Inverted ordering | 0.011 | — | `t4_leak_IO_min.out:11` |
| Every trilinear included | 0.0097–0.010 | 6e-5 | `t4_leak_NO_count.out:11`, `t4_vacB.out:23` |
| Wavefunction term alone | 0.61 | — | `t4_leak_NO_min.out:14` |

**6. Prior art** (templates only, from abstracts). None translates into framework vocabulary without an import.
- Altarelli–Feruglio: SUSY driving fields, U(1)_R and a Z₃ shaping symmetry ([hep-ph/0512103](https://arxiv.org/abs/hep-ph/0512103)). Three imports.
- Altarelli–Feruglio: the two flavons on separate branes of an extra dimension ([hep-ph/0504165](https://arxiv.org/abs/hep-ph/0504165)). There is no extra dimension here.
- Altarelli–Feruglio–Lin: local symmetries at orbifold fixed points ([hep-ph/0610165](https://arxiv.org/abs/hep-ph/0610165)). The lattice analogue (site versus bond centre) is not sequestered, because the generation index is a lattice momentum.
- Holthausen–Schmidt: cross contractions force a common subgroup; the fix is a larger group with an accidental symmetry ([1111.1730](https://arxiv.org/abs/1111.1730)). G is fixed here. Orders on which the axis half-turns act nontrivially are an unchecked lead, but they cannot remove P.
- King–Luhn and Luhn: S₄ alignments for TM2 and TM1 using driving fields ([1107.5332](https://arxiv.org/abs/1107.5332), [1306.2358](https://arxiv.org/abs/1306.2358)).
- Hagedorn et al.: keeping the alignment after soft SUSY breaking ([2312.07430](https://arxiv.org/abs/2312.07430)). Still needs SUSY.
- Feruglio, and de Medeiros Varzielas–King–Zhou: modular symmetry, with one modulus per sector ([1706.08749](https://arxiv.org/abs/1706.08749), [1906.02208](https://arxiv.org/abs/1906.02208)). That is separation by construction, and there is no modulus here.

## Labels
- **Proved:** the Schur obstruction; that the Majorana irreps are a subset of the Dirac irreps; the m_e bound; Michel stationarity; the ±1 joint stabilizer; that no internal unitary symmetry forbids the neutral-pair terms.
- **Checked:** all counts, the non-stationarity, every Δ and t_req distribution, the vacuum strata, and the axis rule below.
- **Suggested:** the 17ε estimate; that the nearest-neighbour rule blocks sequestering; the half-turn-charged order lead; the Lorentz cost of φ_ν's E part (0.42 of its norm, `t4_group.out:27`).
- **Comparator:** masses, Δm² and NuFIT ranges, all recalled rather than fetched.

**Side finding (checked; `t4_axis.out`).** TM1 does not need a bond-centred axis.
- A C₂[110] axis through the sites (0,1,0) or (1,0,0) also gives TM1.
- Axes through (0,0,0), (0,0,1), (1,1,0), or the face centre (½,½,0) give θ₁₃ = 0.
- The class is set by (c_x − c_y + 2c_z) mod 2, where c is a point on the axis.
- So the derivation's line 104 ("the same half-turn through a site gives θ₁₃ = 0") holds only for the even class.

## Deviations from the pre-registration
1. Added after the smoke run: the trilinear variant with all 414/342 operators, and Parts A and A2 (untuned vacuum strata).
2. In vacuum Part B, sampling for true local minima found 0 of 13. I replaced it with a first-order shift using a natural-stiffness surrogate (the absolute value of the symmetry-breaking Hessian). That part's stationarity tuning needed cubic coefficients, and it was not refit for θ₁₃.
3. I reran Part A after guarding against unbounded directions. The Z₃ count went from 58 to 89 of 300; the neutrino count stayed at 1 of 300.
4. I cut A2 to 4 pairs because the full version was projected to take 1–2 hours.
5. In the U(1)×U(1) runs, the within-sector potentials were left general.
6. The all-trilinear leak run crossed the 400 MB watchdog only after all its output was written.

## Files
Everything is in `masswall/T4/`:
- `PREREG_NOTES.md`
- `scripts/`:
  - `t4_core.py`, `t4_inv.py`
  - `t4_group.py`, `t4_count.py`, `t4_axis.py`
  - `t4_leak.py`, `t4_vacuum.py`, `t4_vacA2.py`
  - `run_all.sh`, `run_A.sh`, `capped.sh`
- Outputs:
  - `t4_group.out`, `t4_count.out`, `t4_axis.out`
  - `t4_leak_NO_min.out`, `t4_leak_NO_count.out`, `t4_leak_NO0_min.out`, `t4_leak_IO_min.out`
  - `t4_vacA.out`, `t4_vacA2.out`, `t4_vacB.out`
  - smoke outputs