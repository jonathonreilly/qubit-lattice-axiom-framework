# HIER-2 PREREG: fermion mass hierarchy on the scale ladder

Written 11:40Z, 2026-10-18, before any run. Worker: Claude Opus 5.5 (test agent; same family as the supervisor, not independent).
Deadline (corrected by the coordinator): 17:30Z.

## Item and fixed readings (TESTS.md, packet copy `../packet/TESTS.md`, HIER-2 block)

Question: can protected masses (PR #9702 item 4: m proportional to the breaking) plus breaking entering at different rungs or orders give the observed charged-fermion ratios, m_i ∝ ε^{n_i}, integer n_i set by symmetry, ε a ladder parameter?

- MASS-DERIVED: symmetry fixes the n_i; with at most 2 continuous parameters all 9 charged-fermion masses within a factor 3; CKM consistent with the structure, at least its hierarchy pattern.
- MASS-PARTIAL: the pattern holds for one sector, or within a factor of 10.
- MASS-NO: a proof that the class cannot produce it.
- OPEN: otherwise.

I did not read `SUPERVISOR_PREDICTION.md` on the packet branch, to keep this test blind.

## Prior art read before this PREREG (main unless stated)

- `docs/CHARGED_LEPTON_MASS_HIERARCHY_REVIEW_NOTE_2026-04-17.md`: hw=1 triplet; leptons accommodated only by an observational pin; S2 residual; three named missing primitives.
- `docs/YT_GENERATION_HIERARCHY_PRIMITIVE_ANALYSIS_NOTE_2026-04-18.md`: Outcome D (C3-commuting operators have equal position-basis diagonals) with the §0 circulant correction; §3.4 geometric ε ladders need three different ε per sector when n = (0,1,2); §4.3 the three sector columns are not proportional.
- `docs/YT_CLASS_7_SPONTANEOUS_C3_BREAKING_NOTE_2026-04-18.md`: no spontaneous C3 breaking on the retained surface; the taste staircase is generation-symmetric at every rung.
- `docs/CKM_FROM_MASS_HIERARCHY_NOTE.md`: GST bounded reading; E5: an FN charge approach with ε = 1/3 gives |V_us| = |V_cb|.
- `docs/QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md`: down-type closed forms in α_s(v); 2026-09-30 corrigendum (common-scale m_s/m_b off by about 19%).
- `docs/HIERARCHY_VALUE_FRONTIER_PROBE_2026-06-05.md` §4: FN readout of lepton Yukawas with ε = α_bare gives q ≈ (5.03, 2.93, 1.81), flagged as a loose observation and an unauthorized import.
- `docs/PRIMITIVE_P_HEAVYQ_SPECIES_PROPOSAL_NOTE_2026-05-10_pPheavyq.md` §2.2: FN on α_LM with integer exponents, runner verdict WEAK.
- `docs/GST_TEXTURE_REDUCES_TO_RANK1_C3_SYMMETRIC_MASS_LIGHT_MASS_FROM_BREAKING_NARROW_THEOREM_NOTE_2026-06-08.md` and `docs/RANK1_SINGLE_SOURCE_TEMPLATE_FROM_K_J_MINUS_I_STRUCTURE_GST_HIERARCHY_LOCATOR_NOTE_2026-06-08.md`: rank-1 C3-symmetric mass plus one breaking source gives a see-saw light mass at second order and sin θ = √(m_l/m_h).
- `docs/historic_intake/HISTORIC_EWSB_GENERATION_CASCADE_NOTE_INTAKE_NOTE_2026-08-05.md`: historic S3 → Z2 cascade; loop suppression 1 : 0.0027 : 7.3e-6 against 1 : 0.0073 : 1.3e-5.
- `docs/YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md`: Yukawa unification at M_Pl overshoots m_b by about 33x.
- Branch `claude/chirality-grid-exercise-20261014`: `campaign/GEN1/REPORT.md` (X2′: generations as an internal label at Γ; Yukawas arbitrary; "the 3 is put in by hand") and `campaign/sf_referees/GEN1_GEN2_LOCK1.md` (GEN-2: axis/rod placement; O_h-invariant Y = a·1 + b·J has a degenerate pair).
- PR #9702 note (branch `claude/scale-ladder-20261018`): item 4 (O × I protects the quartet; A2 term gives a gap linear in ε), item 7 (eight cube points: orbits {k*}, {−k*} with little group O, two 3-orbits with little group D4), the doubler chiralities, and "relevant couplings ... transported by the ladder but never fixed by it".

## Supplied inputs (all listed)

1. Masses, recalled, not fetched (comparator data only):
   - Set M_Z (Xing–Zhang–Zhou 2008, SM running at M_Z, in GeV): u 1.27e-3, d 2.90e-3, s 0.055, c 0.619, b 2.89, t 171.7; e 0.48657e-3, μ 0.102718, τ 1.74624.
   - Set GUT (same source, SM at 2e16 GeV): u 0.48e-3, d 1.14e-3, s 0.022, c 0.235, b 1.00, t 74.0; e 0.469652e-3, μ 0.0991466, τ 1.68558.
   - Set MIX (main's `YT_GENERATION_HIERARCHY_PRIMITIVE_ANALYSIS_NOTE` §4.1 values): u 2.16e-3, d 4.67e-3, s 0.0934, c 1.27, b 4.18, t 172.69; e 0.511e-3, μ 0.1057, τ 1.777.
   - CKM magnitudes (recalled): |V_us| 0.225, |V_cb| 0.041, |V_ub| 0.0037.
2. Comparator model for the numerical illustration: the naive lattice Weyl fermion H(k) = Σ_j sin k_j σ_j on Z³. It has the same node and charge structure as PR #9702 item 7 (eight cube-point nodes, chirality (−1)^{hw}, Z2³ translation characters, little groups O and D4) and as main's hw grading. It is not the corner model, and its spinor (PSG) action is the ordinary SU(2) one. Results from it are labelled comparator-model results.
3. Parameter counting: an overall scale Λ and one breaking amplitude ε are the 2 continuous parameters. O(1) coefficients are set to 1 unless a symmetry fixes them. Tolerance: factor 3 per mass (MASS-DERIVED) or 10 (MASS-PARTIAL).

## Class under test (stated before any run)

Class L (ladder class). The fermions are node states of a symmetric lattice fermion. Their masses vanish in the symmetric theory (PR #9702 item 4). The breaking is a lattice spurion: a term with a translation character (momentum Q) and a point-group transformation, of amplitude ε. The ladder's symmetries (translations, point group, PSG) act on lattice labels only, identically on every internal (sector) label.

Generation placements covered:
- P-int (X2′): generation is an internal label; the ladder's symmetries act trivially on it.
- P-lat: generations are lattice labels forming orbits of the point group (main's hw=1 corners; the PR's three D4 doubler pairs; GEN-2's rods).

Subclass L1: one period-2 spurion (Q ∈ πZ2³) in one irrep, with a symmetry-fixed direction (its stabiliser fixes a single line).

## Planned analyses (in this order; every run via `zsh scripts/capped.sh OUT python3 ...`, one at a time)

- A1 (fit and density control; `fit_control.py`). For free integers n_i ≥ 0 and per-sector assignments, find the ε range where all 9 masses fit within ×3 (and ×10), the smallest possible maximum exponent N*, and the same for one sector. Control: the fraction of random log-uniform 9-mass spectra over the same range that admit a free-integer ×3 fit. Prediction: free-integer fits are generic once ε ≳ 0.1, so a fit carries no evidence unless the n_i are derived.
- A2 (sector blindness; proof plus arithmetic in `fit_control.py`). If the n_i and the coefficients are sector-independent, every generation's three sector masses must lie within a factor 9 (×3 tolerance) or 100 (×10) of one another. Compute the observed spreads in sets M_Z, GUT and MIX. With sector-common coefficients, U_u = U_d, so V_CKM = 1.
- A3 (symmetry-fixed orders; `orders_group.py`). Build O_h and D4h with explicit irreps. For each irrep R and each symmetry-fixed direction φ in R, and each target irrep T, find the smallest order n ≤ 9 at which a G-equivariant degree-n map R → T is nonzero at φ (random-polynomial group averaging), restricted to the parity allowed by the translation charge. Report the set of distinct finite orders per (R, φ). Prediction: at most two distinct finite orders, {1, 3}.
- A4 (comparator-model illustration; `naive_spurion_orders.py`). Naive Weyl fermion on the L = 4 torus with a menu of period-2 single spurions (on-site σ_μ and nearest-neighbour bonds, four charge classes). Measure the 16 low levels at ε = 4e-3, 2e-3, 1e-3. Fit each level's order in ε and record degeneracies. Prediction: the orders are 1 or 3 (or the level stays at zero), and with one spurion there are never three distinct non-degenerate generation masses at three distinct orders.
- A5 (ladder-ratio lemma; proof in the report). A mass is the q → 0 gap, so a factor (a/w)^p, which multiplies q^p, cannot set a mass. So ε must be a breaking amplitude, which the ladder transports but does not fix (PR #9702).

## Decision rule (fixed now)

- MASS-DERIVED needs n_i derived in A3/A4 (not fitted), all 9 within ×3 with Λ and ε only, and a nontrivial CKM hierarchy.
- MASS-PARTIAL needs the same derived n_i to fit one sector within ×3, or all 9 within ×10.
- MASS-NO: if A2 proves sector-blind failure at ×3 for every assignment, and A3/A4 show that L1 gives at most two distinct symmetry-fixed orders, I read MASS-NO for class L1 with sector-blind couplings, and state the scope exactly.
- OPEN: for classes outside L1 (multi-period supplied textures, internal flavour symmetries), flagged as such.
- My prediction before running: MASS-NO for L1 plus sector blindness; OPEN outside it; P-int gives no symmetry-fixed n_i at all.
