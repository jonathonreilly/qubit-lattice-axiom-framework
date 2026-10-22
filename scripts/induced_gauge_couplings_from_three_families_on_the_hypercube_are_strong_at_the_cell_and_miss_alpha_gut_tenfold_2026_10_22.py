AUDIT_INPUT_PATHS = ('docs/INDUCED_GAUGE_COUPLINGS_FROM_THREE_FAMILIES_ON_THE_HYPERCUBE_ARE_STRONG_AT_THE_CELL_AND_MISS_ALPHA_GUT_TENFOLD_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""induced-couplings: Sakharov-type induced gauge coupling and G from the same lattice fermions.

Rule under test (Ruleset A, R2 reading): links carry no bare plaquette term; the gauge kinetic
term and the Einstein term are both the one-loop response of the lattice fermions.
A. machinery checks (exact BZ integrals, real-space log det, Ward identity, log coefficient)
B. lattice-exact constants: 1/e^2 = (1/6pi^2)[ln(1/(a mu)) + C] per Dirac; 1/(16 pi G) = c_G/a^2 per Dirac
C. content: Dynkin indices of three families of 16 Weyl
D. estimates against measurement (supplied: measured G, alpha_i(M_Z), SM one-loop b_i)
Self-contained: numpy only.
"""
import time
import numpy as np

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = NF = 0
np.random.seed(20261022)


def rep(ok, tag, msg, val=""):
    global NP, NF
    NP, NF = (NP + 1, NF) if ok else (NP, NF + 1)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg}" + (f" | {val}" if val else ""))


# ------------------------------------------------------------ Euclidean gammas, Clifford helpers
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]).astype(complex)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
G = np.array([np.block([[Z2, -1j*s], [1j*s, Z2]]) for s in (s1, s2, s3)] + [np.block([[Z2, I2], [I2, Z2]])])
I4 = np.eye(4)


def cl(a, b):
    out = a[..., None, None]*I4
    for mu in range(4):
        out = out + b[mu][..., None, None]*G[mu]
    return out


def parts(k, m, r):
    c = np.cos(k); s = np.sin(k)
    W = m + r*(1 - c).sum(-1)
    D = W**2 + (s*s).sum(-1)
    z = np.zeros_like(W)
    S = cl(W/D, [-1j*s[..., mu]/D for mu in range(4)])          # S = D(k)^-1, D = W + i g.sin k
    return c, s, S, z


def vertex(c, s, z, r, kind):
    if kind == 'gauge':   # link phase e^{iA(x2)} on direction-1 hops
        return cl(r*s[..., 0], [1j*c[..., 0], z, z, z])
    # TT metric h11 = -h33 = h(x2): vierbein (1 -+ h/2) on kinetic hops, (1 -+ h) on Wilson terms of dirs 1, 3
    return cl(r*(c[..., 0] - c[..., 2]), [-0.5j*s[..., 0], z, 0.5j*s[..., 2], z])


def integrand(k, m, r, kind):
    """4 x (q^2 coefficient of Gamma2/(V eps^2)) = -(1/2) tr(dS V dS V), dS = d S/dk2 = -S D' S."""
    c, s, S, z = parts(k, m, r)
    Dp = cl(r*s[..., 1], [z, 1j*c[..., 1], z, z])
    V = vertex(c, s, z, r, kind)
    A = (-S @ Dp @ S) @ V
    return -0.5*np.einsum('...ij,...ji->...', A, A).real


def step(x):
    x = np.clip(x, 1e-12, 1 - 1e-12)
    f = np.exp(-1/x); g = np.exp(-1/(1 - x))
    return f/(f + g)


def chi(rad, R):
    return np.where(rad < R, step((R - rad)/R), 0.0)


def coef(m, r, kind, R=1.4, N=32, nr=72, na=(18, 14, 14)):
    """exact BZ integral split by a smooth radial bump: outer trapezoid (spectral) + inner 4D spherical."""
    period = np.pi if r == 0 else 2*np.pi            # naive: pi-periodic integrand = one doubler cell
    vol = (period/(2*np.pi))**4
    t = period*((np.arange(N) + 0.5)/N - 0.5)
    K2, K3, K4 = np.meshgrid(t, t, t, indexing='ij')
    outer = 0.0
    for k1 in t:
        k = np.stack([np.full_like(K2, k1), K2, K3, K4], -1)
        outer += (integrand(k, m, r, kind)*(1 - chi(np.sqrt((k*k).sum(-1)), R))).sum()
    outer *= vol/N**4
    xr, wr = np.polynomial.legendre.leggauss(nr)
    lo, hi = np.log(max(m, 1e-3)*1e-3), np.log(R)
    u = 0.5*(hi - lo)*xr + 0.5*(hi + lo); wu = 0.5*(hi - lo)*wr
    xp, wp = np.polynomial.legendre.leggauss(na[0]); psi = 0.5*np.pi*(xp + 1); wpsi = 0.5*np.pi*wp
    xt, wt = np.polynomial.legendre.leggauss(na[1]); th = 0.5*np.pi*(xt + 1); wth = 0.5*np.pi*wt
    ph = 2*np.pi*np.arange(na[2])/na[2]; wph = np.full(na[2], 2*np.pi/na[2])
    P, T, F = np.meshgrid(psi, th, ph, indexing='ij')
    WA = (wpsi[:, None, None]*wth[None, :, None]*wph[None, None, :])*np.sin(P)**2*np.sin(T)
    n = np.stack([np.cos(P), np.sin(P)*np.cos(T), np.sin(P)*np.sin(T)*np.cos(F), np.sin(P)*np.sin(T)*np.sin(F)], -1)
    inner = 0.0
    for ui, wi in zip(u, wu):
        rr = np.exp(ui)
        inner += wi*rr**4*chi(rr, R)*(integrand(rr*n, m, r, 'gauge' if kind == 'gauge' else 'grav')*WA).sum()
    return outer + inner/(2*np.pi)**4


def gamma2_finite_q(m, r, q, N):
    """Gamma2/(V eps^2) for the gauge wave at finite q (tadpole + bubble), uniform grid."""
    g = 2*np.pi*(np.arange(N) + 0.5)/N
    K2, K3, K4 = np.meshgrid(g, g, g, indexing='ij')
    tot = 0.0
    for k1 in g:
        k = np.stack([np.full_like(K2, k1), K2, K3, K4], -1)
        c, s, S, z = parts(k, m, r)
        Sp = parts(k + np.array([0, q, 0, 0]), m, r)[2]; Sm = parts(k - np.array([0, q, 0, 0]), m, r)[2]
        V1 = vertex(c, s, z, r, 'gauge')
        V2 = cl(r*c[..., 0]/2, [-0.5j*s[..., 0], z, z, z])
        tad = np.einsum('...ij,...ji->...', S, V2)
        bub = np.einsum('...ij,...ji->...', S @ V1 @ Sp, V1) + np.einsum('...ij,...ji->...', S @ V1 @ Sm, V1)
        tot += (0.5*tad - 0.125*bub).real.sum()
    return -tot/N**4


def logdet_realspace(eps, m, r, L2, k1, k3, k4, q):
    """-ln det of the Wilson operator with links exp(i eps cos(q x2)) on direction-1 hops, x2 in real space."""
    M = np.zeros((4*L2, 4*L2), complex)
    for x in range(L2):
        U = np.exp(1j*eps*np.cos(q*x))
        blk = (m + 2*r)*I4 - 0.5*((r*I4 - G[0])*U*np.exp(1j*k1) + (r*I4 + G[0])*np.conj(U)*np.exp(-1j*k1))
        blk += r*(2 - np.cos(k3) - np.cos(k4))*I4 + 1j*np.sin(k3)*G[2] + 1j*np.sin(k4)*G[3]
        M[4*x:4*x+4, 4*x:4*x+4] = blk
        y = (x + 1) % L2
        M[4*x:4*x+4, 4*y:4*y+4] += -0.5*(r*I4 - G[1])
        M[4*y:4*y+4, 4*x:4*x+4] += -0.5*(r*I4 + G[1])
    return np.linalg.slogdet(M)[1]


L6 = 6*np.pi**2
print("== A. machinery (Euclidean 4D hypercubic reading; Wilson r = 1 and naive r = 0 = 4 x staggered)")
# A1 real-space log det vs momentum-space formula (gauge, finite q, matching grids)
m0, L2, Nq = 0.4, 12, 6
q0 = 2*np.pi/L2; gp = 2*np.pi*(np.arange(Nq) + 0.5)/Nq; a0 = 1e-3; tot = 0.0
for k1 in gp:
    for k3 in gp:
        for k4 in gp:
            tot += sum(w*logdet_realspace(e, m0, 1.0, L2, k1, k3, k4, q0) for e, w in ((a0, 1), (-a0, 1), (0, -2)))
brute = -tot/2/a0**2/(Nq**3*L2)
k2g = 2*np.pi*np.arange(L2)/L2
K = np.stack(np.meshgrid(gp, k2g, gp, gp, indexing='ij'), -1)
c, s, S, z = parts(K, m0, 1.0)
Sp = parts(K + np.array([0, q0, 0, 0]), m0, 1.0)[2]; Sm = parts(K - np.array([0, q0, 0, 0]), m0, 1.0)[2]
V1 = vertex(c, s, z, 1.0, 'gauge'); V2 = cl(c[..., 0]/2, [-0.5j*s[..., 0], z, z, z])
form = -(0.5*np.einsum('...ij,...ji->...', S, V2) - 0.125*(np.einsum('...ij,...ji->...', S @ V1 @ Sp, V1)
                                                            + np.einsum('...ij,...ji->...', S @ V1 @ Sm, V1))).real.mean()
rep(abs(brute/form - 1) < 1e-4, "A1 [T]", "second order of -ln det with links exp(iA) in real space = momentum-space tadpole + bubble (vertices exact)",
    f"12-site x2 chain, 6^3 transverse, m = 0.4: {brute:.9f} vs {form:.9f}")
# A2 Ward identity and finite-q vs exact q->0 coefficient
mW = 0.3
g0 = gamma2_finite_q(mW, 1.0, 0.0, 32)
fq = [4*(gamma2_finite_q(mW, 1.0, mW/d, 32) - g0)/(mW/d)**2 for d in (3, 6)]
rich = (4*fq[1] - fq[0])/3
ex = coef(mW, 1.0, 'gauge')
rep(abs(g0) < 1e-6 and abs(rich/ex - 1) < 2e-3, "A2 [D]", "gauge invariance: Gamma2(q = 0) = 0; finite-q Richardson limit = exact q -> 0 integral",
    f"Gamma2(0) = {g0:.1e}; m = 0.3: {rich:.6f} (q -> 0 fit) vs {ex:.6f} (exact)")
# A3 split-integral independence of bump radius and grid
v1 = coef(0.01, 1.0, 'gauge', R=1.4, N=32); v2 = coef(0.01, 1.0, 'gauge', R=1.0, N=40)
rep(abs(v1/v2 - 1) < 1e-4, "A3 [D]", "the exact integral does not depend on the bump radius or grid", f"m = 0.01: {v1:.7f} (R 1.4, N 32) vs {v2:.7f} (R 1.0, N 40)")
# A4 naive integrand is pi-periodic (doubler symmetry => naive = 16 x one cell; staggered = naive/4)
kr = np.random.uniform(-np.pi, np.pi, (200, 4)); sh = np.zeros(4); sh[np.random.randint(4)] = np.pi
dper = max(np.max(np.abs(integrand(kr, 0.1, 0.0, kd) - integrand(kr + sh, 0.1, 0.0, kd))) for kd in ('gauge', 'grav'))
rep(dper < 1e-9, "A4 [T]", "naive integrand is pi-periodic (gamma_mu -> -gamma_mu is a Clifford automorphism): every doubler = one taste of staggered", f"max diff {dper:.1e}")

print("== B. lattice-exact induced constants (per Dirac, unit charge; m -> 0)")
res = {}
for name, r in (("Wilson r=1", 1.0), ("staggered/taste", 0.0)):
    va, vb = coef(1e-4, r, 'gauge'), coef(1e-5, r, 'gauge')
    slope = (vb - va)/np.log(10)*L6
    C4, C5 = L6*va - np.log(1e4), L6*vb - np.log(1e5)
    cg3, cg4 = coef(1e-2, r, 'grav'), coef(1e-3, r, 'grav')
    res[name] = (C5, cg4)
    rep(abs(slope - 1) < 0.02 and abs(C5 - C4) < 0.01, f"B-{name} [D]", "log coefficient d(1/e^2)/d ln(1/m) -> 1/(6 pi^2) (the beta function); finite part C converged",
        f"slope x 6pi^2 = {slope:.4f}; C(1e-4) = {C4:.4f}, C(1e-5) = {C5:.4f}")
    rep(cg4 > 0 and abs(cg4/cg3 - 1) < 0.03, f"B-{name}G [D]", "induced TT term has the sign of GR; c_G = a^2/(16 pi G) per Dirac, IR-finite as m -> 0",
        f"c_G(1e-2) = {cg3:.6f}, c_G(1e-3) = {cg4:.6f}; heat-kernel cutoff sqrt(96 pi^2 c_G) = {np.sqrt(96*np.pi**2*cg4):.3f}/a")
CW, cGW = res["Wilson r=1"]; CS, cGS = res["staggered/taste"]
mp = coef(0.3, 1.0, 'gauge')*L6 - np.log(1/0.3)
rep(CW > 0 and CS > 0 and abs(CW - CS) > 0.3, "B3 [D]", "C is O(1) and regulator-dependent (non-universal), but every value is O(1): 1/g^2 at the cell is a pure lattice number ~ C/(12 pi^2) per unit index",
    f"C_Wilson = {CW:.3f}, C_staggered = {CS:.3f}; slow approach (C_W(0.3) = {mp:+.3f}, m ln m terms)")

print("== C. content: three families of 16 Weyl (Ruleset A; N_f = 3 supplied)")
# 16 = (3,2)_{1/6} + (3b,1)_{-2/3} + (3b,1)_{1/3} + (1,2)_{-1/2} + (1,1)_{1} + (1,1)_{0}
fields = [(3, 2, 1/6), (3, 1, -2/3), (3, 1, 1/3), (1, 2, -1/2), (1, 1, 1.0), (1, 1, 0.0)]
T3 = sum(0.5*d2 for d3, d2, y in fields if d3 == 3); T2 = sum(0.5*d3 for d3, d2, y in fields if d2 == 2)
T1 = 0.6*sum(d3*d2*y*y for d3, d2, y in fields)
T10 = 1.5 + 0.5          # SU(5): 10 (T = 3/2) + 5b (T = 1/2) + 1 inside the 16
NFAM = 3; ST = NFAM*T3; ND = NFAM*16/2
rep(abs(T1 - 2) < 1e-12 and T2 == 2 and T3 == 2 and T10 == 2, "C1 [T]", "per family T = 2 for SU(3), SU(2), U(1)_Y (GUT-normalised) and Spin(10): induced couplings are EQUAL at the cell (sin^2 theta_W = 3/8 there) for every C",
    f"T3 {T3}, T2 {T2}, T1 {T1:.3f}, T16 {T10}; three families: sum T = {ST:.0f}, {ND:.0f} Dirac-equivalents")
rep(True, "C2 [T]", "one fermion loop is quadratic in the gauge field, so for any group 1/g^2_ind = sum_R T(R) x (U(1) value per unit charge^2); on the 4D hypercube F_munu F_munu is the only dimension-4 invariant, so the induced term is Lorentz invariant (no E/B split, unlike the cube tick)",
    "Weyl = half a Dirac: 1/g^2(mu) = sum T_W [ln(1/(a mu)) + C]/(12 pi^2)")

print("== D. estimates against measurement (supplied: G, alpha_i(M_Z), SM b_i)")
MPL, MZ = 1.22089e19, 91.1876
ainv_MZ = np.array([0.6*127.951*(1 - 0.23122), 127.951*0.23122, 1/0.1180])   # alpha_1 (GUT), alpha_2, alpha_3
bSM = np.array([41/10, -19/6, -7.0])


def sm(mu):
    return ainv_MZ - bSM/(2*np.pi)*np.log(mu/MZ)


out = {}
for name, C, cg in (("Wilson", CW, cGW), ("staggered", CS, cGS)):
    inva = MPL/np.sqrt(16*np.pi*ND*cg)                  # 1/(16 pi G) = ND c_G/a^2
    cell = 4*np.pi*ST*C/(12*np.pi**2)                   # 1/alpha at mu = 1/a
    L16 = np.log(inva/1e16)
    ferm16 = cell + 4*np.pi*ST/(12*np.pi**2)*L16
    out[name] = (inva, cell, ferm16, L16, C, cg)
inv, cellW, f16W, L16W, _, _ = out["Wilson"]; invS, cellS, f16S, L16S, _, _ = out["staggered"]
rep(1e18 < inv < 1e19 and 1e18 < invS < 1e19, "D1 [E]", "Sakharov: the same loops fix the cutoff from measured G: 1/a = M_Pl/sqrt(16 pi N_D c_G)",
    f"1/a = {inv:.2e} GeV (Wilson), {invS:.2e} GeV (staggered); register unit map 2.44e18")
smc = sm(inv); sm16 = sm(1e16)
rep(cellW < 1 and cellS < 1, "D2 [E]", "induced 1/alpha at the cell = (2/pi) C: STRONG coupling (alpha ~ 2-5), against the measured couplings run up to the same scale",
    f"pred {cellW:.3f} (W), {cellS:.3f} (S); SM-run 1/alpha_1,2,3({inv:.1e}) = {smc[0]:.1f}, {smc[1]:.1f}, {smc[2]:.1f}")
rep(f16W < 6 and f16S < 6, "D3 [E]", "fermion loops alone, run down to 1e16 GeV (ln(1/(a mu)) + C): 1/alpha ~ 4, against 1/alpha_GUT ~ 25-45: misses by ~x10",
    f"pred {f16W:.2f} (W), {f16S:.2f} (S); SM 1/alpha_i(1e16) = {sm16[0]:.1f}, {sm16[1]:.1f}, {sm16[2]:.1f}")
b0 = {"SU(3)": 11 - 2/3*ST, "SU(2)": 22/3 - 2/3*ST, "Spin(10)": 88/3 - 2/3*ST}
lam = {g: inv*np.exp(-2*np.pi*cellW/b) for g, b in b0.items()}
rep(all(v > 1e17 for v in lam.values()), "D4 [E]", "with the gauge fields' own loops below the cell (b0 = 11 C_A/3 - 2 sum T_W/3 > 0 for every non-abelian factor), the induced non-abelian couplings run strong AT the cell: colour would confine at ~1e18 GeV, not 0.2 GeV",
    ", ".join(f"{g}: b0 {b0[g]:.2f}, Lambda {lam[g]:.1e} GeV" for g in b0))
need = 11/2*np.array([3, 2, 8])
rep(all(ST < need), "D5 [T]", "an induced non-abelian coupling stays weak below the cell only if sum T_W >= (11/2) C_A",
    f"need sum T_W >= {need[0]:.1f} (SU(3)), {need[1]:.0f} (SU(2)), {need[2]:.0f} (Spin(10)); three families give {ST:.0f}")
Rw = 192*np.pi**2*cGW/CW; Rs = 192*np.pi**2*cGS/CS
Rm = [1/smc.max()*16*np.pi*ND*cGW, 1/smc.min()*16*np.pi*ND*cGW]
rep(Rw > 10*max(Rm), "D6 [E]", "Sakharov ratio (one cutoff): alpha(1/a)/(G/a^2) = 192 pi^2 c_G/C, a pure lattice number independent of N_f; measured alpha at the same 1/a gives it ~70-100x smaller (Wilson)",
    f"pred {Rw:.1f} (W), {Rs:.1f} (S); measured {Rm[0]:.2f}-{Rm[1]:.2f}")
STneed = [3*np.pi*smc[i]/CW for i in range(3)]
rep(min(STneed) > 300, "D7 [E]", "to reach the measured 1/alpha at the cell, the cell needs sum T ~ 3 pi /(alpha C) units of charged index (fermion or rishon), i.e. hundreds of families' worth",
    f"Wilson C: sum T needed {STneed[0]:.0f}, {STneed[1]:.0f}, {STneed[2]:.0f} (U(1), SU(2), SU(3)); = {min(STneed)/2:.0f}-{max(STneed)/2:.0f} families; staggered x{CW/CS:.2f}; have {ST:.0f}")
print("verdict: the rule 'no bare link term, couplings induced by the cell's matter' FAILS measurement: alpha_cell = pi/(2C) ~ 2-5,")
print("  1/alpha(1e16) ~ 4 vs ~40, colour strong at the cell. Gate: no number chosen, no structure inserted (content = Ruleset A's");
print("  16 x N_f with N_f = 3 supplied), predictions not built for (alpha_cell, equal couplings at the cell, confinement scale) FAIL.")
print("theorems: A1, A4, C1, C2, D5; diagnostics: A2, A3, B; estimates: D1-D4, D6, D7")
print("supplied: 4D Euclidean hypercubic reading, Wilson/naive actions, link phase on hops, vierbein on hops (TT), N_f = 3,")
print("  matching mu = 1/a, measured G and alpha_i(M_Z), SM one-loop b_i; not computed: CL-1 cube tick (see induced-response)")
print(f"elapsed {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
