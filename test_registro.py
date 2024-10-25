def cuestionario():
    print("Bienvenido al cuestionario de registro de estudio")
    
    # Pregunta 1: Horas disponibles para estudiar
    expectativa_horas = int(input("¿Cuántas horas a la semana te gustaría dedicarle al estudio? "))

    # Pregunta 2: Trabajo
    tiene_trabajo = input("¿Tienes un trabajo? (sí/no): ").strip().lower()
    
    if tiene_trabajo == 'sí':
        horas_trabajo = int(input("¿Cuántas horas a la semana trabajas? "))
    else:
        horas_trabajo = 0

    # Pregunta 3: Actividades extracurriculares
    actividades_extracurriculares = input("¿Tienes actividades extracurriculares? (sí/no): ").strip().lower()
    
    if actividades_extracurriculares == 'sí':
        nueva_actividad ="si"
        actividades_nuevas = {}
        while nueva_actividad in ["si", "s"] :
            tipo_actividad_extra = ("Que tipo de actividad es?: ")
            horas_actividades = int(input("¿Cuántas horas a la semana dedicas a esta actividad? "))
            actividad_nueva = {
            "actividad": tipo_actividad_extra, 
            "cantidad_horas": horas_actividades
            }
            actividades_nuevas.append(actividad_nueva)
            nueva_actividad = input("¿Desea agregar otra actividad extracurricular? (si/no): ").lower()
        extra_total = sum(actividades_nuevas.values())
    else:
        horas_actividades = 0

    horas_dia = 24
    horas_sueño = 8
    tiempo_estudio= horas_dia - horas_trabajo - extra_total - horas_sueño

    # Resumen de respuestas
    print("\nResumen de tus respuestas:")
    print(f"Tu expectativa de tiempo de estudio son de {expectativa_horas} horas.")
    print(f"Horas trabajadas a la semana: {horas_trabajo} horas")
    print (f"la cantidad de horas que destinas a actividades extracurriculares es de: {extra_total} horas. ")
    print(f"La cantidad de horas que tenes disponibles en el día para estudiar son {tiempo_estudio}, suponiendo que descansas 8 horas por día.")


    # Análisis simple
 