import numpy as np, json
from sea_stiffness import a2_bz, qlat2
N=64
res={}
# full-range scan of Pi(q)=a2(q) along x and along (1,1,1); T1 check at q=(pi,pi,pi)
scan=[]
for d in ['x','d']:
    for m in range(0,N//2+1,2):
        a2,c0=a2_bz(N,m,0.0,3,d)
        scan.append(dict(dir=d,m=m,q=2*np.pi*m/N,a2=float(a2)))
    print(d,[round(r['a2'],4) for r in scan if r['dir']==d])
res['scan']=scan
res['a2_max_over_scan']=max(r['a2'] for r in scan)
res['a2_at_chessboard']=[r['a2'] for r in scan if r['dir']=='d' and r['m']==N//2][0]
res['c0']=float(c0)
# tuning ratio |c0|/kappa and c0+12 kappa
k0=0.09936290373818159
res['c0_over_kappa']=float(c0/k0); res['c0_plus_12kappa']=float(c0+12*k0)
# induced G and gamma (b55 normalisation: nabla^2 du = (gamma/wbar) e => 4 pi G = gamma, gamma = 1/kappa)
res['gamma_ind']=1/k0; res['G_lat_ind']=1/(4*np.pi*k0); res['K_b129']=k0/4
# static kernel of sea alone at small q: du_q = -e_q/(4 a2(q)); sign
res['sign_of_sea_only_response']='delta u > 0 at a positive source (a2<0): clock runs faster at the mass -> repulsive'
# extrapolated kappa from finer meshes (N=192)
def kap(N,m,d='x'):
    a2,c0=a2_bz(N,m,0.0,3,d); return 4*(a2-c0/4)/qlat2(N,m,3,d)
k1,k2=kap(192,3),kap(192,6); q1,q2=(2*np.pi*3/192)**2,(2*np.pi*6/192)**2
res['kappa_x_N192_extrap']=float((k1*q2-k2*q1)/(q2-q1)); res['kappa_x_N192_m3']=float(k1)
print(json.dumps({k:v for k,v in res.items() if k!='scan'},indent=1))
json.dump(res,open('T69_results_scan.json','w'),indent=1)
