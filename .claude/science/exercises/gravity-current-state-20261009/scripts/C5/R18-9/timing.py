import time, numpy as np, lib9 as L
t=time.time(); F=L.dirac(0.167717434, 0.484514796); print('dirac UD', F, '%.1fs'%(time.time()-t))
t=time.time(); r=L.rstar(0.15); print('rstar(0.15)=', r, '%.1fs'%(time.time()-t))
t=time.time(); P=L.phot_quad(1.271203310, 0.259985516/(np.pi-1.271203310), 48); print('phot_quad', P, '%.1fs'%(time.time()-t))
a=-0.122744585
print('quad at a: T %.6e E %.6e' % (np.polyval(P['T2g'][::-1], a), np.polyval(P['Eg'][::-1], a)))
t=time.time(); V=L.phot_at(1.271203310, 0.259985516/(np.pi-1.271203310), a, 48); print('direct at a', V, '%.1fs'%(time.time()-t))
t=time.time(); s=L.scal(2.361985868, 0.134479073/(np.pi-2.361985868)); print('scal', s, '%.1fs'%(time.time()-t))
