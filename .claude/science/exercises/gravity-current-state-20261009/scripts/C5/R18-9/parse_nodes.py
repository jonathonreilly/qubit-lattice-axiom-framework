"""parse photres2_N160_*.out lines into photres2_N160_parsed.npy (b, fw, T0,T1,T2, E0,E1,E2, muE)."""
import re, glob, numpy as np
rows = []
for f in sorted(glob.glob('photres2_N160_*.out')):
    for line in open(f):
        m = re.match(r'gGw\(([\d.]+),fw=([\d.]+)\) N=160 T:\(([^ ]+) ([^ ]+) ([^)]+)\) E:\(([^ ]+) ([^ ]+) ([^)]+)\) muE ([^ ]+)', line)
        if m: rows.append([float(v) for v in m.groups()])
np.save('photres2_N160_parsed.npy', np.array(rows)); print(np.array(rows)[:, :2])
