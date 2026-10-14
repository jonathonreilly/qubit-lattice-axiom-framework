"""F6 library: one-loop Higgs mass^2 Sigma_H(P = 0; t) on the root's SF-strained law (F1's law: B1, Psym, U = 1), lattice units a = 1.

Edges (root R18-9, refined, vR18-9:11): scalar edge G_w(b_s, w = pi - b_s) = SymG(b_s) [rR19-12:73; R18-5 content4.py:7-11],
  eps_s^2 = m^2 + sum_j h_s(k_j)^2  (h_s = k on the box |k| <= b_s, h_s' = 1 - sstep((|k|-b_s)/(pi-b_s)) beyond)  -- separable;
  photon Gph(2.9435) = SymG(2.9435).h (r1934_lib.py:113-119; F1);  Dirac D1(b_f, r) (dirac.py), F1's non-separable SF flow.
SF (registered strain, rR19-15:127-138): each band strained by its own flow, v = (t/2) diag(1,-1,0) grad(E^2/2).
  scalar: p_j = h_s h_s'(k_j)  (separable -> per-axis 1D flows, identical in form to F1's photon flow flowG1).
  photon: p_j = d d'(q_j)  (F1).   Dirac: p = s s' + M W' (F1 flowF; B1 mflow = 0.01, B2 mflow = 0).
Strained scalar operator K_t(q) = sum_j G_j(q_j), G_j = h_s(phi^s_j(q_j))^2.  A 1x1 (per component) operator equals its symbol,
  so the SF spectrum fixes the scalar lift uniquely (no F3-type dressing freedom); every hop is axial, so the shortest gauge path
  is unique (F4's families coincide).  Minimal coupling by divided differences (R8-5/R13-7/R19-34/F1 convention):
  V_j(0,q) = [G_j(q_j) - G_j(0)]/d_j(q_j),  seagull T_jj(0;q,-q) = [G_j(q_j) + G_j(-q_j) - 2 G_j(0)]/(2 d_j^2) = G_j/d_j^2,
  T_jk = 0 (j != k; axial hops only), temporal vertex Q0 and seagull 1 (continuum time).  Ward: sum_j d_j V_j = K(q) - K(0).
Loop 1 (U(1), Feynman gauge, P = 0, per e^2; Q0 integrated analytically):
  Sig_g/e^2 = < sum_j T_j/(2 Om) + E/(2 Om (Om+E)) - sum_j V_j^2 /(2 Om E (Om+E)) >,   Om^2 = sum_j d_j^2,  E^2 = m^2 + K.
  [reduces to R19-31's 4 G_gam - G_s for the NN scalar + NN photon under H-cov; checked in f6_controls]
  gauge-parameter part (covariant gauge, proved from the two Ward identities):
  Sig_xi/e^2 = (1 - xi) (-m^2) < 1/(4 Om^3) - m^2 (E + 2 Om)/(4 E Om^3 (E + Om)^2) >   (vanishes identically at m = 0).
Loop 2: SU(2)xU(1) on the same vector edge: one-loop scalar self-energy carries T^a T^a = C2 in both diagrams, so
  Sig = [C2(SU2) g^2 + Y^2 g'^2] x Sig_g/e^2 = [(3/4) g^2 + (1/4) g'^2] Sig_g/e^2 (doublet, Y = 1/2).
Loop 3 (top Yukawa, vectorlike D1 Dirac convention of the root, m_t = y_t h/sqrt2, N_c colours, e_vac = -2<E> per field):
  Sig_Y = -N_c y_t^2 < c^2/E^3 >  at the flowed momenta (branch Y-a: flow is a law datum at mflow), propagator mass 0.
Loop 4 (Higgs quartic V = lam (H^dag H)^2, 4 real components on the scalar edge): Sig_lam = 6 lam G_s,  G_s = <1/(2 eps_s)>.
< . > = BZ average d^3q/(2 pi)^3, done on [0, pi]^3 (integrands even in each q_j) with R19-34's composite GL panels.
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch'))
from f1_lib import Ferm, Phot, flowF, flowG1, ROOT, ROOT0, CPH
from r1934_lib import panels

BS = 2.526103698      # R18-9 refined root scalar edge b_s (vR18-9:11; rR19-12:21,73)
BS0 = 2.590035        # R19-11 0+ root scalar edge (rR19-11:34)


def mkgrid(bs, n, hm, mph, extra=()):
    br = [bs, CPH] + [CPH + i*(np.pi - CPH)/mph for i in range(1, mph)] + [bs + i*(np.pi - bs)/6 for i in range(1, 6)] + list(extra)
    return panels(br, n, hm)


def sym1(L, x, sgn, t, nrk):
    """1D strained symbol h(phi_t(x)) of a separable SymG-type edge along an axis with sign sgn (+1 x, -1 y, 0 z)."""
    return L.d(flowG1(L, x, sgn, t, nrk))


def sig_gauge(S, G, x, w, t, m=0.0, sflow='own', gflow='own', nrk=6, chunk=None, parts=False, hcov=None, xi=False):
    """Sig_g/e^2 at P = 0 on the strained law.  S: scalar edge (Phot-like object with .d = h_s, .p1 = h_s h_s'),
    G: photon edge.  sflow/gflow: 'own' (own SF flow), 'none' (unstrained), 'phot' (scalar on the photon's flow) / 'scal'
    (photon on the scalar's flow).  hcov: None, or ('nn', h) = R19-31's H-cov law (NN scalar 4 sin^2, NN photon 2 sin, l = (e^h, e^-h, 1)).
    xi=True returns the gauge-parameter coefficient < 1/(4 Om^3) - m^2 (E + 2 Om)/(4 E Om^3 (E+Om)^2) > times (-m^2) instead."""
    N = len(x)
    if hcov is not None:
        h = hcov[1]; l = (np.exp(h), np.exp(-h), 1.0)
        Gs = [4*np.sin(x/2)**2/l[j]**2 for j in range(3)]
        dg = [2*np.sin(x/2)/l[j] for j in range(3)]
    else:
        def flowed(L, mode, sgn, own, other):
            if mode == 'none' or sgn == 0:
                return L.d(x)
            if mode == 'own':
                return L.d(flowG1(L, x, sgn, t, nrk))
            # flowed by the other edge's flow
            return L.d(flowG1(other, x, sgn, t, nrk))
        hs = [flowed(S, sflow if sflow != 'phot' else 'other', s_, S, G) for s_ in (+1, -1, 0)]
        dg = [flowed(G, gflow if gflow != 'scal' else 'other', s_, G, S) for s_ in (+1, -1, 0)]
        Gs = [hh*hh for hh in hs]
    A = [Gs[j]/dg[j]**2 for j in range(3)]           # seagull T_j
    B = [Gs[j]**2/dg[j]**2 for j in range(3)]        # V_j^2
    if chunk is None:
        chunk = max(1, int(1.2e6/(N*N)))
    tad = 0.0; tmp = 0.0; exch = 0.0; xis = 0.0
    for i0 in range(0, N, chunk):
        sl = slice(i0, min(N, i0 + chunk))
        ww = w[:, None, None]*w[None, :, None]*w[sl][None, None, :]
        K = Gs[0][:, None, None] + Gs[1][None, :, None] + Gs[2][sl][None, None, :]
        Om = np.sqrt(dg[0][:, None, None]**2 + dg[1][None, :, None]**2 + dg[2][sl][None, None, :]**2)
        E = np.sqrt(m*m + K)
        if xi:
            xis += float((ww*(-m*m)*(1/(4*Om**3) - m*m*(E + 2*Om)/(4*E*Om**3*(E + Om)**2))).sum())
            continue
        At = A[0][:, None, None] + A[1][None, :, None] + A[2][sl][None, None, :]
        Bt = B[0][:, None, None] + B[1][None, :, None] + B[2][sl][None, None, :]
        tad += float((ww*At/(2*Om)).sum())
        tmp += float((ww*E/(2*Om*(Om + E))).sum())
        exch += float((ww*Bt/(2*Om*E*(Om + E))).sum())
    if xi:
        return xis
    tot = tad + tmp - exch
    if parts:
        return tot, tad, tmp, -exch
    return tot


def g_scalar(S, x, w, t, m=0.0, nrk=6, chunk=None):
    """G_s = <1/(2 eps_s)> on the SF-strained scalar edge (loop 4 per 6 lam)."""
    N = len(x)
    hs = [S.d(flowG1(S, x, s_, t, nrk)) if s_ else S.d(x) for s_ in (+1, -1, 0)]
    Gs = [hh*hh for hh in hs]
    if chunk is None:
        chunk = max(1, int(2e6/(N*N)))
    tot = 0.0
    for i0 in range(0, N, chunk):
        sl = slice(i0, min(N, i0 + chunk))
        ww = w[:, None, None]*w[None, :, None]*w[sl][None, None, :]
        eps = np.sqrt(m*m + Gs[0][:, None, None] + Gs[1][None, :, None] + Gs[2][sl][None, None, :])
        tot += float((ww/(2*eps)).sum())
    return tot


def yuk(F, x, w, t, mprop=0.0, nrk=4, chunk=None, dress=None):
    """Y-a: returns (Y, C):  Y = -<c^2/E^3>  (Sigma_Y per N_c y_t^2) and C = -2<M/E> (vacuum condensate d e_vac/dm per field,
    whose t-Hessian x N_c y_t/sqrt2 is the strain-dependent Higgs TADPOLE) on the SF-strained D1 edge; flow mass = F.mflow.
    dress=('G1'|'G2') returns instead the t = 0 responses to F3's D-H rotation (f3_lib.py:3-8; d/d eps (c, M) = 2 (f M, -f.c)):
    dY/deps = -4 < M (f.c)/E^3 >,   dC/deps = +4 < (f.c)/E >   (Hessian shift = 2 a x response at eps = a t^2)."""
    N = len(x)
    if chunk is None:
        chunk = max(1, int(2.5e5/(N*N)))
    totY = 0.0; totC = 0.0
    X = x[:, None, None]; Y = x[None, :, None]
    for i0 in range(0, N, chunk):
        sl = slice(i0, min(N, i0 + chunk))
        Z = x[sl][None, None, :]
        ww = w[:, None, None]*w[None, :, None]*w[sl][None, None, :]
        Wz = F.W(Z)
        if t != 0.0:
            fx_, fy_ = flowF(F, X + 0*Y + 0*Z, Y + 0*X + 0*Z, Wz, t, nrk)
        else:
            fx_, fy_ = X + 0*Y + 0*Z, Y + 0*X + 0*Z
        cx, cy, cz = F.s(fx_), F.s(fy_), F.s(Z) + 0*fx_
        M = mprop + F.W(fx_) + F.W(fy_) + Wz
        c2 = cx*cx + cy*cy + cz*cz
        E = np.sqrt(c2 + M*M)
        if dress is None:
            totY += float((ww*(-c2/E**3)).sum())
            totC += float((ww*(-2*M/E)).sum())
        else:
            if dress == 'G1':
                f = (np.sin(fx_), np.sin(fy_), np.sin(Z) + 0*fx_)
            elif dress == 'G2':
                ccx, ccy, ccz = np.cos(fx_), np.cos(fy_), np.cos(Z) + 0*fx_
                f = (np.sin(fx_)*(ccy + ccz), np.sin(fy_)*(ccz + ccx), np.sin(Z)*(ccx + ccy))
            else:
                raise ValueError(dress)
            fc = f[0]*cx + f[1]*cy + f[2]*cz
            totY += float((ww*(-4*M*fc/E**3)).sum())
            totC += float((ww*(4*fc/E)).sum())
    return totY, totC


def evac_track(b, r, x, w, t, m, nrk=4, chunk=None):
    """Y-b helper: e(m, t) = -2 < E_m o Phi_t^{(m)} > per Dirac field with the flow recomputed at the actual mass m (own flow tracks m)."""
    F = Ferm(b, r, mflow=m)
    N = len(x)
    if chunk is None:
        chunk = max(1, int(2.5e5/(N*N)))
    tot = 0.0
    X = x[:, None, None]; Y = x[None, :, None]
    for i0 in range(0, N, chunk):
        sl = slice(i0, min(N, i0 + chunk))
        Z = x[sl][None, None, :]
        ww = w[:, None, None]*w[None, :, None]*w[sl][None, None, :]
        Wz = F.W(Z)
        if t != 0.0:
            fx_, fy_ = flowF(F, X + 0*Y + 0*Z, Y + 0*X + 0*Z, Wz, t, nrk)
        else:
            fx_, fy_ = X + 0*Y + 0*Z, Y + 0*X + 0*Z
        M = m + F.W(fx_) + F.W(fy_) + Wz
        E = np.sqrt(F.s(fx_)**2 + F.s(fy_)**2 + F.s(Z)**2 + M*M)
        tot += float((ww*E).sum())
    return -2*tot


def hess_even(f, d):
    """Hessian of an even function of t: 2[f(d) - f(0)]/d^2 with Richardson over d, 2d."""
    f0 = f(0.0); f1 = f(d); f2 = f(2*d)
    h1 = 2*(f1 - f0)/d**2; h2 = 2*(f2 - f0)/(2*d)**2
    return f0, h1, h2, (4*h1 - h2)/3


def hess_gen(f, d):
    f0 = f(0.0); fp, fm = f(d), f(-d); fp2, fm2 = f(2*d), f(-2*d)
    h1 = (fp - 2*f0 + fm)/d**2; h2 = (fp2 - 2*f0 + fm2)/(2*d)**2
    return f0, (fp - fm)/(2*d), h1, h2, (4*h1 - h2)/3
