"""F1 part 1: ghost cohomology of the lattice linearized gauge map = Killing jets.

H(gamma) in the ghost sector is spanned by the jets of C modulo the gamma-exact symmetrized
differences S = D C.  Its dimension on a box equals dim ker D (Killing fields).  Claim
(F1, Lemma K): for ANY translation-invariant local D whose symbol has the continuum value and
first derivative at k=0 (IR normalization), ker D contains exactly the 10 affine Killing
fields (4 translations + 6 rotations) and nothing else for an elliptic stencil.
Checked on open boxes for three stencils + one non-normalized control:
  K7a   : nabla_m = forward unit difference (K2's placement)
  IMP   : nabla_m = (27*Delta_1 - Delta_3)/24  (range-2 improved staggered difference)
  AVG   : nabla_m = transverse-averaged unit difference
  BAD   : component-dependent normalization 2*Delta for m=0 (control: IR first moment wrong)
Rank: float SVD on integer matrices (gap reported) in 4D; exact GF(p) rank in 3D.
"""
import numpy as np, itertools
P = 1000003

def build(dim, n, stencil):
    sites = list(itertools.product(range(n), repeat=dim))
    sid = {s: i for i, s in enumerate(sites)}
    nunk = dim * len(sites)
    def var(nu, x):
        return None if x not in sid else nu * len(sites) + sid[x]
    def e(mu, a=1):
        v = [0]*dim; v[mu] = a; return v
    def add(x, v): return tuple(i+j for i, j in zip(x, v))
    def nabla(m, nu, x):
        """returns dict var->coef for (nabla_m xi_nu) at base x (position x+e_nu/2+e_m/2)."""
        if stencil == 'K7a':
            terms = [(e(m,1),1),(e(m,0),-1)]
        elif stencil == 'BAD':
            c = 2 if m == 0 else 1
            terms = [(e(m,1),c),(e(m,0),-c)]
        elif stencil == 'IMP':  # (27(F(+1)-F(0)) - (F(+2)-F(-1)))/24, scaled by 24
            terms = [(e(m,1),27),(e(m,0),-27),(e(m,2),-1),(e(m,-1),1)]
        elif stencil == 'AVG':  # average over transverse +-e_r, r != m, nu ; scaled by 2*#r
            rs = [r for r in range(dim) if r not in (m, nu)]
            terms = []
            for r in rs:
                for sgn in (1, -1):
                    sh = [0]*dim; sh[r] = sgn
                    terms += [(add(e(m,1), sh),1),(add(e(m,0), sh),-1)]
            if not rs:
                terms = [(e(m,1),1),(e(m,0),-1)]
        out = {}
        for v, c in terms:
            j = var(nu, add(x, v))
            if j is None: return None
            out[j] = out.get(j, 0) + c
        return out
    rows = []
    scale = {'K7a':1,'BAD':1,'IMP':24,'AVG':None}
    for x in sites:
        for m in range(dim):
            for nn in range(m, dim):
                a = nabla(m, nn, x); b = nabla(nn, m, x)
                if a is None or b is None: continue
                if stencil == 'AVG':
                    # normalize each term to unit first moment: multiply by lcm of counts
                    na = 2*max(1, len([r for r in range(dim) if r not in (m, nn)]))
                    a = {k: v*1 for k, v in a.items()}; b = {k: v*1 for k, v in b.items()}
                    # both a and b have the same number of transverse terms -> same scale
                row = np.zeros(nunk, dtype=np.int64)
                for k, v in a.items(): row[k] += v
                for k, v in b.items(): row[k] += v
                rows.append(row)
    return np.array(rows), sites, var

def killing_fields(dim, sites, var, nunk):
    """10 (4D) / 6 (3D) affine Killing fields; xi_nu at position x + e_nu/2."""
    out = []
    for c in range(dim):
        v = np.zeros(nunk)
        for x in sites: v[var(c, x)] = 1.0 if True else 0
        # only component c
        v = np.zeros(nunk)
        for x in sites: v[var(c, x)] = 1.0
        out.append(v)
    for a in range(dim):
        for b in range(a+1, dim):
            v = np.zeros(nunk)
            for x in sites:
                # xi_b = +x_a (position of xi_b has x_a coordinate x[a]); xi_a = -x_b - ... position x_b + 0
                v[var(b, x)] = x[a]          # pos of xi_b: x + e_b/2 -> a-coordinate x[a]
                v[var(a, x)] = -x[b]         # pos of xi_a: x + e_a/2 -> b-coordinate x[b]
            out.append(v)
    return np.array(out)

def rank_gfp(M):
    M = M.copy() % P
    r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = None
        nz = np.nonzero(M[r:, c])[0]
        if len(nz) == 0: continue
        piv = r + nz[0]
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), P-2, P)
        M[r] = (M[r] * inv) % P
        others = np.nonzero(M[:, c])[0]
        others = others[others != r]
        if len(others):
            M[others] = (M[others] - np.outer(M[others, c], M[r])) % P
        r += 1
        if r == rows: break
    return r

for dim, n, exact in ((3, 5, True), (3, 6, True), (4, 4, False), (4, 5, False)):
    for st in ('K7a', 'IMP', 'AVG', 'BAD'):
        M, sites, var = build(dim, n, st)
        nunk = M.shape[1]
        K = killing_fields(dim, sites, var, nunk)
        res = np.abs(M.astype(float) @ K.T).max()
        if exact:
            rk = rank_gfp(M)
            ker = nunk - rk
            info = f"GF(p) rank {rk}: ker_p = {ker}"
        else:
            sv = np.linalg.svd(M.astype(float), compute_uv=False)
            tol = 1e-8 * sv[0]
            rk = int((sv > tol).sum()); ker = nunk - rk
            nzs = sv[sv > tol]
            info = f"SVD ker = {ker}, smallest nonzero sv {nzs[-1]:.3g}, largest null sv {sv[rk:].max() if rk < len(sv) else 0:.1e}"
        kk = np.linalg.matrix_rank(K)
        print(f"d={dim} box {n}^{dim} stencil {st:4s}: unknowns {nunk}, eqs {M.shape[0]}, {info}; "
              f"affine Killing family rank {kk}, max|D xi_K| = {res:g}")
    print()
print("Expected: ker = d(d+1)/2 (6 in 3D, 10 in 4D) and residual 0 for K7a/IMP/AVG;")
print("BAD: rescaled first moment -> the affine family above is not Killing (residual 1); its own 10-dim kernel is the e(4) of a rescaled flat metric (see f1_killing_poly.out).")
