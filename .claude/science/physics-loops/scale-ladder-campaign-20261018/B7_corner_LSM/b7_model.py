"""B7 shared model layer: the supplied corner fermion (flux square = plaquette = tube = pi,
triangle = 0, translation-invariant gauge) reduced to infinite-lattice data.

Builds, from the repository's reviewed definitions (L = 4 torus):
  * the translation-invariant Z2 gauge u (same GF(2) solve as the cross-rung runner);
  * for each of the 48 elements g of O_h about site 0 its PSG lift on the L = 4 torus and
    the decomposition  sigma_g(v, c) = lam_g . v + tau_g(c)  (mod 2), i.e. the operator
        G_g |v, c> = (-1)^(lam_g . v) (-1)^(tau_g(c)) |g v, g c>,
    with the k-independent fibre matrix U_g (12 x 12) and the affine momentum shift
    s_g = |g| lam_g (mod 2):   G_g maps the Bloch fibre k onto the fibre g k + pi s_g;
  * hopping blocks h_delta of the supplied Hamiltonian H0(t1, t2) (and of the runner's X);
  * a block-space symmetriser over any subgroup of O_h and H(k) = sum_delta h_delta e^{-i k.delta};
  * 2O / O character tables (copied from the cross-rung runner) for decompositions.
Nothing here is a claim; the checks live in the b7_*.py scripts.
"""
import itertools, os, sys
import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *(['..'] * 5)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))


def build():
    import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as _model
    C = _model._run_reviewed_program(definitions_only=True)
    L = C['L']; VERTS = C['VERTS']; nV = len(VERTS); CORN = C['CORNERS']; ROTS = C['ROTS']; DIRS = C['DIRS']
    F = dict(square=1, triangle=0, plaquette=1, tube=1)
    def dmod(x): return ((x + 1) % L) - 1

    # ---- translation-invariant gauge (verbatim logic of the cross-rung runner)
    def neg(d): return tuple(-x for x in d)
    def perp(d, e): return sum(a*b for a, b in zip(d, e)) == 0 and d != e
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
        return [ekey[(c1, c2, tuple(y - x for x, y in zip(p1, p2)))] for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1])]
    def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
    cell = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
    for d in DIRS:
        a = [f for f in DIRS if perp(f, d) and f != neg(d)]; a0 = a[0]
        b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]; ring = [a0, b0, neg(a0), neg(b0)]
        cell['square'].append(cyc([(frozenset((d, r)), Z0) for r in ring]))
        for i in range(4):
            p, q = ring[i], ring[(i+1) % 4]
            cell['tube'].append(cyc([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d), (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]))
    for s in itertools.product((1, -1), repeat=3):
        x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
        cell['triangle'].append(cyc([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]))
    for d, e in (((1,0,0),(0,1,0)), ((0,1,0),(0,0,1)), ((0,0,1),(1,0,0))):
        cell['plaquette'].append(cyc([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d), (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
    rows = []; rhs = []
    for k, cs in cell.items():
        for c in cs: rows.append(c); rhs.append(F[k])
    ucell = C['gf2_solve'](rows, rhs, nT)
    u = np.zeros(C['nE'], np.uint8)
    for key, i in C['EID'].items():
        a, b = tuple(key); (v, c), (w, c2) = VERTS[a], VERTS[b]
        u[i] = ucell[ekey[(c, c2, tuple(dmod(y - x) for x, y in zip(v, w)))]]
    flux_ok = all({int(sum(u[j] for j in c) % 2) for c in cs} == {F[k]} for k, cs in C['cycles'].items())

    # ---- O_h elements and their PSG lifts on the L = 4 torus
    OH = [R for R in ROTS] + [-R for R in ROTS]          # proper first, then I*R
    psg = [C['psg_sign'](lambda q, M=M: C['rot_vert'](M, q), u) for M in OH]
    CI = {c: i for i, c in enumerate(CORN)}
    E3 = np.eye(3, dtype=int)
    lam, tau, Ug = [], [], []
    dec_ok = True
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

    # ---- hopping blocks of H0 (onsite t1, link t2) read from the L = 4 matrix
    loc0 = [C['VID'][((0, 0, 0), c)] for c in CORN]
    def H0mat(t1, t2):
        H = np.zeros((nV, nV))
        for key in C['EDGES']:
            i, j = tuple(key); t = t1 if C['edges'][key] == 'onsite' else t2
            H[i, j] = H[j, i] = -t * (-1.0) ** u[C['EID'][key]]
        return H
    def blocks_from(Hr):
        """h[delta][a, b] = <delta, a| H |0, b> (range < L/2 assumed)."""
        bl = {}
        for a, (v, c) in enumerate(VERTS):
            sh = tuple(dmod(x) for x in v)
            for bi, j in enumerate(loc0):
                if abs(Hr[a, j]) > 1e-13:
                    bl.setdefault(sh, np.zeros((12, 12), complex))[CI[c], bi] += Hr[a, j]
        return bl
    return dict(C=C, L=L, u=u, flux_ok=flux_ok, OH=OH, psg=psg, lam=lam, tau=tau, U=Ug, shift=shift,
                dec_ok=dec_ok, W1=W1, CORN=CORN, CI=CI, loc0=loc0, H0mat=H0mat, blocks_from=blocks_from,
                VERTS=VERTS, nV=nV, DIRS=DIRS)


# ---------------- block-space utilities (infinite lattice)
def act_blocks(M, lamg, Ug_, h):
    """Image of the block family h under G_g:  (g.h)[M d] = (-1)^(lam.d) U h[d] U^dag."""
    out = {}
    for d, B in h.items():
        dd = tuple(int(x) for x in M @ np.array(d))
        out[dd] = out.get(dd, 0) + ((-1.0) ** int(np.dot(lamg, d))) * (Ug_ @ B @ Ug_.conj().T)
    return out


def symmetrize(h, D, idx):
    """Average the block family over the O_h elements with indices idx; also Hermitise."""
    acc = {}
    for g in idx:
        for d, B in act_blocks(D['OH'][g], D['lam'][g], D['U'][g], h).items():
            acc[d] = acc.get(d, 0) + B / len(idx)
    herm = {}
    for d, B in acc.items():
        md = tuple(-x for x in d)
        herm[d] = herm.get(d, 0) + 0.5 * B
        herm[md] = herm.get(md, 0) + 0.5 * B.conj().T
    return {d: B for d, B in herm.items() if np.abs(B).max() > 1e-14}


def random_blocks(rng, r, cplx=True):
    h = {}
    for d in itertools.product(range(-r, r + 1), repeat=3):
        if max(abs(x) for x in d) > r: continue
        B = rng.normal(size=(12, 12)) + (1j * rng.normal(size=(12, 12)) if cplx else 0)
        h[d] = B
    return h


def Hk(h, ks):
    """Bloch Hamiltonian H(k) = sum_d h_d e^{-i k.d} for an array of momenta ks (n, 3)."""
    ks = np.atleast_2d(ks)
    out = np.zeros((len(ks), 12, 12), complex)
    for d, B in h.items():
        out += np.exp(-1j * ks @ np.array(d, float))[:, None, None] * B[None]
    return out


def lipschitz(h):
    return sum(np.linalg.norm(B, 2) * np.linalg.norm(d) for d, B in h.items())


def add(h1, h2, a=1.0, b=1.0):
    out = {}
    for d, B in h1.items(): out[d] = out.get(d, 0) + a * B
    for d, B in h2.items(): out[d] = out.get(d, 0) + b * B
    return out


def kgrid(N):
    t = 2 * np.pi * np.arange(N) / N
    return np.array(list(itertools.product(t, t, t)))


# ---------------- binary octahedral machinery (from the cross-rung runner)
def two_O(D):
    ROTS = D['OH'][:24]
    def q2su(qv):
        a, b, c, d = qv; return np.array([[a+1j*b, c+1j*d], [-c+1j*d, a-1j*b]])
    qs = []
    for i in range(4):
        for s_ in (1, -1):
            vv = [0]*4; vv[i] = s_; qs.append(vv)
    for sg in itertools.product((1, -1), repeat=4): qs.append([x/2 for x in sg])
    for i, j in itertools.combinations(range(4), 2):
        for si, sj in itertools.product((1, -1), repeat=2):
            vv = [0]*4; vv[i], vv[j] = si/np.sqrt(2), sj/np.sqrt(2); qs.append(vv)
    G2 = [q2su(qv) for qv in qs]
    PAU = [np.array([[0,1],[1,0]]), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]])]
    def so3(U): return np.rint(np.array([[0.5*np.real(np.trace(PAU[i]@U@PAU[j]@U.conj().T)) for j in range(3)] for i in range(3)])).astype(int)
    def rid(R): return [k for k, S in enumerate(ROTS) if (S == R).all()][0]
    proj = [rid(so3(U)) for U in G2]
    def gidx(U): return [k for k, Vv in enumerate(G2) if np.allclose(U, Vv)][0]
    def spin_char(j2, U):
        tr = max(-1, min(1, np.real(np.trace(U)) / 2)); th = 2 * np.arccos(tr)
        if abs(np.sin(th / 2)) < 1e-12: return float(j2 + 1) * (1 if np.isclose(tr, 1) else (-1) ** j2)
        return np.sin((j2 + 1) * th / 2) / np.sin(th / 2)
    W1 = D['W1']
    G32 = np.array([spin_char(3, U) for U in G2])
    IRR = {'E1/2': np.array([spin_char(1, U) for U in G2]), 'E5/2': np.array([spin_char(5, U) for U in G2]) - G32, 'G3/2': G32}
    A2c = np.array([(-1.0) ** W1[proj[e]] for e in range(48)])
    T1c = np.array([spin_char(2, U) for U in G2]); T2c = A2c * T1c
    IRR.update({'A1': np.ones(48), 'A2': A2c, 'T1': T1c, 'T2': T2c, 'E': np.array([spin_char(4, U) for U in G2]) - T2c})
    # a genuine 2O representation on the fibre: twisted U's with GF(2)-solved signs
    C = D['C']
    Ml = [D['U'][k] * (1j ** W1[k]) for k in range(24)]
    sec = [proj.index(k) for k in range(24)]
    rows = []; rhs = []
    for a in range(24):
        for b in range(24):
            prod = G2[sec[a]] @ G2[sec[b]]; ab = proj[gidx(prod)]
            w = 0 if np.allclose(prod, G2[sec[ab]]) else 1
            X, Y = Ml[a] @ Ml[b], Ml[ab]
            e = 0 if np.allclose(X, Y) else (1 if np.allclose(X, -Y) else None)
            assert e is not None
            cnt = {}
            for x in (a, b, ab): cnt[x] = cnt.get(x, 0) ^ 1
            rows.append([x for x, v in cnt.items() if v]); rhs.append(e ^ w)
    beta = C['gf2_solve'](rows, rhs, 24)
    lift = None
    if beta is not None:
        lift = [((-1.0) ** int(beta[proj[k]])) * (1 if np.allclose(G2[k], G2[sec[proj[k]]]) else -1) * Ml[proj[k]] for k in range(48)]
    def decompose_chars(ch):
        d = {k: int(round(np.real(sum(np.conj(IRR[k][e]) * ch[e] for e in range(48))) / 48)) for k in IRR}
        return {k: n for k, n in d.items() if n}
    return dict(G2=G2, proj=proj, gidx=gidx, IRR=IRR, lift=lift, decompose_chars=decompose_chars, sec=sec)


# ---------------- exact operator algebra for site groups of affine maps (M, t)
def wy_op(D, g, t):
    """T_t G_g as (M, t, lam mod 2, U, phase); acts |v>phi -> phase (-1)^(lam.v) |M v + t> U phi."""
    return (D['OH'][g], np.array(t, int), D['lam'][g] % 2, D['U'][g].astype(complex), 1.0 + 0j)


def wy_comp(o2, o1):
    M2, t2, l2, U2, p2 = o2; M1, t1, l1, U1, p1 = o1
    return (M2 @ M1, M2 @ t1 + t2, (l1 + M1.T @ l2) % 2, U2 @ U1, p1 * p2 * (-1.0) ** int(np.dot(l2, t1)))


def wy_ratio(oa, ob):
    Ma, ta, la, Ua, pa = oa; Mb, tb, lb, Ub, pb = ob
    assert (Ma == Mb).all() and (ta == tb).all() and ((la - lb) % 2 == 0).all()
    X = pa * Ua; Y = pb * Ub; r = np.vdot(Y.ravel(), X.ravel()) / np.vdot(Y.ravel(), Y.ravel())
    assert np.allclose(X, r * Y); return r


def site_group(D, w, idx):
    out = []
    for g in idx:
        Mw = [sum(int(D['OH'][g][i, j]) * w[j] for j in range(3)) for i in range(3)]
        t = [w[i] - Mw[i] for i in range(3)]
        if all(x.denominator == 1 for x in t): out.append((g, [int(x) for x in t]))
    return out


def wyckoff_class(D, w, idx):
    """Site group of the point w (Fractions) and the commuting pairs whose dressed operators anticommute."""
    S = site_group(D, w, idx); ops = [wy_op(D, g, t) for g, t in S]; bad = []
    for (a, oa), (b, ob) in itertools.combinations(list(enumerate(ops)), 2):
        ab, ba = wy_comp(oa, ob), wy_comp(ob, oa)
        if (ab[0] == ba[0]).all() and (ab[1] == ba[1]).all():
            r = wy_ratio(ab, ba)
            if not np.isclose(r, 1): bad.append((S[a][0], S[b][0], np.round(r, 6)))
    return S, bad
