AUDIT_INPUT_PATHS = ('docs/SKIP_PATTERNS_CARRY_THE_TICK_FRACTION_ON_CLOCKS_BUT_EVERY_SKIP_FRONT_MAKES_PAIRS_SO_THE_LAPSE_IS_READ_INTO_THE_CUBE_STEP_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Skip rule: can a discrete, local tick-or-skip rule carry the tick fraction N = 1 + Phi of CL-1's
adopted tick-fraction clause?
A. clock noise of two candidate rules: deterministic error diffusion (sigma-delta) and the CL-2-style
   stochastic skip (independent odds per site); Allan deviation scaling; physical numbers vs clocks.
B. what a skip does to the update: a skip front (neighbours one ticking, one skipping) always leaves an
   unpaired half-tick (exhaustive: 1D ring, 3D torus), and on the split-step Floquet sea each front
   event creates pairs (~0.1 eps^2 per boundary, energy ~2 eps per pair); a uniform skip creates none.
C. discordance: any coupling of two sites' skips disagrees at rate >= |N_i - N_j| (exact); the shared-
   threshold (comonotone) rule attains it; independent rules disagree at ~2(1-N); pair creation on a
   gradient ring tracks the discordance; the step-angle reading (N read into the cube's step, every
   site ticking) is a static update and creates nothing.
D. against measurement: minimal pair-production power in Earth's field.
E. the step-angle reading realises the lapse: low-band quasi-energies scale exactly by N.
F. self-consistency with the hinge sum on a 3D lattice with a point source: the skip pattern's
   measured fraction solves the static stationarity equation to 1/T (sigma-delta), log T/T
   (comonotone), 1/sqrt(T) (stochastic).
Self-contained; seeded (20261023); numpy + scipy only."""
AUDIT_TIMEOUT_SEC = 120
import time
import numpy as np
import scipy.sparse as spm
from scipy.sparse.linalg import spsolve

T0 = time.time()
RNG = np.random.default_rng(20261023)
P = F = 0
def check(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

# ---------------- A. clock noise ----------------
def allan(x, taus):
    out = []
    for m in taus:
        d = x[2*m:] - 2*x[m:-m] + x[:-2*m]
        out.append(np.sqrt(np.mean(d**2)/(2.0*m*m)))
    return np.array(out)
T = 2**18
N0 = 1 - 0.0137*np.sqrt(2)
a0 = RNG.random()
# simulate sigma-delta step by step for a shorter run, compare with closed form floor(a0 + N t)
acc, cnt, err = a0, 0, 0
Ts = 20000
for t in range(1, Ts + 1):
    acc += N0
    if acc >= 1.0: acc -= 1.0; cnt += 1
    if t % 1000 == 0: err = max(err, abs(cnt - (np.floor(a0 + N0*t))))
check("A1 sigma-delta count = floor(a0 + N T) (simulated vs closed form, 20000 steps)", err == 0, f"max diff {err}")
t = np.arange(T + 1)
nsd = np.floor(a0 + N0*t)
xsd = nsd - N0*t
# time-varying target: |n - sum N| < 1 at all T
Nt = N0 + 0.003*np.sin(2*np.pi*t/5000.0)
nvar = np.floor(a0 + np.concatenate([[0], np.cumsum(Nt[1:])]))
check("A2 sigma-delta with slowly varying N: |n(T) - sum N| < 1 tick for every T", np.max(np.abs(nvar - a0 - np.concatenate([[0], np.cumsum(Nt[1:])]))) < 1.0 + 1e-9,
      f"max {np.max(np.abs(nvar - a0 - np.concatenate([[0], np.cumsum(Nt[1:])]))):.3f}")
taus = 2**np.arange(4, 13)
sd = allan(xsd, taus)
slope_sd = np.polyfit(np.log(taus), np.log(sd), 1)[0]
xb = np.concatenate([[0], np.cumsum(RNG.random(T) < N0)]) - N0*t
sb = allan(xb, taus)
slope_b = np.polyfit(np.log(taus), np.log(sb), 1)[0]
check("A3 Allan deviation: sigma-delta ~ 1/tau, stochastic ~ tau^-1/2 (slopes)", abs(slope_sd + 1) < 0.15 and abs(slope_b + 0.5) < 0.1,
      f"{slope_sd:.3f}, {slope_b:.3f}")
pred_b = np.sqrt((1 - N0)*N0/taus)  # white frequency noise of a Bernoulli count, fractional per tick
check("A4 stochastic Allan deviation = sqrt(N(1-N)/tau) (ticks)", np.max(np.abs(sb/pred_b - 1)) < 0.1, f"max dev {np.max(np.abs(sb/pred_b-1)):.3f}")
tP = 5.391e-44
sy_sd = np.sqrt(2)*tP/1e4
sy_b1 = np.sqrt(tP/1.0)
check("A5 sigma-delta jitter at 1e4 s (Planck tick) below optical-clock 1e-18", sy_sd < 1e-18, f"{sy_sd:.1e}")
check("A6 stochastic jitter at 1 s <= sqrt(t_P/1 s) below best clocks ~1e-16 (not excluded by clocks)", sy_b1 < 1e-16,
      f"{sy_b1:.1e}; with |Phi| = 1e-6: {np.sqrt(1e-6*tP):.1e}")

# ---------------- B. a skip front on the update ----------------
def unions_count_1d(L):
    ev = [((2*j) % L, (2*j+1) % L) for j in range(L//2)]
    od = [((2*j+1) % L, (2*j+2) % L) for j in range(L//2)]
    good = 0
    for S in range(2**L):
        bits = [(S >> k) & 1 for k in range(L)]
        if all(bits[a] == bits[b] for a, b in ev) and all(bits[a] == bits[b] for a, b in od): good += 1
    return good
g1 = unions_count_1d(12)
check("B1 1D ring L=12: sets that are unions of both pair tilings (only these skip with no unpaired half-tick)", g1 == 2, f"{g1} of 4096 (empty, all)")
def cubes(L, off):
    cs = []
    for x in range(off, L, 2):
        for y in range(off, L, 2):
            for z in range(off, L, 2):
                cs.append({((x+i) % L, (y+j) % L, (z+k) % L) for i in (0, 1) for j in (0, 1) for k in (0, 1)})
    return cs
ev3, od3 = cubes(4, 0), cubes(4, 1)
g3 = 0
for m in range(2**len(ev3)):
    A = set().union(*[ev3[i] for i in range(len(ev3)) if (m >> i) & 1]) if m else set()
    if all(c <= A or not (c & A) for c in od3): g3 += 1
check("B2 3D torus 4^3: unions of even cubes that are also unions of odd cubes", g3 == 2, f"{g3} of 256")

L = 64
def pairU(ang, parity, mask):
    U = np.eye(L, dtype=complex)
    for j in range(L//2):
        if not mask[j]: continue
        a = (2*j + parity) % L; b = (a + 1) % L; c, s = np.cos(ang[j]), np.sin(ang[j])
        U[a, a] = c; U[b, b] = c; U[a, b] = -1j*s; U[b, a] = -1j*s
    return U
def tick(ee, eo, me, mo):  # even exp(-i(eps - mu/2)R), odd exp(+i(eps + mu/2)R), R = pair hop
    return pairU(-eo, 1, mo) @ pairU(ee, 0, me)
def vac(U):
    w, V = np.linalg.eig(U); q = np.angle(w); Q, _ = np.linalg.qr(V[:, q < 0]); return Q @ Q.conj().T, V, q
def masks(skip):  # a cube applies iff none of its sites skips
    me = np.array([not (skip[2*j] or skip[(2*j+1) % L]) for j in range(L//2)])
    mo = np.array([not (skip[(2*j+1) % L] or skip[(2*j+2) % L]) for j in range(L//2)])
    return me, mo
ON = np.ones(L//2, bool); I = np.eye(L)
res = {}
for eps, mu in ((0.05, 0.002), (0.2, 0.02), (0.5, 0.02)):
    ee, eo = np.full(L//2, eps - mu/2), np.full(L//2, eps + mu/2)
    U = tick(ee, eo, ON, ON); Pv, V, q = vac(U)
    H = V @ np.diag(q) @ np.linalg.inv(V)
    S = np.zeros(L, bool); S[:L//2] = True
    Ud = tick(ee, eo, *masks(S)); P2 = Ud @ Pv @ Ud.conj().T
    exc = np.trace((I - Pv) @ P2).real/2; dE = np.trace(H @ (P2 - Pv)).real/2
    Uz = tick(ee, eo, ~ON, ~ON); z = abs(np.trace((I - Pv) @ Uz @ Pv @ Uz.conj().T).real)
    P3 = P2.copy()
    for _ in range(50): P3 = U @ P3 @ U.conj().T
    keep = abs(np.trace((I - Pv) @ P3).real/2 - exc)
    res[eps] = (exc/eps**2, dE/exc, z, keep)
c_ok = all(0.05 < r[0] < 0.2 for r in res.values())
check("B3 pairs per front boundary ~ c eps^2 with 0.05 < c < 0.2 (eps = 0.05, 0.2, 0.5)", c_ok,
      "c = " + ", ".join(f"{r[0]:.3f}" for r in res.values()))
check("B4 energy per pair ~ 2 eps hbar/tick (band edge) and uniform skip creates none (<1e-12)",
      all(1.5 < r[1]/e < 2.6 for e, r in res.items()) and all(r[2] < 1e-12 for r in res.values()),
      "E/eps = " + ", ".join(f"{r[1]/e:.2f}" for e, r in res.items()))
check("B5 created pairs persist under later full ticks (50 ticks)", all(r[3] < 1e-10 for r in res.values()),
      f"max change {max(r[3] for r in res.values()):.1e}")
C_PAIR = res[0.2][0]; E_PAIR = res[0.2][1]/0.2

# ---------------- C. discordance ----------------
pq = RNG.random((200, 2))
lp_ok = True
for p, qq in pq:  # minimise P(xor) over couplings: joint (a,b,c,d) on 00,01,10,11 with marginals
    lo = max(0.0, p + qq - 1); hi = min(p, qq)   # P(11) range
    xor_min = p + qq - 2*hi; xor_ind = p*(1-qq) + qq*(1-p)
    lp_ok &= abs(xor_min - abs(p - qq)) < 1e-12 and xor_ind >= xor_min - 1e-12 and lo <= hi
check("C1 any coupling of two skips disagrees with probability >= |p_i - p_j|; comonotone attains it (200 pairs)", lp_ok)
def vdc(n):  # van der Corput radical inverse base 2: binary digits of the global step reversed
    v = np.zeros(n); b = 0.5; k = np.arange(n)
    while k.any(): v += b*(k & 1); k >>= 1; b /= 2
    return v
eps, mu = 0.2, 0.02
Tg = 1500
xs = np.arange(L)
Nx = 1 - 0.05*(1 - np.cos(2*np.pi*xs/L))/2
dN = np.abs(Nx - np.roll(Nx, -1))
u = vdc(Tg + 1)
offs = RNG.random(L)
def pattern(rule, t):
    if rule == "comonotone": return u[t] < 1 - Nx                    # skip iff shared threshold below 1-N
    if rule == "sd-common": return np.floor(Nx*t) == np.floor(Nx*(t-1))
    if rule == "sd-indep": return np.floor(offs + Nx*t) == np.floor(offs + Nx*(t-1))
    return RNG.random(L) < 1 - Nx                                     # independent odds per site
ee, eo = np.full(L//2, eps - mu/2), np.full(L//2, eps + mu/2)
U = tick(ee, eo, ON, ON); Pv, _, _ = vac(U)
out = {}
for rule in ("comonotone", "sd-common", "sd-indep", "stochastic"):
    Pt = Pv.copy(); disc = 0; ticks = np.zeros(L)
    for tt in range(1, Tg + 1):
        sk = pattern(rule, tt); ticks += ~sk
        disc += np.sum(sk != np.roll(sk, -1))
        Ut = tick(ee, eo, *masks(sk)); Pt = Ut @ Pt @ Ut.conj().T
    out[rule] = (disc/(L*Tg), np.trace((I - Pv) @ Pt).real, disc, np.max(np.abs(ticks/Tg - Nx)))
r_co = out["comonotone"][0]/np.mean(dN)
check("C2 comonotone (shared van der Corput threshold) discordance per bond per tick = mean |dN|", abs(r_co - 1) < 0.1, f"ratio {r_co:.3f}")
r_in = out["stochastic"][0]/np.mean(2*(1 - Nx)*Nx)
check("C3 independent skips discord at ~2N(1-N) per bond; sigma-delta desynchronises to the same order",
      abs(r_in - 1) < 0.1 and out["sd-indep"][0] > 5*out["comonotone"][0] and out["sd-common"][0] > 5*out["comonotone"][0],
      " ".join(f"{k}:{v[0]:.2e}" for k, v in out.items()))
ratios = [out[k][1]/(C_PAIR*eps**2*out[k][2]) for k in out]
check("C4 pairs created on the gradient ring track discordance: created/(c eps^2 x events) in [0.2, 2]",
      all(0.2 < r < 2 for r in ratios) and out["comonotone"][1] < out["stochastic"][1]/5,
      " ".join(f"{k}:{v[1]:.2f} pairs, ratio {r:.2f}" for (k, v), r in zip(out.items(), ratios)))
check("C5 every skip rule reproduces the target fraction (max |n/T - N|)", max(v[3] for v in out.values()) < 0.03,
      " ".join(f"{v[3]:.1e}" for v in out.values()))
Nc_e = 0.5*(Nx[0::2] + Nx[1::2]); Nc_o = 0.5*(Nx[1::2] + np.roll(Nx, -1)[1::2])
eeA = np.arcsin(Nc_e*np.sin(eps)) - Nc_e*mu/2; eoA = np.arcsin(Nc_o*np.sin(eps)) + Nc_o*mu/2
UA = tick(eeA, eoA, ON, ON); PA, _, _ = vac(UA); Pt = PA.copy()
for _ in range(Tg): Pt = UA @ Pt @ UA.conj().T
check("C6 step-angle reading (every site ticks, N in the cube's step): static update, 0 pairs over 1500 ticks",
      abs(np.trace((I - PA) @ Pt).real) < 1e-9, f"{abs(np.trace((I - PA) @ Pt).real):.1e}")

# ---------------- D. against measurement ----------------
hbar, cc, g = 1.0546e-34, 2.998e8, 9.81
a = np.sqrt(8*np.pi)*1.616e-35   # cell rung
for e_ in (0.5, 0.05):
    # minimal discordance per gradient bond per tick = (g/c^2) a; tick = sin(eps) a/(sqrt3 c) (CL-1 light speed)
    tk = np.sin(e_)*a/(np.sqrt(3)*cc)
    Pw = C_PAIR*e_**2*(E_PAIR*e_*hbar/tk)*((g/cc**2)*a/tk)/a**3
    print(f"INFO eps={e_}: tick {tk:.1e} s; minimal (comonotone) pair-production power near Earth {Pw:.1e} W/m^3")
check("D1 minimal skip rule: vacuum pair production near Earth exceeds 1 W/m^3 by > 1e80 (skip reading excluded)", Pw > 1e80, f"{Pw:.1e} W/m^3 at eps=0.05")
ratio_ind = 2*(6.96e-10)/((g/cc**2)*a)
print(f"INFO independent / sigma-delta rules discord {ratio_ind:.1e} times more (2|Phi|/(|grad Phi| a), Earth surface)")

# ---------------- E. the step-angle reading realises the lapse ----------------
devs = []
for e_ in (0.05, 0.2):
    q1 = np.sort(np.abs(np.angle(np.linalg.eigvals(tick(np.full(L//2, e_ - 0.01), np.full(L//2, e_ + 0.01), ON, ON)))))
    for Nn in (0.7, 0.9):
        e2 = np.arcsin(Nn*np.sin(e_))
        q2 = np.sort(np.abs(np.angle(np.linalg.eigvals(tick(np.full(L//2, e2 - Nn*0.01), np.full(L//2, e2 + Nn*0.01), ON, ON)))))
        devs.append(np.max(np.abs(q2[:8]/q1[:8] - Nn)))
check("E1 sin(eps_cube) = N sin(eps0), mu = mN: lowest quasi-energies scale by N (clock rate = lapse)", max(devs) < 1e-3, f"max dev {max(devs):.1e}")

# ---------------- F. self-consistency with the hinge sum (3D, point source) ----------------
n = 21; m = n - 2
idx = np.arange(m**3).reshape(m, m, m)
rows, cols, vals = [], [], []
for ax in range(3):
    for sgn in (1, -1):
        sh = np.roll(idx, -sgn, axis=ax); valid = np.ones_like(idx, bool)
        sl = [slice(None)]*3; sl[ax] = -1 if sgn == 1 else 0; valid[tuple(sl)] = False
        rows += list(idx[valid]); cols += list(sh[valid]); vals += [-1.0]*int(valid.sum())
rows += list(idx.ravel()); cols += list(idx.ravel()); vals += [6.0]*m**3
K = spm.csr_matrix((vals, (rows, cols)), shape=(m**3, m**3))   # = -lattice Laplacian (one-g kernel, units 2kappa = 1)
GM = 0.05
rho = np.zeros(m**3); c0 = idx[m//2, m//2, m//2]; rho[c0] = 4*np.pi*GM
psi = spsolve(K.tocsc(), rho)           # lapse equation: -lap psi = 4 pi G rho
Phi = -psi                              # density equation: Phi + psi = 0 (tick-skip-gamma)
Ntar = 1 + Phi
KP = np.max(np.abs(K @ psi))
offs3 = RNG.random(m**3)
def resid(Nm): return np.max(np.abs(K @ ((Nm - 1) + psi)))/KP
rs, rb, rc = [], [], []
for TT in (10**3, 10**4, 10**5):
    rs.append(resid(np.floor(offs3 + Ntar*TT)/TT))
for TT in (10**4, 10**6):
    rb.append(resid(RNG.binomial(TT, Ntar)/TT))
Tc = 2**16; us = np.sort(vdc(Tc))
rc.append(resid((Tc - np.searchsorted(us, 1 - Ntar))/Tc))
check("F1 sigma-delta pattern solves the stationarity equation to <= 12/(T |K psi|) (T = 1e3, 1e4, 1e5)",
      all(r <= 12/(TT*KP) for r, TT in zip(rs, (1e3, 1e4, 1e5))) and rs[-1] < 1e-3, " ".join(f"{r:.1e}" for r in rs))
check("F2 stochastic pattern residual falls as T^-1/2 (ratio 1e4 -> 1e6 in [5, 20])", 5 < rb[0]/rb[1] < 20, f"{rb[0]:.1e} -> {rb[1]:.1e}")
check("F3 comonotone pattern residual <= 12 (log2 T + 2)/(T |K psi|) at T = 2^16", rc[0] <= 12*(16 + 2)/(Tc*KP), f"{rc[0]:.1e}")
Phim = (np.floor(offs3 + Ntar*1e5)/1e5 - 1).reshape(m, m, m)
for r in (2, 3, 4):
    vals_r = [Phim[m//2 + r, m//2, m//2], Phim[m//2, m//2 + r, m//2], Phim[m//2, m//2, m//2 + r]]
    print(f"INFO r={r}: measured -Phi r/(GM) = {-np.mean(vals_r)*r/GM:.3f} (Dirichlet box 21^3; continuum 1); axes spread {np.ptp(vals_r):.1e}")
check("F4 measured fraction field is attractive and falls with r (Phi(1) < Phi(2) < Phi(4) < 0)",
      Phim[m//2+1, m//2, m//2] < Phim[m//2+2, m//2, m//2] < Phim[m//2+4, m//2, m//2] < 0)
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")
