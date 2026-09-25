"""Correct inline-math escaping in the new, unsealed POST report only."""
from pathlib import Path
import re
import json
from hashlib import sha256

HERE=Path(__file__).resolve().parent
path=HERE/'POST.md'
raw=path.read_bytes()
history=HERE/'post_history'
history.mkdir(exist_ok=True)
with (history/'POST_before_math_typesetting.md').open('xb') as f:f.write(raw)
text=raw.decode()
lines=[];display=False;count=0
for line in text.splitlines(keepends=True):
    if line.strip()==r'\[':display=True
    if display:
        lines.append(line)
        if line.strip()==r'\]':display=False
        continue
    output=[];i=0
    while i<len(line):
        if line[i]!='(':
            output.append(line[i]);i+=1;continue
        depth=1;j=i+1
        while j<len(line) and depth:
            if line[j]=='(':depth+=1
            elif line[j]==')':depth-=1
            j+=1
        assert depth==0
        math=line[i+1:j-1]
        for symbol in ('Pi','Gamma','chi','psi','delta','langle','operatorname'):
            math=re.sub(r'(?<![A-Za-z\\])'+symbol+r'(?![A-Za-z])',lambda m:'\\'+m.group(),math)
        if math=='{a,d}':math=r'\{a,d\}'
        output.extend(('$',math,'$'));count+=1;i=j
    lines.append(''.join(output))
fixed=''.join(lines)
path.write_text(fixed)
print(json.dumps({'scope':'Editorial inline-math escaping only; no scientific code or sealed PRE change',
                  'before_sha256':sha256(raw).hexdigest(),'after_sha256':sha256(fixed.encode()).hexdigest(),
                  'inline_math_spans':count,'preserved_draft':'post_history/POST_before_math_typesetting.md'},indent=2))
