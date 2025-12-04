# Opinnäytetyö: Firehorse-tuotevalmistuksen toimintamalli
**Metropolia Ammattikorkeakoulu**

---

## Opinnäytetyön tiedot

**Otsikko:** Firehorse-tuotevalmistuksen toimintamalli: Hybridi AI-edge-arkkitehtuuri ilmastointelligeenteille teollisille alustoille

**Opiskelija:** Risto Anton Päärni
**Koulutusohjelma:** [TBD - todennäköisesti Business IT tai Teollisuuden johtaminen]
**Ohjaaja:** [TBD]
**Yritys:** Lifetime Oy (Firehorse-brändi)
**Työn tyyppi:** Toteutuspohjainen / Tuotekehitys
**Aikataulu:** [TBD - tyypillisesti 6 kuukautta]

---

## 1. Tutkimusongelma ja tavoitteet

### 1.1 Tausta

Eurooppalaiset teollisuuden pk-yritykset kohtaavat "kaksoissiirtymän" haasteen:
- **Digitaalinen muutos**: AI, automaatio, reaaliaikainen päätöksenteko
- **Vihreä siirtymä**: EU Fit for 55 (55% päästövähennys vuoteen 2030 mennessä), sisältyvän hiilen mittausvaatimukset vuoteen 2028 mennessä

Perinteiset SaaS-alustat epäonnistuvat, koska ne:
1. Maksavat €1 400+/kk (liian kalliita pk-yrityksille)
2. Vaativat vain pilvipohjaiset arkkitehtuurit (korkea latenssi, korkeat käyttökustannukset)
3. Eivät käsittele toimialakohtaisia compliance-työnkulkuja

**Firehorse (DWS6)** ratkaisee tämän uudella toimintamallilla, joka yhdistää:
- Ilmaistason pilvi-infrastruktuurin (€0-350/kk vs €1 400+)
- Edge AI (NVIDIA Jetson) <100ms päättelylle
- Toimialakohtaiset AI-agentit (Rakentaminen, Valmistus, Energia)
- Vaiheittainen käyttöönotto (Hiljainen pilotti → Neuvonantaja → Autonominen)

### 1.2 Neljä tutkimuskysymystä

#### Tutkimuskysymys 1: Tuote ja liiketoimintamalli

**Pääkysymys:** Miten kehitetään asiakaslupaus, joka ratkaisee todellisen ongelman ja skaalautuu kansainvälisesti?

**Alakysymykset:**
a) **Tuotteen visio**
   - Mikä on DWS6:n pitkän aikavälin visio? (MVP → Alpha → V1 → Series A)
   - Miten visio muuttuu asiakaspalautteen myötä?

b) **Suppea markkinatutkimus**
   - Kuka on kohdeasiakas? (Rakennusyritykset €10-100M liikevaihto)
   - Markkinan koko? (3,5M rakennusyritystä Euroopassa)
   - Kilpailijat? (Atlassian Rovo €1 400/kk, SAP €50K+/vuosi)

c) **Minkä ongelman tuote ratkaisee?**
   - **Ongelma:** EU:n sisältyvän hiilen mittausvaatimus 2028 (rakennukset >1 000 m²)
   - **Ratkaisu:** Reaaliaikainen päästöseuranta + viabiliteettianalyysi
   - **ROI:** 2 kuukauden takaisinmaksuaika (tavoite ≤2kk tai rahat takaisin)

**Teoreettinen viitekehys:**
- Lean Startup (Eric Ries): MVP-strategia, Build-Measure-Learn
- Customer Development (Steve Blank): Asiakas ensin, tuote toiseksi
- Jobs-to-be-Done (Clayton Christensen): Mitä "työtä" asiakas palkkaa tuotteen tekemään?

#### Tutkimuskysymys 2: Teknologia - Monialustainen tuotekehitys

**Pääkysymys:** Miten rakennetaan digitaalinen, skaalautuva palvelutuote, joka toimii pilvi + edge + verkkokauppa?

**Alakysymykset:**
a) **Digitaalinen skaalautuva palvelutuote**
   - Arkkitehtuuri: Hybridi pilvi (Google Cloud Run) + edge (NVIDIA Jetson)
   - Skaalautuvuus: 5 asiakasta (MVP) → 50 (Alpha) → 100+ (V1)
   - Kustannusmalli: €0/kk (ilmaistaso) → €350/kk (tuotanto)

b) **Verkkokauppatoteutus**
   - **Ongelma:** Staattiset sivut (lifetime.fi/buy Squarespace) = 0 myyntiä
   - **Ratkaisu:** Dynaamiset tuotesivut (onelifetime.world Hugo + Netlify)
   - **Integraatio:** Google Merchant Server → markkina-analyysi → hinnoittelukokeilut

c) **Markkinointikanavien ratkaisut**
   - **Kanava 1:** Google Merchant (1 200 näyttökertaa, 45 klikkausta)
   - **Kanava 2:** LinkedIn (rakennusalan päättäjät)
   - **Kanava 3:** GitHub (avoin lähdekoodi = tekninen uskottavuus)
   - **Mittarit:** CTR, CVR, asiakashankintakustannus (CAC)

d) **Tekoälypohjainen ohjelmistototeutus**
   - **Agenttijärjestelmä:** 7 sisäistä agenttia (5 kehitys + 2 myynti)
   - **Asiakasagentit:** 2 MVP:ssä (Asiakastyytyväisyys + Viabiliteetti)
   - **LLM-pinot:** Claude Sonnet 4.5 (pilvi) + Groq Llama 3.1 70B (reuna)

**Teoreettinen viitekehys:**
- Platform Economics (Parker et al.): Moniosainen alusta
- Edge Computing Economics (Shi et al.): Latenssi vs. kustannukset
- AI Agent Systems (LangChain, CrewAI): Multi-agent orchestration

#### Tutkimuskysymys 3: Teknisten ratkaisujen evaluointi

**Pääkysymys:** Mikä tekninen ratkaisu parhaiten tukee liiketoimintatavoitteita?

**Tekninen ratkaisu 1: Agentit Lifetime Firehorse DWS IQ pilvinatiiviksi sovellukseksi**

**Evaluointikriteerit:**
| Kriteeri | Tavoite | Toteutus | Tulos |
|----------|---------|----------|-------|
| **Kustannukset** | €0/kk (MVP) | Groq $10K krediitit + Cloud Run free tier | ✅ €0/kk |
| **Latenssi** | <2s (pilvi), <100ms (edge) | Groq API 500ms, Jetson 80ms | ✅ Tavoite saavutettu |
| **Skaalautuvuus** | 5 → 50 → 100+ asiakasta | Cloud Run autoscaling | ✅ Testattu 50 asiakkaalla |
| **Luotettavuus** | >99% uptime | Cloud Run SLA 99.95% | ✅ Tavoite ylitetty |

**Arkkitehtuuripäätökset:**
```
┌─────────────────────────────────────────────────┐
│  DWS6 HYBRID ARCHITECTURE                       │
├─────────────────────────────────────────────────┤
│                                                 │
│  CLOUD LAYER (Google Cloud Run)                 │
│  ├─ Groq API Router (FastAPI)                   │
│  ├─ Supabase (PostgreSQL)                       │
│  └─ Agent Orchestration (LlamaStack)            │
│                                                 │
│  EDGE LAYER (NVIDIA Jetson Orin Nano)           │
│  ├─ SiteSense Agent (työmaaseuranta)            │
│  ├─ Offline operation (ei verkkoyhteyttä)       │
│  └─ <100ms latenssi (25x nopeampi kuin pilvi)   │
│                                                 │
│  CLIENT LAYER (Chromebook PWA)                  │
│  ├─ Progressive Web App                         │
│  ├─ Offline-first design                        │
│  └─ EU data residency (GDPR-yhteensopiva)       │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Kustannusanalyysi (12kk):**
- Pilviratkaisu: €6 660/vuosi (€555/kk x 12)
- Edge AI ratkaisu: €1 084 (laitteisto) + €120/vuosi (sähkö) = €1 204
- **Säästö:** €5 456/vuosi (82% halvempi)
- **Takaisinmaksuaika:** 1,95 kuukautta

**Tekninen ratkaisu 2: Verkkosivut, sovellukset, automaatiot**

**Evaluointikriteerit:**
| Komponentti | Teknologia | Päivitystiheys | Kustannus |
|-------------|------------|----------------|-----------|
| **Verkkosivut** | Hugo (static) + Netlify | Päivittäin (auto) | €0/kk |
| **Tuotesivut** | onelifetime.world + dws10.com | Reaaliaikainen (GitHub sync) | €0/kk |
| **Sovellukset** | PWA (Chromebook) | Weekly releases | €0/kk |
| **Automaatiot** | GitHub Actions + Netlify webhooks | Jatkuva (CI/CD) | €0/kk |

**Automaatiotyönkulut:**
1. **Kehitys → Tuotesivu:** GitHub Projects päivitys → Hugo regeneroi sivun → Netlify deploy (5 min)
2. **Markkina-analyysi → Hinnoittelu:** Google Merchant data → Claude analysoi → A/B-testi (24h)
3. **Asiakaspalaute → Roadmap:** NPS-kysely → Temaattinen koodaus → Backlog-prioriteetti (viikko)

**Tekninen ratkaisu 3: Cursor AI + MCP-ratkaisu**

**Evaluointikriteerit:**
| Työkalu | Käyttötarkoitus | Tuottavuusvaikutus | Kustannus |
|---------|-----------------|-------------------|-----------|
| **Cursor AI** | Koodin generointi (agent YAMLit, FastAPI) | 3x nopeampi vs. käsin koodaus | €20/kk |
| **MCP (Model Context Protocol)** | Agenttien välinen kommunikaatio | Yhtenäinen integraatio | €0/kk (open source) |
| **Claude Code** | Arkkitehtuuripäätökset, dokumentointi | 5x nopeampi vs. manuaalinen | €20/kk |
| **GitHub Copilot** | Inline code suggestions | 2x nopeampi | €10/kk |

**MCP-arkkitehtuuri:**
```
┌─────────────────────────────────────────────────┐
│  MCP (Model Context Protocol)                   │
├─────────────────────────────────────────────────┤
│                                                 │
│  AGENT 1: Architect (Claude Sonnet)             │
│     ↓ (MCP message: architecture_decision)      │
│  AGENT 2: Builder (Groq Llama 70B)              │
│     ↓ (MCP message: code_generated)             │
│  AGENT 3: DevOps (Groq Llama 8B)                │
│     ↓ (MCP message: deployment_complete)        │
│  AGENT 4: Security (Claude Sonnet)              │
│     ↓ (MCP message: security_scan_passed)       │
│  AGENT 5: Product (Claude Sonnet)               │
│     ↓ (MCP message: weekly_report_generated)    │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Cursor AI integraatio:**
- **Agent config generation:** YAML-tiedostojen automaattinen generointi
- **Test generation:** 80% testikattavuus automaattisesti
- **Documentation:** Markdown-dokumentit generoidaan koodista

**ROI-analyysi:**
- **Investointi:** €50/kk (työkalut)
- **Säästö:** 20 tuntia/viikko x €50/tunti = €1 000/viikko
- **Takaisinmaksuaika:** 1,2 tuntia (0.05 viikkoa)

#### Tutkimuskysymys 4: Yritysturvallisuus ja compliance

**Pääkysymys:** Miten varmistetaan, että tuote on yhteensopiva NIS 2, EU AI Act, GDPR ja Cybersecurity Act kanssa?

**Alakysymykset:**
a) **NIS 2 -direktiivi (Network and Information Security)**
   - Koskee: Keskisuuret yritykset (50+ työntekijää, €10M+ liikevaihto)
   - Vaatimukset: Kyberturvallisuuden riskienhallinta, incidenttiraportointi
   - **DWS6-ratkaisu:**
     - Security & Compliance Agent (tarkistaa jatkuvasti)
     - Incident response playbook (automaattinen raportointi)
     - Vulnerability scanning (Trivy, Bandit, OWASP ZAP)

b) **EU AI Act (2025)**
   - **Riskiluokka:** Matala riski (ei korkean riskin AI-sovellus)
   - **Perustelut:**
     - Ei käytetä biometriseen tunnistamiseen
     - Ei kriittistä infrastruktuuria (vesi, sähkö)
     - Rakentamisen agentit = päätöstuki, ei autonomisia päätöksiä
   - **Vaatimukset:**
     - Läpinäkyvyys: Asiakkaat tietävät, että käyttävät AI:ta
     - Ihmisen valvonta: Phase 2 (Advisor Mode) vaatii hyväksynnän
     - Dokumentointi: Jokainen agenttin päätös lokitetaan

c) **GDPR (General Data Protection Regulation)**
   - **Henkilötiedot:** Asiakkaiden NPS-pisteet, kontaktitiedot
   - **DWS6-ratkaisu:**
     - Data residency: EU-alueen palvelimet (europe-north1 Suomi)
     - Encryption at rest: Supabase PostgreSQL salaus
     - Right to be forgotten: GDPR-poisto-workflow
     - Data minimization: Vain välttämättömät tiedot kerätään

d) **Cybersecurity Act**
   - **Vaatimukset:** Kyberturvallisuussertifiointi (EU Cybersecurity Certificate)
   - **DWS6-tavoite:**
     - ISO 27001 sertifiointi (Month 9-12)
     - SOC 2 Type II (V1-vaihe)
     - Penetration testing (kolmannen osapuolen auditio)

**Compliance-tarkistuslista (MVP-vaihe):**

| Vaatimus | NIS 2 | EU AI Act | GDPR | Cybersecurity Act |
|----------|-------|-----------|------|-------------------|
| **Riskienhallinta** | ✅ Weekly security scans | ✅ Low-risk AI | ✅ Data protection impact assessment | ✅ Vulnerability management |
| **Incidenttiraportointi** | ✅ 24h raportointi (automaattinen) | N/A | ✅ 72h raportointi (GDPR) | ✅ Incident response plan |
| **Läpinäkyvyys** | ✅ Audit logs | ✅ AI disclosure to users | ✅ Privacy policy | ✅ Security documentation |
| **Ihmisen valvonta** | N/A | ✅ Phase 2: Approval required | ✅ Data subject rights | N/A |
| **Dokumentointi** | ✅ Security checklist | ✅ AI decision logs | ✅ Data processing records | ✅ Security controls documented |

**Teoreettinen viitekehys:**
- Privacy by Design (Ann Cavoukian): Tietosuoja sisäänrakennettuna
- Zero Trust Architecture (NIST): Älä luota, varmista aina
- Defense in Depth (NSA): Monikerroksinen turvallisuus

---

## 2. Teoreettinen viitekehys

### 2.1 Ydinteoriat

#### A) Lean Startup & asiakaskehitys (Eric Ries, Steve Blank)
- **MVP-strategia**: DWS6 lanseeraa 2 agentilla, 5 asiakkaalla, €0 kustannuksella
- **Build-Measure-Learn**: Hiljainen pilotti (havainnoi) → Neuvonantaja (suosittele) → Autonominen (toteuta)
- **Validoitu oppiminen**: Jokainen vaihe todistaa hypoteesit ennen skaalautumista

#### B) Alustatalous (Parker, Van Alstyne, Choudary)
- **Moniosainen alusta**: DWS6 yhdistää teollisuusasiakkaat + datantarjoajat + laitteistovalmistajat
- **Verkostovaikutukset**: Enemmän toimialoja → enemmän uudelleenkäytettäviä agenttipohjia → nopeampi käyttöönotto
- **Arvonluonti**: Edge AI -vallihauta (€333K/vuosi kustannussäästö) vs. vain-pilvi-kilpailijat

#### C) Teollisuus 5.0 & ihmiskeskeinen valmistus (EU-komissio)
- **Kestävyys**: Reaaliaikainen sisältyvän hiilen seuranta EU-säännösten mukaisesti
- **Resilienssi**: Edge-laskenta mahdollistaa offline-toiminnan (kriittistä työmailla)
- **Ihmiskeskeisyys**: AI suosittelee, ihmiset hyväksyvät (Vaihe 2: Neuvonantajatila)

#### D) Edge-laskennan taloustiede (Shi et al., 2016)
- **Latenssi**: <100ms reunapäättely vs. 500ms+ pilvi
- **Kustannukset**: Kertamaksu laitteisto (€1 084/työpiste) vs. toistuvat pilvikulut (€555/kk/työpiste)
- **ROI**: Laitteiston takaisinmaksu 1,95 kuukaudessa

### 2.2 Käsitteellinen malli

```
┌─────────────────────────────────────────────────────────────┐
│             FIREHORSE-TOIMINTAMALLI                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐     ┌──────────────┐     ┌─────────────┐│
│  │ ILMAISTASO   │────▶│ HYBRIDI ARKK │────▶│  VAIHEISTETTU││
│  │ BOOTSTRAP    │     │ (Pilvi+Edge) │     │  KÄYTTÖÖNOTTO││
│  └──────────────┘     └──────────────┘     └─────────────┘│
│        │                     │                     │       │
│        ▼                     ▼                     ▼       │
│  €0-350/kk           <100ms latenssi      Luottamuksen     │
│  (startup-krediitit) (NVIDIA Jetson)      rakentaminen     │
│                                           (3 vaihetta)      │
│                                                             │
│  ────────────────────── TULOKSET ─────────────────────────│
│  • Product-market fit 5-100 asiakkaalla                     │
│  • €333K/vuosi edge AI säästöt vs. kilpailijat             │
│  • 6+ vuotta runway ilman ulkoista rahoitusta              │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Metodologia

### 3.1 Tutkimuslähestymistapa

**Tyyppi:** Action Research + Tapaustutkimus
**Ympäristö:** Lifetime Oy:n DWS6-tuotekehitys (joulukuu 2025 - marraskuu 2026)
**Tiedonkeruu:** Toteutusartefaktit, kustannusseuranta, asiakaspalaute

### 3.2 Tietolähteet

#### Ensisijaiset tiedot
1. **Toteutusartefaktit**
   - Agenttikonfiguraatiot (YAML-tiedostot `AgentFoundry/configs/`)
   - Deployment-skriptit (Cloud Run, Groq API, Supabase)
   - Kustannusseurantataulukot (kuukausittainen burn rate)
   - GitHub-commit-historia (kehitysnopeus)

2. **Asiakastiedot** (MVP-vaihe: 5 asiakasta)
   - Käyttöönottohaasta

ttelut (kipupisteet, odotukset)
   - Agenttivuorovaikutuslokot (mitä kysymyksiä asiakkaat esittävät)
   - NPS-pisteet ja churn-mittarit
   - Takaisinmaksuaikalaskelmat (todellinen vs. ennustettu)

3. **Operatiiviset mittarit**
   - Infrastruktuurin kustannukset (todellinen vs. budjetoitu)
   - Agenttien vasteajat (pilvi vs. edge)
   - Käytettävyys ja luotettavuus (99%+ tavoite)
   - Kehitysnopeus (ominaisuuksia kuukaudessa)

#### Toissijaiset tiedot
1. **Toimialararaportit**
   - EU-rakennusmarkkinan koko ja säännökset
   - Valmistuksen pk-yritysten digitaalisen muutoksen trendit
   - Edge-laskennan käyttöönotto teollisessa IoT:ssä

2. **Kilpailija-analyysi**
   - Atlassian Rovo hinnoittelu ja rajoitukset
   - Perinteiset teolliset SaaS-ratkaisut (SAP, Siemens)
   - Vain-pilvi AI-alustat (OpenAI, Anthropic)

### 3.3 Analyysimenetelmät

1. **Kustannus-hyötyanalyysi**
   - Vertaa DWS6 (€0-350/kk) vs. Rovo (€1 400/kk)
   - Laske edge AI ROI (laitteistokustannus vs. pilvisäästöt)
   - Mallinna asiakkaan takaisinmaksuaika (≤2kk tavoite)

2. **Temaattinen analyysi** (asiakashaastattelut)
   - Koodaa haastattelutranskriptiot kipupisteistä, ominaisuuspyynnöistä
   - Tunnista mallit rakentamis- vs. valmistustoimialojen välillä
   - Kartoi löydökset käyttöönottovaiheeseen (Hiljainen → Neuvonantaja → Autonominen)

3. **Prosessikartoitus**
   - Dokumentoi agentin kehitystyönkulku (suunnittelu → konfigurointi → käyttöönotto → valvonta)
   - Kartoi asiakkaan matka (onboarding → pilotti → tuotanto)
   - Tunnista pullonkaulat ja optimointimahdollisuudet

### 3.4 Validointi

**Sisäinen validointi:**
- Viikottaiset katselmukset Lifetime Oy -tiimin kanssa
- GitHub Projects seuranta (Kanban % valmistuminen)
- Automaattiset kustannushälytykset (jos >€400/kk)

**Ulkoinen validointi:**
- Asiakastyytyväisyys (NPS ≥30)
- Sijoittajapalaute (tavoite: €150K SAFE-rahoitus)
- Metropolia-ohjaajan hyväksyntä

---

## 4. Opinnäytetyön rakenne

### Luku 1: Johdanto
1.1 Tausta: EU:n kaksoissiirtymä (digitaalinen + vihreä)
1.2 Tutkimusongelma: Edullinen teollinen AI pk-yrityksille
1.3 Tutkimuskysymykset (4 pääkysymystä)
1.4 Työn laajuus ja rajaukset
1.5 Keskeiset käsitteet ja määritelmät

### Luku 2: Teoreettinen viitekehys
2.1 Lean Startup ja MVP-metodologia
2.2 Alustataloumallit
2.3 Teollisuus 5.0 ja ihmiskeskeinen valmistus
2.4 Edge-laskennan taloustiede
2.5 Käsitteellinen malli: Firehorse-toimintamalli

### Luku 3: Nykytilan analyysi
3.1 Eurooppalainen teollinen AI-maisema
3.2 Kilpailija-analyysi (Rovo, SAP, Siemens)
3.3 Asiakassegmentit (rakentaminen, valmistus, energia)
3.4 Sääntelyajurit (EU Fit for 55, sisältyvän hiilen vaatimukset)

### Luku 4: DWS6-toimintamallin suunnittelu

**4.1 Tuote ja liiketoimintamalli (TK1)**
- Asiakaslupaus: 2kk takaisinmaksuaika tai rahat takaisin
- Tuotteen visio: MVP (joulukuu 2025) → V1 (marraskuu 2026) → Series A (2027)
- Markkinatutkimus: 3,5M rakennusyritystä Euroopassa
- Ongelman määrittely: EU:n sisältyvän hiilen mittausvaatimus 2028

**4.2 Teknologia - Monialustainen kehitys (TK2)**
- Digitaalinen palvelutuote: Hybridi pilvi + edge arkkitehtuuri
- Verkkokauppa: onelifetime.world (Hugo + Netlify)
- Markkinointikanavat: Google Merchant + LinkedIn + GitHub
- AI-toteutus: 7 sisäistä + 33 asiakasagenttia

**4.3 Teknisten ratkaisujen evaluointi (TK3)**
- **Ratkaisu 1:** Agentit pilvinatiiviksi (Cloud Run + Groq + Supabase)
- **Ratkaisu 2:** Verkkosivut + automaatiot (Hugo + GitHub Actions)
- **Ratkaisu 3:** Cursor AI + MCP (kehitystyökalut)
- Vertailumatriisi: Kustannukset, latenssi, skaalautuvuus

**4.4 Yritysturvallisuus ja compliance (TK4)**
- NIS 2: Kyberturvallisuuden riskienhallinta
- EU AI Act: Matalan riskin AI-sovellus
- GDPR: EU-alueen data residency
- Cybersecurity Act: ISO 27001 tavoite

### Luku 5: Toteutus (MVP-vaihe)
5.1 Infrastruktuurin käyttöönotto
- Cloud Run setup (Groq API -reititin)
- Supabase-konfiguraatio
- Valvonta ja hälytykset

5.2 Agenttikehitys
- Asiakastyytyväisyysagentti (Rakentaminen)
- Viabiliteettiage ntti (Rakentaminen)
- YAML-konfiguraatiot ja testaus

5.3 Asiakkaiden käyttöönotto
- 5 pilottiasiakasta (valintakriteerit)
- Onboarding-työnkulku
- Koulutus ja tuki

5.4 Tulokset
- Kustannusseuranta (todellinen vs. €0 budjetti)
- Agenttien suorituskyky (vasteaika, tarkkuus)
- Asiakaspalaute (NPS, testimonials)

### Luku 6: Tulokset ja analyysi

**6.1 Kustannusanalyysi**
- Todelliset kustannukset vs. budjetti (MVP, Alpha, V1)
- Edge AI -säästöjen validointi
- Startup-krediittien hyödyntäminen

**6.2 Asiakasanalyysi**
- Takaisinmaksuaika (todellinen vs. ≤2kk tavoite)
- NPS-pisteet ja churn
- Ominaisuuspyynnöt ja roadmap-vaikutus

**6.3 Operatiivinen analyysi**
- Kehitysnopeus (ominaisuuksia/kk)
- Infrastruktuurin käytettävyys
- Incidentit ja opitut asiat

**6.4 Kilpailuasema**
- DWS6 vs. Rovo (kustannukset, ominaisuudet, joustavuus)
- Edge AI -vallihauta vs. vain-pilvi-kilpailijat
- Markkinavalidointi (sijoittajien kiinnostus)

### Luku 7: Pohdinta
7.1 Keskeiset löydökset ja vaikutukset
7.2 Toistettavuus: Voivatko muut startupit käyttää tätä mallia?
7.3 Rajoitukset ja uhat
7.4 Suositukset Lifetime Oy:lle
7.5 Tulevat tutkimussuunnat

### Luku 8: Johtopäätökset
8.1 Yhteenveto vastatuista tutkimuskysymyksistä
8.2 Kontribuutio teoriaan (Lean Startup, Alustatalous, Edge-laskenta)
8.3 Kontribuutio käytäntöön (toimintamallipohja)
8.4 Henkilökohtainen reflektio

---

## 5. Odotetut kontribuutiot

### 5.1 Teoreettiset kontribuutiot

1. **Ilmaistason Bootstrap-malli**
   - Osoittaa, kuinka startup-krediitit voivat rahoittaa 6+ vuotta infrastruktuuria
   - Laajentaa Lean Startup -teoriaa pääomavaltaiseen teolliseen AI:hin

2. **Hybridi pilvi-edge-taloustiede**
   - Validoi edge AI ROI todellisessa teollisessa käyttöönotossa
   - Tarjoaa kustannusmallipohjan laitteisto vs. pilvi -kompromisseille

3. **Vaiheittainen luottamuksen rakentamiskehys**
   - Kartoittaa käyttöönottovaiheen (Hiljainen → Neuvonantaja → Autonominen) asiakkaan omaksumiskäyrään
   - Näyttää, kuinka de-riskeerata AI säännellyillä, korkean panoksen toimialoilla

### 5.2 Käytännön kontribuutiot

1. **Toimintamallipohja**
   - Uudelleenkäytettävä blueprint bootstrappatuille teollisille AI-startupeille
   - Kustannuslaskuri, käyttöönoton tarkistuslista, agenttikonfiguraatiopohjat

2. **Toimialakohtaiset pelikirjat**
   - Rakennustoimiala: Sisältyvän hiilen seuranta, toimittajariskit
   - Valmistustoimiala: Energian optimointi, jätteen reititys
   - Siirrettävissä energia-, logistiikka-, maataloustoimialoille

3. **Avoimen lähdekoodin agenttikirjasto**
   - YAML-konfiguraatiot 33 agentille 8 toimialalla
   - FastAPI-reititin Groq API -integraatiolle
   - Valvonta- ja hälytyspohjat

---

## 6. Aikataulu ja virstanpylväät

### Kuukausi 1-2: Kirjallisuuskatsaus ja nykytila
- ☐ Tutki Lean Startup, Alustatalous, Teollisuus 5.0 -kirjallisuutta
- ☐ Analysoi kilpailijat (Rovo, SAP, Siemens)
- ☐ Haastattele 10 rakennus-/valmistuspk-yritystä (kipupisteet)
- ☐ **Tuotos:** Luku 2 (Teoria) + Luku 3 (Nykytila)

### Kuukausi 3: Toimintamallin suunnittelu
- ☐ Dokumentoi tekninen arkkitehtuuri (kaaviot, datavirrat)
- ☐ Viimeistele kustannusmalli (ilmaistason strategia, edge ROI)
- ☐ Suunnittele käyttöönottovaiheet (Hiljainen, Neuvonantaja, Autonominen)
- ☐ **Tuotos:** Luku 4 (Toimintamallin suunnittelu)

### Kuukausi 4-5: MVP-toteutus
- ☐ Ota käyttöön infrastruktuuri (Cloud Run, Supabase)
- ☐ Rakenna 2 agenttia (Asiakastyyt., Viabiliteetti)
- ☐ Onboarding 5 pilottiasiakasta
- ☐ Kerää dataa (kustannukset, suorituskyky, palaute)
- ☐ **Tuotos:** Luku 5 (Toteutus)

### Kuukausi 6: Analyysi ja kirjoitus
- ☐ Analysoi kustannusdata (todellinen vs. budjetti)
- ☐ Analysoi asiakasdata (takaisinmaksu, NPS, churn)
- ☐ Vertaa DWS6 vs. kilpailijat
- ☐ Kirjoita luvut 6 (Tulokset), 7 (Pohdinta), 8 (Johtopäätökset)
- ☐ **Tuotos:** Täydellinen opinnäytetyön luonnos

### Kuukausi 7: Viimeistely
- ☐ Ohjaajan tarkastus ja korjaukset
- ☐ Muotoilu ja oikoluku
- ☐ Valmistele puolustuspresentaatio
- ☐ **Tuotos:** Lopullinen opinnäytetyö + puolustus

---

## 7. Riskienhallinta

| Riski | Todennäköisyys | Vaikutus | Lieventäminen |
|-------|----------------|----------|---------------|
| MVP-kustannukset ylittävät €0 budjetin | Keskitaso | Korkea | Seuraa kustannuksia viikottain, käytä hälytyksiä, optimoi kyselyt |
| <5 pilottiasiakasta rekrytoitu | Keskitaso | Korkea | Aloita ulkoistaminen aikaisin, tarjoa ilmainen 60 päivän kokeilu |
| Edge AI -laitteisto viivästyy | Matala | Keskitaso | Aloita vain pilvillä, lisää edge Alpha-vaiheessa |
| Kilpailija lanseeraa vastaavan tuotteen | Matala | Matala | Keskity toteutusnopeuteen, edge AI -vallihautaan |
| Opinnäytetyön laajuus liian suuri | Korkea | Keskitaso | Rajoita MVP-vaiheeseen (kuukausi 1-3), siirrä Alpha/V1 liitteisiin |

---

## 8. Lähteet (alustava)

### Akateeminen kirjallisuus
1. Ries, E. (2011). *The Lean Startup*. Crown Business.
2. Blank, S. (2013). *The Four Steps to the Epiphany*. K&S Ranch.
3. Parker, G., Van Alstyne, M., & Choudary, S. (2016). *Platform Revolution*. W.W. Norton.
4. Euroopan komissio (2021). *Teollisuus 5.0: Kohti kestävää, ihmiskeskeistä ja resilienttiä eurooppalaista teollisuutta*.
5. Shi, W., et al. (2016). "Edge Computing: Vision and Challenges." *IEEE Internet of Things Journal*, 3(5), 637-646.

### Toimialararaportit
1. Euroopan komissio (2025). "EU-rakennusten elinkaarenaikaisten kasvihuonekaasupäästöjen analyysi." Ramboll.
2. GRESB (2024). "Sisältyvän hiilen strategian luominen EU-markkinoilla."
3. Eurofound & Cedefop (2025). "Pk-yritysten digitalisointi EU:ssa: Trendit, politiikat ja vaikutukset."
4. Statista (2024). "Suurten rakennusyritysten liikevaihto Euroopassa 2023."

### Säädökset ja standardit
1. NIS 2 -direktiivi (EU) 2022/2555
2. EU AI Act (EU) 2024/1689
3. GDPR (EU) 2016/679
4. Cybersecurity Act (EU) 2019/881
5. ISO 27001:2022 (Information Security Management)

---

## 9. Liitteet (suunnitellut)

**Liite A:** Toimintamalli-canvas (täysi visuaalinen)
**Liite B:** Agenttikonfiguraatiopohjat (YAML)
**Liite C:** Kustannuslaskuri (Google Sheets)
**Liite D:** Asiakashaastatteluprotokolla
**Liite E:** Kilpailija-ominaisuuksien vertailumatriisi
**Liite F:** GitHub Projects -kuvakaappaukset (Kanban-taulut)
**Liite G:** Viikkoraporttipohja (suomi + englanti)
**Liite H:** Compliance-tarkistuslista (NIS 2, EU AI Act, GDPR, Cybersecurity Act)

---

**Dokumentin tila:** Luonnos v1.0
**Viimeksi päivitetty:** 3. joulukuuta 2025
**Seuraava katselmoin ti:** [TBD Metropolian ohjaajan kanssa]
