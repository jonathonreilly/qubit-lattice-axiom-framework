"""R19-25 s3: the Gupta-Bleuler null pair (the unphysical half of a quartet) on finite Krein slots.
Pre-registered (07:01Z, before running):
 Model: slot L (metric +1), slot T (metric (-1)^n, the negative-norm partner), each d-dimensional, lowering A
 (n -> n-1): HP  A|n> = sqrt(n(2S-n+1)/(2S))|n-1>, d = 2S+1;  truncated boson A|n> = sqrt(n)|n-1>.
 Krein adjoint X^K = eta X^dag eta. G+ = A_L - A_T, H0 = w (n_L + n_T) (exact frequency: [H0, G+] = -w G+).
 CCR: [G+, G+^K] = [A_L,A_L^K] + [A_T,A_T^K] = 1 - 1 = 0 (null constraint); V = ker G+ = span{X^N|0>}, all
 null for N >= 1, quotient = vacuum only.
 Finite d: (1) nullness defect [G+, G+^K] (HP: (n_T - n_L)/S; truncated: d(P_top,T - P_top,L)) -- a KO-type Q has
 Q^2 proportional to it; (2) per-level N inertia of the Krein Gram on V_N: CCR gives (0,0,1) for N>=1;
 (3) the sourced weak condition (G+ - rho) psi = 0, rho != 0: G+ nilpotent => only psi = 0 (min singular value);
 (4) leak of V under a coupling J*phi to the BRST-closed field phi = (A_L + A_L^K) - (A_T + A_T^K):
     [G+, phi] (CCR: 0); norm of the leak on V_N.
 (5) Lemma K check: for C+ = sum_a Y_a on separate slots, [C+, C+^K] = sum_a [Y_a, Y_a^K], and the partial trace
     isolates each term, so exact nullness forces [Y_a, Y_a^K] = 0 slot by slot (random instances).
"""
import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=150)

def lowering(d, kind, S=None):
    A = np.zeros((d, d))
    for n in range(1, d):
        A[n-1, n] = np.sqrt(n*(2*S - n + 1)/(2*S)) if kind == 'HP' else np.sqrt(n)
    return A

def analyse(d, kind):
    S = (d - 1)/2
    A = lowering(d, kind, S); I = np.eye(d)
    etaL = np.eye(d); etaT = np.diag([(-1.)**n for n in range(d)])
    eta = np.kron(etaL, etaT)
    K = lambda X: eta@X.conj().T@eta
    AL = np.kron(A, I); AT = np.kron(I, A)
    Gp = AL - AT
    nL = np.kron(np.diag(np.arange(d)), I); nT = np.kron(I, np.diag(np.arange(d))); N = np.diag(nL + nT)
    H0 = nL + nT
    freq = np.abs(H0@Gp - Gp@H0 + Gp).max()
    null_defect = Gp@K(Gp) - K(Gp)@Gp
    phi = (AL + K(AL)) - (AT + K(AT))
    leak = Gp@phi - phi@Gp
    # per-level kernel of G+ and Krein Gram inertia
    rows = []
    first_bad = None
    for lev in range(0, 2*d - 1):
        idx = np.where(np.abs(N - lev) < 1e-9)[0]; dn = np.where(np.abs(N - (lev - 1)) < 1e-9)[0]
        if len(dn):
            M = Gp[np.ix_(dn, idx)]
            u, s, vh = np.linalg.svd(M)
            r = int((s > 1e-10).sum()); ker = vh[r:].conj().T
        else:
            ker = np.eye(len(idx))
        if ker.shape[1] == 0:
            rows.append((lev, 0, (0, 0, 0), 0.0)); continue
        Vfull = np.zeros((d*d, ker.shape[1]), complex); Vfull[idx] = ker
        Gram = Vfull.conj().T@eta@Vfull
        ev = np.linalg.eigvalsh((Gram + Gram.conj().T)/2)
        tol = 1e-9
        inert = (int((ev > tol).sum()), int((ev < -tol).sum()), int((np.abs(ev) <= tol).sum()))
        lk = np.linalg.norm(leak@Vfull, 2) if Vfull.size else 0.0
        rows.append((lev, ker.shape[1], inert, lk))
        if lev >= 1 and (inert[0] or inert[1]) and first_bad is None:
            first_bad = (lev, inert, ev[np.abs(ev) > tol])
    # sourced condition
    smin = np.linalg.svd(Gp - 0.3*np.eye(d*d), compute_uv=False).min()
    nilp = next(k for k in range(1, 4*d) if np.abs(np.linalg.matrix_power(Gp, k)).max() < 1e-12)
    return dict(freq=freq, null_norm=np.linalg.norm(null_defect, 2),
                null_on_low=np.linalg.norm(null_defect[np.ix_(N <= 2, N <= 2)], 2),
                rows=rows, first_bad=first_bad, smin=smin, nilp=nilp,
                leak_norm=np.linalg.norm(leak, 2), null_diag=np.diag(null_defect).real)

for kind in ['HP', 'trunc']:
    print(f"=== {kind} slots ===")
    for d in [2, 3, 5, 9, 17]:
        r = analyse(d, kind)
        print(f" d={d:2d}: exact frequency residual {r['freq']:.1e}; ||[G+,G+^K]|| full = {r['null_norm']:.4f}, on N<=2: {r['null_on_low']:.4f};"
              f" G+ nilpotent of index {r['nilp']}; min sing. value of (G+ - 0.3) = {r['smin']:.3f}; ||[G+,phi]|| = {r['leak_norm']:.3f}")
        fb = r['first_bad']
        print(f"       first level N>=1 where V_N is not purely null: {None if fb is None else (fb[0], fb[1], np.round(fb[2], 4))}")
        if d in (5, 9):
            print("       per level (N, dim V_N, inertia(+,-,0), ||leak on V_N||):",
                  [(a, b, c, round(e, 3)) for (a, b, c, e) in r['rows'][:min(len(r['rows']), 2*d - 1)]])

print("\n(5) Lemma K: partial trace isolates each single-slot term of [C+, C+^K]")
rng = np.random.default_rng(1)
for trial in range(3):
    dims = [3, 2, 4]; etas = [np.diag(rng.choice([-1., 1.], size=k)) for k in dims]
    Ys = [rng.normal(size=(k, k)) + 1j*rng.normal(size=(k, k)) for k in dims]
    def emb(X, a):
        mats = [np.eye(k) for k in dims]; mats[a] = X; M = mats[0]
        for Z in mats[1:]: M = np.kron(M, Z)
        return M
    eta = emb(etas[0], 0)@emb(etas[1], 1)@emb(etas[2], 2)
    C = sum(emb(Ys[a], a) for a in range(3)); CK = eta@C.conj().T@eta
    comm = C@CK - CK@C
    kap = [Ys[a]@etas[a]@Ys[a].conj().T@etas[a] - etas[a]@Ys[a].conj().T@etas[a]@Ys[a] for a in range(3)]
    # partial trace over slots other than a
    T = comm.reshape(dims + dims)
    pt0 = np.einsum('ibcjbc->ij', T); pt1 = np.einsum('aibajb->ij', T); pt2 = np.einsum('abiabj->ij', T)
    res = [np.abs(pt0 - kap[0]*dims[1]*dims[2]).max(), np.abs(pt1 - kap[1]*dims[0]*dims[2]).max(), np.abs(pt2 - kap[2]*dims[0]*dims[1]).max()]
    print(f"  trial {trial}: |partial trace - (prod dims) kappa_a| = {np.round(res, 12)};  tr kappa_a = {[round(abs(np.trace(k)), 12) for k in kap]}")
