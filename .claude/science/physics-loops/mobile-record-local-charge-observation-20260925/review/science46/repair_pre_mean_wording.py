#!/usr/bin/env python3
"""One-time pre-seal prose repair WRITER; equations and scientific code unchanged."""
from datetime import datetime, timezone
from pathlib import Path
import difflib, hashlib, json

base=Path(__file__).resolve().parent
target=base/'PRE.md'
before=target.read_bytes()
old='The charge mean is -60 kappa on A and +60 kappa on B.'
new='The initial charge-mean derivative is -60 kappa on A and +60 kappa on B.'
text=before.decode();assert text.count(old)==1
after=text.replace(old,new).encode()
history=base/'history';history.mkdir(exist_ok=True)
snapshot=history/'PRE_before_mean_derivative_wording.md'
with snapshot.open('xb') as f:f.write(before)
target.write_bytes(after)
diff=''.join(difflib.unified_diff(text.splitlines(keepends=True),after.decode().splitlines(keepends=True),fromfile='PRE before wording correction',tofile='PRE corrected'))
with (base/'PRE_WORDING_REPAIR.diff').open('x') as f:f.write(diff)
record=dict(at_utc=datetime.now(timezone.utc).isoformat(),old_phrase=old,new_phrase=new,
            before_sha256=hashlib.sha256(before).hexdigest(),after_sha256=hashlib.sha256(after).hexdigest(),
            preserved_before=str(snapshot.relative_to(base)),reason='Correct prose to say initial derivative; mean itself vanishes at t=0 as equations already state.',
            equations_or_controls_changed=False,scientific_programs_rerun=False)
with (base/'PRE_WORDING_REPAIR.json').open('x') as f:f.write(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
