# -- Project information -----------------------------------------------------
project = 'Smart Home Quick Start Guide'
copyright = '2025, Lafvin'
author = 'Lafvin'

# -- General configuration ---------------------------------------------------
extensions = ["myst_parser"]

from pygments.lexers import Python3Lexer
pygments_lexers = {
    "python-repl": Python3Lexer(),
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# 指定 logo 图片（放在 docs/_static/Logo2.png）
html_logo = "_static/Logo2.png"

# 静态资源目录（必须保留 _static）
html_static_path = ['_static']

# 主题选项
html_theme_options = {
    'logo_only': False,        # 显示 logo + 项目名称
    'display_version': False,  # 不显示版本号
    'navigation_depth': 4,     # 导航层级
    'collapse_navigation': False,
    'style_nav_header_background': "#2980B9",  # 顶部蓝色
}

# 加载自定义 CSS
html_css_files = [
    'custom.css',
]

# 代码高亮
pygments_style = "sphinx"
pygments_dark_style = "monokai"
