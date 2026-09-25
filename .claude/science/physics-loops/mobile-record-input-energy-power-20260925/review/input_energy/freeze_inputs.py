"""Freeze only the explicitly authorized inputs and applicable procedures."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import subprocess
import json

BASE=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth')
OUT=Path(__file__).resolve().parent
MAIN='0e6ad8285096ed668816f18caaa6fbbfbd9c50e8'

def git(repo,*args):return subprocess.check_output(['git','-C',str(repo),*args])
def digest(data):return sha256(data).hexdigest()

def main():
    directory=OUT/'frozen_inputs';directory.mkdir(exist_ok=True)
    rows=[]
    specs=[
      ('campaign-working','docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',MAIN,'7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a','physics parent'),
      ('campaign-working','docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',MAIN,'c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b','physics parent'),
      ('campaign-working','docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',MAIN,'651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf','physics parent'),
      ('prepared-observation-publication','docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md','fb1991dfa6971e449513fb8e29884376739d21cc','14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b','provisional admitted exact preparation'),
      ('campaign-working','AGENTS.md',MAIN,None,'procedure pointer'),
      ('campaign-working','docs/ai_methodology/SCIENCE_WORKFLOW.md',MAIN,'d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4','procedure'),
      ('campaign-working','docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md',MAIN,'9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455','procedure reused at same revision'),
      ('campaign-working','docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md',MAIN,'b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0','procedure reused at same revision'),
      ('campaign-working','docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md',MAIN,'be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258','procedure reused at same revision')]
    for repo,path,ref,expected,role in specs:
        origin=BASE/repo/path;data=origin.read_bytes();gh=git(BASE/repo,'show',f'{ref}:{path}')
        assert data==gh,(path,'working/git bytes differ')
        if expected:assert digest(data)==expected,path
        dest=directory/Path(path).name
        dest.write_bytes(data)
        rows.append({'path':str(origin),'git_repository':str(BASE/repo),'git_revision':ref,
                     'git_path':path,'sha256':digest(data),'git_bytes_exact_equal':True,
                     'frozen_path':str(dest),'role':role})
    planning=git(BASE/'campaign-working','rev-parse','origin/ai/execution').decode().strip()
    planning_data=git(BASE/'campaign-working','show',f'{planning}:AGENTS.md')
    dest=directory/'PLANNING_AGENTS.md';dest.write_bytes(planning_data)
    rows.append({'git_repository':str(BASE/'campaign-working'),'git_revision':planning,
                 'git_path':'AGENTS.md','sha256':digest(planning_data),'frozen_path':str(dest),
                 'role':'applicable cached planning instructions; no campaign checkpoint read'})
    for name,expected in [('PRE.md','3f9bae4b8de40697dce8ddd0d12382fd7b505156922ed8f713cc26de5e3a9a27'),
                          ('PRE_SEAL.json','c6686cc03d195af4487e3df90cd64e152869c608d5170cd70c5dd81f544b9fdc'),
                          ('primitive_dynamics_control.py','f24031d1dc29abecae15dc47adf5a7eb1cadd83957f241fbc7a9bcdd321d8e2c')]:
        origin=BASE/'prepared-probe-dynamics-independent'/name;data=origin.read_bytes()
        assert digest(data)==expected,name
        dest=directory/('PRIOR_23_24_'+name);dest.write_bytes(data)
        rows.append({'path':str(origin),'sha256':digest(data),'frozen_path':str(dest),
                     'role':'own previously sealed background; no new increment result imported'})
    result={'created_utc':datetime.now(timezone.utc).isoformat(),'blind_scope':
            'Only four authorized physics sources, unchanged procedures and own sealed 23/24 background. No author runner or active root packet was read.',
            'sources':rows,'freeze_code_sha256':digest(Path(__file__).read_bytes())}
    (OUT/'SOURCE_PINS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'sources':len(rows),'all_named_expected_hashes_match':True,
                      'all_nine_working_source_files_equal_pinned_git_bytes':True,
                      'source_pins_sha256':digest((OUT/'SOURCE_PINS.json').read_bytes())},indent=2))

if __name__=='__main__':main()
