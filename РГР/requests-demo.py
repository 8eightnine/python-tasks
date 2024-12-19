import requests

def get_weather(city, lang='ru'):
    """
    Получение погоды для указанного города
    
    :param city: Название города
    :param lang: Язык ответа (ru, en и др.)
    :return: Словарь с информацией о погоде
    """
    try:
        # Формирование URL с параметрами
        url = f'https://wttr.in/{city}?format=j1&lang={lang}'
        
        # Установка пользовательского заголовка
        headers = {
            'User-Agent': 'PythonWeatherApp/1.0',
            'Accept': 'application/json'
        }
        
        # Выполнение GET-запроса с таймаутом
        response = requests.get(url, headers=headers, timeout=10)
        
        # Проверка успешности запроса
        response.raise_for_status()
        
        # Парсинг JSON-ответа
        weather_data = response.json()
        return weather_data
    
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при получении погоды: {e}')
        return None

def display_weather(weather_data):
    """
    Вывод информации о погоде
    
    :param weather_data: Словарь с данными о погоде
    """
    if not weather_data:
        print("Не удалось получить данные о погоде")
        return
    
    current = weather_data['current_condition'][0]
    location = weather_data['nearest_area'][0]
    
    print(f"Погода в городе {location['areaName'][0]['value']}:")
    print(f"Температура: {current['temp_C']}°C")
    print(f"Ощущается как: {current['FeelsLikeC']}°C")
    print(f"Влажность: {current['humidity']}%")
    print(f"Скорость ветра: {current['windspeedKmph']} км/ч")
    print(f"Осадки: {current['weatherDesc'][0]['value']}")

def get_weather_for_multiple_cities():
    """
    Демонстрация запросов для нескольких городов
    """
    cities = ['Moscow', 'Berlin', 'New York', 'Beijing']
    
    # Получение погоды для нескольких городов
    for city in cities:
        print(f"\n{'='*20}")
        weather = get_weather(city)
        if weather:
            display_weather(weather)

def main():
    # 1. Получение погоды для одного города с обработкой ошибок
    moscow_weather = get_weather('Novosibirsk')
    if moscow_weather:
        display_weather(moscow_weather)
    
    # 2. Получение погоды для нескольких городов
    get_weather_for_multiple_cities()
    
if __name__ == "__main__":
    main()
