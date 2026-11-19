# TrustNet

**Rețea de încredere multidimensională bazată pe colaborări**  
Proiect de analiză și modelare software — [AMSS 2026/2027](https://traiansf.github.io/class/amss2026/), Facultatea de Matematică și Informatică, Universitatea din București.

## Despre proiect

TrustNet propune un sistem de reputație în care actori identificabili — persoane, echipe, organizații sau agenți AI — înregistrează acorduri voluntare și își pot evalua reciproc caracteristicile și competențele utilizate în colaborare. Evaluările contribuie la reputația multidimensională a actorilor și sunt luate în calcul doar în perioada de relevanță stabilită.

Acordurile pot fi înregistrate direct de participanți sau transmise de platforme partenere, cu acceptarea verificabilă a participanților. TrustNet urmărește evidența acordurilor necesară evaluărilor, nu conținutul sau îndeplinirea obligațiilor contractuale. Sistemul este gândit și pentru integrarea ca serviciu extern în alte platforme.

**Scopul academic:** specificarea, modelarea și justificarea unei soluții de proiectare.

## Documentație

- [Sinteza dosarului de proiectare](SINTEZA.md) — vedere de ansamblu, generată automat din contribuții.
- [Dosarul contribuțiilor](dosar/) — analizele, modelele, scenariile și verificările individuale.
- [Model pentru contribuții](dosar/model_contributie.md) — structura Markdown folosită de echipă.
- [Idei arhitecturale inițiale (pagină interactivă)](https://olympians-amss.github.io/TrustNet/TrustNet.html) — diagrame și simulări; conține și opțiuni încă în discuție.
- [Cerințele proiectului AMSS](https://traiansf.github.io/class/amss2026/proiect/).

## Organizare și progres

- [Discussions](https://github.com/Olympians-AMSS/TrustNet/discussions) — clarificări, alternative și acorduri în echipă, înainte de finalizarea contribuțiilor.
- [Issues](https://github.com/Olympians-AMSS/TrustNet/issues) — responsabilități și sarcini.
- [Projects](https://github.com/Olympians-AMSS/TrustNet/projects) — planificarea lucrului, dacă este utilizată.
- [Istoricul modificărilor](https://github.com/Olympians-AMSS/TrustNet/commits/main/) — evoluția documentației.

### Structura documentației

```text
TrustNet/
├── README.md
├── TrustNet.html
├── SINTEZA.md
├── dosar/
│   ├── model_contributie.md
│   └── ...                  # contribuțiile membrilor, fișiere .md
├── scripts/
│   └── generate_sinteza.py
└── .github/workflows/
    └── sinteza.yml
```

**Fluxul de lucru:** discutăm în Discussions → responsabilul completează fișierul propriu din `dosar/` → fragmentul delimitat de `<!-- SINTEZA:START -->` și `<!-- SINTEZA:END -->` este preluat automat în `SINTEZA.md`. Fiecare contribuție indică autorul și poate include justificări, scenarii și verificări.

## Echipa

- [Condruz Filip Gabriel](https://github.com/CondruzFilipGabriel)
- [Schilizzi Filippos](https://github.com/filippos855)
- [Stăncioiu Adrian Florian](https://github.com/adi4pk)
- [Petcu Andreea Elena](https://github.com/AAAMON)
- [Iorga Iustin Nicolae](https://github.com/Uniror)

## Licență

**În curs de alegere de către echipă.** Este propusă [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0): permite utilizarea, modificarea și distribuirea, inclusiv comercială, cu păstrarea notificărilor de drepturi de autor și a condițiilor de atribuire aplicabile. Până la adoptarea licenței și adăugarea fișierului `LICENSE`, publicarea în repository nu echivalează cu acordarea unei licențe open-source.
