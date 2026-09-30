"""T18 Test B: the repo's coin walker (H = sum_a sigma_a S_a; hop x->x+e_a carries -i sigma_a,
back-hop +i sigma_a; unit-normalised) with two hard-core records.
Far exchange loop: both records ride a rectangular ring clockwise by half its length.
X_plus  : loop operator on C^2 (x) C^2 for the bounded-range (unlabelled, 'boson') rule.
X_minus : same with the Jordan-Wigner sign at every order flip (free-fermion sector K_-).
"""
import numpy as np, itertools
s1 = np.array([[0,1],[1,0]],complex); s2 = np.array([[0,-1j],[1j,0]]); s3 = np.array([[1,0],[0,-1]],complex)
SIG = [s1, s2, s3]
I2 = np.eye(2, dtype=complex)
SWAP = np.zeros((4,4), complex)
for a in range(2):
    for b in range(2):
        SWAP[2*b+a, 2*a+b] = 1

def hop_block(u, v):
    """coin matrix for a nearest-neighbour hop u->v (coordinates)"""
    d = np.array(v) - np.array(u)
    ax = int(np.nonzero(d)[0][0]); sg = int(d[ax])
    return (-1j if sg > 0 else 1j) * SIG[ax]

def ring_sites(x0, y0, w, h):
    """clockwise rectangular ring of w x h plaquettes with lower-left corner (x0,y0); z=0"""
    pts = []
    for i in range(w): pts.append((x0+i, y0, 0))
    for j in range(h): pts.append((x0+w, y0+j, 0))
    for i in range(w): pts.append((x0+w-i, y0+h, 0))
    for j in range(h): pts.append((x0, y0+h-j, 0))
    return pts

def rank(p):      # row-major order key
    return (p[2], p[1], p[0])

def loop_operator(ring, fermion):
    m = len(ring); half = m // 2
    posA, posB = 0, half            # ring indices
    X = np.eye(4, dtype=complex)
    flips = 0
    for step in range(half):
        for who in ('A', 'B'):
            if who == 'A':
                u, v = ring[posA], ring[(posA+1) % m]; other = ring[posB]
            else:
                u, v = ring[posB], ring[(posB+1) % m]; other = ring[posA]
            M = hop_block(u, v)
            # slot of the moving record before the hop: first slot iff rank(u) < rank(other)
            first_before = rank(u) < rank(other)
            first_after = rank(v) < rank(other)
            Mfull = np.kron(M, I2) if first_before else np.kron(I2, M)
            blk = Mfull
            if first_before != first_after:
                blk = SWAP @ Mfull
                flips += 1
                if fermion: blk = -blk
            X = blk @ X
            if who == 'A': posA = (posA+1) % m
            else: posB = (posB+1) % m
    assert ring[posA] == ring[half] and ring[posB] == ring[0]
    return X, flips

def spec(X):
    ev = np.linalg.eigvals(X)
    return sorted(np.round(ev, 6), key=lambda z: (round(z.real,4), round(z.imag,4)))

print("plaquette holonomy of the one-body walker (x, y, -x, -y):")
P = hop_block((0,0,0),(1,0,0)); Q = hop_block((1,0,0),(1,1,0)); R = hop_block((1,1,0),(0,1,0)); S = hop_block((0,1,0),(0,0,0))
print(np.round(S@R@Q@P, 6).tolist(), " -> scalar -1 (pi flux)")
for (w, h) in [(2,2),(3,2),(3,3),(4,2),(4,3),(4,4),(5,2),(5,3),(6,4)]:
    ring = ring_sites(1, 1, w, h)          # needs an even ring length for antipodal start
    if len(ring) % 2: continue
    Xp, fp = loop_operator(ring, False)
    Xm, fm = loop_operator(ring, True)
    A = w*h
    tr = np.trace(Xp)
    sq = np.allclose(Xp @ Xp, np.eye(4))
    same = np.allclose(Xm, -Xp)
    sp, sm = spec(Xp), spec(Xm)
    conj = np.allclose(sorted([complex(z) for z in np.linalg.eigvals(Xp)], key=lambda z:(z.real,z.imag)),
                       sorted([complex(z) for z in np.linalg.eigvals(Xm)], key=lambda z:(z.real,z.imag)), atol=1e-6)
    print(f"ring {w}x{h} area A={A} len={len(ring)} order-flips={fp}: X+^2=1? {sq}  tr X+ = {np.round(tr,6)} (pred {2*(-1)**A})  "
          f"X- = -X+? {same}  spec X+ = {[complex(z) for z in sp]}  spec X- = {[complex(z) for z in sm]}  conjugate-equivalent? {conj}")
