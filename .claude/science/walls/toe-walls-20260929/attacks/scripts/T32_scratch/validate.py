import time, numpy as np
import su3mc as m
def run(dims, beta, nth, nmeas, n_or=2, seedv=1):
    up, dn, coords = m.make_tables(dims)
    V = up.shape[1]
    U = m.cold_start(V)
    m.seed(seedv)
    t0=time.time()
    for i in range(nth): m.sweep(U, up, dn, beta, n_or)
    ps=[]
    for i in range(nmeas):
        m.sweep(U, up, dn, beta, n_or)
        ps.append(m.plaquette_avg(U, up))
    ps=np.array(ps)
    dev = max(np.abs(U[s,mu].conj().T@U[s,mu]-np.eye(3)).max() for s in range(0,V,37) for mu in range(4))
    det = np.abs(np.linalg.det(U[::37,0])-1).max()
    print(dims, beta, "plaq=%.5f +- %.5f  time/sweep=%.3fs unit_dev=%.1e det_dev=%.1e"%(ps.mean(), ps.std()/np.sqrt(len(ps)), (time.time()-t0)/(nth+nmeas), dev, det), flush=True)
    return ps
if __name__=="__main__":
    run((4,4,4,4), 1.0, 100, 200)
    run((6,6,6,6), 1.0, 100, 200)
    run((8,8,8,8), 6.0, 150, 200)
