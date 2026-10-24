AUDIT_INPUT_PATHS = ('docs/THE_CAYLEY_COMPLETION_OF_THE_CHARGE_FOUR_TERM_HALVES_THE_GAPPING_COUPLING_OF_THE_EIGHT_MAJORANA_PROXY_CHAIN_BUT_BOTH_FORMS_PERSIST_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""cayley-mirror-gap runner. (A) on-site Cayley check (w2): so(8) stabilisers, spectra, Spin(7) singlet ground state.
(B) momentum-sector engine gate against full Fock at L = 2. (C) live L = 4 chain (8 Majoranas / site, SO(8) hopping,
on-site g ReOmega^ or g [ReOmega^ + (1/2) omega^omega^]) vs the embedded mini results. (D) embedded L = 4..8 results
(Mac mini, chain.py) and the pre-set classification (criteria_pre_run.txt)."""
import itertools, json, math, sys
import numpy as np

AUDIT_TIMEOUT_SEC = 120
np.random.seed(20261024)
IP = np.array([1, 1j, -1, -1j])
PASS = FAIL = 0

def check(name, ok, info=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(('PASS' if ok else 'FAIL') + ' ' + name + (': ' + info if info else ''))

# ---------------- local algebra ----------------
D16 = 16
def cop(j):
    M = np.zeros((D16, D16))
    for s in range(D16):
        if s >> j & 1: M[s ^ (1 << j), s] = (-1) ** bin(s & ((1 << j) - 1)).count('1')
    return M
C = [cop(j) for j in range(4)]
G = []
for j in range(4): G += [C[j] + C[j].T, -1j * (C[j] - C[j].T)]
REO = []
for ch in itertools.product([0, 1], repeat=4):
    ph = 1j ** sum(ch)
    if abs(ph.real) > .5: REO.append((ph.real, [2 * j + ch[j] for j in range(4)]))
W2 = [(1.0, [2 * j, 2 * j + 1, 2 * k, 2 * k + 1]) for j, k in itertools.combinations(range(4), 2)]
op4 = lambda T: sum(cf * G[a] @ G[b] @ G[c] @ G[d] for cf, (a, b, c, d) in T)
def form(T):
    F = np.zeros((8,) * 4)
    for cf, idx in T:
        for p in itertools.permutations(range(4)):
            F[tuple(idx[i] for i in p)] += cf * round(np.linalg.det(np.eye(4)[list(p)]))
    return F
def stab(F):
    rows = []
    for a, b in itertools.combinations(range(8), 2):
        X = np.zeros((8, 8)); X[a, b], X[b, a] = 1, -1
        rows.append((np.einsum('ia,abcd->ibcd', X, F) + np.einsum('jb,abcd->ajcd', X, F) +
                     np.einsum('kc,abcd->abkd', X, F) + np.einsum('ld,abcd->abcl', X, F)).ravel())
    return 28 - np.linalg.matrix_rank(np.array(rows), tol=1e-9)
def spec(H):
    v, c = np.unique(np.round(np.linalg.eigvalsh(H), 8), return_counts=True); return [(float(a), int(b)) for a, b in zip(v, c)]

print('== A. on-site 4-forms on 8 Majoranas (4 complex modes) ==')
OP = {'ReO': op4(REO), 'w2': op4(W2), 'Cay': op4(REO + W2)}
st = {k: stab(form(T)) for k, T in (('ReO', REO), ('w2', W2), ('Cay', REO + W2))}
sp_ = {k: spec(OP[k]) for k in OP}
for k in OP: print(f'  {k}: stabiliser {st[k]}, spectrum {sp_[k]}')
check('A1 stabiliser dims 15 (SU4), 16 (U4), 21 (Spin7)', (st['ReO'], st['w2'], st['Cay']) == (15, 16, 21))
check('A2 spectra: ReO -8(1),0(14),+8(1); Cay -14(1),0(8),+2(7)',
      sp_['ReO'] == [(-8., 1), (0., 14), (8., 1)] and sp_['Cay'] == [(-14., 1), (0., 8), (2., 7)])
e, V = np.linalg.eigh(OP['Cay']); gs = V[:, 0]; eo, Vo = np.linalg.eigh(OP['ReO'])
bil = [G[a] @ G[b] for a, b in itertools.combinations(range(8), 2)]
A = np.array([(B @ OP['Cay'] - OP['Cay'] @ B).ravel() for B in bil]).T
ncomm = 28 - np.linalg.matrix_rank(A, tol=1e-9)
ns = np.linalg.svd(A)[2][np.linalg.matrix_rank(A, tol=1e-9):]
gens = [sum(c * B for c, B in zip(v, bil)) for v in ns]
sing = max(np.linalg.norm(Gm @ gs) for Gm in gens)
check('A3 Cayley ground state = ReO ground state (-8 - 6 = -14), even, annihilated by the 21 commuting bilinears',
      abs(abs(np.vdot(gs, Vo[:, 0])) - 1) < 1e-10 and ncomm == 21 and sing < 1e-10, f'commutant {ncomm}, max |X gs| = {sing:.1e}')
check('A4 on-site gap 8 -> 14 (ratio 7/4), 14-fold middle level replaced by 8 (odd) + 7 (even)', abs((e[1] - e[0]) / (eo[1] - eo[0]) - 1.75) < 1e-12)
OLOC = OP['ReO'].real; WLOC = np.diag(OP['w2']).real

# ---------------- chain engine (inline copy of chain.py) ----------------
class Chain:
    def __init__(self, L, q): self.L, self.q = L, np.array(q) % 4
    def sector_states(self, d):
        L = self.L; out = []; pats = {N: np.array([v for v in range(1 << L) if bin(v).count('1') == N], np.int64) for N in range(L + 1)}
        def spread(p, j):
            s = np.zeros_like(p)
            for x in range(L): s |= ((p >> x) & 1) << (4 * x + j)
            return s
        for m in range(-max(d), L - min(d) + 1):
            Ns = [m + dj for dj in d]
            if min(Ns) < 0 or max(Ns) > L: continue
            acc = np.zeros(1, np.int64)
            for j in range(4): acc = (acc[:, None] | spread(pats[Ns[j]], j)[None, :]).ravel()
            out.append(acc)
        return np.sort(np.concatenate(out))
    def translate(self, s):
        L = self.L; top = (s >> (4 * (L - 1))) & 15; s2 = ((s << 4) & ((1 << (4 * L)) - 1)) | top
        nt = np.bitwise_count(top).astype(np.int64); N = np.bitwise_count(s).astype(np.int64)
        pw = 2 * ((nt * (N - nt)) & 1)
        for j in range(4): pw = pw - ((top >> j) & 1) * self.q[j]
        return s2, pw % 4
    def setup(self, d):
        S = self.sector_states(d); L = self.L; cur = S.copy(); acc = np.zeros(len(S), np.int64); best = S.copy()
        ustar = np.zeros(len(S), np.int64); pstar = np.zeros(len(S), np.int64); per = np.zeros(len(S), np.int64); mu = np.zeros(len(S), np.int64)
        for u in range(1, L + 1):
            cur, pw = self.translate(cur); acc = (acc + pw) % 4
            if u < L:
                lt = cur < best; best[lt] = cur[lt]; ustar[lt] = u; pstar[lt] = acc[lt]
            bk = (cur == S) & (per == 0); per[bk] = u; mu[bk] = acc[bk]
        assert np.all(cur == S) and len(np.unique(acc)) == 1
        self.S = S; self.rep_of = np.searchsorted(S, best); self.l_of = L - ustar; self.phipw = (acc - pstar) % 4
        self.R = np.where(best == S)[0]; self.perR = per[self.R]; self.mu = mu[self.R]; self.lam = int(acc[0])
        self.perf = np.zeros(len(S), np.int64); self.perf[self.R] = self.perR
    def kappas(self): return [(np.pi / 2 * self.lam + 2 * np.pi * p) / self.L for p in range(self.L)]
    def terms(self, src):
        L = self.L
        for x in range(L):
            for j in range(4):
                a, b = 4 * x + j, 4 * ((x + 1) % L) + j; tw = 1j * (IP[self.q[j]] if x == L - 1 else 1)
                for cr, an, amp in ((a, b, tw), (b, a, np.conj(tw))):
                    pos = np.where((((src >> an) & 1) == 1) & (((src >> cr) & 1) == 0))[0]; s = src[pos]
                    lo, hi = min(cr, an), max(cr, an)
                    btw = np.bitwise_count(s & (((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1))) & 1
                    yield 'hop', pos, s ^ (1 << cr) ^ (1 << an), amp * (1 - 2 * btw.astype(float))
        for x in range(L):
            blk = (src >> (4 * x)) & 15
            for b0, b1 in ((0, 15), (15, 0)):
                pos = np.where(blk == b0)[0]; s = src[pos]
                yield 'O', pos, (s & ~(15 << (4 * x))) | (b1 << (4 * x)), np.full(len(pos), OLOC[b1, b0], complex)
    def block(self, kap, g, w):
        ok = np.abs(np.exp(-1j * kap * self.perR) * IP[self.mu] - 1) < 1e-9
        Rk = self.R[ok]; n = len(Rk); idx = -np.ones(len(self.S), np.int64); idx[Rk] = np.arange(n); src = self.S[Rk]
        H = np.zeros((n, n), complex)
        for x in range(self.L): H[np.arange(n), np.arange(n)] += g * w * WLOC[(src >> (4 * x)) & 15]
        for kd, pos, tgt, amp in self.terms(src):
            tp = np.searchsorted(self.S, tgt); r = self.rep_of[tp]; ti = idx[r]; good = ti >= 0
            val = amp * (1 if kd == 'hop' else g) * np.exp(1j * kap * self.l_of[tp]) * np.conj(IP[self.phipw[tp]]) * np.sqrt(self.perR[ok][pos] / self.perf[r])
            np.add.at(H, (ti[good], pos[good]), val[good])
        return H

def full_fock(L, q, g, w):
    ch = Chain(L, q); S = np.arange(1 << (4 * L), dtype=np.int64); H = np.zeros((len(S), len(S)), complex)
    for kd, pos, tgt, amp in ch.terms(S): np.add.at(H, (tgt, pos), amp * (1 if kd == 'hop' else g))
    for x in range(L): H[S, S] += g * w * WLOC[(S >> (4 * x)) & 15]
    return np.linalg.eigvalsh(H)

print('== B. engine gate: momentum sectors vs full Fock, L = 2 ==')
okB = True; worst = 0
for q in ((1, 1, -1, -1), (2, 2, 2, 2)):
    for w in (0., 1.):
        full = full_fock(2, q, 0.37, w); ev = []
        for a, b, c in itertools.product(range(-2, 3), repeat=3):
            ch = Chain(2, q)
            try: ch.setup([a, b, c, 0])
            except ValueError: continue
            for k in ch.kappas():
                H = ch.block(k, 0.37, w)
                if len(H): okB &= np.abs(H - H.conj().T).max() < 1e-12; ev += list(np.linalg.eigvalsh(H))
        ev = np.sort(ev); okB &= len(ev) == len(full); worst = max(worst, np.abs(ev - full).max())
check('B1 all (d, kappa) blocks Hermitian and reproduce the full 2^8 spectrum (twist and APBC, ReO and Cay)', okB and worst < 1e-12, f'max dev {worst:.1e}')

SECS = [(0, 0, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0), (1, 1, 0, 0), (0, 0, 1, 1), (1, 0, 1, 0), (1, -1, 0, 0), (1, 0, -1, 0), (0, 0, 1, -1), (-1, 0, 0, 0), (0, 0, -1, 0)]
def chain_gaps(L, q, g, w):
    lev = []
    for d in SECS:
        ch = Chain(L, q); ch.setup(list(d))
        for p, k in enumerate(ch.kappas()):
            H = ch.block(k, g, w)
            if len(H): lev += [(e, d) for e in np.linalg.eigvalsh(H)[:2]]
    lev.sort(); E0 = lev[0][0]
    d1 = min(e for e, d in lev if d in ((1, 0, 0, 0), (0, 0, 1, 0), (-1, 0, 0, 0), (0, 0, -1, 0))) - E0
    return E0, lev[1][0] - E0, d1, lev[0][1]

# ---------------- embedded Mac-mini results (analyze.py summary; bc tw = twist (1,1,-1,-1), ap = antiperiodic) ----------------
EMBED = r'''[{"bc":"ap","model":"Cay","g":0.125,"L":4,"E0":-11.741931,"gs":[[0,0,0,0],0],"gap":1.49486,"gap_blk":[[1,0,0,0],1],"d1":1.49486,"dadj":3.02841,"dpair":1.96187,"dneu":1.96187,"nsec":4,"nblk":16},{"bc":"ap","model":"Cay","g":0.125,"L":6,"E0":-16.713247,"gs":[[0,0,0,0],0],"gap":1.1034,"gap_blk":[[1,0,0,0],0],"d1":1.1034,"dadj":2.19621,"dpair":1.30867,"dneu":1.30867,"nsec":4,"nblk":24},{"bc":"ap","model":"Cay","g":0.25,"L":4,"E0":-15.463603,"gs":[[0,0,0,0],0],"gap":2.70346,"gap_blk":[[1,1,0,0],2],"d1":2.85312,"dadj":5.00114,"dpair":2.70346,"dneu":2.70346,"nsec":4,"nblk":16},{"bc":"ap","model":"Cay","g":0.25,"L":6,"E0":-23.129194,"gs":[[0,0,0,0],0],"gap":2.69919,"gap_blk":[[0,0,0,0],3],"d1":2.78558,"dadj":5.02662,"dpair":2.69919,"dneu":2.69919,"nsec":4,"nblk":24},{"bc":"ap","model":"Cay","g":0.5,"L":4,"E0":-28.604912,"gs":[[0,0,0,0],0],"gap":6.23267,"gap_blk":[[1,0,0,0],2],"d1":6.23267,"dadj":12.19462,"dpair":7.10464,"dneu":7.10464,"nsec":4,"nblk":16},{"bc":"ap","model":"Cay","g":0.5,"L":6,"E0":-42.905584,"gs":[[0,0,0,0],0],"gap":6.03129,"gap_blk":[[1,0,0,0],4],"d1":6.03129,"dadj":12.04696,"dpair":7.10498,"dneu":7.10498,"nsec":4,"nblk":24},{"bc":"ap","model":"Cay","g":1.0,"L":4,"E0":-56.289752,"gs":[[0,0,0,0],0],"gap":13.24282,"gap_blk":[[1,0,0,0],2],"d1":13.24282,"dadj":26.49528,"dpair":15.49962,"dneu":15.49962,"nsec":4,"nblk":16},{"bc":"ap","model":"Cay","g":1.0,"L":6,"E0":-84.434476,"gs":[[0,0,0,0],0],"gap":12.98069,"gap_blk":[[1,0,0,0],4],"d1":12.98069,"dadj":26.08138,"dpair":15.49864,"dneu":15.49864,"nsec":4,"nblk":24},{"bc":"ap","model":"ReO","g":0.0,"L":4,"E0":-11.313708,"gs":[[0,0,0,0],0],"gap":1.41421,"gap_blk":[[1,0,0,0],1],"d1":1.41421,"dadj":2.82843,"dpair":2.82843,"dneu":2.82843,"nsec":4,"nblk":16},{"bc":"ap","model":"ReO","g":0.0,"L":6,"E0":-16.0,"gs":[[0,0,0,0],0],"gap":1.0,"gap_blk":[[1,0,0,0],0],"d1":1.0,"dadj":2.0,"dpair":2.0,"dneu":2.0,"nsec":4,"nblk":24},{"bc":"ap","model":"ReO","g":0.125,"L":4,"E0":-11.456271,"gs":[[0,0,0,0],0],"gap":1.4288,"gap_blk":[[1,0,0,0],0],"d1":1.4288,"dadj":2.85097,"dpair":2.30091,"dneu":2.70527,"nsec":4,"nblk":16},{"bc":"ap","model":"ReO","g":0.125,"L":6,"E0":-16.219377,"gs":[[0,0,0,0],0],"gap":1.01127,"gap_blk":[[1,0,0,0],2],"d1":1.01127,"dadj":2.01667,"dpair":1.60336,"dneu":1.89021,"nsec":4,"nblk":24},{"bc":"ap","model":"ReO","g":0.25,"L":4,"E0":-12.053181,"gs":[[0,0,0,0],0],"gap":1.55497,"gap_blk":[[1,0,0,0],0],"d1":1.55497,"dadj":2.96429,"dpair":1.77856,"dneu":2.37453,"nsec":4,"nblk":16},{"bc":"ap","model":"ReO","g":0.25,"L":6,"E0":-17.250872,"gs":[[0,0,0,0],0],"gap":1.18962,"gap_blk":[[1,1,0,0],3],"d1":1.20296,"dadj":2.22229,"dpair":1.18962,"dneu":1.63463,"nsec":4,"nblk":24},{"bc":"ap","model":"ReO","g":0.5,"L":4,"E0":-17.219278,"gs":[[0,0,0,0],0],"gap":2.91839,"gap_blk":[[1,1,0,0],2],"d1":3.27291,"dadj":5.56392,"dpair":2.91839,"dneu":4.19023,"nsec":4,"nblk":16},{"bc":"ap","model":"ReO","g":0.5,"L":6,"E0":-25.796274,"gs":[[0,0,0,0],0],"gap":2.92786,"gap_blk":[[1,1,0,0],3],"d1":3.23953,"dadj":5.62975,"dpair":2.92786,"dneu":4.51846,"nsec":4,"nblk":24},{"bc":"ap","model":"ReO","g":1.0,"L":4,"E0":-32.523846,"gs":[[0,0,0,0],0],"gap":7.21665,"gap_blk":[[1,0,0,0],3],"d1":7.21665,"dadj":13.60008,"dpair":7.32022,"dneu":12.17278,"nsec":4,"nblk":16},{"bc":"ap","model":"ReO","g":1.0,"L":6,"E0":-48.784681,"gs":[[0,0,0,0],0],"gap":7.00139,"gap_blk":[[1,0,0,0],4],"d1":7.00139,"dadj":13.64173,"dpair":7.32063,"dneu":12.37787,"nsec":4,"nblk":24},{"bc":"tw","model":"Cay","g":0.125,"L":4,"E0":-11.053259,"gs":[[0,0,0,0],0],"gap":0.99265,"gap_blk":[[0,0,-1,0],1],"d1":0.99265,"dadj":1.96591,"dpair":1.23826,"dneu":1.23826,"nsec":11,"nblk":44},{"bc":"tw","model":"Cay","g":0.125,"L":5,"E0":-13.413056,"gs":[[0,0,0,0],0],"gap":0.07091,"gap_blk":[[1,1,0,0],2],"d1":0.56305,"dadj":1.243,"dpair":0.07091,"dneu":0.90815,"nsec":11,"nblk":55},{"bc":"tw","model":"Cay","g":0.125,"L":6,"E0":-16.367618,"gs":[[0,0,0,0],0],"gap":0.79084,"gap_blk":[[0,0,-1,0],2],"d1":0.79084,"dadj":1.48888,"dpair":0.89211,"dneu":0.89211,"nsec":11,"nblk":66},{"bc":"tw","model":"Cay","g":0.125,"L":7,"E0":-18.922501,"gs":[[0,0,0,0],0],"gap":0.27448,"gap_blk":[[1,1,0,0],3],"d1":0.60208,"dadj":1.13683,"dpair":0.27448,"dneu":0.87687,"nsec":9,"nblk":63},{"bc":"tw","model":"Cay","g":0.125,"L":8,"E0":-21.742909,"gs":[[0,0,0,0],0],"gap":0.71438,"gap_blk":[[1,0,0,0],3],"d1":0.71438,"dadj":null,"dpair":0.7455,"dneu":0.7455,"nsec":4,"nblk":26},{"bc":"tw","model":"Cay","g":0.25,"L":4,"E0":-15.423408,"gs":[[0,0,0,0],0],"gap":2.71938,"gap_blk":[[1,0,1,0],2],"d1":2.8328,"dadj":4.90757,"dpair":2.71938,"dneu":2.71938,"nsec":11,"nblk":44},{"bc":"tw","model":"Cay","g":0.25,"L":5,"E0":-19.27181,"gs":[[0,0,0,0],0],"gap":2.67943,"gap_blk":[[1,1,0,0],2],"d1":2.7874,"dadj":4.80621,"dpair":2.67943,"dneu":2.91197,"nsec":11,"nblk":55},{"bc":"tw","model":"Cay","g":0.25,"L":6,"E0":-23.127646,"gs":[[0,0,0,0],0],"gap":2.70238,"gap_blk":[[1,0,1,0],3],"d1":2.78984,"dadj":4.93972,"dpair":2.70238,"dneu":2.70238,"nsec":11,"nblk":66},{"bc":"tw","model":"Cay","g":0.25,"L":7,"E0":-26.981941,"gs":[[0,0,0,0],0],"gap":2.70055,"gap_blk":[[1,1,0,0],3],"d1":2.78252,"dadj":4.88413,"dpair":2.70055,"dneu":2.81355,"nsec":9,"nblk":63},{"bc":"tw","model":"Cay","g":0.25,"L":8,"E0":-30.836571,"gs":[[0,0,0,0],0],"gap":2.70163,"gap_blk":[[0,0,0,0],4],"d1":2.78039,"dadj":null,"dpair":2.70163,"dneu":2.70163,"nsec":4,"nblk":26},{"bc":"tw","model":"Cay","g":0.5,"L":4,"E0":-28.603749,"gs":[[0,0,0,0],0],"gap":6.08211,"gap_blk":[[0,0,1,0],3],"d1":6.08211,"dadj":12.08371,"dpair":7.10513,"dneu":7.10513,"nsec":11,"nblk":44},{"bc":"tw","model":"Cay","g":0.5,"L":5,"E0":-35.754647,"gs":[[0,0,0,0],0],"gap":6.03126,"gap_blk":[[0,0,-1,0],3],"d1":6.03126,"dadj":12.0428,"dpair":7.10485,"dneu":7.2153,"nsec":11,"nblk":55},{"bc":"tw","model":"Cay","g":0.5,"L":6,"E0":-42.905578,"gs":[[0,0,0,0],0],"gap":6.05398,"gap_blk":[[0,0,1,0],4],"d1":6.05398,"dadj":12.07808,"dpair":7.10498,"dneu":7.10498,"nsec":11,"nblk":66},{"bc":"tw","model":"Cay","g":0.5,"L":7,"E0":-50.056508,"gs":[[0,0,0,0],0],"gap":6.03128,"gap_blk":[[0,0,1,0],5],"d1":6.03128,"dadj":12.12069,"dpair":7.10498,"dneu":7.16215,"nsec":9,"nblk":63},{"bc":"tw","model":"Cay","g":0.5,"L":8,"E0":-57.207437,"gs":[[0,0,0,0],0],"gap":7.10498,"gap_blk":[[0,0,0,0],4],"d1":7.25517,"dadj":null,"dpair":null,"dneu":7.10498,"nsec":2,"nblk":7},{"bc":"tw","model":"Cay","g":1.0,"L":4,"E0":-56.289651,"gs":[[0,0,0,0],0],"gap":13.04823,"gap_blk":[[-1,0,0,0],3],"d1":13.04823,"dadj":26.2673,"dpair":15.49865,"dneu":15.49865,"nsec":11,"nblk":44},{"bc":"tw","model":"Cay","g":1.0,"L":5,"E0":-70.362063,"gs":[[0,0,0,0],0],"gap":12.98069,"gap_blk":[[1,0,0,0],3],"d1":12.98069,"dadj":26.12062,"dpair":15.49859,"dneu":15.55938,"nsec":11,"nblk":55},{"bc":"tw","model":"Cay","g":1.0,"L":6,"E0":-84.434476,"gs":[[0,0,0,0],0],"gap":13.01088,"gap_blk":[[0,0,1,0],4],"d1":13.01088,"dadj":26.13001,"dpair":15.49864,"dneu":15.49864,"nsec":11,"nblk":66},{"bc":"tw","model":"Cay","g":1.0,"L":7,"E0":-98.506888,"gs":[[0,0,0,0],0],"gap":12.98069,"gap_blk":[[0,0,1,0],5],"d1":12.98069,"dadj":26.13269,"dpair":15.49864,"dneu":15.53012,"nsec":9,"nblk":63},{"bc":"tw","model":"Cay","g":1.0,"L":8,"E0":-112.579301,"gs":[[0,0,0,0],0],"gap":14.44432,"gap_blk":[[1,0,0,0],0],"d1":14.44432,"dadj":null,"dpair":null,"dneu":15.49864,"nsec":2,"nblk":7},{"bc":"tw","model":"ReO","g":0.0,"L":4,"E0":-10.452504,"gs":[[0,0,0,0],0],"gap":0.76537,"gap_blk":[[1,0,0,0],1],"d1":0.76537,"dadj":1.53073,"dpair":1.53073,"dneu":1.53073,"nsec":11,"nblk":44},{"bc":"tw","model":"ReO","g":0.0,"L":5,"E0":-12.944272,"gs":[[1,1,0,0],2],"gap":0.61803,"gap_blk":[[1,0,0,0],4],"d1":0.61803,"dadj":1.23607,"dpair":0.0,"dneu":1.23607,"nsec":11,"nblk":55},{"bc":"tw","model":"ReO","g":0.0,"L":6,"E0":-15.454813,"gs":[[0,0,0,0],0],"gap":0.51764,"gap_blk":[[0,0,1,0],0],"d1":0.51764,"dadj":1.03528,"dpair":1.03528,"dneu":1.03528,"nsec":11,"nblk":66},{"bc":"tw","model":"ReO","g":0.0,"L":7,"E0":-17.975837,"gs":[[1,1,0,0],3],"gap":0.44504,"gap_blk":[[1,0,0,0],3],"d1":0.44504,"dadj":0.89008,"dpair":0.0,"dneu":0.89008,"nsec":9,"nblk":63},{"bc":"tw","model":"ReO","g":0.125,"L":4,"E0":-10.623686,"gs":[[0,0,0,0],0],"gap":0.80314,"gap_blk":[[1,0,0,0],1],"d1":0.80314,"dadj":1.59723,"dpair":1.27569,"dneu":1.55518,"nsec":11,"nblk":44},{"bc":"tw","model":"ReO","g":0.125,"L":5,"E0":-13.102591,"gs":[[1,1,0,0],2],"gap":0.6008,"gap_blk":[[1,0,0,0],4],"d1":0.6008,"dadj":1.20935,"dpair":0.0,"dneu":0.70504,"nsec":11,"nblk":55},{"bc":"tw","model":"ReO","g":0.125,"L":6,"E0":-15.699951,"gs":[[0,0,0,0],0],"gap":0.55035,"gap_blk":[[0,0,1,0],0],"d1":0.55035,"dadj":1.09135,"dpair":0.85552,"dneu":1.04815,"nsec":11,"nblk":66},{"bc":"tw","model":"ReO","g":0.125,"L":7,"E0":-18.212952,"gs":[[1,1,0,0],3],"gap":0.42981,"gap_blk":[[1,0,0,0],3],"d1":0.42981,"dadj":0.86773,"dpair":0.0,"dneu":0.47065,"nsec":9,"nblk":63},{"bc":"tw","model":"ReO","g":0.125,"L":8,"E0":-20.822968,"gs":[[0,0,0,0],0],"gap":0.42015,"gap_blk":[[1,0,0,0],3],"d1":0.42015,"dadj":null,"dpair":0.64011,"dneu":0.789,"nsec":4,"nblk":26},{"bc":"tw","model":"ReO","g":0.25,"L":4,"E0":-11.456074,"gs":[[0,0,0,0],0],"gap":1.12986,"gap_blk":[[0,0,-1,0],1],"d1":1.12986,"dadj":2.0368,"dpair":1.19204,"dneu":1.65366,"nsec":11,"nblk":44},{"bc":"tw","model":"ReO","g":0.25,"L":5,"E0":-14.047339,"gs":[[0,0,0,0],0],"gap":0.31364,"gap_blk":[[1,1,0,0],2],"d1":0.8294,"dadj":1.51195,"dpair":0.31364,"dneu":1.14732,"nsec":11,"nblk":55},{"bc":"tw","model":"ReO","g":0.25,"L":6,"E0":-17.008314,"gs":[[0,0,0,0],0],"gap":0.91671,"gap_blk":[[1,0,1,0],3],"d1":0.97599,"dadj":1.65609,"dpair":0.91671,"dneu":1.30838,"nsec":11,"nblk":66},{"bc":"tw","model":"ReO","g":0.25,"L":7,"E0":-19.754467,"gs":[[0,0,0,0],0],"gap":0.52781,"gap_blk":[[1,1,0,0],3],"d1":0.86865,"dadj":1.42231,"dpair":0.52781,"dneu":1.14114,"nsec":9,"nblk":63},{"bc":"tw","model":"ReO","g":0.25,"L":8,"E0":-22.627034,"gs":[[0,0,0,0],0],"gap":0.82351,"gap_blk":[[1,0,1,0],4],"d1":0.93651,"dadj":null,"dpair":0.82351,"dneu":1.20514,"nsec":4,"nblk":26},{"bc":"tw","model":"ReO","g":0.5,"L":4,"E0":-17.199204,"gs":[[0,0,0,0],0],"gap":2.93593,"gap_blk":[[1,0,1,0],2],"d1":3.23759,"dadj":5.53862,"dpair":2.93593,"dneu":4.54868,"nsec":11,"nblk":44},{"bc":"tw","model":"ReO","g":0.5,"L":5,"E0":-21.496096,"gs":[[0,0,0,0],0],"gap":2.92243,"gap_blk":[[1,1,0,0],2],"d1":3.23656,"dadj":5.44549,"dpair":2.92243,"dneu":4.55094,"nsec":11,"nblk":55},{"bc":"tw","model":"ReO","g":0.5,"L":6,"E0":-25.79576,"gs":[[0,0,0,0],0],"gap":2.92911,"gap_blk":[[1,0,1,0],3],"d1":3.2373,"dadj":5.57152,"dpair":2.92911,"dneu":4.53896,"nsec":11,"nblk":66},{"bc":"tw","model":"ReO","g":0.5,"L":7,"E0":-30.094979,"gs":[[0,0,0,0],0],"gap":2.92879,"gap_blk":[[1,1,0,0],3],"d1":3.23545,"dadj":5.50852,"dpair":2.92879,"dneu":4.54809,"nsec":9,"nblk":63},{"bc":"tw","model":"ReO","g":0.5,"L":8,"E0":-34.394274,"gs":[[0,0,0,0],0],"gap":3.74799,"gap_blk":[[1,0,0,0],0],"d1":3.74799,"dadj":null,"dpair":null,"dneu":4.5381,"nsec":2,"nblk":7},{"bc":"tw","model":"ReO","g":1.0,"L":4,"E0":-32.523131,"gs":[[0,0,0,0],0],"gap":7.05617,"gap_blk":[[-1,0,0,0],3],"d1":7.05617,"dadj":13.5546,"dpair":7.32068,"dneu":12.35703,"nsec":11,"nblk":44},{"bc":"tw","model":"ReO","g":1.0,"L":5,"E0":-40.653898,"gs":[[0,0,0,0],0],"gap":7.00138,"gap_blk":[[1,0,0,0],3],"d1":7.00138,"dadj":13.60195,"dpair":7.32058,"dneu":12.37533,"nsec":11,"nblk":55},{"bc":"tw","model":"ReO","g":1.0,"L":6,"E0":-48.784679,"gs":[[0,0,0,0],0],"gap":7.02585,"gap_blk":[[0,0,-1,0],4],"d1":7.02585,"dadj":13.65699,"dpair":7.32063,"dneu":12.36644,"nsec":11,"nblk":66},{"bc":"tw","model":"ReO","g":1.0,"L":7,"E0":-56.915459,"gs":[[0,0,0,0],0],"gap":7.00139,"gap_blk":[[0,0,1,0],5],"d1":7.00139,"dadj":13.69698,"dpair":7.32063,"dneu":12.37128,"nsec":9,"nblk":63},{"bc":"tw","model":"ReO","g":1.0,"L":8,"E0":-65.046238,"gs":[[0,0,0,0],0],"gap":8.27422,"gap_blk":[[1,0,0,0],0],"d1":8.27422,"dadj":null,"dpair":null,"dneu":12.36647,"nsec":2,"nblk":7}]'''
RES = json.loads(EMBED)
T = {(r['bc'], r['model'], r['g'], r['L']): r for r in RES}

print('== C. live L = 4 (twisted) vs embedded ==')
dev = 0; free_ok = True
E0, gap, d1, gsd = chain_gaps(4, (1, 1, -1, -1), 0.0, 0.0)
free_ok = abs(d1 - 2 * math.sin(math.pi / 8)) < 1e-10 and abs(gap - d1) < 1e-10
for model, w in (('ReO', 0.), ('Cay', 1.)):
    for g in (0.125, 0.25, 0.5, 1.0):
        E0, gap, d1, gsd = chain_gaps(4, (1, 1, -1, -1), g, w); r = T[('tw', model, g, 4)]
        dev = max(dev, abs(E0 - r['E0']), abs(gap - r['gap']), abs(d1 - r['d1']))
check('C1 g = 0: free single-particle gap 2 sin(pi/2L) at L = 4', free_ok)
check('C2 live L = 4 E0, gap, Delta_1 (both models, 4 couplings) match the embedded mini values', dev < 1e-4, f'max dev {dev:.1e}')

print('== D. embedded mini results: gap Delta over all computed blocks (twisted chain) ==')
FULL8 = 26  # L = 8 blocks: S0 p0-4, 1000 all p, 1100 all p, 1010 p0-4 (others equal by symmetry verified at L = 6, 7)
print('  model g     ' + ' '.join(f'L={L:<5d}' for L in range(4, 9)) + ' rho   even-rho class (L used)')
CLS = {}
for model in ('ReO', 'Cay'):
    for g in (0.125, 0.25, 0.5, 1.0):
        Ls = [L for L in range(4, 9) if L < 8 or T[('tw', model, g, 8)]['nblk'] >= FULL8]
        Dl = [T[('tw', model, g, L)]['gap'] for L in Ls]
        rho = Dl[-1] / Dl[0]; DL = [d * L for d, L in zip(Dl, Ls)]
        ev = [T[('tw', model, g, L)]['gap'] for L in (4, 6, 8) if L in Ls]; erho = ev[-1] / ev[0]
        uniq = min(Dl) > 0.1 and all(T[('tw', model, g, L)]['gs'][0] == [0, 0, 0, 0] for L in Ls)
        incr = all(y > x for x, y in zip(DL, DL[1:])); flat = (max(DL) - min(DL)) / np.mean(DL) < 0.2
        c = 'OPEN' if (uniq and rho >= 0.75 and incr) else ('CLOSING' if (rho <= 0.6 or flat or not uniq) else 'INCONCLUSIVE')
        CLS[(model, g)] = c
        row = ' '.join(f'{T[("tw", model, g, L)]["gap"]:<7.3f}' if L in Ls else f'({T[("tw", model, g, L)]["gap"]:.2f})' for L in range(4, 9))
        print(f'  {model:4s} {g:<5} {row} {rho:<5.3f} {erho:<8.3f} {c} (4-{Ls[-1]})')
print('  free chain (g = 0): ' + ' '.join(f'{T[("tw", "ReO", 0.0, L)]["gap"]:.3f}' for L in range(4, 8)) + ' = 2 sin(pi/2L); (x) = L = 8 partial (S0 all p, 1000 p = 0, 1 only), not classified')
ap = [(m, g, T[('ap', m, g, 4)]['gap'], T[('ap', m, g, 6)]['gap']) for m in ('ReO', 'Cay') for g in (0.125, 0.25, 0.5)]
print('  APBC (exact Spin(7) BC) Delta(4)->Delta(6): ' + '; '.join(f'{m} {g}: {a:.2f}->{b:.2f}' for m, g, a, b in ap) + ' (free 1.41->1.00)')
part = max(abs(T[('tw', m, g, 8)]['dneu'] / T[('tw', m, g, 7)]['dneu'] - 1) for m in ('ReO', 'Cay') for g in (0.5, 1.0))
check('D1 g = 0.5, 1.0: both models OPEN on L = 4..7; L = 8 neutral gap within 1% of L = 7 (both persist)',
      all(CLS[(m, g)] == 'OPEN' for m in ('ReO', 'Cay') for g in (0.5, 1.0)) and part < 0.01, f'max L8/L7 neutral dev {part:.3f}')
check('D2 g = 0.25 (L = 4..8 complete): Cayley OPEN, Re Omega alone not OPEN', CLS[('Cay', 0.25)] == 'OPEN' and CLS[('ReO', 0.25)] != 'OPEN',
      f"Cay {CLS[('Cay', 0.25)]}, ReO {CLS[('ReO', 0.25)]}")
check('D3 no coupling where Re Omega is OPEN and Cayley is not', not any(CLS[('ReO', g)] == 'OPEN' and CLS[('Cay', g)] != 'OPEN' for g in (0.125, 0.25, 0.5, 1.0)))
r0 = T[('tw', 'ReO', 0.125, 8)]['gap'] / T[('tw', 'ReO', 0.125, 4)]['gap']; f0 = math.sin(math.pi / 16) / math.sin(math.pi / 8)
check('D4 g = 0.125: Re Omega free-like (Delta(8)/Delta(4) within 5% of the free 1/L ratio), Cayley not OPEN',
      abs(r0 / f0 - 1) < 0.05 and CLS[('Cay', 0.125)] != 'OPEN', f'ReO {r0:.3f} vs free {f0:.3f}')
check('D5 matched on-site gap (ReO at 0.5: 4.0; Cay at 0.25: 3.5): both OPEN, so the gain is per unit coupling',
      CLS[('ReO', 0.5)] == 'OPEN' and CLS[('Cay', 0.25)] == 'OPEN')
outcome = 'PASS (Cayley advantage at g = 0.25; both persist for g >= 0.5)' if (CLS[('Cay', 0.25)] == 'OPEN' and CLS[('ReO', 0.25)] != 'OPEN' and not any(CLS[('ReO', g)] == 'OPEN' and CLS[('Cay', g)] != 'OPEN' for g in (0.125, 0.25, 0.5, 1.0))) else 'NOT PASS'
print('Task outcome (pre-set criteria): ' + outcome)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
