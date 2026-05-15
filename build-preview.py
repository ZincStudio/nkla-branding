#!/usr/bin/env python3
"""
build-preview.py — Genera design/preview/tokens.json y tokens.js desde DESIGN.md

Uso:
  python3 build-preview.py

Lee el frontmatter YAML de DESIGN.md y genera:
  - tokens.json (para consumo programático)
  - tokens.js   (variable NKLA_TOKENS para carga local via <script>)
"""

import re
import yaml
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DESIGN_MD = os.path.join(ROOT, 'design', 'DESIGN.md')
OUTPUT_JSON = os.path.join(ROOT, 'design', 'preview', 'tokens.json')
OUTPUT_JS = os.path.join(ROOT, 'design', 'preview', 'tokens.js')

def resolve_ref(value, tokens):
    """Resuelve referencias estilo {colors.primary}"""
    if isinstance(value, str):
        m = re.match(r'\{([\w.-]+)\}', value)
        if m:
            parts = m.group(1).split('.')
            ref = tokens
            for p in parts:
                if p in ref:
                    ref = ref[p]
                else:
                    return value
            return str(ref) if not isinstance(ref, (dict, list)) else value
    return value

def build():
    with open(DESIGN_MD, 'r', encoding='utf-8') as f:
        raw = f.read()

    match = re.match(r'^---\s*\n(.*?)\n---', raw, re.DOTALL)
    if not match:
        raise ValueError('No se encontró frontmatter YAML')

    tokens = yaml.safe_load(match.group(1))

    # Resolver referencias en componentes
    components_raw = tokens.get('components', {})
    components = {}
    for name, spec in components_raw.items():
        resolved = {}
        for key, val in spec.items():
            if isinstance(val, str) and '{' in val:
                resolved[key] = resolve_ref(val, tokens)
            else:
                resolved[key] = val
        components[name] = resolved

    data = {
        'name': tokens.get('name', ''),
        'description': tokens.get('description', ''),
        'colors': tokens.get('colors', {}),
        'typography': tokens.get('typography', {}),
        'spacing': tokens.get('spacing', {}),
        'rounded': tokens.get('rounded', {}),
        'components': components,
    }

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)

    # tokens.json
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # tokens.js (variable global NKLA_TOKENS para <script>)
    js = 'var NKLA_TOKENS = ' + json.dumps(data, indent=2, ensure_ascii=False) + ';'
    with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
        f.write(js)

    print(f'✅ JSON: {OUTPUT_JSON}')
    print(f'✅ JS:   {OUTPUT_JS}')
    print(f'   {len(data["colors"])} colores · {len(data["typography"])} tipografías · {len(data["components"])} componentes')

if __name__ == '__main__':
    build()
