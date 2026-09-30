"""Calibration of world-F frequencies against (i) the TRUE formation order and (ii) a GUESSED independent random order,
plus exact joint KL(formation||static) on the 2x2x2 cube. Independent generator (own code); attacker's calib() reused only as a scorer."""
import numpy as np, importlib.util, sys, itertools
exec(open("kill_N_records.py").read().split("# per-record log score difference")[0])   # regenerates vals, ppred (true order), qstat
sys.argv = ["x", "10"]
spec = importlib.util.spec_from_file_location("C", "../../attacks/T05_scratch/calib_test.py")
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
allsites = np.arange(N)
# (i) true order, all 64 sites per history
X = vals.reshape(-1)
r_true = C.calib(ppred.reshape(-1, 6), X)
# (ii) guessed independent random order
rank = np.argsort(rng.random((M, N)), axis=1).argsort(axis=1)
guess = np.zeros((M, N, 6))
for xi in range(N):
    nbv = -np.ones((M, 6), dtype=int)
    for k, y in enumerate(nbrs[xi]):
        nbv[:, k] = np.where(rank[:, y] < rank[:, xi], vals[:, y], -1)
    guess[:, xi, :] = rule(nbv)
r_guess = C.calib(guess.reshape(-1, 6), X)
print(f"M={M}: F x Pred(TRUE order)     chi2/df = {r_true['chi2_df']:.2f} (df={r_true['df']}), max|z|={r_true['zmax']:.2f}")
print(f"M={M}: F x Pred(GUESSED order)  chi2/df = {r_guess['chi2_df']:.2f} (df={r_guess['df']}), max|z|={r_guess['zmax']:.2f}")
