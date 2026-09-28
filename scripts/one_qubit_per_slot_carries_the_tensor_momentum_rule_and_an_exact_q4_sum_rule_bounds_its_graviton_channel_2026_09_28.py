#!/usr/bin/env python3
"""One qubit per slot carries the tensor momentum rule, and its graviton channel obeys an exact q^4 sum rule.

Question (the owner, 2026-09-28): can gravity be a pattern of qubit records under
a neighbourhood rule (the tensor version of the photon test)? The tensor setting
is LANDED on main and is not rebuilt here: the vector (momentum) stencil G, the
canonical slots and the regular compact-character bound are in
docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md;
the linear comparator's exact symbol in
docs/TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_BOTH_CANONICAL_VARIABLES_MUST_BE_NON_COMPACT_BOUNDED_THEOREM_NOTE_2026-09-24.md;
the ten-slot planar kernel moves (coefficients up to 2) in
docs/DYNAMICS_CLAUSE_THE_LANDED_TENSOR_CONSTRAINTS_FREEZE_UNDER_TWO_SITE_GENERATORS_AND_NO_SINGLE_NEIGHBOURHOOD_MOVES_THEM_BOUNDED_THEOREM_NOTE_2026-09-24.md;
the spectral-moment chain in
docs/RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md.
The landed bound needs lifted clock characters and a smooth small-field
expansion, so it does not cover one qubit per slot. This runner does.

Stencil (landed, coarse cell x, doubled positions: diagonal slot jj at 2x,
face slot ij at 2x+e_i+e_j, row j at 2x+e_j):
  (G p)_j(x) = p_jj(x+e_j) - p_jj(x) + sum_{i != j} [p_ij(x) - p_ij(x-e_i)].
A qubit (spin-1/2) slot has electric value +-1/2; a move changes each touched
slot by exactly +-1, so a qubit-carriable move is an integer vector m with
G m = 0 and entries in {-1,0,1}.

Not pre-registered: the move searches were exploratory; the checks below were
frozen after them and before the note.

Checks:
  A  stencil consistency: the landed ten-slot planar move is in ker G; the
     bounded MILP with coefficient bound 2 reproduces support 10.
  B  qubit moves exist: coefficient bound 1 has no move in the radius-1 box
     (diagonal anchor) and minimum support 20 in the radius-2 box (both
     anchors); two explicit 20-slot witnesses (a 3D move and the 2x2 planar
     block) are verified row by row.
  C  moment lemma (landed 2026-09-14, re-verified): G^T of polynomials of degree <= 2 realises every constant
     and linear symmetric strain; hence every finitely supported m in ker G has
     vanishing zeroth and first moments (checked on witnesses and random
     integer combinations).
  D  exact double commutator (the landed ring-note identity, here for tensor
     change patterns): for a diagonal electric mode O and any shift
     operator T_m, [O^dag,[T_m,O]] = -|w(m)|^2 T_m; for eigenstates,
     m1(O) <= <[O^dag,[H,O]]> <= sum |c| |w(m)|^2 (dense check, 10 qubits).
  E  the q^4 law: the qubit family (both witnesses, all 24 proper rotations,
     all translations) stiffens all three physical modes in every direction,
     each proportional to q^4; |m_hat(q)| <= mu_2 |q|^2 / 2 on a grid.
  F  comparators: the landed linear comparator has m1 = g t (t = sum 4
     sin^2(k/2)), i.e. order q^2; the qubit sum rule is order q^4, so their
     ratio falls like q^2. U(1) ring moves (first moment nonzero) give q^2.
  G  moment-chain consequence (Gaussian illustrations): finite electric
     susceptibility gives omega ~ q^2; a light-cone lowest mode needs chi ~ q^2
     (then S ~ q^3 follows); in the Gaussian ansatz that is an electric energy
     growing like 1/q^2.
Prints one line per check, the N5 resolution lines and TOTAL: PASS=N FAIL=M.
"""
import itertools
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix, vstack, csr_matrix, hstack, identity

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


E3 = np.eye(3, dtype=int)
FACES = [(0, 1), (1, 2), (0, 2)]
COMP = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (0, 1): 3, (1, 2): 4, (0, 2): 5}


def row_terms(x, j):
    x = np.array(x); t = [(('d', tuple(x + E3[j]), j), +1), (('d', tuple(x), j), -1)]
    for i in range(3):
        if i == j:
            continue
        f = tuple(sorted((i, j)))
        t += [(('f', tuple(x), f), +1), (('f', tuple(x - E3[i]), f), -1)]
    return t


def in_kernel(move):
    d = dict(move)
    for s, _ in move:
        for dx in itertools.product(range(-2, 3), repeat=3):
            for j in range(3):
                y = tuple(np.array(s[1]) + np.array(dx))
                if sum(c * d.get(k, 0) for k, c in row_terms(y, j)) != 0:
                    return False
    return True


def build(R):
    S = []
    for x in itertools.product(range(-R, R + 1), repeat=3):
        for j in range(3):
            S.append(('d', x, j))
        for f in FACES:
            S.append(('f', x, f))
    idx = {s: k for k, s in enumerate(S)}
    rows = set()
    for x in itertools.product(range(-R - 1, R + 2), repeat=3):
        for j in range(3):
            if any(k in idx for k, _ in row_terms(x, j)):
                rows.add((x, j))
    G = lil_matrix((len(rows), len(S)))
    for r, (y, j) in enumerate(sorted(rows)):
        for k, c in row_terms(y, j):
            if k in idx:
                G[r, idx[k]] += c
    return S, idx, G.tocsr()


def min_support(R, M, anchor):
    """Minimum support of an integer m in ker G with |m| <= M, slots in the radius-R box
    (all rows touching the box imposed, so m is a kernel vector of the infinite lattice),
    and the anchor slot fixed to +1."""
    S, idx, G = build(R); n = len(S); m = G.shape[0]
    In = identity(n, format='csr')
    A = vstack([hstack([G, csr_matrix((m, n))]), hstack([In, -M * In]), hstack([-In, -M * In])])
    lb = np.concatenate([np.zeros(m), -np.inf * np.ones(2 * n)]); ub = np.zeros(m + 2 * n)
    lo = np.concatenate([-M * np.ones(n), np.zeros(n)]); hi = np.concatenate([M * np.ones(n), np.ones(n)])
    lo[idx[anchor]] = hi[idx[anchor]] = 1
    sol = milp(np.concatenate([np.zeros(n), np.ones(n)]), constraints=LinearConstraint(A, lb, ub),
               integrality=np.ones(2 * n), bounds=Bounds(lo, hi), options={'time_limit': 300})
    if sol.status != 0:
        return sol.status, None
    v = np.round(sol.x[:n]).astype(int)
    assert np.all(G @ v == 0)
    return 0, [(S[k], int(v[k])) for k in np.nonzero(v)[0]]


def planar(c, a, b):
    """The landed ten-slot planar move in the ab plane around cell c."""
    c = np.array(c); Ea, Eb = E3[a], E3[b]; f = tuple(sorted((a, b)))
    mv = [(('d', tuple(c), a), -2), (('d', tuple(c), b), -2), (('d', tuple(c + Eb), a), 1), (('d', tuple(c - Eb), a), 1),
          (('d', tuple(c + Ea), b), 1), (('d', tuple(c - Ea), b), 1)]
    mv += [(('f', tuple(c + np.array(o)), f), s) for o, s in [((0, 0, 0), -1), (-Ea, 1), (-Eb, 1), (-Ea - Eb, -1)]]
    return mv


def add_moves(*moves):
    d = {}
    for mv in moves:
        for k, v in mv:
            d[k] = d.get(k, 0) + v
    return [(k, v) for k, v in sorted(d.items(), key=str) if v != 0]


# ---------------------------------------------------------------- A: stencil consistency
p10 = planar((0, 0, 0), 0, 1)
stA, mvA = min_support(2, 2, ('d', (0, 0, 0), 0))
check("A: stencil consistency: the landed ten-slot planar move is in ker G and the radius-2, coefficient-bound-2 MILP reproduces minimum support 10",
      in_kernel(p10) and stA == 0 and len(mvA) == 10,
      f"landed planar move in kernel: {in_kernel(p10)}; MILP (radius 2, |m| <= 2, diagonal anchor): support {len(mvA) if mvA else None}, max|m| {max(abs(c) for _, c in mvA)}")

# ---------------------------------------------------------------- B: qubit moves
st1, _ = min_support(1, 1, ('d', (0, 0, 0), 0))
st2d, mv2d = min_support(2, 1, ('d', (0, 0, 0), 0))
st2f, mv2f = min_support(2, 1, ('f', (0, 0, 0), (0, 1)))
MOVE3D = [(('f', (-1, -2, 0), (0, 1)), 1), (('f', (-1, -2, 1), (0, 1)), -1), (('d', (-1, -1, 0), 1), -1), (('f', (-1, -1, 0), (1, 2)), -1),
          (('f', (-1, -1, 0), (0, 2)), 1), (('d', (-1, -1, 1), 1), 1), (('f', (-1, 0, 0), (0, 2)), -1), (('d', (0, -2, 0), 0), -1),
          (('f', (0, -2, 0), (1, 2)), 1), (('f', (0, -2, 0), (0, 2)), -1), (('d', (0, -2, 1), 0), 1), (('f', (0, -1, 0), (0, 1)), -1),
          (('f', (0, -1, 0), (1, 2)), 1), (('f', (0, -1, 0), (0, 2)), 1), (('f', (0, -1, 1), (0, 1)), 1), (('d', (0, 0, 0), 0), 1),
          (('d', (0, 0, 1), 0), -1), (('f', (1, -2, 0), (1, 2)), -1), (('d', (1, -1, 0), 1), 1), (('d', (1, -1, 1), 1), -1)]
BLOCK = add_moves(*[planar(c, 0, 2) for c in [(0, 0, 0), (1, 0, 0), (0, 0, 1), (1, 0, 1)]])
okB = (st1 == 2 and st2d == 0 and st2f == 0 and len(mv2d) == 20 and len(mv2f) == 20
       and all(abs(c) == 1 for _, c in mv2d + mv2f) and in_kernel(MOVE3D) and in_kernel(BLOCK)
       and len(MOVE3D) == 20 and len(BLOCK) == 20 and all(abs(c) == 1 for _, c in MOVE3D + BLOCK))
check("B: one qubit per slot carries the momentum rule: no coefficient-bound-1 move in the radius-1 box; minimum support 20 in the radius-2 box; two explicit 20-slot witnesses verified row by row",
      okB,
      f"radius 1 (diagonal anchor): {'infeasible' if st1 == 2 else st1}; radius 2: support {len(mv2d)} (diagonal anchor), {len(mv2f)} (face anchor), all entries +-1; "
      f"witness 3D move: in kernel {in_kernel(MOVE3D)}, 20 slots; witness 2x2 planar block (four landed planar moves, the +-2 entries cancel): in kernel {in_kernel(BLOCK)}, 20 slots, max|m| {max(abs(c) for _, c in BLOCK)}. "
      f"Box-bounded search only; no box-free minimum is claimed.")


# ---------------------------------------------------------------- tensors, rotations, Fourier
def to_tl(move):
    out = []
    for (t, x, a), c in move:
        x = np.array(x)
        if t == 'd':
            out.append((2 * x, (a, a), c))
        else:
            i, j = a; out.append((2 * x + E3[i] + E3[j], (i, j), c))
    return out


def rotations():
    Rs = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3), int)
            for i in range(3):
                R[i, p[i]] = s[i]
            if round(np.linalg.det(R)) == 1:
                Rs.append(R)
    return Rs


def rotate(tl, R):
    out = {}
    for pos, (i, j), c in tl:
        a = int(np.nonzero(R[:, i])[0][0]); b = int(np.nonzero(R[:, j])[0][0])
        key = (tuple(R @ pos), tuple(sorted((a, b))))
        out[key] = out.get(key, 0) + R[a, i] * R[b, j] * c
    return [(np.array(k[0]), k[1], v) for k, v in out.items() if v != 0]


def fourier(tl, q):
    v = np.zeros(6, complex)
    for pos, ij, c in tl:
        v[COMP[tuple(sorted(ij))]] += c * np.exp(0.5j * q @ pos)
    return v


def moments(tl):
    m0 = np.zeros(6); m1 = np.zeros((6, 3)); mu2 = 0.0
    for pos, ij, c in tl:
        k = COMP[tuple(sorted(ij))]; r = pos / 2
        m0[k] += c; m1[k] += c * r; mu2 += abs(c) * (r @ r)
    return m0, m1, mu2


def Gsym(q):
    G = np.zeros((3, 6), complex)
    for j in range(3):
        r = E3[j]
        G[j, COMP[(j, j)]] += np.exp(0.5j * q @ (2 * E3[j] - r)) - np.exp(0.5j * q @ (-r))
        for i in range(3):
            if i != j:
                f = E3[i] + E3[j]
                G[j, COMP[tuple(sorted((i, j)))]] += np.exp(0.5j * q @ (f - r)) - np.exp(0.5j * q @ (f - 2 * E3[i] - r))
    return G


def phys_basis(q):
    _, s, vh = np.linalg.svd(Gsym(q)); return vh[np.sum(s > 1e-10):].conj().T


# ---------------------------------------------------------------- C: moment lemma
# (i) G^T applied to polynomial gauge vectors xi of degree <= 2 realises every constant and linear symmetric strain.
Rb = 3
S, idx, Gbox = build(Rb)
rows_sorted = sorted({(x, j) for x in itertools.product(range(-Rb - 1, Rb + 2), repeat=3) for j in range(3)
                      if any(k in idx for k, _ in row_terms(x, j))})
rpos = np.array([2 * np.array(x) + E3[j] for x, j in rows_sorted]) / 2     # physical row positions
ridx_j = np.array([j for _, j in rows_sorted])
spos = np.array([(2 * np.array(s[1]) + (0 if s[0] == 'd' else E3[s[2][0]] + E3[s[2][1]])) / 2 for s in S])
scomp = [COMP[(s[2], s[2])] if s[0] == 'd' else COMP[s[2]] for s in S]
interior = np.array([np.all(np.abs(s[1]) <= Rb - 1) for s in S])
monos = [()] + [(a,) for a in range(3)] + [(a, b) for a in range(3) for b in range(a, 3)]
gauge_imgs = []
for j in range(3):
    for mono in monos:
        xi = np.array([(1.0 if ridx_j[r] == j else 0.0) * np.prod([rpos[r][a] for a in mono]) for r in range(len(rows_sorted))])
        gauge_imgs.append((Gbox.T @ xi)[interior])
strains = []
for k in range(6):
    for w in [None, 0, 1, 2]:
        v = np.array([(1.0 if scomp[t] == k else 0.0) * (1.0 if w is None else spos[t][w]) for t in range(len(S))])
        strains.append(v[interior])
Gi = np.array(gauge_imgs).T; St = np.array(strains).T
coef, *_ = np.linalg.lstsq(Gi, St, rcond=None)
resid = np.abs(Gi @ coef - St).max()
rng = np.random.default_rng(20260928)
fam_moves = [MOVE3D, BLOCK, p10, planar((1, -1, 2), 1, 2)]
combos_ok = True
for _ in range(20):
    tl = []
    for mv in fam_moves:
        c = int(rng.integers(-3, 4)); R = rotations()[int(rng.integers(24))]; sh = rng.integers(-3, 4, size=3)
        tl += [(p + 2 * sh, ij, c * v) for p, ij, v in rotate(to_tl(mv), R)]
    m0, m1, _ = moments(tl)
    combos_ok &= (np.abs(m0).max() < 1e-12 and np.abs(m1).max() < 1e-9)
w0 = [moments(to_tl(mv)) for mv in (MOVE3D, BLOCK)]
# route check (soft rule): a single-slot change violates the rule; its |m_hat(q)|^2 stays 1 as q -> 0, so the exact rule is load-bearing
soft = [abs(fourier([(np.array([0, 0, 0]), (0, 0), 1)], qq * np.array([0.3, 0.5, 0.81]) / np.linalg.norm([0.3, 0.5, 0.81]))[0]) ** 2 for qq in (0.1, 0.01)]
single_violates = not in_kernel([(('d', (0, 0, 0), 0), 1)])
check("C: moment lemma: G^T of polynomials of degree <= 2 realises every constant and linear symmetric strain, so every finitely supported kernel move has vanishing zeroth and first moments",
      resid < 1e-9 and combos_ok and all(np.abs(a).max() == 0 and np.abs(b).max() == 0 for a, b, _ in w0) and single_violates and min(soft) > 0.999,
      f"24 strain patterns (6 constant + 18 linear) reproduced by G^T xi on the interior of a radius-{Rb} box, max residual {resid:.1e}; "
      f"witnesses: zeroth/first moments exactly 0, second-moment weights mu_2 = {w0[0][2]:.0f} (3D move), {w0[1][2]:.0f} (block); 20 random integer combinations of rotated/translated moves: moments 0; "
      f"soft-rule route: a single-slot change is not in ker G and keeps |m_hat|^2 = {min(soft):.3f} as q -> 0, so without the exact rule the q^4 law is lost")

# ---------------------------------------------------------------- D: exact double commutator (dense, 10 qubits)
nq = 10
sp = np.array([[0, 1], [0, 0]], complex); sm = sp.T.copy(); sz = np.diag([0.5, -0.5]).astype(complex); I2 = np.eye(2)


def kron_list(ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def shift_op(m):
    return kron_list([sp if a == 1 else sm if a == -1 else I2 for a in m])


Ez = [kron_list([sz if b == a else I2 for b in range(nq)]) for a in range(nq)]
rngD = np.random.default_rng(7)
pats = []
for _ in range(12):                      # two- and three-slot shift patterns, so the ground state is well connected
    m = np.zeros(nq, int); sup = rngD.choice(nq, size=int(rngD.integers(2, 4)), replace=False); m[sup] = rngD.choice([-1, 1], size=len(sup)); pats.append(m)
cs = rngD.normal(size=len(pats))
Ts = [shift_op(m) for m in pats]
Hd = np.diag(rngD.normal(size=2 ** nq))
H = Hd + sum(c * (T + T.conj().T) for c, T in zip(cs, Ts))
w = rngD.normal(size=nq) + 1j * rngD.normal(size=nq)
O = sum(w[a] * Ez[a] for a in range(nq))
DC = O.conj().T @ (H @ O - O @ H) - (H @ O - O @ H) @ O.conj().T
pred = -sum(c * abs(w @ m) ** 2 * (T + T.conj().T) for c, T, m in zip(cs, Ts, pats))
ev, U = np.linalg.eigh(H)
ok_m1 = True; worst = 0.0
for n0 in [0, 3, 17]:
    psi = U[:, n0]; amp = U.conj().T @ (O @ psi)
    m1 = np.sum((ev - ev[n0]) * np.abs(amp) ** 2)
    # the f-sum with the sign convention of an arbitrary eigenstate: m1(O) + m1(O^dag) = <[O^dag,[H,O]]>
    amp2 = U.conj().T @ (O.conj().T @ psi); m1d = np.sum((ev - ev[n0]) * np.abs(amp2) ** 2)
    lhs = np.real(psi.conj() @ DC @ psi)
    ok_m1 &= abs(m1 + m1d - lhs) < 1e-9
    if n0 == 0:
        bound = sum(abs(c) * abs(w @ m) ** 2 for c, m in zip(cs, pats))
        ok_m1 &= (m1 <= lhs + 1e-12 and lhs <= bound + 1e-12); worst = lhs / bound
check("D: exact double commutator for one qubit per slot: [O^dag,[T_m,O]] = -|w.m|^2 T_m for diagonal electric modes; m1(O) + m1(O^dag) = <[O^dag,[H,O]]> in eigenstates; ground state m1(O) <= <[O^dag,[H,O]]> <= sum |c||w.m|^2",
      np.abs(DC - pred).max() < 1e-10 and ok_m1,
      f"dense 2^{nq}-dimensional check, {len(pats)} random two- and three-slot shift patterns plus a random diagonal part: operator identity residual {np.abs(DC - pred).max():.1e}; "
      f"sum-rule identity holds in eigenstates 0, 3, 17; the ground-state double commutator is {worst:.3f} of the norm bound")

# ---------------------------------------------------------------- E: the q^4 law for the qubit family
famQ = [rotate(to_tl(mv), R) for mv in (MOVE3D, BLOCK) for R in rotations()]
mu2max = max(moments(f)[2] for f in famQ)
rows = []; okE = True
for name, qd in [("axis", [0, 0, 1.]), ("face", [1, 1, 0.]), ("body", [1, 1, 1.]), ("generic", [0.3, 0.5, 0.81])]:
    qd = np.array(qd) / np.linalg.norm(qd); vals = []
    for qq in [0.2, 0.1, 0.05, 0.025]:
        q = qq * qd; N = phys_basis(q)
        V = sum(np.outer(fourier(f, q), fourier(f, q).conj()) for f in famQ)
        vals.append(np.linalg.eigvalsh(N.conj().T @ V @ N) / qq ** 4)
    okE &= (vals[-1].min() > 1.0 and np.abs(vals[-1] / vals[-2] - 1).max() < 0.01 and N.shape[1] == 3)
    rows.append(f"{name}: {np.round(vals[-1], 2)}")
# leading q^4 coefficient over a Fibonacci sphere of directions (plus the axes): smallest physical eigenvalue
def lead_min(u, qq=1e-3):
    q = qq * u; N = phys_basis(q)
    V = sum(np.outer(fourier(f, q), fourier(f, q).conj()) for f in famQ)
    return np.linalg.eigvalsh(N.conj().T @ V @ N).min() / qq ** 4
nd = 1500; gold = np.pi * (3 - np.sqrt(5))
dirs = [np.array([np.cos(gold * i) * np.sqrt(1 - (1 - 2 * (i + .5) / nd) ** 2), np.sin(gold * i) * np.sqrt(1 - (1 - 2 * (i + .5) / nd) ** 2), 1 - 2 * (i + .5) / nd]) for i in range(nd)]
dirs += [np.array(v, float) for v in np.eye(3)]
sphere_min = min(lead_min(u) for u in dirs)
okE &= sphere_min > 15.9
grid = [np.array(v) * s for v in itertools.product([-1, 0, 1], repeat=3) if any(v) for s in [0.3, 1.0, 2.0, np.pi]]
taylor_ok = all(np.linalg.norm(fourier(f, q)) <= moments(f)[2] * (q @ q) / 2 + 1e-12 for f in famQ[::6] for q in grid)
qz = 0.05 * np.array([0, 0, 1.]); Nz = phys_basis(qz)
single = [int(np.sum(np.linalg.eigvalsh(Nz.conj().T @ sum(np.outer(fourier(f, qz), fourier(f, qz).conj()) for f in famQ[k * 24:(k + 1) * 24]) @ Nz) > 1e-9)) for k in range(2)]
check("E: the q^4 law: the qubit family (both witnesses, 24 proper rotations, all translations) stiffens all three physical modes in every sampled direction (smallest leading coefficient 16, on the coordinate planes), each eigenvalue / q^4 converging; |m_hat(q)| <= mu_2 |q|^2/2 on a zone grid",
      okE and taylor_ok,
      f"physical-block eigenvalues / q^4 at q = 0.025: {'; '.join(rows)}; smallest leading coefficient over {len(dirs)} directions (Fibonacci sphere plus axes) {sphere_min:.3f}; along an axis the 3D family alone stiffens only the cross shear and the block family only the plus shear and scalar "
      f"(ranks {single[0]}, {single[1]}); Taylor bound holds on {len(grid)} zone points for every sampled image")

# ---------------------------------------------------------------- F: comparators
def Xr(q):
    K = 2 * np.sin(q / 2); X = np.zeros((6, 6))
    dd = [0, 1, 2]; fc = {3: (0, 1), 4: (1, 2), 5: (0, 2)}
    for a in dd:
        for b in dd:
            if a != b:
                c = 3 - a - b; X[a, b] = -K[c] ** 2
    for a in dd:
        for f, (i, j) in fc.items():
            if a not in (i, j):
                X[a, f] = X[f, a] = K[i] * K[j]
    for f, (i, j) in fc.items():
        c = 3 - i - j; X[f, f] = K[c] ** 2 / 2
        for g, (k, l) in fc.items():
            if g != f:
                sh = set((i, j)) & set((k, l)); o1 = (set((i, j)) - sh).pop(); o2 = (set((k, l)) - sh).pop()
                X[f, g] = -K[o1] * K[o2] / 2
    return X


def Gr(q):
    K = 2 * np.sin(q / 2); G = np.zeros((3, 6))
    for j in range(3):
        G[j, j] = K[j]
    for f, (i, j) in {3: (0, 1), 4: (1, 2), 5: (0, 2)}.items():
        G[i, f] = K[j]; G[j, f] = K[i]
    return G


qd = np.array([0.3, 0.5, 0.81]); qd /= np.linalg.norm(qd)
ratios = []; ttX = []; okF = True
for qq in [0.2, 0.1, 0.05, 0.025]:
    q = qq * qd; K = 2 * np.sin(q / 2); t = K @ K
    X = Xr(q); Gq = Gr(q)
    okF &= np.abs(Gq @ X).max() < 1e-12
    s = np.array([-(t - K[0] ** 2), -(t - K[1] ** 2), -(t - K[2] ** 2), K[0] * K[1], K[1] * K[2], K[0] * K[2]])
    M = np.diag([1, 1, 1, 2, 2, 2.]) - np.outer([1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0]) / 2
    okF &= np.abs(X @ M @ X - t * X - np.outer(s, s) / 2).max() < 1e-12
    # TT subspace of the comparator (E-space): ker G_r with the scalar-gauge direction s_r removed; X_r restricted there is t times a fixed positive form
    _, sv, vh = np.linalg.svd(np.vstack([Gq, s[None, :]])); TT = vh[np.sum(sv > 1e-12):].T
    ttX.append(np.linalg.eigvalsh(TT.T @ X @ TT) / t)
    N = phys_basis(q)
    Vq = sum(np.outer(fourier(f, q), fourier(f, q).conj()) for f in famQ)
    ratios.append(np.linalg.eigvalsh(N.conj().T @ Vq @ N).max() / t)
slope = np.polyfit(np.log([0.2, 0.1, 0.05, 0.025]), np.log(ratios), 1)[0]
plaq = [(np.array([1, 0, 0.]), 0, +1), (np.array([2, 1, 0.]), 1, +1), (np.array([1, 2, 0.]), 0, -1), (np.array([0, 1, 0.]), 1, -1)]
u1 = []
for qq in [0.2, 0.1, 0.05]:
    q = qq * qd; v = np.zeros(3, complex)
    for p, a, c in plaq:
        v[a] += c * np.exp(0.5j * q @ p)
    u1.append(np.linalg.norm(v) ** 2 / qq ** 2)
u1_first = sum(c * p / 2 for p, a, c in plaq if a == 0)
okF &= all(len(v) == 2 and v.min() > 0.4 for v in ttX) and np.abs(ttX[-1] - ttX[-2]).max() < 1e-3
check("F: comparators: the landed linear comparator's stiffness is g*t = O(q^2) (TT restriction of its potential symbol / t positive and convergent; its identities G_r X_r = 0 and X_r M X_r = t X_r + s s^T/2 re-verified); the qubit family's is O(q^4), their ratio falling with slope 2; U(1) ring moves keep a first moment and give O(q^2)",
      okF and abs(slope - 2) < 0.05 and abs(u1[-1] / u1[-2] - 1) < 0.01 and np.abs(u1_first).max() > 0,
      f"comparator TT potential / t at q = 0.025: {np.round(ttX[-1], 4)}; qubit/linear stiffness ratio at q = 0.2..0.025: {[round(float(r), 5) for r in ratios]}, log-log slope {slope:.3f}; U(1) plaquette |m_hat|^2/q^2 -> {u1[-1]:.4f} (first moment of its x-links {[float(a) for a in u1_first]}, not zero)")

# ---------------------------------------------------------------- G: moment-chain consequences (Gaussian illustrations)
qd = np.array([0.3, 0.5, 0.81]); qd /= np.linalg.norm(qd); ks = [0.2, 0.1, 0.05, 0.025]
soft, lin, Sl, chil = [], [], [], []
for qq in ks:
    q = qq * qd; N = phys_basis(q)
    V = N.conj().T @ sum(np.outer(fourier(f, q), fourier(f, q).conj()) for f in famQ) @ N
    soft.append(np.sqrt(np.linalg.eigvalsh(V)))                 # J = 1: finite electric susceptibility chi = 1
    t = (2 * np.sin(q / 2)) @ (2 * np.sin(q / 2)); J = 1.0 / t     # incompressible electric energy J(q) = 1/t
    w_ = np.sqrt(J * np.linalg.eigvalsh(V)); lin.append(w_)
    Sl.append(w_ / (2 * J)); chil.append(1 / J)                 # Gaussian: S = omega/(2J), chi = 1/J per mode
sl_soft = np.polyfit(np.log(ks), np.log([s.min() for s in soft]), 1)[0]
sl_lin = np.polyfit(np.log(ks), np.log([s.min() for s in lin]), 1)[0]
sl_S = np.polyfit(np.log(ks), np.log([s.min() for s in Sl]), 1)[0]
sl_chi = np.polyfit(np.log(ks), np.log(chil), 1)[0]
check("G: moment-chain consequences: with a finite electric susceptibility the qubit family gives omega ~ q^2; a light-cone mode needs an electric energy growing like 1/q^2, i.e. chi ~ q^2 and S ~ q^3",
      abs(sl_soft - 2) < 0.02 and abs(sl_lin - 1) < 0.02 and abs(sl_S - 3) < 0.02 and abs(sl_chi - 2) < 0.02,
      f"exponents: omega (chi fixed) {sl_soft:.3f}; omega (chi = t) {sl_lin:.3f}, S {sl_S:.3f}, chi {sl_chi:.3f}; the exact chain omega_min <= sqrt(m1/m_-1) <= m1/m0 (landed ring-model note) turns m1 <= C q^4 into omega_min <= sqrt(2C/chi) q^2 and omega_min <= C q^4/S")

print("N5 resolution 1: qubit-carriable moves exist; the landed ten-slot move's +-2 entries cancel in a 2x2 planar block, and a separate 3D move reaches the cross shear.")
print("N5 resolution 2: the double-commutator sum rule is exact for any eigenstate and any finite local dimension with commuting unit-step electric spectra, term-by-term sector preservation and a uniform constant; no small-field expansion is used.")
print("N5 resolution 3: finite-support kernel moves have vanishing zeroth and first moments (the landed lemma, re-verified), so every active change component moves the electric field at order q^2.")
print("N5 resolution 4: the linear comparator's order-q^2 sum rule is not reachable by a fixed bounded finite-range linear readout; a light-cone LOWEST weighted mode needs chi = O(q^2) (necessary, not sufficient), which no check here constructs.")
print("per_element: every witness move is checked row by row against the landed stencil; every rotation image is recomputed from the tensor transformation law.")
print("per_site: slot positions (vertex, face) and row positions (link) follow the landed doubled-lattice placement; the moment lemma uses those positions.")
print("per_mode: physical-block stiffness eigenvalues at each momentum and direction; Taylor bound checked per image and zone point.")
print("per_block: MILP searches in radius-1 and radius-2 boxes with every touching row imposed; a dense 2^10-dimensional check of the operator identity and sum rule.")
print("lattice_wide: checked and not executed - a native qubit ground state, its susceptibility chi(q) and a thermodynamic phase are not computed; box-free minimum support is not claimed.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
