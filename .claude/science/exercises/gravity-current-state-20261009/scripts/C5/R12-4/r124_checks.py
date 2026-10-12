#!/usr/bin/env python3
"""C5 R12-4 checks: one cone no-go for classical metric records across the CQ classes.

Sections
 [1] felt-field product bound  sigma_bar * P_bar >= |C|^2/4  (any correlation), random unsymmetrized spectra
 [2] same bound from Wightman positivity in a random finite-dimensional NON-Gaussian stationary system
 [3] Gaussian QMFS meter (single shell): self-commuting record, zero reverse gain, product bound attained
 [4] cone non-integrability: product of truncated integrals >= (2 ln(delta/s_min))^2 kappa ; profiles
 [5] frame-tied 4D check: local finiteness of 1/|omega^2-k^2| near a regular null point (Jacobian)
 [6] stationary escape with damped G (frame friction gamma): both integrals finite, L = 2 asinh(delta/(gamma w))
 [7] Lorentz-invariant log self-energy does not regulate the cone: int |G| ds ~ ln ln
 [8] numbers: L for gamma = H0 and finite age; GW amplitude loss over distance; phase-velocity shift
Subtraction: none in every section (positive integrands / spectral densities only).
"""
import numpy as np
from math import log, asinh, pi
rng = np.random.default_rng(20261012)

def psd2(rng):
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    return A @ A.conj().T

print("[1] felt-field product bound, random unsymmetrized (f,J) spectra at +p and -p")
print("    convention: S_XY(w)=int e^{iwt}<X(t)Y(0)>, Hermitian PSD; C_XY(w)=S_XY(w)-S_YX(-w)")
N = 200000
ratios = []
subfloor = 0
for _ in range(N):
    Sp = psd2(rng); Sm = psd2(rng)
    # self-commuting record: S_JJ(p) = S_JJ(-p). Rescale J-row/col of Sm to match (keeps PSD).
    a = np.sqrt(Sp[1, 1].real / Sm[1, 1].real)
    D = np.diag([1.0, a]); Sm = D @ Sm @ D
    C = Sp[0, 1] - np.conj(Sm[0, 1])          # C_fJ(p) = S_fJ(p) - S_Jf(-p) = S_fJ(p) - conj(S_fJ(-p))
    sig = 0.5 * (Sp[0, 0].real + Sm[0, 0].real)
    P = Sp[1, 1].real
    ratios.append(sig * P / (abs(C) ** 2 / 4))
ratios = np.array(ratios)
print(f"    draws={N}  min ratio sigma_bar*P/(|C|^2/4) = {ratios.min():.6f}  (>=1 required)  violations={np.sum(ratios<1-1e-12)}")
# attainment: S(p) = S(-p)^T-type rank-one with aligned phases
x = 0.7; P = 2.3
Sp = np.array([[x * x, x * np.sqrt(P)], [x * np.sqrt(P), P]], complex)   # rank one
Sm = np.array([[x * x, -x * np.sqrt(P)], [-x * np.sqrt(P), P]], complex)
C = Sp[0, 1] - np.conj(Sm[0, 1]); sig = 0.5 * (Sp[0, 0] + Sm[0, 0]).real
print(f"    explicit equality case: ratio = {sig*P/(abs(C)**2/4):.12f}")
# correlation allows total felt noise far below the ADDITIVE floor |G||C| (R9-4 sub-floor), product bound intact
G = 5.0; Cmag = 1.0
for Pj in [1.0, 10.0, 100.0]:
    sig_min = Cmag ** 2 / (4 * Pj)
    print(f"    P={Pj:6.1f}: min felt noise allowed = {sig_min:.4e}; additive floor |G||C| = {G*Cmag:.1f}; ratio {sig_min/(G*Cmag):.2e}; M=|G|^2P={G*G*Pj:.1f}; sigma*M/(|G|^2|C|^2/4)={sig_min*G*G*Pj/(G*G*Cmag**2/4):.3f}")

print("\n[2] non-Gaussian finite-dimensional stationary system: |C_XY(w)| <= 2 sqrt(sbar_X sbar_Y) per frequency bin")
worst = np.inf; nviol = 0; ntest = 0
for trial in range(60):
    d = 7
    H = rng.normal(size=(d, d)); H = H + H.T
    E, V = np.linalg.eigh(H)
    pz = rng.random(d); pz /= pz.sum()              # arbitrary stationary (non-thermal, non-Gaussian) state
    X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)); X = X + X.conj().T
    Y = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)); Y = Y + Y.conj().T
    Xe = V.T @ X @ V; Ye = V.T @ Y @ V
    # S_XY(w) = sum_{mn} p_m X_mn Y_nm delta(w - (E_n - E_m))  (Bohr frequencies)
    bins = np.linspace(-15, 15, 41)
    def spec(A, B):
        out = np.zeros(len(bins) - 1, complex)
        for m in range(d):
            for n in range(d):
                w = E[n] - E[m]
                k = np.searchsorted(bins, w) - 1
                if 0 <= k < len(out):
                    out[k] += pz[m] * A[m, n] * B[n, m]
        return out
    SXX = spec(Xe, Xe).real; SYY = spec(Ye, Ye).real; SXY = spec(Xe, Ye); SYX = spec(Ye, Xe)
    nb = len(SXX)
    for k in range(nb):
        km = nb - 1 - k                              # bin of -w (symmetric bins)
        C = SXY[k] - SYX[km]
        sx = 0.5 * (SXX[k] + SXX[km]); sy = 0.5 * (SYY[k] + SYY[km])
        if abs(C) > 1e-12:
            r = 2 * np.sqrt(max(sx, 0) * max(sy, 0)) / abs(C)
            worst = min(worst, r); ntest += 1
            if r < 1 - 1e-9: nviol += 1
print(f"    bins tested={ntest}  min [2 sqrt(sx sy)/|C|] = {worst:.6f}  violations={nviol}")

print("\n[3] Gaussian QMFS meter on one frequency shell (R10-3 Lemma D form), exact correlators")
# modes a (H=+w a^dag a), b (H=-w b^dag b), both in vacuum. J = x_a + x_b, B_theta = cos(th) p_a + sin(th) p_b (generic)
# Heisenberg: x_a(t)=x cos wt + p sin wt; x_b(t)=x_b cos wt - p_b sin wt; vacuum <x x>=<p p>=1/2, <x p>=i/2 (a), for b-sector
# b with H=-w b^dag b in its 'vacuum' |0_b>: <x_b p_b> = i/2 still (state), dynamics reversed.
w = 1.0
def corr_xa(t):  # <x_a(t) x_a(0)> = 1/2 e^{-iwt}
    return 0.5 * np.exp(-1j * w * t)
def corr_xb(t):  # reversed dynamics -> 1/2 e^{+iwt}
    return 0.5 * np.exp(1j * w * t)
ts = np.linspace(0, 20, 2001)
JJ = corr_xa(ts) + corr_xb(ts)
comm_JJ = JJ - np.conj(JJ)
print(f"    max |<[J(t),J(0)]>| = {np.max(np.abs(comm_JJ)):.2e}  (self-commuting record)")
print(f"    <J(t)J(0)> = cos(wt): max dev {np.max(np.abs(JJ-np.cos(w*ts))):.2e}  -> symmetric spectrum P(w)=P(-w)")
# spectral weights at +-w: x_a contributes 1/2 at w>0? convention e^{iwt}: <x_a(t)x_a(0)>=1/2 e^{-iwt} -> weight at omega=+w
# Felt field f = alpha x_a + beta x_b (Hermitian combination of the record sectors), J = x_a + x_b.
for (al, be) in [(1.0, 0.0), (1.0, 0.3), (0.5, -0.5), (1.0, 1.0)]:
    Sff_p = 0.5 * al * al; Sff_m = 0.5 * be * be     # x_a weight at +w, x_b weight at -w
    SfJ_p = 0.5 * al; SfJ_m = 0.5 * be
    P = 0.5
    C = SfJ_p - SfJ_m                                  # C_fJ(+w) = S_fJ(+w) - S_Jf(-w)
    sig = 0.5 * (Sff_p + Sff_m)
    rr = sig * P / (abs(C) ** 2 / 4) if abs(C) > 0 else np.inf
    print(f"    f={al:+.1f}x_a{be:+.1f}x_b : emission weight S_ff(-w)={Sff_m:.3f}  |C|={abs(C):.3f}  sigma_bar*P/(|C|^2/4)={rr:.4f}")

print("\n[4] cone non-integrability: product of truncated integrals over s_min<|s|<delta (one side)")
kap = 0.25; delta = 1.0
profiles = {
    'floor split  P=|s|      (M~1/|s|, sig~1/|s|)': lambda s: s,
    'record-light P=|s|^1.5  (M integrable)      ': lambda s: s ** 1.5,
    'matter-light P=|s|^0.5  (sig integrable)    ': lambda s: s ** 0.5,
    'log split    P=|s|ln^2  (M integrable)      ': lambda s: s * np.log(np.e / s) ** 2,
    'eps-band     P=eps*|s| (|s|<1e-3) else |s|  ': lambda s: np.where(s < 1e-3, 1e-4 * s, s),
}
g = 1.0
for name, Pf in profiles.items():
    row = []
    for smin in [1e-4, 1e-8, 1e-16, 1e-32]:
        u = np.linspace(np.log(smin), np.log(delta), 200001); s = np.exp(u)
        P = Pf(s); sig = kap / P; M = g * g * P / s ** 2
        Is = np.trapezoid(sig * s, u); IM = np.trapezoid(M * s, u)
        bound = kap * g * g * (np.log(delta / smin)) ** 2
        row.append((smin, Is, IM, Is * IM / bound))
    print("    " + name + "  " + "  ".join(f"[smin={a:.0e}: Isig={b:.3g} IM={c:.3g} prod/bound={d:.3f}]" for a, b, c, d in row))

print("\n[5] frame-tied 4D: local finiteness of d^4p/|s| near a regular null point (w0,k0)=(1,(1,0,0)), no Lorentz invariance used")
nmc = 2000000
pts = rng.uniform(-0.1, 0.1, size=(nmc, 4)); pts[:, 0] += 1.0; pts[:, 1] += 1.0
s = pts[:, 0] ** 2 - (pts[:, 1] ** 2 + pts[:, 2] ** 2 + pts[:, 3] ** 2)
V = 0.2 ** 4
for x in [1e-1, 1e-2, 1e-3]:
    fr = np.mean(np.abs(s) < x)
    print(f"    vol fraction |s|<{x:.0e} = {fr:.4e}; fraction/(2x) = {fr/(2*x):.4f}  (constant => s is a local coordinate, density rho_s(0) finite > 0)")
rho0 = np.mean(np.abs(s) < 1e-2) / 2e-2
for eta in [1e-2, 1e-4, 1e-8, 1e-16]:
    I = V * rho0 * 2 * np.log(0.05 / eta)
    print(f"    eta={eta:.0e}: int_(eta<|s|<0.05) d^4p/|s| ~ V rho_s(0) 2 ln(0.05/eta) = {I:.4e}  (diverges as eta->0)")
mc = np.mean(np.where((np.abs(s) > 1e-4) & (np.abs(s) < 0.05), 1/np.abs(s), 0.0)) * V
print(f"    direct MC eta=1e-4: {mc:.4e} vs shell estimate {V*rho0*2*np.log(0.05/1e-4):.4e}")

print("\n[6] stationary escape: frame friction gamma in G = g/(s + i gamma w), saturated split, both finite")
w0 = 1.0
for gam in [1e-2, 1e-6, 1e-12, 1e-30]:
    u = np.linspace(-80, np.log(delta), 400001); s = np.exp(u)
    mod2 = g * g / (s ** 2 + (gam * w0) ** 2)
    a = 1.0
    P = a * np.sqrt(s ** 2 + (gam * w0) ** 2)          # record noise
    sig = kap / P                                      # felt noise at the product bound
    M = mod2 * P
    Is = 2 * np.trapezoid(sig * s, u); IM = 2 * np.trapezoid(M * s, u)   # both sides of the cone
    L = 2 * asinh(delta / (gam * w0))
    print(f"    gamma*w={gam*w0:.0e}: Isig={Is:.4f}  IM={IM:.4f}  2asinh(delta/gw)={L:.4f}  Isig/(kap*L)={Is/(kap*L):.4f} IM/(g^2 a L)={IM/(g*g*a*L):.4f}")

print("\n[7] Lorentz-invariant dressings of the massless pole near s=0 (one side, s in (s_min, 1))")
print("    (a) Maxwell-type stress loop Pi ~ c s^2 ln|s|: G = g/(s - g c s^2 ln|s|); |G| s -> g")
for smin in [1e-4, 1e-16, 1e-64]:
    s = smin; Gs = 1.0 / abs(1 - 0.1 * s * np.log(s))
    print(f"        s={s:.0e}: |G|*|s|/g = {Gs:.12f}  -> pole intact, int|G| ~ ln(1/s_min) = {np.log(1/smin):.1f}")
print("    (b) field-strength log, |G| = g/(|s|(1+alpha ln(1/|s|))): int|G| = ln(1+alpha ln(1/s_min))/alpha (ln ln divergence)")
for alpha in [1e-1, 1e-2]:
    vals = []
    for lnin in [23.0, 92.1, 368.4, 1473.7]:
        T = lnin
        t = np.linspace(0, T, 400001)
        num = np.trapezoid(1 / (1 + alpha * t), t)
        vals.append(f"ln(1/s_min)={lnin:.0f}: num={num:.4f} exact={np.log(1+alpha*T)/alpha:.4f}")
    print(f"        alpha={alpha:.0e}: " + "; ".join(vals))
print("    (c) absorptive threshold Im Sigma(0+) = c != 0 (Kramers-Kronig Re Sigma ~ (c/pi) ln|s|): pole destroyed, |G| ~ pi g/(c |ln|s||)")
for smin in [1e-4, 1e-16, 1e-64]:
    T = np.log(1 / smin); t = np.linspace(np.log(1/0.5), T, 400001)  # s from 0.5 down to s_min, ds = s dt
    s = np.exp(-t)
    G = 1.0 / np.abs(s - (1/np.pi) * np.log(s) - 1j)
    print(f"        s_min={smin:.0e}: int|G|^2 ds = {np.trapezoid(G**2 * s, t):.5f} (finite) ; |G|*|s| at s_min = {G[-1]*s[-1]:.2e} (no 1/s pole -> no standard radiation zone; fails (R))")

print("\n[8] numbers")
c = 2.998e8; H0 = 2.2e-18; tH = 4.35e17; Mpc = 3.086e22
for ell in [1e-8, 2e-7, 1e-6, 5e-6]:
    w = c / ell
    print(f"    ell={ell:.0e} m: w=c/ell={w:.2e} s^-1  L_damp(gamma=H0)=ln(2w/H0)={np.log(2*w/H0):.1f}  L_age=ln(w tH)={np.log(w*tH):.1f}")
wL = 2 * pi * 100
print(f"    LIGO band 100 Hz: ln(2w/H0)={np.log(2*wL/H0):.1f}")
for D in [40, 1000, 3000]:
    loss = 1 - np.exp(-H0 * D * Mpc / c / 2)
    print(f"    gamma=H0: GW amplitude loss over {D} Mpc = {loss:.3%}")
print(f"    gamma=H0, 100 Hz: phase-velocity shift ~ gamma^2/(8 w^2) = {H0**2/(8*wL**2):.1e}")
