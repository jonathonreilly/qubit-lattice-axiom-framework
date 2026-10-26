import pickle,itertools,time
exec(open('setup.py').read().split("# ---------- polynomial engine")[0])
# polynomial engine pieces needed for build_unitarity
src=open('setup.py').read()
exec("# ---------- polynomial engine"+src.split("# ---------- polynomial engine")[1])
U=build_unitarity()
lab={}
for m,acc in U.items():
    for a in range(4):
        for b in range(4):
            for pi,part in enumerate(acc[a][b]):
                if part: lab[(m,a,b,pi)]=tuple(sorted(part.items()))
pickle.dump(lab,open('labels_raw.pkl','wb'))
print('labels',len(lab))
