#!/usr/bin/env python3
"""Build public/fr/self-assessment.html from public/self-assessment.html.

Applies an explicit EN->FR string map. Every source string MUST be found;
the script fails loudly listing anything unmatched, so the logic stays
byte-identical and only user-facing strings change.
"""
import sys, pathlib

SRC = pathlib.Path('public/self-assessment.html')
DST = pathlib.Path('public/fr/self-assessment.html')

P = []  # (old, new, min_count)
def r(old, new, n=1): P.append((old, new, n))

# ---------- HTML head / body chrome ----------
r('<html lang="en">', '<html lang="fr">')
r('<title>elect-rix Audit — Self-Assessment Tool</title>', '<title>Audit elect-rix — Outil d\u2019auto-évaluation</title>')
r('<div class="tagline">Make it work.</div>\n    <div style="font-size:12px;margin-top:6px"><a href="/fr/self-assessment" style="color:var(--accent);text-decoration:none">Français</a></div>',
  '<div class="tagline">Faites que ça marche.</div>\n    <div style="font-size:12px;margin-top:6px"><a href="/self-assessment" style="color:var(--accent);text-decoration:none">English</a></div>')

# ---------- Intro screen ----------
r('Data Sovereignty Self-Assessment', 'Auto-évaluation de la souveraineté des données')
r("Map where your business data lives, what's cloud-dependent, what compliance paperwork is missing, and what to fix first. Based on the elect-rix 5-layer audit methodology.",
  'Repérez où vivent les données de votre entreprise, ce qui dépend du nuage, quels documents de conformité manquent et quoi corriger en premier. Basé sur la méthodologie d\u2019audit en 5 couches d\u2019elect-rix.')
r('"You\'re already responsible for personal and client data under Canadian rules. Most small firms can\'t answer, on one page, where that data lives, who can open it, or what dies if Microsoft/Google is down. This tool builds that page."',
  '« Vous êtes déjà responsable des données personnelles et des données clients en vertu des règles canadiennes. La plupart des petites entreprises ne peuvent pas répondre, sur une seule page, où vivent ces données, qui peut les ouvrir, ni ce qui cesse de fonctionner si Microsoft/Google tombe en panne. Cet outil construit cette page. »')
r('This self-assessment produces a clarity map, not a compliance certification. Not legal advice. Not a penetration test. Based on your responses — honest blanks and "unknown" are valid answers.',
  'Cette auto-évaluation produit une carte de clarté, pas une certification de conformité. Ceci n\u2019est pas un avis juridique. Ceci n\u2019est pas un test d\u2019intrusion. Basé sur vos réponses — les cases laissées vides honnêtement et « inconnu » sont des réponses valides.')
r('Organization Information', 'Renseignements sur l\u2019organisation')
r('<label>Organization name</label>', '<label>Nom de l\u2019organisation</label>')
r('placeholder="e.g., Smith & Associates Law"', 'placeholder="p. ex. Tremblay & Associés Avocats"')
r('<label>Your name (auditor)</label>', '<label>Votre nom (auditeur)</label>')
r('placeholder="e.g., John Smith"', 'placeholder="p. ex. Marie Tremblay"')
r('<label>Role / title</label>', '<label>Rôle / titre</label>')
r('placeholder="e.g., Managing Partner"', 'placeholder="p. ex. Associée directrice"')
r('Select Your Industry Profile', 'Sélectionnez votre profil d\u2019industrie')
r('This determines which compliance frameworks and questions apply to your assessment.',
  'Cela détermine quels cadres de conformité et quelles questions s\u2019appliquent à votre évaluation.')
r('Select Audit Tier', 'Sélectionnez le niveau d\u2019audit')
r('Quick Scan covers all 5 layers at a summary level. Standard adds staff workflow detail. Full adds remediation roadmap.',
  'Le Survol rapide couvre les 5 couches au niveau sommaire. Standard ajoute le détail des flux de travail du personnel. Complet ajoute une feuille de route de remédiation.')
r('Start Assessment →', 'Commencer l\u2019évaluation →')
r('<span id="progress-layer">Layer 1 of 5</span>', '<span id="progress-layer">Couche 1 sur 5</span>')
r('← Back', '← Retour')
r('← Start Over', '← Recommencer')
r('Print / Save PDF', 'Imprimer / Enregistrer en PDF')
r('Download Report', 'Télécharger le rapport')

# ---------- Profiles & tiers ----------
r("name: 'General SMB', icon: '🏢', desc: 'Standard commercial business', frameworks: ['PIPEDA']",
  "name: 'PME générale', icon: '🏢', desc: 'Entreprise commerciale standard', frameworks: ['LPRPDE']")
r("name: 'Healthcare', icon: '⚕️', desc: 'Clinic / patient data', frameworks: ['PIPEDA', 'PHIPA']",
  "name: 'Santé', icon: '⚕️', desc: 'Clinique / données de patients', frameworks: ['LPRPDE', 'LPRPSA']")
r("name: 'Legal', icon: '⚖️', desc: 'Law firm / privilege', frameworks: ['PIPEDA', 'Solicitor-Client']",
  "name: 'Droit', icon: '⚖️', desc: 'Cabinet d\u2019avocats / secret professionnel', frameworks: ['LPRPDE', 'Secret professionnel']")
r("name: 'Government', icon: '🏛️', desc: 'Public sector / contractor', frameworks: ['PIPEDA', 'ITSG-33/37', 'FOIPOP']",
  "name: 'Gouvernement', icon: '🏛️', desc: 'Secteur public / entrepreneur', frameworks: ['LPRPDE', 'ITSG-33/37', 'LPRIP']")
r(r"desc: 'Quebec residents\' data', frameworks: ['PIPEDA', 'Law 25']", r"desc: 'Données de résidents du Québec', frameworks: ['LPRPDE', 'Loi 25']")
r("name: 'Quebec', icon:", "name: 'Québec', icon:")
r("name: 'Quick Scan', icon: '⚡', desc: 'All 5 layers, summary level'", "name: 'Survol rapide', icon: '⚡', desc: 'Les 5 couches, niveau sommaire'")
r("name: 'Standard', icon: '📋', desc: 'Adds staff workflow detail'", "name: 'Standard', icon: '📋', desc: 'Ajoute le détail des flux de travail du personnel'")
r("name: 'Full', icon: '📊', desc: 'Adds remediation roadmap'", "name: 'Complet', icon: '📊', desc: 'Ajoute une feuille de route de remédiation'")

# ---------- Layer 1 ----------
r("num: 1, name: 'Data', icon: '💾'", "num: 1, name: 'Données', icon: '💾'")
r("desc: 'What sensitive stuff exists, and where does it live?'", "desc: 'Quelles données sensibles existent et où vivent-elles?'")
r("pitch: 'If the building burned but internet still worked — what would you still have, and where?'",
  "pitch: 'Si l\u2019immeuble brûlait mais qu\u2019internet fonctionnait encore — que vous resterait-il, et où?'")
r("text: 'What types of sensitive data does your organization handle?'", "text: 'Quels types de données sensibles votre organisation traite-t-elle?'")
r("label: 'Client / customer files'", "label: 'Dossiers clients'")
r("label: 'Email / messages'", "label: 'Courriels / messages'")
r("label: 'Financial / accounting / invoices'", "label: 'Finances / comptabilité / factures'")
r("label: 'Employee HR / payroll'", "label: 'RH des employés / paie'")
r("label: 'Contracts / legal documents'", "label: 'Contrats / documents juridiques'")
r("label: 'Health / clinical records'", "label: 'Dossiers de santé / cliniques'")
r("label: 'Photos / scans / media'", "label: 'Photos / numérisations / médias'")
r("label: 'Project / job files'", "label: 'Fichiers de projets / chantiers'")
r("label: 'Marketing lists / CRM'", "label: 'Listes de marketing / CRM'")
r("label: 'Other (specify)'", "label: 'Autre (précisez)'", 6)
r("text: 'Where does each data type primarily live? Mark all that apply.'", "text: 'Où vit principalement chaque type de données? Cochez tout ce qui s\u2019applique.'")
r("{ id: 'local_pc', label: 'Local PC' }", "{ id: 'local_pc', label: 'PC local' }")
r("{ id: 'shared_drive', label: 'Shared drive / NAS' }", "{ id: 'shared_drive', label: 'Lecteur partagé / NAS' }")
r("{ id: 'email_only', label: 'Email only' }", "{ id: 'email_only', label: 'Courriel seulement' }")
r("{ id: 'cloud_folder', label: 'Cloud folder' }", "{ id: 'cloud_folder', label: 'Dossier infonuagique' }")
r("{ id: 'industry_saas', label: 'Industry SaaS' }", "{ id: 'industry_saas', label: 'SaaS sectoriel' }")
r("{ id: 'paper', label: 'Paper' }", "{ id: 'paper', label: 'Papier' }")
r("label: 'Unknown'", "label: 'Inconnu'", 8)
r("text: 'Who outside your company can open these files today?'", "text: 'Qui, à l\u2019extérieur de votre entreprise, peut ouvrir ces fichiers aujourd\u2019hui?'")
r("label: 'Nobody that we know of'", "label: 'Personne à notre connaissance'")
r("label: 'Cloud vendor staff / sub-processors (assumed)'", "label: 'Personnel du fournisseur infonuagique / sous-traitants (présumé)'")
r("label: 'MSP / IT vendor'", "label: 'Fournisseur de services gérés / TI'")
r("label: 'Accountant / bookkeeper (remote access)'", "label: 'Comptable / teneur de livres (accès à distance)'")
r("label: 'Former staff accounts still active'", "label: 'Comptes d\u2019anciens employés encore actifs'")
r("label: 'Unknown — flag for report'", "label: 'Inconnu — à signaler au rapport'")

# ---------- Layer 2 ----------
r("num: 2, name: 'Cloud & Services', icon: '☁️',", "num: 2, name: 'Nuage et services', icon: '☁️',")
r("desc: 'Which cloud apps keep the business alive? What dies offline?'",
  "desc: 'Quelles applications infonuagiques gardent l\u2019entreprise en vie? Qu\u2019est-ce qui meurt hors ligne?'")
r(r"pitch: 'What do you log into every morning? What\'s always on the phone home screen for work?'",
  "pitch: 'À quoi vous connectez-vous chaque matin? Qu\u2019est-ce qui est toujours sur l\u2019écran d\u2019accueil du téléphone pour le travail?'")
r("text: 'Which email and office suite do you use?'", "text: 'Quelle suite de courriel et de bureau utilisez-vous?'")
r("label: 'Other email host (specify)'", "label: 'Autre hébergeur de courriel (précisez)'")
r("label: 'Unknown / mixed personal + work'", "label: 'Inconnu / mélange personnel + travail'")
r("text: 'Which file storage and collaboration tools do you use?'", "text: 'Quels outils de stockage de fichiers et de collaboration utilisez-vous?'")
r("label: 'Local only (no cloud file sync)'", "label: 'Local seulement (aucune synchro infonuagique)'")
r("text: 'Which accounting or financial software do you use?'", "text: 'Quel logiciel de comptabilité ou de finance utilisez-vous?'")
r("label: 'Bank online only'", "label: 'Banque en ligne seulement'")
r("text: 'Which CRM, sales, or booking tools do you use?'", "text: 'Quels outils de CRM, de vente ou de réservation utilisez-vous?'")
r("label: 'Jobber / ServiceTitan / field-service app'", "label: 'Jobber / ServiceTitan / application de services sur le terrain'")
r("label: 'Calendly / booking tool'", "label: 'Calendly / outil de réservation'")
r("label: 'Spreadsheet only'", "label: 'Tableur seulement'")
r("{ id: 'none_crm', label: 'None' }", "{ id: 'none_crm', label: 'Aucun' }")
r("text: 'Which industry-specific or vertical software do you use?'", "text: 'Quel logiciel propre à votre industrie utilisez-vous?'")
r("label: 'Practice management / EHR / EMR (specify)'", "label: 'Gestion de pratique / DSE / DME (précisez)'")
r("label: 'Legal practice / trust accounting (specify)'", "label: 'Gestion juridique / comptabilité en fiducie (précisez)'")
r("label: 'Dental / clinic software (specify)'", "label: 'Logiciel dentaire / de clinique (précisez)'")
r("label: 'Construction / estimating (specify)'", "label: 'Construction / estimation (précisez)'")
r("label: 'Other vertical (specify)'", "label: 'Autre secteur (précisez)'")
r("label: 'None / not applicable'", "label: 'Aucun / sans objet'")
r("text: 'Which communication and meeting tools do you use?'", "text: 'Quels outils de communication et de réunion utilisez-vous?'")
r("label: 'WhatsApp / iMessage for business'", "label: 'WhatsApp / iMessage pour les affaires'")
r("label: 'Phone / VoIP (specify provider)'", "label: 'Téléphone / VoIP (précisez le fournisseur)'")
r("text: 'What backup and security tools do you have in place?'", "text: 'Quels outils de sauvegarde et de sécurité avez-vous en place?'")
r("label: 'Vendor backup only (OneDrive/Google built-in)'", "label: 'Sauvegarde du fournisseur seulement (OneDrive/Google intégré)'")
r("label: 'Backblaze / Carbonite / similar cloud backup'", "label: 'Backblaze / Carbonite / sauvegarde infonuagique similaire'")
r("label: 'Local external drive / NAS backup'", "label: 'Disque externe local / sauvegarde NAS'")
r("label: 'No formal backup known'", "label: 'Aucune sauvegarde formelle connue'")
r("label: 'Password manager (specify)'", "label: 'Gestionnaire de mots de passe (précisez)'")
r("label: 'Antivirus / EDR (specify)'", "label: 'Antivirus / EDR (précisez)'")
r("label: 'VPN for remote work'", "label: 'VPN pour le télétravail'")
r("text: 'What AI tools are in use today?'", "text: 'Quels outils d\u2019IA sont utilisés aujourd\u2019hui?'")
r("label: 'Claude / other cloud AI'", "label: 'Claude / autre IA infonuagique'")
r("label: 'Local AI only'", "label: 'IA locale seulement'")
r("{ id: 'none_ai', label: 'None known' }", "{ id: 'none_ai', label: 'Aucun connu' }")
r("label: 'Staff use personal AI on work data (RISK)'", "label: 'Le personnel utilise des IA personnelles sur des données de travail (RISQUE)'")
r("text: 'If your cloud services go down for a day, what stops completely?'",
  "text: 'Si vos services infonuagiques tombent en panne pendant une journée, qu\u2019est-ce qui s\u2019arrête complètement?'")
r("{ id: 'email_stops', label: 'Email' }", "{ id: 'email_stops', label: 'Courriel' }")
r("label: 'File access'", "label: 'Accès aux fichiers'")
r("label: 'Billing / invoicing'", "label: 'Facturation'")
r("label: 'Scheduling / bookings'", "label: 'Horaires / réservations'")
r("label: 'Industry app (clinical/legal/etc.)'", "label: 'Application sectorielle (clinique/juridique/etc.)'")
r("label: 'Phones / VoIP'", "label: 'Téléphones / VoIP'")
r("label: 'Almost nothing — local-first already'", "label: 'Presque rien — déjà en mode local d\u2019abord'")
r("text: 'If a cloud outage occurs, does a workaround exist?'", "text: 'En cas de panne infonuagique, existe-t-il une solution de rechange?'")
r("{ id: 'workaround_yes', label: 'Yes', risk: 0, allowText: true, textLabel: 'Describe the workaround' }",
  "{ id: 'workaround_yes', label: 'Oui', risk: 0, allowText: true, textLabel: 'Décrivez la solution de rechange' }")
r("{ id: 'workaround_partial', label: 'Partial', risk: 1 }", "{ id: 'workaround_partial', label: 'Partielle', risk: 1 }")
r("{ id: 'workaround_no', label: 'No', risk: 3 }", "{ id: 'workaround_no', label: 'Non', risk: 3 }")

# ---------- Layer 3 ----------
r("num: 3, name: 'Gear & Network', icon: '🔌',", "num: 3, name: 'Équipement et réseau', icon: '🔌',")
r("desc: 'What boxes and Wi-Fi exist on site?'", "desc: 'Quels boîtiers et quel Wi-Fi existe-t-il sur place?'")
r('pitch: \'Where does the internet come in? Any box people call "the server"?\'',
  "pitch: 'Où entre l\u2019internet? Y a-t-il un boîtier que les gens appellent « le serveur »?'")
r("text: 'What is your internet setup?'", "text: 'Quelle est votre configuration internet?'")
r("label: 'Single ISP'", "label: 'FAI unique'")
r("label: 'Dual / backup link'", "label: 'Lien double / de secours'")
r("label: 'Cellular hotspot fallback'", "label: 'Point d\u2019accès cellulaire de secours'")
r("label: 'Unknown ISP'", "label: 'FAI inconnu'")
r("text: 'What on-site equipment do you have?'", "text: 'Quel équipement avez-vous sur place?'")
r("label: 'Workstations / laptops only'", "label: 'Postes de travail / portables seulement'")
r('label: \'Desktop "server" under desk\'', "label: '« Serveur » de bureau sous le bureau'")
r("label: 'NAS / Synology / TrueNAS / similar'", "label: 'NAS / Synology / TrueNAS / similaire'")
r("label: 'Rack / closet gear'", "label: 'Équipement en rack / en armoire'")
r("label: 'Managed router / firewall (specify brand)'", "label: 'Routeur géré / pare-feu (précisez la marque)'")
r("label: 'Consumer router only'", "label: 'Routeur grand public seulement'")
r("label: 'Printers with scan-to-email / cloud'", "label: 'Imprimantes avec numérisation vers courriel / nuage'")
r("label: 'Security cameras / NVR'", "label: 'Caméras de sécurité / NVR'")
r("label: 'Unknown — needs site walk'", "label: 'Inconnu — nécessite une visite des lieux'")
r("text: 'How is your Wi-Fi configured?'", "text: 'Comment votre Wi-Fi est-il configuré?'")
r("label: 'Staff + guest separated'", "label: 'Personnel + invités séparés'")
r("label: 'One network for everything'", "label: 'Un seul réseau pour tout'")
r("text: 'How do staff access the office network remotely?'", "text: 'Comment le personnel accède-t-il au réseau du bureau à distance?'")
r("label: 'RDP / screen share tools'", "label: 'RDP / outils de partage d\u2019écran'")
r("label: 'Cloud-only (no remote to office machines)'", "label: 'Nuage seulement (aucun accès distant aux machines du bureau)'")

# ---------- Layer 4 ----------
r("num: 4, name: 'Compliance Paperwork', icon: '📋',", "num: 4, name: 'Documents de conformité', icon: '📋',")
r("desc: 'What rules apply, what paper exists? Yes/no/unknown — not legal opinion.'",
  "desc: 'Quelles règles s\u2019appliquent, quels documents existent? Oui/non/inconnu — pas une opinion juridique.'")
r(r"pitch: 'Do you have a privacy policy? Retention rules? Who gets told if there\'s a breach?'",
  "pitch: 'Avez-vous une politique de confidentialité? Des règles de conservation? Qui est avisé en cas d\u2019atteinte?'")
r(r"disclaimer: 'I\'m not your lawyer. I only check whether basic paperwork exists.'",
  "disclaimer: 'Je ne suis pas votre avocat. Je vérifie seulement si les documents de base existent.'")
r("text: 'Which compliance frameworks may apply to your organization?'",
  "text: 'Quels cadres de conformité peuvent s\u2019appliquer à votre organisation?'")
r("label: 'PIPEDA (general Canadian commercial personal info)'", "label: 'LPRPDE (renseignements personnels commerciaux au Canada)'")
r("label: 'Provincial health privacy (e.g. PHIPA) — if health sector'", "label: 'Protection provinciale des renseignements sur la santé (p. ex. LPRPSA) — si secteur de la santé'")
r("label: 'Solicitor-client / professional duty — if law'", "label: 'Secret professionnel de l\u2019avocat / devoir professionnel — si droit'")
r("label: 'Government customer / ITSG / security questionnaire'", "label: 'Client gouvernemental / ITSG / questionnaire de sécurité'")
r("label: 'FOIPOP / public-sector angle'", "label: 'LPRIP / angle du secteur public'")
r(r"label: 'Quebec Law 25 — if handling Quebec residents\' data'", "label: 'Loi 25 du Québec — si vous traitez des données de résidents du Québec'")
r("label: 'None they know of'", "label: 'Aucun à leur connaissance'")
r("label: 'Unknown — note in report'", "label: 'Inconnu — à noter au rapport'")
r("text: 'Which compliance documents exist in your organization?'", "text: 'Quels documents de conformité existent dans votre organisation?'")
r("columns: ['Yes', 'No', 'Unknown']", "columns: ['Oui', 'Non', 'Inconnu']")
r("label: 'Privacy policy', gap: 2", "label: 'Politique de confidentialité', gap: 2")
r("label: 'Written data inventory', gap: 2", "label: 'Inventaire écrit des données', gap: 2")
r("label: 'Access / who-can-open-what documentation', gap: 2", "label: 'Documentation des accès (qui peut ouvrir quoi)', gap: 2")
r("label: 'Breach response plan / who to tell', gap: 3", "label: 'Plan d\u2019intervention en cas d\u2019atteinte / qui aviser', gap: 3")
r("label: 'Data retention schedule', gap: 2", "label: 'Calendrier de conservation des données', gap: 2")
r("label: 'Vendor list (where client data goes)', gap: 2", "label: 'Liste des fournisseurs (où vont les données clients)', gap: 2")
r("label: 'Staff acceptable-use / device policy', gap: 1", "label: 'Politique d\u2019utilisation acceptable / des appareils pour le personnel', gap: 1")
r("label: 'Client data processing / processor agreements', gap: 2", "label: 'Ententes de traitement des données clients / sous-traitants', gap: 2")
r("text: 'What control hygiene practices are in place?'", "text: 'Quelles pratiques d\u2019hygiène des contrôles sont en place?'")
r("label: 'MFA on email / main suite'", "label: 'AMF sur le courriel / la suite principale'")
r("label: 'Shared passwords in use (RISK)'", "label: 'Mots de passe partagés en usage (RISQUE)'")
r("label: 'Former staff accounts cleaned up'", "label: 'Comptes des anciens employés nettoyés'")

# ---------- Layer 5 ----------
r("num: 5, name: 'Staff & Tools', icon: '👥',", "num: 5, name: 'Personnel et outils', icon: '👥',")
r('desc: \'Who does what on which tools? Where do people put files "just for a second"?\'',
  "desc: 'Qui fait quoi sur quels outils? Où les gens déposent-ils des fichiers « juste pour une seconde »?'")
r("pitch: 'Walk me through yesterday, tool by tool.'", "pitch: 'Décrivez-moi votre journée d\u2019hier, outil par outil.'")
r("text: 'Which roles are present in your organization? (Check and provide count for each)'",
  "text: 'Quels rôles sont présents dans votre organisation? (Cochez et indiquez le nombre pour chacun)'")
r("label: 'Owner / partner'", "label: 'Propriétaire / associé'")
r("label: 'Admin / office manager'", "label: 'Administration / directeur de bureau'")
r("label: 'Reception / front desk'", "label: 'Réception / accueil'")
r("label: 'Bookkeeper / finance'", "label: 'Teneur de livres / finances'")
r("label: 'Professional (lawyer, clinician, technician)'", "label: 'Professionnel (avocat, clinicien, technicien)'")
r("label: 'Field / mobile workers'", "label: 'Travailleurs sur le terrain / mobiles'")
r("label: 'IT / MSP external'", "label: 'TI / services gérés externes'")
r("text: 'For each role, what are the main tools and cloud dependencies?'",
  "text: 'Pour chaque rôle, quels sont les principaux outils et les dépendances infonuagiques?'")
r("{ id: 'main_tools', label: 'Main tools', type: 'text' }", "{ id: 'main_tools', label: 'Outils principaux', type: 'text' }")
r("{ id: 'cloud_dependent', label: 'Cloud-dependent?', type: 'select', options: ['Y', 'N', 'Partial'] }",
  "{ id: 'cloud_dependent', label: 'Dépendant du nuage?', type: 'select', options: ['O', 'N', 'Partiel'] }")
r("{ id: 'if_internet_dies', label: 'If internet dies...', type: 'text' }", "{ id: 'if_internet_dies', label: 'Si internet tombe...', type: 'text' }")
r("text: 'Are any of these shadow IT habits present?'", "text: 'L\u2019une de ces habitudes d\u2019informatique fantôme est-elle présente?'")
r("label: 'Personal Dropbox / Google for work files'", "label: 'Dropbox / Google personnel pour des fichiers de travail'")
r("label: 'Personal AI with client data'", "label: 'IA personnelle avec des données clients'")
r('label: \'USB sticks for "quick transfer"\'', "label: 'Clés USB pour des « transferts rapides »'")
r("label: 'Home computer for work files'", "label: 'Ordinateur personnel pour des fichiers de travail'")
r("{ id: 'no_shadow_known', label: 'None known', risk: 0 }", "{ id: 'no_shadow_known', label: 'Aucune connue', risk: 0 }")
r("label: 'Unknown / not asked yet'", "label: 'Inconnu / pas encore demandé'")

# ---------- JS UI strings ----------
r("`Layer ${layer.num} of ${total} — ${layer.name}`", "`Couche ${layer.num} sur ${total} — ${layer.name}`")
r("<div class=\"layer-badge\">Layer ${layer.num} / ${total} · ${layer.icon} ${layer.name}</div>",
  "<div class=\"layer-badge\">Couche ${layer.num} / ${total} · ${layer.icon} ${layer.name}</div>")
r('placeholder="Specify..."', 'placeholder="Précisez..."', 2)
r("placeholder=\"${opt.textLabel || 'Specify...'}\"", "placeholder=\"${opt.textLabel || 'Précisez...'}\"")
r("<option value=\"\">-- Select --</option>", "<option value=\"\">-- Sélectionnez --</option>")
r('Select data types in the previous question to populate this table.', 'Sélectionnez des types de données à la question précédente pour remplir ce tableau.')
r('placeholder="Notes / rough volume estimates"', 'placeholder="Notes / estimations approximatives du volume"')
r('<thead><tr><th>Document</th><th>Yes</th><th>No</th><th>Unknown</th><th>Current? (Y/N/U)</th></tr></thead>',
  '<thead><tr><th>Document</th><th>Oui</th><th>Non</th><th>Inconnu</th><th>À jour? (O/N/I)</th></tr></thead>')
r("<option value=\"yes\" ${current === 'yes' ? 'selected' : ''}>Yes</option>", "<option value=\"yes\" ${current === 'yes' ? 'selected' : ''}>Oui</option>")
r("<option value=\"no\" ${current === 'no' ? 'selected' : ''}>No</option>", "<option value=\"no\" ${current === 'no' ? 'selected' : ''}>Non</option>")
r("<option value=\"unknown\" ${current === 'unknown' ? 'selected' : ''}>Unknown</option>", "<option value=\"unknown\" ${current === 'unknown' ? 'selected' : ''}>Inconnu</option>")
r('Select roles in the previous question to populate this table.', 'Sélectionnez des rôles à la question précédente pour remplir ce tableau.')
r("html += '<th>Role</th>';", "html += '<th>Rôle</th>';")
r('placeholder="Count"', 'placeholder="Nombre"')
r("alert('Please answer all required questions before proceeding.');", "alert('Veuillez répondre à toutes les questions obligatoires avant de continuer.');")
r("'Generate Report →'", "'Générer le rapport →'")
r("'Next →'", "'Suivant →'")
r('<button class="btn btn-primary" id="btn-next" onclick="nextLayer()">Next →</button>',
  '<button class="btn btn-primary" id="btn-next" onclick="nextLayer()">Suivant →</button>')

# ---------- Scoring: layer names & gap text ----------
r("layer: 'Data', text:", "layer: 'Données', text:", 2)
r("layer: 'Cloud & Services', text:", "layer: 'Nuage et services', text:", 3)
r("layer: 'Gear & Network', text:", "layer: 'Équipement et réseau', text:", 2)
r("layer: 'Compliance', text:", "layer: 'Conformité', text:", 3)
r("layer: 'Staff & Tools', text:", "layer: 'Personnel et outils', text:", 2)
r("`External access: ${opt.label}`", "`Accès externe : ${opt.label}`", 2)
r("`No workaround for cloud outage`", "`Aucune solution de rechange en cas de panne infonuagique`")
r("`Missing: ${r.label}`", "`Manquant : ${r.label}`", 2)

# ---------- Risk levels ----------
r("riskLevel = 'Low'; riskClass = 'risk-low'; riskDesc = 'Most controls in place. Minor gaps to address.';",
  "riskLevel = 'Faible'; riskClass = 'risk-low'; riskDesc = 'La plupart des contrôles sont en place. Lacunes mineures à corriger.';")
r("riskLevel = 'Moderate'; riskClass = 'risk-moderate'; riskDesc = 'Several gaps identified. Remediation plan recommended.';",
  "riskLevel = 'Modéré'; riskClass = 'risk-moderate'; riskDesc = 'Plusieurs lacunes identifiées. Plan de remédiation recommandé.';")
r("riskLevel = 'Elevated'; riskClass = 'risk-elevated'; riskDesc = 'Significant gaps across multiple layers. Priority remediation needed.';",
  "riskLevel = 'Élevé'; riskClass = 'risk-elevated'; riskDesc = 'Lacunes importantes sur plusieurs couches. Remédiation prioritaire nécessaire.';")
r("riskLevel = 'High'; riskClass = 'risk-high'; riskDesc = 'Critical gaps identified. Immediate action required.';",
  "riskLevel = 'Critique'; riskClass = 'risk-high'; riskDesc = 'Lacunes critiques identifiées. Action immédiate requise.';")

# ---------- Report ----------
r("toLocaleDateString('en-CA')", "toLocaleDateString('fr-CA')", 2)
r('<div>Document classification: Confidential</div>', '<div>Classification du document : Confidentiel</div>')
r('<div>Prepared for: ${escapeHtml(state.orgName)}</div>', '<div>Préparé pour : ${escapeHtml(state.orgName)}</div>')
r('<div>Date: ${date}</div>', '<div>Date : ${date}</div>')
r('<div>Tier: ${tier.name}</div>', '<div>Niveau : ${tier.name}</div>')
r('margin-top:2px">Make it work.</div>', 'margin-top:2px">Faites que ça marche.</div>')
r('<div class="card-title">Executive Summary</div>', '<div class="card-title">Résumé</div>')
r('<strong>Audited organization:</strong>', '<strong>Organisation évaluée :</strong>')
r('<strong>Auditor:</strong>', '<strong>Auditeur :</strong>')
r('<strong>Industry profile:</strong>', '<strong>Profil d\u2019industrie :</strong>')
r('<strong>Applicable frameworks:</strong>', '<strong>Cadres applicables :</strong>', 2)
r("'None identified'", "'Aucun identifié'")
r('<div class="result-label">Overall Risk Level</div>', '<div class="result-label">Niveau de risque global</div>')
r('Total risk score: ${score.totalRisk} points', 'Score de risque total : ${score.totalRisk} points')
r('>High Risk</div>', '>Risque critique</div>')
r('>Medium Risk</div>', '>Risque moyen</div>')
r('>Low Risk</div>', '>Risque faible</div>')
r('<h3>1. Data Inventory</h3>', '<h3>1. Inventaire des données</h3>')
r('<strong>Data types identified:</strong>', '<strong>Types de données identifiés :</strong>')
r('<em>Notes: ${escapeHtml(notes)}</em>', '<em>Notes : ${escapeHtml(notes)}</em>')
r('<h3>2. Cloud Dependency Map</h3>', '<h3>2. Carte des dépendances infonuagiques</h3>')
r('<strong>Active cloud services:</strong>', '<strong>Services infonuagiques actifs :</strong>')
r('<strong>What stops if cloud goes down:</strong>', '<strong>Ce qui s\u2019arrête si le nuage tombe :</strong>')
r('<strong>Workaround exists:</strong>', '<strong>Solution de rechange :</strong>')
r('<h3>3. Equipment & Network</h3>', '<h3>3. Équipement et réseau</h3>')
r('<h3>4. Compliance Gap Analysis</h3>', '<h3>4. Analyse des lacunes de conformité</h3>')
r('<thead><tr><th>Document</th><th>Status</th><th>Gap severity</th></tr></thead>',
  '<thead><tr><th>Document</th><th>Statut</th><th>Gravité de la lacune</th></tr></thead>')
r("sevLabel = g.gap >= 3 ? 'Critical' : 'Notable';", "sevLabel = g.gap >= 3 ? 'Critique' : 'Notable';")
r("${g.status === 'unknown' ? 'Unknown' : 'Missing'}", "${g.status === 'unknown' ? 'Inconnu' : 'Manquant'}")
r('All compliance documents are in place.', 'Tous les documents de conformité sont en place.')
r('<strong>Control hygiene:</strong>', '<strong>Hygiène des contrôles :</strong>')
r('<h3>5. Staff Workflow Assessment</h3>', '<h3>5. Évaluation des flux de travail du personnel</h3>')
r('<strong>Roles:</strong>', '<strong>Rôles :</strong>')
r('<strong>Shadow IT / risk habits:</strong>', '<strong>Informatique fantôme / habitudes à risque :</strong>')
r('<h3>6. Risk Assessment</h3>', '<h3>6. Évaluation des risques</h3>')
r('No significant risks identified.', 'Aucun risque important identifié.')
r('<h3>7. Prioritized Recommendations</h3>', '<h3>7. Recommandations prioritaires</h3>')
r('<h4>Want a Professional Review?</h4>', '<h4>Vous voulez un examen professionnel?</h4>')
r('This self-assessment gives you a clarity map. For a full-service audit with on-site review, deployment planning, and Local Vault specification, elect-rix offers professional audits starting at $2,000.',
  'Cette auto-évaluation vous donne une carte de clarté. Pour un audit complet avec examen sur place, planification de déploiement et spécification Local Vault, elect-rix offre des audits professionnels à partir de 2 000 $.')
r('<strong>Disclaimer:</strong> This self-assessment produces a clarity map, not a compliance certification. Not legal advice. Not a penetration test. Based on information provided by the respondent. For regulatory confirmation, consult a qualified lawyer or privacy officer.',
  '<strong>Avertissement :</strong> Cette auto-évaluation produit une carte de clarté, pas une certification de conformité. Ceci n\u2019est pas un avis juridique. Ceci n\u2019est pas un test d\u2019intrusion. Basé sur les renseignements fournis par le répondant. Pour une confirmation réglementaire, consultez un avocat qualifié ou un responsable de la protection de la vie privée.')
r('Generated by elect-rix Audit Self-Assessment Tool ·', 'Généré par l\u2019outil d\u2019auto-évaluation elect-rix ·')
r('<title>elect-rix Audit Report — ${escapeHtml(state.orgName)} — ${date}</title>',
  '<title>Rapport d\u2019évaluation elect-rix — ${escapeHtml(state.orgName)} — ${date}</title>')
r('a.download = `elect-rix-audit-${date}-${state.orgName.replace', 'a.download = `elect-rix-evaluation-${date}-${state.orgName.replace')

# ---------- Recommendations: branch matchers + text ----------
r("g.text.includes('Former staff')", "g.text.includes('anciens employés')")
r("g.text.includes('Personal AI')", "g.text.includes('IA personnelle')")
r("g.text.includes('Personal Dropbox')", "g.text.includes('Dropbox')")
r("g.text.includes('No formal backup')", "g.text.includes('Aucune sauvegarde')")
r("g.text.includes('No workaround')", "g.text.includes('Aucune solution de rechange')")
r("g.text.includes('Shared passwords')", "g.text.includes('Mots de passe partagés')")
r("g.text.includes('breach')", "g.text.includes('atteinte')")
r(r"g.text.includes('Unknown')", "g.text.includes('Inconnu')")
r("g.text.includes('Missing:')", "g.text.includes('Manquant')")
r("g.text.replace('Missing: ', '')", "g.text.replace('Manquant : ', '')")
r("detail = 'Audit and deactivate all former staff accounts immediately. Review access logs for unusual activity.';",
  "detail = 'Auditez et désactivez immédiatement tous les comptes des anciens employés. Examinez les journaux d\u2019accès pour détecter toute activité inhabituelle.';")
r("detail = 'Establish an AI usage policy. Prohibit personal AI accounts for work data. Consider a Local Vault with RixBot for controlled AI.';",
  "detail = 'Établissez une politique d\u2019utilisation de l\u2019IA. Interdisez les comptes d\u2019IA personnels pour les données de travail. Envisagez un Local Vault avec RixBot pour une IA contrôlée.';")
r("detail = 'Migrate work files from personal cloud accounts to organization-controlled storage.';",
  "detail = 'Migrez les fichiers de travail des comptes infonuagiques personnels vers un stockage contrôlé par l\u2019organisation.';")
r("detail = 'Implement a 3-2-1 backup strategy immediately: 3 copies, 2 media, 1 offsite.';",
  "detail = 'Mettez en place immédiatement une stratégie de sauvegarde 3-2-1 : 3 copies, 2 supports, 1 hors site.';")
r("detail = 'Document a business continuity plan for cloud outages. Consider local-first alternatives for critical functions.';",
  "detail = 'Documentez un plan de continuité des activités pour les pannes infonuagiques. Envisagez des solutions locales d\u2019abord pour les fonctions critiques.';")
r("detail = 'Deploy a password manager and enforce individual accounts. Eliminate shared credentials.';",
  "detail = 'Déployez un gestionnaire de mots de passe et imposez des comptes individuels. Éliminez les identifiants partagés.';")
r("detail = 'Draft a breach response plan immediately. Identify who must be notified, in what order, and within what timeframe.';",
  "detail = 'Rédigez immédiatement un plan d\u2019intervention en cas d\u2019atteinte. Identifiez qui doit être avisé, dans quel ordre et dans quel délai.';")
r(r"detail = 'Investigate and document. Unknown risks are unmanaged risks — you cannot protect what you haven\'t mapped.';",
  "detail = 'Enquêtez et documentez. Les risques inconnus sont des risques non gérés — vous ne pouvez pas protéger ce que vous n\u2019avez pas cartographié.';")
r("detail = 'Address this gap as a priority. See elect-rix for a professional audit and remediation plan.';",
  "detail = 'Corrigez cette lacune en priorité. Consultez elect-rix pour un audit professionnel et un plan de remédiation.';")
r("recs.push({ text: `Address: ${g.text}`, priority: 'high', detail });", "recs.push({ text: `Corriger : ${g.text}`, priority: 'high', detail });")
r("recs.push({ text: `Review: ${g.text}`, priority: 'medium', detail });", "recs.push({ text: `Examiner : ${g.text}`, priority: 'medium', detail });")
r("detail = 'Review telemetry settings, disable unnecessary data collection, and evaluate whether a sovereign alternative (Local Vault) is appropriate.';",
  "detail = 'Examinez les paramètres de télémétrie, désactivez la collecte de données inutile et évaluez si une solution souveraine (Local Vault) convient.';")
r("detail = 'Evaluate whether desktop accounting or a Local Vault deployment would reduce data exposure.';",
  "detail = 'Évaluez si la comptabilité de bureau ou un déploiement Local Vault réduirait l\u2019exposition des données.';")
r("detail = `Draft or update: ${g.text.replace('Manquant : ', '')}. Use a template or engage elect-rix for documentation support.`;",
  "detail = `Rédiger ou mettre à jour : ${g.text.replace('Manquant : ', '')}. Utilisez un modèle ou retenez elect-rix pour du soutien en documentation.`;")
r("detail = 'Review and address. Schedule remediation within 30-60 days.';",
  "detail = 'Examinez et corrigez. Planifiez la remédiation dans les 30 à 60 jours.';")
r("recs.push({ text: 'Reduce cloud dependency', priority: 'medium', detail: 'Multiple cloud services create compound risk. Consider consolidating or deploying a Local Vault for critical operations.' });",
  "recs.push({ text: 'Réduire la dépendance au nuage', priority: 'medium', detail: 'Plusieurs services infonuagiques créent un risque composé. Envisagez de consolider ou de déployer un Local Vault pour les opérations critiques.' });")
r("recs.push({ text: 'Compliance documentation sprint', priority: 'high', detail: 'Multiple compliance documents missing. Recommend a focused documentation session or engaging elect-rix for a full audit.' });",
  "recs.push({ text: 'Sprint de documentation de conformité', priority: 'high', detail: 'Plusieurs documents de conformité manquent. Nous recommandons une séance de documentation ciblée ou de retenir elect-rix pour un audit complet.' });")
r('<span class="rec-priority ${r.priority}">${r.priority}</span>',
  '<span class="rec-priority ${r.priority}">${r.priority === \'high\' ? \'haute\' : \'moyenne\'}</span>')

# ---------- Apply ----------
src = SRC.read_text(encoding='utf-8')
errors = []
total = 0
for old, new, min_count in P:
    count = src.count(old)
    if count < min_count:
        errors.append(f"NOT FOUND ({count}<{min_count}): {old[:90]!r}")
    else:
        src = src.replace(old, new)
        total += count

if errors:
    print("FAILED — unmatched strings:")
    for e in errors: print(" ", e)
    sys.exit(1)

DST.parent.mkdir(parents=True, exist_ok=True)
DST.write_text(src, encoding='utf-8')
print(f"OK — {len(P)} rules, {total} replacements -> {DST}")
