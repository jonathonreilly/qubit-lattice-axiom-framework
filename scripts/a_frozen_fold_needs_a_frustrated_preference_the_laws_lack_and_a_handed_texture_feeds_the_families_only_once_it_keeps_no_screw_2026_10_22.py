AUDIT_INPUT_PATHS = ('docs/A_FROZEN_FOLD_NEEDS_A_FRUSTRATED_PREFERENCE_THE_LAWS_LACK_AND_A_HANDED_TEXTURE_FEEDS_THE_FAMILIES_ONLY_ONCE_IT_KEEPS_NO_SCREW_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""chiral-texture-family: can a handed neighbourhood configuration (a fold, helix or screw of the edge or link
registers) that the laws realise spontaneously supply the polar, A-odd family term the mass no-gos ask for?
A  what a shared structure does to the mixing matrix (unit entries, zeros, J)           [exact, seeded]
B  the protein-fold test: frustrated local rules, the tetrahedron fold, a register chain [exact / finite]
C  the matter sea and the vacuum standard: no handedness preference, no driving         [exact / finite]
D  the family term of handed textures on the copy-massed two-tiling tick (216 sites)    [exact / finite]
E  weak chirality, pitch and the zoom ladder                                            [exact / estimate]
Tags: [T] exact or exact-to-rounding, [F] finite diagnostic, [E] estimate, [S] speculation (no check).
"""
import itertools, time
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
from scipy.linalg import expm, logm

AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261022)
NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

# ---------------- A ----------------
print("== A. shared symmetries and the mixing matrix")
def herm(n): a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return (a + a.conj().T) / 2
def Jmax(V):
    n = len(V); return max(abs(np.imag(V[a, b] * V[c, d] * np.conj(V[a, d]) * np.conj(V[c, b])))
                           for a in range(n) for c in range(n) for b in range(n) for d in range(n) if a != c and b != d)
def mixing(hu, hd): return np.linalg.eigh(hu)[1].conj().T @ np.linalg.eigh(hd)[1]
ok = True; worst = []
for dims in ((1, 2), (3, 2, 1), (4, 2)):
    for _ in range(50):
        Q = np.linalg.qr(herm(sum(dims)))[0]
        def blk(): return Q @ np.block([[herm(d) if i == j else np.zeros((d, e)) for j, e in enumerate(dims)]
                                         for i, d in enumerate(dims)]) @ Q.conj().T
        aV = np.abs(mixing(blk(), blk())); nz = (aV < 1e-10).sum(); need = sum(dims) ** 2 - sum(d * d for d in dims)
        ok &= nz >= need and ((1 not in dims) or aV.max() > 1 - 1e-10)
check("[T] lemma: if up and down family terms share a unitary with eigenspaces of sizes d_i, |V| is block diagonal "
      "(at least n^2 - sum d_i^2 zeros) and a 1-dimensional eigenspace gives an entry 1 (50 seeded pairs per size set)", ok)
print("   measured |V|: no zero, no unit entry, J = 3.1e-5, so a shared structure may leave no unitary with two distinct "
      "eigenvalues on the light family space")

# ---------------- B ----------------
print("== B. the protein-fold test")
dih = np.arccos(1 / 3)
print("   (1) CL-3's hinge sum is stationary at zero deficit, met by flat edges in every cell: no frustrated preference (stated)")
cube5 = [np.array(v, float) for v in [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]]
el = sorted(np.linalg.norm(cube5[i] - cube5[j]) for i in range(4) for j in range(i))
corner = [np.array(v, float) for v in [(1, 0, 0), (0, 0, 0), (1, 1, 0), (1, 0, 1)]]
elc = sorted(np.linalg.norm(corner[i] - corner[j]) for i in range(4) for j in range(i))
check("[T] (1') a supplied frustrated preference: all-regular tetrahedra. The block cube's central tetrahedron is regular, "
      "its corner ones are not; 2 pi / arccos(1/3) = 5.104, so regular tetrahedra cannot close around an edge",
      np.allclose(el, np.sqrt(2)) and not np.allclose(elc, elc[0]) and abs(2 * np.pi / dih - 5.104) < 1e-3)
def reflect(p, a, b, c):
    n = np.cross(b - a, c - a); n /= np.linalg.norm(n); return p - 2 * np.dot(p - a, n) * n
SEED = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float) / np.sqrt(8)
def build(seq, seed=SEED):
    V = [*seed]; cur = [0, 1, 2, 3]
    for ch in seq:
        drop = cur[ch]; keep = [v for v in cur if v != drop]
        V.append(reflect(V[drop], *[V[k] for k in keep])); cur = keep + [len(V) - 1]
    return np.array(V)
def score(V, r=5):
    D = np.linalg.norm(V[:, None] - V[None], axis=2)
    if (D[np.triu_indices(len(V), 1)] < 0.9).any(): return None
    return sum(D[i, i + r] < 1.7 for i in range(len(V) - r))
def hand(V): d = np.diff(V, axis=0); return np.sign(np.einsum('ij,ij->i', np.cross(d[:-2], d[1:-1]), d[2:]))
n = 9; res = {}; n3 = 0
for seq in itertools.product(range(3), repeat=n):
    Vq = build(seq); s_ = score(Vq)
    if s_ is not None: res[seq] = s_
    n3 += all(abs(np.linalg.norm(Vq[i] - Vq[i + r]) - 1) < 1e-9 for r in (1, 2, 3) for i in range(len(Vq) - r))
m = max(res.values()); best = [k for k, v in res.items() if v == m]
mir = SEED.copy(); mir[[1, 2]] = mir[[2, 1]]
Vh = build((0,) * n); Vm = build((0,) * n, mir)
check("[T] (2) fold: among the 3^9 face-sharing chains of 10 regular tetrahedra, the range-3 rule 'each new site bonds "
      "to the newest three' (mirror-blind) holds for exactly one chain, the Boerdijk-Coxeter helix, one sense throughout; "
      "the mirrored seed folds the other sense, so the sense is the seed's orientation",
      n3 == 1 and len(set(hand(Vh))) == 1 and len(set(hand(Vm))) == 1 and hand(Vh)[0] == -hand(Vm)[0] and score(Vh) == score(Vm) == m)
check("[F] (2') the funnel is not single: the preference alone leaves thousands of non-overlapping folds, and a longer "
      "contact rule (most i -> i+5 contacts) has several best chains, all helical for their first four steps and then "
      "branching", len(res) > 1000 and len(best) > 1 and all(b[:4] == (0, 0, 0, 0) for b in best),
      f"{len(res)} non-overlapping chains; {len(best)} best by contacts (score {m})")
A_, B_ = Vh[:4] - Vh[:4].mean(0), Vh[1:5] - Vh[1:5].mean(0)
U_, _, W_ = np.linalg.svd(B_.T @ A_); Rm = U_ @ W_
ang = np.arccos((np.trace(Rm) - 1) / 2); ax = np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]])
rise = abs((Vh[1:5].mean(0) - Vh[:4].mean(0)) @ ax / np.linalg.norm(ax))
check("[T] (3) the fold is a screw: per site a turn of arccos(-2/3) = 131.81 deg (cos rational and not 0, +-1/2, +-1, so "
      "the turn is an irrational part of a circle: no lattice period) and a rise of 1/sqrt10 edge",
      abs(np.cos(ang) + 2 / 3) < 1e-12 and abs(rise - 1 / np.sqrt(10)) < 1e-12, f"{np.degrees(ang):.4f} deg, rise {rise:.6f}")
def chain(Lc, nv=6, J1=1., J2=.5, t=.1):
    th = 2 * np.pi * np.arange(nv) / nv
    cfg = np.array(list(itertools.product(range(nv), repeat=Lc))); D = len(cfg); pw = nv ** np.arange(Lc)[::-1]; ix = cfg @ pw
    E = sum(-J1 * np.cos(th[cfg[:, i]] - th[cfg[:, i + 1]]) for i in range(Lc - 1)) \
        + sum(J2 * np.cos(th[cfg[:, i]] - th[cfg[:, i + 2]]) for i in range(Lc - 2))
    chi = sum(np.sin(th[cfg[:, i + 1]] - th[cfg[:, i]]) for i in range(Lc - 1))
    pm = lambda c2: sp.coo_matrix((np.ones(D), (c2 @ pw, ix)), shape=(D, D)).tocsr()
    K = sum(pm(np.where(np.arange(Lc) == i, (cfg + s) % nv, cfg)) for i in range(Lc) for s in (1, -1))
    H = -t * K + sp.diags(E); M = pm((-cfg) % nv); R = pm((cfg + 1) % nv); Id = sp.identity(D)
    pen = 20 * (Id - sum(R ** k for k in range(nv)) / nv)
    lo = lambda X_: sla.eigsh(X_, k=1, which='SA', v0=np.ones(D))[0][0]
    Ee, Eo = lo(H + pen + 10 * (Id - M)), lo(H + pen + 10 * (Id + M))
    w, v = sla.eigsh(H + pen, k=1, which='SA', v0=np.ones(D)); p = v[:, 0] ** 2
    Dodd = sp.diags(sum(np.sin(th[cfg[:, i + 1]] - th[cfg[:, i]]) for i in range(Lc - 1)))
    return dict(cl=np.unique(np.round(chi[np.isclose(E, E.min())], 2)), split=Eo - Ee, chi=(p * chi).sum(),
                Pp=p[chi > 1e-9].sum(), Pm=p[chi < -1e-9].sum(), Mc=abs(M @ H - H @ M).max(), Dodd=abs(M @ Dodd @ M + Dodd).max())
ch = {Lc: chain(Lc) for Lc in (4, 5, 6)}
check("[T] (4) a quantum register chain (Z_6 values per site, mirror-even frustrated preference -cos(d1) + 0.5 cos(d2), "
      "value hops t = 0.1): the classical minima are helices of both senses (6 sites: chirality +-2.6..4.3, none 0); the "
      "quantum vacuum is mirror-even with <chirality> = 0 and equal odds of each sense; the only sense-picking local term "
      "(sum sin d1, the DM form) is mirror-odd, so a mirror-keeping law cannot contain it",
      0 not in ch[6]['cl'] and all(abs(c['chi']) < 1e-9 and abs(c['Pp'] - c['Pm']) < 1e-9 and c['Mc'] < 1e-12
                                   and c['Dodd'] < 1e-12 for c in ch.values()),
      "P(+) = P(-) = " + ", ".join(f"{c['Pp']:.4f}" for c in ch.values()))
sp_ = [ch[L]['split'] for L in (4, 5, 6)]
check("[F] (4') the mirror-even/odd splitting (tunnelling between senses) falls with length: the sense is chosen "
      "spontaneously in the long-chain limit, with no law preference", sp_[0] > sp_[1] > sp_[2] > 0,
      "4, 5, 6 sites: " + ", ".join(f"{x:.4f}" for x in sp_))

# ---------------- C / D: the two-tiling tick ----------------
print("== C. the matter sea on handed textures (copy-massed two-tiling tick, 6^3 sites)")
V8 = list(itertools.product((0, 1), repeat=3)); sx = np.array([[0, 1], [1, 0.]]); sz = np.diag([1., -1]); I2 = np.eye(2)
kr = lambda a, b, c: np.kron(np.kron(a, b), c)
Wh = [kr(sx, I2, I2), kr(sz, sx, I2), kr(sz, sz, sx)]; G = kr(I2, sz, I2)
pol = np.diag([sum(v) - 1.5 for v in V8])
L = 6; N = L ** 3; X = np.array(list(itertools.product(range(L), repeat=3)))
def idx(x): return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
cubes = {par: [(2 * np.array(nn) + par, [idx(2 * np.array(nn) + par + np.array(v)) for v in V8])
               for nn in itertools.product(range(3), repeat=3)] for par in (0, 1)}
def w2(c, tex):
    cc = c + 0.5; out = np.ones(3) / 3; ii = np.arange(3)
    for kind, a, h in tex:
        phi = np.pi / 3 * cc.sum()
        if kind == 'helix': out = out + a * np.sin(phi - 2 * np.pi * ii * h / 3) / 3
        if kind == 'linear': out = out + a * np.array([1, -.5, -.5]) * np.sin(phi) / 3
        if kind == 'triple':
            for al in range(3): out = out + a / np.sqrt(3) * np.sin(np.pi / 3 * cc[al] - 2 * np.pi * (ii - al) * h / 3) / 3
    return out
def tick(tex=(), eps=.5, mu=.2, M=.6, gp=0.):
    Ms = []
    for par in (0, 1):
        Mx = np.zeros((N, N), complex)
        for c, ids in cubes[par]:
            R = sum(np.sqrt(wi) * Wi for wi, Wi in zip(w2(c, tex), Wh)); s = 1j * Wh[0] @ Wh[1] @ Wh[2] @ R
            if par == 0:
                C = expm(1j * (M / 4) * (np.eye(8) - s) @ R); Uc = C @ expm(-1j * ((eps - mu / 2) * R + gp * pol)) @ C
            else: Uc = expm(1j * (eps + mu / 2) * (G @ R @ G))
            Mx[np.ix_(ids, ids)] = Uc
        Ms.append(Mx)
    return Ms[1] @ Ms[0]
def perm(f):
    P = np.zeros((N, N))
    for i, x in enumerate(X): P[idx(f(x)), i] = 1
    return P
Iop = np.diag((-1.0) ** X[:, 1]) @ perm(lambda x: 1 - x)
gC3 = np.diag((-1.0) ** ((X[:, 0] * X[:, 1] + X[:, 0] * X[:, 2]) % 2)) @ perm(lambda x: np.array([x[2], x[0], x[1]]))
Tx = perm(lambda x: x + np.array([2, 0, 0]))
H1, Hm1 = [('helix', .3, 1)], [('helix', .3, -1)]
U0, Up, Um = tick(), tick(H1), tick(Hm1)
c0 = np.array([0., 0, 0]); swp = lambda c: np.array([c[1], c[0], c[2]])
okA = all(np.allclose(w2(swp(c), H1)[[1, 0, 2]], w2(c + np.array([-2, 0, 0]), Hm1)) for c in [rng.integers(0, 6, 3).astype(float) for _ in range(20)])
check("[T] (a) handedness is odd under every improper operation: I U(h) I^-1 = U(-h) exactly; the diagonal mirror maps "
      "the helix of sense h to the -h helix shifted by one cube (so A = sigma_d K, the texture being real, does too)",
      np.abs(Iop @ Up @ Iop.T - Um).max() < 1e-13 and okA, f"I: {np.abs(Iop @ Up @ Iop.T - Um).max():.0e}")
def Esea(U): w = np.angle(np.linalg.eigvals(U)); return w[w < 0].sum()
E0 = Esea(U0); dE = {}
for a in (.1, .2):
    dE[a] = (Esea(tick([('helix', a, 1)])) - E0, Esea(tick([('helix', a, -1)])) - E0, Esea(tick([('linear', a * np.sqrt(2), 0)])) - E0)
Epp, Epm = Esea(tick(H1, gp=.3)), Esea(tick(Hm1, gp=.3))
check("[T] (b) the two senses have equal vacuum quasi-energy, with the polar term too (I broken, A kept)",
      max(abs(d[0] - d[1]) for d in dE.values()) < 1e-11 and abs(Epp - Epm) < 1e-11, f"polar: {abs(Epp - Epm):.0e}")
r_h = dE[.2][0] / dE[.1][0]; dd = [(d[2] - d[0]) / d[0] for d in dE.values()]
check("[F] (c) handed vs unhanded at equal rms strain: equal at order a^2 (the cross term is the mirror-odd Lifshitz "
      "term), differ at higher order, and the bare sea's energy rises for both (no instability)", abs(r_h - 4) < .1 and 0 < dd[0] < dd[1] and min(d[0] for d in dE.values()) > 0,
      f"dE(helix) a=0.1: {dE[.1][0]:.3e}, a=0.2: {dE[.2][0]:.3e} (ratio {r_h:.2f}); lin-helix rel {dd[0]:.4f}, {dd[1]:.4f}")
print("   (d) CL-3 subtracts the vacuum phase of the same edges: the vacuum sea adds nothing at any texture (law text)")
qh = np.ones(3) / np.sqrt(3); Pq = np.eye(3) - np.outer(qh, qh)
fr = []
for pv in (np.cos(2 * np.pi * np.arange(3) / 3), np.sin(2 * np.pi * np.arange(3) / 3)):
    h = np.diag(pv); hTT = Pq @ h @ Pq - 0.5 * Pq * np.trace(Pq @ h); fr.append(np.sum(hTT ** 2) / np.sum(h ** 2))
check("[T] (e) the helical strain is traceless with no linear scalar curvature (q_i q_j h_ij = 0) but has a transverse-"
      "traceless part, which the hinge sum's static energy charges positively: the flat vacuum is the minimum",
      min(fr) > .1 and abs(np.trace(np.diag(np.cos(2 * np.pi * np.arange(3) / 3)))) < 1e-14, f"TT fraction {fr[0]:.3f}, {fr[1]:.3f}")

print("== D. the family term of handed textures (up mu = 0.20, down mu = 0.35, eps 0.5, M 0.6, a = 0.3)")
def fam_basis(U):
    Ps = []
    for j in range(3):
        k = 2 * np.pi / 3 * j * np.ones(3); Bm = np.zeros((N, 8), complex)
        for si, v in enumerate(V8):
            for nn in itertools.product(range(3), repeat=3): Bm[idx(2 * np.array(nn) + np.array(v)), si] = np.exp(1j * k @ np.array(nn)) / np.sqrt(27)
        w, vv = np.linalg.eig(Bm.conj().T @ U @ Bm); an = np.angle(w); o = [i for i in np.argsort(an) if an[i] > 1e-9][:2]
        Ps.append(Bm @ np.linalg.qr(vv[:, o])[0])
    return np.hstack(Ps)
P = fam_basis(tick(mu=.275))
def heff(tex, mu, gp=0.):
    h = P.conj().T @ (1j * logm(tick(tex, mu=mu, gp=gp))) @ P; return (h + h.conj().T) / 2
def sym_eigs(O): return np.round(np.angle(np.linalg.eigvals(P.conj().T @ O @ P)) / np.pi * 6).astype(int) % 12
Sx = Tx @ gC3
check("[T] (a) the commensurate helix (pitch 3 cubes along the family axis) is a screw: T(2 e_x) C3 commutes with its tick "
      "exactly, and on the six light family states its eigenvalues have multiplicities 3, 2, 1",
      np.abs(Sx @ Up @ np.linalg.inv(Sx) - Up).max() < 1e-13 and sorted(np.unique(sym_eigs(Sx), return_counts=True)[1]) == [1, 2, 3],
      f"[S, U] {np.abs(Sx @ Up @ np.linalg.inv(Sx) - Up).max():.0e}")
cases = {"helix": (H1, 0.), "helix + polar split": (H1, .3), "linear (unhanded)": ([('linear', .3, 0)], 0.),
         "triple helix (x, y, z)": ([('triple', .3, 1)], 0.), "distorted helix (+ 0.15 linear)": ([('helix', .3, 1), ('linear', .15, 0)], 0.)}
out = {}
for nm, (tex, gp) in cases.items():
    hu, hd = heff(tex, .2, gp), heff(tex, .35, gp); V = mixing(hu, hd); aV = np.abs(V)
    out[nm] = (aV.max(), int((aV < 1e-9).sum()), Jmax(V), np.linalg.eigvalsh(hu), np.linalg.eigvalsh(hd))
    print(f"   {nm:32s} max|V| {aV.max():.6f}  zeros {out[nm][1]:2d}  max|J| {out[nm][2]:.2e}")
Ut = tick(cases["triple helix (x, y, z)"][0])
check("[T] (b) every symmetric texture fails by the lemma: the helix and helix + polar split keep the screw (unit entry); "
      "the triple helix keeps the pure turn C3 about the family axis (unit entry); the unhanded wave keeps I (zeros)",
      all(out[k][0] > 1 - 1e-9 for k in ("helix", "helix + polar split", "triple helix (x, y, z)")) and out["linear (unhanded)"][1] >= 16
      and np.abs(gC3 @ Ut @ gC3.T - Ut).max() < 1e-13)
od = out["distorted helix (+ 0.15 linear)"]
check("[F] (c) a distorted helix (no screw, no turn, no I, no A) gives a mixing matrix with no zero and no unit entry and "
      "J != 0: the needed structure is a LOW-symmetry handed texture",
      od[0] < 1 - 1e-5 and od[1] == 0 and od[2] > 1e-6, f"max|V| {od[0]:.4f}, max|J| {od[2]:.2e}")
eu = np.abs(od[3]); ed = np.abs(od[4])
print(f"   [E] family quasi-energies (rad/tick) up {np.round(eu, 3)}, down {np.round(ed, 3)}: smallest/largest "
      f"{eu.min() / eu.max():.2f} (up), {ed.min() / ed.max():.2f} (down), set by the band at the three family momenta, "
      f"not by the texture; measured m_u/m_t = 1.3e-5, m_d/m_b = 1.1e-3: no hierarchy")

# ---------------- E ----------------
print("== E. weak chirality, pitch and the zoom ladder")
s3 = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1])]
m_, b0 = .3, .2; okW = True
for _ in range(20):
    p = rng.normal(size=3); ps = sum(pi * si for pi, si in zip(p, s3)); Z = np.zeros((2, 2))
    H = np.block([[ps + b0 * np.eye(2), m_ * np.eye(2)], [m_ * np.eye(2), -ps - b0 * np.eye(2)]])  # chiral basis, b0 gamma5
    pn = np.linalg.norm(p); ex = np.sort([sg * np.sqrt(m_ ** 2 + (pn + hh * b0) ** 2) for sg in (1, -1) for hh in (1, -1)])
    okW &= np.allclose(np.linalg.eigvalsh(H), ex)
check("[T] (a) a time-even handed background reaches a Dirac field as b0 gamma5 (P-odd, T-even): E = +-sqrt(m^2 + (|p| +- "
      "b0)^2), both helicities present at every momentum (20 seeded p): a shift, not a missing helicity, so a fold's "
      "handedness is not weak chirality", okW)
th = np.arccos(-2 / 3) / (2 * np.pi); near = [(k, abs(((k * th) % 1) - t)) for k in range(1, 31) for t in (1 / 3, 2 / 3)]
near = sorted(near, key=lambda z: z[1])[:4]
print("   [S] the fold's turn is 0.36614 of a circle: its multiples come within " + ", ".join(f"{d:.4f} (n={k})" for k, d in near)
      + " of a family character (1/3, 2/3): an incommensurate fold has no exact family hop; "
      "near-commensurate orders would stage it (not derived)")
print("   [S] zoom ladder: a fold of folds (a coiled coil) needs a frustrated preference at each rung; CL-1..CL-3 supply none")
print(f"elapsed {time.time() - t0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
