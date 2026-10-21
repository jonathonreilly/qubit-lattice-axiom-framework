from collections import defaultdict
import json,time,math
R=int(__import__("sys").argv[1]) if len(__import__("sys").argv)>1 else 13
g=5;h=4
bit=lambda x,y:1<<((x%R)*R+y%R)
E={};P={}
for x in range(R):
 for y in range(R):
  for dx,dy in [(1,0),(0,1)]:E[(0,bit(x,y)|bit(x+dx,y+dy))]=1
  P[(bit(x,y)|bit(x+1,y)|bit(x,y+1)|bit(x+1,y+1),0)]=1
K={**{k:-g for k in E},**{k:-h for k in P}}
def comm(A,B):
 C=defaultdict(int)
 for (x,z),a in A.items():
  for (v,w),b in B.items():
   s=((z&v).bit_count()&1);t=((w&x).bit_count()&1)
   if s!=t:C[x^v,z^w]+=(-2 if s else 2)*a*b
 return {k:v for k,v in C.items() if v}
D={(0,bit(0,0)|bit(1,0)):1,(0,bit(0,0)|bit(0,1)):1}
counts=[]
for _ in range(3):D=comm(K,D);counts.append(len(D))
D=comm(E,D);b=sum(abs(v) for v in D.values())/2
assert b==9003008 and counts==[8,76,524] and len(D)==3336
assert all((x&z).bit_count()%2==0 for x,z in D)
m=2*h/(math.sqrt((16*g)**2+4*h*h)+16*g);a=2*h*m*(8-4*h/g)**2
print(json.dumps(dict(counts=counts,final_terms=len(D),M3_density_l1_bound=b,m=m,M1_density_lower=a,variance_density_lower=a**1.5/math.sqrt(b),omega=math.sqrt(2*b/a),window_density_lower=a/(2*math.sqrt(2*b/a))),indent=2))
