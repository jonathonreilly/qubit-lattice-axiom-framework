"""Create a separately bound prose qualification; preserve all sealed evidence."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json

E = Path(__file__).resolve().parent
A = E / 'native-charge-current-noise-personal'
I = E / 'native-charge-current-noise-independent'
Q = E / 'native-charge-current-noise-qualified'
assert not Q.exists()
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
source = A / 'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md'
assert sha(source) == 'b8bec7cc03e7af401aae097445ae24faecd45dcffd8e0273300f16d17d455c1d'
assert sha(I / 'POST.md') == '66301af4de56c7a539b31fded490b8fd3196f978fc3f8cfeaeb51402ddf9927b'
assert sha(I / 'POST_SEAL.json') == '474656df6a908fd8964eb87e9ce20221b0fdd0496fb97363c071323856443e26'
old = ('Only for the separately supplied zero-field\n'
       'basis vector does the expectation of that off-diagonal Hamiltonian current\n'
       'vanish.')
new = ('For the separately supplied zero-field basis vector, the expectation of\n'
       'that off-diagonal Hamiltonian current vanishes; it need not vanish for\n'
       'arbitrary field input.')
text = source.read_text()
assert text.count(old) == 1
qualified = text.replace(old, new)
Q.mkdir()
note = Q / 'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_QUALIFIED.md'
note.write_text(qualified)
diff = ''.join(difflib.unified_diff(text.splitlines(True), qualified.splitlines(True),
                                 fromfile=str(source), tofile=str(note)))
(Q / 'WORDING_ONLY.diff').write_text(diff)
(Q / 'QUALIFICATION.md').write_text(
    '# Charge-current wording qualification\n\n'
    'This separate generation applies exactly the one prose repair required by '
    'sealed POST46. The original author note, author seal, PRE, POST, code and '
    'stored outputs remain unchanged. No equation or code changes.\n\n'
    'Every physical electric basis state, and every normal density diagonal in '
    'that basis, has zero expectation of the bounded off-diagonal Hamiltonian '
    'current. Nonzero circulation basis vectors disprove exclusivity of the '
    'zero-field vector. Coherent field inputs can have nonzero mean magnetic '
    'circulation. POST46 supplies the counterexample and proof.\n\n'
    'The qualified copy preserves the original author-stage chronology and '
    'does not relabel PRE additions as root discoveries. This is a wording '
    'qualification, not an audit verdict or empirical identification.\n')
bindings = [source, A/'AUTHOR_SEAL.json', I/'PRE.md', I/'PRE_SEAL.json',
            I/'POST.md', I/'POST_SEAL.json',
            E/'FORTY_SIXTH_POST_ROOT_READONLY_EXECUTION.json',
            E/'FORTY_SIXTH_POST_ROOT_READONLY.stdout.json', Path(__file__).resolve()]
seal = dict(at=datetime.now(timezone.utc).isoformat(), kind='Wording-only qualification',
            original_preserved=True, equations_or_code_changed=False,
            sources=[dict(path=str(p),sha256=sha(p)) for p in bindings],
            members=[dict(path=p.name,sha256=sha(p)) for p in sorted(Q.iterdir())])
(Q/'QUALIFICATION_SEAL.json').write_text(json.dumps(seal,indent=2,sort_keys=True)+'\n')
assert sha(source) == seal['sources'][0]['sha256']
assert note.read_text().replace(new,old) == text
print(diff)
print(json.dumps({'qualified_sha256':sha(note),'seal_sha256':sha(Q/'QUALIFICATION_SEAL.json')}))
