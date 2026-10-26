import pickle,numpy as np
rows=pickle.load(open('scan600.pkl','rb'))
sel=[r for r in rows if r[7]>0.3 and r[4]>3]
print(len(sel))
sel.sort(key=lambda r:-r[7])
for r in sel[:25]: print('it%d E=%.4f g=%.4f null=%d evmax=%.4f evmin=%.4f gap=%.3f'%(r[0],r[1],r[2],r[3],r[4],r[5],r[7]))
sel1=[r for r in rows if r[3]==1 and r[7]>0.2 and r[4]>3]
print('singlets',len(sel1))
for r in sorted(sel1,key=lambda r:-r[7])[:10]: print('it%d E=%.4f g=%.4f null=%d evmax=%.4f gap=%.3f'%(r[0],r[1],r[2],r[3],r[4],r[7]))
