# Row 970 (gap-direction2-max). GUIDE arithmetic guard for three hand formulas. Not a proof step.
# Criteria written before the run:
#  C1 (Proposition ROTOR): Var(cos theta) under e^(h cos theta) on S^2 equals 1/h^2 - 1/sinh^2 h, and
#      2 Var - Q = -(2/rho^2) h^2/sinh^2 h, relative error below 1e-6 at h in {0.3, 1, 3, 10}.
#  C2 (Proposition TIE): (b) P_{0,t} tanh(a.) = tanh(a.) at 5 points, abs error below 1e-6;
#      (d) kap_min := a^2 (3 M5/M3 - 2) equals the value from the three expectations computed directly under the
#      mixture density, rel error below 1e-6, and kap_min >= a^2/4, for a in {1, 3}, c = 0.1, t in {0, 0.05, 0.09}.
#  C3 (Identity MM): two-point model, J = (1/2, 1/2) on {+a, -a}, J' = (p, 1-p): D(mu | nu) equals
#      (1/2) int_0^c E_{J'} |E_{J'}[q|phi_t] - E_J[q|phi_t]|^2 dt, rel error below 1e-4, for (a, c, p) in a small grid.
# A failure of any criterion means an algebra error in the note (or in this script): report it, do not tune.
import numpy as np, sys, resource
def trap(y, x): return np.trapezoid(y, x)
ok = True
# C1
th = np.linspace(0.0, np.pi, 200001)
for h in (0.3, 1.0, 3.0, 10.0):
    w = np.exp(h*np.cos(th))*np.sin(th); Z = trap(w, th)
    m1 = trap(w*np.cos(th), th)/Z; m2 = trap(w*np.cos(th)**2, th)/Z
    var = m2 - m1**2; f = 1/h**2 - 1/np.sinh(h)**2
    rho = 1.0; R = h/rho
    lhs = 2*R*R*var - 2/rho**2; rhs = -(2/rho**2)*h*h/np.sinh(h)**2
    e1 = abs(var-f)/f; e2 = abs(lhs-rhs)/abs(rhs)
    print(f"C1 h={h}: var={var:.8f} formula={f:.8f} relerr={e1:.1e}; 2Var-Q={lhs:.8f} formula={rhs:.8f} relerr={e2:.1e}")
    ok &= (e1 < 1e-6 and e2 < 1e-6)
# C2
c = 0.1
for a in (1.0, 3.0):
    for t in (0.0, 0.05, 0.09):
        r = c - t
        phi = np.linspace(-40/a - 10*np.sqrt(r), 40/a + 10*np.sqrt(r), 800001)
        dens = np.cosh(a*phi)*np.exp(-phi**2/(2*r)); dens /= trap(dens, phi)
        G1 = a/np.cosh(a*phi)**2; G2 = -2*a*a*np.tanh(a*phi)/np.cosh(a*phi)**2
        lhs = 2*trap(dens*a*a/np.cosh(a*phi)**2*G1**2, phi)
        e_g1 = trap(dens*G1**2, phi); e_g2 = trap(dens*G2**2, phi)
        kap_direct = (lhs - e_g2)/(2*e_g1)
        u = a*phi; A = a*a*r
        M3 = trap(np.exp(-u*u/(2*A))/np.cosh(u)**3, u); M5 = trap(np.exp(-u*u/(2*A))/np.cosh(u)**5, u)
        kap_formula = a*a*(3*M5/M3 - 2)
        e = abs(kap_direct-kap_formula)/kap_formula
        print(f"C2d a={a} t={t}: kap_direct={kap_direct:.8f} kap_formula={kap_formula:.8f} relerr={e:.1e} a^2/4={a*a/4:.4f} M5/M3={M5/M3:.6f}")
        ok &= (e < 1e-6 and kap_formula >= a*a/4 - 1e-9)
    # (b): P_{0,t} G at points, t = 0.05
    t = 0.05
    for x0 in (-0.7, -0.2, 0.0, 0.3, 1.1):
        z = np.linspace(-12*np.sqrt(t), 12*np.sqrt(t), 400001)
        g = np.exp(-z*z/(2*t))
        num = trap(g*np.cosh(a*(x0+z))*np.tanh(a*(x0+z)), z); den = trap(g*np.cosh(a*(x0+z)), z)
        e = abs(num/den - np.tanh(a*x0)); print(f"C2b a={a} phi={x0}: P G={num/den:.9f} tanh={np.tanh(a*x0):.9f} abserr={e:.1e}")
        ok &= (e < 1e-6)
# C3
def gauss(x, mu, v): return np.exp(-(x-mu)**2/(2*v))/np.sqrt(2*np.pi*v)
for (a, c, p) in ((1.0, 0.1, 0.8), (3.0, 0.1, 0.8), (3.0, 0.3, 0.95), (6.0, 0.1, 0.6)):
    y = np.linspace(-a*c - 14*np.sqrt(c), a*c + 14*np.sqrt(c), 400001)
    mu = p*gauss(y, a*c, c) + (1-p)*gauss(y, -a*c, c); nu = 0.5*gauss(y, a*c, c) + 0.5*gauss(y, -a*c, c)
    D = trap(mu*np.log(mu/nu), y)
    ts = np.linspace(0.0, c, 2001)[:-1] + c/4000.0   # midpoints
    lam = 0.5*np.log(p/(1-p)); acc = 0.0
    for t in ts:
        r = c - t
        ph = np.linspace(-a*r - 14*np.sqrt(r), a*r + 14*np.sqrt(r), 20001)
        lp = p*gauss(ph, a*r, r) + (1-p)*gauss(ph, -a*r, r)
        d = a*np.tanh(a*ph + lam) - a*np.tanh(a*ph)
        acc += trap(lp*d*d, ph)*(c/2000.0)
    rhs = 0.5*acc; e = abs(D-rhs)/D
    print(f"C3 a={a} c={c} p={p}: D={D:.8f} MM={rhs:.8f} relerr={e:.1e}")
    ok &= (e < 1e-4)
print("peak RSS MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
print("ALL CRITERIA PASS" if ok else "SOME CRITERION FAILED")
