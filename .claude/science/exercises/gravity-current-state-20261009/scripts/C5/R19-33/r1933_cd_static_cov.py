"""R19-33 (c) static response of the constraint bridge on the lattice; (d) W(B4) covariance.
(c) Bridge exponent B_t = lam[rho K rho + 2 rho K A + 4 Pperp K Pperp + PL K PL], K = (-Delta_3)^{-1}.
    Two static dust masses M1, M2 (rho = M delta, A = P = 0): cross term 2 lam M1 M2 K(r) per slice
    -> potential V(r) = -2 lam M1 M2 K(r): attractive iff lam K > 0; check 4 pi r K(r) -> 1.
    Light probe (line of T_11 along x at impact parameter b; A = theta_11 T_11 with q_1 = 0 exactly,
    theta_11 = 1): cross = 2 lam (rho_l + A_l) K rho_m -> ratio to dust probe = 2 (gamma = 1) on the lattice.
(d) (i) on lattice-conserved sources (s.J = 0, s = 2 sin(k/2)), W_TT + W_inst = W_GR exactly (numeric
    check at random lattice momenta); (ii) W_inst alone is not invariant under the W(B4) element
    swapping axes 1 <-> 4 (W_GR is); (iii) D2's rho is not conserved: residual of K2's O(kappa)
    Ward identity sum (nabla xi) T on an exact Euclidean lattice solution, K2 vs D2.
"""
import numpy as np
rng = np.random.default_rng(11)
print("== (c) static dust-dust response of the bridge, L^3 periodic, zero mode removed ==")
for L in (32, 64):
    k = 2 * np.pi * np.fft.fftfreq(L); K3 = np.meshgrid(k, k, k, indexing='ij')
    s2 = sum((2 * np.sin(kk / 2)) ** 2 for kk in K3)
    Gq = np.where(s2 > 0, 1.0 / np.where(s2 > 0, s2, 1), 0.0)
    G = np.fft.ifftn(Gq).real
    G -= G[L // 2, L // 2, L // 2]  # remove the torus offset (compare differences)
    for name, dirv in [("axis", (1, 0, 0)), ("face diag", (1, 1, 0)), ("body diag", (1, 1, 1))]:
        rows = []
        for n in (2, 4, 6, 8):
            x = tuple((np.array(dirv) * n) % L)
            r = n * np.linalg.norm(dirv)
            if r < L / 4:
                # V(r) - V(far) with far = (L/2,L/2,L/2); compare 1/(4 pi r) - 1/(4 pi r_far)
                rf = np.linalg.norm([L / 2] * 3)
                rows.append("r=%.2f 4pi(K(r)-K(far))/(1/r-1/r_far)=%.4f" % (r, 4 * np.pi * G[x] / (1 / r - 1 / rf)))
        print(" L=%d %-9s " % (L, name) + " | ".join(rows))
print(" sign: K(r) - K(far) > 0 at all listed r -> cross term +2 lam M1 M2 K raises the weight of nearby")
print("       like masses -> attractive, V(r) = -2 lam M1 M2/(4 pi r) + const, G_N = lam/(2 pi) [lam = kappa^2/4]")
print(" light probe on the lattice: q_1 = 0 for a source uniform along x, theta_11(q_1=0) = 1 exactly ->")
print("       (rho_l + A_l)/rho_l = 2 exactly -> 1 + gamma = 2;  Newton-only bridge (no rho A term): ratio 1, gamma = 0")

print("\n== (d)(i) lattice-conserved sources: W_TT + W_inst - W_GR at random lattice momenta ==")
def theta3(q):
    return np.eye(3) - np.outer(q, q) / (q @ q)
def W_parts(J, s):
    q = s[:3]; p2 = s @ s; th = theta3(q)
    Jij = J[:3, :3]
    JTT = th @ Jij @ th - 0.5 * th * np.trace(th @ Jij)
    WTT = np.sum(JTT * JTT) / p2
    WGR = (np.sum(J * J) - 0.5 * np.trace(J) ** 2) / p2
    rho = J[3, 3]; A = np.trace(th @ Jij); P = J[:3, 3]
    Pp = th @ P; PL = (q @ P) / np.linalg.norm(q)
    Winst = (0.5 * rho ** 2 - rho * A + 2 * Pp @ Pp + 0.5 * PL ** 2) / (q @ q)
    return WTT, Winst, WGR
def conserved_J(s):
    # random symmetric J projected onto s.J = 0 (4D transverse projector on both indices)
    X = rng.normal(size=(4, 4)); X = X + X.T
    Pt = np.eye(4) - np.outer(s, s) / (s @ s)
    return Pt @ X @ Pt
worst = 0
for trial in range(200):
    kk = rng.uniform(-np.pi, np.pi, size=4); s = 2 * np.sin(kk / 2)
    J = conserved_J(s); WTT, Wi, WGR = W_parts(J, s)
    worst = max(worst, abs(WTT + Wi - WGR) / max(1e-12, abs(WGR)))
print(" max relative |W_TT + W_inst - W_GR| over 200 momenta: %.2e" % worst)
print("\n== (d)(ii) covariance under the W(B4) element swapping axes 1<->4 ==")
Pm = np.eye(4)[[3, 1, 2, 0]]
dev_inst, dev_gr = 0, 0
for trial in range(200):
    kk = rng.uniform(-np.pi, np.pi, size=4); s = 2 * np.sin(kk / 2)
    J = conserved_J(s)
    a = W_parts(J, s); b = W_parts(Pm @ J @ Pm.T, Pm @ s)
    dev_inst = max(dev_inst, abs(a[1] - b[1]) / (abs(a[1]) + abs(b[1])))
    dev_gr = max(dev_gr, abs(a[2] - b[2]) / (abs(a[2]) + 1e-12))
print(" W_GR: max rel. change %.1e (covariant);  W_inst alone: max rel. change %.2f (not covariant);"
      " W_TT alone likewise" % (dev_gr, dev_inst))

print("\n== (d)(iii) conservation: K2's exact stress vs D2's T_44 on an exact Euclidean lattice solution ==")
D = 4
def sh(F, mu, n): return np.roll(F, -n, axis=mu)
def Dl(phi, mu): return sh(phi, mu, 1) - phi
def stress(phi, m2, d2=False):
    T = np.zeros((D, D) + phi.shape)
    for m in range(D):
        for n in range(D):
            if m != n:
                T[m, n] = 0.25 * (Dl(phi, m) + sh(Dl(phi, m), n, 1)) * (Dl(phi, n) + sh(Dl(phi, n), m, 1))
        if d2 and m == 3:
            z = -0.25 * (Dl(phi, m) ** 2 + sh(Dl(phi, m), m, -1) ** 2) - 0.5 * m2 * phi ** 2   # sign: T_44 = -rho
            z = -z * 0 + (-0.25 * (Dl(phi, m) ** 2 + sh(Dl(phi, m) ** 2, m, -1))) * (-1) - 0.5 * m2 * phi ** 2
        else:
            z = 0.5 * Dl(phi, m) * sh(Dl(phi, m), m, -1) - 0.5 * m2 * phi ** 2
        for r in range(D):
            if r != m:
                z = z - 0.25 * (Dl(phi, r) ** 2 + sh(Dl(phi, r) ** 2, r, -1))
        T[m, m] = sh(z, m, 1)
    return T
def gauge(xi):
    h = np.zeros((D, D) + xi.shape[1:])
    for m in range(D):
        for n in range(D):
            h[m, n] = (sh(xi[n], m, 1) - xi[n]) + (sh(xi[m], n, 1) - xi[m])
    return h
L, Lt, m2 = 6, 14, 0.5
x = np.arange(L); t = np.arange(Lt)
kx = 2 * np.pi / L
E = np.arccosh(1 + (4 * np.sin(kx / 2) ** 2 + m2) / 2)
TT, XX = np.meshgrid(t, x, indexing='ij')
phi = (np.cosh(E * (TT - Lt / 2)) * np.cos(kx * XX))[:, :, None, None] * np.ones((Lt, L, L, L))
phi = np.moveaxis(phi, 0, 3)     # axes (x, y, z, t); time = axis 3
Eom = -sum(sh(phi, mu, 1) + sh(phi, mu, -1) - 2 * phi for mu in range(D)) + m2 * phi
print(" EOM residual in the interior (t=3..Lt-4): %.1e" % np.abs(Eom[..., 3:Lt - 3]).max())
for d2 in (False, True):
    res = []
    for trial in range(4):
        xi = np.zeros((D,) + phi.shape)
        xi[3][..., 5:Lt - 5] = rng.integers(-5, 6, size=(L, L, L, Lt - 10))
        val = np.sum(gauge(xi) * stress(phi, m2, d2))
        res.append(val)
    print(" %s: sum (nabla xi + nabla xi) T over time-gauge xi (interior support) = %s" % ("D2" if d2 else "K2", np.round(res, 6)))
