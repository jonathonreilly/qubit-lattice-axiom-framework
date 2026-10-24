AUDIT_INPUT_PATHS = ('docs/THE_3450_FAR_WALL_TERM_KEEPS_A_UNIQUE_GAPPED_WALL_MODE_CHAIN_STATE_TO_L_18_BUT_ITS_GAP_FALLS_FROM_SIX_TO_EIGHT_MODES_PER_FLAVOUR_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""far-wall-L16: does the gap of the forced 3-4-5-0 far-wall term persist as the wall-mode chain grows?
Model = far-wall-smg section C exactly: far-wall modes |k| < pi/2, antiperiodic k = pi t / L (t odd, |t| < L/2), E_f = s_f sin k,
far-layer amplitude a(k) = sqrt(1 - (1 - cos k)^2), the two fewest-change 6-fermion bond terms l1 = (1,-2,1,2), l2 = (2,1,-2,1),
one coupling g, sectors (Q_A, Q_B, P) with charges (3,4,5,0), (2,1,2,-1). Modes per flavour n: L = 8,10 -> 4; 12,14 -> 6;
16,18 -> 8; 20 -> 10 (a single neutral momentum sector has 3.5e8 states: not computed).
This runner re-verifies L = 12 (g = 0, 200; all neutral and charged momentum sectors) live, then prints the Mac-mini
results for L = 8..18 from the committed data file mini_results.json and applies the criteria fixed BEFORE the larger
runs (criteria_pre_run.txt). Labels: [T] exact, [F] finite diagnostic, [R] recorded mini result (read from file).
Supplied: the wall-mode projection (bulk dropped), the bond forms, g, L. Cited: far-wall-smg (agents/far-wall-smg)."""
AUDIT_TIMEOUT_SEC = 120
import os, sys, json, time, itertools, resource, gc
MINI_RESULTS_JSON = '{"meta":{"engine":"mini_chain.py (Mac mini, Apple M4, 4 threads, nice 10)","date":"2026-10-24","model":"far-wall-smg section C wall-mode chain; l1=(1,-2,1,2), l2=(2,1,-2,1); antiperiodic; |k|<pi/2","peak_rss_gb":6.11,"note":"L=16,18: neutral P=0..L (P,-P degenerate), Q=(3,2) all P; E(-3,-2,P)=E(3,2,P)","peak_footprint_gb":8.5},"summary":[{"L":8,"n":4,"g":0.0,"nP":8,"E0":-5.2262518595,"gap":0.7653668647,"gsP":[0],"E_P2":0.7653668647,"E_P4":1.3065629649,"dim_max":214,"nnz_max":1728,"rss_gb":0.05,"imag_rel":2.8950418117615464e-16,"sp":0.3826834324,"sp_nP":[8,8]},{"L":8,"n":4,"g":40.0,"nP":8,"E0":-6.5541115382,"gap":0.0848915209,"gsP":[0],"E_P2":1.6074350134,"E_P4":2.1994378592,"dim_max":214,"nnz_max":1728,"rss_gb":0.05,"imag_rel":2.8950418117615464e-16,"sp":0.9447569983,"sp_nP":[8,8]},{"L":8,"n":4,"g":200.0,"nP":8,"E0":-25.5187128946,"gap":0.1829345093,"gsP":[0],"E_P2":5.2766720297,"E_P4":7.6023974791,"dim_max":214,"nnz_max":1728,"rss_gb":0.05,"imag_rel":2.8950418117615464e-16,"sp":1.531157504,"sp_nP":[8,8]},{"L":10,"n":4,"g":0.0,"nP":10,"E0":-4.472135955,"gap":0.6180339887,"gsP":[0],"E_P2":0.6180339887,"E_P4":1.1180339887,"dim_max":212,"nnz_max":1728,"rss_gb":0.04,"imag_rel":2.9874826664258086e-16,"sp":0.3090169944,"sp_nP":[10]},{"L":10,"n":4,"g":5.0,"nP":10,"E0":-4.4725886332,"gap":0.6179997925,"gsP":[0],"E_P2":0.6179997925,"E_P4":1.1183734071,"dim_max":212,"nnz_max":1728,"rss_gb":0.04,"imag_rel":2.9874826664258086e-16,"sp":0.3090033692,"sp_nP":[10]},{"L":10,"n":4,"g":40.0,"nP":10,"E0":-4.8962489958,"gap":0.0888259069,"gsP":[0],"E_P2":0.8858507262,"E_P4":1.3941816749,"dim_max":212,"nnz_max":1728,"rss_gb":0.04,"imag_rel":2.9874826664258086e-16,"sp":0.6416527407,"sp_nP":[10]},{"L":10,"n":4,"g":200.0,"nP":10,"E0":-18.3609803984,"gap":0.0926328848,"gsP":[0],"E_P2":2.9896070907,"E_P4":4.8874119415,"dim_max":212,"nnz_max":1728,"rss_gb":0.04,"imag_rel":2.9874826664258086e-16,"sp":1.6069056103,"sp_nP":[10]},{"L":10,"n":4,"g":1000.0,"nP":10,"E0":-89.1876242506,"gap":0.2674478645,"gsP":[0],"E_P2":13.2717149559,"E_P4":22.775128162,"dim_max":212,"nnz_max":1728,"rss_gb":0.04,"imag_rel":2.9874826664258086e-16,"sp":7.8557398517,"sp_nP":[10]},{"L":12,"n":6,"g":0.0,"nP":12,"E0":-7.7274066103,"gap":0.5176380902,"gsP":[0],"E_P2":0.5176380902,"E_P4":0.9659258263,"dim_max":17872,"nnz_max":1135136,"rss_gb":0.07,"imag_rel":2.5856653589517935e-16,"sp":0.2588190451,"sp_nP":[12,12]},{"L":12,"n":6,"g":5.0,"nP":12,"E0":-7.7285687196,"gap":0.5173113631,"gsP":[0],"E_P2":0.5173113631,"E_P4":0.9656729639,"dim_max":17872,"nnz_max":1135136,"rss_gb":0.07,"imag_rel":2.5856653589517935e-16,"sp":0.2586496045,"sp_nP":[12,12]},{"L":12,"n":6,"g":40.0,"nP":12,"E0":-8.9552645108,"gap":0.0790017822,"gsP":[0],"E_P2":0.884545608,"E_P4":1.0752207617,"dim_max":17872,"nnz_max":1135136,"rss_gb":0.07,"imag_rel":2.5856653589517935e-16,"sp":0.6555879601,"sp_nP":[12,12]},{"L":12,"n":6,"g":200.0,"nP":12,"E0":-37.0455889401,"gap":4.0309792958,"gsP":[0],"E_P2":4.0309792958,"E_P4":4.100129901,"dim_max":17872,"nnz_max":1135136,"rss_gb":0.07,"imag_rel":2.5856653589517935e-16,"sp":4.8377491277,"sp_nP":[12,12]},{"L":12,"n":6,"g":1000.0,"nP":12,"E0":-184.4044485645,"gap":20.2595006349,"gsP":[0],"E_P2":20.2595006349,"E_P4":20.4758459795,"dim_max":17872,"nnz_max":1135136,"rss_gb":0.07,"imag_rel":2.5856653589517935e-16,"sp":26.3684804833,"sp_nP":[12,12]},{"L":14,"n":6,"g":0.0,"nP":14,"E0":-6.9879184149,"gap":0.4450418679,"gsP":[0],"E_P2":0.4450418679,"E_P4":0.8460107358,"dim_max":17190,"nnz_max":1121248,"rss_gb":0.07,"imag_rel":4.131927298892403e-16,"sp":0.222520934,"sp_nP":[14,14]},{"L":14,"n":6,"g":5.0,"nP":14,"E0":-6.988792464,"gap":0.4448050556,"gsP":[0],"E_P2":0.4448050556,"E_P4":0.8458025014,"dim_max":17190,"nnz_max":1121248,"rss_gb":0.07,"imag_rel":4.131927298892403e-16,"sp":0.2223986541,"sp_nP":[14,14]},{"L":14,"n":6,"g":40.0,"nP":14,"E0":-7.816829055,"gap":0.063109006,"gsP":[0],"E_P2":0.7289048763,"E_P4":0.9213226232,"dim_max":17190,"nnz_max":1121248,"rss_gb":0.07,"imag_rel":4.131927298892403e-16,"sp":0.5865428353,"sp_nP":[14,14]},{"L":14,"n":6,"g":200.0,"nP":14,"E0":-33.356346003,"gap":3.3596814386,"gsP":[0],"E_P2":3.7876883106,"E_P4":3.3596814386,"dim_max":17190,"nnz_max":1121248,"rss_gb":0.07,"imag_rel":4.131927298892403e-16,"sp":4.3056931612,"sp_nP":[14,14]},{"L":14,"n":6,"g":1000.0,"nP":14,"E0":-166.1347527152,"gap":16.7904621913,"gsP":[0],"E_P2":19.0756637908,"E_P4":16.7904621913,"dim_max":17190,"nnz_max":1121248,"rss_gb":0.07,"imag_rel":4.131927298892403e-16,"sp":23.1818631381,"sp_nP":[14,14]},{"L":16,"n":8,"g":5.0,"nP":8,"E0":-10.2531270327,"gap":0.3898318653,"gsP":[0],"E_P2":0.3898318653,"E_P4":0.7501707329,"dim_max":2267718,"nnz_max":632435392,"rss_gb":4.76,"imag_rel":4.88261417783707e-16,"sp":null,"sp_nP":[]},{"L":16,"n":8,"g":40.0,"nP":9,"E0":-11.7077504958,"gap":0.1128809231,"gsP":[0],"E_P2":0.4717602486,"E_P4":0.6594414286,"dim_max":2267718,"nnz_max":632435392,"rss_gb":4.76,"imag_rel":4.88261417783707e-16,"sp":0.596709413,"sp_nP":[16]},{"L":16,"n":8,"g":200.0,"nP":9,"E0":-43.9052835571,"gap":1.5968943895,"gsP":[0],"E_P2":2.0160451486,"E_P4":1.5968943895,"dim_max":2267718,"nnz_max":632435392,"rss_gb":4.76,"imag_rel":4.88261417783707e-16,"sp":1.5435052599,"sp_nP":[16]},{"L":16,"n":8,"g":1000.0,"nP":9,"E0":-213.1202580536,"gap":6.4486512535,"gsP":[0],"E_P2":10.9845676217,"E_P4":6.4486512535,"dim_max":2267718,"nnz_max":632435392,"rss_gb":5.64,"imag_rel":4.88261417783707e-16,"sp":null,"sp_nP":[]},{"L":18,"n":8,"g":200.0,"nP":10,"E0":-41.6465273709,"gap":1.4435373999,"gsP":[0],"E_P2":2.0208726236,"E_P4":1.4435373999,"dim_max":2133134,"nnz_max":603691296,"rss_gb":6.11,"imag_rel":4.768874404878015e-16,"sp":1.4207122486,"sp_nP":[18]}],"checks":{"sym_P_L16":1.8474111129762605e-13,"verdict":"INCONCLUSIVE"}}'
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'): os.environ[_v] = '1'
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla

T0 = time.time(); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

QA = np.array([3, 4, 5, 0]); QB = np.array([2, 1, 2, -1]); SF = np.array([1, 1, -1, -1])
L1 = (1, -2, 1, 2); L2 = (2, 1, -2, 1)
aF = lambda k: np.sqrt(max(0.0, 1 - (1 - np.cos(k))**2))

class Chain:
    def __init__(self, L):
        t = np.arange(-L + 1, L, 2); t = t[np.abs(t) < L / 2]
        self.L, self.t, self.n = L, t, len(t); self.k = np.pi * t / L; n = self.n
        self.E = np.concatenate([SF[f] * np.sin(self.k) for f in range(4)]); self.amp = np.array([aF(x) for x in self.k])
        occ = np.arange(1 << n); self.N1 = np.array([bin(o).count('1') for o in occ])
        self.T1 = np.array([sum(int(t[i]) for i in range(n) if o >> i & 1) for o in occ]); self.imag_rel = 0.0
    def basis(self, target, P):
        n, M = self.n, 2 * self.L; out = []; occ = np.arange(1 << n, dtype=np.int64)
        for Nv in itertools.product(range(n + 1), repeat=4):
            d = np.array(Nv) - n // 2
            if d @ QA != target[0] or d @ QB != target[1]: continue
            s = [occ[self.N1 == Nv[f]] for f in range(4)]; tt = [self.T1[self.N1 == Nv[f]] for f in range(4)]
            a = (s[0][:, None] | (s[1][None, :] << n)).ravel(); ta = ((tt[0][:, None] + tt[1][None, :]) % M).ravel()
            b = ((s[2][:, None] << 2 * n) | (s[3][None, :] << 3 * n)).ravel(); tb = ((tt[2][:, None] + tt[3][None, :]) % M).ravel()
            bk = {int(c): b[tb == c] for c in np.unique(tb)}
            for c in np.unique(ta):
                need = int((P - c) % M)
                if need in bk: out.append((a[ta == c][:, None] | bk[need][None, :]).ravel())
        return np.sort(np.concatenate(out)) if out else np.zeros(0, np.int64)
    def factor(self, f, p):
        L, n = self.L, self.n; ph = lambda t: np.exp(1j * np.pi * t / L); out = []
        F = [(f * n + i, self.amp[i], int(self.t[i])) for i in range(n)]
        if abs(p) == 1:
            for (g, a, t) in F:
                c = a / np.sqrt(L) * (1 + ph(t)) / 2                      # bond average (psi_x + psi_x+1)/2
                out.append((c, [(g, False)], t) if p > 0 else (np.conj(c), [(g, True)], -t))
        else:
            for (g1, a1, t1), (g2, a2, t2) in itertools.combinations(F, 2):
                c = a1 * a2 / L * (ph(t2) - ph(t1))                       # psi_x psi_x+1
                out.append((c, [(g1, False), (g2, False)], t1 + t2) if p > 0 else (np.conj(c), [(g2, True), (g1, True)], -t1 - t2))
        return out
    @staticmethod
    def apply(st, sg, idx, ops):
        for (j, d) in reversed(ops):
            ok = ((st >> j) & 1) == (0 if d else 1); st, sg, idx = st[ok], sg[ok], idx[ok]
            if not len(st): break
            sg = np.where(np.bitwise_count(st & ((1 << j) - 1)) & 1, -sg, sg); st = st ^ (1 << j)
        return st, sg, idx
    def O(self, B):
        M = 2 * self.L; rows, cols, vals = [], [], []
        def rec(fac, f, st, sg, idx, coef, tsum):
            if f < 0:
                c = self.L * coef
                if abs(c) < 1e-15: return
                self.imag_rel = max(self.imag_rel, abs(c.imag) / abs(c))
                pos = np.searchsorted(B, st); assert np.all(B[pos] == st)
                rows.append(pos); cols.append(idx); vals.append(c.real * sg); return
            for (c, ops, t) in fac[f]:
                if f == 0 and (tsum + t) % M: continue
                s2, g2, i2 = self.apply(st, sg, idx, ops)
                if len(s2): rec(fac, f - 1, s2, g2, i2, coef * c, tsum + t)
        for l in (L1, L2):
            rec([self.factor(f, l[f]) for f in range(4)], 3, B, np.ones(len(B), np.int8), np.arange(len(B)), 1.0 + 0j, 0)
        O = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(len(B), len(B)))
        D = sum(self.E[g] * (((B >> g) & 1) - 0.5) for g in range(4 * self.n))
        return D, O + O.T

def lowest(D, V, g, k, seed):
    H = sp.diags(D) + g * V
    if H.shape[0] <= 1500: return np.linalg.eigvalsh(H.toarray())[:k]
    return np.sort(sla.eigsh(H, k=k, which='SA', tol=1e-10, v0=np.random.default_rng(seed).standard_normal(H.shape[0]),
                             return_eigenvectors=False))

# ------------------------------------------------------------------ A. live L = 12
print("== A. live re-verification at L = 12 (n = 6), g = 0 and 200, all neutral and Q = (3,2) momentum sectors")
L = 12; ch = Chain(L); gs = (0.0, 200.0); neu = {g: {} for g in gs}; chg = {g: {} for g in gs}; dims = []
for P in range(2 * L):
    for Q, store, k in (((0, 0), neu, 2), ((3, 2), chg, 1)):
        B = ch.basis(Q, P)
        if not len(B): continue
        dims.append(len(B)); D, V = ch.O(B)
        for g in gs: store[g][P] = lowest(D, V, g, k, 20261024 + P)
        del D, V, B; gc.collect()
live = {}
for g in gs:
    E0 = min(v[0] for v in neu[g].values()); lv = np.sort(np.concatenate(list(neu[g].values())))
    live[g] = dict(gap=lv[1] - E0, sp=min(v[0] for v in chg[g].values()) - E0,
                   gsP=[P for P, v in neu[g].items() if v[0] - E0 < 1e-8], E_P2=neu[g][2][0] - E0, E_P4=neu[g][4][0] - E0)
    print(f"   g = {g:g}: neutral gap {live[g]['gap']:.4f}, single-particle gap {live[g]['sp']:.4f}, ground state P = {live[g]['gsP']}, "
          f"E(P=2) {live[g]['E_P2']:.3f}, E(P=4) {live[g]['E_P4']:.3f}")
check("A1 [T] g = 0 is the free mirror: neutral gap 2 sin(pi/L), single-particle gap sin(pi/L)",
      abs(live[0.0]['gap'] - 2 * np.sin(np.pi / L)) < 1e-9 and abs(live[0.0]['sp'] - np.sin(np.pi / L)) < 1e-9)
check("A2 [T] the interaction matrix is real in the mode basis (each factor carries phase e^{i pi q / 2L} times i or -i per pair, "
      "and momentum conservation makes the product real): max |Im c| / |c| over all momentum-conserving products",
      ch.imag_rel < 1e-12, f"{ch.imag_rel:.1e}")
r = live[200.0]
check("A3 [F] reproduction gate (far-wall-smg C2): L = 12, g = 200 unique ground state at P = 0, neutral gap 4.031 and "
      "single-particle gap 4.838 (to 1e-3)", r['gsP'] == [0] and abs(r['gap'] - 4.031) < 1e-3 and abs(r['sp'] - 4.838) < 1e-3,
      f"gap {r['gap']:.4f}, sp {r['sp']:.4f}, max sector dim {max(dims)}")

# ------------------------------------------------------------------ B. recorded mini results
print("== B. Mac-mini results (mini_results.json; engine mini_chain.py, same model; [R] = read from file)")
here = os.path.dirname(os.path.abspath(__file__))
MR = json.loads(MINI_RESULTS_JSON)  # embedded copy of the Mac-mini results file
S = {(row['L'], row['g']): row for row in MR['summary']}
m12 = S[(12, 200.0)]
check("B0 [R] the mini engine agrees with the live runner at L = 12, g = 200 (gap, sp to 1e-6)",
      abs(m12['gap'] - r['gap']) < 1e-6 and abs(m12['sp'] - r['sp']) < 1e-6, f"mini {m12['gap']:.6f}, {m12['sp']:.6f}")
print("   L  n  g     neutral-gap  sp-gap   GS-P   E(P2)  E(P4)  gap*L   max sector dim")
for (Lx, g) in sorted(S):
    if g not in (5.0, 40.0, 200.0, 1000.0): continue
    w = S[(Lx, g)]; fm = lambda x: '   NA ' if x is None else f"{x:7.3f}"
    print(f"   {Lx:2d} {w['n']}  {g:5g} {w['gap']:9.4f} {fm(w['sp'])} {str(w['gsP']):>6} {fm(w['E_P2'])}{fm(w['E_P4'])} "
          f"{w['gap'] * Lx:6.2f}   {w['dim_max']}")
for key, val in MR.get('checks', {}).items(): print(f"   {key}: {val}")
G = 200.0; Ls = [Lx for Lx in (12, 14, 16, 18) if (Lx, G) in S]; W = [S[(Lx, G)] for Lx in Ls]
dg = np.array([w['gap'] for w in W]); sg = np.array([w['sp'] for w in W]); LL = np.array(Ls, float)
check("B1 [R] sector coverage at g = 200: every neutral momentum sector P = 0..L computed (P and -P are degenerate: exact at "
      "L = 12, 14 over all P; at L = 16 E(P=30) = E(P=2) to 1e-12) and every Q = (3,2) sector; E(-3,-2,P) = E(3,2,P) (checked "
      "at L = 8, 12, 14), so the single-particle gap is E(3,2) - E0",
      all(w['nP'] == Lx // 2 + 1 or w['nP'] == Lx for Lx, w in zip(Ls, W)) and MR['checks']['sym_P_L16'] < 1e-9,
      f"nP {[w['nP'] for w in W]}, charged sectors {[w['sp_nP'] for w in W]}")
check("B2 [R] unique ground state at g = 200 for L = 12, 14, 16, 18: neutral, P = 0, next state above it by > 1",
      all(w['gsP'] == [0] and w['gap'] > 1 for w in W), "gaps " + ", ".join(f"{x:.3f}" for x in dg))
check("B3 [R] single-particle gap at g = 200 stays > 1 for L = 12..18 (free values sin(pi/L) <= 0.26)",
      all(sg > 1), "sp " + ", ".join(f"{x:.3f}" for x in sg))
# ------------------------------------------------------------------ C. pre-set criteria and trend
print("== C. pre-set criteria (criteria_pre_run.txt, fixed before the L > 12 runs) and finite-size trend, g = 200")
ratio = dg[-1] / dg[0]; dl = dg * LL
crit_pass = all(w['gsP'] == [0] and w['gap'] > 1 and w['sp'] > 1 for w in W) and ratio >= 0.5 and dl[-1] >= 0.75 * dl[-2]
crit_fail = any(w['gap'] < 0.3 for w in W if w['L'] >= 16) or (np.ptp(dl) / dl.mean() < 0.15)
verdict = 'PASS' if crit_pass else ('FAIL' if crit_fail else 'INCONCLUSIVE')
print(f"   gap*L = {', '.join(f'{x:.1f}' for x in dl)} (L = {Ls}); gap(18)/gap(12) = {ratio:.3f}; classification {verdict}")
check("C1 [R] (recorded result) persistence criterion NOT met: gap(18)/gap(12) < 0.5 although every gap stays > 1; the closing "
      "criterion (gap < 0.3, or gap*L constant to 15%) is not met either, so the pre-set classification is INCONCLUSIVE",
      verdict == 'INCONCLUSIVE' and MR['checks']['verdict'] == verdict, f"ratio {ratio:.3f}, gap*L spread {np.ptp(dl)/dl.mean():.2f}")
pair = [(12, 16), (14, 18)]
fr = [S[(b, G)]['gap'] / S[(a, G)]['gap'] for a, b in pair]
nn = [(S[(12, G)]['gap'] * 12, S[(14, G)]['gap'] * 14), (S[(16, G)]['gap'] * 16, S[(18, G)]['gap'] * 18)]
check("C2 [R] the drop sits at the mode-number step: at fixed n the gap tracks 1/L (gap*L equal to 4% within n = 6: L = 12, 14 "
      "and within n = 8: L = 16, 18), while at equal window fraction n/L (12 -> 16, 14 -> 18) the gap falls by ~0.4", all(abs(x / y - 1) < 0.04 for x, y in nn) and all(0.3 < f < 0.5 for f in fr),
      f"gap*L n=6: {nn[0][0]:.1f}, {nn[0][1]:.1f}; n=8: {nn[1][0]:.1f}, {nn[1][1]:.1f}; ratios {fr[0]:.3f}, {fr[1]:.3f}")
A = np.c_[np.ones(len(LL)), 1 / LL]; cf = np.linalg.lstsq(A, dg, rcond=None)[0]; res1 = np.abs(A @ cf - dg).max()
pw = np.polyfit(np.log(LL), np.log(dg), 1)
check("C3 [R] trend fits (4 sizes, 2 mode numbers: a trend, not a limit): gap = D_inf + c/L gives D_inf < 0 with residual > 0.3, "
      "so the data do not support a finite L -> infinity gap of this form; a power law gap ~ L^-p gives p > 2 (faster than the "
      "1/L of a gapless branch)", cf[0] < 0 and res1 > 0.3 and -pw[0] > 2,
      f"D_inf {cf[0]:.2f}, c {cf[1]:.1f}, max residual {res1:.2f}; p {-pw[0]:.2f}")
s1k = [S[(Lx, 1000.0)]['gap'] / 1000.0 for Lx in (12, 14, 16)]; s2 = [S[(Lx, G)]['gap'] / G for Lx in (12, 14, 16)]
check("C4 [R] stronger coupling does not remove the drop: gap/g at g = 1000 falls x0.32 from L = 12 to 16 (x0.40 at g = 200); "
      "L = 12 is linear in g (strong-coupling regime), L = 16 is not yet (gap/g still decreasing between 200 and 1000)", 0.25 < s1k[2] / s1k[0] < 0.4 and abs(s1k[0] / s2[0] - 1) < 0.02 and s1k[2] / s2[2] < 0.9,
      "gap/g at 1000: " + ", ".join(f"{x:.5f}" for x in s1k) + "; at 200: " + ", ".join(f"{x:.5f}" for x in s2))
g5 = [S[(Lx, 5.0)]['gap'] / (2 * np.sin(np.pi / Lx)) for Lx in (12, 14, 16)]
g40 = [S[(Lx, 40.0)]['gap'] for Lx in (12, 14, 16)]
check("C5 [R] weak and intermediate coupling: g = 5 is free-like (gap / 2 sin(pi/L) within 0.2% at L = 12, 14, 16: gapless reading); "
      "g = 40 keeps a small neutral gap (< 0.15, the crossing region) at L = 12, 14, 16",
      all(abs(x - 1) < 2e-3 for x in g5) and all(x < 0.15 for x in g40),
      "g=5 ratios " + ", ".join(f"{x:.4f}" for x in g5) + "; g=40 gaps " + ", ".join(f"{x:.3f}" for x in g40))
print("   Not computed: L = 20 (n = 10; one neutral momentum sector has 3.5e8 states); L = 18 at g != 200; L = 16 charged at g = 5, 1000;")
print("   L = 16, g = 5 at P = 16 (Lanczos stalled on near-degenerate free levels; free-like reading from the other sectors).")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1 << 20)
print(f"Supplied: wall-mode projection (bulk dropped), bond forms, g, L. elapsed {time.time()-T0:.1f}s, peak RSS {rss:.0f} MB")
print(f"TOTAL: PASS={NP} FAIL={NF}")
