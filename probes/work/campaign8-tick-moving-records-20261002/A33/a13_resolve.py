"""A33 a13: resolve the P2-A(r2<=4) survivors that stayed mobile on L = 6, 8, 10 without an impurity
certificate.  usage: python3 a13_resolve.py start end
Per candidate and role:
  - moves on L = 6, 8, 16 (a role immobile on ANY of them is immobile on Z^3: EXACT);
  - for roles mobile on all three: explicit Z^3 mover search (a10.find_mover, margins 1-2) for the
    shortest lifts of the L=16 moves and the in-plane/axis vectors 4e_a, 4(e_a+e_b) (EXACT if found).
Appends to r4_resolve.txt.
"""
import signal, sys, time, re, ast, pickle
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns
from p2_tests import build, syndrome_span, mobile_moves
from a10_mover import find_mover

REP = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}
a, b = int(sys.argv[1]), int(sys.argv[2])
t0 = time.time()
S = Space(4)
surv = pickle.load(open("r4_stage1.pkl", "rb"))
todo = []
for line in open("r4_stage3.txt"):
    if "mobL=10" in line and "cert5=-" in line and "mob={'V': 0, 'C': 0, 'E': 0, 'F': 0}" not in line:
        todo.append(int(line.split()[0]))
todo = todo[a:b]
out = []
for n in todo:
    s, ti = surv[n]
    sh = shapes_of(S, s)
    res = {}
    alive = set(REP)
    for L in (6, 8, 16):
        if not alive:
            break
        T, gens = build(generator_patterns(sh, L), L)
        E = syndrome_span(T, gens)
        for r in sorted(alive):
            mv = mobile_moves(T, E, REP[r])
            res[(r, L)] = mv
            if not mv:
                alive.discard(r)
    movers = {}
    for r in sorted(alive):
        lifts = sorted({tuple(((c + 7) % 16) - 7 for c in v) for v in res[(r, 16)]},
                       key=lambda v: (sum(abs(c) for c in v), v))[:4]
        extra = [(4, 0, 0), (0, 4, 0), (0, 0, 4), (4, 4, 0), (0, 4, 4), (4, 0, 4)]
        found = []
        for v in lifts + extra:
            Q, _ = find_mover(S, sh, REP[r], v, 1)
            if Q is None:
                Q, _ = find_mover(S, sh, REP[r], v, 2)
            if Q is not None:
                found.append(v)
        movers[r] = (len(res[(r, 16)]), lifts, found)
    stat = {r: ("imm" if r not in alive else f"L16:{movers[r][0]} lifts{movers[r][1][:3]} Z3movers{movers[r][2]}") for r in REP}
    out.append(f"{n} sol={s} " + " | ".join(f"{r}:{stat[r]}" for r in "VCEF"))
    if time.time() - t0 > 48:
        out.append(f"# stopped early after #{n}")
        break
with open("r4_resolve.txt", "a") as fh:
    fh.write("\n".join(out) + "\n")
print(f"resolved {len(out)} of todo[{a}:{b}]   ({time.time()-t0:.1f}s)")
