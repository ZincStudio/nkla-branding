# Guía de Despliegue — NKL Assistance Design System

> Última actualización: 14 de mayo de 2026

## 📦 Entrega al Cliente

### Opción rápida: solo el DESIGN.md
El archivo `DESIGN.md` es **100% standalone** para agentes de IA:
- Los 4 SVGs (logo, logo blanco, isotipo, isotipo blanco) están embebidos en base64
- Una IA como Claude, ChatGPT o Gemini puede **ver los logos** directamente
- Los tokens de color, tipografía y componentes viajan en el YAML del frontmatter
- **Solo falta alojar Intro** — es una fuente comercial, no está en Google Fonts. El .md recomienda Outfit como fallback

**Para compartir:** enviar el `DESIGN.md` solo, o comprimido en ZIP con la carpeta `design/assets/` para acceso a fuentes y vector editable (.ai).

---

## 🌐 Despliegue: brand.nklassistance.com

### Prerrequisitos
- Repo: `github.com/ZincStudio/nkla-branding` (privado)
- Token de GitHub con scopes: `repo` + `workflow`
- Acceso a DNS de `nklassistance.com`

### 1. GitHub — habilitar Pages con Actions
1. Ir a **github.com/ZincStudio/nkla-branding → Settings → Pages**
2. En **Source**, seleccionar **"GitHub Actions"**
3. El workflow ya está subido (`.github/workflows/deploy-pages.yml`), se ejecuta automáticamente en cada push a `main`

### 2. DNS — agregar CNAME
Donde se gestionen los DNS de `nklassistance.com`:

| Tipo | Nombre | Valor |
|------|--------|-------|
| CNAME | `brand` | `zincstudio.github.io` |

**Nota:** Si usas Cloudflare, desactivar el proxy (naranja → gris). GitHub Pages requiere tráfico directo.

### 3. Verificar
- Actions: **github.com/ZincStudio/nkla-branding/actions** — buscar workflow en verde
- Una vez propagado el DNS (5 min - 1 hr): abrir `https://brand.nklassistance.com`
- Debería mostrar el showcase con hero NKLA, paleta de colores, tabla de tokens, componentes y toggle ☀ ◐ ☾

### 4. Estructura del sitio desplegado
```
brand.nklassistance.com/
├── index.html              ← Showcase principal (Aura-style)
├── preview.html            ← Brand manual detallado
├── DESIGN.md               ← Spec fuente (descargable)
├── NKL-Assistance-DESIGN.md ← Copia del spec (descargable)
└── assets/
    ├── logo-nkla.svg
    ├── logo-nkla-white.svg
    ├── isotipo-nkla.svg
    ├── isotipo-nkla-white.svg
    ├── logos/NKL_Assistance.ai
    └── fonts/
        ├── INTRO ALT/      ← OTF + webfonts (woff, woff2)
        └── BASKERVILLE/    ← Baskerville.ttc
```

---

## 📂 Estructura Local (fuente de verdad)

```
proyectos/NKLA/
├── DESIGN.md                  ← Spec + logos embebidos (base64)
├── CNAME                      ← brand.nklassistance.com
├── .gitignore
└── design/
    ├── assets/
    │   ├── logo-nkla.svg
    │   ├── logo-nkla-white.svg
    │   ├── isotipo-nkla.svg
    │   ├── isotipo-nkla-white.svg
    │   ├── logos/             ← AI editable
    │   ├── patrones/          ← Para texturas futuras
    │   └── fonts/
    │       ├── INTRO ALT/
    │       └── BASKERVILLE/
    ├── impresion/guia-impresion.md
    ├── especificaciones/
    └── preview/
        ├── index.html         ← Showcase (Aura-style)
        └── preview.html       ← Brand manual detallado
```

---

## 🎯 Próximos Pasos

- [ ] Configurar DNS (CNAME `brand → zincstudio.github.io`)
- [ ] Verificar despliegue en `brand.nklassistance.com`
- [ ] (Opcional) Hostear webfonts de Intro en el mismo CDN para que cargue la fuente real
- [ ] Branding de Albatros — programa "Platinum Voyage Assistance" powered by NKL
