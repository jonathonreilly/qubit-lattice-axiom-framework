#!/usr/bin/env python3
"""Supervisor control and refuting pass, block 71 (floating point; machinery disjoint from the exact runner's).

W1  THE CHASE.  Block 55's control (two walkers on a ring sourcing the rate field that times them; reduced walk H(m) = m sigma_x + sigma_z D,
    H_w = sqrt(w) H sqrt(w); weak-field law 2u_z - u_{z+1} - u_{z-1} = -Gam (e_z - mean e), e the ENERGY density) with walker B taken from the
    NEGATIVE-energy branch. Reported: the energies, the displacement of each packet, the change of each wave vector (matched pulls: the two
    changes cancel), the ledger. For comparison the same run with both walkers of positive energy.
W2  A NEGATIVE BODY AT REST in block 60's curvature member on a box (interior 9x9x9, walls at w = l = 1): Newton's method on the two field
    equations from empty space, continuation in m downwards, against the closed forms w_0 = (1 + g_0 m/(2K))^(-1/2), chi_0 = (1 + r)/2; the
    smallest eigenvalue of -Delta + Q/chi on the way to the bound m = -2K/g_0.
"""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply


def ring(n, u, m):
    rt = np.exp(0.5 * u)
    rows, cols, vals = [], [], []
    for s1, s2 in ((0, 1), (1, 0)):
        rows.append(2 * np.arange(n) + s1); cols.append(2 * np.arange(n) + s2); vals.append(rt * rt * m + 0j)
    up, dn = (np.arange(n) + 1) % n, np.arange(n)
    amp = rt[up] * rt[dn]
    for s, c in ((0, 1.0), (1, -1.0)):
        rows.append(2 * up + s); cols.append(2 * dn + s); vals.append(0.5j * amp * c)
        rows.append(2 * dn + s); cols.append(2 * up + s); vals.append(-0.5j * amp * c)
    return coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(2 * n, 2 * n)).tocsr()


def packet(n, z0, width, m, k0=0.0, branch=1):
    k = 2 * np.pi * np.fft.fftfreq(n)
    gk = np.exp(-(np.angle(np.exp(1j * (k - k0))) ** 2) * width ** 2) * np.exp(-1j * k * z0)
    e = branch * np.sqrt(m * m + np.sin(k) ** 2)                  # branch = -1: the eigenvector of the negative energy
    upc, dnc = e + np.sin(k), m * np.ones_like(k)
    nrm = np.sqrt(upc ** 2 + dnc ** 2)
    psi = np.stack([np.fft.ifft(gk * upc / nrm), np.fft.ifft(gk * dnc / nrm)], axis=1).reshape(-1)
    return psi / np.linalg.norm(psi)


def energy_density(h, chi, n):
    return np.real((chi.conj() * (h @ chi)).reshape(n, 2).sum(axis=1))


def density(chi, n):
    return (np.abs(chi) ** 2).reshape(n, 2).sum(axis=1)


def field(n, s, gam):
    k = 2 * np.pi * np.fft.fftfreq(n)
    sym = 2 - 2 * np.cos(k); sym[0] = 1.0
    sh = np.fft.fft(-(s - s.mean())) * gam / sym; sh[0] = 0
    return np.real(np.fft.ifft(sh))


def circ_mean(p, n):
    ang = 2 * np.pi * np.arange(n) / n
    return (np.angle((p * np.exp(1j * ang)).sum()) % (2 * np.pi)) * n / (2 * np.pi)



def run(branches, gam, t_end, ms, n=1500, width=30.0, dt=1.0, sep=300.0):
    za, zb = n/2 - sep/2, n/2 + sep/2
    chis = [packet(n, za, width, ms[0], 0.0, branches[0]), packet(n, zb, width, ms[1], 0.0, branches[1])]

    def src(chis, u):
        return sum(energy_density(ring(n, u, m), c, n) for c, m in zip(chis, ms))

    def solve_u(chis, u):
        for _ in range(6):
            u = field(n, src(chis, u), gam)
        return u

    def ledger(chis, u):
        em = [np.real(np.vdot(c, ring(n, u, m) @ c)) for c, m in zip(chis, ms)]
        return em, (u * (2 * u - np.roll(u, 1) - np.roll(u, -1))).sum() / (2 * gam)

    u = solve_u(chis, np.zeros(n))
    em0, ef0 = ledger(chis, u)
    pos0 = [circ_mean(density(c, n), n) for c in chis]
    u_at = (float(u[int(za)]), float(u[int(zb)]))
    for _ in range(int(round(t_end / dt))):
        trial = [expm_multiply(-1j * ring(n, u, m) * dt, c) for c, m in zip(chis, ms)]
        u_mid = 0.5 * (u + solve_u(trial, u))
        chis = [expm_multiply(-1j * ring(n, u_mid, m) * dt, c) for c, m in zip(chis, ms)]
        u = solve_u(chis, u_mid)
    em, ef = ledger(chis, u)
    pos = [circ_mean(density(c, n), n) for c in chis]
    kv = [-np.angle(np.vdot(c, np.roll(c.reshape(n, 2), 1, axis=0).reshape(-1))) for c in chis]
    return dict(moved=(pos[0] - pos0[0], pos[1] - pos0[1]), dk=kv, energies=em0, drift=em[0] + em[1] + ef - em0[0] - em0[1] - ef0, u_at=u_at)


def box_statics():
    side = 9; n = side**3
    idx = np.arange(n).reshape(side, side, side)
    lap = 6*np.eye(n)
    for a in range(3):
        lo = np.take(idx, range(side - 1), axis=a).ravel(); hi = np.take(idx, range(1, side), axis=a).ravel()
        lap[lo, hi] -= 1; lap[hi, lo] -= 1
    body = idx[side//2, side//2, side//2]
    g = np.linalg.solve(lap, np.eye(n)[body]); g0 = g[body]
    K = 1.0
    print(f"\n[W2] box with interior 9x9x9, one body at the centre, K = 1: g_0 = {g0:.6f}; bound m = -2K/g_0 = {-2*K/g0:.4f}")
    chi = np.ones(n); N = np.ones(n)                           # unknowns: chi - 1 and N - 1 vanish on the walls; equations: -lap(chi-1) = -mu/chi at the body, -lap(N-1) = (mu/chi^2) N at the body
    for frac in (0.0, -0.25, -0.5, -0.75, -0.9, -0.99, -0.999):
        m = frac*2*K/g0; mu = m/(8*K)
        for it in range(400):
            r1 = lap@(chi - 1); r1[body] -= mu/chi[body]
            r2 = lap@(N - 1); r2[body] += mu*N[body]/chi[body]**2
            J11 = lap.copy(); J11[body, body] += mu/chi[body]**2
            J22 = lap.copy(); J22[body, body] += mu/chi[body]**2
            dchi = np.linalg.solve(J11, -r1)
            r2c = r2.copy(); r2c[body] += (-2*mu*N[body]/chi[body]**3)*dchi[body]
            dN = np.linalg.solve(J22, -r2c)
            chi += dchi; N += dN
            if max(np.abs(dchi).max(), np.abs(dN).max()) < 1e-11: break
        r = np.sqrt(1 + g0*m/(2*K)); Q = mu/chi[body]
        op = lap.copy(); op[body, body] += Q/chi[body]
        print(f"     m = {frac:+.3f} x 2K/g_0: w_0 = {N[body]/chi[body]:.6f} (closed form {1/r:.6f}); chi_0 = {chi[body]:.6f} ((1 + r)/2 = {(1 + r)/2:.6f}); smallest rate {np.min(N/chi):.4f}, largest {np.max(N/chi):.4f}; smallest eigenvalue of -Delta + Q/chi = {np.linalg.eigvalsh(op)[0]:.5f}; Newton steps {it + 1}")
    m = -1.05*2*K/g0; mu = m/(8*K); chi = np.ones(n); worst = None
    for it in range(200):
        r1 = lap@(chi - 1); r1[body] -= mu/chi[body]
        J11 = lap.copy(); J11[body, body] += mu/chi[body]**2
        chi += np.linalg.solve(J11, -r1); worst = np.abs(r1).max()
    print(f"     m = -1.050 x 2K/g_0 (beyond the bound): Newton on the lengths' equation from empty space, 200 steps: residual still {worst:.2e} (no real root: 1 + 4 g_0 mu = {1 + 4*g0*mu:+.3f})")


if __name__ == "__main__":
    gam, t_end = 0.002, 300.0
    print(f"[W1] ring of 1500 sites, packets of width 30 at 600 (A) and 900 (B), both at rest, rest energies 0.3 (A) and 0.6 (B), Gam = {gam}, T = {t_end}; source = the energy density")
    for label, branches in (("A positive, B positive", (1, 1)), ("A positive, B NEGATIVE", (1, -1)), ("A NEGATIVE, B NEGATIVE", (-1, -1))):
        r = run(branches, gam, t_end, (0.3, 0.6))
        print(f"     {label}: energies {r['energies'][0]:+.4f}, {r['energies'][1]:+.4f}; u at A {r['u_at'][0]:+.2e}, at B {r['u_at'][1]:+.2e}; displacements A {r['moved'][0]:+.3f}, B {r['moved'][1]:+.3f}; wave vectors A {r['dk'][0]:+.6f}, B {r['dk'][1]:+.6f}, sum {r['dk'][0] + r['dk'][1]:+.1e}; ledger changed by {r['drift']:+.1e}")
    box_statics()
