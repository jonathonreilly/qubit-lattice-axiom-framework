#!/usr/bin/env python3
"""B20 check 2: L3 (W3 = 0 for every word) and the Floquet Nielsen-Ninomiya link.
Own W3 integrator (analytic letter derivatives from the Bloch blocks / diagonal; finite differences for the
Hopf control), own controls:
 (a) per letter: S, S^2, R_L, on-site;  (b) a reflection 1-2P(k) whose P is the Hopf map T^3 -> CP^1 (Hopf
     invariant 1, NOT null-homotopic as a map to the Grassmannian) still has W3 = 0, as the explicit homotopy
     U_s = 1 + (e^{i pi s} - 1) P(k) predicts;  (c) additivity on a product with a W3 = 1 factor;
 (d) net chirality = W3 on an anomalous control built as (degree-1 map) x (corner word)."""
import time
from chklib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
SH_L = list(blL.keys()); SH_S = list(blS.keys())
def lw(L, k):
    if isinstance(L, str):
        if L == 'R':
            M = sum(blL[s] * np.exp(1j * np.dot(k, s)) for s in SH_L)
            G = [sum(1j * s[j] * blL[s] * np.exp(1j * np.dot(k, s)) for s in SH_L) for j in range(3)]
            return M, G
        p = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}[L]; d = np.diag(Sk(k, p)); fc = np.array([FACE[c] for c in CORN], float)
        return np.diag(d), [np.diag(1j * p * fc[:, j] * d) for j in range(3)]
    if callable(L): return L(k)
    return L, [np.zeros_like(L)] * 3
def wgrad(w, k):
    M = np.eye(len(lw(w[0], k)[0]), dtype=complex); G = [np.zeros_like(M) for _ in range(3)]
    for L in w:
        A, dA = lw(L, k); G = [g @ A + M @ da for g, da in zip(G, dA)]; M = M @ A
    return M, G
def W3(fun, N, off=0.137):
    g = np.arange(N) * 2 * np.pi / N + off; tot = 0
    for k in itertools.product(g, repeat=3):
        U, G = fun(np.array(k)); A = [np.linalg.solve(U, x) for x in G]
        # (1/24pi^2) eps_ijk tr A_i A_j A_k
        tot += sum(np.sign(np.linalg.det(np.eye(3)[list(p)])) * np.trace(A[p[0]] @ A[p[1]] @ A[p[2]]) for p in itertools.permutations(range(3)))
    return tot * (2 * np.pi / N) ** 3 / (24 * np.pi ** 2)
rng = np.random.default_rng(5)
for nm, w in (("S", ['S']), ("S^2", ['S2']), ("R_L", ['R']), ("on-site", [rand_onsite_unitary(rng)])):
    v = W3(lambda k: wgrad(w, k), 12)
    check(f"W3[{nm}] = 0", abs(v) < 1e-9, f"{v.real:+.1e}")
# R_L is Hermitian unitary with constant trace; explicit homotopy to 1 through unitaries
ks = rng.uniform(-np.pi, np.pi, (20, 3))
herm = all(np.allclose(RLk(k), RLk(k).conj().T) and np.allclose(RLk(k) @ RLk(k), np.eye(12)) for k in ks)
trs = {round(np.trace(RLk(k)).real, 9) for k in ks}
Pk = lambda k: (np.eye(12) - RLk(k)) / 2
homot = all(np.allclose((lambda U: U @ U.conj().T)(np.eye(12) + (np.exp(1j * np.pi * s) - 1) * Pk(k)), np.eye(12)) for k in ks[:5] for s in np.linspace(0, 1, 7))
check("R_L(k) = 1 - 2P(k) (Hermitian unitary, constant trace); U_s = 1 + (e^{i pi s}-1)P(k) is unitary for all s: an explicit null-homotopy", herm and len(trs) == 1 and homot, f"tr R_L = {trs}")
# Hopf control
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
def hopfP(k, m=2.0):
    z = np.array([np.sin(k[0]) + 1j * np.sin(k[1]), np.sin(k[2]) + 1j * (np.cos(k).sum() - m)]); return np.outer(z, z.conj()) / np.vdot(z, z).real
def fdfun(F, h=1e-5):
    def f(k):
        return F(k), [(F(k + h * e) - F(k - h * e)) / (2 * h) for e in np.eye(3)]
    return f
refl = lambda k: np.eye(2) - 2 * hopfP(k)
# Hopf invariant of P (Chern-Simons of the Berry connection of z/|z|): computed independently below via linking-free route:
# W3 of U = (z1, -conj z2; z2, conj z1)/|z| is the degree of z/|z| : T^3 -> S^3, which equals the Hopf invariant of z^dag sigma z
def su2(k, m=2.0):
    z = np.array([np.sin(k[0]) + 1j * np.sin(k[1]), np.sin(k[2]) + 1j * (np.cos(k).sum() - m)]); z = z / np.linalg.norm(z)
    return np.array([[z[0], -np.conj(z[1])], [z[1], np.conj(z[0])]])
deg = W3(fdfun(su2), 28); wr = W3(fdfun(refl), 28)
check("Hopf control: the map z/|z| has degree +-1 (so P = zz^dag/|z|^2 has Hopf invariant +-1, P not null-homotopic in CP^1), yet W3[1-2P] = 0",
      abs(abs(deg.real) - 1) < 2e-3 and abs(wr) < 2e-3, f"deg = {deg.real:+.5f}, W3[1-2P] = {wr.real:+.1e}")
# additivity with a W3 = deg factor: U = su2 (x) 1_6 times the eight-node step (12x12)
step8 = ['S', 'R', UH, UL]
big = lambda k: (lambda A, B: (np.kron(A[0], np.eye(6)) @ B[0], [np.kron(dA, np.eye(6)) @ B[0] + np.kron(A[0], np.eye(6)) @ dB for dA, dB in zip(A[1], B[1])]))(fdfun(su2)(k), wgrad(step8, k))
w8 = W3(lambda k: wgrad(step8, k), 16); wb = W3(big, 24)
check("additivity: W3[eight-node step] = 0 and W3[(su2 (x) 1_6) . step] = 6 W3[su2] + 0 = 6 deg", abs(w8) < 1e-9 and abs(wb - 6 * deg) < 5e-3, f"{w8.real:+.1e}, {wb.real:+.5f}")
# words (different from B20's three)
for w in (['S2', rand_onsite_unitary(rng), 'R', 'Si', rand_onsite_unitary(rng), 'S', 'S', 'R'], ['S2i', 'R', rand_onsite_unitary(rng), 'S2', 'S2', rand_onsite_unitary(rng)]):
    v = W3(lambda k: wgrad(w, k), 14); v2 = W3(lambda k: wgrad(w, k), 18, off=0.41)
    check("W3 = 0 for a random long word (two grids)", abs(v) < 1e-8 and abs(v2) < 1e-8, f"{v.real:+.1e} {v2.real:+.1e}")
# (d) Floquet NN on an anomalous control: U(k) = su2(k) with m=2: nodes at quasi-energy E where z-phase hits E
# Here U = (z1, -z2*; z2, z1*): eigenphases +-arccos(Re z1)/... ; E = 0 reached where z = (1,0): k with sin kx=0? use direct census
def census(F, E, N=24):
    g = np.linspace(-np.pi, np.pi, N, endpoint=False) + 0.011
    from scipy.optimize import minimize
    f = lambda k: float(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(F(np.asarray(k)))) - E))))
    G_ = np.array(list(itertools.product(g, repeat=3))); d = np.array([f(k) for k in G_]); sols = []
    for i in np.argsort(d)[:60]:
        r = minimize(f, G_[i], method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 3000})
        if r.fun < 1e-6:
            x = wrap(r.x)
            if not any(np.linalg.norm(wrap(x - s)) < 1e-4 for s in sols): sols.append(x)
    return sols
def chi_of(F, k0, E):
    U = F(k0); h = 1e-6; Gs = [(F(k0 + h * e) - F(k0 - h * e)) / (2 * h) for e in np.eye(3)]
    hs = [(-1j * U.conj().T @ g + (-1j * U.conj().T @ g).conj().T) / 2 for g in Gs]
    # project to the 2 levels at E (here the whole 2-dim space)
    M = np.array([[np.trace(x @ s_).real / 2 for s_ in (sx, sy, sz)] for x in hs]); return int(np.sign(np.linalg.det(M)))
for E in (0.0, np.pi):
    sols = census(su2, E)
    chis = [chi_of(su2, s, E) for s in sols]
    check(f"anomalous control su2 (W3 = {deg.real:+.0f}): at E = {E:+.3f} the det-M chiralities of all nodes sum to W3", sum(chis) == round(deg.real), f"{len(sols)} nodes, chi {chis}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
