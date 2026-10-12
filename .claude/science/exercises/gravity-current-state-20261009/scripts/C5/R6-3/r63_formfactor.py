"""R6-3 (a)-(b): Fourier transforms of the sharp unit diamond D_1 and the unit truncated past cone P_1,
and the shell integrals J(M) = int_{q^2 = M} |W^(q)|^2 dmu, dmu = delta(q^2 - M) d^4q (both sheets),
signature (-+++), q = (omega, k).

D_1 = {(t,x): |x| <= t <= 1-|x|},  |D_1| = pi/24
P_1 = {(t,x): -1 <= t <= -|x|},    |P_1| = pi/3

Closed forms (derived in the report):
  |D^(omega,k)| = (8 pi/(k omega)) |F|,  F = (G(k+w; -w/2) - G(k-w; w/2))/2,
     G(beta; phi) = int_0^{1/2} u cos(phi + beta u) du = Re[e^{i phi} g_h(beta)],
     g_h(beta) = int_0^{1/2} u e^{i beta u} du.
  P^(omega,k) = (4 pi/(i k omega)) [ (gh1(k-w) - gh1(-k-w))/(2i) - e^{-i w}(sin k - k cos k)/k^2 ],
     gh1(beta) = int_0^1 r e^{i beta r} dr.
Tails (k, omega >> 1): phase-averaged forms, see report section 3.
"""
import numpy as np, sys, time

def gh(beta, h):
    """int_0^h u e^{i beta u} du, stable."""
    beta = np.asarray(beta, dtype=float)
    out = np.empty(beta.shape, dtype=complex)
    small = np.abs(beta*h) < 1e-2
    b = beta[~small]
    e = np.exp(1j*b*h)
    out[~small] = e*(h/(1j*b) + 1/b**2) - 1/b**2
    bs = beta[small]; x = 1j*bs
    # series: sum_n (i beta)^n h^{n+2}/(n! (n+2))
    s = np.zeros(bs.shape, dtype=complex); term = np.ones(bs.shape, dtype=complex); fact = 1.0
    for n in range(0, 12):
        if n > 0: fact *= n
        s += (x**n)*h**(n+2)/(fact*(n+2))
    out[small] = s
    return out

def D_abs2(w, k):
    """|D_1^(w,k)|^2, exact (closed form). w, k arrays, k>0, w != 0."""
    Gp = np.real(np.exp(-1j*w/2)*gh(k+w, 0.5))
    Gm = np.real(np.exp(1j*w/2)*gh(k-w, 0.5))
    F = 0.5*(Gp - Gm)
    return (8*np.pi*F/(k*w))**2

def D_abs2_avg(w, k):
    """phase average over the fast phase k/2 (valid for k >> 1): <F^2> = |W|^2/8."""
    bp, bm = k + w, k - w
    P = 1/(2j*bp) + 1/bp**2; Q = -1/bp**2
    W = np.exp(1j*bm/2)*P + Q - gh(bm, 0.5)
    return (8*np.pi/(k*w))**2*np.abs(W)**2/8

def P_abs2(w, k):
    """|P_1^(w,k)|^2 exact."""
    phi = (gh(k-w, 1.0) - gh(-k-w, 1.0))/(2j) - np.exp(-1j*w)*(np.sin(k) - k*np.cos(k))/k**2
    return (4*np.pi/(k*w))**2*np.abs(phi)**2

def P_abs2_avg(w, k):
    """average over the single fast phase e^{-i(k+w)}: |Phi_slow|^2 + |Phi_fast|^2."""
    bm, bp = k - w, k + w
    # gh1(beta) = e^{i beta}(1/(i beta) + 1/beta^2) - 1/beta^2 ; gh1(-bp) = e^{-i bp} p + q
    p = -1/(1j*bp) + 1/bp**2; q = -1/bp**2
    slow = (gh(bm, 1.0) - q)/(2j) - (np.exp(1j*bm)/(2j) - k*np.exp(1j*bm)/2)/k**2
    fast = (-p)/(2j) - (-1/(2j) - k/2)/k**2
    return (4*np.pi/(k*w))**2*(np.abs(slow)**2 + np.abs(fast)**2)

def quad_check(Wname, w, k, n=20000):
    """direct midpoint quadrature of the radial/time integral for checking the closed forms."""
    if Wname == 'D':
        r = (np.arange(n)+0.5)/n*0.5; dr = 0.5/n
        tint = np.where(np.abs(w) > 0, (np.exp(1j*w*(1-r)) - np.exp(1j*w*r))/(1j*w), 1-2*r)
        val = 4*np.pi*np.sum(r**2*np.sinc(k*r/np.pi)*tint)*dr
    else:
        r = (np.arange(n)+0.5)/n; dr = 1.0/n
        tint = (np.exp(-1j*w*r) - np.exp(-1j*w))/(1j*w)
        val = 4*np.pi*np.sum(r**2*np.sinc(k*r/np.pi)*tint)*dr
    return abs(val)**2

def J(M, Wname, ompeak=1.0e4, verbose=False):
    """J(M) for M<0 (timelike, m=-M, both sheets) or M>0 (spacelike).
    eta-parametrisation: timelike w = sqrt(m) cosh, k = sqrt(m) sinh, weight 4 pi m sinh^2;
                         spacelike w = sqrt(m) sinh, k = sqrt(m) cosh, weight 4 pi m cosh^2.
    exact closed form for eta < eta_c (w,k < ompeak), phase-averaged beyond."""
    m = abs(M); sm = np.sqrt(m)
    exact = D_abs2 if Wname == 'D' else P_abs2
    avg = D_abs2_avg if Wname == 'D' else P_abs2_avg
    eta_c = max(0.0, np.log(2*ompeak/sm))
    eta_max = max(eta_c, 0.5*np.log(max(m, 1e-30)) + 0.0) + 25.0
    tot = 0.0
    if eta_c > 0:
        # resolve the fast phase ~ k/2 ~ ompeak/2 at eta_c: step ~ 1/(ompeak*10)
        n = int(min(4e6, max(2e4, eta_c*ompeak*6)))
        e = np.linspace(1e-7, eta_c, n+1)
        if M < 0: w, k, wt = sm*np.cosh(e), sm*np.sinh(e), 4*np.pi*m*np.sinh(e)**2
        else:     w, k, wt = sm*np.sinh(e), sm*np.cosh(e), 4*np.pi*m*np.cosh(e)**2
        f = np.empty(n+1)
        for i0 in range(0, n+1, 500000):
            sl = slice(i0, min(n+1, i0+500000))
            f[sl] = wt[sl]*exact(w[sl], k[sl])
        tot += np.trapezoid(f, e)
    e = np.linspace(eta_c, eta_max, 40001)
    if M < 0: w, k, wt = sm*np.cosh(e), sm*np.sinh(e), 4*np.pi*m*np.sinh(e)**2
    else:     w, k, wt = sm*np.sinh(e), sm*np.cosh(e), 4*np.pi*m*np.cosh(e)**2
    if eta_c == 0:
        e[0] = max(e[0], 1e-9)
        if M < 0: w, k = sm*np.cosh(e), sm*np.sinh(e)
        else: w, k = sm*np.sinh(e), sm*np.cosh(e)
    f = wt*avg(w, k) if eta_c > 0 or sm > 2*ompeak else wt*exact(w, k)
    tot += np.trapezoid(f, e)
    return tot

if __name__ == '__main__':
    t0 = time.time()
    rng = np.random.default_rng(1)
    print("== closed forms vs direct quadrature (relative error) ==")
    for Wn in ('D', 'P'):
        errs = []
        for i in range(12):
            w = rng.uniform(-60, 60); k = rng.uniform(0.05, 60)
            ex = (D_abs2 if Wn == 'D' else P_abs2)(np.array([w]), np.array([k]))[0]
            qc = quad_check(Wn, w, k)
            errs.append(abs(ex-qc)/max(qc, 1e-30))
        print("  %s: max rel err over 12 random (w,k) = %.2e" % (Wn, max(errs)))
    print("  D at rest limit k->0,w=0: %.6f vs vol pi/24 = %.6f" % (D_abs2(np.array([1e-6]), np.array([1e-6]))[0]**0.5, np.pi/24))
    print("  P at k->0,w->0: %.6f vs vol pi/3 = %.6f" % (P_abs2(np.array([1e-5]), np.array([1e-5]))[0]**0.5, np.pi/3))
    print("== phase-averaged tail forms vs exact, averaged over a fast-phase window ==")
    for Wn in ('D', 'P'):
        for (w0, k0) in [(3000.5, 3000.0), (5000.0, 4990.0), (2000.0, 2010.0), (4000.0, 3000.0)]:
            dk = np.linspace(0, 4*np.pi, 4001)
            ww, kk = w0 + dk, k0 + dk   # shift the common fast phase, keep beta_- fixed
            ex = np.mean((D_abs2 if Wn == 'D' else P_abs2)(ww, kk))
            av = np.mean((D_abs2_avg if Wn == 'D' else P_abs2_avg)(ww, kk))
            print("  %s (w,k)=(%.1f,%.1f): <exact>=%.6e  avg-form=%.6e  ratio=%.5f" % (Wn, w0, k0, ex, av, av/ex))
    print("elapsed %.1f s" % (time.time()-t0))
