# Panel E dossier: the chirality campaign at its midpoint (2026-10-15)

Jon asked for a 24-hour campaign on the chirality exercise. This panel sets direction for the second half. **Jon decides.** The panel advises only.

Standing rules:
- Axiom changes are named as prices, never adopted.
- The standard is that only observed physical outcomes need to be matched.
- Owner readings are thoughts, not rules.

## Where to read

All paths are read-only. Read files from the packet branch with:

`git -C /Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790 show origin/claude/chirality-grid-exercise-20261014:.claude/science/exercises/chirality-grid-20261014/<file>`

**Read in this order:**
1. SUMMARY.md, all of it, including §7 (round 2).
2. TESTS.md from "24-hour campaign, wave 1" to the end: every pre-registration, result and referee entry of this campaign.
3. The campaign reports: `campaign/{OBS2,OBS3,OBS4,CLS1,NT1P,NT1PP,QMC1,TOR1}/REPORT.md`, each with its `REFEREE_VERDICT.md` where present.
4. `combos/X2/COMBO_REPORT.md`: the corner package.
5. `panel_D/PANEL_D_SYNTHESIS.md`: the previous panel.
6. `docs/MINIMAL_AXIOMS_2026-06-29.md` in full, in that worktree.

## State of play (convened 2026-10-15 ~17:10Z)

Referee status is given in brackets: [ref ✓c] means confirmed with corrections by codex gpt-5.6-sol at xhigh; [unref] means not yet refereed.

### Route 2: X2 corner package (set C)

**Flavour and Lorentz violation**
- **OBS-2** [ref ✓c]: with OBS-1's textures, c_TT^d ≈ −2e-8 against a 1e-22 bound. Removing it needs about 1e-14 tuning.
- **OBS-3** [ref ✓c]: that result is texture-dependent. The universal-strength "B-gen" textures fit the masses, CKM and J exactly, with zero one-loop residual.
  - This holds within the one-loop family.
  - Open: FCNC, two-loop L-words, the "up-flat" case.

**FCNC**
- **OBS-4** [ref ✓c]: FCNC-PRICE.
  - **Selection rule:** corner-changing Yukawas need carriers at momentum Q_c + Q_c′ ∈ hw2.
  - **NFC lemma:** with exact translations, CKM is a permutation.
  - **D3 benchmark:** the electroweak-doublet carriers have |Ŷ_uc| ≈ 0.66. They need M* ≈ 1.3–7.9e3 TeV untuned, but exact translations remove the decoupling term, so the carriers come out naturally at TeV scale. The shortfall is at least 180, even tuned.
  - **The passing route is class S:** a lattice-scale singlet condensate, which breaks translations to BCC.
  - **Not established:** a universal ceiling, D6, general potentials.

**Class S**
- **CLS-1** [ref ✓c]: CLS-PRICE.
  - The BCC sectors are single-handed: {hw0, hw2} all R, {hw1, hw3} all L. So bilinears cannot pair corners.
  - But light–light density and kinetic operators share the Yukawa's translation charge and are allowed by every symmetry. Their coefficients are natural, not forced.
  - At natural size the bounds are exceeded by ×1e42 (dimension 3, unless a lattice CPT Θ is imposed) and by about ×1e26 (dimension 4). A one-loop toy regenerates a spread of about 2.9e-2 (referee-corrected).
  - The price is Θ plus about 1e-27 tuning.
- **Supervisor synthesis:** `campaign/CKM_CORNER_TENSION_SYNTHESIS.md`. The YY† spurion argument says no flavour symmetry can forbid the class-S kinetic mixing.

**Mirror gapping**
- **QMC-1** [unref; referee running]: a validated sign-free AFQMC (λ1 = 0, ungauged, global Spin(10)).
  - 2+1D, filter f2, L = 4 and 6, β = 4. Once the mirror gap opens (W ≳ 2), S10/L² is flat: ratios 0.98(5), 1.35(26), 0.87(10).
  - No SMG window was found, and there is no strong-coupling turnover up to W = 16 at L = 4 (K1's G1 seen numerically).
  - Mechanically OPEN by the registered estimator. GPR-PILOT by the replacement estimators.
  - Caveats: short statistics, Δτ artefacts, L ≤ 6, finite temperature.
  - Cost of a cluster run: 3+1D L = 8 needs about 5e4 core-hours per W per 1000 sweeps.

### Route 1: overlap / set B (Euclidean)

- **NT-1** [ref: NOT CONFIRMED]: the measure was not legitimate.
- **NT-1′** [ref ✓c]: a Lüscher measure for 11112 at Lx = 4 on open time.
  - RP is negative on 3/3 pools (22–49 × E), and the negativity sits in the modulus.
  - OPEN at G-LEG(b).
- **NT-1″** [ref ✓c]: OPEN at (b″). The open-time geometry obstructs a legitimate measure:
  - edge zero modes of H_W (a Chern insulator) block Wilson-line winding;
  - the edge tail is algebraic, about Lx⁻⁵;
  - on the torus, C(11112) = 0 and C(L1) = −1.
- **TOR-1** [running, due 21:00Z]: the periodic-torus chiral RP test, Lx ≥ 4.
- **Earlier context:** UV-1 found a lattice-scale tail; NT-2 found the hard plaquette bound is not RP in 3D; BLEAK-1 found Planck-size light-cone leaks for set B's RP-safe gravity bridge.

### Owner decisions still parked

D1–D4 from panel D (`panel_D/PANEL_D_SYNTHESIS.md`).

## Questions for the panel

1. **Route 2.** Given OBS-2, 3 and 4, CLS-1 and QMC-1: is X2 viable? What is its exact remaining price list? Is the CKM-versus-translation tension a structural no-go for corner generations, or a price?
2. **Route 1.** Given NT-1′, NT-1″ and TOR-1: is the overlap's RP failure now established for a legitimate chiral measure? What would remain to call set B's real-time branch closed?
3. **The second half (about 14 h).** Which three tests most change the picture? Pre-register their readings now.
4. **D1–D4.** Does anything here move the panel D advice?

## What each panelist must deliver

Work in your lens. Plain words first, then technical.
- Labels: proved / checked / suggested / reading / comparator.
- Cite path:line.
- Your folder is `.../scratchpad/chirality_ex/campaign/panel_E/<lens>/`.
- Tiny scripts only, under 200 MB.
- Do not edit any repository.

Deliver:
1. Your verdict on each question.
2. The strongest argument from your tradition, and the steelman against your verdict.
3. What evidence would change your mind.
4. One or two concrete next tests, with fixed readings.

Return within about 60 minutes. Your final text is your statement. Be direct; no flattery.
