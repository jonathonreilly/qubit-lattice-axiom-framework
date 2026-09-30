import sys, json, numpy as np
from multiprocessing import Pool
from sim import run_eta, run_actual

def classify(out,T):
    # out: list of (n,rho) records, terminated early if disordered blow-up
    if out[-1][0]<T: return "D",out[-1][1]
    rho_end=out[-1][1]
    half=[v for n,v in out if n<=T//2][-1]
    if rho_end<0.2 and not (rho_end>1.5*half+0.005): return "O",rho_end
    if rho_end>=0.2: return "D",rho_end
    return "?",rho_end   # growing but not yet blown up

def job(args):
    which,p,L,T,seed=args
    f=run_eta if which=="eta" else run_actual
    out=f(p,L,T,seed,rec=max(1,T//8))
    c,rho=classify(out,T)
    return (which,p,L,T,seed,c,rho,out[-1][0])

if __name__=="__main__":
    which=sys.argv[1]; L=int(sys.argv[2]); T=int(sys.argv[3]); nseed=int(sys.argv[4])
    ps=[float(x) for x in sys.argv[5].split(",")]
    jobs=[(which,p,L,T,s) for p in ps for s in range(nseed)]
    with Pool(int(__import__("os").environ.get("NP","9"))) as P: res=P.map(job,jobs)
    for p in ps:
        rr=[r for r in res if r[1]==p]
        cl="".join(r[5] for r in rr)
        print(which,"L=%d T=%d p=%g"%(L,T,p),cl,"rho_end=",[round(r[6],4) for r in rr],"stop=",[r[7] for r in rr])
