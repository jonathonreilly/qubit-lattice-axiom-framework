"""R19-23 (a)-(c): the full quadratic action s*K_EH - eps*Pi in unitary gauge (no gauge fixing needed when Pi
breaks the Ward identity). Exact quadratic eigenvalue problem Q(omega) = Q0 + omega Q1 + omega^2 Q2 (degree <= 2):
all propagating branches, their eps- and q-scaling, norm signs (ghost test), and the face1 pole versus its row."""
import numpy as np, sys, scipy.linalg as sl
sys.path.insert(0, '.')
from kernels import *
rng3 = np.random.default_rng(23)

def rawA(entries):
    A = np.zeros((4,)*4)
    for idx, v in entries: A[idx] += v
    return symA(A)
sp = [1, 2, 3]
A_h00 = rawA([((0,0,0,0), 1.)])
A_h00tr = rawA([((0,0,i,i), 1.) for i in sp])
A_tr = rawA([((i,i,j,j), 1.) for i in sp for j in sp])
A_E = rawA([((i,i,j,j), (1. if i == j else 0.) - 1/3) for i in sp for j in sp])/2     # mu_E row = 1
A_T = rawA([((i,j,i,j), 1.) for i in sp for j in sp if i != j])/2                       # mu_T2 row = 1
A_h0i = rawA([((0,i,0,i), 1.) for i in sp])
Aflat = Ab.reshape(len(Ab), -1).T
for nm, A in [('h00^2', A_h00), ('h00 trh', A_h00tr), ('(trh)^2', A_tr), ('Eg', A_E), ('T2g', A_T), ('h0i^2', A_h0i)]:
    res = np.linalg.norm(A.ravel() - Aflat @ np.linalg.lstsq(Aflat, A.ravel(), rcond=None)[0])
    print('explicit degree-0 tensor %-8s in invariant span: residual %.1e; rows %s' % (nm, res, np.round(rows(A, 0*Bb[0]), 6)))
def solid(lb, mE, mT): return lb*A_tr + mE*A_E + mT*A_T

def residual_gauge(A, B, qvec, eps):
    """which gauge parameters (xi_0; xi_i) leave Q(omega) invariant for all omega (checked at 3 omegas)"""
    inv0 = invs = True
    for w in (0.37, -0.81, 1.3):
        Q = Qmat(A, B, w, qvec, eps); g = gauge_dirs(w, qvec); sc = np.abs(Q).max()
        inv0 &= np.abs(Q @ g[:, 0]).max() < 1e-11*sc
        invs &= np.abs(Q @ g[:, 1:]).max() < 1e-11*sc
    return inv0, invs
def qep_roots(A, B, qvec, eps):
    Q0, Q1, Q2 = Qparts(A, B, qvec, eps)
    inv0, invs = residual_gauge(A, B, qvec, eps)
    keep = list(range(10))
    if inv0: keep.remove(0)                      # gauge-fix xi_0: h00 = 0 (omega != 0)
    if invs: keep = [k for k in keep if k not in (1, 2, 3)]   # gauge-fix xi_i: h0i = 0
    Q0, Q1, Q2 = [M[np.ix_(keep, keep)] for M in (Q0, Q1, Q2)]
    n = Q0.shape[0]; I = np.eye(n); Z = np.zeros((n, n))
    L = np.block([[Z, I], [-Q0, -Q1]]); R = np.block([[I, Z], [Z, Q2]])
    w, V = sl.eig(L, R)
    fin = np.isfinite(w) & (np.abs(w) < 1e8)
    out = []
    for wi, vi in zip(w[fin], V[:, fin].T):
        if abs(wi) < 1e-7*np.linalg.norm(qvec): continue    # residual-gauge / constraint roots at omega = 0
        x = vi[:n]; x = x/np.linalg.norm(x)
        dQ = Q1 + 2*wi*Q2
        nrm = np.real(np.conj(x) @ dQ @ x)
        out.append((wi, nrm, x))
    return out, (Q0, Q1, Q2)

def classify(A, B, qdir, label, eps_list=(1e-3, 1e-4, 1e-5), q_list=(1e-2, 3e-3)):
    print('\n=== %s ===' % label)
    print('  rows (Xi_Eg, Xi_T2g, face1, face2, mu_E, mu_T2) of Pi:', np.round(rows(A, B), 5))
    for eps in eps_list:
        for q in q_list:
            out, (Q0, Q1, Q2) = qep_roots(A, B, q*qdir, eps)
            pos = [(w, nr, x) for (w, nr, x) in out if np.real(w) > 1e-14 or (abs(np.real(w)) <= 1e-14 and np.imag(w) > 0)]
            pos.sort(key=lambda t: abs(t[0]))
            desc = []
            for w, nr, x in pos:
                w2 = w*w
                tag = 'real' if abs(np.imag(w)) < 1e-9*max(abs(w), 1e-30) else 'COMPLEX'
                desc.append('w^2/q^2=%s %s norm%s' % (np.format_float_scientific(np.real(w2)/q**2, 4) if tag == 'real'
                            else '(%.3e%+.3ei)' % (np.real(w2)/q**2, np.imag(w2)/q**2), tag, '+' if nr > 0 else '-'))
            inv0, invs = residual_gauge(A, B, q*qdir, eps)
            print('  eps=%.0e q=%.0e: residual gauge xi0=%s xi_i=%s; rank Q2 = %d, #finite nonzero roots (w>0 or Im>0) = %d' % (eps, q, inv0, invs, np.linalg.matrix_rank(Q2, tol=1e-12*max(1, np.abs(Q2).max())), len(pos)))
            for d in desc: print('      ', d)

# ---- Part 1: face1 physical pole versus its row (degree-2 kernels only, A = 0) ----
print('\n#### Part 1: face1 pole (A1 block) vs row; q along (110); first order in eps ####')
def face1_pole(A, B, q, eps):
    out, _ = qep_roots(A, B, q*fd3, eps)
    u = vec(F1)/np.sqrt(2)
    cand = [(w, x) for (w, nr, x) in out if abs(np.imag(w)) < 1e-12 and np.real(w) > 0]
    # TT-like root: largest overlap with u, near omega = q
    best = max(cand, key=lambda t: abs(np.conj(t[1]) @ u) - 10*abs(np.real(t[0])/q - 1))
    return np.real(best[0]), abs(np.conj(best[1]) @ u)
def schur_face1(A, B, q):
    w = q; p = np.r_[w, q*fd3]
    Pi = mat(kernel(A, B, p)); u = vec(F1)/np.sqrt(2)
    Gd = gauge_dirs(w, q*fd3)
    # A1 gauge directions: xi along t and along n
    Gn = np.column_stack([Gd[:, 0], Gd[:, 1:] @ fd3])
    P11 = u @ Pi @ u; P1G = u @ Pi @ Gn; PGG = Gn.T @ Pi @ Gn
    return 2*(P11 - P1G @ np.linalg.solve(PGG, P1G)), 2*P11
# check that the null space of K_EH(omega = q) in the A1 block is exactly {TT face1, 2 gauge dirs}
q = 0.01; p = np.r_[q, q*fd3]; K = s_EH*mat(kernel(0*Ab[0], Beh, p))
sv = np.linalg.svd(K, compute_uv=False)
print('K_EH(omega=q, q along 110): singular values', np.format_float_scientific(sv[-6], 3), '...', [np.format_float_scientific(x, 2) for x in sv[-5:]])
print('  (expected null dimension: TT face1 + TT face2 + 4 gauge = 6)')
for trial in range(6):
    B = combB(rng3.normal(size=len(Bb))); A = 0*Ab[0]
    r = rows(A, B)
    for eps in (1e-6, 1e-7):
        q = 1e-2
        w, ov = face1_pole(A, B, q, eps)
        xi_phys = (w*w - q*q)/(eps*q*q)
        sch, diag = schur_face1(A, B, q)
        xi_sch = sch/(q*q)/2*2   # Pi_ee convention e:e = 2 -> 2*u.Pi.u
        print('  trial %d eps=%.0e: pole Xi_face1(phys)=%+.6f  Schur=%+.6f  row face1=%+.6f  (3Eg+T2g)/4=%+.6f  overlap=%.4f'
              % (trial, eps, xi_phys, sch/(q*q), r[2], (3*r[0]+r[1])/4, ov))
# same with Ward-satisfying FULL B plus a pure SPATIAL-allowed B: physical face1 should equal the row when no gauge mixing
print('\n  control: B in the SPATIAL-Ward-allowed subspace (8-dim; A = 0): the A1 gauge dir xi_n has no kinetic term,')
for trial in range(3):
    B = combB(NB_sp @ rng3.normal(size=NB_sp.shape[1])); A = 0*Ab[0]; r = rows(A, B)
    q = 1e-2; eps = 1e-7
    try:
        w, ov = face1_pole(A, B, q, eps)
        print('   trial %d: pole Xi_face1=%+.6f row face1=%+.6f (3Eg+T2g)/4=%+.6f' % (trial, (w*w-q*q)/(eps*q*q), r[2], (3*r[0]+r[1])/4))
    except Exception as ex:
        print('   trial %d: pencil singular or no isolated root (%s); row face1=%+.6f (3Eg+T2g)/4=%+.6f' % (trial, type(ex).__name__, r[2], (3*r[0]+r[1])/4))

# ---- Part 2: mode counting ----
print('\n#### Part 2: propagating branches of s*K_EH - eps*Pi (unitary gauge), q along (110) unless stated ####')
qd = fd3
classify(solid(0.7, 1.0, 0.6), 0*Bb[0], qd, 'S1 solid: degree-0 spatial elastic tensor only (lb=0.7, mu_E=1, mu_T2=0.6), B=0')
classify(solid(0.7, 1.0, 0.6), combB(NB_full @ np.array([0.8, -0.5])), qd, 'S2 solid + Ward-satisfying degree-2 (FULL)')
Bgen = combB(rng3.normal(size=len(Bb)))
classify(0*Ab[0], Bgen, qd, 'S3 generic degree-2 (Ward-violating), A=0')
classify(solid(0.7, 1.0, 0.6), Bgen, qd, 'S4 solid + generic degree-2')
classify(combA(rng3.normal(size=len(Ab))), Bgen, qd, 'S5 generic degree-0 + generic degree-2')
classify(0.9*A_h00, combB(NB_sp @ rng3.normal(size=NB_sp.shape[1])), qd, 'S6 SPATIAL-Ward kernel (projectable-like): h00^2 mass + spatially gauge-invariant degree-2')

# ---- realistic class R (suggested from W1 + vacuum translation invariance): at q = 0, T^{0nu} are conserved charges that
# annihilate (or fix) the vacuum, so Pi^{0nu, rho sigma}(omega, q=0) has no omega dependence: B^{0 nu rho sigma, 0 0} = 0.
# The tadpole-subtracted degree-0 part is the spatial elastic tensor (solid). Spectral positivity: the omega^2 coefficient
# of Pi on spatial components is negative semidefinite (R9-9 Theorem T step 1: beta < 0).
print('\n#### Part 3: class R (momentum-conserving vacuum; spectral-positive) ####')
cons = []
for B in Bb:
    C = B[0, :, :, :, 0, 0]
    cons.append(C.ravel())
NB_R = nullspace(np.array(cons).T)
print('dim of degree-2 kernels with B^{0nu rho sigma,00} = 0:', NB_R.shape[1], ' (of 26)')
def omega2_block(B):
    M = mat(np.einsum('mnrsab,a,b->mnrs', B, t4, t4)); return M
def sample_R(sign_ok=True, tries=2000):
    for _ in range(tries):
        B = combB(NB_R @ rng3.normal(size=NB_R.shape[1]))
        W = omega2_block(B); ev = np.linalg.eigvalsh(W[4:, 4:])      # spatial-spatial (indices 4..9 are h11..h33)
        if (not sign_ok) or ev.max() < -1e-3: return B
    return None
for i in range(3):
    B = sample_R()
    if B is None: print('no spectral-positive sample found'); break
    for (lb, mE, mT) in [(0.7, 1.0, 0.6), (0.7, -1.0, 0.6)]:
        classify(solid(lb, mE, mT), B, fd3, 'S7.%d R-class B + solid(lb=%.1f, mu_E=%.1f, mu_T2=%.1f)' % (i, lb, mE, mT), eps_list=(1e-4, 1e-5), q_list=(1e-2, 3e-3))
