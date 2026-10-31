"""Post-hoc (informational, not pre-registered): re-run x5 A3(ii) kernel location test with new seeds, more samples."""
import sys, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/.claude/science/toe-ruleset-20261021/agents/ym4d-existence/checks')
import x5_su2_soft as X
for seed in (11, 12, 13):
    rng = np.random.default_rng(seed)
    T = X.haar(rng, (7,))
    T = X.qmul(np.broadcast_to(X.haar(rng, ()), (7, 4)), (T * np.array([3, 1, 1, 1])) / np.linalg.norm(T * np.array([3, 1, 1, 1]), axis=-1, keepdims=True))
    w = rng.dirichlet(np.ones(7)); Mq = (w[:, None] * T).sum(0); r = np.linalg.norm(Mq); Wq = Mq / r; beta = 6.0 / r
    acc = []
    while sum(len(a) for a in acc) < 1_000_000:
        V = X.haar(rng, (2_000_000,)); keep = rng.random(len(V)) < np.exp(beta * (V @ Mq - r)); acc.append(V[keep])
    V = np.concatenate(acc); Z = X.qmul(np.broadcast_to(X.qconj(Wq), V.shape), V)
    zs = [(Z[:, k].mean() / (Z[:, k].std() / np.sqrt(len(Z)))) for k in range(4)]
    print(f"seed {seed}: r={r:.3f} n={len(Z)} (mean q0 - a(6))/SE = {(Z[:,0].mean()-X.a_of_t(6.0))/(Z[:,0].std()/np.sqrt(len(Z))):+.2f}; vector comps / SE = {zs[1]:+.2f} {zs[2]:+.2f} {zs[3]:+.2f}")
