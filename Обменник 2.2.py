#! Программа обменный пункт 2.2

usd = 58
euro = 65

while True:

	print ("Вас приветствует программа:\"Обменный пункт v2.2\"")
	print (f"В данный момент курс доллара к рублю: {usd}")
	print (f"В данный момент курс евро к рублю: {euro}")
	print ("Для выхода нажмите Y.")


	data = input ("Введите сумму для обмена: ")
	if data.lower () == "y":
		break # выход из цикла
	money = int (data)
	if money < 0:
		print ("Сумма должна быть положительной!")
		continue

	currency = int (input ("Укажите код валюты(доллары - 400, евро - 401): "))

	if currency == 400:
		cache = round (money / usd, 2)
		print ("Валюта: доллары США")
		print ("К выдаче", cache, "долларов.")
	elif currency == 401:
		cache = round (money / euro, 2)
		print ("Валюта: евро")
		print ("К выдаче", cache, "евро.")
	else:
		cashe = 0
		print ("Неизвестная валюта")

	print ("-----------------------------------------------------------------")

print ("Работа обменного пункта завершена.")