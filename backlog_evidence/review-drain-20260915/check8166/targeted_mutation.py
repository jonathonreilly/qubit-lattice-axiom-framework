import pathlib,json,time
p=pathlib.Path('/private/tmp/review-drain-20260915/drain8166-originals/.claude/science/physics-loops/toe-compact-response-20260916/evidence/bridge_cubic_check.py')
source=p.read_text();space={'__name__':'review_control','__file__':str(p)};exec(compile(source,str(p),'exec'),space)
expected=-0.069524531146387996873118102977193374
args=(.55,.24,.71,48);original=space['one_face_quadrature'](*args)['cubic'];assert abs(original-expected)<1e-12
rows=[]
for old,new in [('-3*covariance(A,B,w)/(g*g)','+3*covariance(A,B,w)/(g*g)'),('math.sqrt(2*g*g*T)*nodes','math.sqrt(2*g*g*T/4)*nodes')]:
 changed={'__name__':'review_control','__file__':str(p)};exec(compile(source.replace(old,new),str(p),'exec'),changed);actual=changed['one_face_quadrature'](*args)['cubic'];assert abs(actual-expected)>1e-5;rows.append({'change':new,'independent_target_error':abs(actual-expected),'rejected':True})
print(json.dumps({'scope':'Two targeted changed-runner mutations against independently differentiated positive integral; primary main not run.','baseline_error':abs(original-expected),'mutations':rows},indent=2))
