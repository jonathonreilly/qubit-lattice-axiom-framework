import pickle,json,zlib,base64
from fractions import Fraction as F
from poly import *
exec(open('export.py').read().split("data={'M'")[0])   # reuse helpers fs,pj,reduce_label, loads d,lab,red
data=json.load(open('data.json'))
L=pickle.load(open('lay_b4.pkl','rb')); m=L['m']
free,sub,r=red[m]
gens,levels,needed,needg=L['gens'],L['levels'],L['needed'],L['needg']
byp={}
for key_,poly in sorted(lab.items()):
    rp=reduce_label(poly,sub)
    if rp: byp.setdefault(tuple(sorted(rp.items())),key_)
gid={i:t for t,i in enumerate(needg)}
glabels=[list(byp[tuple(sorted(gens[i].items()))]) for i in needg]
glabels=[[list(g[0]),g[1],g[2],g[3]] for g in glabels]
lv=[]
for L_,(kind,cofs) in enumerate(levels):
    outs=[]
    for j in needed[L_]:
        ent=[[gid[i] if L_==0 else i, pj(q)] for i,q in cofs[j].items()]
        outs.append([j,ent])
    lv.append([kind[0] if isinstance(kind,tuple) else kind,outs])
data['flat']={'m':list(m),'glabels':glabels,'levels':lv,'seeds':[list(s) for s in L['seeds']]}
s=json.dumps(data,separators=(',',':'))
z=base64.b64encode(zlib.compress(s.encode(),9)).decode()
print(len(s),len(z))
open('data.json','w').write(s); open('data.b64','w').write(z)
