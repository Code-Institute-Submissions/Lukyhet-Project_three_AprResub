import gspread
from google.oauth2.credentials import Credentials
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


def load_document():
    creds = Credentials.from_service_account_file('creds.json')
    scope = creds.with_scopes(SCOPE)
    client = gspread.authorize(scope)
    sheet = client.open('skincare_survey')
    return sheet

def get_age_range(survey1_sheets):
    values = survey1_sheets.col_values(1)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    age_values = get_age_range(survey)
    print(age_values)


def get_skin_type(survey1_sheets):
    values = survey1_sheets.col_values(2)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    type_values = get_skin_type(survey)
    print(type_values)


def get_cleanse_habit(survey1_sheets):
    values = survey1_sheets.col_values(3)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    cleanse_values = get_cleanse_habit(survey)
    print(cleanse_values)


def get_sunscreen_habit(survey1_sheets):
    values = survey1_sheets.col_values(4)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    sunscreen_values = get_sunscreen_habit(survey)
    print(sunscreen_values)


def get_routine_adjust(survey1_sheets):
    values = survey1_sheets.col_values(5)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    routine_values = get_routine_adjust(survey)
    print(routine_values)


def get_water_intake(survey1_sheets):
    values = survey1_sheets.col_values(6)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    water_values = get_water_intake(survey)
    print(water_values)


def get_skin_concern(survey1_sheets):
    values = survey1_sheets.col_values(7)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    concern_values = get_skin_concern(survey)
    print(concern_values)


def get_favourite_product(survey1_sheets):
    values = survey1_sheets.col_values(8)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    product_values = get_favourite_product(survey)
    print(product_values)


def get_fragrance_preference(survey1_sheets):
    values = survey1_sheets.col_values(9)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    fragrance_values = get_fragrance_preference(survey)
    print(fragrance_values)


def get_price_preference(survey1_sheets):
    values = survey1_sheets.col_values(10)
    return values


if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    price_values = get_price_preference(survey)
    print(price_values)