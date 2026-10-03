"""A33 a2c: size diagnostics for the P2-A search at a given radius (no enumeration of pairs)."""
import signal, sys, time
signal.alarm(55)
from p2a_core import Space, quad_ok, sign_ok_role, ROLES
r2 = int(sys.argv[1]); t0 = time.time()
S = Space(r2)
cons = S.bilinear_constraints()
print("dims", S.dim, " constraints", {f"{a}{b}": len(v) for (a, b), v in sorted(cons.items())}, f"({time.time()-t0:.1f}s)", flush=True)
for r in ROLES:
    mats = list(cons.get((r, r), ()))
    v = [c for c in range(1, 1 << S.dim[r]) if quad_ok(c, mats)]
    vs = [c for c in v if sign_ok_role(S, r, c)]
    print(f"  role {r}: self-commuting {len(v)}, + exact sign {len(vs)}  ({time.time()-t0:.1f}s)", flush=True)
