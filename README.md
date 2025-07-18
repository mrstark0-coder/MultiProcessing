# MultiProcessing
Runs code in separate CPU processes. Useful for CPU-bound tasks (like heavy calculations) — better performance than threads.

<h1> Use case:</h1> Image processing, data transformation, ML training.

<h1>Library</h1>
import multiprocessing

<H1>Also a mini project</H1>
#Image Auto Downloader using Python Multiprocessing
Python project that demonstrates how to download multiple images **concurrently** using the `multiprocessing` module and `concurrent.futures.ProcessPoolExecutor`.

#Features
- Downloads high-resolution random images from [https://picsum.photos](https://picsum.photos)
- Uses **multiprocessing** for parallel downloads

#Concepts Used
- `multiprocessing` module
- `ProcessPoolExecutor` from `concurrent.futures`
- HTTP requests with `requests`
- File handling and exception handling in Python
