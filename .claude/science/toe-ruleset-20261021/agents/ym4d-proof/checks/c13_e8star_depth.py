#!/usr/bin/env python3
"""Check c13 (PROOF.md, session 4): E8* at depth k = 2 and the sup-norm induction (L6loc, E8*-k), plus the REVIEW_S3
threshold recomputation for E8.3.
(R) E8.3 AF-window exponent 3 x^2 4 N b0 (delta -> 0), x = 2 arcsin(t/2), at t = 1 and t = 3 tau_N/4 (R3-fix).
(A) One-step sup lemma (Lemma E8*-sup): for S4' (all d! orders) and any field whose plaquettes in the relevant region obey
    ||1 - U_p|| <= eta with A_L eta <= 1/2, every coarse plaquette obeys ||1 - V'_p|| <= C_1 eta, C_1 = L^2 + 4 c A_L,
    A_L = (d-1) L (L-1)/2, c = 4 arcsin(1/4). Tested on random small fields (random gauge transform of small random links),
    SU(2), d = 3, L = 3, for one and two steps (two-step bound C_1^2 eta, needs A_L C_1 eta <= 1/2).
(B) Sharpness (Proposition E8*-ob): constant U(1)-in-SU(2) flux eta per (1,2)-plaquette (one flux quantum on the torus):
    the level-k coarse plaquette has flux exactly L^{2k} eta, so ||1 - V^(k)_p|| / max ||1 - U_p|| = sin(L^{2k} eta / 2) /
    sin(eta / 2) ~ L^{2k}: the deterministic induction constant cannot beat L^2 per step.
Torus side 4 L^K (session-4 convention: level-m side divisible by 4). Pre-registered criteria are the PASS lines below.
Checks test instances, not uniformity.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, math, numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(13)
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
# (R)
rows = []
for N in (2, 3, 4, 5, 6, 7, 10):
    tau = min(1, 2 * math.sin(math.pi / N)); b0 = 11 * N / (48 * math.pi ** 2); out = []
    for t in (1.0, 0.75 * tau):
        ok = (N == 2 and t <= 2) or t < 2 * math.sin(math.pi / N)
        out.append(3 * (2 * math.asin(t / 2)) ** 2 * 4 * N * b0 if ok else float("nan"))
    rows.append((N, out))
print("INFO (R) 3x^2*4N*b0 [dense iff < 4]: " + "; ".join(f"N={N}: t=1 {o[0]:.3f}, t=3tau/4 {o[1]:.3f}" for N, o in rows))
dense = [N for N, o in rows if o[1] < 4]
check("R E7.0-in-AF-window falsification at t = 3 tau_N/4 holds exactly for N in {2,3,4} among those tested", dense == [2, 3, 4],
      f"dense for N = {dense}; SU(2) lambda_c/lambda_AF = {4 / rows[0][1][1]:.2f}")
# quaternion SU(2)
def qmul(p, q):
    a1, v1 = p[..., :1], p[..., 1:]; a2, v2 = q[..., :1], q[..., 1:]
    return np.concatenate([a1 * a2 - np.sum(v1 * v2, -1, keepdims=True), a1 * v2 + a2 * v1 + np.cross(v1, v2)], -1)
conj = lambda q: q * np.array([1, -1, -1, -1])
def qlog(q):  # principal log; odd branch rule irrelevant here (all fields in domain)
    a = np.clip(q[..., 0], -1, 1); v = q[..., 1:]; nv = np.linalg.norm(v, axis=-1, keepdims=True)
    return np.where(nv > 1e-15, v / np.maximum(nv, 1e-300) * np.arccos(a)[..., None], 0.0)
def qexp(w):
    nw = np.linalg.norm(w, axis=-1, keepdims=True)
    return np.concatenate([np.cos(nw), np.where(nw > 1e-15, np.sin(nw) / np.maximum(nw, 1e-300), 1.0) * w], -1)
dist1 = lambda q: 2 * np.sqrt(np.maximum(0, (1 - q[..., 0]) / 2))  # ||U - 1|| (operator norm) = 2 sin(theta/2)
d, L = 3, 3; E = np.eye(d, dtype=int); ORD = list(it.permutations(range(d)))
def block(U):
    """S4' on a d-torus field U[mu][x...] (quaternions). Returns the coarse field and max ||Z - 1||."""
    S = U.shape[1]; Tc = S // L; Xs = np.array(list(it.product(range(Tc), repeat=d))); out = np.zeros((d,) + (Tc,) * d + (4,)); zmax = 0.0
    def link(m, x, sg):
        if sg > 0: x = x % S; return U[m][tuple(x.T)]
        x = (x - E[m]) % S; return conj(U[m][tuple(x.T)])
    def path(a, b, order):
        P = np.tile([1.0, 0, 0, 0], (len(a), 1)); cur = a.copy(); diff = (b - a)[0]
        for m in order:
            sg = int(np.sign(diff[m]))
            for _ in range(abs(diff[m])): P = qmul(P, link(m, cur, sg)); cur = cur + sg * E[m]
        return P
    def straight(y, m):
        P = np.tile([1.0, 0, 0, 0], (len(y), 1)); cur = y.copy()
        for _ in range(L): P = qmul(P, link(m, cur, 1)); cur = cur + E[m]
        return P
    for m in range(d):
        cX = Xs * L + 1; cY = cX + L * E[m]; Sc = straight(cX, m); acc = np.zeros((len(Xs), 3))
        for o in ORD:
            for off in it.product(range(L), repeat=d):
                y = Xs * L + np.array(off)
                Z = qmul(conj(Sc), qmul(qmul(path(cX, y, o), straight(y, m)), conj(path(cY, y + L * E[m], o))))
                acc += qlog(Z); zmax = max(zmax, dist1(Z).max())
        out[m][tuple(Xs.T)] = qmul(Sc, qexp(acc / (len(ORD) * L ** d)))
    return out, zmax
def plaq_dist(V):
    r = []
    for a, b in it.combinations(range(d), 2):
        P = qmul(qmul(V[a], np.roll(V[b], -1, axis=a)), qmul(conj(np.roll(V[a], -1, axis=b)), conj(V[b]))); r.append(dist1(P).ravel())
    return np.concatenate(r)
def plaq_q(V, a, b):
    return qmul(qmul(V[a], np.roll(V[b], -1, axis=a)), qmul(conj(np.roll(V[a], -1, axis=b)), conj(V[b])))
AL = (d - 1) * L * (L - 1) // 2; c = 4 * math.asin(0.25); C1 = L ** 2 + 4 * c * AL
print(f"INFO A_L = {AL}, c = {c:.4f}, C_1 = L^2 + 4 c A_L = {C1:.2f} (d = {d}, L = {L})")
# (A) random small fields: U_b = g_x exp(amp * xi_b) g_y^-1
S = 4 * L ** 2; worst1 = worst2 = 0.0; zm = 0.0
for trial in range(2):
    amp = 1e-4 / (1 + trial)  # second run used 1e-4*(1+trial), also aborted at trial 1; first run used 2e-4*(1+trial); trial 1 violated the domain assert
    xi = rng.normal(size=(d,) + (S,) * d + (3,)); Uloc = qexp(amp * xi)
    g = rng.normal(size=(S,) * d + (4,)); g /= np.linalg.norm(g, axis=-1, keepdims=True)
    U = np.stack([qmul(qmul(g, Uloc[m]), conj(np.roll(g, -1, axis=m))) for m in range(d)])
    eta = plaq_dist(U).max(); V1, z1 = block(U); eta1 = plaq_dist(V1).max(); V2, z2 = block(V1); eta2 = plaq_dist(V2).max()
    print(f"INFO domain factor A_L C_1 eta = {AL * C1 * eta:.3f} (must be <= 0.5)"); assert AL * C1 * eta <= 0.5
    worst1 = max(worst1, eta1 / eta); worst2 = max(worst2, eta2 / eta); zm = max(zm, z1 / eta)
    print(f"INFO (A) trial {trial}: eta = {eta:.2e}, max||Z1-1||/eta = {z1 / eta:.2f} (<= A_L = {AL}), level-1 ratio {eta1 / eta:.2f}, level-2 ratio {eta2 / eta:.2f}; t={time.time() - T0:.0f}s")
check("A1 ribbon: max ||Z - 1|| <= A_L eta at the first step", zm <= AL + 1e-9, f"{zm:.2f} <= {AL}")
check("A2 one-step sup lemma: ||1 - V'_p|| <= C_1 eta", worst1 <= C1, f"max ratio {worst1:.2f} <= {C1:.2f}")
check("A3 two-step sup induction: ||1 - V''_p|| <= C_1^2 eta", worst2 <= C1 ** 2, f"max ratio {worst2:.2f} <= {C1 ** 2:.0f}")
# (B) constant flux: U_1(x) = exp(-i eta x_2 sigma_3); U_2 wrap links at x_2 = S-1 carry exp(+i eta S x_1 sigma_3); eta S^2 = 2 pi
eta = 2 * np.pi / S ** 2; U = np.zeros((d,) + (S,) * d + (4,)); U[..., 0] = 1.0
x1 = np.arange(S)[:, None, None] * np.ones((S, S, S)); x2 = np.arange(S)[None, :, None] * np.ones((S, S, S))
ph = -eta * x2; U[0][..., 0] = np.cos(ph); U[0][..., 3] = np.sin(ph)
ph2 = np.where(x2 == S - 1, eta * S * x1, 0.0); U[1][..., 0] = np.cos(ph2); U[1][..., 3] = np.sin(ph2)
P0 = plaq_q(U, 0, 1); fl0 = np.arctan2(P0[..., 3], P0[..., 0])
check("B0 fine field: every (1,2) plaquette has flux eta, other planes flat",
      np.allclose(np.abs(fl0), eta, atol=1e-12) and plaq_dist(U)[S ** 3:].max() < 1e-7 if d == 3 else False, f"eta = {eta:.4e}")  # run 3 used 1e-12: dist1 = 2 sqrt((1-q0)/2) loses half the digits
V1, _ = block(U); V2, _ = block(V1); res = []
for k, V in ((1, V1), (2, V2)):
    Pk = plaq_q(V, 0, 1); flk = np.abs(np.arctan2(Pk[..., 3], np.abs(Pk[..., 0]) * np.sign(Pk[..., 0])))
    res.append((k, flk.min(), flk.max(), L ** (2 * k) * eta))
ok = all(abs(lo - pr) < 1e-9 and abs(hi - pr) < 1e-9 for _, lo, hi, pr in res)
rat = [math.sin(pr / 2) / math.sin(eta / 2) for *_, pr in res]
check("B1 sharpness: level-k coarse flux = L^{2k} eta exactly (k = 1, 2), so the sup ratio is sin(L^{2k} eta/2)/sin(eta/2)",
      ok, "; ".join(f"k={k}: flux in [{lo:.6f}, {hi:.6f}] vs {pr:.6f}" for k, lo, hi, pr in res) + "; ratios " + ", ".join(f"{r:.2f}" for r in rat))
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
