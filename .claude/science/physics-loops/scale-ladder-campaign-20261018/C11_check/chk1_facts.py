"""C11 check, part (a): model facts F1-F5 by an independent route (characters + group-averaging projectors)."""
import itertools, collections
from c11model import *

NP = NF = 0
def rep(ok, msg):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(("[PASS] " if ok else "[FAIL] ") + msg, flush=True)

# F1 little group
for nm, k0 in KP.items():
    fixed = [np.allclose(wrapk(g['M'].T @ k0 + np.pi * g['lam'] - k0), 0, atol=1e-12) for g in GRP]
    rep(all(fixed), f"F1 {nm}: all 24 proper rotations fix it under k -> R^T k + pi lam (mod 2pi)")
# inversion check (informational): k -> -k maps k* -> -k*, so O_h does not fix k*
print("   note: -k* != k* mod 2pi:", not np.allclose(wrapk(2 * KST), 0))

# F2 group {+-U_R}
els = [s * g['U'] for g in GRP for s in (1, -1)]
def key(X): return tuple(np.round(X.flatten().real, 6)) + tuple(np.round(X.flatten().imag, 6))
S_ = {key(X) for X in els}
closed = all(key(X @ Y) in S_ for X in els for Y in els)
rep(len(S_) == 48 and closed, f"F2: {{+-U_R}} is a closed group of order {len(S_)}")
def order(X):
    Y = X.copy()
    for n in range(1, 50):
        if np.allclose(Y, np.eye(12)): return n
        Y = Y @ X
def orders(group): return dict(sorted(collections.Counter(order(X) for X in group).items()))
oa = orders(els); print("   element orders {+-U_R}:", oa)
# GL(2,3) order statistics: 1:1, 2:13, 3:8, 4:6, 6:8, 8:12 ; 2O: 1:1,2:1,3:8,4:18,6:8,8:12 ; S4xZ2: 1:1,2:19,3:8,4:12,6:8
GL23 = {1: 1, 2: 13, 3: 8, 4: 6, 6: 8, 8: 12}; BO = {1: 1, 2: 1, 3: 8, 4: 18, 6: 8, 8: 12}
rep(oa == GL23, "F2: order statistics of {+-U_R} equal those of GL(2,3) (13 involutions); not 2O (1), not S4xZ2 (19), "
    "not the fourth extension (7 involutions)")
# check GL(2,3) concretely: build GL(2,3) and compare order statistics
gl = [np.array(m).reshape(2, 2) for m in itertools.product(range(3), repeat=4) if round(np.linalg.det(np.array(m).reshape(2, 2))) % 3 != 0]
def ordmod(A):
    B = A.copy() % 3
    for n in range(1, 50):
        if np.array_equal(B, np.eye(2, dtype=int)): return n
        B = (B @ A) % 3
print("   GL(2,3) built over F3: orders", dict(sorted(collections.Counter(ordmod(A) for A in gl).items())))
rel = [s * (1 if g['chi'] == 1 else 1j) * g['U'] for g in GRP for s in (1, -1)]
ob = orders(rel); print("   element orders after relift g -> i g on chi=-1 elements:", ob)
rep(ob == BO, "F2: relifted group has the order statistics of 2O (binary octahedral)")
Srel = {key(X) for X in rel}
rep(len(Srel) == 48 and all(key(X @ Y) in Srel for X in rel for Y in rel), "F2: relifted set is closed (a group of order 48)")
# relift invariance of conjugation, commutant, A2 character relation
ok = all(np.allclose(np.linalg.inv(Up) @ X @ Up, X.conj().T) or True for Up, X in [(np.eye(2), np.eye(2))])
rng = np.random.default_rng(7)
Xr = rng.normal(size=(12, 12))
ok = all(np.allclose((1j * g['U']) @ Xr @ np.linalg.inv(1j * g['U']), g['U'] @ Xr @ g['U'].T) for g in GRP)
rep(ok, "F2: relift leaves every conjugation U X U^-1 unchanged (so covariance, Schur and commutant are unchanged); "
    "NB covariance must be written with U^-1, since (iU)^T != (iU)^-1")

# F3 decomposition
def chi_on(D, lift=None):
    return np.array([np.trace(D.conj().T @ ((1 if lift is None else lift(g)) * g['U']) @ D) for g in GRP])
cP, cM = chi_on(DP), chi_on(DM); cA2 = np.array([g['chi'] for g in GRP]); trR = np.array([np.trace(g['M']) for g in GRP])
c12 = np.array([np.trace(g['U']) for g in GRP])
inv = lambda a, b: np.mean(np.conj(a) * b)
ok = all(np.allclose(g['U'] @ D, D @ (D.conj().T @ g['U'] @ D)) for g in GRP for D in (DP, DM))
rep(ok, "F3: D+ and D- (H_on=2, Lambda=-+2sqrt2) are U_R-invariant")
rep(abs(inv(cP, cP) - 1) < 1e-12 and abs(inv(cM, cM) - 1) < 1e-12 and abs(inv(cP, cM)) < 1e-12,
    f"F3: D+, D- irreducible and inequivalent  <+,+>={inv(cP,cP).real:.3f} <-,->={inv(cM,cM).real:.3f} |<+,->|={abs(inv(cP,cM)):.1e}")
rep(abs(inv(cP, c12) - 1) < 1e-12 and abs(inv(cM, c12) - 1) < 1e-12, "F3: D+ and D- each occur exactly once in the 12 (character multiplicity)")
cG = c12 - cP - cM
rep(abs(inv(cG, cG) - 4) < 1e-12 and abs(inv(cP, cG)) < 1e-12 and abs(inv(cM, cG)) < 1e-12 and abs(inv(cG / 2, cG / 2) - 1) < 1e-12,
    "F3: 8-dim complement has <chi,chi>=4, no D+- content, chi/2 is an irreducible 4-dim character -> 2 G3/2")
rep(np.allclose(cM, cA2 * cP), "F3: chi_{D-}(g) = chi_A2(g) chi_{D+}(g) for all 24 (sign-of-lift independent)")
comm_dim = round(inv(c12, c12).real)
rep(comm_dim == 6, f"F3: commutant dim = <chi12,chi12> = {comm_dim}")
# relift: which doublet is E1/2 (chi(C4) = +sqrt2) is a convention
for nm, lf in (("i", lambda g: 1 if g['chi'] == 1 else 1j), ("-i", lambda g: 1 if g['chi'] == 1 else -1j)):
    c4 = [i for i, g in enumerate(GRP) if np.trace(g['M']) == 1][0]
    print(f"   relift by {nm}: chi_D+(C4) = {chi_on(DP, lf)[c4]:.4f}, chi_D-(C4) = {chi_on(DM, lf)[c4]:.4f}")
rep(np.allclose(chi_on(DM, lambda g: 1 if g['chi'] == 1 else 1j), cA2 * chi_on(DP, lambda g: 1 if g['chi'] == 1 else 1j)),
    "F3: D- = A2 (x) D+ also holds after the relift; E1/2 vs E5/2 naming flips between relift by i and by -i (convention)")

# F4/F5 multiplicities by characters (End(D) = conj(chi) chi, T1 character = tr R)
m_T1_EndP = inv(trR, np.conj(cP) * cP); m_T1_EndM = inv(trR, np.conj(cM) * cM)
m_T1_Hom = inv(trR, np.conj(cP) * cM); m_T2_Hom = inv(cA2 * trR, np.conj(cP) * cM); m_T2_End = inv(cA2 * trR, np.conj(cP) * cP)
m_A1_End = inv(np.ones(24), np.conj(cP) * cP)
print(f"   multiplicities: T1 in End(D+) {m_T1_EndP.real:.3f}, End(D-) {m_T1_EndM.real:.3f}, Hom(D+,D-) {m_T1_Hom.real:.3f}; "
      f"T2 in Hom {m_T2_Hom.real:.3f}, T2 in End(D+) {m_T2_End.real:.3f}; A1 in End(D+) {m_A1_End.real:.3f}")
rep(abs(m_T1_EndP - 1) < 1e-12 and abs(m_T1_EndM - 1) < 1e-12 and abs(m_A1_End - 1) < 1e-12,
    "F4 (characters): End(D_b) = A1 + T1, T1 once")
rep(abs(m_T1_Hom) < 1e-12 and abs(m_T2_Hom - 1) < 1e-12 and abs(m_T2_End) < 1e-12,
    "F5 (characters): Hom(D+,D-) = A2 + T2, no T1; End(D) has no T2")

# F4 frame by group-averaging projector on triples
def proj_triple(Din, Dout, Y, chi=False):
    out = np.zeros_like(Y)
    for g in GRP:
        ro = Dout.conj().T @ g['U'] @ Dout; ri = Din.conj().T @ g['U'] @ Din
        w = g['chi'] if chi else 1
        for i in range(3):
            out[i] += w * ro @ sum(g['M'][i, j] * Y[j] for j in range(3)) @ np.linalg.inv(ri) / 24
    return out
def rank_of_proj(Din, Dout, chi=False):
    basis = []
    for idx in range(12):
        Y = np.zeros((3, 2, 2), complex); Y.flat[idx] = 1; basis.append(proj_triple(Din, Dout, Y, chi).flatten())
    return np.linalg.matrix_rank(np.array(basis), tol=1e-9)
EPS = np.zeros((3, 3, 3))
for p in itertools.permutations(range(3)): EPS[p] = np.linalg.det(np.eye(3)[list(p)])
TAU = {}
for b, D in DOUB.items():
    r = rank_of_proj(D, D)
    Y = proj_triple(D, D, rng.normal(size=(3, 2, 2)) + 1j * rng.normal(size=(3, 2, 2)))
    mu = (Y[0] @ Y[0])[0, 0]; assert np.allclose(Y[0] @ Y[0], mu * np.eye(2))
    T = Y / np.sqrt(mu)
    if np.allclose(T[0] @ T[1], -1j * T[2]): T = -T
    herm = all(np.allclose(T[i], T[i].conj().T) for i in range(3))
    alg = all(np.allclose(T[i] @ T[j], (i == j) * np.eye(2) + 1j * sum(EPS[i, j, k] * T[k] for k in range(3))) for i in range(3) for j in range(3))
    trl = max(abs(np.trace(T[i])) for i in range(3))
    # -T is also a Hermitian T1 triple with T^2 = 1 but has the opposite epsilon sign
    altm = all(np.allclose((-T[i]) @ (-T[j]), (i == j) * np.eye(2) - 1j * sum(EPS[i, j, k] * (-T[k]) for k in range(3))) for i in range(3) for j in range(3))
    rep(r == 1 and herm and alg and trl < 1e-12 and altm,
        f"F4 D{'+' if b > 0 else '-'}: projector rank {r}; normalised triple Hermitian, traceless, tau_i tau_j = d_ij + i eps tau_k; "
        f"-tau satisfies the -i eps relation, so the eps relation fixes the sign uniquely")
    TAU[b] = T
rep(rank_of_proj(DP, DM) == 0 and rank_of_proj(DP, DM, chi=True) == 1 and rank_of_proj(DP, DP, chi=True) == 0,
    "F5 (projector ranks): T1 in Hom(D+,D-) 0, T2 in Hom(D+,D-) 1, T2 in End(D+) 0")
np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tau_frames.npy'), np.array([TAU[1], TAU[-1]]))
print(f"TOTAL PASS={NP} FAIL={NF}")
