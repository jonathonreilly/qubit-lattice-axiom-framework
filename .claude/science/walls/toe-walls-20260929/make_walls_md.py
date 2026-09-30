"""Write WALLS.md (registry) from clusters, lane jsonl, attacks, kills and final_labels. Rerunnable."""
import json, glob, os, re, collections
W = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(W, '..', 'main_wt', '.claude', 'science', 'walls', 'toe-walls-20260929')
exec(open(os.path.join(W, 'clusters.py')).read())
exec(open(os.path.join(W, 'final_labels.py')).read())
walls = {}
for f in glob.glob(os.path.join(W, 'L*_*.jsonl')):
    for l in open(f):
        if l.strip(): d = json.loads(l); walls[d['id']] = d
SEV = {'blocking': 0, 'major': 1, 'minor': 2}
def kill(t):
    p = os.path.join(W, 'kills', t + '.md')
    if not os.path.exists(p): return 'none'
    m = re.search(r'(CONFIRMED|WEAKENED|OVERTURNED)', open(p).read())
    return m.group(1) if m else '?'
def att(t):
    p = os.path.join(W, 'attacks', t + '.json')
    return json.load(open(p)).get('outcome', '?') if os.path.exists(p) else 'none'
rows = []
for tid, title, ms in C:
    sev = min((walls[m]['severity'] for m in ms), key=lambda s: SEV[s])
    lab, line = F[tid]
    pend = '[kill pending]' in line and kill(tid) == 'none'
    line = line.replace(' [kill pending]', '') if kill(tid) != 'none' else line
    rows.append((tid, title, sev, ms, att(tid), kill(tid), lab, line))
cnt = collections.Counter(r[6] for r in rows)
cs = collections.Counter((r[2], r[6]) for r in rows)
kc = collections.Counter(r[5] for r in rows)
L = []
L.append('# TOE wall registry, 2026-09-29\n')
L.append('Distinct walls of the qubit-lattice TOE, found by 16 lane probes, merged by the supervisor, attacked once each and kill-checked once each. Workers: Claude Sonnet 5.5; supervisor and final labels: Claude Opus 5.5. All checks are same-family, not independent referees. Nothing here is audited.\n')
L.append('**Final labels.** PRICED = equivalent to named premises that are not derived. STANDS = open, no route passes. MISFRAMED = the question should be replaced (the replacement is named in the attack). EXERCISED = the gravity wall, handled by the 09-29 exercise packet.\n')
L.append('| | blocking | major | minor | total |\n|---|---|---|---|---|')
for lab in ['PRICED', 'STANDS', 'MISFRAMED', 'EXERCISED']:
    L.append(f"| {lab} | {cs[('blocking',lab)]} | {cs[('major',lab)]} | {cs[('minor',lab)]} | {cnt[lab]} |")
L.append(f"\nKill checks: {kc['WEAKENED']} weakened, {kc['CONFIRMED']} confirmed, {kc['OVERTURNED']} overturned, {kc['none']} not run.\n")
L.append('No wall was passed.\n')
L.append('| Wall | Sev | Final | Attack → kill | What it comes down to | Members |')
L.append('|---|---|---|---|---|---|')
for tid, title, sev, ms, a, k, lab, line in rows:
    L.append(f"| **{tid}** {title} | {sev} | {lab} | {a} → {k} | {line} | {', '.join(ms)} |")
L.append('\nFiles: `probes/` (lane probe reports and jsonl), `attacks/T*.md|json`, `kills/T*.md`, `attacks/scripts/` and `kills/scripts/` (runnable checks), `walls.jsonl` (machine-readable), `lane_walls.jsonl` (all 179 lane walls), `clusters.py` (the merge), `final_labels.py`, `SUPERVISOR_THREAD.md` (pre-registered supervisor view), `SUMMARY.md` (plain summary), `SUPERVISOR_COMPARISON.md`.')
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, 'WALLS.md'), 'w').write('\n'.join(L) + '\n')
print(cnt, kc)
