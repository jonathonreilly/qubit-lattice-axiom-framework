import sys, re, zlib
data = open(sys.argv[1], 'rb').read()
out = []
for m in re.finditer(rb'stream\r?\n', data):
    start = m.end()
    end = data.find(b'endstream', start)
    if end < 0: continue
    chunk = data[start:end]
    try:
        dec = zlib.decompress(chunk)
    except Exception:
        try:
            dec = zlib.decompressobj().decompress(chunk)
        except Exception:
            continue
    if b'TJ' not in dec and b'Tj' not in dec: continue
    line = []
    for t in re.finditer(rb'\[(.*?)\]\s*TJ|\((.*?)\)\s*Tj|(T\*|Td|TD|Tm|ET)', dec, re.S):
        if t.group(1) is not None:
            parts = re.findall(rb'\(((?:\\.|[^\\)])*)\)|(-?\d+\.?\d*)', t.group(1))
            s = b''
            for p, num in parts:
                if p: s += p
                elif num:
                    try:
                        if float(num) < -200: s += b' '
                    except: pass
            line.append(s)
        elif t.group(2) is not None:
            line.append(t.group(2))
        else:
            line.append(b'\n' if t.group(3) in (b'T*', b'ET') else b' ')
    txt = b''.join(line)
    txt = re.sub(rb'\\(\d{3})', lambda q: bytes([int(q.group(1), 8)]), txt)
    txt = txt.replace(b'\\(', b'(').replace(b'\\)', b')').replace(b'\\\\', b'\\')
    out.append(txt.decode('latin-1'))
open(sys.argv[2], 'w').write('\n'.join(out))
print(len(out))
