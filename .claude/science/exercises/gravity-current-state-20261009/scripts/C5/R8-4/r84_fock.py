"""R8-4 script B: the Hamiltonian itself, as explicit second-quantised monomials on a finite periodic lattice,
applied to Fock basis states with explicit CAR signs.  Rayleigh-Schroedinger shifts (one-particle minus vacuum)
are computed from H's matrix elements only, then compared with the closed forms used elsewhere.

Part 1 (one loop, model S, the four-species box Hamiltonian): RS2 from H  vs  closed form
        forward sum |A_f|^2/(E-W) + Pauli-blocked vacuum sum |A_0|^2/(E+W).   d = 1 (L = 6, 8; periodic and
        antiperiodic species) and d = 3 (L = 3, 4).
Part 2 (two-loop toy N): species X,Y,A,B (outer quartet) and Y,U,C,D (inner quartet).  RS4 mixed coefficient
        b = E4(go=1,gi=1) - E4(1,0) - E4(0,1) for X_p minus vacuum, from H,  vs the Goldstone linked closed form
        mixed = sum_outer w N(alpha, k_Y).   d = 1, small L.
Mode momenta k = pi*(2n + t_s)/L (t_s = 0 periodic, 1 antiperiodic); conservation sum q_created - sum q_annih = 0 mod 2L."""
import numpy as np, itertools, sys, time
from collections import defaultdict
np.seterr(all='ignore')
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
    e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def plateau(x, x1, x2): return 1.0 - sstep((np.abs(x) - x1)/(x2 - x1))
def wrap(k): return (k + np.pi) % (2*np.pi) - np.pi

# ---------------- generic sparse fermionic Fock engine ----------------
BOSE = [False]
def apply_ops_bose(state, ops):
    st = list(state); amp = 1.0
    for kind, md in reversed(ops):
        n = st.count(md)
        if kind == 'c':
            if n == 0: return None, 0
            amp *= np.sqrt(n); st.remove(md)
        else:
            amp *= np.sqrt(n + 1); st.append(md); st.sort()
    return tuple(st), amp

def apply_ops(state, ops):
    if BOSE[0]: return apply_ops_bose(state, ops)
    """ops: list of (kind, mode) applied right-to-left as written left-to-right in the monomial;
    i.e. monomial = ops[0] ops[1] ... ops[-1]; we apply ops[-1] first.  kind 'c' annihilate, 'a' create."""
    st = list(state); sign = 1
    for kind, md in reversed(ops):
        if kind == 'c':
            try: pos = st.index(md)
            except ValueError: return None, 0
            if pos & 1: sign = -sign
            st.pop(pos)
        else:
            if md in st: return None, 0
            pos = 0
            while pos < len(st) and st[pos] < md: pos += 1
            if pos & 1: sign = -sign
            st.insert(pos, md)
    return tuple(st), sign

class Ham:
    def __init__(self):
        self.by_ann = defaultdict(list)   # sorted ann tuple -> list of (ops, amp)
        self.sizes = set()
        self.E = {}
    def add(self, cre, ann, amp):
        """monomial amp * c+_{cre[0]}..c+_{cre[-1]} c_{ann[0]}..c_{ann[-1]}  plus its hermitian conjugate"""
        if amp == 0: return
        ops = [('a', c) for c in cre] + [('c', a) for a in ann]
        self.by_ann[tuple(sorted(ann))].append((ops, amp)); self.sizes.add(len(ann))
        opsh = [('a', a) for a in reversed(ann)] + [('c', c) for c in reversed(cre)]
        self.by_ann[tuple(sorted(cre))].append((opsh, np.conj(amp))); self.sizes.add(len(cre))
    def energy(self, st): return sum(self.E[m] for m in st)
    def applyV(self, vec):
        out = defaultdict(float)
        for st, c in vec.items():
            for sz in self.sizes:
                for sub in itertools.combinations(st, sz):
                    for ops, amp in self.by_ann.get(sub, ()):
                        ns, sg = apply_ops(st, ops)
                        if ns is not None: out[ns] += sg*amp*c
        return out

def rs(H, psi, order4=True):
    E0 = H.energy(psi)
    v1 = H.applyV({psi: 1.0})
    a = {}
    E2 = 0.0
    for n, c in v1.items():
        if n == psi: continue
        d = E0 - H.energy(n); a[n] = c/d; E2 += c*c/d
    if not order4: return E2, None, None
    E1 = v1.get(psi, 0.0)
    b = H.applyV(a)
    E3 = sum(a.get(n, 0.0)*c for n, c in b.items())
    E4 = 0.0
    for n, c in b.items():
        if n == psi: continue
        E4 += c*c/(E0 - H.energy(n))
    E4 -= E2*sum(c*c for c in a.values())
    return E2, E3, E4, E1

# ---------------- lattice kinematics ----------------
class Lat:
    def __init__(self, L, d, species, twist, mass):
        self.L, self.d = L, d; self.species = species; self.ns = L**d; self.N = L**d
        self.idx = {}; self.q = {}; self.k = {}; self.Em = {}
        mi = 0
        for s in species:
            for nvec in itertools.product(range(L), repeat=d):
                qv = tuple(2*n + twist[s] for n in nvec)
                kv = np.array([wrap(np.pi*qq/L) for qq in qv])
                self.idx[(s, nvec)] = mi; self.q[mi] = qv; self.k[mi] = kv
                self.Em[mi] = np.sqrt(mass[s]**2 + kv @ kv)    # = box dispersion on the leg-cutoff support
                mi += 1
        self.modes_of = {s: [self.idx[(s, n)] for n in itertools.product(range(L), repeat=d)] for s in species}
        self.qmap = {}
        for s in species:
            for m in self.modes_of[s]: self.qmap[(s, tuple(x % (2*L) for x in self.q[m]))] = m
    def conserve(self, cre, ann):
        tot = np.zeros(self.d, int)
        for m in cre: tot += np.array(self.q[m])
        for m in ann: tot -= np.array(self.q[m])
        return np.all(tot % (2*self.L) == 0)
    def find(self, s, qv):
        return self.qmap.get((s, tuple(int(x) % (2*self.L) for x in qv)))

def s_inv(lat, m1, m2):
    k = lat.k[m1] + lat.k[m2]; return (lat.Em[m1] + lat.Em[m2])**2 - k @ k

P = dict(L1=1.0, L2=1.4, A1=2.0, A2=2.5, C1=1.2, C2=1.6, C=1.0)
def Fs(s): return float(plateau(np.sqrt(max(s, 0.0)), P['L1'], P['L2']))
def legc(lat, m): return float(np.prod(plateau(lat.k[m], P['A1'], P['A2'])))
def totc(lat, m): return float(np.prod(plateau(lat.k[m], P['C1'], P['C2'])))
def Psi(lat, ms): return np.prod([Fs(s_inv(lat, a, b)) for a, b in itertools.combinations(ms, 2)])
def hfac(Ex, W): return (W*(1 + 2*P['C']) - Ex)/(W + Ex)

def build_S(lat, g=1.0):
    """model S: species A,B,C,D; vacuum term with all six pair factors; four forward terms."""
    H = Ham(); H.E = lat.Em; sp = lat.species; N = lat.N
    nvac = 0; nfw = 0
    for mA in lat.modes_of[sp[0]]:
        for mB in lat.modes_of[sp[1]]:
            for mC in lat.modes_of[sp[2]]:
                qD = tuple(-(np.array(lat.q[mA]) + lat.q[mB] + lat.q[mC]))
                mD = lat.find(sp[3], qD)
                if mD is None: continue
                ms = (mA, mB, mC, mD)
                amp = g*Psi(lat, ms)*np.prod([legc(lat, x) for x in ms])/np.sqrt(np.prod([2*lat.Em[x] for x in ms]))/N
                if amp != 0: H.add(ms, (), amp); nvac += 1
    for xi, X in enumerate(sp):
        rest = [s for s in sp if s != X]
        for mx in lat.modes_of[X]:
            for m1 in lat.modes_of[rest[0]]:
                for m2 in lat.modes_of[rest[1]]:
                    q3 = tuple(np.array(lat.q[mx]) - lat.q[m1] - lat.q[m2]); m3 = lat.find(rest[2], q3)
                    if m3 is None: continue
                    ms = (m1, m2, m3); W = sum(lat.Em[x] for x in ms); Ex = lat.Em[mx]
                    amp = g*Psi(lat, ms)*np.sqrt(hfac(Ex, W))*np.prod([legc(lat, x) for x in ms])*totc(lat, mx)/np.sqrt(2*Ex*np.prod([2*lat.Em[x] for x in ms]))/N
                    if amp != 0: H.add(ms, (mx,), amp); nfw += 1
    return H, nvac, nfw

def closed_S(lat, H, mx):
    """closed-form one-loop shift for the one-particle state mx from the same amplitudes (read back from H)."""
    Ex = lat.Em[mx]; fw = 0.0; zz = 0.0
    for ops, amp in H.by_ann.get((mx,), ()):
        cre = [m for k_, m in ops if k_ == 'a']
        if len(cre) == 3: fw += amp**2/(Ex - sum(lat.Em[c] for c in cre))
    for ops, amp in H.by_ann.get((), ()):
        cre = [m for k_, m in ops if k_ == 'a']
        if mx in cre: zz += amp**2/(sum(lat.Em[c] for c in cre))
    return fw + zz

if __name__ == '__main__':
    t0 = time.time()
    pr('# R8-4 B part 1: one-loop shift of model S from the explicit Fock Hamiltonian vs closed form')
    pr(f'# params {P}')
    for (L, d, tw) in [(6, 1, (0, 0, 0, 0)), (8, 1, (1, 1, 0, 0)), (3, 3, (0, 0, 0, 0)), (4, 3, (1, 1, 0, 0))]:
        sp = ['A', 'B', 'C', 'D']; mass = dict(A=0.3, B=0.3, C=0.3, D=0.3)
        lat = Lat(L, d, sp, dict(zip(sp, tw)), mass)
        H, nv, nf = build_S(lat)
        E2v = rs(H, (), order4=False)[0]
        pr(f'## L={L} d={d} twists={tw}: {nv} vacuum monomials, {nf} forward monomials (each + h.c.)  t={time.time()-t0:.1f}s')
        for s in sp[:4:2] if d == 3 else sp:
            for mx in lat.modes_of[s][:3 if d == 3 else 4]:
                E2x = rs(H, (mx,), order4=False)[0]
                cf = closed_S(lat, H, mx)
                pr(f'   {s} k={np.round(lat.k[mx],3)}  RS2(H): {E2x - E2v:+.15e}   closed: {cf:+.15e}   diff {E2x - E2v - cf:+.1e}')
    open(__file__.replace('.py', '_part1.out'), 'w').write('\n'.join(OUT) + '\n')
