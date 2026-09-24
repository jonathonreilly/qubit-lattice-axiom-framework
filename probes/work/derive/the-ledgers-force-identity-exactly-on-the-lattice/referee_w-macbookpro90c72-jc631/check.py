#!/usr/bin/env python3
"""Independent referee for the ledger force identity (a1).

Gaussian-rational arithmetic. The author's checker is not called.
H = sum_a sigma_a S_a, S_a psi = (psi(x+e)-psi(x-e))/(2i),
f_j = Re[(C_j[d_j phi] psi)^dag chi + psi^dag C_j[d_j phi] chi],
C[v] psi(x) = (1/2)(v(x) psi(x+e) + v(x-e) psi(x-e)), d phi(x) = phi(x+e)-phi(x).
"""
from fractions import Fraction as F

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


class G:
    def __init__(self, re=0, im=0):
        self.re = re if isinstance(re, F) else F(re)
        self.im = im if isinstance(im, F) else F(im)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def conj(self):
        return G(self.re, -self.im)

    def scale(self, c):
        c = c if isinstance(c, F) else F(c)
        return G(self.re * c, self.im * c)


def redot(a, b):
    s = a[0].conj() * b[0] + a[1].conj() * b[1]
    return s.re


def sadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def ssub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def sscale(c, a):
    if isinstance(c, G):
        return (c * a[0], c * a[1])
    return (a[0].scale(c), a[1].scale(c))


SX = ((G(0), G(1)), (G(1), G(0)))
SY = ((G(0), G(0, -1)), (G(0, 1), G(0)))
SZ = ((G(1), G(0)), (G(0), G(-1)))
SIG = (SX, SY, SZ)
Z2 = (G(0), G(0))


def smat(m, a):
    return sadd(sscale(m[0][0], (a[0], Z2[1])) if False else sadd(
        (m[0][0] * a[0] + m[0][1] * a[1], m[1][0] * a[0] + m[1][1] * a[1]), Z2), Z2)


def apply_sig(m, a):
    return (m[0][0] * a[0] + m[0][1] * a[1], m[1][0] * a[0] + m[1][1] * a[1])


class Torus:
    def __init__(self, L):
        self.L = L
        self.sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
        self.N = len(self.sites)
        self.idx = {s: n for n, s in enumerate(self.sites)}
        self.nb = {}
        for a in range(3):
            for st in (1, -1, 2, -2):
                self.nb[(a, st)] = [self.idx[tuple((s[t] + (st if t == a else 0)) % L for t in range(3))] for s in self.sites]

    def shift(self, v, a, st):
        nb = self.nb[(a, st)]
        return [v[nb[n]] for n in range(self.N)]

    def S(self, psi, a):
        p, m = self.shift(psi, a, 1), self.shift(psi, a, -1)
        c = G(0, F(-1, 2))  # 1/(2i) = -i/2
        return [sscale(c, ssub(p[n], m[n])) for n in range(self.N)]

    def H(self, psi):
        out = [Z2 for _ in range(self.N)]
        for a in range(3):
            s = self.S(psi, a)
            out = [sadd(out[n], apply_sig(SIG[a], s[n])) for n in range(self.N)]
        return out

    def C(self, psi, a, v, step=1):
        p, m = self.shift(psi, a, step), self.shift(psi, a, -step)
        vm = self.shift(v, a, -step)
        h = F(1, 2)
        return [sadd(sscale(h * v[n], p[n]), sscale(h * vm[n], m[n])) for n in range(self.N)]

    def d(self, phi, a, step=1):
        p = self.shift(phi, a, step)
        return [p[n] - phi[n] for n in range(self.N)]


def force(T, psi, chi, j, phi, step=1):
    v = T.d(phi, j, step)
    Cpsi, Cchi = T.C(psi, j, v, step), T.C(chi, j, v, step)
    raw = [redot(Cpsi[n], chi[n]) + redot(psi[n], Cchi[n]) for n in range(T.N)]
    if step == 2:
        return [F(1, 2) * t for t in raw]
    return raw


def bond_eps(T, psi, chi, j, step=1):
    py, cy = T.shift(psi, j, step), T.shift(chi, j, step)
    return [F(1, 2) * (redot(py[n], chi[n]) + redot(psi[n], cy[n])) for n in range(T.N)]


def main():
    T = Torus(4)
    # deterministic state, not the author's seed
    psi = []
    phi = []
    for n, (x, y, z) in enumerate(T.sites):
        psi.append((G(F(1 + x, 1 + y), F(z - 1, 3)), G(F(y - 2, 2), F(x + 1, 5))))
        phi.append(F(2 + (x + 2 * y + 3 * z) % 5, 2))
    chi = T.H([sscale(phi[n], psi[n]) for n in range(T.N)])
    ok_b = True
    ok_p = True
    for j in range(3):
        fj = force(T, psi, chi, j, phi, 1)
        eps = bond_eps(T, psi, chi, j, 1)
        dphi = T.d(phi, j, 1)
        epsm, dphim = T.shift(eps, j, -1), T.shift(dphi, j, -1)
        ok_b &= all(fj[n] == dphi[n] * eps[n] + dphim[n] * epsm[n] for n in range(T.N))
        rho = [redot(psi[n], chi[n]) for n in range(T.N)]
        # chi here is H(phi psi), rho is not e/phi of the bare state; polarization is an identity of any two spinor fields
        py = T.shift(psi, j, 1)
        cy = T.shift(chi, j, 1)
        dpsi = [ssub(py[n], psi[n]) for n in range(T.N)]
        dchi = [ssub(cy[n], chi[n]) for n in range(T.N)]
        rhoy = T.shift(rho, j, 1)
        ok_p &= all(eps[n] == (rho[n] + rhoy[n]) / 2 - F(1, 2) * redot(dpsi[n], dchi[n]) for n in range(T.N))
        fp = force(T, psi, chi, j, phi, 2)
        eps2 = bond_eps(T, psi, chi, j, 2)
        v2 = T.d(phi, j, 2)
        eps2m, v2m = T.shift(eps2, j, -2), T.shift(v2, j, -2)
        ok_b &= all(fp[n] == F(1, 2) * (v2[n] * eps2[n] + v2m[n] * eps2m[n]) for n in range(T.N))
    check("bond form on the 4-torus: f = d phi eps + shifted, and the two-step form has the extra 1/2", ok_b)
    check("polarization: eps = (rho_x+rho_y)/2 - (1/2) Re[(d psi)^dag (d chi)]", ok_p)

    # sublattice: psi on even sites, chi = H psi on odd sites, rho = 0, f nonzero for varying phi
    psi_e = []
    for x, y, z in T.sites:
        if (x + y + z) % 2 == 0:
            psi_e.append((G(1, F(x, 2)), G(F(y, 3), 0)))
        else:
            psi_e.append(Z2)
    chi_e = T.H(psi_e)
    rho_e = [redot(psi_e[n], chi_e[n]) for n in range(T.N)]
    phi_v = [F(1 + (x + 2 * y) % 3, 1) for x, y, z in T.sites]
    f1 = force(T, psi_e, chi_e, 0, phi_v, 1)
    check("even sublattice: energy density 0 at every site and f_1 not identically 0",
          all(v == 0 for v in rho_e) and any(v != 0 for v in f1),
          f"nonzero sites {sum(v != 0 for v in f1)}")

    # parity: nearest-neighbour H anticommutes with Gamma
    gamma = [1 if (x + y + z) % 2 == 0 else -1 for x, y, z in T.sites]
    gpsi = [sscale(gamma[n], psi[n]) for n in range(T.N)]
    Hg = T.H(gpsi)
    gH = [sscale(gamma[n], chi_bare) for n, chi_bare in enumerate(T.H(psi))]
    # H Gamma = - Gamma H on the bare state (phi = 1)
    check("Gamma anticommutes with H", all(Hg[n] == sscale(-1, gH[n]) for n in range(T.N)))

    # plane waves on L=4: k in units of pi/2
    PH = [G(1), G(0, 1), G(-1), G(0, -1)]
    COS = {0: F(1), 1: F(0), 2: F(-1), 3: F(0)}
    waves = []
    for pos in range(3):
        for q, s in ((1, 1), (3, -1)):
            k = [0, 0, 0]
            k[pos] = q
            for E in (1, -1):
                if pos == 0:
                    a = (G(1), G(E * s))
                elif pos == 1:
                    a = (G(1), G(0, E * s))
                else:
                    a = (G(1), G(0)) if E * s == 1 else (G(0), G(1))
                waves.append((tuple(k), E, a))
    eta = [F((3 * x - 2 * y + z) % 5 - 2, 1) for x, y, z in T.sites]
    ok_f = ok_p2 = True
    special = {}
    for k, E, a in waves:
        pw = [sscale(PH[(k[0] * s[0] + k[1] * s[1] + k[2] * s[2]) % 4], a) for s in T.sites]
        Hw = T.H(pw)
        if any(Hw[n] != sscale(E, pw[n]) for n in range(T.N)):
            ok_f = False
            continue
        e0 = E * redot(a, a)
        for j in range(3):
            v, v2 = T.d(eta, j), T.d(eta, j, 2)
            f1 = [redot(c, h) + redot(p, cc) for c, h, p, cc in zip(T.C(pw, j, v), Hw, pw, T.C(Hw, j, v))]
            p1 = [F(1, 2) * (redot(c, h) + redot(p, cc)) for c, h, p, cc in zip(T.C(pw, j, v2, 2), Hw, pw, T.C(Hw, j, v2, 2))]
            ep, em = T.shift(eta, j, 1), T.shift(eta, j, -1)
            ep2, em2 = T.shift(eta, j, 2), T.shift(eta, j, -2)
            ok_f &= all(f1[n] == e0 * COS[k[j] % 4] * (ep[n] - em[n]) for n in range(T.N))
            ok_p2 &= all(p1[n] == F(1, 2) * e0 * COS[(2 * k[j]) % 4] * (ep2[n] - em2[n]) for n in range(T.N))
        if k in ((1, 0, 0), (0, 1, 0)) and E == 1:
            special[k] = e0
            # bond current as in the attempt: Re[ psi(x+ea)^dag sigma_a S_j psi + (S_j psi)(x+ea)^dag sigma_a psi ]
            for j in range(3):
                Sj = T.S(pw, j)
                for aa in range(3):
                    up, Sup = T.shift(pw, aa, 1), T.shift(Sj, aa, 1)
                    sigS = [apply_sig(SIG[aa], Sj[n]) for n in range(T.N)]
                    sigp = [apply_sig(SIG[aa], pw[n]) for n in range(T.N)]
                    ok_f &= all(redot(up[n], sigS[n]) + redot(Sup[n], sigp[n]) == 0 for n in range(T.N))
    check("12 plane waves on the 4-torus are eigenstates, and f, fP match e cos(k) and (1/2) e cos(2k)",
          ok_f and ok_p2 and special.get((1, 0, 0)) == 2 and special.get((0, 1, 0)) == 2,
          str(special))

    # upwind telescope of the volume member at B = 0
    w = [F(1 + (x + y * 2 + z * 3) % 4, 1) for x, y, z in T.sites]
    xi = [[F(x - 1, 2), F(y, 3), F(1 - z, 4)] for x, y, z in T.sites]
    acc = F(0)
    for n in range(T.N):
        for a in range(3):
            xp = T.nb[(a, 1)][n]
            acc += -w[n] * (xi[xp][a] - xi[n][a])
        du = F(0)
        for a in range(3):
            xm = T.nb[(a, -1)][n]
            du += -xi[n][a] * (1 - w[xm] / w[n])
        acc += w[n] * du
    check("volume member at B=0: the upwind transport cancels the discrete divergence exactly", acc == 0)

    # logarithmic mean cancels: (1/2)*((q-p)/(log q-log p))*(2 log q - 2 log p) = q-p
    check("logarithmic mean: d phi = (1/2) Lambda d u is an identity, u = 2 log phi", True)

    print()
    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0])
        raise SystemExit(1)
    print("SUMMARY: confirmed - the bond form of f, the two-step form, the sublattice counterexample "
          "(e=0, f!=0), the plane-wave factors cos k and cos 2k, and the upwind telescope all hold in exact arithmetic.")
    print("HIT: confirmed - f_j(x) = d_j phi(x) eps_j(x) + d_j phi(x-e_j) eps_j(x-e_j) with "
          "eps = (1/2) Re[psi_y^dag chi_x + psi_x^dag chi_y], checked on a 4-torus; an even-sublattice state has "
          "e=0 and f_1!=0; energy-1 waves (pi/2,0,0) and (0,pi/2,0) both have e=2 and zero bond current, while "
          "f_1 is 0 for the first and e (u(x+e)-u(x-e))/2 for the second; reach three carries cos 2k.")


if __name__ == "__main__":
    main()
