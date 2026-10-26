from dev_engine import *
import time
t=time.time()
dls=list(np.geomspace(0.03,4,34))+list(np.geomspace(4.6,70,30))
tabs=[]
for dl in dls:
    tabs.append(make_tab(EC+dl,N_for(dl)))
print('tables',time.time()-t,flush=True)
pickle.dump(tabs,open('tabs.pkl','wb'))
