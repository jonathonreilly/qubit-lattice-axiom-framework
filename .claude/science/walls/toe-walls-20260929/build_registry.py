"""Build the distinct-wall registry from lane jsonl + clusters + attack/kill outputs. Rerunnable."""
import json, glob, os, re, shutil, collections
W = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(W, '..', 'main_wt', '.claude', 'science', 'walls', 'toe-walls-20260929')
exec(open(os.path.join(W, 'clusters.py')).read())
LANES = {}
for f in sorted(glob.glob(os.path.join(W, 'L*_*.md'))):
    code = os.path.basename(f)[:3]
    LANES[code] = os.path.basename(f)
walls = {}
for f in sorted(glob.glob(os.path.join(W, 'L*_*.jsonl'))):
    for line in open(f):
        if line.strip():
            d = json.loads(line); walls[d['id']] = d
SEV = {'blocking': 0, 'major': 1, 'minor': 2}
def attack(tid):
    p = os.path.join(W, 'attacks', tid + '.json')
    if os.path.exists(p):
        try: return json.load(open(p))
        except Exception: return {'outcome': 'UNREADABLE'}
    return None
def kill(tid):
    p = os.path.join(W, 'kills', tid + '.md')
    if not os.path.exists(p): return None
    txt = open(p).read()
    m = re.search(r'## Outcome verdict\s*\n+\s*\**([A-Z]+)', txt)
    return m.group(1) if m else 'SEE-FILE'
rows = []
for tid, title, members in C:
    ms = [walls[m] for m in members]
    sev = min((m['severity'] for m in ms), key=lambda s: SEV[s])
    st = collections.Counter(m['status'] for m in ms)
    lanes = sorted({m['lane'] if m.get('lane','').startswith('L') else m['id'][:3] for m in ms})
    a = attack(tid); k = kill(tid)
    rows.append(dict(id=tid, title=title, severity=sev, member_status=dict(st), lanes=lanes,
                     members=[dict(id=m['id'], lane_file=LANES[m['id'][:3]], severity=m['severity'], status=m['status'], title=m['title'], plain=m['plain']) for m in ms],
                     attack=a, kill=k))
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, 'walls.jsonl'), 'w') as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(os.path.join(OUT, 'lane_walls.jsonl'), 'w') as f:
    for k_ in sorted(walls, key=lambda s: (s[:3], int(s.split('-W')[1]))): f.write(json.dumps(walls[k_], ensure_ascii=False) + '\n')
os.makedirs(os.path.join(OUT, 'probes'), exist_ok=True)
for code, name in LANES.items():
    shutil.copy(os.path.join(W, name), os.path.join(OUT, 'probes', name))
    shutil.copy(os.path.join(W, name[:-3] + '.jsonl'), os.path.join(OUT, 'probes', name[:-3] + '.jsonl'))
for sub in ('attacks', 'kills'):
    os.makedirs(os.path.join(OUT, sub), exist_ok=True)
    for p in glob.glob(os.path.join(W, sub, 'T*.md')) + glob.glob(os.path.join(W, sub, 'T*.json')):
        shutil.copy(p, os.path.join(OUT, sub, os.path.basename(p)))
    for d in glob.glob(os.path.join(W, sub, 'T*_scratch')):
        dst = os.path.join(OUT, sub, 'scripts', os.path.basename(d))
        if os.path.exists(dst): shutil.rmtree(dst)
        shutil.copytree(d, dst, ignore=shutil.ignore_patterns('*.npy','*.npz','*.pkl','__pycache__','*.bin','*.h5'))
print('rows', len(rows), 'attacked', sum(1 for r in rows if r['attack']), 'killed', sum(1 for r in rows if r['kill']))
print(collections.Counter(r['severity'] for r in rows))
print(collections.Counter((r['attack'] or {}).get('outcome','-') for r in rows))
