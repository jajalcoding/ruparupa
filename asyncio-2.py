import asyncio
import aiohttp
import aiofiles
import time

async def fetch(url):
    async with aiohttp.ClientSession() as ses:
        t1 = time.perf_counter()
        print("Start to fetch "+url)
        resp = await ses.get(url)
        teks = await resp.text()
        t2 = time.perf_counter() - t1
        print(f"{url} fetch executed in {t2:0.2f} seconds.")
        return teks

async def simpan_file(file,teks):
    async with aiofiles.open(file,'w') as f:
        await f.write( teks )

async def main(urls):
    time1 = time.perf_counter()
    tasks = []
    for url in urls:
        file = f'{url.split("//")[-1]}.txt'
        html = await fetch(url)
        tasks.append( simpan_file(file, html) )

    print( tasks )    
    await asyncio.gather(*tasks)
    time2 = time.perf_counter() - time1
    print(f"{__file__} completely executed in {time2:0.2f} seconds.")


# this is the main start of the code

daftarurl = ('https://www.detik.com',
            'https://www.google.com', 
            'https://stackoverflow.com', 
            "https://www.fortinet.com", 
            "https://www.checkpoint.com",
            "https://www.liputan6.com",
            "https://www.youtube.com"
            )

asyncio.run( main(daftarurl) )
