"""Order-of-magnitude knock-on: vacuum <psibar psi> per 4-comp D1 root field (Dirac sea), times the rule's counterterm curvature.
<psibar psi>_vac per cell = -(1/V) sum_k tr[beta P_-(k)] = -2 <M/E>  (two filled negative-energy states per k, <beta> = -M/E each)."""
import sys, numpy as np
sys.path.insert(0, sys.argv[1])
from dirac import D1
law = D1(0.909103708, 0.555604226)
for N in (48, 96):
    k = (np.arange(N) + 0.5) * 2*np.pi/N - np.pi
    S, W = law.S(k), law.W(k)
    acc = 0.0
    for i in range(N):
        M = 0.0 + W[i] + W[:, None] + W[None, :]
        E = np.sqrt(S[i]**2 + S[:, None]**2 + S[None, :]**2 + M**2)
        acc += (M/E).sum()
    meanME = acc / N**3
    print(f"N={N}: <M/E> = {meanME:.6f};  <psibar psi>_vac per field per cell = {-2*meanME:+.6f} /a^3")
e2 = 4*np.pi/137.036
hess = 2.42401e-2
print(f"knock-on curvature of vacuum energy per field per cell (SF units): -Hess*e2*<psibar psi> = {-hess*e2*(-2*meanME):+.3e} /a^4 (QED charge 1; quarks scale by Q^2 or C_F g_s^2/e^2)")
