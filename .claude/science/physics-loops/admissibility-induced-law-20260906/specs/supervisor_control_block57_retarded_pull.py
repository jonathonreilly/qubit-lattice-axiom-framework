"""Block 57 control (supervisor-run; floating point; evidence, not proof): a rate field with its own motion, referred to the clocks at the walls.

Line of N sites, walls at both ends held at the ambient rate; block 54's reduced walk for two walkers (rest energies m_A, m_B); block 56's simplest
bond energy on a line, F = (2/G) sum (phi_z - phi_(z+1))^2, phi = sqrt(w); and the kinetic term of this block's T4,
    K = (1/(2 G c^2)) sum (du_z/dt)^2 / w_z = (2/(G c^2)) sum (dpsi_z/dt)^2,   psi = w^(-1/2),   t = the time of the wall clocks.
Equations:  i dchi/dt = phi H phi chi;   d^2 psi_z/dt^2 = (G c^2 / (2 psi_z)) (dF/du_z + e_z),   e_z = Re chi_z^dagger (H_w chi)_z.
Ledger: <H_w>_A + <H_w>_B + F + K.

(1) SWITCH-ON.  The field starts at the ambient rate everywhere with the two walkers present, d = 300 sites apart.  Each walker's own field builds
    up symmetrically around it and pulls it nowhere; the other's field arrives as a front.  Reported: B's wave vector against time, for c = 1 and
    c = 2, and for walls at twice the ambient rate (rates, and so both speeds, doubled).  Expected arrival: d/(c wbar).
(2) SLOW MOTION.  The field starts at its static solution; the run is compared with the static law of block 56 (field re-solved at every step)."""
import numpy as np
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import expm_multiply, spsolve


def walk(n, phi, m):
    rows, cols, vals = [], [], []
    for s1, s2 in ((0, 1), (1, 0)):
        rows.append(2 * np.arange(n) + s1); cols.append(2 * np.arange(n) + s2); vals.append(phi * phi * m + 0j)
    up, dn = np.arange(1, n), np.arange(0, n - 1)
    amp = phi[1:] * phi[:-1]
    for s, c in ((0, 1.0), (1, -1.0)):
        rows.append(2 * up + s); cols.append(2 * dn + s); vals.append(0.5j * amp * c)
        rows.append(2 * dn + s); cols.append(2 * up + s); vals.append(-0.5j * amp * c)
    return coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(2 * n, 2 * n)).tocsr()


def packet(n, z0, width, m):
    k = 2 * np.pi * np.fft.fftfreq(n)
    gk = np.exp(-(k ** 2) * width ** 2) * np.exp(-1j * k * z0)
    e = np.sqrt(m * m + np.sin(k) ** 2)
    upc, dnc = e + np.sin(k), m * np.ones_like(k)
    nrm = np.sqrt(upc ** 2 + dnc ** 2)
    psi = np.stack([np.fft.ifft(gk * upc / nrm), np.fft.ifft(gk * dnc / nrm)], axis=1).reshape(-1)
    return psi / np.linalg.norm(psi)


def energy_density(h, chi, n):
    return np.real((chi.conj() * (h @ chi)).reshape(n, 2).sum(axis=1))


def bond_force(phi, g):
    """dF/du_z for F = (2/g) sum (phi_z - phi_(z+1))^2, the two end sites being walls (not varied)."""
    out = np.zeros_like(phi)
    out[1:-1] = 2 / g * phi[1:-1] * (2 * phi[1:-1] - phi[2:] - phi[:-2])
    return out


def bond_energy(phi, g):
    return 2 / g * ((phi[1:] - phi[:-1]) ** 2).sum()


def static_phi(n, chis, ms, g, wall):
    """Block 56: at a fixed amplitude the static law is linear in phi: ((2/g)(2 phi_z - phi_(z+1) - phi_(z-1)) + (K phi)_z) = 0."""
    kd = np.zeros(n); ko = np.zeros(n - 1)
    for chi, m in zip(chis, ms):
        c = chi.reshape(n, 2)
        kd += m * 2 * np.real(c[:, 0].conj() * c[:, 1])
        hop = 0.5j * (c[1:, 0].conj() * c[:-1, 0] - c[1:, 1].conj() * c[:-1, 1])
        ko += np.real(hop)                                                  # K_(z+1,z) = K_(z,z+1) = Re chi_(z+1)^dagger H_(z+1,z) chi_z
    lap = diags([np.full(n - 1, -2 / g), np.full(n, 4 / g), np.full(n - 1, -2 / g)], [-1, 0, 1]).tolil()
    kmat = diags([ko, kd, ko], [-1, 0, 1]).tolil()
    a = (lap + kmat).tocsr()[1:-1, :]
    rhs = -(a[:, 0].toarray().ravel() + a[:, -1].toarray().ravel()) * wall
    inner = spsolve(a[:, 1:-1].tocsc(), rhs)
    return np.concatenate([[wall], inner, [wall]])


def run(mode, g, c, t_end, ms=(0.3, 0.6), n=1500, sep=300, wall=1.0, dt=0.5, report_every=50):
    za, zb = n / 2 - sep / 2, n / 2 + sep / 2
    chis = [packet(n, za, 30.0, ms[0]), packet(n, zb, 30.0, ms[1])]
    if mode == "switch-on":
        phi = np.full(n, wall)
    else:
        phi = static_phi(n, chis, ms, g, wall)
    psi = 1 / phi
    vel = np.zeros(n)

    def force(psi, chis):
        phi = 1 / psi
        e = sum(energy_density(walk(n, phi, m), ch, n) for ch, m in zip(chis, ms))
        f = g * c * c / (2 * psi) * (bond_force(phi, g) + e)
        f[0] = f[-1] = 0.0
        return f, e

    def ledger(psi, vel, chis):
        phi = 1 / psi
        return sum(np.real(np.vdot(ch, walk(n, phi, m) @ ch)) for ch, m in zip(chis, ms)) + bond_energy(phi, g) + 2 / (g * c * c) * (vel ** 2).sum()

    start = ledger(psi, vel, chis)
    rows = []
    steps = int(round(t_end / dt))
    f, _ = force(psi, chis)
    for step in range(steps + 1):
        if step % int(round(report_every / dt)) == 0:
            kv = [-np.angle(np.vdot(ch, np.roll(ch.reshape(n, 2), 1, axis=0).reshape(-1))) for ch in chis]
            rows.append((step * dt, kv[0], kv[1], ledger(psi, vel, chis) - start, float((1 / psi ** 2).min())))
        if step == steps:
            break
        if mode == "static":
            chis = [expm_multiply(-1j * walk(n, 1 / psi, m) * dt, ch) for ch, m in zip(chis, ms)]
            psi = 1 / static_phi(n, chis, ms, g, wall)
            continue
        vel_half = vel + 0.5 * dt * f
        psi_new = psi + dt * vel_half
        psi_mid = 0.5 * (psi + psi_new)
        chis = [expm_multiply(-1j * walk(n, 1 / psi_mid, m) * dt, ch) for ch, m in zip(chis, ms)]
        psi = psi_new
        f, _ = force(psi, chis)
        vel = vel_half + 0.5 * dt * f
    return rows


if __name__ == "__main__":
    g = 0.002
    print(f"line of 1500 sites, walls at the ends, walkers of rest energy 0.3 (A) and 0.6 (B) 300 sites apart, G = {g}")
    print("(1) switch-on: the field starts at the ambient rate; B's wave vector by time (A's pull on B arrives as a front)")
    for label, c, wall in (("c = 1, ambient rate 1", 1.0, 1.0), ("c = 2, ambient rate 1", 2.0, 1.0), ("c = 1, ambient rate 4 (phi = 2 at the walls)", 1.0, 2.0)):
        t_end = 450 if (c == 1.0 and wall == 1.0) else (240 if c == 2.0 else 120)
        rows = run("switch-on", g, c, t_end, wall=wall, dt=0.4 / (c * wall * wall), report_every=t_end / 9)      # step well inside the lattice stability limit c wbar dt < 1
        expected = 300 / (c * wall * wall)
        print(f"    {label}: front expected at t = {expected:.0f}")
        print("        " + "; ".join(f"t = {t:.0f}: k_B = {kb:+.2e}" for t, ka, kb, led, wmin in rows))
        print(f"        ledger moved by {rows[-1][3]:+.1e} over the run (start to end)")
    print("(2) slow motion from the static field, T = 300: the dynamic field (c = 1) against the static law of block 56, for two strengths of the coupling")
    for g2 in (0.002, 0.0004):
        dyn = run("dynamic", g2, 1.0, 300, report_every=100)
        sta = run("static", g2, 1.0, 300, report_every=100)
        print(f"    G = {g2}:")
        for (t, ka, kb, led, wmin), (_, ka2, kb2, _, _) in zip(dyn, sta):
            print(f"        t = {t:.0f}: k_A = {ka:+.6f} (static law {ka2:+.6f}); k_B = {kb:+.6f} (static law {kb2:+.6f}); speeds k/m = {abs(ka) / 0.3:.3f}, {abs(kb) / 0.6:.3f} of the limit; ledger moved by {led:+.1e}; lowest rate {wmin:.4f}")
