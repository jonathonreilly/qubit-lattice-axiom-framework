import numpy as np, sys, time
from s1_matrix_collision import *
d = int(sys.argv[1]); seed = int(sys.argv[2]); Rlist = [int(r) for r in sys.argv[3].split(',')]
nproc = int(sys.argv[4]); inters = sys.argv[5].split(','); masses = [float(x) for x in sys.argv[6].split(',')]
rng = np.random.default_rng(seed)
BC = [s for s in ALLCH if s[0] + s[1] != s[2] + s[3]]   # band-changing channels
for inter in inters:
    for m in masses:
        model = Stag(d, m, inter)
        t0 = time.time()
        procs = sample_processes(model, nproc, ALLCH, rng)
        specials = [np.zeros(d), np.full(d, np.pi/2), np.array([np.pi/2] + [0]*(d-1))]
        for sp_ in specials:
            procs += sample_processes(model, nproc//6, ALLCH, rng, special=sp_)
        nb0 = len(procs)
        procs += sample_processes(model, nproc//6, BC, rng, ball=0.5)
        chs = {}
        for p in procs: chs[p[0]] = chs.get(p[0], 0) + 1
        mx = max(abs(s[0]*model.omega(k1)[0] + s[1]*model.omega(k2)[0] - s[2]*model.omega(k3)[0] - s[3]*model.omega(k4)[0]) for (s, k1, k2, k3, k4) in procs)
        print(f"\n== d={d} inter={inter} m={m}: {len(procs)} on-shell processes ({len(procs)-nb0} band-changing) ({time.time()-t0:.1f}s); "
              f"channels hit {len(chs)}/16; max energy residual {mx:.1e}")
        for R in Rlist:
            t0 = time.time()
            for sec, ex in (('odd', 0), ('even', 2)):
                sv, ncol, nsec, Wn = nullspace_run(model, R, procs, sec, rng)
                report(f"R={R} {sec}", sv, ncol, nsec, Wn, ex)
            print(f"   ({time.time()-t0:.1f}s)"); sys.stdout.flush()
