text = "Иван Иванов"
print(text.istitle())
if not text.istitle():
    raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
else:
    print("норм")