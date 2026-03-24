from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def proyectos(request):
    data = [
        {
            "id": 1,
            "nombre": "Gestión Documental – Municipalidad de Coquimbo",
            "descripcion": "3 aplicaciones para automatización de procesos documentales con OCR.",
            "tecnologias": ["Python", "Django", "OpenCV", "Tesseract OCR"],
            "anio": "2025",
        },
        {
            "id": 2,
            "nombre": "ecoREPORT ITOs – Capstone",
            "descripcion": "Módulos de gestión de mantenimiento con flujos de trabajo.",
            "tecnologias": ["Yii2", "PHP", "MySQL", "AJAX"],
            "anio": "2025",
        },
        {
            "id": 3,
            "nombre": "Cartelera de Cine",
            "descripcion": "Interfaz frontend para sistema de gestión de cartelera.",
            "tecnologias": ["React Native", "Nest.js"],
            "anio": "2024",
        },
    ]
    return Response(data)