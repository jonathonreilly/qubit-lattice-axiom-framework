#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 66 (floating point; machinery disjoint from the exact runner's).

W1  the three lattice identities of T3 on a random COMPLEX state with a random positive rate field, 6x5x4 torus.
W2  a packet of the clocked walk on a ring of 256 in a smooth rate well: the rate of change of its lattice momentum <S>, by finite differences of an
    accurate evolution, against minus the total force (exact identity) and against minus the total weight sum e du (leading order only).
W3  a STATIONARY state of H_w (numerical eigenvector on the ring): is the divergence of the bond current of phi psi equal to minus the force density,
    site by site?  how close is the force density to the weight?
W4  the ledger's identity for a third member of block 64's family with other coefficients (exact symbolic algebra, second order)."""
import numpy as np
import sympy as sp
from scipy.linalg import expm

rng = np.random.default_rng(6)
sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]

if __name__ == "__main__":
    shape = (6,5,4)
    up = lambda f, a: np.roll(f, -1, axis=a); dn = lambda f, a: np.roll(f, 1, axis=a)
    S = lambda f, j: (up(f,j) - dn(f,j))/(2j)
    sg = lambda a, f: np.einsum("st,...t->...s", sig[a], f)
    H = lambda f: sum(sg(a, S(f,a)) for a in range(3))
    C = lambda f, a, w: 0.5*(w[...,None]*up(f,a) + dn(w,a)[...,None]*dn(f,a))
    dot = lambda f, g: np.einsum("...s,...s->...", f.conj(), g)
    psi = rng.standard_normal(shape+(2,)) + 1j*rng.standard_normal(shape+(2,))
    phi = np.exp(0.3*rng.standard_normal(shape)); xi = [rng.standard_normal(shape) for _ in range(3)]
    Pm = lambda f: phi[...,None]*f
    r1 = max(np.abs(1j*(Pm(S(psi,j)) - S(Pm(psi),j)) + C(psi, j, up(phi,j)-phi)).max() for j in range(3))
    G = lambda f: sum(0.5*(xi[j][...,None]*S(f,j) + S(xi[j][...,None]*f, j)) for j in range(3))
    Hw = lambda f: Pm(H(Pm(f)))
    Lam = lambda f: sum(0.5*(xi[j][...,None]*C(f, j, up(phi,j)-phi) + C(xi[j][...,None]*f, j, up(phi,j)-phi)) for j in range(3))
    lhs = 1j*(Hw(G(psi)) - G(Hw(psi)))
    rhs = Pm(1j*(H(G(Pm(psi))) - G(H(Pm(psi))))) - (Lam(H(Pm(psi))) + Pm(H(Lam(psi))))
    print(f"[W1] |i[phi,S] + C[d phi]| = {r1:.1e};  |i[H_w,G] - (phi i[H,G] phi - Lam H phi - phi H Lam)| = {np.abs(lhs-rhs).max():.1e}")

    n = 256; x = np.arange(n)
    u = -0.3*np.exp(-((x-n/2)/40.0)**2); ph = np.exp(u/2)
    S1 = np.zeros((n,n), complex)
    for i in range(n): S1[i,(i+1)%n] += 1/(2j); S1[i,(i-1)%n] -= 1/(2j)
    Hring = np.kron(np.diag(ph)@S1@np.diag(ph), sig[2])                       # coin along sigma_3 on a ring: H_w = phi (sigma_3 S) phi
    k0 = 0.35; env = np.exp(-((x-n/2+45)/14.0)**2)
    psi0 = np.kron(env*np.exp(1j*k0*x), np.array([1.0, 0.0])); psi0 /= np.linalg.norm(psi0)
    Sfull = np.kron(S1, np.eye(2))
    dt = 0.5; U = expm(-1j*Hring*dt)
    def force_and_weight(v):
        a = v.reshape(n,2); chi = ph[:,None]*a
        g = (np.roll(chi,-1,0) - np.roll(chi,1,0))/(2j)*np.array([1,-1])[None,:]
        w = np.roll(ph,-1) - ph
        Cf = lambda f: 0.5*(w[:,None]*np.roll(f,-1,0) + np.roll(w,1)[:,None]*np.roll(f,1,0))
        f = np.real(np.einsum("xs,xs->x", Cf(a).conj(), g) + np.einsum("xs,xs->x", a.conj(), Cf(g)))
        e = np.real(np.einsum("xs,xs->x", chi.conj(), g)); du = (np.roll(u,-1) - np.roll(u,1))/2
        return f.sum(), (e*du).sum()
    print("\n[W2] packet in a rate well (depth 0.3, width 40), wave number 0.35; t, d<S>/dt by finite differences, -total force, -total weight:")
    v = psi0.copy(); mom = []; data = []
    for step in range(121):
        mom.append(np.real(v.conj()@Sfull@v)); data.append(force_and_weight(v)); v = U@v
    for step in (20, 40, 60, 80, 100):
        num = (mom[step+1]-mom[step-1])/(2*dt)
        print(f"     t = {step*dt:5.1f}: {num:+.6e}   {-data[step][0]:+.6e}   {-data[step][1]:+.6e}   (ratio force/weight {data[step][0]/data[step][1]:.4f}; cos k0 = {np.cos(k0):.4f})")

    print("\n[W3] stationary states of H_w on a 6x5x4 torus with a smooth rate field (numerical eigenvectors of the dense matrix): divergence of the bond")
    print("     current of phi psi against minus the force density, site by site.  (On a ring the test is empty: a non-degenerate stationary state of")
    print("     i x (real antisymmetric) carries no momentum current and feels no force density: the first version of this test reported 0 = 0.)")
    import itertools
    dims = (6,5,4); sites = list(itertools.product(*(range(d) for d in dims))); idx = {s_:i for i,s_ in enumerate(sites)}; N = len(sites)
    sh = lambda x_, a, st=1: tuple((x_[i] + (st if i == a else 0)) % dims[i] for i in range(3))
    u3 = np.array([0.25*np.cos(2*np.pi*s_[0]/6) + 0.15*np.sin(2*np.pi*s_[1]/5) - 0.2*np.cos(2*np.pi*s_[2]/4) for s_ in sites]); p3 = np.exp(u3/2)
    Sm = []
    for j in range(3):
        M = np.zeros((N,N), complex)
        for x_ in sites: M[idx[x_], idx[sh(x_,j)]] += 1/(2j); M[idx[x_], idx[sh(x_,j,-1)]] -= 1/(2j)
        Sm.append(M)
    H0 = sum(np.kron(Sm[a], sig[a]) for a in range(3)); Pd = np.kron(np.diag(p3), np.eye(2)); Hw3 = Pd@H0@Pd
    w3, v3 = np.linalg.eigh(Hw3)
    for target in (0.4, 0.9):
        i = np.argmin(np.abs(w3 - target)); sel = np.abs(w3 - w3[i]) < 1e-9
        a = v3[:, i].reshape(N, 2); chi = p3[:,None]*a
        up3 = lambda f, a_: np.array([f[idx[sh(x_,a_)]] for x_ in sites]); dn3 = lambda f, a_: np.array([f[idx[sh(x_,a_,-1)]] for x_ in sites])
        S3 = lambda f, j: (up3(f,j) - dn3(f,j))/(2j)
        g = sum(np.einsum("st,xt->xs", sig[a_], S3(chi,a_)) for a_ in range(3))
        worst, fmax, wmax = 0, 0, 0
        for j in range(3):
            div = 0
            for a_ in range(3):
                Sj = S3(chi, j)
                J = 0.5*np.real(np.einsum("xs,st,xt->x", up3(chi,a_).conj(), sig[a_], Sj) + np.einsum("xs,st,xt->x", up3(Sj,a_).conj(), sig[a_], chi))
                div = div + J - dn3(J, a_)
            wj = up3(p3, j) - p3
            Cf = lambda f: 0.5*(wj[:,None]*up3(f,j) + dn3(wj,j)[:,None]*dn3(f,j))
            fj = np.real(np.einsum("xs,xs->x", Cf(a).conj(), g) + np.einsum("xs,xs->x", a.conj(), Cf(g)))
            e = np.real(np.einsum("xs,xs->x", chi.conj(), g)); du = (up3(u3,j) - dn3(u3,j))/2
            worst = max(worst, np.abs(div + fj).max()); fmax = max(fmax, np.abs(fj).max()); wmax = max(wmax, np.abs(e*du).max())
        print(f"     energy {w3[i]:+.5f} (degeneracy {sel.sum()}): max |div J + f| = {worst:.1e};  max |f| = {fmax:.2e};  max |e du| = {wmax:.2e}")
    print("     (hydrostatic balance holds site by site to rounding with a force density that is not zero; on this small torus the wave numbers are not small")
    print("      and f differs from the weight by factors of order cos k)")

    print("\n[W4] the ledger's identity for a third member, coefficients (c0, c1, c2, c3, c4) = (-2/5, 3, 1/7, -5/3, 1/2), through second order (exact symbolic algebra):")
    X = sp.symbols("x y z", real=True); eps = sp.symbols("epsilon", real=True)
    def tr(expr, m=3):
        expr = sp.expand(expr); return sum(expr.coeff(eps, k)*eps**k for k in range(m+1))
    B = sp.Matrix(3, 3, lambda j, a: sp.Function(f"B{j}{a}")(*X)); uu = sp.Function("u")(*X)
    I3 = sp.eye(3); A = eps*B; e = I3 + A
    einv = (I3 - A + A*A - A*A*A).applyfunc(tr)
    t1, t2, t3 = A.trace(), (A*A).trace(), (A*A*A).trace()
    dete = tr(1 + t1 + (t1**2 - t2)/2 + (t1**3 - 3*t1*t2 + 2*t3)/6)
    T = [[[sp.diff(e[j,b], X[a]) - sp.diff(e[j,a], X[b]) for b in range(3)] for a in range(3)] for j in range(3)]
    Tc = [[[tr(sum(einv[a,k]*einv[b,l]*T[j][a][b] for a in range(3) for b in range(3))) for l in range(3)] for k in range(3)] for j in range(3)]
    q1 = tr(sum(Tc[j][k][l]**2 for j in range(3) for k in range(3) for l in range(3)))
    q2 = tr(sum(Tc[j][k][l]*Tc[l][k][j] for j in range(3) for k in range(3) for l in range(3)))
    V = [tr(sum(Tc[k][k][l] for k in range(3))) for l in range(3)]
    q3 = tr(sum(v**2 for v in V))
    Vup = [tr(sum(einv[b,l]*V[l] for l in range(3))) for b in range(3)]
    dv = tr(sum(sp.diff(tr(dete*Vup[b]), X[b]) for b in range(3)))
    dens = tr(sp.Rational(-2,5)*dete + dete*(3*q1 + q2/7 - sp.Rational(5,3)*q3) + dv/2)
    lag = tr((1 + eps*uu + eps**2*uu**2/2 + eps**3*uu**3/6)*dens)
    def varder(L, f):
        out = sp.diff(L, f)
        for i in range(3):
            out -= sp.diff(sp.diff(L, sp.Derivative(f, X[i])), X[i])
            for k in range(i, 3):
                d2 = sp.Derivative(f, X[i], X[k]) if i != k else sp.Derivative(f, (X[i], 2))
                out += sp.diff(sp.diff(L, d2), X[i], X[k])
        return out
    Ef = sp.Matrix(3, 3, lambda j, a: tr(varder(lag, B[j,a])/eps, 2)); Uf = tr(varder(lag, uu)/eps, 2)
    ok = all(tr(sum(Ef[j,a]*sp.diff(e[j,a], X[b]) for j in range(3) for a in range(3)) - sum(sp.diff(Ef[j,a]*e[j,b], X[a]) for j in range(3) for a in range(3)) + Uf*eps*sp.diff(uu, X[b]), 2) == 0 for b in range(3))
    no_rates = all(tr(sum(Ef[j,a]*sp.diff(e[j,a], X[b]) for j in range(3) for a in range(3)) - sum(sp.diff(Ef[j,a]*e[j,b], X[a]) for j in range(3) for a in range(3)), 2) == 0 for b in range(3))
    print(f"     identity holds: {ok};  the same expression WITHOUT the rates' term vanishes: {no_rates}")
