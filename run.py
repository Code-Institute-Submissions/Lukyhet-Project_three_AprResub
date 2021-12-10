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


def get_skin_type(survey1_sheets):
    values = survey1_sheets.col_values(2)
    return values


def get_cleanse_habit(survey1_sheets):
    values = survey1_sheets.col_values(3)
    return values


def get_sunscreen_habit(survey1_sheets):
    values = survey1_sheets.col_values(4)
    return values


def get_routine_adjust(survey1_sheets):
    values = survey1_sheets.col_values(5)
    return values


def get_packaging_preference(survey1_sheets):
    values = survey1_sheets.col_values(6)
    return values


def get_skin_concern(survey1_sheets):
    values = survey1_sheets.col_values(7)
    return values


def get_favourite_product(survey1_sheets):
    values = survey1_sheets.col_values(8)
    return values


def get_fragrance_preference(survey1_sheets):
    values = survey1_sheets.col_values(9)
    return values


def get_price_preference(survey1_sheets):
    values = survey1_sheets.col_values(10)
    return values


def get_age_report(survey1_sheets):
    age_values = get_age_range(survey1_sheets)
    initial_range = []
    last_range = []
    age_values_len = len(age_values)
    for age_value in age_values[1:age_values_len]:
        int_age_value = int(age_value)
        if int_age_value <= 40:
            initial_range.append(int_age_value)
        else:
            last_range.append(int_age_value)
    all_age_values_len = len(age_values) - 1
    initial_range_len = len(initial_range)
    last_range_len = len(last_range)
    initial_range_percentage = (initial_range_len * 100) / all_age_values_len
    last_range_percentage = (last_range_len * 100) / all_age_values_len
    initial_range_format_percentage = round(initial_range_percentage, 2)
    last_range_format_percentage = round(last_range_percentage, 2)
    print('Ages 15 - 40 answer: %s' % str(initial_range_format_percentage) + '%')
    print('Ages 40+ answer: %s' % str(last_range_format_percentage)+ '%')


def get_skin_type_report(survey1_sheets):
    dry_list = []
    oily_list = []
    combo_list = []
    sensitive_list = []
    all_skin_values = get_skin_type(survey1_sheets)
    all_skin_values_len = len(all_skin_values)
    for skin_value in all_skin_values[1:all_skin_values_len]:
        if skin_value == 'dry':
            dry_list.append(skin_value)
        if skin_value == 'combo':
            combo_list.append(skin_value)
        if skin_value == 'oily':
            oily_list.append(skin_value)
        if skin_value == 'sensitive':
            sensitive_list.append(skin_value)
    dry_list_len = len(dry_list)
    combo_list_len = len(combo_list)
    oily_list_len = len(oily_list)
    sensitive_list_len = len(sensitive_list)
    most_common = ''
    if (dry_list_len > combo_list_len) and (dry_list_len > oily_list_len) and (dry_list_len > sensitive_list_len):
        most_common = 'Dry'
    if (combo_list_len > dry_list_len) and (combo_list_len > oily_list_len) and (combo_list_len > sensitive_list_len):
        most_common = 'Combo'
    if (oily_list_len > dry_list_len) and (oily_list_len > combo_list_len) and (oily_list_len > sensitive_list_len):
        most_common = 'Oily'
    if (sensitive_list_len > dry_list_len) and (sensitive_list_len > combo_list_len) and (sensitive_list_len > oily_list_len):
        most_common = 'Sensitive'
    print('Most common skin type is %s' % most_common)


def get_cleanse_report(survey1_sheets):
    cleanse_values = get_cleanse_habit(survey1_sheets)
    yes_habit = []
    no_habit = []
    cleanse_values_len = len(cleanse_values)
    for cleanse_value in cleanse_values[1:cleanse_values_len]:
        cleanse_value = (cleanse_value)
        if cleanse_value == "yes":
            yes_habit.append(cleanse_value)
        else:
            no_habit.append(cleanse_value)
    all_cleanse_values_len = len(cleanse_values) - 1
    yes_habit_len = len(yes_habit)
    no_habit_len = len(no_habit)
    yes_habit_percentage = (yes_habit_len * 100) / all_cleanse_values_len
    no_habit_percentage = (no_habit_len * 100) / all_cleanse_values_len
    yes_habit_format_percentage = round(yes_habit_percentage, 2)
    no_habit_format_percentage = round(no_habit_percentage, 2)
    print('Do double cleanse: %s' % str(yes_habit_format_percentage) + '%')
    print('No double cleanse habit: %s' % str(no_habit_format_percentage)+ '%')
    

def get_sunscreen_report(survey1_sheets):
    sunscreen_values = get_sunscreen_habit(survey1_sheets)
    yes_habit = []
    no_habit = []
    sunscreen_values_len = len(sunscreen_values)
    for sunscreen_value in sunscreen_values[1:sunscreen_values_len]:
        sunscreen_value = (sunscreen_value)
        if sunscreen_value == "yes":
            yes_habit.append(sunscreen_value)
        else:
            no_habit.append(sunscreen_value)
    all_sunscreen_values_len = len(sunscreen_values) - 1
    yes_habit_len = len(yes_habit)
    no_habit_len = len(no_habit)
    yes_habit_percentage = (yes_habit_len * 100) / all_sunscreen_values_len
    no_habit_percentage = (no_habit_len * 100) / all_sunscreen_values_len
    yes_habit_format_percentage = round(yes_habit_percentage, 2)
    no_habit_format_percentage = round(no_habit_percentage, 2)
    print('Use sunscreen daily: %s' % str(yes_habit_format_percentage) + '%')
    print('No daily sunscreen habit: %s' % str(no_habit_format_percentage)+ '%')


def get_routine_report(survey1_sheets):
    routine_values = get_routine_adjust(survey1_sheets)
    yes_adjust = []
    no_adjust = []
    routine_values_len = len(routine_values)
    for routine_value in routine_values[1:routine_values_len]:
        routine_value = (routine_value)
        if routine_value == "yes":
            yes_adjust.append(routine_value)
        else:
            no_adjust.append(routine_value)
    all_routine_values_len = len(routine_values) - 1
    yes_adjust_len = len(yes_adjust)
    no_adjust_len = len(no_adjust)
    yes_adjust_percentage = (yes_adjust_len * 100) / all_routine_values_len
    no_adjust_percentage = (no_adjust_len * 100) / all_routine_values_len
    yes_adjust_format_percentage = round(yes_adjust_percentage, 2)
    no_adjust_format_percentage = round(no_adjust_percentage, 2)
    print('Adjust skincare routine with seasons: %s' % str(yes_adjust_format_percentage) + '%')
    print('Does not adjust skincare routine with seasons: %s' % str(no_adjust_format_percentage)+ '%')


def get_packaging_report(survey1_sheets):
    packaging_values = get_packaging_preference(survey1_sheets)
    plastic_preference = []
    glass_preference = []
    packaging_values_len = len(packaging_values)
    for packaging_value in packaging_values[1:packaging_values_len]:
        packaging_value = (packaging_value)
        if packaging_value == "plastic":
            plastic_preference.append(packaging_value)
        else:
            glass_preference.append(packaging_value)
    all_packaging_values_len = len(packaging_values) - 1
    plastic_preference_len = len(plastic_preference)
    glass_preference_len = len(glass_preference)
    plastic_preference_percentage = (plastic_preference_len * 100) / all_packaging_values_len
    glass_preference_percentage = (glass_preference_len * 100) / all_packaging_values_len
    plastic_preference_format_percentage = round(plastic_preference_percentage, 2)
    glass_preference_format_percentage = round(glass_preference_percentage, 2)
    print('Prefer plastic packaging: %s' % str(plastic_preference_format_percentage) + '%')
    print('Prefer glass packaging: %s' % str(glass_preference_format_percentage)+ '%')


def get_skin_concern_report(survey1_sheets):
    aging_list = []
    acne_list = []
    sensitive_skin_list = []
    pigmentation_list = []
    big_pores_list = []
    all_skin_values = get_skin_concern(survey1_sheets)
    all_skin_values_len = len(all_skin_values)
    for skin_value in all_skin_values[1:all_skin_values_len]:
        if skin_value == 'aging':
            aging_list.append(skin_value)
        if skin_value == 'acne':
            acne_list.append(skin_value)
        if skin_value == 'sensitive skin':
            sensitive_skin_list.append(skin_value)
        if skin_value == 'pigmentation':
            pigmentation_list.append(skin_value)
        if skin_value == 'big pores':
            big_pores_list.append(skin_value)
    aging_list_len = len(aging_list)
    acne_list_len = len(acne_list)
    sensitive_skin_list_len = len(sensitive_skin_list)
    pigmentation_list_len = len(pigmentation_list)
    big_pores_list_len = len(big_pores_list)
    most_common = ''
    if (aging_list_len > acne_list_len) and (aging_list_len > sensitive_skin_list_len) and (aging_list_len > pigmentation_list_len) and (aging_list_len > big_pores_list_len):
        most_common = 'Aging'
    if (acne_list_len > aging_list_len) and (acne_list_len > sensitive_skin_list_len) and (acne_list_len > pigmentation_list_len) and (acne_list_len > big_pores_list_len):
        most_common = 'Acne'
    if (sensitive_skin_list_len > aging_list_len) and (sensitive_skin_list_len > acne_list_len) and (sensitive_skin_list_len > pigmentation_list_len) and (sensitive_skin_list_len > big_pores_list_len):
        most_common = 'Sensitive skin'
    if (pigmentation_list_len > aging_list_len) and (pigmentation_list_len > acne_list_len) and (pigmentation_list_len > sensitive_skin_list_len) and (pigmentation_list_len > big_pores_list_len):
        most_common = 'Pigmentation'
    if (big_pores_list_len > aging_list_len) and (big_pores_list_len > acne_list_len) and (big_pores_list_len > sensitive_skin_list_len) and (big_pores_list_len > pigmentation_list_len):
        most_common = 'Big pores'
    print('Most common skin concern is %s' % most_common)


def get_favourite_product_report(survey1_sheets):
    serum_list = []
    moisturizer_list = []
    sunscreen_list = []
    cleanser_list = []
    retinol_list = []
    acids_list = []
    all_favourite_product_values = get_favourite_product(survey1_sheets)
    all_favourite_product_values_len = len(all_favourite_product_values)
    for favourite_product_value in all_favourite_product_values[1:all_favourite_product_values_len]:
        if favourite_product_value == 'serum':
            serum_list.append(favourite_product_value)
        if favourite_product_value == 'moisturizer':
            moisturizer_list.append(favourite_product_value)
        if favourite_product_value == 'sunscreen':
            sunscreen_list.append(favourite_product_value)
        if favourite_product_value == 'cleanser':
            cleanser_list.append(favourite_product_value)
        if favourite_product_value == 'retinol':
            retinol_list.append(favourite_product_value)
        if favourite_product_value == 'acids':
            acids_list.append(favourite_product_value)
    serum_list_len = len(serum_list)
    moisturizer_list_len = len(moisturizer_list)
    sunscreen_list_len = len(sunscreen_list)
    cleanser_list_len = len(cleanser_list)
    retinol_list_len = len(retinol_list)
    acids_list_len = len(acids_list)
    most_common = ''
    if (serum_list_len > moisturizer_list_len) and (serum_list_len > sunscreen_list_len) and (serum_list_len > cleanser_list_len) and (serum_list_len > retinol_list_len) and (serum_list_len > acids_list_len):
        most_common = 'Serum'
    if (moisturizer_list_len > serum_list_len) and (moisturizer_list_len > sunscreen_list_len) and (moisturizer_list_len > cleanser_list_len) and (moisturizer_list_len > retinol_list_len) and (moisturizer_list_len > acids_list_len):
        most_common = 'Moisturizer'
    if (sunscreen_list_len > serum_list_len) and (sunscreen_list_len > moisturizer_list_len) and (sunscreen_list_len > cleanser_list_len) and (sunscreen_list_len > retinol_list_len) and (sunscreen_list_len > acids_list_len):
        most_common = 'Sunscreen'
    if (cleanser_list_len > serum_list_len) and (cleanser_list_len > moisturizer_list_len) and (cleanser_list_len > sunscreen_list_len) and (cleanser_list_len > retinol_list_len) and (cleanser_list_len > acids_list_len):
        most_common = 'Cleanser'
    if (retinol_list_len > serum_list_len) and (retinol_list_len > moisturizer_list_len) and (retinol_list_len > sunscreen_list_len) and (retinol_list_len > cleanser_list_len) and (retinol_list_len > acids_list_len):
        most_common = 'Retinol'
    if (acids_list_len > serum_list_len) and (acids_list_len > moisturizer_list_len) and (acids_list_len > sunscreen_list_len) and (acids_list_len > cleanser_list_len) and (acids_list_len > retinol_list_len):
        most_common = 'Acids'
    print('Most common favourite product is %s' % most_common)


def get_fragrance_preference_report(survey1_sheets):
    fragrance_values = get_fragrance_preference(survey1_sheets)
    fragrance_preference = []
    fragrance_free_preference = []
    fragrance_values_len = len(fragrance_values)
    for fragrance_value in fragrance_values[1:fragrance_values_len]:
        fragrance_value = (fragrance_value)
        if fragrance_value == "fragrance":
            fragrance_preference.append(fragrance_value)
        else:
            fragrance_free_preference.append(fragrance_value)
    all_fragrance_values_len = len(fragrance_values) - 1
    fragrance_preference_len = len(fragrance_preference)
    fragrance_free_preference_len = len(fragrance_free_preference)
    fragrance_preference_percentage = (fragrance_preference_len * 100) / all_fragrance_values_len
    fragrance_free_preference_percentage = (fragrance_free_preference_len * 100) / all_fragrance_values_len
    fragrance_preference_format_percentage = round(fragrance_preference_percentage, 2)
    fragrance_free_preference_format_percentage = round(fragrance_free_preference_percentage, 2)
    print('Prefer fragrance: %s' % str(fragrance_preference_format_percentage) + '%')
    print('Prefer fragrance-free: %s' % str(fragrance_free_preference_format_percentage)+ '%')


def get_price_preference_report(survey1_sheets):
    price_values = get_price_preference(survey1_sheets)
    high_end_preference = []
    low_end_preference = []
    price_values_len = len(price_values)
    for price_value in price_values[1:price_values_len]:
        price_value = (price_value)
        if price_value == "high end":
            price_preference.append(price_value)
        else:
            low_end_preference.append(value_value)
    all_price_values_len = len(price_values) - 1
    high_end_preference_len = len(high_end_preference)
    low_end_preference_len = len(low_end_preference)
    high_end_preference_percentage = (high_end_preference_len * 100) / all_price_values_len
    low_end_preference_percentage = (low_end_preference_len * 100) / all_price_values_len
    high_end_preference_format_percentage = round(high_end_preference_percentage, 2)
    low_end_preference_format_percentage = round(low_end_preference_percentage, 2)
    print('Prefer high end price: %s' % str(high_end_preference_format_percentage) + '%')
    print('Prefer low end price: %s' % str(low_end_preference_format_percentage)+ '%')




if __name__ == '__main__':
    survey = load_document().worksheet('survey1')
    # data = survey.get_all_values()
    # skin_types = get_skin_type(survey)
    # print(skin_types)
    # price_preference = get_price_preference(survey)
    # print(price_preference)
    get_age_report(survey)
    get_skin_type_report(survey)
    get_cleanse_report(survey)
    get_sunscreen_report(survey)
    get_routine_report(survey)
    get_packaging_report(survey)
    get_skin_concern_report(survey)
    get_favourite_product_report(survey)
    get_fragrance_preference_report(survey)
    
