# J:derive:the-massive-seas-inertia-in-the-zero-mode:a1 -- attempt (Claude Sonnet 5.5, same family as the supervisor, unrefereed)

I read `docs/MINIMAL_AXIOMS_2026-06-29.md` (full, 233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (full) on main (a77a3449c9) before choosing premises. Neither axiom text nor a registered primitive supplies anything used below: every object here (the walk, the member's scalar action, the sea, the effective-action term) is supplied by a lane note. I did not run `probes/run_probe.py` (my only write area is the output folder) and I did not read earlier attempts.

## Plain-language summary

Block 147 asks whether a closed lattice, filled with a staggered-mass walker sea, can still bounce and still need rest energy m0 > mu to grow large, once the sea's own inertia (a stretching lattice stirs the massive sea) is counted. In the model as supplied, the lattice's kinetic coefficient becomes `D = 24 alpha l^3 - m_lam/2`, and the question is whether D stays positive.

- It does not stay positive in general. D is positive above one length tau_* and negative below. On the 4^3 torus D is positive at every length exactly when alpha/mu^2 >= 0.002769 (a closed form below). On Z^3 it is negative below some length for every alpha, because m_lam/l^3 grows like ln(1/(mu l))/pi^2.
- The large-length statement stands exactly: arbitrarily large lengths still need m0 > mu.
- The bounce at m = 0 survives with D > 0 only for m0/mu below a computable bound (always above 1). Beyond it, the point m = 0 becomes a maximum-size turning point of a different, small-length branch.
- For m0 <= mu, T2's "no motion" statement does fail in the modified model, but only in the D < 0 region, where the model's own rate satisfies lamdot > 2 mu (proved): the leading adiabatic order is already out of control there. So the supervisor's prior is confirmed in this sense: the small-length statement fails only where the adiabatic order already fails.
- I found no error in T3(b)'s coefficient m_lam.

## 1. Setting and every premise

Notation: ell = e^lambda; mu = 1 units; tau = mu*ell; a = alpha/mu^2; s_a = sin k_a; y = s^2/tau^2; angle brackets are averages over the momenta (all 64 modes on the 4^3 torus; the Brillouin zone on Z^3).

- ASSUMED (P1, block 146, landed, `docs/ADMISSIBILITY_RULE_THE_LATTICE_EXPANDS_...2026-09-25.md`): scalar action `L = c_k e^{3 lambda} lamdot^2 / w - w m(lambda)` with `c_k = -24 alpha`, alpha > 0; varying w gives `24 alpha l^3 lamdot^2 = m`. The landed text calls the volume exponent 3 a supplied ansatz.
- ASSUMED (P2, block 147 T1, landed): even torus or Z^3, two coin states, staggered-mass block `H = A/l + B`, `A = (sigma.s) tau_z`, `B = mu tau_x`, filled negative band; `<E> = <sqrt(mu^2 + s^2/l^2)>`.
- ASSUMED (P3, block 147 T2): source `m = m0 - <E>` (the member sees the sea's instantaneous energy).
- ASSUMED (P4, block 147 "Late source update", landed): the leading adiabatic sea energy `(1/2) m_lam lamdot^2` per site enters as the lapse-covariant effective-action term `+(1/2) m_lam lamdot^2 / w`. Then `D lamdot^2 = m`, `D = 24 alpha l^3 - m_lam/2`. The landed text states this is a conditional model and that T2's m0 <= mu conclusion is not extended to it.
- The branch version of the note (#9240 head df4a90a8) says the effect of the inertia on T2's second statement "is not computed"; the landed text controls and says the same in softer words. This attempt computes it inside P1-P4.

Provenance: the landed block-147 note on main differs from the branch note (hashes in `RECOVERY_STATUS.json`); all definitions here use the landed text.

## 2. Steps

1. CHECKED (check.py A1-A8, exact sympy). `{A,B}=0`, `H^2 = (mu^2 + s^2/l^2) I`, `[H(l1),H(l2)] = 2(1/l1 - 1/l2) A B`, and `Tr(P+ H_lam P- H_lam) = 2 mu^2 s^2/(l^2 E^2)` for symbolic s1,s2,s3, with `H_lam = -A/l`. Hence the second-order adiabatic excess per block is `lamdot^2 Tr/(2E)^3 = lamdot^2 mu^2 s^2/(4 l^2 E^5)`, giving `m_lam = <mu^2 s^2/(4 l^2 E^5)>` per site. The largest first-order amplitude over modes satisfies `eps^2 <= lamdot^2/(216 mu^2)`, attained at `s^2/l^2 = mu^2/2` (exact maximisation).

2. CHECKED (B1, numerical ODE, not exact). One 4x4 block (mu = 1/2, s = (1/2,0,0)) evolved with a C-infinity ramp so that no switching transient enters. The excess energy equals `lamdot^2 Tr/(2E)^3` to 0.9 percent at rate 0.04 and 0.6 percent at 0.02. No error in T3(b)'s coefficient. Independent landed cross-check (READING): the note `ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_A_RELABELLING_..._NOTE_2026-09-25.md` (T4 (b), lines 112-118) gives the sea's inertia for a uniform strain as `v.M.v = <(|s x v s|^2 + mu^2 |v s|^2)/(|s|^2 + mu^2)^{5/2}>/16`; with the dilation `v = 2 lamdot I` of block 146 this is `mu^2 s^2/(4E^5)`, the same expression. That note concerns the full strain tensor and the closing line, not the zero-mode sign question; no overlap in result.

3. PROVED (algebra). With `tau = mu l`: `m_lam / l^3 = mu^2 F(tau)`, `F(tau) = (1/4) < s^2/(tau^2 + s^2)^{5/2} >`; `<E> = (mu/tau) J(tau)`, `J = <sqrt(tau^2 + s^2)>`. So `D = l^3 mu^2 (24 a - F/2)`: **D > 0 iff F(tau) < 48 a.** Each summand `s^2/(tau^2+s^2)^{5/2}` is strictly decreasing in tau (C4), so F is strictly decreasing and D changes sign at most once, at `tau_*(a)` solving `F = 48 a`: D < 0 for tau < tau_*, D > 0 for tau > tau_*. Also `J/tau` is strictly decreasing to 1, so `m = mu (m0/mu - J/tau)` is strictly increasing with `m(infinity) = m0 - mu` (needs a mode with s != 0, present on both lattices).

4. PROVED + CHECKED (answer to (i), 4^3 torus). Modes have `s^2 in {0,1}` per coordinate, so `s^2 = j` with multiplicity `8 C(3,j)` (C1, enumerated). F(0+) is finite: `F_T(0+) = (1/32)(3 + 3/(2 sqrt 2) + 1/(3 sqrt 3)) = 0.13290970` (C3, exact). Since F_T(tau) < F_T(0+) for every tau > 0: **D > 0 at every length iff a >= a_T := F_T(0+)/48 = 1/512 + sqrt(2)/2048 + sqrt(3)/13824 = 0.00276895.** For a < a_T, D < 0 exactly for tau < tau_*(a); examples (E2): a = 1e-4: tau_* = 1.967; a = 1e-3: 0.7946; a = 2e-3: 0.4094.

5. PROVED (answer to (i), Z^3: the sign is lost for every alpha). Around each of the 8 corners put q = k - corner, `|q| <= 1`. There `|s| <= |q|` and `|s| >= (2/pi)|q|` (each |q_a| <= 1 < pi/2). Where `|s| >= tau`, `s^2/(tau^2+s^2)^{5/2} >= 2^{-5/2}/|s|^3 >= 2^{-5/2}/|q|^3`. This region contains `pi tau/2 <= |q| <= 1`. Summing the eight disjoint balls with measure `d^3 q/(2 pi)^3`:
   `F_Z(tau) >= (1/4)(8)(2pi)^{-3} 2^{-5/2} 4 pi ln(2/(pi tau)) = c ln(2/(pi tau))`, `c = 2^{-5/2}/pi^2`, for `tau <= 2/pi`.
   So F_Z > 48 a for `tau < (2/pi) exp(-48 a / c)`: **for every a > 0, D < 0 on an interval of small lengths.** CHECKED numerically (D4, 1-D heat-kernel representation cross-validated against a 3-D tensor sum to 1e-8): `F_Z(tau) = ln(1/tau)/pi^2 + 0.0739 + o(1)` (slope 1/pi^2 to four digits), hence `tau_* ~ exp(-pi^2 (48 a - 0.0739))` once tau_* is small (a = 0.01: 0.0181; a = 0.05: 1.1e-10). The proved bound is far weaker than the true tau_* but positive.

6. PROVED (large lengths). `(tau^2+s^2)^{5/2} >= tau^5` and `<s^2> = 3/2` on both lattices give `F <= 3/(8 tau^5)`. So D > 0 whenever `tau^5 > 1/(128 a)`. This confirms the supervisor's large-length prior in quantitative form (`m_lam <= <s^2>/(4 mu^3 l^2)` is the same estimate).

7. PROVED (sign logic). The modified constraint `D lamdot^2 = m` admits real motion at a length iff `m/D > 0`. Since m is increasing with a single zero at `tau_t` when `m0 > mu` (none if `m0 <= mu`), and D has its single zero at tau_*:
   - tau > tau_*: D > 0, motion iff m > 0.
   - tau < tau_*: D < 0, motion iff m < 0.
   - `lamdot^2 = m/D` diverges at tau_* whenever `m(tau_*) != 0` (F4, numerical value 4e7 one part in 1e6 inside).

8. PROVED (answer to (iii), the threshold). On tau > tau_* motion needs m > 0. m is increasing to `m0 - mu`, so reaching arbitrarily large lengths needs `m0 > mu`, exactly as in block 147 T2. At large length the correction vanishes (step 6), so the large-length statement stands with no change of threshold.

9. PROVED + CHECKED (answer to (iii), the bounce). Let `m0 > mu` and `tau_t` solve `J(tau_t)/tau_t = m0/mu`. Since `J/tau` is decreasing, `tau_t > tau_*` iff `m0/mu < m0_c(a) := J(tau_*)/tau_*`; and `m0_c(a) > 1` always.
   - If `m0/mu < m0_c`: D(l_t) > 0, m = 0 is a minimum-size bounce, with `lamddot = m'/(2D)` where `m' = dm/dlambda = <s^2/(l^2 E)>`. Differentiating `D lamdot^2 = m` gives this; with the sea inertia dropped it reduces to block 147's `m0^4/(48 alpha I^3)` (E8, exact sympy).
   - If `m0/mu > m0_c`: tau_t < tau_*. The allowed set is tau <= tau_t (m < 0, D < 0, lamdot^2 = m/D > 0 and lamdot -> 0 at tau_t, F8/F8b) union tau > tau_*; the stretch tau_t < tau < tau_* is forbidden. So m = 0 is a maximum-size turning point of the lower branch, and the upper branch reaches tau_* with lamdot -> infinity in finite time. The original bounce no longer exists.
   - Values (E5, E7): 4^3: a = 1e-4: m0_c/mu = 1.174; a = 1e-3: 1.793; a = 2e-3: 3.007; a >= a_T: infinity (bounce kept for every m0 > mu). Z^3: a = 1e-3: 1.691; a = 1e-2: 65.8; a = 5e-2: 1.1e10. On Z^3 m0_c is finite for every a > 0 (step 5).

10. PROVED (answer to (ii), T2 for m0 <= mu). Then `m < 0` at every finite l, so motion needs D < 0, i.e. tau < tau_*. If a >= a_T on the 4^3 torus, D > 0 everywhere and T2's no-motion statement is intact (F5). Otherwise (always on Z^3) T2's statement fails inside the model for tau < tau_*, with `lamdot^2/mu^2 = (J/tau - m0/mu)/(tau^3 (F/2 - 24 a)) =: h(tau)`. **Claim: h(tau) > 4/(1 - 48 a/F) > 4 throughout.** Proof: for m0 <= mu, `J/tau - m0/mu >= <sqrt(1+y) - 1>`, and `2 tau^3 F = <y/(2(1+y)^{5/2})>` (y = s^2/tau^2). Pointwise, with w = sqrt(1+y) > 1, `sqrt(1+y) - 1 = y/(w+1) > y/(2 w^5)` because `2 w^5 - w - 1 = (w-1)(2w^4+2w^3+2w^2+2w+1) > 0` (F2, exact factorisation). Averaging (some mode has y > 0) gives `J/tau - 1 > 2 tau^3 F`, so `h > 2F/(F/2 - 24 a) = 4F/(F - 48 a) > 4`. So **in the whole window `lamdot > 2 mu`, the minimal single-particle gap.** The bound is nearly sharp: for large tau, `h ~ 4/(1 - (tau/tau_*)^5)`, and the tabulated minima approach 4 from above as a -> 0 (4.58 at a = 2e-8 on the torus, 6.14 at 1e-6, 25.1 at 1e-4, 492 at 1e-3, 3e7 at 2.7e-3; Z^3: 4.52, 5.90, 21.1, 235). Conclusion for the question: the leading adiabatic order does not hold where it matters for m0 <= mu. T2's m0 <= mu statement is not refuted by a controlled calculation; it is replaced by "the leading-order model has a fast, non-adiabatic motion in tau < tau_*", which this method cannot resolve. The supervisor's prior (fails only where the adiabatic order already fails) is supported in this precise sense.
    - READING (supplementary, NUMERIC, not part of the proof): the first-order amplitude of the worst real mode is smaller than the gap criterion suggests (min eps^2 = 0.005 at a = 2e-8 torus, 0.12 at 1e-4, 0.67 at 1e-3, 21 at 2.7e-3; Z^3 reaches 1.09 at 1e-3 and becomes huge at 1e-2), because the massless limit commutes. This does not restore control: the rate also changes on the time scale 1/lamdot, comparable to 1/gap, which the first-order amplitude does not test.

11. CHECKED + SUGGESTED (near a bounce). Away from the window, at a bounce lamdot = 0 and the leading adiabatic term vanishes, but the sea still carries energy of second order in lamddot: numerically `lamddot^2 Tr/(2E)^5` to within 4 to 14 percent (B2, one block, three turn widths); it is smaller than the leading expression by 1/(2E)^2 (B3). SUGGESTED (an argument, not checked beyond this single-block fit): in the constraint this shifts the turn to `m = -(1/2) M2 lamddot^2` with `M2 = <mu^2 s^2/(16 l^2 E^7)>`; the dimensionless size `Xi = M2 m'/(8 D^2)` is 3e-7 (a = 0.01, m0 = 1.05 mu), 3e-5 (a = 1e-3, 1.05 mu) and 1.8e-2 (a = 1e-3, 1.2 mu). At the last point `lamddot_turn = 1.4 mu`, so the turn lasts about 1/mu and the leading order is controlled only for about |t| < 1/lamddot; where `m0/mu` is near 1 the bounce is slow and well controlled (lamddot_turn = 0.004 mu to 0.04 mu). This higher-order term is not part of the HIT.

12. Where the route stops (first unresolved step). The leading-adiabatic effective action is not controlled (a) for the whole m0 <= mu window and near tau_* in general (lamdot > 2 mu, step 10), (b) on the time scale 1/lamddot around a fast bounce (step 11). What would finish it: an exact time-dependent evolution of the filled massive sea for the homogeneous protocol `lamdot^2 = m/D` (evolve each 4x4 block under `H(lambda(t))`, obtain the sea energy, and iterate the constraint to self-consistency). That is a finite computation, not done here. Separately the owner question remains whether the member sees the sea's energy at all (block 147's reading T2/T3); nothing here changes it.

## 3. What is new, and what is not

Not new: the coefficient `m_lam` and its bound (landed in block 147; independently reproduced by the landed T4 note), T2's formulas, and the bounce formula without inertia.

New (all inside P1-P4, unrefereed, same family): steps 3-10, namely the exact sign criterion `F(tau) < 48 a`; the exact 4^3 threshold a_T; the Z^3 logarithmic divergence with an explicit proved lower bound; the sufficient large-length condition `tau^5 > 1/(128 a)`; the survival criterion for the bounce `m0/mu < J(tau_*)/tau_*` and the alternative maximum-size turning point; and the proved inequality `lamdot > 2 mu` in the m0 <= mu window.

Overlap search: `git grep` on main for the inertia coefficient finds only block 147 and the landed T4 note above; no open PR was found with this title (`gh pr list` search returned nothing); probe-view lists a `the-massive-sea-at-the-chessboard-momentum` task, which is a different object.

## 4. Scope limits

Everything is conditional on P1-P4; the effective action is a supplied model, not derived from a lattice action. Z^3 sums rely on a numerical 1-D heat-kernel quadrature (accuracy about 1e-8 against a tensor sum) and, in the tables, a cubic spline (accuracy 5e-4); the proofs in steps 5, 6 and 10 do not use them. The torus results (steps 3, 4, 6, 9, 10) use exact closed forms and monotonicity; the root tau_* and the tables are floating point.
