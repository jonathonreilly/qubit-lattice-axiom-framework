#!/usr/bin/env python3
"""Mechanical helpers for docs/ai_methodology/SCIENCE_WORKFLOW.md section 10.

  worktree-add     sparse worktree on its own local branch
  worktree-remove  remove a worktree once its work is pushed
  preflight        check machine, model floor and sandbox before a launch
  numeric-lock     hold the one numeric job allowed on this machine
  status           leads, leases, requests and computed standing of a target
  check-hash       print the hash lines a check record needs
  doctor           refuse when this checkout's rules differ from origin/main

Machine limits come from flags or LAB_MIN_DISK_GB, LAB_MIN_MEM_PCT,
LAB_MAX_LOAD and LAB_LOCK_DIR. Exit 0 means go or done, 1 means refused, and
2 means the numeric lock is held. No scientific authority.
"""

from __future__ import annotations

import argparse
from collections import Counter
import datetime as dt
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import automation_lock  # noqa: E402

DEFAULT_SPARSE_PATHS = (
    "/.gitignore",
    "/AGENTS.md",
    "/CLAUDE.md",
    "/.claude/commands/",
    "/docs/ai_methodology/",
    "/docs/repo/controlled_vocabulary.yaml",
    "/scripts/lab_ops.py",
    "/scripts/automation_lock.py",
    "/scripts/vocab_lint.py",
)
THREAD_VARS = (
    "OMP_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
)
# Older part files type one of four labels by hand. Current ones type only
# `open` or `argued`; anything further is computed from check records.
OBLIGATION_RE = re.compile(
    r"^-\s+(gap|unchecked|implication|discharged|open|argued)\s*:\s*(\S.*)$"
)
OLD_LABELS = ("gap", "unchecked", "implication", "discharged")
NAME_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
# A typed obligation is `<name> [given <premises>] -> <consumer>`.
TYPED_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\s+(given\s+\S.*\s+)?->\s+\S")
PROVENANCE_RE = re.compile(r"\S+/\S+/\S+ \S.*\Z")
VERDICTS = ("right", "wrong", "undecided")
REQUIRED_FIELDS = ("statement", "commit", "content", "verdict", "failure", "path",
                   "checker", "author")
RECORD_FIELDS = REQUIRED_FIELDS + ("answers", "steer")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FLOOR_RE = re.compile(r"^model_floor\s+([\w-]+):\s*(.+)$")
# Entry files, rules, procedures and the step references they bind.
RULE_PATHS = (
    "AGENTS.md",
    "CLAUDE.md",
    "docs/ai_methodology",
    ".claude/commands",
    ":(exclude)docs/ai_methodology/raw",
)


def run(*cmd: str, cwd: Path | str | None = None, timeout: int = 120):
    try:
        return subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout,
            stdin=subprocess.DEVNULL,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return subprocess.CompletedProcess(cmd, 1, "", str(exc))


def git(*args: str, cwd: Path | str | None = None, timeout: int = 120):
    return run("git", *args, cwd=cwd, timeout=timeout)


def refuse(message: str) -> int:
    print(f"refuse: {message}")
    return 1


def env_float(name: str, default: float) -> float:
    return float(os.environ.get(name, default))


# --- worktrees -------------------------------------------------------------


def worktree_add(args: argparse.Namespace) -> int:
    common = git("rev-parse", "--path-format=absolute", "--git-common-dir")
    if common.returncode:
        return refuse(f"not in a git checkout: {common.stderr.strip()}")
    root = Path(common.stdout.strip()).parent
    path = Path(args.dir) if args.dir else root / ".claude" / "worktrees" / args.name
    source = args.target or args.base.removeprefix("origin/")
    fetched = git(
        "fetch", "-q", "origin", f"+refs/heads/{source}:refs/remotes/origin/{source}"
    )
    if fetched.returncode:
        return refuse(f"cannot fetch {source}: {fetched.stderr.strip()}")
    add = ["worktree", "add", "-q", "--no-checkout"]
    if git("show-ref", "--verify", "--quiet", f"refs/heads/{args.name}").returncode == 0:
        add += [str(path), args.name]
    else:
        add += ["--track" if args.target else "--no-track", "-b", args.name,
                str(path), f"origin/{source}"]
    created = git(*add)
    if created.returncode:
        return refuse(created.stderr.strip())
    patterns = list(DEFAULT_SPARSE_PATHS)
    patterns += [p if p.startswith("/") else f"/{p}" for p in args.path]
    for step in (
        ["sparse-checkout", "set", "--no-cone", *patterns],
        ["checkout", "-q", args.name],
    ):
        done = git(*step, cwd=path)
        if done.returncode:
            return refuse(done.stderr.strip())
    print(path)
    if args.target:
        print(
            "share with: git pull --rebase origin "
            f"{args.target} && git push origin HEAD:{args.target}"
        )
    return 0


def worktree_remove(args: argparse.Namespace) -> int:
    path = Path(args.path).resolve()
    state = git("status", "--porcelain", cwd=path)
    if state.returncode:
        return refuse(f"cannot read {path}: {state.stderr.strip()}")
    lines = state.stdout.splitlines()
    untracked = [line[3:] for line in lines if line.startswith("??")]
    if len(untracked) != len(lines):
        return refuse("tracked changes are not committed")
    if untracked and not args.discard_untracked:
        shown = ", ".join(untracked[:5])
        return refuse(f"untracked files would be lost ({shown}); "
                      "keep them or pass --discard-untracked")
    ignored = git("ls-files", "--others", "--ignored", "--exclude-standard", "-z",
                  cwd=path)
    if ignored.returncode:
        return refuse(f"cannot inventory ignored files: {ignored.stderr.strip()}")
    ignored_paths = ignored.stdout.rstrip("\0").split("\0") if ignored.stdout else []
    if ignored_paths:
        shown = ", ".join(ignored_paths[:5])
        return refuse(f"ignored files would be lost ({shown}); "
                      "preserve or remove them explicitly first")
    refs = {"main"}
    branch = git("rev-parse", "--abbrev-ref", "HEAD", cwd=path).stdout.strip()
    if branch and branch != "HEAD":
        refs.add(branch)
    upstream = git("rev-parse", "--abbrev-ref", "@{upstream}", cwd=path)
    if upstream.returncode == 0:
        refs.add(upstream.stdout.strip().removeprefix("origin/"))
    reached = False
    pushed = False
    for ref in sorted(refs):
        remote = f"refs/remotes/origin/{ref}"
        fetched = git("fetch", "-q", "origin", f"+refs/heads/{ref}:{remote}", cwd=path)
        if fetched.returncode:
            continue
        reached = True
        if git("merge-base", "--is-ancestor", "HEAD", remote, cwd=path).returncode == 0:
            pushed = True
    if not reached:
        return refuse("cannot reach origin, so cannot verify that the work is pushed")
    if not pushed:
        return refuse(f"HEAD is not on origin ({', '.join(sorted(refs))}); push first")
    remove = ["worktree", "remove", str(path)]
    if untracked:
        remove.insert(2, "--force")
    removed = git(*remove)
    if removed.returncode:
        return refuse(removed.stderr.strip())
    git("worktree", "prune")
    print(f"removed {path}")
    return 0


# --- doctor ----------------------------------------------------------------


def stale_rules(fetch: bool) -> tuple[list[str] | None, str]:
    """Rule files here that differ from origin/main, and a note on the comparison.

    The list is None when no comparison could be made.
    """
    note = ""
    if fetch:
        fetched = git("fetch", "-q", "origin",
                      "+refs/heads/main:refs/remotes/origin/main", timeout=60)
        if fetched.returncode:
            note = "origin not reachable; compared with the last fetched main"
    diff = git("diff", "--name-only", "origin/main", "--", *RULE_PATHS)
    if diff.returncode:
        return None, diff.stderr.strip() or "cannot compare with origin/main"
    return diff.stdout.split(), note


def doctor(args: argparse.Namespace) -> int:
    changed, note = stale_rules(fetch=not args.no_fetch)
    if changed is None:
        return refuse(f"cannot compare rules with origin/main: {note}")
    behind = git("rev-list", "--count", "HEAD..origin/main").stdout.strip() or "?"
    print(f"checkout: {behind} commits behind origin/main"
          + (f" ({note})" if note else ""))
    if not changed:
        print("rules: match origin/main")
        return 0
    for path in changed[:20]:
        print(f"differs: {path}")
    if len(changed) > 20:
        print(f"differs: {len(changed) - 20} more")
    print("rules: differ from origin/main; read the current ones with "
          "git show origin/main:<path>")
    return 1


# --- preflight -------------------------------------------------------------


def memory_free_pct() -> float | None:
    meminfo = Path("/proc/meminfo")
    if meminfo.exists():
        values = dict(
            re.findall(r"^(MemTotal|MemAvailable):\s+(\d+)", meminfo.read_text(), re.M)
        )
        if len(values) == 2:
            return 100 * int(values["MemAvailable"]) / int(values["MemTotal"])
    found = re.search(r"free percentage:\s*(\d+)", run("memory_pressure", "-Q").stdout)
    return float(found[1]) if found else None


def read_floors(goal: Path) -> dict[str, list[str]]:
    floors: dict[str, list[str]] = {}
    for line in goal.read_text(encoding="utf-8").splitlines():
        found = FLOOR_RE.match(line.strip())
        if found:
            floors[found[1]] = [x.strip() for x in found[2].split(",") if x.strip()]
    return floors


def floor_allows(allowed: list[str], model: str | None, effort: str | None) -> bool:
    if not model:
        return False
    return model in allowed or (effort is not None and f"{model}@{effort}" in allowed)


def numeric_lock_paths() -> tuple[str, str]:
    root = Path(os.environ.get("LAB_LOCK_DIR", "/tmp/physics-lab"))
    return str(root / "numeric_lock.json"), str(root / "numeric_lock.guard")


def preflight(args: argparse.Namespace) -> int:
    refusals: list[str] = []

    def report(kind: str, name: str, detail: str) -> None:
        print(f"{kind:<7} {name}: {detail}")
        if kind == "refuse":
            refusals.append(name)

    free_gb = shutil.disk_usage(".").free / 1e9
    report("refuse" if free_gb < args.min_disk_gb else "ok", "disk",
           f"{free_gb:.0f} GB free, limit {args.min_disk_gb:g}")

    free_mem = memory_free_pct()
    if free_mem is None:
        report("note", "memory", "free share unknown on this machine")
    else:
        report("refuse" if free_mem < args.min_mem_pct else "ok", "memory",
               f"{free_mem:.0f}% free, limit {args.min_mem_pct:g}")

    load = os.getloadavg()[0]
    high_load = load > args.max_load
    report("refuse" if high_load and args.numeric else "note" if high_load else "ok",
           "load", f"{load:.1f}, limit {args.max_load:g}")

    if not args.target:
        report("note", "model floor", "no target named, no floor checked")
    else:
        goal = Path(args.target) / "GOAL.md"
        floors = read_floors(goal) if goal.exists() else {}
        if not floors:
            report("note", "model floor", "none declared; use the configured model")
        elif args.role not in floors:
            report("refuse", "model floor", f"name a role from {sorted(floors)}")
        elif floor_allows(floors[args.role], args.model, args.effort):
            report("ok", "model floor", f"{args.model} allowed for {args.role}")
        else:
            report("refuse", "model floor",
                   f"{args.model}@{args.effort} is not in {floors[args.role]} "
                   f"for {args.role}")

    nice_ok = run("nice", "-n", "10", "true").returncode == 0
    report("ok" if nice_ok else "refuse" if args.numeric else "note", "nice",
           "works here" if nice_ok else "not allowed in this sandbox")
    cap_ok = run("bash", "-c", "ulimit -v 4194304").returncode == 0
    report("ok" if cap_ok else "note", "memory cap",
           "ulimit works here" if cap_ok else
           "ulimit unavailable; a job must watch its own memory")
    online = git("ls-remote", "--exit-code", "origin", "HEAD", timeout=30).returncode == 0
    report("ok" if online else "note", "network", "origin reachable" if online else
           "origin not reachable from here")
    changed, _ = stale_rules(fetch=False)
    if changed is None:
        report("note", "rules", "cannot compare with origin/main here")
    elif changed:
        report("note", "rules", f"{len(changed)} rule file(s) differ from the last "
               "fetched origin/main; run lab_ops.py doctor")
    else:
        report("ok", "rules", "match the last fetched origin/main")
    if args.needs_push:
        probe = git("push", "--dry-run", "origin",
                    "HEAD:refs/heads/lab-preflight-dry-run", timeout=30)
        report("ok" if probe.returncode == 0 else "refuse", "push",
               "dry run accepted" if probe.returncode == 0 else
               "this session cannot push, so it cannot hold a lease")

    if args.numeric:
        lock_path, _ = numeric_lock_paths()
        try:
            Path(lock_path).parent.mkdir(parents=True, exist_ok=True)
            writable = os.access(Path(lock_path).parent, os.W_OK)
        except OSError:
            writable = False
        lock = automation_lock.load_lock(lock_path) if writable else None
        if not writable:
            report("refuse", "numeric lock", f"{Path(lock_path).parent} is not writable here")
        elif automation_lock.lock_is_live(lock):
            report("refuse", "numeric lock",
                   f"held by {lock.get('owner')} until {lock.get('expires_at')}")
        else:
            report("ok", "numeric lock", "free")
        unset = [name for name in THREAD_VARS if os.environ.get(name) != "1"]
        if unset:
            report("note", "threads", "export " + " ".join(f"{n}=1" for n in unset))

    print("preflight: refuse (" + ", ".join(refusals) + ")" if refusals else "preflight: go")
    return 1 if refusals else 0


def numeric_lock(args: argparse.Namespace) -> int:
    lock_path, guard_path = numeric_lock_paths()
    cli = ["--lock-path", lock_path, "--meta-lock-path", guard_path, args.action]
    if args.action != "status":
        if not args.holder:
            return refuse("--holder is required")
        cli += ["--owner", args.holder, "--holder-id", args.holder]
    if args.action == "acquire":
        cli += ["--purpose", args.purpose, "--ttl-hours", str(args.ttl_hours)]
    if args.action == "refresh":
        cli += ["--ttl-hours", str(args.ttl_hours)]
    return automation_lock.run_with_guard(automation_lock.build_parser().parse_args(cli))


# --- status ----------------------------------------------------------------


def lease_state(value: str | None, now: dt.datetime) -> str:
    if not value:
        return "no lease"
    try:
        until = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return f"unreadable lease {value}"
    if until.tzinfo is None:
        until = until.replace(tzinfo=dt.timezone.utc)
    return f"live until {value}" if until > now else f"expired {value}"


def span_hash(root: Path, ref: str) -> str | None:
    """SHA-256 of a file, or of one heading's section when ref is PATH#HEADING.

    A section runs from its heading to the next heading of the same or a
    higher level. None means the file is not there, or the heading is missing
    or appears more than once, so the reference names no single text.
    """
    path, _, heading = ref.partition("#")
    try:
        data = (root / path).read_bytes()
    except OSError:
        return None
    if not heading:
        return hashlib.sha256(data).hexdigest()
    lines = data.decode("utf-8", errors="replace").splitlines(keepends=True)
    headings: list[tuple[int, int, str]] = []
    fenced = False
    for index, line in enumerate(lines):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        found = None if fenced else HEADING_RE.match(line.rstrip("\r\n"))
        if found:
            headings.append((index, len(found[1]), found[2]))
    matches = [entry for entry in headings if entry[2] == heading]
    if len(matches) != 1:
        return None
    start, level, _ = matches[0]
    end = next((i for i, lvl, _ in headings if i > start and lvl <= level), len(lines))
    return hashlib.sha256("".join(lines[start:end]).encode()).hexdigest()


def content_hash(lines: list[str]) -> str:
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def read_check(path: Path) -> dict:
    """Front matter of one check record.

    Only the fields a record may carry are kept. Every value a field was given
    is remembered under "said", so a broken record can still be held against
    the statements it names. Whatever is wrong with the record is under "bad".
    """
    record: dict = {"file": path.name, "text": [], "reads": [], "raw": [], "bad": "",
                    "said": {}}
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        record["bad"] = f"cannot be read ({exc.__class__.__name__})"
        return record
    if not lines or lines[0] != "---":
        record["bad"] = "no front matter"
        return record
    seen: set[str] = set()
    key = ""
    for line in lines[1:]:
        if line == "---":
            return record
        if line.startswith("  - ") and key in ("text", "reads"):
            want = 2 if key == "text" else 3
            fields = line[4:].split(" ", want - 1)
            record["raw"].append(line)
            if len(fields) == want and re.fullmatch(r"[0-9a-f]{64}", fields[0]):
                record[key].append(tuple(fields))
            else:
                record["bad"] = record["bad"] or f"a {key} line is not `<sha256> ...`"
            continue
        key, colon, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if colon and key in RECORD_FIELDS:
            record["said"].setdefault(key, []).append(value)
        if not colon or key not in RECORD_FIELDS + ("text", "reads"):
            record["bad"] = record["bad"] or f"unknown line: {line.strip()[:40]}"
            key = ""
        elif key in seen:
            record["bad"] = record["bad"] or f"{key} appears twice"
        elif key in ("text", "reads"):
            if value:
                record["bad"] = record["bad"] or f"{key} takes list lines"
        else:
            record[key] = value
        seen.add(key)
    record["bad"] = "front matter is not closed"
    return record


def session_of(provenance: str) -> str:
    return provenance.split(" ", 1)[1].strip() if " " in provenance else ""


def answers_of(record: dict) -> list[str]:
    """The record files this record answers; `none` and an absent field are no files."""
    names = re.split(r"[,\s]+", record.get("answers", "none"))
    return [name for name in names if name and name != "none"]


def record_problem(record: dict) -> str | None:
    """Why a record can never count, or None. A broken record is rejected, not skipped."""
    if record["bad"]:
        return record["bad"]
    for key in REQUIRED_FIELDS:
        if not record.get(key):
            return f"{key} is missing"
    if not NAME_RE.match(record["statement"]):
        return "statement is not a name without spaces"
    if not re.fullmatch(r"[0-9a-f]{40}", record["commit"]):
        return "commit is not 40 hex digits"
    if record["verdict"] not in VERDICTS:
        return "verdict is not right, wrong or undecided"
    failure = record["failure"].split(" ")
    if record["verdict"] == "wrong":
        if failure[0] not in ("step", "counterexample") or len(failure) < 2:
            return "a wrong verdict names `step <where>` or `counterexample <where>`"
    elif failure != ["none"]:
        return "only a wrong verdict names a failure"
    if not record["text"]:
        return "text lists nothing"
    if any(name != "-" and not NAME_RE.match(name) for _, name, _ in record["reads"]):
        return "a reads line names something that is not a statement name"
    for who in ("checker", "author"):
        if not PROVENANCE_RE.match(record[who]):
            return f"{who} is not `<provider>/<model>/<effort> <session>`"
    if session_of(record["checker"]) == session_of(record["author"]):
        return "checker and author are the same session"
    if content_hash(record["raw"]) != record["content"]:
        return "content does not match the text and reads lines"
    if record["file"] in answers_of(record):
        return "a record cannot answer itself"
    return None


def live_records(records: list[dict]) -> tuple[list[dict], set[str]]:
    """The records that stand, and the files of those whose answers carry weight.

    Records that answer one another in a circle settle nothing: their answers
    are void, for setting a record aside and for lifting a block alike. Among
    the rest, a record with no answerer stands, one answered by a standing
    record is set aside, and one whose answerers are all set aside stands again.
    A record on a circle stands unless a record outside it answers it.
    """
    by_file = {r["file"]: r for r in records}
    aims = {file: [a for a in answers_of(r) if a in by_file] for file, r in by_file.items()}

    def reaches(start: str) -> bool:
        seen: set[str] = set()
        todo = list(aims[start])
        while todo:
            at = todo.pop()
            if at == start:
                return True
            if at not in seen:
                seen.add(at)
                todo.extend(aims[at])
        return False

    circular = {file for file in by_file if reaches(file)}
    answerers: dict[str, list[str]] = {file: [] for file in by_file}
    for file, targets in aims.items():
        if file not in circular:
            for aim in targets:
                answerers[aim].append(file)
    state: dict[str, bool] = {}

    def stands(file: str) -> bool:
        if file not in state:
            state[file] = not any(stands(a) for a in answerers[file])
        return state[file]

    standing = [r for r in records if stands(r["file"])]
    return standing, {r["file"] for r in standing} - circular


def compute_standing(root: Path, folder: Path,
                     names: set[str]) -> tuple[dict, Counter, list, dict]:
    """Standing from the check records in a target's checks/ folder.

    Returns the standing by statement name; by name, how many records are
    about an earlier text; the rejected records with the reason for each; and,
    by name, the records that keep it from `checked`. Those are every `wrong`
    record, current or about an earlier text, and every rejected record that
    does not plainly say `right` or `undecided`, until a live counting record
    answers them. A rejected record's own hashes are never trusted, and one
    that names no statement is held against the names its file name starts
    with. `names` are the obligation names of the target.
    """
    counting: dict[str, list[dict]] = {}
    stale: Counter = Counter()
    rejected: list[tuple[str, str]] = []
    negative: dict[str, set[str]] = {}
    for path in sorted((folder / "checks").glob("*.md")):
        record = read_check(path)
        problem = record_problem(record)
        if problem:
            rejected.append((path.name, problem))
            said = record["said"]
            if said.get("verdict") in (["right"], ["undecided"]):
                continue
            named = {n for n in said.get("statement", []) if NAME_RE.match(n)}
            for name in named or {n for n in names if path.name.startswith(f"{n}-")}:
                negative.setdefault(name, set()).add(path.name)
            continue
        name = record["statement"]
        if any(span_hash(root, e[-1]) != e[0] for e in record["text"] + record["reads"]):
            stale[name] += 1
            if record["verdict"] == "wrong":
                negative.setdefault(name, set()).add(path.name)
            continue
        counting.setdefault(name, []).append(record)
    live = {name: live_records(records) for name, records in counting.items()}
    blocked: dict[str, list[str]] = {}
    for name, files in negative.items():
        records, voiced = live.get(name, ([], set()))
        left = files - {a for r in records if r["file"] in voiced for a in answers_of(r)}
        if left:
            blocked[name] = sorted(left)
    found: dict[str, dict] = {}
    for name, (records, _) in live.items():
        wrong = [r for r in records if r["verdict"] == "wrong"]
        right = [r for r in records if r["verdict"] == "right"]
        if wrong and right:
            word = "argued"
        elif any(r["failure"].startswith("counterexample") for r in wrong):
            word = "refuted"
        elif wrong:
            word = "open"
        elif right:
            word = "argued" if name in blocked else "checked"
        else:
            continue
        reads = {e[1] for r in right for e in r["reads"] if e[1] != "-"}
        found[name] = {"word": word, "disputed": bool(wrong and right), "reads": reads}

    def rests_on(name: str, trail: frozenset[str]) -> set[str]:
        unmet: set[str] = set()
        for read in found[name]["reads"]:
            if read in trail or found.get(read, {}).get("word") != "checked":
                unmet.add(read)  # not checked, or a circle of reads
            else:
                unmet |= rests_on(read, trail | {read})
        return unmet

    for name, entry in found.items():
        entry["given"] = sorted(rests_on(name, frozenset({name}))) \
            if entry["word"] == "checked" else []
    return found, stale, rejected, blocked


def read_part(path: Path) -> dict:
    part: dict = {"lead": None, "lease": None, "counts": Counter(), "requests": [],
                  "typed": [], "legacy": [], "unreadable": [], "damaged": False}
    data = path.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        # Keep what can be read; status counts the damage as one more obligation.
        text = data.decode("utf-8", errors="replace")
        part["damaged"] = True
    section = ""
    for line in text.splitlines():
        if line.startswith("lead:") and part["lead"] is None:
            part["lead"] = line.split(":", 1)[1].strip()
        elif line.startswith("lease_until:") and part["lease"] is None:
            part["lease"] = line.split(":", 1)[1].strip()
        elif line.startswith("## "):
            section = line.strip().lower()
        elif section == "## requests" and line.startswith("- "):
            part["requests"].append(line[2:].strip())
        found = OBLIGATION_RE.match(line)
        if found and found[1] in OLD_LABELS:
            part["counts"][found[1]] += 1
            name = re.split(r"\s+given\s+|\s+->\s+", found[2], maxsplit=1)[0].strip()
            part["legacy"].append((found[1], name))
        elif found and TYPED_RE.match(found[2]):
            part["typed"].append((found[1], found[2].split()[0]))
        elif found or (section == "## obligations" and line.lstrip().startswith("-")):
            part["unreadable"].append(line.strip())
    return part


def status(args: argparse.Namespace) -> int:
    folder = Path(args.folder)
    now = dt.datetime.now(dt.timezone.utc)
    top = git("rev-parse", "--show-toplevel", cwd=folder)
    root = Path(top.stdout.strip()) if top.returncode == 0 else folder.resolve()
    parts = []
    for path in sorted((folder / "parts").glob("*.md")):
        try:
            parts.append((path, read_part(path)))
        except OSError as exc:
            print(f"unreadable part file {path.name} ({exc.__class__.__name__}), "
                  "counted as one open obligation")
            parts.append((path, {"lead": None, "lease": None, "counts": Counter(gap=1),
                                 "requests": [], "typed": [], "legacy": [],
                                 "unreadable": [], "damaged": False}))
    names = {name for _, part in parts for _, name in part["typed"] + part["legacy"]}
    standing, stale, rejected, blocked = compute_standing(root, folder, names)
    for file, reason in rejected:
        print(f"rejected check record {file}: {reason}")
    checks = folder / "checks"
    for stray in sorted(checks.iterdir()) if checks.is_dir() else []:
        if stray.suffix != ".md":
            print(f"not a check record, ignored: checks/{stray.name}")
    goal = folder / "GOAL.md"
    if goal.exists():
        head = read_part(goal)
        print(f"target lead: {head['lead'] or 'none'} ({lease_state(head['lease'], now)})")
    open_total = 0
    requests: list[str] = []
    for path, part in parts:
        counts = part["counts"]
        notes: list[str] = []
        if "--" in path.stem:
            tally = "attempt file, not counted"
        else:
            words: Counter = Counter()
            given = 0
            for typed, name in part["typed"]:
                entry = standing.get(name)
                word = entry["word"] if entry else typed
                if not entry and (stale[name] or name in blocked):
                    word = "argued"
                if entry and entry["word"] == "checked" and entry["given"]:
                    given += 1
                    circle = " (a circle of reads)" if name in entry["given"] else ""
                    notes.append(f"checked given {', '.join(entry['given'])}{circle}: {name}")
                else:
                    words[word] += 1
                if entry and entry["disputed"]:
                    notes.append(f"disputed, so argued: {name}")
                if name in blocked:
                    notes.append(f"not checked until a record answers "
                                 f"{', '.join(blocked[name])}: {name}")
                if stale[name]:
                    notes.append(f"{stale[name]} check record(s) are about an earlier "
                                 f"text: {name}")
            contradicted = 0
            for label, name in part["legacy"]:
                if label not in ("implication", "discharged"):
                    continue
                entry = standing.get(name)
                closed = entry and entry["word"] == "checked" and not entry["given"]
                if entry and not closed:
                    why = f"check records give {entry['word']}"
                elif name in blocked:
                    why = f"no record answers {', '.join(blocked[name])}"
                elif stale[name] and not closed:
                    why = f"{stale[name]} check record(s) are about an earlier text"
                else:
                    continue
                contradicted += label == "discharged"
                notes.append(f"typed {label}, but {why}: {name}")
            for line in part["unreadable"]:
                notes.append(f"unreadable obligation, counted open: {line}")
            if part["damaged"]:
                notes.append("this file is not valid UTF-8, counted as one more "
                             "open obligation")
            tally = (f"open {words['open']} argued {words['argued']} "
                     f"checked-given {given} checked {words['checked']} "
                     f"refuted {words['refuted']}")
            if part["legacy"]:
                tally += ("; typed, not computed: " + " ".join(
                    f"{label} {counts[label]}" for label in OLD_LABELS))
            open_total += (words["open"] + words["argued"] + given + contradicted
                           + len(part["unreadable"]) + part["damaged"] + counts["gap"]
                           + counts["unchecked"] + counts["implication"])
        print(f"{path.stem}: {part['lead'] or 'no lead'} "
              f"({lease_state(part['lease'], now)}); {tally}")
        for note in notes:
            print(f"  {note}")
        requests += [f"{path.stem}: {text}" for text in part["requests"]]
    print(f"open obligations: {open_total}")
    for request in requests:
        print(f"request from {request}")
    return 0


def check_hash(args: argparse.Namespace) -> int:
    top = git("rev-parse", "--show-toplevel")
    root = Path(top.stdout.strip()) if top.returncode == 0 else Path.cwd()
    lines: list[str] = []
    for ref in args.text:
        digest = span_hash(root, ref)
        if digest is None:
            return refuse(f"cannot hash {ref}: no such file, or the heading is "
                          "missing or appears more than once")
        lines.append(f"  - {digest} {ref}")
    split = len(lines)
    for item in args.reads:
        name, sep, ref = item.partition("=")
        if not sep or not (name == "-" or NAME_RE.match(name)):
            return refuse(f"--reads takes NAME=PATH[#HEADING]; NAME is a statement "
                          f"name without spaces, or -: {item}")
        digest = span_hash(root, ref)
        if digest is None:
            return refuse(f"cannot hash {ref}: no such file, or the heading is "
                          "missing or appears more than once")
        lines.append(f"  - {digest} {name} {ref}")
    print(f"content: {content_hash(lines)}")
    print("text:")
    print("\n".join(lines[:split]))
    print("reads:")
    if lines[split:]:
        print("\n".join(lines[split:]))
    return 0


# --- command line ----------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("worktree-add", help="create a sparse worktree")
    add.add_argument("name", help="worktree folder and local branch name")
    source = add.add_mutually_exclusive_group()
    source.add_argument("--target", help="target branch to join and track")
    source.add_argument("--base", default="origin/main", help="start point for new work")
    add.add_argument("--path", action="append", default=[],
                     help="extra path to check out; repeat as needed")
    add.add_argument("--dir", help="worktree location (default .claude/worktrees/NAME)")
    add.set_defaults(handler=worktree_add)

    remove = commands.add_parser("worktree-remove", help="remove a pushed worktree")
    remove.add_argument("path")
    remove.add_argument("--discard-untracked", action="store_true")
    remove.set_defaults(handler=worktree_remove)

    check = commands.add_parser("preflight", help="check before launching a job")
    check.add_argument("--target", help="target folder holding GOAL.md")
    check.add_argument("--role", help="role in the target, such as worker or checker")
    check.add_argument("--model", help="model the job will run")
    check.add_argument("--effort", help="reasoning effort the job will run")
    check.add_argument("--numeric", action="store_true", help="the job does numerics")
    check.add_argument("--needs-push", action="store_true", help="the session must push")
    check.add_argument("--min-disk-gb", type=float, default=env_float("LAB_MIN_DISK_GB", 10))
    check.add_argument("--min-mem-pct", type=float, default=env_float("LAB_MIN_MEM_PCT", 25))
    check.add_argument("--max-load", type=float,
                       default=env_float("LAB_MAX_LOAD", os.cpu_count() or 1))
    check.set_defaults(handler=preflight)

    lock = commands.add_parser("numeric-lock", help="one numeric job per machine")
    lock.add_argument("action", choices=("acquire", "refresh", "release", "status"))
    lock.add_argument("--holder", help="unique session/job identity holding the lease")
    lock.add_argument("--purpose", default="numeric job")
    lock.add_argument("--ttl-hours", type=float, default=2.0)
    lock.set_defaults(handler=numeric_lock)

    show = commands.add_parser("status", help="summarise a target folder")
    show.add_argument("folder")
    show.set_defaults(handler=status)

    hashes = commands.add_parser("check-hash", help="hash lines for a check record")
    hashes.add_argument("--text", action="append", required=True, metavar="PATH[#HEADING]",
                        help="the statement and its argument; repeat as needed")
    hashes.add_argument("--reads", action="append", default=[],
                        metavar="NAME=PATH[#HEADING]",
                        help="something the statement reads; NAME is its statement "
                             "name, or - when it is not a statement")
    hashes.set_defaults(handler=check_hash)

    fresh = commands.add_parser("doctor", help="check this checkout's rules are current")
    fresh.add_argument("--no-fetch", action="store_true",
                       help="compare with the last fetched origin/main")
    fresh.set_defaults(handler=doctor)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
