# skifer-snowflake

> Connecteur **Snowflake** pour [Skifer](https://github.com/morzu117/skifer), le framework déclaratif de pipelines Bronze → Silver → Gold.

**État : deuxième jalon, **pas commencé**. Le nom est réservé ; le travail démarre quand la tranche DuckDB aura prouvé l'architecture SQL-first du cœur. Snowflake éprouvera ce que DuckDB ne teste pas : permissions distantes, jobs asynchrones, sémantique d'un entrepôt cloud.**

## Rôle

Skifer compile un pipeline YAML en SQL une seule fois, dans son cœur. Un connecteur ne fait que
brancher ce SQL sur une plateforme. Il implémente les trois contrats du cœur, et rien d'autre :

| Contrat | Ce que le connecteur fournit |
|---|---|
| Exécution | Soumettre un SQL, lire un résultat borné |
| Catalogue | Résoudre et décrire les relations |
| Publication | Créer ou remplacer une table ou une vue, avec les règles d'atomicité et de droits de la plateforme dites explicitement |

Ce qu'un connecteur **ne contient jamais** : de logique métier, un dispatch d'opérations par
plateforme, une méthode `filter` / `join` / `with_column`. La portabilité est déclarée opération
par opération dans la matrice de capacités du cœur, et prouvée par des tests de parité exécutés sur
le vrai moteur, jamais par le seul SQL généré.

## Installation

```bash
pip install skifer-snowflake          # tire skifer et Snowflake
pip install -e ".[dev]"    # développement : pytest + ruff
```

La dépendance au cœur est aujourd'hui `skifer` ; elle deviendra `skifer-core` quand cette
distribution sera publiée, sans autre changement ici.

## Développement

```bash
pytest -q && ruff check src/ tests/
```

Toute modification de `src/` s'accompagne d'un test et d'une entrée dans `CHANGELOG.md` sous
`[Unreleased]`. La version est gérée par le mainteneur, jamais par un agent.

## Écosystème

- [skifer](https://github.com/morzu117/skifer) — cœur, couche gouvernée, connecteur Spark/Databricks
- [skifer-atlas](https://github.com/morzu117/skifer-atlas) — carte canonique des KPI
- [skifer-board](https://github.com/morzu117/skifer-board) — BI self-service

## Licence

MIT — voir [LICENSE](LICENSE).
