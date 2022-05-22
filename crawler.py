import asyncio
import re

import requests
from bs4 import BeautifulSoup


async def crawl_douban_beijing_movies():
    url = 'https://movie.douban.com/cinema/later/beijing/'
    soup = create_soup(url)
    div_showing_soon = soup.find('div', id='showing-soon')
    if div_showing_soon:
        items = div_showing_soon.find_all('div', class_='item')
        tasks = [asyncio.create_task(parse_div_movie(div_movie)) for div_movie in items]
        movie_ids = await asyncio.gather(*tasks)
        print(movie_ids)
        get_photo_tasks = [asyncio.create_task(get_photo_urls(movie_id)) for movie_id in movie_ids]
        await asyncio.gather(*get_photo_tasks)


async def parse_div_movie(div_movie):
    movie_name = div_movie.find('h3').find('a').text
    print(f'movie_name: {movie_name}')
    lis = div_movie.find('ul').find_all('li')
    for li in lis:
        print(li.text)
    photo_href = div_movie.find('a')['href']
    movie_id = re.search(r'\d+', photo_href, re.M | re.I).group()
    print('----------------------------------')
    return movie_id


async def get_photo_urls(movie_id):
    photo_url = f'https://movie.douban.com/subject/{movie_id}/photos?type=R'
    soup = create_soup(photo_url)
    div_content = soup.find('div', id='content')
    print(div_content.find('h1').text)
    imgs = div_content.find_all('img')
    img_srcs = [img['src'] for img in imgs]
    print(img_srcs)
    print('----------------------------------')


def create_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.64 Safari/537.36 '
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')


if __name__ == '__main__':
    asyncio.run(crawl_douban_beijing_movies())
