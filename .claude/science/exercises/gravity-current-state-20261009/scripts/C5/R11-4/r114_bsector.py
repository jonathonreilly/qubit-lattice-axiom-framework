"""R11-4: d = 3 symmetric stress on the bound-triplet sector B (spin-1 internal space), pole-dipole
coupling to prescribed linear fields.  Checks:
 (0) Lemma KB3 (d = 3 Belinfante division) near-zero step and far formula, random data.
 (1) closed-form box-sector stress (d = 3 generalisation of R9-10 s3.4): symmetry, Hermiticity,
     Ward identities nu = 0, i pointwise in (P, Q) on B, moments H, K, J_T = J.
 (2) von Laue: forward int T^ij = P_i P_j / H on B (zero at rest), any M_b.
 (3) uniqueness of pole-dipole data on B: rank of the homogeneous Ward/J_T system (Christoffel step).
 (4) spin-orbit (geodetic) coefficient c(v) for field (ii) against Gam/(Gam+1) + gamma; GR (2Gam+1)/(Gam+1).
 (5) frame dragging: coupling -int w_i T^{0i} -> -(1/2) curl w . S at rest (ratio 1).
 (6) random Riemann-symmetric improvement Y: Ward kept on B, pole-dipole data unchanged, quadrupole changed.
Convention: T(Q) raises total momentum by Q; on B, T(Q) = e^{iQX/2} tau(Pbar,Q) e^{iQX/2}, X = X_NW;
[H, T^{0nu}(Q)] = Q_j T^{j nu}(Q) (D = Q near 0); moments = -i d/dQ at 0.
"""
import numpy as np, itertools
rng = np.random.default_rng(11)
eps3 = np.zeros((3,3,3))
for a,b,c in itertools.permutations(range(3)):
    eps3[a,b,c] = np.linalg.det(np.eye(3)[[a,b,c]])
S = np.array([-1j*eps3[a] for a in range(3)])          # (S_a)_{bc} = -i eps_abc, spin 1
I3 = np.eye(3)
def pr(*a): print(*a, flush=True)

# ---------------- (0) Lemma KB3 ----------------
pr('(0) Lemma KB3 (d=3 Koszul-Belinfante division)')
worst = 0.0
for trial in range(200):
    Q = rng.normal(size=3); beta = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3))
    alpha = Q @ beta                                   # alpha_m = Q_k beta_km
    w = np.einsum('jim,j,m->i', eps3, Q, alpha)        # target Q_j eps^{jim} alpha_m
    Y = -(np.einsum('jlm,l,im->ji', eps3, Q, beta) + np.einsum('ilm,l,jm->ji', eps3, Q, beta))
    worst = max(worst, np.abs(Q @ Y - w).max(), np.abs(Y - Y.T).max())
pr('  near-zero step: max |Q_j Y^ji - Q_j eps^jim alpha_m|, |Y - Y^T| over 200 random draws = %.2e' % worst)
worst = 0.0
for trial in range(200):
    D = rng.normal(size=3) + 1j*rng.normal(size=3); R = rng.normal(size=3) + 1j*rng.normal(size=3)
    a = D.conj()/np.sum(np.abs(D)**2)
    T = np.outer(R, a) + np.outer(a, R) - (R @ D)*np.outer(a, a)
    worst = max(worst, np.abs(T @ D - R).max(), np.abs(T - T.T).max())
pr('  far formula T = R a^T + a R^T - (R.D) a a^T: max |T.D - R|, |T - T^T| = %.2e' % worst)
# angular moment of the transverse fix -i eps^{jkl} D_k sigma_l (D = Q near 0): J_T change = 2 sigma(0)
sig = rng.normal(size=3)
dJ = np.array([sum(eps3[m,a,b]*(-1j)*(-1j)*eps3[b,a,l]*sig[l] for a in range(3) for b in range(3) for l in range(3)) for m in range(3)])
pr('  transverse fix: J_T change / sigma(0) =', np.round((dJ/sig).real, 12))

# ---------------- closed form on B ----------------
class Bsector:
    def __init__(s, Mb): s.M = Mb
    def h(s, P): return np.sqrt(s.M**2 + P @ P)
    def f(s, P): return 1.0/(s.M + s.h(P))
    def PxS(s, P): return np.einsum('abc,b,cij->aij', eps3, P, S)
    def d(s, P): return s.PxS(P)*s.f(P)                       # energy dipole coefficient (P x S)/(M+H)
    def Sig(s, P):                                            # Belinfante curl coefficient (fixed by J_T = J)
        PS = np.einsum('a,aij->ij', P, S)
        return 0.5*(S - (S*(P @ P) - np.einsum('a,ij->aij', P, PS))*s.f(P)/s.h(P))
    def Delta(s, P, Q):                                       # staircase-symmetrised divided difference, 6 orderings
        out = np.zeros(3)
        for perm in itertools.permutations(range(3)):
            x = P - Q/2
            for j in perm:
                x2 = x.copy(); x2[j] += Q[j]
                if abs(Q[j]) > 1e-6:
                    out[j] += (s.h(x2) - s.h(x))/Q[j]
                else:                                   # tiny step: centred derivative, error O(Q_j^2)
                    mid = 0.5*(x + x2); out[j] += mid[j]/s.h(mid)
                x = x2
        return out/6.0
    def tau(s, P, Q):
        """4x4 array (mu,nu) of 3x3 internal matrices tau^{mu nu}(Pbar=P, Q)."""
        T = np.zeros((4,4,3,3), complex)
        Tc = s.h(P)*I3 + 1j*np.einsum('a,aij->ij', Q, s.d(P))
        Dl = s.Delta(P, Q)
        Sg = s.Sig(P)
        curl = np.einsum('bkl,k,lij->bij', eps3, Q, Sg)         # eps_bkl Q_k Sigma_l
        T[0,0] = Tc
        for b in range(3):
            T[0,b+1] = T[b+1,0] = Tc*Dl[b] - 1j*curl[b]
        for i in range(3):
            for j in range(3):
                T[i+1,j+1] = Tc*Dl[i]*Dl[j] - 1j*(Dl[i]*curl[j] + Dl[j]*curl[i])
        return T
    def omega(s, P, Q): return s.h(P + Q/2) - s.h(P - Q/2)

def fd1(fun, P, hstep=2e-3):
    """-i d/dQ_a fun(P, Q) at Q = 0, 8th-order central differences, avoiding Q components == 0 exactly."""
    c = [4/5, -1/5, 4/105, -1/280]
    out = []
    base = np.zeros(3)
    for a in range(3):
        g = 0
        for n, cn in enumerate(c, 1):
            e = np.zeros(3); e[a] = n*hstep
            g = g + cn*(fun(P, base + e) - fun(P, base - e))
        out.append(-1j*g/hstep)
    return np.array(out)

for Mb in (0.95, 0.85, 0.70):
    B = Bsector(Mb)
    pr('\n==== bound triplet M_b = %.2f (binding fraction %.2f) ====' % (Mb, (1.0 - Mb)/1.0))
    # (1) Ward identities, symmetry, Hermiticity at random (P, Q)
    wW = wS = wH = 0.0
    for trial in range(60):
        P = rng.uniform(-0.35, 0.35, 3); Q = rng.uniform(-0.4, 0.4, 3)
        T = B.tau(P, Q); Tm = B.tau(P, -Q); om = B.omega(P, Q)
        for nu in range(4):
            lhs = om*T[0,nu]; rhs = sum(Q[j]*T[j+1,nu] for j in range(3))
            wW = max(wW, np.abs(lhs - rhs).max())
        wS = max(wS, np.abs(T - T.transpose(1,0,2,3)).max())
        wH = max(wH, np.abs(T - Tm.conj().transpose(0,1,3,2)).max())
    pr('(1) Ward nu=0..3 max |omega tau^{0nu} - Q_j tau^{j nu}| = %.2e; symmetry %.2e; Hermiticity tau(Q)^dag = tau(-Q): %.2e' % (wW, wS, wH))
    for P in (np.zeros(3), np.array([0.21, -0.13, 0.30])):
        h = B.h(P); v = P/h
        t0 = B.tau(P, np.zeros(3))
        m1 = fd1(lambda P_, Q_: B.tau(P_, Q_), P)            # m1[a, mu, nu] = -i d_a tau^{mu nu}
        # zeroth moments
        e00 = np.abs(t0[0,0] - h*I3).max()
        e0i = max(np.abs(t0[0,i+1] - P[i]*I3).max() for i in range(3))
        eij = max(np.abs(t0[i+1,j+1] - P[i]*P[j]/h*I3).max() for i in range(3) for j in range(3))
        # first moments: energy dipole coefficient d, J_T spin part
        ed = np.abs(m1[:,0,0] - B.d(P)).max()
        JT = np.array([sum(eps3[b,a,j]*m1[a,0,j+1] for a in range(3) for j in range(3)) for b in range(3)])
        eJ = np.abs(JT - S).max()
        # predicted momentum-density first moment m^{a,j} = (v_j d_a + v_a d_j)/2 + eps_ajc S_c / 2
        dd = B.d(P)
        mpred = np.array([[0.5*(v[j]*dd[a] + v[a]*dd[j]) + 0.5*np.einsum('c,cij->ij', eps3[a,j], S) for j in range(3)] for a in range(3)])
        em = max(np.abs(m1[a,0,j+1] - mpred[a,j]).max() for a in range(3) for j in range(3))
        # first moment of the spatial-stress trace: predicted (v x S)_a
        nkk = np.array([sum(m1[a,k+1,k+1] for k in range(3)) for a in range(3)])
        vxS = np.einsum('abc,b,cij->aij', eps3, v, S)
        en = np.abs(nkk - vxS).max()
        pr('  P = %s: int T00 - H %.1e | int T0i - P_i %.1e | int Tij - P_iP_j/H %.1e | dipole - (PxS)/(M+H) %.1e | J_T - (spin S) %.1e | m^{a,j} - pred %.1e | n^{a,kk} - (v x S)_a %.1e'
           % (np.round(P, 3), e00, e0i, eij, ed, eJ, em, en))
        if np.allclose(P, 0):
            pr('  (2) von Laue at rest: max |int T^ij| on the triplet = %.1e (any spin state; T^ij forward is c-number zero)' % eij)

    # (4) geodetic coefficient: H_SO = d_a Phi (d_a + gamma n^{a,kk}) ;  compare c(v) S.(gradPhi x v)
    pr('  (4) spin-orbit coefficient c(v) in H_SO = c(v) S.(grad Phi x v), field (ii) at linear order:')
    for pmag in (1e-3, 0.1, 0.3, 0.55):
        P = np.array([0.0, pmag, 0.0]); h = B.h(P); v = P/h; Gam = h/Mb
        m1 = fd1(lambda P_, Q_: B.tau(P_, Q_), P)
        g = np.array([1.0, 0.0, 0.0])                          # grad Phi
        ref = np.einsum('aij,a->ij', S, np.cross(g, v))         # S.(g x v)
        for gam in (1.0, 0.0, 0.5):
            HSO = sum(g[a]*(m1[a,0,0] + gam*sum(m1[a,k+1,k+1] for k in range(3))) for a in range(3))
            c = np.trace(HSO @ ref.conj().T).real/np.trace(ref @ ref.conj().T).real
            res = np.abs(HSO - c*ref).max()
            if gam == 1.0:
                pr('     |P|=%.3f v=%.4f gamma=1: c = %.12f  vs Gam/(Gam+1)+1 = %.12f  [GR (2Gam+1)/(Gam+1) = %.12f]  structure residual %.1e'
                   % (pmag, np.linalg.norm(v), c, Gam/(Gam+1) + 1, (2*Gam+1)/(Gam+1), res))
            else:
                pr('     |P|=%.3f gamma=%.1f: c = %.12f  vs Gam/(Gam+1)+gamma = %.12f' % (pmag, gam, c, Gam/(Gam+1) + gam))
    # (5) frame dragging: w_i = generic linear field w_i = W_ia x_a ; H = -d_a w_i m^{a,i} (spin part), at rest
    P = np.zeros(3); m1 = fd1(lambda P_, Q_: B.tau(P_, Q_), P)
    W = rng.normal(size=(3,3))                                 # w_i = W[i,a] x_a  -> d_a w_i = W[i,a]
    Hgm = -sum(W[i,a]*m1[a,0,i+1] for a in range(3) for i in range(3))
    curlw = np.array([sum(eps3[l,a,i]*W[i,a] for a in range(3) for i in range(3)) for l in range(3)])
    ref = -0.5*np.einsum('l,lij->ij', curlw, S)
    pr('  (5) frame dragging at rest: max |H_gm - (-1/2 curl w . S)| = %.1e (ratio %.12f)'
       % (np.abs(Hgm - ref).max(), np.trace(Hgm @ ref.conj().T).real/np.trace(ref @ ref.conj().T).real))

# ---------------- (3) uniqueness: homogeneous system rank ----------------
pr('\n(3) uniqueness of first moments of T^ij on B (Christoffel step): unknowns dtau1^{a,(ji)} (18), constraints sym_(a,j) dtau1^{a,ji} = 0')
idx = {}
for a in range(3):
    for (j,i) in [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]:
        idx[(a,j,i)] = len(idx)
def var(a,j,i): return idx[(a,) + tuple(sorted((j,i)))]
rows = []
for a in range(3):
    for j in range(a, 3):
        for i in range(3):
            r = np.zeros(18); r[var(a,j,i)] += 1; r[var(j,a,i)] += 1; rows.append(r)
A = np.array(rows)
pr('   rank = %d of 18 unknowns (%d constraints): nullspace dim = %d' % (np.linalg.matrix_rank(A), len(rows), 18 - np.linalg.matrix_rank(A)))

# ---------------- (6) random Riemann-symmetric improvement ----------------
pr('\n(6) random improvement dT^{mu nu} = d_rho d_sigma Y^{rho mu sigma nu} (Kulkarni-Nomizu Y, internal Hermitian ops, Y(-Q) = Y(Q)^dag)')
def KN(Bm, Cm):
    return (np.einsum('rs,mn->rmsn', Bm, Cm) + np.einsum('rs,mn->rmsn', Cm, Bm)
            - np.einsum('rn,ms->rmsn', Bm, Cm) - np.einsum('rn,ms->rmsn', Cm, Bm))
def herm(n=3):
    A = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n)); return 0.5*(A + A.conj().T)
terms = []
for k in range(3):
    Bm = rng.normal(size=(4,4)); Bm = Bm + Bm.T; Cm = rng.normal(size=(4,4)); Cm = Cm + Cm.T
    terms.append((KN(Bm, Cm), herm(), [herm() for _ in range(3)]))
Ytest = terms[0][0]
sym_err = max(np.abs(Ytest + Ytest.transpose(1,0,2,3)).max(), np.abs(Ytest + Ytest.transpose(0,1,3,2)).max(),
              np.abs(Ytest - Ytest.transpose(2,3,0,1)).max(),
              np.abs(Ytest + Ytest.transpose(0,2,3,1) + Ytest.transpose(0,3,1,2)).max())
pr('   Riemann symmetries + first Bianchi of the KN tensor: %.1e' % sym_err)
def Yop(Q):
    Y = np.zeros((4,4,4,4,3,3), complex)
    for (Kt, O0, O1) in terms:
        O = O0 + 1j*sum(Q[a]*O1[a] for a in range(3))
        Y += np.einsum('rmsn,ij->rmsnij', Kt, O)
    return Y
class Improved(Bsector):
    def tau(s, P, Q):
        T = Bsector.tau(s, P, Q)
        kap = np.array([1j*s.omega(P, Q), -1j*Q[0], -1j*Q[1], -1j*Q[2]])
        return T + np.einsum('r,s,rmsnij->mnij', kap, kap, Yop(Q))
for Mb in (0.85,):
    B0 = Bsector(Mb); B1 = Improved(Mb)
    wW = wS = wH = 0.0
    for trial in range(40):
        P = rng.uniform(-0.3, 0.3, 3); Q = rng.uniform(-0.4, 0.4, 3)
        T = B1.tau(P, Q); Tm = B1.tau(P, -Q); om = B1.omega(P, Q)
        for nu in range(4):
            wW = max(wW, np.abs(om*T[0,nu] - sum(Q[j]*T[j+1,nu] for j in range(3))).max())
        wS = max(wS, np.abs(T - T.transpose(1,0,2,3)).max())
        wH = max(wH, np.abs(T - Tm.conj().transpose(0,1,3,2)).max())
    pr('   improved stress: Ward %.1e, symmetry %.1e, Hermiticity %.1e' % (wW, wS, wH))
    for P in (np.zeros(3), np.array([0.2, -0.1, 0.25])):
        m0 = fd1(lambda P_, Q_: B0.tau(P_, Q_), P); m1 = fd1(lambda P_, Q_: B1.tau(P_, Q_), P)
        z0 = B0.tau(P, np.zeros(3)); z1 = B1.tau(P, np.zeros(3))
        # second moment of T00: -d_a d_b tau^{00} at 0 (fiber coefficient of the energy quadrupole)
        hq = 2e-2
        def sec(Bx, a, b):
            ea = np.zeros(3); ea[a] = hq; eb = np.zeros(3); eb[b] = hq; base = np.zeros(3)
            return -(Bx.tau(P, base+ea+eb)[0,0] - Bx.tau(P, base+ea-eb)[0,0] - Bx.tau(P, base-ea+eb)[0,0] + Bx.tau(P, base-ea-eb)[0,0])/(4*hq*hq)
        dq = max(np.abs(sec(B1,a,b) - sec(B0,a,b)).max() for a in range(3) for b in range(3))
        pr('   P = %s: max change in zeroth moments %.1e, in all first moments %.1e (FD floor), in the T00 second-moment coefficient %.3f'
           % (np.round(P,2), np.abs(z1 - z0).max(), np.abs(m1 - m0).max(), dq))
