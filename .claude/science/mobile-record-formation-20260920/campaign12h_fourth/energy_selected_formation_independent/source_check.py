"""Authenticate only the declared allowed prior sources; no new-author access."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
D=HERE.parent
RAW=D.parents[3]
SPEC=[
('finite_spin_post_birth_author/PREPARED_FLAT_SECTOR_WITH_ELECTRIC_DYNAMICS_AND_FORMATION.md','94cef6093e754d59cf11ca07c1124f6ee8becd944c07865af21b1c6dd05ec2a9','Checked prepared no-event theorem; pure-Hamiltonian extension reconstructed in new report'),
('finite_spin_post_birth_author/AUTHOR_SEAL.json','dfc55f6eac748bb11130fe3a8e5544194c6babd810c0c06d45e177c56c72df7e','Supplied prepared source seal'),
('post_birth_ring_spectrum_author/EXACT_FAST_SPECTRUM_AND_FORMATION_OUTPUTS_ON_RINGS.md','b9c30d8418cb4d4c577ea193dee8482d2d0c92125823593feb2a7c01b8310bf5','Complete checked ring spectrum; ring point subspace and first outputs'),
('finite_spin_flat_independent/FINAL_SEAL.json','4bbbdcf3fa5a12181ccaf4e9ad09ec5dfb82fe4a078d5256ccad67caedf10cfe','Prior selective prepared check; not a new audit'),
('finite_spin_flat_independent/physical_builder.py','1cbc6dcb8a994c5f7fc4ec178c586b3aefcede49fd6a30906b0446bf332c9dc2','Frozen independent local rules imported by new controls'),
('finite_spin_flat_independent/flat_probe.py','ba04c00080143a8f0b9bfe3ed6b249139c1201a691f23584d911a78ebf237fd6','Frozen independent compact frame imported by new controls'),
('finite_spin_flat_independent/decisive_controls.py','a71dc53563701bbeae33e31e749527ea1cda4dc43166bb0aa670b480d68c1dc6','Read as prior reference; not imported; old unfiltered-loss comment is superseded by the prior clarification'),
('actual_first_output_independent/REPORT.md','578dc3b86852d4418d66b07c8d1f2159d68ad12730b6cbc16fc225cc363fbebb','Previously checked ring first sector, jump bounds, and projection conventions'),
('actual_first_output_independent/FINAL_SEAL.json','c5ed54dd73a633a433f51cba08c5221e6cad58ea306219a3002e2104e53ea69a','Prior ring actual-output check'),
('cube_point_spectrum_independent/REPORT.md','20303cc9320deb32799bdc98befc986c856943ac632d0245ace929c8140a7d7d','Supplied checked absence of physical cube H6 point spectrum'),
('cube_point_spectrum_independent/FINAL_SEAL.json','f2df1efd5a7c7a63fb5200c0becb48278f79e448000afddcc8dc2bc48785111f','Previously closed selective spectral comparison dependency; no new spectral proof'),
('cube_point_spectrum_independent/COMPARISON.md','8872145e6701ca9ee33e33572a9bc01fc816af429ad36867582aa8b9b31cbe08','Previously read spectral comparison, reused at unchanged identity'),
('cube_unprepared_independent/REPORT.md','2d33b037ebbdc469cb81db26af37554c3b8ba5aad47cf2772ca8cdd66c0b1294','Checked cube first electric/face Hamiltonian and full-space jump bounds'),
('cube_unprepared_independent/FINAL_SEAL.json','6c093df454da76bb474ce0f7f2283fc4729ced3ed540b779881418c07233b9ca','Previously completed cube consequence comparison'),
]


def identity(path,role=None):
    path=Path(path).resolve();data=path.read_bytes()
    answer={'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    if role is not None:answer['role']=role
    return answer


def bound_rows(value):
    if isinstance(value,dict):
        if all(k in value for k in ('path','bytes','sha256')):yield value
        for x in value.values():yield from bound_rows(x)
    elif isinstance(value,list):
        for x in value:yield from bound_rows(x)


def main():
    assert not (HERE/'SOURCE_IDENTITIES.json').exists()
    rows=[]
    for rel,sha,role in SPEC:
        row=identity(D/rel,role);assert row['sha256']==sha,rel;rows.append(row)
    manifests={name:json.loads((D/name).read_text()) for name in
               ['finite_spin_post_birth_author/AUTHOR_SEAL.json','finite_spin_flat_independent/FINAL_SEAL.json',
                'actual_first_output_independent/FINAL_SEAL.json','cube_point_spectrum_independent/FINAL_SEAL.json',
                'cube_unprepared_independent/FINAL_SEAL.json']}
    checks=[]
    for name,manifest in manifests.items():
        available={r['path']:r for r in bound_rows(manifest)}
        matched=[]
        for row in rows:
            if row['path'] in available:
                assert all(row[k]==available[row['path']][k] for k in ('path','bytes','sha256'))
                matched.append(row['path'])
        checks.append({'manifest':name,'matching_declared_source_bindings':matched})
    # Record other explicitly read allowed prior helpers, not new premises.
    extra=[identity(D/'actual_first_output_independent/consequence_check.py','Read prior independent implementation; not imported'),
           identity(D/'finite_spin_flat_independent/FINITE_SPIN_LOSS_CLARIFICATION.md','Prior correction: original unfiltered losses agree at finite S; energy-filtered losses need a new check')]
    instructions=[identity(RAW/'AGENTS.md'),identity(RAW/'docs/ai_methodology/SCIENCE_WORKFLOW.md'),
                  identity(RAW/'docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md'),
                  identity(Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md')),
                  identity(Path('/Users/jonreilly/.codex/skills/physics-loop/references/proof-search-governance.md'))]
    result={'science_sources':rows+extra,'matching_manifest_rows':checks,'instruction_snapshots':instructions,
            'instruction_freshness_limit':'Task forbids Git and checkpoint operations. Existing source snapshots are identified by hash; no fresh origin/main or ai/execution fetch is claimed. Only scoped proof-obligation and adversarial checks from the reviewer skill are applied.',
            'new_author_exposure':'No energy_selected_formation_author path, file, runner, result, or new root scientific message outside the brief was read before PRE.',
            'reuse_limit':'Only declared prior files authenticated; no recursive reopening of transitive author research, compensation/proposal/general-checker sources, plans, registries or checkpoints.',
            'writes':'Only energy_selected_formation_independent; no Git, checkpoint edits, publication, audit or delegation.'}
    (HERE/'SOURCE_IDENTITIES.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
