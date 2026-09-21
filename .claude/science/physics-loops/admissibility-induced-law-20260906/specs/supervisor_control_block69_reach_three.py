#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 69 (floating point; real space; machinery disjoint from the exact runner's).

Block 68's control with a third coupling added: (c) the relabelling generated with the two-step momentum P_x = S_x C_x (reach three),
H = sigma_1 [S_x + (1/2){C_x[b], P_x}] + sigma_2 S_y.

A two-dimensional slice (x, y) of the walk, H = sigma_1 S_x + sigma_2 S_y, on a 160 x 128 torus, with a stretch of the x-bonds that varies with y,
b(y) = b0 sin(2 pi y/Ly), carried (a) by the nearest-neighbour frame, H = (1/2){1 + b, S_x} sigma_1 + sigma_2 S_y (b on the sites), and (b) by the
relabelling's second-neighbour coupling, H = sigma_1 [S_x + (1/2){C_x[b], S_x}] + sigma_2 S_y (b on the x-bonds).
Packets of species (0, 0) and (1, 0), positive energy, moving along +x through the place where b has its largest gradient.
W1  the sideways displacement of each packet (part odd in b0) after time T against the rays' -+ (1/2) b' T^2 (times |s_x|/energy factors).
W2  the speeds along x in a UNIFORM stretch for the two species and the two couplings, from the real-space evolution.
W3  (dense matrices, 5 x 6 x 7 torus) eigenstates of the three-dimensional walk: the lattice divergence of the two-step current K_a^j at every site, and the
    local conservation law d/dt Re psi^dagger P_j psi = -(div K^j) at every site for a state in motion."""
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply

Lx, Ly = 160, 128
sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]])]
X, Y = np.meshgrid(np.arange(Lx), np.arange(Ly), indexing="ij")
idx = (X*Ly + Y)

def shift_op(axis, step):
    Xs, Ys = (X + (step if axis == 0 else 0)) % Lx, (Y + (step if axis == 1 else 0)) % Ly
    return sps.csr_matrix((np.ones(Lx*Ly), (idx.ravel(), (Xs*Ly + Ys).ravel())), shape=(Lx*Ly, Lx*Ly))      # (T psi)(x) = psi(x + step e)

Tx, Ty = shift_op(0, 1), shift_op(1, 1)
Sx, Sy = (Tx - Tx.T)/(2j), (Ty - Ty.T)/(2j)
Cx_plain = (Tx + Tx.T)/2

def generator(bfield, coupling):
    D = sps.diags(bfield.ravel())
    if coupling == "frame":
        hx = Sx + 0.5*(D@Sx + Sx@D)
    elif coupling == "strain":
        Cb = 0.5*(D@Tx + Tx.T@D)                     # symmetric hop weighted by b on the bond from x to x + e_x (b depends on y only, so the bond's b is its sites')
        hx = Sx + 0.5*(Cb@Sx + Sx@Cb)
    else:
        Cb = 0.5*(D@Tx + Tx.T@D)
        Px = (Tx@Tx - Tx.T@Tx.T)/(4j)                # the two-step momentum, symbol (1/2) sin 2k
        hx = Sx + 0.5*(Cb@Px + Px@Cb)
    return sps.kron(hx, sig[0]) + sps.kron(Sy, sig[1])

def packet(species, q=0.6, x0=30, y0=0.0, width=9.0):
    kx = q if species == 0 else np.pi - q            # species (1, 0): k_x = pi - q, so that sin k_x = sin q > 0 and the packet moves along... see below
    s = np.array([np.sin(kx), 0.0]); H2 = s[0]*sig[0]; w, v = np.linalg.eigh(H2)
    branch = 1 if np.cos(kx) > 0 else 0              # choose the branch whose group velocity along x, sin k cos k / energy x (sign of branch), is positive
    chi = v[:, branch]
    dy = ((Y - y0 + Ly/2) % Ly) - Ly/2
    env = np.exp(-((X - x0)**2 + dy**2)/(2*width**2))
    psi = (env*np.exp(1j*kx*X))[..., None]*chi[None, None, :]
    return (psi/np.linalg.norm(psi)).reshape(-1)

def centre(v):
    p = (np.abs(v.reshape(Lx, Ly, 2))**2).sum(-1)
    dy = ((Y + Ly/2) % Ly) - Ly/2
    ang = np.angle(np.sum(p*np.exp(2j*np.pi*X/Lx)))
    return (ang % (2*np.pi))*Lx/(2*np.pi), np.sum(p*dy)

if __name__ == "__main__":
    b0, T = 0.2, 60.0
    bprime = b0*2*np.pi/Ly
    print(f"[W1] stretch of the x-bonds b(y) = {b0} sin(2 pi y/{Ly}) (gradient {bprime:.5f} at y = 0), T = {T}: sideways displacement, part odd in b0:")
    for coupling in ("frame", "strain", "reach3"):
        for species in (0, 1):
            ys = []
            for sign in (+1, -1):
                Hm = generator(sign*b0*np.sin(2*np.pi*Y/Ly), coupling)
                v = expm_multiply(-1j*T*Hm, packet(species))
                ys.append(centre(v)[1])
            odd = 0.5*(ys[0] - ys[1])
            print(f"     coupling {coupling:6s}, species ({species}, 0): {odd:+.3f}")
    print(f"     rays at the start: a packet that sees the stretch as 1 + b is pushed sideways at -b' per unit time: -(1/2) b' T^2 = {-0.5*bprime*T**2:+.3f} if the gradient stayed at its largest value (it falls as the packet drifts: cos(2 pi 15/128) = {np.cos(2*np.pi*15/128):.2f}); one that sees 1 - b is pushed the other way; under the strain coupling the stretch enters through cos k, which lowers both by cos q = {np.cos(0.6):.3f}")

    print("\n[W2] uniform stretch b = 0.2: distance travelled along x in T = 40 (no stretch: cos q x 40 = %.3f):" % (np.cos(0.6)*40))
    for coupling in ("frame", "strain", "reach3"):
        for species in (0, 1):
            Hm = generator(0.2*np.ones((Lx, Ly)), coupling); H0 = generator(np.zeros((Lx, Ly)), coupling)
            x1 = centre(expm_multiply(-1j*40.0*Hm, packet(species)))[0]; x0 = centre(packet(species))[0]
            print(f"     coupling {coupling:6s}, species ({species}, 0): {x1 - x0:+.3f}")
    q0 = 0.6
    print(f"     (group velocities x 40: frame (1 + b) cos q = {1.2*np.cos(q0)*40:.2f} for both species; strain cos q +- b cos 2q = {(np.cos(q0)+0.2*np.cos(2*q0))*40:.2f}, {(np.cos(q0)-0.2*np.cos(2*q0))*40:.2f}; reach three d/dq[sin q (1 + b cos^2 q)] = {(np.cos(q0)*(1+0.2*np.cos(q0)**2) - 0.4*np.sin(q0)**2*np.cos(q0))*40:.2f} for BOTH species; the packets' spread in wave number lowers all of them by one to two per cent)")

    # W3: dense three-dimensional check of T3(c), site by site
    rng = np.random.default_rng(69)
    dims = (5, 6, 7); n = int(np.prod(dims))
    grid = np.indices(dims).reshape(3, -1)
    def T3d(axis, step=1):
        g = grid.copy(); g[axis] = (g[axis] + step) % dims[axis]
        M = np.zeros((n, n)); M[np.arange(n), np.ravel_multi_index(g, dims)] = 1.0
        return M                                         # (T psi)(x) = psi(x + step e)
    sig3 = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
    Ts = [T3d(a) for a in range(3)]
    S3 = [(t - t.T)/(2j) for t in Ts]; P3 = [(t@t - t.T@t.T)/(4j) for t in Ts]
    H3 = sum(np.kron(S3[a], sig3[a]) for a in range(3))
    evals, evecs = np.linalg.eigh(H3)
    def K_div(psi, j):
        """site-resolved lattice divergence of K_a^j: sum_a [K_a^j(x -> x+e_a) - K_a^j(x-e_a -> x)]"""
        ps = psi.reshape(n, 2); Pp = (np.kron(P3[j], np.eye(2))@psi).reshape(n, 2)
        div = np.zeros(n)
        for a in range(3):
            ps_up = Ts[a]@ps; Pp_up = Ts[a]@Pp           # values at x + e_a
            Kb = 0.5*np.real(np.einsum("xi,ij,xj->x", ps_up.conj(), sig3[a], Pp) + np.einsum("xi,ij,xj->x", Pp_up.conj(), sig3[a], ps))
            div += Kb - Ts[a].T@Kb
        return div
    worst = 0.0; biggest = 0.0
    for col in rng.choice(2*n, size=12, replace=False):
        # a generic vector inside one (degenerate) eigenspace is still stationary
        mask = np.abs(evals - evals[col]) < 1e-9
        v = evecs[:, mask]@(rng.normal(size=mask.sum()) + 1j*rng.normal(size=mask.sum())); v /= np.linalg.norm(v)
        for j in range(3):
            d = K_div(v, j); worst = max(worst, np.abs(d).max())
            ps = v.reshape(n, 2); Pp = (np.kron(P3[j], np.eye(2))@v).reshape(n, 2)
            for a in range(3):
                biggest = max(biggest, np.abs(np.real(np.einsum("xi,ij,xj->x", (Ts[a]@ps).conj(), sig3[a], Pp))).max())
    print(f"\n[W3] 5x6x7 torus, 12 stationary states drawn inside eigenspaces of the walk, j = 1, 2, 3: largest |div K^j| at any site = {worst:.2e} (largest bond term of K itself {biggest:.2e})")
    psi = rng.normal(size=2*n) + 1j*rng.normal(size=2*n); psi /= np.linalg.norm(psi)
    dpsi = -1j*H3@psi; worst_law = 0.0; size = 0.0
    for j in range(3):
        Pm = np.kron(P3[j], np.eye(2))
        rate = np.real(np.einsum("xi,xi->x", dpsi.reshape(n,2).conj(), (Pm@psi).reshape(n,2)) + np.einsum("xi,xi->x", psi.reshape(n,2).conj(), (Pm@dpsi).reshape(n,2)))
        worst_law = max(worst_law, np.abs(rate + K_div(psi, j)).max()); size = max(size, np.abs(rate).max())
    print(f"     a random state in motion: largest |d/dt Re psi^dagger P_j psi + div K^j| at any site = {worst_law:.2e} (largest rate {size:.2e})")
