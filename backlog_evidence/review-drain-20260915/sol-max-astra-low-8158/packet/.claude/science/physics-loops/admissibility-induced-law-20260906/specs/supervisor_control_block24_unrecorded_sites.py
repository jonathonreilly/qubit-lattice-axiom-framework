"""Control, block 24 (supervisor): unrecorded sites — the free-window reading (R1) versus the integrated-exterior reading (R2).
Six-axis menu M = {+-e_i}, product rule phi(v,v') = p (same), q (antipodal), r (orthogonal).
(a) one exterior site adjacent to two recorded sites: the effective factor is phi^2(v1, v2); its nontrivial eigenvalues (p-q)^2, (p+q-2r)^2;
    constant iff p = q = r (symbolic);
(b) one attachment: an exterior path of two sites hanging off one recorded site b: the factor is constant in v_b (exact, any (p,q,r) sample);
    two attachments: an exterior path of two sites bridging b1, b2: nonconstant (exact);
(c) the plaquette W (4 sites) plus one exterior site adjacent to two adjacent corners: exact TV distance between R1 and R2 at (3,1,2), (5,2,4), (2,1,2);
(d) the 2x2x2 cube: W = a face, E = the opposite face (connected, attached to all four W-sites): TV(R1, R2) at (3,1,2);
(e) the sphere rule e^{beta s.s'}: one attachment factor 4 pi sinh(beta)/beta (constant); two attachments through one site: 4 pi sinh(beta|v1+v2|)/(beta|v1+v2|)
    with |v1+v2|^2 = 2 + 2 v1.v2 — nonconstant (symbolic derivative in t = v1.v2 nonzero);
(f) a forest of one-attachment components on a 3x3 window: R1 = R2 exactly."""
from fractions import Fraction as F
from itertools import product
import sympy as sp
M = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def rel(v, w):
    if v == w: return "same"
    if tuple(-c for c in v) == w: return "anti"
    return "orth"
def phi(v, w, p, q, r):
    return {"same": p, "anti": q, "orth": r}[rel(v, w)]
p, q, r = sp.symbols("p q r", positive=True)
Phi = sp.Matrix(6, 6, lambda i, j: phi(M[i], M[j], p, q, r))
ev = Phi.eigenvals()
print("(a) eigenvalues of phi:", {sp.simplify(k): v for k, v in ev.items()})
Phi2 = Phi * Phi
diff = sp.simplify(Phi2[0, 0] - Phi2[0, 2])  # same vs orthogonal entry of phi^2
print("(a) phi^2 same-entry minus orth-entry =", sp.factor(diff), "; anti minus orth =", sp.factor(sp.simplify(Phi2[0, 1] - Phi2[0, 2])))
print("(a) constant iff p = q = r:", sp.solve([sp.simplify(Phi2[0,0]-Phi2[0,2]), sp.simplify(Phi2[0,1]-Phi2[0,2])], [p, q], dict=True))
def weight_sum(bonds, fixed, free_sites, pv):
    # sum over records on free_sites of the product of phi over bonds (integer weights)
    tot = 0
    for u in product(range(6), repeat=len(free_sites)):
        rec = dict(fixed); rec.update({s: M[k] for s, k in zip(free_sites, u)})
        w = 1
        for a, b in bonds:
            w *= phi(rec[a], rec[b], *pv)
        tot += w
    return tot
pv = (3, 1, 2)
# (b) one attachment: b - u1 - u2 ; two attachments: b1 - u1 - u2 - b2
one = {v: weight_sum([("b","u1"),("u1","u2")], {"b": v}, ["u1","u2"], pv) for v in M}
print("(b) one-attachment factor over v_b:", set(one.values()), "(constant:", len(set(one.values())) == 1, ")")
two = {(v1, v2): weight_sum([("b1","u1"),("u1","u2"),("u2","b2")], {"b1": v1, "b2": v2}, ["u1","u2"], pv) for v1 in M for v2 in M}
print("(b) two-attachment factor values by relation:", {k: two[(M[0], M[j])] for k, j in (("same",0),("anti",1),("orth",2))}, "(constant:", len(set(two.values())) == 1, ")")
# (c) plaquette + one exterior site adjacent to corners c0, c1
def law(bonds, sites, pv):
    Z = 0; wts = {}
    for u in product(range(6), repeat=len(sites)):
        rec = {s: M[k] for s, k in zip(sites, u)}
        w = 1
        for a, b in bonds: w *= phi(rec[a], rec[b], *pv)
        wts[u] = w; Z += w
    return {k: F(v, Z) for k, v in wts.items()}
def marginal(lawd, sites, keep):
    idx = [sites.index(s) for s in keep]
    out = {}
    for u, w in lawd.items():
        key = tuple(u[i] for i in idx); out[key] = out.get(key, F(0)) + w
    return out
def tv(a, b):
    keys = set(a) | set(b); return sum(abs(a.get(k, F(0)) - b.get(k, F(0))) for k in keys) / 2
W = ["c0","c1","c2","c3"]; Wb = [("c0","c1"),("c1","c2"),("c2","c3"),("c3","c0")]
for pvv in ((3,1,2), (5,2,4), (2,1,2)):
    R1 = law(Wb, W, pvv)
    R2 = marginal(law(Wb + [("c0","x"),("c1","x")], W + ["x"], pvv), W + ["x"], W)
    d = tv(R1, R2)
    print(f"(c) plaquette + one exterior site on corners c0,c1 at {pvv}: TV(R1,R2) = {d} = {float(d):.5f}")
# (d) cube: W = bottom face f0..f3, E = top face t0..t3
Wc = ["f0","f1","f2","f3"]; Ec = ["t0","t1","t2","t3"]
Wcb = [("f0","f1"),("f1","f2"),("f2","f3"),("f3","f0")]
Eb = [("t0","t1"),("t1","t2"),("t2","t3"),("t3","t0")] + [(f"f{i}", f"t{i}") for i in range(4)]
R1 = law(Wcb, Wc, pv); R2 = marginal(law(Wcb + Eb, Wc + Ec, pv), Wc + Ec, Wc)
print(f"(d) cube, face vs opposite face integrated out at (3,1,2): TV = {tv(R1,R2)} = {float(tv(R1,R2)):.5f}")
# (e) sphere
beta, t = sp.symbols("beta t", positive=True)
one_s = 4 * sp.pi * sp.sinh(beta) / beta
two_s = 4 * sp.pi * sp.sinh(beta * sp.sqrt(2 + 2 * t)) / (beta * sp.sqrt(2 + 2 * t))
print("(e) sphere one-attachment factor:", one_s, "(no v-dependence); two-attachment factor derivative in t at t = 0:", sp.simplify(sp.diff(two_s, t).subs(t, 0)))
# (f) forest of one-attachment components on the plaquette: a pendant path p1-p2 off c0 and a pendant site p3 off c2
pend = [("c0","p1"),("p1","p2"),("c2","p3")]
sites = W + ["p1", "p2", "p3"]
R1 = law(Wb, W, (2, 1, 2))
R2 = marginal(law(Wb + pend, sites, (2, 1, 2)), sites, W)
print(f"(f) plaquette with two pendant exterior components at (2,1,2): TV(R1,R2) = {tv(R1,R2)}")
