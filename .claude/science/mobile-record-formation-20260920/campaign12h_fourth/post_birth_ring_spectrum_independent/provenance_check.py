from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent;B=D.parent.parent/'campaign12h_third'
expected={
 'FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md':'002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e',
 'fast_matter_formation_independent/REPORT.md':'0a114dadc553ccbb4ef9bf15faf87a70f64a0d5719bf1d1743de86b94a0205b5',
 'fast_matter_formation_independent/FINAL_SEAL.json':'63ddf9823aa23d678e8f61863ddeedf36596918e2cb600f100fa334e6d1432db',
 'post_birth_fast_motion_author/FAST_VACANCY_MOTION_AFTER_FORMATION.md':'76d7f2faf3a0b4635499ddff1d8a88868d691d58c035780af737129701e30eeb',
 'post_birth_fast_motion_independent/REPORT.md':'ac396a036961d37f8f0deec41538a083d66fb41b18521c714abab2ad998e6727',
 'post_birth_fast_motion_independent/FINAL_SEAL.json':'943e0342f29b1095c2e970517d21f35738ea27a241b2a263c41200b2627532ef'}
rows=[]
for rel,h in expected.items():
 p=B/rel;b=p.read_bytes();actual=hashlib.sha256(b).hexdigest();assert actual==h
 rows.append({'path':str(p),'bytes':len(b),'sha256':actual})
# Verify the preserved failing source against its original real command receipt.
r=json.loads((D/'ring_run_RECEIPT.json').read_text());p=D/'ring_control_before_char_symbol_fix.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()==r['runner']['sha256']
for name in ('stdout','stderr'):
 q=Path(r[name]['path']);assert hashlib.sha256(q.read_bytes()).hexdigest()==r[name]['sha256']
for receipt in ('ring_repaired_run_RECEIPT.json','spectral_run_RECEIPT.json','component_run_RECEIPT.json'):
 r=json.loads((D/receipt).read_text());assert r['exit_code']==0
 for key in ('runner','stdout','stderr'):
  q=Path(r[key]['path']);b=q.read_bytes();assert len(b)==r[key]['bytes'] and hashlib.sha256(b).hexdigest()==r[key]['sha256']
out={'sources':rows,'prior_exposure':'The L=3 six-site post-birth path/Bessel result was checked in the preceding campaign. L=4 and general-L diagonalization here are new independent calculations from the neutral model.','read_boundary':'No campaign12h_fourth/post_birth_ring_spectrum_author file, fourth-campaign author derivation, checkpoint or registry was read. Only the assigned independent directory was written.','literature':'No external theorem or literature imported for this reconstruction.','failed_attempt':'SymPy charpoly generator assumptions mismatch; original source and real failed streams/receipt authenticate, coefficients unchanged.'}
(D/'SOURCE_IDENTITIES.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
