"""Kahler-Dirac fibre: Gamma_a = eps_a + iota_a on 2^d exterior algebra; G = diag((-1)^k)."""
import numpy as np
from itertools import combinations

def ext_ops(d):
    """Return eps[a], iota[a] (a=0..d-1) and grade operator on 2^d dim exterior algebra."""
    dim = 1 << d
    def bits(S): return [i for i in range(d) if (S >> i) & 1]
    eps = []
    for a in range(d):
        E = np.zeros((dim, dim), dtype=complex)
        for S in range(dim):
            if (S >> a) & 1: continue
            sgn = (-1) ** sum(1 for i in range(a) if (S >> i) & 1)
            E[S | (1 << a), S] = sgn
        eps.append(E)
    iot = [E.conj().T for E in eps]
    grade = np.array([bin(S).count("1") for S in range(dim)])
    G = np.diag(((-1.0) ** grade).astype(complex))
    return eps, iot, G, grade

def kd_gammas(d):
    eps, iot, G, grade = ext_ops(d)
    Gam = [eps[a] + iot[a] for a in range(d)]
    Gbar = [eps[a] - iot[a] for a in range(d)]   # anticommute with all Gam
    return Gam, Gbar, G

def checks(d):
    Gam, Gbar, G = kd_gammas(d); dim = 1 << d; I = np.eye(dim)
    out = {}
    out['clifford'] = max(np.max(np.abs(Gam[a]@Gam[b]+Gam[b]@Gam[a] - 2*(a==b)*I))
                          for a in range(d) for b in range(d))
    out['G_anticomm'] = max(np.max(np.abs(G@Gam[a]+Gam[a]@G)) for a in range(d))
    out['G2'] = np.max(np.abs(G@G - I))
    out['Gam_herm'] = max(np.max(np.abs(Gam[a]-Gam[a].conj().T)) for a in range(d))
    out['Gam_real'] = max(np.max(np.abs(Gam[a].imag)) for a in range(d))
    out['Gbar_anti_Gam'] = max(np.max(np.abs(Gbar[a]@Gam[b]+Gam[b]@Gbar[a]))
                               for a in range(d) for b in range(d))
    return out

if __name__ == "__main__":
    for d in [2,4]:
        print(f"d={d} fibre dim={1<<d}: ", {k: f"{v:.2e}" for k,v in checks(d).items()})
    Gam,Gbar,G = kd_gammas(2)
    T = Gbar[0]@Gbar[1]
    print("\nd=2 taste generator T = Gbar_1 Gbar_2")
    print("  T^2 + I  :", np.max(np.abs(T@T+np.eye(4))))
    print("  [T,Gam_a]:", max(np.max(np.abs(T@Gam[a]-Gam[a]@T)) for a in range(2)))
    print("  [T,G]    :", np.max(np.abs(T@G-G@T)))
    print("  eig(T)   :", np.round(np.linalg.eigvals(T),10))
    print("  Gam_1 =\n", Gam[0].real.astype(int))
    print("  Gam_2 =\n", Gam[1].real.astype(int))
    print("  G     =", np.diag(G).real.astype(int))
