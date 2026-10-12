# Decision matrix for candidate laws (2026-10-08, v2 after the four sweeps)

**Status: planning.** These are test settings, not adopted axioms, and nothing here enters `docs/MINIMAL_AXIOMS_2026-06-29.md`. A setting becomes an axiom question only if a candidate survives the kill sheet and the owner then chooses to adopt it.

**Owner instruction (2026-10-08).**
- Go with the supervisor's recommendation for the first decisions.
- Record forks only as settings to test.
- Build the matrix of possible decisions, ranked by probability of TOE, so that we can iterate through it.

**What the numbers are.** Every factor is a supervisor prior: a judgement, with its reason given below. None is computed. The ranking is the useful output; the products are not probabilities of anything measurable. To change a number, edit `decision_matrix.py` and run:
- `python3 decision_matrix.py --top 20 --sensitivity`
- `python3 decision_matrix.py --physics-only` (drops axiom fit)

**v1 → v2.** v1 was written before the repo sweeps. v2 applies four read-only sweeps of main, `ai/probes` campaign 8 and the preserved campaign branches (light, matter, gravity, records/dynamics; Sonnet 5.5, same-family). Their findings are the reasons quoted below.

## The five forks (192 combinations)

| Fork | Options |
|---|---|
| **motion** | **H**: continuous-time local Hamiltonian, with time not a lattice direction. **Q**: hypercubic tick, with time a lattice direction of the same step as space. |
| **turns** | **L**: turns act up to a site-local U(1) frame. This is main's kinetic-class reading; it keeps all 24 turns, and translations become projective. **E**: every site's possibilities turn rigidly with the grid (owner Q3, 10-04). |
| **room** | **P**: one qubit per site, with jobs set by a pattern. **M**: more room per site (several qubits, or primitive fermion modes). **U**: one qubit per site, uniform. **O**: continuous variables per site plus fermion modes, i.e. ordinary lattice fields. |
| **records** | **B**: Bell-type beables (fermion occupations). **F**: collapse flashes (GRW/CSL). **D**: decoherence-defined records. |
| **gravity** | **G**: emergent helicity-2 mode. **X**: explicit linear spin-2 field. **I**: induced or entanglement gravity. **R**: record-carried gravity. |

## Priors and reasons (v2)

**K1 light: a 3D photon.**

| Room | Prior | Reason |
|---|---|---|
| P | 0.45 | The repo's pure spin-half ring leans quadratic up to 12³. A linear term appears only near the Rokhsar–Kivelson point, and its controls failed. Literature Coulomb phases (Hermele–Fisher–Balents; the cubic dimer model) are not tested on main. |
| M | 0.50 | |
| U | 0.10 | A uniform rule over a calm vacuum gives heavy ripples only. |
| O | 0.85 | Compact U(1) in 4D has a proven massless phase at weak coupling (Fröhlich–Spencer 1982), and Yee Maxwell is unique in its class. |

Modifiers:
- Q × 0.85.
- U + E × 0.7.
- Q + E + U = 0 (A42).

**K2 matter: one-handed fermions with Standard Model gauge structure.**

| Room | L | E |
|---|---|---|
| P | 0.06 | 0.05 |
| M | 0.15 | 0.08 |
| U | 0.03 | 0.02 |
| O | 0.18 | 0.10 |

Reasons:
- Fermions are assumed on main, not derived from qubits. JW strings are non-local, statistics are not forced, and a local χ is impossible for d ≥ 2 (A54).
- A52's corner records give fermions under exact turns.
- Non-abelian links need 2 or 3 qubits per link (PROVED).
- Chirality: every repo route keeps a mirror partner. Symmetric mass generation (Wang–Wen) is named only as prior art.
- Q × 1.1.

**K3 gravity: Newton, light bending ×2, equivalence to 1e-15, c_g = c.**

| Gravity | P | M | U | O |
|---|---|---|---|---|
| G | 0.03 | 0.03 | 0.02 | 0.05 |
| X | 0.02 | 0.02 | 0.01 | 0.06 |
| I | 0.02 | 0.02 | 0.02 | 0.02 |
| R | 0.01 | 0.01 | 0.01 | 0.01 |

Reasons:
- Finite slots give no partner-free light-speed graviton at the harmonic level (probes 10, 20, 21; main's oscillator-slots note).
- The only working construction is A25, with continuous variables.
- A fixed grid lets the interacting sea induce Planck-size mass-type terms (probe 6).
- Jacobson entanglement gravity is dead on the grid: the coefficient varies 16–18% with cut direction.
- Record-carried gravity falls short (campaign 8).
- E × 0.8.

**K4 quantum rules.**
- **B 0.90.** Equivariance holds, and CHSH 2.81 vs 2.79 is reached on 1D rings.
- **F 0.85.**
- **D 0.85.**

**K5 record-sector data.**
- **B 0.95, D 0.95.**
- **F 0.10.** The mass-proportional CSL window at r_C = 1e-7 m is 1e-16 ≲ λ ≲ 5e-15 s⁻¹ (Majorana, PRL 129 080401). A site-local hit heats the vacuum at the bond scale: 4 bond energies per unit rate on a 2×2×2 cube (CHECKED this session). "Mass" is not defined in the axioms.

**K6 numbers.**
- **L: 0.04** for P, M and O; 0.02 for U.
- **E: 0.02**, and 0.01 for U.
- Reason: the hw=1 triplet is a label algebra, not a symmetry (e69519ec7a), and the Koide, 5/6 and dark-matter matches failed.

**K7 one cone: photon, matter and graviton share one speed** (GW170817 ~1e-15).
- **H 0.10.** Interactions split speeds at second order: v_ψ − v_φ ≈ 0.026 g².
- **Q 0.15.** Hypercubic symmetry forbids a dimension-4 split, but only if every sector, gravity included, is hypercubic.

**K0 fit to the four axioms.**
- **turns:** L 0.95 (main already uses it), E 1.
- **room:**
  - P 0.6: one qubit cannot hold its own job label, so the pattern sits in the law, against "No site is privileged".
  - M 0.5.
  - U 1.
  - O 0.2: it sets aside M_2(C).
- **records:** B 0.6, F 0.95, D 0.4.
- **gravity:** G 1, X 0.6, I 0.9, R 1.

## Ranking (v2, no checks recorded)

Codes run in the order motion, turns, room, records, gravity.

**Physics × axiom fit:**

```
   1  QLOBG  1.000
   2  QLMBG  0.735
   3  QLOBX  0.720  <- Candidate 1
   4  HLOBG  0.713
   5  QLODG  0.630
   6  HLMBG  0.524
```

**Physics only:**

```
   1  QLOBX  1.000  <- Candidate 1
   2  QLODX  0.944
   3  QLOBG  0.833
   4  QLODG  0.787
   5  HLOBX  0.713
```

12 of 192 combinations are zero by A42.

**Best score with each option held fixed (physics × axiom fit).**

| Fork | Scores | Reading |
|---|---|---|
| turns | L 1.00, E 0.23 | **decisive** |
| records | B 1.00, D 0.63, F 0.16 | **decisive** |
| room | O 1.00, M 0.74, P 0.32, U 0.02 | **now the biggest lever.** P fell from 0.85 in v1, because fermions and the graviton both press on one qubit per site. |
| gravity | G 1.00, X 0.72, I 0.44, R 0.25 | |
| motion | Q 1.00, H 0.71 | was a coin flip. One cone tips it to the hypercubic tick. |

## Choice of Candidate 1: Q L O B X

Candidate 1 is rank 1 on physics alone and rank 3 with axiom fit. It is chosen over QLOBG and QLMBG for three reasons:
1. **It is the only top-ranked combination whose every sector has an existing construction:**
   - compact U(1) and Yee for light;
   - staggered Kogut–Susskind fermions for matter;
   - A25 for gravity;
   - the 09-27 notes for beables.

   Neither G under O nor gravity under M has a construction, so neither can be written down whole.
2. **The goal is a TOE, not the method** (owner, 08-26).
3. **Its kill tests target the walls that do not depend on room:** chirality, one cone, gravity on a fixed grid, and numbers. If it fails there, qubits would not have saved it.

**The qubit question runs in parallel.** The kill sheet's gate G0 tests it in minutes.

## Iteration rule

- Record each outcome in `RESULTS` in `decision_matrix.py`: pass → 1, fail → 0.
- Key the outcome by the check and the candidate's settings on that check's dependency forks. A failure then removes every combination sharing those settings.
- A diagnosis that blames fewer forks gets a narrower key.
- The next-ranked survivor is the next candidate.
- If gravity fails for every option on every room, the casualty is the fixed grid. That is outside the matrix and goes to the owner.
