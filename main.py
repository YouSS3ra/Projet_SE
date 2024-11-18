import subprocess
# Exécuter la commande 'ls' sur Linux
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Afficher le résultat
print(result.stdout)