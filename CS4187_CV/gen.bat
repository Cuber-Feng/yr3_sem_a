@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul

echo.
echo === 开始转换Markdown文件至HTML ===

rem -- 使用 for 循环遍历当前目录下的所有 .md 文件 --
for %%f in (*.md) do (
    rem -- 获取当前文件名（不含扩展名） --
    set "filename=%%~nf"

    rem -- 替换文件名中的所有空格为下划线 --
    set "html_filename=!filename: =_!"

    echo.
    echo 正在转换： "%%f" -> "!html_filename!.html"

    rem -- 调用 Pandoc 进行转换，并使用 -s 参数包含样式 --
    pandoc -s "%%f" -o "!html_filename!.html" --css ../style.css
    
    rem -- 检查 Pandoc 是否成功执行 --
    if errorlevel 1 (
        echo 警告：Pandoc 转换失败，请检查文件 "%%f" 是否有错误。
    )
)

echo.
echo === 所有文件转换完成 ===