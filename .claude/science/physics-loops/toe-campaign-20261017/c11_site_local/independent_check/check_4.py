"""Item (4): phase-sensitive transfer tests directly in the half-edge (site-local) model.

- T-junction sign (Levin-Wen) in the half-edge model;
- signed sectors: validity and bare site-action invariance (flux 0 / flux pi / mixed);
- pair test lambda = P_R eigenvalue of S|vac> relative to vac, S a hop string x -> Rx,
  for every C2 in the stabilizer of every code, both uniform sectors; edge model cross-check;
- repetition-code sign R = -ZZ variant;
- controls: toric code (no ordering Z's) boson, and pi-flux boson under a plaquette-centred C2.
"""
import itertools, sys, time, collections
from ilib import *

t0 = time.time()
ORD = list(itertools.permutations(range(6)))
ROTS = rotations()
L = int(sys.argv[1]) if len(sys.argv) > 1 else 6


def rot_ordering(M, o):
    return tuple(rot_dir(M, d) for d in o)


# --- code representatives and stabilizers (unsigned, L=4 classification is cheap; recomputed here)
H4 = HalfModel(4)

def base_gens(model, o):
    return [S(model, o, (0, 0, 0), a, b) for (a, b) in PLANES]

reps = []
for o in ORD:
    if any(all(sp.eig(P) is not None for P in base_gens(H4, o)) for (_, sp) in reps):
        continue
    reps.append((o, span_of(H4, generators(H4, o))))
assert len(reps) == 60

def stab4(o, sp):
    out = []
    for M in ROTS:
        perm = H4.rot_qubit_perm(M)
        if all(sp.eig(permute_pauli(P, perm)) is not None for P in base_gens(H4, o)):
            out.append(M)
    return out

codes = []
for (o, sp) in reps:
    st = stab4(o, sp)
    codes.append((o, st))
print('60 codes; stabilizer orders', collections.Counter(len(st) for _, st in codes), flush=True)


# --- general site map v -> M v + t on the half-edge model
def site_perm(model, M, t=(0, 0, 0)):
    lat = model.lat
    perm = [0] * model.n
    for i in range(lat.N):
        v = lat.vec(i)
        Rv = tuple(c + tt for c, tt in zip(mvec(M, v), t))
        for d in range(6):
            perm[6 * i + d] = model.q(Rv, rot_dir(M, d))
    return perm


def hop(model, o, u, d):
    """hop operator for the step u -> u + d (d a direction index)"""
    a, s = DIRS[d]
    if s == 1:
        return model.A(o, u, a)
    w = list(u)
    w[a] -= 1
    return model.A(o, tuple(w), a)


def path(x, y):
    """Manhattan path in Z^3 (unwrapped), as list of (u, d)"""
    steps = []
    u = list(x)
    for a in range(3):
        while u[a] != y[a]:
            s = 1 if y[a] > u[a] else -1
            steps.append((tuple(u), DIDX[(a, s)]))
            u[a] += s
    return steps


def string(model, o, x, y):
    P = (0, 0, 0)
    for (u, d) in path(x, y):
        P = pmul(P, hop(model, o, u, d))
    return P


def secname(sec):
    return {(1, 1, 1): 'flux0', (-1, -1, -1): 'fluxpi'}.get(sec, 'mixed' + str(sec))


# ================= T-junction in the half-edge model (L given), a sample of codes
def tjunction(model, o, c=(0, 0, 0), ell=2):
    results = []
    for tri in itertools.combinations(range(6), 3):
        U = []
        for d in tri:
            end = c
            for _ in range(ell):
                end = model.lat.add(end, d)
            U.append(string(model, o, c, end))
        lhs = pmul(pmul(U[0], pdag(U[1])), U[2])
        rhs = pmul(pmul(U[2], pdag(U[1])), U[0])
        assert lhs[:2] == rhs[:2]
        results.append(1 if lhs[2] == rhs[2] else (-1 if (lhs[2] - rhs[2]) % 4 == 2 else None))
    return results

Ht = HalfModel(L)
tj = collections.Counter()
for (o, st) in codes:
    r = tjunction(Ht, o)
    tj[tuple(sorted(collections.Counter(r).items()))] += 1
print('T-junction (half-edge, L=%d, 60 codes, 20 triples each):' % L, dict(tj), flush=True)


# toric-code control: model with no ordering Z's
class TCHalf(HalfModel):
    def A(self, o, v, a):
        w = self.lat.add(v, a)
        return ((1 << self.q(v, a)) | (1 << self.q(w, a + 3)), 0, 0)

tc = TCHalf(L)
print('T-junction toric-code control:', collections.Counter(tjunction(tc, None)), flush=True)


# ================= signed sectors and pair test
SECS = list(itertools.product([1, -1], repeat=3))


def pair_test(model, o, sec, M, xs, perm=None):
    g = generators(model, o, sec)
    sp = span_of(model, g)
    if not sp.consistent:
        return 'inconsistent', None
    if perm is None:
        perm = model.rot_qubit_perm(M)
    # P_R preserves signed group?  check images of base generators (translation covariance)
    v0 = (0, 0, 0)
    base = [model.B(v0)] + model.gens_extra(v0) + [S(model, o, v0, a, b, sec[normal(a, b)]) for (a, b) in PLANES]
    eigs = [sp.eig(permute_pauli(P, perm)) for P in base]
    sym = all(e == 0 for e in eigs)
    lams = []
    for x in xs:
        Rx = tuple(cc + tt for cc, tt in zip(mvec(M, x), (0, 0, 0)))
        Sx = string(model, o, x, Rx)
        SR = permute_pauli(Sx, perm)
        T = pmul(pdag(Sx), SR)
        e = sp.eig(T)
        lams.append(None if e is None else {0: 1, 2: -1, 1: 'i', 3: '-i'}[e])
    return sym, lams


def offaxis_points(M):
    """two vertices x with x != Rx, |x - Rx| >= 2 (unwrapped), small"""
    pts = []
    for x in itertools.product(range(-2, 3), repeat=3):
        Rx = mvec(M, x)
        dist = sum(abs(a - b) for a, b in zip(x, Rx))
        if dist >= 3:
            pts.append((dist, sum(abs(c) for c in x), x))
    pts.sort()
    return [pts[0][2], pts[len(pts) // 3][2]]


H = HalfModel(L)
E = EdgeModel(L)
Hm = HalfModel(L, rsign=-1)
summary = collections.Counter()
detail = []
npairs = 0
for ci, (o, st) in enumerate(codes):
    otype = {24 // 4: 'D3', 24 // 6: 'D2', 24 // 12: 'Z2'}[len(st)]
    for M in st:
        rt = rot_type(M)
        if not rt.startswith('C2'):
            continue
        npairs += 1
        xs = offaxis_points(M)
        for sec in [(1, 1, 1), (-1, -1, -1)]:
            symH, lamH = pair_test(H, o, sec, M, xs)
            symE, lamE = pair_test(E, o, sec, M, xs)
            symM, lamM = pair_test(Hm, o, sec, M, xs)
            summary[('half', secname(sec), symH, tuple(lamH))] += 1
            summary[('edge', secname(sec), symE, tuple(lamE))] += 1
            summary[('half R=-ZZ', secname(sec), symM, tuple(lamM) if lamM else None)] += 1
            detail.append((ci, otype, rt, sec, symH, lamH, symE, lamE, symM, lamM))
    if ci % 10 == 9:
        print('  ..', ci + 1, 'codes', round(time.time() - t0), 's', flush=True)
print('pairs (code, C2):', npairs)
for k, v in sorted(summary.items(), key=str):
    print('  ', k, v)

# ================= mixed sectors: bare site action invariance (half vs edge), count codes needing correction
mixed_bad_h = collections.Counter()
mixed_bad_e = collections.Counter()
H4p = {M: H4.rot_qubit_perm(M) for M in ROTS}
E4 = EdgeModel(4)
E4p = {M: E4.rot_qubit_perm(M) for M in ROTS}
for sec in SECS:
    for (o, st) in codes:
        for model, perms, ctr in ((H4, H4p, mixed_bad_h), (E4, E4p, mixed_bad_e)):
            sp = span_of(model, generators(model, o, sec))
            assert sp.consistent
            v0 = (0, 0, 0)
            base = [model.B(v0)] + model.gens_extra(v0) + [S(model, o, v0, a, b, sec[normal(a, b)]) for (a, b) in PLANES]
            bad = any(any(sp.eig(permute_pauli(P, perms[M])) != 0 for P in base) for M in st)
            if bad:
                ctr[sec] += 1
print('codes with a stabilizing rotation needing sign correction, per sector (half):', dict(mixed_bad_h))
print('                                                           (edge):', dict(mixed_bad_e))

# ================= controls with the half-edge site action
# pi-flux toric-code boson under a plaquette-centred C2 about z through (1/2,1/2,*): v -> (1-x, 1-y, z)
Mz = ((-1, 0, 0), (0, -1, 0), (0, 0, 1))
for sec in [(1, 1, 1), (-1, -1, -1)]:
    for label, t in (('vertex C2z', (0, 0, 0)), ('plaquette C2z', (1, 1, 0))):
        perm = site_perm(tc, Mz, t)
        g = generators(tc, None, sec)
        sp = span_of(tc, g)
        lam = []
        for x in [(2, 0, 0), (2, 1, 1), (3, -1, 0)]:
            Rx = tuple(c + tt for c, tt in zip(mvec(Mz, x), t))
            Sx = string(tc, None, x, Rx)
            T = pmul(pdag(Sx), permute_pauli(Sx, perm))
            e = sp.eig(T)
            lam.append(None if e is None else {0: 1, 2: -1}.get(e, e))
        print('control toric-code boson', secname(sec), label, lam)

print('elapsed', round(time.time() - t0), 's')
import pickle
pickle.dump(detail, open('check_4_detail_L%d.pkl' % L, 'wb'))
