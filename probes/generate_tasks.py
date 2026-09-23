#!/usr/bin/env python3
"""Generate probes/TASKS.json: every runner in scripts/ with a pinned cache becomes a re-execution task (type R), every runner with
--list-mutations becomes a mutation-census task (type M), every *refuter*.py control in a science pack becomes a re-run task (type F);
the hand-written tasks in probes/tasks/*.json (searches, scans, falsifier work) are appended.  Run from the repository root."""
import json, os, re, glob, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tasks = []
cache = set(os.path.splitext(f)[0] for f in os.listdir(os.path.join(ROOT, "logs", "runner-cache")) if f.endswith(".txt")) if os.path.isdir(os.path.join(ROOT, "logs", "runner-cache")) else set()
VERDICT = r"PASS\s*=\s*\d+[^\n]{0,40}FAIL\s*=\s*\d+"
FAILLINE = r"(?m)^\s*(?:\[FAIL\]|FAIL\b(?!\s*[=:]\s*0\b)(?!ED\s*[=:]?\s*0\b))"      # TOTAL: / SUMMARY: / SCORECARD / bare PASS=n FAIL=m lines
def cache_body(name):
    p = os.path.join(ROOT, "logs", "runner-cache", name + ".txt")
    if not os.path.exists(p): return None
    s = open(p, errors="replace").read()
    return s.split("----- stdout -----")[-1].split("----- stderr -----")[0]
def verdict_patterns(name):
    """Per-runner expectation derived from its own pinned cache: the runners of this repository end with one of several
    summary formats (TOTAL: PASS=n FAIL=0; SUMMARY: ... PASS=n FAIL=0; SCORECARD PASS=n FAIL=0; a bare PASS=n FAIL=0; or
    a free-form last line such as VERIFIED or a certificate sentence).  Without a cache the verdict is the exit code."""
    body = cache_body(name)
    if body is None:      # no pinned cache: nothing to compare with; exit code 0 without a failing count or line is the pass
        return {"expect_pattern": None, "parse": {}, "hit_pattern": r"(?m)FAIL\s*=\s*[1-9]|" + FAILLINE[4:] + r"|Traceback \(most recent call last\)"}
    if re.search(VERDICT, body):
        return {"expect_pattern": r"PASS\s*=\s*\d+[^\n]{0,40}FAIL\s*=\s*0\b", "parse": {"total": VERDICT}, "hit_pattern": r"(?m)PASS\s*=\s*\d+[^\n]{0,40}FAIL\s*=\s*[1-9]|" + FAILLINE[4:]}
    lines = [l.rstrip() for l in body.splitlines() if len(re.findall(r"[A-Za-z0-9]", l)) >= 3]
    last = lines[-1] if lines else ""
    return {"expect_pattern": None, "parse": {}, "hit_pattern": r"(?m)FAIL\s*=\s*[1-9]|" + FAILLINE[4:] + r"|Traceback \(most recent call last\)", "verdict_line": last}
runners = sorted(glob.glob(os.path.join(ROOT, "scripts", "*_20[0-9][0-9]_[0-9][0-9]_[0-9][0-9].py")))
for r in runners:
    name = os.path.splitext(os.path.basename(r))[0]
    src = open(r, encoding="utf-8", errors="ignore").read()
    total = re.search(r"Expected final line: `TOTAL: PASS=(\d+) FAIL=0`", src) or re.search(r"TOTAL: PASS=(\d+) FAIL=0", src)
    fam = name.split("_")[0]
    if "__main__" not in src and name not in cache: continue      # a source-only module, not a runner
    tasks.append({"id": f"R:{name}", "type": "runner-reexecution", "lane": fam, "tier": 0,
                  "command": f"python3 scripts/{name}.py", "cwd": ".", "timeout_s": 1200,
                  **verdict_patterns(name), "cached": name in cache,
                  "what": "re-execute the runner; a hit is any FAIL or a verdict line differing from logs/runner-cache/<name>.txt (the expected format was read from that cache)"})
    if "--list-mutations" in src:
        tasks.append({"id": f"M:{name}", "type": "mutation-census", "lane": fam, "tier": 0,
                      "command": f"for m in $(python3 scripts/{name}.py --list-mutations | awk '{{print $1}}'); do echo \"== $m\"; python3 scripts/{name}.py --mutation $m | grep 'mutation_family\\|TOTAL'; done",
                      "cwd": ".", "timeout_s": 3600, "parse": {"expected": r"mutation_family_expected: (\S+)", "observed": r"mutation_family_observed: (\S+)"},
                      "hit_pattern": r"mutation_family_observed: -", "what": "run every declared mutation; a hit is a mutation that fails no family or fails outside its family (compare expected/observed)"})
for spec in sorted(glob.glob(os.path.join(ROOT, ".claude", "science", "**", "specs", "*refuter*.py"), recursive=True)):
    rel = os.path.relpath(spec, ROOT); name = os.path.splitext(os.path.basename(spec))[0]
    tasks.append({"id": f"F:{name}", "type": "refuter-rerun", "lane": rel.split("/")[3] if rel.count("/") >= 3 else "pack", "tier": 1,
                  "command": f"cd scripts && python3 ../{rel} . {{EXTRA}}", "cwd": ".", "timeout_s": 3600,
                  "hit_pattern": r"INCONSISTENC|refuted|FAIL", "parse": {"verdict": r"== verdict: (.*)"},
                  "what": "re-run the refuting control (its own seeds; pass --extra for other arguments); a hit is an inconsistency it reports"})
# type P: every open science PR, re-executed in an isolated worktree by probes/run_pr_branch.py (a direct task)
try:
    import subprocess
    prs = json.loads(subprocess.check_output(["gh", "pr", "list", "--state", "open", "--limit", "200", "--json", "number,title,headRefName,files"], cwd=ROOT, text=True, timeout=120))
    for p in sorted(prs, key=lambda x: x["number"]):
        if p["headRefName"].startswith("ai/"):
            continue
        notes = [f["path"] for f in p.get("files", []) if f["path"].startswith("docs/") and f["path"].endswith(".md") and "/audit/" not in f["path"] and "/repo/" not in f["path"]]
        # type J per PR: one falsifier implementation and one provenance audit for the notes the PR adds or changes
        if notes:
            shown = ", ".join(n.split("/")[-1] for n in notes[:3]) + (" ..." if len(notes) > 3 else "")
            common = (f" The notes live on the PR branch: git fetch origin {p['headRefName']}; git show origin/{p['headRefName']}:<note>. "
                      f"Create probes/work/pr{p['number']}/<script>.py on ai/probes (self-contained; exact arithmetic where the note is exact); "
                      f"it prints SUMMARY: ... and HIT: ... lines. Run: python3 probes/run_probe.py <task> --worker <name> --review \"...\" --extra \"python3 probes/work/pr{p['number']}/<script>.py\"")
            tasks.append({"id": f"J:falsifier:PR{p['number']}", "type": "judgment", "lane": p["headRefName"].split("/")[-1][:40], "tier": 2,
                          "command": "{EXTRA}", "cwd": ".", "timeout_s": 7200, "hit_pattern": r"(?mi)^HIT", "parse": {"summary": r"(?m)^SUMMARY: (.*)"},
                          "what": f"PR #{p['number']} ({p['title'][:60]}): implement ONE falsifier from the Falsifiers section (or one stated theorem's finite check) of {shown} with machinery disjoint from the note's runner, and run it beyond the note's sizes. A HIT is a falsifier that fires." + common})
            tasks.append({"id": f"J:attack:PR{p['number']}", "type": "judgment", "lane": p["headRefName"].split("/")[-1][:40], "tier": 2,
                          "command": "{EXTRA}", "cwd": ".", "timeout_s": 7200, "hit_pattern": r"(?mi)^HIT", "parse": {"summary": r"(?m)^SUMMARY: (.*)"},
                          "what": f"PR #{p['number']} ({p['title'][:60]}): attack {shown} with ONE of the patterns that have already found defects in this repository; choose the one that fits the note and say which in the SUMMARY line. "
                                  "(a) WITNESS REALIZABILITY: every stated witness, configuration or example exists in the declared setting (Z^3 is bipartite: no triangles; window shapes; parameter ranges; the graph a runner builds is the graph the note describes). "
                                  "(b) SAME TEST, BOTH SIDES: for every separation claim (A has property X, B lacks it) apply the identical test to both objects in every representation the note uses; a property that both have or both lack in the same representation separates nothing. "
                                  "(c) EXECUTED NUMBERS: every executed range, count or sampler named in the claim scope against the control outputs on the PR branch (.claude/science/**/specs/*.out.txt). "
                                  "(d) QUANTIFIER SCOPE: 'for every coupling/size/window' against what is proved and what was only executed at some sizes. "
                                  "(e) SAMPLED EVIDENCE: any 'never/always observed' resting on random sampling gets a hill-climb or adversarial search instead of more samples. "
                                  "(f) NORMALIZATION: factors of L, N, 2 pi and conjugation conventions in Fourier sums, recomputed at a small size by brute force. A HIT is a defect your script demonstrates." + common})
            PATTERNS = {
                "g": "PROOF STEP BY BRUTE FORCE (the pattern with the best yield so far): pick ONE step of a proof that asserts a finite combinatorial or algebraic fact (the orbit of an event under a reflection group, a count, an identity, a bound at finite size, a recursion's solution) and verify it LITERALLY at small sizes by enumeration, exactly as written, not as you think it was meant. Block 17's chessboard step failed this way: the stated disseminated event was 'every bond', the computed orbit was a quarter of them",
                "a": "WITNESS REALIZABILITY: every stated witness, configuration, example or counterexample exists in the declared setting (Z^3 is bipartite: no triangles; window shapes; parameter ranges; the graph a runner builds is the graph the note describes)",
                "b": "SAME TEST, BOTH SIDES: for every separation claim (A has property X, B lacks it) apply the identical test to both objects in every representation the note uses; a property both have, or both lack, in the same representation separates nothing",
                "d": "QUANTIFIER SCOPE: every 'for every coupling / size / window / order' against what is proved and what was only executed at some sizes; look for a parameter value inside the stated range where the proof's inequality fails",
                "e": "SAMPLED EVIDENCE: any 'never / always observed' or conjecture resting on random sampling gets a hill-climb or adversarial construction instead of more samples (block 31 refuted a 2/3 budget this way)",
                "f": "NORMALIZATION: factors of L, N, 2 pi, 1/2 and conjugation conventions in Fourier sums, structure factors and sum rules, recomputed at a small size by brute force",
            }
            for key, text in PATTERNS.items():
                tasks.append({"id": f"J:attack-{key}:PR{p['number']}", "type": "judgment", "lane": p["headRefName"].split("/")[-1][:40], "tier": 2,
                              "command": "{EXTRA}", "cwd": ".", "timeout_s": 7200, "hit_pattern": r"(?mi)^HIT", "parse": {"summary": r"(?m)^SUMMARY: (.*)"},
                              "what": f"PR #{p['number']} ({p['title'][:60]}): attack {shown} with this ONE pattern. {text}. If the pattern has no purchase on this note, say so in one SUMMARY line and finish: that is a valid result. A HIT is a defect your script demonstrates; a defect already listed under KNOWN HITS is not a result." + common})
            tasks.append({"id": f"J:provenance:PR{p['number']}", "type": "judgment", "lane": p["headRefName"].split("/")[-1][:40], "tier": 2,
                          "command": "{EXTRA}", "cwd": ".", "timeout_s": 7200, "hit_pattern": r"(?mi)^HIT", "parse": {"summary": r"(?m)^SUMMARY: (.*)"},
                          "what": f"PR #{p['number']} ({p['title'][:60]}): for every number in the theorem statements of {shown}, locate the runner line that prints it (the PR's scripts/ runner and its cached stdout in logs/runner-cache/) or its exact derivation in the note; the script prints one line per number with its source, and HIT: for any number without one. A number the note attributes to ANOTHER block or note is sourced when that block's cache prints it (check it; print INFO, not HIT, when it does). Match exponents and fractions in both ASCII and Unicode forms." + common})
        tasks.append({"id": f"P:{p['number']}", "type": "pr-reexecution", "lane": p["headRefName"].split("/")[-1][:40], "tier": 0, "direct": True,
                      "command": f"python3 probes/run_pr_branch.py {p['number']}", "cwd": ".", "timeout_s": 7200,
                      "hit_pattern": r"(?m)^HIT: ", "parse": {"runners": r"runners in the PR: (\d+)"},
                      "what": f"re-execute the runners of PR #{p['number']} ({p['title'][:70]}) in a temporary worktree of its branch, with their mutation censuses; a HIT is a non-zero exit, a failing count or check line, or a census mismatch (a runner without a PASS/FAIL count line passes on exit code 0). Run: python3 probes/run_pr_branch.py {p['number']} --worker <name> --review \"...\""})
except Exception as e:
    print("open PRs not enumerated (gh unavailable?):", e)
# type J per note on main that declares falsifiers: the lowest judgment priority, a deep backlog
for f in sorted(glob.glob(os.path.join(ROOT, "docs", "*.md"))):
    try: text = open(f, encoding="utf-8", errors="ignore").read()
    except Exception: continue
    if "\n## Falsifiers" not in text: continue
    stub = re.sub(r"[^A-Za-z0-9]+", "_", os.path.basename(f)[:-3]).strip("_")[:90]
    tasks.append({"id": f"J:note:{stub}", "type": "judgment", "lane": stub.split("_")[0].lower(), "tier": 2, "command": "{EXTRA}", "cwd": ".", "timeout_s": 7200,
                  "hit_pattern": r"(?mi)^HIT", "parse": {"summary": r"(?m)^SUMMARY: (.*)"},
                  "what": f"Note on main: docs/{os.path.basename(f)}. Implement ONE falsifier of its Falsifiers section, or verify one proof step literally at small sizes by enumeration, with machinery disjoint from the note's runner, beyond the note's sizes. Create probes/work/note_{stub[:40]}/<script>.py (self-contained; exact arithmetic where the note is exact); it prints SUMMARY: ... and HIT: ... lines. Run: python3 probes/run_probe.py <task> --worker <name> --review \"...\" --extra \"python3 probes/work/note_{stub[:40]}/<script>.py\""})
for f in sorted(glob.glob(os.path.join(ROOT, "probes", "tasks", "*.json"))):
    tasks.extend(t for t in json.load(open(f)) if not t.get("retired"))      # retired tasks stay in their files with the reason, out of the queue
json.dump(tasks, open(os.path.join(ROOT, "probes", "TASKS.json"), "w"), indent=1)
by = {}
for t in tasks: by[t["type"]] = by.get(t["type"], 0) + 1
print("tasks:", len(tasks), by)
