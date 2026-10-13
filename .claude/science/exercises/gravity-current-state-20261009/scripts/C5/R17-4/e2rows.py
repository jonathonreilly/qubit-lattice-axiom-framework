"""R17-4: off-axis U rows under the E2 (product) extension. Expansion in q = s n:
V_E2 = V0 + s^2 V2, V0 = e:ff, V2 = (1/4) sum_ij e_ij [n_i^2 f''_i f_j - n_i n_j f'_i f'_j]  (first order cancels for symmetric e),
so Xi_E2 = Xi_E1 - (1/4) <V0 V2 / eps^3>. Checked against the direct-grid E2 numbers (ext_e2.out) on NN."""
import numpy as np, sympy as sp, sys, time; sys.path.insert(0, '.')
from offaxis import Moments, POLS, xi_off
from math import gamma
fx = sp.symbols('f0:3'); fpx = sp.symbols('fp0:3'); fppx = sp.symbols('fpp0:3')
def e2terms(name):
    n, e = POLS[name]; n = [float(x) for x in n]
    V0 = sum(float(e[i, j])*fx[i]*fx[j] for i in range(3) for j in range(3))
    V2 = sum(float(e[i, j])*(n[i]**2*fppx[i]*fx[j] - n[i]*n[j]*fpx[i]*fpx[j]) for i in range(3) for j in range(3))/4
    ex = sp.expand(-V0*V2/4); out = []
    for mon, c in sp.Poly(ex, *(fx + fpx + fppx)).terms():
        exps = tuple((mon[i], mon[3+i], mon[6+i]) for i in range(3))
        if any((a + cc) % 2 for (a, b, cc) in exps): continue   # f, f'' odd; f' even
        out.append((float(c), exps))
    return out
class Mom2(Moments):
    def __init__(self, law, m, **kw):
        super().__init__(law, m, **kw)
        n1 = len(self.s); kk = 2*np.pi*(np.arange(n1)+0.5)/n1 - np.pi; a = np.abs(kk); sg = np.sign(kk)
        sig = law.sig; spv = law.sp; k = law.k
        fl = sig*spv; fpl = np.gradient(fl, k); fppl = np.gradient(fpl, k)
        self.fp2 = np.interp(a, k, fpl); self.fpp = sg*np.interp(a, k, fppl)
    def m3(self, key):
        if ('e2',) + key not in self.cache:
            a, b, c = key; w = self.f**a * self.fp2**b * self.fpp**c; out = np.empty(len(self.t))
            for i0 in range(0, len(self.t), self.chunk):
                E = np.exp(-np.outer(self.t[i0:i0+self.chunk], self.g)); out[i0:i0+self.chunk] = E @ w/len(self.g)
            self.cache[('e2',) + key] = out
        return self.cache[('e2',) + key]
    def corr(self, terms):
        t, m = self.t, self.m; tot = 0.0
        for c, exps in terms:
            prod = np.ones_like(t)
            for ex in exps: prod = prod*self.m3(ex)
            tot += c*np.sum(t*self.du*t**0.5*np.exp(-t*m*m)*prod)/gamma(1.5)
        return tot
def rows_E2(law, m, **kw):
    X1, mom = xi_off(law, m, 'U', mom=Mom2(law, m, **kw))
    return {nm: X1[nm] + mom.corr(e2terms(nm)) for nm in X1}, X1
if __name__ == '__main__':
    from validate import NN
    T0 = time.time(); nn = NN()
    for m in [1.0, 0.5]:
        X2, X1 = rows_E2(nn, m)
        print('NN m=%.1f E2 rows: %s' % (m, ' '.join('%s %+.6e' % (k, v) for k, v in X2.items())), flush=True)
    import numpy as np
    from zz import ZLaw, Mix
    from floor_scan import Zz
    NF = 1 << 16
    A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF); C2 = Zz(1.0, 0.35, 0.47, 0.03); C = Zz(1.0, 0.35, 0.43, 0.03)
    for nm, L in [('A', A), ('C2', C2), ('C', C), ('U zero m=0.1', Mix([A, C2, C], [1-0.964879-0.007410, 0.964879, 0.007410]))]:
        X2, X1 = rows_E2(L, 0.1)
        print('%-13s m=0.1  E1: %s\n%-13s        E2: %s' % (nm, ' '.join('%s %+.3e' % kv for kv in X1.items()), '', ' '.join('%s %+.3e' % kv for kv in X2.items())), flush=True)
    print('runtime %.1fs' % (time.time()-T0))
