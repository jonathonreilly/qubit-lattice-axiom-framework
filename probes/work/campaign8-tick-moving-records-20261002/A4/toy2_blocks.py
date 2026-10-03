"""Block-density view of clumping: 2D 128^2, 2000 ticks, no formation. 4x4 blocks (16 sites).
Reports: fraction of records sitting in dense blocks (>= 15/16), hole fraction inside dense blocks,
vapour density = record density in blocks with <= 1/16, fraction of blocks that are 'dense' / 'dilute', bimodality."""
import sys, numpy as np
from t1lib import move_phase
rho=float(sys.argv[1]); gs=[float(v) for v in sys.argv[2].split(",")]; L=128; T=2000; b=4
for g in gs:
    rng=np.random.default_rng(int(100*g)+3); occ=rng.random((L,L))<rho; expg=np.exp(g*np.arange(5))
    acc=[]
    for t in range(1,T+1):
        occ,mv,arr,w=move_phase(occ,g,rng,expg)
        if t>T-500 and t%50==0:
            blk=occ.reshape(L//b,b,L//b,b).sum(axis=(1,3))
            dense=blk>=15; dil=blk<=1
            fr_rec_dense=blk[dense].sum()/occ.sum()
            holes_dense=1-blk[dense].mean()/16 if dense.any() else np.nan
            vap=blk[dil].mean()/16 if dil.any() else np.nan
            mid=((blk>=4)&(blk<=12)).mean()
            acc.append((fr_rec_dense,holes_dense,vap,dense.mean(),dil.mean(),mid,mv.mean()))
    a=np.nanmean(np.array(acc),axis=0)
    print(f"rho={rho} g={g:4.2f}: recs in dense blocks={a[0]:.3f} hole frac in dense blocks={a[1]:.4f} vapour dens (dilute blocks)={a[2]:.4f} "
          f"dense blocks={a[3]:.3f} dilute blocks={a[4]:.3f} middling blocks={a[5]:.3f} moves/site/tick={a[6]:.4f} | e^-2g={np.exp(-2*g):.4f}",flush=True)
