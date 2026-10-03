"""A33 a12: torus move sets for one defect role of a P2-A(r2) solution.
usage: python3 a12_moves.py r2 V C E F role Ls
Prints, per L, the number of moves and the smallest few (fine units, reduced to (-L/2, L/2]),
and whether specific test vectors are moves.
"""
import signal, sys, time
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns
from p2_tests import build, syndrome_span, mobile_moves

REP = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}
r2 = int(sys.argv[1]); sol = dict(zip("VCEF", (int(t) for t in sys.argv[2:6]))); role = sys.argv[6]
Ls = [int(t) for t in sys.argv[7].split(",")]
t0 = time.time()
S = Space(r2); sh = shapes_of(S, sol)
for L in Ls:
    T, gens = build(generator_patterns(sh, L), L)
    E = syndrome_span(T, gens)
    mv = mobile_moves(T, E, REP[role])
    red = sorted({tuple(((c + L // 2 - 1) % L) - (L // 2 - 1) for c in v) for v in mv}, key=lambda v: (sum(abs(c) for c in v), v))
    coarse_odd = (L // 2) % 2 == 1
    print(f"L={L} (coarse {L//2}{' odd' if coarse_odd else ''}): {len(mv)} moves; shortest: {red[:10]}   ({time.time()-t0:.1f}s)", flush=True)
