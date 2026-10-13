"""R19-30 probe (e): are the rows unchanged?
(1) O(q^4) scaling of the re-placement in the tilde (row) kernel: max |tilde_PR - tilde_raw| / |q|^4 for the Dirac UD and
    scalar E1 kernels along the axial, face and body directions (and R19-26's FF for the per-leg U).
(2) Direct one-loop Dirac TT rows Xi = d_{q^2} Pi(0,q) + d_{w^2} Pi(w,0) on a kbar midpoint grid with continuous q
    (legs kbar +- q/2; Pi(0,q) = -< (t_{+-} + t_{-+}) / (E1 + E2) >, t_{+-} = tr[P+(k1) Gam P-(k2) Gam^dag],
    beta = -< t0 / (4 E^3) >; R16-13/R18-5 normalization, dface.py polarizations) for three vertices:
      'rows'  : Gam = sum e_ij UD^{ij}(kbar)                    (R18-5/R18-13's rows convention: tilde = UD)
      'PR'    : Gam = sum e_ij [parity-resolved re-placed UD]^{ij}
      'R19-5' : Gam = sum e_ij e^{+i q.p_ij} UD^{ij}(kbar)      (tilde of R19-5's literal site-label pair block)
    alpha by Richardson on s = h, 2h.  Usage: python r1930_rows.py m N h"""
import sys, time, numpy as np
import lib1930 as L
t0 = time.time()
m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.3
N = int(sys.argv[2]) if len(sys.argv) > 2 else 40
h = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
DI = L.Dirac(m=m); SC = L.Scalar(m=m)
COMPS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]

# ---------------- (1) O(q^4) scaling -----------------------------------------------------------------------------------
rng = np.random.default_rng(193005)
kb = rng.uniform(-np.pi, np.pi, (3000, 3))
print('R19-30 (e) rows.  (1) re-placement in the row kernel is O(q^4): max over comps and 3000 kbar of |tilde_new - tilde_raw|/|q|^4')
for nm, n in (('axial z', (0, 0, 1)), ('face 110', (1, 1, 0)), ('body 111', (1, 1, 1))):
    n = np.array(n, float)/np.linalg.norm(n); row = []
    for s in (0.2, 0.1, 0.05, 0.025):
        q = np.tile(s*n, (len(kb), 1)); dD = dS = 0.0
        for (i, j) in COMPS:
            fD = lambda kk: DI.UDcoef(kk, i, j)
            dD = max(dD, np.abs(L.tilde_component(fD, kb, q, i, j, 'PR') - fD(kb)).max())
            fS = lambda kk: (SC.f(kk[..., i])*SC.f(kk[..., j]))[..., None]
            dS = max(dS, np.abs(L.tilde_component(fS, kb, q, i, j, 'PR') - fS(kb)).max())
        row.append('s=%.3f: Dirac %.3e scalarE1 %.3e' % (s, dD/s**4, dS/s**4))
    print('  %-8s ' % nm + ' | '.join(row))

# ---------------- (2) direct Dirac rows ------------------------------------------------------------------------------
r2, r6 = np.sqrt(2.0), np.sqrt(6.0)
def pols():
    P = {}
    e = np.zeros((3, 3)); e[0, 1] = e[1, 0] = 0.5; P['T2g'] = (e, (0, 0, 1))
    P['Eg'] = (np.diag([0.5, -0.5, 0.0]), (0, 0, 1))
    a = np.array([1, -1, 0])/r2; b = np.array([0, 0, 1.0])
    P['face1'] = (0.5*(np.outer(a, a) - np.outer(b, b)), (1, 1, 0)); P['face2'] = (0.5*(np.outer(a, b) + np.outer(b, a)), (1, 1, 0))
    b2 = np.array([1, 1, -2])/r6; P['body'] = (0.5*(np.outer(a, a) - np.outer(b2, b2)), (1, 1, 1))
    return P
POL = pols()
kg = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
KB = np.stack(np.meshgrid(kg, kg, kg, indexing='ij'), -1).reshape(-1, 3)
UDc = {c: DI.UDcoef(KB, *c) for c in COMPS}
UDpar = {c: L.parity_parts(lambda kk, c=c: DI.UDcoef(kk, *c), KB) for c in COMPS}

def gamma(e, q, variant):
    acc = np.zeros(KB.shape[:-1] + (4,), complex)
    for (i, j) in COMPS:
        w = e[i, j] + (e[j, i] if i != j else 0.0)
        if w == 0.0: continue
        if variant == 'rows':
            c = UDc[(i, j)]
        elif variant == 'R19-5':
            c = UDc[(i, j)]*np.exp(0.5j*(q[i] + q[j]))
        else:
            t = L.tau(i, j); qq = np.tile(q, (len(KB), 1)); c = 0.0
            for s, v in UDpar[(i, j)].items():
                c = c + L.A_sigma(qq, np.array(s), t)[:, None]*v
        acc = acc + w*c
    return np.einsum('na,aij->nij', acc, L.GAM)

def Pi0q(e, q, variant):
    k1, k2 = KB + q/2, KB - q/2
    Pp1, Pm1, Pp2, Pm2 = DI.proj(k1, 1), DI.proj(k1, -1), DI.proj(k2, 1), DI.proj(k2, -1)
    G = gamma(e, q, variant); Gd = np.conj(np.swapaxes(G, -1, -2))
    t = np.einsum('nij,njk,nkl,nli->n', Pp1, G, Pm2, Gd) + np.einsum('nij,njk,nkl,nli->n', Pm1, G, Pp2, Gd)
    return -np.mean(t.real/(DI.E(k1) + DI.E(k2))), np.abs(t.imag).max()

print('(2) direct one-loop Dirac rows, D1(%.9f, %.9f), m = %g, kbar grid N = %d, Richardson s = %g, %g' % (DI.b, DI.r, m, N, h, 2*h))
res = {}
for name, (e, n) in POL.items():
    n = np.array(n, float)/np.linalg.norm(n)
    out = []
    for variant in ('rows', 'PR', 'R19-5'):
        P0, _ = Pi0q(e, 0*n, variant); P1, im1 = Pi0q(e, h*n, variant); P2, im2 = Pi0q(e, 2*h*n, variant)
        alpha = (16*(P1 - P0) - (P2 - P0))/(12*h*h)
        # beta at q = 0 (identical for all variants: at q = 0 the vertices coincide)
        E = DI.E(KB); Pp, Pm = DI.proj(KB, 1), DI.proj(KB, -1); G = gamma(e, 0*n, variant); Gd = np.conj(np.swapaxes(G, -1, -2))
        t0_ = (np.einsum('nij,njk,nkl,nli->n', Pp, G, Pm, Gd) + np.einsum('nij,njk,nkl,nli->n', Pm, G, Pp, Gd)).real/2
        beta = -np.mean(t0_/(4*E**3))
        out.append((alpha + beta, max(im1, im2)))
    res[name] = out
    print('  %-6s Xi rows %+.8e | PR - rows %+.2e | R19-5 literal - rows %+.4e (rel %.1e) | max|Im t| %.1e'
          % (name, out[0][0], out[1][0] - out[0][0], out[2][0] - out[0][0], abs(out[2][0] - out[0][0])/abs(out[0][0]), max(o[1] for o in out)), flush=True)
X = {k: v[0][0] for k, v in res.items()}
print('  O_h relation residual (rows) body - (8 face1 + 4 face2 - 3 Eg)/9 = %+.2e' % (X['body'] - (8*X['face1'] + 4*X['face2'] - 3*X['Eg'])/9))
X5 = {k: v[2][0] for k, v in res.items()}
print('  O_h relation residual (R19-5 literal)                          = %+.2e' % (X5['body'] - (8*X5['face1'] + 4*X5['face2'] - 3*X5['Eg'])/9))
print('time %.1f s' % (time.time() - t0))
