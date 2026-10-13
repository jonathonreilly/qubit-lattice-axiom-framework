"""C5 R17-2: Boltzmann exponents for the edge-quantum infimum 1.431782/a (vR16-12:19) at a = l_P (conditional, AX:189-190). No subtraction."""
import math, os
lP_GeV = 1.22089e19; e = 1.431782 * lP_GeV
lines = []
for name, T in [('T_CMB', 2.348e-13), ('1 TeV', 1e3), ('1e16 GeV', 1e16)]:
    lines.append(f"{name} eps/T={e/T:.4g} log10 occupation={-(e/T)/math.log(10):.4g}")
lines.append(f"eps(GeV)={e:.4g}")
print("\n".join(lines))
open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w").write("\n".join(lines) + "\n")
