#!/usr/bin/env python3
"""C2_check ck3: lattice spot checks (claim 3), m = 1.0.

X1  Independent route for C2's one-loop kernel Pi(disc, K): build the lattice operator D[h] in POSITION space on a small
    periodic L^4 lattice directly from the transcription definitions (exact sqrt g g^{-1}, no h-expansion, no alpha/beta
    symbol tables), compute W(eps) = 1/2 log det D[eps h] exactly for h = 2 eps A cos(K.x), and compare the eps^2
    coefficient (5-point finite difference) with A^T Pi(K) A from C2's momentum-space formula (imported from the runner
    source) evaluated on the same periodic momentum set.  Done for S, M1, M2 and two K.
X2  Fierz-Pauli normalisation: my own sympy expansion of [sqrt g R]^(2) (4D, plane wave) vs C2's hand-coded FP(n).
X3  From C2's saved symbols (m = 1.0, N = 16): recompute Ward ratios and c_EH with my FP and gauge vectors; compare to the
    log; recompute <phi^2>.
X4  M1 - M2 EH projection from the placement tadpole (my own position-space reading: bond factor cos^2(K_mu/2), plaquette
    cos^2(K_mu/2) cos^2(K_nu/2) on the seagull only), compared with the saved symbols.
"""
import sys, os, time, itertools
import numpy as np
import sympy as sp

T0 = time.time()
RES = {"pass": 0, "fail": 0}
def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time()-T0:.1f}s] {msg}", flush=True)

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "C2_seagull_from_closure", "c2_lattice_scalar.py")
src = open(SRC).read()
src = src[:src.index("DIRS = [")]          # definitions only (no runs)
m = 1.0
ns = {"__name__": "c2mod"}
sys_argv = sys.argv
sys.argv = ["x", str(m), "16"]
exec(compile(src, SRC, "exec"), ns)
sys.argv = sys_argv
Pi_c2, E, IDX, FP_c2, gauge_vecs = ns["Pi"], ns["E"], ns["IDX"], ns["FP"], ns["gauge_vecs"]
d = 4

# ------------------------------------------------------------------ X1 position-space exact log det
Lx = 6
sites = list(itertools.product(range(Lx), repeat=4))
sid = {s: i for i, s in enumerate(sites)}
Ns = len(sites)
def sh(x, mu, s=1):
    y = list(x); y[mu] = (y[mu] + s) % Lx; return tuple(y)
def Wfull(hm):
    g = np.eye(4) + hm
    return np.sqrt(np.linalg.det(g)) * np.linalg.inv(g)
def sqrtg(hm):
    return np.sqrt(np.linalg.det(np.eye(4) + hm))
def grad_vec(x, mu, kind):
    """returns dict site->coef for a difference operator at x"""
    if kind == "+":
        return {sid[sh(x, mu)]: 1.0, sid[x]: -1.0}
    if kind == "-":
        return {sid[x]: 1.0, sid[sh(x, mu, -1)]: -1.0}
def add_bilinear(Dm, w, u, v):
    """S += 1/2 w (u.phi)(v.phi)  ->  D += w/2 (u v^T + v u^T)"""
    for i, a in u.items():
        for j, b in v.items():
            Dm[i, j] += 0.5 * w * a * b
            Dm[j, i] += 0.5 * w * a * b
def build_D(disc, hfield):
    Dm = np.zeros((Ns, Ns))
    for x in sites:
        i0 = sid[x]
        Dm[i0, i0] += m * m * sqrtg(hfield[x])
        if disc == "S":
            Wx = Wfull(hfield[x])
            for mu in range(4):
                for kd in "+-":
                    gv = grad_vec(x, mu, kd)
                    add_bilinear(Dm, 0.5 * Wx[mu, mu], gv, gv)
            for mu in range(4):
                for nu in range(4):
                    if mu == nu:
                        continue
                    for s1 in "+-":
                        for s2 in "+-":
                            add_bilinear(Dm, 0.25 * Wx[mu, nu], grad_vec(x, mu, s1), grad_vec(x, nu, s2))
        else:
            for mu in range(4):
                c = [x, sh(x, mu)]
                Wb = Wfull(np.mean([hfield[y] for y in c], 0)) if disc == "M1" else np.mean([Wfull(hfield[y]) for y in c], 0)
                gv = grad_vec(x, mu, "+")
                add_bilinear(Dm, Wb[mu, mu], gv, gv)
            for mu in range(4):
                for nu in range(mu + 1, 4):
                    c = [x, sh(x, mu), sh(x, nu), sh(sh(x, mu), nu)]
                    Wp = Wfull(np.mean([hfield[y] for y in c], 0)) if disc == "M1" else np.mean([Wfull(hfield[y]) for y in c], 0)
                    # plaquette gradients: mean of the two parallel bond differences
                    gm, gn = {}, {}
                    for (base, dirn, out) in ((x, mu, gm), (sh(x, nu), mu, gm), (x, nu, gn), (sh(x, mu), nu, gn)):
                        for kk, vv in grad_vec(base, dirn, "+").items():
                            out[kk] = out.get(kk, 0) + 0.5 * vv
                    add_bilinear(Dm, 2 * Wp[mu, nu], gm, gn)
    return Dm
def Wlog(disc, A, Kv, eps):
    hf = {x: 2 * eps * A * np.cos(np.dot(Kv, x)) for x in sites}
    return 0.5 * np.linalg.slogdet(build_D(disc, hf))[1]
pgrid = 2 * np.pi * np.arange(Lx) / Lx
P = np.stack(np.meshgrid(pgrid, pgrid, pgrid, pgrid, indexing="ij"), -1).reshape(-1, 4)
rng = np.random.default_rng(11)
worst = 0.0
for Kn in ([1, 0, 0, 0], [1, 1, 0, -1]):
    Kv = 2 * np.pi * np.array(Kn, float) / Lx
    for disc in ("S", "M1", "M2"):
        Pi_mat = Pi_c2(disc, Kv, P, "full")[0]
        for trial in range(2):
            a = rng.normal(size=10)
            A = sum(c * Ea for c, Ea in zip(a, E))
            dl = 2e-3
            f = {k_: Wlog(disc, A, Kv, k_ * dl) for k_ in (-2, -1, 0, 1, 2)}
            c2 = (-f[2] + 16 * f[1] - 30 * f[0] + 16 * f[-1] - f[-2]) / (12 * dl * dl) / 2
            pred = (a @ Pi_mat @ a).real
            rel = abs(c2 - pred) / abs(pred)
            worst = max(worst, rel)
            print(f"   K = {Kn} {disc:2s} trial {trial}: position-space eps^2 coeff {c2:.8f}  vs C2 formula {pred:.8f}  rel {rel:.1e}")
check("X1", worst < 1e-5, f"C2's momentum-space second variation (seagull + bubble, D1A/D1B placements, symmetrisation) equals "
      f"the exact position-space 1/2 log det for S, M1, M2 on a periodic 6^4 lattice (max rel dev {worst:.1e})")

# ------------------------------------------------------------------ X2 FP normalisation via sympy
kk = sp.symbols("k0:4", real=True)
Z, ep = sp.symbols("Z ep")
As = {ab: sp.Symbol(f"A{ab[0]}{ab[1]}") for ab in IDX}
Bs = {ab: sp.Symbol(f"B{ab[0]}{ab[1]}") for ab in IDX}
Am = sp.Matrix(4, 4, lambda i, j: As[(min(i, j), max(i, j))])
Bm = sp.Matrix(4, 4, lambda i, j: Bs[(min(i, j), max(i, j))])
H = ep * (Am * Z + Bm / Z)
def tr2(e):
    e = sp.expand(e); return sum(e.coeff(ep, j) * ep ** j for j in range(3))
def Dx(e, mu):
    e = sp.expand(e); out = 0
    for t in sp.Add.make_args(e):
        out += t * sp.I * t.as_powers_dict().get(Z, 0) * kk[mu]
    return sp.expand(out)
g = sp.eye(4) + H
gi = (sp.eye(4) - H + H * H).applyfunc(tr2)
trH = H.trace()
sq = tr2(1 + trH / 2 + trH ** 2 / 8 - (H * H).trace() / 4)
dg = [[[Dx(g[a, b], c) for c in range(4)] for b in range(4)] for a in range(4)]
Gam = [[[tr2(sum(gi[l, mm] * (dg[mm][a][b] + dg[mm][b][a] - dg[a][b][mm]) for mm in range(4)) / 2) for b in range(4)]
        for a in range(4)] for l in range(4)]
Rsc = 0
for a in range(4):
    for b in range(4):
        Rab = sum(Dx(Gam[l][a][b], l) - Dx(Gam[l][a][l], b) for l in range(4))
        Rab += sum(Gam[l][l][mm] * Gam[mm][a][b] - Gam[l][b][mm] * Gam[mm][a][l] for l in range(4) for mm in range(4))
        Rsc += gi[a, b] * tr2(Rab)
sgR2 = sp.expand(sp.expand(tr2(sq * tr2(Rsc))).coeff(ep, 2) * Z ** 2).coeff(Z, 2)
def FP_mine(n):
    sub = {kk[i]: float(n[i]) for i in range(4)}
    e = sp.expand(sgR2.subs(sub))
    Mx = np.zeros((10, 10))
    for i, ab in enumerate(IDX):
        for j, cd in enumerate(IDX):
            Mx[i, j] = float(e.coeff(As[ab]).coeff(Bs[cd]))
    return Mx
dat = np.load(os.path.join(HERE, "..", "C2_seagull_from_closure", "c2_lattice_symbols_m1.0_N16.npz"))
DIRS = dat["dirs"]
fpdev = max(np.abs(FP_mine(n) - FP_c2(n)).max() / np.abs(FP_c2(n)).max() for n in DIRS[:3])
check("X2", fpdev < 1e-10, f"C2's hand-coded Fierz-Pauli kernel equals the sympy [sqrt g R]^(2) cross kernel (rel dev {fpdev:.1e}); "
      "so c_EH in 'W contains -c_EH FP' is 1/(16 pi G) in the Euclidean convention")
FPs = [FP_mine(n) for n in DIRS]

# ------------------------------------------------------------------ X3 recompute log numbers from saved symbols
NG = 16
pp = -np.pi + (np.arange(NG) + 0.5) * 2 * np.pi / NG
Pm = np.stack(np.meshgrid(pp, pp, pp, pp, indexing="ij"), -1).reshape(-1, 4)
phat2 = np.sum((2 * np.sin(Pm / 2)) ** 2, -1)
phi2 = np.mean(1 / (phat2 + m * m))
cov = phi2 / 12
def gvecs(n):
    out = []
    for nu in range(4):
        hm = np.outer(n, np.eye(4)[nu]) + np.outer(np.eye(4)[nu], n)
        out.append(np.array([hm[a, b] for (a, b) in IDX]))
    return out
logv = {"S": (0.650, 1.191, -0.002855), "M1": (0.431, 1.863, 0.003332), "M2": (0.431, 1.191, -0.004564)}
ok3 = abs(phi2 - 0.127112) < 1e-6
for disc in ("S", "M1", "M2"):
    Ms = dat[disc]
    wr = [max(np.abs(Mx @ v).max() for v in gvecs(n)) / np.abs(Mx).max() for Mx, n in zip(Ms, DIRS)]
    A_ = np.concatenate([F.ravel() for F in FPs]); y = np.concatenate([Mx.ravel() for Mx in Ms])
    cE = -A_ @ y / (A_ @ A_)
    print(f"   {disc:2s}: Ward ratio {min(wr):.3f}..{max(wr):.3f}  c_EH {cE:.6f} ({cE/cov:+.3f} x cov ref)   log: {logv[disc]}")
    ok3 &= abs(min(wr) - logv[disc][0]) < 2e-3 and abs(max(wr) - logv[disc][1]) < 2e-3 and abs(cE - logv[disc][2]) < 2e-6
check("X3", ok3, f"saved m = 1.0 symbols reproduce the logged Ward ranges and c_EH with my FP and gauge vectors; <phi^2> = {phi2:.6f}")

# ------------------------------------------------------------------ X4 placement tadpole projected on EH
def W2bil(A, B):
    """symmetric bilinear second-order part of sqrt g g^{-1} (from exact numerical differentiation, not C2's W2)."""
    e = 1e-3
    f = lambda s, t: Wfull(s * A + t * B)
    return (f(e, e) - f(e, -e) - f(-e, e) + f(-e, -e)) / (4 * e * e)
Gp = 1 / (phat2 + m * m)
t_bond = [np.mean(Gp * (2 * np.sin(Pm[:, mu] / 2)) ** 2) for mu in range(4)]          # <(D+_mu phi)^2>
t_plaq = {}
for mu in range(4):
    for nu in range(mu + 1, 4):
        a_ = 0.5 * (np.exp(1j * Pm[:, mu]) - 1) * (1 + np.exp(1j * Pm[:, nu]))
        b_ = 0.5 * (np.exp(1j * Pm[:, nu]) - 1) * (1 + np.exp(1j * Pm[:, mu]))
        t_plaq[(mu, nu)] = np.mean(Gp * (a_.conj() * b_).real)                         # <Dp_mu phi Dp_nu phi>
print(f"   bond tadpole <(D_mu phi)^2> = {t_bond[0]:.6f};  plaquette tadpoles max |.| = {max(abs(v) for v in t_plaq.values()):.1e}")
W2E = [[W2bil(EA, EB) for EB in E] for EA in E]
def diff_mine(n):
    """k^2 coefficient of Pi_M1 - Pi_M2: seagull 1/2 x 2 x W2bil x tadpole x (|avg|^2 - 1)_k^2"""
    out = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            Wb = W2E[i][j]
            v = sum(Wb[mu, mu] * t_bond[mu] * (-0.25 * n[mu] ** 2) for mu in range(4))
            v += sum(2 * Wb[mu, nu] * t_plaq[(mu, nu)] * (-0.25 * (n[mu] ** 2 + n[nu] ** 2)) for (mu, nu) in t_plaq)
            out[i, j] = v
    return out
res = max(np.abs((a_ - b_) - diff_mine(n)).max() for a_, b_, n in zip(dat["M1"], dat["M2"], DIRS))
scale = max(np.abs(a_ - b_).max() for a_, b_ in zip(dat["M1"], dat["M2"]))
A_ = np.concatenate([F.ravel() for F in FPs])
dc = -A_ @ np.concatenate([diff_mine(n).ravel() for n in DIRS]) / (A_ @ A_)
check("X4", res / scale < 1e-4, f"M1 - M2 = bond-tadpole x (cos^2(K/2) - 1) on the seagull only (my W2 by numerical "
      f"differentiation; rel residual {res/scale:.1e}); its EH projection {dc:.6f} = {dc/cov:+.3f} x covariant ref -- "
      f"an O(1) shift of 1/G from O(a^2) leg placement")
print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time()-T0:.1f}s)")
