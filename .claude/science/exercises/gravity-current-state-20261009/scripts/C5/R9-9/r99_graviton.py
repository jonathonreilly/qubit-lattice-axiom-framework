"""C5 R9-9 parts A-B: the box graviton (tree level) and its coupling to R8-2's universal box+edge stress.

(A) 09-14 N-type linear graviton on Z^3 with the midpoint symbol qhat_a = 2 sin(q_a/2) replaced by
      d(q) = rho(q) q + (1 - rho(q)) 2 sin(q/2),  rho = 1 on |q| <= c1, 0 on |q| >= c2   (R8-5's photon trick)
    i.e. derivative symbol i d(q_a) in midpoint variables; lattice divergence symbol D(q) = d(q) e^{iq/2} (periodic).
    H_N = (J/2)[E:E - (tr E)^2/2] + (g/2) h:R(h),  R_ij = -eps_iab eps_jcd d_a d_c h_bd,
    vector constraint G_j = d_i E_ij, scalar constraint S = tr R(h).
    Checks: Hermiticity, gauge invariance R(d xi + xi d) = 0, Bianchi d_i R_ij = 0, {G, S} = 0,
            TT spectrum w^2 = J g |d|^2, w = |q| on the graviton box, no zeros of |d| off q = 0.
(B) R8-2 Construction A with D(q) = d(q) e^{iq/2} (instead of R8-2's s_c + i psi) and the continuum kernel
    carried with midpoint phases e^{-i q_j/2} per spatial index; Ward identity, Hermiticity, symmetry, forward values.
"""
import numpy as np, sys, itertools, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r99_profiles import plateau, wrap, profile, B as BOX
T0 = time.time()
C1, C2 = 1.0, 2.5

def dsym(q):
    q = wrap(q); r = plateau(q, C1, C2)
    return r*q + (1-r)*2*np.sin(q/2)

def Dsym(q):
    q = wrap(q)
    return dsym(q)*np.exp(0.5j*q)

print('=== (A) box graviton, tree level ===')
qq = np.linspace(-np.pi, np.pi, 200001)
print('  max |D(pi-) - D(-pi+)| = %.2e  (periodic) ; max |D(q)* + D(-q)| = %.2e'
      % (abs(Dsym(np.pi-1e-9) - Dsym(-np.pi+1e-9)), np.max(np.abs(np.conj(Dsym(qq)) + Dsym(-qq)))))
off = np.abs(qq) >= 0.05
print('  min |d(q)| over 0.05 <= |q| <= pi = %.4f (no zero off q = 0: no graviton doublers) ; d(pi) = %.4f'
      % (np.min(np.abs(dsym(qq[off]))), dsym(np.array([np.pi]))[0]))
inb = np.abs(qq) <= C1
print('  max |d(q) - q| on |q| <= c1 = %.2e' % np.max(np.abs(dsym(qq[inb]) - qq[inb])))
# periodic smoothness at pi: numerical derivatives from both sides
hh = 1e-4
for n in (1, 2):
    dl = (Dsym(np.pi-hh) - Dsym(np.pi-2*hh))/hh if n == 1 else (Dsym(np.pi-hh)-2*Dsym(np.pi-2*hh)+Dsym(np.pi-3*hh))/hh**2
    dr = (Dsym(-np.pi+2*hh) - Dsym(-np.pi+hh))/hh if n == 1 else (Dsym(-np.pi+3*hh)-2*Dsym(-np.pi+2*hh)+Dsym(-np.pi+hh))/hh**2
    print('  derivative order %d of D at the zone face: left %.4f%+.4fi  right %.4f%+.4fi' % (n, dl.real, dl.imag, dr.real, dr.imag))

LC = np.zeros((3, 3, 3))
for (i, j, k), s in [((0,1,2),1), ((1,2,0),1), ((2,0,1),1), ((0,2,1),-1), ((2,1,0),-1), ((1,0,2),-1)]:
    LC[i, j, k] = s
basis = []
for i in range(3):
    e = np.zeros((3, 3)); e[i, i] = 1; basis.append(e)
for i, j in [(0,1),(1,2),(0,2)]:
    e = np.zeros((3, 3)); e[i, j] = e[j, i] = 1/np.sqrt(2); basis.append(e)
basis = np.array(basis)

def Rop(dv, h):
    return -np.einsum('iab,jcd,a,c,bd->ij', LC, LC, dv, dv, h)

rng = np.random.default_rng(99)
worst = dict(herm=0, gauge=0, bianchi=0, GS=0, ttdisp=0, trspec=0)
qs = np.concatenate([rng.uniform(-np.pi, np.pi, (3000, 3)), rng.uniform(-C1, C1, (2000, 3))])
boxdev = 0.0
for q in qs:
    dv = dsym(q)
    Rm = np.array([[np.sum(ea*Rop(dv, eb)) for eb in basis] for ea in basis])
    worst['herm'] = max(worst['herm'], np.max(np.abs(Rm - Rm.T)))
    for j in range(3):
        xi = np.zeros(3); xi[j] = 1
        worst['gauge'] = max(worst['gauge'], np.max(np.abs(Rop(dv, np.outer(dv, xi) + np.outer(xi, dv)))))
    for eb in basis:
        worst['bianchi'] = max(worst['bianchi'], np.max(np.abs(dv @ Rop(dv, eb))))
    # constraints as rows on the 6-dim canonical space (orthonormal basis, pairing E:hdot)
    Gm = np.array([[np.sum(dv[:, None]*ea[:, j][:, None].T.ravel()[:3] if False else dv @ ea[:, j]) for ea in basis] for j in range(3)])
    Sm = np.array([np.trace(Rop(dv, ea)) for ea in basis])
    worst['GS'] = max(worst['GS'], np.max(np.abs(Gm @ Sm)))
    # TT subspace: symmetric, d.e = 0, tr e = 0
    C = np.vstack([Gm, [np.trace(ea) for ea in basis]])         # 4 x 6 (vector-transverse + traceless)
    _, sv, Vt = np.linalg.svd(C)
    TT = Vt[4:]                                                  # 2 x 6 orthonormal
    KE = np.eye(6) - 0.5*np.outer([np.trace(ea) for ea in basis], [np.trace(ea) for ea in basis])
    KE_TT = TT @ KE @ TT.T; Kh_TT = TT @ Rm @ TT.T
    w2 = np.linalg.eigvals(KE_TT @ Kh_TT).real                  # J = g = 1
    worst['ttdisp'] = max(worst['ttdisp'], np.max(np.abs(w2/np.sum(dv**2) - 1)))
    if np.all(np.abs(q) <= C1):
        boxdev = max(boxdev, np.max(np.abs(np.sqrt(np.abs(w2)) - np.linalg.norm(q))))
    # transverse (vector-gauge-fixed) spatial form: eigenvalues |d|^2, |d|^2, -|d|^2 (transverse trace; 09-14: -k^2|tr h_T|^2/2 with tr h = sqrt2 c; removed by S)
    Tr = Vt[3:] if False else np.linalg.svd(Gm)[2][3:]
    ev = np.sort(np.linalg.eigvalsh(Tr @ Rm @ Tr.T))/np.sum(dv**2)
    worst['trspec'] = max(worst['trspec'], np.max(np.abs(ev - np.array([-1.0, 1, 1]))))
for kname, v in worst.items():
    print('  %-8s max residual over %d random q: %.2e' % (kname, len(qs), v))
print('  graviton box |q_a| <= %.1f: max | w_TT - |q| | (J g = 1) = %.2e' % (C1, boxdev))
print('  (herm: R symmetric; gauge: R(d xi + xi d) = 0; bianchi: d_i R_ij = 0; GS: {G, S} = 0;')
print('   ttdisp: TT w^2/(J g |d|^2) - 1; trspec: transverse spatial form eigenvalues = |d|^2 (-1, 1, 1))')

print('\n=== (B) R8-2 Construction A with D(q) = d(q) e^{iq/2} (d = 2) ===')
M = 0.3
CHI_IN, CHI_OUT = 1.6, 1.9
Q_IN, Q_OUT = 0.5, 0.9            # continuum kernel only where |q_i| <= 0.9 < c1, so d = q there

def make_eps(name):
    def f(k):
        u0 = profile(name, k[..., 0])[0]; u1 = profile(name, k[..., 1])[0]
        return np.sqrt(M*M + u0 + u1)
    return f

def divdiff(f, a, j, qj):
    e = np.zeros_like(a); e[..., j] = qj
    num = f(a + e) - f(a)
    den = Dsym(qj)
    small = np.abs(qj) < 1e-7
    h = 1e-6; eh = np.zeros_like(a); eh[..., j] = h
    der = (f(a + eh) - f(a - eh))/(2*h)
    return np.where(small, der, num/np.where(small, 1.0, den))

def Delta(f, k, q):
    e0 = np.zeros_like(k); e0[..., 0] = q[..., 0]
    e1 = np.zeros_like(k); e1[..., 1] = q[..., 1]
    d0 = 0.5*(divdiff(f, k, 0, q[..., 0]) + divdiff(f, k + e1, 0, q[..., 0]))
    d1 = 0.5*(divdiff(f, k + e0, 1, q[..., 1]) + divdiff(f, k, 1, q[..., 1]))
    return np.stack([d0, d1], -1)

def F_all(f, k, q):
    kp = k + q
    e, ep = f(k), f(kp)
    om = ep - e
    Fd00 = 0.5*(e + ep)
    Dl = Delta(f, k, q)
    u = np.concatenate([np.ones(k.shape[:-1] + (1,)), Dl], -1)
    Fdust = Fd00[..., None, None]*u[..., :, None]*u[..., None, :]
    kw, kpw, qw = wrap(k), wrap(kp), wrap(q)
    phi = np.prod(plateau(kw, CHI_IN, CHI_OUT), -1)*np.prod(plateau(kpw, CHI_IN, CHI_OUT), -1)*np.prod(plateau(qw, Q_IN, Q_OUT), -1)
    ec = np.sqrt(M*M + (kw**2).sum(-1)); epc = np.sqrt(M*M + (kpw**2).sum(-1))
    K4 = np.concatenate([ec[..., None], kw], -1); Kp4 = np.concatenate([epc[..., None], kpw], -1)
    dot = ec*epc - (kw*kpw).sum(-1)
    eta = np.diag([1.0, -1.0, -1.0])
    Fc = (Kp4[..., :, None]*K4[..., None, :] + K4[..., :, None]*Kp4[..., None, :]
          - eta*(dot - M*M)[..., None, None])/(2*np.sqrt(ec*epc))[..., None, None]
    ph = np.concatenate([np.ones(k.shape[:-1] + (1,)), np.exp(-0.5j*qw)], -1)   # midpoint phase per spatial index
    Fc = Fc*ph[..., :, None]*ph[..., None, :]
    F = phi[..., None, None]*Fc + (1-phi)[..., None, None]*Fdust
    return F, om, phi

for name in ['L', 'G']:
    f = make_eps(name)
    print('[%s profile]' % name)
    sets = {
      'random (k, q) on torus': (rng.uniform(-np.pi, np.pi, (4000, 2)), rng.uniform(-np.pi, np.pi, (4000, 2))),
      'box pairs, small q (phi=1)': (rng.uniform(-1.2, 1.2, (4000, 2)), rng.uniform(-0.4, 0.4, (4000, 2))),
      'box -> edge across the face': (np.stack([rng.uniform(1.7, 2.0, 4000), rng.uniform(-1, 1, 4000)], -1),
                                      np.stack([rng.uniform(0.2, 0.8, 4000), rng.uniform(-0.3, 0.3, 4000)], -1)),
      'edge -> edge': (rng.uniform(2.1, np.pi, (4000, 2))*rng.choice([-1, 1], (4000, 2)), rng.uniform(-np.pi, np.pi, (4000, 2))),
    }
    for sname, (k, q) in sets.items():
        F, om, phi = F_all(f, k, q)
        Dq = Dsym(q)
        res = max(np.max(np.abs(om*F[:, 0, nu] - (Dq[:, 0]*F[:, 1, nu] + Dq[:, 1]*F[:, 2, nu]))) for nu in range(3))
        Fr, _, _ = F_all(f, k + q, -q)
        herm = np.max(np.abs(F - np.conj(Fr)))
        sym = np.max(np.abs(F - np.swapaxes(F, -1, -2)))
        print('  %-30s Ward |res| max = %.2e ; Hermiticity %.2e ; symmetry %.2e ; phi in [%.2f, %.2f]'
              % (sname, res, herm, sym, phi.min(), phi.max()))
    k = rng.uniform(-np.pi, np.pi, (2000, 2)); q = np.full_like(k, 1e-9)
    F, _, _ = F_all(f, k, q)
    h = 1e-6
    v = np.stack([(f(k + np.array([h, 0])) - f(k - np.array([h, 0])))/(2*h), (f(k + np.array([0, h])) - f(k - np.array([0, h])))/(2*h)], -1)
    U = np.concatenate([np.ones((len(k), 1)), v], -1)
    Ffw = f(k)[:, None, None]*U[:, :, None]*U[:, None, :]
    print('  forward values: max |F(k,k) - eps (1,v)(1,v)^T| = %.2e' % np.max(np.abs(F - Ffw)))
print('done %.0fs' % (time.time()-T0))
