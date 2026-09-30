import sys
sys.argv = ['B', '4', '4']
import importlib.util
spec = importlib.util.spec_from_file_location('B', 'B_ergodic_2d.py'); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
import time
for N in (4,):
    for flags in ((False, True), (True, True)):
        sect = B.report(N, *flags)
        # summarise: for each P, list top component fraction
        tot = 0; big = 0
        rows = []
        for P, v in sect.items():
            sizes = sorted((len(m) for m in v.values()), reverse=True)
            rows.append((P, sum(sizes), sizes[:4], len(sizes)))
        rows.sort(key=lambda r: -r[1])
        for r in rows[:14]:
            print('   P=%s total=%d top comps=%s ncomp=%d' % r)
