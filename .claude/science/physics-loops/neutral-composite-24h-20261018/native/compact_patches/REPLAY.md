# Replay

Run from this folder. These scripts generate synthetic model states, not observational data. Ordinary Python needs NumPy, SciPy and numba. Tensor scripts use the existing `/private/tmp/neutral-tensor-venv/bin/python` with quimb. Set OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=4 for comparable resource use. No binary input from another campaign is required.

1. Tensor Python: `mpo_check.py`, `moment_control.py`, `fusion_control.py`, `volume_algebra.py`.
2. Ordinary Python: `exact_sheet.py`, `exact_sheet_deep.py`, `sheet_fixed_characters.py`.
3. Tensor Python: `ground_states.py`, then `refine_states.py`; `volume_ground.py` independently.
4. Tensor Python: `patch_response.py --bond 32`, `patch_response.py --bond 128`, `boundary_response.py --bond 32`, `volume_response.py --bond 32`.
5. Ordinary Python: `dressing_checks.py` and `check_results.py`.

Scripts write JSON beside their source and tensor checkpoints with `.pkl` extension. The checkpoints are local disposable numerical artifacts, excluded from git and identified by the final manifest. `native_mpo.py` contains the full 3D Hamiltonian. Exact sheet scripts use the tracked parent `compass_sector_basis.py` and `compass_sector_solve.py`. One-layer controls omit x bonds by geometry, not as an approximation to the 3D result. No elapsed-time or convergence flag substitutes for the reported residuals.

Full 3D exact controls: ordinary Python `exact_periodic_cube.py`, then `exact_cube_poles.py` and `pole_analysis.py`. These use the unchanged tracked CSS code plus the 27 native periodic wrap bonds. Peak eigensolver memory is substantial; these are small-volume controls, not substitutes for large-box convergence.
