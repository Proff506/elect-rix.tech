export const ui = {
  en: {
    nav: {
      home: 'Home',
      builds: 'Builds',
      blog: 'Blog',
      about: 'About',
      trust: 'Trust',
      safety: 'Safety',
      audit: 'Legacy Audit',
      report: 'Hyperscaler Report',
      lab: 'Lab',
      contact: 'Contact',
    },
    footer: {
      rights: '© {year} elect-rix.tech',
      tagline: 'Resilience, privacy, trust — built in, not bolted on.',
    },
    lang: {
      label: 'Français',
      switchTo: 'fr',
    },
    available: 'Available for projects',
    cta: {
      seeBuilds: 'Read the Hyperscaler Report →',
      getInTouch: 'Discuss your exposure',
      whyItMatters: 'Why local-first matters →',
    },
    home: {
      heroTitle: 'Hyperscaler AI telemetry is not a footnote.',
      heroSubtitle: 'It is a risk surface.',
      heroBody:
        'I map where cloud AI systems send data, what vendors disclose, what remains ambiguous, and why local-first infrastructure matters when privacy, continuity, and jurisdiction are not optional.',
      builtDifferent: 'Built Different',
      builtDifferentBody1:
        'One builder. Dedicated infrastructure. Local LLM inference on owned hardware, not a cloud API with a quota. The target architecture is self-hosted, private, and able to keep working when external services fail.',
      builtDifferentBody2:
        'The AI industry builds for connectivity. I build for what happens when it fails. Resilience isn\'t a feature you add — it\'s architecture you commit to. Sensitive data stays under client control where possible. Systems should degrade gracefully when the cloud drops. Trust should be verifiable, not taken on faith.',
      whatIDo: 'What I Do',
      whatIDoBody: 'Not features. Principles. Every engagement starts with these four commitments.',
      services: {
        resilience: {
          title: 'Resilience Engineering',
          description:
            "AI systems that run when the cloud doesn't. Protected even when the lights go out.",
        },
        privacy: {
          title: 'Privacy Architecture',
          description:
            'Telemetry minimized and made visible by design, not hidden behind policy. Keep sensitive data on owned hardware. Audit the flows. Prove the boundary.',
        },
        trust: {
          title: 'Verifiable Trust',
          description:
            'Trust measured in logs, not promises. Inspectable behavior, transparent operations, and proof that your systems do exactly what they claim.',
        },
        integration: {
          title: 'Integration & Consulting',
          description:
            'From audit to deployment. Find the gaps in your AI stack — cloud dependency, telemetry leaks, compliance risks — and close them by design.',
        },
      },
      startAudit: 'Start with the report. Then decide what needs an audit.',
      startAuditBody:
        'The hyperscaler report is the advance scout: a public map of common telemetry, jurisdiction, and dependency risks. If it matches what you are worried about, I can help turn that concern into evidence and a practical Local Vault path.',
    },
  },
  fr: {
    nav: {
      home: 'Accueil',
      builds: 'Builds',
      blog: 'Blog',
      about: 'À propos',
      trust: 'Confiance',
      safety: 'Sécurité',
      audit: 'Audit ancien',
      report: 'Rapport hyperscalers',
      lab: 'Lab',
      contact: 'Contact',
    },
    footer: {
      rights: '© {year} elect-rix.tech',
      tagline: 'Résilience, confidentialité, confiance — intégrées, pas ajoutées.',
    },
    lang: {
      label: 'English',
      switchTo: 'en',
    },
    available: 'Disponible pour projets',
    cta: {
      seeBuilds: 'Lire le rapport hyperscalers →',
      getInTouch: 'Discuter de votre exposition',
      whyItMatters: 'Pourquoi le local-first compte →',
    },
    home: {
      heroTitle: 'La télémétrie IA hyperscaler n’est pas une note de bas de page.',
      heroSubtitle: 'C’est une surface de risque.',
      heroBody:
        'Protégez vos données. Même quand les lumières s\'éteignent. Quand le cloud tombe, vos systèmes ne devraient pas. Quand l\'audit arrive, vos données devraient être les vôtres à rendre compte. Une IA qui fonctionne hors ligne, ne fuit rien et le prouve — intégrée, pas ajoutée.',
      builtDifferent: 'Conçu différemment',
      builtDifferentBody1:
        'Un seul builder. Infrastructure dédiée. Inférence LLM locale sur matériel propriétaire, pas une API cloud avec quota. Tout est auto-hébergé, privé et fonctionne hors ligne par architecture.',
      builtDifferentBody2:
        'L\'industrie de l\'IA construit pour la connectivité. Je construis pour ce qui arrive quand elle échoue. La résilience n\'est pas une fonctionnalité qu\'on ajoute — c\'est une architecture à laquelle on s\'engage. Vos données ne quittent pas la boîte. Vos systèmes ne tombent pas quand le cloud tombe. Votre confiance est vérifiable, pas prise sur parole.',
      whatIDo: 'Ce que je fais',
      whatIDoBody:
        'Pas des fonctionnalités. Des principes. Chaque engagement commence avec ces quatre engagements.',
      services: {
        resilience: {
          title: 'Ingénierie de résilience',
          description:
            "Des systèmes d'IA qui fonctionnent quand le cloud ne fonctionne pas. Protégés même quand les lumières s'éteignent.",
        },
        privacy: {
          title: 'Architecture de confidentialité',
          description:
            "Zéro télémétrie par conception, pas par configuration. Vos données restent sur votre matériel. Auditez chaque paquet. Prouvez que rien ne sort.",
        },
        trust: {
          title: 'Confiance vérifiable',
          description:
            "Une confiance mesurée en journaux, pas en promesses. Comportement inspectable, opérations transparentes et preuve que vos systèmes font exactement ce qu'ils prétendent.",
        },
        integration: {
          title: 'Intégration et conseil',
          description:
            "De l'audit au déploiement. Trouvez les lacunes dans votre pile IA — dépendance au cloud, fuites de télémétrie, risques de conformité — et éliminez-les par conception.",
        },
      },
      startAudit: 'Commencez par le rapport. Décidez ensuite ce qui doit être audité.',
      startAuditBody:
        "J'aide les équipes à trouver les risques dans leur pile IA — dépendance au cloud, fuites de confidentialité, lacunes de conformité — avant qu'un régulateur, une brèche ou un procès ne le fasse. Si vous savez déjà que vous avez un problème, nous commençons là. Si vous voulez prouver que vous n'en avez pas, nous le trouvons aussi.",
    },
  },
} as const;

export type Lang = 'en' | 'fr';

export function useTranslations(lang: Lang) {
  return function t(key: string): string {
    const keys = key.split('.');
    let value: any = ui[lang];
    for (const k of keys) {
      value = value?.[k];
    }
    return typeof value === 'string' ? value : key;
  };
}
