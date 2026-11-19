# minimal-toe-merged: A + B + info-min-law, after the B hostile test (2026-10-22)

Zero premise weight; axioms and register untouched. `runner.py`: 24 PASS / 0 FAIL, 1 s, 72 MB (`out.txt`). Inputs: A = `minimal-toe`, B = `minimal-toe-b`,
H = `minimal-toe-b-tests` (hostile test, all three checks negative), L = `info-min-law`.
Cited, not rederived: Jacobson, Gleason, Z16, Cominetti–San Martín, staggered spin-taste basis.

## 1. Does B's 2+3 split serve as A's breaking rule?

**Embedding (theorem, runner S1–S6, W1–W2).**
- Lambda(C^5) built on 5 modes is the Spin(10) Dirac spinor: the 45 Majorana bilinears span so(10).
- The stabiliser of the occupation number N inside so(10) is u(5), of dimension 25. Adding the level/link
  number N_L gives u(2)+u(3), of dimension 13.
- Y = -1/3 N_L + 1/2 N_Q lies in so(10). This is the standard Georgi–Glashow SU(5) inside Spin(10).
- The extra U(1) is X = N - 5/2.
  - The twist -5/2 is forced: X is in so(10) and the untwisted N is not.
  - Untwisted N is anomalous (Tr N = 40, Tr N^3 = 400 on the 16).
  - X has charges (-5, -1, 3) on (1, 10, 5b). This is U(1)_chi.
  - All X anomalies vanish, including the mixed ones with Y, SU(3), SU(2) and gravity.
  - exp(i pi X/2) = -i on the whole 16. So A's protecting Z4 sits inside U(1)_chi, and a nu^c nu^c condensate
    (X = -10) breaks Z4 to Z2.
- Hypercharge normalisation is standard. On the 16, Tr T3^2 = Tr T_colour^2 = (3/5) Tr Y^2 = 2, which gives
  **sin^2 theta_W = 3/8 at the breaking scale**, with alpha_3 = alpha_2.

**But the split is not derived.**
- H showed that minimum information picks the unsplit C^5 (or Spin(10) itself). C^2 (+) C^3 wins only after
  supplied conditioning.
- The runner (S6) shows exactly what the split is. A generic **45-adjoint orientation aX + bY** has
  stabiliser u(3)+u(2). So "2+3" is a **vacuum choice of Spin(10)** that restates the target subgroup. It is
  not a rule from sites.
- Verdict: the split *is* the right shape for A's missing breaking rule, and the embedding and the 3/8 are
  correct. As a rule, however, it fails gate item (2), because it inserts the observed subgroup through the
  mode choice.
- What remains is a well-posed dynamical question: does any channel of the rules' own dynamics orient a 45
  along aX + bY?
  - A's 16x16: the 10 is most attractive, giving Spin(9) (wrong way).
  - New (C1): for 16x16bar, Delta C is 45/4 (singlet), 13/4 (45) and -3/4 (210). The 45 is attractive, but
    the singlet, which gaps the 16 together with its mirror, is stronger. That is a chirality hazard.
- **Row 12 stays P (partial).**

**Consequence for B's other claims.**
- With Spin(10) as the frame group, B's "no gauge proton decay" is withdrawn. X and Y bosons exist.
- SM-only one-loop running (measured M_Z couplings, comparison only, W3): alpha_1 = alpha_2 at 1.0e13 GeV,
  1/alpha_3 off by 5.6; that scale is below the proton bound (M_X >~ 10^15.5 GeV).
- So the merged ruleset **requires thresholds** (mirror, taste, U(1)_chi states): a falsifiable tension.

## 2. Families: one, three, or the taste count?

**B's record-axis rule fails (theorem, F1–F3).** It fails three precise counts:
- (i) Holevo. The three Bloch axes are the 3 mutually unbiased bases of ONE qubit. Three readings of one
  register carry at most 1 bit in total, so they are not three registers. The three axis-sector pattern
  spaces span 32 states, not 96.
- (ii) Gauge. The axis change is an SU(2) frame element that commutes with N and N_L, so a family label tied
  to it is frame-dependent and unobservable.
- (iii) Double use. Lambda^1 and Lambda^2 of C^3 (the 3 and 3b) already spend the axis triplet on colour.

**A is right about what is forced:** P0 with A's rules forces N_f = 1. Adding copies satisfies no additional
constraint. "One per axis" is an optional, supplied rule, so B's 3 is not a prediction.

**Taste route (new, finite diagnostic T0–T4).**
- H found spin on the 2^3 cell x qubit: 16 = 2 spin x 4 taste x 2 qubit. That leaves an 8-fold flavour
  space per spin doublet.
- Under the binary octahedral lattice group (order 48), with spin and taste locked as in the staggered
  basis:
  - Qubit not locked: flavour 8 = 4 copies of the spinor doublet. No singlet or triplet can appear, so every
    cubic-symmetric reduction gives 2 + 2. **3 is impossible.**
  - Qubit Bloch axes locked to lattice axes (L's "space rotations = qubit rotations" bridge, already needed
    for d = 3): flavour 8 = 2 x (1 + 3). The triplet is the vector of the d = 3 rotation group, so **3 = d**
    appears with no number chosen.
- The invariant sigma_taste . sigma_qubit has eigenvalues -3 (singlet) and +1 (triplet).
  - A cubic-invariant taste mass m0 + m(sigma.sigma) leaves the triplet massless only if m0 = -m. That is
    tuned, so it fails R4's "absent unless protected".
  - **Missing:** a symmetry that protects the triplet and gaps both the singlet and the centre doubling.
  - Candidate: the swap (1 + sigma.sigma)/2 (+1 triplet, -1 singlet).
- Verdict: one bridge (the lock) gives both d = 3 and a (1 + 3) family structure. Three families are
  **natural but not derived; row 15 M -> P.**
- Prediction if this route holds:
  a degenerate family triplet at leading order (hierarchy needs lock breaking) plus a heavy singlet taste.

## 3. Merged ruleset (6 rules, verbatim)

**M0 (Least information).** The world is the shortest description satisfying M1–M5. No bit is stored that
the rest fixes, and every detail the constraints leave open has maximal entropy. The only selectors are
"smallest", "largest" and "absent".

**M1 (Unit, grid, cell).**
- Possibilities live in qubits, reached by one reversible update that is the same everywhere and acts only
  on neighbours.
- The qubit's rotations are the rotations of space, so the grid has one commuting generator per Bloch axis.
  This gives Z^3 with 6 neighbours, and Z^3 with a tick is the slicing of a 4D hypercubic description in
  which time is not privileged.
- Spin is the Clifford structure of the 2^3 cell.

**M2 (Actuality = least surprise).**
- A fact is actual only when recorded. A record is a permanent, exclusive copy, and exactly one record
  history is actual.
- Each half-tick, the history minimises relative entropy to the change-penalised reference process, in the
  zero-noise limit, with the odds held as marginals: fewest changes first, then least before/after mutual
  information.

**M3 (Relations only).** Internal labels, positions and the time direction may be relabelled independently
at every place without changing anything. Neighbours are compared by a connection on every link. The
relabelling group is as large as M4 permits.

**M4 (Consistency and protection).**
- The description stays local under every background relabelling: no perturbative or global anomaly.
- A light degree of freedom whose lightness no symmetry or anomaly forces is absent, gapped at the cell
  scale.
- The content is the smallest that a relabelling symmetry can protect from every mass.

**M5 (Spread).**
- In small regions, vacuum entanglement is maximal at fixed volume.
- The vacuum term is the integration constant conjugate to 4-volume.

Removed:
- B's R4 split (supplied; H).
- B's R5c record-axis families (fails F1–F3).
- B's Sorkin record-noise Lambda. L shows it conflicts with the exact record counts (Fano 0), and it fails
  BBN/CMB unless its coefficient is tuned.
- A's R2–R4 survive as M3–M4; B's R1/R2 survive inside M1 as the lock bridge (L).
- L's least-surprise principle is M2, which merges A's R3, B's R3 and the CL-2 transport into one objective.
  Born |a|^2 is the only weighting with a finite-information transport (L).

## 4. Scorecard (24 rows as in A)

Key: D derived · P plausible (missing step named) · M missing · S supplied (counts as failure) · Prim
primitive. "B corr." is B after H and L.

| # | Physics | A | B corr. | **Merged** | Merged note |
|---|---|---|---|---|---|
| 1 | Quantum mechanics | Prim | Prim | **Prim** | Reconstruction inserts continuity and tomography (L) |
| 2 | Born | D | P | **D** | M2: unique finite-information weighting, plus Gleason |
| 3 | Unitarity, locality | Prim | Prim | **Prim** | |
| 4 | Records, complementarity | D | D | **D** | |
| 5 | One light cone | D(c) | P | **D(c)** | 4D hypercubic reading (A, D2) |
| 6 | 3+1 dimensions | P | P | **P** | d = 3 from the lock bridge (inserted) |
| 7 | GR | P | P | **P** | Jacobson; small-ball modular Hamiltonian missing |
| 8 | Equivalence principle | D | P | **D** | |
| 9 | GW speed, 2 polarisations | D(c) | P | **D(c)** | |
| 10 | G | P | P | **P** | G = 1/(4 eta); eta not computed |
| 11 | Why gauge fields | D | D | **D** | |
| 12 | Which group | P | S | **P** | Spin(10) selected. The SM x U(1)_chi = 45 orientation aX + bY is exact, but its selection is open |
| 13 | Content and charges | D | D | **D** | 16 with nu^c; standard Y; 3/8 at breaking |
| 14 | Chirality realised | P | P | **P** | Mirror SMG unproved; the 16x16bar singlet is the most attractive channel (hazard) |
| 15 | Three families | M | M | **P** | The lock gives (1 + 3) taste multiplets. Triplet protection is missing |
| 16 | Hierarchy, mixing | M | P | **M** | Triplet degenerate at leading order |
| 17 | Higgs, weak scale | M | M | **M** | R4 tension |
| 18 | Neutrino masses | P | P | **P** | Z4 ⊂ U(1)_chi forbids Majorana until broken, which gives a seesaw |
| 19 | Strong CP | M | M | **M** | |
| 20 | Vacuum energy not gravitating | D | D | **D** | |
| 21 | Size of Lambda | M | M | **M** | Sorkin estimate dropped |
| 22 | Inflation | M | M | **M** | |
| 23 | Dark matter | M | M | **M** | Gapped mirror or singlet taste (speculation) |
| 24 | Arrow | D | D | **D** | |

| | D | P | M | S | Prim |
|---|---|---|---|---|---|
| A | 9 | 6 | 7 | 0 | 2 |
| B self-scored | 8 | 11 | 4 | 0 | 1 |
| B corrected | 5 | 10 | 6 | 1 | 2 |
| **Merged** | **9** | **7** | **6** | **0** | **2** |
| Register | 5 | 3 | 6 | 8 | 2 |

**Summary.**
- Merged beats corrected B clearly and A modestly (rows 2, 15); 6 rules replace A's 5 + B's 5 + CL-2.
- It does **not** derive the low-energy group or N_f = 3.
- What is new and tested:
  - The exact embedding: forced spinor twist, U(1)_chi containing the Z4, and 3/8.
  - The two-route family no-go: the record axes fail, and the taste route without the lock fails.
  - The (1 + 3) taste structure under the lock.

## 5. Gate (merged)

1. **No number chosen.** Pass. The M_Z couplings are comparison only.
2. **No observed structure named.** Pass for M0–M5. The 2+3 split was removed for failing this item. The
   lock bridge names no group, but it is an inserted identification, borderline, the same one L flags.
3. **Predictions it was not built for:**
   - nu^c
   - a Z4 that forbids Majorana mass until U(1)_chi-type breaking
   - sin^2 theta_W = 3/8 together with gauge proton decay, which with SM-only running is in **tension** and
     requires thresholds
   - families as a (1 + 3) cubic multiplet, with a heavy singlet taste
   - Lorentz violation starting at dimension 6
   - w = -1
4. **Axioms bent:**
   - Lattice: re-read as the slicing of a 4D hypercubic description.
   - Qubit: locked to space rotations, with 16 internal Weyl modes per site.
   - Admissibility: group-valued links.
   - Record: kept, with actuality given by least surprise.

## 6. Three most decisive next calculations

1. **Vacuum orientation (row 12, and 14).** In the 16 + mirror sector with the cell structure, compare the
   free energy of the 45 orientation aX + bY, the 10 orientation (Spin(9)), and the singlet 16·16bar gap.
   If aX + bY wins, the observed group is derived; if the singlet wins, chirality is lost.
2. **Triplet protection (row 15).** Build the locked cell x qubit staggered hop. List every mass operator
   that is cubic- and Z4-invariant, and test whether a swap-type symmetry forbids triplet masses while
   allowing singlet and centre-partner masses with no tuning.
   Yes: N_f = 3 = d derived. No: row 15 returns to M.
3. **Thresholds and proton (rows 13 and 10).** Run one-loop with the merged ruleset's own intermediate
   states (mirror, singlet taste, U(1)_chi). Find whether the three couplings meet above about 10^15.5 GeV,
   and compute induced 1/g^2 against G = 1/(4 eta) for l_P/a.
