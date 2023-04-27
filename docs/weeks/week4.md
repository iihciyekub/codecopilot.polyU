# week4 (問題分享與討論)

![Relative date](https://img.shields.io/date/1682610044?color=%239035&label=last%20update%3A&logo=anchor)

>[!NOTE] workshop.w4 分享內容快速預覽：
>
>- 過往研究項目中遇到的數據處理任務，編程技術相關的分享與討論；

> [!DANGER] task.1
>
> - 有多个pdf 公司公告;(提供273份pdf文件)
> - 有两组key words, (提供excel 表格)
>   - 1）首先识别sheet1中的单词/短语出现的个数
>   - 2）然后识别sheet2中的单词/短语出现的个数
>   - 3）接着识别sheet1中单词/短语出现时，其前10个单词和后10个单词内，sheet2中单词/短语也出现了的情况的个数
>   - 4）最后识别整个pdf文件的单词数量



> [!WARNING]
>
> 数据文件存放在项目目录的 orgdata 文件夹中;



> [!TIP] prompting
>
> - 先读取key words , 清洗格式化
> - 读取 pdf 内容, 整理成list, 方便计数与索引
> - 定义好一个key word 在给定 pdf 的情况下, 处理方法
> - 再用 pandas 矢量操作,apply 映射到整列执行
> - 导出过程数据以便检验
> - 再次封装方法. 输入是 pdf,  输出结果是 pdf 的分析结果;
> - 循环对所有pdf 进行同样的操作, 再合并最终结果

1

```
用pandas 读取本项目根目录下的 wording.xlsx ,它有两个sheet 保存为 df1  ,df2, 加载数据时, 忽略列名

1. 对 df1  所有列合并为一列, 列为sheet1_term 
2,全部转小写,
3 按值排序
4 去空值去nan值,去重复值,
5.最后重置索引
6,转为 dataframe 类型
df2 也是相同的操作
```

2

```
遍历项目根目录下 orgdata 文件夹中 包含pdf的文件名, 将其加字符前缀 "orgdata/" 保存到 pdflist 数组中
```

3


```
取出df1 的第一个元素变量名是 term, 取出pdflist的第一个元素为变量名是 pdf
```

4

```
用PyMuPDF 库读取变量 pdf 
1 读取文件将所有文本拼到一起,保存为变量 alltext,
2,对 alltext 用空格进行分割得到数组 textlist ;
3,textlist 所有元素字符字母转小写,得到数组 lowtextlist 
```

5

```
定义函数 getcount，输入参数为 term 和 lowtextlist，
0 初始化变量 num 为0,  令num对 变量term 在 lowtextlist 中出现的次数, 
1 初始化变量 fb10_num 为0,  
2,初始化变量 fbtext 为 none ;
3,如果 num 是大于0的, 则取出  term 所在的索引位置,左边界-10, 右边界+10 切片数组, 保存为 fbtext,
4, 当 变量 fbtext 不是 none 时, 遍历全局变量 df2['trem'] 的所有元素, 
将它们出现在 fbtext 的总次数保存到变量 fb10_num 中,,
5.返回值为 num 与 fbtext ,fb10_num 
```

6

```
对变量df1 的 term 列, 使用 apply 方法 执行getcount ,保留第一个返回值,列名为 '# of sheet1_term" ,
第二个返回值 保存到df1 的 'sheet1_termfb10 列中,
第三个返回 保存到 '# of sheet2_term_in_sheet1_termfb10'
```

7

```
对变量df2 的 term 列, 使用 apply 方法 执行getcount
只需要保留第一个返回值,列名为 '# of sheet2_term"
其它不要
```

8

```
创建字典, resdic
1,key 名为 file ,值为  pdf
2,key 名为 "total # of sheet1_term, 
值是 df1 '# of sheet1_term'这一列的求和值
3,key 名为 "total # of sheet2_term_in_sheet1_termfb10" 
值是 df1 '# of sheet2_term_in_sheet1_termfb10' 这一列的求和值
4,key 名为 total # of sheet2_term, 
值是 df2 '# of sheet2_term'这一列的求和值
5,key 名为 "total # of pdf" 值为 lowtextlist 数组的长度
```

8

```
将 resdic 转dataframe , key 作为列名
```

9

```
创建变量 filen ,
将 变量 pdf 的 ".pdf" 修改为 ".xlsx",保存到 变量filen中,
将 df1,与df2 以 sheet1 还有sheet2的不同页面 
保存到同一个名为变量 filen 的excel表格中,  
```

10, 选中对 pdf 进行处理往后的代码进行封装,封装的时候,需要注意 chapGPT 有没有将保存的操作遗漏

```
将这一段内容封装为   pdf_count 方法, 传入参数是 pdf, 返回值是 df_resdic
```

11

```
遍历所有pdflist 执行pdf_count 方法, 将所有返回值存在 alldf 数组中, 通过 pasndas concat 输出结果
```



