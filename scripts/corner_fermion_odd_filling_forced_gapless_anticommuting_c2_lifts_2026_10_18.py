#!/usr/bin/env python3
"""Odd filling of the supplied corner fermion is forced gapless by anticommuting gauge-dressed C2 lifts.

Supplied model only (corner fermion, flux square = plaquette = tube = pi, triangle = 0,
translation-invariant gauge); number-conserving fermions; no physical identification.

Sections (each prints [PASS]/[FAIL] lines):
  A  reduction: every PSG lift is G_g|v,c> = (-1)^(lam_g.v + tau_g(c)) |g v, g c>; the Bloch relation
     U_g H(k) U_g^T = H(g k + pi s_g); exactly 21 of 24 proper rotations carry a nonzero shift s_g, and
     only +-k* are fixed by all 24 affine maps;
  B  global anticommutation: for all 12 commuting pairs of proper C2 rotations the dressed lifts
     anticommute as operators on the whole one-particle space (exact sign bookkeeping, plus the
     L = 4 torus operators);
  C  even levels at momenta fixed by both C2s (+-k* for O; all 8 points (+-pi/2)^3 for D2) and the
     odd-filling free-fermion gaplessness logic E_nu(k*) = E_{nu+1}(k*) for odd nu;
  D  a certified nu = 2 insulator (translations + 24 dressed rotations), a certified nu = 1 insulator
     with C2x only, and the site irreps (O: [2,2,4,4]; O_h: [4,4,4]);
  E  twisted odd-L tori (theta = +-k*; L = 1, 3): all 24 rotations are symmetries, theta = 0 fails for
     21; one-particle levels even; Fock-space Gamma(C2x)Gamma(C2y) = (-1)^N Gamma(C2y)Gamma(C2x) at
     L = 1 and even degeneracy of interacting symmetric Hamiltonians in odd-N sectors;
  F  the doubled-cell class (dressed O_h about site 0 + even translations): free-fermion quartets at
     the folded k*, and a symmetric atomic (product) pair state at nu = 1; scoping control showing the
     class differs from the cube-centre (A2-staggered-mass) group.
Companion: docs/CORNER_FERMION_ODD_FILLING_IS_FORCED_GAPLESS_BY_ANTICOMMUTING_GAUGE_DRESSED_C2_LIFTS_BOUNDED_THEOREM_NOTE_2026-10-18.md
"""
import itertools, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


def mults(ev, tol=1e-8):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol: j += 1
        out.append(j - i + 1); i = j + 1
    return out


# ============================================================ model layer (repo definitions)
def build():
    import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as _model
    C = _model._run_reviewed_program(definitions_only=True)
    L = C['L']; VERTS = C['VERTS']; nV = len(VERTS); CORN = C['CORNERS']; ROTS = C['ROTS']; DIRS = C['DIRS']
    F = dict(square=1, triangle=0, plaquette=1, tube=1)
    def dmod(x): return ((x + 1) % L) - 1
    def neg(d): return tuple(-x for x in d)
    def perp(d, e): return sum(a * b for a, b in zip(d, e)) == 0 and d != e
    # translation-invariant gauge on the one-site cell (same GF(2) solve as the cross-rung runner)
    etypes = []; ekey = {}
    def addt(c1, c2, sh):
        if (c1, c2, sh) in ekey or (c2, c1, neg(sh)) in ekey: return
        ekey[(c1, c2, sh)] = ekey[(c2, c1, neg(sh))] = len(etypes); etypes.append((c1, c2, sh))
    Z0 = (0, 0, 0)
    for c in CORN:
        d, e = tuple(c)
        for a, b in ((d, e), (e, d)):
            for f in DIRS:
                if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                    addt(c, frozenset((a, f)), Z0)
            addt(c, frozenset((neg(a), b)), a)
    nT = len(etypes)
    def cyc(seq):
        return [ekey[(c1, c2, tuple(y - x for x, y in zip(p1, p2)))]
                for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1])]
    def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
    cell = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
    for d in DIRS:
        a = [f for f in DIRS if perp(f, d) and f != neg(d)]; a0 = a[0]
        b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]; ring = [a0, b0, neg(a0), neg(b0)]
        cell['square'].append(cyc([(frozenset((d, r)), Z0) for r in ring]))
        for i in range(4):
            p, q = ring[i], ring[(i + 1) % 4]
            cell['tube'].append(cyc([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d),
                                     (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]))
    for s in itertools.product((1, -1), repeat=3):
        x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
        cell['triangle'].append(cyc([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]))
    for d, e in (((1, 0, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0))):
        cell['plaquette'].append(cyc([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d),
                                      (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
    rows = []; rhs = []
    for k, cs in cell.items():
        for c in cs: rows.append(c); rhs.append(F[k])
    ucell = C['gf2_solve'](rows, rhs, nT)
    u = np.zeros(C['nE'], np.uint8)
    for key, i in C['EID'].items():
        a, b = tuple(key); (v, c), (w, c2) = VERTS[a], VERTS[b]
        u[i] = ucell[ekey[(c, c2, tuple(dmod(y - x) for x, y in zip(v, w)))]]
    flux_ok = all({int(sum(u[j] for j in c) % 2) for c in cs} == {F[k]} for k, cs in C['cycles'].items())
    # O_h about site 0: proper first, then I*R; PSG lifts on the L = 4 torus from the repo's psg_sign
    OH = [R for R in ROTS] + [-R for R in ROTS]
    psg = [C['psg_sign'](lambda q, M=M: C['rot_vert'](M, q), u) for M in OH]
    CI = {c: i for i, c in enumerate(CORN)}
    E3 = np.eye(3, dtype=int)
    lam, tau, Ug = [], [], []
    dec_ok = all(p is not None for p in psg)
    for M, (P, s) in zip(OH, psg):
        t = np.array([int(s[C['VID'][((0, 0, 0), c)]]) for c in CORN])
        l = np.array([(int(s[C['VID'][(tuple(E3[j]), CORN[0])]]) - t[0]) % 2 for j in range(3)])
        for a, (v, c) in enumerate(VERTS):
            dec_ok &= (int(s[a]) - (int(np.dot(l, v)) + t[CI[c]])) % 2 == 0
        U = np.zeros((12, 12))
        for c in CORN:
            Rc = frozenset(tuple(int(x) for x in M @ np.array(d)) for d in c)
            U[CI[Rc], CI[c]] = (-1.0) ** t[CI[c]]
        lam.append(l); tau.append(t); Ug.append(U)
    shift = [np.abs(M) @ l % 2 for M, l in zip(OH, lam)]
    def w1(R):
        p = [DIRS.index(tuple(int(x) for x in R @ np.array(d))) for d in DIRS]; sgn = 1
        for i in range(6):
            while p[i] != i:
                j = p[i]; p[i], p[j] = p[j], p[i]; sgn = -sgn
        return 0 if sgn == 1 else 1
    W1 = [w1(R) for R in ROTS]
    loc0 = [C['VID'][((0, 0, 0), c)] for c in CORN]
    def H0mat(t1, t2):
        H = np.zeros((nV, nV))
        for key in C['EDGES']:
            i, j = tuple(key); tt = t1 if C['edges'][key] == 'onsite' else t2
            H[i, j] = H[j, i] = -tt * (-1.0) ** u[C['EID'][key]]
        return H
    def blocks_from(Hr):
        bl = {}
        for a, (v, c) in enumerate(VERTS):
            sh = tuple(dmod(x) for x in v)
            for bi, j in enumerate(loc0):
                if abs(Hr[a, j]) > 1e-13:
                    bl.setdefault(sh, np.zeros((12, 12), complex))[CI[c], bi] += Hr[a, j]
        return bl
    return dict(C=C, L=L, OH=OH, psg=psg, lam=lam, tau=tau, U=Ug, shift=shift, dec_ok=dec_ok, flux_ok=flux_ok,
                W1=W1, CORN=CORN, CI=CI, VERTS=VERTS, nV=nV, DIRS=DIRS, H0mat=H0mat, blocks_from=blocks_from)


# ============================================================ block-space utilities (infinite lattice)
def act_blocks(D, g, h):
    M, l, U = D['OH'][g], D['lam'][g], D['U'][g]
    out = {}
    for d, B in h.items():
        dd = tuple(int(x) for x in M @ np.array(d))
        out[dd] = out.get(dd, 0) + ((-1.0) ** int(np.dot(l, d))) * (U @ B @ U.T)
    return out


def symmetrize(h, D, idx):
    acc = {}
    for g in idx:
        for d, B in act_blocks(D, g, h).items():
            acc[d] = acc.get(d, 0) + B / len(idx)
    herm = {}
    for d, B in acc.items():
        md = tuple(-x for x in d)
        herm[d] = herm.get(d, 0) + 0.5 * B
        herm[md] = herm.get(md, 0) + 0.5 * B.conj().T
    return {d: B for d, B in herm.items() if np.abs(B).max() > 1e-14}


def random_blocks(rng, r):
    return {d: rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12))
            for d in itertools.product(range(-r, r + 1), repeat=3)}


def Hk(h, ks):
    ks = np.atleast_2d(ks)
    out = np.zeros((len(ks), 12, 12), complex)
    for d, B in h.items():
        out += np.exp(-1j * ks @ np.array(d, float))[:, None, None] * B[None]
    return out


def wrap(k):
    return (np.asarray(k) + np.pi) % (2 * np.pi) - np.pi


def certify(h, nu, N):
    """Grid indirect gap between bands nu and nu+1 and a Lipschitz-certified lower bound for all k."""
    t = 2 * np.pi * np.arange(N) / N
    ks = np.array(list(itertools.product(t, t, t)))
    Emax, Emin = -np.inf, np.inf
    for chunk in np.array_split(ks, max(1, len(ks) // 4000)):
        e = np.linalg.eigvalsh(Hk(h, chunk))
        Emax = max(Emax, e[:, nu - 1].max()); Emin = min(Emin, e[:, nu].min())
    Lip = sum(np.linalg.norm(B, 2) * np.linalg.norm(d) for d, B in h.items())
    delta = np.sqrt(3) / 2 * 2 * np.pi / N          # covering radius of the grid (sup norm cell, Euclidean)
    return Emin - Emax, Emin - Emax - 2 * Lip * delta


# ============================================================ monomial operators (torus and Fock)
def mono_from_matrix(A):
    """A monomial matrix (one nonzero per column) -> (image index, amplitude) per column."""
    img = np.argmax(np.abs(A), axis=0)
    amp = A[img, np.arange(A.shape[1])]
    assert np.allclose(np.abs(amp), 1) and np.allclose(np.abs(A).sum(0), 1)
    return img, amp


def fock_mono(A):
    """Fock lift Gamma(A) of a one-particle monomial unitary A on n modes (Gamma|0> = |0>,
    Gamma c^dag_c Gamma^-1 = sum_j A_jc c^dag_j); states are bit strings, |s> = c^dag_{o1} c^dag_{o2} ... |0>
    with o1 < o2 < ... .  Returns (image state, amplitude) for every basis state."""
    pi, uc = mono_from_matrix(A); n = A.shape[0]; dim = 1 << n
    img = np.zeros(dim, np.int64); amp = np.zeros(dim, complex)
    for s in range(dim):
        occ = [c for c in range(n) if s >> c & 1]
        state = 0; a = 1.0 + 0j
        for o in reversed(occ):                       # rightmost creation operator acts first
            t = pi[o]
            a *= (-1) ** bin(state & ((1 << t) - 1)).count('1') * uc[o]
            state |= 1 << t
        img[s] = state; amp[s] = a
    return img, amp


def mono_compose(A, B):
    """(A B)|s> = amp_B[s] amp_A[img_B[s]] |img_A[img_B[s]]>."""
    ia, aa = A; ib, ab = B
    return ia[ib], ab * aa[ib]


# ============================================================ main
def main():
    t0 = time.time()
    D = build(); OH = D['OH']; U = D['U']; lam = D['lam']; sh = D['shift']; W1 = D['W1']
    PROPER = list(range(24)); ALL = list(range(48))
    def find(M): return [g for g in ALL if (OH[g] == np.array(M)).all()][0]
    c2x, c2y, c2z = find(np.diag([1, -1, -1])), find(np.diag([-1, 1, -1])), find(np.diag([-1, -1, 1]))
    D2 = [0, c2x, c2y, c2z]
    kst = np.array([1, -1, 1]) * np.pi / 2
    rng = np.random.default_rng(20261018)

    # ------------------------------------------------------------ A
    print("A. reduction to the infinite lattice")
    check("translation-invariant gauge reproduces the flux pattern; every O_h PSG lift on the L = 4 torus has the "
          "form (-1)^(lam.v + tau(c))", D['flux_ok'] and D['dec_ok'])
    h0 = D['blocks_from'](D['H0mat'](-1.0, 0.2))
    hr = symmetrize(random_blocks(rng, 2), D, ALL)
    ks = rng.uniform(-np.pi, np.pi, size=(20, 3)); okA = True
    for h in (h0, hr):
        Hks = Hk(h, ks)
        for g in ALL:
            okA &= np.allclose(Hk(h, (OH[g] @ ks.T).T + np.pi * sh[g]), U[g][None] @ Hks @ U[g].T[None], atol=1e-10)
    VERTS, CI = D['VERTS'], D['CI']
    def Bloch4(k):
        B = np.zeros((D['nV'], 12), complex)
        for a, (v, c) in enumerate(VERTS): B[a, CI[c]] = np.exp(1j * np.dot(k, v)) / np.sqrt(64)
        return B
    kk = np.array([1, 2, 3]) * np.pi / 2
    okT = np.allclose(Bloch4(kk).conj().T @ D['H0mat'](-1.0, 0.2) @ Bloch4(kk), Hk(h0, kk)[0])
    check("Bloch relation U_g H(k) U_g^T = H(g k + pi s_g) for all 48 g at 20 random continuous k (supplied H0 and "
          "a random O_h-symmetric range-2 H); L = 4 Bloch restriction of H0 agrees", okA and okT)
    nshift = sum(1 for g in PROPER if sh[g].any())
    N = 24; t = 2 * np.pi * np.arange(N) / N
    grid = np.array(list(itertools.product(t, t, t)))
    def fixed(idx):
        ok = np.ones(len(grid), bool)
        for g in idx:
            img = (OH[g] @ grid.T).T + np.pi * sh[g]
            ok &= np.all(np.abs(wrap(img - grid)) < 1e-9, axis=1)
        return grid[ok]
    FO = fixed(PROPER)
    fo_ok = len(FO) == 2 and {tuple(np.round(wrap(k) / np.pi, 6)) for k in FO} == {(0.5, -0.5, 0.5), (-0.5, 0.5, -0.5)}
    check("exactly 21 of the 24 proper rotations have a nonzero affine shift s_g; on the N = 24 grid only +-k* "
          "(k* = (pi/2, -pi/2, pi/2)) are fixed by all 24 affine maps k -> g k + pi s_g",
          nshift == 21 and fo_ok, f"shifted {nshift}; fixed {sorted(tuple(np.round(wrap(k)/np.pi, 3)) for k in FO)}")

    # ------------------------------------------------------------ B
    print("\nB. global anticommutation of commuting-C2 lifts")
    c2s = [g for g in PROPER if round(np.trace(OH[g])) == -1]
    pairs = [(a, b) for a, b in itertools.combinations(c2s, 2) if (OH[a] @ OH[b] == OH[b] @ OH[a]).all()]
    vpart_ok = all((((lam[b] + OH[b].T @ lam[a]) - (lam[a] + OH[a].T @ lam[b])) % 2 == 0).all() for a, b in pairs)
    fib_ok = all(np.array_equal(U[a] @ U[b], -(U[b] @ U[a])) for a, b in pairs)
    check("all 12 commuting pairs (a, b) of proper C2 rotations: the site-dependent signs agree, "
          "lam_b + R_b^T lam_a = lam_a + R_a^T lam_b (mod 2), and the fibre matrices anticommute exactly, "
          "U_a U_b = -U_b U_a; hence G_a G_b = -G_b G_a on all of l^2(Z^3) (x) C^12",
          len(pairs) == 12 and vpart_ok and fib_ok, f"pairs {len(pairs)}")
    # explicit L = 4 torus operators (monomial; even L keeps (-1)^(lam.v) periodic)
    L4 = 4; sites4 = list(itertools.product(range(L4), repeat=3)); si4 = {v: i for i, v in enumerate(sites4)}
    n4 = 12 * len(sites4)
    def G4(g):
        A = np.zeros((n4, n4))
        for v in sites4:
            w = tuple(int(x) % L4 for x in OH[g] @ np.array(v)); s = (-1.0) ** int(lam[g] @ np.array(v))
            A[12 * si4[w]:12 * si4[w] + 12, 12 * si4[v]:12 * si4[v] + 12] = s * U[g]
        return A
    G4s = [G4(g) for g in ALL]
    okB = all(np.allclose(G4s[a] @ G4s[b], -G4s[b] @ G4s[a]) for a, b in pairs)
    check("on the L = 4 torus the 768 x 768 operators satisfy G_a G_b = -G_b G_a for all 12 pairs", okB)

    # ------------------------------------------------------------ C
    print("\nC. even levels at momenta fixed by both C2s; odd-filling logic")
    FD2 = fixed(D2)
    pts8 = {tuple(s) for s in itertools.product((0.5, -0.5), repeat=3)}
    check("the momenta fixed by the D2 affine maps (C2x, C2y, C2z) on the N = 24 grid are exactly the 8 points "
          "(+-pi/2)^3", {tuple(np.round(wrap(k) / np.pi, 6)) for k in FD2} == pts8, f"{len(FD2)} points")
    okO, okD2, okLogic, gen = True, True, True, []
    for trial in range(6):
        r = 1 + trial % 2; sc = [0.05, 1.0, 10.0][trial % 3]
        hO = symmetrize({d: sc * B for d, B in random_blocks(rng, r).items()}, D, PROPER)
        hD = symmetrize({d: sc * B for d, B in random_blocks(rng, r).items()}, D, D2)
        for kk_ in (kst, -kst):
            okO &= all(m % 2 == 0 for m in mults(np.linalg.eigvalsh(Hk(hO, kk_)[0]), 1e-8 * sc))
        okD2 &= all(m % 2 == 0 for k in FD2 for m in mults(np.linalg.eigvalsh(Hk(hD, k)[0]), 1e-8 * sc))
        kg = rng.uniform(-np.pi, np.pi, 3)
        gen.append((max(mults(np.linalg.eigvalsh(Hk(hO, kg)[0]), 1e-8 * sc)),
                    max(mults(np.linalg.eigvalsh(Hk(hD, kg)[0]), 1e-8 * sc))))
        for h, kset in ((hO, [kst]), (hD, list(FD2))):
            for k in kset:
                e = np.linalg.eigvalsh(Hk(h, k)[0])
                okLogic &= all(abs(e[nu] - e[nu - 1]) < 1e-8 * sc for nu in range(1, 12, 2))
    check("6 random Hamiltonians symmetric under translations + 24 dressed rotations (range 1-2, scale 0.05-10): "
          "every level at k* and -k* has even multiplicity", okO)
    check("6 random Hamiltonians symmetric under translations + dressed D2 only: every level at all 8 points "
          "(+-pi/2)^3 has even multiplicity", okD2)
    check("control: at a random generic momentum both families have only simple levels",
          all(a == 1 and b == 1 for a, b in gen), f"max multiplicities {gen}")
    check("odd-filling logic: for every odd nu, E_nu(k) = E_{nu+1}(k) at k* (O) and at the 8 D2-fixed points (D2), so "
          "min_k E_{nu+1} - max_k E_nu <= 0: no band gap, no gapped Slater ground state at odd nu", okLogic)

    # ------------------------------------------------------------ D
    print("\nD. insulators at allowed fillings; site irreps")
    def site_irreps(idx, seed):
        rr = np.random.default_rng(seed)
        X = rr.normal(size=(12, 12)) + 1j * rr.normal(size=(12, 12)); X = X + X.conj().T
        Y = sum(U[g] @ X @ U[g].T for g in idx) / len(idx)
        return np.linalg.eigh(Y)
    ev, V = site_irreps(PROPER, 3)
    mO = mults(ev); start = 0; P2 = None
    for d_ in mO:
        if d_ == 2: P2 = V[:, start:start + 2] @ V[:, start:start + 2].conj().T; break
        start += d_
    hop = symmetrize(random_blocks(np.random.default_rng(11), 1), D, PROPER)
    nrm = max(np.linalg.norm(B, 2) for B in hop.values())
    h2 = {d: 0.02 * B / nrm for d, B in hop.items()}
    h2[(0, 0, 0)] = h2.get((0, 0, 0), 0) - P2
    ks = rng.uniform(-np.pi, np.pi, (10, 3))
    symB = all(np.allclose(U[g] @ P2 @ U[g].T, P2) for g in PROPER) and all(
        np.allclose(U[g] @ Hk(h2, k)[0] @ U[g].T, Hk(h2, OH[g] @ k + np.pi * sh[g])[0]) for g in PROPER for k in ks)
    gap2, cert2 = certify(h2, 2, 48)
    check("nu = 2 insulator in the class translations + 24 dressed rotations: on-site -P (P onto a 2-dim site irrep) "
          "+ symmetric range-1 hopping; Bloch symmetry verified; Lipschitz-certified global gap > 0 (N = 48 grid)",
          symB and cert2 > 0, f"grid gap {gap2:.4f}, certified >= {cert2:.4f}")
    ev1, V1 = site_irreps([0, c2x], 4)
    P1 = np.outer(V1[:, 0], V1[:, 0].conj())
    hop1 = symmetrize(random_blocks(np.random.default_rng(12), 1), D, [0, c2x])
    nrm1 = max(np.linalg.norm(B, 2) for B in hop1.values())
    h1 = {d: 0.02 * B / nrm1 for d, B in hop1.items()}
    h1[(0, 0, 0)] = h1.get((0, 0, 0), 0) - P1
    sym1 = all(np.allclose(U[g] @ Hk(h1, k)[0] @ U[g].T, Hk(h1, OH[g] @ k + np.pi * sh[g])[0]) for g in [0, c2x] for k in ks)
    gap1, cert1 = certify(h1, 1, 48)
    check("nu = 1 insulator with translations + dressed C2x only: certified global gap > 0 (no commuting C2 pair, "
          "so no obstruction)", sym1 and cert1 > 0, f"grid gap {gap1:.4f}, certified >= {cert1:.4f}")
    mOh = mults(site_irreps(ALL, 5)[0])
    def comm_dim(idx):
        A = np.vstack([np.kron(np.eye(12), U[g]) - np.kron(U[g].T, np.eye(12)) for g in idx])
        return 144 - np.linalg.matrix_rank(A)
    check("site irreps of the dressed operators (generic commutant splitting): O gives [2, 2, 4, 4], O_h gives "
          "[4, 4, 4]; so no O_h-symmetric on-site Slater state has N = 2 mod 4", sorted(mO) == [2, 2, 4, 4] and
          mOh == [4, 4, 4], f"O {mO} (commutant dim {comm_dim(PROPER)}); O_h {mOh} (commutant dim {comm_dim(ALL)})")

    # ------------------------------------------------------------ E
    print("\nE. twisted odd-L tori and the Fock-space (-1)^N relation")
    def qp_ops(L, theta):
        """Quasi-periodic states psi(w + L n) = e^{i theta.n} psi(w); operators restricted from the infinite lattice."""
        sites = list(itertools.product(range(L), repeat=3)); si = {v: i for i, v in enumerate(sites)}
        n = 12 * len(sites)
        def red(w):
            w = np.array(w); w0 = w % L; return tuple(int(x) for x in w0), (w - w0) // L
        def G(g):
            A = np.zeros((n, n), complex); Rinv = OH[g].T
            for w0 in sites:
                v = Rinv @ np.array(w0); v0, nn = red(v)
                A[12 * si[w0]:12 * si[w0] + 12, 12 * si[v0]:12 * si[v0] + 12] += \
                    (-1.0) ** int(lam[g] @ v) * np.exp(1j * np.dot(theta, nn)) * U[g]
            return A
        def H(h):
            A = np.zeros((n, n), complex)
            for w in sites:
                for d, B in h.items():
                    v0, nn = red(np.array(w) - np.array(d))
                    A[12 * si[w]:12 * si[w] + 12, 12 * si[v0]:12 * si[v0] + 12] += B * np.exp(1j * np.dot(theta, nn))
            return A
        return G, H
    hE = symmetrize(random_blocks(np.random.default_rng(2), 1), D, PROPER)
    for L, theta, lab in ((3, kst, 'k*'), (3, -kst, '-k*'), (1, kst, 'k*'), (1, -kst, '-k*')):
        G, H = qp_ops(L, theta); HL = H(hE); Gs = [G(g) for g in PROPER]
        uni = all(np.allclose(X.conj().T @ X, np.eye(len(HL))) for X in Gs)
        sym = [g for g in PROPER if np.allclose(Gs[g] @ HL, HL @ Gs[g], atol=1e-9)]
        pred = [g for g in PROPER if np.allclose(wrap(OH[g] @ theta + np.pi * L * (OH[g] @ lam[g]) - theta), 0, atol=1e-9)]
        ac = np.allclose(Gs[c2x] @ Gs[c2y], -Gs[c2y] @ Gs[c2x])
        ev = np.linalg.eigvalsh(HL)
        evn = all(m % 2 == 0 for m in mults(ev, 1e-8))
        # spectrum = union of H(k) over L k = theta (mod 2 pi)
        kset = [(theta + 2 * np.pi * np.array(nv)) / L for nv in itertools.product(range(L), repeat=3)]
        spec = np.sort(np.concatenate([np.linalg.eigvalsh(Hk(hE, k)[0]) for k in kset]))
        check(f"L = {L}, theta = {lab}: H Hermitian, the 24 dressed rotations unitary and all symmetries (= the set "
              f"predicted by R theta + pi L R lam = theta), C2x/C2y anticommute on the whole one-particle space, every "
              f"one-particle level even; spectrum = union of H(k) over L k = theta",
              np.allclose(HL, HL.conj().T) and uni and len(sym) == 24 and sorted(sym) == sorted(pred) and ac and evn
              and np.allclose(ev, spec), f"symmetric {len(sym)}/24")
    G, H = qp_ops(3, np.zeros(3)); HL = H(hE)
    broken = [g for g in PROPER if not np.allclose(G(g) @ HL, HL @ G(g), atol=1e-9)]
    check("control: L = 3 with theta = 0 -- exactly the 21 rotations with nonzero shift s_g fail to be symmetries",
          len(broken) == 21 and sorted(broken) == sorted(g for g in PROPER if sh[g].any()), f"{len(broken)} fail")
    # Fock space at L = 1 (12 modes, 4096 states), theta = k*
    G1, H1 = qp_ops(1, kst)
    G1s = [G1(g) for g in PROPER]
    F = [fock_mono(X) for X in G1s]
    Nn = np.array([bin(s).count('1') for s in range(1 << 12)])
    ab = mono_compose(F[c2x], F[c2y]); ba = mono_compose(F[c2y], F[c2x])
    rel = np.array_equal(ab[0], ba[0]) and np.allclose(ab[1], (-1.0) ** Nn * ba[1])
    hom = all((lambda P, Q: np.array_equal(P[0], Q[0]) and np.allclose(P[1], Q[1]))(
        mono_compose(F[a], F[b]), fock_mono(G1s[a] @ G1s[b])) for a, b in [(c2x, c2y), (c2y, c2x), (3, 7), (10, 20)])
    check("L = 1 twisted torus Fock space (4096 states): Gamma(G_a) Gamma(G_b) = Gamma(G_a G_b) (vacuum-fixing lift is "
          "multiplicative) and Gamma(C2x) Gamma(C2y) = (-1)^N Gamma(C2y) Gamma(C2x) exactly", rel and hom)
    # interacting symmetric Hamiltonians in fixed-N sectors (group average of a random Hermitian sector matrix)
    def sector_ops(Nf):
        states = [s for s in range(1 << 12) if Nn[s] == Nf]; idx = {s: i for i, s in enumerate(states)}
        mats = []
        for img, amp in F:
            A = np.zeros((len(states), len(states)), complex)
            for j, s in enumerate(states): A[idx[img[s]], j] = amp[s]
            mats.append(A)
        return mats
    res = {}
    for Nf in (2, 3, 4, 5):
        mats = sector_ops(Nf); dim = len(mats[0])
        rr = np.random.default_rng(100 + Nf)
        X = rr.normal(size=(dim, dim)) + 1j * rr.normal(size=(dim, dim)); X = X + X.conj().T
        Hs = sum(A @ X @ A.conj().T for A in mats) / len(mats)
        comm = all(np.allclose(A @ Hs, Hs @ A, atol=1e-8) for A in mats)
        res[Nf] = (comm, mults(np.linalg.eigvalsh(Hs), 1e-8))
    odd_ok = all(res[Nf][0] and all(m % 2 == 0 for m in res[Nf][1]) for Nf in (3, 5))
    even_ctrl = all(res[Nf][0] for Nf in (2, 4)) and any(1 in res[Nf][1] for Nf in (2, 4))
    check("L = 1, theta = k*: generic interacting N-conserving Hamiltonians commuting with all 24 Fock lifts have "
          "only even-degenerate levels in the N = 3 and N = 5 sectors; control: N = 2 or 4 sectors have simple levels",
          odd_ok and even_ctrl, f"ground multiplicities {{N: m}} = { {Nf: res[Nf][1][0] for Nf in res} }")

    # ------------------------------------------------------------ F
    print("\nF. doubled-cell class: dressed O_h about site 0 + even translations")
    box = np.array(list(itertools.product(range(-2, 3), repeat=3)))
    par = all(np.all(((OH[g] @ box.T).T.sum(1) - box.sum(1)) % 2 == 0) for g in ALL)
    check("every O_h element preserves the parity of x + y + z, so the class maps the even sublattice to itself", par)
    # free fermions: folded k* fibre of class-symmetric random L = 4 Hamiltonians (monomial actions by indexing)
    monoG = [mono_from_matrix(Gm) for Gm in G4s]
    def Tperm(tv):
        img = np.zeros(n4, np.int64)
        for v in sites4:
            w = tuple((x + y) % L4 for x, y in zip(v, tv)); img[12 * si4[v]:12 * si4[v] + 12] = 12 * si4[w] + np.arange(12)
        return img
    even_t = [tv for tv in sites4 if sum(tv) % 2 == 0]
    def conj_mono(A, img, amp):
        """M A M^dag for M|j> = amp_j |img_j>."""
        B = np.zeros_like(A); B[np.ix_(img, img)] = (amp[:, None] * A * amp.conj()[None, :]); return B
    def bloch4(k):
        B = np.zeros((n4, 12), complex)
        for v in sites4: B[12 * si4[v]:12 * si4[v] + 12, :] = np.exp(1j * np.dot(k, v)) * np.eye(12) / 8.0
        return B
    B2 = np.hstack([bloch4(kst), bloch4(-kst)])
    okF, mf = True, []
    for trial in range(2):
        rr = np.random.default_rng(300 + trial)
        A = rr.normal(size=(n4, n4)) + 1j * rr.normal(size=(n4, n4)); A = (A + A.conj().T) / 2
        A = sum(conj_mono(A, Tperm(tv), np.ones(n4)) for tv in even_t) / len(even_t)
        A = sum(conj_mono(A, img, amp) for img, amp in monoG) / 48
        sym = all(np.allclose(conj_mono(A, img, amp), A) for img, amp in monoG)
        oddbroken = not np.allclose(conj_mono(A, Tperm((1, 0, 0)), np.ones(n4)), A)
        sub = B2.conj().T @ A @ B2; leak = np.linalg.norm(A @ B2 - B2 @ sub)
        m_ = mults(np.linalg.eigvalsh(sub), 1e-8); mf.append(m_)
        okF &= sym and oddbroken and leak < 1e-8 and all(x % 4 == 0 for x in m_)
    check("free fermions in the doubled-cell class (random symmetric L = 4 Hamiltonians, odd translations broken): "
          "every level of the folded 24-state k* fibre has multiplicity divisible by 4, so odd nu per site admits no "
          "Slater band insulator in this class", okF, f"multiplicities {mf}")
    # two-fermion site states in 1-dim reps of the dressed O_h
    pairs2 = list(itertools.combinations(range(12), 2))
    def vec2mat(x):
        Mx = np.zeros((12, 12), complex)
        for (a, b), c in zip(pairs2, x): Mx[a, b] = c; Mx[b, a] = -c
        return Mx
    def mat2vec(Mx): return np.array([Mx[a, b] for a, b in pairs2])
    R2 = [np.array([mat2vec(U[g] @ vec2mat(e) @ U[g].T) for e in np.eye(66)]).T for g in ALL]
    mul = {(a, b): find(OH[a] @ OH[b]) for a in ALL for b in ALL}
    lin = all(np.allclose(R2[a] @ R2[b], R2[mul[(a, b)]]) for a in ALL for b in ALL)
    chi = np.array([(-1.0) ** (g >= 24) for g in ALL])     # 1-dim character of O_h: the improper sign
    Pch = sum(c * R for c, R in zip(chi, R2)) / 48
    evp, Vp = np.linalg.eigh((Pch + Pch.conj().T) / 2); Vs = Vp[:, evp > 0.5]
    psi = Vs[:, 0] if Vs.shape[1] else None
    rank = int(np.sum(np.linalg.svd(vec2mat(psi), compute_uv=False) > 1e-9)) if psi is not None else 0
    inv_ok = psi is not None and all(np.allclose(R2[g] @ psi, chi[g] * psi) for g in ALL)
    check("U (x) U on the 66-dim two-fermion site space is a linear O_h representation; it contains a state psi "
          "transforming by a 1-dim character, with antisymmetric coefficient rank > 2 (not a Slater determinant)",
          lin and inv_ok and rank > 2, f"invariant dim {Vs.shape[1]}, coefficient rank {rank}")
    Msite = vec2mat(psi)
    def pair_big(v):
        K = np.zeros((n4, n4), complex); i = si4[tuple(x % 4 for x in v)]
        K[12 * i:12 * i + 12, 12 * i:12 * i + 12] = Msite; return K
    even_sites = [v for v in sites4 if sum(v) % 2 == 0]
    okP = True
    for g in ALL:
        img, amp = monoG[g]
        for v in even_sites:
            Rv = tuple(int(x) % 4 for x in OH[g] @ np.array(v))
            okP &= np.allclose(conj_mono(pair_big(v), img, amp), chi[g] * pair_big(Rv))
    for tv in even_t[:6]:
        img = Tperm(tv)
        for v in even_sites[:4]:
            w = tuple((x + y) % 4 for x, y in zip(v, tv))
            okP &= np.allclose(conj_mono(pair_big(v), img, np.ones(n4)), pair_big(w))
    check("pair operators P_v^dag = (1/2) sum_ab psi_ab c^dag_{v,a} c^dag_{v,b} on even sites satisfy "
          "G_g P_v^dag G_g^-1 = chi_g P_{g v}^dag (all 48 g) and T_t P_v^dag T_t^-1 = P_{v+t}^dag (even t) on the "
          "L = 4 torus: the product state prod_{v even} P_v^dag |0> is symmetric (as a ray) and is a product of "
          "on-site states, the unique ground state of sum_even (1 - |psi><psi|_v) + sum_odd N_v (gap 1), filling 1 "
          "per site", okP)
    # scoping control: the cube-centre rotations (A2-staggered-mass group) are not in this class
    cc = np.array([0.5, 0.5, 0.5])
    tpar = [int(round(sum(cc - OH[g] @ cc))) % 2 for g in PROPER]
    check("scoping control: the 24 rotations about the cube centre c = (1/2,1/2,1/2), as maps (R, c - Rc), have "
          "integer-translation parity w1(R); the 12 w1-odd ones need an odd translation, so the cube-centre group "
          "(the A2-staggered-mass symmetry) is a different class from O_h about site 0 + even translations",
          tpar == [W1[g] for g in PROPER] and sum(W1) == 12, f"w1-odd count {sum(W1)}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   ({time.time() - t0:.0f} s)")


if __name__ == '__main__':
    main()
