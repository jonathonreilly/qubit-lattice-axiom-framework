import json,glob,re,sys,collections
root=sys.argv[1]; pat=re.compile(sys.argv[2],re.I)
c=collections.Counter()
rows=[]
for f in glob.glob(root+'/docs/audit/data/ledger/**/*.json',recursive=True):
    try: d=json.load(open(f))
    except Exception: continue
    if not isinstance(d,dict) or 'claim_id' not in d: continue
    c[d.get('effective_status')]+=1
    if pat.search(d['claim_id']) or pat.search(d.get('note_path') or ''):
        rows.append((d.get('effective_status'),d.get('claim_type'),d['claim_id'],d.get('note_path')))
print(c)
for r in sorted(rows):
    if r[0] and r[0].startswith('retained'): print(*r)
print('--- non-retained count', sum(1 for r in rows if not (r[0] or '').startswith('retained')))
