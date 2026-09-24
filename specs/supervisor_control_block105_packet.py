"""Supervisor control for block 105 (the worker's executed part, re-run): the partial-swap walk on a line of 1600 sites with bond
angles eps0 sqrt(w_x w_(x+1)), w = exp(0.001 (x - 500)), eps0 = 0.6; a packet of width 30 at k = pi/3 on the upper band, 400 steps;
its centroid against the exact discrete rays of sin(omega/2) = sin eps |cos k| and against block 54's separable law. Floating point."""
import numpy as np


def rep(tag, ok, msg):
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def P7():
    L, eps0, g = 1600, 0.6, 0.001
    x = np.arange(L)
    x0, k0, sig = 500.0, np.pi / 3, 30.0
    w = np.exp(g * (x - x0))
    epsb = eps0 * np.sqrt(w * np.roll(w, -1))
    cb, sb = np.cos(epsb), np.sin(epsb)
    xs_, ys_ = x, np.roll(x, -1)

    def step(ps):
        out = ps.copy()                                   # A: pairs (up, x) - (down, x+1)
        p_, q_ = 2 * xs_, 2 * ys_ + 1
        out[p_], out[q_] = cb * ps[p_] - 1j * sb * ps[q_], -1j * sb * ps[p_] + cb * ps[q_]
        ps = out.copy()                                   # B: pairs (down, x) - (up, x+1)
        p_, q_ = 2 * xs_ + 1, 2 * ys_
        ps[p_], ps[q_] = cb * out[p_] - 1j * sb * out[q_], -1j * sb * out[p_] + cb * out[q_]
        return ps
    # initial packet on the upper band at k0 (eigenvector of the uniform step at eps0 w(x0))
    e_ = eps0
    MA = np.array([[0, np.exp(1j * k0)], [np.exp(-1j * k0), 0]])
    MB = MA.conj()
    Uk = (np.cos(e_) * np.eye(2) - 1j * np.sin(e_) * MB) @ (np.cos(e_) * np.eye(2) - 1j * np.sin(e_) * MA)
    vals, vecs = np.linalg.eig(Uk)
    j = int(np.argmin(np.angle(vals)))                                   # e^{-i omega} with omega > 0
    chi = vecs[:, j]
    env = np.exp(-(x - x0)**2 / (4 * sig**2) + 1j * k0 * x)
    psi = np.zeros(2 * L, complex)
    psi[0::2], psi[1::2] = env * chi[0], env * chi[1]
    psi /= np.linalg.norm(psi)
    steps = 400
    for _ in range(steps):
        psi = step(psi)
    prob = np.abs(psi[0::2])**2 + np.abs(psi[1::2])**2
    xc = (prob * x).sum()

    def omega(xx, kk, exact=True):
        eps = eps0 * np.exp(g * (xx - x0))
        return 2 * np.arcsin(np.sin(eps) * abs(np.cos(kk))) if exact else 2 * eps * abs(np.cos(kk))

    def rays(exact):
        X, Kk, h = x0, k0, 1e-6
        for _ in range(steps):
            vx = (omega(X, Kk + h, exact) - omega(X, Kk - h, exact)) / (2 * h)
            fk = -(omega(X + h, Kk, exact) - omega(X - h, Kk, exact)) / (2 * h)
            X, Kk = X + vx, Kk + fk
        return X
    xr, xs = rays(True), rays(False)
    disp = xr - x0
    ok = abs(xc - xr) < 0.01 * abs(disp) and abs(xc - xs) > 5 * abs(xc - xr)
    rep("P7 line (executed)", ok,
        f"packet at k = pi/3 in eps = 0.6 exp(0.001 (x - 500)), 400 steps: centroid moved {xc - x0:.2f} sites; exact discrete rays "
        f"{disp:.2f} (off {abs(xc - xr):.3f}); block 54's separable law {xs - x0:.2f} (off {abs(xc - xs):.3f}): the O(eps^2) of P3 and P5 is seen")



P7()
