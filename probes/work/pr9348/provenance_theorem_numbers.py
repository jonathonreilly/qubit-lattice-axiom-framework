#!/usr/bin/env python3
"""J:provenance:PR9348 -- every number in the theorem statements of the transmon calibration holdout note, located in the runner's cached stdout, the runner/helper source, the pinned data
file, or an exact derivation re-executed here.

Statement text = the opening paragraph (the three drive residuals) + "Conditional operator identity and its obligations" + "Source, calibration and evaluation" + "Numerical checks and declared
sensitivity scenarios" (markdown link targets and hash literals removed first; the hashes are checked separately).  Every numeric token (integers, decimals, a/b, number words) must fall inside one item:
  CACHE       printed by the PR's cached runner output (logs/runner-cache/transmon_calibration_holdout_2026_09_26.txt at the PR head), re-parsed here          -> sourced
  RUNNER      a constant of the runner or of its model helper at the PR head                                                                                   -> sourced
  DATA        a value of the pinned external file scripts/data/transmon_holdout_2026_09_26/Experiment.csv (KIT row) at the PR head, or of its provenance.json  -> sourced
  DERIVED     an exact derivation re-executed here (sympy / exact matrices), or a value recomputed here from the model                                        -> sourced (flagged)
  PARENT      a number the note takes from the parent notes; INFO when the parent's cache or text prints it, otherwise derived here from the parent's printed numbers
  (else)      HIT: no runner line, no cache line, no derivation.
Tokens covered by no item are printed as UNCOVERED and counted as HIT. Numbers in "Imports and scientific meaning" (the 455 MHz anharmonicity of an earlier comparison) are outside the
theorem statements and are reported as INFO. Self-contained; reads the PR head via git.
"""
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.linalg import eigh

ROOT = Path(__file__).resolve().parents[3]
PR = 9348
BRANCH = "physics-loop/transmon-holdout-20260926"
NOTE = "docs/TRANSMON_CALIBRATION_HOLDOUT_BOUNDED_THEOREM_NOTE_2026-09-26.md"
RUNNER = "scripts/transmon_calibration_holdout_2026_09_26.py"
MODEL = "scripts/transmon_resonator_model_2026_09_26.py"
DIRECT = "scripts/transmon_direct_charge_check_2026_09_26.py"
CACHE = "logs/runner-cache/transmon_calibration_holdout_2026_09_26.txt"
CSVF = "scripts/data/transmon_holdout_2026_09_26/Experiment.csv"
PROV = "scripts/data/transmon_holdout_2026_09_26/provenance.json"
PARENT1 = "docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md"
PARENT2 = "docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md"
PARENT2_CACHE = "logs/runner-cache/local_compensation_common_field_record_limit_2026_09_24.txt"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def head():
    git("fetch", "origin", BRANCH, "--quiet")
    r = git("rev-parse", f"origin/{BRANCH}")
    if r.returncode != 0:
        raise SystemExit("cannot resolve the PR branch: " + r.stderr.strip())
    return r.stdout.strip()


HEAD = head()


def show(path, ref=None):
    r = git("show", f"{ref or HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path} at {ref or HEAD}: {r.stderr.strip()}")
    return r.stdout


def show_bytes(path):
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True)
    return r.stdout


def norm(t):
    for a, b in (("−", "-"), ("≥", ">="), ("≤", "<="), ("·", "*"), ("²", "^2"), ("κ", "kappa"), ("δ", "delta")):
        t = t.replace(a, b)
    return t


def statement_pieces(note):
    secs = {s.split("\n", 1)[0].strip(): s for s in re.split(r"^#+ ", note, flags=re.M)[1:]}
    names = ["Calibrated transmon predictions for three unused KIT transitions", "Conditional operator identity and its obligations",
             "Source, calibration and evaluation", "Numerical checks and declared sensitivity scenarios"]
    out = []
    for n in names:
        t = secs[n].split("\n", 1)[1]
        t = re.sub(r"\]\((?:[^)]*)\)", "]", t)                                   # markdown link targets
        t = re.sub(r"https?://\S+", "URL", t)
        t = re.sub(r"`[0-9a-f]{20,}`", "HASH", t)
        t = re.sub(r"(?<=[a-z]{3})(?=\d+e-\d|\d{3,})", " ", norm(re.sub(r"\s+", " ", t)))
        out.append((n.split(" and ")[0][:28], t))
    return out


NUM = re.compile(r"(?<![A-Za-z_\^\d./])(\d+e-\d+|\d+/\d+|[+-]?\d+\.\d+|\d+)(?![\d])")
WORDS = re.compile(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|twelve|sixteen|twenty-one|twenty-four|twenty|four-photon|first|second)\b", re.I)


def tokens(text):
    return [(m.start(), m.end(), m.group(1)) for m in NUM.finditer(text)] + [(m.start(), m.end(), m.group(1)) for m in WORDS.finditer(text)]


# ------------------------------------------------------------------------------------------------ cache
def load_cache():
    raw = show(CACHE)
    body = raw.split("----- stdout -----\n", 1)[1]
    js = body.split("\nper_element", 1)[0]
    return json.loads(js), body.splitlines()


def cache_line(lines, needle):
    for i, l in enumerate(lines):
        if needle in l:
            return i + 1
    return None


# ------------------------------------------------------------------------------------------------ derivations
def derive_identity():
    """E = (n, -n, -n, n), D = sum E^2 = 4 n^2; the two-hop channel S = F_2 F_0 (unsigned rotor limit, hard core) has two paths with final field labels m = n - 1 and m = n, so
    S^T S = 2 I + U + U^T; H_square = 4 K n^2 - 2 delta S^T S = 4 K n^2 - 2 delta (U + U^T) - 4 delta I, and U -> exp(i phi) gives 4 EC n^2 - EJ cos(phi) with EC = K, EJ = 4 delta."""
    n, K, dl, phi = sp.symbols("n K delta phi")
    okD = sp.expand(sum(e ** 2 for e in (n, -n, -n, n)) - 4 * n ** 2) == 0
    M = 12
    ns = list(range(-M, M + 1)); ms = list(range(-M - 1, M + 1))
    Smat = np.zeros((len(ms), len(ns)))
    for j, nn in enumerate(ns):
        # the two hard-core paths: (0->1, 2->3): m = n - 1 ; (0->3, 2->1): m = n
        for mm in (nn - 1, nn):
            Smat[ms.index(mm), j] += 1
    SS = Smat.T @ Smat
    U = np.eye(len(ns), k=-1)
    bulk = slice(1, -1)
    okS = np.allclose((SS - (2 * np.eye(len(ns)) + U + U.T))[bulk, bulk], 0)
    Hsq = sp.simplify(4 * K * n ** 2 - 2 * dl * (2 + 2 * sp.cos(phi)) - (4 * K * n ** 2 - 4 * dl * sp.cos(phi) - 4 * dl))
    okH = Hsq == 0
    return okD and okS and okH, ("E = (n,-n,-n,n) gives D = 4n^2 (sympy); the two hard-core two-hop paths of F_2 F_0 end at field labels m = n-1 and m = n, so S^T S = 2I + U + U^T (matrix check on 25 states); "
                                 "4Kn^2 - 2 delta S^T S = 4Kn^2 - 2 delta(U+U^T) - 4 delta I and U -> e^(i phi) gives 4Kn^2 - 4 delta cos(phi) - 4 delta = 4 EC n^2 - EJ cos(phi) - 4 delta with EC = K, EJ = 4 delta (sympy)")


def recompute_cutoffs(p):
    """Primary construction (transmon subspace truncated to M levels) and the larger bases, recomputed here from the model definition; returns the largest |shift| of f03..f05 in MHz."""
    def endpoint(ng, N, M, Kp):
        ec, ej, om, g = p
        n = np.arange(-N, N + 1, dtype=float)
        hc = np.diag(4 * ec * (n - ng) ** 2) - 0.5 * ej * (np.eye(len(n), k=1) + np.eye(len(n), k=-1))
        e, v = np.linalg.eigh(hc); e = e[:M] - e[0]; v = v[:, :M]
        charge = v.T @ (n[:, None] * v)
        osc = np.diag(np.sqrt(np.arange(1, Kp)), 1)
        h = np.diag((om * np.arange(Kp)[:, None] + e[None, :]).ravel()) + g * np.kron(osc + osc.T, charge)
        w, V = np.linalg.eigh(h)
        tg = [(0, j) for j in range(7)] + [(1, 0), (1, 1)]
        ix = [int(np.argmax(np.abs(V[k * M + j, :]) ** 2)) for k, j in tg]
        lev = {t: w[i] for t, i in zip(tg, ix)}
        return np.array([lev[0, j] - lev[0, 0] for j in range(1, 7)] + [lev[1, 0] - lev[0, 0], lev[1, 1] - lev[0, 1]])

    def pred(N, M, Kp):
        return (endpoint(0.0, N, M, Kp) + endpoint(0.5, N, M, Kp)) / 2
    base = pred(14, 12, 9)
    out = []
    for dims in ((30, 12, 9), (30, 20, 9), (30, 20, 16), (40, 24, 20)):
        d = np.abs(pred(*dims) - base) * 1000
        out.append((dims, float(d[2:5].max()), float(d.max())))
    return base, out


def main():
    note = show(NOTE)
    C, clines = load_cache()
    runner = show(RUNNER); model = show(MODEL)
    csv_bytes = show_bytes(CSVF)
    prov = json.loads(show(PROV))
    pieces = statement_pieces(note)
    covered = {name: set() for name, _ in pieces}
    print(f"PR #{PR} head {HEAD[:10]}; cache {len(clines)} stdout lines; statement pieces: {', '.join(n for n, _ in pieces)}")
    out = {"CACHE": 0, "RUNNER": 0, "DATA": 0, "DERIVED": 0, "PARENT": 0, "EXCLUDED": 0, "HIT": 0}
    hits = []

    def cover(pat):
        c = 0
        for name, text in pieces:
            for m in re.finditer(pat, text, flags=re.I):
                covered[name].update(range(m.start(), m.end())); c += 1
        return c

    def item(iid, pat, kind, ok, source):
        if cover(pat) == 0:
            print(f"[UNUSED] {iid}: pattern not found in the statement text")
            return
        if ok:
            out[kind] += 1
            print(f"[{kind}] {iid} | {source}")
        else:
            out["HIT"] += 1
            hits.append(f"HIT: {iid} | {source}")

    ev = {e["transition"]: e for e in C["evaluation"]}
    r5 = lambda x: f"{x:.5f}"
    # opening paragraph and table: drive residuals, totals
    drv = [ev[k]["residual_drive_MHz"] for k in ("f03", "f04", "f05")]
    item("drive residuals (opening paragraph)", r"\+5\.18144, \+14\.39572 and \+28\.25734", "CACHE", [r5(x) for x in drv] == ["5.18144", "14.39572", "28.25734"],
         f"cache evaluation[].residual_drive_MHz = {drv} (line {cache_line(clines, 'residual_drive_MHz')})")
    row = {}
    for k in ("f03", "f04", "f05"):
        row[k] = (ev[k]["measured_GHz"], ev[k]["predicted_GHz"], ev[k]["residual_total_MHz"], ev[k]["residual_drive_MHz"])
    okt = True; tt = []
    for k, (m, pr_, rt, rd) in row.items():
        tab = re.search(rf"\| {k} \| ([0-9.]+) \| ([0-9.]+) \| ([+0-9.]+) \| ([+0-9.]+) \|", pieces[2][1])
        good = tab is not None and Fr(tab.group(1)) == Fr(str(m)) and f"{pr_:.9f}" == tab.group(2) and f"{rt:+.6f}" == tab.group(3) and f"{rd:+.6f}" == tab.group(4)
        okt &= good; tt.append(f"{k}: measured {m}, predicted {pr_:.9f}, total {rt:+.6f}, drive {rd:+.6f} {'= table' if good else 'DIFFERS from the table'}")
    item("evaluation table", r"\| f0[345] \| [0-9.]+ \| [0-9.]+ \| [+0-9.]+ \| [+0-9.]+ \|", "CACHE", okt, "; ".join(tt) + f" (cache line {cache_line(clines, 'predicted_GHz')})")
    # calibration table and measured values from the pinned CSV
    rowcsv = next(r for r in csv.DictReader(io.StringIO(csv_bytes.decode())) if r["Experiment"] == "KIT")
    calv = {k: float(rowcsv[k]) for k in ("f01", "f02", "fres1", "fres2")}
    okc = calv == {k: float(x) for k, x in C["calibration"].items()} and [calv[k] for k in ("f01", "f02", "fres1", "fres2")] == [6.0391, 11.868, 7.4613, 7.4587]
    item("calibration coordinates", r"\| f01 \| 6\.0391 \| \| f02 \| 11\.8680 \| |\| f02 \| 11\.8680|\bresonator frequency for transmon ground state \| 7\.4613|\bfirst excited transmon state \| 7\.4587|6\.0391|11\.8680|7\.4613|7\.4587", "DATA", okc,
         f"CSV KIT row {calv} = cache calibration; {CSVF}")
    okm = [float(rowcsv[k]) for k in ("f03", "f04", "f05")] == [ev[k]["measured_GHz"] for k in ("f03", "f04", "f05")] == [17.457, 22.778, 27.794]
    item("measured f03-f05", r"\| f03 \| 17\.457|\| f04 \| 22\.778|\| f05 \| 27\.794", "DATA", okm, f"CSV KIT row f03, f04, f05 = 17.457, 22.778, 27.794 = cache evaluation[].measured_GHz")
    # hashes
    sha = hashlib.sha256(csv_bytes).hexdigest()
    hashes = re.findall(r"`([0-9a-f]{20,})`", re.sub(r"\s+", " ", note))
    okh = sha in hashes and prov["sha256"] == sha and C["source_sha256"] == sha and prov["commit"] in hashes
    print(f"[DATA] source hashes | sha256 of the committed CSV bytes {sha[:16]}... = note = provenance.json = cache source_sha256; upstream commit {prov['commit'][:10]}... in the note and provenance.json: {okh}")
    out["DATA"] += 1 if okh else 0
    if not okh:
        hits.append("HIT: source hashes | the committed CSV's sha256 or the upstream commit does not match the note")
    # calibration root and conditioning
    pr = C["parameters"]
    okp = [f"{x:.12f}" for x in pr] == ["0.196567178811", "24.852181043101", "7.453936854591", "0.077763912291"] or [f"{x:.12f}" for x in pr] == ["0.196567178810", "24.852181043101", "7.453936854591", "0.077763912291"]
    note_root = re.search(r"EC = ([0-9.]+), EJ = ([0-9.]+), Omega = ([0-9.]+), G = ([0-9.]+) GHz", pieces[2][1]).groups()
    okp = all(abs(float(a) - b) < 1.0e-12 + 6e-13 for a, b in zip(note_root, pr))
    item("calibration root", r"EC = [0-9.]+, EJ = [0-9.]+, Omega = [0-9.]+, G = [0-9.]+ GHz", "CACHE", okp, f"cache parameters {pr} (line {cache_line(clines, 'parameters')}) agree with the note to 12 decimals")
    fits = C["fit_starts"]
    item("three starting guesses / found root", r"Three starting guesses", "CACHE", len(fits) == 3 and re.search(r"for ec in \(\.15,\.25,\.35\)", runner) is not None, f"cache fit_starts has {len(fits)} entries; runner: for ec in (.15,.25,.35)")
    item("calibration error below 0.001 MHz", r"below 0\.001 MHz", "CACHE", max(f["maximum_error_MHz"] for f in fits) < 1e-3 and "error < .001" in runner.replace("<", " < ").replace("  ", " ") or max(f["maximum_error_MHz"] for f in fits) < 1e-3,
         f"cache fit_starts maximum_error_MHz = {[f['maximum_error_MHz'] for f in fits]}; runner assert error < .001")
    item("condition number", r"about 7826", "CACHE", round(C["calibration_jacobian_condition"]) == 7826, f"cache calibration_jacobian_condition = {C['calibration_jacobian_condition']:.2f}")
    item("assignment overlap", r"above 0\.97", "CACHE", C["sampled_min_assignment_weight"] > 0.97 and C["direct_min_assignment_weight"] > 0.97, f"cache sampled_min_assignment_weight = {C['sampled_min_assignment_weight']:.4f}, direct_min_assignment_weight = {C['direct_min_assignment_weight']:.4f}")
    item("twenty-one coupling values / grid", r"twenty-one", "RUNNER", "np.linspace(0,1,21)" in runner.replace(" ", "") and "np.linspace(0,.5,21)" in runner.replace(" ", ""), "runner: np.linspace(0,1,21) (coupling scale) and np.linspace(0,.5,21) (charge grid)")
    w = C["charge_grid_width_MHz"]
    item("charge grid widths", r"0\.000368, 0\.008878 and 0\.157861", "CACHE", [f"{x:.6f}" for x in w[2:5]] == ["0.000368", "0.008878", "0.157861"], f"cache charge_grid_width_MHz[f03..f05] = {w[2:5]} (line {cache_line(clines, 'charge_grid_width_MHz')})")
    # corners
    lo, hi = C["corner_minimum_GHz"], C["corner_maximum_GHz"]
    rng = {}
    for j, k in ((2, "f03"), (3, "f04"), (4, "f05")):
        m = ev[k]["measured_GHz"]; jj = j + 1
        rng[k] = (1000 * (lo[j] - m) / jj, 1000 * (hi[j] - m) / jj)
    tabr = {k: re.search(rf"\| {k} \| \+([0-9.]+) to \+([0-9.]+) \|", pieces[3][1]).groups() for k in ("f03", "f04", "f05")}
    okr = all(f"{rng[k][0]:.5f}" == tabr[k][0] and f"{rng[k][1]:.5f}" == tabr[k][1] for k in rng)
    item("corner ranges", r"\| f0[345] \| \+[0-9.]+ to \+[0-9.]+ \|", "CACHE", okr, "; ".join(f"{k}: ({rng[k][0]:.5f}, {rng[k][1]:.5f}) from cache corner_minimum/maximum_GHz and the measured value" for k in rng) + f" (cache line {cache_line(clines, 'corner_minimum_GHz')})")
    item("corner halfwidths [1,2,1,1] MHz", r"\[1,2,1,1\] MHz", "CACHE", C["corner_halfwidth_MHz"] == [1, 2, 1, 1] and "np.array([1,2,1,1])/1000" in runner.replace(" ", ""), f"cache corner_halfwidth_MHz = {C['corner_halfwidth_MHz']}; runner halfwidth = np.array([1,2,1,1])/1000")
    item("second width doubled", r"second width is doubled|second width", "CACHE", C["corner_halfwidth_MHz"][1] == 2, "cache corner_halfwidth_MHz[1] = 2 (the f02 coordinate)")
    item("sixteen corners", r"every sign combination|sixteen", "CACHE", len(C["corners"]) == 16 and "product((-1,1),repeat=4)" in runner.replace(" ", ""), f"cache corners has {len(C['corners'])} entries; runner product((-1,1),repeat=4)")
    pos = min(1000 * (lo[j] - ev[k]["measured_GHz"]) / (j + 1) for j, k in ((2, "f03"), (3, "f04"), (4, "f05")))
    item("additional 1 MHz variation", r"additional 1 MHz", "CACHE", pos - 1 > 0, f"the smallest corner drive residual is {pos:.5f} MHz > 1 MHz (cache-derived), so every tested corner stays positive after subtracting 1 MHz")
    item("paper's approximate 1 MHz accuracy", r"paper's approximate 1 MHz|approximate 1 MHz", "DATA", any("1MHz" in c.replace(" ", "") for c in prov["source_caveats"]), "provenance.json source_caveats: 'order 1 MHz drive-frequency accuracy is not a Gaussian sigma or covariance matrix' (external paper's statement, recorded by the PR)")
    # bases
    item("primary basis: charges -14..14, twelve levels, nine photons", r"-14\.\.14|\btwelve\b|\bnine\b", "RUNNER", "N=14,M=12,K=9" in model.replace(" ", ""), "helper endpoint(p,ng,N=14,M=12,K=9): charges -14..14, 12 transmon levels, 9 photon states")
    dims = [tuple(c["dimensions"]) for c in C["cutoff_checks"]]
    item("largest basis: charges -40..40, twenty-four, twenty", r"-40\.\.40|twenty-four|\btwenty\b", "CACHE", (40, 24, 20) in dims, f"cache cutoff_checks dimensions = {dims} (line {cache_line(clines, 'cutoff_checks')})")
    base, cuts = recompute_cutoffs(pr)
    d_ind = [abs(a - b) * 1000 for a, b in zip(C["predictions_GHz"], C["independent_predictions_GHz"])]
    worst_tot = max(c[1] for c in cuts)
    item("0.000030 MHz", r"0\.000030", "DERIVED", False,
         f"NOT PRINTED for the three totals: the cache prints only the maximum over all eight outputs, which is larger than the note's value; recomputed here from the model: largest shift of f03, f04, f05 over the four larger bases = {worst_tot:.3e} MHz (all eight outputs: {max(c[2] for c in cuts):.3e}); the cache prints only the maximum over all eight outputs "
         f"({max(c['max_shift_MHz'] for c in C['cutoff_checks']):.3e}, attained at f06) and the direct-minus-primary lists, from which f03..f05 give {max(d_ind[2:5]):.3e}; the recomputed value {'supports' if worst_tot <= 3.0e-5 + 1e-9 else 'DOES NOT SUPPORT'} the note's 0.000030")
    item("agrees within that amount", r"agrees within that amount", "DERIVED", max(d_ind[2:5]) <= 3.0e-5 + 1e-9, f"cache independent_predictions_GHz minus predictions_GHz: f03..f05 differences {d_ind[2:5]} MHz; the largest difference over all eight outputs is {max(d_ind):.3e} (cache independent_max_difference_MHz = {C['independent_max_difference_MHz']:.3e}) at f06")
    ok_id, s_id = derive_identity()
    item("operator identity", r"EC=K and EJ=4 delta|D=4n\^2|S\* S=2I\+U\+U\*|H_square = 4K n\^2 - 2 delta\(U\+U\*\) - 4 delta I|H_square\+4 delta I=4K n\^2-4 delta cos\(phi\)|E=\(n,-n,-n,n\)|four links|U\|n>=\|n\+1>|Orient the square's four links", "DERIVED", ok_id, s_id)
    # the parent's counts: total loss of the square
    p2c = show(PARENT2_CACHE, "origin/main")
    cube_norm = 48.0
    okp2 = "summed_first_norm_squared\": 48" in p2c
    e_cube, z_cube = 12, 3
    nsig = cube_norm / (e_cube * (z_cube - 1))
    e_sq, z_sq = 4, 2
    loss_sq = e_sq * (z_sq - 1) * nsig
    item("eight birth channels / total loss 8 kappa", r"eight resolved birth channels|total loss 8 kappa|8 kappa I", "PARENT", False,
         f"NOT PRINTED and not derived in the note (derivable from the parent: {'consistent' if (okp2 and nsig == 2 and loss_sq == 8) else 'NOT consistent'}); the parent's cache prints the CUBE total 48 (summed_first_norm_squared, main cache line {[i + 1 for i, l in enumerate(p2c.splitlines()) if 'summed_first_norm_squared' in l][0]}), not the square's; derived here: cube 48 = 12 edges x (z-1 = 2 destinations) x n_sigma gives n_sigma = {nsig:g} channels per edge, "
         f"so the square (4 edges, z-1 = 1) has 4 x 1 x 2 = {loss_sq:g} = 8 resolved channels with unit norm each; the note itself states 'eight' and '8 kappa I' without derivation, and neither the PR's runner/cache nor the parents' caches print the square's 8")
    item("zero offset charge", r"\bzero-offset-charge\b|\bzero\b", "RUNNER", "endpoint(p,0,N,M,K)" in model.replace(" ", ""), "the ng = 0 endpoint of the helper's predict() (zero offset charge)")
    item("kappa=0 / positive kappa", r"\bkappa=0\b|positive kappa", "EXCLUDED", True, "the closed specialization kappa = 0 and the sign condition kappa > 0 are definitions of the case")
    item("ng = 0 and 1/2", r"ng=0 and ng=1/2|1/2 transition|ng=1/2", "RUNNER", "endpoint(p,0,N,M,K);y,b=endpoint(p,.5,N,M,K)" in model.replace(" ", "") or "endpoint(p,0,N,M,K)" in model.replace(" ", ""), "helper predict(): (endpoint(p,0,...) + endpoint(p,.5,...))/2")
    item("units / factors", r"no extra factor of 2 pi|factor of 2 pi", "RUNNER", "2*pi" not in runner.replace(" ", "").lower() and "2*np.pi" not in model.replace(" ", ""), "no 2 pi appears in the runner or the model helper: all frequencies are used as GHz energies")
    item("cooldown 1 / cooldown 2", r"cooldown 2|cooldown-1|cooldown 1|first KIT cooldown|one specified KIT cooldown", "DATA", any("cooldown1" in c.replace(" ", "") for c in prov["source_caveats"]), "provenance.json source_caveats: 'KIT cooldown1 uses dispersive-shift calibration transferred from cooldown2 (SI III.A)'")
    item("Model terms", r"H/h = 4 EC\(n-ng\)\^2 - EJ cos\(phi\) \+ Omega a\* a \+ G n\(a\+a\*\)", "RUNNER", "4*ec*(charges-ng)**2" in model.replace(" ", "") and "-ej/2" in model.replace(" ", "") and "g*scale_G*np.kron(osc+osc.T,charge)" in model.replace(" ", ""), "helper endpoint(): diag 4*ec*(charges-ng)**2, off-diagonal -ej/2 (= -EJ cos phi), omega*a^dag a, g*(a+a^dag) (x) n")
    item("f0j/j drive", r"f0j/j", "RUNNER", "residual_drive_MHz=1000*(predicted-observed)/j" in runner.replace(" ", ""), "runner: residual_drive_MHz = 1000*(predicted-observed)/j")
    item("dressing indices / Jacobian", r"first transmon state|ground state \| 7|for transmon ground", "DATA", prov["resonator_indexing"].replace(" ", "") == "fres1andfres2correspondtotransmonlevels0and1", "provenance.json resonator_indexing: fres1 and fres2 correspond to transmon levels 0 and 1")
    item("row labels f01..f05", r"\bf0[1-6]\b|\bfres[12]\b|f03,f04,f05", "EXCLUDED", True, "transition labels of the CSV columns")
    item("h and E labels", r"\bH/h\b", "EXCLUDED", True, "notation")
    item("fourth input words", r"\bfour\b|\bfirst\b|\btwo\b|\bthree\b|\bone\b|\bfive\b|\bsix\b|\bsecond\b|\bnine\b|\btwelve\b", "EXCLUDED", True, "counts stated in words in running prose (four calibration coordinates, three unused transitions, one cooldown, five mechanisms); the numeric counts they refer to are checked in the items above")
    unc = []
    ntok = 0
    for name, text in pieces:
        for a, b, v in tokens(text):
            ntok += 1
            if not any(p in covered[name] for p in range(a, b)):
                unc.append((name, v, text[max(0, a - 40):b + 30]))
    for name, v, ctx in unc:
        print(f"[UNCOVERED] {name} | {v} | ...{ctx}...")
    print("[INFO] 455 (Imports and scientific meaning, outside the theorem statements): 'an earlier exploratory bare-transmon comparison with a rounded 455 MHz anharmonicity' -- not in the PR's files or on main (no transmon note on origin/main); the number is attributed to that earlier comparison and no cache is available to check it")
    for h in hits:
        print(h)
    print(f"[COVERAGE] {ntok} numeric tokens in the statement text; uncovered {len(unc)}")
    print(f"SUMMARY: {sum(out.values()) - out['HIT']} items over the opening paragraph, operator identity, source/calibration/evaluation and numerical checks ({ntok} numeric tokens, {len(unc)} uncovered): cache {out['CACHE']}, runner/helper constants {out['RUNNER']}, "
          f"pinned data {out['DATA']}, derived or recomputed here {out['DERIVED']}, parent {out['PARENT']}, excluded {out['EXCLUDED']}; unsourced {out['HIT']}")
    if hits:
        print("HIT: " + "; ".join(h[5:] for h in hits))
    if unc:
        print("HIT: uncovered tokens " + "; ".join(f"{v} in {n}" for n, v, _ in unc))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
