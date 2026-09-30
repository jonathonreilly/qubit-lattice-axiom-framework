"""Merge lane wall logs (L*.jsonl) into one registry; report counts, severities and cross-lane links."""
import json, glob, os, collections
W = os.path.dirname(os.path.abspath(__file__))
walls = []
for f in sorted(glob.glob(os.path.join(W, "L*_*.jsonl"))):
    for line in open(f):
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except Exception as e:
            print("bad line in", os.path.basename(f), e); continue
        d["_file"] = os.path.basename(f)
        walls.append(d)
print("walls:", len(walls))
by_lane = collections.Counter(w.get("lane", "?") for w in walls)
by_sev = collections.Counter(str(w.get("severity", "?")).lower() for w in walls)
by_status = collections.Counter(str(w.get("status", "?")).lower()[:20] for w in walls)
print("by lane:", dict(by_lane)); print("by severity:", dict(by_sev)); print("by status:", dict(by_status))
json.dump(walls, open(os.path.join(W, "registry.json"), "w"), indent=1)
for w in walls:
    print(f"{w.get('id')}\t{w.get('severity')}\t{w.get('status')}\t{w.get('title')}\tsame_as={w.get('same_as')}")
