import numpy as np, sys, time
from s1_matrix_collision import *
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 2026)
d = int(sys.argv[1]) if len(sys.argv) > 1 else 2
Rlist = {1: [1, 2, 4, 8, 16], 2: [1, 2, 4, 6, 8], 3: [1, 2, 3]}[d]
for inter in ['nn', 'cube']:
    for m in [0.5, 0.0]:
        model = Stag(d, m, inter)
        t0 = time.time()
        nproc = {1: 300, 2: 1500, 3: 400}[d]
        procs = sample_processes(model, nproc, ALLCH, rng)
        # deliberate special branches: K = 0, K = (pi/2,..), K = (pi/2,0,..)
        specials = [np.zeros(d), np.full(d, np.pi/2), np.array([np.pi/2] + [0]*(d-1))]
        for sp_ in specials:
            procs += sample_processes(model, nproc//6, ALLCH, rng, special=sp_)
        chs = {}
        for p in procs: chs[p[0]] = chs.get(p[0], 0) + 1
        print(f"\n== d={d} inter={inter} m={m}: {len(procs)} on-shell processes ({time.time()-t0:.1f}s); channels hit {len(chs)}/16")
        # residual check
        mx = 0
        for (s, k1, k2, k3, k4) in procs:
            E = s[0]*model.omega(k1)[0] + s[1]*model.omega(k2)[0] - s[2]*model.omega(k3)[0] - s[3]*model.omega(k4)[0]
            mx = max(mx, abs(E))
        print(f"  max energy residual {mx:.1e}")
        for R in Rlist:
            t0 = time.time()
            for sec, ex in (('odd', 0), ('even', 2)):
                sv, ncol, nsec, Wn = nullspace_run(model, R, procs, sec, rng)
                report(f"R={R} {sec}", sv, ncol, nsec, Wn, ex)
            print(f"   ({time.time()-t0:.1f}s)"); sys.stdout.flush()
