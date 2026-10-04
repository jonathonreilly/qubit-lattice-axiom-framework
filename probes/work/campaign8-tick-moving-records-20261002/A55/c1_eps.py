"""A55 c1: exact transformation of the staggered sign eps(x) = (-1)^(x1+x2+x3) (coarse x, corner v = 2x fine)
under the turns that preserve the 2x2x2 role pattern (about corners, cube centres, link centres, face centres) and
under coarse translations; covariance of the Gauss parity P_v and the U(1) divergence G_v; KS gap with eps-mass."""
import signal, sys, itertools
signal.alarm(100)
import numpy as np
sys.path.insert(0, '/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A52')
from a52lib import ROT, DIRS, Torus, gauss_string, turn_string

def eps(x):
    return (-1) ** int(round(sum(x)))

def perm_sign_parity(R):
    """parity of the underlying coordinate permutation of the signed permutation matrix R."""
    p = [int(np.nonzero(R[i])[0][0]) for i in range(3)]
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return inv % 2

rng = np.random.default_rng(55)
pts = [rng.integers(-5, 6, size=3) for _ in range(40)]
centres = {'corner (0,0,0)': (0, 0, 0), 'cube centre (1/2,1/2,1/2)': (.5, .5, .5),
           'link centre (1/2,0,0)': (.5, 0, 0), 'face centre (1/2,1/2,0)': (.5, .5, 0)}
print("Q1(a) eps under turns x -> c + R(x - c) that map corners to corners (coarse units):")
for name, c in centres.items():
    c = np.array(c)
    keep = []; flip = []; bad = 0
    for g, R in enumerate(ROT):
        sh = c - R @ c
        if np.max(np.abs(sh - np.round(sh))) > 1e-12:
            continue                              # not a symmetry of the corner lattice
        ratios = {eps(np.round(c + R @ (x - c))) * eps(x) for x in pts}
        if len(ratios) != 1:
            bad += 1
        (keep if ratios == {1} else flip).append(g)
    nodd_keep = sum(perm_sign_parity(ROT[g]) for g in keep); nodd_flip = sum(perm_sign_parity(ROT[g]) for g in flip)
    print("  %-26s pattern-preserving turns %2d: eps kept by %2d (odd perms %d), flipped by %2d (odd perms %d); non-constant ratio %d"
          % (name, len(keep) + len(flip), len(keep), nodd_keep, len(flip), nodd_flip, bad))
print("  rule: eps(c+R(x-c)) = eps(x) * (-1)^{sum(c - Rc)}; for a corner centre the sum is even for all 24 turns.")

print("Q1(b) eps under coarse translations a: ratio (-1)^{sum a}")
for a in [(1, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (1, -1, 0)]:
    r = {eps(np.array(x) + np.array(a)) * eps(x) for x in pts}
    print("  a=%s: ratio %s" % (a, r))

# (c) covariance of the Gauss parity P_v (Z2 form) under turns about a corner and a cube centre (symbolic Pauli strings)
tor = Torus(4)
bad = 0; tot = 0
for cen in [(0, 0, 0), (2, 2, 2), (1, 1, 1), (3, 1, 5)]:
    for g in range(24):
        R = ROT[g]
        # only pattern-preserving turns (fine centre c: c - Rc even)
        sh = np.array(cen) - R @ np.array(cen)
        if np.any(sh % 2):
            continue
        for v in tor.corners:
            img = turn_string(tor, g, gauss_string(tor, v), cen)
            gv = tor.turn(g, v, cen)
            tot += 1
            if img[:2] != gauss_string(tor, gv)[:2]:
                bad += 1
print("Q1(c) Gauss parity P_v = prod of the 6 leg Z's maps to P_{gv}: %d/%d mismatches (turns about corners and cube centres)" % (bad, tot))

# (d) U(1) divergence G_v = sum_legs (outward E): E on a link = field along +axis; a turn maps +e_a to s e_a' -> E -> s E'
bad = 0; tot = 0
for g in range(24):
    R = ROT[g]
    for leg in range(6):
        d = np.array(DIRS[leg])
        # outward field on leg d at v: sign(d) * E_link(v + d/2); image: outward field on leg R d at gv
        s_out = int(np.sign(d.sum()))
        Rd = R @ d; s_img = int(np.sign(Rd.sum()))
        # E_link transforms by the sign of the image of its +axis vector
        a = int(np.nonzero(d)[0][0]); ea = np.zeros(3, int); ea[a] = 1
        s_link = int((R @ ea).sum())
        tot += 1
        if s_out * s_link != s_img:
            bad += 1
print("Q1(d) U(1) divergence: outward leg field maps to outward leg field under all 24 turns: %d/%d failures" % (bad, tot))

# (e) KS pi-flux bands with the staggered mass: |E| = sqrt(4 sum cos^2 k + m^2) (t = 1), 2-site cell along nothing:
# use the c5 gauge u_x = 1, u_y = (-1)^x, u_z = (-1)^(x+y) on a finite torus L^3, real-space diagonalisation
def ks_ham(L, m=0.0):
    N = L ** 3; idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    H = np.zeros((N, N))
    for x, y, z in itertools.product(range(L), repeat=3):
        a = idx(x, y, z)
        for axis, u in [(0, 1), (1, (-1) ** x), (2, (-1) ** (x + y))]:
            e = [0, 0, 0]; e[axis] = 1
            b = idx(x + e[0], y + e[1], z + e[2])
            H[a, b] += -u; H[b, a] += -u
        H[a, a] += m * (-1) ** (x + y + z)
    return H
L = 8
for m in [0.0, 0.3, 1.0]:
    ev = np.sort(np.linalg.eigvalsh(ks_ham(L, m)))
    ks = 2 * np.pi * np.arange(L) / L
    pred = []
    for k in itertools.product(ks, repeat=3):
        e = np.sqrt(4 * np.sum(np.cos(k) ** 2) + m * m)
        pred += [e, -e]
    pred = np.sort(np.array(pred))
    # each k appears with +-; the real-space spectrum has N levels; pred has 2N -> compare with doubled list
    evd = np.sort(np.concatenate([ev, ev]))
    print("Q1(e) 8^3 pi flux, m=%.1f: max |E_realspace - E_formula| = %.1e; half-filling gap = %.4f (2|m| = %.4f)" % (
        m, np.abs(evd - pred).max(), ev[L ** 3 // 2] - ev[L ** 3 // 2 - 1], 2 * m))
# translation T_x maps H(m) to a gauge copy of H(-m): check spectra equal and the eps term anticommutes with hopping
H0 = ks_ham(4, 0.0); Me = ks_ham(4, 1.0) - H0
print("   {hopping, eps-mass} = 0: %.1e;  T_x: eps(x+e_x) = -eps(x) (from (b))" % np.abs(H0 @ Me + Me @ H0).max())
print("done")
