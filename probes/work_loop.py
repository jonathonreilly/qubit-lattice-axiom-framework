#!/usr/bin/env python3
"""The mechanical worker.  Start it and leave it running; it needs no arguments and no coordination with other workers.

    python3 probes/work_loop.py [--model <name>] [--hours H] [--kinds P,R,M,F,S]

It takes a free slot on this machine (a file lock), creates or reuses a PRIVATE detached worktree of ai/probes for that slot
under ~/.probe-workers/<repo>/slot-<k> (so workers never share a checkout), and then repeats: claim a free unit atomically
(probes/claim.py), run its tasks through run_probe.py (every log self-checked), commit the logs, push every few minutes, release
the claims.  It stops when no unit is free or after --hours.  Lines starting with ATTENTION name logs that need a reader."""
import argparse, fcntl, json, os, re, platform, random, shutil, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import claim as C
PUSH_EVERY = 600

def outer(a):
    base = C.base_dir()
    for k in range(1, 200):
        fd = open(os.path.join(base, f"slot-{k}.lock"), "w")
        try: fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError: fd.close(); continue
        wt = os.path.join(base, f"slot-{k}"); ref = C.fetch_branch(f"slot-{k}")
        if not os.path.exists(wt): C.git("worktree", "add", "--quiet", "--detach", wt, ref)
        worker = f"w-{C.machine_id()}-{k}"; print(f"worker {worker}, private worktree {wt}", flush=True)
        cmd = [sys.executable, os.path.join(wt, "probes", "work_loop.py"), "--inner", worker, "--model", a.model, "--hours", str(a.hours), "--kinds", a.kinds]
        C.sync(wt)
        return subprocess.call(cmd, cwd=wt)          # the slot lock is held until the inner loop ends
    print("no free slot"); return 1

def inner(a):
    worker, root = a.inner, os.getcwd(); t_end = time.time() + a.hours * 3600 if a.hours else None
    kinds = [k for k in a.kinds.split(",") if k in C.PRIORITY]
    if "P" in kinds and (not shutil.which("gh") or subprocess.run(["gh", "auth", "status"], capture_output=True).returncode != 0):
        kinds.remove("P"); print("gh not available: PR re-executions left to other workers", flush=True)
    review = f"automatic loop run ({platform.system()} {platform.machine()}, python {platform.python_version()}); verdict and hit re-derived by check_log; not read by a model"
    pending, last_push, skipped = [], time.time(), set()
    def flush():
        nonlocal pending, last_push
        if not pending: return
        C.git("add", "logs/probes", cwd=root)
        if C.git("status", "--porcelain", "--", "logs/probes", cwd=root).stdout.strip():
            C.git("commit", "--quiet", "-m", f"probe: {len(pending)} units by {worker}: " + " ".join(u for u, _ in pending)[:400], cwd=root)
        if C.push(root):
            for u, sha in pending: C.release(u, sha)
            pending = []; last_push = time.time()
        else: print("push failed; will retry", flush=True)
    try:
        while not t_end or time.time() < t_end:
            C.sync(root); tasks = C.load_tasks(root); idx = C.log_index(root)
            u, sha = C.pick_and_claim(worker, kinds, tasks, idx, exclude=skipped | {p for p, _ in pending})
            if not u:
                flush(); print("no free unit: done" if not pending else "units pending push", flush=True)
                if not pending: break
                time.sleep(30); continue
            pending.append((u["unit"], sha)); ran = ok = hits = 0; t0 = time.time()
            for r in u["runs"]:
                if C.run_done(r, idx, u["fresh"]): continue
                if "pr" in r: cmd = [sys.executable, "probes/run_pr_branch.py", r["pr"], "--worker", worker, "--review", review]
                else:
                    cmd = [sys.executable, "probes/run_probe.py", r["task"], "--worker", worker, "--review", review]
                    if "seed" in r: cmd += ["--seed", str(r["seed"])]
                    if r.get("box"): cmd += ["--box", r["box"]]
                    if r.get("extra"): cmd += ["--extra", r["extra"]]
                    if r.get("minutes"): cmd += ["--minutes", str(r["minutes"])]
                if a.model: cmd += ["--model", a.model]
                p = subprocess.run(cmd, cwd=root, text=True, capture_output=True); out = p.stdout + p.stderr; ran += 1
                good = "CHECK PASS" in out; hit = False
                lp = [l[5:].split()[0] for l in out.splitlines() if l.startswith("log: ")]
                try: hit = bool(json.load(open(os.path.join(root, lp[-1]))).get("hit"))
                except Exception: hit = '"hit": true' in out
                ok += good; hits += bool(hit)
                if (hit or not good) and lp and r["task"].startswith("R:"):
                    try:
                        tail = json.load(open(os.path.join(root, lp[-1]))).get("stdout_tail") or ""
                        gone = re.search(r"No such file or directory: '([^']+)'|note-missing[^\n]*?(docs/\S+)|missing (?:note|file)[^\n]*?(docs/\S+)", tail)
                        if gone:
                            path = next(g for g in gone.groups() if g)
                            subprocess.run([sys.executable, "probes/check_log.py", lp[-1], "--reviewer", worker, "--verdict", "stale", "--triage-note", f"automatic: the runner reads {path}, which is not in the tree at that path"], cwd=root, capture_output=True)
                            print(f"STALE {r['task']}: reads {path}", flush=True); continue
                    except Exception: pass
                if hit or not good:
                    logline = [l for l in out.splitlines() if l.startswith("log: ")]
                    print(f"ATTENTION {'HIT' if hit else 'CHECK FAIL'} {r['task']}" + (f" seed {r['seed']}" if "seed" in r else "") + f"  {logline[-1] if logline else '(no log written: ' + out.strip().splitlines()[-1][:120] + ')' if out.strip() else ''}", flush=True)
            print(f"UNIT {u['unit']}: ran={ran} pass={ok} fail={ran-ok} hits={hits} in {time.time()-t0:.0f}s", flush=True)
            if ran and ok == 0 and ran == len(u["runs"]): skipped.add(u["unit"])
            if time.time() - last_push > PUSH_EVERY or len(pending) >= 8: flush()
    except KeyboardInterrupt:
        print("interrupted: pushing what is finished", flush=True)
    flush(); C.forget_seen(worker); return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--model", default=os.environ.get("PROBE_MODEL", "")); ap.add_argument("--hours", type=float, default=0.0)
    ap.add_argument("--kinds", default=",".join(C.PRIORITY)); ap.add_argument("--inner", default="")
    a = ap.parse_args(); sys.exit(inner(a) if a.inner else outer(a))
