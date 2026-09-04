"""Schlaefli identity test: sum_h A_h dtheta_h = 0 for arbitrary variation of a
4-simplex's squared edge lengths.  This is what makes dS_Regge = sum_h delta_h dA_h,
i.e. the deficit-angle terms drop out of finite differences of S."""
import numpy as np, math, itertools
from geom import ip, HINGES, hinge_area_angle

def from_l2(l2):
    G = np.empty((4,4))
    for a in range(1,5):
        for b in range(1,5):
            G[a-1,b-1] = 0.5*(l2[0,a]+l2[0,b]-l2[a,b])
    Gt = np.zeros((5,5)); Gt[1:,1:] = G
    return Gt

def areas_angles(l2):
    Gt = from_l2(l2)
    A = []; TH = []
    for tri, rest in HINGES:
        a, t = hinge_area_angle(Gt, tri, rest); A.append(a); TH.append(t)
    return np.array(A), np.array(TH)

rng = np.random.default_rng(7)
# random non-degenerate 4-simplex: embed 5 random points, take squared distances
pts = rng.normal(size=(5,4))
l2 = ((pts[:,None,:]-pts[None,:,:])**2).sum(-1)
A0, TH0 = areas_angles(l2)
print("sum theta over 10 hinges (regular-ish simplex check, must be >0):", TH0.sum())
h = 1e-6
worst = 0.0; worstA = 0.0
for (a,b) in itertools.combinations(range(5),2):
    lp = l2.copy(); lp[a,b]+=h; lp[b,a]+=h
    lm = l2.copy(); lm[a,b]-=h; lm[b,a]-=h
    Ap,THp = areas_angles(lp); Am,THm = areas_angles(lm)
    dTH = (THp-THm)/(2*h); dA = (Ap-Am)/(2*h)
    worst = max(worst, abs(A0@dTH))
    worstA = max(worstA, np.abs(dA).max())
print("max |sum_h A_h dtheta_h/dl2_e| over 10 edges :", worst)
print("typical scale |dA/dl2| :", worstA)
