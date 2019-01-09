---
title: oracle中的exists和not exists用法
date: 2018-11-19 16:42
tags: oracle exists not exists
---
相关子查询
---
        子查询的查询条件依赖于外层父查询的某个属性值，称这类查询为相关子查询。
        首先去外层查询中表的第1个元组，根据它与内层查询相关的属性值处理内层查询，若WHERE子句返回值为真，则取此元组放入结果表；然后再取表的下一个元组；重复这个过程直到外层表全部检查完为止
exists
---
        //带有EXISTS谓词的子查询不返回任何数据，只产生逻辑真值“true”或逻辑假值“false”。
        //EXISTS里的子查询结果集非空，EXISTS()子句的值就是true。
        //EXISTS里的子查询结果集为空，EXISTS()子句的值就是false。 
        select * from emp where exists (select * from dept where dname like '%A%' and deptno = emp.deptno)
not exists
---
        select * from emp where not exists (select * from dept where dname like '%A%' and deptno = emp.deptno)
exists和in
---
        in子句通常用在不相关子查询中。通常先执行子查询，将子查询的结构用于父查询。
        子查询的查询条件不依赖于父查询，这类子查询称为不相关子查询。

        in 和 exists 的区别

        性能上的比较
        Select * from T1 where x in ( select y from T2 )
        执行的过程相当于:
        select *
            from t1, ( select distinct y from t2 ) t2
        where t1.x = t2.y;


        select * from t1 where exists ( select null from t2 where y = x )
        执行的过程相当于:
        for x in ( select * from t1 )
            loop
                if ( exists ( select null from t2 where y = x.x ) )
                then
            OUTPUT THE RECORD
                end if
        end loop
        表 T1 不可避免的要被完全扫描一遍

        以子查询 ( select y from T2 )为考虑方向，如果子查询的结果集很大需要消耗很多时间，
        但是T1比较小执行( select null from t2 where y = x.x )非常快，那么exists就比较适合用在这里。
        相对应得子查询的结果集比较小的时候就应该使用in. 
