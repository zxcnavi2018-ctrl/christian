import json,subprocess,pymupdf,os
P='/home/user/christian/packs/';SP=os.getcwd()
def gen():
    subprocess.run(['python3',P+'fichas.py'],capture_output=True,check=True);subprocess.run(['python3',P+'fichas8.py'],capture_output=True,check=True)
def render(items):
    jobs=[[f'{P}u{n}/s{i}.html',f'{SP}/m_{n}_{i}.pdf'] for n,i in items]
    subprocess.run(['node','r1.js',json.dumps(jobs)],check=True,env={**os.environ,'NODE_PATH':'/opt/node22/lib/node_modules'})
def meas(n,i):
    d=pymupdf.open(f'{SP}/m_{n}_{i}.pdf');p=d[-1]
    ys=[b[3] for b in p.get_text('blocks')]+[r['rect'].y1 for r in p.get_drawings() if r['rect'].height<p.rect.height*0.9]
    return len(d),p.rect.height-40-max(ys)
S=[(7,i) for i in range(1,12)]+[(8,i) for i in range(1,8)]
fill={f'{n}-{i}':{"k":0,"h":0} for n,i in S}
json.dump(fill,open(P+'fill.json','w'));gen();render(S)
base={s:meas(*s) for s in S}
cfg={s:{"k":0,"r":0,"v":0,"c":0,"s":0,"h":0} for s in S}
steps=[("r",1),("c",1),("v",1),("k",1),("k",2),("k",3),("s",1),("k",4),("k",5)]
for key,val in steps:
    trial={s:dict(cfg[s]) for s in S}
    for s in S:trial[s][key]=val
    json.dump({f'{n}-{i}':trial[(n,i)] for n,i in S},open(P+'fill.json','w'));gen();render(S)
    for s in S:
        pg,fr=meas(*s)
        if pg==base[s][0]:cfg[s]=trial[s]
fill={f'{n}-{i}':cfg[(n,i)] for n,i in S}
json.dump(fill,open(P+'fill.json','w'));gen();render(S)
free={s:meas(*s)[1] for s in S}
for n,i in S:
    fr=free[(n,i)]
    fill[f'{n}-{i}']["h"]=int((fr-30)*96/72) if fr>80 else 0
json.dump(fill,open(P+'fill.json','w'));gen();render(S)
for s in S:
    pg,fr=meas(*s)
    if pg!=base[s][0] and fill[f'{s[0]}-{s[1]}']["h"]:
        fill[f'{s[0]}-{s[1]}']["h"]=max(0,fill[f'{s[0]}-{s[1]}']["h"]-60)
json.dump(fill,open(P+'fill.json','w'));gen();render(S)
for s in S:
    pg,fr=meas(*s);print(s,'pág',base[s][0],'->',pg,'| hueco antes',round(base[s][1]),'después',round(fr),'| datos',fill[f'{s[0]}-{s[1]}'])
