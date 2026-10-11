"""RL4 B: explicit end-factor constants for Lemma T' (source with a spacelike past edge and regular turn-on).
z_k sits in the layer 0 < N.z <= a above the edge; C(z_k) = J^-(z_k) n {N.y >= 0} has volume (pi/3) t^4 <= (pi/3) a^4.
Turn-on regularity: |J(y)| <= kJ |J(z_k)| for y in C(z_k).  Computes a_0 such that |F_k^J| >= (1/2)(1-2 delta) h0 |G_{k-1}| |J(z_k)|.
"""
import numpy as np
from math import pi, sqrt, exp, log
import rl2_core as rc
from rl4_A_lemmaU_constants import analyse, fder, tail_sup
tau1, tau2 = 0.1, 0.6
for kJ in [1.0, 2.0]:
  for k, C in enumerate(rc.OPS):
    o = analyse(k, C, tau1, tau2); pv = o["pv"]; th = o["theta_star"]; d = pv["delta"]; q = pv["q"]
    h_inf, h0, psi0, e_w, om = o["h_inf"], o["h0"], o["psi0"], o["e_w"], o["om"]
    mm = np.concatenate([np.linspace(0, 50, 200001), np.linspace(50.0005, 2000, 40000)])
    Phi2 = tail_sup(np.abs(fder(C, 2, mm)))
    x = np.linspace(0, np.sqrt(24*2000/pi), 400001)
    S2p = np.trapezoid(np.interp(pi*x**2/24, mm, Phi2), x)          # int_0^inf Phi_2(pi x^2/24) dx
    g2 = S2p*(2*tau2/tau1)*exp(-th)                                   # last block {z_{k-1}, z_k}: top-end suppression only
    def need(a):
        kp = kJ*(1 + h_inf*(pi/3)*a**4)                                # sup |Psi| on C(z_k) / |J(z_k)|
        Ekm1 = (1 + h_inf*(pi/24)*tau2**4)*psi0*(pi/3)*a**4*kp        # a = k-1 term
        Cend = (1 + e_w)*max(1.0, om)*max(psi0, g2/q)*(pi/3)*kp*2      # a <= k-2, per delta^{n'} (n' >= 1)
        tail = sum(((d/(1-2*d))**n)*Cend*a**4 for n in range(1, 200))
        node = (1-2*d)*h0*(1 - h_inf*kJ*(pi/3)*a**4)
        return node - Ekm1 - tail - 0.5*(1-2*d)*h0, Ekm1, tail, node
    a0 = 0.0
    for a in np.linspace(0.001, 0.5, 5000):
        if need(a)[0] >= 0: a0 = a
        else: break
    r = need(a0)
    print("kJ=%.1f op%d: theta*=%.2f delta=%.4f q=%.3e S2'=%.3f g2=%.3e | a_0 = %.4f : node %.4f, E_{k-1} %.4f, a<=k-2 tail %.4f  (>= half node: %s)"
          % (kJ, k, th, d, q, S2p, g2, a0, r[3], r[1], r[2], r[0] >= 0))
