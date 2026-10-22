#!/usr/bin/env python3
"""Link dressing of the one-copy 4^3 tick S (s-tick-dressing).

 1  exact algebra of S: W U W = U^-1, U = W eps (overlap algebra, GW relation with W in place of gamma5) for every mu;
    the block pseudoscalar G5 = i W IP; the W-compatible minimal coupling (one site phase per nested 2^3 cube);
 2  validation: second-order Floquet self-energy (particle + hole + seagull + Hartree) against exact many-body
    diagonalisation of a toy; Ward identity; a static transverse field on a 12x4x4 torus against exact diagonalisation;
 3  single static backgrounds: mass part of the four K=0 light levels of S (magnetic and electric);
 4  one loop on n^3 block tori: Coulomb exchange with the sea (Gauss law, frame block charges) and transverse links;
 5  control: the W-glide tick P (protected) gives exactly zero mass part with the same machinery;
 6  the overlap (Ginsparg-Wilson) Hamiltonian built from S's kernel: one copy, W, exact chirality X for every
    magnetostatic background, quasi-local not block-local; electric backgrounds and dynamical links break it;
 7  estimates against the measured electron mass.
Supplied model, finite diagnostic; no physical identification.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/LINK_DRESSING_GIVES_THE_ONE_COPY_BLOCK_TICK_AN_UNPROTECTED_ADDITIVE_MASS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1'); os.environ.setdefault('OMP_NUM_THREADS', '1')
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.alarm(AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from scipy.linalg import expm, schur

T_START = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ============================================================ tick S (rebuilt from onecopy-verify, sections 3 and 8)
def qmul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return np.array([w1*w2 - x1*x2 - y1*y2 - z1*z2, w1*x2 + x1*w2 + y1*z2 - z1*y2, w1*y2 - x1*z2 + y1*w2 + z1*x2, w1*z2 + x1*y2 - y1*x2 + z1*w2])
def qkey(q): return tuple(np.round(q, 8) + 0.0)
def binary_octahedral():
    r2 = np.sqrt(0.5); gens = [np.array([r2, 0, 0, r2]), np.array([0.5, 0.5, 0.5, 0.5])]
    els = {qkey(np.array([1., 0, 0, 0])): np.array([1., 0, 0, 0])}; fr = list(els.values())
    while fr:
        new = []
        for a in fr:
            for g in gens:
                c = qmul(a, g)
                if qkey(c) not in els: els[qkey(c)] = c; new.append(c)
        fr = new
    return list(els.values())
def q_so3(q):
    w, x, y, z = q
    return np.array([[1 - 2*(y*y + z*z), 2*(x*y - z*w), 2*(x*z + y*w)], [2*(x*y + z*w), 1 - 2*(x*x + z*z), 2*(y*z - x*w)], [2*(x*z - y*w), 2*(y*z + x*w), 1 - 2*(x*x + y*y)]])
def q_su2(q): w, x, y, z = q; return np.array([[w - 1j*z, -1j*x - y], [-1j*x + y, w + 1j*z]])
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
CORN = np.array(list(itertools.product((0, 1), repeat=3))); J32 = Jm(1.5); XI = []
for c in CORN:
    n_ = (2 * c - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J32[k] for k in range(3))); XI.append(v_[:, -1])
W8 = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.abs(CORN[a] - CORN[b]).sum() == 1: g = XI[a].conj() @ XI[b]; W8[a, b] = -g / abs(g) / np.sqrt(3)
N = 64; SITES = np.array(list(itertools.product(range(4), repeat=3))); IDX = {tuple(x): i for i, x in enumerate(SITES)}
RES = (SITES % 2) @ [4, 2, 1]; P0 = np.full(3, 1.5); Id = np.eye(N); WA = np.zeros((N, N), complex)
CUBE_OF = np.zeros(N, int); CUBE_ORIG = np.array(list(itertools.product((0, 2), repeat=3)))
for ci, b0 in enumerate(CUBE_ORIG):
    ids = [IDX[tuple(b0 + c)] for c in CORN]; WA[np.ix_(ids, ids)] = W8[np.ix_(RES[ids], RES[ids])]; CUBE_OF[ids] = ci
XC = CUBE_ORIG[CUBE_OF] + 0.5; SC = CUBE_ORIG - 1        # cube centre of each site; s_c (even->odd centre bond = 2 s_c)
LIFT = []
for q in binary_octahedral():
    R = np.round(q_so3(q)); w0, x, y, z = q; ang = 2 * np.arccos(np.clip(w0, -1, 1)); sn = np.sqrt(max(1 - w0 * w0, 0))
    nv = np.array([x, y, z]) / sn if sn > 1e-12 else np.array([0, 0, 1.0])
    LIFT.append((R, q_su2(q), expm(-1j * ang * sum(nv[k] * J32[k] for k in range(3)))))
def site_rot(R, D):
    Gm = np.zeros((N, N), complex)
    for i, x in enumerate(SITES):
        y = np.rint(R @ (x - P0) + P0).astype(int) % 4
        Gm[IDX[tuple(y)], i] = XI[int((y % 2) @ [4, 2, 1])].conj() @ D @ XI[int((x % 2) @ [4, 2, 1])]
    return Gm
GROT = [site_rot(R, D) for R, U, D in LIFT]
T0 = np.zeros((N, N))
for i, x in enumerate(SITES): T0[IDX[tuple((x + 2) % 4)], i] = 1
ORB = {}
for i, x in enumerate(SITES): ORB.setdefault(tuple(np.sort(np.abs(x - P0))), []).append(i)
PERM_I = [IDX[tuple(3 - x)] for x in SITES]; PI_ = np.zeros((N, N)); PI_[PERM_I, np.arange(N)] = 1
def inversion_actions():
    out, base = [], {}
    for kk in ORB:
        r = ORB[kk][0]; d = {r: 1.0 + 0j}; fr = [r]
        while fr:
            nf = []
            for s_ in fr:
                for Gm in GROT:
                    t = int(np.argmax(np.abs(Gm[:, s_]))); val = Gm[PERM_I[t], PERM_I[s_]] * d[s_] / Gm[t, s_]
                    if t not in d: d[t] = val; nf.append(t)
            fr = nf
        v = np.zeros(N, complex)
        for k_, x_ in d.items(): v[k_] = x_
        base[kk] = v / np.sqrt(v[r] * v[PERM_I[r]])
    for sg in itertools.product((1, -1), repeat=len(ORB)):
        I = PI_ @ np.diag(sum(s_ * base[k_] for s_, k_ in zip(sg, ORB)))
        if np.abs(I @ I - Id).max() < 1e-9 and max(np.abs(I @ Gm - Gm @ I).max() for Gm in GROT) < 1e-9: out.append((sg, I))
    return out
IP = [I for sg, I in inversion_actions() if np.abs(I @ WA + WA @ I).max() < 1e-9 and sg[0] == 1][0]
GALL = GROT + [Gm @ IP for Gm in GROT]
e12 = np.array([np.trace(U) for R, U, D in LIFT])
CH = np.concatenate([e12, e12])
P_E12g = 2 / len(GALL) * sum(np.conj(c) * Gm for c, Gm in zip(CH, GALL))
E_EDGE = np.zeros((N, N))
for k_, o in ORB.items():
    if k_ == (0.5, 1.5, 1.5): E_EDGE[o, o] = 1
P_EDGE = E_EDGE @ P_E12g
LAM = (np.array([[v if v >= 2 else v + 4 for v in x] for x in SITES]) - SITES).astype(float)
def bloch_odd(Ao, K): ph = np.exp(-1j * (LAM @ K)); return (ph[:, None] * Ao) * ph.conj()[None, :]
RT = (Id + 1j * T0) / np.sqrt(2); P_CIRC = RT @ P_EDGE @ RT.conj().T; TW = T0 @ WA
def gensS(e=np.pi / 3, fe=np.pi / 2, fo=np.pi / 6, mu=0.0, Pa=P_CIRC):
    Pb = WA @ Pa @ WA; Q = Id - Pa - Pb; B = Pa - Pb
    return (e - mu / 2) * B + fe * IP @ Q, -(e + mu / 2) * B + fo * IP @ Q
def tickS(**kw): He, Ho = gensS(**kw); return expm(-0.5j * He), expm(-1j * Ho)
def basis(P): w, V = np.linalg.eigh((P + P.conj().T) / 2); return V[:, w > 0.5]
Vh, Ao = tickS(); US = lambda K: Vh @ bloch_odd(Ao, K) @ Vh; frS = lambda K: [Vh, bloch_odd(Ao, K) @ Vh]
PaS = P_CIRC; PbS = WA @ PaS @ WA; BS = np.concatenate([basis(PaS), basis(PbS)], 1)     # columns g, g, u, u
G5 = 1j * WA @ IP
rng = np.random.default_rng(20261021)
z3 = np.zeros(3)

# ============================================================ 1. exact algebra
print('== 1. exact algebra of S')
q0 = -np.angle(np.linalg.eigvals(US(z3))); Ks = rng.uniform(-0.7, 0.7, (3, 3))
check('S: 4 light states at Gamma; W U W = U^-1; IP U(K) IP = U(-K)',
      int(np.sum(np.abs(q0) < 1e-9)) == 4 and max(np.abs(WA @ US(K) @ WA - US(K).conj().T).max() for K in Ks) < 1e-12
      and max(np.abs(IP @ US(K) @ IP - US(-K)).max() for K in Ks) < 1e-12)
Vm, Aom = tickS(mu=0.04); Um = lambda K: Vm @ bloch_odd(Aom, K) @ Vm; gw_err = 0
for Uf in (US, Um):
    for K in Ks:
        U = Uf(K); ep = WA @ U; D = Id - U
        gw_err = max(gw_err, np.abs(ep - ep.conj().T).max(), np.abs(ep @ ep - Id).max(), np.abs(WA @ D + D @ WA - D @ WA @ D).max())
check('U = W eps with eps a Hermitian involution, so D = 1 - U obeys W D + D W = D W D, at mu = 0 and mu = 0.04: '
      'the relation holds for every mass and forbids none', gw_err < 1e-12, f'{gw_err:.1e}')
c5 = max(np.abs(G5 @ US(K) - US(K) @ G5).max() for K in Ks)
check('G5 = i W IP: Hermitian involution, commutes with the 48 rotation lifts, anticommutes with IP and W, G5 U(K) G5 = U(-K)^-1;'
      ' it is not a symmetry of S (|[G5, U(K)]| = O(1))',
      np.abs(G5 @ G5 - Id).max() < 1e-12 and max(np.abs(G5 @ g - g @ G5).max() for g in GROT) < 1e-12 and np.abs(G5 @ IP + IP @ G5).max() < 1e-12
      and np.abs(G5 @ WA + WA @ G5).max() < 1e-12 and max(np.abs(G5 @ US(K) @ G5 - US(-K).conj().T).max() for K in Ks) < 1e-12 and c5 > 0.1, f'|[G5,U]| = {c5:.2f}')
chc = np.exp(1j * rng.uniform(-1, 1, 8))[CUBE_OF]; chs = np.exp(1j * rng.uniform(-1, 1, 64))
Uc = lambda K, ph1, ph2: Vh @ (ph2[:, None] * bloch_odd(Ao, K)) @ (ph1[:, None] * Vh)
K = Ks[0]; mag = np.abs(WA @ Uc(K, chc, chc.conj()) @ WA - Uc(K, chc, chc.conj()).conj().T).max()
ele = np.abs(WA @ Uc(K, chc, chc) @ WA - Uc(K, chc.conj(), chc.conj()).conj().T).max()
check('minimal coupling: one phase per nested 2^3 cube (= per bond of the block-centre lattice) commutes with W, a phase per'
      ' site does not; W maps a magnetic configuration to itself and an electric one to its negative (W acts as CT)',
      np.abs(WA * chc - chc[:, None] * WA).max() < 1e-15 and np.abs(WA * chs - chs[:, None] * WA).max() > 0.3 and mag < 1e-12 and ele < 1e-12,
      f'|[W, site phases]| = {np.abs(WA * chs - chs[:, None] * WA).max():.2f}')

# ============================================================ 2. validation of the second-order Floquet formula
print('== 2. validation')
def eig_u(U): T, Z = schur(U, output='complex'); return np.diag(T), Z
def kernel(oo, l0, z_ratio): x = z_ratio * np.exp(-1j * oo); return x ** l0 / (1 - x)
def second_order(Ab, Em, Abp, Emp, zm, seam, zp, seap, zk, om, taus=(0.25, 0.75), sig=(1, -1), hart=None):
    """i * X: second-order quasi-energy shift matrix in the external space for one quantised mode of frequency om.
    Ab/Em: absorption/emission between external and particle sector; Abp/Emp: hole sector."""
    nk = Ab[0].shape[0]; X = np.zeros((nk, nk), complex)
    for i2 in range(2):
        for i1 in range(2):
            l0 = 0 if i1 < i2 else 1; pre = sig[i1] * sig[i2] * np.exp(-1j * om * (taus[i2] - taus[i1]))
            fm = np.where(~seam, kernel(om, l0, zm / zk), 0); fp = np.where(seap, kernel(om, l0, zk / zp), 0)
            X += -pre * (Ab[i2] @ (fm[:, None] * Em[i1]) - Emp[i1] @ (fp[:, None] * Abp[i2]))
            if hart is not None: X += -pre * hart[(i1, i2)] * kernel(om, l0, 1.0)
    for i in range(2):
        X += -0.5 * (Ab[i] @ (np.where(~seam, 1, 0)[:, None] * Em[i]) - Emp[i] @ (np.where(seap, 1, 0)[:, None] * Abp[i]))
        if hart is not None: X += -0.5 * hart[(i, i)]
    return 1j * X
# toy: 4 modes, kicks A, B, C, two cube-phase insertions coupled to one oscillator, sea = levels w < 0
tr = np.random.default_rng(53); M = 4
def herm(n): X = tr.normal(size=(n, n)) + 1j * tr.normal(size=(n, n)); return (X + X.conj().T) / 2
hA, hB, hC = herm(M), herm(M), herm(M); A_, B_, C_ = expm(-1j * hA), expm(-1j * hB), expm(-1j * hC)
w_, V_ = np.linalg.eig(C_ @ B_ @ A_); o_ = np.argsort(-np.angle(w_)); V_, _ = np.linalg.qr(V_[:, o_]); zt = w_[o_]; seat = -np.angle(zt) < 0
cubes = [[0, 1], [2, 3]]; phi_t = np.array([0.7 + 0.2j, -0.4 + 0.5j])
def Pc(c): P = np.zeros((M, M)); P[c, c] = 1; return P
def f_at(i, amp):
    Ui = A_ if i == 0 else B_ @ A_; return V_.conj().T @ Ui.conj().T @ sum(amp[j] * Pc(c) for j, c in enumerate(cubes)) @ Ui @ V_
def toy_formula(k, om):
    Ab = [f_at(i, phi_t) for i in range(2)]; Em = [f_at(i, phi_t.conj()) for i in range(2)]
    P = seat; hart = {(i1, i2): Ab[i2][k, k] * np.trace(Em[i1][np.ix_(P, P)]) + np.trace(Ab[i2][np.ix_(P, P)]) * Em[i1][k, k] for i1 in range(2) for i2 in range(2)}
    return second_order([a[[k], :] for a in Ab], [e[:, [k]] for e in Em], [a[:, [k]] for a in Ab], [e[[k], :] for e in Em],
                        zt, seat, zt, seat, zt[k], om, hart={kk: np.array([[v]]) for kk, v in hart.items()})[0, 0].real
dimF = 2 ** M
def cop(j):
    m = np.zeros((dimF, dimF))
    for s in range(dimF):
        if (s >> j) & 1: m[s ^ (1 << j), s] = (-1) ** bin(s & ((1 << j) - 1)).count('1')
    return m
cs = [cop(j) for j in range(M)]
def sq(h): return sum(h[i, j] * cs[i].T @ cs[j] for i in range(M) for j in range(M))
aop = np.diag(np.sqrt(np.arange(1, 4)), 1); nph = aop.T @ aop
def U_tot(gc, om):
    pe = lambda t: expm(-1j * om * t * nph)
    cpl = lambda i: expm(1j * (1, -1)[i] * sum(np.kron(sq(Pc(c)), gc * phi_t[j] * aop + np.conj(gc * phi_t[j]) * aop.T) for j, c in enumerate(cubes)))
    return np.kron(expm(-1j * sq(hC)), pe(0.25)) @ cpl(1) @ np.kron(expm(-1j * sq(hB)), pe(0.5)) @ cpl(0) @ np.kron(expm(-1j * sq(hA)), pe(0.25))
def mb(occ, gc, om):
    st = np.zeros(dimF, complex); st[0] = 1
    for p in occ: st = sum(V_[j, p] * cs[j].T for j in range(M)) @ st
    psi = np.kron(st, np.eye(4)[0]); l0 = psi.conj() @ U_tot(0.0, om) @ psi; ev, EV = np.linalg.eig(U_tot(gc, om))
    j = np.argmax(np.abs(EV.conj().T @ psi)); return -np.angle(ev[j] / l0)
dev = 0; seaocc = list(np.nonzero(seat)[0]); gc = 5e-4
for om in (0.9, 2.2):
    base = mb(seaocc, gc, om)
    for k in range(M):
        occ = seaocc + [k] if not seat[k] else [x for x in seaocc if x != k]; sgn = 1 if not seat[k] else -1
        ex = sgn * (mb(occ, gc, om) - base) / gc ** 2; fo_ = toy_formula(k, om); dev = max(dev, abs(ex - fo_) / max(abs(fo_), 1e-3))
check('toy (4 modes, 3 kicks, 2 insertions, 1 quantised mode, omega = 0.9 and 2.2): formula = exact many-body shift'
      ' for every added particle and removed hole', dev < 1e-4, f'max rel. dev {dev:.1e}')
def pols(q, nmodes=2):
    ge = -np.exp(-1j * SC @ q); go = np.exp(1j * SC @ q); G, _ = np.linalg.qr(np.stack([ge, go], 1)); PN = np.eye(8) - G @ G.conj().T
    if nmodes == 6: w, V = np.linalg.eigh(PN); return V[:, w > 0.5]
    qh = q / np.linalg.norm(q); e1 = np.cross(qh, [0.3, 0.5, 0.8]); e1 /= np.linalg.norm(e1); e2 = np.cross(qh, e1)
    Lf = np.stack([(SC @ e) * np.sinc((SC @ q) / np.pi) for e in (e1, e2)], 1); Uq, _ = np.linalg.qr(PN @ Lf); return Uq
def mode_matrix(Uf, frames, Bext, q, phi8, om, zk=1.0, sectors=None):
    zm, Zm = eig_u(Uf(-q)) if sectors is None else sectors[0]; zp, Zp = eig_u(Uf(q)) if sectors is None else sectors[1]
    seam = -np.angle(zm) < 0; seap = -np.angle(zp) < 0; F0 = frames(z3); Fm = frames(-q); Fp = frames(q)
    dab = phi8[CUBE_OF] * np.exp(1j * XC @ q); dem = np.conj(dab)
    Em = [Zm.conj().T @ Fm[i].conj().T @ (dem[:, None] * (F0[i] @ Bext)) for i in range(2)]
    Ab = [Bext.conj().T @ F0[i].conj().T @ (dab[:, None] * (Fm[i] @ Zm)) for i in range(2)]
    Abp = [Zp.conj().T @ Fp[i].conj().T @ (dab[:, None] * (F0[i] @ Bext)) for i in range(2)]
    Emp = [Bext.conj().T @ F0[i].conj().T @ (dem[:, None] * (Fp[i] @ Zp)) for i in range(2)]
    return second_order(Ab, Em, Abp, Emp, zm, seam, zp, seap, zk, om)
ward = 0
for q in (np.array([0.3, -0.1, 0.2]), np.array([np.pi / 6, 0, 0])):
    for g in (np.exp(1j * SC @ q), -np.exp(-1j * SC @ q)):
        ph = 0.1 * g / np.linalg.norm(g); ward = max(ward, np.abs(mode_matrix(US, frS, BS, q, ph, 0.0) + mode_matrix(US, frS, BS, -q, ph.conj(), 0.0)).max())
check('Ward identity: a static pure-gauge configuration (odd- or even-block phases) gives zero second-order shift', ward < 1e-15, f'{ward:.1e}')
LL = np.array([12, 4, 4]); SR = np.array(list(itertools.product(range(12), range(4), range(4)))); IR = {tuple(x): i for i, x in enumerate(SR)}; NR = len(SR)
def layer(B64, off):
    Mx = np.zeros((NR, NR), complex)
    for o in ((0, 0, 0), (4, 0, 0), (8, 0, 0)):
        org = np.array(o) + off; ids = [IR[tuple((x + org) % LL)] for x in SITES]; cs_ = [IDX[tuple((x + org) % 4)] for x in SITES]
        Mx[np.ix_(ids, ids)] += B64[np.ix_(cs_, cs_)]
    return Mx
qx = np.array([np.pi / 6, 0, 0]); ux = pols(qx)[:, 0]
ccR = ((SR % 4) // 2) @ [4, 2, 1]; xR = (SR // 4) * 4 + (SR % 4 // 2) * 2 + 0.5
def chi_static(eps): return 2 * np.real(eps * ux[ccR] * np.exp(1j * (xR @ qx)))
evid = SR[:, 0] // 4
def phi_static(eps): return eps * np.cos(2 * np.pi * evid / 3 + 0.4)
def k0vec(v64):
    out = np.zeros(NR, complex)
    for o in ((0, 0, 0), (4, 0, 0), (8, 0, 0)): out[[IR[tuple((x + np.array(o)) % LL)] for x in SITES]] = v64
    return out / np.sqrt(3)
def mass_part(evals, evecs, Bk):
    C = Bk.conj().T @ evecs; H = C @ np.diag(evals) @ np.linalg.pinv(C); H = (H + H.conj().T) / 2
    return np.trace(np.diag([1, 1, -1, -1.0]) @ H).real / 4
VeR, AoR = layer(Vh @ Vh, 0), layer(Ao, 2); BkS = np.stack([k0vec(Vh.conj().T @ BS[:, j]) for j in range(4)], 1)
eps = 0.005; chi = chi_static(eps); wq = -np.angle(np.linalg.eigvals((np.exp(-1j * chi)[:, None] * AoR * np.exp(1j * chi)[None, :]) @ VeR))
lev = np.sort(wq[np.abs(wq) < 0.05]) / eps ** 2; Mst = mode_matrix(US, frS, BS, qx, eps * ux, 0.0) + mode_matrix(US, frS, BS, -qx, eps * ux.conj(), 0.0)
fev = np.sort(np.linalg.eigvals(Mst).real) / eps ** 2
check('static transverse field on a 12x4x4 torus: exact light-level shifts (pair means) = formula at omega = 0',
      len(lev) == 4 and abs((lev[2] + lev[3]) / 2 - fev[3]) < 1e-4 * abs(fev[3]) and abs((lev[0] + lev[1]) / 2 - fev[0]) < 1e-4 * abs(fev[0]),
      f'exact {np.round(lev, 4).tolist()}, formula +-{fev[3]:.5f} (units eps^2)')

# ============================================================ 3. single static backgrounds, S
print('== 3. S in single static backgrounds (exact diagonalisation, 12x4x4 torus): mass part tr(beta H_eff)/4')
res = {}
for kind in ('magnetic', 'electric'):
    vals = []
    for eps in (0.02, 0.01):
        if kind == 'magnetic': chi = chi_static(eps); Ug = (np.exp(-1j * chi)[:, None] * AoR * np.exp(1j * chi)[None, :]) @ VeR
        else: Ug = AoR @ (np.exp(-0.5j * phi_static(eps))[:, None] * VeR)
        w, V = np.linalg.eig(Ug); qe = -np.angle(w); sel = np.abs(qe) < 0.05; vals.append(mass_part(qe[sel], V[:, sel], BkS) / eps ** 2)
    res[kind] = vals
check('S is unprotected even by static backgrounds: magnetic and electric configurations both move the mass part at O(eps^2)',
      min(abs(res['magnetic'][1]), abs(res['electric'][1])) > 0.05 and abs(res['magnetic'][0] - res['magnetic'][1]) < 1e-3,
      f"magnetic {res['magnetic'][1]:+.4f}, electric {res['electric'][1]:+.4f} (units eps^2)")

# ============================================================ 4. one loop on n^3 block tori
print('== 4. one loop, units e^2 = 4 pi alpha, quasi-energy per tick (shift of the u doublet = the +mu level)')
def qgrid(n):
    k = 2 * np.pi * np.arange(n) / (4 * n); k = (k + np.pi / 4) % (np.pi / 2) - np.pi / 4; return np.array(list(itertools.product(k, k, k)))
def Gt(q): c = np.prod(np.cos(2 * q)); return 1.0 / (8 * (1 - c * c))      # even-even Green function of the block-centre Laplacian
def coulomb(Uf, frames, Bext, n, Vfirst):
    C = np.zeros((2, 2)); G0 = 0; Qg = qgrid(n)
    for q in Qg:
        if np.linalg.norm(q) < 1e-12: continue
        Uq = Uf(q); a, V = np.linalg.eigh((Uq - Uq.conj().T) / 2j); sea = V[:, a > 0]; g = Gt(q); G0 += g; ph = np.exp(-1j * (LAM @ q))
        for j, sl in enumerate((slice(0, 2), slice(2, 4))):
            Bk = Bext[:, sl]
            C[0, j] += g * np.mean(np.sum(np.abs(sea.conj().T @ Bk) ** 2, 0))
            C[1, j] += g * np.mean(np.sum(np.abs((Vfirst @ sea).conj().T @ (ph[:, None] * (Vfirst @ Bk))) ** 2, 0))
    return G0 / len(Qg) / 2 - C / len(Qg)          # rows: even frame, odd frame; columns g, u
def transverse(Uf, frames, Bext, n, omf, nmodes=2):
    Qg = qgrid(n); M4 = np.zeros((4, 4), complex)
    for q in Qg:
        if np.linalg.norm(q) < 1e-12: continue
        sec = (eig_u(Uf(-q)), eig_u(Uf(q))); om = omf(q); P8 = pols(q, nmodes)
        for pol in range(P8.shape[1]): M4 += mode_matrix(Uf, frames, Bext, q, np.sqrt(1 / (2 * om * len(Qg))) * P8[:, pol], om, sectors=sec)
    return M4
# real-space cross-check on the 8^3 torus (n = 2): frame block projectors, sea of the full 512-site tick
S8_ = np.array(list(itertools.product(range(8), repeat=3))); I8_ = {tuple(x): i for i, x in enumerate(S8_)}
def lay8_(B64, off):
    Mx = np.zeros((512, 512), complex)
    for o in itertools.product((0, 4), repeat=3):
        org = np.array(o) + off; ids = [I8_[tuple((x + org) % 8)] for x in SITES]; cs_ = [IDX[tuple((x + org) % 4)] for x in SITES]
        Mx[np.ix_(ids, ids)] += B64[np.ix_(cs_, cs_)]
    return Mx
VhR8 = lay8_(Vh, 0); U8 = VhR8 @ lay8_(Ao, 2) @ VhR8; a8_, V8_ = np.linalg.eigh((U8 - U8.conj().T) / 2j); P8s = V8_[:, a8_ > 1e-9] @ V8_[:, a8_ > 1e-9].conj().T
blk_e = (S8_ // 4) @ [4, 2, 1]; blk_o = (((S8_ - 2) % 8) // 4) @ [4, 2, 1]; Rb = np.array(list(itertools.product((0, 4), repeat=3)), float)
qs8 = [np.array(m) * np.pi / 4 for m in itertools.product(range(2), repeat=3) if any(m)]
G8 = np.array([[sum(Gt(q) * np.cos(q @ (Rb[i] - Rb[j])) for q in qs8) / 8 for j in range(8)] for i in range(8)])
def k0_8(v64):
    out = np.zeros(512, complex)
    for o in itertools.product((0, 4), repeat=3): out[[I8_[tuple((x + np.array(o)) % 8)] for x in SITES]] = v64
    return out / np.sqrt(8)
def S_rs(v, Pm, blk):
    w = [Pm @ (v * (blk == b)) for b in range(8)]
    return sum(G8[b, bp] * np.real(np.vdot(v * (blk == bp), w[b])) for b in range(8) for bp in range(8))
rs = [np.mean([G8[0, 0] / 2 - (S_rs(k0_8(BS[:, c]), P8s, blk_e) + S_rs(VhR8 @ k0_8(BS[:, c]), VhR8 @ P8s @ VhR8.conj().T, blk_o)) / 2 for c in cols]) for cols in ((0, 1), (2, 3))]
c2 = coulomb(US, frS, BS, 2, Vh).mean(0)
check('Coulomb exchange: real-space 8^3 computation (block projectors, full sea) = momentum sum at n = 2',
      abs(rs[0] - c2[0]) < 1e-12 and abs(rs[1] - c2[1]) < 1e-12, f'eps_g {rs[0]:+.6f} vs {c2[0]:+.6f}')
cS = {}
for n in (8, 12, 16):
    e_ = coulomb(US, frS, BS, n, Vh); cS[n] = e_.mean(0)
w_ok = all(abs(cS[n][0] + cS[n][1]) < 1e-12 for n in cS)
cinf = (16 ** 2 * cS[16][1] - 12 ** 2 * cS[12][1]) / (16 ** 2 - 12 ** 2)
check('Coulomb exchange with the sea (frame block charges, Gauss law): eps_g = -eps_u (W) and nonzero; n = 8, 12, 16',
      w_ok and abs(cinf) > 0.01, f'eps_u = {cS[8][1]:+.6f}, {cS[12][1]:+.6f}, {cS[16][1]:+.6f} -> {cinf:+.5f} (1/n^2)')
def om_band(q): w = -np.angle(np.linalg.eigvals(US(q))); return np.min(w[w > 0])
om_lin = lambda q: 2.0 * np.linalg.norm(q)
tS = {}
for n in (8, 10, 12):
    Mt = transverse(US, frS, BS, n, om_band); tS[n] = (np.trace(Mt[:2, :2]) / 2, np.trace(Mt[2:, 2:]) / 2, np.abs(Mt[:2, 2:]).max())
tinf = (12 ** 2 * tS[12][1].real - 10 ** 2 * tS[10][1].real) / (12 ** 2 - 10 ** 2)
check('transverse links (2 polarisations, photon band = lowest positive band of S, extras frozen): delta_g = -delta_u, no g-u mixing, real',
      all(abs(tS[n][0] + tS[n][1]) < 1e-12 and tS[n][2] < 1e-12 and abs(tS[n][1].imag) < 1e-12 for n in tS) and abs(tinf) > 0.05,
      f'delta_u = {tS[8][1].real:+.5f}, {tS[10][1].real:+.5f}, {tS[12][1].real:+.5f} -> {tinf:+.4f}')
tl = transverse(US, frS, BS, 10, om_lin); t6 = transverse(US, frS, BS, 6, om_band, nmodes=6)
tl_u, t6_u = np.trace(tl[2:, 2:]).real / 2, np.trace(t6[2:, 2:]).real / 2
check('photon-law variants keep the sign: linear dispersion v|q| (n=10); all six non-gauge cube modes dynamical (n=6)',
      tl_u < -0.02 and t6_u < tinf, f'{tl_u:+.4f}, {t6_u:+.4f}')
scan = []
for s_ in (np.pi / 2, np.pi / 3, np.pi / 6):
    vh_, ao_ = tickS(fo=s_ - np.pi / 2); uf = lambda K: vh_ @ bloch_odd(ao_, K) @ vh_
    scan.append(coulomb(uf, None, BS, 6, vh_).mean(0)[1])
check('heavy-phase scan fe + fo = pi/2, pi/3, pi/6 (n = 6): the Coulomb shift stays nonzero at each tested gapped choice',
      min(abs(x) for x in scan) > 0.01, ', '.join(f'{x:+.4f}' for x in scan))
dm_lo, dm_cl5, dm_hi = cinf + tl_u, cinf + tinf, cinf + t6_u
a_ = 1 / 137.036; e2 = 4 * np.pi * a_
print(f'   delta m (u level) = Coulomb {cinf:+.4f} + transverse {tinf:+.4f} = {dm_cl5:+.4f} e^2 = {dm_cl5 * 4 * np.pi:+.2f} alpha per tick'
      f'  [law range {dm_lo * 4 * np.pi:+.2f} .. {dm_hi * 4 * np.pi:+.2f} alpha]')

# ============================================================ 5. glide control
print('== 5. control: W-glide tick P (odd half-tick = (2,2,2)-translate of W V W), same machinery')
VeP = np.exp(-1j * 7 * np.pi / 12) * P_EDGE + np.exp(1j * 7 * np.pi / 12) * (TW @ P_EDGE @ TW.conj().T) + np.exp(-1j * np.pi / 12) * (Id - P_EDGE - TW @ P_EDGE @ TW.conj().T)
AoP = TW @ VeP @ TW.conj().T; UP = lambda K: bloch_odd(AoP, K) @ VeP; frP = lambda K: [VeP, bloch_odd(AoP, K) @ VeP]
BP = np.concatenate([basis(P_EDGE), basis(TW @ P_EDGE @ TW.conj().T)], 1)
cP = coulomb(UP, frP, BP, 6, VeP).mean(0); tP = transverse(UP, frP, BP, 4, lambda q: 2.23 * np.linalg.norm(q))
mP = abs((np.trace(tP[2:, 2:]) - np.trace(tP[:2, :2])) / 4)
check('P: Coulomb and transverse mass parts vanish identically; only the common (non-mass) shift is nonzero',
      abs(cP[1] - cP[0]) < 1e-13 and mP < 1e-13 and abs(np.trace(tP).real) > 1e-3, f'mass parts {abs(cP[1] - cP[0]):.0e}, {mP:.0e}; common {np.trace(tP).real / 4:+.4f}')

# ============================================================ 6. overlap Hamiltonian from S's kernel
print('== 6. overlap tick: H_GW = IP - i W sign(i W H_S), kernel H_S = H_e + H_o(K) with light Wilson mass -0.6')
He0, Ho0 = gensS(mu=0.6)
def HSk(K): return He0 + bloch_odd(Ho0, K)
def gwK(K):
    a, V = np.linalg.eigh(1j * WA @ HSk(K)); ep = (V * np.sign(a)) @ V.conj().T; H = IP - 1j * WA @ ep; E, Z = np.linalg.eigh(H); return a, V, ep, H, E, Z
errs = 0
for K in Ks:
    a, V, ep, H, E, Z = gwK(K); D = Id + G5 @ ep; X = (G5 - ep) / 2
    errs = max(errs, np.abs(H - H.conj().T).max(), np.abs(WA @ H @ WA + H).max(), np.abs(G5 @ D + D @ G5 - D @ G5 @ D).max(), np.abs(X @ H - H @ X).max())
E0 = gwK(z3)[4]; gq = (np.arange(12) - 6) * (np.pi / 2) / 12; offmin, kgap = 9, 9
for K in itertools.product(gq, gq, gq):
    K = np.array(K); a, V, ep, H, E, Z = gwK(K); kgap = min(kgap, np.abs(a).min())
    if np.linalg.norm(K) > 1e-9: offmin = min(offmin, np.abs(E).min() / np.linalg.norm(K))
check('H_GW: Hermitian, W-odd, GW relation exact, chirality X = (G5 - sign)/2 commutes with H_GW; Gamma: 4 light at 0, 60 at +-2;'
      ' kernel gapped and no light state off Gamma on a 12^3 grid', errs < 1e-12 and np.sum(np.abs(E0) < 1e-9) == 4 and np.sum(np.abs(np.abs(E0) - 2) < 1e-9) == 60
      and kgap > 0.1 and offmin > 1.0, f'kernel gap {kgap:.3f}, min |E|/|K| off Gamma {offmin:.2f}')
nF = 12; gF = 2 * np.pi * np.arange(nF) / (4 * nF); RS = [(1, 0, 0), (2, 0, 0), (4, 0, 0), (6, 0, 0)]
acc = {R: np.zeros((N, N), complex) for R in RS}; accU = {R: np.zeros((N, N), complex) for R in RS}; tauGW = 2.0 / 5.185
for m in itertools.product(range(nF), repeat=3):
    K = gF[list(m)]; a, V, ep, H, E, Z = gwK(K); UGW = (Z * np.exp(-1j * tauGW * E)) @ Z.conj().T
    for R in RS: ph = np.exp(-1j * 4 * np.dot(K, R)); acc[R] += ph * H; accU[R] += ph * UGW
nr = {R: np.linalg.norm(acc[R] / nF ** 3, 2) for R in RS}; nu = {R: np.linalg.norm(accU[R] / nF ** 3, 2) for R in RS}
check('H_GW and its tick exp(-i tau H_GW) (tau: speed of S) are quasi-local, not block-local: block amplitudes at 1, 2, 4, 6'
      ' blocks never vanish (a Margolus tick stops at 1)', min(nr[(6, 0, 0)], nu[(6, 0, 0)]) > 1e-7 and nr[(6, 0, 0)] < nr[(2, 0, 0)],
      'H ' + ', '.join(f'{nr[R]:.1e}' for R in RS) + '; U ' + ', '.join(f'{nu[R]:.1e}' for R in RS))
L8 = 8; S8 = np.array(list(itertools.product(range(L8), repeat=3))); I8 = {tuple(x): i for i, x in enumerate(S8)}; N8 = 512
def lay8(B64, off):
    Mx = np.zeros((N8, N8), complex)
    for o in itertools.product((0, 4), repeat=3):
        org = np.array(o) + off; ids = [I8[tuple((x + org) % L8)] for x in SITES]; cs_ = [IDX[tuple((x + org) % 4)] for x in SITES]
        Mx[np.ix_(ids, ids)] += B64[np.ix_(cs_, cs_)]
    return Mx
He8, Ho8, W8R, IP8 = lay8(He0, 0), lay8(Ho0, 2), lay8(WA, 0), lay8(IP, 0); cid8 = (S8 // 2) @ [16, 4, 1]; G58 = 1j * W8R @ IP8
chi8 = rng.uniform(-np.pi, np.pi, 64)[cid8]; H8 = He8 + np.exp(-1j * chi8)[:, None] * Ho8 * np.exp(1j * chi8)[None, :]
a8, V8 = np.linalg.eigh(1j * W8R @ H8); ep8 = (V8 * np.sign(a8)) @ V8.conj().T; Hg8 = IP8 - 1j * W8R @ ep8; X8 = (G58 - ep8) / 2
Pblk = np.diag(np.all(S8 < 4, axis=1).astype(float))
check('8^3 torus, random magnetostatic cube phases: [X, H_GW] = 0 exactly, but X does not commute with a block charge',
      np.abs(X8 @ Hg8 - Hg8 @ X8).max() < 1e-12 and np.linalg.norm(X8 @ Pblk - Pblk @ X8, 2) > 0.1, f'|[X, Pi_block]| = {np.linalg.norm(X8 @ Pblk - Pblk @ X8, 2):.3f}')
HeR, HoR, WRr, IPRr = layer(He0, 0), layer(Ho0, 2), layer(WA, 0), layer(IP, 0)
def HGWR(chi=None, phi=None):
    Ho_ = HoR if chi is None else np.exp(-1j * chi)[:, None] * HoR * np.exp(1j * chi)[None, :]
    a, V = np.linalg.eigh(1j * WRr @ (HeR + Ho_)); Hg = IPRr - 1j * WRr @ ((V * np.sign(a)) @ V.conj().T)
    return Hg if phi is None else Hg + np.diag(phi)
E0R, Z0R = np.linalg.eigh(HGWR()); Bl = Z0R[:, np.abs(E0R) < 1e-8]; ipl = Bl.conj().T @ IPRr @ Bl; wi, Ui = np.linalg.eigh((ipl + ipl.conj().T) / 2); Bl = Bl @ Ui[:, ::-1]
gwm = {}
for kind in ('magnetic', 'electric'):
    eps = 0.01; Hg = HGWR(chi=chi_static(eps)) if kind == 'magnetic' else HGWR(phi=phi_static(eps))
    E, Z = np.linalg.eigh(Hg); sel = np.abs(E) < 0.05; gwm[kind] = mass_part(E[sel], Z[:, sel], Bl) / eps ** 2
check('overlap tick in single static backgrounds: the magnetic mass part vanishes, the electric one does not',
      abs(gwm['magnetic']) < 1e-6 and abs(gwm['electric']) > 0.05, f"magnetic {gwm['magnetic']:+.1e}, electric {gwm['electric']:+.4f} (eps^2)")
E0, Z0 = gwK(z3)[4:]; Bg = Z0[:, np.abs(E0) < 1e-8]; ipl = Bg.conj().T @ IP @ Bg; wi, Ui = np.linalg.eigh((ipl + ipl.conj().T) / 2); BG = Bg @ Ui[:, ::-1]   # g, g, u, u
Cg = np.zeros(2); G0 = 0
for q in qgrid(8):
    if np.linalg.norm(q) < 1e-12: continue
    E, Z = gwK(q)[4:]; sea = Z[:, E < 0]; g = Gt(q); G0 += g
    for j, sl in enumerate((slice(0, 2), slice(2, 4))): Cg[j] += g * np.mean(np.sum(np.abs(sea.conj().T @ BG[:, sl]) ** 2, 0))
cGW = G0 / 512 / 2 - Cg / 512
cache = {}
def gwc(K):
    key = tuple(np.round(K, 12))
    if key not in cache: cache[key] = gwK(K)
    return cache[key]
def V1(K2, K1, d):
    dA = 1j * WA @ (-1j * (d[:, None] * bloch_odd(Ho0, K1) - bloch_odd(Ho0, K2) * d[None, :]))
    a2, V2 = gwc(K2)[:2]; a1, Vv1 = gwc(K1)[:2]; s2, s1 = np.sign(a2), np.sign(a1)
    num = s2[:, None] - s1[None, :]; den = a2[:, None] - a1[None, :]; F = np.divide(num, den, out=np.zeros_like(den), where=np.abs(num) > 0.5)
    return -1j * WA @ (V2 @ ((V2.conj().T @ dA @ Vv1) * F) @ Vv1.conj().T)
Dl = np.zeros((4, 4), complex); nT = 6; Qg = qgrid(nT)
for q in Qg:
    if np.linalg.norm(q) < 1e-12: continue
    Em_, Zm = gwc(-q)[4:]; Ep_, Zp = gwc(q)[4:]; om = np.min(Ep_[Ep_ > 1e-9]); P8 = pols(q)
    for pol in range(2):
        d = np.sqrt(1 / (2 * om * len(Qg))) * P8[CUBE_OF, pol] * np.exp(1j * XC @ q)
        Emv = Zm.conj().T @ V1(-q, z3, np.conj(d)) @ BG; Abv = BG.conj().T @ V1(z3, -q, d) @ Zm
        Abp = Zp.conj().T @ V1(q, z3, d) @ BG; Emp = BG.conj().T @ V1(z3, q, np.conj(d)) @ Zp
        for sgn, oo in ((1, om), (-1, 0.0)):
            fm = np.divide(1.0, -Em_ - oo, out=np.zeros_like(Em_), where=Em_ > 0); fp = np.divide(1.0, Ep_ - oo, out=np.zeros_like(Ep_), where=Ep_ < 0)
            Dl += sgn * (Abv @ (fm[:, None] * Emv) - Emp @ (fp[:, None] * Abp))
dGW = (np.trace(Dl[:2, :2]) - np.trace(Dl[2:, 2:])).real / 4
check('overlap tick dressed at one loop: Coulomb exchange (n=8) and dynamical transverse links (n=6, static part removed:'
      ' it vanishes by the exact chirality) both give a mass', abs(cGW[0] + cGW[1]) < 1e-12 and abs(cGW[0]) > 0.02 and abs(dGW) > 0.005,
      f'Coulomb eps_g {cGW[0]:+.4f}, dynamical {dGW:+.4f} (e^2, H_GW units; x c_GW/c_S = 2.59 for alpha)')

# ============================================================ 7. estimates
print('== 7. estimates (supplied: site spacing a = 5 l_P, light speed 2 sites per tick -> tick = 10 t_P)')
me_tick = 0.51099895e-3 / 1.220890e19 * 10
print(f'   electron rest level per tick m_e c^2 tau / hbar = {me_tick:.2e};  |delta m| = {abs(dm_cl5) * e2:.2e} per tick'
      f' (range {abs(dm_lo) * e2:.1e} .. {abs(dm_hi) * e2:.1e}): bare mu must cancel it to 1 part in {abs(dm_cl5) * e2 / me_tick:.0e}')
print(f'   runtime {time.time() - T_START:.1f} s')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
