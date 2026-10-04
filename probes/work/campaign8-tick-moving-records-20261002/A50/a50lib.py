"""A50 shared helpers: covariant product dressings under the exact soldered action (Q3),
per-site Levin-Wen words, link part on the six leg links, state-vector cross-check.

Sites are integer offsets from the corner v = (0,0,0).  Kind = number of odd coordinates
(0 corner, 1 edge/link, 2 face, 3 cube).  A link's field axis is its odd coordinate.
Hop t_i (i = leg index in DIRS) = raise_out(i) on link DIRS[i] (x) product of 2x2 factors.
theta(i,j,k): t_i t_j^dag t_k = theta t_k t_j^dag t_i.
"""
import sys, itertools
import numpy as np
sys.path.insert(0, '/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A48')
from a48lib import (ROT, RIDX, MUL, ID, INV, DIRS, NAMES, AXIS, SIGN, PERM, GROUPS, C4, C2, C3d,
                    su2_of_rot, rot_axis_angle, raise_out, I2, SX, SY, SZ, PAUL, key, closure)

U = [su2_of_rot(R) for R in ROT]
GRP = {'O': GROUPS['O (24 turns)'], 'T': GROUPS['T (12 even turns)'],
       'D2': GROUPS['D2 (3 axis half-turns)'], 'C2z': GROUPS['{1, C2z}']}
LEGLINK = [tuple(d) for d in DIRS]
TRIPLES = list(itertools.combinations(range(6), 3))
def is_T(tri):
    return any(AXIS[a] == AXIS[b] for a, b in itertools.combinations(tri, 2))
T_TRI = [t for t in TRIPLES if is_T(t)]
C_TRI = [t for t in TRIPLES if not is_T(t)]

def kind(o):
    return sum(c % 2 for c in o)
def link_axis(o):
    return [c % 2 for c in o].index(1)
def act(g, o):
    return tuple(int(v) for v in ROT[g] @ np.array(o))
def ad(g, m):
    return U[g] @ m @ U[g].conj().T
def window(rad, extra=()):
    w = [o for o in itertools.product(range(-rad, rad + 1), repeat=3)]
    return w + [tuple(e) for e in extra if tuple(e) not in w]
FAR = [tuple(2 * np.array(d)) for d in DIRS]
W27 = window(1)
WFAR = window(1, FAR)
AXSITES = [(0, 0, 0)] + list(LEGLINK) + FAR          # v, 6 links, 6 far corners

def su2_exp(a):
    """exp(i a.sigma) for a real 3-vector."""
    a = np.asarray(a, float); t = np.linalg.norm(a)
    if t < 1e-15:
        return I2.copy()
    n = a / t
    return np.cos(t) * I2 + 1j * np.sin(t) * (n[0] * SX + n[1] * SY + n[2] * SZ)
def nsig(n):
    return n[0] * SX + n[1] * SY + n[2] * SZ
def rot_of(u):
    """SO(3) matrix of Ad(u)."""
    return np.array([[0.5 * np.trace(PAUL[b + 1] @ u @ PAUL[a + 1] @ u.conj().T).real
                      for a in range(3)] for b in range(3)])

CLIFF = U   # the 24 single-qubit Clifford rotations (lifts), mod phase

def stab_type(S):
    """classify a stabilizer subgroup S (indices) of a leg stabilizer: ('triv',), ('so2', n), ('o2', n)."""
    if len(S) == 1:
        return ('triv', None)
    g = max(S, key=lambda k: -np.trace(ROT[k]))   # smallest trace = largest angle; pick any non-id
    nonid = [k for k in S if k != ID]
    k = nonid[0]
    R = ROT[k].astype(float)
    w, v = np.linalg.eig(R)
    n = np.real(v[:, np.argmin(abs(w - 1))]); n = n / np.linalg.norm(n)
    orders = set()
    for k in nonid:
        Rk = ROT[k]; m = 1; M = Rk.copy()
        while not np.array_equal(M, np.eye(3, dtype=int)):
            M = M @ Rk; m += 1
        orders.add(m)
    return ('so2', n) if max(orders) >= 3 else ('o2', n)

def centralizer_cliffords(S, field_axis=None):
    out = []
    for k in range(24):
        if field_axis is not None:
            if not np.allclose(ROT[k][:, field_axis] * 1.0, np.eye(3)[field_axis]):
                continue
        if all(np.array_equal(ROT[k] @ ROT[s], ROT[s] @ ROT[k]) for s in S):
            out.append(U[k])
    return out

def sample_seed(o, S, rng, mode):
    """a 2x2 unitary at site o, Ad-invariant up to phase under stabilizer S.
    links: field-diagonal exp(i phi sigma^a).  mode in {'id','cliff','cont','mix'}."""
    if mode == 'mix':
        mode = rng.choice(['id', 'cliff', 'cont'], p=[0.3, 0.35, 0.35])
    if mode == 'id':
        return I2.copy()
    if kind(o) == 1:
        a = link_axis(o)
        if mode == 'cliff':
            phi = np.pi / 4 * rng.integers(4)
        else:
            phi = rng.uniform(0, np.pi)
        e = np.zeros(3); e[a] = phi
        return su2_exp(e)
    st, n = stab_type(S)
    if mode == 'cliff':
        pool = centralizer_cliffords(S)
        return pool[rng.integers(len(pool))]
    if st == 'triv':
        q = rng.normal(size=4); q /= np.linalg.norm(q)
        return q[0] * I2 + 1j * (q[1] * SX + q[2] * SY + q[3] * SZ)
    if st == 'so2' or rng.random() < 0.5:
        return su2_exp(rng.uniform(0, np.pi) * n)
    b = np.cross(n, rng.normal(size=3)); b /= np.linalg.norm(b)
    return nsig(b)

def build_hops(G, win, seeder, gauss_bits=None):
    """covariant product dressings: seeds on orbit reps of each leg-orbit rep's stabilizer,
    transported by the exact soldered action.  seeder(o, S) -> 2x2.  Returns list of 6 dicts."""
    hops = [None] * 6
    wset = set(win)
    for i0 in range(6):
        if hops[i0] is not None:
            continue
        H = [g for g in G if PERM[g][i0] == i0]
        h0 = {LEGLINK[i0]: raise_out(i0)}
        for x in win:
            if x in h0:
                continue
            S = [h for h in H if act(h, x) == x]
            u = seeder(x, S)
            for h in H:
                y = act(h, x)
                assert y in wset
                if y not in h0:
                    h0[y] = ad(h, u)
        for g in G:
            i = PERM[g][i0]
            if hops[i] is None:
                hops[i] = {act(g, y): ad(g, m) for y, m in h0.items()}
    if gauss_bits is not None:   # multiply hop i by B_v^{c_i}: sigma^a on the six links at v
        for i in range(6):
            if gauss_bits[i]:
                for m in range(6):
                    s = LEGLINK[m]
                    hops[i][s] = hops[i].get(s, I2) @ PAUL[AXIS[m] + 1]
    return hops

def phase_fit(A, B):
    nb = np.vdot(B, B).real
    if nb < 1e-14:
        return None, np.inf
    c = np.vdot(B, A) / nb
    return c, np.linalg.norm(A - c * B) / np.sqrt(nb)

def covariance_residual(hops, G, win):
    worst = 0.0
    for g in G:
        for i in range(6):
            gi = PERM[g][i]
            for x in win:
                A = ad(g, hops[i].get(x, I2)); B = hops[gi].get(act(g, x), I2)
                c, r = phase_fit(A, B)
                if c is None or abs(abs(c) - 1) > 1e-6:
                    r = max(r, 1.0)
                worst = max(worst, r)
    return worst

def site_word(ui, uj, uk):
    W = ui.conj().T @ uj @ uk.conj().T @ ui @ uj.conj().T @ uk
    lam = np.trace(W) / 2
    return lam, np.linalg.norm(W - lam * I2)

def kron6(ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out

def link_part(hops, tri):
    i, j, k = tri
    T = [kron6([hops[h].get(LEGLINK[m], I2) for m in range(6)]) for h in (i, j, k)]
    T1 = T[0] @ T[1].conj().T @ T[2]
    T2 = T[2] @ T[1].conj().T @ T[0]
    return phase_fit(T1, T2)

def junction(hops, tri, win, tol=1e-9, detail=False):
    """theta for ordered triple tri (None if not scalar), max residual, per-site lambdas."""
    i, j, k = tri
    cL, rL = link_part(hops, tri)
    theta = cL; worst = rL; lams = {}
    for x in win:
        if x in LEGLINK:
            continue
        lam, r = site_word(hops[i].get(x, I2), hops[j].get(x, I2), hops[k].get(x, I2))
        worst = max(worst, r)
        theta = theta * lam
        if detail and abs(lam - 1) > 1e-9:
            lams[x] = lam
    ok = worst < tol
    return (theta if ok else None), worst, lams

def all_junctions(hops, win, tol=1e-9):
    return {tri: junction(hops, tri, win, tol)[:2] for tri in TRIPLES}

# ---------- state-vector cross-check (no dense operators) ----------
def apply_prod(ops, psi, n):
    psi = psi.reshape((2,) * n)
    for q, m in enumerate(ops):
        if m is None:
            continue
        psi = np.moveaxis(np.tensordot(m, psi, axes=([1], [q])), 0, q)
    return psi.reshape(-1)

def sv_junction(hops, tri, sites, rng, nvec=3):
    """theta from t_i t_j^dag t_k psi vs t_k t_j^dag t_i psi on random psi, sites = qubit list."""
    n = len(sites)
    def ops(h, dag=False):
        L = [hops[h].get(s, None) for s in sites]
        return [None if m is None else (m.conj().T if dag else m) for m in L]
    i, j, k = tri
    cs = []; res = 0.0
    for _ in range(nvec):
        psi = rng.normal(size=2 ** n) + 1j * rng.normal(size=2 ** n)
        a = apply_prod(ops(i), apply_prod(ops(j, True), apply_prod(ops(k), psi, n), n), n)
        b = apply_prod(ops(k), apply_prod(ops(j, True), apply_prod(ops(i), psi, n), n), n)
        c, r = phase_fit(a, b); cs.append(c); res = max(res, r)
    return cs[0], res, max(abs(c - cs[0]) for c in cs)

# ---------- fast transport map (same seeding order as build_hops) ----------
def build_map(G, win):
    """returns struct = [(o, S)], entries = list of (leg, site, seed_index or -1-own_leg, turn)."""
    struct = []; entries = []
    done = [False] * 6
    wset = set(win)
    for i0 in range(6):
        if done[i0]:
            continue
        H = [g for g in G if PERM[g][i0] == i0]
        h0 = {LEGLINK[i0]: (-1 - i0, ID)}
        for x in win:
            if x in h0:
                continue
            S = [h for h in H if act(h, x) == x]
            e = len(struct); struct.append((x, S))
            for h in H:
                y = act(h, x)
                if y not in h0:
                    h0[y] = (e, h)
        for g in G:
            i = PERM[g][i0]
            if not done[i]:
                done[i] = True
                for y, (e, h) in h0.items():
                    entries.append((i, act(g, y), e, MUL[g][h]))
    return struct, entries

class FastHops:
    def __init__(self, G, win):
        self.struct, self.entries = build_map(G, win)
        self.nonleg = [x for x in win if x not in LEGLINK]
        sidx = {x: n for n, x in enumerate(self.nonleg)}
        E = [(i, sidx[y], e, g) for (i, y, e, g) in self.entries if y in sidx]
        self.Li, self.Ls, self.Le = (np.array([t[k] for t in E]) for k in range(3))
        self.LU = np.array([U[t[3]] for t in E])
        self.linkE = [(i, LEGLINK.index(y), e, g) for (i, y, e, g) in self.entries if y in LEGLINK]
    def arrays(self, seeds):
        """seeds: array (nstruct,2,2).  Returns A (6, nsites, 2, 2) and link factors [leg][link]."""
        A = np.broadcast_to(I2, (6, len(self.nonleg), 2, 2)).copy()
        Ug = self.LU
        A[self.Li, self.Ls] = Ug @ seeds[self.Le] @ np.conj(np.swapaxes(Ug, -1, -2))
        L = [[I2] * 6 for _ in range(6)]
        for (i, m, e, g) in self.linkE:
            base = raise_out(-1 - e) if e < 0 else seeds[e]
            L[i][m] = U[g] @ base @ U[g].conj().T
        return A, L
