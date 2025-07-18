import multiprocessing
import requests
import concurrent.futures
import os

url = "https://picsum.photos/2000/3000"

def downloadFile(url,name):
    print(f"Started downloading {name}")

    try:
        os.makedirs("file", exist_ok=True)
        response = requests.get(url)
        response.raise_for_status()
        
        with open(f"file/file{name}.jpg", "wb") as f:
            f.write(response.content)
        print(f"Finished downloading {name}")
    except Exception as e:
        
        print(f"Error Downloading {name} - {e}")



if __name__ == "__main__":

    # pros = []

    # for i in range(5):
    #     # downloadFile(url,i)
    #     p = multiprocessing.Process(target=downloadFile, args=[url,i])
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #     p.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(60)]
        l2 = [i for i in range(60)]
        results = executor.map(downloadFile,l1,l2)
        for r in results:
            print(r)