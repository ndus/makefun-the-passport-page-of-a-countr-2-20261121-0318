import os, time, zlib, struct, math

S=2; W=H=1024; w=h=W*S
img=bytearray([238,232,211,255])*(w*h)
def px(x,y,c):
    if 0<=x<w and 0<=y<h:
        i=(y*w+x)*4; img[i:i+4]=bytes(c)
def rect(x0,y0,x1,y1,c):
    x0,x1=int(x0*S),int(x1*S); y0,y1=int(y0*S),int(y1*S)
    for y in range(max(0,y0),min(h,y1)):
        i=(y*w+max(0,x0))*4; img[i:i+max(0,min(w,x1)-max(0,x0))*4]=bytes(c)*max(0,min(w,x1)-max(0,x0))
def line(x0,y0,x1,y1,c,th=1):
    x0*=S;y0*=S;x1*=S;y1*=S; dx=x1-x0;dy=y1-y0; n=int(max(abs(dx),abs(dy)))+1
    for k in range(n):
        t=k/max(1,n-1); x=int(x0+dx*t); y=int(y0+dy*t)
        for yy in range(y-int(th*S/2),y+int(th*S/2)+1):
            for xx in range(x-int(th*S/2),x+int(th*S/2)+1): px(xx,yy,c)
def ellipse(cx,cy,rx,ry,c,outline=None,th=1):
    x0=int((cx-rx)*S);x1=int((cx+rx)*S);y0=int((cy-ry)*S);y1=int((cy+ry)*S)
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            q=((x/S-cx)/rx)**2+((y/S-cy)/ry)**2
            if q<=1 and outline is None: px(x,y,c)
            elif outline is not None and 1-th/100<=q<=1: px(x,y,outline)
def text(x,y,s,c=(35,43,47,255),scale=2,mono=False,spacing=1):
    # compact 5x7 font; unknown glyphs render as a box
    F={'A':'01110 10001 10001 11111 10001 10001 10001','B':'11110 10001 10001 11110 10001 10001 11110','C':'01111 10000 10000 10000 10000 10000 01111','D':'11110 10001 10001 10001 10001 10001 11110','E':'11111 10000 10000 11110 10000 10000 11111','F':'11111 10000 10000 11110 10000 10000 10000','G':'01111 10000 10000 10111 10001 10001 01111','H':'10001 10001 10001 11111 10001 10001 10001','I':'11111 00100 00100 00100 00100 00100 11111','J':'00111 00010 00010 00010 10010 10010 01100','K':'10001 10010 10100 11000 10100 10010 10001','L':'10000 10000 10000 10000 10000 10000 11111','M':'10001 11011 10101 10101 10001 10001 10001','N':'10001 11001 10101 10011 10001 10001 10001','O':'01110 10001 10001 10001 10001 10001 01110','P':'11110 10001 10001 11110 10000 10000 10000','Q':'01110 10001 10001 10001 10101 10010 01101','R':'11110 10001 10001 11110 10100 10010 10001','S':'01111 10000 10000 01110 00001 00001 11110','T':'11111 00100 00100 00100 00100 00100 00100','U':'10001 10001 10001 10001 10001 10001 01110','V':'10001 10001 10001 10001 10001 01010 00100','W':'10001 10001 10001 10101 10101 11011 10001','X':'10001 10001 01010 00100 01010 10001 10001','Y':'10001 10001 01010 00100 00100 00100 00100','Z':'11111 00001 00010 00100 01000 10000 11111','0':'01110 10011 10101 11001 10001 10001 01110','1':'00100 01100 00100 00100 00100 00100 01110','2':'01110 10001 00001 00010 00100 01000 11111','3':'11110 00001 00001 01110 00001 00001 11110','4':'00010 00110 01010 10010 11111 00010 00010','5':'11111 10000 10000 11110 00001 00001 11110','6':'01110 10000 10000 11110 10001 10001 01110','7':'11111 00001 00010 00100 01000 01000 01000','8':'01110 10001 10001 01110 10001 10001 01110','9':'01110 10001 10001 01111 00001 00001 01110','<':'10000 01000 00100 00010 00001 00000 00000','-':'00000 00000 00000 11111 00000 00000 00000','/':'00001 00010 00100 01000 10000 00000 00000',' ':'00000 00000 00000 00000 00000 00000 00000',':':'00000 00100 00100 00000 00100 00100 00000'}
    for ch in s:
        rows=F.get(ch,F['-']).split();
        for yy,row in enumerate(rows):
            for xx,v in enumerate(row):
                if v=='1': rect(x+xx*scale,y+yy*scale,x+(xx+1)*scale,y+(yy+1)*scale,c)
        x+=(5+spacing)*scale
def label(x,y,k,v): text(x,y,k,(83,87,81,255),1); text(x,y+9,v,(28,36,40,255),2)

# desk and booklet shadow
rect(0,0,1024,1024,(25,34,43,255)); rect(86,77,938,950,(10,14,18,255)); rect(92,70,932,944,(239,233,211,255))
rect(92,70,512,944,(244,239,220,255)); rect(512,70,932,944,(235,229,207,255)); line(512,70,512,944,(166,157,137,255),3)
# restrained guilloche
for r in range(35,240,16): ellipse(300,470,r,r*.68,None,(213,208,186,255),1)
for r in range(30,220,22): ellipse(720,510,r,r*.7,None,(216,210,187,255),1)
text(120,100,'REPUBLIC OF VESPERAL',(40,50,53,255),3); text(120,125,'PASSPORT / PASSEPORT',(91,94,86,255),1)
line(120,145,475,145,(64,72,70,255),1)
# portrait
rect(122,170,292,345,(210,215,207,255)); rect(128,176,286,339,(195,205,201,255)); ellipse(207,246,48,68,(225,188,158,255)); ellipse(207,200,52,31,(119,61,45,255)); rect(160,187,254,215,(119,61,45,255)); ellipse(188,245,5,4,(75,82,84,255)); ellipse(226,245,5,4,(75,82,84,255)); line(194,275,220,275,(120,70,62,255),2); rect(152,310,262,339,(83,91,101,255)); line(122,345,292,345,(83,87,81,255),1)
label(315,174,'SURNAME','MARSH'); label(315,214,'GIVEN NAMES','ELENA VEY'); label(315,254,'NATIONALITY','VESPERALIAN'); label(315,294,'DATE OF BIRTH','14 MAR 1988'); label(315,334,'PLACE OF BIRTH','PORT LUMEN'); label(120,370,'SEX','F'); label(220,370,'HEIGHT','168 CM'); label(330,370,'EYES','GREY'); label(120,410,'PASSPORT NO','VSP 0044172'); label(300,410,'DATE OF ISSUE','02 MAY 2019'); label(120,450,'DATE OF EXPIRY','02 MAY 2029'); label(300,450,'AUTHORITY','PORT LUMEN')
rect(120,510,475,570,(238,232,209,255)); line(120,510,475,510,(80,82,75,255),1); line(120,570,475,570,(80,82,75,255),1); text(132,525,'VALID FOR ENTRY 18:00-06:00 ONLY',(53,58,58,255),2); text(132,546,'NIGHT RECIPROCITY CLASS',(53,58,58,255),2); text(370,550,'DUSK FEE PAID 40 MOON CREDITS',(100,62,52,255),1)
text(120,870,'P<VSPVEY<<ELENA<MARSH<<<<<<<<<<<<<<<<<<<<<<<',(28,34,37,255),2,True,0); text(120,890,'0044172<8VSP8803146F2905024<<<<<<<<<<<<<<<04',(28,34,37,255),2,True,0)
text(548,105,'VISAS',(45,54,56,255),3); line(548,145,890,145,(64,72,70,255),1)
def stamp(cx,cy,name,kind,date,col,ang=0):
    ellipse(cx,cy,116,67,(235,230,208,255),col,2); ellipse(cx,cy,104,56,(235,230,208,255),col,1); text(cx-75,cy-30,name,col,1 if len(name)>15 else 2); text(cx-47,cy-5,kind,col,2); text(cx-47,cy+20,date,col,2); line(cx-80,cy+43,cx+80,cy+43,col,1)
stamp(700,250,'KHARAT UNION','ENTRY','18 NOV 2021',(35,70,125,255)); stamp(805,390,'KHARAT UNION','EXIT','02 DEC 2021',(117,40,45,255)); stamp(670,545,'REPUBLIC OF OSTROV','ENTRY','09 JUN 2023',(45,113,70,255)); stamp(790,700,'VESPERAL PORT LUMEN','ENTRY','27 AUG 2024',(35,70,125,255))
for y in range(760,840,14): text(550,y,'VESPERAL  VESPERAL  VESPERAL',(188,183,164,255),1)

def downscale():
    out=bytearray(W*H*4)
    for y in range(H):
        for x in range(W):
            vals=[0,0,0,0]
            for yy in (0,1):
                for xx in (0,1):
                    i=((y*2+yy)*w+x*2+xx)*4
                    for q in range(4): vals[q]+=img[i+q]
            j=(y*W+x)*4
            for q in range(4): out[j+q]=vals[q]//4
    return out
def png(data):
    def chunk(t,d): return struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
    raw=b''.join(b'\0'+data[y*W*4:(y+1)*W*4] for y in range(H))
    return b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',W,H,8,6,0,0,0))+chunk(b'IDAT',zlib.compress(raw,9))+chunk(b'IEND',b'')
start=time.time(); outdir=os.environ.get('MAKEFUN_OUTPUT_DIR','/output'); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,'entry.png'),'wb') as f:f.write(png(downscale()))
print('render_seconds %.3f'% (time.time()-start)); print('MRZ lengths',len('P<VSPVEY<<ELENA<MARSH<<<<<<<<<<<<<<<<<<<<<<<'),len('0044172<8VSP8803146F2905024<<<<<<<<<<<<<<<04'))
