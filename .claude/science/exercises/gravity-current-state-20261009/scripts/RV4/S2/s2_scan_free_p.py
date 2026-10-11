"""S2 (a): fixed nearest-neighbour KG dispersion, momentum symbol p FREE (odd, periodic, cubic covariant, p~k),
range r<=4 (max-norm), separable and non-separable.  mu_ch = a^T Q_ch(M) a.
(1) named symbols; (2) common zeros of mu_E, mu_T2 at one mass (closest to sin k); (3) mass dependence;
(4) all-mass question via level-set moments <g_ch Psi_n(A)>, Psi_n Chebyshev in the KG symbol A."""
import numpy as np, time
from scipy.optimize import minimize
from s2_core import *
np.set_printoptions(linewidth=160, precision=4)
rng = np.random.default_rng(1)

def solve_common_zero(Qs, c, a_ref, nstart=30):
    """min |a-a_ref|^2 s.t. a^T Q a = 0 for Q in Qs, c.a = 1.  returns best feasible."""
    cons = [{'type': 'eq', 'fun': (lambda a, Q=Q: a @ Q @ a / max(1e-30, np.abs(Q).max()))} for Q in Qs]
    cons.append({'type': 'eq', 'fun': lambda a: c @ a - 1})
    best = None
    for s in range(nstart):
        a0 = a_ref + (0.3 if s else 0.0)*rng.standard_normal(len(a_ref))*(1+s/10)
        r = minimize(lambda a: np.sum((a-a_ref)**2), a0, constraints=cons, method='SLSQP',
                     options={'maxiter': 2000, 'ftol': 1e-14})
        viol = max(abs(cn['fun'](r.x)) for cn in cons)
        if viol < 1e-10 and (best is None or r.fun < best.fun):
            best = r
    return best

for d, L, r in [(2, 128, 4), (3, 48, 4)]:
    tl = terms(d, r); c = slope_vec(tl); T = len(tl)
    print(f"\n================ d={d}  range<={r}  ({T} terms)  L={L} ================")
    Qm = {}
    for M in [1.0, 0.3]:
        t0 = time.time(); Qm[M] = quad_forms(d, L, tl, lambda K, M=M: kg_vac(K, M)); 
        print(f"Q forms at M={M} built ({time.time()-t0:.1f}s)")
    def mus(a, M):
        return tuple(a @ Qm[M][ch] @ a for ch in ('E', 'T2', 'tr'))
    def unit(t):
        a = np.zeros(T); a[tl.index(t)] = 1.0/t[0]; return a
    one = (1, 0) if d == 2 else (1, 0, 0); diag = (1, 1) if d == 2 else (1, 1, 1)
    a_sin = unit(one)
    print("-- named symbols (mu_E, mu_T2, mu_tr) at M=1 | M=0.3")
    named = {'sin k (separable)': a_sin, 'diag: sin kx cos ky [cos kz]': unit(diag)}
    a_imp = np.zeros(T); a_imp[tl.index(one)] = 4/3; a_imp[tl.index((2,0) if d==2 else (2,0,0))] = -1/6   # O(k^5) improved sin
    named['improved (4/3 sin k - 1/6 sin 2k)'] = a_imp
    for nm, a in named.items():
        print(f"   {nm:38s} " + " ".join(f"{x:+.4e}" for x in mus(a, 1.0)) + " | " + " ".join(f"{x:+.4e}" for x in mus(a, 0.3)))
    # eigen-structure: is each form indefinite on the slope hyperplane?
    for M in [1.0]:
        for ch in ('E', 'T2'):
            ev = np.linalg.eigvalsh(Qm[M][ch]); print(f"   Q_{ch}(M={M}) eigenvalues: min {ev.min():+.3e} max {ev.max():+.3e}  (#neg {np.sum(ev<-1e-12)}, #pos {np.sum(ev>1e-12)})")
    # (2) common zero at one mass, nearest to sin k
    for M in [1.0, 0.3]:
        b = solve_common_zero([Qm[M]['E'], Qm[M]['T2']], c, a_sin)
        if b is None: print(f"-- no common zero found at M={M}"); continue
        a = b.x
        print(f"-- common zero mu_E=mu_T2=0 at M={M}: |a - a_sin| = {np.sqrt(b.fun):.4f}")
        print("   largest coefficients:", sorted([(round(a[i],4), tl[i]) for i in range(T)], key=lambda z: -abs(z[0]))[:6])
        for M2 in [1.0, 0.3]:
            print(f"   at M={M2}: mu_E={mus(a,M2)[0]:+.4e}  mu_T2={mus(a,M2)[1]:+.4e}  mu_tr={mus(a,M2)[2]:+.4e}   [F(M2)-scale ref mu_E(sin k)={mus(a_sin,M2)[0]:+.4e}]")
        np.save(f"s2_zero_d{d}_M{M}.npy", a)
    # (3) zero at both masses simultaneously, test elsewhere
    b = solve_common_zero([Qm[1.0]['E'], Qm[1.0]['T2'], Qm[0.3]['E'], Qm[0.3]['T2']], c, a_sin)
    if b is not None:
        a = b.x; np.save(f"s2_zero_d{d}_both.npy", a)
        print(f"-- zero at M=1 AND M=0.3 (4 eqs): |a-a_sin|={np.sqrt(b.fun):.4f}; residual at other masses:")
        for M2 in [0.1, 0.5, 2.0, 4.0]:
            Q2 = quad_forms(d, L, tl, lambda K, M=M2: kg_vac(K, M), chans=('E', 'T2'))
            ref = a_sin @ Q2['E'] @ a_sin
            print(f"   M={M2}: mu_E={a@Q2['E']@a:+.4e} mu_T2={a@Q2['T2']@a:+.4e}  (sin k mu_E {ref:+.4e})")
    else:
        print("-- no zero at both masses found")
    # (4) all-mass: Chebyshev level-set moments  mu(M)=0 for all M  <=>  <g_ch Psi_n(A)> = 0 all n
    Amax = 4.0*d
    def vac_cheb(K, n):
        A = sum(4*np.sin(k/2)**2 for k in K)
        x = 2*A/Amax - 1
        Tn = np.cos(n*np.arccos(np.clip(x, -1, 1)))
        # g = (grad Omega/2 . v) div v with grad(Omega/2)=sin k  (Omega=omega^2); weight Psi_n(A)
        return 0.5*Tn, [np.sin(k)*Tn for k in K]
    NM = 3*d*r + 6
    vecs = []
    for n in range(NM):
        Qn = quad_forms(d, L if d == 3 else 128, tl, lambda K, n=n: vac_cheb(K, n), chans=('E', 'T2'))
        for ch in ('E', 'T2'):
            S = Qn[ch]; vecs.append(S[np.triu_indices(T)])
    V = np.array(vecs); sv = np.linalg.svd(V, compute_uv=False)
    rank = np.sum(sv > 1e-10*sv[0])
    print(f"-- all-mass conditions: {len(vecs)} quadratic forms (n<{NM}, E and T2); numerical rank {rank} (unknowns {T}, minus 1 slope)")
    # least-squares attempt: minimise sum of squared normalised moments with slope fixed
    Qlist = [];
    for n in range(NM):
        Qn = quad_forms(d, L if d == 3 else 128, tl, lambda K, n=n: vac_cheb(K, n), chans=('E', 'T2'))
        Qlist += [Qn['E'], Qn['T2']]
    def obj(a): return sum((a @ Q @ a)**2 for Q in Qlist)
    best = None
    for s in range(12):
        a0 = a_sin + 0.5*rng.standard_normal(T)
        cons = [{'type': 'eq', 'fun': lambda a: c @ a - 1}]
        rr = minimize(obj, a0, constraints=cons, method='SLSQP', options={'maxiter': 3000, 'ftol': 1e-30})
        if best is None or rr.fun < best.fun: best = rr
    a = best.x
    print(f"   best sum of squared moments = {best.fun:.3e} (sin k: {obj(a_sin):.3e});  |a| = {np.linalg.norm(a):.3f}")
    for M2 in [0.1, 0.3, 1.0, 3.0]:
        Q2 = quad_forms(d, L, tl, lambda K, M=M2: kg_vac(K, M), chans=('E', 'T2'))
        print(f"   M={M2}: mu_E={a@Q2['E']@a:+.4e} mu_T2={a@Q2['T2']@a:+.4e}  (sin k mu_E {a_sin@Q2['E']@a_sin:+.4e})")
