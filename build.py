#!/usr/bin/env python3
"""Build Blaster Master (BLAST) — Sunsoft's 1988 NES game (the localization of
Chō Wakusei Senki Metafight) as a UD0 game-world, themed to the source: a dark
cavern / steel-blue SOPHIA palette, an ANIMATED CANVAS 3D title (software-rendered
rotating low-poly SOPHIA THE 3RD over a perspective grid — not SVG, not 2D),
8-bit/CRT, hobby domain. Genesis (the Metafight localization), the descent, and
the .dlw birth. Render-not-invent; the Jason/Fred localization vs Metafight flagged.
Blaster Master is © Sunsoft; a fan tribute."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "BLASTER MASTER", "axiom": "BLAST",
 "position": "Blaster Master · Sunsoft · NES 1988 — the localization of Chō Wakusei Senki Metafight (1988)",
 "origin": "a subterranean world of eight areas a boy descends into after his frog, piloting the tank SOPHIA THE 3RD",
 "mechanism": "Crystallized from Blaster Master (Sunsoft, NES 1988) — the Western localization of the Famicom's Metafight.",
 "crystallization": "A side-scrolling tank game and a top-down dungeon-crawler in one: drive SOPHIA THE 3RD, grow it Hover→Dive→Wall-climb, step out on foot into overhead bases, and descend to the Plutonium Boss.",
 "nature": "Blaster Master — Sunsoft's dual-mode NES classic: the battle tank SOPHIA THE 3RD across side-scrolling caverns, Jason on foot in top-down bases, a Metroid-like gated descent, and one of the system's most celebrated soundtracks.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Blaster Master; Metafight; Jason; Fred the frog; SOPHIA THE 3RD; the upgrades; the overhead bases; the Plutonium Boss",
 "witness": "A planetary-war epic in Japan, a boy-and-his-frog story in the West — the same tank, two stories bolted to one cartridge.",
 "role": "the dual-mode game-world",
 "seal": "Chase the frog down the hole, climb into the tank — and grow it, wall by wall, until it drives on ceilings to the bottom of the world.",
 "source": "Blaster Master, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#7fa0c0", "flesh and the underground — the boy, the frog, the mutant wardens"),
 "ethereal":  ("#9a7cff", "of the descent — the overhead maze, the deepening dark, the boss at the bottom"),
 "spiritual": ("#e0405a", "of the soul beneath — the original Metafight, and the score the cartridge is remembered by"),
 "electrical":("#3a9bd5", "of the wire and the machine — SOPHIA THE 3RD and the powers she grows into"),
}

# ── the title scene · ANIMATED CANVAS 3D (rotating low-poly SOPHIA THE 3RD) ─────
CANVAS_ART = r'''<canvas id="bm" width="700" height="380" style="width:100%;height:auto;display:block;background:#05070e"></canvas>
<script>
(function(){
var cv=document.getElementById('bm');if(!cv)return;var g=cv.getContext('2d'),W=700,H=380,CX=350,CY=210,F=560,CAM=6,TX=-0.34;
var stars=[];for(var i=0;i<70;i++)stars.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.3+.4,a:Math.random()});
var BOXES=[
 [0,-0.5,0, 3.0,0.5,1.7,'#243140'],
 [0,0,0, 2.6,0.62,1.4,'#3f5f80'],
 [0.12,0.62,0, 1.15,0.7,0.95,'#5f93c0'],
 [1.4,0.45,0, 1.8,0.24,0.24,'#9aa6b4'],
 [-1.25,0.34,0, 0.5,0.55,1.05,'#2a3a4c'],
 [0.12,1.02,0, 0.5,0.2,0.5,'#d83828'],
 [0,-0.5,0.95, 3.0,0.55,0.22,'#1b2630'],
 [0,-0.5,-0.95, 3.0,0.55,0.22,'#1b2630']
];
function mkBox(b){var cx=b[0],cy=b[1],cz=b[2],w=b[3]/2,h=b[4]/2,d=b[5]/2;
 var v=[[-w,-h,-d],[w,-h,-d],[w,h,-d],[-w,h,-d],[-w,-h,d],[w,-h,d],[w,h,d],[-w,h,d]].map(function(p){return [p[0]+cx,p[1]+cy,p[2]+cz];});
 return {v:v,f:[[0,1,2,3],[5,4,7,6],[4,0,3,7],[1,5,6,2],[3,2,6,7],[4,5,1,0]],col:b[6]};}
var MODEL=BOXES.map(mkBox);
function rotY(p,a){var c=Math.cos(a),s=Math.sin(a);return [p[0]*c+p[2]*s,p[1],-p[0]*s+p[2]*c];}
function rotX(p,a){var c=Math.cos(a),s=Math.sin(a);return [p[0],p[1]*c-p[2]*s,p[1]*s+p[2]*c];}
function proj(p){var z=p[2]+CAM;if(z<0.1)z=0.1;return [CX+p[0]*F/z,CY-p[1]*F/z];}
var L=[0.4,0.7,-0.6],ll=Math.hypot(L[0],L[1],L[2]);L=[L[0]/ll,L[1]/ll,L[2]/ll];
function shade(col,br){var n=parseInt(col.slice(1),16),r=(n>>16)&255,gg=(n>>8)&255,bb=n&255;br=Math.max(.34,Math.min(1.15,br));
 return 'rgb('+Math.min(255,r*br|0)+','+Math.min(255,gg*br|0)+','+Math.min(255,bb*br|0)+')';}
function grid(){g.strokeStyle='rgba(60,130,180,.22)';g.lineWidth=1;var gz;
 for(var gx=-7;gx<=7;gx++){var a=rotX([gx,-0.85,-3],TX),b=rotX([gx,-0.85,12],TX),pa=proj(a),pb=proj(b);g.beginPath();g.moveTo(pa[0],pa[1]);g.lineTo(pb[0],pb[1]);g.stroke();}
 for(gz=-3;gz<=12;gz++){var a=rotX([-7,-0.85,gz],TX),b=rotX([7,-0.85,gz],TX),pa=proj(a),pb=proj(b);g.beginPath();g.moveTo(pa[0],pa[1]);g.lineTo(pb[0],pb[1]);g.stroke();}}
function frame(t){
 g.fillStyle='#05070e';g.fillRect(0,0,W,H);
 stars.forEach(function(s){g.globalAlpha=.3+.6*Math.abs(Math.sin(t/900+s.a*6));g.fillStyle='#9fc8e8';g.fillRect(s.x,s.y,s.r,s.r);});g.globalAlpha=1;
 grid();
 var ang=t/1700,polys=[];
 MODEL.forEach(function(m){var rv=m.v.map(function(p){return rotX(rotY(p,ang),TX);});
  m.f.forEach(function(f){var p0=rv[f[0]],p1=rv[f[1]],p2=rv[f[2]];
   var ux=p1[0]-p0[0],uy=p1[1]-p0[1],uz=p1[2]-p0[2],wx=p2[0]-p0[0],wy=p2[1]-p0[1],wz=p2[2]-p0[2];
   var nx=uy*wz-uz*wy,ny=uz*wx-ux*wz,nz=ux*wy-uy*wx,nl=Math.hypot(nx,ny,nz)||1;nx/=nl;ny/=nl;nz/=nl;
   var br=0.5+0.7*Math.max(0,nx*L[0]+ny*L[1]+nz*L[2]);
   var avz=(rv[f[0]][2]+rv[f[1]][2]+rv[f[2]][2]+rv[f[3]][2])/4;
   polys.push({pts:f.map(function(i){return proj(rv[i]);}),z:avz,col:shade(m.col,br)});});});
 polys.sort(function(a,b){return b.z-a.z;});
 polys.forEach(function(P){g.beginPath();g.moveTo(P.pts[0][0],P.pts[0][1]);for(var i=1;i<4;i++)g.lineTo(P.pts[i][0],P.pts[i][1]);g.closePath();
  g.fillStyle=P.col;g.fill();g.strokeStyle='rgba(0,0,0,.3)';g.lineWidth=1;g.stroke();});
 g.textAlign='center';
 g.fillStyle='#0a0e16';g.font='900 30px "Arial Black",Impact,sans-serif';g.fillText('BLASTER MASTER',352,50);
 g.fillStyle='#e0a828';g.fillText('BLASTER MASTER',350,48);
 g.fillStyle='#6fa8d8';g.font='10px monospace';g.fillText('SUNSOFT · NES · 1988 · pilot SOPHIA THE 3RD',350,70);
 requestAnimationFrame(frame);
}
frame(0);
})();
</script>'''

GENESIS = [
 ("Metafight, Localized", "Japan 1988 → US 1988",
  "In Japan the game is 超惑星戦記メタファイト — Chō Wakusei Senki Metafight — an interstellar war on the planet Sophia, a soldier in the tank Metal Attacker. Sunsoft's US localization bolted on a homier frame: a boy, Jason, and his pet frog Fred."),
 ("The Frog Down the Hole", "the American premise",
  "Fred touches a glowing radioactive chest, mutates and leaps, and falls into a hole in the ground. Jason chases him down — and finds SOPHIA THE 3RD, an abandoned battle tank, and a subterranean world of mutants."),
 ("Two Games in One", "side-scroll + overhead",
  "Drive SOPHIA through side-scrolling caverns; then exit on foot, gun in hand, as the camera flips to a top-down OVERHEAD view for the dungeon-bases and their bosses. Eight areas, and Sunsoft's legendary sound by Naoki Kodaka."),
]

ARC = [
 ("Down After Fred", "the descent begins",
  "Jason follows his mutated frog into a hole and finds the tank SOPHIA THE 3RD waiting in the dark. He climbs in, and the underground war is his."),
 ("Grow the Machine", "Metroid-like gating",
  "The tank you start with can't pass certain walls or waters — until you beat a boss and gain HOVER, then DIVE, then WALL-CLIMB. Each power opens the map further; on foot in the overhead bases you upgrade the gun."),
 ("The Bottom of the World", "the Plutonium Boss",
  "Eight areas deep, past the mutant wardens, waits the Plutonium Boss — the thing the whole long climb-down was always heading toward."),
]

IDEAS = [
 ("Tank and Foot", "the dual-mode design", [
   "A side-scrolling vehicle game and a top-down dungeon-crawler in one cartridge — you switch by leaving the tank.",
   "The overhead bases hide the bosses; SOPHIA waits outside while Jason goes in alone." ]),
 ("Grow Into a God-Machine", "the upgrade map", [
   "Hover, dive, wall-climb — each unlock turns the tank you couldn't steer past a wall into one that drives on ceilings.",
   "A Metroid-style gated world, when that was still rare." ]),
 ("The Sunsoft Sound", "remembered by its score", [
   "Naoki Kodaka's soundtrack is among the most celebrated on the NES — Sunsoft's bass-heavy audio mastery.",
   "People who never finished Blaster Master still hum it." ]),
]

SECTIONS = [
 ("The Releases", "the war, ported", [
   ("超惑星戦記メタファイト · Metafight", "1988 · Famicom (Sunsoft)", "the Japanese original — a planetary war, no boy, no frog"),
   ("Blaster Master", "1988 · NES (Sunsoft, US)", "the Western localization — Jason, Fred, SOPHIA THE 3RD"),
   ("re-releases", "later", "Virtual Console · NES — Nintendo Switch Online"),
 ]),
 ("The Makers", "Sunsoft", [
   ("Sunsoft", "developer / publisher", "the house known for NES technical &amp; audio mastery"),
   ("Naoki Kodaka", "composer", "the legendary Blaster Master score"),
 ]),
 ("The Legacy", "the tank reborn", [
   ("Blaster Master 2", "1991 · Genesis", "the direct sequel"),
   ("Blaster Master: Blasting Again", "2000 · PS1", "the 3D sequel"),
   ("Blaster Master Zero", "2017 · Inti Creates", "the revival that re-canonized the series (+ Zero 2 2019, Zero 3 2021), fusing Metafight and Jason's lore"),
 ]),
]

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("jason", "Jason", "the boy who chased his frog · the pilot", "natural",
  "the boy who follows his frog down a hole and finds a war machine — the on-foot pilot of SOPHIA who exits the tank, gun in hand, to enter the overhead dungeon-bases (the American story's hero)",
  "He is the everyboy at the wheel of a god-machine: a kid who went after a runaway frog and ended up fighting a subterranean war."),
 ("fred", "Fred", "the frog · the smallest cause", "natural",
  "Jason's pet frog, who touches a glowing radioactive chest, mutates and leaps, and falls into the hole — the inciting accident of the American story",
  "He is the smallest cause of the largest war: the frog whose one jump opened the earth."),
 ("sophia", "SOPHIA THE 3RD", "the battle tank · the star", "electrical",
  "the armored battle tank Jason finds and pilots through the side-scrolling world — the star of the game and the box, grown from a stuck vehicle into a wall-walking god-machine (the 1988 game names it simply Sophia the 3rd; 'Sophia J-7' is the later-series designation)",
  "It is the machine made a character: a tank you grow into a god, climbing walls and diving seas it could not at the start."),
 ("the-upgrades", "The Upgrades", "Hover · Dive · Wall-climb", "electrical",
  "SOPHIA's gained powers — Hover (sustained flight), Dive (underwater), Wall-climb (crawl up walls and across ceilings), plus the cannon and gun upgrades — each unlocked by beating a boss",
  "They are the machine's growth rings: the Metroid-like gating where the tank that couldn't pass a wall becomes the tank that walks on the ceiling."),
 ("the-overhead", "The Overhead", "the top-down dungeon mode", "ethereal",
  "the top-down OVERHEAD sections — Jason leaves SOPHIA, on foot with an upgradeable gun, to enter the dungeon-bases and fight the bosses; the camera flips from side-scroll to overhead",
  "It is the game's second self: the perspective that turns when you step out of the machine, the maze beneath the side-scroll."),
 ("plutonium-boss", "The Plutonium Boss", "the thing at the bottom", "ethereal",
  "the final boss at the deepest area — the mutant lord guarding the bottom of the descent",
  "It is the thing at the bottom of the world: the horror the whole long climb-down was always for."),
 ("the-mutants", "The Mutants", "the wardens of the dark", "natural",
  "the menagerie of mutant creatures and area bosses Jason and SOPHIA fight across the eight areas — the radioactive life of the underground",
  "They are the underworld's wardens: the mutated life that filled the dark while the surface forgot it."),
 ("the-descent", "The Subterranean World", "eight areas, going down", "ethereal",
  "the underground world of eight areas Jason descends into through the hole — caverns, water, bases, the deepening dark",
  "It is the stage as a going-down: a world entered by falling, each area deeper and stranger than the last."),
 ("metafight", "Metafight", "the game beneath · the true self", "spiritual",
  "超惑星戦記メタファイト — Chō Wakusei Senki Metafight (Sunsoft, Japan 1988) — the original Blaster Master is the localization of: an interstellar war whose hero is Kane Gardner, no boy and no frog. The twist: in Metafight, 'Sophia the 3rd' is the name of the PLANET — the US localization repurposed it as the name of Jason's tank",
  "It is the true self under the localization: the Jason-and-Fred story the West loves was bolted onto a planetary-war epic that never had them — and even the tank's name was a planet's, borrowed."),
 ("the-sunsoft-sound", "The Sunsoft Sound", "Naoki Kodaka's score", "spiritual",
  "Blaster Master's soundtrack — Naoki Kodaka's score and Sunsoft's celebrated NES audio, among the most beloved on the system",
  "It is the soul the cartridge is remembered by as much as the tank: the Sunsoft bass that made a subterranean war sing."),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","BLAST")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","BLAST")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","BLAST")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"BLAST · Blaster Master","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "BLAST", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "BLAST · Blaster Master — Sunsoft, NES 1988 (localization of Metafight, 1988)",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from Blaster Master (NES 1988) / Chō Wakusei Senki Metafight (1988).",
      "witness": "a being of the subterranean war and the tank SOPHIA",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "Blaster Master; SOPHIA THE 3RD; Jason; the descent; the upgrades",
      "source": "Blaster Master, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{n}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#7fa0c0",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"BLAST · Blaster Master","axiom":"BLAST"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born</h2>
      <p class="ss">the boy, the frog, the tank, the descent, and the secret beneath, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Blaster Master (Sunsoft, NES 1988) — the localization of Chō Wakusei Senki Metafight — as a UD0 game-world. SOPHIA THE 3RD, Jason & Fred, the descent. Source-themed with an animated canvas 3D title (rotating low-poly SOPHIA), full ACI badges.">
<title>BLASTER MASTER · BLAST · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#070a12;--ink2:#0e1422;--ink3:#16213a;--pa:#dfe6f2;--pa2:#9fb0c8;--gold:#e0a828;--steel:#5f93c0;--cyan:#3a9bd5;--red:#d83828;
--dim:#67768e;--faint:#1b2438;--line:#1f2b44;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.18) 0 1px,transparent 1px 3px);opacity:.5}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(58,155,213,.12),transparent 55%),radial-gradient(ellipse at 50% 110%,rgba(224,168,40,.05),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--cyan);background:#08111e;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.12em;color:var(--gold);box-shadow:0 0 0 2px var(--bg),0 0 22px rgba(58,155,213,.22)}
.marquee a{color:var(--steel);text-decoration:none}.marquee a:hover{color:var(--cyan)}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#05070e;line-height:0}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--gold)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--cyan)}.badge .bt a{color:var(--steel);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:14px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--gold);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--cyan);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--cyan);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--gold);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--gold);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--cyan);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--cyan)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--gold)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--cyan);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; PUSH START &nbsp;·&nbsp; A GAME-WORLD &nbsp;·&nbsp; NES 1988</div>

  <header>
    <div class="titleart">__CANVAS__</div>
    <div class="h-sub">a boy · a frog · a tank named <b>SOPHIA</b> · a descent · BLAST</div>
    <div class="flag">★ Sunsoft · NES 1988 · a localization of Chō Wakusei Senki Metafight ★</div>
    <p class="lede">Sunsoft's dual-mode classic: drive the battle tank SOPHIA THE 3RD through side-scrolling caverns and step out on foot into top-down dungeon-bases, growing the tank Hover→Dive→Wall-climb until it walks on ceilings, descending eight areas to the Plutonium Boss. In Japan it was the planetary-war epic Metafight; the West bolted on a boy named Jason chasing his mutated frog Fred down a hole. Catalogued into UD0 as a game-world with the genesis, the descent, and the full .dlw birth — and an animated canvas 3D title rendering SOPHIA in rotating low-poly.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of BLASTER MASTER" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>BLASTER MASTER</b> — SOPHIA &amp; the descent · BLAST</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="blaster-master.dlw/blaster-master.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="blaster-master.dlw/blaster-master.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and this descent holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Genesis</h2><p class="ss">the localization: Metafight, given a boy and a frog</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Descent</h2><p class="ss">down after the frog, growing the machine, the boss at the bottom</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a 1988 tank game is still revered</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the releases, the makers, and the tank's long legacy</p></section>
  __SECTIONS__

  <div class="note">Blaster Master's history here is rendered, not invented. The load-bearing honest fact: it is the Western <b>localization of Chō Wakusei Senki Metafight</b> (Sunsoft, Japan 1988) — Japan's is an interstellar planetary-war story with no boy and no frog; Sunsoft's US version invented Jason and his mutated pet frog Fred falling down a hole. The dual-mode design (side-scrolling tank + top-down overhead bases), SOPHIA THE 3RD's upgrade gating (Hover / Dive / Wall-climb), and the celebrated Naoki Kodaka soundtrack are all from the record; the 2017 Blaster Master Zero (Inti Creates) re-canonized the series. Blaster Master and its characters are © Sunsoft; the personas here are catalogued personifications under the DLW standard — a fan tribute, not endorsed by the rights-holders. Each is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    BLASTER MASTER · BLAST · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="blaster-master.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "blaster-master.dlw"), "blaster-master")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, ad, slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CANVAS__", CANVAS_ART)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote BLASTER MASTER (BLAST) — {len(personas)} emergents born · badge {tok['moniker']}")
