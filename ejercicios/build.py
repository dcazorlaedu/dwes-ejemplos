#!/usr/bin/env python3
"""Genera el índice público y una página (y README) por ejercicio a partir de ejercicios.json."""
import html, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "ejercicios.json").read_text(encoding="utf-8"))
UNIDADES, EJERCICIOS = DATA["unidad"], DATA["ejercicios"]
RA_TEXTO, CE_ESPERADOS = DATA["ra_texto"], DATA["ce_esperados"]


def esc(v):
    return html.escape(str(v), quote=True)


def md(v):
    """Convierte `código` en <code> tras escapar el HTML."""
    out, partes = "", esc(v).split("`")
    for i, p in enumerate(partes):
        out += f"<code>{p}</code>" if i % 2 else p
    return out


def ce_text(ce):
    return ", ".join(f"{c.split(':')[0]} {c.split(':')[1]})" for c in sorted(ce))


def validar():
    if len(EJERCICIOS) != 20:
        raise ValueError(f"Se esperaban 20 ejercicios; hay {len(EJERCICIOS)}")
    for n, e in enumerate(EJERCICIOS, 1):
        if e["id"] != f"{n:02d}_ejercicio_UT{e['ut']}":
            raise ValueError("Numeración o nombre incorrectos: " + e["id"])
    for ut, info in UNIDADES.items():
        niveles = [e["dificultad"] for e in EJERCICIOS if e["ut"] == int(ut)]
        if not niveles or niveles != sorted(niveles):
            raise ValueError(f"UT{ut}: ejercicios ausentes o no ordenados por dificultad")
        for ra in info["ra"]:
            cubiertos = {c.split(":")[1] for e in EJERCICIOS if e["ut"] == int(ut) for c in e["ce"] if c.startswith(ra + ":")}
            if cubiertos != set(CE_ESPERADOS[ra]):
                raise ValueError(f"UT{ut} {ra}: faltan {sorted(set(CE_ESPERADOS[ra]) - cubiertos)}")


def header(title, pref, active=""):
    uts = "".join(f'<a href="{pref}ut{n}/">UT{n}</a>' for n in range(1, 8))
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · DWES</title><link rel="icon" href="{pref}assets/favicon.svg"><link rel="stylesheet" href="{pref}assets/site.css"></head><body>
<header class="top"><div class="in"><a class="logo" href="{pref}">&lt;/&gt; DWES</a>
<nav>{uts}<a href="{pref}lab/">Laboratorio PHP</a><a href="{pref}demos/">Demos JS</a><a href="{pref}docker/">Docker</a><a href="{pref}ejercicios/" class="{active}">Ejercicios</a></nav></div></header>"""


def listing():
    p = header("Batería de ejercicios", "../", "on")
    p += """<div class="hero"><div class="in"><div class="badge">DWES · 2.º DAW</div><h1>20 ejercicios por UT</h1>
<p>Una secuencia progresiva, de lo básico a proyectos integrados. Cada unidad trabaja todos sus RA y todos sus criterios de evaluación.</p>
<p><a class="btn" href="#lista">Ver ejercicios</a> <a class="btn sec" href="material/LEEME.md">Preparar el entorno (Docker + DataGrip)</a></p></div></div>
<main><div class="tip"><strong>Cómo usar la batería.</strong> Los ejercicios van por unidad y, dentro de cada una, por dificultad creciente. Las PHP se ejecutan siempre desde el navegador (<code>http://localhost:8080</code>) con el entorno Docker del material y la base de datos se consulta también desde DataGrip. No hay soluciones públicas: cada ejercicio incluye <em>criterios de aceptación</em> observables para que compruebes tu trabajo.</div>
<label for="unidad"><strong>Filtrar por unidad</strong></label> <select id="unidad" style="width:auto"><option value="">Todas</option>"""
    for ut, i in UNIDADES.items():
        p += f'<option value="{ut}">UT{ut} · {" + ".join(i["ra"])} · {sum(e["ut"]==int(ut) for e in EJERCICIOS)} ejercicios</option>'
    p += '</select><h2 id="lista">Ejercicios</h2><div class="grid">'
    for e in EJERCICIOS:
        i = UNIDADES[str(e["ut"])]
        p += f"""<a class="card ejercicio" data-ut="{e['ut']}" href="{esc(e['id'])}/"><div class="ra">{esc(e['id'])} · {esc(' + '.join(i['ra']))} · Nivel {e['dificultad']}</div>
<h3>{esc(e['titulo'])}</h3><p>{esc(e['contexto'][:170])}…</p><p><strong>CE:</strong> {esc(ce_text(e['ce']))}</p></a>"""
    p += "</div><h2>Cobertura curricular</h2><div class=\"cols\">"
    for ut, i in UNIDADES.items():
        for ra in i["ra"]:
            ces = sorted({c.split(":")[1] for e in EJERCICIOS if e["ut"] == int(ut) for c in e["ce"] if c.startswith(ra + ":")})
            p += f'<div class="tip"><strong>UT{ut} · {ra}</strong><br><small>{esc(RA_TEXTO[ra])}</small><br>Criterios cubiertos: {", ".join(c + ")" for c in ces)}</div>'
    p += """</div><h2>Material de prácticas</h2><p><a href="material/LEEME.md">Guía del entorno</a> · <a href="material/docker-compose.yml">docker-compose.yml</a> · <a href="material/db/init/schema.sql">Base de datos TiendaTech</a> · <a href="material/db/init/02_club.sql">Rutas y reservas del club</a> · <a href="material/ventas_demo.csv">ventas_demo.csv</a>. Todos los datos son ficticios; usa siempre bases de datos de pruebas.</p></main>
<footer>Material didáctico · 2026-27 · Ejercicios sin soluciones públicas; datos ficticios.</footer>
<script>const u=document.getElementById('unidad'),q=new URLSearchParams(location.search);u.value=q.get('ut')||'';
function f(){document.querySelectorAll('.ejercicio').forEach(e=>e.hidden=!!u.value&&e.dataset.ut!==u.value)}u.onchange=()=>{f();history.replaceState(null,'',u.value?'?ut='+u.value:location.pathname)};f();</script></body></html>"""
    return p


def pagina(e):
    ut, i = e["ut"], UNIDADES[str(e["ut"])]
    maxn = max(x["dificultad"] for x in EJERCICIOS if x["ut"] == ut)
    ras = " + ".join(i["ra"])
    p = header(e["titulo"], "../../")
    p += f"""<div class="hero"><div class="in"><div class="badge">{esc(e['id'])} · UT{ut} · {esc(ras)}</div><h1>{esc(e['titulo'])}</h1><p>Nivel {e['dificultad']} de {maxn} · {esc(i['nombre'])}</p></div></div>
<main><div class="crumb"><a href="../">Batería de ejercicios</a> › <a href="../../ut{ut}/">UT{ut}</a> › {esc(e['id'])}</div>
<div class="tip">""" + "<br>".join(f"<strong>{ra}:</strong> {esc(RA_TEXTO[ra])}" for ra in i["ra"]) + f"<br><strong>Criterios trabajados:</strong> {esc(ce_text(e['ce']))}</div>"
    p += f"<h2>Situación</h2><p>{md(e['contexto'])}</p><h2>Enunciado</h2><ol>" + "".join(f"<li>{md(t)}</li>" for t in e["tareas"]) + f"</ol><h2>Entrega</h2><p>{md(e['entrega'])}</p>"
    p += "<h2>Criterios de aceptación (compruébalos tú)</h2><ul>" + "".join(f"<li>{md(a)}</li>" for a in e["aceptacion"]) + "</ul>"
    if e.get("ampliacion"):
        p += "<h2>Ampliación (opcional, no evaluable)</h2><ul>" + "".join(f"<li>{md(a)}</li>" for a in e["ampliacion"]) + "</ul>"
    p += f"""<div class="tip"><strong>Pista:</strong> {md(e['pista'])}</div>
<h2>Material y entorno</h2><p><a href="../material/LEEME.md">Guía de Docker + DataGrip</a> · <a href="../material/docker-compose.yml">docker-compose.yml</a>. Guarda tus páginas en <code>src/</code> y ábrelas en <code>http://localhost:8080</code>. La base de datos <code>tienda</code> está también en DataGrip (<code>localhost:3306</code>, usuario <code>dwes</code>).</p>
</main><footer>Material didáctico · 2026-27 · Datos ficticios · Sin soluciones públicas.</footer></body></html>"""
    return p


def readme(e):
    i = UNIDADES[str(e["ut"])]
    t = "\n".join(f"{n}. {x}" for n, x in enumerate(e["tareas"], 1))
    a = "\n".join(f"- {x}" for x in e["aceptacion"])
    amp = ("\n## Ampliación (opcional, no evaluable)\n\n" + "\n".join(f"- {x}" for x in e["ampliacion"]) + "\n") if e.get("ampliacion") else ""
    ras = "\n".join(f"**{ra}:** {RA_TEXTO[ra]}" for ra in i["ra"])
    return f"""# {e['id']} · {e['titulo']}

**UT{e['ut']} · {' + '.join(i['ra'])} · Nivel {e['dificultad']}** — {i['nombre']}

{ras}

**Criterios trabajados:** {ce_text(e['ce'])}

## Situación

{e['contexto']}

## Enunciado

{t}

## Entrega

{e['entrega']}

## Criterios de aceptación (compruébalos tú)

{a}
{amp}
## Pista

{e['pista']}

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/{e['id']}/)
"""


def main():
    validar()
    (ROOT / "index.html").write_text(listing(), encoding="utf-8")
    for e in EJERCICIOS:
        d = ROOT / e["id"]; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(pagina(e), encoding="utf-8")
        (d / "README.md").write_text(readme(e), encoding="utf-8")
    print(f"Generados {len(EJERCICIOS)} ejercicios en 7 UT.")


if __name__ == "__main__":
    main()
