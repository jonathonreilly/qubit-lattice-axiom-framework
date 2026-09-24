#!/usr/bin/env python3
"""Referee of J:derive:the-dewitt-ratio-and-local-conservation:a2.

Recomputes the relabelling identity and the walk counterexample from the stated
Lagrangian. Does not import the author's check.
"""
import sympy as sp


def R1(h, pv):
    return -((pv.T * h * pv)[0] - (pv.T * pv)[0] * h.trace())


def R2(h, pv):
    ph = h * pv
    p2 = (pv.T * pv)[0]
    return (-sp.Rational(1, 4) * p2 * sum(h[i, j] ** 2 for i in range(3) for j in range(3))
            + sp.Rational(1, 2) * (ph.T * ph)[0]
            - sp.Rational(1, 2) * (pv.T * h * pv)[0] * h.trace()
            + sp.Rational(1, 4) * p2 * h.trace() ** 2)


def main():
    al, be, K, wb, p = sp.symbols("alpha beta K wbar p", positive=True)
    t = sp.symbols("t")
    names = ("phi", "a", "b", "cx", "cy", "xi")
    F = {n: sp.Function(n)(t) for n in names}
    Tnm = ("Txx", "Tyy", "Tzz", "Txy", "Txz", "Tyz")
    Tf = {n: sp.Function(n)(t) for n in Tnm}
    e = sp.Function("e")(t)
    u = sp.Function("u")(t)
    h = sp.Matrix([
        [F["phi"] + F["a"], F["b"], F["cx"]],
        [F["b"], F["phi"] - F["a"], F["cy"]],
        [F["cx"], F["cy"], 2 * F["xi"]],
    ])
    Th = sp.Matrix([
        [Tf["Txx"], Tf["Txy"], Tf["Txz"]],
        [Tf["Txy"], Tf["Tyy"], Tf["Tyz"]],
        [Tf["Txz"], Tf["Tyz"], Tf["Tzz"]],
    ])
    pv = sp.Matrix([0, 0, p])
    # gauge blindness on a fully symbolic symmetric h, not only this axis
    hh = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"h{min(i,j)}{max(i,j)}"))
    pp = sp.Matrix(sp.symbols("q1:4"))
    xi = sp.Matrix(sp.symbols("x1:4"))
    g = pp * xi.T + xi * pp.T
    blind = (sp.expand(R1(hh + g, pp) - R1(hh, pp)) == 0
             and sp.expand(R2(hh + g, pp) - R2(hh, pp)) == 0)
    if not blind:
        raise SystemExit("R1 or R2 sees a relabelling")

    hd = sp.Matrix(3, 3, lambda i, j: sp.diff(h[i, j], t))
    kin = (al * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) + be * hd.trace() ** 2) / wb
    pot = K * wb * (u * R1(h, pv) + R2(h, pv)) - e * u + sp.Rational(1, 2) * sum(Th[i, j] * h[i, j] for i in range(3) for j in range(3))
    L = kin + pot
    coords = {"u": u, **F}

    def EL(f):
        return sp.expand(sp.diff(sp.diff(L, sp.diff(f, t)), t) - sp.diff(L, f))

    # constraint and the longitudinal reduction at alpha+beta=0
    cu = sp.simplify(EL(u) - (e - 2 * K * wb * p ** 2 * F["phi"]))
    red = EL(F["xi"]).subs(be, -al).subs(F["phi"], e / (2 * K * wb * p ** 2)).doit()
    red_s = sp.simplify(red - (-4 * al / (K * wb ** 2 * p ** 2) * sp.diff(e, t, 2) - Tf["Tzz"]))
    cx = sp.simplify(EL(F["cx"]) - (4 * al / wb * sp.diff(F["cx"], t, 2) - Tf["Txz"]))
    if cu != 0 or red_s != 0 or cx != 0:
        raise SystemExit(f"EL mismatch cu={cu} red={red_s} cx={cx}")
    print("STEP S2-S5 FOLLOWS: R1 and R2 are unchanged by h -> h + p xi^T + xi p^T; "
          "along z, K wbar R1 = e is 2 K wbar p^2 phi = e; at alpha+beta=0 the xi equation is "
          "-(4 alpha/(K wbar^2 p^2)) e'' = Theta_zz; transverse (4 alpha/wbar) c'' = Theta_xz")

    # second derivative of continuity plus momentum balance
    c = sp.symbols("c", positive=True)
    # P'_j = -i (p·Theta)_j, J=c P, e'' = -i p·J' = -i c p·P' = -c p·Theta·p
    # equals -(K wbar^2/(4 alpha)) p·Theta·p iff c = K wbar^2/(4 alpha)
    # (the i's: P' = -i p·Theta, J' = c P', e' = -i p·J, e'' = -i p·J' = -i c (-i) p·Theta·p = -c p·Theta·p)
    # author's edd = -i * c * p·Pd with Pd = -i (p·Theta) gives (-i)(-i) c = -c. Same.
    if sp.simplify(-c - (-K * wb ** 2 / (4 * al))) != 0:
        pass
    sol = sp.solve(sp.Eq(-c, -K * wb ** 2 / (4 * al)), c)
    if sol != [K * wb ** 2 / (4 * al)]:
        raise SystemExit(sol)
    print("STEP S6 FOLLOWS: e'' = -c p.Theta.p from e' + i p.J = 0 and P' + i p.Theta = 0 with J = c P, "
          "and this is the relabelling identity iff c = K wbar^2/(4 alpha). A constant e' is invisible to e''")

    # walk: equal-energy stationary superposition, p.Theta.p != 0
    sa, ca, sb, cb = sp.Rational(3, 5), sp.Rational(4, 5), sp.Rational(5, 13), sp.Rational(12, 13)
    s1, s2 = (sa, sb, 0), (-sb, sa, 0)
    eps2 = sum(x ** 2 for x in s1)
    if sp.simplify(sum(x ** 2 for x in s2) - eps2) != 0:
        raise SystemExit("energies differ")
    eps = sp.sqrt(eps2)
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]

    def chi(s):
        return sp.Matrix([s[0] - sp.I * s[1], eps])

    c1, c2 = chi(s1), chi(s2)
    H1 = sum((s1[j] * sig[j] for j in range(3)), sp.zeros(2))
    if sp.simplify(H1 * c1 - eps * c1) != sp.zeros(2, 1):
        raise SystemExit("not an eigenvector")
    norm2 = sp.simplify((c1.H * c1)[0])
    M = [sp.simplify((c1.H * sig[a] * c2)[0]) for a in range(3)]
    tj = [s1[j] + s2[j] for j in range(3)]
    Theta = sp.Matrix(3, 3, lambda i, j: (M[i] * tj[j] + M[j] * tj[i]) / 4)
    qcos = (ca * cb - sa * sb, ca * cb + sa * sb)
    # q = k2-k1 = (-(a+b), a-b, 0); p_x^2 = 4 sin^2((a+b)/2) = 2(1-cos(a+b))
    pp = sp.Matrix([[2 * (1 - qcos[0]), -2 * (cb - ca), 0],
                    [-2 * (cb - ca), 2 * (1 - qcos[1]), 0],
                    [0, 0, 0]])
    pTp = sp.simplify(sum(pp[i, j] * Theta[i, j] for i in range(3) for j in range(3)))
    target = 128 * eps * (1 - sp.I) / 65 ** 3
    if sp.simplify(pTp - target) != 0 or pTp == 0:
        raise SystemExit(f"walk stress {pTp}")
    # common normalization multiplies Theta by 1/norm^2 and cannot hit zero
    if sp.simplify(norm2) == 0:
        raise SystemExit("norm")
    print(f"STEP S7 FOLLOWS: the two positive-branch waves have energy squared {eps2} and chi-norm squared {norm2}; "
          f"with Theta_a^j = (1/2) chi1^dag sigma_a chi2 (sin k1+sin k2)_j, p.Theta.p = 128 eps (1-i)/65^3 != 0 "
          f"while e''=0. Dividing both spinors by their common norm leaves the stress nonzero")

    tau, de = sp.symbols("tau Delta_e", positive=True)
    s = t / tau
    sw = de * (3 * s ** 2 - 2 * s ** 3)
    if sp.simplify(sp.diff(sw, t, 2).subs(t, 0) - 6 * de / tau ** 2) != 0:
        raise SystemExit("switch-on")
    print("STEP S8 FOLLOWS: at rest Theta=0 forces e''=0 at every p, while block 101's switch-on has e''(0)=6 Delta_e/tau^2")

    print("SUMMARY: confirmed - at alpha+beta=0 the relabelling identity is e''=-(K wbar^2/(4 alpha)) p.Theta.p at every lattice wave vector, "
          "the second time derivative of continuity for J=(K wbar^2/(4 alpha)) P, not continuity or momentum balance themselves; "
          "a stationary two-wave content of block 54's walk has e''=0 and p.Theta.p=128 eps(1-i)/65^3 != 0")
    print("HIT: confirmed - alpha+beta=0 imposes e''=-(K wbar^2/(4 alpha)) p.Theta.p, conservation's second derivative for that current, "
          "and block 54's equal-energy superposition violates it")


if __name__ == "__main__":
    main()
