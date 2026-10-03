"""A33 a2b: P2-A search with the exact-sign filter applied per role BEFORE the cross constraints
(same class and result definition as a2; faster for larger balls).  usage: python3 a2b_p2a_search_presign.py r2"""
import signal, sys, time, pickle
signal.alarm(55)
from p2a_core import Space, solve, shapes_of, exact_signs_ok

r2 = int(sys.argv[1])
t0 = time.time()
S = Space(r2)
sols = solve(S, presign=True)
good = []
for s in sols:
    sh = shapes_of(S, s)
    assert exact_signs_ok(sh)
    good.append((s, sh["V"] == sh["C"] == sh["E"] == sh["F"]))
print(f"r2<={r2}: commuting + exact-sign solutions: {len(good)} (translation-invariant: {sum(t for _, t in good)})"
      f"   ({time.time()-t0:.1f}s)")
pickle.dump({"r2": r2, "sols": good}, open(f"p2a_sols_r{r2}{'b' if r2 < 4 else ''}.pkl", "wb"))
