# probe: are the 24 improper dressed lifts symmetries of the eight-node step (unitary, possibly with W -> W^dag)?
from c1lib import *
rng = np.random.default_rng(3); KT = rng.uniform(-np.pi, np.pi, (3, 3))
INVM = -np.eye(3)
res = []
for R, (P, s) in zip(ROTS, invs):
    U = fibre_matrix(P, s); M = (R @ INVM).astype(float)
    hit = []
    for th in itertools.product((0, 1), repeat=3):
        th = np.pi * np.array(th)
        for lab, f in (("W", lambda k: W(k)), ("W^dag", lambda k: W(k).conj().T), ("-W", lambda k: -W(k)), ("-W^dag", lambda k: -W(k).conj().T)):
            if all(np.allclose(U @ W(k) @ U.T, f(M @ k + th), atol=1e-9) for k in KT): hit.append((lab, (th / np.pi).astype(int).tolist()))
    res.append(hit)
print("improper lifts that map W to W / W^dag / -W / -W^dag at some affine image:", sum(bool(h) for h in res), "of 24;", [h for h in res if h][:4])
# antiunitary candidates: V W(k)^* V^dag = W(Mk+th)^{+-1} with V a dressed (proper or improper) lift
cnt = 0
for lifts, Mf in ((rots, lambda R: R), (invs, lambda R: R @ INVM)):
    for R, (P, s) in zip(ROTS, lifts):
        U = fibre_matrix(P, s); M = Mf(R).astype(float)
        for th in itertools.product((0, 1), repeat=3):
            th = np.pi * np.array(th)
            for f in (lambda k: W(k), lambda k: W(k).conj().T, lambda k: -W(k), lambda k: -W(k).conj().T):
                if all(np.allclose(U @ W(k).conj() @ U.T, f(M @ k + th), atol=1e-9) for k in KT): cnt += 1
print("antiunitary (lift x complex conjugation) candidates found:", cnt)
