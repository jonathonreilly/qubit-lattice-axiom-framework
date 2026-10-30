#!/usr/bin/env python3
"""Mechanical helpers for docs/ai_methodology/SCIENCE_WORKFLOW.md section 10.

  worktree-add     sparse worktree on its own local branch
  worktree-remove  remove a worktree once its work is pushed
  preflight        check machine, model floor and sandbox before a launch
  numeric-lock     hold the one numeric job allowed on this machine
  status           leads, leases, requests and open obligations of a target

Machine limits come from flags or LAB_MIN_DISK_GB, LAB_MIN_MEM_PCT,
LAB_MAX_LOAD and LAB_LOCK_DIR. Exit 0 means go or done, 1 means refused, and
2 means the numeric lock is held. No scientific authority.
"""

from __future__ import annotations

import argparse
from collections import Counter
import datetime as dt
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
OBLIGATION_RE = re.compile(r"^- (gap|unchecked|implication|discharged): ")
FLOOR_RE = re.compile(r"^model_floor\s+([\w-]+):\s*(.+)$")


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


def read_part(path: Path) -> dict:
    part: dict = {"lead": None, "lease": None, "counts": Counter(), "requests": []}
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
        if found:
            part["counts"][found[1]] += 1
    return part


def status(args: argparse.Namespace) -> int:
    folder = Path(args.folder)
    now = dt.datetime.now(dt.timezone.utc)
    goal = folder / "GOAL.md"
    if goal.exists():
        head = read_part(goal)
        print(f"target lead: {head['lead'] or 'none'} ({lease_state(head['lease'], now)})")
    open_total = 0
    requests: list[str] = []
    for path in sorted((folder / "parts").glob("*.md")):
        part = read_part(path)
        counts = part["counts"]
        if "--" in path.stem:
            tally = "attempt file, not counted"
        else:
            tally = " ".join(
                f"{label} {counts[label]}"
                for label in ("gap", "unchecked", "implication", "discharged")
            )
            open_total += counts["gap"] + counts["unchecked"] + counts["implication"]
        print(f"{path.stem}: {part['lead'] or 'no lead'} "
              f"({lease_state(part['lease'], now)}); {tally}")
        requests += [f"{path.stem}: {text}" for text in part["requests"]]
    print(f"open obligations: {open_total}")
    for request in requests:
        print(f"request from {request}")
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
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
