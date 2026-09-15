"""Supervisor control B, block 08: (5) exact stationary plane law pi_2 of the 2x2 cross-section by orbit reduction;
(6) exact influence checks against the path-counting bound; (7) down-set consistency on the cube.  Exact arithmetic."""
from fractions import Fraction as F
from itertools import product, permutations
import sys, time
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from supervisor_control_block08_z3 import AXES, M, kernels, cond, tv, mu2d_square, plane_transfer_2x2, sensitivities
import sympy as sp

# internal symmetry group: the 48 signed axis permutations acting on the six axes (+x,-x,+y,-y,+z,-z) = indices 0..5
def group48():
    axes = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    idx = {a: i for i, a in enumerate(axes)}
    elems = set()
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            mp = []
            for a in axes:
                b = [0, 0, 0]
                for i in range(3):
                    b[perm[i]] = signs[i] * a[i]
                mp.append(idx[tuple(b)])
            elems.add(tuple(mp))
    return sorted(elems)

def stationary_2x2(tr):
    phi, Z1, K, K2, K3 = kernels(tr)
    states = list(product(range(M), repeat=4))
    G = group48()
    def act(g, s, transpose):
        v = tuple(g[x] for x in s)
        if transpose:  # plane transpose x2 <-> x3: sites 00,01,10,11 -> 00,10,01,11
            v = (v[0], v[2], v[1], v[3])
        return v
    orbit_of, reps = {}, []
    for s in states:
        if s in orbit_of:
            continue
        o = len(reps); reps.append(s)
        stack = [s]; orbit_of[s] = o
        while stack:
            u = stack.pop()
            for g in G:
                for tr_ in (False, True):
                    v = act(g, u, tr_)
                    if v not in orbit_of:
                        orbit_of[v] = o; stack.append(v)
    n = len(reps)
    sizes = [0] * n
    for s in states: sizes[orbit_of[s]] += 1
    # quotient Q[o][o'] = sum_{v in o'} P(rep_o -> v); check representative independence on a second member
    Q = [[F(0)] * n for _ in range(n)]
    for o, w in enumerate(reps):
        for v in states:
            Q[o][orbit_of[v]] += plane_transfer_2x2(K, K2, K3, w, v)
    # commutation check: another member of each orbit gives the same row (first 3 orbits, all members)
    ok = True
    for o in range(min(n, 4)):
        members = [s for s in states if orbit_of[s] == o]
        for w in members[1:3]:
            row = [F(0)] * n
            for v in states:
                row[orbit_of[v]] += plane_transfer_2x2(K, K2, K3, w, v)
            ok = ok and row == Q[o]
    # stationary law on orbits: pi Q = pi (row vector), sum pi = 1 ; exact solve
    Qm = sp.Matrix(n, n, lambda i, j: sp.Rational(Q[i][j].numerator, Q[i][j].denominator))
    A = (Qm.T - sp.eye(n))
    A = A.row_insert(n, sp.ones(1, n))
    b = sp.zeros(n + 1, 1); b[n, 0] = 1
    sol = A.solve_least_squares(b) if False else None
    # exact: solve the square system with the last equation replaced
    A2 = (Qm.T - sp.eye(n))
    A2[n - 1, :] = sp.ones(1, n)
    b2 = sp.zeros(n, 1); b2[n - 1, 0] = 1
    pi_orb = A2.LUsolve(b2)
    pi_orb = [F(int(sp.numer(x)), int(sp.denom(x))) for x in pi_orb]
    assert all(x > 0 for x in pi_orb) and sum(pi_orb) == 1
    # lift to states
    pi = {s: pi_orb[orbit_of[s]] / sizes[orbit_of[s]] for s in states}
    mu = mu2d_square(K, K2)
    tvd = sum(abs(pi[s] - mu[s]) for s in states) / 2
    def pair_law(law, i, j):
        out = {}
        for v in states:
            out[(v[i], v[j])] = out.get((v[i], v[j]), F(0)) + law[v]
        return out
    def is_K_pair(pl):
        return all(pl[(a, b)] == F(1, 6) * K[a][b] for a in range(M) for b in range(M))
    one_uniform = all(sum(law for v, law in pi.items() if v[i] == s) == F(1, 6) for i in range(4) for s in range(M))
    p01_11 = pair_law(pi, 1, 3)
    # exact sector contraction: the exact TV between two rows of Q^n (orbit sector) for n = 1..6, against the theorem's rate theta = c/(1-2c)
    c = max(sensitivities(tr)[k][0] for k in (1, 2, 3)); theta = c / (1 - 2 * c)
    Qn = [row[:] for row in Q]
    mods = []
    for step in range(1, 7):
        # TV between the plane-state rows: use rows of two representatives lifted: TV(P^n(w,.), P^n(w',.)) = sum_o |Qn[o1][o] - Qn[o2][o]| / 2 for orbit-constant... (rows of Q^n are orbit-summed laws)
        d = max(sum(abs(Qn[o1][o] - Qn[o2][o]) for o in range(n)) / 2 for o1 in range(n) for o2 in range(n))
        mods.append((step, d, theta ** step, d <= theta ** step))
        Qn = [[sum(Qn[i][k] * Q[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return dict(n_orbits=n, commutes=ok, tv_pi_mu=tvd, one_uniform=one_uniform,
                row_x3_0_K=is_K_pair(pair_law(pi, 0, 2)), row_x3_1_K=is_K_pair(pair_law(pi, 1, 3)),
                col_x2_0_K=is_K_pair(pair_law(pi, 0, 1)), col_x2_1_K=is_K_pair(pair_law(pi, 2, 3)),
                antidiag_K2=all(pair_law(pi, 1, 2)[(a, b)] == F(1, 6) * K2[a][b] for a in range(M) for b in range(M)),
                interior_pair_pp=p01_11[(0, 0)], K_pair_pp=F(1, 6) * K[0][0],
                sector_tv=mods)

def cube_law(tr):
    phi, Z1, K, K2, K3 = kernels(tr)
    sites = list(product(range(2), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    preds = {x: [tuple(x[i] - (1 if j == i else 0) for i in range(3)) for j in range(3) if x[j] > 0] for x in sites}
    law = {}
    for v in product(range(M), repeat=8):
        w = F(1)
        for x in sites:
            rec = tuple(v[idx[y]] for y in preds[x])
            w *= cond(K, K2, K3, rec)[v[idx[x]]]
        law[v] = w
    return sites, idx, preds, law, K, K2, K3

def main():
    print("=== (5) exact stationary plane law pi_2 (2x2 cross-section) by orbit reduction")
    for tr in [(3, 1, 2), (5, 2, 4)]:
        t0 = time.time()
        r = stationary_2x2(tr)
        print(f"{tr}: orbits={r['n_orbits']} commutes={r['commutes']} TV(pi_2, mu_2D)={r['tv_pi_mu']} ({float(r['tv_pi_mu']):.6g}); one-site uniform={r['one_uniform']}; "
              f"row x3=0 K-pair={r['row_x3_0_K']} row x3=1 K-pair={r['row_x3_1_K']} col x2=0 K-pair={r['col_x2_0_K']} col x2=1 K-pair={r['col_x2_1_K']} antidiag K^2={r['antidiag_K2']}; "
              f"interior pair P(+x,+x)={r['interior_pair_pp']} vs (1/6)K={r['K_pair_pp']}; sector row-TV after n steps vs theta^n: {[(s, float(d), float(th), ok_) for s, d, th, ok_ in r['sector_tv']]}; {time.time()-t0:.1f}s")
    print()
    print("=== (6)+(7) cube: down-set consistency, one-site uniformity, and the exact influence of v_000 on v_111 against 6 c^3")
    for tr in [(3, 1, 2)]:
        t0 = time.time()
        sites, idx, preds, law, K, K2, K3 = cube_law(tr)
        assert sum(law.values()) == 1
        # down-set {x3 = 0}: marginal equals the 2D 2x2 law with sites (x1,x2)
        mu2 = mu2d_square(K, K2)
        marg = {}
        ds = [(0,0,0),(0,1,0),(1,0,0),(1,1,0)]  # as (row=x1, col=x2): 00,01,10,11
        for v, w in law.items():
            key = tuple(v[idx[s]] for s in ds)
            marg[key] = marg.get(key, F(0)) + w
        print(f"{tr}: down-set x3=0 marginal == mu_2D(2x2): {marg == mu2}")
        one = all(sum(w for v, w in law.items() if v[idx[x]] == s) == F(1, 6) for x in sites for s in range(M))
        print(f"{tr}: one-site marginals uniform on the cube: {one}")
        # influence: conditional law of v_111 given v_000 = s, over the box law (all else formed by the rule)
        c = max(sensitivities(tr)[k][0] for k in (1, 2, 3))
        best = F(0)
        for s in range(M):
            for s2 in range(M):
                if s2 <= s: continue
                ls = [F(0)] * M; ls2 = [F(0)] * M
                for v, w in law.items():
                    if v[idx[(0,0,0)]] == s: ls[v[idx[(1,1,1)]]] += w
                    if v[idx[(0,0,0)]] == s2: ls2[v[idx[(1,1,1)]]] += w
                ls = [x * 6 for x in ls]; ls2 = [x * 6 for x in ls2]
                best = max(best, tv(ls, ls2))
        print(f"{tr}: max TV of law(v_111 | v_000=s) over s,s' = {best} ({float(best):.6f}); bound 6 c^3 = {6*c**3} ({float(6*c**3):.6f}); bound holds: {best <= 6*c**3}; {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
