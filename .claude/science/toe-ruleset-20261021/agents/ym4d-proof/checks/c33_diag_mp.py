"""c33 POST-RUN diagnostic (not a criterion): Part A, constant field D = 0.2, at 40 digits (mpmath).
Written after c33A FAILED as pre-registered on A1/A4/A5 at the constant seed (double-precision cancellation in the
brute-force log coefficients). Output recorded in c33_time.txt."""
import sys, itertools, math
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks')
import mpmath as mp
mp.mp.dps = 40
import c33_bfour as c
c.math.exp = mp.exp  # high-precision activities
tor = c.Torus(2, 9)
sites = list(itertools.product(range(9), repeat=2))
sets = c.connected_sets_upto(tor, sites, 3)
tuples = c.build_tuples(tor, sets, 3)
D = {s: mp.mpf('0.2') for s in sites}
terms = c.tuple_terms(tor, tuples, D)
tot = [mp.mpf(0)]*4
for (tup, ph, N, S, X), t in zip(tuples, terms):
    tot[N] += t
a = [mp.mpf(1)] + [mp.mpf(0)]*3
for m in (1,2,3):
    s = mp.mpf(0)
    for B in itertools.combinations(sites, m):
        s += math.prod(c.activity(tor, Y, D) for Y in c.components(tor, B))
    a[m] = s
cc = [0, a[1], a[2]-a[1]**2/2, a[3]-a[1]*a[2]+a[1]**3/3]
for N in (1,2,3):
    print(N, mp.nstr(tot[N], 20), mp.nstr(cc[N], 20), mp.nstr((tot[N]-cc[N])/cc[N], 5))
