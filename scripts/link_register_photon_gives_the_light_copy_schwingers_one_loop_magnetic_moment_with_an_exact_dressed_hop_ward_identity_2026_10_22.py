AUDIT_INPUT_PATHS = ('docs/LINK_REGISTER_PHOTON_GIVES_THE_LIGHT_COPY_SCHWINGERS_ONE_LOOP_MAGNETIC_MOMENT_WITH_AN_EXACT_DRESSED_HOP_WARD_IDENTITY_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""g2-qlinks: one-loop anomalous magnetic moment of the CL-1 light copy coupled to the Gaussian (large-S) photon of the
site-bond link registers, on the lattice, and its continuum limit.

Supplied model.  CL-1 cube tick on flat equal edges (spin-3/2 edge hop W, even then odd 2^3 cubes, mass angle mu, copy
mass M on the copy with copy sign -1), taken in its small-step (Hamiltonian) limit: step eps = eta e0, mu = eta m,
M = eta M0, eta -> 0, e0 = sqrt3/2 (fermion cone c = 1 site per unit time).  Odd-cube hops dressed by the site phase
chi_s = e A_s of the site's own register (bond even centre -> odd centre), Ho -> exp(-i chi) Ho exp(i chi), even hops
undressed.  Registers in the Gaussian limit with the CL-3 skew-loop law of a flat cell (skew-light: electric weight
1/(s.s) per bond, magnetic weight 1/6 per skew loop; flat cell, so literal = Hodge reading), continuous time, a
Lorenz-type gauge fixing with weight w = 4/3 (Feynman form at small k), and a photon mass lam added to every mode
(Feynman-Stueckelberg infrared regulator).  A4 couples to the matter at even centres (the only centres that carry
matter charge in this frame).  One loop: vertex, two seagulls, tadpole (all from the exact BCH expansion of the
dressed hop), external-leg spinor corrections and the mass-angle counterterm (the dressed-rest-phase clause).
Euclidean frequency integrals by residues (continued from E = 0).  F2 = C_mag - C_conv: the spin-flip coefficient at
transfer q minus the convection coefficient at zero transfer, both relative to the tree vertex (cancels F1, Z2 and
every renormalisation of the dimension-4 terms).  Finite diagnostics; no physical identification beyond section F.
 A fermion rules   B photon rules   C Ward identities   D engine validation   E lattice F2   F estimates
"""
import itertools, os, signal, time
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm, logm
from scipy.integrate import quad
np.seterr(divide='ignore', invalid='ignore')
T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261022)
# ------------------------------------------------------------------ CL-1 cube hop (as in g2-copy / fermion-cones)
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); X8 = C8.astype(float); DA = 2 * X8 - 1
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); NV = (2 * C8 - 1.0) / r3; XI = []
for i in range(8):
    _, v_ = np.linalg.eigh(sum(NV[i, k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex); WAX = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(a + 1, 8):
        if np.sum(abs(C8[a] - C8[b])) == 1:
            g_ = XI[a].conj() @ XI[b]; x = -g_ / abs(g_) / r3; ax = int(np.argmax(abs(C8[a] - C8[b])))
            for Mx in (W, WAX[ax]): Mx[a, b] = x; Mx[b, a] = np.conj(x)
S3 = 1j * r3 ** 3 * WAX[0] @ WAX[1] @ WAX[2] @ W; PH = (np.eye(8) - S3) / 2; e0 = r3 / 2
def Hparts(K, m0, M0):
    """position-phase Bloch Hamiltonian (8 sites of the even cube); returns (H, odd part)"""
    D = np.exp(1j * K @ C8.T)
    He = D.conj()[:, :, None] * ((e0 - m0 / 2) * W - M0 * PH @ W)[None] * D[:, None, :]
    Ho = D[:, :, None] * (-(e0 + m0 / 2) * W)[None] * D.conj()[:, None, :]
    return He + Ho, Ho
# ------------------------------------------------------------------ registers: skew-loop Gaussian law (skew-light)
SG = [np.array(s) for s in itertools.product((-1, 1), repeat=3)]; SIDX = {tuple(s): i for i, s in enumerate(SG)}
D4 = [np.array(d) for d in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1))]; DIDX = {tuple(d): i for i, d in enumerate(D4)}
S4 = np.array(D4, float)
LOOPS = {}
for start in (np.zeros(3, int), np.ones(3, int)):
    for ss in itertools.product(range(8), repeat=3):
        st = [SG[i] for i in ss]; s4 = -(st[0] + st[1] + st[2])
        if tuple(s4) not in SIDX: continue
        st.append(s4); vs = [start.copy()]
        for s in st: vs.append(vs[-1] + s)
        if len({tuple(v) for v in vs[:4]}) < 4: continue
        if not (np.count_nonzero(vs[2] - vs[0]) == 1 and np.count_nonzero(vs[3] - vs[1]) == 1): continue
        mn = np.array(min(map(tuple, vs[:4]))); vt = [v - mn for v in vs]
        LOOPS.setdefault(frozenset(frozenset((tuple(vt[j]), tuple(vt[j + 1]))) for j in range(4)), vt)
def step_bond(v, s): return (v, DIDX[tuple(s)], 1) if s[0] == 1 else (v + s, DIDX[tuple(-s)], -1)
LOOPINFO = [[step_bond(vt[j], vt[j + 1] - vt[j]) for j in range(4)] for vt in LOOPS.values()]
ME = np.array([1 / (s @ s) for s in S4]); WPL = 1 / 6
def Kmat(k):
    C = np.zeros((len(k), len(LOOPINFO), 4), complex)
    for i, st in enumerate(LOOPINFO):
        for x, t, sg in st: C[:, i, t] += sg * np.exp(1j * k @ np.array(x, float))
    return WPL * np.einsum('nit,nis->nts', C.conj(), C)
def gvec(k): return np.exp(1j * k @ S4.T) - 1
def photon(k, lam, w=4 / 3):
    """modes (omega^2 (N,5)) and coupling vectors (N, 4 bonds + A4, mode) of the gauge-fixed register law"""
    g = gvec(k); Kt = Kmat(k) + np.einsum('nt,ns->nts', g * ME, (g * ME).conj()) / w
    om2, y = np.linalg.eigh(3 * Kt); V = np.zeros((len(k), 5, 5), complex); V[:, :4, :4] = np.sqrt(3) * y; V[:, 4, 4] = 1 / np.sqrt(w)
    ob = np.einsum('nt,t,nt->n', g.conj(), ME, g).real / w
    return np.concatenate([om2, ob[:, None]], 1) + lam ** 2, V
# site -> its register bond (type, start centre, orientation); bcc centre coordinates
SIT = [(DIDX[tuple(DA[a].astype(int))], np.zeros(3), 1.0) if DA[a, 0] == 1 else (DIDX[tuple(-DA[a].astype(int))], DA[a], -1.0) for a in range(8)]
TT = np.array([s[0] for s in SIT]); XS = np.array([s[1] for s in SIT]); SGN = np.array([s[2] for s in SIT])
def Xt(k):
    ph = np.exp(1j * np.einsum('ni,ai->na', k, XS - X8)) * SGN[None]; out = np.zeros((len(k), 4, 8), complex)
    for a in range(8): out[:, TT[a], a] = ph[:, a]
    return out
def ad(Xd, kX, Op): return lambda K: Xd[:, :, None] * Op(K) - Op(K + kX) * Xd[:, None, :]
XE = DA[:, 0].astype(complex)   # external field along x: chi = A d_x
class Model:
    def __init__(s, m0, M0, A=0.0):
        ph = np.exp(-1j * A * XE); s.m0, s.M0 = m0, M0
        s.Ho = lambda K: ph[None, :, None] * Hparts(K, m0, M0)[1] * ph.conj()[None, None, :]
        s.H = lambda K: (lambda h: h[0] - h[1] + s.Ho(K))(Hparts(K, m0, M0))
    def vert(s, Kin, k):
        X = Xt(k); Vt = -1j * (X[:, :, :, None] * s.Ho(Kin)[:, None] - s.Ho(Kin + k)[:, None] * X[:, :, None, :])
        return np.concatenate([Vt, (1j * np.exp(-1j * k @ X8.T)[:, :, None] * np.eye(8)[None])[:, None]], 1)
    def ext(s, Kin, q, Op=None):
        Xe = np.repeat(XE[None], len(Kin), 0); return -1j * ad(Xe, np.repeat(q[None], len(Kin), 0), Op or s.Ho)(Kin)
    def dmu(s, K):
        D = np.exp(1j * K @ C8.T); Wo = D[:, :, None] * W[None] * D.conj()[:, None, :]
        return -0.5 * (D.conj()[:, :, None] * W[None] * D[:, None, :] + Wo), -0.5 * Wo
# ------------------------------------------------------------------ frequency integrals (residues, continued from E = 0)
def fint(a, b, om, sa, sb):
    def mix(x, y): B = -y; return -(x + B + 2 * om) / (2 * om * (x + om) * (x + B) * (om + B))
    return np.where((sa > 0) & (sb > 0), 1 / (2 * om * (a + om) * (b + om)),
                    np.where((sa < 0) & (sb < 0), 1 / (2 * om * (om - a) * (om - b)), np.where(sa > 0, mix(a, b), mix(b, a))))
def gint(b, om, sb): return np.where(sb > 0, 1 / (2 * om * (b + om)), -1 / (2 * om * (om - b)))
# ------------------------------------------------------------------ one-loop pieces
def loop_all(md, Phf, kpts, wts, pp, p, uo, ui, Eo_, Ei_, chunk=1200):
    q = pp - p; acc = {'vertex': 0, 'seagull': 0, 'tadpole': 0}
    for s in range(0, len(kpts), chunk):
        k = kpts[s:s + chunk]; wv = wts[s:s + chunk]; N = len(k); K1 = pp[None] - k; K2 = p[None] - k; P = np.repeat(p[None], N, 0)
        E1, U1 = np.linalg.eigh(md.H(K1)); E2, U2 = np.linalg.eigh(md.H(K2)); om2, PV = Phf(k); om = np.sqrt(om2)
        AL = np.einsum('nml,nmab->nlab', PV, md.vert(K1, k)); AR = np.einsum('nml,nmab->nlab', PV.conj(), md.vert(P, -k))
        Lb = np.einsum('as,nlab,nbc->nlsc', uo.conj(), AL, U1); Rb = np.einsum('nac,nlab,bs->nlcs', U2.conj(), AR, ui)
        Dm = np.einsum('nac,nab,nbd->ncd', U1.conj(), md.ext(K2, q), U2)
        f = fint((E1 - Eo_)[:, None, :, None], (E2 - Ei_)[:, None, None, :], om[:, :, None, None], np.sign(E1)[:, None, :, None], np.sign(E2)[:, None, None, :])
        acc['vertex'] += np.einsum('n,nlsc,nlcd,nlde->se', wv, Lb, f * Dm[:, None], Rb, optimize=True)
        Xk = Xt(k); Xmk = Xt(-k); Xe = np.repeat(XE[None], N, 0); qb = np.repeat(q[None], N, 0)
        for l in range(4):
            Xl = np.einsum('nt,nta->na', PV[:, :4, l], Xk); Xlt = np.einsum('nt,nta->na', PV[:, :4, l].conj(), Xmk)
            SL = -ad(Xe, qb, ad(Xl, k, md.Ho))(K2); SR = -ad(Xe, qb, ad(Xlt, -k, md.Ho))(P)
            left = np.einsum('as,nab,nbc->nsc', uo.conj(), SL, U2) * gint(E2 - Ei_, om[:, l:l + 1], np.sign(E2))[:, None, :]
            right = np.einsum('nac,nab,bs->ncs', U1.conj(), SR, ui) * gint(E1 - Eo_, om[:, l:l + 1], np.sign(E1))[:, :, None]
            acc['seagull'] -= np.einsum('n,nsc,ncd->sd', wv, left, Rb[:, l]) + np.einsum('n,nsc,ncd->sd', wv, Lb[:, l], right)
            T = 0.5j * ad(Xe, qb, ad(Xl, k, ad(Xlt, -k, md.Ho)))(P) / (2 * om[:, l])[:, None, None]
            acc['tadpole'] += np.einsum('n,as,nab,bd->sd', wv, uo.conj(), T, ui)
    return acc
def sigma(md, Phf, kpts, wts, p, E, chunk=1200):
    acc = 0
    for s in range(0, len(kpts), chunk):
        k = kpts[s:s + chunk]; wv = wts[s:s + chunk]; N = len(k); K2 = p[None] - k; P = np.repeat(p[None], N, 0)
        E2, U2 = np.linalg.eigh(md.H(K2)); om2, PV = Phf(k); om = np.sqrt(om2)
        AL = np.einsum('nml,nmab->nlab', PV, md.vert(K2, k)); AR = np.einsum('nml,nmab->nlab', PV.conj(), md.vert(P, -k))
        g = gint((E2 - E)[:, None, :], om[:, :, None], np.sign(E2)[:, None, :])
        acc = acc - np.einsum('n,nlab,nbc,nlc,ndc,nlde->ae', wv, AL, U2, g, U2.conj(), AR, optimize=True)
        Xk = Xt(k); Xmk = Xt(-k)
        for l in range(4):
            Xl = np.einsum('nt,nta->na', PV[:, :4, l], Xk); Xlt = np.einsum('nt,nta->na', PV[:, :4, l].conj(), Xmk)
            acc = acc + np.einsum('n,nab->ab', wv, -0.5 * ad(Xl, k, ad(Xlt, -k, md.Ho))(P) / (2 * om[:, l])[:, None, None])
    return acc
def light(Hm, u0=None):
    E, U = np.linalg.eigh(Hm); pos = np.where(E > 0)[0]; idx = pos[np.argsort(E[pos])[:2]]
    if u0 is None: return E[idx].mean(), U[:, idx]
    v = U[:, idx] @ U[:, idx].conj().T @ u0; s_, V_ = np.linalg.eigh(v.conj().T @ v)
    return E[idx].mean(), v @ V_ @ np.diag(s_ ** -0.5) @ V_.conj().T
def bz_grid(Ns, Nu, smin):
    """one bcc zone (rhombic dodecahedron) as 12 pyramids, log-graded towards k = 0; sum w F = int_[-pi,pi]^3 F d3k/(2pi)^3"""
    t, wt = np.polynomial.legendre.leggauss(Ns); gl = np.log(1 / smin)
    s = np.exp(gl * (t - 1) / 2) - smin * (1 - t) / 2; ws = wt * (gl / 2 * np.exp(gl * (t - 1) / 2) + smin / 2)
    u, wu = np.polynomial.legendre.leggauss(Nu); Sg, Tg = [z.ravel() for z in np.meshgrid(u, u, indexing='ij')]; Wst = np.outer(wu, wu).ravel()
    pts = []; wts = []; h = np.pi / 2; E = np.eye(3)
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        for si in (1, -1):
            for sj in (1, -1):
                c = h * (si * E[i] + sj * E[j]); A = h * (si * E[i] - sj * E[j]); B = h * E[3 - i - j]
                F = c[None] + ((Sg + Tg) / 2)[:, None] * A[None] + ((Sg - Tg) / 2)[:, None] * B[None]
                jac = abs(np.linalg.det(np.stack([c, (A + B) / 2, (A - B) / 2])))
                pts.append((s[:, None, None] * F[None]).reshape(-1, 3)); wts.append((ws[:, None] * s[:, None] ** 2 * Wst[None] * jac).ravel())
    return np.concatenate(pts), 4 * np.concatenate(wts) / (2 * np.pi) ** 3
def F2run(md, Phf, kpts, wts, dq, spin=False):
    ey = np.array([0, 1.0, 0]); ex = np.array([1.0, 0, 0]); E00, u0 = light(md.H(np.zeros((1, 3)))[0]); out = {}
    if spin:
        S0 = sigma(md, Phf, kpts, wts, np.zeros(3), E00); dmu = np.trace(u0.conj().T @ S0 @ u0).real / np.trace(u0.conj().T @ md.dmu(np.zeros((1, 3)))[0][0] @ u0).real; out['dmu'] = dmu
    for name, (pf, pi) in {'mag': (lambda s: s * dq / 2 * ey, lambda s: -s * dq / 2 * ey), 'conv': (lambda s: s * dq * ex, lambda s: s * dq * ex)}.items():
        dA = {}; dT = 0
        for s in (1, -1):
            pp, p = pf(s), pi(s); Hp, Hq = md.H(pp[None])[0], md.H(p[None])[0]; Eo_, uo = light(Hp, u0); Ei_, ui = light(Hq, u0)
            A = loop_all(md, Phf, kpts, wts, pp, p, uo, ui, Eo_, Ei_); T = uo.conj().T @ md.ext(p[None], pp - p)[0] @ ui
            if spin:
                So = sigma(md, Phf, kpts, wts, pp, Eo_); Si = So if name == 'conv' else sigma(md, Phf, kpts, wts, p, Ei_)
                So = (So + So.conj().T) / 2 - dmu * md.dmu(pp[None])[0][0]; Si = (Si + Si.conj().T) / 2 - dmu * md.dmu(p[None])[0][0]
                h = 1e-4; A['legs'] = sum(e * (light(Hp + e * h * So, u0)[1].conj().T @ md.ext(p[None], pp - p)[0] @ light(Hq + e * h * Si, u0)[1]) for e in (1, -1)) / (2 * h)
                A['ct'] = -dmu * (uo.conj().T @ md.ext(p[None], pp - p, lambda K: md.dmu(K)[1])[0] @ ui)
            for kk, v in A.items(): dA[kk] = dA.get(kk, 0) + s * v
            dT = dT + s * T
        nT = np.trace(dT.conj().T @ dT).real; tot = sum(dA.values())
        out[name] = {kk: np.trace(dT.conj().T @ v).real / nT for kk, v in dA.items()}
        out[name]['res'] = np.linalg.norm(tot - sum(out[name][kk] for kk in dA) * dT) / np.linalg.norm(tot)
    out['F2'] = {kk: out['mag'][kk] - out['conv'][kk] for kk in out['mag'] if kk != 'res'}
    return out
A2P = 3 / (4 * np.pi) / (2 * np.pi)    # alpha/2pi for e = 1 (B3)
def Fcont(r): return quad(lambda z: 2 * z * (1 - z) ** 2 / ((1 - z) ** 2 + z * r * r), 0, 1)[0]
def lattice_F2(m0, M0=0.6, r=1.0, Ns=18, Nu=5, spin=False):
    md = Model(m0, M0); kp, kw = bz_grid(Ns, Nu, 0.03 * m0 / np.pi)
    return F2run(md, lambda k: photon(k, r * m0), kp, kw, 0.01 * m0, spin)

# ================================================================== A
print('== A. fermion rules: CL-1 tick -> Hamiltonian limit, light copy = Dirac (exact/finite)')
K = np.array([[0.3, -0.2, 0.5]]); m0, M0 = 0.1, 0.6; errs = []
for eta in (2e-3, 1e-3):
    F = expm(1j * eta * M0 / 2 * PH @ W); Ue = F @ expm(-1j * eta * (e0 - m0 / 2) * W) @ F; Eo = expm(1j * eta * (e0 + m0 / 2) * W)
    D = np.exp(1j * C8 @ K[0]); U = (D[:, None] * Eo * D.conj()[None]) @ (D.conj()[:, None] * Ue * D[None])
    errs.append(np.abs(1j * logm(U) / eta - Hparts(K, m0, M0)[0][0]).max())
check('A1 tick generator (i/eta) log U(K) -> H(K) = even hop (e0 - mu/2) W - M PH W, odd hop -(e0 + mu/2) W, error O(eta)',
      errs[1] < 1e-3 and 1.8 < errs[0] / errs[1] < 2.2, f'{errs[0]:.1e}, {errs[1]:.1e}')
ev0 = np.linalg.eigvalsh(Hparts(np.zeros((1, 3)), m0, M0)[0][0]); evc = np.linalg.eigvalsh(Hparts(np.pi / 2 * np.ones((1, 3)), m0, M0)[0][0])
check('A2 K = 0: light copy +-m (x2), heavy copy +-(m + M) (x2); zone corner: +-|2 e0 - M|, +-2 e0; [s, W] = 0',
      np.allclose(ev0, [-.7, -.7, -.1, -.1, .1, .1, .7, .7]) and np.allclose(sorted(np.abs(evc)), sorted([r3 - .6] * 4 + [r3] * 4)) and abs(S3 @ W - W @ S3).max() < 1e-13,
      'corner ' + ', '.join(f'{x:.4f}' for x in sorted(set(np.round(np.abs(evc), 4)))))
E0, U0 = np.linalg.eigh(Hparts(np.zeros((1, 3)), m0, M0)[0][0]); P4 = U0[:, np.abs(E0) < .2]
h = 1e-6; vm = [P4.conj().T @ ((Hparts(h * np.eye(3)[i][None], m0, M0)[0][0] - Hparts(-h * np.eye(3)[i][None], m0, M0)[0][0]) / (2 * h)) @ P4 for i in range(3)]
beta = P4.conj().T @ Hparts(np.zeros((1, 3)), m0, M0)[0][0] @ P4 / m0; cl = max(abs(vm[i] @ vm[j] + vm[j] @ vm[i] - 2 * (i == j) * np.eye(4)).max() for i in range(3) for j in range(3))
cl = max(cl, max(abs(vm[i] @ beta + beta @ vm[i]).max() for i in range(3)), abs(beta @ beta - np.eye(4)).max())
check('A3 light block at small p is the Dirac Hamiltonian c alpha.p + beta m: {v_i, v_j} = 2 c^2 delta_ij, {v_i, beta} = 0, c = 1',
      cl < 1e-8, f'Clifford defect {cl:.1e}')
gl = []
for mm in (0.4, 0.2, 0.1):
    md = Model(mm, 0.6); _, u0 = light(md.H(np.zeros((1, 3)))[0]); dq = 1e-4 * mm; ey = np.array([0, 1., 0]); ex = np.array([1., 0, 0])
    _, uo = light(md.H((dq / 2 * ey)[None])[0], u0); _, ui = light(md.H((-dq / 2 * ey)[None])[0], u0)
    T = uo.conj().T @ md.ext((-dq / 2 * ey)[None], dq * ey)[0] @ ui; Ep = light(md.H((1e-3 * ex)[None])[0])[0]; ck2 = (Ep ** 2 - mm ** 2) / 1e-6
    gl.append((np.abs(np.linalg.eigvals(T)).max() * 2 / dq * mm / ck2, ck2))
check('A4 tree level: the dressed-hop vertex gives g = 2 against the kinetic cone (c_kin^2 = 1 - m^2/3 + ...), copy mass on',
      all(abs(g - 1) < 1e-5 for g, _ in gl), 'g/2 - 1 = ' + ', '.join(f'{g - 1:.0e}' for g, _ in gl) + '; c_kin^2 ' + ', '.join(f'{c:.4f}' for _, c in gl))

# ================================================================== B
print('== B. photon rules: Gaussian site-bond registers, skew-loop plaquettes (flat cell)')
kr = rng.normal(size=(5, 3)); Kg = np.abs(np.einsum('nts,ns->nt', Kmat(kr), gvec(kr))).max()
check('B1 6 skew loops per bcc cell; plaquettes gauge invariant (K g = 0 at random k)', len(LOOPINFO) == 6 and Kg < 1e-13, f'|K g| = {Kg:.0e}')
cone = []; extra = []; gm = []
for n in (np.array([1., 0, 0]), np.ones(3) / r3, np.array([1., 2, 0]) / 5 ** .5):
    for kk in (1e-2, 5e-3):
        k = kk * n[None]; om2, V = photon(k, 0.0); om = np.sqrt(np.abs(om2[0])) / kk
        cone.append(np.sort(om[:4])[:3]); extra.append(np.sort(om2[0, :4])[-1]); gm.append(om[4])
cone = np.array(cone); dev = np.abs(cone - 1).max(axis=1)
check('B2 small k: two transverse modes and the gauge mode on omega = |k| (c_gamma = c_fermion = 1), the A4 mode too (w = 4/3), error O(k^2); fourth (copy-sign) mode gapped',
      dev[1::2].max() < 1e-4 and dev[0::2].max() / dev[1::2].max() > 3 and abs(np.array(gm) - 1).max() < 1e-4 and min(extra) > 1,
      f'max |omega/k - 1| {dev[1::2].max():.1e} at k = .005; A4 {abs(np.array(gm) - 1).max():.1e}; extra omega^2 >= {min(extra):.2f}')
k = 1e-3 * np.array([[0.3, 0.5, 0.8]]); epsc = (np.einsum('nt,t,nt->n', gvec(k).conj(), ME, gvec(k)).real / np.sum(k * k))[0]
om2, V = photon(k, 0.0); it = np.argsort(om2[0, :4])[:3]; ct = [np.linalg.norm(S4.T @ V[0, :4, l] / 4) ** 2 * epsc for l in it]
check('B3 medium: electric constant eps_c = 4/3 per cell of volume 4 and every small-k mode has Cartesian residue 1/eps_c: alpha = e^2 V_c/(4 pi eps_c c) = 3 e^2/(4 pi)',
      abs(epsc - 4 / 3) < 1e-6 and max(abs(np.array(ct) - 1)) < 1e-5, f'eps_c {epsc:.6f}; residues x eps_c ' + ', '.join(f'{c:.6f}' for c in ct))

# ================================================================== C
print('== C. Ward identities')
md = Model(0.1, 0.6); wt1 = 0
for _ in range(3):
    Kr = rng.uniform(-2, 2, (1, 3)); kq = rng.uniform(-2, 2, (1, 3)); k0, w0 = rng.uniform(-1, 1, 2)
    V = md.vert(Kr, kq)[0]; Lm = np.diag(np.exp(-1j * kq[0] @ X8.T))
    lhs = np.einsum('t,tab->ab', gvec(kq)[0], V[:4]) + 1j * k0 * V[4]
    rhs = 1j * (Lm @ (md.H(Kr)[0] - 1j * w0 * np.eye(8)) - (md.H(Kr + kq)[0] - 1j * (w0 + k0) * np.eye(8)) @ Lm)
    wt1 = max(wt1, abs(lhs - rhs).max())
check('C1 THEOREM (exact, all orders in the site phase; checked at random finite k, k0): pure-gauge register mode x vertex = i(Lambda G^-1(K) - G^-1(K+k) Lambda)',
      wt1 < 1e-13, f'{wt1:.0e}')
I8 = np.eye(8, dtype=complex); Phf = lambda x: photon(x, 0.05); wt2 = 0; vo = 0
for _ in range(3):
    kk = rng.uniform(-2, 2, (1, 3)); p = rng.uniform(-.05, .05, 3); E = rng.uniform(0, .2)
    G1 = loop_all(md, Phf, kk, np.ones(1), p, p, I8, I8, E, E); hA = 1e-5
    dS = (sigma(Model(.1, .6, hA), Phf, kk, np.ones(1), p, E) - sigma(Model(.1, .6, -hA), Phf, kk, np.ones(1), p, E)) / (2 * hA)
    wt2 = max(wt2, abs(G1['vertex'] + G1['seagull'] + G1['tadpole'] - dS).max() / abs(dS).max()); vo = max(vo, abs(G1['vertex'] - dS).max() / abs(dS).max())
check('C2 one-loop Ward identity at fixed loop momentum: zero-transfer vertex + seagulls + tadpole = d Sigma/dA (vertex alone fails)',
      wt2 < 1e-6 and vo > 0.1, f'rel. miss {wt2:.0e}; vertex alone {vo:.2f}')

# ================================================================== D
print('== D. engine validation')
import mpmath as mp
fe = 0
for (a, b, w_) in ((.3, .7, .5), (-.3, -.9, .4), (.3, -.9, .4), (.05, -2., 1.3)):
    nq = complex(mp.quad(lambda x: 1 / ((a + 1j * x) * (b + 1j * x) * (x * x + w_ * w_)), [-mp.inf, 0, mp.inf]) / (2 * mp.pi))
    ng = complex(mp.quad(lambda x: 1 / ((b + 1j * x) * (x * x + w_ * w_)), [-mp.inf, 0, mp.inf]) / (2 * mp.pi))
    fe = max(fe, abs(nq - fint(a, b, w_, np.sign(a), np.sign(b))), abs(ng - gint(b, w_, np.sign(b))))
check('D1 residue formulas for the two- and one-propagator frequency integrals = quadrature', fe < 1e-10, f'{fe:.0e}')
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex); Z2 = np.zeros((2, 2))
AL4 = np.array([np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]); BE4 = np.block([[s0, Z2], [Z2, -s0]]).astype(complex)
class Dirac:
    def __init__(s, m): s.H = lambda K: np.einsum('ni,iab->nab', K, AL4) + m * BE4[None]
def dirac_F2(m, r, Ns, Nu):
    d = Dirac(m); lam = r * m; kp, kw = bz_grid(Ns, Nu, 0.03 * m / np.pi); kw = kw / 4; ey = np.array([0, 1., 0]); ex = np.array([1., 0, 0])
    _, u0 = light(d.H(np.zeros((1, 3)))[0]); C = {}
    for name, (pf, pi) in {'mag': (lambda s: s * .005 * m * ey, lambda s: -s * .005 * m * ey), 'conv': (lambda s: s * .01 * m * ex, lambda s: s * .01 * m * ex)}.items():
        dL = 0; dT = 0
        for sgn in (1, -1):
            pp, p = pf(sgn), pi(sgn); Eo_, uo = light(d.H(pp[None])[0], u0); Ei_, ui = light(d.H(p[None])[0], u0); acc = 0
            E1, U1 = np.linalg.eigh(d.H(pp[None] - kp)); E2, U2 = np.linalg.eigh(d.H(p[None] - kp)); om = np.sqrt(np.sum(kp * kp, 1) + lam ** 2)
            Vs = [-AL4[0], -AL4[1], -AL4[2], 1j * np.eye(4)]
            f = fint((E1 - Eo_)[:, :, None], (E2 - Ei_)[:, None, :], om[:, None, None], np.sign(E1)[:, :, None], np.sign(E2)[:, None, :])
            Dm = np.einsum('nac,ab,nbd->ncd', U1.conj(), -AL4[0], U2)
            for V_ in Vs:
                acc = acc + np.einsum('n,sa,nac,ncd,nbd,be->se', kw, uo.conj().T @ V_, U1, f * Dm, U2.conj(), V_ @ ui, optimize=True)
            dL = dL + sgn * acc; dT = dT + sgn * (uo.conj().T @ (-AL4[0]) @ ui)
        C[name] = np.trace(dT.conj().T @ dL).real / np.trace(dT.conj().T @ dT).real
    return (C['mag'] - C['conv']) * 8 * np.pi ** 2
dv = [(r, dirac_F2(m, r, 30, 10), Fcont(r)) for m, r in ((0.05, 1.0), (0.02, 0.25))]
check('D2 continuum Dirac + Feynman-Stueckelberg photon (same engine, cutoff region |k_i| + |k_j| < pi): F2/(alpha/2pi) = int 2z(1-z)^2/((1-z)^2 + z r^2), r = lam/m',
      all(abs(a / b - 1) < 2e-3 for _, a, b in dv), '; '.join(f'r {r}: {a:.5f} vs {b:.5f}' for r, a, b in dv) + '  (Schwinger: r -> 0 gives 1)')
print(f'   [{time.time() - T0:.0f} s]')

# ================================================================== E
print('== E. lattice one-loop F2/(alpha/2pi), photon mass lam = r m, copy mass M = .6, e0 = sqrt3/2 (c = 1)')
o = lattice_F2(0.05, spin=True); P = {k: v / A2P for k, v in o['F2'].items()}
print('   m = .05 parts: ' + ', '.join(f'{k} {v:+.5f}' for k, v in P.items()) + f';  mass counterterm dmu = {o["dmu"]:.4f} e^2 = {o["dmu"] / (3 / (4 * np.pi)):.3f} alpha')
check('E1 external-leg spinor corrections + mass-angle counterterm cancel to < 2e-3 (tree g = 2 holds across the CL-1 family); structure fits the tree spin matrix',
      abs(P['legs'] + P['ct']) < 2e-3 and max(o['mag']['res'], o['conv']['res']) < 1e-8, f"legs + ct = {P['legs'] + P['ct']:+.1e}; fit residual {max(o['mag']['res'], o['conv']['res']):.0e}")
F1PI = sum(P[k] for k in ('vertex', 'seagull', 'tadpole')); Fc1 = Fcont(1.0)
ms = [0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625]; rows = []
for mm in ms:
    if mm == 0.05: rows.append((mm, P['vertex'], P['seagull'], F1PI)); continue
    Ns = 18 + max(0, int(round(2 * np.log2(0.05 / mm)))); oo = lattice_F2(mm, Ns=Ns)
    rows.append((mm, oo['F2']['vertex'] / A2P, oo['F2']['seagull'] / A2P, sum(oo['F2'][k] for k in ('vertex', 'seagull', 'tadpole')) / A2P))
print('   m a       vertex    seagull    total     total - F(1)   (F(1) = %.5f, continuum, r = 1)' % Fc1)
for mm, v, s, t in rows: print(f'   {mm:<8}  {v:+.5f}  {s:+.5f}  {t:+.5f}  {t - Fc1:+.5f}')
mm = np.array([r_[0] for r_ in rows]); FF = np.array([r_[3] for r_ in rows]); dd = FF - Fc1
ext = [np.linalg.lstsq(np.stack([np.ones_like(mm[s]), mm[s] * np.log(mm[s]), mm[s]] + ([mm[s] ** 2] if q4 else []), 1), FF[s], rcond=None)[0][0]
       for s in (slice(0, 6), slice(1, 6), slice(2, 6)) for q4 in (0, 1)]
check('E2 continuum limit: the lattice deviation shrinks monotonically, about halving with m (m ln m), and the fits F + m(a ln m + b) [+ c m^2] extrapolate to the continuum F(1) within 3%',
      np.all(np.diff(np.abs(dd)) < 0) and abs(dd[-1] / dd[-2] - 0.55) < 0.12 and all(abs(e / Fc1 - 1) < 0.03 for e in ext),
      f'last ratio {dd[-1] / dd[-2]:.3f}; extrapolations {min(ext):.4f} .. {max(ext):.4f} vs {Fc1:.4f}')
dr = []
for m_ in (0.05, 0.025):
    oo = lattice_F2(m_, r=0.25, Ns=20); dr.append(sum(oo['F2'][k] for k in ('vertex', 'seagull', 'tadpole')) / A2P - Fcont(0.25))
d1 = dd[[ms.index(.05), ms.index(.025)]]
check('E3 the lattice deviation is an ultraviolet term: at r = 1/4 it is within 10% of its r = 1 value (so with lam -> 0, a -> (alpha/2pi)(1 + dev))',
      all(abs(a / b - 1) < 0.1 for a, b in zip(dr, d1)), ', '.join(f'{a:+.4f} vs {b:+.4f}' for a, b in zip(dr, d1)))
dM = []
for MM in (0.3, 1.0):
    oo = lattice_F2(0.05, M0=MM); dM.append(sum(oo['F2'][k] for k in ('vertex', 'seagull', 'tadpole')) / A2P - Fc1)
check('E4 copy mass M = .3, .6, 1.0 at m = .05: the deviation is not set by m/M (changes < 15%, non-monotonic): copies enter only through the lattice term',
      all(abs(x / d1[0] - 1) < 0.15 for x in dM), ', '.join(f'{x:+.4f}' for x in dM) + f' vs {d1[0]:+.4f}')
og = lattice_F2(0.05, Ns=24, Nu=7); fg = sum(og['F2'][k] for k in ('vertex', 'seagull', 'tadpole')) / A2P
check('E5 zone-grid convergence at m = .05 (18x5x5 -> 24x7x7 per pyramid)', abs(fg - F1PI) < 1e-3, f'{F1PI:.5f} -> {fg:.5f}')

# ================================================================== F
print('== F. ESTIMATES (measured numbers supplied; not theorems)')
al = 1 / 137.035999; a_meas, s_meas = 1.15965218059e-3, 1.3e-13; lP = 1.616255e-35; lC = 3.8615926796e-13
ma = np.sqrt(8 * np.pi) * lP / lC; cf = np.linalg.lstsq(np.stack([mm * np.log(mm), mm], 1), dd, rcond=None)[0]
dlat = al / (2 * np.pi) * ma * (cf[0] * np.log(ma) + cf[1])
print(f'   alpha/2pi = {al / 2 / np.pi:.9e} (Schwinger term; measured a_e = {a_meas:.11e} +- {s_meas:.1e}, the rest is higher-order QED)')
print(f'   lattice term at site spacing sqrt(8 pi) l_P: m a = {ma:.2e}; dev ~ m a ({cf[0]:.2f} ln(m a) {cf[1]:+.2f}) -> delta a ~ {dlat:.1e} ({abs(dlat) / s_meas:.0e} x precision)')
vp2 = (al / np.pi) ** 2 * (119 / 36 - np.pi ** 2 / 3); hv = (al / np.pi) ** 2 / 45 * (ma / 0.6) ** 2
print(f'   second LIGHT copy (M = 0): one-loop vacuum polarisation inside the photon, i.e. TWO loops in a_e: (alpha/pi)^2 (119/36 - pi^2/3) = {vp2:.3e} = {vp2 / s_meas:.1e} x precision')
print(f'   heavy copy / zone-corner partners (mass ~ .6/a): one loop inside the lattice term above; two-loop VP (alpha/pi)^2 (m a/M)^2/45 = {hv:.0e}')
check('F1 arithmetic: the lattice term and the heavy partners are below the a_e precision by > 1e8; a light second copy is excluded (> 1e5 x)',
      abs(dlat) < 1e-8 * s_meas and hv < 1e-8 * s_meas and vp2 / s_meas > 1e5)
print('theorem-grade: C1 (exact Ward identity of the dressed hop); finite/numerical: A, B, C2, D, E; estimates: F.')
print('supplied: Hamiltonian limit of the tick, flat cell, Gaussian registers, gauge fixing w = 4/3, Stueckelberg photon mass,')
print('  straight-bond external field, one loop, alpha = 3 e^2/4pi from B3; not included: finite step (Floquet), the cone (step) counterterm.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
