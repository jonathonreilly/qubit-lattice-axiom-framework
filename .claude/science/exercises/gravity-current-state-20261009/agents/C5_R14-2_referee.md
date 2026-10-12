# VERDICT: CONFIRMED WITH CORRECTIONS

1. **E2 drag and orbit map — confirmed, statistical qualifier corrected.**  In the stated linearized Newtonian model,
   `Gamma_i=2 gamma |U_i|/(3M_i c^2)` and
   `Pdot_b/P_b=-3 Gamma_eff`, with
   `Gamma_eff=(Gamma_A m_B+Gamma_B m_A)/(m_A+m_B)`; the CM velocity cancels for
   linear drag (`R14-2_report.md:88-126`; `scripts/r142_checks.out:1-32`).  The
   worker's `0.032-0.047 H0` and `x21-31` reproduce exactly when the abstract's
   `1.3e-4` precision is treated as a conservative allowance.  Kramer et al.
   Eq. (48), `0.999963(63)`, instead gives about `0.016-0.024 H0` under a
   Gaussian one-sided 95% treatment (`r142_referee_checks.out:1-6`).  Either is
   only a suggested strong-field estimate.  [Kramer et al.](https://arxiv.org/abs/2112.06795)

2. **P-r14a — kernel confirmed, costs narrowed.**  With a causal unit impulse,
   `gamma(s)=gamma0 s/(s+omega_c)` is analytic and positive-real for `Re s>0`,
   has its pole at `-omega_c`, and has zero DC value, so preferred-frame
   causality and passivity are proved (`R14-2_report.md:134-147`;
   `r142_referee_checks.py:181-183`).  The boosted pole scan and inerter
   realization remain evidence/suggestion, not general proofs.  The
   conservative `gamma0<62H0` result at `omega_c=3000 rad/s` is reproduced;
   the signed timing limit gives about `31.7H0`.  That point has
   `1/omega_c=0.333 ms`, and the report's roughly threefold budget example is
   the separate `gamma0=7H0`, `omega_c=1000 rad/s` point
   (`scripts/r142_checks.out:40-48`; `r142_referee_checks.out:8-12`).

3. **CMB correction to `tau_c` — confirmed on the worker's convention.**  The
   cubic orbit average is proportional to
   `V^2+V_parallel^2+w_i^2`, so the CMB speed cannot be omitted.  Independent
   real-space polytrope integration reproduces `4.969 ps` in-plane and
   `5.792 ps` normal to the orbit (`R14-2_report.md:168-176`;
   `r142_referee_checks.py:120-151`).  With the conservative timing envelope,
   the conditional window crosses at `ell=1.73e-9 m`, validating "near
   1-2e-9 m" (`scripts/r142_checks.out:97-101`).  The signed one-sided timing
   limit would instead give `3.98 ps` and a crossover near `3.38e-9 m`.

4. **Content equivalence — asymptotically confirmed.**  The exact Bessel
   Laplace transform gives
   `Var_E2~ln(8 Omega/gamma)/(2 pi Omega)`, whereas
   `Var_E1~[ln(8 Omega T)+gamma_E]/(2 pi Omega)`; hence
   `T_eq=e^{-gamma_E}/gamma=0.56146/gamma` (`R14-2_report.md:202-212`;
   `r142_referee_checks.py:154-179`).  This is an asymptotic near-cone
   equivalence, not an exact finite-`gamma/Omega` identity.  The same-convention
   strict budgets differ by at most 8%, and the `tau_c` lower ends by about 1%,
   subject to the shared tensor/Isaacson/sink premises
   (`scripts/r142_checks.out:69-80`).  The worker's conservative friction range
   gives `2/gamma=44-65 t_H` (about `70t_H` at `0.03H0`); the signed limit gives
   roughly `86-127t_H` (`R14-2_report.md:240-246`).

5. **Readings and prices — OPEN/OPEN confirmed; price dominance narrowed.**
   The fixed rules make both routes OPEN: each has a nonempty region, but
   neither supplies the complete spin-2/nonlinear/budget construction, and E2
   additionally lacks a field-level gravitating sink (`TESTS.md:4829-4832`;
   `R14-2_report.md:22-33,182-198`).  They tie on the listed tests at the stated
   order.  The inventory does show more named E2 assumptions—dissipative metric
   law, sink, and long history or high-pass scale—but "strictly more prices" is
   bookkeeping, not a proved ordering, because no cost metric is defined and
   E1's initial-state interpretation remains open (`R14-2_report.md:250-273`;
   `MINIMAL_AXIOMS_2026-06-29.md:87-95,173-190`).

## Strongest correct statement

Within the stated linearized, preferred-CMB-frame, Newtonian mean-field model, E2 friction gives `Gamma_i=2 gamma |U_i|/(3M_i c^2)` and `Pdot_b/P_b=-3 Gamma_eff`; Double-Pulsar timing restricts ohmic friction to `gamma/H0<0.032-0.047` under the worker's conservative abstract-level envelope, or about `0.016-0.024` under a signed Gaussian one-sided use of Kramer et al. Eq. (48), making E2's stationary memory tens to more than one hundred Hubble times.  The zero-integral kernel is causal and passive in the preferred frame and can permit faster damping only by adding a cutoff, frequency-dependent wave damping, and a larger sink budget; the conservative `62H0` point corresponds to `0.333 ms`.  The CMB velocity correctly tightens the repaired-gain ceiling to `4.97 ps` and closes the conditional window near `1.7 nm` on that same convention, while `T_eq=e^{-gamma_E}/gamma` is the correct asymptotic near-cone content equivalence and the equal-terms budgets differ by at most 8%.  Both routes remain **OPEN** and tie on the stated tests; E2 has more named assumptions in this accounting, but strict price dominance is not a theorem.

Artifacts: `C5_R14-2_referee.md`, `r142_referee_checks.py`, and
`r142_referee_checks.out`.  The worker runner and independent checker both
rerun exactly.
