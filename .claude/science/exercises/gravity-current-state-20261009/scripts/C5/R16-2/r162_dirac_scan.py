"""R16-2 (a),(c): on-shell one-loop Dirac speed F_1/2(m) = dc_e (per e^2, x16pi^2) and photon moment G_1/2(m)
on R14-1's D1(r) edges and R8-5's literal BQ edges, Peierls, Feynman gauge, photon mass lam (IR regulator).
Runner: R13-7's refereed on-shell code (r137_onshell.ce2_minus_1), with the p-step h adapted so that the
emission threshold E_p < W + E_k holds on the whole grid (p^2 < 2 m lam): h = min(0.02, 0.3 sqrt(2 m lam)).
Subtractions named before the run: none (the photon-side counterterm is a separate tuning, not a subtraction).
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r162_laws import D1Law
from r85_box_qed_copy import Law
from r137_onshell import dE_onshell, U
from r101_dirac_moment_copy import moment

def ce2(law, N, lam, h):
    r = dE_onshell(law, N, lam, [0.0, h, 2*h])
    F = {p: 2*r[p]['Ep']*r[p]['dE'] for p in r}
    D1 = (F[h]-F[0.0])/h**2; D2 = (F[2*h]-F[0.0])/(4*h**2)
    Ft = {p: 2*r[p]['Ep']*r[p]['tad'] for p in r}
    T1 = (Ft[h]-Ft[0.0])/h**2; T2 = (Ft[2*h]-Ft[0.0])/(4*h**2)
    return (4*D1-D2)/3/2*U, (4*T1-T2)/3/2*U

def hstep(m, lam):
    return min(0.02, 0.3*np.sqrt(2*m*lam))

if __name__ == '__main__':
    mode = sys.argv[1]
    t0 = time.time()
    if mode == 'conv':   # N, lam, h convergence on one D1 law
        for (b, r, c1, c2) in [(1.0, 1/np.sqrt(3), None, None), (1.4, 1/np.sqrt(3), None, None)]:
            for m in (0.1, 0.05):
                for lam in (0.05, 0.02, 0.01):
                    for N in (96, 128, 192):
                        L = D1Law(b, r, c1, c2, m); h = hstep(m, lam)
                        Fe, Ft = ce2(L, N, lam, h)
                        print('D1 b=%.1f r=%.3f ph=%s m=%.3f lam=%.3f N=%3d h=%.4f  F12*U=%+9.4f  [tad %+9.4f, rest %+8.4f]'
                              % (b, r, c1, m, lam, N, h, Fe, Ft, Fe-Ft), flush=True)
    if mode == 'family':  # F_1/2 at small m over the D1 family and photon shapes, plus G_1/2 (photon moment)
        N = int(sys.argv[2]); lam = 0.02
        for b in (1.0, 1.2, 1.4):
            for r in (0.0, 0.2, 0.4, 1/np.sqrt(3)):
                for (c1, c2) in [(None, None), (1.0, 2.0), (2.0, 3.0)]:
                    row = []
                    for m in (0.2, 0.1, 0.05):
                        L = D1Law(b, r, c1, c2, m)
                        Fe, Ft = ce2(L, N, lam, hstep(m, lam))
                        row.append((m, Fe, Ft))
                    L = D1Law(b, r, c1, c2, 0.05); G = moment(L, N)['tot']
                    # quadratic extrapolation in m to m -> 0 from (0.2, 0.1, 0.05)
                    ms = np.array([x[0] for x in row]); Fs = np.array([x[1] for x in row])
                    c = np.polyfit(ms, Fs, 2)
                    print('D1 b=%.1f r=%.3f Wpi=%.3f ph=%-4s N=%d | F(0.2,0.1,0.05)= %+8.4f %+8.4f %+8.4f | tad(0.05) %+8.4f | F0_extrap %+8.4f slope %+7.3f | G12(0.05) %+8.4f'
                          % (b, r, L.Wpi, c1, N, Fs[0], Fs[1], Fs[2], row[2][2], c[2], c[1], G), flush=True)
    if mode == 'literal':  # R8-5 literal BQ family (r = 0)
        N = int(sys.argv[2]); lam = 0.02
        for (b1, b2) in [(1.0, 2.0), (2.0, 3.0), (0.5, 1.5), (1.0, 3.0), (2.5, 3.1)]:
            for (c1, c2) in [(None, None), (1.0, 2.0), (2.0, 3.0)]:
                row = []
                for m in (0.2, 0.1, 0.05):
                    L = Law(b1, b2, 0.0, c1, c2, m, naive_photon=(c1 is None))
                    Fe, Ft = ce2(L, N, lam, hstep(m, lam)); row.append((m, Fe, Ft))
                ms = np.array([x[0] for x in row]); Fs = np.array([x[1] for x in row]); c = np.polyfit(ms, Fs, 2)
                L = Law(b1, b2, 0.0, c1, c2, 0.05, naive_photon=(c1 is None)); G = moment(L, N)['tot']
                print('LIT box=(%.1f,%.1f) ph=%-4s N=%d | F(0.2,0.1,0.05)= %+8.4f %+8.4f %+8.4f | tad %+8.4f | F0_extrap %+8.4f slope %+7.3f | G12(0.05) %+8.4f'
                      % (b1, b2, c1, N, Fs[0], Fs[1], Fs[2], row[2][2], c[2], c[1], G), flush=True)
    print('elapsed %.1fs' % (time.time()-t0))
