"""R4-4 checks (C5 round 4): beable-sourced gravity.

[1] Free Gaussian: per-trajectory Bohmian energy, including the quantum
    potential, is not conserved; closed form dE = hbar^2 (x0^2 - s0^2)/(4 m s0^4).
[2] Signalling toy (ESSW crossing): a classical field sourced by the point
    beable X_A(t) and read by a third party through a time-integrated kick.
    Single-time marginals of X_A do not depend on Bob's setting; the
    distribution of the integrated readout does.
[3] Conditional-wave-function source: single-shot TV = 1 (R3-4 toy realised).
[4] BMV discriminator: concurrence under quantum Newtonian coupling vs a
    classical field sourced by the beables (product preserved exactly).
[5] Momentum: total beable momentum change in the reflection branch.
[6] Illustrative vacuum-noise scaling (suggested; assumption stated).
Units hbar = m = 1 in [1],[2],[5]; SI in [4],[6].
"""
import numpy as np

rng = np.random.default_rng(20261012)
print("=" * 72)
print("[1] free Gaussian: E_tot = m v^2/2 + Q along Bohmian trajectories")
hb, m, s0 = 1.0, 1.0, 1.0


def sig(t):
    return s0 * np.sqrt(1 + (hb * t / (2 * m * s0**2))**2)


def sigdot(t):
    tau = hb / (2 * m * s0**2)
    return s0 * tau**2 * t / np.sqrt(1 + (tau * t)**2)


def Etot(x0, t):
    st = sig(t)
    x = x0 * st / s0
    v = x * sigdot(t) / st
    Q = hb**2 / (4 * m * st**2) - hb**2 * x**2 / (8 * m * st**4)
    return 0.5 * m * v**2 + Q


# numerical Q from the wavefunction, as an independent check of the formula
def psi_free(x, t):
    a = s0**2 + 1j * hb * t / (2 * m)
    return (2 * np.pi)**-0.25 * np.sqrt(s0 / a) * np.exp(-x**2 / (4 * a))


def Q_num(x, t, h=1e-3):
    R = lambda y: np.abs(psi_free(y, t))
    return -hb**2 / (2 * m) * (R(x + h) - 2 * R(x) + R(x - h)) / h**2 / R(x)


for x0 in [0.0, 0.5, 1.0, 2.0]:
    Es = [Etot(x0, t) for t in [0, 1, 3, 10, 100]]
    pred = hb**2 * (x0**2 - s0**2) / (4 * m * s0**4)
    print(f"x0={x0:4.1f}  E_tot(t=0,1,3,10,100) = " + ", ".join(f"{e:+.5f}" for e in Es)
          + f"   E(100)-E(0) = {Es[-1]-Es[0]:+.5f}  closed form (t->inf) {pred:+.5f}")
xs = np.array([0.3, 1.2]); ts = np.array([0.0, 2.0])
for x0 in xs:
    for t in ts:
        st = sig(t); x = x0 * st / s0
        Qa = hb**2 / (4 * m * st**2) - hb**2 * x**2 / (8 * m * st**4)
        print(f"   Q check x0={x0}, t={t}: analytic {Qa:+.6f}  finite-diff {Q_num(x, t):+.6f}")
x0s = rng.normal(0, s0, 400000)
print(f"   ensemble mean E_tot: t=0 {Etot(x0s,0).mean():.5f}, t=100 {Etot(x0s,100).mean():.5f};"
      f" <H> = hbar^2/(8 m s0^2) = {hb**2/(8*m*s0**2):.5f}")
# physical size: nucleon, s0 = 0.1 um
hbar, mn = 1.054571817e-34, 1.67262192e-27
print(f"   scale hbar^2/(4 m s0^2) for a nucleon at s0 = 0.1 um: {hbar**2/(4*mn*(1e-7)**2):.3e} J")

print("=" * 72)
print("[2] signalling toy: classical field sourced by the point beable X_A(t)")
a, k0, sg = 8.0, 4.0, 1.0
T, dt = 4.0, 0.002


def gpk(x, t, x0, k):
    al = sg**2 + 1j * t / 2
    return (2 * np.pi)**-0.25 * np.sqrt(sg / al) * np.exp(
        -(x - x0 - k * t)**2 / (4 * al) + 1j * k * (x - x0) - 1j * k**2 * t / 2)


def dgpk(x, t, x0, k):
    al = sg**2 + 1j * t / 2
    return gpk(x, t, x0, k) * (-(x - x0 - k * t) / (2 * al) + 1j * k)


def phiL(x, t): return gpk(x, t, -a, +k0)
def phiR(x, t): return gpk(x, t, +a, -k0)
def dphiL(x, t): return dgpk(x, t, -a, +k0)
def dphiR(x, t): return dgpk(x, t, +a, -k0)


def make(cL, cR):
    f = lambda x, t: cL * phiL(x, t) + cR * phiR(x, t)
    df = lambda x, t: cL * dphiL(x, t) + cR * dphiR(x, t)
    return f, df


def vel(df, f, x, t):
    p = f(x, t)
    return np.imag(df(x, t) / p)


def sample(f, n):
    xg = np.linspace(-20, 20, 40001)
    p = np.abs(f(xg, 0.0))**2
    c = np.cumsum(p); c /= c[-1]
    return np.interp(rng.random(n), c, xg)


def run(f, df, n):
    X = sample(f, n)
    I = np.zeros(n)
    snaps = {}
    nst = int(round(T / dt))
    for i in range(nst):
        t = i * dt
        if i in (0, nst // 2):
            snaps[round(t, 3)] = X.copy()
        k1 = vel(df, f, X, t)
        k2 = vel(df, f, X + 0.5 * dt * k1, t + 0.5 * dt)
        k3 = vel(df, f, X + 0.5 * dt * k2, t + 0.5 * dt)
        k4 = vel(df, f, X + dt * k3, t + dt)
        Xn = X + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        I += 0.5 * dt * (X + Xn)
        X = Xn
    snaps[round(T, 3)] = X.copy()
    return snaps, I


n = 4000
ov = np.sum(np.conj(phiL(np.linspace(-40, 40, 80001), 0)) * phiR(np.linspace(-40, 40, 80001), 0)) * 0.001
print(f"   <phiL|phiR> at t=0: {abs(ov):.2e} (negligible; conserved in time)")
# Bob measures Z: Alice's conditional wf is phiL or phiR (prob 1/2 each)
fL, dfL = make(1, 0); fR, dfR = make(0, 1)
# Bob measures X: conditional wf (phiL +/- phiR)/sqrt(2)
fP, dfP = make(2**-0.5, 2**-0.5); fM, dfM = make(2**-0.5, -2**-0.5)
res = {}
for name, (f, df) in {"Z,L": (fL, dfL), "Z,R": (fR, dfR), "X,+": (fP, dfP), "X,-": (fM, dfM)}.items():
    res[name] = run(f, df, n // 2)
IZ = np.concatenate([res["Z,L"][1], res["Z,R"][1]])
IX = np.concatenate([res["X,+"][1], res["X,-"][1]])
for tt in sorted(res["Z,L"][0]):
    XZ = np.concatenate([res["Z,L"][0][tt], res["Z,R"][0][tt]])
    XX = np.concatenate([res["X,+"][0][tt], res["X,-"][0][tt]])
    hZ, e = np.histogram(XZ, bins=40, range=(-14, 14)); hX, _ = np.histogram(XX, bins=e)
    print(f"   t={tt:4.1f}: single-time marginal of X_A  mean Z {XZ.mean():+.3f} X {XX.mean():+.3f};"
          f"  <x^2> Z {np.mean(XZ**2):7.3f} X {np.mean(XX**2):7.3f};  TV(hist) {0.5*np.abs(hZ-hX).sum()/n:.3f}")
cross_Z = np.mean(np.sign(res['Z,L'][0][0.0]) != np.sign(res['Z,L'][0][T]))
cross_X = np.mean(np.sign(res['X,+'][0][0.0]) != np.sign(res['X,+'][0][T]))
print(f"   fraction of trajectories that change side 0->T: Z-branch {cross_Z:.3f}, X-branch {cross_X:.3f}")
print(f"   readout I = int_0^T X_A dt:  Z: mean {IZ.mean():+.3f} sd {IZ.std():.3f};"
      f"  X: mean {IX.mean():+.3f} sd {IX.std():.3f}")
hZ, e = np.histogram(IZ, bins=60, range=(-40, 40)); hX, _ = np.histogram(IX, bins=e)
print(f"   TV distance between the readout distributions (histogram): {0.5*np.abs(hZ-hX).sum()/n:.3f}")
# Charlie: test packet of width w kicked by kappa*I; final position ~ N(kappa*I*tau, w^2)
for kap in [0.01, 0.05, 0.2, 1.0]:
    yg = np.linspace(-60, 60, 6001); w = 1.0
    pZ = np.mean(np.exp(-(yg[:, None] - kap * IZ[None, :])**2 / (2 * w**2)), axis=1)
    pX = np.mean(np.exp(-(yg[:, None] - kap * IX[None, :])**2 / (2 * w**2)), axis=1)
    pZ /= pZ.sum(); pX /= pX.sum()
    print(f"   Charlie (shift kappa*I, width 1): kappa={kap:5.2f}  TV(Z vs X) = {0.5*np.abs(pZ-pX).sum():.3f}")

# control: same setting (Z) twice, independent samples -> sampling-noise floor of the TV figures
resZ2 = {k: run(*fg, n // 2) for k, fg in {"L": (fL, dfL), "R": (fR, dfR)}.items()}
IZ2 = np.concatenate([resZ2["L"][1], resZ2["R"][1]])
h1, e = np.histogram(IZ, bins=60, range=(-40, 40)); h2, _ = np.histogram(IZ2, bins=e)
XZa = np.concatenate([res["Z,L"][0][T], res["Z,R"][0][T]]); XZb = np.concatenate([resZ2["L"][0][T], resZ2["R"][0][T]])
g1, e2 = np.histogram(XZa, bins=40, range=(-14, 14)); g2, _ = np.histogram(XZb, bins=e2)
print(f"   control (Z vs independent Z): readout TV {0.5*np.abs(h1-h2).sum()/n:.3f}; t=T marginal TV {0.5*np.abs(g1-g2).sum()/n:.3f}  (noise floor)")

print("=" * 72)
print("[3] conditional-wave-function source (R3-4 E1 toy realised exactly)")
print("   Bob Z: Alice's conditional wf = phiL or phiR -> sourced field g_L or g_R (p=1/2 each)")
print("   Bob X: conditional wf = (phiL +/- phiR)/sqrt2 -> <T> has half the mass in each packet -> g_mean")
print("   field distributions {1/2 d(gL) + 1/2 d(gR)} vs {d(gmean)}: TV = 1 (single shot)")

print("=" * 72)
print("[4] BMV discriminator (parameters as recalled for Bose et al. 2017)")
G = 6.674e-11
mB, dx, d, tB = 1e-14, 250e-6, 450e-6, 2.5
# masses 1 and 2, each in |L>,|R>; separations between branch positions
# geometry: 1 at {0, dx}, 2 at {d+dx... } use simple collinear layout as recalled:
# closest approach d - dx ... take branch distances r_LL=d, r_RL=d+dx, r_LR=d-dx, r_RR=d
r = {("L", "L"): d, ("R", "R"): d, ("R", "L"): d - dx, ("L", "R"): d + dx}
ph = {k: G * mB**2 * tB / (hbar * v) for k, v in r.items()}
amp = np.array([np.exp(1j * ph[("L", "L")]), np.exp(1j * ph[("L", "R")]),
                np.exp(1j * ph[("R", "L")]), np.exp(1j * ph[("R", "R")])]) / 2
psi = amp.reshape(2, 2)
conc = 2 * abs(psi[0, 0] * psi[1, 1] - psi[0, 1] * psi[1, 0])
print(f"   quantum Newtonian coupling: branch phases (rad) "
      + ", ".join(f"{k[0]}{k[1]}:{v:.3f}" for k, v in ph.items()) + f";  concurrence {conc:.3f}")
# classical field sourced by the actual beables: mass 1's wf evolves under the potential of
# mass 2's actual position (and vice versa). Product state stays product: concurrence 0 exactly.
for X2 in ["L", "R"]:
    for X1 in ["L", "R"]:
        p1 = np.array([np.exp(1j * G * mB**2 * tB / (hbar * r[(s, X2)])) for s in "LR"]) / np.sqrt(2)
        p2 = np.array([np.exp(1j * G * mB**2 * tB / (hbar * r[(X1, s)])) for s in "LR"]) / np.sqrt(2)
        P = np.outer(p1, p2)
        c = 2 * abs(P[0, 0] * P[1, 1] - P[0, 1] * P[1, 0])
        print(f"   beable-sourced classical field, actual (X1,X2)=({X1},{X2}): concurrence {c:.2e}")

print("=" * 72)
print("[5] beable momentum in the reflection (X) branch: p = v (m=1)")
f, df = fP, dfP
X0 = sample(f, 2000)
sn, _ = run(f, df, 2000)
vi = vel(df, f, sn[0.0], 0.0); vf = vel(df, f, sn[T], T)
print(f"   X+ branch: mean beable momentum t=0 {vi.mean():+.3f}, t=T {vf.mean():+.3f};"
      f"  per-trajectory <|p_f - p_i|> = {np.mean(np.abs(vf-vi)):.3f}  (k0 = {k0})")
print(f"   left-starting trajectories: p_i mean {vi[sn[0.0]<0].mean():+.3f} -> p_f mean {vf[sn[0.0]<0].mean():+.3f}")
print("   (Alice's beable reverses its momentum with no local partner: the total beable")
print("    momentum of the isolated free pair changes per realization; dP/dt = -sum grad Q)")

print("=" * 72)
print("[6] illustrative quenched-vacuum noise (SUGGESTED; assumption n_v ~ alpha*Lambda^3)")
c0 = 2.99792458e8; me = 9.109e-31; alpha = 1 / 137.036
lP = 1.616e-35; L = 3.086e25  # 1 Gpc
for name, lam in [("Planck cutoff", 1 / lP), ("1 TeV cutoff", 1.602e-7 / (hbar * c0))]:
    nv = alpha * lam**3
    dPhi = G * me / c0**2 * np.sqrt(nv * L)
    print(f"   {name}: n_v = {nv:.2e} m^-3, white-noise dPhi/c^2 at 1 Gpc ~ (G m_e/c^2) sqrt(n_v L) = {dPhi:.2e}")
print("=" * 72)
print("[7] active mass from the beable stress alone (no quantum-potential stress)")
# hydrogen 1s: real wavefunction -> Bohmian velocity 0; beable energy = m + V(r_actual)
a0 = 5.29177e-11; Ry = 13.6057
rs = rng.gamma(3, a0 / 2, 2_000_000)   # r ~ r^2 exp(-2r/a0)
V = -2 * Ry * a0 / rs
print(f"   H 1s: E[V(r_actual)] = {V.mean():.3f} eV (2E0 = {-2*Ry:.3f}); sd {V.std():.2f} eV per atom")
print(f"   beable-sourced active energy - inertial energy = E[V] - E0 = {V.mean()+Ry:.3f} eV per atom"
      f" = {abs(V.mean()+Ry)/938.78e6:.2e} of m_H")
# composition dependence from the electronic shells (Thomas-Fermi binding ~ 20.8 Z^(7/3) eV, RECALLED;
# virial: missing beable kinetic energy = |E_bind| for closed-shell real ground states)
mu = 931.494e6
for nm, Z, A in [("Al", 13, 27), ("Fe", 26, 56), ("Pt", 78, 195), ("Be", 4, 9), ("Ti", 22, 48)]:
    Eb = 20.8 * Z**(7/3)
    print(f"   {nm}: TF electronic binding {Eb/1e3:7.2f} keV/atom; missing fraction {Eb/(A*mu):.2e}")
dAlFe = 20.8 * (26**(7/3)/56 - 13**(7/3)/27) / mu
print(f"   Fe - Al difference of active/passive ratio (electrons only, estimate): {dAlFe:.2e}"
      f"  vs LLR bound 4e-12 (1986) / 3.9e-14 (2023): margin {np.log10(dAlFe/3.9e-14):.1f} decades")
print("done")
