"""Item 3: fermion-level PSG, 2O lift of the 12-corner site representation, cluster spectrum (own code)."""
import sys, itertools
import numpy as np
from geom import Lattice, CTYPES, DIRS, rotations, classify, w1, rot_vec, perp, add, neg
from ccode import CornerCode

L = 4
C = CornerCode(L)  # reuse only the graph/face lists (corner ids, edges, faces)
lat = C.lat
nc = lat.ncorner
edges = C.edges
eid = {e: i for i, e in enumerate(edges)}
faces = C.faces()
Ms = rotations()
idx = {tuple(M.flatten()): i for i, M in enumerate(Ms)}
mul = [[idx[tuple((Ms[a] @ Ms[b]).flatten())] for b in range(24)] for a in range(24)]


def gf2_solve(rows, rhs, nvar):
    """rows: list of int masks; returns one solution int or None."""
    piv = {}
    for v, r in zip(rows, rhs):
        while v:
            hb = v.bit_length() - 1
            if hb in piv:
                pv, pr = piv[hb]
                v ^= pv
                r ^= pr
            else:
                piv[hb] = (v, r)
                break
        if v == 0 and r:
            return None
    sol = 0
    for hb in sorted(piv):
        v, r = piv[hb]
        val = r ^ (bin((v ^ (1 << hb)) & sol).count('1') & 1)
        if val:
            sol |= 1 << hb
    return sol


def gauge_field(flux):
    rows, rhs = [], []
    for (t, cyc) in faces:
        m = 0
        for i in range(len(cyc)):
            m ^= 1 << eid[frozenset([cyc[i], cyc[(i + 1) % len(cyc)]])]
        rows.append(m)
        rhs.append(0 if flux[t] == 1 else 1)
    sol = gf2_solve(rows, rhs, len(edges))
    if sol is None:
        return None
    return np.array([-1 if (sol >> i) & 1 else 1 for i in range(len(edges))])


def corner_map(f):
    return [f(c) for c in range(nc)]


def psg_gauge(u, cmap):
    """find g with g(Rj) g(Rk) = u(Rj,Rk) u(j,k) ; vertex variables indexed by image corner."""
    rows, rhs = [], []
    for i, e in enumerate(edges):
        j, k = tuple(e)
        a, b = cmap[j], cmap[k]
        rows.append((1 << a) | (1 << b))
        s = u[eid[frozenset([a, b])]] * u[i]
        rhs.append(0 if s == 1 else 1)
    sol = gf2_solve(rows, rhs, nc)
    if sol is None:
        return None
    return np.array([-1 if (sol >> i) & 1 else 1 for i in range(nc)])


class SPOp:
    """single-particle operator |j> -> g[cmap j] |cmap j>  (as sparse signed permutation)."""

    def __init__(self, cmap, g):
        self.cmap = list(cmap)
        self.g = np.array(g, dtype=complex)

    def mul(self, other):
        # (A B)|j> = A (g_B[mB j] |mB j>) = g_B[mB j] g_A[mA mB j] |mA mB j>
        cm = [self.cmap[other.cmap[j]] for j in range(nc)]
        g = np.zeros(nc, dtype=complex)
        for j in range(nc):
            g[cm[j]] = other.g[other.cmap[j]] * self.g[cm[j]]
        return SPOp(cm, g)

    def scalar_ratio(self, other):
        assert self.cmap == other.cmap
        r = self.g / other.g
        assert np.allclose(r, r[0])
        return r[0]


def run_psg(flux, verbose=False):
    u = gauge_field(flux)
    if u is None:
        return None
    Gs = []
    for M in Ms:
        cmap = corner_map(lambda c: C.rot_corner(M, c))
        g = psg_gauge(u, cmap)
        if g is None:
            return ('no PSG for', classify(M))
        Gs.append(SPOp(cmap, g))
    # signs
    sq = {}
    for i, M in enumerate(Ms):
        t = classify(M)
        if t in ('C2axis', 'C2edge'):
            s = Gs[i].mul(Gs[i]).scalar_ratio(SPOp(range(nc), np.ones(nc)))
            sq.setdefault(t, set()).add(round(s.real))
        if t == 'C4':
            P = Gs[i].mul(Gs[i]).mul(Gs[i]).mul(Gs[i])
            s = P.scalar_ratio(SPOp(range(nc), np.ones(nc)))
            sq.setdefault('C4^4', set()).add(round(s.real))
    # translations
    Ts = []
    for a in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        def tm(c, a=a):
            v, ct = lat.corner_info(c)
            return lat.corner(add(v, a), ct)
        cmap = corner_map(tm)
        g = psg_gauge(u, cmap)
        if g is None:
            return ('no translation PSG',)
        Ts.append(SPOp(cmap, g))
    comm = []
    for a, b in [(0, 1), (0, 2), (1, 2)]:
        comm.append(round(Ts[a].mul(Ts[b]).scalar_ratio(Ts[b].mul(Ts[a])).real))
    return u, Gs, sq, comm


# ---------- 2O ----------
def quat_of_rot(M):
    """unit quaternion (w,x,y,z) for rotation matrix M (one of the two)."""
    M = np.array(M, dtype=float)
    tr = np.trace(M)
    w = np.sqrt(max(0, 1 + tr)) / 2
    x = np.sqrt(max(0, 1 + M[0, 0] - M[1, 1] - M[2, 2])) / 2
    y = np.sqrt(max(0, 1 - M[0, 0] + M[1, 1] - M[2, 2])) / 2
    z = np.sqrt(max(0, 1 - M[0, 0] - M[1, 1] + M[2, 2])) / 2
    # fix signs
    if w > 1e-9:
        x = np.copysign(x, M[2, 1] - M[1, 2]); y = np.copysign(y, M[0, 2] - M[2, 0]); z = np.copysign(z, M[1, 0] - M[0, 1])
    elif x > 1e-9:
        y = np.copysign(y, M[0, 1] + M[1, 0]); z = np.copysign(z, M[0, 2] + M[2, 0])
    elif y > 1e-9:
        z = np.copysign(z, M[1, 2] + M[2, 1])
    return np.array([w, x, y, z])


def qmul(a, b):
    w1_, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return np.array([w1_ * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1_ * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1_ * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1_ * z2 + x1 * y2 - y1 * x2 + z1 * w2])


def rot_of_quat(q):
    w, x, y, z = q
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


def chi_j(q, j):
    """SU(2) spin-j character for quaternion q: rotation angle th with cos(th/2) = w."""
    w = np.clip(q[0], -1, 1)
    half = np.arccos(w)  # th/2
    if abs(np.sin(half)) < 1e-9:
        return (2 * j + 1) * (1 if w > 0 else (-1) ** int(round(2 * j)))
    return np.sin((2 * j + 1) * half) / np.sin(half)


def main():
    default = {'square': -1, 'triangle': 1, 'plaquette': -1, 'tube': 1}
    # 16 uniform flux patterns
    print('flux pattern (sq,tri,pl,tube) -> PSG signs, translation commutators')
    for fl in itertools.product([1, -1], repeat=4):
        flux = dict(zip(['square', 'triangle', 'plaquette', 'tube'], fl))
        r = run_psg(flux)
        if r is None:
            print(fl, 'INCONSISTENT flux')
            continue
        if isinstance(r, tuple) and isinstance(r[0], str):
            print(fl, r)
            continue
        u, Gs, sq, comm = r
        print(fl, {k: sorted(v) for k, v in sq.items()}, 'T comm', comm)
    u, Gs, sq, comm = run_psg(default)
    # group law signs eps(a,b): G_a G_b = eps G_ab
    eps = np.zeros((24, 24))
    for a in range(24):
        for b in range(24):
            eps[a, b] = Gs[a].mul(Gs[b]).scalar_ratio(Gs[mul[a][b]]).real
    # site rep on origin corners
    site = [lat.corner((0, 0, 0), ct) for ct in CTYPES]
    spos = {c: i for i, c in enumerate(site)}
    def site_mat(G, twist):
        Mx = np.zeros((12, 12), dtype=complex)
        for c in site:
            Mx[spos[G.cmap[c]], spos[c]] = G.g[G.cmap[c]]
        return Mx * twist
    qs = [quat_of_rot(M) for M in Ms]
    for i, M in enumerate(Ms):
        assert np.allclose(rot_of_quat(qs[i]), M)
    # omega(a,b): s(a)s(b) = omega s(ab)
    om = np.zeros((24, 24))
    for a in range(24):
        for b in range(24):
            p = qmul(qs[a], qs[b])
            om[a, b] = 1 if np.allclose(p, qs[mul[a][b]]) else (-1 if np.allclose(p, -qs[mul[a][b]]) else 0)
    assert np.all(om != 0)
    for twist_name, tw in [('none', lambda M: 1), ('i^w1', lambda M: 1j ** w1(M)), ('(-i)^w1', lambda M: (-1j) ** w1(M))]:
        mats = [site_mat(Gs[i], tw(Ms[i])) for i in range(24)]
        e2 = np.zeros((24, 24), dtype=complex)
        for a in range(24):
            for b in range(24):
                X = mats[a] @ mats[b]
                Y = mats[mul[a][b]]
                k = np.argmax(np.abs(Y).sum(axis=0))
                ratio = (X[:, k] @ Y[:, k].conj()) / (Y[:, k] @ Y[:, k].conj())
                assert np.allclose(X, ratio * Y)
                e2[a, b] = ratio
        # need signs sigma: e2(a,b) sigma(a) sigma(b) sigma(ab) = omega(a,b)  (all real +-1?)
        real = np.allclose(e2.imag, 0)
        if not real:
            print('twist', twist_name, ': cocycle not real -> no sign fix to 2O; values', set(np.round(e2.flatten(), 6)))
            continue
        rows, rhs = [], []
        for a in range(24):
            for b in range(24):
                rows.append((1 << a) ^ (1 << b) ^ (1 << mul[a][b]))
                val = e2[a, b].real * om[a, b]
                rhs.append(0 if val > 0 else 1)
        sol = gf2_solve(rows, rhs, 24)
        if sol is None:
            print('twist', twist_name, ': not a linear rep of 2O (cocycle != SU(2) cocycle)')
            # check if it is linear rep of O
            rhs2 = [0 if e2[a, b].real > 0 else 1 for a in range(24) for b in range(24)]
            print('   linear rep of O after signs?', gf2_solve(rows, rhs2, 24) is not None)
            continue
        sig = [(-1 if (sol >> i) & 1 else 1) for i in range(24)]
        # characters on 2O: element +q_a -> sig_a * mats[a], -q_a -> -sig_a mats[a]
        chars = []
        for a in range(24):
            chars.append((qs[a], sig[a] * np.trace(mats[a])))
            chars.append((-qs[a], -sig[a] * np.trace(mats[a])))
        def mult(irr):
            return sum(np.conj(irr(q)) * ch for q, ch in chars) / 48
        sgn = {}
        for a in range(24):
            sgn[a] = (-1) ** w1(Ms[a])
        A2 = lambda q: (-1) ** w1(Ms[min(range(24), key=lambda a: min(np.abs(qs[a] - q).sum(), np.abs(qs[a] + q).sum()))])
        irreps = {'E1/2': lambda q: chi_j(q, 0.5), 'E5/2': lambda q: chi_j(q, 0.5) * A2(q),
                  'G3/2': lambda q: chi_j(q, 1.5),
                  'A1': lambda q: 1, 'A2': A2, 'E': lambda q: chi_j(q, 1) - 1 + 0 * A2(q),
                  }
        res = {k: np.round(mult(f), 6) for k, f in irreps.items()}
        print('twist', twist_name, ': linear 2O rep; multiplicities', res)
    print('default flux PSG signs:', {k: sorted(v) for k, v in sq.items()}, 'translation commutators', comm)
    # ---------- cluster Hamiltonian ----------
    on_edges = [e for e in edges if C.ekind[e] == 'onsite' and all(c in spos for c in e)]
    tri = [cyc for (t, cyc) in faces if t == 'triangle' and all(c in spos for c in cyc)]
    assert len(on_edges) == 24 and len(tri) == 8
    # orientation sigma_jk from outward-oriented triangles
    sigma = {}
    for cyc in tri:
        pos = [np.array(lat.corner_pos4((0, 0, 0), lat.corner_info(c)[1])) for c in cyc]
        nrm = np.cross(pos[1] - pos[0], pos[2] - pos[1])
        cen = sum(pos)
        cyc2 = cyc if nrm @ cen > 0 else cyc[::-1]
        for i in range(3):
            j, k = cyc2[i], cyc2[(i + 1) % 3]
            sigma[(j, k)] = 1
            sigma[(k, j)] = -1
    assert len(sigma) == 48
    def Hsite(t1, lam):
        H = np.zeros((12, 12), dtype=complex)
        for e in on_edges:
            j, k = tuple(e)
            uu = u[eid[e]]
            H[spos[j], spos[k]] = (t1 + 1j * lam * sigma[(j, k)]) * uu
            H[spos[k], spos[j]] = np.conj(H[spos[j], spos[k]])
        return H
    # projectors onto irreps using sigma-fixed twisted lift (i^w1)
    tw = lambda M: 1j ** w1(M)
    mats = [site_mat(Gs[i], tw(Ms[i])) for i in range(24)]
    # recompute sigma for this twist
    e2 = np.array([[np.trace(np.linalg.inv(mats[mul[a][b]]) @ mats[a] @ mats[b]) / 12 for b in range(24)] for a in range(24)])
    rows, rhs = [], []
    for a in range(24):
        for b in range(24):
            rows.append((1 << a) ^ (1 << b) ^ (1 << mul[a][b]))
            rhs.append(0 if e2[a, b].real * om[a, b] > 0 else 1)
    sol = gf2_solve(rows, rhs, 24)
    sig = [(-1 if (sol >> i) & 1 else 1) for i in range(24)]
    A2v = [(-1) ** w1(M) for M in Ms]
    def proj(irr):
        dim = {'E1/2': 2, 'E5/2': 2, 'G3/2': 4}[irr]
        P = np.zeros((12, 12), dtype=complex)
        for a in range(24):
            for s in (1, -1):
                q = s * qs[a]
                Mx = s * sig[a] * mats[a]
                ch = {'E1/2': chi_j(q, .5), 'E5/2': chi_j(q, .5) * A2v[a], 'G3/2': chi_j(q, 1.5)}[irr]
                P += np.conj(ch) * Mx
        return P * dim / 48
    Ps = {k: proj(k) for k in ['E1/2', 'E5/2', 'G3/2']}
    print('projector ranks', {k: round(np.trace(P).real) for k, P in Ps.items()})
    for t1, lam in [(-1, 0), (1, 0), (-1, -0.5), (-1, 0.5), (1, -0.5), (1, 0.5)]:
        H = Hsite(t1, lam)
        assert np.allclose(H, H.conj().T)
        inv = max(np.abs(Mx @ H - H @ Mx).max() for Mx in mats)
        w, V = np.linalg.eigh(H)
        lv = []
        i = 0
        while i < 12:
            j = i
            while j < 12 and abs(w[j] - w[i]) < 1e-8:
                j += 1
            sub = V[:, i:j]
            lab = {k: round(np.trace(sub.conj().T @ P @ sub).real / {'E1/2': 2, 'E5/2': 2, 'G3/2': 4}[k], 3) for k, P in Ps.items()}
            lab = {k: v for k, v in lab.items() if v > 1e-6}
            lv.append((round(w[i], 4), j - i, lab))
            i = j
        print(f't1={t1} chiral={lam} O-inv err {inv:.1e}; levels:', lv[:3], ' gap', round(lv[1][0] - lv[0][0], 4))


if __name__ == '__main__':
    main()
