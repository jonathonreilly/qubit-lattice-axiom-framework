"""A33 a15: detailed look at one P2-A(r2<=4) stage-1 survivor (by stage-1 index n).
usage: python3 a15_candidate.py n [parts]   parts: s(hapes) k(L) b(oxes) m(oves) z(Z3 movers)
"""
import signal, sys, time, pickle, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns, role_of, shape_at
from p2lib import pat_str
from p2_tests import build, rank_k, syndrome_span, mobile_moves
from a10_mover import find_mover
from a9_inspect_lib import certificate

REP = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}
n = int(sys.argv[1]); parts = sys.argv[2] if len(sys.argv) > 2 else "skbmz"
t0 = time.time()
S = Space(4)
s, ti = pickle.load(open("r4_stage1.pkl", "rb"))[n]
sh = shapes_of(S, s)
print(f"#{n} sol={s}")
if "s" in parts:
    for r in "VCEF":
        role, axis = role_of(REP[r])
        _, p = shape_at(sh[r], role, axis, REP[r])
        touched = sorted({role_of(y)[0] + (str(role_of(y)[1]) if role_of(y)[1] is not None else "") for y in p})
        print(f"  g_{r} at {REP[r]} (|supp| {len(p)}): {pat_str(p)}\n      touches {touched}")
if "k" in parts:
    for L in (8, 12, 16):
        T, gens = build(generator_patterns(sh, L), L)
        print(f"  k({L}) = {rank_k(T, gens)[0]} of N={T.N}   ({time.time()-t0:.1f}s)", flush=True)
if "b" in parts:
    for side in (4, 5, 6):
        dimC, pair = certificate(S, sh, side)
        print(f"  box {side}^3: dim commutant {dimC}; {'IMPURE (anticommuting local logicals)' if pair else 'no anticommuting pair'}   ({time.time()-t0:.1f}s)", flush=True)
mv16 = {}
if "m" in parts:
    for L in (8, 16):
        T, gens = build(generator_patterns(sh, L), L)
        E = syndrome_span(T, gens)
        for r, x0 in REP.items():
            mv = mobile_moves(T, E, x0)
            red = sorted({tuple(((c + L // 2 - 1) % L) - (L // 2 - 1) for c in v) for v in mv},
                         key=lambda v: (sum(abs(c) for c in v), v))
            if L == 16:
                mv16[r] = red
            roles = sorted({role_of(tuple(a + b for a, b in zip(x0, v)))[0] for v in red})
            print(f"  L={L} role {r}: {len(mv)} moves, landing roles {roles}; shortest {red[:8]}   ({time.time()-t0:.1f}s)", flush=True)
if "z" in parts:
    for r, red in mv16.items():
        if not red:
            continue
        for v in red[:6]:
            for m in (1, 2):
                Q, nb = find_mover(S, sh, REP[r], v, m)
                if Q is not None:
                    print(f"  Z3 mover role {r} v={v} (margin {m}): |supp|={len(Q)}: {pat_str(Q) if len(Q) <= 24 else '...'}")
                    break
            else:
                print(f"  Z3 mover role {r} v={v}: none (margins 1,2)")
print(f"done ({time.time()-t0:.1f}s)")
