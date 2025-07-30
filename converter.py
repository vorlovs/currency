import requests

def convert(amount: float, from_currency: str, to_currency: str, rates: dict, base_currency: str = "USD") -> float | None:
    try: 
        if from_currency == to_currency:
            return amount
        if from_currency == base_currency:
            return amount * rates[to_currency]
        else:
            base_amount = amount / rates[from_currency]
            return base_amount * rates[to_currency]
    except KeyError as e:
        return None