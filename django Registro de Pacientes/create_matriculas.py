import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from core.models import Matricula

def criar_matriculas():
    matriculas = ['2024001', '2024002', '2024003', '2024004', '2024005']
    
    for numero in matriculas:
        matricula, created = Matricula.objects.get_or_create(
            numero=numero,
            defaults={'disponivel': True}
        )
        if created:
            print(f"Matrícula {numero} criada com sucesso!")
        else:
            print(f"Matrícula {numero} já existe!")

if __name__ == '__main__':
    criar_matriculas()