import numpy as np, time
from scipy.linalg import expm
import r1913_dirac as D
# (1) R19-10 reproduction at R=0 with their P-loc = negproj(beta(m+3r)) and their 8x8 antiperiodic grid
for m in (0.0, 1.0):
    kp = 2*np.pi*(np.arange(8)+0.5)/8
    w, V = np.linalg.eigh(D.be*(m+3)); Ploc = V[:, w<0] @ V[:, w<0].conj().T
    acc = 0; accopt = 0
    for ky in kp:
        for kz in kp:
            h0 = D.be*(m + (2-np.cos(ky)-np.cos(kz)) + 1) + D.al[1]*np.sin(ky) + D.al[2]*np.sin(kz)
            W = D.window(h0, 0)
            W2 = dict(W); G0 = W['G0'].copy(); G0[:, :] = Ploc; W2['G0'] = G0
            acc += D.energy(W2, np.eye(4)) - W['Emid_old'] - W['e0']
            accopt += D.energy(W, np.eye(4)) - W['Emid_old'] - W['e0']
    print('m=%g R=0 P-loc (R19-10 state, infinite chain) = %.6f  [R19-10 ring Lx=32: %s];  per-q optimal R=0 = %.6f' % (m, acc/64, {0.0:'0.975567',1.0:'0.677308'}[m], accopt/64), flush=True)
# (2) finite-difference gradient check of the optimiser's objective
h0 = D.be*(0.3+1.0) + D.al[1]*np.sin(0.4) + D.al[2]*np.sin(0.2)
W = D.window(h0, 1); d = W['d']
rng = np.random.default_rng(0)
Z = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d)); U = expm(0.05j*(Z+Z.conj().T))
x0 = rng.normal(size=2*d*d)*0.01
from scipy.linalg import expm_frechet
rho0 = U @ W['G0'] @ U.conj().T; Cp = U @ W['C']; A = W['A']
def f(x):
    Z = (x[:d*d] + 1j*x[d*d:]).reshape(d, d); K = (Z+Z.conj().T)/2; X = 1j*K; V = expm(X)
    E = np.real(np.trace(A @ V @ rho0 @ V.conj().T)) + 2*np.real(np.trace(Cp @ V))
    Gv = 2*(A @ V @ rho0 + Cp.conj().T); M = expm_frechet(X.conj().T, Gv, compute_expm=False)
    Y = 1j*M.conj().T; Gz = (Y + Y.conj().T)/2
    return E, np.concatenate([Gz.real.ravel(), Gz.imag.ravel()])
E, g = f(x0); dx = rng.normal(size=2*d*d); h = 1e-6
fd = (f(x0+h*dx)[0] - f(x0-h*dx)[0])/(2*h)
print('gradcheck: analytic %.10e  finite-diff %.10e' % (g @ dx, fd))
# (3) R=1,2 optimisation at one q, plus random restarts
for R in (1, 2, 3):
    W = D.window(h0, R); t = time.time(); dE, U = D.opt(W); t1 = time.time()-t
    rs = []
    for s in range(2):
        Z = rng.normal(size=(W['d'],)*2) + 1j*rng.normal(size=(W['d'],)*2); U0 = expm(0.5j*(Z+Z.conj().T))
        rs.append(D.opt(W, U0)[0])
    print('R=%d dE=%.10e (%.1fs); random restarts: %s' % (R, dE, t1, ' '.join('%.10e' % v for v in rs)), flush=True)
