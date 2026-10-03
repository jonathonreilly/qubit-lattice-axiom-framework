"""A33 a3: screen P2-A candidates.  usage: python3 a3_p2a_screen.py r2 start end [purity]
For each candidate (commuting + exact signs, from a2):
  - single-defect mobility on the L=4 torus for each role (V at (0,0,0), C at (1,1,1), E_x at
    (1,0,0), F_z at (1,1,0)); immobile here => immobile on Z^3 (EXACT, see p2_tests.py);
  - k(L) = N - rank at L = 4 (and with 'purity': k(6) and the local-logical test C_B vs S_B on a
    3x3x3 box of the L=6 torus).
Appends one line per candidate to p2a_screen_r{r2}.txt and prints a summary.
"""
import signal, sys, time, pickle
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns
from p2_tests import build, rank_k, syndrome_span, mobile_moves, creatable, local_logicals, box

r2, a, b = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
purity = len(sys.argv) > 4
t0 = time.time()
D = pickle.load(open(f"p2a_sols_r{r2}.pkl", "rb"))
S = Space(r2)
sols = D["sols"][a:b]
X0 = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}
lines, nmob, nsingle = [], 0, 0
for n, (sol, is_ti) in enumerate(sols, start=a):
    sh = shapes_of(S, sol)
    T, gens = build(generator_patterns(sh, 4), 4)
    k4, _ = rank_k(T, gens)
    E = syndrome_span(T, gens)
    mob = {r: len(mobile_moves(T, E, x0)) for r, x0 in X0.items()}
    single = {r: creatable(E, T.idx(x0)) for r, x0 in X0.items()}
    extra = ""
    if purity:
        T6, g6 = build(generator_patterns(sh, 6), 6)
        k6, _ = rank_k(T6, g6)
        CB, SB = local_logicals(T6, g6, box((1, 1, 1), 3))
        extra = f" k6={k6} box3:C={CB},S={SB}{' LOCAL-LOGICAL' if CB > SB else ''}"
    if any(mob.values()):
        nmob += 1
    if any(single.values()):
        nsingle += 1
    lines.append(f"{n} ti={int(is_ti)} sol={sol} k4={k4} mobL4={mob} creatable={single}{extra}")
with open(f"p2a_screen_r{r2}.txt", "a") as fh:
    fh.write("\n".join(lines) + "\n")
print(f"r2<={r2} candidates {a}..{b-1}: {len(sols)} screened; with any mobile single defect on L=4: {nmob};"
      f" with a locally creatable single defect: {nsingle}   ({time.time()-t0:.1f}s)")
