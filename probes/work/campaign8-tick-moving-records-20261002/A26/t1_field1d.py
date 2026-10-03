"""A26 t1_field1d: A18's 1D time-symmetric brickwork (one excitation) coupled to a STATIC field configuration through
FIXED lapse and frame factors (supplied toy; nothing adopted).  Adapted from A18 lapse1d.py.
Field: U(site); lapse N = 1 - U on one-site terms; spatial metric h = 2U (A23 D16), frame e = 1 - h/2 on bonds.
Bond-factor rules (bond j, j+1):
  field-mean : Nb * eb, Nb = (N_j + N_j+1)/2, eb = 1 - (h_j + h_j+1)/4     (the fixed coupling of task 1)
  field-min  : min(N_j, N_j+1) * eb
  field-geo  : sqrt(N_j N_j+1) * sqrt(e_j e_j+1)
  lapse      : Nb only (A18 'OR'),  frame : eb only,  and : N_j N_j+1 (A18 'AND', chosen product)
Two-site mass (staggered angles th0 +- delta): 'os' = whole angle x bond factor; 'st' = Nb (th0 eb +- delta).
Parts: b Bloch facts; m massless delay through a bump; f free fall (one-site vs two-site)."""
import os, sys, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np

PARTS = sys.argv[1] if len(sys.argv) > 1 else "bmf"


def bloch(K, the, tho, mN):
    ce, se, co, so = np.cos(the / 2), np.sin(the / 2), np.cos(tho), np.sin(tho)
    Eh = np.array([[ce, -1j * se], [-1j * se, ce]])
    O = np.array([[co, -1j * so * np.exp(-1j * K)], [-1j * so * np.exp(1j * K), co]])
    Mh = np.diag([np.exp(-0.5j * mN), np.exp(0.5j * mN)])
    return Mh @ Eh @ O @ Eh @ Mh


def bands(K, the, tho, mN):
    w, v = np.linalg.eig(bloch(K, the, tho, mN))
    om = -np.angle(w)
    i = np.argmax(om)
    vec = v[:, i] * np.exp(-1j * np.angle(v[0, i]))
    return om[i], vec / np.linalg.norm(vec)


def packet(Nc, c0, K0, sig, the, tho, mN):
    Ks = 2 * np.pi * np.arange(Nc) / Nc
    dK = np.angle(np.exp(1j * (Ks - K0)))
    g = np.exp(-0.5 * (dK * sig) ** 2) * np.exp(-1j * Ks * c0)
    keep = np.abs(g) > 1e-12
    A = np.zeros(Nc, complex); B = np.zeros(Nc, complex)
    cs = np.arange(Nc)
    for K, gk in zip(Ks[keep], g[keep]):
        _, vec = bands(K, the, tho, mN)
        ph = np.exp(1j * K * cs)
        A += gk * vec[0] * ph; B += gk * vec[1] * ph
    psi = np.empty(2 * Nc, complex); psi[0::2] = A; psi[1::2] = B
    return psi / np.linalg.norm(psi)


GF = float(os.environ.get("A26_GF", "1.0"))      # field's spatial strength: h = 2 GF U (A23 D16 gives GF = 1)


def bond_factor(U, rule):
    N = 1 - U; h = 2 * GF * U; e = 1 - h / 2
    Nn, en = np.roll(N, -1), np.roll(e, -1)
    Nb = 0.5 * (N + Nn); eb = 0.5 * (e + en)       # = 1 - (h + h')/4
    return {'field-mean': Nb * eb, 'field-min': np.minimum(N, Nn) * eb, 'field-geo': np.sqrt(N * Nn * e * en),
            'lapse': Nb, 'frame': eb, 'and': N * Nn}[rule], Nb, eb


def make_stepper(U, th0, delta, mu, rule, mode='os'):
    amp = rule.endswith('-amp')
    B, Nb, eb = bond_factor(U, rule.replace('-amp', ''))
    par = np.where(np.arange(U.size) % 2 == 0, 1.0, -1.0)      # even bond (2c,2c+1): +1 ; odd: -1
    if amp:                                                       # amplitude coupling: sin(angle) = B sin(th0)
        ang = np.arcsin(B * np.sin(th0 + par * delta))
    elif mode == 'os':
        ang = (th0 + par * delta) * B
    else:
        ang = Nb * (th0 * eb + par * delta)
    thE, thO = ang[0::2], ang[1::2]
    cE, sE, cO, sO = np.cos(thE / 2), np.sin(thE / 2), np.cos(thO), np.sin(thO)
    eps = par
    mh = np.exp(-0.5j * mu * (1 - U) * eps)                   # one-site mass x lapse

    def step(psi):
        psi = psi * mh
        a, b = psi[0::2], psi[1::2]
        a, b = cE * a - 1j * sE * b, -1j * sE * a + cE * b
        a2 = np.roll(a, -1)
        b, a2 = cO * b - 1j * sO * a2, -1j * sO * b + cO * a2
        a = np.roll(a2, 1)
        a, b = cE * a - 1j * sE * b, -1j * sE * a + cE * b
        out = np.empty_like(psi); out[0::2] = a; out[1::2] = b
        return out * mh
    return step


def cellprob(psi):
    p = np.abs(psi) ** 2
    return p[0::2] + p[1::2]


def uniform_om(K, U, th0, delta, mu, rule, mode):
    """quasi-energy of the upper band in a uniform field U under the given coupling"""
    B, Nb, eb = [np.atleast_1d(x)[0] for x in bond_factor(np.array([U, U]), rule)]
    if mode == 'os':
        the, tho = (th0 + delta) * B, (th0 - delta) * B
    else:
        the, tho = Nb * (th0 * eb + delta), Nb * (th0 * eb - delta)
    return bands(K, the, tho, mu * (1 - U))[0]


if "b" in PARTS:
    print("(b) Bloch facts, uniform U, at the cone K = pi")
    for U in (0.0, 0.05, 0.1):
        r1 = uniform_om(np.pi, U, 0.3, 0.0, 0.05, 'field-mean', 'os') / (0.05 * (1 - U))
        r2 = uniform_om(np.pi, U, 0.3, 0.025, 0.0, 'field-mean', 'os') / (0.05 * (1 - U) ** 2)
        r3 = uniform_om(np.pi, U, 0.3, 0.025, 0.0, 'field-mean', 'st') / (0.05 * (1 - U))
        print("   U=%.2f: one-site rest omega/(mu N) = %.12f ; two-site os omega/(2 delta N e) = %.12f ; "
              "two-site st omega/(2 delta N) = %.12f" % (U, r1, r2, r3))

if "m" in PARTS:
    print("(m) massless delay through U = U0 exp(-((c-1500)/80)^2): N = 1-U, h = 2U")
    Nc, c0, cd, sig, q0 = 3000, 500, 2300, 50.0, 0.12
    cells = np.arange(Nc)
    U0 = float(os.environ.get("A26_U0", "0.05"))
    Ucell = U0 * np.exp(-((cells - 1500) / 80.0) ** 2)
    Usite = np.repeat(Ucell, 2)
    rules = os.environ.get("A26_RULES", "field-mean,field-min,field-geo,lapse,frame,and").split(",")
    for th0 in [float(x) for x in os.environ.get("A26_TH", "0.2").split(",")]:
        Tmax = int(2 * (cd - c0) / np.sin(th0)) + 400
        def arrival(Us, rule):
            step = make_stepper(Us, th0, 0.0, 0.0, rule)
            psi = packet(Nc, c0, np.pi + q0, sig, th0, th0, 0.0)
            prev = 0.0
            for t in range(1, Tmax + 1):
                psi = step(psi)
                if t % 4 == 0:
                    f = cellprob(psi)[cd:].sum()
                    if f >= 0.5 > prev:
                        return t - 4 + 4 * (0.5 - prev) / (f - prev)
                    prev = f
            return np.nan
        t0 = arrival(np.zeros(2 * Nc), 'lapse')
        om0, _ = bands(np.pi + q0, th0, th0, 0.0)
        vinf = None
        res = {}
        for rule in rules:
            dt = arrival(Usite, rule) - t0
            # exact-dispersion eikonal: omega conserved, local K, local group velocity
            Bc = bond_factor(Usite, rule.replace('-amp', ''))[0]
            if rule.endswith('-amp'):
                thE, thO = np.arcsin(Bc[0::2] * np.sin(th0)), np.arcsin(Bc[1::2] * np.sin(th0))
            else:
                thE, thO = th0 * Bc[0::2], th0 * Bc[1::2]
            cosK = (np.cos(thE) * np.cos(thO) - np.cos(om0)) / (np.sin(thE) * np.sin(thO))
            K = 2 * np.pi - np.arccos(np.clip(cosK, -1, 1))
            v = -np.sin(thE) * np.sin(thO) * np.sin(K) / np.sin(om0)
            vinf = -np.sin(th0) ** 2 * np.sin(np.pi + q0) / np.sin(om0)
            pred = np.sum(1 / v - 1 / vinf)
            small = np.sum(1 / Bc[0::2] - 1) / np.sin(th0)            # small-dose metric: n = 1/B
            res[rule] = dt
            print("   th0=%.2f U0=%.3f %-10s delay %8.3f cycles ; exact-dispersion eikonal %8.3f (ratio %.5f) ;"
                  " small-dose metric %8.3f" % (th0, U0, rule, dt, pred, dt / pred, small))
        if 'lapse' in res:
            for rule in rules:
                print("      %-10s delay / lapse-only delay = %.4f   (=> 1+gamma for light)" % (rule, res[rule] / res['lapse']))

if "f" in PARTS:
    print("(f) free fall from rest in a lapse gradient: U = g (c - c0), N = 1 - U, h = 2U ; g = 1e-4 per cell")
    Nc, c0, g, T = int(os.environ.get("A26_NC", "2000")), 1000, 1e-4, int(os.environ.get("A26_TF", "1500"))
    sig = float(os.environ.get("A26_SIG", "150"))
    cells = np.arange(Nc)
    Usite = np.repeat(g * (cells - c0), 2)
    th0 = 0.3
    c2g = np.sin(th0) ** 2 * g
    print("   packet width sigma = %.0f cells, T = %d cycles" % (sig, T))
    out = {}
    for label, delta, mu, mode in (("one-site mu=0.05", 0.0, 0.05, 'os'), ("one-site mu=0.10", 0.0, 0.10, 'os'),
                                   ("two-site os d=0.025", 0.025, 0.0, 'os'), ("two-site st d=0.025", 0.025, 0.0, 'st')):
        step = make_stepper(Usite, th0, delta, mu, 'field-mean', mode)
        psi = packet(Nc, c0, np.pi, sig, th0 + delta, th0 - delta, mu)
        ts, xs = [], []
        for t in range(T + 1):
            if t % 10 == 0:
                p = cellprob(psi); ts.append(t); xs.append(np.sum(cells * p))
            psi = step(psi)
        a_meas = 2 * np.polyfit(np.array(ts, float), np.array(xs), 2)[0]
        dU, dK = 1e-5, 1e-3
        om = lambda K, U: uniform_om(K, U, th0, delta, mu, 'field-mean', mode)
        domdU = (om(np.pi, dU) - om(np.pi, -dU)) / (2 * dU)
        d2 = (om(np.pi + dK, 0) - 2 * om(np.pi, 0) + om(np.pi - dK, 0)) / dK ** 2
        a_sc = -domdU * g * d2
        out[label] = a_meas
        print("   %-22s a = %.4e ; semiclassical %.4e (ratio %.4f) ; a/(c^2 g) = %.4f" % (label, a_meas, a_sc, a_meas / a_sc, a_meas / c2g))
    ref = out["one-site mu=0.05"]
    print("   universality ratios vs one-site mu=0.05: " + "; ".join("%s %.4f" % (k, v / ref) for k, v in out.items()))
