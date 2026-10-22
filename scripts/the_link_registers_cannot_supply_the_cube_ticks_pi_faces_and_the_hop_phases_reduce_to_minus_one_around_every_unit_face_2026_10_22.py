AUDIT_INPUT_PATHS = ('docs/THE_LINK_REGISTERS_CANNOT_SUPPLY_THE_CUBE_TICKS_PI_FACES_AND_THE_HOP_PHASES_REDUCE_TO_MINUS_ONE_AROUND_EVERY_UNIT_FACE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Face-clause unification: can CL-1's fixed hop phases (spin-3/2 overlap = pi flux on every face) be the link
registers' plaquette phases, selected by the half-filled sea against the plaquette law? (finite runner, seeded)

  A  the existing Links layout (registers on B_f-block faces, only crossing odd hops dressed): what flux it can reach,
     its energetics against the CL-3 magnetic term as a function of g^2 and B_f, and the contrast with the current law
  B  a register on every matter edge: R^2 = 1 leaves the inter-cube faces free; the sea's energy against g^2
  C  the photon about the vacuum: the sea's own magnetic response, the CL-3 term read from 1 or from the vacuum,
     and which factor can carry pi
  D  the simplified hop clause ("phase -1 around every unit face"): R^2 = 1, spin-3/2 field, tick with copy mass,
     double cover, dressed hops
  E  passing and the vison cost of a dynamical face register
Hop 1 (static) or the CL-1 tick (Floquet, proper units = quasi-energy per tick / N, N = sin(eps)/sqrt3). Energies per
site. n_m = matter modes per site seen by the register (one qubit per site gives n_m = 1). Supplied: half filling, eps.
"""
import time
import itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
PI = np.pi; S3 = np.sqrt(3); E3 = np.eye(3, dtype=int)
NP = NF = 0


def check(ok, tag, text, vals=""):
    global NP, NF
    ok = bool(ok); NP += ok; NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}" + (f"  {vals}" if vals else ""))


# ------------------------------------------------------------------ supercell Bloch form, hop -exp(iA)
def sites(D):
    return np.array(list(itertools.product(*[range(p) for p in D])))


def build(D, Af, ks, amp=1.0, part=None, dirs=(0, 1, 2)):
    D = np.array(D); S = sites(D); n = len(S); idx = {tuple(s): i for i, s in enumerate(S)}
    H = np.zeros((len(ks), n, n), complex)
    for i, r in enumerate(S):
        for mu in dirs:
            if part is not None and (r[mu] % 2) != part:
                continue
            t = r + E3[mu]; j = idx[tuple(t % D)]
            ph = -amp * np.exp(1j * Af(mu, r)) * np.exp(1j * ks @ (t // D))
            H[:, j, i] += ph; H[:, i, j] += ph.conj()
    return H


def kg(m):
    m = [m] * 3 if np.isscalar(m) else m
    ax = [(np.arange(x) + 0.5) / x * 2 * PI for x in m]
    return np.stack(np.meshgrid(*ax, indexing='ij'), -1).reshape(-1, 3)


def Estat(D, Af, m):
    ks = kg(m); s = 0.0; n = int(np.prod(D)); ch = max(1, int(1.5e6 // n ** 2))
    for i in range(0, len(ks), ch):
        ev = np.linalg.eigvalsh(build(D, Af, ks[i:i + ch])); s += np.sum(np.where(ev < 0, ev, 0))
    return s / len(ks) / n


def expmh(H, t):
    w, v = np.linalg.eigh(H); return (v * np.exp(-1j * t * w)[..., None, :]) @ np.conj(np.swapaxes(v, -1, -2))


def Efloq(D, Af, m, eps):
    ks = kg(m); n = int(np.prod(D))
    U = expmh(build(D, Af, ks, 1 / S3, 1), -eps) @ expmh(build(D, Af, ks, 1 / S3, 0), eps)
    om = -np.angle(np.linalg.eigvals(U))
    return np.sum(np.where(om < 0, om, 0)) / len(ks) / n / (np.sin(eps) / S3)


def fluxes(D, Af):
    D = np.array(D); out = {}
    for r in sites(D):
        for mu, nu in ((0, 1), (1, 2), (2, 0)):
            f = Af(mu, r) + Af(nu, (r + E3[mu]) % D) - Af(mu, (r + E3[nu]) % D) - Af(nu, r)
            out[(tuple(r), mu, nu)] = (f + PI) % (2 * PI) - PI
    return out


ZERO = lambda mu, r: 0.0
KS = lambda mu, r: [0.0, PI * r[0], PI * (r[0] + r[1])][mu]


def reg(B, theta=None, base=ZERO):
    """Links clause: a hop crossing a B-block face (only odd-cube hops can) is dressed by that face's register
    value exp(i theta); theta = None puts the coarse Kogut-Susskind field (pi on every block-edge loop)."""
    def Af(mu, r):
        a = base(mu, r)
        if (r[mu] + 1) % B == 0:
            X = tuple(np.array(r) // B)
            a += theta[(mu,) + X] if theta is not None else [0.0, PI * X[0], PI * (X[0] + X[1])][mu]
        return a
    return Af


def ztube(B, base=ZERO):
    return lambda mu, r: base(mu, r) + (PI * (r[0] // B) if mu == 1 and (r[1] + 1) % B == 0 else 0.0)


EZ, EPI = -1.002431, Estat((2, 2, 2), KS, 24)
GAIN = EZ - EPI
print("AUDIT_TIMEOUT_SEC = 120; seed 20261022; hop 1 or CL-1 tick (proper units), per site; CL-3 magnetic "
      "(1/g^2)(1 - cos) l/S per loop (l/S = 1/B_f); n_m = modes per site per register")

print("== A. the existing Links layout (B_f-block face registers; crossing odd hops dressed; fixed phases removed)")
cov = []
for B in (2, 4):
    P = 2 * B; th = {(mu, a, b, c): RNG.uniform(-PI, PI) for mu in range(3) for a in range(2) for b in range(2) for c in range(2)}
    F = fluxes((P,) * 3, reg(B, th))
    nz = [k for k, v in F.items() if abs(v) > 1e-9]
    edge = all((k[0][k[1]] + 1) % B == 0 and (k[0][k[2]] + 1) % B == 0 for k in nz)
    evenz = max(abs(v) for k, v in F.items() if k[0][k[1]] % 2 == 0 or k[0][k[2]] % 2 == 0)
    cov.append((B, len(nz), len(F), edge, evenz))
ev0 = np.linalg.eigvalsh(build((2, 2, 2), ZERO, np.zeros((1, 3)), 1 / S3, 0)[0])
check(all(c[3] and c[4] < 1e-12 and c[1] == c[2] // c[0] ** 2 for c in cov) and abs(ev0[0] + S3) < 1e-12, "A1 [T+D]",
      "reach: without the fixed phases, registers put flux only on block-edge fine faces (1/B_f^2 per "
      "orientation, odd-cube faces); even-cube and inter-cube faces read 0, so R_even is the bare hop (R^2 != 1) at "
      "every register value: the pi sector is unreachable",
      "; ".join(f"B_f={c[0]}: {c[1]}/{c[2]} nonzero, at block edges {c[3]}, max even/mixed {c[4]:.0e}" for c in cov)
      + f"; R_even spectrum {np.round(ev0[[0, 1, 7]], 4)}")

gA = {}
for B, m in ((2, 8), (4, 4)):
    P = (2 * B,) * 3; e0 = Estat(P, ZERO, m); gA[B] = (e0 - Estat(P, reg(B), m), Estat(P, reg(B, base=KS), m) - Estat(P, KS, m))
tub = {}
for B in (2, 4, 6, 8):
    D = (2 * B, B, 1); m = (int(np.ceil(64 / (2 * B))), int(np.ceil(64 / B)), 48)
    tub[B] = Estat(D, ZERO, m) - Estat(D, ztube(B), m)
xc = {B: 6 / B ** 4 / gA[B][0] for B in gA}; lt = {B: tub[B] * B ** 2 for B in tub}
ltinf = np.mean([lt[6], lt[8]]); xinf = lambda B: 2 / (ltinf * B ** 2)
check(all(gA[B][0] > 0 for B in gA) and all(tub[B] > 0 for B in tub) and abs(lt[8] / lt[6] - 1) < 0.1 and xc[4] < xc[2],
      "A2 [D]", "reachable energetics (pi on every block-edge loop vs magnetic 6/(g^2 B_f^4) per site): the sea gains; "
      "a lone pi flux line binds (gain per length converges), so n_m g_c^2 ~ 2/(lambda B_f^2): at large B_f the "
      "zero-flux photon vacuum goes to a pi flux-line crystal, still with no fine Dirac cone",
      f"gain/site B_f=2: {gA[2][0]:.4f} (n_m g_c^2 {xc[2]:.1f}), B_f=4: {gA[4][0]:.4f} ({xc[4]:.1f}); line gain per length "
      + ", ".join(f"B={B}: {lt[B]:.4f}" for B in lt) + f"; lambda ~ {ltinf:.4f}; n_m g_c^2 at B_f = 12, 27: {xinf(12):.2f}, {xinf(27):.3f}")
ktub = {B: Estat((2 * B, B, 1), ztube(B, KS), (int(np.ceil(64 / (2 * B))), int(np.ceil(64 / B)), 48))
        - Estat((2 * B, B, 1), KS, (int(np.ceil(64 / (2 * B))), int(np.ceil(64 / B)), 48)) for B in (4, 8)}
check(all(gA[B][1] > 0 for B in gA) and all(v > 0 for v in ktub.values()), "A3 [D]",
      "current law: on CL-1's pi background the same register flux COSTS energy, so the registers' vacuum "
      "is zero flux at every g^2 and B_f",
      f"cost/site B_f=2: {gA[2][1]:.4f}, 4: {gA[4][1]:.4f}; flux line on pi background, cost per length B=4: "
      f"{ktub[4] * 16:.4f}, B=8: {ktub[8] * 64:.4f}")
fl = {}
for eps in (0.3, 0.8, 1.2):
    z = Efloq((2, 2, 2), ZERO, 12, eps); fl[eps] = (z - Efloq((2, 2, 2), KS, 12, eps), Efloq((4, 4, 4), ZERO, 6, eps) - Efloq((4, 4, 4), reg(2), 6, eps))
check(all(v[0] > v[1] > 0 for v in fl.values()), "A4 [D]",
      "CL-1 tick (Floquet vacuum, proper units): same ordering at finite step",
      "; ".join(f"eps={e}: full-pi gain {v[0]:.4f}, B_f=2 register gain {v[1]:.4f}" for e, v in fl.items()))

print("== B. a register on every matter edge (new carrier): R^2 = 1 fixes cube faces only; the sea fixes the rest")
D2 = (2, 2, 2); oddE = [(mu, r) for mu in range(3) for r in itertools.product((0, 1), repeat=3) if r[mu] == 1]
cls = {}
for bits in range(4096):
    sg = {(mu, r): (bits >> i) & 1 for i, (mu, r) in enumerate(oddE)}
    Af = (lambda sg: (lambda mu, r: KS(mu, r) if r[mu] % 2 == 0 else PI * sg[(mu, tuple(r))]))(sg)
    F = fluxes(D2, Af)
    if not all(abs(abs(v) - PI) < 1e-9 for k, v in F.items() if k[0][k[1]] % 2 == k[0][k[2]] % 2):
        continue
    c = sum(abs(v) > 1 for k, v in F.items() if (k[0][k[1]] + k[0][k[2]]) % 2 == 1)
    cls.setdefault(c, []).append(Af)
Ec = {c: [Estat(D2, a, 12) for a in v] for c, v in cls.items()}
Fq = {c: Efloq(D2, v[0], 12, 0.8) for c, v in cls.items()}
cs = sorted(Ec); spread = max(np.ptp(v) for v in Ec.values())
check(sum(len(v) for v in cls.values()) == 128 and cs == [0, 4, 6, 8, 12] and spread < 1e-9
      and all(np.diff([np.mean(Ec[c]) for c in cs]) < 0) and all(np.diff([Fq[c] for c in cs]) < 0)
      and abs(np.mean(Ec[12]) - Estat(D2, KS, 12)) < 1e-12, "B1 [D]",
      "even cube fixed, all 128 odd-cube fields with R^2 = 1 (2^3 cell): the 12 inter-cube faces per cell are "
      "free; energy falls with each inter-cube pi face (static, eps 0.8); least = pi on every face; inter-cube all 0 "
      "lies above the zero-flux sea",
      "static: " + ", ".join(f"{c} pi: {np.mean(Ec[c]):.5f}" for c in cs) + f" (zero flux {EZ}); eps=0.8: "
      + ", ".join(f"{Fq[c]:.4f}" for c in cs))
xy = Estat(D2, lambda mu, r: [0.0, PI * r[0], 0.0][mu], 12)
pats = [("zero", 0, 0.0), ("odd faces (=B_f 2)", 0.75, gA[2][0]), ("xy layers", 1.0, EZ - xy)] + \
       [(f"R^2=1, {c} mixed", (12 + c) / 8, EZ - np.mean(Ec[c])) for c in cs]
win = []
for x in np.geomspace(0.5, 200, 400):
    win.append((x, min(pats, key=lambda p: -p[2] + 2 * p[1] / x)[0]))
xs = next(x for x, w in win if w == "R^2=1, 12 mixed"); inter = sorted({w for _, w in win} - {"zero", "R^2=1, 12 mixed"})
check(abs(xs - 6 / GAIN) / xs < 0.05 and inter == [], "B2 [D]",
      "winner against CL-3's (1/g^2)(1 - cos) per fine face: zero flux until n_m g^2 = 6/0.191, then pi on "
      "every face at once; Floquet thresholds 6/gain (A4)",
      f"switch at n_m g^2 = {xs:.1f}; intermediate winners: {inter or 'none'}; eps .3/.8/1.2: "
      + ", ".join(f"{6 / v[0]:.1f}" for v in fl.values()) + "; alpha_c = g_c^2/(4 pi) = " + f"{6 / GAIN / (4 * PI):.2f}/n_m")

print("== C. the photon about the vacuum")
q_ = (8, 16, 32, 48); cpi = {}; c0 = {}
for q in q_:
    d = 2 * PI / q; m = (max(1, int(np.ceil(96 / q))), 24, 48)
    cpi[q] = (Estat((q, 2, 1), (lambda d: lambda mu, r: [0.0, (PI + d) * r[0], PI * (r[0] + r[1])][mu])(d), m) - EPI) / d ** 2
    c0[q] = (Estat((q, 2, 1), (lambda d: lambda mu, r: [0.0, d * r[0], 0.0][mu])(d), m) - EZ) / d ** 2
sl = (cpi[48] - cpi[16]) / np.log(3)
check(all(v > 0 for v in cpi.values()) and all(np.diff([cpi[q] for q in q_]) > 0) and all(v < 0 for v in c0.values()),
      "C1 [D]", "uniform field delta = 2 pi/q per xy face: about pi the sea is diamagnetic, growing with ln(1/delta) "
      "(Dirac vacuum polarisation); about 0 paramagnetic: the matter's magnetic minimum is at pi",
      "c = dE/delta^2 about pi: " + ", ".join(f"q={q}: {cpi[q]:.4f}" for q in q_) + f" (slope/ln {sl:.4f}, not asymptotic; "
      f"continuum 1/(48 pi^2) = {1 / (48 * PI ** 2):.4f}); about 0: "
      + ", ".join(f"{c0[q]:.4f}" for q in q_))
xs_pi = {q: 1 / (2 * cpi[q]) for q in q_}
check(all(1 / (2 * cpi[q]) > 1 for q in q_), "C2 [T+D]",
      "photon stiffness per xy face: CL-3's term read from 1 gives -1/(2g^2) about pi, so pi with photons "
      "needs n_m c > 1/(2g^2); read from the vacuum holonomy (n - Re tr(U_vac^dag U)) it gives +1/(2g^2) about the "
      "sea-selected vacuum (pi; B1), stiffness 1/(2g^2) + n_m c > 0 at every g",
      "n_m g^2 needed (read from 1), by q: " + ", ".join(f"{q}: {xs_pi[q]:.1f}" for q in q_))
mult = [("Q", 1, 1, 1 / 6), ("u", 1, 0, 2 / 3), ("d", 1, 0, -1 / 3), ("L", 0, 1, -1 / 2), ("e", 0, 0, -1.0), ("nu_R", 0, 0, 0.0)]
th = np.linspace(0, 12 * PI, 240001); best = 9.0
for k in range(3):
    for j in range(2):
        dev = np.max([np.abs(np.exp(2j * PI * k * t / 3) * (-1) ** (j * dd) * np.exp(1j * th * y) + 1) for _, t, dd, y in mult[:5]], 0)
        best = min(best, dev.min())
check(best > 0.5, "C3 [T]", "no element of SU(3) x SU(2) x U(1)_Y acts as -1 on every measured multiplet (u_R, d_R force "
      "exp(i theta) = 1, then e_R gets +1): pi must sit in a factor acting alike on all modes (fermion parity Z2; a "
      "U(1)_F photon is excluded)",
      f"min_g max_multiplet |g + 1| = {best:.3f}")

print("== D. the simplified hop clause: 'phase -1 around every unit face' (no spin-3/2 construction)")
Cc = np.array(list(itertools.product((0, 1), repeat=3)))
NN = [(a, b) for a in range(8) for b in range(8) if a < b and np.sum((Cc[a] - Cc[b]) ** 2) == 1]
def cubeW(Af):
    Wd = [np.zeros((8, 8), complex) for _ in range(3)]
    for a, b in NN:
        mu = int(np.argmax(Cc[b] - Cc[a])); v = -np.exp(1j * Af(mu, Cc[a])); Wd[mu][b, a] = v; Wd[mu][a, b] = np.conj(v)
    return Wd
gz = RNG.uniform(-PI, PI, 8); Gd = np.diag(np.exp(1j * gz))
W1 = [Gd @ w @ Gd.conj().T for w in cubeW(KS)]; flip = cubeW(KS); flip[0][4, 0] *= -1; flip[0][0, 4] *= -1
okR = []
for _ in range(5):
    wt = RNG.uniform(0.2, 2, 3); wt /= np.linalg.norm(wt)
    okR.append(np.abs(sum(wt[i] * W1[i] for i in range(3)) @ sum(wt[i] * W1[i] for i in range(3)) - np.eye(8)).max())
Rf = sum(flip) / S3
check(max(okR) < 1e-12 and np.abs(Rf @ Rf - np.eye(8)).max() > 0.1, "D1 [T]",
      "-1 on every cube face <=> {W_i, W_j} = 0 <=> (sum w_i W_i)^2 = sum w_i^2 for any positive weights; "
      "one flipped link breaks it",
      f"max |R^2 - 1| (5 weights, random gauge) {max(okR):.0e}; flipped {np.abs(Rf @ Rf - np.eye(8)).max():.2f}")


def Jm(j):
    dd = int(round(2 * j + 1)); mm = j - np.arange(dd); Jp = np.zeros((dd, dd), complex)
    for a in range(1, dd):
        Jp[a - 1, a] = np.sqrt(j * (j + 1) - mm[a] * (mm[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(mm).astype(complex)]


J3 = Jm(1.5); XI = []
for c in Cc:
    n_ = (2 * c - 1.0) / S3; w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
lab = lambda p: int((p[0] % 2) * 4 + (p[1] % 2) * 2 + p[2] % 2)
def A32(mu, r):
    g = XI[lab(np.array(r) + E3[mu])].conj() @ XI[lab(r)]; return float(np.angle(g))
F32 = fluxes(D2, A32); allm = max(abs(abs(v) - PI) for v in F32.values())
gl = RNG.uniform(-PI, PI, 8); AKg = lambda mu, r: KS(mu, r) + gl[lab(np.array(r) + E3[mu])] - gl[lab(r)]


def tick(Af, ks, eps=0.3, mu=0.1, MN=0.3):
    Re = build(D2, Af, ks[:1], 1 / S3, 0)[0]; Ri = [build(D2, Af, ks[:1], 1.0, 0, (i,))[0] for i in range(3)]
    s = 1j * Ri[0] @ Ri[1] @ Ri[2] @ Re; C = expmh(-(MN / 4) * (np.eye(8) - s) @ Re, 1.0)
    Ro = build(D2, Af, ks, 1 / S3, 1)
    return expmh(Ro, -(eps + mu / 2)) @ C @ expmh(Re, eps - mu / 2) @ C, np.linalg.eigvalsh((s + s.conj().T) / 2)


ks6 = kg(6); U1, s1 = tick(A32, ks6); U2, s2 = tick(AKg, ks6)
qa = np.sort(np.angle(np.linalg.eigvals(U1)).ravel()); qb = np.sort(np.angle(np.linalg.eigvals(U2)).ravel())
kd = np.array(list(itertools.product((0, PI / 2, PI, 3 * PI / 2), repeat=3)))
gap = np.abs(np.angle(np.linalg.eigvals(tick(A32, kd, mu=0.0, MN=0.0)[0]))).min()
check(allm < 1e-9 and np.abs(qa - qb).max() < 1e-10 and np.allclose(s1, s2) and np.allclose(np.sort(s1), [-1] * 4 + [1] * 4) and gap < 1e-12,
      "D2 [T+D]", "the spin-3/2 field has -1 on EVERY face (cube faces and the 12 inter-cube faces per cell): "
      "gauge-equivalent to '-1 around every unit face'; the tick with mu and copy mass has identical quasi-energies, "
      "copy-sign spectrum and Dirac point",
      f"max ||F| - pi| {allm:.0e}; |quasi diff| (eps .3, mu .1, MN .3) {np.abs(qa - qb).max():.0e}; "
      f"s = {np.round(s1, 6).tolist()[::4]} x4; min |w| (mu = 0) {gap:.0e}")


def rot_op(Rm, Wd):
    perm = [int(np.argmin(np.sum((Cc - (Rm @ (c - 0.5) + 0.5)) ** 2, 1))) for c in Cc]
    Pm = np.zeros((8, 8)); Pm[perm, range(8)] = 1; M = sum(Wd); Mp = Pm @ M @ Pm.T; g = np.zeros(8, complex); g[0] = 1; done = {0}
    while len(done) < 8:
        for a, b in NN:
            for x, y in ((a, b), (b, a)):
                if y in done and x not in done:
                    g[x] = M[x, y] * g[y] / Mp[x, y]; done.add(x)
    O = np.diag(g) @ Pm
    return O, np.abs(O @ M @ O.conj().T - M).max()


Wk = cubeW(KS); Oz, ez = rot_op(np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]), Wk); Ox, ex = rot_op(np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]), Wk)
Om, em = rot_op(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]), Wk); O3, e3 = rot_op(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]), Wk)
comm = Oz @ Ox @ np.linalg.inv(Oz) @ np.linalg.inv(Ox); lam = comm[0, 0]
check(max(ez, ex, em, e3) < 1e-12 and np.abs(comm - lam * np.eye(8)).max() < 1e-12 and abs(lam + 1) < 1e-12, "D3 [T]",
      "rotations: each maps the all-minus class to itself, so is a symmetry of R up to a site gauge "
      "(90, 120, 180 deg); compensated half-turns about z and x anticommute: half-integer spin, the double cover, derived",
      f"max |O R O^dag - R| {max(ez, ex, em, e3):.0e}; O_z O_x O_z^-1 O_x^-1 = {lam.real:+.0f} x 1")
thd = {(mu, a, b, c): RNG.uniform(-PI, PI) for mu in range(3) for a in range(2) for b in range(2) for c in range(2)}
G4 = RNG.uniform(-PI, PI, 64); S4 = sites((4, 4, 4)); ix = {tuple(s): i for i, s in enumerate(S4)}
A32d = reg(2, thd, A32); AKd = reg(2, thd, lambda mu, r: KS(mu, r) + G4[ix[tuple((np.array(r) + E3[mu]) % 4)]] - G4[ix[tuple(r)]])
ks3 = kg(3); qd = [np.sort(np.angle(np.linalg.eigvals(expmh(build((4, 4, 4), A, ks3, 1 / S3, 1), -0.3) @ expmh(build((4, 4, 4), A, ks3, 1 / S3, 0), 0.3))).ravel()) for A in (A32d, AKd)]
check(np.abs(qd[0] - qd[1]).max() < 1e-10, "D4 [T+D]",
      "dressed hops: the same random registers on crossing odd hops (B_f = 2) give the same dressed tick for "
      "both fields: dressed cones, species eps and mu, and the split's C3v are unchanged",
      f"|quasi difference| on 4^3 cells {np.abs(qd[0] - qd[1]).max():.0e}")

print("== E. passing; the cost of a dynamical face register")
vis = {}
for P in (4, 6):
    Af = (lambda P: lambda mu, r: KS(mu, r) + (PI if (mu == 0 and tuple(r) == (0, 0, 0)) else 0.0))(P)
    m = {4: 6, 6: 4}[P]; vis[P] = (Estat((P,) * 3, Af, m) - Estat((P,) * 3, KS, m)) * P ** 3
check(all(v > 0 for v in vis.values()) and abs(vis[6] / vis[4] - 1) < 0.15, "E1 [T+D]",
      "Stokes: children at pi read +1 around a parent face, so a dynamical face register cannot pass pi "
      "per face (pi-flux-fold D1); each split seeds visons (one flipped link), each costing the sea; the kinematic "
      "clause fixes each rung directly", f"vison cost {vis[4]:.4f} (4^3 cells), {vis[6]:.4f} (6^3)")
print(f"time {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
