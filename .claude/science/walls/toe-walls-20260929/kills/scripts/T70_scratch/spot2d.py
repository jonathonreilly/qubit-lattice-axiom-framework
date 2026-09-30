import numpy as np, importlib.util, math
spec = importlib.util.spec_from_file_location("t2b", "test2b_lattice_induced_scalar.py"); t2b = importlib.util.module_from_spec(spec); spec.loader.exec_module(t2b)
m,Nt,Nqz=0.5,24,6
res={}
for sec in ('TT','CONF','NP'):
    v=[t2b.response(sec,p,m,Nt,Nqz,a=0.01)[1] for p in (24,32)]
    k1,k2=2*np.pi/24,2*np.pi/32
    res[sec]=(v[0]-v[1])/(k1**2-k2**2)
Anp=res['NP']-res['CONF']
print("spot m=0.5 Nt=24:",res,"G_TT",1/(64*math.pi*res['TT']),"G_conf",-1/(4*math.pi*res['CONF']),"A_np",Anp)
