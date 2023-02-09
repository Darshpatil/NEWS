import requests
from bs4 import BeautifulSoup
from re import search
import re as z
import tkinter as tk

master = tk.Tk()
j = 2
o = 3
print(12)
for h in range(1, 4):
    url = 'https://allaboutbelgaum.com/category/news/page/' + str(h) + '/'
    h + 1
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    header = soup.findAll('h4',class_='gb-headline gb-headline-a8c661f2 gb-headline-text')
    link = soup.find_all('a')
    # print(header)

    # .find_all('a')
    # link = soup.find_all('a')
    #  unwanted = ['BBC World News TV', 'BBC World Service Radio',
    #             'News daily newsletter', 'Mobile app', 'Get in touch']
    def linkGet(q):
        li = 'https://allaboutbelgaum.com/news/'
        li2 = 'https://allaboutbelgaum.com/'
        li3 = 'https://allaboutbelgaum.com/iambelagavi/'
        # for i in range(4):
        for x in link:

            if "href" in x.attrs:
                b = x.attrs['href']
                e = str(b)
                f = e[-7:]
                j = f[-5:]
                # print(e)
                if "#respond" not in a:
                    if search(f, c):
                        if search(j, c):
                            # for m in soup.find_all('a',
                            #                           attrs={'href': z.compile("^https://allaboutbelgaum.com/news/m")}):
                            # display the actual urls
                            # print(m.get('href'))
                            # if (i == 3):
                            # print(a.text.strip())
                            if li2 != e:
                                if li != e:
                                    if li3 != e:
                                        # if li2 == e:
                                        # btn = tk.Button(master, text=e)
                                        # btn.grid(row=o, column=1, sticky=tk.W, pady=4)
                                        # btn = tk.Button(master, text='')
                                        # btn.grid(row=o, column=1, sticky=tk.W, pady=4)

                                        # o + 1

                                        print(e)
                                        break
                                    else:
                                        continue

                    #     i=0
                    #     continue
                    # else:
                    #     break


    for i in header:

        h1 = 'Primary Sidebar'
        a = i
        c = str(a)
        d = a.text.strip()
        if d != h1:
            # info_message = d
            #
            # tk.Label(master, text=info_message).grid(row=j, column=1)
            # j+1

            print(d)
        # i = 0
        # for i in range(5):
        #     if (i == 3):
        linkGet(d)

# master.mainloop()

# for x in link:
#     if "href" in x.attrs:
#         b = x.attrs['href']
#         e = str(b)
#         f = e[-10:]
#         # print(f)
#         if "#respond" not in a:
#             if search(f, c):
#                 print(a.text.strip())
#                 print(f)
#             else:
#                 continue

# for x in link:
#     if "href" in x.attrs:
# # if x.text.strip() not in unwanted:
# print(x.text.strip())
# print(str(x.attrs['href']) + "\n")
#     a = x.attrs['href']
# if "https://allaboutbelgaum.com/news/" in a:
#     if "#respond" not in a:
#         print(a)
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.bbc.com/news'
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# headlines = soup.find('body').find_all('h3')
# for x in headlines:
#     print(x.text.strip())
