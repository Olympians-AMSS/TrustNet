# Specificații TrustNet

**Autor:** Condruz Filip - Gabriel  
**Discuție:** [Specificatie — GitHub Discussions #2](https://github.com/Olympians-AMSS/TrustNet/discussions/2)  
**Status:** În lucru — propunere pentru echipă

<!-- SINTEZA:START -->
## Specificații — TrustNet

TrustNet este un serviciu independent de reputație multidimensională, reutilizabilă între platforme. Reputația se bazează pe evaluări voluntare între participanții unor acorduri confirmate. Sistemul nu verifică executarea contractelor, nu arbitrează opiniile evaluatorilor și nu păstrează documentele contractuale.

- Acordurile sunt imuabile, semnate de toți participanții și anulabile numai prin unanimitate. Dreptul de evaluare durează 24 de luni de la confirmarea acordului.
- Doar actorii cu identitate verificată extern pot evalua; agenții AI au reputație proprie și pot fi evaluați, dar nu pot evalua.
- Pentru fiecare pereche evaluator–evaluat și caracteristică există o singură notă curentă, între 1 și 10, valabilă 24 de luni de la emitere.
- Reputația publică afișează, pe fiecare caracteristică sau competență, **mediana** și **numărul evaluatorilor**, fără prag minim și fără scor general. Acordurile și evaluările individuale rămân private.
- Sunt prevăzute integrarea cu platforme externe, API public de reputație, istoric privat pentru restaurarea evaluărilor și măsuri împotriva fraudelor.
<!-- SINTEZA:END -->

## Analiza și contribuția completă

### Idei, reguli și decizii

#### Problema, beneficiarii și limitele

Reputația rezultată din colaborări este de regulă dependentă de platforma care o colectează sau redusă la un scor global. TrustNet urmărește o reputație **independentă de platformă**, exprimată separat pentru calități generale și competențe profesionale.

Beneficiarii sunt persoane, echipe, societăți, ONG-uri, instituții, agenți AI și platforme care doresc să consulte sau să integreze reputația. Un actor își poate folosi identitatea TrustNet în mai multe contexte de colaborare.

**În afara scopului:** negocierea și executarea contractelor, intermedierea plăților, verificarea prestațiilor profesionale, soluționarea litigiilor contractuale, certificarea adevărului evaluărilor, verificarea directă a identității reale de către TrustNet și arhivarea documentelor contractuale. Specificația nu prescrie arhitectura sau tehnologiile de implementare.

#### Cerințe funcționale

**Identitate și conturi**

- **RF-01.** TrustNet identifică distinct fiecare actor (persoană, echipă, organizație sau agent AI), cu reputație proprie, independentă de platformele externe. Aceeași identitate reală verificată trebuie asociată unui singur actor TrustNet, inclusiv între furnizori de identitate diferiți.
- **RF-02.** Autentificarea și verificarea identității sunt distincte. Verificarea identității este furnizată exclusiv de parteneri externi acceptați individual de TrustNet; fiecare actor are un singur furnizor activ. Profilul indică public dacă identitatea este verificată.
- **RF-03.** Orice cont poate participa la acorduri și poate primi evaluări. Numai actorii cu identitate verificată pot emite evaluări; agenții AI nu pot emite evaluări, indiferent de statutul lor.
- **RF-04.** Dacă verificarea expiră, este revocată sau furnizorul nu mai este acceptat, actorul își pierde temporar dreptul de evaluare, iar ratingurile emise sunt excluse din statistici fără a fi șterse. Reverificarea poate reactiva numai ratingurile încă valabile. Frauda de identitate confirmată invalidează definitiv ratingurile emise sub verificarea frauduloasă.
- **RF-05.** Schimbarea datelor de identificare păstrează contul și reputația dacă furnizorul confirmă continuitatea identității. Conturile duplicate sunt suspendate; actorul păstrează unul singur, iar evaluările emise și primite prin conturile eliminate sunt șterse, fără transfer.
- **RF-06.** Dezactivarea contului oprește participarea la operațiuni noi și afișarea reputației sale, dar nu șterge automat ratingurile acordate altora, care își păstrează valabilitatea, sub rezerva obligațiilor legale.
- **RF-07.** Agentul AI are identitate și reputație distincte de ale operatorului verificat care îl administrează. Identificatorul public al operatorului este afișat în profilul agentului. Operatorul autorizează acordurile în numele agentului; schimbarea operatorului nu modifică reputația sau acordurile agentului.
- **RF-08.** Identificatorul TrustNet, tipul actorului și statutul verificării sunt publice; publicarea numelui real sau a denumirii este opțională. Datele private furnizate pentru verificarea identității nu sunt publice.

**Acorduri și autorizarea evaluărilor**

- **RF-09.** Orice cont poate propune un acord bilateral sau multilateral, direct ori printr-o platformă parteneră. Acordul este înregistrat numai după confirmarea autentică a tuturor participanților.
- **RF-10.** Confirmarea acordului se face prin semnături criptografice distincte, asociate identităților TrustNet, asupra acelorași date ale acordului și a amprentei documentului contractual. TrustNet verifică autenticitatea semnăturilor și integritatea datelor, fără a stoca sau interpreta contractul.
- **RF-11.** TrustNet administrează cheile de semnare ale conturilor, folosind o cheie distinctă pentru fiecare actor și acord, derivată din secretul principal al actorului. Utilizatorul autentificat autorizează explicit semnarea, fără reautentificare obligatorie la fiecare semnătură; o platformă parteneră nu poate semna autonom în numele său.
- **RF-12.** După înregistrare, acordul și lista sa de competențe sunt imuabile. Anularea este posibilă numai cu acceptarea unanimă a tuturor participanților, inclusiv când un cont devine inaccesibil. Anularea încetează drepturile de evaluare și invalidează ratingurile bazate pe acordul respectiv.
- **RF-13.** Orice participant eligibil poate evalua orice alt participant din acord, fără obligația de a evalua și fără condiția unei interacțiuni directe. Autoevaluarea este interzisă. Evaluarea este permisă din momentul confirmării acordului, inclusiv înainte de finalizarea colaborării, timp de **24 de luni** de la confirmare.
- **RF-14.** Competențele evaluabile sunt fixate în acord și trebuie să existe în catalogul aprobat înainte de semnare. Caracteristicile generale pot fi evaluate în orice acord. Pentru competențe suplimentare este necesar un acord nou, nu modificarea celui existent.
- **RF-15.** TrustNet păstrează numai informațiile minimale necesare pentru acordurile care justifică ratinguri active ori încă restaurabile. Dovezile care nu mai justifică evaluări sunt eliminate; nu se păstrează un istoric contractual permanent.

**Evaluări și reputație**

- **RF-16.** Caracteristicile generale sunt respectarea angajamentelor, promptitudinea, comunicarea și flexibilitatea. Calitatea muncii se evaluează separat pentru fiecare competență specifică din acord. Toate dimensiunile sunt opționale; o caracteristică neevaluată nu primește notă implicită.
- **RF-17.** Fiecare rating este un număr **întreg între 1 și 10**. Pentru aceeași combinație evaluator → evaluat → caracteristică/competență există cel mult **un rating curent**, indiferent de numărul acordurilor dintre actori.
- **RF-18.** Evaluatorul poate modifica sau retrage un rating numai cât timp deține un drept de evaluare valabil. Nota nouă înlocuiește nota curentă; actualizarea reputației este imediată. Fiecare rating este relevant timp de **24 de luni de la emiterea sa**, separat de durata dreptului de evaluare.
- **RF-19.** TrustNet păstrează timp de 24 de luni istoricul privat al creării, modificării, retragerii și restaurării evaluărilor: evaluator, evaluat, caracteristică, valoare, dată, tipul operațiunii și dovada autorizării. Evaluatorul îl consultă în regim read-only; administratorii autorizați îl pot consulta pentru securitate. Istoricul nu multiplică influența unui evaluator asupra reputației.
- **RF-20.** După recuperarea accesului, un evaluator poate restaura o versiune anterioară din istoric. Restaurarea produce o operațiune nouă de audit, păstrează data emiterii originale și nu prelungește relevanța notei; nu reînvie ratinguri expirate sau invalidate definitiv.
- **RF-21.** Dacă acordul care justifică ratingul curent este anulat, TrustNet reactivează automat cea mai recentă evaluare anterioară **încă validă și justificată printr-un alt acord neanulat**. În lipsa uneia eligibile, ratingul curent dispare.
- **RF-22.** Catalogul de competențe este centralizat, fără ierarhie. Actorii pot propune competențe noi, utilizabile numai după aprobare. Competențele echivalente pot fi unificate; în cazul mai multor ratinguri ale aceluiași evaluator pentru competența rezultată se păstrează cel mai recent, fără modificarea acordurilor semnate.
- **RF-23.** Reputația este exclusiv multidimensională: pentru fiecare caracteristică sau competență se publică **mediana ratingurilor eligibile** și **numărul evaluatorilor distincți**, cu ponderi egale și fără prag minim. Pentru un număr par, mediana este media aritmetică a celor două note centrale. În absența evaluărilor valide apare „Neevaluat”. Nu există scor general.
- **RF-24.** Reputația este vizibilă public inclusiv fără autentificare. Ratingurile individuale și identitatea evaluatorilor nu sunt vizibile nici publicului, nici actorului evaluat. Acordurile și relațiile dintre participanți sunt private. Actorul nu poate ascunde selectiv competențe cu ratinguri valide.
- **RF-25.** Toți actorii activi sunt incluși în căutarea publică după identificator, nume public sau competențe, cu filtrare după mediană și număr de evaluatori, fără clasament general. Conturile dezactivate nu sunt afișate.

**Interoperabilitate, securitate și administrare**

- **RF-26.** Reputația și căutarea sunt accesibile prin API public, gratuit și fără autentificare, exclusiv cu date publice. Sistemul limitează automat frecvența cererilor și răspunde explicit la depășirea limitelor.
- **RF-27.** Platformele partenere se identifică separat și pot acționa în numele utilizatorilor doar cu permisiuni explicite, limitate și revocabile. Revocarea oprește operațiunile viitoare, fără să anuleze acorduri sau ratinguri deja confirmate.
- **RF-28.** Retrimiterea aceleiași solicitări după întreruperea serviciului nu trebuie să producă operațiuni duplicate. La conflictele concurente pentru același rating, modificarea directă în TrustNet prevalează asupra celei delegate; pentru operațiuni de aceeași prioritate prevalează ultima procesată.
- **RF-29.** Notificările sunt disponibile în aplicație și prin e-mail; notificările critice de securitate nu pot fi dezactivate, iar cele neesențiale sunt configurabile.
- **RF-30.** Dacă o cheie de acord este compromisă, acordul afectat este suspendat până la reconfirmare. Dacă secretul principal este compromis, dreptul de evaluare este suspendat temporar până la recuperarea securizată a accesului; acordurile și ratingurile anterioare nu sunt invalidate automat. Utilizatorul este notificat și își poate verifica și corecta istoricul, fără blocarea activității după recuperare.
- **RF-31.** Recuperarea unui cont inaccesibil este permisă prin reverificarea identității la un furnizor acceptat și resetarea credențialelor. Pierderea accesului, în sine, nu anulează ratingurile emise anterior.
- **RF-32.** Orice utilizator autentificat poate semnala suspiciuni de fraudă. Administratorii pot suspenda preventiv ratinguri și le pot invalida definitiv numai pe baza dovezilor de fraudă sau încălcare a regulilor TrustNet, nu pentru că apreciază diferit calitatea unei prestații.
- **RF-33.** Actorii afectați pot solicita reexaminarea unei măsuri administrative. Contestația nu suspendă măsura; în cazul revocării deciziei, ratingurile neexpirate sunt restabilite cu data inițială. Accesul administrativ la istoricul privat și deciziile administrative sunt înregistrate.

#### Cerințe nefuncționale

- **RNF-01 — Confidențialitate:** numai persoanele autorizate pot accesa acordurile, evaluările individuale și istoricul privat; informațiile expuse public sunt limitate la cele declarate publice.
- **RNF-02 — Securitate:** semnarea, evaluarea, delegarea și intervențiile administrative necesită autentificare și autorizare; cheile private și datele de verificare a identității trebuie protejate.
- **RNF-03 — Integritate:** operațiunile confirmate și istoricul lor sunt protejate prin controlul accesului; utilizatorii nu pot rescrie istoricul. Nu se impune jurnal criptografic pentru audit.
- **RNF-04 — Persistență:** datele confirmate se păstrează durabil, iar serviciul trebuie să permită recuperarea după incidente din copii de siguranță, fără a prescrie soluția tehnică.
- **RNF-05 — Consistență:** calculele reputației, expirarea evaluărilor și retrimiterea cererilor trebuie să ofere rezultate consecvente cu regulile funcționale, inclusiv la operațiuni concurente.
- **RNF-06 — Protecția datelor:** colectarea și retenția datelor trebuie limitate la scopurile declarate și la obligațiile legale; posibilitatea de a deduce unele note din statistici cu puțini evaluatori nu reprezintă anonimitate garantată.

### Justificări și alternative

- Reputația separată pe competențe evită reducerea unor aptitudini diferite la un singur scor. **Mediana**, propusă în locul mediei aritmetice, reduce influența valorilor extreme individuale, dar nu previne evaluările coordonate; alegerea trebuie validată de echipă.
- Lipsa pragului minim păstrează vizibilitatea evaluărilor provenite din colaborări rare sau de lungă durată. Compromisul este posibilitatea deducerii unei note când există puțini evaluatori.
- Un singur rating curent per evaluator și caracteristică previne multiplicarea influenței prin acorduri repetate; istoricul limitat permite corectarea operațiunilor neautorizate și restaurarea unor note anterioare încă valide.

### Scenarii, verificări și limite

*Exemple de acceptare pentru cerințele de mai sus; verificarea detaliată a modelelor și comportamentelor aparține contribuțiilor dedicate.*

| Exemplu | Rezultat așteptat |
|---|---|
| Un actor neverificat participă la un acord și încearcă să evalueze. | Poate semna și primi ratinguri; emiterea ratingului este respinsă. |
| Patru evaluatori acordă notele `1, 7, 8, 10` aceleiași competențe. | Mediana publică este `7,5`, cu `4` evaluatori. |
| Există un singur rating valid, cu nota `3`. | Sunt afișate `3` și `1 evaluator`, fără prag minim. |
| Un evaluator actualizează o notă printr-un alt acord valabil. | Noua notă este singura contribuție curentă a sa pentru caracteristica respectivă. |
| Acordul asociat ratingului curent este anulat unanim; o notă anterioară este încă validă și susținută de alt acord. | Este reactivată nota anterioară, cu data și termenul originale. |
| Un agent AI își schimbă operatorul. | Identitatea, acordurile și reputația agentului rămân neschimbate. |
| O solicitare confirmată este retransmisă după o întrerupere. | Operațiunea nu se execută a doua oară. |

### Întrebări rămase deschise

- **Acordurile fără document extern:** care este documentul a cărui amprentă se semnează când acordul este creat integral în TrustNet? Cerința RF-10 nu presupune încă o soluție.
- **Identități între furnizori:** cum poate fi garantată unicitatea unei identități reale verificate de furnizori independenți, fără colectare excesivă de date personale? Cerința RF-01 rămâne ținta funcțională.
- **Aspecte pentru proiectare:** reprezentarea exactă a datelor semnate, gestionarea și revocarea cheilor, precum și delimitarea operațiunilor concurente sunt de precizat în contribuțiile de proiectare, fără schimbarea comportamentului cerut aici.

## Referințe (opțional)

- [Issue #3 — Crearea specificațiilor](https://github.com/Olympians-AMSS/TrustNet/issues/3)
- [GitHub Discussions #2 — Specificatie](https://github.com/Olympians-AMSS/TrustNet/discussions/2)
- [TrustNet.html — prezentarea inițială](https://olympians-amss.github.io/TrustNet/TrustNet.html)
- [AMSS 2026/2027 — cerințe proiect](https://traiansf.github.io/class/amss2026/proiect/)
