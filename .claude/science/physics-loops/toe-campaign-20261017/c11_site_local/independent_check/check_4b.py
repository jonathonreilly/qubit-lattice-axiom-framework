"""Item (4), general pair test (directly in the half-edge model; edge model as cross-check).

For code o, a C2 rotation R in its stabilizer, and an off-axis vertex x:
  S0 = hop string of A^o from x to Rx (it flips only B_x, B_Rx);
  solve over GF(2) for C supported on the radius-r boxes around x and Rx with
      syn(S0 C) = syn((S0 C)^R),    (S0 C)^R = P_R (S0 C) P_R^-1  (bare site permutation)
  then T = (S0 C)^dag (S0 C)^R commutes with every generator; lambda = eigenvalue of T on the
  code space (T must lie in +-G). lambda is the P_R eigenvalue of S|vac> relative to |vac>.
Robustness: lambda is recomputed for several random solutions (nullspace shifts) and two x.
"""
import itertools, sys, time, collections, random
from ilib import *

random.seed(1)
t0 = time.time()
ORD = list(itertools.permutations(range(6)))
ROTS = rotations()
L = int(sys.argv[1]) if len(sys.argv) > 1 else 8
RAD = int(sys.argv[2]) if len(sys.argv) > 2 else 1
NRAND = 6
MIND = int(sys.argv[3]) if len(sys.argv) > 3 else 4
XR = int(sys.argv[4]) if len(sys.argv) > 4 else 2

# ---- code reps + stabilizers (L=4 classification)
H4 = HalfModel(4)
def base_gens(model, o, sec=(1, 1, 1)):
    return [S(model, o, (0, 0, 0), a, b, sec[normal(a, b)]) for (a, b) in PLANES]
reps = []
for o in ORD:
    if any(all(sp.eig(P) is not None for P in base_gens(H4, o)) for (_, sp) in reps):
        continue
    reps.append((o, span_of(H4, generators(H4, o))))
codes = []
for (o, sp) in reps:
    st = [M for M in ROTS if all(sp.eig(permute_pauli(P, H4.rot_qubit_perm(M))) is not None
                                 for P in base_gens(H4, o))]
    codes.append((o, st))
assert len(codes) == 60


def hop(model, o, u, d):
    a, s = DIRS[d]
    if s == 1:
        return model.A(o, u, a)
    w = list(u); w[a] -= 1
    return model.A(o, tuple(w), a)


def path(x, y):
    steps = []; u = list(x)
    for a in range(3):
        while u[a] != y[a]:
            s = 1 if y[a] > u[a] else -1
            steps.append((tuple(u), DIDX[(a, s)])); u[a] += s
    return steps


def string(model, o, x, y):
    P = (0, 0, 0)
    for (u, d) in path(x, y):
        P = pmul(P, hop(model, o, u, d))
    return P


def qubits_near(model, centre, r):
    lat = model.lat
    out = []
    per = 6 if isinstance(model, HalfModel) else 3
    seen = set()
    for dv in itertools.product(range(-r, r + 1), repeat=3):
        v = tuple(c + d for c, d in zip(centre, dv))
        i = lat.vid(v)
        if i in seen:
            continue
        seen.add(i)
        if per == 6:
            out.extend(range(6 * i, 6 * i + 6))
        else:
            # edge model: only edges with both endpoints inside the box (no bridging between boxes)
            for a in range(3):
                if dv[a] < r:
                    out.append(3 * i + a)
    return out


def gen_masks(model, gens):
    xg = [0] * model.n   # generators with X on q (anticommute with Z_q)
    zg = [0] * model.n   # generators with Z on q (anticommute with X_q)
    for gi, (x, z, k) in enumerate(gens):
        b = 1 << gi
        xx = x
        while xx:
            low = xx & -xx; q = low.bit_length() - 1; xg[q] |= b; xx ^= low
        zz = z
        while zz:
            low = zz & -zz; q = low.bit_length() - 1; zg[q] |= b; zz ^= low
    return xg, zg


def syn(P, xg, zg):
    s = 0
    x, z, _ = P
    while x:
        low = x & -x; s ^= zg[low.bit_length() - 1]; x ^= low
    while z:
        low = z & -z; s ^= xg[low.bit_length() - 1]; z ^= low
    return s


def solve(cols, target):
    """cols: list of ints; find subset XOR == target. returns (solution mask, nullspace masks) or None"""
    basis = {}  # leading bit -> (vec, combo)
    null = []
    for j, c in enumerate(cols):
        combo = 1 << j
        while c:
            hb = c.bit_length() - 1
            if hb in basis:
                bv, bc = basis[hb]; c ^= bv; combo ^= bc
            else:
                basis[hb] = (c, combo); break
        if c == 0:
            null.append(combo)
    t = target; combo = 0
    while t:
        hb = t.bit_length() - 1
        if hb not in basis:
            return None
        bv, bc = basis[hb]; t ^= bv; combo ^= bc
    return combo, null


def pair_lambda(model, o, M, x, spans, xg, zg, gens, nB):
    perm = model.rot_qubit_perm(M)
    Rx = mvec(M, x)
    S0 = string(model, o, x, Rx)
    S0R = permute_pauli(S0, perm)
    delta = syn(S0, xg, zg) ^ syn(S0R, xg, zg)
    qs = sorted(set(qubits_near(model, x, RAD)) | set(qubits_near(model, Rx, RAD)))
    cols = []
    basisP = []
    for q in qs:
        cols.append(zg[q] ^ zg[perm[q]]); basisP.append((1 << q, 0, 0))
        cols.append(xg[q] ^ xg[perm[q]]); basisP.append((0, 1 << q, 0))
    sol = solve(cols, delta)
    if sol is None:
        return None
    combo, null = sol
    out = {}
    trials = [combo] + [combo ^ (random.choice(null) if null else 0) ^ (random.choice(null) if null else 0)
                        for _ in range(NRAND)]
    Bmask = 0
    lamset = collections.defaultdict(set)
    bsyn_ok = True
    nper = len(gens) // model.lat.N
    for cm in trials:
        C = (0, 0, 0)
        j = 0
        while cm:
            if cm & 1:
                C = pmul(C, basisP[j])
            cm >>= 1; j += 1
        Sx = pmul(S0, C)
        SR = permute_pauli(Sx, perm)
        assert syn(Sx, xg, zg) == syn(SR, xg, zg)
        # vertex-generator syndrome parity near x must be odd (fermion), check B flips
        # (a) vertex-generator (B) flips: parity in the box of x / of Rx (naive charge)
        sx = syn(Sx, xg, zg)
        def near(v, c, r=RAD + 1):
            return all(min((a - b) % L, (b - a) % L) <= r for a, b in zip(v, c))
        bfl = [model.lat.vec(gi // nper) for gi in range(len(gens)) if (sx >> gi) & 1 and gi % nper == 0]
        lamset['Bparity'].add((sum(near(v, x) for v in bfl) % 2, sum(near(v, Rx) for v in bfl) % 2))
        # (b) gauge-invariant charge: commutation with Q_Omega = prod_{v in Omega} B_v * prod_{e inside Omega} R_e,
        #     Omega = box of radius RAD+1 around the centre (disjoint from the other centre since
        #     |x-Rx|_inf >= 4 > 2(RAD+1)-... and containing the whole correction support; in the edge model
        #     Q_Omega = prod B_v). Q_Omega = Z on the boundary-crossing qubits, so this is the flux through dOmega.
        def charge(c):
            Q = (0, 0, 0)
            for dv in itertools.product(range(-RAD - 1, RAD + 2), repeat=3):
                v = tuple(a + b for a, b in zip(c, dv))
                Q = pmul(Q, model.B(v))
                if isinstance(model, HalfModel):
                    for a in range(3):
                        if dv[a] < RAD + 1:
                            Q = pmul(Q, model.R(v, a))
            return 0 if commute(Q, Sx) else 1
        # (c) no excitation outside the radius-(RAD+2) boxes (vertex, repetition or plaquette generators)
        far = 0
        for gi in range(len(gens)):
            if (sx >> gi) & 1:
                v = model.lat.vec(gi // nper)
                if not near(v, x, RAD + 2) and not near(v, Rx, RAD + 2):
                    far += 1
        key3 = (charge(x), charge(Rx), far)
        lamset['charge(x,Rx,far)'].add(key3)
        if key3 != (1, 1, 0):
            lamset['invalid_trial'].add(True)
            continue
        T = pmul(pdag(Sx), SR)
        for key, sp in spans.items():
            e = sp.eig(T)
            lamset[key].add(None if e is None else {0: 1, 2: -1, 1: 'i', 3: '-i'}[e])
    return {k: tuple(sorted(v, key=str)) for k, v in lamset.items()}


def xs_for(M):
    pts = []
    for x in itertools.product(range(-XR, XR + 1), repeat=3):
        Rx = mvec(M, x)
        d = max(abs(a - b) for a, b in zip(x, Rx))
        if d >= MIND:
            pts.append((sum(abs(c) for c in x), x))
    pts.sort()
    return [pts[0][1], pts[-1][1]]


models = {'half': HalfModel(L), 'edge': EdgeModel(L), 'half_Rminus': HalfModel(L, rsign=-1)}
summary = collections.Counter()
fails = []
npairs = 0
for ci, (o, st) in enumerate(codes):
    otype = {4: 'D3', 6: 'D2', 12: 'Z2'}[24 // len(st)]
    c2s = [M for M in st if rot_type(M).startswith('C2')]
    if not c2s:
        continue
    pre = {}
    for name, model in models.items():
        spans = {}
        for sec in [(1, 1, 1), (-1, -1, -1)]:
            g = generators(model, o, sec)
            spans[sec] = span_of(model, g)
            assert spans[sec].consistent
        g = generators(model, o)
        xg, zg = gen_masks(model, g)
        pre[name] = (spans, xg, zg, g)
    for M in c2s:
        npairs += 1
        for x in xs_for(M):
            for name, model in models.items():
                spans, xg, zg, g = pre[name]
                res = pair_lambda(model, o, M, x, spans, xg, zg, g, None)
                if res is None:
                    summary[(name, otype, rot_type(M), 'nosolution')] += 1
                    fails.append((ci, M, x, name))
                    continue
                for sec, lam in res.items():
                    lab = {(1, 1, 1): 'flux0', (-1, -1, -1): 'fluxpi'}.get(sec, sec)
                    summary[(name, otype, rot_type(M), lab, lam)] += 1
    print('  .. code', ci + 1, round(time.time() - t0), 's', flush=True)
print('L =', L, 'radius', RAD, 'min |x-Rx|_inf', MIND, '(code, C2) pairs:', npairs)
for k, v in sorted(summary.items(), key=str):
    print('  ', k, v)
print('no-solution cases:', len(fails), fails[:5])
print('elapsed', round(time.time() - t0), 's')
