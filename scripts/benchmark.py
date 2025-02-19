import time
import psutil
import os
from fetch_data import fetch_data
from transform_data import transform_data
from visualize_data import visualize_data
from compress_data import compress_data

def track_resources(pid):
    process = psutil.Process(pid)
    cpu_percent = process.cpu_percent(interval=1)
    memory_info = process.memory_info()
    memory_mb = memory_info.rss / (1024 * 1024)
    return cpu_percent, memory_mb

def benchmark():
    pid = os.getpid()

    tasks = {
        "Récupération des données": fetch_data,
        "Transformation des données": transform_data,
        "Compression des données": compress_data,
        "Visualisation des données": visualize_data
    }

    with open("benchmarks/benchmark_results.txt", "w") as f:
        for task_name, task_function in tasks.items():
            start_time = time.time()
            initial_cpu, initial_memory = track_resources(pid)

            task_function()

            end_time = time.time()
            final_cpu, final_memory = track_resources(pid)
            execution_time = end_time - start_time

            log = f"{task_name} - Temps: {execution_time:.4f}s, CPU: {final_cpu - initial_cpu}%, Mémoire: {final_memory - initial_memory:.2f}Mo\n"
            print(log)
            f.write(log)

    print("✅ Benchmark terminé et enregistré.")

if __name__ == "__main__":
    benchmark()
