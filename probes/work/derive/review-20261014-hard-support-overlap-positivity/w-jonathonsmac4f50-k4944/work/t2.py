import numpy as np, sys
d=0.6
def trace_pows(w,Lxs,M,Ly=3):
    g=(np.arange(M)+0.5)/M*2*d-d; h=2*d/M
    D1,D2=np.meshgrid(g,g,indexing='ij'); D1=D1.ravel();D2=D2.ravel()
    ok=(np.abs(D1)<d)&(np.abs(D2)<d)&(np.abs(D2-D1)<d)
    D=np.stack([np.zeros(ok.sum()),D1[ok],D2[ok]],1)   # rows y=0,1,2
    S=D[None,:,:]-D[:,None,:]   # s_y=d'_y-d_y
    mn=S.min(2); mx=S.max(2)
    half=d-(mx-mn)/2
    ph=np.exp(1j*w*(mn+mx)/2)
    T=np.where(half>0, ph*2*np.sin(w*np.maximum(half,0))/w,0)*h*h
    ev=np.linalg.eigvalsh((T+T.conj().T)/2)
    return {L:(ev**L).sum() for L in Lxs}, ev
if __name__=="__main__":
    for w in (0,1,2,4,6,7,8,9,10,11):
        ww=w if w>0 else 1e-6
        res=[trace_pows(ww,(2,3,4,5),M)[0] for M in (30,45,60)]
        print(w,[ (round(r[3],6),round(r[2],6)) for r in res])
