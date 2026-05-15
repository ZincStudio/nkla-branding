# NKL Assistance — Brand Kit

Identidad visual de NKL Assistance. Diseñado para consumo humano y para agentes de IA generativa.

## Estructura

```
brand/
├── README.md                        ← Este archivo. Entry point.
├── spec-ia/                         ← Spec visual para IA
│   ├── index.html                   ← Viewer interactivo (doble clic)
│   └── spec/                        ← Descargables — spec en bruto
│       ├── DESIGN.md                ← Tokens de marca (fuente de verdad para IA)
│       ├── preview.html             ← Preview standalone
│       ├── tokens.json              ← Tokens en JSON
│       └── tokens.js                ← Tokens como variable JS
├── assets/                          ← Descargables (logos, isotipos, fuentes, patrones)
├── especificaciones/                ← Documentación técnica detallada
├── impresion/                       ← Guías de impresión (CMYK, Pantone, sangrados)
```

## Cómo usar

### Para ver la marca
Abrir `spec-ia/index.html` en el navegador. Muestra colores, tipografía, spacing y componentes con toggle claro/oscuro. Los botones descargan desde `spec/`.

### Para IA generativa
Incluir `spec-ia/spec/DESIGN.md` en el prompt de cualquier agente de IA generativa. Contiene la especificación completa de la marca en formato tokenizado.

### Para descargar assets
Desde el viewer (`spec-ia/index.html`) hay botones de descarga directa. También puedes acceder directamente a `assets/` o `spec-ia/spec/`.

---

*NKL Assistance — Professional trust meets compassionate service.*
