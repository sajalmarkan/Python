# import multiprocessing
# import requests
# import os
# import concurrent.futures

# def downloadFile(url, name):
#     print(f"Started Downloading {name}")
#     response = requests.get(url)
#     if not os.path.exists('files'):
#         os.makedirs('files')
#     open(f"files/file{name}.jpg", "wb").write(response.content)
#     print(f"Finished Downloading {name}")

# if __name__ == '__main__':
#     url = "https://picsum.photos/2000/3000"
#     pros = []

#     for i in range(5):
#         p = multiprocessing.Process(target=downloadFile, args=(url, i))
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()

import requests
import os
import concurrent.futures

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    if not os.path.exists('files'):
        os.makedirs('files')
    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished Downloading {name}")
    return f"Downloaded {name}"

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for _ in range(60)]
        l2 = list(range(60))
        results = executor.map(downloadFile, l1, l2)

        for result in results:
            print(result)
