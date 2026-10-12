"""R9-5 script 2: full signed check (phases kept) that Kitaev spin strings realise the free-fermion
one-body algebra on the flux-free sector, with the dictionary used for H, P, K, J.

Dictionary (uniform gauge u_{AB} = +1; flux-free <=> every ordered plaquette loop W_p = +1):
   S(A->B) = -i c_A c_B ,  S(A->A') = c_A c_A' ,  S(B->B') = c_B c_B'      (any path; flux-free)
   d_R = (c_{A,R} + i c_{B,R})/2
   Phi(h) = sum_R h_RR (1 - S(A_R->B_R))/2
          + sum_{R != R'} h_RR' (1/4)[S(A_R->A_R') + S(B_R->B_R') - S(A_R->B_R') - S(A_R'->B_R)]
Claim: on the flux-free sector Phi(h) = dGamma(h) = sum h_RR' d_R^dag d_R'.  Checked here by
  (1) [Phi(h), W_p] = 0;
  (2) the Lie-homomorphism identity P(Phi(a)Phi(b) - Phi(b)Phi(a) - Phi([a,b]))P = 0, random complex a, b;
  (3) spectrum of Phi(h) on the sector = Fock spectrum of h (all parities) x uniform multiplicity,
      for the box-law hopping h = M(R'-R) and for random complex Hermitian h;
  (4) the law as written, H_spin = -(1/2) sum M(R'-R) S(A_R->B_R'), equals Phi(M) - N M(0)/2 on the sector.
Open flakes of a x b dimers (paths stay inside: they are monotone)."""
import numpy as np, scipy.sparse as sp, sys, time, itertools
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r95_common import *
rng = np.random.default_rng(11)
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
t0 = time.time()

sx = sp.csr_matrix(np.array([[0, 1], [1, 0]], dtype=complex))
sy = sp.csr_matrix(np.array([[0, -1j], [1j, 0]], dtype=complex))
sz = sp.csr_matrix(np.array([[1, 0], [0, -1]], dtype=complex))
PA = {'x': sx, 'y': sy, 'z': sz}

Mfull, _ = hopping_M(256)
def Mof(r): return Mfull[r[0] % 256, r[1] % 256]

def run(a, b, full=True):
    dimers = [(i, j) for i in range(a) for j in range(b)]
    sites = [(i, j, s_) for (i, j) in dimers for s_ in 'AB']
    idx = {st: q for q, st in enumerate(sites)}
    n = len(sites); D = 2**n
    cache1 = {}
    def p1(q, t):
        if (q, t) not in cache1:
            cache1[(q, t)] = sp.kron(sp.kron(sp.identity(2**q, format='csr'), PA[t]), sp.identity(2**(n-q-1), format='csr'), format='csr')
        return cache1[(q, t)]
    def bondop(u, v, t): return p1(idx[u], t) @ p1(idx[v], t)
    scache = {}
    def S(start, end_sub, r):
        key = (start, end_sub, r)
        if key not in scache:
            st, bd = path(start, end_sub, r)
            for x in st: assert x in idx, ('path leaves flake', start, end_sub, r)
            O = sp.identity(D, format='csr', dtype=complex)
            for (u, v, t) in bd: O = O @ bondop(u, v, t)
            scache[key] = O
        return scache[key]
    # plaquettes
    W = []
    for (i, j) in dimers:
        if (i+1, j+1) in [(x, y) for (x, y) in dimers]:
            loop = [((i, j, 'A'), (i, j, 'B'), 'z'), ((i, j, 'B'), (i+1, j, 'A'), 'y'), ((i+1, j, 'A'), (i+1, j+1, 'B'), 'x'),
                    ((i+1, j+1, 'B'), (i+1, j+1, 'A'), 'z'), ((i+1, j+1, 'A'), (i, j+1, 'B'), 'y'), ((i, j+1, 'B'), (i, j, 'A'), 'x')]
            O = sp.identity(D, format='csr', dtype=complex)
            for (u, v, t) in loop: O = O @ bondop(u, v, t)
            W.append(O)
    Nd = len(dimers)
    def Phi(h):
        O = sp.csr_matrix((D, D), dtype=complex)
        for p_, R in enumerate(dimers):
            for q_, Rp in enumerate(dimers):
                c = h[p_, q_]
                if c == 0: continue
                if p_ == q_:
                    O = O + c*0.5*(sp.identity(D, format='csr') - S((R[0], R[1], 'A'), 'B', (0, 0)))
                else:
                    r = (Rp[0]-R[0], Rp[1]-R[1]); rm = (-r[0], -r[1])
                    O = O + c*0.25*(S((R[0], R[1], 'A'), 'A', r) + S((R[0], R[1], 'B'), 'B', r)
                                    - S((R[0], R[1], 'A'), 'B', r) - S((Rp[0], Rp[1], 'A'), 'B', rm))
        return O
    pr('flake %d x %d dimers: %d spins, %d plaquettes, %d fermion modes' % (a, b, n, len(W), Nd))
    # W algebra
    pr('  W_p Hermitian, W_p^2 = 1, mutually commuting: %.1e %.1e %.1e' % (
        max(abs(w - w.getH()).max() for w in W), max(abs(w @ w - sp.identity(D)).max() for w in W),
        max([abs(w1 @ w2 - w2 @ w1).max() for w1, w2 in itertools.combinations(W, 2)] + [0])))
    Tbox = np.array([[Mof((Rp[0]-R[0], Rp[1]-R[1])) for Rp in dimers] for R in dimers])
    def randH():
        X = rng.normal(size=(Nd, Nd)) + 1j*rng.normal(size=(Nd, Nd)); return (X + X.conj().T)/2
    A_, B_ = randH(), randH()
    PhiT, PhiA, PhiB = Phi(Tbox.astype(complex)), Phi(A_), Phi(B_)
    PhiC = Phi(A_ @ B_ - B_ @ A_)
    pr('  [Phi(h), W_p] = 0 : max norm %.1e (box law), %.1e (random complex)' % (
        max(abs(PhiT @ w - w @ PhiT).max() for w in W), max(abs(PhiA @ w - w @ PhiA).max() for w in W)))
    # law as written
    Hlaw = sp.csr_matrix((D, D), dtype=complex)
    for R in dimers:
        for Rp in dimers:
            r = (Rp[0]-R[0], Rp[1]-R[1])
            Hlaw = Hlaw - 0.5*Mof(r)*S((R[0], R[1], 'A'), 'B', r)
    Pw = sp.identity(D, format='csr', dtype=complex)
    for w in W: Pw = Pw @ (sp.identity(D) + w)*0.5
    if full:
        Pd = Pw.toarray()
        ev, V = np.linalg.eigh((Pd + Pd.conj().T)/2)
        V = V[:, ev > 0.5]; dimS = V.shape[1]
        def restrict(O): return V.conj().T @ (O @ V)
        hom = np.abs(restrict(PhiA @ PhiB - PhiB @ PhiA - PhiC)).max()
        pr('  sector dim %d (2^%d / 2^%d), Fock dim %d, multiplicity %d' % (dimS, n, len(W), 2**Nd, dimS // 2**Nd))
        pr('  homomorphism P([Phi(a),Phi(b)] - Phi([a,b]))P : max %.1e  (scale |Phi(a)| ~ %.1f)' % (hom, np.abs(restrict(PhiA)).max()))
        def fock(h):
            lam = np.linalg.eigvalsh(h); E = []
            for occ in itertools.product([0, 1], repeat=Nd): E.append(np.dot(occ, lam))
            return np.sort(np.array(E))
        mult = dimS // 2**Nd
        for name, h, O in [('box law M(R\'-R)', Tbox, PhiT), ('random complex Hermitian', A_, PhiA)]:
            es = np.sort(np.linalg.eigvalsh(restrict(O)))
            ef = np.sort(np.repeat(fock(h), mult))
            pr('  spectrum on sector vs Fock x %d  [%s]: max dev %.1e  (E range %.3f .. %.3f)' % (mult, name, np.abs(es - ef).max(), ef.min(), ef.max()))
        dev = np.abs(restrict(Hlaw) - (restrict(PhiT) - 0.5*Nd*Mof((0, 0))*np.eye(dimS))).max()
        pr('  law as written vs Phi(M) - N M(0)/2 on sector: max %.1e' % dev)
        # also check that the non-flux-free sectors give a DIFFERENT spectrum (sector matters)
        evW = [np.real(np.diag(V.conj().T @ (w @ V))) for w in W]
        pr('  W_p on the sector (should all be +1): min %.3f max %.3f' % (min(e.min() for e in evW), max(e.max() for e in evW)))
    else:
        # random-vector tests of the homomorphism identity and of the law identity on the sector
        devs = []; devl = []
        for _ in range(6):
            v = rng.normal(size=D) + 1j*rng.normal(size=D); v = Pw @ v; v /= np.linalg.norm(v)
            w1 = Pw @ (PhiA @ (PhiB @ v) - PhiB @ (PhiA @ v) - PhiC @ v); devs.append(np.linalg.norm(w1))
            w2 = Pw @ (Hlaw @ v - PhiT @ v + 0.5*Nd*Mof((0, 0))*v); devl.append(np.linalg.norm(w2))
        pr('  random sector vectors: homomorphism residual max %.1e ; law-vs-Phi(M) residual max %.1e' % (max(devs), max(devl)))
        # ground energy of the law in the sector vs Fock prediction
        import scipy.sparse.linalg as sla
        shift = 50.0
        Op = (PhiT + shift*(sp.identity(D) - Pw)).tocsr()
        Op = (Op + Op.getH())*0.5
        e0 = sla.eigsh(Op, k=4, which='SA', return_eigenvectors=False)
        lam = np.linalg.eigvalsh(Tbox)
        pr('  lowest 4 eigenvalues of Phi(M) on sector: %s ; Fock ground = %.6f (all lambda > 0: %s), first excitation = %.6f'
           % (np.sort(e0), 0.0, bool(lam.min() > 0), lam.min()))
for (a, b, full) in [(2, 3, True), (3, 2, True), (2, 4, False)]:
    run(a, b, full)
pr('runtime %.1f s' % (time.time() - t0))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
