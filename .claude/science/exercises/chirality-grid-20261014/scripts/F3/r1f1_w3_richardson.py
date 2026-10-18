import os; os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("r1", os.path.join(os.path.dirname(os.path.abspath(__file__)), "r1_duality_check.py"))
r1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r1)
target = {"U_g (T4 exact)": 4, "V = q_tr/|q_tr| (T4 range-2)": 4, "Wilson-normalized M=2": -1, "Wilson-normalized M=-2": -1, "Wilson-normalized M=0.5": 2}
allok = True
for name, f in r1.TICKS.items():
    Ns = [32, 48, 64]; ws = [r1.W3(f, N) for N in Ns]
    A = np.array([[1, 1 / N ** 2] for N in Ns]); sol, *_ = np.linalg.lstsq(A, np.array(ws), rcond=None)
    ok = abs(sol[0] - target[name]) < 0.05; allok &= ok
    print(f"{name:32s} W3(N=32,48,64) = {', '.join(f'{w:+.4f}' for w in ws)}  extrapolated = {sol[0]:+.4f}  target sum chi(eps=0) = {target[name]:+d}  {'PASS' if ok else 'FAIL'}")
print("OVERALL R1-F1:", "PASS" if allok else "FAIL")
