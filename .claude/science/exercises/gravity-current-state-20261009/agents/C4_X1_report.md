# C4 lane RX, probe X1: where the 1e-19 m locality bar comes from, and whether ℓ_k ≈ 7e-19 m is excluded (worker report)

**Worker:** Claude Opus 5.5 (probe X1), the same model family as the exercise authors. **Unrefereed.** Worked 21:01–21:10Z on 2026-10-11. No repository file was edited. No files were downloaded: literature was read with WebFetch (arXiv abstract pages and ar5iv full text), plus the BBL 2015 text the E1 referee had already saved to scratch.

**Labels used:**
- VERIFIED: read in fetched text. Full text is marked "(ft)", the abstract only "(abs)". Numbers from full text were pulled out by a summarizer pass, not read line by line.
- VERIFIED-LOCAL: read in a repository or scratch file.
- CHECKED: my own arithmetic.
- RECALLED: from memory, not fetched this session.
- SUGGESTED: my reasoning, not proved.

## Verdict (worker)

**Reading against the FIXED X1 readings: BAR JUSTIFIED, conditional on universality.** "Universality" means the readout's ℓ_k is also the non-locality scale of Standard Model fields. That is E1's own setting: "fields live on events" and all propagate by Benincasa–Dowker-type operators.
- Under that reading, ℓ_k ≈ 7e-19 m means 1/ℓ_k ≈ 282 GeV. Every collider bound on Lorentz-invariant non-local form factors excludes it:
  - LEP: Λ > 1.0–1.6 TeV;
  - LHC 8 TeV Drell–Yan: Λ > 2.5–3 TeV;
  - CMS 13 TeV dijets: Λ > 4.7 TeV.
- In length that is ℓ ≲ 1.9e-19 to 4.2e-20 m. 7e-19 m misses these by factors of 3.6 to 17.
- Even the requirement from the **proved** constant (c_low = 0.63, which gives ℓ_k ≥ 4.0e-19 m, i.e. 493 GeV) is excluded, by factors of 2 to 10.
- If anything, the E1 bar of 1e-19 m is **looser** than current data (4.2e-20 m), not stricter.

**If ℓ_k belongs to the gravitational readout only, the reading would be "bar too strict".**
- Then no current bound excludes 7e-19 m. Gravitational non-locality is bounded only at about 5e-5 m (torsion balances). GW dispersion over 1 Gpc is blind to it: (kℓ_k)² ~ 1e-48 at 100 Hz.
- But that is a different model: a species-dependent ℓ_k with gravity alone non-local at the mesoscale. Per the fixed readings it needs a new dated pre-registration.
- Such a model must also face the same noise theorem for **light**. The RL readout is the propagator of a lensed massless wave, and light is the wave whose √Δ lensing is observed. The photon's ℓ_k is collider-bounded to ≲ 8e-20 m. Whether the photon noise then fails depends on the effective source extent for light (see §4). I did not settle this.

**The non-collider bounds do not give a robust exclusion.**
- Optomechanical bounds claimed from Bawaj et al. third-harmonic data (2e-22 to 1e-29 m) would exclude 7e-19 m by a wide margin. They assume a macroscopic oscillator's centre of mass obeys the non-local Klein–Gordon/Schrödinger law with its **total** mass. With a nucleon mass instead, the same data give only 2e-14 to 1.3e-18 m, which excludes nothing (CHECKED rescaling).
- The Unruh–DeWitt/nuclear proposals are projections, not measurements.

## 1. Origin of the 1e-19 m bar (VERIFIED-LOCAL, plus VERIFIED (ft) for the literature step)

- **First appearance in the packet.** Commit `b08bd6f9f0` (2026-10-09 13:02 −0400, "E1 … pre-registered at owner request") added TESTS.md:176: "Use about 1e-19 m (the LHC) as the locality bar." This is E1(d), "What ℓ is required, and is it below the scales where locality is tested?"
- **The supervisor's use.** `agents/supervisor_thread.md:45` uses "the LHC locality bar of 1e-19 m" in the power-count follow-up. No citation is given anywhere in the packet: a grep for Biswas, Okada, 1512.02083, optomech, Krasnikov or collider in the exercise folder finds only the X1 tasking. The E1 referee files make no comment on the bar's value. C3 G-A's referee noted that the bar was "not needed" for that FAIL (TESTS.md:601).
- **Literature origin (VERIFIED (ft)).** The number is the one causal-set phenomenology uses. Belenchia, Benincasa, Liberati, Marin, Marino, Ortolan, *PRL 116, 161303 (2016)*, arXiv:1512.02083, state the current LHC constraint as ℓ_k ≤ 1e-19 m, citing Biswas & Okada.
- **The same figure elsewhere.** Belenchia, Benincasa, Martín-Martínez, Saravani (arXiv:1605.03973, *PRD 94*, 061902) repeat "ℓ_n ≲ 1e-19 m … of the same order as present constraints … from LHC data", also citing Biswas–Okada (VERIFIED (ft)).
- **The underlying bound.** Biswas & Okada, *Nucl. Phys. B 898 (2015) 113*, arXiv:1407.3331 (VERIFIED (ft)), get M ≳ 2.5 TeV for e^{−s/M²} and ≳ 3 TeV for e^{+s/M²}.
  - Data: ATLAS 8 TeV Drell–Yan pp → γ*/Z → e⁺e⁻, 21.7 fb⁻¹.
  - The form factor sits on the photon and Z propagators of a toy non-local Standard Model.
  - Their LEP comparison is ≈ 1.62–1.63 TeV.
  - ħc/2.5 TeV = 7.9e-20 m (CHECKED). So "1e-19 m" is a rounded-up version of an 8 TeV Drell–Yan bound on the **electroweak gauge sector**.

## 2. Bounds on ℓ_k from the literature, with assumptions

| # | Source | Bound | Observable | Form factor | Sector | Status |
|---|---|---|---|---|---|---|
| C1 | Krasnikov, hep-ph/9503220 (1995) | Λ_nl > 1020 GeV (95% CL), i.e. ℓ < 1.9e-19 m | LEP precision data (process not named in the abstract) | non-local scale Λ_nl | leptons, quarks, gauge bosons | VERIFIED (abs) |
| C2 | Biswas–Okada 2015, arXiv:1407.3331 | M > 2.5 TeV (e^{−s/M²}) or 3 TeV (e^{+s/M²}), i.e. ℓ < 7.9e-20 or 6.6e-20 m. LEP: 1.62 TeV, i.e. 1.2e-19 m | ATLAS 8 TeV Drell–Yan M_ee spectrum, 21.7 fb⁻¹ | exponential, entire function | γ and Z propagators (toy model) | VERIFIED (ft) |
| C3 | Anderson–Carone, *PRD 110, 055018 (2024)*, arXiv:2406.12073 | Λ_nl > 4.7 TeV in the non-local limit (4.9 with CTEQ6.1), i.e. ℓ < 4.2e-20 m. Asymptotically non-local N = 30: > 4.2 TeV | CMS 13 TeV dijet invariant mass (arXiv:1911.03947) | f₁(p²) → e^{−ℓ²p²}, ℓ = 1/Λ_nl | gluons, quarks (kinetic and mass terms) | VERIFIED (ft) |
| O1 | Belenchia et al. PRL 2016 (cooled membrane, Lecocq et al. 2015 data) | ℓ_k < 2e-15 m | ground-state occupation; ε = mωℓ_k²/ħ < 0.2 | general analytic f(□), b₂ = 1 | centre of mass of a 50 pg membrane, total mass | VERIFIED (ft) |
| O2 | same, from Bawaj et al. 2015 third-harmonic data | ℓ_k ≲ 2e-22 m (m = 2e-11 kg) to 1e-29 m (m = 3e-5 kg) | third harmonic of macroscopic oscillators | same; assumes no cancellation with structural non-linearities ("worst case") | centre of mass, **total** mass | VERIFIED (ft) |
| P1 | Belenchia–Benincasa–Martín-Martínez–Saravani 2016, arXiv:1605.03973 | **projections only:** ℓ_n ≲ 1e-19 m (20 g ²⁰Na, Δ ~ 1e-10) to 1e-25 m (200 g) | spontaneous emission of an MeV detector | non-analytic, retarded (causal-set-inspired ρ and exponential ρ) | one real scalar, Unruh–DeWitt monopole coupling | VERIFIED (ft) |
| G1 | infinite-derivative gravity, torsion balance (quoted in arXiv:1805.03559) | M_s > 0.004 eV, i.e. ℓ ≲ 5e-5 m | short-range gravity | e^{−□/M_s²} in the graviton kinetic term | gravity only | VERIFIED (search snippet only) |
| G2 | IDG–Starobinsky, arXiv:1611.05062 | M > 1.18e14 GeV | CMB r, n_s | IDG with R² inflation | gravity and inflaton, model-specific | VERIFIED (search snippet only); does not transfer |

Also searched, with no bound found:
- Saravani–Aslanbeigy, "Dark matter from spacetime nonlocality" (arXiv:1502.01655): the scale Λ is a free parameter, with no number or bound (VERIFIED (ft), first 100k characters).
- Sorkin 2007 (gr-qc/0703099): the abstract gives no number (VERIFIED (abs)). E1's attribution of "about 1e-14 m" to its body is not verified here.
- I found no 2020–2026 measured bound specific to causal-set ℓ_k (search, not exhaustive).

**Strongest bounds:**
- Robust (collider, matter sector): **ℓ ≲ 4.2e-20 m** (C3, exponential form factor on QCD), or 7.9e-20 m on the electroweak gauge sector (C2).
- Claimed but assumption-laden: O2, down to 1e-29 m.
- Gravity-only: G1, about 5e-5 m.

## 3. Does the collider bound transfer to the Benincasa–Dowker form factor? (SUGGESTED, order of magnitude)

- **The conventions match.** In BBL 2015 (local copy `scratchpad/referee_E1/lit_bbl2015/bbl2015.txt:262-289`, VERIFIED-LOCAL), ℓ_k = ρ^{−1/d}. In 4D the IR expansion is f(□) = □ − (3/(2π√6)) (□²/√ρ) [3γ − 2 + ln(3□²/(2πρ))] + …, with √ρ = ℓ_k^{−2}. This is the same ℓ_k convention as E1/RL (ε = (ℓ_P/ℓ_k)⁴, ρ_k = ℓ_k^{−4}).
- **The BD correction is at least as large as the exponential one at low pℓ_k.** The relative correction is about −0.195 (pℓ_k)² [ln(0.48 (pℓ_k)⁴) − 0.27], which is log-enhanced (CHECKED):

| pℓ_k | BD correction | exponential factor (pℓ)² |
|---|---|---|
| 0.1 | −2.0% | 1.0% |
| 0.32 | −11% | 10% |
| 0.74 | −24% | 55% |

- **Size of the effect at ℓ_k = 7e-19 m (CHECKED):**
  - Z pole: pℓ_k = 0.32, about a 10% distortion against a lineshape measured at the per-mille level.
  - LEP2 (√s ≈ 209 GeV): pℓ_k ≈ 0.74, an O(25%) change in e⁺e⁻ → f f̄.
  - LHC TeV scale: pℓ_k ≈ 3.5, so the propagators are fully non-local.
- **Why the transfer is not exact:**
  - The BD kernel is retarded and non-analytic. It has a branch cut, with a continuum of off-shell massive modes (Saravani–Aslanbeigy), and complex-mass modes in 4D (BBL).
  - A Feynman (in-out) propagator for it is not established. BBL say this remains to be constructed.
  - No dedicated BD-form-factor collider analysis exists (none found).
  - The extra continuum would add signals (missing-energy-like off-shell production), not remove them.
- **Conclusion:** for any field that propagates by a BD-type operator, 282 GeV is excluded by an order-of-magnitude margin. That is far more than the O(1) form-factor ambiguity.

## 4. Must the same ℓ_k enter matter propagation? (SUGGESTED)

- **What the substrate fixes and what it does not.** The discreteness scale ℓ (= ℓ_P) is common to the substrate. The smearing scale ℓ_k is a per-operator phenomenological parameter: BBL call it "a purely phenomenological parameter" (VERIFIED-LOCAL, bbl2015.txt:89). E1's own check ran two species with ℓ_k = 1 and 2 on the same sprinklings (E1_report.md:31). So the packet's setting already allows a species-dependent ℓ_k.
- **No radiative tie.** Matter loops shift the graviton kinetic term only at relative order (k/M_P)². So a gravity-only ℓ_k of 7e-19 m is not forced down to the matter value at the EFT level.
- **But the RL readout is not GW-specific.** It is the per-sprinkling inverse of a stable layer operator, i.e. the retarded propagator of a lensed massless wave. Observed √Δ lensing is mainly of light.
  - If light propagates on the same event substrate, its operator has ℓ_k^γ ≲ 7.9e-20 m (C2, photon/Z).
  - The RL3b/RL4 scaling then applies to light: n ≈ 281 · √((2Ds + s²)/(2D · 10 km)) · (1e-19 m/ℓ_k)³ sd e-folds. This takes the RL constants at face value; RL4 proved c_low = 0.63, and the table uses the node-ladder value about 2.7.
  - At ℓ_k^γ = 7.9e-20 m (CHECKED):

| effective source extent s | n (sd e-folds) |
|---|---|
| 0.3 m (single-atom emission, ~ns) | ≈ 3 |
| 10 km | ≈ 570 |
| 3e5 m (ms-coherent radio, e.g. an FRB) | ≈ 3e3 |

  - So a gravity-only escape is open only if the effective s for observed coherent light is atomic-scale. Defining s for an incoherent source is an open modelling step. It is not settled here.
- **The other way to escape.** Matter could propagate by a different, local mechanism while gravity alone is read out from the order with a mesoscale ℓ_k. That is a two-sector substrate, not E1's setting.

## 5. Map to the FIXED readings

- **Bar justified:** some bound excludes 7e-19 m, namely C1–C3 (and O2, with caveats), provided ℓ_k is the matter-sector non-locality scale as in E1's setting. **This is my reading.**
  - Margin: ℓ_k(required) / ℓ(bound) ≈ 3.6 (LEP), 9 (LHC Drell–Yan), 17 (CMS dijets).
  - It holds even at the proved constant (4.0e-19 m) and at other source extents (1.7e-18 m for a 100 Hz cycle, 8e-18 m for 100 s), which are excluded by more.
- **Bar too strict:** this holds only for a gravity-only ℓ_k, where the strongest bound is about 5e-5 m. Per the fixed readings, it is a new model needing a dated pre-registration, and it must pass the photon-noise check in §4.
- Per the TESTS.md X1 rule, no lane PASS/FAIL changes on the basis of X1. E1's readings stand.

## 6. Open items for a referee

1. Collider bounds are for entire exponential form factors. A BD-specific (retarded, non-analytic) collider computation would make the transfer rigorous.
2. Krasnikov 1995 was read as an abstract only. I did not check which LEP observable it uses, or whether it assumes local or non-local fields (the abstract wording is ambiguous).
3. Optomechanical O2 depends on the composite-mass assumption. Kumar & Plenio (*Nat. Commun.* 2020, doi:10.1038/s41467-020-17518-5, arXiv:1908.11164; VERIFIED (abs)) show that the scaling with the number of constituents is unknown and must itself be bounded.
4. The photon-sector noise in §4 needs a definition of the effective source extent for incoherent light. This is the decisive input for the gravity-only escape.
5. The G1 and G2 gravity-only numbers come from search snippets, not full text.

## Sources
- [Belenchia et al. PRL 116, 161303 (2016), arXiv:1512.02083](https://arxiv.org/abs/1512.02083) ([ar5iv](https://ar5iv.labs.arxiv.org/html/1512.02083))
- [Biswas & Okada, NPB 898 (2015), arXiv:1407.3331](https://ar5iv.labs.arxiv.org/html/1407.3331)
- [Anderson & Carone, PRD 110, 055018 (2024), arXiv:2406.12073](https://arxiv.org/html/2406.12073v1)
- [Krasnikov, hep-ph/9503220](https://arxiv.org/abs/hep-ph/9503220)
- [Belenchia, Benincasa, Martín-Martínez, Saravani, arXiv:1605.03973](https://ar5iv.labs.arxiv.org/html/1605.03973)
- [Saravani & Aslanbeigy, arXiv:1502.01655](https://ar5iv.labs.arxiv.org/html/1502.01655)
- [Belenchia, Benincasa, Liberati, JHEP 2015, arXiv:1411.6513](https://arxiv.org/abs/1411.6513) (local copy)
- [Belenchia et al. CQG 36, 155006 (2019), arXiv:1901.05819](https://arxiv.org/abs/1901.05819) (abstract only; no revised numbers)
- [Kumar & Plenio, arXiv:1908.11164](https://www.arxiv.org/abs/1908.11164)
- [Sorkin, gr-qc/0703099](https://arxiv.org/abs/gr-qc/0703099)
- [arXiv:1805.03559](https://arxiv.org/pdf/1805.03559) and [arXiv:1611.05062](https://arxiv.org/pdf/1611.05062) (snippets)
