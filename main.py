import http.client
import json

#Створюю коннект з планомвим api
conn = http.client.HTTPSConnection("chat-gpt26.p.rapidapi.com")

#Зтворюю квоту запит на api з моделю open ai та з повідомленням для створення диплому з його умовами
payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": '''
            Створити тему дипломної роботи, визначити мету, завдання, предмет, обʼєкт,
            актуальність, практичне значення, проаналізувати аналоги (2-3) та визначити потенційний стек проєкту з аргументацією вибору,
            відповідність 121 спеціальності. Документ повинен розкривати в цілому, ідею проекту.
            Може містити декілька сторінок. Обмежень по обʼєму немає.
            
            Оцінювання:
            Формулювання теми - 2
            Визначення мети та завдання - 3
            Предмет, Обʼєкт - 2
            Актуальність - 3
            Практичне значення - 1
            Аналоги - 2
            Потенційний стек - 2
            '''
		}
	]
}

headers = {
    'x-rapidapi-key': "6b060f05c7msh53183ba8b89206dp1a7d22jsn6a688890bc9f",
    'x-rapidapi-host': "chat-gpt26.p.rapidapi.com",
    'Content-Type': "application/json"
}

#Дані з словарю перетворюю у json 
json_payload = json.dumps(payload)

conn.request("POST", "", json_payload, headers)

res = conn.getresponse()
data = res.read()