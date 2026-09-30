"""T24 test A2 (reduced, per range, run in parallel because the machine is loaded)."""
import sys, json
import numpy as np
import A_pin as A
r = int(sys.argv[1]); nsamp = int(sys.argv[2]); seed = int(sys.argv[3])
A.rng = np.random.default_rng(seed)
sums = []; counts = []; pats = {}
for s in range(nsamp):
    const, C = A.random_coeffs(r)
    cav, tab = A.average(const, C, A.rot("O"), "full")
    nodes = A.find_nodes(cav, tab)
    chis = [c for _, c in nodes]
    sums.append(sum(chis)); counts.append(len(nodes))
    ncorner = sum(1 for k, _ in nodes if any(np.linalg.norm((k - c + np.pi) % (2*np.pi) - np.pi) < 1e-5 for c in A.CORNERS))
    pat = A.corner_pattern(nodes)
    key = tuple((next(iter(pat[h])) if (h in pat and len(pat[h]) == 1) else 9) for h in range(4))
    pats[(key, ncorner)] = pats.get((key, ncorner), 0) + 1
    print(f"  sample {s}: nodes {len(nodes)}, corner nodes {ncorner}, sum chi {sum(chis)}", flush=True)
bad = sum(1 for x in sums if x != 0)
print(f"A2b range {r}: samples {nsamp}; nodes per sample min/median/max = {min(counts)}/{int(np.median(counts))}/{max(counts)}; samples with sum(chirality) != 0: {bad}")
print(f"   corner chirality pattern (hw0..hw3), #corner nodes -> count: {dict(sorted(pats.items(), key=lambda kv: -kv[1]))}")
json.dump(dict(r=r, nsamp=nsamp, bad=bad, counts=counts, patterns={str(k): v for k, v in pats.items()}), open(f"A2b_r{r}.json", "w"))
