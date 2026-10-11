import numpy as np, warnings
warnings.filterwarnings('ignore')
import importlib.util, sys
spec = importlib.util.spec_from_file_location('c', 's1_checks.py')
# reuse only the functions: exec the def part
src = open('s1_checks.py').read().split("out = []")[0]
exec(src)
P = print
P('scan b=0 (separable u = c + a c^2): a, muE(m=1), min u')
for a in np.linspace(-0.24, 0.6, 15):
    P(f'{a:+.3f}', mu_channels(1.0, 48, a=a), round(umin(a,0,0),4))
P('scan a=0: b, (muE, muT2)(m=1), min u')
for b in np.linspace(-0.4, 1.0, 15):
    P(f'{b:+.3f}', mu_channels(1.0, 48, b=b), round(umin(0,b,0),4))
P('scan g (body-diag admixture), a=b=0: g, (muE, muT2)')
for g in (-0.3, -0.1, 0.0, 0.3, 1.0, 3.0):
    P(g, mu_channels(1.0, 48, g=g), round(umin(0,0,g),4))
