import json


def load_candidates():
    """Получает содержимое страницы в формате json и переводит в список"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    """Выводит всех кандидатов"""
    candidates_list = ''
    for item in load_candidates():
        candidates_list += f"{item['name']} -\n{item['position']}\n{item['skills']}\n\n"
    return candidates_list


def get_by_pk(pk):
    """Возвращает кандидатов по pk"""
    for item in load_candidates():
        if item['pk'] == pk:
            return f"<img src={item['picture']}>\n\n{item['name']} -\n{item['position']}\n{item['skills']}"


def get_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    candidates_list = ''
    skill_name = skill_name.lower()
    for item in load_candidates():
        skills = item['skills'].lower().split(', ')
        if skill_name in skills:
            candidates_list += f"{item['name']} -\n{item['position']}\n{item['skills']}\n\n"
    return candidates_list

    