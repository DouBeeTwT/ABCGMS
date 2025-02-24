from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLabel, QFrame, QScrollArea, QGridLayout, QSizePolicy)
from PyQt6.QtCore import Qt
import qtawesome as qta

class ImageCard(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #e9ecef;
            }
            QFrame:hover {
                border: 1px solid #4a69bd;
                background-color: #fafafa;
            }
        """)
        self.setMinimumSize(200, 200)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

class ImagePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # 顶部工具栏
        toolbar = QFrame()
        toolbar.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                padding: 10px;
            }
        """)
        toolbar_layout = QHBoxLayout(toolbar)

        # 添加图片按钮
        add_btn = QPushButton(qta.icon('fa5s.plus', color='#4a69bd'), '添加图片')
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #4a69bd;
                color: white;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #5c6bc0;
            }
        """)
        toolbar_layout.addWidget(add_btn)
        toolbar_layout.addStretch()

        layout.addWidget(toolbar)

        # 图片网格容器
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)

        container = QWidget()
        grid_layout = QGridLayout(container)
        grid_layout.setSpacing(20)

        # 添加示例图片卡片
        for i in range(6):
            card = ImageCard()
            row = i // 3
            col = i % 3
            grid_layout.addWidget(card, row, col)

        scroll.setWidget(container)
        layout.addWidget(scroll)