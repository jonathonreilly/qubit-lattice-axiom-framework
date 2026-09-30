"""Exact finite geometry; no Hilbert states and no dynamics."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import resource,time,json,hashlib,datetime,itertools
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
t0=time.process_time();here=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not any((runtime/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'))
assert datetime.datetime.now(datetime.timezone.utc).timestamp()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
axes=((1,0,0),(0,1,0),(0,0,1));dirs=axes+tuple(tuple(-x for x in v) for v in axes)
results=[]
for L in (None,6,8,10):
 def add(a,b):return tuple((x+y)%L if L else x+y for x,y in zip(a,b))
 def N(a):return {add(a,v) for v in dirs}
 h=(0,0,0);near={add(add(h,u),v) for u in dirs for v in dirs}-{h}
 axial={add(v,v) for v in dirs};E={c:N(c)-N(h) for c in axial}
 assert len(near)==18 and len(axial)==6 and all(len(x)==5 for x in E.values())
 # Any shared B implies a distance-two center; thus this exhausts all
 # possible nonempty pair intersections, including torus aliases.
 max_pair=max(len(N(h)&N(c)) for c in near)
 triple_sizes=[len(N(h)|N(c)|N(d)) for c,d in itertools.combinations(near,2) if N(c)&N(d)]
 min_three=min(triple_sizes)
 max_extra=max(len(E[c]&E[d]) for c,d in itertools.combinations(axial,2))
 competitors=set().union(*(set(add(add(c,u),v) for u in dirs for v in dirs) for c in axial))-{h}
 def adjacent(a,b):return a!=b and bool(N(a)&N(b))
 counts={d:sum(adjacent(d,c) for c in axial) for d in competitors}
 max_comp=max(counts.values())
 assert max_pair==2 and min_three==13 and max_extra<=1 and max_comp<=2
 diag=add(axes[0],axes[1]);ax=add(axes[0],axes[0])
 assert len(N(h)|N(diag))==10 and len(N(h)|N(ax))==11
 # Any non-near third center in a triple has a disjoint star pair, and
 # 6+6+6-2-2=14 lower bounds its union. No global enumeration is needed.
 results.append({'L':L or 'infinite Z3','distance_two_centers':len(near),'nearby_center_pairs_tested':len(list(itertools.combinations(near,2))),'max_two_star_overlap':max_pair,'min_three_star_union_in_pairwise_overlap_case':min_three,'disjoint_pair_three_star_lower_bound':14,'max_extra_set_overlap':max_extra,'max_competing_axial_rows':max_comp,'competitor_centers_tested':len(competitors),'minimum_unique_bright_rows_from_counting':6-1-max_comp})
result={'results':results,'scope':'Exact geometry control only; analytic dark-row injectivity and loss estimate are separate.','cpu_seconds':time.process_time()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'plan_sha256':hashlib.sha256((here/'ABSORPTION_EXTENSION_PLAN.md').read_bytes()).hexdigest()}
assert result['cpu_seconds']<30 and result['peak_rss_bytes']<150*1024**2
(here/'ABSORPTION_EXTENSION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
