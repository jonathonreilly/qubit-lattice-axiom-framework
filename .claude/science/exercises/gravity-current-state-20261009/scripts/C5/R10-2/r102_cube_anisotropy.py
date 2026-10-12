# R10-2 part 3 (proxy for the one-loop O(q^0) graviton mass forms).
# For a minimal-type one-loop vacuum polarization at q=0, Pi^{abcd}(0) ~ int_BZ v_a v_b v_c v_d G^2,
# with v the vertex symbol. O(4) needs int v1^4 G^2 = 3 int v1^2 v2^2 G^2, i.e. R = 1, where
# R := int v1^4 G^2 / (3 int v1^2 v2^2 G^2). R != 1 is the W(B4)-only mass split (K1's M1 vs M2 on TT).
import numpy as np
def step(x):
    x = np.clip(x, 0, 1)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        a = np.where(x > 0, np.exp(-1/np.where(x > 0, x, 1)), 0.0)
        b = np.where(x < 1, np.exp(-1/np.where(x < 1, 1-x, 1)), 0.0)
    return a/(a+b)
def s_box(k, b=2.0, b2=3.1):
    r = step((b2-np.abs(k))/(b2-b)); return r*k + (1-r)*np.sin(k)
n = 56
k = (np.arange(n)+0.5)/n*2*np.pi - np.pi
m2 = 0.25
K1, K2, K3, K4 = np.meshgrid(k, k, k, k, indexing='ij', sparse=True)
def R_of(v, G2):
    v1, v2 = v[0], v[1]
    num = np.sum(v1**4*G2); den = 3*np.sum(v1**2*v2**2*G2); return num/den
rows = []
# (i) NN control: v = sin k, G = 1/(sum 4 sin^2(k/2)+m^2)
v = [np.sin(K1), np.sin(K2)]
G2 = 1/(4*(np.sin(K1/2)**2+np.sin(K2/2)**2+np.sin(K3/2)**2+np.sin(K4/2)**2)+m2)**2
rows.append(('NN (sin vertex, NN propagator)', R_of(v, G2)))
# (ii) whole-zone SLAC on the cube
p2 = K1**2+K2**2+K3**2+K4**2
rows.append(('whole-zone SLAC (v=k, G=1/(k^2+m^2) on cube)', R_of([K1, K2], 1/(p2+m2)**2)))
# (iii) C^infty box law, all modes in the loop (edge included)
S = [s_box(K1), s_box(K2), s_box(K3), s_box(K4)]
G2b = 1/(S[0]**2+S[1]**2+S[2]**2+S[3]**2+m2)**2
rows.append(('C^inf box law, loop over whole zone (edge modes in)', R_of([S[0], S[1]], G2b)))
# (iv) same with an O(4) ball-supported vertex form factor chi(|k|) (radius a=1.9 < b=2.0): non-RP class
chi = step((1.9-np.sqrt(p2))/0.6)
rows.append(('box law + O(4) ball form factor chi^4 (a=1.9)', R_of([S[0], S[1]], G2b*chi**4)))
for name, R in rows:
    print('%-58s R = %.6f   (R-1 = %+.3e)' % (name, R, R-1))
print('grid n=%d per axis (midpoint rule); m^2=%.2f. Ball case: deviation from 1 is quadrature error of a ball on a cubic grid.' % (n, m2))
