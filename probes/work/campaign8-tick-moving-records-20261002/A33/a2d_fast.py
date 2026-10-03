"""A33 a2d: P2-A exhaustive search with solve_fast (same class as a2/a2b).  usage: python3 a2d_fast.py r2"""
import signal, sys, time, pickle
signal.alarm(55)
from p2a_core import Space, solve_fast, shapes_of
r2 = int(sys.argv[1]); t0 = time.time()
S = Space(r2)
sols = solve_fast(S)
ti = 0
good = []
for s in sols:
    sh = shapes_of(S, s)
    t = sh["V"] == sh["C"] == sh["E"] == sh["F"]
    ti += t
    good.append((s, t))
print(f"r2<={r2}: commuting + exact-sign solutions: {len(good)} (translation-invariant: {ti})   ({time.time()-t0:.1f}s)", flush=True)
pickle.dump({"r2": r2, "sols": good}, open(f"p2a_sols_r{r2}{'f' if r2 < 4 else ''}.pkl", "wb"))
