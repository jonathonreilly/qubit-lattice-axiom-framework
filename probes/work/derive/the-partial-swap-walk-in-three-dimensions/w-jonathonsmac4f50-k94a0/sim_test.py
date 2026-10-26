from sim_lib import *
# test: plane wave symbol equals layer action
L=8
rng=np.random.default_rng(1)
for order in ('pal','plain'):
  for trial in range(3):
    kk=2*np.pi*rng.integers(0,L,3)/L
    u=rng.normal(size=2)+1j*rng.normal(size=2)
    x=np.stack(np.meshgrid(*[np.arange(L)]*3,indexing='ij'),-1)
    ph=np.exp(1j*(x@kk))
    psi=ph[...,None]*u
    w=np.ones((L,L,L))
    out=make_tick(w,0.37,order)(psi)
    S=symbol(kk,0.37,order)
    exp=ph[...,None]*(S@u)
    print(order,np.abs(out-exp).max())
