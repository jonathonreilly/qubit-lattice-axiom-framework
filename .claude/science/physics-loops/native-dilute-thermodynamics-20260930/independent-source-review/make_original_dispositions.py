from pathlib import Path
import json,subprocess,hashlib,datetime
base='ea3d4f6236160233f6f9e183b4b6eb5ba3252607';tree='e4b261bde8908d41acbf69663901ac96164080bf';main='fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7'
prefix='.claude/science/physics-loops/native-dilute-thermodynamics-20260930/'
def blob(p):return subprocess.check_output(['git','show',tree+':'+p])
def sha(b):return hashlib.sha256(b).hexdigest()
paths=subprocess.check_output(['git','diff','--name-only','--no-renames',base,tree],text=True).splitlines()
rows=[]
for p in paths:
 b=blob(p);h=sha(b)
 if p.startswith('docs/NATIVE_DILUTE'):
  reason='Current canonical argument or owned supporting proof; complete scientific read, accepted under explicit supplied-model hypotheses.';read='complete source read and independent manual reconstruction'
 elif p.startswith('scripts/'):
  reason='Finite exact primary; seven finite families only. Executable accepted; original comment corrected separately per FINDINGS_01.';read='complete source read; independent positive-square path control'
 elif '/mutations/' in p:
  reason='Historical author sensitivity control evidence; no scientific authority or fresh-run claim. Oracle/formula distinctions are recorded in FINDINGS_01.';read='primary complete read plus exact single-assignment delta; raw failure/capture/receipt structural verification'
 elif '/historical/' in p:
  reason='Historical recovery/provenance only. No old verdict or abandoned claim is adopted. Current adopted arguments appear in fully read current proofs.';read='source-map role inspection and complete byte/hash equality to campaign source; gzip decompressed and terminal-whitespace comparison where applicable; not independent recertification of historical proof bodies'
 elif p=='docs/audit/data/citation_graph_manifest.json':
  reason='Generated topology acknowledgment only; four owned nodes and fourteen dependencies, no old-node change and no audit status.';read='complete parsed old/new manifest comparison; new source links inspected'
 elif p.startswith('logs/'):
  reason='Original author finite-control cache; source/input-bound historical execution, pending supersession after comment-only primary correction.';read='complete stdout/header read and exact capture equality'
 elif '/primary/' in p or '/graph/' in p or '/preexecution/' in p:
  reason='Original author execution, capture or mechanical preflight evidence; no reviewer verdict or audit authority.';read='receipt/input identities and actual captures parsed/verified; stdout examined; author-preflight ownership explicitly read'
 else:
  reason='Author contract, method, resource, provenance or unpublished delivery metadata; not independent science or audit authority.';read='current narrative/control/wrapper full read; structured inventory/freeze records parsed and checked against exact identities'
 rows.append({'original_path':p,'original_sha256':h,'disposition':'accepted unchanged as original frozen source/evidence, with separately recorded narrow correction where applicable','recovery':'git '+tree+':'+p,'final_path':p,'final_sha256':h,'role_and_rationale':reason,'actual_read_scope':read})
context=json.loads(blob(prefix+'CONTRACT_FREEZE.json'))['base_inputs']
inherited=[]
for x in context:
 p=x['path'];isth='NATIVE_FOUR_PARTICLE' in p
 inherited.append({'original_path':p,'original_sha256':x['sha256'],'disposition':'accepted unchanged as provisional mathematical input' if isth else 'accepted unchanged as current-main context/premise source','recovery':'git '+(base if isth else main)+':'+p,'final_path':p,'final_sha256':x['sha256'],'actual_read_scope':'complete source read; mathematical argument independently examined' if 'NATIVE_' in p else 'complete authority/source read; grant and non-grants checked','authority_boundary':'PR9401 remains provisional; no inherited review assumed' if isth else 'Actual main authority read; axiom/primitive grants do not select supplied model'})
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer_session':'/root/native_thermodynamics_source_review','original_base':base,'original_tree':tree,'original_dispositions':rows,'input_dispositions':inherited,'deleted_paths':[],'correction_boundary':'These are original-tree dispositions; corrected final source/input/evidence mapping must be supplied in the same-session final addendum, not by mutating this historical record.','read_scope_limit':'Full scientific closure current proof bodies and primary read; historical originals are provenance-only, verified lossless but not independently recertified.'}
Path('independent-source-review/ORIGINAL_DISPOSITIONS.json').write_text(json.dumps(result,indent=2)+'\n')
print('original dispositions',len(rows),'input dispositions',len(inherited))
