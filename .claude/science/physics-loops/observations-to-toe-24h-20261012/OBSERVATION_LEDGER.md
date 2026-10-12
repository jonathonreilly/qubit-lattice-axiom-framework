# Primary observation inventory

Dated benchmarks checked during launch research on 2026-10-12. This is a starting inventory, not a claim to list the latest constraints. Primary links below were read by a focused observation-research agent. Verify exact inputs again when binding a numerical test.

| Observable and source | Benchmark | Inference boundary |
|---|---|---|
| [Hensen Bell test (2015)](https://arxiv.org/abs/1508.05949) | S=2.42 +/- 0.20; 245 trials; reported local-null p=0.039 | Setting-independence/locality assumptions; no unique ontology is selected |
| [Fein molecular interference (2019)](https://www.nature.com/articles/s41567-019-0663-9) | Interference with molecules above 25,000 Da, up to 2,000 atoms | Actual fringes, source velocities and environmental/apparatus response must enter a decoherence test |
| [MICROSCOPE (2022)](https://arxiv.org/abs/2209.15487) | Ti/Pt eta = (-1.5 +/- 2.3 statistical +/- 1.5 systematic) x 10^-15 | Composition- and instrument-specific, not by itself a derivation of GR |
| [GW170817/GRB170817A (2017)](https://arxiv.org/abs/1710.05834) | Arrival lag +1.74 +/- 0.05 s | Published speed interval [-3e-15,7e-16] depends on intrinsic gamma delay 0-10 s and conservative distance 26 Mpc |
| [Fan electron magnetic moment (2023)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.130.071801) | g/2 = 1.00115965218059(13) | Inferring alpha imports QED; it cannot calibrate its own independent g prediction |
| [Parker Cs recoil (2018)](https://arxiv.org/abs/1812.04130), [Morel Rb recoil (2020)](https://www.nature.com/articles/s41586-020-2964-7) | Inferred alpha inverse: Cs 137.035999046(27); Rb 137.035999206(11) | Recoil-to-alpha uses mass ratios/Rydberg input; preserve disagreement and shared inputs |
| [LEP/SLD Z-pole report](https://arxiv.org/abs/hep-ex/0509008) | Fitted N_nu = 2.9840 +/- 0.0082 | Cross-sections/asymmetries are observed; light-neutrino count uses SM partial-width interpretation |
| [Daya Bay 3158 days](https://arxiv.org/abs/2211.14988v1) | Fitted sin^2(2 theta13)=0.0851 +/- 0.0024; NO delta m32^2=(2.466 +/- 0.060)e-3 eV^2 | Energy/baseline spectra constrain a propagation family; fit parameters are not theory-independent observations |
| [Planck likelihood](https://arxiv.org/abs/1907.12875), [parameters](https://arxiv.org/abs/1807.06209) | Base-LambdaCDM H0=67.4 +/- 0.5 km/s/Mpc | Use observed spectra and nuisance likelihood; inferred expansion/density summaries inherit cosmology |
| [Cooke primordial deuterium (2018)](https://arxiv.org/abs/1710.11129) | D/H=(2.527 +/- 0.030)e-5, seven selected low-metallicity absorbers | Primordial extraction uses absorber/line assumptions; baryon-density inference additionally uses BBN and rates |

## Daya Bay available inputs and limitations

Source prefix: https://arxiv.org/src/2211.14988v1/anc/ . Ten files are linked: DayaBay_IBDPromptSpectrum_EH1_3158days.txt, EH2 and EH3 equivalents; DayaBay_BackgroundSpectrum_EH1_3158days.txt, EH2 and EH3 equivalents; DayaBay_DetectorModel_Etrue_to_Eprompt.txt; DayaBay_DeltaChiSq_NO_3158days.txt; DayaBay_DeltaChiSq_IO_3158days.txt; supplemental.tex.

The spectra are hall-aggregated after nonlinearity correction and split into 6/8/7-detector periods. Nobs includes background and fractional entries; it is not independent raw Poisson data. Npred is the collaboration's fitted background-subtracted prediction and must not be used as independent observation. The nominal response uses 50 keV bins; its true-positron/prompt energy convention must be checked before combining with corrected spectra. Full detector-level nuisance arrays and covariance have not been established available.

Each published chi-square grid has 10,000 rows. Agent-verified discrete minima: NO (0.085,0.002468,0.004), IO (0.085,0.002572,0.003), ordered as mixing amplitude, positive mass-splitting magnitude, delta chi-square. These are ingestion controls only; the grids apply only to the published oscillation family and their separately normalized minima do not test ordering or arbitrary alternatives.

One candidate survival-law family for a carefully qualified shape test is P_ee=1-A/2 [1-exp(-Gamma L) cos(2 kappa L (E/E0)^n)], testing n=-1,0,+1 separately and a monotonic alternative. Standard coherent mass oscillation is a control; any new law must satisfy its own probability/composition requirements. Forward-model baseline mixtures and detector response; do not assign full-likelihood significance to an incomplete approximate comparison.

For each selected test freeze candidate, calibration, model-selection and test roles; covariance; nuisance/range treatment; physical response map; decision rule; input hashes. Public known data reserved from fitting are model-development holdouts, not blind validation.
