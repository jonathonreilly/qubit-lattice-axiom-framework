"""Items (1)-(3): commuting, code dimension, exact covariance, stabilizers/orbits."""
import itertools, sys, time, collections
from ilib import *

t0 = time.time()
ORD = list(itertools.permutations(range(6)))
ROTS = rotations()
L = 4
H = HalfModel(L)
E = EdgeModel(L)
res = {}

# ---------------- (1) commuting, consistent, log2 dim at L=4 for all 720 orderings (both models)
dims_h = collections.Counter()
dims_e = collections.Counter()
ok_comm = True
for o in ORD:
    gh = generators(H, o)
    ge = generators(E, o)
    if not all_commute(gh) or not all_commute(ge):
        ok_comm = False
    sh = span_of(H, gh)
    se = span_of(E, ge)
    dims_h[(H.n - sh.rank(), sh.consistent)] += 1
    dims_e[(E.n - se.rank(), se.consistent)] += 1
print('(1) L=4 all 720: commute', ok_comm, 'half dims', dict(dims_h), 'edge dims', dict(dims_e), flush=True)

# ---------------- classify into codes (unsigned group equality), half-edge model, L=4
def base_gens(model, o):
    v0 = (0, 0, 0)
    return [S(model, o, v0, a, b) for (a, b) in PLANES]

def classify(model):
    reps = []  # (o, span)
    cls = {}
    for o in ORD:
        found = None
        for idx, (ro, sp) in enumerate(reps):
            if all(sp.eig(P) is not None for P in base_gens(model, o)):
                found = idx
                break
        if found is None:
            sp = span_of(model, generators(model, o))
            reps.append((o, sp))
            found = len(reps) - 1
        cls[o] = found
    return reps, cls

reps_h, cls_h = classify(H)
reps_e, cls_e = classify(E)
# same partition?
part_h = collections.defaultdict(set)
part_e = collections.defaultdict(set)
for o in ORD:
    part_h[cls_h[o]].add(o)
    part_e[cls_e[o]].add(o)
same_part = set(frozenset(s) for s in part_h.values()) == set(frozenset(s) for s in part_e.values())
print('codes: half', len(reps_h), 'edge', len(reps_e), 'same partition', same_part, flush=True)

# ---------------- (1b) L=6 dims for one rep of each code (all 60)
H6 = HalfModel(6)
d6 = collections.Counter()
for (o, _) in reps_h:
    g = generators(H6, o)
    sp = span_of(H6, g)
    d6[(H6.n - sp.rank(), sp.consistent)] += 1
print('(1b) L=6 half dims over 60 reps', dict(d6), flush=True)

# ---------------- (2) exact covariance of A, B, R under the site action
def rot_ordering(M, o):
    return tuple(rot_dir(M, d) for d in o)

perms_h = {M: H.rot_qubit_perm(M) for M in ROTS}
lat = H.lat
bad2 = 0
nchk = 0
for M in ROTS:
    perm = perms_h[M]
    for v in lat.verts():
        Rv = mvec(M, v)
        # B, R
        if permute_pauli(H.B(v), perm) != H.B(Rv):
            bad2 += 1
        for a in range(3):
            w = lat.add(v, a)
            d2 = rot_dir(M, a)
            b, s = DIRS[d2]
            # rotated edge: tail Rv if s=+1, else R(v+e_a)
            tail = Rv if s == 1 else mvec(M, w)
            if permute_pauli(H.R(v, a), perm) != H.R(tail, b):
                bad2 += 1
    for o in ORD:
        Ro = rot_ordering(M, o)
        for v in lat.verts():
            Rv = mvec(M, v)
            for a in range(3):
                w = lat.add(v, a)
                b, s = DIRS[rot_dir(M, a)]
                tail = Rv if s == 1 else mvec(M, w)
                nchk += 1
                if permute_pauli(H.A(o, v, a), perm) != H.A(Ro, tail, b):
                    bad2 += 1
print('(2) site action: A^o_e -> A^{Ro}_{Re} exact (incl. phase), B->B, R->R: checks', nchk, 'failures', bad2,
      round(time.time() - t0), 's', flush=True)

# ---------------- (3) stabilizers under site action (half-edge) and edge action (edge model), computed
# directly by permuting generators and testing membership (no use of item (2)).
perms_e = {M: E.rot_qubit_perm(M) for M in ROTS}

def stab(model, perms, o, sp):
    out = []
    for M in ROTS:
        perm = perms[M]
        ok = True
        v0 = (0, 0, 0)
        imgs = [permute_pauli(P, perm) for P in base_gens(model, o)]
        imgs.append(permute_pauli(model.B(v0), perm))
        imgs += [permute_pauli(P, perm) for P in model.gens_extra(v0)]
        for P in imgs:
            if sp.eig(P) is None:
                ok = False
                break
        if ok:
            out.append(M)
    return out

same_stab = True
orbit_info = collections.Counter()
types = collections.Counter()
for idx, (o, sp) in enumerate(reps_h):
    st_h = stab(H, perms_h, o, sp)
    # edge span for the same ordering
    sp_e = reps_e[cls_e[o]][1]
    st_e = stab(E, perms_e, o, sp_e)
    if set(st_h) != set(st_e):
        same_stab = False
    orbit_info[24 // len(st_h)] += 1
    types[(24 // len(st_h), tuple(sorted(collections.Counter(rot_type(M) for M in st_h).items())))] += 1
print('(3) site stabilizer == edge stabilizer for all 60:', same_stab, flush=True)
print('    orbit size -> #codes:', dict(orbit_info))
for k, v in sorted(types.items()):
    print('   ', k, v)
print('elapsed', round(time.time() - t0), 's')
