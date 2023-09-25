# -*- coding:utf-8 -*-
import os
import time

IP = '127.0.0.1'

PORT = 10405

BASE_ROOT = os.path.dirname(os.path.abspath(__file__)) + os.path.sep

LOG_DIR = BASE_ROOT + 'logs/archive-{}.log'.format(time.strftime('%Y-%m-%d', time.localtime(time.time())))

STATIC_PATH = os.path.join(BASE_ROOT, 'static_files')

TEMPLATE_PATH = os.path.join(STATIC_PATH, 'template')

EXPORT_PATH = os.path.join(STATIC_PATH, 'export_files')

INSPECT_TYPE = {
    1: '日检',
    2: '隔日检',
    3: '半月检',
    4: '月检',
    5: '季检',
    6: '年检',
    7: '五年检',
    8: '十年检',
    9: '临时检',
}

FIND_TYPE = {
    1: 'FRACAS',
    2: '报警中心',
    3: '巡检报单',
}

FAULT_TP = {
    1: '正线故障',
    2: '库内故障',
}

LOCALIZATION_OR_OUTSOURCING = {
    1: '自主化',
    2: '外购',
}

DEAL_STATUS = {
    1: '待处理',
    2: '检修中',
    3: '已消除',
    4: '挂起',
}

QUESTION_TYPE = {
    1: '配置问题',
    2: '硬件问题',
    3: '软件问题',
    4: '其他问题',
    5: '电源问题',
    6: '质量问题',
    7: '结构问题',
}
TAB_MAPPING = {
    "operational_history": 1,  # 运营历史记录
    "inspect_history": 2,  # 修程履历表
    "fault_maintenance": 3,  # 故障维修记录
    "health_resume": 4,  # 健康履历
    "component_resume": 5,  # 部件履历
    "soft_hard_config": 6,  # 软硬件配置
    "consum_vulner_replacement": 7,  # 耗材和易损更换记录
    "technical_transform": 8,  # 技术改造项目及资产沉淀
}

TEMPLATE_DIR_MAPPING = {
    1: os.path.join(STATIC_PATH, TEMPLATE_PATH, '运营历史记录模版.xlsx'),
    7: os.path.join(STATIC_PATH, TEMPLATE_PATH, '耗材和易损更换记录模版.xlsx'),
    8: os.path.join(STATIC_PATH, TEMPLATE_PATH, '技术改造项目及资产沉淀模版.xlsx'),
}

IMPORT_COLUMNS_MAPPING = {
    1: {
        '省份': 'province_name',
        '城市': 'city_name',
        '线路': 'line_name',
        '列车号': 'vehicle_number',
        '日期': 'create_time',
        '日行走里程': 'day_distance',
        '日载客运行里程': 'day_passenge_distance',
        '日测试运行里程': 'day_test_distance',
        '日载客人数': 'day_passenge_number',
        '日运行班次数': 'day_run_or_flights_number',
        '日准点率': 'day_punctuality_rate',
        '日误点时长': 'day_delay_duration',
        '日因故中断时长': 'day_interruption_duration'
    },
    7: {
        '省份': 'province_name',
        '城市': 'city_name',
        '线路': 'line_name',
        '列车号': 'vehicle_number',
        '日期': 'replace_time',
        '物料类别': 'material_category',
        '物料名称': 'material_name',
        '物料编号': 'material_code',
        '是否归还': 'is_back',
        '归还时间': 'back_time',
        '规格型号': 'specification',
        '重量': 'weight',
        '品牌': 'brand',
        '单价': 'unit_price',
        '供应商': 'supplier',
        '使用专业': 'use_professional',
        '消耗数量': 'cost_num',
        '消耗总价': 'cost_price',
        '库存总量': 'inventory_total',
    },
    8: {
        '省份': 'province_name',
        '城市': 'city_name',
        '线路': 'line_name',
        '项目号': 'project_code',
        '项目名称': 'project_name',
        '总包单位': 'general_contracting_work_unit',
        '项目起始日期': 'start_time',
        '项目结项日期': 'end_time',
        '项目进程': 'project_schedule',
        '是否续期': 'is_continue',
        '改造说明': 'describe',
        '车型': 'vehicle_category_name',
        '列车号': 'vehicle_number',
        '专业': 'vehicle_professional_name',
        '设备': 'device_name',
        '设备位置': 'device_position',
        '供应商': 'supplier',
        '项目反馈': 'project_feedback',
    }
}

EXPORT_COLUMNS_MAPPING = {
    1: {
        'province_name': '省份',
        'city_name': '城市',
        'line_name': '线路',
        'vehicle_number': '列车号',
        'create_time': '日期',
        'day_distance': '日行走里程',
        'day_passenge_distance': '日载客运行里程',
        'day_test_distance': '日测试运行里程',
        'day_passenge_number': '日载客人数',
        'day_run_or_flights_number': '日运行班次数',
        'day_punctuality_rate': '日准点率',
        'day_delay_duration': '日误点时长',
        'day_interruption_duration': '日因故中断时长'
    },
    2: {
        'vehicle_number': '列车号',
        "inspect_type": "修程方式",
        "periodic_indicators_distance": "周期指标里程（万公里）",
        "periodic_indicator_time_interval": "周期指标时间间隔",
        "start_time": "开始时间",
        "end_time": "结束时间",
        "schedule": "进度",
        "inspect_name": "检修名称",
        "department_name": "职责部门",
        "responsible_shift": "职责工班",
        "responsible_user_name": "总负责人",
        "worker_number": "投入用工人数",
        "cost_person_time": "人时耗用",
        "find_fault_number": "发现故障数",
        "solve_fault_number": "解决故障数",
        "not_solve_work_order_num": "未解决故障单号",
        "find_danger_number": "发现隐患数",
        "solve_danger_number": "消除隐患数",
        "not_solve_danger_num": "未消除隐患单号",
    },
    3: {
        'vehicle_number': '列车号',
        "work_order_id": "工单id",
        "occurrence_time": "故障发生时间",
        "find_type": "发现方式",
        "vehicle_professional_name": "专业",
        "device_name": "设备",
        "device_version": "设备序列号",
        "device_position": "设备位置",
        "mini_replacement_name": "最小可拆换单元",
        "replacement_part_list": "更换件",
        "nums": "件数",
        "fault_category": "问题现象",
        "fault_name": "故障原因",
        "level": "等级",
        "fault_tp": "正线/库内故障",
        "descriptibe": "故障描述",
        "reason_list": "原因分析",
        "repair_place_name": "检修地点",
        "question_tp": "问题种类",
        "hardware_version": "硬件版本号",
        "software_version": "软件版本号",
        "localization_or_outsourcing": "自主化/外购",
        "deal_description": "处置过程",
        "resource_time": "恢复时间",
        "fault_cost_time": "故障下线天数",
        "responsible_department_name": "维修责任部门",
        "responsible_user_name": "维修人员",
        "material_cost": "材料成本（元）",
        "find_department_name": "发现部门",
        "find_user_name": "上报人",
        "find_time": "上报时间",
        "deal_status": "处理状态",
        "update_time": "更新时间",
    },
    4: {
        "vehicle_professional_name": "专业",
        "vehicle_professional_score": "专业分数",
        "device_name": "设备",
        "device_score": "设备分数",
        "create_time": "评分时间"

    },
    5: {
        "vehicle_number": "车辆号",
        "time": "时间",
        "mini_replacement_name": "部件名称",
        "vehicle_professional_name": "所属专业",
        "device_name": "所属设备",
        "device_position": "更换位置",
        "replace_num": "更换数量",
        "replace_reason": "更换原因",
        "cycle_indicator_distance": "周期指标里程(万公里)",
        "cycle_indicator_time": "周期指标时间间隔(年)",
        "department_name": "维修责任部门",
        "maintenance_team": "维修工班",
        "repair_user_name": "修改人员",
        "unit_price": "更换部件单价",
        "total_cost": "更换总成本",
    },
    6: {
        'vehicle_number': '列车号',
        'create_time': '录入系统时间',
        'vehicle_professional_name': '专业',
        'device_name': '设备名称',
        'device_position': '设备位置',
        'mini_replacement_name': '最小可拆换单元',
        'hardware_supplier': '硬件供应商',
        'hardware_version': '硬件序列号',
        'hardware_update_time': '硬件更新时间',
        'software_supplier': '软件供应商',
        'software_version': '软件版本',
        'software_update_time': '软件更新时间',
        'responsible_department_name': '维护部门',
        'responsible_user_name': '维护人员',
    },
    7: {
        'province_name': '省份',
        'city_name': '城市',
        'line_name': '线路',
        'vehicle_number': '列车号',
        'replace_time': '日期',
        'material_category': '物料类别',
        'material_name': '物料名称',
        'material_code': '物料编号',
        'is_back': '是否归还',
        'back_time': '归还时间',
        'specification': '规格型号',
        'weight': '重量',
        'brand': '品牌',
        'unit_price': '单价',
        'supplier': '供应商',
        'use_professional': '使用专业',
        'cost_num': '消耗数量',
        'cost_price': '消耗总价',
        'inventory_total': '库存总量'
    }
    ,
    8: {
        'province_name': '省份',
        'city_name': '城市',
        'line_name': '线路',
        'project_code': '项目号',
        'project_name': '项目名称',
        'general_contracting_work_unit': '总包单位',
        'start_time': '项目起始日期',
        'end_time': '项目结项日期',
        'project_schedule': '项目进程',
        'is_continue': '是否续期',
        'describe': '改造说明',
        'vehicle_category_name': '车型',
        'vehicle_number': '列车号',
        'vehicle_professional_name': '专业',
        'device_name': '设备',
        'device_position': '设备位置',
        'supplier': '供应商',
        'project_feedback': '项目反馈'
    }

}

URL_MAPPING_DICT = {
    1: 'http://{}:{}/archive/operational_history_list?'.format(IP, PORT),
    2: 'http://{}:{}/archive/inspection_history_list?'.format(IP, PORT),
    3: 'http://{}:{}/archive/fault_maintenance_list?'.format(IP, PORT),
    4: 'http://{}:{}/archive/health_resume_list?'.format(IP, PORT),
    5: 'http://{}:{}/archive/component_resume_list?'.format(IP, PORT),
    6: 'http://{}:{}/archive/software_and_hardware_config_list?'.format(IP, PORT),
    7: 'http://{}:{}/archive/consum_and_vulner_replacement?'.format(IP, PORT),
    8: 'http://{}:{}/archive/technical_transformation?'.format(IP, PORT),
}

ATTRIBUTE_DICT = {
    1: 'operational_history_list',
    2: 'inspection_history_list',
    3: 'fault_maintenance_list',
    4: 'health_resume_list',
    5: 'component_resume_list',
    6: 'software_and_hardware_config_list',
    7: 'consum_and_vulner_replacement_list',
    8: 'technical_transformation_list',
}

EXPORT_FILE_NAME = {
    1: '运营历史记录表',
    2: '修程履历表',
    3: '故障维修表',
    4: '健康履历表',
    5: '部件履历表',
    6: '软硬件配置记录表',
    7: '耗材和易损更换记录表',
    8: '技术改造及资产沉淀记录表',
}
