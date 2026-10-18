"""C7 shared code: oriented flux bookkeeping and Bloch Hamiltonians on the corner graph.

Geometry is imported from C6 (c6_corner_graph.py, written independently of the repo runners).
New here: faces are traversed with orientation, so that complex (in particular purely
imaginary, Majorana-type) hopping amplitudes can be assigned gauge-invariant fluxes.

Convention ('standard', as in C6): the one-particle matrix is h, with h[J, I] = amp_e for the
stored edge e = (I -> J) and h[I, J] = conj(amp_e); tau := -h; the flux of an oriented cycle
p_0 -> p_1 -> ... -> p_0 is arg prod_k tau[p_{k+1}, p_k].  All-negative real hops = flux 0.

Majorana / Kitaev convention: H = sum_e J_e u_e (i c_I c_J) with u_e = +-1 for the stored
orientation.  Then H = (1/2) sum_jk c_j h_jk c_k ... with the one-particle matrix
h[I, J] = 2 i J u (we drop the overall factor 2: h[J, I] = -i J u_e, h[I, J] = +i J u_e),
and E0 = (1/2) * sum of the negative eigenvalues of (2 h_used) = sum of negative eigenvalues of
h_used.  So 'Majorana half filling' is the half-filled (nu = 6) complex hopping problem with
purely imaginary amplitudes amp_e = -i J u_e; its triangle fluxes are +-pi/2, its 4-cycle
fluxes 0 or pi.
"""
import itertools, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
C6 = os.path.join(os.path.dirname(HERE), 'C6_rung0_to_rung1')
sys.path.insert(0, C6)
from c6_corner_graph import CornerGraph, gf2_solve, neg, CORNERS, DIRS  # noqa: E402

TYPES = ('square', 'triangle', 'plaquette', 'tube')


class Lattice:
    def __init__(self, L):
        self.G = G = CornerGraph(L)
        self.L = L
        self.n = G.nV
        self.nE = G.nE
        self.I = np.array([e[0] for e in G.edges])
        self.J = np.array([e[1] for e in G.edges])
        self.onsite = np.array([e[2] == 'onsite' for e in G.edges])
        self.W = np.array([e[3] for e in G.edges], float)
        # oriented traversals of every face: list of (type, [(edge, sigma)], det-sign for triangles)
        self.faces = []
        for k in TYPES:
            for seq in G.face_seq[k]:
                trav = self._traverse(seq)
                chi = 1
                if k == 'triangle':
                    # seq = [(x,y),(y,z),(z,x)] with x = s0 e1 ...: orientation is outward iff s0 s1 s2 = +1
                    c0 = seq[0][1]; c1 = seq[1][1]
                    x, y = sorted(c0, key=lambda d: [abs(t) for t in d].index(1))
                    z = [d for d in c1 if d != y][0]
                    chi = int(round(np.linalg.det(np.array([x, y, z]))))
                self.faces.append((k, trav, chi))
        self.ftype = np.array([TYPES.index(k) for k, _, _ in self.faces])

    def _traverse(self, seq):
        G = self.G
        out = []
        for (p1, c1), (p2, c2) in zip(seq, seq[1:] + seq[:1]):
            v1 = tuple(x % self.L for x in p1)
            disp = tuple(y - x for x, y in zip(p1, p2))
            w, wind = G._wrap(v1, disp)
            i, j = G.vid[(v1, c1)], G.vid[(w, c2)]
            e = G.ekey[(i, j, wind)]
            I, J, _, We = G.edges[e]
            sig = +1 if (I == i and J == j and tuple(We) == tuple(wind)) else -1
            if sig == -1:
                assert I == j and J == i and tuple(We) == tuple(-x for x in wind)
            out.append((e, sig))
        return out

    # --------------------------------------------------------------- fluxes
    def face_phases(self, amp):
        """gauge-invariant flux (radians, in (-pi, pi]) of every face, standard convention."""
        out = np.empty(len(self.faces))
        for f, (_, trav, _) in enumerate(self.faces):
            p = 1.0 + 0j
            for e, s in trav:
                p *= -(amp[e] if s == 1 else np.conj(amp[e]))
            out[f] = np.angle(p)
        return out

    def solve_u(self, base, target, rng=None):
        """find u in {0,1}^E (u_e = (-1)^bit) with face_phases(base * (-1)^u) == target (mod 2pi).
        Returns None when some face cannot reach its target with a Z2 gauge field or the system
        is inconsistent.  With rng, a random pure-gauge transformation is applied afterwards."""
        ph0 = self.face_phases(base)
        d = np.mod(np.asarray(target) - ph0 + 1e-9, 2 * np.pi) - 1e-9
        bitsv = np.round(d / np.pi).astype(int)
        if np.max(np.abs(d - np.pi * bitsv)) > 1e-6:
            return None
        rows = [[e for e, _ in trav] for _, trav, _ in self.faces]
        u = gf2_solve(rows, list(bitsv % 2), self.nE)
        if u is None:
            return None
        if rng is not None:
            g = rng.integers(0, 2, self.n)
            u = (u + g[self.I] + g[self.J]) % 2
        return u.astype(np.uint8)

    # --------------------------------------------------------------- Bloch / real-space
    def blochH(self, amp, Ks):
        n = self.n
        ph = np.exp(1j * Ks @ self.W.T)
        H = np.zeros((len(Ks), n, n), complex)
        A = amp[None, :] * ph
        np.add.at(H, (slice(None), self.J, self.I), A)
        np.add.at(H, (slice(None), self.I, self.J), np.conj(A))
        return H

    def kgrid(self, nk, shift=0.0):
        g = 2 * np.pi * (np.arange(nk) + shift) / nk
        return np.array(list(itertools.product(g, repeat=3)))

    def spectrum(self, amp, nk, shift=0.0):
        return np.sort(np.linalg.eigvalsh(self.blochH(amp, self.kgrid(nk, shift))).ravel())


def per_site(ev, nu):
    """ground energy per fine site with nu fermions per site (12 bands per site)."""
    nsites = len(ev) / 12.0
    return float(ev[:int(round(nu * nsites))].sum() / nsites)


def majorana_amp(lat, u, t1, t2):
    """purely imaginary amplitudes of the Kitaev-type Majorana hopping: amp_e = -i J_e u_e."""
    J = np.where(lat.onsite, t1, t2)
    return -1j * J * (-1.0) ** u


def real_amp(lat, u, t1, t2):
    """the C6 / corner-model real hopping in the standard convention: amp_e = -|t| u_e."""
    J = np.where(lat.onsite, t1, t2)
    return -J * (-1.0) ** u.astype(float)


def uniform_targets(lat, sq, tri, pl, tu, model):
    """target face phases for a uniform pattern.
    model 'real': 4 bits, 1 = pi.  model 'maj': tri in {'c+','c-','s+','s-'}:
    chiral (outward flux +-pi/2 on all 8 octants) or staggered (outward flux alternating with
    the octant parity s0 s1 s2)."""
    tg = np.zeros(len(lat.faces))
    for f, (k, _, chi) in enumerate(lat.faces):
        if k == 'square':
            tg[f] = np.pi * sq
        elif k == 'plaquette':
            tg[f] = np.pi * pl
        elif k == 'tube':
            tg[f] = np.pi * tu
        else:
            if model == 'real':
                tg[f] = np.pi * tri
            else:
                sgn = 1 if tri[1] == '+' else -1
                # seq orientation is outward iff chi = +1
                outward = sgn * np.pi / 2 if tri[0] == 'c' else sgn * chi * np.pi / 2
                tg[f] = outward * chi
    return tg


def flux_summary(lat, amp):
    ph = lat.face_phases(amp)
    out = {}
    for t, k in enumerate(TYPES):
        sel = ph[lat.ftype == t]
        if k == 'triangle':
            chis = np.array([chi for kk, _, chi in lat.faces if kk == 'triangle'])
            outw = sel * chis
            out[k] = (f"outward mean {np.mean(outw)/np.pi:+.3f}pi, "
                      f"frac(+pi/2) {np.mean(np.isclose(np.mod(outw, 2*np.pi), np.pi/2)):.2f}, "
                      f"frac(|phi|=pi/2) {np.mean(np.isclose(np.abs(sel), np.pi/2)):.2f}")
        else:
            out[k] = f"frac(pi) {np.mean(np.isclose(np.abs(sel), np.pi)):.3f}"
    return out
