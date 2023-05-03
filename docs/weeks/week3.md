# week3 (數據處理&分析主題)
![Relative date](https://img.shields.io/date/1682473794?color=%239035&label=last%20update%3A&logo=anchor)
>[!DANGER] 分享內容快速預覽：
>
>- chatGPT 對話場景下,自我學習以下內容
>- python 基礎回顧、完善、補充3 (語法;流程控制;邏輯處理;面向對象編程;面向函數編程;等基本概念)
>- python numpy， pandas 庫常用命令；
>- 複雜數據讀取，處理，及自動化處理；
>- 提供一些練習結合 AI 輔助工具解決任務需求



> [!TIP]
>
> 系统学习 pandas 的资料:
> http://joyfulpandas.datawhale.club/Content/index.html
>
> 相应 GitHub 项目
>
> `git clone https://github.com/iihciyekub/joyful-pandas`



[filename](https://raw.githubusercontent.com/iihciyekub/codecopilot.polyU/main/docs/drawio/week3dataFL1.drawio ':include :type=xml')

!> week.2 中爬取的数据进行整理


```
#init{1}
创建一个pandas dataframe 空数据表 edf , 列名为k 与v , 
遍历res 元组中所有元素,用临时变量r 表示元素 
1 使用pandas 库, 判断元素 r 是否为 dataframe 类型变量, 如果为真, 则进行以下操作
2 先过滤操作, 保留有包含 "Details for breach" 字符的元素 r 的列名,变量名为 col 
如果col 元素数量大于0 , 令 edf 的 v列第一行值为等于这个列名 , 再令变量 edf 的 k 列第一行值为 "case/breach" ,  
如果没有,则不作处理,
2 接着则构建一个循环, 每次均取出将元素 r 的最前面 2列 并更改列名为 k 与v, 拼接到 edf 中,之后删除最前面的2列, 直到元素r 无法取出前2列数据的
```

```

以下的操作每次都要更新 edf 
1 对edf 进行去重操作, 
2 剔除 v 列为 pandas 的 NaN 
3 如果k列与 v列 值一致或相同时请剔除;
4 填充k 列 空值为 Description
5 重置索引值 
6 设置 k 列为索引, 并对edf 进行转置,
```

```
 
对方法进行封装,循环调用方法,直至 reslist 数组处理完毕
```

```
 
通过concat 的方法将返回值进行拼接,得到完整的数据表
```

