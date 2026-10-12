"""RL3b (D): physical translation of gamma = k_h sqrt(eps)/l_k (variance rate; sd rate = gamma/2), eps = (l_P/l_k)^4,
proper time tau = sqrt(2 D s + s^2) (RL2 B.1 scale; transfer to the extended source not proved -- see report).
sd e-folds n = k l_P^2 tau / (2 l_k^3); bounded (n <= 1) needs l_k >= (k l_P^2 tau/2)^(1/3);
the bar fails iff k > k_crit = 2 l_k^3/(l_P^2 tau) at l_k = 1e-19 m.
"""
import numpy as np
lP = 1.616255e-35; pc = 3.0856776e16; D = 1e9*pc
KH = {"op0": 2.73484, "op1": 2.83527, "op2": 3.25389}
print("D = 1 Gpc = %.5e m ; eps at l_k = 1e-19 m: %.4e ; sqrt(eps) = %.4e" % (D, (lP/1e-19)**4, (lP/1e-19)**2))
for s, lab in [(1e4, "s = 1.0e4 m (10 km source)"), (1.2e4, "s = 1.2e4 m (E1'-b scale)"), (3e6, "s = 3e6 m (one 100 Hz cycle)"), (3e10, "s = 3e10 m (100 s)")]:
    tau = np.sqrt(2*D*s + s*s)
    kc = 2*(1e-19)**3/(lP**2*tau)
    row = []
    for op, k in KH.items():
        n = k*lP**2*tau/(2*(1e-19)**3); lk = (k*lP**2*tau/2)**(1/3)
        row.append("%s: n_sd(bar)=%.1f, l_k needed %.2e m" % (op, n, lk))
    print("%-30s tau = %.4e m ; k_crit = %.5f (k_h/k_crit = %.0f..%.0f)\n     " % (lab, tau, kc, KH["op0"]/kc, KH["op2"]/kc) + " | ".join(row))
# how small would the TRUE constant have to be, or how large the exponent, for PASS at the bar (s = 1e4 m)
tau = np.sqrt(2*D*1e4 + 1e8); eps = (lP/1e-19)**4
for op, k in KH.items():
    n = k*lP**2*tau/(2*(1e-19)**3)
    alpha = 0.5 + np.log(n)/np.log(1/eps)
    print("%s: PASS at the bar would need c_true <= k_h/%.0f, or exponent alpha >= %.4f (vs 1/2 derived)" % (op, n, alpha))
