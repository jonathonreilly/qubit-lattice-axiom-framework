# C5 R13-8: set C's one-loop tuning count (Z³ × ℝ, nearest-neighbour or box, QED plus the N-type graviton)

**Probe.** R13-8 of campaign C5, round 13. The pre-registration is at `TESTS.md:4749-4758`.
- Run by Claude Opus 5.5 (same family as the other C5 workers), 2026-10-12, 20:48Z to about 21:25Z.
- **Not refereed.** No repository file was edited.

**Labels.**
- **proved**: an argument given here that is complete under its stated hypotheses.
- **checked**: a computation that ran here.
- **refereed**: a codex verdict in the packet.
- **worker**: an unrefereed packet result.
- **comparator**: a published number. It is marked "fetched" (verified via web this session or by a cited referee) or RECALLED.
- **suggested**: argued, not proved.
- **reading**: an interpretation.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`
- `S/` = scratch `C5/R13-8/`. Scripts and outputs are in `S/scripts/`.

---

## 0. In plain words

- **Results.**
  - I counted, by symmetry, every Lorentz-violating number that set C (a 3D cubic grid with separate time and only proper rotations, carrying an electron, light and the N-type graviton) allows at the renormalizable level.
  - I then checked which of those numbers one loop actually produces.
- **With a mirror- and time-symmetric matter law (like F2's QED)**, there are **8** numbers to cancel, plus the ordinary cosmological constant:
  - the electron–light speed difference;
  - the graviton–light speed difference;
  - **three** direction-dependences of the graviton's speed (not two);
  - two graviton masses;
  - one "vacuum pressure is not minus vacuum energy" tadpole.
- **What one loop was shown to produce.** Seven of the eight are shown nonzero at one loop. The eighth, the T₂g graviton mass, is exactly zero at one loop for the local coupling V3 used. Whether it appears depends on the coupling.
- **With a generic law in the axioms' class (no mirror or time symmetry)**, three more must be cancelled: a handed energy offset b₀, a handed speed d₀₀, and graviton birefringence. That makes 11. Two further graviton terms and light's k_AF are probably forced to zero by vacuum stability.
- **One structural fact (checked).** If the graviton's gauge symmetry were exact, the only Lorentz-violating graviton number left would be its overall speed. Every graviton mass, anisotropy and birefringence is a symptom of the coupling failing its gauge identity. That failure is the grid's boost obstruction.
- **Each extra charged species adds one speed**, plus two more if handedness is present. The graviton block does not grow. So:
  - N_tune = N_s + 7 (+ the cosmological constant) for mirror- and time-symmetric laws;
  - N_tune = 3N_s + 8 for generic ones.
- **Verdict: OPEN.** The count is explicit, but not every coefficient is shown generated at one loop in one law:
  - the T₂g mass depends on the coupling;
  - the handed coefficients were not computed;
  - the graviton witnesses use couplings that are not gauge-complete.
- **The old "≥ 6".** It survives as a lower bound (reading). Its "3 graviton speeds" is really 1 match plus 3 anisotropies (= 4). It also missed the tadpole.

---

## 1. Class, hypotheses, outside realizations

**Class (fixed by `TESTS.md:4749-4755`).**
- Z³ × ℝ, with a Hermitian, finite-range lattice law (nearest-neighbour, or R7-1/R8-2 box symbols).
- Covariant under translations and the 24 proper cubic rotations (`AX:38,57-58`). No inversion and no antiunitary symmetry is required.
- Time translation in a preferred frame. Time is downstream content (`AX:185`); Admissibility is not a dynamics axiom.
- Content: one charged Dirac species, a U(1) photon, and the N-type graviton (lapse, shift, h_ij; linearized-diffeomorphism Ward structure, `C5_R9-9_referee_verdict.md:5`).

**Hypotheses.**
- **(H-EFT)** The IR is a local EFT. Lorentz-violating coefficients are counted at dimension ≤ 4 for matter and photon, and up to two derivatives for the graviton (degrees 0, 1, 2 in p).
- **(H-1st)** The dispersion counts are first order in the Lorentz-violating coefficients (on-shell TT projection). TT–longitudinal mixing enters only at second order or through the longitudinal sector.
- **(H-tune)** "Must be tuned" means: allowed by the law's exact symmetry, generically generated at one loop, and observationally bounded below its natural size. The count is an operator codimension (K1's convention, `C4_K1_referee.md:15`).

**Outside realizations not covered.**
- Dimension ≥ 5 coefficients. They are listed only where the packet has them (R6-5's d = 5 photon term).
- Two-loop structures.
- Non-equilibrium vacua.
- Non-on-site U(1) charges.
- Chiral lattice content.
- Nonlinear graviton completions.
- Supersymmetric or paired spectra (R10-1/R11-1: pairing cancels some A-moment coefficients, not the electron's).

---

## 2. Prior art (each counted once)

| Source | What it gives | Used as |
|---|---|---|
| `SUMMARY.md:435`; `PRICE_NOTE.md:311-314,358` | "≥ 6" = 2 TT + ≥1 QED + 3 graviton speeds; K1 worker assembly; a reading | The claim under test |
| `C5_R10-1_referee_verdict.md:15` | "six tunings" is bookkeeping, not derived | Why R13-8 exists |
| `C4_F2_referee.md:7-9,39-42,62` (refereed) | One dim-4 speed per multiplet under O. No photon dim-4 birefringence. d₀₀ allowed. b₀ and (k_AF)₀ allowed by proper O. c_e − c_γ = −8.55e-3. SM bookkeeping: 9 speeds, or 49 with flavour matrices | Rows 1, 9, 10; per-species scaling |
| `C4_K1_referee.md:3,9,15` (refereed) | Z⁴: 3 + 9 forms, codimension 11, Euclidean-TT rank 5; one loop gives "one non-EH vector" | Validation target for my form code; the codimension convention |
| `C5_O1_referee.md:7` (refereed) | Proper O × time: (V, S2) = (1, 2); 6 mass and 30 kinetic h-forms (O_h × T: 26) | Reproduced below |
| `R2_referee.md:29`; `TESTS.md:757` (refereed) | Z³ graviton speeds "3, or 4 without P/T", a local codimension in R2's S/S-tl models | Compared: the general Ward-defect count is 4 (+1) |
| `C5_R9-9_referee_verdict.md:12,21,23,27` (refereed) | The box graviton's Ξ ≠ 0. E_g ≠ T_2g at axial q (a "robust graviton-sector speed anomaly"). The mass split is narrow (minimal-metric seagull only) | Anisotropy and mass evidence (axial only) |
| `TESTS.md:1779-1802` (V3, refereed) | Free local coupling: μ_E = 1.97e-3; μ_T2 = 0 (Liouville) | Rows 6–7 |
| `TESTS.md:859` (RN L2, refereed with corrections) | μ_T2 = +1.61e-8 λ² at O(λ²), coupling-design dependent | Row 7 (two-loop-type order) |
| `C5_R11-3_referee_verdict.md:45-47,79` (refereed) | "two independent tadpole renormalization conditions in the linear preferred-time EFT"; w ≥ 0 | Row 8 |
| `C5_R6-5_report.md:115,142,225,237`; `TESTS.md:3264-3268` (worker) | b₀ generated across species at O(g²) (χ₅ = −0.507 a⁻²), 43–49 decades, ≥ 3 conditions. (k_AF)₀ protected by stability plus Bloch. The d = 5 photon term is about 10 decades (suggested) | Rows 9, 14 |
| `C5_R13-5` (`TESTS.md:4707-4716`, refereed) | Ward-complete second-order pair stress blocked (W2); the graviton–matter split is OPEN | Why the graviton witnesses are not Ward-complete |
| `C5_R10-1_referee_verdict.md:9,11` (refereed) | Box paired electron residual δc_e·16π² = −10.66 to −17.96. Lemma N(m): one fixed shape cannot vanish on a mass interval | Box row 1; per-species independence |

---

## 3. Results

### 3.1 Symmetry count (checked: `r138_forms.py` → `r138_forms.out`)

**Matter and photon tensors under proper O, time fixed.**
- One invariant vector (time).
- Two symmetric rank-2 invariants: the η-trace and u⊗u.
- No antisymmetric rank-2 invariant.
- Two invariants of g_{λμν}.
- Photon: three O-invariant quadratic forms on (E, B): E·E, B·B and E·B.

**What survives**, after removing:
- the Lorentz-invariant parts;
- the θ total derivative E·B;
- the single-species unobservables a₀, e₀, f₀ and the g trace (field redefinitions, comparator RECALLED: Colladay–McDonald 2002, Altschul 2006).

| Field | Allowed Lorentz-violating coefficients (dim ≤ 4) | P, T |
|---|---|---|
| Dirac | c₀₀ (isotropic speed) | even |
| Dirac | d₀₀ (chirality-dependent speed) | P-odd |
| Dirac | b̃₀ = b₀ ⊕ totally antisymmetric g (they enter together; comparator RECALLED, the KR b̃_T combination) | P-odd, CPT-odd |
| Photon | κ_tr (isotropic speed); **no dim-4 birefringence** (no traceless rank-2 invariant) | even |
| Photon | (k_AF)₀ | P-odd, CPT-odd |

**Graviton quadratic forms.** These are the invariant polynomials Π(p) on h_μν. Gauge-invariant means Π(p)G(p) = 0 for δh = p⊗ξ + ξ⊗p. The on-shell TT rank is dispersion-relevant at first order.

| Group | Degree 0 (masses) | Degree 1 | Degree 2 | Gauge-invariant (deg 2) | On-shell TT ranks: deg 0 / 1 / 2 | Tadpoles |
|---|---|---|---|---|---|---|
| W(B4) on Z⁴ (validation) | 3 | 0 | 9 | 1 | TT rank 2 / 0 / 4 (off-shell, Euclidean) | 1 |
| **Set C: O × time** | **6** | **8** | **30** | **2** | **2 / 2 / 5** | **2** |
| O_h × T on Z³ × ℝ | 6 | 0 | 26 | 2 | 2 / 0 / 4 | 2 |

**Validation (checked).**
- W(B4) reproduces K1 exactly: 3 masses, 9 two-derivative forms, 1 gauge-invariant form, codimension 3 + 8 = 11.
- The TT conditions come out as 2 + (4 − 1) = 5, K1's Euclidean-TT rank (`C4_K1_referee.md:3,15`).
- Set C's 6 and 30, and O_h × T's 26, reproduce O1's counts (`C5_O1_report.md:92-93`; confirmed `C5_O1_referee.md:7`).

**On-shell reading of set C's degree 2 (checked).** The on-shell rank is 5:
- c_T (1);
- **three P,T-even TT anisotropies**;
- one P- and T-odd birefringence (the ωk term, which is absent under O_h × T).

The Einstein–Hilbert form vanishes on shell. Off shell the TT span is 7 (ω²: 2, ωk: 1, k²: 4). One anisotropic combination is ∝ (ω² − k²) and drops out on shell.

The two degree-1 TT structures are P-odd and T-even. They are helicity splittings linear in k: an isotropic one and a cubic one.

### 3.2 Ward-defect lemma (checked numerically; proved for the two forms found)

**Statement.** Under exact linearized-diffeomorphism invariance and O × time:
- no invariant degree-0 or degree-1 form is gauge-invariant;
- exactly 2 degree-2 forms are gauge-invariant, with on-shell TT rank 1.

**The two gauge-invariant forms (proved).** They are h_μν ε^{μαβγ}ε^{νρσδ}Y_{αρ}∂_β∂_σh_γδ with Y ∈ {η, u⊗u}. These are identically conserved and gauge-invariant by antisymmetry: Einstein–Hilbert and its time-rescaled copy, i.e. **c_T**. The numerical kernel has dimension 2, so there are no others.

**Consequence.** Every TT mass, every anisotropy, the birefringence and both one-derivative terms are **Ward-defect coefficients**. They exist only because the matter–graviton coupling fails the Ward identity. That is C3's boost obstruction, and R13-5 found the Ward-complete pair stress blocked. An exact N-type Ward identity would leave c_T as the graviton's only Lorentz-violating number.

*Scope.* This is linear order, up to two derivatives, with full linearized diffeomorphisms as the target. For foliation-preserving gauge only (Hořava-type), more forms are gauge-invariant; that is not computed.

**Full gauge-restoration codimension (checked; the K1 analog).**
- Set C: 6 + 8 + 28 = **42**.
- O_h × T: 6 + 0 + 24 = **30**.
- Z⁴: 11.

As with K1, this is an operator codimension, not a count of measured observables.

### 3.3 One-loop generation (checked witnesses; `r138_onshell_loop.py`, `r138_box_witness.py`, `r138_dirac_witness.py`)

**Method.**
- Paramagnetic one-loop TT self-energy for three laws, each with an O_h-covariant, Hermitian, local metric vertex:
  - NN scalar;
  - literal-box scalar (R7-1/R9-9 profile L, with R9-9's M vertex extended to q ≠ 0);
  - naive Dirac sea (8 tastes).
- The vertices are **not Ward-complete**, as in every packet witness (§3.2).
- The on-shell degree-2 TT matrix is extracted by Richardson differences along p = s(1, k̂) at 8 directions. It is fitted to the invariant on-shell basis and projected on c_T and the three anisotropies.

**Results.**

| Law | Fit residual (rel.) | c_T component | Anisotropy span over m ∈ {0.3, 0.6, 1, 2} (singular values) | Grid check |
|---|---|---|---|---|
| NN scalar | ≤ 6e-8 | +7.6e-3 … +3.5e-3 | **3 of 3**: 1.10e-2, 1.94e-4, 1.67e-5 | N = 36 vs 46: 1.670e-5 vs 1.663e-5 |
| Box scalar (L) | ≤ 2.4e-4 | +4.8e-2 … +2.9e-2 | **3 of 3**: 2.86e-2, 1.10e-2, 1.91e-4 | N = 56/72/88: 1.902/1.905/1.908e-4 |
| Dirac sea | ≤ 4e-7 | −9.8e-2 … +2.4e-2 (sign change between m = 1 and 2: an isolated zero) | **3 of 3**: 3.02e-2, 2.69e-2, 1.27e-3 | N = 20/28/36 stable |

**Readings of the table.**
- At every mass, every anisotropic component is nonzero. The smallest is 4e-4, against fit noise of 1e-8 to 1e-5.
- The TT masses (paramagnetic only, no seagull) span 2 of 2 in all three laws. This is **not** a mass claim, because the seagull is free (`C5_R9-9_referee_verdict.md:21`).
- The fit residuals confirm that the loops land exactly in the symmetry-counted span: the basis is complete, and no structure is missing.

### 3.4 The count

**One charged Dirac species + photon + N-type graviton, P,T-symmetric law (F2-type).**

| # | Coefficient | Generated at one loop? | Evidence | Tuning depth |
|---|---|---|---|---|
| 1 | c_e − c_γ | **yes** | NN: F2 −8.55e-3 (refereed). Box: R10-1 paired residual −10.66 to −17.96 e²/16π² (refereed) | 16.5 decades (photon decay at 1.4 PeV, 2.66e-19; KR κ̃_tr ~1e-19, fetched by R6-5) |
| 2 | c_T − c_γ | **yes** | c_T shift nonzero in all three witnesses (checked). QED δc_γ ≠ 0 at O(e²) (F2), while the graviton has no O(e²κ⁰) self-energy, so the two cannot cancel by symmetry (proved, elementary) | 12–13 decades (GW170817: −3e-15 to +7e-16; fetched by O1 referee) |
| 3–5 | three TT anisotropies | **yes, in the witness classes** | Span 3/3 for NN, box and Dirac (checked). Axial E_g ≠ T_2g on the box graviton (R9-9, refereed) | 13 (GW170817 direction, two-sided); 12.8–16.8 one-sided, from gravitational Cherenkov (Moore–Nelson 2001: c − c_g < 2e-15 galactic, 2e-19 extragalactic; web abstract) |
| 6 | μ_E | **yes** | V3: 1.97e-3 (refereed). Edge-carried on the box (R9-2, refereed) | ~98 decades (P0: 5.7e-99) |
| 7 | μ_T2 | **coupling-dependent** | 0 at one loop for V3's local coupling (Liouville, refereed). Nonzero E–T2 split with the minimal-metric seagull (R9-9, narrow). +1.61e-8 λ² at O(λ²) (RN L2) | ~98 decades if present |
| 8 | ρ + p (Lorentz-violating tadpole) | **yes** | R11-3: two independent conditions, w ≥ 0 (refereed) | ~123 decades (assumes \|1 + w\| ≲ 0.05–0.1, RECALLED) |
| (CC) | ρ | yes | R11-3 | ~122 decades; Lorentz-invariant, counted separately as in P0 and K1 |

**Totals for this law.**
- **8** Lorentz-violating coefficients plus the cosmological constant.
- **7** are shown generated at one loop, in witness classes.
- With V3's coupling the one-loop count is 7, and μ_T2 enters at O(λ²).

**Generic set-C law (proper O only): additions.**

| # | Coefficient | Status |
|---|---|---|
| 9 | b̃₀ | Generated across species at O(g²) once any handed term is present (R6-5 worker, unrefereed). 43–49 decades (KR b̃_T ~1e-26 to 1e-27 GeV, fetched by R6-5) |
| 10 | d₀₀ | Allowed (checked). **Not computed** at one loop. Bound not identified: the KR summary's d̃ combinations are ~1e-26 to 1e-27 GeV for the electron, and the d_TT admixture was not worked out |
| 11 | graviton birefringence (ωk, P- and T-odd) | Allowed (checked). **Not computed.** Needs P-odd and T-odd seeds |
| 12–13 | graviton degree-1 helicity terms (P-odd) | Allowed (checked). The isotropic one destabilizes long waves (R2, `R2_report.md:168`). The analog of R6-5's Lemma S suggests stability forces both to zero (suggested). The cubic one has the same small-k sign problem (suggested) |
| 14 | (k_AF)₀ | Protected: Lemma S plus Bloch/Watanabe (R6-5 worker) |

**Totals for a generic law.**
- **11** tunings plus the cosmological constant.
- **+2** graviton degree-1 terms, probably stability-protected (suggested).
- Outside the dim-4 count: the d = 5 CPT-odd photon term, about 10 decades (R6-5, suggested).

**Per extra species, and the scaling (reading; each item labelled).**
- **Each extra charged Dirac species:** +1 speed (P,T-even). It is mass-dependent: by R10-1's Lemma N(m) (refereed) a fixed shape cannot vanish on a mass interval. Isolated zeros are possible, as the Dirac witness's c_T shows.
- **With handedness:** +b̃₀ and +d₀₀ per species. The b̃₀ conditions are joint across species, because χ₅ mixes them (R6-5).
- **Each extra gauge field or charged scalar:** +1 speed.
- **The graviton block (c_T, 3 anisotropies, 2 masses, LV tadpole)** is shared and does not grow with N_s. That holds at one loop (checked symmetry), since every species feeds the same invariant structures.
- **Flavour mixing** makes c and d matrices: the SM gives 9 speeds, or 49 with flavour matrices (F2 referee).
- **The totals:**
  - P,T-symmetric laws: **N_tune = N_s + 7** (+ CC).
  - Generic: **3N_s + 8** (+ CC; + 2 stability-protected).
  - Here N_s counts fields with their own speed: charged Dirac species, gauge fields beyond the photon, and scalars.
- **Precision against N_s.**
  - Matter speeds: 13 to 19 decades each. Per-species bounds range from 1e-10 to 1e-21, and several directions have no separate bound (`C4_F2_referee.md:40-41`; `C5_O1_referee.md:38`).
  - Graviton block: 4 × (12–17) + 2 × 98 + 123 decades.
  - Handed laws: + N_s × 43–49 decades.

**Against "≥ 6" (`SUMMARY.md:435`).**
- The assembled 2 TT + 1 QED + 3 graviton speeds is replaced by 2 TT + 1 QED + 4 graviton speed (1 match + 3 anisotropies) + 1 LV tadpole = 8.
- R2's "2 isotropy" was a local codimension inside its S/S-tl coefficient set (`R2_report.md:126-131`). The general Ward-defect set has 3 on-shell anisotropies (checked).
- The "≥ 6" survives as a lower bound (reading). Its decomposition was incomplete.

---

## 4. Against the FIXED readings (`TESTS.md:4757-4758`)

**COUNTED requires** an explicit count, with each coefficient shown generated (nonzero) at one loop and independent, checked.

**Met.**
- An explicit count with independence (checked):
  - the symmetry count;
  - the on-shell ranks;
  - the K1 validation.
- One-loop generation, in witness classes, for coefficients 1–6 and 8:
  - 1, 6 and 8 refereed;
  - 2–5 checked here, for three laws including box and Dirac.

**Not met.**
- **μ_T2:** zero at one loop under V3's local coupling (refereed). So "8" is coupling-dependent at one loop.
- **The P- and T-odd sector:** d₀₀, the graviton birefringence and the degree-1 terms are not shown generated. b̃₀'s generation is an unrefereed worker result.
- **The graviton witnesses** use vertices that are not Ward-complete, and they are not V3's coupling. By §3.2 every anisotropy is a Ward defect, so its size depends on the (blocked, R13-5) completion. No single law is shown to generate all of 1–8 together.

**Reading: OPEN.**

The strongest supported statement (checked or refereed):
- For P,T-symmetric set-C laws, the dimension ≤ 4 Lorentz-violating space at one loop is 8 (+CC). Seven of the eight are shown nonzero at one loop in witness classes.
- For generic proper-O laws it is 11 (+CC), plus 2 terms probably fixed by stability.
- Scaling: N_s + 7 and 3N_s + 8.

---

## 5. Strong words checked

- **"only Lorentz-violating graviton number"** under exact Ward identities: at linear order, ≤ 2 derivatives, full linearized diffeomorphisms (§3.2).
- **"three anisotropies"**: first-order on-shell TT count. Second-order TT–longitudinal effects are not counted.
- **"shared, does not grow"**: at one loop and dim ≤ 4. Each species changes the value, not the number.
- **"protected"** for the degree-1 graviton terms: suggested only.
- **"exactly"**: used only for the K1 validation and the gauge-invariant kernel (numerical rank, with gaps of more than 1e-8).

---

## 6. What would change this

**What would make it COUNTED:**
- a single law in the class (QED plus the N-type graviton, with a stated pair-stress completion) in which c_T, the 3 anisotropies, μ_E and μ_T2 are computed together;
- a P-odd and T-odd seed showing d₀₀ and the birefringence generated;
- a referee on b̃₀.

**What would lower the count:**
- a Ward-complete coupling (not just R9-9's number-conserving one) would remove items 3–7 (§3.2);
- the open question is whether one exists (R13-5 W2).

**Requests for the referee:**
- check the gauge-invariant kernel (2 forms) and the on-shell rank 5;
- check the Richardson extraction;
- check whether the cubic degree-1 term is stability-protected.

---

## 7. Files

**Scripts (`S/scripts/`):**
- `r138_forms.py/.out`: tensor invariants, graviton forms, gauge codimension, TT ranks, tadpoles (with the K1 validation).
- `r138_onshell_loop.py/.out` and `_conv`: on-shell ranks; the NN scalar witness.
- `r138_box_witness.py`, with `_N40`, `_N56` and `_conv.out`: the box scalar witness.
- `r138_dirac_witness.py`, with `_N20` and `_conv.out`: the Dirac sea witness.
- `r138_precision.py/.out`: tuning-depth arithmetic.

**Downloads:** none new. The KR tables text was read from `C5/R6-5/downloads_kr/` (untrusted data, not executed).

**Web (fetched this session):**
- [GWTC-3 tests of GR](https://arxiv.org/abs/2112.06861): m_g ≤ 1.27e-23 eV (arXiv) or 2.42e-23 eV (published PRD version, per search result). Either way that is (m/M_Pl)² ~ 1e-102, consistent with P0.
- Moore–Nelson, [hep-ph/0106220](https://arxiv.org/abs/hep-ph/0106220): c − c_g < 2e-15 (galactic) or 2e-19 (extragalactic).
- Kostelecký–Tasson, [1508.07007](https://arxiv.org/abs/1508.07007): gravitational Cherenkov limits on the graviton-sector SME (abstract only).
