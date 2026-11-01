"""Génère assets/activity.svg : carte d'activité GitHub autonome (sans service tiers).

Sources : l'API GraphQL de GitHub via la CLI `gh` (identifiant lu dans GITHUB_USER ou celui du dépôt).
Contenu : chiffres des 12 derniers mois, carte de chaleur des contributions, langages des dépôts publics.
Le fichier s'adapte au thème clair ou sombre du lecteur.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from collections import defaultdict
from html import escape
from pathlib import Path

UTILISATEUR = os.environ.get("GITHUB_USER", "Jean-Paul15")
SORTIE = Path(__file__).resolve().parent.parent / "assets" / "activity.svg"

REQUETE = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
    repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 6, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""


def interroger() -> dict:
    resultat = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={REQUETE}", "-F", f"login={UTILISATEUR}"],
        capture_output=True, text=True, check=False,
    )
    if resultat.returncode != 0:
        sys.exit(f"Requête GitHub refusée : {resultat.stderr.strip()[:300]}")
    return json.loads(resultat.stdout)["data"]["user"]


def milliers(n: int) -> str:
    return f"{n:,}".replace(",", " ")


def niveau(compte: int, maximum: int) -> int:
    if compte <= 0 or maximum <= 0:
        return 0
    rapport = compte / maximum
    return 1 if rapport <= 0.25 else 2 if rapport <= 0.5 else 3 if rapport <= 0.75 else 4


def langages(depots: list[dict]) -> list[tuple[str, str, int]]:
    total: dict[str, int] = defaultdict(int)
    couleur: dict[str, str] = {}
    for depot in depots:
        for arete in depot["languages"]["edges"]:
            nom = arete["node"]["name"]
            total[nom] += arete["size"]
            couleur[nom] = arete["node"]["color"] or "#8b949e"
    tries = sorted(total.items(), key=lambda x: x[1], reverse=True)[:6]
    return [(nom, couleur[nom], taille) for nom, taille in tries]


def construire(user: dict) -> str:
    collection = user["contributionsCollection"]
    semaines = collection["contributionCalendar"]["weeks"]
    jours = [j for s in semaines for j in s["contributionDays"]]
    maximum = max((j["contributionCount"] for j in jours), default=0)
    depots = user["repositories"]["nodes"]
    etoiles = sum(d["stargazerCount"] for d in depots)
    langs = langages(depots)
    total_langs = sum(t for _, _, t in langs) or 1

    largeur, marge = 1000, 44
    cellule, pas = 14, 17
    haut_chaleur = 7 * pas

    blocs = [
        ("Contributions", milliers(collection["contributionCalendar"]["totalContributions"])),
        ("Commits", milliers(collection["totalCommitContributions"])),
        ("Pull requests", milliers(collection["totalPullRequestContributions"])),
        ("Dépôts publics", milliers(user["repositories"]["totalCount"])),
        ("Étoiles reçues", milliers(etoiles)),
    ]

    y_stats = 92
    y_chaleur = 150
    y_langs = y_chaleur + haut_chaleur + 48
    hauteur = y_langs + 82

    parts: list[str] = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{largeur}" height="{hauteur}" '
        f'viewBox="0 0 {largeur} {hauteur}" role="img" aria-label="Activité GitHub de {escape(UTILISATEUR)}">'
    )
    parts.append(
        """<style>
  :root { --fond:#ffffff; --bord:#d0d7de; --titre:#0f2027; --texte:#57606a; --accent:#0369a1;
          --c0:#ebedf0; --c1:#bae6fd; --c2:#7dd3fc; --c3:#0ea5e9; --c4:#0369a1; }
  @media (prefers-color-scheme: dark) {
    :root { --fond:#0d1117; --bord:#30363d; --titre:#f0f6fc; --texte:#8b949e; --accent:#38bdf8;
            --c0:#161b22; --c1:#0c4a6e; --c2:#0369a1; --c3:#0ea5e9; --c4:#7dd3fc; }
  }
  text { font-family: 'Segoe UI','Helvetica Neue',Arial,sans-serif; }
  .titre { fill: var(--titre); font-size: 22px; font-weight: 700; }
  .sous { fill: var(--texte); font-size: 13px; }
  .valeur { fill: var(--accent); font-size: 30px; font-weight: 700; }
  .legende { fill: var(--texte); font-size: 13px; }
  .l0{fill:var(--c0)} .l1{fill:var(--c1)} .l2{fill:var(--c2)} .l3{fill:var(--c3)} .l4{fill:var(--c4)}
</style>"""
    )
    parts.append(
        f'<rect x="1" y="1" width="{largeur - 2}" height="{hauteur - 2}" rx="14" fill="var(--fond)" stroke="var(--bord)"/>'
    )
    parts.append(f'<text x="{marge}" y="46" class="titre">Activité des 12 derniers mois</text>')
    parts.append(f'<text x="{marge}" y="68" class="sous">Contributions publiques, mises à jour chaque jour</text>')

    colonne = (largeur - 2 * marge) / len(blocs)
    for i, (libelle, valeur) in enumerate(blocs):
        x = marge + i * colonne
        parts.append(f'<text x="{x:.0f}" y="{y_stats + 22}" class="valeur">{escape(valeur)}</text>')
        parts.append(f'<text x="{x:.0f}" y="{y_stats + 42}" class="legende">{escape(libelle)}</text>')

    for ci, semaine in enumerate(semaines):
        for ji, jour in enumerate(semaine["contributionDays"]):
            x = marge + ci * pas
            y = y_chaleur + ji * pas
            n = niveau(jour["contributionCount"], maximum)
            parts.append(
                f'<rect x="{x}" y="{y}" width="{cellule}" height="{cellule}" rx="3" class="l{n}">'
                f'<title>{jour["date"]} : {jour["contributionCount"]}</title></rect>'
            )

    parts.append(f'<text x="{marge}" y="{y_langs - 14}" class="titre" style="font-size:16px">Langages</text>')
    x = float(marge)
    zone = largeur - 2 * marge
    for nom, couleur, taille in langs:
        part = zone * taille / total_langs
        parts.append(f'<rect x="{x:.1f}" y="{y_langs}" width="{part:.1f}" height="10" fill="{escape(couleur)}"/>')
        x += part
    parts.append(f'<rect x="{marge}" y="{y_langs}" width="{zone}" height="10" rx="5" fill="none" stroke="var(--bord)"/>')
    xl = float(marge)
    for nom, couleur, taille in langs:
        pct = 100 * taille / total_langs
        parts.append(f'<circle cx="{xl + 5:.0f}" cy="{y_langs + 34}" r="5" fill="{escape(couleur)}"/>')
        etiquette = f"{nom} {pct:.0f} %"
        parts.append(f'<text x="{xl + 16:.0f}" y="{y_langs + 39}" class="legende">{escape(etiquette)}</text>')
        xl += 30 + 8.2 * len(etiquette)

    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    user = interroger()
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(construire(user), encoding="utf-8")
    print(f"Écrit : {SORTIE}")


if __name__ == "__main__":
    main()
