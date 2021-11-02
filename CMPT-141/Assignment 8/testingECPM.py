

def calculate_ecpm(ad_spend, ad_impressions):

    '''

    Calculate the effective cost per mille (1000)

    :param ad_spend: number representing total advertising spend

    :param ad_impressions: number representing total advertising impressions

    :return: float of calculated ecpm
 
    '''

    ecpm = 0.0

    if ad_spend > 0 and ad_impressions > 0:

        ecpm = ( ad_spend / ad_impressions ) * 1000

    return round(ecpm, 2)



def calculate_arpdau(user_list, revenue_list):

    '''

    Calculate the average revenue per daily active user

    :param user_list: list containing number of users per day

    :param revenue_list: list containing revenue per day

    :return: float of calculated arpdau

    '''

    arpdau = 0.0

    if len(user_list) > 0 and len(revenue_list) > 0 and len(user_list) == len(revenue_list) and sum(user_list) > 0:

        arpdau = sum(revenue_list) / sum(user_list) / len(user_list)

    return round(arpdau, 4)
