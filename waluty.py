value = float(input("Podaj kwotę:"))
currency = input("Podaj kod waluty (eur,chf,usd):")
currency = currency.upper()

#kurs euro 4,71
#kurs dolara 4,34
#kurs franka 4,70


ratesdict = {
    "EUR": 4.71,
    "USD": 4.34,
    "CHF": 4.70
}

print(f"Kurs {currency} to: {ratesdict[currency]} zł.")
print(f"Kwota po przewalutowaniu to {value*ratesdict[currency]} zł.")
