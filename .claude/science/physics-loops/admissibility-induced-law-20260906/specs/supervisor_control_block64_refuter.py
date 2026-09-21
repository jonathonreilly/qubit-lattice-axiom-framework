#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 64 (machinery disjoint from the exact runner's).

W1  H[B] as a dense matrix on a 4x3x3 torus with a random strain: hermitian?  the derivative of <H[B]> in one bond's strain against the bond current.
W2  a relabelling as a change of the strain, B = d xi: the spectrum should move only at SECOND order in xi (H[d xi] = exp(iG) H exp(-iG) + O(xi^2)).
W3  uniqueness by another route: EXACT frames (no truncated expansions) with polynomial strains and a polynomial rotation field; the six basis
    densities' first-order change under the rotation, evaluated exactly at rational points; the null space of the resulting linear system.
W4  the blind density against sqrt(g) R for a finite, non-small polynomial strain at rational points (all orders, not second order)."""
import itertools
import numpy as np
import sympy as sp

sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
rng = np.random.default_rng(4)

def dense_walk(dims, strain):
    sites = list(itertools.product(*(range(d) for d in dims))); idx = {s:i for i,s in enumerate(sites)}; N = len(sites)
    sh = lambda x, a, s=1: tuple((x[i] + (s if i == a else 0)) % dims[i] for i in range(3))
    def S(j):
        M = np.zeros((N,N), complex)
        for x in sites: M[idx[x], idx[sh(x,j)]] += 1/(2j); M[idx[x], idx[sh(x,j,-1)]] -= 1/(2j)
        return M
    def C(a, w):
        M = np.zeros((N,N), complex)
        for x in sites: M[idx[x], idx[sh(x,a)]] += 0.5*w[x]; M[idx[x], idx[sh(x,a,-1)]] += 0.5*w[sh(x,a,-1)]
        return M
    Ss = [S(j) for j in range(3)]
    H = sum(np.kron(Ss[a], sig[a]) for a in range(3))
    for (a, j), w in strain.items():
        Ca = C(a, w); H = H + np.kron(0.5*(Ca@Ss[j] + Ss[j]@Ca), sig[a])
    return H, sites, idx, sh

if __name__ == "__main__":
    dims = (4,3,3)
    sites = list(itertools.product(*(range(d) for d in dims)))
    strain = {(a,j): {x: 0.1*rng.standard_normal() for x in sites} for a in range(3) for j in range(3)}
    H, sites, idx, sh = dense_walk(dims, strain)
    print(f"[W1] dense H[B] on a 4x3x3 torus, random strain of size 0.1: |H - H^dagger| = {np.abs(H-H.conj().T).max():.1e}")
    psi = rng.standard_normal(2*len(sites)) + 1j*rng.standard_normal(2*len(sites)); psi /= np.linalg.norm(psi)
    a0, j0, x0 = 2, 0, (1,2,1); h = 1e-6
    sp_, sm_ = {k: dict(v) for k,v in strain.items()}, {k: dict(v) for k,v in strain.items()}
    sp_[(a0,j0)][x0] += h; sm_[(a0,j0)][x0] -= h
    num = np.real(psi.conj()@(dense_walk(dims, sp_)[0] - dense_walk(dims, sm_)[0])@psi)/(2*h)
    P = psi.reshape(len(sites), 2)
    Sj = lambda f, j: np.array([(f[idx[sh(x,j)]] - f[idx[sh(x,j,-1)]])/(2j) for x in sites])
    SP = Sj(P, j0); up = lambda f, a: np.array([f[idx[sh(x,a)]] for x in sites])
    J = 0.5*np.real(np.einsum("xs,st,xt->x", up(P,a0).conj(), sig[a0], SP) + np.einsum("xs,st,xt->x", up(SP,a0).conj(), sig[a0], P))
    print(f"     d<H[B]>/dB on one bond: numerical {num:.8f}, bond current {J[idx[x0]]:.8f}")

    print("\n[W2] B = d xi: largest shift of an eigenvalue of H[B] against H, for xi of size s:")
    xi0 = [{x: rng.standard_normal() for x in sites} for _ in range(3)]
    base = np.linalg.eigvalsh(dense_walk(dims, {})[0])
    for s in (0.04, 0.02, 0.01):
        st = {(a,j): {x: s*(xi0[j][sh(x,a)] - xi0[j][x]) for x in sites} for a in range(3) for j in range(3)}
        ev = np.linalg.eigvalsh(dense_walk(dims, st)[0])
        print(f"     s = {s}: max shift {np.abs(ev-base).max():.3e}   (shift / s^2 = {np.abs(ev-base).max()/s**2:.3f})")
    gen = {(a,j): {x: 0.01*rng.standard_normal() for x in sites} for a in range(3) for j in range(3)}
    print(f"     a strain of size 0.01 that is NOT a relabelling: max shift {np.abs(np.linalg.eigvalsh(dense_walk(dims, gen)[0]) - base).max():.3e}  (first order)")

    print("\n[W3] exact frames, polynomial strain and rotation fields; change of each basis density under the rotation at rational points:")
    x, y, z, eta = sp.symbols("x y z eta"); X = (x, y, z)
    R3 = sp.Rational
    Bm = sp.Matrix([[R3(1,5)*x*y, R3(1,7)*z, R3(-1,6)*y*y], [R3(1,4)*z*x, R3(-1,5)*y, R3(1,9)*x], [R3(1,8)*y, R3(1,6)*x*z, R3(-1,7)*z*z]])
    omv = [R3(1,3)*y*z, R3(-1,4)*x*x, R3(1,5)*x + R3(1,6)*z*y]
    Om = sp.Matrix([[0, -omv[2], omv[1]], [omv[2], 0, -omv[0]], [-omv[1], omv[0], 0]])
    def basis(e):
        einv = e.inv(); dete = e.det()
        T = [[[sp.diff(e[j,b], X[a]) - sp.diff(e[j,a], X[b]) for b in range(3)] for a in range(3)] for j in range(3)]
        Tc = [[[sum(einv[a,k]*einv[b,l]*T[j][a][b] for a in range(3) for b in range(3)) for l in range(3)] for k in range(3)] for j in range(3)]
        T1 = sum(Tc[j][k][l]**2 for j in range(3) for k in range(3) for l in range(3))
        T2 = sum(Tc[j][k][l]*Tc[l][k][j] for j in range(3) for k in range(3) for l in range(3))
        V = [sum(Tc[k][k][l] for k in range(3)) for l in range(3)]
        T3 = sum(v**2 for v in V)
        Vup = [sum(einv[b,l]*V[l] for l in range(3)) for b in range(3)]
        div = sum(sp.diff(dete*Vup[b], X[b]) for b in range(3))
        odd = sum(sp.LeviCivita(j,k,l)*Tc[j][k][l] for j in range(3) for k in range(3) for l in range(3))
        return [dete, dete*T1, dete*T2, dete*T3, div, dete*odd]
    e_rot = (sp.eye(3) + eta*Om)*(sp.eye(3) + Bm)
    dens = basis(e_rot)
    changes = [sp.diff(d, eta).subs(eta, 0) for d in dens]
    pts = [(R3(1,2), R3(-1,3), R3(2,5)), (R3(-3,4), R3(1,5), R3(1,3)), (R3(2,3), R3(3,4), R3(-1,2)), (R3(1,7), R3(-2,3), R3(-3,5)), (R3(-1,2), R3(-1,2), R3(1,4)),
           (R3(4,5), R3(1,6), R3(2,7)), (R3(-2,5), R3(3,7), R3(-1,6)), (R3(3,8), R3(-5,6), R3(1,9))]
    M = sp.Matrix([[sp.nsimplify(c.subs(dict(zip(X, p)))) for c in changes] for p in pts])
    null = M.nullspace()
    print(f"     rank of the 8 x 6 system: {M.rank()}; null space dimension {len(null)}")
    for v in null:
        v = v/ (v[4] if v[4] != 0 else (v[0] if v[0] != 0 else 1))
        print("     null vector (c0, c1, c2, c3, c4, c5) =", [sp.nsimplify(t) for t in v])
    print("     (expected: the volume alone, and (0, -1/8, -1/4, 1/2, 1, 0): the blind combination; the rotation is exact in the strain here, not first order)")

    print("\n[W4] D* + sqrt(g) R at rational points for the finite polynomial strain above (exact frames and exact curvature):")
    e0 = sp.eye(3) + Bm; b0 = basis(e0)
    star = b0[1]/4 + b0[2]/2 - b0[3] - 2*b0[4]
    g = e0.T*e0; gi = g.inv()
    Gam = [[[sum(gi[i,l]*(sp.diff(g[l,k], X[j]) + sp.diff(g[l,j], X[k]) - sp.diff(g[j,k], X[l])) for l in range(3))/2 for k in range(3)] for j in range(3)] for i in range(3)]
    Ric = sp.zeros(3,3)
    for j in range(3):
        for k in range(3):
            Ric[j,k] = sum(sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k]) + sum(Gam[i][i][l]*Gam[l][j][k] - Gam[i][k][l]*Gam[l][j][i] for l in range(3)) for i in range(3))
    Rs = sum(gi[j,k]*Ric[j,k] for j in range(3) for k in range(3))
    tot = star + e0.det()*Rs
    for p in pts[:4]:
        print(f"     at {p}: D* = {float(star.subs(dict(zip(X,p)))):+.6f},  D* + sqrt(g) R = {sp.nsimplify(tot.subs(dict(zip(X,p))))}")
