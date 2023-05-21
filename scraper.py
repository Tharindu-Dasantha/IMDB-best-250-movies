from bs4 import BeautifulSoup
import requests


def main():
    # going to the main page and getting the 250 movie list
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    movie_chart = soup.find("table", class_="chart")
    # now get individual movie
    movie_items = movie_chart.find_all("tr")
    for movie_item in movie_items:
        movie_title_info = movie_item.find(class_="titleColumn")
        if movie_title_info != None:
            movie_title = movie_title_info.find("a").text
            print(movie_title)
    
    
    
    w
if __name__== "__main__":
    main()