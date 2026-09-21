#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 62 (floating point; machinery disjoint from the exact runner's).

W1  the walk with a uniform TILTED coin frame as a real-space matrix on a 6x6x6 torus: its spectrum against +-sqrt(g^ij sin k_i sin k_j).
W2  the group velocity in a sheared frame: numerical derivative of the real-space spectrum's branch against g^ij sin k_j cos k_i / energy.
W3  stationary superpositions of the identity-frame walk: is the symmetric frame response divergence-free on the lattice?  (the member of T3 asks for
    it.)  The divergence against the box size at fixed mode numbers, and the bond current of the momentum density, which IS conserved exactly.
W4  the two travelling disturbances by a numerical constrained eigenproblem at random directions (rotation-invariant kinetic term).
W5  static responses to divergence-free stresses at 300 random directions, many near coordinate planes: largest entry x p^2 / |stress|.
W6  relabelling invariance of R_1 in REAL space with the staggered placement (h_jj on sites, h_ij on faces, xi_j on bonds): random integer xi."""
import numpy as np
import itertools

sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
rng = np.random.default_rng(5)

def walk_matrix(L, E):
    """H = sum_j (E^j . sigma) S_j on an L^3 torus, uniform frame E[a, j]."""
    N = L**3; idx = lambda x: ((x[0]%L)*L + x[1]%L)*L + x[2]%L
    H = np.zeros((2*N, 2*N), complex)
    for x in itertools.product(range(L), repeat=3):
        for j in range(3):
            M = sum(E[a, j]*sig[a] for a in range(3))
            up = list(x); up[j] += 1; dn = list(x); dn[j] -= 1
            for s in range(2):
                for t in range(2):
                    H[2*idx(x)+s, 2*idx(up)+t] += M[s, t]/(2j)
                    H[2*idx(x)+s, 2*idx(dn)+t] -= M[s, t]/(2j)
    return H

if __name__ == "__main__":
    E = np.eye(3) + 0.3*rng.standard_normal((3,3)); g = E.T@E
    L = 6; H = walk_matrix(L, E)
    print(f"[W1] tilted frame, 6^3 torus: |H - H^dagger| = {np.abs(H-H.conj().T).max():.1e}")
    ev = np.sort(np.linalg.eigvalsh(H))
    pred = []
    for n in itertools.product(range(L), repeat=3):
        s = np.sin(2*np.pi*np.array(n)/L); e = np.sqrt(max(s@g@s, 0.0)); pred += [e, -e]
    print(f"     spectrum against +-sqrt(g^ij s_i s_j): max difference {np.abs(ev-np.sort(pred)).max():.2e}  (off-diagonal g: {g[0,1]:+.3f}, {g[0,2]:+.3f}, {g[1,2]:+.3f})")

    print("\n[W2] group velocity in the sheared frame at k = (0.4, 0.7, -0.3): numerical gradient of the energy against g^ij s_j cos k_i / energy:")
    k = np.array([0.4, 0.7, -0.3]); en = lambda q: np.sqrt(np.sin(q)@g@np.sin(q))
    num = np.array([(en(k+h)-en(k-h))/2e-6 for h in 1e-6*np.eye(3)]); ana = np.cos(k)*(g@np.sin(k))/en(k)
    print(f"     numerical {num.round(6)}, formula {ana.round(6)}; in the identity frame it would be {(np.cos(k)*np.sin(k)/np.linalg.norm(np.sin(k))).round(6)}: the tilt turns the walker")

    print("\n[W3] stationary superpositions (identity frame), two plane waves of equal energy, mode numbers (1,2,3) and (3,1,2):")
    def run(L):
        u = 2*np.pi/L
        def eigv(kk):
            s = np.sin(kk); w, v = np.linalg.eigh(sum(s[j]*sig[j] for j in range(3))); return v[:,1]
        def field(kk, sp_):
            x = np.arange(L); X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
            return np.exp(1j*(kk[0]*X+kk[1]*Y+kk[2]*Z))[...,None]*sp_[None,None,None,:]
        S = lambda psi, j: (np.roll(psi,-1,axis=j)-np.roll(psi,1,axis=j))/(2j)
        ka, kb = u*np.array((1,2,3)), u*np.array((3,1,2))
        psi = field(ka, eigv(ka)) + 0.7*np.exp(0.3j)*field(kb, eigv(kb))
        Th = np.zeros((3,3,L,L,L))
        for j in range(3):
            Sp = S(psi, j)
            for a in range(3): Th[a,j] = np.real(np.einsum("xyzs,st,xyzt->xyz", psi.conj(), sig[a], Sp))
        sym = 0.5*(Th + Th.transpose(1,0,2,3,4)); osc = np.abs(sym - sym.mean(axis=(2,3,4), keepdims=True)).max()
        div = max(np.abs(sum((np.roll(sym[a,j],-1,axis=a)-np.roll(sym[a,j],1,axis=a))/2 for a in range(3))).max() for j in range(3))
        worst = 0
        for j in range(3):
            Sp = S(psi, j); tot = 0
            for a in range(3):
                J = 0.5*np.real(np.einsum("xyzs,st,xyzt->xyz", np.roll(psi,-1,axis=a).conj(), sig[a], Sp) + np.einsum("xyzs,st,xyzt->xyz", np.roll(Sp,-1,axis=a).conj(), sig[a], psi))
                tot = tot + J - np.roll(J,1,axis=a)
            worst = max(worst, np.abs(tot).max())
        return osc, div, worst
    for L in (12, 24, 48):
        osc, div, worst = run(L)
        print(f"     L = {L:2d}: oscillating stress {osc:.3f}; divergence of its symmetric part {div:.2e} (relative {div/osc:.1e}, x L^3/12^3 = {div/osc*L**3/12**3:.3f}); bond current of the momentum density {worst:.1e}")
    print("     (the frame response is divergence-free only up to terms of second order in the wave vector; what is conserved exactly is a bond current)")

    print("\n[W4] two travelling disturbances, alpha = 1/4, beta = 1, K = 1: generalized eigenvalues X/p^2 at random directions (constraint imposed by projection):")
    pairs = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
    def forms(p):
        def r2(h):
            Hm = np.zeros((3,3))
            for v,(i,j) in zip(h, pairs): Hm[i,j] = Hm[j,i] = v
            psq = p@p; tr = np.trace(Hm); d = p@Hm
            return -0.25*psq*np.sum(Hm*Hm) + 0.5*d@d - 0.5*(d@p)*tr + 0.25*psq*tr**2
        def kin(h, al=0.25, be=1.0):
            Hm = np.zeros((3,3))
            for v,(i,j) in zip(h, pairs): Hm[i,j] = Hm[j,i] = v
            return al*np.sum(Hm*Hm) + be*np.trace(Hm)**2
        I = np.eye(6)
        hess = lambda f: np.array([[(f(I[a]+I[b]) - f(I[a]) - f(I[b]) + f(0*I[a])) for b in range(6)] for a in range(6)])
        A = -hess(r2)*(-1)                      # V = -(u R1 + R2): Hessian of V in h is -Hess(R2)
        A = -hess(r2)
        Kn = hess(kin)
        c = np.array([-(p[i]*p[j]*(1 if i == j else 2) - (p@p if i == j else 0)) for (i,j) in pairs])   # dR1/dh
        return A, Kn, c
    for _ in range(4):
        p = rng.standard_normal(3); A, Kn, c = forms(p)
        Q = np.linalg.svd(c.reshape(1,6))[2][1:].T
        w = np.linalg.eigvals(np.linalg.solve(Q.T@Kn@Q, Q.T@A@Q)).real
        print(f"     p = {p.round(3)}: X/p^2 = {np.sort(w/(p@p)).round(6)}")
    print("     (two values equal to 1/(4 alpha) = 1, the rest zero)")

    print("\n[W5] static responses to divergence-free stresses at 300 random directions (100 of them with one component below 1/100):")
    worst = 0
    for n in range(300):
        p = rng.standard_normal(3)
        if n < 100: p[rng.integers(3)] *= 1e-3
        A, Kn, c = forms(p)
        M = np.zeros((7,7)); M[:6,:6] = A; M[:6,6] = -c; M[6,:6] = -c       # V = -(u R1 + R2)
        v = np.cross(p, rng.standard_normal(3)); Th = np.outer(v, v)
        b = np.array([Th[0,0]/2, Th[1,1]/2, Th[2,2]/2, Th[0,1], Th[0,2], Th[1,2], 0.0])
        x = np.linalg.lstsq(M, b, rcond=None)[0]
        resid = np.abs(M@x-b).max()
        worst = max(worst, np.abs(x).max()*(p@p)/np.abs(Th).max())
        assert resid < 1e-8*max(1, np.abs(b).max()), resid
    print(f"     largest |response| x p^2 / |stress| = {worst:.3f}: bounded, direction by direction (block 61's three-length response grows like p_1^2/(p_2^2 p_3^2))")

    print("\n[W6] relabelling invariance of R_1 in real space, staggered placement, 5x4x3 torus, random integer xi on the bonds:")
    dims = (5,4,3); sites = list(itertools.product(*(range(d) for d in dims)))
    sh = lambda x, j, s: tuple((x[i] + (s if i == j else 0)) % dims[i] for i in range(3))
    xi = [{x: int(rng.integers(-5, 6)) for x in sites} for _ in range(3)]          # xi_j on the bond from x along j
    hd = [{x: 2*(xi[j][x] - xi[j][sh(x,j,-1)]) for x in sites} for j in range(3)]     # h_jj at the site x
    ho = {}
    for (i,j) in ((0,1),(0,2),(1,2)):                                                # h_ij on the face at x + e_i/2 + e_j/2
        ho[(i,j)] = {x: (xi[j][sh(x,i,1)] - xi[j][x]) + (xi[i][sh(x,j,1)] - xi[i][x]) for x in sites}
    worst = 0
    for x in sites:
        tr = lambda y: sum(hd[j][y] for j in range(3))
        lap_tr = sum(tr(sh(x,j,1)) + tr(sh(x,j,-1)) - 2*tr(x) for j in range(3))
        dd = sum(hd[j][sh(x,j,1)] + hd[j][sh(x,j,-1)] - 2*hd[j][x] for j in range(3))
        for (i,j) in ((0,1),(0,2),(1,2)):
            f = ho[(i,j)]
            dd += 2*(f[x] - f[sh(x,i,-1)] - f[sh(x,j,-1)] + f[sh(sh(x,i,-1),j,-1)])
        worst = max(worst, abs(dd - lap_tr))
    print(f"     max |d_i d_j h_ij - Lap h| over all sites for a pure relabelling: {worst}  (integers: exactly zero)")
