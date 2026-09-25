"""Read-only structural inspection of released/frozen and own PRE evidence."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
paths=['DECISIVE_RESULTS.json','UNWRAPPED_PRIMITIVE_COLUMNS.json',
       'post_sources/author/attempt01/stdout.json','post_sources/author/attempt02/RESULT.json',
       'post_sources/author/attempt03/RESULT.json','post_sources/author/attempt04/RESULT.json',
       'post_sources/author/attempt05/RESULT.json']
for path in paths:
    data=json.loads((HERE/path).read_bytes())
    print('\nFILE',path)
    if isinstance(data,list):
        print('list length',len(data),'first row',json.dumps(data[0])[:2500])
        continue
    for key,value in data.items():
        if isinstance(value,list):
            print(key,'list',len(value),'first=',json.dumps(value[:1])[:1000])
        elif isinstance(value,dict):
            print(key,'dict keys=',list(value))
        else:print(key,json.dumps(value))
    if path=='DECISIVE_RESULTS.json':
        print('supersolution row',json.dumps(data['supersolution']['complete_unwrapped_type_rows'][0]))
        print('cross row',json.dumps(data['supersolution']['raw_ordered_primitive_cross_checks'][0]))
