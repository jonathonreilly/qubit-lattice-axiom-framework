"""T1 (pre-registered in ../PREREG.md): 2D overlap index in U(1) flux vs Chern number of the
free eps-bundle.  Overlap D = 1 + g5 sign(H_W), H_W = g5 D_W.  index = -(1/2) Tr sign(H_W).
Wilson kernel: D_W(p) = -m + r*sum(1-cos p) + i gamma.sin p.
"""
import numpy as np

s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex)
g = [s1, s2]
g5 = s3
I2 = np.eye(2)


def links(L, n):
    """uniform flux n on LxL torus; returns U1[x,y], U2[x,y] (link from (x,y) in dir mu)."""
    U1 = np.ones((L, L), complex)
    U2 = np.ones((L, L), complex)
    for x in range(L):
        for y in range(L):
            U2[x, y] = np.exp(2j * np.pi * n * x / L**2)
    for y in range(L):
        U1[L - 1, y] = np.exp(-2j * np.pi * n * y / L)
    return U1, U2


def plaquettes(U1, U2):
    L = U1.shape[0]
    P = np.zeros((L, L), complex)
    for x in range(L):
        for y in range(L):
            P[x, y] = U1[x, y] * U2[(x + 1) % L, y] * np.conj(U1[x, (y + 1) % L]) * np.conj(U2[x, y])
    return P


def wilson_dirac(L, n, m, r):
    U1, U2 = links(L, n)
    N = 2 * L * L
    D = np.zeros((N, N), complex)
    idx = lambda x, y: 2 * ((x % L) * L + (y % L))
    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            D[i:i + 2, i:i + 2] += (2 * r - m) * I2
            for mu, (dx, dy), U in ((0, (1, 0), U1), (1, (0, 1), U2)):
                j = idx(x + dx, y + dy)
                u = U[x, y]
                # forward hop: -(1/2)(r - gamma) U psi(x+mu)
                D[i:i + 2, j:j + 2] += -0.5 * (r * I2 - g[mu]) * u
                # backward hop: -(1/2)(r + gamma) U^dag(x) psi(x) from site x+mu to x
                D[j:j + 2, i:i + 2] += -0.5 * (r * I2 + g[mu]) * np.conj(u)
    return D


def overlap_index(L, n, m, r):
    D = wilson_dirac(L, n, m, r)
    G5 = np.kron(np.eye(L * L), g5)
    H = G5 @ D
    assert np.allclose(H, H.conj().T, atol=1e-12)
    ev = np.linalg.eigvalsh(H)
    gap = np.min(np.abs(ev))
    idx = -0.5 * np.sum(np.sign(ev))
    return idx, gap


def chern_free(m, r, Nk=48):
    ks = 2 * np.pi * np.arange(Nk) / Nk
    vec = np.zeros((Nk, Nk, 2), complex)
    for a, kx in enumerate(ks):
        for b, ky in enumerate(ks):
            Dp = (-m + r * (2 - np.cos(kx) - np.cos(ky))) * I2 + 1j * (np.sin(kx) * s1 + np.sin(ky) * s2)
            H = g5 @ Dp
            w, v = np.linalg.eigh(H)
            vec[a, b] = v[:, 0]  # negative-eigenvalue band of H_W (= eps = -1 band)
    F = 0.0
    for a in range(Nk):
        for b in range(Nk):
            u1 = np.vdot(vec[a, b], vec[(a + 1) % Nk, b])
            u2 = np.vdot(vec[(a + 1) % Nk, b], vec[(a + 1) % Nk, (b + 1) % Nk])
            u3 = np.vdot(vec[(a + 1) % Nk, (b + 1) % Nk], vec[a, (b + 1) % Nk])
            u4 = np.vdot(vec[a, (b + 1) % Nk], vec[a, b])
            F += np.angle(u1 * u2 * u3 * u4)
    return F / (2 * np.pi)


if __name__ == "__main__":
    # sanity: plaquettes uniform
    for L in (8, 10):
        for n in (1, 2, 3):
            P = plaquettes(*links(L, n))
            ph = np.angle(P)
            assert np.allclose(ph, 2 * np.pi * n / L**2, atol=1e-12), (L, n, ph.min(), ph.max())
    print("plaquette check: uniform flux 2*pi*n/L^2 on all plaquettes, OK")
    masses = [-0.5, 0.5, 1.0, 1.5, 2.5, 3.0, 3.5, 4.5]
    rows = []
    signs = set()
    allpass = True
    for r in (1.0, 0.6):
        for m in masses:
            c1 = chern_free(m, r)
            c1r = int(round(c1))
            for L in (8, 10):
                for n in (1, 2, 3):
                    ind, gap = overlap_index(L, n, m, r)
                    ok_int = abs(ind - round(ind)) < 1e-6
                    rows.append((r, m, c1, L, n, ind, gap))
                    if c1r != 0:
                        s = round(ind) / (c1r * n)
                        signs.add(s)
                        if s not in (1.0, -1.0):
                            allpass = False
                    else:
                        if round(ind) != 0:
                            allpass = False
                    if not ok_int:
                        allpass = False
            print(f"r={r} m={m:5.2f} c1(free eps band)={c1:+.4f}  "
                  + "  ".join(f"L{L}n{n}:{ind:+.0f}(gap {gap:.2e})" for (rr, mm, _, L, n, ind, gap) in rows[-6:]))
    print("global signs seen:", signs)
    verdict = "PASS" if (allpass and len(signs) == 1) else "FAIL"
    print("T1 verdict:", verdict)
