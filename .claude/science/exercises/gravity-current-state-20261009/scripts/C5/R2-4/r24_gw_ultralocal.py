"""R2-4 check A2: no ultralocal (hypercube-range) W(B_d)-covariant free Ginsparg-Wilson operator.

Free lattice Dirac operator with the hypercubic symmetries:
    D(p) = a(p) + i gamma.b(p),   a even in every p_mu, b_mu odd in p_mu, even in the others.
Hypercube range (every coupling inside the unit hypercube, |x_mu| <= 1) means
    a   = multilinear polynomial in c_mu = cos p_mu, symmetric under S_d,
    b_mu= sin p_mu * multilinear symmetric polynomial in the other c_nu.
(Nearest-neighbour on axes is the sub-case alpha_k = beta_k = 0 for k >= 2.)

GW relation {g5, D} = 2 D g5 R D with R = r(p) * 1 (trivial in Dirac space):
    since g5 (a + i g.b) g5 = a - i g.b,  D g5 D = g5 (a - i g.b)(a + i g.b) = g5 (a^2 + |b|^2)
    so GW <=> a = r (a^2 + |b|^2)  (canonical R = 1/2:  2a = a^2 + |b|^2).
Physical requirements: a(0) = 0 (massless at origin), b_mu ~ p_mu (B_mu(c=1) = 1),
and D invertible at the 2^d - 1 doubler corners (a != 0 there, since b = 0 at corners).
Exact sympy solve of the polynomial identity in c_mu (sin^2 = 1 - c^2).
"""
import itertools, sympy as sp

def esym(vars_, k):
    if k == 0:
        return sp.Integer(1)
    return sp.Add(*[sp.Mul(*comb) for comb in itertools.combinations(vars_, k)])

def run(d, general_R, rmax_range=None):
    c = sp.symbols('c0:%d' % d)
    al = sp.symbols('al0:%d' % (d + 1))
    be = sp.symbols('be0:%d' % d)
    a = sum(al[k] * esym(c, k) for k in range(d + 1))
    B = []
    for mu in range(d):
        others = [c[nu] for nu in range(d) if nu != mu]
        B.append(sum(be[k] * esym(others, k) for k in range(d)))
    b2 = sum((1 - c[mu] ** 2) * B[mu] ** 2 for mu in range(d))
    unknowns = list(al) + list(be)
    if general_R:
        rh = sp.symbols('rh0:%d' % (d + 1))
        r = sum(rh[k] * esym(c, k) for k in range(d + 1))
        unknowns += list(rh)
        ident = sp.expand(a - r * (a ** 2 + b2))
    else:
        ident = sp.expand(2 * a - (a ** 2 + b2))
    poly = sp.Poly(ident, *c)
    eqs = [sp.Eq(co, 0) for co in poly.coeffs()]
    # physical normalisation: a(c=1)=0 and B_mu(c=1)=1
    one = {ci: 1 for ci in c}
    eqs.append(sp.Eq(a.subs(one), 0))
    eqs.append(sp.Eq(B[0].subs(one), 1))
    sols = sp.solve(eqs, unknowns, dict=True)
    print(f"d={d}  R={'general multilinear r(p)' if general_R else 'canonical 1/2'}  "
          f"#unknowns={len(unknowns)}  #equations={len(eqs)}  #solutions={len(sols)}")
    good = 0
    for s in sols:
        aa = sp.simplify(a.subs(s))
        # values of a at doubler corners (c_mu = +/-1, not all +1)
        corner_vals = []
        for signs in itertools.product([1, -1], repeat=d):
            if all(x == 1 for x in signs):
                continue
            corner_vals.append(sp.simplify(aa.subs({c[i]: signs[i] for i in range(d)})))
        doubler_free = all(v != 0 for v in corner_vals)
        free_params = [u for u in unknowns if u not in s]
        print("   solution:", {k: v for k, v in s.items()}, " free:", free_params)
        print("     a(p) =", aa, "  a at doubler corners:", corner_vals[:6], "..." if len(corner_vals) > 6 else "")
        print("     doubler-free (all corners a != 0 for generic free params):", doubler_free)
        good += doubler_free
    print(f"   => doubler-free GW solutions in class: {good}\n")
    return good

if __name__ == "__main__":
    print("Control d=1 (expect a solution: 1D Wilson r=1 satisfies canonical GW):")
    run(1, False)
    for d in (2, 3, 4):
        run(d, False)
    # general R: see r24_gw_generalR.py (Groebner; sympy.solve cannot handle it)
