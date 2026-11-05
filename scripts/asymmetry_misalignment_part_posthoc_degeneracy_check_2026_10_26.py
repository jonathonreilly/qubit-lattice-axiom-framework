# diagnostic only: re-examine the sol_D post-hoc claim "median |J|/Jmax 0.2-0.5" (generic cell-periodic on-site vertex)
import numpy as np
src = __import__('pathlib').Path(__file__).with_name('asymmetry_misalignment_part_posthoc_generic_vertex_2026_10_26.py').read_text().split("t = lambda Y, dY")[0]
exec(src)
for i, ((Vu, Pu), (Vd, Pd)) in enumerate(DRv[:6]):
    Yu, Yd = yuk_v(sl, Vu, 1), yuk_v(sl, Vd, 5)
    su = np.linalg.svd(Yu, compute_uv=False); sd = np.linalg.svd(Yd, compute_uv=False)
    Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T
    inv = abs(np.linalg.det(Hu @ Hd - Hd @ Hu)) / (np.linalg.norm(Hu) ** 3 * np.linalg.norm(Hd) ** 3)
    print(i, "sv_u/sv0", np.round(su / su[0], 8), "sv_d/sv0", np.round(sd / sd[0], 8), f"commutator invariant {inv:.1e}  jarlskog() {jarlskog(Yu, Yd):.2f}")
