# J:derive:review-20261014-hard-support-overlap-positivity:a1 -- attempt

Same-family (Claude Sonnet 5.5), unrefereed. Nothing here is accepted science. Labels: PROVED (argument given here), CHECKED (executed by `check.py`, 30 PASS / 0 FAIL, 117 s, 421 MB peak), ASSUMED (premise), READING (interpretation).

I read in full `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines) on current main (a77a3449c9) before choosing premises.

## Plain-language summary

The earlier K2c work reports that a gauged overlap fermion with a "hard support" gauge weight fails a positivity test. I regenerated its torus pool and replicated the number with K2c's own independent builder (replication, not new). I could not make the fermion claim rigorous: there is no a priori error bound for the 48x48 overlap determinant integral, and I did not find one.

What I could advance exactly is the pure-gauge part of the same hard measure, with no fermions. For a spatial torus of 3 x 2 sites in 2+1 dimensions the hard-support reflection kernel has a negative Fourier coefficient, computed in closed form. That gives a negative eigenvalue on a small pool of flat configurations (13 points suffice for open time; 16 points give lambda_min/lambda_max = -1.6e-2). The same pool with a Wilson-type weight, or with an even torus length, shows no violation. The result is about odd torus size. Whether the hard measure is reflection-positive on even tori or in infinite volume is still open.

## Setting and premises

- ASSUMED P1 (lane-supplied, not axiom content): pure U(1) gauge fields, beta_g = 0, Haar links, weight prod over plaquettes of f(theta) = 1(|theta| < delta), one reflection plane between time slices, link reflection (spatial links keep orientation), Theta F = conj(F o reflection). This is the K2c/X3 comparator (`PREREG.md:16`). The axioms supply no gauge measure, no dynamics and no time metric (`MINIMAL_AXIOMS_2026-06-29.md:55-73`, `:114-123`); physical sites stay Z^3 with M_2(C). Carrier U(1), the plane and the weight are comparators.
- ASSUMED P2: delta = 0.6, as in K2c (`PREREG.md:16`). Mismatch to note: X3's own admissible-set runs used delta = 0.3 and 0.5 and Lx = 4 (`COMBO_REPORT.md:177`, `:301`). So "X3's measure at delta = 0.6" is K2c's choice. Step 9 shows the sign result for 0.3, 0.5, 0.6, 0.9.
- ASSUMED P3: spatial cross-section is the periodic torus Z_3 x Z_2 (Lx = 3, Ly = 2; the doubled y-links are a degeneracy like K2's Lx = 2) and a second one, Z_3 x Z_3. Open time (any even number of slices, minimum 2) and periodic time are both treated.

## Steps

1. PROVED (source identity). The five named objects match their stated sha256 at `dd7d358c6f6b0fd049b46962970397dbdc7d2e1f` (also CHECKED, S0). The run-time scripts `lat2d.py`, `k2b_lib.py`, `k2c_lib.py`, `k2c_search.py` are present in that tree; their hashes are in `RECOVERY_STATUS.json`. No `.npz` pool exists in the tree.

2. CHECKED (recovery, REPLICATION not new). K2c's torus pool `wgsearch hard torus Lt12 seed 4412 K24` regenerates deterministically with the unchanged scripts (`python3 k2c_search.py wgsearch torus 6 24 4412 hard O`, 261 s). The trajectory matches the recorded `V2_torus_Lt12_wgsearch_hard.out` line by line to printed digits, final lambda_min = -1.4728e-4. The array hash is pinned in `check.py` S8 and `RECOVERY_STATUS.json`. The source V6 builder, run on the regenerated pool, gives O lambda_min = -1.47281e-4 and Wilson +8.8e-15 (S8). K2c's E remains an a-posteriori estimate (`K2c_REPORT.md:132`). Other pools (open Lt 12 and 20, torus Lt 16, Fejer references) were not regenerated.

3. PROVED (reflection algebra, abelian). Let G be the cross-section graph, u_s the crossing temporal links, (A, B) the slice-1 links of the two half-lattices. A crossing plaquette on spatial link l = (s -> s') has angle (A_b - A_a)_l + u_s - u_s'. Hence the crossing kernel is
   kappa(a) = volume of {u in T^V : |a_l + (du)_l| < delta for every l}, with Z(a,b) = kappa(A_b - A_a) (even in a). Other plaquettes factor into positive weights of each half.

4. PROVED (pool lemma). If pool points A_1..A_k have every half-lattice plaquette strictly inside (-delta, delta), the half weights are positive and continuous near them and Z is continuous. Bump functions F_i around A_i then give <Theta F F> -> sum c_i* c_j w_i w_j Z(A_i, A_j) times neighbourhood volumes. A negative eigenvalue of the finite matrix Z therefore gives a gauge-invariant F with <Theta F F> < 0. The same lemma covers K2c's "point configuration" kernels.

5. PROVED (support restriction does not decouple, reading of K2c (c)). K2c's criterion "some closed-current coefficient c_6 c_3^6 ... is negative" (`K2c_REPORT.md:105-108`) is a statement about functions on the full torus of slice links. Test functions are supported on slice configurations whose spatial plaquettes are admissible, so it does not by itself give a violation (K2c says so, `:107`). Step 6 handles this by choosing a pool of flat connections, which are interior points.

6. PROVED (uniform-holonomy pool, Z_3 x Z_2). Pool A_Delta: every x-link angle Delta/3, every y-link 0. It is flat (all slice plaquettes 0), so Step 4 applies. For Lx = 3 and delta < pi/3 all lifts are unique, and substituting e_x = Delta/3 + u_{x+1,0} - u_{x,0}, d_x = u_{x,1} - u_{x,0} gives
   kappa(Delta) = sum_w C(w) e^{iw Delta}, C(w) = integral over d in (-delta, delta)^3 of prod_x (2/w) sin(w(delta - |d_{x+1} - d_x|/2)), indices cyclic,
   with C(0) = 304 delta^6/15. In operator form C(w) = Tr T_w^3 for the Hermitian kernel T_w(d, d') = (2/w) sin(w(delta - |d' - d|/2)) on (-delta, delta); the Lx-site analogue is Tr T_w^Lx.

7. CHECKED (closed form, MC from the original definition). Sympy integration over the six orderings gives, with x = delta w,
   C(w) = 4 e^{-3ix} [ -2i x^3 e^{4ix} + 2i x^3 e^{2ix} - 6x^2 e^{4ix} - 6x^2 e^{2ix} - 3i x e^{6ix} - 9i x e^{4ix} + 9i x e^{2ix} + 3i x + 3e^{6ix} - 3e^{4ix} - 3e^{2ix} + 3 ] / w^6.
   Re-derived independently inside `check.py` (S2) and matched to a Nystrom trace of T_w (S3, 5e-7). A Monte-Carlo estimate of kappa(Delta) taken directly from the 12-indicator definition on T^6 (no reduction used) agrees with the series within 4 sigma at Delta = 0 and 1 (S4: 4.785 +- 0.011 vs 4.788; 0.565 +- 0.002 vs 0.566). Values: C(7) = -7.16e-3, C(8) = -8.01e-3, C(9) = -6.08e-3, C(10) = -2.86e-3.

8. CHECKED with a rigorous tail (floating-point rounding is not interval-certified; margin about 1e6). |C(w)| <= B(w) = 4(4x^3 + 12x^2 + 24x + 12)/w^6 term by term from the closed form, so truncating the series at w = 20000 changes kappa by at most tau = 8.6e-9. The pool matrix K_ab = kappa(Delta_a - Delta_b), Delta_a = 2 pi a/N, is circulant with eigenvalues lambda_j = N sum_k C(j + kN). Results (S5):
   - open time, smallest N with lambda_min < -10 N tau: N = 13 (lambda_min/lambda_max = -7.3e-3);
   - N = 16: lambda_min = -0.2494 at j = 8, lambda_min/lambda_max = -1.65e-2; the character e^{-i 8 Delta} has Rayleigh quotient -0.2494;
   - N = 64: lambda_min = -0.5122, relative -8.5e-3, equal to the aliasing sum.
   Via Step 4 this is a gauge-invariant F with <Theta F F> < 0 for the hard pure-gauge measure on the 3 x 2 torus, open time, any even number of time slices >= 2. Label: CHECKED (computer-assisted); I do not call it a theorem.
   - periodic time (two crossing planes, kernel kappa^2): N = 32 gives -0.846 (relative -8.0e-3), N = 64 gives -1.74; N = 16 is positive (+0.083). CHECKED.

9. CHECKED (robustness and controls on the same pool).
   - delta sweep: min over w of C(w; delta) is negative for delta = 0.3, 0.5, 0.6, 0.9 (S6d), all with 3 delta < pi. So the sign is not specific to 0.6.
   - Wilson-type positive-type weight exp(cos theta): all Fourier coefficients >= 0 (w = 0..16) and the pool kernel is PSD (S6c).
   - even Lx = 2 and 4 with Ly = 2: Tr T_w^Lx >= 0 for w = 0..40, because T_w is Hermitian (sum of even powers). PROVED for the uniform pool at every w; so this pool cannot detect even sizes (S6a).
   - 2D odd ring (Ly = 1, Lx = 3) reproduces the recorded lambda_min = -3.99e-3, min/max = -8.9e-3 (`K2c_REPORT.md:99`), computed here independently from c_n^3 (S6b).
   - Z_3 x Z_3 (no doubled links), grid transfer trace, not certified: coefficient negative at w = 8, 9, 10 (about -2.4e-3, -2.3e-3, -1.4e-3, stable to 5% between two resolutions, S7).

10. READING. The mechanism is the 2D odd-ring mechanism of `K2c_REPORT.md:93-96` (odd noncontractible loop, c_6 < 0), carried into 2+1 dimensions with slice-plaquette support enforced. In the pure-gauge sector the failure needs odd size; it is not a thin-ring accident, because the transverse row coupling does not remove it. Whether this matters for the physical OS programme depends on whether spatial sizes may be restricted to even values; that is a choice outside the axioms.

11. FIRST UNRESOLVED STEP.
    (a) Fermion overlap, torus and open: a rigorous quadrature bound for the 48x48 overlap-determinant kernel integral. A crude bound through |det M| <= ||M||^N and a Bernstein-ellipse radius limited by the spectral gap (0.3 for the torus pool) would demand hundreds of nodes per variable; this is an estimate I did not run (suggested). Until a bound exists, K2c's torus and open negatives rest on a-posteriori convergence plus two builders, both ours.
    (b) Pure gauge: positivity of the hard-support kernel on EVEN periodic cross-sections and in infinite spatial volume (the local-current mechanism c_6 c_3^6). Concrete object: the kernel kappa_G(A_b - A_a) restricted to admissible slice configurations S (a Krein-type positivity question on a restricted domain), for G = Z_2 x Z_2 and Z_4 x Z_2; first artifact: exact polytope-volume kernel plus a pool search with a certified error. The uniform-holonomy pool used here is provably blind to even sizes (Step 9).
    Not tested: 3+1D, non-abelian groups, the chiral measure, domain-wall controls (only replicated Wilson-fermion control on the regenerated torus pool).

## What is new, and what is not

Not new: the K2c/X3 numbers, the regenerated torus pool and its replication (Step 2), the 2D odd-ring failure (Step 9, S6b), the character-expansion criterion, the cusp-masking explanation.
New (same-family, unrefereed): Steps 6-8, the closed-form hard-support Fourier coefficient on a 2+1D cross-section and the resulting certified-tail negative eigenvalue for open and periodic time with slice-plaquette support enforced, the delta sweep, and the proof that the uniform pool is blind to even sizes. This resolves K2c's "suggested, not tested" (`K2c_REPORT.md:105-108`, `:287`) for odd cross-sections only. It does not decide the hard-support question for the fermion overlap, for even sizes, or for 3+1D.

## Prior-art and claim search

Read: the five source objects in full; K2c scripts. Searched current main `docs/` and `.claude/` for "hard indicator", "hard-support", "reflection positivity" (no note on pure-gauge hard-support kernels found); the probes view (`probes/review-science-20261014.md`, `probes/tasks/`, `probes/work/derive`) shows the catalog entry only and no earlier attempt or claim file for this task id. `gh pr list` returned nothing usable in this environment, so open-PR overlap is not excluded. No referee report for K2c arrived in what I could see.

## Files

`check.py`, `RECOVERY_STATUS.json`, `pool_K2c_wgsearch_hard_O_torus_Lt12_seed4412.npz` (regenerated pool), `src/` (extracted source objects, run-time scripts, regeneration output), `work/` (scratch).
