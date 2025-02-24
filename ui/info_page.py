from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class InfoPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        # 添加页面标题
        title = QLabel('信息')
        title.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title)

        # 添加内容区域
        content = QLabel('信息页面内容区域')
        content.setStyleSheet("""
            QLabel {
                color: #34495e;
                font-size: 16px;
            }
        """)
        layout.addWidget(content)

        # 添加弹性空间
        layout.addStretch()