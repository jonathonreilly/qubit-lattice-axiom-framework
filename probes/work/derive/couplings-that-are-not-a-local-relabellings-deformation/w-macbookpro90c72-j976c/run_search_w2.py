#!/usr/bin/env python3
"""Window-2 nearest-neighbour search with the comparison against the on-site-generator family (executed, floating point)."""
import numpy as np
import search_exact_current as S

unk, Z = S.main(2, 'nn')
F = S.onsite_family(unk, 2)
sv = np.linalg.svd(F, compute_uv=False)
rankF = int(np.sum(sv > 1e-9 * sv[0]))
coef, *_ = np.linalg.lstsq(Z, F, rcond=None)
resid = np.linalg.norm(Z @ coef - F) / np.linalg.norm(F)
v = S.u1_vector(unk)
cu, *_ = np.linalg.lstsq(Z, v, rcond=None)
print(f"on-site generator family i[H, zeta]: rank {rankF}; its residual outside the solution space {resid:.1e}")
print(f"solution space equals the family: {Z.shape[1] == rankF and resid < 1e-9}")
print('U(1) residual', np.linalg.norm(Z @ cu - v) / np.linalg.norm(v))
