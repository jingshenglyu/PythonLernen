# exception handling

try:
    print(10 / 8)
    print(10 + 'o')
    print(10 / 0)


except ArithmeticError as e:
    print(e)
except Exception:
    print("there is something wrong")

# Wenn es einen Fehler gibt, zeigt erster Fehler vor Ort.