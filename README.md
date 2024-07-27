# Wafer mapping image viewer

## 專案描述

**繪製wafer mapping，並擷取chip資訊的小程式**

![Static Badge](https://img.shields.io/badge/Suppprted_file-CSV-red)

- 可以繪製指定wafer與項目的mapping圖
- 在mapping圖上滑動時，可以看個別chip資訊
- 可以擷取指定之chip資訊，並存出csv檔

## 使用方式

### 讀取檔案

按下"讀取檔案"，並選擇wafer mapping的檔案<br>
一次可讀取多個檔案<br>
Wafer讀取完成後，狀態列會顯示讀取wafer與chip數目<br>


<img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMG93ZmZuZm13dTVrbXZ3M2t0bHVkbGJiNHA5YnZkY2s3NzlrbW8yZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Jo3QYk0DKoGN9DBua8/giphy.gif width="80%" height="80%" />

### 繪製wafer mapping檔案

檔案讀取完成後，按下繪製圖像<br>
Wafer mapping圖像會在另一視窗跳出<br>

    Wafer ID: 選擇想繪製的Wafer ID
    繪圖項目：選擇想看的項目
    Color上下限：可以設置圖像繪製的上下限，上下限須同時設定或同時不設定

<img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTA3bmdyanBjbGt0Zmc5Zzd1Nnoyb2VqYnNha3Fscjlvenl3bWFoNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fRmhC2B5u3rUMqqp0z/giphy.gif width="80%" height="80%" />

### 確認wafer mapping的各點數值

鼠標在mapping圖上滑動時，即可在data table確認該顆chip資訊

<img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcm94NWN3YjNiMGFoYjk1b3FzZTUzYjFqanN2ZDEwdzczaXRxZmNsaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uy8yyfcsqxE6cGzhB6/giphy.gif width="80%" height="80%" />

### 擷取指定chip之資訊並儲存

#### 擷取指定chip

鼠標在chip上方並按下左鍵時，可以擷取該chip的資訊<br>

<img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmFqM3cxOWpodGtrZHNjaDNyOWVjZzZuMWhvaGVyN2xzdmhsZnJiaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/a28iTAkyJvs52sIYiV/giphy.gif width="80%" height="80%" />

#### 儲存chip資訊

鼠標在mapping圖上方並按下右鍵時，可以刪除最後一筆chip的資訊<br>
> 按下"儲存chip資訊"，可儲存已擷取之chip資訊

<img src=https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHFhNjR3NWR4bzlkdzh6c3NzNDM4cTQyNWk1MXp5c21hYWdoOWZrNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/x1uvr7MbkdAQkAdIEf/giphy.gif width="80%" height="80%" />



### 另存wafer mapping圖像
在圖面視窗按下存檔及可儲存檔案

<img src=https://i.imgur.com/cfA8qCa.png width="70%" height="80%" />

## 運行方式與相關文件說明

### 運行方式

cd到`firstMainWinRun.py`的路徑，並在cmd執行以下指令

```python
py firstMainWinRun.py
```

### 相關文件說明

    main.ui: 使用QT disigner編輯之UI檔
    main.py: 將main.ui重新編譯後的py檔
    firstMainWinRun.py: 邏輯檔案，設定程式功能，讀取介面檔案(.py)並實例化
    wafer_mapping: 測試用wafer mapping檔案

## 編寫環境

### Python 3.12.1

### 相關模組

    numpy 1.26.3
    matplotlib 3.8.2
    pandas 2.2.0
    PySide6 6.6.0

## 待更新項目

- 一次輸出多張wafer mapping
- 針對wafer mapping的 color bar 美化