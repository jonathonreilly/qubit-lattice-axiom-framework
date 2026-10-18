"""Q3: is the gravitational source allowed to be the record count? Test on the 2-rung carrier {1} with a block
reading L (exact on constant metrics, blind to non-site vertex moves). A source T couples as J = L^dag T.
Solvability needs J orthogonal to every null direction (vertex displacements).
 count source: formation adds T_tt with no current (k_t != 0, T_ti = 0).
 content source: the same T_tt, but carried by a current with k_t T_tt + k_i T_ti = 0 (formation moves content)."""
import sys, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
C = pickle.load(open('canon_1.pkl', 'rb')); site = [i for i, o in enumerate(C.OFF) if np.allclose(o, 0)][0]
HC = [(0,0),(1,1),(2,2),(3,3),(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def Gns(k):
    G = C.gauge(k); return np.hstack([G[:, 4*t:4*t+4] for t in range(len(C.types)) if t != site])
def reading(k):
    A = np.hstack([C.line_map(k), Gns(k)]); return np.linalg.solve(A.conj().T @ A, A.conj().T)[:10]
def Tvec(T4):
    return np.array([T4[a, b]*(1 if a == b else 2) for a, b in HC])   # pairing h_ab T^ab with symmetric off-diagonals counted twice
for kk in [np.array([0.02, -0.01, 0.015, 0.01j]), np.array([0.01, 0.0, 0.0, 0.02j]), np.array([0.012, 0.009, -0.006, 0.015j])]:
    L = reading(kk); G = C.gauge(kk)
    # count: only T_tt
    T = np.zeros((4, 4), complex); T[3, 3] = 1.0
    Jc = L.conj().T @ Tvec(T)
    # content: T_tt with the conserving current T_ti = -k_t T_tt k_i/|k_s|^2 ... continuity  k_t T_tt + k_i T_ti = 0
    ks = kk[:3]; kt = kk[3]; Tq = T.copy(); ti = -(kt*T[3, 3])*ks/np.dot(ks, ks)
    for i in range(3): Tq[i, 3] = Tq[3, i] = ti[i]
    Jq = L.conj().T @ Tvec(Tq)
    ov = lambda J: np.linalg.norm(G.conj().T @ J)/(np.linalg.norm(G)*np.linalg.norm(J))
    print(f"k={np.round(kk, 3)}: null-direction overlap  count source {ov(Jc):.2e}   content (conserved) source {ov(Jq):.2e}")
