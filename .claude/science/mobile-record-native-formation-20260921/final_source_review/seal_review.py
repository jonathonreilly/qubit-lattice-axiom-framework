#!/usr/bin/env python3
"""Seal the bounded review, checking every frozen input again."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
sources=json.loads((HERE/'AUTHENTICATION_RESULTS.json').read_text())["sources"]
for row in sources:
    path=ROOT/row["path"]
    assert sha(path)==row["sha256"] and path.stat().st_size==row["bytes"],row["path"]
procedures=[]
for path in [ROOT/'AGENTS.md',ROOT/'docs/ai_methodology/SCIENCE_WORKFLOW.md',
             Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md')]:
    procedures.append(dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path)))
receipt=dict(
 scope="Post-source complete mathematical review; earlier sealed blind results reused by identity.",
 frozen_sources_reauthenticated=len(sources),
 execution=[
 dict(script="authenticate_evidence.py",exit_code=0,stdout_and_stderr="AUTHENTICATION.log",
      mode="authenticate existing baseline/mutations and raw arrays; no author rerun"),
 dict(script="independent_check.py",exit_code=0,stdout_and_stderr="INDEPENDENT_CHECK.log",
      mode="one new exact finite/symbolic run; ten groups; deliberate negative controls included"),
 dict(script="../verify_capsules.py",exit_code=0,stdout_and_stderr="CAPSULE_VERIFICATION.log",
      mode="read-only archive/dependency byte verification")],
 new_failed_executions=[],
 source_read_scope="Complete note, runner and all three scientific checkers; relevant inherited proof premises and authenticated independent capsule dependencies.",
 excluded=["Git/PR/audit actions","Production-source edits","Graph/cache review or seal","External communications or delegation","Unrelated sources and new external literature"],
 instructions=procedures)
(HERE/'PROCEDURE_RECEIPT.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
artifacts=[]
for path in sorted(HERE.iterdir()):
    if path.is_file() and path.name!='SOURCE_REVIEW_SEAL.json':
        artifacts.append(dict(path=path.name,bytes=path.stat().st_size,sha256=sha(path)))
seal=dict(
 created_utc=datetime.now(timezone.utc).isoformat(),
 scope=receipt["scope"],
 disposition="Two narrow corrections F1/F2 required in frozen source; no other unresolved mathematical finding in bounded claims; no audit verdict.",
 sources=sources,procedure_identities=procedures,artifacts=artifacts,
 counts=dict(source_evidence_files=len(sources),procedure_files=len(procedures),review_artifacts=len(artifacts)),
 report_sha256=sha(HERE/'REPORT.md'),
 mutation_reexecution=False,
 statement="No original independent capsule, author source, baseline, mutation result or raw supplemental output was modified.")
(HERE/'SOURCE_REVIEW_SEAL.json').write_text(json.dumps(seal,indent=2,sort_keys=True)+'\n')
print(json.dumps(dict(report_sha256=seal["report_sha256"],seal_sha256=sha(HERE/'SOURCE_REVIEW_SEAL.json'),counts=seal["counts"]),indent=2))
