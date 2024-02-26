import json


API_INPUT = {
    "dimensao": {
        "altura": 102,
        "largura": 40
    },
    "peso": 400
}

DELIVERY_NINJA = {
    "nome": "Entrega Ninja",
    "dimensao": {
        "altura": range(10, 201),
        "largura": range(6, 141)
    },
    "frete": 0.3,
    "prazo": 6
}

DELIVERY_KABUM = {
    "nome": "Entrega Kabum",
    "dimensao": {
        "altura": range(5, 141),
        "largura": range(13, 126)
    },
    "frete": 0.2,
    "prazo": 4
}

CARRIERS = [DELIVERY_NINJA, DELIVERY_KABUM]


def shipping(weight: int, freight: float) -> None:
    total = (weight * freight) / 10
    return total


def term(days: int) -> None:
     return f"{days} dias"


def delivery(name: str, weight: int, freight: float, days: str ) -> dict:
    return {
                "nome": name,
                "frete": shipping(weight, freight),
                "prazo dias": term(days) 
            }      


if __name__ == "__main__":

    api_output = [] 

    try:
    
        if not all(map(lambda key_to_check: key_to_check in API_INPUT, ("dimensao", "peso"))):
            raise Exception("Não contém dimensão ou peso")

        if not all(map(lambda key_to_check: key_to_check in API_INPUT["dimensao"], ("altura", "largura"))):
            raise Exception("Não contém altura ou largura")
        
        dimension_input = API_INPUT["dimensao"]
        weight_input = API_INPUT["peso"]

        if (
            not isinstance(dimension_input["altura"], int) 
            or not isinstance(dimension_input["largura"], int)
            or not (isinstance(weight_input, int) and (weight_input > 0))
        ):
            raise Exception("Tipo inválido")
        
        for company in CARRIERS:

            if (dimension_input["altura"] in company["dimensao"]["altura"] and
                dimension_input["largura"] in company["dimensao"]["largura"]):
                api_output.append( 
                    delivery(company["nome"], weight_input, company["frete"], company["prazo"])
                )                      
                
    except Exception as exc:
        # Log
        print(exc) 

    finally: 
        # Return
        print(json.dumps(api_output, indent=4))
