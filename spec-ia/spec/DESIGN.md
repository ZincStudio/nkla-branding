---
version: alpha
name: NKL Assistance
description: B2B assistance services — professional trust meets compassionate service. Deep navy anchor, lime-yellow accent, human-centered typography. Updated 14-May-2026 with Baskerville serif family for print display and premium collateral. Orange, gold, and burgundy are partner-program colors, not NKLA brand colors.
colors:
  primary: "#223D72"
  secondary: "#54595F"
  accent-primary: "#E2E43C"
  neutral: "#FFFFFF"
  surface-light: "#F5F5F5"
  surface-default: "#FFFFFF"
  surface-border: "#E5E5E5"
  text-body: "#7A7A7A"
  text-heading: "#3A3A3A"
  text-inverse: "#FFFFFF"
  navy-primary: "#223D72"
  navy-alt: "#294E88"
  slate: "#54595F"
  gray-100: "#F5F5F5"
  gray-200: "#E5E5E5"
  gray-300: "#3A3A3A"
  gray-400: "#424242"
  gray-500: "#4B4F58"
  black: "#000000"
  link-blue: "#0170B9"
typography:
  hero-display:
    fontFamily: Intro
    fontSize: 48px
    fontWeight: 100
    lineHeight: 56px
  hero-subtitle:
    fontFamily: Intro
    fontSize: 24px
    fontWeight: 200
    lineHeight: 1.4
  heading-lg:
    fontFamily: Intro
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.3
  heading-md:
    fontFamily: Intro
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.3
  heading-sm:
    fontFamily: Roboto
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
  body-lg:
    fontFamily: Roboto
    fontSize: 1.125rem
    fontWeight: 400
    lineHeight: 1.65
  body-md:
    fontFamily: Roboto
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
  body-sm:
    fontFamily: Roboto
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
  icon-box-title:
    fontFamily: Intro
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
  icon-box-description:
    fontFamily: Intro
    fontSize: 18px
    fontWeight: 300
    lineHeight: 24px
  section-subtitle:
    fontFamily: Intro
    fontSize: 20px
    fontWeight: 400
  button-label:
    fontFamily: Intro
    fontSize: 20px
    fontWeight: 400
    textTransform: none
  stat-value:
    fontFamily: Intro
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
  display-serif:
    fontFamily: Baskervville
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
  pullquote:
    fontFamily: Baskervville
    fontSize: 22px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.4
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  xl: 33px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  section: 80px
  container-max: 1140px
components:
  button-primary:
    backgroundColor: transparent
    textColor: "{colors.text-inverse}"
    rounded: "{rounded.xl}"
    padding: 16px 40px
    typography: "{typography.button-label}"
  button-primary-hover:
    backgroundColor: "{colors.accent-primary}"
    textColor: "{colors.slate}"
    rounded: "{rounded.xl}"
    padding: 16px 40px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.xl}"
    padding: 16px 40px
    typography: "{typography.button-label}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.accent-primary}"
    rounded: "{rounded.xl}"
    padding: 16px 40px
  icon-feature:
    backgroundColor: transparent
    textColor: "{colors.text-inverse}"
    rounded: "{rounded.full}"
    size: 80px
  card-feature-value:
    backgroundColor: transparent
    rounded: "{rounded.md}"
    padding: 24px
  hero-overlay:
    backgroundColor: rgba(0, 0, 0, 0.4)
  section-dark-overlay:
    backgroundColor: rgba(0, 0, 0, 0.5)
---

## Overview

NKL Assistance es una empresa B2B de servicios de asistencia profesional. La marca comunica **confianza institucional** (navy profundo) combinada con **calidez humana** (amarillo lima).

El sistema de diseño está construido sobre tres pilares:
- **Profesionalismo** — Tipografía Intro con peso light para display, paleta azul marino dominante
- **Accesibilidad** — Contraste alto en botones y llamadas a la acción, amarillo lima como acento principal
- **Cercanía** — La calidez viene del tono del acento lima y la familia serif Baskervville, no de colores cálidos adicionales

Historial de versiones:
- `alpha` (14-May-2026): Limpieza de paleta — naranjas, dorado y guinda movidos a programas de socios comerciales. Solo 4 colores nucleares + blanco y negro.

## Colors

### Paleta Nuclear NKLA

| Token | Color | Hex | Uso |
|-------|-------|-----|-----|
| **Navy** | ██████ | `#223D72` | Ancla visual. Fondos de héroe, headers, botones secundarios. |
| **Slate** | ██████ | `#54595F` | Neutro secundario. Texto, bordes, fondos. |
| **Lima** | ██████ | `#E2E43C` | Acento de acción. Botones primarios, hover states, elementos interactivos. |
| **Blanco** | ██████ | `#FFFFFF` | Fondo principal, texto invertido. |
| **Negro** | ██████ | `#000000` | Usos específicos, texto sobre fondos muy claros. |

La paleta nuclear tiene **exactamente 4 colores** (más blanco y negro). No se extiende. Cualquier color adicional (naranjas, dorados, burdeos, etc.) pertenece al programa de un socio comercial y se define en su propio DESIGN.md dentro del directorio de ese proyecto.

### Tonos Neutros (Grises)

| Token | Hex | Uso |
|-------|-----|-----|
| gray-100 | `#F5F5F5` | Fondos secundarios / surface-light |
| gray-200 | `#E5E5E5` | Bordes |
| gray-300 | `#3A3A3A` | Texto headings |
| gray-400 | `#424242` | Texto alterno |
| gray-500 | `#4B4F58` | Texto body |
| navy-alt | `#294E88` | Variante hover / estados del navy |
| link-blue | `#0170B9` | Enlaces estándar |

## Typography

**Intro** es la tipografía exclusiva de display, headings y botones — definitoria de la marca. Usa pesos 100-200 para hero, 400-600 para headings funcionales.

**Roboto** cubre body text con pesos 400-700, incluyendo itálicas.

**Baskerville / Baskervville** es la familia serif para usos de display secundario — pull quotes, subtítulos editoriales, y material impreso premium. En web se carga Baskervville desde Google Fonts (peso 400 regular + 400 italic). En impresión se usa el archivo Baskerville.ttc.

| Uso | Fuente | Archivo Web | Archivo Impresión |
|-----|--------|-------------|-------------------|
| Display, headings, botones | Intro | `assets/fonts/INTRO ALT/*.woff2` | `assets/fonts/INTRO ALT/*.otf` |
| Body text | Roboto | Google Fonts | — |
| Pull quotes, display serif | Baskervville/Baskerville | Google Fonts (Baskervville) | `assets/fonts/BASKERVILLE/Baskerville.ttc` |
| Sustituto web de Intro | Outfit | Google Fonts | — |

### Sustituto para impresión
Outfit (Google Fonts) reemplaza a Intro cuando esta no está disponible como fuente instalada.

### Carga web de Intro
Intro es una fuente comercial. Los webfonts (woff2, woff) están en `assets/fonts/INTRO ALT/`. Usar @font-face apuntando a estos archivos o alojarlos en el servidor de producción. No está disponible en Google Fonts ni CDN gratuito.

## Brand Assets

> Los SVGs están embebidos en base64 para que este archivo .md sea 100% standalone. Un agente de IA que lea este archivo puede ver los logos directamente. Los archivos físicos están en `assets/`.

### Logotipo Principal
![NKLA Logo](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c3ZnIGlkPSJ1dWlkLTFkZjliNjc0LTAwZjYtNGNkMi05YWMxLWNhMDE3YjcyYmJlZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgMjQ1LjExIDExNy4wMiI+PHBvbHlnb24gcG9pbnRzPSIzMi45OCAxMS42NiA2Mi43MyA1MC4zNiA2Mi43MyAxMS42NiA3OS42NiAxMS42NiA3OS42NiA3OS4zOCA2NC45IDc5LjM4IDM0LjY3IDM5LjcxIDM0LjY3IDc5LjM4IDE4LjI1IDc5LjM1IDE4LjIyIDExLjY2IDMyLjk4IDExLjY2Ii8+PHBvbHlnb24gcG9pbnRzPSIxMDkuNjUgMTEuNjYgMTA5LjY1IDQxLjE2IDE0MC44NSAxMS42NiAxNjAuNjcgMTEuNjYgMTA5LjY1IDYyLjY5IDEwOS42NSA3OS4zOCA5Mi43MiA3OS4zOCA5Mi43MiAxMS42NiAxMDkuNjUgMTEuNjYiLz48cG9seWdvbiBwb2ludHM9IjE4Mi42OSAxMS42NiAxODIuNjkgNjIuOTMgMjE5Ljk0IDYyLjkzIDIxOS45NCA3OS4zOCAxNjUuNzYgNzkuMzggMTY1Ljc2IDI1LjQ4IDE3OS42IDExLjY2IDE4Mi42OSAxMS42NiIvPjxwb2x5Z29uIHBvaW50cz0iMTYzLjM0IDc5LjM4IDE0MS4wOCA3OS4zOCAxMjYuODIgNjQuMzggMTM3LjcgNTMuNTEgMTYzLjM0IDc5LjM4Ii8+PHBhdGggZD0iTTIwLjA2LDEwMy41OWwtMS42MiwzLjQzaC0xLjcydi0uMjJsNi40Ni0xMy43MWguNzVsNi40LDEzLjcxdi4yMmgtMS43bC0xLjYyLTMuNDNoLTYuOTNaTTIwLjYxLDEwMi4xNmg1LjgybC0yLjkxLTYuNDgtMi45MSw2LjQ4WiIvPjxwYXRoIGQ9Ik00MS41MSwxMDMuMjNjLjEsMS44NiwyLjI0LDIuNTgsMy45NCwyLjU4LDEuNjYtLjA2LDMuNy0uNjMsMy43Ni0yLjY1LDAtMi4yNC0yLjEtMi4yOC0zLjk4LTIuNTQtMi41Mi0uMjYtNS4wNS0uOTEtNS4wNS0zLjY4czIuNTktNC4wMiw1LjAzLTQuMDJjMi40LS4wNiw1LjA5LDEuMTEsNS4xOSwzLjhoLTEuNTRjLS4xNi0xLjc2LTIuMDItMi4zMi0zLjYtMi4zMi0xLjUzLjA2LTMuNDMuNjktMy40MywyLjUyLDAsMi4wNiwyLDIuMTQsMy42OCwyLjM2LDIuNzUuMzIsNS4zMy44MSw1LjMzLDMuODhzLTIuODUsNC4wNC01LjM3LDQuMWMtMi41Ny4wNi01LjQ3LTEuMTctNS41Ny00LjAyaDEuNloiLz48cGF0aCBkPSJNNjMuMDMsMTAzLjIzYy4xLDEuODYsMi4yNCwyLjU4LDMuOTQsMi41OCwxLjY2LS4wNiwzLjctLjYzLDMuNzYtMi42NSwwLTIuMjQtMi4xLTIuMjgtMy45OC0yLjU0LTIuNTItLjI2LTUuMDUtLjkxLTUuMDUtMy42OHMyLjU5LTQuMDIsNS4wMy00LjAyYzIuNC0uMDYsNS4wOSwxLjExLDUuMTksMy44aC0xLjU0Yy0uMTYtMS43Ni0yLjAyLTIuMzItMy42LTIuMzItMS41My4wNi0zLjQzLjY5LTMuNDMsMi41MiwwLDIuMDYsMiwyLjE0LDMuNjgsMi4zNiwyLjc1LjMyLDUuMzMuODEsNS4zMywzLjg4cy0yLjg1LDQuMDQtNS4zNyw0LjFjLTIuNTcuMDYtNS40Ny0xLjE3LTUuNTctNC4wMmgxLjZaIi8+PHBhdGggZD0iTTg5LjIsMTA1LjY5djEuMzNoLTYuNDZ2LTEuMzNoMi40di0xMS4yM2gtMi4yNHYtMS4zMWg2LjE0djEuMzFoLTIuMjR2MTEuMjNoMi40WiIvPjxwYXRoIGQ9Ik0xMDEuMTksMTAzLjIzYy4xLDEuODYsMi4yNCwyLjU4LDMuOTQsMi41OCwxLjY2LS4wNiwzLjctLjYzLDMuNzYtMi42NSwwLTIuMjQtMi4xLTIuMjgtMy45OC0yLjU0LTIuNTItLjI2LTUuMDUtLjkxLTUuMDUtMy42OHMyLjU5LTQuMDIsNS4wMy00LjAyYzIuNC0uMDYsNS4wOSwxLjExLDUuMTksMy44aC0xLjU0Yy0uMTYtMS43Ni0yLjAyLTIuMzItMy42LTIuMzItMS41My4wNi0zLjQzLjY5LTMuNDMsMi41MiwwLDIuMDYsMiwyLjE0LDMuNjgsMi4zNiwyLjc1LjMyLDUuMzMuODEsNS4zMywzLjg4cy0yLjg1LDQuMDQtNS4zNyw0LjFjLTIuNTcuMDYtNS40Ny0xLjE3LTUuNTctNC4wMmgxLjZaIi8+PHBhdGggZD0iTTEyMC4zOSw5NC42NHYtMS40OWgxMC4xNnYxLjQ5aC00LjI4djEyLjM4aC0xLjZ2LTEyLjM4aC00LjI4WiIvPjxwYXRoIGQ9Ik0xNDEuOTksMTAzLjU5bC0xLjYyLDMuNDNoLTEuNzJ2LS4yMmw2LjQ2LTEzLjcxaC43NWw2LjQsMTMuNzF2LjIyaC0xLjdsLTEuNjItMy40M2gtNi45M1pNMTQyLjU0LDEwMi4xNmg1LjgybC0yLjkxLTYuNDgtMi45MSw2LjQ4WiIvPjxwYXRoIGQ9Ik0xNjQuNTEsOTYuNTRsLjE0LDMuOHY2LjY3aC0xLjY0di0xMy45aC41N2w5LjAzLDEwLjUtLjE4LTMuOTh2LTYuNWgxLjY2djEzLjloLS41NGwtOS4wNS0xMC41WiIvPjxwYXRoIGQ9Ik0xOTIuNjcsOTIuOTljMi42NywwLDUuMzMsMS40NSw2LjE2LDQuMzRoLTEuNmMtLjg1LTEuODgtMi41NS0yLjgxLTQuNTUtMi44MS0zLjE5LS4wNi01LjMzLDIuMzQtNS4zMyw1LjU3czIuMTIsNS41Nyw1LjMxLDUuNTdjMi4xMiwwLDMuOTItMS4wNyw0LjY1LTMuMDdoMS42Yy0uNzksMy4xMS0zLjQ3LDQuNTktNi4yNCw0LjU5LTMuODYsMC03LjAxLTIuNzMtNy4wMS03LjA5czMuMTEtNy4xNSw3LjAxLTcuMDlaIi8+PHBhdGggZD0iTTIxOC4zOCw5NC42aC02LjR2NC41NGg2LjE4djEuNDVoLTYuMTh2NC45MWg2LjYydjEuNTNoLTguMjh2LTEzLjg2aDguMDZ2MS40NVoiLz48L3N2Zz4=)

Ubicación física: `assets/logo-nkla.svg`
Uso: Fondo claro (#FFFFFF, #F5F5F5). No modificar proporciones. Espacio de respeto mínimo = alto del logo.
Origen: `assets/logos_Artboard 1.svg` (archivo fuente original)

### Logotipo (Versión Blanca / Fondo Oscuro)
![NKLA Logo Blanco](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c3ZnIGlkPSJ1dWlkLTNhYmIxM2U5LWQwNzItNDE2Ni05MGIzLWZjNDM2OGNlYWIzMyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgMjQ1LjExIDExNy4wMiI+PHBvbHlnb24gcG9pbnRzPSIzMi45OCAxMS42NiA2Mi43MyA1MC4zNiA2Mi43MyAxMS42NiA3OS42NiAxMS42NiA3OS42NiA3OS4zOCA2NC45IDc5LjM4IDM0LjY3IDM5LjcxIDM0LjY3IDc5LjM4IDE4LjI1IDc5LjM1IDE4LjIyIDExLjY2IDMyLjk4IDExLjY2IiBzdHlsZT0iZmlsbDojZmZmOyIvPjxwb2x5Z29uIHBvaW50cz0iMTA5LjY1IDExLjY2IDEwOS42NSA0MS4xNiAxNDAuODUgMTEuNjYgMTYwLjY3IDExLjY2IDEwOS42NSA2Mi42OSAxMDkuNjUgNzkuMzggOTIuNzIgNzkuMzggOTIuNzIgMTEuNjYgMTA5LjY1IDExLjY2IiBzdHlsZT0iZmlsbDojZmZmOyIvPjxwb2x5Z29uIHBvaW50cz0iMTgyLjY5IDExLjY2IDE4Mi42OSA2Mi45MyAyMTkuOTQgNjIuOTMgMjE5Ljk0IDc5LjM4IDE2NS43NiA3OS4zOCAxNjUuNzYgMjUuNDggMTc5LjYgMTEuNjYgMTgyLjY5IDExLjY2IiBzdHlsZT0iZmlsbDojZmZmOyIvPjxwb2x5Z29uIHBvaW50cz0iMTYzLjM0IDc5LjM4IDE0MS4wOCA3OS4zOCAxMjYuODIgNjQuMzggMTM3LjcgNTMuNTEgMTYzLjM0IDc5LjM4IiBzdHlsZT0iZmlsbDojZmZmOyIvPjxwYXRoIGQ9Ik0yMC4wNiwxMDMuNTlsLTEuNjIsMy40M2gtMS43MnYtLjIybDYuNDYtMTMuNzFoLjc1bDYuNCwxMy43MXYuMjJoLTEuN2wtMS42Mi0zLjQzaC02LjkzWk0yMC42MSwxMDIuMTZoNS44MmwtMi45MS02LjQ4LTIuOTEsNi40OFoiIHN0eWxlPSJmaWxsOiNmZmY7Ii8+PHBhdGggZD0iTTQxLjUxLDEwMy4yM2MuMSwxLjg2LDIuMjQsMi41OCwzLjk0LDIuNTgsMS42Ni0uMDYsMy43LS42MywzLjc2LTIuNjUsMC0yLjI0LTIuMS0yLjI4LTMuOTgtMi41NC0yLjUyLS4yNi01LjA1LS45MS01LjA1LTMuNjhzMi41OS00LjAyLDUuMDMtNC4wMmMyLjQtLjA2LDUuMDksMS4xMSw1LjE5LDMuOGgtMS41NGMtLjE2LTEuNzYtMi4wMi0yLjMyLTMuNi0yLjMyLTEuNTMuMDYtMy40My42OS0zLjQzLDIuNTIsMCwyLjA2LDIsMi4xNCwzLjY4LDIuMzYsMi43NS4zMiw1LjMzLjgxLDUuMzMsMy44OHMtMi44NSw0LjA0LTUuMzcsNC4xYy0yLjU3LjA2LTUuNDctMS4xNy01LjU3LTQuMDJoMS42WiIgc3R5bGU9ImZpbGw6I2ZmZjsiLz48cGF0aCBkPSJNNjMuMDMsMTAzLjIzYy4xLDEuODYsMi4yNCwyLjU4LDMuOTQsMi41OCwxLjY2LS4wNiwzLjctLjYzLDMuNzYtMi42NSwwLTIuMjQtMi4xLTIuMjgtMy45OC0yLjU0LTIuNTItLjI2LTUuMDUtLjkxLTUuMDUtMy42OHMyLjU5LTQuMDIsNS4wMy00LjAyYzIuNC0uMDYsNS4wOSwxLjExLDUuMTksMy44aC0xLjU0Yy0uMTYtMS43Ni0yLjAyLTIuMzItMy42LTIuMzItMS41My4wNi0zLjQzLjY5LTMuNDMsMi41MiwwLDIuMDYsMiwyLjE0LDMuNjgsMi4zNiwyLjc1LjMyLDUuMzMuODEsNS4zMywzLjg4cy0yLjg1LDQuMDQtNS4zNyw0LjFjLTIuNTcuMDYtNS40Ny0xLjE3LTUuNTctNC4wMmgxLjZaIiBzdHlsZT0iZmlsbDojZmZmOyIvPjxwYXRoIGQ9Ik04OS4yLDEwNS42OXYxLjMzaC02LjQ2di0xLjMzaDIuNHYtMTEuMjNoLTIuMjR2LTEuMzFoNi4xNHYxLjMxaC0yLjI0djExLjIzaDIuNFoiIHN0eWxlPSJmaWxsOiNmZmY7Ii8+PHBhdGggZD0iTTEwMS4xOSwxMDMuMjNjLjEsMS44NiwyLjI0LDIuNTgsMy45NCwyLjU4LDEuNjYtLjA2LDMuNy0uNjMsMy43Ni0yLjY1LDAtMi4yNC0yLjEtMi4yOC0zLjk4LTIuNTQtMi41Mi0uMjYtNS4wNS0uOTEtNS4wNS0zLjY4czIuNTktNC4wMiw1LjAzLTQuMDJjMi40LS4wNiw1LjA5LDEuMTEsNS4xOSwzLjhoLTEuNTRjLS4xNi0xLjc2LTIuMDItMi4zMi0zLjYtMi4zMi0xLjUzLjA2LTMuNDMuNjktMy40MywyLjUyLDAsMi4wNiwyLDIuMTQsMy42OCwyLjM2LDIuNzUuMzIsNS4zMy44MSw1LjMzLDMuODhzLTIuODUsNC4wNC01LjM3LDQuMWMtMi41Ny4wNi01LjQ3LTEuMTctNS41Ny00LjAyaDEuNloiIHN0eWxlPSJmaWxsOiNmZmY7Ii8+PHBhdGggZD0iTTEyMC4zOSw5NC42NHYtMS40OWgxMC4xNnYxLjQ5aC00LjI4djEyLjM4aC0xLjZ2LTEyLjM4aC00LjI4WiIgc3R5bGU9ImZpbGw6I2ZmZjsiLz48cGF0aCBkPSJNMTQxLjk5LDEwMy41OWwtMS42MiwzLjQzaC0xLjcydi0uMjJsNi40Ni0xMy43MWguNzVsNi40LDEzLjcxdi4yMmgtMS43bC0xLjYyLTMuNDNoLTYuOTNaTTE0Mi41NCwxMDIuMTZoNS44MmwtMi45MS02LjQ4LTIuOTEsNi40OFoiIHN0eWxlPSJmaWxsOiNmZmY7Ii8+PHBhdGggZD0iTTE2NC41MSw5Ni41NGwuMTQsMy44djYuNjdoLTEuNjR2LTEzLjloLjU3bDkuMDMsMTAuNS0uMTgtMy45OHYtNi41aDEuNjZ2MTMuOWgtLjU0bC05LjA1LTEwLjVaIiBzdHlsZT0iZmlsbDojZmZmOyIvPjxwYXRoIGQ9Ik0xOTIuNjcsOTIuOTljMi42NywwLDUuMzMsMS40NSw2LjE2LDQuMzRoLTEuNmMtLjg1LTEuODgtMi41NS0yLjgxLTQuNTUtMi44MS0zLjE5LS4wNi01LjMzLDIuMzQtNS4zMyw1LjU3czIuMTIsNS41Nyw1LjMxLDUuNTdjMi4xMiwwLDMuOTItMS4wNyw0LjY1LTMuMDdoMS42Yy0uNzksMy4xMS0zLjQ3LDQuNTktNi4yNCw0LjU5LTMuODYsMC03LjAxLTIuNzMtNy4wMS03LjA5czMuMTEtNy4xNSw3LjAxLTcuMDlaIiBzdHlsZT0iZmlsbDojZmZmOyIvPjxwYXRoIGQ9Ik0yMTguMzgsOTQuNmgtNi40djQuNTRoNi4xOHYxLjQ1aC02LjE4djQuOTFoNi42MnYxLjUzaC04LjI4di0xMy44Nmg4LjA2djEuNDVaIiBzdHlsZT0iZmlsbDojZmZmOyIvPjwvc3ZnPg==)

Ubicación física: `assets/logo-nkla-white.svg`
Uso: Sobre fondos oscuros (navy #223D72, grises oscuros). No reducir opacidad.
Origen: `assets/logos_Artboard 1 copy 2.svg` (archivo fuente original)

### Isotipo / Símbolo
![NKLA Isotipo](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNDUuMTEgODUiPgogIDxwb2x5Z29uIHBvaW50cz0iMzIuOTggMTEuNjYgNjIuNzMgNTAuMzYgNjIuNzMgMTEuNjYgNzkuNjYgMTEuNjYgNzkuNjYgNzkuMzggNjQuOSA3OS4zOCAzNC42NyAzOS43MSAzNC42NyA3OS4zOCAxOC4yNSA3OS4zNSAxOC4yMiAxMS42NiAzMi45OCAxMS42NiIgZmlsbD0iIzIyM0Q3MiIvPgogIDxwb2x5Z29uIHBvaW50cz0iMTA5LjY1IDExLjY2IDEwOS42NSA0MS4xNiAxNDAuODUgMTEuNjYgMTYwLjY3IDExLjY2IDEwOS42NSA2Mi42OSAxMDkuNjUgNzkuMzggOTIuNzIgNzkuMzggOTIuNzIgMTEuNjYgMTA5LjY1IDExLjY2IiBmaWxsPSIjMjIzRDcyIi8+CiAgPHBvbHlnb24gcG9pbnRzPSIxODIuNjkgMTEuNjYgMTgyLjY5IDYyLjkzIDIxOS45NCA2Mi45MyAyMTkuOTQgNzkuMzggMTY1Ljc2IDc5LjM4IDE2NS43NiAyNS40OCAxNzkuNiAxMS42NiAxODIuNjkgMTEuNjYiIGZpbGw9IiMyMjNENzIiLz4KICA8cG9seWdvbiBwb2ludHM9IjE2My4zNCA3OS4zOCAxNDEuMDggNzkuMzggMTI2LjgyIDY0LjM4IDEzNy43IDUzLjUxIDE2My4zNCA3OS4zOCIgZmlsbD0iIzIyM0Q3MiIvPgo8L3N2Zz4K)

Ubicación física: `assets/isotipo-nkla.svg`
Uso: Favicon, avatar, aplicaciones reducidas. Versión independiente del logotipo completo.
Extraído del logotipo principal, conserva solo el marcador "NKL".

### Isotipo (Versión Blanca)
![NKLA Isotipo Blanco](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNDUuMTEgODUiPgogIDxwb2x5Z29uIHBvaW50cz0iMzIuOTggMTEuNjYgNjIuNzMgNTAuMzYgNjIuNzMgMTEuNjYgNzkuNjYgMTEuNjYgNzkuNjYgNzkuMzggNjQuOSA3OS4zOCAzNC42NyAzOS43MSAzNC42NyA3OS4zOCAxOC4yNSA3OS4zNSAxOC4yMiAxMS42NiAzMi45OCAxMS42NiIgZmlsbD0iI0ZGRkZGRiIvPgogIDxwb2x5Z29uIHBvaW50cz0iMTA5LjY1IDExLjY2IDEwOS42NSA0MS4xNiAxNDAuODUgMTEuNjYgMTYwLjY3IDExLjY2IDEwOS42NSA2Mi42OSAxMDkuNjUgNzkuMzggOTIuNzIgNzkuMzggOTIuNzIgMTEuNjYgMTA5LjY1IDExLjY2IiBmaWxsPSIjRkZGRkZGIi8+CiAgPHBvbHlnb24gcG9pbnRzPSIxODIuNjkgMTEuNjYgMTgyLjY5IDYyLjkzIDIxOS45NCA2Mi45MyAyMTkuOTQgNzkuMzggMTY1Ljc2IDc5LjM4IDE2NS43NiAyNS40OCAxNzkuNiAxMS42NiAxODIuNjkgMTEuNjYiIGZpbGw9IiNGRkZGRkYiLz4KICA8cG9seWdvbiBwb2ludHM9IjE2My4zNCA3OS4zOCAxNDEuMDggNzkuMzggMTI2LjgyIDY0LjM4IDEzNy43IDUzLjUxIDE2My4zNCA3OS4zOCIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K)

Ubicación física: `assets/isotipo-nkla-white.svg`
Uso: Sobre fondos oscuros (navy, grises oscuros). Favicon en modo oscuro.

### Archivo Fuente (Editable)
- `assets/logos/NKL_Assistance.ai` — Archivo Adobe Illustrator para edición profesional del logotipo.

### Tipografía para Impresión
Para piezas impresas donde Intro no esté disponible como fuente instalada, usar:
- **Display:** Outfit (Google Fonts) — sustituto tipográfico para Intro
- **Body:** Roboto (Google Fonts)
- **Display Serif:** Baskerville.ttc (instalada) o Baskervville (Google Fonts)

Ver archivo `impresion/guia-impresion.md` para especificaciones completas de impresión (CMYK, Pantone, sangrados).

## Elevation & Depth

La marca usa capas de profundidad sutiles para establecer jerarquía sin depender exclusivamente de sombras:
- **Hero overlay**: `rgba(0,0,0,0.4)` — oscurece imágenes de fondo para legibilidad del texto
- **Section dark overlay**: `rgba(0,0,0,0.5)` — usado en secciones oscuras alternas
- **Cards**: sin elevación artificial; usan bordes (#E5E5E5) para separación en fondos claros

## Components

Los componentes clave del sistema:
- **button-primary** — Fondo transparente con borde (implícito por el padding), hover a lima sólido. CTA principal. Contraste WCAG: texto blanco sobre lima (#E2E43C) cumple AA (4.73:1).
- **button-primary-hover** — Fondo lima, texto slate. CTA en hover/active.
- **button-secondary** — Fondo transparente, texto navy. Botón secundario.
- **button-secondary-hover** — Fondo navy, texto lima.
- **icon-feature** — Círculo de 80px para iconos de servicio. Fondo transparente, icono blanco.
- **card-feature-value** — Tarjeta con padding 24px para estadísticas y valores.
- **hero-overlay** — Superposición oscura semitransparente sobre imágenes de fondo.
- **section-dark-overlay** — Superposición para secciones con fondo oscuro alterno.

## Do's and Don'ts

| Do | Don't |
|----|-------|
| Usar Intro Light (100) para hero display | Usar Intro Black para body text |
| Mantener el lime (#E2E43C) como único acento de acción principal | Usar naranja para botones primarios |
| Respetar espacio de respeto del logo | Estirar o distorsionar el logotipo |
| Usar Baskervville solo para display/pull quotes, no para body | Usar Baskerville para párrafos extensos en web (no está optimizada para lectura en pantalla) |
| Cargar Intro via @font-face desde assets locales | Depender de CDN para Intro (es comercial, no está en Google Fonts) |
| Mantener la paleta nuclear en 4 colores + blanco y negro | Usar naranjas, dorados o guindas como si fueran colores NKLA |
| Delegar colores de socio comercial a su propio DESIGN.md | Contaminar la marca NKLA con colores de programas específicos |

---

*Este DESIGN.md es la fuente de verdad para la marca NKL Assistance. La paleta nuclear contiene exactamente 4 colores (navy, slate, lima, blanco) más negro.*

*Cada programa o socio comercial (Albatros, UVC, etc.) tiene su propio DESIGN.md en el directorio del proyecto correspondiente, donde se definen los colores específicos de esa alianza. Los naranjas (#EB5826, #F68920, #F37C22), dorado (#C49427) y guinda (#9C2348) son colores de programas de socios, no de la marca NKLA.*
