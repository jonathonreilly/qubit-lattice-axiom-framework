from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,platform,sys
import numpy,scipy,sympy
D=Path(__file__).resolve().parent
third=D.parent.parent/'campaign12h_third'
prior=D.parent/'post_birth_ring_spectrum_independent'
expected={
 third/'FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md':'002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e',
 third/'fast_matter_formation_independent/REPORT.md':'0a114dadc553ccbb4ef9bf15faf87a70f64a0d5719bf1d1743de86b94a0205b5',
 third/'fast_matter_formation_independent/FINAL_SEAL.json':'63ddf9823aa23d678e8f61863ddeedf36596918e2cb600f100fa334e6d1432db',
 prior/'REPORT.md':'8bb9e330303d5b66e14c19031716d8fb8e7baa5a49d193759dbabce1f343b7b2',
 prior/'PRE_COMPARISON_SEAL.json':'cffc3495e440045bd73077e8be1a5e231ff39a07e53889a22336c204f60f5c37',
 prior/'COMPARISON.md':'9fc278830ca7473f631139845b76e55c4ed72ab44b8e136759c22a481907a160',
 prior/'FINAL_SEAL.json':'6beaa587833b2d626154ffdd8fd2729ad844f164ee4be6b0c607b3f9b4402851',
}
def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
sources=[]
for p,sha in expected.items():
 r=row(p);assert r['sha256']==sha,p;sources.append(r)
receipts=[]
for p in sorted(D.glob('*_RECEIPT.json')):
 r=json.loads(p.read_text())
 for key in ('runner','stdout','stderr'):assert row(Path(r[key]['path']))==r[key]
 receipts.append({'receipt':str(p),'exit_code':r['exit_code'],'source_sha256':r['runner']['sha256']})
assert sum(r['exit_code']!=0 for r in receipts)==2
out={'created_utc':datetime.now(timezone.utc).isoformat(),'sources':sources,
 'execution_receipts_authenticated':receipts,
 'runtime':{'python':sys.version,'executable':sys.executable,'platform':platform.platform(),
            'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__},
 'read_boundary':'Only checked third-campaign model and frozen independent ring reconstruction/comparison reused. No second_event_author or finite_spin_post_birth_author contents, fourth-campaign working derivations, checkpoint, or registry accessed.',
 'prior_exposure':'The L=3 fast-motion example and the complete preceding ring-spectrum reconstruction/comparison were already known. New second-event algebra and cube Grams are independently assembled.',
 'failure_policy':'Two failed source versions, their actual command streams and receipts are preserved unchanged beside separately named repaired scripts.'}
p=D/'SOURCE_BINDINGS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
