export const ui = {
  en: {
    nav: {
      home: 'Home',
      builds: 'Builds',
      blog: 'Blog',
      about: 'About',
      trust: 'Trust',
      safety: 'Safety',
      audit: 'Audit',
      report: 'Report',
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
      seeBuilds: 'See Builds →',
      getInTouch: 'Get in Touch',
      whyItMatters: 'Why it matters →',
    },
    home: {
      heroTitle: 'Make it work.',
      heroSubtitle: 'Trust you can verify.',
      heroBody:
        'Protect your data. Even when the lights go out. When the cloud drops, your systems shouldn\'t. When the audit comes, your data should be yours to account for. AI that works offline, leaks nothing, and proves it — built in, not bolted on.',
      builtDifferent: 'Built Different',
      builtDifferentBody1:
        'One builder. Dedicated infrastructure. Local LLM inference on owned hardware, not a cloud API with a quota. Everything is self-hosted, private, and runs offline by architecture.',
      builtDifferentBody2:
        'The AI industry builds for connectivity. I build for what happens when it fails. Resilience isn\'t a feature you add — it\'s architecture you commit to. Your data doesn\'t leave the box. Your systems don\'t drop when the cloud does. Your trust is verifiable, not taken on faith.',
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
            'Zero telemetry by design, not by configuration. Your data stays on your hardware. Audit every packet. Prove nothing leaves.',
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
      startAudit: 'Start with an audit, not an apology.',
      startAuditBody:
        'I help teams find the risks in their AI stack — cloud dependency, privacy leaks, compliance gaps — before a regulator, a breach, or a lawsuit does. If you already know you have a problem, we start there. If you want proof you don\'t, we find that too.',
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
      audit: 'Audit',
      report: 'Rapport',
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
      seeBuilds: 'Voir les builds →',
      getInTouch: 'Nous joindre',
      whyItMatters: 'Pourquoi ça compte →',
    },
    home: {
      heroTitle: 'Faites-le fonctionner.',
      heroSubtitle: 'Une confiance vérifiable.',
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
      startAudit: 'Commencez par un audit, pas des excuses.',
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
