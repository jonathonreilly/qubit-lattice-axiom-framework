from pathlib import Path
import datetime, hashlib, json, re, subprocess

D = Path(__file__).resolve().parent
S = D.parent
OLD = S/'lean_audit'
ML = OLD/'mathlib'
RUNTIME = OLD/'lean-4.35.0-rc4-darwin_aarch64'


def identity(p, role):
    data = p.read_bytes()
    return {'path':str(p),'relative_to_packet':str(p.relative_to(D)) if p.is_relative_to(D) else None,
            'role':role,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
            'logical_lines':None if p.suffix=='.olean' else len(data.splitlines())}


protected = []
for rel, expected, role in [
    ('INTERSPECIES_CURRENT_RIGIDITY_PROBE.md','ca44d1c852e6cd0437cf9e98913fb5fb106abb1b42567c68fb6bf3e9a60c80b8','frozen authored theorem'),
    ('interspecies_current_rigidity/receipt.json','283511b410dafa614c1e4453483b540e744604e66b538a803516c8294379267f','frozen authored receipt'),
    ('lean_audit/receipt.json','1564b0bf532aca6c7f43c301455163b1af0afb96405e620eb56c481bdf7ed96d','reused runtime/formalization receipt, fully read'),
    ('lean_audit/run_compile.py','12b8eb52bb33c16bf17c6d87763ac191242b72eea4ac05a853e2a4ef41ed9521','reused compilation entrypoint, fully read')]:
    rec=identity(S/rel,role)
    assert rec['sha256']==expected, rec
    protected.append(rec)

runtime_identity=json.loads((D/'runtime_identity.json').read_text())
for rel in ('lean','lake'):
    rec=identity(RUNTIME/'bin'/rel,'pinned executable, independently rehashed')
    assert rec['sha256']==runtime_identity['records'][rel]['sha256']
    protected.append(rec)

source_ranges = {
 'Mathlib/LinearAlgebra/AffineSpace/Independent.lean':['25-82','80-150','770-840'],
 'Mathlib/LinearAlgebra/AffineSpace/Combination.lean':['220-272','407-429'],
 'Mathlib/LinearAlgebra/LinearIndependent/Defs.lean':['760-779; explored, not the final direct proof route'],
 'Mathlib/Tactic/Module.lean':['1-70; prior complete reading of 1-160 reused'],
 'Mathlib/Tactic/Ring.lean':['source identity; tactic contract via Module; not a full implementation read'],
 'Mathlib/Tactic/NormNum.lean':['import list only; not a full implementation read'],
 'Mathlib/Tactic/FinCases.lean':['source identity only; ordinary elaboration used'],
 'Mathlib/Data/Fin/VecNotation.lean':['source identity only; ordinary elaboration used'],
 'Mathlib/Basic/Real/Basic.lean':['1-55','459-510'],
}
for rel in source_ranges:
    protected.append(identity(ML/rel,'pinned mathlib source; manual coverage separately recorded'))
    object_path=ML/'.lake/build/lib/lean'/Path(rel).with_suffix('.olean')
    if object_path.exists():
        protected.append(identity(object_path,'reused cached library object; no full dependency rebuild'))
for rel in ('lake-manifest.json','lean-toolchain'):
    rec=identity(ML/rel,'pinned dependency configuration')
    assert rec['sha256']==runtime_identity['records'][rel]['sha256']
    protected.append(rec)

revision=subprocess.run(['git','rev-parse','HEAD'],cwd=ML,capture_output=True,text=True,check=True).stdout.strip()
assert revision=='939d5d5d9e6f07d1d8c80a16fa3fa39a7518b716'
status=subprocess.run(['git','status','--porcelain','--untracked-files=no'],cwd=ML,capture_output=True,text=True,check=True).stdout
assert status==''
old_receipt=json.loads((OLD/'receipt.json').read_text())
packages={}
for name, expected in old_receipt['mathlib']['packages'].items():
    actual=subprocess.run(['git','rev-parse','HEAD'],cwd=ML/'.lake/packages'/name,
                          capture_output=True,text=True,check=True).stdout.strip()
    assert actual==expected, (name,actual,expected)
    packages[name]=actual

accepted=[('RigidityGeometry.lean','attempt02','InterspeciesRigidity'),
          ('ControlData.lean','controls02','RigidityControls')]
theorems=[]
compiles=[]
for source,label,namespace in accepted:
    path=D/source
    text=path.read_text()
    assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b',text)
    assert path.read_bytes()==(D/'logs'/(label+'.lean')).read_bytes()
    execution=json.loads((D/'logs'/(label+'.json')).read_text())
    assert execution['exit']==0
    assert execution['source_sha256']==hashlib.sha256(path.read_bytes()).hexdigest()
    log=(D/'logs'/(label+'.log')).read_text()
    assert 'error:' not in log and 'warning:' not in log and 'sorryAx' not in log
    compiles.append(execution)
    for match in re.finditer(r'^theorem\s+(\w+)',text,re.MULTILINE):
        theorems.append({'name':namespace+'.'+match.group(1),'source':source,
                         'line':text[:match.start()].count('\n')+1})
assert len(theorems)==14
inventory=(D/'logs/axiom_inventory.log').read_text()
inventory_execution=json.loads((D/'logs/axiom_inventory.json').read_text())
assert inventory_execution['exit']==0
axioms={name:[x.strip() for x in names.split(',') if x.strip()]
        for name,names in re.findall(r"'([^']+)' depends on axioms: \[([^]]*)\]",inventory)}
assert set(axioms)=={t['name'] for t in theorems}
assert all(set(a)<= {'propext','Classical.choice','Quot.sound'} for a in axioms.values())
assert 'error:' not in inventory and 'warning:' not in inventory and 'sorryAx' not in inventory

false=json.loads((D/'false_controls_manifest.json').read_text())
assert len(false)==4
for item in false:
    assert item['expected_exit']==item['actual_exit']==item['wrapper_exit']==1
    assert item['reached_intended_mathematical_goal'] and not item['unexpected_failure_markers']
    assert not (D/(item['case']+'.olean')).exists()
    assert hashlib.sha256((D/(item['case']+'.lean')).read_bytes()).hexdigest()==item['source_sha256']

(D/'final_compiler.log').write_bytes((D/'logs/attempt02.log').read_bytes())
(D/'positive_compiler.log').write_bytes((D/'logs/controls02.log').read_bytes())
(D/'axioms.txt').write_bytes((D/'logs/axiom_inventory.log').read_bytes())
(D/'CHECKPOINT.md').write_text('''# Frozen scoped Lean packet

Completed six universal finite-geometry theorems in RigidityGeometry.lean: the four-point affine adapter, four-cycle multiplier equality, exceptional skew-line residual elimination, four-anchor homothety, direction exclusion and line disjointness. Main source SHA256: c72e7a9a961d1eec1ff60842ac3e8a5530c8b71dfc1505dc098d7cab780044df.

Principal and positive-control modules compile normally against the pinned Lean 4.35.0-rc4 and mathlib 939d5d5d9e6f07d1d8c80a16fa3fa39a7518b716. All fourteen accepted theorem axiom inventories contain only propext, Classical.choice, Quot.sound. Four false concrete geometry claims reject at mathematical goals. One initial positive-control API-argument error and its complete diagnostic are preserved; final accepted proofs have no holes or custom axioms.

No frozen note/receipt, old runtime evidence, dependency manifest or repository source was edited. No network, package installation, delegation, global configuration change or audit-status decision occurred.

Full labeled-family extension, anchor extraction, shell IFT, measure upgrade, integration, cubic/current and physical premises remain outside this Lean scope. See STATEMENT_MAP.md, SCOPE_REPORT.md and receipt.json for the exact boundary. The separate independent review of the full authored note is not replaced by this same-author formalization.
''')

artifacts=[identity(p,'new source, object, log, control, execution record or report')
           for p in sorted(D.rglob('*')) if p.is_file() and p.name!='receipt.json']
receipt={
 'schema':'scoped-lean-finite-geometry-evidence-v1',
 'frozen_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Six finite-geometry theorems for I9-I14, not the full interspecies collision-invariant theorem or physical law.',
 'formalized_premises':['arbitrary field K','additive commutative group V with Module K V',
    'mathlib AffineIndependent of the four anchor vectors',
    'all four explicit cross-edge equations for the cycle theorem',
    'explicit two line parameterizations, residual direction representations and cross residual equation for the exceptional theorem'],
 'outside_scope':['full-affine-span anchor extraction','full labeled-family extension I7-I8',
    'off-line confinement and remaining propagation','shell IFT','full-support measure upgrade',
    'integration','cubic/current corollary','asymptotic/physical assumptions'],
 'independence':'Formalization and controls by the same author as the frozen note; separate independent proof review is not certified here.',
 'theorems':theorems,'theorem_axioms':axioms,'successful_compilations':compiles,
 'axiom_inventory_execution':inventory_execution,'false_controls':false,
 'failed_development_attempt':{'source':'logs/controls01.lean','log':'logs/controls01.log',
    'execution':'logs/controls01.json','cause':'Omitted explicit Finset argument in a mathlib helper invocation.',
    'repair':'Added Finset.univ; principal geometry proof unchanged.',
    'failed_sorryAx_diagnostics':'Preserved as failed elaboration, never accepted as evidence.'},
 'other_tooling_observations':['A runtime-identity command was rejected before process creation due to a duplicated cwd component, then rerun successfully.',
    'Read-only cache discovery found legacy Mathlib/Data/Real paths absent; the already cached Mathlib/Basic/Real/Basic import was used. No fetch or import compilation failure occurred.'],
 'runtime':runtime_identity,'mathlib_commit':revision,'mathlib_final_tracked_status':status,'packages':packages,
 'library_manual_reading_ranges':source_ranges,
 'library_trust_boundary':'Ordinary pinned upstream cached objects reused; complete transitive library not rebuilt or manually reverified.',
 'reading_coverage':{'RigidityGeometry.lean':'complete final 146 lines','ControlData.lean':'complete final 91 lines',
    'STATEMENT_MAP.md':'complete 108 lines','SCOPE_REPORT.md':'complete',
    'successful_logs':'complete principal, controls and axiom inventory',
    'failed_logs':'complete initial control failure and all four intended false-case failures',
    'old_runtime_receipt_and_entrypoint':'complete','original_note':'earlier complete reading reused at unchanged frozen SHA256'},
 'environment_boundary':{'all_new_writes':'this packet directory','network_fetch':False,'package_installation':False,
    'global_configuration_change':False,'repository_or_frozen_source_edit':False,'delegation':False,
    'selected_model_and_reasoning':'unchanged'},
 'protected_sources':protected,'artifacts':artifacts,'no_retained_status_decision':True,
 'receipt_self_hash':'Excluded to avoid self-reference; communicated separately.'}
path=D/'receipt.json'
assert not path.exists(), 'Do not overwrite a frozen receipt'
path.write_text(json.dumps(receipt,indent=2)+'\n')
for rec in protected+artifacts:
    assert hashlib.sha256(Path(rec['path']).read_bytes()).hexdigest()==rec['sha256']
for name in ('RigidityGeometry.lean','RigidityGeometry.olean','SCOPE_REPORT.md','STATEMENT_MAP.md',
             'final_compiler.log','axioms.txt','receipt.json'):
    print(name,hashlib.sha256((D/name).read_bytes()).hexdigest())
print('FROZEN',len(artifacts),'artifacts;',len(protected),'protected records;',len(theorems),'theorems')
