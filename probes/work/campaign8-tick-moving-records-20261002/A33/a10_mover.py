"""A33 a10: explicit local movers on Z^3 (no torus).
usage: python3 a10_mover.py r2 V C E F role vx,vy,vz [margins=1,2,3]

Unknown: a Pauli Q supported in the box B = bounding box of {x0, x0+v} enlarged by `margin`.
Constraints: for every generator g_x touching B, omega(Q, g_x) = [x == x0] + [x == x0+v].
Generators not touching B commute with Q automatically. A solution is an exact local operator on Z^3
whose syndrome is exactly the defect pair, i.e. it moves a lone defect by v (EXACT).
No solution in B only means none supported in B.
"""
import signal, sys, time, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, role_of, shape_at
from p2lib import Elim, BITS2L, pat_str

REP = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}


def find_mover(S, sh, x0, v, margin):
    x1 = tuple(a + b for a, b in zip(x0, v))
    lo = [min(a, b) - margin for a, b in zip(x0, x1)]
    hi = [max(a, b) + margin for a, b in zip(x0, x1)]
    B = list(itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]))
    pos = {y: k for k, y in enumerate(B)}
    rad = S.rinf
    xs = set()
    for y in B:
        for d in itertools.product(range(-rad, rad + 1), repeat=3):
            xs.add(tuple(a + b for a, b in zip(y, d)))
    rows = []
    for x in xs:
        role, axis = role_of(x)
        _, p = shape_at(sh[role], role, axis, x)
        row = 0
        for z, l in p.items():
            if z in pos:
                k = pos[z]
                bx, bz = {1: (1, 0), 2: (1, 1), 3: (0, 1)}[l]
                if bz:
                    row |= 1 << (2 * k)
                if bx:
                    row |= 1 << (2 * k + 1)
        rhs = int(x == x0) ^ int(x == x1)
        if row == 0:
            if rhs:                      # a defect generator that does not touch B: unsatisfiable
                return None, len(B)
            continue
        rows.append((row, rhs))
    if x0 not in xs or x1 not in xs:     # defect generators farther than r_inf from every site of B
        return None, len(B)
    # check the two defect generators are among the touching ones (else unsatisfiable)
    n = 2 * len(B)
    E = Elim()
    for row, rhs in rows:
        v_, c_ = E.reduce(row, rhs)
        if v_ == 0:
            if c_:
                return None, len(B)
            continue
        E.rows[v_.bit_length() - 1] = (v_, c_)
    # back-substitute: free variables = 0
    sol = 0
    for h in sorted(E.rows):
        v_, c_ = E.rows[h]
        rest = v_ ^ (1 << h)
        val = c_ ^ (bin(rest & sol).count("1") & 1)
        if val:
            sol |= 1 << h
    Q = {}
    for k, y in enumerate(B):
        a_, b_ = (sol >> (2 * k)) & 1, (sol >> (2 * k + 1)) & 1
        if a_ or b_:
            Q[y] = BITS2L[(a_, b_)]
    return Q, len(B)


if __name__ == "__main__":
    r2 = int(sys.argv[1])
    sol = dict(zip("VCEF", (int(t) for t in sys.argv[2:6])))
    role = sys.argv[6]
    vs = [tuple(int(c) for c in t.split(",")) for t in sys.argv[7].split(";")]
    margins = [int(t) for t in sys.argv[8].split(",")] if len(sys.argv) > 8 else [1, 2, 3]
    t0 = time.time()
    S = Space(r2)
    sh = shapes_of(S, sol)
    x0 = REP[role]
    for v in vs:
        for m in margins:
            Q, nb = find_mover(S, sh, x0, v, m)
            if Q is not None:
                print(f"role {role} at {x0}, v={v}, margin {m} (|B|={nb}): MOVER FOUND, |supp|={len(Q)}   ({time.time()-t0:.1f}s)")
                if len(Q) <= 40:
                    print("    Q =", pat_str(Q))
                break
            else:
                print(f"role {role} at {x0}, v={v}, margin {m} (|B|={nb}): none in box   ({time.time()-t0:.1f}s)", flush=True)
