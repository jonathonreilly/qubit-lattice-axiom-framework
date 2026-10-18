#!/usr/bin/env python3
"""C6 runner: registration lemma controls, dimension/density facts, and the freedom of the corner flux.

Companion note:
  docs/NO_EQUIVARIANT_FACTOR_OF_IID_NOISE_REGISTERS_A_COARSE_BLOCK_LATTICE_AND_THE_CORNER_FLUX_IS_A_FREE_SECTOR_LABEL_OF_ITS_LOCAL_FERMIONIZATION_BOUNDED_THEOREM_NOTE_2026-10-18.md

The registration lemma (note section 2) is proved analytically; nothing here proves it.  This runner
consolidates the campaign's exact finite certificates and illustrations:

  R. Registration-lemma illustrations and controls (finite Monte Carlo / exact finite statevector):
     R1 an iid-priority formation packing (range 4, empty start, covariant rule) has superlattice
        amplitudes at the 1/sqrt(N_c) noise level; R2 a coding-radius-2 equivariant factor of iid noise
        has sqrt(N_c) max_Q |S(Q)| = O(1) from L = 20 to 80 and balanced coset frequencies; R3 the two
        trivial controls (periodic planted start; position-dependent rule) register perfectly;
        R4 quantum analogue: a translation-invariant finite-depth circuit on a translation-invariant
        product state has uniform one-point functions and exactly vanishing connected correlations
        outside the light cone (1D ring, exact statevector).
  D. Dimension/density facts (exact): even algebra of n modes is M + M (n = 1..4), so a faithful
     representation needs n qubits; O-invariant sublattices of Z^3 of index <= 32 by Hermite-normal-form
     enumeration (smallest index >= 12 is 16); block arithmetic.
  A. Flux sector freedom (exact, GF(2) and Pauli algebra):
     A1 corner-graph cycle space, face relations and the 16 uniform patterns on L = 3, 4 (6 with --full);
     A2 BKSF Pauli algebra on L = 3: the formal bare-sector flux kappa depends on conventions; the identity
        prod_r kappa = sigma_r, so in any fixed convention the sectors are exactly the consistent F; in the
        three generic conventions tested the all-bare-+1 assignment is inconsistent, but a translation-
        invariant vertex ordering found by local search makes it consistent, and hop-sign flips of that
        convention make uniform 1011, 1111 and 0000 each the bare sector (which consistent F is 'bare'
        is set by the dictionary); A3 one sign flip flips kappa exactly on the faces through that edge;
     A4 fermion-level PSG (BFS sign propagation) on L = 4 for all 16 uniform patterns; design targets
        select {1011, 1111}; the gauge-invariant standard-convention statement (pi through every face
        at t1 = -1, lambda = 0) and the chiral-term phase of every face, pi + arctan(lambda) * sum_e sigma_e over on-site edges.
  E. (--energetics) nu = 1 free-fermion energetics of the 16 uniform sectors on a 2^3 Bloch supercell
     (6^3 K-grid), with the Bloch / real-space cross-check, the diamagnetic inequality and the
     particle-hole identity.  Numerical.

Usage: python3 scripts/equivariant_iid_factor_registration_lemma_and_corner_flux_sector_freedom_2026_10_18.py
         [--energetics] [--full] [--seed N]
"""
import argparse, itertools, math, sys, time
import numpy as np

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  :: {detail}" if detail else ''), flush=True)


T0 = time.time()
def el():
    return f"t={time.time() - T0:.0f}s"


# =====================================================================================================
# corner-graph geometry (vertices = the 12 perpendicular direction pairs at each site; on-site edges =
# cuboctahedron edges; link edges {a,b}@v -- {-a,b}@v+a; faces = squares, triangles, plaquettes, tubes)
# =====================================================================================================
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
TYPES = ('square', 'triangle', 'plaquette', 'tube')


def neg(d):
    return tuple(-x for x in d)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def perp(d, e):
    return dot(d, e) == 0 and d != e


CORNERS = [frozenset((d, e)) for d, e in itertools.combinations(DIRS, 2) if dot(d, e) == 0]
assert len(CORNERS) == 12


class CornerGraph:
    def __init__(self, L):
        self.L = L
        self.sites = list(itertools.product(range(L), repeat=3))
        self.verts = [(v, c) for v in self.sites for c in CORNERS]
        self.vid = {q: i for i, q in enumerate(self.verts)}
        self.nV = len(self.verts)
        self.edges = []; self.edesc = []; self.ekey = {}
        for v in self.sites:
            for c in CORNERS:
                d, e = tuple(c)
                for a, b in ((d, e), (e, d)):
                    for f in DIRS:
                        if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                            self._add((v, c), frozenset((a, f)), (0, 0, 0), 'onsite')
                    self._add((v, c), frozenset((neg(a), b)), a, 'link')
        self.nE = len(self.edges)
        deg = np.zeros(self.nV, int)
        for i, j, _, _ in self.edges:
            deg[i] += 1; deg[j] += 1
        assert set(deg.tolist()) == {6}
        self._faces()

    def _wrap(self, v, disp):
        raw = tuple(x + y for x, y in zip(v, disp))
        w = tuple(x % self.L for x in raw)
        return w, tuple((r - x) // self.L for r, x in zip(raw, w))

    def _add(self, q, c2, disp, kind):
        v, c = q
        w, wind = self._wrap(v, disp)
        i, j = self.vid[q], self.vid[(w, c2)]
        if (i, j, wind) in self.ekey:
            return
        k = len(self.edges)
        self.edges.append((i, j, kind, wind)); self.edesc.append((v, c, tuple(disp), c2))
        self.ekey[(i, j, wind)] = k; self.ekey[(j, i, tuple(-x for x in wind))] = k

    def edge_between(self, q, disp, c2):
        v, c = q
        w, wind = self._wrap(v, disp)
        return self.ekey[(self.vid[q], self.vid[(w, c2)], wind)]

    def _cycle(self, seq):
        out = []
        for (p1, c1), (p2, c2) in zip(seq, seq[1:] + seq[:1]):
            v1 = tuple(x % self.L for x in p1)
            out.append(self.edge_between((v1, c1), tuple(y - x for x, y in zip(p1, p2)), c2))
        return out

    def _faces(self):
        F = {k: [] for k in TYPES}; S = {k: [] for k in TYPES}
        for v in self.sites:
            for d in DIRS:
                a = [f for f in DIRS if perp(f, d) and f != neg(d)]
                a0 = a[0]; b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]
                ring = [a0, b0, neg(a0), neg(b0)]
                seq = [(v, frozenset((d, r))) for r in ring]
                F['square'].append(self._cycle(seq)); S['square'].append(seq)
                for i in range(4):
                    p, q = ring[i], ring[(i + 1) % 4]
                    w = tuple(x + y for x, y in zip(v, d))
                    seq = [(v, frozenset((d, p))), (w, frozenset((neg(d), p))),
                           (w, frozenset((neg(d), q))), (v, frozenset((d, q)))]
                    F['tube'].append(self._cycle(seq)); S['tube'].append(seq)
            for s in itertools.product((1, -1), repeat=3):
                x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
                seq = [(v, frozenset((x, y))), (v, frozenset((y, z))), (v, frozenset((z, x)))]
                F['triangle'].append(self._cycle(seq)); S['triangle'].append(seq)
            for d, e in (((1, 0, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0))):
                vd = tuple(x + y for x, y in zip(v, d)); ve = tuple(x + y for x, y in zip(v, e))
                vde = tuple(x + y for x, y in zip(vd, e))
                seq = [(v, frozenset((d, e))), (vd, frozenset((neg(d), e))),
                       (vde, frozenset((neg(d), neg(e)))), (ve, frozenset((d, neg(e))))]
                F['plaquette'].append(self._cycle(seq)); S['plaquette'].append(seq)
        self.faces = {}; self.face_seq = {}
        for k in TYPES:                       # each tube is generated twice (from v along d, from v+d along -d)
            seen = set(); fl = []; sl = []
            for f, s in zip(F[k], S[k]):
                key = frozenset(f)
                if key in seen:
                    continue
                seen.add(key); fl.append(f); sl.append(s)
            self.faces[k] = fl; self.face_seq[k] = sl

    def face_list(self):
        return [(k, f) for k in TYPES for f in self.faces[k]]


def bits(idx):
    x = 0
    for j in idx:
        x ^= (1 << j)
    return x


def gf2_rank(rows):
    piv = {}
    for x in rows:
        while x:
            c = x.bit_length() - 1
            if c in piv:
                x ^= piv[c]
            else:
                piv[c] = x; break
    return len(piv)


def gf2_solve(rows, rhs, n):
    """solve sum_{j in row} x_j = rhs over GF(2); rows are index lists; None if inconsistent."""
    piv = {}
    for r, b in zip(rows, rhs):
        x = bits(r) ^ ((1 << n) if b else 0)
        while True:
            low = x & ((1 << n) - 1)
            if low == 0:
                if x:
                    return None
                break
            c = low.bit_length() - 1
            if c in piv:
                x ^= piv[c]
            else:
                piv[c] = x; break
    sol = 0
    for c in sorted(piv):
        x = piv[c]
        if ((x >> n) & 1) ^ (bin(x & ((1 << c) - 1) & sol).count('1') & 1):
            sol |= (1 << c)
    return np.array([(sol >> j) & 1 for j in range(n)], dtype=np.uint8)


def gauge_for(G, F):
    fl = G.face_list()
    return gf2_solve([f for _, f in fl], [F[TYPES.index(k)] for k, _ in fl], G.nE)


def face_fluxes(G, u):
    return [(k, int(sum(int(u[e]) for e in f) % 2)) for k, f in G.face_list()]


# =====================================================================================================
# R. registration-lemma illustrations and controls
# =====================================================================================================
def superlattice_amplitude(pts, m=5):
    Qs = np.array([2 * np.pi * np.array(q) / m for q in itertools.product(range(m), repeat=3) if any(q)])
    return float(np.abs(np.exp(1j * pts @ Qs.T).mean(0)).max())


def part_R(rng):
    print("\nR. registration lemma: illustrations and controls (the lemma itself is proved in the note)")
    # R1: iid-priority formation (B3 class): a site becomes a centre at its iid time iff no earlier-formed
    # centre lies within l_inf distance 4 (range-4 rule, empty start, translation covariant).
    L = 40
    offs = np.array(list(itertools.product(range(-4, 5), repeat=3)))
    amps = []; ns = []
    for trial in range(3):
        order = rng.permutation(L ** 3)
        cen = np.zeros((L, L, L), bool)
        for s in order:
            x = np.array((s // (L * L), (s // L) % L, s % L))
            nb = (x + offs) % L
            if not cen[nb[:, 0], nb[:, 1], nb[:, 2]].any():
                cen[tuple(x)] = True
        pts = np.argwhere(cen).astype(float)
        amps.append(superlattice_amplitude(pts)); ns.append(len(pts))
        print(f"  R1 trial {trial}: {len(pts)} centres (perfect 5Z^3 lattice: {L**3 // 125}); max_Q |S(Q)| = {amps[-1]:.4f};"
              f" 1/sqrt(N_c) = {1/np.sqrt(len(pts)):.4f}")
    check("R1 iid-priority block packing (range 4, empty start, covariant): no superlattice peak, max |S(Q)| < 4/sqrt(N_c) in each trial"
          " (a registered 5Z^3 lattice gives 1)", all(a < 4 / np.sqrt(n) for a, n in zip(amps, ns)),
          f"max amplitude {max(amps):.3f}")
    # R2: a coding-radius-2 equivariant factor: x is a centre iff its uniform label is the strict max of
    # its l_inf radius-2 window.
    from scipy.ndimage import maximum_filter
    rows = []
    for L in (20, 40, 60, 80):
        vals = []
        for _ in range(3):
            x = rng.random((L, L, L))
            pts = np.argwhere(x == maximum_filter(x, size=5, mode='wrap')).astype(float)
            vals.append((len(pts), superlattice_amplitude(pts)))
        Nc = np.mean([v[0] for v in vals]); S = np.mean([v[1] for v in vals])
        rows.append((L, Nc, S, S * np.sqrt(Nc)))
        print(f"  R2 L={L}: N_c ~ {Nc:.0f}; mean max_Q |S(Q)| = {S:.4f}; sqrt(N_c) * that = {S*np.sqrt(Nc):.2f}")
    r = [x[3] for x in rows]
    check("R2 radius-2 equivariant factor of iid: sqrt(N_c) max_Q |S(Q)| stays in [1, 4] from L = 20 to 80 while |S| falls (no Bragg peak)",
          all(1 <= v <= 4 for v in r) and rows[-1][2] < rows[0][2] / 2.5, f"{[round(v, 2) for v in r]}")
    # coset balance (the step mu(A_c) = 1/m of the proof is translation invariance): chi-square over the
    # 125 cosets of 5Z^3, pooled over 10 samples at L = 40
    L = 40; cnt = np.zeros(125)
    for _ in range(10):
        x = rng.random((L, L, L))
        p = np.argwhere(x == maximum_filter(x, size=5, mode='wrap')) % 5
        np.add.at(cnt, p[:, 0] * 25 + p[:, 1] * 5 + p[:, 2], 1)
    exp_ = cnt.sum() / 125; chi2 = float(((cnt - exp_) ** 2 / exp_).sum())
    z = (chi2 - 124) / math.sqrt(2 * 124)
    check("R2 coset frequencies of centres mod 5Z^3 are balanced (chi-square over 124 dof within 4 sigma)", abs(z) < 4,
          f"chi2 = {chi2:.1f}, z = {z:+.2f}, {int(cnt.sum())} centres")
    # R3 controls: the hypotheses are load-bearing
    L = 40
    cen = np.zeros((L, L, L), bool); cen[::5, ::5, ::5] = True
    a = superlattice_amplitude(np.argwhere(cen).astype(float))
    check("R3 control (a): deterministic periodic start slice B = 5Z^3 (allowed by B3 Definition 1, not empty) registers: |S| = 1",
          abs(a - 1) < 1e-12)
    y = np.indices((L, L, L)).reshape(3, -1).T
    a = superlattice_amplitude(y[(y % 5 == 0).all(1)].astype(float))
    check("R3 control (b): position-dependent rule F_y (reads y mod 5; coding radius 0, not covariant) registers: |S| = 1",
          abs(a - 1) < 1e-12)
    # R4: quantum analogue (illustration, 1D ring, exact statevector)
    N = 12
    a1, b1 = 0.37, 0.61
    dim = 2 ** N
    idx = np.arange(dim)
    zb = np.array([1 - 2 * ((idx >> (N - 1 - q)) & 1) for q in range(N)], float)   # Z eigenvalue per qubit
    def layer_x(psi, a):
        c, s = math.cos(a), -1j * math.sin(a)
        for q in range(N):
            psi = psi.reshape(2 ** q, 2, 2 ** (N - q - 1))
            p0, p1 = psi[:, 0, :].copy(), psi[:, 1, :].copy()
            psi[:, 0, :] = c * p0 + s * p1; psi[:, 1, :] = s * p0 + c * p1
            psi = psi.reshape(dim)
        return psi
    def layer_zz(psi, b):
        ph = sum(zb[q] * zb[(q + 1) % N] for q in range(N))
        return psi * np.exp(-1j * b * ph)
    psi = np.zeros(dim, complex); psi[0] = 1.0                    # |0...0>, a TI product state
    for lay in ('x', 'zz', 'x', 'zz', 'x'):                       # TI layers; two ZZ layers: light-cone radius 2
        psi = layer_x(psi, a1) if lay == 'x' else layer_zz(psi, b1)
    pr = np.abs(psi) ** 2
    ez = np.array([pr @ zb[q] for q in range(N)])
    conn = [float(pr @ (zb[0] * zb[r]) - ez[0] * ez[r]) for r in range(N // 2 + 1)]
    print(f"  R4 ring N={N}, circuit X ZZ X ZZ X: <Z_x> = {ez[0]:.6f} (spread {np.ptp(ez):.1e}); connected <Z_0 Z_r>, r = 0..6:"
          f" {[f'{c:+.2e}' for c in conn]}")
    check("R4 TI finite-depth circuit on |0...0>: <Z_x> is the same at every site and connected <Z_0 Z_r> vanishes exactly"
          " for r > 4 (light cone), while it is nonzero for some r <= 4",
          np.ptp(ez) < 1e-12 and all(abs(c) < 1e-12 for c in conn[5:]) and max(abs(c) for c in conn[1:5]) > 1e-3)


# =====================================================================================================
# D. dimension / density facts
# =====================================================================================================
def majoranas(n):
    X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1.]).astype(complex)
    out = []
    for k in range(n):
        for P in (X, Y):
            m = np.array([[1.0 + 0j]])
            for o in [Z] * k + [P] + [np.eye(2)] * (n - k - 1):
                m = np.kron(m, o)
            out.append(m)
    return out


def hnf_sublattices(n):
    """all sublattices of Z^3 of index n as lower-triangular Hermite normal forms (rows = basis)."""
    out = []
    for a in range(1, n + 1):
        if n % a: continue
        for c in range(1, n // a + 1):
            if (n // a) % c: continue
            f = n // (a * c)
            for b in range(a):
                for d in range(a):
                    for e in range(c):
                        out.append(np.array([[a, 0, 0], [b, c, 0], [d, e, f]]))
    return out


def in_lattice(Bm, v):
    """is integer vector v in the row lattice of lower-triangular Bm (positive diagonal)?"""
    v = np.array(v, dtype=np.int64).copy()
    for i in (2, 1, 0):
        if v[i] % Bm[i, i]:
            return False
        v = v - (v[i] // Bm[i, i]) * Bm[i]
    return not v.any()


def part_D():
    print("\nD. dimension and density facts (exact)")
    ok = True
    for n in range(1, 5):
        g = majoranas(n)
        basis = []
        for S in itertools.chain.from_iterable(itertools.combinations(range(2 * n), r) for r in range(0, 2 * n + 1, 2)):
            m = np.eye(2 ** n, dtype=complex)
            for s in S:
                m = m @ g[s]
            basis.append(m)
        gens = [g[a] @ g[b] for a in range(2 * n) for b in range(a + 1, 2 * n)]
        C = np.vstack([np.array([(h @ b - b @ h).ravel() for b in basis]).T for h in gens])
        cdim = len(basis) - np.linalg.matrix_rank(C, tol=1e-9)
        # the even algebra acting on C^(2^n) splits by parity into two blocks of size 2^(n-1); both are needed
        P = np.diag([(-1) ** bin(i).count('1') for i in range(2 ** n)]).astype(complex)
        par_central = all(np.allclose(P @ b, b @ P) for b in basis)
        ok &= cdim == 2 and len(basis) == 2 * (2 ** (n - 1)) ** 2 and par_central
        print(f"  n={n}: even algebra dim {len(basis)} = 2*(2^{n-1})^2, centre dim {cdim} (spanned by 1 and the parity)")
    check("D1 even algebra of n complex modes is M_{2^(n-1)} + M_{2^(n-1)} (n = 1..4), so a faithful representation has"
          " dimension >= 2^n, i.e. needs n qubits; n = 12 for a corner site", ok)
    # O-invariant sublattices of Z^3 of index <= 32
    gens = [np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]), np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])]   # C4z, C3(111)
    found = {}
    nsub = 0
    for n in range(1, 33):
        for Bm in hnf_sublattices(n):
            nsub += 1
            if all(in_lattice(Bm, R @ Bm[i]) for R in gens for i in range(3)):
                found.setdefault(n, []).append(Bm)
    idxs = sorted(found)
    print(f"  enumerated {nsub} sublattices (HNF) of index <= 32; O-invariant indices: {idxs}"
          f" (counts {[len(found[n]) for n in idxs]})")
    def typ(Bm):
        # classify: P-type kZ^3, F-type k*D3 (index 2k^3), I-type k*BCC (index 4k^3)
        for k in range(1, 5):
            gensP = k * np.eye(3, dtype=int)
            gensF = k * np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
            gensI = k * np.array([[2, 0, 0], [0, 2, 0], [1, 1, 1]])
            for name, Gm in (('P', gensP), ('F', gensF), ('I', gensI)):
                if round(abs(np.linalg.det(Gm))) == round(abs(np.linalg.det(Bm))) and all(in_lattice(Bm, r) for r in Gm):
                    return f"{name}{k}"
        return '?'
    types = {n: [typ(b) for b in found[n]] for n in idxs}
    print(f"  types (P = kZ^3, F = k*FCC/D3, I = k*BCC): {types}")
    check("D2 the O-invariant sublattices of Z^3 of index <= 32 are exactly kZ^3, k*D3, k*BCC (indices k^3, 2k^3, 4k^3):"
          " {1, 2, 4, 8, 16, 27, 32}, one each", idxs == [1, 2, 4, 8, 16, 27, 32] and all(len(found[n]) == 1 for n in idxs)
          and '?' not in sum(types.values(), []))
    check("D3 smallest O-invariant index >= 12 is 16 (the 2*D3 sublattice); the long-wavelength note's registered blocks have index 125 = 48 + 77",
          min(n for n in idxs if n >= 12) == 16 and types[16] == ['F2'] and 48 + 77 == 125 == 5 ** 3)
    # integer (indeed real) 3x3 matrices M with M R = R M for the generators of O are scalar (Schur):
    # a linear O-equivariant placement x -> c + M x of the coarse cubic lattice has Lambda = kZ^3
    rows = []
    for R in gens:
        for i in range(3):
            for j in range(3):
                row = np.zeros(9)
                for k in range(3):
                    row[i * 3 + k] += R[k, j]      # (M R)_ij = sum_k M_ik R_kj
                    row[k * 3 + j] -= R[i, k]      # (R M)_ij = sum_k R_ik M_kj
                rows.append(row)
    A = np.array(rows)
    ns = 9 - np.linalg.matrix_rank(A)
    check("D4 the commutant of O in 3x3 matrices is the scalars (null space dim 1, spanned by I): an O-equivariant linear placement of the"
          " coarse cubic lattice has Lambda = kZ^3, so index k^3 >= 27 under the 12-qubit density bound",
          ns == 1 and np.allclose(A @ np.eye(3).ravel(), 0) and min(k ** 3 for k in range(1, 6) if k ** 3 >= 12) == 27)


# =====================================================================================================
# A. the corner flux is a free sector label
# =====================================================================================================
def straight_loop(G, axis):
    L = G.L
    a = DIRS[2 * axis]; b = DIRS[(2 * axis + 2) % 6]; c = DIRS[(2 * axis + 4) % 6]
    seq = []
    for n in range(L):
        v = tuple(n * x for x in a); w = tuple((n + 1) * x for x in a)
        seq += [(v, frozenset((a, b))), (w, frozenset((neg(a), b))), (w, frozenset((b, c)))]
    pts = seq + [(tuple(L * x for x in a), frozenset((a, b)))]
    es = []
    for (p1, c1), (p2, c2) in zip(pts[:-1], pts[1:]):
        es.append(G.edge_between((tuple(x % L for x in p1), c1), tuple(y - x for x, y in zip(p1, p2)), c2))
    return es


def part_A1(Ls, rng):
    print("\nA1. cycle space, face relations and the 16 uniform flux patterns (exact GF(2))")
    for L in Ls:
        G = CornerGraph(L); N = L ** 3
        fl = G.face_list()
        cyc = G.nE - G.nV + 1
        rk = gf2_rank([bits(f) for _, f in fl])
        rk3 = gf2_rank([bits(f) for _, f in fl] + [bits(straight_loop(G, a)) for a in range(3)])
        print(f"  L={L}: V={G.nV} E={G.nE} faces={len(fl)} ({ {k: len(G.faces[k]) // N for k in TYPES} } per site);"
              f" E-V+1={cyc}; rank(faces)={rk}; rank(+3 straight loops)={rk3}; {el()}")
        check(f"A1 L={L}: faces span the cycle space up to the 3 noncontractible classes (rank = E - V + 1 - 3)",
              rk == cyc - 3 and rk3 == cyc)
        rels = face_relations(G)
        tidx = {k: [i for i, (kk, _) in enumerate(fl) if kk == k] for k in TYPES}
        prof = {tuple(sum((r >> i) & 1 for i in tidx[k]) % 2 for k in TYPES) for r in rels}
        print(f"  L={L}: {len(rels)} independent face relations; type-parity vectors {sorted(prof)}")
        if L % 2 == 0:
            check(f"A1 L={L}: every face relation has even type parity (all 16 uniform patterns consistent)", prof == {(0, 0, 0, 0)})
        else:
            check(f"A1 L={L}: the only odd type parity is (square, plaquette) from a wrapped relation (torus-size effect)",
                  prof == {(0, 0, 0, 0), (1, 0, 1, 0)})
        ok = True; nsol = 0
        for Fb in itertools.product((0, 1), repeat=4):
            u = gauge_for(G, Fb)
            expect = (L % 2 == 0) or (Fb[0] == Fb[2])
            if u is None:
                ok &= not expect; continue
            nsol += 1
            ok &= expect and all(fx == Fb[TYPES.index(k)] for k, fx in face_fluxes(G, u))
        check(f"A1 L={L}: uniform patterns realized by a gauge field exactly as the parities predict ({nsol}/16; fluxes re-measured)", ok)
        if L == 4:
            # the 4-periodic lift of each L = 4 solution is a gauge field on Z^3 with the uniform flux on every face
            u = rng.integers(0, 2, G.nE)
            Fr = [fx for _, fx in face_fluxes(G, u)]
            check("A1 L=4: a random gauge field gives a consistent non-uniform flux configuration (sectors are not unique)",
                  gauge_for_list(G, Fr) is not None and 0.3 < np.mean(Fr) < 0.7, f"mean flux {np.mean(Fr):.3f}")


def gauge_for_list(G, Flist):
    return gf2_solve([f for _, f in G.face_list()], Flist, G.nE)


class Pauli:
    """i^p X^x Z^z with x, z boolean arrays."""
    __slots__ = ('p', 'x', 'z')

    def __init__(self, p, x, z):
        self.p, self.x, self.z = p % 4, x, z

    def __mul__(self, o):
        return Pauli(self.p + o.p + 2 * (int(np.count_nonzero(self.z & o.x)) % 2), self.x ^ o.x, self.z ^ o.z)

    def std_phase(self):
        return (self.p - int(np.count_nonzero(self.x & self.z))) % 4


def face_relations(G):
    """basis of the GF(2) relations among the faces (face-index bitmasks, face_list order)."""
    fl = G.face_list(); piv = {}; rels = []
    for idx, (k, f) in enumerate(fl):
        x = bits(f) | (1 << (G.nE + idx))
        while True:
            low = x & ((1 << G.nE) - 1)
            if low == 0:
                rels.append(x >> G.nE); break
            c = low.bit_length() - 1
            if c in piv: x ^= piv[c]
            else: piv[c] = x; break
    return rels


def part_A2A3(rng):
    print("\nA2/A3. Bravyi-Kitaev superfast encoding on the corner graph, L = 3 (exact Pauli algebra with phases)")
    G = CornerGraph(3); nE = G.nE; L = 3
    INC = [[] for _ in range(G.nV)]
    for k, (i, j, _, _) in enumerate(G.edges):
        INC[i].append(k); INC[j].append(k)

    def build_S(order):
        """S_e = X_e prod_{l <_i e} Z_l prod_{l <_j e} Z_l (BKSF edge operators for vertex orders <_v)."""
        rank = [dict((e, r) for r, e in enumerate(order[v])) for v in range(G.nV)]
        S = []
        for k, (i, j, _, _) in enumerate(G.edges):
            x = np.zeros(nE, bool); z = np.zeros(nE, bool); x[k] = True
            for v in (i, j):
                for l in order[v]:
                    if rank[v][l] < rank[v][k]: z[l] ^= True
            S.append(Pauli(0, x, z))
        return S

    def algebra_ok(S, sample=400):
        ok = True
        for _ in range(sample):
            a, b = rng.integers(0, nE, 2)
            if a == b: continue
            anti = (int(np.count_nonzero(S[a].x & S[b].z)) + int(np.count_nonzero(S[a].z & S[b].x))) % 2
            share = len({G.edges[a][0], G.edges[a][1]} & {G.edges[b][0], G.edges[b][1]}) == 1
            ok &= (anti == 1) == share
        return ok

    faces = [(k, f, s) for k in TYPES for f, s in zip(G.faces[k], G.face_seq[k])]
    kinds = np.array([k for k, _, _ in faces])
    fl = [f for _, f, _ in faces]
    rels = face_relations(G)
    members = [[i for i in range(len(fl)) if (r >> i) & 1] for r in rels]

    def loops(S, label):
        """for each face C: kappa_C = i^n (prod eps) i^q and the bare tensor-product Pauli string B_C, where
        prod_{e in C} S_e = i^q B_C (eps_jk = +1 if label[j] < label[k]).  The signed loop stabilizer of
        flux F is g_C = F_C kappa_C B_C (Hermitian); F_C is then the flux of the encoded fermion."""
        kap = []; bare = []
        for k, f, seq in faces:
            vs = [G.vid[(tuple(x % L for x in p), c)] for p, c in seq]
            P = Pauli(0, np.zeros(nE, bool), np.zeros(nE, bool)); eps = 1
            for e, a, b in zip(f, vs, vs[1:] + vs[:1]):
                P = P * S[e]; eps *= 1 if label[a] < label[b] else -1
            q = P.std_phase()
            val = (1j ** len(f)) * eps * (1j ** q)
            assert abs(val.imag) < 1e-12 and abs(abs(val.real) - 1) < 1e-12
            kap.append(int(round(val.real))); bare.append(Pauli(P.p - q, P.x, P.z))
        return np.array(kap), bare

    def relation_signs(bare):
        """sigma_r = +-1 with prod_{C in r} B_C = sigma_r I (the bare strings commute; X and Z parts cancel)."""
        out = []
        for mem in members:
            Q = Pauli(0, np.zeros(nE, bool), np.zeros(nE, bool))
            for i in mem:
                Q = Q * bare[i]
            assert not Q.x.any() and not Q.z.any()
            out.append(1 if Q.std_phase() == 0 else -1)
        return np.array(out)

    def sector_consistent(F, kap, sig):
        """the group generated by g_C = F_C kappa_C B_C contains no -I iff every basis relation multiplies to +I."""
        return all(np.prod(F[mem]) * np.prod(kap[mem]) * s == 1 for mem, s in zip(members, sig))

    conv = {}
    for name in ('canonical', 'random-1', 'random-2'):
        if name == 'canonical':
            order = [sorted(INC[v]) for v in range(G.nV)]; label = np.arange(G.nV)
        else:
            order = [list(rng.permutation(INC[v])) for v in range(G.nV)]; label = rng.permutation(G.nV)
        S = build_S(order)
        kap, bare = loops(S, label)
        sig = relation_signs(bare)
        conv[name] = (S, label, kap, bare, sig)
        check(f"A2 BKSF hops under convention '{name}' anticommute exactly when the edges share one vertex (400 sampled pairs)",
              algebra_ok(S))
    d = conv['random-1'][2] != conv['random-2'][2]
    check("A2 the formal 'natural' flux kappa_C (the flux of the 'all bare loop strings = +1' assignment) depends on the arbitrary"
          " labelling/ordering convention", d.sum() > 0,
          f"faces differing between two random conventions: { {k: int(d[kinds == k].sum()) for k in TYPES} } of {len(faces)}")
    kc = conv['canonical'][2]
    print("  canonical convention, # faces with kappa = -1 per type:", {k: (int((kc[kinds == k] == -1).sum()), int((kinds == k).sum())) for k in TYPES})
    check("A2 observation (L = 3, index labelling only): the canonical kappa is not uniform on every face type",
          any(len(set(kc[kinds == k].tolist())) > 1 for k in TYPES))
    ok = True; empt = {}
    for name, (S, label, kap, bare, sig) in conv.items():
        ok &= all(np.prod(kap[mem]) == s for mem, s in zip(members, sig))
        empt[name] = int((sig == -1).sum())
    check("A2 identity: for every basis face relation r, prod_{C in r} kappa_C = sigma_r (the operator sign of the product of bare strings),"
          " in all three conventions; so the flux-free sector F = +1 exists in every convention", ok,
          f"relations with sigma_r = -1 (all-bare-+1 assignment inconsistent): {empt} of {len(rels)}")
    check("A2 observation: in these three generic conventions the all-bare-strings-+1 assignment is not a consistent sector (some basis"
          " relation has bare product -I); hop-sign flips alone cannot change this (they leave B_C and sigma unchanged)",
          all(v > 0 for v in empt.values()))
    # the vertex orderings are part of the convention: search translation-invariant orderings (the same order of the six
    # incident edge slots (corner, neighbour corner, displacement) at every vertex of a given corner type) for one in which
    # every sigma_r = +1, so that the all-bare-+1 assignment IS a consistent sector.  Fast bitmask Paulis for the search;
    # the result is re-verified from scratch with the array implementation above.
    def slot(v, k):
        i, j, _, _ = G.edges[k]; (vs, c, disp, c2) = G.edesc[k]
        return (c, c2, disp) if v == i else (c2, c, tuple(-x for x in disp))
    ctype = [G.verts[v][1] for v in range(G.nV)]
    slots_of = {}
    for v in range(G.nV):
        slots_of.setdefault(ctype[v], sorted((slot(v, k) for k in INC[v]), key=repr))
    slotmap = [{slot(v, k): k for k in INC[v]} for v in range(G.nV)]
    def make_order(perm):
        return [[slotmap[v][s] for s in perm[ctype[v]]] for v in range(G.nV)]
    def nviol(order):
        Sb = []
        for k, (i, j, _, _) in enumerate(G.edges):
            z = 0
            for v in (i, j):
                for l in order[v]:
                    if l == k: break
                    z ^= 1 << l
            Sb.append((0, 1 << k, z))
        bare_b = []
        for f in fl:
            p, x, z = 0, 0, 0
            for e in f:
                p2, x2, z2 = Sb[e]
                p, x, z = p + p2 + 2 * (z & x2).bit_count(), x ^ x2, z ^ z2
            q = (p - (x & z).bit_count()) % 4
            bare_b.append(((p - q) % 4, x, z))
        n = 0
        for mem in members:
            p, x, z = 0, 0, 0
            for i in mem:
                p2, x2, z2 = bare_b[i]
                p, x, z = p + p2 + 2 * (z & x2).bit_count(), x ^ x2, z ^ z2
            n += ((p - (x & z).bit_count()) % 4) != 0
        return n
    srng = np.random.default_rng(5)
    types = sorted(slots_of, key=repr)
    perm = {t: [slots_of[t][i] for i in srng.permutation(6)] for t in types}
    cur = nviol(make_order(perm)); start = cur; Ttemp = 2.0; step = 0
    for step in range(3000):
        if cur == 0: break
        t = types[srng.integers(len(types))]; a, b = srng.choice(6, 2, replace=False)
        perm[t][a], perm[t][b] = perm[t][b], perm[t][a]
        nv = nviol(make_order(perm))
        if nv <= cur or srng.random() < math.exp(-(nv - cur) / Ttemp):
            cur = nv
        else:
            perm[t][a], perm[t][b] = perm[t][b], perm[t][a]
        Ttemp = max(0.05, Ttemp * 0.997)
    print(f"  translation-invariant ordering search: {start} -> {cur} relations with sigma_r = -1 after {step} steps; {el()}")
    ok = cur == 0
    if ok:
        order = make_order(perm); label = np.arange(G.nV)
        S = build_S(order); kap, bare = loops(S, label); sig = relation_signs(bare)
        ok &= algebra_ok(S) and (sig == 1).all() and all(np.prod(kap[mem]) == s for mem, s in zip(members, sig))
        b0 = (kap == -1).astype(int)
        for tname in ('uniform 1011', 'uniform 1111', 'uniform 0000'):
            T = np.array([tuple(int(ch) for ch in tname.split()[1])[TYPES.index(k)] for k in kinds])
            w = gf2_solve(fl, (T ^ b0).tolist(), nE)
            if w is None:
                ok = False; continue
            S2 = [Pauli(s.p + 2, s.x, s.z) if w[e] else s for e, s in enumerate(S)]
            kap2, bare2 = loops(S2, label)
            ok &= ((kap2 == -1).astype(int) == T).all() and (relation_signs(bare2) == 1).all()
    check("A2 a translation-invariant vertex ordering exists on L = 3 for which every sigma_r = +1 (re-verified from scratch, hop"
          " algebra re-checked), and hop-sign flips of it make uniform 1011, 1111 and 0000 each the consistent bare sector:"
          " which consistent F is 'bare' is set by the dictionary", ok)
    # a fixed convention realizes every consistent flux configuration, and only those
    u = rng.integers(0, 2, nE)
    targets = {'uniform 1011': np.array([(1, 0, 1, 1)[TYPES.index(k)] for k in kinds]),
               'uniform 1111': np.array([(1, 1, 1, 1)[TYPES.index(k)] for k in kinds]),
               'uniform 0000': np.zeros(len(fl), int),
               'random consistent': np.array([int(sum(int(u[e]) for e in f) % 2) for f in fl])}
    ok = True
    for name, (S, label, kap, bare, sig) in conv.items():
        for tname, T in targets.items():
            F = 1 - 2 * T
            ok &= sector_consistent(F, kap, sig) and gf2_solve(fl, T.tolist(), nE) is not None
        Tbad = targets['uniform 1011'].copy(); Tbad[0] ^= 1
        ok &= (not sector_consistent(1 - 2 * Tbad, kap, sig)) and gf2_solve(fl, Tbad.tolist(), nE) is None
    check("A2 in each fixed convention the signed loop stabilizers of flux F generate a group without -I exactly for consistent F:"
          " uniform 1011, 1111, 0000 and a random consistent F all exist; one flipped face does not", ok)
    S, label, kap, bare, sig = conv['canonical']
    ok = True
    for e in rng.integers(0, nE, 5):
        S2 = list(S); S2[e] = Pauli(S[e].p + 2, S[e].x, S[e].z)
        kap2, bare2 = loops(S2, label)
        ok &= all((a != b) == (e in f) for f, a, b in zip(fl, kap, kap2))
        ok &= all((b1.x == b2.x).all() and (b1.z == b2.z).all() and b1.p == b2.p for b1, b2 in zip(bare, bare2))
    check("A3 flipping one hop sign A_e -> -A_e (all algebraic relations preserved) flips kappa on exactly the faces containing e and"
          " leaves every bare string unchanged (5 random edges, all faces); it relabels sectors F -> F * (-1)^[e in C]", ok)


ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROTS.append(M)
assert len(ROTS) == 24


def part_A4():
    print("\nA4. fermion-level projective symmetry group on L = 4 (BFS sign propagation) and design-target selection")
    L = 4; G = CornerGraph(L); V = G.nV
    nbr = [[] for _ in range(V)]
    pairedge = {}
    for k, (i, j, _, _) in enumerate(G.edges):
        nbr[i].append((j, k)); nbr[j].append((i, k))
        key = frozenset((i, j)); assert key not in pairedge; pairedge[key] = k

    def vperm(f):
        return np.array([G.vid[f(q)] for q in G.verts])
    def rot(R):
        return lambda q: (tuple(int(x) % L for x in R @ np.array(q[0])), frozenset(tuple(int(x) for x in R @ np.array(d)) for d in q[1]))
    def trans(t):
        return lambda q: (tuple((a + b) % L for a, b in zip(q[0], t)), q[1])

    def psg(P, u):
        """D (+-1 per vertex) with D[Pi] D[Pj] s(Pi,Pj) = s(i,j) on every edge (s = (-1)^u), or None."""
        s = 1 - 2 * u.astype(int)
        D = np.zeros(V, int); D[P[0]] = 1
        seen = np.zeros(V, bool); seen[0] = True; stack = [0]
        while stack:
            i = stack.pop()
            for j, k in nbr[i]:
                val = D[P[i]] * s[pairedge[frozenset((P[i], P[j]))]] * s[k]
                if not seen[j]:
                    seen[j] = True; D[P[j]] = val; stack.append(j)
                elif D[P[j]] != val:
                    return None
        return D

    # operator U = (P, D): U e_i = D[P i] e_{P i}
    def comp_fix(*ops):
        """compose right-to-left; track the sign attached to each basis vector i."""
        img = np.arange(V); sign = np.ones(V, int)
        for (P2, D2) in reversed(ops):
            img = P2[img]; sign = sign * D2[img]
        return img, sign
    def inv(op):
        P, D = op
        Pi = np.empty(V, int); Pi[P] = np.arange(V)
        # U^-1 e_{P i} = D[P i] e_i  ->  (Pi, D') with D'[i] = D[P i]
        return Pi, D[P]
    def scalar(*ops):
        img, sign = comp_fix(*ops)
        if not (img == np.arange(V)).all() or len(set(sign.tolist())) != 1:
            return None
        return int(sign[0])
    def power(op, m):
        return scalar(*([op] * m))

    Rp = [vperm(rot(R)) for R in ROTS]
    E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    Tp = [vperm(trans(a)) for a in E3]
    def kind(R):
        tr = int(np.trace(R)); m = {3: 1, -1: 2, 0: 3, 1: 4}[tr]
        if m == 2: return ('C2axis' if (np.abs(np.diag(R)) == 1).all() else 'C2edge'), 2
        return {1: 'e', 3: 'C3', 4: 'C4'}[m], m
    table = {}
    for Fb in itertools.product((0, 1), repeat=4):
        u = gauge_for(G, Fb)
        res = {}
        T = []
        for P in Tp:
            D = psg(P, u)
            if D is None: res = None; break
            T.append((P, D))
        if res is None: table[Fb] = None; continue
        Rops = []
        for R, P in zip(ROTS, Rp):
            D = psg(P, u)
            if D is None: res = None; break
            Rops.append((P, D))
            kname, m = kind(R)
            res.setdefault(kname, set()).add(power((P, D), m))
        if res is None: table[Fb] = None; continue
        c = scalar(inv(T[1]), inv(T[0]), T[1], T[0])
        res['TxTy'] = c
        res['T^4'] = [power(t, 4) for t in T]
        fixed = None
        if c == 1 and res['T^4'] == [1, 1, 1]:
            shifts = []
            for R, MR in zip(ROTS, Rops):
                sh = np.zeros(3, int)
                for a_i, a in enumerate(E3):
                    Ra = R @ np.array(a); ax = int(np.argmax(np.abs(Ra)))
                    Ta = T[ax] if Ra[ax] > 0 else inv(T[ax])
                    cval = scalar(MR, T[a_i], inv(MR), inv(Ta))
                    assert cval is not None
                    if cval == -1: sh[ax] += 1
                shifts.append(sh % 2)
            fixed = [k for k in itertools.product(range(4), repeat=3)
                     if all(((R @ np.array(k) + 2 * s - np.array(k)) % 4 == 0).all() for R, s in zip(ROTS, shifts))]
        res['fixed'] = fixed
        table[Fb] = res
        print('   ', ''.join(map(str, Fb)), {k: (sorted(v) if isinstance(v, set) else v) for k, v in res.items()}, flush=True)
    check("A4 the PSG exists for all 16 uniform patterns (consistent BFS sign propagation for the 24 rotations and 3 translations)",
          all(v is not None for v in table.values()))
    check("A4 C4^4 = -1 exactly when square = pi; axis C2^2 = -1 exactly when square = pi (u-convention)",
          all((v['C4'] == {-1}) == (F[0] == 1) and (v['C2axis'] == {-1}) == (F[0] == 1) for F, v in table.items()))
    check("A4 translations commute exactly when square = plaquette, and anticommute otherwise",
          all((v['TxTy'] == 1) == (F[0] == F[2]) and v['TxTy'] in (1, -1) for F, v in table.items()))
    targets = sorted(F for F, v in table.items() if v['C4'] == {-1} and v['TxTy'] == 1 and v['fixed'])
    print("  patterns with C4^4 = -1, commuting translations and an O-fixed momentum:", [''.join(map(str, F)) for F in targets])
    check("A4 the design targets (C4^4 = -1, commuting translations, an O-fixed momentum) select exactly {1011, 1111}: triangle free",
          targets == [(1, 0, 1, 1), (1, 1, 1, 1)])
    fx = table[(1, 0, 1, 1)]['fixed']
    check("A4 1011 has exactly two O-fixed momenta, differing by (pi, pi, pi) (their form is gauge dependent)",
          len(fx) == 2 and (((np.array(fx[0]) - np.array(fx[1])) % 4) == 2).all(), f"units pi/2: {fx}")
    check("A4 with square = 0 and commuting translations an O-fixed momentum exists iff tube = 0 (tube = pi needs square = pi)",
          all(bool(table[F]['fixed']) == (F[3] == 0) for F in table if F[0] == 0 and F[2] == 0))
    # gauge-invariant standard-convention statement
    u = gauge_for(G, (1, 0, 1, 1))
    ok = True
    for t2 in (0.2, -0.2):
        for k, f in G.face_list():
            prod = 1.0
            for e in f:
                t = -1.0 if G.edges[e][2] == 'onsite' else t2
                prod *= t * (-1) ** int(u[e])         # prod(-h), h = -t (-1)^u
            ok &= prod < 0
    check("A4 u-pattern 1011 with t1 = -1 (either sign of t2, lambda = 0) has standard-convention flux pi through every face", ok)
    ok = all(np.prod([(-1) ** int(u[e]) for e in f]) > 0 for f in G.faces['triangle'])
    check("A4 control: with t1 = +1 the same gauge field gives standard triangle flux 0 (the sign of t1 is load-bearing)", ok)
    # chiral triangle phase
    lam = -0.5
    ok = True
    for v in G.sites[:8]:
        for s in itertools.product((1, -1), repeat=3):
            x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
            cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
            if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
            prod = 1.0 + 0j
            for a in range(3):
                e = G.edge_between((v, cy[a]), (0, 0, 0), cy[(a + 1) % 3])
                h = -(-1.0) * (-1) ** int(u[e]) + 1j * lam * (-1) ** int(u[e])     # H[r, q], oriented q -> r
                prod *= -h
            ok &= abs(np.angle(prod * np.exp(-1j * (np.pi + 3 * np.arctan(lam))))) < 1e-12
    check("A4 with the chiral term (t1 = -1, lambda = -0.5) every oriented triangle carries standard phase pi + 3 arctan(lambda)", ok)
    # every face type with the chiral term: a face carries pi + arctan(lambda) * sum_e sigma_e over its on-site edges,
    # sigma_e = +1 (-1) when the face runs along (against) the det > 0 orientation of the triangle containing e
    M = Model(L); orient = {e: (q, r) for q, r, e in M.tri}
    amp = -np.where(M.kind == 0, -1.0, 0.2) * (-1.0) ** u
    Hk = np.zeros((V, V), complex)
    np.add.at(Hk, (M.J, M.I), amp); np.add.at(Hk, (M.I, M.J), amp)
    for q, r, e in M.tri:
        a = 1j * lam * (-1.0) ** u[e]; Hk[r, q] += a; Hk[q, r] += np.conj(a)
    th = np.arctan(lam); ok = True; net = {k: set() for k in TYPES}
    for k in TYPES:
        for seq in G.face_seq[k]:
            ids = [G.vid[(tuple(x % L for x in p_), c)] for p_, c in seq]
            prod = 1.0 + 0j; sg = 0
            for (a_, b_), e in zip(zip(ids, ids[1:] + ids[:1]), G._cycle(seq)):
                prod *= -Hk[b_, a_]
                if G.edges[e][2] == 'onsite':
                    sg += 1 if orient[e] == (a_, b_) else -1
            ok &= abs(np.angle(prod * np.exp(-1j * (np.pi + th * sg)))) < 1e-12
            net[k].add(abs(sg))
    print("  |sum sigma| by face type:", {k: sorted(v) for k, v in net.items()})
    check("A4 with the chiral term every face carries standard phase pi + arctan(lambda) * sum_e sigma_e over its on-site edges;"
          " |sum sigma| = 4 (square), 3 (triangle), 0 (plaquette), 2 (tube): squares pi -+ 4 arctan(lambda), tubes pi -+ 2 arctan(lambda)",
          ok and net == {'square': {4}, 'triangle': {3}, 'plaquette': {0}, 'tube': {2}})


# =====================================================================================================
# E. energetics (numerical, behind --energetics)
# =====================================================================================================
class Model:
    def __init__(self, Ls):
        self.G = G = CornerGraph(Ls)
        self.n = G.nV
        self.I = np.array([e[0] for e in G.edges]); self.J = np.array([e[1] for e in G.edges])
        self.kind = np.array([0 if e[2] == 'onsite' else 1 for e in G.edges])
        self.W = np.array([e[3] for e in G.edges], float)
        self.tri = []
        for v in G.sites:
            for s in itertools.product((1, -1), repeat=3):
                x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
                cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
                if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
                for a in range(3):
                    q, r = (v, cy[a]), (v, cy[(a + 1) % 3])
                    self.tri.append((G.vid[q], G.vid[r], G.edge_between(q, (0, 0, 0), cy[(a + 1) % 3])))

    def spectrum(self, u, nk, t1, t2, lam=0.0):
        g = 2 * np.pi * np.arange(nk) / nk
        Ks = np.array(list(itertools.product(g, repeat=3)))
        amp = -np.where(self.kind == 0, t1, t2) * (-1.0) ** u
        A = amp[None, :] * np.exp(1j * Ks @ self.W.T)
        H = np.zeros((len(Ks), self.n, self.n), complex)
        np.add.at(H, (slice(None), self.J, self.I), A)
        np.add.at(H, (slice(None), self.I, self.J), np.conj(A))
        if lam:
            for q, r, e in self.tri:
                a = 1j * lam * (-1.0) ** u[e]
                H[:, r, q] += a; H[:, q, r] += np.conj(a)
        return np.sort(np.linalg.eigvalsh(H).ravel())

    @staticmethod
    def E(ev, nu):
        ns = len(ev) / 12.0
        return float(ev[:int(round(nu * ns))].sum() / ns)


def part_E(rng):
    print(f"\nE. nu = 1 energetics of the 16 uniform sectors (free fermions; numerical); {el()}")
    M2 = Model(2); M4 = Model(4)
    u2 = rng.integers(0, 2, M2.G.nE).astype(np.uint8)
    desc2 = {}
    for k, (v, c, disp, c2) in enumerate(M2.G.edesc):
        desc2[(v, c, disp, c2)] = k
        w = tuple((a + b) % 2 for a, b in zip(v, disp))
        desc2[(w, c2, tuple(-x for x in disp), c)] = k
    u4 = np.array([u2[desc2[(tuple(x % 2 for x in v), c, disp, c2)]] for (v, c, disp, c2) in M4.G.edesc], np.uint8)
    ok = all(np.allclose(M2.spectrum(u2, 2, 1.0, 0.3, lam), M4.spectrum(u4, 1, 1.0, 0.3, lam), atol=1e-9) for lam in (0.0, -0.5))
    check("E0 Bloch 2^3 supercell with K in {0, pi}^3 reproduces the direct L = 4 real-space spectrum (random gauge, lambda = 0, -0.5)", ok)
    PATS = list(itertools.product((0, 1), repeat=4))
    gauges = {F: gauge_for(M2.G, F) for F in PATS}
    lab = lambda F: ''.join(map(str, F))
    prior = {0.2: (15, 1.854), 1.0: (16, 1.514)}       # recorded by the C6 worker and the C6 check (two implementations)
    for t2 in (0.2, 1.0):
        spec = {F: M2.spectrum(gauges[F], 6, 1.0, t2) for F in PATS}
        E1 = {F: Model.E(spec[F], 1) for F in PATS}
        order = sorted(PATS, key=lambda F: E1[F])
        rk = order.index((1, 1, 1, 1)) + 1; exc = E1[(1, 1, 1, 1)] - E1[(0, 0, 0, 0)]
        print(f"  t1 = 1, t2 = {t2} (standard convention; corner = 1111): " +
              ', '.join(f"{lab(F)} {E1[F]:.4f}" for F in order) + f"; {el()}")
        check(f"E1 t2 = {t2}, nu = 1: the corner pattern 1111 ranks 15th or 16th of 16 uniform sectors and lies > 1.5 per site above flux-free",
              rk >= 15 and exc > 1.5, f"rank {rk}/16, excess {exc:+.4f} (campaign record: rank {prior[t2][0]}, {prior[t2][1]:+.3f})")
        if t2 == 0.2:
            e1 = {F: spec[F][0] for F in PATS}
            others = min(e1[F] for F in PATS if F != (0, 0, 0, 0))
            check("E2 diamagnetic inequality: flux-free 0000 has the strictly lowest one-particle energy", e1[(0, 0, 0, 0)] < others - 1e-9,
                  f"{e1[(0,0,0,0)]:.6f} vs {others:.6f}")
            dev = 0.0
            for F in PATS:
                Fp = (F[0], 1 - F[1], F[2], F[3])
                for nu in (1, 5, 7):
                    dev = max(dev, abs(Model.E(spec[F], nu) - Model.E(spec[Fp], 12 - nu)))
            check("E3 particle-hole identity E(F, nu) = E(F with triangle flipped, 12 - nu) (nu = 1, 5, 7; all 16 patterns)", dev < 1e-9,
                  f"max dev {dev:.1e}")
            g1011 = gauges[(1, 0, 1, 1)]
            e_repo = Model.E(M2.spectrum(g1011, 6, -1.0, t2), 1)
            check("E4 gauge consistency: repo convention (t1 = -1, u-pattern 1011) has the same nu = 1 energy as standard 1111",
                  abs(e_repo - E1[(1, 1, 1, 1)]) < 1e-9, f"{e_repo:.6f} vs {E1[(1,1,1,1)]:.6f}")
    Ec = {F: Model.E(M2.spectrum(gauges[F], 6, -1.0, 0.2, -0.5), 1) for F in PATS}
    order = sorted(PATS, key=lambda F: Ec[F]); rk = order.index((1, 0, 1, 1)) + 1
    print(f"  repo convention t1 = -1, t2 = 0.2, lambda = -0.5 (corner = u-pattern 1011): " + ', '.join(f"{lab(F)} {Ec[F]:.4f}" for F in order))
    check("E5 with the chiral term the corner pattern is not the lowest uniform sector at nu = 1", rk > 1,
          f"rank {rk}/16 (campaign record: 6/16), E = {Ec[(1,0,1,1)]:.4f}, best {lab(order[0])} {Ec[order[0]]:.4f}")


def n5_certificate(energetics):
    print("\nN5 execution certificate (resolution classes actually exercised)")
    print("per_element: exact GF(2) face-flux values on every face of the L = 3, 4 corner tori; single-hop sign flips (A3) on 5 random edges.")
    print("per_site: per-site face counts, PSG sign functions D on every corner vertex, 12-mode even-algebra dimension facts for n = 1..4.")
    print("per_mode: " + ("Bloch one-particle spectra of 16 uniform sectors on a 2^3 cell with a 6^3 K-grid, nu = 1 sums." if energetics else
                          "checked and not executed — the one-particle energetics run only with --energetics."))
    print("per_block: superlattice (5Z^3) amplitudes over all 124 nonzero block momenta; coset frequencies over the 125 cosets.")
    print("lattice_wide: cycle-space ranks and face-relation parities of whole tori; O-invariant sublattice enumeration to index 32;"
          " the infinite-volume registration lemma is analytic and is not executed.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--energetics', action='store_true', help='run the nu = 1 free-fermion energetics spot check (part E)')
    ap.add_argument('--full', action='store_true', help='also run A1 on the L = 6 torus')
    ap.add_argument('--seed', type=int, default=20261018)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)
    part_R(rng)
    part_D()
    part_A1((3, 4, 6) if args.full else (3, 4), rng)
    part_A2A3(rng)
    part_A4()
    if args.energetics:
        part_E(rng)
    n5_certificate(args.energetics)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}  ({time.time()-T0:.0f} s, seed {args.seed}, energetics={args.energetics}, full={args.full})")
    sys.exit(1 if FAIL else 0)


if __name__ == '__main__':
    main()
