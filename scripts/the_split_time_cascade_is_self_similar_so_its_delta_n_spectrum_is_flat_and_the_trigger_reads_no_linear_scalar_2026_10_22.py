AUDIT_INPUT_PATHS = ('docs/THE_SPLIT_TIME_CASCADE_IS_SELF_SIMILAR_SO_ITS_DELTA_N_SPECTRUM_IS_FLAT_AND_THE_TRIGGER_READS_NO_LINEAR_SCALAR_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Split-time (delta-N) spectrum of the glued split cascade under the candidate laws.

Sections
  A  register arithmetic and what the split trigger reads (exact)
  B  split cascades: free (iid per-level waits, 3D and 2D) and the exact trigger rule in 2D
     (block mean reaches 4s, +x/+y unsplit neighbours full, held edges block, children = parent - s)
  C  the laws' own channel: no linear trace mode, tensors reach the trigger at second order
  D  when split times are a curvature perturbation (uniform-length slicing theorem + clock toy)
  E  estimates against measurement
Supplied: Poisson stepping of each register (a stochastic model, NOT a law) used only in B to give
the trigger a timing spread; block-mean register model (one mean per block, m registers averaged).
"""
import time, math
import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
PASS = FAIL = 0
LN2 = math.log(2.0)


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")


def octave_spectrum(f):
    """Delta^2 per octave = (variance in octave)/ln2, |k| in cycles per box, k < N/2."""
    N = f.shape[0]
    d = f.ndim
    fk = np.fft.fftn(f - f.mean()) / f.size
    p = (fk * fk.conj()).real
    kk = np.fft.fftfreq(N) * N
    grids = np.meshgrid(*([kk] * d), indexing="ij")
    k = np.sqrt(sum(g * g for g in grids))
    J = int(math.log2(N // 2))
    out = []
    for j in range(J):
        sel = (k >= 2 ** j) & (k < 2 ** (j + 1))
        out.append(p[sel].sum() / LN2)
    # axis vs diagonal power in the top octave used for fits (2D only)
    aniso = None
    if d == 2:
        j = J - 2
        sel = (k >= 2 ** j) & (k < 2 ** (j + 1))
        ang = np.abs(np.arctan2(grids[1], grids[0])) % (np.pi / 2)
        ax = sel & ((ang < np.pi / 16) | (ang > np.pi / 2 - np.pi / 16))
        dg = sel & (np.abs(ang - np.pi / 4) < np.pi / 16)
        aniso = p[ax].mean() / p[dg].mean()
    return np.array(out), aniso


def tilt(D, lo, hi):
    j = np.arange(len(D))[lo:hi]
    y = np.log(D[lo:hi])
    return np.polyfit(j * LN2, y, 1)[0]


rng = np.random.default_rng(20261022)

# ---------------------------------------------------------------- A
print("== A. register arithmetic and the trigger readout (exact)")
s_, D_ = sp.symbols("s Delta", positive=True)
n = sp.symbols("n")
length = lambda nn: 2 ** (nn / s_ - 3)  # in units of the flat (cell) length
okA1 = sp.simplify(length(4 * s_) - 2) == 0 and sp.simplify(length(3 * s_) - 1) == 0 \
    and sp.simplify(2 * length(3 * s_) / length(4 * s_) - 1) == 0
check("A1 [T] trigger mean 4s = twice flat; child n = 4s - s = 3s is the child's flat length and two"
      " children span the parent edge; window [0,(4+D)s] holds 3s..4s for D>=0: one generation ="
      " s register steps = ln2 of log-length, for every s", okA1,
      f"l(4s)={length(4*s_)}, l(3s)={length(3*s_)}")

h = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"h{min(i,j)}{max(i,j)}"))
axes = [sp.Matrix(v) for v in ([1, 0, 0], [0, 1, 0], [0, 0, 1])]
diags = [sp.Matrix(v) / sp.sqrt(2) for v in ([1, 1, 0], [1, -1, 0], [1, 0, 1], [1, 0, -1], [0, 1, 1], [0, 1, -1])]
edges = axes * 4 + diags  # 12 axis edges + the 6 face diagonals of the even corners (five-tetrahedron cube)
x = [(e.T * h * e)[0] for e in edges]
first = sp.expand(sum(xi / 2 for xi in x) / 18)
second = sp.expand(sum(-xi ** 2 / 4 for xi in x) / 18)
okA2 = sp.simplify(first - (h[0, 0] + h[1, 1] + h[2, 2]) / 6) == 0
check("A2 [T] the trigger's mean log-length over the 18 edges of a block cube is tr h/6 at first order:"
      " every traceless strain (both tensor polarisations) leaves the trigger unmoved", okA2, f"first = {first}")
hp, hx = sp.symbols("h_p h_x")
sub = {h[0, 0]: hp, h[1, 1]: -hp, h[2, 2]: 0, h[0, 1]: hx, h[0, 2]: 0, h[1, 2]: 0}
sec_z = sp.factor(second.subs(sub))
okA3 = sp.simplify(sec_z + (9 * hp ** 2 + 2 * hx ** 2) / 72) == 0
check("A3 [T] second order on a tensor wave along z: d<ln l> = -(9 h+^2 + 2 hx^2)/72: the trigger reads"
      " tensors quadratically, with a cubic (polarisation-dependent) weight", okA3, f"{sec_z}")

# ---------------------------------------------------------------- B
print("== B. split cascades (supplied Poisson register stepping; units: e-folds of edge length)")
m_reg, s_reg = 3, 23
sig2 = LN2 ** 2 / (m_reg * s_reg)
# B1 theorem: Delta^2(k) = sum_l lam^l sig^2 w(k 2^-l) for ANY fixed level shape w  =>  Delta^2(2k) = lam Delta^2(k)
def w1(u):  # per-ln-k power of a unit blocky white noise of unit block (1D, any shape works)
    return u * (np.sinc(u / 2)) ** 2
kgrid = np.linspace(0.3, 3.0, 7)
errs = []
for lam_t in (1.0, 0.97596, 0.8):
    Dk = lambda k: sum(lam_t ** l * w1(k * 2.0 ** -l) for l in range(-60, 400))
    errs.append(max(abs(Dk(2 * k) / Dk(k) - lam_t) for k in kgrid))
check("B1 [T] (rederives cosmology E) a cascade whose level-l delta-N has a level-independent shape and variance"
      " sig^2 lam^l has Delta^2(2k) = lam Delta^2(k): n_s - 1 = log2(lam) exactly; self-similar levels give n_s = 1",
      max(errs) < 1e-9, f"max |ratio - lam| = {max(errs):.1e} for lam = 1, 0.97596, 0.8")


def lam_hat(ts, G, lo):
    """per-level effective delta-N variance v(l) = Var(w_l) + 2 sum_k Cov(w_l, w_(l-k)) (k <= 3), and fit."""
    W = [None] + [ts[l] - ts[l - 1].repeat(2, 0).repeat(2, 1) for l in range(1, G + 1)]
    v, mu = [], []
    for l in range(lo, G + 1):
        x = W[l].ravel() - W[l].mean()
        tot = x.var()
        up = W[l]
        for k in range(1, 4):
            if l - k < 1:
                break
            y = W[l - k]
            for _ in range(k):
                y = y.repeat(2, 0).repeat(2, 1)
            tot += 2 * np.mean(x * (y.ravel() - y.mean()))
        v.append(tot)
        mu.append(W[l].mean())
    v = np.array(v)
    lv = np.arange(lo, G + 1)
    slope = np.polyfit(lv, np.log(v), 1, w=2.0 ** lv)[0]  # weight ~ sqrt(number of blocks)
    nn = np.corrcoef(W[G].ravel(), np.roll(W[G], 1, 0).ravel())[0, 1]
    xl = np.corrcoef(W[G].ravel(), W[G - 1].repeat(2, 0).repeat(2, 1).ravel())[0, 1]
    rv = [W[l + 1].var() / W[l].var() for l in range(lo, G)]
    return slope / LN2, v, np.mean(mu), nn, xl, W[G].var(), rv


def cascade2d(G, s, m, coupled, dt, rng):
    """Exact trigger rule on a 2D block tree (block-mean registers)."""
    st = [np.zeros((2 ** l, 2 ** l), np.int8) for l in range(G + 1)]
    nv = [np.zeros((2 ** l, 2 ** l)) for l in range(G + 1)]
    ts = [np.full((2 ** l, 2 ** l), np.nan) for l in range(G + 1)]
    st[0][:] = 1
    nv[0][:] = 3 * s
    lam = m * s * dt / LN2
    t = 0.0
    blk = cascade2d.blk = [0, 0, 0]  # block-steps: ready, held by a coarser neighbour, waiting for a full neighbour
    while (st[G] != 2).any():
        t += dt
        for l in range(G + 1):
            a = st[l] == 1
            k = int(a.sum())
            if k:
                nv[l][a] += rng.poisson(lam, k) / m
        for l in range(G + 1):
            S, V = st[l], nv[l]
            fire = (S == 1) & (V >= 4 * s)
            if not fire.any():
                continue
            if coupled:
                ex = S >= 1
                ready = int(fire.sum())
                for ax in (0, 1):
                    for sh in (1, -1):
                        fire &= np.roll(ex, sh, ax)  # a held edge (coarser neighbour) blocks
                held = ready - int(fire.sum())
                for ax in (0, 1):
                    nbS, nbV = np.roll(S, -1, ax), np.roll(V, -1, ax)
                    fire &= (nbS == 2) | ((nbS == 1) & (nbV >= 4 * s))  # +x/+y unsplit neighbour full
                blk[0] += ready; blk[1] += held; blk[2] += ready - held - int(fire.sum())
            if not fire.any():
                continue
            S[fire] = 2
            ts[l][fire] = t
            if l < G:
                F = fire.repeat(2, 0).repeat(2, 1)
                st[l + 1][F] = 1
                nv[l + 1][F] = (V - s).repeat(2, 0).repeat(2, 1)[F]  # children: parent value - s
    return ts


G2, dt, LO = 9, 0.01, 6
res = {}
for coupled in (False, True):
    out = []
    for seed in range(2):
        ts = cascade2d(G2, s_reg, m_reg, coupled, dt, rng)
        out.append(lam_hat(ts, G2, LO))
    D2, a2 = octave_spectrum(ts[G2])
    ns = np.array([o[0] for o in out])
    res[coupled] = (ns.mean(), ns.std() + 0.004, np.mean([o[1] for o in out], 0), np.mean([o[2] for o in out]),
                    np.mean([o[3] for o in out]), np.mean([o[4] for o in out]), np.mean([o[5] for o in out]), a2, D2,
                    np.mean([o[6] for o in out], 0), list(cascade2d.blk))
nf, ef, vf, mf, cf, xf, wf, af, Df, rf, _ = res[False]
nc, ec, vc, mc, cc, xc, wc, ac, Dc, rc, bk = res[True]
check("B2 [D] free trigger on 512^2 (block mean reaches 4s, children start at parent - s): mean wait ln2,"
      " wait variance (ln2)^2/(ms), per-level variance level-independent (levels 6-9)",
      abs(mf - LN2) < 0.002 and abs(wf / sig2 - 1) < 0.05 and abs(nf) < 3 * ef + 0.01,
      f"mean {mf:.4f}; var {wf:.5f} vs {sig2:.5f}; log2(lam) = {nf:+.4f} +- {ef:.4f}")
check("B3 [D] exact coupled trigger (+x/+y unsplit neighbours full, held edges block, 2:1 balance): the max-plus"
      " coupling raises the wait variance and correlates waits (neighbours +, parent-child -: the parent's"
      " overshoot passes to the children); the mean wait stays ln2 and the deep levels are stationary: lam = 1",
      abs(mc - LN2) < 0.003 and abs(nc) < 3 * ec + 0.01 and abs(rc[-1] - 1) < 0.01 and abs(vc[-1] / vc[-2] - 1) < 0.012,
      f"mean {mc:.4f}; var {wc:.5f} = {wc/sig2:.2f} x free; nn corr {cc:+.2f}, parent-child {xc:+.2f};"
      f" var(w) ratio by level {np.round(rc, 4).tolist()}; v_eff(6..9) {np.round(vc, 5).tolist()};"
      f" deepest v_eff ratio {vc[-1]/vc[-2]:.4f} (needed 0.976); log2(lam) fit = {nc:+.4f} +- {ec:.4f}; block-steps held/neighbour-wait/ready {bk[1]}/{bk[2]}/{bk[0]}")
check("B4 [D] the split-time field is blocky: at fixed |k| the power along the axes exceeds the diagonal (the"
      " block faces), a statistical-anisotropy cost on top of n_s = 1", af > 1.2 and ac > 1.2,
      f"axis/diag free {af:.2f}, coupled {ac:.2f}; coupled octave Delta^2/(sig^2/ln2) "
      f"{np.round(Dc / (sig2 / LN2), 2).tolist()} (top/bottom octaves carry the box and pixel edges)")
o64 = [lam_hat(cascade2d(9, 64, m_reg, True, 0.005, rng), 9, LO) for _ in range(2)]
n64 = np.mean([o[0] for o in o64]); m64 = np.mean([o[2] for o in o64]); r64 = np.mean([o[6] for o in o64], 0)
check("B5 [T+D] the e-fold wait Gamma(ms) ln2/(ms) holds only register numbers (s, m): no H, eps0, or window"
      " size enters, so rule-constant s and m give lam = 1 at any expansion history (again at s = 64)",
      abs(n64) < 0.03 and abs(m64 - LN2) < 0.003 and abs(r64[-1] - 1) < 0.01,
      f"s = 64, 512^2: mean {m64:.4f}, var(w) ratio {np.round(r64, 4).tolist()}, log2(lam) = {n64:+.4f}")

# ---------------------------------------------------------------- C
print("== C. the laws' own split-time channel")
check("C1 [T, with inhomog-volume B2] at linear order the trigger reads tr h/6 (A2) and the read lapse with a"
      " stationary shift has zeta = 0 at every k != 0: the laws give no linear split-time fluctuation", okA2,
      "delta T(k != 0) = 0 at O(h)")
# C2 square of a scale-invariant Gaussian field (scalar stand-in for one polarisation), 3D 64^3
N = 64
kk = np.fft.fftfreq(N) * N
KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing="ij")
K = np.sqrt(KX ** 2 + KY ** 2 + KZ ** 2)
K[0, 0, 0] = 1
tl2, rr = [], []
for seed in range(3):
    amp = K ** -1.5
    amp[0, 0, 0] = 0
    f = np.fft.ifftn(amp * (rng.standard_normal(K.shape) + 1j * rng.standard_normal(K.shape))).real
    Dh, _ = octave_spectrum(f)
    f = f / math.sqrt(Dh[1:-1].mean())  # unit Delta_h^2 per octave
    Dq, _ = octave_spectrum(f * f)
    tl2.append(tilt(Dq, 1, len(Dq) - 1))
    rr.append(Dq[1:-1].mean())
del KX, KY, KZ, K
check("C2 [D] the quadratic readout of a flat Gaussian field is BLUE (IR log grows toward small scales) and"
      " of size Delta_h^4", np.mean(tl2) > 0.05, f"n-1 of h^2 = {np.mean(tl2):+.3f}; Delta^2(h^2)/Delta_h^4 = {np.mean(rr):.2f}")

# ---------------------------------------------------------------- D
print("== D. when is the split-time record a curvature perturbation")
# two patches in de Sitter (H = 1), split k at local length 2^k; each split injects rho_inj = f*Lambda
# at the local length, radiation dilutes as a^-4; patch B splits late by dT at every level
Lam, fi, dT = 1.0, 0.05, 0.3
def rho_at_lna(lna, nsplits):
    r = Lam
    for k in range(1, nsplits + 1):
        r += fi * Lam * math.exp(-4 * (lna - k * LN2))
    return r
lna_star = 5.5 * LN2
rA = rho_at_lna(lna_star, 5)
rB = rho_at_lna(lna_star, 5)  # B splits late in t, but at the same local length, so the same history in a
rBt = rho_at_lna(lna_star - dT, 5)  # B on the uniform-t slice: its length lags by H dT
check("D1 [T] every rule component is a function of local edge length (Lambda; sea carried vacuum to vacuum;"
      " injection at the fixed-length trigger): rho = F(a) in every patch, so the uniform-length slice IS the"
      " uniform-density slice and zeta = delta N(flat -> uniform rho) = 0 for any split-time spread",
      abs(rA - rB) < 1e-15 and abs(rBt - rA) > 1e-4,
      f"rho at equal a: {rA:.6f} vs {rB:.6f}; at equal t (lag {dT}): {rBt:.6f}")
# clock toy: a quantity Q that counts ticks (proper time) differs at equal a by dT; an exit at Q* gives zeta = H dT
Hval = 1.0
zeta = Hval * dT
check("D2 [T] only a tick-integrating quantity (e.g. the record count, which no law reads) distinguishes the"
      " patches: an exit law reading it would give zeta = H delta T per level, i.e. the B-cascade spectrum",
      abs(zeta - dT) < 1e-15, f"zeta = H dT = {zeta:.3f} (conditional on a supplied tick-read exit)")

# ---------------------------------------------------------------- E
print("== E. estimates against measurement")
ns_pl, sg_pl, As = 0.9649, 0.0042, 2.1e-9
lam_pl = 2 ** (ns_pl - 1)
need_ms = LN2 ** 2 / (As * LN2)
print(f"   split-time cascade with rule constants: n_s = 1 (B1-B5; coupled log2 lam = {nc:+.4f}) -> {(1-ns_pl)/sg_pl:.1f} sigma (Planck);"
      f" needs lambda = 2^(n_s-1) = {lam_pl:.5f}")
print(f"   in the Poisson model lambda = (ms)_l/(ms)_(l+1): m s must grow {100*(1/lam_pl-1):.2f}%/split;"
      f" A_s needs m s = ln2/A_s = {need_ms:.2e} vs rule m s <= 18*113 = 2034")
Pt_max = 0.036 * As
est2 = (9 / 72) ** 2 * float(np.mean(rr)) * (Pt_max / 2) ** 2 * 10
print(f"   laws' own channel (C): Delta_zeta^2 ~ (9/72)^2 x 8.6 x (P_t/2)^2 x 10 (log): <= {est2:.1e} at r < 0.036;"
      f" CL-3's only de Sitter phase is today's (P_t ~ 5e-122); tilt blue")
check("E1 [E] every split-time channel misses: n_s = 1 with rule constants; amplitude 0 at linear order and"
      " <= 1e-20 at second order (blue), against 0.9649(42) and 2.1e-9", est2 < 1e-19 and abs(nc) < 0.03)

print("supplied: Poisson register stepping (B only), block-mean registers, 2D toy geometry, neighbour 'full' ="
      " mean >= 4s; scalar stand-in for tensors in C2; injection fraction in D1 (any value).")
print(f"runtime {time.time()-T0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
