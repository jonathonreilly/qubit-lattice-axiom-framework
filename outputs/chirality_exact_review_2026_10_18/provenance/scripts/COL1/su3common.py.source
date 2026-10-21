"""Shared SU(3) data for COL-1 scripts (no repository imports)."""
import numpy as np

def gellmann_halves():
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1] = -1j; l[1][1, 0] = 1j
    l[2][0, 0] = 1; l[2][1, 1] = -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2] = -1j; l[4][2, 0] = 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2] = -1j; l[6][2, 1] = 1j
    l[7][0, 0] = l[7][1, 1] = 1 / np.sqrt(3); l[7][2, 2] = -2 / np.sqrt(3)
    return l / 2

T = gellmann_halves()
Tbar = -np.conj(T)          # generators of the conjugate representation 3bar

def structure_constants():
    f = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            c_ = T[a] @ T[b] - T[b] @ T[a]
            for c in range(8):
                # [T^a,T^b] = i f^{abc} T^c, Tr(T^c T^d) = delta/2
                f[a, b, c] = np.real(np.trace(c_ @ T[c]) * 2 / 1j)
    return f

F = structure_constants()

def check_su3_relations(Gs, normfun, tol=1e-12):
    """Max deviation of [G^a,G^b] - i f^{abc} G^c over a,b."""
    worst = 0.0
    for a in range(8):
        for b in range(a + 1, 8):
            lhs = Gs[a] @ Gs[b] - Gs[b] @ Gs[a]
            rhs = sum(1j * F[a, b, c] * Gs[c] for c in range(8) if abs(F[a, b, c]) > 0)
            d = normfun(lhs - rhs)
            worst = max(worst, d)
    return worst
