# Projekt Obrazci

## Projektna naloga pri predmetu Osnove podatkovnih baz (Fakulteta za matematiko in fiziko).

Spletna aplikacija je namenjena kreiranju in gostovanju poljubnih spletnih obrazcev (HTML injectable) ter hrambi zbranih odzivov v podatkovni bazi SQL.

## Uporabljene tehnologije

- Python/Django
- PostgreSQL
- [Formio.js](https://github.com/formio/formio.js) form builder & renderer.

# Avtorji
[David Lajevec](https://github.com/davidlajevec), [Luka Skeledžija](https://github.com/lukaske)

# ER diagram podatkovne baze
![alt text](https://github.com/lukaske/the-forms-project-OPB/blob/dev_david/db_diagram.png)

Zgenerira se ga z:
`python manage.py graph_models -a -g -o db_diagram.png`