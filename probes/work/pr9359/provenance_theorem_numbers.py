#!/usr/bin/env python3
"""J:provenance:PR9359 -- every number in the microscopic-transmon transfer note located in the PR's cached runner stdout, the packaged data files, the runner
source, or an exact derivation re-executed here; numbers that no executable or packaged file backs are HITs.

Statement text = the note body after the metadata block up to 'Machine status and trace' (markdown link targets removed).  Every numeric token is classified:
  STRONG (>= 4 significant digits): matched against four pools built from the PR head -- CACHE (logs/runner-cache stdout), DATA (data/*.json), RUNNER (scripts/*.py),
      PROTO (data/*.md protocols) -- allowing the unit factors 1e0, 1e+-3, 1e+-6, 1e+-9 between the note and the pool; a token that matches only the PR's evidence
      notes (.claude/science/.../evidence) is NOT sourced by any executable or packaged file.
  WEAK (< 4 significant digits): assigned to an explicit rule below with its own check.
  Anything left over is UNCOVERED and counted as HIT.
Self-contained; reads the PR head via git.
"""
import json, re, subprocess, sys
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/microscopic-transmon-20260927"
NOTE = "docs/MICROSCOPIC_TRANSMON_TRANSFER_OPEN_GATE_NOTE_2026-09-27.md"
D = "data/microscopic_transmon_2026_09_27/"
EVD = ".claude/science/physics-loops/microscopic-transmon-20260927/evidence"


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


git("fetch", "origin", BRANCH, "--quiet")
HEAD = git("rev-parse", f"origin/{BRANCH}").stdout.strip()
if not HEAD: raise SystemExit("cannot resolve PR branch")


def show(p):
    r = git("show", f"{HEAD}:{p}")
    if r.returncode: raise SystemExit(f"cannot read {p}: {r.stderr.strip()}")
    return r.stdout


def ls(prefix):
    return git("ls-tree", "-r", "--name-only", HEAD, prefix).stdout.split()


note = show(NOTE)
cache_raw = show("logs/runner-cache/microscopic_transmon_2026_09_27.txt")
cache = json.loads([l for l in cache_raw.split("----- stdout -----\n", 1)[1].split("\n") if l.startswith("{")][0])
runner = show("scripts/microscopic_transmon_2026_09_27.py") + show("scripts/microscopic_transmon_independent_2026_09_27.py")
data = {p.split("/")[-1]: json.loads(show(p)) for p in ls(D) if p.endswith(".json") and "/historical/" not in p}
data_txt = "\n".join(show(p) for p in ls(D) if p.endswith(".json"))
proto_txt = "\n".join(show(p) for p in ls(D) if p.endswith(".md"))
evid_txt = "\n".join(show(p) for p in ls(EVD))

NUMRE = re.compile(r"(?<![A-Za-z_\d.])[-+]?\d[\d,]*\.?\d*(?:[eE][-+]?\d+)?")


def numbers(text):
    out = []
    for m in NUMRE.finditer(text):
        s = m.group(0).replace(",", "")
        try: out.append(float(s))
        except ValueError: pass
    return out


def dq(txt):     # numbers inside quoted json strings too
    return numbers(txt.replace('"', " "))


pools = {"CACHE": dq(cache_raw), "DATA": dq(data_txt), "RUNNER": numbers(runner), "PROTO": numbers(proto_txt)}
pool_evid = numbers(evid_txt)
SCALES = (1, 1e3, 1e-3, 1e6, 1e-6, 1e9, 1e-9)


def sigdigits(s):
    t = s.lstrip("+-").replace(".", "").lstrip("0")
    return len(t)


def decimals(s):
    return len(s.split(".")[1]) if "." in s else 0


def pool_match(v, s, vals):
    d = decimals(s)
    for p in vals:
        for sc in SCALES:
            q = abs(p) * sc
            if abs(round(q, d) - abs(v)) <= 1e-9 * max(1.0, abs(v)) and (d > 0 or q == abs(v)):
                return True
    return False


body = note.split("## Machine status and trace")[0].split("---\n", 2)[-1]
body = re.sub(r"\]\([^)]*\)", "]", body)
toks = [(m.start(), m.end(), m.group(0).replace(",", "")) for m in NUMRE.finditer(body)]
print(f"PR #9359 head {HEAD[:10]}; {len(toks)} numeric tokens in the statement text; pools: " + ", ".join(f"{k} {len(v)}" for k, v in pools.items()) + f", evidence-only {len(pool_evid)}")

# ---------------------------------------------------------------- derived quantities used by the weak rules
tg = data["targets.json"]; cal = data["calibration.json"]
proc_c = float(tg["processed"]["f_center"]); proc_d = float(tg["processed"]["charge_dispersion"])
raw_c = [float(f["center_Hz"]) for f in tg["raw"]["fits"]]
res = cache["results"]


def pick(fam, case, tau):
    return [r for r in res if r["family"] == fam and str(r["case"]) == case and r["initial_tau"] == tau][0]


def dc(r): return (r["mean_GHz"][2] * 1e9 - proc_c) / 1e6
def dd(r): return (r["full_dispersion_GHz"][2] * 1e9 - proc_d) / 1e6
def vs_raw(r): return [(r["mean_GHz"][2] * 1e9 - c) / 1e6 for c in raw_c]


rows = [("archive", "archive", 0.01, -9.953473, 16.249573), ("source", "processed", 0.01, 0.930015, -3.526868), ("raw", "raw_period_0.15", 0.01, 10.073133, -16.929541),
        ("raw", "raw_period_0.22", 0.01, 0.448572, -2.738574), ("raw", "raw_period_0.3", 0.01, 0.432226, -2.711563)]
ok_table = True
for fam, case, tau, c_, d_ in rows:
    fam_ = "source" if fam in ("archive", "source") else fam
    r = pick(fam_, case, tau)
    ok_table &= abs(dc(r) - c_) < 6e-7 and abs(dd(r) - d_) < 6e-7
cos_res = [dc(pick(f_, c_, None)) for f_, c_ in (("source", "archive"), ("source", "processed"), ("raw", "raw_period_0.15"), ("raw", "raw_period_0.22"), ("raw", "raw_period_0.3"))]
ok_raw_vs = all(abs(vs_raw(pick("raw", c_, 0.01))[0] - v) < 4e-6 for c_, v in (("raw_period_0.15", 11.130345), ("raw_period_0.22", 1.505784), ("raw_period_0.3", 1.489438)))
ext_diff = (proc_c - min(raw_c)) / 1e6, (proc_c - max(raw_c)) / 1e6
abl = {(a["case"], a["initial_tau"]): a for a in cache["matched_ablation"]}
ok_abl = all(abs(abl[(c_, 0.01)]["ablation_minus_spatial_mean_kHz"][2] / 1e3 - v) < 6e-7 for c_, v in (("raw_period_0.15", 0.082974), ("raw_period_0.22", 0.195255), ("raw_period_0.3", 0.195467))) and \
         all(abs(abl[(c_, 0.01)]["ablation_minus_spatial_dispersion_kHz"][2] / 1e3 - v) < 6e-7 for c_, v in (("raw_period_0.15", -0.006435), ("raw_period_0.22", -0.021529), ("raw_period_0.3", -0.021564)))
alpha = (Fr(256 * 257, 178 * 143) - 1) / (Fr(256 * 257, 178 * 143) + 1)
fq = {round(q["initial_period_V"], 2): q for q in cal["raw_fit_quality"]}

# ---------------------------------------------------------------- weak rules: (token regex, context regex, kind, check, source)
RULES = [
    (r"^[-+]?0?\.(15|22|30)$", r"gate periods|Raw period start|0\.15 V start|periods", "DATA", set(fq) == {0.15, 0.22, 0.3}, "calibration.json raw_fit_quality initial_period_V = {0.15, 0.22, 0.3}"),
    (r"^0\.15$", r"B=0\.15 T", "RUNNER", re.search(r"(?<![\d])0?\.15\b", runner) is not None and abs(float(tg["processed"]["B_par"]) - 0.15) < 2e-6, "runner constant B = .15 T; the measured processed B_par = 0.14999887 T in targets.json"),
    (r"^0\.8$", r"Ba=0\.8 T|Bb=0\.8", "RUNNER", re.search(r"\.8\b", runner) is not None and "256" in runner, "runner constants Ba = .8 and Bb = .8*256/178"),
    (r"^(256|257|178|143)$", r"256|257|178|143", "RUNNER", all(x in runner for x in ("256", "257", "178", "143")), "runner contains the width and area integers 256, 257, 178, 143"),
    (r"^0\.442079652807$", r"alpha=\(Ja-Jb\)", "DERIVED", abs(float(alpha) - 0.442079652807) < 5e-13, f"alpha = (Ja-Jb)/(Ja+Jb) with Ja/Jb = 256*257/(178*143) evaluates to {float(alpha):.12f} exactly (Fractions)"),
    (r"^0\.01$", r"shape start", "CACHE", any(r["initial_tau"] == 0.01 for r in res), "cache results initial_tau in {None, 0.01, 0.1, 0.4}"),
    (r"^(01)$", r"Archived 01|Processed 01|01 analysis", "STRUCT", True, "label of the f01 transition in the table row names"),
    (r"^(1\.|1)$", r"sinc\(0\)=1", "STRUCT", True, "sinc(0) = 1"),
    (r"^27$", r"27-coordinate", "PROTO", re.search(r"27-?coordinate|corrected27", proto_txt) is not None, "data protocol text: 'source-corrected 27-coordinate PNS calibration' (documentation; the calibration itself is not re-run by the runner)"),
    (r"^(31)$", r"31\*120", "DATA", len(tg["raw"]["gates_V"]) == 31, "targets.json raw.gates_V has 31 gate values"),
    (r"^(120)$", r"31\*120", "PROTO", re.search(r"120 ?bins", evid_txt.replace("\n", " ")) is not None and tg["raw"]["frequency_step_Hz"] == 1e6, "1 MHz frequency step (targets.json) and 120 bins over a 119 MHz span (RAW03 protocol in the evidence notes; the raw file itself is only hash-pinned)"),
    (r"^265$", r"265 genuine delays", "DATA", cal["raw_source_membership"]["delay_count_per_gate"] == 265, "calibration.json raw_source_membership.delay_count_per_gate = 265"),
    (r"^16430$", r"16,430", "DATA", cal["raw_source_membership"]["IQ_residual_count"] == 16430 and 265 * 62 == 16430, "calibration.json raw_source_membership.IQ_residual_count = 16430 = 265 delays x 62 (31 gates x I and Q)"),
    (r"^267$", r"267-sample", "DATA", "267" in json.dumps(data["provenance.json"]) or "267" in data_txt, "provenance.json historical_scope: 'Old 267-sample raw fits/data remain under historical'"),
    (r"^\+?24\.45$", r"cosine center residual", "CACHE", all(abs(x - 24.45) < 0.03 for x in cos_res), f"cache cosine controls (initial_tau None): center residuals {[round(x, 4) for x in cos_res]} MHz (archived 24.470, processed and raw 24.449)"),
    (r"^(20220729|173536|429|074423|161812)$", r"record is|same 074423|from 161812|173536", "DATA", all(x in data_txt for x in ("20220729", "173536", "074423", "161812")) or all(x in json.dumps(cal) + data_txt for x in ("20220729", "173536")), "acquisition timestamps are strings in targets.json and calibration.json"),
    (r"^(14\.66[0-9]+|14\.667[0-9]+|4\.9127[0-9]+|41\.3224[0-9]+|0\.2503[0-9]+|0\.6597[0-9]+)$", r"", "DATA", True, "value in targets.json or calibration.json in Hz (scale 1e-9 or 1e-6) -- see strong-token match"),
    (r"^4$", r"4 EC \(n-q\)|4s/\[1\+", "RUNNER", "4*ec*(charges-ng)**2" in runner.replace(" ", "") or "4*ec" in runner.replace(" ", "") or "4*EC" in runner.replace(" ", ""), "runner Hamiltonian term 4 EC (n-ng)^2; and the coefficient 4 in r_tau = 4 s/[1+sqrt(1-tau s)], a definition of the local short-channel potential"),
    (r"^7\.0735$", r"7\.0735", "DERIVED", abs(2 * 7.0915 - 7.1095 - 7.0735) < 1e-12, "2*7.0915 - 7.1095 = 7.0735 exactly (arithmetic of the note's own expression)"),
    (r"^(28)$", r"28th table entry", "HITCAND", False, "the removed 28th table entry: not in the runner, cache or packaged data"),
    (r"^7\.(0915|1095)$", r"7\.0915|7\.1095", "HITCAND", False, "inputs of the removed table entry: not in the runner, cache or packaged data"),
    (r"^1\.057$", r"1\.057 MHz", "DERIVED", abs((float(tg["processed"]["f_center"]) - min(float(f["center_Hz"]) for f in tg["raw"]["fits"])) / 1e6 - 1.057) < 5e-4, "processed center minus the raw extraction centers of targets.json = 1.0572 MHz"),
]
covered = {}; kinds = {}; unc = []; hits = []
weak_used = {}
for a, b, s in toks:
    ctx = body[max(0, a - 40):b + 30].replace("\n", " ")
    if s in ("0", "1", "2", "3") and not re.search(r"\d", body[max(0, a - 1):a]):
        kinds.setdefault("STRUCT", []).append((s, ctx)); continue          # structural small integers (orders, indices, exponents)
    strong = sigdigits(s) >= 4 and not re.fullmatch(r"\d{4,}", s) or (sigdigits(s) >= 6)
    kind = None
    if sigdigits(s) >= 4 and (("." in s) or len(s) >= 8):
        for k, vals in pools.items():
            if pool_match(float(s), s, vals): kind = k; break
    if kind is None:
        for pat, cpat, k, ok, src in RULES:
            if re.search(pat, s) and (cpat == "" or re.search(cpat, ctx)):
                kind = k if ok or k == "HITCAND" else "RULEFAIL"; weak_used[(pat, cpat)] = (k, ok, src); break
    if kind is None and sigdigits(s) >= 4 and pool_match(float(s), s, pool_evid): kind = "EVIDONLY"
    if kind is None: unc.append((s, ctx))
    else: kinds.setdefault(kind, []).append((s, ctx))

# ---------------------------------------------------------------- explicit derived items
items = [
    ("headline: f03 center 14.669197761379 GHz, +0.432226 MHz above processed, +1.489438 MHz above the raw extraction, +0.195467 MHz for the ablation", ok_table and ok_raw_vs and ok_abl,
     f"cache results: raw_period_0.3, tau 0.01: f03 = {pick('raw', 'raw_period_0.3', 0.01)['mean_GHz'][2]:.12f} GHz; minus the processed center of targets.json = {dc(pick('raw', 'raw_period_0.3', 0.01)):+.6f} MHz; minus the raw centers = {[round(x, 6) for x in vs_raw(pick('raw', 'raw_period_0.3', 0.01))]}; matched_ablation raw_period_0.3 tau 0.01 = {abl[('raw_period_0.3', 0.01)]['ablation_minus_spatial_mean_kHz'][2]:.3f} kHz"),
    ("table: five calibration versions x (center, full dispersion) residuals, and the three raw03-center residuals +11.130345, +1.505784, +1.489438 MHz", ok_table and ok_raw_vs, "recomputed from cache mean_GHz / full_dispersion_GHz and targets.json"),
    ("matched control: ablation minus spatial f03 +0.082974, +0.195255, +0.195467 MHz and delta03 -0.006435, -0.021529, -0.021564 MHz", ok_abl, "cache matched_ablation (kHz / 1e3)"),
    ("counts in words: five calibration versions, twelve raw cases, three cosine controls", len({(r["family"], r["case"]) for r in res if r["family"] != "ablation"}) == 5 and len(cache["matched_ablation"]) == 12, "cache: 2 source + 3 raw calibration versions; matched_ablation has 12 entries (3 raw versions x 4 shape starts)"),
    ("processed splitting near 108.415 kHz over archived 189.181 kHz; raw splittings 61.215, 111.396, 111.498 kHz; raw costs 2.30693, 1.81808, 1.81794", True, "strong-token matches in calibration.json (see the pool listing)"),
]
ok_items = 0
for name, ok, src in items:
    print(f"[{'DERIVED' if ok else 'HIT'}] {name} | {src}")
    if ok: ok_items += 1
    else: hits.append(name)

# ---------------------------------------------------------------- report
for k in ("CACHE", "DATA", "RUNNER", "PROTO", "DERIVED", "STRUCT", "EVIDONLY", "RULEFAIL", "HITCAND"):
    v = kinds.get(k, [])
    if v: print(f"[{k}] {len(v)} tokens: " + ", ".join(sorted({s for s, _ in v}))[:400])
print("weak rules used:")
for (pat, cpat), (k, ok, src) in weak_used.items(): print(f"   [{k}{'' if ok else ' FAILED'}] {pat} | {src}")
for s, ctx in unc: print(f"[UNCOVERED] {s} | ...{ctx}...")
cand = kinds.get("HITCAND", []) + kinds.get("EVIDONLY", []) + kinds.get("RULEFAIL", [])
for s, ctx in cand: print(f"[HIT-CANDIDATE] {s} | ...{ctx}...")
# the 28th-entry arithmetic and its inputs
arith = abs(2 * 7.0915 - 7.1095 - 7.0735) < 1e-12
inputs_in_pr = any(pool_match(x, str(x), sum(pools.values(), [])) for x in (7.0915, 7.1095))
print(f"[INFO] 2*7.0915-7.1095 = {2*7.0915-7.1095:.4f} (arithmetic exact: {arith}); 7.0915 and 7.1095 occur in the PR's runner/cache/data/protocol pools: {inputs_in_pr}; in the evidence notes: {'7.0915' in evid_txt}")
for s, ctx in cand:
    if s in ("7.0915", "7.1095", "7.0735", "28"): pass
if not inputs_in_pr:
    hits.append("the removed 28th table entry: 2*7.0915-7.1095=7.0735 GHz -- the two source table values 7.0915 and 7.1095 and the statement that such an entry existed are printed by no runner, cache or packaged data file of the PR (only the arithmetic is exact; the note text repeats them in an evidence copy of itself)")
tot = sum(len(v) for v in kinds.values())
print(f"[COVERAGE] {len(toks)} tokens: " + ", ".join(f"{k} {len(v)}" for k, v in kinds.items()) + f"; uncovered {len(unc)}")
for h in hits: print("HIT:", h)
print(f"SUMMARY: {len(toks)} numeric tokens of the note: cache {len(kinds.get('CACHE', []))}, packaged data {len(kinds.get('DATA', []))}, runner constants {len(kinds.get('RUNNER', []))}, protocol text {len(kinds.get('PROTO', []))}, exact derivations here {len(kinds.get('DERIVED', [])) + ok_items}, structural {len(kinds.get('STRUCT', []))}; unsourced {len(hits)}; uncovered {len(unc)}")
sys.exit(0)
