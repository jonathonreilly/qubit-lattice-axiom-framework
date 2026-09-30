"""T70 test 2d: mass dependence of the k^2 coefficients (p = 32 vs 48 for slope in k^2) and G values."""
import numpy as np, importlib.util, math
spec = importlib.util.spec_from_file_location("t2b", "test2b_lattice_induced_scalar.py"); t2b = importlib.util.module_from_spec(spec); spec.loader.exec_module(t2b)
out=[]
def P(*a):
    s=" ".join(str(x) for x in a); print(s); out.append(s)
P("m, Nt, A2_TT, A2_CONF, A2_NP, A_np(=NP-CONF-nn), G_TT=1/(64 pi A_TT), G_conf=-1/(4 pi A_pp), G_N=-A_pp/(4 pi A_np^2), A_uni_TT, A_uni_CONF, rho0")
for m,Nt,Nqz in ((0.25,64,10),(0.5,48,10),(1.0,32,8),(2.0,24,8)):
    res={}
    for sec in ('TT','CONF','NP'):
        vals=[]
        for p in (32,48):
            e0,A = t2b.response(sec,p,m,Nt,Nqz,a=0.01); vals.append(A)
        k1,k2 = 2*np.pi/32, 2*np.pi/48
        res[sec]=(vals[0]-vals[1])/(k1**2-k2**2)
    e0u,Atu = t2b.response('TT',1,m,Nt,Nqz*8,a=0.01,uniform=True)
    _,Acu = t2b.response('CONF',1,m,Nt,Nqz*8,a=0.01,uniform=True)
    Anp = res['NP']-res['CONF']
    G_TT = 1/(64*math.pi*res['TT']); G_c = -1/(4*math.pi*res['CONF']); G_N = -res['CONF']/(4*math.pi*Anp**2)
    P(f"{m}, {Nt}, {res['TT']:.3e}, {res['CONF']:.4f}, {res['NP']:.4f}, {Anp:.4f}, {G_TT:.2f}, {G_c:.3f}, {G_N:.2f}, {Atu:.4f}, {Acu:.4f}, {e0u:.4f}")
open("test2d_output.txt","w").write("\n".join(out)+"\n")
