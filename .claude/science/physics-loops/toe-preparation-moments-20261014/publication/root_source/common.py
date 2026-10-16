from pathlib import Path
import datetime, hashlib, json, subprocess, time

N = Path(__file__).resolve().parents[1]
T = N.parent
W = T / "correlation_worktree"
DEADLINE = datetime.datetime(2026, 10, 15, 21, 43, 9, tzinfo=datetime.timezone.utc)

def now():
    return datetime.datetime.now(datetime.timezone.utc)

def pin(path):
    path = Path(path)
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}

def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2) + "\n")

def read_json(path):
    return json.loads(Path(path).read_text())

def check_pin(path, expected):
    actual = pin(path)
    assert actual["bytes"] == expected["bytes"] and actual["sha256"] == expected["sha256"], str(path)
    return actual

def require_campaign_active():
    assert now() < DEADLINE, "Fixed research deadline reached; preserve only."

def run(directory, label, argv, *, cwd=W, expected=(0,)):
    directory = Path(directory) / label
    directory.mkdir(parents=True, exist_ok=False)
    argv = [str(x) for x in argv]
    source = None
    if len(argv) > 1 and Path(argv[0]).name.startswith("python"):
        path = Path(argv[1])
        if not path.is_absolute():
            path = Path(cwd) / path
        if path.is_file():
            source = pin(path)
            (directory / "executed_source.py").write_bytes(path.read_bytes())
    started = now().isoformat()
    clock = time.monotonic()
    result = subprocess.run(argv, cwd=cwd, capture_output=True)
    (directory / "stdout").write_bytes(result.stdout)
    (directory / "stderr").write_bytes(result.stderr)
    receipt = {"argv": argv, "cwd": str(cwd), "start_utc": started,
               "end_utc": now().isoformat(), "elapsed_seconds": time.monotonic()-clock,
               "exit_code": result.returncode, "expected_exit_codes": list(expected),
               "stdout": pin(directory / "stdout"), "stderr": pin(directory / "stderr"),
               "python_source_at_launch": source, "recorder": pin(__file__)}
    write_json(directory / "EXECUTION.json", receipt)
    assert result.returncode in expected, str(directory)
    return result.stdout

def git_read(*args):
    return subprocess.check_output(["git", *args], cwd=W)

def require_clean_branch(branch, head):
    assert git_read("branch", "--show-current").decode().strip() == branch
    assert git_read("rev-parse", "HEAD").decode().strip() == head
    assert git_read("status", "--porcelain", "-z") == b""

def stage_exact(paths):
    require_campaign_active()
    paths = sorted(set(paths))
    assert all(not Path(x).is_absolute() and ".." not in Path(x).parts for x in paths)
    subprocess.run(["git", "add", "--", *paths], cwd=W, check=True)
    actual = git_read("diff", "--cached", "--name-only", "-z").decode().rstrip("\0").split("\0")
    assert set(actual) == set(paths), "Unexpected staged membership"
    subprocess.run(["git", "diff", "--cached", "--check"], cwd=W, check=True)
    assert git_read("diff", "--name-only", "-z") == b"", "Unstaged tracked changes"
    return {p: pin(W / p) for p in paths}
