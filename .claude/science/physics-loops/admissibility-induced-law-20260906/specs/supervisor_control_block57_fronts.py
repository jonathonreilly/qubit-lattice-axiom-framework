"""Block 57 control (supervisor-run; floating point; evidence, not proof): what a switched-on source does to the rate field at weak field, for the
two kinds of kinetic term that survive an arbitrary change of the time parameter.

(i)  REFERENCE CLOCK (each rate against the clocks at the walls; T4):  d^2u/dt^2 = c^2 wbar^2 Lap u - s(t)  in a 61^3 box with u = 0 on the walls,
     a point source switched on at t = 0.  Reported: the time at which u at distance r reaches half of its final value, along an axis and along a
     body diagonal, for ambient rates 1 and 2: expected r/(c wbar).
(ii) NEIGHBOURS ONLY (each rate against its neighbours' rates; T2, T3):  Lap[(kappa/wbar) d^2u/dt^2 + (wbar/gamma) u] = P_0 s(t)  on a 24^3 torus
     (the operator is inverted by transform at every step).  Reported: u(x, t)/u_static(x) at sites 1, 6 and 12*sqrt(3) away, at several times:
     the same number everywhere, 1 - cos(omega_0 t): the whole static profile appears at once and swings in place."""
import numpy as np


def lap(u):
    out = -6 * u
    for ax in range(3):
        out += np.roll(u, 1, ax) + np.roll(u, -1, ax)
    return out


def reference_clock(side, wbar, c=1.0, t_end=44.0):
    h = 0.25 / (c * wbar)
    mid = side // 2
    u_prev = np.zeros((side,) * 3); u = np.zeros((side,) * 3)
    src = np.zeros((side,) * 3); src[mid, mid, mid] = 1.0
    wall = np.ones((side,) * 3, bool); wall[1:-1, 1:-1, 1:-1] = False
    probes = {"axis": [(mid + r, mid, mid) for r in (8, 16, 24)], "diagonal": [(mid + r, mid + r, mid + r) for r in (5, 9, 14)]}
    traces = {k: [[] for _ in v] for k, v in probes.items()}
    times = []
    steps = int(round(t_end / (c * wbar) / h))
    for n in range(steps):
        new = 2 * u - u_prev + h * h * (c * c * wbar * wbar * lap(u) - src)
        new[wall] = 0.0
        u_prev, u = u, new
        times.append((n + 1) * h)
        for k, pts in probes.items():
            for i, p in enumerate(pts):
                traces[k][i].append(u[p])
    out = {}
    for k, pts in probes.items():
        for i, p in enumerate(pts):
            r = np.linalg.norm(np.array(p) - mid)
            tr = np.array(traces[k][i])
            final = -1.0 / (c * c * wbar * wbar) / (4 * np.pi * r)                      # static value far from the walls
            idx = np.argmax(tr <= 0.5 * final)
            out[(k, round(float(r), 2))] = times[idx]
    return out


def neighbours_only(side=24, wbar=1.0, gamma=1.0, kappa=1.0, h=0.05, steps=200):
    k = 2 * np.pi * np.fft.fftfreq(side)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    sym = 6 - 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz)); sym[0, 0, 0] = 1.0
    src = np.zeros((side,) * 3); src[0, 0, 0] = 1.0

    def inv_lap(f):                                                                  # solves -Lap v = f - mean f, zero mean
        fh = np.fft.fftn(f - f.mean()); fh[0, 0, 0] = 0
        return np.real(np.fft.ifftn(fh / sym))

    static = -(gamma / wbar) * inv_lap(src)
    omega0 = wbar / np.sqrt(gamma * kappa)
    u_prev = np.zeros((side,) * 3)
    u = 0.5 * h * h * (-(wbar / kappa) * inv_lap(src))                               # first step from rest: u(h) = a(0) h^2/2
    rows = []
    sites = [(1, 0, 0), (6, 0, 0), (12, 12, 12)]
    for n in range(1, steps):
        # -Lap[(kappa/wbar) a + (wbar/gamma) u] = -P_0 s   =>   a = -(wbar^2/(gamma kappa)) u - (wbar/kappa) inv_lap(s)
        acc = -(omega0 ** 2) * u - (wbar / kappa) * inv_lap(src)
        new = 2 * u - u_prev + h * h * acc
        u_prev, u = u, new
        if (n + 1) in (1, 20, 60, 120, 200):
            t = (n + 1) * h
            ratios = [u[s] / static[s] for s in sites]
            rows.append((t, ratios, 1 - np.cos(omega0 * t)))
    return rows


if __name__ == "__main__":
    print("(i) reference clock, 61^3 box, c = 1: time at which u reaches half its final value, against r/(c wbar)")
    for wbar in (1.0, 2.0):
        res = reference_clock(61, wbar)
        print(f"    ambient rate {wbar:.0f}: " + "; ".join(f"{k} r = {r}: t = {t:.2f} (r/(c wbar) = {r / wbar:.2f})" for (k, r), t in res.items()))
    print("(ii) neighbours only, 24^3 torus: u(x, t)/u_static(x) at distances 1, 6 and 20.8 against 1 - cos(omega_0 t)")
    for t, ratios, want in neighbours_only():
        print(f"    t = {t:5.2f}: " + ", ".join(f"{v:.6f}" for v in ratios) + f"   (1 - cos(omega_0 t) = {want:.6f})")
