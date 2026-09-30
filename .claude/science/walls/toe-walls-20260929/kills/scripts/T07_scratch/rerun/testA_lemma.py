"""Test A: fine-grained H-theorem, dissipation identity, max principle, frozen real wave.
Random nearest-neighbour Hermitian hopping (2-component coin per site) on 1D/2D/3D tori,
Bell minimal rates on site configurations, exact ensemble evolution (Radau, rtol 1e-11)."""
import numpy as np
from scipy.integrate import solve_ivp

def build(dims, rng, real=False):
    n = int(np.prod(dims)); D = len(dims)
    idx = np.arange(n).reshape(dims)
    H = np.zeros((2*n, 2*n), complex)
    rnd = lambda: rng.normal(size=(2, 2)) + (0 if real else 1j*rng.normal(size=(2, 2)))
    pairs = set()
    for ax in range(D):
        nb = np.roll(idx, -1, axis=ax)
        for x, y in zip(idx.ravel(), nb.ravel()):
            if x != y: pairs.add((min(x, y), max(x, y)))
    for (x, y) in sorted(pairs):
        B = rnd()
        H[2*x:2*x+2, 2*y:2*y+2] += B; H[2*y:2*y+2, 2*x:2*x+2] += B.conj().T
    for x in range(n):
        A = rnd(); H[2*x:2*x+2, 2*x:2*x+2] += (A + A.conj().T)/2
    return n, H, sorted(pairs)

def make_W(n, H, pairs):
    xs = np.array([p[0] for p in pairs]); ys = np.array([p[1] for p in pairs])
    Hb = np.array([H[2*x:2*x+2, 2*y:2*y+2] for x, y in pairs])   # H_{x,y}, (npairs,2,2)
    def W(psi):
        ps = psi.reshape(n, 2)
        P = (np.abs(ps)**2).sum(1)
        # J_{x<-y} = 2 Im[psi_x^dag H_{xy} psi_y]  (flow y->x); J_{y<-x} = -J_{x<-y}
        Jxy = 2*np.imag(np.einsum('pi,pij,pj->p', ps[xs].conj(), Hb, ps[ys]))   # current y -> x
        Jp = np.zeros((n, n))       # Jp[dst, src] = max(0, J_{dst<-src})
        for k in range(len(xs)):
            if Jxy[k] > 0: Jp[xs[k], ys[k]] += Jxy[k]
            else:          Jp[ys[k], xs[k]] += -Jxy[k]
        Wm = Jp / P[None, :]
        Wm = Wm - np.diag(Wm.sum(0))
        return P, Jp, Wm, Jxy
    return W

phi = lambda a, b: a*np.log(a/b) - a + b

def run(dims, seed, real=False, T=3.0, nt=61):
    rng = np.random.default_rng(seed)
    n, H, pairs = build(dims, rng, real)
    E, V = np.linalg.eigh(H)
    if real:
        psi0 = V[:, 0].astype(complex)
    else:
        psi0 = rng.normal(size=2*n) + 1j*rng.normal(size=2*n)
    psi0 = psi0/np.linalg.norm(psi0)
    Wfun = make_W(n, H, pairs)
    psi = lambda t: (V*np.exp(-1j*E*t)) @ (V.conj().T @ psi0)
    rho0 = rng.random(n)**2 + 0.01; rho0 /= rho0.sum()
    Wt = lambda t: Wfun(psi(t))
    ts = np.linspace(0, T, nt)
    sol = solve_ivp(lambda t, y: Wt(t)[2] @ y, (0, T), rho0, method='Radau', jac=lambda t, y: Wt(t)[2],
                    t_eval=ts, rtol=1e-11, atol=1e-14)
    R = sol.y.T
    Ds, fmax, fmin, derr, maxJ, eqerr = [], [], [], [], 0.0, 0.0
    for i, t in enumerate(ts):
        P, Jp, Wm, Jxy = Wt(t)
        maxJ = max(maxJ, np.abs(Jxy).max())
        fr = R[i]/P
        Ds.append(float((R[i]*np.log(fr)).sum())); fmax.append(fr.max()); fmin.append(fr.min())
        diss = sum(Jp[y, x]*phi(fr[x], fr[y]) for x in range(n) for y in range(n) if Jp[y, x] > 0)
        h = 1e-5
        dPdt = ((np.abs(psi(t+h).reshape(n, 2))**2).sum(1) - (np.abs(psi(t-h).reshape(n, 2))**2).sum(1))/(2*h)   # true Schroedinger dP/dt
        eqerr = max(eqerr, np.abs(Wm @ P - dPdt).max())                                                       # equivariance check
        dD = float(((Wm @ R[i])*(np.log(fr)+1)).sum() - (fr*dPdt).sum())
        derr.append(abs(dD + diss)/(abs(dD) + 1e-9))
    Ds = np.array(Ds)
    return dict(n=n, D0=Ds[0], DT=Ds[-1], max_increase=float(np.max(np.diff(Ds))), diss_relerr=max(derr),
                eqerr=float(eqerr), fmax_mono=bool(np.all(np.diff(fmax) <= 1e-9)), fmin_mono=bool(np.all(np.diff(fmin) >= -1e-9)), maxJ=float(maxJ))

if __name__ == '__main__':
    out = []
    print('--- complex random waves (A1, A2) ---')
    for dims in [(8,), (4, 4), (3, 3, 3), (6,), (2, 2, 2)]:
        for seed in range(3):
            r = run(dims, seed); out.append(r)
            print(dims, seed, 'D0=%.4f DT=%.4f maxinc=%.2e diss_relerr=%.2e fmax_mono=%s fmin_mono=%s' % (r['D0'], r['DT'], r['max_increase'], r['diss_relerr'], r['fmax_mono'], r['fmin_mono']), flush=True)
    print('SUMMARY  max increase of D over all runs: %.2e' % max(o['max_increase'] for o in out))
    print('SUMMARY  max dissipation-identity relative error: %.2e' % max(o['diss_relerr'] for o in out))
    print('SUMMARY  max equivariance mismatch |W P - dP/dt|: %.2e' % max(o['eqerr'] for o in out))
    print('SUMMARY  f-max monotone down all: %s ; f-min monotone up all: %s' % (all(o['fmax_mono'] for o in out), all(o['fmin_mono'] for o in out)))
    print('--- real wave = ground state of a real Hamiltonian (A3) ---')
    for dims in [(8,), (4, 4), (3, 3, 3)]:
        r = run(dims, 11, real=True)
        print(dims, 'max|J|=%.2e  D0=%.6f DT=%.6f |DT-D0|=%.2e' % (r['maxJ'], r['D0'], r['DT'], abs(r['DT']-r['D0'])))
