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

rng = np.random.default_rng(7)
def background(kind, s):
    Ux = np.ones((Lt, Lx), complex); Ut = np.ones((Lt, Lx), complex)
    if kind == "free": return Ux, Ut
    if kind == "S":
        A = rng.normal(0, s, Lx)
        for ti in range(Lt): Ux[ti] = np.exp(1j * A)
        return Ux, Ut
    # generic theta-symmetric
    for t in plus:
        Ux[t + 3] = np.exp(1j * rng.normal(0, s, Lx))
        Ux[theta(t) + 3] = Ux[t + 3]
    for t in [1, 2, 3]:
        Ut[t + 3] = np.exp(1j * rng.normal(0, s, Lx))
        Ut[-t + 3] = np.conj(Ut[t + 3])   # link (-t) -> (-t+1)
    # crossing links t=0->1 and t=4->-3 stay 1
    return Ux, Ut

m = 0.05
print("calibration (free):")
for name, D in [("Wilson r=1", wilson(*background("free", 0))), ("overlap M=1", overlap(*background("free", 0), 1.0)[0])]:
    P, Q1, Q2 = blocks(D, m)
    print(f"  {name:12s} P: min/max {stats(P)[0]:+.2e} herm {stats(P)[2]:.1e} | Q1 eig range [{stats(Q1)[0]:+.2e},{stats(Q1)[1]:+.2e}] herm {stats(Q1)[2]:.1e}"
          f" | Q2 [{stats(Q2)[0]:+.2e},{stats(Q2)[1]:+.2e}] herm {stats(Q2)[2]:.1e}")
res = {}
for M in [1.0, 1.5]:
    for kind in ["S", "E"]:
        for s in [0.3, 1.0]:
            worstP = {"W": 1, "O": 1}; q1max = -9; q2min = 9; hq = 0; gapmin = 9; hP = 0
            for c in range(20):
                Ux, Ut = background(kind, s)
                # check theta-symmetry of the Wilson operator: D^dag = Theta D Theta (gamma0)
                DW = wilson(Ux, Ut)
                PW, _, _ = blocks(DW, m)
                worstP["W"] = min(worstP["W"], stats(PW)[0])
                DO, gap = overlap(Ux, Ut, M)
                gapmin = min(gapmin, gap)
                P, Q1, Q2 = blocks(DO, m)
                a, b, h = stats(P); worstP["O"] = min(worstP["O"], a); hP = max(hP, h)
                a1, b1, h1 = stats(Q1); a2, b2, h2 = stats(Q2)
                q1max = max(q1max, b1); q2min = min(q2min, a2); hq = max(hq, h1, h2)
            print(f"M={M} bg={kind} s={s}: Wilson P min/max worst {worstP['W']:+.2e} | overlap P worst {worstP['O']:+.2e} (herm {hP:.1e})"
                  f" | Q1 max-eig/scale worst {q1max:+.2e}, Q2 min-eig/scale worst {q2min:+.2e} (herm {hq:.1e}) | min|H_W| {gapmin:.3f}")
print("done")
