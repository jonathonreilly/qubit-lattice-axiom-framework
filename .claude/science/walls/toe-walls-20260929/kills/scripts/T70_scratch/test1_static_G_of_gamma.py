"""Test 1 (T70): which Newton constant does gamma give in the supplied static model
(blocks 55-56), and which K does a = l_P ask for?

Model (docs/ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_...2026-09-21.md, T1-T4):
  rates w = phi^2 ; F = (2/gamma) sum_bonds (phi_x-phi_y)^2 ; bodies at rest, bare energy m_i,
  walls phi = 1 ; static law ((1-A)+D) phi = walls, D = (gamma/12) M ; ledger = sum m_i phi_i
  (= total static energy: bodies in the field m phi^2 plus field energy F).
Prints: far field of phi and of w=phi^2, pair ledger deficit vs separation, lattice Green function
asymptotics c(r) -> 3/(2 pi r), and the resulting G_lat(gamma) and K*.
"""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spla, math, sys

gamma = 1.0

def build(L):
    n = L - 2                       # interior side
    idx = np.arange(n**3).reshape(n, n, n)
    rows, cols, vals = [], [], []
    diag = np.ones(n**3)            # (1 - A) has diagonal 1
    b = np.zeros(n**3)
    off = []
    for ax in range(3):
        for s in (+1, -1):
            sl_from = [slice(None)]*3; sl_to = [slice(None)]*3
            if s == +1:
                sl_from[ax] = slice(0, n-1); sl_to[ax] = slice(1, n)
            else:
                sl_from[ax] = slice(1, n); sl_to[ax] = slice(0, n-1)
            i = idx[tuple(sl_from)].ravel(); j = idx[tuple(sl_to)].ravel()
            rows.append(i); cols.append(j); vals.append(np.full(i.size, -1/6))
            # boundary neighbours = walls (phi=1): contribute +1/6 to rhs
            sl_edge = [slice(None)]*3
            sl_edge[ax] = (n-1) if s == +1 else 0
            e = idx[tuple(sl_edge)].ravel()
            b[e] += 1/6
    A1 = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n**3, n**3))
    return n, idx, A1 + sp.identity(n**3, format='csr'), b

def solve(L, bodies, gamma=1.0):
    n, idx, M0, b = build(L)
    d = np.zeros(n**3)
    for (pos, m) in bodies:
        d[idx[pos]] += gamma/12*m
    M = M0 + sp.diags(d)
    phi, info = spla.cg(M, b, rtol=1e-13, atol=0, maxiter=4000)
    assert info == 0, info
    ledger = sum(m*phi[idx[pos]] for pos, m in bodies)
    return phi.reshape(n, n, n), ledger, idx

def watson_c(r_vec, N=384):
    """c(r) = G_inf(0) - int (1-cos q.r)/(1-A(q)) d^3q/(2pi)^3 , G_inf(0)=1.516386 (3 x Watson 0.505462)."""
    q = 2*np.pi*(np.arange(N)+0.5)/N          # midpoint grid: avoids q=0
    qx, qy, qz = np.meshgrid(q, q, q, indexing='ij')
    den = 1 - (np.cos(qx)+np.cos(qy)+np.cos(qz))/3
    num = 1 - np.cos(qx*r_vec[0]+qy*r_vec[1]+qz*r_vec[2])
    return 1.516386 - float(np.mean(num/den))

if __name__ == "__main__":
    out = []
    P = lambda *a: (print(*a), out.append(" ".join(str(x) for x in a)))
    P("=== lattice Green function of (1-A) on Z^3: c(r) and its Coulomb tail 3/(2 pi r) ===")
    for r in (2, 4, 6, 8, 12):
        c = watson_c((r, 0, 0))
        P(f"r={r:3d}  c(r)={c:.5f}   c*(2 pi r/3)={c*2*np.pi*r/3:.4f}")
    P()
    P("=== one body, weak field, box 61 (interior 59): far field of phi and of w=phi^2 ===")
    L = 61; n = L-2; ctr = (n//2,)*3; m = 0.02
    phi, led, idx = solve(L, [(ctr, m)], gamma)
    for r in (4, 6, 8, 12):
        p = phi[ctr[0]+r, ctr[1], ctr[2]]
        # box correction: compare against the box Green function via the same solve for m->tiny is same; use Coulomb + const
        P(f"r={r:3d}  (1-phi)*r/(gamma*m/(8pi)) = {(1-p)*r/(gamma*m/(8*np.pi)):.4f}    (1-w)*r/(gamma*m/(4pi)) = {(1-p*p)*r/(gamma*m/(4*np.pi)):.4f}")
    P("(walls at distance 30 shift these by an additive constant ~ few %; use the slope in 1/r, which removes the wall constant)")
    rs = np.array([4, 6, 8, 12]); vals = np.array([1-phi[ctr[0]+r, ctr[1], ctr[2]] for r in rs])
    slope = np.polyfit(1/rs, vals, 1)[0]
    P(f"slope d(1-phi)/d(1/r) = {slope:.6e}   gamma m/(8 pi) = {gamma*m/(8*np.pi):.6e}   ratio = {slope/(gamma*m/(8*np.pi)):.4f}")
    valsw = np.array([1-phi[ctr[0]+r, ctr[1], ctr[2]]**2 for r in rs]); slw = np.polyfit(1/rs, valsw, 1)[0]
    P(f"slope d(1-w)/d(1/r)   = {slw:.6e}   gamma m/(4 pi) = {gamma*m/(4*np.pi):.6e}   ratio = {slw/(gamma*m/(4*np.pi)):.4f}   (w = phi^2 = local clock rate)")
    P()
    P("=== pair, weak field, box 81: ledger deficit vs (gamma/6) m1 m2 c_box and vs the Coulomb value gamma m1 m2/(4 pi r) ===")
    L = 81; n = L-2; ctr = n//2
    m1 = m2 = 0.05
    rows = []
    for r in (3, 5, 8, 12):
        p1 = (ctr-r//2, ctr, ctr); p2 = (ctr-r//2+r, ctr, ctr)
        _, l12, _ = solve(L, [(p1, m1), (p2, m2)], gamma)
        _, l1, _ = solve(L, [(p1, m1)], gamma)
        _, l2, _ = solve(L, [(p2, m2)], gamma)
        deficit = l1 + l2 - l12
        c_inf = watson_c((r, 0, 0))
        # exact box Green function c_box(x1,x2) of (1-A) with zero walls
        n_, idx_, M0_, b_ = build(L)
        e = np.zeros(n_**3); e[idx_[p1]] = 1.0
        g_, info_ = spla.cg(M0_, e, rtol=1e-13, atol=0, maxiter=4000)
        c_box = g_[idx_[p2]]
        P(f"      c_box(x1,x2)={c_box:.5f}  c_inf(r)={c_inf:.5f}  deficit/[(g/6) m1 m2 c_box]={deficit/((gamma/6)*m1*m2*c_box):.4f}  (T4: leading term; m-corrections O(m))")
        P(f"r={r:3d} deficit={deficit:.6e}  /[(g/6)m1m2 c_inf(r)]={deficit/((gamma/6)*m1*m2*c_inf):.4f}  "
          f"/[g m1 m2/(4 pi r)]={deficit/(gamma*m1*m2/(4*np.pi*r)):.4f}  /[g m1 m2/(8 pi r)]={deficit/(gamma*m1*m2/(8*np.pi*r)):.4f}")
    P()
    P("=== conversion table (arithmetic) ===")
    P("gamma = 1/(4K) (block 55 Corollary: log kappa = -m/(24K) = -(gamma/6) m, note 2026-09-21 curvature-member, line 75)")
    P("static pair energy: E_int = -(gamma/6) m1 m2 c(r) -> -gamma m1 m2/(4 pi r)  => G_lat = gamma/(4 pi) = 1/(16 pi K)")
    P("comparator (ADM, h_ij = ell^2 delta): L_kin = -(6/(16 pi G)) ell ell'^2/N  vs block 60  c_k = -6K  => K = 1/(16 pi G): agrees")
    for label, G in (("G_lat=1 (G=l_P^2, unreduced Planck mass)", 1.0), ("8 pi G_lat = 1 (reduced Planck mass)", 1/(8*np.pi))):
        K = 1/(16*np.pi*G); gam = 4*np.pi*G
        P(f"{label}: gamma* = {gam:.5f}, K* = {K:.5f}")
    for K in (1/4, 1/2, 1.0):
        G = 1/(16*np.pi*K)
        P(f"K={K}: gamma={1/(4*K)}, G_lat={G:.5f}, a/l_P = 1/sqrt(G_lat) = {1/np.sqrt(G):.3f}, a/l_P(reduced) = 1/sqrt(8 pi G) = {1/np.sqrt(8*np.pi*G):.3f}")
    P("entry's mapping G=gamma/(8 pi) would give K* = 1/(32 pi) = %.5f (unreduced): factor 2 different" % (1/(32*np.pi)))
    open(sys.path[0] + "/test1_output.txt", "w").write("\n".join(out) + "\n")
