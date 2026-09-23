from fractions import Fraction as Q
import json,time
start=time.monotonic()
# Exact independent Cartesian derivative: D s=(s3,0,-s1).
spins=[(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1)),(Q(3,5),Q(0),Q(4,5))]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def d(s):return(s[2],Q(0),-s[0])
residuals=[dot(d(a),b)+dot(a,d(b)) for a in spins for b in spins]
assert all(v==0 for v in residuals)
bad=[dot(d(a),b)-dot(a,d(b)) for a in spins for b in spins]
assert any(v!=0 for v in bad)
# N normalization exact without invoking the submitted implementation.
N=len(spins);F=sum(s[0] for s in spins);m1=F/N
assert F*F==N*N*m1*m1
assert F*F != N*m1*m1
# P s=s-M(M dot s)/(M dot M) avoids numerical normalization.
M=tuple(sum(s[i] for s in spins)/N for i in range(3));mm=dot(M,M)
projected=[tuple(s[i]-M[i]*dot(M,s)/mm for i in range(3)) for s in spins]
total=tuple(sum(s[i] for s in projected) for i in range(3));assert total==(0,0,0)
lab=tuple(sum(s[i] for s in spins) if i<2 else Q(0) for i in range(3));assert lab!=(0,0,0)
print(json.dumps({'bond_pairs':16,'global_rotation_cancellation':True,'wrong_bond_sign_rejected':True,'ward_N_squared_normalization':True,'extra_division_N_rejected':True,'projection_zero_total':[str(v) for v in total],'fixed_axis_substitution_rejected':True,'fixed_axis_total':[str(v) for v in lab],'elapsed_sec':time.monotonic()-start,'limits':'One deterministic standard-library Fraction run; four explicit rational unit spins, 16 pairs. No primary/mutation CLI/simulation execution. No timeout, memory enforcement, stochastic or exhaustive-lattice claim.'},indent=2))
