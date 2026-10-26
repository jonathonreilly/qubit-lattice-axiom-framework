# J:derive:review-20260929-interacting-cones-and-chiral-carriers:a1 — attempt 1

Worker: Claude Sonnet 5.5, same model family as the source. Unrefereed. No agents spawned, nothing in the repository edited,
no claim.py / run_probe.py / commit performed (output directory only).

**Plain-language summary.** The task has two halves: (i) the interacting speed-of-light gap between a lattice walker and a lattice
scalar, (ii) interacting chiral carriers. I took ONE obligation, the first half's walker loop: derive the loop integrand myself,
settle the order of the limits (momentum p, scalar mass mu, volume), and give the numerical error. Result: the walker's one-loop
speed shift is **-0.0116752(1) g^2 in both orders of limits** (mu to 0 after p to 0, and mu = 0 first). The source note's separate
"mu = 0 exactly" value (-0.009564, giving +0.0284 g^2) is not reproduced; it equals the pointwise number plus the infrared term
counted twice (reading). The infrared term itself is a clean exact result: g^2/(48 pi^2). The qualitative claim of the note (the two
speeds differ by about 0.026 g^2 at this order) survives. The chiral-carrier half is untouched.

## 0. What I read (state of reading)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (current main checkout `main_wt`; origin/main fetched at 3e1a2dd). Lattice (`Z^3`, cubic),
  Qubit, Admissibility, Record. It supplies **no dynamics, no time metric, no fields**: "Admissibility ... does not choose a
  Hamiltonian or transfer operator ... define a time metric". So the walker, the scalar, the Yukawa coupling and Hamiltonian time are
  all supplied comparator content of the note, none is an axiom consequence.
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` in full. Approved primitives: `scale_reference_primitive`,
  `kinetic_isotropy_primitive` (`c_t = c_s`, hypercubic `Z^3 x Z_tau`), `realized_state_primitive`. The note's continuous-time
  surface is exactly the one where `kinetic_isotropy_primitive` is NOT used, so nothing below touches that primitive.
- Source branch `claude/toe-viability-probes-20260927` frozen at `fd51a1f4c7f3...`; all 29 task source objects verified by sha256
  (RECOVERY_STATUS.json). I read in full: the one-light-cone note (242 lines), the lattice-handedness note (404 lines), and the
  note's runner `scripts/one_light_cone_under_interactions_...second_order_2026_09_27.py` (same frozen commit; it is not in the
  task's `source_paths` but is the "paired code"). Neither note is on origin/main (searched `docs/` of origin/main; no
  corrected version exists there). Prior attempts: `probes/work/derive/one-cone-for-field-and-walker` (tree-level K/alpha only),
  `filling-between-the-a-terms-levels-chiral-content` (free-fermion filling; not this). No loop-level attempt for this unit.
- The numbers -0.009564 (mu = 0 exactly) and +0.0284 appear **only in the note text** (grep of the whole frozen branch: no code, no
  log). The runner computes only mu >= 1/8 at p = 0.02 and a two-point mu^2 fit.

## 1. Setting and premises (every one ASSUMED comparator content)

- **S1 ASSUMED.** Walker `H = sum_k psi_k^dag s(k).sigma psi_k`, `s_j = sin k_j`; nodes at `{0,pi}^3`, speed 1; `s(k+Q) = -s(k)`, `Q=(pi,pi,pi)`.
- **S2 ASSUMED.** Scalar, Hamiltonian time, `Omega_q^2 = mu^2 + sum_j 4 sin^2(q_j/2)`, propagator `1/(omega^2+Omega^2)`.
- **S3 ASSUMED.** Coupling `g phi_x eps_x psi_x^dag psi_x`, `eps_x = (-1)^{x1+x2+x3}`; it moves momentum by `Q`. `g -> 0` first; all
  numbers are coefficients of `g^2`. Filled negative-energy sea. Scalar mass `mu` is the renormalised mass in the propagator.
- **S4 ASSUMED (scope).** Infinite-volume integrals (Brillouin-zone integrals), p > 0 or p -> 0 *after* the integral is formed. Finite
  volume is NOT treated (see step 18).
- **S5 READING.** "Walker speed shift" `delta v_psi = d(delta E)/dP` at `P = |p| -> 0`, `p = (0,0,P)` (equal to the note's `(p,0,0)` by
  an exact cubic relabelling), with `E = sin P + delta E(p)`.

## 2. Loop integrand (independent derivation)

- **1 PROVED (residue).** For lambda = +-e: `int dw/2pi 1/(w^2+Om^2) 1/(i(nu-w)-lambda)` equals `(1/2Om)/(E-e-Om)` for lambda=+e and
  `(1/2Om)/(E+e+Om)` for lambda=-e, `E = i nu`. Close the contour on the side without the fermion pole (integrand ~ 1/w^3); the only
  pole is the scalar's at -+ i Om. Executed symbolically in check.py A1 and confirmed by a direct real-line quadrature (A1b, 2e-22).
  Hence the Euclidean self-energy `Sigma(E,p) = g^2 int d^3q/(2pi)^3 sum_{+-} <u_+(p)|P_{+-}(p')|u_+(p)> (1/2Om) /(E -+ (e' + Om))`,
  `p' = p - q + Q`, which is the Rayleigh-Schroedinger sum of the note including the filled sea (the P_- term *is* the process the note
  calls "blocked vacuum" subtracted).
- **2 PROVED.** Overlaps `<u_+(a)|P_{+-}(b)|u_+(a)> = (1 +- a.b)/2` (A2), and `s(k+Q) = -s(k)` (A2b), so with `c = shat(p).shat(p-q)`,
  `e_k = |s(p-q)|`: weights `(1-c)/2` (P_+) and, after `q -> -q` in the P_- term (Omega, BZ measure even), `(1+c)/2`. Combining (A2c):
  `delta E(p) = g^2 int d^3q/(2pi)^3 (1/2Om) [e_p - c (e_k+Om)] / [e_p^2 - (e_k+Om)^2]`.
- **3 ASSUMED/READING.** `delta E = <u|Sigma(e_p)|u> + O(g^4)` (first-order shift of an isolated level). Caveat: at tree level the two
  speeds are equal, so collinear emission `p -> p-q + q` has a vanishing denominator when `mu = 0` (`e_p - e_k - Om = 0`). In the
  continuum this is a removable singularity (step 5: the overlap `(1-c)` vanishes there); on the lattice the same structure
  appears; the finite-P integrals below are finite and converge.

## 3. Continuum Weyl pair (no lattice): exact results

Fermion `e=|k|`, `Om = sqrt(q^2+mu^2)`, `k = |p-q|`, `c k = P - q cos(theta)`.

- **4 PROVED (A3a, A3b).** Law of cosines `c k = (P^2 - q^2 + k^2)/(2P)`; change of variables `(2pi) q^2 dq dcos = (2pi) q k dq dk / P`.
  For `mu = 0` the integrand per `dq dk` is *exactly* `-(q-k)/(16 pi^2 P^2)`: the numerator `2P^2 k - (P^2-q^2+k^2)(k+q)` factors as
  `(q-k)((q+k)^2 - P^2)` and cancels the denominator. The collinear singularity of step 3 is thereby shown removable.
- **5 PROVED (A4).** `k` ranges over `[|q-P|, q+P]`. For `q > P` the `k`-integral of `-(q-k)` is `0` (symmetric interval); for `q < P` it is
  `2q(P-q)`. Hence **`delta E(P) = g^2 P/(48 pi^2)` exactly, for every P and every spatial cutoff Lambda >= P**. All of it comes from the
  infrared shell `q < P`; the massless angular density vanishes identically for `q > P`.
- **6 PROVED (A5).** `mu > 0`, `P -> 0` first: the angular average of the P-derivative of the integrand at fixed q is
  `(1/3)(Om-q)/(Om q (q+Om)^2)` (zero at `mu = 0`); with `q = mu sinh t` the radial integral is `g^2/(6 pi^2) int_0^oo sinh t e^{-3t} dt = g^2/(48 pi^2)`
  (`J = 1/8`). Same number, independent of mu.
- **7 CHECKED (A6, A6b; mpmath 20 digits).** Direct 2D quadrature of the full continuum integrand: `delta E/P = 0.0021108579925487` at
  `mu = 0` for P = 0.01 (Lambda = 5 and 500), P = 0.002; `1/(48 pi^2) = 0.00211085799254870`; and for `P = 1e-3 << mu = 1` the value
  approaches it as Lambda grows. **The two orders agree in the continuum.**
- **8 READING.** The pointwise-in-q derivative (what one gets by differentiating under the integral at `mu = 0`) is exactly 0 in the continuum;
  the true value `1/(48 pi^2)` is the nonuniform infrared region `q ~ P`. So "differentiate under the integral at mu = 0" is the wrong
  object, and the correction is universal (set by the IR region, not by the lattice).

## 4. Lattice: numerics with error (floating point, double precision)

Quadrature: Gauss-Legendre on `[0,pi]^2 x [-pi,pi]` with the smooth-step map `t = x^3(10-15x+6x^2)` clustering at the zone corners
(where `|s(p-q)|` and `Om` vanish); disjoint from the source's midpoint grids.

- **9 CHECKED (B1, B1b).** `P -> 0` first at fixed mu, derivative taken analytically (sympy) then integrated: mu = 1, 1/2, 1/4, 1/8, 1/16 ... 1/256 converge
  between N = 100 and 160 to 2e-8 and reproduce the note's quoted values (-0.0096707, -0.0110696, -0.0115076, -0.0116301) to all printed
  digits. (Reproduction; not new.)
- **10 CHECKED (B2).** `mu -> 0`: differences of successive halvings shrink by ~3.8 (mu^2 with a logarithm), and the fit `V0 + a mu^2 + b mu^2 ln mu`
  on two overlapping triples gives `V(0+) = -0.011675239`, the two triples differing by 4e-11. Quoted as `-0.0116752(1)` (the error is dominated by the assumed extrapolation form, not by the quadrature).
  The note quotes -0.011675(1): agreement; the added content is the error control and the extrapolation form.
- **11 CHECKED (B3).** The pointwise derivative at `mu = 0` exactly: `V_naive(0) = -0.0137860967` (N = 100 vs 160 agree to 2e-9).
- **12 CHECKED (B4).** `V(0+) - V_naive(0) = 0.00211086`, equal to `1/(48 pi^2) = 0.0021108580` within 1e-11 (check.py prints diff -1.1e-12). This is the continuum infrared
  term of step 6/8 reappearing on the lattice.
- **13 CHECKED (B5, B5b).** The *other* order, at mu = 0 exactly, finite P, then P -> 0, direct lattice integral of the unexpanded integrand:
  `dE(P)/sin P` = -0.011323 (P=.4), -0.011543 (.2), -0.011630 (.1), -0.011661 (.05), -0.011672 (.025); quadrature sensitivity 3e-7 to 4e-6
  (N-change printed by check.py), so deviations from V(0+) are 3.5e-4, 1.3e-4, 4.5e-5, 1.4e-5, 3.4e-6 with errors up to ~4e-6: a monotone approach to
  -0.011675 with deviation falling roughly as P^1.5 to P^1.9 (fit exponent 1.85, noisy). It does not head to -0.009564.
- **14 SUGGESTED (first unresolved step).** The lattice identity `lim_{P->0} V_fin(P, mu=0) = V_naive(0) + 1/(48 pi^2)` = `V(0+)`. Argument: near
  `q = 0` the lattice integrand equals the continuum one times `1 + O(q^2, P^2)`, away from the IR shell the pointwise derivative is
  integrable, so the nonuniformity is the continuum one (steps 5, 8). A proof needs an explicit dominated-convergence bound for
  `(F_lat - F_cont chi_{|q|<rho})/P` uniform in P, including the point `k = p - q = 0` where `shat(k)` is direction-dependent. Not done.
  Steps 12 and 13 are numerical support (agreement to 1e-11 on the mu->0 side; direct finite-P approach to 3e-6 at P = 0.025), not a proof.
- **15 CHECKED / READING (B6, B6b).** The note's "`mu = 0` exactly" number `-0.009564` is >= 2.0e-3 away from every finite-P value at P <= 0.05
  and from the pointwise number; numerically `V_naive(0) + 2/(48 pi^2) = -0.0095644`, i.e. the printed value to six digits. READING (not
  proved; the author's code is not in the frozen branch): the infrared term was counted twice (added to a quantity that already contained it, or a
  finite-grid evaluation at `mu = 0` mixed the two limits. Consequence: the order-of-limits paragraph of the note ("The two differ by an
  order-of-limits term"), and "`+0.0284 g^2` at zero scalar mass", are not supported by the supplied formula.

## 5. Scalar side and the gap

- **16 CHECKED (C1, C2) — partial.** Same formula as the note, `chi(nu,q) = <(1+shat.shat) 2E/(nu^2+E^2)/2>`, midpoint-grid evaluation with growing N:
  `(chi(r,0)-chi(0,r))/r^2 = -0.07479 (r=.2, N=512), -0.07556 (.1, N=768), -0.07579 (.05, N=1024)`, extrapolated (measured step ratio) to
  `A-B = -0.0759(2)`. Three digits of support only; I did not derive the scalar integrand independently beyond the standard
  `1/(E-i nu) + 1/(E+i nu) = 2E/(E^2+nu^2)` and I did not reproduce the analytic -0.0758907. The scalar side has no mu-dependence at this order.
- **17 CHECKED (D).** `v_psi - v_phi = V - (A-B)/2 = -0.011675 + 0.03795 = +0.02627(10) g^2` in **both** walker orders (the note: 0.0263 and 0.0284).

## 6. What is NEW, what is not

- Not new: the formulas, the mu >= 1/8 values, -0.011675, -0.0759, +0.0263 (all reproduced from the note), the collinear structure.
- New (scoped to this supplied comparator and this formula): (a) exact continuum identity `delta E = g^2 P/(48 pi^2)` at mu = 0 for all P and
  the vanishing massless shell density for q > P (steps 4-5); (b) the mu>0 closed form and the equality of both orders in the continuum
  (step 6); (c) lattice numerics showing the equality of both orders at -0.0116752(1) with error control (steps 9-13); (d) a defect: the note's
  separate zero-mass value and +0.0284 are not reproduced, and are exactly what one gets by counting the g^2/(48 pi^2) term twice (steps 15).
- Not claimed: any observational tuning bound (the gap depends on the regulator: the note's own lambda-universality test moves it 5-12%); any
  statement for the full theory, higher order in g, gauge/gravity members, or the hypercubic-tick surface.

## 7. Remaining obligations

- **18.** Step 14 (prove the lattice IR identity). Finite-volume ordering: on a box of side L, p is quantised (>= 2pi/L), so "p -> 0 first" and
  "L -> infinity" interplay with mu L; untreated.
- **19.** Scalar A-B certified beyond three digits and its analytic evaluation; the claim that no mu-dependence enters at O(g^2).
- **20.** Uniformity over `p` direction for the lattice (only p along an axis used; cubic symmetry makes the first-order coefficient isotropic,
  proved by symmetry of rank-2 cubic tensors, not rechecked numerically).
- **21. Chiral-carrier half NOT attempted:** the note's `W3 = 0` proof (K-theory step), the range-two truncation certificate (sampled bounds
  are not uniform certificates), heating of an interacting Floquet tick, sixteen-state necessity, and interacting mirror removal each need
  their own proof. I read the handedness note in full but produced no check of it; the note's T2 argument (SK_1 = 0 for Laurent polynomial
  rings, homotopy invariance of W3) looks standard to me but I did not verify it here (reading only).
- **22.** Workflow items for the supervisor: no commit/run_probe/claim.py performed; same-family only; needs cross-family confirmation before
  any status change.
