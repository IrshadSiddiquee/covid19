import api_calling as api
import constant as const


# Create public variable to store data frame
df_state_wise_cases = api.df_state_wise_cases


def get_case(state):
    if state == const.COUNTRY_NAME:
        state = const.STR_TOTAL

    cases = df_state_wise_cases[df_state_wise_cases[const.STR_STATE] == state].iloc[:, 0:5].to_dict(const.STR_RECORDS)
    return cases[0]


sub = get_case('India')
print(sub)
