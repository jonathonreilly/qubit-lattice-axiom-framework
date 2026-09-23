from pathlib import Path
import hashlib,json,difflib
D=Path(__file__).resolve().parent;B=D.parent
name='FIRST_EVENT_INSTRUMENT_COROLLARY_DRAFT.md'
def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def auth(r,p=None):
 p=Path(r['path']) if p is None else p;x=row(p);assert x['sha256']==r['sha256'] and x['bytes']==r['bytes'];return x
seal=B/'FIRST_EVENT_INSTRUMENT_AUTHOR_SEAL.json';assert row(seal)['sha256']=='2c446eb379dafa054df99ecb872e25ba0a9799d0f4801398132506bf0f2c48da'
s=json.loads(seal.read_text())
for r in s['artifacts']:auth(r)
h=B/'first_event_instrument_history';first=h/'before_zero_total_rate_qualification';second=h/'before_erasure_scope_qualification'
for d,expected in [(first,'5b0039fd58733af4a43b614299ce5f01d16cebc8635be462a21dad304c0d2353'),(second,'d1ee868b2f831f06d4c343c44beb6afc6198deb63be25401e958e2832a5b3470')]:
 oldseal=d/'FIRST_EVENT_INSTRUMENT_AUTHOR_SEAL.json';assert row(oldseal)['sha256']==expected
 for r in json.loads(oldseal.read_text())['artifacts']:
  p=Path(r['path']);auth(r,d/name if p==B/name else p)
texts=[(first/name).read_text(),(second/name).read_text(),(B/name).read_text()]
assert row(first/name)['sha256']=='3f3794aa3473ae9442de9d48b7bccbbd0e000c6ae1a00c262975efa7ed6bca29'
assert row(B/name)['sha256']=='4b9dc935444bdfb3c01835c0c21e2d6cf420f5ea09cc1a5b2f52795cb00492ac'
# Exact scientific replacements plus the explicit review provenance are inspected below.
for i in (0,1):
 (D/('F%d_DELTA.txt'%(i+1))).write_text(''.join(difflib.unified_diff(texts[i].splitlines(True),texts[i+1].splitlines(True),fromfile='before',tofile='after')))
assert 'If r=0, no first event occurs' in texts[2]
assert 'When r>0, for a specified pre-event density' in texts[2]
assert 'No loss of input recoverability from tracing matter alone is\nasserted' in texts[2]
ack={'original_note':row(first/name),'intermediate_note':row(second/name),'current_note':row(B/name),'current_author_seal':row(seal),'F1':'Resolved: r>0 is explicit for first-mark probabilities and normalized joint output; r=0 has no first event.','F2':'Resolved: removes the unjustified matter-erasure loss assertion and states the orthogonal field-divergence qualification.','core_Gram_and_full_output_recovery':'Unchanged; independently verified on degree-three cyclic K2,3.','historical_authentication':'Original three and intermediate six binding seals recover through their archived same-basename notes; all other exact dependencies unchanged.','verdict_scope':'Narrow scientific correction acknowledgment; no formal audit or publication status.'}
(D/'CORRECTION_ACK.json').write_text(json.dumps(ack,indent=2)+'\n');print(json.dumps(ack,indent=2))
