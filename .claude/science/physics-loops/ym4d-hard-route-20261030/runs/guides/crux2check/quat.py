# Pure-Python quaternion and SU(2) lattice utilities for guide checks of
# library/gap-crux2-astra62.md. Guide only; no proof step depends on these.
import math
import random

ONE = (1.0, 0.0, 0.0, 0.0)


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2,
            a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2,
            a1*d2 + b1*c2 - c1*b2 + d1*a2)


def qconj(q):
    return (q[0], -q[1], -q[2], -q[3])


def qadd(p, q):
    return (p[0]+q[0], p[1]+q[1], p[2]+q[2], p[3]+q[3])


def qscale(s, q):
    return (s*q[0], s*q[1], s*q[2], s*q[3])


def qnorm(q):
    return math.sqrt(q[0]**2 + q[1]**2 + q[2]**2 + q[3]**2)


def im(q):
    return (q[1], q[2], q[3])


def vdot(u, v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]


def vcross(u, v):
    return (u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0])


def vadd(u, v):
    return (u[0]+v[0], u[1]+v[1], u[2]+v[2])


def vsub(u, v):
    return (u[0]-v[0], u[1]-v[1], u[2]-v[2])


def vscale(s, u):
    return (s*u[0], s*u[1], s*u[2])


def vnorm2(u):
    return u[0]**2 + u[1]**2 + u[2]**2


def ad(q, v):
    """Ad(q) v = q v q^-1 for imaginary v (3-vector)."""
    r = qmul(qmul(q, (0.0, v[0], v[1], v[2])), qconj(q))
    return (r[1], r[2], r[3])


def ad_inv(q, v):
    return ad(qconj(q), v)


def haar(rng):
    while True:
        x = [rng.gauss(0.0, 1.0) for _ in range(4)]
        n = math.sqrt(sum(t*t for t in x))
        if n > 1e-12:
            return tuple(t/n for t in x)


def qexp(v, t=1.0):
    """exp(t v) for imaginary 3-vector v (as quaternion exponential)."""
    n = math.sqrt(vnorm2(v))
    if n < 1e-15:
        return ONE
    s = math.sin(t*n)/n
    return (math.cos(t*n), s*v[0], s*v[1], s*v[2])


def sym3_eigs(m):
    """Eigenvalues of a symmetric 3x3 matrix m (list of lists), ascending."""
    a, b, c = m[0][0], m[1][1], m[2][2]
    d, e, f = m[0][1], m[1][2], m[0][2]
    p1 = d*d + e*e + f*f
    q = (a + b + c)/3.0
    if p1 < 1e-30:
        return sorted([a, b, c])
    p2 = (a-q)**2 + (b-q)**2 + (c-q)**2 + 2*p1
    p = math.sqrt(p2/6.0)
    bm = [[(m[i][j] - (q if i == j else 0.0))/p for j in range(3)] for i in range(3)]
    detb = (bm[0][0]*(bm[1][1]*bm[2][2] - bm[1][2]*bm[2][1])
            - bm[0][1]*(bm[1][0]*bm[2][2] - bm[1][2]*bm[2][0])
            + bm[0][2]*(bm[1][0]*bm[2][1] - bm[1][1]*bm[2][0]))
    r = max(-1.0, min(1.0, detb/2.0))
    phi = math.acos(r)/3.0
    e1 = q + 2*p*math.cos(phi)
    e3 = q + 2*p*math.cos(phi + 2*math.pi/3)
    e2 = 3*q - e1 - e3
    return sorted([e1, e2, e3])


def outer_sum(vs):
    m = [[0.0]*3 for _ in range(3)]
    for v in vs:
        for i in range(3):
            for j in range(3):
                m[i][j] += v[i]*v[j]
    return m


def lam_min_cross(vs):
    """min over unit w of sum_i |v_i x w|^2 = tr M - lambda_max(M)."""
    m = outer_sum(vs)
    ev = sym3_eigs(m)
    return (m[0][0] + m[1][1] + m[2][2]) - ev[2]


class Lattice:
    """Periodic 4D lattice of side L (list of 4 sides), links U[(x, mu)]."""

    def __init__(self, sides, rng=None, cold=True):
        self.sides = tuple(sides)
        self.sites = []
        L0, L1, L2, L3 = self.sides
        for a in range(L0):
            for b in range(L1):
                for c in range(L2):
                    for d in range(L3):
                        self.sites.append((a, b, c, d))
        self.U = {}
        for x in self.sites:
            for mu in range(4):
                self.U[(x, mu)] = ONE if cold else haar(rng)

    def sh(self, x, mu, s=1):
        y = list(x)
        y[mu] = (y[mu] + s) % self.sides[mu]
        return tuple(y)

    def staples(self, x, mu):
        """Sum over the six plaquettes through (x,mu) of the rest R_p, so that
        U_p (based at x, starting along (x,mu)) = U_mu(x) R_p."""
        U = self.U
        out = []
        for nu in range(4):
            if nu == mu:
                continue
            xm = self.sh(x, mu)
            xn = self.sh(x, nu)
            # forward plaquette (x; mu, nu)
            r = qmul(qmul(U[(xm, nu)], qconj(U[(xn, mu)])), qconj(U[(x, nu)]))
            out.append(r)
            # backward plaquette (x - nu; mu, nu)
            xmn = self.sh(xm, nu, -1)
            xn_ = self.sh(x, nu, -1)
            r = qmul(qmul(qconj(U[(xmn, nu)]), qconj(U[(xn_, mu)])), U[(xn_, nu)])
            out.append(r)
        return out

    def force(self, x, mu, b):
        """N_e = b sum_p Im(h_p), h_p based at tail x, starting along e."""
        u = self.U[(x, mu)]
        n = (0.0, 0.0, 0.0)
        for r in self.staples(x, mu):
            n = vadd(n, im(qmul(u, r)))
        return vscale(b, n)

    def action(self, b):
        """b sum_p (1/2) tr U_p = b sum_p Re U_p (each plaquette once)."""
        U = self.U
        s = 0.0
        for x in self.sites:
            for mu in range(4):
                for nu in range(mu+1, 4):
                    p = qmul(qmul(qmul(U[(x, mu)], U[(self.sh(x, mu), nu)]),
                                  qconj(U[(self.sh(x, nu), mu)])), qconj(U[(x, nu)]))
                    s += p[0]
        return b*s

    def plaq(self, x, mu, nu):
        U = self.U
        return qmul(qmul(qmul(U[(x, mu)], U[(self.sh(x, mu), nu)]),
                         qconj(U[(self.sh(x, nu), mu)])), qconj(U[(x, nu)]))

    def heatbath_link(self, x, mu, b, rng):
        A = (0.0, 0.0, 0.0, 0.0)
        for r in self.staples(x, mu):
            A = qadd(A, r)
        k = qnorm(A)
        if k < 1e-12:
            self.U[(x, mu)] = haar(rng)
            return
        V = qscale(1.0/k, A)
        alpha = b*k
        # sample w0 with density ~ exp(alpha w0) sqrt(1 - w0^2) on [-1, 1]
        while True:
            lo = math.exp(-2.0*alpha)
            y = lo + (1.0 - lo)*rng.random()
            w0 = 1.0 + math.log(y)/alpha
            if rng.random() < math.sqrt(max(0.0, 1.0 - w0*w0)):
                break
        # direction uniform
        while True:
            d = [rng.gauss(0.0, 1.0) for _ in range(3)]
            nd = math.sqrt(sum(t*t for t in d))
            if nd > 1e-12:
                break
        s = math.sqrt(max(0.0, 1.0 - w0*w0))/nd
        W = (w0, s*d[0], s*d[1], s*d[2])
        # weight exp(b Re(U A)) = exp(alpha Re(U V)); W = U V
        self.U[(x, mu)] = qmul(W, qconj(V))

    def sweep(self, b, rng):
        for x in self.sites:
            for mu in range(4):
                self.heatbath_link(x, mu, b, rng)

    def mean_plaq(self):
        s = 0.0
        n = 0
        for x in self.sites:
            for mu in range(4):
                for nu in range(mu+1, 4):
                    s += self.plaq(x, mu, nu)[0]
                    n += 1
        return s/n
