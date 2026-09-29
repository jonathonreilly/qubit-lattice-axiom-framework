"""PR 9355 attack-f: NORMALIZATION of the drive amplitude D = 10^(-22/20) / (0.411 * 50 * |X_ge|) (GHz) against a time-domain pi pulse.

The note converts the source's 50 ns cosine-envelope pulse (pi-amplitude 0.411, spectroscopy 22 dB lower) into the Hamiltonian amplitude D with its own model's cavity-X transition matrix at f = 0.5035.
Which factors this hides:
  1. D_pi = 1/(50 |X_ge|) is the rotating-wave pi-pulse amplitude of a cos-drive D X cos(2 pi w t) with an envelope of mean 1/2 (Hann); checked by direct time-domain simulation in the note's own
     model (device levels from the charge-basis rotor with the two-arm second-harmonic potential, cavity Fock ladder, coupling G n P): excitation of the dressed |e~> from |g~> versus peak amplitude, for a Hann,
     a half-sine and a rectangular envelope of 50 ns, drive on the dressed g -> e frequency;
  2. the factor 10^(-22/20) / 0.411 between D and D_pi: -22 dB relative to the pi amplitude would give 10^(-22/20) D_pi, the formula gives 2.43 times that (-14.3 dB relative to the pi amplitude);
     what each reading gives for D in MHz and what a drive-squared scaling does to a shift.
The runner's own numbers are not used; the model parameters are the drive-reference snapshot of inputs.json.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import json, re, subprocess, sys, time
from pathlib import Path
import numpy as np
from scipy.linalg import expm

ROOT = Path.home() / ".probe-clones/probes-view" if "--scratch" in sys.argv else Path(__file__).resolve().parents[3]
PR = 9355
D = "data/driven_squid_resonator_2026_09_27"
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
    ent = git("ls-tree", HEAD, path).stdout.decode().split()
    if len(ent) < 4: raise SystemExit(f"{path} not in the PR head")
    return git("cat-file", "-p", ent[2]).stdout
INP = json.loads(blob(f"{D}/inputs.json")); MEAS = json.loads(blob(f"{D}/measurements.json"))

def device_h(EC, J, a_asym, f, EL, ng, N):
    n = np.arange(-N, N + 1, dtype=float); d = len(n)
    Jl, Jr = J * (1 + a_asym), J * (1 - a_asym)
    H = np.diag(4 * EC * (n - ng) ** 2).astype(complex)
    up1 = np.eye(d, k=-1); up2 = np.eye(d, k=-2)
    c1 = lambda ph: -(np.exp(1j * ph) * up1 + np.exp(-1j * ph) * up1.T) / 2
    c2 = lambda ph: (np.exp(1j * ph) * up2 + np.exp(-1j * ph) * up2.T) / 2
    H += Jl * c1(0.0) + Jr * c1(2 * np.pi * f)
    H += (Jl ** 2 * c2(0.0) + Jr ** 2 * c2(4 * np.pi * f)) / (4 * EL) * 1.0
    return H, np.diag(n)

T0 = time.time()
dr = INP["drive_reference"]; EC, J, aa = dr["params"]; ng = dr["ng"]; G = dr["G_GHz"]; Om = dr["Omega_GHz"]; EL = INP["EL_GHz"]; frab = INP["rabi_flux"]
Hd, nop = device_h(EC, J, aa, frab, EL, ng, 40)
ev, V = np.linalg.eigh(Hd); ND, K = 8, 5
Ed = ev[:ND] - ev[0]; nd = V[:, :ND].conj().T @ nop @ V[:, :ND]
a = np.diag(np.sqrt(np.arange(1, K)), 1); X = a + a.T; P = 1j * (a.T - a)
I_d, I_k = np.eye(ND), np.eye(K)
H0 = np.kron(np.diag(Ed), I_k) + Om * np.kron(I_d, np.diag(np.arange(K, dtype=float))) + G * np.kron(nd, P)
Xf = np.kron(I_d, X)
e, U = np.linalg.eigh(H0)
def label(dev, ph):
    b = np.zeros(ND * K); b[dev * K + ph] = 1; ov = np.abs(U.conj().T @ b) ** 2; i = int(np.argmax(ov)); return i, ov[i]
ig, wg = label(0, 0); ie, we = label(1, 0)
w_ge = e[ie] - e[ig]; Xge = abs(U[:, ie].conj() @ Xf @ U[:, ig])
print(f"drive-reference model at f = {frab}: dressed g -> e frequency {w_ge:.6f} GHz, |X_ge| = {Xge:.6f}, label weights {wg:.5f}, {we:.5f}")
Dpi_formula = 1 / (50 * Xge)
D_note = 10 ** (-22 / 20) / (INP["pi_amplitude"] * INP["pulse_ns"] * Xge)
D_alt = 10 ** (-22 / 20) / (INP["pulse_ns"] * Xge)
print(f"   D_pi = 1/(50|X_ge|) = {1e3*Dpi_formula:.4f} MHz; D of the note (10^(-22/20)/(0.411*50*|X_ge|)) = {1e3*D_note:.4f} MHz; if -22 dB were relative to the pi amplitude: {1e3*D_alt:.4f} MHz; ratio {D_note/D_alt:.4f}")
check("the note's D equals 10^(-22/20)/0.411 = 0.1932 times D_pi; a spectroscopy amplitude 22 dB below the pi amplitude would be 0.0794 times D_pi (a factor 2.433 smaller, 7.7 dB)",
      abs(D_note / Dpi_formula - 10 ** (-22 / 20) / 0.411) < 1e-12 and abs(D_note / D_alt - 1 / 0.411) < 1e-12, f"{D_note/Dpi_formula:.4f} vs {D_alt/Dpi_formula:.4f}")
print(f"   the note's D is {20*np.log10(D_note/Dpi_formula):.2f} dB relative to D_pi (the prose says 22 dB lower); a drive-squared quantity (any second-order shift) would change by {(D_note/D_alt)**2:.2f}x between the two readings")

# time-domain pulse
Tn, dt = 50.0, 0.02
tm = (np.arange(int(Tn / dt)) + 0.5) * dt
env = {"Hann (1-cos)/2": 0.5 * (1 - np.cos(2 * np.pi * tm / Tn)), "half sine": np.sin(np.pi * tm / Tn), "rectangular": np.ones_like(tm)}
Ue = U   # dressed basis
Xd = Ue.conj().T @ Xf @ Ue; Ed_ = e
def pulse(Dpk, envelope):
    psi = np.zeros(ND * K, complex); psi[ig] = 1.0       # in the dressed basis
    for k, t in enumerate(tm):
        Hm = np.diag(Ed_) + Dpk * envelope[k] * np.cos(2 * np.pi * w_ge * t) * Xd
        psi = expm(-2j * np.pi * Hm * dt) @ psi
    return abs(psi[ie]) ** 2
res = {}
for nm, en in env.items():
    area = en.mean()
    Dpk_rwa = 1 / (2 * Tn * Xge * area)          # rotating-wave pi-pulse peak amplitude for this envelope
    grid = Dpk_rwa * np.array([0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2])
    pe = np.array([pulse(d, en) for d in grid])
    i = int(pe.argmax())
    # parabola through the maximum for the best amplitude
    if 0 < i < len(grid) - 1:
        c = np.polyfit(grid[i - 1:i + 2], pe[i - 1:i + 2], 2); best = -c[1] / (2 * c[0])
    else: best = grid[i]
    res[nm] = (area, Dpk_rwa, best, pe.max())
    print(f"   {nm:16s}: mean envelope {area:.4f}; RWA pi amplitude {1e3*Dpk_rwa:.4f} MHz; simulated best {1e3*best:.4f} MHz (ratio {best/Dpk_rwa:.4f}); max excitation {pe.max():.4f}")
check("the rotating-wave pi-pulse amplitude 1/(2 T |X_ge| <envelope>) is confirmed by the full-model time-domain pulse to 5% for every envelope", all(abs(v[2] / v[1] - 1) < 0.05 and v[3] > 0.95 for v in res.values()), "; ".join(f"{k}: {v[2]/v[1]:.3f}" for k, v in res.items()))
hann = res["Hann (1-cos)/2"]
check("D_pi = 1/(50 |X_ge|) (the note's formula with the 0.411 divided out) is the pi-pulse peak amplitude of an envelope of mean 1/2 (Hann), and not of the half-sine (mean 2/pi) or a rectangular envelope",
      abs(hann[2] / Dpi_formula - 1) < 0.05 and abs(res["half sine"][2] / Dpi_formula - 1) > 0.2 and abs(res["rectangular"][2] / Dpi_formula - 1) > 0.4, f"simulated Hann {hann[2]/Dpi_formula:.3f}, half sine {res['half sine'][2]/Dpi_formula:.3f}, rectangular {res['rectangular'][2]/Dpi_formula:.3f} of D_pi")
print(f"NOTE: with a half-sine envelope (mean 2/pi) the pi amplitude would be {res['half sine'][2]/Dpi_formula:.3f} D_pi, so the 'cosine-envelope' reading matters at the {abs(res['half sine'][2]/Dpi_formula-1)*100:.0f}% level in D; the note lists pulse-area interpretation among its supplied assumptions.")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-f normalization on PR 9355: in the drive-reference model |X_ge| = {Xge:.4f}, D_pi = 1/(50|X_ge|) = {1e3*Dpi_formula:.3f} MHz is the pi amplitude of a Hann (mean-1/2) envelope (time-domain best {hann[2]/Dpi_formula:.3f} x), {res['half sine'][2]/Dpi_formula:.3f} x for a half-sine; the note's D = 10^(-22/20) D_pi / 0.411 is {20*np.log10(D_note/Dpi_formula):.1f} dB relative to D_pi (prose: 22 dB lower), i.e. {D_note/D_alt:.3f} x the D of a 22 dB-below-pi reading ({(D_note/D_alt)**2:.2f} x for any second-order shift); the note lists pulse-area interpretation as a supplied assumption; PASS={PASS} FAIL={FAIL}; no HIT")
sys.exit(1 if FAIL else 0)
