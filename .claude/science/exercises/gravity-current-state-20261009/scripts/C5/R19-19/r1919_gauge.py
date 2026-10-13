"""R19-19 (a)/(c): which of the six graviton-cone rows can a LOCAL, Bianchi-exact (transverse) vacuum response carry?
Space: local symmetric response kernels Pi^{(mu nu)(rho sigma)}(p), p = (omega, q), polynomial of degree <= 2,
invariant under O_h (spatial signed permutations, time fixed) x T (time index sign flip), P,T-even.
Degree 0: A^{mu nu rho sigma}; degree 2: B^{mu nu rho sigma alpha beta} p_alpha p_beta.
Rows (R9-9 / R17-4 conventions; e:e = 2):
  mu_E, mu_T2   = e.A.e  for e = diag(1,-1,0) and xy+yx (q -> 0 static TT shear rows)
  Xi(n,e)       = d/d(omega^2) + d/d(q^2) of e.Pi(omega, q n).e   (LI form ~ (omega^2 - q^2) gives 0)
  for (n,e) = (z,Eg), (z,T2g), (110, face1), (110, face2).
Gauge conditions (linearized diffeo, delta h_{mu nu} = p_mu xi_nu + p_nu xi_mu):
  FULL:     p_mu Pi^{mu nu, rho sigma}(p) = 0 for all nu, as a polynomial identity in p;
  SPATIAL:  only for nu spatial (xi_0 = 0);
  NONE:     no condition.
Also checks that the linearized Einstein-Hilbert kernel and the eps.eps.t family lie in the FULL-transverse space."""
import numpy as np, itertools
rng = np.random.default_rng(7)
D = 4
eta = np.diag([-1., 1, 1, 1])
# group O_h x T as 4x4 matrices
G = []
for p in itertools.permutations(range(3)):
    for s in itertools.product([1, -1], repeat=3):
        for tsgn in (1, -1):
            M = np.zeros((4, 4)); M[0, 0] = tsgn
            for i in range(3): M[1+i, 1+p[i]] = s[i]
            G.append(M)

def act(R, T):
    for ax in range(T.ndim):
        T = np.moveaxis(np.tensordot(R, T, axes=([1], [ax])), 0, ax)
    return T

def symB(T):
    T = (T + T.transpose(1,0,2,3,4,5))/2; T = (T + T.transpose(0,1,3,2,4,5))/2
    T = (T + T.transpose(2,3,0,1,4,5))/2; T = (T + T.transpose(0,1,2,3,5,4))/2
    return T
def symA(T):
    T = (T + T.transpose(1,0,2,3))/2; T = (T + T.transpose(0,1,3,2))/2
    T = (T + T.transpose(2,3,0,1))/2
    return T
def reyn(T, sym):
    T = sym(T); out = np.zeros_like(T)
    for R in G: out += act(R, T)
    return out/len(G)

def basis(shape, sym, nsamp):
    Ts = [reyn(rng.normal(size=shape), sym).ravel() for _ in range(nsamp)]
    M = np.array(Ts); u, s, vt = np.linalg.svd(M, full_matrices=False)
    r = int((s > 1e-10*s[0]).sum())
    return vt[:r].reshape((r,)+shape), s
Bb, sB = basis((D,)*6, symB, 60)
Ab, sA = basis((D,)*4, symA, 30)
print('dim invariant degree-2 kernels B:', len(Bb), ' (60 samples; next sv ratio %.1e)' % (sB[len(Bb)]/sB[0] if len(Bb) < len(sB) else 0))
print('dim invariant degree-0 kernels A:', len(Ab))

# polarizations (spatial 3x3 embedded in 4x4)
r2 = np.sqrt(2)
def emb(e3):
    e = np.zeros((4, 4)); e[1:, 1:] = e3; return e
Eg = emb(np.diag([1., -1, 0])); T2 = np.zeros((3, 3)); T2[0, 1] = T2[1, 0] = 1; T2 = emb(T2)
a = np.array([1, -1, 0])/r2; bz = np.array([0, 0, 1.])
F1 = emb(np.outer(a, a)-np.outer(bz, bz)); F2 = emb(np.outer(a, bz)+np.outer(bz, a))
z4 = np.array([0, 0, 0, 1.]); fd4 = np.array([0, 1, 1, 0])/r2; t4 = np.array([1., 0, 0, 0])
NAMED = [('Eg', z4, Eg), ('T2g', z4, T2), ('face1', fd4, F1), ('face2', fd4, F2)]
for nm, n, e in NAMED:
    assert abs(e @ n).max() < 1e-12 and abs(np.trace(e)) < 1e-12 and abs((e*e).sum()-2) < 1e-12

def xi_rows(B):
    out = []
    for nm, n, e in NAMED:
        ct = np.einsum('ij,kl,ijklab,a,b->', e, e, B, t4, t4)   # d/d omega^2
        cs = np.einsum('ij,kl,ijklab,a,b->', e, e, B, n, n)     # d/d q^2
        out.append(ct + cs)
    return np.array(out)
def mu_rows(A):
    return np.array([np.einsum('ij,kl,ijkl->', Eg, Eg, A), np.einsum('ij,kl,ijkl->', T2, T2, A)])

def ward_B(B, nus):
    """coefficients of the cubic polynomial p_mu B^{mu nu rho sigma alpha beta} p_alpha p_beta, nu restricted."""
    C = B.copy()   # p_mu (lower) contracts the upper first index directly
    C = (C + C.transpose(4,1,2,3,0,5) + C.transpose(5,1,2,3,4,0))/3   # symmetrize mu, alpha, beta
    C = (C + C.transpose(0,1,2,3,5,4))/2
    C = (C + C.transpose(4,1,2,3,0,5) + C.transpose(5,1,2,3,4,0))/3
    return C[:, nus].ravel()
def ward_A(A, nus):
    C = A.copy()
    return C[:, nus].ravel()

def nullspace(M, tol=1e-9):
    if M.shape[0] == 0: return np.eye(M.shape[1])
    u, s, vt = np.linalg.svd(M)
    r = int((s > tol*max(s[0], 1e-300)).sum())
    return vt[r:].T

for label, nus in [('NONE', []), ('SPATIAL (xi_0 = 0)', [1, 2, 3]), ('FULL (4D linearized diffeo)', [0, 1, 2, 3])]:
    WB = np.array([ward_B(B, nus) for B in Bb]).T if nus else np.zeros((0, len(Bb)))
    WA = np.array([ward_A(A, nus) for A in Ab]).T if nus else np.zeros((0, len(Ab)))
    NB = nullspace(WB); NA = nullspace(WA)
    XB = np.array([xi_rows(B) for B in Bb]).T @ NB if NB.size else np.zeros((4, 0))
    MA = np.array([mu_rows(A) for A in Ab]).T @ NA if NA.size else np.zeros((2, 0))
    rows = np.zeros((6, XB.shape[1] + MA.shape[1]))
    rows[:4, :XB.shape[1]] = XB; rows[4:, XB.shape[1]:] = MA
    rk = np.linalg.matrix_rank(rows, tol=1e-9) if rows.size else 0
    print('\n[%s] dim B allowed = %d, dim A allowed = %d, rank of map to rows (Xi_Eg, Xi_T2g, face1, face2, mu_E, mu_T2) = %d'
          % (label, NB.shape[1], NA.shape[1], rk))
    if rows.size:
        u, s, vt = np.linalg.svd(rows)
        img = u[:, :rk]
        print('  image basis (columns, rows ordered Xi_Eg, Xi_T2g, face1, face2, mu_E, mu_T2):')
        # present in a readable basis: reduced row echelon of img^T
        Q = img.T.copy()
        for i in range(Q.shape[0]):
            j = np.argmax(np.abs(Q[i]) > 1e-9); Q[i] /= Q[i, j]
            for k in range(Q.shape[0]):
                if k != i: Q[k] -= Q[k, j]*Q[i]
        print(np.round(Q, 6))

# sanity: linearized EH kernel and eps.eps.t family
eps = np.zeros((4,)*4)
for perm in itertools.permutations(range(4)):
    sgn = np.linalg.det(np.eye(4)[list(perm)])
    eps[perm] = sgn
def epsfam(t):
    K = np.einsum('mrAl,nsBk,lk->mnrsAB', eps, eps, t)
    return symB(K)
etaU = eta  # eta^{-1} = eta
def EH():
    # E^{mu nu rho sigma}(p) for L = 1/2 h E h, coefficients of p_a p_b (upper p via eta)
    B = np.zeros((4,)*6)
    I = np.eye(4)
    for m, n, r, s, A, Bi in itertools.product(range(4), repeat=6):
        pA = etaU[A]; pB = etaU[Bi]   # p^A = eta^{A a} p_a
        val = 0.5*(etaU[m, r]*etaU[n, s] + etaU[m, s]*etaU[n, r])*etaU[A, Bi]
        val -= 0.5*(pA[m]*pB[r]*etaU[n, s] + pA[m]*pB[s]*etaU[n, r] + pA[n]*pB[r]*etaU[m, s] + pA[n]*pB[s]*etaU[m, r])
        val += pA[m]*pB[n]*etaU[r, s] + pA[r]*pB[s]*etaU[m, n]
        val -= etaU[m, n]*etaU[r, s]*etaU[A, Bi]
        B[m, n, r, s, A, Bi] = val
    return symB(B)
Beh = EH()
print('\nEH kernel: |Ward FULL| =', np.abs(ward_B(Beh, [0, 1, 2, 3])).max(),
      ' in invariant span: residual', np.linalg.norm(Beh.ravel() - Bb.reshape(len(Bb), -1).T @ (Bb.reshape(len(Bb), -1) @ Beh.ravel())))
print('EH rows (Xi..., should be 0):', np.round(xi_rows(Beh), 12))
for nm, t in [('t = eta', eta), ('t = diag(1,0,0,0)', np.diag([1., 0, 0, 0])), ('t = diag(0,1,1,1)', np.diag([0., 1, 1, 1]))]:
    K = epsfam(t)
    print('eps.eps.t (%s): |Ward FULL| = %.1e, rows Xi = %s' % (nm, np.abs(ward_B(K, [0, 1, 2, 3])).max(), np.round(xi_rows(K), 10)),
          ' omega^2 coeff on Eg/T2g (z):', np.round([np.einsum('ij,kl,ijklab,a,b->', e, e, K, t4, t4) for e in (Eg, T2)], 10))
# cubic kinetic term sum_a K_aa^2 (allowed by SPATIAL): K_ij ~ omega h_ij at q along axis -> check rows
