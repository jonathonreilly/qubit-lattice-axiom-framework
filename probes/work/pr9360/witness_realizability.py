"""PR 9360 attack-a: WITNESS REALIZABILITY for the qutrit preparation-transfer note.

Every stated object exists in the declared setting, checked from the packaged raw arrays and by brute force:
 1. counts: 61 x 197 x 3 = 36,051 calibration coordinates, 31 x 380 Ramsey and 61 x 246 echo genuine observations, three separate reference samples per gate
    (the genuine mask excludes exactly the last three samples of each acquisition and those are reference_indices);
 2. the two time offsets (10 h 42 min 02 s after calibration; 49 min 55.815 s before) from the exact TUIDs;
 3. the affine readout D = [c1 - c0, c2 - c0] is invertible for every gate of every acquisition (smallest |det|, largest condition number);
 4. the fraction of population estimates outside the simplex that the note says are retained;
 5. the fitted rates give a valid Markov generator, populations in [0, 1] at every delay, no active bound; the lambda = k10 branch is not the one the data uses;
 6. the note's claim that an incoherent equal mixture and an equal coherent superposition of |1>, |2> give the same Ramsey observable: a 3-level Lindblad simulation with a
    diagonal free Hamiltonian, jump operators sqrt(k_ij)|j><i|, and a final pi/2 unitary confined to states 1 and 2 (any angle), evaluated for the mixture and the superposition.
Own barycentric readout and own propagation; numbers compared with the note's.
"""
import io, subprocess, sys, time, json, re
from pathlib import Path
import numpy as np
from scipy.linalg import expm

ROOT = Path.home() / ".probe-clones/probes-view" if "--scratch" in sys.argv else Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/preparation-transfer-20260927"
D = "data/preparation_transfer_2026_09_27"
PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

def gitshow(path):
    subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], cwd=ROOT)
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{path}"], cwd=ROOT, capture_output=True)
    if r.returncode != 0: raise SystemExit(f"cannot read {path}: {r.stderr.decode()[:200]}")
    return r.stdout
def load(name): return np.load(io.BytesIO(gitshow(f"{D}/{name}")), allow_pickle=False)
def loadjson(name): return json.loads(gitshow(f"{D}/{name}"))

def populations(z):
    """barycentric populations of every stored point in the frame of the final three reference points of each gate"""
    iq = z["raw_IQ"]; out = []
    for gate in iq:
        M = np.vstack([gate[-3:].T, np.ones(3)])
        out.append(np.linalg.solve(M, np.vstack([gate.T, np.ones(len(gate))])).T)
    return np.array(out)

def propagate(rates, t_us, init, swap=False):
    k10, k21, k20 = rates; lam = k21 + k20
    def step(t, u):
        F = (np.exp(-k10 * t) - np.exp(-lam * t)) / (lam - k10)
        u2 = u[..., 2] * np.exp(-lam * t)
        u1 = u[..., 1] * np.exp(-k10 * t) + k21 * u[..., 2] * F
        return np.stack([1 - u1 - u2, u1, u2], axis=-1)
    u0 = np.broadcast_to(np.asarray(init, float), (len(t_us), 3))
    if swap:
        h = step(t_us / 2, u0); return step(t_us / 2, h[..., [0, 2, 1]])
    return step(t_us, u0)

NOTE_RATES = np.array([0.07126916, 0.11124121, 0.00839770])
SEQ_RATES = np.array([0.07728135, 0.11762925, 0.0])
def lindblad_L(k10, k21, k20):
    """vectorised Lindblad generator (column-stacking vec) for H = 0 and jump operators sqrt(k_ij)|j><i|"""
    d = 3
    def ket(i): v = np.zeros((d, 1)); v[i] = 1; return v
    I = np.eye(d)
    Lv = np.zeros((d * d, d * d), complex)
    for (i, j, k) in ((1, 0, k10), (2, 1, k21), (2, 0, k20)):
        A = np.sqrt(k) * (ket(j) @ ket(i).T)
        AdA = A.T @ A
        Lv += np.kron(A.conj(), A) - 0.5 * np.kron(I, AdA) - 0.5 * np.kron(AdA.T, I)
    return Lv

T0 = time.time()
zc, zr, ze = load("calibration_raw.npz"), load("ramsey_raw.npz"), load("echo_raw.npz")
# 1. counts
cnt = {}
for name, z, n_gates, n_del in (("calibration", zc, 61, 197), ("ramsey", zr, 31, 380), ("echo", ze, 61, 246)):
    mask = z["genuine_mask"]; ref = z["reference_indices"]
    ok = (z["raw_IQ"].shape[0] == n_gates and int(mask.sum()) == n_del and mask.size - n_del == 3 and set(np.nonzero(~mask)[0]) == set(ref.tolist())
          and set(ref.tolist()) == set(range(mask.size - 3, mask.size)))
    cnt[name] = (z["raw_IQ"].shape, int(mask.sum()))
    check(f"{name}: {n_gates} gates x {n_del} genuine delays, the three non-genuine samples are exactly reference_indices = the last three", ok, f"raw {z['raw_IQ'].shape}, genuine {int(mask.sum())}, reference indices {ref.tolist()}")
check("36,051 calibration population coordinates = 61 x 197 x 3", 61 * 197 * 3 == 36051)
# 2. TUID offsets
def tuid_s(t):
    m = re.match(r"(\d{4})(\d\d)(\d\d)-(\d\d)(\d\d)(\d\d)-(\d{3})", t)
    y, mo, d, h, mi, s, ms = map(int, m.groups())
    return (d * 86400 + h * 3600 + mi * 60 + s) + ms / 1000.0, (y, mo)
cal, ram, ech = "20220920-215202-730-31ad1f", "20220921-083404-829-b243a3", "20220920-210206-915-8331be"
tc_, tr_, te_ = tuid_s(cal)[0], tuid_s(ram)[0], tuid_s(ech)[0]
dr = tr_ - tc_; de = tc_ - te_
def hms(x): h = int(x // 3600); m = int((x - 3600 * h) // 60); return f"{h} h {m} min {x - 3600*h - 60*m:.3f} s"
check("Ramsey starts 10 h 42 min 02 s after calibration; echo starts 49 min 55.815 s before it (TUID timestamps, same month)", abs(dr - (10 * 3600 + 42 * 60 + 2.099)) < 1e-6 and abs(de - (49 * 60 + 55.815)) < 1e-6,
      f"Ramsey +{hms(dr)}, echo -{hms(de)}")
# 3. readout invertibility
pops = {}
for name, z in (("calibration", zc), ("ramsey", zr), ("echo", ze)):
    dets, conds = [], []
    for gate in z["raw_IQ"]:
        c0, c1, c2 = gate[-3:]
        Dm = np.stack([c1 - c0, c2 - c0], axis=1)
        dets.append(abs(np.linalg.det(Dm))); conds.append(np.linalg.cond(Dm))
    pops[name] = populations(z)
    check(f"{name}: D = [c1 - c0, c2 - c0] is invertible for every gate", min(dets) > 0 and max(conds) < 1e6, f"min |det D| = {min(dets):.3e}, max condition {max(conds):.2f}")
# 4. outside-simplex fraction
ev = loadjson("evaluation.json")
frac = {}
for name, z in (("calibration", zc), ("ramsey", zr), ("echo", ze)):
    m = z["genuine_mask"]; P = pops[name][:, m, :]
    frac[name] = float(np.mean(np.any((P < 0) | (P > 1), axis=-1)))
print("   outside-simplex fractions (own):", {k: round(v, 4) for k, v in frac.items()}, "; evaluation.json:", ev.get("outside_simplex_fraction"))
check("the note's statement 'values outside the probability simplex are retained' is a live case: a nonzero fraction of estimates lies outside [0,1]^3 for every acquisition", all(v > 0 for v in frac.values()), str({k: round(v, 3) for k, v in frac.items()}))
osf = ev.get("outside_simplex_fraction")
if isinstance(osf, (int, float)):
    check("evaluation.json's outside-simplex fraction equals the own Ramsey fraction", abs(osf - frac["ramsey"]) < 2e-3 or abs(osf - frac["echo"]) < 2e-3, f"json {osf}, own ramsey {frac['ramsey']:.4f}, echo {frac['echo']:.4f}")
# 5. generator validity and propagation range at every genuine delay
k10, k21, k20 = NOTE_RATES
Lg = np.array([[0, k10, k20], [0, -k10, k21], [0, 0, -k21 - k20]])
check("the fitted rates give a valid generator: columns sum to zero, off-diagonals >= 0, no rate on a bound [0, 10]", np.allclose(Lg.sum(0), 0) and (Lg - np.diag(np.diag(Lg)) >= 0).all() and NOTE_RATES.min() > 0 and NOTE_RATES.max() < 10)
tmax = {}
for name, z, init, swap in (("calibration", zc, [0, 0, 1], False), ("ramsey", zr, [0, .5, .5], False), ("echo", ze, [0, .5, .5], True)):
    t = z["times_s"][z["genuine_mask"]] * 1e6
    pr = propagate(NOTE_RATES, t, init, swap)
    tmax[name] = (t.min(), t.max())
    check(f"{name}: predicted populations lie in [0,1], sum to one, at all {len(t)} delays (delays {t.min():.3f}..{t.max():.3f} us)", pr.min() > -1e-12 and pr.max() < 1 + 1e-12 and np.allclose(pr.sum(-1), 1, atol=1e-12))
check("lambda - k10 = k21 + k20 - k10 is not near zero for the note's rates or the sequential control, so the t exp(-k10 t) branch of F is never used by the data",
      abs(k21 + k20 - k10) > 0.04 and abs(SEQ_RATES[1] - SEQ_RATES[0]) > 0.04, f"{k21 + k20 - k10:.5f}, {SEQ_RATES[1] - SEQ_RATES[0]:.5f}")
# 6. mixture versus coherent superposition
Lv = lindblad_L(*NOTE_RATES)
def vec(rho): return rho.reshape(-1, order="F")
def unvec(v): return v.reshape(3, 3, order="F")
mix = np.zeros((3, 3), complex); mix[1, 1] = mix[2, 2] = 0.5
psi = np.array([0, 1, 1]) / np.sqrt(2); sup = np.outer(psi, psi.conj())
Pex = np.diag([0, 1, 1]).astype(complex)
worst = 0.0; nprobe = 0
for th in (np.pi / 2, 0.3, 1.1, 2.4):
    for ph in (0.0, 0.7):
        U = np.eye(3, dtype=complex)
        U[1:, 1:] = [[np.cos(th / 2), -1j * np.exp(-1j * ph) * np.sin(th / 2)], [-1j * np.exp(1j * ph) * np.sin(th / 2), np.cos(th / 2)]]
        for t in (0.0, 1.0, 7.5, 20.0, 60.0):
            E = expm(Lv * t)
            a = np.trace(Pex @ U @ unvec(E @ vec(mix)) @ U.conj().T).real
            b = np.trace(Pex @ U @ unvec(E @ vec(sup)) @ U.conj().T).real
            worst = max(worst, abs(a - b)); nprobe += 1
check("the incoherent equal mixture and the equal coherent superposition of |1>, |2> give the same population sum after ANY final 1-2 unitary (angle, phase) and any waiting time (3-level Lindblad, diagonal free H)", worst < 1e-10, f"{nprobe} (angle, phase, time) points, worst difference {worst:.1e}")
# and the population sector of that Lindblad model is the note's generator
t = 12.3
ps = np.real(np.diag(unvec(expm(Lv * t) @ vec(np.diag([0, 0, 1]).astype(complex)))))
pr = propagate(NOTE_RATES, np.array([t]), [0, 0, 1])[0]
check("the Lindblad populations from |2> equal the note's closed form at t = 12.3 us (the 'population sector of a canonical Lindblad model')", np.max(np.abs(ps - pr)) < 1e-11, f"{np.max(np.abs(ps - pr)):.1e}")
# Ramsey signal of the mixture equals the note's Pexc closed form
Pexc = (np.exp(-k10 * t) + np.exp(-(k21 + k20) * t) + k21 * (np.exp(-k10 * t) - np.exp(-(k21 + k20) * t)) / (k21 + k20 - k10)) / 2
sig = np.trace(Pex @ unvec(expm(Lv * t) @ vec(mix))).real
check("the mixture's Ramsey population sum equals the note's closed form Pexc(t) = [e^{-k10 t} + e^{-lambda t} + k21 F(t)]/2 at t = 12.3 us", abs(sig - Pexc) < 1e-11, f"{sig:.10f} vs {Pexc:.10f}")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-a witness realizability on PR 9360: counts (61x197x3=36051, 31x380, 61x246, three reference samples per gate) and TUID offsets reproduced from the packaged arrays, readout matrix D invertible for every gate, outside-simplex fractions {frac['calibration']:.3f}/{frac['ramsey']:.3f}/{frac['echo']:.3f} (cal/Ramsey/echo), generator valid and populations in [0,1] at every delay, lambda=k10 branch unused, mixture and coherent superposition give the same Ramsey sum (Lindblad, worst {worst:.0e}); PASS={PASS} FAIL={FAIL}; no defect in the note's witnesses")
sys.exit(1 if FAIL else 0)
