"""R17-10: fast-only (u = s^2 = 1 a.e. incl. box) one-variable forms, all from the five-moment U+E1 rows (R17-4, refereed):
  x(t) = t<g>_t (= -t Phi'/Phi), dlam = t^{-1/2} e^{-t m^2} Phi^3 dt, c7 = 1/Gamma(7/2), s = m^2 t
  T2g   = c7 (5/16) int dlam (2x^3 - x^2)                                   [no IBP]
  Eg    = c7 (5/32) int dlam (-3x^3 + 5.5x^2 - 1.5x - s(x^2 - x))           [one IBP in t]
  face1 = c7 (1/128) int dlam (-63.5x^3 + 98.75x^2 - 26.25x + s(20x - 25.5x^2) - s^2 x)   [two IBPs]
Lagrangian certificate: face1 - alpha Eg - beta T2g = c7 int dlam x P(x, s), with A = 5 alpha/32, B = 5 beta/16:
  P(x,s) = q(x) + s[(20/128 - A) + (A - 25.5/128) x] - s^2/128,  q(x) = (-63.5/128 + 3A - 2B) x^2 + (98.75/128 - 5.5A + B) x + (-26.25/128 + 1.5A).
If P < 0 wherever (x(t), m^2 t) can lie, then at the axis zeros face1 < 0, i.e. <K6/e^7> > 0."""
import numpy as np
from math import gamma
L = 50; smin = 0.15; lev = np.linspace(smin, np.pi, L)
def check(M, b, m, A, B, NU=6000):
    u = np.linspace(-16.0, np.log(80.0/(m*m)) + 2, NU); t = np.exp(u); du = u[1]-u[0]
    xg, wg = np.polynomial.legendre.leggauss(400); kb = 0.5*b*(xg+1); wb = 0.5*b*wg
    mom = lambda p: (np.exp(-np.outer(t, kb*kb))@(wb*kb**p) + np.exp(-np.outer(t, lev**2))@(M*lev**p))/np.pi
    E0, F2, F4, F6 = mom(0), mom(2), mom(4), mom(6)
    w7 = t*du*t**2.5*np.exp(-t*m*m)/gamma(3.5); w5 = t*du*t**1.5*np.exp(-t*m*m)/gamma(2.5)
    a6 = w7@(F6*E0*E0); a42 = w7@(F4*F2*E0); a222 = w7@F2**3; b4 = w5@(F4*E0*E0); b22 = w5@(F2*F2*E0)
    rows = dict(Eg=(5/16)*(a42-a222) - (b4-b22)/16, T2g=(5/8)*a222 - b22/8, face1=-a6/128 + 45*a42/128 - 5*a222/16 - 3*b4/64 + b22/64)
    X = t*F2/E0; s = m*m*t; dl = t*du*t**-0.5*np.exp(-t*m*m)*E0**3; c7 = 1/gamma(3.5)
    fast = dict(T2g=c7*5/16*np.sum(dl*(2*X**3 - X**2)), Eg=c7*5/32*np.sum(dl*(-3*X**3 + 5.5*X**2 - 1.5*X - s*(X*X - X))),
                face1=c7/128*np.sum(dl*(-63.5*X**3 + 98.75*X**2 - 26.25*X + s*(20*X - 25.5*X**2) - s*s*X)))
    q = lambda X: (-63.5/128 + 3*A - 2*B)*X**2 + (98.75/128 - 5.5*A + B)*X + (-26.25/128 + 1.5*A)
    P = q(X) + s*((20/128 - A) + (A - 25.5/128)*X) - s*s/128
    lag = rows['face1'] - (32*A/5)*rows['Eg'] - (16*B/5)*rows['T2g']
    return rows, fast, lag, c7*np.sum(dl*X*P), P.max(), X
if __name__ == '__main__':
    A, B = 0.1340, -0.040
    for fn, b, m in [('relaxK6_ge_m0.01_b0.30_hi0.80.npy', 0.3, 0.01), ('relaxK6_ge_m0.01_b0.60_hi0.65.npy', 0.6, 0.01), ('relaxK6_ge_m0.1_b0.20_hi0.95.npy', 0.2, 0.1)]:
        M = np.load(fn)[:L]
        rows, fast, lag, lagP, Pmax, X = check(M, b, m, A, B)
        print('%s (all-fast version): ' % fn + ' '.join('%s %+.8e/%+.8e' % (k, rows[k], fast[k]) for k in rows) + ' | Lagrangian %+.6e = int x P %+.6e | max_t P(x(t),s) %+.3e' % (lag, lagP, Pmax))
    rng = np.random.default_rng(1)
    for trial in range(6):   # random all-fast measures, NOT tied to axis zeros: identity checks
        M = rng.exponential(1.0, L)*(rng.uniform(size=L) < 0.3); b = rng.uniform(0.15, 1.2); M *= (np.pi - b)/M.sum(); m = rng.choice([0.01, 0.03, 0.1])
        rows, fast, lag, lagP, Pmax, X = check(M, b, m, A, B)
        print('random fast b=%.2f m=%.2f: ' % (b, m) + ' '.join('%s diff %.1e' % (k, abs(rows[k]-fast[k])) for k in rows) + ' | face1 %+.3e  Lagrangian %+.3e  max P %+.3e' % (rows['face1'], lag, Pmax))
