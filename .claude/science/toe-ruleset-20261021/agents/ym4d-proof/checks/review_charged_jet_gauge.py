"""Post-exposure supplement; imports only this reviewer's independent code."""
import json
import numpy as np
from scipy import sparse as sp
from review_charged_jet_independent import Paths, gradient, sites, index, solve, record, witness, checks

rng = np.random.default_rng(88271)
fine = (3, 6, 3, 3)
top = (1, 2, 1, 1)
p = Paths(fine)
c = Paths(fine, "plaquette")
kappa = 0.8
D = sp.vstack([c.Q, -np.sqrt(kappa) * p.Q], format="csr")
v = rng.normal(size=(p.nout, 3)) * 0.3
fixed = np.zeros((D.shape[0], 3))
fixed[-p.nout:] = np.sqrt(kappa) * v
a, stats = solve(D, -fixed, "supplement_linear_stationary")
r = v - p.Q @ a
f = c.Q @ a
B, DB = p.bilinear(a, r)
Bp, DBp = c.bilinear(a, f)
S = c.Q.T @ Bp + DBp + kappa * (p.Q.T @ B - DB)
roots = index(3 * sites(top), 0, fine) // 4
phi = rng.normal(size=(int(np.prod(fine)), 3))
phi[roots] = 0
g = gradient(fine) @ phi
record("rootfixed_gauge_null_D", np.linalg.norm(D @ g), np.linalg.norm(g))
record("source_annihilates_rootfixed_gauge", abs(np.sum(S * g)), np.linalg.norm(S) * np.linalg.norm(g))
record("Moore_Penrose_solution_orthogonal_to_gauge", abs(np.sum(a * g)), np.linalg.norm(a) * np.linalg.norm(g))
witness("full_hidden_inverse_on_null_mutation", np.linalg.norm(g))
x = rng.normal(size=a.shape)
y = rng.normal(size=v.shape)
lhs = float(np.sum(y * (p.Q @ x)))
rhs = float(np.sum(x * (p.Q.T @ y)))
record("literal_counting_adjoint", abs(lhs-rhs), abs(lhs))
bad = abs(lhs-rhs/81)
witness("density_rescaled_adjoint_mutation", bad, max(1e-7,100*abs(lhs-rhs)))
h = np.tile(rng.normal(size=(4,3)), (int(np.prod(fine)),1))
record("constant_harmonic_curl_zero", np.linalg.norm(c.Q @ h), np.linalg.norm(h))
expected = np.tile(3*h[:4], (int(np.prod(top)),1))
record("constant_harmonic_Q_is_L", np.linalg.norm(p.Q @ h-expected), np.linalg.norm(expected))
witness("dropping_harmonic_hidden_soft_cost", np.linalg.norm(D @ h))
result=dict(scope="post-author-exposure gauge/counting supplement",checks=checks,passed=sum(x['pass_'] for x in checks),total=len(checks),linear_solver=stats)
print(json.dumps(result,indent=2,allow_nan=False))
raise SystemExit(0 if all(x['pass_'] for x in checks) else 1)
