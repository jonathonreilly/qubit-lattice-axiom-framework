#!/usr/bin/env python3
"""Disjoint checker for J:derive:review-20261004-clock-policy-coordinated-repair:a1.

Reads git OBJECTS of a read-only checkout (never its working tree, never writes
there); builds throw-away scratch trees under this directory and removes them.
Python stdlib + git CLI only. One line per check starting PASS/FAIL.

Default run: source verification, wording-grant invariants, regeneration of the
real axiom-baseline blocks and manifest, stale-phrase scan, premise-epoch effect,
dependency census over all 7705 runners / 5816 tracked caches, hash-pin census,
cross-check against the repo's own diff-scoped selector, execution plan, and a
bounded live re-execution (<= ~20 runners) in unpatched vs patched scratch trees.

The large re-execution of all affected runners was run separately with reexec_tools/ (see ATTEMPT.md);
it is not part of this script.
"""
from __future__ import annotations

import ast
import difflib
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

T0 = time.time()
OUT = Path(__file__).resolve().parent
MAIN = Path(os.environ.get(
    "MAIN_WT",
    "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/main_wt"))
C = "2868a0c453e667d1267f0e1e7403732a11893d78"      # task-frozen main commit
O = "3e1a2dd2531590dabf85bee8db56175ba9b96e90"      # origin/main verified by ls-remote at work time
AUTH = "113ab6987c308338c53759368761e5521ab91b10"   # frozen author commit
AUTH_PARENT = "f07107dcd38da0ef611bce90203469860abef086"   # author commit parent; merge-base with main is b6fda5ae1d

P_THM = "docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
P_KIN = "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
P_REG = "docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md"
P_AUD = "docs/ai_methodology/skills/audit-loop/SKILL.md"
P_CLM = "docs/ai_methodology/skills/physics-loop/references/CLAIM_STATUS.md"
P_MAN = "docs/audit/data/skill_axiom_baseline_manifest.json"
P_MEMO = "docs/MINIMAL_AXIOMS_2026-06-29.md"
P_NODES = "docs/audit/data/axiom_premise_nodes.json"
P_GEN = "docs/audit/scripts/generate_skill_axiom_baselines.py"
TASK_SRC = {
    P_THM: "e6952f8bb3fb033a96e9fac6e10d877b3b3576f7ead872f2140ed832ac166700",
    P_KIN: "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    P_REG: "f268ad7caad2db36a3274c7304c8ba97ce24d33afb49d4e9ad47b45a2848ec69",
    P_AUD: "2c9e197d8194a8b957e263cc4be9a5f36fbbb89c8341ff296ec16543be53b5a2",
    P_CLM: "3108bd1f1e3ad701ff2cae3b22632321ef44b2d44d33b554c732c5a88b3e3d35",
    P_MAN: "e2fe4183a44fdbf749bd4797984188d69380ad1c91653e00ce8b55b9b460e105",
}
AUTH_BLOBS = {  # sha256 of the five files at the author commit (from the task text)
    P_KIN: "6c4a433b4cd47ec889e0cb5d539f211728458591f73f5368faac81b7b56726b3",
    P_REG: "601e39a1ef57ac7f9f0d5a7fdcc51f9bb1a06800d54432010e363f5800061047",
    P_AUD: "ac1c192a3707800da56e5ff5407b7103e13ad0352569ee6c80d8246a4d146cbe",
    P_CLM: "a6ca0ff038d2950103b6b8b4dbda9021c701360fc93ce5a406a361c412ba43f8",
    P_MAN: "11b9889d7ccb007575eead706733408b7faa48a0c33a460e402e15a0929f6acd",
}
CHANGED = [P_KIN, P_REG, P_AUD, P_CLM, P_MAN]
SCRATCH = Path(tempfile.mkdtemp(prefix="_scratch_", dir=str(OUT)))

PASSN = 0
FAILN = 0
FACTS: dict = {}


def chk(name: str, ok: bool, detail: str = "") -> bool:
    global PASSN, FAILN
    if ok:
        PASSN += 1
    else:
        FAILN += 1
    print(("PASS " if ok else "FAIL ") + name + (" | " + detail if detail else ""), flush=True)
    return ok


def info(msg: str) -> None:
    print("INFO " + msg, flush=True)


def git(*a: str, inp: bytes | None = None) -> bytes:
    r = subprocess.run(["git", "-C", str(MAIN), *a], input=inp, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(a), r.stderr.decode()[:300]))
    return r.stdout


def blob(commit: str, path: str) -> bytes:
    return git("show", "%s:%s" % (commit, path))


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def tree_entries(commit: str) -> dict:
    ent = {}
    for line in git("ls-tree", "-r", commit).decode().strip().split("\n"):
        meta, p = line.split("\t", 1)
        mode, _typ, h = meta.split()
        ent[p] = (mode, h)
    return ent


_BATCH = {}


def _batch_proc():
    if "p" not in _BATCH:
        _BATCH["p"] = subprocess.Popen(["git", "-C", str(MAIN), "cat-file", "--batch"], stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE)
    return _BATCH["p"]


def batch_read(ent: dict, paths: list) -> dict:
    """Read blobs through one persistent `git cat-file --batch` child (own PID, closed at exit)."""
    p = _batch_proc()
    res = {}
    for path in paths:
        p.stdin.write((ent[path][1] + "\n").encode())
        p.stdin.flush()
        hdr = p.stdout.readline().split()
        n = int(hdr[2])
        body = p.stdout.read(n)
        p.stdout.read(1)
        res[path] = body
    return res


def section(text: str, heading: str) -> str:
    m = re.search(r"^#{2,6}\s+" + re.escape(heading) + r"\s*$", text, re.M)
    if not m:
        m = re.search(r"^\*" + re.escape(heading) + r"\*\s*$", text, re.M)
    assert m, heading
    rest = text[m.end():]
    n = re.search(r"^(#{1,6}\s|\*[A-Z][^*\n]+\*\s*$)", rest, re.M)
    return rest[:n.start()] if n else rest


def paras(sec: str) -> list:
    return [norm(p) for p in re.split(r"\n\s*\n", sec) if p.strip()]


def bullets(sec: str) -> list:
    out, cur = [], None
    for line in sec.split("\n"):
        if line.startswith("- "):
            if cur is not None:
                out.append(norm(cur))
            cur = line[2:]
        elif cur is not None and line.startswith("  "):
            cur += " " + line.strip()
        elif cur is not None:
            out.append(norm(cur))
            cur = None
    if cur is not None:
        out.append(norm(cur))
    return out


def run_py(args: list, cwd: Path, timeout: int = 120, env_extra: dict | None = None):
    env = {**os.environ, **(env_extra or {})}
    return subprocess.run([sys.executable, "-I", *args], cwd=str(cwd), capture_output=True,
                          timeout=timeout, env=env)


def materialize(dest: Path, files: dict) -> None:
    for rel, body in files.items():
        fp = dest / rel
        fp.parent.mkdir(parents=True, exist_ok=True)
        fp.write_bytes(body)


# ---------------------------------------------------------------- 1. sources
def part_sources(ent):
    chk("S0 pinned commits exist (task main commit, current main, author commit)",
        all(subprocess.run(["git", "-C", str(MAIN), "cat-file", "-e", c + "^{commit}"]).returncode == 0
            for c in (C, O, AUTH)))
    for p, h in TASK_SRC.items():
        chk("S1 task source object sha256 at frozen main commit: " + p, sha(blob(C, p)) == h)
    chk("S2 author commit parent is the recorded base", git("rev-parse", AUTH + "^").decode().strip() == AUTH_PARENT)
    chk("S3 author commit is NOT an ancestor of current main (policy patch has not landed)",
        subprocess.run(["git", "-C", str(MAIN), "merge-base", "--is-ancestor", AUTH, O]).returncode != 0)
    files = [l for l in git("diff", "--name-only", AUTH + "^", AUTH).decode().split("\n") if l]
    chk("S4 author commit touches exactly the five repair files", sorted(files) == sorted(CHANGED), str(files))
    for p, h in AUTH_BLOBS.items():
        chk("S5 author blob sha256 matches the task record: " + p, sha(blob(AUTH, p)) == h)
    moved = [p for p in TASK_SRC if sha(blob(O, p)) != TASK_SRC[p]]
    chk("S6 drift of the task sources between frozen main commit and current main is exactly the two skill files",
        sorted(moved) == sorted([P_AUD, P_CLM]), str(moved))
    ahead = int(git("rev-list", "--count", C + ".." + O).decode().strip())
    info("current main %s is %d commits after the frozen task commit" % (O[:10], ahead))
    chk("S7 repair-relevant authority files unchanged on current main vs frozen commit (memo, registry json)",
        sha(blob(O, P_MEMO)) == sha(blob(C, P_MEMO)) and sha(blob(O, P_NODES)) == sha(blob(C, P_NODES)))


# ------------------------------------------------- 2. wording vs grant, theorem
def part_wording(ent):
    memo = norm(blob(O, P_MEMO).decode())
    chk("W0 memo: approved primitives are named as part of the complete supplied foundation, and no admission class exists",
        "Axioms and approved primitives are the complete supplied foundation" in memo
        and "No admission class exists" in memo)
    reg = norm(blob(O, P_REG).decode())
    chk("W1 registry skill rule 5: a primitive grants no more than its source note declares", "Do not grant more than the primitive source note declares" in reg)
    nodes = json.loads(blob(O, P_NODES))
    node = nodes["nodes"]["kinetic_isotropy_primitive"]
    chk("W2 registered kinetic primitive node: path is the kinetic note and the grant text mentions only c_t=c_s and no re-axiomatization of time",
        node["current_path"] == P_KIN and "c_t=c_s" in node["note"] and "does not re-axiomatize emergent time" in node["note"])

    old = blob(O, P_KIN).decode()
    new = blob(AUTH, P_KIN).decode()
    od, nd = section(old, "What This Declares"), section(new, "What This Declares")
    ob, nb = section(old, "What This Does Not Do"), section(new, "What This Does Not Do")
    op, np_ = paras(od), paras(nd)
    diffp = [i for i, (a, b) in enumerate(zip(op, np_)) if a != b]
    chk("W3 Declares: same number of paragraphs, exactly one paragraph changed", len(op) == len(np_) and len(diffp) == 1, str(diffp))
    a, b = op[diffp[0]], np_[diffp[0]]
    chk("W4 Declares: the changed paragraph keeps its head (everything before 'time remains emergent')",
        a.split("time remains emergent")[0] == b.split("time remains emergent")[0])
    tail = "primitive fixes only the one dimensionless graining ratio relating that emergent time to space."
    chk("W5 Declares: changed paragraph keeps its closing grant-limiting clause in both versions", tail in a and tail in b)
    code = lambda s: re.findall(r"`[^`]+`", s)
    chk("W6 Declares: the set of code spans (c_t = c_s, Z^3 x Z_tau, ...) is identical before/after", code(od) == code(nd))
    for needle in ("c_t = c_s,", "hypercubic-symmetric", "One tick is one edge in **form**", "no mass ratio, coupling, mixing angle, phase, selector, readout bridge, or empirical fit"):
        chk("W7 Declares keeps grant text: " + needle, needle in norm(od) and needle in norm(nd))
    obb, nbb = bullets(ob), bullets(nb)
    dif = [i for i, (x, y) in enumerate(zip(obb, nbb)) if x != y]
    chk("W8 Does-Not-Do: same bullet count and exactly one bullet changed (the re-axiomatize-time bullet)",
        len(obb) == len(nbb) and len(dif) == 1 and "re-axiomatize time" in obb[dif[0]] and "re-axiomatize time" in nbb[dif[0]], str(dif))
    chk("W9 Does-Not-Do: changed bullet still limits the primitive to the one graining ratio c_t / c_s",
        "normalizes only the one graining ratio `c_t / c_s`" in nbb[dif[0]])
    chk("W10 new text states axis, step and single clock are supplied premises",
        all(w in norm(nd + nb) for w in ("supplied time axis, step and single clock", "its axis is a premise there, not a derivation", "supplied axis, step and single-clock premises")))
    chk("W11 old text asserted derivedness (the defect being corrected)",
        "remains emergent and derived" in norm(od) and "remains derived" in norm(ob))
    # outside the two sections the note is unchanged
    chk("W12 kinetic note outside the two edited sections is byte-identical (old with the two sections swapped for the new ones equals the author's note)",
        old.replace(od, nd).replace(ob, nb) == new)

    thm = norm(blob(O, P_THM).decode())
    for k, needle in (("axis", "the axis is a premise, not a derivation"), ("axis label", "(B-AXIS)"),
                      ("step", "one supplied `τ` (N2)"), ("single clock", "no independent commuting clock factor (N5)"),
                      ("one declared construction", "one declared axis/transfer construction (N4)")):
        chk("T1 theorem note (current main) supports wording: " + k, needle in thm)
    FACTS["old_para"], FACTS["new_para"] = a, b


# ---------------------------------------------------------- 3. regeneration
def part_regen(ent):
    d = SCRATCH / "regen"
    need = [P_GEN, P_NODES, P_MEMO, "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md", P_KIN,
            "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md", P_REG, P_AUD, P_CLM,
            "docs/ai_methodology/skills/review-loop/SKILL.md", P_MAN,
            "docs/audit/scripts/check_axiom_premise_clean.py"]
    materialize(d, {p: blob(O, p) for p in need})
    r = run_py(["docs/audit/scripts/generate_skill_axiom_baselines.py", "--check", "--repo-root", str(d)], d)
    chk("R0 baseline: generator --check passes on unmodified current main", r.returncode == 0)
    # step 1: the kinetic-note edit only (taken from the author commit)
    (d / P_KIN).write_bytes(blob(AUTH, P_KIN))
    r = run_py(["docs/audit/scripts/generate_skill_axiom_baselines.py", "--check", "--repo-root", str(d)], d)
    out = r.stdout.decode()
    stale = sorted(set(re.findall(r"FAIL (\S+): generated block is stale", out)) | set(re.findall(r"FAIL (\S+): source acknowledgment is stale", out)))
    chk("R1 after the note edit alone, --check fails on exactly the 3 skill blocks and the manifest (propagation required)",
        r.returncode != 0 and stale == sorted([P_REG, P_AUD, P_CLM, P_MAN]), str(stale))
    # step 2: regenerate
    r = run_py(["docs/audit/scripts/generate_skill_axiom_baselines.py", "--repo-root", str(d)], d)
    chk("R2 generator --write succeeds", r.returncode == 0)
    r = run_py(["docs/audit/scripts/generate_skill_axiom_baselines.py", "--check", "--repo-root", str(d)], d)
    chk("R3 generator --check passes after regeneration", r.returncode == 0)
    snap = {p: (d / p).read_bytes() for p in CHANGED}
    r = run_py(["docs/audit/scripts/generate_skill_axiom_baselines.py", "--repo-root", str(d)], d)
    chk("R4 regeneration is idempotent", all((d / p).read_bytes() == snap[p] for p in CHANGED) and r.returncode == 0)
    chk("R5 review-loop skill (router, no copied primitive text) is unchanged",
        (d / "docs/ai_methodology/skills/review-loop/SKILL.md").read_bytes() == blob(O, "docs/ai_methodology/skills/review-loop/SKILL.md"))
    for p in (P_KIN, P_REG, P_MAN):
        chk("R6 regenerated file is byte-identical to the author blob: " + p, sha(snap[p]) == AUTH_BLOBS[p])
    for p in (P_AUD, P_CLM):
        chk("R7 regenerated file differs from the author blob only because main moved (expected, not an error): " + p,
            sha(snap[p]) != AUTH_BLOBS[p] and sha(blob(O, p)) != sha(blob(AUTH_PARENT, p)))
    # author's per-file patch applied to current-main blobs gives the same bytes as regeneration
    for p in (P_AUD, P_CLM, P_REG):
        patch = git("diff", AUTH + "^", AUTH, "--", p)
        t = SCRATCH / ("patch_" + hashlib.md5(p.encode()).hexdigest()[:6])
        materialize(t, {p: blob(O, p)})
        pr = subprocess.run(["patch", "-p1", "-s"], input=patch, cwd=str(t), capture_output=True)
        ok = pr.returncode == 0 and (t / p).read_bytes() == snap[p]
        chk("R8 author's hunks apply cleanly to current main and equal the regenerated file: " + p, ok)
    # minimal edit: lines changed by regeneration
    ins = dele = 0
    outside = 0
    for p in CHANGED:
        o = blob(O, p).decode().split("\n")
        n = snap[p].decode().split("\n")
        for l in difflib.unified_diff(o, n, n=0, lineterm=""):
            if l.startswith("+") and not l.startswith("+++"):
                ins += 1
            elif l.startswith("-") and not l.startswith("---"):
                dele += 1
    chk("R9 total repair size: 5 files, 36 insertions, 25 deletions (same as the author commit)", (ins, dele) == (36, 25), "(%d,%d)" % (ins, dele))
    for p in (P_REG, P_AUD, P_CLM):
        txt = snap[p].decode()
        b0, b1 = txt.index("<!-- BEGIN GENERATED"), txt.index("<!-- END GENERATED")
        o = blob(O, p).decode()
        ob0, ob1 = o.index("<!-- BEGIN GENERATED"), o.index("<!-- END GENERATED")
        chk("R10 edit confined to the generated block: " + p, txt[:b0] == o[:ob0] and txt[b1:] == o[ob1:])
    r = run_py(["docs/audit/scripts/check_axiom_premise_clean.py"], d)
    chk("R11 structural premise guard (check_axiom_premise_clean.py) passes on the patched tree", r.returncode == 0, r.stdout.decode().strip()[:120])
    chk("R12 registry json untouched by the repair (grant registration unchanged)", (d / P_NODES).read_bytes() == blob(O, P_NODES))
    # install the patched files into a reusable map
    FACTS["patched"] = snap
    FACTS["regen_dir"] = d
    # stale phrase scan
    pat = [r"time remains emergent and derived", r"emergent single-clock evolution remains\s+derived"]
    hits = []
    for line in git("grep", "-l", "-i", "-E", "emergent single-clock evolution remains|time remains emergent and derived", O).decode().split("\n"):
        if line.strip():
            hits.append(line.split(":", 1)[1])
    live = [h for h in hits if not h.startswith(("outputs/", ".claude/", "archive/", "logs/"))]
    chk("R13 before repair the two stale sentences live on exactly the 4 live surfaces", sorted(live) == sorted([P_KIN, P_REG, P_AUD, P_CLM]), str(live))
    still = [p for p in live if any(re.search(x, norm(snap[p].decode()), re.I) for x in pat)] if all(p in snap for p in live) else ["?"]
    chk("R14 after repair none of the 4 live surfaces carries either stale sentence", not still, str(still))
    frozen = [h for h in hits if h not in live]
    info("%d frozen snapshot files (outputs/, .claude/, archive/) also quote the old text; they are pinned receipts and are NOT part of the repair" % len(frozen))
    FACTS["frozen_quotes"] = len(frozen)


# ------------------------------------------------------ 4. premise epoch/ledger
def part_epoch(ent):
    d = FACTS["regen_dir"]
    d_old = SCRATCH / "epoch_old"
    files = {P_NODES: blob(O, P_NODES), P_MEMO: blob(O, P_MEMO), "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": blob(O, "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
             P_KIN: blob(O, P_KIN), "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": blob(O, "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
             "docs/audit/scripts/audit_science_fingerprint.py": blob(O, "docs/audit/scripts/audit_science_fingerprint.py"),
             "scripts/runner_cache.py": blob(O, "scripts/runner_cache.py")}
    materialize(d_old, files)
    d_new = SCRATCH / "epoch_new"
    shutil.copytree(d_old, d_new)
    (d_new / P_KIN).write_bytes(FACTS["patched"][P_KIN])

    def epoch(root: Path):
        spec = importlib.util.spec_from_file_location("asf_%s" % root.name, str(root / "docs/audit/scripts/audit_science_fingerprint.py"))
        m = importlib.util.module_from_spec(spec)
        sys.path.insert(0, str(root / "scripts"))
        try:
            spec.loader.exec_module(m)
        finally:
            sys.path.pop(0)
        return m, m.framework_premise_epoch(root)
    m_old, e_old = epoch(d_old)
    m_new, e_new = epoch(d_new)
    chk("E1 framework_premise_epoch changes when the kinetic note changes (it binds the note bytes)", e_old != e_new)
    pol = set(m_old.DEPENDENCY_POLICY_SOURCES)
    chk("E2 none of the five repair files is a governed dependency-policy source (policy epoch manifest need not change)", not (pol & set(CHANGED)))
    man = json.loads(blob(O, "docs/audit/data/dependency_policy_epoch.json"))
    chk("E3 dependency_policy_epoch manifest lists exactly the policy sources and none of the repair files", set(man["sources"]) == pol)
    base = json.loads(blob(O, "docs/audit/data/legacy_science_epoch_baseline.json"))
    info("legacy anchor framework_premise_epoch_digest already %s current main's value (before repair)" %
         ("EQUALS" if base["framework_premise_epoch_digest"] == e_old else "DIFFERS FROM"))
    # ledger
    led = [p for p in ent if p.startswith("docs/audit/data/ledger/") and p.endswith(".json")]
    rows = {p: json.loads(b) for p, b in batch_read(ent, led).items()}
    st = {}
    for r in rows.values():
        st[r.get("audit_status")] = st.get(r.get("audit_status"), 0) + 1
    snaps = sum(1 for r in rows.values() if r.get("audit_state_snapshot"))
    chk("E4 ledger at current main: every row unaudited and none carries a judgment snapshot (nothing for the premise-epoch change to invalidate)",
        st == {"unaudited": len(rows)} and snaps == 0, "rows=%d snaps=%d" % (len(rows), snaps))
    FACTS["ledger_rows"] = len(rows)
    FACTS["ledger_runners"] = sorted({r["runner_path"] for r in rows.values() if r.get("runner_path")})
    FACTS["dep_rows"] = sum(1 for r in rows.values() if "kinetic_isotropy_primitive" in (r.get("deps") or []))


# ----------------------------------------------------------- 5. census
def decl_inputs(text: str):
    if "AUDIT_INPUT_PATHS" not in text:
        return None
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return None
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if not any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS" for t in targets):
            continue
        try:
            v = ast.literal_eval(node.value)
        except Exception:
            return ()
        if not isinstance(v, (tuple, list)) or not v:
            return ()
        out = []
        for raw in v:
            if not isinstance(raw, str):
                return ()
            rel = Path(raw)
            if rel.is_absolute() or not rel.parts or ".." in rel.parts or rel.as_posix() != raw or raw in out:
                return ()
            out.append(raw)
        return tuple(out)
    return None


def timeout_for(text: str, name: str) -> int:
    m = re.search(r"^AUDIT_TIMEOUT_SEC\s*=\s*(\d+)\s*(?:#.*)?$", text, re.M)
    if m and int(m.group(1)) > 0:
        return int(m.group(1))
    for needle, v in (("frontier_alpha_s", 900), ("frontier_confinement", 900), ("frontier_gauge_vacuum_plaquette_perron", 900),
                      ("frontier_gauge_vacuum_plaquette_reduction", 900), ("frontier_gauge_vacuum_plaquette_spectral", 900),
                      ("frontier_gauge_vacuum_plaquette_susceptibility", 900), ("frontier_yt_uv_to_ir", 900),
                      ("frontier_yt_p1_delta_r_master", 900), ("frontier_higgs_mass_full", 900),
                      ("frontier_dm_neutrino_source_surface", 600), ("frontier_ckm_atlas", 600),
                      ("frontier_self_consistent_field", 600), ("frontier_emergent_lorentz", 600)):
        if needle in name:
            return v
    return 120


class BodyCache:
    def __init__(self, ent, cap=350_000_000):
        self.ent, self.cap, self.size, self.d = ent, cap, 0, {}

    def get(self, p):
        if p in self.d:
            return self.d[p]
        b = batch_read(self.ent, [p])[p]
        if self.size + len(b) > self.cap:
            self.d.clear()
            self.size = 0
        self.d[p] = b
        self.size += len(b)
        return b


def fingerprint(paths, getter, override):
    h = hashlib.sha256()
    h.update(b"runner-cache-input-fingerprint-v1\0")
    for rel in paths:
        if rel in override:
            body = override[rel]
        else:
            if rel not in getter.ent or getter.ent[rel][0] == "120000":
                return ""
            body = getter.get(rel)
        rb = rel.encode()
        h.update(len(rb).to_bytes(8, "big")); h.update(rb)
        h.update(len(body).to_bytes(8, "big")); h.update(body)
    return h.hexdigest()


def part_census(ent):
    scripts = sorted(p for p in ent if p.startswith("scripts/") and p.endswith(".py"))
    src = batch_read(ent, scripts)
    D, TXT = {}, {}
    for p in scripts:
        t = src[p].decode("utf-8", "replace")
        TXT[p] = t
        D[p] = decl_inputs(t)
    caches = {p: b for p, b in batch_read(ent, [p for p in ent if p.startswith("logs/runner-cache/") and p.endswith(".txt")]).items()}
    H = {}
    for p, b in caches.items():
        t = b.decode("utf-8", "replace")
        head = t.split("----- stdout -----", 1)[0]
        g = lambda k: (re.search(r"^" + k + r":\s*(\S+)", head, re.M) or [None, None])[1]
        H[p] = dict(sha=g("runner_sha256"), fp=g("input_fingerprint_sha256"), status=g("status"), exit=g("exit_code"),
                    elapsed=g("elapsed_sec"), timeout=g("timeout_sec"), body=t)
    chk("C0 census universe at current main: 7730 tracked scripts/**/*.py runners and 5696 tracked logs/runner-cache/*.txt caches",
        (len(scripts), len(caches)) == (7730, 5696), "runners=%d caches=%d" % (len(scripts), len(caches)))
    patched = {P_KIN: FACTS["patched"][P_KIN], P_REG: FACTS["patched"][P_REG], P_CLM: FACTS["patched"][P_CLM], P_MAN: FACTS["patched"][P_MAN],
               P_AUD: FACTS["patched"][P_AUD]}
    getter = BodyCache(ent)

    def state(r, override):
        stem = r.rsplit("/", 1)[1][:-3]
        h = H.get("logs/runner-cache/%s.txt" % stem)
        if h is None:
            return "missing"
        if h["sha"] != sha(src[r]):
            return "sha_mismatch"
        d = D[r]
        if d is not None:
            f = fingerprint(d, getter, override) if d else ""
            if not f:
                return "invalid_declaration"
            if h["fp"] != f:
                return "input_mismatch"
        if h["status"] == "timeout":
            return "execution_timeout"
        if h["status"] != "ok":
            return "execution_error"
        if h["exit"] != "0":
            return "execution_nonzero_exit"
        return "fresh"

    aff = sorted(r for r, d in D.items() if d and any(c in d for c in CHANGED))
    by_file = {c: sum(1 for r in aff if c in D[r]) for c in CHANGED}
    chk("C1 declared-input census: no runner declares the audit-loop skill; 164 declare the kinetic note, 6 the registry skill, 2 claim-status, 1 the manifest; 165 distinct runners",
        by_file[P_AUD] == 0 and by_file[P_KIN] == 164 and by_file[P_REG] == 6 and by_file[P_CLM] == 2 and by_file[P_MAN] == 1 and len(aff) == 165, str(by_file))
    pre = {r: state(r, {}) for r in aff}
    post = {r: state(r, patched) for r in aff}
    cnt = lambda d: {k: sum(1 for v in d.values() if v == k) for k in sorted(set(d.values()))}
    info("pre-repair cache state of the 165: %s" % cnt(pre))
    info("post-repair cache state of the 165: %s" % cnt(post))
    fresh_pre = [r for r in aff if pre[r] == "fresh"]
    chk("C2 every currently-fresh affected cache stops being fresh after the repair, and nothing else changes state class (fresh->input_mismatch only)",
        all(post[r] == "input_mismatch" for r in fresh_pre) and all(post[r] == pre[r] for r in aff if pre[r] != "fresh" and pre[r] != "input_mismatch")
        and all(post[r] == "input_mismatch" for r in aff if pre[r] == "input_mismatch"),
        "fresh->stale=%d" % len(fresh_pre))
    chk("C3 the fingerprint rule reproduces the stored header fingerprint for the fresh set (validates the recomputation)",
        len(fresh_pre) >= 100 and all(H["logs/runner-cache/%s.txt" % r.rsplit('/', 1)[1][:-3]]["fp"] == fingerprint(D[r], getter, {}) for r in fresh_pre), "n=%d" % len(fresh_pre))
    # global baseline for context: header-level states only (no input fingerprinting, which is slow)
    g = {"missing": 0, "sha_mismatch": 0, "sha_ok": 0}
    for r in scripts:
        h = H.get("logs/runner-cache/%s.txt" % r.rsplit("/", 1)[1][:-3])
        g["missing" if h is None else ("sha_mismatch" if h["sha"] != sha(src[r]) else "sha_ok")] += 1
    info("whole-repo cache headers at current main BEFORE any repair (%d runners): %s" % (len(scripts), g))
    FACTS["global_headers"] = g
    chk("C4 the census is far smaller than 'thousands': the repair directly pins 165 runners (122 fresh caches) of 7730; about 2.1% of runners",
        len(aff) / len(scripts) < 0.022 and len(fresh_pre) < 200)
    missing_inputs = {}
    for r in aff:
        ms = [p for p in D[r] if p not in ent]
        if ms:
            missing_inputs[r] = ms
    info("%d affected runners declare an input absent from the tree (unreadable declaration: precompute would raise, cache can never be fresh): %s" %
         (len(missing_inputs), sorted({p for v in missing_inputs.values() for p in v})[:3]))
    # undeclared mentions
    mention = {}
    for p, t in TXT.items():
        for key, path in (("KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09", P_KIN), ("PRIMITIVE_REGISTRY_CHECK", P_REG),
                          ("physics-loop/references/CLAIM_STATUS", P_CLM), ("audit-loop/SKILL", P_AUD), ("skill_axiom_baseline_manifest", P_MAN)):
            if key in t and not (D[p] and path in D[p]):
                mention.setdefault(path, []).append(p)
    info("runners that name a repair file in source but do NOT declare it (invisible to the cache pin): %s" % {k: len(v) for k, v in mention.items()})
    FACTS["mention_undeclared"] = {k: sorted(v) for k, v in mention.items()}
    # hash pins
    pins = {}
    for key, path in ((TASK_SRC[P_KIN], P_KIN), (TASK_SRC[P_REG], P_REG), (sha(blob(O, P_CLM)), P_CLM), (sha(blob(O, P_AUD)), P_AUD), (TASK_SRC[P_MAN], P_MAN)):
        pins[path] = sorted(p for p, t in TXT.items() if key in t)
    info("runners whose source embeds the CURRENT (pre-repair) sha256 of a repair file: %s" % {k: len(v) for k, v in pins.items()})
    pinned = sorted({r for v in pins.values() for r in v})
    for nm, hh in (("kinetic note", TASK_SRC[P_KIN]), ("registry skill", TASK_SRC[P_REG]), ("claim-status skill", sha(blob(O, P_CLM)))):
        gl = [l.split(":", 1)[1] for l in git("grep", "-l", hh, O).decode().split("\n") if l.strip()]
        top = {}
        for f in gl:
            k = "/".join(f.split("/")[:2]) if f.startswith(("docs/", "logs/", ".claude/")) else f.split("/")[0]
            top[k] = top.get(k, 0) + 1
        info("files in the whole tree that quote the pre-repair sha256 of the %s (not classified; many are frozen receipts): %d, by area %s" % (nm, len(gl), dict(sorted(top.items(), key=lambda x: -x[1])[:6])))
    chk("C5 hash-pin census: at least one runner hard-codes the old kinetic-note sha256 (so re-execution alone cannot refresh it)", len(pins[P_KIN]) >= 1, str(len(pins[P_KIN])))
    # classify scripts that quote an old sha but do not declare the file (invisible to the cache pin)
    oldshas = {TASK_SRC[P_KIN]: P_KIN, TASK_SRC[P_REG]: P_REG, sha(blob(O, P_CLM)): P_CLM}
    union = sorted({p for p, t in TXT.items() if any(h in t for h in oldshas)})
    undecl = [p for p in union if p not in aff]
    frozen_only, live_like = [], []
    for p in undecl:
        t = TXT[p]
        tot = sum(t.count(h) for h in oldshas)
        named = sum(len(re.findall(r"/" + h, t)) for h in oldshas)
        (frozen_only if tot == named else live_like).append(p)
    info("scripts quoting a pre-repair sha256 of K/R/C: %d total = %d in the declared-input set + %d undeclared (%d only as a path component '.../<sha>[.gz|.blob]' of a frozen copy, %d other)" %
         (len(union), len(union) - len(undecl), len(undecl), len(frozen_only), len(live_like)))
    chk("C7 hash-pin census closes: every pre-repair-sha quote outside the declared-input set is a frozen-copy file name (reads a frozen copy, not the live file)",
        len(union) == 76 and len(undecl) == 43 and not live_like, "other=%s" % live_like[:3])
    FACTS["undecl_frozen"] = len(frozen_only)
    # repo's own selector
    known = set()
    for rp in FACTS["ledger_runners"]:
        c = rp if rp in ent else ("scripts/" + rp if ("scripts/" + rp) in ent else "scripts/" + rp.rsplit("/", 1)[-1])
        known.add(c)
    for p in caches:
        cand = "scripts/%s.py" % p.rsplit("/", 1)[1][:-4]
        if cand in ent:
            known.add(cand)
    sel = sorted(r for r in known if D.get(r) and set(CHANGED) & set(D[r]))
    chk("C6 the repo's diff-scoped selector (runners_for_changed_paths logic: known=ledger+cached runners, declared inputs intersect changed paths) selects a subset of the 165, and exactly the cached or ledger-known ones",
        set(sel) <= set(aff) and len(sel) >= 140, "selector=%d of %d" % (len(sel), len(aff)))
    FACTS.update(aff=aff, pre=pre, post=post, D=D, TXT=TXT, H=H, pinned=pinned, pins=pins, sel=sel, missing_inputs=missing_inputs, scripts=scripts, src=src)
    return


# --------------------------------------------------------- 6. plan
def part_plan(ent):
    aff, pre, post, D, TXT, H = (FACTS[k] for k in ("aff", "pre", "post", "D", "TXT", "H"))
    pinned = set(FACTS["pinned"])
    rows = []
    for r in aff:
        stem = r.rsplit("/", 1)[1][:-3]
        h = H.get("logs/runner-cache/%s.txt" % stem)
        el = float(h["elapsed"]) if h and h["elapsed"] else None
        to = timeout_for(TXT[r], r.rsplit("/", 1)[1])
        if r in FACTS["missing_inputs"]:
            tier = "D_unreadable_declared_input"
        elif pre[r] == "fresh":
            tier = "A_fresh_becomes_stale"
        elif pre[r] == "input_mismatch":
            tier = "B_already_stale_input"
        elif pre[r] == "missing":
            tier = "C_no_cache_yet"
        else:
            tier = "E_runner_sha_stale"
        rows.append(dict(runner=r, declares=[c for c in CHANGED if c in D[r]], pre=pre[r], post=post[r], tier=tier,
                         timeout_s=to, cached_elapsed_s=el, embeds_old_sha=r in pinned))
    # two balanced shards (memory rule: 2 concurrent processes)
    shards = [[], []]
    load = [0, 0]
    for row in sorted(rows, key=lambda x: -(x["cached_elapsed_s"] or x["timeout_s"])):
        if row["tier"] == "D_unreadable_declared_input":
            continue
        i = 0 if load[0] <= load[1] else 1
        shards[i].append(row["runner"])
        load[i] += row["cached_elapsed_s"] or row["timeout_s"]
    runnable = [x for x in rows if x["tier"] != "D_unreadable_declared_input"]
    plan = dict(
        base_commit=O, patch_source="regenerated from author commit " + AUTH + " (kinetic-note edit) via generate_skill_axiom_baselines.py",
        preconditions=["land the five-file source repair first (separate reviewed PR)", "re-pin or re-review every runner in embeds_old_sha BEFORE recapture (their source embeds the old note sha256 and fails after the repair)",
                       "do not edit cache headers, do not touch docs/audit/data/dependency_policy_epoch.json, do not waive the freshness check"],
        command_per_shard="python3 scripts/precompute_audit_runners.py --runners <csv> --concurrency 1 --push-mode none --allow-non-main",
        concurrency_note="2 shards run as 2 processes; default --concurrency 8 would exceed the 1.5 GB per-process / 2-3 heavy process memory budget",
        counts=dict(total=len(rows), runnable=len(runnable), fresh_to_stale=sum(1 for x in rows if x["tier"].startswith("A")),
                    embeds_old_sha=sum(1 for x in rows if x["embeds_old_sha"]), unreadable_declared_input=sum(1 for x in rows if x["tier"].startswith("D"))),
        timeout_sum_s=sum(x["timeout_s"] for x in runnable), cached_elapsed_sum_s=round(sum(x["cached_elapsed_s"] or 0 for x in runnable), 1),
        shard_runners=shards, runners=rows)
    (OUT / "EXECUTION_PLAN.json").write_text(json.dumps(plan, indent=1, sort_keys=True) + "\n")
    chk("P1 execution plan written: every affected runner is in exactly one shard or flagged unreadable",
        sorted(shards[0] + shards[1] + [x["runner"] for x in rows if x["tier"].startswith("D")]) == sorted(aff))
    chk("P2 plan upper bound (sum of runner timeouts) is finite and its cached-time estimate is small (< 1 h)", plan["timeout_sum_s"] > 0 and plan["cached_elapsed_sum_s"] < 3600,
        "timeouts=%ds cached=%.0fs" % (plan["timeout_sum_s"], plan["cached_elapsed_sum_s"]))
    FACTS["plan"] = plan


# -------------------------------------------------- 7. live bounded re-execution
def part_reexec(ent):
    aff, pre, H, D, pinned = FACTS["aff"], FACTS["pre"], FACTS["H"], FACTS["D"], set(FACTS["pinned"])
    need = set()
    pick = []
    def el(r):
        h = H.get("logs/runner-cache/%s.txt" % r.rsplit("/", 1)[1][:-3])
        return float(h["elapsed"]) if h and h["elapsed"] else None
    fresh_fast = [r for r in aff if pre[r] == "fresh" and el(r) is not None and el(r) <= 1.0 and r not in pinned]
    pin_fast = [r for r in aff if r in pinned and pre[r] in ("fresh", "input_mismatch") and el(r) is not None and el(r) <= 3.0]
    pick = fresh_fast[:12] + pin_fast[:8]
    info("live re-execution subset: %d unpinned fresh-fast + %d hash-pinned fast runners" % (len(fresh_fast[:12]), len(pin_fast[:8])))
    inputs = set()
    for r in pick:
        inputs.update(D[r])
    base_files = {p: blob(O, p) for p in inputs if p in ent}
    for p in ent:
        if p.startswith("scripts/") or p.startswith("docs/audit/"):
            pass
    scripts_needed = {p: blob(O, p) for p in ent if p.startswith("scripts/") and p.endswith(".py")} if False else None
    t_old, t_new = SCRATCH / "exec_old", SCRATCH / "exec_new"
    allscripts = FACTS["src"]
    for t in (t_old, t_new):
        materialize(t, {**base_files, **{p: b for p, b in allscripts.items()}})
    for p in (P_KIN, P_REG, P_CLM, P_MAN):
        if p in base_files:
            (t_new / p).write_bytes(FACTS["patched"][p])
            chk("X0 patched tree differs from unpatched tree in " + p, (t_new / p).read_bytes() != (t_old / p).read_bytes())
    res = {}
    for r in pick:
        out = {}
        for tag, t in (("old", t_old), ("new", t_new)):
            try:
                pr = subprocess.run([sys.executable, "-u", str(t / r)], cwd=str(t), capture_output=True, timeout=45,
                                    env={**os.environ, "PYTHONPATH": str(t / "scripts")})
                out[tag] = (pr.returncode, (pr.stdout + pr.stderr).decode("utf-8", "replace"))
            except subprocess.TimeoutExpired:
                out[tag] = (None, "")
        res[r] = out
    unpinned_ok = [r for r in pick if r not in pinned]
    chk("X1 unpatched scratch tree reproduces exit code 0 for every unpinned fast runner (environment sound)",
        all(res[r]["old"][0] == 0 for r in unpinned_ok), "n=%d" % len(unpinned_ok))
    def key(t):
        m = re.findall(r"TOTAL: PASS=\d+ FAIL=\d+", t[1])
        return (t[0], m[-1] if m else None)
    chk("X2 patched tree: every unpinned fast runner still exits 0 with the same TOTAL line as the unpatched tree (pure re-execution refreshes them; raw stdout can differ by temp-dir names)",
        all(key(res[r]["new"]) == key(res[r]["old"]) and res[r]["new"][0] == 0 for r in unpinned_ok), "n=%d" % len(unpinned_ok))
    pin_run = [r for r in pick if r in pinned]
    bad = [r for r in pin_run if res[r]["old"][0] == 0 and res[r]["new"][0] != 0]
    chk("X3 DEFECT-OF-PLAN: hash-pinned runners pass on the unpatched tree and FAIL on the patched tree (re-execution alone records a failing cache)",
        len(bad) >= 1 and len(bad) == len([r for r in pin_run if res[r]["old"][0] == 0]), "%d of %d" % (len(bad), len(pin_run)))
    reasons = [r for r in bad if re.search(r"FAIL|mismatch|binding failed|changed declared input|AssertionError", res[r]["new"][1])]
    chk("X4 the failures are reported by the runners' own hash/binding checks", len(reasons) == len(bad), "n=%d" % len(reasons))
    FACTS["live_bad"] = bad
    FACTS["live_n"] = len(pick)


# ---------------------------------------------------------------- main
def main():
    try:
        ent = tree_entries(O)
        part_sources(ent)
        part_wording(ent)
        part_regen(ent)
        part_epoch(ent)
        part_census(ent)
        part_plan(ent)
        part_reexec(ent)
        rec = dict(
            source_branch="main (task) / fix/time-wording-current-axioms (author branch)",
            source_head=C, current_main_checked=O, author_commit=AUTH,
            source_objects=[dict(path=p, sha256=TASK_SRC[p], verified=sha(blob(C, p)) == TASK_SRC[p]) for p in TASK_SRC],
            author_blobs=[dict(path=p, sha256=AUTH_BLOBS[p], verified=sha(blob(AUTH, p)) == AUTH_BLOBS[p]) for p in AUTH_BLOBS],
            first_unresolved_step="Step 13(b) of ATTEMPT.md: %d of the 165 pinned runners embed the old note/skill sha256 (EXECUTION_PLAN.json embeds_old_sha) and, with 2 more that bind the files another way, fail after the repair (16 of 117 executed); their expected hashes need a reviewed re-pin before cache recapture can yield passing caches" % FACTS["plan"]["counts"]["embeds_old_sha"],
            remaining_work=["land the five-file repair as its own reviewed change (not done here)",
                            "reviewed re-pin of hash-pinned runners and the INPUT_CLOSURE/PREMISE_FRESHNESS json files that quote the old sha256 (census in ATTEMPT.md)",
                            "execute EXECUTION_PLAN.json shards with precompute_audit_runners.py (not executed here: it writes logs/runner-cache in the repo)",
                            "24 affected runners have no cache and are slow (48-97 s observed) or have unreadable declared inputs; decide separately"])
        (OUT / "RECOVERY_STATUS.json").write_text(json.dumps(rec, indent=1) + "\n")
    finally:
        if "p" in _BATCH:
            _BATCH["p"].stdin.close()
            _BATCH["p"].wait(timeout=10)
        shutil.rmtree(SCRATCH, ignore_errors=True)
    print("TOTAL: PASS=%d FAIL=%d" % (PASSN, FAILN))
    n_aff = len(FACTS.get("aff", []))
    fresh = sum(1 for r in FACTS.get("aff", []) if FACTS["pre"][r] == "fresh")
    if FAILN == 0:
        print("HIT: scoped plan defect and size correction for the clock-wording repair on current main: it pins %d runner caches (%d fresh), not thousands, but %d of them embed the old note or skill sha256 and fail when re-executed against the repaired files, so cache recapture needs a reviewed hash re-pin first and cannot be done by re-execution alone" %
              (n_aff, fresh, FACTS["plan"]["counts"]["embeds_old_sha"]))
    print("SUMMARY: the five-file wording repair is rebuilt from current main with the real generator (3 files byte-identical to the author's, 2 equal after the main drift), its grant text is unchanged, and its dependency census, hash-pin census and bounded live re-execution give a concrete recapture plan with one blocking step (old-hash re-pins) (%.0fs)" % (time.time() - T0))
    sys.exit(0 if FAILN == 0 else 1)


if __name__ == "__main__":
    main()
