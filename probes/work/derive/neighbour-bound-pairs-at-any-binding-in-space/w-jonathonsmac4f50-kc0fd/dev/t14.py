import pickle,numpy as np
rows=pickle.load(open('scan600.pkl','rb'))
EC=2*np.sqrt(3)
sel=[r for r in rows if r[1]-EC>=1.0 and r[4]>3.0 and r[7]>0.3]
print(len(sel))
sel.sort(key=lambda r:-r[7])
for r in sel[:20]: print('it%d E=%.4f d=%.3f g=%.4f null=%d evmax=%.4f evmin=%.4f gap=%.3f'%(r[0],r[1],r[1]-EC,r[2],r[3],r[4],r[5],r[7]))
