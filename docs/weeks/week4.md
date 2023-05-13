# week4 (問題分享與討論)

![Relative date](https://img.shields.io/date/1682854015?color=%239035&label=last%20update%3A&logo=anchor)

>[!DANGER] 分享內容快速預覽：
>
>- 過往研究項目中遇到的數據處理任務，編程技術相關的分享與討論；

> [!NOTE] task.1
>
> - 数据文件存放在项目目录的 orgdata 文件夹中;
> - 有多个pdf 公司公告;(提供273份pdf文件)
> - 有两组key words, (提供excel 表格)
>   - 1）首先识别sheet1中的单词/短语出现的个数;
>   - 2）然后识别sheet2中的单词/短语出现的个数;
>   - 3）接着识别sheet1中单词/短语出现时，其前10个单词和后10个单词内，sheet2中单词/短语也出现了的情况的个数;
>   - 4）最后识别整个pdf文件的单词数量;

> [!TIP] prompting
>
> - 先读取key words , 清洗格式化
> - 读取 pdf 内容, 整理成list, 方便计数与索引
> - 定义好一个key word 在给定 pdf 的情况下, 处理方法
> - 再用 pandas 矢量操作,apply 映射到整列执行
> - 导出过程数据以便检验
> - 再次封装方法. 输入是 pdf,  输出结果是 pdf 的分析结果;
> - 循环对所有pdf 进行同样的操作, 再合并最终结果



<!-- [filename](https://raw.githubusercontent.com/iihciyekub/codecopilot.polyU/main/docs/drawio/dataFL1.drawio ':include :type=xml') -->

```pdf
https://github.com/iihciyekub/codecopilot.polyU/blob/main/docs/pdf/dataFL1.pdf
```


> [!TIP]  1) 读取 wroding


```
#init{1}
用pandas 读取本项目根目录下的 wording.xlsx ,它有两个sheet 保存为 df1 ,df2, 加载数据时, 忽略列名
对变量 df1 , df2 分别进行以下操作
1 操作所有列合并为一列, 列为 sheet_序号_term
2 列元素转小写
3 去空值去nan值,去重复值,
4 按值排序
5.最后重置索引
6 转为 dataframe 类型
```
<br>

> [!TIP]  2) 获取目录文件夹下所有pdf 文件的路径作为 pdflsit, 以其中一个元素为例,创建方法

```
遍历当前相对目录下, orgdata 文件夹中 包含.pdf 后缀的文件相对路径, 并保存到 pdflist 数组中
```


```
取出变量 df1 的第一列的第一个元素作为变量 term 的值,
取出数组 pdflist 的第一个元素作为变量 pdf 的值
```

```
如果不了解哪些库可以处理 pdf 文件,可以在 coding 前与chatGPT 对话学习#end
用 PyMuPDF 库读取变量 pdf
1 读取文件将所有文本拼接成字符变量 alltext
2 对变量 alltext 用空格进行分割得到数组 textlist
3 对数组 textlist 所有元素字符字母转小写,得到数组 lowtextlist
4 对数组 textlist 去除空格,空值后,统计 textlist 的元素数量, 得到 变量 num_of_pdftext
```
<br>

> [!TIP]  3) 以处理  wording  数据表中的其中一个关键词为例, 构建方法

```
定义函数 getcount，输入参数为 term 

1 初始化变量 count_term 的值为 0
2 初始化变量 term_fb10 的值为 空数组
3 初始化变量 count_term2 为 0 
4 遍历全局变量 lowtextlist, 执行以下操作,
a) 如果元素等于变量 term时, count_term 递增1 , 并取出 lowtextlist 的切片数组,边界中当前索引值左右偏移10个元素,结果保存为临时变量 fb10 , 将变量 fb10 用空格拼接成字符串,添加到数组 term_fb10 中,   遍历临时变量 fb10 的所有元素, 是否出现在全局变量 df2 的第一列的元素中,如果为真,则 count_term2 递增1,
b) 如果元素不等于变量 term时, 则不作处理,
5 将 term_fb10 数组用换行符进行拼接;
返回值为, count_term ,term_fb10 , count_term2 
```

```
代码增加
对变量df1的第一列应用  apply 方法 , 输入参数是 getcount ,
三个返回值分别保存为列名
# of sheet1_term
sheet1_termfb10
# of sheet2_term_in_sheet1_termfb10
```

```
代码增加 
对变量df2 的第一列应用  apply 方法 , 输入参数是 getcount ,
但只需要保留第一个返回值,列名为 '# of sheet2_term"
其它返回值不要
```
<br>

> [!TIP]  4)  将结果转 dataframe 作为 output 的结果

```
对 df1 列名为 '# of sheet1_term'  '# of sheet2_term_in_sheet1_termfb10' 以及 df2 列名 '# of sheet2_term' 分别求和, 并保存为变量名 a,b,c
```

```
代码增加, 将变量 pdf, a, b, c,num_of_pdftex 的值转dataframe 类型的变量 resdf, 列名分别为
pdffile
total_#_of_sheet1_term
total_#_of_sheet2_term_in_sheet1_termfb10
total_#_of_sheet2_term
#_of_pdftext
```

```
将 变量 pdf  ".pdf" 字符替换为 ".xlsx",保存到变量 xlsxfile 中,
将 df1,与df2 用pandas库导出为 sheet1 与 sheet2 的不同页面的 xlsx 文件, 该文件名与所在目录为变量 xlsxfile 的值
```

<br>

> [!DANGER]
> 下一步代码自动生成时总是会遗漏掉 文件保存操作, prompting 过程中需要检查代码完整性

```
选中对 pdf 进行处理往后的代码进行封装,封装的时候,需要注意 chapGPT 有没有将保存的操作遗漏#end
修改代码, 将我选中的这一段内容封装为 pdf_count 方法, 传入参数是 pdf, 返回值是 resdf
```

```
遍历所有pdflist 执行pdf_count 方法, 将所有返回值存在 alldf 数组中, 通过 pasndas concat 输出结果
```


