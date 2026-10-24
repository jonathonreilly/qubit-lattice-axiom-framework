AUDIT_INPUT_PATHS = ('docs/WALL_LOCAL_ELECTROWEAK_REGISTERS_ARE_REALISABLE_ON_A_CONFINING_LAYER_BULK_BUT_CHOSEN_AND_LEAVE_STABLE_FRACTIONAL_CHARGES_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""wall-local-electroweak: can the rules realise X1 (wall-local electroweak link registers, shared colour,
with a Gauss-law repair)?  Strong-coupling (confining) bulk, layered toys, per-wall anomalies, which factors
can be shared, and consequences (QCD running, mirror-quark stability, relics).
Self-contained (numpy/scipy/stdlib).  Seeded.  Prints < 6000 chars."""
AUDIT_TIMEOUT_SEC = 120
import itertools, math, time
from fractions import Fraction as Fr
import numpy as np
from scipy.special import iv
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

np.random.seed(20261024)
T0 = time.time()
PASS = FAIL = 0
def check(tag, ok, msg):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} {tag}: {msg}")

print("== A. Confining (strong-coupling) bulk between two Coulomb walls ==")
# A1 strip of L mixed plaquettes, interior links integrated: Z(th) = (2pi)^(L-1) sum_n I_n^L e^{in th}
beta, L, N = 0.5, 3, 128
phi = 2*np.pi*np.arange(N)/N; d = 2*np.pi/N
M = np.exp(beta*np.cos(phi[:, None]-phi[None, :]))*d
Znum = np.linalg.matrix_power(M, L)[0]/d
Zch = sum((2*np.pi)**(L-1)*iv(n, beta)**L*np.cos(n*phi) for n in range(-30, 31))
check("A1", np.max(np.abs(Znum-Zch))/np.max(Zch) < 1e-12,
      f"strip integral = sum_n I_n^L e^(in th): rel err {np.max(np.abs(Znum-Zch))/np.max(Zch):.1e}")

# A2 effective inter-wall link Phi = product of layer links; stiffness at leading strong-coupling order
def K_u1(b, Ls): return 2*(iv(1, b)/iv(0, b))**(Ls-1)
def K_su2(b, Ls): return 4*(iv(2, b)/iv(1, b))**(Ls-1)
KcU, KcS = 0.25, 0.5   # mean-field ordering values (4D XY, O(4)); MF underestimates true Kc -> conservative
rows = []
ok = True
for Ls in (3, 4, 8, 16):
    ku = [K_u1(b, Ls) for b in (0.25, 0.5)]; ks = [K_su2(b, Ls) for b in (0.5, 1.0)]
    ok &= max(ku) < KcU and max(ks) < KcS
    rows.append(f"Ls={Ls}: U1 {ku[1]:.1e} SU2 {ks[1]:.1e}")
check("A2", ok, "K_eff below mean-field Kc (U1 b<=0.5, SU2 b<=1): Phi disordered, no A_n-A_f mass; " + "; ".join(rows[:2]))
def bmax(Kf, Kc, Ls):
    lo, hi = 1e-3, 50.0
    for _ in range(60):
        mid = 0.5*(lo+hi); (lo, hi) = (mid, hi) if Kf(mid, Ls) < Kc else (lo, mid)
    return lo
print(f"  max bulk beta for disorder: U1 Ls=4 {bmax(K_u1,KcU,4):.2f}, Ls=16 {bmax(K_u1,KcU,16):.2f}; "
      f"SU2 Ls=4 {bmax(K_su2,KcS,4):.2f}, Ls=16 {bmax(K_su2,KcS,16):.2f}")

# A3 layer mass operator: Coulomb bulk (ordered bonds) vs confining bulk (disordered bonds, gapped bulk layers)
Ls = 8
w = 0.5+np.random.rand(Ls-1)
def lap(wb, bulkmass):
    Lm = np.zeros((Ls, Ls))
    for b, x in enumerate(wb):
        Lm[b, b] += x; Lm[b+1, b+1] += x; Lm[b, b+1] -= x; Lm[b+1, b] -= x
    for s in range(1, Ls-1): Lm[s, s] += bulkmass
    return Lm
ev, V = np.linalg.eigh(lap(w, 0.0)); nz_c = int(np.sum(ev < 1e-10))
flat = np.max(np.abs(V[:, 0]/V[0, 0]-1))
ev2, V2 = np.linalg.eigh(lap(np.zeros(Ls-1), 1.0)); z = V2[:, ev2 < 1e-10]
cross = min(np.sum(np.abs(z[1:, i])**2) for i in range(2))
wl = [min(abs(z[0, i])**2, abs(z[-1, i])**2) for i in range(2)]
check("A3", nz_c == 1 and flat < 1e-12 and z.shape[1] == 2 and max(wl) < 1e-12,
      f"Coulomb bulk: {nz_c} flat zero mode (dev {flat:.0e}); confining bulk: {z.shape[1]} zero modes, "
      f"each on one wall (cross weight {max(wl):.0e})")

# A4 leading kinetic mixing from the 4-strip tube
u = iv(1, 0.5)/iv(0, 0.5)
LsL = np.arange(4, 17, 4); eps = u**(4*(LsL-1))
sl = np.polyfit(LsL, np.log(eps), 1)[0]
check("A4", abs(sl-4*np.log(u)) < 1e-9, f"eps ~ u^(4(Ls-1)), beta_b=0.5: Ls=4 {eps[0]:.1e}, Ls=16 {eps[-1]:.1e}; "
      f"slope {sl:.3f} = 4 ln u")

# A5 transverse flux gap: unit flux through one bulk bond layer, ring of A sites, |E|<=1
def flux_E0(A, g2, q):
    states = [c for c in itertools.product((-1, 0, 1), repeat=A) if sum(c) == q]
    idx = {c: i for i, c in enumerate(states)}
    r, cidx, val = [], [], []
    xp = 1.0/(2*g2)
    for i, c in enumerate(states):
        r.append(i); cidx.append(i); val.append(0.5*g2*sum(e*e for e in c))
        for x in range(A):
            y = (x+1) % A; cc = list(c); cc[x] -= 1; cc[y] += 1
            if abs(cc[x]) <= 1 and abs(cc[y]) <= 1:
                j = idx[tuple(cc)]; r += [i, j]; cidx += [j, i]; val += [-xp, -xp]
    H = coo_matrix((val, (r, cidx)), shape=(len(states),)*2).tocsr()
    return eigsh(H, k=1, which='SA')[0][0]
gap = {}
for g2 in (4.0, 0.5):
    for A in (4, 10):
        gap[(g2, A)] = flux_E0(A, g2, 1)-flux_E0(A, g2, 0)
rs, rw = gap[(4.0, 10)]/gap[(4.0, 4)], gap[(0.5, 10)]/gap[(0.5, 4)]
fo = 2.0-2*(1/8)   # first order: g2/2 minus the unit flux's band bottom 2 x_p (x_p = 1/(2 g2))
check("A5", abs(rs-1) < 0.05 and abs(gap[(4.0, 10)]/fo-1) < 0.02 and rw < 0.7,
      f"flux gap strong g2=4: {gap[(4.0,4)]:.3f}->{gap[(4.0,10)]:.3f} (A=4->10; g2/2-2x_p={fo:.2f}); "
      f"weak g2=0.5: {gap[(0.5,4)]:.3f}->{gap[(0.5,10)]:.3f} (ratio {rw:.2f})")

print("== B. Gauss-law repair: gauge-dressed layer chain ==")
Lc, t = 5, 1.0
basis = [(s,)+E for s in range(Lc) for E in itertools.product((-1, 0, 1), repeat=Lc-1)]
bi = {b: i for i, b in enumerate(basis)}; n = len(basis)
H = np.zeros((n, n)); Hu = np.zeros((Lc, Lc))
for i, b in enumerate(basis):
    s, E = b[0], list(b[1:])
    H[i, i] = 0.7*sum(e*e for e in E)
    if s < Lc-1:                      # hop s->s+1 dressed by the link on bond s (E_s -> E_s - 1)
        EE = E.copy(); EE[s] -= 1
        if abs(EE[s]) <= 1:
            j = bi[(s+1,)+tuple(EE)]; H[i, j] = H[j, i] = -t
for s in range(Lc-1): Hu[s, s+1] = Hu[s+1, s] = -t
Qn = np.diag([(1 if b[0] == 0 else 0)-b[1] for b in basis]).astype(float)       # near-wall charge
Gs = [np.diag([(1 if b[0] == s else 0)-(b[s+1]-b[s]) for b in basis]).astype(float) for s in range(1, Lc-1)]
cQ = np.linalg.norm(H@Qn-Qn@H, 2); cG = max(np.linalg.norm(H@G-G@H, 2) for G in Gs)
Qf = np.diag([1.0 if s >= Lc//2 else 0.0 for s in range(Lc)])
cU = np.linalg.norm(Hu@Qf-Qf@Hu, 2)
check("B1", cQ < 1e-12 and cG < 1e-12 and abs(cU-t) < 1e-12,
      f"dressed: ||[H,Q_near]|| = {cQ:.0e}, bulk Gauss {cG:.0e}; undressed far-only register ||[H,Q_far]|| = {cU:.3f} = t")
# B2 near-wall bound state in its own sector (string of length s costs sigma*s); far-tail amplitude
def tail(Ls, sig, r=0.4):
    Hm = np.diag(sig*np.arange(Ls, dtype=float)); Hm[0, 0] += -t/r
    for s in range(Ls-1): Hm[s, s+1] = Hm[s+1, s] = -t
    v = np.linalg.eigh(Hm)[1][:, 0]; return abs(v[-1]/v[0])
LL = [4, 8, 12, 16]
tl = {sg: [tail(x, sg) for x in LL] for sg in (0.0, 0.5, 2.0)}
d1 = np.log(tl[0.5][1]/tl[0.5][0])/4; d2 = np.log(tl[0.5][3]/tl[0.5][2])/4
check("B2", tl[0.0][3] > tl[0.5][3] > tl[2.0][3] and d2 < d1 < np.log(0.4),
      f"far tail Ls=16: sigma 0 {tl[0.0][3]:.1e} (~0.4^15), 0.5 {tl[0.5][3]:.1e}, 2 {tl[2.0][3]:.1e}; "
      f"log-slope {d1:.2f} -> {d2:.2f} (super-exp.); far-photon charge = 0 exactly")

# B3 per-wall anomalies of one 16 under its own SU2 x U1, colour shared
F = [("3", 2, Fr(1, 6)), ("3b", 1, Fr(-2, 3)), ("3b", 1, Fr(1, 3)), ("1", 2, Fr(-1, 2)), ("1", 1, Fr(1)), ("1", 1, Fr(0))]
dc = {"3": 3, "3b": 3, "1": 1}; A3 = {"3": 1, "3b": -1, "1": 0}; T3 = {"3": Fr(1, 2), "3b": Fr(1, 2), "1": 0}
Y3 = sum(dc[c]*w*y**3 for c, w, y in F); Yg = sum(dc[c]*w*y for c, w, y in F)
S2Y = sum(dc[c]*y for c, w, y in F if w == 2); S3Y = sum(T3[c]*w*y for c, w, y in F)
S33 = sum(A3[c]*w for c, w, y in F); nd = sum(dc[c] for c, w, y in F if w == 2)
check("B3", Y3 == Yg == S2Y == S3Y == S33 == 0 and nd % 2 == 0,
      f"per wall: Y^3 {Y3}, Y-grav {Yg}, SU2^2Y {S2Y}, SU3^2Y {S3Y}, SU3^3 {S33}, doublets {nd} (even)")

print("== C. What fixes which factors are wall-local ==")
conj = {"3": "3b", "3b": "3", "1": "1"}
def vectorlike(S):
    m, mc = {}, {}
    for c, w, y in F:
        mult = (1 if "SU3" in S else dc[c])*(1 if "SU2" in S else w)
        k = (c if "SU3" in S else "1", w if "SU2" in S else 1, y if "U1" in S else Fr(0))
        kc = (conj[k[0]], k[1], -k[2])
        m[k] = m.get(k, 0)+mult; mc[kc] = mc.get(kc, 0)+mult
    if m != mc: return False
    return all(v % 2 == 0 for k, v in m.items() if k[1] == 2 and k[0] == "1" and k[2] == 0)
subs = [S for r_ in (1, 2, 3) for S in itertools.combinations(("SU3", "SU2", "U1"), r_)]
vl = [S for S in subs if vectorlike(S)]
maxi = [S for S in vl if not any(set(S) < set(T) for T in vl)]
check("C1", sorted(maxi) == [("SU2",), ("SU3",)],
      f"shareable (vector-like) sets: {vl}; maximal: {maxi} -> two maxima, no unique choice")
# C2 uniform couplings: 1-loop SM running MZ -> cutoff (supplied PDG inputs)
MZ, LAM = 91.19, 2.4e18
ai = np.array([59.0, 29.6, 1/0.1180]); bsm = np.array([41/10, -19/6, -7.0])
aL = ai-bsm/(2*np.pi)*np.log(LAM/MZ)
check("C2", bsm[2] < bsm[1] < 0 < bsm[0] and abs(aL[1]-aL[2]) < 0.1*aL[2],
      f"b = (41/10, -19/6, -7): colour most asymptotically free, largest Casimir (3 vs 2); 1/alpha at cutoff "
      f"(1,2,3) = ({aL[0]:.1f}, {aL[1]:.1f}, {aL[2]:.1f}): no ordering singles out SU2 x U1 to confine and SU3 not")
bw2 = 4*aL[1]/(4*np.pi); bwY = (5/3)*aL[0]/(4*np.pi)
print(f"  wall lattice betas at cutoff: SU2 {bw2:.1f}, U1_Y {bwY:.1f}; confining bulk needs beta_b <~ 1 -> "
      f"bulk/wall coupling ratio ~{bw2:.0f}x (SU2), ~{bwY/0.5:.0f}x (U1): SUPPLIED")

print("== D. Consequences: shared colour with a heavy mirror ==")
nf = 12; b0 = 11-2*nf/3; b1 = 102-38*nf/3
check("D1", b0 > 0, f"QCD with 6 light + 6 mirror flavours: b0 = {b0:.0f} > 0 (asymptotically free); b1 = {b1:.0f}")
mq = {"u": 2.16e-3, "d": 4.67e-3, "s": 0.093, "c": 1.27, "b": 4.18, "t": 172.7}
def a3inv(vp):
    th = sorted([mq["t"]]+[m*vp/246.0 for m in mq.values()])
    a, mu, nfl = 1/0.1180, MZ, 5
    for m in th+[LAM]:
        m = min(m, LAM); a += (11-2*nfl/3)/(2*np.pi)*np.log(m/mu); mu = m; nfl += 1
        if mu >= LAM: break
    return a
r8, r11 = a3inv(1e8), a3inv(1e11)
lsmax = 6*r8/(4*np.pi)/3.0
check("D2", 0 < r8 < aL[2] and r11 > 0, f"1/alpha3(cutoff) with mirror thresholds: v'=1e8 {r8:.1f}, v'=1e11 {r11:.1f} "
      f"(SM {aL[2]:.1f}); no Landau pole")
print(f"  [E] flat colour over Ls layers: per-layer beta3 = {6*r8/(4*np.pi):.1f}/Ls; >= 5D bulk value ~3 (supplied) "
      f"needs Ls <~ {lsmax:.0f} (isotropic)")
# D3 light-mirror bilinears with H^a H'^b: Y-balance needs 6Y_q in 3Z, impossible
Yq = [Fr(1, 6), Fr(2, 3), Fr(-1, 3)]
found = [(y, yp, a, b) for y in Yq for yp in Yq for a in range(-6, 7) for b in range(-6, 7)
         if -y+Fr(a, 2) == 0 and yp+Fr(b, 2) == 0]
qs = sorted({sum(c) % 1 for nq in (2, -1) for c in itertools.combinations_with_replacement(
    [Fr(2, 3), Fr(-1, 3)] if nq > 0 else [Fr(-2, 3), Fr(1, 3)], abs(nq))})
check("D3", not found and Fr(0) not in qs,
      f"no gauge-invariant light-mirror quark bilinear with H^a H'^b (|a|,|b|<=6); mirror-quark hadrons "
      f"(u'qq, u'qbar) have OUR charge mod 1 in {[str(q) for q in qs]}: stable fractional charges")
# D4 relics [E, supplied]: mirror electron e'e'->g'g' (alpha'=alpha), Omega h^2 = 2.6e-9 GeV^-2 * m^2/(pi alpha^2)
al = 1/137.036
for vp in (1e8, 1e11):
    me = 0.511e-3*vp/246; mu_ = mq["u"]*vp/246
    print(f"  [E] v'={vp:.0e}: m_e'={me:.0f} GeV Omega_e'h2={2.6e-9*me**2/(np.pi*al**2):.1e} (T'=T); "
          f"m_u'={mu_:.0f} GeV, T_RH < {mu_/25:.0f} GeV avoids relics")
print("  [E] coloured stable relic n/n_B >~ 1e-12 (supplied) vs fractional-charge searches <~ 1e-20/nucleon")
check("D4", 2.6e-9*(0.511e-3*1e8/246)**2/(np.pi*al**2) > 0.12,
      "thermal mirror sector overcloses (e') and leaves fractional charges; supplied low T_RH removes both "
      "and the Delta N_eff signal")
print(f"runtime {time.time()-T0:.2f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
