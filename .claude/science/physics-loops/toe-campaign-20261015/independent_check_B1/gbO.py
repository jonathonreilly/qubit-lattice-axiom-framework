import pickle,sympy as sp,time,sys
z,zb,eqs=pickle.load(open('eqs_O.pkl','rb'))
t=time.time()
G=sp.groebner(eqs,*z[1:],*zb[1:],z[0],zb[0],order='grevlex',domain=sp.QQ_I)
print(time.time()-t,'s',len(G.exprs))
for g in G.exprs: print(g)
pickle.dump(G.exprs,open('gb_O.pkl','wb'))
