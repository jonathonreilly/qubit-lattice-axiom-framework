#!/usr/bin/env python3
"""Scale-ladder cross-rung invariants of the supplied corner-fermion model.

Four matching checks between the lattice rung (corner fermion with its
projective symmetry group) and the long-wavelength rung (Weyl/Dirac node
quartet at the rotation-fixed momenta), on the L = 4 torus:
  1. UV gauge data becomes IR momentum: rotations act as k -> R k + pi s_R,
     and exactly k* and -k* are fixed;
  2. class transport: the whole twelve-state space at k* is spinorial (the
     central element of the binary octahedral lift acts as -1), so EVERY
     Hamiltonian commuting with the gauge-dressed rotations and the translations,
     at any strength and range on the torus, has only even, spinorial levels
     at k*;
  3. emergent isotropy: the Weyl cone is isotropic at linear order and its
     anisotropy grows as |q|^2 (suppression (a/w)^2 for a packet of width w);
  4. naturalness: with the site rotations and the site inversion kept, every
     level of the folded Hamiltonian at k* keeps multiplicity divisible by 4 under strong
     symmetric staggered and uniform perturbations (no quartet splitting at any
     order), and an A2 breaking of strength eps opens a gap linear in eps.
Supplied model only; no physical identification.
Companion: docs/SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md
"""
import itertools, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def main():
    global PASS, FAIL
    import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as _model
    C = _model._run_reviewed_program(definitions_only=True)

    PASS = FAIL = 0
    def check(name, ok, detail=''):
        global PASS, FAIL
        PASS += bool(ok); FAIL += (not ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

    L = C['L']; VERTS = C['VERTS']; nV = len(VERTS); CORN = C['CORNERS']; ROTS = C['ROTS']
    F = dict(square=1, triangle=0, plaquette=1, tube=1)
    def dmod(x): return ((x + 1) % L) - 1

    # ---------------- translation-invariant gauge (one-site cell), mapped to the L = 4 lattice
    DIRS = C['DIRS']
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
    check("translation-invariant gauge on the L = 4 lattice reproduces the flux pattern",
          all({int(sum(u[j] for j in c) % 2) for c in cs} == {F[k]} for k, cs in C['cycles'].items()))

    INVM = -np.eye(3, dtype=int)
    psg = lambda f: C['psg_sign'](f, u)
    rots = [psg(lambda q, M=R: C['rot_vert'](M, q)) for R in ROTS]
    invs = [psg(lambda q, M=R @ INVM: C['rot_vert'](M, q)) for R in ROTS]
    TV = list(itertools.product(range(L), repeat=3))
    trans = [psg(lambda q, t=t: C['trans_vert'](t, q)) for t in TV]
    check("rotations, inversion and translations all have PSG lifts; translations act without gauge signs",
          all(s is not None for P, s in rots + invs + trans) and all(len(set(s.tolist())) == 1 for P, s in trans))
    def conj(Xm, P, s):
        sg = (-1.0) ** s; Y = np.zeros_like(Xm); Y[np.ix_(P, P)] = Xm * np.outer(sg, sg); return Y
    def w1(R):
        p = [DIRS.index(tuple(int(x) for x in R @ np.array(d))) for d in DIRS]; sgn = 1
        for i in range(6):
            while p[i] != i:
                j = p[i]; p[i], p[j] = p[j], p[i]; sgn = -sgn
        return 0 if sgn == 1 else 1
    W1 = [w1(R) for R in ROTS]
    def sym(Xm, Qmom=False, a2=False, inversion=False):
        Y = np.zeros_like(Xm)
        for (P, s), t in zip(trans, TV): Y += ((-1.0) ** sum(t) if Qmom else 1.0) * conj(Xm, P, s)
        Z = np.zeros_like(Xm)
        for (P, s), w in zip(rots, W1): Z += ((-1.0) ** w if a2 else 1.0) * conj(Y, P, s)
        if inversion:
            Z2 = np.zeros_like(Z)
            for P, s in invs[:1]: Z2 += conj(Z, P, s)
            Z = (Z + Z2) / 2
        return Z
    loc0 = [C['VID'][((0, 0, 0), c)] for c in CORN]; CI = {c: i for i, c in enumerate(CORN)}
    def H0(t1, t2):
        H = np.zeros((nV, nV))
        for key in C['EDGES']:
            i, j = tuple(key); t = t1 if C['edges'][key] == 'onsite' else t2
            H[i, j] = H[j, i] = -t * (-1.0) ** u[C['EID'][key]]
        return H
    def blocks_from(Hr):
        bl = {}
        for a, v in enumerate(VERTS):
            sh = tuple(dmod(x) for x in v[0])
            for bi, j in enumerate(loc0):
                if abs(Hr[a, j]) > 1e-12: bl.setdefault(sh, np.zeros((12, 12), complex))[CI[v[1]], bi] += Hr[a, j]
        return bl
    def Hk(bl, k):
        H = np.zeros((12, 12), complex)
        for sh, M in bl.items(): H += M * np.exp(1j * np.dot(k, sh))
        return H
    kst = np.array([1, -1, 1]) * np.pi / 2; Q = np.array([np.pi] * 3)

    # ---------------- rung-0 data: the supplied conjugation-odd O x I invariant term X (as in the Dirac-pair note)
    rng = np.random.default_rng(0)
    nbr = [C['VID'][(tuple(x % L for x in d), c)] for d in [(0,0,0)] + list(DIRS) for c in CORN]
    basis = []
    for trial in range(14):
        A = np.zeros((nV, nV))
        for i in loc0:
            for j in nbr:
                v, w = VERTS[i][0], VERTS[j][0]
                dd = [abs(dmod(y - x)) for x, y in zip(v, w)]
                if i != j and sum(dd) <= 1: A[i, j] = rng.normal()
        A = A - A.T
        basis.append(sym(1j * A, inversion=True))
    sv = np.linalg.svd(np.array([b.ravel() for b in basis]), compute_uv=False)
    dimX = int(np.sum(sv > 1e-8 * sv[0]))
    X = basis[0] / np.abs(basis[0]).max()
    Hb = H0(-1.0, 0.2) + 0.05 * X
    bl = blocks_from(Hb); f = lambda k: Hk(bl, k)

    # ---------------- binary octahedral machinery (as in the Dirac-pair note)
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
    def opmat(k):
        P, s = rots[k]; M = np.zeros((nV, nV)); M[P, np.arange(nV)] = (-1.0) ** s; return M * (1j ** W1[k])
    Mf = [opmat(k) for k in range(24)]
    def chars(Vs, elems):
        Rm = {k: Vs.conj().T @ Mf[k] @ Vs for k in set(proj[e] for e in elems)}
        sec = {}
        for e in elems: sec.setdefault(proj[e], e)
        Rs = sorted(sec); idx = {R: i for i, R in enumerate(Rs)}; rows = []; rhs = []
        for a in Rs:
            for b in Rs:
                g = gidx(G2[sec[a]] @ G2[sec[b]]); ab = proj[g]; wv = 0 if g == sec[ab] else 1
                Xm, Ym = Rm[a] @ Rm[b], Rm[ab]
                e = 0 if np.allclose(Xm, Ym) else (1 if np.allclose(Xm, -Ym) else None)
                if e is None: return None
                cnt = {}
                for x in (idx[a], idx[b], idx[ab]): cnt[x] = cnt.get(x, 0) ^ 1
                rows.append([x for x, vv in cnt.items() if vv]); rhs.append(e ^ wv)
        beta = C['gf2_solve'](rows, rhs, len(Rs))
        if beta is None: return None
        return {e: ((-1.0) ** int(beta[idx[proj[e]]])) * (1 if e == sec[proj[e]] else -1) * np.trace(Rm[proj[e]]) for e in elems}
    def spin_char(j2, U):
        tr = max(-1, min(1, np.real(np.trace(U)) / 2)); th = 2 * np.arccos(tr)
        if abs(np.sin(th / 2)) < 1e-12: return float(j2 + 1) * (1 if np.isclose(tr, 1) else (-1) ** j2)
        return np.sin((j2 + 1) * th / 2) / np.sin(th / 2)
    G32 = np.array([spin_char(3, U) for U in G2])
    IRR = {'E1/2': np.array([spin_char(1, U) for U in G2]), 'E5/2': np.array([spin_char(5, U) for U in G2]) - G32, 'G3/2': G32}
    allO = list(range(48)); Tel = [e for e in allO if W1[proj[e]] == 0]
    A2c = np.array([(-1.0) ** W1[proj[e]] for e in allO])
    T1c = np.array([spin_char(2, U) for U in G2]); T2c = A2c * T1c
    IRR.update({'A1': np.ones(48), 'A2': A2c, 'T1': T1c, 'T2': T2c, 'E': np.array([spin_char(4, U) for U in G2]) - T2c})
    def decompose(Vs):
        ch = chars(Vs, allO)
        if ch is None: return None
        d = {k: int(round(np.real(sum(np.conj(IRR[k][e]) * ch[e] for e in allO)) / 48)) for k in IRR}
        return {k: n for k, n in d.items() if n}
    SPIN = {'E1/2', 'E5/2', 'G3/2'}
    def Bloch(k):
        B = np.zeros((nV, 12), complex)
        for a, (v, c) in enumerate(VERTS): B[a, CI[c]] = np.exp(1j * np.dot(k, v)) / np.sqrt(L ** 3)
        return B
    def levels(ev, tol=1e-8):
        out = []; i = 0
        while i < len(ev):
            j = i
            while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol: j += 1
            out.append((i, j + 1)); i = j + 1
        return out

    # ---------------- Part 1: UV gauge data becomes IR crystal momentum
    print("Part 1: rotations act on crystal momentum affinely, k -> R k + pi s_R")
    KS = [np.array(t) * 2 * np.pi / L for t in TV]; BK = [Bloch(k) for k in KS]; BALL = np.hstack(BK)
    image = {}; affine = True; shifts = {}
    for r in range(24):
        Y = np.abs(BALL.conj().T @ Mf[r] @ BALL) ** 2
        Wb = Y.reshape(len(KS), 12, len(KS), 12).sum(axis=(1, 3))
        for i, k in enumerate(KS):
            w = Wb[:, i]
            j = int(np.argmax(w)); affine &= abs(w[j] - 12) < 1e-8; image[(r, i)] = j
            s = np.rint((KS[j] - ROTS[r] @ k) / np.pi).astype(int) % 2
            shifts.setdefault(r, set()).add(tuple(s))
    one_shift = all(len(v) == 1 for v in shifts.values())
    check("every twisted rotation maps each Bloch space onto exactly one Bloch space, with a single shift s_R per rotation (k -> R k + pi s_R)",
          affine and one_shift, f"distinct shift vectors {sorted(set(next(iter(v)) for v in shifts.values()))}")
    fixed = [i for i in range(len(KS)) if all(image[(r, i)] == i for r in range(24))]
    fixedk = sorted(tuple(np.round(((KS[i] + np.pi) % (2 * np.pi) - np.pi) / (np.pi / 2)).astype(int)) for i in fixed)
    kidx = lambda k: [i for i, q in enumerate(KS) if np.allclose(np.exp(1j * (q - k)), 1)][0]
    check("exactly two momenta are fixed by all 24 rotations: k* = (pi/2)(1,-1,1) and -k* (UV PSG data -> IR valley position)",
          sorted(fixed) == sorted([kidx(kst), kidx(-kst)]), f"fixed momenta in units of pi/2: {fixedk}")

    # ---------------- Part 2: class transport to the fixed momentum
    print("\nPart 2: the fixed-momentum space carries only the spin-1/2 class, for every symmetric Hamiltonian")
    Bst = BK[kidx(kst)]; Bmst = BK[kidx(-kst)]
    dk, dmk = decompose(Bst), decompose(Bmst)
    check("the twelve Bloch states at k* and at -k* each form a linear representation of the binary octahedral group "
          "in which the central element acts as -1 (all spinorial)",
          dk is not None and dmk is not None and set(dk) <= SPIN and set(dmk) <= SPIN, f"k*: {dk}; -k*: {dmk}")
    rng2 = np.random.default_rng(11); ok_even = True; ok_spin = True; mults = []; gam = []
    for trial in range(6):
        A = np.zeros((nV, nV), complex)
        A[loc0, :] = rng2.normal(size=(12, nV)) + 1j * rng2.normal(size=(12, nV)) * (trial % 2)
        Hs = sym(A + A.conj().T); Hs /= np.abs(Hs).max()
        Hr2 = H0(-1.0, 0.2) + 1.0 * Hs
        ok_sym = all(np.allclose(conj(Hr2, P, s), Hr2) for P, s in rots + trans[:3])
        ev, W = np.linalg.eigh(Bst.conj().T @ Hr2 @ Bst)
        ms = []
        for a, b in levels(ev):
            ms.append(b - a); ok_even &= (b - a) % 2 == 0
            d = decompose(Bst @ W[:, a:b]); ok_spin &= d is not None and set(d) <= SPIN and ok_sym
        mults.append(ms)
        gam.append([b - a for a, b in levels(np.linalg.eigvalsh(BK[0].conj().T @ Hr2 @ BK[0]))])
    check("six random Hamiltonians commuting with the rotations and translations (strength 1, every range on the torus, "
          "real and complex) have only even, spinorial levels at k*", ok_even and ok_spin, f"multiplicities {mults[:2]} ...")
    check("control: at Gamma, which is not rotation-fixed, the same Hamiltonians have odd multiplicities",
          any(m % 2 for g in gam for m in g), f"Gamma multiplicities {gam[0]}")

    # ---------------- Part 3: emergent isotropy
    print("\nPart 3: emergent isotropy of the Weyl cone (t1 = -1, t2 = 0.2, X strength 0.05)")
    eK = np.linalg.eigvalsh(f(kst)); EN = eK[0]
    dirs = np.vstack([np.eye(3), np.array(list(itertools.product((1, -1), repeat=3))) / np.sqrt(3),
                      rng2.normal(size=(40, 3))]); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    aniso = []; speeds = []
    for dq in (0.04, 0.02, 0.01):
        sp = []
        for d in dirs:
            e = np.linalg.eigvalsh(f(kst + dq * d)); sp.append((e[1] - e[0]) / (2 * dq))
        speeds.append(np.mean(sp)); aniso.append(np.ptp(sp) / np.mean(sp))
    ratios = [aniso[i] / aniso[i + 1] for i in range(2)]
    check("the cone speed is isotropic at linear order and its relative anisotropy falls as |q|^2 "
          "(ratios ~4 per halving): a packet of width w sees anisotropy ~ (a/w)^2",
          all(abs(x - 4) < 0.3 for x in ratios) and aniso[0] > 1e-6, f"anisotropy {np.array(aniso)}, ratios {np.round(ratios, 3)}, v -> {speeds[-1]:.6f}")

    # ---------------- Part 4: naturalness of the Dirac mass
    print("\nPart 4: the Dirac mass is protected by site rotations x site inversion at every strength")
    B2 = np.hstack([Bst, Bmst])
    def onsite_seed(kind):
        A = rng2.normal(size=(12, 12)); A = (A + A.T) if kind == 'real' else (A - A.T)
        S = np.zeros((nV, nV), complex); S[np.ix_(loc0, loc0)] = (1 if kind == 'real' else 1j) * A; return S
    def full_seed():
        A = np.zeros((nV, nV), complex); A[loc0, :] = rng2.normal(size=(12, nV)) + 1j * rng2.normal(size=(12, nV)); return A + A.conj().T
    def nrm(M): return M / np.abs(M).max()
    Mm = sym(onsite_seed('imag'), Qmom=True, a2=True); Mm = nrm((Mm + Mm.conj().T) / 2)
    ok4 = True; info = []
    for trial in range(3):
        Bg = Hb + 0.3 * nrm(sym(full_seed(), inversion=True)) + 0.3 * nrm(sym(full_seed(), Qmom=True, inversion=True))
        ev = np.linalg.eigvalsh(B2.conj().T @ Bg @ B2)
        ms = [b - a for a, b in levels(ev)]; ok4 &= all(m % 4 == 0 for m in ms); info.append(ms)
    check("with strong (0.3) random uniform and staggered terms invariant under site rotations, site inversion and the "
          "translations (up to the staggered sign), every level of the folded Hamiltonian at k* has multiplicity divisible by 4: no quartet splitting at any order",
          ok4, f"multiplicities {info[0]}")
    ev0, W0 = np.linalg.eigh(B2.conj().T @ Bg @ B2); lv = levels(ev0)
    gaps = []
    for eps in (2e-3, 1e-3, 5e-4):
        e = np.linalg.eigvalsh(B2.conj().T @ (Bg + eps * Mm) @ B2)
        gaps.append(np.array([e[a + 2] - e[a + 1] for a, b in lv]) / eps)
    lin = np.allclose(gaps[1], gaps[2], rtol=2e-3, atol=1e-6) and np.allclose(gaps[0], gaps[1], rtol=4e-3, atol=1e-6)
    check("an A2 (site-rotation-to-T) breaking of strength eps splits the quartets into doublets with a gap linear in eps "
          "('t Hooft-natural small mass)", lin and np.max(gaps[-1]) > 1e-2, f"gap/eps per quartet {np.round(gaps[-1], 4)}")
    Bo = Hb + 0.3 * nrm(sym(full_seed(), Qmom=True))
    ev = np.linalg.eigvalsh(B2.conj().T @ Bo @ B2); ms = [b - a for a, b in levels(ev)]
    check("control: keeping the rotations but breaking the inversion leaves every level even (pinned Weyl doublets) "
          "but separates the two valleys in energy (some levels 2-fold)", all(m % 2 == 0 for m in ms) and any(m % 4 for m in ms),
          f"multiplicities {ms}")

    # ---------------- Part 5: what fixes a common speed across fields
    print("\nPart 5: invariant kinetic tensors with and without time on the same footing as space")
    def signed_perms(n, fixed_last=False):
        out = []
        for p in itertools.permutations(range(n - 1 if fixed_last else n)):
            for sg in itertools.product((1, -1), repeat=n):
                M = np.zeros((n, n))
                for i, j in enumerate(p): M[i, j] = sg[i]
                if fixed_last: M[n - 1, n - 1] = sg[n - 1]
                out.append(M)
        return out
    def n_invariant_sym2(G, n):
        rows = []
        for _ in range(12):
            A = rng2.normal(size=(n, n)); A = A + A.T
            rows.append(sum(g @ A @ g.T for g in G).ravel())
        sv = np.linalg.svd(np.array(rows), compute_uv=False); return int(np.sum(sv > 1e-9 * sv[0]))
    B4 = signed_perms(4); OhT = signed_perms(4, fixed_last=True)
    nB4, nOhT = n_invariant_sym2(B4, 4), n_invariant_sym2(OhT, 4)
    check("symmetric rank-2 tensors on (t,x,y,z): the 4D hyperoctahedral group (384 elements) leaves one invariant (a common "
          "speed for every field), spatial O_h x time reversal (96) leaves two (each field's speed is a free parameter)",
          len(B4) == 384 and len(OhT) == 96 and nB4 == 1 and nOhT == 2, f"{nB4} vs {nOhT}")

    # ---------------- Part 6: parameter-free step rules (no tunable couplings)
    print("\nPart 6: parameter-free local step rules fix the speed from the grid alone")
    s3 = np.sqrt(3)
    def omega_dp(k):    # minimal Weyl automaton (D'Ariano-Perinotti 2014, BCC lattice)
        c, s = np.cos(k / s3), np.sin(k / s3)
        return np.arccos(np.clip(c[0]*c[1]*c[2] - s[0]*s[1]*s[2], -1, 1))
    dq = rng2.normal(size=(300, 3)); dq /= np.linalg.norm(dq, axis=1)[:, None]
    sp = {q: np.array([omega_dp(q * d) / q for d in dq]) for q in (0.02, 0.01, 0.005)}
    an = [np.ptp(sp[q]) / sp[q].mean() for q in (0.02, 0.01, 0.005)]
    vmax = 0.0
    for k in rng2.uniform(-np.pi * s3, np.pi * s3, size=(3000, 3)):
        g = [(omega_dp(k + 1e-6 * e) - omega_dp(k - 1e-6 * e)) / 2e-6 for e in np.eye(3)]; vmax = max(vmax, np.linalg.norm(g))
    kmax = s3 * np.array([3 * np.pi / 4, -np.pi / 4, 5 * np.pi / 4])
    gmax = np.array([(omega_dp(kmax + 1e-6 * e) - omega_dp(kmax - 1e-6 * e)) / 2e-6 for e in np.eye(3)])
    vcomp = 0.0
    for k in rng2.uniform(-np.pi * s3, np.pi * s3, size=(3000, 3)):
        g = [(omega_dp(k + 1e-6 * e) - omega_dp(k - 1e-6 * e)) / 2e-6 for e in np.eye(3)]; vcomp = max(vcomp, np.max(np.abs(g)))
    kk = np.array([0.3, 0.2, 0.1]); edge = np.array([kk[1], kk[0], -kk[2]]); cyc3 = np.array([kk[1], kk[2], kk[0]])
    check("minimal Weyl automaton: speed 1/sqrt3 with no parameter; fastest group speed 1/sqrt2 and every component within the one-step "
          "cone 1/sqrt3; anisotropy linear in |k| because its dispersion is invariant under C3 but not under the w1-odd edge C2",
          abs(sp[0.005].mean() - 1 / s3) < 1e-4 and abs(sp[0.005].mean() - 1 / s3) < abs(sp[0.02].mean() - 1 / s3)
          and abs(np.linalg.norm(gmax) - 1 / np.sqrt(2)) < 1e-6 and vmax <= 1 / np.sqrt(2) + 1e-9 and vcomp <= 1 / s3 + 1e-6
          and all(abs(an[i] / an[i + 1] - 2) < 0.05 for i in range(2))
          and abs(omega_dp(kk) - omega_dp(cyc3)) < 1e-12 and abs(omega_dp(kk) - omega_dp(edge)) > 1e-4,
          f"v = {sp[0.005].mean():.7f}, group speed at the maximiser {np.linalg.norm(gmax):.6f}, sampled max component {vcomp:.4f}, anisotropy {np.round(an, 5)}")
    RLr = H0(0.0, 1.0) / np.sqrt(2)
    won, Von = np.linalg.eigh(Bloch(np.zeros(3)).conj().T @ H0(1.0, 0.0) @ Bloch(np.zeros(3)))
    P2 = Von[:, np.abs(won - 2) < 1e-6]; Uc = np.eye(12) - 2 * P2 @ P2.conj().T
    Uon = np.zeros((nV, nV), complex)
    for v in range(L ** 3):
        idx = [C['VID'][(TV[v], c)] for c in CORN]; Uon[np.ix_(idx, idx)] = Uc
    Wr = RLr @ Uon
    ok_rule = (np.allclose(RLr @ RLr, np.eye(nV)) and np.allclose(Uon @ Uon, np.eye(nV)) and P2.shape[1] == 4
               and all(np.allclose(conj(Wr, P, s), Wr) for P, s in rots + trans[:5]))
    check("the corner step W = (link hopping / sqrt2) x (reflection about the eigenvalue-2 space of the on-site corner hopping) "
          "is an exact local unitary with no parameter, built from two reflections, commuting with the gauge-dressed rotations and translations",
          ok_rule, f"on-site eigenvalues {np.round(sorted(set(np.round(won, 6))), 4)}")
    blW = blocks_from(Wr); blL = blocks_from(RLr)
    Wk = lambda k: Hk(blL, k) @ Uc
    check("the Bloch step reproduces the real-space step on the torus and stays unitary at off-grid momenta (infinite volume: the link "
          "hopping squares to 2 at every k)", all(np.allclose(Hk(blW, KS[i]), Wk(KS[i])) for i in range(0, 64, 7))
          and all(np.allclose(Wk(k) @ Wk(k).conj().T, np.eye(12)) for k in rng2.uniform(-np.pi, np.pi, size=(5, 3))))
    ev_k, vk = np.linalg.eig(Bst.conj().T @ Wr @ Bst)
    node_idx = np.where(np.abs(np.angle(ev_k)) < 1e-7)[0]; Qn, _ = np.linalg.qr(vk[:, node_idx])
    dnode = decompose(Bst @ Qn)
    flat = [int(np.sum(np.abs(np.angle(np.linalg.eigvals(Wk(rng2.uniform(-np.pi, np.pi, 3))))) < 1e-9)) for _ in range(5)]
    cone = {}
    for q in (0.004, 0.002, 0.001):
        S = []
        for d in dq[:60]:
            e = np.angle(np.linalg.eigvals(Wk(kst + q * d))); e = np.sort(e[np.abs(e) < 0.05]); S.append(e / q)
        cone[q] = np.array(S)
    vcone = np.abs(cone[0.001][:, [0, 1, 4, 5]])
    anc = [np.ptp(np.abs(cone[q][:, [0, 1, 4, 5]])) for q in (0.004, 0.002, 0.001)]
    check("at k* the step has a 6-fold node, G3/2 + one spin-1/2 doublet: four bands leave at +-|q|/sqrt3 (each 2-fold; spin-1 x spin-1/2 "
          "form) with anisotropy falling as |q|^2, and two bands are exactly flat (forced: +1 spaces of dimension 6 and 8 in 12 meet in >= 2)",
          len(node_idx) == 6 and dnode is not None and dnode.get('G3/2') == 1 and sum(dnode.values()) == 2 and set(dnode) <= SPIN
          and np.allclose(vcone, 1 / s3, atol=1e-6) and np.allclose(cone[0.001][:, 2:4], 0, atol=1e-9)
          and min(flat) == 2 and all(abs(anc[i] / anc[i + 1] - 4) < 0.2 for i in range(2)),
          f"node content {dnode}, speed {vcone.mean():.8f}, anisotropy {np.array(anc)}, flat bands at generic k {flat}")
    # no-go illustration: doublet velocity at k* vanishes for products of symmetric reflections and on-site unitaries
    from scipy.linalg import expm
    loc_reps = []
    for P, s_ in rots:
        Mx = np.zeros((nV, nV)); Mx[P, np.arange(nV)] = (-1.0) ** s_; loc_reps.append(Mx[np.ix_(loc0, loc0)])
    def rand_onsite():
        A = rng2.normal(size=(12, 12)) + 1j * rng2.normal(size=(12, 12)); A = A + A.conj().T
        return expm(1j * sum(R @ A @ R.T for R in loc_reps) / 24)
    vmax_d = 0.0
    for trial in range(3):
        U1, U2 = rand_onsite(), rand_onsite()
        for Wf in (lambda k: Hk(blL, k) @ U1 / np.sqrt(2), lambda k: Hk(blL, k) @ U1 @ Hk(blL, k) @ U2 / 2):
            e0, v0 = np.linalg.eig(Wf(kst)); order = np.argsort(np.angle(e0)); e0 = e0[order]
            ang = np.angle(e0)
            for i in range(11):
                if abs(ang[i + 1] - ang[i]) < 1e-8 and (i == 0 or abs(ang[i] - ang[i - 1]) > 1e-8) and (i + 2 > 11 or abs(ang[i + 2] - ang[i]) > 1e-8):
                    for d in dq[:6]:
                        e = np.angle(np.linalg.eigvals(Wf(kst + 1e-4 * d)) * np.exp(-1j * ang[i]))
                        e = np.sort(e[np.abs(e) < 0.01]); vmax_d = max(vmax_d, abs(e[-1] - e[0]) / 2e-4)
    check("no-go illustration: with random symmetric on-site unitaries between link reflections, every isolated spin-1/2 doublet at k* "
          "has zero velocity (its states are fixed by symmetry; a reflection's projected derivative vanishes since {R, dR} = 0)",
          vmax_d < 1e-3, f"largest doublet half-splitting/q {vmax_d:.2e}")

    # diagonal shift: {d,e} at v -> {d,e} at v+d+e, signs fixed by symmetrising one hop
    c_xy = [c for c in CORN if set(c) == {(1, 0, 0), (0, 1, 0)}][0]
    i0 = C['VID'][((0, 0, 0), c_xy)]; j0 = C['VID'][((1, 1, 0), c_xy)]
    Sr = np.zeros((nV, nV))
    for Pr, sr in rots:
        for Pt, st in trans:
            P = Pt[Pr]; s_ = sr ^ st[Pr]; Sr[P[j0], P[i0]] += (-1.0) ** (int(s_[i0]) + int(s_[j0]))
    Sr /= np.abs(Sr).max()
    ok_shift = (np.allclose(Sr @ Sr.T, np.eye(nV)) and np.all(np.isin(np.round(np.abs(Sr), 9), [0, 1]))
                and all(np.allclose(conj(Sr, P, s_), Sr) for P, s_ in rots + trans[:5]))
    Lam = np.zeros((12, 12), complex)
    for sg in itertools.product((1, -1), repeat=3):
        x, y, z = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
        cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
        if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
        for a_ in range(3):
            q_, r_ = cy[a_], cy[(a_ + 1) % 3]; ii, jj = C['VID'][((0, 0, 0), q_)], C['VID'][((0, 0, 0), r_)]
            amp = 1j * (-1.0) ** u[C['EID'][frozenset((ii, jj))]]; Lam[CI[r_], CI[q_]] += amp; Lam[CI[q_], CI[r_]] += np.conj(amp)
    def eproj(M):
        w_, V_ = np.linalg.eigh(M); ls = sorted(set(np.round(w_, 6)))
        return [V_[:, np.abs(w_ - l) < 1e-6] @ V_[:, np.abs(w_ - l) < 1e-6].conj().T for l in ls]
    PH, PLm = eproj(Bloch(np.zeros(3)).conj().T @ H0(1.0, 0.0) @ Bloch(np.zeros(3))), eproj(Lam)
    UH = PH[0] - PH[1] - 1j * PH[2]; UL = PLm[0] + 1j * PLm[1] + 1j * PLm[2] + PLm[3]
    blS = blocks_from(Sr); Ws = lambda k: Hk(blS, k) @ Hk(blL, k) @ UH @ UL / np.sqrt(2)
    def wrap(x): return np.angle(np.exp(1j * x))
    e0 = np.angle(np.linalg.eigvals(Ws(kst))); E = [x for x in e0 if np.sum(np.abs(wrap(e0 - x)) < 1e-7) == 2][0]
    def node(k0):
        out = {}
        for q in (0.004, 0.002, 0.001):
            sp_ = []
            for d in dq[:40]:
                e = wrap(np.angle(np.linalg.eigvals(Ws(k0 + q * d))) - E); e = np.sort(e[np.abs(e) < 0.1]); sp_.append((e[-1] - e[0]) / (2 * q))
            out[q] = np.array(sp_)
        return out
    def berry(k0, r=0.02, n=14):
        th = np.linspace(0, np.pi, n + 1); phs = np.linspace(0, 2 * np.pi, 2 * n, endpoint=False); Uv = []
        for t in th:
            row = []
            for p_ in phs:
                e, v = np.linalg.eig(Ws(k0 + r * np.array([np.sin(t) * np.cos(p_), np.sin(t) * np.sin(p_), np.cos(t)])))
                a_ = wrap(np.angle(e) - E); idx = np.argsort(np.where(np.abs(a_) < 0.3, a_, 9))[0]; row.append(v[:, idx] / np.linalg.norm(v[:, idx]))
            Uv.append(row)
        tot = 0
        for i_ in range(n):
            for j_ in range(2 * n):
                a_, b_, c_, d_ = Uv[i_][j_], Uv[i_ + 1][j_], Uv[i_ + 1][(j_ + 1) % (2 * n)], Uv[i_][(j_ + 1) % (2 * n)]
                tot += np.angle(np.vdot(a_, b_) * np.vdot(b_, c_) * np.vdot(c_, d_) * np.vdot(d_, a_))
        return tot / (2 * np.pi)
    nk = node(kst); ank = [np.ptp(nk[q]) / nk[q].mean() for q in (0.004, 0.002, 0.001)]
    cube = [np.array(sg_) * np.pi / 2 for sg_ in itertools.product((1, -1), repeat=3)]
    fluxes = [round(berry(c)) for c in cube]
    at_E = [int(np.sum(np.abs(wrap(np.angle(np.linalg.eigvals(Ws(c))) - E)) < 1e-7)) for c in cube]
    grid = [np.array(t) * 2 * np.pi / 10 - np.pi + 0.11 for t in itertools.product(range(10), repeat=3)]
    far = [g for g in grid if min(np.linalg.norm(wrap(g - c)) for c in cube) > 0.5]
    gapE = min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Ws(g))) - E))) for g in far)
    check("the diagonal shift S ({d,e} at v -> {d,e} at v+d+e) is a symmetric signed permutation; the step S x link reflection x two "
          "Clifford-phase on-site factors has an isolated spin-1/2 Weyl doublet at k* with speed sqrt2/3, anisotropy ~ |q|^2, and Weyl nodes "
          "(flux +-1, net 0) at all eight points (pi/2)(+-1,+-1,+-1) at the node quasi-energy, which no other sampled momentum reaches",
          ok_shift and np.allclose(nk[0.001], np.sqrt(2) / 3, atol=1e-6) and all(abs(ank[i] / ank[i + 1] - 4) < 0.2 for i in range(2))
          and all(m == 2 for m in at_E) and all(abs(f) == 1 for f in fluxes) and sum(fluxes) == 0 and gapE > 0.05,
          f"E = {E:.4f}, speed {nk[0.001].mean():.8f}, anisotropy {np.array(ank)}, fluxes {fluxes}, min distance to E elsewhere {gapE:.3f}")

    def mults(M):
        e = np.sort(np.angle(np.linalg.eigvals(M))); out = []; i = 0
        while i < len(e):
            j = i
            while j + 1 < len(e) and abs(wrap(e[j + 1] - e[i])) < 1e-7: j += 1
            out.append(j - i + 1); i = j + 1
        if len(out) > 1 and abs(wrap(e[0] - e[-1])) < 1e-7: out[0] += out.pop()
        return out
    even_all = all(all(m % 2 == 0 for m in mults(Ws(c))) for c in cube)
    phs = np.concatenate([np.angle(np.linalg.eigvals(Ws(g))) for g in grid])
    hist, edges = np.histogram(phs, bins=720, range=(-np.pi, np.pi))
    gap_arcs = edges[:-1][hist == 0]
    gap_away = [x for x in gap_arcs if abs(wrap(x - E)) > 0.1]
    check("doubling-corollary ingredient: every level of this step at all eight cube points is even (anticommuting axis-C2 lifts); "
          "the gap hypothesis is NOT asserted for this step (coarse-grid empty arcs are reported only)",
          even_all and all(m == 2 for m in at_E), f"coarse-grid empty arcs away from E: {len(gap_away)} of 720 bins (not a gap certificate)")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
