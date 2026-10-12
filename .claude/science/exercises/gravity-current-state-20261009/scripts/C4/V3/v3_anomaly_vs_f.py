"""V3: is mu_E^anom = 0 reachable by choosing a different local free momentum symbol f (free theory: any odd f(k) is conserved)?
Scalar, E channel, RN L1 normalisation (velocity eps/2 * hhat * f), family f_a(k) = sin k + a sin 2k (slope at k=0 is 1+2a).
Exact: mu = 1/2 d2/deps2 <omega(Phi^{-1} k)> = 1/2 <omega * d2J/deps2> with d2J = (f f')' terms; computed by flow + finite differences."""
import numpy as np
from scipy.optimize import brentq
def flow1(k, e, f, n=100):
    x = k.copy(); h = 1.0/n
    for _ in range(n):
        a1 = -e*f(x); a2 = -e*f(x+h/2*a1); a3 = -e*f(x+h/2*a2); a4 = -e*f(x+h*a3)
        x = x + h/6*(a1+2*a2+2*a3+a4)
    return x
L = 64; k = 2*np.pi*(np.arange(L)+0.5)/L
def mu(a, m, de=0.02):
    f = lambda x: 0.5*(np.sin(x) + a*np.sin(2*x))
    def E(e):
        qx = flow1(k, e, f); qy = flow1(k, -e, f)
        QX, QY, QZ = np.meshgrid(qx, qy, k, indexing='ij')
        return 0.5*np.sqrt(m*m + 4*np.sin(QX/2)**2 + 4*np.sin(QY/2)**2 + 4*np.sin(QZ/2)**2).mean()
    v = {e: E(e) for e in [-de, -de/2, 0, de/2, de]}
    D = lambda e: (v[e]+v[-e]-2*v[0])/e**2
    return (4*D(de/2)-D(de))/3
for m in [0.5, 1.0]:
    for a in [-0.4, -0.2, 0.0, 0.2, 0.4]:
        print(f'm={m} a={a:+.1f}: mu_E^anom = {mu(a, m):+.6e}')
    try:
        r = brentq(lambda a: mu(a, m), -0.45, 0.45)
        print(f'  root a* = {r:+.5f} (slope at k=0: {1+2*r:.4f}) -> one-parameter tuning of the transported momentum')
    except ValueError as ex:
        print('  no sign change in [-0.45,0.45]')
