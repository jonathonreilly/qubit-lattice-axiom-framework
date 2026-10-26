from t22 import *
M=proj(UU)+proj(DD)+0.5*proj(S)
Mall=build_M_all(M)
M24=np.zeros((24,24),complex)
for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
rows=scanM(M,tabs)
rows=[r for r in rows if r[3]>1.6]
for r in sorted(rows,key=lambda r:r[0]): print('E=%.4f dE=%.3f g=%.4f null=%d W=%.3f..%.3f gap=%.3f'%(r[0],r[0]-EC,r[1],r[2],r[4],r[3],r[6]))
