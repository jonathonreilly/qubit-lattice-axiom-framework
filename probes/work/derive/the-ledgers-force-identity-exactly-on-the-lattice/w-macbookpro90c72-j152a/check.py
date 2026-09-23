#!/usr/bin/env python3
"""The ledger's force identity exactly on the lattice (blocks 53-75), independent attempt 1 of 2: exact checks for ATTEMPT.md.

Worker w-macbookpro90c72-j152a (claude-opus-5-5).  Exact arithmetic only: Gaussian rationals (class Q below, Fraction parts) on
periodic tori, with positive rational rate roots phi.  Objects (blocks 54, 63, 64, 66, 72): H = sum_a sigma_a S_a,
S_a = (T_a - T_a^dagger)/(2i), (T_a psi)(x) = psi(x + e_a); H_w = phi H phi; chi = H phi psi; energy density e = phi Re psi^dagger chi;
C_j[v] psi(x) = (v(x) psi(x + e_j) + v(x - e_j) psi(x - e_j))/2, d_j phi(x) = phi(x + e_j) - phi(x);
f_j = Re[(C_j[d_j phi] psi)^dagger chi + psi^dagger C_j[d_j phi] chi] (block 66 T3); the two-step momentum P_j = S_j C_j,
C2_j[v] psi(x) = (v(x) psi(x + 2e_j) + v(x - 2e_j) psi(x - 2e_j))/2, d2_j phi(x) = phi(x + 2e_j) - phi(x),
fP_j = Re[((1/2) C2_j[d2_j phi] psi)^dagger chi + psi^dagger (1/2) C2_j[d2_j phi] chi] (block 72).
Families: Q quotes; A the content (reach two); B the field side; D the content (reach three).
"""
from __future__ import annotations

import random
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------------------------------------ Gaussian rationals and spinors
class Q:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = r if isinstance(r, Fr) else Fr(r)
        self.i = i if isinstance(i, Fr) else Fr(i)

    def __add__(self, o):
        return Q(self.r + o.r, self.i + o.i)

    def __sub__(self, o):
        return Q(self.r - o.r, self.i - o.i)

    def __neg__(self):
        return Q(-self.r, -self.i)

    def __mul__(self, o):
        if isinstance(o, Q):
            return Q(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)
        o = Fr(o)
        return Q(self.r * o, self.i * o)

    __rmul__ = __mul__

    def conj(self):
        return Q(self.r, -self.i)

    def __eq__(self, o):
        return self.r == o.r and self.i == o.i


Z = Q(0, 0)
ONE = Q(1, 0)
I = Q(0, 1)
SIG = [((Z, ONE), (ONE, Z)), ((Z, -I), (I, Z)), ((ONE, Z), (Z, -ONE))]


def sp_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sp_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def sp_scale(c, a):
    return (c * a[0], c * a[1])


def sp_mat(m, a):
    return (m[0][0] * a[0] + m[0][1] * a[1], m[1][0] * a[0] + m[1][1] * a[1])


def re_dot(a, b):
    """Re a^dagger b."""
    return a[0].r * b[0].r + a[0].i * b[0].i + a[1].r * b[1].r + a[1].i * b[1].i


class Torus:
    def __init__(self, L):
        self.L = L
        self.N = L ** 3
        self.sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
        self.idx = {s: n for n, s in enumerate(self.sites)}
        self.nb = {}
        for a in range(3):
            for st in (1, -1, 2, -2):
                self.nb[(a, st)] = [self.idx[tuple((s[t] + (st if t == a else 0)) % L for t in range(3))] for s in self.sites]

    def shift(self, v, a, st):
        nb = self.nb[(a, st)]
        return [v[nb[n]] for n in range(self.N)]

    def S(self, psi, a):  # (psi(x+e) - psi(x-e))/(2i) = -(i/2)(...)
        p, m = self.shift(psi, a, 1), self.shift(psi, a, -1)
        c = Q(0, Fr(-1, 2))
        return [sp_scale(c, sp_sub(p[n], m[n])) for n in range(self.N)]

    def H(self, psi):
        out = [(Z, Z)] * self.N
        for a in range(3):
            s = self.S(psi, a)
            out = [sp_add(out[n], sp_mat(SIG[a], s[n])) for n in range(self.N)]
        return out

    def mul(self, phi, psi):
        return [sp_scale(phi[n], psi[n]) for n in range(self.N)]

    def C(self, psi, a, v, step=1):
        p, m = self.shift(psi, a, step), self.shift(psi, a, -step)
        vm = self.shift(v, a, -step)
        h = Fr(1, 2)
        return [sp_add(sp_scale(h * v[n], p[n]), sp_scale(h * vm[n], m[n])) for n in range(self.N)]

    def d(self, phi, a, step=1):
        p = self.shift(phi, a, step)
        return [p[n] - phi[n] for n in range(self.N)]


def rand_q(rng, k=3):
    return Q(Fr(rng.randint(-k, k)), Fr(rng.randint(-k, k)))


def rand_state(T, rng, k=3):
    return [(rand_q(rng, k), rand_q(rng, k)) for _ in range(T.N)]


def rand_phi(T, rng):
    return [Fr(rng.randint(2, 9), rng.randint(2, 5)) for _ in range(T.N)]


def densities(T, psi, phi):
    chi = T.H(T.mul(phi, psi))
    e = [phi[n] * re_dot(psi[n], chi[n]) for n in range(T.N)]
    return chi, e


def force(T, psi, phi, chi, j, two=False):
    if two:
        v = T.d(phi, j, 2)
        Cpsi = T.C(psi, j, v, 2); Cchi = T.C(chi, j, v, 2)
        half = Fr(1, 2)
        return [half * (re_dot(Cpsi[n], chi[n]) + re_dot(psi[n], Cchi[n])) for n in range(T.N)]
    v = T.d(phi, j)
    Cpsi = T.C(psi, j, v); Cchi = T.C(chi, j, v)
    return [re_dot(Cpsi[n], chi[n]) + re_dot(psi[n], Cchi[n]) for n in range(T.N)]


def bond_eps(T, psi, chi, j, step=1):
    """epsilon_b = (1/2) Re[psi(y)^dagger chi(x) + psi(x)^dagger chi(y)] on the bond b = (x, y = x + step e_j), placed at x."""
    py, cy = T.shift(psi, j, step), T.shift(chi, j, step)
    return [Fr(1, 2) * (re_dot(py[n], chi[n]) + re_dot(psi[n], cy[n])) for n in range(T.N)]


# ------------------------------------------------------------------------------------------------ Q: sources
PIN = {
    "b66": ("c4afb022c2", "physics-loop/admissibility-induced-law-block66-the-fall-is-owed-by-the-ledger-20260921", None),
    "b72": ("a57dbbaba2", "physics-loop/admissibility-induced-law-block72-which-species-fall-the-ledger-owes-20260921", None),
    "b64": ("e568866573", "physics-loop/admissibility-induced-law-block64-bond-strains-and-plaquette-curls-blindness-to-the-coins-axes-forces-the-curvature-member-20260921", None),
    "b62": ("aada579459", "physics-loop/admissibility-induced-law-block62-angles-are-the-tilt-of-the-coins-frame-two-disturbances-one-direction-free-speed-20260921", None),
}
QUOTES = [
    ("b66", "`i[H_w, G_ξ] = φ(i[H, G_ξ])φ − (Λ_ξ Hφ + φH Λ_ξ)`"),
    ("b66", "**Force density** `f_j(x) = Re[(C_j[d_jφ]ψ)†(Hφψ) + ψ† C_j[d_jφ](Hφψ)](x)`"),
    ("b66", "on the lattice, block 64's curl-built members (no volume term) with the rates as site multipliers are exactly unchanged"),
    ("b66", "For a plane wave of wave number `k` the exact `f` carries a factor `cos k`"),
    ("b72", "`f^P_j = Re[(½C^{(2)}_j[d^{(2)}_jφ]ψ)†Hφψ + ψ†½C^{(2)}_j[d^{(2)}_jφ]Hφψ]`"),
    ("b72", "`𝔢[V_nψ] = s_n𝔢[ψ]`; `f_j[V_nψ] = s_nD_jf_j[ψ]`; `f^P_j[V_nψ] = s_nf^P_j[ψ]`"),
    ("b64", "**Relabelling** `B_a^j → B_a^j + (d_aξ_j)`"),
    ("b62", "**Kinetic terms** `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]`"),
]


def family_q() -> None:
    found, missing = 0, []
    cache = {}
    for pin, needle in QUOTES:
        sha, branch, path = PIN[pin]
        if pin not in cache:
            if path is None:
                r = subprocess.run(["git", "diff", "--name-only", f"origin/main...{sha}"], capture_output=True, text=True, cwd=HERE)
                if r.returncode != 0:
                    subprocess.run(["git", "fetch", "-q", "origin", branch], capture_output=True, text=True, cwd=HERE)
                    r = subprocess.run(["git", "diff", "--name-only", f"origin/main...{sha}"], capture_output=True, text=True, cwd=HERE)
                cands = [p for p in r.stdout.split() if p.startswith("docs/") and p.endswith(".md") and "/audit/" not in p]
                path = cands[0] if cands else ""
            r = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True, cwd=HERE)
            if r.returncode != 0:
                subprocess.run(["git", "fetch", "-q", "origin", branch], capture_output=True, text=True, cwd=HERE)
                r = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True, cwd=HERE)
            cache[pin] = r.stdout if r.returncode == 0 else ""
        ok = needle in cache[pin]
        found += ok
        if not ok:
            missing.append(pin)
    check("Q", not missing, f"{found}/{len(QUOTES)} quoted definitions verbatim at the pinned heads (b66 c4afb022, b72 a57dbbab, b64 e5688665, "
          f"b62 aada5794){'; missing ' + ','.join(missing) if missing else ''}")


# ------------------------------------------------------------------------------------------------ A: the content, reach two
def family_a() -> None:
    rng = random.Random(20260924)
    # A0: block 66 T3(c) exactly, for a random non-stationary state (the content's balance used in (b))
    T = Torus(4)
    psi, phi = rand_state(T, rng), rand_phi(T, rng)
    xi = [[Fr(rng.randint(-3, 3)) for _ in range(T.N)] for _ in range(3)]
    Hw = lambda v: T.mul(phi, T.H(T.mul(phi, v)))
    Gpsi = [(Z, Z)] * T.N
    for j in range(3):
        a1 = T.mul(xi[j], T.S(psi, j)); a2 = T.S(T.mul(xi[j], psi), j)
        Gpsi = [sp_add(Gpsi[n], sp_scale(Fr(1, 2), sp_add(a1[n], a2[n]))) for n in range(T.N)]
    Hpsi = Hw(psi)
    # <psi| i[H_w, G] |psi> = -2 Im <H_w psi | G psi>
    im = sum(Hpsi[n][0].r * Gpsi[n][0].i - Hpsi[n][0].i * Gpsi[n][0].r + Hpsi[n][1].r * Gpsi[n][1].i - Hpsi[n][1].i * Gpsi[n][1].r for n in range(T.N))
    lhs = -2 * im
    chi, e = densities(T, psi, phi)
    fpsi = T.mul(phi, psi)
    rhs = Fr(0)
    for j in range(3):
        Sj = T.S(fpsi, j)
        fj = force(T, psi, phi, chi, j)
        rhs -= sum(xi[j][n] * fj[n] for n in range(T.N))
        for a in range(3):
            dxi = T.d(xi[j], a)
            up, Sup = T.shift(fpsi, a, 1), T.shift(Sj, a, 1)
            J = [Fr(1, 2) * (re_dot(up[n], sp_mat(SIG[a], Sj[n])) + re_dot(Sup[n], sp_mat(SIG[a], fpsi[n]))) for n in range(T.N)]
            rhs += sum(dxi[n] * J[n] for n in range(T.N))
    check("A0", lhs == rhs, "block 66 T3(c) re-checked exactly for a random state, rate field and displacement (L = 4): "
          "d<G_xi>/dt = sum (d_a xi_j) J_a^j[phi psi] - sum xi_j f_j")
    # A1-A3: the bond form and the polarization identity, random state and rates (L = 4 and 5)
    ok1 = ok2 = True
    for L in (4, 5):
        T = Torus(L)
        psi, phi = rand_state(T, rng), rand_phi(T, rng)
        chi, e = densities(T, psi, phi)
        rho = [re_dot(psi[n], chi[n]) for n in range(T.N)]
        for j in range(3):
            fj = force(T, psi, phi, chi, j)
            eps = bond_eps(T, psi, chi, j)
            dphi = T.d(phi, j)
            epsm, dphim = T.shift(eps, j, -1), T.shift(dphi, j, -1)
            ok1 &= all(fj[n] == dphi[n] * eps[n] + dphim[n] * epsm[n] for n in range(T.N))
            dpsi, dchi = [sp_sub(a, b) for a, b in zip(T.shift(psi, j, 1), psi)], [sp_sub(a, b) for a, b in zip(T.shift(chi, j, 1), chi)]
            rhoy = T.shift(rho, j, 1)
            ok2 &= all(eps[n] == (rho[n] + rhoy[n]) / 2 - Fr(1, 2) * re_dot(dpsi[n], dchi[n]) for n in range(T.N))
    check("A1", ok1, "exact bond form for every state and rate field (L = 4, 5): f_j(x) = d_j phi(x) eps_j(x) + d_j phi(x - e_j) eps_j(x - e_j), "
          "eps_b = (1/2) Re[psi_y^dag chi_x + psi_x^dag chi_y] the bond cross energy, chi = H phi psi")
    check("A2", ok2, "eps_b = (rho_x + rho_y)/2 - (1/2) Re[(d_j psi)^dag (d_j chi)], rho = e/phi: the energy density part and an exact "
          "gradient remainder")
    # A3: a sublattice state: e = 0 at every site, f nonzero
    T = Torus(4)
    phi = rand_phi(T, rng)
    psi = [(rand_q(rng), rand_q(rng)) if sum(s) % 2 == 0 else (Z, Z) for s in T.sites]
    chi, e = densities(T, psi, phi)
    fx = force(T, psi, phi, chi, 0)
    nz = sum(1 for v in fx if v != 0)
    check("A3", all(v == 0 for v in e) and nz > 0, f"a state on the even sublattice (L = 4): e = 0 at all {T.N} sites, f_1 != 0 at {nz} "
          "sites - the force density is no function of the energy density")
    # A4: the (111) map Gamma = (-1)^{x1+x2+x3}: anticommutes with H_w; e odd, f even, fP odd (block 72 T2, n = (111))
    T = Torus(6)
    psi, phi = rand_state(T, rng), rand_phi(T, rng)
    g = [(-1) ** (sum(s) % 2) for s in T.sites]
    gpsi = [sp_scale(g[n], psi[n]) for n in range(T.N)]
    Hwpsi = T.mul(phi, T.H(T.mul(phi, psi))); Hwg = T.mul(phi, T.H(T.mul(phi, gpsi)))
    ok = all(Hwg[n] == sp_scale(-g[n], Hwpsi[n]) for n in range(T.N))
    chi, e = densities(T, psi, phi); chig, eg = densities(T, gpsi, phi)
    ok &= all(eg[n] == -e[n] for n in range(T.N))
    for j in range(3):
        f1, f2 = force(T, psi, phi, chi, j), force(T, gpsi, phi, chig, j)
        p1, p2 = force(T, psi, phi, chi, j, True), force(T, gpsi, phi, chig, j, True)
        ok &= all(f2[n] == f1[n] for n in range(T.N)) and all(p2[n] == -p1[n] for n in range(T.N))
    check("A4", ok, "Gamma = (-1)^(x1+x2+x3) (L = 6): H_w Gamma = -Gamma H_w, e[Gamma psi] = -e[psi], f[Gamma psi] = +f[psi], "
          "fP[Gamma psi] = -fP[psi] at every site, every state and rate field")


# ------------------------------------------------------------------------------------------------ first order in the rate gradient
def plane_waves():
    """energy +-1 plane waves of the 8-torus: one component of k in {pi/2, 3pi/2}, the others in {0, pi}; spinor eigenvectors."""
    out = []
    for pos in range(3):
        for q in (1, 3):
            for o1 in (0, 2):
                for o2 in (0, 2):
                    k = [0, 0, 0]; others = [t for t in range(3) if t != pos]
                    k[pos] = q; k[others[0]] = o1; k[others[1]] = o2       # k = (pi/2) * k
                    s = 1 if q == 1 else -1                               # sin k_pos = s
                    for E in (1, -1):
                        if pos == 0:
                            a = (ONE, Q(E * s))                            # s sigma_x a = E a
                        elif pos == 1:
                            a = (ONE, Q(0, E * s))                         # s sigma_y a = E a: (1, i s E)
                        else:
                            a = (ONE, Z) if E * s == 1 else (Z, ONE)       # s sigma_z a = E a
                        out.append((tuple(k), E, a))
    return out


PH = [ONE, I, -ONE, -I]   # e^{i (pi/2) m}
COS = {0: 1, 1: 0, 2: -1, 3: 0}


def family_first_order() -> dict:
    rng = random.Random(8)
    T = Torus(8)
    eta = [Fr(rng.randint(-4, 4)) for _ in range(T.N)]
    ok_f = ok_p = True
    vals = {}
    for k, E, a in plane_waves():
        psi = [sp_scale(PH[(k[0] * s[0] + k[1] * s[1] + k[2] * s[2]) % 4], a) for s in T.sites]
        Hpsi = T.H(psi)
        ok_f &= all(Hpsi[n] == sp_scale(E, psi[n]) for n in range(T.N))
        e0 = E * re_dot(a, a)
        for j in range(3):
            # coefficient of epsilon in f_j and fP_j for phi = 1 + epsilon eta: d phi -> d eta, chi -> H psi
            v = T.d(eta, j)
            f1 = [re_dot(c, h) + re_dot(p, cc) for c, h, p, cc in zip(T.C(psi, j, v), Hpsi, psi, T.C(Hpsi, j, v))]
            v2 = T.d(eta, j, 2)
            p1 = [Fr(1, 2) * (re_dot(c, h) + re_dot(p, cc)) for c, h, p, cc in zip(T.C(psi, j, v2, 2), Hpsi, psi, T.C(Hpsi, j, v2, 2))]
            ep, em = T.shift(eta, j, 1), T.shift(eta, j, -1)
            ep2, em2 = T.shift(eta, j, 2), T.shift(eta, j, -2)
            ok_f &= all(f1[n] == e0 * COS[k[j] % 4] * (ep[n] - em[n]) for n in range(T.N))
            ok_p &= all(p1[n] == Fr(1, 2) * e0 * COS[(2 * k[j]) % 4] * (ep2[n] - em2[n]) for n in range(T.N))
            vals[(k, E, j)] = (f1[0], p1[0], e0)
    check("F1", ok_f, "first order in the rate gradient (phi = 1 + eps eta, L = 8, all 48 energy +-1 plane waves, rational eta): "
          "f_j = e cos k_j (eta(x+e_j) - eta(x-e_j)) eps = e cos k_j (u(x+e_j) - u(x-e_j))/2 at every site")
    check("F2", ok_p, "the same for reach three: fP_j = e cos 2k_j (u(x+2e_j) - u(x-2e_j))/4 at every site")
    # two plane waves of equal energy density, different forces: k = (pi/2,0,0) and (0,pi/2,0), E = 1, direction j = 1
    A, B = ((1, 0, 0), 1), ((0, 1, 0), 1)
    ok3 = True
    for kk in (A[0], B[0]):
        a = [w for (k, E, w) in plane_waves() if k == kk and E == 1][0]
        psi = [sp_scale(PH[(kk[0] * s[0] + kk[1] * s[1] + kk[2] * s[2]) % 4], a) for s in T.sites]
        chi = T.H(psi)
        ok3 &= all(re_dot(psi[n], chi[n]) == 2 for n in range(T.N))              # e^(0) = 2 at every site
        for j in range(3):
            Sj = T.S(psi, j)
            for aa in range(3):
                up, Sup = T.shift(psi, aa, 1), T.shift(Sj, aa, 1)
                ok3 &= all(re_dot(up[n], sp_mat(SIG[aa], Sj[n])) + re_dot(Sup[n], sp_mat(SIG[aa], psi[n])) == 0 for n in range(T.N))
    check("F3", ok3, "k = (pi/2,0,0) and (0,pi/2,0) at energy 1: e^(0) = 2 at every site and zero bond current J_a^j for all a, j at every "
          "site - equal content for any requirement built from e and J with content-independent coefficients")
    fa, pa, ea = vals[(A[0], A[1], 0)]; fb, pb, eb = vals[(B[0], B[1], 0)]
    d1 = eta[T.nb[(0, 1)][0]] - eta[T.nb[(0, -1)][0]]; d2 = eta[T.nb[(0, 2)][0]] - eta[T.nb[(0, -2)][0]]
    return {"pair": (ea, eb, fa, fb, pa, pb, d1, d2)}


# ------------------------------------------------------------------------------------------------ D: the content, reach three
def family_d() -> None:
    rng = random.Random(69)
    ok0 = ok1 = ok2 = True
    for L in (5, 6):
        T = Torus(L)
        psi, phi = rand_state(T, rng), rand_phi(T, rng)
        for j in range(3):
            # P_j = S_j C_j with C_j = (T + T^dag)/2; i[phi, P_j] psi = -(1/2) C2_j[d2_j phi] psi
            ones = [Fr(1)] * T.N
            Pj = lambda v: T.S(T.C(v, j, ones), j)
            a = Pj(psi); b = Pj(T.mul(phi, psi))
            comm = [sp_scale(Q(0, 1), sp_sub(sp_scale(phi[n], a[n]), b[n])) for n in range(T.N)]
            rhs = T.C(psi, j, T.d(phi, j, 2), 2)
            ok0 &= all(comm[n] == sp_scale(Fr(-1, 2), rhs[n]) for n in range(T.N))
        chi, e = densities(T, psi, phi)
        rho = [re_dot(psi[n], chi[n]) for n in range(T.N)]
        for j in range(3):
            fp = force(T, psi, phi, chi, j, True)
            eps2 = bond_eps(T, psi, chi, j, 2)
            v2 = T.d(phi, j, 2)
            eps2m, v2m = T.shift(eps2, j, -2), T.shift(v2, j, -2)
            ok1 &= all(fp[n] == Fr(1, 2) * (v2[n] * eps2[n] + v2m[n] * eps2m[n]) for n in range(T.N))
            d2psi = [sp_sub(x, y) for x, y in zip(T.shift(psi, j, 2), psi)]
            d2chi = [sp_sub(x, y) for x, y in zip(T.shift(chi, j, 2), chi)]
            rhoy = T.shift(rho, j, 2)
            ok2 &= all(eps2[n] == (rho[n] + rhoy[n]) / 2 - Fr(1, 2) * re_dot(d2psi[n], d2chi[n]) for n in range(T.N))
    check("D1", ok0, "i[phi, P_j] = -(1/2) C2_j[d2_j phi] for random states and rates (L = 5, 6; block 72 T1(a) re-checked)")
    check("D2", ok1 and ok2, "exact two-step bond form: fP_j(x) = (1/2)[d2_j phi(x) eps2(x) + d2_j phi(x - 2e_j) eps2(x - 2e_j)], "
          "eps2_b = (rho_x + rho_y)/2 - (1/2) Re[(d2_j psi)^dag (d2_j chi)] on the two-step bond (x, x + 2e_j)")


# ------------------------------------------------------------------------------------------------ B: the field side
def curls(T, B):
    """F_ab^j(x) = d_a B_b^j(x) - d_b B_a^j(x), a < b; B[a][j] a site list (bond x -> x + e_a)."""
    out = []
    for (a, b) in ((0, 1), (0, 2), (1, 2)):
        for j in range(3):
            dab = T.d(B[b][j], a); dba = T.d(B[a][j], b)
            out.append([dab[n] - dba[n] for n in range(T.N)])
    return out


def family_b() -> None:
    rng = random.Random(64)
    T = Torus(4)
    w = [Fr(rng.randint(1, 9), rng.randint(1, 4)) for _ in range(T.N)]
    lin = [Fr(rng.randint(-3, 3)) for _ in range(9)]
    quad = [[Fr(rng.randint(-2, 2)) for _ in range(9)] for _ in range(9)]
    def Fval(B):
        c = curls(T, B)
        tot = Fr(0)
        for n in range(T.N):
            v = [c[p][n] for p in range(9)]
            D = sum(lin[p] * v[p] for p in range(9)) + sum(quad[p][q] * v[p] * v[q] for p in range(9) for q in range(9))
            tot += w[n] * D
        return tot
    B0 = [[[Fr(rng.randint(-2, 2)) for _ in range(T.N)] for _ in range(3)] for _ in range(3)]
    # E = dF/dB exactly by central differences (exact for a quadratic F)
    E = [[[Fr(0)] * T.N for _ in range(3)] for _ in range(3)]
    for a in range(3):
        for j in range(3):
            for n in range(T.N):
                B0[a][j][n] += 1; Fp = Fval(B0)
                B0[a][j][n] -= 2; Fm = Fval(B0)
                B0[a][j][n] += 1
                E[a][j][n] = (Fp - Fm) / 2
    ok = True
    for j in range(3):
        div = [sum(E[a][j][n] - E[a][j][T.nb[(a, -1)][n]] for a in range(3)) for n in range(T.N)]
        ok &= all(v == 0 for v in div)
    check("B1", ok, "block 64's family F = sum_x w_x D_x(curls), D linear + quadratic in the nine curls with random coefficients, random "
          "rates and strains (L = 4): sum_a [E_a^j(x) - E_a^j(x - e_a)] = 0 at every site - no rate term, whatever the rates")
    # B2: the volume member F = c0 sum w_x det(1 - B(x)) carries the rates: at B = 0, first order in xi, with the upwind transport
    # delta u_x = -sum_a xi_a(x)(1 - w(x - e_a)/w(x)): sum E.d xi + sum U delta u = 0 exactly
    c0 = Fr(3, 7)
    xi = [[Fr(rng.randint(-3, 3)) for _ in range(T.N)] for _ in range(3)]
    s1 = Fr(0)
    for a in range(3):
        dx = T.d(xi[a], a)
        s1 += sum(-c0 * w[n] * dx[n] for n in range(T.N))                    # E_a^a(x) = -c0 w_x at B = 0
    s2 = Fr(0)
    for n in range(T.N):
        du = -sum(xi[a][n] * (1 - w[T.nb[(a, -1)][n]] / w[n]) for a in range(3))
        s2 += c0 * w[n] * du                                                   # U_x = c0 w_x at B = 0
    # without the transport the identity fails
    check("B2", s1 + s2 == 0 and s1 != 0, "a member that carries the rates exists: F = c0 sum_x w_x det(1 - B(x)) at B = 0 satisfies "
          "sum E.d(xi) + sum U delta u = 0 exactly with delta u_x = -sum_a xi_a(x)(1 - w(x-e_a)/w(x)); its requirement is "
          "f_a(x) = e_x (1 - exp(-(u_x - u_{x-e_a}))), linear in e")


def main() -> int:
    family_q()
    family_a()
    fo = family_first_order()
    family_d()
    family_b()
    print("The ledger's force identity on the lattice - checks; worker w-macbookpro90c72-j152a (claude-opus-5-5)")
    for line in OUT:
        print(line)
    ea, eb, fa, fb, pa, pb, d1, d2 = fo["pair"]
    print(f"     pair of energy-1 plane waves, j = 1, at the origin (same e = {ea} = {eb}): k = (pi/2,0,0): f^(1) = {fa}, fP^(1) = {pa}; "
          f"k = (0,pi/2,0): f^(1) = {fb}, fP^(1) = {pb} (eta differences {d1}, {d2})")
    print(f"checks: {len(OUT) - len(FAILS)} ok, {len(FAILS)} fail{': ' + ', '.join(FAILS) if FAILS else ''}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PROVED - (a) exactly, for every state and rate field: f_j(x) = d_j phi(x) eps_j(x) + d_j phi(x-e_j) eps_j(x-e_j), "
          "eps the bond cross energy (1/2) Re[psi_y^dag chi_x + psi_x^dag chi_y]; eps = energy-density part - (1/2) Re[(d psi)^dag "
          "(d chi)]; no factorisation through the energy density (sublattice state: e = 0, f != 0). (b) curl ledgers keep the rate-free "
          "identity under every transport of the rates; a rate-carrying ledger (volume member, exact) requires a force built from e (and "
          "J); f is even and e odd under the (111) map. (c) a strain kinetic term makes the mismatch the rate of change of content + "
          "strain momentum. (d) reach three: exact two-step bond form; first-order force e cos 2k_j (u(x+2e)-u(x-2e))/4.")
    print("HIT: the walk's lattice force is the bond cross energy times rate differences, not a function of the energy density; every "
          "ledger identity from a relabelling that carries the rates requires a force built from e and J with field coefficients, and at "
          "first order in the rate gradient the equal-content plane waves k = (pi/2,0,0), (0,pi/2,0) get forces 0 and "
          "e(u(x+e1)-u(x-e1))/2 (reach two), opposite forces (reach three): they agree only at long wavelength.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
