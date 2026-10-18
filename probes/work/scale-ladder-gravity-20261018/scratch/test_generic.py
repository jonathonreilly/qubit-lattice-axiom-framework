import sys, time, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
import regge_generic as RG
t0 = time.time(); OFF, S = RG.kuhn(); K = RG.Complex(OFF, S); print("kuhn built", K.E, "edges,", len(K.terms), "hinges", f"{time.time()-t0:.1f}s")
rng = np.random.default_rng(0)
for _ in range(2):
    k = rng.standard_normal(4)*0.5
    s = R.sv(K.Q(k)); G = K.gauge(k); print("nullity", int((s < 1e-9).sum()), " |QG|", np.abs(K.Q(k) @ G).max())
# pullback symbol vs EH
k = np.array([0.3, -0.2, 0.5, 0.1])*1e-3
Qh = K.line_map(-k).T @ K.Q(k) @ K.line_map(k)
E = np.zeros((10, 10))
for i in range(10):
    for j in range(10):
        ei = np.zeros(10); ej = np.zeros(10); ei[i] = 1; ej[j] = 1
        f = lambda x: R.EH(R.hfull(x), k, np.eye(4)); E[i, j] = 0.25*(f(ei+ej) - f(ei-ej))
lam = np.real(np.trace(Qh.conj().T @ E))/np.trace(E.T @ E)
print("pullback / EH =", lam, " misfit", np.linalg.norm(Qh.real - lam*E)/np.linalg.norm(E*lam))
# compare spectra with the landed module at a momentum
Qe0, _ = R.regge(np.eye(4)); k = np.array([0.4, 0.1, -0.3, 0.2])
print("singular values agree:", np.allclose(np.sort(np.linalg.svd(K.Q(k), compute_uv=False)), np.sort(np.linalg.svd(Qe0(k), compute_uv=False)), atol=1e-7))
