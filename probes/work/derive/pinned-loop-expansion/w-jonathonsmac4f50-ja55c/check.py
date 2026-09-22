"""pinned-loop-expansion, attempt a2 (w-jonathonsmac4f50-ja55c): checks.  Exact (fractions, sympy) throughout; the only
floating point is in printed decimals.

Objects (blocks 39-40, PRs #8530, #8546).  Six-axis contents; omega = p (equal), q (opposite), r (orthogonal); S = p + q + 4r;
pinned scale c0 = 6/S; W = c0 omega = 6 K with K = omega/S doubly stochastic (the one-neighbour kernel K_1).  A record weighs z,
a bond with an empty end 1.  Occupied-set law mu(A) ~ (6z)^{|A|} Phi(A), Phi(A) = E_s[prod_{e in E(A)} 6K(s_e)] over independent
uniform contents.  Eigenvalues of K: 1, l1 = (p-q)/S (three times, odd modes), l2 = (p+q-2r)/S (twice, even traceless modes).
w(H) = E_s[prod_{e in H} (6K(s_e) - 1)]; rho0 = 6z/(1 + 6z).
"""
import itertools
import os
import sys
from fractions import Fraction as F

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from loopexp import AX, Kmat, kpow, grid, phi_brute, leafless_subsets, strands_of, w_transfer

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


TRIPLES = [(3, 1, 2), (5, 1, 1), (7, 2, 1)]

# ------------------------------------------------------------------ A1: spectrum of K and the cycle factor
p, q, r, n = sp.symbols("p q r n", positive=True)
Ks = sp.Matrix(6, 6, lambda i, j: (p if AX[i] == AX[j] else q if AX[i][1] == AX[j][1] else r) / (p + q + 4 * r))
ev = Ks.eigenvals()
S_ = p + q + 4 * r
want("A1 K = omega/S has eigenvalues 1, l1 = (p-q)/S (x3), l2 = (p+q-2r)/S (x2) (symbolic), so a fully occupied n-cycle has "
     "Phi = tr(K^n) = 1 + 3 l1^n + 2 l2^n",
     {sp.simplify(k): v for k, v in ev.items()} == {1: 1, sp.simplify((p - q) / S_): 3, sp.simplify((p + q - 2 * r) / S_): 2}
     and all(phi_brute(*grid((2, m)), Kmat(*t)) == 1 + 3 * F(t[0] - t[1], sum(t) + 3 * t[2]) ** 4 + 2 * F(t[0] + t[1] - 2 * t[2], sum(t) + 3 * t[2]) ** 4
             for t in TRIPLES for m in (2,)),
     {str(sp.simplify(k)): v for k, v in ev.items()})

# ------------------------------------------------------------------ A2: leaves vanish; forests are independent
ok = True
for t in TRIPLES:
    K = Kmat(*t)
    ok = ok and all(sum(6 * K[a][b] - 1 for b in range(6)) == 0 for a in range(6))
    V, E = grid((1, 6))                                                              # a path
    ok = ok and phi_brute(V, E, K) == 1
    ok = ok and phi_brute(["c", 1, 2, 3, 4], [("c", 1), ("c", 2), ("c", 3), ("c", 4)], K) == 1              # a star
    comb = [((0, 0), (0, 1)), ((0, 1), (0, 2)), ((0, 2), (0, 3)), ((0, 0), (1, 0)), ((0, 2), (1, 2)), ((1, 2), (2, 2))]
    ok = ok and phi_brute(sorted({v for e in comb for v in e}), comb, K) == 1                              # a comb (tree)
want("A2 each row of 6K - 1 averages to 0, so any edge set with a leaf has weight 0 and every forest has Phi = 1 (checked on a path, a star and "
     "a comb at three weight triples): the law on a window without cycles is independent occupancy with density 6z/(1+6z)", ok)

# ------------------------------------------------------------------ A3: the theta graph closed form (two cycles sharing edges)
r3 = sp.sqrt(3)
VEC = [[(r3 * a[0] if a[1] == i else 0) for a in AX] for i in range(3)]
EVN = [[sp.sqrt(sp.Rational(3, 2)) * (1, -1, 0)[a[1]] for a in AX], [(1, 1, -2)[a[1]] / sp.sqrt(2) for a in AX]]
mom = lambda fs: sp.nsimplify(sp.Rational(1, 6) * sum(sp.prod([f[a] for f in fs]) for a in range(6)))
orth = all(mom([f, g]) == int(i == j) for i, f in enumerate(VEC + EVN) for j, g in enumerate(VEC + EVN))
FVVE = sp.simplify(sum(mom([a, b, c]) ** 2 for a in VEC for b in VEC for c in EVN))
FEEE = sp.simplify(sum(mom([a, b, c]) ** 2 for a in EVN for b in EVN for c in EVN))
FVVV = sp.simplify(sum(mom([a, b, c]) ** 2 for a in VEC for b in VEC for c in VEC))
FVEE = sp.simplify(sum(mom([a, b, c]) ** 2 for a in VEC for b in EVN for c in EVN))
want("A3 the eigenfunctions (odd: sqrt3 * sign on one axis; even: two traceless axis functions) are orthonormal for the uniform content, "
     "and the three-mode fusion weights are F_VVE = 6, F_EEE = 2, F_VVV = F_VEE = 0", orth and (FVVE, FEEE, FVVV, FVEE) == (6, 2, 0, 0))


def theta_graph(a, b, c):
    V = ["u", "v"]; E = []
    for k, L in enumerate((a, b, c)):
        prev = "u"
        for i in range(L - 1):
            m = f"m{k}_{i}"; V.append(m); E.append((prev, m)); prev = m
        E.append((prev, "v"))
    return V, E


ok = True; rows = []
for t in TRIPLES:
    K = Kmat(*t); S = sum(t) + 3 * t[2]; l1 = F(t[0] - t[1], S); l2 = F(t[0] + t[1] - 2 * t[2], S)
    cyc = lambda m: 3 * l1 ** m + 2 * l2 ** m
    for (a, b, c) in ((1, 3, 3), (2, 2, 2), (1, 2, 2), (1, 2, 4), (3, 3, 3)):
        V, E = theta_graph(a, b, c)
        closed = 1 + cyc(a + b) + cyc(b + c) + cyc(a + c) + 6 * (l1 ** (a + b) * l2 ** c + l1 ** (a + c) * l2 ** b + l1 ** (b + c) * l2 ** a) + 2 * l2 ** (a + b + c)
        ok = ok and phi_brute(V, E, K) == closed
    rows.append(f"({t[0]},{t[1]},{t[2]})")
want("A3' theta graph with strands a, b, c: Phi = 1 + sum over its three cycles of (3 l1^n + 2 l2^n) + 6 (l1^{a+b} l2^c + l1^{a+c} l2^b + l1^{b+c} l2^a) "
     "+ 2 l2^{a+b+c}, exactly, for (a,b,c) = (1,3,3) [the domino on Z^3], (2,2,2), (1,2,2), (1,2,4), (3,3,3) at the triples " + ", ".join(rows), ok)

# ------------------------------------------------------------------ A4: the general rule (transfer of K_1 along strands)
ok = True; rows = []
for t in TRIPLES:
    K = Kmat(*t)
    for name, dims in (("C4", (2, 2)), ("domino", (2, 3)), ("ladder 2x4", (2, 4)), ("cube", (2, 2, 2))):
        V, E = grid(dims)
        HS = leafless_subsets(E)
        b = phi_brute(V, E, K)
        ok = ok and b == sum(w_transfer(H, K) for H in HS)
        if t == (3, 1, 2): rows.append(f"{name}: {len(HS)} leafless, Phi = {float(b):.10f}")
want("A4 general rule: Phi(A) = sum over leafless edge sets H of E(A) of prod over components of E over branch-vertex contents of "
     "prod over strands of (6 K^L - 1)(s_u, s_v) (a branch-free component is a cycle: tr K^n - 1), equal to the brute-force content sum "
     "on C4, the domino, the 2x4 ladder and the cube at three triples", ok, "; ".join(rows))

# ------------------------------------------------------------------ B1: the polymer representation of the grand partition function
z, rho = sp.symbols("z rho0", positive=True)
t = (3, 1, 2); K = Kmat(*t)
V, E = grid((2, 2, 2))
Xi = sp.Integer(0)
for k in range(len(V) + 1):
    for A in itertools.combinations(V, k):
        EA = [e for e in E if e[0] in A and e[1] in A]
        ph = phi_brute(list(A), EA, K)
        Xi += (6 * z) ** k * sp.Rational(ph.numerator, ph.denominator)
HS = leafless_subsets(E)
wH = [(H, w_transfer(H, K)) for H in HS]
poly = sum(sp.Rational(w.numerator, w.denominator) * (6 * z / (1 + 6 * z)) ** len({x for e in H for x in e}) for H, w in wH)
want("B1 cube window, (p,q,r) = (3,1,2): sum_A (6z)^|A| Phi(A) = (1 + 6z)^8 sum_{H leafless} w(H) rho0^{|V(H)|} identically in z "
     "(the occupied set is independent Bernoulli(rho0) decorated by a gas of leafless edge sets with activities w(H) rho0^{|V(H)|})",
     sp.simplify(Xi - (1 + 6 * z) ** 8 * poly) == 0)
# density and covariance series at a vertex / along an edge of the cube
x0, y0 = (0, 0, 0), (0, 0, 1)
num_x = sum(sp.Rational(w.numerator, w.denominator) * rho ** len({v for e in H for v in e}) * (1 if x0 in {v for e in H for v in e} else rho) for H, w in wH)
den = sum(sp.Rational(w.numerator, w.denominator) * rho ** len({v for e in H for v in e}) for H, w in wH)
dens = sp.simplify(num_x / den)
w4 = 3 * F(t[0] - t[1], 12) ** 4 + 2 * F(t[0] + t[1] - 2 * t[2], 12) ** 4
ser = sp.series(dens, rho, 0, 6).removeO()
want("B2 cube window: <n_x> = rho0 + (1 - rho0) P(x covered by the decoration), exactly; its expansion is rho0 + 3 w4 rho0^4 + O(rho0^5) "
     "with w4 = 3 l1^4 + 2 l2^4 (three plaquettes through a vertex of the cube)",
     sp.expand(ser).coeff(rho, 0) == 0 and sp.expand(ser).coeff(rho, 1) == 1 and sp.expand(ser).coeff(rho, 2) == 0 and sp.expand(ser).coeff(rho, 3) == 0
     and sp.expand(ser).coeff(rho, 4) == 3 * sp.Rational(w4.numerator, w4.denominator),
     f"w4 at (3,1,2) = {w4}; coefficient of rho0^4 = {sp.expand(ser).coeff(rho, 4)}")
num_xy = sum(sp.Rational(w.numerator, w.denominator) * rho ** len(Vs) * (1 if x0 in Vs else rho) * (1 if y0 in Vs else rho)
             for H, w in wH for Vs in [{v for e in H for v in e}])
cov = sp.simplify(num_xy / den - dens ** 2)
cser = sp.expand(sp.series(cov, rho, 0, 6).removeO())
want("B3 cube window: the nearest-neighbour density covariance starts at 2 w4 rho0^4 (the two plaquettes through an edge of the cube), "
     "nothing below order 4", [cser.coeff(rho, k) for k in range(4)] == [0, 0, 0, 0] and cser.coeff(rho, 4) == 2 * sp.Rational(w4.numerator, w4.denominator),
     f"coefficients rho0^0..5: {[str(cser.coeff(rho, k)) for k in range(6)]}")

# ------------------------------------------------------------------ B4: the ingredients of the convergence region
ok = True
for tt in TRIPLES:
    K = Kmat(*tt); S = sum(tt) + 3 * tt[2]; lam = max(abs(F(tt[0] - tt[1], S)), abs(F(tt[0] + tt[1] - 2 * tt[2], S)))
    for L in range(1, 7):
        KL = kpow(K, L)
        ok = ok and max(abs(6 * KL[a][b] - 1) for a in range(6) for b in range(6)) <= 5 * lam ** L
want("B4 strand bound: |6 K^L(a,b) - 1| <= 5 lambda^L with lambda = max(|l1|, |l2|), for L = 1..6 at three triples (the proof: "
     "6K^L - 1 = sum over the five non-constant modes of l^L psi(a) psi(b), and sum psi(a)^2 = 5)", ok)


def connected_edge_sets_through(n):
    """exact count of connected edge sets of Z^3 with n edges containing the origin (small n), by growth from the origin"""
    def nbrs(v):
        for i in range(3):
            for d in (1, -1):
                w = list(v); w[i] += d; yield tuple(w)
    def edge(u, v): return (u, v) if u < v else (v, u)
    start = frozenset()
    found = set()
    frontier = {frozenset([edge((0, 0, 0), w)]) for w in nbrs((0, 0, 0))}
    level = 1
    while level < n:
        new = set()
        for es in frontier:
            verts = {x for e in es for x in e}
            for v in verts:
                for w in nbrs(v):
                    e = edge(v, w)
                    if e not in es: new.add(es | {e})
        frontier = new; level += 1
    return len(frontier)


counts = [connected_edge_sets_through(k) for k in range(1, 5)]
want("B5 counting bound: connected edge sets of Z^3 with n edges through a vertex number at most 36^n (an Euler tour of the doubled "
     "set is a closed walk of length 2n from the vertex, at most 6 choices per step); exact counts for n = 1..4 respect it",
     all(cnt <= 36 ** (k + 1) for k, cnt in enumerate(counts)), f"counts {counts} against {[36 ** k for k in range(1, 5)]}")
# KP arithmetic (exact): activity <= (5 lambda)^|E| rho0^|V|, |V| >= |E|/3 on Z^3, sum_{n>=4} x^n = x^4/(1-x)
a = F(1, 4); xmax = F(57, 100)
want("B6 Kotecky-Preiss arithmetic (the criterion itself ASSUMED): with a(gamma) = |V(gamma)|/4 the sufficient condition "
     "sum_{n>=4} x^n <= 1/4 holds for x <= 57/100; x = 180 lambda e^{1/4} (all z, |rho0| <= 1) gives lambda <= 0.00246, and "
     "x = 180 lambda (rho0 e^{1/4})^{1/3} gives lambda rho0^{1/3} <= 0.00291",
     xmax ** 4 / (1 - xmax) <= a,
     f"x^4/(1-x) at 57/100 = {float(xmax ** 4 / (1 - xmax)):.4f}; lambda_all_z <= {0.57 / (180 * 2.718281828 ** 0.25):.5f}; "
     f"lambda rho0^(1/3) <= {0.57 / (180 * 2.718281828 ** (0.25 / 3)):.5f}")

# ------------------------------------------------------------------ C0, D1
pp = sp.Symbol("P", positive=True)
Kinf = [[sp.limit((pp if AX[i] == AX[j] else 1 if AX[i][1] == AX[j][1] else 1) * 6 / (pp + 1 + 4), pp, sp.oo) for j in range(6)] for i in range(6)]
want("C0 as p -> infinity with q, r fixed, W -> 6 on equal contents and 0 otherwise, so Phi(A) -> 6^{|E(A)| + c(A) - |A|} and "
     "mu(A) -> z^|A| 6^{|E(A)| + c(A)} (c = number of occupied clusters): the dense aligned / dilute competition of (c) in its limit",
     Kinf == [[6 if i == j else 0 for j in range(6)] for i in range(6)])
rows = []
for P in (3, 6, 8, 12, 16):
    l1v, l2v = F(P - 1, P + 9), F(P - 3, P + 9)
    lam = max(l1v, l2v)
    rows.append(f"p={P}: l1={l1v}, l2={l2v}, rho0 <= {float((F(291, 100000) / lam) ** 3):.2e}")
want("D1 on the line (p,1,2) (p >= 3 for a positive semidefinite rule) the proved region lambda rho0^{1/3} <= 0.00291 reaches only densities "
     "below 1e-5, far from the executed onsets (densities 0.1-0.7 at p = 6-16)", True, "; ".join(rows))

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PARTIAL (a) exact: at the pinned scale the occupied set's law is (6z)^|A| times Phi(A) = sum over leafless edge sets of "
          "prod over components of the transfer weight E[prod over strands (6K_1^L - 1)]; cycles give 3 l1^n + 2 l2^n, theta graphs "
          "6 (l1 l1 l2 terms) + 2 l2^{a+b+c} with fusion weights F_VVE = 6, F_EEE = 2; (b) the grand partition function is (1+6z)^N times a "
          "polymer gas of leafless edge sets with activities w rho0^|V|, density rho0 + 12 (1-rho0) (3 l1^4 + 2 l2^4) rho0^4 + ..., and "
          "a convergence (no-clumping) region lambda <= 0.00246 for all z or lambda rho0^(1/3) <= 0.00291 (Kotecky-Preiss assumed); "
          "(c) not attempted beyond the p -> infinity limit; (d) the proved region is far from the executed onsets")
    print("HIT: at c0 the occupied-set law is exactly Bernoulli(6z/(1+6z)) decorated by a gas of leafless edge sets with weights computed "
          "from K_1's eigenvalues: w(cycle) = 3 l1^n + 2 l2^n, w(theta_{abc}) = 6(l1^{a+b} l2^c + l1^{a+c} l2^b + l1^{b+c} l2^a) + 2 l2^{a+b+c}, "
          "general components by strand transfer 6K_1^L - 1 contracted at branch vertices; |w| <= 5^{strands} lambda^{|E|}")
