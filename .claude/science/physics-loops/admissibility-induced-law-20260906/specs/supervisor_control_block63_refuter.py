#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 63 (floating point; machinery disjoint from the exact runner's).

W1  the four identities on a random COMPLEX state of a 6x5x4 torus (unequal sides): continuity with the bond current; i[H, G_xi]; the bond current
    against the bond average of the site response; the torque on the coin.
W2  a pair of plane waves of equal energy on a 24^3 torus: the Fourier components of J and Theta at q = k - k': is J = exp(i q_a/2) cos(kbar_a) Theta?
W3  is there a symbol depending on q ALONE whose law holds for all equal-energy pairs with that q?  Two pairs with the same q and different mean wave
    vectors: the law's symbol is unique up to scale for each pair (the real vector orthogonal to Re M and Im M); compare the two.
W4  block 62's executed defect explained: sum_a p_a(q) M_a = sum_a p_a(q)(1 - cos kbar_a) M_a exactly, since sum_a p_a cos(kbar_a) M_a = 0."""
import numpy as np
rng = np.random.default_rng(9)
sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
up = lambda f, a: np.roll(f, -1, axis=a); dn = lambda f, a: np.roll(f, 1, axis=a)
S = lambda f, j: (up(f,j) - dn(f,j))/(2j)
sg = lambda a, f: np.einsum("st,...t->...s", sig[a], f)
Hm = lambda f: sum(sg(a, S(f,a)) for a in range(3))
dot = lambda f, g: np.einsum("...s,...s->...", f.conj(), g)

if __name__ == "__main__":
    shape = (6,5,4)
    psi = rng.standard_normal(shape+(2,)) + 1j*rng.standard_normal(shape+(2,)); pd = -1j*Hm(psi)
    worst = 0
    for j in range(3):
        dpi = np.real(dot(pd, S(psi,j)) + dot(psi, S(pd,j))); div = 0
        for a in range(3):
            J = 0.5*np.real(dot(up(psi,a), sg(a,S(psi,j))) + dot(up(S(psi,j),a), sg(a,psi))); div = div + J - dn(J,a)
        worst = max(worst, np.abs(dpi+div).max())
    print(f"[W1] continuity with the bond current, random complex state, 6x5x4 torus: {worst:.1e}")
    xi = [rng.standard_normal(shape) for _ in range(3)]
    Gx = lambda f: sum(0.5*(xi[j][...,None]*S(f,j) + S(xi[j][...,None]*f, j)) for j in range(3))
    lhs = 1j*(Hm(Gx(psi)) - Gx(Hm(psi))); rhs = 0
    for a in range(3):
        for j in range(3):
            w = up(xi[j],a) - xi[j]; C = lambda f: 0.5*(w[...,None]*up(f,a) + dn(w,a)[...,None]*dn(f,a))
            rhs = rhs + sg(a, 0.5*(C(S(psi,j)) + S(C(psi),j)))
    print(f"     i[H, G_xi] against sigma_a (1/2){{(d_a xi_j) C_a, S_j}}: {np.abs(lhs-rhs).max():.1e}")
    worst = 0
    for a in range(3):
        for j in range(3):
            Th = np.real(dot(psi, sg(a,S(psi,j)))); J = 0.5*np.real(dot(up(psi,a), sg(a,S(psi,j))) + dot(up(S(psi,j),a), sg(a,psi)))
            corr = 0.5*np.real(dot(up(psi,a)-psi, sg(a, up(S(psi,j),a)-S(psi,j))))
            worst = max(worst, np.abs(J - 0.5*(Th+up(Th,a)) + corr).max())
    print(f"     bond current against the bond average of Theta minus the two-difference term: {worst:.1e}")
    eps = np.zeros((3,3,3)); eps[0,1,2]=eps[1,2,0]=eps[2,0,1]=1; eps[0,2,1]=eps[2,1,0]=eps[1,0,2]=-1
    Theta = [[np.real(dot(psi, sg(a,S(psi,j)))) for j in range(3)] for a in range(3)]
    worst = 0
    for c in range(3):
        dS = 2*np.real(dot(pd, sg(c,psi))); tor = 2*sum(eps[c,a,d]*Theta[d][a] for a in range(3) for d in range(3)); b = np.real(dot(psi, up(psi,c)))
        worst = max(worst, np.abs(dS - tor + (b - dn(b,c))).max())
    print(f"     torque on the coin: {worst:.1e}")

    print("\n[W2] plane-wave pair on a 24^3 torus, mode numbers (1,2,3) and (3,1,2): J_a^j(q)/Theta_a^j(q) against exp(i q_a/2) cos(kbar_a):")
    L = 24; u = 2*np.pi/L; ka, kb = u*np.array((1,2,3)), u*np.array((3,1,2))
    def eigv(k):
        s = np.sin(k); w, v = np.linalg.eigh(sum(s[j]*sig[j] for j in range(3))); return v[:,1]
    x = np.arange(L); X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    fld = lambda k, sp_: np.exp(1j*(k[0]*X+k[1]*Y+k[2]*Z))[...,None]*sp_
    psi = fld(ka, eigv(ka)) + 0.7*np.exp(0.3j)*fld(kb, eigv(kb))
    qn = (1-3, 2-1, 3-2); kbar = (ka+kb)/2; q = ka-kb
    worst = 0
    for a in range(3):
        for j in range(3):
            Th = np.real(dot(psi, sg(a,S(psi,j)))); J = 0.5*np.real(dot(up(psi,a), sg(a,S(psi,j))) + dot(up(S(psi,j),a), sg(a,psi)))
            r = np.fft.fftn(J)[qn]/np.fft.fftn(Th)[qn]
            worst = max(worst, abs(r - np.exp(1j*q[a]/2)*np.cos(kbar[a])))
    print(f"     largest deviation over the nine (a, j): {worst:.1e}   (cos kbar = {np.cos(kbar).round(4)})")

    print("\n[W3] two equal-energy pairs with the SAME q = (0.5, -0.3, 0.9) and different mean wave vectors; the law's symbol (unique up to scale) for each:")
    q = np.array([0.5, -0.3, 0.9])
    def pair(k1, k2):
        k3 = 0.5*np.arcsin(-(np.sin(2*k1)*np.sin(q[0]) + np.sin(2*k2)*np.sin(q[1]))/np.sin(q[2]))      # equal energies: sum_a sin(2 kbar_a) sin(q_a) = 0
        kbar = np.array([k1,k2,k3]); k, kp = kbar+q/2, kbar-q/2
        M = np.array([eigv(kp).conj()@sig[a]@eigv(k) for a in range(3)])
        sym = np.cross(M.real, M.imag); sym /= np.linalg.norm(sym)
        true = np.sin(k)-np.sin(kp); true /= np.linalg.norm(true)
        return kbar, sym*np.sign(sym@true), true, abs(np.linalg.norm(np.sin(k))-np.linalg.norm(np.sin(kp)))
    pq = 2*np.sin(q/2); pq /= np.linalg.norm(pq)
    res = [pair(0.3, 0.9), pair(1.1, -0.4)]
    for kbar, sym, true, de in res:
        print(f"     kbar = {kbar.round(4)} (energy difference {de:.0e}): symbol from M = {sym.round(5)}; sin k - sin k' normalised = {true.round(5)}; angle to p(q) = {np.degrees(np.arccos(abs(sym@pq))):.2f} deg")
    print(f"     angle between the two pairs' symbols: {np.degrees(np.arccos(abs(res[0][1]@res[1][1]))):.2f} deg: no symbol depending on q alone serves both")

    print("\n[W4] block 62's defect: sum_a p_a M_a against sum_a p_a (1 - cos kbar_a) M_a, mode numbers (1,2,3), (3,1,2):")
    for L in (12, 24, 48):
        u = 2*np.pi/L; ka, kb = u*np.array((1,2,3)), u*np.array((3,1,2)); q = ka-kb; kbar = (ka+kb)/2
        M = np.array([eigv(kb).conj()@sig[a]@eigv(ka) for a in range(3)]); p = 2*np.sin(q/2)
        print(f"     L = {L}: |sum p M| = {abs(p@M):.3e}; |sum p (1 - cos kbar) M| = {abs((p*(1-np.cos(kbar)))@M):.3e}; |sum p cos(kbar) M| = {abs((p*np.cos(kbar))@M):.1e}; ratio to |p||M| = {abs(p@M)/(np.linalg.norm(p)*np.linalg.norm(M)):.2e}")
