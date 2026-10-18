from chklib import *
print('onsite basis dim', len(ONSITE_BASIS), all(onsite_check(B) for B in ONSITE_BASIS[:3]))
# is it an algebra containing Hon0, Lam?
def inspan(M):
    A=np.array([B.ravel() for B in ONSITE_BASIS]).T; x=np.linalg.lstsq(A,M.ravel(),rcond=None)[0]; return np.linalg.norm(A@x-M.ravel())
print('Hon0 in span', inspan(Hon0), 'Lam in span', inspan(Lam), 'RLk(0) in span', inspan(RLk(np.zeros(3))))
# momentum action
for nm,ops in (('rots',rots),('trans',trans[:8])):
    acts=[]
    for P,s in ops:
        kk,U=op_bloch(P,s,kst); acts.append(kred(kk))
    print(nm, 'image of k*:', acts)
