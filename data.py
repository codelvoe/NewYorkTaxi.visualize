#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

import json

class SourceDataDemo:

    def __init__(self):
        self.title = '纽约市出租车数据展示'
        self.counter = {'name': '2018年Yellow公司总收入（$）', 'value':1705127784}
        self.counter2 = {'name': '2018年Green公司总收入情况（$）', 'value': 124569303}
        self.echart1_data = {
            'title': 'G 租车区域收入分布($)',
            'data': [
                {"name": "East Harlem", "value": 7443709.18},
                {"name": "Williamsburg", "value": 1167649.57},
                {"name": "Long Insland", "value": 1848194.21},
                {"name": "Brooklyn", "value": 3084665.57},
                {"name": "hamiliton Heights", "value": 2397300.00},
            ]
        }
        self.echart2_data = {
            'title': '总收入行政区分布',
            'data': [
                {"name": "Brooklyn", "value": 5245080},
                {"name": "Queens", "value": 5303500},
                {"name": "Manhattan", "value": 4890600},
                {"name": "Bronx", "value": 2580609},
                {"name": "Staten Island", "value": 1350498}
            ]
        }
        self.echarts3_1_data = {
            'title': '支付偏好',
            'data': [
                {"name": "Credit Card", "value": 5101942},
                {"name": "Cash", "value": 3737631},
                {"name": "No Charge", "value": 40684},
                {"name": "Dispute", "value": 19086},
                {"name": "Unknown", "value": 375}
            ]
        }
        self.echarts3_2_data = {
            'title': '行程类型',
            'data': [
                {"name": "Street-hail", "value": 855521},
                {"name": "Dispatch", "value": 245222}
            ]
        }

        # 极端天气收入影响
        self.echarts3_3_data = {
            'title':'极端天气收入',
            'data':[
                {"name": "ExtreRain", "value": 6000000},
                {"name": "ExtreHeat", "value": 1200000},
                {"name": "ExtreCold", "value": 3000000},
                {"name": "ExtreSnow", "value": 2000000}
            ]
        }

        self.yearly_data = {
            'title': '年度打车数据统计',
            'data': [
                {"year": 2014, "total_trips": 5638910, "average_distance": 2.97, "total_revenue": 82069585.77,
                 "average_passengers": 1.42, "average_duration": "15:22"},
                {"year": 2015, "total_trips": 6464658, "average_distance": 2.87, "total_revenue": 95809666.62,
                 "average_passengers": 1.37, "average_duration": "17.72"},
                {"year": 2016, "total_trips": 5367650, "average_distance": 2.78, "total_revenue": 78463222.27,
                 "average_passengers": 1.35, "average_duration": "22.05"},
                {"year": 2017, "total_trips": 3923809, "average_distance": 2.68, "total_revenue": 56146176.44,
                 "average_passengers": 1.36, "average_duration": "20.50"},
                {"year": 2018, "total_trips": 2976478, "average_distance": 3.36, "total_revenue": 49137348.02,
                 "average_passengers": 1.34, "average_duration": "22.45"}
            ]
        }
        self.echart4_data = {
            'title': '总年份时间趋势',
            'data': [
                {"name": "安卓", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4]},
                {"name": "IOS", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23', '24'],
        }
        #日降雨量与出租车行程数关系（2018年）
        self.rainfall_taxi_trips_2018 = [
            {"Date": "2018-01-05", "Rainfall (inches)": 0.8, "Taxi Trips": 16000},
            {"Date": "2018-01-15", "Rainfall (inches)": 0.0, "Taxi Trips": 22500},
            {"Date": "2018-01-28", "Rainfall (inches)": 1.1, "Taxi Trips": 15500},
            {"Date": "2018-02-06", "Rainfall (inches)": 0.0, "Taxi Trips": 23000},
            {"Date": "2018-02-14", "Rainfall (inches)": 0.5, "Taxi Trips": 19000},
            {"Date": "2018-02-27", "Rainfall (inches)": 0.2, "Taxi Trips": 21500},
            {"Date": "2018-03-03", "Rainfall (inches)": 1.2, "Taxi Trips": 15000},
            {"Date": "2018-03-15", "Rainfall (inches)": 0.4, "Taxi Trips": 21000},
            {"Date": "2018-03-26", "Rainfall (inches)": 0.1, "Taxi Trips": 22000},
            {"Date": "2018-04-08", "Rainfall (inches)": 0.3, "Taxi Trips": 20500},
            {"Date": "2018-04-17", "Rainfall (inches)": 0.9, "Taxi Trips": 17500},
            {"Date": "2018-04-29", "Rainfall (inches)": 0.0, "Taxi Trips": 22500},
            {"Date": "2018-05-10", "Rainfall (inches)": 0.5, "Taxi Trips": 19500},
            {"Date": "2018-05-18", "Rainfall (inches)": 0.3, "Taxi Trips": 21000},
            {"Date": "2018-05-25", "Rainfall (inches)": 0.0, "Taxi Trips": 22000},
            {"Date": "2018-06-05", "Rainfall (inches)": 1.0, "Taxi Trips": 18000},
            {"Date": "2018-06-16", "Rainfall (inches)": 0.2, "Taxi Trips": 21000},
            {"Date": "2018-06-27", "Rainfall (inches)": 0.0, "Taxi Trips": 23000},
            {"Date": "2018-07-06", "Rainfall (inches)": 0.5, "Taxi Trips": 20000},
            {"Date": "2018-07-19", "Rainfall (inches)": 0.1, "Taxi Trips": 22000},
            {"Date": "2018-07-30", "Rainfall (inches)": 0.4, "Taxi Trips": 21000},
            {"Date": "2018-08-09", "Rainfall (inches)": 0.3, "Taxi Trips": 21500},
            {"Date": "2018-08-21", "Rainfall (inches)": 0.0, "Taxi Trips": 23500},
            {"Date": "2018-08-31", "Rainfall (inches)": 1.5, "Taxi Trips": 15500},
            {"Date": "2018-09-12", "Rainfall (inches)": 0.2, "Taxi Trips": 22000},
            {"Date": "2018-09-21", "Rainfall (inches)": 0.7, "Taxi Trips": 18000},
            {"Date": "2018-09-30", "Rainfall (inches)": 0.0, "Taxi Trips": 22500},
            {"Date": "2018-10-10", "Rainfall (inches)": 0.4, "Taxi Trips": 20000},
            {"Date": "2018-10-22", "Rainfall (inches)": 0.6, "Taxi Trips": 19000},
            {"Date": "2018-10-31", "Rainfall (inches)": 0.1, "Taxi Trips": 22000},
            {"Date": "2018-11-09", "Rainfall (inches)": 0.3, "Taxi Trips": 21000},
            {"Date": "2018-11-19", "Rainfall (inches)": 1.0, "Taxi Trips": 17500},
            {"Date": "2018-11-28", "Rainfall (inches)": 0.0, "Taxi Trips": 23000},
            {"Date": "2018-12-05", "Rainfall (inches)": 0.8, "Taxi Trips": 16500},
            {"Date": "2018-12-16", "Rainfall (inches)": 0.0, "Taxi Trips": 22000},
            {"Date": "2018-12-27", "Rainfall (inches)": 0.5, "Taxi Trips": 19000}
        ]
        self.echart5_data = {
            'title': '季节性与出租车消费行为变化',
            'data': [
                {"name": "浙江", "value": 2},
                {"name": "上海", "value": 3},
                {"name": "江苏", "value": 3},
                {"name": "广东", "value": 9},
                {"name": "北京", "value": 15},
                {"name": "深圳", "value": 18},
                {"name": "安徽", "value": 20},
                {"name": "四川", "value": 13},
            ]
        }

        # 日降雪量与出租车行程数关系（2018年）
        self.snowfall_taxi_trips_2018 = [
            {"Date": "2018-01-04", "Snowfall (inches)": 2.5, "Taxi Trips": 12500},
            {"Date": "2018-01-16", "Snowfall (inches)": 0.0, "Taxi Trips": 26000},
            {"Date": "2018-01-28", "Snowfall (inches)": 1.8, "Taxi Trips": 15000},
            {"Date": "2018-02-07", "Snowfall (inches)": 2.0, "Taxi Trips": 12000},
            {"Date": "2018-02-15", "Snowfall (inches)": 0.0, "Taxi Trips": 25000},
            {"Date": "2018-02-25", "Snowfall (inches)": 0.2, "Taxi Trips": 24000},
            {"Date": "2018-03-02", "Snowfall (inches)": 3.1, "Taxi Trips": 11000},
            {"Date": "2018-03-17", "Snowfall (inches)": 0.0, "Taxi Trips": 27000},
            {"Date": "2018-03-28", "Snowfall (inches)": 1.0, "Taxi Trips": 20000},
            {"Date": "2018-04-05", "Snowfall (inches)": 0.0, "Taxi Trips": 28000},
            {"Date": "2018-04-18", "Snowfall (inches)": 0.0, "Taxi Trips": 27500},
            {"Date": "2018-04-27", "Snowfall (inches)": 0.0, "Taxi Trips": 29000},
            {"Date": "2018-05-05", "Snowfall (inches)": 0.0, "Taxi Trips": 30000},
            {"Date": "2018-05-14", "Snowfall (inches)": 0.0, "Taxi Trips": 29000},
            {"Date": "2018-05-25", "Snowfall (inches)": 0.0, "Taxi Trips": 30500},
            {"Date": "2018-06-05", "Snowfall (inches)": 0.0, "Taxi Trips": 31000},
            {"Date": "2018-06-16", "Snowfall (inches)": 0.0, "Taxi Trips": 32000},
            {"Date": "2018-06-26", "Snowfall (inches)": 0.0, "Taxi Trips": 31500},
            {"Date": "2018-07-06", "Snowfall (inches)": 0.0, "Taxi Trips": 32000},
            {"Date": "2018-07-19", "Snowfall (inches)": 0.0, "Taxi Trips": 33000},
            {"Date": "2018-07-30", "Snowfall (inches)": 0.0, "Taxi Trips": 32500},
            {"Date": "2018-08-06", "Snowfall (inches)": 0.0, "Taxi Trips": 34000},
            {"Date": "2018-08-19", "Snowfall (inches)": 0.0, "Taxi Trips": 34500},
            {"Date": "2018-08-30", "Snowfall (inches)": 0.0, "Taxi Trips": 35000},
            {"Date": "2018-09-09", "Snowfall (inches)": 0.0, "Taxi Trips": 34500},
            {"Date": "2018-09-20", "Snowfall (inches)": 0.0, "Taxi Trips": 34000},
            {"Date": "2018-09-29", "Snowfall (inches)": 0.0, "Taxi Trips": 35000},
            {"Date": "2018-10-08", "Snowfall (inches)": 0.0, "Taxi Trips": 35500},
            {"Date": "2018-10-18", "Snowfall (inches)": 0.0, "Taxi Trips": 35000},
            {"Date": "2018-10-29", "Snowfall (inches)": 0.0, "Taxi Trips": 36000},
            {"Date": "2018-11-07", "Snowfall (inches)": 0.0, "Taxi Trips": 34500},
            {"Date": "2018-11-17", "Snowfall (inches)": 0.0, "Taxi Trips": 35000},
            {"Date": "2018-11-27", "Snowfall (inches)": 0.0, "Taxi Trips": 34000},
            {"Date": "2018-12-04", "Snowfall (inches)": 1.2, "Taxi Trips": 22000},
            {"Date": "2018-12-15", "Snowfall (inches)": 0.0, "Taxi Trips": 32000},
            {"Date": "2018-12-26", "Snowfall (inches)": 1.0, "Taxi Trips": 23000}
        ]


        self.echart6_data = {
            'title': '各字段相关性',
            'data': [
                {"name": "二月", "value": 80, "value2": 20, "color": "01", "radius": ['59%', '70%']},
                {"name": "四月", "value": 70, "value2": 30, "color": "02", "radius": ['49%', '60%']},
                {"name": "六月", "value": 65, "value2": 35, "color": "03", "radius": ['39%', '50%']},
                {"name": "北京", "value": 60, "value2": 40, "color": "04", "radius": ['29%', '40%']},
                {"name": "深圳", "value": 50, "value2": 50, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '海门', 'value': 239},
                {'name': '鄂尔多斯', 'value': 231},
                {'name': '招远', 'value': 203},
            ]
        }

        self.yellow_monthly_data = {
            'title': 'Yellow公司2018年每月打车数据',
            'data': [
                {"Month": 1, "Rides": 8760687, "Total Revenue": "$135,712,580.38"},
                {"Month": 2, "Rides": 8492819, "Total Revenue": "$131,435,642.00"},
                {"Month": 3, "Rides": 9431289, "Total Revenue": "$150,573,218.56"},
                {"Month": 4, "Rides": 9306216, "Total Revenue": "$152,091,278.89"},
                {"Month": 5, "Rides": 9224788, "Total Revenue": "$155,091,939.66"},
                {"Month": 6, "Rides": 8714667, "Total Revenue": "$145,188,446.31"},
                {"Month": 7, "Rides": 7851143, "Total Revenue": "$130,239,543.00"},
                {"Month": 8, "Rides": 7855040, "Total Revenue": "$130,617,593.38"},
                {"Month": 9, "Rides": 8049094, "Total Revenue": "$135,641,084.25"},
                {"Month": 10, "Rides": 8834520, "Total Revenue": "$150,255,119.56"},
                {"Month": 11, "Rides": 8155449, "Total Revenue": "$137,269,075.00"},
                {"Month": 12, "Rides": 8195675, "Total Revenue": "$136,160,866.88"}
            ]
        }
        # Green公司2018年每月数据
        self.green_monthly_data = {
            'title': 'Green公司2018年每月打车数据',
            'data': [
                {"Month": 1, "Rides": 792809, "Avg Spending": "$14.00"},
                {"Month": 2, "Rides": 769067, "Avg Spending": "$14.15"},
                {"Month": 3, "Rides": 836070, "Avg Spending": "$14.91"},
                {"Month": 4, "Rides": 799424, "Avg Spending": "$15.48"},
                {"Month": 5, "Rides": 796602, "Avg Spending": "$16.09"},
                {"Month": 6, "Rides": 738525, "Avg Spending": "$16.25"},
                {"Month": 7, "Rides": 684361, "Avg Spending": "$16.06"},
                {"Month": 8, "Rides": 675764, "Avg Spending": "$16.66"},
                {"Month": 9, "Rides": 682201, "Avg Spending": "$17.33"},
                {"Month": 10, "Rides": 731860, "Avg Spending": "$17.61"},
                {"Month": 11, "Rides": 673312, "Avg Spending": "$17.49"},
                {"Month": 12, "Rides": 719723, "Avg Spending": "$17.86"}
            ]
        }
        # 字段相关性补充完整
        self.feature_correlation = {
            'title': '字段相关性',
            'data': [
                {"name": "VendorID",
                 "values": [1.000, 0.014, 0.001, -0.001, 0.081, 0.040, 0.052, 0.011, -0.003, -0.066, 0.022, -0.048,
                            0.042, -0.074, 0.021]},
                {"name": "RatecodeID",
                 "values": [0.014, 1.000, 0.049, 0.017, -0.026, 0.105, 0.132, -0.110, -0.471, -0.021, 0.066, -0.652,
                            0.115, -0.025, 0.880]},
                {"name": "PULocationID",
                 "values": [0.001, 0.049, 1.000, 0.139, 0.011, 0.052, 0.053, 0.020, -0.043, 0.019, 0.027, -0.048, 0.054,
                            -0.020, 0.050]},
                {"name": "DOLocationID",
                 "values": [-0.001, 0.017, 0.139, 1.000, 0.008, 0.056, 0.060, -0.008, -0.008, 0.070, 0.022, -0.007,
                            0.067, -0.038, 0.013]},
                {"name": "passenger_count",
                 "values": [0.081, -0.026, 0.011, 0.008, 1.000, -0.007, -0.008, -0.013, 0.002, 0.005, -0.001, 0.037,
                            -0.007, 0.003, -0.028]},
                {"name": "trip_distance",
                 "values": [0.040, 0.105, 0.052, 0.056, -0.007, 1.000, 0.689, 0.040, 0.024, 0.172, 0.336, -0.122, 0.693,
                            -0.175, 0.094]},
                {"name": "fare_amount",
                 "values": [0.052, 0.132, 0.053, 0.060, -0.008, 0.689, 1.000, 0.086, 0.099, 0.190, 0.341, -0.163, 0.985,
                            -0.216, 0.115]},
                {"name": "extra",
                 "values": [0.011, -0.110, 0.020, -0.008, -0.013, 0.040, 0.086, 1.000, 0.106, -0.000, 0.025, -0.144,
                            0.116, -0.040, -0.119]},
                {"name": "mta_tax",
                 "values": [-0.003, -0.471, -0.043, -0.008, 0.002, 0.024, 0.099, 0.106, 1.000, 0.012, -0.009, 0.668,
                            0.106, -0.138, -0.533]},
                {"name": "tip_amount",
                 "values": [-0.066, -0.021, 0.019, 0.070, 0.005, 0.172, 0.190, -0.000, 0.012, 1.000, 0.109, 0.069,
                            0.330, -0.423, -0.040]},
                {"name": "tolls_amount",
                 "values": [0.022, 0.066, 0.027, 0.022, -0.001, 0.336, 0.341, 0.025, -0.009, 0.109, 1.000, -0.070,
                            0.418, -0.082, 0.050]},
                {"name": "improvement_surcharge",
                 "values": [-0.048, -0.652, -0.048, -0.007, 0.037, -0.122, -0.163, -0.144, 0.668, 0.069, -0.070, 1.000,
                            -0.143, -0.021, -0.736]},
                {"name": "total_amount",
                 "values": [0.042, 0.115, 0.054, 0.067, -0.007, 0.693, 0.985, 0.116, 0.106, 0.330, 0.418, -0.143, 1.000,
                            -0.271, 0.094]},
                {"name": "payment_type",
                 "values": [-0.074, -0.025, -0.020, -0.038, 0.003, -0.175, -0.216, -0.040, -0.138, -0.423, -0.082,
                            -0.021, -0.271, 1.000, -0.022]},
                {"name": "trip_type",
                 "values": [0.021, 0.880, 0.050, 0.013, -0.028, 0.094, 0.115, -0.119, -0.533, -0.040, 0.050, -0.736,
                            0.094, -0.022, 1.000]}
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    # def echarts3_3(self):
    #     data = self.echarts3_3_data
    #     echart = {
    #         'title': data.get('title'),
    #         'xAxis': [i.get("name") for i in data.get('data')],
    #         'data': data.get('data'),
    #     }
    #     return echart
    def echarts_01(self):
        data = self.yearly_data  # 使用新的数据类型 self.yearly_data
        echart_data = []
        for item in data.get('data'):
            echart_data.append({
                'year': item.get('year'),
                'total_trips': item.get('total_trips'),
                'average_distance': item.get('average_distance'),
                'total_revenue': item.get('total_revenue'),
                'average_passengers': item.get('average_passengers'),
                'average_duration': item.get('average_duration')
            })
        echart = {
            'title': data.get('title'),
            'data': echart_data
        }
        return echart
    #
    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart
    # def echart4(self):
    #     # 日降雨量与出租车行程数关系数据
    #     rainfall_data = self.rainfall_taxi_trips_2018
    #     dates = [item['Date'] for item in rainfall_data]
    #     rainfalls = [item['Rainfall (inches)'] for item in rainfall_data]
    #     taxi_trips = [item['Taxi Trips'] for item in rainfall_data]
    #
    #     echart = {
    #         'title': '日降雨量与出租车行程数关系（2018年）',
    #         'names': ['Rainfall (inches)', 'Taxi Trips'],
    #         'xAxis': dates,
    #         'data': [
    #             {'name': 'Rainfall (inches)', 'value': rainfalls, 'type': 'bar'},
    #             {'name': 'Taxi Trips', 'value': taxi_trips, 'type': 'line'}
    #         ],
    #     }
    #     return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart
    # def echart5(self):
    #     # 日降雪量与出租车行程数关系数据
    #     snowfall_data = self.snowfall_taxi_trips_2018
    #     dates = [item['Date'][5:] for item in snowfall_data]  # 提取 MM-DD 格式
    #     snowfalls = [item['Snowfall (inches)'] for item in snowfall_data]
    #     taxi_trips = [item['Taxi Trips'] for item in snowfall_data]
    #
    #     echart = {
    #         'title': '日降雪量与出租车行程数关系（2018年）',
    #         'names': ['Snowfall (inches)', 'Taxi Trips'],
    #         'xAxis': dates,
    #         'data': [
    #             {'name': 'Snowfall (inches)', 'value': snowfalls, 'type': 'bar'},
    #             {'name': 'Taxi Trips', 'value': taxi_trips, 'type': 'line'}
    #         ],
    #     }
    #     return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '大数据可视化展板通用模板'

class CorpData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('corp.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')

class JobData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('job.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')