"""R19-32 s5 (pre-registered 07:50Z): numerical check of the TOP-SUPPORT LEMMA (proved in the report):
 with formula lowering parts and Bogoliubov mixing (v_k != 0 for a constrained k, chat_nA != 0 on every slot of the sector),
 V cap W_<top = {0}, W_<top = span of slot configurations with every slot below level d-1.
 Check: in every mixing case with V != 0 (found in s3), dim(V cap W_<top) = 0 and min over unit v in V of the top-level weight;
 control: no-mixing cases have the slot vacuum in V cap W_<top."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from mb import *
def V_of(S):
    M = np.vstack([D.toarray() for D in S.constraints()])
    u, s, vh = np.linalg.svd(M); r = int((s > 1e-9*max(1, s.max())).sum()); return vh[r:].conj().T
for (sec, L, tw, d, nu) in [('vecx', 1, -1, 3, 1.), ('vecx', 1, -1, 5, 1.), ('vecx', 1, -1, 4, 1.), ('vecx', 2, -1, 3, 1.), ('vecx', 2, -1, 5, 1.),
                            ('scal', 1, -1, 3, 1.), ('scal', 1, -1, 5, 1.), ('vecx', 1, -1, 4, 2.), ('vecx', 2, -1, 4, np.sqrt(2)), ('scal', 1, -1, 4, 2.)]:
    S = Sector(sec, L, d, nu, tw); V = V_of(S)
    idx = np.arange(S.dim); occmax = np.zeros(S.dim, int)
    for s_ in range(S.ns): occmax = np.maximum(occmax, (idx // S.d**(S.ns - s_ - 1)) % S.d)
    top = occmax == d - 1
    if V.shape[1] == 0:
        print(f"{sec} L={L} d={d} nu={nu:.4f}: V = 0"); continue
    Vt = V[top]                       # top-level components
    sv = np.linalg.svd(Vt, compute_uv=False) if Vt.size else np.zeros(V.shape[1])
    sv = np.concatenate([sv, np.zeros(V.shape[1] - len(sv))])
    print(f"{sec} L={L} d={d} nu={nu:.4f} (v_k {'!= 0' if abs(nu - S.ws[0]) > 1e-9 else '= 0'}): dim V {V.shape[1]}; dim(V cap W_<top) = {(sv < 1e-9).sum()}; "
          f"min top-level weight over unit v in V = {sv.min()**2:.4f}")
