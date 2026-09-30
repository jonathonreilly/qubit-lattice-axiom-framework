"""Kill-check T67: the third NN-length reading the attack did not test.
Diagonal edges SLAVED to the four axis lengths by Pythagoras (rectangular cells, the diagonal-metric
truncation that blocks 59-61 use), not frozen at flat and not relaxed.
Uses the repository's own R4 Hessian (read-only import).
"""
import sys
import numpy as np
MAIN = "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts"
sys.path.insert(0, MAIN)
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4
np.set_printoptions(precision=4, suppress=True, linewidth=160)
rng = np.random.default_rng(1)
DIAG = [0, 1, 2, 3]      # xx yy zz tt in HCOMPS

def sym(A): return (A + A.conj().T) / 2
out=[]
def P(*a):
    s=" ".join(str(x) for x in a); print(s); out.append(s)

P("== D1: Q_D(k) = M_d^dag Q M_d  (diag metric h_mumu -> all 15 edges by the landed line-averaged map)")
for lam in [0.2, 0.1, 0.05, 0.02]:
    k = np.array([0.6, -0.4, 0.5, 0.3]) * lam
    Q = R4.bloch_Q(k); M = R4.metric_map(k)
    Md = M[:, DIAG]
    QD = sym(Md.conj().T @ Q @ Md)
    ev = np.linalg.eigvalsh(QD)
    P(f"lam={lam}: eig(Q_D)/lam^2 =", np.round(ev / lam**2, 4), " |Q_D|/|Q_h| ratio", np.linalg.norm(QD)/np.linalg.norm(sym(M.conj().T@Q@M)))

P("\n== D2: is Q_D degenerate along the residual diagonal-preserving gauge (xi_mu depends on x_mu only)?")
# gauge: h = k_mu xi_nu + k_nu xi_mu. diagonal-preserving iff off-diagonals vanish: k_mu xi_nu + k_nu xi_mu = 0 (mu!=nu)
# for a generic k this forces xi = 0. So generic k: no residual gauge; count zero modes of Q_D
for kk in [np.array([0.06,-0.04,0.05,0.03]), np.array([0.06,0,0,0]), np.array([0.06,0.05,0,0]), np.array([0.06,0.05,0.04,0])]:
    Q = R4.bloch_Q(kk); M = R4.metric_map(kk)
    Md = M[:, DIAG]; QD = sym(Md.conj().T @ Q @ Md)
    P("k=",kk," eig(Q_D)/|k|^2 =", np.round(np.linalg.eigvalsh(QD)/np.dot(kk,kk),4))

P("\n== D3: does the diag-truncated Q_D equal the continuum EH quadratic form restricted to diagonal h?")
for lam in [0.05, 0.02, 0.01]:
    k = np.array([0.6, -0.4, 0.5, 0.3]) * lam
    Q = R4.bloch_Q(k); M = R4.metric_map(k)
    Qh = sym(M.conj().T @ Q @ M)
    QEH = R4.einstein_pairing_4d(k)
    # the R4 runner's comparator: Q_h = c * Q_EH + O(k^4) with c = -1/2
    c = np.vdot(QEH.flatten(), Qh.flatten()).real / np.vdot(QEH.flatten(), QEH.flatten()).real
    Md_idx = DIAG
    QD = Qh[np.ix_(Md_idx, Md_idx)]
    QEHd = QEH[np.ix_(Md_idx, Md_idx)]
    P(f"lam={lam}: fit c={c:.4f}; ||Q_h - c Q_EH||/||Q_h||={np.linalg.norm(Qh-c*QEH)/np.linalg.norm(Qh):.2e}; diag block: ||Q_D - c Q_EH,dd||/||Q_D||={np.linalg.norm(QD-c*QEHd)/np.linalg.norm(QD):.2e}")
    if lam==0.02:
        P("  Q_D/lam^2 =\n", np.round(QD.real/lam**2,4))
        P("  eig Q_D/lam^2:", np.round(np.linalg.eigvalsh(QD)/lam**2,4))

P("\n== D4: gauge non-invariance of Q_D: pure-gauge h (from xi) projected on diagonal part; residual action")
k = np.array([0.06,-0.04,0.05,0.03])
Q = R4.bloch_Q(k); M = R4.metric_map(k)
Qh = sym(M.conj().T @ Q @ M)
xi = np.array([1.0,0.7,-0.3,0.5])
h = np.zeros(10,complex)
HC=R4.HCOMPS
for i,(a,b) in enumerate(HC):
    h[i] = 1j*(k[a]*xi[b] + k[b]*xi[a])   # up to convention; check gauge null
P("Q_h on pure-gauge h (should be ~0):", np.linalg.norm(Qh@h)/ (np.linalg.norm(Qh)*np.linalg.norm(h)))
hd = h.copy(); hd[4:]=0
P("diag part of a pure-gauge mode has action ", np.real(np.vdot(hd, Qh@hd))/ (np.linalg.norm(Qh)*np.linalg.norm(hd)**2), " (nonzero => diagonal truncation breaks invariance)")
open("rerun_testD_output.txt","w").write("\n".join(out)+"\n")
