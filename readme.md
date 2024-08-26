## with
### with语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中的锁的自动获取和释放等。

## python和java
### python是强类型语言，不需要隐式转换；python是动态类型语言，java是静态类型语言
### 一个python包package是包含一个__init__.py文件的
### java的接口需要通过interface关键字定义，类实现implements；python就是def函数
### \_\_all__ 公共的接口 isinstance(object, classinfo) 检查某一个对象是否属于某一个类，类型
### optional表明一个变量可以包含指定的类型或者none，在函数的参数定义中可以接受有名字的和没有名字的调用
### hooks允许开发者在特定的执行点或事件发生时插入自定义代码，以改变系统的行为或扩展其功能



## SQL
### 通配符：%表示任意长度的任意字符序列；_表示任意单个字符  “%李%”  “_李”
### 去重 distinct
### 排序 order by asc（升序） desc（降序）
### 截断和偏移：获取部分数据 limit 2 只获取前面两条数据  limit 2 2 从下标为2开始获取两条数据 
### 条件分支 select name, case when(age>60) then “1“ when(age>20) then "2" else "3" end as age_level from 
### 时间函数 date() datetime() time() 
### 字符串处理upper lower() length()
### 聚合函数 count min max avg sum count是计算行数，sum是求值
### 分类聚合 group by class_id, name (有顺序的区别) 后面接having 条件
### 关联查询 cross join返回所有可能的结果集 from student, class   inner join 交集 from student join class on student.id=class.id 
### outer join left join s on dddd(有些数据库并不支持right join)
### 子查询 嵌套查询 select。。。where in（select） exists返回true or false   where (not)exists 如果存在返回数据，不存在不返回
### 组合查询 union 将两个表的查询结果合在一起，去除重复行；union all 保留重复行
### 开窗函数1 sum() over (partition by) 分组总和
### 开窗函数2 sum() over (partition by order by )累加
### 开窗函数3 rank() over (partition by order by ) 排序查找
### 开窗函数4 row_number() over (partition by order by ) 给排序分配排序号
### 开窗函数5 lead/lag(column_name, offset, default_value) over (partition by order by) 获取当前行之后或之前的行的值  offset上或下几行

