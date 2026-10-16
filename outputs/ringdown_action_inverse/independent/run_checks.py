"""Bounded isolated reproduction and independent check orchestration."""
AUDIT_TIMEOUT_SEC=120
from pathlib import Path
import os,subprocess,time,json,hashlib,shutil,ast,difflib
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
PACK=Path('/Users/jonBridger/.codex/worktrees/observations-backward-derivation-24h-20261015/New Axioms Lets Go/.claude/science/physics-loops/observations-backward-derivation-24h-20261015')
# Reuse independent derivations only after the canonical source review.
imports={}
for old,new in [('independent_common_action_ringdown/check.py','common_check.py'),('independent_ringdown_reconstruction/check.py','reconstruction_check.py')]:
    data=(PACK/old).read_bytes();(OUT/new).write_bytes(data);imports[str(PACK/old)]=hashlib.sha256(data).hexdigest()
(OUT/'reused_independent_bindings.json').write_text(json.dumps(imports,indent=2))
proof='''# Independent canonical derivation and correspondence

The complete canonical note, primary, helper, controls and cache were inspected. The formulas of the previously independent proofs below correspond to canonical equations1-13. The canonical unit makes the unsigned path-error integral explicit, distinguishes ideal continuum identities from finite-grid tests, preserves rest-linearization as a premise, and identifies the static derivative comparison as generator-side verification. No mathematical premise was silently weakened in integration.

The primary imports and executes both mathematical bodies directly; source hashing and output aggregation are new packaging. Four declared predicate strengthenings replace trivial literal/object comparisons with actual rank loss, integrated zero excitation, recomputed Q and differentiated conjugate-force transformation. AST-normalized comparison diffs are stored separately. They are representation evidence rather than proof.

'''
for old in ['independent_common_action_ringdown/derivation_before_code.md','independent_ringdown_reconstruction/derivation_before_code.md']:
    proof+='\n\n'+(PACK/old).read_text()
(OUT/'PROOF.md').write_text(proof)
# Check exact extraction by normalized syntax, preserving every actual change.
helper=ast.parse((ROOT/'scripts/ringdown_action_math.py').read_text())
for oldname,func,startname,endname in [('check_common_action_ringdown_v2.py','common_controls','checks','root'),('check_ringdown_action_reconstruction_v1.py','reconstruction_controls','rows','result')]:
    old=ast.parse((PACK/oldname).read_text());body=[];active=False
    for node in old.body:
        names=[n.id for n in getattr(node,'targets',[]) if isinstance(n,ast.Name)]
        if startname in names:active=True
        if endname in names:break
        if active:body.append(node)
    new=next(n for n in helper.body if isinstance(n,ast.FunctionDef) and n.name==func).body[:-1]
    a=ast.unparse(ast.Module(body=body,type_ignores=[])).splitlines(True)
    b=ast.unparse(ast.Module(body=new,type_ignores=[])).splitlines(True)
    # unparse emits no newlines between split lines; restore for readable evidence.
    a=[z.rstrip()+'\n' for z in a];b=[z.rstrip()+'\n' for z in b]
    (OUT/(func+'_extraction.diff')).write_text(''.join(difflib.unified_diff(a,b,fromfile=oldname,tofile=func)))
SCRATCH=OUT/'scratch';SCRATCH.mkdir(exist_ok=True)
for rel in ['docs/RINGDOWN_ACTION_RECONSTRUCTION_NOTE_2026-10-16.md','scripts/ringdown_action_inverse.py','scripts/ringdown_action_math.py']:
    dst=SCRATCH/rel;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((ROOT/rel).read_bytes())
receipts=[];env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
for name,path,cwd in [('common',OUT/'common_check.py',OUT),('reconstruction',OUT/'reconstruction_check.py',OUT),('integration',OUT/'integration_check.py',OUT),('primary',SCRATCH/'scripts/ringdown_action_inverse.py',SCRATCH)]:
    cmd=['python3','-B',str(path)];start=time.time()
    try:
        r=subprocess.run(cmd,cwd=cwd,env=env,capture_output=True,text=True,timeout=120)
        (OUT/(name+'_stdout.txt')).write_text(r.stdout);(OUT/(name+'_stderr.txt')).write_text(r.stderr)
        receipts.append({'name':name,'command':cmd,'cwd':str(cwd),'timeout_seconds':120,'PYTHONDONTWRITEBYTECODE':'1','elapsed_seconds':time.time()-start,'returncode':r.returncode})
    except subprocess.TimeoutExpired as e:
        receipts.append({'name':name,'timeout':True});(OUT/'execution_receipts.json').write_text(json.dumps(receipts,indent=2));raise
(OUT/'execution_receipts.json').write_text(json.dumps(receipts,indent=2))
canon=(ROOT/'outputs/ringdown_action_inverse/controls.json').read_bytes();repro=(SCRATCH/'outputs/ringdown_action_inverse/controls.json').read_bytes()
cache=(ROOT/'logs/runner-cache/ringdown_action_inverse.txt').read_text();cached_stdout=cache.split('----- stdout -----\n',1)[1].split('\n----- stderr -----',1)[0]
actual=(OUT/'primary_stdout.txt').read_text()
comparison={'controls_byte_identical':canon==repro,'cache_stdout_equal_ignoring_separator_newlines':cached_stdout.rstrip('\n')==actual.rstrip('\n'),'primary_summary':json.loads(repro)['summary'],'independent_summaries':{n:json.loads((OUT/(n+'_stdout.txt')).read_text())['summary'] for n in ['common','reconstruction','integration']},'all_returncodes_zero':all(r.get('returncode')==0 for r in receipts)}
(OUT/'comparison.json').write_text(json.dumps(comparison,indent=2));print(json.dumps(comparison,indent=2))
