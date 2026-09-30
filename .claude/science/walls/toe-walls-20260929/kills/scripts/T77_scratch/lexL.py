import testB_orders as T
for L in (6,10,14):
    r=T.stats(L,'lex',0.0,6 if L==14 else 12,torus=True)
    print(L, r['vert_defect'], r['vert_defect']*L)
