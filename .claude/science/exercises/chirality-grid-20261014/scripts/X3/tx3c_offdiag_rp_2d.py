"""T-X3c: off-diagonal (U+ != theta U-) RP necessary condition at beta_g = 0. Pre-registered in ../PREREG.md."""
"""T-X3b: necessary condition for RP of the gauged overlap (pre-registered in ../PREREG.md).
2D U(1), Lx=8 periodic, t in {-3..4} antiperiodic, link reflection t -> 1-t.
P_xy = Gamma D^{-1}(x, theta y) (x,y in Lambda+) must be PSD in every theta-symmetric background.
Also K-U's sufficient cross-kernel criterion Q1 = D(x,theta y) g0, Q2 = g0 D(theta x, y).
"""
import numpy as np
Lx, Lt = 8, 8
ts = np.arange(-3, 5)            # t values, index = t+3
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]).astype(complex)
gt, gx, g5 = s1, s2, s3
I2 = np.eye(2)
N = 2 * Lx * Lt
def idx(x, t):  # t actual value
    return 2 * (((t + 3) % Lt) * Lx + (x % Lx))

def wilson(Ux, Ut, kind="wilson"):
    """Ux[t_idx, x]: link (x,t)->(x+1,t); Ut[t_idx, x]: link (x,t)->(x,t+1) (t=4 wraps to -3, antiperiodic)."""
    D = np.zeros((N, N), complex)
    for ti, t in enumerate(ts):
        for x in range(Lx):
            a = idx(x, t)
            D[a:a + 2, a:a + 2] += 2 * I2
            # x forward / backward
            b = idx(x + 1, t); u = Ux[ti, x]
            D[a:a + 2, b:b + 2] += -0.5 * (I2 - gx) * u
            D[b:b + 2, a:a + 2] += -0.5 * (I2 + gx) * np.conj(u)
            # t forward
            tn = t + 1; sgn = 1.0
            if tn == 5: tn = -3; sgn = -1.0
            b = idx(x, tn); u = Ut[ti, x] * sgn
            D[a:a + 2, b:b + 2] += -0.5 * (I2 - gt) * u
            D[b:b + 2, a:a + 2] += -0.5 * (I2 + gt) * np.conj(u)
    return D

G5 = np.kron(np.eye(N // 2), g5); G0 = np.kron(np.eye(N // 2), gt)
def overlap(Ux, Ut, M):
    X = wilson(Ux, Ut) - M * np.eye(N)
    H = G5 @ X
    assert np.abs(H - H.conj().T).max() < 1e-12
    w, V = np.linalg.eigh(H)
    sgn = (V * np.sign(w)) @ V.conj().T
    return np.eye(N) + G5 @ sgn, np.abs(w).min()

plus = [t for t in ts if t >= 1]
def theta(t): return 1 - t
def blocks(D, m):
    Dm = (1 - m / 2) * D + m * np.eye(N) if m is not None else D
    S = np.linalg.inv(Dm)
    n = len(plus) * Lx
    P = np.zeros((2 * n, 2 * n), complex); Q1 = np.zeros_like(P); Q2 = np.zeros_like(P)
    sites = [(x, t) for t in plus for x in range(Lx)]
    for i, (x, t) in enumerate(sites):
        for j, (y, s) in enumerate(sites):
            a = idx(x, t); bth = idx(y, theta(s)); ath = idx(x, theta(t)); b = idx(y, s)
            P[2*i:2*i+2, 2*j:2*j+2] = gt @ S[a:a+2, bth:bth+2]
            Q1[2*i:2*i+2, 2*j:2*j+2] = Dm[a:a+2, bth:bth+2] @ gt
            Q2[2*i:2*i+2, 2*j:2*j+2] = gt @ Dm[ath:ath+2, b:b+2]
    return P, Q1, Q2

def stats(A):
    herm = np.abs(A - A.conj().T).max() / np.abs(A).max()
    ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
    sc = np.abs(ev).max()
    return ev.min() / sc, ev.max() / sc, herm


rng = np.random.default_rng(11)
def rand_half(kind, s):
    if kind == "S":
        A = rng.normal(0, s, Lx)
        return {"Ux": {t: np.exp(1j * A) for t in plus}, "Ut": {t: np.ones(Lx, complex) for t in [1, 2, 3]}}
    return {"Ux": {t: np.exp(1j * rng.normal(0, s, Lx)) for t in plus},
            "Ut": {t: np.exp(1j * rng.normal(0, s, Lx)) for t in [1, 2, 3]}}
def bg(ua, ub):
    Ux = np.ones((Lt, Lx), complex); Ut = np.ones((Lt, Lx), complex)
    for t in plus:
        Ux[t + 3] = ua["Ux"][t]; Ux[theta(t) + 3] = ub["Ux"][t]
    for t in [1, 2, 3]:
        Ut[t + 3] = ua["Ut"][t]; Ut[-t + 3] = np.conj(ub["Ut"][t])
    return Ux, Ut
m = 0.05
def Dm_of(kind, Ux, Ut, M=1.0):
    D = wilson(Ux, Ut) if kind == "W" else overlap(Ux, Ut, M)[0]
    return (1 - m / 2) * D + m * np.eye(N)
sites = [(x, t) for t in plus for x in range(Lx)]
def Pmat(Dm):
    S = np.linalg.inv(Dm); n = len(sites)
    P = np.zeros((2 * n, 2 * n), complex)
    for i, (x, t) in enumerate(sites):
        a = idx(x, t)
        for j, (y, s_) in enumerate(sites):
            b = idx(y, theta(s_))
            P[2*i:2*i+2, 2*j:2*j+2] = gt @ S[a:a+2, b:b+2]
    return P
def herm_min(K):
    h = np.abs(K - K.conj().T).max() / np.abs(K).max()
    ev = np.linalg.eigvalsh(0.5 * (K + K.conj().T))
    return h, ev.min() / np.abs(ev).max()
k = 8
for kind in ["S", "E"]:
    for s in [0.3, 1.0]:
        out = {"W": [], "O": []}
        for rep in range(10):
            U = [rand_half(kind, s) for _ in range(k)]
            for F in ["W", "O"]:
                logZ = np.zeros((k, k), complex); Ps = {}
                for a in range(k):
                    for b in range(k):
                        Dm = Dm_of(F, *bg(U[a], U[b]))
                        sg, ld = np.linalg.slogdet(Dm)
                        logZ[a, b] = ld + np.log(sg)
                        Ps[(a, b)] = Pmat(Dm)
                d = np.real(np.diag(logZ))
                Zn = np.exp(logZ - 0.5 * (d[:, None] + d[None, :]))
                hZ, mZ = herm_min(Zn)
                diagpos = bool(np.all(np.abs(np.imag(np.exp(1j*np.imag(np.diag(logZ))))) < 1e-8) and np.all(np.real(np.exp(1j*np.imag(np.diag(logZ)))) > 0))
                nb = Ps[(0, 0)].shape[0]
                variants = {}
                for vname, fn in {"Z_ab P_ab": lambda a, b: Zn[a, b] * Ps[(a, b)],
                                  "Z_ab P_ab^T": lambda a, b: Zn[a, b] * Ps[(a, b)].T,
                                  "Z_ba P_ba": lambda a, b: Zn[b, a] * Ps[(b, a)],
                                  "Z_ba P_ba^T": lambda a, b: Zn[b, a] * Ps[(b, a)].T}.items():
                    K = np.zeros((k * nb, k * nb), complex)
                    for a in range(k):
                        for b in range(k):
                            K[b*nb:(b+1)*nb, a*nb:(a+1)*nb] = fn(a, b)
                    variants[vname] = herm_min(K)
                out[F].append((hZ, mZ, diagpos, variants))
        for F in ["W", "O"]:
            hZ = max(o[0] for o in out[F]); mZ = min(o[1] for o in out[F]); dp = all(o[2] for o in out[F])
            vs = {v: (max(o[3][v][0] for o in out[F]), min(o[3][v][1] for o in out[F])) for v in out[F][0][3]}
            vstr = "; ".join(f"{v}: herm {h:.1e} min {mm:+.2e}" for v, (h, mm) in vs.items())
            print(f"type={kind} s={s} {'Wilson ' if F=='W' else 'overlap'}: Z herm {hZ:.1e}, Z min-eig/max {mZ:+.3e}, Z_aa>0 all {dp} | B: {vstr}")
print("done")
