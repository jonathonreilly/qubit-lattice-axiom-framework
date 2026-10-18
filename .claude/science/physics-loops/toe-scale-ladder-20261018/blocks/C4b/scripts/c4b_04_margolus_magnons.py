"""C4b-04: magnon transport in O_c-covariant SU(2)-invariant Margolus QCAs (OUT of the Z^3-TI
premise: these are only 2Z^3-translation invariant, see c4b_03).

Block V on the 8 corners of a 2x2x2 cube.  V commutes with global SU(2) (built from SWAPs or
functions of total S^2) and with the 24 corner permutations of O about the cube centre; hence
it is covariant under O_c with ANY on-site soldering action whose image lies in SO(3)
(trivial/sign/axis/full), because a global SU(2) rotation is the on-site part of beta_R.
Two-step QCA U = V_{P1} V_{P0}.  Magnon number (number of down spins) is conserved.

Blocks:
 (a) V_inv  = product of the 4 body-diagonal SWAPs (= inversion of the cube) -- a permutation QCA
 (b) V_gen  = exp(i (J1 H1 + J2 H2 + J3 H3 - vac)),  H_d = sum of SWAPs over corner pairs at
              Hamming distance d (O_c orbits: 12 edges, 12 face diagonals, 4 body diagonals)
 (c) V_c    = exp(i Pi_{S<=2} (J1 H1 + J2 H2 + J3 H3))  -- identity on the 0- and 1-magnon sectors.
Dynamics is computed EXACTLY on the infinite lattice Z^3 with a sparse dict state (only reachable
configurations), so "support stays bounded" statements are exact up to the number of steps run.
"""
import itertools
import math
import numpy as np
from scipy.linalg import expm
from c4b_common import check, total, O, SX, SY, SZ, I2

CORN = list(itertools.product((0, 1), repeat=3))           # corner c in {0,1}^3
CI = {c: i for i, c in enumerate(CORN)}
J = (0.7, 0.4, 0.25)


def ham(c1, c2):
    return sum(a != b for a, b in zip(c1, c2))


def sector_basis(m):
    return list(itertools.combinations(range(8), m))


def swap_sector(i, j, m):
    B = sector_basis(m)
    idx = {b: k for k, b in enumerate(B)}
    M = np.zeros((len(B), len(B)))
    for k, b in enumerate(B):
        s = set(b)
        t = set()
        for x in s:
            t.add(j if x == i else i if x == j else x)
        M[idx[tuple(sorted(t))], k] = 1
    return M


def Hd_sector(d, m):
    return sum(swap_sector(i, j, m) for i in range(8) for j in range(i + 1, 8) if ham(CORN[i], CORN[j]) == d)


def S2_sector(m):
    # S^2 = 6 + sum_{i<j} SWAP_ij - 14  (spin-1/2, 8 sites)
    tot = sum(swap_sector(i, j, m) for i in range(8) for j in range(i + 1, 8))
    return (6 - 14) * np.eye(tot.shape[0]) + tot   # (first version added the scalar to every entry: bug, see WORKLOG)


VAC = 12 * J[0] + 12 * J[1] + 4 * J[2]


def V_sector(kind, m):
    dim = math.comb(8, m)
    if kind == 'inv':
        M = np.eye(dim)
        for i in range(8):
            for j in range(i + 1, 8):
                if ham(CORN[i], CORN[j]) == 3:
                    M = swap_sector(i, j, m) @ M
        return M.astype(complex)
    H = sum(Jd * Hd_sector(d + 1, m) for d, Jd in enumerate(J))
    if kind == 'gen':
        return expm(1j * (H - VAC * np.eye(dim)))
    if kind == 'c':
        S2 = S2_sector(m)
        w, U = np.linalg.eigh(S2)
        Pi = U[:, w < 2 * 3 + 0.5] @ U[:, w < 2 * 3 + 0.5].T     # S(S+1) <= 6  <=> S <= 2
        return expm(1j * Pi @ H @ Pi)
    raise ValueError


# ---------------------------------------------------------------- full 256-dim covariance checks
def full_op(kind):
    """assemble V on the full 2^8 space from its sectors (basis: bit=1 means magnon/down)."""
    Vf = np.zeros((256, 256), complex)
    for m in range(9):
        B = sector_basis(m)
        Vs = V_sector(kind, m)
        ids = [sum(1 << (7 - i) for i in b) for b in B]
        for a, ia in enumerate(ids):
            for b, ib in enumerate(ids):
                Vf[ia, ib] = Vs[a, b]
    return Vf


def kron_list(ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def tot(p):
    return sum(kron_list([p if k == i else I2 for k in range(8)]) for i in range(8))


def corner_perm(R):
    P = np.zeros((256, 256))
    c0 = np.array([0.5] * 3)
    mp = {}
    for i, c in enumerate(CORN):
        x = R @ (np.array(c) - c0) + c0
        mp[i] = CI[tuple(int(round(v)) for v in x)]
    for s in range(256):
        bits = [(s >> (7 - i)) & 1 for i in range(8)]
        out = [0] * 8
        for i in range(8):
            out[mp[i]] = bits[i]
        P[sum(b << (7 - i) for i, b in enumerate(out)), s] = 1
    return P


TOT = [tot(SX), tot(SY), tot(SZ)]
PERMS = [corner_perm(R) for R in O]
for kind in ['inv', 'gen', 'c']:
    Vf = full_op(kind)
    uni = np.abs(Vf.conj().T @ Vf - np.eye(256)).max()
    su2 = max(np.abs(Vf @ T - T @ Vf).max() for T in TOT)
    oc = max(np.abs(Vf @ P - P @ Vf).max() for P in PERMS)
    check(f"block {kind}: unitary, SU(2)-invariant, commutes with all 24 O_c corner permutations",
          uni < 1e-10 and su2 < 1e-10 and oc < 1e-10, f"{uni:.1e} {su2:.1e} {oc:.1e}")
    if kind == 'c':
        triv = max(np.abs(V_sector('c', m) - np.eye(math.comb(8, m))).max() for m in (0, 1))
        check("block c acts as the identity on the 0- and 1-magnon block sectors", triv < 1e-12)
        nontriv = np.abs(V_sector('c', 2) - np.eye(28)).max()
        check("block c is nontrivial on the 2-magnon block sector", nontriv > 1e-3, f"{nontriv:.3f}")

# ---------------------------------------------------------------- one-magnon Bloch bands
def bloch_U(kind, K):
    v1 = V_sector(kind, 1)          # basis: corner index (single magnon)
    K = np.asarray(K)
    M0 = np.zeros((8, 8), complex)
    M1 = np.zeros((8, 8), complex)
    for c in range(8):
        for cp in range(8):
            dc = np.array(CORN[c]) - np.array(CORN[cp])
            M0[cp, c] = v1[cp, c] * np.exp(1j * K @ dc)
    # P1 block: sites b'+d, b' odd; sublattice class of b'+d is (1+d) mod 2
    cls = lambda d: CI[tuple((1 + x) % 2 for x in CORN[d])]
    for d in range(8):
        for dp in range(8):
            dd = np.array(CORN[d]) - np.array(CORN[dp])
            M1[cls(dp), cls(d)] = v1[dp, d] * np.exp(1j * K @ dd)
    return M1 @ M0


def max_group_velocity(kind, nk=7):
    best = 0.0
    h = 1e-5
    for K in itertools.product(np.linspace(-np.pi / 2, np.pi / 2, nk), repeat=3):
        K = np.array(K) + 0.0137
        U = bloch_U(kind, K)
        w, vecs = np.linalg.eig(U)
        for j in range(3):
            e = np.zeros(3); e[j] = h
            dU = (bloch_U(kind, K + e) - bloch_U(kind, K - e)) / (2 * h)
            # theta = arg(lambda): dtheta = Im(lambda^-1 psi_L dU psi) for normal U (unitary)
            for b in range(8):
                psi = vecs[:, b] / np.linalg.norm(vecs[:, b])
                val = (psi.conj() @ dU @ psi) / w[b]
                best = max(best, abs(val.imag))
    return best


for kind in ['inv', 'gen', 'c']:
    vmax = max_group_velocity(kind)
    print(f"[bands] block {kind}: one-magnon max |d omega/dK_j| = {vmax:.4f} (lattice units per 2-step)")
    if kind == 'c':
        check("block c: one-magnon bands flat (frozen), max group velocity < 1e-8", vmax < 1e-8)
    else:
        check(f"block {kind}: one-magnon bands disperse (max group velocity > 0.1)", vmax > 0.1)


# ---------------------------------------------------------------- exact multi-magnon dynamics on Z^3
VS = {}


def layer(state, kind, par):
    """apply V on every block of partition par (0 or 1) to a dict state {sorted tuple of points: amp}."""
    out = {}
    for conf, amp in state.items():
        blocks = {}
        for x in conf:
            base = tuple(2 * ((xi - par) // 2) + par for xi in x)
            corner = CI[tuple(xi - bi for xi, bi in zip(x, base))]
            blocks.setdefault(base, []).append(corner)
        parts = [[((), amp)]]
        for base, cs in blocks.items():
            m = len(cs)
            key = (kind, m)
            if key not in VS:
                VS[key] = (V_sector(kind, m), {b: k for k, b in enumerate(sector_basis(m))}, sector_basis(m))
            Vm, idx, B = VS[key]
            col = Vm[:, idx[tuple(sorted(cs))]]
            opts = []
            for k in np.nonzero(np.abs(col) > 1e-15)[0]:
                pts = tuple(tuple(bi + ci for bi, ci in zip(base, CORN[c])) for c in B[k])
                opts.append((pts, col[k]))
            parts.append(opts)
        # tensor product of per-block superpositions
        acc = [((), amp)]
        for opts in parts[1:]:
            acc = [(p + q, a * b) for p, a in acc for q, b in opts]
        for pts, a in acc:
            key2 = tuple(sorted(pts))
            out[key2] = out.get(key2, 0) + a
    return {k: v for k, v in out.items() if abs(v) > 1e-14}


def stats(state, c0):
    norm = sum(abs(a) ** 2 for a in state.values())
    msd = 0.0
    reach = 0.0
    for conf, a in state.items():
        com = np.mean(np.array(conf, float), axis=0)
        d2 = float(((com - c0) ** 2).sum())
        msd += abs(a) ** 2 * d2
        reach = max(reach, math.sqrt(d2))
    return norm, msd, reach


def run(kind, init, steps):
    st = {tuple(sorted(init)): 1.0 + 0j}
    c0 = np.mean(np.array(init, float), axis=0)
    rows = []
    for n in range(1, steps + 1):
        st = layer(layer(st, kind, 0), kind, 1)
        norm, msd, reach = stats(st, c0)
        rows.append((n, norm, msd, reach, len(st), st))
        if len(st) > 400000:
            print(f"  [run stopped after n={n}: support {len(st)} exceeds cap 400000 -- operational limit]")
            break
    return rows


def report(label, rows):
    for n, norm, msd, reach, size, _ in rows:
        print(f"  {label} n={n:2d} norm={norm:.12f} <dCOM^2>={msd:9.4f} maxCOMreach={reach:7.3f} |supp|={size}")


# 1 magnon
for kind, steps in [('inv', 6), ('gen', 6), ('c', 6)]:
    rows = run(kind, [(0, 0, 0)], steps)
    report(f"1mag {kind}", rows)
    if kind == 'c':
        check("block c: a single magnon never moves (exact, 6 two-steps)", all(r[3] == 0 for r in rows))
    else:
        check(f"block {kind}: single-magnon COM reach grows linearly (reach(6) >= 6)", rows[-1][3] >= 6 - 1e-9)

# 2 magnons, block c: confinement lemma (exact)
for init in [[(0, 0, 0), (1, 0, 0)], [(0, 0, 0), (1, 1, 1)], [(1, 0, 0), (2, 0, 0)], [(0, 0, 0), (3, 1, 0)]]:
    rows = run('c', init, 8)
    report(f"2mag c {init}", rows[-2:])
    allpts = set(p for r in rows for conf in r[5] for p in conf)
    span = max(max(p[i] for p in allpts) - min(p[i] for p in allpts) for i in range(3))
    check(f"block c, 2 magnons from {init}: support stays inside one 2x2x2 cube (+ initial sites), "
          f"never moves (8 two-steps)", span <= max(1, max(abs(a - b) for a, b in zip(*init))),
          f"coordinate span {span}")

# 2 magnons, block gen: bound-pair diagnostics (one magnon already mobile, for comparison)
rows = run('gen', [(0, 0, 0), (1, 0, 0)], 2)
report("2mag gen", rows)
check("block gen: two-magnon state norm conserved (2 two-steps)", abs(rows[-1][1] - 1) < 1e-9)

# 3 magnons, block c: does a three-magnon cluster move while 1 and 2 are frozen?
for init in [[(0, 0, 0), (1, 0, 0), (2, 0, 0)], [(0, 0, 0), (1, 0, 0), (1, 1, 0)], [(1, 1, 1), (2, 2, 2), (0, 0, 0)]]:
    rows = run('c', init, 6)
    report(f"3mag c {init}", rows)
    check(f"block c, 3 magnons from {init}: norm conserved", abs(rows[-1][1] - 1) < 1e-9)
    print(f"  3mag c {init}: final <dCOM^2> = {rows[-1][2]:.4f}, reach = {rows[-1][3]:.3f}")
total()
