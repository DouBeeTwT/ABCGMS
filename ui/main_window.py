from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QStackedWidget, QToolBar, QSizePolicy,
                             QLineEdit, QFrame, QSpacerItem)
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt
import qtawesome as qta

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ABCGMS')
        self.resize(1200, 600)
        self.initUI()

    def initUI(self):
        # 设置应用主题色
        self.setStyleSheet("""
            QMainWindow { 
                background-color: #f5f6f7; 
                border: none;
            }
            QToolBar { background-color: #3f51b5; color: white; border: none; }
            QToolBar QToolButton { color: white; padding: 8px; margin: 0; border: none; }
            QToolBar QToolButton:hover { background-color: #5c6bc0; }
            QLineEdit { padding: 5px; border: 1px solid #ddd; border-radius: 4px; }
            QPushButton { padding: 5px 15px; margin-bottom: 10px; }
        """)

        # 创建中央部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 创建左侧导航栏
        nav_widget = QFrame()
        nav_widget.setStyleSheet("background-color: #303f9f; color: white; min-width: 200px; max-width: 200px;")
        nav_layout = QVBoxLayout(nav_widget)
        nav_layout.setContentsMargins(0, 10, 0, 0)
        nav_layout.setSpacing(5)

        # 创建导航按钮
        def create_nav_button(icon, text):
            btn = QPushButton(qta.icon(icon, color='white', size=20), text)
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 12px 20px;
                    border: none;
                    color: white;
                    background: transparent;
                    font-size: 20px;
                    border-radius: 8px;
                    margin: 5px 15px;
                }
                QPushButton:hover {
                    background-color: #3949ab;
                }
            """)
            return btn

        info_btn = create_nav_button('fa5s.info-circle', '信息')
        image_btn = create_nav_button('fa5s.image', '图像')
        analysis_btn = create_nav_button('fa5s.chart-bar', '分析')
        report_btn = create_nav_button('fa5s.file-alt', '报告')

        nav_layout.addWidget(info_btn)
        nav_layout.addWidget(image_btn)
        nav_layout.addWidget(analysis_btn)
        nav_layout.addWidget(report_btn)
        nav_layout.addStretch()

        # 创建设置按钮
        settings_btn = create_nav_button('fa5s.cog', '设置')
        nav_layout.addWidget(settings_btn)

        main_layout.addWidget(nav_widget)

        # 创建右侧内容区域
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)

        # 创建堆叠部件用于页面切换
        self.stacked_widget = QStackedWidget()

        # 创建并添加页面
        from .info_page import InfoPage
        from .image_page import ImagePage
        from .analysis_page import AnalysisPage
        from .report_page import ReportPage
        from .settings_page import SettingsPage

        self.info_page = InfoPage()
        self.image_page = ImagePage()
        self.analysis_page = AnalysisPage()
        self.report_page = ReportPage()
        self.settings_page = SettingsPage()

        self.stacked_widget.addWidget(self.info_page)
        self.stacked_widget.addWidget(self.image_page)
        self.stacked_widget.addWidget(self.analysis_page)
        self.stacked_widget.addWidget(self.report_page)
        self.stacked_widget.addWidget(self.settings_page)

        # 连接导航按钮的点击事件
        info_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.info_page))
        image_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.image_page))
        analysis_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.analysis_page))
        report_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.report_page))
        settings_btn.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.settings_page))

        # 添加堆叠部件到右侧布局
        content_layout.addWidget(self.stacked_widget)

        # 创建右侧容器并设置布局
        content_widget = QWidget()
        content_widget.setLayout(content_layout)
        main_layout.addWidget(content_widget)

        # 设置默认显示的页面
        self.stacked_widget.setCurrentWidget(self.info_page)