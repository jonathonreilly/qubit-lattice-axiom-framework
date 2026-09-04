"""
T254 - the actual mechanism behind R169: the Born weight's STIFFNESS falls as 1/k.

Two explanations have now been refuted:
  contrast  n/k        -- refuted by R169 (M8 rank 2 and M12 rank 3 have
                          contrast 4.0, same as rank 1, and disorder anyway)
  target size dim Gr   -- refuted by T253 (Gr(2,3) has dim 4 < CP^3's 6 and
                          disorders anyway)

Third candidate, with a formula: at alignment Tr(P P') -> k, so
      -log Tr(P P') = -log k + (1/k) * (something quadratic in the separation)
i.e. the coupling that resists misalignment is weakened by 1/k.  Measured here
by fitting the small-separation behaviour directly.
"""
import numpy as np
rng = np.random.default_rng(331)

def orth(A):
    k=A.shape[-1]; cols=[]
    for j in range(k):
        v=A[...,j]
        for u in cols: v=v-np.sum(np.conj(u)*v,axis=-1,keepdims=True)*u
        v=v/np.maximum(np.linalg.norm(v,axis=-1,keepdims=True),1e-300); cols.append(v)
    return np.stack(cols,axis=-1)
Pj = lambda Q: Q @ Q.conj().T

print("fit  -log Tr(P P')  vs  the projector separation  D = ||P - P'||_F^2 / 2")
print("small-D slope is the stiffness that resists misalignment\n")
print(f"{'algebra, rank':22s} {'Tr at alignment':>16s} {'stiffness':>11s} {'1/k':>7s} {'x k':>7s}")
for (n,k) in ((4,1),(3,2),(4,2),(8,2),(12,3),(8,4)):
    Ds, Ls = [], []
    for _ in range(6000):
        A = rng.normal(size=(n,k))+1j*rng.normal(size=(n,k))
        Q = orth(A)
        eps = 10**rng.uniform(-2.2,-1.0)
        Q2 = orth(Q + eps*(rng.normal(size=(n,k))+1j*rng.normal(size=(n,k))))
        P1, P2 = Pj(Q), Pj(Q2)
        D = np.linalg.norm(P1-P2,'fro')**2/2
        t = np.real(np.trace(P1@P2))
        Ds.append(D); Ls.append(-np.log(t) + np.log(k))
    Ds, Ls = np.array(Ds), np.array(Ls)
    m = Ds < 0.05
    slope = np.sum(Ds[m]*Ls[m])/np.sum(Ds[m]**2)      # through the origin
    print(f"  M{n}(C) rank {k:1d}        {k:16d} {slope:11.5f} {1/k:7.4f} {slope*k:7.4f}")

print("""
=== reading ===
  The stiffness is 1/k to good accuracy at every rank tested: the Born weight
  resists misalignment k times more weakly at rank k than at rank 1.

  So neither contrast nor target size explains R169 -- the coupling itself is
  weakened by the normalisation Tr(P P') -> k at alignment.  Rank 1 orders
  because it is the ONLY rank at which the Born weight couples at full strength.""")
