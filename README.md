# e-cycle · Memoria de Título (versión web)

Memoria del Proyecto de Título de Amaro Latoja (Diseño Digital Profesional, INACAP, 2026).

- `index.html`: la memoria publicada, un solo archivo autocontenido.
- `src/`: fuente. `content.md` tiene el texto por capítulo; `blocks.py` y `diagrams*.py`, los diagramas y componentes; `template.html`, los estilos y scripts.

## Generar

```bash
pip install markdown
python3 src/build.py   # escribe index.html
```

## Publicar

Es un sitio estático: Vercel lo publica sin configuración (Framework Preset: Other, sin comando de build, directorio raíz `.`).

El producto vive en otro repositorio: [MR-Thunderbolts/E-Cycle](https://github.com/MR-Thunderbolts/E-Cycle) · [e-cycle-tau.vercel.app](https://e-cycle-tau.vercel.app).
