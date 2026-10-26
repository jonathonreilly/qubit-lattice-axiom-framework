import pickle,json,zlib,base64,glob
from fractions import Fraction as F
from poly import *
d=pickle.load(open('cache.pkl','rb')); lab=pickle.load(open('labels_raw.pkl','rb'))
red=pickle.load(open('red.pkl','rb'))
def fs(x): return str(x) if x.denominator!=1 else str(x.numerator)
def pj(p): return [[list(mo),fs(c)] for mo,c in sorted(p.items())]
def reduce_label(poly,sub):
    out={}
    for mon,cf in poly:
        term={():cf}
        for v in mon: term=pmul(term,sub[v])
        for mo,c in term.items(): out[mo]=out.get(mo,F(0))+c
    return {k:v for k,v in out.items() if v!=0}
data={'M':[], 'branches':{}}
for (n,j),mat in sorted(d['M'].items(),key=lambda kv:(kv[0][1],kv[0][0])):
    data['M'].append([list(n),j,[[ [fs(c[0]),fs(c[1])] for c in row] for row in mat]])
data['sites']=sorted({tuple(k[0]) for k in d['M']})
data['param_sites']=[list(n) for n,k in d['params']]
tot=0
for fn in sorted(glob.glob('lay_*.pkl')):
    L=pickle.load(open(fn,'rb')); m=L['m']
    free,sub,r=red[m]
    gens,levels,needed,final=L['gens'],L['levels'],L['needed'],L['final']
    # labels for gens
    byp={}
    for key_,poly in sorted(lab.items()):
        rp=reduce_label(poly,sub)
        if rp: byp.setdefault(tuple(sorted(rp.items())),key_)
    # needed gens: those referenced in level 0 needed outputs
    kind0,cofs0=levels[0]
    needg=sorted({i for j in needed[0] for i in cofs0[j]})
    glabels={}
    for i in needg:
        k=tuple(sorted(gens[i].items()))
        assert k in byp,(m,i)
        glabels[i]=byp[k]
    # remap gen ids to compact
    gid={i:t for t,i in enumerate(needg)}
    lv=[]
    for L_,(kind,cofs) in enumerate(levels):
        outs=[]
        for j in needed[L_]:
            ent=[]
            for i,q in cofs[j].items():
                ent.append([gid[i] if L_==0 else i, pj(q)])
            outs.append([j,ent])
        lv.append([kind,outs])
    data['branches'][str(m)]={'m':list(m),'glabels':[list(map(lambda x:x if not isinstance(x,tuple) else list(x),glabels[i])) for i in needg],
        'levels':lv,'final':final}
    tot+=sum(len(e[1]) for kind,outs in lv for o in outs for e in o[1])
    print(m,'gens',len(needg),'levels',len(lv))
s=json.dumps(data,separators=(',',':'))
z=base64.b64encode(zlib.compress(s.encode(),9)).decode()
print('json',len(s),'b64z',len(z),'terms',tot)
open('data.json','w').write(s); open('data.b64','w').write(z)
