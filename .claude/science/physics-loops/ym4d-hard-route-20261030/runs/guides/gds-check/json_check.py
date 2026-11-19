# Reads the row 1081 GUIDE data (read only) and checks the claims of L65, L78, L80.
import json, sys, os
R = sys.argv[1]
def load(m, J): 
    p = os.path.join(R, f"out_{m}_{J}.json")
    return {float(k): v for k, v in json.load(open(p)).items()} if os.path.exists(p) else None
for m, Js in (("n3", (10, 14, 18, 22)), ("2s", (10, 14, 18))):
    print("== model", m)
    data = {J: load(m, J) for J in Js}
    for J, d in data.items():
        if d is None: continue
        bad_pos = bad_dec = 0; minfx = 9e9; bad_heat = 0
        for bM, v in d.items():
            w = v["wilson"]; diffs = [x[1] for x in w]
            bad_pos += sum(1 for x in diffs if x <= 0)
            bad_dec += sum(1 for a, b in zip(diffs, diffs[1:]) if b >= a)
            ms = [x[1] for x in v["heat"]]; fx = [x[2] for x in v["heat"]]
            bad_heat += sum(1 for a, b in zip(ms, ms[1:]) if b < a)
            minfx = min(minfx, min(fx))
        print(f" J2={J} bM={sorted(d)} nonpositive Wilson diffs: {bad_pos}; non-decreasing steps in bL: {bad_dec}; heat steps with m falling: {bad_heat}; min(n1-n0) {minfx:.5f}")
    for Ja, Jb in ((14, 18), (10, 14), (18, 22)):
        da, db = data.get(Ja), data.get(Jb)
        if not da or not db: continue
        for bM in sorted(set(da) & set(db)):
            wa = [x[1] for x in da[bM]["wilson"]]; wb = [x[1] for x in db[bM]["wilson"]]
            fa = [x[2] for x in da[bM]["heat"]]; fb = [x[2] for x in db[bM]["heat"]]
            # skip t = 0 for 2s (degenerate first excited level)
            k0 = 1 if m == "2s" else 0
            dw = max(abs(a-b) for a, b in zip(wa, wb)); df = max(abs(a-b) for a, b in zip(fa[k0:], fb[k0:]))
            print(f"  {Ja} vs {Jb} bM {bM:5.2f}: max |Wilson diff change| {dw:.1e}  max |(n1-n0) change| {df:.1e}  m_inf change {abs(da[bM]['minf']-db[bM]['minf']):.1e}")
