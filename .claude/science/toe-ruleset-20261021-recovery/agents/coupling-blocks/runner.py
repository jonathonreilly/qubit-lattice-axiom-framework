#!/usr/bin/env python3
"""coupling-blocks: gauge couplings at the cell scale from rishon counts of a role-assigned block.

A. exact: F-flavour rishon links (U(1): spin F/2; SU(N): U(2N) rectangular rep N x F) and the
   exact magnitude identity sum_ab U_ab U_ab^+ = (C - C_x - C_y - N(n_x - n_y))/2.
B. estimate (semiclassical, J-free): alpha_SU(N) = 2/(pi sqrt(F(F+2N))), alpha_U(1)link = 1/(pi sqrt(F(F+2))).
C. exact: rotation orbits of a b^3 block, which orbits can host bond ends covariantly, parity of the rest.
D. estimates vs measurement + look-elsewhere count.
"""
import os, time, itertools, math
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
import scipy.sparse as sp
import sympy as sy

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = 0; NF = 0
def check(tag, ok, msg, extra=""):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg}" + (f" | {extra}" if extra else ""))

# ---------------------------------------------------------------- A. exact link algebra
def flavour_ops(N):
    """one flavour: 2N modes (x1..xN, y1..yN) holding N fermions; return e_ij on that sector."""
    M = 2 * N
    basis = [s for s in itertools.combinations(range(M), N)]
    idx = {s: k for k, s in enumerate(basis)}
    d = len(basis)
    e = {}
    for i in range(M):
        for j in range(M):
            A = np.zeros((d, d))
            for s, k in idx.items():
                if j not in s: continue
                if i != j and i in s: continue
                # c_i^+ c_j with JW sign
                sgn = (-1) ** sum(1 for m in s if m < j)
                t = [m for m in s if m != j]
                sgn *= (-1) ** sum(1 for m in t if m < i)
                t = tuple(sorted(t + [i]))
                A[idx[t], k] += sgn
            e[(i, j)] = sp.csr_matrix(A)
    return e, basis, d

def link_rep(N, F):
    e1, basis, d = flavour_ops(N)
    I = sp.identity(d, format="csr")
    def emb(op, f):
        out = None
        for g in range(F):
            m = op if g == f else I
            out = m if out is None else sp.kron(out, m, format="csr")
        return out
    M = 2 * N
    E = {k: sum(emb(v, f) for f in range(F)) for k, v in e1.items()}
    # highest weight: every flavour has its N fermions on the x end
    k0 = basis.index(tuple(range(N)))
    v = np.zeros(d); v[k0] = 1
    psi = v
    for _ in range(F - 1): psi = np.kron(psi, v)
    # Krylov span under all generators
    vecs = [psi]; Q = psi[:, None] / np.linalg.norm(psi)
    frontier = [psi]
    while frontier:
        new = []
        for w in frontier:
            for k, op in E.items():
                u = op @ w
                u = u - Q @ (Q.T @ u)
                nu = np.linalg.norm(u)
                if nu > 1e-9:
                    u = u / nu; Q = np.hstack([Q, u[:, None]]); new.append(u)
        frontier = new
    R = {k: Q.T @ (op @ Q) for k, op in E.items()}
    return R, Q.shape[1]

def weyl_dim(lam):
    n = len(lam); num = 1; den = 1
    for i in range(n):
        for j in range(i + 1, n):
            num *= (lam[i] - lam[j] + j - i); den *= (j - i)
    return num // den

print("== A. exact: F-flavour rishon links (F modes per colour per bond end, N fermions per flavour per link)")
maxdev = 0.0; dims = {}; c2eq = 0.0
for N, Fs in [(1, [1, 2, 3, 4, 5]), (2, [1, 2, 3, 4]), (3, [1, 2])]:
    for F in Fs:
        R, dim = link_rep(N, F)
        dims[(N, F)] = (dim, weyl_dim([F] * N + [0] * N))
        X = range(N); Y = range(N, 2 * N)
        C = sum(R[(i, j)] @ R[(j, i)] for i in range(2 * N) for j in range(2 * N))
        Cx = sum(R[(a, b)] @ R[(b, a)] for a in X for b in X)
        Cy = sum(R[(a, b)] @ R[(b, a)] for a in Y for b in Y)
        nx = sum(R[(a, a)] for a in X); ny = sum(R[(a, a)] for a in Y)
        UUd = sum(R[(b, a)] @ R[(a, b)] for a in X for b in Y)   # U_ab = E_{y b, x a} moves a rishon x -> y
        Cval = N * F * F + N * N * F
        rhs = (Cval * np.eye(dim) - Cx - Cy - N * (nx - ny)) / 2
        maxdev = max(maxdev, np.abs(C - Cval * np.eye(dim)).max(), np.abs(UUd - rhs).max())
        # SU(N) Casimirs of the two ends agree (left = right electric Casimir)
        c2x = Cx - nx @ nx / N; c2y = Cy - ny @ ny / N
        c2eq = max(c2eq, np.abs(c2x - c2y).max())
okdim = all(a == b for a, b in dims.values())
check("A1 [T]", okdim and maxdev < 1e-9,
      "the link sector reached from the filled x end is the U(2N) irrep with N rows of length F (U(1), N=1: spin F/2); "
      "its Casimir is NF^2 + N^2 F, and sum_ab U_ab U_ab^+ = (C - C_x - C_y - N(n_x - n_y))/2 exactly",
      f"dims {[(k, v[0]) for k, v in dims.items()]}, max dev {maxdev:.1e}")
check("A2 [T]", c2eq < 1e-9,
      "the SU(N) electric Casimirs at the two ends are equal on the whole link sector (the link is a rotor: E_R = -u^+ E_L u classically)",
      f"max |C2_x - C2_y| {c2eq:.1e}")
print("   so at n_x = n_y: Tr UU^+ = N F(F+2N)/4 - 2 C2: the link field shrinks with its electric Casimir; F_eff = sqrt(F(F+2N))")

# ---------------------------------------------------------------- B. semiclassical coupling, J-free
F, N, J, e2 = sy.symbols("F N J E2", positive=True)
Feff = sy.Symbol("Feff", positive=True)
# per link magnitude (Feff/2)(1 - 8 Ehat^2/Feff^2), Tr Ehat^2 = E2/2 (E2 = sum_A E^A E^A); four links per plaquette, four plaquettes per link
mag_el = -J * 2 * (Feff / 2) ** 4 * (-(8 / Feff ** 2) * e2 / 2)   # per plaquette per link
coef_E = sy.simplify(mag_el * 4 / e2)                                 # coefficient of sum_l E^2
ge2 = 2 * coef_E                                                      # H_el = (g_e^2/2) sum E^2
gm2 = 1 / (J * (Feff / 2) ** 4)                                       # H_mag = (1/g_m^2) Tr(2 - U_p - U_p^+)
g2 = sy.simplify(sy.sqrt(ge2 * gm2))
# U(1): H_mag = 2 J (Feff/2)^4 (1 - cos B) = (1/g_m^2)(1 - cos B); per link magnitude (Feff/2)(1 - 2E^2/Feff^2)
ge2_u1 = 2 * sy.simplify(-J * 2 * (Feff / 2) ** 4 * (-(2 / Feff ** 2)) * 4)
gm2_u1 = 1 / (2 * J * (Feff / 2) ** 4)
g2_u1 = sy.simplify(sy.sqrt(ge2_u1 * gm2_u1))
check("B1 [E]", sy.simplify(g2 - 8 / Feff) == 0 and sy.simplify(g2_u1 - 4 / Feff) == 0 and J not in g2.free_symbols,
      "large-F ring exchange -J sum Tr(U_p + U_p^+): J cancels; SU(N) g^2 = 8/F_eff, alpha_N = 2/(pi sqrt(F(F+2N))) for every N; "
      "U(1) g^2 = 4/F_eff, alpha_link = 1/(pi sqrt(F(F+2))) = 1/(2 pi sqrt(S(S+1))), S = F/2 (the register's value)",
      f"g^2 SU(N) = {g2}, U(1) = {g2_u1}")
print("   strong/weak map: F=1..4 tree alpha SU(3): " + ", ".join(f"{2/(math.pi*math.sqrt(f*(f+6))):.3f}" for f in [1, 2, 4, 30])
      + " (F=30); box/tree kappa for U(1) (qlm-coulomb): 2.13 (F=1), 1.43 (F=2) ~ 1 + 1.1/F: tolerance band below")

# ---------------------------------------------------------------- C. block orbits
def rotations():
    Rs = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[i, p[i]] = s[i]
            if round(np.linalg.det(M)) == 1: Rs.append(M)
    return Rs
ROT = rotations()
AXES = [np.array(v) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]

def block_orbits(b):
    h = (b - 1) / 2.0
    pts = [tuple(np.array(c) * 2 - (b - 1)) for c in itertools.product(range(b), repeat=3)]  # doubled coords
    seen = set(); orbs = []
    for p in pts:
        if p in seen: continue
        orb = {tuple(R @ np.array(p)) for R in ROT}
        seen |= orb
        stab = [R for R in ROT if tuple(R @ np.array(p)) == p]
        host = any(all(tuple(R @ a) == tuple(a) for R in stab) for a in AXES)
        orbs.append((len(orb), host))
    return orbs

print("== C. exact: 24-rotation orbits of a b^3 block; an orbit hosts bond ends covariantly iff its stabiliser fixes an axis")
BL = {}
okf = True
for b in range(2, 22):
    o = block_orbits(b)
    hostable_sizes = sorted({s for s, hst in o if hst}); non = sorted({s for s, hst in o if not hst})
    K = sum(s // 6 for s, hst in o if hst)                  # rishons per bond end if every hostable site is a rishon
    n6 = sum(1 for s, hst in o if hst and s == 6); n24 = sum(1 for s, hst in o if hst and s == 24)
    M = b ** 3 - 6 * K
    BL[b] = dict(K=K, n6=n6, n24=n24, M=M)
    Kf = (b ** 3 - 10 * b + 9) // 6 if b % 2 else (b ** 3 - 4 * b) // 6
    Mf = 10 * b - 9 if b % 2 else 4 * b
    okf &= (K == Kf and M == Mf and set(hostable_sizes) <= {6, 24} and (b % 2 == 0 or n6 == (b - 1) // 2))
check("C1 [T]", okf, "hostable orbits are exactly the axis 6-orbits (1 site per end) and the 24-orbits (4 per end, one C4 cycle); "
      "centre, 8- and 12-orbits cannot host an end; maximal rishon fill gives K_b = (b^3-10b+9)/6 per end and 10b-9 other sites (odd b), "
      "K_b = (b^3-4b)/6 and 4b other sites on the 8-orbits (even b)",
      "K: " + " ".join(f"{b}:{BL[b]['K']}" for b in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]))
par = all((b ** 3 - 6 * k) % 2 == 1 for b in range(3, 22, 2) for k in range(0, BL[b]['K'] + 1))
check("C2 [T]", par, "parity: in an odd block every covariant rishon set is 6 x (per-end count), so the non-rishon sites number b^3 - 6k = b (mod 6), "
      "always odd: an exhausted odd block cannot hold 16n matter modes (one per role) and nothing else; it needs an odd extra role (the centre)")
sol_odd = [(b, (BL[b]['M'] - 1) // 16) for b in range(3, 22, 2) if (BL[b]['M'] - 1) % 16 == 0]
sol_even = [(b, BL[b]['M'] // 16) for b in range(2, 22, 2) if BL[b]['M'] % 16 == 0]
check("C3 [T]", sol_odd == [(9, 5), (17, 10)] and sol_even == [(4, 1), (8, 2), (12, 3), (16, 4), (20, 5)],
      "maximal fill: odd b gives 16n + centre only at b = 9 (n=5), 17 (n=10); even b gives 4b = 16n on the body-diagonal 8-orbits at b = 4n "
      "(b = 12: exactly three families of 16)", f"odd {sol_odd}, even {sol_even}")

# ---------------------------------------------------------------- D. against measurement
MZ = 91.1876; AINV = 127.951; S2W = 0.23122; AS = 0.1180; A0INV = 137.035999
DELTA0 = A0INV - AINV
inv_meas = {"Y": AINV * (1 - S2W), "2": AINV * S2W, "3": 1 / AS}
BETA = {"Y": 41 / 6, "2": -19 / 6, "3": -7.0}
MBAR = 1.22089e19 / math.sqrt(8 * math.pi)             # 1/a with a = sqrt(8 pi) l_P (G = a^2/8pi)
def inv_at(mu):  # required 1/alpha at mu from measured values (SM one loop, 3 families, 1 Higgs; nu^c has Y=0)
    L = math.log(mu / MZ); return {k: inv_meas[k] - BETA[k] / (2 * math.pi) * L for k in BETA}
def inv_cell(FY, F2, F3):
    return {"Y": math.pi * math.sqrt(FY * (FY + 2)) / 36.0, "2": math.pi * math.sqrt(F2 * (F2 + 4)) / 2,
            "3": math.pi * math.sqrt(F3 * (F3 + 6)) / 2}
def run_down(inv, mu):
    L = math.log(mu / MZ); out = {k: inv[k] + BETA[k] / (2 * math.pi) * L for k in BETA}
    return out
def Freq(invv, k):
    if k == "Y": return -1 + math.sqrt(1 + (36 * invv / math.pi) ** 2)
    Nn = 2 if k == "2" else 3; return -Nn + math.sqrt(Nn ** 2 + (2 * invv / math.pi) ** 2)
def match(Fs, mu, tol=0.02):
    pred = inv_cell(*Fs); need = inv_at(mu); ok = True
    for (k, f) in zip(["Y", "2", "3"], Fs):
        lo = pred[k] / (1 + 1.13 / f) * (1 - tol); hi = pred[k] * (1 + tol)
        ok &= lo <= need[k] <= hi
    return ok
def feasible(FY, F2, F3, b):
    t = [FY, F2, F2, F3, F3, F3]
    return min(t) >= 1 and FY >= 6 and sum(t) == BL[b]['K'] and sum(x // 4 for x in t) >= BL[b]['n24']

mu17 = MBAR / 17
need = inv_at(MBAR); need17 = inv_at(mu17)
print("== D. estimates (tree alpha(F), SM one-loop, measured MZ inputs; cell scale mu = 1/(b a), a = sqrt(8pi) l_P)")
print("   needed 1/alpha (Y unit 1/6 -> link alpha_Y/36) at 1/a: Y %.1f 2 %.1f 3 %.1f -> F_Y %.0f F_2 %.1f F_3 %.1f; at 1/(17a): %.1f %.1f %.1f -> %.0f %.1f %.1f"
      % (need["Y"], need["2"], need["3"], Freq(need["Y"], "Y"), Freq(need["2"], "2"), Freq(need["3"], "3"),
         need17["Y"], need17["2"], need17["3"], Freq(need17["Y"], "Y"), Freq(need17["2"], "2"), Freq(need17["3"], "3")))
fy, f2, f3 = Freq(need17["Y"], "Y"), Freq(need17["2"], "2"), Freq(need17["3"], "3")
check("D1 [E]", fy / f2 > 15 and fy / f3 > 15 and abs(f2 / f3 - 1) < 0.15,
      "any match needs F_Y/F_2 ~ F_Y/F_3 ~ 20 (the 1/6 Gauss unit costs 36, SU(N) links are twice as strong as U(1) at equal F): "
      "the hypercharge register is ~80% of all rishon sites, so no rule that treats the six (factor, colour) classes alike can fit",
      f"F_Y/F_2 {fy/f2:.1f}, F_Y/F_3 {fy/f3:.1f}, rishon share of Y {fy/(fy+2*f2+3*f3):.2f}")

def report(Fs, mu):
    inv = run_down(inv_cell(*Fs), mu)
    if min(inv.values()) <= 0: return None
    s2 = (1 / inv["Y"]) / ((1 / inv["Y"]) + (1 / inv["2"]))
    return dict(a0=inv["Y"] + inv["2"] + DELTA0, s2=s2, as_=1 / inv["3"], inv=inv)

# forced split rules on the maximal fill
rules = {"S1 equal F per class": lambda K: (K / 6, K / 6, K / 6),
         "S2 equal modes per end per factor": lambda K: (K / 3, K / 6, K / 9),
         "S3 modes per end ~ generators 1:3:8": lambda K: (K / 12, K * 3 / 24, K * 8 / 36)}
trials = 0; hits = []; rows = []
for b in range(3, 22):
    K = BL[b]['K']
    for name, fn in rules.items():
        for mu in [MBAR / b, MBAR * math.sqrt(8 * math.pi)]:
            trials += 1
            Fs = fn(K)
            if any(abs(x - round(x)) > 1e-9 for x in Fs): continue
            Fs = tuple(int(round(x)) for x in Fs)
            if not feasible(*Fs, b): continue
            if match(Fs, mu): hits.append((b, name))
            if b == 17 and mu == MBAR / b: rows.append((name, Fs, report(Fs, mu)))
for name, Fs, r in rows:
    print(f"   b=17 {name}: F={Fs} -> " + ("Landau/strong above MZ" if r is None else
          f"1/alpha(0) {r['a0']:.1f}, sin2 {r['s2']:.3f}, alpha_s {r['as_']:.3f}"))
check("D2 [E]", len(hits) == 0, f"forced splits (S1 democratic, S2 equal modes, S3 ~ generator count) on the maximal fill, b = 3..21, two cell scales: "
      f"{trials} trials, {len(hits)} matches; the measured couplings are not reached by any class-symmetric rule", f"hits {hits}")

# free split: F_2, F_3 fitted to the measured alpha_2, alpha_3, F_Y = K_b - 2F_2 - 3F_3 is then forced
tot_splits = sum(1 for b in range(3, 22, 2) for F2 in range(1, BL[b]['K'] // 2 + 1)
                 for F3 in range(1, (BL[b]['K'] - 2 * F2) // 3 + 1) if feasible(BL[b]['K'] - 2 * F2 - 3 * F3, F2, F3, b))
def free_fit(b, mu, s=1.0):
    need = inv_at(mu); F2 = round(Freq(need["2"], "2")); F3 = round(Freq(need["3"], "3"))
    FY = BL[b]['K'] - 2 * F2 - 3 * F3
    return (FY, F2, F3), Freq(need["Y"], "Y") * s
scales = {"1/(b a)": lambda b: MBAR / b, "1/a": lambda b: MBAR}
line = []; within = {}
for sn, sf in scales.items():
    for b in range(3, 22, 2):
        Fs, FYn = free_fit(b, sf(b))
        rat = Fs[0] / FYn if Fs[0] > 0 else 0
        if b in (15, 17, 19): line.append(f"{sn} b{b}: F_Y {Fs[0]} / needed {FYn:.0f} = {rat:.3f}")
        if Fs[0] > 6 and abs(math.log(rat)) < 0.06: within.setdefault(sn, []).append(b)
print("   free split: " + "; ".join(line))
for sn, sf in scales.items():
    Fs, _ = free_fit(17, sf(17)); r = report(Fs, sf(17))
    print(f"   b=17 at {sn}: F={Fs} (S_Y = {Fs[0]/2}) -> 1/alpha(0) {r['a0']:.1f} (137.04), sin2 {r['s2']:.4f} (0.2312), alpha_s {r['as_']:.4f} (0.1180, fitted)")
# chance: rescale the needed F_Y by s, log-uniform over x1/3..x3, and ask whether some odd b lands within 5%
pch = {}
for sn, sf in scales.items():
    rng = np.linspace(-math.log(3), math.log(3), 601); ok_s = 0
    for ls in rng:
        hit = False
        for b in range(3, 22, 2):
            Fs, FYn = free_fit(b, sf(b), math.exp(ls))
            if Fs[0] > 6 and abs(math.log(Fs[0] / FYn)) < 0.06: hit = True
        ok_s += hit
    pch[sn] = ok_s / len(rng)
check("D3 [E]", within.get("1/(b a)") == [17] and within.get("1/a") == [17] and min(pch.values()) > 0.05,
      "with F_2, F_3 fitted (two parameters for two couplings) only the total budget tests anything: it fixes alpha_Y and 1/alpha(0). "
      "Among odd b = 3..21 only b = 17 (K = 792 per end) lands within 6%, at either cell scale; a log-uniform rescaling of the needed F_Y "
      "lands within 6% on some odd b with probability p, so this is chance level, not evidence",
      f"within 6%: {within}, p = {pch['1/(b a)']:.2f}, {pch['1/a']:.2f}; realisable splits on odd b: {tot_splits}")
r12 = None
for F2 in [4, 8]:
    for F3 in [4, 8]:
        FY = BL[12]['K'] - 2 * F2 - 3 * F3
        r = report((FY, F2, F3), MBAR / 12)
        r12 = r12 or r
check("D4 [E]", r12 is None or r12['a0'] < 100,
      "the three-family even block b = 12 (C3) has K = 280 per end, ~3x short: with the smallest colour sets (F = 4, multiples of 4 on 24-orbits) "
      "SU(2) and SU(3) are strong above MZ (or 1/alpha(0) far below 137)", "r12 " + ("strong" if r12 is None else f"{r12['a0']:.0f}"))
print("   integer F quantises the colour couplings: 1/alpha_{2,3}(cell) moves by ~pi/2 per flavour, so alpha_s(MZ) takes only the values "
      + ", ".join(f"{1/run_down(inv_cell(655, 28, f3), MBAR/17)['3']:.3f}" for f3 in (26, 27, 28)) + " near F_3 = 27 (measured 0.1180 lies between)")
print("   b=17 maximal fill leaves 161 non-rishon sites = 10 x 16 + centre (C3): read as light families this contradicts the measured 3 "
      "(and nf = 20 kills asymptotic freedom); with 3 families, 113 sites need another role")
print("supplied: pure ring-exchange plaquette (CL-3 read as -J Tr(U_p+U_p^+)), N fermions per flavour per link, maximal fill, split rules, "
      "cell scale 1/(b a), SM one-loop betas with 3 families, kappa band 1+1.13/F, measured MZ couplings and Delta(1/alpha).")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
