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
    r"^- (gap|unchecked|implication|discharged|open|argued): (.+)$"
)
OLD_LABELS = ("gap", "unchecked", "implication", "discharged")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FLOOR_RE = re.compile(r"^model_floor\s+([\w-]+):\s*(.+)$")
RULE_PATHS = (
    "AGENTS.md",
    "CLAUDE.md",
    "docs/ai_methodology/RULES.md",
    "docs/ai_methodology/SETTINGS.md",
    "docs/ai_methodology/PROCEDURES.md",
    "docs/ai_methodology/procedures",
    "docs/ai_methodology/SCIENCE_WORKFLOW.md",
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
    for path in changed:
        print(f"differs: {path}")
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
    higher level. None means the file or the heading is not there.
    """
    path, _, heading = ref.partition("#")
    try:
        data = (root / path).read_bytes()
    except OSError:
        return None
    if not heading:
        return hashlib.sha256(data).hexdigest()
    kept: list[str] = []
    level = 0
    fenced = False
    for line in data.decode("utf-8", errors="replace").splitlines(keepends=True):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            found = None
        else:
            found = None if fenced else HEADING_RE.match(line.rstrip("\r\n"))
        if not level:
            if found and found[2] == heading:
                level = len(found[1])
                kept.append(line)
            continue
        if found and len(found[1]) <= level:
            break
        kept.append(line)
    return hashlib.sha256("".join(kept).encode()).hexdigest() if level else None


def content_hash(lines: list[str]) -> str:
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def read_check(path: Path) -> dict | None:
    """Front matter of one check record, or None when it has none."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return None
    record: dict = {"file": path.name, "text": [], "reads": [], "raw": [], "bad": False}
    key = ""
    for line in lines[1:]:
        if line == "---":
            return record
        if line.startswith("  - ") and key in ("text", "reads"):
            want = 2 if key == "text" else 3
            fields = line[4:].split(" ", want - 1)
            record["raw"].append(line)
            if len(fields) == want:
                record[key].append(tuple(fields))
            else:
                record["bad"] = True
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        if key not in ("text", "reads"):
            record[key] = value.strip()
    return None


def session_of(provenance: str) -> str:
    return provenance.split(" ", 1)[1].strip() if " " in provenance else ""


def record_counts(root: Path, record: dict) -> bool:
    """True while the record is intact, independent and about the current text."""
    if record["bad"] or not record["text"]:
        return False
    if content_hash(record["raw"]) != record.get("content"):
        return False
    for entry in record["text"] + record["reads"]:
        if span_hash(root, entry[-1]) != entry[0]:
            return False
    checker = session_of(record.get("checker", ""))
    return bool(checker) and checker != session_of(record.get("author", ""))


def compute_standing(root: Path, folder: Path) -> tuple[dict[str, dict], Counter]:
    """Standing of every statement that has a counting check record.

    Returns the standing by statement name and, by name, how many records no
    longer count (edited text, same session on both sides, or a broken record).
    """
    live: dict[str, list[dict]] = {}
    stale: Counter = Counter()
    for path in sorted((folder / "checks").glob("*.md")):
        record = read_check(path)
        if not record or not record.get("statement"):
            continue
        if record_counts(root, record):
            live.setdefault(record["statement"], []).append(record)
        else:
            stale[record["statement"]] += 1
    found: dict[str, dict] = {}
    for name, records in live.items():
        answered = {r.get("answers", "none") for r in records}
        records = [r for r in records if r["file"] not in answered]
        wrong = [r for r in records if r.get("verdict") == "wrong"]
        right = [r for r in records if r.get("verdict") == "right"]
        if wrong and right:
            word = "argued"
        elif any(r.get("failure", "").startswith("counterexample") for r in wrong):
            word = "refuted"
        elif wrong:
            word = "open"
        elif right:
            word = "checked"
        else:
            continue
        reads = {e[1] for r in right for e in r["reads"] if e[1] != "-"}
        found[name] = {"word": word, "disputed": bool(wrong and right), "reads": reads}

    def rests_on(name: str, seen: frozenset[str]) -> set[str]:
        unmet: set[str] = set()
        for read in found[name]["reads"]:
            if read in seen:
                continue
            if found.get(read, {}).get("word") != "checked":
                unmet.add(read)
            else:
                unmet |= rests_on(read, seen | {read})
        return unmet

    for name, entry in found.items():
        entry["given"] = sorted(rests_on(name, frozenset({name}))) \
            if entry["word"] == "checked" else []
    return found, stale


def read_part(path: Path) -> dict:
    part: dict = {"lead": None, "lease": None, "counts": Counter(), "requests": [],
                  "typed": []}
    in_requests = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("lead:") and part["lead"] is None:
            part["lead"] = line.split(":", 1)[1].strip()
        elif line.startswith("lease_until:") and part["lease"] is None:
            part["lease"] = line.split(":", 1)[1].strip()
        elif line.startswith("## "):
            in_requests = line.strip().lower() == "## requests"
        elif in_requests and line.startswith("- "):
            part["requests"].append(line[2:].strip())
        found = OBLIGATION_RE.match(line)
        if not found:
            continue
        if found[1] in OLD_LABELS:
            part["counts"][found[1]] += 1
        else:
            name = re.split(r" given | -> ", found[2], maxsplit=1)[0].strip()
            part["typed"].append((found[1], name))
    return part


def status(args: argparse.Namespace) -> int:
    folder = Path(args.folder)
    now = dt.datetime.now(dt.timezone.utc)
    top = git("rev-parse", "--show-toplevel", cwd=folder)
    root = Path(top.stdout.strip()) if top.returncode == 0 else folder.resolve()
    standing, stale = compute_standing(root, folder)
    goal = folder / "GOAL.md"
    if goal.exists():
        head = read_part(goal)
        print(f"target lead: {head['lead'] or 'none'} ({lease_state(head['lease'], now)})")
    open_total = 0
    requests: list[str] = []
    for path in sorted((folder / "parts").glob("*.md")):
        part = read_part(path)
        counts = part["counts"]
        notes: list[str] = []
        if "--" in path.stem:
            tally = "attempt file, not counted"
        else:
            words = Counter({"open": counts["gap"], "argued": counts["unchecked"],
                             "checked": counts["discharged"]})
            given = counts["implication"]
            for typed, name in part["typed"]:
                entry = standing.get(name)
                word = entry["word"] if entry else typed
                if entry and entry["word"] == "checked" and entry["given"]:
                    given += 1
                    notes.append(f"checked given {', '.join(entry['given'])}: {name}")
                else:
                    words[word] += 1
                if entry and entry["disputed"]:
                    notes.append(f"disputed, so argued: {name}")
                if stale[name]:
                    notes.append(f"{stale[name]} check record(s) no longer count: {name}")
            tally = (f"open {words['open']} argued {words['argued']} "
                     f"checked-given {given} checked {words['checked']} "
                     f"refuted {words['refuted']}")
            open_total += words["open"] + words["argued"] + given
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
            return refuse(f"cannot read {ref} under {root}")
        lines.append(f"  - {digest} {ref}")
    split = len(lines)
    for item in args.reads:
        name, sep, ref = item.partition("=")
        if not sep or " " in name:
            return refuse(f"--reads takes NAME=PATH[#HEADING], with no space in NAME: {item}")
        digest = span_hash(root, ref)
        if digest is None:
            return refuse(f"cannot read {ref} under {root}")
        lines.append(f"  - {digest} {name or '-'} {ref}")
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
