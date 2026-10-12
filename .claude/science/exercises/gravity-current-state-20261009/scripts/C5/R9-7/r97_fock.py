"""R9-7 script A: the complete crossing set of toy N on an explicit Fock Hamiltonian (d = 1, small L), brute-force
RS4 mixed O(go^2 gi^2) coefficient of E(X_p) - E(vac), compared with the 24-ordering closed form (r97_common.ORD).
Independent engine (written here; bitset CAR for fermions, occupation tuples for bosons).
Outer monomials (+ h.c.), amplitude / N:
  dec : a+_Y a+_A a+_B a_X        Psi_o(Y,A,B) sqrt(h(E_X,W_YAB)) / sqrt(16 E_X E_Y E_A E_B)   (h = 1 bosons)
  vac : a+_X a+_Y a+_A a+_B       Psi_o(Y,A,B) / sqrt(16 ...)
  22  : a+_A a+_B a_X a_Y         s22 * F(s_AB) / sqrt(16 ...)
  31  : a+_X a+_A a+_B a_Y        s31 * F(s_XA) F(s_XB) F(s_AB) / sqrt(16 ...)
Inner: a+_U a+_C a+_D a_Y  Psi_in sqrt(h(E_Y, W_UCD)) / sqrt(...);   a+_Y a+_U a+_C a+_D  Psi_in / sqrt(...).
Psi = product of F over the three pairs of the created triple (toy N)."""
import numpy as np, itertools, sys, time
from collections import defaultdict
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r97_common import Fpl, s2, hfac, ORD, plateau
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)
L1, L2 = 1.0, 1.4
PRESC = ['P1']
def F(s): return float(Fpl(s, L1, L2))
def wrap(k): return (k + np.pi) % (2*np.pi) - np.pi

class Lat:
    def __init__(self, L, twist, mass):
        self.L = L; self.N = L; self.k = {}; self.E = {}; self.sp = {}; self.modes = {}; self.q = {}
        mi = 0
        for s in ['X', 'Y', 'A', 'B', 'U', 'C', 'D']:
            self.modes[s] = []
            for n in range(L):
                qq = 2*n + twist[s]; k = wrap(np.pi*qq/L)
                self.k[mi] = k; self.E[mi] = np.sqrt(mass[s]**2 + k*k); self.sp[mi] = s; self.q[mi] = qq % (2*L)
                self.modes[s].append(mi); mi += 1
        self.find = {(self.sp[m], self.q[m]): m for m in self.k}
        self.nm = mi
    def f(self, s, qq): return self.find.get((s, qq % (2*self.L)))

def legs(lat, *ms):
    return float(np.prod([plateau(lat.k[m], 2.0, 2.5) for m in ms]))

def Psi3(lat, a, b, c):
    k, E = lat.k, lat.E
    return F(s2(E[a], k[a], E[b], k[b]))*F(s2(E[a], k[a], E[c], k[c]))*F(s2(E[b], k[b], E[c], k[c]))

def build(lat, go, gi, stat, new, s22=1.0, s31=1.0):
    """list of (cre tuple, ann tuple, amp) incl. h.c."""
    T = []; N = lat.N; E = lat.E; k = lat.k
    hh = (lambda e, w: hfac(e, w)) if stat == 'F' else (lambda e, w: 1.0)
    def add(cre, ann, amp):
        if amp == 0: return
        T.append((tuple(cre), tuple(ann), amp)); T.append((tuple(reversed(ann)), tuple(reversed(cre)), amp))
    def nrm(ms): return legs(lat, *ms)/np.sqrt(np.prod([2*E[m] for m in ms]))/N
    for (P, Q, R, S, g) in [('X', 'Y', 'A', 'B', go), ('Y', 'U', 'C', 'D', gi)]:
        if not g: continue
        for mp in lat.modes[P]:
            for mq in lat.modes[Q]:
                for mr in lat.modes[R]:
                    ms_ = lat.f(S, lat.q[mp] - lat.q[mq] - lat.q[mr])     # decay P -> Q R S
                    W = E[mq] + E[mr] + E[ms_]
                    P2o = (P == 'X' and PRESC[0] == 'P2')
                    kd = F(s2(E[mr], k[mr], E[ms_], k[ms_])) if P2o else Psi3(lat, mq, mr, ms_)
                    add((mq, mr, ms_), (mp,), g*kd*np.sqrt(hh(E[mp], W))*nrm((mp, mq, mr, ms_)))
                    ms2 = lat.f(S, -lat.q[mp] - lat.q[mq] - lat.q[mr])     # vacuum 0 -> P Q R S
                    kv = F(s2(E[mr], k[mr], E[ms2], k[ms2])) if P2o else Psi3(lat, mq, mr, ms2)
                    add((mp, mq, mr, ms2), (), g*kv*nrm((mp, mq, mr, ms2)))
                    if P == 'X' and '22' in new:      # X(mp) Y(mq) -> A(mr) B(ms3)
                        ms3 = lat.f(S, lat.q[mp] + lat.q[mq] - lat.q[mr])
                        add((mr, ms3), (mp, mq), g*s22*F(s2(E[mr], k[mr], E[ms3], k[ms3]))*nrm((mp, mq, mr, ms3)))
                    if P == 'X' and '31' in new:      # Y(mq) -> X(mp) A(mr) B(ms4)
                        ms4 = lat.f(S, lat.q[mq] - lat.q[mp] - lat.q[mr])
                        ff = F(s2(E[mp], k[mp], E[mr], k[mr]))*F(s2(E[mp], k[mp], E[ms4], k[ms4]))*F(s2(E[mr], k[mr], E[ms4], k[ms4]))
                        if PRESC[0] == 'P2': ff = F(s2(E[mr], k[mr], E[ms4], k[ms4]))
                        add((mp, mr, ms4), (mq,), g*s31*ff*nrm((mp, mq, mr, ms4)))
    return T

# ---- Fock engine
def app_F(st, cre, ann):
    sign = 1.0
    for isann, m in reversed([(False, c) for c in cre] + [(True, a) for a in ann]):
        below = bin(st & ((1 << m) - 1)).count('1')
        occ = (st >> m) & 1
        if isann:
            if not occ: return None, 0.0
            st &= ~(1 << m)
        else:
            if occ: return None, 0.0
            st |= (1 << m)
        if below & 1: sign = -sign
    return st, sign
def app_B(st, cre, ann):
    st = dict(st); amp = 1.0
    for isann, m in reversed([(False, c) for c in cre] + [(True, a) for a in ann]):
        n = st.get(m, 0)
        if isann:
            if n == 0: return None, 0.0
            amp *= np.sqrt(n); st[m] = n - 1
            if st[m] == 0: del st[m]
        else:
            amp *= np.sqrt(n + 1); st[m] = n + 1
    return tuple(sorted(st.items())), amp
def modes_of(st, stat):
    if stat == 'F':
        return [i for i in range(st.bit_length()) if (st >> i) & 1]
    out = []
    for m, n in st: out += [m]*n
    return out

class Engine:
    def __init__(self, T, E, stat):
        self.stat = stat; self.E = E; self.by = defaultdict(list); self.sizes = set()
        for cre, ann, amp in T:
            self.by[tuple(sorted(ann))].append((cre, ann, amp)); self.sizes.add(len(ann))
    def en(self, st): return sum(self.E[m] for m in modes_of(st, self.stat))
    def V(self, vec):
        out = defaultdict(float); app = app_F if self.stat == 'F' else app_B
        for st, c in vec.items():
            md = modes_of(st, self.stat)
            subs = set()
            for sz in self.sizes:
                for sub in itertools.combinations(md, sz): subs.add(tuple(sorted(sub)))
            for sub in subs:
                for cre, ann, amp in self.by.get(sub, ()):
                    ns, f = app(st, cre, ann)
                    if ns is not None: out[ns] += c*amp*f
        return out
    def rs4(self, psi):
        e0 = self.en(psi); v = self.V({psi: 1.0}); a = {}; e2 = 0.0; r2 = 0.0
        for n, c in v.items():
            if n == psi: continue
            d = e0 - self.en(n); a[n] = c/d; e2 += c*c/d; r2 += c*c/(d*d)
        b = self.V(a); first = 0.0
        for n, c in b.items():
            if n == psi: continue
            first += c*c/(e0 - self.en(n))
        return e2, first - e2*r2

def state(ms, stat):
    if stat == 'F':
        s = 0
        for m in ms: s |= 1 << m
        return s
    d = defaultdict(int)
    for m in ms: d[m] += 1
    return tuple(sorted(d.items()))

def closed(lat, mx, stat, new, s22=1.0, s31=1.0):
    """24-ordering (or subset) closed form on the finite lattice."""
    E, k, N = lat.E, lat.k, lat.N; p = k[mx]; Ex = E[mx]
    hh = (lambda e, w: hfac(e, w)) if stat == 'F' else (lambda e, w: 1.0)
    neg = lambda m: lat.f(lat.sp[m], -lat.q[m])
    tot = 0.0; one = 0.0
    for mA in lat.modes['A']:
        for mB in lat.modes['B']:
            mY = lat.f('Y', lat.q[mx] - lat.q[mA] - lat.q[mB])
            EY, EA, EB = E[mY], E[mA], E[mB]
            Wo = EY + EA + EB
            po = Psi3(lat, mY, mA, mB) if PRESC[0] != 'P2' else F(s2(EA, k[mA], EB, k[mB]))
            kern = {'dec': po*np.sqrt(hh(Ex, Wo)), 'vac': po,
                    '22': s22*F(s2(EA, k[mA], EB, k[mB])),
                    '31': s31*F(s2(Ex, p, E[neg(mA)], k[neg(mA)]))*F(s2(Ex, p, E[neg(mB)], k[neg(mB)]))*F(s2(EA, k[mA], EB, k[mB]))}
            if PRESC[0] == 'P2': kern['31'] = s31*F(s2(EA, k[mA], EB, k[mB]))
            nrm_o = legs(lat, mx, mY, mA, mB)**2/(2*Ex*2*EY*2*EA*2*EB)/N**2
            one += po*po*(hh(Ex, Wo)/(Ex - Wo) + (-1 if stat == 'F' else 1)/(-(Ex + Wo)))*nrm_o
            for mU in lat.modes['U']:
                for mC in lat.modes['C']:
                    mD = lat.f('D', lat.q[mY] - lat.q[mU] - lat.q[mC])
                    W = E[mU] + E[mC] + E[mD]
                    wi = legs(lat, mY, mU, mC, mD)**2*Psi3(lat, mU, mC, mD)**2/(2*EY*8*E[mU]*E[mC]*E[mD])/N**2
                    en = {'Y1': EY, 'Y2': EY, 'Phi': W, 'A': EA, 'B': EB, 'Xin': Ex, 'Xout': Ex}
                    hi = hh(EY, W)
                    for o in ORD:
                        allowed = ('dec', 'vac') + tuple(new)
                        if not (o['oa'] in allowed and o['ob'] in allowed):
                            continue
                        val = kern[o['oa']]*kern[o['ob']]*nrm_o*wi
                        val *= (np.sqrt(hi) if o['i1_dec'] else 1.0)*(np.sqrt(hi) if o['i2_dec'] else 1.0)
                        if stat == 'F' and (o['nback'] & 1): val = -val
                        for ls in o['pres']:
                            val /= (Ex - sum(en[x] for x in ls))
                        tot += val
    return tot, one

if __name__ == '__main__':
    stat = sys.argv[1] if len(sys.argv) > 1 else 'B'
    if len(sys.argv) > 2: PRESC[0] = sys.argv[2]
    t0 = time.time()
    pr(f'# R9-7 A: complete crossing set, brute-force RS4 vs 24-ordering closed form; statistics {stat}; prescription {PRESC[0]}; F plateau L1={L1} L2={L2}')
    mass = dict(X=0.30, Y=0.33, A=0.37, B=0.41, U=0.29, C=0.35, D=0.43)
    cases = [(5, dict(X=0, Y=0, A=0, B=0, U=0, C=0, D=0)), (6, dict(X=1, Y=1, A=0, B=0, U=1, C=0, D=0))]
    if stat == 'F': signsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    else: signsets = [(1, 1)]
    for (L, tw) in cases:
        lat = Lat(L, tw, mass)
        for new in [(), ('22',), ('31',), ('22', '31')]:
            for (a22, a31) in signsets if new else [(1, 1)]:
                res = {}
                for (go, gi) in [(1, 1), (1, 0), (0, 1)]:
                    T = build(lat, go, gi, stat, new, a22, a31)
                    eng = Engine(T, lat.E, stat)
                    ev = eng.rs4(state((), stat))
                    for mx in lat.modes['X'][:2]:
                        ex = eng.rs4(state((mx,), stat))
                        res[(go, gi, mx)] = (ex[0] - ev[0], ex[1] - ev[1])
                for mx in lat.modes['X'][:2]:
                    b = res[(1, 1, mx)][1] - res[(1, 0, mx)][1] - res[(0, 1, mx)][1]
                    best = None
                    for (c22, c31) in signsets:
                        cm, one = closed(lat, mx, stat, new, c22, c31)
                        if best is None or abs(b - cm) < abs(best[0]): best = (b - cm, c22, c31, cm, one)
                    pr(f'L={L} new={new} H-signs(s22,s31)=({a22:+d},{a31:+d}) k={lat.k[mx]:+.4f}: E2 {res[(1,0,mx)][0]:+.10e} (closed 1-loop {best[4]:+.10e}); '
                       f'mixed RS4(H) {b:+.15e}  closed {best[3]:+.15e}  diff {best[0]:+.1e}  [closed-form signs ({best[1]:+d},{best[2]:+d})]  t={time.time()-t0:.0f}s')
    open(__file__.replace('.py', f'_{stat}{"" if PRESC[0] == "P1" else "_" + PRESC[0]}.out'), 'w').write('\n'.join(OUT) + '\n')
