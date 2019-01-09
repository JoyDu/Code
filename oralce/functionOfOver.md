---
title: Oracle开窗函数之Over
date: 2018-03-05 17:42
tags: oracle
---
作用及用法
---
    按指定字段分组排序，对分组结果集进行排序  
    partition by为分组字段(可选) order by 排序字段
    Rank() over([partition by] order by)排序
    Dense_Rank() over([partition by] order by) 分组排序后相同序号行占位置eg：1 1 3 4 4 6
    Row_number() over([partition by] order by) 分组排序后相同序号行不占位置eg：1 1 2 3 4 4 5
    Sum(column) over() 某列数据总和
    Sum(column) over(Order by column) 连续求和，按照指定的列排序，求和方式为每行的该列数值加上前面所有行的数据
    Sum(column) over(partition by column) 按照column分组求每组指定列的和
实例
---
    select warehouse.suppliername warehousename,
       sales.amount,
       sum(sales.amount) over() totalamount,
       round(sales.amount/(sum(sales.amount) over()),6) saleszhanbi,
       row_number() over(order by sales.amount desc) salesindex,
       round(sales.TotalProfit/(sum(sales.TotalProfit) over()),6) profitzhanbi,
       row_number() over(order by sales.TotalProfit desc) profitindex,
       sales.TotalCost,
       sales.TotalProfit,
       client.fullname
    from salesorderprofit_vw sales
    left join t_supplier warehouse
        on warehouse.id = sales.supplierckid
    left join cm_sec_client client
        on client.id=sales.clientid
参考
---
    http://www.cnblogs.com/umen/archive/2011/04/11/2012136.html

