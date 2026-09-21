"""Block 55 control (supervisor-run; floating point; evidence, not proof): two walkers on a ring source the rate field that times them.

Reduced walk of block 54 on a ring of N sites: H(m) = m sigma_x + sigma_z D, H_w = sqrt(w) H sqrt(w), w = exp(u); each walker has its own rest
energy m (motion across the line).  Field law (block 53's operator on a line, weak-field form, zero mode removed, sum u = 0):
    (2 u_z - u_{z+1} - u_{z-1}) = -Gam (s_z - mean s).
Sources compared:
    energy        s = e^A + e^B,   e_z = Re chi_z^dagger (H_w chi)_z      (the derivative of <H_w> with respect to u_z)
    probability   s = ebar (|chi^A|^2 + |chi^B|^2)                        (every walker sources alike, whatever its energy)
    rest          s = w (m_A |chi^A|^2 + m_B |chi^B|^2)                   (the weak-field packet's density, times the rest energy and the local rate:
                                                                           by the runner's E1 this IS the energy density of a body at rest)
Ledger: <H_w>_A + <H_w>_B + (1/(2 Gam)) sum_z u (2u - u+ - u-).  Note T2(b) predicts d(ledger)/dt = sum_z (e_z - s_z) du_z/dt; the control
accumulates that prediction step by step and compares it with the change of the ledger.
Wave vectors: k_a = -arg <chi_a| T |chi_a>; by block 54 each changes at -E_a du/dz, so k_A + k_B stays zero iff the pulls are matched."""
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


def packet(n, z0, width, m, k0=0.0):
    k = 2 * np.pi * np.fft.fftfreq(n)
    gk = np.exp(-(np.angle(np.exp(1j * (k - k0))) ** 2) * width ** 2) * np.exp(-1j * k * z0)
    e = np.sqrt(m * m + np.sin(k) ** 2)
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


def run(source, gam, t_end, ms, k0s, n=1500, width=30.0, dt=1.0):
    chis = [packet(n, 500.0, width, ms[0], k0s[0]), packet(n, 1000.0, width, ms[1], k0s[1])]
    ebar = 0.5 * (ms[0] + ms[1])

    def src(chis, u):
        if source == "energy":
            return sum(energy_density(ring(n, u, m), c, n) for c, m in zip(chis, ms))
        if source == "probability":
            return ebar * sum(density(c, n) for c in chis)
        return np.exp(u) * sum(m * density(c, n) for c, m in zip(chis, ms))

    def solve_u(chis, u):
        for _ in range(1 if source == "probability" else 6):           # the energy and rest sources depend on u: iterate the static law
            u = field(n, src(chis, u), gam)
        return u

    def ledger(chis, u):
        em = [np.real(np.vdot(c, ring(n, u, m) @ c)) for c, m in zip(chis, ms)]
        return em, (u * (2 * u - np.roll(u, 1) - np.roll(u, -1))).sum() / (2 * gam)

    u = solve_u(chis, np.zeros(n))
    em0, ef0 = ledger(chis, u)
    pos0 = [circ_mean(density(c, n), n) for c in chis]
    predicted = 0.0
    for _ in range(int(round(t_end / dt))):
        trial = [expm_multiply(-1j * ring(n, u, m) * dt, c) for c, m in zip(chis, ms)]
        u_mid = 0.5 * (u + solve_u(trial, u))
        new = [expm_multiply(-1j * ring(n, u_mid, m) * dt, c) for c, m in zip(chis, ms)]
        u_new = solve_u(new, u_mid)
        mismatch_old = sum(energy_density(ring(n, u, m), c, n) for c, m in zip(chis, ms)) - src(chis, u)
        mismatch_new = sum(energy_density(ring(n, u_new, m), c, n) for c, m in zip(new, ms)) - src(new, u_new)
        predicted += (0.5 * (mismatch_old + mismatch_new) * (u_new - u)).sum()          # trapezoid rule for sum_z (e_z - s_z) du_z
        chis, u = new, u_new
    em, ef = ledger(chis, u)
    pos = [circ_mean(density(c, n), n) for c in chis]
    kv = [-np.angle(np.vdot(c, np.roll(c.reshape(n, 2), 1, axis=0).reshape(-1))) for c in chis]
    k_start = list(k0s)
    return dict(moved=(pos[0] - pos0[0] - 0.0, pos[1] - pos0[1]), dk=(kv[0] - k_start[0], kv[1] - k_start[1]), energies=em0, drift=em[0] + em[1] + ef - em0[0] - em0[1] - ef0, predicted=predicted,
                depth=float(u.min()), height=float(u.max()))


if __name__ == "__main__":
    gam, t_end = 0.002, 300.0
    print(f"ring of 1500 sites, packets of width 30 at 500 and 1000, Gam = {gam}, T = {t_end}")
    for label, ms, k0s in (("both at rest, rest energies 0.3 and 0.6", (0.3, 0.6), (0.0, 0.0)), ("A moving at wave vector 0.4 (energy 0.49, rest energy 0.3), B at rest with rest energy 0.6", (0.3, 0.6), (0.4, 0.0))):
        print(f"  {label}")
        for source in ("energy", "probability", "rest"):
            r = run(source, gam, t_end, ms, k0s)
            dk = r["dk"]
            print(f"    source = {source:11s}: change of wave vectors A {dk[0]:+.6f}, B {dk[1]:+.6f}, sum {dk[0] + dk[1]:+.2e} ({abs(dk[0] + dk[1]) / max(abs(dk[0]), abs(dk[1])):.1e} of the larger); ledger changed by {r['drift']:+.2e}, note T2(b) predicts {r['predicted']:+.2e}; energies A {r['energies'][0]:.4f}, B {r['energies'][1]:.4f}; u from {r['depth']:+.3f} to {r['height']:+.3f}")
