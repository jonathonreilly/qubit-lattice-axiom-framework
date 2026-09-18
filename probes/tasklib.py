"""Shared by run_probe, check_log and claim: task lookup, including tasks that are derived from the logs instead of listed."""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def safe(s): return re.sub(r"-+", "-", re.sub(r"[^A-Za-z0-9._]", "-", s)).strip("-.")[:180]
def family(model):
    m = re.search(r"[a-z]+", (model or "").lower()); f = m.group(0) if m else ""
    return {"opus": "claude", "sonnet": "claude", "haiku": "claude", "fable": "claude", "mythos": "claude", "o": "gpt", "chatgpt": "gpt", "codex": "gpt"}.get(f, f)
def confirm_id(task_id): return "J:confirm:" + safe(task_id)
def synth(task_id, tasks):
    """J:confirm:<task> — an independent reproduction of a HIT logged under another task.  Derived, not listed: a confirm task
    exists as soon as a hit is on the branch, without anyone regenerating TASKS.json."""
    if not task_id.startswith("J:confirm:"): return None
    src = next((t for t in tasks if safe(t) == task_id[len("J:confirm:"):]), None)
    if src and src.startswith("J:derive:"):
        prob = src.split(":")[2]
        return {"id": task_id, "type": "judgment", "lane": "referee", "tier": 3, "command": "{EXTRA}", "cwd": ".", "timeout_s": 14400,
                "hit_pattern": r"(?mi)^HIT", "parse": {"summary": r"(?m)^SUMMARY: (.*)"}, "confirms": src,
                "what": (f"REFEREE A DERIVATION. Another worker claims a proof, a counterexample or a new exact partial result under logs/probes/{src}/; its files are probes/work/derive/{prob}/<worker>/ATTEMPT.md and check.py. You are the hostile reader. "
                         "1. Read the problem statement in probes/TASKS.json (the task's `what`) and the definitions in the notes it names; check that the attempt proves THAT statement and not a weaker or neighbouring one. 2. Go through ATTEMPT.md step by step and find the FIRST step that does not follow; for every step that asserts a finite fact, verify it yourself by brute force at small sizes with your own code, not theirs. 3. Look for the classic failures: a quantifier swapped, an induction hypothesis used at the wrong level, a bound that holds only for the sizes checked, an outside theorem used beyond its hypotheses, a circular use of the statement. "
                         f"Write probes/work/derive/{prob}/referee_<your worker name>/REPORT.md (step-by-step verdicts) and check.py (your independent verifications). It prints `HIT: confirmed - <the claim survives; what you verified independently>` or `SUMMARY: fails at step <n> - <why>`; always a SUMMARY line. If your model family is the author's, release the unit.")}
    return {"id": task_id, "type": "judgment", "lane": "confirm", "tier": 2, "command": "{EXTRA}", "cwd": ".", "timeout_s": 7200,
            "hit_pattern": r"(?mi)^HIT", "parse": {"summary": r"(?m)^SUMMARY: (.*)"}, "confirms": src,
            "what": (f"CONFIRM OR REFUTE a HIT. Another worker logged hit=true under logs/probes/{src}/ (read that log, its .txt and, for a judgment task, the script it names under probes/work/). "
                     "1. Re-run the finder's script and read it line by line for an error in the TEST, not in the note. 2. Write your OWN script under probes/work/confirm/<stub>/ that tests the same statement with different machinery (another representation, exact arithmetic where the finder used floats, another size). "
                     "3. It prints `HIT: confirmed - <what>` when your independent test reaches the finder's conclusion, or `SUMMARY: not reproduced - <why the finder's test is wrong>`; always a SUMMARY line. "
                     "The note lives on its PR branch: git fetch origin <branch>; git show origin/<branch>:<note>. If your model family is the finder's, release the unit: a confirmation must come from a different family.")}
def lookup(task_id, root=ROOT):
    tasks = {t["id"]: t for t in json.load(open(os.path.join(root, "probes", "TASKS.json")))}
    return tasks.get(task_id) or synth(task_id, list(tasks))
