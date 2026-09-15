from pathlib import Path
import subprocess,json
r=Path('/private/tmp/review-drain-20260915/pr8010/scripts');o=Path('/private/tmp/review-drain-20260915/check8010');res=[]
a=r/'native_gauge_transfer_central_character_gaussian_spectral_second_order_2026_09_07.py';b=r/'native_gauge_transfer_dimension_divided_wilson_second_order_2026_09_07.py'
cases=[(a,'theta=(3-omega)/2','theta=(3+omega)/2','Mehler branch'),(a,'q+q*q/4','q+q*q/3','quartic multiplier'),(a,'Rational(7,4)*q','Rational(6,4)*q','linear multiplier'),(a,'a=2/omega','a=1/omega','heat exponent'),(a,'heat/4','heat/8','heat normalization'),(a,'3*k+2*n==N','2*k+2*n==N','angular spectrum'),(b,'(s1,-1)','(s1,1)','reflection sign'),(b,'-s.I*Delta if n==3','s.I*Delta if n==3','alternant sign'),(b,'term/6-Delta**2/6','term-Delta**2/6','factor six'),(b,'C<1710','C<1700','ratio bound')]
for i,(p,old,new,name) in enumerate(cases):
 src=p.read_text();assert old in src;f=o/f'mutant{i}.py';f.write_text(src.replace(old,new,1));run=subprocess.run(['python3',str(f),'--json'],capture_output=True,text=True,timeout=30);res.append(dict(name=name,exit=run.returncode,stderr=run.stderr));assert run.returncode!=0,name
(o/'mutations.json').write_text(json.dumps(res,indent=2));print('Rejected',len(res),'mutants')
