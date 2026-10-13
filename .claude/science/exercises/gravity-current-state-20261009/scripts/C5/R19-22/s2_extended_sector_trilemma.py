"""R19-22 s2: the small-field (Holstein-Primakoff / large-N) linearization of the N-type at finite S is the
EXTENDED six-pair quadratic theory. What do local completions of it do?

Pre-registered (06:33Z, before running):
 (a) TT block: omega^2 = J g qhat^2 for every local penalty / completion that vanishes on TT (U|GE|^2, V|Sh|^2,
     lam (trE)^2, mu |G h|^2, nu qhat^2 (tr h)^2).  Expect exact.
 (b) lam = 0, any finite U, V: scalar kinetic block has det = -J^2/2 (N0914:338-346 recheck, count once);
     Hamilton matrix nilpotent on scalar+vector sectors (Jordan chains).
 (c) lam > J/12 (kinetic made PSD): conformal mode becomes a tachyon, growth rate gamma ~ c |k| at small k.
 (d) full PSD local completion (lam, mu, nu > thresholds): number of gapless branches at small k > 2
     (expect 6 here; R15-3 refereed bound is >= 4 for the finite continuous PSD class, count once).
Conventions: orthonormal Sym^2 basis; R(h) := -eps eps qhat qhat h (momentum space) so h:R(h) = +qhat^2|h|^2 on TT;
H = 1/2 p^T A p + 1/2 q^T B q, qdot = A p, pdot = -B q, Hamilton matrix F = [[0,A],[-B,0]]; omega^2 = eig(A B).
"""
import numpy as np
np.set_printoptions(precision=5, suppress=True, linewidth=150)

def sym_basis():
    Bs = []
    for i in range(3):
        M = np.zeros((3, 3)); M[i, i] = 1; Bs.append(M)
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1/np.sqrt(2); Bs.append(M)
    return Bs
BS = sym_basis()
def vec(M): return np.array([np.sum(M*b) for b in BS])
eps = np.zeros((3, 3, 3))
for (i, j, k), s in {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}.items(): eps[i,j,k] = s

def ops(k):
    q = 2*np.sin(np.asarray(k, float)/2)
    G = np.array([[q @ b[:, j] for b in BS] for j in range(3)])          # (G E)_j = q_i E_ij
    S = np.array([[q@b@q - (q@q)*np.trace(b) for b in BS]])                              # S h = q q h - q^2 tr h
    R = np.zeros((6, 6))
    for c, b in enumerate(BS):
        Rb = -np.einsum('iab,jcd,a,c,bd->ij', eps, eps, q, q, b)
        R[:, c] = vec(Rb)
    t = np.array([np.trace(b) for b in BS])
    return q, G, S, (R + R.T)/2, t

def tt_basis(q):
    n = q/np.linalg.norm(q); a = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0])
    e1 = a - (a@n)*n; e1 /= np.linalg.norm(e1); e2 = np.cross(n, e1)
    P = [vec((np.outer(e1, e1) - np.outer(e2, e2))/np.sqrt(2)), vec((np.outer(e1, e2) + np.outer(e2, e1))/np.sqrt(2))]
    return np.array(P).T

def build(k, J=1., g=1., U=0., V=0., lam=0., mu=0., nu=0.):
    q, G, S, R, t = ops(k); q2 = q@q
    A = J*(np.eye(6) - 0.5*np.outer(t, t)) + U*G.T@G + 2*lam*np.outer(t, t)
    B = g*R + V*S.T@S + mu*G.T@G + nu*q2*np.outer(t, t)
    return q, A, B, G, S, R, t

dirs = {'z': [0, 0, 1], '110': [1, 1, 0], '111': [1, 1, 1], '125': [1, 2, 5]}
print("(0) sanity: h-side spectrum of R/qhat^2 and E-side spectrum of K at k=0.3 along (1,2,5)")
q, A, B, G, S, R, t = build(0.3*np.array(dirs['125'])/np.linalg.norm(dirs['125']))
print("  eig R/qhat^2 =", np.linalg.eigvalsh(R)/(q@q), "  eig K =", np.linalg.eigvalsh(np.eye(6) - 0.5*np.outer(t, t)))
print("  G S^T =", np.abs(G@S.T).max(), "  G R =", np.abs(G@R).max())

print("\n(a) TT block omega^2/(J g qhat^2) under every completion (k=1e-2)")
pars = [dict(), dict(U=5, V=3), dict(U=5, V=3, lam=1.0), dict(U=5, V=3, lam=1.0, mu=2.0, nu=4.0)]
for name, d in dirs.items():
    kk = 1e-2*np.array(d)/np.linalg.norm(d)
    out = []
    for p in pars:
        q, A, B, *_ = build(kk, **p); P = tt_basis(q)
        Mtt = (P.T@A@P)@(P.T@B@P)
        # TT block decoupled? check A P, B P stay in span(P)
        leak = max(np.abs(A@P - P@(P.T@A@P)).max(), np.abs(B@P - P@(P.T@B@P)).max())
        out.append((np.linalg.eigvals(Mtt).real/(q@q), leak))
    print(f"  {name:4s}", "  ".join(f"[{o[0][0]:.6f},{o[0][1]:.6f}] leak {o[1]:.1e}" for o in out))

def nilpotency(F, tol=1e-9):
    M = np.eye(F.shape[0]); idx = []
    for n in range(1, 9):
        M = M@F; idx.append(np.linalg.matrix_rank(M, tol=tol*max(1, np.abs(F).max()**n)))
    return idx

print("\n(b) lam=0, finite penalties: scalar kinetic det and Hamilton-matrix structure (k=0.05 along z)")
for (U, V) in [(0, 0), (1, 0), (10, 10), (1000, 1000)]:
    kk = np.array([0, 0, 0.05]); q, A, B, G, S, R, t = build(kk, U=U, V=V)
    # scalar sector basis: transverse trace e_t and longitudinal e_z (orthonormal)
    n = q/np.linalg.norm(q); PT = np.eye(3) - np.outer(n, n)
    es = np.array([vec(PT/np.sqrt(2)), vec(np.outer(n, n))]).T
    As = es.T@A@es; Bs = es.T@B@es
    F = np.block([[np.zeros((6, 6)), A], [-B, np.zeros((6, 6))]])
    ev = np.linalg.eigvals(A@B)
    print(f"  U={U:5g} V={V:5g}: det A_scalar = {np.linalg.det(As):+.4f} (J=1: -1/2 expected);"
          f" B_scalar diag = {np.diag(Bs)} ; eig(AB)/q^2 = {np.sort(ev.real)/(q@q)}")
    # restrict F to the non-TT 4-dim subspace (scalar+vector) and check nilpotency
    P = tt_basis(q); Q = np.linalg.svd(np.eye(6) - P@P.T)[0][:, :4]
    Fn = np.block([[np.zeros((4, 4)), Q.T@A@Q], [-(Q.T@B@Q), np.zeros((4, 4))]])
    print(f"       rank(F_nonTT^n), n=1..6: {nilpotency(Fn)}  (0 => nilpotent: Jordan chains, polynomial growth)")

print("\n(c) kinetic made PSD by lam (trE)^2: conformal-mode growth rate gamma(k) = sqrt(-min eig(AB))")
for lam in [0.1, 0.25, 1.0]:
    row = []
    for kz in [1e-1, 1e-2, 1e-3, 1e-4]:
        q, A, B, *_ = build(np.array([0, 0, kz]), U=1.0, V=1.0, lam=lam)
        ev = np.linalg.eigvals(A@B).real
        gam = np.sqrt(max(0, -ev.min())); row.append(gam/np.linalg.norm(q))
    q, A, *_ = build(np.array([0, 0, 1e-2]), U=1.0, V=1.0, lam=lam)
    print(f"  lam={lam:5.2f}: min eig A = {np.linalg.eigvalsh(A).min():+.4f};  gamma/|qhat| at k=1e-1..1e-4 = {np.round(row, 6)}")

print("\n(d) full PSD local completion: count small-k branches with omega -> 0 (k=1e-3, 1e-4)")
# scalar B block = qhat^2 [[2nu-1, sqrt2 nu],[sqrt2 nu, nu+mu]] at small k: PSD iff nu>=1/2 and 2 nu mu >= nu + mu (derived by hand)
for p in [dict(U=1, V=1, lam=1, mu=2, nu=2), dict(U=3, V=2, lam=0.5, mu=3, nu=1), dict(U=1, V=1, lam=0.3, mu=1, nu=5), dict(U=1, V=1, lam=1, mu=1, nu=1), dict(U=1, V=1, lam=1, mu=1, nu=0.6)]:
    res = []
    for kz in [1e-3, 1e-4]:
        kk = kz*np.array(dirs['125'])/np.linalg.norm(dirs['125'])
        q, A, B, *_ = build(kk, **p)
        psd = (np.linalg.eigvalsh(A).min() > -1e-12, np.linalg.eigvalsh(B).min() > -1e-12*(q@q))
        w2 = np.sort(np.linalg.eigvals(A@B).real)
        res.append((psd, w2/(q@q)))
    print(f"  {p}: PSD(A,B)={res[0][0]}; omega^2/qhat^2 at 1e-3: {res[0][1]}; at 1e-4: {res[1][1]}")

print("  (gamma formula check: 4*lam for B11=-q^2 => gamma/|q| = 2 sqrt(lam):", [round(2*np.sqrt(l),5) for l in (0.1,0.25,1.0)], ")")
print("\n(e) trace collapse, one cell, diagonal slots only: min over |e_i|<=Emax of e.e - (sum e)^2/2")
for Emax2, lab in [(1.0, 'Emax^2=1'), (16.0, 'Emax^2=16')]:
    import itertools
    best = min(sum(x*x for x in e) - 0.5*sum(e)**2 for e in itertools.product(np.linspace(-np.sqrt(Emax2), np.sqrt(Emax2), 9), repeat=3))
    print(f"  {lab}: min K_diag = {best:+.4f}  (claim -3/2 Emax^2 = {-1.5*Emax2:+.4f})")
