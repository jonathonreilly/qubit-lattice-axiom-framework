# Block 80 — control and findings (2026-09-22)

1. Disjoint machinery (`specs/supervisor_control_block80_interacting_sea.py`): sparse many-record diagonalisation on rings and 2D tori; the exact runner has two records and exact quadratic forms.
2. **A wrong real part caught by the runner (supervisor).** The site-resolved density was first computed as `2UᵀP_xAV` (right for the total, wrong per site); the derivative failed at every site while the sums agreed; the real part `UᵀP_xAV − VᵀP_xAU` per slot fixed it. The factor between `φ_x∂/∂φ_x` and `∂/∂u_x` was caught by the weight-one check.
3. **The 1D comparison discarded (supervisor).** The 1D free sea has no gradient part at the longest mode, so 1D says nothing about 3D's `κ`; the 2D free sea's gradient part (`+0.017–0.023`) was checked against 3D's (`+0.024`) before the interacting sign was read.
4. **The jammed filling named (supervisor).** Under exclusion the free-branch filling is a record on nearly every site; the sign reversal is that jam's; half filling has the free sea's sign — both are reported.
5. Finding folded: the note first had no `## Theorem T3`, so the injection mutation could not bite; T2(c) became T3.
6. Control detail: the `5×3` torus (823k states at half filling) was dropped from the control for time; the strain section (W3) was added after the first pipeline pass, which the pipeline rejected ("classifier inputs changed"), and the passes were re-run.
