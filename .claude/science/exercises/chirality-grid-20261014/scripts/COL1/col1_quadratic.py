"""COL-1 check 1: class Q (one complex fermion mode per site, quadratic Gauss generators).

G = c^dag t c is a Lie-algebra homomorphism t -> G; [c^dag t c, c^dag s c] = c^dag [t,s] c.
So everything reduces to single-particle matrices t on C^N (N = number of sites).
"""
import numpy as np
from su3common import T, check_su3_relations

mx = lambda m: float(np.abs(m).max())

def embed(N, sites):
    """single-particle t^a for colour i on site sites[i]"""
    out = np.zeros((8, N, N), dtype=complex)
    for a in range(8):
        for i in range(3):
            for j in range(3):
                out[a, sites[i], sites[j]] += T[a][i, j]
    return out

def max_comm(tA, tB):
    return max(mx(tA[a] @ tB[b] - tB[b] @ tA[a]) for a in range(8) for b in range(8))

N = 12
print("=== class Q, ring N = %d single-particle space" % N)

# (A) overlapping consecutive windows: colour i of point x on site x+i (untwisted)
tA = [embed(N, [(x + i) % N for i in range(3)]) for x in range(N)]
print("(A) windows {x,x+1,x+2}: su(3) relations err %.1e" % check_su3_relations(tA[0], mx))
for d in (1, 2, 3):
    print("    max |[t_0^a, t_%d^b]| = %.4f" % (d, max_comm(tA[0], tA[d])))

# (B) twisted (staggered-style) assignment s(x,i) = x + ((i - x) mod 3)
def sB(x, i):
    return (x + ((i - x) % 3)) % N
tB = [embed(N, [sB(x, i) for i in range(3)]) for x in range(N)]
# twisted translation: shift by one site maps component i of point x to component i+1 of x+1
P = np.zeros((3, 3)); P[(np.arange(3) + 1) % 3, np.arange(3)] = 1   # cyclic colour permutation
S = np.zeros((N, N)); S[(np.arange(N) + 1) % N, np.arange(N)] = 1   # one-step shift
cov = max(mx(S @ tB[x][a] @ S.T - sum(np.real(np.trace(P @ T[a] @ P.T @ T[b]) * 2) * tB[(x + 1) % N][b] for b in range(8)))
          for x in range(N) for a in range(8))
print("(B) twisted s(x,i)=x+((i-x) mod 3): covariance err under shift (x) cyclic colour perm = %.1e" % cov)
occ = np.zeros(N, int)
for x in range(N):
    for i in range(3):
        occ[sB(x, i)] += 1
print("    colour components per site (needs 1 for one mode/site):", sorted(set(occ.tolist())))
for d in (1, 2, 3):
    print("    max |[t_0^a, t_%d^b]| = %.4f" % (d, max_comm(tB[0], tB[d])))

# (C) block assignment: gauge points only at x = 0 mod 3 -> commuting but density 1/3
tC = {x: embed(N, [x + i for i in range(3)]) for x in range(0, N, 3)}
worst = max(max_comm(tC[x], tC[y]) for x in tC for y in tC if x != y)
print("(C) blocks at x = 0 mod 3: max cross commutator %.1e; gauge points %d = N/3" % (worst, len(tC)))
Sb = S @ tC[0][0] @ S.T
print("    shifted block generator equals some block generator? ",
      any(mx(Sb - tC[y][0]) < 1e-12 for y in tC))

# (D) counting bound, general: dim >= sum over irreducible components of prod dims >= 3 * (#points)
#     enumerate: maximum #mutually commuting nontrivial su(3) reps on C^N is floor(N/3) (blocks attain it)
print("(D) counting: |I| <= N/3 (complex); Majorana/BdG form: real dim 2N >= 6|I| (3 is 6-dim over R) -> same bound")
print("    translation orbits are free on a ring of N > range sites, so |I| = k N with k >= 1 -> 3kN <= N impossible")

# (E) classification of covariant assignments s(x+1, sigma(i)) = s(x,i)+1 for sigma in S_3
import itertools
print("(E) covariant assignments s(x,i) = x + c(sigma^{-x}(i)), c in {0..4}^3, sigma in S_3:")
best = None
for perm in itertools.permutations(range(3)):
    for c in itertools.product(range(5), repeat=3):
        def s(x, i, perm=perm, c=c):
            j = i
            inv = [perm.index(k) for k in range(3)]
            for _ in range(x % 6):
                j = inv[j]
            return x + c[j]
        # check covariance and count components per site on a long stretch
        ok = all(s(x + 1, perm[i]) == s(x, i) + 1 for x in range(12) for i in range(3))
        if not ok:
            continue
        cnt = {}
        for x in range(-10, 30):
            for i in range(3):
                cnt[s(x, i)] = cnt.get(s(x, i), 0) + 1
        per_site = set(cnt[k] for k in range(5, 20))
        best = per_site if best is None else best | per_site
print("    components per site over all covariant assignments:", sorted(best), "(always 3)")
