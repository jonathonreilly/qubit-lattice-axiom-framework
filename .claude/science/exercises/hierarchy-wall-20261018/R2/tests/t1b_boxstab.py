"""T1b: box stability and admissibility-faithful rerun.

mode 'stab': for given (base, rule) pairs found in T1 at box 5, recompute the
  exact minimal flip in larger boxes (binary search on |S|).
mode 'faithful': rerun the T1 CEGAR with the extra admissibility clause that
  every neighbour configuration allows at least one centre value (a
  probability distribution exists at every site).
usage: python3 t1b_boxstab.py stab BOX | faithful BOX
"""
import sys, itertools, time
from pysat.solvers import Solver
from pysat.card import ITotalizer
import t1_minflip as T

MODE = sys.argv[1] if __name__ == "__main__" else None
BOX = int(sys.argv[2]) if __name__ == "__main__" else None


def encode(base, orb, nor, box, fixedA=None, faithful=False, twisted=False):
    sites = list(itertools.product(range(box), repeat=3))
    xv = {s: i + 1 + nor for i, s in enumerate(sites)}
    top = nor + len(sites)
    clauses = []
    Bc = T.base_patterns(base, orb)
    for o in Bc:
        clauses.append([o + 1])
    if fixedA is not None:
        for o in range(nor):
            clauses.append([o + 1] if o in fixedA else [-(o + 1)])
    if faithful:
        for f in range(64):
            c0 = f << 1
            c1 = c0 | 1
            clauses.append(sorted({orb[c0] + 1, orb[c1] + 1}))
    centres = set()
    for s in sites:
        for t in T.star_sites(s):
            centres.add(t)
    for r in centres:
        ss = T.star_sites(r)
        inbox = [(j, xv[s]) for j, s in enumerate(ss) if s in xv]
        b = base.star(r)
        for tau in range(1, 1 << len(inbox)):
            cfg = b
            lits = []
            for q, (j, v) in enumerate(inbox):
                if (tau >> q) & 1:
                    cfg ^= 1 << j
                    lits.append(-v)
                else:
                    lits.append(v)
            o = orb[cfg]
            if o in Bc:
                continue
            clauses.append(lits + [o + 1])
    allx = [xv[s] for s in sites]
    clauses.append(allx)
    p = base.period
    for ax in range(3):
        clauses.append([xv[s] for s in sites if s[ax] < p[ax]])
    return sites, xv, top, clauses, allx, Bc


def min_flip_fixed(base, orb, nor, box, A, ub):
    sites, xv, top, clauses, allx, Bc = encode(base, orb, nor, box, fixedA=A)
    tot = ITotalizer(lits=allx, ubound=ub, top_id=top)
    s = Solver(name='cadical153', bootstrap_with=clauses + tot.cnf.clauses)
    if not s.solve():
        s.delete()
        return None, None
    m = s.get_model()
    best = [x for x in sites if m[xv[x] - 1] > 0]
    lo, hi = 1, min(len(best), ub)
    # invariant: a flip of size hi exists; none of size < lo
    while lo < hi:
        mid = (lo + hi) // 2
        if s.solve(assumptions=[-tot.rhs[mid]]):
            m = s.get_model()
            best = [x for x in sites if m[xv[x] - 1] > 0]
            hi = len(best)
        else:
            lo = mid + 1
    s.delete()
    return hi, best


def bases_by_name():
    d = {}
    for b in T.period2_bases() + T.layered_bases(3) + T.layered_bases(4):
        d[b.name] = b
    return d


if MODE == 'stab':
    # rules found at box 5 (trivial action): pattern sets transcribed from t1_all_b5.out
    orb, reps = T.orbits(False)
    nor = len(reps)
    name_of = {T.describe(reps[o]): o for o in range(nor)}
    cases = {
        'p2:00000001': "c=0 f={}; c=1 f={}; c=1 f={+x}; c=0 f={+x,-x}; c=1 f={+x,+y}; c=0 f={+x,-x,+y}; c=0 f={+x,+y,+z}; c=1 f={+x,-x,+y,-y,+z,-z}",
        'p2:00011011': "c=0 f={+x}; c=0 f={+x,-x}; c=1 f={+x,-x}; c=1 f={+x,+y}; c=0 f={+x,-x,+y}; c=0 f={+x,-x,+y,-y}; c=1 f={+x,-x,+y,-y}; c=1 f={+x,-x,+y,+z}",
        'p2:00000110': "c=0 f={}; c=1 f={}; c=0 f={+x}; c=0 f={+x,-x}; c=0 f={+x,+y}; c=1 f={+x,+y}; c=1 f={+x,-x,+y}; c=0 f={+x,-x,+y,-y}; c=1 f={+x,-x,+y,-y}; c=0 f={+x,+y,+z}; c=1 f={+x,-x,+y,+z}; c=0 f={+x,-x,+y,-y,+z}; c=1 f={+x,-x,+y,-y,+z}",
        'p2:01101001': "c=1 f={}; c=1 f={+x}; c=0 f={+x,+y}; c=1 f={+x,+y}; c=0 f={+x,-x,+y,+z}; c=0 f={+x,-x,+y,-y,+z}; c=0 f={+x,-x,+y,-y,+z,-z}",
    }
    bb = bases_by_name()
    for nm, desc in cases.items():
        A = {name_of[x.strip()] for x in desc.split(';')}
        t0 = time.time()
        m, S = min_flip_fixed(bb[nm], orb, nor, BOX, A, ub=min(BOX ** 3, 150))
        print(f"{nm} box={BOX} minflip={m} t={time.time()-t0:.1f}s", flush=True)
        if m is not None and m <= 30:
            print("   S=", S, flush=True)
elif MODE == 'faithful':
    for action in ['trivial', 'twist']:
        orb, reps = T.orbits(action == 'twist')
        nor = len(reps)
        overall = 0
        for base in T.period2_bases() + T.layered_bases(3) + T.layered_bases(4):
            t0 = time.time()
            sites, xv, top, clauses, allx, Bc = encode(base, orb, nor, BOX, faithful=True)
            tot = ITotalizer(lits=allx, ubound=min(len(allx), 150), top_id=top)
            s = Solver(name='cadical153', bootstrap_with=clauses + tot.cnf.clauses)
            best = (0, None, None)
            rounds = 0
            while s.solve():
                rounds += 1
                model = s.get_model()
                Afull = {o for o in range(nor) if model[o] > 0}
                S = [x for x in sites if model[xv[x] - 1] > 0]
                # minimal-ish candidate: base + patterns of S + model's support completion
                need = set(Bc)
                Sset = set(S)
                cs = set(t for x in S for t in T.star_sites(x))
                for r in cs:
                    cfg = base.star(r)
                    for j, q in enumerate(T.star_sites(r)):
                        if q in Sset:
                            cfg ^= 1 << j
                    need.add(orb[cfg])
                for f in range(64):
                    o0, o1 = orb[f << 1], orb[(f << 1) | 1]
                    if o0 not in need and o1 not in need:
                        need.add(o0 if o0 in Afull else o1)
                assum = [(o + 1) if o in need else -(o + 1) for o in range(nor)]
                lo, hi = 1, len(S)
                Smin = S
                while lo < hi:
                    mid = (lo + hi) // 2
                    if mid < len(tot.rhs) and s.solve(assumptions=assum + [-tot.rhs[mid]]):
                        mm = s.get_model()
                        Smin = [x for x in sites if mm[xv[x] - 1] > 0]
                        hi = len(Smin)
                    else:
                        lo = mid + 1
                if hi > best[0]:
                    best = (hi, sorted(need), sorted(Smin))
                Sset = set(Smin)
                cs = set(t for x in Smin for t in T.star_sites(x))
                pats = set()
                for r in cs:
                    cfg = base.star(r)
                    for j, q in enumerate(T.star_sites(r)):
                        if q in Sset:
                            cfg ^= 1 << j
                    pats.add(orb[cfg])
                blk = [-(o + 1) for o in pats if o not in Bc]
                if not blk:
                    break
                s.add_clause(blk)
            s.delete()
            overall = max(overall, best[0])
            print(f"[{action}] {base.name:16s} rounds={rounds:4d} maxfinite_minflip={best[0]:3d} t={time.time()-t0:.1f}s", flush=True)
            if best[0] >= 9:
                print("    rule needs:", '; '.join(T.describe(reps[o]) for o in best[1]), flush=True)
                if best[0] <= 30:
                    print("    flip:", best[2], flush=True)
        print(f"== faithful [{action}] OVERALL max finite minimal flip (box {BOX}) = {overall}", flush=True)
