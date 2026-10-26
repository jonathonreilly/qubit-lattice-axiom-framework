import json,subprocess,hashlib,sys
M,P,OUT=sys.argv[1:4]
d=json.load(open(P+'/batch-10.json'))
res=[];groups={}
for s in d['sources']:
    r=subprocess.run(['git','-C',M,'show',s['head']+':'+s['path']],capture_output=True)
    h=hashlib.sha256(r.stdout).hexdigest() if r.returncode==0 else None
    res.append({'pr':s['pr'],'head':s['head'],'path':s['path'],'sha256':s['sha256'],'verified':h==s['sha256'],'category':s['category']})
    groups.setdefault(s['content_group'],0); groups[s['content_group']]+=1
json.dump({'n':len(res),'verified':sum(x['verified'] for x in res),'distinct_groups':len(groups),'items':res},open(OUT+'/_verify.json','w'),indent=0)
print(len(res),sum(x['verified'] for x in res),len(groups))
