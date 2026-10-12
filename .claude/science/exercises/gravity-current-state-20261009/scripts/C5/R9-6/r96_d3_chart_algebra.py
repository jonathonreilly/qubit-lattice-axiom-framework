"""R9-6, script 1 (d = 3): the BT box law with the p-wave TRIPLET and the spin term (P x S)/(M + H).

Conventions (R7-1 measured, R8-1 d = 2): X = i d/dk, [X_a, P_b] = i delta_ab, J = X x P (+ S),
  [K_a, P_b] = i delta_ab H, [K_a, H] = i P_a, [K_a, K_b] = -i eps_abc J_c, [J_a, K_b] = i eps_abc K_c,
  [J_a, P_b] = i eps_abc P_c, [J_a, J_b] = i eps_abc J_c.
Generators in the canonical chart (P, q):  H = sqrt(M^2 + P^2),  J = X_NW x P + S,  S = -i q x grad_q,
  K = (1/2){H, X_NW} + alpha (P x S)/(M + H),  alpha = +1 (proved in the report),
  M = M0 + V, V = lam sum_{a=1..3} |g_a><g_a|, g_a = q_a b(|q|^2)  (odd => fermionic; rotation scalar => [V, S] = 0).
(a) chart: FD Jacobian of (P,q) -> (k1,k2) in d = 3 and round trip; then the FREE lattice box generators
    K0 = sum_i (1/2){eps_i, X_i}, J0 = sum_i X_i x k_i pulled into the chart vs the BT free generators (M = M0),
    pointwise with 8th-order FD on 12 random points in 6D.  Comparators: printed sign, no spin term, alpha = -1.
(b) the full interacting algebra, ALL 45 commutators of {H, P_a, J_a, K_a}, on a spectral P-grid (NP^3) x
    (Gauss-Legendre radial x Y_lm, l <= 2) q-basis.  Comparators: (c1) printed sign, (c2) spin term dropped,
    (c3) alpha = -1, (c4) single rank-one g_z channel, (c5) the d = 2 doublet (g_x, g_y) carried into d = 3.
"""
import numpy as np, time, sys, itertools
from r81_common import sstep

m, KAP, MU_B = 0.5, 0.8, 0.85
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
LC = np.zeros((3, 3, 3))
for a, b, c in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    LC[a, b, c] = 1; LC[a, c, b] = -1

# ---------------- (a) chart identity in d = 3 ----------------
def to_k(P, q):
    w = np.sqrt(m*m + (q**2).sum(-1)); M0 = 2*w; H0 = np.sqrt(M0**2 + (P**2).sum(-1))
    Pq = (P*q).sum(-1)
    k1 = q + P*(Pq/(M0*(H0 + M0)) + w/M0)[..., None]
    return k1, P - k1
def to_Pq(k1, k2):
    e1 = np.sqrt(m*m + (k1**2).sum(-1)); e2 = np.sqrt(m*m + (k2**2).sum(-1))
    P = k1 + k2; H0 = e1 + e2; M0 = np.sqrt(H0**2 - (P**2).sum(-1))
    Pk = (P*k1).sum(-1)
    q = k1 + P*(Pk/(M0*(H0 + M0)) - e1/M0)[..., None]
    return P, q
def jac_formula(P, q):
    k1, k2 = to_k(P, q)
    e1 = np.sqrt(m*m + (k1**2).sum(-1)); e2 = np.sqrt(m*m + (k2**2).sum(-1))
    w = np.sqrt(m*m + (q**2).sum(-1)); M0 = 2*w; H0 = e1 + e2
    return e1*e2*M0/(w*w*H0)

rng = np.random.default_rng(96)
pts = [(rng.uniform(-0.5, 0.5, 3), rng.uniform(-0.6, 0.6, 3)) for _ in range(12)]
errJ = errRT = 0
for P, q in pts:
    h = 1e-6; Jm = np.zeros((6, 6)); z = np.concatenate([P, q])
    for j in range(6):
        dz = np.zeros(6); dz[j] = h
        kp = np.concatenate(to_k((z+dz)[:3], (z+dz)[3:])); km = np.concatenate(to_k((z-dz)[:3], (z-dz)[3:]))
        Jm[:, j] = (kp - km)/(2*h)
    errJ = max(errJ, abs(abs(np.linalg.det(Jm)) - jac_formula(P, q))/jac_formula(P, q))
    Pb, qb = to_Pq(*to_k(P, q)); errRT = max(errRT, np.abs(Pb - P).max() + np.abs(qb - q).max())
pr('(a) d = 3 chart: |FD Jacobian - e1 e2 M0/(w^2 H0)|/J = %.1e ; round-trip error = %.1e (max over 12 points)' % (errJ, errRT))

def phi(P, q):
    qx, qy, qz = q[..., 0], q[..., 1], q[..., 2]; r2 = qx**2 + qy**2 + qz**2
    Px, Py, Pz = P[..., 0], P[..., 1], P[..., 2]
    return np.exp(-((Px-0.1)**2 + (Py+0.05)**2 + (Pz-0.07)**2)/0.08) * np.exp(-r2/0.3) * \
        (0.7 + (qx + 0.4j*qy - 0.3*qz) + 0.5*(qx**2 - qy**2 + 0.3j*qx*qz + 0.2*qy*qz) + 0.2*Px*qy + 0.15j*Pz*qx
         - 0.1*Py*qz)
def psi_k(k1, k2):
    P, q = to_Pq(k1, k2); return phi(P, q)/np.sqrt(jac_formula(P, q))
c8 = np.array([1/280, -4/105, 1/5, -4/5, 0, 4/5, -1/5, 4/105, -1/280])
def d_dir(f, z, j, h=2e-3):
    acc = 0
    for i, c in enumerate(c8):
        if c == 0: continue
        dz = np.zeros(6); dz[j] = (i-4)*h; acc = acc + c*f(z + dz)
    return acc/h
eps = lambda k: np.sqrt(m*m + (k**2).sum(-1))
fk = lambda z: psi_k(z[:3], z[3:])
fq = lambda z: phi(z[:3], z[3:])
maxrel = {}
for P, q in pts:
    k1, k2 = to_k(P, q); zk = np.concatenate([k1, k2]); zq = np.concatenate([P, q])
    sJ = np.sqrt(jac_formula(P, q))
    dk = np.array([d_dir(fk, zk, j) for j in range(6)])   # d/dk1 (3), d/dk2 (3)
    dq = np.array([d_dir(fq, zq, j) for j in range(6)])   # d/dP (3), d/dq (3)
    p0 = fk(zk); f0 = fq(zq); e1, e2 = eps(k1), eps(k2)
    K0 = [1j*(e1*dk[a] + 0.5*(k1[a]/e1)*p0 + e2*dk[3+a] + 0.5*(k2[a]/e2)*p0) for a in range(3)]
    # J0_a = sum_i i eps_abc k_ic d_{k_i b}
    J0 = [1j*sum(LC[a, b, c]*(k1[c]*dk[b] + k2[c]*dk[3+b]) for b in range(3) for c in range(3)) for a in range(3)]
    w = np.sqrt(m*m + q @ q); M0 = 2*w; H0 = np.sqrt(M0**2 + P @ P)
    # S_a = -i eps_abc q_b d_{q_c}
    S = [-1j*sum(LC[a, b, c]*q[b]*dq[3+c] for b in range(3) for c in range(3)) for a in range(3)]
    XN = [1j*dq[a] for a in range(3)]
    XxP = [sum(LC[a, b, c]*XN[b]*P[c] for b in range(3) for c in range(3)) for a in range(3)]
    Jbt = [XxP[a] + S[a] for a in range(3)]
    PxS = [sum(LC[a, b, c]*P[b]*S[c] for b in range(3) for c in range(3)) for a in range(3)]
    base = [H0*XN[a] + 0.5j*(P[a]/H0)*f0 for a in range(3)]
    Kbt = [base[a] + PxS[a]/(M0 + H0) for a in range(3)]
    Kbad = [-base[a] + PxS[a]/(M0 + H0) for a in range(3)]
    Knos = base
    Kam = [base[a] - PxS[a]/(M0 + H0) for a in range(3)]
    scale = abs(f0) + sum(abs(Kbt[a]) for a in range(3))
    rows = [('K0_%s vs BT' % 'xyz'[a], K0[a]*sJ, Kbt[a]) for a in range(3)] + \
           [('J0_%s vs BT' % 'xyz'[a], J0[a]*sJ, Jbt[a]) for a in range(3)] + \
           [('H0 vs BT', (e1+e2)*p0*sJ, H0*f0)] + \
           [('(c1) K0 vs printed sign', max(abs(K0[a]*sJ - Kbad[a]) for a in range(3)), 0),
            ('(c2) K0 vs no spin term', max(abs(K0[a]*sJ - Knos[a]) for a in range(3)), 0),
            ('(c3) K0 vs alpha = -1', max(abs(K0[a]*sJ - Kam[a]) for a in range(3)), 0)]
    for lab, A, B in rows:
        maxrel[lab] = max(maxrel.get(lab, 0), abs(A - B)/scale)
for lab, v in maxrel.items():
    pr('(a) %-26s max relative difference over 12 points = %.2e' % (lab, v))

# ---------------- (b) the interacting algebra, all 45 commutators ----------------
NP = int(sys.argv[1]) if len(sys.argv) > 1 else 28
Wn = 1.1
Pg = np.linspace(-Wn, Wn, NP, endpoint=False); dP = Pg[1] - Pg[0]
kP = 2*np.pi*np.fft.fftfreq(NP, d=dP)
PX, PY, PZ = np.meshgrid(Pg, Pg, Pg, indexing='ij'); P2 = PX**2 + PY**2 + PZ**2
PC = [PX, PY, PZ]
Nr, Q, LMAX = 12, 1.2, 2
xr, wr = np.polynomial.legendre.leggauss(Nr); r = 0.5*Q*(xr + 1); wr = 0.5*Q*wr
M0r = 2*np.sqrt(m*m + r**2)
bq = sstep(1.0 - r**2/KAP**2)/KAP
hvec = np.sqrt(wr*r**2)*r*bq*np.sqrt(4*np.pi/3)     # l = 1 radial vector of sum_a |g_a><g_a|
lms = [(l, mm) for l in range(LMAX+1) for mm in range(-l, l+1)]; NLM = len(lms)
Sp = np.zeros((NLM, NLM)); Sz = np.zeros((NLM, NLM))
for j, (l, mm) in enumerate(lms):
    Sz[j, j] = mm
    if mm < l: Sp[lms.index((l, mm+1)), j] = np.sqrt(l*(l+1) - mm*(mm+1))
Sm = Sp.T
Smat = [0.5*(Sp + Sm), (Sp - Sm)/(2j), Sz.astype(complex)]
for a, b in [(0, 1), (1, 2), (2, 0)]:
    c = 3 - a - b
    assert np.abs(Smat[a] @ Smat[b] - Smat[b] @ Smat[a] - 1j*Smat[c]).max() < 1e-14
s1 = np.sum(hvec**2/(M0r - MU_B)); LAM = -1.0/s1   # bound state at exactly MU_B on this grid
pr('(b) NP = %d on [-%.1f, %.1f)^3, radial GL Nr = %d on [0, %.1f], Y_lm l <= %d; lam_eff = %.6f (M_b = %.2f)'
   % (NP, Wn, Wn, Nr, Q, LMAX, LAM, MU_B))

def build(chan):
    """per-(l,m) eigen-decomposition of M; chan = which (l=1, m) channels carry V."""
    U = np.zeros((NLM, Nr, Nr)); mu = np.zeros((NLM, Nr))
    for j, (l, mm) in enumerate(lms):
        Mm = np.diag(M0r).copy()
        if l == 1 and mm in chan: Mm = Mm + LAM*np.outer(hvec, hvec)
        mu[j], U[j] = np.linalg.eigh(Mm)
    return U, mu

def make_ops(chan, sign=+1, alpha=+1.0, spin=True):
    U, mu = build(chan)
    def fM(v, fun):
        c = np.einsum('xyzjr,jrs->xyzjs', v, U)
        c = c*fun(mu[None, None, None], P2[..., None, None])
        return np.einsum('xyzjs,jrs->xyzjr', c, U)
    Hop = lambda v: fM(v, lambda mu_, p2: np.sqrt(mu_**2 + p2))
    Fop = lambda v: fM(v, lambda mu_, p2: 1.0/(mu_ + np.sqrt(mu_**2 + p2)))
    Sop = lambda v, a: np.einsum('xyzjr,kj->xyzkr', v, Smat[a])
    def Xop(v, a):
        sh = [1, 1, 1, 1, 1]; sh[a] = NP
        return 1j*np.fft.ifft(1j*kP.reshape(sh)*np.fft.fft(v, axis=a), axis=a)
    Pop = lambda v, a: PC[a][..., None, None]*v
    def Jop(v, a):
        acc = Sop(v, a)
        for b in range(3):
            for c in range(3):
                if LC[a, b, c] != 0: acc = acc + LC[a, b, c]*Xop(Pop(v, c), b)
        return acc
    def Kop(v, a):
        base = sign*0.5*(Hop(Xop(v, a)) + Xop(Hop(v), a))
        if not spin: return base
        Fv = Fop(v); acc = base
        for b in range(3):
            for c in range(3):
                if LC[a, b, c] != 0:
                    sp = 0.5*(Sop(Fv, c) + Fop(Sop(v, c)))
                    acc = acc + alpha*LC[a, b, c]*Pop(sp, b)
        return acc
    gens = [('H', Hop)] + [('P%s' % 'xyz'[a], (lambda v, a=a: Pop(v, a))) for a in range(3)] + \
           [('J%s' % 'xyz'[a], (lambda v, a=a: Jop(v, a))) for a in range(3)] + \
           [('K%s' % 'xyz'[a], (lambda v, a=a: Kop(v, a))) for a in range(3)]
    return gens, U, mu, Sop, fM

def expected(A, B, G):
    """[A, B] as a dict {generator: coefficient}."""
    t = lambda n: (n[0], 'xyz'.index(n[1]) if len(n) > 1 else None)
    (a, ia), (b, ib) = t(A), t(B)
    e = {}
    def add(name, coef): e[name] = e.get(name, 0) + coef
    if a == 'H':
        if b == 'K': add('P' + 'xyz'[ib], -1j)
        return e
    if a == 'P':
        if b == 'J':
            for c in range(3):
                if LC[ia, ib, c]: add('P' + 'xyz'[c], 1j*LC[ia, ib, c])
        if b == 'K' and ia == ib: add('H', -1j)
        return e
    if a == 'J':
        for c in range(3):
            if LC[ia, ib, c] and b in 'JKP': add(b + 'xyz'[c], 1j*LC[ia, ib, c])
        return e
    if a == 'K':
        if b == 'K':
            for c in range(3):
                if LC[ia, ib, c]: add('J' + 'xyz'[c], -1j*LC[ia, ib, c])
        return e
    return e

def algebra(chan, sign=+1, alpha=1.0, spin=True, label=''):
    t0 = time.time()
    gens, U, mu, Sop, fM = make_ops(chan, sign, alpha, spin)
    # packet: two terms with different P profiles; bound triplet + scattering, l = 0, 1, 2
    j10 = lms.index((1, 0)); j11 = lms.index((1, 1)); j1m = lms.index((1, -1))
    bound = U[j10][:, np.argmin(mu[j10])]
    chi1 = np.zeros((NLM, Nr), complex)
    chi1[j10] += bound; chi1[j11] += 0.5j*U[j11][:, np.argmin(mu[j11])]; chi1[j1m] += 0.3*U[j1m][:, np.argmin(mu[j1m])]
    rad = np.sqrt(wr*r**2)*np.exp(-r**2/(2*0.25**2))
    chi1[lms.index((0, 0))] += 0.6*rad; chi1[lms.index((2, 1))] += (0.4+0.2j)*rad*r/0.25
    chi2 = np.zeros((NLM, Nr), complex)
    chi2[lms.index((2, -2))] += 0.5*rad*r/0.25; chi2[j11] += 0.7*rad*r/0.25; chi2[lms.index((0, 0))] += 0.3j*rad
    s = np.sqrt(1.0/(2*np.pi*NP/(2*Wn)))   # s^2 = D/(2 k_Nyq), D = 1: balances P-edge decay and spectral aliasing
    A1 = np.exp(-((PX-0.08)**2 + (PY+0.05)**2 + (PZ-0.04)**2)/(4*s*s))
    A2 = np.exp(-((PX+0.06)**2 + (PY-0.03)**2 + (PZ+0.05)**2)/(4*s*s))
    v = A1[..., None, None]*chi1 + A2[..., None, None]*chi2
    v = v/np.linalg.norm(v)
    names = [g[0] for g in gens]; G = dict(gens)
    Gv = {n: G[n](v) for n in names}
    n = np.linalg.norm
    res = {}
    for A, B in itertools.combinations(names, 2):
        ABv = G[A](Gv[B]); BAv = G[B](Gv[A])
        e = expected(A, B, G)
        rhs = sum(cf*Gv[nm] for nm, cf in e.items()) if e else 0*v
        scale = n(rhs) if e else max(n(ABv), n(BAv))
        res['[%s,%s]' % (A, B)] = n(ABv - BAv - rhs)/scale
        del ABv, BAv
    SMres = max(n(Sop(fM(v, lambda mu_, p2: mu_ + 0*p2), a) - fM(Sop(v, a), lambda mu_, p2: mu_ + 0*p2))/n(v)
                for a in range(3))
    worst = sorted(res.items(), key=lambda kv: -kv[1])
    pr('(b) %s   [time %.0fs]' % (label, time.time() - t0))
    pr('    M_min = %.10f; max over 45 = %.1e (%s); median = %.1e; [S,M] = %.1e'
       % (mu.min(), worst[0][1], worst[0][0], np.median(list(res.values())), SMres))
    return res, worst

R, W = algebra({-1, 0, 1}, +1, 1.0, True, 'REPAIRED d = 3: p-wave triplet, K = (1/2){H,X} + (P x S)/(M+H)')
pr('    all 45: ' + '  '.join('%s %.1e' % kv for kv in R.items()))
ONLY_REPAIRED = len(sys.argv) > 2
for args, lab in ([] if ONLY_REPAIRED else [(({-1, 0, 1}, -1, 1.0, True), '(c1) R7-1 printed sign: -(1/2){H,X} + (P x S)/(M+H)'),
                  (({-1, 0, 1}, +1, 1.0, False), '(c2) spin term dropped'),
                  (({-1, 0, 1}, +1, -1.0, True), '(c3) alpha = -1: (1/2){H,X} - (P x S)/(M+H)'),
                  (({0}, +1, 1.0, True), '(c4) single rank-one g_z channel (not rotation invariant)'),
                  (({-1, 1}, +1, 1.0, True), '(c5) d = 2 doublet (g_x, g_y) carried into d = 3')]):
    Rc, Wc = algebra(*args, label=lab)
    pr('    failing (> 1e-6): ' + '  '.join('%s %.1e' % kv for kv in Wc if kv[1] > 1e-6))
with open(__file__.replace('.py', '_NP%d%s.out' % (NP, '_repaired' if ONLY_REPAIRED else '')), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
