"""A33 a4: deeper tests of selected P2-A candidates.  usage: python3 a4_p2a_deep.py r2 i1,i2,...
For each: k(L) at L = 4, 6, 8; local logicals (C_B vs S_B) on 3x3x3 and 4x4x4 boxes of the L=8 torus;
single-defect moves for each role on L = 6 and 8 (listed when few).
"""
import signal, sys, time, pickle
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns
from p2lib import pat_str
from p2_tests import build, rank_k, syndrome_span, mobile_moves, local_logicals, box

r2 = int(sys.argv[1])
idx = [int(t) for t in sys.argv[2].split(",")]
t0 = time.time()
D = pickle.load(open(f"p2a_sols_r{r2}.pkl", "rb"))
S = Space(r2)
X0 = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}
for n in idx:
    sol, is_ti = D["sols"][n]
    sh = shapes_of(S, sol)
    print(f"#{n} sol={sol}")
    for r in ("V", "C", "E", "F"):
        print(f"   g_{r} = {pat_str(sh[r])}")
    ks = []
    for L in (4, 6, 8):
        T, gens = build(generator_patterns(sh, L), L)
        k, _ = rank_k(T, gens)
        ks.append(f"k({L})={k}")
        if L >= 6:
            E = syndrome_span(T, gens)
            mv = {r: mobile_moves(T, E, x0) for r, x0 in X0.items()}
            print(f"   L={L}: moves per role: " + ", ".join(
                f"{r}:{len(v)}" + (f" {sorted(v)[:8]}" if 0 < len(v) <= 8 else "") for r, v in mv.items()))
        if L == 8:
            for side in (3, 4):
                CB, SB = local_logicals(T, gens, box((2, 2, 2), side))
                print(f"   L=8 box {side}^3: C_B={CB} S_B={SB}" + ("  <-- LOCAL LOGICAL (impure)" if CB > SB else "  (no local logical)"))
    print("   " + " ".join(ks) + f"   ({time.time()-t0:.1f}s)")
    sys.stdout.flush()
