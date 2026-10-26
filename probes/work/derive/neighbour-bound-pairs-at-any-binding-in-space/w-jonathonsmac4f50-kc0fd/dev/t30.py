from t22 import *
Ebig=[t for t in tabs if t['E']>25]
print(len(Ebig))
def dark_W(a,b=0.0,mu=1.0):
    M=mu*(proj(UU)+proj(DD))+a*proj(S)+b*proj(T0)
    Mall=build_M_all(M)
    M24=np.zeros((24,24),complex)
    for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
    gs=[];ws=[]
    for tab in Ebig:
        g=tab['E']/mu
        o=weights_tab(tab,g,M24,tolN=1e-6)
        ev=np.linalg.eigvalsh(o['Wsum']); 
        gs.append(g*mu); ws.append(ev.max()); 
    gs=np.array(gs);ws=np.array(ws)
    # nullsize check
    X=np.vstack([1/gs**2,1/gs**4,1/gs**6]).T
    coef=np.linalg.lstsq(X,ws-1.5,rcond=None)[0]
    return coef
for a in (0,0.1,0.25,0.5,0.75,0.9,-0.5,2.0):
    print(a,dark_W(a))
for b in (0.3,):
    print('b',b,dark_W(0.25,b))
