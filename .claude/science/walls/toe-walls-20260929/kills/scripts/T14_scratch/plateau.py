import sys,time,numpy as np
sys.path.insert(0,'/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T14_scratch')
from yukawa_chunked import run_chunked as run
for (eps,m,mu,Lt,Ns) in [(0.25,0.125,0.125,160,64),(0.12,0.125,0.125,160,64),(0.12,0.0625,0.0625,200,96),(0.06,0.0625,0.0625,200,96)]:
    Nt=int(Lt/eps); t0=time.time()
    r=run(Nt,Ns,eps,m,mu,chunk=8)
    print(f"eps={eps} m=mu={m} Nt={Nt} Ns={Ns}: a_psi={r['a_psi']:.5f} a_phi/4={r['a_phi']/4:.5f} gap4fl={r['a_psi']-r['a_phi']/4:.5f}  ({time.time()-t0:.0f}s)",flush=True)
