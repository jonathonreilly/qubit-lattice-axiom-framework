#!/usr/bin/env python3
"""Run one science probe by id and write its log.

    python3 probes/run_probe.py <task_id> --worker <name> [--model <name>] [--seed N] [--minutes M] [--box AxBxL] [--extra "..."]

Tasks are read from probes/TASKS.json (generated + hand-written).  A log is written to
logs/probes/<task_id>/<worker>__<git-sha8>__<utc-timestamp>.json with the full stdout beside it (.txt).
The worker then commits ONLY files under logs/probes/ and pushes to the branch ai/probes (pull --rebase first).
Nothing here modifies notes, runners or packs."""
import argparse, json, os, subprocess, sys, time, datetime, hashlib, shlex, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short=8", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "nogit"

def load_tasks():
    with open(os.path.join(ROOT, "probes", "TASKS.json")) as f:
        return {t["id"]: t for t in json.load(f)}

def build_command(task, args):
    cmd = task["command"]
    subs = {"SEED": str(args.seed), "MINUTES": str(args.minutes), "SECONDS": str(int(args.minutes * 60)), "EXTRA": args.extra or ""}
    if args.box:
        a, b, c = args.box.lower().split("x"); subs.update({"A": a, "B": b, "L": c})
    else:
        a, b, c = task.get("default_box", "4x4x7").split("x"); subs.update({"A": a, "B": b, "L": c})
    for k, v in subs.items():
        cmd = cmd.replace("{" + k + "}", v)
    return cmd

def summarize(task, stdout):
    out = {}
    for name, pat in task.get("parse", {}).items():
        m = re.findall(pat, stdout)
        if m:
            out[name] = m[-1] if len(m) == 1 else m
    hit = False
    if task.get("hit_pattern"):
        hit = re.search(task["hit_pattern"], stdout) is not None
    if task.get("expect_pattern"):
        out["expected_ok"] = re.search(task["expect_pattern"], stdout) is not None
    return out, hit

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task_id"); ap.add_argument("--worker", required=True); ap.add_argument("--model", default="")
    ap.add_argument("--seed", type=int, default=int(time.time()) % 100000); ap.add_argument("--minutes", type=float, default=10)
    ap.add_argument("--box", default=""); ap.add_argument("--extra", default="")
    args = ap.parse_args()
    tasks = load_tasks()
    if args.task_id not in tasks:
        print("unknown task; see probes/TASKS.json"); return 2
    task = tasks[args.task_id]
    cmd = build_command(task, args)
    started = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    t0 = time.time()
    proc = subprocess.run(cmd, shell=True, cwd=os.path.join(ROOT, task.get("cwd", ".")), capture_output=True, text=True, timeout=task.get("timeout_s", 7200))
    elapsed = time.time() - t0
    stdout = proc.stdout + ("\n[stderr]\n" + proc.stderr[-4000:] if proc.stderr else "")
    summary, hit = summarize(task, stdout)
    sha = git_sha()
    d = os.path.join(ROOT, "logs", "probes", args.task_id); os.makedirs(d, exist_ok=True)
    base = f"{args.worker}__{sha}__{started}"
    log = {"task": args.task_id, "type": task.get("type"), "lane": task.get("lane"), "worker": args.worker, "model": args.model,
           "command": cmd, "seed": args.seed, "minutes": args.minutes, "box": args.box or task.get("default_box"), "git_sha": sha,
           "started_utc": started, "elapsed_s": round(elapsed, 1), "returncode": proc.returncode, "hit": hit, "summary": summary,
           "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(), "stdout_tail": stdout[-1500:]}
    with open(os.path.join(d, base + ".json"), "w") as f:
        json.dump(log, f, indent=1)
    with open(os.path.join(d, base + ".txt"), "w") as f:
        f.write(stdout)
    print(json.dumps({k: log[k] for k in ("task", "worker", "elapsed_s", "returncode", "hit", "summary")}, indent=1))
    print(f"log: logs/probes/{args.task_id}/{base}.json")
    return 0

if __name__ == "__main__":
    sys.exit(main())
