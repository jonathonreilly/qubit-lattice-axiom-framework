"""A45 f1: can covariant hops make Gauss-law point charges fermions under full soldering?

Lemma F (claimed EXACT): let g be a soldered half-turn about a coordinate axis (sites permuted
by g, every qubit conjugated by the same SU(2) lift of g).  For every Pauli monomial A,
A and gAg^dag commute.  Hence, for single-link hops t = (raise E_out on the hop link) x D with
D a Pauli monomial that is E-diagonal (I or sigma^axis) on the other link qubits and arbitrary
elsewhere, the two antipodal hops at a vertex commute, and the Levin-Wen T-junction sign of
the legs (+x, -x, +z) is +1: the charge is not a fermion.

Checks:
 (1) GF(2): Z-decorations on the 6 links at a vertex, with Gauss-parity switching freedom,
     covariant under the 24 proper turns (or subgroups), solved for the fermionic condition.
 (2) symplectic random test of the Pauli lemma on a 5x5x5 window; controls.
 (3) dense 10-qubit T-junction check with explicit C2z-covariant hops; non-covariant control.
"""
import itertools, signal, sys
import numpy as np

signal.alarm(55)
rng = np.random.default_rng(20261003)

# ---------- proper cubic rotations ----------
def proper_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for i, p in enumerate(perm):
                M[p, i] = signs[i]
            if round(np.linalg.det(M)) == 1:
                out.append(M)
    return out

ROT = proper_rotations()
assert len(ROT) == 24
DIRS = [np.array(v) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
NAMES = ['+x','-x','+y','-y','+z','-z']
def dir_index(v):
    for i, d in enumerate(DIRS):
        if np.array_equal(d, v):
            return i
    raise ValueError
PERM = [[dir_index(R @ d) for d in DIRS] for R in ROT]

def is_c2_about(R, axis):
    a = np.array(axis)
    return np.array_equal(R @ a, a) and np.array_equal(R @ R, np.eye(3, dtype=int)) and not np.array_equal(R, np.eye(3, dtype=int))

# ---------- GF(2) solver on python-int bit rows ----------
def gf2_consistent(rows, nvar):
    """rows: list of (mask, rhs). Returns True if the affine system is consistent."""
    pivots = {}
    for mask, rhs in rows:
        m, r = mask, rhs
        while m:
            p = m.bit_length() - 1
            if p in pivots:
                pm, pr = pivots[p]
                m ^= pm; r ^= pr
            else:
                pivots[p] = (m, r)
                break
        if m == 0 and r == 1:
            return False
    return True

def system(group_idx, statistics, vpauli=None, allow_switch=True):
    """Unknowns: d(i,j) i!=j (30), y_i (6), c_g(i) (6 per group element)."""
    pairs = [(i, j) for i in range(6) for j in range(6) if i != j]
    dvar = {p: k for k, p in enumerate(pairs)}
    yvar = {i: 30 + i for i in range(6)}
    cvar = {}
    nxt = 36
    for gi in group_idx:
        for i in range(6):
            cvar[(gi, i)] = nxt; nxt += 1
    rows = []
    for gi in group_idx:
        P = PERM[gi]
        for (i, j) in pairs:
            m = (1 << dvar[(P[i], P[j])]) ^ (1 << dvar[(i, j)])
            if allow_switch:
                m ^= (1 << cvar[(gi, i)])
            rows.append((m, 0))
    target = 1 if statistics == 'fermion' else 0
    for i in range(6):
        for j in range(i + 1, 6):
            m = (1 << dvar[(i, j)]) ^ (1 << dvar[(j, i)]) ^ (1 << yvar[i]) ^ (1 << yvar[j])
            e = 0
            if vpauli is not None:
                a, b = vpauli[i], vpauli[j]
                e = int(a != 0 and b != 0 and a != b)
            rows.append((m, target ^ e))
    return gf2_consistent(rows, nxt)

print("(1) GF(2) census: Z-decorations on the six links at a vertex")
ALL = list(range(24))
c2z = [k for k, R in enumerate(ROT) if is_c2_about(R, (0,0,1))]
c2_axes = [k for k, R in enumerate(ROT) if any(is_c2_about(R, ax) for ax in [(1,0,0),(0,1,0),(0,0,1)])]
c3 = [k for k, R in enumerate(ROT) if np.array_equal(R @ np.array([1,1,1]), np.array([1,1,1]))]
ident = [k for k, R in enumerate(ROT) if np.array_equal(R, np.eye(3, dtype=int))]
print("   group sizes: O=24, C2z-subgroup=%d, three axis C2s=%d, C3(111) subgroup=%d" % (len(c2z) + 1, len(c2_axes), len(c3)))
for label, grp in [("O, fermion, switching allowed", ALL), ("O, fermion, no switching", ALL),
                   ("O, boson", ALL), ("{1,C2z}, fermion, switching", ident + c2z),
                   ("C3(111) only, fermion, switching", c3), ("no covariance, fermion", [])]:
    stat = 'boson' if 'boson' in label else 'fermion'
    sw = 'no switching' not in label
    print("   %-36s consistent = %s" % (label, system(grp, stat, allow_switch=sw)))

# covariant V-qubit Pauli factors: p(g i) = axis-permutation of p(i)
def axis_perm(R):
    return [int(np.nonzero(R[:, a])[0][0]) for a in range(3)]
cov_p = []
for p in itertools.product(range(4), repeat=6):
    ok = True
    for gi, R in enumerate(ROT):
        ap = axis_perm(R)
        for i in range(6):
            img = 0 if p[i] == 0 else ap[p[i] - 1] + 1
            if p[PERM[gi][i]] != img:
                ok = False; break
        if not ok:
            break
    if ok:
        cov_p.append(p)
print("   covariant V-qubit Pauli assignments:", ["".join("IXYZ"[k] for k in p) for p in cov_p])
for p in cov_p:
    print("   with V factors %s: fermion consistent = %s" % ("".join("IXYZ"[k] for k in p), system(ALL, 'fermion', vpauli=p)))

# ---------- (2) Pauli lemma, symplectic ----------
print("(2) Pauli lemma on a 5x5x5 window (random monomials)")
L = 5; off = 2
sites = [(x, y, z) for x in range(-off, off + 1) for y in range(-off, off + 1) for z in range(-off, off + 1)]
sidx = {s: k for k, s in enumerate(sites)}
n = len(sites)
def type_map(R, extra=None):
    """soldered action on Pauli types 1=X,2=Y,3=Z (unsigned); extra: dict site->type permutation applied after"""
    ap = axis_perm(R)
    return ap
def apply_g(A, R, local_twist_on_fixed=False):
    """A: array n of types 0..3. returns image monomial (types only)."""
    ap = axis_perm(R)
    B = np.zeros(n, dtype=int)
    for k, s in enumerate(sites):
        t = A[k]
        img_site = tuple(int(v) for v in (R @ np.array(s)))
        nt = 0 if t == 0 else ap[t - 1] + 1
        if local_twist_on_fixed and img_site == s and nt in (1, 2):
            nt = 3 - nt  # an extra quarter phase about z on fixed qubits: X<->Y
        B[sidx[img_site]] = nt
    return B
def anticommute(A, B):
    c = 0
    for a, b in zip(A, B):
        if a and b and a != b:
            c ^= 1
    return c
R_c2z = ROT[c2z[0]]
R_c2d = [R for R in ROT if is_c2_about(R, (1,1,0))][0]
for label, R, tw in [("C2 about z (soldered)", R_c2z, False), ("C2 about x+y (soldered)", R_c2d, False),
                     ("C2 about z + quarter phase on fixed qubits", R_c2z, True)]:
    cnt = 0; trials = 3000
    for _ in range(trials):
        A = rng.integers(0, 4, size=n)
        cnt += anticommute(A, apply_g(A, R, tw))
    print("   %-44s anticommuting pairs (A, gA): %d / %d" % (label, cnt, trials))

# ---------- (3) dense T-junction check on 10 qubits ----------
print("(3) dense Levin-Wen T-junction check, 10 qubits")
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
PAUL = [I2, sx, sy, sz]
# qubits: 0 V(fixed), 1 +x, 2 -x, 3 +y, 4 -y, 5 +z, 6 -z, 7 a, 8 b (swapped by C2z), 9 c (fixed)
NQ = 10
c2z_perm = [0, 2, 1, 4, 3, 5, 6, 8, 7, 9]
link_axis = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2}
link_sign = {1: 1, 2: -1, 3: 1, 4: -1, 5: 1, 6: -1}
def kron_list(ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out
def raise_out(q):
    a = link_axis[q]; b = (a + 1) % 3; c = (a + 2) % 3
    s = link_sign[q]
    return (PAUL[b + 1] + s * 1j * PAUL[c + 1]) / 2  # raises s*sigma^a
U1 = -1j * sz  # soldered half-turn about z on every qubit
def c2z_op(ops):
    new = [None] * NQ
    for q in range(NQ):
        new[c2z_perm[q]] = U1 @ ops[q] @ U1.conj().T
    return new
def random_decoration(hop_q, fixed_only_symmetric=False):
    ops = []
    for q in range(NQ):
        if q == hop_q:
            ops.append(raise_out(q))
        elif q in link_axis:
            ops.append(I2 if rng.random() < 0.5 else PAUL[link_axis[q] + 1])  # E-diagonal on other links
        else:
            ops.append(PAUL[rng.integers(0, 4)])
    return ops
def symmetrize_for_c2z(ops, hop_q):
    # make the decoration C2z-invariant up to phase: copy each swapped pair's first member
    ops = list(ops)
    for q in range(NQ):
        p = c2z_perm[q]
        if p > q and q != hop_q and p != hop_q:
            img = U1 @ ops[q] @ U1.conj().T
            ops[p] = img
    return ops
def tjunction_phase(t1, t2, t3):
    X1 = t1 @ t2.conj().T @ t3
    X2 = t3 @ t2.conj().T @ t1
    nrm = np.vdot(X2, X2).real
    if nrm < 1e-12:
        return None, None
    c = np.vdot(X2, X1) / nrm
    res = np.linalg.norm(X1 - c * X2) / np.sqrt(nrm)
    return c, res
phases_cov = []; worst = 0.0; comm_anti = 0
for trial in range(60):
    o1 = random_decoration(1)
    t1 = kron_list(o1)
    t2 = kron_list(c2z_op(o1))            # exactly the C2z image: the -x hop
    o3 = symmetrize_for_c2z(random_decoration(5), 5)
    t3 = kron_list(o3)
    assert np.allclose(kron_list(c2z_op(o3)) / np.vdot(t3, t3).real ** 0 , kron_list(c2z_op(o3)))
    # check o3 is C2z-invariant up to a phase
    g3 = kron_list(c2z_op(o3)); ph = np.vdot(t3, g3) / np.vdot(t3, t3)
    assert np.linalg.norm(g3 - ph * t3) < 1e-9
    c, res = tjunction_phase(t1, t2, t3)
    phases_cov.append(np.round(c, 9)); worst = max(worst, res)
    comm_anti += int(np.linalg.norm(t1 @ t2 + t2 @ t1) < 1e-9 and np.linalg.norm(t1 @ t2) > 1e-9)
print("   covariant hops (t_-x = C2z t_+x, t_+z C2z-invariant): T-junction phases seen:", sorted(set(complex(p) for p in phases_cov), key=lambda z: (z.real, z.imag)),
      " max residual %.1e, antipodal pairs anticommuting: %d/60" % (worst, comm_anti))
# non-covariant control: Bravyi-Kitaev order -x<-y<-z<+x<+y<+z, Z decorations on earlier links at V
order = {2: 0, 4: 1, 6: 2, 1: 3, 3: 4, 5: 5}
def bk_hop(q):
    ops = [I2] * NQ
    ops = list(ops)
    ops[q] = raise_out(q)
    for r in link_axis:
        if r != q and order[r] < order[q]:
            ops[r] = PAUL[link_axis[r] + 1]
    return kron_list(ops)
c, res = tjunction_phase(bk_hop(1), bk_hop(2), bk_hop(5))
c2, res2 = tjunction_phase(bk_hop(1), bk_hop(3), bk_hop(5))
print("   Bravyi-Kitaev-ordered hops (not covariant): T-junction (+x,-x,+z) phase %s, (+x,+y,+z) phase %s, residuals %.1e %.1e" % (np.round(c, 9), np.round(c2, 9), res, res2))
# is the BK hop set C2z-covariant? compare C2z image of the +x hop with the -x hop
o_bk = [I2] * NQ; o_bk = list(o_bk); o_bk[1] = raise_out(1)
for r in link_axis:
    if r != 1 and order[r] < order[1]:
        o_bk[r] = PAUL[link_axis[r] + 1]
img = kron_list(c2z_op(o_bk)); tgt = bk_hop(2)
ph = np.vdot(tgt, img) / np.vdot(tgt, tgt)
print("   BK: is C2z(t_+x) a phase times t_-x?  residual = %.3f (0 would mean covariant)" % (np.linalg.norm(img - ph * tgt) / np.linalg.norm(tgt)))
print("done")
