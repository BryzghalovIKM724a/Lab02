# lab02_main.py
# Основна програма для обробки показників системи "розумний будинок"

import stats_module as sm


def parse_input(input_str):
    """Перетворює введений рядок на список дійсних чисел (з перевіркою)."""
    try:
        values = input_str.split()
        numbers = []

        for value in values:
            numbers.append(float(value))

        return numbers

    except ValueError:
        print("Помилка: введено некоректні дані.")
        return None


def create_data_dict(temp_list, hum_list, pres_list):
    """Формує словник даних з мітками часу."""
    data = {
        "temperature": {},
        "humidity": {},
        "pressure": {}
    }

    for i in range(len(temp_list)):
        label = f"T{i + 1}"

        data["temperature"][label] = temp_list[i]
        data["humidity"][label] = hum_list[i]
        data["pressure"][label] = pres_list[i]

    return data


def process_measurements(title, data_dict, threshold):
    """Виводить таблицю та статистику для заданого виду даних."""

    sm.show_table(data_dict, title)

    average = sm.get_average(data_dict)
    minimum = sm.get_min(data_dict)
    maximum = sm.get_max(data_dict)
    median = sm.get_median(data_dict)
    jumps = sm.find_jumps(data_dict, threshold)

    print(f"\nСереднє значення: {average:.2f}")
    print(f"Мінімум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Медіана: {median}")

    if jumps:
        print("Різкі перепади:")
        for time1, time2, difference in jumps:
            print(f"між {time1} → {time2} ({difference:.1f})")
    else:
        print("Різкі перепади: не виявлено")


def main():
    print("=== Обробка показів системи 'Розумний будинок' ===")

    temp_input = input("Введіть температури (°C): ")
    hum_input = input("Введіть вологість (%): ")
    pres_input = input("Введіть тиск (Па): ")

    temp_list = parse_input(temp_input)
    hum_list = parse_input(hum_input)
    pres_list = parse_input(pres_input)

    if temp_list is None or hum_list is None or pres_list is None:
        return

    if len(temp_list) != len(hum_list) or len(temp_list) != len(pres_list):
        print("Помилка: кількість значень у всіх рядах повинна бути однаковою.")
        return

    data = create_data_dict(temp_list, hum_list, pres_list)

    process_measurements("Temperature", data["temperature"], 7)
    process_measurements("Humidity", data["humidity"], 20)
    process_measurements("Pressure", data["pressure"], 5000)


if __name__ == "__main__":
    main()
