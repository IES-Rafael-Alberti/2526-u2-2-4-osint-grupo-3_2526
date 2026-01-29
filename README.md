[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/uK91JyEB)
[Ir al informe (plantilla a completar)](informe/IS-2.d.01-Iniciales.md)

# IS 2.d.02 - OSINT (Auditoría pasiva)

Repositorio de entrega para la parte **(a) GRUPO: Auditoría de Superficie de Exposición Post-Incidente (OSINT pasivo)** sobre la *Clínica de San Rafael de Cádiz*.

## Reglas críticas (solo OSINT pasivo)

- Solo se consulta información ya pública (buscadores, archivos, redes, registros, repositorios, hemeroteca, etc.).
- Prohibido: escaneos de puertos, traceroute, intentos de login, fuerza bruta, inyección de tráfico, crawling agresivo, interacción directa con servidores/sistemas.
- Documentad fecha/hora, fuente y evidencia de cada hallazgo.
- Todas las evidencias que se incluyan deben quedar enlazadas en el informe (URL y/o ruta relativa a `evidencias/`).

## Estructura del repo

- `informe/IS-2.d.01-Iniciales.md`: informe (plantilla) con el proceso OSINT + resultados + conclusiones.
- `evidencias/`: capturas, PDFs públicos descargados, exportaciones (redactadas si procede).

## Cómo usar

1) Copiad/renombrad `informe/IS-2.d.01-Iniciales.md` con vuestras iniciales si lo necesitáis.
2) Rellenad la plantilla (priorizad hallazgos con impacto en ingeniería social, exposición de contactos y huella digital).
3) Guardad evidencias en `evidencias/` y enlazadlas desde el informe.
4) (Si el profesor exige PDF) exportad a `IS-2.d.01-Iniciales.pdf` manteniendo el límite: **máximo 6 folios (12 caras) para (a)**.

Sugerencia de exportación (si tenéis pandoc instalado y LaTeX):

```bash
pandoc informe/IS-2.d.01-Iniciales.md -o informe/IS-2.d.01-Iniciales.pdf
```

```bash
pandoc informe/IS-2.d.01-Iniciales.md -o informe/IS-2.d.01-Iniciales.pdf -V papersize=a4 -V geometry:margin=2.5cm
```
