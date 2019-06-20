---
title: Oracle分析函数之lead和lag
date: 2019-06-17 10:42
tags: lead lag oracle
---
lead和lag
---
lag与lead函数是跟偏移量相关的两个分析函数，通过这两个函数可以在一次查询中取出同一字段的前N行的数据(lag)和后N行的数据(lead)作为独立的列,从而更方便地进行进行数据过滤。这种操作可以代替表的自联接，并且LAG和LEAD有更高的效率。

over()表示 lag()与lead()操作的数据都在over()的范围内，他里面可以使用partition by 语句（用于分组） order by 语句（用于排序）。partition by a order by b表示以a字段进行分组，再 以b字段进行排序，对数据进行查询。

lead(field, num, defaultvalue) field需要查找的字段，num往后查找的num行的数据，defaultvalue没有符合条件的默认值
