"""RL1 (F6): grid check of the stable member's mean-inverse tail at tau = 30..40 (is the tau=40 uptick numerical?).
Varies the tau step and the number of tau1 nodes on the long piece."""
import numpy as np
from scipy.special import gammaln
src = open("RL1_B_bd_mean_volterra.py").read().split('if __name__ == "__main__":')[0]
C = np.load("RL1_F4b_stable_L6.npy")[0]; L = 6
def fstab(s):
    m = np.pi*np.asarray(s, float)**2/24
    return np.exp(-m)*sum(C[n]*m**n/np.exp(gammaln(n+1)) for n in range(L))
for nb, h in [(120, 0.05), (240, 0.05), (240, 0.025)]:
    g = {}
    exec(src.replace("leggauss(120)", "leggauss(%d)" % nb), g)
    taus, H = g["solve"](fstab, 42.0, 0.02, h)
    print("nb=%d h=%.3f: " % (nb, h) + "  ".join("H(%g)=%+.2e" % (T, np.interp(T, taus, H)) for T in [20, 25, 30, 35, 38, 40, 42]), flush=True)
