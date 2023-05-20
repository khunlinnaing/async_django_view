import aiohttp
from django.shortcuts import render
import requests, time, asyncio
from .utils import fetch
async def home_view(request):
    start_time = time.time()
    url_list = ['https://swapi.dev/api/people/','https://swapi.dev/api/starships/']
    async with aiohttp.ClientSession() as client:
        tasks =[]
        for url in url_list:
            task = asyncio.ensure_future(fetch(client, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        total = time.time() - start_time
        print("total: " ,total)
    return render(request, 'home.html',{'people': results[0], 'starships': results[1]})
# 1.405038833618164


"""def home_view(request):
    start_time = time.time()
    data =[]
    url_list = ['https://swapi.dev/api/people/','https://swapi.dev/api/starships/']
    for url in url_list:
        data.append(requests.get(url).json())
    total = time.time() - start_time
    print("total: " ,total)
    return render(request, 'home.html', {"people": data[0], 'starships': data[1]})
# 3.0380287170410156"""