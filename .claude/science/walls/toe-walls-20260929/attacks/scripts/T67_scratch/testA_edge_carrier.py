"""T67 Test A: can nearest-neighbour bond lengths be the geometric carrier?

Uses the repository's own landed Regge Hessian (read-only import of R4).
Pre-registration: PREREG.md in this folder.
"""
import sys, itertools
import numpy as np

MAIN = "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts"
sys.path.insert(0, MAIN)
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4

DIRS = R4.DIRS15
IDX = R4.DIR_IDX
AX = [IDX[(1, 0, 0, 0)], IDX[(0, 1, 0, 0)], IDX[(0, 0, 1, 0)], IDX[(0, 0, 0, 1)]]
FACE = [IDX[v] for v in DIRS if sum(v) == 2]
TRIP = [IDX[v] for v in DIRS if sum(v) == 3]
BODY = [IDX[(1, 1, 1, 1)]]
assert len(AX) == 4 and len(FACE) == 6 and len(TRIP) == 4

rng = np.random.default_rng(20260929)


def schur(Q, S):
    """Effective Hessian on edge set S with the complement relaxed (minimised over)."""
    S = list(S)
    C = [i for i in range(15) if i not in S]
    Qss = Q[np.ix_(S, S)]
    if not C:
        return Qss
    Qsc = Q[np.ix_(S, C)]
    Qcs = Q[np.ix_(C, S)]
    Qcc = Q[np.ix_(C, C)]
    # pinv with tolerance; range consistency checked separately
    Qcc_p = np.linalg.pinv(Qcc, rcond=1e-10, hermitian=True)
    return Qss - Qsc @ Qcc_p @ Qcs


def schur_diag(Q, S):
    """returns (Q_eff, nullity of Q_cc, consistency residual ||(1-Qcc Qcc^+) Qcs|| / ||Q||)."""
    S = list(S)
    C = [i for i in range(15) if i not in S]
    if not C:
        return Q[np.ix_(S, S)], 0, 0.0
    Qcc = Q[np.ix_(C, C)]
    Qcs = Q[np.ix_(C, S)]
    ev = np.linalg.eigvalsh((Qcc + Qcc.conj().T) / 2)
    nul = int(np.sum(np.abs(ev) < 1e-9 * max(np.abs(Q).max(), 1e-30)))
    Qcc_p = np.linalg.pinv(Qcc, rcond=1e-10, hermitian=True)
    res = np.linalg.norm(Qcs - Qcc @ Qcc_p @ Qcs) / max(np.linalg.norm(Q, 2), 1e-30)
    return schur(Q, S), nul, float(res)


def eig_abs(Q):
    return np.sort(np.abs(np.linalg.eigvalsh((Q + Q.conj().T) / 2)))[::-1]


def rank_tol(Q, rel=1e-9, ref=None):
    ev = eig_abs(Q)
    ref = ev[0] if ref is None else ref
    return int(np.sum(ev > rel * ref))


out = []


def P(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


P("T67 Test A: edge-carrier test on the landed 4D cubic-Coxeter Regge Hessian")
P("edge classes: 4 axis (NN incl. tick), 6 face-diag, 4 triple-diag, 1 body-diag; only the 4 axis edges join NN sites")

# ---------------------------------------------------------------- A1
P("\n== A1: axis-only carrier, 11 diagonals frozen at flat ==")
Q0 = R4.bloch_Q(np.zeros(4))
P("Q(0) full spectrum (sorted |ev|):", np.round(eig_abs(Q0), 6))
Qaa0 = Q0[np.ix_(AX, AX)]
P("Q_aa(0) eigenvalues:", np.round(np.linalg.eigvalsh(Qaa0), 6), " |Q_aa(0)|_F =", round(float(np.linalg.norm(Qaa0)), 6))
P("=> mass-type term at k=0 for axis lengths:", bool(np.linalg.norm(Qaa0) > 1e-8))

# gauge leakage and low-k scaling
P("\ngauge leakage of Q_aa on the axis-edge image of vertex displacements, and Q_aa spectrum scaling")
for lam in [0.2, 0.1, 0.05, 0.02]:
    leaks, mins, maxs = [], [], []
    for _ in range(20):
        k = rng.uniform(0.3, 1.0, 4) * rng.choice([-1, 1], 4) * lam
        Q = R4.bloch_Q(k)
        G = R4.gauge_map(k)
        assert np.abs(Q @ G).max() < 1e-10  # full Q kills the full gauge orbit
        Qaa = Q[np.ix_(AX, AX)]
        GA = G[AX, :]
        num = np.linalg.norm(Qaa @ GA)
        den = np.linalg.norm(Qaa) * np.linalg.norm(GA)
        leaks.append(num / den)
        ev = eig_abs(Qaa)
        mins.append(ev[-1]); maxs.append(ev[0])
    P(f"lam={lam:5.2f}: median leakage ratio {np.median(leaks):.3f}; |Q_aa| eig max median {np.median(maxs):.4g}, min median {np.median(mins):.4g}")

# ---------------------------------------------------------------- A2
P("\n== A2: axis-only carrier, diagonals relaxed (Schur complement) ==")
for lam in [0.2, 0.1, 0.05, 0.02]:
    r_list, nrm_ratio, nuls, ress = [], [], [], []
    for _ in range(20):
        k = rng.uniform(0.3, 1.0, 4) * rng.choice([-1, 1], 4) * lam
        Q = R4.bloch_Q(k)
        Qe, nul, res = schur_diag(Q, AX)
        ref = max(np.linalg.norm(Q, 2), 1e-30)
        nrm_ratio.append(np.linalg.norm(Qe, 2) / ref)
        r_list.append(rank_tol(Qe, 1e-9, ref))
        nuls.append(nul); ress.append(res)
    P(f"lam={lam:5.2f}: max ||Q_eff||/||Q|| = {max(nrm_ratio):.3e}; ranks seen {sorted(set(r_list))}; nullity(Q_cc) {sorted(set(nuls))}; max consistency residual {max(ress):.1e}")

P("\ndegenerate momenta (some k_mu = 0): rank of A2 Q_eff (axis-only relaxed)")
lam = 0.1
for zeros in [(), (0,), (1,), (3,), (0, 1), (0, 3), (0, 1, 2), (1, 2, 3)]:
    k = rng.uniform(0.3, 1.0, 4) * lam
    for z in zeros:
        k[z] = 0.0
    Q = R4.bloch_Q(k)
    Qe = schur(Q, AX)
    ref = np.linalg.norm(Q, 2)
    P(f"  zero comps {zeros}: rank {rank_tol(Qe, 1e-9, ref)}, ||Q_eff||/||Q|| = {np.linalg.norm(Qe,2)/ref:.3e}")

# ---------------------------------------------------------------- A3 / A4
P("\n== A3/A4: supplementary edge sets S (containing the 4 axes), rest relaxed ==")
P("generic k (lam=0.1); expected metric chart: rank 6 = 10 metric comps - 4 gauge")
k = np.array([0.083, -0.061, 0.097, 0.052])
Q = R4.bloch_Q(k)
ref = np.linalg.norm(Q, 2)
G = R4.gauge_map(k)
sets = {
    "axes (4)": AX,
    "axes + 3 spatial face diag (7)": AX + [IDX[v] for v in DIRS if sum(v) == 2 and v[3] == 0],
    "axes + 3 tick-space face diag (7)": AX + [IDX[v] for v in DIRS if sum(v) == 2 and v[3] == 1],
    "axes + 6 face diag (10)": AX + FACE,
    "axes + face + triple (14)": AX + FACE + TRIP,
    "all 15": list(range(15)),
}
for name, S in sets.items():
    Qe, nul, res = schur_diag(Q, S)
    GS = G[S, :]
    gz = np.linalg.norm(Qe @ GS) / max(np.linalg.norm(Qe, 2) * np.linalg.norm(GS), 1e-30)
    P(f"  {name:38s} |S|={len(S):2d}: nullity(Q_cc)={nul:2d}, relax-consistency residual {res:.1e}; rank(Q_eff)={rank_tol(Qe,1e-9,ref):2d}; ||Q_eff||/||Q|| = {np.linalg.norm(Qe,2)/ref:.3e}; gauge-orbit leakage {gz:.1e}")

# frozen (no relaxation) version of the same sets, for the mass-term diagnosis
P("\nfrozen-complement versions (complement edges held at flat): Q[S,S] at k=0 and gauge leakage at generic k")
Q0 = R4.bloch_Q(np.zeros(4))
for name, S in sets.items():
    QS0 = Q0[np.ix_(S, S)]
    QS = Q[np.ix_(S, S)]
    GS = G[S, :]
    lk = np.linalg.norm(QS @ GS) / max(np.linalg.norm(QS, 2) * np.linalg.norm(GS), 1e-30)
    P(f"  {name:38s}: ||Q_SS(0)||_F = {np.linalg.norm(QS0):.4g}; gauge leakage at generic k = {lk:.3f}")

# does relaxed 10-edge chart reproduce the landed low-k EH class? compare with metric-map pullback
P("\ncontrol: relaxed 10-edge (axes+face) Hessian vs metric-sector pullback M^dag Q M at lam=0.02 (both are the landed Q_h up to chart)")
lam = 0.02
kk = np.array([0.6, -0.4, 0.5, 0.3]) * lam
Q = R4.bloch_Q(kk)
S = AX + FACE
Qe = schur(Q, S)
M = R4.metric_map(kk)
# metric h -> S-edges via M[S,:]; pull Qe back
MS = M[S, :]
Qh_from_S = MS.conj().T @ Qe @ MS
Qh_full = M.conj().T @ Q @ M
P("  ||Qh_from_S - Qh_full||/||Qh_full|| =", f"{np.linalg.norm(Qh_from_S-Qh_full)/np.linalg.norm(Qh_full):.3e}")
P("  eigenvalues of Qh_full / lam^2:", np.round(np.linalg.eigvalsh(Qh_full) / lam**2, 4))

# 3 spatial axes only, static (k_tau = 0): the space-only version of the same test
P("\n== A2s: spatial axes only (3), static k_tau=0, everything else (tick edge, all diagonals) relaxed ==")
SP = AX[:3]
for lam in [0.2, 0.05]:
    for _ in range(3):
        k = np.r_[rng.uniform(0.3, 1.0, 3) * rng.choice([-1, 1], 3) * lam, 0.0]
        Q = R4.bloch_Q(k)
        Qe, nul, res = schur_diag(Q, SP)
        P(f"  lam={lam}: ||Q_eff||/||Q|| = {np.linalg.norm(Qe,2)/np.linalg.norm(Q,2):.2e}, nullity(Q_cc)={nul}, consistency residual {res:.1e}")

open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T67_scratch/testA_output.txt", "w").write("\n".join(out) + "\n")
