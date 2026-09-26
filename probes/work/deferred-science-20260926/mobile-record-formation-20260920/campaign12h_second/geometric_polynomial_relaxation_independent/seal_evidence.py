#!/usr/bin/env python3
"""Bind this bounded review; never writes outside its evidence directory."""
from pathlib import Path
import datetime,hashlib,json,sys
HERE=Path(__file__).resolve().parent
RAW=HERE.parent
ROOT=RAW.parents[3]
LIT=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/literature')
def identity(path):
    path=Path(path)
    return {'path':str(path),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
def save(name,data):
    (HERE/name).write_text(json.dumps(data,indent=2)+'\n')
def expected(path,digest):
    row=identity(path);assert row['sha256']==digest,(str(path),row['sha256'],digest);return row

sources=[
    expected(RAW/'GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md','f9d12f1fccc3ea54d3b640deaccdcbb04749db1d6ac5b7b2708193a4a0dd89bb'),
    expected(RAW/'geometric_polynomial_relaxation_check.py','fded420e936b93bee16aeba4bfed676363d0298e6c1268fa5193cea5ef0c0202'),
    expected(RAW/'GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md','70af6469a0e81cbb592ae710eaac07a61912d9754bc98d277ffbf5023301a959'),
    expected(RAW/'GEOMETRIC_PARTNER_RECORD_FORMATION.md','1bc76bc39c672c7eec318fb4e999dc6e2b1f80aad9a058683dbeb7f7ae247969'),
    expected(RAW/'GEOMETRIC_LAST_PAIR_CLOCK_AND_MONOMERS.md','0f5c6bdb5ce0c2ac3e7aa32bef5dfe57e1de0f914c81af984e4195d92722ebd7'),
    expected(LIT/'Jerrum_Sinclair_1989_ApproximatingPermanent.pdf','607ee31f4dbea8dd7cc3f59ca27915252334671268c6b4251069a23cd8ada3e9'),
    expected(LIT/'Taggi_1909.06558v3.pdf','50a6f8a42cd5865a509efb706823e2dd0061233f49e6ec06d5395a627c1d2517'),
]
procedures=[
    expected(ROOT/'AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
    expected(ROOT/'docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'),
    expected('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md','9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455'),
]
dependencies=[]
for folder,names,seal_hash in [
    ('geometric_general_graph_independent',['REPORT.md','independent_check.py','COUNTERCONTROLS.json','BRIDGE_EXCURSION.json'],'98d1312f06eb9bb0ce929b9d56c7dec687f0383a732330034b9029d276811646'),
    ('geometric_last_pair_clock_independent',['REPORT.md','LITERATURE_READ_RECEIPT.json'],'e960bd539083047d983c763122177b3478e89ad5df48d24427535cd61e10affb'),
]:
    sealed=RAW/folder/'FINAL_SEAL.json';dependencies.append(expected(sealed,seal_hash))
    prior=json.loads(sealed.read_text())
    known={Path(row['path']).name:row for row in prior['artifacts']}
    for name in names:dependencies.append(expected(RAW/folder/name,known[name]['sha256']))
external_extracts=[identity(p) for p in sorted((LIT/'independent_polynomial_relaxation').iterdir()) if p.is_file()]
mode=sys.argv[1]
if mode=='pre':
    assert not (HERE/'PRE_COMPARISON_SEAL.json').exists()
    save('READ_BOUNDARY.json',{
        'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'read':['Complete frozen primary note','Identity-matched earlier independent connectivity and clock evidence','JS1989 pages4,5,8,9,13; formula images pages5 and13'],
        'not_read':['Author polynomial checker body (only hash)','Author polynomial results or logs','New kinetic sources','Production simulations or observables'],
        'verification_kind':'Independent reconstruction of supplied proof before comparison; external theorem statements/hypotheses imported, not their whole proofs',
        'writes':'This evidence directory; external third-party page extracts/renderings kept in the supplied literature area only.'})
    save('LITERATURE_RECEIPT.json',{
        'primary_url':'https://people.eecs.berkeley.edu/~sinclair/perm.pdf',
        'source':sources[-2],
        'read_boundary':'PDF pages4,5,8,9,13; exact theorem3.6 formula checked visually on page13 and theorem2.2 on page5; whole 1989 proof not independently reconstructed.',
        'web_attempt':'web.open primary URL failed: content length too large (11,144,147 bytes). This is a transcription of the tool result, not a raw saved HTTP response.',
        'extraction_warning':'pypdf layout extraction warned: Rotated text discovered. Output will be incomplete. Formula-bearing pages were visually checked; no claim that extraction covers sidebar text.',
        'page_files_external':external_extracts,
        'hypotheses_checked':['Any finite simple graph with a perfect matching for theorem3.6','Uniform matching law','One graph-edge proposal and extra one-half hold','Theorem2.2 reversible ergodic lazy chain and stationary-escape conductance'],
        'Taggi_reuse':{'pdf':sources[-1],'prior_statement_hypothesis_receipt':dependencies[-1],
                      'scope':'Fixed d>2, even cubic periodic side>=4, unweighted all-sector perfect matchings; Eq2.5 and Theorem2.1 imported at unchanged identity.'},
        'not_claimed':'Independent proof verification of the entire JS1989 or Taggi theorem.'})
    artifacts=[identity(p) for p in sorted(HERE.iterdir()) if p.is_file()]
    seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':'Before author-checker/results access','sources':sources,'procedures_reused':procedures,'dependencies_reused':dependencies,'external_extracts':external_extracts,'artifacts':artifacts,'provisional_findings':[]}
    save('PRE_COMPARISON_SEAL.json',seal)
elif mode=='final':
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in pre['artifacts']:expected(row['path'],row['sha256'])
    additions=json.loads((HERE/'AUTHOR_COMPARISON.json').read_text())['author_evidence_sources']
    for row in additions:expected(row['path'],row['sha256'])
    artifacts=[identity(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='FINAL_SEAL.json']
    seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':'Final source comparison','sources':sources+additions,'procedures_reused':procedures,'dependencies_reused':dependencies,'external_extracts':external_extracts,'artifacts':artifacts,'precomparison_preserved':True,'unresolved_findings':[],'status':'Bounded scientific source check; no formal audit or landing verdict.'}
    save('FINAL_SEAL.json',seal)
else: raise ValueError(mode)
print(json.dumps(identity(HERE/('PRE_COMPARISON_SEAL.json' if mode=='pre' else 'FINAL_SEAL.json')),indent=2))
