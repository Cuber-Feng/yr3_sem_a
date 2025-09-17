import os
import re

def generate_index_html(root_dir="."):
    """遍历目录并生成一个按文件夹分类的HTML文件索引。"""
    
    html_content = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Notes (Year 3 Sem A)</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 2em; background-color: #f8f9fa; color: #333; }
            h1 { text-align: center; color: #1a1a1a; }
            h2 { margin-top: 2em; color: #007bff; border-bottom: 2px solid #ccc; padding-bottom: 0.5em; }
            ul { list-style-type: none; padding: 0; }
            li { margin-bottom: 0.5em; background-color: #ffffff; padding: 1em; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
            a { text-decoration: none; color: #333; font-weight: bold; }
            a:hover { text-decoration: underline; color: #007bff; }
            .folder-list { margin-top: 1em; }
            .folder-list li { margin-left: 2em; background-color: #f1f3f5; }
            footer {
                padding-top: 1rem;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>My Notes</h1>
    """
    
    # 存储文件夹及其包含的HTML文件
    folder_map = {}
    
    # 遍历目录
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 排除 .git 目录
        if '.git' in dirpath:
            continue
            
        # 获取当前文件夹的相对路径
        relative_folder_path = os.path.relpath(dirpath, root_dir)
        
        # 忽略根目录下的index.html文件
        if relative_folder_path == '.' and "index.html" in filenames:
            filenames.remove("index.html")

        # 检查当前文件夹是否有html文件
        html_files_in_folder = [f for f in filenames if f.endswith(".html")]
        
        if html_files_in_folder:
            folder_map[relative_folder_path] = html_files_in_folder
            
    # 根据文件夹生成HTML内容
    for folder_path, files in sorted(folder_map.items()):
        # 获取文件夹名称
        folder_name = os.path.basename(folder_path)
        if folder_name == '.':
            folder_name = "根目录"
            
        html_content += f'<h2>{folder_name}</h2>\n<ul class="folder-list">\n'
        
        for filename in sorted(files):
            relative_path = os.path.join(folder_path, filename)
            link_text = re.sub(r'\.html$', '', filename)
            html_content += f'<li><a href="{relative_path}">{link_text}</a></li>\n'
        
        html_content += '</ul>\n'

    html_content += """
        <footer>
            By Maple Feng
        </footer>
    </body>
    </html>
    """
    
    with open(os.path.join(root_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("index.html 文件已生成！")

if __name__ == "__main__":
    generate_index_html()