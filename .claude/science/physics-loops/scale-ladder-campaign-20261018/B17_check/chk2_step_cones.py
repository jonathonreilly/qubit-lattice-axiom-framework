"""B17 check, claim 2: rebuild the eight-node step S.R_L.U_H.U_L (runner Part 6, via steplib.py extracted
verbatim from the runner) and fit the full Weyl cone at every node by exact first-order degenerate
perturbation theory with the analytic Bloch derivative (independent of the runner's finite-q speed probe).

For a node at k0, quasi-energy E (W = e^{i theta} convention as in the runner):
  M_j = -i e^{-iE} Q^dag (dW/dk_j) Q  (2x2 Hermitian),  M_j = t_j 1 + sum_a V_aj tau_a
  theta - E = t.q +- sqrt(q^T g q),  g = V^T V  (cone metric, basis independent), chirality = sign det V.
"""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B17_check')
import steplib

d = steplib.build()
Ws_runner, Hk, blS, blL, UH, UL, kst = d['Ws'], d['Hk'], d['blS'], d['blL'], d['UH'], d['UL'], d['kst']
# NOTE (first run): the runner's Ws carries an extra 1/sqrt2 (blL is built from RLr = H0(0,1)/sqrt2 already), so
# Ws_runner = W/sqrt2 is not unitary; eigenphases (all the runner uses) are unaffected. Use the unitary W = sqrt2 Ws_runner.
Ws = lambda k: np.sqrt(2) * Ws_runner(k)
wrap = lambda x: np.angle(np.exp(1j * x))
NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

def dHk(bl, k, j):
    H = np.zeros((12, 12), complex)
    for sh, M in bl.items(): H += M * (1j * sh[j]) * np.exp(1j * np.dot(k, sh))
    return H
def dW(k, j):
    return (dHk(blS, k, j) @ Hk(blL, k) + Hk(blS, k) @ dHk(blL, k, j)) @ UH @ UL

kr = np.array([0.3, 1.1, -2.0])
check("runner quirk: Ws_runner(k) = W/sqrt2 (W W^dag = 1 for W = sqrt2 Ws_runner at generic k); phases unchanged",
      np.allclose(Ws(kr) @ Ws(kr).conj().T, np.eye(12)) and np.allclose(Ws_runner(kr) @ Ws_runner(kr).conj().T, np.eye(12) / 2))
# finite-difference sanity of the analytic derivative
k_t = np.array([0.31, -0.7, 1.2]); h = 1e-6
fd = max(np.abs((Ws(k_t + h * e) - Ws(k_t - h * e)) / (2 * h) - dW(k_t, j)).max() for j, e in enumerate(np.eye(3)))
check("analytic Bloch derivative of the step matches central differences", fd < 1e-7, f"max err {fd:.1e}")

PAU = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
def node_fit(k0, E):
    W0 = Ws(k0); ev, V = np.linalg.eig(W0)
    idx = np.where(np.abs(wrap(np.angle(ev) - E)) < 1e-7)[0]
    if len(idx) != 2: return None, len(idx)
    Q, _ = np.linalg.qr(V[:, idx])
    Ms = [-1j * np.exp(-1j * E) * Q.conj().T @ dW(k0, j) @ Q for j in range(3)]
    herm = max(np.abs(M - M.conj().T).max() for M in Ms)
    t = np.array([np.trace(M).real / 2 for M in Ms])
    Vm = np.array([[np.trace(PAU[a] @ M).real / 2 for M in Ms] for a in range(3)])  # V[a, j]
    return dict(t=t, V=Vm, g=Vm.T @ Vm, herm=herm, chi=int(np.sign(np.linalg.det(Vm)))), 2

ev_kst = np.angle(np.linalg.eigvals(Ws(kst)))
Es = sorted({round(float(x), 9) for x in ev_kst if np.sum(np.abs(wrap(ev_kst - x)) < 1e-7) == 2})
print("2-fold quasi-energies at k*:", Es, " full spectrum at k*:", np.round(np.sort(ev_kst), 6))
cube = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)]
def label(c):
    s = np.rint(c / (np.pi / 2)).astype(int); ks = np.rint(kst / (np.pi / 2)).astype(int)
    if (s == ks).all(): return 'k*'
    if (s == -ks).all(): return '-k*'
    for i in range(3):
        for base, nm in ((ks, 'k*'), (-ks, '-k*')):
            b = base.copy(); b[i] = -b[i]
            if (s == b).all(): return f"{nm}+pi e_{'xyz'[i]}"
    return '?'

rng = np.random.default_rng(7); dirs = rng.normal(size=(40, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
results = {}
for E in Es:
    print(f"\n=== node quasi-energy E = {E:+.6f} ===")
    res = {}
    for c in cube:
        f, n = node_fit(c, E)
        lab = label(c)
        if f is None:
            print(f"  {lab:12s}: {n} states at E"); res[lab] = None; continue
        sp, ax = np.linalg.eigh(f['g'])
        # finite-q dispersion check of the fitted cone
        errs = []
        for q in (1e-3,):
            for dd in dirs[:12]:
                th = wrap(np.angle(np.linalg.eigvals(Ws(c + q * dd))) - E); th = np.sort(th[np.abs(th) < 0.05])
                pred = np.sort([f['t'] @ dd * q + s * np.sqrt(dd @ f['g'] @ dd) * q for s in (-1, 1)])
                errs.append(np.abs(th - pred).max() / q if len(th) == 2 else np.inf)
        f.update(speeds=np.sqrt(sp), axes=ax, disp_err=max(errs))
        res[lab] = f
        print(f"  {lab:12s}: chi={f['chi']:+d} |tilt|={np.linalg.norm(f['t']):.1e} herm={f['herm']:.1e} "
              f"speeds={np.round(np.sqrt(sp), 7)} g=\n{np.round(f['g'], 7)}  disp rel err/q={max(errs):.1e}")
    results[E] = res

# ---- claims
E0 = min(Es, key=lambda x: abs(x - np.pi / 2))  # runner reports pi/2
R = results[E0]
check("the step has an exactly 2-fold level at E = pi/2 at all eight cube points (same quasi-energy)",
      all(R[l] is not None for l in R) and len(R) == 8)
check("first-order node matrices are Hermitian and the tilt vanishes at all eight nodes",
      all(R[l]['herm'] < 1e-9 and np.linalg.norm(R[l]['t']) < 1e-9 for l in R))
check("fitted cones reproduce the finite-q dispersion (rel. error/q < 1e-2 at q = 1e-3)", all(R[l]['disp_err'] < 1e-2 for l in R),
      f"max {max(R[l]['disp_err'] for l in R):.1e}")
v0 = np.sqrt(2) / 3
check("at +-k* the cone metric is (2/9) I: isotropic, speed sqrt2/3", all(np.allclose(R[l]['g'], 2 / 9 * np.eye(3), atol=1e-9) for l in ('k*', '-k*')))
dbl = [l for l in R if 'pi e_' in l]
okax = True; vals = []
for l in dbl:
    i = 'xyz'.index(l[-1]); g = R[l]['g']
    okax &= abs(g - np.diag(np.diag(g))).max() < 1e-9  # diagonal in lattice axes
    va = np.sqrt(g[i, i]); vt = [np.sqrt(g[j, j]) for j in range(3) if j != i]
    okax &= abs(vt[0] - vt[1]) < 1e-9; vals.append((va, vt[0]))
vals = np.array(vals)
check("each doubler k* + pi e_i / -k* + pi e_i has a diagonal uniaxial cone metric about its own axis e_i", okax)
check("doubler speeds: axial 0.2467, transverse 0.5838 (4 d.p.), identical for all six",
      np.allclose(vals[:, 0], vals[0, 0], atol=1e-9) and np.allclose(vals[:, 1], vals[0, 1], atol=1e-9)
      and round(vals[0, 0], 4) == 0.2467 and round(vals[0, 1], 4) == 0.5838, f"v_axial={vals[0,0]:.10f}, v_trans={vals[0,1]:.10f}")
chis = {l: R[l]['chi'] for l in R}
check("chiralities: k* and the three -k*+pi e_i one sign, -k* and k*+pi e_i the other; net zero", sum(chis.values()) == 0
      and len({chis['k*']} | {chis[f'-k*+pi e_{a}'] for a in 'xyz'}) == 1, f"{chis}")
# coordinate-free statement: the four distinct cone metrics are pairwise non-proportional
gs = [R['k*']['g']] + [R[f'k*+pi e_{a}']['g'] for a in 'xyz']
def prop(a, b):
    r = np.trace(a) / np.trace(b); return np.allclose(a, r * b, atol=1e-9)
check("the four cone-metric classes (isotropic, uniaxial x, y, z) are pairwise non-proportional, so no linear coordinate change or "
      "constant background strain can make all equal to one structure function", not any(prop(gs[i], gs[j]) for i in range(4) for j in range(i + 1, 4)))
print("invariants: det g^(1/3) isotropic", np.cbrt(np.linalg.det(gs[0])), " doubler", np.cbrt(np.linalg.det(gs[1])),
      " vt^2 va", vals[0, 1] ** 2 * vals[0, 0], " (sqrt2/3)^3", v0 ** 3, " tr g/3:", np.trace(gs[0]) / 3, np.trace(gs[1]) / 3)

# second 2-fold quasi-energy (-pi/2) if present
for E in Es:
    if E == E0: continue
    R2 = results[E]
    print(f"\nSecond 2-fold level at k*: E = {E:+.6f}: nodes present at {[l for l in R2 if R2[l] is not None]}")
    if all(R2[l] is not None for l in R2):
        same = all(np.allclose(R2[l]['g'], R[l]['g'], atol=1e-9) for l in R)
        print("  cone metrics equal to those at pi/2:", same, "; chiralities", {l: R2[l]['chi'] for l in R2})

# --- isolation of E: dense grid + local refinement away from the eight nodes
from scipy.optimize import minimize
def dist0(k): return np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Ws(k))) - E0)))
def dist(k): return dist0(k) + 10 * max(0.0, 0.25 - dnode(k))   # penalise walking into a node
n = 20
grid = [np.array(t) * 2 * np.pi / n - np.pi + 0.037 for t in itertools.product(range(n), repeat=3)]
def dnode(k): return min(np.linalg.norm(wrap(k - c)) for c in cube)
far = [g for g in grid if dnode(g) > 0.3]
dv = np.array([dist0(g) for g in far]); order = np.argsort(dv)[:25]
best = []
for i in order:
    r = minimize(dist, far[i], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-12, maxiter=4000))
    best.append((dist0(r.x), dnode(r.x)))
best_far = min(b[0] for b in best if b[1] > 0.2) if any(b[1] > 0.2 for b in best) else None
print(f"\nisolation of E=pi/2: grid {n}^3 min distance away from nodes {dv.min():.4f}; refined minima (dist, distance-to-node):",
      sorted([(round(a, 5), round(b, 3)) for a, b in best])[:6])
check("E = pi/2 is reached only near the eight cube points (20^3 grid + 25 local refinements, > 0.2 from any node)",
      best_far is not None and best_far > 1e-3, f"best refined distance away from nodes {best_far}")

# --- quasi-energy coverage (relevant to a local Floquet Hamiltonian, claim 3)
ph = np.concatenate([np.angle(np.linalg.eigvals(Ws(g))) for g in grid])
hist, edges = np.histogram(ph, bins=360, range=(-np.pi, np.pi))
empty = edges[:-1][hist == 0]
print(f"quasi-energy coverage on {n}^3 grid: {len(empty)} of 360 one-degree bins empty;", "empty bin starts (rad):", np.round(empty, 3)[:20])
print(f"\nTOTAL: PASS={NP} FAIL={NF}")
