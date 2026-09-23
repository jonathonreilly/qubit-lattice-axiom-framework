from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
D=Path(__file__).resolve().parent
def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
bindings=json.loads((D/'SOURCE_BINDINGS.json').read_text())
for r in bindings['sources']:assert row(Path(r['path']))==r
receipts=[]
for p in sorted(D.glob('*_RECEIPT.json')):
 receipt=json.loads(p.read_text())
 for key in ('runner','stdout','stderr'):assert row(Path(receipt[key]['path']))==receipt[key]
 receipts.append({'path':str(p),'exit_code':receipt['exit_code']})
assert len(receipts)==9 and sum(r['exit_code']!=0 for r in receipts)==2
for name,prefix in [('RING_PROBE_RESULTS','ring_probe_run'),
                    ('RING_EXACT_RESULTS','ring_exact_repaired_run'),
                    ('CUBE_GRAM_RESULTS','cube_gram_run'),
                    ('CUBE_FIELD_RESULTS','cube_field_run'),
                    ('RING_SURVIVAL_RESULTS','ring_survival_repaired_run'),
                    ('LIMIT_RESULTS','limit_run'),
                    ('SOURCE_BINDINGS','provenance_run')]:
 assert (D/(name+'.json')).read_bytes()==(D/(prefix+'.stdout')).read_bytes()
 assert (D/(prefix+'.stderr')).read_bytes()==b''
target=D/'PRE_COMPARISON_SEAL.json';assert not target.exists()
artifacts=[row(p) for p in sorted(D.iterdir()) if p.is_file() and p!=target]
out={'created_utc':datetime.now(timezone.utc).isoformat(),
 'status':'Independent reconstruction frozen before new author-source access; ready for bounded source comparison, no formal audit or publication status.',
 'sources':bindings['sources'],'artifacts':artifacts,
 'scientific_scope':'Exact eight-site unit-rotor no-event survival with H4 retained; fixed-normalizable-input fast limit, count law and mean; complete cube immediate marked/total field Grams. No joint finite-spin theorem or cube ordinary-time dynamics.',
 'prior_exposure':bindings['prior_exposure'],
 'read_boundary':bindings['read_boundary'],
 'author_seal_hash_received_but_contents_unread':'47868fa10d852a2c6e57b5600b0f761ccbed01969867c87f53e4cefb71850610',
 'actual_command_receipts':receipts,
 'failures_preserved':'Original ring_exact.py structural simplification assertion and original ring_survival.py off-diagonal Lyapunov sign assertion; both unchanged with full command streams/receipts and separate diagnostics/repaired runners.',
 'next_action':'Stop and await explicit authorization before reading second_event_author or any new finite-spin author source.'}
target.write_text(json.dumps(out,indent=2)+'\n')
for r in out['sources']+out['artifacts']:assert row(Path(r['path']))==r
print(json.dumps({'report':row(D/'REPORT.md'),'pre_seal':row(target),
                  'source_bindings':len(out['sources']),'artifact_bindings':len(out['artifacts'])},indent=2))
