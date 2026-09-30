"""T24 test C: what do '8' and '16' count? Zero-mode census of four supplied kernels on periodic even tori.
Reported in Weyl-equivalents (2 zero-mode states per Weyl node)."""
import itertools
import json
import numpy as np

SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]


def shifts(L):
    N = L ** 3
    coords = np.array(list(itertools.product(range(L), repeat=3)))
    T = []
    for a in range(3):
        tgt = coords.copy(); tgt[:, a] = (tgt[:, a] + 1) % L
        perm = (tgt[:, 0] * L + tgt[:, 1]) * L + tgt[:, 2]
        M = np.zeros((N, N)); M[np.arange(N), perm] = 1.0     # (T psi)(c) = psi(c+e_a)
        T.append(M)
    return T, coords


def main():
    res = {}
    lines = []
    L = 4
    T, coords = shifts(L)
    N = L ** 3
    S = [(T[a] - T[a].T) / (2j) for a in range(3)]
    # 1. walker, 2 components
    H = sum(np.kron(SIG[a], S[a]) for a in range(3))
    ev = np.linalg.eigvalsh(H); n1 = int((np.abs(ev) < 1e-9).sum())
    res["walker_2comp_flow"] = n1
    lines.append(f"walker H = sigma.S (2 comp/site), L=4: zero modes {n1} -> {n1//2} Weyl nodes")
    # 2. Kawamoto-Smit one-mode staggered
    eta = [np.ones(N), np.array([(-1) ** c[0] for c in coords], float), np.array([(-1) ** (c[0] + c[1]) for c in coords], float)]
    D = sum(0.5 * (np.diag(eta[a]) @ T[a] - T[a].T @ np.diag(eta[a])) for a in range(3))   # anti-Hermitian check below
    # D_{x,x+mu} = eta_mu(x)/2 ; D_{x+mu,x} = -eta_mu(x)/2
    Dm = np.zeros((N, N))
    for a in range(3):
        for i in range(N):
            j = int(np.argmax(T[a][i]))
            Dm[i, j] += 0.5 * eta[a][i]
            Dm[j, i] -= 0.5 * eta[a][i]
    assert np.allclose(Dm, -Dm.T)
    ev = np.linalg.eigvalsh(1j * Dm); n2 = int((np.abs(ev) < 1e-9).sum())
    res["KS_one_mode"] = n2
    lines.append(f"Kawamoto-Smit staggered (1 component/site), L=4: zero modes {n2} -> {n2//2} Weyl-equivalents (= {n2//4} four-component Dirac)")
    # 3. naive Hamiltonian, 4-component alpha matrices
    al = [np.kron(SIG[0], SIG[a]) for a in range(3)]
    H4 = sum(np.kron(al[a], S[a]) for a in range(3))
    ev = np.linalg.eigvalsh(H4); n3 = int((np.abs(ev) < 1e-9).sum())
    res["naive_4comp_flow"] = n3
    lines.append(f"naive Hamiltonian alpha.S (4 comp/site), L=4: zero modes {n3} -> {n3//2} Weyl-equivalents ({n3//4} Dirac)")
    # 4. ordered conditional-shift tick U = S_x S_y S_z on L=12
    L2 = 12
    T2, _ = shifts(L2)
    N2 = L2 ** 3
    Id = np.eye(N2)
    def Sj(a):
        Tp, Tm = T2[a], T2[a].T
        P_plus = np.diag([1, 0]); P_minus = np.diag([0, 1])
        # conditional shift along a by sigma_a eigenvalue: T (1-sigma)/2 + T^-1 (1+sigma)/2  (= cos k - i sin k sigma_a)
        return np.kron((np.eye(2) - SIG[a]) / 2, Tp) + np.kron((np.eye(2) + SIG[a]) / 2, Tm)
    U = Sj(0) @ Sj(1) @ Sj(2)
    assert np.allclose(U.conj().T @ U, np.eye(2 * N2), atol=1e-10)
    ev = np.linalg.eigvals(U)
    n0 = int((np.abs(ev - 1) < 1e-7).sum()); npi = int((np.abs(ev + 1) < 1e-7).sum())
    res["tick_ordered"] = dict(q0=n0, qpi=npi)
    lines.append(f"ordered tick U=S_x S_y S_z (2 comp/site), L=12: states at U=+1: {n0}, at U=-1: {npi} -> {(n0+npi)//2} Weyl nodes")
    lines.append("Weyl-equivalents: walker flow 8, KS staggered 4, naive 4-comp flow 16, ordered tick 16.")
    lines.append("Euclidean 4D (analytic, not run): naive Dirac 2^4 = 16 four-component Dirac (32 Weyl); staggered 4 tastes (8 Weyl).")
    return lines, res


if __name__ == "__main__":
    lines, res = main()
    for l in lines: print(l)
    json.dump(res, open("C_census_results.json", "w"), indent=1)
