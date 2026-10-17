import pickle, random, itertools, time, sys
from polytools import *
from orbits import D, name
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
NS=int(sys.argv[2]) if len(sys.argv)>2 else 25
res=[]
def test(label, orbitlist):
    rule=[s for o in orbitlist for s in o]
    a=analyse(rule,'c')
    ll=a['local_logicals']
    rf=recordfree(rule,ll,'r')
    bad1=any(v==0 for v in rf.values())
    bad2=(not ll) and a['ext3zero']==0
    res.append((label,len(rule),ll,a['ext3zero'],rf,bad1,bad2))
    if bad1 or bad2 or a['ext3zero'] is None: print('VIOLATION/ERR',label,len(rule),ll,a['ext3zero'],rf,flush=True)
t0=time.time()
for mode in (0,1):
    orbs=pickle.load(open(D+'orbs%d.pkl'%mode,'rb'))
    cl,adj=pickle.load(open(D+'cl%d.pkl'%mode,'rb'))
    for ci,c in enumerate(cl):
        c=sorted(c)
        if len(c)<=3:
            for k in range(1,len(c)+1):
                for sub in itertools.combinations(c,k):
                    test('m%d c%d %s'%(mode,ci,sub),[orbs[i] for i in sub])
        else:
            # singles (mode 0 only, all; mode 1 a sample) + random subsets
            singles=c if mode==0 else random.sample(c,30)
            for i in singles: test('m%d c%d single %d'%(mode,ci,i),[orbs[i]])
            for _ in range(NS):
                k=random.choice([2,3,4,6,10])
                sub=sorted(random.sample(c,k))
                test('m%d c%d %s'%(mode,ci,sub),[orbs[i] for i in sub])
    print('mode',mode,'done',time.time()-t0,flush=True)
pickle.dump(res,open(D+'claimC_res_%s.pkl'%(sys.argv[1] if len(sys.argv)>1 else '1'),'wb'))
from collections import Counter
print('rules tested',len(res),'violations part1',sum(r[5] for r in res),'part2',sum(r[6] for r in res))
print('ext3 nonzero (3D-mobile by some op):',sum(1 for r in res if r[3]==0),' of which with no LL:',sum(1 for r in res if r[3]==0 and not r[2]))
print('no-LL rules:',sum(1 for r in res if not r[2]))
for r in res:
    if r[0].startswith('m1') and ('c0' in r[0] or 'c1' in r[0] or 'c2' in r[0]) and len(r[0])<40: pass
