"""F1 corroboration of Theorem T1 (not the proof; vectorized): for the strictly local K2 scalar
shell A = sum(2-2cos k) + m^2 on Z^4, search over IR-normalized odd hypercubic-covariant
translation symbols f of range <= r (family f_mu = sum_j a_j sin(j k_mu)
+ sum_{j,l} B_jl sin(j k_mu) * mean_{nu!=mu} cos(l k_nu)) and a free structure constant c,
minimizing tangency + closure residuals of the BV-forced first-moment rotations on complex shell
points.  T1: the minimum is never 0 for any r.  SLAC (f = k, A = k^2 + m^2) gives exactly 0.
"""
import numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(7)
m2 = 0.75
def shell_points(N, scale):
    ks = rng.uniform(-scale, scale, (N, 3))
    rhs = m2 + np.sum(2 - 2*np.cos(ks), axis=1)
    k0 = 1j*np.arccosh(1 + rhs/2)
    return np.column_stack([k0, ks.astype(complex)])
Js = []
for x in range(4):
    for y in range(x+1, 4):
        J = np.zeros((4, 4)); J[x, y] = 1; J[y, x] = -1; Js.append(J)
Js = np.array(Js)                                    # (6,4,4)
def fD(K, a, B, r):
    N = K.shape[0]; f = np.zeros((N, 4), complex); Df = np.zeros((N, 4, 4), complex)
    for mu in range(4):
        oth = [nu for nu in range(4) if nu != mu]
        for j in range(1, r+1):
            s, cj = np.sin(j*K[:, mu]), j*np.cos(j*K[:, mu])
            f[:, mu] += a[j-1]*s; Df[:, mu, mu] += a[j-1]*cj
            for l in range(1, r+1):
                cs = sum(np.cos(l*K[:, nu]) for nu in oth)/3
                f[:, mu] += B[j-1, l-1]*s*cs; Df[:, mu, mu] += B[j-1, l-1]*cj*cs
                for nu in oth:
                    Df[:, mu, nu] += -B[j-1, l-1]*s*l*np.sin(l*K[:, nu])/3
    return f, Df
def unpack(p, r):
    a = np.zeros(r); a[1:] = p[:r-1]; B = p[r-1:r-1+r*r].reshape(r, r); c = p[-1]
    a[0] = 1 - sum(j*a[j-1] for j in range(2, r+1)) - sum(j*B[j-1, l-1] for j in range(1, r+1) for l in range(1, r+1))
    return a, B, c
def resid(p, K, r):
    a, B, c = unpack(p, r)
    f, Df = fD(K, a, B, r); gA = 2*np.sin(K)
    nf = np.linalg.norm(f, axis=1)[:, None] + 1e-12; ng = np.linalg.norm(gA, axis=1)[:, None]
    Jf = np.einsum('jab,nb->nja', Js, f)                       # (N,6,4)
    tang = np.einsum('nja,na->nj', Jf, gA)/(nf*ng)
    clo = (np.einsum('nab,njb->nja', Df, Jf) - c*Jf)/nf[:, :, None]
    out = np.concatenate([tang.ravel(), clo.ravel()])
    return np.concatenate([out.real, out.imag])
for scale, label in ((np.pi, "full zone"), (0.6, "IR-ish |k_spatial|<0.6")):
    K = shell_points(40, scale)
    for r in (1, 2, 3):
        best = None
        for trial in range(4):
            p0 = np.concatenate([rng.normal(0, 0.1, r-1), rng.normal(0, 0.1, r*r), [1.0]])
            sol = least_squares(resid, p0, args=(K, r), xtol=1e-13, ftol=1e-13, max_nfev=300)
            rms = np.sqrt(np.mean(sol.fun**2))
            if best is None or rms < best[0]: best = (rms, sol.x[-1])
        print(f"{label:24s} r={r}: min rms residual = {best[0]:.3e} (best c = {best[1]:.3f})", flush=True)
K = rng.uniform(-np.pi, np.pi, (40, 3)); k0 = 1j*np.sqrt(m2 + np.sum(K**2, axis=1)); K = np.column_stack([k0, K])
Jf = np.einsum('jab,nb->nja', Js, K)
print(f"SLAC control (f = k, A = k^2 + m^2): max |tangency| = {np.abs(np.einsum('nja,na->nj', Jf, 2*K)).max():.1e}, "
      f"max |closure| = {np.abs(Jf - Jf).max():.1e} (Df = I)")

print("\nWith the structure constant fixed to the e(4) value c = 1 (gravity's Killing algebra):", flush=True)
def resid1(p, K, r):
    return resid(np.concatenate([p, [1.0]]), K, r)
for scale, label in ((np.pi, "full zone"), (0.6, "IR-ish |k_spatial|<0.6"), (0.25, "deep IR |k_spatial|<0.25")):
    K = shell_points(40, scale)
    for r in (1, 2, 3):
        best = None
        for trial in range(4):
            p0 = np.concatenate([rng.normal(0, 0.1, r-1), rng.normal(0, 0.1, r*r)])
            sol = least_squares(resid1, p0, args=(K, r), xtol=1e-13, ftol=1e-13, max_nfev=300)
            rms = np.sqrt(np.mean(sol.fun**2))
            if best is None or rms < best: best = rms
        print(f"{label:26s} r={r}: min rms residual (c=1) = {best:.3e}", flush=True)
print("(c = 0 near-solutions above on a small patch are the Carroll branch [L,P]=0, not e(4); T1 excludes it globally")
print(" unless A depends on one linear combination of k.)")
