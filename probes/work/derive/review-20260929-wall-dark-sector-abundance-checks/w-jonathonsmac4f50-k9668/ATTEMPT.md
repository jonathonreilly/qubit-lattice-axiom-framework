# J:derive:review-20260929-wall-dark-sector-abundance-checks:a1

Author: Claude Sonnet 5.5, same family as the sources. Same-family, unrefereed. `check.py` (39 checks, 0 FAIL, about 15 s) is the evidence for every CHECKED label below; `RECOVERY_STATUS.json` holds the hashes.

## Plain-language result

The eight-state taste cube, read the way the DM notes read it (one weak doublet qubit times a 3+1 split of the other two), has no state that is neutral under colour and weak isospin. This is an exact statement about that action, not about the axioms. A different weak action on the same eight states does have two singlets, so the statement depends on a chosen embedding.

The Coulomb enhancement under the lane's own velocity convention (relative speed, weight `v^2 exp(-x v^2/4)`) is `S = 2 pi z/(1-exp(-2 pi z))` with `z = alpha/v_rel`. I derived it again by a route different from the landed check, and it agrees with the 2026-09-30 corrigendum on main. The archived `pi z` form is the same function at half the coupling.

Pushing that factor through a freeze-out calculation gives a conditional table, not a prediction. If a Dirac dark pair feels `alpha_X = alpha_LM` as a Coulomb force, as the same coupling in `sigma v` implies, then at 16 v it gives Omega h^2 of 0.072 to 0.085, not 0.1275. The Kolb-Turner closed form cannot be used for this, because it overstates by more than 40%. Which dark representation, conjugacy and counting actually apply is not supplied by anything on main. That is the first unresolved step (step 14).

## What I read (stated as required)

1. READING. I read in full `docs/MINIMAL_AXIOMS_2026-06-29.md` and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` on current main (`a77a3449c9`). Supplied: a cubic lattice, a one-site possibility domain `M_2(C)`, a nearest-neighbour distribution rule, and records (`MINIMAL_AXIOMS_2026-06-29.md:24-83`). It states there is no dynamics, no mass, no gauge group and no cosmology (`:114-130`, `:173-190`). Approved primitives are only `scale_reference_primitive` (`a^{-1} = M_Pl`), `kinetic_isotropy_primitive` and `realized_state_primitive` (`PRIMITIVE_REGISTRY_CHECK.md:31-129`). The last one makes the realized history (including T_0, H_0, Omega_Lambda) registered data (`:98-114`). So every premise listed in step 2 is supplied by a lane or is data, not an axiom.
2. ASSUMED (lane/model premises; none is an axiom or a primitive except where noted):
   - P-emb: `C^8 = (C^2)^3`; fibre = one qubit; `SU(3)_c` acts as Gell-Mann/2 on the 3-dim symmetric subspace of the other two qubits (zero on the antisymmetric state); `SU(2)_L` is spin on the fibre; `Y = (1/3) P_sym - P_anti` (`scripts/dm_dark_candidate_consistency_check.py:7-20`). Identification with physical colour is a separate bridge (`CL3_COLOR_AUTOMORPHISM_THEOREM`, as quoted in the kill of T54).
   - P-S: s-wave, `V = -alpha/r` between a pair of equal masses `m` (reduced mass `m/2`), attractive for a particle-antiparticle singlet. No bound states, no resonances, no Yukawa screening.
   - P-v: velocity convention: `v` is the relative speed; weight `v^2 exp(-x v^2/4)`, `x = m/T` (corrigendum, `scripts/dm_full_closure_same_surface_thermal_support_common.py:6-20`).
   - P-freeze: the supplied model is `Omega h^2 = K x_F/(sqrt(g_*) M_Pl <sigma v>)`, `K = 1.07e9 GeV^-1`, `x_F = 25`, `<sigma v> = pi alpha_X^2/m^2` (`DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md`, section A).
   - P-cosmo (my Boltzmann solver): radiation domination, constant `g_* = g_*S = 106.75`, no entropy injection, `T_chi = T` up to a stated cutoff `x_max`, spin degeneracy `g = 2`, `M_Pl = 1.2209e19 GeV`, `T_0 = 2.7255 K`, `g_*S0 = 3.909`, `rho_c/h^2 = 1.05367e-5 GeV cm^-3`. T_0 and the density scale are data (realized-state primitive).
   - P-mass/coupling: `m = 16 v = 3940.5 GeV` (a scanned candidate, unproved, T55) and `alpha_X = alpha_LM = 1/(4 pi 0.5934^{1/4}) = 0.090668` (supplied choice, T56). Neither is derived here.
3. CHECKED prior art (landed on main, so nothing in this step is new): the 2026-09-30 corrigenda in the bypass note (Sommerfeld factor 2, dark "singlet" meaning, comparator) and the scripts `dm_sommerfeld_kernel_radial_schrodinger_verification.py` and `dm_dark_candidate_consistency_check.py`. The source SHAs and sha256 of all 14 named objects matched `SOURCE_MAP.json` (see `RECOVERY_STATUS.json`). T54-T57 attack/kill already contain: no singlet on the cube; the factor 2; Dirac versus self-conjugate counting; a 0.079 Dirac figure; and a counter-model with two singlets (kill T54, error 2).

## A. Charge census (exact, sympy)

4. CHECKED (`A1-A3`). In P-emb the three algebras commute and close, `Tr Y = 0`, `C_3 = (4/3) P_sym` and `C_2 = (3/4) 1` as exact matrix identities. A gauge singlet would need `C_2 = 0`. Hence there is no `SU(3) x SU(2)` singlet. This is a proof inside P-emb (one line: `C_2` is the scalar 3/4). Rank of the stacked generators is 8 in the rational basis (`A4`).
5. PROVED + CHECKED (`A5, A6`). The commutant of `su(3) x su(2)` in `M_8` has dimension exactly 2 (Schur, multiplicity-free `(3,2) + (1,2)`), spanned by `P_sym x 1` and `P_anti x 1`. Therefore any `U(1)` commuting with the colour and weak algebras is `a P_sym + b P_anti`. Tracelessness forces `b = -3a`, giving `Y = (1/3, -1)` up to scale. The hypercharge ratio is fixed by the embedding and tracelessness; it is not a free choice.
6. CHECKED (`A7, A8`). With `Q = T_3 + Y/2` the charges are `2/3 (x3), -1/3 (x3), 0 (x1), -1 (x1)`. The one neutral colour-singlet is the `T_3 = +1/2` member of a weak doublet with `(C_3, C_2, Y) = (0, 3/4, -1)`. It is not a gauge singlet and not a dark candidate.
7. READING (`A9`). The check over the three fibre-axis choices for `|000>` and `|111>` is a relabelling by tensor-factor permutation, so it cannot fail and does not discriminate (this agrees with the kill of T54).
8. CHECKED (`A10, A11`). Counter-embedding on the same `C^8` and the same `SU(3)`: take `SU(2)'` = fibre spin acting only on the symmetric-base sector. It is a valid `su(2)` commuting with `su(3)`, with content `(3,2) + 2 x (1,1)`, and `C_3 + C_2'` has eigenvalue 0 with multiplicity 2. With quark hypercharge `a = 1/3`, tracelessness gives `c + d = -2`, so the two singlets are not both `Y`-neutral. If both were, then `a = 0`. So "no singlet" is a property of the weak action, not of `C^8`; and "a neutral singlet with a charged quark sector" is excluded by tracelessness alone.

## B. Sommerfeld normalisation

9. PROVED + CHECKED (`B1, B2, B3c`). Radial equation for `u = r R` at relative speed `v` with `k = mu v`, `mu = m/2`: `u'' + (k^2 + 2 mu alpha/r) u = 0`. In units `k = 1` this is `u'' + (1 + 2 eta/r) u = 0` with `eta = mu alpha/k = alpha/v`. The solution regular at the origin with `u'(0) = 1` is `u = r e^{-ir} 1F1(1 + i eta; 2; 2ir)` (the Coulomb function `F_0/C_0`). Its asymptotic amplitude is `1/C_0`, so `S = |psi(0)|^2/|psi_free(0)|^2 = C_0^2(-eta)`. By `|Gamma(1+i eta)|^2 = pi eta/sinh(pi eta)`, `C_0^2(eta_C) = 2 pi eta_C/(e^{2 pi eta_C} - 1)`, hence `S = 2 pi eta/(1 - e^{-2 pi eta})` with `eta = alpha/v_rel`. Checked to 1e-40 for the Gamma identity (`B1`), the ODE residual and `u'(0) = 1` (`B2a`), and the amplitude extracted from the Kummer solution to better than 1e-6 for `eta` = 0.1 to 2 (`B2b`). This route does not use the ODE integrator or `coulombf` of the landed check.
10. PROVED (symbolic, `B3a, B3b, B4a, B4b`). With `beta = v_rel/2` (per-particle CM speed): the textbook `pi alpha/beta` form is identically `S(alpha, v_rel)`. The archived `pi z` form with a relative-speed weight equals the correct kernel at `alpha/2`. The Maxwell-Boltzmann relative-speed density is `4 pi v^2 (x/4pi)^{3/2} e^{-x v^2/4}` with `<v^2> = 6/x`, which becomes `u^2 e^{-x u^2}` in `u = v/2`.
11. CHECKED (`B5a-c`). The thermal average `<S>` at `x = 25`, `alpha_LM` is 2.061429 in either consistent convention (agree to 1e-15). The archived pairing gives 1.475172, which equals the correct value at `alpha/2` (1e-15). For large `x`, `<S> -> 2 sqrt(pi) alpha sqrt(x)`.

## C. Propagation

12. CHECKED (`C1-C3`, `C11-C14`). The supplied Kolb-Turner formula gives 0.1275 at the lane's inputs. My own Boltzmann solver (K_2 equilibrium, Radau) gives 0.1259 with `S = 1` (1.3% below). The Dirac pair, counted as `n_chi = n_chibar` with total density, gives exactly 2x (two-species check). The corrigendum's visible numbers reproduce independently: archived `R = 5.442020`, corrected `S_vis = 2.3143`, `R = 7.9716`, `eta_pred = 4.38e-10` (-28.4%), matching mass 4657 GeV = 18.9 v. At `alpha = 0.0454` I get `eta_pred = 2.558e-9` against the note's rounded `2.55e-9`. The difference is the rounding of 0.0454, not an error. Conditional table, 16 v, `alpha_X = alpha_LM`, Omega h^2:

| dark-pair model (premises P-S, P-cosmo) | Omega h^2 |
|---|---|
| lane: self-conjugate counting, no Coulomb force (`S_dark = 1`), closed form | 0.1275 |
| same, Boltzmann solve | 0.1259 |
| Dirac counting, no Coulomb force | 0.252 |
| Dirac, attractive Coulomb at `alpha_X`, correct kernel, `T_chi = T` to `x_max = 1e3 / 1e4 / 1e6 / inf` | 0.0850 / 0.0760 / 0.0727 / 0.0724 |
| same with the archived half-argument kernel | 0.136 / 0.124 / 0.1195 / 0.119 |

   The mass giving 0.120 in the correct-kernel row is 19.0 to 20.6 v (`Omega ~ m^2` up to a 0.6% logarithmic shift; `C8`). Sensitivity (`C10`): spin degeneracy 2 to 4 moves Omega by +1.6%; `g_*` 106.75 to 100 moves it by +3.4%.
13. CHECKED (`C5, C6`), conditional on P-S, P-cosmo. (a) A Dirac pair feeling `alpha_LM` as a Coulomb force gives Omega h^2 between 0.072 and 0.085 at 16 v for any cutoff `x_max >= 1e3`; it misses 0.1275 by -33% to -43% and Planck's 0.120 by -29% to -40%. The spread is set by when the dark state kinetically decouples, which is not supplied. (b) The Kolb-Turner closed form with `<S>(x_F = 25)` in `<sigma v>` gives 0.1237, over 40% above every cutoff value. The closed form assumes `sigma v` is constant after freeze-out, while the Coulomb factor keeps growing as `sqrt(x)` (`B5c`). So it cannot be used for the dark side once the Coulomb force is included. (c) The corrigendum's sentence that Omega_DM h^2 = 0.1275 is "unchanged" is correct only when the dark pair has no Coulomb force and self-conjugate counting. Both are premises the corrigendum itself questions (its item 3 says the dark state is a colour fundamental that feels a force).

## What is new, and what is not

- Not new: no singlet on the cube (landed script, kill T54); factor-2 Sommerfeld (corrigendum plus landed script); Dirac versus self-conjugate (kill T55/T56); the 0.079 figure (T56); the counter-embedding with two singlets (kill T54 error 2); corrected R, eta and mass numbers (corrigendum, reproduced in step 12).
- New in this attempt, small and scoped: exact sympy versions of the census with the commutant dimension 2 and unique traceless `Y` (steps 4-8); a Kummer/Gamma derivation of `S` (step 9); the cutoff-dependence of the dark-alone Omega (0.072 to 0.085, where T56's 0.079 is one point of a range); and the quantified failure of the closed-form Kolb-Turner when `sigma v` carries the 1/v factor (step 13b). None is a result about the axioms, and I do not call any of it a HIT.

## First unresolved step

14. The physical dark carrier. Neither the axioms nor anything on main supplies the dark state's gauge representation, conjugacy, force, or counting (Dirac versus self-conjugate), nor its kinetic decoupling or the bound-state/resonance structure of its Coulomb channel. Until it does, step 12 is a conditional table. In particular the bypass identity `eta = C m^2` and "R = 5.48" have no consistent dark-side inputs: with a force the dark pair's `S_dark != 1`, without one `alpha_X` is not a gauge coupling. A defect in the selected candidate says nothing about whether some other dark sector exists, and `31/9` remains a group-theory factor rather than a density ratio.

Remaining obligations are in `RECOVERY_STATUS.json`. A failed route is not a no-go: negative statements here are limited to the stated embedding and model, and no N1-N8 promotion is claimed.
