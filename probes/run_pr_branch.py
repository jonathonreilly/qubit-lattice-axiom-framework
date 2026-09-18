#!/usr/bin/env python3
"""Re-execute the runners of an open science PR in an isolated worktree (task type P).

    python3 probes/run_pr_branch.py <pr-number> --worker <name> [--model <m>] [--review "..."] [--no-census]

Fetches the PR's branch, creates a temporary git worktree, finds the runners the PR adds or changes under scripts/, runs each
(recording the TOTAL line) and its mutation census when it exposes --list-mutations, then removes the worktree and writes the log
under logs/probes/P:<pr-number>/ in THIS checkout (ai/probes).  Nothing on the PR branch is modified.  A hit is a runner with a
FAIL, a mutation that fails no family or the wrong family, or a runner that does not run."""
import argparse, json, os, re, subprocess, sys, time, datetime, hashlib, shutil, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def sh(cmd, cwd=ROOT, timeout=3600):
    p = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout + (("\n[stderr]\n" + p.stderr[-3000:]) if p.stderr else "")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pr", type=int); ap.add_argument("--worker", required=True); ap.add_argument("--model", default="")
    ap.add_argument("--review", default=""); ap.add_argument("--no-census", action="store_true")
    a = ap.parse_args()
    rc, out = sh(f"gh pr view {a.pr} --json headRefName,title,baseRefName -q '.headRefName+\"|\"+.baseRefName+\"|\"+.title'")
    if rc != 0 or "|" not in out:
        print("cannot read the PR (is gh authenticated?)", out); return 2
    branch, base, title = out.strip().split("|", 2)
    sh(f"git fetch -q origin {branch} {base}")
    wt = tempfile.mkdtemp(prefix=f"probe-pr{a.pr}-")
    rc, out2 = sh(f"git worktree add --detach {wt} origin/{branch}")
    if rc != 0:
        print("worktree failed:", out2); return 2
    started = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ"); t0 = time.time()
    lines = [f"PR #{a.pr}: {title}", f"branch {branch} (base {base})"]
    try:
        rc, changed = sh(f"git diff --name-only origin/{base}...origin/{branch} -- 'scripts/*.py'")
        runners = [f for f in changed.split() if re.search(r"_20\d\d_\d\d_\d\d\.py$", f)]
        lines.append(f"runners in the PR: {len(runners)}")
        hit = False; results = []
        for r in runners:
            rc1, o1 = sh(f"python3 {r}", cwd=wt, timeout=1800)
            total = re.findall(r"TOTAL: PASS=\d+ FAIL=\d+", o1)
            tline = total[-1] if total else "no TOTAL line"
            res = {"runner": r, "returncode": rc1, "total": tline}
            lines.append(f"== {r}: rc={rc1} {tline}")
            if rc1 != 0 or not total or "FAIL=0" not in tline:
                hit = True; lines.append(o1[-1500:])
            if not a.no_census and "--list-mutations" in open(os.path.join(wt, r), encoding="utf-8", errors="ignore").read():
                rc2, muts = sh(f"python3 {r} --list-mutations", cwd=wt)
                bad = []
                for m in [l.split()[0] for l in muts.split("\n") if l.strip() and not l.startswith("[")]:
                    rc3, o3 = sh(f"python3 {r} --mutation {m}", cwd=wt, timeout=1800)
                    exp = re.findall(r"mutation_family_expected: (\S+)", o3); obs = re.findall(r"mutation_family_observed: (\S+)", o3)
                    okm = bool(exp and obs and exp[-1] == obs[-1])
                    lines.append(f"   mutation {m}: expected {exp[-1] if exp else '?'} observed {obs[-1] if obs else '?'} {'ok' if okm else 'MISMATCH'}")
                    if not okm: bad.append(m); hit = True
                res["census_mismatches"] = bad
            results.append(res)
    finally:
        sh(f"git worktree remove --force {wt}"); shutil.rmtree(wt, ignore_errors=True)
    stdout = "\n".join(lines)
    sha = subprocess.check_output(["git", "rev-parse", "--short=8", "HEAD"], cwd=ROOT, text=True).strip()
    task_id = f"P:{a.pr}"
    d = os.path.join(ROOT, "logs", "probes", task_id); os.makedirs(d, exist_ok=True)
    basename = f"{a.worker}__{sha}__{started}"
    log = {"task": task_id, "type": "pr-reexecution", "lane": branch.split("/")[-1][:40], "worker": a.worker, "model": a.model,
           "command": f"python3 probes/run_pr_branch.py {a.pr}", "pr": a.pr, "branch": branch, "git_sha": sha, "started_utc": started,
           "elapsed_s": round(time.time() - t0, 1), "returncode": 0, "hit": hit, "summary": {"runners": results}, "review": a.review,
           "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(), "stdout_tail": stdout[-1500:]}
    json.dump(log, open(os.path.join(d, basename + ".json"), "w"), indent=1)
    open(os.path.join(d, basename + ".txt"), "w").write(stdout)
    print(stdout[-2000:]); print(f"log: logs/probes/{task_id}/{basename}.json  hit={hit}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
