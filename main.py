import json


API_INPUT = {
    "dimensao": {
        "altura": 102,
        "largura": 40
    },
    "peso": 400
}

ENTREGA_NINJA = {
    "dimensao": {
        "altura": range(10, 201),
        "largura": range(6, 141)
    },
    "frete": 0.3,
    "prazo": 6
}

ENTREGA_KABUM = {
    "dimensao": {
        "altura": range(5, 141),
        "largura": range(13, 126)
    },
    "frete": 0.2,
    "prazo": 4
}

if __name__ == "__main__":

    api_output = [] 

    try:
    
        if not all(map(lambda key_to_check: key_to_check in API_INPUT, ("dimensao", "peso"))):
            raise Exception("Não contém dimensão ou peso")

        if not all(map(lambda key_to_check: key_to_check in API_INPUT["dimensao"], ("altura", "largura"))):
            raise Exception("Não contém altura ou largura")
        
        dimensao = API_INPUT["dimensao"]
        peso = API_INPUT["peso"]

        if (
            not isinstance(dimensao["altura"], int) 
            or not isinstance(dimensao["largura"], int)
            or not (isinstance(peso, int) and (peso > 0))
        ):
            raise Exception("Tipo inválido")

        if (API_INPUT["dimensao"]["altura"] in ENTREGA_NINJA["dimensao"]["altura"] and 
            API_INPUT["dimensao"]["largura"] in ENTREGA_NINJA["dimensao"]["largura"]):
            api_output.append(
                {
                    "nome": "Entrega Ninja",
                    "frete": (API_INPUT["peso"] * ENTREGA_NINJA["frete"]) / 10,
                    "prazo_dias": f"{ENTREGA_NINJA['prazo']} dias"
                }
            )
            
        if (API_INPUT["dimensao"]["altura"] in ENTREGA_KABUM["dimensao"]["altura"] and 
            API_INPUT["dimensao"]["largura"] in ENTREGA_KABUM["dimensao"]["largura"]):
            api_output.append(
                {
                    "nome": "Entrega Kabum",
                    "frete": (API_INPUT["peso"] * ENTREGA_KABUM["frete"]) / 10,
                    "prazo_dias": f"{ENTREGA_KABUM['prazo']} dias"
                }
            )
        
    except Exception as exc:
        # Log
        print(exc) 

    finally: 
        # Return
        print(json.dumps(api_output, indent=4))
