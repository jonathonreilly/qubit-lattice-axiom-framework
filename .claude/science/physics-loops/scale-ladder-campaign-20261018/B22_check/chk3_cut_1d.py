"""B22 check 3: Definition A (causal-cut timing), own implementation.

Circuit: sites 2i = a_i (X = i), 2i+1 = b_i (X = i + 1/2).  Layer t even: gate u1 = [[-is, c], [c, -is]] on
(a_i, b_i) at X = i + 1/4; layer t odd: swap on (b_i, a_{i+1}) at X = i + 3/4.  One period = 2 layers = the walk
W(k) = [[c e^{-ik}, -is e^{-ik}], [-is e^{ik}, c e^{ik}]].
Cut by a layer-valued function F: gate (bond, t) is applied iff 0 <= t < F(X_bond) (inverse gates for
F(X_bond) <= t < 0).  Wire count lambda_s = number of applied gates touching site s.

Checks:
 L1 [exhaustive over random cuts] adjacency |lambda_s - lambda_{s+1}| <= 1 for every past-closed cut, and
    #odd wires >= T, with T := sum over cyclically consecutive maximal even-count runs of |Delta(lambda/2)|.
    (A precise version of B22's C4; "total variation of the period count" needs this definition: e.g.
    counts 2n+2, 2n+1, 2n+2 have one odd wire and floor(lambda/2)-variation 2.)
 L2 [exact, theta = 0] chirality bookkeeping: R content (from a-sites) ends on even-count a-wires and on
    odd-count b-wires; hence in any window, #R contents - #a-slots = #odd b - #odd a; the cumulative
    imbalance along the cut reaches O(A) for lapse amplitude A periods, so a chirality-preserving
    identification of cut data with flat data must move content by O(A) cells (not lattice-local).
 L3 [reproduction] B22 C5 displacements for theta = 0 and 0.2 (A = 16, 32, Lc = 4096), independently coded.
 L4 [new, decisive for the scope of "A fails"] massive walk at FIXED lapse tilt (A kk const, Lc = 128 A),
    A = 16 ... 128: does the A-commutator approach -w g(k0) as the lapse amplitude grows?
"""
import time
import numpy as np

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"\n        {detail}" if detail else ""))
t0 = time.time()
rng = np.random.default_rng(2022)

class Circuit:
    def __init__(self, Lc, th):
        self.Lc, self.th = Lc, th; self.n = 2 * Lc
        c, s = np.cos(th), np.sin(th)
        self.g = [np.array([[-1j * s, c], [c, -1j * s]]), np.array([[0, 1], [1, 0]], complex)]
        i = np.arange(Lc)
        self.pairs = [(2 * i, 2 * i + 1), (2 * i + 1, (2 * i + 2) % self.n)]
        self.Xb = [i + 0.25, i + 0.75]
    def gate_sets(self, F):
        """list of (t, mask, inverse) in application order: inverse part (descending t), then forward."""
        Fb = [F(self.Xb[0]), F(self.Xb[1])]
        lo = int(np.floor(min(Fb[0].min(), Fb[1].min()))) - 2; hi = int(np.ceil(max(Fb[0].max(), Fb[1].max()))) + 2
        ops = []
        for t in range(-1, lo, -1):
            m = Fb[t % 2] <= t
            if m.any(): ops.append((t, m, True))
        for t in range(0, hi):
            m = t < Fb[t % 2]
            if m.any(): ops.append((t, m, False))
        return ops
    def counts(self, F):
        lam = np.zeros(self.n, int)
        for t, m, inv in self.gate_sets(F):
            p, q = self.pairs[t % 2]
            lam[p[m]] += 1; lam[q[m]] += 1
        return lam
    def _layer(self, psi, t, m, inv):
        u = self.g[t % 2]; u = u.conj().T if inv else u
        p, q = self.pairs[t % 2]; p, q = p[m], q[m]
        x, y = psi[..., p].copy(), psi[..., q].copy()
        psi[..., p] = u[0, 0] * x + u[0, 1] * y; psi[..., q] = u[1, 0] * x + u[1, 1] * y
    def evolve(self, psi, F, dagger=False):
        psi = psi.copy(); ops = self.gate_sets(F)
        if dagger:
            for t, m, inv in reversed(ops): self._layer(psi, t, m, not inv)
        else:
            for t, m, inv in ops: self._layer(psi, t, m, inv)
        return psi
    def commutator(self, psi, FN, FM):     # W_N W_M W_N^dag W_M^dag psi
        p = self.evolve(psi, FM, True); p = self.evolve(p, FN, True); p = self.evolve(p, FM); return self.evolve(p, FN)
    # Bloch data
    def Wk(self, k):
        c, s = np.cos(self.th), np.sin(self.th)
        return np.array([[c * np.exp(-1j * k), -1j * s * np.exp(-1j * k)], [-1j * s * np.exp(1j * k), c * np.exp(1j * k)]])
    def plus_vec(self, k):
        ev, V = np.linalg.eig(self.Wk(k)); j = np.argmax(-np.angle(ev)); v = V[:, j] / np.linalg.norm(V[:, j])
        return v * np.exp(-1j * np.angle(v[np.argmax(abs(v))]))
    def packet(self, k0, X0, sig):
        k = 2 * np.pi * np.fft.fftfreq(self.Lc); dk = (k - k0 + np.pi) % (2 * np.pi) - np.pi
        A = np.zeros((self.Lc, 2), complex)
        for j in np.where(np.abs(dk) * sig < 6)[0]:
            A[j] = np.exp(-(dk[j] * sig) ** 2) * np.exp(-1j * k[j] * X0) * self.plus_vec(k[j])
        cells = np.fft.ifft(A, axis=0)              # psi_i = sum_k e^{iki} A_k
        psi = np.empty(self.n, complex); psi[0::2], psi[1::2] = cells[:, 0], cells[:, 1]
        return psi / np.linalg.norm(psi)
    def plus_weight(self, psi):
        cells = np.stack([psi[0::2], psi[1::2]], 1); A = np.fft.fft(cells, axis=0)
        k = 2 * np.pi * np.fft.fftfreq(self.Lc)
        tot = np.sum(np.abs(A) ** 2)
        return sum(abs(np.vdot(self.plus_vec(k[j]), A[j])) ** 2 for j in range(self.Lc) if np.abs(A[j]).max() > 1e-9 * np.sqrt(tot)) / tot
    def xmean(self, psi):
        Xs = np.arange(self.n) / 2.0; p = np.abs(psi) ** 2
        z = np.sum(p * np.exp(2j * np.pi * Xs / self.Lc)); return self.Lc * np.angle(z) / (2 * np.pi)

def omega(k, th): return np.arccos(np.cos(th) * np.cos(k))
def gfun(k, th):
    o = omega(k, th); d = np.cos(th) * np.sin(k) / np.sin(o)
    return d**2 + o * np.cos(o) * (1 - d**2) / np.sin(o)

def stair(y, d):
    f = np.floor(y); r = y - f
    return f + np.clip((r - 0.5) / d + 0.5, 0, 1)

# ---------------------------------------------------------------- L1 lemma over random cuts
def T_of(lam):
    ev = lam % 2 == 0
    if ev.all(): return 0
    # cyclic maximal even runs
    s0 = np.argmax(~ev); l = np.roll(lam, -s0); e = l % 2 == 0
    runs = []; i = 0; nn = len(l)
    while i < nn:
        if e[i]:
            j = i
            while j < nn and e[j]: j += 1
            runs.append(l[i] // 2); i = j
        else: i += 1
    if len(runs) <= 1: return 0
    return int(sum(abs(runs[(r + 1) % len(runs)] - runs[r]) for r in range(len(runs))))
C = Circuit(96, 0.3); bad_adj = bad_T = 0; ntr = 0; examples = []
for trial in range(400):
    # random smooth lapse with |dF/dX| < 2 layers per cell (past-closed)
    modes = rng.integers(1, 6, size=3); amps = rng.normal(size=3); ph = rng.uniform(0, 2 * np.pi, 3)
    raw = lambda X: sum(a_ * np.cos(2 * np.pi * m_ * X / 96 + p_) for a_, m_, p_ in zip(amps, modes, ph))
    Xg = np.linspace(0, 96, 4000); slope = np.abs(np.gradient(raw(Xg), Xg)).max()
    sc = rng.uniform(0.2, 1.95) / slope
    off = rng.uniform(-3, 3); kind = rng.integers(2)
    if kind == 0: F = lambda X: sc * raw(X) + off
    else: F = lambda X: 2 * stair((sc * raw(X) + off) / 2, 0.3)       # staircase variant (may be steeper locally)
    Fs = lambda X: F(X)
    # verify past-closure directly: adjacent bonds' top layers differ by <= 1 in the required way
    lam = C.counts(Fs)
    adj = np.abs(np.diff(np.r_[lam, lam[0]])).max()
    # past-closure test: each applied forward gate's predecessors applied
    pc = True
    ops = C.gate_sets(Fs); applied = {}
    for t, m, inv in ops: applied[t] = m
    for t, m in applied.items():
        if t >= 1 and (t - 1) in applied:
            prev = applied[t - 1]
            if t % 2 == 1:   # odd bond i (b_i, a_{i+1}) needs even bonds i and i+1 at t-1
                need = prev & np.roll(prev, -1)
            else:            # even bond i (a_i, b_i) needs odd bonds i-1 and i at t-1
                need = prev & np.roll(prev, 1)
            if np.any(m & ~need): pc = False
        elif t >= 1 and m.any(): pc = False
    if not pc: continue
    ntr += 1
    bad_adj += adj > 1
    odd = int(np.sum(lam % 2)); T = T_of(lam)
    bad_T += odd < T
    if len(examples) < 3 and T > 0: examples.append((odd, T))
check("L1 [exhaustive over random past-closed cuts] adjacent wire counts differ by <= 1 and #odd-count wires >= T"
      " (T over consecutive even runs)", ntr > 100 and bad_adj == 0 and bad_T == 0,
      f"{ntr} past-closed cuts tested; adjacency violations {bad_adj}; lemma violations {bad_T}; examples (odd, T) {examples}")

# ---------------------------------------------------------------- L2 massless chirality bookkeeping
C0 = Circuit(512, 0.0); kk0 = 2 * np.pi / 512
info = []; okc = True
for A in (4, 8, 16):
    F = lambda X: 2 * stair(A * np.cos(kk0 * X) + 0.37, min(0.9, 1.5 * A * kk0))
    lam = C0.counts(F)
    src = np.arange(C0.n)
    tag = C0.evolve(src.astype(complex)[None, :].repeat(1, 0) * 0 + np.eye(C0.n)[:, :][0:0].sum(0) if False else None, F) if False else None
    # permutation: push the identity through (rows), cheap: evolve basis via index tracking with a label vector
    lab = (np.arange(C0.n) + 1).astype(complex)
    out = C0.evolve(lab, F)                         # theta = 0 gates are swaps: labels are permuted exactly
    srcs = np.rint(out.real).astype(int) - 1
    isR = srcs % 2 == 0                             # content from a-sites = right movers
    a_slot = np.arange(C0.n) % 2 == 0
    oddw = lam % 2 == 1
    ok_book = np.array_equal(isR, a_slot ^ oddw)
    imb = np.cumsum((isR.astype(int) - a_slot.astype(int)))
    pred_imb = np.cumsum((oddw & ~a_slot).astype(int) - (oddw & a_slot).astype(int))
    okc &= ok_book and np.array_equal(imb, pred_imb)
    info.append(f"A={A}: bookkeeping {'ok' if ok_book else 'FAIL'}, max cumulative R-imbalance {np.abs(imb - imb.mean()).max():.1f} slots")
mx = [float(s.split('imbalance ')[1].split()[0]) for s in info]
check("L2 [exact, theta = 0] R content sits exactly on even-count a-wires and odd-count b-wires; window imbalance"
      " #R - #a-slots = #odd b - #odd a; the cumulative imbalance grows ~ A (lapse amplitude in periods)",
      okc and mx[1] > 1.6 * mx[0] and mx[2] > 1.6 * mx[1], "; ".join(info))

# ---------------------------------------------------------------- L3 reproduce B22 C5 (staircase lapses)
print("\n  L3: staircase integer-period lapses N = A cos, M = A sin, Lc = 4096, sigma = 20, X0 = 1000")
print("  theta  A   k0     dx         -w g(k0)   ratio    +band weight")
L3 = {}
for th in (0.0, 0.2):
    Cc = Circuit(4096, th); kk = 2 * np.pi / 4096
    for A in (16, 32):
        d = min(0.9, 1.5 * A * kk)
        FN = lambda X: 2 * stair(A * np.cos(kk * X), d); FM = lambda X: 2 * stair(A * np.sin(kk * X), d)
        w = A * A * kk
        for k0 in (0.1, -0.1):
            psi = Cc.packet(k0, 1000.0, 20.0); out = Cc.commutator(psi, FN, FM)
            dx = Cc.xmean(out) - Cc.xmean(psi); pr = -w * gfun(k0, th) if th > 0 else -w
            L3[(th, A, k0)] = dx
            print(f"  {th:.1f}   {A:2d}  {k0:+.1f}  {dx:9.4f}  {pr:9.4f}  {dx / pr:7.3f}   {Cc.plus_weight(out):.4f}")
ref = {(0.0, 16, 0.1): -0.7749, (0.0, 16, -0.1): 0.9001, (0.0, 32, 0.1): -2.4577, (0.0, 32, -0.1): 2.1784,
       (0.2, 16, 0.1): -0.3824, (0.2, 16, -0.1): -0.2375, (0.2, 32, 0.1): -1.4107, (0.2, 32, -0.1): -1.2606}
dev = max(abs(L3[k_] - ref[k_]) for k_ in ref)
check("L3 [reproduction, independent code] B22 C5 table values (theta = 0, 0.2; A = 16, 32) reproduced", dev < 2e-3,
      f"max |difference| from B22's log: {dev:.1e}")

# ---------------------------------------------------------------- L4 fixed-tilt scaling
print("\n  L4: fixed tilt A*kk = 2pi/128 (Lc = 128 A), staircase lapses, X0 = 0.244 Lc, sigma = 20")
print("  theta  A    Lc      k0     dx         -w g(k0)   ratio   +band weight")
L4 = {}
for th in (0.0, 0.2, 0.5):
    for A in (16, 32, 64, 128):
        Lc = 128 * A; Cc = Circuit(Lc, th); kk = 2 * np.pi / Lc
        d = min(0.9, 1.5 * A * kk)
        FN = lambda X: 2 * stair(A * np.cos(kk * X), d); FM = lambda X: 2 * stair(A * np.sin(kk * X), d)
        w = A * A * kk
        for k0 in (0.1, -0.1):
            psi = Cc.packet(k0, 0.244 * Lc, 20.0); out = Cc.commutator(psi, FN, FM)
            dx = Cc.xmean(out) - Cc.xmean(psi); pr = -w * gfun(k0, th) if th > 0 else -w
            wt = Cc.plus_weight(out)
            L4[(th, A, k0)] = (dx / pr, wt)
            print(f"  {th:.1f}  {A:3d}  {Lc:6d}  {k0:+.1f}  {dx:9.4f}  {pr:9.4f}  {dx / pr:7.3f}   {wt:.4f}")
for th in (0.2, 0.5):
    dv = [max(abs(L4[(th, A, k0)][0] - 1) for k0 in (0.1, -0.1)) for A in (16, 32, 64, 128)]
    print(f"  theta = {th}: max |ratio - 1| vs A = 16..128: {np.round(dv, 4)}")
dv0 = [max(abs(L4[(0.0, A, k0)][0] - 1) for k0 in (0.1, -0.1)) for A in (16, 32, 64, 128)]
print(f"  theta = 0: max |ratio - 1| vs A: {np.round(dv0, 3)}")
check("L4a [numerical] massless walk at fixed tilt: Definition A's commutator does NOT approach -w (deviation stays O(1))",
      min(dv0) > 0.5, f"{np.round(dv0, 3)}")
dv2 = [max(abs(L4[(0.2, A, k0)][0] - 1) for k0 in (0.1, -0.1)) for A in (16, 32, 64, 128)]
dv5 = [max(abs(L4[(0.5, A, k0)][0] - 1) for k0 in (0.1, -0.1)) for A in (16, 32, 64, 128)]
check("L4b [numerical, informational: PASS = the deviation shrinks monotonically with A at fixed tilt for both massive"
      " theta] massive walk: Definition A approaches -w g(k0) as the lapse amplitude grows",
      all(dv2[i + 1] < dv2[i] for i in range(3)) and all(dv5[i + 1] < dv5[i] for i in range(3)),
      f"theta=0.2: {np.round(dv2, 4)}; theta=0.5: {np.round(dv5, 4)}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}  ({time.time() - t0:.1f} s)")
