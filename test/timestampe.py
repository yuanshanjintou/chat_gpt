import time

import time

now = float(1694507880)
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

data = [
    {
        "custom_vehicle_category_id": "",
        "custom_vehicle_category_name": "",
        "line_info_list": [
            {
                "line_id": "",
                "line_name": "",
                "vehicle_professional_info_list": [
                    {
                        "vehicle_professional_id": "",
                        "vehicle_professional_name": "",
                        "device_info_list": [
                            {
                                "device_id": "",
                                "device_name": "",
                                "replacement_part_info_list": [
                                    {
                                        "replacement_part_id": "",
                                        "replacement_part_name": ""
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

line_data = [
    {
        "replacement_part_id": "",
        "replacement_part_name": "",
        "score_group_info_list": [
            {
                "model_info_list": [
                    {
                        "expert_model_id": "",
                        "expert_model_name": "",
                        "weight": ""
                    }
                ],
                "weight_device_info_list": [
                    {
                        "vehicle_id": "",
                        "vehicle_number": "",
                        "vehicle_box_list": [
                            {
                                "vehicle_box_id": "",
                                "vehicle_box_name": "",
                                "device_position_list": [
                                    {
                                        "device_id": "",
                                        "device_name": "",
                                        "device_position": "",
                                        "replacement_part_list": [
                                            {
                                                "replacement_part_id": "",
                                                "replacement_part_name": ""
                                            }
                                        ]

                                    }
                                ]

                            }
                        ]

                    }
                ]
            }
        ]
    }
]

can_weight_allocation_list = [
    {
        "group_id": "",
        "vehicle_id": "",
        "vehicle_number": "",
        "vehicle_box_id": "",
        "vehicle_box_name": "",
        "device_id": "",
        "device_name": "",
        "device_position": "",
        "replacement_part_id": "",
        "replacement_part_name": ""
    }
]

param = {
    "score_group_info_list": [
        {
            "model_info_list": [
                {
                    "expert_model_id": "模型",
                    "expert_model_name": "模型名称",
                    "weight": "权重"
                }
            ],
            "weight_device_info_list": [
                {
                    "vehicle_id": "",
                    "vehicle_number": "",
                    "vehicle_box_id": "",
                    "vehicle_box_name": "",
                    "device_id": "",
                    "device_name": "",
                    "device_position": "",
                    "replacement_part_id": "",
                    "replacement_part_name": ""
                }

            ]

        }
    ]
}

score_data = {
    "line_id": "",
    "line_name": "",
    "vehicle_score_info_list": [
        {
            "vehicle_id": "",
            "vehicle_number": "",
            "vehicle_score": "",
            "vehicle_professional_info_list": [
                {
                    "vehicle_processional_id": "",
                    "vehicle_processional_name": "",
                    "vehicle_processional_score": "",
                    "device_info_list": [
                        {
                            "device_id": "",
                            "device_name": "",
                            "device_position": "",
                            "replacement_part_id": "",
                            "replacement_part_name": "",
                            "score": ""
                        }
                    ]
                }
            ]
        }
    ]
}
