"""bb1 POST-HOC diagnostic (added after reading A2's FAIL; not a criterion): Z_col of a_S at T = 8 by c37's own code path
(level0_hats(want_x) complex64 + kernel float32 + colsums) against bb1's complex128 path."""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c37_kcurv as K37  # noqa: E402
import bb1_decay as B1  # noqa: E402

F = B1.build()
F1h, rh, xh, aph = K37.level0_hats(F, 8, 1.0, want_x=True)
del F1h, rh, xh
ka, _ = K37.kernel(aph)
print(f"c37 path (complex64 hats, float32 kernel): Z_row = {K37.rowsums(ka).max():.6f}, Z_col = {K37.colsums(ka).max():.6f}")
print(f"  same kernel, column sums accumulated in float64: {np.abs(ka).astype(np.float64).sum(axis=(0, 1, 2, 3, 4)).max():.6f}")
del ka
aS, aB, H1, _ = B1.hats(F, 8, cdt=np.complex128)
ka64, _ = K37.kernel(aS, np.float64)
print(f"bb1 path (complex128 hats, float64 kernel): Z_row = {K37.rowsums(ka64).max():.6f}, Z_col = {K37.colsums(ka64).max():.6f}")
ka32, _ = K37.kernel(aS.astype(np.complex64))
print(f"complex128 solves, hats cast to complex64, float32 kernel: Z_col = {K37.colsums(ka32).max():.6f}")
print("diag: post-hoc", flush=True)
