"""E1: exact counterexample to C + Markov-L (no settings needed), and C + NS feasibility.

A: one bond {L=0, R=1}.  B: ring Z_5 with the conveyor tick (shift +1).
psi_0 = (|+>|0> + |->|1>)/sqrt2 .  Tick 0: A applies H (s=1) or identity (s=0);
B shifts.  Tick 1 (for the 3-time runs): A applies H or identity again; B shifts.

Expected (EXACT, see report):
  B's transport (1/2,1/2,0,..) -> (0,1/2,1/2,..) is forced: b' = b+1.
  With s=1 Born_{1} = 1/2[(L,1)+(R,2)], so a_1 = L iff b_0 = 0 while a_0 is uniform and
  independent of b_0: A's move odds must depend on B's position  => Markov-L infeasible.
"""
import numpy as np
from mtlp import Model, history_lp, markov_local_lp, ring_adj, H2

I2 = np.eye(2, dtype=complex)
nB = 5
S = np.roll(np.eye(nB), 1, axis=0).astype(complex)       # |b> -> |b+1>
plus = np.array([1, 1]) / np.sqrt(2)
minus = np.array([1, -1]) / np.sqrt(2)
e0 = np.eye(nB)[0]
e1 = np.eye(nB)[1]
psi0 = (np.kron(plus, e0) + np.kron(minus, e1)) / np.sqrt(2)
movA = np.ones((2, 2), bool)          # bond: any move is one step
movB = ring_adj(nB)

for T in (1, 2):
    UA = [[I2, H2] for _ in range(T)]
    UB = [[S] for _ in range(T)]
    m = Model(psi0, UA, UB, [movA] * T, [movB] * T)
    print(f"--- T = {T} tick(s); A settings {{1, H}} each tick; B = conveyor ---")
    for sig in m.sigmas():
        P = m.born(sig)
        nz = [(a, b, round(P[a, b], 6)) for a in range(2) for b in range(nB) if P[a, b] > 1e-12]
        print(f"  sigma={sig}: Born_T support {nz}")
    lp, idx = history_lp(m, ns=False)
    print("  C (+causality) alone      :", lp.solve().status == 0)
    lp, idx = history_lp(m, ns=True)
    print("  C + NS (multi-tick, both) :", lp.solve().status == 0)
    for k in range(T):
        res, *_ = markov_local_lp(m, k)
        print(f"  C + Markov-L at tick {k}    :", res.status == 0, f"(HiGHS status {res.status}: {res.message[:40]})")
