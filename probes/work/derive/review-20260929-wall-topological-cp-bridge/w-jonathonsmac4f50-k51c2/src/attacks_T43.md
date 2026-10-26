# Attack on T43: Strong CP mass side on a supplied surface, and no link between the two halves of theta-bar

Attacker: Claude Sonnet 5.5, same vendor family as the supervisor (Opus 5.5); same-family checks, not independent referees.

Read: `MINIMAL_AXIOMS_2026-06-29.md` and `PRIMITIVE_REGISTRY_CHECK.md` in full; L11-W4, W8; the operator-basis, pairing, joint-bridge, paired-shift, flavored-grading, ABJ P-REC, emergent-Q reality and taste-singlet second-mass notes; siblings T41, T42, T23.

## Verdict in plain words
The lane proves the mass phase vanishes for a mass direction that cannot carry it: the staggered-sign mass rotates away exactly. The mass that carries the strong-CP phase is the taste-singlet pseudoscalar. It is multi-link, absent from the lane's mass class, and its determinant phase is proportional to the same winding integer as the gauge angle. So "no link" is misstated: both halves enter through one sector phase. What remains is one sum, one symmetry and a hidden premise (masses are site-diagonal). Not passed; moved onto T42 and T23.

## The wall (checked)
- Plain: The mass half of the strong-CP zero is shown for one kind of mass, and nothing ties it to the gauge half although only their sum is physical.
- Precise: derive from the axioms that the CP-odd mass phase vanishes (W4) and a mechanism fixing theta_gauge + arg det M jointly (W8). A supplied class does not pass.
- Real? Open, but misstated twice. M_eps is the taste-dressed sign mass (`ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md:75-80`), already inert by `THETA_ASSEMBLY_PAIRED_SHIFT_...2026-07-02.md:63-82`. The link is the paired shift (`STRONG_CP_JOINT_BRIDGE_FAILS_...2026-06-04.md:48`); the 07-02 supplier note builds its taste-singlet grading with no determinant (its runner has no `det`, grep). No open PR (36) touches it.

## Load-bearing premises
| Premise | Kind | Path:line | If wrong | Tested? | Cheapest test |
|---|---|---|---|---|---|
| Mass term site-diagonal | hidden | `THETA_EMERGENT_Q_WEIGHTING_REALITY_RG_STABLE_...2026-06-13.md:72,144`; `THE_TASTE_SINGLET_SECOND_MASS_...2026-09-03.md:103` | CP-odd multi-link mass allowed | partly | below; T21 |
| M_eps = 0 | supplied | `STRONG_CP_OPERATOR_BASIS_...2026-05-19.md:295-317` | nothing changes | yes | done |
| Winding phase links the halves | method | `THETA_ASSEMBLY_PAIRED_SHIFT_...:63-82` | halves independent | no | below |
| Orientation swap / reality of the whole weight | reading | `MINIMAL_AXIOMS_2026-06-29.md:38,58` | both halves open | parked | T23 |
| Positive weight | supplied | T42 | gauge half open | audited | T42 |

## Routes
| Route | Approach | Premise dropped | Must believe | First artifact | Cost | Changes | Verdict |
|---|---|---|---|---|---|---|---|
| R1 assembly (misframe) | mass phase and theta share e^{i(theta_g + N alpha)Q} via the taste-singlet grading | joint basis; mass class | sectors exist (T42 W3) | this test (checked) | low | T43 becomes T42 + T23 | survives as reframing; blocked-equivalent as proof |
| R2 outside: Vafa-Witten (PRL 53, 535; NPB 234, 173, 1984) | pairing makes det(D+m) e^{-S} >= 0 | none | mass in the pairing class | lemma: pairing protects only eps-commuting masses; checked: singlet direction breaks it | low | T42 | dead as a pass (assumes the class); prices it |
| R3 parity / Nelson-Barr (Beg-Tsao PRL 41, 278; Mohapatra-Senjanovic PLB 79, 283; Nelson PLB 136, 387; Barr PRL 53, 329) | orientation-swap invariance kills E.B and the singlet mass together; CKM phase state-level, real determinant | chiral law | achirality plus radiative stability | missing: leakage with the framework CKM carrier | high | T23, T41, T45 | wounded: leakage untried |

## Test run
- Pre-registered (`T43_scratch/PREREG.md`): P0 construction valid; P1 eps direction inert; P2/P3 singlet direction phase proportional to Q, coefficient 1 +- 0.25 (2D), 1 +- 0.3 (4D); P4 Hermitian-type flavour class inert; P5 linear. Fail: singlet phase not tied to Q.
- Script: `T43_scratch/{p0_construction,p0b_4d,p2_2d,p2b_mscan,p3_4d,p1_su3,p5_k_real}.py`, outputs `*_out.txt`; deviations in `DEVIATIONS.md`.
- Result: P0 pass. The spin-taste singlet equals the 07-02 note's Gamma_f exactly (2D, flux and free) and (-1)^{x1+x3} times the symmetrised product of shifts in 4D. P1 pass: |arg det| <= 1e-14 on 2D flux, 4D flux, six SU(3) hot 4^4. P2: 2D L=8, m5/m=0.2, arg det = -0.2727, -0.5327 for Q=1,2 (ratio 1.95), sign flips with Q, 0 at Q=0; coefficient 0.69 at the pre-registered m=0.5, so that criterion FAILED. A post hoc scan gives 0.98 at m=0.05, L=16. P3: 4D Q=0 sectors 0; L=6, m=0.1: c=0.81, 0.74 for Q=1,2 (pass); L=4 (0.63/0.45) and L=6, m=0.5 (0.52/0.49) fail; 4 and 8 zero modes. P4 pass: |arg det| <= 3e-14 for arbitrary complex flavour phase; control gives generic phases (up to 2.3 rad). P5 pass. Unregistered: on SU(3) hot the singlet phase is small (1e-3) and even under U to U*; it is odd in m5 (2D); Hamiltonian M2 is K-odd (exact).
- Reading: the eps direction is inert, the singlet direction registers Q with N = 2 tastes in 2D (c to 0.98); 4D is consistent with N = 4 but unconverged (c = 0.81). Coefficient below 1 is a lattice-scale factor (post hoc).

## Outcome
MISFRAMED. Cheaper question: is the coefficient of the taste-singlet (gamma5 x 1) mass, equivalently the sector phase (theta_g + N alpha), zero, and does one symmetry (orientation swap; reality of the weight) forbid E.B and that mass together? Note U to U* invariance cannot decide it, because the phase is even under it. Price: site-diagonal masses plus T23 plus T42's positivity.

## Claims and labels
- eps-direction mass phase inert: proved (07-02 L2, unaudited); checked here.
- Singlet-direction determinant phase proportional to Q; flavour-class inertness: checked, U(1) and hot SU(3) only, small lattices.
- Site-diagonality is the hidden premise, and the singlet mass is multi-link: proved for the Hamiltonian version (09-03, unaudited); Euclidean 4-link form checked.
- Radiative stability of arg det, orientation swap killing both halves: suggested.
- Vafa-Witten, Beg-Tsao, Nelson-Barr: templates only, from memory.
