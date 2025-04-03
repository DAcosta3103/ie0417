# Tarea 1

## 1. Herramientas de gestión de proyectos de software

A continuación, se analizan tres herramientas ampliamente utilizadas en la planificación, seguimiento y ejecución de proyectos de software: **Jira**, **Trello** y **GitHub Projects**.

### 1.1 Jira

**Descripción breve:**  
Jira, desarrollado por Atlassian, es un sistema de seguimiento de incidencias y gestión de proyectos que facilita la planificación, seguimiento y control de versiones de software.

**Principales funcionalidades:**
- Creación y gestión de tareas e incidencias.
- Tableros personalizables de Scrum y Kanban.
- Informes detallados para métricas de rendimiento.
- Amplia integración con herramientas de desarrollo.

**Relación con metodologías ágiles:**  
Jira permite implementar Scrum mediante la creación de sprints, backlog y tableros de seguimiento; así como Kanban, configurando el flujo continuo y límites WIP. Soporta ambas metodologías de forma nativa.

### 1.2 Trello

**Descripción breve:**  
Trello es una herramienta visual para la gestión de tareas que se basa en un sistema de tableros, listas y tarjetas, ideal para equipos que requieren organización sencilla y rápida.

**Principales funcionalidades:**
- Tableros colaborativos con tarjetas movibles.
- Etiquetas, fechas límite, listas de verificación y adjuntos.
- Automatización de tareas con Butler.
- Power-Ups para integrar otras plataformas.

**Relación con metodologías ágiles:**  
Trello puede adaptarse fácilmente a metodologías ágiles. Existen plantillas específicas para Scrum y Kanban, y se pueden configurar flujos personalizados según el marco de trabajo elegido.

### 1.3 GitHub Projects

**Descripción breve:**  
GitHub Projects es una funcionalidad integrada en GitHub que facilita la planificación y seguimiento de tareas directamente asociadas a repositorios de código.

**Principales funcionalidades:**
- Gestión de issues y pull requests como unidades de trabajo.
- Vistas tipo tabla, tablero Kanban y cronogramas.
- Campos personalizados y filtros avanzados.
- Integración con GitHub Actions para automatización.

**Relación con metodologías ágiles:**  
GitHub Projects se adapta bien a Kanban, al permitir seguimiento de flujo de trabajo por etapas. Puede emplearse en entornos Scrum con configuraciones específicas y scripts de automatización.

### 1.4 Comparación entre las herramientas

| Característica               | Jira                                                               | Trello                                                            | GitHub Projects                                                   |
|------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| **Facilidad de uso**         | Requiere curva de aprendizaje por su riqueza funcional             | Interfaz visual e intuitiva                                       | Simple para usuarios de GitHub                                    |
| **Integración**              | Altamente integrable (Bitbucket, Confluence, Slack, etc.)          | Mediante Power-Ups                                                | Nativa con repositorios y GitHub Actions                         |
| **Popularidad**              | Muy usada por equipos ágiles profesionales                         | Popular entre equipos interdisciplinarios                         | Común en proyectos open-source y equipos que usan GitHub         |
| **Soporte Scrum/Kanban**     | Soporte nativo y robusto para ambos marcos                         | Adaptable con plantillas y configuraciones                        | Principalmente orientado a Kanban, posible soporte para Scrum     |

> Referencias:
> - [Jira Software Guide - Atlassian](https://www.atlassian.com/software/jira/guides)
> - [Trello Scrum Guide](https://www.atlassian.com/blog/trello/how-to-scrum-and-trello-for-teams-at-work)
> - [GitHub Projects Overview](https://github.com/features/project-management)


## 2. Marco teórico profundo de Scrum y Kanban

### 2.1 Scrum

**Historia y origen:**  
Scrum fue definido por Ken Schwaber y Jeff Sutherland en los años 1990 como un marco para desarrollar y mantener productos complejos. Su primera aparición formal fue en 1995, y desde entonces ha sido refinado a través de la "Guía de Scrum". [Fuente](https://hbr.org/1986/01/the-new-new-product-development-game)

**Principios fundamentales:**
- Empirismo: el conocimiento se genera a partir de la experiencia.
- Transparencia, inspección y adaptación como pilares clave.
- Enfoque iterativo e incremental.

**Estructura del trabajo:**

- **Roles:**
  - *Product Owner:* maximiza el valor del producto.
  - *Scrum Master:* facilita el proceso Scrum y elimina impedimentos.
  - *Equipo de desarrollo:* profesionales multifuncionales que crean el incremento.

- **Artefactos:**
  - *Product Backlog:* lista priorizada de requisitos.
  - *Sprint Backlog:* tareas seleccionadas para un sprint.
  - *Incremento:* versión entregable del producto.

- **Ceremonias:**
  - *Sprint Planning:* planificación del trabajo del sprint.
  - *Daily Scrum:* reunión diaria de sincronización.
  - *Sprint Review:* revisión del producto entregado.
  - *Sprint Retrospective:* reflexión para mejorar el proceso.

**Ventajas:**
- Incrementos frecuentes de valor.
- Alta visibilidad del progreso.
- Adaptabilidad ante cambios.

**Limitaciones:**
- Requiere compromiso constante del equipo.
- Difícil de escalar sin experiencia.
- Puede generar sobrecarga en reuniones si mal implementado.

---

### 2.2 Kanban

**Historia y origen:**  
Kanban se originó en Toyota en la década de 1940 como parte del sistema Just-In-Time. Fue adaptado al desarrollo de software por David J. Anderson en los 2000s, como método de gestión del flujo de trabajo. [Fuente](https://kanbantool.com/kanban-guide/introduction)

**Principios fundamentales:**
- Visualización del trabajo.
- Límite del trabajo en progreso (WIP).
- Gestión del flujo y mejora continua.
- Políticas explícitas.

**Estructura del trabajo:**

- **Columnas:** representan los estados del flujo (por ejemplo: Pendiente, En progreso, Terminado).
- **Tarjetas:** representan unidades de trabajo (tareas, historias, bugs).
- **Límites WIP:** controlan la cantidad de trabajo activo en cada etapa.

**Ventajas:**
- Flexibilidad para adaptarse a cualquier flujo.
- Reducción de cuellos de botella.
- Transparencia del estado del proyecto.

**Limitaciones:**
- Menor estructura formal que Scrum.
- Requiere disciplina para limitar WIP.
- No prescribe roles ni eventos, lo que puede llevar a confusión sin guía.

---

### 2.3 Comparación entre Scrum y Kanban

Aunque ambos marcos buscan optimizar el trabajo en equipo y la entrega continua de valor, difieren significativamente en estructura, enfoque y nivel de formalidad. Scrum prescribe roles, eventos y artefactos específicos, lo cual lo hace ideal para entornos predecibles con ciclos definidos. Kanban, en cambio, ofrece un enfoque más flexible basado en la visualización del flujo de trabajo y la limitación del trabajo en progreso (WIP, como se vio en clase), lo que lo vuelve útil en contextos cambiantes o de mantenimiento continuo.

| Característica             | Scrum                                        | Kanban                                       |
|----------------------------|----------------------------------------------|----------------------------------------------|
| **Enfoque**                | Iterativo e incremental                      | Flujo continuo                                |
| **Roles definidos**        | Sí (Product Owner, Scrum Master, Equipo)     | No                                           |
| **Eventos establecidos**   | Sí (Daily, Review, Retrospective, Planning)  | No (opcional)                                |
| **Backlogs**               | Product y Sprint Backlog                     | No es obligatorio                            |
| **WIP limitado**           | Indirectamente, por capacidad del sprint     | Directamente, por columna                    |
| **Adaptabilidad**          | Alta en ciclos de sprint                     | Alta en tiempo real                          |

---

### 2.4 Reflexión sobre su aplicación en proyectos reales o estudiantiles

Scrum puede ser especialmente útil en proyectos estudiantiles con entregables frecuentes y equipos bien organizados, ya que promueve la planificación estructurada y la mejora continua. Se le pueden dar reportes semanales o bisemanales, por ejemplo, al profesor (quien sería como el cliente) para así ir midiendo el progreso. Por otro lado, Kanban resulta ideal cuando las tareas llegan de forma impredecible o en proyectos de mantenimiento, como suele suceder en la industria, ya que permite mayor flexibilidad.

Ambos enfoques son compatibles y pueden combinarse para ajustarse a las necesidades del equipo. La elección del marco dependerá del tipo de proyecto, experiencia del equipo y cultura organizacional. Al fin y al cabo la eficiencia o la correcta realización de proyectos dependerá más de las personas del equipio que del framework de trabajo qe elijan.

> Referencias:
> - [Scrum Guide – scrumguides.org](https://scrumguides.org/)
> - [Kanban Tool](https://kanbantool.com/kanban-guide)
> - [Scrum vs Kanban – Atlassian](https://www.atlassian.com/agile/kanban/kanban-vs-scrum)