"""R19-1 s1: exact RK Hamiltonian on the L=2 coset (1024 states). Checks: H psi0 = 0, H >= 0 (frustration-free),
RK/Markov similarity, quantum double commutator = classical f-sum formula, spectral measures of TT/V/S at k=(0,0,pi),
spectral gap vs bU, N_type counts, and the bU=0 exact character solution."""
import numpy as np, itertools, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
from mc import move_tables, channel_pols, cvec, OFFS
L = 2; V = L**3; G = G_matrix(L); P = pattern_vectors(L); B = f2_basis(P); d = B.shape[0]
states = np.array([(np.array(c) @ B) % 2 for c in itertools.product([0, 1], repeat=d)], dtype=np.int64)
key = {s.tobytes(): i for i, s in enumerate(states.astype(np.int8))}
gam = (G @ states.T)//2; Es = (gam**2).sum(0).astype(float)
print("L=2 span dim", d, "states", len(states), "all Gn even:", np.all((G @ states.T) % 2 == 0))
# N_type: number of moves (pattern translates) containing a given slot, at large L (no wrap) -- from PATTERNS
cnt = np.zeros(6, int)
for p in PATTERNS:
    for (dx, t) in p: cnt[t] += 1
print("N_type (moves containing one slot of each type; xx yy zz xy yz xz):", cnt)
# moves at L=2 as XOR vectors (with multiplicity: every pattern x every base site)
mv = P % 2
def build_H(bU, t=1.0):
    N = len(states); H = np.zeros((N, N))
    for i, s in enumerate(states):
        for p in mv:
            s2 = (s ^ p); j = key[s2.astype(np.int8).tobytes()]
            dE = Es[j] - Es[i]
            if j == i: continue    # identity flip: -t + t*e^0 = 0
            H[j, i] += -t; H[i, i] += t*np.exp(-bU*dE/2)
    return H
def Ovec(kvec, eps):
    K = 2*np.pi*np.array(kvec)/L; c = cvec(eps)
    sites = list(itertools.product(range(L), repeat=3)); vals = np.zeros(len(states), complex)
    for t in range(6):
        for x in sites:
            s0 = (x[0]*L + x[1])*L + x[2]; ph = np.exp(-1j*K @ (np.array(x) + OFFS[t]))
            vals += c[t]*ph*(states[:, t*V + s0] - 0.5)
    return vals/np.sqrt(V)
for bU in [0.0, 1.0, 2.0, 3.0, 4.0]:
    H = build_H(bU); pi = np.exp(-bU*Es); pi /= pi.sum(); psi = np.sqrt(pi)
    w, U = np.linalg.eigh(H)
    nz = w[w > 1e-9]
    print("\nbU=%.1f: |H-H^T|=%.1e |H psi0|=%.1e min eig=%.2e  #zero modes=%d  gap=%.6f  max eig=%.3f" %
          (bU, np.abs(H - H.T).max(), np.linalg.norm(H @ psi), w.min(), int((w < 1e-9).sum()), nz.min(), w.max()))
    # Markov similarity: Lgen = -D^{-1/2} H D^{1/2}: rows sum to zero, off-diagonal >= 0
    Dm = np.diag(1/psi); Dp = np.diag(psi); Lg = -Dm @ H @ Dp
    off = Lg - np.diag(np.diag(Lg))
    print("   Markov: max|row sum|=%.1e  min offdiag=%.2e  detailed balance err=%.1e" %
          (np.abs(Lg.sum(1)).max(), off.min(), np.abs(pi[:, None]*Lg - (pi[:, None]*Lg).T).max()))
    for kv in [(0, 0, 1), (1, 1, 0), (1, 1, 1)]:
        pols = channel_pols(np.array(kv, float))
        for ch in ["TT", "V", "S"]:
            for ie, eps in enumerate(pols[ch]):
                O = Ovec(kv, eps); Opsi = O*psi
                Od = np.diag(O); HO = H @ Od - Od @ H
                dc = (Od.conj().T @ HO - HO @ Od.conj().T)
                fq = np.real(psi @ dc @ psi)/2
                # classical formula
                fc = 0.0
                for i, s in enumerate(states):
                    for p in mv:
                        s2 = s ^ p; j = key[s2.astype(np.int8).tobytes()]
                        if j == i: continue
                        fc += pi[i]*np.exp(-bU*(Es[j] - Es[i])/2)*abs(O[j] - O[i])**2
                fc /= 2
                Sk = np.real(np.vdot(Opsi, Opsi)) - abs(np.vdot(psi, Opsi))**2
                amp = U.T @ Opsi; wt = np.abs(amp)**2
                wt[w < 1e-9] = 0     # remove ground-space (k=pi has no overlap anyway)
                sup = sorted([(round(w[i], 4), wt[i]) for i in range(len(w)) if wt[i] > 1e-10])
                agg = {}
                for om, a in sup: agg[om] = agg.get(om, 0) + a
                top = sorted(agg.items(), key=lambda x: -x[1])[:4]
                lowest = min(agg) if agg else None
                print("   k=%s %s%d: f_quantum=%.5f f_classical=%.5f S=%.5f f/S=%.4f | lowest weighted omega=%s ; top weights %s" %
                      (kv, ch, ie + 1, fq, fc, Sk, fq/Sk if Sk > 1e-12 else np.nan, lowest,
                       [(o, round(a, 5)) for o, a in top]))
