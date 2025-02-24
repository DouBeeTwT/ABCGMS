from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QPushButton, QLabel, QFileDialog, QSplitter, QGroupBox, QTextEdit,
                             QComboBox, QFormLayout)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import qtawesome as qta

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('ABCGMS-GUI')
        self.setGeometry(100, 100, 1200, 800)
        
        # 设置窗口图标
        self.setWindowIcon(qta.icon('fa5s.window-maximize'))

        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建导航栏
        self.navbar = QWidget()
        self.navbar.setObjectName('navbar')
        self.navbar.setFixedHeight(50)
        self.navbar.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                border-bottom: 1px solid #3a3a3a;
            }
        """)
        navbar_layout = QHBoxLayout(self.navbar)
        navbar_layout.setContentsMargins(10, 5, 10, 5)
        navbar_layout.addStretch()

        # 将主题切换和语言切换按钮移动到导航栏
        self.theme_switch = QPushButton()
        self.theme_switch.setCheckable(True)
        self.theme_switch.setIcon(qta.icon('fa5s.sun'))
        self.theme_switch.setToolTip('切换主题')
        self.theme_switch.clicked.connect(self.toggle_theme)
        navbar_layout.addWidget(self.theme_switch)

        self.lang_switch = QPushButton()
        self.lang_switch.setCheckable(True)
        self.lang_switch.setIcon(qta.icon('fa5s.language'))
        self.lang_switch.setToolTip('切换语言')
        self.lang_switch.clicked.connect(self.toggle_language)
        navbar_layout.addWidget(self.lang_switch)

        # 创建主布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 添加导航栏到主布局
        main_layout.addWidget(self.navbar)

        # 创建内容区域
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.addWidget(content_widget)

        # 创建左侧分割器
        left_splitter = QSplitter(Qt.Orientation.Vertical)
        content_layout.addWidget(left_splitter)

        # 创建基本信息分组
        basic_info_group = QGroupBox('基本信息')
        basic_info_group.setObjectName('basic_info_group')
        basic_info_layout = QFormLayout(basic_info_group)

        # 创建基本信息下拉菜单
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(['请选择性别', '男', '女'])
        basic_info_layout.addRow('性别:', self.gender_combo)

        self.age_combo = QComboBox()
        self.age_combo.addItems(['请选择年龄'] + [str(i) for i in range(1, 121)])
        basic_info_layout.addRow('年龄:', self.age_combo)

        self.smoking_combo = QComboBox()
        self.smoking_combo.addItems(['是否吸烟', '是', '否'])
        basic_info_layout.addRow('吸烟:', self.smoking_combo)

        self.drinking_combo = QComboBox()
        self.drinking_combo.addItems(['是否酗酒', '是', '否'])
        basic_info_layout.addRow('酗酒:', self.drinking_combo)

        self.family_history_combo = QComboBox()
        self.family_history_combo.addItems(['是否有疾病家族史', '是', '否'])
        basic_info_layout.addRow('疾病家族史:', self.family_history_combo)

        left_splitter.addWidget(basic_info_group)

        # 创建月经信息分组
        menstrual_info_group = QGroupBox('月经信息')
        menstrual_info_group.setObjectName('menstrual_info_group')
        menstrual_info_layout = QFormLayout(menstrual_info_group)

        # 创建月经信息下拉菜单
        self.menarche_combo = QComboBox()
        self.menarche_combo.addItems(['请选择初潮年龄'] + [str(i) for i in range(8, 21)])
        menstrual_info_layout.addRow('初潮年龄:', self.menarche_combo)

        self.period_duration_combo = QComboBox()
        self.period_duration_combo.addItems(['请选择月经持续时间'] + [f'{i}天' for i in range(1, 11)])
        menstrual_info_layout.addRow('月经持续时间:', self.period_duration_combo)

        self.period_cycle_combo = QComboBox()
        self.period_cycle_combo.addItems(['请选择月经周期'] + [f'{i}天' for i in range(20, 41)])
        menstrual_info_layout.addRow('月经周期:', self.period_cycle_combo)

        self.pregnancy_combo = QComboBox()
        self.pregnancy_combo.addItems(['是否有过怀孕', '是', '否'])
        menstrual_info_layout.addRow('怀孕史:', self.pregnancy_combo)

        self.menopause_combo = QComboBox()
        self.menopause_combo.addItems(['是否停经', '是', '否'])
        menstrual_info_layout.addRow('停经状态:', self.menopause_combo)

        left_splitter.addWidget(menstrual_info_group)

        # 创建图像预览区域组
        image_preview_group = QGroupBox('图像预览')
        image_preview_group.setObjectName('image_preview_group')
        image_preview_layout = QVBoxLayout(image_preview_group)

        # 创建文件选择区域
        file_layout = QHBoxLayout()
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText('请选择图像文件...')
        self.file_path.setReadOnly(True)
        file_layout.addWidget(self.file_path)

        select_button = QPushButton('选择文件')
        select_button.setObjectName('select_button')
        select_button.clicked.connect(self.select_file)
        select_button.setIcon(qta.icon('fa5s.folder-open'))
        file_layout.addWidget(select_button)
        image_preview_layout.addLayout(file_layout)

        # 创建图像预览区域
        self.image_preview = QLabel()
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_preview.setMinimumSize(400, 300)
        self.image_preview.setText('暂无图片预览')
        image_preview_layout.addWidget(self.image_preview)
        left_splitter.addWidget(image_preview_group)

        # 创建右侧自动化报告区域
        report_group = QGroupBox('自动化报告')
        report_group.setObjectName('report_group')
        report_layout = QVBoxLayout(report_group)
        self.report_edit = QTextEdit()
        report_layout.addWidget(self.report_edit)

        # 添加左侧分割器和右侧报告区域到内容布局
        content_layout.addWidget(left_splitter)
        content_layout.addWidget(report_group)

        # 设置深色主题
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QGroupBox {
                border: 2px solid #3a3a3a;
                border-radius: 5px;
                margin-top: 1em;
                padding-top: 10px;
            }
            QGroupBox::title {
                color: #ffffff;
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
            }
            QLineEdit, QTextEdit {
                background-color: #3a3a3a;
                border: 1px solid #505050;
                color: #ffffff;
                border-radius: 3px;
                padding: 2px;
                min-width: 120px;
            }
            QComboBox:hover {
                border: 1px solid #606060;
            }
            QComboBox::drop-down {
                border: none;
                background-color: #505050;
                width: 20px;
            }
            QComboBox::drop-down:hover {
                background-color: #606060;
            }
            QComboBox::down-arrow {
                width: 12px;
                height: 12px;
                image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
            }
            QPushButton {
                background-color: #505050;
                border: none;
                color: #ffffff;
                padding: 5px 15px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #606060;
            }
            QLabel {
                border: 1px solid #3a3a3a;
                background-color: #2b2b2b;
            }
        """)

        # 设置分割器样式
        left_splitter.setStyleSheet("""
            QSplitter::handle {
                background-color: #3a3a3a;
            }
        """)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "选择图像文件",
            "",
            "图像文件 (*.png *.jpg *.jpeg *.bmp *.gif);;所有文件 (*.*)"
        )
        if file_name:
            self.file_path.setText(file_name)
            self.show_image(file_name)

    def show_image(self, file_path):
        pixmap = QPixmap(file_path)
        if not pixmap.isNull():
            # 按比例缩放图片以适应预览区域
            scaled_pixmap = pixmap.scaled(
                self.image_preview.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_preview.setPixmap(scaled_pixmap)
        else:
            self.image_preview.setText('无法加载图片')

    def toggle_theme(self):
        if self.theme_switch.isChecked():
            # 切换到亮色主题
            # 更新导航栏样式
            self.navbar.setStyleSheet("""
                QWidget {
                    background-color: #e0e0e0;
                    border-bottom: 1px solid #d0d0d0;
                }
            """)
            
            self.setStyleSheet("""
                QMainWindow, QWidget {
                    background-color: #f0f0f0;
                    color: #000000;
                }
                QGroupBox {
                    border: 2px solid #d0d0d0;
                    border-radius: 5px;
                    margin-top: 1em;
                    padding-top: 10px;
                }
                QGroupBox::title {
                    color: #000000;
                    subcontrol-origin: margin;
                    left: 10px;
                    padding: 0 3px 0 3px;
                }
                QLineEdit, QTextEdit {
                    background-color: #ffffff;
                    border: 1px solid #d0d0d0;
                    color: #000000;
                    border-radius: 3px;
                    padding: 2px;
                    min-width: 120px;
                }
                QComboBox:hover {
                    border: 1px solid #a0a0a0;
                }
                QComboBox::drop-down {
                    border: none;
                    background-color: #e0e0e0;
                    width: 20px;
                }
                QComboBox::drop-down:hover {
                    background-color: #d0d0d0;
                }
                QComboBox::down-arrow {
                    width: 12px;
                    height: 12px;
                    image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24'%3E%3Cpath fill='black' d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
                }
                QPushButton {
                    background-color: #e0e0e0;
                    border: none;
                    color: #000000;
                    padding: 5px 15px;
                    border-radius: 3px;
                }
                QPushButton:hover {
                    background-color: #d0d0d0;
                }
                QLabel {
                    border: 1px solid #d0d0d0;
                    background-color: #f0f0f0;
                }
            """)
            self.theme_switch.setIcon(qta.icon('fa5s.moon'))
        else:
            # 切换到深色主题
            # 更新导航栏样式
            self.navbar.setStyleSheet("""
                QWidget {
                    background-color: #1a1a1a;
                    border-bottom: 1px solid #3a3a3a;
                }
            """)
            
            self.setStyleSheet("""
                QMainWindow, QWidget {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QGroupBox {
                    border: 2px solid #3a3a3a;
                    border-radius: 5px;
                    margin-top: 1em;
                    padding-top: 10px;
                }
                QGroupBox::title {
                    color: #ffffff;
                    subcontrol-origin: margin;
                    left: 10px;
                    padding: 0 3px 0 3px;
                }
                QLineEdit, QTextEdit {
                    background-color: #3a3a3a;
                    border: 1px solid #505050;
                    color: #ffffff;
                    border-radius: 3px;
                    padding: 2px;
                    min-width: 120px;
                }
                QComboBox:hover {
                    border: 1px solid #606060;
                }
                QComboBox::drop-down {
                    border: none;
                    background-color: #505050;
                    width: 20px;
                }
                QComboBox::drop-down:hover {
                    background-color: #606060;
                }
                QComboBox::down-arrow {
                    width: 12px;
                    height: 12px;
                    image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
                }
                QPushButton {
                    background-color: #505050;
                    border: none;
                    color: #ffffff;
                    padding: 5px 15px;
                    border-radius: 3px;
                }
                QPushButton:hover {
                    background-color: #606060;
                }
                QLabel {
                    border: 1px solid #3a3a3a;
                    background-color: #2b2b2b;
                }
            """)
            self.theme_switch.setIcon(qta.icon('fa5s.sun'))

    def toggle_language(self):
        try:
            if self.lang_switch.isChecked():
                # 切换到英文
                self.setWindowTitle('ABCGMS-GUI')
                self.theme_switch.setToolTip('Toggle Theme')
                self.lang_switch.setToolTip('Toggle Language')
                self.file_path.setPlaceholderText('Please select an image file...')
                self.image_preview.setText('No image preview')
                
                # 更新基本信息组
                basic_info_group = self.findChild(QGroupBox, 'basic_info_group')
                if basic_info_group:
                    basic_info_group.setTitle('Basic Information')
                    # 更新基本信息标签
                    for i, label in enumerate(['Gender:', 'Age:', 'Smoking:', 'Drinking:', 'Family History:']):
                        basic_info_group.layout().itemAt(i, QFormLayout.ItemRole.LabelRole).widget().setText(label)
                
                # 更新下拉菜单选项
                self.gender_combo.clear()
                self.gender_combo.addItems(['Select Gender', 'Male', 'Female'])
                
                self.age_combo.clear()
                self.age_combo.addItems(['Select Age'] + [str(i) for i in range(1, 121)])
                
                self.smoking_combo.clear()
                self.smoking_combo.addItems(['Smoking Status', 'Yes', 'No'])
                
                self.drinking_combo.clear()
                self.drinking_combo.addItems(['Drinking Status', 'Yes', 'No'])
                
                self.family_history_combo.clear()
                self.family_history_combo.addItems(['Family History', 'Yes', 'No'])
                
                # 更新月经信息组
                menstrual_info_group = self.findChild(QGroupBox, 'menstrual_info_group')
                if menstrual_info_group:
                    menstrual_info_group.setTitle('Menstrual Information')
                    # 更新月经信息标签
                    for i, label in enumerate(['Menarche Age:', 'Period Duration:', 'Period Cycle:', 'Pregnancy History:', 'Menopause Status:']):
                        menstrual_info_group.layout().itemAt(i, QFormLayout.ItemRole.LabelRole).widget().setText(label)
                
                self.menarche_combo.clear()
                self.menarche_combo.addItems(['Select Menarche Age'] + [str(i) for i in range(8, 21)])
                
                self.period_duration_combo.clear()
                self.period_duration_combo.addItems(['Select Period Duration'] + [f'{i} days' for i in range(1, 11)])
                
                self.period_cycle_combo.clear()
                self.period_cycle_combo.addItems(['Select Period Cycle'] + [f'{i} days' for i in range(20, 41)])
                
                self.pregnancy_combo.clear()
                self.pregnancy_combo.addItems(['Pregnancy History', 'Yes', 'No'])
                
                self.menopause_combo.clear()
                self.menopause_combo.addItems(['Menopause Status', 'Yes', 'No'])
                
                # 更新图像预览组
                image_preview_group = self.findChild(QGroupBox, 'image_preview_group')
                if image_preview_group:
                    image_preview_group.setTitle('Image Preview')
                
                # 更新按钮文本
                select_button = self.findChild(QPushButton, 'select_button')
                if select_button:
                    select_button.setText('Select File')
                
                # 更新报告组
                report_group = self.findChild(QGroupBox, 'report_group')
                if report_group:
                    report_group.setTitle('Automated Report')
            else:
                # 切换到中文
                self.setWindowTitle('ABCGMS-GUI')
                self.theme_switch.setToolTip('切换主题')
                self.lang_switch.setToolTip('切换语言')
                self.file_path.setPlaceholderText('请选择图像文件...')
                self.image_preview.setText('暂无图片预览')
                
                # 更新基本信息组
                basic_info_group = self.findChild(QGroupBox, 'basic_info_group')
                if basic_info_group:
                    basic_info_group.setTitle('基本信息')
                    # 更新基本信息标签
                    for i, label in enumerate(['性别:', '年龄:', '吸烟:', '酗酒:', '疾病家族史:']):
                        basic_info_group.layout().itemAt(i, QFormLayout.ItemRole.LabelRole).widget().setText(label)
                
                # 更新下拉菜单选项
                self.gender_combo.clear()
                self.gender_combo.addItems(['请选择性别', '男', '女'])
                
                self.age_combo.clear()
                self.age_combo.addItems(['请选择年龄'] + [str(i) for i in range(1, 121)])
                
                self.smoking_combo.clear()
                self.smoking_combo.addItems(['是否吸烟', '是', '否'])
                
                self.drinking_combo.clear()
                self.drinking_combo.addItems(['是否酗酒', '是', '否'])
                
                self.family_history_combo.clear()
                self.family_history_combo.addItems(['是否有疾病家族史', '是', '否'])
                
                # 更新月经信息组
                menstrual_info_group = self.findChild(QGroupBox, 'menstrual_info_group')
                if menstrual_info_group:
                    menstrual_info_group.setTitle('月经信息')
                    # 更新月经信息标签
                    for i, label in enumerate(['初潮年龄:', '月经持续时间:', '月经周期:', '怀孕史:', '停经状态:']):
                        menstrual_info_group.layout().itemAt(i, QFormLayout.ItemRole.LabelRole).widget().setText(label)
                
                self.menarche_combo.clear()
                self.menarche_combo.addItems(['请选择初潮年龄'] + [str(i) for i in range(8, 21)])
                
                self.period_duration_combo.clear()
                self.period_duration_combo.addItems(['请选择月经持续时间'] + [f'{i}天' for i in range(1, 11)])
                
                self.period_cycle_combo.clear()
                self.period_cycle_combo.addItems(['请选择月经周期'] + [f'{i}天' for i in range(20, 41)])
                
                self.pregnancy_combo.clear()
                self.pregnancy_combo.addItems(['是否有过怀孕', '是', '否'])
                
                self.menopause_combo.clear()
                self.menopause_combo.addItems(['是否停经', '是', '否'])
                
                # 更新图像预览组
                image_preview_group = self.findChild(QGroupBox, 'image_preview_group')
                if image_preview_group:
                    image_preview_group.setTitle('图像预览')
                
                # 更新按钮文本
                select_button = self.findChild(QPushButton, 'select_button')
                if select_button:
                    select_button.setText('选择文件')
                
                # 更新报告组
                report_group = self.findChild(QGroupBox, 'report_group')
                if report_group:
                    report_group.setTitle('自动化报告')
        except Exception as e:
            print(f'Language switch error: {str(e)}')