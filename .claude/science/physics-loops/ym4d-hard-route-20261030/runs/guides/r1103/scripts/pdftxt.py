import sys, re, zlib
data = open(sys.argv[1],'rb').read()
out=[]
for m in re.finditer(rb'stream\r?\n(.*?)\r?\nendstream', data, re.S):
    raw=m.group(1)
    try:
        d=zlib.decompress(raw)
    except Exception:
        continue
    if b'BT' not in d: continue
    # collect text from TJ / Tj
    txt=[]
    for line in re.finditer(rb'\[(.*?)\]\s*TJ|\((.*?)\)\s*Tj|(T\*|Td|TD|ET)', d, re.S):
        if line.group(1) is not None:
            parts=re.findall(rb'\(((?:\\.|[^\\)])*)\)|(-?\d+\.?\d*)', line.group(1))
            s=b''
            for a,b in parts:
                if a or not b: s+=a
                else:
                    if float(b) < -250: s+=b' '
            txt.append(s)
        elif line.group(2) is not None:
            txt.append(line.group(2))
        else:
            txt.append(b'\n')
    out.append(b''.join(txt))
sys.stdout.write(b'\n=====PAGE=====\n'.join(out).decode('latin-1'))
