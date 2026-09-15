from pathlib import Path
import gzip,io,json,time,math
import numpy as np
from fractions import Fraction as F
r=Path(__file__).parent;p=r/'original-8061/outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs';start=time.monotonic();a=np.load(io.BytesIO(gzip.decompress((p/'vectors/chi_real.npy.gz').read_bytes())),allow_pickle=False);bins=[0]*22
for i,raw in enumerate(a.view(np.uint64)):
 b=int(raw);ex=(b>>52)&2047;mant=b&((1<<52)-1);assert ex!=2047
 if ex:mant|=1<<52;shift=2*(ex-1)
 else:shift=0
 n=i.bit_count();particle=n+(1^(n&1));bins[particle]+=(mant*mant)<<shift
D=1<<2148;E=F('0.00000000004825');scale=10**40
def interval(n):
 q=F(n,D);s=math.isqrt(q.numerator*scale*scale//q.denominator);lo=F(s,scale);hi=F(s+1,scale);return[max(F(0),lo-E)**2,(hi+E)**2]
high=interval(sum(bins[3:]));assert F('0.001921920169')<high[0]<high[1]<F('0.001921920178');assert F('0.04383')**2<high[0] and high[1]<F('0.04384')**2
assert all(interval(bins[k])[0]>0 for k in (3,5,7));result={'status':'PASS','complete_chi_coordinates':len(a),'odd_buckets':list(range(1,22,2)),'higher_interval_using_conservative_error':list(map(str,high)),'positive3_5_7':True,'error_bound_import':'Echi <= exact decimal4.825e-11 remains conditional until final independent residual replay','seconds':time.monotonic()-start,'canonical_helper_imports':False};(r/'control_projection.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
