"""A40 k1: which period-2 'kinds of places' patterns are state-level covariant?
Supplied toy combinatorics only.  A pattern K assigns a kind (0,1,2) to each parity class r in F2^3
(site y has class y mod 2).  A proper turn about site c acts on classes as r -> P(r-c)+c (mod 2),
P = permutation part (signs drop out mod 2).
 alone : for every turn g there is a translation t with K(g^-1 y) = K(y+t) for all y.
 joint : the same t must be the one that moves A25's role layout (s = 0): t = g(0) - 0 = g(0).
Expected: joint-covariant patterns = functions of the role (V, E, F, C) = 3^4 = 81.
"""
import itertools, signal
signal.alarm(28)
CL = list(itertools.product((0, 1), repeat=3))
PERMS = list(itertools.permutations(range(3)))

def act(P, c, r):
    d = tuple((r[i] - c[i]) % 2 for i in range(3))
    pd = tuple(d[P.index(i)] for i in range(3))   # (P d)_i = d_{P^-1 i}
    return tuple((pd[i] + c[i]) % 2 for i in range(3))

def inv_act(P, c, y):
    for r in CL:
        if act(P, c, r) == y:
            return r

def add(a, b):
    return tuple((a[i] + b[i]) % 2 for i in range(3))

TURNS = [(P, c) for P in PERMS for c in CL]
n_alone = n_joint = 0
joint_role = 0
alone_list = []
for vals in itertools.product(range(3), repeat=8):
    K = dict(zip(CL, vals))
    ok_alone = ok_joint = True
    for P, c in TURNS:
        Kg = {y: K[inv_act(P, c, y)] for y in CL}
        ts = [t for t in CL if all(Kg[y] == K[add(y, t)] for y in CL)]
        if not ts:
            ok_alone = ok_joint = False
            break
        if act(P, c, (0, 0, 0)) not in ts:
            ok_joint = False
    if ok_alone:
        n_alone += 1
        alone_list.append(vals)
    if ok_joint:
        n_joint += 1
        # role function?  same kind on classes of equal weight
        byw = {}
        rf = all(byw.setdefault(sum(r), K[r]) == K[r] for r in CL)
        joint_role += rf
print("patterns enumerated: 3^8 =", 3 ** 8)
print("covariant up to translation (alone):", n_alone)
print("jointly covariant with the role layout s=0:", n_joint, "; of these role functions:", joint_role)
# are all alone-covariant patterns role functions of some shifted layout s'?
def is_shifted_role_function(vals):
    K = dict(zip(CL, vals))
    for s in CL:
        byw = {}
        if all(byw.setdefault(sum(add(r, s)), K[r]) == K[r] for r in CL):
            return True
    return False
print("alone-covariant patterns that are role functions of some layout translate s':",
      sum(is_shifted_role_function(v) for v in alone_list), "of", n_alone)
# layered / axis-selective controls
ctrl = {'layered r_x': tuple(r[0] for r in CL),
        'E_x only matter': tuple(1 if r == (1, 0, 0) else 0 for r in CL),
        'checkerboard': tuple(sum(r) % 2 for r in CL)}
for name, v in ctrl.items():
    print("control", name, "alone-covariant:", v in alone_list)
