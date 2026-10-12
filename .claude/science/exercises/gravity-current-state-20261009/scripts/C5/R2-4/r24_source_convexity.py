"""G4: convexity test.  For ANY probability measure with a local coupling of a real test source J_mn to a
real observable h_mn, d^2/dJ^2 log Z = Var(h.J) - <seagull>, the seagull being local (polynomial in p), so the
1/p^2 (long-range) part of the source-source response W(J,J) must be >= 0 on every conserved real J.
Linearised GR (de Donder covariance; W is gauge independent on conserved J): W = (J.J - a (trJ)^2)/p^2, a = 1/2.
Checks: (1) extract a for GR (B) and the positive 4D-TT Gaussian (A); (2) W on J = theta (conformal source)
and on a random spin-2 source; (3) gamma_PPN = a/(1-a) for each; (4) bound: positivity on conserved J <=> a <= 1/3."""
import numpy as np, sympy as sp
src = open('r24_conformal_rp.py').read().split("# linearised Riemann")[0]
src = src.replace("q = sp.Integer(1)\np = [q, sp.Integer(0), sp.Integer(0), p4]",
                  "q = sp.Integer(1)\np = [sp.Rational(3,5), sp.Rational(-2,5), sp.Rational(1,3), p4]")
exec(src)
w = np.array([1.0 if m == n else 2.0 for (m, n) in pairs])
def W(Ch, J, p4v):
    C = np.array(Ch.subs(p4, p4v).evalf(), dtype=float)
    v = w*np.array([J[m, n] for (m, n) in pairs])
    return v @ C @ v
rng = np.random.default_rng(3)
for p4v in (sp.Rational(7, 10), sp.Rational(-13, 10)):
    pv = np.array([float(x.subs(p4, p4v)) for x in p]); P2 = pv @ pv
    th = np.eye(4) - np.outer(pv, pv)/P2
    X = rng.normal(size=(4, 4)); X = X + X.T
    J2 = th @ X @ th; J2 = J2 - th*np.trace(J2)/3          # conserved, spin-2 (traceless-transverse)
    Jm = th @ (np.diag([1., 0, 0, 0]) + 0*X) @ th            # conserved, mixed spin-2 + spin-0
    for name, Ch in (("B GR", CB), ("A positive 4D-TT", CA)):
        Wth, W2, Wm = W(Ch, th, p4v), W(Ch, J2, p4v), W(Ch, Jm, p4v)
        # fit a from the mixed source: W*p^2*norm = J.J - a trJ^2  (normalisation from the spin-2 source)
        norm = W2*P2/np.sum(J2*J2)
        a_fit = (np.sum(Jm*Jm) - Wm*P2/norm)/np.trace(Jm)**2
        print(f"p4={float(p4v):+.2f} {name:18s}: W(theta)*p^2/norm = {Wth*P2/norm:+.6f}   W(spin2) > 0: {W2 > 0}   "
              f"a = {a_fit:.6f}   gamma_PPN = a/(1-a) = {a_fit/(1-a_fit):.6f}")
print("positivity bound on conserved J: J.J - a(trJ)^2 >= 0 for J = theta requires 3 - 9a >= 0, a <= 1/3, gamma <= 1/2")
print("Cassini (Bertotti-Iess-Tortora 2003, recalled): gamma - 1 = (2.1 +/- 2.3)e-5  ->  a = gamma/(1+gamma) = 0.500005 +/- 0.000006")
