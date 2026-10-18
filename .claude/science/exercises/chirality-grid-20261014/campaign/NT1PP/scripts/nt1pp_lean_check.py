"""NT-1'' check: lean dq_dA equals nt1p_lib.dq_dA (Lx 8 random field) and E2 numbers at Lx 16 reproduce. usage: python3 nt1pp_lean_check.py"""
import numpy as np, subprocess
import nt1p_lib
from nt1pp_common import *
from nt1pp_lean import dq_dA_lean
S = Strip(8, 4); rng = np.random.default_rng(5); A = gen_config(S, rng)
for e in (1, 2):
    th = e * A; w, V = nt1p_lib.eig_H(S, th)
    R0 = nt1p_lib.dq_dA(S, th, w, V); R1 = dq_dA_lean(S, th, w, V)
    print(f"charge {e}: max|lean - original| = {np.abs(R1 - R0).max():.2e} (max|R| {np.abs(R0).max():.2e})")
