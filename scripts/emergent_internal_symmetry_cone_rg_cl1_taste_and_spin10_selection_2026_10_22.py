AUDIT_INPUT_PATHS = ('docs/EMERGENT_INTERNAL_SYMMETRY_PROTECTS_NOTHING_THE_LATTICE_GROUP_DOES_NOT_GAUGE_FLOW_KILLS_8_OF_11_CONE_COUPLINGS_ONLY_LOGARITHMICALLY_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Emergent internal symmetry from a qubit lattice: what flows to zero, what is protected, what is accidental.

P: one-loop RG of the 13 cubic-covariant cone couplings on (E+T1) x spin (the half-link 5) under a flavour-blind
   U(1) gauge field: 10 irrelevant (rate -8/3 alpha/2pi), 3 exactly marginal = redundant spin-flavour frame
   rotations that reappear as relevant on-site terms.
C: CL-1 cube tick (flat edges, mu = 0): light content, exact lattice group, robust (dim <= 4) emergent commutant.
S: emergent Spin(10)/SU(5) on 16 free Weyl modes: Burnside, maximal-subgroup selection table.
Supplied model, finite diagnostic, no physical identification. Seeded, self-contained.
"""
import itertools, signal, sys, time
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (print("TIMEOUT"), sys.exit(1)))
signal.alarm(AUDIT_TIMEOUT_SEC - 5)
rng = np.random.default_rng(20261022)
T0 = time.time()
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))


I2 = np.eye(2)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1.]).astype(complex)]


def herm_basis(n):
    out = [np.diag(np.eye(n)[i]).astype(complex) for i in range(n)]
    for i, j in itertools.combinations(range(n), 2):
        E = np.zeros((n, n), complex); E[i, j] = E[j, i] = 1; out.append(E)
        E = np.zeros((n, n), complex); E[i, j] = -1j; E[j, i] = 1j; out.append(E)
    return out


def nullspace_real(M, tol=1e-9):
    w, V = np.linalg.eigh(M.T @ M)
    return V[:, w < tol].T


def cdim_commutant(mats, n):
    gl = [np.eye(n)[:, [i]] @ np.eye(n)[[j], :] for i in range(n) for j in range(n)]
    Mx = np.array([np.concatenate([(b @ M - M @ b).ravel() for M in mats]) for b in gl]).T
    s = np.linalg.svd(Mx, compute_uv=False)
    return int(np.sum(s < 1e-7 * s[0])) + max(0, n * n - len(s))


def signed_perms(d, det=None):
    out = []
    for p in itertools.permutations(range(d)):
        for s in itertools.product([1, -1], repeat=d):
            M = np.zeros((d, d))
            for i in range(d):
                M[p[i], i] = s[i]
            if det is None or round(np.linalg.det(M)) == det:
                out.append(M)
    return out


def lift(R):
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if th < 1e-9:
        return np.eye(2, dtype=complex)
    n = np.linalg.eigh(R)[1][:, -1] if abs(th - np.pi) < 1e-9 else \
        np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(th))
    return np.cos(th / 2) * I2 - 1j * np.sin(th / 2) * sum(n[i] * SIG[i] for i in range(3))


# =============================================================== P
print("== P. RG of the 13 covariant cone couplings on the half-link 5 (E+T1) x spin ==")
O24 = signed_perms(3, det=1)
dirs = [s * np.eye(3)[m] for m in range(3) for s in (1, -1)]
def P6(R):
    M = np.zeros((6, 6))
    for i, v in enumerate(dirs):
        M[[k for k, w in enumerate(dirs) if np.allclose(w, R @ v)][0], i] = 1
    return M
odd = [(np.eye(6)[2 * m] - np.eye(6)[2 * m + 1]) / np.sqrt(2) for m in range(3)]
ev = np.array([(np.eye(6)[2 * m] + np.eye(6)[2 * m + 1]) / np.sqrt(2) for m in range(3)])
Qa, _ = np.linalg.qr(np.column_stack([ev.sum(0) / np.sqrt(3), ev[0], ev[1]]))
B5 = np.column_stack([Qa[:, 1], Qa[:, 2]] + odd)
D10 = [np.kron(B5.T @ P6(R) @ B5, lift(R)) for R in O24]
GEN = [i for i, R in enumerate(O24) if np.allclose(R, [[0, -1, 0], [1, 0, 0], [0, 0, 1]]) or np.allclose(R, [[0, 0, 1], [1, 0, 0], [0, 1, 0]])]
h10 = herm_basis(10)
nrm = np.array([np.real(np.trace(b.conj().T @ b)) for b in h10])
def coords(Ms):
    return np.concatenate([[np.real(np.trace(b.conj().T @ M)) for b in h10] for M in Ms]) / np.tile(nrm, 3)
def build(v):
    return [sum(v[100 * m + b] * h10[b] for b in range(100)) for m in range(3)]
rows = []
for bi in range(300):
    m0, b = divmod(bi, 100); Ms = [np.zeros((10, 10), complex) for _ in range(3)]; Ms[m0] = h10[b]
    r = []
    for gi in GEN:
        D, R = D10[gi], O24[gi]
        r += [(D @ Ms[m] @ D.conj().T - sum(R[n, m] * Ms[n] for n in range(3))).ravel() for m in range(3)]
    rows.append(np.concatenate(r))
Mx = np.array(rows).T; NB = nullspace_real(np.vstack([Mx.real, Mx.imag]))
PE = np.diag([1, 1, 0, 0, 0.]); PT = np.diag([0, 0, 1, 1, 1.])
blind = [NB @ coords([np.kron(P, SIG[m]) for m in range(3)]) for P in (PE, PT)]
check("P1 cubic-covariant k-linear cone couplings on (E+T1) x spin: 13; colour/weak-blind 2 inside; 11 breaking",
      len(NB) == 13 and all(abs(np.linalg.norm(b) - np.sqrt(np.sum(coords([np.kron(P, SIG[m]) for m in range(3)]) ** 2))) < 1e-9
                            for b, P in zip(blind, (PE, PT))), f"dim {len(NB)}")

# S^3 quadrature for the log-divergent one-loop self-energy (Euclidean, Feynman-type gauge xi)
xc, wc = np.polynomial.legendre.leggauss(12); chi = (xc + 1) * np.pi / 2; wchi = wc * np.sin(chi) ** 2
xt, wt = np.polynomial.legendre.leggauss(12); ph = np.arange(24) * 2 * np.pi / 24
pts, wts = [], []
for c, a in zip(chi, wchi):
    for ct, b in zip(xt, wt):
        st = np.sqrt(1 - ct ** 2)
        for p_ in ph:
            pts.append([np.cos(c), np.sin(c) * st * np.cos(p_), np.sin(c) * st * np.sin(p_), np.sin(c) * ct]); wts.append(a * b)
pts = np.array(pts); wts = np.array(wts) / np.sum(wts)


def beta(V, xi=1.0):
    """dV_b/dl in units of alpha/2pi (l = ln Lambda/mu), photon cone fixed at 1, unit flavour-blind charge."""
    n = V[0].shape[0]; I = np.eye(n)
    K = -1j * pts[:, 0, None, None] * I + np.einsum('pb,bij->pij', pts[:, 1:], np.array(V))
    G = np.linalg.inv(K); Gam = [-1j * I] + list(V)
    Gq = np.einsum('pm,mij->pij', pts, np.array(Gam))
    A = []
    for Kmu in Gam:
        GKG = G @ Kmu @ G
        acc = sum(np.einsum('p,pij->ij', wts, Gam[mu] @ GKG @ Gam[mu]) for mu in range(4))
        acc = acc - (1 - xi) * np.einsum('p,pij->ij', wts, Gq @ GKG @ Gq)
        A.append(acc)
    iA0 = 1j * A[0]
    return [A[b + 1] - 0.5 * (iA0 @ V[b] + V[b] @ iA0) for b in range(3)]


rates = {}
for xi in (0.0, 1.0, 3.0):
    rates[xi] = [np.real(np.trace(beta([c * s for s in SIG], xi)[0] @ SIG[0])) / 2 for c in (0.6, 1.0, 1.4)]
okP2 = all(np.allclose(rates[x], rates[1.0], atol=1e-9) for x in rates) and rates[1.0][0] > 0 and abs(rates[1.0][1]) < 1e-9 and rates[1.0][2] < 0
check("P2 sanity: one Weyl with speed c flows to the photon cone c=1 (Nielsen-Chadha), gauge-independent (xi=0,1,3)",
      okP2, "dc/dl[c=.6,1,1.4] = " + ', '.join(f"{r:+.3f}" for r in rates[1.0]))

Vs = [np.kron(np.eye(5), SIG[m]) for m in range(3)]
def Bc(d):
    return NB @ coords(beta([Vs[m] + build(NB.T @ d)[m] for m in range(3)]))
h = 1e-4
J = np.column_stack([(Bc(h * e) - Bc(-h * e)) / (2 * h) for e in np.eye(13)])
wJ = np.sort(np.linalg.eigvals(J).real)
check("P3 linearised flow at the blind cone: eigenvalues -8/3 (x10, irrelevant) and 0 (x3); none relevant",
      np.allclose(wJ[:10], -8 / 3, atol=1e-5) and np.allclose(wJ[10:], 0, atol=1e-6) and np.max(np.abs(Bc(np.zeros(13)))) < 1e-10,
      f"eig {np.round(wJ[0], 5)} x{np.sum(np.abs(wJ + 8/3) < 1e-5)}, 0 x{np.sum(np.abs(wJ) < 1e-6)}")
check("P3b the 2 blind couplings (c_E, c_T) are in the -8/3 space: both speeds flow to the photon cone",
      all(np.linalg.norm(J @ b + 8 / 3 * b) < 1e-6 * np.linalg.norm(b) for b in blind))
Mx = np.array([np.concatenate([(D @ b @ D.conj().T - b).ravel() for D in D10]) for b in h10]).T
Sinv = [sum(c * b for c, b in zip(v, h10)) for v in nullspace_real(np.vstack([Mx.real, Mx.imag]))]
red = np.array([NB @ coords([1j * (S @ V - V @ S) for V in Vs]) for S in Sinv])
rk = np.linalg.matrix_rank(red, 1e-8)
_, sv, vt = np.linalg.svd(red); Rsp = vt[:rk]
_, _, vz = np.linalg.svd(J); Zsp = vz[-3:]
same = np.linalg.matrix_rank(np.vstack([Rsp, Zsp]), 1e-6) == 3
check("P4 the 3 zero modes are exactly the redundant directions i[S, V*]: S = covariant on-site spin-flavour Hermitians",
      len(Sinv) == 5 and rk == 3 and same, f"covariant on-site dim {len(Sinv)}, redundant rank {rk}")
check("P5 so of the 11 colour/weak-breaking couplings: 8 irrelevant, 3 exactly marginal (redundant), 0 relevant",
      10 - 2 == 8 and rk == 3)

# P6 nonlinear flow from a generic covariant cone (alpha/2pi * l as flow time)
d = NB.T @ rng.normal(size=13); d *= 0.35 / np.linalg.norm(d)
V = [Vs[m] + build(d)[m] for m in range(3)]
kh = [q / np.linalg.norm(q) for q in rng.normal(size=(6, 3))]
def spread(V):
    e = np.array([np.linalg.eigvalsh(sum(k[b] * V[b] for b in range(3))) for k in kh])
    return np.max(np.abs(np.abs(e) - 1))
sp = [spread(V)]; dt = 0.05
for step in range(60):
    k1 = beta(V); V = [V[b] + dt * k1[b] for b in range(3)]; V = [(v + v.conj().T) / 2 for v in V]
    if step % 20 == 19:
        sp.append(spread(V))
check("P6 nonlinear flow of a generic covariant cone: band speeds converge to 5-fold degenerate |k| (spread falls)",
      sp[-1] < 0.05 * sp[0], ' -> '.join(f"{x:.3g}" for x in sp))

# P7 time reversal (1 x i sigma_y) K
Ty = np.kron(np.eye(5), SIG[1])
Tm = np.array([NB @ coords([-(Ty @ M.conj() @ Ty) for M in build(NB.T @ e)]) for e in np.eye(13)]).T
wt_, Vt = np.linalg.eigh((Tm + Tm.T) / 2); Pt = Vt[:, wt_ > 0.5]
Jt = np.sort(np.linalg.eigvals(Pt.T @ J @ Pt).real)
Sev = [S for S in Sinv if np.allclose(Ty @ S.conj() @ Ty, S)]
cS = np.array([[np.real(np.trace(a.conj().T @ b)) for b in Sinv] for a in Sinv])
To = np.array([[np.real(np.trace(a.conj().T @ (Ty @ b.conj() @ Ty))) for b in Sinv] for a in Sinv])
nTe = int(np.sum(np.linalg.eigvals(np.linalg.solve(cS, To)).real > 0.5))
check("P7 with time reversal: cone 9 (2 blind + 7 breaking): 6 irrelevant, 1 redundant; on-site covariant 4 (2 blind + 2)",
      Pt.shape[1] == 9 and np.sum(np.abs(Jt + 8 / 3) < 1e-5) == 8 and np.sum(np.abs(Jt) < 1e-6) == 1 and nTe == 4,
      f"-8/3 x{np.sum(np.abs(Jt + 8 / 3) < 1e-5)}, 0 x{np.sum(np.abs(Jt) < 1e-6)}, on-site {nTe}")

# P8 relevant on-site terms and the commutant
gl5 = [np.eye(5)[:, [i]] @ np.eye(5)[[j], :] for i in range(5) for j in range(5)]
ib = [np.kron(e, I2) for e in gl5] + [np.kron(1j * e, I2) for e in gl5]
def icomm(mats):
    Mx = np.array([np.concatenate([(b @ M - M @ b).ravel() for M in mats]) for b in ib]).T
    s = np.linalg.svd(np.vstack([Mx.real, Mx.imag]), compute_uv=False)
    return int(np.sum(s < 1e-8 * s[0])) // 2
bc = [0.7 * np.kron(PE, SIG[m]) + 1.3 * np.kron(PT, SIG[m]) for m in range(3)]
M0 = np.kron(np.diag([.3, .3, -.2, -.2, -.2]), I2)
Mgen = sum(rng.normal() * S for S in Sinv)
# a TR-even generic on-site
Ste = []
for S in Sinv:
    Sp = (S + Ty @ S.conj() @ Ty) / 2
    if np.linalg.norm(Sp) > 1e-9:
        Ste.append(Sp)
MgT = sum(rng.normal() * S for S in Ste)
c13, cg, cgT = icomm([M0] + bc), icomm([Mgen] + bc), icomm([MgT] + bc)
check("P8 blind cone + blind on-site keeps u(2)+u(3)=13; any generic covariant on-site term (relevant) leaves 1",
      c13 == 13 and cg == 1 and cgT == 1, f"13 -> {cg} (TR-even on-site: {cgT})")
Sx = [S for S in Sinv if np.linalg.norm(S @ Vs[0] - Vs[0] @ S) > 1e-6][0]
dM = 1j * (Sx @ M0 - M0 @ Sx)
inS = np.linalg.matrix_rank(np.array([np.concatenate([coords([X, 0 * X, 0 * X])[:100]]) for X in Sinv + [dM]]), 1e-8) == len(Sinv)
check("P9 the redundant rotation U = exp(iS) carries the 2+3 on-site term into the spin-flavour on-site terms: "
      "marginal misalignment = relevant breaking", inS and np.linalg.norm(dM) > 1e-6 and icomm([expm(1j * 0.3 * Sx) @ M0 @ expm(-1j * 0.3 * Sx)] + Vs) < 13,
      f"commutant {icomm([expm(1j * 0.3 * Sx) @ M0 @ expm(-1j * 0.3 * Sx)] + Vs)}")
# P10 how much the irrelevant 8 shrink: delta ~ alpha^p, p = (8/3)(1/2pi) / b, b = N_W/(3 pi) (IR-free U(1))
for NW in (5, 16, 48):
    p = (8 / 3) / (2 * np.pi) / (NW / (3 * np.pi))
    rates[NW] = (p, (1 / 137.036) ** p)
p5, sup5 = rates[5]
check("P10 IR-free U(1): delta_IR/delta_UV = (alpha_IR/alpha_UV)^p, p = 4/N_W; even alpha_UV=1 -> 1/137 gives >= 1e-2",
      abs(p5 - 0.8) < 1e-12 and sup5 > 1e-3, ', '.join(f"N_W={n}: p={rates[n][0]:.3f}, {rates[n][1]:.2g}" for n in (5, 16, 48)))
check("P10b fixed alpha=1/137 from Planck to 1 GeV (l=44): exp(-(8/3)(alpha/2pi) l) = 0.87, far from <=1e-15",
      0.8 < np.exp(-(8 / 3) / (2 * np.pi) / 137.036 * 44) < 0.9)

# =============================================================== C
print("== C. CL-1 cube tick (flat, mu=0): light content and robust emergent copy symmetry ==")
sites = list(itertools.product((0, 1), repeat=3)); idx = {s: i for i, s in enumerate(sites)}
def eta(i, x): return (-1) ** sum(x[:i])
def Rc(k, par):
    H = np.zeros((8, 8), complex)
    for x in sites:
        for i in range(3):
            if x[i] != par:
                continue
            y = list(x); y[i] ^= 1; y = tuple(y)
            H[idx[y], idx[x]] += eta(i, x) * np.exp(1j * k[i]) / np.sqrt(3); H[idx[x], idx[y]] += eta(i, x) * np.exp(-1j * k[i]) / np.sqrt(3)
    return H
def Uf(k, e):
    Ue = expm(-1j * e / 2 * Rc(k, 0)); return Ue @ expm(1j * e * Rc(k, 1)) @ Ue
def HF(k, e):
    w, V = np.linalg.eig(Uf(k, e)); H = V @ np.diag(-np.angle(w)) @ np.linalg.inv(V); return (H + H.conj().T) / 2
eps = 0.6; I3 = np.eye(3); dk = 1e-4
A = [(HF(dk * I3[i], eps) - HF(-dk * I3[i], eps)) / (2 * dk) for i in range(3)]
v2 = (A[0] @ A[0])[0, 0].real
cliff = all(np.allclose(A[i] @ A[j] + A[j] @ A[i], 2 * v2 * (i == j) * np.eye(8), atol=1e-6) for i in range(3) for j in range(3))
om = -1j * A[0] @ A[1] @ A[2] / v2 ** 1.5
corner = np.sort(np.abs(np.angle(np.linalg.eigvals(Uf(np.pi / 2 * np.ones(3), eps)))))
check("C1 one node at k=0 with 8 components, isotropic cone v = 2 sin(eps)/sqrt3, chirality 4/4: 2 Dirac copies",
      np.allclose(HF(np.zeros(3), eps), 0, atol=1e-9) and cliff and abs(np.sqrt(v2) - 2 * np.sin(eps) / np.sqrt(3)) < 1e-6
      and abs(np.trace(om).real) < 1e-6, f"corner quasi-energy {corner[0]:.4f} = 2 eps")
gauge_fail = 0; syms = []
c0 = np.array([.5, .5, .5]); ks = [rng.normal(size=3) for _ in range(3)]
def perm_of(f):
    P = np.zeros((8, 8))
    for x in sites:
        P[idx[tuple(int(round(t)) % 2 for t in f(np.array(x)))], idx[x]] = 1
    return P
def gauge(M, T):
    D = np.full(8, np.nan, complex); D[0] = 1
    for _ in range(8):
        for a in range(8):
            for b in range(8):
                if abs(M[a, b]) > 1e-9 and np.isnan(D[a]) and not np.isnan(D[b]):
                    D[a] = T[a, b] / M[a, b] * D[b]
                if abs(M[a, b]) > 1e-9 and np.isnan(D[b]) and not np.isnan(D[a]):
                    D[b] = np.conj(T[a, b] / M[a, b] / D[a])
    return None if np.any(np.isnan(D)) else np.diag(D / np.abs(D))
for g in signed_perms(3):
    P = perm_of(lambda x: g @ (x - c0) + c0); D = gauge(P @ Rc(ks[0], 0) @ P.T, Rc(g @ ks[0], 0))
    ok = D is not None and all(np.allclose(D @ P @ Uf(k, eps) @ P.T @ D.conj().T, Uf(g @ k, eps)) for k in ks)
    if ok:
        syms.append((D @ P, g))
    else:
        gauge_fail += 1
PT_ = perm_of(lambda x: x + 1); DT = gauge(PT_ @ Rc(ks[0], 0) @ PT_.T, Rc(ks[0], 1))
epsd = np.diag([(-1.) ** sum(x) for x in sites]).astype(complex); GT = epsd @ DT @ PT_
okG = all(np.allclose((lambda Gk: Gk @ Uf(k, eps) @ Gk.conj().T)(epsd @ (expm(-1j * eps / 2 * Rc(k, 1)) @ expm(1j * eps / 2 * Rc(k, 0))).conj().T @ DT @ PT_), Uf(k, eps)) for k in ks)
check("C2 exact lattice group of the tick: all 48 O_h about the even-cube centre, and the (1,1,1) glide x sublattice sign",
      len(syms) == 48 and okG)
SH = []
H0 = lambda k: Rc(k, 0) - Rc(k, 1)
for i in range(3):
    Pi = perm_of(lambda x: x + I3[i]); Di = gauge(Pi @ H0(ks[0]) @ Pi.T, H0(ks[0])); SH.append(Di @ Pi)
viol = []
for e in (0.2, 0.4):
    kq = 0.3 * ks[1] / np.linalg.norm(ks[1])
    viol.append(np.linalg.norm(SH[0] @ HF(kq, e) @ SH[0].conj().T - HF(kq, e)) / np.linalg.norm(HF(kq, e)))
check("C2b leading order eps(R_e - R_o) is the Kogut-Susskind Hamiltonian (single-site shifts exact); the tick breaks them at O(eps^2)",
      all(np.allclose(S @ H0(k) @ S.conj().T, H0(k)) for S in SH for k in ks) and 3.0 < viol[1] / viol[0] < 5.0,
      f"rel. shift violation {viol[0]:.2e}, {viol[1]:.2e}")
# Pauli-Gursey: antisymmetric B with A_i^T B = B A_i
asb = [np.eye(8)[:, [i]] @ np.eye(8)[[j], :] - np.eye(8)[:, [j]] @ np.eye(8)[[i], :] for i, j in itertools.combinations(range(8), 2)]
Mx = np.array([np.concatenate([(a.T @ B - B @ a).ravel() for a in A]) for B in asb]).T
npg = int(np.sum(np.linalg.svd(Mx, compute_uv=False) < 1e-6))
check("C3 free cone: number-conserving commutant u(2)+u(2) (8); with Pauli-Gursey pairings (4 complex) the free U(4) of 4 Weyl",
      cdim_commutant(A, 8) == 8 and npg == 4, f"pairings {npg}")
H8 = herm_basis(8); n8 = np.array([np.real(np.trace(b.conj().T @ b)) for b in H8])
def co(M): return np.array([np.real(np.trace(b.conj().T @ M)) for b in H8]) / n8
def fr(v): return sum(x * b for x, b in zip(v, H8))
def allowed(gens, anti=(), chi=()):
    def sp(v): return fr(v[:64]), [fr(v[64 * (i + 1):64 * (i + 2)]) for i in range(3)]
    def pk(h, Aa): return np.concatenate([co(h)] + [co(a) for a in Aa])
    rows = []
    for U, O in gens:
        rows.append(np.array([pk(*(lambda h, Aa: (U @ h @ U.conj().T - h, [U @ Aa[i] @ U.conj().T - sum(O[j, i] * Aa[j] for j in range(3)) for i in range(3)]))(*sp(e))) for e in np.eye(256)]).T)
    for U, O in anti:
        rows.append(np.array([pk(*(lambda h, Aa: (U @ h.conj() @ U.conj().T - h, [-U @ Aa[i].conj() @ U.conj().T - sum(O[j, i] * Aa[j] for j in range(3)) for i in range(3)]))(*sp(e))) for e in np.eye(256)]).T)
    for U, O in chi:
        rows.append(np.array([pk(*(lambda h, Aa: (epsd @ U @ h @ U.conj().T @ epsd + h, [epsd @ U @ Aa[i] @ U.conj().T @ epsd + sum(O[j, i] * Aa[j] for j in range(3)) for i in range(3)]))(*sp(e))) for e in np.eye(256)]).T)
    N = nullspace_real(np.vstack(rows))
    hs = [sp(v)[0] for v in N]; ms = [m for v in N for m in [sp(v)[0]] + sp(v)[1] if np.linalg.norm(m) > 1e-9]
    return len(N), np.linalg.matrix_rank(np.array([co(x) for x in hs]), 1e-8) if hs else 0, cdim_commutant(ms, 8), hs
def fnd(g): return [s for s in syms if np.allclose(s[1], g)][0]
C4, C3, INV, C2 = fnd(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1.]])), fnd(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.]])), fnd(-I3), fnd(np.diag([-1, -1, 1.]))
TR = (np.eye(8), I3); CH = (np.eye(8), I3)
res = {nm: allowed(*a) for nm, a in {
    "O_h": ([C4, C3, INV],), "O_h+glide": ([C4, C3, INV, (GT, I3)],), "O_h+glide+T": ([C4, C3, INV, (GT, I3)], [TR]),
    "O_h+glide+T+PH": ([C4, C3, INV, (GT, I3)], [TR], [CH])}.items()}
check("C4 robust (all dim<=4 terms the lattice group allows) commutant: O_h 1, +glide 2, +T 8, +PH 8 (=u(2)+u(2))",
      [res[k][2] for k in res] == [1, 2, 8, 8], ' '.join(f"{k}:{v[0]}ops/{v[2]}" for k, v in res.items()))
W = []
for i in range(3):
    Hh = np.zeros((8, 8), complex)
    for x in sites:
        if x[i] == 0:
            y = list(x); y[i] = 1; y = tuple(y); Hh[idx[y], idx[x]] += eta(i, x); Hh[idx[x], idx[y]] += eta(i, x)
    W.append(Hh)
s_c = 1j * W[0] @ W[1] @ W[2] @ (sum(W) / np.sqrt(3))
nG, rG, cG, hsG = allowed([C3, C2, INV], [C4], [C4])
nGg, rGg, cGg, _ = allowed([C3, C2, INV, (GT, I3)], [C4], [C4])
mass_ok = []
for sg in (1, -1):
    Pc = (np.eye(8) + sg * s_c) / 2
    mass_ok.append(any(np.linalg.norm(Pc @ (hh @ A[0] + A[0] @ hh) @ Pc) < 1e-8 and np.linalg.norm(Pc @ hh @ Pc) > 1e-6 for hh in hsG))
check("C5 copy sign s: s^2=1, commutes with the cone, odd under C4; with the copy mass's group (T_h, T.C4, PH.C4) a Dirac "
      "mass of each copy is allowed unless the glide survives", np.allclose(s_c @ s_c, np.eye(8)) and all(np.allclose(s_c @ a, a @ s_c, atol=1e-6) for a in A)
      and np.allclose(C4[0] @ s_c @ C4[0].conj().T, -s_c) and all(mass_ok) and rG == 2 and cGg == 4,
      f"no glide: {rG} relevant, commutant {cG}; with glide: commutant {cGg} = U(1)^4")
deg = np.sort(-np.angle(np.linalg.eigvals(Uf(0.4 * ks[2], eps))))
check("C6 the free tick's spectrum stays 4-fold degenerate at every k (copy pair x Kramers-type)", np.allclose(deg[:4], deg[0], atol=1e-8))

# =============================================================== S
print("== S. Emergent Spin(10) or SU(5) on 16 free Weyl modes ==")
Xp, Yp, Zp = SIG[0], SIG[1], SIG[2]
def kr(*m):
    o = np.eye(1)
    for x in m:
        o = np.kron(o, x)
    return o
Gm = []
for j in range(5):
    Gm += [kr(*([Zp] * j), Xp, *([I2] * (4 - j))), kr(*([Zp] * j), Yp, *([I2] * (4 - j)))]
Nn = sum((Gm[2 * j] + 1j * Gm[2 * j + 1]).conj().T @ (Gm[2 * j] + 1j * Gm[2 * j + 1]) / 4 for j in range(5))
evn = [i for i in range(32) if round(np.real(Nn[i, i])) % 2 == 0]
gens16 = [(0.5j * Gm[a] @ Gm[b])[np.ix_(evn, evn)] for a, b in itertools.combinations(range(10), 2)]
def alg_dim(gs, n):
    basis = [np.eye(n)]; vecs = np.array([np.eye(n).ravel()])
    frontier = list(gs)
    while frontier:
        new = []
        for M in frontier:
            v = M.ravel()
            if np.linalg.matrix_rank(np.vstack([vecs, v]), 1e-8) > len(vecs):
                vecs = np.vstack([vecs, v]); basis.append(M); new.append(M)
        frontier = [a @ b for a in new for b in gs][:400] if len(vecs) < n * n else []
    return len(vecs)
ad = 256 if cdim_commutant(gens16, 16) == 1 else -1
check("S1 Burnside: so(10) on the 16 generates all of gl(16): a free fixed point with emergent Spin(10) has emergent U(16)",
      ad == 256, f"algebra dim {ad}")
Th = (Gm[0] @ Gm[1] @ Gm[2] @ Gm[3])[np.ix_(evn, evn)]
ThH = Th if np.allclose(Th, Th.conj().T) else 1j * Th
Mx = np.array([g.ravel() for g in gens16]).T
inso = np.linalg.matrix_rank(np.column_stack([Mx, ThH.ravel()]), 1e-8) > np.linalg.matrix_rank(Mx, 1e-8)
cth = np.linalg.matrix_rank(np.array([(ThH @ g - g @ ThH).ravel() for g in gens16]), 1e-8)
check("S2 a number-conserving lattice gives vector-like U(1)_N = Theta (+1 on 8, -1 on 8): not in so(10); commutant PS (21)",
      inso and 45 - cth == 21, f"commutant {45 - cth}")
def sym_inv(gs, n):
    S = [np.eye(n)[:, [i]] @ np.eye(n)[[j], :] + np.eye(n)[:, [j]] @ np.eye(n)[[i], :] for i in range(n) for j in range(i, n)]
    Mx = np.array([np.concatenate([(g.T @ B + B @ g).ravel() for g in gs]) for B in S]).T
    return int(np.sum(np.linalg.svd(Mx, compute_uv=False) < 1e-8))
def cubic(gs):
    X = sum(rng.normal() * g for g in gs); return abs(np.trace(X @ X @ X))
def su(n):
    out = []
    for i, j in itertools.combinations(range(n), 2):
        E = np.zeros((n, n), complex); E[i, j] = E[j, i] = 1; out.append(E)
        E = np.zeros((n, n), complex); E[i, j] = -1j; E[j, i] = 1j; out.append(E)
    out += [np.diag(np.r_[np.ones(k), -k, np.zeros(n - k - 1)]).astype(complex) for k in range(1, n)]
    return out
def so(n): return [m for m in su(n) if np.allclose(m.imag, m.imag) and np.allclose(m.real, 0)]
def tens(ga, gb, na, nb): return [np.kron(g, np.eye(nb)) for g in ga] + [np.kron(np.eye(na), g) for g in gb]
Jy = np.kron(np.eye(8), SIG[1])
spg = [m for m in su(16) if np.allclose(m.T @ Jy + Jy @ m, 0)]
j = 7.5; mm = np.arange(j, -j - 1, -1); Jp = np.diag(np.sqrt(j * (j + 1) - mm[1:] * (mm[1:] + 1)), 1)
jg = [(Jp + Jp.T) / 2, (Jp - Jp.T) / (2j), np.diag(mm)]
tab = {"SO(16)": (so(16), 120, None), "Sp(16)": (spg, 136, 1), "SU2xSU8": (tens(su(2), su(8), 2, 8), 66, None),
       "SU4xSU4": (tens(su(4), su(4), 4, 4), 30, None), "S(U8xU8)": ([np.kron(np.eye(2), g) for g in []] + tens([np.diag([1, -1.]).astype(complex)], su(8), 2, 8)[:1] + [np.kron(np.diag([1, 0]), g) for g in su(8)] + [np.kron(np.diag([0, 1]), g) for g in su(8)], 127, None),
       "Spin(10)": (gens16, 45, 0), "SU2(j=15/2)": (jg, 3, 0), "SU2xSO8": (tens(su(2), so(8), 2, 8), 31, 0)}
verdict = {}
for nm, (gs, dim, witten_odd) in tab.items():
    ok = cubic(gs) < 1e-8 and sym_inv(gs, 16) == 0 and witten_odd in (0, None)
    verdict[nm] = ok
want = {"SO(16)": False, "Sp(16)": False, "SU2xSU8": False, "SU4xSU4": False, "S(U8xU8)": False, "Spin(10)": True, "SU2(j=15/2)": True, "SU2xSO8": True}
check("S3 16 Weyl: largest anomaly-free AND mass-forbidding subgroup among maximal SU(16) subgroups (+ SU2xSO8) is Spin(10), 45",
      verdict == want and not verdict["Sp(16)"], ' '.join(f"{k}:{'ok' if v else 'x'}" for k, v in verdict.items()))
tab32 = {"Spin(12) 32": 66, "SU2xSO16 (2,16)": 123}
g32 = tens(su(2), so(16), 2, 16)
check("S3b the same selector at 32 Weyl picks the pseudoreal SU(2)xSO(16) (123) over Spin(12) (66): it is not a GUT selector",
      cubic(g32) < 1e-8 and sym_inv([sum(rng.normal() * g for g in g32) for _ in range(4)], 32) == 0 and (16 % 2 == 0))
counts = [4 * b ** 3 for b in range(1, 5)] + [8 * b ** 3 for b in range(1, 5)]
check("S4 Weyl counts of CL-type cells: 4 b^3 (zoom b, one node) or 8 b^3 (partner light) never equal 16", 16 not in counts,
      str(sorted(set(counts))))

print(f"elapsed {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
