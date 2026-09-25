#!/usr/bin/env python3
"""Repair lost inline Markdown math delimiters; preserve the reviewed draft."""
from pathlib import Path
from datetime import datetime,timezone
import difflib,hashlib,json,re
HERE=Path(__file__).resolve().parent
path=HERE/'PRE.md';before=path.read_text();history=HERE/'history'
history.mkdir(exist_ok=True)
with (history/'PRE_before_math_delimiter_repair.md').open('x') as f:f.write(before)
contents=[
 r'L',r'n=|A|=|B|=L^3/2',r'g',r'P',r'N=n',r'N=n+2',r'n+2',
 r'E_q',r'E_q+Ck',r'k\in\mathbb Z^r',r'L^2(\mathbb T^r;\mathbb C^M)',
 r'K(0)',r'v',r'b,d',r"J,J'\subset B",r'Q_L=\sum C_{uv}C_{uv}^*',
 r"J'",r"Q_L(J',J)",r'Q_L',r'x',r'y',r'u',r'w',r'v\ne u',r'z',
 r'S_{uv}^*S_{uv}',r'6\times6',r'v_J>0',r'J',r'v_J',
 r'O(1)',r'\lambda',r'q_{0,L}',r'\Lambda_L',r'D\ge0',
 r'h_g\ge-\lambda/(2\tau g^2)',r'1+\sum_e E_e^2',r'D(D)',r'D',
 r'O_L(g^{-2})',r'H_4(\theta)',r'-2\lambda',r'O_L(|\theta|^2)',
 r'a,d',r'M',r'm(\{i,j\})',r'r\in\{1,2\}',r'r',r'a',r'd',
 r'L\ge6',r'3n',r'6n',r'L=4',r'15n/2',r'321n',r'3666n',r'6624n',
 r'270n',r'3120n',r'5280n',r'L=2',r'R',r'n-3',r'R_L',r'-5',
 r'(a,b)',r'B_j=Pj_{(a,b,\sigma)}F_aP',r'b',r'z_a-1',
 r'1/\sqrt{z_a-1}',r'E_0',r'V=H_4/(4\tau)',r'f',r'f(v_*)>0',
 r'V\ge v_*',r'v_*',r'(V-z)\mathcal F',r'V-z',r'V',r'f(V)',r'f(A_g)',
 r'L\ge4',r'm_{uv}',r'J=\{x,y\}',r'q_{0,L}-s_x-s_y',r'A_{xz}',
 r'x\to z\ne y',r"G(J',J)",r"J',J",r'L=2,4,6,8',r'36\times36',r'g^{-2}'
]
pattern=re.compile('|'.join(re.escape('('+x+')') for x in sorted(contents,key=len,reverse=True)))
fix_unbalanced={r'(M\)':r'(M)',r'(J=\{x,y\}\)':r'(J=\{x,y\})',
                r'(x\to z\ne y\)':r'(x\to z\ne y)'}
display=False;lines=[];replacements=0
for line in before.splitlines(keepends=True):
    if line.strip()==r'\[':display=True
    if display:
        lines.append(line)
        if line.strip()==r'\]':display=False
        continue
    for old,new in fix_unbalanced.items():line=line.replace(old,new)
    parts=re.split(r'(\\\(.*?\\\))',line)
    for i in range(0,len(parts),2):
        parts[i],count=pattern.subn(lambda m:r'\('+m.group(0)[1:-1]+r'\)',parts[i])
        replacements+=count
    lines.append(''.join(parts))
after=''.join(lines);path.write_text(after)
diff=''.join(difflib.unified_diff(before.splitlines(keepends=True),after.splitlines(keepends=True),
 fromfile='history/PRE_before_math_delimiter_repair.md',tofile='PRE.md'))
with (history/'MATH_DELIMITER_REPAIR.diff').open('x') as f:f.write(diff)
receipt=dict(created_utc=datetime.now(timezone.utc).isoformat(),scope=__doc__,
 before_sha256=hashlib.sha256(before.encode()).hexdigest(),
 after_sha256=hashlib.sha256(after.encode()).hexdigest(),inline_delimiter_replacements=replacements,
 complete_diff_sha256=hashlib.sha256(diff.encode()).hexdigest(),
 formulas_and_claims_changed=False,earlier_scientific_verifier_binding_retained=True)
with (HERE/'MATH_DELIMITER_REPAIR.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2))
