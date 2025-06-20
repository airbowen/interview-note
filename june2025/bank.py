# 问的什么啊？
#  unflat the nested list
#这个是原问题输入
from ctypes import DEFAULT_MODE


nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#这个是for 循环便利取
flat_list = [item for sublist in nested_list for item in sublist]

print(flat_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

需要默认值 用defalutdict。defaultd ditc 可以 access a key that does not exist →
就是哪怕是空的，也有个默认值default value，可以直接访问、
defaultdict（这里可以指定类型，比如int，）

不需要默认值直接dict 
提前退出

就好

if condition:
    for item in items:
        break
        或者
        continue 也可以
        # Do something】

    python 操作sql 也行，适合复杂的
    context manage object that defines enter and exit actions:
    比如
    with open('file.txt') as f:
    f.read()
# if the string is matrix how to convert it: if a string is reversable or sysmmetric

    string 就是一个list 底层，
    python 中所有的string都是 可以当list 用，可以直接rerverse  ：：-1 就是python 的翻转
    
    ## 原始的输入就是matrix
    # 比如
    matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
    ]
    # 直接当做list 翻转
    matrix_reversed = [row[::-1] for row in matrix]

# return the rank of the banks using sql if there are many bank
# to determine the top ranked revenue 

# all in one table the dpt name etc
# return retveue with each department by each bank
# PARTITION BY department → 每个部门单独排名
# desc 降序排名，从高到低

# RANK() → 会处理平级（相同 revenue 共享 rank）
# two dpt same rank rev, what will 3rd one's rank
如果1，,2 并列，直接跳到3 所以rank 会自动跳，不用担心，
DENSE_RANK() → 不跳号 2，
bank_name    revenue    RANK()
A    1000    1
B    1000    1
C    900    3
SELECT 
    department,
    bank_name,
    revenue,
    RANK() OVER (PARTITION BY department ORDER BY revenue DESC) AS revenue_rank
FROM
    bank_revenue; 



##   spark 是内存中的内存分布式计算（可溢出磁盘）spark 自身不带数据
自身不存储数据，通常读取 HDFS、S3、Hive、Parquet
    海量数据处理、离线/流批处理、数据仓库分析（OLAP）spark 是个分析工具

mysql 是个数据库，数据在硬盘上，spark 读到内存中，处理。 流入后做大数据 ETL、机器学习、复杂报表

可以连接mysql 也可以连接hadoop，都可以连
mysql 是relationial ，MongoDB 是non relantion database finanicial data real time effecient I think

Can I get exposed to the quant trading team to collaborate with them and what is the most common dataset i get tick one?

will that requires me to have a solid understanding of quant trading?

did your team apply llm to deal with quality check, cuz i think u r familar with prompt tuning

