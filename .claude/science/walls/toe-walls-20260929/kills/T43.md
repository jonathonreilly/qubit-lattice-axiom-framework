# Kill check on T43

Checker: Claude Sonnet 5.5, same family as attacker and supervisor; not independent. Read the axioms memo and registry check in full, L11-W4/W8, the attack and the notes it cites. Re-ran all seven scripts (identical output). Independent code (`T43_scratch/k1_indep2d.py`, `k2_4d.py`, `k3_noise2d.py`) matches to 5 digits and extends to 2D L=32, 4D L=10.

## Outcome verdict
**WEAKENED.** The computation is right. The reading is not: it is the standard staggered index theorem, the coefficient is 1 only in the continuum limit, and W8 was not misstated.

## Route verdicts
| Route | Verdict | Reason, with evidence |
|---|---|---|
| R1 assembly | wounded | Prior art; asymptotic; tested only with exact zero modes (errors 1 to 3). |
| R2 Vafa-Witten | dead (agree) | Assumes the mass class. |
| R3 Nelson-Barr | wounded (agree) | Untested; citations unverified. |

## Errors found
1. **Standard physics, already in the repo.** Phase = index x angle is Adams (PRL 104, 141602, 2D U(1) spectral flow), Follana-Hart-Davies (PRL 93, 241601), Smit-Vink (NPB 286, 485); Duerr-Hoelbling (PRD 74, 014513) study staggered complex mass. In the repo: the 07-02 supplier note has this Gamma_f, this surface, flow -2Q; the 07-02 paired-shift note (C2) names Adams; the 05-30 note (lines 137, 198) lists it; the 06-04 note (section 1) has the anomaly bookkeeping; the parent note (lines 52, 410) says an admitted complex mass phase reopens theta. W8 already says "physics sees only the sum". No open PR touches it. The attack cites none of this, so "no link is misstated" is unsupported.
2. **Coefficient does not converge to 1 at fixed mass.** m=0.5, 2D L=8 to 32: 0.691, 0.696, 0.697, 0.697, 0.697; 4D L=4 to 10: 0.433, 0.521, 0.542, 0.548. Only a to 0 gives 1: zero-mode chirality 1-g = pi/L^2; 4D m=0.02, L=4 to 10: 0.640, 0.833, 0.904, 0.937 (1-c ~ 6.3/L^2). At m >= 0.1 it depends on the operator: Gamma(1+kappa D^2) moves c(0.5) from 0.65 to 0.78. And {Gamma_f, D} != 0 (07-02: 0.48), so the exact paired-shift identity (07-02 L3) does not carry over. "(theta_g + N alpha)Q" is asymptotic, with non-integer N_eff(m).
3. **Scope.** Only exact-zero-mode uniform flux. With link noise (2D L=12, Q=1, m=0.05) c = 0.973, 0.954, 0.741, 0.434 at sigma = 0, 0.05, 0.2, 0.4; Q=0 configs get a non-topological phase (std 0.14). The hot SU(3) leg measures no Q. Sectors are supplied by the flux (W3 untouched).
4. **Pre-registration.** As registered, P2 failed (0.69, L-independent) and P3 failed at 2 of 3 points; MISFRAMED was chosen afterwards. DEVIATIONS.md says so; the Reading still says "registers Q".
5. **Mislabel.** Site-diagonality is not "hidden": 06-13 Step A' names it a consumed premise with a computed violation; W4's scope excludes Wilson shifts.
6. **Missed consequence (helps the attack).** The 4D phase is C-even ((-1,-1) equals (1,1)); 2D is C-odd. So 06-13 Step B ("any emergent Q is conjugation-odd", a 2D check) fails in 4D.

## Corrected plain-language verdict
The tie the attack found is the ordinary chiral anomaly: a taste-singlet pseudoscalar mass adds a phase proportional to the winding number, reaching the integer count only as the lattice spacing goes to zero. The lane already knew the two angles combine, and the wall stands: nothing here makes the sum zero. Passing it costs three supplied items: a multi-link mass, a supplied winding number, and one symmetry (T23).
