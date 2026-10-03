"""Sanity for 7b: LOC must be feasible for unlinked (product) possibilities."""
import numpy as np
import t7b_no_signalling_nn as m
from common import rand_state, haar_unitary
rng = np.random.default_rng(5)
ok_prod, ok_mix = 0, 0
for tr in range(50):
    Psi = np.kron(rand_state(4, rng), rand_state(4, rng))
    UA = [m.region_gate([haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(2)]
    UB = [m.region_gate([haar_unitary(2, rng), haar_unitary(2, rng)]) for _ in range(2)]
    ok_prod += m.solve(Psi, UA, UB, 'LOC')
    # weakly linked: product + 5% random linked part
    Psi2 = Psi + 0.05 * rand_state(16, rng); Psi2 /= np.linalg.norm(Psi2)
    ok_mix += m.solve(Psi2, UA, UB, 'LOC')
print(f"LOC feasible for unlinked possibilities: {ok_prod}/50; weakly linked (5%): {ok_mix}/50")
