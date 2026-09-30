"""Kill check T49: what does the massive covariant NEAREST-NEIGHBOUR pairing (1,0,0) actually do?
Compare BdG spectrum of [[hm, lam*D],[-lam*D, -hm]] with lam=0 (full spectrum, not only the light levels)."""
import sys, numpy as np
sys.argv = ['x', '8']
exec(open('massive_bdg.py').read().split('RM = 2 if L == 8 else 3')[0])
val = all_invariants((1, 0, 0))[0]
Delta = np.zeros((N, N))
for (i, j), x in val.items(): Delta[i, j] = x; Delta[j, i] = -x
print("NN pairing: pairs", len(val), " Delta symmetric-part norm", np.abs(Delta + Delta.T).max())
E0 = np.sort(np.linalg.eigvalsh(np.block([[hm, 0*Delta], [0*Delta, -hm]])))
for lam in [0.1, 0.3, 0.6, 1.0]:
    H = np.block([[hm, lam * Delta], [-lam * Delta, -hm]])
    E = np.sort(np.linalg.eigvalsh(H))
    a = np.sort(np.abs(E))
    print(f"lam={lam}: max |E - E0| over full BdG spectrum = {np.abs(E-E0).max():.4f};  lowest |E| = {a[:2]},  16th = {a[15]:.4f};  max|E| {np.abs(E).max():.4f} vs {np.abs(E0).max():.4f}")
# is pairing conserving a different U(1)? test: does [Delta-part, hop-part structure] permit a Bogoliubov rotation?  Check whether Delta commutes with h (same sign structure as hop restricted to NN bonds)
Hop = np.zeros((N, N))
for (i, j), e in hop.items(): Hop[i, j] = e
print("Delta vs hop: ||Delta - Hop*sign||? overlap |<Delta,Hop>|/(|Delta||Hop|) =", abs(np.sum(Delta*Hop))/np.linalg.norm(Delta)/np.linalg.norm(Hop))
print("bond pattern: fraction of NN bonds carrying nonzero Delta:", (np.abs(np.triu(Delta)) > 0).sum() / (3*N))
