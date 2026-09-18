#!/usr/bin/env python3
"""Atomic checkout of work units for any number of parallel workers, with git itself as the lock server.

A unit is claimed by creating the remote ref refs/probes/claims/<unit> (create-if-absent: the server refuses the push when the
ref exists, so exactly one worker wins).  The ref points at a tiny commit whose message names the worker and whose date is the
claim time; a claim older than LEASE_H hours is expired and may be taken over by compare-and-swap.  Completion is never read
from claims: a unit is done when its logs are on ai/probes.  Claims are released after the logs are pushed.

    python3 probes/claim.py status                      units by kind: total / done / claimed / free
    python3 probes/claim.py next --kind J [--model M]   claim one judgment unit, create its private worktree, print the task
    python3 probes/claim.py finish <unit>               push that worktree's commits, release the claim, remove the worktree
    python3 probes/claim.py release <unit>              give a claim back without finishing
Mechanical units (P, R, M, F, S) are claimed and run by probes/work_loop.py; nobody claims those by hand."""
import argparse, datetime, glob, json, os, random, re, secrets, socket, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try: import tasklib
except ImportError: tasklib = None      # a boot copy of claim.py alone: fetched below when needed
NS = "refs/probes/claims/"
LEASE_H = 8.0          # a claim older than this is expired
FRESH_DAYS = 7         # P, R, M units are re-done weekly; F, S, J units once
R_SHARD = 20           # runner re-executions per unit
F_SEEDS, F_BLOCK = 200, 20
S_SEEDS, S_BOXES, S_MINUTES = 200, ["", "5x5x8"], 30
PRIORITY = ["P", "R", "M", "F", "X", "S"]      # the loop's order; J is claimed by hand
J_ORDER = ["J-confirm", "J-attack-g", "J-attack-a", "J-attack-b", "J-attack", "J-falsifier", "J-provenance", "J-note"]      # inside kind J: confirmations first, then the attack patterns by their yield so far
KIND_WEIGHT = {"P": 8, "R": 4, "M": 4, "F": 2, "X": 3, "S": 2}      # the loop draws the kind at random with these weights, so cheap kinds do not starve behind a long one

GIT_CWD = ROOT if os.path.exists(os.path.join(ROOT, ".git")) else os.getcwd()
def git(*a, cwd=None, check=True, env=None, quiet=False):
    r = subprocess.run(["git", *a], cwd=cwd or GIT_CWD, text=True, capture_output=True, env=env)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(a)} failed: {r.stderr.strip()[:400]}")
    return r
def base_dir():
    common = git("rev-parse", "--path-format=absolute", "--git-common-dir").stdout.strip()
    repo = os.path.basename(os.path.dirname(common)) or "repo"
    d = os.path.join(os.path.expanduser("~"), ".probe-workers", repo); os.makedirs(d, exist_ok=True); return d
def machine_id():
    p = os.path.join(os.path.expanduser("~"), ".probe-workers", "machine-id"); os.makedirs(os.path.dirname(p), exist_ok=True)
    if not os.path.exists(p):
        open(p, "w").write(secrets.token_hex(2))
    host = re.sub(r"[^a-z0-9]+", "", socket.gethostname().split(".")[0].lower())[:12] or "host"
    return f"{host}{open(p).read().strip()}"
def safe(s): return re.sub(r"-+", "-", re.sub(r"[^A-Za-z0-9._]", "-", s)).strip("-.")[:180]
def now(): return datetime.datetime.now(datetime.timezone.utc)
def parse_utc(s):
    try: return datetime.datetime.strptime(s, "%Y%m%dT%H%M%SZ").replace(tzinfo=datetime.timezone.utc)
    except Exception: return None

# ---- units -------------------------------------------------------------------------------------------------------------
def load_tasks(root=ROOT): return json.load(open(os.path.join(root, "probes", "TASKS.json")))
def units(tasks, idx=None):
    out = []; idx = idx or {}
    for t in tasks:
        if t["id"].startswith("P:"): out.append({"unit": "P-" + t["id"][2:], "kind": "P", "runs": [{"task": t["id"], "pr": t["id"][2:]}], "fresh": True})
    R = [t["id"] for t in tasks if t["id"].startswith("R:")]
    n = (len(R) + R_SHARD - 1) // R_SHARD
    for k in range(n): out.append({"unit": f"R-{k+1:03d}of{n}", "kind": "R", "runs": [{"task": i} for i in R[k*R_SHARD:(k+1)*R_SHARD]], "fresh": True})
    for t in tasks:
        if t["id"].startswith("M:"): out.append({"unit": "M-" + safe(t["id"][2:]), "kind": "M", "runs": [{"task": t["id"]}], "fresh": True})
    F = [t["id"] for t in tasks if t["id"].startswith("F:") and "{SEED}" in t["command"]]
    for b in range(F_SEEDS // F_BLOCK):
        out.append({"unit": f"F-seeds{b*F_BLOCK+1:03d}to{(b+1)*F_BLOCK:03d}", "kind": "F", "fresh": False,
                    "runs": [{"task": i, "seed": s} for s in range(b*F_BLOCK+1, (b+1)*F_BLOCK+1) for i in F]})
    for t in tasks:
        if t["id"].startswith("S:"):
            boxes = S_BOXES if "{A}" in t["command"] else [""]
            for box in boxes:
                for s in range(1, S_SEEDS + 1):
                    out.append({"unit": "S-" + safe(t["id"][2:]) + f"-s{s:03d}" + (f"-b{box}" if box else ""), "kind": "S", "fresh": False,
                                "runs": [{"task": t["id"], "seed": s, "box": box, "minutes": S_MINUTES}]})
    for t in tasks:      # scans with a declared grid: one unit per grid point
        for g, point in enumerate(t.get("grid", [])):
            out.append({"unit": "X-" + safe(t["id"][2:]) + f"-g{g+1:02d}", "kind": "X", "fresh": False, "runs": [{"task": t["id"], "extra": point["extra"], "box": point.get("box", "")}]})
    for t in tasks:
        if t["id"].startswith("J:") and (":PR" in t["id"] or t["id"].startswith("J:note:")): out.append({"unit": "J-" + safe(t["id"][2:]), "kind": "J", "runs": [{"task": t["id"]}], "fresh": False})
    # derived units: every hit on a judgment or search task that no reader has triaged as a false positive gets ONE independent confirmation
    def defect_class(tid):      # executed-number defects are found by provenance audits AND by attack pattern (c): one confirmation per PR is enough
        revs = " ".join(l.get("review", "") for l in idx.get(tid, []) if l.get("hit"))
        return "executed" if tid.startswith("J:provenance") or re.search(r"\(c\)|EXECUTED NUMBERS", revs) else tid
    def pr_of(tid):
        m = re.search(r"PR(\d+)$", tid); return m.group(1) if m else tid
    confirmed = set()
    for tid in idx:
        if tid and tid.startswith("J:confirm:"):
            src = next((t for t in idx if t and safe(t) == tid[len("J:confirm:"):]), None)
            if src: confirmed.add((pr_of(src), defect_class(src)))
    for tid, logs in sorted(idx.items(), key=lambda kv: str(kv[0])):
        if tid and tid[:2] in ("J:", "S:") and not tid.startswith("J:confirm:"):
            hits = [l for l in logs if l.get("hit") and l.get("verdict") != "false-positive"]
            key = (pr_of(tid), defect_class(tid))
            if hits and key in confirmed and not idx.get("J:confirm:" + safe(tid)): continue      # the same defect on the same PR already has its confirmation
            if hits: confirmed.add(key)
            if hits: out.append({"unit": "J-confirm-" + safe(tid), "kind": "J", "fresh": False, "runs": [{"task": "J:confirm:" + safe(tid)}], "finder_families": sorted({fam(l.get("model")) for l in hits} - {""})})
    return out
def fam(model):
    import re as _re
    m = _re.search(r"[a-z]+", (model or "").lower()); f = m.group(0) if m else ""
    return {"opus": "claude", "sonnet": "claude", "haiku": "claude", "fable": "claude", "mythos": "claude", "o": "gpt", "chatgpt": "gpt", "codex": "gpt"}.get(f, f)

# ---- completion, read from the logs on the branch ------------------------------------------------------------------------
def entry(L, when):
    verdict = L.get("triage", {}).get("verdict", "")
    ok = (L.get("checked", {}).get("result") == "PASS" if "checked" in L else L.get("returncode") == 0) and (not L.get("hit") or verdict == "false-positive")
    return {"when": when, "worker": L.get("worker"), "ok": ok, "seed": L.get("seed"), "box": L.get("box") or "", "hit": bool(L.get("hit")), "model": L.get("model", ""), "verdict": verdict, "command": L.get("command", ""), "review": (L.get("review") or "")[:400]}
def log_index(root=ROOT):
    idx = {}
    for f in glob.glob(os.path.join(root, "logs", "probes", "*", "*.json")):
        try: L = json.load(open(f))
        except Exception: continue
        when = parse_utc(L.get("started_utc", "")) or parse_utc(os.path.basename(f).split("__")[-1][:-5])
        idx.setdefault(L.get("task"), []).append(entry(L, when))
    return idx
def run_done(run, idx, fresh):
    logs = idx.get(run["task"], [])
    if "seed" in run: logs = [l for l in logs if l["seed"] == run["seed"] and l["box"] == run.get("box", "")]
    if "extra" in run: logs = [l for l in logs if run["extra"] in l.get("command", "") and (not run.get("box") or l["box"] == run["box"])]
    if fresh:
        cut = now() - datetime.timedelta(days=FRESH_DAYS); logs = [l for l in logs if l["when"] and l["when"] > cut]
        return any(l["ok"] or l.get("verdict") == "stale" for l in logs) or len({l["worker"] for l in logs}) >= 2      # a failing task gets one second opinion, not endless re-runs; a stale runner (its input file is gone) gets none
    return bool(logs)
def unit_done(u, idx): return all(run_done(r, idx, u["fresh"]) for r in u["runs"])

# ---- claims ------------------------------------------------------------------------------------------------------------------
def remote_claims(worker):
    """{unit: (sha, age_hours, subject)} — one fetch into a namespace private to this worker."""
    seen = f"refs/probes/seen-{safe(worker)}/"
    for attempt in range(3):
        r = git("fetch", "--quiet", "--prune", "origin", f"+{NS}*:{seen}*", check=False)
        if r.returncode == 0: break
        time.sleep(1 + 2 * random.random())
    out = {}
    fmt = "%(refname)\t%(objectname)\t%(committerdate:unix)\t%(subject)"
    for line in git("for-each-ref", f"--format={fmt}", seen).stdout.splitlines():
        ref, sha, ts, subj = line.split("\t", 3)
        out[ref[len(seen):]] = (sha, (time.time() - int(ts)) / 3600.0, subj)
    return out
def try_claim(unit, worker, expect=""):
    env = dict(os.environ, GIT_AUTHOR_NAME=worker, GIT_AUTHOR_EMAIL="probe@localhost", GIT_COMMITTER_NAME=worker, GIT_COMMITTER_EMAIL="probe@localhost")
    tree = git("hash-object", "-w", "-t", "tree", os.devnull).stdout.strip()
    sha = git("commit-tree", tree, "-m", f"claim {unit} by {worker} nonce {secrets.token_hex(4)}", env=env).stdout.strip()
    r = git("push", "--quiet", f"--force-with-lease={NS}{unit}:{expect}", "origin", f"{sha}:{NS}{unit}", check=False)
    return sha if r.returncode == 0 else None
def release(unit, sha):
    return git("push", "--quiet", f"--force-with-lease={NS}{unit}:{sha}", "origin", f":{NS}{unit}", check=False).returncode == 0
def forget_seen(worker):
    seen = f"refs/probes/seen-{safe(worker)}/"
    for line in git("for-each-ref", "--format=%(refname)", seen).stdout.splitlines(): git("update-ref", "-d", line, check=False)
def state_path(unit): return os.path.join(base_dir(), f"held-{unit}.json")      # one file per unit: no shared state between workers
def held(unit):
    try: return json.load(open(state_path(unit)))
    except Exception: return None
def remember(unit, sha, extra=None): json.dump(dict(sha=sha, **(extra or {})), open(state_path(unit), "w"), indent=1)
def forget(unit):
    if os.path.exists(state_path(unit)): os.remove(state_path(unit))
def fetch_branch(tag):
    """Fetch ai/probes into a ref private to the caller (FETCH_HEAD of a shared checkout can be overwritten by a neighbour)."""
    ref = f"refs/probes/head-{safe(tag)}"; git("fetch", "--quiet", "origin", f"+refs/heads/ai/probes:{ref}"); return ref
def tasks_at(ref): return json.loads(git("show", f"{ref}:probes/TASKS.json").stdout)
def log_names_at(ref):
    """Log index from file NAMES in the branch tree (no checkout needed): enough for units that are done once any log exists."""
    idx = {}
    for line in git("ls-tree", "-r", "--name-only", ref, "logs/probes/").stdout.splitlines():
        parts = line.strip('"').split("/")
        if len(parts) == 4 and parts[3].endswith(".json"):
            w = parts[3][:-5].split("__")
            if parts[2][:2] in ("J:", "S:"):
                try: idx.setdefault(parts[2], []).append(entry(json.loads(git("show", f"{ref}:{line.strip(chr(34))}").stdout), parse_utc(w[-1]))); continue
                except Exception: pass
            idx.setdefault(parts[2], []).append({"when": parse_utc(w[-1]), "worker": w[0], "ok": True, "seed": None, "box": "", "hit": False, "model": "", "verdict": "", "command": ""})
    return idx
def pick_and_claim(worker, kinds, tasks, idx, exclude=(), model=""):
    """Claim one free unit: the first kind in `kinds` that has free units, a random unit inside it (random, so that many
    workers starting together do not all race for the same ref)."""
    claims = remote_claims(worker)
    us = [u for u in units(tasks, idx) if u["kind"] in kinds and u["unit"] not in exclude and not (model and fam(model) in u.get("finder_families", []))]
    order = list(kinds)
    if len(order) > 1:
        order = []; pool = list(kinds)
        while pool:
            k = random.choices(pool, weights=[KIND_WEIGHT.get(x, 1) for x in pool])[0]; order.append(k); pool.remove(k)
    for kind in order:
        free = []
        for u in (x for x in us if x["kind"] == kind):
            c = claims.get(u["unit"])
            if c and c[1] < LEASE_H: continue
            if unit_done(u, idx): continue
            free.append((u, c[0] if c else ""))
        random.shuffle(free)
        if kind == "J": free.sort(key=lambda fe: next((i for i, pre in enumerate(J_ORDER) if fe[0]["unit"].startswith(pre)), len(J_ORDER)))
        for u, expect in free[:6]:
            sha = try_claim(u["unit"], worker, expect)
            if sha: return u, sha
    return None, None
def sync(cwd):
    """Bring a detached private worktree up to origin/ai/probes, keeping local commits (logs have unique names: no conflicts)."""
    git("fetch", "--quiet", "origin", "ai/probes", cwd=cwd)
    r = git("rebase", "--quiet", "FETCH_HEAD", cwd=cwd, check=False)
    if r.returncode != 0:
        git("rebase", "--abort", cwd=cwd, check=False); raise RuntimeError("rebase onto origin/ai/probes failed: " + r.stderr.strip()[:300])
def push(cwd, tries=12):
    for k in range(tries):
        sync(cwd)
        if git("push", "--quiet", "origin", "HEAD:refs/heads/ai/probes", cwd=cwd, check=False).returncode == 0: return True
        time.sleep(2 + 6 * random.random() * (k + 1))
    return False

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["status", "next", "finish", "release"]); ap.add_argument("unit", nargs="?")
    ap.add_argument("--kind", default="J"); ap.add_argument("--model", default="")
    a = ap.parse_args(); worker = "w-" + machine_id() + "-j"
    if a.cmd == "status":
        git("fetch", "--quiet", "origin", "ai/probes"); tasks = load_tasks(); idx = log_index(); claims = remote_claims(worker); rows = {}
        for u in units(tasks, idx):
            r = rows.setdefault(u["kind"], [0, 0, 0]); r[0] += 1
            if unit_done(u, idx): r[1] += 1
            elif u["unit"] in claims and claims[u["unit"]][1] < LEASE_H: r[2] += 1
        print("kind  units   done  claimed   free   (done is read from the logs in THIS checkout: pull first)")
        for k, (n, d, c) in rows.items(): print(f"{k:>4} {n:6d} {d:6d} {c:8d} {n-d-c:6d}")
        for u, (sha, age, subj) in sorted(claims.items()): print(f"  claim {u}: {subj.split(' by ')[-1].split(' nonce')[0]}, {age:.1f} h" + (" EXPIRED" if age >= LEASE_H else ""))
        forget_seen(worker); return 0
    if a.cmd == "next":
        worker = worker + secrets.token_hex(2); ref = fetch_branch(worker); tasks = tasks_at(ref); idx = log_names_at(ref)
        u, sha = pick_and_claim(worker, [a.kind], tasks, idx, model=a.model); forget_seen(worker)
        if not u: git("update-ref", "-d", ref, check=False); print("no free unit of kind", a.kind); return 0
        wt = os.path.join(base_dir(), u["unit"])
        if not os.path.exists(wt): git("worktree", "add", "--quiet", "--detach", wt, ref)
        git("update-ref", "-d", ref, check=False)
        remember(u["unit"], sha, {"worktree": wt, "worker": worker}); tid = u["runs"][0]["task"]
        if tid.startswith("J:confirm:"):
            sys.path.insert(0, os.path.join(wt, "probes")); import importlib; tl = importlib.import_module("tasklib"); t = tl.synth(tid, [x["id"] for x in tasks])
        else: t = {x["id"]: x for x in tasks}[tid]
        m = re.search(r"PR(\d+)$", u["unit"])
        known = [(k, l) for k, ls in idx.items() if m and k and k.endswith("PR" + m.group(1)) for l in ls if l.get("hit") and l.get("verdict") != "false-positive"] if m else []
        if known and not tid.startswith("J:confirm:"):
            print("KNOWN HITS ON THIS PR - do not re-find them; a unit that only repeats one of these is wasted. Find something else or report none:")
            for k, l in known: print(f"   {k}: {l.get('review', '')[:260]}")
            print()
        print(f"UNIT {u['unit']}\nTASK {t['id']}\nWORKER {worker}   <- pass this as --worker\nWORKTREE {wt}   <- cd there; do ALL work for this unit in that directory and nowhere else\n\n{t['what']}\n\nRead probes/README.md sections 0, 1 and 4 in that directory. When the log says CHECK PASS: git add logs/probes probes/work; git commit -m 'probe: {u['unit']}'; python3 probes/claim.py finish {u['unit']}")
        return 0
    h = held(a.unit)
    if not h: print("this machine holds no claim on", a.unit); return 1
    if a.cmd == "finish":
        wt = h.get("worktree")
        if wt and os.path.exists(wt):
            dirty = git("status", "--porcelain", "--", "logs/probes", "probes/work", cwd=wt).stdout.strip()
            if dirty: print("uncommitted work in", wt, "— commit logs/probes and probes/work first:\n" + dirty); return 1
            if not push(wt): print("push failed; try again"); return 1
            print("released" if release(a.unit, h["sha"]) else "claim was already gone (expired and taken over?)"); forget(a.unit)
            main = os.path.dirname(git("rev-parse", "--path-format=absolute", "--git-common-dir").stdout.strip()); os.chdir(main)
            if subprocess.run(["git", "worktree", "remove", wt], cwd=main, capture_output=True).returncode != 0: print("note: worktree left in place (it has untracked files):", wt)
            return 0
    print("released" if release(a.unit, h["sha"]) else "claim was already gone (expired and taken over?)"); forget(a.unit); return 0
if __name__ == "__main__":
    sys.exit(main())
