from ana import *
OFF,Sm=d4cone(); C=CA(OFF,Sm)
np.set_printoptions(linewidth=200,precision=4)
for q in (np.zeros(4), 0.01*np.array([.3,-.5,.6,.55])/np.linalg.norm([.3,-.5,.6,.55])):
    Q=C.Q(q); ev=np.linalg.eigvalsh((Q+Q.conj().T)/2)
    print('herm err',np.abs(Q-Q.conj().T).max())
    print(ev[:48])
    G=C.gauge(q); print('gauge sv min', np.linalg.svd(G,compute_uv=False)[-6:])
