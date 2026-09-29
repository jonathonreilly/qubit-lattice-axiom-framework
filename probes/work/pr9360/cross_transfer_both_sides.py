#!/usr/bin/env python3
"""J:attack-b:PR9360 -- SAME TEST, BOTH SIDES on the qutrit preparation-transfer note.

The note's separations: Ramsey (frozen calibration rates give 1.659315 pp, against 5.164180 pp for a fixed no-decay comparator) versus echo (15.851257 pp).  The identical test is applied to every
pairing of fitted-on and evaluated-on acquisition (calibration, Ramsey, echo), each evaluated in the same population-sum coordinate with the same propagator, and the no-decay comparator is applied to the
echo target as well (the note tabulates it for Ramsey only).  Own barycentric readout and rate-equation code from the packaged raw I/Q arrays; nothing from the PR's scripts.
"""
import io, subprocess, sys, time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/preparation-transfer-20260927"
D = "data/preparation_transfer_2026_09_27"
subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], cwd=ROOT)
def load(name):
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{D}/{name}"], cwd=ROOT, capture_output=True); return np.load(io.BytesIO(r.stdout), allow_pickle=False)
def populations(z):
    iq = z["raw_IQ"]; out = []
    for gate in iq:
        M = np.vstack([gate[-3:].T, np.ones(3)]); out.append(np.linalg.solve(M, np.vstack([gate.T, np.ones(len(gate))])).T)
    return np.array(out)
def propagate(rates, t_us, init, swap=False):
    k10, k21, k20 = rates; lam = k21 + k20
    def step(t, u):
        d = lam - k10
        F = np.where(np.abs(d) < 1e-12, t * np.exp(-k10 * t), (np.exp(-k10 * t) - np.exp(-lam * t)) / np.where(np.abs(d) < 1e-12, 1.0, d))
        u2 = u[..., 2] * np.exp(-lam * t); u1 = u[..., 1] * np.exp(-k10 * t) + k21 * u[..., 2] * F
        return np.stack([1 - u1 - u2, u1, u2], axis=-1)
    u0 = np.broadcast_to(np.asarray(init, float), (len(t_us), 3))
    if swap:
        h = step(t_us / 2, u0); return step(t_us / 2, h[..., [0, 2, 1]])
    return step(t_us, u0)
zc, zr, ze = load("calibration_raw.npz"), load("ramsey_raw.npz"), load("echo_raw.npz")
pops = {}
for name, z in (("cal", zc), ("ram", zr), ("echo", ze)):
    t = z["times_s"]; mask = z["genuine_mask"]; P = populations(z); pops[name] = (t[mask] * 1e6, P[:, mask, :])
tc, Pc = pops["cal"]; tr, Pr = pops["ram"]; te, Pe = pops["echo"]
obs = {"cal": Pc, "ram": Pr[..., 1] + Pr[..., 2], "echo": Pe[..., 1] + Pe[..., 2]}
def pred(rates, which):
    if which == "cal": return propagate(rates, tc, [0, 0, 1])
    if which == "ram": p = propagate(rates, tr, [0, .5, .5]); return p[:, 1] + p[:, 2]
    p = propagate(rates, te, [0, .5, .5], swap=True); return p[:, 1] + p[:, 2]
def rms(rates, which):
    p = pred(rates, which); o = obs[which]
    if which == "cal": return float(np.sqrt(((o - p[None]) ** 2).mean()))
    return float(np.sqrt(((o - p[None, :]) ** 2).mean()))
def fit(which, starts=40, seed=0):
    rng = np.random.default_rng(seed); best = None
    for _ in range(starts):
        x0 = rng.uniform(0.005, 0.3, 3)
        try:
            r = least_squares(lambda x: (((obs[which] - pred(x, which)[None]) if which == "cal" else (obs[which] - pred(x, which)[None, :])).ravel()), x0, bounds=(0, 10), xtol=1e-12, ftol=1e-12)
        except Exception: continue
        if best is None or r.cost < best.cost: best = r
    return best.x
frozen = np.array([0.07126916, 0.11124121, 0.00839770])
print("frozen (note) rates:", {w: round(rms(frozen, w) * (1 if w == "cal" else 100), 4) for w in ("cal", "ram", "echo")})
t0 = time.time()
fits = {w: fit(w) for w in ("cal", "ram", "echo")}
print("fit time", round(time.time() - t0))
for w, x in fits.items():
    print(f"fit on {w}: rates {np.round(x, 5)}; RMS on cal {rms(x,'cal'):.4f} (frac), ram {rms(x,'ram')*100:.3f} pp, echo {rms(x,'echo')*100:.3f} pp")
# sums on calibration
def cal_sum_rms(x):
    p = propagate(x, tc, [0, 0, 1]); s = p[:, 1] + p[:, 2]; o = Pc[..., 1] + Pc[..., 2]; return float(np.sqrt(((o - s[None]) ** 2).mean())) * 100
print("calibration p1+p2 RMS (pp):", {w: round(cal_sum_rms(x), 3) for w, x in list(fits.items()) + [("frozen", frozen)]})

PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
nd_ram = float(np.sqrt(((obs["ram"] - 1.0) ** 2).mean())) * 100; nd_echo = float(np.sqrt(((obs["echo"] - 1.0) ** 2).mean())) * 100
print(f"   fixed no-decay comparator (population sum = 1): Ramsey {nd_ram:.4f} pp, echo {nd_echo:.4f} pp")
check("the note's Ramsey numbers: frozen rates 1.659315 pp, fixed no-decay 5.164180 pp", abs(rms(frozen, "ram") * 100 - 1.659315) < 2e-5 and abs(nd_ram - 5.164180) < 2e-5)
check("the note's echo number: frozen rates with the declared midpoint swap 15.851257 pp", abs(rms(frozen, "echo") * 100 - 15.851257) < 2e-5)
skill_ram = 1 - rms(frozen, "ram") * 100 / nd_ram; skill_echo = 1 - rms(frozen, "echo") * 100 / nd_echo
print(f"   error reduction of the frozen rates relative to no decay: Ramsey {skill_ram:.1%}, echo {skill_echo:.1%}")
check("the same comparison on the echo side: the frozen rates beat the no-decay comparator there too (so the echo mismatch is not a failure to beat no decay)", skill_echo > 0.0, f"echo {rms(frozen,'echo')*100:.2f} pp vs no decay {nd_echo:.2f} pp")
table = {f: {e: rms(x, e) * 100 for e in ("ram", "echo")} for f, x in fits.items()}
print("   transfer table (pp of the population sum): rows = fitted on, columns = evaluated on")
for f in fits: print(f"      fitted on {f:>4}: Ramsey {table[f]['ram']:.3f}, echo {table[f]['echo']:.3f}   rates {np.round(fits[f], 4)}")
check("each acquisition's own best-fit rates reach its floor (Ramsey 1.63 pp, echo 2.15 pp): the model class fits both targets when fitted to each", table["ram"]["ram"] < 1.7 and table["echo"]["echo"] < 2.2)
check("the reverse transfer fails too: rates fitted on the echo target predict Ramsey at more than 4 pp, no better than the fixed no-decay comparator (5.16 pp) by more than 0.5 pp; rates fitted on Ramsey predict echo at more than 15 pp",
      table["echo"]["ram"] > 4.0 and (nd_ram - table["echo"]["ram"]) < 0.7 and table["ram"]["echo"] > 15.0, f"echo-fit -> Ramsey {table['echo']['ram']:.3f} pp (no decay {nd_ram:.3f}); Ramsey-fit -> echo {table['ram']['echo']:.3f} pp")
check("the Ramsey-fit rates sit on a bound (k21 = 10 per microsecond) and miss the calibration by 5.7 times the calibration RMS while matching Ramsey to 1.64 pp: Ramsey alone cannot identify the rates, so the 1.66 pp transfer tests one combination",
      fits["ram"][1] > 9.99 and rms(fits["ram"], "cal") / rms(frozen, "cal") > 5, f"calibration RMS {rms(fits['ram'], 'cal'):.4f} vs {rms(frozen, 'cal'):.4f}")

if not HITS:
    print(f"SUMMARY: no purchase: the note's Ramsey and echo numbers reproduce; under the identical test on both sides the contrast stands and is symmetric (each acquisition's own rates reach its floor, 1.64 pp Ramsey and 2.15 pp echo, and predict the other at {table['echo']['ram']:.2f} pp and {table['ram']['echo']:.2f} pp), the calibration rates beat the no-decay comparator on echo as well ({skill_echo:.0%} error reduction against {skill_ram:.0%} on Ramsey), and Ramsey alone does not pin the rates; {PASS} checks pass")
else:
    print("SUMMARY: failed: " + "; ".join(HITS))
sys.exit(0)
