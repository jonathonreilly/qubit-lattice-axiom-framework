"""A51 anal51b: (1) profile J(d) of the best full-reach rule (Casimir-removed metric) with jackknife errors and a
power-law fit; (2) q-orbit structure-factor operators P_Q: their relative variance vs the Gaussian estimate S(Q)^2;
(3) Haldane-Shastry-like ansatz J(d) = s(d) / D(d)^alpha, D^2 = sum_a (L/pi)^2 sin^2(pi d_a / L), alone and with the
8 star four-spin terms optimized on top; (4) the parton's best rule evaluated on the reference states.
Usage: anal51b.py L parton_spec ref1,ref2,...  Saves best rules to rules51_<L>.npz."""
import sys, signal, numpy as np
signal.alarm(280)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from anal51 import *

L = int(sys.argv[1]); pspec = sys.argv[2]; refs = sys.argv[3].split(",") if len(sys.argv) > 3 else []
ks, m, F4, G, Gm = metrics(L); nc = len(ks); N = L ** 3; n = len(G)
K = np.array(ks, float); dn = np.sqrt((K ** 2).sum(1)); par = K.sum(1).astype(int) % 2
S, nf = load(L, pspec); print(f"L={L} {pspec}: {len(S)} samples")
C = covm(S, N)
rules = {}
for key, idx in (("B", list(range(nc))), ("B4", list(range(nc + 8)))):
    o = lam_jk(S, N, idx, Gm, nvec=True)
    # gauge: at full reach the rule is defined modulo the Casimir (J_c -> J_c + mu for all classes); fix mu by
    # minimizing the far-weighted norm sum_c m_c |d_c|^2 (J_c - mu)^2 (the most local representative), then J_NN = 1
    w2 = m * dn ** 2
    def fix(vec):
        v = np.zeros(n); v[idx] = vec; v[:nc] -= (w2 @ v[:nc]) / w2.sum(); return v / v[0]
    v = fix(o["vec"]); vjs = np.array([fix(x) for x in o["vj"]])
    e = np.sqrt((15 / 16) * ((vjs - vjs.mean(0)) ** 2).sum(0)); rules[key] = v
    print(f"\n[{key}] full reach, Casimir-removed metric: lam = {o['lam']:.4g} +- {o['err']:.2g} (bias-corr {o['corr']:.4g}); lam2 = {o['lam2']:.4g}")
    print("  class      |d|   m  par   J(d)/J_NN  +- err")
    for c in range(nc):
        print(f"  {str(ks[c]):10s} {dn[c]:5.2f} {m[c]:3d}  {par[c]}  {v[c]:+.4f}  {e[c]:.4f}")
    if key == "B4":
        print("  four-spin (A49 normalized units, same scale): " + " ".join(f"{F4[k][0]}:{v[nc+k]:+.3f}({e[nc+k]:.3f})" for k in range(8)))
    # the Casimir-removed rule is defined modulo the Casimir: shift J_c -> J_c - mu with mu fixed by <rule, Cas> = 0
    sig = np.abs(v[:nc]) > 2 * e[:nc]
    sel = sig & (dn > 1.01)
    if sel.sum() >= 3:
        A = np.c_[np.ones(sel.sum()), -np.log(dn[sel])]; w = 1. / np.maximum(e[:nc][sel] / np.abs(v[:nc][sel]), 0.02)
        coef, *_ = np.linalg.lstsq(A * w[:, None], np.log(np.abs(v[:nc][sel])) * w, rcond=None)
        print(f"  power-law fit |J| = A/|d|^alpha over {sel.sum()} significant classes beyond NN: alpha = {coef[1]:.2f}, A = {np.exp(coef[0]):.3f}")
    for p in (0, 1):
        s_ = sel & (par == p)
        if s_.sum() >= 2:
            sg = np.sign(v[:nc][s_]); print(f"  parity |d|_1 {'odd ' if p else 'even'}: {s_.sum()} significant, signs + {int((sg>0).sum())} / - {int((sg<0).sum())}")
    print(f"  insignificant classes (|J| < 2 err): {int((~sig).sum())} of {nc}")

# (2) q-orbit operators
qk = [(0, 0, 0)] + ks
grid = np.array(list(itertools.product(range(L), repeat=3)))
lab = {k: i for i, k in enumerate(qk)}
ql = np.array([lab[tuple(r)] for r in np.sort(fold(grid, L), axis=1)])
F = np.zeros((len(qk), nc))
for c in range(nc):
    F[:, c] = np.bincount(ql, weights=np.cos(2 * np.pi * grid @ K[c] / L), minlength=len(qk))
ev = S[:, :nc].real.mean(0) / N; cnt = np.bincount(ql, minlength=len(qk))
Sbar = 1. + (2. / 3.) * (F @ ev) / cnt
out = []
for Qi in range(1, len(qk)):
    v = np.zeros(n); v[:nc] = F[Qi]; lamQ = (v @ C @ v) / (v @ Gm @ v); out.append((lamQ, Qi))
out.sort()
print("\n[q-orbits] relative variance of P_Q (Casimir-removed metric) vs Gaussian estimate Sbar(Q)^2; lowest 6:")
for lamQ, Qi in out[:6]:
    print(f"  Q = 2pi/L {qk[Qi]}: lam {lamQ:.4g}, Sbar {Sbar[Qi]:.4f}, Sbar^2 {Sbar[Qi]**2:.4g}")
print(f"  Sbar(Q) at the smallest Q {qk[1]}: {Sbar[1]:.4f}; maximum Sbar {Sbar.max():.3f} at {qk[int(np.argmax(Sbar))]}")

# (3) Haldane-Shastry-like ansatz
D2 = ((L / np.pi) ** 2 * np.sin(np.pi * K / L) ** 2).sum(1)
pats = {"af": np.ones(nc), "stag": np.where(par == 1, 1., -1.), "fit": np.sign(rules["B4"][:nc])}
print("\n[HS ansatz] J(d) = s(d)/D^alpha: lam (Casimir-removed) bilinear-only | + 8 star four-spin optimized")
for pn, sv in pats.items():
    line = []
    for al in (1, 2, 3, 4, 6):
        v = np.zeros(n); v[:nc] = sv / D2 ** (al / 2)
        l0 = (v @ C @ v) / (v @ Gm @ v)
        Bm = np.zeros((n, 9)); Bm[:, 0] = v; Bm[nc:nc + 8, 1:] = np.eye(8)
        l1 = releig(Bm.T @ C @ Bm, Bm.T @ Gm @ Bm)[0][0]
        line.append(f"a={al}: {l0:.3g} | {l1:.3g}")
    print(f"  s={pn:5s} " + ";  ".join(line))

# (3b) local cluster Casimirs: sum over stars of (star spin)^2 -> J1:J2:J(0,0,2) = 2:2:1; sum over unit cubes -> J1:J2:J(1,1,1) = 4:2:1
print("\n[cluster Casimirs] lam (Casimir-removed) bilinear-only | + 8 star four-spin optimized")
for nm, cfg in (("star", {(0, 0, 1): 2., (0, 1, 1): 2., (0, 0, 2): 1.}), ("cube", {(0, 0, 1): 4., (0, 1, 1): 2., (1, 1, 1): 1.})):
    v = np.zeros(n)
    for k, val in cfg.items(): v[ks.index(k)] = val
    l0 = (v @ C @ v) / (v @ Gm @ v)
    Bm = np.zeros((n, 9)); Bm[:, 0] = v; Bm[nc:nc + 8, 1:] = np.eye(8)
    print(f"  {nm}: {l0:.4g} | {releig(Bm.T @ C @ Bm, Bm.T @ Gm @ Bm)[0][0]:.4g}")

# (4) the parton's best rules on the references (relative variance, Casimir-removed metric)
for r in refs:
    Sr, _ = load(L, r)
    if Sr is None: continue
    Cr = covm(Sr, N)
    print(f"\n[ref {r}] {len(Sr)} samples: parton-best-rule lam  B {(rules['B'] @ Cr @ rules['B']) / (rules['B'] @ Gm @ rules['B']):.4g}, "
          f"B4 {(rules['B4'] @ Cr @ rules['B4']) / (rules['B4'] @ Gm @ rules['B4']):.4g}")
# (5) finite-reach rules (no gauge freedom): |d|^2 <= 4, <= 9, and every class with all components < L/2 ("inner")
extra = {}
for nm, cl_ in (("r4", [c for c in range(nc) if dn[c] ** 2 <= 4.01]), ("r9", [c for c in range(nc) if dn[c] ** 2 <= 9.01]),
                ("inner", [c for c in range(nc) if max(ks[c]) < L / 2])):
    for key, idx in (("B", cl_), ("B4", cl_ + list(range(nc, nc + 8)))):
        o = lam_jk(S, N, idx, Gm); v = np.zeros(n); v[idx] = o["vec"]; v /= v[0]; extra[f"{key}_{nm}"] = v
        print(f"[{key}_{nm}] {len(cl_)} classes: lam {o['lam']:.4g} +- {o['err']:.2g} (bias-corr {o['corr']:.4g}); J: " +
              " ".join(f"{ks[c]}:{v[c]:+.3f}" for c in cl_[:8]) + (" ..." if len(cl_) > 8 else ""))
# (6) profile of the finite-reach B4_inner rule (no gauge freedom) with jackknife errors and power-law fit
cl_ = [c for c in range(nc) if max(ks[c]) < L / 2]; idx = cl_ + list(range(nc, nc + 8))
o = lam_jk(S, N, idx, Gm, nvec=True)
vj = np.array([x / x[0] for x in o["vj"]]); v0 = o["vec"] / o["vec"][0]; ee = np.sqrt((15 / 16) * ((vj - vj.mean(0)) ** 2).sum(0))
print(f"\n[B4_inner profile] lam {o['lam']:.4g}; class |d| J/J_NN +- err:")
print("  " + "; ".join(f"{ks[c]} {dn[c]:.2f} {v0[q]:+.3f}({ee[q]:.3f})" for q, c in enumerate(cl_)))
print("  four-spin: " + " ".join(f"{F4[k][0]}:{v0[len(cl_)+k]:+.3f}({ee[len(cl_)+k]:.3f})" for k in range(8)))
J_ = v0[:len(cl_)]; E_ = ee[:len(cl_)]; D_ = dn[cl_]; sel = (np.abs(J_) > 2 * E_) & (D_ > 1.01)
if sel.sum() >= 3:
    A = np.c_[np.ones(sel.sum()), -np.log(D_[sel])]; w = np.abs(J_[sel]) / np.maximum(E_[sel], 1e-3)
    coef, *_ = np.linalg.lstsq(A * w[:, None], np.log(np.abs(J_[sel])) * w, rcond=None)
    print(f"  power law |J| = A/|d|^alpha over {sel.sum()} significant classes beyond NN: alpha = {coef[1]:.2f}; signs of significant: "
          f"+{int((J_[sel] > 0).sum())} / -{int((J_[sel] < 0).sum())}")
    ex = np.c_[np.ones(sel.sum()), -D_[sel]]
    ce, *_ = np.linalg.lstsq(ex * w[:, None], np.log(np.abs(J_[sel])) * w, rcond=None)
    r1 = np.sum((w * (A @ coef - np.log(np.abs(J_[sel])))) ** 2); r2 = np.sum((w * (ex @ ce - np.log(np.abs(J_[sel])))) ** 2)
    print(f"  exponential |J| = B exp(-|d|/xi): xi = {1/ce[1]:.2f}; weighted chi2 power {r1:.1f} vs exponential {r2:.1f}")
np.savez(f"rules51_{L}.npz", B=rules["B"], B4=rules["B4"], ks=np.array(ks), m=m, **extra)
