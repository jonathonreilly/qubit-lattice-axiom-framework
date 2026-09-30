#!/usr/bin/env python3
"""T28 Test A: is the operator-side 'unit point' a property of the actual Wilson kernel at beta = 6?

Definitions are those of archive/notes/docs/WILSON_TEMPORAL_KERNEL_CASIMIR_GENERATOR_BETA_GBARE_TRANSPORT_THEOREM_NOTE_2026-07-01.md
  W_beta(U) = exp[(beta/N) Re Tr U],  w_R = (1/d_R) int W chi_R^* dU,  eps_R = -ln(w_R / w_0),
  g_{E,R}^2(beta) = 2 eps_R / C_2(R)   (C_2 in half-trace normalisation).
Unit heat kernel exp(t Delta/2), t = 1  <=>  g_{E,R}^2 = 1 for every R.
Nothing here is asymptotic: exact Haar integrals by Weyl integration on the maximal torus
(periodic analytic integrand -> trapezoid rule converges spectrally; grid checked by doubling).
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import ive

# ---------------- SU(3) ----------------
def su3_grid(n):
    # offset grid avoids coincident eigenvalues (Weyl denominator zero) and is spectrally accurate
    off = 0.3183098861837907  # irrational-ish offset, breaks symmetry only in the grid points, not in the integrand
    t = (np.arange(n) + off) * 2 * np.pi / n
    t1, t2 = np.meshgrid(t, t, indexing="ij")
    t3 = -(t1 + t2)
    z = [np.exp(1j * t1), np.exp(1j * t2), np.exp(1j * t3)]
    return t1, t2, t3, z

def hk(z, k):
    """complete homogeneous symmetric polynomial h_k in 3 variables"""
    if k < 0:
        return np.zeros_like(z[0])
    tot = np.zeros_like(z[0])
    for a in range(k + 1):
        for b in range(k - a + 1):
            c = k - a - b
            tot = tot + z[0] ** a * z[1] ** b * z[2] ** c
    return tot

def chi_pq(z, p, q):
    # Jacobi-Trudi for partition (p+q, q)
    l1, l2 = p + q, q
    return hk(z, l1) * hk(z, l2) - hk(z, l1 + 1) * hk(z, l2 - 1)

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def c2_pq(p, q):
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0

def haar_density(t1, t2, t3):
    # |Delta|^2 = prod_{j<k} |e^{i t_j} - e^{i t_k}|^2 = prod 4 sin^2((t_j - t_k)/2); normalised below
    d = (4 * np.sin((t1 - t2) / 2) ** 2) * (4 * np.sin((t1 - t3) / 2) ** 2) * (4 * np.sin((t2 - t3) / 2) ** 2)
    return d

class SU3:
    def __init__(self, n=256):
        self.t1, self.t2, self.t3, self.z = su3_grid(n)
        self.h = haar_density(self.t1, self.t2, self.t3)
        self.h = self.h / self.h.mean()  # int dHaar = 1
        self.retr = np.real(self.z[0] + self.z[1] + self.z[2])
        self.chi = {}
    def char(self, p, q):
        if (p, q) not in self.chi:
            self.chi[(p, q)] = np.real(chi_pq(self.z, p, q))  # real part; W is real & symmetric under conjugation
        return self.chi[(p, q)]
    def w(self, beta, p, q):
        # w_R/w_0 without overflow: shift exponent
        e = np.exp((beta / 3.0) * (self.retr - 3.0))
        w0 = (e * self.h).mean()
        wr = (e * self.h * self.char(p, q)).mean() / dim_pq(p, q)
        return wr / w0
    def gE2(self, beta, p, q):
        r = self.w(beta, p, q)
        return 2 * (-np.log(r)) / c2_pq(p, q)

# ---------------- SU(2) control (closed form via Bessel) ----------------
def su2_ratio(beta, j2):
    """w_j / w_0 for W = exp(beta cos theta) on SU(2), spin j = j2/2, d = j2+1.
    chi_j = sin((j2+1)th)/sin th; Haar (2/pi) sin^2 th dth on [0,pi].
    int e^{b cos} sin((n)th) sin(th) dth*(2/pi)/n with n=j2+1  = (I_{n-1}(b) - I_{n+1}(b))/ n ."""
    n = j2 + 1
    from scipy.special import iv
    # use exponentially-scaled Bessel to avoid overflow: ive(v,x)=iv*exp(-|x|)
    num = (ive(n - 1, beta) - ive(n + 1, beta)) / n
    den = (ive(0, beta) - ive(2, beta)) / 1.0
    return num / den

def su2_gE2(beta, j2):
    j = j2 / 2.0
    return 2 * (-np.log(su2_ratio(beta, j2))) / (j * (j + 1))

def main():
    out = []
    P = lambda *a: (print(*a), out.append(" ".join(str(x) for x in a)))
    reps = [(1, 0), (1, 1), (2, 0), (2, 1), (3, 0)]
    names = {(1, 0): "3", (1, 1): "8", (2, 0): "6", (2, 1): "15", (3, 0): "10"}

    # grid convergence check
    for n in (192, 384):
        s = SU3(n)
        P(f"grid n={n}: g_E,3^2(beta=6) = {s.gE2(6.0,1,0):.10f}, g_E,8^2(6) = {s.gE2(6.0,1,1):.10f}")
    s = SU3(384)

    # sanity gate: July-1 K3  beta * g_E^2 -> 2 N_c = 6
    P("\nSanity gate (July-1 K3): beta * g_{E,3}^2(beta) should -> 6")
    for b in (6.0, 24.0, 96.0, 384.0):
        P(f"  beta={b:6.0f}  beta*g_E,3^2 = {b*s.gE2(b,1,0):.4f}   (SU(3))")
    gate = abs(96.0 * s.gE2(96.0, 1, 0) / 6.0 - 1) < 0.05
    P("  gate (within 5% at beta=96):", "OK" if gate else "FAIL")

    # main table at beta = 6
    P("\nSU(3) Wilson plane kernel at beta = 6 (the pinned point):")
    P("  R     dim  C_2      w_R/w_0    eps_R     g_E,R^2(6)   beta_R (g_E,R^2=1)")
    betaR = {}
    for (p, q) in reps:
        c2 = c2_pq(p, q)
        r = s.w(6.0, p, q)
        g2 = s.gE2(6.0, p, q)
        f = lambda b: s.gE2(b, p, q) - 1.0
        try:
            bR = brentq(f, 0.5, 60.0, xtol=1e-9)
        except ValueError:
            bR = float("nan")
        betaR[(p, q)] = bR
        P(f"  {names[(p,q)]:>3}  {dim_pq(p,q):4d}  {c2:6.3f}  {r:9.5f}  {-np.log(r):8.5f}  {g2:10.5f}   {bR:8.4f}")
    # unit heat kernel comparison
    P("\n  unit heat kernel exp(Delta/2): w_R = exp(-C_2/2) =", ", ".join(f"{names[k]}:{np.exp(-c2_pq(*k)/2):.5f}" for k in reps))

    # verdict on pre-registered reading
    g3, g8, g6 = (s.gE2(6.0, 1, 0), s.gE2(6.0, 1, 1), s.gE2(6.0, 2, 0))
    bs = [betaR[(1, 0)], betaR[(1, 1)], betaR[(2, 0)]]
    dev = max(abs(g3 - 1), abs(g8 - 1), abs(g6 - 1))
    spread = max(bs) / min(bs)
    P(f"\nPre-registered criteria: max|g_E^2(6)-1| over (3,8,6) = {dev:.4f} (pass <= 0.10);"
      f" beta_R spread = {spread:.4f} (pass <= 1.20)")
    P("READING:", "PASS (unit point robust at beta=6)" if (dev <= 0.10 and spread <= 1.20) else "FAIL (unit point is an asymptotic-jet statement, not a property of the beta=6 kernel)")

    # how large must beta be for the Casimir-scaling (R-independence) to hold to 5%?
    P("\nR-dependence of g_E,R^2 * beta / 6 (should tend to 1 for all R):")
    P("  beta      R=3      R=8      R=6      R=15     R=10")
    for b in (6.0, 12.0, 24.0, 48.0, 96.0, 192.0):
        row = [b * s.gE2(b, *k) / 6.0 for k in reps]
        P(f"  {b:5.0f}  " + "  ".join(f"{x:7.4f}" for x in row))

    # cross-check against the repo's own single-plaquette value
    P(f"\ncross-check: w_3/w_0 at beta=6 = {s.w(6.0,1,0):.10f}  (repo: <P>_W = 0.4225317396, docs/ACTION_FORM_NO_GO_EQUIVALENCE_PREMISE_CONTINUUM_REMOVAL_SCOPED_RELOCATION_NOTE_2026-06-08.md:64)")
    # Hessian identity by finite differences along exp(i x T_3), T_3 = diag(1/2,-1/2,0)
    def lnK(x, beta):
        return (beta/3.0)*(2*np.cos(x/2)+1.0)
    hh = 1e-3
    for beta in (6.0, 24.0):
        d2 = -(lnK(hh,beta)-2*lnK(0,beta)+lnK(-hh,beta))/hh**2
        P(f"Hessian check beta={beta}: -d2 ln K/dx2 = {d2:.6f}   beta/(2N_c) = {beta/6:.6f}")
    # sensitivity of the 32nd-power chain to which unit point is called g_bare = 1
    P("\nSensitivity of v_cand (goes as g^32 = (g^2)^16, at fixed plaquette) if g_bare^2 := 6/beta_R:")
    for k in reps:
        P(f"  R={names[k]:>3}: beta_R={betaR[k]:.4f}  (6/beta_R)^16 = {(6.0/betaR[k])**16:.4f}  (factor {1.0/((6.0/betaR[k])**16):.1f} down)")
    # SU(2) control
    P("\nSU(2) control: W = exp(beta cos th), beta_pin = 2 N_c = 4")
    P("  j     C_2     g_E,j^2(4)   beta_j (g_E,j^2=1)")
    for j2 in (1, 2, 3, 4):
        f = lambda b: su2_gE2(b, j2) - 1.0
        bj = brentq(f, 0.3, 40.0)
        P(f"  {j2/2:3.1f}  {j2/2*(j2/2+1):6.3f}  {su2_gE2(4.0,j2):10.5f}   {bj:8.4f}")
    P("  SU(2) sanity: beta*g_E,1/2^2 at beta=400:", f"{400*su2_gE2(400.0,1):.4f} (target 2 N_c = 4)")

    open("testA_output.txt", "w").write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
