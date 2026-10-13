"""R19-23 (a)/(c): static potential between conserved sources (vDVZ-type test) for the solid kernel (degree-0 Ward
violation only = the shear rows), and coupling of the extra branches to conserved matter sources (class R)."""
import numpy as np, sys
sys.path.insert(0, '.')
from kernels import *
exec(open('r1923_modes.py').read().split("# ---- Part 1")[0].split("def solid")[0])   # reuse explicit A tensors
def solid(lb, mE, mT): return lb*A_tr + mE*A_E + mT*A_T
import scipy.linalg as sl

def conserved_basis(omega, qvec):
    p = np.concatenate([[omega], qvec])
    # T^{mu nu} upper; coupling h_{mu nu} T^{mu nu} = vec(h).vec(T); conservation p_mu T^{mu nu} = 0
    M = np.einsum('i,aij->ja', p, EB)          # M[nu, a] = p_i E_a^{i nu}
    Cb = nullspace(M)
    assert Cb.shape[1] == 6
    return Cb
def amp(Q, T1, T2):
    x = np.linalg.lstsq(Q, T2, rcond=None)[0]
    return T1 @ x
Tm = vec(np.diag([1., 0, 0, 0]))                       # static mass
for qdir, nm in [(z3, 'z'), (fd3, '110')]:
    # light-like source moving along a direction perpendicular to q: T^{00} = T^{ee} = T^{0e} = 1
    e = np.cross(qdir, [0.3, 0.5, 0.8]); e /= np.linalg.norm(e); e4 = np.r_[0, e]; t = t4
    Tl = vec(np.outer(t, t) + np.outer(e4, e4) + np.outer(t, e4) + np.outer(e4, t))
    print('\n=== static amplitudes, q along %s; GR comparator uses the pseudo-inverse (T orthogonal to gauge nulls) ===' % nm)
    for q in (1e-1, 1e-2):
        QGR = Qmat(0*Ab[0], 0*Bb[0], 0., q*qdir, 0.)
        print('  q=%.0e GR: U_mm*q^2 = %.6f  U_ml*q^2 = %.6f  (ratio U_ml/U_mm = %.6f; GR expects 2)' % (q, amp(QGR, Tm, Tm)*q*q, amp(QGR, Tm, Tl)*q*q, amp(QGR, Tm, Tl)/amp(QGR, Tm, Tm)))
    for (lb, mE, mT) in [(0.7, 1.0, 0.6), (0.0, 1.0, 1.0), (0.7, -1.0, 0.6), (-0.4, 0.3, 2.0)]:
        A = solid(lb, mE, mT)
        for eps in (1e-4, 1e-6, 1e-8):
            for q in (1e-1, 1e-2, 1e-3):
                Q = Qmat(A, 0*Bb[0], 0., q*qdir, eps); QGR = Qmat(0*Ab[0], 0*Bb[0], 0., q*qdir, 0.)
                rmm = amp(Q, Tm, Tm)/amp(QGR, Tm, Tm); rml = amp(Q, Tm, Tl)/amp(QGR, Tm, Tl)
                print('  solid(lb=%.1f,muE=%.1f,muT=%.1f) eps=%.0e q=%.0e (m^2/q^2 ~ %.0e): U_mm/GR = %.6f, U_ml/GR = %.6f'
                      % (lb, mE, mT, eps, q, eps/q**2, rmm, rml))

# coupling of the extra branches to conserved sources (class R sample, as in r1923_modes Part 3)
print('\n=== coupling of each branch to conserved sources: max over the 6-dim conserved T space of |T.v|^2/|v.dQ.v| ===')
src = open('r1923_modes.py').read()
exec(src.split("# ---- Part 1")[0].split("import numpy")[0])
rngc = np.random.default_rng(23)
for _ in range(len(Ab) + len(Bb)): pass
cons = [B[0, :, :, :, 0, 0].ravel() for B in Bb]
NB_R = nullspace(np.array(cons).T)
def omega2_block(B): return mat(np.einsum('mnrsab,a,b->mnrs', B, t4, t4))
found = 0
while found < 2:
    B = combB(NB_R @ rngc.normal(size=NB_R.shape[1]))
    if np.linalg.eigvalsh(omega2_block(B)[4:, 4:]).max() < -1e-3:
        found += 1
        A = solid(0.7, 1.0, 0.6)
        for eps, q in [(1e-5, 1e-2), (1e-7, 1e-2), (1e-5, 1e-3)]:
            qvec = q*fd3
            Q0, Q1, Q2 = Qparts(A, B, qvec, eps)
            n = 10; I = np.eye(n); Z = np.zeros((n, n))
            w, V = sl.eig(np.block([[Z, I], [-Q0, -Q1]]), np.block([[I, Z], [Z, Q2]]))
            ok = np.isfinite(w) & (np.abs(w) < 10) & (np.abs(w) > 1e-7*q) & ((np.real(w) > 0) | ((np.abs(np.real(w)) < 1e-12) & (np.imag(w) > 0)))
            print('  sample %d eps=%.0e q=%.0e:' % (found, eps, q))
            for wi, vi in sorted(zip(w[ok], V[:, ok].T), key=lambda t: abs(t[0])):
                v = vi[:n]; v = v/np.linalg.norm(v)
                dQ = Q1 + 2*wi*Q2
                Nn = np.conj(v) @ dQ @ v
                Cb = conserved_basis(wi, qvec) if abs(np.imag(wi)) < 1e-12 else conserved_basis(np.real(wi), qvec)
                c = np.linalg.norm(Cb.T @ v)**2/abs(Nn)
                print('     w^2/q^2 = %-28s coupling = %.3e   overlap with TT(face1,face2) = %.3f' %
                      (np.round(wi*wi/q**2, 4), c, np.linalg.norm([np.conj(v) @ vec(F1)/r2, np.conj(v) @ vec(F2)/r2])))

# ---- check of the branch couplings: gauge content of each eigenvector, and the static amplitude for class R ----
print('\n=== class R + solid: eigenvector gauge content, |T.v| (max over unit conserved T), norm, and static amplitude vs GR ===')
rngc = np.random.default_rng(23)
found = 0
while found < 2:
    B = combB(NB_R @ rngc.normal(size=NB_R.shape[1]))
    if np.linalg.eigvalsh(omega2_block(B)[4:, 4:]).max() < -1e-3:
        found += 1
        A = solid(0.7, 1.0, 0.6)
        for eps in (1e-5, 1e-7, 1e-9):
            q = 1e-2; qvec = q*fd3
            Q0, Q1, Q2 = Qparts(A, B, qvec, eps)
            n = 10; I = np.eye(n); Z = np.zeros((n, n))
            w, V = sl.eig(np.block([[Z, I], [-Q0, -Q1]]), np.block([[I, Z], [Z, Q2]]))
            ok = np.isfinite(w) & (np.abs(w) < 10) & (np.abs(w) > 1e-7*q) & (np.abs(np.imag(w)) < 1e-9) & (np.real(w) > 0)
            print('  sample %d eps=%.0e q=%.0e:' % (found, eps, q))
            for wi, vi in sorted(zip(np.real(w[ok]), np.real(V[:, ok].T)), key=lambda t: abs(t[0])):
                v = vi[:n]; v = v/np.linalg.norm(v)
                Gd = gauge_dirs(wi, qvec); Pg = Gd @ np.linalg.pinv(Gd)
                gfrac = np.linalg.norm(Pg @ v)
                Cb = conserved_basis(wi, qvec); Tv = np.linalg.norm(Cb.T @ v)
                Nn = v @ (Q1 + 2*wi*Q2) @ v
                print('     w^2/q^2 = %10.4f  |P_gauge v| = %.6f  max|T.v| = %.3e  norm v.dQ.v = %+.3e  residue ~ |T.v|^2/|norm| = %.3e'
                      % (wi*wi/q**2, gfrac, Tv, Nn, Tv**2/abs(Nn)))
            for qq in (1e-1, 1e-2, 1e-3):
                Qs = Qmat(A, B, 0., qq*fd3, eps); QGR = Qmat(0*Ab[0], 0*Bb[0], 0., qq*fd3, 0.)
                e = np.cross(fd3, [0.3, 0.5, 0.8]); e /= np.linalg.norm(e); e4 = np.r_[0, e]
                Tl = vec(np.outer(t4, t4) + np.outer(e4, e4) + np.outer(t4, e4) + np.outer(e4, t4))
                print('     static q=%.0e: U_mm/GR = %.6f  U_ml/GR = %.6f' % (qq, amp(Qs, Tm, Tm)/amp(QGR, Tm, Tm), amp(Qs, Tm, Tl)/amp(QGR, Tm, Tl)))

# which Goldstone is each real extra branch? decomposition of the eigenvector over gauge directions xi_0 / xi_n / xi_a / xi_b
print('\n=== class R + solid, q along 110: gauge-direction content of the real extra branches (eps = 1e-7, q = 1e-2) ===')
rngc = np.random.default_rng(23); found = 0
nv3 = fd3; av3 = a3; bv3 = b3
while found < 3:
    B = combB(NB_R @ rngc.normal(size=NB_R.shape[1]))
    if np.linalg.eigvalsh(omega2_block(B)[4:, 4:]).max() < -1e-3:
        found += 1; A = solid(0.7, 1.0, 0.6); eps = 1e-7; q = 1e-2; qvec = q*fd3
        Q0, Q1, Q2 = Qparts(A, B, qvec, eps)
        n = 10; I = np.eye(n); Z = np.zeros((n, n))
        w, V = sl.eig(np.block([[Z, I], [-Q0, -Q1]]), np.block([[I, Z], [Z, Q2]]))
        ok = np.isfinite(w) & (np.abs(w) < 0.3) & (np.abs(w) > 1e-7*q)
        for wi, vi in sorted(zip(w[ok], V[:, ok].T), key=lambda t: abs(t[0])):
            if np.real(wi) < -1e-14 or (abs(np.real(wi)) <= 1e-14 and np.imag(wi) < 0): continue
            v = vi[:n]; v = v/np.linalg.norm(v)
            pv = np.r_[wi, qvec]
            cols = []
            for xi in (np.r_[1., 0, 0, 0], np.r_[0, nv3], np.r_[0, av3], np.r_[0, bv3]):
                cols.append(vec(np.outer(pv, xi) + np.outer(xi, pv)))
            Gm = np.array(cols).T
            c = np.linalg.lstsq(Gm, v, rcond=None)[0]; resid = np.linalg.norm(Gm @ c - v)
            c = np.abs(c)/max(np.abs(c).max(), 1e-300)
            print('  sample %d: w^2/q^2 = %-26s |xi_0|,|xi_n|,|xi_a|,|xi_b| (rel) = %s  non-gauge residual = %.1e  TT overlap = %.3f'
                  % (found, np.round(wi*wi/q**2, 4), np.round(c, 3), resid, np.linalg.norm([np.conj(v) @ vec(F1)/r2, np.conj(v) @ vec(F2)/r2])))
