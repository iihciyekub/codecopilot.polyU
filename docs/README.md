# HK polyU workshop：code copilot (未完成)

**Last Update:** 23.04.12

**Workshop Topic** : code copilot 

**Keys:** `chatGPT` `Python` `GitHub` `GitHub Copilot`  `Cursor` `Google Colaboratory`

> AI 輔助編程工作坊分享會，預計3-4周時間完成以下內容：(通曉入門知識結合AI 工具輔助編程)
>
> (i) 第1周：0基礎入門 python 編程，認識基本概念，安裝編程環境及編輯器擴展包等。利用 AI(chatGPT/GitHub /GitHub Copilot/vscode  extension GitHub Copilot/[cursor](https://www.cursor.so/)，以下简称 AI ) 等認識了解 AI 工具如何幫助用戶自我學習或代碼質量改進等，認識輔助編程工作流程；
>
> (ii) 第2周：網絡數據收集、整理，從技術框架上了解爬蟲相關基礎 (resquest,pyquery,selenium)，結合 AI 工具實現數據收集；
>
> (ii) 第3周：學習 numpy，pandas 等數據處理包的基本術語，結合 AI 工具實現數據處理或者甚至是搭建數據自動化處理的技術流程；
>
> (v)第4周：過往研究項目中遇到的數據處理任務，編程技術相關的分享與討論；

#  week 1 （基礎主題，下載安裝&配置）

> workshop.w1 分享內容快速預覽：

- 介紹 AI(chatGPT/github copilot/github copilot labs/cursor) copilot 輔助編程工作流程；
- 安裝編程環境：python 或 miniconda；
- 安裝編輯器工具：vscode 及相關擴展包；
- 解決所有安裝或配置時出現的問題；
- 介紹編程相關術語（chatGPT對話需要， prompting）
- python 基礎 (語言;流程控制;邏輯處理;面向對象編程;面向函數編程;等基本概念)
- Hello, World  本地 cmd/jupyter/ coding 練習；
- 結合 chatGPT 完成一個或多個對話式輔助編程的練習；
- 總結 。

>相關細節: 

- AI: chatGPT/GitHub Copilot/cursor 輔助編程介紹：介紹結合辅助编程,自我学习或改进代码工作流程；

  - 註冊帳號 -> 獲取或分配權限 -> 搭建編程環境  -> 輔助工具或擴展包配置 -> happy coding!!
- <span style="color:#FF0000;font-weight:bold;">請提前完成帳號註冊：</span >
  - 谷歌帳號（推薦）
  - [chatGPT ](https://chat.openai.com/chat) 帳號申請（需要VPN，可用谷歌帳號關聯註冊）
  - [GitHub](https://github.com/) 請使用 HKpolyU 郵箱或其它，并完成教育用戶認證 。
  - [cursor](https://www.cursor.so/) 使用GitHub 關聯登陸，授權使用即可。
- 輔助平臺或社區網站介紹
  - [chatGPT ](https://chat.openai.com/chat) 簡介；
  - [google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=Nma_JWh-W-IF) 簡介
  - [GitHub](https://github.com/)简介：介绍GitHub及其用途，并介绍GitHub上可用的一些Python项目和代码库。

- 编程环境相關簡介；
  - python 簡介；
  - miniconda 簡介；

- 開始安裝，解決安裝或配置時出現的問題
  - 安裝 miniconda；
  - `pip install ****` 安裝 python 庫流程；
  - 啟動python，啟動jupyternotebook；
  - 安裝 vscode；
  - 安裝 vscode 擴展包：python/jupyter notebook/git/github copilot/github copilot labs；
  - 安裝cursor；

- python 語言編譯器相關簡介；

  - cmd （命令行窗口）
  - jupyter notebook （交互性編程）
  - **vscode** extension GitHub Copilot 提示式編程、自動補全
  - **vs code** extension GitHub Copilot Labs 代碼解釋、語言轉換、bug修正等
  - [chatGPT](https://chat.openai.com/chat)：對話式輔助編程 （不是編輯器）
  - [cursor](https://www.cursor.so/)：對話式編程工具（基于chatGPT api 或訂閱會員）
- 总结：总结研讨会内容，并为参与者提供资源和建议，以便他们在自己的项目中使用Python和GitHub。

> 可選內容細節:

- Git和GitHub基础：介绍Git版本控制系统和如何在GitHub上托管代码。
- Python和GitHub的集成：展示如何使用Python和GitHub集成，例如如何克隆GitHub存储库，如何对其进行修改和提交更改。
- 使用vscode进行GitHub自动化：展示如何使用Python编写脚本来自动化GitHub上的一些任务，例如创建存储库、问题和拉取请求。
- 练习：提供一些练习，让参与者尝试使用Python和GitHub进行一些简单的自动化任务。

> 註冊帳號,軟件下載及安裝

- [x] chatGPT

  |      | 網頁                   | URL                                          | 访问要求 | 使用 |
  | ---- | ---------------------- | -------------------------------------------- | -------- | ---- |
  | 1    | chatGPT                | https://chat.openai.com/chat                 | VPN      | ✓    |
  | 2    | chatGPT **playground** | https://platform.openai.com/playground       | VPN      | ✓    |
  | 3    | chatGPT **API**        | https://platform.openai.com/account/api-keys | VPN      | ✓    |
  
- [x] GitHub
  
  |      | 網頁             | URL                                | 访问要求                          | 使用 |
  | ---- | ---------------- | ---------------------------------- | --------------------------------- | ---- |
  | 1    | GitHub           | https://github.com/                | HK可訪問                          | ✓    |
  | 2    | education GitHub | https://education.github.com/      | HK可訪問,教育用戶認證             | ✓    |
  | 3    | GitHub Copilot   | https://docs.github.com/zh/copilot | 教育用戶認證通過后,免費 (5星推薦) | ✓    |
  
- [x] 下載與安裝
  
  |      | 編程環境包 | download link/page                                           | 版本號                                                       | 使用 |
  | ---- | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
  | 1    | miniconda  | [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/) | [Miniconda3-py39_4.12.0-Windows-x86_64.exe](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py39_4.12.0-Windows-x86_64.exe) | ✓    |
  | 2    | anaconda   | [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=S&O=A) | -                                                            | ✘    |
  
  |      | 編輯器 | download link/page                       | 版本號       | 使用 |
  | ---- | ------ | ---------------------------------------- | ------------ | ---- |
  | 1    | vscode | [vscode](https://code.visualstudio.com/) | version 1.77 | ✓    |
  | 2    | cursor | [cursor](https://www.cursor.so/)         | -            | ✓    |



# week2 (網絡數據收集主題)

> workshop.w2 分享內容快速預覽：

- chatGPT 對話場景下,自我學習以下內容
- python 基礎回顧、完善、補充3 (語法;流程控制;邏輯處理;面向對象編程;面向函數編程;等基本概念)
- python 網絡數據整理或收集 (request;pyquery;selenium)
- 網站數據請求，數據響應獲取；網頁結構，標籤解析等；
- 自動化測試工具 selenium 請求動態網站數據；

> 其它細節未完成，歡迎留言補充

# week3 (數據處理&分析主題)

> workshop.w3 分享內容快速預覽：

- chatGPT 對話場景下,自我學習以下內容
- python 基礎回顧、完善、補充3 (語法;流程控制;邏輯處理;面向對象編程;面向函數編程;等基本概念)
- python numpy， pandas 庫常用命令；
- 複雜數據讀取，處理，及自動化處理；
- 提供一些練習結合 AI 輔助工具解決任務需求

> 其它細節未完成，歡迎留言補充



# week4 (問題分享與討論)

> workshop.w4 分享內容快速預覽：

- 過往研究項目中遇到的數據處理任務，編程技術相關的分享與討論；

  

  


## 參考

- Anaconda使用教程一（新手友好）https://zhuanlan.zhihu.com/p/348120084





