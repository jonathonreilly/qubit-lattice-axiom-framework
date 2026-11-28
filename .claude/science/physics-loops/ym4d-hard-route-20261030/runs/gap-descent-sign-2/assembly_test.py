"""GUIDE check for row 1085: the contraction in tplaq.py (tensor R, weights, einsum) against a brute-force sum
with the Gram-tested coefficients of gram_test.py, sector s_x = s_y = 1/2, with the K_Phi weights of the final state."""
import numpy as np, tplaq, gram_test
A, D = 4, 4
S = tplaq.setup(A, D)
rng = np.random.default_rng(3)
bM = 3.0
u = tplaq.uvec(bM, 40)
G = np.zeros((S['big'], S['big'])); G[:A, :A] = rng.normal(size=(A, A))
worst = 0.0
for (nI, nII) in ((1, 3), (2, 2)):
    wq = np.array([(JI+1)*(JII+1)*u[JI]**nI*u[JII]**nII for (JI, JII) in S['PJ']])
    upp = np.array([[u[j], u[jp]] for (j, jp) in S['PP']]); kf = upp[:, 0]**nI * upp[:, 1]**nII
    amp = np.einsum('q,qka,ab,qjb->kj', wq, S['R'], G, S['R'], optimize=True)
    v1 = float(np.sum(kf[:, None]*kf[None, :]*amp**2))
    acc = {}
    for (JI, JII) in S['PJ']:
        for a in range(A):
            for b in range(A):
                for st, c in gram_test.coefs(JI, JII, a, b).items():
                    if st[4] == 1 and st[5] == 1:
                        acc[st] = acc.get(st, 0.0) + (JI+1)*(JII+1)*u[JI]**nI*u[JII]**nII*G[a, b]*c
    v2 = sum(v*v*u[j]**nI*u[jp]**nII*u[k]**nI*u[kp]**nII for (j, jp, k, kp, sx, sy), v in acc.items())
    print(f"arcs ({nI},{nII}): einsum {v1:.12e}  brute {v2:.12e}  rel diff {abs(v1-v2)/v2:.1e}")
