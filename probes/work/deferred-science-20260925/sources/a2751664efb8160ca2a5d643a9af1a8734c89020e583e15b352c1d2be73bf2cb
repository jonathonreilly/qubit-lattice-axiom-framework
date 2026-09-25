"""Pin only the three authorized scientific parents and applicable procedure."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json, subprocess

HERE=Path(__file__).resolve().parent
REPO=HERE.parent/'campaign-working'
REV='60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
SCIENCE={
 'LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md':'7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a',
 'LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md':'c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b',
 'FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md':'2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516'}

def digest(data):return sha256(data).hexdigest()

def save(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as stream:stream.write(data)

def main():
    pins=[]
    for name,expected in SCIENCE.items():
        source=REPO/'docs'/name;data=source.read_bytes()
        historical=subprocess.check_output(['git','show',REV+':docs/'+name],cwd=REPO)
        assert data==historical and digest(data)==expected
        target=HERE/'sources'/name;save(target,data)
        pins.append({'origin':str(source),'frozen_path':str(target.relative_to(HERE)),
            'revision':REV,'sha256':expected,'bytes':len(data),'exact_git_object':True,
            'role':'Conditional supplied common rotor law; complete authorized source reading.'})
    for name,expected in [
        ('AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
        ('docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4')]:
        source=REPO/name;data=source.read_bytes();assert digest(data)==expected
        target=HERE/'sources'/source.name;save(target,data)
        pins.append({'origin':str(source),'frozen_path':str(target.relative_to(HERE)),
                     'sha256':expected,'bytes':len(data),'role':'Unchanged applicable procedure, fully reread.'})
    instruction_rev=subprocess.check_output(['git','rev-parse','origin/ai/execution'],cwd=REPO).decode().strip()
    data=subprocess.check_output(['git','show',instruction_rev+':AGENTS.md'],cwd=REPO)
    target=HERE/'sources'/'AGENTS_execution.md';save(target,data)
    pins.append({'origin':'git:origin/ai/execution:AGENTS.md','repository':str(REPO),
                 'revision':instruction_rev,'frozen_path':str(target.relative_to(HERE)),
                 'sha256':digest(data),'bytes':len(data),'role':'Instruction-only ref; no fetch or repository mutation.'})
    source=Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md')
    data=source.read_bytes();target=HERE/'sources'/'physics-claim-reviewer_SKILL.md';save(target,data)
    pins.append({'origin':str(source),'frozen_path':str(target.relative_to(HERE)),
                 'sha256':digest(data),'bytes':len(data),'role':'Read for bounded premise/evidence scrutiny; no landing/audit workflow, model change or delegation invoked.'})
    result={'phase':'Blind independent PRE43','at_utc':datetime.now(timezone.utc).isoformat(),
            'sources':pins,
            'historical_exposure':'Prior40 work is known. None of its scientific code/results is imported for this new reconstruction.',
            'author43_or_other_active_packet_opened':False,'scientific_parent_runners_executed':False,
            'model_and_effort_unchanged':True,'delegation':False}
    data=(json.dumps(result,indent=2)+'\n').encode();save(HERE/'SOURCE_PINS.json',data)
    print(data.decode(),end='')

if __name__=='__main__':main()
