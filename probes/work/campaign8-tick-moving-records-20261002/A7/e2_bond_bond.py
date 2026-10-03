"""E2: two distant bonds, linked possibilities (Bell pair), CHSH tick choices.

A, B: one bond each (sites 0,1).  psi_0 = (|00> + |11>)/sqrt2.
Tick k: A applies rot(alpha_s), B applies rot(beta_r), settings at every tick.
alpha in {0, pi/4}, beta in {pi/8, -pi/8}  (CHSH-optimal for real rotations).

Checks
  (a) CHSH value of the Born odds of the record positions after one tick (EXACT: 2 sqrt2).
      Any rule where the two moves are independent given the full past and each uses only
      its own setting obeys CHSH <= 2 (Bell)  ->  C + L_Bell impossible.
  (b) C + Markov-L (moves' odds local, joint correlation free) at every tick: LP.
  (c) The correlated forgetful re-draw: verify C + Markov-L exactly (constructive).
  (d) C + NS over 2 and 3 ticks (history LP).
  (e) How much memory can a C + Markov-L rule keep?  LP: maximise P(b_{k+1} = b_k).
"""
import numpy as np
from mtlp import Model, history_lp, markov_local_lp, rot

alphas = [0.0, np.pi / 4]
betas = [np.pi / 8, -np.pi / 8]
psi0 = np.array([1, 0, 0, 1], complex) / np.sqrt(2)
mov = np.ones((2, 2), bool)

# (a) CHSH of Born odds after one tick
E = np.zeros((2, 2))
for s in range(2):
    for r in range(2):
        P = (np.abs(np.kron(rot(alphas[s]), rot(betas[r])) @ psi0) ** 2).reshape(2, 2)
        E[s, r] = P[0, 0] + P[1, 1] - P[0, 1] - P[1, 0]
chsh = E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1]
print(f"(a) CHSH of record positions after one tick = {chsh:.12f}  (2*sqrt2 = {2*np.sqrt(2):.12f})")

for T in (1, 2, 3):
    UA = [[rot(a) for a in alphas] for _ in range(T)]
    UB = [[rot(b) for b in betas] for _ in range(T)]
    m = Model(psi0, UA, UB, [mov] * T, [mov] * T)
    ok_ml = [markov_local_lp(m, k)[0].status == 0 for k in range(T)]
    lp, idx = history_lp(m, ns=True)
    ok_ns = lp.solve().status == 0
    print(f"T={T}: (b) C + Markov-L per tick: {ok_ml};  (d) C + NS (history LP, {lp.nv} vars): {ok_ns}")

# (c) constructive forgetful re-draw: pi = P_k (x) P_{k+1}; check Markov-L exactly
T = 3
UA = [[rot(a) for a in alphas] for _ in range(T)]
UB = [[rot(b) for b in betas] for _ in range(T)]
m = Model(psi0, UA, UB, [mov] * T, [mov] * T)
worst = 0.0
for sig in m.sigmas():
    for k in range(T):
        P0 = m.born(sig[:k]); P1 = m.born(sig[:k + 1])
        pi = np.einsum('ab,cd->abcd', P0, P1)        # (a,b) -> (a',b'), independent of (a,b)
        # B's move odds given (a,b): sum_a' pi / P0 = P1_B(b')  for every a
        TB = pi.sum(axis=2) / P0[:, :, None]
        worst = max(worst, np.abs(TB - P1.sum(axis=0)[None, None, :]).max())
        TA = pi.sum(axis=3) / P0[:, :, None]
        worst = max(worst, np.abs(TA - P1.sum(axis=1)[None, None, :]).max())
        worst = max(worst, np.abs(pi.sum(axis=(0, 1)) - P1).max(), np.abs(pi.sum(axis=(2, 3)) - P0).max())
print(f"(c) correlated forgetful re-draw: max deviation from C / Markov-L = {worst:.1e}")


# (e) maximal memory: maximise P(b_1 = b_0) at tick 0 (setting pair (s,r)) under C + Markov-L
def c_fn_factory(target_sig):
    def c_fn(lp, pis, TA, TB, model, k):
        c = np.zeros(lp.nv)
        for (a, b, a2, b2), j in pis[target_sig].items():
            if b2 == b:
                c[j] = -1.0
        return c
    return c_fn


m1 = Model(psi0, [[rot(a) for a in alphas]], [[rot(b) for b in betas]], [mov], [mov])
for sig in m1.sigmas():
    res, pis, TA, TB = markov_local_lp(m1, 0, c_fn=c_fn_factory(sig))
    print(f"(e) setting pair {sig[0]}: max P(B stays) under C + Markov-L = {-res.fun:.6f}"
          f"   [forgetful value 0.5]")
# and jointly maximise the sum over all four setting pairs of P(B stays)+P(A stays)
def c_all(lp, pis, TA, TB, model, k):
    c = np.zeros(lp.nv)
    for sig, var in pis.items():
        for (a, b, a2, b2), j in var.items():
            c[j] -= (b2 == b) + (a2 == a)
    return c
res, pis, TA, TB = markov_local_lp(m1, 0, c_fn=c_all)
print(f"(e') max of sum over 4 setting pairs of [P(A stays)+P(B stays)] = {-res.fun:.6f}  (forgetful: 4.0, full memory: 8.0)")
