#!/usr/bin/env python3
"""Does the fluctuation form stay coercive on the complex class defined by plaquette curvature alone? Text 3.3(b), 3.4.

The class C(Om; eps_0, alpha) of an earlier version of Text 3.3(b) asks only |Re F_p| <= eps_0, |Im F_p| <= alpha on each plaquette. It contains
    V_(x, 1) = exp(i sigma_3 theta(x_2)),  V_(x, 2) = 1,   theta(x_2) = i c(x_2),   c a sawtooth with increments +- alpha,
which has |Im F_p| = alpha and F_p imaginary, whatever the size of c. So on a torus of side N the imaginary part of the connection reaches alpha N / 2 in this
gauge, and it cannot be removed by a real gauge function. The same field with theta real is the control: real flux +- alpha, unitary transports.

Model: SU(2) on a 2D torus 3 L x N, blocks of side L, charged fluctuations (b^+, b^-) about this Cartan field, the exact second variation of the Wilson action,
    bilinear form B(b^-, b^+) := Hess A (b^-, b^+) + tau < Pi_0 D^* b^-, Pi_0 D^* b^+ >,    tau = 1,
restricted to X^+- := ker Q^+- with Q the paired-contour constraint per bond at this field, and Pi_0 the covariant projection on zero block average.
This is the structure of A = H + tau D Pi_0 D^* on X in 4.6. It is 2D, one step, with V not corrected to the exact lift, and mu . Hess M left out. It is a model of
the mechanism, and it does not test the 4D map.

By hand: for b_2 independent of x_1 the curl is (e^(2c) - 1) b^+ against (e^(-2c) - 1) b^-, with product -4 sinh^2(c), so the form has a potential well going to
minus infinity with the size of c, against a gap of order L^-2. So I expect a zero of the form at alpha N L of order one.

Pre-registered criteria, written before the first run.
    PASS-REAL: at real flux, on the whole grid, the smallest singular value of B on X times L^2 stays above 2.
    PASS-SING: at imaginary flux, on the same grid, det B changes sign along alpha, and bisection brings the smallest singular value below 1e-6.
    SING means: the statement "A >= c L^-2 at every field in the class, uniformly in the volume" is false, in this model, on the class by curvature.
    NO-SING: no sign change on the grid. Then report the smallest singular value, and the statement is not falsified by this model.
    SCALE: report alpha_c N L at the first zero, for the sizes run. No threshold: it is a number for the text.

Run under the numeric lock, nice, BLAS threads 1, RSS checked against 2 GB.

First run, under a confirmed lock: FAIL-REAL as registered, and two errors of mine. (1) The grid went to alpha L^2 of order 1 at real flux, far outside the regular regime
alpha L^2 << 1 of the file, and there the form does go soft: smin L^2 = 0.026, 0.001, 0.013 at the worst point of the grid, which is the Nielsen-Olesen mode, the -2 B spin shift of 8.2. That is true physics and not
in the class. (2) The sign test was invalid: det(R_-^T B R_+) depends on the sign of the arbitrary null bases, so it flipped with smin = 0.5. So the numbers of the first run say nothing about zeros.

Second stage, criteria written before it ran, after the errors above.
    The sign is now that of the bordered matrix K := [[B, Q_-^T], [Q_+, 0]], real at imaginary flux, analytic in alpha, and it changes sign only where B on X is singular, Q having full rank.
    Grid: alpha L^2 <= 0.2 for both real and imaginary flux, the same grid, N large.
    PASS-REAL2: at real flux, on this grid, smin L^2 stays above 2, on every size.
    PASS-SING2: at imaginary flux on this grid, sign K changes at some alpha, and bisection brings smin below 1e-6, on every size, with alpha_c N L reported.
    NO-SING2: no sign change on the grid: report min smin L^2.

Second run, under a confirmed lock: FAIL-REAL2 (smin L^2 = 0.018, 0.008, 0.184), PARTIAL-SING2. The control did its job: a diagnostic gave 4.5 at alpha = 0 and a fall only at large theta, and the cause is a bug of mine.
D^* and Pi_0 had charge 1 in place of the adjoint charge 2, and the wrong order of transports in Pi_0, so the gauge term was not covariant against the Hessian. So the numbers of the first two runs are void, zeros included.

Third stage, criteria written before it ran. Fixed as above, and Q is now Q_str, the straight contours with the transports of the legs, the pair (Q_str, Pi_0) of (CUT) item 1. Same model otherwise.
    Sizes: (L, N, n1) = (3, 72, 3), (3, 108, 3), (5, 140, 2), where the torus is n1 L x N. Grid: alpha L^2 <= 0.2, for real and imaginary flux alike.
    PASS-REAL3: at real flux on this grid, smin L^2 stays above 2, at every size.
    PASS-SING3: at imaginary flux on this grid, sign K changes at some alpha, and bisection brings smin below 1e-6, at every size; report alpha_c N L.
    NO-SING3: no sign change at some size; report min smin L^2 there.

Fourth stage (argument "zero"), criteria written after seeing the third stage so far: PASS-REAL3 at L = 3, min 4.500; at imaginary flux no sign change of K on the coarse grid, with smin L^2 falling from 4.5 to 0.065, 0.055.
So a pair of eigenvalues passes near zero, or a grid of 21 points misses a pair of crossings. Decide it by locating the zero itself, at L = 3, N = 72, n1 = 3.
    Step 1: scan the real axis near the minimum of smin on a grid of 200 points, and bisect any sign change of K.
    Step 2: if there is none, Newton on the analytic function det K(alpha) at complex alpha, with the logarithmic derivative by a central difference, from the minimum of smin. A complex alpha means flux with both parts: |Re F_p| = |Im alpha|, |Im F_p| = |Re alpha|.
    PASS-ZERO: smin < 1e-8 at a real or complex alpha_* with |alpha_*| L^2 <= 0.25, with alpha_* reported.
    NO-ZERO: neither. Then the file says only that smin falls by a factor of about 80 on the grid.

Results, third stage, under a confirmed lock: PASS-REAL3, smin L^2 = 4.500, 4.500, 4.775. PARTIAL-SING3: L = 5, N = 140, n1 = 2: det K changes sign at alpha_c = 0.002876, smin = 7.52e-10, alpha_c N L = 2.014, max |Im connection| = 0.201.
L = 3: no sign change on the grid, min smin L^2 = 0.0646 (N = 72), 0.0545 (N = 108), both at the end of the grid. Fourth stage, L = 3, N = 72: no sign change on the fine scan, Newton stalled at alpha = 0.0212 + 0.0142 i with smin = 0.0099: NO-ZERO.
"""
import resource
import sys

import numpy as np

RSS_LIMIT = 2 * 1024**3
S3 = np.diag([1.0 + 0j, -1.0])
SP = np.array([[0, 1], [0, 0]], dtype=complex)
SM = np.array([[0, 0], [1, 0]], dtype=complex)
ID = np.eye(2, dtype=complex)


def check_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss > RSS_LIMIT:
        raise SystemExit(f"RSS {rss} above limit")


def sawtooth(N, alpha):
    c = np.zeros(N)
    for j in range(N):
        c[j] = alpha * min(j, N - j)
    return c


class Model:
    def __init__(self, L, N, alpha, imag, tau=1.0, n1=3, qstr=True):
        self.L, self.N1, self.N2 = L, n1 * L, N
        self.qstr = qstr
        self.alpha = alpha
        self.tau = tau
        c = sawtooth(N, 1.0) * alpha  # alpha may be complex
        self.theta = np.zeros((self.N1, self.N2, 2), dtype=complex)
        self.theta[:, :, 0] = (1j * c if imag else c)[None, :]
        self.nl = 2 * self.N1 * self.N2
        self.ns = self.N1 * self.N2

    def lid(self, x1, x2, mu):
        return 2 * ((x1 % self.N1) * self.N2 + (x2 % self.N2)) + mu

    def sid(self, x1, x2):
        return (x1 % self.N1) * self.N2 + (x2 % self.N2)

    def th(self, x1, x2, mu):
        return self.theta[x1 % self.N1, x2 % self.N2, mu]

    def contour_row(self, steps, charge, main_mu=0):
        """steps: list of (x1, x2, mu, sign) in path order. Coefficients of b^charge on the links: exp(i charge (A_l - B_l)) * sign, with the insertion after
        V^-1 for a backward step, as in V^-1 exp(-i b)."""
        total = sum(s * self.th(x1, x2, mu) for x1, x2, mu, s in steps)
        out = {}
        pref = 0j
        for x1, x2, mu, s in steps:
            t = s * self.th(x1, x2, mu)
            if s > 0:
                a = pref
                b = total - pref
            else:
                a = pref + t
                b = total - pref - t
            co = np.exp(1j * charge * (a - b)) * s
            k = self.lid(x1, x2, mu)
            if not self.qstr or mu == main_mu:
                out[k] = out.get(k, 0) + co
            pref += t
        return out

    def bond_contours(self, y1, y2, mu):
        """paths from the block centre y to y + L e_mu, one per transverse offset s"""
        L = self.L
        h = (L - 1) // 2
        nu = 1 - mu
        paths = []
        for s in range(-h, h + 1):
            steps = []
            p = [y1, y2]
            sgn = 1 if s > 0 else -1
            for _ in range(abs(s)):
                if sgn > 0:
                    steps.append((p[0], p[1], nu, 1))
                    p[nu] += 1
                else:
                    p[nu] -= 1
                    steps.append((p[0], p[1], nu, -1))
            for _ in range(L):
                steps.append((p[0], p[1], mu, 1))
                p[mu] += 1
            for _ in range(abs(s)):
                if sgn > 0:
                    p[nu] -= 1
                    steps.append((p[0], p[1], nu, -1))
                else:
                    steps.append((p[0], p[1], nu, 1))
                    p[nu] += 1
            paths.append(steps)
        return paths

    def Q(self, charge):
        L = self.L
        h = (L - 1) // 2
        rows = []
        for i1 in range(self.N1 // L):
            for i2 in range(self.N2 // L):
                y = (h + i1 * L, h + i2 * L)
                for mu in (0, 1):
                    row = np.zeros(self.nl, dtype=complex)
                    for steps in self.bond_contours(y[0], y[1], mu):
                        for k, v in self.contour_row(steps, charge, mu).items():
                            row[k] += v / L
                    rows.append(row)
        return np.array(rows)

    def hess(self):
        """Second variation of A_p = 1 - (1/2) Tr V_p in (b^-, b^+), the exact plaquette Taylor coefficient."""
        H = np.zeros((self.nl, self.nl), dtype=complex)  # H[j, i]: b^-_j b^+_i
        for x1 in range(self.N1):
            for x2 in range(self.N2):
                # the plaquette: x -> x+e1 -> x+e1+e2 -> x+e2 -> x
                ls = [(x1, x2, 0, 1), (x1 + 1, x2, 1, 1), (x1, x2 + 1, 0, -1), (x1, x2, 1, -1)]
                facs = []
                for a1, a2, mu, s in ls:
                    t = self.th(a1, a2, mu)
                    Vmat = np.diag([np.exp(1j * t), np.exp(-1j * t)])
                    if s < 0:
                        Vmat = np.diag([np.exp(-1j * t), np.exp(1j * t)])
                    facs.append((self.lid(a1, a2, mu), s, Vmat))

                def word(ins):
                    m = ID.copy()
                    for pos, (k, s, Vm) in enumerate(facs):
                        slot = ins.get(pos, ID)
                        m = m @ (slot @ Vm if s > 0 else Vm @ slot)
                    return np.trace(m)

                for i, (ki, si, _) in enumerate(facs):
                    # i: slot of sigma_+ ; j: slot of sigma_-
                    for j, (kj, sj, _) in enumerate(facs):
                        if i == j:
                            val = -0.5 * word({i: -0.5 * (SP @ SM + SM @ SP)})
                        else:
                            val = -0.5 * word({i: 1j * si * SP, j: 1j * sj * SM})
                        H[kj, ki] += val
        return H

    def dstar(self, charge):
        """(D^* b)^charge (x) = sum_mu [ b_mu(x) - exp(-2 i charge' theta) b_mu(x - mu) ] with charge' = +1 for b^+"""
        D = np.zeros((self.ns, self.nl), dtype=complex)
        for x1 in range(self.N1):
            for x2 in range(self.N2):
                s = self.sid(x1, x2)
                for mu in (0, 1):
                    D[s, self.lid(x1, x2, mu)] += 1
                    a = (x1 - (mu == 0), x2 - (mu == 1))
                    D[s, self.lid(a[0], a[1], mu)] += -np.exp(-2j * charge * self.th(a[0], a[1], mu))
        return D

    def pi0(self, charge):
        """Covariant projection on zero block average, transports along axial paths to the block centre"""
        L = self.L
        h = (L - 1) // 2
        P = np.eye(self.ns, dtype=complex)
        for i1 in range(self.N1 // L):
            for i2 in range(self.N2 // L):
                y = (h + i1 * L, h + i2 * L)
                sites = []
                trans = []
                for d1 in range(-h, h + 1):
                    for d2 in range(-h, h + 1):
                        # transport from x = y + d to y in the frame convention of dstar: first along 2 then along 1
                        ph = 0j
                        p = [y[0], y[1]]
                        sg1 = 1 if d1 > 0 else -1
                        for _ in range(abs(d1)):
                            if sg1 > 0:
                                ph += self.th(p[0], p[1], 0)
                                p[0] += 1
                            else:
                                p[0] -= 1
                                ph -= self.th(p[0], p[1], 0)
                        sg2 = 1 if d2 > 0 else -1
                        for _ in range(abs(d2)):
                            if sg2 > 0:
                                ph += self.th(p[0], p[1], 1)
                                p[1] += 1
                            else:
                                p[1] -= 1
                                ph -= self.th(p[0], p[1], 1)
                        sites.append(self.sid(y[0] + d1, y[1] + d2))
                        trans.append(np.exp(2j * charge * ph))
                trans = np.array(trans)
                inv = 1.0 / trans
                for a, sa in enumerate(sites):
                    for b, sb in enumerate(sites):
                        P[sa, sb] -= inv[a] * trans[b] / L**2
        return P

    def form(self):
        H = self.hess()
        Dp = self.pi0(1) @ self.dstar(1)
        Dm = self.pi0(-1) @ self.dstar(-1)
        B = H + self.tau * Dm.T @ Dp
        # X^+- := ker Q^+-
        Qp = self.Q(1)
        Qm = self.Q(-1)
        Rp = null_basis(Qp)
        Rm = null_basis(Qm)
        return Rm.T @ B @ Rp


def null_basis(Q):
    u, s, vh = np.linalg.svd(Q, full_matrices=True)
    r = int(np.sum(s > 1e-10 * s[0]))
    return vh[r:].conj().T


def smin_and_sign(L, N, alpha, imag, n1=3, qstr=True):
    m = Model(L, N, alpha, imag, n1=n1, qstr=qstr)
    H = m.hess()
    Dp = m.pi0(1) @ m.dstar(1)
    Dm = m.pi0(-1) @ m.dstar(-1)
    B = H + m.tau * Dm.T @ Dp
    Qp = m.Q(1)
    Qm = m.Q(-1)
    F = null_basis(Qm).T @ B @ null_basis(Qp)
    s = np.linalg.svd(F, compute_uv=False)
    nb = Qp.shape[0]
    K = np.block([[B, Qm.T], [Qp, np.zeros((nb, nb), dtype=complex)]])
    sign, logdet = np.linalg.slogdet(K)
    check_rss()
    return s[-1], sign, F


def run(L, N, alphas, n1=3):
    print(f"L = {L}, N = {N}, n1 = {n1}: links {2 * n1 * L * N}", flush=True)
    worst_real = 1e9
    for a in alphas:
        smin, sign, F = smin_and_sign(L, N, a, False, n1=n1)
        worst_real = min(worst_real, smin * L**2)
    print(f"  real flux: min over the grid of smin L^2 = {worst_real:.3f}", flush=True)
    prev = None
    zero = None
    best = 1e9
    for a in alphas:
        smin, sign, F = smin_and_sign(L, N, a, True, n1=n1)
        best = min(best, smin * L**2)
        if prev is not None and np.real(prev[1] * np.conj(sign)) < 0:
            zero = (prev[0], a)
            break
        prev = (a, sign)
    if zero is None:
        print(f"  imaginary flux: no sign change; min smin L^2 = {best:.4f}; sign at the end {prev[1]}", flush=True)
        return worst_real, None
    lo, hi = zero
    slo = smin_and_sign(L, N, lo, True, n1=n1)[1]
    for _ in range(25):
        mid = 0.5 * (lo + hi)
        smin, sign, F = smin_and_sign(L, N, mid, True, n1=n1)
        if smin < 1e-10:
            lo = hi = mid
            break
        if np.real(slo * np.conj(sign)) < 0:
            hi = mid
        else:
            lo, slo = mid, sign
    mid = 0.5 * (lo + hi)
    smin, sign, F = smin_and_sign(L, N, mid, True, n1=n1)
    print(f"  imaginary flux: det changes sign at alpha_c = {mid:.6f}, smin = {smin:.2e}, alpha_c N L = {mid * N * L:.3f}, max |Im connection| = {mid * N / 2:.3f}", flush=True)
    return worst_real, (mid, smin)


def log_det_K(L, N, alpha, n1=3):
    m = Model(L, N, alpha, True, n1=n1)
    H = m.hess()
    Dp = m.pi0(1) @ m.dstar(1)
    Dm = m.pi0(-1) @ m.dstar(-1)
    B = H + m.tau * Dm.T @ Dp
    Qp = m.Q(1)
    Qm = m.Q(-1)
    nb = Qp.shape[0]
    K = np.block([[B, Qm.T], [Qp, np.zeros((nb, nb), dtype=complex)]])
    sign, logdet = np.linalg.slogdet(K)
    check_rss()
    return np.log(sign) + logdet


def zero(L=3, N=72, n1=3):
    grid = np.linspace(0, 0.2 / L**2, 21)
    vals = [smin_and_sign(L, N, a, True, n1=n1)[0] for a in grid]
    i = int(np.argmin(vals))
    print(f"coarse minimum: alpha = {grid[i]:.5f}, smin L^2 = {vals[i] * L**2:.4f}", flush=True)
    lo = grid[max(i - 1, 0)]
    hi = grid[min(i + 1, len(grid) - 1)]
    fine = np.linspace(lo, hi, 60)
    prev = None
    best = (1e9, None)
    found = None
    for a in fine:
        smin, sign, F = smin_and_sign(L, N, a, True, n1=n1)
        if smin < best[0]:
            best = (smin, a)
        if prev is not None and np.real(prev[1] * np.conj(sign)) < 0:
            found = (prev[0], a)
        prev = (a, sign)
    print(f"fine scan: best smin L^2 = {best[0] * L**2:.5f} at alpha = {best[1]:.6f}; sign change: {found}", flush=True)
    if found:
        a0, a1 = found
        s0 = smin_and_sign(L, N, a0, True, n1=n1)[1]
        for _ in range(30):
            mid = 0.5 * (a0 + a1)
            smin, sign, F = smin_and_sign(L, N, mid, True, n1=n1)
            if np.real(s0 * np.conj(sign)) < 0:
                a1 = mid
            else:
                a0, s0 = mid, sign
        print(f"real zero: alpha_* = {mid:.8f}, smin = {smin:.2e}, alpha_* N L = {mid * N * L:.3f}", flush=True)
        print("PASS-ZERO" if smin < 1e-8 else "NO-ZERO")
        return
    z = complex(best[1], best[0] * 2)
    for it in range(25):
        h = 1e-6
        dl = (log_det_K(L, N, z + h, n1) - log_det_K(L, N, z - h, n1)) / (2 * h)
        step = 1.0 / dl
        z2 = z - step
        smin = smin_and_sign(L, N, z2, True, n1=n1)[0]
        print(f"newton {it}: alpha = {z2:.8f}, smin = {smin:.3e}", flush=True)
        z = z2
        if smin < 1e-9:
            break
    ok = smin < 1e-8 and abs(z) * L**2 <= 0.25
    print(f"complex zero: alpha_* = {z:.8f}, |Re F_p| = {abs(z.imag):.6f}, |Im F_p| = {abs(z.real):.6f}, alpha_* N L = {z * N * L:.3f}, smin = {smin:.2e}", flush=True)
    print("PASS-ZERO" if ok else "NO-ZERO")


def diag():
    for qstr in (False, True):
        for a in (0.0, 0.002, 0.005, 0.01, 0.02):
            smin, sign, F = smin_and_sign(3, 36, a, False, qstr=qstr)
            print(f"qstr={qstr} real alpha={a}: smin L^2 = {smin * 9:.3f}", flush=True)


def main():
    results = []
    # consistency of the Hessian: at alpha = 0 the form is Hermitian and the kernel is the known block modes
    m = Model(3, 18, 0.0, False)
    F = m.form()
    print(f"control: |F - F^H| at alpha = 0: {np.abs(F - F.conj().T).max():.2e}", flush=True)
    m = Model(3, 18, 0.04, False)
    F = m.form()
    print(f"control: |F - F^H| at real flux 0.04: {np.abs(F - F.conj().T).max():.2e}", flush=True)
    for L, N, n1, n in ((3, 72, 3, 21), (3, 108, 3, 21), (5, 140, 2, 9)):
        alphas = np.linspace(0, 0.2 / L**2, n)
        results.append(run(L, N, alphas, n1))
    print("PASS-REAL3" if all(r[0] > 2 for r in results) else "FAIL-REAL3")
    sing = [r[1] for r in results if r[1] is not None and r[1][1] < 1e-6]
    print("PASS-SING3" if len(sing) == len(results) else ("PARTIAL-SING3" if sing else "NO-SING3"))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "diag":
        diag()
    elif len(sys.argv) > 1 and sys.argv[1] == "zero":
        zero()
    else:
        main()
