import sys; sys.dont_write_bytecode=True; sys.path.insert(0,".")
import numpy as np
from t63_runner_audit import runner_coords, poisson_coords, fit_from_coords, agg, formula_star
import math
for d in (2,3,4):
    for name,gen in (("replica",runner_coords),("poisson",poisson_coords)):
        v=[]
        for s in range(300,312):
            rng=np.random.default_rng(s); c,sp,nt=gen(d,8,4,rng); v.append(fit_from_coords(c,sp,d,nt)[0])
        m,e=agg(v); print("d=%d %-8s n_s=%+.3f +- %.3f   (*)=%+.3f   runner registered: d2 +1.207, d3 -0.165, d4 -0.287"%(d,name,m,e,formula_star(d,math.log(4))),flush=True)
