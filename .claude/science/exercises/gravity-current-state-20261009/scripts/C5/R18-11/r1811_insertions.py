#!/usr/bin/env python3
"""R18-11 [8]: which insertions make the mean O(G noise^2) source independent of the readout gauge?
Compares the Poisson-gauge law with the harmonic-gauge law (same flat record J, same physical O(G) field)
for insertion families:
  C_w : J^{mu nu} = (-g)^{w/2} T^{mu nu}          (contravariant, density weight w; w = 2 - a/2, so a = 4 - 2w)
  M_w : J^{mu}_{nu} = (-g)^{w/2} T^{mu}_{nu}      (mixed; J^mu_nu := J^{mu s} eta_{s nu})
  L_w : J_{mu nu} = (-g)^{w/2} T_{mu nu}          (covariant; J_{mu nu} := eta J eta)
Prints Delta(tau_00 + tau_kk) and Delta tau_kk (Poisson minus harmonic) per mode, rho channel and V channel.
Imports the per-mode machinery from r1811_modes.py (same folder). Subtraction: none.
"""
import sympy as sp, sys, os, time, importlib.util
t0 = time.time()
spec = importlib.util.spec_from_file_location("m", os.path.join(os.path.dirname(os.path.abspath(__file__)), "r1811_modes_lib.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
eta = m.eta; Jup = m.Jup; Jlow = m.Jlow; avg = m.avg; einstein_to_2 = m.einstein_to_2
w_ = sp.Symbol('w_')
def T2_lower(h, fam):
    """second-order part of T_{mu nu} for the insertion family fam with weight w_."""
    trh = sp.expand(sum(eta[i, i] * h[i, i] for i in range(4)))      # (-g)^(1)
    hu = eta * h * eta                                                # h^{mu nu}
    Jmix = Jup * eta                                                  # J^mu_nu
    T = sp.zeros(4, 4)
    for a_ in range(4):
        for b in range(4):
            if fam == 'C':     # T^{ab} = (1 - w/2 trh) J^{ab};  T_{mn} = g g T
                val = -(w_ / 2) * trh * Jlow[a_, b]
                for al in range(4):
                    for be in range(4):
                        val += h[a_, al] * eta[b, be] * Jup[al, be] + eta[a_, al] * h[b, be] * Jup[al, be]
            elif fam == 'M':   # T^a_b = (1 - w/2 trh) J^a_b ; T_{mn} = g_{m a} T^a_n
                val = -(w_ / 2) * trh * Jlow[a_, b]
                for al in range(4):
                    val += h[a_, al] * Jmix[al, b]
            else:              # L: T_{mn} = (1 - w/2 trh) J_{mn}
                val = -(w_ / 2) * trh * Jlow[a_, b]
            T[a_, b] = val
    return T
res = {}
for fam in ('C', 'M', 'L'):
    for lab, h in (('P', m.hP), ('H', m.hH)):
        G = einstein_to_2(h)
        T2 = T2_lower(h, fam)
        tau = [[sp.simplify(avg(T2[i][j] if isinstance(T2, list) else T2[i, j]) - avg(G[i][j][1]) / (8 * sp.pi)) for j in range(4)] for i in range(4)]
        res[(fam, lab)] = (sp.simplify(tau[0][0]), sp.simplify(tau[1][1] + tau[2][2] + tau[3][3]))
    d_act = sp.factor(sp.simplify(res[(fam, 'P')][0] + res[(fam, 'P')][1] - res[(fam, 'H')][0] - res[(fam, 'H')][1]))
    d_kk = sp.factor(sp.simplify(res[(fam, 'P')][1] - res[(fam, 'H')][1]))
    sub = {m.Tp: 0, m.tp: 0}
    print("[8] family %s: Delta(tau_00+tau_kk) [P - H] = %s" % (fam, sp.factor(d_act.subs(sub))))
    print("    family %s: Delta tau_kk          [P - H] = %s" % (fam, sp.factor(d_kk.subs(sub))))
    for wv in (0, 1, 2):
        print("      w = %d: Delta act = %s ; Delta kk = %s" % (wv, sp.factor(d_act.subs(sub).subs(w_, wv)), sp.factor(d_kk.subs(sub).subs(w_, wv))))
    print("    family %s static rho-only Poisson law: (tau_00 + tau_kk)/u1 = %s" % (fam, sp.expand(sp.simplify((res[(fam, 'P')][0] + res[(fam, 'P')][1]).subs(sub).subs({m.jx: 0}).subs(m.w, 0) / m.u1))))
print("runtime %.1f s" % (time.time() - t0))
