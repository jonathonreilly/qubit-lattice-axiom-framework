"""R9-7 script B: infinite-volume (1+1D, continuum dispersion on the support) two-loop mixed coefficient of toy N
with (i) toy N's 10 orderings, (ii) the complete 24-ordering crossing set, under several vertex prescriptions.
Uses the 24-ordering closed form that script A (r97_fock.py) verified against brute-force RS4 on the Fock space.
Inner cluster U C D enters only through its invariant mass M (exact: its vertex functions depend only on UCD's
internal invariants; Lemma INV-3F), so  mix(p) = sum_n w_n Ktil(p; M_n)  with rest-frame samples (M_n, w_n) and
Ktil interpolated in M (Chebyshev).  Rapidity grids: dk/(2E) = dtheta/2.
Prescriptions (outer kernels; inner always toy N's Psi(U,C,D), h_i on the inner decay for fermions):
  P0  toy N: dec = Psi(Y,A,B) sqrt(h_o), vac = Psi(Y,A,B); no 22/31  (10 orderings)
  P1  registered completion: P0 + 22 = s22 F(s_AB), 31 = s31 F(s_XA)F(s_XB)F(s_AB)      (24 orderings)
  P2  'closed-cluster' prescription: every outer type = F(s_AB) only (dec also x sqrt(h_o) for fermions)  (24)
  P2T same kernels as P2 but toy N's 10 orderings only
F == 1 (L1 = None) is the local limit (no plateau at all)."""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r97_common import Fpl, s2, hfac, ORD
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)
MASS = dict(X=0.30, Y=0.33, A=0.37, B=0.41, U=0.29, C=0.35, D=0.43)

def inner_samples(L1, L2, Gin, Th, mass):
    th = np.linspace(-Th, Th, Gin); dth = th[1] - th[0]
    tU, tC = np.meshgrid(th, th, indexing='ij'); tU = tU.ravel(); tC = tC.ravel()
    kU = mass['U']*np.sinh(tU); kC = mass['C']*np.sinh(tC); kD = -kU - kC
    EU = mass['U']*np.cosh(tU); EC = mass['C']*np.cosh(tC); ED = np.sqrt(mass['D']**2 + kD**2)
    Psi = Fpl(s2(EU, kU, EC, kC), L1, L2)*Fpl(s2(EU, kU, ED, kD), L1, L2)*Fpl(s2(EC, kC, ED, kD), L1, L2)
    w = dth*dth*EU*EC/(2*np.pi)**2*Psi**2/(8*EU*EC*ED)
    M = EU + EC + ED; keep = w > 0
    return M[keep], w[keep]

def cheb_nodes(a, b, n):
    j = np.arange(n); x = np.cos(np.pi*(j + 0.5)/n)
    return 0.5*(a + b) + 0.5*(b - a)*x, x
def bary_eval(xn, fn, x):
    n = len(xn); j = np.arange(n); wts = (-1.0)**j*np.sin(np.pi*(j + 0.5)/n)
    d = x[:, None] - xn[None, :]
    exact = np.isclose(d, 0.0, atol=1e-15)
    d = np.where(exact, 1.0, d)
    t = wts[None, :]/d
    val = (t*fn[None, :]).sum(1)/t.sum(1)
    hit = exact.any(1)
    if hit.any(): val[hit] = fn[np.argmax(exact[hit], 1)]
    return val

def run(stat, presc, L1, L2, ps, G=601, Th=7.5, Gin=601, Thin=None, nM=40, s22=1.0, s31=1.0, mass=MASS, verbose=False, Mlist=None):
    m = mass
    if Thin is None: Thin = 9.0 if L1 is None else np.arcsinh(2.5*L2/0.29)
    Mn, wn = inner_samples(L1, L2, Gin, Thin, m)
    Mmin = m['U'] + m['C'] + m['D']; Mmax = Mn.max()
    unbounded = L1 is None
    if unbounded:      # nodes in x = Mmin/M in (0, 1]
        xmax = 1.0; xmin = Mmin/Mmax
        xs, _ = cheb_nodes(xmin, xmax, nM); Mnodes = Mmin/xs
    else:
        Mnodes, _ = cheb_nodes(Mmin, Mmax, nM)
    if Mlist is not None: Mnodes = np.array(Mlist, float)
    th = np.linspace(-Th, Th, G); dth = th[1] - th[0]
    tA, tB = np.meshgrid(th, th, indexing='ij'); tA = tA.ravel(); tB = tB.ravel()
    kA = m['A']*np.sinh(tA); kB = m['B']*np.sinh(tB); EA = m['A']*np.cosh(tA); EB = m['B']*np.cosh(tB)
    meas = dth*dth*EA*EB/(2*np.pi)**2
    fer = stat == 'F'
    allowed = {'P0': ('dec', 'vac'), 'P2T': ('dec', 'vac')}.get(presc, ('dec', 'vac', '22', '31'))
    ords = [o for o in ORD if o['oa'] in allowed and o['ob'] in allowed]
    rows = []
    for p in ps:
        E = np.sqrt(m['X']**2 + p*p)
        kY = p - kA - kB; EY = np.sqrt(m['Y']**2 + kY**2); Wo = EY + EA + EB
        FAB = Fpl(s2(EA, kA, EB, kB), L1, L2)
        ho = hfac(E, Wo) if fer else 1.0
        if presc in ('P0', 'P1'):
            Po = Fpl(s2(EY, kY, EA, kA), L1, L2)*Fpl(s2(EY, kY, EB, kB), L1, L2)*FAB
            kern = {'dec': Po*np.sqrt(ho), 'vac': Po, '22': s22*FAB,
                    '31': s31*Fpl(s2(E, p, EA, -kA), L1, L2)*Fpl(s2(E, p, EB, -kB), L1, L2)*FAB}
            P1o = Po
        elif presc == 'P3':   # crossing-consistent: one Y-dependent function of Feynman-orientation 3-momenta for all types
            Po = Fpl(s2(EY, kY, EA, kA), L1, L2)*Fpl(s2(EY, kY, EB, kB), L1, L2)*FAB
            kern = {'dec': Po*np.sqrt(ho), 'vac': Po, '22': s22*Po, '31': s31*Po}
            P1o = Po
        elif presc == 'P4':   # plateau on the invariant mass of the whole created set
            FYAB = Fpl(Wo**2 - p*p, L1, L2)
            EXAB = E + EA + EB
            FXAB = Fpl(EXAB**2 - (p - kA - kB)**2, L1, L2)
            kern = {'dec': FYAB*np.sqrt(ho), 'vac': FYAB, '22': s22*FAB, '31': s31*FXAB}
            P1o = FYAB
        elif presc == 'P2swap':   # P2 with the dressed line inside the plateau pair: F(s_{Y B}) on every type (Feynman-orientation momenta)
            FYB = Fpl(s2(EY, kY, EB, kB), L1, L2)
            kern = {'dec': FYB*np.sqrt(ho), 'vac': FYB, '22': s22*FYB, '31': s31*FYB}
            P1o = FYB
        elif presc == 'FF':   # comparator: frame-fixed leg cutoffs, same function for every crossing (local vertex x chi)
            from r97_common import plateau
            chi = plateau(kY, L1, L2)*plateau(kA, L1, L2)*plateau(kB, L1, L2)
            kern = {'dec': chi*np.sqrt(ho), 'vac': chi, '22': s22*chi, '31': s31*chi}
            P1o = chi
        else:   # P2, P2T
            kern = {'dec': FAB*np.sqrt(ho), 'vac': FAB, '22': s22*FAB, '31': s31*FAB}
            P1o = FAB
        nrm = meas/(2*E*4*EY*EY*2*EA*2*EB)
        one = np.sum(meas/(2*E*2*EY*2*EA*2*EB)*P1o**2*(ho/(E - Wo) + (1.0 if fer else -1.0)/(E + Wo)))
        nz = np.zeros_like(kA, bool)
        for t in allowed: nz |= kern[t] != 0
        idx = np.nonzero(nz)[0]
        en0 = dict(Y1=EY[idx], Y2=EY[idx], A=EA[idx], B=EB[idx], Xin=E, Xout=E)
        kk = {t: kern[t][idx] for t in allowed}
        Kt = np.zeros(len(Mnodes)); KtT = np.zeros(len(Mnodes))
        for iM, M in enumerate(Mnodes):
            W = np.sqrt(M*M + kY[idx]**2); en = dict(en0); en['Phi'] = W
            hi = hfac(EY[idx], W) if fer else 1.0
            acc = np.zeros(len(idx)); accT = np.zeros(len(idx))
            for o in ords:
                v = kk[o['oa']]*kk[o['ob']]
                if o['i1_dec']: v = v*np.sqrt(hi)
                if o['i2_dec']: v = v*np.sqrt(hi)
                if fer and (o['nback'] & 1): v = -v
                for ls in o['pres']:
                    v = v/(E - sum(en[x] for x in ls))
                acc += v
                if o['toyN']: accT += v
            Kt[iM] = np.sum(nrm[idx]*acc*M/W); KtT[iM] = np.sum(nrm[idx]*accT*M/W)
        if unbounded:
            mix = np.sum(wn*bary_eval(xs, Kt, Mmin/Mn)); mixT = np.sum(wn*bary_eval(xs, KtT, Mmin/Mn))
        else:
            mix = np.sum(wn*bary_eval(Mnodes, Kt, Mn)); mixT = np.sum(wn*bary_eval(Mnodes, KtT, Mn))
        rows.append((p, 2*E*one, 2*E*mix, 2*E*mixT, Kt.copy(), Mnodes.copy()))
    return rows

def report(tag, rows, which=2):
    r0 = rows[0]
    s = []
    for r in rows:
        s.append(f'p={r[0]:.2f}: {(r[which]-r0[which])/abs(r0[which]):+.3e}')
    pr(f'  {tag}: m2(0)={r0[which]:+.6e}  rel.dev  ' + '  '.join(s))

if __name__ == '__main__':
    t0 = time.time()
    args = sys.argv[1:]
    stat = args[0] if args else 'B'
    mode = args[1] if len(args) > 1 else 'base'
    ps = [0.0, 0.1, 0.2, 0.3, 0.4, 0.6]
    pr(f'# R9-7 B: statistics {stat}, mode {mode}; masses {MASS}')
    if mode == 'base':
        for (G, Th, Gin, nM) in [(401, 7.5, 401, 32), (601, 8.5, 601, 48)]:
            pr(f'## grid G={G} Theta={Th} Gin={Gin} nM={nM}   (L1, L2) = (1.0, 1.4)')
            for presc in ['P1', 'P2']:
                rows = run(stat, presc, 1.0, 1.4, ps, G=G, Th=Th, Gin=Gin, nM=nM)
                report(f'{presc} one-loop     ', rows, 1)
                report(f'{presc} 10 toyN ords ', rows, 3)
                report(f'{presc} all 24 ords  ', rows, 2)
                pr(f'     t={time.time()-t0:.0f}s')
    if mode == 'local':
        for lam in [1.0, 2.0, 4.0, 8.0, 16.0, None]:
            L1 = lam; L2 = None if lam is None else 1.4*lam
            for (G, Th, Gin, nM) in [(401, 8.5, 401, 40), (601, 10.0, 601, 56)]:
                rows = run(stat, 'P1', L1, L2, ps, G=G, Th=Th, Gin=Gin, nM=nM)
                pr(f'## P1 plateau scale Lambda1={lam} (F==1 if None), grid G={G} Theta={Th} Gin={Gin} nM={nM}  t={time.time()-t0:.0f}s')
                report('one-loop     ', rows, 1)
                report('10 toyN ords ', rows, 3)
                report('all 24 ords  ', rows, 2)
    if mode == 'family':
        sets = [(1.0, 1.0)] if stat == 'B' else [(1.0, 1.0), (1.0, -1.0), (-1.0, 1.0), (-1.0, -1.0)]
        for presc in ['P1', 'P2', 'P3', 'P4']:
            for (a, b) in sets:
                for (G, Th, Gin, nM) in [(401, 7.5, 401, 32), (601, 8.5, 601, 48)]:
                    rows = run(stat, presc, 1.0, 1.4, ps, G=G, Th=Th, Gin=Gin, nM=nM, s22=a, s31=b)
                    pr(f'## {presc} (s22,s31)=({a:+.0f},{b:+.0f}) (L1,L2)=(1,1.4) grid G={G} Theta={Th} Gin={Gin} nM={nM}  t={time.time()-t0:.0f}s')
                    report('one-loop     ', rows, 1)
                    report('10 toyN ords ', rows, 3)
                    report('all 24 ords  ', rows, 2)
        rows = run(stat, 'P1', None, None, ps, G=601, Th=10.0, Gin=601, nM=56)
        pr(f'## F==1 local limit (all prescriptions coincide), G=601 Theta=10  t={time.time()-t0:.0f}s')
        report('one-loop     ', rows, 1); report('10 toyN ords ', rows, 3); report('all 24 ords  ', rows, 2)
    if mode == 'mscale':
        for presc in ['P1', 'P3', 'P4']:
            for sc, G in [(1.0, 401), (0.5, 601), (0.25, 801)]:
                mass = {k: v*sc for k, v in MASS.items()}
                p1 = mass['X']/3
                rows = run(stat, presc, 1.0, 1.4, [0.0, p1], G=G, Th=8.5 + np.log(1/sc), Gin=G, nM=48, mass=mass)
                r0, r1 = rows
                rel = (r1[2] - r0[2])/abs(r0[2]); relT = (r1[3] - r0[3])/abs(r0[3]); rel1 = (r1[1] - r0[1])/abs(r0[1])
                pr(f'{presc} masses x{sc}: G={G} p/m=1/3: m2_mix(0)={r0[2]:+.6e} rel={rel:+.4e} c=rel/(p/m)^2={9*rel:+.4e} | toyN-subset c={9*relT:+.4e} | one-loop rel {rel1:+.1e}  t={time.time()-t0:.0f}s')
    if mode == 'Mkernel':
        Ml = [1.2, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0]
        for presc in ['P1', 'P3', 'P4', 'P2']:
            rows = run(stat, presc, 1.0, 1.4, [0.0, 0.1, 0.2], G=601, Th=8.5, Gin=201, nM=8, Mlist=Ml)
            K0, K1, K2 = rows[0][4], rows[1][4], rows[2][4]
            E0 = MASS['X']; E1 = np.sqrt(MASS['X']**2 + 0.01); E2 = np.sqrt(MASS['X']**2 + 0.04)
            pr(f'{presc}: fixed-M kernel, rel.dev of 2E*K(p;M) at p=0.1 / p=0.2:  ' + '  '.join(
               f'M={M:g}: {(2*E1*K1[i]-2*E0*K0[i])/abs(2*E0*K0[i]):+.3e}/{(2*E2*K2[i]-2*E0*K0[i])/abs(2*E0*K0[i]):+.3e} (M^2*2EK0={M*M*2*E0*K0[i]:+.3e})' for i, M in enumerate(Ml)) + f'  t={time.time()-t0:.0f}s')
    if mode == 'swap':
        for presc in ['P2', 'P2swap']:
            for (G, Th, Gin, nM) in [(401, 7.5, 401, 32), (601, 8.5, 601, 48)]:
                rows = run(stat, presc, 1.0, 1.4, ps, G=G, Th=Th, Gin=Gin, nM=nM)
                pr(f'## {presc} grid G={G} Theta={Th}  t={time.time()-t0:.0f}s')
                report('one-loop     ', rows, 1); report('10 toyN ords ', rows, 3); report('all 24 ords  ', rows, 2)
    if mode == 'lamscan':
        for presc in ['P1', 'P3', 'P4', 'FF']:
            for lam in [1.0, 2.0, 4.0]:
                rows = run(stat, presc, lam, 1.4*lam, [0.0, 0.1], G=601, Th=9.0, Gin=601, nM=56)
                r0, r1 = rows
                pr(f'{presc} Lambda1={lam}: one-loop rel(p=0.1) {(r1[1]-r0[1])/abs(r0[1]):+.4e}   two-loop all-24 rel(p=0.1) {(r1[2]-r0[2])/abs(r0[2]):+.4e}   toyN-10 rel {(r1[3]-r0[3])/abs(r0[3]):+.4e}  t={time.time()-t0:.0f}s')
    open(__file__.replace('.py', f'_{stat}_{mode}.out'), 'w').write('\n'.join(OUT) + '\n')
