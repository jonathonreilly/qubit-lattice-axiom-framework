AUDIT_INPUT_PATHS = ('docs/SITE_BOND_LINK_REGISTERS_NEED_SKEW_LOOP_PLAQUETTES_TO_GAP_THE_EXTRA_MODE_AND_GIVE_AN_ISOTROPIC_PHOTON_COULOMB_LAW_AND_A_GAUSS_CONSISTENT_SPLIT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""site-registers: consistency of CL-1's site-bond link layout (one register per site, on its even-centre ->
odd-centre bond). Supplied model, finite diagnostics; numpy only; no Fock space is built.

A  geometry: the register bonds are the nearest-neighbour bonds of the body-centred centre lattice; per 2^3 cell
   8 registers, 2 centres, 6 values beyond gauge; that lattice is Bravais, so the 6 are 3 per primitive cell, i.e.
   2 photons + 1 extra, zone-folded twice; smallest register loops (4-cycles): 12 skew + 12 planar per cell.
B  quadratic plaquette spectra (H = U/2 sum E_b^2 + K/2 sum_p F_p^2, omega^2 = U K lambda):
   B1 CL-3 as written (even-centre squares, centre-bond holonomy = mean of its four two-site paths): 4 exact zero
      branches at every momentum (no stiffness for the extras);
   B2-B4 register loops: skew (mixed) quads, planar rhombi, both: zeros only the photon pair at q = 0, extras gapped
      over the whole zone; photon isotropy at O(q^2), polarisation degeneracy, O(q^4) anisotropy.
C  Coulomb from Gauss's law with least electric energy on the register lattice; large-S alpha for ring exchange on
   the register loops.
D  split: the coarse-total map for site registers (corner 1, edge 1/2, face 1/4) obeys R D_c = D_p S exactly; no
   covariant integer assignment exists; the collinear-half skeleton passing is integer, local, covariant and keeps
   every Gauss law; the coarse map carries the children's long-wavelength photons onto the parent's.
"""
import itertools, math, os, signal, sys, time
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.alarm(AUDIT_TIMEOUT_SEC - 5)
import numpy as np

T0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261022)
SG = [np.array(s) for s in itertools.product((-1, 1), repeat=3)]          # 8 bond directions from an even centre
SIDX = {tuple(s): i for i, s in enumerate(SG)}
D4 = [np.array(d) for d in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1))]   # primitive bond representatives
DIDX = {tuple(d): i for i, d in enumerate(D4)}
def is_even(v): return all(c % 2 == 0 for c in v)                       # centres relative to an even centre: even = 2Z^3

# ---------------- A. geometry ----------------
print('== A. geometry of the site-bond layout')
L = 4; sites = np.array(list(itertools.product(range(2 * L), repeat=3)))
ec = 2 * (sites // 2) + 0.5; oc = 2 * ((sites - 1) // 2) + 1.5; sv = oc - ec
okA = np.allclose((ec + oc) / 2, sites) and {tuple(x) for x in sv.astype(int)} == {tuple(s) for s in SG}
bset = {(tuple(e % (2 * L)), tuple(o % (2 * L))) for e, o in zip(ec, oc)}
check('A1 [T] each site is the midpoint of its own bond from even to odd centre (offset in {+-1}^3); bonds <-> sites is a bijection; '
      'the centres form the body-centred lattice and these are its nearest-neighbour bonds (8 per centre)',
      okA and len(bset) == len(sites), f'{len(sites)} sites, {len(bset)} bonds, {L**3} cells')

def cycles4():
    """all 4-cycles of the centre lattice through 0 or (1,1,1), unique modulo 2Z^3 translations"""
    out = {}
    for start in (np.zeros(3, int), np.ones(3, int)):
        for ss in itertools.product(range(8), repeat=3):
            st = [SG[i] for i in ss]; s4 = -(st[0] + st[1] + st[2])
            if tuple(s4) not in SIDX: continue
            st.append(s4); vs = [start.copy()]
            for s in st: vs.append(vs[-1] + s)
            if len({tuple(v) for v in vs[:4]}) < 4: continue
            mn = min(map(tuple, vs[:4])); sh = np.array(mn) - (0 if is_even(mn) else 1)
            vt = [v - sh for v in vs]; key = frozenset(frozenset((tuple(vt[j]), tuple(vt[j + 1]))) for j in range(4))
            if key in out: continue
            d02 = vt[2] - vt[0]; d13 = vt[3] - vt[1]
            ax = lambda d: int(np.count_nonzero(d)) == 1
            kind = 'skew' if (ax(d02) and ax(d13)) else 'planar'
            out[key] = (kind, vt[:5])
    return list(out.values())
CYC = cycles4()
nsk = sum(k == 'skew' for k, _ in CYC); npl = sum(k == 'planar' for k, _ in CYC)
def planar_ok(vs):
    a, b, c, d = [np.array(v, float) for v in vs[:4]]
    return abs(np.linalg.det(np.array([b - a, c - a, d - a]))) < 1e-12
pl_flat = all(planar_ok(v) == (k == 'planar') for k, v in CYC)
check('A2 [T] smallest register loops (4-cycles) per 2^3 cell: 12 skew quads (both diagonals along axes; the mixed plaquettes) '
      '+ 12 planar rhombi (one axis diagonal, one face diagonal; rhombic-dodecahedron faces); each register lies in 6 of each kind',
      nsk == 12 and npl == 12 and pl_flat, f'skew {nsk}, planar {npl}; 4*12/8 = 6 loops of each kind per register')

# ---------------- Bloch machinery ----------------
def step_bond_conv(v, s):
    """conventional cell: register bond index (type 0..7 at an even centre) and sign for the step v -> v+s"""
    if is_even(v): return v, SIDX[tuple(s)], 1
    return v + s, SIDX[tuple(-s)], -1
def step_bond_prim(v, s):
    if s[0] == 1: return v, DIDX[tuple(s)], 1
    return v + s, DIDX[tuple(-s)], -1
def _prim_cycles():
    """the same loops modulo all centre-lattice translations (the centre lattice is Bravais): one primitive cell = half a 2^3 cell"""
    out = {}
    for kind, vs in CYC:
        mn = np.array(min(map(tuple, vs[:4]))); vt = [v - mn for v in vs]
        key = frozenset(frozenset((tuple(vt[j]), tuple(vt[j + 1]))) for j in range(4))
        out.setdefault(key, (kind, vt))
    return list(out.values())
CYCP = _prim_cycles()
def loop_rows(q, kinds, prim):
    rows = []
    for kind, vs in (CYCP if prim else CYC):
        if kind not in kinds: continue
        r = np.zeros(4 if prim else 8, complex)
        for j in range(4):
            x, t, sg = (step_bond_prim if prim else step_bond_conv)(vs[j], vs[j + 1] - vs[j])
            r[t] += sg * np.exp(1j * q @ x)
        rows.append(r)
    return np.array(rows)
def gauge_conv(q):   # chi_e at 0, chi_o at s: dA_s = chi_o(s) - chi_e(0)
    return np.stack([-np.ones(8, complex), np.array([np.exp(1j * q @ s) for s in SG])], 1)
def gauge_prim(q):
    return np.array([np.exp(1j * q @ d) - 1 for d in D4])[:, None]
def phys_spec(M, G):
    """eigenvalues of M on the orthogonal complement of the gauge columns G"""
    U_, sv, _ = np.linalg.svd(G, full_matrices=False); r = int(np.sum(sv > 1e-12)); Q = U_[:, :r]
    P = np.eye(M.shape[0]) - Q @ Q.conj().T
    w = np.sort(np.linalg.eigvalsh(P @ M @ P))
    return w[r:]                      # drop the gauge directions (exact zeros of P M P on range(G))
def Pi_even(q):      # CL-3 as written: even-centre bond a = mean of four two-site paths e -> o -> e + 2 e_a
    P = np.zeros((3, 8), complex)
    for a in range(3):
        for i, s in enumerate(SG):
            if s[a] != 1: continue
            t = s.copy(); t[a] = -1                        # e + 2e_a = o - t with o = e + s: path uses bond (e, s) then (e+2e_a, t) reversed
            P[a, i] += 0.25; P[a, SIDX[tuple(t)]] -= 0.25 * np.exp(1j * q[a] * 2)
    return P
def curl_cubic(q, h=2.0):  # cubic-lattice plaquettes of spacing h on a 3-component connection
    C = []
    for a, b in ((0, 1), (1, 2), (2, 0)):
        r = np.zeros(3, complex); r[a] += 1 - np.exp(1j * q[b] * h); r[b] += np.exp(1j * q[a] * h) - 1; C.append(r)
    return np.array(C)
def M_form(q, form):
    if form == 'cl3':
        A = curl_cubic(q) @ Pi_even(q); return A.conj().T @ A, gauge_conv(q)
    if form == 'cl3eo':           # both tilings' centre lattices, each centre bond = mean of its four two-site paths
        A1 = curl_cubic(q) @ Pi_even(q)
        P2 = np.zeros((3, 8), complex)   # odd centre o at the origin: path o -> e = o - s -> o + 2e_a uses -A(e,s) + A(e,t), t = s + 2e_a
        for a in range(3):
            for i, s in enumerate(SG):
                if s[a] != -1: continue
                t = s.copy(); t[a] = 1; ph = np.exp(-1j * q @ s)
                P2[a, i] -= 0.25 * ph; P2[a, SIDX[tuple(t)]] += 0.25 * ph
        A2 = curl_cubic(q) @ P2
        A = np.vstack([A1, A2]); return A.conj().T @ A, gauge_conv(q)
    kinds = {'skew': ('skew',), 'planar': ('planar',), 'all': ('skew', 'planar')}[form]
    C = loop_rows(q, kinds, prim=True); return C.conj().T @ C, gauge_prim(q)

print('== B. quadratic spectrum of the plaquette phase on the register bonds (eigenvalues lambda of curl^T curl)')
qr = rng.uniform(-np.pi, np.pi, 3)
w_cl3 = phys_spec(*M_form(qr, 'cl3')); w_eo = phys_spec(*M_form(qr, 'cl3eo'))
nz_cl3 = [];
for _ in range(30):
    qq = rng.uniform(-np.pi, np.pi, 3); nz_cl3.append(int(np.sum(np.abs(phys_spec(*M_form(qq, 'cl3'))) < 1e-10)))
w0 = phys_spec(*M_form(np.array([1e-9, 0, 0]), 'cl3'))
check('B1 [T] CL-3 as written (even-centre squares; each centre bond = mean of its four two-site paths) has NO stiffness for the '
      'extras: of the 6 gauge-invariant values per cell exactly 4 have lambda = 0 at every momentum (flat, unconstrained)',
      all(n == 4 for n in nz_cl3), f'zero physical branches at 30 random q: {sorted(set(nz_cl3))}; nonzero at q_r: {np.round(w_cl3[w_cl3 > 1e-9], 3)}')
nz_eo = int(np.sum(np.abs(w_eo) < 1e-10))
check('B1b [T] adding the odd tiling\'s centre squares the same way still leaves 2 flat zero branches per cell',
      nz_eo == 2, f'zero physical branches: {nz_eo}')

def zone_scan(form, n=14):
    """primitive BZ: q in the BCC reciprocal cell; returns min of 3rd branch, min of 1st branch away from q = 0"""
    A = np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1]], float); B = 2 * np.pi * np.linalg.inv(A).T
    ext, ph, ph_q = 1e9, 1e9, None
    for i, j, k in itertools.product(range(n), repeat=3):
        q = (i / n) * B[0] + (j / n) * B[1] + (k / n) * B[2]
        if i == j == k == 0: continue
        w = phys_spec(*M_form(q, form))
        ext = min(ext, w[2])
        # distance of q to nearest reciprocal lattice vector
        if w[0] < ph: ph, ph_q = w[0], q
    return ext, ph, B
res = {}
for form in ('skew', 'planar', 'all'):
    wG = phys_spec(*M_form(np.array([1e-7, 0, 0]), form))
    ext, ph_min, B = zone_scan(form)
    # photon kappa along axis, face, body, generic; polarisation splitting
    kap = []; split = 0.0; aniso4 = []
    for nv in (np.array([1., 0, 0]), np.array([1., 1, 0]) / math.sqrt(2), np.ones(3) / math.sqrt(3), np.array([1., 2, 3]) / math.sqrt(14)):
        for qm in (1e-3, 0.05):
            w = phys_spec(*M_form(qm * nv, form))
            if qm == 1e-3: kap.append(w[0] / qm**2); split = max(split, abs(w[1] - w[0]) / qm**2)
            else: aniso4.append((w[0] + w[1]) / 2 / qm**2)
    res[form] = (wG, ext, kap, split, aniso4)
def spec_vec(q, form):
    M, G = M_form(q, form); U_, sv, _ = np.linalg.svd(G, full_matrices=False); Q = U_[:, :int(np.sum(sv > 1e-12))]
    P = np.eye(M.shape[0]) - Q @ Q.conj().T; w, V = np.linalg.eigh(P @ M @ P)
    keep = [i for i in np.argsort(w) if np.linalg.norm(P @ V[:, i]) > 0.5]; return w[keep], V[:, keep]
def c4_coeff(form, nv):   # lambda_photon = kappa q^2 (1 + c4 q^2 + ...), Richardson from q = 0.02, 0.04
    vals = [np.mean(phys_spec(*M_form(qm * nv, form))[:2]) / qm**2 for qm in (0.02, 0.04)]
    k0 = (4 * vals[0] - vals[1]) / 3; return k0, (vals[1] - vals[0]) / (0.04**2 - 0.02**2) / k0
dirs = [np.array([1., 0, 0]), np.array([1., 1, 0]) / math.sqrt(2), np.ones(3) / math.sqrt(3), np.array([1., 2, 3]) / math.sqrt(14),
        np.array([2., 1, 0]) / math.sqrt(5)]
for tag, form in (('B2', 'skew'), ('B4', 'all')):
    wG, ext, kap, split, an = res[form]; k0 = np.mean(kap)
    c4 = [c4_coeff(form, nv)[1] for nv in dirs]
    check(f'{tag} [T/D] {form} register loops: zeros only the photon pair at q -> 0; the one extra branch per centre is gapped over the whole '
          f'primitive zone; photon isotropic at O(q^2), polarisations degenerate',
          wG[0] < 1e-9 and wG[1] < 1e-9 and wG[2] > 1 and ext > 0.5 and np.ptp(kap) < 1e-5 * k0 and split < 1e-5,
          f'extra at q=0 {wG[2]:.3f}, min over zone {ext:.3f}; kappa {k0:.4f}; O(q^4) c4 axis/face/body/gen/(2,1,0) '
          + '/'.join(f'{c:+.4f}' for c in c4))
bir = []
for nv in dirs:
    bir.append(np.mean([(lambda w: (w[1] - w[0]) / (2 * 2.0 * qm**4))(phys_spec(*M_form(qm * nv, 'skew'))) for qm in (0.02,)]))
check('B2c [D] skew loops: the photon pair splits only at O(q^4): lambda_pm = 2 q^2 (1 - q^2/12 +- b q^2), b = 0 on axes and body diagonals, '
      '1/12 on face diagonals (dimension-six birefringence, Delta v/c = b (qa)^2)', abs(bir[0]) < 1e-6 and abs(bir[2]) < 1e-6 and abs(bir[1] - 1/12) < 1e-3,
      'b axis/face/body/gen/(2,1,0) = ' + '/'.join(f'{b:.4f}' for b in bir))
wG, ext, kap, split, an = res['planar']
lam_x = [spec_vec(qm * dirs[3], 'planar')[0][2] / qm**2 for qm in (0.01, 0.02)]
check('B3 [T/D] planar rhombi alone are not enough: the extra branch is gapless at q = 0 (a third massless mode, lambda_extra ~ q^2), so the planar faces '
      'cannot be the plaquette set by themselves', wG[2] < 1e-9 and abs(lam_x[0] - lam_x[1]) < 0.05 * lam_x[0],
      f'extra at q=0 {wG[2]:.1e}; lambda_extra/q^2 = {lam_x[0]:.3f} (photon kappa {np.mean(kap):.3f})')
wx, Vx = spec_vec(np.zeros(3), 'skew'); vx = Vx[:, -1]; patt = np.array([d[0] * d[1] * d[2] for d in D4], float)
ov = abs(patt @ vx) / np.linalg.norm(patt)
check('B2b [T] the gapped extra at q = 0 is the pattern A_d = d1 d2 d3 on the four bond directions (+ toward one tetrahedron of each cube, '
      '- toward the other): invariant under the 12 tetrahedral turns, odd under the 12 the copy mass breaks (the copy-sign channel)',
      ov > 1 - 1e-9, f'overlap {ov:.12f}; lambda = {wx[-1]:.3f}')
# zone-folding: conventional spectrum at q equals the primitive spectrum at q and q + (pi, pi, pi)/... (folding vector of the cell)
qf = rng.uniform(-1, 1, 3)
Cc = loop_rows(qf, ('skew',), prim=False); wc = phys_spec(Cc.conj().T @ Cc, gauge_conv(qf))
G1 = np.array([np.pi, np.pi, np.pi]) / 1.0                      # e^{i G.v} = -1 on odd centres, +1 on even: G = (pi,pi,pi)/1 in site units
wp = np.sort(np.concatenate([phys_spec(*M_form(qf, 'skew')), phys_spec(*M_form(qf + G1, 'skew'))]))
check('B5 [T] zone folding: the 6 conventional-cell branches are the primitive cell\'s 3 (photon pair + 1 extra) at q and at q + (pi,pi,pi); '
      'so of the 4 "extras" per cell, 2 are the photon\'s own folded copy and only 2 (one per centre) are new modes',
      np.allclose(np.sort(wc), wp, atol=1e-9) and len(CYCP) == 12, f'max dev {np.abs(np.sort(wc) - wp).max():.1e}')
# identify the k=0 content of the skew form: conventional Gamma spectrum (the mixed-plaquette law of photon placement)
wc0 = phys_spec(*(lambda C: (C.conj().T @ C, gauge_conv(np.zeros(3))))(loop_rows(np.zeros(3), ('skew',), prim=False)))
print(f'   skew loops, conventional Gamma (7 values beyond the 1 gauge): {np.round(np.sort(wc0), 6)}  '
      f'(= 3 flat holonomies + T2 triplet [folded photon/extra at zone point H] + singlet [the extra])')
wGs = res['skew'][0]; wGp = res['planar'][0]; wGa = res['all'][0]

# ---------------- C. Coulomb and alpha ----------------
print('== C. Coulomb law from Gauss\'s law with least electric energy; alpha for ring exchange on register loops')
Lc = 48
k1 = 2 * np.pi * np.fft.fftfreq(Lc)                               # per conventional cell (2 sites)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
f = (1 + np.exp(-1j * KX)) * (1 + np.exp(-1j * KY)) * (1 + np.exp(-1j * KZ))   # sum over the 8 odd neighbours of an even centre
den = 64 - np.abs(f)**2; den[0, 0, 0] = np.inf
Gee = np.real(np.fft.ifftn(8 / den)); Vtot = (2 * Lc)**3            # volume in site units
def Gc(n):
    r = 2 * np.linalg.norm(n); return Gee[tuple(np.array(n) % Lc)] - r**2 / (6 * Vtot)
coef = []
for nv, Rs in (((1, 0, 0), (4, 6, 8)), ((1, 1, 1), (2, 3, 4))):
    for m in Rs:
        a = np.array(nv) * m; R = 2 * np.linalg.norm(a)
        coef.append(4 * np.pi * (Gc(a) - Gc(2 * a)) / (1 / R - 1 / (2 * R)))
check('C1 [T/D] least electric energy under Gauss\'s law on the register lattice: E = -grad phi, Lap phi = q; static +-1 charges '
      '(even centres) shift the energy by -U G(R) with 4 pi R G -> 1 isotropically (8 bonds of length sqrt3 per centre, 1/4 centre per site '
      'volume: (8*3/6)(1/4) = 1), so Coulomb with alpha = U/(4 pi c)',
      all(abs(c - 1) < 0.02 for c in coef), f'axis R=8,12,16: {coef[0]:.3f},{coef[1]:.3f},{coef[2]:.3f}; body R=4,6,8 sqrt3: '
      f'{coef[3]:.3f},{coef[4]:.3f},{coef[5]:.3f} (48^3 cells)')
# large-S ring exchange: U = 2 J S(S+1) N_p, K = 2 J [S(S+1)]^2, c = sqrt(U K kappa) -> alpha = sqrt(N_p / (kappa S(S+1))) / (4 pi)
for form, Np in (('skew', 6), ('planar', 6), ('all', 12)):
    kap = np.mean(res[form][2]); res[form] = res[form] + (Np, kap)
a_sk = lambda S, form: math.sqrt(res[form][5] / (res[form][6] * S * (S + 1))) / (4 * math.pi)
a_cub = lambda S: 1 / (2 * math.pi * math.sqrt(S * (S + 1)))
need = {form: math.sqrt(res[form][5] / res[form][6]) / (4 * math.pi * 5.01e-4) for form in ('skew', 'planar', 'all')}
check('C2 [E] large-S pure ring on register loops: alpha(S) = sqrt(N_p/(kappa S(S+1)))/(4 pi) (N_p loops per register); at CL-1\'s S = 3/2 '
      'it is O(0.1), far above the hypercharge-unit target 5.0e-4 (cubic edge layout: 1/(2 pi sqrt(S(S+1))))',
      all(a_sk(1.5, fm) > 0.03 for fm in ('skew', 'planar', 'all')),
      f'S=3/2: skew {a_sk(1.5, "skew"):.4f}, planar {a_sk(1.5, "planar"):.4f}, both {a_sk(1.5, "all"):.4f}, cubic {a_cub(1.5):.4f}; '
      f'sqrt(S(S+1)) for 5e-4: skew {need["skew"]:.0f}, planar {need["planar"]:.0f}, both {need["all"]:.0f}')

# ---------------- D. split ----------------
print('== D. split: children\'s site registers from the parent\'s')
# child units: parent even centres 4Z^3 (+ 2(1,1,1) for parent odd); child even = all-odd vectors, child odd = all-even vectors
Lt = 8                                                     # torus length in child units (parent 2^3 cells, children 4^3 cells)
def wrap(v): return tuple(int(c) % Lt for c in v)
pe = [wrap(4 * np.array(n)) for n in itertools.product(range(2), repeat=3)]
po = [wrap(4 * np.array(n) + 2) for n in itertools.product(range(2), repeat=3)]
pv = pe + po; PV = {v: i for i, v in enumerate(pv)}
pbonds = [(P, s) for P in pe for s in SG]; PB = {(P, tuple(s)): i for i, (P, s) in enumerate(pbonds)}
ce = [wrap(v) for v in itertools.product(range(1, Lt, 2), repeat=3)]
co = [wrap(v) for v in itertools.product(range(0, Lt, 2), repeat=3)]
cv = ce + co; CV = {v: i for i, v in enumerate(cv)}
cbonds = [(C, s) for C in ce for s in SG]; CB = {(C, tuple(s)): i for i, (C, s) in enumerate(cbonds)}
def div(vlist, VI, bonds, step):
    Dm = np.zeros((len(vlist), len(bonds)))
    for j, (v, s) in enumerate(bonds):
        Dm[VI[v], j] += 1; Dm[VI[wrap(np.array(v) + step * s)], j] -= 1
    return Dm
Dp = div(pv, PV, pbonds, 2); Dc = div(cv, CV, cbonds, 1)
def tdist(a, b):
    d = (np.array(a) - np.array(b) + Lt / 2) % Lt - Lt / 2; return np.linalg.norm(d)
# R: child centre -> parent centre weights; child even -> its parent even block; child odd D: = parent even if it is one, else shared
# evenly among the nearest parent odd centres (corner 1, edge midpoint 2 -> 1/2, face centre 4 -> 1/4)
Rm = np.zeros((len(pv), len(cv))); ties = {}
for C in ce:
    P = min(pe, key=lambda P: tdist(P, C)); Rm[PV[P], CV[C]] = 1
for D in co:
    if D in PV and D in pe: Rm[PV[D], CV[D]] = 1; continue
    dm = min(tdist(D, O) for O in po); near = [O for O in po if abs(tdist(D, O) - dm) < 1e-9]
    for O in near: Rm[PV[O], CV[D]] = 1 / len(near)
    ties[len(near)] = ties.get(len(near), 0) + 1
# S: child bond (C -> D) contributes to parent bond (P -> O) with weight R[O, D], P = block of C, when D is not P
Sm = np.zeros((len(pbonds), len(cbonds)))
for j, (C, s) in enumerate(cbonds):
    D = wrap(np.array(C) + s); P = min(pe, key=lambda P: tdist(P, C))
    if D == P: continue
    for O in po:
        w = Rm[PV[O], CV[D]]
        if w == 0: continue
        dd = ((np.array(O) - np.array(P) + Lt / 2) % Lt - Lt / 2) / 2
        Sm[PB[(P, tuple(dd.astype(int)))], j] += w
err = np.abs(Rm @ Dc - Dp @ Sm).max()
check('D1 [T] coarse totals for site registers: each parent register\'s value = flux of its even cube\'s children into the child centres on '
      'the cube\'s boundary nearest its odd end (the corner itself 1, edge midpoints 1/2, face centres 1/4); then every parent Gauss law '
      'is the weighted sum of child Gauss laws (R D_c = D_p S exactly)',
      err < 1e-12, f'2^3 parent cells -> 4^3 child cells: max |R D_c - D_p S| = {err:.1e}; ties per boundary centre: {dict(sorted(ties.items()))}')
check('D2 [T] no covariant integer assignment exists: a face-centre (edge-midpoint) child centre is equidistant from 4 (2) parent odd centres '
      'that the parent cube\'s symmetries permute transitively, and putting it in a parent even centre would join two even centres',
      ties.get(4, 0) > 0 and ties.get(2, 0) > 0 and ties.get(1, 0) == len(po), f'nearest-parent-odd counts {dict(sorted(ties.items()))}')
# skeleton passing: parent value on the outer half (P+s -> P+2s), inner half (P+s -> P) carries q_child - E, all else 0
ok_all = True; worst = 0.0
Np_ = len(pbonds)
Dpe = Dp[:len(pe)]
for trial in range(20):
    # random parent Gauss configuration: integer E with zero divergence at odd centres and arbitrary even charges
    E = rng.integers(-3, 4, Np_).astype(float)
    # enforce odd Gauss: adjust along random loops is hard; instead solve: E = E0 + loop combo; take E0 integer from charges via a tree
    Qp = Dp @ E
    # parent odd charges must vanish: correct E on the bonds of one odd centre at a time (shift one bond per odd centre)
    for O in po:
        i = PV[O]; r = Qp[i]
        # pick bond (P,s) ending at O: P = O - 2s
        s = SG[0]; P = wrap(np.array(O) - 2 * s); E[PB[(P, tuple(s))]] += r   # this bond has -1 at O: adds -r there, +r at P
        Qp = Dp @ E
    assert np.abs(Qp[len(pe):]).max() == 0
    qc = np.zeros(len(cv))
    Ec = np.zeros(len(cbonds))
    for P in pe:
        Pq = Qp[PV[P]]
        # split the parent charge over its 8 children at random integer values summing to Pq
        qs = rng.multinomial(int(abs(Pq)), np.ones(8) / 8) * np.sign(Pq) if Pq != 0 else np.zeros(8)
        for k, s in enumerate(SG):
            C = wrap(np.array(P) + s); Ev = E[PB[(P, tuple(s))]]
            Ec[CB[(C, tuple(s))]] = Ev; Ec[CB[(C, tuple(-s))]] = qs[k] - Ev; qc[CV[C]] = qs[k]
    gauss_c = np.abs(Dc @ Ec - qc).max(); tot = np.abs(Sm @ Ec - E).max()
    charge_ok = abs(qc.sum() - Qp.sum()) < 1e-12
    worst = max(worst, gauss_c, tot); ok_all &= gauss_c < 1e-12 and tot < 1e-12 and charge_ok and np.allclose(Ec, np.round(Ec))
check('D3 [T] skeleton passing: a parent register\'s bond is two collinear child bonds; its value rides the outer half (child even centre -> '
      'parent odd centre), the inner half carries child charge minus that value, all other child values 0: integer, local, covariant, every '
      'child Gauss law holds for any split of the parent charge over its children, and the coarse totals return the parent values',
      ok_all, f'20 random parent Gauss configurations with charges: max residual {worst:.1e}')
# D4: coarse map carries the children's long-wavelength photon onto the parent's (Bloch). Child conventional cell = 2 child units,
# parent conventional cell = 4 child units. Build T(q): parent 8 bond types x child bonds (Bloch sum over the 8 child cells of a parent cell).
def child_M(q):           # skew loops on the child lattice, conventional formulation (child units)
    C = loop_rows(q, ('skew',), prim=False); return C.conj().T @ C
def parent_M(q):          # same lattice scaled by 2
    C = loop_rows(2 * q, ('skew',), prim=False); return C.conj().T @ C
def T_bloch(q):
    """rows: parent bond types s at parent even centre 0; columns: child bond Bloch amplitudes indexed (child cell offset within the
    parent cell r in {+-1}^3 child-even positions) x 8 types; returns (8, 64) map acting on a child Bloch vector expanded over the
    8 child even centres of one parent cell"""
    Tm = np.zeros((8, 64), complex)
    for j, (C, s) in enumerate(cbonds):
        for i in range(Np_):
            w = Sm[i, j]
            if w == 0: continue
            P, sp = pbonds[i]
            if P != (0, 0, 0): continue
            dC = ((np.array(C) - np.array(P) + Lt / 2) % Lt - Lt / 2)          # child even centre position relative to P
            # the 8 child even centres of P's block are P + t, t in {+-1}^3; other blocks' children never feed P's bonds
            Tm[SIDX[tuple(sp)], 8 * SIDX[tuple(dC.astype(int))] + SIDX[tuple(s)]] += w * 1.0
    return Tm
Tm0 = T_bloch(None)
def child_block_vec(q, v8):
    """child Bloch mode (amplitude v8 per bond type at a child even centre at x, times e^{i q.x}) restricted to the 8 child even
    centres P + t of one parent cell"""
    out = np.zeros(64, complex)
    for k, t in enumerate(SG):
        out[8 * k: 8 * k + 8] = v8 * np.exp(1j * q @ t)
    return out
wts = []
for qm in (0.02, 0.05, 0.1):
    for nv in (np.array([1., 0, 0]), np.ones(3) / math.sqrt(3), np.array([1., 2, 3]) / math.sqrt(14)):
        q = qm * nv
        Mc = child_M(q); Gc_ = gauge_conv(q); Q, _ = np.linalg.qr(Gc_); Pp = np.eye(8) - Q @ Q.conj().T
        w, V = np.linalg.eigh(Pp @ Mc @ Pp); idx = [i for i in np.argsort(w) if np.linalg.norm(Pp @ V[:, i]) > 0.5][:2]
        Vc = V[:, idx]
        Mp = parent_M(q); Gp = np.stack([-np.ones(8, complex), np.array([np.exp(1j * 2 * q @ s) for s in SG])], 1)
        Qp_, _ = np.linalg.qr(Gp); Ppp = np.eye(8) - Qp_ @ Qp_.conj().T
        wp_, Vp_ = np.linalg.eigh(Ppp @ Mp @ Ppp); idp = [i for i in np.argsort(wp_) if np.linalg.norm(Ppp @ Vp_[:, i]) > 0.5][:2]
        Vp2 = Vp_[:, idp]
        for c in range(2):
            img = Ppp @ (Tm0 @ child_block_vec(q, Vc[:, c]))
            wts.append(np.linalg.norm(Vp2.conj().T @ img)**2 / max(np.linalg.norm(img)**2, 1e-30))
wts = np.array(wts).reshape(3, -1)
check('D4 [T/D] the coarse map is level-matched at long wavelength: it sends each child photon (electric mode, transverse, skew loops) into '
      'the parent photon pair at the same momentum, with leakage into the parent extras falling as q^2',
      wts.min() > 0.99 and (1 - wts[2].min()) > (1 - wts[0].max()), 'weight on parent photon pair at |q| = 0.02, 0.05, 0.1 (child units): '
      + ', '.join(f'{1 - r.min():.1e}' for r in wts) + ' (leakage)')
print('supplied: loop set, U/K from |S^+|, large S, target 5.0e-4, skeleton rest (the law uses the vacuum-weighted rest).')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
