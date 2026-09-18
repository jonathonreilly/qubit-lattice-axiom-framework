#!/usr/bin/env python3
"""Run one science probe by id and write its log.

    python3 probes/run_probe.py <task_id> --worker <name> --review "<one sentence>" [--model <name>] [--seed N] [--minutes M] [--box AxBxL] [--extra "..."]

Tasks are read from probes/TASKS.json (generated + hand-written).  A log is written to
logs/probes/<task_id>/<worker>__<git-sha8>__<utc-timestamp>.json with the full stdout beside it (.txt), and the self-check
(probes/check_log.py) runs on it at once; its last line must be CHECK PASS before the log is committed.
--review is the worker's own one-sentence reading of the output (what it shows; whether it matches the task's `what`); write it
after looking at the output — run once without it to see the output, then re-run with it, or add it afterwards with
`python3 probes/check_log.py <log> --review "..."` .  Tasks marked `direct` (the P: re-executions) are run by their own script.
The worker commits ONLY files under logs/probes/ (and, for judgment tasks, probes/work/) and pushes to ai/probes (pull --rebase first).
Nothing here modifies notes, runners or packs."""
import argparse, json, os, subprocess, sys, time, datetime, hashlib, shlex, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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
    ap.add_argument("--box", default=""); ap.add_argument("--extra", default=""); ap.add_argument("--review", default="")
    args = ap.parse_args()
    tasks = load_tasks()
    import tasklib
    task = tasks.get(args.task_id) or tasklib.synth(args.task_id, list(tasks))
    if not task:
        print("unknown task; see probes/TASKS.json"); return 2
    if task.get("direct"):
        print("this task runs through its own script:"); print("   " + task["command"].replace("{EXTRA}", args.extra) + f" --worker {args.worker}" + (f" --model {args.model}" if args.model else "") + (f' --review "{args.review}"' if args.review else ""))
        return 3
    cmd = build_command(task, args)
    started = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
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
           "started_utc": started, "elapsed_s": round(elapsed, 1), "returncode": proc.returncode, "hit": hit, "summary": summary, "review": args.review, "what": task.get("what", ""),
           "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(), "stdout_tail": stdout[-1500:]}
    with open(os.path.join(d, base + ".json"), "w") as f:
        json.dump(log, f, indent=1)
    with open(os.path.join(d, base + ".txt"), "w") as f:
        f.write(stdout)
    print(json.dumps({k: log[k] for k in ("task", "worker", "elapsed_s", "returncode", "hit", "summary")}, indent=1))
    print(f"log: logs/probes/{args.task_id}/{base}.json")
    print("self-check:")
    chk = subprocess.run([sys.executable, os.path.join(ROOT, "probes", "check_log.py"), os.path.join(d, base + ".json")], capture_output=True, text=True)
    print(chk.stdout.strip())
    return 0 if chk.returncode == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
