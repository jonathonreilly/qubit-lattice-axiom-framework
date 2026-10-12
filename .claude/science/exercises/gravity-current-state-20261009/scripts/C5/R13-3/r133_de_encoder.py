"""R13-3 (a) encoder mean and (e) dark-energy visibility under the P-T (Prony) reading.

(a) Integrate-and-fire creation clock (R12-2 S4): a site with phase phi in [0,1) advances at rate c/ln2 per
    unit time (one doubling per phase unit); at phi = 1 it inserts a neighbour and both restart at 0.
    Referee R12-2 finding 4: with UNIFORM initial phases the mean count is 2^n (1+f) (n = floor(Phi),
    f = frac(Phi)), 5.56% above 2^Phi at Phi = 3.3, 6.6.  Claim: with the stationary age density of an
    exponentially growing population, p(phi) = 2 ln2 * 2^-phi, the mean is exactly 2^Phi for every Phi.
    Low-discrepancy version: phi_i = -log2(1 - u_i/2), u_i = frac(i * golden).
(e) Prony (N = 2, 3) reconstruction at a = 1 of rho_m a^-3 + rho_DE(a) for CPL dark energy
    w(a) = w0 + wa (1-a) (DESI DR2-type values RECALLED: w0 = -0.75, wa = -0.86) and constant w,
    against the exact non-vacuum density (subtraction: rho_nc := rho_m + rho_DE, no constant part present).
"""
import numpy as np
import sympy as sp

# (a) exact mean with stationary age density
Phi = sp.symbols('Phi', positive=True)
ph = sp.symbols('phi', nonnegative=True)
for PhiV in (sp.Rational(33, 10), sp.Rational(66, 10), sp.Rational(1, 2)):
    n = sp.floor(PhiV); f = PhiV - n
    # descendants D(phi, Phi) = 2^floor(Phi + phi); integrate against p(phi)
    p = 2 * sp.log(2) * 2**(-ph)
    mean = sp.integrate(p * 2**n, (ph, 0, 1 - f)) + sp.integrate(p * 2**(n + 1), (ph, 1 - f, 1))
    unif = 2**n * (1 + f)
    print(f'(a) Phi={float(PhiV):.2f}: stationary-age mean/2^Phi = {float(sp.simplify(mean / 2**PhiV)):.12f};'
          f' uniform-phase mean/2^Phi = {float(unif / 2**PhiV):.6f}')

# low-discrepancy numerical check: N0 sites, windows
gold = (np.sqrt(5) - 1) / 2
N0, nwin = 20000, 400
idx = np.arange(N0 * nwin)
u = np.mod(idx * gold, 1.0)
phi_stat = -np.log2(1 - u / 2)
rng = np.random.default_rng(1)
phi_rand = -np.log2(1 - rng.random(idx.size) / 2)
for PhiV in (3.3, 6.6):
    for lab, phis in (('quasi-periodic, stationary', phi_stat), ('random, stationary', phi_rand)):
        D = 2.0 ** np.floor(PhiV + phis)
        W = D.reshape(nwin, N0).sum(axis=1)
        print(f'    Phi={PhiV}: {lab:28s} mean/(N0 2^Phi) = {W.mean()/(N0*2**PhiV):.6f}, window std = {W.std():.1f}')

# (e) CPL visibility
a = sp.symbols('a', positive=True)
uu = sp.symbols('u', real=True)
Om, Ode = 0.31, 0.69


def rho_tot_u(w0, wa):
    aa = sp.exp(uu)
    rde = Ode * aa**(-3 * (1 + w0 + wa)) * sp.exp(-3 * wa * (1 - aa))
    return Om * aa**-3 + rde, Om * aa**-3 + rde


def prony_val(mk, N):
    M = np.array(mk[1:2 * N + 1], dtype=float)
    Hk = np.array([[M[i + j] for j in range(N)] for i in range(N)])
    c = np.linalg.solve(Hk, -np.array([M[N + i] for i in range(N)]))
    xs = np.roots(np.concatenate(([1.0], c[::-1])))
    V = np.vander(xs, N, increasing=True).T
    wts = np.linalg.solve(V, M[:N].astype(complex))
    return float(np.real(np.sum(wts / xs))), xs


for (w0, wa, lab) in ((-0.95, 0.0, 'const w=-0.95'), (-0.99, 0.0, 'const w=-0.99'), (-1.0, 0.0, 'true Lambda'),
                      (-0.75, -0.86, 'CPL DESI-type'), (-0.85, 0.10, 'CPL non-phantom')):
    rt, rnc = rho_tot_u(w0, wa)
    mk = [None] + [float(((-1) ** k * sp.diff(rt, uu, k)).subs(uu, 0)) for k in range(1, 11)]
    rnc0 = float(rnc.subs(uu, 0)) if w0 != -1.0 else Om
    out = []
    for N in (1, 2, 3, 4, 5):
        try:
            val, xs = prony_val(mk, N)
            out.append(f'N={N}: {val/rnc0:.4f}')
        except np.linalg.LinAlgError:
            out.append(f'N={N}: singular')
    print(f'(e) {lab:16s} rho_hat/rho_nc(a=1): ' + '; '.join(out))
print('    (true Lambda row: rho_nc := rho_m only; Lambda invisible by construction, exact at N=1)')
