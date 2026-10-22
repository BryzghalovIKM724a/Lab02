# stats_module.py
# Модуль із підпрограмами для статистичної обробки показників

import statistics


def get_average(data_dict):
    """Повертає середнє значення."""
    if not data_dict:
        return None

    values = list(data_dict.values())
    return sum(values) / len(values)


def get_min(data_dict):
    """Повертає мінімальне значення."""
    if not data_dict:
        return None

    return min(data_dict.values())


def get_max(data_dict):
    """Повертає максимальне значення."""
    if not data_dict:
        return None

    return max(data_dict.values())


def get_median(data_dict):
    """Повертає медіану."""
    if not data_dict:
        return None

    return statistics.median(data_dict.values())


def find_jumps(data_dict, threshold):
    """Знаходить різкі перепади між сусідніми значеннями."""
    jumps = []

    labels = list(data_dict.keys())
    values = list(data_dict.values())

    for i in range(1, len(values)):
        difference = abs(values[i] - values[i - 1])

        if difference > threshold:
            jumps.append((labels[i - 1], labels[i], difference))

    return jumps


def show_table(data_dict, title):
    """Виводить таблицю значень."""
    print(f"\n=== Таблиця показів: {title} ===")
    print("Мітка часу | Значення")

    for label, value in data_dict.items():
        print(f"{label:<10} | {value}")
