import sys; sys.dont_write_bytecode = True
sys.path.insert(0, ".")
import numpy as np, math
import t63_runner_audit as A
D = 3
vals = A.mean_profile_ns(D, 8, 4, list(range(100, 140)))
m, e = A.agg(vals)
print("runner coordinate law, f=4, delta measured about the ensemble-mean profile (40 seeds): n_s = %+.3f +- %.3f" % (m, e))
print("white-noise expectation n_s = 1 + d =", 1 + D)
