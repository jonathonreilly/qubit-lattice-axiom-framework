# CLS-1 PREREG follow-ups (dated; PREREG.md unchanged)

## F1, 15:10Z (after runs labels/light/theta/count/bounds; before cls1_loop.py)
- P-b (on-site spin density sigma_{a(K)} cos(K.x)) failed the cubic-covariance audit (defect 0.6, labels.out); it is not an allowed cubic-symmetric class-S term and is dropped from the readings. P-a, P-c, P-d pass.
- Theta measurement: the first model-B "direct-diag" theta in light.out mixed the degenerate psi zero modes with decoupled chi zero modes (chi weight up to 2.2, visible in the output). Replaced by a degeneracy-safe measurement (psi-span of the zero eigenspace) in cls1_theta.py; light.out's SVD column is unaffected. Recorded, not hidden.
- Added after PREREG: (a) the literal task model (hw1<->hw3 hopping only) in cls1_theta.py; (b) cls1_count.py (counting the cubic-invariant light-sector structures, exact translations vs BCC); first run hit the 0.4 GB cap (full SVD U matrix 5184^2), rerun with economy SVD (count_run1_memcap.out kept); (c) cls1_bounds.py arithmetic; (d) cls1_loop.py, a one-loop toy to test whether the BCC-only c-type structures are regenerated when the tree-level P-c/P-d are set to zero (R4 asks for this).
- Bounds fetched (ar5iv of arXiv:1709.03434, Table 1): IceCube a(3)_mutau < 2.9e-24 GeV, c(4)_mutau < 3.9e-28 (99% CL). Others recalled.
- Interpretation note, not a reading change: the registered primary proxy (model A, static site partner) lifts the light zero modes at Delta*sigma_light for every kappa != 0. The reason is that the free partner field has unpaired zero modes at the light corners (Nielsen-Ninomiya on the extended free system; the same vector-like modes X2 T5 reported). The registered threshold rule is evaluated with model B (partner only on channels above threshold). Both are reported.

## F2, 15:18Z (all runs finished)
- Added after F1: cls1_loop2.py (quadratic-form check of the one-loop off-diagonal coefficient), cls1_loop3.py (complex y0 = y1 e^{i phi}), cls1_loop4.py (speed spread from the one-loop off-diagonal part), cls1_index.py (sphere Chern numbers under random BCC bilinears). cls1_archive.npz collects the arrays.
- cls1_index.py result to keep in scope: random non-symmetric BCC bilinears of strength >= 0.3 move nodes out of a radius-0.6 sphere around P; this is node motion, not a measured gap. Global node annihilation for O(1) bilinears without Theta was not tested.
- Supervisor's CLS1 SUPERVISOR_OWN_THREAD.md read only now, after all results.
- NT-3-style ED proxy (registered "only if time"): not run. Reason: the reading is fixed by (iii); a 1D marginal-coupling ED would not change it.
- Another agent's python (runner.py, ~557 MB) is running on the machine; it is not mine and was not touched.
