#!/usr/bin/env python3
"""Self-check of a probe log before it is committed.  Run it on every log you produce:

    python3 probes/check_log.py logs/probes/<task_id>/<file>.json [--reviewer <name>]

It verifies that the log is well formed and consistent with the checkout, re-derives the hit/parse fields from the saved stdout,
compares runner re-executions with the pinned cache, checks that judgment-task scripts are committed under probes/work/, and
writes a `checked` block into the log.  Commit only logs whose last line here is `CHECK PASS`.  A `CHECK FAIL` log is not
committed: fix the cause (re-run with the right arguments, or complete the script) or discard the log.

Exit code 0 = PASS, 1 = FAIL."""
import argparse, json, os, re, subprocess, sys, datetime, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def git(*args):
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    except Exception:
        return ""

def cache_stdout(runner_name):
    p = os.path.join(ROOT, "logs", "runner-cache", runner_name + ".txt")
    if not os.path.exists(p):
        return None, None
    s = open(p, encoding="utf-8", errors="ignore").read()
    m = re.search(r"^runner_sha256:\s*([0-9a-f]{64})", s, flags=re.M)
    body = s.split("----- stdout -----\n", 1)[1].split("\n----- stderr -----", 1)[0] if "----- stdout -----" in s else None
    return (m.group(1) if m else None), body

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("log"); ap.add_argument("--reviewer", default=""); ap.add_argument("--review", default="", help="add or replace the review sentence in the log before checking")
    ap.add_argument("--triage-note", default="", help="the reader's sentence for a triage; the finder's review sentence is kept")
    ap.add_argument("--verdict", default="", choices=["", "science", "false-positive", "machine"], help="triage of a hit or a failed check by a reader: science (open ONE issue per task), false-positive (the task's pattern is wrong: no issue), machine (missing package, timeout: no issue)")
    a = ap.parse_args()
    findings, ok = [], True
    def fail(msg):
        nonlocal ok; ok = False; findings.append("FAIL: " + msg)
    def note(msg):
        findings.append("ok: " + msg)
    try:
        log = json.load(open(a.log))
    except Exception as e:
        print("CHECK FAIL: unreadable log:", e); return 1
    if a.review:
        log["review"] = a.review
    txt = a.log[:-5] + ".txt"
    if not os.path.exists(txt):
        fail("stdout file missing beside the log (expected " + os.path.basename(txt) + ")")
        stdout = ""
    else:
        stdout = open(txt, encoding="utf-8", errors="ignore").read()
        if hashlib.sha256(stdout.encode()).hexdigest() != log.get("stdout_sha256"):
            fail("stdout file does not match the log's stdout_sha256 (edited after the run?)")
        else:
            note("stdout file matches its hash")
    tasks = {t["id"]: t for t in json.load(open(os.path.join(ROOT, "probes", "TASKS.json")))}
    import tasklib
    task = tasks.get(log.get("task")) or tasklib.synth(str(log.get("task")), list(tasks))
    if not task:
        fail(f"unknown task id {log.get('task')!r} (regenerate TASKS.json or fix the id)")
    for k in ("worker", "command", "git_sha", "started_utc", "returncode"):
        if k not in log: fail(f"log lacks field {k}")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", str(log.get("worker", ""))):
        fail("worker name must be a plain token (letters, digits, - _ .)")
    exp_name = f"{log.get('worker')}__{log.get('git_sha')}__{log.get('started_utc')}.json"
    if os.path.basename(a.log) != exp_name:
        fail(f"file name should be {exp_name}")
    if os.path.dirname(os.path.abspath(a.log)) != os.path.abspath(os.path.join(ROOT, "logs", "probes", str(log.get("task")))):
        fail("log is not under logs/probes/<task_id>/")
    head = git("rev-parse", "--short=8", "HEAD")
    if head and log.get("git_sha") != head:
        note(f"log's git sha {log.get('git_sha')} differs from the current HEAD {head} (fine if you pulled since; the run is bound to its sha)")
    if log.get("returncode") not in (0, None):
        fail(f"the command exited with code {log.get('returncode')} — the run did not complete; see the stdout tail")
    if task:
        # re-derive hit and parse fields from the saved stdout
        hit = bool(task.get("hit_pattern")) and re.search(task["hit_pattern"], stdout) is not None
        if hit != bool(log.get("hit")) and (a.verdict or log.get("triage", {}).get("verdict")) == "false-positive":
            note(f"hit field {log.get('hit')} was a false positive of an earlier pattern (triaged); the current pattern gives {hit}")
        elif hit != bool(log.get("hit")):
            fail(f"hit field {log.get('hit')} disagrees with the task's hit pattern on the stdout ({hit})")
        else:
            note(f"hit field consistent ({hit})")
        for name, pat in task.get("parse", {}).items():
            if not re.findall(pat, stdout) and (a.verdict or log.get("triage", {}).get("verdict")) == "false-positive":
                note(f"parse field {name!r} not found (log written under an earlier task definition; triaged)")
            elif not re.findall(pat, stdout):
                fail(f"parse field {name!r} found nothing in the stdout: the run may not have reached its summary")
        if task.get("expect_pattern") and not re.search(task["expect_pattern"], stdout):
            fail("expected pattern absent (for a runner: no `PASS=n FAIL=0` verdict line of the format its cache has)")
        if task["type"] == "runner-reexecution":
            name = task["command"].split("scripts/")[1].split(".py")[0]
            csha, cbody = cache_stdout(name)
            rsha = hashlib.sha256(open(os.path.join(ROOT, "scripts", name + ".py"), "rb").read()).hexdigest() if os.path.exists(os.path.join(ROOT, "scripts", name + ".py")) else None
            if cbody is None:
                note("no pinned cache for this runner (nothing to compare)")
            else:
                same_runner = (csha == rsha)
                VERDICT = r"(?:TOTAL: |SUMMARY:[^\n]*?|SCORECARD )?PASS\s*=\s*\d+[^\n]{0,40}FAIL\s*=\s*\d+"
                cache_total = re.findall(VERDICT, cbody)
                run_total = re.findall(VERDICT, stdout)
                if cache_total and run_total and cache_total[-1] != run_total[-1]:
                    fail(f"verdict line differs from the pinned cache: run {run_total[-1]!r} vs cache {cache_total[-1]!r}")
                elif cache_total and not run_total:
                    fail(f"the pinned cache ends with the verdict {cache_total[-1]!r} and this run printed none")
                elif task.get("verdict_line") is not None:
                    rl = [l.rstrip() for l in stdout.split("\n[stderr]")[0].splitlines() if len(re.findall(r"[A-Za-z0-9]", l)) >= 3]
                    if not rl or rl[-1] != task["verdict_line"]:
                        fail(f"last line differs from the pinned cache: run {(rl[-1] if rl else '')[:80]!r} vs cache {task['verdict_line'][:80]!r}")
                    else:
                        note("last line identical to the pinned cache (this runner prints no PASS/FAIL count)")
                if cache_total and run_total and cache_total[-1] != run_total[-1]:
                    pass
                elif not same_runner:
                    note("runner file differs from the pinned cache's runner_sha256 (cache is stale or the runner changed); verdict lines compared only")
                else:
                    # compare stdout bodies modulo trailing whitespace
                    if cbody.strip() == stdout.split("\n[stderr]")[0].strip():
                        note("stdout identical to the pinned cache")
                    else:
                        note("stdout differs from the pinned cache in some lines (verdict lines agree); a reviewer should diff logs/runner-cache/" + name + ".txt against the .txt beside this log")
                    log.setdefault("summary", {})["cache_stdout_identical"] = (cbody.strip() == stdout.split("\n[stderr]")[0].strip())
        if task["type"] == "judgment":
            cmd = log.get("command", "")
            scripts = re.findall(r"probes/work/[\w\-./]+\.py", cmd)
            if not scripts:
                fail("judgment task: the command must run a script under probes/work/<stub>/ (pass it with --extra)")
            for sp in scripts:
                if not os.path.exists(os.path.join(ROOT, sp)):
                    fail(f"script {sp} does not exist in the checkout")
                elif git("ls-files", "--error-unmatch", sp) == "":
                    fail(f"script {sp} is not committed (git add it with the log)")
            if not re.search(r"(?m)^SUMMARY:", stdout):
                fail("judgment task: the script must print a final line starting with `SUMMARY:`")
    if not log.get("review"):
        fail("no `review` sentence in the log: re-run with --review \"<one sentence: what the output shows and whether it matches the task's description>\" or add it now with --reviewer")
    if a.reviewer and not log.get("review"):
        pass
    if a.verdict:
        log["triage"] = {"verdict": a.verdict, "note": a.triage_note, "by": a.reviewer or log.get("worker"), "at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")}
    log["checked"] = {"by": a.reviewer or log.get("worker"), "at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ"), "result": "PASS" if ok else "FAIL", "findings": findings}
    json.dump(log, open(a.log, "w"), indent=1)
    for f in findings: print(f)
    print("CHECK PASS" if ok else "CHECK FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
