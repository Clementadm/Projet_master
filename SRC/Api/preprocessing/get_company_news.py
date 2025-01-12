from API.get_data.api_apinews_org import get_news


def save_file():
    all_news = get_news(business_name="tesla", anteriorite_en_jours=7)
    all_news.to_csv("../Data/Output/my_test_1.csv")
    return "Done"
