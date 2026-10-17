from fractions import Fraction as F

def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def scale(a,k):return (k*a[0],k*a[1])
def norm(a):return a[0]**2+a[1]**2
for x in [1,-1]:
 for arm in [0,1]:
  d=[(0,0)]*12;d[0]=(-x,0);d[11]=(0,1);weights=[1]*11
  if arm:
   for k in [2,5]: d[k]=d[k+1]=(-1,0);weights[k]=2
  theta=[(1,0),d[0]]
  for k in range(2,13):theta.append(sub(mul(d[k-1],theta[k-1]),scale(theta[k-2],weights[k-2])))
  tail=[(0,0)]*13;tail[12]=(1,0);tail[11]=d[11]
  for k in range(10,-1,-1):tail[k]=sub(mul(d[k],tail[k+1]),scale(tail[k+2],weights[k]))
  frob=F(0);col=F(0)
  for i in range(12):
   prod=1
   for j in range(i,12):
    if j>i:prod*=weights[j-1]
    sq=F(prod*norm(theta[i])*norm(tail[j+1]),norm(theta[12]))
    frob+=sq*(1 if i==j else 2)
    if j==11:col+=sq
  num=mul(theta[11],(theta[12][0],-theta[12][1]));den=norm(theta[12])
  print(x,arm,'det=',theta[12],'F2=',frob,'col2=',col,'diag=',(F(num[0],den),F(num[1],den)))
