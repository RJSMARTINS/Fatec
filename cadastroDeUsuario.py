import json

arquivo = open ("Db.csv", "a")

json.dump("Elefantebranco", arquivo)


arquivo.close()