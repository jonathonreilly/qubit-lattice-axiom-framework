"""D1 check 1 (1D): what does soft emission do to a face kink?

Insert the exact SLAC band E(k) = sqrt(m^2 + beta k^2) (lifted zone, periodic
extension) as the dressed intermediate band, couple it to a gapless lattice
boson omega(q) = 2c|sin(q/2)| with a nearest-neighbour vertex of order n
  w_n(q) = g^2 (2|sin(q/2)|)^(2n) / (2 omega(q))  ~ |q|^(2n-1),  i.e. a = n - 1/2,
and compute the on-shell one-loop (rainbow, dressed-intermediate) self-energy
  Sigma_os(k) = int dq/2pi  w(q) / (E(k) - E(k-q) - omega(q))
near the face k = pi - delta.  Predictions (D1 report, Lemma K):
  * IR-convergent (d+2a = 2n > 2):  Sigma_os'(0+) = + s K, with
    s = beta pi / E_f and K = int w / D0^2 = 1/Z - 1  (a V-kink, opposite to E's).
    the slope correction is the regular O(delta) term; the soft non-analytic piece is |delta|^(2n-1), subleading.
  * marginal (n = 1):  [Sigma(delta)-Sigma(0)]/delta ~ C log(1/delta),
    C = s g^2 / (2 pi c (c - s)^2).
"""
import numpy as np
from scipy.integrate import quad

m, beta, c, g = 1.0, 1.0, 2.0, 1.0
Ef = np.sqrt(m**2 + beta*np.pi**2)
s = beta*np.pi/Ef


def red(k):
    return (k + np.pi) % (2*np.pi) - np.pi


def E(k):
    kr = red(k)
    return np.sqrt(m**2 + beta*kr**2)


def om(q):
    return 2*c*np.abs(np.sin(q/2))


def w(q, n):
    return g**2*(2*np.abs(np.sin(q/2)))**(2*n)/(2*om(q)) if q != 0 else 0.0


def D(k, q):
    return E(k) - E(k-q) - om(q)


def sig(k, n):
    pts = sorted(set([0.0, float(red(k - np.pi)) if abs(red(k-np.pi)) < np.pi else 0.0]))
    f = lambda q: w(q, n)/D(k, q) if q != 0 else 0.0
    val, err = quad(f, -np.pi, np.pi, points=pts, limit=2000, epsabs=1e-15, epsrel=1e-14)
    return val/(2*np.pi), err


def Kf(k, n):
    pts = sorted(set([0.0, float(red(k - np.pi))]))
    f = lambda q: w(q, n)/D(k, q)**2 if q != 0 else 0.0
    val, err = quad(f, -np.pi, np.pi, points=pts, limit=2000, epsabs=1e-15, epsrel=1e-13)
    return val/(2*np.pi)


# global stability (subsonic, no decay): max_q D(k,q) <= 0 for all k
kk = np.linspace(-np.pi, np.pi, 801)
qq = np.linspace(-np.pi, np.pi, 1601)
qq = qq[qq != 0]
Dmax = max(np.max(D(k, qq)) for k in kk)
print(f"params m={m} beta={beta} c={c} g={g};  E_f={Ef:.6f}  s=beta*pi/E_f={s:.6f}")
print(f"stability: max_(k,q!=0) D(k,q) = {Dmax:.3e}  (<0: band stable, threshold at q=0)")

for n in (2, 3):
    K = Kf(np.pi, n)
    Z = 1/(1+K)
    S0, e0 = sig(np.pi, n)
    print(f"\n--- n={n} (a={n-0.5}, d+2a={2*n}): K(face)={K:.10f}  Z={Z:.8f}  Sigma_os(face)={S0:.12f}")
    print(f"    predicted Sigma'(0+) = s*K = {s*K:.10f}")
    print("    delta        slope=[S(d)-S(0)]/d    slope - sK        (slope-sK)/d [regular O(d)]   even-check S(-d)-S(d)")
    for dl in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4]:
        Sp, _ = sig(np.pi - dl, n)
        Sm, _ = sig(np.pi + dl, n)
        sl = (Sp - S0)/dl
        print(f"    {dl:8.1e}   {sl:.10f}          {sl - s*K:+.3e}       {(sl - s*K)/dl:+.4e}        {Sm-Sp:+.1e}")

n = 1
S0, _ = sig(np.pi, n)
C = s*g**2/(2*np.pi*c*(c-s)**2)
print(f"\n--- n=1 marginal (a=1/2, d+2a=2): Sigma_os(face)={S0:.12f}; K(face) diverges (log)")
print(f"    predicted log coefficient C = s g^2/(2 pi c (c-s)^2) = {C:.8f}")
prev = None
print("    delta        slope=[S(d)-S(0)]/d      d slope / d log(1/delta)")
for dl in [1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5, 3e-6, 1e-6]:
    Sp, _ = sig(np.pi - dl, n)
    sl = (Sp - S0)/dl
    if prev is not None:
        rate = (sl - prev[1])/np.log(prev[0]/dl)
        print(f"    {dl:8.1e}   {sl:.8f}              {rate:.6f}")
    else:
        print(f"    {dl:8.1e}   {sl:.8f}")
    prev = (dl, sl)
# K(k) away from the face at marginal coupling: also log divergent -> Z = 0 everywhere
print("    K at interior k=1.0 with q cut |q|>eps (marginal => grows like log(1/eps)):")
for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
    f = lambda q: w(q, 1)/D(1.0, q)**2
    v1, _ = quad(f, -np.pi, -eps, limit=2000, epsabs=1e-14)
    v2, _ = quad(f, eps, np.pi, limit=2000, epsabs=1e-14)
    print(f"      eps={eps:.0e}: K_eps={(v1+v2)/(2*np.pi):.6f}")
