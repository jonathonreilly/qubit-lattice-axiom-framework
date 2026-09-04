"""Continuum reference: (1/2) Int R sqrt(g) d^4x for g = diag(1+eps P_mu cos(k x0)).
Fully numerical (finite differences in x0), independent of the Regge code."""
import numpy as np, math

def metric(t, eps, P, k):
    return np.diag(1.0+eps*np.asarray(P,float)*np.cos(k*t))

def christoffel(t, eps, P, k, h=1e-5):
    g  = metric(t,eps,P,k); gi = np.linalg.inv(g)
    dg = np.zeros((4,4,4))   # dg[a] = partial_a g
    dg[0] = (metric(t+h,eps,P,k)-metric(t-h,eps,P,k))/(2*h)
    Ga = np.zeros((4,4,4))   # Ga[a,b,c] = Gamma^a_{bc}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                s = 0.0
                for d in range(4):
                    s += gi[a,d]*(dg[b][d,c]+dg[c][d,b]-dg[d][b,c])
                Ga[a,b,c] = 0.5*s
    return Ga

def ricci_scalar(t, eps, P, k, h=1e-4):
    g = metric(t,eps,P,k); gi = np.linalg.inv(g)
    G  = christoffel(t,eps,P,k)
    dG = np.zeros((4,4,4,4))  # dG[e][a,b,c] = partial_e Gamma^a_{bc}
    dG[0] = (christoffel(t+h,eps,P,k)-christoffel(t-h,eps,P,k))/(2*h)
    # R^a_{bcd} = d_c G^a_{db} - d_d G^a_{cb} + G^a_{ce}G^e_{db} - G^a_{de}G^e_{cb}
    R = (np.einsum('cabd->abcd', dG.transpose(0,1,3,2)*0 + np.einsum('cadb->cabd',dG))
         )  # placeholder, do explicit loops for clarity
    Ric = np.zeros((4,4))
    for b in range(4):
        for d in range(4):
            s = 0.0
            for a in range(4):
                s += dG[a][a,d,b] - dG[d][a,a,b]
                for e in range(4):
                    s += G[a][a,e]*G[e][d,b] - G[a][d,e]*G[e][a,b]
            Ric[b,d] = s
    return float(np.einsum('bd,bd->', gi, Ric)), float(math.sqrt(np.linalg.det(g)))

def action(L, eps, P, k, N=4096):
    ts = (np.arange(N)+0.5)*L/N
    tot = 0.0
    for t in ts:
        R, sg = ricci_scalar(t,eps,P,k)
        tot += R*sg
    return 0.5*tot*(L/N)*L**3

def volume(L, eps, P, k, N=4096):
    ts = (np.arange(N)+0.5)*L/N
    return sum(math.sqrt(np.linalg.det(metric(t,eps,P,k))) for t in ts)*(L/N)*L**3
