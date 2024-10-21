import os

# Génère une clé secrète de 24 octets (48 caractères hexadécimaux)
print(os.urandom(24).hex())