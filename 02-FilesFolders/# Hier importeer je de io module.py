# Hier importeer je de io module
import io

# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Een tekst naar het bestand schrijven
bestand2.write("Lekker alles overschrijven")

# Vergeet bestand niet te sluiten!
bestand.close()