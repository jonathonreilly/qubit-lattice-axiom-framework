"""Dilation (trace) channel of the bulk flow for the nn KG scalar, RN-L1 normalization v = (1/2) h grad u, h = I.
p = dE/de = -<(div v) eps>, mu_D = <eps J''>.  Compact-gauge covariance would need mu_E = mu_T2 (= -2p in the
linear parametrization of the metric); the flow gives mu_T2 = 0, mu_E = F(M)."""
import numpy as np
N = 64
k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
X, Y, Z = np.meshgrid(k, k, k, indexing='ij')
out = []
for m in (0.5, 1.0):
    om = np.sqrt(m*m + 2*(3 - np.cos(X) - np.cos(Y) - np.cos(Z)))
    eps = om/2
    v = [0.5*np.sin(X), 0.5*np.sin(Y), 0.5*np.sin(Z)]
    div = 0.5*(np.cos(X) + np.cos(Y) + np.cos(Z))
    # grad(div) . v
    gdiv_v = -0.25*(np.sin(X)**2 + np.sin(Y)**2 + np.sin(Z)**2)
    p = -np.mean(div*eps)
    muD = np.mean(eps*(div**2 + gdiv_v))
    out.append(f'm={m}: p (trace linear response) = {p:+.6e}, mu_D = {muD:+.6e}, -2p = {-2*p:+.6e}')
print('\n'.join(out)); open('s1_dilation.out','w').write('\n'.join(out)+'\n')
