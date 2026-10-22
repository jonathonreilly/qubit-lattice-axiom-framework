AUDIT_INPUT_PATHS = ('docs/NUMBER_CONSERVING_TICK_FIXES_THE_U5_FRAME_BUT_HALF_LINK_2_PLUS_3_SPLIT_IS_ORBITAL_NOT_INTERNAL_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Does the update's own time structure supply the complex structure J that picks U(5) inside Spin(10),
and can a composite (site-cluster) structure supply the second split U(5) -> S(U(3)xU(2))?

Exact finite linear algebra on Cl(10) built from 5 modes (Jordan-Wigner, 32 dims, 16 = even half).
  T. time -> J: positive frequency J_A = A(-A^2)^(-1/2) of a one-body tick generator; commutants by frequency
     multiplicity; the complex-amplitude i alone; the Z^3 x tick point group on R^4; momentum dependence of J(k)
     with and without number conservation; the pi/2 half-tick; arrow <-> which half is the 16.
  S. second split: 2d half-link patterns = 1 + (d-1) + d; the site + 6 half-link star; Gamma-point tick on E+T1
     gives u(2)+u(3) and the A = aX + bY orientation; hypercharges and anomalies of the 16; then generic
     cubic-covariant cone terms on (E+T1) x spin; the qubit-spinor reading; the Lee-sphere 7-star tiling.
Supplied model; finite diagnostic; no physical identification.
"""
import itertools, signal, sys, time
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (print('TIMEOUT'), sys.exit(1)))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
rng = np.random.default_rng(20261022)
T0 = time.time()
PASS = FAIL = 0
TOL = 1e-9


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))


def kron(*m):
    out = np.eye(1)
    for a in m:
        out = np.kron(out, a)
    return out


I2 = np.eye(2); X2 = np.array([[0, 1], [1, 0]], complex); Y2 = np.array([[0, -1j], [1j, 0]]); Z2 = np.diag([1., -1.])
SIG = [X2, Y2, Z2.astype(complex)]


def majoranas(n):
    G = []
    for j in range(n):
        pre = [Z2] * j; post = [I2] * (n - 1 - j)
        G.append(kron(*pre, X2, *post).astype(complex)); G.append(kron(*pre, Y2, *post).astype(complex))
    return G


G = majoranas(5)
cmode = [(G[2 * j] + 1j * G[2 * j + 1]) / 2 for j in range(5)]
Nmode = [c.conj().T @ c for c in cmode]
Ntot = sum(Nmode)
GAM = 1j * np.linalg.multi_dot(G)                      # chirality Gamma_11, squares to 1


def F(B):          # Fock lift: [F(B), g_k] = sum_i B_ik g_i
    return 0.25 * sum(B[i, j] * G[i] @ G[j] for i in range(10) for j in range(10) if B[i, j] != 0)


def antisym_basis(n):
    out = []
    for i, j in itertools.combinations(range(n), 2):
        E = np.zeros((n, n)); E[i, j] = 1; E[j, i] = -1; out.append(E)
    return out


SO10 = antisym_basis(10)


def commutant_dim(mats, basis):
    rows = [np.concatenate([(b @ M - M @ b).ravel() for M in mats]) for b in basis]
    Mx = np.array(rows).T
    s = np.linalg.svd(Mx, compute_uv=False)
    return int(np.sum(s < 1e-8 * max(1, s[0]))) + max(0, len(basis) - len(s))


def sqrt_inv_psd(S):
    w, V = np.linalg.eigh(S)
    return V @ np.diag(w ** -0.5) @ V.T


def Jof(A):
    return A @ sqrt_inv_psd(-A @ A)


def pf(A):
    n = A.shape[0]
    if n == 0:
        return 1.0
    tot = 0.0
    for j in range(1, n):
        if A[0, j] != 0:
            idx = [k for k in range(n) if k not in (0, j)]
            tot += (-1) ** (j + 1) * A[0, j] * pf(A[np.ix_(idx, idx)])
    return tot


def NJ(J):
    return 1j * F(J) + 2.5 * np.eye(32)


def herm_basis(n):
    out = [np.diag(np.eye(n)[i]).astype(complex) for i in range(n)]
    for i, j in itertools.combinations(range(n), 2):
        E = np.zeros((n, n), complex); E[i, j] = E[j, i] = 1; out.append(E)
        E = np.zeros((n, n), complex); E[i, j] = -1j; E[j, i] = 1j; out.append(E)
    return out


def rand_so(n):
    M = rng.normal(size=(n, n)); return M - M.T


def rand_orth(n):
    Q, R = np.linalg.qr(rng.normal(size=(n, n))); return Q @ np.diag(np.sign(np.diag(R)))


# standard complex structure fixed by the JW modes: N_{J0} = N_total
J0 = np.zeros((10, 10))
for a in range(5):
    J0[2 * a + 1, 2 * a] = 1; J0[2 * a, 2 * a + 1] = -1
if np.linalg.norm(NJ(J0) - Ntot) > 1e-9:
    J0 = -J0
print("== T. Does the tick supply J? ==")
check("T0 N_J = iF(J) + 5/2 reproduces the JW occupation number for the mode complex structure J0",
      np.linalg.norm(NJ(J0) - Ntot) < 1e-9)

# T1 positive frequency
okJ = okC = okG = okH = True
for t in range(6):
    A = rand_so(10)
    J = Jof(A)
    okJ &= np.linalg.norm(J @ J + np.eye(10)) < 1e-9 and np.linalg.norm(J.T @ J - np.eye(10)) < 1e-9 \
        and np.linalg.norm(J @ A - A @ J) < 1e-9
    H = 1j * F(A); N = NJ(J)
    okC &= np.linalg.norm(H @ N - N @ H) < 1e-8
    w, V = np.linalg.eigh(H)
    g = V[:, 0]
    okG &= abs(np.real(g.conj() @ N @ g)) < 1e-8
    om = np.sort(np.abs(np.linalg.eigvals(A).imag))[::2]
    okH &= abs(w[0] + om.sum() / 2) < 1e-8
check("T1a J_A = A(-A^2)^(-1/2) is an orthogonal complex structure commuting with A (6 random ticks)", okJ)
check("T1b the tick H_A = iF(A) conserves the number N_{J_A} (fermion number is the tick's own)", okC)
check("T1c positive frequency: ground state of H_A is the N_{J_A} = 0 state, E0 = -sum(omega)/2", okG and okH)
A = rand_so(10); J = Jof(A)
c25 = commutant_dim([J], SO10)
check("T1d C_so10(J_A) has dim 25 = u(5); the J-orbit SO(10)/U(5) has dim 20 (a choice of J is 20 numbers)",
      c25 == 25 and 45 - c25 == 20, f"dim {c25}")

# T1e arrow <-> chirality labelling
okA = True; signs = []
for t in range(6):
    A = rand_so(10); J = Jof(A)
    for s in (1, -1):
        P = np.diag(np.exp(1j * np.pi * np.round(np.linalg.eigvalsh(NJ(s * J)))))
        w, V = np.linalg.eigh(NJ(s * J)); Ppar = V @ P @ V.conj().T
        r = np.real(np.trace(Ppar @ GAM)) / 32
        signs.append(np.sign(r) * np.sign(pf(s * J)))
        okA &= abs(abs(r) - 1) < 1e-8
check("T1e (-1)^{N_J} = c Pf(J) Gamma_11 with one fixed c: reversing time (A->-A, J->-J) swaps 16 <-> 16bar",
      okA and len(set(signs)) == 1, f"c = {signs[0]:+.0f}")

# T2 multiplicities
def tick_with(mults):
    blocks = []; om = 1.0
    for m in mults:
        blocks += [om] * m; om += 0.7
    A = np.zeros((10, 10))
    for a, w in enumerate(blocks):
        A[2 * a + 1, 2 * a] = w; A[2 * a, 2 * a + 1] = -w
    O = rand_orth(10)
    return O @ A @ O.T


res = {m: commutant_dim([tick_with(m)], SO10) for m in [(5,), (3, 2), (4, 1), (2, 2, 1), (1, 1, 1, 1, 1)]}
exp_ = {(5,): 25, (3, 2): 13, (4, 1): 17, (2, 2, 1): 9, (1, 1, 1, 1, 1): 5}
check("T2 C_so10(A) = sum u(m_k) over frequency multiplicities: (5)25 (3,2)13 (4,1)17 (2,2,1)9 (1^5)5",
      res == exp_, str(list(res.values())))

# T3 complex amplitudes alone
okI = all(np.linalg.norm((1j * np.eye(32)) @ (G[i] @ G[j]) - (G[i] @ G[j]) @ (1j * np.eye(32))) < 1e-12
          for i in range(10) for j in range(10))
check("T3 the amplitude i is central on Fock space: it commutes with all 45 so(10) generators (selects nothing)", okI)

# T4 point groups on R^4
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


WB3 = [np.block([[g, np.zeros((3, 1))], [np.zeros((1, 3)), np.eye(1) * tr]]) for g in signed_perms(3) for tr in (1, -1)]
WB4 = signed_perms(4)
gl4 = [np.eye(4)[:, [i]] @ np.eye(4)[[j], :] for i in range(4) for j in range(4)]
cB3 = commutant_dim(WB3, gl4); cB4 = commutant_dim(WB4, gl4)
# commutant of W(B3) x time reversal is R(+)R (diag(a 1_3, b)); x^2 >= 0 on both blocks so no J^2 = -1
check("T4 Z^3 x tick point group on R^4: commutant dim 2 = R(+)R (W(B4): 1), contains no J (odd real blocks)",
      cB3 == 2 and cB4 == 1, f"W(B3)xT {cB3}, W(B4) {cB4}")

# T5 momentum-dependent J(k): pairing vs number-conserving ticks (5 modes per site, 1D chain suffices)
def bloch(A0, B, k):
    return A0 + B * np.exp(1j * k) - B.T * np.exp(-1j * k)


def realify(h):            # one-body number-conserving h on C^5 -> real antisymmetric A on the 10 Majoranas
    Hf = sum(h[a, b] * cmode[a].conj().T @ cmode[b] for a in range(5) for b in range(5))
    return np.array([[np.real(-1j * np.trace(G[i] @ (Hf @ G[k] - G[k] @ Hf)) / 32) for k in range(10)]
                     for i in range(10)])


A0 = rand_so(10); B = rng.normal(size=(10, 10)) * 0.4
def Jk_of(k):
    Ak = bloch(A0, B, k); w, V = np.linalg.eigh(-Ak @ Ak)
    return Ak @ V @ np.diag(w ** -0.5) @ V.conj().T
dJ = np.linalg.norm(Jk_of(0.3) - Jk_of(1.9))
cP = commutant_dim([A0, B, B.T], SO10)
J2 = J0[:2, :2]
def Rf(M):
    return np.kron(M.real, np.eye(2)) + np.kron(M.imag, J2)
h0 = rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5)); h0 = h0 + h0.conj().T
h1 = rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5))
mats = [Rf(1j * h0), Rf(h1), Rf(h1).T]
cN = commutant_dim(mats, SO10)
okJ0 = np.linalg.norm(Rf(1j * np.eye(5)) - J0) < 1e-12 and all(np.linalg.norm(M @ J0 - J0 @ M) < 1e-9 for M in mats)
check("T5a generic Majorana tick with pairing: positive-frequency J(k) varies with k; on-site commutant 0",
      dJ > 0.1 and cP == 0, f"|J(.3)-J(1.9)| = {dJ:.2f}, commutant {cP}")
check("T5b number-conserving tick (CL-1 hops move occupations): k-independent J0 commutes; commutant 1 = U(1)_X",
      okJ0 and cN == 1, f"commutant {cN}")
R6 = rand_orth(6); R6 = R6 @ np.diag([1, 1, 1, -1, -1, -1]) @ R6.T
Uh = expm(-1j * (np.pi / 2) * R6); Ue = expm(-1j * 0.37 * R6)
check("T5c pi/2 half-tick exp(-i pi/2 R) squares to -1 (a J), but it is the hop R itself: site-nonlocal; eps=.37 not",
      np.linalg.norm(Uh @ Uh + np.eye(6)) < 1e-9 and np.linalg.norm(Ue @ Ue + np.eye(6)) > 0.5
      and np.abs(R6 - np.diag(np.diag(R6))).max() > 0.1)

print("== S. The second split: composite half-link patterns ==")
O24 = signed_perms(3, det=1)
check("S0 rotation group of the cube: 24 signed permutations", len(O24) == 24)


def dir_rep(d, group):
    dirs = [s * np.eye(d)[m] for m in range(d) for s in (1, -1)]
    def P(R):
        M = np.zeros((2 * d, 2 * d))
        for i, v in enumerate(dirs):
            j = [k for k, w in enumerate(dirs) if np.allclose(w, R @ v)][0]
            M[j, i] = 1
        return M
    return [P(R) for R in group], dirs


def iso_pieces(d):
    """basis of the 2d direction space: A1, the (d-1) even traceless patterns, the d odd (dipole) patterns."""
    n = 2 * d
    odd = [(np.eye(n)[2 * m] - np.eye(n)[2 * m + 1]) / np.sqrt(2) for m in range(d)]
    ev = np.array([(np.eye(n)[2 * m] + np.eye(n)[2 * m + 1]) / np.sqrt(2) for m in range(d)])
    a1 = ev.sum(0) / np.sqrt(d)
    Q, _ = np.linalg.qr(np.column_stack([a1] + [ev[m] for m in range(d - 1)]))
    E = [Q[:, i] for i in range(1, d)]
    return a1, np.array(E).T, np.array(odd).T


okS1 = True; info = []
for d in (2, 3, 4):
    grp = signed_perms(d, det=1) if d == 3 else signed_perms(d)
    Ps, dirs = dir_rep(d, grp)
    a1, Eb, Tb = iso_pieces(d)
    glE = [np.eye(d - 1)[:, [i]] @ np.eye(d - 1)[[j], :] for i in range(d - 1) for j in range(d - 1)]
    glT = [np.eye(d)[:, [i]] @ np.eye(d)[[j], :] for i in range(d) for j in range(d)]
    cE = commutant_dim([Eb.T @ P @ Eb for P in Ps], glE)
    cT = commutant_dim([Tb.T @ P @ Tb for P in Ps], glT)
    full = commutant_dim(Ps, [np.eye(2 * d)[:, [i]] @ np.eye(2 * d)[[j], :] for i in range(2 * d) for j in range(2 * d)])
    okS1 &= cE == 1 and cT == 1 and full == 3
    info.append(f"d={d}: 1+{d-1}+{d}")
check("S1 2d half-link patterns = A1 + (d-1) + d, irreducible and inequivalent (d=2,3,4): SU(d-1)xSU(d) at d=3",
      okS1, ', '.join(info))
Ps6, dirs6 = dir_rep(3, O24)
a1, Eb, Tb = iso_pieces(3)
B5 = np.column_stack([Eb, Tb])                                     # E (2) + T1 (3)
D5 = [B5.T @ P @ B5 for P in Ps6]
# other cells: 3 unoriented axes, 3 oriented axes, 8 cube corners
ax_un = [np.abs(R) for R in O24]; ax_or = O24
corn = [s for s in itertools.product([1, -1], repeat=3)]
Pc = [np.array([[1.0 if np.allclose(np.array(corn[i]), R @ np.array(corn[j])) else 0 for j in range(8)] for i in range(8)]) for R in O24]
def mult_E(mats):          # multiplicity of E via characters: chi_E = 2,0,-1,0,2 on (e, C4, C3, C2', C2)
    chi = []
    for R, M in zip(O24, mats):
        tr = round(np.trace(R)); ang = {3: 'e', 1: 'C4', 0: 'C3', -1: 'C2'}[tr]
        if ang == 'C2':
            ang = 'C2a' if np.allclose(np.abs(np.diag(R)), 1) else 'C2b'
        chi.append({'e': 2, 'C4': 0, 'C3': -1, 'C2a': 2, 'C2b': 0}[ang] * np.trace(M))
    return round(sum(chi) / 24)
mE = [mult_E(ax_un), mult_E(ax_or), mult_E(Pc), mult_E(Ps6)]
check("S1b E-multiplicity: unoriented axes 1, oriented axes (vector) 0, 2^3 cube corners 0, 6 half-links 1",
      mE == [1, 0, 0, 1], str(mE))

# S2 site + 6 half-link star
H7 = np.zeros((7, 7)); H7[0, 1:] = 1; H7[1:, 0] = 1
w7 = np.linalg.eigvalsh(H7)
anti = sum(np.outer(np.eye(6)[2 * m], np.eye(6)[2 * m + 1]) + np.outer(np.eye(6)[2 * m + 1], np.eye(6)[2 * m]) for m in range(3))
adj = np.array([[1.0 if abs(dirs6[i] @ dirs6[j]) < 0.5 else 0 for j in range(6)] for i in range(6)])
evE = [float(np.round(Eb.T @ M @ Eb, 9)[0, 0]) for M in (anti, adj)]; evT = [float(np.round(Tb.T @ M @ Tb, 9)[0, 0]) for M in (anti, adj)]
check("S2a star (site + 6 half-links, site-link hop only): spectrum +-sqrt6, 0^5; the zero space is E+T1 -> u(5)",
      np.allclose(sorted(w7), sorted([-np.sqrt(6), np.sqrt(6)] + [0] * 5)) and
      np.allclose(H7[1:, 1:] @ B5, 0) and np.allclose(H7[0, 1:] @ B5, 0))
check("S2b covariant half-link terms split it: antipode swap E +1 / T1 -1; adjacency E -2 / T1 0 (A1 4)",
      evE == [1, -2] and evT == [-1, 0], f"E {evE} T1 {evT}")

# S3 Gamma-point tick on E+T1
gl5 = [np.eye(5)[:, [i]] @ np.eye(5)[[j], :] for i in range(5) for j in range(5)]
herm5 = herm_basis(5)
def inv_space(mats, basis):
    rows = [np.concatenate([(D @ b @ D.T - b).ravel() for D in mats]) for b in basis]
    Mx = np.array(rows).T; Mx = np.vstack([Mx.real, Mx.imag])
    u, s, vt = np.linalg.svd(Mx)
    null = vt[np.sum(s > 1e-9):]
    return [sum(c * b for c, b in zip(v, basis)) for v in null]
inv0 = inv_space(D5, herm5)
M0 = sum(rng.normal() * b for b in inv0)
check("S3a cubic-invariant on-site tick on E+T1: 2 parameters (omega_E, omega_T); generic omega_E != omega_T",
      len(inv0) == 2 and abs(np.linalg.eigvalsh(M0)[0] - np.linalg.eigvalsh(M0)[-1]) > 1e-3, f"{len(inv0)}")
AG = realify(M0); JG = Jof(AG)
cG = commutant_dim([AG], SO10)
check("S3b its so(10) commutant is u(2)+u(3) = 13 (= SM x U(1)_chi floor of the merged ruleset)", cG == 13, f"{cG}")
Pmode = []
for a in range(5):
    P = np.zeros((10, 10)); P[2 * a, 2 * a] = P[2 * a + 1, 2 * a + 1] = 1; Pmode.append(P)
Nm = [1j * F(JG @ P) + 0.5 * np.eye(32) for P in Pmode]
NE = Nm[0] + Nm[1]; NT = Nm[2] + Nm[3] + Nm[4]; NN = NE + NT
Yop = NE / 2 - NT / 3; Xop = 2 * NN - 5 * np.eye(32)
HG = 1j * F(AG)
basis_fit = np.array([Xop.ravel(), Yop.ravel(), np.eye(32).ravel()]).T
coef, *_ = np.linalg.lstsq(basis_fit, HG.ravel(), rcond=None)
check("S3c the tick generator itself is the 45 orientation a X + b Y (+const): residual 0",
      np.linalg.norm(basis_fit @ coef - HG.ravel()) < 1e-9, f"a={coef[0].real:+.3f} b={coef[1].real:+.3f}")
dN = np.real(np.diag(NN)); dE = np.real(np.diag(NE)); dT = np.real(np.diag(NT))
diag_ok = all(np.linalg.norm(M - np.diag(np.diag(M))) < 1e-9 for M in (NN, NE, NT))
even = np.where(np.round(dN) % 2 == 0)[0]
content = {}
for i in even:
    key = (int(round(dT[i])), int(round(dE[i])))
    content[key] = content.get(key, 0) + 1
names = {(1, 1): 'Q(3,2)', (2, 0): 'u^c(3b,1)', (2, 2): 'd^c(3b,1)', (3, 1): 'L(1,2)', (0, 2): 'e^c', (0, 0): 'nu^c'}
Ys = {k: k[1] / 2 - k[0] / 3 for k in content}
want = {(1, 1): (6, 1 / 6), (2, 0): (3, -2 / 3), (2, 2): (3, 1 / 3), (3, 1): (2, -1 / 2), (0, 2): (1, 1.0), (0, 0): (1, 0.0)}
okc = diag_ok and all(k in content and content[k] == v[0] and abs(Ys[k] - v[1]) < 1e-12 for k, v in want.items()) \
    and sum(content.values()) == 16
check("S4a the 16 (even N_{J_A}) is Q u^c d^c L e^c nu^c with Y = 1/6,-2/3,1/3,-1/2,1,0",
      okc, ' '.join(f"{names[k]}:{Ys[k]:+.2f}" for k in sorted(content)))
P16 = np.eye(32)[:, even]
def tr16(M):
    return np.real(np.trace(P16.T @ M @ P16))
lam3 = Nm[2] - Nm[3]; tau3 = Nm[0] - Nm[1]
anom = {'Y': tr16(Yop), 'Y3': tr16(Yop @ Yop @ Yop), 'SU3^2Y': tr16(lam3 @ lam3 @ Yop), 'SU2^2Y': tr16(tau3 @ tau3 @ Yop),
        'X': tr16(Xop), 'X3': tr16(Xop @ Xop @ Xop), 'X2Y': tr16(Xop @ Xop @ Yop), 'XY2': tr16(Xop @ Yop @ Yop),
        'SU3^2X': tr16(lam3 @ lam3 @ Xop), 'SU2^2X': tr16(tau3 @ tau3 @ Xop)}
ndoub = content[(1, 1)] // 2 * 1 + content[(3, 1)] // 2
check("S4b anomaly-free: Y, Y^3, SU3^2 Y, SU2^2 Y, X, X^3, X^2Y, XY^2, SU3^2 X, SU2^2 X all 0; doublets even (Witten)",
      all(abs(v) < 1e-9 for v in anom.values()) and ndoub % 2 == 0, f"doublets {ndoub}")
Xch = sorted(set(float(x) for x in np.round(np.real(np.diag(P16.T @ Xop @ P16)), 6)))
check("S4c X = 2N_J - 5 (time's own number, twisted into so(10)) has charges -5,-1,3 on 1,10,5b: U(1)_chi",
      Xch == [-5.0, -1.0, 3.0], str(Xch))

# S5 cone terms on (E+T1) x spin: binary lifts
def lift(R):
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if th < 1e-9:
        return np.eye(2, dtype=complex)
    if abs(th - np.pi) < 1e-9:
        n = np.linalg.eigh(R)[1][:, -1]
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(th))
    return np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * sum(n[i] * SIG[i] for i in range(3))
Us = [lift(R) for R in O24]
okL = all(np.allclose(U @ SIG[m] @ U.conj().T, sum(R[n, m] * SIG[n] for n in range(3))) for U, R in zip(Us, O24) for m in range(3))
check("S5a SU(2) lifts of the 24 rotations act on sigma as the vector", okL)
D10 = [np.kron(D, U) for D, U in zip(D5, Us)]
gens = [i for i, R in enumerate(O24) if np.allclose(R, [[0, -1, 0], [1, 0, 0], [0, 0, 1]]) or np.allclose(R, [[0, 0, 1], [1, 0, 0], [0, 1, 0]])]
gl10 = [np.eye(10)[:, [i]] @ np.eye(10)[[j], :] for i in range(10) for j in range(10)]
h10 = herm_basis(10)
rows = []
for b_idx in range(3 * len(h10)):
    mu, b = divmod(b_idx, len(h10))
    Ms = [np.zeros((10, 10), complex) for _ in range(3)]; Ms[mu] = h10[b]
    res_ = []
    for gi in gens:
        D, R = D10[gi], O24[gi]
        for m in range(3):
            res_.append((D @ Ms[m] @ D.conj().T - sum(R[n, m] * Ms[n] for n in range(3))).ravel())
    rows.append(np.concatenate(res_))
Mx = np.array(rows).T; Mx = np.vstack([Mx.real, Mx.imag])
u_, s_, vt_ = np.linalg.svd(Mx, full_matrices=True)
null = vt_[np.sum(s_ > 1e-9):]
ncov = len(null)
def build(v):
    Ms = [np.zeros((10, 10), complex) for _ in range(3)]
    for b_idx, cval in enumerate(v):
        mu, b = divmod(b_idx, len(h10)); Ms[mu] = Ms[mu] + cval * h10[b]
    return Ms
PE = np.diag([1, 1, 0, 0, 0.]); PT = np.diag([0, 0, 1, 1, 1.])
blind = [[np.kron(P, SIG[m]) for m in range(3)] for P in (PE, PT)]
proj = null.T @ null
def coords(Ms):
    v = []
    for mu in range(3):
        for b in h10:
            v.append(np.real(np.trace(b.conj().T @ Ms[mu])) / np.real(np.trace(b.conj().T @ b)))
    return np.array(v)
blind_in = all(np.linalg.norm(proj @ coords(Bm) - coords(Bm)) < 1e-8 for Bm in blind)
check("S5b cubic-covariant k-linear terms on (E+T1) x spin: space dim > 2; the 2 colour/weak-blind cones lie in it",
      ncov > 2 and blind_in, f"covariant dim {ncov}, blind 2, tuned {ncov - 2}")
vgen = null.T @ rng.normal(size=ncov)
Mgen = build(vgen)
M0s = np.kron(M0, I2)
int_basis = [np.kron(e, I2) for e in gl5] + [np.kron(1j * e, I2) for e in gl5]
def int_commutant(mats):
    rows = [np.concatenate([(b @ M - M @ b).ravel() for M in mats]) for b in int_basis]
    Mx = np.array(rows).T; Mx = np.vstack([Mx.real, Mx.imag])
    s = np.linalg.svd(Mx, compute_uv=False)
    return (int(np.sum(s < 1e-8 * s[0])) + max(0, len(int_basis) - len(s))) // 2
cb = int_commutant([M0s] + [0.7 * blind[0][m] + 1.3 * blind[1][m] for m in range(3)])
cg = int_commutant([M0s] + Mgen)
offEt = max(np.abs(np.kron(PE, I2) @ M @ np.kron(PT, I2)).max() for M in Mgen)
check("S5c internal commutant: blind cone 13 = u(2)+u(3); generic covariant cone 1 = U(1)_X only", cb == 13 and cg == 1,
      f"blind {cb}, generic {cg}, E-T1 mixing {offEt:.2f}")
check("S5d the generic covariant cone mixes E with T1 (N_E, N_T, hence Y, not conserved)", offEt > 1e-3)
cq = commutant_dim([s for s in SIG], [np.eye(2)[:, [i]] @ np.eye(2)[[j], :] for i in range(2) for j in range(2)])
check("S6 qubit-spinor reading of the 2: the cone sigma.k leaves commutant dim 1 on it (the 2 is spin, not weak)",
      cq == 1)

# S7 6th (A1) mode: Spin(12) even half = 16 + 16bar of the 5-mode Spin(10)
G6 = majoranas(6)
c6 = [(G6[2 * j] + 1j * G6[2 * j + 1]) / 2 for j in range(6)]
N6 = np.real(np.diag(sum(c.conj().T @ c for c in c6)))
Gam5 = 1j * np.linalg.multi_dot(G6[:10])
ev6 = np.where(np.round(N6) % 2 == 0)[0]
g5 = np.round(np.linalg.eigvalsh(Gam5[np.ix_(ev6, ev6)]), 6)
check("S7 keeping the A1 half-link mode: Spin(12) half-spinor 32 = 16 + 16bar (a mirror family comes along)",
      list(g5).count(1.0) == 16 and list(g5).count(-1.0) == 16)

# S8 Lee-sphere tiling of Z^3 by 7-site stars (centres x+2y+3z = 0 mod 7)
L = 7
cent = [(x, y, z) for x in range(L) for y in range(L) for z in range(L) if (x + 2 * y + 3 * z) % L == 0]
cov = np.zeros((L, L, L), int)
for (x, y, z) in cent:
    for dv in [(0, 0, 0)] + [tuple(int(t) for t in v) for v in dirs6]:
        cov[(x + dv[0]) % L, (y + dv[1]) % L, (z + dv[2]) % L] += 1
cs = set(cent)
stabR = [i for i, R in enumerate(O24) if all(tuple(int(t) % L for t in R @ np.array(p)) in cs for p in cent)]
invS = inv_space([D5[i] for i in stabR], herm5)
MS = sum(rng.normal() * b for b in invS)
gapS = np.min(np.diff(np.linalg.eigvalsh(MS)))
check("S8 7-site stars tile Z^3 exactly (Golomb-Welch); the tiling keeps only a C3 of the 24 rotations, whose generic"
      " invariant tick on the 5 is non-degenerate (no protected 2+3)",
      cov.min() == 1 and cov.max() == 1 and len(stabR) == 3 and gapS > 1e-3,
      f"{len(cent)} stars on 7^3, stabiliser {len(stabR)}, invariants {len(invS)}, min gap {gapS:.3f}")

print(f"elapsed {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
