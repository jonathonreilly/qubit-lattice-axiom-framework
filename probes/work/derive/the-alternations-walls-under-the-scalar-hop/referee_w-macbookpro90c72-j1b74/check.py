#!/usr/bin/env python3
"""Independent check: {h,c} = (D^2 - Ddag^2)/i, and it is nonzero for unequal hops."""
import numpy as np

D = np.zeros((3, 3), dtype=complex)
D[1, 0] = 1.0
D[2, 1] = 2.0
Dd = D.conj().T
h = (D - Dd) / (2j)
c = D + Dd
ac = h @ c + c @ h
rhs = (D @ D - Dd @ Dd) / 1j
ok = np.allclose(ac, rhs) and np.max(np.abs(rhs)) > 0
print(f"identity {np.allclose(ac, rhs)} nonzero {np.max(np.abs(rhs)) > 0}")
if ok:
    print(
        "HIT: confirmed - {h,c}=(D^2-Ddag^2)/i holds and is nonzero for unequal hop "
        "amplitudes, so the scalar hop's cross terms in H_a^2 do not cancel"
    )
    print(
        "SUMMARY: confirmed the square-expansion identity behind separability failing; "
        "the 128-dimensional rank census was not rebuilt here"
    )
else:
    print("SUMMARY: fails at the {h,c} identity")
