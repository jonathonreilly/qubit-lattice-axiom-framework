#!/usr/bin/env python3
"""Reviewer checks for the C11 note (fresh-context, same model family). Reuses the runner's model build (sections 0-3,
exec'd from the runner file, read-only) and then tests two statements the runner does not test directly:
  R1 proof step 4: at an isolated 2-fold D_a level the O(q^2) term is a scalar, so the half eigenphase splitting is
     |sum v| |q| + O(q^3): (s(dl)/dl - |sum v|) must scale like dl^2, not dl.
  R2 'one global kappa' is exact: each tau^(b) satisfies tau_x tau_y tau_z = i (orientation of the Pauli triple), so
     tau^(b) = V sigma V^dag for a unitary V.
Usage: python3 rev_q2_and_kappa.py <path to runner>"""
import sys, numpy as np
src = open(sys.argv[1]).read()
cut = src.index("# Section 4: random words")
ns = {}
sys.argv = [sys.argv[0]]
exec(compile(src[:cut].rsplit("# ====", 1)[0], "runner_0_3", "exec"), ns)
rng = np.random.default_rng(7)
TAU, KPTS, DOUB = ns['TAU'], ns['KPTS'], ns['DOUB']
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
ok2 = True
for b in (1, -1):
    t = TAU[b]; prod = t[0] @ t[1] @ t[2]
    # find V with V sigma_z V^dag = tau_z, then fix phase so that V sigma_x V^dag = tau_x
    w, U = np.linalg.eigh(t[2]); V = U[:, ::-1]                      # columns: +1, -1 eigvecs of tau_z
    X = V.conj().T @ t[0] @ V; ph = np.conj(X[0, 1]) / abs(X[0, 1]); V = V @ np.diag([1, ph])
    err = max(np.abs(V @ SIG[i] @ V.conj().T - t[i]).max() for i in range(3))
    print(f"R2 D{'+' if b > 0 else '-'}: tau_x tau_y tau_z = {prod[0,0]:.3f} * 1 (offdiag {abs(prod[0,1]):.1e}); unitary equivalence to sigma err {err:.1e}")
    ok2 &= np.allclose(prod, 1j * np.eye(2)) and err < 1e-12
print("R2", "PASS" if ok2 else "FAIL")

L_S, L_AS, L_gen, L_RL, L_onsite, word_eval, predicted = (ns[k] for k in ("L_S", "L_AS", "L_gen", "L_RL", "L_onsite", "word_eval", "predicted"))
def rand_word():
    while True:
        w = []
        for _ in range(int(rng.integers(2, 5))):
            r = rng.random()
            w.append(L_gen() if r < 0.4 else L_S(int(rng.choice([1, -1, 2]))) if r < 0.6 else L_RL if r < 0.7
                     else L_onsite() if r < 0.8 else L_AS(int(rng.integers(-2, 3))) if r < 0.92 else L_gen(a2=True))
        if sum(L.chi == -1 for L in w) % 2 == 0: return w
def half_split(w, k0, w0, q, dl):
    ev = np.linalg.eigvals(word_eval(w, k0 + dl * q)); ph = np.angle(ev / w0); idx = np.argsort(np.abs(ph))[:2]
    p = np.sort(ph[idx]); return (p[1] - p[0]) / 2 / dl
ratios = []; n = 0
while n < 40:
    w = rand_word()
    for kn, k0 in KPTS.items():
        W = word_eval(w, k0); ev = np.linalg.eigvals(W)
        for a, D in DOUB.items():
            X = D.conj().T @ W @ D
            if not np.allclose(X, X[0, 0] * np.eye(2), atol=1e-10): continue
            w0 = X[0, 0]
            if np.sort(np.abs(ev - w0))[2] < 0.1: continue
            pv = predicted(w, k0, a)
            if abs(pv) < 0.05: continue
            q = rng.normal(size=3); q /= np.linalg.norm(q)
            d1 = half_split(w, k0, w0, q, 4e-3) - abs(pv); d2 = half_split(w, k0, w0, q, 2e-3) - abs(pv)
            if abs(d2) > 1e-11: ratios.append(d1 / d2)
            n += 1
ratios = np.array(ratios)
print(f"R1 {n} isolated levels: (s(dl)/dl - |sum v|) ratio at dl = 4e-3 vs 2e-3: median {np.median(ratios):.3f}, "
      f"min {ratios.min():.3f}, max {ratios.max():.3f}  (O(dl^2) -> 4, O(dl) -> 2)")
print("R1", "PASS" if np.all(np.abs(ratios - 4) < 0.3) else "FAIL")
