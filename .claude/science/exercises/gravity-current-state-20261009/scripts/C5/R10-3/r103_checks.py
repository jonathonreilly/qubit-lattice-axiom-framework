#!/usr/bin/env python3
"""C5 R10-3 checks (worker, Opus 5.5): the emission-cancelled classical-quantum hybrid.
Every number in R10-3_report.md comes from here.  hbar = 1 unless stated; g = coupling in G(p) = -g/s.
Sections:
 [1] explicit spectral matrices of model M_E at a timelike p (emission-silent, minimal) and a
     spacelike p (additive at the floor); PSD, commutator identity, classical record, S_ff values
 [2] general bound S_ff(p)+S_ff(-p) >= |F|^2/(2P) over random constrained spectral matrices
 [3] FDT identity of the closed loop: C_ff = C_BB - 2 Im(G F), so Im R = -C_ff/2 (random data)
 [4] QMFS operator realisation (positive + negative energy oscillator); emission silence => f has no b part
 [5] Theorem P (null-cone dichotomy): int rho ds and int |G|^2 P ds near s -> 0+ for P ~ s^a
 [6] secular pumping of an on-shell record mode by a noise with P(s) ~ |s|^a near the cone
 [7] forced tower: static potential correction dV/V_N(r) for rho = (lam g/pi)/(s+mu^2); ISL numbers
 [8] absorption: atomic quadrupole graviton-like rate (order of magnitude) and the tower factor
 [9] BMV: timelike-sector leakage factor; two-qubit LOCC check with the tower covered by classical noise
"""
import numpy as np
from scipy import integrate, linalg

rng = np.random.default_rng(103)

def psd_min(M):
    return np.linalg.eigvalsh((M + M.conj().T) / 2).min()

# ---------------------------------------------------------------- [1]
print("[1] model M_E at fixed p: S(p) = [[S_BB, S_BJ],[S_JB, S_JJ]], S_ff = S_BB + G S_JB + conj(G) S_BJ + |G|^2 S_JJ")
def Sff(S, G):
    return (S[0, 0] + G * S[1, 0] + np.conj(G) * S[0, 1] + abs(G) ** 2 * S[1, 1]).real
worst = dict(psd=np.inf, comm=0.0, emit=0.0, absr=0.0)
for t in range(20000):
    G = (rng.normal() + 1j * rng.normal()) * rng.uniform(0.1, 10)  # G(p); G(-p) = conj(G)
    F = rng.normal() + 1j * rng.normal()                              # forward gain at p; F(-p) = conj(F)
    P = rng.uniform(0.01, 10)                                         # record spectrum, S_JJ(p) = S_JJ(-p) = P
    # emission side (-p): rank one, null vector of f(-p) = B + G(-p) J  => S_JB(-p) = -G(p) P
    SJB_m = -G * P
    Sm = np.array([[abs(G) ** 2 * P, np.conj(SJB_m)], [SJB_m, P]])
    # absorption side (p): commutator identity S_JB(p) - conj(S_JB(-p)) = i F; minimal S_BB
    SJB_p = 1j * F + np.conj(SJB_m)
    Sp = np.array([[abs(SJB_p) ** 2 / P, np.conj(SJB_p)], [SJB_p, P]])
    worst['psd'] = min(worst['psd'], psd_min(Sm) / P, psd_min(Sp) / P)
    worst['comm'] = max(worst['comm'], abs((SJB_p - np.conj(SJB_m)) - 1j * F))
    worst['emit'] = max(worst['emit'], abs(Sff(Sm, np.conj(G))) / (abs(G) ** 2 * P))
    worst['absr'] = max(worst['absr'], abs(Sff(Sp, G) / (abs(F) ** 2 / P) - 1))
print(f"    20000 random (G, F, P): min eig/P = {worst['psd']:.2e} (>= 0 up to rounding); "
      f"max |commutator error| = {worst['comm']:.1e}")
print(f"    emission side S_ff(-p)/(|G|^2 P) max = {worst['emit']:.1e} (silent);  absorption S_ff(p) = |F|^2/P to {worst['absr']:.1e}")
# spacelike p: G real, F real; additive (symmetrised B-J correlation zero) at the AM-GM floor
G, F = -2.7, 0.8
P = abs(F) / (2 * abs(G)); SBB = abs(G) * abs(F) / 2
for sgn in (+1, -1):
    SJB = 1j * F / 2
    S = np.array([[SBB, np.conj(SJB)], [SJB, P]])
    print(f"    spacelike {'+p' if sgn > 0 else '-p'}: min eig = {psd_min(S):+.3e}, S_ff = {Sff(S, G):.6f}, floor |G||F| = {abs(G)*abs(F):.6f}")

# ---------------------------------------------------------------- [2]
print("\n[2] general bound sigma = S_ff(p) + S_ff(-p) >= |F|^2/(2P) for any correlation (random constrained draws)")
mn = np.inf
for t in range(50000):
    G = (rng.normal() + 1j * rng.normal()) * rng.uniform(0.1, 10)
    F = rng.normal() + 1j * rng.normal(); P = rng.uniform(0.01, 10)
    SJB_m = (rng.normal() + 1j * rng.normal()) * rng.uniform(0, 5)
    SJB_p = 1j * F + np.conj(SJB_m)
    SBB_m = abs(SJB_m) ** 2 / P + rng.exponential(1.0) * rng.uniform(0, 1)
    SBB_p = abs(SJB_p) ** 2 / P + rng.exponential(1.0) * rng.uniform(0, 1)
    Sm = np.array([[SBB_m, np.conj(SJB_m)], [SJB_m, P]]); Sp = np.array([[SBB_p, np.conj(SJB_p)], [SJB_p, P]])
    sig = Sff(Sp, G) + Sff(Sm, np.conj(G))
    mn = min(mn, sig / (abs(F) ** 2 / (2 * P)))
print(f"    min sigma / (|F|^2/2P) over 50000 draws = {mn:.6f}  (bound attained at a = -conj(b) = iF/2)")
G = 1.7 - 0.4j; F = 0.9 + 0.2j; P = 0.37
SJB_p = 1j * F / 2 - np.conj(G) * P; SJB_m = 1j * np.conj(F) / 2 - G * P   # a = iF/2, b = i conj(F)/2 (so a - conj(b) = iF)
Sp = np.array([[abs(SJB_p) ** 2 / P, np.conj(SJB_p)], [SJB_p, P]]); Sm = np.array([[abs(SJB_m) ** 2 / P, np.conj(SJB_m)], [SJB_m, P]])
print(f"    attained case: commutator err = {abs(SJB_p - np.conj(SJB_m) - 1j*F):.1e}, sigma/(|F|^2/2P) = {(Sff(Sp, G) + Sff(Sm, np.conj(G)))/(abs(F)**2/(2*P)):.6f}")

# ---------------------------------------------------------------- [3]
print("\n[3] closed-loop FDT: C_ff = C_BB + G C_JB + conj(G) C_BJ with C_JB = iF, C_BJ = -i conj(F)")
err = 0.0
for t in range(10000):
    G = rng.normal() + 1j * rng.normal(); F = rng.normal() + 1j * rng.normal(); CBB = rng.normal()
    Cff = CBB + G * 1j * F + np.conj(G) * (-1j * np.conj(F))
    err = max(err, abs(Cff - (CBB - 2 * np.imag(G * F))))
    # Im R with R = chi_BB + G F and Im chi_BB = -C_BB/2 :
    ImR = -CBB / 2 + np.imag(G * F)
    err = max(err, abs(ImR - (-Cff.real / 2)), abs(Cff.imag))
print(f"    max error of C_ff = C_BB - 2Im(GF) and Im R = -C_ff/2 over 10000 draws: {err:.1e}")

# ---------------------------------------------------------------- [4]
print("\n[4] QMFS realisation at one frequency: H = w(a^dag a - b^dag b), state |0_a,0_b>, J = x_a + x_b")
N = 24; w = 1.0
a1 = np.diag(np.sqrt(np.arange(1, N)), 1)
I = np.eye(N)
a = np.kron(a1, I); b = np.kron(I, a1)
H = w * (a.conj().T @ a - b.conj().T @ b)
xa = (a + a.conj().T) / np.sqrt(2); pa = (a - a.conj().T) / (1j * np.sqrt(2))
xb = (b + b.conj().T) / np.sqrt(2); pb = (b - b.conj().T) / (1j * np.sqrt(2))
psi0 = np.zeros(N * N, complex); psi0[0] = 1.0
J = xa + xb
def heis(O, t):
    U = linalg.expm(1j * H * t)
    return U @ O @ U.conj().T
for t in [0.3, 1.1, 2.5]:
    Jt = heis(J, t)
    c = psi0.conj() @ (Jt @ J - J @ Jt) @ psi0
    corr = psi0.conj() @ (Jt @ J) @ psi0
    print(f"    t={t}: <[J(t),J(0)]> = {c:.2e}; <J(t)J(0)> = {corr:.6f}  (= cos(wt) = {np.cos(w*t):.6f}: symmetric spectrum)")
# Emission silence for a Hermitian f = alpha x_a + beta p_a + gamma x_b + delta p_b: weight on b^dag acting on the state
for (al, be, ga, de) in [(1, 0.3, 0, 0), (1, 0.3, 0.2, 0), (0.5, 0, 0, 0.1)]:
    f = al * xa + be * pa + ga * xb + de * pb
    v = f @ psi0
    # meter energy of f|psi0>: components with one b quantum have energy -w (emission side)
    proj_b = np.zeros(N * N); proj_b[1] = 1.0  # |0_a,1_b> index = 0*N + 1
    emit = abs(v[1]) ** 2
    print(f"    f = {al}x_a+{be}p_a+{ga}x_b+{de}p_b: emission weight |<0_a,1_b|f|0,0>|^2 = {emit:.4f}")
print("    => emission silence <=> f has no b-sector component; the b (negative-energy) sector enters only J.")

# ---------------------------------------------------------------- [5]
print("\n[5] Theorem P near s -> 0+: |F| = 1, g = 1, rho = 1/P (minimal emission-silent absorption), record |G|^2 P = P/s^2")
def pint(e, d):  # closed form of int_d^1 s^e ds
    return np.log(1 / d) if abs(e + 1) < 1e-12 else (1 - d ** (e + 1)) / (e + 1)
for aexp in [0.0, 0.5, 1.0, 1.5]:
    out = []
    for d in [1e-2, 1e-4, 1e-6, 1e-8]:
        I_rho = pint(-aexp, d); I_rec = pint(aexp - 2, d); I_cs = pint(-1.0, d)
        out.append((d, I_rho, I_rec, np.sqrt(I_rho * I_rec) / I_cs))
    print(f"    P = s^{aexp}: " + "; ".join(f"d={d:.0e}: int rho={r:.3g}, int rec={q:.3g}, sqrt(prod)/ln(1/d)={c:.2f}" for d, r, q, c in out))
print("    => int rho and int |G|^2 P cannot both stay finite (Cauchy-Schwarz: their product >= (ln 1/d)^2).")

# ---------------------------------------------------------------- [6]
print("\n[6] secular pumping of one on-shell record mode: h'' + k^2 h = J(t), stationary noise S_J(w) = P(|w^2 - k^2|), k = 1")
def E_of_T(T, Pfun, wmax=6.0):
    # <E(T)> for h(0)=h'(0)=0: E = (1/2)(h'^2 + k^2 h^2); exact kernel:
    # <E> = (1/4) int dw/2pi S(w) [ sinc-like(w-k) + sinc-like(w+k) ], K(u) = 4 sin^2(uT/2)/u^2
    k = 1.0
    def Kf(u):
        return T ** 2 if abs(u) < 1e-12 else 4 * np.sin(u * T / 2) ** 2 / u ** 2
    f = lambda wv: Pfun(abs(wv * wv - k * k)) * (Kf(wv - k) + Kf(wv + k)) / 4 / (2 * np.pi)
    pts = [k - 1e-3, k, k + 1e-3]
    val = 0.0
    edges = np.concatenate([np.linspace(-wmax, -k - 0.05, 5), [-k], np.linspace(-k + 0.05, k - 0.05, 5), [k], np.linspace(k + 0.05, wmax, 5)])
    edges = np.unique(np.concatenate([edges, k + np.array([-1, 1]) * 0.5 / T, -k + np.array([-1, 1]) * 0.5 / T]))
    for i in range(len(edges) - 1):
        val += integrate.quad(f, edges[i], edges[i + 1], limit=400)[0]
    return val
for lab, Pf in [("P = const (P(0)>0)", lambda s: 1.0), ("P = |s|^0.5", lambda s: s ** 0.5),
                ("P = |s|", lambda s: s), ("P = |s|^2", lambda s: s ** 2)]:
    vals = [E_of_T(T, Pf) for T in [1e1, 1e2, 1e3, 1e4]]
    print(f"    {lab:20s}: E(T) at T=1e1,1e2,1e3,1e4 = " + ", ".join(f"{v:.4g}" for v in vals))
print("    => linear growth for P(0)>0, ~T^(1-a) for 0<a<1, ln T for a=1, bounded for a>1 (no secular pumping only if P vanishes faster than |s|).")

# ---------------------------------------------------------------- [7]
print("\n[7] forced tower (emission-silent sector): rho(s) = (lam g/pi)|F|^2/(s+mu^2), |F|=1 for s < 1/l^2")
def dV_over_V(r, mu, l, lam=1.0):
    umax = r / l; m = mu * r   # u = x r
    edges = sorted(set([min(e, umax) for e in [0.0, 1.0, 10.0, 80.0] + ([m] if m < 80 else [])]))
    val = sum(integrate.quad(lambda u: u * np.exp(-u) / (u * u + m * m), edges[i], edges[i + 1], limit=400)[0]
              for i in range(len(edges) - 1))
    return 2 * lam / np.pi * val
for mu_inv in [1e-6, 1e-5]:
    mu = 1 / mu_inv
    for r in [1e-7, 1e-6, 3.86e-5, 5.2e-5, 1e-3, 1e-2]:
        print(f"    1/mu={mu_inv:.0e} m, l=4e-10 m, r={r:.2e} m: dV/V_N = {dV_over_V(r, mu, 4e-10):.3e}"
              f"   (asymptote (2/pi)/(mu r)^2 = {2/np.pi/(mu*r)**2:.3e})")
print("    Lee et al. 2020 (local text, untrusted data): an |alpha| = 1 Yukawa must have range < 38.6 um (95%).")
print("    A power-law tail (2 lam/pi)(mu r)^-2 is not a single Yukawa; compare at r = 38.6-52 um as an order-of-magnitude check only.")

# ---------------------------------------------------------------- [8]
print("\n[8] absorption into the meter (matter loses energy): order-of-magnitude rates")
Gn, me, a0, hbar, c = 6.674e-11, 9.109e-31, 5.29e-11, 1.0546e-34, 2.998e8
for dE_eV in [10.0, 1e3]:
    wq = dE_eV * 1.602e-19 / hbar
    rate = Gn * me ** 2 * a0 ** 4 * wq ** 5 / (5 * hbar * c ** 5)
    print(f"    quadrupole graviton-like rate, electron, a0 lever arm, dE={dE_eV:g} eV: {rate:.2e} s^-1 (GR order of magnitude, own)")
for lam, mu_inv in [(1.0, 1e-6), (1.0, 1e-9)]:
    for dE_eV in [10.0, 1e3]:
        kmax = dE_eV * 1.602e-19 / (hbar * c)   # m^-1
        fac = lam / np.pi * np.log(1 + (kmax * mu_inv) ** 2)
        print(f"    tower/graviton factor (lam={lam}, 1/mu={mu_inv:.0e} m, dE={dE_eV:g} eV): (lam/pi) ln(1+dE^2/mu^2) = {fac:.3g}")
lP2 = Gn * hbar / c ** 3; n_cmb = 4.11e8
print(f"    CMB photon into tower, sigma ~ lam*l_P^2 = {lP2:.2e} m^2 (suggested O(1)): rate per photon ~ {lP2*n_cmb*c:.1e} s^-1")

# ---------------------------------------------------------------- [9]
print("\n[9] BMV")
wB, dx = 2 * np.pi / 2.5, 250e-6
print(f"    timelike transfers need |k| < w/c; branch sensitivity ~ (w dx/c)^2 = {(wB*dx/c)**2:.1e} for w=2pi/2.5 s, dx=250 um")
Z = np.diag([1.0, -1.0]).astype(complex); I2 = np.eye(2, dtype=complex)
Z1, Z2 = np.kron(Z, I2), np.kron(I2, Z)
def liouv(Hm, Ls):
    d = Hm.shape[0]; Id = np.eye(d)
    Lv = -1j * (np.kron(Id, Hm) - np.kron(Hm.T, Id))
    for L in Ls:
        LdL = L.conj().T @ L
        Lv += np.kron(L.conj(), L) - 0.5 * np.kron(Id, LdL) - 0.5 * np.kron(LdL.T, Id)
    return Lv
def negativity(rho):
    rr = rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    ev = np.linalg.eigvalsh((rr + rr.conj().T) / 2)
    return float(-ev[ev < 0].sum())
plus = np.array([1, 1], dtype=complex) / np.sqrt(2); psi = np.kron(plus, plus); rho0 = np.outer(psi, psi.conj())
t = np.pi / 8
for delta in [0.0, 1e-3, 0.1]:
    g_tot = 1.0 + delta
    # classical spacelike sector: local meters (LOCC) at the AM-GM floor for the TOTAL coupling g_tot
    k = g_tot / 2; lam = g_tot / (2 * np.sqrt(k))
    c1 = np.sqrt(k) * Z1; c2 = np.sqrt(k) * Z2
    Hb = (lam * Z2 @ c1 + c1.conj().T @ (lam * Z2)) / 2 + (lam * Z1 @ c2 + c2.conj().T @ (lam * Z1)) / 2
    Lvb = liouv((Hb + Hb.conj().T) / 2, [c1 - 1j * lam * Z2, c2 - 1j * lam * Z1])
    rt = (linalg.expm(Lvb * t) @ rho0.reshape(-1, order='F')).reshape(4, 4, order='F')
    # quantum alternative: same total coupling, coherent, no noise
    Uc = linalg.expm(-1j * g_tot * Z1 @ Z2 * t); rc = Uc @ rho0 @ Uc.conj().T
    print(f"    tower fraction {delta:g}: Z1Z2 coeff (LOCC) = {np.real(np.trace(Hb@Z1@Z2))/4:.4f}; negativity LOCC = {negativity(rt):.2e}; coherent = {negativity(rc):.4f}")
print("    R4-4 benchmark (refereed): concurrence 0.156 quantum vs 0 for a classical channel.")
