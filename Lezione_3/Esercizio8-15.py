def printing_models(models):
    for model in models:
        print(f"Eseguendo il modello {model}")

def show_completed_models(completed_models):
    print("\nI seguenti modelli sono stati importati:")
    for model in completed_models:
        print(model)

from printing_models import printing_models, show_completed_models

# Lista dei modelli da stampare
unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Usa le funzioni importate
printing_models(unprinted_models)
show_completed_models(completed_models)