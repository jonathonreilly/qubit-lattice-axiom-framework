"""T02 script A: how much freedom do the axioms' symmetries leave a local qubit generator?

Object: translation-invariant Hermitian generators H = sum_x T_x( sum_S sum_labels a[S,b] * sigma^{b1}_{s1} ... sigma^{bn}_{sn} )
whose terms are supported inside a translate of the 'star' (a site and its six nearest
neighbours).  A term is a Pauli string on a set S of star sites (distinct sites, label in {x,y,z}
on every site of S, identity elsewhere).  Because H is translation invariant, only the
translation class of S matters; the coefficient tensor a[class, labels] is the unknown.
Different (class, labels) are different operators (distinct Pauli strings), so the real
dimension of a covariant coefficient space equals the number of independent covariant
generators (mod the identity).

Two covariance flavours:
  unsoldered: SU(2) acting on the Pauli labels of every site simultaneously ("no possibility is
              privileged"), times the 24 proper cubic rotations acting on positions only.
  soldered  : the 24 proper cubic rotations acting on positions AND on the Pauli labels
              (rotation matrix R_g), no continuous internal symmetry.
Counts by two independent methods: characters (all n <= 7) and explicit nullspace (n <= 4).
Also: the 'NN-local' subspace = classes whose shape is a clique of Z^3 (single site or bond).
"""
import itertools, sys, json
import numpy as np

# ------------------------------------------------------------------ lattice data
E = [(1,0,0),(0,1,0),(0,0,1)]
STAR = [(0,0,0)] + [tuple(s*np.array(e)) for e in E for s in (1,-1)]
STAR = [tuple(int(v) for v in p) for p in STAR]

def rot_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1,-1), repeat=3):
            M = np.zeros((3,3), dtype=int)
            for i,(p,s) in enumerate(zip(perm,signs)):
                M[i,p] = s
            if round(np.linalg.det(M)) == 1:
                mats.append(M)
    return mats
G = rot_group()
assert len(G) == 24

def canon(points):
    pts = sorted(tuple(int(v) for v in p) for p in points)
    m = pts[0]
    return tuple(sorted(tuple(int(a-b) for a,b in zip(p,m)) for p in pts))

# translation classes of subsets of the star
classes = {}
for mask in range(1, 1 << 7):
    S = [STAR[i] for i in range(7) if mask >> i & 1]
    classes.setdefault(canon(S), []).append(mask)
K_list = sorted(classes.keys(), key=lambda K: (len(K), K))
print("translation classes of star subsets:", len(K_list),
      "by size", {n: sum(1 for K in K_list if len(K)==n) for n in range(1,8)})

def is_clique(K):
    for a,b in itertools.combinations(K, 2):
        d = sum(abs(x-y) for x,y in zip(a,b))
        if d != 1: return False
    return True

def act(g, K):
    """image class and slot permutation: slot i of K -> slot pi[i] of K'."""
    pts = [tuple(int(v) for v in g @ np.array(p)) for p in K]
    m = min(pts)
    pts = [tuple(a-b for a,b in zip(p,m)) for p in pts]
    Kp = tuple(sorted(pts))
    pi = [Kp.index(p) for p in pts]
    return Kp, pi

def cycles(pi):
    seen, out = set(), []
    for i in range(len(pi)):
        if i in seen: continue
        c, j = 0, i
        while j not in seen:
            seen.add(j); j = pi[j]; c += 1
        out.append(c)
    return out

# ------------------------------------------------------------------ characters
NTH = 4096
TH = 2*np.pi*np.arange(NTH)/NTH
HAAR_W = (1 - np.cos(TH)) / NTH          # (1/2pi) * (1-cos) dtheta on the uniform grid

def chi_unsoldered(cyc):
    f = np.ones_like(TH)
    for c in cyc:
        f = f * (1 + 2*np.cos(c*TH))
    return float(np.sum(f * HAAR_W))

def chi_soldered(g, cyc):
    val = 1
    for c in cyc:
        val *= int(np.trace(np.linalg.matrix_power(g, c)))
    return val

def char_dim(classes_used, flavour):
    tot = {}
    for g in G:
        for K in classes_used:
            Kp, pi = act(g, K)
            if Kp != K: continue
            cyc = cycles(pi)
            chi = chi_unsoldered(cyc) if flavour == "unsoldered" else chi_soldered(g, cyc)
            tot[len(K)] = tot.get(len(K), 0.0) + chi / len(G)
    return tot

# ------------------------------------------------------------------ direct nullspace (n <= 4)
def so3_gens():
    L = []
    for k in range(3):
        M = np.zeros((3,3))
        for a in range(3):
            for b in range(3):
                M[a,b] = -np.linalg.det(np.array([np.eye(3)[k], np.eye(3)[a], np.eye(3)[b]]))
        L.append(M)
    return L
LGEN = so3_gens()

def inv_basis(n):
    """orthonormal basis (columns) of SO(3)-invariant tensors in (R^3)^{(x)n}"""
    dim = 3**n
    rows = []
    for L in LGEN:
        Mtot = np.zeros((dim, dim))
        for i in range(n):
            ops = [np.eye(3)]*n
            ops[i] = L
            T = ops[0]
            for o in ops[1:]:
                T = np.kron(T, o)
            Mtot += T
        rows.append(Mtot)
    A = np.vstack(rows)
    u, s, vt = np.linalg.svd(A)
    rank = int(np.sum(s > 1e-9))
    return vt[rank:].T

def perm_matrix(n, pi):
    """matrix on (R^3)^{(x)n} sending slot i -> slot pi[i]"""
    dim = 3**n
    M = np.zeros((dim, dim))
    for idx in itertools.product(range(3), repeat=n):
        new = [0]*n
        for i in range(n): new[pi[i]] = idx[i]
        a = int(np.ravel_multi_index(idx, (3,)*n))
        b = int(np.ravel_multi_index(new, (3,)*n))
        M[b, a] = 1.0
    return M

def kron_pow(R, n):
    T = R
    for _ in range(n-1): T = np.kron(T, R)
    return T if n > 1 else R

def direct_dim(nmax, flavour, only_cliques=False):
    used = [K for K in K_list if len(K) <= nmax and (is_clique(K) or not only_cliques)]
    off, tot = {}, 0
    B = {}
    for K in used:
        n = len(K)
        Bk = inv_basis(n) if flavour == "unsoldered" else np.eye(3**n)
        B[K] = Bk
        off[K] = tot
        tot += Bk.shape[1]
    Rey = np.zeros((tot, tot))
    for g in G:
        Rg = g.astype(float)
        for K in used:
            n = len(K)
            Kp, pi = act(g, K)
            P = perm_matrix(n, pi)
            if flavour == "soldered":
                P = P @ kron_pow(Rg, n)       # rotate labels, then move slots
            blk = B[Kp].T @ P @ B[K]
            Rey[off[Kp]:off[Kp]+blk.shape[0], off[K]:off[K]+blk.shape[1]] += blk / len(G)
    return float(np.trace(Rey)), Rey

if __name__ == "__main__":
    res = {}
    print("\n=== character counts (real dimension of covariant coefficient space) ===")
    for flavour in ("unsoldered", "soldered"):
        allK = K_list
        clq = [K for K in K_list if is_clique(K)]
        two = [K for K in K_list if len(K) <= 2]
        d_all = char_dim(allK, flavour)
        d_clq = char_dim(clq, flavour)
        d_two = char_dim(two, flavour)
        f = lambda d: {k: round(v, 6) for k, v in sorted(d.items())}
        print(flavour)
        print("  all star-range by n :", f(d_all), " total", round(sum(d_all.values()), 6))
        print("  clique (bond) range :", f(d_clq), " total", round(sum(d_clq.values()), 6))
        print("  star range n<=2     :", f(d_two), " total", round(sum(d_two.values()), 6))
        Teven = sum(v for k, v in d_all.items() if k % 2 == 0)
        Todd = sum(v for k, v in d_all.items() if k % 2 == 1)
        print("  star-range T-even (n even) / T-odd (n odd):", round(Teven, 6), round(Todd, 6))
        res[flavour] = dict(all_by_n=f(d_all), all_total=round(sum(d_all.values()), 6),
                            clique_by_n=f(d_clq), clique_total=round(sum(d_clq.values()), 6),
                            n_le2_total=round(sum(d_two.values()), 6),
                            T_even=round(Teven, 6), T_odd=round(Todd, 6))

    print("\n=== direct nullspace cross-check (n <= 4) ===")
    for flavour in ("unsoldered", "soldered"):
        d4, Rey = direct_dim(4, flavour)
        d4c, _ = direct_dim(4, flavour, only_cliques=True)
        chk = char_dim([K for K in K_list if len(K) <= 4], flavour)
        chk_c = char_dim([K for K in K_list if len(K) <= 4 and is_clique(K)], flavour)
        proj_err = float(np.abs(Rey @ Rey - Rey).max())
        print(f"{flavour}: direct n<=4 total {d4:.6f}  character {sum(chk.values()):.6f} | "
              f"clique direct {d4c:.6f} character {sum(chk_c.values()):.6f} | projector err {proj_err:.2e}")
        res[flavour]["direct_n_le4"] = round(d4, 6)
        res[flavour]["char_n_le4"] = round(sum(chk.values()), 6)
        res[flavour]["direct_clique_n_le4"] = round(d4c, 6)

    # cross-check with landed note (9040): bond range unsoldered 1, soldered 3
    print("\n=== cross-check with landed DYNAMICS_CLAUSE covariant NN two-qubit generators note ===")
    print("unsoldered (possibility covariance) bond range expected 1 ->", res["unsoldered"]["clique_total"])
    print("soldered (full soldering) bond range expected 3 ->", res["soldered"]["clique_total"])
    json.dump(res, open(sys.argv[0].replace(".py", "_result.json"), "w"), indent=1)
