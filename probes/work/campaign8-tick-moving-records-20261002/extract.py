import json, sys
src, dst = sys.argv[1], sys.argv[2]
last = None
for line in open(src):
    try:
        d = json.loads(line)
    except Exception:
        continue
    msg = d.get("message") or {}
    if d.get("type") == "assistant" or msg.get("role") == "assistant":
        content = msg.get("content")
        if isinstance(content, list):
            txt = "".join(c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text")
        elif isinstance(content, str):
            txt = content
        else:
            txt = ""
        if txt.strip():
            last = txt
open(dst, "w").write(last or "")
print(len(last or ""), "chars")
