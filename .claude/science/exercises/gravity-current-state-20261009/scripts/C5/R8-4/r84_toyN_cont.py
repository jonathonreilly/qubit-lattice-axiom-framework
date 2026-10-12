"""R8-4 script D: two-loop toy N in 1+1D, infinite volume (trapezoid sums on a fine momentum grid; on the
vertex support every leg is inside the box, so these are the infinite-volume lattice sums).  Uses the Goldstone
closed form that script B2 verified against brute-force RS4 on the Fock space to 1e-17.
Reports, for p in a range:  one-loop  m2_1(p) = 2E_p dE2(p)  and two-loop mixed  m2_mix(p) = 2E_p mixed(p)
(the O(go^2 gi^2) coefficient of E^2 - p^2), split into nested-forward and nested-Z parts.
A Lorentz-invariant dressed dispersion needs both p-independent."""
import numpy as np, sys, time
np.seterr(all='ignore')
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)
def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
    e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def plateau(x, x1, x2): return 1.0 - sstep((np.abs(x) - x1)/(x2 - x1))
P = dict(L1=1.0, L2=1.4, A1=2.0, A2=2.5, C1=1.2, C2=1.6, C=1.0)
mass = dict(X=0.30, Y=0.33, A=0.37, B=0.41, U=0.29, C=0.35, D=0.43)
def E(k, s): return np.sqrt(mass[s]**2 + k*k)
def F(s): return plateau(np.sqrt(np.maximum(s, 0.0)), P['L1'], P['L2'])
def sinv(E1, k1, E2, k2): return (E1 + E2)**2 - (k1 + k2)**2
def Psi3(e, k): return F(sinv(e[0], k[0], e[1], k[1]))*F(sinv(e[0], k[0], e[2], k[2]))*F(sinv(e[1], k[1], e[2], k[2]))
def legc(k): return plateau(k, P['A1'], P['A2'])
def totc(k): return plateau(k, P['C1'], P['C2'])
STAT = ['F']
def hfac(Ex, W): return (W*(1 + 2*P['C']) - Ex)/(W + Ex) if STAT[0] == 'F' else 1.0 + 0*W
def zs(): return -1.0 if STAT[0] == 'F' else 1.0

def cluster(K, sp, grid, h):
    """all 3-particle configurations of species sp with total momentum K: k1, k2 on the grid, k3 = K - k1 - k2.
    returns energies, momenta, Psi*cuts, weight h^2/(2pi)^2"""
    k1, k2 = np.meshgrid(grid, grid, indexing='ij'); k1 = k1.ravel(); k2 = k2.ravel(); k3 = K - k1 - k2
    e = (E(k1, sp[0]), E(k2, sp[1]), E(k3, sp[2])); k = (k1, k2, k3)
    ps = Psi3(e, k)*legc(k1)*legc(k2)*legc(k3)
    keep = ps != 0
    return [x[keep] for x in e], [x[keep] for x in k], ps[keep], h*h/(2*np.pi)**2

def run(G, K=2.6):
    grid = np.linspace(-K, K, G); h = grid[1] - grid[0]
    # inner data per Y momentum is needed at arbitrary kY (outer cluster legs), so compute on the fly with caching by value
    cache = {}
    def inner(kY):
        key = round(float(kY), 12)
        if key in cache: return cache[key]
        EY = E(kY, 'Y')
        e, k, ps, w = cluster(kY, ('U', 'C', 'D'), grid, h)
        W = e[0] + e[1] + e[2]
        wF = w*ps**2*hfac(EY, W)/(2*EY*8*e[0]*e[1]*e[2])*totc(kY)**2
        cF = W - EY
        e, k, ps, w = cluster(-kY, ('U', 'C', 'D'), grid, h)
        W = e[0] + e[1] + e[2]
        wZ = w*ps**2/(2*EY*8*e[0]*e[1]*e[2])*totc(kY)**2
        bZ = EY + W
        cache[key] = (wF, cF, np.sum(wZ/bZ), np.sum(wZ/bZ**2))
        return cache[key]
    def Nfun(al, kY):
        wF, cF, Z1, Z2 = inner(kY)
        fw = np.sum(wF/(al - cF))/al**2
        zz = zs()*(al*Z2 - Z1)/al**2      # = sum zs wZ (al - b)/(al^2 b^2)
        return fw, zz
    rows = []
    for p in [0.0, 0.1, 0.2, 0.3, 0.4, 0.6]:
        Ep = E(p, 'X')
        one = 0.0; mixF = 0.0; mixZ = 0.0; onshellY = 0.0
        for sgn in (+1, -1):     # forward cluster at +p ; Z cluster at -p
            e, k, ps, w = cluster(sgn*p, ('Y', 'A', 'B'), grid, h)
            W = e[0] + e[1] + e[2]
            if sgn > 0:
                wo = w*ps**2*hfac(Ep, W)/(2*Ep*8*e[0]*e[1]*e[2])*totc(p)**2; al = Ep - W
            else:
                wo = zs()*w*ps**2/(2*Ep*8*e[0]*e[1]*e[2])*totc(p)**2; al = -(Ep + W)
            one += np.sum(wo/al)
            for i in range(len(wo)):
                fw, zz = Nfun(al[i], k[0][i])
                mixF += wo[i]*fw; mixZ += wo[i]*zz
        rows.append((p, 2*Ep*one, 2*Ep*mixF, 2*Ep*mixZ, 2*Ep*(mixF + mixZ)))
    # inner (Y) one-loop covariance check, same grid
    yrows = []
    for kY in [0.0, 0.2, 0.4, 0.6]:
        wF, cF, Z1, Z2 = inner(kY); EY = E(kY, 'Y')
        yrows.append((kY, 2*EY*(np.sum(wF/(-cF)) - zs()*Z1)))
    return rows, yrows

if __name__ == '__main__':
    t0 = time.time()
    pr('# R8-4 D: toy N, 1+1D infinite volume; columns p, m2_1loop, m2_mix[nested fwd], m2_mix[nested Z], m2_mix[total]')
    pr(f'# params {P} masses {mass}')
    args = sys.argv[1:]
    if args and args[0] in ('F', 'B'): STAT[0] = args.pop(0)
    pr(f'# statistics {STAT[0]}')
    for G in [int(a) for a in (args or ['81', '121'])]:
        rows, yrows = run(G)
        pr(f'## grid G={G} (spacing {5.2/(G-1):.4f})  t={time.time()-t0:.0f}s')
        r0 = rows[0]
        for r in rows:
            pr(f'  p={r[0]:.2f}  m2_1={r[1]:+.10e}  mixF={r[2]:+.10e}  mixZ={r[3]:+.10e}  mix={r[4]:+.10e}   rel.dev: 1loop {(r[1]-r0[1])/abs(r0[1]):+.2e}  mix {(r[4]-r0[4])/abs(r0[4]):+.2e}')
        y0 = yrows[0][1]
        pr('  inner Y one-loop m2(kY): ' + '  '.join(f'kY={a:.1f}:{b:+.10e}({(b-y0)/abs(y0):+.1e})' for a, b in yrows))
    open(__file__.replace('.py', f'_{STAT[0]}.out'), 'w').write('\n'.join(OUT) + '\n')
