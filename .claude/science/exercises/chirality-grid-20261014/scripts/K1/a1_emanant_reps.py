"""K1 test A1/A3/A4 (see ../PREREG.md).  Exact arithmetic where possible (signed permutations, integers).

A1: emanant action of the lattice symmetry group (3 unit translations, 24 proper cubic rotations about a site
    with SU(2) spin lift) on the 8 corner Weyl doublets of the walker H = sum_a sigma_a sin p_a.
    Internal part of a rotation R on corner fields: Gamma_{mn}(R) = V_m U_R V_n^dag U_R^dag (m = R n mod 2),
    where V_n puts corner n's Weyl field in the canonical frame H_n = chi_n sigma.q.  Must be +-1 (scalar).
A3: Z16 index nu_u for every u = g z^j (g in the emanant internal group, z = centre of Spin(10), i on 16;
    for G_SM: z = i^X, also i on every 15/16 component since X = 1 mod 4) with u^2 = (-1)^F on fermions;
    sets: light hw1, mirror hw0+hw2+hw3, every single corner, whole; multiplicity d = 1, 15, 16.
A3': mixed T_x x Spin(10) class on S^1(A, T_x-twisted) x CP^2 with Spin x_{Z2} Spin(10) bundles reducible to the
    maximal torus: anomaly = (-1)^{sum over corners with n_x = 1 of ind(CP^2; 16)}; ind computed exactly from
    spin^c indices (c_w^2 - 1)/8 over the 16 weights.  Control: a single weight (one Weyl, charge 1).
A4: control: 15 without nu^c reproduces F6-tC (walker mirror 3 mod 16) and C1 per-component values.
"""
import itertools, numpy as np
from fractions import Fraction as Fr

out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
SIG = [sx, sy, sz]

# ---- 24 proper cubic rotations (signed permutation matrices, det +1) with SU(2) lifts ----
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3): R[i, perm[i]] = signs[i]
        if round(np.linalg.det(R)) == 1: rots.append(R)
assert len(rots) == 24

def su2_lift(R):
    """U with U sigma_a U^dag = sum_b R_{ba} sigma_b (one of the two lifts)."""
    Rf = R.astype(float)
    ang = np.arccos(np.clip((np.trace(Rf) - 1) / 2, -1, 1))
    if abs(ang) < 1e-12: return s0.copy()
    if abs(ang - np.pi) < 1e-9:
        M = (Rf + np.eye(3)) / 2; i = np.argmax(np.diag(M)); n = M[:, i] / np.sqrt(M[i, i])
    else:
        n = np.array([Rf[2, 1] - Rf[1, 2], Rf[0, 2] - Rf[2, 0], Rf[1, 0] - Rf[0, 1]]) / (2 * np.sin(ang))
    U = np.cos(ang / 2) * s0 - 1j * np.sin(ang / 2) * sum(n[k] * SIG[k] for k in range(3))
    for a in range(3):
        lhs = U @ SIG[a] @ U.conj().T; rhs = sum(Rf[b, a] * SIG[b] for b in range(3))
        if not np.allclose(lhs, rhs):
            U = np.cos(ang / 2) * s0 + 1j * np.sin(ang / 2) * sum(n[k] * SIG[k] for k in range(3)); break
    for a in range(3):
        assert np.allclose(U @ SIG[a] @ U.conj().T, sum(Rf[b, a] * SIG[b] for b in range(3)))
    return U

corners = list(itertools.product((0, 1), repeat=3)); cidx = {c: i for i, c in enumerate(corners)}
hw = {c: sum(c) for c in corners}; chi = {c: (-1) ** hw[c] for c in corners}   # +1 = R (H = +sigma.q)
# canonical frame V_n:  V^dag sigma_b V = sum_a O_ab sigma_a with O = chi * diag((-1)^n)
Vfr = {}
for c in corners:
    O = chi[c] * np.diag([(-1) ** x for x in c])
    cand = {(1, 1, 1): s0, (1, -1, -1): 1j * sx, (-1, 1, -1): 1j * sy, (-1, -1, 1): 1j * sz}
    V = cand[tuple(int(x) for x in np.diag(O))]
    for b in range(3):
        assert np.allclose(V.conj().T @ SIG[b] @ V, sum(O[a, b] * SIG[a] for a in range(3)))
    Vfr[c] = V
# check: walker near corner c in canonical frame is chi_c sigma.q
for c in corners:
    D = np.diag([(-1) ** x for x in c])
    q = np.array([0.3, -0.7, 0.2]); Hq = sum(SIG[a] * D[a, a] * q[a] for a in range(3))
    assert np.allclose(Vfr[c] @ Hq @ Vfr[c].conj().T, chi[c] * sum(SIG[a] * q[a] for a in range(3)))
P("walker corner frames verified: H_c = chi_c sigma.q in canonical frame for all 8 corners")

# ---- A1: emanant internal matrices ----
def rot_internal(R):
    U = su2_lift(R); G = np.zeros((8, 8), int)
    for c in corners:
        m = tuple(int(x) % 2 for x in (R @ np.array(c)))
        assert hw[m] == hw[c]
        X = Vfr[m] @ U @ Vfr[c].conj().T @ U.conj().T
        assert np.allclose(X, X[0, 0] * s0), ("non-scalar internal action", R, c)
        ph = X[0, 0]; assert np.isclose(abs(ph), 1) and np.isclose(ph.imag, 0), ph
        G[cidx[m], cidx[c]] = int(round(ph.real))
    # also the other lift -U gives the same internal matrix (2pi rotation is Lorentz (-1)^F)
    return G
def trans(v):
    return np.diag([(-1) ** (np.dot(v, c) % 2) for c in corners]).astype(int)

gens = [rot_internal(R) for R in rots] + [trans(v) for v in corners]
# close the group
grp = {}
frontier = [np.eye(8, dtype=int)]
key = lambda M: M.tobytes()
grp[key(frontier[0])] = frontier[0]
while frontier:
    nf = []
    for A in frontier:
        for g in gens:
            B = g @ A
            if key(B) not in grp: grp[key(B)] = B; nf.append(B)
    frontier = nf
G = list(grp.values())
P(f"A1: all 24 rotation internal parts are scalar (+-1) on each corner Weyl doublet: True (asserted)")
P(f"A1: emanant internal group (rotations x corner translations) acting on 8 corners: order {len(G)}; "
  f"all elements signed permutation matrices: {all((np.abs(M).sum(0) == 1).all() and set(np.unique(M)) <= {-1,0,1} for M in G)}")
# stabiliser characters per corner
allvals = set()
for c in corners:
    i = cidx[c]; vals = set()
    for M in G:
        if M[i, i] != 0: vals.add(int(M[i, i]))
    allvals |= vals
    P(f"  corner {c} (hw{hw[c]}, {'R' if chi[c] == 1 else 'L'}): stabiliser character values {sorted(vals)}")
P(f"A1 verdict: stabiliser characters take values in {sorted(allvals)} subset of {{+-1, +-i}}: "
  f"{allvals <= {1, -1}}  -> absorption lemma hypothesis {'HOLDS' if allvals <= {1, -1} else 'FAILS'}")
orbits = {}
for c in corners:
    orb = tuple(sorted({corners[int(np.nonzero(M[:, cidx[c]])[0][0])] for M in G}))
    orbits[orb] = True
P("A1: corner orbits under the emanant group:", list(orbits.keys()))

# ---- A3/A4: Z16 indices for u = g z^j with u^2 = (-1)^F ----
sets = {"light hw1": [c for c in corners if hw[c] == 1],
        "mirror hw0+hw2+hw3": [c for c in corners if hw[c] != 1],
        "whole": corners}
for c in corners: sets[f"single {c}"] = [c]

def nu_u(M, j, cset):
    """per internal component: u = M (x) i^j on corners in cset (must be M-invariant).  Returns nu (int) or None."""
    idx = [cidx[c] for c in cset]
    Ms = M[np.ix_(idx, idx)]
    if not (np.abs(Ms).sum(0) == 1).all(): return None          # cset not invariant
    nu = 0
    for hand in (+1, -1):
        sub = [k for k, c in enumerate(cset) if chi[c] == hand]
        if not sub: continue
        lam = np.linalg.eigvals(Ms[np.ix_(sub, sub)].astype(float)) * (1j ** j)
        for l in lam:
            l = complex(l)
            if hand == +1: l = l.conjugate()                    # R Weyl -> LH conjugate
            if np.isclose(l, 1j): nu += 1
            elif np.isclose(l, -1j): nu -= 1
            else: return "not Spin-Z4"
    return nu

checked = 0; bad16 = []; per_comp = {}
for M in G:
    for j in range(4):
        # u^2 on fermions = M^2 * i^{2j} ; need = -1 (i.e. (-1)^F) on every corner
        if not np.array_equal(M @ M * ((-1) ** j), -np.eye(8, dtype=int)): continue
        for name, cs in sets.items():
            v = nu_u(M, j, cs)
            if v is None or isinstance(v, str): continue
            checked += 1
            per_comp.setdefault(name, set()).add(v)
            if (16 * v) % 16: bad16.append((name, v))
P(f"\nA3: Spin-Z4 elements u = g z^j checked (element x invariant set pairs): {checked}")
for name in ["light hw1", "mirror hw0+hw2+hw3", "whole"] + [f"single {c}" for c in corners]:
    vals = sorted(per_comp.get(name, []))
    P(f"  {name:22s}: per-component nu values {vals};  d=16 -> all 0 mod 16: {all((16*v) % 16 == 0 for v in vals)};"
      f"  d=1 obstructed: {any(v % 16 for v in vals)};  d=15 obstructed: {any((15*v) % 16 for v in vals)}")
P(f"A3 verdict (d = 16): nonzero classes found: {bad16 if bad16 else 'none'}")

# A4 control: identity element with j = 1 (pure Z4^X = i^X on every component), 15 components (no nu^c)
v_mir = nu_u(np.eye(8, dtype=int), 1, sets["mirror hw0+hw2+hw3"])
P(f"A4 control: mirror, u = Z4^X only, per component nu = {v_mir}; x15 mod 16 = {(15*v_mir) % 16} "
  f"(F6-tC reported 3)  -> control {'PASS' if (15*v_mir) % 16 == 3 else 'FAIL'}")
# C1 cross-check: per-component nu for translations T^v * i^F on mirror (C1 reported (-3,-1,-1,1,-1,1,1,-5))
c1 = [nu_u(trans(np.array(v)), 1, sets["mirror hw0+hw2+hw3"]) for v in corners]
P(f"A4 control: C1 mirror per-component nu over T^v i^F, v in {{0,1}}^3 = {c1} (C1: [-3,-1,-1,1,-1,1,1,-5]) -> "
  f"{'PASS' if c1 == [-3,-1,-1,1,-1,1,1,-5] else 'MISMATCH (sign convention?)'}")

# ---- A3': mixed T_x x Spin(10) class on S^1(A, T_x) x CP^2, torus-reducible Spin x_{Z2} Spin(10) bundles ----
# weights of 16: (+-1/2)^5 with even number of minus signs.  Torus bundle on CP^2: integers c_1..c_5 (in units of H),
# fermion line of weight w has c1 = sum_i w_i c_i ; Spin x_{Z2} structure requires sum_i w_i c_i in 1/2 + Z, i.e.
# c_w := 2 sum w_i c_i odd (it is then the spin^c class), index = (c_w^2 - 1)/8 (CP^2, sigma = 1).
W16 = [w for w in itertools.product((Fr(1, 2), Fr(-1, 2)), repeat=5) if sum(1 for x in w if x < 0) % 2 == 0]
assert len(W16) == 16
odd_found = 0; ntest = 0; minmax = []
for cvec in itertools.product(range(-3, 4), repeat=5):
    cws = [int(2 * sum(w[i] * cvec[i] for i in range(5))) for w in W16]
    if any(cw % 2 == 0 for cw in cws): continue            # not a Spin x_Z2 Spin(10) structure (needs all odd)
    ntest += 1
    ind16 = sum((cw * cw - 1) // 8 for cw in cws)
    assert all((cw * cw - 1) % 8 == 0 for cw in cws)
    if ind16 % 2: odd_found += 1
P(f"\nA3': CP^2 torus-reducible Spin x_Z2 Spin(10) bundles tested: {ntest}; bundles with odd ind(16): {odd_found}")
P("     -> mixed class S^1(A,T_x) x CP^2 = (-1)^{(#corners with n_x=1) * ind(16)}: "
  f"{'trivial for every corner set' if odd_found == 0 else 'NONTRIVIAL for odd corner counts'}")
# control: single Weyl of charge 1 under U(1) in spin^c (c odd): ind = (c^2-1)/8 odd for c = 3
P(f"     control (one spin^c Weyl, c = 3): ind = {(9-1)//8} (odd) -> the same class detects a single charged Weyl")
lt = [c for c in corners if hw[c] == 1]; mr = [c for c in corners if hw[c] != 1]
for a in range(3):
    P(f"     axis {a}: corners with n_a = 1: light {sum(c[a] for c in lt)}, mirror {sum(c[a] for c in mr)} "
      f"(odd count would expose a d=1-type single-weight anomaly)")

open(__file__.replace('.py', '.out'), 'w').write("\n".join(out) + "\n")
