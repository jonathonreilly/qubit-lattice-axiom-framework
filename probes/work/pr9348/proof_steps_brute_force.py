"""PR 9348 attack-g: the note's exact operator identity and its calibration Jacobian, verified LITERALLY at small size.

Steps of the 'Conditional operator identity' section, as written:
  (i)   Gauss law on the oriented square gives E = (n, -n, -n, n), D = 4 n^2  (enumeration over integer link fields);
  (ii)  S = (1 + U) up to a phase for the two allowed assignments with the same final matter word and relative field shift U|n> = |n+1>, hence S*S = 2I + U + U*
        (checked as matrices on the cyclic charge ring of M = 3..41 sites, exactly, for the sum of the two path operators, and by expanding the two-path Gram matrix on random amplitudes);
  (iii) H_square = 4K n^2 - 2 delta (U + U*) - 4 delta I  =  4K n^2 - 2 delta S*S;
  (iv)  Fourier transformation on the circle sends U to exp(i phi): F H_square F^dagger + 4 delta I = 4K n^2 - 4 delta cos(phi) (phase-basis matrix built independently, M = 3..41),
        i.e. the zero-offset Cooper-pair-box Hamiltonian with EC = K and EJ = 4 delta; eigenvalues compared, and the nearest-neighbour matrix element equals -EJ/2;
  (v)   the local calibration Jacobian 'condition number about 7826' (drive of the four calibration coordinates by the four parameters, GHz coordinates), and in other units.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import hashlib, itertools, subprocess, sys, time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

ROOT = Path.home() / ".probe-clones/probes-view" if "--scratch" in sys.argv else Path(__file__).resolve().parents[3]
PR = 9348
PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True)
git("fetch", "origin", f"pull/{PR}/head", "--quiet")
HEAD = git("rev-parse", "FETCH_HEAD").stdout.decode().strip()
def blob(path):
    """file at the PR head via ls-tree + cat-file (rev:path is not used)"""
    ent = git("ls-tree", HEAD, path).stdout.decode().split()
    if len(ent) < 4: raise SystemExit(f"{path} not in the PR head")
    return git("cat-file", "-p", ent[2]).stdout

CAL = np.array([6.0391, 11.8680, 7.4613, 7.4587])                    # f01, f02, fres1, fres2 (GHz)
MEAS = {3: 17.457, 4: 22.778, 5: 27.794}
NOTE_ROOT = np.array([0.196567178810, 24.852181043101, 7.453936854591, 0.077763912291])
NOTE_DRIVE = {3: 5.181438, 4: 14.395723, 5: 28.257343}
NOTE_WIDTH = {3: 0.000368, 4: 0.008878, 5: 0.157861}

class Unassignable(Exception):
    pass

def endpoint(p, ng, N=12, K=8, ntr=None):
    """levels of the full charge x Fock Hamiltonian at offset charge ng (charges -N..N, photons 0..K-1); returns f01..f05, fres1, fres2 in GHz (dressed states labelled by dominant bare overlap) and the smallest label weight"""
    ec, ej, om, g = p
    n = np.arange(-N, N + 1, dtype=float); nq = len(n)
    hc = np.diag(4 * ec * (n - ng) ** 2) - 0.5 * ej * (np.eye(nq, k=1) + np.eye(nq, k=-1))
    _, bare = np.linalg.eigh(hc)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.kron(hc, np.eye(K)) + om * np.kron(np.eye(nq), np.diag(np.arange(K, dtype=float))) + g * np.kron(np.diag(n), a + a.T)
    e, v = np.linalg.eigh(h)
    labels = [(j, 0) for j in range(6)] + [(0, 1), (1, 1)]
    idx, wts = [], []
    for j, k in labels:
        b = np.kron(bare[:, j], np.eye(K)[:, k]); ov = np.abs(b @ v) ** 2
        i = int(np.argmax(ov)); idx.append(i); wts.append(ov[i])
    if len(set(idx)) != len(idx) or min(wts) < 0.5: raise Unassignable()
    lev = e[idx]
    return np.array([lev[j] - lev[0] for j in range(1, 6)] + [lev[6] - lev[0], lev[7] - lev[1]]), float(min(wts))
def predict(p, ngs=(0.0, 0.5), **kw):
    fs = [endpoint(p, ng, **kw) for ng in ngs]
    return np.mean([f for f, _ in fs], axis=0), min(w for _, w in fs)
CALIDX = [0, 1, 5, 6]
def resid_cal(z, target=CAL, ngs=(0.0, 0.5), **kw):
    try: f, _ = predict(np.exp(z), ngs, **kw)
    except Unassignable: return np.full(4, 1e3)
    return (f[CALIDX] - target) * 1000.0
def solve(start, target=CAL, ngs=(0.0, 0.5), **kw):
    r = least_squares(lambda z: resid_cal(z, target, ngs, **kw), np.log(start), xtol=1e-14, ftol=1e-14, gtol=1e-12, max_nfev=80)
    return np.exp(r.x), float(np.max(np.abs(r.fun)))
def drive_res(p, ngs=(0.0, 0.5), **kw):
    f, w = predict(p, ngs, **kw)
    return {j: 1000.0 * (f[j - 1] - MEAS[j]) / j for j in (3, 4, 5)}, f, w

T0 = time.time()
# (i) Gauss law
links = [(0, 1), (0, 3), (2, 1), (2, 3)]
sols = []
for E in itertools.product(range(-3, 4), repeat=4):
    div = [0] * 4
    for (a, b), e in zip(links, E): div[a] += e; div[b] -= e
    if not any(div): sols.append(E)
check("(i) Gauss law on the oriented square: integer solutions are (n, -n, -n, n) and D = 4 n^2", sols == [(n, -n, -n, n) for n in range(-3, 4)] and all(sum(e * e for e in E) == 4 * E[0] ** 2 for E in sols))
# (ii)-(iv)
rng = np.random.default_rng(90348)
worst_ss = worst_h = worst_spec = worst_off = worst_dg = 0.0
for M in range(3, 42, 2):
    m = (M - 1) // 2
    nn = np.arange(-m, m + 1).astype(float)
    U = np.roll(np.eye(M), 1, axis=0)             # U|n> = |n+1> (cyclic)
    I = np.eye(M)
    # two allowed assignments: path operators P1 = c1 * (I) and P2 = c2 * U  (same final matter word; the field shifts by 0 and by U): S = a I + b U with |a| = |b| = 1
    a, b = np.exp(1j * rng.uniform(0, 2 * np.pi, 2))
    S = a * I + b * U
    # S*S = 2I + conj(a) b U + a conj(b) U*  ; equals 2I + U + U* iff a conj(b) = 1, i.e. equal phases (the note: same final matter word)
    SS = S.conj().T @ S
    worst_ss = max(worst_ss, np.abs(((1 + 0j) * (I + U)).conj().T @ (I + U) - (2 * I + U + U.T)).max(), np.abs(SS - (2 * I + np.conj(a) * b * U + a * np.conj(b) * U.T)).max())
    K, dl = 0.37, 1.13
    Hs = 4 * K * np.diag(nn ** 2) - 2 * dl * (U + U.T) - 4 * dl * I
    worst_h = max(worst_h, np.abs(Hs - (4 * K * np.diag(nn ** 2) - 2 * dl * (I + U).conj().T @ (I + U))).max())   # (iii) H_square = 4K n^2 - 2 delta S*S
    # phase basis: F |n> -> exp(-i n phi_j)/sqrt(M), phi_j = 2 pi j / M ; charge n symmetric range
    j = np.arange(M)
    F = np.exp(-1j * np.outer(nn, 2 * np.pi * j / M)) / np.sqrt(M)      # rows: n, columns: phase points
    Fd = F.conj().T                                                       # phase <- charge
    # H in phase basis from the charge Hamiltonian, and independently: kinetic 4K n^2 via F, cos via diag
    Hp = Fd @ (Hs + 4 * dl * I) @ F
    Hcpb = Fd @ (4 * K * np.diag(nn ** 2)) @ F - 4 * dl * np.diag(np.cos(2 * np.pi * j / M))
    worst_off = max(worst_off, np.abs(Hp - Hcpb).max())
    e1 = np.linalg.eigvalsh(Hs + 4 * dl * I); e2 = np.linalg.eigvalsh(Hcpb)
    worst_spec = max(worst_spec, np.abs(e1 - e2).max())
    # U -> exp(i phi): F^dagger U F is diagonal with the phases
    D = Fd @ U @ F
    worst_dg = max(worst_dg, np.abs(D - np.diag(np.exp(1j * 2 * np.pi * j / M))).max())
check("(ii) with equal phases the two-path operator S = I + U has S*S = 2I + U + U* exactly on the cyclic charge ring (M = 3..41); unequal phases give conj(a) b U + a conj(b) U* instead", worst_ss < 1e-13, f"{worst_ss:.1e}")
check("(iii) H_square = 4K n^2 - 2 delta S*S with S = I + U (M = 3..41)", worst_h < 1e-12, f"{worst_h:.1e}")
check("(iv) F^dagger U F = diag(exp(+i phi_j)) and H_square + 4 delta I = 4K n^2 - 4 delta cos(phi) as phase-basis matrices (M = 3..41)", worst_off < 1e-10 and worst_dg < 1e-12, f"matrix difference {worst_off:.1e}, U -> exp(i phi) {worst_dg:.1e}")
check("the spectra of H_square + 4 delta I and of the Cooper-pair box 4 EC n^2 - EJ cos(phi) (EC = K, EJ = 4 delta) coincide (M = 3..41)", worst_spec < 1e-11, f"{worst_spec:.1e}")
# EJ = 4 delta and the nearest-neighbour element -EJ/2
K, dl = 0.37, 1.13
M = 21; nn = np.arange(-10, 11).astype(float); U = np.roll(np.eye(M), 1, axis=0)
Hs = 4 * K * np.diag(nn ** 2) - 2 * dl * (U + U.T) - 4 * dl * np.eye(M)
EJ = 4 * dl
check("the charge-basis nearest-neighbour element of H_square is -2 delta = -EJ/2 with EJ = 4 delta, and the diagonal is 4K n^2 - 4 delta", abs(Hs[11, 10] + EJ / 2) < 1e-14 and abs(Hs[10, 10] - (4 * K * 0 - 4 * dl)) < 1e-14, f"{Hs[11,10]:.4f} vs {-EJ/2:.4f}")
# unequal amplitudes (a != b in modulus): what S*S becomes
a_, b_ = 1.0, 0.8
SSu = np.abs(a_) ** 2 * np.eye(M) + np.abs(b_) ** 2 * np.eye(M) + a_ * b_ * (U + U.T)
print(f"   (for scale) unequal path weights |a|=1, |b|=0.8 give S*S = {a_**2 + b_**2:.2f} I + {a_*b_:.2f}(U + U*): the identity S*S = 2I + U + U* needs |a| = |b| = 1")
# (v) Jacobian
def F(p): return predict(p)[0][CALIDX]
def jac(f, x, h=1e-6):
    f0 = f(x); J = np.empty((len(f0), len(x)))
    for i in range(len(x)):
        d = h * abs(x[i]); xp = x.copy(); xm = x.copy(); xp[i] += d; xm[i] -= d; J[:, i] = (f(xp) - f(xm)) / (2 * d)
    return J
J = jac(F, NOTE_ROOT); sv = np.linalg.svd(J, compute_uv=False)
ul = np.log(NOTE_ROOT)
Jl = np.empty((4, 4))
for i in range(4):
    up = ul.copy(); um = ul.copy(); up[i] += 1e-6; um[i] -= 1e-6; Jl[:, i] = (F(np.exp(up)) - F(np.exp(um))) / 2e-6
svl = np.linalg.svd(Jl, compute_uv=False)
J2 = np.diag([1, 0.5, 1, 1]) @ J; sv2 = np.linalg.svd(J2, compute_uv=False)
check("(v) the calibration Jacobian condition number 'about 7826' in the stated units (parameters in GHz, coordinates in GHz or MHz): 7825.5 with the f02 total as coordinate", abs(sv[0] / sv[-1] - 7826) < 2, f"{sv[0]/sv[-1]:.1f}")
print(f"   other units: log-parameters {svl[0]/svl[-1]:.0f}; f02/2 (two-photon drive) coordinate {sv2[0]/sv2[-1]:.0f}; so the note's number depends on the coordinate convention, which it states ('stated coordinate units')")
# linearised half-widths of the parameters for the note's box [1, 2, 1, 1] MHz
box = np.array([1.0, 2.0, 1.0, 1.0]) * 1e-3
hw = np.abs(np.linalg.inv(J)) @ box
print(f"   linearised box half-widths of (EC, EJ, Omega, G): {np.round(hw, 6)} GHz")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-g proof steps on PR 9348: Gauss solutions (n,-n,-n,n), S*S=2I+U+U* on cyclic rings M=3..41 (needs equal-modulus paths), H_square+4 delta I = CPB(EC=K, EJ=4 delta) as phase-basis matrices and spectra to {worst_spec:.0e}, Jacobian condition {sv[0]/sv[-1]:.0f} (note 7826; {svl[0]/svl[-1]:.0f} in log-parameters, {sv2[0]/sv2[-1]:.0f} with the f02/2 coordinate); PASS={PASS} FAIL={FAIL}; no defect in the note's operator steps")
sys.exit(1 if FAIL else 0)
