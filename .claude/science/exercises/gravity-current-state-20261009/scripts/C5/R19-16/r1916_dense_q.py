"""R19-16 dense checks aimed at the repaired regions, r from argv:
 D1  10000 pairs: k2 uniform on T^3, k1 = wrap(k2 + q), q = random direction x 10^U(-16, 0.5), each component zeroed w.p. 0.2
     (forward region, q_j = 0 planes, wrapped across BZ faces);
 D2  10000 pairs: both legs log-uniform in size 1e-12..pi with random exact-zero components (k_j = 0 planes; soft legs);
     W1 on the physical block by lib199.w1_resid and by an independent SVD transverse-frame contraction.
 L1  line scans of the kernel M(m + t e_j/2, m - t e_j/2), t on 801 points across (a) [-2e-7, 2e-7] (old 1e-7 switch) at the
     referee midpoint, (b) the same at a transition midpoint next to a face, (c) [1 - 1e-6, 1 + 1e-6] (graviton plateau edge, where q/dsym(q) leaves 1);
     max second difference |M(t+h) - 2M(t) + M(t-h)| -- a jump shows up as O(jump), smooth as O(M'' h^2) + rounding.
     Done for the REPAIRED kernel and, as a control, for the ORIGINAL lib199 kernel."""
import sys, time, numpy as np
import lib1916 as R
L = R.L
r = float(sys.argv[1]) if len(sys.argv) > 1 else 0.1
rng = np.random.default_rng(19160 + int(100*r)); t0 = time.time()
def tframe(k):
    s = L.sig(k); _, _, vh = np.linalg.svd(s.reshape(1, 3), full_matrices=True); e = vh[1:].T
    out = np.zeros((6, 4)); out[:3, :2] = e; out[3:, 2:] = e; return out
def check(k1, k2):
    M, used, _ = L.glued(k1, k2, r, parts=True)
    res = L.w1_resid(M, k1, k2)
    h1, h2 = L.hmat(L.sig(k1)), L.hmat(L.sig(k2)); d = L.dsym(L.wrap(k1 - k2)); q1, q2 = tframe(k1), tframe(k2)
    ind = max(np.abs(q1.T @ (h1 @ M[0, nu] - M[0, nu] @ h2 - sum(d[j]*M[1+j, nu] for j in range(3))) @ q2).max() for nu in range(4))
    return max(x[0] for x in res), max(x[1] for x in res), ind, used, bool(np.isfinite(M).all())
def run(name, gen, n=10000):
    mx = [0.0, 0.0, 0.0]; cnt = {}; fin = True
    for _ in range(n):
        k1, k2 = gen()
        if np.linalg.norm(k1) == 0 or np.linalg.norm(k2) == 0: continue
        a, rel, ind, used, f = check(k1, k2); fin &= f
        for u in used: cnt[u] = cnt.get(u, 0) + 1
        mx = [max(mx[0], a), max(mx[1], rel), max(mx[2], ind)]
    print(f'r={r} {name:44s}: max abs {mx[0]:.2e}, rel {mx[1]:.2e}, independent-frame abs {mx[2]:.2e}; finite {fin}; pieces {cnt} [{time.time()-t0:.0f}s]', flush=True)
def gen1():
    k2 = rng.uniform(-np.pi, np.pi, 3); u = rng.normal(size=3); u /= np.linalg.norm(u)
    q = u*10**rng.uniform(-16, 0.5); q[rng.uniform(size=3) < 0.2] = 0.0
    return L.wrap(k2 + q), k2
def logleg():
    v = rng.normal(size=3); v /= np.linalg.norm(v); k = v*10**rng.uniform(-12, np.log10(np.pi))
    k[rng.uniform(size=3) < 0.2] = 0.0
    return L.wrap(k)
run('D1 forward-region q 1e-16..3, zero planes, faces', gen1)
run('D2 log-uniform legs 1e-12..pi, k_j = 0 planes', lambda: (logleg(), logleg()))

def scan(m, ax, t):
    out = []
    for tt in t:
        k1, k2 = m.copy(), m.copy(); k1[ax] += tt/2; k2[ax] -= tt/2
        out.append(L.glued(L.wrap(k1), L.wrap(k2), r))
    M = np.array(out); d2 = np.abs(M[2:] - 2*M[1:-1] + M[:-2]).reshape(len(t) - 2, -1).max(1)
    i = int(np.argmax(d2)); return d2.max(), t[i + 1], np.abs(M).max()
lines = (('(a) referee midpoint, t in +-2e-7', np.array([3.05, 1.0, 0.7]), 0, np.linspace(-2e-7, 2e-7, 801)),
         ('(b) transition, near face, t in +-2e-7', np.array([0.3, -3.1415, 3.0]), 2, np.linspace(-2e-7, 2e-7, 801)),
         ('(c) referee midpoint, t in 1 +- 1e-6', np.array([3.05, 1.0, 0.7]), 0, np.linspace(1 - 1e-6, 1 + 1e-6, 801)))
for tag, patchfn in (('REPAIRED', R.patch), ('ORIGINAL lib199', R.unpatch)):
    patchfn()
    for name, m, ax, t in lines:
        d2, tw, sc = scan(m, ax, t)
        print(f'L1 {tag:16s} {name:40s}: max |second difference| {d2:.2e} at t = {tw:+.4e} (|M| max {sc:.1f})', flush=True)
R.patch()
print(f'time {time.time() - t0:.0f}s')
