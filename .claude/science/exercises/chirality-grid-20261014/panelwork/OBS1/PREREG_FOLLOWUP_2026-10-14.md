# OBS-1 dated follow-ups to PREREG.md (PREREG.md itself is unedited)

## 2026-10-14 ~21:33Z (written after the first registered runs; before the runs listed here)

1. **Registered result that forced the follow-up.** The registered quantity (an on-site, cubic-singlet corner mass) has K = C_par - C_perp = 0 to 1e-14 at Delta = 0 and K = 1.5e-3 e^2 at Delta = 0.5 (r1_loop.out:9-99). The zero is a symmetry: the free walker, the NN photon, on-site masses and diagonal SF strain are all invariant under the staggered reflection R_a: x_a -> -x_a with sign (-1)^{x_a} (k_a -> pi - k_a), which maps hw1 corner e_a to the origin. So the registered quantity does not see flavour structure at all. What CKM forces lives in the flavour-breaking mass operators. Added (not pre-registered; same machinery, same grids/controls):
   - r1_leak.py `leak`: one-loop leak of a corner-selective mass symbol mu (1 - cos k_z)/2 (heavy at hw1 corner e_z) into the light corner e_x, and its strain derivatives;
   - r1_leak.py `own`: the same symbol at its own corner;
   - r1_offdiag.py: off-diagonal generation mass from an on-site condensate at lattice momentum (pi, pi, 0) (pairs corners e_x, e_y);
   - all at N = 24/32/48/64, m0 = 0.1 (and 0.05), Delta = 0.5 (and 0).
   - sizes.py: realistic mass matrices for branches A, B, B' with two realisations of the diagonal entries ("trace": on-site part tr/3 plus corner-selective deviations; "selective": all diagonal mass from corner-selective symbols).
   The reading rules of PREREG.md are unchanged and are applied to these numbers.
2. **Correction to the registered SME residual formula.** "y^2/16pi^2 x K_v" double-counts the loop factor: K_v is already a full lattice loop integral (per e^2). sizes.py prints both the registered and the corrected (y^2 x K_v) value; the report uses the corrected one, labelled suggested.
3. **R2 operator table.** A mislabelled dim-7 entry (it had B-L = 0) was replaced by the B-L-violating d^c d^c d^c L H^dag before the final sizes.py run.
