"""C8 core: the supplied walk (C7 / parent definition) in Clifford-vector form, and the
static second-order vacuum response to a metric (or lapse) perturbation of wavevector q.

Walk: U(k) = f + i x.Gamma, Gamma = (tau1, tau2, tau3 s1, tau3 s2, tau3 s3), x = (h1, h2, g1, g2, g3),
(f, h1, h2) = F phi(k) (F^T F = G(b), massless member F phi0 = e_f, h-plane rotated so W || h1),
massive member U_theta = M U0 M, M = exp(i theta hhat.tau/2), hhat = (cos chi, sin chi).
Generator (C7 Theorem A): H = -rho(f) x.Gamma, E = arccos f, rho = E / sqrt(1-f^2).
Lattice units a = tau = 1.

Second-order vacuum energy for delta H = lambda (O_q + O_q^dag), O_q(k+q <- k) = o(k+q/2).Gamma
(midpoint quantisation), per unit volume:
  e2(q) = -int_BZ d^3k/(2pi)^3 F(k, q/2),
  F(k, t) = 2 [ o^2 (1 + ahat.bhat) - 2 (ahat.o)(bhat.o) ] / (E(k+t qhat) + E(k-t qhat)),
  ahat = xhat(k + t qhat), bhat = xhat(k - t qhat)   (Clifford trace identity, c8_exact E4).
"""
from __future__ import annotations

import numpy as np

# ------------------------------------------------------------------ parameter points (C7 / parent)
co = [259200000000, -453744000000, 12644840000, 1185396800, -39225499]
ustar = min(r.real for r in np.roots(co) if abs(r.imag) < 1e-12 and r.real > 0)
r5, r6, r15 = np.sqrt(5), np.sqrt(6), np.sqrt(15)
POINTS = {'bstar': (11/30, np.sqrt(ustar), 3/20),
          'iso': ((r6 + 2*r15)/27, (5*r6 - 2*r15)/27, (2*r15 - 2*r6)/27),
          'gold': ((9*r5 - 5)/38, (5*r5 - 7)/19, (71 - 29*r5)/38)}


def Gmat(b0, b1, b2):
    return np.array([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
                     [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
                     [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
                     [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])


phi0 = np.array([1.0, 3, 3, 1]); wv = np.array([0.0, 1, 2, 1])


def build_F(b):
    """Same construction as C7 c7_numeric.Walk (imported premise P2)."""
    G = Gmat(*b)
    ev, V = np.linalg.eigh(G)
    keep = ev > 1e-13
    F = (V[:, keep]*np.sqrt(ev[keep])).T
    if F.shape[0] < 3:
        F = np.vstack([F, np.zeros((3 - F.shape[0], 4))])
    e = F @ phi0
    Q = np.linalg.qr(np.column_stack([e, np.eye(3)]))[0][:, :3]
    if Q[:, 0] @ e < 0:
        Q[:, 0] *= -1
    F = Q.T @ F
    W = F[1:] @ wv
    if np.linalg.norm(W) > 1e-12:
        ang = np.arctan2(W[1], W[0])
        R = np.array([[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])
        F[1:] = R @ F[1:]
    return F


def rho_u(u):
    """rho = arccos(1-u)/sqrt(u(2-u)); series (c8_exact E5) for small u."""
    u = np.asarray(u, float)
    out = np.empty_like(u)
    sm = u < 2e-3
    us = u[sm]
    out[sm] = 1 + us/3 + 2*us**2/15 + 2*us**3/35 + 8*us**4/315
    ul = u[~sm]
    out[~sm] = 2*np.arcsin(np.sqrt(ul/2))/np.sqrt(ul*(2 - ul))
    return out


def drho_u(u, rho):
    """d rho / d f = (f rho - 1)/(1 - f^2); series for small u."""
    u = np.asarray(u, float)
    out = np.empty_like(u)
    sm = u < 2e-3
    us = u[sm]
    out[sm] = -1/3 - 4*us/15 - 6*us**2/35 - 32*us**3/315
    ul = u[~sm]
    out[~sm] = ((1 - ul)*rho[~sm] - 1)/(ul*(2 - ul))
    return out


class Walk:
    def __init__(self, name, theta=0.0, chi=np.pi/2, b=None):
        self.name = name
        self.b = np.array(POINTS[name] if b is None else b, float)
        self.s = self.b[0] + 2*self.b[1] + self.b[2]
        self.F = build_F(self.b)
        self.W = self.F[1:] @ wv
        self.theta, self.chi = theta, chi
        self.hh = np.array([np.cos(chi), np.sin(chi)])

    def sym(self, k, deriv=False):
        """u = 1 - f (computed without cancellation), x (n,5); optionally df (n,3), dx (n,3,5)."""
        b0, b1, b2 = self.b
        c = np.cos(k); sn = np.sin(k)
        xa = 2*np.sin(k/2)**2
        x1, x2, x3 = xa[:, 0], xa[:, 1], xa[:, 2]
        dphi = np.stack([np.zeros_like(x1), x1 + x2 + x3,
                         (x1 + x2 - x1*x2) + (x1 + x3 - x1*x3) + (x2 + x3 - x2*x3),
                         x1 + x2 + x3 - (x1*x2 + x1*x3 + x2*x3) + x1*x2*x3], axis=1)
        u0 = dphi @ self.F[0]
        f0 = 1 - u0
        h = -(dphi @ self.F[1:].T)                    # F[1:] phi0 = 0
        g = np.stack([sn[:, i]*(b0 + b1*(c[:, (i+1) % 3] + c[:, (i+2) % 3]) + b2*c[:, (i+1) % 3]*c[:, (i+2) % 3])
                      for i in range(3)], axis=1)
        th, hh = self.theta, self.hh
        if th != 0.0:
            hd = h @ hh
            u = (1 - np.cos(th)) + np.cos(th)*u0 + np.sin(th)*hd
            h = h - (1 - np.cos(th))*hd[:, None]*hh[None, :] + np.sin(th)*f0[:, None]*hh[None, :]
        else:
            u = u0
        x = np.concatenate([h, g], axis=1)
        if not deriv:
            return u, x
        # derivatives d/dk_i
        dph = np.zeros((k.shape[0], 3, 4))
        for i in range(3):
            j, l = (i+1) % 3, (i+2) % 3
            dph[:, i, 1] = -sn[:, i]
            dph[:, i, 2] = -sn[:, i]*(c[:, j] + c[:, l])
            dph[:, i, 3] = -sn[:, i]*c[:, j]*c[:, l]
        df0 = dph @ self.F[0]                          # (n,3)
        dh = dph @ self.F[1:].T                        # (n,3,2)
        dg = np.zeros((k.shape[0], 3, 3))              # dg[:, i, a] = d g_a / d k_i
        for a in range(3):
            j, l = (a+1) % 3, (a+2) % 3
            dg[:, a, a] = c[:, a]*(b0 + b1*(c[:, j] + c[:, l]) + b2*c[:, j]*c[:, l])
            dg[:, j, a] = sn[:, a]*(-b1*sn[:, j] - b2*sn[:, j]*c[:, l])
            dg[:, l, a] = sn[:, a]*(-b1*sn[:, l] - b2*c[:, j]*sn[:, l])
        if th != 0.0:
            hd0 = (-(dphi @ self.F[1:].T)) @ hh
            dhd = dh @ hh
            df = np.cos(th)*df0 - np.sin(th)*dhd
            dh = dh - (1 - np.cos(th))*dhd[:, :, None]*hh[None, None, :] + np.sin(th)*df0[:, :, None]*hh[None, None, :]
        else:
            df = df0
        dx = np.concatenate([dh, dg], axis=2)
        return u, x, df, dx


def Efun(u):
    return 2*np.arcsin(np.sqrt(np.clip(u, 0, 2)/2))


def tt_eps(qhat_name, pol):
    if qhat_name == 'z':
        qh = np.array([0.0, 0, 1])
        e = np.diag([1.0, -1, 0])/np.sqrt(2) if pol == 'A' else np.array([[0, 1.0, 0], [1, 0, 0], [0, 0, 0]])/np.sqrt(2)
    elif qhat_name == 'd':                          # (111)
        qh = np.ones(3)/np.sqrt(3)
        u1 = np.array([1.0, -1, 0])/np.sqrt(2); u2 = np.array([1.0, 1, -2])/np.sqrt(6)
        e = (np.outer(u1, u1) - np.outer(u2, u2))/np.sqrt(2) if pol == 'A' else (np.outer(u1, u2) + np.outer(u2, u1))/np.sqrt(2)
    elif qhat_name == 'f':                          # (110)
        qh = np.array([1.0, 1, 0])/np.sqrt(2)
        u1 = np.array([1.0, -1, 0])/np.sqrt(2); u2 = np.array([0.0, 0, 1])
        e = (np.outer(u1, u1) - np.outer(u2, u2))/np.sqrt(2) if pol == 'A' else (np.outer(u1, u2) + np.outer(u2, u1))/np.sqrt(2)
    elif qhat_name == 'g':                          # (1,2,3): generic direction, used to test the cubic fit
        qh = np.array([1.0, 2, 3])/np.sqrt(14)
        u1 = np.array([2.0, -1, 0])/np.sqrt(5); u2 = np.cross(qh, u1)
        e = (np.outer(u1, u1) - np.outer(u2, u2))/np.sqrt(2) if pol == 'A' else (np.outer(u1, u2) + np.outer(u2, u1))/np.sqrt(2)
    else:
        raise ValueError
    return qh, e


def vertex(walk, coupling, eps, km, ka, kb):
    """Clifford vector o (n,5) of the perturbation symbol between kb = k - t qhat and ka = k + t qhat."""
    n = km.shape[0]
    o = np.zeros((n, 5))
    if coupling in ('M1', 'M2', 'M3'):
        u, x = walk.sym(km)
        if coupling == 'M1':
            P = rho_u(u)[:, None]*x[:, 2:]
        elif coupling == 'M2':
            P = x[:, 2:]
        else:
            P = walk.s*np.sin(km)
        o[:, 2:] = 0.5*(P @ eps.T)                 # O = -(1/2) eps_ij alpha_i P_j, alpha_i = -Gamma_{2+i}
    elif coupling == 'M4':
        u, x, df, dx = walk.sym(km, deriv=True)
        rho = rho_u(u); drho = drho_u(u, rho)
        dHc = drho[:, None, None]*df[:, :, None]*x[:, None, :] + rho[:, None, None]*dx   # -dH/dk_i (Clifford comps)
        w = np.sin(km) @ eps.T                     # w_i = eps_ij sin k_j
        o = 0.5*np.einsum('ni,nic->nc', w, dHc)
    elif coupling == 'L1':
        u, x = walk.sym(km)
        o = rho_u(u)[:, None]*x
    elif coupling == 'L2':
        ua, xa = walk.sym(ka); ub, xb = walk.sym(kb)
        o = 0.5*(rho_u(ua)[:, None]*xa + rho_u(ub)[:, None]*xb)
    else:
        raise ValueError(coupling)
    return o


def Fval(walk, coupling, eps, qh, k, t):
    ka = k + t[:, None]*qh[None, :] if np.ndim(t) else k + t*qh[None, :]
    kb = k - (t[:, None]*qh[None, :] if np.ndim(t) else t*qh[None, :])
    ua, xa = walk.sym(ka); ub, xb = walk.sym(kb)
    ah = xa/np.linalg.norm(xa, axis=1)[:, None]; bh = xb/np.linalg.norm(xb, axis=1)[:, None]
    o = vertex(walk, coupling, eps, k, ka, kb)
    o2 = np.sum(o*o, 1)
    num = o2*(1 + np.sum(ah*bh, 1)) - 2*np.sum(ah*o, 1)*np.sum(bh*o, 1)
    return 2*num/(Efun(ua) + Efun(ub))


def F2val(walk, coupling, eps, qh, k, rel=0.05):
    """Pointwise t^2 coefficient of F(k,t) (F is even in t), by two-level Richardson."""
    _, x0 = walk.sym(k)
    hstep = rel*np.minimum(1.0, np.linalg.norm(x0, axis=1))
    F0 = Fval(walk, coupling, eps, qh, k, 0.0)
    D = []
    for fac in (1.0, 0.5, 0.25):
        hh = fac*hstep
        D.append((Fval(walk, coupling, eps, qh, k, hh) - F0)/hh**2)
    R1 = (4*D[1] - D[0])/3; R2 = (4*D[2] - D[1])/3
    return F0, (16*R2 - R1)/15, np.abs(R2 - R1)


def bump(r, kap):
    """C-infinity cutoff: 1 for r <= kap/2, 0 for r >= kap."""
    xx = np.clip((kap - r)/(kap/2), 0, 1)
    out = np.zeros_like(xx)
    inner = (xx > 0) & (xx < 1)
    a = np.exp(-1/xx[inner]); bb = np.exp(-1/(1 - xx[inner]))
    out[inner] = a/(a + bb)
    out[xx >= 1] = 1.0
    return out


def wrap(v):
    return (v + np.pi) % (2*np.pi) - np.pi


def bz_integral(walk, coupling, eps, qh, N, kap=1.0, nr=24, nmu=24, nph=48, chunk=1 << 15, centers=None):
    """Returns (int F0, int F2) with int = int_BZ d^3k/(2pi)^3, split by a smooth partition of
    unity around Gamma: outer part on an N^3 midpoint (periodic trapezoid) grid, inner ball in
    spherical Gauss-Legendre x Gauss-Legendre x trapezoid coordinates."""
    centers = [np.zeros(3)] if centers is None else [np.asarray(c, float) for c in centers]
    g1 = -np.pi + 2*np.pi*(np.arange(N) + 0.5)/N
    S0 = S2 = 0.0; rerr = 0.0
    KX, KY, KZ = np.meshgrid(g1, g1, g1, indexing='ij')
    K = np.stack([KX.ravel(), KY.ravel(), KZ.ravel()], 1)
    for i in range(0, K.shape[0], chunk):
        kk = K[i:i+chunk]
        w = 1 - sum(bump(np.linalg.norm(wrap(kk - c[None, :]), axis=1), kap) for c in centers)
        F0, F2, er = F2val(walk, coupling, eps, qh, kk)
        S0 += np.sum(w*F0); S2 += np.sum(w*F2); rerr = max(rerr, np.max(w*er/(np.abs(F2) + 1e-30)))
    outer0, outer2 = S0/N**3, S2/N**3
    # inner ball
    xr, wr = np.polynomial.legendre.leggauss(nr); r = kap*(xr + 1)/2; wr = wr*kap/2
    xm, wm = np.polynomial.legendre.leggauss(nmu)
    ph = 2*np.pi*np.arange(nph)/nph; wp = np.full(nph, 2*np.pi/nph)
    R, MU, PH = np.meshgrid(r, xm, ph, indexing='ij')
    Wt = (wr[:, None, None]*wm[None, :, None]*wp[None, None, :])*R**2
    st = np.sqrt(1 - MU**2)
    K0 = np.stack([(R*st*np.cos(PH)).ravel(), (R*st*np.sin(PH)).ravel(), (R*MU).ravel()], 1)
    Wt = Wt.ravel()*bump(R.ravel(), kap)
    I0 = I2 = 0.0
    for c in centers:
        K = K0 + c[None, :]
        for i in range(0, K.shape[0], chunk):
            kk = K[i:i+chunk]
            F0, F2, er = F2val(walk, coupling, eps, qh, kk)
            I0 += np.sum(Wt[i:i+chunk]*F0); I2 += np.sum(Wt[i:i+chunk]*F2)
    I0 /= (2*np.pi)**3; I2 /= (2*np.pi)**3
    return outer0 + I0, outer2 + I2, rerr
