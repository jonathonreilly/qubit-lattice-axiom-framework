"""A33 a2: exhaustive P2-A search (one generator per site, role-dependent site-group-invariant
shapes in the ball |d|^2 <= r2). Prints counts and pickles the commuting solutions that also pass
exact sign invariance.  usage: python3 a2_p2a_search.py r2
"""
import signal, sys, time, pickle
signal.alarm(55)
from p2a_core import Space, solve, shapes_of, exact_signs_ok, ROLES

r2 = int(sys.argv[1])
t0 = time.time()
S = Space(r2)
sols = solve(S)
print(f"r2<={r2}: commuting nonzero solutions (mod 2): {len(sols)}   ({time.time()-t0:.1f}s)")
good, ti = [], 0
for s in sols:
    sh = shapes_of(S, s)
    if not exact_signs_ok(sh):
        continue
    is_ti = sh["V"] == sh["C"] == sh["E"] == sh["F"]
    ti += is_ti
    good.append((s, is_ti))
print(f"  ... with exact sign invariance of all four shapes: {len(good)} (of which translation-invariant: {ti})"
      f"   ({time.time()-t0:.1f}s)")
pickle.dump({"r2": r2, "sols": good}, open(f"p2a_sols_r{r2}.pkl", "wb"))
