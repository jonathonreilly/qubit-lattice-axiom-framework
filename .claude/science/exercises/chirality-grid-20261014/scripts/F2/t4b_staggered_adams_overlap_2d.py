"""T4 (pre-registered in ../PREREG.md): one fermion component per site (staggered, qubit-compatible)
supports an exact Ginsparg-Wilson index.  Adams-type staggered overlap in 2D.
D_st psi(x) = 1/2 sum_mu eta_mu(x) [U_mu(x) psi(x+mu) - U_mu(x-mu)^dag psi(x-mu)],  eta_1 = 1, eta_2 = (-1)^x1.
C_mu = (V_mu + V_mu^dag)/2 (gauge-covariant symmetric shift), Gamma5 = eta5 (C1C2 + C2C1)/2,
Gamma55 = eps Gamma5.  D_A = D_st + r (1 - Gamma55).  H = eps (D_A - m).  index = -(1/2) Tr sign(H).
"""
import numpy as np
import itertools


def links(L, n):
    U1 = np.ones((L, L), complex)
    U2 = np.ones((L, L), complex)
    for x in range(L):
        for y in range(L):
            U2[x, y] = np.exp(2j * np.pi * n * x / L**2)
    for y in range(L):
        U1[L - 1, y] = np.exp(-2j * np.pi * n * y / L)
    return U1, U2


def build(L, n, eta5_choice, phase=1.0):
    U1, U2 = links(L, n)
    N = L * L
    idx = lambda x, y: (x % L) * L + (y % L)
    V = [np.zeros((N, N), complex), np.zeros((N, N), complex)]  # (V_mu psi)(x) = U_mu(x) psi(x+mu)
    for x in range(L):
        for y in range(L):
            V[0][idx(x, y), idx(x + 1, y)] = U1[x, y]
            V[1][idx(x, y), idx(x, y + 1)] = U2[x, y]
    eta = [np.ones(N), np.array([(-1) ** x for x in range(L) for y in range(L)], float)]
    eps = np.array([(-1) ** (x + y) for x in range(L) for y in range(L)], float)
    Dst = sum(0.5 * np.diag(eta[mu]) @ (V[mu] - V[mu].conj().T) for mu in range(2))
    C = [0.5 * (V[mu] + V[mu].conj().T) for mu in range(2)]
    e5 = {"1": np.ones(N),
          "x1": np.array([(-1) ** x for x in range(L) for y in range(L)], float),
          "x2": np.array([(-1) ** y for x in range(L) for y in range(L)], float),
          "x1x2": eps.copy()}[eta5_choice]
    G5 = phase * np.diag(e5) @ (0.5 * (C[0] @ C[1] + C[1] @ C[0]))
    G55 = np.diag(eps) @ G5
    return Dst, G55, np.diag(eps)


def free_check(L=8):
    out = {}
    for ch in [(c, p) for p in (1.0, 1j) for c in ("1", "x1", "x2", "x1x2")]:
        Dst, G55, E = build(L, 0, ch[0], ch[1])
        herm = np.allclose(G55, G55.conj().T)
        comm_eps = np.allclose(G55 @ E, E @ G55)
        # zero modes of free D_st
        w, v = np.linalg.eigh(1j * Dst)  # i D_st hermitian
        zm = v[:, np.abs(w) < 1e-10]
        g = zm.conj().T @ G55 @ zm
        gev = np.sort(np.linalg.eigvalsh(0.5 * (g + g.conj().T))) if zm.shape[1] else []
        comm_D = np.linalg.norm(G55 @ Dst - Dst @ G55)
        out[ch] = (herm, comm_eps, zm.shape[1], np.round(gev, 6), comm_D)
    return out


if __name__ == "__main__":
    fc = free_check()
    good = None
    for ch, (herm, ce, nz, gev, cD) in fc.items():
        ok = herm and ce and nz == 4 and np.allclose(sorted(gev), [-1, -1, 1, 1], atol=1e-6) and cD < 1e-10
        print(f"eta5={ch[0]:5s} phase={ch[1]} hermitian={herm} [G55,eps]=0:{ce} #zero modes={nz} G55 on zero modes={gev} "
              f"||[G55,Dst]||={cD:.3e}  -> {'OK' if ok else 'no'}")
        if ok and good is None:
            good = ch
    if good is None:
        print("T4b: NOT RUN (no eta5 choice passes the free-field check)")
        raise SystemExit
    print("using eta5 =", good)
    r = 1.0
    res = {}
    for m in (0.3, 0.6, 1.0, 1.4):
        row = []
        for L in (8, 12):
            for n in (1, 2, 3):
                Dst, G55, E = build(L, n, good[0], good[1])
                DA = Dst + r * (np.eye(L * L) - G55)
                H = E @ (DA - m * np.eye(L * L))
                assert np.allclose(H, H.conj().T, atol=1e-12)
                ev = np.linalg.eigvalsh(H)
                ind = -0.5 * np.sum(np.sign(ev))
                row.append((L, n, ind, np.min(np.abs(ev))))
        res[m] = row
        print(f"m={m}: " + "  ".join(f"L{L}n{n}:{ind:+.0f}(gap {g:.2e})" for L, n, ind, g in row))
    passed = False
    for m, row in res.items():
        ratios = {round(ind) / n for L, n, ind, g in row}
        ints = all(abs(ind - round(ind)) < 1e-6 for L, n, ind, g in row)
        if ints and len(ratios) == 1 and list(ratios)[0] in (1.0, -1.0):
            passed = True
            print(f"  m={m}: index = {list(ratios)[0]:+.0f} * n for all L, n")
    print("T4b verdict:", "PASS" if passed else "FAIL")
