"""Hopping range of the root D1 edge: odd harmonics (s(pi-k)=s(k) kills even ones)."""
import sys, numpy as np
sys.path.insert(0, '/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790/.claude/science/exercises/gravity-current-state-20261009/scripts/C5/R18-5')
from dirac import D1
L = D1(0.909103708, 0.555604226)
K = 2**18
k = (np.arange(K) + 0.5)*2*np.pi/K - np.pi
s = L.S(k); W = L.W(k)
print(' n    |s_n|        |W_n|')
for n in (1,3,5,7,9,11,15,21,31,41,61,81,101,151,201,301):
    print('%4d  %.3e    %.3e' % (n, abs(np.mean(s*np.sin(n*k))*2), abs(np.mean(W*np.cos(n*k))*2)))
