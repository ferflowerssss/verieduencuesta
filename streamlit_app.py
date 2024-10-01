import streamlit as st

# Función que procesa las respuestas y devuelve el arquetipo y recomendaciones
def procesar_resultado(respuestas):
    puntaje_total = sum(respuestas)
    
    if puntaje_total <= 30:
        return "El Líder Consciente", {
            "Fortalezas": "Empático, buen comunicador, mantiene la calma en situaciones difíciles.",
            "Áreas de mejora": "Delegar tareas más eficientemente y mejorar la toma de decisiones bajo presión.",
            "Webinar": "Liderazgo Tranquilo: Cómo inspirar a tu equipo desde la calma.",
            "Curso": "Gestión de Equipos y Delegación de Tareas.",
            "Recurso": "Guía de comunicación efectiva en el trabajo.",
            "Entrevista": "Cómo manejar el estrés como líder."
        }
    elif 31 <= puntaje_total <= 45:
        return "El Innovador Creativo", {
            "Fortalezas": "Proactivo, siempre busca aprender algo nuevo, creatividad alta.",
            "Áreas de mejora": "Tendencia a procrastinar en la toma de decisiones y manejar el estrés bajo presión.",
            "Webinar": "Innovación en Equipos: Potencia tu creatividad en el trabajo.",
            "Curso": "Solución de Problemas Complejos.",
            "Recurso": "Guía para fomentar la innovación personal.",
            "Entrevista": "Cómo ser un líder creativo en un entorno corporativo."
        }
    elif 46 <= puntaje_total <= 60:
        return "El Estratega Preciso", {
            "Fortalezas": "Gran capacidad de toma de decisiones y planificación, gestión del tiempo eficiente.",
            "Áreas de mejora": "Puede mejorar en la apertura a recibir feedback constructivo y flexibilidad en situaciones de cambio.",
            "Webinar": "Tomando decisiones efectivas bajo presión.",
            "Curso": "Gestión del tiempo y optimización personal.",
            "Recurso": "Plantilla de planificación estratégica diaria.",
            "Entrevista": "Cómo ser un líder estratégico en tiempos de cambio."
        }
    elif 61 <= puntaje_total <= 75:
        return "El Facilitador Empático", {
            "Fortalezas": "Excelente en relaciones interpersonales, gestionando conflictos y mediación.",
            "Áreas de mejora": "Delegación efectiva de tareas y mejora de habilidades de autogestión.",
            "Webinar": "Manejo de conflictos y mediación en equipos de trabajo.",
            "Curso": "Desarrollo de la inteligencia emocional.",
            "Recurso": "Guía para mantener relaciones laborales saludables.",
            "Entrevista": "Cómo resolver conflictos laborales con empatía."
        }
    else:
        return "El Líder Dinámico", {
            "Fortalezas": "Gran capacidad de liderazgo, toma de decisiones rápidas, multitarea eficiente.",
            "Áreas de mejora": "Mejorar el equilibrio entre la vida laboral y personal, gestión del estrés.",
            "Webinar": "Liderazgo en tiempos dinámicos.",
            "Curso": "Equilibrio entre vida laboral y personal para líderes.",
            "Recurso": "Guía para mantener el equilibrio emocional en el trabajo.",
            "Entrevista": "Cómo liderar en ambientes cambiantes."
        }

# Configuración de la aplicación en Streamlit
st.title("Evaluación Psicométrica Personalizada")

# Instrucciones
st.write("Responde a las siguientes preguntas del 1 al 5:")

# Preguntas del cuestionario
preguntas = [
    "¿Qué tan cómodo te sientes al tomar decisiones importantes bajo presión?",
    "¿Con qué frecuencia asumes un rol de liderazgo en tu equipo de trabajo?",
    "¿Cómo describirías tu capacidad para manejar el estrés en tu vida diaria?",
    "¿Qué tan importante es para ti aprender nuevas habilidades fuera del trabajo?",
    "¿Qué tan efectivas consideras tus habilidades de comunicación en situaciones laborales y personales?",
    "¿Con qué frecuencia logras un buen equilibrio entre tu vida personal y profesional?",
    "¿Cuánto te afecta emocionalmente un conflicto o desacuerdo en el trabajo?",
    "¿Qué tan abierto/a estás a recibir feedback o críticas constructivas?",
    "¿Sientes que gestionas adecuadamente tu tiempo entre tareas personales y laborales?",
    "¿Qué tan satisfecho/a estás con el progreso de tu desarrollo personal?",
    "¿Tiendes a evitar tomar decisiones hasta que es absolutamente necesario?",
    "¿Cómo describirías tu capacidad para resolver problemas complejos?",
    "¿Qué tan importante es para ti mantener relaciones interpersonales saludables en el trabajo?",
    "¿Qué tan efectivo/a te consideras en la delegación de tareas dentro de un equipo?",
    "¿Con qué frecuencia te propones metas personales y las sigues de manera disciplinada?"
]

# Guardar respuestas en una lista
respuestas = []
for i, pregunta in enumerate(preguntas, 1):
    respuesta = st.slider(f"{i}. {pregunta}", 1, 5, 3)
    respuestas.append(respuesta)

# Botón para procesar los resultados
if st.button("Calcular mi arquetipo"):
    arquetipo, recomendaciones = procesar_resultado(respuestas)
    
    st.subheader(f"Tu arquetipo es: {arquetipo}")
    
    # Mostrar fortalezas y áreas de mejora
    st.write(f"**Fortalezas**: {recomendaciones['Fortalezas']}")
    st.write(f"**Áreas de mejora**: {recomendaciones['Áreas de mejora']}")
    
    # Mostrar las recomendaciones
    st.write("### Recomendaciones para tu desarrollo:")
    st.write(f"- **Webinar**: {recomendaciones['Webinar']}")
    st.write(f"- **Curso**: {recomendaciones['Curso']}")
    st.write(f"- **Recurso descargable**: {recomendaciones['Recurso']}")
    st.write(f"- **Entrevista recomendada**: {recomendaciones['Entrevista']}")
