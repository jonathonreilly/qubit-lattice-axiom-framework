"""A30 q1_dirac_b: is the staggered-mass capture law a function of group velocity alone?
Compares A(E; m, Gam) from q1_dirac's exact transfer matrix with the massless closed form
A0(u; Gam) = 2 t Gam u / (t^2 + Gam^2/4 + t Gam u), u = v/(2t)."""
import signal, numpy as np
signal.alarm(55)
import importlib.util, sys, io, contextlib
spec = importlib.util.spec_from_file_location("qd", "q1_dirac.py")
src = open("q1_dirac.py").read().split("# sanity: m = 0")[0]     # import only the definitions
ns = {}
exec(src, ns)
absorb = ns['absorb']; t = 1.0
worst = {}
for m in [0.05, 0.2, 0.6]:
    for Gam in [0.3, 1.0, 2.0, 5.0]:
        ks = np.linspace(0.05, np.pi / 2 - 0.02, 40)
        dev = 0.0
        for k in ks:
            E = np.sqrt(m * m + 4 * t * t * np.cos(k) ** 2)
            v = 4 * t * t * np.cos(k) * np.sin(k) / E
            u = v / (2 * t)
            A, _ = absorb(E, m, Gam)
            A0 = 2 * t * Gam * u / (t * t + Gam * Gam / 4 + t * Gam * u)
            dev = max(dev, abs(A - A0))
        worst[(m, Gam)] = dev
        print(f"m={m} Gam={Gam}: max |A - A0(u)| over 40 energies = {dev:.2e}")
