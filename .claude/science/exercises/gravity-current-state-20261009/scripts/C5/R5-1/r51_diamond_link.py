"""C5 R5-1 (2): Example D -- timelike-link observables of a continuum free field, indexed by one
LRL realization L7, with exact Gamma x L7 covariance, a mass-shell dispersion and a covariant charge.

Physical coords x = Dn, D = diag(sqrt7,1,1,1), eta = diag(-1,1,1,1).  Gamma acts by Lam = D g D^-1.
Link l = (x, x+d), d in L7 future-timelike, u = d/sqrt(-d^2).  Smearing profile (Gaussian in the
link's rest frame, centred at the link midpoint):  f_l(y) = exp(-E_u(y-x-d/2)/(2 s^2)),
E_u(z) = 2 (u.z)^2 + z.z  (rest-frame Euclidean norm^2; Lorentz covariant).
One-particle vector of Phi(f_l):  v_l(q) = F_d(q) e^{i q.x},  F_d(q) = (2 pi s^2)^2 exp(-s^2 E_u(q)/2) e^{i q.d/2},
q on H_m^+ (q.q = -m^2, q0>0), T(a) = e^{i q.a}, U(Lam) v(q) = v(Lam^-1 q).
(A) covariance F_{Lam d}(Lam q) = F_d(q) at 60 digits (random q, several Lam in Gamma, two d's);
(B) rho_d(a) = W_d(a)/W_d(0), W_d(a) = int dOmega |F_d|^2 e^{i q.a}, d = e0 (rest-frame radial integral);
    decay along timelike / spacelike lattice directions;
(C) independent lab-frame 2D quadrature of W_{Lam d}(Lam a) for Lam = g1 (rapidity arccosh 8), compared with (B);
(D) the bounded link observable s_l = sign(Phi(f_l)): Hermite weights; one-particle weight 2/pi.
"""
import numpy as np
import mpmath as mp
from scipy import integrate, special

m, s = 0.5, 1.0
r7 = np.sqrt(7.0)
Dm = np.diag([r7, 1, 1, 1])
eta = np.diag([-1.0, 1, 1, 1])

def emb(a, b, c, d, i, j):
    M = np.eye(4); M[i, i], M[i, j], M[j, i], M[j, j] = a, b, c, d; return M
g1 = emb(8, 3, 21, 8, 0, 1); g2 = emb(8, 3, 21, 8, 0, 2)
Rz = np.array([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], float)
def phys(g):
    return Dm @ g @ np.linalg.inv(Dm)

# ---------- (A) 60-digit covariance ----------
mp.mp.dps = 60
def mpmat(A):
    return mp.matrix([[mp.mpf(int(round(x))) if abs(x - round(x)) < 1e-12 else mp.mpf(x) for x in row] for row in A])
S7 = mp.sqrt(7)
Dmp = mp.diag([S7, 1, 1, 1]); Dinv = mp.diag([1 / S7, 1, 1, 1])
def physmp(gint):
    return Dmp * mp.matrix(gint.tolist()) * Dinv
def eta_mp(a, b):
    return -a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]
def F_mp(dphys, q):
    u = dphys / mp.sqrt(-eta_mp(dphys, dphys))
    E = 2 * eta_mp(u, q) ** 2 + eta_mp(q, q)
    return (2 * mp.pi * s ** 2) ** 2 * mp.e ** (-mp.mpf(s) ** 2 * E / 2) * mp.expjpi(eta_mp(q, dphys / 2) / mp.pi)
rng = np.random.default_rng(51)
Lams = {"g1": g1.astype(int), "g2": g2.astype(int), "g1*Rz*g2^-1": (g1 @ Rz @ np.round(np.linalg.inv(g2))).astype(int),
        "g2^-1*g1^2": (np.round(np.linalg.inv(g2)) @ g1 @ g1).astype(int)}
for gname, gi in Lams.items():
    gm = mp.matrix(gi.tolist())
    G7 = mp.diag([-7, 1, 1, 1])
    assert mp.norm(gm.T * G7 * gm - G7) == 0
print("(A) covariance |F_{Lam d}(Lam q) - F_d(q)| (60 digits), m=%.2f s=%.2f" % (m, s))
for dn in ([1, 0, 0, 0], [1, 1, 1, 0]):
    dphys = Dmp * mp.matrix(dn)
    worst = mp.mpf(0)
    for gname, gi in Lams.items():
        L = physmp(gi)
        for t in range(6):
            k = mp.matrix([mp.mpf(float(x)) for x in rng.normal(size=3) * 1.5])
            q = mp.matrix([mp.sqrt(m ** 2 + k[0] ** 2 + k[1] ** 2 + k[2] ** 2), k[0], k[1], k[2]])
            Lq = L * q
            assert abs(eta_mp(Lq, Lq) + mp.mpf(m) ** 2) < mp.mpf(10) ** -50
            diff = abs(F_mp(L * dphys, Lq) - F_mp(dphys, q))
            worst = max(worst, diff / abs(F_mp(dphys, q)))
    print("    d(n) =", dn, " Q7(d) =", -7 * dn[0] ** 2 + sum(x * x for x in dn[1:]),
          " max relative deviation over 4 Lam x 6 q:", mp.nstr(worst, 3))

# ---------- (B) rest-frame radial W_d(a), d = e0 ----------
def W_rest(t, r):
    """int d^3k/omega exp(-2 s^2 omega^2) e^{-i omega t} j0(k r)  (constant factors dropped; same in (C))."""
    def re(k):
        w = np.sqrt(k * k + m * m); j0 = np.sinc(k * r / np.pi) if r > 0 else 1.0
        return 4 * np.pi * k * k / w * np.exp(-2 * s * s * w * w) * np.cos(w * t) * j0
    def im(k):
        w = np.sqrt(k * k + m * m); j0 = np.sinc(k * r / np.pi) if r > 0 else 1.0
        return -4 * np.pi * k * k / w * np.exp(-2 * s * s * w * w) * np.sin(w * t) * j0
    R = integrate.quad(re, 0, 12, limit=800, epsabs=1e-14, epsrel=1e-12)[0]
    I = integrate.quad(im, 0, 12, limit=800, epsabs=1e-14, epsrel=1e-12)[0]
    return complex(R, I)
W0 = W_rest(0.0, 0.0)
def rho_n(n):
    a = Dm @ np.array(n, float)
    return W_rest(a[0], np.linalg.norm(a[1:])) / W0
print("(B) rho_d(a) = W_d(a)/W_d(0) for d = e0 (lattice coords n of a), m=%.2f s=%.2f" % (m, s))
print("    timelike a = (n0,0,0,0): t = sqrt7 n0;  |rho| * t^{3/2} should approach a constant (massive dispersive decay)")
for n0 in (1, 2, 4, 8, 16, 32):
    r = rho_n([n0, 0, 0, 0]); t = r7 * n0
    print(f"      n0={n0:3d} t={t:7.2f}  rho={r.real:+.6e}{r.imag:+.6e}i  |rho|={abs(r):.4e}  |rho| t^1.5={abs(r)*t**1.5:.4f}  phase/(m t)={np.angle(r)/(m*t):+.3f}")
print("    spacelike a = (0,n,0,0): |rho| e^{m r} r^{?}")
for n in (1, 2, 4, 8, 16, 24):
    r = rho_n([0, n, 0, 0])
    print(f"      n={n:3d}  rho={r.real:+.6e}{r.imag:+.1e}i  |rho| e^(m r)={abs(r)*np.exp(m*n):.4e}  |rho| e^(m r) r^1.5={abs(r)*np.exp(m*n)*n**1.5:.4e}")
print("    the link fixes only finitely many Gamma elements: rho_d(g1 a) != rho_d(a) in general:")
for n in ([0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0]):
    a = np.array(n, float); ga = g1 @ a
    print(f"      a={n}  rho(a)={rho_n(n):.6f}   g1 a={ga.astype(int).tolist()}  rho(g1 a)={rho_n(ga):.3e}")

# ---------- (C) lab-frame 2D quadrature of W_{Lam d}(Lam a) ----------
L1 = phys(g1)
up = L1 @ np.array([1.0, 0, 0, 0])          # boosted link direction, (8, 3 sqrt7, 0, 0)
def W_lab(b):
    """same integrand as W_rest but with u -> up, in lab variables (q_x, q_perp); b in physical coords."""
    bt, bx, bperp = b[0], b[1], np.hypot(b[2], b[3])
    def integrand(qp, qx, part):
        w = np.sqrt(m * m + qx * qx + qp * qp)
        uq = -up[0] * w + up[1] * qx         # eta(u', q)
        E = 2 * uq * uq - m * m              # rest-frame E_u'(q) on shell
        ph = -w * bt + qx * bx
        base = 2 * np.pi * qp / w * np.exp(-s * s * (E + m * m)) * special.j0(qp * bperp)
        return base * (np.cos(ph) if part == 0 else np.sin(ph))
    out = []
    for part in (0, 1):
        val = integrate.dblquad(lambda qp, qx: integrand(qp, qx, part), -40, 70, 0, 8,
                                epsabs=1e-11, epsrel=1e-9)[0]
        out.append(val)
    return complex(*out)
# note: rest-frame integrand exp(-2 s^2 w^2) = exp(-s^2 (E + m^2)) with E = 2w^2 - m^2: identical normalisation
print("(C) independent lab-frame check W_{g1 d}(g1 a) / W_d(a)  (d = e0; g1 = rapidity arccosh 8 = %.4f)" % np.arccosh(8))
for n in ([0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0]):
    a = Dm @ np.array(n, float); b = L1 @ a
    Wr = W_rest(a[0], np.linalg.norm(a[1:])); Wl = W_lab(b)
    print(f"      a={n}  W_d(a)={Wr.real:+.10e}{Wr.imag:+.10e}i  W_g1d(g1a)={Wl.real:+.10e}{Wl.imag:+.10e}i  |diff|/|W(0)|={abs(Wl-Wr)/abs(W0):.2e}", flush=True)

# ---------- (D) sign observable: Hermite weights ----------
phi = lambda x: np.exp(-x * x / 2) / np.sqrt(2 * np.pi)
tot = 0.0
print("(D) s_l = sign(Phi_l/sigma) = sum_k a_k He_k ; one-particle weight a_1^2 * 1! and partial sums of sum a_k^2 k!")
for k in range(1, 60, 2):
    He = special.hermitenorm(k)
    ak = 2 * integrate.quad(lambda x: He(x) * phi(x), 0, 40, limit=400)[0] / special.factorial(k)
    w = ak * ak * special.factorial(k); tot += w
    if k in (1, 3, 5, 11, 21, 41, 59):
        print(f"      k={k:2d}  a_k^2 k! = {w:.6e}   partial sum = {tot:.6f}")
print("      2/pi =", 2 / np.pi, "  (one-particle fraction of ||s_l Omega||^2 = 1);  tail ~ k^{-3/2} so sum -> 1 slowly")
