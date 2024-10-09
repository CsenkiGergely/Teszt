def szamologep():
    print("Egyszerű számológép")
    print("Írd be az első számot:")
    szam1 = float(input())
    
    print("Írd be a második számot:")
    szam2 = float(input())
    
    print("Válassz egy műveletet (+, -, *, /):")
    muvelet = input()
    
    if muvelet == '+':
        eredmeny = szam1 + szam2
    elif muvelet == '-':
        eredmeny = szam1 - szam2
    elif muvelet == '*':
        eredmeny = szam1 * szam2
    elif muvelet == '/':
        if szam2 != 0:
            eredmeny = szam1 / szam2
        else:
            return "Hiba: osztás nullával nem lehetséges."
    else:
        return "Hiba: ismeretlen művelet."
    
    return f"Az eredmény: {eredmeny}"

# A számológép futtatása
print(szamologep())
