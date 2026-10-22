AUDIT_INPUT_PATHS = ('docs/THE_ZOOM_LADDER_ADDS_NO_FAMILY_CHARGE_SO_ITS_CHARACTERS_GIVE_NO_MASS_TOWER_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""zoom-tower: does reading the zoom-3 family characters on the whole zoom ladder (zoom 3, 9, 27, ...)
give a Froggatt-Nielsen epsilon-tower with epsilon a rung ratio?

Supplied model: the three families are the turn-fixed characters (j,j,j) of CL-1's tick translations
T(2e_i) read at zoom 3 (characters of 2Z^3/6Z^3); a character read at zoom 3^n lives in Z_{3^n}^3;
vacua (spurions) carry characters; a rung-m vacuum (zoom 3^m) carries amplitude eps^m (the lapse clause:
a block of edge L ticks 1/L as often, so eps = 1/3 per zoom-3 step; eps = 1/2, the octree warp, is the
alternative counted in the look-elsewhere). Mass entries psibar_R,i psi_L,j H need character
q_L,j - q_R,i + h = 0 after the spurion insertions; H~ carries -h.
 A targets [M]   B theorems (exact)   C fit-free ensembles vs measurement + look-elsewhere
 D Nelson-Barr theta_bar on the two-rung assignment
"""
AUDIT_TIMEOUT_SEC = 120
import itertools, heapq, time
import numpy as np

T0 = time.time(); NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))
rng = np.random.default_rng(20261022)

# ---------------- A ----------------
MEAS = dict(u32=7e-3, u21=1e-5 / 7e-3, d32=2e-2, d21=1e-3 / 2e-2, Vus=0.225, Vcb=0.042, Vub=0.0037)
LEP = dict(e32=6e-2, e21=3e-4 / 6e-2)
print("== A. targets [M] (as supplied in the task): m_t:m_c:m_u 1:7e-3:1e-5, m_b:m_s:m_d 1:2e-2:1e-3, "
      "m_tau:m_mu:m_e 1:6e-2:3e-4; |V_us|,|V_cb|,|V_ub| 0.225, 0.042, 0.0037")

# ---------------- B ----------------
print("== B. theorems")
# B1 inflation: family j at zoom 3 has T(2e_i) eigenvalue w3^(2j); on Z_{3^n} that is w_N^(2k) with k = 3^(n-1) j only
ok = True; img = {}
for n in (2, 3, 4):
    N = 3 ** n
    for j in range(3):
        ks = [k for k in range(N) if np.isclose(np.exp(2j * np.pi * 2 * k / N), np.exp(2j * np.pi * 2 * j / 3))]
        ok &= ks == [3 ** (n - 1) * j]
        # coarser translation T(6e_i) (zoom-9 block step) acts on family j by exp(2 pi i 6 j/3) = 1
        ok &= np.isclose(np.exp(2j * np.pi * 6 * j / 3), 1)
    img[N] = [3 ** (n - 1) * j for j in range(3)]
check("[T] inflation: the zoom-3 family characters (j,j,j) have exactly one image at every rung, 3^(n-1)(j,j,j) in "
      "Z_{3^n}^3, and the next rung's translations T(6e_i) act trivially on all three: the ladder adds no family "
      "charge, the families still form the order-3 subgroup {0, psi, psi^2}", ok, f"images {img}")

def dijkstra(N, steps):
    """min cost over spurion monomials to reach each character of Z_N (1D: the turn-fixed diagonal); steps: (char, cost)"""
    dist = {0: 0.0}; pq = [(0.0, 0)]
    while pq:
        d, x = heapq.heappop(pq)
        if d > dist.get(x, 1e9): continue
        for c, w in steps:
            y = (x + c) % N
            if d + w < dist.get(y, 1e9) - 1e-12:
                dist[y] = d + w; heapq.heappush(pq, (d + w, y))
    return dist
# B2: any conjugation-closed spurion set on any rung: f(psi) = f(psi^2) -> all three pairs at one suppression
ok = True; ok_h = True; ex = None
for trial in range(300):
    n = rng.integers(2, 5); N = 3 ** n
    chars = rng.choice(np.arange(1, N), size=rng.integers(1, 6), replace=False)
    costs = rng.uniform(0.5, 4, len(chars))
    st = [(int(c), w) for c, w in zip(chars, costs)] + [(int(-c) % N, w) for c, w in zip(chars, costs)]
    f = dijkstra(N, st); q = img[N]
    pair = [f.get((q[b] - q[a]) % N, np.inf) for a, b in ((0, 1), (1, 2), (0, 2))]
    ok &= np.isclose(pair[0], pair[1]) and np.isclose(pair[1], pair[2])
    fh = dijkstra(N, [(int(c), w) for c, w in zip(chars, costs)])        # holomorphic: no conjugates
    ph = [fh.get((q[b] - q[a]) % N, np.inf) for a, b in ((0, 1), (1, 2), (0, 2))]
    ok_h &= np.isclose(ph[0], ph[1]) and len({round(x, 9) for x in ph if np.isfinite(x)}) <= 2
fz = dijkstra(9, [(1, 2.0), (8, 2.0)]); fz3 = dijkstra(9, [(3, 1.0), (6, 1.0), (1, 2.0), (8, 2.0)])
check("[T] no tower from any rung: pair characters are psi, psi, psi^2 = psi^*; any spurion set closed under "
      "conjugation (sigma and sigma^* at one weight) gives f(psi) = f(psi^*), so the 12, 23, 13 pairs open at ONE "
      "suppression whatever the rungs and weights (300 random spurion systems, zoom 9-81); holomorphic sets give at most "
      "two (12 = 23)", ok and ok_h,
      f"pure zoom-9 spurion: degree 3, eps^{fz[3]:.0f}; with the zoom-3 spurion: eps^{fz3[3]:.0f} for every pair")
# B3: the tick keeps k -> -k (family-flux item 3); every negation-closed triple has <= 2 pair classes
res = {}
for N in (6, 8, 9, 16, 18, 27, 32, 81):
    mx_sym = 0; mx_all = 0
    for S in itertools.combinations(range(N), 3):
        cls = {min(d % N, (-d) % N) for d in (S[1] - S[0], S[2] - S[1], S[2] - S[0])}
        mx_all = max(mx_all, len(cls))
        if {(-s) % N for s in S} == set(S): mx_sym = max(mx_sym, len(cls))
    res[N] = (mx_sym, mx_all)
check("[T] k -> -k: in Z_N every family triple closed under negation is {0, k, -k} (or {N/2, k, -k}); its pair "
      "differences fall in at most two classes up to sign, so it has at most two spurion distances, while generic "
      "triples reach three: a three-distance texture needs k -> -k broken in the family sector",
      all(v[0] <= 2 and v[1] == 3 for N, v in res.items() if N > 6), "N: (sym max, all max) " + str(res))
# B4: same family set for doublets and singlets and S a group -> an unsuppressed-class permutation, masses of one order
def texture_exp(S, h, N, wfun):
    return np.array([[wfun((sL - sR + h) % N) for sL in S] for sR in S])
ok = True
for n in (2, 3):
    N = 3 ** n; S = img[N]
    f = dijkstra(N, [(3 ** (n - m), float(m)) for m in range(1, n + 1)] + [((-3 ** (n - m)) % N, float(m)) for m in range(1, n + 1)])
    for h in range(N):
        E = texture_exp(S, h, N, lambda c: f[c])
        # entries depend only on sL - sR: each difference class is a permutation; the cheapest class is a full permutation
        mins = E.min()
        perm_ok = any(all(E[i, p[i]] == mins for i in range(3)) for p in itertools.permutations(range(3)))
        ok &= perm_ok
check("[T] Dirac entries carry differences: with doublet and singlet families on the same subgroup S (rule-forced), "
      "M = sum_g eps^f(g+h) P_g with P_g permutations, so the cheapest class is a full permutation and all three masses "
      "are of one order for every Higgs character h and every rung: the ladder gives no mass hierarchy", ok,
      "all h in Z_9, Z_27, rung-graded weights")

# ---------------- C ----------------
print("== C. fit-free ensembles (complex O(1) coefficients, |c| log-uniform in [1/3,3]; 200 samples/cell; hit = within x3 of each target)")
W = np.log10(3.0); NS = 200
def coeff(*sh): return np.exp(rng.uniform(np.log(1 / 3), np.log(3), sh)) * np.exp(2j * np.pi * rng.uniform(size=sh))
def sv(M):
    U, s, Vh = np.linalg.svd(M)
    return s[:, ::-1], np.conj(np.swapaxes(Vh, 1, 2))[:, :, ::-1]          # ascending; doublet-side vectors
def obs_from(Eu, Ed, El, eps):
    Mu = coeff(NS, 3, 3) * eps ** Eu; Md = coeff(NS, 3, 3) * eps ** Ed; Ml = coeff(NS, 3, 3) * eps ** El
    su, Vu = sv(Mu); sd, Vd = sv(Md); sl, _ = sv(Ml)
    V = np.abs(np.conj(np.swapaxes(Vu, 1, 2)) @ Vd)
    return dict(u32=su[:, 1] / su[:, 2], u21=su[:, 0] / su[:, 1], d32=sd[:, 1] / sd[:, 2], d21=sd[:, 0] / sd[:, 1],
                Vus=V[:, 0, 1], Vcb=V[:, 1, 2], Vub=V[:, 0, 2], e32=sl[:, 1] / sl[:, 2], e21=sl[:, 0] / sl[:, 1])
def score(o):
    hq = np.all([np.abs(np.log10(o[k] / MEAS[k])) < W for k in MEAS], axis=0)
    hm = np.all([np.abs(np.log10(o[k] / MEAS[k])) < W for k in ("u32", "u21", "d32", "d21")], axis=0)
    chi = sum(np.log10(np.median(o[k]) / MEAS[k]) ** 2 for k in MEAS)
    return hq.mean(), hm.mean(), chi
cells = []; nc = 0
for n in (2, 3):
    N = 3 ** n
    graded = [(3 ** (n - m), float(m)) for m in range(1, n + 1)] + [((-3 ** (n - m)) % N, float(m)) for m in range(1, n + 1)]
    laws = dict(graded=dijkstra(N, graded), unit=dijkstra(N, [(1, 1.0), (N - 1, 1.0)]))
    triples = [("forced", img[N])] + [(f"0,+-{k}", [0, k, N - k]) for k in range(1, (N + 1) // 2) if k % (N // 3) != 0]
    for tname, S in triples:
        for lname, f in laws.items():
            for h in range(N):
                Eu = texture_exp(S, h, N, lambda c: f[c]); Ed = texture_exp(S, -h, N, lambda c: f[c])
                Eu = Eu - Eu.min(); Ed = Ed - Ed.min()       # overall scale is the Yukawa normalisation
                for eps in (1 / 3, 1 / 2):
                    o = obs_from(Eu, Ed, Ed, eps); nc += 1
                    cells.append((score(o), N, tname, lname, h, eps, o))
forced = [c for c in cells if c[2] == "forced"]
fm = max(np.median(c[6]["u32"]) for c in forced); fmin = min(np.median(c[6]["u21"] * c[6]["u32"]) for c in forced)
check("[E] rule-forced assignment (inflated zoom-3 characters), every rung, h, weight law and eps in {1/2, 1/3}: "
      "median m1/m3 stays order one, no sample hits the quark mass ratios", all(c[0][1] == 0 for c in forced),
      f"{len(forced)} cells, min median m1/m3 {fmin:.2f}, max joint hit {max(c[0][0] for c in forced):.3f}")
cells.sort(key=lambda c: c[0][2]); b = cells[0]
tot_q = sum(c[0][0] for c in cells) * NS; tot_m = sum(c[0][1] for c in cells) * NS
print(f"   best cell by median log-distance: N={b[1]} S={{{b[2]}}} law={b[3]} h={b[4]} eps={b[5]:.2f} chi={b[0][2]:.2f}; "
      "medians " + " ".join(f"{k} {np.median(b[6][k]):.1e}" for k in list(MEAS) + list(LEP)))
print(f"   look-elsewhere: {nc} cells (2 zooms x triples x 2 weight laws x all h x 2 eps) x {NS}; "
      f"joint 7-hit samples {tot_q:.0f}, mass-4-hit samples {tot_m:.0f}")
# controls
Ea = np.zeros((3, 3)); oa = obs_from(Ea, Ea, Ea, 0.5); sa = score(oa)
qQ, qu, qd = np.array([3, 2, 0]), np.array([4, 1, 0]), np.array([1, 0, 0])
oF = obs_from(np.add.outer(qu, qQ), np.add.outer(qd, qQ), np.add.outer(qd, qQ), 0.22); sF = score(oF)
print(f"   anarchy null: joint {sa[0]:.3f}, masses {sa[1]:.3f}; positive control (supplied U(1) FN, Q=(3,2,0), "
      f"u=(4,1,0), d=(1,0,0), eps=0.22): joint {sF[0]:.3f}, masses {sF[1]:.3f}, chi {sF[2]:.2f}")
bj = max(c[0][0] for c in cells)
check("[E] a supplied ordered U(1) charge (three distinct distances) passes the same test while the best of the ladder's "
      "1548 textures does not: the test can detect a tower, and the ladder does not supply one",
      sF[0] > 5 * bj + 0.01 and b[0][2] > 3 * sF[2],
      f"joint 7-hit rate: best ladder cell {bj:.3f}, FN control {sF[0]:.3f}; median log-distance chi best ladder {b[0][2]:.2f} vs FN {sF[2]:.2f}")

# ---------------- D ----------------
print("== D. Nelson-Barr on the two-rung assignment (Z_9^3 characters)")
N = 9
L = [3 * np.array([j, j, j]) for j in range(3)]; h0 = 3 * np.array([0, 1, 2])
def nb_theta(Nh, extra, S=400, lam_dim5=0.0):
    """rows l(3), qc(Nh); cols Q(3), X(Nh); vacua: heavy coset 3(h0+L_t) plus `extra` characters; returns sin theta_bar"""
    vac = [np.mod(h0 + L[t], N) for t in range(3)] + [np.mod(e, N) for e in extra]
    vval = rng.uniform(0.5, 1.5, (S, len(vac))) * np.exp(2j * np.pi * rng.uniform(size=(S, len(vac))))
    th = np.zeros(S); filled_extra = 0
    for sgn in (+1, -1):                                           # up (H), down (H~ = conj character)
        rows = [L[j] for j in range(3)] + [np.mod(h0 + L[a], N) for a in range(Nh)]
        cols = [L[k] for k in range(3)] + [np.mod(-(h0 + L[a]), N) for a in range(Nh)]
        M = np.zeros((S, 3 + Nh, 3 + Nh), complex)
        for i, rc in enumerate(rows):
            for k, cc in enumerate(cols):
                kap = np.mod(-(rc + cc), N)                         # c_H = 0 in the light subgroup
                if k < 3:
                    if not kap.any(): M[:, i, k] = rng.normal(size=S)  # real Yukawa (kept antiunitary)
                    elif lam_dim5 and i < 3:
                        for t in range(3, len(vac)):
                            if np.array_equal(kap, vac[t]): M[:, i, k] = lam_dim5 * rng.normal(size=S) * vval[:, t]
                            if np.array_equal(np.mod(-kap, N), vac[t]): M[:, i, k] = lam_dim5 * rng.normal(size=S) * np.conj(vval[:, t])
                    continue
                if not kap.any(): M[:, i, k] = 1e3 * (np.abs(rng.normal(size=S)) + 0.3); continue
                for t, v in enumerate(vac):
                    if np.array_equal(kap, v) or np.array_equal(np.mod(-kap, N), v):
                        z = vval[:, t] if np.array_equal(kap, v) else np.conj(vval[:, t])
                        M[:, i, k] += 1e3 * rng.normal(size=S) * z; filled_extra += (t >= 3)
        th += np.angle(np.linalg.det(M))
    return np.abs(np.sin(th)), filled_extra
new9 = [c for c in itertools.product(range(N), repeat=3) if np.mod(c, 3).any()]
ex9 = [np.array(new9[i]) for i in rng.choice(len(new9), 8, replace=False)]
ok = True; det = []
for Nh in (1, 2, 3):
    s, fe = nb_theta(Nh, ex9); ok &= s.max() < 1e-9 and fe == 0; det.append(f"Nh={Nh} {s.max():.0e}")
check("[T, checked] rule-forced two-rung assignment: zoom-9 vacua with non-inflated characters fill no entry at "
      "renormalisable order (every field character is inflated), so the zoom-3 Nelson-Barr texture is unchanged and "
      "arg det(M_u M_d) = 0 exactly", ok, "max |sin theta_bar| " + ", ".join(det))
lam = [3 * np.array([1, 1, 1])]
r = {Nh: nb_theta(Nh, lam) for Nh in (1, 2, 3)}
check("[T, checked] a family-pair (tower) spurion lambda must carry a light-subgroup character; at renormalisable order "
      "it fills the heavy-heavy block qc_a X_b (a != b) with lambda above and lambda^* below the diagonal. The texture "
      "stays block-triangular, so theta_bar = arg det M_hh: real for N_h <= 2 (det = M_0 M_1 - c c' |lambda|^2), "
      "generic for N_h = 3 (the lambda^3 cycle of the three copies)",
      r[1][0].max() < 1e-9 and r[2][0].max() < 1e-9 and np.median(r[3][0]) > 0.05,
      "median |sin theta_bar| " + ", ".join(f"Nh={k} {np.median(v[0]):.2f}" for k, v in r.items()))
s5, _ = nb_theta(1, lam, lam_dim5=1 / 3)
check("[E] even with N_h = 1, the same spurion enters the light block at dimension five (H lambda l Q / Lambda) with "
      "the tower's own strength eps = 1/3: theta_bar ~ eps, against |theta_bar| < 1e-10", np.median(s5) > 1e-2,
      f"median |sin theta_bar| {np.median(s5):.2f}; CP-even tower spurion needed to 1e-10 (supplied)")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
