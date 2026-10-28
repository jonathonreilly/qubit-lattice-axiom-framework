"""bb8t: Lemma GE-T (BFT_B §24.1), the box-Neumann adjoint Gamma_E^T, d = 4, abelian (lane B session 8).

Criteria: checks/bb8t_criteria.md (written before this script).
Box coordinates {0..S-1}^4, S = 4n + 1, centre c = (2n,)*4. Reflection torus side M = 2S (Lemma REF): torus coordinate y < S is
box coordinate y, y >= S is box coordinate M - 1 - y. 1-forms on the box: arrays (4, S, S, S, S), component mu at z is the link
z -> z + e_mu, zero where z_mu = S - 1 (no such box link). d f(b) = f(b+) - f(b-); d* = d^T.
"""
import time

import numpy as np

T0 = time.time()
rng = np.random.default_rng(8181)
D4 = 4


def sig5(t):
    t = np.minimum(np.abs(t), 1.0)
    return 1 - 10 * t ** 3 + 15 * t ** 4 - 6 * t ** 5


def symbol(M):
    k = 2 * np.pi * np.arange(M) / M
    kh = 2 * np.pi * np.arange(M // 2 + 1) / M
    c = 2 - 2 * np.cos(k)
    ch = 2 - 2 * np.cos(kh)
    lam = c[:, None, None, None] + c[None, :, None, None] + c[None, None, :, None] + ch[None, None, None, :]
    lam[0, 0, 0, 0] = np.inf
    return lam


def fold_idx(S):
    return np.concatenate([np.arange(S), np.arange(S)[::-1]])


def torus_potential(rho, S, lam):
    """u = G_M rho^R on the reflection torus (rho on the box; mean-zero Green function)."""
    idx = fold_idx(S)
    rR = rho[np.ix_(idx, idx, idx, idx)]
    return np.fft.irfftn(np.fft.rfftn(rR) / lam, s=rR.shape, axes=(0, 1, 2, 3))


def dbox(u, S):
    """box links of du (u on the torus or box; only the box part y < S is read)."""
    ub = u[:S, :S, :S, :S]
    F = np.zeros((D4,) + ub.shape)
    for mu in range(D4):
        F[mu] = np.roll(ub, -1, axis=mu) - ub
        sl = [slice(None)] * D4
        sl[mu] = S - 1
        F[mu][tuple(sl)] = 0.0
    return F


def crossing_max(u, S):
    """max |du| on links crossing the reflection planes (torus links S-1 -> S and M-1 -> 0)."""
    m = 0.0
    for mu in range(D4):
        du = np.roll(u, -1, axis=mu) - u
        sl = [slice(None)] * D4
        for pos in (S - 1, 2 * S - 1):
            sl[mu] = pos
            m = max(m, np.abs(du[tuple(sl)]).max())
    return m


def dstar(F):
    out = np.zeros(F.shape[1:])
    for mu in range(F.shape[0]):
        out += np.roll(F[mu], 1, axis=mu) - F[mu]
    return out


def field(rho, S, lam):
    u = torus_potential(rho, S, lam)
    return dbox(u, S), u


out = []
ok = {}
NS = [2, 3, 4, 5, 6]
q = {}
C1v = {}
C2v = {}
T0ok = T1ok = T2ok = T3ok = True
for n in NS:
    S = 4 * n + 1
    M = 2 * S
    lam = symbol(M)
    c = (2 * n,) * D4
    # T2: C_inf
    G = np.fft.irfftn(1.0 / lam, s=(M,) * 4, axes=(0, 1, 2, 3))
    cinf = max(np.abs(np.roll(G, -1, axis=mu) - G).max() for mu in range(D4))
    T2ok &= cinf <= 2.0
    del G
    # T0, T1 point dipoles
    ws = {"corner": (0, 0, 0, 0), "face": (0, 2 * n, 2 * n, 2 * n), "c+e1": (2 * n + 1, 2 * n, 2 * n, 2 * n),
          "random": tuple(int(v) for v in rng.integers(0, S, 4))}
    l1 = {}
    t0 = 0.0
    tz = 0.0
    for key, w in ws.items():
        rho = np.zeros((S,) * 4)
        rho[w] += 1.0
        rho[c] -= 1.0
        F, u = field(rho, S, lam)
        t0 = max(t0, np.abs(dstar(F) - rho).max())
        tz = max(tz, crossing_max(u, S) / np.abs(F).max())
        l1[key] = np.abs(F).sum()
        T1ok &= l1[key] <= 2 * M
        if key == "c+e1":
            C2v[n] = l1[key]
    q[n] = max(l1.values()) / n
    # random neutral rho for T0
    rho = rng.standard_normal((S,) * 4)
    rho -= rho.mean()
    F, u = field(rho, S, lam)
    t0r = np.abs(dstar(F) - rho).max() / np.abs(rho).max()
    tzr = crossing_max(u, S) / np.abs(F).max()
    T0ok &= (t0 <= 1e-9) and (tz <= 1e-9) and (t0r <= 1e-9) and (tzr <= 1e-9)
    # T1/T3 random psi on N_X
    grid = np.indices((S,) * 4)
    inN = np.all(np.abs(grid - 2 * n) <= n, axis=0)
    rat3 = []
    rat1 = []
    for kind in ("gauss", "unif"):
        psi = np.where(inN, rng.standard_normal((S,) * 4) if kind == "gauss" else rng.random((S,) * 4), 0.0)
        tot = psi.sum()
        rho = psi.copy()
        rho[c] -= tot
        F, _ = field(rho, S, lam)
        b1 = M * np.abs(rho).sum()
        rat1.append(np.abs(F).sum() / b1)
        b3 = (M / 4) * np.abs(psi).max() + 32 * abs(tot)
        rat3.append(np.abs(F).max() / b3)
    T1ok &= max(rat1) <= 1.0
    T3ok &= max(rat3) <= 1.0
    # C1: psi = 1 on N_X
    psi = inN.astype(float)
    rho = psi.copy()
    rho[c] -= psi.sum()
    F, _ = field(rho, S, lam)
    C1v[n] = np.abs(F).max() / (2 * n + 1) ** 4
    out.append(f"n = {n} (S = {S}, M = {M}): C_inf = {cinf:.4f}; T0 max|d*F - rho| = {max(t0, t0r):.1e}, crossing flux "
               f"{max(tz, tzr):.1e}; ||F||_1 (corner, face, c+e1, random) = " + ", ".join(f"{l1[k]:.3f}" for k in ws)
               + f" (bound 2M = {2 * M}); max_w ||F||_1/n = {q[n]:.4f}; T1 random ratio max {max(rat1):.4f}; "
               f"T3 ratio max {max(rat3):.4f}; C1 sup/(2n+1)^4 = {C1v[n]:.4f}")
    del lam
T1ok &= q[6] <= 1.25 * q[4]
out.append(f"T0 identity (a) and zero crossing flux: {'PASS' if T0ok else 'FAIL'}")
out.append(f"T1 l1 bound and GE-F1 (q(6)/q(4) = {q[6] / q[4]:.4f} <= 1.25): {'PASS' if T1ok else 'FAIL'}")
out.append(f"T2 C_inf <= 2: {'PASS' if T2ok else 'FAIL'}")
out.append(f"T3 l-infinity bound (e): {'PASS' if T3ok else 'FAIL'}")


# ---------- T4: adjointness against a direct CG solve (n = 2) ----------
def cg(apply, b, tol=1e-14, maxit=20000):
    x = np.zeros_like(b)
    r = b - apply(x)
    p = r.copy()
    rs = (r * r).sum()
    b2 = (b * b).sum()
    for it in range(maxit):
        Ap = apply(p)
        a = rs / (p * Ap).sum()
        x += a * p
        r -= a * Ap
        rn = (r * r).sum()
        if rn <= tol ** 2 * b2:
            break
        p = r + (rn / rs) * p
        rs = rn
    return x, it


def mask1(S):
    m = np.ones((D4,) + (S,) * 4, bool)
    for mu in range(D4):
        sl = [slice(None)] * D4
        sl[mu] = S - 1
        m[mu][tuple(sl)] = False
    return m


def dfun(lmb, S):
    F = np.zeros((D4,) + lmb.shape)
    for mu in range(D4):
        F[mu] = np.roll(lmb, -1, axis=mu) - lmb
        sl = [slice(None)] * D4
        sl[mu] = S - 1
        F[mu][tuple(sl)] = 0.0
    return F


def lam_direct(x, S, cidx):
    rhs = -dstar(x)
    sol, it = cg(lambda v: dstar(dfun(v, S)), rhs)
    return sol - sol[cidx], it


n = 2
S = 4 * n + 1
M = 2 * S
lam = symbol(M)
c = (2 * n,) * D4
MK = mask1(S)
x = np.where(MK, rng.standard_normal((D4,) + (S,) * 4), 0.0)
psi = rng.standard_normal((S,) * 4)
lx, it4 = lam_direct(x, S, c)
rho = psi.copy()
rho[c] -= psi.sum()
F, _ = field(rho, S, lam)
lhs = (psi * lx).sum()
rhs = (-F * x).sum()
t4a = abs(lhs - rhs) / abs(lhs)
w = (0, 0, 0, 0)
rho = np.zeros((S,) * 4)
rho[w] = 1.0
rho[c] -= 1.0
F, _ = field(rho, S, lam)
xs = np.where(MK, np.sign(-F), 0.0)
lxs, _ = lam_direct(xs, S, c)
t4b = abs(lxs[w] - np.abs(F).sum()) / np.abs(F).sum()
T4ok = t4a <= 1e-8 and t4b <= 1e-8 and lxs[w] <= 2 * M
out.append(f"T4 adjointness (n = 2, CG {it4} its): rel. diff {t4a:.1e}; dual bound: lambda(x)(corner) = {lxs[w]:.4f}, "
           f"||F||_1 = {np.abs(F).sum():.4f} (rel. {t4b:.1e}), 2M = {2 * M}: {'PASS' if T4ok else 'FAIL'}")

# ---------- T5: Q_X combinatorics (d = 4, n = 27) ----------
T5ok = True
n5 = 27
for s in (1, 3, 9):
    ys = np.arange(-3 * n5, 3 * n5 + 1, s)
    vals = sig5(ys / n5)
    S1 = vals.sum()
    D1 = np.abs(sig5((ys + s) / n5) - vals).sum()
    tot = D4 * D1 * S1 ** (D4 - 1)
    bound = 240 * (n5 / s) ** 3
    T5ok &= tot <= bound
    out.append(f"T5 n = 27, s = {s}: sum|d ev chi| = {tot:.2f}, (n/s)^3 = {(n5 / s) ** 3:.0f}, ratio {tot / (n5 / s) ** 3:.4f} "
               f"(bound 240)")
out.append(f"T5 Q_X bound (f): {'PASS' if T5ok else 'FAIL'}")

# ---------- T6: composite Gamma_E^T on a torus (coarse side 5, n = 3) ----------
n = 3
Tc = 5
L = n * Tc
S = 4 * n + 1
M = 2 * S
lam = symbol(M)
HW = 2 * n
loc = np.arange(S) - HW
chi_box = np.ones((S,) * 4)
for mu in range(D4):
    sh = [1] * D4
    sh[mu] = S
    chi_box = chi_box * sig5(loc / n).reshape(sh)
j = np.zeros((D4,) + (L,) * 4)
gridL = np.indices((L,) * 4)
dist = np.max(np.minimum(gridL, L - gridL), axis=0)
near = dist <= 1
j[:, near] = rng.standard_normal((D4, int(near.sum())))
j /= np.abs(j).max()
Dg = dstar(j)
xg = np.zeros((D4,) + (L,) * 4)
near3 = dist <= 3
xg[:, near3] = rng.standard_normal((D4, int(near3.sum())))
GT = np.zeros((D4,) + (L,) * 4)
P = np.zeros((D4,) + (L,) * 4)
IchiD = np.zeros((L,) * 4)
pair = 0.0
Qmax = 0.0
MK = mask1(S)
cc = (HW,) * D4
rho_c = np.zeros((S,) * 4)
rho_c[cc] = 1.0
Ac, _ = field(rho_c, S, lam)          # d a_c with the uniform background (mean-zero Green function)
acmax = np.abs(Ac).max()
its6 = []
for X in np.ndindex(3, 3, 3, 3):
    cX = (np.array(X) - 1) * n % L
    gidx = [(cX[mu] + loc) % L for mu in range(D4)]
    ix = np.ix_(*gidx)
    psi = chi_box * Dg[ix]
    QX = psi.sum()
    Qmax = max(Qmax, abs(QX))
    IchiD[tuple(cX)] += QX
    rho = psi.copy()
    rho[cc] -= QX
    F, _ = field(rho, S, lam)
    for mu in range(D4):
        GT[mu][ix] += -F[mu]
        P[mu][ix] += QX * Ac[mu]
    xb = np.stack([xg[mu][ix] for mu in range(D4)])
    xb = np.where(MK, xb, 0.0)
    lx, itx = lam_direct(xb, S, cc)
    its6.append(itx)
    pair += (psi * lx).sum()
Bp = GT - P
t6i = np.abs(dstar(GT) - (-Dg + IchiD)).max() / np.abs(Dg).max()
t6ii = abs(pair - (GT * xg).sum()) / abs(pair)
l1GT = np.abs(GT).sum()
l1j = np.abs(j).sum()
t6iii = l1GT <= 4 * M * l1j
supb = 5 ** 4 * ((M / 4) * np.abs(Dg).max() + 32 * Qmax)
t6iv = np.abs(GT).max() <= supb
T6ok = t6i <= 1e-9 and t6ii <= 1e-8 and t6iii and t6iv
out.append(f"T6 composite (coarse side 5, n = 3, 81 boxes, CG its {min(its6)}-{max(its6)}): (i) d*Gamma^T D vs -D + I^T D "
           f"{t6i:.1e}; (ii) adjointness {t6ii:.1e}; (iii) ||Gamma^T D||_1 = {l1GT:.2f} <= 4M||j||_1 = {4 * M * l1j:.1f}; "
           f"(iv) sup = {np.abs(GT).max():.4f} <= {supb:.1f}; split: sup|P| = {np.abs(P).max():.4f}, sup|B| = "
           f"{np.abs(Bp).max():.4f}, max|Q_X| = {Qmax:.4f}, ||D||_inf = {np.abs(Dg).max():.4f}, sup|A_c| = {acmax:.4f} "
           f"(<= 32): {'PASS' if T6ok and acmax <= 32 else 'FAIL'}")
T6ok = T6ok and acmax <= 32

# ---------- controls ----------
C1ok = all(0.05 <= v <= 0.2 for v in C1v.values())
out.append("C1 control (psi = 1 on N_X): sup/(2n+1)^4 = " + ", ".join(f"{C1v[k]:.4f}" for k in NS)
           + f": {'PASS (grows like n^d, as predicted)' if C1ok else 'FAIL'}")
inc = all(C2v[NS[i + 1]] > C2v[NS[i]] for i in range(len(NS) - 1))
r1 = (C2v[4] - C2v[2]) / np.log(2)
r2 = (C2v[6] - C2v[3]) / np.log(2)
C2ok = inc and 0.5 <= r2 / r1 <= 2.0
out.append("C2 control (adjacent dipole at c, GE-F3): ||F||_1 = " + ", ".join(f"{C2v[k]:.4f}" for k in NS)
           + f"; increments per log 2: {r1:.4f}, {r2:.4f}: {'PASS (log growth, as predicted)' if C2ok else 'FAIL'}")
allp = T0ok and T1ok and T2ok and T3ok and T4ok and T5ok and T6ok and C1ok and C2ok
out.append(f"VERDICT: {'ALL PASS' if allp else 'NOT ALL PASS'} (T0-T6, C1, C2)")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
