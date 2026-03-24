import pytest
from django.test import Client

@pytest.fixture
def client():
    return Client()

def test_proyectos_retorna_200(client):
    response = client.get('/api/proyectos/')
    assert response.status_code == 200

def test_proyectos_retorna_lista(client):
    response = client.get('/api/proyectos/')
    data = response.json()
    assert isinstance(data, list)

def test_proyectos_tiene_campos_correctos(client):
    response = client.get('/api/proyectos/')
    data = response.json()
    primer_proyecto = data[0]
    assert 'id' in primer_proyecto
    assert 'nombre' in primer_proyecto
    assert 'descripcion' in primer_proyecto
    assert 'tecnologias' in primer_proyecto
    assert 'anio' in primer_proyecto

def test_proyectos_no_esta_vacio(client):
    response = client.get('/api/proyectos/')
    data = response.json()
    assert len(data) > 0