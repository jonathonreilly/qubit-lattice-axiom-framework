#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 74 (floating point; vector operations on a two-dimensional torus; machinery disjoint from the
exact runner's).

A two-dimensional slice of the walk, H = sigma_1 S_x + sigma_2 S_y, on a 256 x 256 torus. Packets of positive energy of species (0, 0) and (1, 0),
moving obliquely (own wave number q = (0.5, 0.3)), Gaussian envelope of width 24.
W1  the three responses site by site, relative to the two-step current K: the ratios Theta_a^j/K_a^j and J_a^j/K_a^j where |K| is not small,
    for the four components (a, j), against D_a D_j and D_j (times the lattice factors of a packet at wave number q).
W2  pairings with a smooth displacement, sum_x (d_a xi_j)(x) R_a^j(x), R = Theta, J, K: a stretch (xi_x depends on x), the two shears
    (xi_x depends on y; xi_y depends on x), a stretch along y: the ratios to the pairing with K.
"""
import numpy as np

L = 256
X, Y = np.meshgrid(np.arange(L), np.arange(L), indexing="ij")
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]])]


def sh(f, axis, step):
    return np.roll(f, -step, axis=axis)                                  # f(x + step e_axis)


def S(f, j): return (sh(f, j, 1) - sh(f, j, -1))/(2j)
def P(f, j): return (sh(f, j, 2) - sh(f, j, -2))/(4j)


def sandwich(left, a, right):
    return np.einsum("xyi,ij,xyj->xy", left.conj(), sig[a], right)


def responses(psi):
    out = {}
    for a in range(2):
        for j in range(2):
            s, p = S(psi, j), P(psi, j)
            theta = np.real(sandwich(psi, a, s))
            bond2 = 0.5*np.real(sandwich(sh(psi, a, 1), a, s) + sandwich(sh(s, a, 1), a, psi))
            bond3 = 0.5*np.real(sandwich(sh(psi, a, 1), a, p) + sandwich(sh(p, a, 1), a, psi))
            out[(a, j)] = (theta, bond2, bond3)
    return out


def packet(species, q=(0.5, 0.3), width=24.0):
    k = np.array([np.pi*species[0] + q[0], np.pi*species[1] + q[1]])
    s = np.sin(k); eps = np.hypot(*s)
    spinor = np.array([1.0, (s[0] + 1j*s[1])/eps])/np.sqrt(2)           # H(k) spinor = +eps spinor
    env = np.exp(-((X - L/2)**2 + (Y - L/2)**2)/(4*width**2))*np.exp(1j*(k[0]*X + k[1]*Y))
    psi = env[..., None]*spinor
    return psi/np.linalg.norm(psi), k


if __name__ == "__main__":
    q = (0.5, 0.3)
    names = {0: "x", 1: "y"}
    for species in ((0, 0), (1, 0)):
        psi, k = packet(species, q)
        D = [(-1)**species[0], (-1)**species[1]]
        res = responses(psi)
        print(f"species {species}, own wave number q = {q}, D = {D}:")
        print("  [W1] site by site, where |K| > 0.2 max|K|: ratios to the two-step current (for a plane wave: Theta/K = D_a D_j/(cos q_a cos q_j), J/K = D_j/cos q_j)")
        for (a, j), (theta, b2, b3) in res.items():
            mask = np.abs(b3) > 0.2*np.abs(b3).max()
            r1, r2 = theta[mask]/b3[mask], b2[mask]/b3[mask]
            pred_j = D[j]/np.cos(q[j])
            print(f"       (a, j) = ({names[a]}, {names[j]}): Theta/K in [{r1.min():+.3f}, {r1.max():+.3f}], J/K in [{r2.min():+.3f}, {r2.max():+.3f}]; plane wave: {D[a]*D[j]/(np.cos(q[a])*np.cos(q[j])):+.3f} and {pred_j:+.3f}")
        print("  [W2] pairings sum_x (d_a xi_j) R_a^j with xi_j = sin(2 pi x_a/L) (one Fourier mode of displacement), ratios to the pairing with K:")
        for a in range(2):
            for j in range(2):
                coord = X if a == 0 else Y
                xi = np.sin(2*np.pi*(coord - L/2 + 17)/L)
                dxi = sh(xi, a, 1) - xi
                theta, b2, b3 = res[(a, j)]
                dxi_site = 0.5*(dxi + sh(dxi, a, -1))                     # the site stress is paired with the centred difference
                pk = (dxi*b3).sum()
                kind = "stretch" if a == j else "shear"
                print(f"       {kind:7s} d_{names[a]} xi_{names[j]}: Theta/K = {(dxi_site*theta).sum()/pk:+.4f}, J/K = {(dxi*b2).sum()/pk:+.4f}")
