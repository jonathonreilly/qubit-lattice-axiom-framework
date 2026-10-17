#!/usr/bin/env python3
"""Numerical corner-model Weyl-pair and pseudoscalar-mass candidate controls.

The finite sampled seed ranks are lower bounds. The invariant-mass selection
argument is conditional on distinct valley irreps and applies to first-order
node-space projection. Projected kinetic/mass algebra supports a leading joint
small-momentum/small-mass Dirac form; the lattice has higher-order corrections.
No exact finite-mass dispersion, complete operator-space classification,
physical particle, qubit implementation or mass-selection mechanism is derived.
Companion: docs/CORNER_FERMION_MASSLESS_DIRAC_PAIR_PROTECTED_BY_CUBE_ROTATIONS_AND_PSEUDOSCALAR_DIRAC_MASS_BOUNDED_THEOREM_NOTE_2026-10-17.md
"""
import itertools, os
import numpy as np


AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ("scripts/corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17.py",)

def _run_reviewed_program():
    global A, C, CI, CORN, DIRS, E, EN, F, FAIL, G2, G32, H0, HERE, Hb, Hfold, Hk, Hr, INVM, IRR, L, M, Mf, Mm, P, PASS, PAU, PSG_RUNNER, Q, R, ROTS, TV, Tel, Tok, U, V, VERTS, Vm, Vs, W1, X, Z0, _, _model, a, a0, a1_zero, a2_real_zero, addt, allO, b, b0, basis, berry_flux, bl, blM, blocks_from, c, c2, cK, cM, cO, cT, cell, chars, check, commutes, compose, conj, cs, cyc, d, dd, decO, dev, dimM, dimX, dirs, dmod, e, e0, eK, eM, ee, ef, ekey, er, etypes, ev, even_t, evm, f, gidx, i, info, invs, j, k, key, key2, kind, kst, lab, loc0, m, mD, mid, nT, nV, n_, nbr, neg, node, nrm, oddR_alone, oddR_tx, ok_sp, onsite_seed, opmat, p, perp, proj, psg, q, q2su, qs, qv, r, reps, rhs, rid, ring, rng, rots, rows, s, s_, seeds, seen, sg, sh, si, sj, so3, spin_char, sv, svM, sym, t, trans, trial, tx, u, ucell, v, vadd, vel, vv, w, w1, w4, x, y, z
    HERE = os.path.dirname(os.path.abspath(__file__))
    PSG_RUNNER = os.path.join(HERE, 'corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17.py')
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

    # ---------------- Part 1
    print("Part 1: complex-conjugation-odd terms invariant under O, site inversion and translations (range <= 1 site)")
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
    check("the 14 sampled averaged seeds have numerical rank 9 (lower bound only)", dimX == 9, f"singular values {np.round(sv[:11]/sv[0], 4)}")
    X = basis[0] / np.abs(basis[0]).max()
    check("these terms are invariant under all rotations and the site inversion, and odd under complex conjugation",
          all(np.allclose(conj(X, P, s), X) for P, s in rots + invs[:1] + trans[:5]) and np.allclose(X.conj(), -X))

    # ---------------- Part 2
    print("\nPart 2: Weyl pair at the rotation-fixed momenta (t1 = -1, t2 = 0.2, X strength 0.05)")
    Hb = H0(-1.0, 0.2) + 0.05 * X
    bl = blocks_from(Hb); f = lambda k: Hk(bl, k)
    eK, eM = np.linalg.eigvalsh(f(kst)), np.linalg.eigvalsh(f(-kst))
    EN = eK[0]
    check("the lowest levels at k* and -k* are degenerate doublets at the same energy (inversion)",
          abs(eK[0] - eK[1]) < 1e-10 and abs(eM[0] - eM[1]) < 1e-10 and abs(eK[0] - eM[0]) < 1e-10)
    dirs = rng.normal(size=(6, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    vel = [(np.linalg.eigvalsh(f(kst + 1e-4 * d))[1] - np.linalg.eigvalsh(f(kst + 1e-4 * d))[0]) / 2e-4 for d in dirs]
    check("the doublet splits linearly with the same velocity in every direction (isotropic Weyl cone)",
          np.ptp(vel) < 1e-4 * np.mean(vel) and np.mean(vel) > 1e-3, f"v = {np.mean(vel):.5f}, spread {np.ptp(vel):.1e}")
    def berry_flux(k0, band=0, r=0.02, n=20):
        th = np.linspace(0, np.pi, n + 1); ph = np.linspace(0, 2 * np.pi, 2 * n, endpoint=False)
        Uv = [[np.linalg.eigh(f(k0 + r * np.array([np.sin(t)*np.cos(p), np.sin(t)*np.sin(p), np.cos(t)])))[1][:, band]
               for p in ph] for t in th]
        tot = 0
        for i in range(n):
            for j in range(2 * n):
                a, b, c, d = Uv[i][j], Uv[i+1][j], Uv[i+1][(j+1) % (2*n)], Uv[i][(j+1) % (2*n)]
                tot += np.angle(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, d) * np.vdot(d, a))
        return tot / (2 * np.pi)
    cK, cM = berry_flux(kst), berry_flux(-kst)
    check("Berry flux of the lower band through a small sphere is +1 at one node and -1 at the other (opposite chirality)",
          round(cK) == -round(cM) and abs(abs(cK) - 1) < 1e-6, f"{cK:+.4f}, {cM:+.4f}")

    # ---------------- Part 3
    print("\nPart 3: Dirac mass terms (staggered, momentum Q = (pi,pi,pi), on-site)")
    ev, V = np.linalg.eigh(Hb); node = V[:, np.where(np.abs(ev - EN) < 1e-6)[0]]
    check("the L = 4 lattice contains the four node states", node.shape[1] == 4)
    def onsite_seed(kind):
        A = rng.normal(size=(12, 12)); A = (A + A.T) if kind == 'real' else (A - A.T)
        S = np.zeros((nV, nV), complex); S[np.ix_(loc0, loc0)] = (1 if kind == 'real' else 1j) * A; return S
    a1_zero = True
    for kind in ('real', 'imag'):
        for _ in range(4):
            M = sym(onsite_seed(kind), Qmom=True); M = (M + M.conj().T) / 2
            if np.abs(M).max() > 1e-10:
                a1_zero &= np.allclose(node.conj().T @ M @ node, 0, atol=1e-9)
    check("tested O-invariant staggered on-site seeds have zero projected matrix elements; Schur inference conditional on distinct valley irreps", a1_zero)
    seeds = []
    for _ in range(10):
        M = sym(onsite_seed('imag'), Qmom=True, a2=True); seeds.append(((M + M.conj().T) / 2).ravel())
    svM = np.linalg.svd(np.array(seeds), compute_uv=False); dimM = int(np.sum(svM > 1e-8 * svM[0]))
    Mm = seeds[0].reshape(nV, nV); Mm /= np.abs(Mm).max()
    w4 = np.linalg.eigvalsh(node.conj().T @ Mm @ node)
    check("the chosen imaginary A2 term splits the projected node space into +-m pairs; 10 sampled seeds have rank 5",
          dimM == 5 and np.allclose(w4[:2], w4[0]) and np.allclose(w4[2:], -w4[0]) and abs(w4[0]) > 1e-3,
          f"projected eigenvalues {np.round(w4, 4)}")
    a2_real_zero = True
    for _ in range(3):
        M = sym(onsite_seed('real'), Qmom=True, a2=True); M = (M + M.conj().T) / 2
        if np.abs(M).max() > 1e-10: a2_real_zero &= np.allclose(node.conj().T @ M @ node, 0, atol=1e-9)
    check("three tested real A2 seeds have zero projected mass; no exhaustive real-space classification", a2_real_zero)

    # ---------------- Part 4
    print("\nPart 4: massive Dirac dispersion")
    blM = blocks_from(Mm)
    def Hfold(k, m):
        return np.block([[Hk(bl, k), m * Hk(blM, k).conj().T], [m * Hk(blM, k), Hk(bl, k + Q)]])
    m = 0.05
    Hr = Hb + m * Mm; er = np.sort(np.linalg.eigvalsh(Hr))
    reps = []; seen = set()
    for t in itertools.product(range(L), repeat=3):
        key = tuple(np.array(t) % L); key2 = tuple((np.array(t) + L // 2) % L)
        if key2 in seen: continue
        seen.add(key); reps.append(np.array(t) * 2 * np.pi / L)
    ef = np.sort(np.concatenate([np.linalg.eigvalsh(Hfold(k, m)) for k in reps]))
    check("folded and real-space spectra agree numerically on L = 4", np.allclose(ef, er, atol=1e-9))
    e0 = np.linalg.eigvalsh(Hfold(kst, m)); mD = (e0[2] - e0[1]) / 2; mid = (e0[1] + e0[2]) / 2
    check("at k* the massive spectrum is two doublets at E_N -+ m_D, symmetric about the node", abs(e0[0] - e0[1]) < 1e-10 and
          abs(e0[2] - e0[3]) < 1e-10 and abs(mid - EN) < 1e-3 * mD, f"m_D = {mD:.5f}, m_D / m at this supplied finite strength = {mD/m:.4f}")
    v = np.mean(vel)
    dev = []
    for d in (0.005, 0.01, 0.02):
        for n_ in dirs[:3]:
            ee = np.linalg.eigvalsh(Hfold(kst + d * n_, m))
            dev.append(abs((ee[2] - mid) - np.sqrt(v * v * d * d + mD * mD)) / np.sqrt(v * v * d * d + mD * mD))
    check("finite sampled upper-band comparison with corrected measured Weyl velocity (relative total-energy deviation < 1e-2; not a kinetic-order proof)",
          max(dev) < 1e-2, f"max relative deviation {max(dev):.1e}")

    # Leading joint small-(momentum,mass) algebra, independently of the
    # gap-dominated finite-mass energy comparison above. Central differences
    # are numerical controls, not exact coefficient or uniform remainder proofs.
    unperturbed, frame = np.linalg.eigh(Hfold(kst, 0.0))
    frame = frame[:, :4]
    step = 1e-6
    kinetic = [frame.conj().T @ ((Hfold(kst + step*axis,0.0)-Hfold(kst-step*axis,0.0))/(2*step)) @ frame for axis in np.eye(3)]
    mass_matrix = frame.conj().T @ ((Hfold(kst,step)-Hfold(kst,-step))/(2*step)) @ frame
    v_squared = float(np.trace(kinetic[0] @ kinetic[0]).real/4)
    mass_squared = float(np.trace(mass_matrix @ mass_matrix).real/4)
    kinetic_error = max(np.linalg.norm(a@b+b@a-(2*v_squared*np.eye(4) if i==j else np.zeros((4,4)))) for i,a in enumerate(kinetic) for j,b in enumerate(kinetic))
    mass_error = max(np.linalg.norm(mass_matrix@mass_matrix-mass_squared*np.eye(4)), max(np.linalg.norm(a@mass_matrix+mass_matrix@a) for a in kinetic))
    check("projected linear kinetic/mass matrices obey numerical Clifford relations and use the measured full Weyl velocity",
          kinetic_error < 1e-8 and mass_error < 1e-8 and v_squared > 1e-6 and mass_squared > 1e-6 and abs(np.sqrt(v_squared)-np.mean(vel)) < 1e-6 and unperturbed[4]-unperturbed[3] > 1e-3,
          f"v={np.sqrt(v_squared):.12g}, mass coefficient={np.sqrt(mass_squared):.12g}, kinetic residual={kinetic_error:.3g}, mass residual={mass_error:.3g}")
    joint_errors=[]
    direction=np.array([1.,2.,3.])/np.sqrt(14.)
    for epsilon in (.02,.01,.005):
        displacement=epsilon*direction; strength=.3*epsilon
        prediction=EN+np.array([-1.,-1.,1.,1.])*np.sqrt(v_squared*np.dot(displacement,displacement)+mass_squared*strength*strength)
        actual=np.linalg.eigvalsh(Hfold(kst+displacement,strength))[:4]
        joint_errors.append(float(np.max(np.abs(actual-prediction))))
    check("joint momentum/mass shrinkage has quadratic finite-sample remainder; no exact finite-mass dispersion claimed",
          all(err < .1*eps*eps for err,eps in zip(joint_errors,(.02,.01,.005))) and all(joint_errors[i+1] < .4*joint_errors[i] for i in range(2)),str(joint_errors))

    # ---------------- Part 5
    print("\nPart 5: spin content (twisted site rotations)")
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
    cO = chars(node, allO)
    decO = {k: int(round(np.real(sum(np.conj(IRR[k][e]) * cO[e] for e in allO)) / 48)) for k in IRR}
    check("the four massless node states transform as E1/2 + E5/2 under the twisted O (opposite A2 characters at k* and -k*)",
          decO == {'E1/2': 1, 'E5/2': 1, 'G3/2': 0})
    evm, Vm = np.linalg.eigh(Hr); ok_sp = True; info = []
    for lab, E in (('lower', e0[0]), ('upper', e0[2])):
        Vs = Vm[:, np.where(np.abs(evm - E) < 1e-6)[0]]; cT = chars(Vs, Tel)
        if cT is None or Vs.shape[1] != 2: ok_sp = False; continue
        nrm = np.real(sum(abs(cT[e]) ** 2 for e in Tel)) / 24
        sh = np.real(sum(np.conj(spin_char(1, G2[e])) * cT[e] for e in Tel)) / 24
        info.append((lab, round(nrm, 4), round(sh, 4))); ok_sp &= abs(nrm - 1) < 1e-6 and abs(sh - 1) < 1e-6
    check("each massive Dirac doublet is the irreducible spin-1/2 representation of the binary tetrahedral group (rotations kept about a site)",
          ok_sp, str(info))

    # ---------------- Part 6
    print("\nPart 6: symmetries of the massive model")
    def commutes(P, s, sign=1.0): return np.allclose(conj(Hr, P, s), Hr)
    Tok = all(commutes(*rots[k]) for k in range(24) if W1[k] == 0)
    oddR_alone = any(not commutes(*rots[k]) for k in range(24) if W1[k] == 1)
    tx = trans[TV.index((1, 0, 0))]
    def compose(a, b):   # operator a after b
        Pa, sa = a; Pb, sb = b
        return Pa[Pb], sb ^ sa[Pb]
    oddR_tx = all(np.allclose(conj(Hr, *compose(tx, rots[k])), Hr) for k in range(24) if W1[k] == 1)
    even_t = all(np.allclose(conj(Hr, *trans[i]), Hr) for i, t in enumerate(TV) if sum(t) % 2 == 0)
    check("the massive model keeps the rotations of T about a site, the w1-odd rotations composed with an odd translation "
          "(together: the cube rotations about a cube centre), and the even translations; w1-odd rotations alone are broken",
          Tok and oddR_tx and even_t and oddR_alone)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")

    raise SystemExit(1 if FAIL else 0)

if __name__ == "__main__":
    _run_reviewed_program()
