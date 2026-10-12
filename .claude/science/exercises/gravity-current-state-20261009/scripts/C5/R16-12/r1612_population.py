"""C5 R16-12 (c): edge-quantum population (reading only; conditional on an (alpha) response existing).
Minimum one-quantum energy over the defect-carrying region (Delta != 0) for S(1.4) and G(1.4), then the
Boltzmann exponent eps_min/(a T) at a = l_P (1/a = 1.2209e19 GeV) for several temperatures. Raw numbers, nothing subtracted."""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sublum_copy import SymS, SymG
S14, G14 = SymS(1.4), SymG(1.4)
k = np.linspace(-np.pi, np.pi, 200001)
EP = 1.2209e19
out = []
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
for m in (0.3, 0.0):
    for name, u, dfl in (("S(1.4)", S14.s(k)**2, np.abs(S14.ds(k)**2 + S14.s(k)*S14.d2s(k) - 1) > 1e-9),
                         ("G(1.4)", G14.g(k), np.abs(0.5*G14.d2g(k) - 1) > 1e-9)):
        umin = u[dfl].min()               # one component on the defect support, others at k = 0
        emin = np.sqrt(m*m + umin)
        pr(f"m = {m}: {name}: min one-quantum energy carrying a defect = {emin:.4f}/a = {emin*EP:.3e} GeV")
        for T, lab in ((2.3487e-13, "T_CMB"), (1e3, "1 TeV"), (1e16, "1e16 GeV"), (1e19, "1e19 GeV")):
            x = emin*EP/T
            pr(f"    {lab:9s}: Boltzmann exponent eps/T = {x:.3e}  -> occupation ~ 10^({-x/np.log(10):.3e})")
with open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w") as f:
    f.write("\n".join(out) + "\n")
