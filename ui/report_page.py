from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QSplitter, QGroupBox, QFormLayout, QComboBox, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import qtawesome as qta

class ReportPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建主布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        # 创建工具栏
        toolbar = QHBoxLayout()
        layout.addLayout(toolbar)

        # 添加生成报告按钮
        generate_btn = QPushButton('生成报告')
        generate_btn.setIcon(qta.icon('fa5s.file-medical-alt'))
        generate_btn.clicked.connect(self.generate_report)
        toolbar.addWidget(generate_btn)

        # 添加导出报告按钮
        export_btn = QPushButton('导出报告')
        export_btn.setIcon(qta.icon('fa5s.file-export'))
        export_btn.clicked.connect(self.export_report)
        toolbar.addWidget(export_btn)

        toolbar.addStretch()

        # 创建内容区域
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        layout.addWidget(content_widget)

        # 创建左侧分割器
        left_splitter = QSplitter(Qt.Orientation.Vertical)
        content_layout.addWidget(left_splitter)

        # 创建基本信息分组
        basic_info_group = QGroupBox('基本信息')
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
        image_preview_layout = QVBoxLayout(image_preview_group)

        # 创建文件选择区域
        file_layout = QHBoxLayout()
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText('请选择图像文件...')
        self.file_path.setReadOnly(True)
        file_layout.addWidget(self.file_path)

        select_button = QPushButton('选择文件')
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
        report_layout = QVBoxLayout(report_group)
        self.report_edit = QTextEdit()
        report_layout.addWidget(self.report_edit)

        # 添加左侧分割器和右侧报告区域到内容布局
        content_layout.addWidget(left_splitter)
        content_layout.addWidget(report_group)

    def select_file(self):
        # TODO: 实现文件选择功能
        pass

    def generate_report(self):
        # TODO: 实现报告生成功能
        pass

    def export_report(self):
        # TODO: 实现报告导出功能
        pass