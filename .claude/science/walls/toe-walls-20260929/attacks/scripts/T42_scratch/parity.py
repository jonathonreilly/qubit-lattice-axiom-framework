"""T42 test E: operator parity by orbit sums (abelian link variables) and SU(2) tripod.
Pre-registration: PREREG.md test E.  Exact integer arithmetic."""
import itertools
from itertools import product, permutations
from collections import defaultdict
import numpy as np

n = 3
def unit(mu, s=1):
    v = [0] * n; v[mu] = s; return tuple(v)
def add(p, q): return tuple(a + b for a, b in zip(p, q))
def sub(p, q): return tuple(a - b for a, b in zip(p, q))

def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s

GROUP = []
for perm in permutations(range(n)):
    for signs in product([1, -1], repeat=n):
        det = perm_sign(perm) * int(np.prod(signs))
        GROUP.append((perm, signs, det))
PROPER = [g for g in GROUP if g[2] == 1]
IMPROPER = [g for g in GROUP if g[2] == -1]
assert len(PROPER) == 24 and len(IMPROPER) == 24

def gpoint(g, x):
    perm, signs, _ = g
    y = [0] * n
    for mu in range(n): y[perm[mu]] = signs[mu] * x[mu]
    return tuple(y)

# atoms: ('E', base, mu)  field E on link;  ('S', base, (mu,nu)) sin(plaquette angle);  ('C', ...) cos
def gatom(g, atom):
    perm, signs, _ = g
    kind = atom[0]
    if kind == 'E':
        _, base, mu = atom
        gb = gpoint(g, base); d = perm[mu]
        if signs[mu] == 1: return ('E', gb, d), 1
        return ('E', sub(gb, unit(d)), d), -1          # reversed link: E -> -E
    _, base, (mu, nu) = atom
    gb = gpoint(g, base)
    a = [0] * n; a[perm[mu]] = signs[mu]
    b = [0] * n; b[perm[nu]] = signs[nu]
    corners = [gb, add(gb, tuple(a)), add(add(gb, tuple(a)), tuple(b)), add(gb, tuple(b))]
    al, be = sorted((perm[mu], perm[nu]))
    orient = a[al] * b[be] - b[al] * a[be]
    newbase = tuple(min(c[i] for c in corners) for i in range(n))
    sgn = orient if kind == 'S' else 1
    return (kind, newbase, (al, be)), sgn

def atom_base(atom): return atom[1]

def canon(mono, coeff):
    mn = tuple(min(atom_base(a)[i] for a in mono) for i in range(n))
    shifted = []
    for a in mono:
        b = sub(atom_base(a), mn)
        shifted.append((a[0], b, a[2]))
    return tuple(sorted(shifted)), coeff

def orbit_sum(mono, coset):
    out = defaultdict(int)
    for g in coset:
        c = 1; im = []
        for a in mono:
            a2, s = gatom(g, a); c *= s; im.append(a2)
        m2, c2 = canon(tuple(im), c)
        out[m2] += c2
    return {k: v for k, v in out.items() if v != 0}

def diff(A, B):
    out = defaultdict(int)
    for k, v in A.items(): out[k] += v
    for k, v in B.items(): out[k] -= v
    return {k: v for k, v in out.items() if v != 0}

def analyse(mono):
    mono = canon(tuple(mono), 1)[0]
    OS = orbit_sum(mono, PROPER)
    OSi = orbit_sum(mono, IMPROPER)
    D = diff(OS, OSi)
    return OS, OSi, D

def label(mono):
    return ' * '.join(f"{a[0]}{a[1]}{a[2]}" for a in mono)

def report(name, mono):
    OS, OSi, D = analyse(mono)
    print(f"{name:52s} |OS_O|={len(OS):3d}  |OS_improper|={len(OSi):3d}  P-odd part nonzero: {bool(D)}")
    return OS, OSi, D

o = (0, 0, 0)
P01 = ('S', o, (0, 1)); C01 = ('C', o, (0, 1))
print("=== E(i): single plaquette slots ===")
report("sin(P_xy)  [the reviewed Im Tr U_P slot]", [P01])
report("cos(P_xy)  [Re Tr U_P]", [C01])

print("\n=== E(ii): every monomial supported on one plaquette (E degree<=2 on its 4 links) ===")
plinks = [('E', o, 0), ('E', (0, 1, 0), 0), ('E', o, 1), ('E', (1, 0, 0), 1)]
nmono = 0; nodd = 0; nzero = 0
for deg in range(0, 3):
    for Es in itertools.combinations_with_replacement(plinks, deg):
        for extra in ([], [P01], [C01]):
            mono = list(Es) + extra
            if not mono: continue
            OS, OSi, D = analyse(mono)
            nmono += 1; nodd += bool(D); nzero += (len(OS) == 0)
print(f"monomials tested: {nmono}; with nonzero P-odd part: {nodd}; with vanishing proper orbit sum: {nzero}")

print("\n=== E(iii): positive controls (license-external pseudoscalar carriers) ===")
report("E_z sin(P_xy)   [Hamiltonian E.B]", [('E', o, 2), P01])
report("E_x(0) E_z(y)   [E.curl E, displaced along y]", [('E', o, 0), ('E', (0, 1, 0), 2)])
report("E_x(0) E_z(x)   [control: displaced along x]", [('E', o, 0), ('E', (1, 0, 0), 2)])
report("E_x(0) E_x(y)   [control: parallel]", [('E', o, 0), ('E', (0, 1, 0), 0)])

print("\n=== E(iv): six-arm abelian star, lowest degree with a P-odd covariant polynomial ===")
arms6 = [('E', o, 0), ('E', o, 1), ('E', o, 2), ('E', (-1, 0, 0), 0), ('E', (0, -1, 0), 1), ('E', (0, 0, -1), 2)]
arms3 = arms6[:3]
def min_chiral_degree(arms, maxdeg):
    res = {}
    for deg in range(1, maxdeg + 1):
        cnt = 0
        seen = set()
        for mono in itertools.combinations_with_replacement(arms, deg):
            OS, OSi, D = analyse(mono)
            if D:
                key = tuple(sorted(D.items()))
                seen.add(key)
        res[deg] = len(seen)
    return res
r6 = min_chiral_degree(arms6, 6)
print("six-arm star: number of distinct nonzero P-odd orbit-sum polynomials by degree:", r6)
r3 = min_chiral_degree(arms3, 6)
print("three-arm tripod (+x,+y,+z): by degree:", r3)

print("\n=== E(v): SU(2) tripod triple product ===")
Jx = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])
Jy = np.array([[0, 0, 1j], [0, 0, 0], [-1j, 0, 0]])
Jz = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])
J = [Jx, Jy, Jz]
I3 = np.eye(3)
def on(k, M):
    ops = [I3, I3, I3]; ops[k] = M
    return np.kron(np.kron(ops[0], ops[1]), ops[2])
eps = np.zeros((3, 3, 3))
for a, b, c in permutations(range(3)):
    eps[a, b, c] = perm_sign((a, b, c))
T = sum(eps[a, b, c] * on(0, J[a]) @ on(1, J[b]) @ on(2, J[c])
        for a in range(3) for b in range(3) for c in range(3))
# swap of link 1 and link 2 (a mirror of the tripod), and cyclic shift (a proper rotation)
def perm_op(p):
    U = np.zeros((27, 27))
    for idx in product(range(3), repeat=3):
        src = idx[0] * 9 + idx[1] * 3 + idx[2]
        new = [idx[p[k]] for k in range(3)]
        U[new[0] * 9 + new[1] * 3 + new[2], src] = 1
    return U
S12 = perm_op((1, 0, 2)); S123 = perm_op((1, 2, 0))
print("||T||_F =", round(float(np.linalg.norm(T)), 6), " Hermitian:", np.allclose(T, T.conj().T))
print("cyclic shift (proper rotation) invariant:", np.allclose(S123 @ T @ S123.T, T))
print("arm swap (mirror) gives -T:", np.allclose(S12 @ T @ S12.T, -T))
w = np.linalg.eigvalsh(T)
print("spectrum of T (distinct values):", sorted(set(np.round(w, 6))))
