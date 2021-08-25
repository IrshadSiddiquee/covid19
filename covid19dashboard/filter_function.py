import api_calling as api
import constant as const
import pandas as pd

# Create public variable to store state wise Confirmed', 'Recovered', 'Deaths' and 'Active' cases from dataframe
df_state_wise_cases = api.df_state_wise_cases

# create an interface for state with state code dataframe
df_state_with_code = api.df_state_with_code

# create an interface to import state wise per day cases from API
df_state_wise_per_day_cases = api.df_state_wise_per_day_cases


# Pass state name or 'India' into the function to get state wise or pan india cases
# like total number of Confirmed', 'Recovered', 'Deaths' and 'Active'
def get_case(state):
    if state == const.COUNTRY_NAME:
        state = const.STR_TOTAL

    cases = df_state_wise_cases[df_state_wise_cases[const.STR_STATE] == state].iloc[
            :, const.INT_ZERO:const.INT_FIVE].to_dict(const.STR_RECORDS)
    return cases[const.INT_ZERO]


# Get daily state wise Confirmed', 'Recovered' and 'Deceased'.
def get_daily_cases(last_day):
    state_codes = []
    confirmed_cases = []
    recovered_cases = []
    deceased_cases = []

    for i in range(len(df_state_with_code)):
        state_code = df_state_with_code[i][const.STR_STATE_CODE]
        if state_code != const.STR_TT:
            case = pd.DataFrame(df_state_wise_per_day_cases.loc[(df_state_wise_per_day_cases[const.DATE_YMD]
                                                                 == str(last_day))], columns=[str(state_code)])

            state_codes.append(state_code)
            confirmed_cases.append(case.iloc[0][str(state_code)])
            recovered_cases.append(case.iloc[1][str(state_code)])
            deceased_cases.append(case.iloc[2][str(state_code)])

    cases = {const.STR_STATE_CODE: state_codes,
             const.CONFIRMED_CASES: confirmed_cases,
             const.RECOVERED_CASES: recovered_cases,
             const.DECEASED_CASES: deceased_cases}
    return cases


# Get state code based on state name
def get_state_code(state):
    state_code = ""
    for i in range(len(df_state_with_code)):
        if df_state_with_code[i][const.STR_STATE] == state:
            state_code = df_state_with_code[i][const.STR_STATE_CODE]
            break
    return state_code


# Store all state into the list
def get_state():
    all_state = []
    for i in range(len(df_state_with_code)):
        if df_state_with_code[i][const.STR_STATE] != const.STR_TOTAL:
            all_state.append(df_state_with_code[i][const.STR_STATE])
    return all_state


# Get full state name
def get_full_state_name(state):
    all_state = ""
    for i in range(len(df_state_with_code)):
        if df_state_with_code[i][const.STR_STATE].split(" ", const.INT_ONE)[const.INT_ZERO] == state:
            all_state = df_state_with_code[i][const.STR_STATE]
            break
    return all_state


# Get current day state wise Confirmed', 'Recovered' and 'Deceased'.
def get_state_wise_daily_case(state_code, current_date):
    try:
        case = pd.DataFrame(
            df_state_wise_per_day_cases.loc[(df_state_wise_per_day_cases[const.DATE_YMD] == str(current_date))],
            columns=[str(state_code)])
        cases = {const.CONFIRMED_CASES: case.iloc[0][str(state_code)],
                 const.RECOVERED_CASES: case.iloc[1][str(state_code)],
                 const.DECEASED_CASES: case.iloc[2][str(state_code)],
                 const.ACTIVE_CASES: round(case.iloc[0][str(state_code)] * 0.30)}

        return cases
    except NameError:
        return 0


# get ten days history cases
def get_ten_days_cases(state_code, last_ten_days):
    confirmed_cases = []
    recovered_cases = []
    deceased_cases = []
    case = pd.DataFrame(df_state_wise_per_day_cases.loc[(df_state_wise_per_day_cases[const.DATE_YMD]
                                                         >= str(last_ten_days))], columns=[str(state_code)])
    for i in range(0, len(case), 3):
        confirmed_cases.append(case.iloc[i][str(state_code)])
        recovered_cases.append(case.iloc[i + 1][str(state_code)])
        deceased_cases.append(case.iloc[i + 2][str(state_code)])

    cases = {const.CONFIRMED_CASES: confirmed_cases,
             const.RECOVERED_CASES: recovered_cases,
             const.DECEASED_CASES: deceased_cases}
    return cases


sub = get_state
print(sub())
