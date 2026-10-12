"""R13-8 script C: box variant of the one-loop TT witness (literal box profile L of R7-1/R9-9:
s(k) = r k + (1-r) sin k with smooth plateau r, B=2.0, B2=3.1; eps^2 = m^2 + sum s(k_i)^2).
Vertex: V_ij(k,k') = -1/2[s_i(k)s_j(k') + s_j(k)s_i(k')], k' = -k-q  (R9-9's M vertex at q=0)."""
import numpy as np, os
BOXB, BOXB2 = 2.0, 3.1
def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def wrap(k): return -(((-k) + np.pi) % (2*np.pi) - np.pi)
def s_L(k):
    k = wrap(k); r = sstep((BOXB2 - np.abs(k))/(BOXB2 - BOXB)); return r*k + (1-r)*np.sin(k)
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "r138_onshell_loop.py")).read()
head, tail = src.split("# ---------------- one-loop witness ----------------")
exec(head.split("dirs = [v / np.linalg.norm(v)")[0])
NG = int(os.environ.get("NG", "40"))
def scalar_loop_tt(m, w, q, Ngrid=NG):
    ks = 2*np.pi*(np.arange(Ngrid) + 0.5)/Ngrid - np.pi
    K = np.stack(np.meshgrid(ks, ks, ks, indexing="ij"), -1).reshape(-1, 3)
    Kp = -K - q[None, :]
    S1, S2 = s_L(K), s_L(Kp)
    e1 = np.sqrt(m*m + (S1**2).sum(-1)); e2 = np.sqrt(m*m + (S2**2).sum(-1))
    V = -0.5*(S1[:, :, None]*S2[:, None, :] + S1[:, None, :]*S2[:, :, None])
    qn = q/np.linalg.norm(q)
    E = tt_basis(qn); pol = []
    for a in range(2):
        H = np.zeros((4, 4))
        for A, (x, y) in enumerate(SYM):
            H[x, y] = E[A, a]; H[y, x] = E[A, a]
        pol.append(H[1:, 1:])
    W = np.stack([np.einsum("nij,ij->n", V, P) for P in pol], 1)
    F = (e1 + e2)/(e1*e2*((e1 + e2)**2 - w*w))
    return (-np.einsum("na,nb,n->ab", W, W, F)/K.shape[0]), E
tail2 = tail.replace("np.array2string(sA, precision=3)", "np.array2string(sA, formatter={\"float_kind\": lambda v: f\"{v:.3e}\"})").replace('mons2, N2, F2 = res["O_h x T"]', 'mons2, N2 = invariant_forms(G_C_PT, 2)').replace("def scalar_loop_tt(", "def scalar_loop_tt_nn(")
print(f"[box witness] profile L (B=2.0, B2=3.1), Ngrid={NG}")
exec(tail2, globals())
