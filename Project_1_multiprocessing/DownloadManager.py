import requests
import threading
import multiprocessing


def download_file(url: str) -> bytes:
    """Downloads the content from the given URL and returns it as bytes"""
     
    try:
        response = requests.get(url)
        # We check whether the request was successfully completed
        response.raise_for_status()
        
        return response.content
        
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while uploading the file: {e}")
        return b''  

def execute_function(arg, results):
        result = download_file(arg)
        results.append(result)
  


class DownloadManager:
    def __init__(self,max_threads:int,max_processes:int,) -> None:
        """

        Args:
            max_threads (int):The maximum number of threads to use for simultaneous downloads.
            max_processes (int): The maximum number of processes to use for simultaneous downloads.
            downloads (list): A list to hold the Download objects for each download.
        """
        self.max_threads = max_threads
        self.max_processes = max_processes
        self.downloads = []
        
        
    def download(self,url: str, filename: str):
        """Starts a new download for the given URL and saves it with the specified filename"""
        self.downloads.append(ThreadingDownloader(url,filename))
        
    
    def start(self):
        """Starts the download manager and begins downloading all the files"""
        if self.max_threads< len(self.downloads):
            raise MemoryError
       
        for dow in self.downloads:
            dow.start_download()
            dow.save_file(dow.results[0])
              
        
        
    
    def wait(self):
        """Waits for all downloads to complete"""
        
        for dow in self.downloads:
            dow.thread.join()
            
            
            
    
    

class Download:
    pass
    def __init__(self,url:str,filename:str) -> None:
        """"
        • url (str): The URL of the file to download.
        • filename (str): The filename to save the downloaded file.
        
        
        • download_complete(): 
        
        """
        self.url = url
        self.filename = filename
        
    
    def start_download(self):
        """Starts the download process."""
        return download_file(self.url)
        
    
    def save_file(self,content: bytes):
        """Saves the downloaded content to the specified filename."""
        
        
        decoded_text = content.decode('utf-8')
        with open (self.filename,"w") as file:
            file.write(decoded_text)

        print("file saved")
        
    
    
    def download_complete(self):
        """Signals that the download is complete"""
        print("download is complete")
    
    

class ThreadingDownloader(Download):
    
    def __init__(self, url: str, filename: str) -> None:
        super().__init__(url, filename)
    
    def start_download(self): 
        """Implements the download process using threading."""
              
        self.results = []
        
        self.thread  = threading.Thread(target = execute_function(self.url,self.results))

        self.thread.start()

        
        
    
    
# only threading is used in Download Manager

class MultiprocessingDownloader(Download):
    def __init__(self, url: str, filename: str) -> None:
        super().__init__(url, filename)
        
        
    def start_download(self):
        """ Implements the download process using multiprocessing"""
        self.results = []
        
        self.process = multiprocessing.Process(target = execute_function(self.url,self.results))

        self.process.start()
    

download_manager = DownloadManager(max_threads=3, max_processes=2)

download_manager.download("https://github.com/arman1919/Python_Homework/blob/main/test1.txt", "file1.txt")
download_manager.download("https://github.com/arman1919/Python_Homework/blob/main/test2.txt", "file2.txt")
download_manager.download("https://github.com/arman1919/Python_Homework/blob/main/test3.txt", "file3.txt")

download_manager.start()
download_manager.wait()

print("All downloads completed!")