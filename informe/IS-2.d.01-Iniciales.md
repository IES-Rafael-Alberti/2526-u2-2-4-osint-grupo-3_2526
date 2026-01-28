# IS 2.d.02 (a) - Auditoría de Superficie de Exposición Post-Incidente (OSINT pasivo)
<!-- AYUDA (BORRAR): Plantilla del informe. Rellenad los campos entre corchetes y eliminad todos los bloques "AYUDA (BORRAR)" antes de entregar. -->

- Entidad objetivo: Clínica de San Rafael de Cádiz
<!-- AYUDA (BORRAR): Nombre exacto del objetivo (como aparece en fuentes públicas). -->
- Equipo/Grupo: [Nombre del grupo]
<!-- AYUDA (BORRAR): Identificador del grupo/equipo. -->
- Integrantes: [Nombre Apellido (Iniciales)], [..]
<!-- AYUDA (BORRAR): Lista de integrantes (mismo orden que en la presentación). -->
- Fecha(s) de investigación: [YYYY-MM-DD a YYYY-MM-DD]
<!-- AYUDA (BORRAR): Rango de fechas reales en las que hicisteis las consultas OSINT. -->
- Versión: 1.0
<!-- AYUDA (BORRAR): Subid versión si hay revisiones (1.1, 1.2...). -->
- Límite de entrega (a): máximo 6 folios (12 caras) en PDF (si aplica)
<!-- AYUDA (BORRAR): Recordatorio del límite; podéis quitarlo si no os lo piden. -->

## 1. Resumen ejecutivo
<!-- AYUDA (BORRAR): 8-15 líneas. Debe entenderse sin leer el resto: qué se investigó, hallazgos top y acciones prioritarias. -->

**Objetivo.** Determinar qué información pública existía (antes del incidente supuesto) que podría haber facilitado la fase de reconocimiento de un atacante: identidades digitales, contactos, dominios/subdominios, huella documental (metadatos), menciones públicas y exposiciones derivadas.

**Hallazgos clave (3-7 bullets).**
<!-- AYUDA (BORRAR): Elegid solo lo más relevante (lo que facilita ingeniería social/reconocimiento). -->
- [Hallazgo 1 + por qué importa]
- [Hallazgo 2 + por qué importa]
- [Hallazgo 3 + por qué importa]

**Riesgo global (una frase).**
<!-- AYUDA (BORRAR): Un diagnóstico breve: nivel + causa principal. -->
- [Bajo/Medio/Alto] por [motivo principal].

**Recomendaciones prioritarias (3-5 bullets).**
<!-- AYUDA (BORRAR): Acciones concretas, medibles y alineadas con los hallazgos. -->
- [Acción 1]
- [Acción 2]
- [Acción 3]

## 2. Alcance, supuestos y reglas de compromiso
<!-- AYUDA (BORRAR): Dejad claro QUÉ se ha hecho y QUÉ no (para demostrar OSINT pasivo). Indicad supuestos y límites. -->

**Alcance.** Solo OSINT pasivo sobre la entidad (y su huella pública asociada). No se incluye investigación individual (apartado b).

**Fuentes permitidas (ejemplos).** Motores de búsqueda, hemeroteca, registros públicos, perfiles públicos en RRSS, repositorios públicos, documentos públicos, Wayback/archivos, bases de datos de brechas (consulta pasiva).
<!-- AYUDA (BORRAR): Listad las fuentes reales que usasteis (5-10), no un listado infinito. -->

**Regla crítica.** Prohibida cualquier acción activa: escaneos, enumeración directa de servicios, pruebas de login, interacción con formularios, generación de tráfico hacia los sistemas objetivo.
<!-- AYUDA (BORRAR): Si una herramienta pudiera considerarse “activa”, explicad cómo la usasteis de forma pasiva (solo consultas a datos ya recopilados por terceros). -->

**Minimización y privacidad.**
<!-- AYUDA (BORRAR): Explicad cómo reducís datos personales (enmascarado parcial, iniciales, no incluir PII innecesaria). -->
- Evitar incluir datos personales innecesarios.
- Si aparecen datos personales de terceros (p. ej., correos de empleados), aplicar reducción: mostrar solo lo imprescindible o enmascarar parcialmente cuando no aporte valor al riesgo.

## 3. Metodología (ciclo OSINT)
<!-- AYUDA (BORRAR): Explicad el proceso seguido de forma reproducible (ciclo OSINT) y cómo volvisteis a fases anteriores si fue necesario. -->

Esta sección describe el proceso seguido según el ciclo OSINT: planificación, fuentes, adquisición, procesamiento, análisis y difusión.

### 3.1 Planificación y dirección
<!-- AYUDA (BORRAR): Objetivos, preguntas guía y criterios de priorización. Esto demuestra teoría + método. -->

- Preguntas guía (ejemplos):
  - ¿Qué dominios y marcas usa la entidad?
  - ¿Existen patrones de email/usuarios visibles públicamente?
  - ¿Existen documentos públicos con metadatos reveladores?
  - ¿Hay menciones de tecnologías, proveedores, sedes, organigrama o personal?
  - ¿La entidad aparece asociada a brechas pasadas o leaks públicos?
<!-- AYUDA (BORRAR): Ajustad estas preguntas a lo que realmente investigasteis. -->

- Criterios de priorización:
  - Impacto potencial en ingeniería social.
  - Reutilización de credenciales/patrones.
  - Exposición de infraestructura por huella documental/histórica.
<!-- AYUDA (BORRAR): Indicad 2-4 criterios máximo y cómo los aplicasteis. -->

- Ventana temporal:
  - Consulta realizada en: [YYYY-MM-DD]
  - Evidencias archivadas en: `evidencias/` (todas deben quedar enlazadas en el informe).
<!-- AYUDA (BORRAR): Si usasteis Wayback, indicad el rango de años consultado. -->

### 3.2 Identificación de fuentes
<!-- AYUDA (BORRAR): Fuentes por categoría. Mejor pocas y justificadas. Indicad cómo se mantiene el enfoque pasivo. -->

Tabla de fuentes (añadir/quitar según aplique):
<!-- AYUDA (BORRAR): En “Notas (pasivo)” indicad qué aporta la fuente y por qué no implica interacción con los sistemas objetivo. -->

| Categoría   | Fuente/Herramienta                  | Qué se busca                | Notas (pasivo)              |
|-------------|-------------------------------------|-----------------------------|-----------------------------|
| Buscadores  | Google / Bing / DuckDuckGo          | menciones, PDFs, indexación | dorks sin acceder a paneles |
| Archivo web | Wayback Machine                     | versiones antiguas          | solo lectura                |
| Dominios    | WHOIS/RDAP (consulta)               | datos de registro           | solo consulta pública       |
| DNS pasivo  | dnsdumpster, securitytrails, etc.   | subdominios/histórico       | sin enumeración activa      |
| Brechas     | HIBP / DeHashed (si se usa)         | apariciones en brechas      | no intentar logins          |
| RRSS        | LinkedIn/X/Facebook (público)       | perfiles, roles, nicks      | solo contenido público      |
| Metadatos   | exiftool/FOCA (sobre docs públicos) | autores, rutas, software    | sobre ficheros públicos     |

### 3.3 Adquisición (recopilación)
<!-- AYUDA (BORRAR): Consultas representativas (no todas). Añadid palabras clave, variantes del nombre, ubicaciones, etc. -->

- Consultas realizadas (resumen):
  - [Query/dork 1]
  - [Query/dork 2]
  - [Query/dork 3]

- Evidencias:
  - Guardar capturas o PDFs en `evidencias/` con nombres: `YYYY-MM-DD_fuente_tema.ext`
  - Registrar URL (y, cuando sea útil, captura) y fecha de acceso en cada hallazgo.
  - Toda evidencia mencionada en el informe debe estar enlazada (URL y/o ruta relativa a `evidencias/`).
<!-- AYUDA (BORRAR): Si una URL cambia o desaparece, la captura/PDF en `evidencias/` es la prueba de trazabilidad. -->

### 3.4 Procesamiento y organización
<!-- AYUDA (BORRAR): Cómo ordenasteis datos: deduplicación, clasificación por categorías y relevancia, y control de calidad. -->

- Normalización:
  - Deduplicación de correos/teléfonos/dominios.
  - Agrupación por categoría (contacto, identidad, infra, documentos).

- Criterios de calidad:
  - Fiabilidad de la fuente (primaria vs. terciaria).
  - Fecha y vigencia (actual vs. histórico).
  - Corroboración cruzada (>= 2 fuentes cuando sea posible).
<!-- AYUDA (BORRAR): Indicad qué hallazgos NO pudisteis corroborar y por qué. -->

### 3.5 Análisis e interpretación
<!-- AYUDA (BORRAR): Transformad datos en “inteligencia”: vectores habilitados, probabilidad/impacto, y mitigación recomendada. -->

- Correlaciones (ejemplos):
  - Patrones de email + nombres de empleados + roles (posible spear phishing).
  - Documentos públicos -> metadatos -> nombres de usuario/software.
  - Dominios/subdominios históricos -> superficies olvidadas.
<!-- AYUDA (BORRAR): Añadid 2-5 correlaciones reales. Mejor pocas y buenas. -->

- Valoración de riesgo: usar una escala simple.
  - Alto: facilita acceso/engaño de alta probabilidad o alto impacto.
  - Medio: aporta información útil, pero requiere pasos adicionales.
  - Bajo: información marginal o muy genérica.
<!-- AYUDA (BORRAR): Justificad el riesgo con una frase (“Alto porque permite suplantación del canal X”, etc.). -->

### 3.6 Difusión
<!-- AYUDA (BORRAR): Explicad a quién va dirigido el informe y cómo se usará (priorizar mitigaciones y concienciación). -->

- Este informe resume hallazgos, evidencia y recomendaciones accionables.
- Presentación clara para audiencias técnicas y no técnicas.

## 4. Herramientas utilizadas
<!-- AYUDA (BORRAR): Incluid solo herramientas realmente usadas y una evidencia por cada una (URL o fichero en `evidencias/`). -->

| Herramienta   | Tipo                          | Uso concreto | Salida/evidencia               |
|---------------|-------------------------------|--------------|--------------------------------|
| [Herramienta] | [Buscador/DNS/Metadatos/etc.] | [Para qué]   | [archivo en evidencias/ o URL] |

## 5. Resultados (hallazgos)
<!-- AYUDA (BORRAR): Parte principal. Cada hallazgo debe ser verificable y tener evidencia enlazada (URL y/o `evidencias/...`). -->

Formato recomendado por hallazgo:
<!-- AYUDA (BORRAR): Copiad esta tabla por cada hallazgo importante (o adaptadla si preferís una tabla global). -->

| Campo           | Contenido                                                                  |
|-----------------|----------------------------------------------------------------------------|
| ID              | A-01                                                                       |
| Categoría       | Contacto / Identidad / Dominio-DNS / Documentos-Metadatos / RRSS / Brechas |
| Descripción     | [Qué se encontró, claro y verificable]                                     |
| Evidencia       | [URL] + `evidencias/...`                                                   |
| Fecha evidencia | [YYYY-MM-DD]                                                               |
| Impacto         | [Qué permite a un atacante]                                                |
| Riesgo          | Alto / Medio / Bajo                                                        |
| Recomendación   | [Mitigación concreta]                                                      |

### 5.1 Identidades digitales (nicks, perfiles, cuentas)
<!-- AYUDA (BORRAR): Perfiles corporativos, posibles empleados/roles (solo info pública), y “pivots” para ingeniería social. -->

- A-01
- A-02

### 5.2 Datos de contacto (emails, teléfonos, estructuras)
<!-- AYUDA (BORRAR): Patrones de correo (si se infieren), teléfonos publicados, extensiones, formularios de contacto y riesgos asociados. -->

- A-03
- A-04

### 5.3 Dominios, subdominios y huella DNS (pasivo)
<!-- AYUDA (BORRAR): Dominios oficiales/variantes y subdominios observados en fuentes pasivas/históricas. Evitad enumeración activa. -->

- A-05
- A-06

### 5.4 Huella documental y metadatos (documentos públicos)
<!-- AYUDA (BORRAR): Documentos públicos y metadatos relevantes (autor, software, rutas, fechas). Adjuntad evidencia. -->

- A-07
- A-08

### 5.5 Brechas y filtraciones (consulta pasiva)
<!-- AYUDA (BORRAR): Aparición del dominio/correos en brechas conocidas. No incluyáis contraseñas. Priorizad mitigaciones (2FA, rotación, etc.). -->

- A-09

## 6. Resumen de riesgos
<!-- AYUDA (BORRAR): Tabla para priorizar: qué arreglar primero (P1), después (P2) y al final (P3). -->

| ID   | Hallazgo (resumen) | Riesgo | Prioridad | Acción recomendada |
|------|--------------------|--------|-----------|--------------------|
| A-01 | [..]               | Alto   | P1        | [..]               |
| A-02 | [..]               | Medio  | P2        | [..]               |
| A-03 | [..]               | Bajo   | P3        | [..]               |

## 7. Conclusiones
<!-- AYUDA (BORRAR): 3-6 bullets: qué superficie pública existía y qué vector pudo facilitar. Sin repetir texto, aportad síntesis. -->

- [Conclusión 1: qué explica la exposición encontrada y por qué importa]
- [Conclusión 2]
- [Conclusión 3]

## 8. Recomendaciones
<!-- AYUDA (BORRAR): Convertid hallazgos en acciones concretas. Si podéis, asignad responsable sugerido (IT/Seguridad/RRHH/Comunicacion). -->

**Quick wins (0-30 días)**
<!-- AYUDA (BORRAR): Cambios rápidos: retirar/editar documentos, sanear metadatos, ajustar contenidos públicos, concienciación inmediata. -->
- [..]
- [..]

**Medio plazo (1-3 meses)**
<!-- AYUDA (BORRAR): Cambios estructurales: políticas de publicación, revisión periódica, procesos, formación, controles de identidad. -->
- [..]

**Mejora continua**
<!-- AYUDA (BORRAR): Medidas recurrentes: monitorización de menciones, revisiones trimestrales de exposición, playbook OSINT. -->
- [..]

## 9. Anexos
<!-- AYUDA (BORRAR): Trazabilidad. Esta sección facilita la corrección: fuentes, consultas y evidencias enlazadas. -->

### 9.1 Registro de fuentes
<!-- AYUDA (BORRAR): Fuentes base consultadas (URL + fecha). No hace falta duplicar cada evidencia si ya está en hallazgos, pero sí lo principal. -->

| Fuente   | URL  | Fecha acceso | Nota |
|----------|------|--------------|------|
| [Fuente] | [..] | [YYYY-MM-DD] | [..] |

### 9.2 Consultas (dorks) empleadas
<!-- AYUDA (BORRAR): Dejad 5-15 consultas representativas. Deben ser pasivas y reproducibles. -->

(Registrar aquí las consultas utilizadas. Evitar incluir acciones activas o instrucciones de acceso.)

- `site:[dominio] filetype:pdf [palabra clave]`
- `site:[dominio] "@[dominio]"`
- `"Clínica San Rafael" "Cádiz" [palabra clave]`

### 9.3 Evidencias (índice)
<!-- AYUDA (BORRAR): Índice con enlaces relativos a ficheros dentro de `evidencias/`. Debe permitir abrir cada evidencia sin buscar. -->

<!-- AYUDA (BORRAR): Ejemplo de enlace: `[2026-01-27 - Google - PDF organigrama](../evidencias/2026-01-27_google_organigrama.pdf)` -->

- `evidencias/`:
  - `YYYY-MM-DD_fuente_tema.ext` - [descripción]
