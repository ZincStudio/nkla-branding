# Guía de Impresión — NKL Assistance

> Última actualización: 14 de mayo de 2026
> Fuente de verdad cromática: DESIGN.md (YAML colors)

---

## Tarjetas de Presentación

| Especificación | Valor |
|---------------|-------|
| Tamaño final | 90 × 50 mm |
| Tamaño con sangrado | 96 × 56 mm (3 mm por lado) |
| Orientación | Horizontal |
| Acabado | Mate suave / Spot UV en logo |
| Colores | CMYK — ver perfiles abajo |
| Archivo fuente | `impresion/tarjeta-presentacion.ai` |
| Archivo entrega | `impresion/tarjeta-presentacion.pdf` |

## Hojas Membretadas

| Especificación | Valor |
|---------------|-------|
| Tamaño | Carta (216 × 279 mm) |
| Sangrado | 3 mm |
| Archivo fuente | `impresion/hoja-membretada.ai` |
| Archivo entrega | `impresion/hoja-membretada.pdf` |

## CMYK Profile

Basado en DESIGN.md. Aproximación estándar (consultar con imprenta):

| Token | HEX | CMYK (aproximado) | Pantone (referencia) |
|-------|-----|---------------------|----------------------|
| primary (navy) | #223D72 | C100 M70 Y10 K40 | 654 C |
| accent-primary (lime) | #E2E43C | C15 M0 Y85 K0 | 809 C |
| accent-secondary (orange-red) | #EB5826 | C0 M75 Y95 K0 | 1665 C |
| black | #000000 | C0 M0 Y0 K100 | Process Black |

> **Nota:** Estos valores CMYK son aproximaciones. Solicitar prueba de color física antes de tiraje final.

## Restricciones de Impresión

- El logo nunca se imprime en tamaños menores a 15 mm de ancho
- La versión a una tinta usa negro (K100) o blanco (papel) — nunca grises
- Fondo navy (#223D72) solo en papeles con cobertura de tinta suficiente (> 240%)
- Spot UV reservado exclusivamente para el isotipo / símbolo
