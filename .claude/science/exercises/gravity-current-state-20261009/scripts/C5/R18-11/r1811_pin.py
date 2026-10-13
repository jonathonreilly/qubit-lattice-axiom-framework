#!/usr/bin/env python3
"""R18-11 [9]: R18-7's conserving projection Pi on the homogeneous mode (TESTS:6902; R18-7 section 3 item 3).
K = i(p^a D^b + p^b D^a)/p^2 - i p^a p^b (p.D)/p^4,  D^a = i p_b S^{ab},  eta = diag(-1,1,1,1), p^mu = (w, 0, 0, k).
Checks: (i) i p_b K^{ab} = -D^a identically; (ii) k = 0 exactly (homogeneous switch-on, time dependence only):
K^{00} = -S^{00} (energy removed), K^{0i} = 0, K^{ij} = 0 (no pressure added); (iii) w = 0, k -> 0 (static long-wave approach):
K^{ij} = -p_hat-projected stress, i.e. the p -> 0 limit is direction dependent (Pi is homogeneous of degree 0).
Subtraction: none.
"""
import sympy as sp
w, k = sp.symbols('omega k')
eta = sp.diag(-1, 1, 1, 1)
S = sp.Matrix(4, 4, lambda i, j: sp.Symbol('S%d%d' % (min(i, j), max(i, j))))
def K_of(pu):
    pl = eta * pu
    p2 = (pu.T * eta * pu)[0]
    D = sp.Matrix([sp.I * sum(pl[b] * S[a, b] for b in range(4)) for a in range(4)])
    pD = sum(pl[a] * D[a] for a in range(4))
    K = sp.Matrix(4, 4, lambda a, b: sp.I * (pu[a] * D[b] + pu[b] * D[a]) / p2 - sp.I * pu[a] * pu[b] * pD / p2**2)
    chk = [sp.simplify(sp.I * sum(pl[b] * K[a, b] for b in range(4)) + D[a]) for a in range(4)]
    return sp.simplify(K), chk
pu = sp.Matrix([w, 0, 0, k])
K, chk = K_of(pu)
print("[9] (i) i p_b K^{ab} + D^a =", chk)
K0, _ = K_of(sp.Matrix([w, 0, 0, 0]))
print("    (ii) k = 0: K^{00} =", sp.simplify(K0[0, 0]), "; K^{0i} =", [sp.simplify(K0[0, i]) for i in (1, 2, 3)],
      "; K^{ij} =", [sp.simplify(K0[i, j]) for i in (1, 2, 3) for j in (i, 3)])
print("        => on the homogeneous mode Pi removes exactly the time-dependent part of the mean energy density S^{00}")
print("           (retarded 1/p^2: K^{00}(t) = -[S^{00}(t) - S^{00}(t0)]); it adds no pressure.")
Ks, _ = K_of(sp.Matrix([0, 0, 0, k]))
p_ = sp.Symbol('p')
iso = {S[1, 1]: p_, S[2, 2]: p_, S[3, 3]: p_, S[1, 2]: 0, S[1, 3]: 0, S[2, 3]: 0}
print("    (iii) w = 0, k along z, isotropic stress S^{ij} = p delta: K^{ij} diagonal =", [sp.simplify(Ks[i, i].subs(iso)) for i in (1, 2, 3)],
      "; K^{00} =", sp.simplify(Ks[0, 0]))
print("        => the static long-wave limit removes the longitudinal stress (direction-dependent); the exact homogeneous")
print("           mean of a noise switched on at t0 is the k = 0, w != 0 case (ii).")

# [9b] the linearized Hamiltonian constraint has no homogeneous (k = 0) content: G^(1)_00 = 0 for any h_{mu nu}(t)
import importlib.util, os
spec = importlib.util.spec_from_file_location("m", os.path.join(os.path.dirname(os.path.abspath(__file__)), "r1811_modes_lib.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
H = sp.Matrix(4, 4, lambda i, j: sp.Symbol('A%d%d' % (min(i, j), max(i, j))) * m.c + sp.Symbol('B%d%d' % (min(i, j), max(i, j))) * m.s)
G = m.einstein_to_2(H.subs(m.k, 0))
G = m.einstein_to_2(H)
G00_k0 = sp.simplify(sp.expand(G[0][0][0]).subs(m.k, 0))
Gkk_k0 = sp.simplify(sp.expand(sum(G[i][i][0] for i in (1, 2, 3))).subs(m.k, 0))
print("[9b] k = 0 (homogeneous h(t)): G^(1)_00 =", G00_k0, "; G^(1)_kk =", sp.factor(Gkk_k0))
print("     => a homogeneous mean energy density has no linear response on Minkowski (must be zero, or the background is FRW);")
print("        a homogeneous pressure drives h_kk'' (secular growth ~ 8 pi G p t^2).")
