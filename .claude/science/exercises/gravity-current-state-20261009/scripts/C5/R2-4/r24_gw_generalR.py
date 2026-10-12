"""R2-4 check A2b: general (multilinear, W(B_d)-symmetric, hypercube-range) R = r(p) in the GW relation
a = r (a^2 + |b|^2), with a(0)=0, B_mu(0)=1 and a != 0 at every doubler corner (Rabinowitsch variable t).
Groebner basis over QQ; GB == [1] means no complex solution, hence no real one."""
import itertools, signal, sympy as sp
def esym(v, k):
    return sp.Integer(1) if k == 0 else sp.Add(*[sp.Mul(*c) for c in itertools.combinations(v, k)])
def run(d):
    c = sp.symbols('c0:%d' % d); al = sp.symbols('al0:%d' % (d+1)); be = sp.symbols('be0:%d' % d)
    rh = sp.symbols('rh0:%d' % (d+1)); t = sp.Symbol('t')
    a = sum(al[k]*esym(c, k) for k in range(d+1))
    B = [sum(be[k]*esym([c[n] for n in range(d) if n != m], k) for k in range(d)) for m in range(d)]
    b2 = sum((1-c[m]**2)*B[m]**2 for m in range(d))
    r = sum(rh[k]*esym(c, k) for k in range(d+1))
    ident = sp.expand(a - r*(a**2 + b2))
    eqs = list(sp.Poly(ident, *c).coeffs())
    one = {x: 1 for x in c}
    eqs += [sp.expand(a.subs(one)), sp.expand(B[0].subs(one) - 1)]
    # doubler corners: by S_d symmetry a at a corner depends only on the number j of -1 entries
    corner_vals = []
    for j in range(1, d+1):
        sub = {c[i]: (-1 if i < j else 1) for i in range(d)}
        corner_vals.append(sp.expand(a.subs(sub)))
    eqs.append(sp.expand(t*sp.Mul(*corner_vals) - 1))
    gens = list(al) + list(be) + list(rh) + [t]
    G = sp.groebner(eqs, *gens, order='grevlex')
    print(f"d={d}: unknowns={len(gens)} equations={len(eqs)}  Groebner basis = {list(G.exprs) if len(G.exprs) < 6 else str(len(G.exprs))+' polys'}")
    return G
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError()))
for d in (1, 2, 3, 4):
    signal.alarm(240)
    try:
        G = run(d)
        if d == 1:
            print("   d=1 control: solutions exist (basis != [1]); e.g. Wilson r=1 with r(p)=1/2")
    except TimeoutError:
        print(f"d={d}: Groebner timed out (240 s)")
    signal.alarm(0)
