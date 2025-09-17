@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul

echo.
echo === 开始转换所有Markdown文件至HTML ===

rem -- 使用 for /r 循环递归遍历当前目录及所有子目录下的 .md 文件 --
for /r %%f in (*.md) do (
    
    rem -- 获取当前文件名（带扩展名），例如 "README.md" --
    set "full_filename=%%~nxf"
    
    rem -- 如果文件名是 README.md，则跳过 --
    if /i "!full_filename!"=="README.md" (
        echo.
        echo 跳过 README.md 文件。
    ) else (
        rem -- 获取当前文件名（不含扩展名） --
        set "filename=%%~nf"

        rem -- 替换文件名中的所有空格为下划线 --
        set "html_filename=!filename: =_!"

        rem -- 获取当前文件所在目录的路径 --
        set "file_path=%%~dpf"

        echo.
        echo 正在转换： "%%f" -> "!file_path!!html_filename!.html"

        rem -- 调用 Pandoc 进行转换 --
        pandoc -s "%%f" -o "!file_path!!html_filename!.html" --css ../style.css
        
        rem -- 检查 Pandoc 是否成功执行 --
        if errorlevel 1 (
            echo 警告：Pandoc 失败，请检查文件 "%%f" 是否有错误。
        )
    )
)

echo.
echo === 所有文件转换完成 ===
pause