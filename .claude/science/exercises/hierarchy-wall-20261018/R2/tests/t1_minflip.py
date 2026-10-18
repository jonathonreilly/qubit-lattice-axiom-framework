"""T1: largest finite minimal flip over all one-bit cubic-covariant star support rules.

Declared model: a rule is a set A of allowed star configurations (centre bit,
six face bits), closed under the 24 proper rotations (trivial or sign-twisted
action on the bit).  Given a valid periodic base configuration c, a flip S is a
finite nonempty set of sites such that c xor 1_S is valid.  We compute
M(c) = max over rules A (with c valid) of min |S|, over flips inside a B^3 box,
exactly, by a CEGAR loop with a SAT solver.

usage: python3 t1_minflip.py BOX [action] [basefamily]
"""
import itertools, sys, time
from pysat.solvers import Solver
from pysat.card import ITotalizer

if __name__ == '__main__':
    BOX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    ACTIONS = [sys.argv[2]] if len(sys.argv) > 2 else ['trivial', 'twist']
    FAMILY = sys.argv[3] if len(sys.argv) > 3 else 'all'

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        # sign of permutation
        inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
        psign = -1 if inv % 2 else 1
        for signs in itertools.product([1, -1], repeat=3):
            det = psign * signs[0] * signs[1] * signs[2]
            if det != 1:
                continue
            M = [[0] * 3 for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            out.append((M, psign))
    assert len(out) == 24
    return out


ROTS = rotations()


def apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def face_perm(M):
    return [DIRS.index(apply(M, d)) for d in DIRS]


FPERMS = [(face_perm(M), chi) for (M, chi) in ROTS]


def act(fp, chi, cfg, twisted):
    new = cfg & 1
    for i in range(6):
        if (cfg >> (1 + i)) & 1:
            new |= 1 << (1 + fp[i])
    if twisted and chi == -1:
        new ^= 127
    return new


def orbits(twisted):
    orb = [-1] * 128
    reps = []
    for c in range(128):
        if orb[c] >= 0:
            continue
        k = len(reps)
        reps.append(c)
        stack = [c]
        orb[c] = k
        while stack:
            d = stack.pop()
            for fp, chi in FPERMS:
                e = act(fp, chi, d, twisted)
                if orb[e] < 0:
                    orb[e] = k
                    stack.append(e)
    return orb, reps


def describe(cfg):
    ctr = cfg & 1
    faces = [i for i in range(6) if (cfg >> (1 + i)) & 1]
    names = ['+x', '-x', '+y', '-y', '+z', '-z']
    return f"c={ctr} f={{{','.join(names[i] for i in faces)}}}"


def star_sites(r):
    return [r] + [(r[0] + d[0], r[1] + d[1], r[2] + d[2]) for d in DIRS]


class Base:
    def __init__(self, period, bits, name):
        self.period = period  # (px,py,pz)
        self.bits = bits      # dict (x%px,y%py,z%pz) -> bit
        self.name = name

    def __call__(self, r):
        p = self.period
        return self.bits[(r[0] % p[0], r[1] % p[1], r[2] % p[2])]

    def star(self, r):
        cfg = 0
        for j, s in enumerate(star_sites(r)):
            if self(s):
                cfg |= 1 << j
        return cfg


def base_patterns(base, orb):
    p = base.period
    pats = set()
    for r in itertools.product(range(p[0]), range(p[1]), range(p[2])):
        pats.add(orb[base.star(r)])
    return pats


def run_base(base, orb, nor, box, verbose=False):
    sites = list(itertools.product(range(box), repeat=3))
    xv = {s: i + 1 + nor for i, s in enumerate(sites)}  # a-vars are 1..nor
    top = nor + len(sites)
    clauses = []
    Bc = base_patterns(base, orb)
    for o in Bc:
        clauses.append([o + 1])
    # centres whose star meets the box
    centres = set()
    for s in sites:
        for t in star_sites(s):
            centres.add(t)
    for r in centres:
        ss = star_sites(r)
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
    tot = ITotalizer(lits=allx, ubound=min(len(allx), 60), top_id=top)
    solver = Solver(name='cadical153', bootstrap_with=clauses + tot.cnf.clauses)

    def patterns_of(S):
        Sset = set(S)
        pats = set()
        cs = set()
        for s in S:
            for t in star_sites(s):
                cs.add(t)
        for r in cs:
            cfg = base.star(r)
            for j, s in enumerate(star_sites(r)):
                if s in Sset:
                    cfg ^= 1 << j
            pats.add(orb[cfg])
        return pats

    best = (0, None, None)
    rounds = 0
    while solver.solve():
        rounds += 1
        model = solver.get_model()
        S = [s for s in sites if model[xv[s] - 1] > 0]
        Acand = Bc | patterns_of(S)
        assum = [(o + 1) if o in Acand else -(o + 1) for o in range(nor)]
        m_found = None
        Smin = None
        for k in range(1, len(S) + 1):
            if k >= 60:
                break
            if solver.solve(assumptions=assum + [-tot.rhs[k]] if k < len(tot.rhs) else assum):
                mm = solver.get_model()
                Smin = [s for s in sites if mm[xv[s] - 1] > 0]
                m_found = len(Smin)
                break
        if m_found is None:
            Smin = S
            m_found = len(S)
        if m_found > best[0]:
            best = (m_found, sorted(Acand), sorted(Smin))
        blk = [-(o + 1) for o in patterns_of(Smin) if o not in Bc]
        if not blk:
            break
        solver.add_clause(blk)
    solver.delete()
    return best, rounds, Bc


def period2_bases():
    seen = set()
    out = []
    cells = list(itertools.product(range(2), repeat=3))
    for code in range(256):
        bits = {c: (code >> i) & 1 for i, c in enumerate(cells)}
        # canonical form under rotations, translations, global flip
        forms = []
        for (M, chi) in ROTS:
            for t in cells:
                for fl in (0, 1):
                    nb = 0
                    for i, c in enumerate(cells):
                        # value at cell c of transformed base: bits[g^-1 (c - t)]
                        # use g^T for inverse of signed permutation
                        v = (c[0] - t[0], c[1] - t[1], c[2] - t[2])
                        MT = [[M[j][i2] for j in range(3)] for i2 in range(3)]
                        w = apply(MT, v)
                        w = (w[0] % 2, w[1] % 2, w[2] % 2)
                        nb |= ((bits[w] ^ fl) << i)
                    forms.append(nb)
        can = min(forms)
        if can in seen:
            continue
        seen.add(can)
        b = {c: (can >> i) & 1 for i, c in enumerate(cells)}
        out.append(Base((2, 2, 2), b, f"p2:{can:08b}"))
    return out


def layered_bases(p):
    seen = set()
    out = []
    for code in range(1 << p):
        forms = []
        for t in range(p):
            for refl in (1, -1):
                for fl in (0, 1):
                    nb = 0
                    for z in range(p):
                        w = (refl * (z - t)) % p
                        nb |= (((code >> w) & 1) ^ fl) << z
                    forms.append(nb)
        can = min(forms)
        if can in seen:
            continue
        seen.add(can)
        b = {(0, 0, z): (can >> z) & 1 for z in range(p)}
        out.append(Base((1, 1, p), b, f"layer{p}:{''.join(str((can >> z) & 1) for z in range(p))}"))
    return out


if __name__ == '__main__':
    bases = []
    if FAMILY in ('all', 'p2'):
        bases += period2_bases()
    if FAMILY in ('all', 'layer'):
        bases += layered_bases(3) + layered_bases(4)
    if FAMILY == 'uniform':
        bases = [period2_bases()[0]]
    print(f"BOX={BOX} actions={ACTIONS} bases={len(bases)}", flush=True)
    for action in ACTIONS:
        orb, reps = orbits(action == 'twist')
        nor = len(reps)
        print(f"== action {action}: {nor} star orbits", flush=True)
        overall = 0
        for base in bases:
            t0 = time.time()
            best, rounds, Bc = run_base(base, orb, nor, BOX)
            overall = max(overall, best[0])
            line = f"{base.name:16s} |Bc|={len(Bc):2d} rounds={rounds:4d} maxfinite_minflip={best[0]:3d} t={time.time()-t0:6.1f}s"
            print(line, flush=True)
            if best[0] >= 5:
                print("    rule needs:", '; '.join(describe(reps[o]) for o in best[1]), flush=True)
                print("    flip:", best[2], flush=True)
        print(f"== action {action}: OVERALL max finite minimal flip (box {BOX}) = {overall}", flush=True)
