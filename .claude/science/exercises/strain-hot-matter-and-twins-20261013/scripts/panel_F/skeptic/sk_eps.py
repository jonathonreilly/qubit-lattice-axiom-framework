"""Is the root's odd box symbol compatible with the staggered U(1)_eps (s(k+pi) = -s(k)), and is the SF flow
vector field of the r=0 band pi-periodic per axis (so Phi_t commutes with k -> k + (pi,pi,pi))?"""
import sys, numpy as np
sys.path.insert(0, '/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790/.claude/science/exercises/gravity-current-state-20261009/scripts/C5/R18-5')
from dirac import D1
L = D1(0.909103708, 0.555604226)
k = np.linspace(-np.pi, np.pi, 200001)
s, sp = L.S(k), L.S(k + np.pi)
print('max |s(k+pi) + s(k)| =', np.max(np.abs(sp + s)))
# SF vector field per axis for E^2 = sum s(k_j)^2 (r = 0): p_j = s(k_j) s'(k_j)
p = L.S(k)*L.dS(k); pp = L.S(k+np.pi)*L.dS(k+np.pi)
print('max |p(k+pi) - p(k)| =', np.max(np.abs(pp - p)))
# contrast: Wilson part W is not anti-periodic
W, Wp = L.W(k), L.W(k + np.pi)
print('max |W(k+pi) + W(k)| (Wilson breaks eps) =', np.max(np.abs(Wp + W)))
