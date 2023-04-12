 **Last Update:** 23.04.12

**Keys:** `chatGPT` `Python` `GitHub` `GitHub Copilot`  `Cursor` `Google Colaboratory`

> # week 1 （基礎主題，下載安裝&配置）

> 分享內容快速預覽：

- 介紹 AI(chatGPT/github copilot/github copilot labs/cursor) copilot 輔助編程工作流程；
- 安裝編程環境：python 或 miniconda；
- 安裝編輯器工具：vscode 及相關擴展包；
- 解決所有安裝或配置時出現的問題；
- 介紹編程相關術語（chatGPT對話需要， prompting）
- python 基礎1 (語言;流程控制;邏輯處理;面向對象編程;面向函數編程;等基本概念)
- Hello, World  本地 cmd/jupyter/ coding 練習；
- 結合 chatGPT 完成一個或多個對話式輔助編程的練習；
- 總結 。

> 收穫：

- 通過以上內容的了解， 你已經具備結合 AI 工具實現編程的能力，儘管你可能是個python 語言初學者；
- 倘若你熟悉 python 語言及其它語言特性，那麼以上內容可能會幫助你提升編程效率；
- 你的筆記本或電腦 python 編程環境已經配置完畢，可以隨時創作python 項目； 

>內容相關細節: 

- AI: chatGPT/GitHub Copilot/cursor 輔助編程介紹：介紹結合辅助编程,自我学习或改进代码工作流程；

  - 註冊帳號 -> 獲取或分配權限 -> 搭建編程環境  -> 輔助工具或擴展包配置 -> happy coding!!
- <span style="color:#FF0000;font-weight:bold;">請提前完成帳號註冊：</span >
  - 谷歌帳號（推薦）
  - [chatGPT ](https://chat.openai.com/chat) 帳號申請（需要VPN，可用谷歌帳號關聯註冊）
  - [GitHub](https://github.com/) 請使用 HKpolyU 郵箱或其它，并完成教育用戶認證 。
    - 在 polyu 校園ip 完成認證;
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
  
  - `pip`安裝 python 庫流程；
  
    ```
    pip install jupyter -U
  pip install jupyter notebook-U
    ```
  
    
  
  - 安裝 Git, 配置 郵箱與用戶名
  
    ```git
    git --version
    
    git config --global user.email "you@example.com"
    
    git config --global user.name "Your Name"
    ```
  
  - 安裝 VPN
  
  - 重啟電腦, 
  
  - 通過 cmd 啟動python，啟動jupyternotebook；
  
  - 安裝 vscode；
  
  - 安裝 vscode 擴展包：python/jupyter notebook/git/github copilot/github copilot labs；
  
    - github 配置時,需要登陸;
    - github copilot 最新版存在bug,需要回退版本 1.63.7601, 右下角正常顯示圖標后,登陸使用;
  
  - 安裝cursor；
  
    - 利用github 帳號登陸;
    - https://platform.openai.com/account/api-keys
  
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






## 參考<!-- {docsify-ignore} -->

- Anaconda使用教程一（新手友好）https://zhuanlan.zhihu.com/p/348120084





