"""T-D: walker + i eps F, f = s(s^2-1).  F6 route agent, 2026-10-14."""
import numpy as np, itertools
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex); sz = np.array([[1, 0], [0, -1]], complex)
for L in (4, 8):
    n = L ** 3
    def idx(x, y, z): return ((x % L) * L + (y % L)) * L + (z % L)
    def shift(d):
        T = np.zeros((n, n))
        for x, y, z in itertools.product(range(L), repeat=3):
            T[idx(x, y, z), idx(x + d[0], y + d[1], z + d[2])] = 1.0
        return T
    Tx, Ty, Tz = shift((1, 0, 0)), shift((0, 1, 0)), shift((0, 0, 1))
    S = sum((T + T.T) / 2 for T in (Tx, Ty, Tz))          # symbol s(k) = sum cos k_a
    Fs = S @ (S @ S - np.eye(n))                            # symbol f = s(s^2-1)
    eps_s = np.diag([(-1.0) ** (x + y + z) for x, y, z in itertools.product(range(L), repeat=3)])
    H = sum(np.kron((T - T.T) / 2j, s) for T, s in ((Tx, sx), (Ty, sy), (Tz, sz)))
    M = np.kron(1j * eps_s @ Fs, np.eye(2))
    Td = np.kron(Tx @ Ty @ Tz, np.eye(2))
    print(f"L={L}: |M-M^+|={np.abs(M - M.conj().T).max():.1e}  |{{H,M}}|={np.abs(H @ M + M @ H).max():.1e}  max range of F (sites)=3")
    E, V = np.linalg.eigh(H + M)
    zero = np.abs(E) < 1e-9
    print(f"L={L}: zero modes of H+M = {zero.sum()} (bare walker: {np.sum(np.abs(np.linalg.eigvalsh(H)) < 1e-9)})")
    Z = V[:, zero]
    # momentum content of zero modes: project onto corner plane waves
    for c in itertools.product((0, 1), repeat=3):
        if L % 2: continue
        k = np.pi * np.array(c)
        pw = np.array([np.exp(1j * k @ np.array(r)) for r in itertools.product(range(L), repeat=3)]) / np.sqrt(n)
        P = np.kron(pw.reshape(-1, 1), np.eye(2))           # (2n, 2)
        w = np.linalg.norm(P.conj().T @ Z) ** 2
        if w > 1e-9:
            ZtdZ = (P.conj().T @ Td @ P)
            print(f"   corner {c} hw={sum(c)}: zero-mode weight {w:.3f}, T_d on corner = {np.real(ZtdZ[0,0]):+.0f}")
    nz = np.abs(E[~zero])
    print(f"L={L}: min |E| over non-zero modes = {nz.min():.4f}")
