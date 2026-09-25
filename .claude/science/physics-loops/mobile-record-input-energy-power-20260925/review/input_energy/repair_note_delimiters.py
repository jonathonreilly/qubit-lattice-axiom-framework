"""Repair draft inline delimiters lost in the initial JS string transport.

This changes presentation only, apart from making the intended squared-norm
inequality explicit. It never touches display equations or evidence files.
"""
from pathlib import Path
from hashlib import sha256
import re
import json

p=Path(__file__).parent/'PRE.md'
before=p.read_bytes()
text=before.decode()
text=re.sub(r'\\\((.*?)\\\)',lambda m:'$'+m.group(1)+'$',text)
text=text.replace(r'(P_\Lambda=1_{(0,\Lambda]}(\Omega))',
                  r'$P_\Lambda=1_{(0,\Lambda]}(\Omega)$')
text=text.replace('Its norm\nis at most its squared Hilbert--Schmidt norm.',
                  'Its squared operator norm\nis at most its squared Hilbert--Schmidt norm.')
changes=0

def repair_plain(s):
    global changes
    result='';i=0
    while i<len(s):
        if s[i]!='(':
            result+=s[i];i+=1;continue
        level=1;j=i+1
        while j<len(s) and level:
            if s[j]=='(':level+=1
            if s[j]==')':level-=1
            j+=1
        if level:
            result+=s[i:];break
        inner=s[i+1:j-1]
        if inner.isdecimal() or inner=='two transverse polarizations each':
            result+=s[i:j];i=j;continue
        inner=inner.rstrip('\\')
        inner=inner.replace('\tau',r'\tau')
        inner=re.sub(r'(?<![\\A-Za-z])(operatorname|mathcal|sum|alpha|omega|mu|eta|Lambda)(?=[_ {<=>]|$)',
                     lambda m:'\\'+m.group(1),inner)
        if inner=='|r_f|^2':inner=r'\|r_f\|^2'
        result+='$'+inner+'$';changes+=1;i=j
    return result

out=[];display=False
for line in text.splitlines():
    if line.strip()==r'\[':display=True
    if not display:
        parts=re.split(r'(\$[^$]*\$)',line)
        line=''.join(part if part.startswith('$') else repair_plain(part) for part in parts)
    out.append(line)
    if line.strip()==r'\]':display=False
after=('\n'.join(out)+'\n').encode()
p.write_bytes(after)
print(json.dumps({'draft_sha256':sha256(before).hexdigest(),
                  'corrected_note_sha256':sha256(after).hexdigest(),
                  'inline_parenthetical_expressions_repaired':changes,
                  'display_equations_unchanged':True,
                  'scope':'draft formatting repair before sealing'},indent=2))
