#!/usr/bin/env python3
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,subprocess
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;repo=BASE/'campaign-working'
REV='60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
sha=lambda b:hashlib.sha256(b).hexdigest()
(HERE/'sources').mkdir(exist_ok=True)
specs=[
 ('LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md','7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a','local_pair.md'),
 ('LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md','c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b','common_limit.md'),
 ('FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md','2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516','formation_balance.md')]
rows=[]
for name,expected,dest in specs:
    origin=repo/'docs'/name;raw=origin.read_bytes();assert sha(raw)==expected
    run=subprocess.run(['git','show',REV+':docs/'+name],cwd=repo,capture_output=True,check=True)
    assert not run.stderr and run.stdout==raw
    with (HERE/'sources'/dest).open('xb') as out:out.write(raw)
    rows.append(dict(origin=str(origin),revision=REV,frozen_path='sources/'+dest,
        sha256=sha(raw),bytes=len(raw),exact_git_object=True,
        status='Supplied conditional finite-model parent; no retained-grade import'))
author=BASE/'native-ground-filling-personal'
for name,expected,dest in [
 ('NATIVE_GROUND_SECTOR_FILLING_ROOT.md','aef82e905d9270ae543501dd7548687fae93fda806cc8dd7b7c8861aafe8cadb','provisional_filling.md'),
 ('AUTHOR_SEAL.json','0b72c3cd4dd5404a53de9808a5bf99fab48eab182defedba729b695ff4202066','provisional_filling_seal.json')]:
    raw=(author/name).read_bytes();assert sha(raw)==expected
    with (HERE/'sources'/dest).open('xb') as out:out.write(raw)
    rows.append(dict(origin=str(author/name),frozen_path='sources/'+dest,sha256=sha(raw),bytes=len(raw),
        status='Explicitly allowed provisional dependency; its controls and independent PRE were not read or run'))
for name,dest in [('AGENTS.md','AGENTS_pointer.md'),('docs/ai_methodology/SCIENCE_WORKFLOW.md','SCIENCE_WORKFLOW.md')]:
    raw=(repo/name).read_bytes()
    with (HERE/'sources'/dest).open('xb') as out:out.write(raw)
    rows.append(dict(origin=str(repo/name),frozen_path='sources/'+dest,sha256=sha(raw),bytes=len(raw),
                     status='Current local procedure, completely read; no scientific premise'))
ref=subprocess.run(['git','rev-parse','origin/ai/execution'],cwd=repo,capture_output=True,check=True).stdout.decode().strip()
run=subprocess.run(['git','show',ref+':AGENTS.md'],cwd=repo,capture_output=True,check=True);assert not run.stderr
with (HERE/'sources/AGENTS_execution.md').open('xb') as out:out.write(run.stdout)
rows.append(dict(origin='git:origin/ai/execution:AGENTS.md',repository=str(repo),revision=ref,
    frozen_path='sources/AGENTS_execution.md',sha256=sha(run.stdout),bytes=len(run.stdout),
    status='Current locally available instruction ref, completely read. No fetch or repository mutation.'))
data=dict(created_utc=datetime.now(timezone.utc).isoformat(),phase='Blind selective PRE',
    source_revision=REV,sources=rows,author_incompatibility_packet_read=False,
    other_active_checker_read=False,parent_programs_run_or_imported=False,
    provisional_dependency_scope='Vacancy row bound and half-occupancy variational estimate only, explicitly conditional',
    historical_exposure='Prior native-one-pair-spectrum PRE/POST and original resolved creation convention are known; not claimed as fresh independence.')
with (HERE/'SOURCE_PINS.json').open('x') as out:json.dump(data,out,indent=2);out.write('\n')
print(json.dumps(data,indent=2))
