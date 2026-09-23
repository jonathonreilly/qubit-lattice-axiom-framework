"""Refuting pass, block 30 (independent machinery): (a) the two-level automaton eta' and the six-axis level automaton at (p, 1, 2)
coupled through shared uniforms on a periodic plane: the domination xi <= eta' checked pointwise at every level (p = 12, 30, 200);
(b) the dissent densities of both far below the proved region, against epsilon_1/(1 - 3 epsilon_2) (the seed-plus-branching estimate);
(c) an independent graph implementation (numpy predecessor and sibling tests) re-checking the extended trees on random cones: arrows to
predecessors, forks to siblings, one arrow to a predecessor per node, seeds/amplified classification, forks = |S| - 1, E <= 3(|S|-1)+2|A|;
(d) the certificates' fixed points re-derived by floating-point iteration; the domain edge at y = 0 by bisection against 4/27."""
import numpy as np, sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import supervisor_control_block30_core as core
rng = np.random.default_rng(30)
def devs(p, q, r):
    return (1 - p**3/(p**3+q**3+4*r**3), 1 - p**2*q/(p*q*(p+q)+4*r**3), 1 - p**2*r/(r*(p**2+q**2)+r**2*(p+q)+2*r**3))
print("(a)/(b) coupled runs at (p,1,2): the six-axis law (values 0..5, aligned start 0) and the two-level automaton eta' with the SAME uniforms; L=128, T=1500")
for p in (12, 30, 200):
    q, r = 1.0, 2.0; d1, d2, d3 = devs(p, q, r); e1, e2 = d1, max(d2, d3)
    phi = np.full((6, 6), r)
    for v in range(6): phi[v, v] = p; phi[v, v ^ 1] = q
    L, T = 128, 1500; s = np.zeros((L, L), dtype=np.int64); eta = np.zeros((L, L), dtype=np.int64); viol = 0; dens_xi = []; dens_eta = []; t0 = time.time()
    for t in range(1, T + 1):
        p1, p2, p3 = s, np.roll(s, 1, 0), np.roll(s, 1, 1)
        W = phi[:, p1] * phi[:, p2] * phi[:, p3]; W = W / W.sum(0, keepdims=True)
        # draw the six-axis record with the uniform U so that "not a" happens iff U < 1 - W[0] (put value a = 0 at the top of the cumulative)
        U = rng.random((L, L))
        order = [0, 1, 2, 3, 4, 5]
        C = np.cumsum(W, axis=0)          # C[0] = P(a); "not a" iff U >= C[0]... use U' = 1 - U for monotone coupling: xi = 1 iff U < 1 - W[0]
        new = np.minimum(((1 - U)[None] > C).sum(0), 5)
        xi_new = (new != 0).astype(np.int64)
        n1 = eta + np.roll(eta, 1, 0) + np.roll(eta, 1, 1)
        eta_new = np.where(n1 >= 2, 1, np.where(n1 == 1, (U < e2).astype(np.int64), (U < e1).astype(np.int64)))
        viol += int((xi_new > eta_new).sum())
        s, eta = new, eta_new
        if t > T // 2: dens_xi.append(xi_new.mean()); dens_eta.append(eta_new.mean())
    print(f"  p={p}: eps1={e1:.3e} eps2={e2:.3e}; domination violations {viol} of {L*L*T}; dissent density xi {np.mean(dens_xi):.3e}, eta' {np.mean(dens_eta):.3e}, eps1/(1-3 eps2) = {e1/(1-3*e2) if 3*e2 < 1 else float('inf'):.3e}   ({time.time()-t0:.0f}s)")
print("(c) independent graph checks of the extended trees on random cones")
E3 = np.array(core.E); FORK = np.array(core.FORK_OFFSETS)
def is_pred(a, b): return any((np.array(a) - np.array(b) == e).all() for e in E3)
def is_sib(a, b): return any((np.array(a) - np.array(b) == f).all() for f in FORK)
random.seed(77); ok = True; n = 0; withA = 0
x = (0, 0, 0)
for trial in range(600):
    d = random.choice((3, 4, 5, 6, 7)); dens = random.choice((15, 30, 50)); sites = core.cone(x, d)
    zeta = {z: 1 for z in sites if random.randrange(100) < dens}
    eta = core.run_automaton(sites, zeta)
    if eta[x] != 1: continue
    ex = core.Explainer(eta, zeta); nodes, edges, S, A, refs, bad = ex.explain(x); n += 1; withA += (len(A) > 0)
    # tree: connected with |edges| = |nodes| - 1 via union-find
    parent = {v: v for v in nodes}
    def find(a):
        while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
        return a
    cyc = False
    for e, kind in edges.items():
        a, b = tuple(e)
        if kind == "fork": ok = ok and is_sib(a, b)
        else: ok = ok and (is_pred(a, b) or is_pred(b, a))
        ra, rb = find(a), find(b)
        if ra == rb: cyc = True
        parent[ra] = rb
    ok = ok and (not cyc) and len(edges) == len(nodes) - 1 and len({find(v) for v in nodes}) == 1
    downs = {v: 0 for v in nodes}; E_ = Fk = 0
    for e, kind in edges.items():
        a, b = tuple(e)
        if kind == "fork": Fk += 1; continue
        upper = a if is_pred(a, b) else b; downs[upper] += 1; E_ += (kind == "arrow")
    def npred1(v): return sum(1 for e in E3 if eta.get(tuple(np.array(v) - e), 0) == 1)
    ok = ok and all(npred1(v) == 0 for v in S) and all(npred1(v) == 1 for v in A) and all(npred1(v) >= 2 for v in nodes if v not in S and v not in A)
    ok = ok and max(downs.values()) <= 1 and Fk == len(S) - 1 and E_ <= 3*(len(S)-1) + 2*len(A)
print(f"  {n} explained trees ({withA} with amplified nodes): independent checks pass: {ok}")
print("(d) certificates' fixed points by floating-point iteration, and the domain edge at y = 0")
def fixed(x, y):
    D = U = Fv = 1.0
    for i in range(50000):
        D2, U2, F2 = (1+x*U)**2*(1+3*x*D)*(1+y*Fv)**6, (1+x*U)**3*(1+y*Fv)**6, (1+x*U)**3*(1+3*x*D)*(1+y*Fv)**5
        if max(D2, U2, F2) > 1e9: return None
        if abs(D2-D)+abs(U2-U)+abs(F2-Fv) < 1e-13: return (D2, U2, F2)
        D, U, Fv = D2, U2, F2
    return (D, U, Fv)
for (p, q, r, t, cert) in ((4165,1,2,0.099,(113.388504498346, 3.279872914431, 168.429466648591)), (2085,1,1,0.098,(88.632394933177, 3.254100818939, 131.311435970231)), (6247,1,3,0.099,(97.781302293812, 3.264868815393, 145.029826833424))):
    d1, d2, d3 = devs(p, q, r); e1, e2 = d1, max(d2, d3); x, y = t + e2/t**2, e1/t**3; fp = fixed(x, y)
    diffs = tuple(c - f for c, f in zip(cert, fp)) if fp else None
    print(f"  (p,{q},{r})={p}: x={x:.5f} y={y:.3e}: fixed point {tuple(round(v,4) for v in fp) if fp else None}; certificate minus fixed point {tuple(f'{d:.1e}' for d in diffs) if diffs else None} (the exact inequalities are the runner's; a difference of order 1e-5 or below is the displacement or rounding)")
from fractions import Fraction as Fr
def devs_exact(p, q, r):
    p, q, r = Fr(p), Fr(q), Fr(r)
    return (1 - p**3/(p**3+q**3+4*r**3), 1 - p**2*q/(p*q*(p+q)+4*r**3), 1 - p**2*r/(r*(p**2+q**2)+r**2*(p+q)+2*r**3))
certs_exact = {(4165,1,2): (Fr(99,1000), Fr(56694252249173,500000000000), Fr(3279872914431,1000000000000), Fr(168429466648591,1000000000000)),
               (2085,1,1): (Fr(49,500), Fr(88632394933177,1000000000000), Fr(3254100818939,1000000000000), Fr(131311435970231,1000000000000)),
               (8330,2,4): (Fr(99,1000), Fr(56694252249173,500000000000), Fr(3279872914431,1000000000000), Fr(168429466648591,1000000000000)),
               (6247,1,3): (Fr(99,1000), Fr(24445325573453,250000000000), Fr(3264868815393,1000000000000), Fr(9064364177089,62500000000))}
for (p,q,r), (t, Db, Ub, Fb) in certs_exact.items():
    d1, d2, d3 = devs_exact(p,q,r); e1, e2 = d1, max(d2,d3); x, y = t + e2/t**2, e1/t**3
    rD = (1+x*Ub)**2*(1+3*x*Db)*(1+y*Fb)**6; rU = (1+x*Ub)**3*(1+y*Fb)**6; rF = (1+x*Ub)**3*(1+3*x*Db)*(1+y*Fb)**5
    print(f"  exact margins at ({p},{q},{r}): D {float(Db-rD):.2e}, U {float(Ub-rU):.2e}, F {float(Fb-rF):.2e} (all positive: the certificate dominates the least fixed point exactly; the float iteration near spectral radius 0.99 is not resolved to 1e-6)")
lo, hi = 0.1, 0.2
for _ in range(40):
    mid = (lo+hi)/2
    if fixed(mid, 0.0) is not None: lo = mid
    else: hi = mid
print(f"  domain edge at y = 0 by bisection: {lo:.6f} (4/27 = {4/27:.6f})")
