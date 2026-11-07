#!/usr/bin/env python3
"""Cross-check of fi_map against the attempt's pure-Python map, and a finite-difference test of the gradient.
PASS-X: |W - 1| agrees to 1e-9 on random fields at L = 3 (rule and fixed), and on a rough field that moves x_0. CHARGE: a random gauge transformation leaves |W - 1| fixed to 1e-9.
PASS-G: directional derivative of |W - 1|^2 by autograd agrees with central differences to 1e-5 relative."""
import importlib.util, pathlib, random, sys, time
import numpy as np, torch
import fi_map as fm
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("old", HERE.parent / "hard-core--independent_field_ineq.py")
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)

def rand_links(L, a, seed, patch=None):
    torch.manual_seed(seed)
    U = fm.flat_links(L)
    out = []
    for u in U:
        v = torch.randn(*u.shape[:-1], 3) * a
        th = v.norm(dim=-1, keepdim=True)
        q = torch.cat((torch.cos(th), torch.sin(th) * v / th.clamp_min(1e-12)), -1)
        if patch is not None:
            mask = torch.zeros(u.shape[:-1], dtype=torch.bool)
            mask[patch] = True
            h = torch.randn(*u.shape)
            h = h / h.norm(dim=-1, keepdim=True)
            q = torch.where(mask[..., None], h, q)
        out.append(q)
    return out

def old_field(U, L):
    o = (L - 1) // 2
    def get(s, mu):
        idx = list(c + o for c in s)
        t = U[mu]
        if any(i < 0 or i >= t.shape[k] for k, i in enumerate(idx)):
            return old.ONE
        return tuple(float(c) for c in t[tuple(idx)])
    return old.Field(get)

L = 3
ok = True
old.EPS_RULE = 0.05; old.S_RULE = 0.25
for name, U in (("noise .02", rand_links(L, 0.02, 1)), ("noise .3", rand_links(L, 0.3, 2)),
                ("patch", rand_links(L, 0.01, 3, patch=(slice(0, 2), slice(1, 3), slice(0, 2), slice(0, 2)))),
                ("haar-ish 1.0", rand_links(L, 1.0, 4))):
    for base in ("rule", "fixed"):
        t0 = time.time(); e = fm.evaluate(U, L, 0.05, 0.25, base); t1 = time.time()
        w_old, m_old = old.plaquette_W(old_field(U, L), L, base); t2 = time.time()
        d = abs(e["w1"] - w_old); ok &= d < 1e-9
        print(f"{name:14s} {base:5s} new {e['w1']:.12f} old {w_old:.12f} diff {d:.1e} bases {sorted(e['bases'].values())[:4]} t {t1-t0:.3f} {t2-t1:.1f}", flush=True)
print("PASS-X" if ok else "FAIL-X")
# gauge covariance
U = rand_links(5, 0.3, 7)
torch.manual_seed(8)
g = torch.randn(*fm.shape_box(5), 4); g = g / g.norm(dim=-1, keepdim=True)
V = []
for mu, u in enumerate(U):
    gl = g.narrow(mu, 0, g.shape[mu] - 1); gr = g.narrow(mu, 1, g.shape[mu] - 1)
    V.append(fm.qmul(fm.qmul(gl, u), fm.qconj(gr)))
e1 = fm.evaluate(U, 5, 1e-9, 0.25, "fixed"); e2 = fm.evaluate(V, 5, 1e-9, 0.25, "fixed")
print("gauge L=5 fixed", e1["w1"], e2["w1"], "PASS" if abs(e1["w1"] - e2["w1"]) < 1e-9 else "FAIL")
e1 = fm.evaluate(U, 5, 1e-3, 0.25); e2 = fm.evaluate(V, 5, 1e-3, 0.25)
print("gauge L=5 rule", e1["w1"], e2["w1"], e1["bases"][(0, 0)], e2["bases"][(0, 0)], "PASS" if abs(e1["w1"] - e2["w1"]) < 1e-9 else "FAIL")
# gradient
L = 5
U = rand_links(L, 0.1, 9)
bases = {k: (2, 2, 2, 2) for k in ((0, 0), (1, 0), (0, 1), (1, 1))}
Q = [u.clone().requires_grad_(True) for u in U]
def F(Q):
    V = [q / q.norm(dim=-1, keepdim=True) for q in Q]
    W, _ = fm.coarse_W(V, L, bases)
    return ((W - W.new_tensor([1.0, 0, 0, 0])) ** 2).sum()
t0 = time.time(); val = F(Q); val.backward(); print("grad time L=5", time.time() - t0)
D = [torch.randn(*u.shape) for u in U]
dd = sum(float((q.grad * d).sum()) for q, d in zip(Q, D))
h = 1e-5
with torch.no_grad():
    fd = (float(F([u + h * d for u, d in zip(U, D)])) - float(F([u - h * d for u, d in zip(U, D)]))) / (2 * h)
print("autograd", dd, "fd", fd, "PASS-G" if abs(dd - fd) <= 1e-5 * abs(fd) else "FAIL-G")
# sheet at centre
for L in (3, 5, 7, 9, 11):
    U = fm.flat_links(L)
    U[0][L - 1, L:, ...] = torch.tensor([-1.0, 0, 0, 0])
    t0 = time.time(); e = fm.evaluate(U, L, 0.02 / L ** 2, 0.02)
    print(f"sheet L={L} w1 {e['w1']:.4f} ratio_a {e['ratio_a']:.4f} ratio_c {e['ratio_c']:.4f} nrough {e['nrough']} t {time.time()-t0:.3f}", flush=True)
