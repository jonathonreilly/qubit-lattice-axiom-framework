# Assumed-inputs model (option 1, 2026-10-26)

The owner's option 1: take the audit's 12-rule base, add the fewest clearly labelled ASSUMED inputs that reach the
Standard Model at low energy, then ask what the combination predicts that the SM does not. Runner: runner.py
(TOTAL: PASS=10 FAIL=0, 0.4 s, 79 MB). Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers,
[S] reading or speculation. Axioms unchanged. No CL edit.

## 1. The model

**Base (r4 working set, unchanged):** tick, one copy, chirality (overlap + Luscher, slab tick form), links, edges,
lapse/shift stationarity, one cone, total phase, split, half-filled vacuum, actuality, and content (one 16 per
family; Yukawa-type, uddn and (nu^c)^4 terms; a doublet register). Rule 12 is already a supplied input.

**Assumed inputs:**

- **A1. Far-wall mirror gapping.** The far wall's 3 x 16 mirror is gapped symmetrically by the fewest-change
  charge-4 term, Cayley-completed (Re Omega + (1/2) omega^omega). The 1/2 weight is forced by the largest stabiliser
  (cayley-mirror-gap), and the coupling is assumed strong (g >~ 0.25 in proxy units).
  - ASSUMED: that it gaps in 3+1D.
  - Support: 1+1D SMG (Fidkowski-Kitaev, You-BenTov-Xu) and 3+1D on-site SMG (Ayyar-Chandrasekharan). Against:
    nothing published gaps a mirror alone; the far-end theorems and qmc-face-gapped pair order.
  - Cost: about 1 bit, plus one unproven dynamical assumption.
- **A2. Far-termination winding.** The slab's far layer carries a family-class turn winding; the bulk keeps W = 0.
  - This costs about 3 boundary bits (W != 0, the end, the mirror charge; far-termination-winding G3).
  - The far-wall Z3 anomaly vanishes only for N_f = 0 mod 3, so A1 can act only on all families together.
  - **N_f = 3** is the smallest allowed value, consistent with N_nu = 2.984 +- 0.008 (log2 of the choice is about
    1.6 bits).
- **A3. Higgs doublet and Yukawas (supplied).** A doublet register with mu^2 and lambda. Yukawa matrices for u, d and e,
  plus Dirac nu Yukawas (Dirac is forced by the Z4 of B - L).
- **A4. Strong CP: the axion** (KSVZ-type, PQ phase = the phase of the far-wall vertex). Why not the other two:
  - *Parity (P_slab, the Barr-Chang-Senjanovic / Babu-Mohapatra shape)* fails once the mirror is SMG-gapped (A1).
    The SMG vertex phase enters theta-bar one-for-one, and P_slab never maps it onto Y, so theta-bar is generically
    O(1) (face-swap D3).
  - *Nelson-Barr* (copy-sign-nelson-barr) fails in three ways:
    - the unique 16 x 16bar singlet fills both slots (G = F^T) unless a vacuum direction is CHOSEN;
    - the loop quality needs lam <~ 6e-8 (a ~24-bit tune);
    - the SMG vertex phase is again uncontrolled.
  - *The axion* removes theta-bar whatever its source, including the vertex phase. It costs one scale f_a and a
    quality assumption: PQ must hold to about 1e-10 against cell-scale operators. On the lattice this needs an exact
    Z_N of an angle-grid register with N >~ 10, about 3-4 bits.
  - Bonus: it is the only dark-matter candidate on offer (predictions-sheet K6: no rule-made species qualifies).
  - Variant B (parity, mirror Higgsed at v' in [1e8, 1e11] GeV; mirror-quark-portal) replaces A1 + A4 and is kept
    for comparison. Not chosen: the Luscher projector breaks P_slab explicitly, and its share set is picked to work.
- **A5 (flagged; not needed for low-energy SM).** A primordial scalar seed. The rules give n_s = 1 and no A_s
  (predictions-sheet K7/K8). Without a supplied inflaton the model FAILS the CMB.

## 2. Bits of supplied information

| Sector | SM (+ Dirac nu) | This model |
|---|---|---|
| Gauge couplings | 3 | 3 (rishon size per factor; equal at the cell fails with SM running) |
| Higgs | 2 | 2 (A3) |
| Charged-fermion masses + CKM | 9 + 4 | 9 + 4 (A3; every family mechanism tried fails) |
| theta_QCD | 1 | 0, traded for f_a (A4) |
| Neutrinos (Dirac) | 3 + 4 | 3 + 4 (Majorana phases forbidden, so 2 fewer than SM + Weinberg) |
| **Continuous, particle physics** | **26** | **26** |
| G, Lambda | 2 (GR + LCDM) | 2 (G sets the cell; Lambda per 4-volume) |
| Rule constants visible at low energy | 0 | the floor 1/8 (fitted to J0740), mu_s and kappa_shift (fitted to "no bounce"); eps0 and M are invisible (shown below) |
| Discrete choices | gauge group, reps, N_f (~10-20 bits) | content 16 + handedness (~5), A1 (~1), A2 (~3 + 1.6), PQ Z_N (~3-4), lattice orientation (3 angles, measurable) |

**Verdict.** The model supplies as many continuous numbers as the SM plus Dirac neutrinos (26). On top of those it
supplies about 3 fitted gravity-window constants and about 12-14 discrete bits. The rules buy structure (3+1D, spin 1/2, one cone, link gauge registers, gravity with gamma = beta = 1 and
G_T = G_N), theta_gauge in {0, pi}, the Z4 of B - L, w = -1 to 1e-18 and the fixed dim-6 coefficients below; not
any reduction of the SM's free numbers.

## 3. The one sharply fixed new number: dimension-six Lorentz violation [T/F]

- **A1/A2 [F] (runner A1, A2).** The copy mass shifts the light fermion band from the link band by
  c6(n) = -(1/8)(sum n_i^4 - 1/3).
  - In units of K per cube, this is -1/12 on the axes, -1/48 on the face diagonals and 0 on the body diagonals.
  - It is the same to 5e-7 for every (eps, M) tested: eps 0.005-0.3, M 0.002-0.5. The register had the number "at one
    point only".
  - So it does not depend on the supplied step or copy mass.
- **B [F] (runner B).** The link band itself (photon, gluon, and every fermion before the copy term) has
  c_g(n) = -(sum n_i^4)/24 at small eps.
- **Scale.** E* = hbar c/(2L) = 1.22e18 GeV, with L = sqrt(8 pi) l_P from G (unit map). The split window lets the
  cell vary by up to 2, so energies scale by up to 2^(1/2).
- **In Planck-unit notation** (E^2 = p^2 + m^2 - eta p^4/M_P^2):
  - photons and gluons: eta_gamma = 2.8-8.4;
  - quarks and leptons: eta_f = 2.8 (body diagonal) to 25 (axes).
  - All are **subluminal**, so there is no vacuum Cherenkov radiation.
  - The coefficients are flavour-universal, so neutrino-oscillation LV tests (IceCube flavour ratios) see nothing.
    Flavour dependence enters only through mass terms of order (m/E*)^2 [E].

**Correction to the register's photon-decay number [F] (runner C1).** The register threshold (8/|c6|)^(1/4)
sqrt(m_e E*) leaves out the photon's own term.

- With it included, symmetric splits are closed on every ray, since |c6| < 3|c_g| everywhere.
- Decay proceeds through asymmetric splits, x = b/(6(a + b)), about 0.11, at k_th = (6(a + b)/b^2)^(1/4) sqrt(m_e E*).
- This gives **80 PeV on the axes** (register: 78), **122 PeV on the face diagonals** (register: 110), and never on
  the body diagonals.
- Above k_th the photon lifetime is microscopic, so the sky closes:

| Photon energy | Sky fraction still open |
|---|---|
| 0.1 EeV | 65% |
| 0.2 EeV | 7% |
| 1 EeV | 0.2% |
| 10 EeV | 0.002% |

  The open sky is eight spots around the body diagonals, shrinking as E^-2 [F, runner C2].

**New consequence: proton photopion (GZK) is closed [F/E] (runner D).**

- Kinematics with a subluminal proton term show that p + gamma_CMB -> p + pi is forbidden at EVERY energy once
  eta_p >~ 1e-4. Even photons at 10 kT of the CMB were included.
- The rule estimate is eta_p = sum over partons of <x^3> eta_parton, about 0.05 x (3-25), i.e. 0.1-1 [E; the parton
  fractions are supplied].
- That is 3-4 orders of magnitude above closure.
- Nuclei are suppressed by 1/A^2 and by the nucleon's 1/A momentum share, so photodisintegration (Fe) stays largely
  open [S].
- Predicted:
  - no GZK attenuation of protons;
  - the observed suppression near 4e19 eV must be a source/rigidity cutoff or nuclear;
  - no proton-photopion cosmogenic EeV neutrinos.
- This does not look excluded, since Auger's mixed-composition fits favour a source cutoff. But it must be checked
  against the published UHECR LIV analyses (Auger 2022 LIV paper) before anyone leans on it. If proton-dominated
  GZK were established, the rules as written would be falsified.

## 4. Predictions table

Rank = fixedness (F: fixed by rules; C: conditional on supplied content/history; S: speculative) x testability within
about 10 years.

| # | Prediction | Number / sign | Fixed? | Current status | Test, when | Rank |
|---|---|---|---|---|---|---|
| 1 | Dark energy exactly constant | \|w + 1\| < 1e-18; split ripple ~1e-121 | F (shared with LCDM) | DESI DR2 prefers evolving DE at 2.8-4.2 sigma | DESI final, Euclid, Rubin (2026-30) | high, but not new vs LCDM |
| 2 | Dirac neutrinos: zero 0nubb, no n-nbar, no Majorana phases | m_bb = 0 exactly | C (Z4 of B - L from supplied content terms; Z4-keeping vacuum) | KamLAND-Zen T1/2 > 3.8e26 yr | LEGEND-1000, nEXO to m_bb ~ 10-20 meV (~2032-35); decisive if JUNO/DUNE find inverted ordering | **high** |
| 3 | Extra radiation from three nu^c | Delta N_eff = 0.141 with a Planck-hot start; ~0 if the start is cooler (no rule picks) | C (history) | Planck 2.99 +- 0.17 (+1.1 sigma); ACT DR6 P-ACT-LB 2.86 +- 0.13 puts the prediction 2.5 sigma high | Simons Obs. (2.8 sigma, ~2028), CMB-S4 (4.7 sigma) | **high-medium** |
| 4 | UHE photon decay, cubic sky | threshold 80 PeV (axis) to 122 PeV (face); none on body diagonals; 0.2% sky open at 1 EeV | **F** (c6 independent of eps, M; E* from G; orientation 3 measurable angles) | No UHE photon seen (Auger limits above 0.2 EeV; LHAASO to ~1.4 PeV) | Auger/AugerPrime, TA, GRAND photon searches: two EeV photons not related by a cubic turn falsify | **medium** (fixed, but needs a detection) |
| 5 | No proton GZK photopion | closed for eta_p >~ 1e-4; rules give 0.1-1 | F coefficients, E parton weighting | not obviously excluded (mixed composition) | AugerPrime composition at >4e19 eV, TAx4 proton anisotropy, IceCube-Gen2/GRAND/RNO-G cosmogenic nu | **medium** (cheapest check: existing data) |
| 6 | Axion dark matter | m_a free; native far-wall-vertex reading N_DW = N_f = 3, f_a ~ (0.01-1)E*/3, so m_a ~ 1e-11 to 1e-9 eV | S | BH superradiance probes 1e-13 to 2e-11 eV (top of range at risk) | CASPEr, DMRadio-m3; superradiance spins | low-medium |
| 7 | Gravity-mediated entanglement | 0.79 rad, concurrence 0.156 (1e-14 kg, 200 um, 2.5 s); no Schrodinger-Newton term | F (shared with perturbative QG) | untested | BMV-type experiments (>10 yr) | medium, not new vs QG |
| 8 | Nucleon decay only Delta B = Delta L | tau ~ 1e46 yr | C | > 2.4e34 yr | Hyper-K/DUNE see nothing | low (null, like the SM) |
| 9 | No W_R; Born exact every half-tick (no collapse noise); EP eta < 2e-33; no B - L force; GW dispersion only at E*; exterior BH = GR to (l/M)^2 | nulls | F/C | all consistent | none distinguishes from SM/QM/GR | low/untestable |
| 10 | Tensor seed n_t = 0 + log-periodic ripple; n_s = 1, no A_s | P_t ~ 5e-122 | F | **n_s FAILS without A5** | — | — |
| B | Variant B mirror ladder | m_f' = m_f v'/v: at v' = 1.7e8 GeV, u' 1.5 TeV, d' 3.2 TeV, e' 0.35 TeV, nu' ~35 keV; Delta N_eff >= 0.14-0.64 | C (v' supplied) | LHC vector-like quark bounds set v' >= 1.7e8 GeV | HL-LHC to v' ~ 2e8, FCC-hh to ~1.5e9 | medium (if B is chosen) |

## 5. Plain answer

The only predictions FIXED by the lattice rules and new relative to the SM are the dimension-six Lorentz-violation
coefficients. They are Planck-suppressed (invisible at colliders, GRB timing, clocks) but enhanced as E^4/E*^2 in
ultra-high-energy cosmic rays: photon decay above 80-122 PeV with a cubic sky, and closed proton photopion (check
existing UHECR data first). The accessible new predictions are conditional: Dirac neutrinos with zero 0nubb, and
Delta N_eff = 0.14. w = -1 is the nearest falsifier but is shared with LCDM. With A1 + axion the mirror leaves no
collider signal; only variant B puts mirror states in reach.

## 6. Smuggling review

- **Supplied:** A1's 3+1D gapping and coupling; A2's boundary bits and N_f = 3; all A3 numbers; f_a and the PQ Z_N;
  the content (16, handedness, Z4 terms); thermal history; parton fractions; literature bounds; the unit map's naming
  of the cell rung.
- **Forced:** c6's value, angular form and eps/M independence [F]; the link band's dim-6 term [F]; exact photon-decay
  and photopion kinematics [F]; the Z4 selection rules and theta_gauge in {0, pi} (cited).
- **Gate:** no rule proposed; every input is labelled ASSUMED, not adopted.
