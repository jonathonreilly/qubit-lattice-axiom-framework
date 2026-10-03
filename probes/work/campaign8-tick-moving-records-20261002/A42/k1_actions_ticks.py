"""A42 check k1: the four onsite actions, their centralizers, and explicit
nearest-neighbour ticks tested for exact covariance on the 7-site star.

A tick alpha is translation invariant by construction (same gates everywhere),
so covariance under rotations about every site reduces to
    alpha(rho(R) a rho(R)^dag at 0) == Gamma_R(alpha(a at 0))
for a in {sx, sy, sz} and all 24 R, with Gamma_R = onsite rho(R) on the 7 sites
composed with the site permutation p -> R p.  Internal symmetries g (same turn
at every site) are tested the same way with no site permutation.  The flip
(all three Paulis -> minus) is antilinear: O -> Y^7 conj(O) Y^7.
"""
import itertools, numpy as np

np.set_printoptions(precision=4, suppress=True)
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
PAULI = [SX, SY, SZ]

def sig(n):
    n = np.asarray(n, float); n = n / np.linalg.norm(n)
    return n[0] * SX + n[1] * SY + n[2] * SZ

# ---------- the 24 proper rotations and the four actions (menu matrices) ----------
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3), int)
        for i, p in enumerate(perm):
            R[p, i] = signs[i]
        if round(np.linalg.det(R)) == 1:
            ROTS.append(R)
assert len(ROTS) == 24

def sgn(R):  # sign character of O = S4 = sign of the axis permutation
    return int(round(np.linalg.det(np.abs(R))))

ACTIONS = {
    'trivial': lambda R: np.eye(3),
    'sign_twist': lambda R: np.diag([1, sgn(R), sgn(R)]).astype(float),  # menu: diag(1,s,s)
    'axis': lambda R: sgn(R) * np.abs(R).astype(float),                   # menu: s|g|
    'full': lambda R: R.astype(float),                                    # menu: g
}

def su2_of(Rb):
    """SU(2) element whose adjoint action on Bloch vectors is Rb (in SO(3))."""
    Rb = np.asarray(Rb, float)
    if np.allclose(Rb, np.eye(3)):
        return I2.copy()
    ang = np.arccos(np.clip((np.trace(Rb) - 1) / 2, -1, 1))
    if abs(ang - np.pi) < 1e-6:
        ang = np.pi
        Pn = (Rb + np.eye(3)) / 2          # = n n^T for a half-turn
        k = np.argmax(np.diag(Pn))
        n = Pn[:, k] / np.sqrt(Pn[k, k])
    else:
        n = np.array([Rb[2, 1] - Rb[1, 2], Rb[0, 2] - Rb[2, 0], Rb[1, 0] - Rb[0, 1]]) / (2 * np.sin(ang))
    U = np.cos(ang / 2) * I2 - 1j * np.sin(ang / 2) * sig(n)
    for j in range(3):  # verify U s_j U^dag = sum_i Rb_ij s_i
        lhs = U @ PAULI[j] @ U.conj().T
        rhs = sum(Rb[i, j] * PAULI[i] for i in range(3))
        assert np.allclose(lhs, rhs), (Rb, ang, n)
    return U

def check_homomorphism(rho):
    bad = 0
    for A in ROTS:
        for B in ROTS:
            if not np.allclose(rho(A @ B), rho(A) @ rho(B)):
                bad += 1
    return bad

def character_split(rho):
    # multiplicities of A1, A2, E, T1, T2 from characters by conjugacy class
    def cls(R):
        t = int(round(np.trace(R)))
        return {3: 'e', -1: ('C2' if sgn(R) == 1 else "C2'"), 0: 'C3', 1: 'C4'}[t]
    chi = {'e': [1, 1, 2, 3, 3], 'C3': [1, 1, -1, 0, 0], 'C2': [1, 1, 2, -1, -1],
           'C4': [1, -1, 0, 1, -1], "C2'": [1, -1, 0, -1, 1]}
    mult = np.zeros(5)
    for R in ROTS:
        mult += np.trace(rho(R)) * np.array(chi[cls(R)])
    return dict(zip(['A1', 'A2', 'E', 'T1', 'T2'], np.round(mult / 24).astype(int)))

def centralizer_dim(mats):
    # dimension of {X in M3(R): X M = M X for all M}
    rows = []
    for M in mats:
        rows.append(np.kron(np.eye(3), M) - np.kron(M.T, np.eye(3)))
    A = np.vstack(rows)
    return 9 - np.linalg.matrix_rank(A, tol=1e-9)

# ---------- 7-site star patch ----------
SITES = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
NS = len(SITES)
IDX = {s: i for i, s in enumerate(SITES)}

def kron_all(ops):
    out = np.array([[1]], complex)
    for o in ops:
        out = np.kron(out, o)
    return out

def onsite(op, site):
    ops = [I2] * NS; ops[site] = op
    return kron_all(ops)

def site_perm(O, R):
    """Move operator content at site p to site R p."""
    perm = [IDX[tuple(int(v) for v in (R @ np.array(s)))] for s in SITES]  # p -> perm[p]
    T = O.reshape([2] * (2 * NS))
    # output axes: new tensor index at position perm[p] takes old index p
    inv = [0] * NS
    for p, q in enumerate(perm):
        inv[q] = p
    axes = [inv[q] for q in range(NS)] + [NS + inv[q] for q in range(NS)]
    return T.transpose(axes).reshape(2 ** NS, 2 ** NS)

def global_onsite(U):
    return kron_all([U] * NS)

def Gamma(O, R, rho):
    U = global_onsite(su2_of(rho(R)))
    return U @ site_perm(O, R) @ U.conj().T

def expm_herm(H, t):
    w, v = np.linalg.eigh(H)
    return (v * np.exp(1j * t * w)) @ v.conj().T

def edge_layer(gate2):
    """Product of a symmetric 2-site gate on the six edges at the centre."""
    G = np.eye(2 ** NS, dtype=complex)
    for k in range(1, NS):
        # embed gate on (0,k)
        ops = None
        g = gate2.reshape(2, 2, 2, 2)
        full = np.zeros((2 ** NS, 2 ** NS), complex)
        # build via Pauli expansion of gate2
        for a, Pa in enumerate([I2, SX, SY, SZ]):
            for b, Pb in enumerate([I2, SX, SY, SZ]):
                c = np.trace(np.kron(Pa, Pb).conj().T @ gate2) / 4
                if abs(c) > 1e-14:
                    o = [I2] * NS; o[0] = Pa; o[k] = Pb
                    full += c * kron_all(o)
        G = full @ G
    return G

def make_tick(onsite_u=None, gate2=None):
    """alpha(a_0) = G (u a u^dag)_0 G^dag, G = product of the 6 edge gates at 0."""
    u = I2 if onsite_u is None else onsite_u
    G = np.eye(2 ** NS, dtype=complex) if gate2 is None else edge_layer(gate2)
    def alpha(a):
        return G @ onsite(u @ a @ u.conj().T, 0) @ G.conj().T
    return alpha

def ising(n, th):
    s = sig(n)
    return expm_herm(np.kron(s, s), th)

def cz_axis(n):
    s = sig(n)
    P = (I2 - s) / 2
    return np.eye(4) - 2 * np.kron(P, P)

def rot(n, phi):
    return np.cos(phi / 2) * I2 - 1j * np.sin(phi / 2) * sig(n)

w = np.array([1, 1, 1]) / np.sqrt(3)
TICKS = {
    'onsite rot x (0.7)': make_tick(onsite_u=rot([1, 0, 0], 0.7)),
    'onsite rot z (0.7)': make_tick(onsite_u=rot([0, 0, 1], 0.7)),
    'onsite half-turn w': make_tick(onsite_u=sig(w)),
    'onsite half-turn (y+z)': make_tick(onsite_u=sig([0, 1, 1])),
    'Ising x (0.37)': make_tick(gate2=ising([1, 0, 0], 0.37)),
    'Ising z (0.37)': make_tick(gate2=ising([0, 0, 1], 0.37)),
    'Ising w (0.37)': make_tick(gate2=ising(w, 0.37)),
    'Ising z (pi/4)': make_tick(gate2=ising([0, 0, 1], np.pi / 4)),
    'mover C_s = CZ_z . H_xz': make_tick(onsite_u=sig([1, 0, 1]), gate2=cz_axis([0, 0, 1])),
    "mover C_s' = CZ_z . H_yz": make_tick(onsite_u=sig([0, 1, 1]), gate2=cz_axis([0, 0, 1])),
    'w-controlled: Ising w . half-turn w': make_tick(onsite_u=sig(w), gate2=ising(w, 0.37)),
}

def covariant_spatial(alpha, rho):
    fails = 0
    imgs = [alpha(P) for P in PAULI]
    for R in ROTS:
        U = su2_of(rho(R))
        for j, P in enumerate(PAULI):
            lhs = alpha(U @ P @ U.conj().T)
            rhs = Gamma(imgs[j], R, rho)
            if not np.allclose(lhs, rhs, atol=1e-9):
                fails += 1
    return fails

def covariant_internal(alpha, us):
    fails = 0
    for u in us:
        Ug = global_onsite(u)
        for P in PAULI:
            if not np.allclose(alpha(u @ P @ u.conj().T), Ug @ alpha(P) @ Ug.conj().T, atol=1e-9):
                fails += 1
    return fails

def covariant_flip(alpha):
    Yall = global_onsite(SY)
    fails = 0
    for P in PAULI:
        lhs = alpha(-P)
        rhs = Yall @ alpha(P).conj() @ Yall
        if not np.allclose(lhs, rhs, atol=1e-9):
            fails += 1
    return fails

if __name__ == '__main__':
    print('== the four actions (menu matrices) ==')
    for name, rho in ACTIONS.items():
        imgs = [rho(R) for R in ROTS]
        dets = {int(round(np.linalg.det(M))) for M in imgs}
        print(f"{name:11s} hom-failures={check_homomorphism(rho)} det={dets} split={character_split(rho)} "
              f"|image|={len({tuple(np.round(M,6).ravel()) for M in imgs})} commutant-dim(M3R)={centralizer_dim(imgs)}")
    # invariant lines of rho(Stab(e_z)) (quarter turn about z)
    Qz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    print('quarter turn about z acts on Bloch vectors as:')
    for name, rho in ACTIONS.items():
        M = rho(Qz); ev, V = np.linalg.eig(M)
        print(f"  {name:11s} {M.tolist()}  eigenvalues {np.round(ev,4).tolist()}")
    # centralizer of the image inside SO(3): test candidates
    print('onsite turns that commute with the whole image (centralizer in SO(3)), spot tests:')
    cands = {'half-turn w': su2_of(2*np.outer(w, w) - np.eye(3)),
             'rot x 0.7': rot([1, 0, 0], 0.7), 'half-turn (y+z)': sig([0, 1, 1]),
             'rot w 2pi/3': rot(w, 2*np.pi/3), 'rot w 0.7': rot(w, 0.7)}
    for name, rho in ACTIONS.items():
        ok = []
        for cn, u in cands.items():
            Rb = np.array([[np.real(np.trace(PAULI[i] @ u @ PAULI[j] @ u.conj().T)) / 2 for j in range(3)] for i in range(3)])
            if all(np.allclose(Rb @ rho(R), rho(R) @ Rb) for R in ROTS):
                ok.append(cn)
        print(f"  {name:11s} commuting: {ok}")

    print('\n== covariance of explicit nearest-neighbour ticks (fail counts; 0 = exactly covariant) ==')
    rng = np.random.default_rng(7)
    def rand_su2():
        q = rng.normal(size=4); q /= np.linalg.norm(q)
        return q[0] * I2 - 1j * (q[1] * SX + q[2] * SY + q[3] * SZ)
    rand_us = [rand_su2() for _ in range(3)]
    pauli_us = [SX, SY, SZ]
    cyc = su2_of(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]))  # X->Y->Z->X
    tet_us = pauli_us + [cyc]
    hdr = f"{'tick':38s} {'triv':>4s} {'twist':>5s} {'axis':>4s} {'full':>4s} | {'SU2':>3s} {'Pauli':>5s} {'C3':>3s} {'T':>3s} {'flip':>4s}"
    print(hdr)
    for tn, al in TICKS.items():
        r = [covariant_spatial(al, ACTIONS[a]) for a in ['trivial', 'sign_twist', 'axis', 'full']]
        s = [covariant_internal(al, rand_us), covariant_internal(al, pauli_us),
             covariant_internal(al, [cyc]), covariant_internal(al, tet_us), covariant_flip(al)]
        print(f"{tn:38s} {r[0]:4d} {r[1]:5d} {r[2]:4d} {r[3]:4d} | {s[0]:3d} {s[1]:5d} {s[2]:3d} {s[3]:3d} {s[4]:4d}")
    # nontriviality: each tick moves some Pauli at the centre
    print('\nnontrivial (alpha(P_0) != P_0 for some P):',
          {tn: any(not np.allclose(al(P), onsite(P, 0)) for P in PAULI) for tn, al in TICKS.items()})
