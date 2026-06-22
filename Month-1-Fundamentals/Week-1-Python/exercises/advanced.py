'''
Day 4: Advanced Python & Project (10 exercises)

Lambda functions (square, add, filter, map)
Decorators (timer)
Generators
JSON operations
Regular expressions
List of dicts (filtering, sorting)
Modules & imports
API requests (GitHub API)
Data processing
Final Project: Todo CLI App (full project with all concepts)
'''

#lambda functions

plain = [1,2,3,4,5]
squared=list(map(lambda a: a*a,plain))
print(squared)

even_list = list(map(lambda a: a%2==0,plain))
print(even_list)

def countdown(n):
    for i in range(n,-1,-1):
        yield i
print(list(countdown(5)))

def fib(limit):
    n1=0
    n2=1
    while n1<= limit:
        yield n1
        n1=n2
        n2=n1+n2

print(list(fib(100)))


'''
Data processing Python tasks. Pick:

Beginner
1. CSV → dict list. Read sales.csv (date, product, qty, price). Compute total revenue per product. Sort desc. Write revenue.json.
2. Log parser. Read app.log. Count ERROR/WARN/INFO per hour. Print top 5 error hours.
3. JSON flatten. Nested user JSON → flat CSV with dotted keys (address.city).

Intermediate
4. Dedup pipeline. 1M-row CSV. Drop exact dupes, then near-dupes (Levenshtein ≤ 2 on name field). Time it.
5. ETL chunker. 10GB CSV. Stream-process in 50k chunks, filter, aggregate running stats, write Parquet partitioned by date.
6. Anomaly detect. Time-series CSV. Z-score per group, flag points |z| > 3. Plot with matplotlib.
7. Pivot builder. Sales data. Pivot table: rows=region, cols=month, values=sum(sales). Output multi-index DataFrame → Excel.

Advanced
8. Pipeline DAG. Tasks: extract → clean → enrich → aggregate → load. Use asyncio + queues. Crash-safe resume from checkpoint.
9. Dedupe at scale. 50M rows, 4GB RAM. MinHash + LSH via datasketch. Find near-dupes. Measure precision/recall.
10. Stream join. Two Kafka streams (simulate with generators). Tumbling window join on key. Late-arrival handling.

Production-grade
11. Data quality framework. Schema validation (pandera), null/duplicate checks, distribution drift (KS-test vs baseline), Great Expectations-style report. Pluggable checks.
12. Incremental loader. S3-partitioned Parquet. Track watermark. Only load new partitions. Idempotent. Retry on transient failure.
'''


import pandas as pd

df = pd.read_csv("sales.csv")
df["revenue"] = df["qty"] * df["price"]
by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)

with open("revenue.json",'w') as f:
    f.write(by_product)